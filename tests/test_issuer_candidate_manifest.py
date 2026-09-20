# SPDX-License-Identifier: MIT
import json
import pytest

from prepare_issuer_candidate_manifest import (
    build_units, classify_source_rows, sha, verify_bundle, window_for_day, write_frozen,
)


def row(**changes):
    data = {"action_url": "https://ofac.treasury.gov/recent-actions/20220405", "action_slug": "20220405",
            "normalized_address": "0x" + "a" * 40, "proposed_action_type": "addition", "proposed_list_scope": "sdn",
            "chain_marker": "ETH", "release_date": "2022-04-05", "date_candidate": "2022-04-05",
            "target_entry_prefix_candidate": "EXCHANGE", "entry_text": "EXCHANGE; Digital Currency Address - ETH ...",
            "body_hash": "sha256:source", "source_path": "sources/source.html"}
    data.update(changes)
    return data


def test_aliases_collapse_only_same_action_address_direction_preserving_sources():
    inputs = [row(), row(target_entry_prefix_candidate="EXCHANGE ALIAS"), row(proposed_action_type="removal")]
    units = build_units(classify_source_rows(inputs))
    assert len(units) == 2
    assert sorted(len(u["source_row_ids"]) for u in units) == [1, 2]
    assert all(u["target_adjudication"] == "pending" for u in units)


def test_pilot_family_explicit_exclusion_and_ambiguous_link_are_conservative():
    cases = [row(target_entry_prefix_candidate="TORNADO CASH CLASSIC"),
             row(normalized_address="0x" + "b" * 40, target_entry_prefix_candidate="SEMENOV, Roman",
                 entry_text="SEMENOV, Roman; email poma@tornado.cash"),
             row(target_entry_prefix_candidate="OTHER SHARED ADDRESS")]
    result = classify_source_rows(cases)
    assert [x["machine_disposition"] for x in result] == ["pilot_family_excluded", "pending_family_adjudication", "pending_family_adjudication"]
    assert build_units(result) == []


def test_updates_and_date_disagreements_remain_pending_not_excluded():
    result = classify_source_rows([row(proposed_action_type="update"), row(release_date="2022-04-06")])
    assert [x["machine_disposition"] for x in result] == ["pending_action_adjudication", "pending_date_adjudication"]


def test_day_precision_window_includes_last_possible_thirty_day_endpoint():
    w = window_for_day("2024-02-29")
    assert w["trigger_latest_exclusive_utc"] == "2024-03-01T00:00:00Z"
    assert w["window_start_inclusive_utc"] == "2024-02-22T00:00:00Z"
    assert w["window_end_exclusive_utc"] == "2024-03-31T00:00:00Z"
    assert w["horizon_deadline_intervals"][-1] == {"days": 30, "earliest_utc": "2024-03-30T00:00:00Z", "latest_exclusive_utc": "2024-03-31T00:00:00Z"}


def test_frozen_bundle_refuses_even_identical_overwrite_and_detects_edits(tmp_path):
    dest = tmp_path / "frozen"
    outputs = {"data.json": "[]\n", "bundle.sha256.json": json.dumps({"files": {"data.json": sha(b"[]\n")}})}
    write_frozen(outputs, dest)
    assert verify_bundle(dest)["files_verified"] == 1
    with pytest.raises(ValueError, match="already exists"):
        write_frozen(outputs, dest)
    (dest / "data.json").write_text("changed")
    with pytest.raises(ValueError, match="hash mismatch"):
        verify_bundle(dest)
