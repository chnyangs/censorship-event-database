# SPDX-License-Identifier: MIT
"""Regression guards for sampling-frame trigger registry generation."""
from __future__ import annotations

import textwrap

import pytest

from build_trigger_registry import build_registry


FRAME = """
schema_version: 0.1.0
snapshot_scope:
  candidate_trigger_registry_target_min: 2
  candidate_trigger_registry_target_max: 4
  admitted_event_target_min: 1
  admitted_event_target_max: 2
trigger_registry_statuses:
  - admitted
  - draft
  - candidate
  - promoted_to_event
  - screened_no_extractor_target
  - rejected_out_of_scope
strata:
  S1_ofac_sdn:
    v0_2_admitted_min: 1
    v0_2_candidate_min: 1
target_kinds:
  - address_set
  - entity
"""


def _write(path, body: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(textwrap.dedent(body).strip() + "\n")


def test_trigger_registry_includes_event_and_candidate_rows(tmp_path):
    events_dir = tmp_path / "events"
    candidates_dir = tmp_path / "candidate_triggers"
    frame_path = tmp_path / "frame.yaml"
    _write(frame_path, FRAME)
    _write(
        events_dir / "admitted.yaml",
        """
        id: admitted-event
        status: admitted
        research_stratum: S1_ofac_sdn
        empirical_shape: comparison
        admission_tier: empirical_case
        trigger:
          type: ofac_sdn_designation
          actor: US_OFAC
          timestamp: 2024-01-01T00:00:00Z
          timestamp_precision: day
        target:
          kind: address_set
          chains: [ethereum]
        jurisdiction: [US]
        coverage:
          - {layer: l0_network, status: not_measured}
          - {layer: l1_consensus, status: not_applicable}
          - {layer: l3_rpc, status: not_measured}
          - {layer: l4_frontend, status: measured}
          - {layer: asset_onchain, status: measured}
          - {layer: offramp_cex, status: not_applicable}
        observations:
          - {layer: l4_frontend, observation_kind: observed_change}
        """,
    )
    _write(
        candidates_dir / "2026-01-01-new-trigger.yaml",
        """
        id: new-trigger
        registry_status: candidate
        research_stratum: S1_ofac_sdn
        trigger:
          type: ofac_sdn_designation
          actor: US_OFAC
          timestamp: 2026-01-01T00:00:00Z
          timestamp_precision: day
        target:
          kind: entity
          chains: [bitcoin]
        jurisdiction: [US]
        triage_notes: needs evidence collection
        """,
    )

    _frame, rows = build_registry(events_dir, candidates_dir, frame_path)

    assert [row["trigger_id"] for row in rows] == ["admitted-event", "new-trigger"]
    assert rows[0]["registry_status"] == "admitted"
    assert rows[0]["source_frame_id"] == "legacy_v0_1_event_yaml"
    assert rows[0]["frame_unit_id"].startswith("legacy_v0_1_event_yaml:admitted-event")
    assert rows[0]["coverage_measured_layers"] == "asset_onchain,l4_frontend"
    assert rows[1]["source_type"] == "candidate_trigger"


def test_trigger_registry_fails_on_unknown_candidate_status(tmp_path):
    events_dir = tmp_path / "events"
    candidates_dir = tmp_path / "candidate_triggers"
    frame_path = tmp_path / "frame.yaml"
    _write(frame_path, FRAME)
    _write(
        candidates_dir / "bad.yaml",
        """
        id: bad-trigger
        registry_status: unknown_status
        research_stratum: S1_ofac_sdn
        target: {kind: entity}
        """,
    )

    with pytest.raises(SystemExit):
        build_registry(events_dir, candidates_dir, frame_path)


def test_trigger_registry_keeps_promoted_candidate_event_link(tmp_path):
    events_dir = tmp_path / "events"
    candidates_dir = tmp_path / "candidate_triggers"
    frame_path = tmp_path / "frame.yaml"
    _write(frame_path, FRAME)
    for event_id in ("event-a", "event-b"):
        _write(
            events_dir / f"{event_id}.yaml",
            f"""
            id: {event_id}
            status: admitted
            research_stratum: S1_ofac_sdn
            target: {{kind: address_set}}
            trigger:
              type: ofac_sdn_designation
              actor: US_OFAC
              timestamp: 2024-01-01T00:00:00Z
              timestamp_precision: day
            """,
        )
    _write(
        candidates_dir / "promoted.yaml",
        """
        id: promoted-trigger
        registry_status: promoted_to_event
        promoted_event_id: [event-a, event-b]
        research_stratum: S1_ofac_sdn
        trigger:
          type: ofac_sdn_designation
          actor: US_OFAC
          timestamp: 2024-01-01T00:00:00Z
          timestamp_precision: day
        target: {kind: address_set, chains: [ethereum]}
        """,
    )

    _frame, rows = build_registry(events_dir, candidates_dir, frame_path)

    promoted = next(row for row in rows if row["trigger_id"] == "promoted-trigger")
    assert promoted["registry_status"] == "promoted_to_event"
    assert promoted["event_id"] == "event-a,event-b"


def test_trigger_registry_fails_on_missing_promoted_event_link(tmp_path):
    events_dir = tmp_path / "events"
    candidates_dir = tmp_path / "candidate_triggers"
    frame_path = tmp_path / "frame.yaml"
    _write(frame_path, FRAME)
    _write(
        candidates_dir / "promoted.yaml",
        """
        id: promoted-trigger
        registry_status: promoted_to_event
        promoted_event_id: [missing-event]
        research_stratum: S1_ofac_sdn
        trigger:
          type: ofac_sdn_designation
          actor: US_OFAC
          timestamp: 2024-01-01T00:00:00Z
          timestamp_precision: day
        target: {kind: address_set, chains: [ethereum]}
        """,
    )

    with pytest.raises(SystemExit):
        build_registry(events_dir, candidates_dir, frame_path)
