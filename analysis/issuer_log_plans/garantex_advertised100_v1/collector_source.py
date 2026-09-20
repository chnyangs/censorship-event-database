#!/usr/bin/env python3
"""Plan or resume bounded issuer log collection from a frozen first batch.

Raw captures and the run manifest are immutable; progress reports are derived.
All ranges must succeed before requested-range coverage is complete. That flag
does not prove an endpoint never silently truncated results or validate labels.
"""
from __future__ import annotations

import argparse
import json
import re
import time
from pathlib import Path

from collect_issuer_snapshots import load_batch, timestamp
from measurement_pilot import (CONTRACTS, ENDPOINTS, READ_METHODS, ROOT, digest, dump, http_once,
                               save_attempt, utc_now, validate_result)

DEFAULT_SNAPSHOTS = ROOT / "analysis/issuer_candidate_snapshots/garantex_2022_first_batch_v1"
HEX_WORD = re.compile(r"0x[0-9a-fA-F]{64}")
QUANTITY = re.compile(r"0x(?:0|[1-9a-fA-F][0-9a-fA-F]*)")


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":")).encode()


def immutable_json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("x") as handle:
        handle.write(json.dumps(value, indent=2, sort_keys=True) + "\n")


def partition(first, last, size):
    if first > last or first < 0 or not 1 <= size <= 10000:
        raise ValueError("Invalid finite block partition")
    return [(start, min(start + size - 1, last)) for start in range(first, last + 1, size)]


def chunks_for(units, first, last, size):
    chunks = []
    for unit in units:
        symbol = unit["issuer"]["symbol"].lower()
        contract = CONTRACTS[symbol]
        for start, end in partition(first, last, size):
            topics = [contract["topics"]]
            if contract["indexed_address"]:
                topics.append("0x" + unit["normalized_address"][2:].rjust(64, "0"))
            chunks.append({"id": f"{symbol}_{start}_{end}", "issuer_query_id": unit["issuer_query_id"],
                           "issuer": symbol, "target": unit["normalized_address"], "first": start, "last": end,
                           "method": "eth_getLogs", "params": [{"address": contract["address"], "fromBlock": hex(start), "toBlock": hex(end), "topics": topics}]})
    return chunks


def plan(out, batch_path, snapshot_dir, chunk_blocks=10, http_budget=200):
    if out.exists():
        raise ValueError("Refusing to replace frozen collection plan")
    if not 1 <= http_budget <= 1000000:
        raise ValueError("An explicit finite HTTP attempt budget is required")
    # Currently only the actually exercised public transport is supported.
    # A new transport requires a reviewed, evidence-backed profile in code.
    if chunk_blocks not in (10, 100):
        raise ValueError("Alchemy public profile permits tested10 or advertised100 block planning only")
    batch, bundle_path = load_batch(batch_path)
    prior = json.loads((snapshot_dir / "collection_manifest.json").read_text())
    if prior["candidate_batch_sha256"] != digest(batch_path.read_bytes()) or prior["candidate_bundle_index_sha256"] != digest(bundle_path.read_bytes()):
        raise ValueError("Snapshot boundaries are bound to another candidate batch")
    for field, filename in (("collector_sha256", "collector_source.py"),
                            ("transport_library_sha256", "transport_source.py"),
                            ("candidate_batch_sha256", "candidate_batch.json")):
        if prior[field] != digest((snapshot_dir / filename).read_bytes()):
            raise ValueError("Snapshot source/input integrity mismatch")
    boundaries = json.loads((snapshot_dir / "boundaries.json").read_text())
    expected_headers = []
    unit = batch["query_units"][0]
    for label, field in (("start", "window_start_inclusive_utc"), ("end", "window_end_exclusive_utc")):
        value = boundaries[label]
        at = timestamp(unit[field])
        if value["requested_timestamp"] != at or value["before_block"] + 1 != value["at_or_after_block"] or not value["before_timestamp"] < at <= value["at_or_after_timestamp"]:
            raise ValueError("Invalid adjacent timestamp boundary")
        for position in ("before", "at_or_after"):
            expected_headers.append({"number": value[position + "_block"], "hash": value[position + "_block_hash"], "timestamp": value[position + "_timestamp"]})
    first, last = boundaries["start"]["at_or_after_block"], boundaries["end"]["before_block"]
    chunk_count = len(partition(first, last, chunk_blocks)) * len(batch["query_units"])
    logical = 1 + len(expected_headers) + chunk_count
    source = Path(__file__)
    transport_source = source.with_name("measurement_pilot.py")
    manifest = {"schema_version": 1, "study_role": "source_defined_window_log_collection_human_reference_pending",
                "created_before_queries_at_utc": utc_now(), "candidate_batch_sha256": digest(batch_path.read_bytes()),
                "candidate_bundle_sha256": digest(bundle_path.read_bytes()),
                "snapshot_boundaries_sha256": digest((snapshot_dir / "boundaries.json").read_bytes()),
                "collector_sha256": digest(source.read_bytes()), "transport_source_sha256": digest(transport_source.read_bytes()),
                "endpoint": ENDPOINTS["alchemy_public"], "chunk_blocks": chunk_blocks,
                "range_evidence": "successfully_tested" if chunk_blocks == 10 else "API_error_advertised_limit_not_yet_successfully_tested",
                "first_block": first, "last_block": last, "block_count": last - first + 1,
                "expected_headers": expected_headers, "query_units": batch["query_units"],
                "range_partition_rule": "Inclusive contiguous fixed-size chunks, shortening only the final chunk; deterministic queries derived by frozen collector source",
                "planned_chunks": chunk_count,
                "max_attempts_per_query": 2, "http_attempt_budget": http_budget,
                "planned_logical_queries": logical, "worst_case_http_attempts": logical * 2,
                "launch_fits_budget": logical * 2 <= http_budget,
                "max_logs_per_response_guard": 10000, "minimum_request_interval_seconds": 1.0,
                "completeness_definition": "Every predeclared contiguous block range has a valid captured JSON-RPC response, all logs pass range/identity/ABI checks, and no conflicting duplicates or cap-sized responses occur. Silent server omissions remain unverified without independent reconciliation.",
                "human_reference_complete": False, "historical_implementation_bytecode_reproduced": False,
                "independent_chain_reconciliation_complete": False, "full_window_response_classification": None}
    out.mkdir(parents=True)
    immutable_json(out / "plan.json", manifest)
    (out / "collector_source.py").write_bytes(source.read_bytes())
    (out / "transport_source.py").write_bytes(transport_source.read_bytes())
    (out / "candidate_batch.json").write_bytes(batch_path.read_bytes())
    (out / "source_boundaries.json").write_bytes((snapshot_dir / "boundaries.json").read_bytes())
    immutable_json(out / "plan.sha256.json", {"plan_sha256": digest((out / "plan.json").read_bytes())})
    return {key: manifest[key] for key in ("planned_logical_queries", "worst_case_http_attempts", "http_attempt_budget", "launch_fits_budget", "block_count", "chunk_blocks")}


