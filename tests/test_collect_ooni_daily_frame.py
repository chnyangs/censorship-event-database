import json
from datetime import datetime

import pytest

from collect_ooni_daily_frame import FRAMES, RateLimiter, build_queries, collect_one, validate_page


def result(**changes):
    row = {"probe_cc": "ET", "probe_asn": "AS1", "test_name": "web_connectivity",
           "measurement_start_time": "2025-09-15T12:00:00Z", "input": "https://www.binance.com/",
           "measurement_url": "https://api.ooni.io/m/1", "report_id": "r1",
           "anomaly": False, "confirmed": False, "failure": False}
    row.update(changes)
    return row


def query():
    return {"query_id": "q", "event_id": "e", "probe_cc": "ET", "domain": "binance.com",
            "test_name": "web_connectivity", "since": "2025-09-15", "until": "2025-09-16"}


def test_frozen_query_count_and_half_open_days():
    rows = build_queries()
    expected = sum((datetime.fromisoformat(f["end_exclusive"]) - datetime.fromisoformat(f["start"])).days * len(f["domains"]) for f in FRAMES)
    assert len(rows) == expected == 624
    assert len({r["query_id"] for r in rows}) == expected


@pytest.mark.parametrize("change,match", [
    ({"probe_cc": "TH"}, "country"),
    ({"input": "https://example.com/"}, "domain"),
    ({"measurement_start_time": "2025-09-16T00:00:00Z"}, "UTC day"),
])
def test_result_outside_frame_rejected(change, match):
    with pytest.raises(ValueError, match=match):
        validate_page(query(), {"metadata": {"count": 1}, "results": [result(**change)]})


def test_zero_count_is_complete_but_not_behavioral_negative(tmp_path):
    body = json.dumps({"metadata": {"count": 0}, "results": []}).encode()
    def transport(url, timeout, limiter):
        return {"status": "http_response", "http_status": 200, "final_url": url,
                "body": body, "error": None, "started_at_utc": "a", "finished_at_utc": "b", "elapsed_seconds": 0}
    # collect_one resolves the module-level fetch function; replace explicitly.
    import collect_ooni_daily_frame as module
    original = module.fetch
    module.fetch = transport
    try:
        summary = collect_one(query(), tmp_path, RateLimiter(0), 1, 1, 500, 5000)
    finally:
        module.fetch = original
    assert summary["pagination_complete"] is True
    assert summary["metadata_count"] == 0
    assert "Metadata frame only" in summary["interpretation"]


def test_duplicate_measurements_fail_closed(tmp_path):
    rows = [result(), result()]
    body = json.dumps({"metadata": {"count": 2}, "results": rows}).encode()
    def transport(url, timeout, limiter):
        return {"status": "http_response", "http_status": 200, "final_url": url,
                "body": body, "error": None, "started_at_utc": "a", "finished_at_utc": "b", "elapsed_seconds": 0}
    import collect_ooni_daily_frame as module
    original = module.fetch
    module.fetch = transport
    try:
        summary = collect_one(query(), tmp_path, RateLimiter(0), 1, 1, 500, 5000)
    finally:
        module.fetch = original
    assert summary["pagination_complete"] is False
    assert summary["terminal_error"] == "duplicate_measurement_rows"


def test_capture_resume_verifies_body_hash(tmp_path):
    body = json.dumps({"metadata": {"count": 0}, "results": []}).encode()
    def transport(url, timeout, limiter):
        return {"status": "http_response", "http_status": 200, "final_url": url,
                "body": body, "error": None, "started_at_utc": "a", "finished_at_utc": "b", "elapsed_seconds": 0}
    import collect_ooni_daily_frame as module
    original = module.fetch; module.fetch = transport
    try:
        collect_one(query(), tmp_path, RateLimiter(0), 1, 1, 500, 5000)
        (tmp_path / "q" / "page_000000_attempt_1.body").write_text("tampered")
        with pytest.raises(ValueError, match="hash mismatch"):
            collect_one(query(), tmp_path, RateLimiter(0), 1, 1, 500, 5000)
    finally:
        module.fetch = original
