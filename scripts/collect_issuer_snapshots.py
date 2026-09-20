#!/usr/bin/env python3
"""Collect bounded historical endpoint snapshots from a frozen candidate batch.

This is partial source-defined collection, not the Tornado feasibility pilot.
It does not collect window logs, classify nonresponses, or validate human labels.
"""
from __future__ import annotations

import argparse
import json
import re
from datetime import datetime
from pathlib import Path

from measurement_pilot import (CONTRACTS, ENDPOINTS, PROXY_SLOT, ROOT, digest,
                               dump, http_once, rpc_query, utc_now)


def timestamp(value):
    return int(datetime.fromisoformat(value.replace("Z", "+00:00")).timestamp())


def load_batch(path: Path):
    index_path = path.parent / "bundle.sha256.json"
    index = json.loads(index_path.read_text())
    for name, expected in index["files"].items():
        candidate = path.parent / name
        if candidate.parent != path.parent or digest(candidate.read_bytes()) != expected:
            raise ValueError(f"Frozen candidate bundle mismatch: {name}")
    if path.name not in index["files"]:
        raise ValueError("Batch is not covered by the frozen bundle")
    batch = json.loads(path.read_text())
    units = batch["query_units"]
    if len(units) != 2 or len({u["normalized_address"] for u in units}) != 1:
        raise ValueError("Bounded collector requires one address crossed with two issuers")
    if {u["issuer"]["symbol"].lower() for u in units} != set(CONTRACTS):
        raise ValueError("Batch must contain canonical USDC and USDT units")
    if len({(u["window_start_inclusive_utc"], u["window_end_exclusive_utc"]) for u in units}) != 1:
        raise ValueError("Batch window mismatch")
    for unit in units:
        issuer = unit["issuer"]
        known = CONTRACTS[issuer["symbol"].lower()]
        if issuer["chain_id"] != 1 or issuer["contract_address"].lower() != known["address"]:
            raise ValueError("Unverified chain/contract identity")
        if not re.fullmatch(r"0x[0-9a-f]{40}", unit["normalized_address"]):
            raise ValueError("Malformed target address")
    return batch, index_path


class Collector:
    def __init__(self, out, endpoint, transport=http_once, query_budget=80):
        self.out, self.endpoint, self.transport = out, endpoint, transport
        self.query_budget, self.rows, self.blocks = query_budget, [], {}

    def query(self, name, method, params):
        if len(self.rows) >= self.query_budget:
            raise ValueError("Predeclared query budget exhausted")
        row = rpc_query(self.endpoint, method, params, self.out / "captures" / name, self.transport)
        row.update(query_id=name)
        self.rows.append(row)
        dump(self.out / "queries.json", self.rows)
        return row

    def block(self, number):
        if number not in self.blocks:
            row = self.query(f"block_{number}", "eth_getBlockByNumber", [hex(number), False])
            if row["status"] != "valid_rpc_response" or int(row["result"]["number"], 16) != number:
                raise ValueError(f"Block dependency unavailable or wrong identity: {number}")
            self.blocks[number] = row["result"]
        return self.blocks[number]

    def boundary(self, at, low, high):
        if not int(self.block(low)["timestamp"], 16) < at <= int(self.block(high)["timestamp"], 16):
            raise ValueError("Predeclared bracket does not enclose window boundary")
        while high - low > 1:
            middle = (low + high) // 2
            stamp = int(self.block(middle)["timestamp"], 16)
            if stamp < at:
                low = middle
            else:
                high = middle
        before, after = self.block(low), self.block(high)
        if not int(before["timestamp"], 16) < at <= int(after["timestamp"], 16):
            raise ValueError("Final adjacent boundary timestamp check failed")
        return {"requested_timestamp": at, "before_block": low, "at_or_after_block": high,
                "before_block_hash": before["hash"], "at_or_after_block_hash": after["hash"],
                "before_timestamp": int(before["timestamp"], 16), "at_or_after_timestamp": int(after["timestamp"], 16)}


def word_address(row):
    if row["status"] != "valid_rpc_response":
        return None
    value = row["result"][2:]
    if value[:24] != "0" * 24:
        return None
    return "0x" + value[24:].lower()