def parse_attempt(directory, payload, method):
    meta = json.loads((directory / "capture.json").read_text())
    body = (directory / "response.body").read_bytes()
    if meta["response_body_sha256"] != digest(body) or meta["request_sha256"] != digest(payload) or (directory / "request.json").read_bytes() != payload:
        raise ValueError("Immutable request/response capture integrity mismatch")
    if meta["http_status"] != 200 or meta["transport_error"]:
        return None, meta["transport_error"] or f"HTTP {meta['http_status']}"
    try:
        value = json.loads(body)
        if not isinstance(value, dict) or value.get("jsonrpc") != "2.0" or value.get("id") != 1 or "error" in value or "result" not in value:
            raise ValueError(f"RPC error or malformed response: {value}")
        return validate_result(method, value["result"]), None
    except (ValueError, TypeError, KeyError) as exc:
        return None, str(exc)


def durable_query(out, endpoint, name, method, params, transport, delay):
    """Resume from exact captured attempts; a query gets two attempts total."""
    if method not in READ_METHODS:
        raise ValueError("Only allowlisted read methods may run")
    payload = json.dumps({"jsonrpc": "2.0", "id": 1, "method": method, "params": params}, sort_keys=True).encode()
    errors = []
    for number in (1, 2):
        directory = out / "captures" / name / f"attempt_{number}"
        if not directory.exists():
            if delay:
                time.sleep(delay)
            save_attempt(directory, transport(endpoint, payload), payload, endpoint)
        value, error = parse_attempt(directory, payload, method)
        if error is None:
            return value, None
        errors.append(error)
        if "429" in error or "rate limit" in error.lower() or "too many requests" in error.lower():
            return None, "Rate limit stop; no retry or subsequent range: " + error
    return None, " | ".join(errors)


