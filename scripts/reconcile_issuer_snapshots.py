#!/usr/bin/env python3
"""Bounded cross-transport agreement for a source-ordered snapshot subset.

Separate public transports do not establish independent upstream operators.
One attempt per query/provider; a provider stops immediately on rate limits.
"""
from __future__ import annotations

import argparse
from collections import defaultdict
import json
import time
from pathlib import Path

from collect_issuer_cohort_snapshots import validate_existing_captures
from measurement_pilot import ROOT, digest, dump, http_once, rpc_query, utc_now

PROVIDERS = {"drpc_public": "https://eth.drpc.org/", "one_rpc_public": "https://public.1rpc.io/eth"}
COHORT = ROOT / "analysis/issuer_candidate_snapshots/cohort_endpoint_v1"
READS = {"eth_chainId", "eth_getBlockByNumber", "eth_getCode", "eth_getStorageAt", "eth_call"}


def validate_cached_capture(directory, query, result):
    capture = json.loads((directory / "attempt_1/capture.json").read_text())
    payload = (directory / "attempt_1/request.json").read_bytes()
    request = json.loads(payload)
    body = (directory / "attempt_1/response.body").read_bytes()
    if (capture["response_body_sha256"] != digest(body) or capture["request_sha256"] != digest(payload)
            or request != {"jsonrpc": "2.0", "id": 1, "method": query["method"], "params": query["params"]}):
        raise ValueError("Cached request/response hash or identity mismatch")
    if result.get("rpc_result", {}).get("status") == "valid_rpc_response":
        actual = comparison(query["method"], json.loads(body)["result"])
        expected_status = "cross_transport_match" if actual == query["expected_comparison"] else "cross_transport_disagreement"
        if result["comparison_value"] != actual or result["status"] != expected_status:
            raise ValueError("Cached derived result differs from captured response")


def comparison(method, value):
    if method == "eth_getBlockByNumber":
        return {"number": int(value["number"], 16), "hash": value["hash"].lower(), "timestamp": int(value["timestamp"], 16)}
    if method == "eth_getCode":
        return {"code_sha256": digest(bytes.fromhex(value[2:]))}
    return value.lower()


