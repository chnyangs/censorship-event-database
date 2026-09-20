#!/usr/bin/env python3
"""Read-only Ethereum feasibility pilot; excluded from research evaluation.

No credentials, transactions, guessed keys, or automatic endpoint substitution.
Every HTTP attempt is captured; errors and skipped dependencies remain gaps.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
READ_METHODS = {"eth_chainId", "eth_getCode", "eth_getBlockByNumber", "eth_call", "eth_getLogs", "eth_getStorageAt"}
CONTRACTS = {
    "usdc": {"address": "0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48", "read_signature": "isBlacklisted(address)", "selector": "0xfe575a87", "indexed_address": True,
             "event_signatures": ["Blacklisted(address)", "UnBlacklisted(address)"],
             "topics": ["0xffa4e6181777692565cf28528fc88fd1516ea86b56da075235fa575af6a4b855", "0x117e3210bb9aa7d9baff172026820255c6f6c30ba8999d1c2fd88e2848137c4e"]},
    "usdt": {"address": "0xdac17f958d2ee523a2206206994597c13d831ec7", "read_signature": "isBlackListed(address)", "selector": "0xe47d6060", "indexed_address": False,
             "event_signatures": ["AddedBlackList(address)", "RemovedBlackList(address)"],
             "topics": ["0x42e160154868087d6bfdc0ca23d96a1c1cfa32f1b72ba9ba27b69b98a0d819dc", "0xd7e9ec6e6ecd65492dce6bf513cd6867560d49544421d0783ddf06e76c24470c"]},
}
ENDPOINTS = {"flashbots": "https://rpc.flashbots.net", "alchemy_public": "https://eth-mainnet.g.alchemy.com/public"}
TARGET = "0x8589427373d6d84e98730d7795d8f6f8731fda16"
PILOT_BLOCK = 15301835  # first block >= 2022-08-08 13:30 UTC; captured resolution ledger
PROXY_SLOT = "0x7050c9e0f4ca769c69bd3a8ef740bc37934f8e2c036e5a723fd8ee048ed3f8c3"


def utc_now():
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def digest(data: bytes) -> str:
    return "sha256:" + hashlib.sha256(data).hexdigest()


def dump(path: Path, value) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n")


def http_once(url: str, payload: bytes | None = None, timeout: int = 12) -> dict:
    headers = {"User-Agent": "CensorshipCorpusFeasibility/1.0 (read-only academic measurement)", "Accept": "application/json" if payload else "*/*"}
    if payload:
        headers["Content-Type"] = "application/json"
    request = urllib.request.Request(url, data=payload, headers=headers)
    start = time.monotonic()
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            return {"http_status": response.status, "final_url": response.url,
                    "headers": dict(response.headers.items()), "body": response.read(),
                    "elapsed_seconds": round(time.monotonic() - start, 3), "transport_error": None}
    except urllib.error.HTTPError as exc:
        return {"http_status": exc.code, "final_url": exc.url,
                "headers": dict(exc.headers.items()), "body": exc.read(),
                "elapsed_seconds": round(time.monotonic() - start, 3), "transport_error": str(exc)}
    except (urllib.error.URLError, TimeoutError, OSError) as exc:
        return {"http_status": None, "final_url": url, "headers": {}, "body": b"",
                "elapsed_seconds": round(time.monotonic() - start, 3),
                "transport_error": f"{type(exc).__name__}: {exc}"}


def save_attempt(directory: Path, result: dict, request_bytes: bytes | None, request_url: str) -> dict:
    directory.mkdir(parents=True, exist_ok=False)
    body = result.pop("body")
    (directory / "response.body").write_bytes(body)
    if request_bytes is not None:
        (directory / "request.json").write_bytes(request_bytes)
    record = {**result, "retrieved_at_utc": utc_now(), "request_url": request_url,
              "response_body_sha256": digest(body), "response_bytes": len(body),
              "request_sha256": digest(request_bytes) if request_bytes is not None else None}
    dump(directory / "capture.json", record)
    return {**record, "body": body}


def validate_result(method: str, result):
    if method == "eth_chainId":
        if result != "0x1":
            raise ValueError("Ethereum mainnet chain ID not established")
    elif method == "eth_getBlockByNumber":
        if not isinstance(result, dict) or not all(key in result for key in ("number", "timestamp", "hash")):
            raise ValueError("Historical block missing or malformed")
    elif method == "eth_getLogs":
        if not isinstance(result, list):
            raise ValueError("Log response is not a list")
    else:
        if not isinstance(result, str) or not re.fullmatch(r"0x(?:[0-9a-fA-F]{2})*", result):
            raise ValueError("Missing or malformed hex result")
        if method == "eth_getCode" and result == "0x":
            raise ValueError("No contract code returned")
        if method in {"eth_call", "eth_getStorageAt"} and len(result) != 66:
            raise ValueError("Expected a 32-byte return word")
    return result


def rpc_query(endpoint: str, method: str, params: list, out: Path, transport=http_once, max_attempts: int = 2) -> dict:
    if method not in READ_METHODS:
        raise ValueError("Only explicitly allowlisted read methods may run")
    if max_attempts not in (1, 2):
        raise ValueError("Maximum two total attempts per query")
    payload = json.dumps({"jsonrpc": "2.0", "id": 1, "method": method, "params": params}, sort_keys=True).encode()
    attempts = []
    for number in range(1, max_attempts + 1):
        record = save_attempt(out / f"attempt_{number}", transport(endpoint, payload), payload, endpoint)
        try:
            if record["http_status"] != 200 or record["transport_error"]:
                raise ValueError(record["transport_error"] or f"HTTP {record['http_status']}")
            data = json.loads(record["body"])
            if not isinstance(data, dict) or data.get("jsonrpc") != "2.0" or data.get("id") != 1 or "error" in data or "result" not in data:
                raise ValueError(f"Invalid/RPC-error response: {data}")
            value = validate_result(method, data["result"])
            attempts.append({"number": number, "status": "valid_rpc_response"})
            return {"status": "valid_rpc_response", "method": method, "params": params, "result": value, "attempts": attempts}
        except (ValueError, TypeError, KeyError) as exc:
            attempts.append({"number": number, "status": "unavailable_or_invalid", "error": str(exc)})
            if number < max_attempts:
                time.sleep(0.2)
    return {"status": "gap", "method": method, "params": params, "result": None, "attempts": attempts}


def build_queries(pilot_block: int = PILOT_BLOCK) -> list[dict]:
    block, previous = hex(pilot_block), hex(pilot_block - 1)
    queries = [{"id": "chain_id", "method": "eth_chainId", "params": []},
               {"id": "historical_block", "method": "eth_getBlockByNumber", "params": [block, False]}]
    for name, contract in CONTRACTS.items():
        for label, at in (("latest", "latest"), ("historical", block)):
            queries.append({"id": f"{name}_code_{label}", "method": "eth_getCode", "params": [contract["address"], at]})
        for label, at in (("before", previous), ("after", block)):
            queries.append({"id": f"{name}_blacklist_state_{label}", "method": "eth_call",
                            "params": [{"to": contract["address"], "data": contract["selector"] + TARGET[2:].rjust(64, "0")}, at]})
        # USDT's address is non-indexed: query contract + event topics, then
        # match the address in data. Never add an imaginary address topic.
        topics = [contract["topics"]]
        if contract["indexed_address"]:
            topics.append("0x" + TARGET[2:].rjust(64, "0"))
        queries.append({"id": f"{name}_logs", "method": "eth_getLogs",
                        "params": [{"address": contract["address"], "fromBlock": previous, "toBlock": block, "topics": topics}]})
    queries.extend([
        {"id": "usdc_historical_implementation", "method": "eth_getStorageAt", "params": [CONTRACTS["usdc"]["address"], PROXY_SLOT, block]},
        {"id": "usdt_historical_deprecated", "method": "eth_call", "params": [{"to": CONTRACTS["usdt"]["address"], "data": "0x0e136b19"}, block]},
        {"id": "usdt_historical_upgraded_address", "method": "eth_call", "params": [{"to": CONTRACTS["usdt"]["address"], "data": "0x26976e3f"}, block]},
    ])
    return queries


def decode_target_logs(logs: list, contract: dict, target: str = TARGET, pilot_block: int = PILOT_BLOCK) -> list:
    selected = []
    target_word = target[2:].lower().rjust(64, "0")
    for log in logs:
        if not isinstance(log, dict):
            raise ValueError("Malformed log object")
        if log.get("address", "").lower() != contract["address"]:
            raise ValueError("Response contains a log for another contract")
        if not log.get("topics") or log["topics"][0].lower() not in contract["topics"] or log.get("removed") is True:
            raise ValueError("Unexpected or removed event log")
        try:
            in_range = pilot_block - 1 <= int(log["blockNumber"], 16) <= pilot_block
        except (KeyError, TypeError, ValueError):
            in_range = False
        if not in_range:
            raise ValueError("Event block missing or outside requested range")
        if contract["indexed_address"] and len(log["topics"]) != 2:
            raise ValueError("Indexed event address topic missing")
        location = log["topics"][1][2:] if contract["indexed_address"] else log.get("data", "")[2:66]
        if len(location) != 64:
            raise ValueError("Missing event address word")
        if location.lower() == target_word:
            selected.append(log)
    return selected


def run_pilot(out: Path, panel_manifest: Path, transport=http_once, pilot_block: int = PILOT_BLOCK,
              providers: tuple[str, ...] = tuple(ENDPOINTS)) -> dict:
    if out.exists():
        raise ValueError(f"Refusing to overwrite pilot run: {out}")
    panel = json.loads(panel_manifest.read_text())
    if not panel.get("pilot_contract_prerequisites_met"):
        raise ValueError("Required address/ABI source assertions have not been captured")
    queries = build_queries(pilot_block)
    manifest = {
        "study_role": "feasibility_pilot_excluded_from_evaluation", "created_before_outcome_queries_at_utc": utc_now(),
        "selection": "Tornado Cash training case; trigger-boundary block resolved by captured timestamp search. Known case selection is outcome-informed training, never evaluation sampling.",
        "excluded_episode_family": "tornado_cash", "target_address": TARGET,
        "historical_block": pilot_block, "historical_slice": [pilot_block - 1, pilot_block],
        "timestamp_check_window_utc": ["2022-08-08T00:00:00Z", "2022-08-09T00:00:00Z"],
        "full_protocol_window_covered": False, "full_cohort_execution": False,
        "max_attempts_per_query": 2, "panel_sidecar_sha256": digest(panel_manifest.read_bytes()),
        "endpoints": {name: ENDPOINTS[name] for name in providers}, "queries": queries,
        "collector_sha256": digest(Path(__file__).read_bytes()),
        "credential_required_not_queried": ["infura", "quicknode"],
        "behavioral_limit": "Present RPC access to historical chain data does not observe historical provider filtering, transaction inclusion, or private exchange behavior",
    }
    out.mkdir(parents=True)
    (out / "collector_source.py").write_bytes(Path(__file__).read_bytes())
    dump(out / "pilot_manifest.json", manifest)
    results = []
    for provider in providers:
        endpoint = ENDPOINTS[provider]
        chain_ok = False
        for query in queries:
            if query["id"] != "chain_id" and not chain_ok:
                result = {"status": "not_attempted_chain_identity_unavailable", "result": None, "attempts": [], "method": query["method"], "params": query["params"]}
            else:
                result = rpc_query(endpoint, query["method"], query["params"], out / "captures" / provider / query["id"], transport)
            if query["id"] == "chain_id":
                chain_ok = result["status"] == "valid_rpc_response"
            if query["id"] == "historical_block" and result["status"] == "valid_rpc_response":
                block = result["result"]
                stamp = datetime.fromtimestamp(int(block["timestamp"], 16), timezone.utc)
                if int(block["number"], 16) != pilot_block or stamp.date().isoformat() != "2022-08-08":
                    result.update(status="gap", validation_error="Block identity/time outside predeclared slice")
            if "blacklist_state" in query["id"] and result["status"] == "valid_rpc_response":
                if int(result["result"], 16) not in (0, 1):
                    result.update(status="gap", validation_error="Boolean return is not zero or one")
            if query["id"].endswith("_logs") and result["status"] == "valid_rpc_response":
                try:
                    result["target_logs"] = decode_target_logs(result["result"], CONTRACTS[query["id"].split("_")[0]], pilot_block=pilot_block)
                except ValueError as exc:
                    result.update(status="gap", validation_error=str(exc))
            results.append({"provider": provider, "query_id": query["id"], **result})
            dump(out / "results.json", results)
    summary = {"study_role": manifest["study_role"], "full_cohort_execution": False,
               "historical_provider_behavior_measured": False, "private_exchange_behavior_measured": False,
               "planned_queries": len(results), "attempted_queries": sum(bool(row["attempts"]) for row in results),
               "valid_rpc_responses": sum(row["status"] == "valid_rpc_response" for row in results),
               "gaps_or_dependency_skips": sum(row["status"] != "valid_rpc_response" for row in results),
               "completed_at_utc": utc_now(), "independent_chain_reconciliation_complete": False}
    dump(out / "summary.json", summary)
    return summary


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out-dir", type=Path, required=True)
    parser.add_argument("--panel-manifest", type=Path, default=ROOT / "sources/measurement_panel/verified_panel.json")
    parser.add_argument("--pilot-block", type=int, default=PILOT_BLOCK)
    parser.add_argument("--providers", nargs="+", choices=list(ENDPOINTS), default=list(ENDPOINTS))
    args = parser.parse_args()
    print(json.dumps(run_pilot(args.out_dir, args.panel_manifest, pilot_block=args.pilot_block, providers=tuple(args.providers)), indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
