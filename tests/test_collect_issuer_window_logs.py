import json

import pytest

from collect_issuer_snapshots import collect
from collect_issuer_window_logs import (decode_logs, durable_query, execute,
                                       partition, plan)
from measurement_pilot import CONTRACTS, digest


def fixture_batch(tmp_path):
    units = [{"normalized_address": "0x" + "a" * 40,
              "issuer": {"symbol": name.upper(), "chain_id": 1, "contract_address": c["address"]},
              "issuer_query_id": name, "window_start_inclusive_utc": "1970-01-01T00:20:50Z",
              "window_end_exclusive_utc": "1970-01-01T00:30:00Z"}
             for name, c in CONTRACTS.items()]
    batch = tmp_path / "first_batch.json"
    batch.write_text(json.dumps({"query_units": units, "selection_rule": "source-only frozen test"}))
    (tmp_path / "bundle.sha256.json").write_text(json.dumps({"files": {batch.name: digest(batch.read_bytes())}}))
    panel = tmp_path / "panel.json"
    panel.write_text('{"pilot_contract_prerequisites_met":true}')
    return batch, panel


def snapshot_transport(endpoint, payload):
    query = json.loads(payload)
    method = query["method"]
    if method == "eth_chainId":
        value = "0x1"
    elif method == "eth_getBlockByNumber":
        number = int(query["params"][0], 16)
        value = {"number": hex(number), "timestamp": hex(number * 100), "hash": "0x" + f"{number:064x}"}
    elif method == "eth_getCode":
        value = "0x01"
    elif method == "eth_getStorageAt":
        value = "0x" + "0" * 63 + "1"
    else:
        assert method == "eth_call"
        value = "0x" + "0" * 64
    return rpc_response(value)


def prepare(tmp_path, budget=200):
    batch, panel = fixture_batch(tmp_path)
    snapshots = tmp_path / "snapshots"
    collect(snapshots, batch, panel, snapshot_transport, bracket=(10, 20))
    out = tmp_path / "logs"
    plan(out, batch, snapshots, chunk_blocks=10, http_budget=budget)
    return out


def log_for(contract="usdc", target="0x" + "a" * 40):
    spec = CONTRACTS[contract]
    word = "0x" + target[2:].rjust(64, "0")
    return {"address": spec["address"], "blockNumber": "0xd", "blockHash": "0x" + "b" * 64,
            "transactionHash": "0x" + "c" * 64, "logIndex": "0x0", "transactionIndex": "0x0",
            "topics": [spec["topics"][0], word] if spec["indexed_address"] else [spec["topics"][0]],
            "data": "0x" if spec["indexed_address"] else word, "removed": False}


def rpc_response(value):
    return {"http_status": 200, "final_url": "https://example.test", "headers": {},
            "body": json.dumps({"jsonrpc": "2.0", "id": 1, "result": value}).encode(),
            "transport_error": None, "elapsed_seconds": 0}


def test_partition_is_inclusive_complete_without_overlap():
    assert partition(100, 120, 10) == [(100, 109), (110, 119), (120, 120)]
    with pytest.raises(ValueError):
        partition(10, 9, 10)


def test_budget_refusal_occurs_before_any_network_call(tmp_path):
    out = prepare(tmp_path, budget=1)
    calls = []
    result = execute(out, lambda *args: calls.append(args))
    assert result["status"] == "not_launched_budget_exceeded"
    assert result["network_requests_sent"] == 0 and not calls
    assert not (out / "captures").exists()


def test_complete_ranges_deduplicate_and_resume_without_network(tmp_path):
    out = prepare(tmp_path)
    def transport(endpoint, payload):
        query = json.loads(payload)
        if query["method"] != "eth_getLogs":
            return snapshot_transport(endpoint, payload)
        symbol = "usdc" if query["params"][0]["address"] == CONTRACTS["usdc"]["address"] else "usdt"
        # Duplicate records from one server response are deduplicated.
        return rpc_response([log_for(), log_for()] if symbol == "usdc" else [])
    result = execute(out, transport)
    assert result["requested_range_coverage_complete"] is True
    assert result["unique_target_logs"] == 1
    assert result["full_window_response_classification"] is None
    assert result["independent_log_completeness_verified"] is False
    assert result["http_attempts_on_disk"] == 7
    calls = []
    resumed = execute(out, lambda *args: calls.append(args))
    assert resumed["requested_range_coverage_complete"] is True
    assert not calls


def test_conflicting_duplicate_makes_whole_range_incomplete(tmp_path):
    out = prepare(tmp_path)
    def transport(endpoint, payload):
        if json.loads(payload)["method"] != "eth_getLogs":
            return snapshot_transport(endpoint, payload)
        first = log_for()
        second = {**first, "transactionIndex": "0x1"}
        return rpc_response([first, second])
    result = execute(out, transport)
    assert result["requested_range_coverage_complete"] is False
    assert "Conflicting duplicate" in result["failure_or_stop_reason"]
    assert result["unique_logs"] == 0


@pytest.mark.parametrize("change", [{"blockNumber": "0x100"}, {"removed": True},
                                    {"logIndex": None}, {"blockHash": "0x123"},
                                    {"topics": [None]}, {"data": "0x11"}])
def test_bad_log_never_becomes_valid_empty_range(change):
    chunk = {"issuer": "usdc", "target": "0x" + "a" * 40, "first": 13, "last": 17}
    with pytest.raises(ValueError):
        decode_logs([{**log_for(), **change}], chunk, 10000)


def test_usdt_nonmatching_valid_logs_retained_for_completeness():
    chunk = {"issuer": "usdt", "target": "0x" + "a" * 40, "first": 13, "last": 17}
    rows = decode_logs([log_for("usdt", "0x" + "d" * 40)], chunk, 10000)
    assert len(rows) == 1 and rows[0]["target_match"] is False
    with pytest.raises(ValueError, match="Cap-sized"):
        decode_logs([log_for("usdt")], chunk, 1)


def test_captured_failures_get_no_more_than_two_total_attempts_across_resume(tmp_path):
    calls = []
    def failure(*args):
        calls.append(args)
        result = rpc_response(None)
        result.update(http_status=503, transport_error="temporarily unavailable")
        return result
    for _ in range(2):
        value, error = durable_query(tmp_path, "https://example.test", "q", "eth_getLogs", [], failure, 0)
        assert value is None and error
    assert len(calls) == 2


def test_plan_and_capture_tampering_fail_closed(tmp_path):
    out = prepare(tmp_path)
    (out / "candidate_batch.json").write_text("{}")
    with pytest.raises(ValueError, match="integrity"):
        execute(out, lambda *args: pytest.fail("Must not call network"))


def test_rate_limit_stops_without_retry_even_after_resume(tmp_path):
    calls = []
    def limited(*args):
        calls.append(args)
        result = rpc_response(None)
        result.update(http_status=429, transport_error="HTTP 429 Too Many Requests")
        return result
    for _ in range(2):
        value, error = durable_query(tmp_path, "https://example.test", "q", "eth_getLogs", [], limited, 0)
        assert value is None and "Rate limit stop" in error
    assert len(calls) == 1