def decode_logs(logs, chunk, cap):
    if len(logs) >= cap:
        raise ValueError("Cap-sized response cannot establish complete range; use a newly declared smaller partition")
    contract = CONTRACTS[chunk["issuer"]]
    selected = []
    for log in logs:
        if not isinstance(log, dict) or not isinstance(log.get("address"), str) or log["address"].lower() != contract["address"]:
            raise ValueError("Unexpected log contract")
        topics = log.get("topics")
        count = 2 if contract["indexed_address"] else 1
        if not isinstance(topics, list) or len(topics) != count or any(not isinstance(v, str) or not HEX_WORD.fullmatch(v) for v in topics) or topics[0].lower() not in contract["topics"]:
            raise ValueError("Malformed or unexpected event topics")
        data = log.get("data")
        if contract["indexed_address"]:
            if data != "0x":
                raise ValueError("Indexed-only event has unexpected data")
            word = topics[1][2:]
        else:
            if not isinstance(data, str) or not HEX_WORD.fullmatch(data):
                raise ValueError("Malformed non-indexed address word")
            word = data[2:]
        if word[:24] != "0" * 24:
            raise ValueError("Invalid ABI address padding")
        for field in ("blockHash", "transactionHash"):
            if not isinstance(log.get(field), str) or not HEX_WORD.fullmatch(log[field]):
                raise ValueError("Missing or malformed log hash")
        for field in ("blockNumber", "logIndex", "transactionIndex"):
            if not isinstance(log.get(field), str) or not QUANTITY.fullmatch(log[field]):
                raise ValueError("Malformed log index/block number")
        number = int(log["blockNumber"], 16)
        if not chunk["first"] <= number <= chunk["last"] or log.get("removed") is not False:
            raise ValueError("Removed log or block outside requested range")
        matches = "0x" + word[24:].lower() == chunk["target"]
        if contract["indexed_address"] and not matches:
            raise ValueError("Server ignored the indexed target filter")
        selected.append({"key": [log["transactionHash"].lower(), int(log["logIndex"], 16), log["blockHash"].lower()],
                         "target_match": matches, "log": log})
    return selected


def verified_plan(out):
    manifest = json.loads((out / "plan.json").read_text())
    if json.loads((out / "plan.sha256.json").read_text())["plan_sha256"] != digest((out / "plan.json").read_bytes()):
        raise ValueError("Frozen plan integrity mismatch")
    for field, filename in (("collector_sha256", "collector_source.py"), ("transport_source_sha256", "transport_source.py"),
                            ("candidate_batch_sha256", "candidate_batch.json"), ("snapshot_boundaries_sha256", "source_boundaries.json")):
        if manifest[field] != digest((out / filename).read_bytes()):
            raise ValueError("Frozen input or code snapshot integrity mismatch")
    if manifest["collector_sha256"] != digest(Path(__file__).read_bytes()) or manifest["transport_source_sha256"] != digest(Path(__file__).with_name("measurement_pilot.py").read_bytes()):
        raise ValueError("Running code differs from frozen plan; create a new plan")
    if manifest["endpoint"] != ENDPOINTS["alchemy_public"]:
        raise ValueError("Endpoint not in reviewed no-key transport profile")
    frozen_batch = json.loads((out / "candidate_batch.json").read_text())
    if frozen_batch["query_units"] != manifest["query_units"]:
        raise ValueError("Planned units differ from frozen source candidates")
    manifest["chunks"] = chunks_for(manifest["query_units"], manifest["first_block"], manifest["last_block"], manifest["chunk_blocks"])
    if len(manifest["chunks"]) != manifest["planned_chunks"]:
        raise ValueError("Partition count differs from frozen plan")
    expected = partition(manifest["first_block"], manifest["last_block"], manifest["chunk_blocks"])
    groups = {}
    for chunk in manifest["chunks"]:
        groups.setdefault(chunk["issuer_query_id"], []).append((chunk["first"], chunk["last"]))
        expected_topics = [CONTRACTS[chunk["issuer"]]["topics"]]
        if CONTRACTS[chunk["issuer"]]["indexed_address"]:
            expected_topics.append("0x" + chunk["target"][2:].rjust(64, "0"))
        expected_params = [{"address": CONTRACTS[chunk["issuer"]]["address"], "fromBlock": hex(chunk["first"]), "toBlock": hex(chunk["last"]), "topics": expected_topics}]
        if chunk["method"] != "eth_getLogs" or chunk["params"] != expected_params:
            raise ValueError("Frozen query no longer matches its declared range/filter")
    if any(values != expected for values in groups.values()) or len(groups) != 2 or len({c["id"] for c in manifest["chunks"]}) != len(manifest["chunks"]):
        raise ValueError("Chunk coverage has gaps, overlaps, duplicates or missing units")
    return manifest


