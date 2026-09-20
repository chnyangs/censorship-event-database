import json
from pathlib import Path

import pytest

import reconcile_issuer_snapshots as subject
from measurement_pilot import digest, dump


def frozen_plan(tmp_path, budget=300):
    queries = [
        {"id": "chain", "method": "eth_chainId", "params": [], "expected_comparison": "0x1", "dependencies": [], "is_target_state_query": False},
        {"id": "header", "method": "eth_getBlockByNumber", "params": ["0xa", False],
         "expected_comparison": {"number": 10, "timestamp": 100, "hash": "0x" + "a" * 64}, "dependencies": ["chain"], "is_target_state_query": False},
        {"id": "code", "method": "eth_getCode", "params": ["0x" + "a" * 40, "0xa"],
         "expected_comparison": {"code_sha256": digest(b"\x01")}, "dependencies": ["chain", "header"], "is_target_state_query": False},
        {"id": "state", "method": "eth_call", "params": [{"to": "0x" + "a" * 40, "data": "0x12345678"}, "0xa"],
         "expected_comparison": "0x" + "0" * 64, "dependencies": ["chain", "header", "code"], "is_target_state_query": True},
    ]
    manifest = {"collector_sha256": digest(Path(subject.__file__).read_bytes()),
                "transport_source_sha256": digest(Path(subject.__file__).with_name("measurement_pilot.py").read_bytes()),
                "providers": {key: {"endpoint": endpoint} for key, endpoint in subject.PROVIDERS.items()},
                "queries": queries, "explicit_total_request_budget": budget, "maximum_total_requests": 8,
                "minimum_delay_seconds": 0.5, "selected_window_ids": ["first"], "selected_snapshot_units": ["test"]}
    dump(tmp_path / "plan.json", manifest)
    dump(tmp_path / "plan.sha256.json", {"plan_sha256": digest((tmp_path / "plan.json").read_bytes())})
    return manifest


def mock_transport(endpoint, payload):
    query = json.loads(payload)
    value = {"eth_chainId": "0x1", "eth_getBlockByNumber": {"number": "0xa", "timestamp": "0x64", "hash": "0x" + "a" * 64},
             "eth_getCode": "0x01", "eth_call": "0x" + "0" * 64}[query["method"]]
    return {"http_status": 200, "final_url": endpoint, "headers": {}, "transport_error": None,
            "elapsed_seconds": 0, "body": json.dumps({"jsonrpc": "2.0", "id": 1, "result": value}).encode()}


def test_all_match_and_replay_consumes_no_requests(tmp_path):
    frozen_plan(tmp_path)
    result = subject.run(tmp_path, mock_transport)
    assert result["attempted_queries"] == 8
    assert all(row["matched_queries"] == 4 and row["matched_target_state_queries"] == 1 for row in result["providers"])
    assert result["upstream_operator_independence_verified"] is False
    assert result["full_cohort_reconciliation"] is False
    original = (tmp_path / "summary.json").read_bytes()
    def forbidden(*args):
        pytest.fail("Offline replay attempted network")
    subject.run(tmp_path, forbidden)
    assert original == (tmp_path / "summary.json").read_bytes()


def test_header_disagreement_blocks_dependent_state(tmp_path):
    frozen_plan(tmp_path)
    def transport(endpoint, payload):
        response = mock_transport(endpoint, payload)
        if json.loads(payload)["method"] == "eth_getBlockByNumber":
            row = json.loads(response["body"])
            row["result"]["number"] = "0xb"
            response["body"] = json.dumps(row).encode()
        return response
    result = subject.run(tmp_path, transport)
    assert result["attempted_queries"] == 4
    rows = json.loads((tmp_path / "results.json").read_text())
    assert all(row["status"] == "not_attempted_dependency_gap_or_disagreement" for row in rows if row["method"] == "eth_call")


def test_rate_limit_stops_affected_provider_without_retry(tmp_path):
    frozen_plan(tmp_path)
    calls = []
    def transport(endpoint, payload):
        calls.append(endpoint)
        response = mock_transport(endpoint, payload)
        if endpoint == subject.PROVIDERS["drpc_public"]:
            response.update(http_status=429, body=b"Too many requests", transport_error="HTTP429")
        return response
    result = subject.run(tmp_path, transport)
    assert calls.count(subject.PROVIDERS["drpc_public"]) == 1
    assert calls.count(subject.PROVIDERS["one_rpc_public"]) == 4
    assert result["providers"][0]["rate_limit_stop"] is True
    assert result["attempted_queries"] == 5


def test_budget_refuses_before_transport(tmp_path):
    frozen_plan(tmp_path, budget=7)
    with pytest.raises(ValueError, match="budget exceeded"):
        subject.run(tmp_path, lambda *args: pytest.fail("Budget exceeded before network"))
    assert not (tmp_path / "captures").exists()


def test_cached_response_tampering_fails_closed(tmp_path):
    frozen_plan(tmp_path)
    subject.run(tmp_path, mock_transport)
    path = tmp_path / "captures/drpc_public/chain/attempt_1/response.body"
    path.write_bytes(path.read_bytes() + b" ")
    with pytest.raises(ValueError, match="hash or identity mismatch"):
        subject.run(tmp_path, lambda *args: pytest.fail("Tampered cache attempted network"))


def test_interrupted_request_is_never_retried(tmp_path):
    frozen_plan(tmp_path)
    (tmp_path / "captures/drpc_public/chain").mkdir(parents=True)
    calls = []
    def transport(endpoint, payload):
        calls.append(endpoint)
        return mock_transport(endpoint, payload)
    result = subject.run(tmp_path, transport)
    assert all(endpoint != subject.PROVIDERS["drpc_public"] for endpoint in calls)
    assert result["attempted_queries"] == 5  # Interrupted call conservatively consumes its attempt.
