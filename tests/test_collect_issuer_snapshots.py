import json

import pytest

from collect_issuer_snapshots import collect, load_batch
from measurement_pilot import CONTRACTS, digest


def fixture_batch(tmp_path):
    units = [{"normalized_address": "0x" + "a" * 40,
              "issuer": {"symbol": name.upper(), "chain_id": 1, "contract_address": c["address"]},
              "issuer_query_id": name,
              "window_start_inclusive_utc": "1970-01-01T00:20:50Z",
              "window_end_exclusive_utc": "1970-01-01T00:30:00Z"}
             for name, c in CONTRACTS.items()]
    batch = tmp_path / "first_batch.json"
    batch.write_text(json.dumps({"query_units": units, "selection_rule": "source-only frozen test"}))
    (tmp_path / "bundle.sha256.json").write_text(json.dumps({"files": {batch.name: digest(batch.read_bytes())}}))
    panel = tmp_path / "panel.json"
    panel.write_text('{"pilot_contract_prerequisites_met":true}')
    return batch, panel


def transport(endpoint, payload):
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
        assert method == "eth_call"  # No eth_getLogs or write method in snapshot collector.
        value = "0x" + "0" * 64
    return {"http_status": 200, "final_url": endpoint, "headers": {},
            "body": json.dumps({"jsonrpc": "2.0", "id": 1, "result": value}).encode(),
            "elapsed_seconds": 0, "transport_error": None}


def test_frozen_batch_hash_mismatch_fails_before_transport(tmp_path):
    batch, panel = fixture_batch(tmp_path)
    batch.write_text(batch.read_text() + " ")
    with pytest.raises(ValueError, match="mismatch"):
        load_batch(batch)
    assert not (tmp_path / "run").exists()


def test_adjacent_boundaries_and_partial_snapshots_never_become_full_window(tmp_path):
    batch, panel = fixture_batch(tmp_path)
    out = tmp_path / "run"
    result = collect(out, batch, panel, transport, bracket=(10, 20))
    assert result["valid_endpoint_snapshots"] == 4
    assert result["failure_or_stop_reason"] is None
    assert result["full_window_logs_complete"] is False
    assert result["full_window_response_classification"] is None
    boundaries = json.loads((out / "boundaries.json").read_text())
    assert boundaries["start"]["before_block"] == 12
    assert boundaries["start"]["at_or_after_block"] == 13
    assert boundaries["end"]["before_block"] == 17
    snapshots = json.loads((out / "snapshots.json").read_text())
    assert {row["block_number"] for row in snapshots} == {13, 17}
    assert all(row["historical_implementation_bytecode_reproduced"] is False for row in snapshots)
    manifest = json.loads((out / "collection_manifest.json").read_text())
    assert manifest["candidate_batch_sha256"] == digest((out / "candidate_batch.json").read_bytes())
    assert manifest["collector_sha256"] == digest((out / "collector_source.py").read_bytes())
    with pytest.raises(ValueError, match="overwrite"):
        collect(out, batch, panel, transport)


def test_query_budget_fail_closed_with_partial_capture(tmp_path):
    batch, panel = fixture_batch(tmp_path)
    result = collect(tmp_path / "run", batch, panel, transport, bracket=(10, 20), query_budget=1)
    assert result["attempted_queries"] == 1
    assert "budget exhausted" in result["failure_or_stop_reason"]
    assert result["valid_endpoint_snapshots"] == 0
