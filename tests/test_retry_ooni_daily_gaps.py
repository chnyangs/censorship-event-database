import json

import pytest

from retry_ooni_daily_gaps import load_retry_set, run


def write_json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n")


def source_run(tmp_path):
    source = tmp_path / "source"
    queries = [
        {"query_id": "a", "event_id": "event", "since": "2025-01-01",
         "until": "2025-01-02", "domain": "a.example", "probe_cc": "ZZ",
         "test_name": "web_connectivity"},
        {"query_id": "b", "event_id": "event", "since": "2025-01-02",
         "until": "2025-01-03", "domain": "b.example", "probe_cc": "ZZ",
         "test_name": "web_connectivity"},
    ]
    summaries = [
        {"query": queries[0], "pagination_complete": True, "retrieved_rows": 0},
        {"query": queries[1], "pagination_complete": False, "retrieved_rows": 0},
    ]
    write_json(source / "manifest.json", {"query_count": 2})
    write_json(source / "query_summaries.json", summaries)
    write_json(source / "summary.json", {"query_count": 2, "failed_or_incomplete_queries": 1})
    for row in summaries:
        write_json(source / "captures" / row["query"]["query_id"] / "summary.json", row)
    return source, queries, summaries


def test_retry_set_uses_only_retrieval_completeness(tmp_path):
    source, queries, _ = source_run(tmp_path)
    selected, hashes = load_retry_set(source)
    assert selected == [queries[1]]
    assert set(hashes) == {
        "source_manifest_sha256", "source_query_summaries_sha256", "source_summary_sha256"
    }


def test_retry_set_rejects_aggregate_capture_mismatch(tmp_path):
    source, _, summaries = source_run(tmp_path)
    changed = {**summaries[1], "terminal_error": "changed"}
    write_json(source / "captures" / "b" / "summary.json", changed)
    with pytest.raises(ValueError, match="Aggregate/original"):
        load_retry_set(source)


@pytest.mark.parametrize("kwargs", [
    {"timeout": 24}, {"interval": 0.49}, {"attempts": 2},
])
def test_retry_profile_is_bounded_before_input_or_network(tmp_path, kwargs):
    with pytest.raises(ValueError, match="Retry profile"):
        run(tmp_path / "missing", tmp_path / "out", **kwargs)
