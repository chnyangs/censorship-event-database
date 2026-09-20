# SPDX-License-Identifier: MIT
import csv
import io
import json
from datetime import date

import pytest

from prepare_validation_cohort import ADJUDICATION_FIELDS, extract_page, prepare, write_outputs


ADDRESS = "0x" + "a" * 40


def test_visible_address_candidates_exclude_script_and_do_not_infer_action():
    raw = (f"<script>0x{'b' * 40}</script><p>Release Date 01/02/2022</p>"
           f"<p>{ADDRESS}; {ADDRESS.upper().replace('0X', '0x')}; 0x{'c' * 41}</p>").encode()
    parsed = extract_page(raw)
    assert set(parsed["addresses"]) == {ADDRESS}
    assert parsed["page_release_date"] == "2022-01-02"
    assert "action_type" not in parsed


def test_uncached_days_unassessed_and_human_fields_blank(tmp_path):
    (tmp_path / "20220102.html").write_text(f"Release Date 01/02/2022 {ADDRESS}")
    (tmp_path / "20220103.html").write_text("Release Date 01/03/2022 no extracted address")
    out = prepare(tmp_path, date(2022, 1, 1), date(2022, 1, 3))
    summary = json.loads(out["summary.json"])
    assert summary["cached_pages_in_window"] == 2
    assert summary["candidate_page_address_pairs"] == 1
    assert summary["frame_completeness"] == "not_assessed"
    days = list(csv.DictReader(io.StringIO(out["frame_daily_ledger.csv"])))
    assert days[0]["local_inventory_status"] == "unassessed_no_local_page"
    assert all(row["in_frame_action_count"] == "" for row in days)
    humans = list(csv.DictReader(io.StringIO(out["action_target_adjudication_blank.csv"])))
    assert humans[0]["status"] == "pending_action_target_adjudication"
    assert all(humans[0][field] == "" for field in ADJUDICATION_FIELDS)
    assert list(csv.DictReader(io.StringIO(out["query_log_template.csv"]))) == []


def test_date_mismatch_is_reported_and_raw_hash_changes(tmp_path):
    path = tmp_path / "20220102.html"
    path.write_text("Release Date 01/03/2022")
    out = prepare(tmp_path, date(2022, 1, 1), date(2022, 1, 3))
    first = json.loads(out["summary.json"])
    assert first["date_review_required_pages"] == 1
    path.write_text(path.read_text() + "<!-- new bytes -->")
    second = json.loads(prepare(tmp_path, date(2022, 1, 1), date(2022, 1, 3))["summary.json"])
    assert first["source_input_hash"] != second["source_input_hash"]


def test_changed_query_log_is_preserved_before_any_output_write(tmp_path):
    cache = tmp_path / "cache"
    cache.mkdir()
    out = prepare(cache, date(2022, 1, 1), date(2022, 1, 2))
    dest = tmp_path / "output"
    write_outputs(out, dest)
    write_outputs(out, dest)
    log = dest / "query_log_template.csv"
    log.write_text(log.read_text() + "human query log entry\n")
    with pytest.raises(ValueError, match="Refusing to overwrite"):
        write_outputs({**out, "summary.json": "modified"}, dest)
    assert log.read_text().endswith("human query log entry\n")
    assert (dest / "summary.json").read_text() == out["summary.json"]


@pytest.mark.parametrize("filename", [
    "action_target_adjudication_blank.csv", "frame_daily_ledger.csv",
    "frame_monthly_ledger.csv", "panel_manifest.json",
])
def test_regeneration_preserves_all_human_decisions_before_writing(tmp_path, filename):
    cache = tmp_path / "cache"
    cache.mkdir()
    (cache / "20220102.html").write_text(f"Release Date 01/02/2022 {ADDRESS}")
    out = prepare(cache, date(2022, 1, 1), date(2022, 1, 2))
    dest = tmp_path / "output"
    write_outputs(out, dest)
    path = dest / filename
    if filename == "panel_manifest.json":
        manifest = json.loads(path.read_text())
        manifest["panels"][0]["identity_verification_status"] = "verified_by_reviewer"
        manifest["panels"][0]["contract_or_endpoint"] = ADDRESS
        path.write_text(json.dumps(manifest))
    else:
        rows = list(csv.DictReader(io.StringIO(path.read_text())))
        fieldnames = list(rows[0])
        if filename.startswith("frame_"):
            rows[0]["frame_reconciliation_status"] = "reconciled_by_reviewer"
            rows[0]["in_frame_action_count"] = "1"
        else:
            rows[0]["reviewer_id"] = "reviewer-a"
            rows[0]["eligible_for_frame"] = "yes"
        stream = io.StringIO(newline="")
        writer = csv.DictWriter(stream, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
        path.write_text(stream.getvalue())
    saved_bytes = path.read_bytes()
    with pytest.raises(ValueError, match="Refusing to overwrite"):
        write_outputs({**out, "summary.json": "must not be written"}, dest)
    assert path.read_bytes() == saved_bytes
    assert (dest / "summary.json").read_text() == out["summary.json"]
