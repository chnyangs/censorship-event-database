import json
import urllib.error
import urllib.request
from pathlib import Path

import pytest

import collect_blockscout_issuer_logs as collector
from measurement_pilot import CONTRACTS, digest


def stream(name="usdc", direction=0):
    spec = CONTRACTS[name]
    return {"id": name + ("_add" if direction == 0 else "_remove"), "issuer": name,
            "contract": spec["address"], "topic": spec["topics"][direction],
            "direction": "add" if direction == 0 else "remove",
            "seed_cursor": {"block_number": 20, "index": 0, "items_count": 50}}


def item(spec, block=15, index=1):
    word = "0x" + "0" * 24 + "a" * 40
    indexed = CONTRACTS[spec["issuer"]]["indexed_address"]
    return {"address": {"hash": spec["contract"]}, "block_number": block, "index": index,
            "block_hash": "0x" + "b" * 64, "transaction_hash": "0x" + "c" * 64,
            "block_timestamp": "2022-01-01T00:00:00Z",
            "topics": [spec["topic"], word, None, None] if indexed else [spec["topic"], None, None, None],
            "data": "0x" if indexed else word}


def test_both_abi_layouts_and_server_cursor_are_preserved():
    for name in CONTRACTS:
        spec = stream(name)
        cursor = {"block_number": 15, "index": 1, "items_count": 50}
        rows, following = collector.validate_page({"items": [item(spec)], "next_page_params": cursor}, spec, spec["seed_cursor"])
        assert rows[0]["affected_address"] == "0x" + "a" * 40
        assert following == cursor
        assert "topic=" in collector.page_url(spec, cursor)
        assert "0x" + "a" * 40 not in collector.page_url(spec, cursor)


@pytest.mark.parametrize("change", [{"block_number": 20}, {"index": -1},
                                    {"topics": ["0x" + "d" * 64]}, {"data": "0x01"},
                                    {"block_hash": "missing"}, {"block_timestamp": "not-a-date"}])
def test_invalid_page_is_not_complete_empty_evidence(change):
    spec = stream()
    with pytest.raises(ValueError):
        collector.validate_page({"items": [{**item(spec), **change}], "next_page_params": None}, spec, spec["seed_cursor"])


def test_repeated_cursor_and_nonterminating_empty_page_rejected():
    spec = stream()
    for data in ({"items": [], "next_page_params": spec["seed_cursor"]},
                 {"items": [item(spec)], "next_page_params": spec["seed_cursor"]}):
        with pytest.raises(ValueError):
            collector.validate_page(data, spec, spec["seed_cursor"])


def run_plan(tmp_path):
    source = Path(collector.__file__)
    manifest = {"collector_sha256": digest(source.read_bytes()),
                "transport_library_sha256": digest(source.with_name("measurement_pilot.py").read_bytes()),
                "streams": [stream(name, direction) for name in CONTRACTS for direction in (0, 1)],
                "max_pages_per_stream": 2, "maximum_page_requests": 8,
                "first_block_inclusive": 10, "last_block_inclusive": 19}
    (tmp_path / "plan.json").write_text(json.dumps(manifest))
    (tmp_path / "plan.sha256.json").write_text(json.dumps({"plan_sha256": digest((tmp_path / "plan.json").read_bytes())}))
    return manifest


def response(data, status=200):
    return {"http_status": status, "final_url": "https://eth.blockscout.com", "headers": {},
            "body": json.dumps(data).encode(), "transport_error": None, "elapsed_seconds": 0}


def test_rate_limit_stops_all_streams_and_does_not_retry(tmp_path):
    run_plan(tmp_path)
    calls = []
    def limited(url):
        calls.append(url)
        return response({}, 429)
    result = collector.run(tmp_path, limited)
    assert len(calls) == 1
    assert result["pages_captured"] == 1
    assert result["all_four_index_ranges_complete"] is False
    assert all(s["stop_reason"] == "global_rate_limit_stop" for s in result["streams"][1:])


def test_empty_terminated_streams_complete_only_index_coverage_and_resume(tmp_path):
    run_plan(tmp_path)
    result = collector.run(tmp_path, lambda url: response({"items": [], "next_page_params": None}))
    assert result["all_four_index_ranges_complete"] is True
    assert result["independent_chain_completeness_verified"] is False
    assert result["full_window_response_classification"] is None
    calls = []
    collector.run(tmp_path, lambda url: calls.append(url))
    assert not calls


def test_cross_host_redirect_is_refused():
    request = urllib.request.Request("https://eth.blockscout.com/test")
    with pytest.raises(urllib.error.HTTPError, match="Cross-host"):
        collector.SameHostRedirects().redirect_request(request, None, 302, "redirect", {}, "https://other.example/test")
