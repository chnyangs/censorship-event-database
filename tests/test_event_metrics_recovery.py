# SPDX-License-Identifier: MIT
"""Lock the recovery-row filter (post-2026-04-23 P2 fix).

A recovery row on a layer that is NOT in `changed_layers` must be ignored:
otherwise `recovered_count + unrecovered_count + recovery_unknown_count`
can exceed `changed_layer_count`. This was the tornado-cash-ofac-delisting
bug where an `l3_rpc` resolved=false row (under observed_no_change coverage)
inflated the sum.
"""
from __future__ import annotations

from build_event_metrics import compute_event_metrics


def _event_with_recovery(
    changed_layers: list[str],
    recovery_rows: list[dict],
) -> dict:
    return {
        "id": "test-synth",
        "trigger": {"type": "ofac_sdn_designation", "timestamp": "2022-08-08T13:30:00Z"},
        "target": {"kind": "address_set"},
        "coverage": [
            {"layer": lyr, "status": "measured"}
            for lyr in ["l3_rpc", "l4_frontend", "asset_onchain"]
        ],
        "observations": [
            {
                "layer": lyr,
                "observation_kind": "observed_change",
                "attribution": "direct",
                "timestamp": "2022-08-08T18:00:00Z",
                "delta_hours": 4.5,
            }
            for lyr in changed_layers
        ],
        "recovery": recovery_rows,
    }


def test_recovery_on_changed_layer_counted():
    m = compute_event_metrics(_event_with_recovery(
        changed_layers=["asset_onchain"],
        recovery_rows=[{"layer": "asset_onchain", "resolved": True}],
    ))
    assert m["recovered_layer_count"] == 1
    assert m["unrecovered_layer_count"] == 0
    assert m["recovery_unknown_layer_count"] == 0


def test_recovery_on_non_changed_layer_ignored():
    """P2 regression guard: l3_rpc recovery on an event that did not observe
    change at l3_rpc must NOT inflate the recovery tallies."""
    m = compute_event_metrics(_event_with_recovery(
        changed_layers=["asset_onchain", "l4_frontend"],
        recovery_rows=[
            {"layer": "asset_onchain", "resolved": True},
            {"layer": "l3_rpc",        "resolved": False},   # NOT in changed_layers
        ],
    ))
    total = (
        m["recovered_layer_count"]
        + m["unrecovered_layer_count"]
        + m["recovery_unknown_layer_count"]
    )
    assert total == m["changed_layer_count"] == 2
    # per-layer drill-down should show l3_rpc.resolved as None (not False)
    assert m["per_layer"]["l3_rpc"]["resolved"] is None
    assert m["per_layer"]["asset_onchain"]["resolved"] is True
    assert m["per_layer"]["l4_frontend"]["resolved"] is None


def test_recovery_sum_never_exceeds_changed_layer_count():
    """Hard invariant: recovered + unrecovered + unknown == changed_layer_count."""
    m = compute_event_metrics(_event_with_recovery(
        changed_layers=["asset_onchain", "l1_consensus", "l4_frontend"],
        recovery_rows=[
            {"layer": "asset_onchain",   "resolved": False},
            {"layer": "l3_rpc",          "resolved": False},  # ignored
            {"layer": "offramp_cex",     "resolved": True},   # ignored
        ],
    ))
    total = (
        m["recovered_layer_count"]
        + m["unrecovered_layer_count"]
        + m["recovery_unknown_layer_count"]
    )
    assert total == m["changed_layer_count"]


def test_cascade_breadth_is_coverage_matched():
    event = {
        "id": "breadth-synth",
        "trigger": {"type": "ofac_sdn_designation", "timestamp": "2024-01-01T00:00:00Z"},
        "target": {"kind": "entity"},
        "coverage": [
            {"layer": "l0_network", "status": "not_measured"},
            {"layer": "l4_frontend", "status": "measured"},
            {"layer": "offramp_cex", "status": "not_applicable"},
        ],
        "observations": [
            {
                "layer": "l4_frontend",
                "observation_kind": "observed_change",
                "attribution": "direct",
                "timestamp": "2024-01-01T01:00:00Z",
            }
        ],
    }
    m = compute_event_metrics(event)
    assert m["coverage_denominator_layer_count"] == 1
    assert m["non_na_layer_count"] == 2
    assert m["applicable_layer_count"] == 1
    assert m["coverage_matched_changed_layer_count"] == 1
    assert m["cascade_breadth"] == 1.0
    assert m["non_na_cascade_breadth"] is None


def test_unmeasured_changed_layer_does_not_enter_coverage_matched_breadth():
    event = {
        "id": "unmeasured-change-synth",
        "trigger": {"type": "ofac_sdn_designation", "timestamp": "2024-01-01T00:00:00Z"},
        "target": {"kind": "entity"},
        "coverage": [
            {"layer": "l0_network", "status": "not_measured"},
            {"layer": "l4_frontend", "status": "measured"},
        ],
        "observations": [
            {
                "layer": "l0_network",
                "observation_kind": "observed_change",
                "attribution": "plausible",
                "timestamp": "2024-01-01T01:00:00Z",
            }
        ],
    }
    m = compute_event_metrics(event)
    assert m["changed_layer_count"] == 1
    assert m["coverage_matched_changed_layer_count"] == 0
    assert m["coverage_denominator_layer_count"] == 1
    assert m["cascade_breadth"] == 0.0
    assert m["non_na_cascade_breadth"] is None
