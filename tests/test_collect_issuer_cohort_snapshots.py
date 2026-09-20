import json
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import collect_issuer_cohort_snapshots as collector


def write(path, value):
    path.write_bytes(collector.encoded(value))


def fixture_cohort(tmp_path, actions=2):
    source = ROOT / "analysis/issuer_candidate_manifest"
    selected = collector.jsonl(source / "issuer_query_units.jsonl")
    urls = list(dict.fromkeys(u["action_url"] for u in selected))[:actions]
    selected = [u for u in selected if u["action_url"] in urls]
    mids = {u["measurement_unit_id"] for u in selected}
    measurements = [u for u in collector.jsonl(source / "measurement_units.jsonl") if u["measurement_unit_id"] in mids]
    sids = {sid for u in selected for sid in u["source_row_ids"]}
    sources = [s for s in collector.jsonl(source / "source_rows.jsonl") if s["source_row_id"] in sids]
    directory = tmp_path / "cohort"
    directory.mkdir()
    manifest = json.loads((source / "manifest.json").read_text())
    manifest["counts"].update(issuer_query_units=len(selected), measurement_units=len(measurements), unique_action_urls=len(urls))
    write(directory / "manifest.json", manifest)
    for name, rows in (("issuer_query_units.jsonl", selected), ("measurement_units.jsonl", measurements), ("source_rows.jsonl", sources)):
        (directory / name).write_text("".join(json.dumps(row) + "\n" for row in rows))
    reindex(directory)
    panel = tmp_path / "panel.json"
    write(panel, {"pilot_contract_prerequisites_met": True})
    return directory, panel


def reindex(directory):
    files = {p.name: collector.digest(p.read_bytes()) for p in directory.iterdir() if p.name != "bundle.sha256.json"}
    write(directory / "bundle.sha256.json", {"files": files})


class Transport:
    def __init__(self, fail=None):
        self.calls, self.fail = [], fail

    def __call__(self, url, payload):
        request = json.loads(payload)
        self.calls.append(request)
        if self.fail and self.fail(request):
            return {"http_status": 503, "body": b"temporary unavailable", "transport_error": "503", "headers": {}, "final_url": url}
        method, params = request["method"], request["params"]
        if method == "eth_chainId":
            value = "0x1"
        elif method == "eth_getBlockByNumber":
            n = int(params[0], 16)
            value = {"number": hex(n), "timestamp": hex(1640995200 + n * 12), "hash": "0x" + format(n, "064x")}
        elif method == "eth_getCode":
            value = "0x1234"
        elif method == "eth_getStorageAt":
            value = "0x" + "1".rjust(64, "0")
        else:
            value = "0x" + "0" * 64
        return {"http_status": 200, "body": json.dumps({"jsonrpc": "2.0", "id": 1, "result": value}).encode(), "transport_error": None, "headers": {}, "final_url": url}


def run(out, cohort, panel, transport, **kwargs):
    return collector.collect(out, cohort, panel, transport=transport, bracket=(0, 20000000), sleep=lambda _: None, **kwargs)


def test_grouping_shared_requests_and_exact_boundaries(tmp_path):
    cohort, panel = fixture_cohort(tmp_path)
    units, groups = collector.load_cohort(cohort)
    assert len(groups) == 2 and len(units) > 4  # second action has multiple addresses
    transport = Transport()
    out = tmp_path / "run"
    summary = run(out, cohort, panel, transport)
    assert summary["endpoint_snapshot_campaign_complete"]
    assert summary["valid_endpoint_snapshots"] == 2 * len(units)
    assert summary["full_window_logs_complete"] is False
    assert summary["full_window_response_classification"] is None
    assert len({json.dumps(q, sort_keys=True) for q in transport.calls}) == len(transport.calls)
    assert len(list((out / "prerequisites").glob("*.json"))) == 8
    for path in (out / "boundaries").glob("*.json"):
        for boundary in json.loads(path.read_text()).values():
            assert boundary["before_timestamp"] < boundary["requested_timestamp"] <= boundary["at_or_after_timestamp"]
            assert boundary["before_block"] + 1 == boundary["at_or_after_block"]
    before = {p.relative_to(out): p.read_bytes() for p in out.rglob("*") if p.is_file()}
    transport.calls.clear()
    assert run(out, cohort, panel, transport, resume=True) == summary
    assert transport.calls == []
    assert before == {p.relative_to(out): p.read_bytes() for p in out.rglob("*") if p.is_file()}


def test_immutable_resume_hash_and_capture_refusal(tmp_path):
    cohort, panel = fixture_cohort(tmp_path, actions=1)
    out, transport = tmp_path / "run", Transport()
    run(out, cohort, panel, transport)
    transport.calls.clear()
    with pytest.raises(ValueError, match="explicit --resume"):
        run(out, cohort, panel, transport)
    with pytest.raises(ValueError, match="configuration"):
        run(out, cohort, panel, transport, resume=True, query_budget=1399)
    body = next((out / "captures").glob("*/attempt_1/response.body"))
    body.write_text("changed")
    with pytest.raises(ValueError, match="capture hash"):
        run(out, cohort, panel, transport, resume=True)
    assert not transport.calls


