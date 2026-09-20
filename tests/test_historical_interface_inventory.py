import json
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import prepare_historical_interface_inventory as module


def test_push4_parser_does_not_match_inside_push_payload():
    assert module.push4_offsets("0x6463fe575a8763fe575a87", "0xfe575a87") == [6]


def test_inventory_freezes_captured_code_and_bounded_lookup(tmp_path):
    run = ROOT / "analysis/issuer_candidate_snapshots/cohort_endpoint_v1"
    result = module.prepare(tmp_path / "inventory", run)
    assert result["inventory_entries"] == 3
    assert result["unique_usdc_implementation_addresses"] == 2
    assert result["unique_usdt_code_hashes"] == 1
    assert result["planned_logical_gets"] == 6
    with pytest.raises(ValueError, match="overwrite"):
        module.prepare(tmp_path / "inventory", run)
    calls = []
    def missing(url):
        calls.append(url)
        return {"http_status": 404, "headers": {}, "body": b"missing", "transport_error": "404"}
    summary = module.fetch(tmp_path / "inventory", missing, lambda _: None)
    assert summary["logical_gets_processed"] == 6
    assert summary["http_attempts_started"] == 6
    assert summary["json_captures"] == 0
    assert summary["historical_implementation_bytecode_reproduced"] is False
    calls.clear()
    assert module.fetch(tmp_path / "inventory", missing, lambda _: None) == summary
    assert calls == []


def test_rate_limit_stops_without_following_or_expanding(tmp_path):
    run = ROOT / "analysis/issuer_candidate_snapshots/cohort_endpoint_v1"
    module.prepare(tmp_path / "inventory", run)
    waits = []
    def limited(url):
        return {"http_status": 429, "headers": {}, "body": b"{}", "transport_error": "429"}
    summary = module.fetch(tmp_path / "inventory", limited, waits.append)
    assert summary["logical_gets_processed"] == 1
    assert summary["http_attempts_started"] == 1
    assert summary["rate_limit_stop"]
    assert waits == [0.5]
