# SPDX-License-Identifier: MIT
"""Regression guards for the 2008+ temporal discovery ledger."""
from __future__ import annotations

import textwrap

from build_temporal_discovery_ledger import build_ledger


FRAME = """
schema_version: 0.1.0
snapshot_scope:
  historical_start: 2008-01-01
temporal_tiers:
  discovery_only_2008_2012:
    date_range: [2008-01-01, 2012-12-31]
    analysis_use: discovery_ledger_only
    default_month_status: pending
  historical_baseline_2013_2016:
    date_range: [2013-01-01, 2016-12-31]
    analysis_use: historical_baseline
    default_month_status: pending
  comparable_main_2017_present:
    date_range: [2017-01-01, 2026-12-31]
    analysis_use: comparable_analysis
    default_month_status: pending
source_frames:
  ofac:
    source_frame_id: ofac_recent_actions_crypto_2017_2026
  federal:
    source_frame_id: us_federal_enforcement_crypto_2017_2026
"""


def _write(path, body: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(textwrap.dedent(body).strip() + "\n")


def _patch_meta(monkeypatch, cutoff: str) -> None:
    monkeypatch.setattr(
        "build_temporal_discovery_ledger.load_meta",
        lambda: {"dataset_version": "test", "cutoff_date": cutoff, "source_commit": "test"},
    )


def test_temporal_ledger_has_complete_source_frame_month_grid(tmp_path, monkeypatch):
    frame_path = tmp_path / "frame.yaml"
    events_dir = tmp_path / "events"
    candidates_dir = tmp_path / "candidate_triggers"
    triage_dir = tmp_path / "triage"
    _write(frame_path, FRAME)
    _patch_meta(monkeypatch, "2008-03-15")

    _frame, rows = build_ledger(events_dir, candidates_dir, frame_path, triage_dir)

    assert len(rows) == 6
    assert {
        (row["source_frame_id"], row["discovery_month"])
        for row in rows
    } == {
        ("ofac_recent_actions_crypto_2017_2026", "2008-01"),
        ("ofac_recent_actions_crypto_2017_2026", "2008-02"),
        ("ofac_recent_actions_crypto_2017_2026", "2008-03"),
        ("us_federal_enforcement_crypto_2017_2026", "2008-01"),
        ("us_federal_enforcement_crypto_2017_2026", "2008-02"),
        ("us_federal_enforcement_crypto_2017_2026", "2008-03"),
    }
    assert {row["ledger_status"] for row in rows} == {"pending"}
    assert {row["temporal_tier"] for row in rows} == {"discovery_only_2008_2012"}


def test_temporal_ledger_marks_event_month_as_candidate_found(tmp_path, monkeypatch):
    frame_path = tmp_path / "frame.yaml"
    events_dir = tmp_path / "events"
    candidates_dir = tmp_path / "candidate_triggers"
    triage_dir = tmp_path / "triage"
    _write(
        frame_path,
        FRAME.replace("historical_start: 2008-01-01", "historical_start: 2017-01-01"),
    )
    _patch_meta(monkeypatch, "2017-01-31")
    _write(
        events_dir / "alphabay.yaml",
        """
        id: alphabay
        status: observation_closed
        research_stratum: S3_doj_sec_cftc_fiod
        trigger:
          type: doj_seizure_order
          actor: US_DOJ
          timestamp: 2017-01-20T00:00:00Z
        target: {kind: entity}
        """,
    )

    _frame, rows = build_ledger(events_dir, candidates_dir, frame_path, triage_dir)

    federal = next(
        row for row in rows
        if row["source_frame_id"] == "us_federal_enforcement_crypto_2017_2026"
    )
    assert federal["ledger_status"] == "candidate_found"
    assert federal["event_ids"] == "alphabay"
    assert federal["temporal_tier"] == "comparable_main_2017_present"
    assert federal["analysis_use"] == "comparable_analysis"


def test_temporal_ledger_uses_triage_manifest_status(tmp_path, monkeypatch):
    frame_path = tmp_path / "frame.yaml"
    events_dir = tmp_path / "events"
    candidates_dir = tmp_path / "candidate_triggers"
    triage_dir = tmp_path / "triage"
    _write(frame_path, FRAME)
    _patch_meta(monkeypatch, "2008-01-31")
    _write(
        triage_dir / "official-archives.csv",
        """
        source_frame_id,discovery_month,screening_status,screening_reason
        ofac_recent_actions_crypto_2017_2026,2008-01,not_applicable_pre_market,No official crypto target frame for this month.
        """,
    )

    _frame, rows = build_ledger(events_dir, candidates_dir, frame_path, triage_dir)

    ofac = next(
        row for row in rows
        if row["source_frame_id"] == "ofac_recent_actions_crypto_2017_2026"
    )
    assert ofac["ledger_status"] == "not_applicable_pre_market"
    assert ofac["triage_rows"] == "1"
    assert "No official crypto target frame" in ofac["notes"]
