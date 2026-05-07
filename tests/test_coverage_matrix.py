# SPDX-License-Identifier: MIT
"""Regression guards for denominator-aware coverage matrix generation."""
from __future__ import annotations

import textwrap

import pytest

from build_coverage_matrix import build_rows, denominator_class


def _write_event(events_dir, body: str) -> None:
    events_dir.mkdir()
    (events_dir / "synthetic-event.yaml").write_text(textwrap.dedent(body).strip() + "\n")


def test_denominator_class_retracts_l3_and_asset_rates():
    assert denominator_class("l3_rpc", "partially_measured") == "named_partial_only_no_conditional_rate"
    assert (
        denominator_class("asset_onchain", "measured")
        == "descriptive_only_structural_circularity_v0_1"
    )
    assert denominator_class("l0_network", "not_measured") == "observability_gap"


def test_coverage_matrix_emits_one_row_per_layer_with_counts(tmp_path):
    events_dir = tmp_path / "events"
    _write_event(
        events_dir,
        """
        id: synthetic-event
        status: admitted
        research_stratum: S1_ofac_sdn
        admission_tier: empirical_case
        trigger:
          type: ofac_sdn_designation
        jurisdiction: [US]
        coverage:
          - {layer: l0_network, status: not_measured}
          - {layer: l1_consensus, status: not_applicable}
          - {layer: l3_rpc, status: partially_measured}
          - {layer: l4_frontend, status: measured}
          - {layer: asset_onchain, status: measured}
          - {layer: offramp_cex, status: partially_measured}
        observations:
          - layer: l4_frontend
            observation_kind: observed_change
            attribution: direct
            timestamp: 2024-01-01T00:00:00Z
          - layer: asset_onchain
            observation_kind: observed_change
            attribution: plausible
            timestamp: 2024-01-01T00:01:00Z
        """,
    )

    rows = build_rows(events_dir)

    assert len(rows) == 6
    by_layer = {row["layer"]: row for row in rows}
    assert by_layer["l4_frontend"]["denominator_class"] == "measured_rate_denominator"
    assert by_layer["l4_frontend"]["rate_reportable"] == "yes"
    assert by_layer["l4_frontend"]["observed_change_count"] == 1
    assert by_layer["l4_frontend"]["direct_attribution_count"] == 1
    assert by_layer["asset_onchain"]["denominator_class"] == (
        "descriptive_only_structural_circularity_v0_1"
    )
    assert by_layer["l3_rpc"]["denominator_class"] == "named_partial_only_no_conditional_rate"
    assert by_layer["l3_rpc"]["rate_reportable"] == "no"
    assert "provider_universe" in by_layer["l3_rpc"]["denominator_reason"]
    assert by_layer["l0_network"]["denominator_reason"] == "not_queried_yet; cp_not_ingested_v0_1"


def test_coverage_matrix_fails_closed_on_missing_layer(tmp_path):
    events_dir = tmp_path / "events"
    _write_event(
        events_dir,
        """
        id: synthetic-event
        status: admitted
        research_stratum: S1_ofac_sdn
        admission_tier: empirical_case
        trigger:
          type: ofac_sdn_designation
        jurisdiction: [US]
        coverage:
          - {layer: l0_network, status: not_measured}
        observations: []
        """,
    )

    with pytest.raises(SystemExit):
        build_rows(events_dir)