def prepare(out, cohort=COHORT, max_requests=300):
    if out.exists() or not 1 <= max_requests <= 300:
        raise ValueError("New output and total request budget1..300 required")
    summary = json.loads((cohort / "summary.json").read_text())
    if not summary.get("endpoint_snapshot_campaign_complete"):
        raise ValueError("Completed source-frozen cohort snapshots required")
    validate_existing_captures(cohort)
    queries = {}
    for path in sorted((cohort / "captures").glob("*/result.json")):
        row = json.loads(path.read_text())
        if row["method"] not in READS or row["status"] != "valid_rpc_response":
            raise ValueError("Source query is not a validated endpoint read")
        qid = row["query_id"]
        payload = (path.parent / "request.json").read_bytes()
        if digest(payload).split(":")[1] != qid:
            raise ValueError("Source request identity mismatch")
        if json.loads(payload) != {"jsonrpc": "2.0", "id": 1, "method": row["method"], "params": row["params"]}:
            raise ValueError("Source result/request mismatch")
        latest = sorted(path.parent.glob("attempt_*/response.body"))[-1]
        if json.loads(latest.read_bytes()).get("result") != row["result"]:
            raise ValueError("Source derived result differs from captured response")
        queries[qid] = {"id": qid, "method": row["method"], "params": row["params"],
                        "expected_comparison": comparison(row["method"], row["result"]),
                        "source_result_sha256": digest(path.read_bytes())}
    chain_ids = [qid for qid, row in queries.items() if row["method"] == "eth_chainId"]
    if len(chain_ids) != 1:
        raise ValueError("Exactly one source mainnet identity query required")
    chain_id = chain_ids[0]
    headers = {int(row["params"][0], 16): qid for qid, row in queries.items() if row["method"] == "eth_getBlockByNumber"}
    snapshots = [json.loads(path.read_text()) for path in sorted((cohort / "snapshots").glob("*.json"))]
    groups = defaultdict(list)
    dependencies, all_required = {chain_id: []}, {chain_id}
    for snapshot in snapshots:
        groups[snapshot["window_id"]].append(snapshot)
        block, issuer = snapshot["block_number"], snapshot["issuer"]
        header = headers[block]
        prereq = json.loads((cohort / "prerequisites" / f"{issuer}_{block}.json").read_text())["query_ids"]
        dependencies[header] = [chain_id]
        for qid in prereq:
            dependencies[qid] = [chain_id, header]
        dependencies[snapshot["state_query_id"]] = [chain_id, header] + prereq
        all_required.update([header, snapshot["state_query_id"]] + prereq)
    ordered = sorted(groups, key=lambda key: (min(row["block_number"] for row in groups[key]), groups[key][0]["action_url"]))
    selected, selected_windows, selected_snapshots = {chain_id}, [], []
    for window in ordered:
        needed = set()
        for snapshot in groups[window]:
            qid = snapshot["state_query_id"]
            needed.update([qid] + dependencies[qid])
        proposed = selected | needed
        if len(proposed) * len(PROVIDERS) > max_requests:
            break
        selected, selected_windows = proposed, selected_windows + [window]
        selected_snapshots += groups[window]
    if not selected_windows:
        raise ValueError("Budget cannot include the earliest complete action window")
    priorities = {"eth_chainId": 0, "eth_getBlockByNumber": 1, "eth_getCode": 2, "eth_getStorageAt": 2, "eth_call": 2}
    state_ids = {row["state_query_id"] for row in selected_snapshots}
    chosen = []
    for qid in sorted(selected, key=lambda q: (3 if q in state_ids else priorities[queries[q]["method"]], q)):
        chosen.append({**queries[qid], "dependencies": dependencies[qid], "is_target_state_query": qid in state_ids})
    source_docs = {}
    for provider, endpoint in PROVIDERS.items():
        path = ROOT / "sources/measurement_panel/expanded_transport_sources" / provider / "attempt_1/response.body"
        meta = json.loads(path.with_name("capture.json").read_text())
        if meta["http_status"] != 200 or meta["response_body_sha256"] != digest(path.read_bytes()) or endpoint not in path.read_text():
            raise ValueError("Current official endpoint source not verified")
        source_docs[provider] = {"endpoint": endpoint, "documentation_sha256": digest(path.read_bytes())}
    manifest = {"created_before_queries_at_utc": utc_now(),
                "study_role": "source_defined_partial_cross_transport_agreement_human_reference_pending",
                "selection_rule": "Largest earliest whole-action-window prefix fitting the fixed total request budget across both transports; no target response or event values used for selection",
                "source_cohort_manifest_sha256": digest((cohort / "collection_manifest.json").read_bytes()),
                "source_cohort_units_sha256": digest((cohort / "issuer_query_units.jsonl").read_bytes()),
                "source_cohort_summary_sha256": digest((cohort / "summary.json").read_bytes()),
                "collector_sha256": digest(Path(__file__).read_bytes()),
                "transport_source_sha256": digest(Path(__file__).with_name("measurement_pilot.py").read_bytes()),
                "source_validation_helper_sha256": digest(Path(__file__).with_name("collect_issuer_cohort_snapshots.py").read_bytes()),
                "providers": source_docs, "queries": chosen, "selected_window_ids": selected_windows,
                "selected_snapshot_units": selected_snapshots, "source_action_windows": len(groups),
                "full_source_cohort_queries_per_provider": len(all_required),
                "full_source_cohort_total_requests": len(all_required) * len(PROVIDERS),
                "queries_per_provider": len(chosen), "maximum_total_requests": len(chosen) * len(PROVIDERS),
                "explicit_total_request_budget": max_requests, "max_attempts_per_provider_query": 1,
                "minimum_delay_seconds": 0.5, "stop_rule": "Stop affected provider on first HTTP429/RPCrate-limit; retain gaps and all dependency skips; no retry or endpoint substitution",
                "upstream_operator_independence_verified": False, "full_cohort_reconciliation": False,
                "human_reference_complete": False, "causal_attribution_performed": False}
    out.mkdir(parents=True)
    dump(out / "plan.json", manifest)
    (out / "collector_source.py").write_bytes(Path(__file__).read_bytes())
    (out / "transport_source.py").write_bytes(Path(__file__).with_name("measurement_pilot.py").read_bytes())
    dump(out / "plan.sha256.json", {"plan_sha256": digest((out / "plan.json").read_bytes())})
    return {key: manifest[key] for key in ("source_action_windows", "selected_window_ids", "queries_per_provider", "maximum_total_requests", "full_source_cohort_total_requests")}


