# SPDX-License-Identifier: MIT
"""Guard the audit's distinction between risk flags, judgments and human answers."""
from pathlib import Path

import pytest
import yaml

from audit_measurement_semantics import (
    LAYERS, RESPONSE_FIELDS, build_audit, load_events, render_outputs, write_outputs,
)


def event():
    return {
        "id": "test-target", "status": "admitted",
        "trigger": {"actor": "agency", "timestamp": "2024-01-01",
                    "citation": [{"url": "https://example.test/action", "body_hash": "sha256:abc",
                                  "note": "LEGACY_SECRET_TRIGGER_NOTE"}]},
        "target": {"addresses": ["0x123"]},
        "coverage": [{"layer": layer, "status": "not_applicable",
                      "note": "No captured freeze tx_hash is pinned." if layer == "asset_onchain" else "No surface."}
                     for layer in LAYERS],
        "observations": [{"layer": "offramp_cex", "observation_kind": "observed_no_change",
                          "event": "LEGACY_SECRET_CLAIM", "attribution": "none",
                          "sources": [{"url": "https://example.test/action", "body_hash": "sha256:abc",
                                       "note": "LEGACY_SECRET_SOURCE_NOTE"}]}],
    }


def audit_fixture():
    return build_audit([(Path("test-target.yaml"), event())], "sha256:fixture")


def test_source_overlap_counts_observations_once_not_matching_fields_or_sources():
    e = event()
    e["observations"][0]["sources"].append({"body_hash": "sha256:abc"})
    a = build_audit([(Path("e.yaml"), e)], "sha256:fixture")
    assert a["summary"]["admitted"]["no_change_rows_with_trigger_source_overlap"] == 1
    assert a["summary"]["admitted"]["null_events_with_trigger_source_overlap"] == 1
    assert a["overlaps"][0]["verdict"] == "unadjudicated_risk_flag"
    assert e["coverage"][4]["status"] == "not_applicable"  # never recode


def test_draft_records_are_audited_but_excluded_from_paper_and_human_packet():
    e = event()
    e["status"] = "draft"
    a = build_audit([(Path("admitted.yaml"), event()), (Path("draft.yaml"), {**e, "id": "draft"})], "sha256:fixture")
    assert a["summary"]["all_records"]["null_events"] == 2
    assert a["summary"]["admitted"]["null_events"] == 1
    assert len(a["blind_rows"]) == 6


def test_na_screen_is_context_flag_and_all_review_responses_are_blank():
    a = audit_fixture()
    assert len(a["na_flags"]) == 1
    assert a["na_flags"][0]["layer"] == "asset_onchain"
    for row in a["blind_rows"]:
        assert all(row[field] == "" for field in RESPONSE_FIELDS)
        assert "source_yaml" not in row
        assert "event_id" not in row
        assert "legacy_coverage" not in row
    out = render_outputs(a)
    sheet = out["human_review/reviewer_a.csv"]
    assert "LEGACY_SECRET" not in sheet
    assert "observed_no_change" not in sheet
    assert sheet == out["human_review/reviewer_b.csv"]
    assert "LEGACY_SECRET_CLAIM" in out["human_review/sealed_key.csv"]


def test_regeneration_is_identical_and_cannot_erase_a_reviewers_work(tmp_path):
    out = render_outputs(audit_fixture())
    write_outputs(out, tmp_path)
    write_outputs(out, tmp_path)
    reviewer = tmp_path / "human_review/reviewer_b.csv"
    reviewer.write_text(reviewer.read_text() + "human work\n")
    before = (tmp_path / "summary.json").read_bytes()
    with pytest.raises(ValueError, match="Refusing to overwrite"):
        write_outputs({**out, "summary.json": "changed"}, tmp_path)
    assert reviewer.read_text().endswith("human work\n")
    assert (tmp_path / "summary.json").read_bytes() == before


def test_source_hash_tracks_raw_yaml_and_duplicate_keys_fail_closed(tmp_path):
    path = tmp_path / "e.yaml"
    path.write_text(yaml.safe_dump(event()))
    _, first = load_events(tmp_path)
    path.write_text(path.read_text() + "\n# source change\n")
    _, second = load_events(tmp_path)
    assert first != second
    path.write_text("id: one\nid: two\n")
    with pytest.raises(yaml.constructor.ConstructorError, match="duplicate key"):
        load_events(tmp_path)


def test_changed_action_source_overlap_is_not_a_null_event():
    e = event()
    e["observations"][0]["observation_kind"] = "observed_change"
    a = build_audit([(Path("e.yaml"), e)], "sha256:fixture")
    counts = a["summary"]["admitted"]
    assert counts["changed_rows_with_trigger_source_overlap"] == 1
    assert counts["null_events"] == 0
    assert counts["no_change_rows_with_trigger_source_overlap"] == 0
