#!/usr/bin/env python3
"""Deterministic offline aggregation of validation evidence and pending work.

Required inputs are cross-checked; absent optional results remain pending/null.
No network, human labels, event absence, timing or causal conclusions are inferred.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path

from validation_progress_ooni import audit_stage

ROOT = Path(__file__).resolve().parents[1]
VERSION = "1.1.0"
FRAME = "analysis/validation_frame/summary.json"
CANDIDATES = "analysis/issuer_candidate_manifest"
ENDPOINTS = "analysis/issuer_candidate_snapshots/cohort_endpoint_v1"
INTERFACE = "analysis/historical_interface_verification/v1/association_report.json"
DISCLOSURE = "analysis/disclosure_collection/summary.json"
OPTIONAL = {
    "blockscout_streams": "analysis/blockscout_issuer_logs/full_streams_v2/summary.json",
    "blockscout_matches": "analysis/blockscout_issuer_logs/cohort_matches_v2/summary.json",
    "ooni_main": "analysis/evidence_repairs/l0_ooni_daily_v1/summary.json",
    "ooni_retry": "analysis/evidence_repairs/l0_ooni_daily_retry_v1/summary.json",
    "ooni_raw": "sources/evidence_repairs/l0_ooni_raw_v1/summary.json",
    "ooni_jsonl": "sources/evidence_repairs/l0_ooni_s3_v1/summary.json",
    "ooni_postcan": "sources/evidence_repairs/l0_ooni_postcan_v2/summary.json",
    "cross_transport": "analysis/cross_transport_reconciliation/earliest_windows_v1/summary.json",
}
OONI_PROTOCOLS = {"ooni_raw": "analysis/evidence_repairs/l0_ooni_raw_protocol_v1",
                  "ooni_jsonl": "analysis/evidence_repairs/l0_ooni_s3_protocol_v1",
                  "ooni_postcan": "analysis/evidence_repairs/l0_ooni_postcan_protocol_v2"}
PAIR_LABELS = ("0/0", "0/1", "1/0", "1/1")


def serialized(value):
    return json.dumps(value, indent=2, sort_keys=True, ensure_ascii=False) + "\n"


def digest(raw):
    return "sha256:" + hashlib.sha256(raw).hexdigest()


def require(condition, message):
    if not condition:
        raise ValueError(message)


def count(value, label):
    require(type(value) is int and value >= 0, f"Invalid nonnegative count: {label}")
    return value


def equals(actual, expected, label):
    require(actual == expected, f"Count/identity mismatch for {label}: computed {actual!r}, declared {expected!r}")


class Inputs:
    def __init__(self, root):
        self.root, self.records = root, {}

    def read(self, relative, optional=False, lines=False):
        raw = self.blob(relative, optional)
        if raw is None:
            return None
        if lines:
            return [json.loads(line) for line in raw.decode().splitlines() if line.strip()]
        return json.loads(raw)

    def relative(self, path):
        path = Path(path)
        if path.is_absolute():
            # Captures retain original absolute paths; resolve their repository suffix
            # on another checkout without reading outside that checkout.
            positions = [i for i, part in enumerate(path.parts) if part in {"analysis", "sources"}]
            require(bool(positions), "Unrecognized captured absolute path")
            path = Path(*path.parts[positions[0]:])
        require(".." not in path.parts and not path.is_absolute(), "Input path escapes repository")
        return path.as_posix()

    def blob(self, relative, optional=False):
        relative = self.relative(relative)
        path = self.root / relative
        if not path.is_file():
            if not optional:
                raise ValueError(f"Required input missing: {relative}")
            self.records[relative] = {"status": "pending", "sha256": None, "bytes": None}
            return None
        raw = path.read_bytes()
        self.records[relative] = {"status": "present", "sha256": digest(raw), "bytes": len(raw)}
        return raw

    def verify_hash(self, path, expected):
        raw = self.blob(path)
        equals(digest(raw), expected, f"input hash {self.relative(path)}")
        return raw


def candidates(inputs, frame):
    manifest = inputs.read(f"{CANDIDATES}/manifest.json")
    measurements = inputs.read(f"{CANDIDATES}/measurement_units.jsonl", lines=True)
    units = inputs.read(f"{CANDIDATES}/issuer_query_units.jsonl", lines=True)
    equals(manifest["inputs"]["source_frame_input_hash"], frame["source_input_hash"], "source frame identity")
    if "source_frame_summary_sha256" in manifest["inputs"]:
        equals(manifest["inputs"]["source_frame_summary_sha256"], inputs.records[FRAME]["sha256"], "source frame summary hash")
    require(manifest["status"] == "machine_frozen_not_human_adjudicated" and manifest["human_gold"] is False,
            "Candidate input must retain its machine-proposed, unadjudicated status")
    by_measurement = {m["measurement_unit_id"]: m for m in measurements}
    require(len(by_measurement) == len(measurements), "Duplicate measurement IDs")
    keys = {(m["action_url"], m["normalized_address"], m["proposed_direction"]) for m in measurements}
    require(len(keys) == len(measurements), "Duplicate underlying measurement units")
    by_unit, crossing = {}, defaultdict(set)
    expected_issuers = {i["symbol"].lower(): i for i in manifest["issuers"]}
    equals(set(expected_issuers), {"usdc", "usdt"}, "canonical issuer panel")
    for unit in units:
        uid, mid = unit["issuer_query_id"], unit["measurement_unit_id"]
        require(uid not in by_unit, "Duplicate issuer query IDs")
        require(mid in by_measurement, "Issuer unit references unknown measurement")
        for field in ("action_url", "normalized_address", "proposed_direction", "window_start_inclusive_utc", "window_end_exclusive_utc"):
            equals(unit[field], by_measurement[mid][field], f"candidate {uid} {field}")
        issuer = unit["issuer"]["symbol"].lower()
        require(issuer in expected_issuers and issuer not in crossing[mid], "Unknown or duplicate issuer crossing")
        for field in ("chain_id", "contract_address"):
            equals(unit["issuer"][field], expected_issuers[issuer][field], f"issuer {field}")
        crossing[mid].add(issuer)
        by_unit[uid] = unit
    require(set(crossing) == set(by_measurement) and all(v == set(expected_issuers) for v in crossing.values()),
            "Each measurement must be crossed with both issuers")
    actions = {m["action_url"] for m in measurements}
    for name, value in (("measurement_units", len(measurements)), ("issuer_query_units", len(units)), ("unique_action_urls", len(actions))):
        equals(value, manifest["counts"][name], f"candidate {name}")
    if frame.get("machine_eth_entry_rows") is not None and manifest["counts"].get("source_rows") is not None:
        equals(frame["machine_eth_entry_rows"], manifest["counts"]["source_rows"], "candidate/frame ETH source rows")
    result = {"status": manifest["status"], "measurement_units": len(measurements), "issuer_units": len(units),
              "action_windows": len(actions), "human_eligibility_adjudication": "pending",
              "source_row_dispositions": manifest["counts"].get("source_row_dispositions")}
    return result, by_measurement, by_unit


def timestamp(value):
    parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    require(parsed.tzinfo is not None, "Candidate timestamp is missing its timezone")
    return int(parsed.timestamp())


def endpoints(inputs, by_measurement, by_unit):
    summary = inputs.read(f"{ENDPOINTS}/summary.json")
    directory = inputs.root / ENDPOINTS / "snapshots"
    require(directory.is_dir(), "Required endpoint snapshot directory missing")
    expected_windows = {(u["action_url"], u["window_start_inclusive_utc"], u["window_end_exclusive_utc"]) for u in by_unit.values()}
    windows, boundaries = {}, {}
    for path in sorted((inputs.root / ENDPOINTS / "windows").glob("*.json")):
        window = inputs.read(path.relative_to(inputs.root).as_posix())
        wid = window["window_id"]
        equals(path.name, f"{wid}.json", "window filename/identity")
        require(wid not in windows, "Duplicate window IDs")
        require((window["action_url"], window["start_inclusive_utc"], window["end_exclusive_utc"]) in expected_windows,
                "Endpoint window is outside frozen candidate frame")
        windows[wid] = window
    equals(len(windows), summary["action_window_records"], "endpoint action window records")
    rows, pairs = [], defaultdict(dict)
    for path in sorted(directory.glob("*.json")):
        row = inputs.read(path.relative_to(inputs.root).as_posix())
        uid, label = row["issuer_query_id"], row["snapshot"]
        require(uid in by_unit, f"Snapshot for unknown issuer unit: {uid}")
        require(label in {"window_first_block", "window_last_block"}, "Unexpected endpoint snapshot label")
        equals(path.name, f"{uid}_{label}.json", "snapshot filename/identity")
        require(label not in pairs[uid], "Duplicate endpoint snapshot")
        unit = by_unit[uid]
        for snapshot_field, candidate_field in (("measurement_unit_id", "measurement_unit_id"), ("action_url", "action_url"), ("target_address", "normalized_address")):
            equals(row[snapshot_field], unit[candidate_field], f"snapshot {uid} {snapshot_field}")
        equals(row["issuer"], unit["issuer"]["symbol"].lower(), "snapshot issuer")
        wid = row["window_id"]
        require(wid in windows, "Snapshot references an unknown recorded window")
        window = windows[wid]
        equals((window["action_url"], window["start_inclusive_utc"], window["end_exclusive_utc"]),
               (unit["action_url"], unit["window_start_inclusive_utc"], unit["window_end_exclusive_utc"]), "snapshot window binding")
        if wid not in boundaries:
            boundaries[wid] = inputs.read(f"{ENDPOINTS}/boundaries/{wid}.json")
            for side, field in (("start", "start_inclusive_utc"), ("end", "end_exclusive_utc")):
                boundary = boundaries[wid][side]
                equals(boundary["requested_timestamp"], timestamp(window[field]), "boundary requested timestamp")
                equals(boundary["before_block"] + 1, boundary["at_or_after_block"], "boundary adjacent blocks")
                require(boundary["before_timestamp"] < boundary["requested_timestamp"] <= boundary["at_or_after_timestamp"],
                        "Boundary timestamps do not straddle the requested time")
        boundary, prefix = (boundaries[wid]["start"], "at_or_after") if label == "window_first_block" else (boundaries[wid]["end"], "before")
        for snapshot_field, suffix in (("block_number", "block"), ("block_hash", "hash"), ("timestamp", "timestamp")):
            equals(row[snapshot_field], boundary[f"{prefix}_{suffix}"], f"snapshot {snapshot_field} exact boundary")
        count(row["block_number"], "snapshot block")
        count(row["timestamp"], "snapshot timestamp")
        require(timestamp(unit["window_start_inclusive_utc"]) <= row["timestamp"] < timestamp(unit["window_end_exclusive_utc"]),
                "Snapshot timestamp outside half-open candidate window")
        if row["state_query_status"] == "valid_rpc_response":
            require(row.get("rpc_code_and_forwarding_prerequisites_pass") is True,
                    "Counted endpoint state lacks passing historical prerequisites")
            require(type(row["returned_blacklist_word"]) is int and row["returned_blacklist_word"] in (0, 1), "Invalid endpoint boolean word")
        else:
            require(row["returned_blacklist_word"] is None, "Endpoint gap must not contain an interpreted state word")
        require(row.get("full_window_response_classification") is None, "Endpoint record contains unsupported window classification")
        pairs[uid][label] = row
        rows.append(row)
    pair_counts = {issuer: {label: 0 for label in PAIR_LABELS} for issuer in ("usdc", "usdt")}
    complete = set()
    for uid, points in pairs.items():
        if set(points) != {"window_first_block", "window_last_block"}:
            continue
        first, last = points["window_first_block"], points["window_last_block"]
        require(first["block_number"] <= last["block_number"] and first["timestamp"] <= last["timestamp"], "Endpoint order is reversed")
        if all(r["state_query_status"] == "valid_rpc_response" for r in points.values()):
            complete.add(uid)
            pair_counts[first["issuer"]][f"{first['returned_blacklist_word']}/{last['returned_blacklist_word']}"] += 1
    complete_measurements = {mid for mid in by_measurement if all(uid in complete for uid, unit in by_unit.items() if unit["measurement_unit_id"] == mid)}
    comparisons = {"recorded_snapshots": len(rows), "valid_endpoint_snapshots": sum(r["state_query_status"] == "valid_rpc_response" for r in rows),
                   "issuer_units_with_two_valid_snapshots": len(complete), "measurement_units_with_four_valid_snapshots": len(complete_measurements),
                   "planned_issuer_query_units": len(by_unit), "planned_measurement_units": len(by_measurement),
                   "issuer_units_incomplete_or_gap": sorted(set(by_unit) - complete),
                   "measurement_units_incomplete_or_gap": sorted(set(by_measurement) - complete_measurements),
                   "endpoint_snapshot_campaign_complete": complete == set(by_unit)}
    for key, value in comparisons.items():
        equals(value, summary[key], f"endpoint summary {key}")
    require(summary.get("full_window_response_classification") is None, "Endpoint summary contains unsupported window classification")
    return {"status": "complete_endpoint_pairs" if comparisons["endpoint_snapshot_campaign_complete"] else "partial_endpoint_pairs",
            **comparisons, "pair_counts": pair_counts,
            "logical_queries_reserved": summary.get("logical_queries_reserved"), "http_attempts_captured": summary.get("http_attempts_captured"),
            "interpretation": "First/last states inside half-open windows; equal pairs do not establish event absence. No exact transition time or causal inference."}


def interface(inputs):
    report = inputs.read(INTERFACE)
    entries = report["entries"]
    require(len({(e["address"], e["historical_runtime_bytes_sha256"]) for e in entries}) == len(entries), "Duplicate historical interface entries")
    matches = sum(e["indexed_runtime_equals_observed_historical_bytes"] is True for e in entries)
    abi = sum(e["compatible_read_abi_entry_present"] is True and bool(e["indexed_runtime_push4_selector_offsets"]) for e in entries)
    equals(matches, report["indexed_runtime_hash_matches"], "interface runtime matches")
    equals(abi, report["compatible_abi_and_push4_selector_matches"], "interface ABI/selector matches")
    return {"status": "captured_metadata_comparison", "code_address_entries": len(entries), "indexed_runtime_hash_matches": matches,
            "compatible_abi_selector_matches": abi,
            "provider_runtime_match_literals": dict(sorted(Counter(e["sourcify_runtime_match_literal"] for e in entries).items())),
            "exact_source_metadata_verification_established": report["exact_source_metadata_verification_established"],
            "local_compiler_reproduction_complete": report["historical_implementation_bytecode_reproduced"]}


def disclosures(inputs, machine):
    report = inputs.read(DISCLOSURE)
    equals(report["source_action_urls"], machine["action_windows"], "disclosure action windows")
    equals(report["candidate_target_units"], machine["measurement_units"], "disclosure target units")
    operators = report["operators"]
    require(len({o["operator"] for o in operators}) == len(operators), "Duplicate disclosure operators")
    equals(report["operator_action_windows"], machine["action_windows"] * len(operators), "disclosure operator windows")
    equals(report["candidate_target_operator_units"], machine["measurement_units"] * len(operators), "disclosure crossed units")
    merged = Counter()
    for operator in operators:
        equals(operator["action_windows"], machine["action_windows"], "operator action windows")
        outcomes = operator["target_unit_outcomes"]
        equals(sum(count(v, "disclosure outcome") for v in outcomes.values()), machine["measurement_units"], "operator outcome total")
        merged.update(outcomes)
    equals(dict(merged), report["outcome_counts"], "disclosure outcome totals")
    require(report["human_reference_complete"] is False and report["private_account_action_measured"] is False,
            "Machine public-disclosure summary cannot supply human references or private account outcomes")
    return {"status": report["status"], "operator_action_windows": report["operator_action_windows"],
            "candidate_target_operator_units": report["candidate_target_operator_units"], "outcome_counts": report["outcome_counts"],
            "negative_scope": report["negative_scope"], "private_account_action_measured": report["private_account_action_measured"],
            "human_reference_complete": report["human_reference_complete"]}


def optional_component(inputs, name, keys):
    data = inputs.read(OPTIONAL[name], optional=True)
    if data is None:
        return {"status": "pending", "source_path": OPTIONAL[name], "metrics": None}, None
    metrics = {key: data.get(key) for key in keys}
    for key, value in metrics.items():
        if type(value) is int:
            count(value, f"{name}.{key}")
    return {"status": "available", "source_path": OPTIONAL[name], "reported_status": data.get("status"), "metrics": metrics}, data


def ooni_effective_queries(inputs, main, retry):
    """Merge query completion only after verifying the frozen retry membership."""
    paths = {"main_manifest": str(Path(OPTIONAL["ooni_main"]).with_name("manifest.json")),
             "main_rows": str(Path(OPTIONAL["ooni_main"]).with_name("query_summaries.json")),
             "retry_manifest": str(Path(OPTIONAL["ooni_retry"]).with_name("manifest.json")),
             "retry_rows": str(Path(OPTIONAL["ooni_retry"]).with_name("query_summaries.json"))}
    data = {key: inputs.read(path, optional=True) for key, path in paths.items()}
    if main is None or retry is None or any(v is None for v in data.values()):
        return {"status": "pending", "source_paths": paths, "metrics": None,
                "reason": "Both summaries and frozen query-level manifests/results are required to verify the retry subset."}
    def indexed(rows, nested=False):
        result = {}
        for row in rows:
            query = row["query"] if nested else row
            qid = query["query_id"]
            require(qid not in result, "Duplicate OONI query IDs")
            result[qid] = row
        return result
    frozen_main = indexed(data["main_manifest"]["queries"])
    frozen_retry = indexed(data["retry_manifest"]["queries"])
    main_rows, retry_rows = indexed(data["main_rows"], True), indexed(data["retry_rows"], True)
    equals(set(main_rows), set(frozen_main), "OONI main result membership")
    equals(set(retry_rows), set(frozen_retry), "OONI retry result membership")
    equals(len(main_rows), main["query_count"], "OONI main query ledger count")
    equals(len(retry_rows), retry["retry_query_count"], "OONI retry query ledger count")
    equals(len(frozen_main), data["main_manifest"]["query_count"], "OONI frozen main count")
    equals(len(frozen_retry), data["retry_manifest"]["retry_query_count"], "OONI frozen retry count")
    for qid, row in main_rows.items():
        equals(row["query"], frozen_main[qid], "OONI main frozen query")
        require(type(row["pagination_complete"]) is bool, "OONI pagination status must be explicit")
    completed_main = {qid for qid, row in main_rows.items() if row["pagination_complete"]}
    incomplete_main = set(main_rows) - completed_main
    require(set(frozen_retry) <= incomplete_main, "OONI retry includes a query outside the main incomplete set")
    for qid, row in retry_rows.items():
        equals(row["query"], frozen_retry[qid], "OONI retry frozen query")
        equals(frozen_retry[qid], frozen_main[qid], "OONI retry preserves original query parameters")
        require(type(row["pagination_complete"]) is bool, "OONI retry pagination status must be explicit")
    completed_retry = {qid for qid, row in retry_rows.items() if row["pagination_complete"]}
    equals(len(completed_main), main["complete_queries"], "OONI complete main query ledger")
    equals(len(completed_retry), retry["completed_retries"], "OONI completed retry ledger")
    for source_field, path in (("source_manifest_sha256", paths["main_manifest"]),
                               ("source_query_summaries_sha256", paths["main_rows"]),
                               ("source_summary_sha256", OPTIONAL["ooni_main"])):
        equals(data["retry_manifest"][source_field], inputs.records[path]["sha256"], f"OONI retry {source_field}")
    effective = completed_main | completed_retry
    return {"status": "verified_retry_overlay", "source_paths": paths,
            "metrics": {"frozen_main_queries": len(main_rows), "main_complete_queries": len(completed_main),
                        "verified_retry_complete_queries": len(completed_retry), "effective_complete_queries": len(effective),
                        "effective_incomplete_queries": len(main_rows) - len(effective), "retry_is_subset_of_main_incomplete": True},
            "interpretation": "Repairs query retrieval coverage only; not an independent-probe count or censorship label."}


def rpc_comparison(method, value):
    if method == "eth_getBlockByNumber":
        return {"number": int(value["number"], 16), "hash": value["hash"].lower(), "timestamp": int(value["timestamp"], 16)}
    if method == "eth_getCode":
        return {"code_sha256": digest(bytes.fromhex(value[2:]))}
    return value.lower()


def cross_transport(inputs):
    component, report = optional_component(inputs, "cross_transport", ())
    if report is None:
        return component
    directory = str(Path(OPTIONAL["cross_transport"]).parent)
    plan = inputs.read(f"{directory}/plan.json")
    seal = inputs.read(f"{directory}/plan.sha256.json")
    equals(inputs.records[f"{directory}/plan.json"]["sha256"], seal["plan_sha256"], "cross-transport frozen plan")
    for field, path in (("collector_sha256", f"{directory}/collector_source.py"),
                        ("transport_source_sha256", f"{directory}/transport_source.py"),
                        ("source_cohort_manifest_sha256", f"{ENDPOINTS}/collection_manifest.json"),
                        ("source_cohort_summary_sha256", f"{ENDPOINTS}/summary.json"),
                        ("source_cohort_units_sha256", f"{CANDIDATES}/issuer_query_units.jsonl")):
        inputs.verify_hash(path, plan[field])
    if "source_validation_helper_sha256" in plan:
        inputs.verify_hash(f"{ENDPOINTS}/collector_source.py", plan["source_validation_helper_sha256"])
    for provider, config in plan["providers"].items():
        if "documentation_sha256" in config:
            inputs.verify_hash(f"sources/measurement_panel/expanded_transport_sources/{provider}/attempt_1/response.body", config["documentation_sha256"])
    for obj in (plan, report):
        for flag in ("upstream_operator_independence_verified", "full_cohort_reconciliation", "human_reference_complete", "causal_attribution_performed"):
            require(obj.get(flag) is False, f"Unsupported cross-transport scope flag: {flag}")
    queries = {q["id"]: q for q in plan["queries"]}
    equals(len(queries), len(plan["queries"]), "unique transport queries")
    equals(len(queries), plan["queries_per_provider"], "transport queries per provider")
    equals(plan["max_attempts_per_provider_query"], 1, "transport attempts cap")
    require(plan["minimum_delay_seconds"] >= 0.5, "Transport pacing violates frozen bound")
    equals(len(queries) * len(plan["providers"]), plan["maximum_total_requests"], "transport planned total")
    equals(plan["maximum_total_requests"], report["maximum_total_requests"], "transport summary budget")
    require(plan["maximum_total_requests"] <= plan["explicit_total_request_budget"], "Transport plan exceeds budget")
    for qid, query in queries.items():
        source = json.loads(inputs.verify_hash(f"{ENDPOINTS}/captures/{qid}/result.json", query["source_result_sha256"]))
        equals((source["method"], source["params"]), (query["method"], query["params"]), "transport primary query identity")
        equals(rpc_comparison(query["method"], source["result"]), query["expected_comparison"], "transport frozen comparison")
        require(set(query["dependencies"]) <= set(queries), "Unknown transport dependency")
    snapshots, window_ids = plan["selected_snapshot_units"], plan["selected_window_ids"]
    equals(len(window_ids), len(set(window_ids)), "unique selected transport windows")
    snapshot_keys = set()
    for snapshot in snapshots:
        key = (snapshot["issuer_query_id"], snapshot["snapshot"])
        require(key not in snapshot_keys, "Duplicate selected transport snapshot")
        snapshot_keys.add(key)
        primary = inputs.read(f"{ENDPOINTS}/snapshots/{key[0]}_{key[1]}.json")
        equals(snapshot, primary, "transport selected snapshot primary binding")
        require(snapshot["window_id"] in window_ids, "Selected transport snapshot outside window subset")
        require(snapshot["state_query_id"] in queries and queries[snapshot["state_query_id"]]["is_target_state_query"] is True,
                "Selected snapshot lacks its frozen target state query")
    expected_keys = set()
    for path in sorted((inputs.root / ENDPOINTS / "snapshots").glob("*.json")):
        row = inputs.read(path.relative_to(inputs.root).as_posix())
        if row["window_id"] in window_ids:
            expected_keys.add((row["issuer_query_id"], row["snapshot"]))
    equals(snapshot_keys, expected_keys, "transport whole-window subset")
    equals({s["window_id"] for s in snapshots}, set(window_ids), "selected transport windows have snapshots")
    equals({s["state_query_id"] for s in snapshots}, {q["id"] for q in queries.values() if q["is_target_state_query"]}, "transport state-query membership")
    rows = inputs.read(f"{directory}/results.json")
    by_provider = defaultdict(dict)
    captures = defaultdict(dict)
    for row in rows:
        provider, qid = row["provider"], row["query_id"]
        require(provider in plan["providers"] and qid in queries, "Foreign transport result")
        require(qid not in by_provider[provider], "Duplicate transport result")
        query = queries[qid]
        for field in ("method", "params", "is_target_state_query"):
            equals(row[field], query[field], f"transport result {field}")
        require(type(row["attempted"]) is bool, "Transport attempt flag must be explicit")
        if row["attempted"]:
            equals(row, inputs.read(f"{directory}/results/{provider}/{qid}.json"), "transport result ledger copy")
            capture_dir = f"{directory}/captures/{provider}/{qid}/attempt_1"
            attempt_paths = list((inputs.root / capture_dir).parent.glob("attempt_*"))
            equals({p.name for p in attempt_paths}, {"attempt_1"}, "transport filesystem attempt cap")
            meta = inputs.read(f"{capture_dir}/capture.json")
            request = json.loads(inputs.verify_hash(f"{capture_dir}/request.json", meta["request_sha256"]))
            body = inputs.verify_hash(f"{capture_dir}/response.body", meta["response_body_sha256"])
            equals(request, {"jsonrpc": "2.0", "id": 1, "method": query["method"], "params": query["params"]}, "transport captured request")
            equals(meta["request_url"], plan["providers"][provider]["endpoint"], "transport frozen endpoint")
            equals(len(row["rpc_result"]["attempts"]), 1, "transport captured attempt count")
            if row["rpc_result"]["status"] == "valid_rpc_response":
                require(meta["http_status"] == 200 and not meta.get("transport_error"), "Matched transport has failed HTTP response")
                response = json.loads(body)
                equals(response["result"], row["rpc_result"]["result"], "transport raw RPC result")
                actual = rpc_comparison(query["method"], response["result"])
                equals(actual, row["comparison_value"], "transport comparison recomputation")
                equals(row["status"], "cross_transport_match" if actual == query["expected_comparison"] else "cross_transport_disagreement", "transport match status")
            else:
                equals(row["status"], "gap", "transport invalid RPC status")
            body_text = body.decode(errors="replace").lower()
            captures[provider][qid] = meta["http_status"] == 429 or "rate limit" in body_text or "too many requests" in body_text
        else:
            require(row["status"] in {"not_attempted_provider_rate_limit_stop", "not_attempted_dependency_gap"}, "Invalid transport skip status")
        by_provider[provider][qid] = row
    equals(set(by_provider), set(plan["providers"]), "transport provider membership")
    captured_keys = {(p.parent.parent.name, p.parent.name)
                     for p in (inputs.root / directory / "captures").glob("*/*/attempt_1")}
    equals(captured_keys, {(p, q) for p, outcomes in by_provider.items() for q, r in outcomes.items() if r["attempted"]},
           "transport captured/attempted query membership")
    declared = {row["provider"]: row for row in report["providers"]}
    equals(len(declared), len(report["providers"]), "unique transport provider summaries")
    equals(set(declared), set(plan["providers"]), "transport provider summary membership")
    providers = []
    for provider, outcomes in sorted(by_provider.items()):
        equals(set(outcomes), set(queries), "complete transport result ledger")
        stopped = False
        for query in plan["queries"]:
            row = outcomes[query["id"]]
            if stopped:
                require(not row["attempted"] and row["status"] == "not_attempted_provider_rate_limit_stop", "Transport continued after rate-limit stop")
            elif row["status"] == "not_attempted_provider_rate_limit_stop":
                require(False, "Transport claims rate stop before captured rate error")
            if row["attempted"]:
                require(all(outcomes[d]["status"] == "cross_transport_match" for d in query["dependencies"]), "Transport queried after failed prerequisite")
            elif row["status"] == "not_attempted_dependency_gap":
                require(any(outcomes[d]["status"] != "cross_transport_match" for d in query["dependencies"]), "Unsupported transport dependency skip")
            stopped = stopped or captures[provider].get(query["id"], False)
        computed = {"provider": provider, "planned_queries": len(queries), "attempted_queries": sum(r["attempted"] for r in outcomes.values()),
                    "matched_queries": sum(r["status"] == "cross_transport_match" for r in outcomes.values()),
                    "matched_target_state_queries": sum(r["is_target_state_query"] and r["status"] == "cross_transport_match" for r in outcomes.values()),
                    "rate_limit_stop": stopped}
        equals(computed, declared[provider], "transport provider accounting")
        providers.append({**computed, "unissued_queries": len(queries) - computed["attempted_queries"]})
    for key, actual in (("attempted_queries", sum(p["attempted_queries"] for p in providers)),
                        ("selected_action_windows", len(window_ids)), ("selected_endpoint_snapshots", len(snapshots))):
        equals(actual, report[key], f"transport summary {key}")
    component["metrics"] = {**report, "providers": providers, "selected_measurement_units": len({s["measurement_unit_id"] for s in snapshots}),
                            "selected_issuer_units": len({s["issuer_query_id"] for s in snapshots}), "captured_http_attempts": sum(len(v) for v in captures.values())}
    component["status"] = "verified_frozen_subset_accounting"
    component["interpretation"] = "Cross-transport agreement on a source-defined subset; shared upstreams remain possible. Not full-cohort reconciliation, independent reference labels, or causation."
    return component


def optional_evidence(inputs, machine):
    streams, raw_streams = optional_component(inputs, "blockscout_streams", ("all_four_index_ranges_complete", "accepted_unique_logs", "pages_captured", "independent_chain_completeness_verified"))
    if raw_streams is not None:
        stream_rows = raw_streams["streams"]
        require(len({s["stream"] for s in stream_rows}) == len(stream_rows), "Duplicate Blockscout stream summaries")
        equals(raw_streams["all_four_index_ranges_complete"], len(stream_rows) == 4 and all(s["index_range_complete"] for s in stream_rows), "Blockscout index coverage flag")
        equals(sum(s["pages_processed"] for s in stream_rows), raw_streams["pages_captured"], "Blockscout page total")
    matches, raw_matches = optional_component(inputs, "blockscout_matches", ("issuer_units", "measurement_units", "issuer_units_with_indexed_events", "measurement_units_with_indexed_events", "matching_event_associations", "unique_matching_event_identities", "indexed_stream_coverage_complete", "zero_is_not_no_action", "causal_attribution_performed", "event_trigger_interval_counts", "within_trigger_interval_order_indeterminate", "exact_trigger_latency_established"))
    if raw_matches is not None:
        equals(raw_matches["issuer_units"], machine["issuer_units"], "log matcher issuer units")
        equals(raw_matches["measurement_units"], machine["measurement_units"], "log matcher measurement units")
        require(raw_matches["issuer_units_with_indexed_events"] <= machine["issuer_units"], "Log match issuer count exceeds frame")
        require(raw_matches["measurement_units_with_indexed_events"] <= machine["measurement_units"], "Log match measurement count exceeds frame")
        require(raw_matches["zero_is_not_no_action"] is True and raw_matches["causal_attribution_performed"] is False, "Log matcher scope flags changed")
        if "event_trigger_interval_counts" in raw_matches:
            equals(sum(count(v, "event interval count") for v in raw_matches["event_trigger_interval_counts"].values()), raw_matches["matching_event_associations"], "event/trigger interval accounting")
            require(raw_matches["within_trigger_interval_order_indeterminate"] is True and raw_matches["exact_trigger_latency_established"] is False, "Log timing uncertainty flags changed")
        if raw_streams is not None:
            equals(raw_matches["indexed_stream_coverage_complete"], raw_streams["all_four_index_ranges_complete"], "log matcher/index coverage")
    main, raw_main = optional_component(inputs, "ooni_main", ("query_count", "complete_queries", "failed_or_incomplete_queries", "metadata_rows"))
    retry, raw_retry = optional_component(inputs, "ooni_retry", ("retry_query_count", "completed_retries", "still_incomplete", "metadata_rows"))
    if raw_main is not None:
        equals(raw_main["complete_queries"] + raw_main["failed_or_incomplete_queries"], raw_main["query_count"], "OONI main query accounting")
    if raw_retry is not None:
        equals(raw_retry["completed_retries"] + raw_retry["still_incomplete"], raw_retry["retry_query_count"], "OONI retry accounting")
    raw, raw_result = optional_component(inputs, "ooni_raw", ("frozen_metadata_rows", "frozen_raw_urls", "raw_urls_attempted", "url_status_counts", "identity_valid_metadata_rows", "invalid_locator_rows", "http_attempts", "censorship_finding", "human_review_complete"))
    if raw_result is not None:
        raw["metrics"] = audit_stage(inputs, "ooni_raw", raw_result)
        raw["status"] = "verified_frozen_stage_accounting"
    fallbacks = {}
    for name, label in (("ooni_jsonl", "jsonl_fallback"), ("ooni_postcan", "postcan_fallback")):
        component, report = optional_component(inputs, name, ())
        if report is not None:
            component["metrics"] = audit_stage(inputs, name, report)
            component["status"] = "verified_frozen_stage_accounting"
        fallbacks[label] = component
    overlay = ooni_effective_queries(inputs, raw_main, raw_retry)
    return {"event_logs": {"index_stream_collection": streams, "candidate_event_matching": matches,
                           "interpretation": "Indexed event records are distinct from endpoint pairs; index coverage is not independently verified chain completeness or causation."},
            "cross_transport": cross_transport(inputs),
            "ooni": {"main_metadata": main, "retry_metadata": retry, "effective_query_coverage": overlay, "raw_measurements": raw, **fallbacks,
                     "raw_stage_counts_are_additive": False,
                     "interpretation": "Raw API, UID-free JSONL scanning, and postcan UID recovery are separate retrieval stages of the same selected metadata. Earlier gaps remain recorded; stage counts must not be added as distinct measurements. No censorship finding or human adjudication is inferred."}}


def build(root):
    inputs = Inputs(root)
    frame = inputs.read(FRAME)
    for key in ("enumerated_action_urls", "retrieved_action_pages", "unretrieved_action_pages", "body_parsed_pages"):
        count(frame[key], key)
    equals(frame["retrieved_action_pages"] + frame["unretrieved_action_pages"], frame["enumerated_action_urls"], "frame retrieval accounting")
    require(frame["body_parsed_pages"] <= frame["retrieved_action_pages"], "Parsed frame pages exceed retrieved pages")
    for key in ("machine_eth_entry_rows", "action_pages_with_explicit_eth"):
        if frame.get(key) is not None:
            count(frame[key], key)
    if frame.get("action_pages_with_explicit_eth") is not None:
        require(frame["action_pages_with_explicit_eth"] <= frame["body_parsed_pages"], "ETH pages exceed parsed frame pages")
    machine, measurements, units = candidates(inputs, frame)
    endpoint = endpoints(inputs, measurements, units)
    interfaces, disclosure = interface(inputs), disclosures(inputs, machine)
    optional = optional_evidence(inputs, machine)
    dependency_hashes = {}
    for name in ("validation_progress_ooni.py", "collect_ooni_raw_measurements.py"):
        raw = inputs.blob(f"scripts/{name}") if (root / "scripts" / name).exists() else Path(__file__).with_name(name).read_bytes()
        dependency_hashes[name] = digest(raw)
    provenance = dict(sorted(inputs.records.items()))
    return {"schema_version": VERSION, "procedure": "offline_cross_checked_validation_progress",
            "procedure_sha256": digest(Path(__file__).read_bytes()), "input_hash": digest(serialized(provenance).encode()), "inputs": provenance,
            "procedure_dependency_sha256": dependency_hashes,
            "source_frame": {k: frame.get(k) for k in ("enumerated_action_urls", "retrieved_action_pages", "unretrieved_action_pages", "body_parsed_pages", "source_input_hash", "machine_eth_entry_rows", "action_pages_with_explicit_eth")},
            "machine_candidates": machine, "endpoint_contrasts": endpoint, "historical_interfaces": interfaces,
            "public_disclosures": disclosure, **optional,
            "human_reference": {"status": "pending", "independently_adjudicated_label_count": None,
                                "reason": "No independently adjudicated reference-label artifact is an input to this progress aggregator."},
            "interpretation": "Machine selection, endpoint contrasts, indexed events and human references are separate evidence stages. No event absence, exact response time, causal response, or censorship finding is inferred."}


def value(value):
    return "pending" if value is None else str(value)


def markdown(result):
    m, e, h, d = (result[key] for key in ("machine_candidates", "endpoint_contrasts", "historical_interfaces", "public_disclosures"))
    lines = ["# Validation progress", "", "Generated offline from cross-checked local artifacts; no retrieval is triggered.", "",
             f"Input hash: `{result['input_hash']}`. Per-file hashes and missing-input markers are in `summary.json`.", "",
             "| Evidence stage | Current scope/status |", "|---|---|",
             f"| Source frame | {result['source_frame']['retrieved_action_pages']}/{result['source_frame']['enumerated_action_urls']} enumerated action pages retrieved |",
             f"| Machine candidates | {m['measurement_units']} measurement units; {m['issuer_units']} issuer units; {m['action_windows']} action windows; eligibility adjudication pending |",
             f"| Endpoint contrasts | {e['valid_endpoint_snapshots']}/{2*m['issuer_units']} valid snapshots; {e['issuer_units_with_two_valid_snapshots']} paired issuer units; {e['status']} |",
             f"| Historical interfaces | {h['indexed_runtime_hash_matches']}/{h['code_address_entries']} indexed runtime hash matches; provider literals `{json.dumps(h['provider_runtime_match_literals'], sort_keys=True)}` |",
             f"| Public disclosures | {d['candidate_target_operator_units']} target/operator units; `{json.dumps(d['outcome_counts'], sort_keys=True)}` |",
             "| Human reference labels | pending; independently adjudicated count unavailable |", "",
             "## Recomputed endpoint pairs", "", "| Issuer | 0/0 | 0/1 | 1/0 | 1/1 |", "|---|---:|---:|---:|---:|"]
    for issuer, pairs in e["pair_counts"].items():
        lines.append(f"| {issuer.upper()} | " + " | ".join(str(pairs[key]) for key in PAIR_LABELS) + " |")
    lines += ["", "Pairs use first/last states inside declared windows. Equal pairs do not establish no intervening event; different pairs do not establish exact timing or causation.", "",
              "## Optional evidence stages", "", "Missing artifacts are pending with null metrics, never zero observations. Existing summaries are reported at their stated scope.", ""]
    components = {**result["event_logs"], **result["ooni"], "cross_transport": result["cross_transport"]}
    for name, component in components.items():
        if not isinstance(component, dict):
            continue
        metrics = "pending" if component["metrics"] is None else json.dumps(component["metrics"], sort_keys=True)
        path = component.get("source_path") or ", ".join(component["source_paths"].values())
        lines.append(f"- **{name}**: {component['status']}; `{metrics}`. Input: `{path}`.")
    lines += ["", "Indexed-log collection is not independent chain completeness. Effective OONI query completion is calculated only after checking frozen retry IDs against the main incomplete set; it is not an independent measurement denominator.", "",
              "OONI retrieval stages are not additive: raw-API gaps and UID-free JSONL format gaps remain historical results when postcan later recovers the same selected records. Postcan identity checks do not establish censorship. Cross-transport agreement covers only the frozen subset; shared upstreams and unissued queries remain explicit.", "",
              "Sourcify match levels remain literal. Local compiler reproduction and exact source-metadata verification are not inferred. Human references and source adjudication remain separate from machine collection.", "",
              "Public-disclosure negative scope: " + d["negative_scope"], "",
              "Reproduce with `make validation-progress` or `python scripts/build_validation_progress.py`; `--tex-out PATH` optionally writes TeX macros without editing the manuscript.", ""]
    return "\n".join(lines)


def tex(result):
    m, e, h, d = (result[key] for key in ("machine_candidates", "endpoint_contrasts", "historical_interfaces", "public_disclosures"))
    def optional(stage, name, key):
        metrics = result[stage][name]["metrics"]
        return metrics.get(key) if metrics else None
    log_matches = result["event_logs"]["candidate_event_matching"]["metrics"]
    intervals = log_matches.get("event_trigger_interval_counts") if log_matches else None
    raw_metrics = result["ooni"]["raw_measurements"]["metrics"]
    raw_counts = raw_metrics.get("url_status_counts") if raw_metrics else None
    transport = result["cross_transport"]["metrics"]
    providers = {p["provider"]: p for p in transport["providers"]} if transport else {}
    values = {"FrameActions": result["source_frame"]["enumerated_action_urls"],
              "FrameETHRows": result["source_frame"]["machine_eth_entry_rows"], "FrameETHPages": result["source_frame"]["action_pages_with_explicit_eth"],
              "CandidateUnits": m["measurement_units"],
              "IssuerUnits": m["issuer_units"], "ActionWindows": m["action_windows"], "EndpointSnapshots": e["valid_endpoint_snapshots"],
              "EndpointRequests": e["http_attempts_captured"], "InterfaceCodeHashes": h["code_address_entries"],
              "InterfaceMatches": h["indexed_runtime_hash_matches"], "DisclosureUnits": d["candidate_target_operator_units"],
              "DisclosureGapUnits": d["outcome_counts"].get("gap", 0),
              "DisclosureScopedNoMentions": d["outcome_counts"].get("no_disclosure_found_under_enumerated_archive", 0),
              "LogAccepted": optional("event_logs", "index_stream_collection", "accepted_unique_logs"),
              "LogPages": optional("event_logs", "index_stream_collection", "pages_captured"),
              "LogMatchedIssuerUnits": optional("event_logs", "candidate_event_matching", "issuer_units_with_indexed_events"),
              "LogMatchedMeasurementUnits": optional("event_logs", "candidate_event_matching", "measurement_units_with_indexed_events"),
              "LogWithinTriggerInterval": intervals.get("within_interval") if intervals else None,
              "LogAfterTriggerInterval": intervals.get("after_interval") if intervals else None,
              "OONIMetadataQueries": optional("ooni", "main_metadata", "query_count"),
              "OONIMetadataRows": optional("ooni", "main_metadata", "metadata_rows"),
              "OONIEffectiveCompleteQueries": optional("ooni", "effective_query_coverage", "effective_complete_queries"),
              "OONIRawURLsAttempted": optional("ooni", "raw_measurements", "raw_urls_attempted"),
              "OONIRawGaps": raw_counts.get("retrieval_gap", 0) if raw_counts is not None else None,
              "OONIRawIdentityValidRows": optional("ooni", "raw_measurements", "identity_valid_metadata_rows"), "HumanReferenceLabels": None}
    for stage, prefix in (("jsonl_fallback", "OONIJSONL"), ("postcan_fallback", "OONIPostcan")):
        for key, suffix in (("objects_attempted", "ObjectsAttempted"), ("objects_stream_scanned", "ObjectsScanned"),
                            ("identity_valid_metadata_rows", "IdentityValidRows"), ("selected_uids", "SelectedUIDs"),
                            ("frozen_total_compressed_content_length", "CompressedBytes")):
            values[prefix + suffix] = optional("ooni", stage, key)
    for key, suffix in (("attempted_queries", "Attempts"), ("selected_action_windows", "ActionWindows"),
                        ("selected_endpoint_snapshots", "EndpointSnapshots"), ("selected_measurement_units", "MeasurementUnits"),
                        ("selected_issuer_units", "IssuerUnits")):
        values["CrossTransport" + suffix] = transport.get(key) if transport else None
    for name, prefix in (("drpc_public", "DRPC"), ("one_rpc_public", "OneRPC")):
        for key, suffix in (("attempted_queries", "Attempts"), ("matched_queries", "Matches"),
                            ("matched_target_state_queries", "StateMatches"), ("unissued_queries", "Unissued")):
            values[prefix + suffix] = providers.get(name, {}).get(key)
    for issuer, pairs in e["pair_counts"].items():
        for pair, label in zip(PAIR_LABELS, ("ZeroZero", "ZeroOne", "OneZero", "OneOne")):
            values[f"{issuer.upper()}{label}"] = pairs[pair]
    lines = ["% Deterministic offline validation-progress macros; pending is not zero.", f"% Input hash: {result['input_hash']}"]
    lines.extend(f"\\newcommand{{\\Progress{key}}}{{{value(val)}}}" for key, val in sorted(values.items()))
    return "\n".join(lines) + "\n"


def write(path, content):
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists() and path.read_text() == content:
        return
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(content)
    temporary.replace(path)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=ROOT)
    parser.add_argument("--out-dir", type=Path)
    parser.add_argument("--tex-out", type=Path)
    args = parser.parse_args()
    result = build(args.repo)
    out = args.out_dir or args.repo / "analysis/validation_progress"
    write(out / "summary.json", serialized(result))
    write(out / "README.md", markdown(result))
    if args.tex_out:
        write(args.tex_out, tex(result))
    print(json.dumps({"status": "cross_checked_offline_progress_written", "input_hash": result["input_hash"], "out_dir": str(out)}))


if __name__ == "__main__":
    main()