def run(out, transport=http_once):
    manifest = json.loads((out / "plan.json").read_text())
    if json.loads((out / "plan.sha256.json").read_text())["plan_sha256"] != digest((out / "plan.json").read_bytes()):
        raise ValueError("Frozen plan hash mismatch")
    if manifest["collector_sha256"] != digest(Path(__file__).read_bytes()) or manifest["transport_source_sha256"] != digest(Path(__file__).with_name("measurement_pilot.py").read_bytes()):
        raise ValueError("Running code differs from frozen plan")
    if len(manifest["queries"]) * len(manifest["providers"]) > min(300, manifest["explicit_total_request_budget"]):
        raise ValueError("Frozen request budget exceeded before network")
    reports, all_results = [], []
    for provider, config in manifest["providers"].items():
        if PROVIDERS.get(provider) != config["endpoint"]:
            raise ValueError("Unknown endpoint profile")
        completed, rate = {}, False
        for query in manifest["queries"]:
            qid = query["id"]
            base = {"provider": provider, "query_id": qid, "method": query["method"], "params": query["params"],
                    "is_target_state_query": query["is_target_state_query"]}
            directory = out / "captures" / provider / qid
            if rate:
                result = {**base, "status": "not_attempted_provider_rate_limit_stop", "attempted": False}
            elif any(completed.get(dep) != "cross_transport_match" for dep in query["dependencies"]):
                result = {**base, "status": "not_attempted_dependency_gap_or_disagreement", "attempted": False}
            else:
                result_file = out / "results" / provider / f"{qid}.json"
                if result_file.exists():
                    result = json.loads(result_file.read_text())
                    if result["query_id"] != qid or result["params"] != query["params"]:
                        raise ValueError("Cached reconciliation result mismatch")
                    validate_cached_capture(directory, query, result)
                elif directory.exists():
                    result = {**base, "status": "interrupted_single_attempt_consumed", "attempted": True}
                else:
                    if transport is http_once:
                        time.sleep(manifest["minimum_delay_seconds"])
                    directory.mkdir(parents=True)
                    dump(directory / "started.json", {"at_utc": utc_now(), "query_id": qid})
                    row = rpc_query(config["endpoint"], query["method"], query["params"], directory, transport, max_attempts=1)
                    status = "gap"
                    value = None
                    if row["status"] == "valid_rpc_response":
                        value = comparison(query["method"], row["result"])
                        status = "cross_transport_match" if value == query["expected_comparison"] else "cross_transport_disagreement"
                    result = {**base, "status": status, "attempted": True, "comparison_value": value,
                              "expected_comparison": query["expected_comparison"], "rpc_result": row}
                    dump(result_file, result)
                meta_file = directory / "attempt_1/capture.json"
                if meta_file.exists():
                    meta = json.loads(meta_file.read_text())
                    body = (directory / "attempt_1/response.body").read_text(errors="replace")
                    rate = meta["http_status"] == 429 or "rate limit" in body.lower() or "too many requests" in body.lower()
            completed[qid] = result["status"]
            all_results.append(result)
            dump(out / "results.json", all_results)
        reports.append({"provider": provider, "planned_queries": len(manifest["queries"]),
                        "attempted_queries": sum(row["provider"] == provider and row["attempted"] for row in all_results),
                        "matched_queries": sum(row["provider"] == provider and row["status"] == "cross_transport_match" for row in all_results),
                        "matched_target_state_queries": sum(row["provider"] == provider and row["is_target_state_query"] and row["status"] == "cross_transport_match" for row in all_results),
                        "rate_limit_stop": rate})
    summary = {"providers": reports, "maximum_total_requests": manifest["maximum_total_requests"],
               "attempted_queries": sum(row["attempted"] for row in all_results),
               "selected_action_windows": len(manifest["selected_window_ids"]),
               "selected_endpoint_snapshots": len(manifest["selected_snapshot_units"]),
               "upstream_operator_independence_verified": False, "full_cohort_reconciliation": False,
               "human_reference_complete": False, "causal_attribution_performed": False}
    dump(out / "summary.json", summary)
    return summary


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    p = sub.add_parser("prepare")
    p.add_argument("--out-dir", required=True, type=Path)
    p.add_argument("--cohort", type=Path, default=COHORT)
    p.add_argument("--max-requests", type=int, default=300)
    p = sub.add_parser("run")
    p.add_argument("--plan-dir", required=True, type=Path)
    args = parser.parse_args()
    print(json.dumps(prepare(args.out_dir, args.cohort, args.max_requests) if args.command == "prepare" else run(args.plan_dir), indent=2))


if __name__ == "__main__":
    main()
