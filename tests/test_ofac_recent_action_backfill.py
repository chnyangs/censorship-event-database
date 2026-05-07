# SPDX-License-Identifier: MIT
"""Regression guards for OFAC recent-action candidate materialization."""
from __future__ import annotations

import json
import textwrap

import yaml

import pytest

from materialize_ofac_recent_action_candidates import materialize_candidates


def _write(path, body: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(textwrap.dedent(body).strip() + "\n")


def test_ofac_recent_action_backfill_promotes_existing_event_and_rejects_out_of_scope(tmp_path):
    triage_path = tmp_path / "triage.json"
    events_dir = tmp_path / "events"
    candidate_dir = tmp_path / "candidate_triggers"
    triage_path.write_text(
        json.dumps(
            [
                {
                    "date": "20240220",
                    "status": "addresses_present",
                    "title_listing": "Cyber-related Designations",
                    "page_title": "Cyber-related Designations | Office of Foreign Assets Control",
                    "total_crypto_addresses": 2,
                    "addresses_by_token": {"ETH": 2},
                    "entity_keyword_hits": ["ransomware"],
                },
                {
                    "date": "20240101",
                    "status": "no_crypto_content",
                    "title_listing": "Cyber-related Designations",
                    "page_title": "Cyber-related Designations | Office of Foreign Assets Control",
                    "total_crypto_addresses": 0,
                    "addresses_by_token": {},
                    "entity_keyword_hits": [],
                },
            ]
        )
    )
    _write(
        events_dir / "existing.yaml",
        """
        id: existing-ofac-event
        status: admitted
        research_stratum: S1_ofac_sdn
        trigger:
          type: ofac_sdn_designation
          actor: US_OFAC
          timestamp: 2024-02-20T00:00:00Z
          timestamp_precision: day
        """,
    )

    written = materialize_candidates(triage_path, events_dir, candidate_dir)

    assert len(written) == 2
    promoted = yaml.safe_load((candidate_dir / "ofac-recent-action-20240220.yaml").read_text())
    screened = yaml.safe_load(
        (candidate_dir / "rejected" / "ofac-recent-action-20240101.yaml").read_text()
    )
    assert promoted["registry_status"] == "promoted_to_event"
    assert promoted["promoted_event_id"] == ["existing-ofac-event"]
    assert promoted["target"]["chains"] == ["ethereum"]
    assert screened["registry_status"] == "screened_no_extractor_target"
    assert "target" not in screened


def test_ofac_recent_action_backfill_marks_unpromoted_address_row_candidate(tmp_path):
    triage_path = tmp_path / "triage.json"
    events_dir = tmp_path / "events"
    candidate_dir = tmp_path / "candidate_triggers"
    triage_path.write_text(
        json.dumps(
            [
                {
                    "date": "20240111",
                    "status": "addresses_present",
                    "title_listing": "Russia-related Designations; Cyber-related Designation Update",
                    "page_title": "Cyber-related Designation Update | Office of Foreign Assets Control",
                    "total_crypto_addresses": 3,
                    "addresses_by_token": {"XBT": 1, "USDT": 2},
                    "entity_keyword_hits": ["chatex"],
                }
            ]
        )
    )

    materialize_candidates(triage_path, events_dir, candidate_dir)

    candidate = yaml.safe_load((candidate_dir / "ofac-recent-action-20240111.yaml").read_text())
    assert candidate["registry_status"] == "candidate"
    assert candidate["research_stratum"] == "S1_ofac_sdn"
    assert candidate["target"]["kind"] == "address_set"
    assert candidate["target"]["chains"] == ["bitcoin", "ethereum", "tron"]


def test_ofac_backfill_fails_on_cross_directory_duplicate(tmp_path):
    triage_path = tmp_path / "triage.json"
    events_dir = tmp_path / "events"
    candidate_dir = tmp_path / "candidate_triggers"
    triage_path.write_text(
        json.dumps(
            [
                {
                    "date": "20240101",
                    "status": "no_crypto_content",
                    "title_listing": "Cyber-related Designations",
                    "page_title": "Cyber-related Designations | Office of Foreign Assets Control",
                    "total_crypto_addresses": 0,
                    "addresses_by_token": {},
                    "entity_keyword_hits": [],
                }
            ]
        )
    )
    _write(
        candidate_dir / "ofac-recent-action-20240101.yaml",
        """
        id: ofac-recent-action-20240101
        registry_status: candidate
        research_stratum: S1_ofac_sdn
        target: {kind: entity}
        """,
    )

    with pytest.raises(SystemExit):
        materialize_candidates(triage_path, events_dir, candidate_dir)