def test_duplicate_and_inconsistent_window_rejected(tmp_path):
    cohort, _ = fixture_cohort(tmp_path, actions=1)
    path = cohort / "issuer_query_units.jsonl"
    rows = collector.jsonl(path)
    path.write_text("".join(json.dumps(row) + "\n" for row in rows + rows[:1]))
    reindex(cohort)
    with pytest.raises(ValueError, match="Duplicate issuer"):
        collector.load_cohort(cohort)
    rows[0]["window_end_exclusive_utc"] = "2022-05-07T00:00:00Z"
    path.write_text("".join(json.dumps(row) + "\n" for row in rows))
    reindex(cohort)
    with pytest.raises(ValueError, match="inconsistency"):
        collector.load_cohort(cohort)


def test_pilot_source_rejected(tmp_path):
    cohort, _ = fixture_cohort(tmp_path, actions=1)
    path = cohort / "source_rows.jsonl"
    rows = collector.jsonl(path)
    rows[0]["machine_disposition"] = "pilot_family_excluded"
    path.write_text("".join(json.dumps(row) + "\n" for row in rows))
    reindex(cohort)
    with pytest.raises(ValueError, match="pilot-excluded"):
        collector.load_cohort(cohort)


def test_budget_retry_semantics_and_partial_failure(tmp_path):
    cohort, panel = fixture_cohort(tmp_path, actions=1)
    out, transport = tmp_path / "budget", Transport()
    summary = run(out, cohort, panel, transport, query_budget=1)
    assert summary["logical_queries_reserved"] == 1
    assert summary["http_attempts_started"] == 1
    assert summary["valid_endpoint_snapshots"] == 0
    assert "budget" in summary["failure_or_stop_reason"]
    gaps = Transport(fail=lambda request: request["method"] == "eth_call")
    failed = run(tmp_path / "failed", cohort, panel, gaps)
    assert not failed["endpoint_snapshot_campaign_complete"]
    assert failed["http_attempts_started"] <= 2 * failed["logical_queries_reserved"]
    assert any(len(list(path.glob("attempt_*"))) == 2 for path in (tmp_path / "failed/captures").iterdir())


def test_interrupted_attempt_consumes_allowance_and_rate_error_stops(tmp_path):
    config = {"endpoint": "https://example.invalid", "logical_query_budget": 3, "minimum_request_interval_seconds": 0.15}
    payload = collector.encoded({"jsonrpc": "2.0", "id": 1, "method": "eth_chainId", "params": []})
    qid = collector.digest(payload).split(":")[1]
    directory = tmp_path / "captures" / qid
    collector.immutable(directory / "request.json", payload, raw=True)
    collector.immutable(directory / "attempt_1/started.json", {"request_sha256": collector.digest(payload)})
    calls, waits = [], []
    def limited(url, payload):
        calls.append(payload)
        return {"http_status": 429, "body": b"{}", "transport_error": "429", "headers": {}}
    session = collector.Session(tmp_path, config, limited, waits.append)
    with pytest.raises(collector.StopCollection, match="rate error"):
        session.query("eth_chainId", [])
    assert len(calls) == 1 and waits == [0.15]
    assert len(list(directory.glob("attempt_*"))) == 2
    with pytest.raises(collector.StopCollection):
        session.query("eth_getCode", ["0x" + "1" * 40, "0x1"])
    assert len(calls) == 1


@pytest.mark.parametrize("bad_contract", [collector.CONTRACTS["usdc"]["address"], "0x" + "1".rjust(40, "0")])
def test_empty_canonical_or_implementation_code_prevents_state_read(tmp_path, bad_contract):
    cohort, panel = fixture_cohort(tmp_path, actions=1)
    underlying = Transport()
    def empty_code(url, payload):
        response = underlying(url, payload)
        query = json.loads(payload)
        if query["method"] == "eth_getCode" and query["params"][0] == bad_contract:
            response["body"] = json.dumps({"jsonrpc": "2.0", "id": 1, "result": "0x"}).encode()
        return response
    summary = run(tmp_path / "run", cohort, panel, empty_code)
    assert summary["valid_endpoint_snapshots"] == 2  # USDT only
    assert not any(q["method"] == "eth_call" and q["params"][0]["data"].startswith(collector.CONTRACTS["usdc"]["selector"]) for q in underlying.calls)


def test_wrong_chain_id_is_captured_gap_and_stops_dependencies(tmp_path):
    cohort, panel = fixture_cohort(tmp_path, actions=1)
    calls = []
    def wrong_chain(url, payload):
        calls.append(json.loads(payload))
        return {"http_status": 200, "body": json.dumps({"jsonrpc": "2.0", "id": 1, "result": "0x2"}).encode(), "transport_error": None, "headers": {}}
    summary = run(tmp_path / "run", cohort, panel, wrong_chain)
    assert summary["valid_endpoint_snapshots"] == 0
    assert summary["http_attempts_started"] == 2
    assert all(q["method"] == "eth_chainId" for q in calls)
    assert "mainnet identity" in summary["failure_or_stop_reason"]


def test_safe_resume_after_interruption_preserves_existing_captures(tmp_path):
    cohort, panel = fixture_cohort(tmp_path, actions=1)
    underlying = Transport()
    count = 0
    def interrupted(url, payload):
        nonlocal count
        count += 1
        if count == 3:
            raise KeyboardInterrupt()
        return underlying(url, payload)
    out = tmp_path / "run"
    with pytest.raises(KeyboardInterrupt):
        run(out, cohort, panel, interrupted)
    before = {p.relative_to(out): p.read_bytes() for p in out.rglob("*") if p.is_file()}
    summary = run(out, cohort, panel, underlying, resume=True)
    assert summary["endpoint_snapshot_campaign_complete"]
    assert summary["http_attempts_started"] == summary["http_attempts_captured"] + 1
    assert all((out / path).read_bytes() == value for path, value in before.items())
