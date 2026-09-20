import json
from pathlib import Path

import pytest

from measurement_pilot import (CONTRACTS, PILOT_BLOCK, READ_METHODS, TARGET,
                               build_queries, decode_target_logs, digest,
                               rpc_query, run_pilot, validate_result)
from prepare_measurement_panel import capture_source


def response(result=None, *, error=None, status=200):
    data = {"jsonrpc": "2.0", "id": 1}
    data.update({"error": error} if error else {"result": result})
    return {"http_status": status, "final_url": "https://example.test", "headers": {},
            "body": json.dumps(data).encode(), "elapsed_seconds": 0, "transport_error": None}


def test_write_method_is_rejected_without_transport(tmp_path):
    calls = []
    with pytest.raises(ValueError, match="read methods"):
        rpc_query("https://example.test", "eth_sendRawTransaction", [], tmp_path,
                  lambda *args: calls.append(args))
    assert not calls
    assert all(query["method"] in READ_METHODS for query in build_queries())


def test_rpc_error_stays_gap_and_attempts_are_bounded_and_captured(tmp_path):
    calls = []
    def transport(*args):
        calls.append(args)
        return response(error={"code": -32000, "message": "historical state unavailable"})
    row = rpc_query("https://example.test", "eth_call", [], tmp_path / "query", transport)
    assert row["status"] == "gap" and row["result"] is None
    assert len(calls) == 2
    for number in (1, 2):
        capture = tmp_path / "query" / f"attempt_{number}"
        meta = json.loads((capture / "capture.json").read_text())
        assert meta["response_body_sha256"] == digest((capture / "response.body").read_bytes())
        assert meta["request_sha256"] == digest((capture / "request.json").read_bytes())


@pytest.mark.parametrize("method,value", [("eth_chainId", "0x89"), ("eth_call", "0x"),
                                           ("eth_getCode", "0x"), ("eth_getLogs", None),
                                           ("eth_getBlockByNumber", None)])
def test_invalid_or_missing_result_is_not_a_negative(method, value):
    with pytest.raises(ValueError):
        validate_result(method, value)


@pytest.mark.parametrize("block", [
    {"number": None, "timestamp": "not-hex", "hash": ""},
    {"number": "0x1", "timestamp": "0x" + "f" * 100, "hash": "0x" + "a" * 64},
    {"number": "0x1", "timestamp": "0x1", "hash": None},
])
def test_malformed_block_is_captured_gap(tmp_path, block):
    row = rpc_query("https://example.test", "eth_getBlockByNumber", ["0x1", False],
                    tmp_path / "query", lambda *args: response(block))
    assert row["status"] == "gap"
    assert len(row["attempts"]) == 2


@pytest.mark.parametrize("change", [
    {"address": None}, {"topics": [None]}, {"topics": "not-a-list"},
    {"data": None}, {"data": "0x" + "z" * 64},
    {"data": "0x" + "f" * 64}, {"removed": None},
])
def test_malformed_log_is_not_a_nonmatching_negative(change):
    contract = CONTRACTS["usdt"]
    log = {"address": contract["address"], "topics": [contract["topics"][0]],
           "data": "0x" + TARGET[2:].rjust(64, "0"), "blockNumber": hex(PILOT_BLOCK), "removed": False}
    with pytest.raises(ValueError):
        decode_target_logs([{**log, **change}], contract)


def test_usdt_event_address_is_decoded_from_data_not_a_fabricated_topic():
    queries = {row["id"]: row for row in build_queries()}
    assert len(queries["usdt_logs"]["params"][0]["topics"]) == 1
    assert len(queries["usdc_logs"]["params"][0]["topics"]) == 2
    log = {"address": CONTRACTS["usdt"]["address"], "topics": [CONTRACTS["usdt"]["topics"][0]],
           "data": "0x" + TARGET[2:].rjust(64, "0"), "blockNumber": hex(PILOT_BLOCK), "removed": False}
    assert decode_target_logs([log], CONTRACTS["usdt"]) == [log]
    with pytest.raises(ValueError, match="outside"):
        decode_target_logs([{**log, "blockNumber": hex(PILOT_BLOCK + 5)}], CONTRACTS["usdt"])
    with pytest.raises(ValueError, match="Indexed"):
        decode_target_logs([{**log, "address": CONTRACTS["usdc"]["address"],
                             "topics": [CONTRACTS["usdc"]["topics"][0]]}], CONTRACTS["usdc"])


def test_failed_chain_identity_skips_dependent_queries_and_preserves_run(tmp_path):
    panel = tmp_path / "panel.json"
    panel.write_text('{"pilot_contract_prerequisites_met":true}')
    out = tmp_path / "run"
    summary = run_pilot(out, panel, lambda *args: response("0x89"), providers=("alchemy_public",))
    assert summary["attempted_queries"] == 1
    assert summary["valid_rpc_responses"] == 0
    assert summary["full_cohort_execution"] is False
    manifest = json.loads((out / "pilot_manifest.json").read_text())
    assert manifest["study_role"] == "feasibility_pilot_excluded_from_evaluation"
    assert manifest["collector_sha256"] == digest((out / "collector_source.py").read_bytes())
    with pytest.raises(ValueError, match="overwrite"):
        run_pilot(out, panel)


def test_invalid_historical_block_marks_valid_state_as_transport_only(tmp_path):
    panel = tmp_path / "panel.json"
    panel.write_text('{"pilot_contract_prerequisites_met":true}')
    def transport(endpoint, payload):
        method = json.loads(payload)["method"]
        values = {"eth_chainId": "0x1", "eth_getBlockByNumber":
                  {"number": hex(PILOT_BLOCK), "timestamp": "0x1", "hash": "0x" + "a" * 64},
                  "eth_getLogs": [], "eth_getCode": "0x01"}
        return response(values.get(method, "0x" + "0" * 64))
    out = tmp_path / "run"
    run_pilot(out, panel, transport, providers=("alchemy_public",))
    results = {r["query_id"]: r for r in json.loads((out / "results.json").read_text())}
    assert results["historical_block"]["status"] == "gap"
    state = results["usdc_blacklist_state_after"]
    assert state["status"] == "valid_rpc_response"
    assert state["historical_block_dependency_valid"] is False
    assert "Transport diagnostic only" in state["interpretation_limit"]


def test_http_error_with_matching_words_is_not_verified_source(tmp_path):
    def transport(*args):
        value = response(status=403)
        value["body"] = b"sanctions"
        return value
    row = capture_source(("policy", "https://example.test", ["sanctions"]), tmp_path, transport)
    assert row["status"] == "unavailable_or_content_unverified"
    assert len(row["attempts"]) == 2


def test_eth_signatures_use_keccak_not_nist_sha3():
    keccak = pytest.importorskip("Crypto.Hash.keccak")
    for contract in CONTRACTS.values():
        h = keccak.new(digest_bits=256)
        h.update(contract["read_signature"].encode())
        assert contract["selector"] == "0x" + h.hexdigest()[:8]
        for signature, topic in zip(contract["event_signatures"], contract["topics"]):
            h = keccak.new(digest_bits=256)
            h.update(signature.encode())
            assert topic == "0x" + h.hexdigest()