def execute(out, transport=http_once):
    manifest = verified_plan(out)
    required = 2 * (1 + len(manifest["expected_headers"]) + len(manifest["chunks"]))
    if required > manifest["http_attempt_budget"]:
        refusal = {"status": "not_launched_budget_exceeded", "worst_case_http_attempts": required,
                   "http_attempt_budget": manifest["http_attempt_budget"], "network_requests_sent": 0,
                   "human_review_is_not_the_blocker": True, "at_utc": utc_now()}
        if not (out / "launch_refusal.json").exists():
            immutable_json(out / "launch_refusal.json", refusal)
        return refusal
    delay = manifest["minimum_request_interval_seconds"] if transport is http_once else 0
    results, unique, tx_positions, block_hashes = [], {}, {}, {}
    failure = None
    try:
        result, error = durable_query(out, manifest["endpoint"], "chain_id", "eth_chainId", [], transport, delay)
        if error:
            raise ValueError("Mainnet identity gap: " + error)
        for header in manifest["expected_headers"]:
            result, error = durable_query(out, manifest["endpoint"], f"header_{header['number']}", "eth_getBlockByNumber", [hex(header["number"]), False], transport, delay)
            if error or int(result["number"], 16) != header["number"] or result["hash"].lower() != header["hash"].lower() or int(result["timestamp"], 16) != header["timestamp"]:
                raise ValueError("Window boundary identity/time reconciliation failed")
        for chunk in manifest["chunks"]:
            value, error = durable_query(out, manifest["endpoint"], chunk["id"], "eth_getLogs", chunk["params"], transport, delay)
            if error:
                results.append({"id": chunk["id"], "status": "gap", "error": error})
                raise ValueError("Range failed after bounded attempts: " + chunk["id"])
            try:
                decoded = decode_logs(value, chunk, manifest["max_logs_per_response_guard"])
                local_unique, local_tx_positions, local_block_hashes = {}, {}, {}
                for row in decoded:
                    key = tuple(row["key"])
                    log = row["log"]
                    previous = local_unique.get(key, unique.get(key))
                    if previous is not None and canonical(previous["log"]) != canonical(log):
                        raise ValueError("Conflicting duplicate event identity")
                    old_hash = local_tx_positions.get(key[:2], tx_positions.get(key[:2]))
                    if old_hash is not None and old_hash != key[2]:
                        raise ValueError("Conflicting block hash for transaction/log index")
                    block = int(log["blockNumber"], 16)
                    old_block_hash = local_block_hashes.get(block, block_hashes.get(block))
                    if old_block_hash is not None and old_block_hash != key[2]:
                        raise ValueError("Conflicting hashes for one block number")
                    local_unique[key], local_tx_positions[key[:2]], local_block_hashes[block] = row, key[2], key[2]
                # A malformed range contributes no logs to the accepted output.
                unique.update(local_unique)
                tx_positions.update(local_tx_positions)
                block_hashes.update(local_block_hashes)
                results.append({"id": chunk["id"], "status": "valid_range_response", "raw_log_count": len(value), "target_log_count": sum(r["target_match"] for r in decoded)})
            except ValueError as exc:
                results.append({"id": chunk["id"], "status": "gap", "error": str(exc)})
                raise
            dump(out / "progress.json", results)
    except (ValueError, KeyError, OSError) as exc:
        failure = str(exc)
    dump(out / "progress.json", results)
    ordered = sorted(unique.values(), key=lambda r: (int(r["log"]["blockNumber"], 16), int(r["log"]["logIndex"], 16)))
    dump(out / "deduplicated_logs.json", ordered)
    complete = len(results) == len(manifest["chunks"]) and all(row["status"] == "valid_range_response" for row in results)
    summary = {"status": "requested_ranges_complete" if complete else "incomplete",
               "completed_ranges": sum(row["status"] == "valid_range_response" for row in results),
               "planned_ranges": len(manifest["chunks"]), "requested_range_coverage_complete": complete,
               "unique_logs": len(unique), "unique_target_logs": sum(row["target_match"] for row in unique.values()),
               "failure_or_stop_reason": failure, "completed_at_utc": utc_now(),
               "http_attempts_on_disk": len(list((out / "captures").rglob("capture.json"))),
               "independent_log_completeness_verified": False, "human_reference_complete": False,
               "historical_implementation_bytecode_reproduced": False, "full_window_response_classification": None}
    dump(out / "summary.json", summary)
    return summary


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    prepare = sub.add_parser("plan", help="Write an immutable dry-run plan; no network access")
    prepare.add_argument("--out-dir", required=True, type=Path)
    prepare.add_argument("--batch", type=Path, default=ROOT / "analysis/issuer_candidate_manifest/first_batch.json")
    prepare.add_argument("--snapshot-dir", type=Path, default=DEFAULT_SNAPSHOTS)
    prepare.add_argument("--chunk-blocks", type=int, default=10)
    prepare.add_argument("--http-budget", type=int, default=200)
    launch = sub.add_parser("collect", help="Resume the frozen plan within its predeclared HTTP budget")
    launch.add_argument("--plan-dir", required=True, type=Path)
    args = parser.parse_args()
    result = plan(args.out_dir, args.batch, args.snapshot_dir, args.chunk_blocks, args.http_budget) if args.command == "plan" else execute(args.plan_dir)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