def collect(out: Path, batch_path: Path, panel_path: Path, transport=http_once,
            bracket=(14000000, 15301835), query_budget=80):
    if out.exists():
        raise ValueError("Refusing to overwrite immutable snapshot run")
    batch, index_path = load_batch(batch_path)
    panel = json.loads(panel_path.read_text())
    if not panel.get("pilot_contract_prerequisites_met"):
        raise ValueError("Canonical source/interface prerequisites unavailable")
    if not 1 <= query_budget <= 80 or bracket[0] >= bracket[1]:
        raise ValueError("Invalid bounded collection parameters")
    source = Path(__file__)
    dependency = source.with_name("measurement_pilot.py")
    manifest = {"study_role": "source_defined_partial_endpoint_snapshots_human_review_pending",
                "created_before_outcome_queries_at_utc": utc_now(), "candidate_batch_sha256": digest(batch_path.read_bytes()),
                "candidate_bundle_index_sha256": digest(index_path.read_bytes()), "panel_sidecar_sha256": digest(panel_path.read_bytes()),
                "collector_sha256": digest(source.read_bytes()), "transport_library_sha256": digest(dependency.read_bytes()),
                "selection_rule": batch["selection_rule"], "query_units": batch["query_units"],
                "endpoint": ENDPOINTS["alchemy_public"], "boundary_search_bracket": list(bracket),
                "query_budget": query_budget, "max_attempts_per_query": 2,
                "query_rule": "Verify mainnet and adjacent timestamp boundaries; at first window block and last block before exclusive end, read canonical code, proxy/forwarding metadata, implementation code where applicable, then target blacklist word if prerequisites return valid shapes.",
                "full_window_logs_complete": False, "full_cohort_execution": False,
                "human_reference_complete": False, "independent_chain_reconciliation_complete": False,
                "historical_implementation_bytecode_reproduced": False,
                "endpoint_state_is_not_full_window_response_classification": True}
    out.mkdir(parents=True)
    dump(out / "collection_manifest.json", manifest)
    (out / "collector_source.py").write_bytes(source.read_bytes())
    (out / "transport_source.py").write_bytes(dependency.read_bytes())
    (out / "candidate_batch.json").write_bytes(batch_path.read_bytes())
    collector = Collector(out, manifest["endpoint"], transport, query_budget)
    snapshots, boundaries, failure = [], {}, None
    try:
        chain = collector.query("chain_id", "eth_chainId", [])
        if chain["status"] != "valid_rpc_response":
            raise ValueError("Mainnet identity unavailable; dependent collection skipped")
        unit = batch["query_units"][0]
        for label, field in (("start", "window_start_inclusive_utc"), ("end", "window_end_exclusive_utc")):
            boundaries[label] = collector.boundary(timestamp(unit[field]), *bracket)
            dump(out / "boundaries.json", boundaries)
        points = {"window_first_block": boundaries["start"]["at_or_after_block"],
                  "window_last_block": boundaries["end"]["before_block"]}
        for unit in batch["query_units"]:
            name = unit["issuer"]["symbol"].lower()
            contract = CONTRACTS[name]
            for label, number in points.items():
                prefix, at = f"{name}_{label}", hex(number)
                checks = [collector.query(prefix + "_code", "eth_getCode", [contract["address"], at])]
                metadata = {}
                if name == "usdc":
                    row = collector.query(prefix + "_implementation", "eth_getStorageAt", [contract["address"], PROXY_SLOT, at])
                    checks.append(row)
                    address = word_address(row)
                    metadata["implementation_address"] = address
                    if address and int(address, 16):
                        checks.append(collector.query(prefix + "_implementation_code", "eth_getCode", [address, at]))
                    else:
                        metadata["prerequisite_error"] = "Missing or malformed nonzero proxy implementation address"
                else:
                    deprecated = collector.query(prefix + "_deprecated", "eth_call", [{"to": contract["address"], "data": "0x0e136b19"}, at])
                    upgraded = collector.query(prefix + "_upgraded_address", "eth_call", [{"to": contract["address"], "data": "0x26976e3f"}, at])
                    checks.extend([deprecated, upgraded])
                    metadata["upgraded_address"] = word_address(upgraded)
                    if deprecated["status"] == "valid_rpc_response":
                        metadata["deprecated_word"] = int(deprecated["result"], 16)
                    if metadata.get("deprecated_word") != 0 or metadata["upgraded_address"] is None:
                        metadata["prerequisite_error"] = "Deprecated/unresolved forwarding requires historical interface verification"
                ok = all(row["status"] == "valid_rpc_response" for row in checks) and "prerequisite_error" not in metadata
                if ok:
                    state = collector.query(prefix + "_blacklist_state", "eth_call", [{"to": contract["address"], "data": contract["selector"] + unit["normalized_address"][2:].rjust(64, "0")}, at])
                    if state["status"] == "valid_rpc_response" and int(state["result"], 16) not in (0, 1):
                        state.update(status="gap", validation_error="Invalid boolean return")
                        dump(out / "queries.json", collector.rows)
                else:
                    state = {"status": "not_attempted_historical_code_or_forwarding_prerequisite_gap", "result": None}
                snapshots.append({"issuer_query_id": unit["issuer_query_id"], "issuer": name,
                                  "target_address": unit["normalized_address"], "snapshot": label,
                                  "block_number": number, "block_hash": collector.block(number)["hash"],
                                  "timestamp": int(collector.block(number)["timestamp"], 16),
                                  "state_query_status": state["status"],
                                  "returned_blacklist_word": int(state["result"], 16) if state["status"] == "valid_rpc_response" else None,
                                  "rpc_code_and_forwarding_prerequisites_pass": ok, "metadata": metadata,
                                  "historical_implementation_bytecode_reproduced": False,
                                  "full_window_response_classification": None, "human_reference_complete": False})
                dump(out / "snapshots.json", snapshots)
    except (ValueError, KeyError, OSError) as exc:
        failure = str(exc)
    summary = {"study_role": manifest["study_role"], "completed_at_utc": utc_now(),
               "attempted_queries": len(collector.rows), "http_attempts": sum(len(r["attempts"]) for r in collector.rows),
               "valid_rpc_responses": sum(r["status"] == "valid_rpc_response" for r in collector.rows),
               "planned_endpoint_snapshots": 4, "valid_endpoint_snapshots": sum(r["state_query_status"] == "valid_rpc_response" for r in snapshots),
               "failure_or_stop_reason": failure, "full_window_logs_complete": False,
               "full_cohort_execution": False, "human_reference_complete": False,
               "independent_chain_reconciliation_complete": False, "full_window_response_classification": None}
    dump(out / "summary.json", summary)
    return summary


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out-dir", required=True, type=Path)
    parser.add_argument("--batch", type=Path, default=ROOT / "analysis/issuer_candidate_manifest/first_batch.json")
    parser.add_argument("--panel", type=Path, default=ROOT / "sources/measurement_panel/verified_panel.json")
    args = parser.parse_args()
    print(json.dumps(collect(args.out_dir, args.batch, args.panel), indent=2))


if __name__ == "__main__":
    main()
