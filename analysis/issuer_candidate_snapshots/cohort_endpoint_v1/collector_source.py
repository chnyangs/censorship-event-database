#!/usr/bin/env python3
"""Resumable, source-defined historical endpoint snapshots; no event-window labels.

Frozen input membership is machine proposed and awaits independent adjudication.
Requests are allowlisted reads; response captures and completed records are immutable.
"""
from __future__ import annotations

import argparse
import fcntl
import json
import re
import time
from collections import defaultdict
from datetime import datetime, timedelta, timezone
from pathlib import Path

from measurement_pilot import (CONTRACTS, ENDPOINTS, PROXY_SLOT, ROOT, digest,
                               http_once, utc_now, validate_result)

VERSION = "1.0.0"
STATUS = "machine_source_defined_partial_endpoint_collection_human_review_pending"
FROZEN = "machine_frozen_not_human_adjudicated"
READS = {"eth_chainId", "eth_getBlockByNumber", "eth_getCode", "eth_getStorageAt", "eth_call"}
LIMITS = {"full_window_logs_complete": False, "full_cohort_execution": False,
          "historical_implementation_bytecode_reproduced": False,
          "independent_chain_reconciliation_complete": False,
          "human_reference_complete": False, "full_window_response_classification": None}


class IntegrityError(ValueError):
    pass


def encoded(value):
    return (json.dumps(value, sort_keys=True, indent=2) + "\n").encode()


def immutable(path, value, raw=False):
    content = value if raw else encoded(value)
    if path.exists():
        if path.read_bytes() != content:
            raise IntegrityError(f"Refusing inconsistent immutable output: {path}")
    else:
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("xb") as handle:
            handle.write(content)


def read_json(path):
    return json.loads(path.read_text())


def jsonl(path):
    return [json.loads(line) for line in path.read_text().splitlines() if line]


def stamp(value):
    parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if parsed.tzinfo != timezone.utc:
        raise ValueError("Only explicit UTC window timestamps are supported")
    return int(parsed.timestamp())


def load_cohort(directory):
    index = read_json(directory / "bundle.sha256.json")
    for name, expected in index["files"].items():
        path = directory / name
        if path.parent != directory or digest(path.read_bytes()) != expected:
            raise ValueError(f"Frozen candidate bundle mismatch: {name}")
    required = {"manifest.json", "issuer_query_units.jsonl", "measurement_units.jsonl", "source_rows.jsonl"}
    if not required <= set(index["files"]):
        raise ValueError("Required cohort inputs are not covered by bundle index")
    manifest = read_json(directory / "manifest.json")
    units, measurements, sources = (jsonl(directory / name) for name in
                                    ("issuer_query_units.jsonl", "measurement_units.jsonl", "source_rows.jsonl"))
    if manifest["status"] != FROZEN or manifest["human_gold"] is not False:
        raise ValueError("Expected explicitly machine-frozen, unadjudicated membership")
    by_id = {u["measurement_unit_id"]: u for u in measurements}
    source_by_id = {s["source_row_id"]: s for s in sources}
    if len(by_id) != len(measurements) or len(source_by_id) != len(sources):
        raise ValueError("Duplicate measurement/source IDs")
    seen_ids, seen_measurements, issuers, groups = set(), set(), defaultdict(set), defaultdict(list)
    for measurement in measurements:
        key = tuple(measurement[k] for k in ("action_url", "normalized_address", "proposed_direction"))
        if key in seen_measurements:
            raise ValueError("Duplicate measurement unit")
        seen_measurements.add(key)
    for unit in units:
        uid, mid = unit["issuer_query_id"], unit["measurement_unit_id"]
        if uid in seen_ids:
            raise ValueError("Duplicate issuer query unit")
        seen_ids.add(uid)
        measurement = by_id[mid]
        if unit["status"] != FROZEN or unit["target_adjudication"] != "pending":
            raise ValueError("Unexpected candidate adjudication/status")
        for key, value in measurement.items():
            if key in unit and unit[key] != value:
                raise ValueError(f"Query/measurement inconsistency: {key}")
        if not re.fullmatch(r"0x[0-9a-f]{40}", unit["normalized_address"]):
            raise ValueError("Malformed normalized target")
        if unit["proposed_direction"] not in {"addition", "removal"}:
            raise ValueError("Updates/unclassified directions are not eligible for this frozen cohort")
        for sid in unit["source_row_ids"]:
            source = source_by_id[sid]
            if source["machine_disposition"] != "machine_candidate":
                raise ValueError("Pending or pilot-excluded source entered candidate collection")
            record = source["source_record"]
            if (record["action_url"], record["normalized_address"], record["proposed_action_type"]) != (
                    unit["action_url"], unit["normalized_address"], unit["proposed_direction"]):
                raise ValueError("Candidate source association mismatch")
            if record["chain_marker"] != "ETH" or record["proposed_list_scope"] != "sdn":
                raise ValueError("Candidate does not have explicit SDN/ETH source markers")
        if not unit["source_row_ids"]:
            raise ValueError("Candidate source rows absent")
        trigger = datetime.fromisoformat(unit["trigger_date"]).replace(tzinfo=timezone.utc)
        for field, days in (("trigger_earliest_utc", 0), ("trigger_latest_exclusive_utc", 1),
                            ("window_start_inclusive_utc", -7), ("window_end_exclusive_utc", 31)):
            if stamp(unit[field]) != int((trigger + timedelta(days=days)).timestamp()):
                raise ValueError("Day-precision trigger/window derivation mismatch")
        if unit["trigger_precision"] != "day":
            raise ValueError("Expected day precision")
        issuer = unit["issuer"]
        name = issuer["symbol"].lower()
        if name not in CONTRACTS or issuer["chain_id"] != 1 or issuer["contract_address"].lower() != CONTRACTS[name]["address"]:
            raise ValueError("Canonical issuer/mainnet identity mismatch")
        if name in issuers[mid]:
            raise ValueError("Duplicate issuer crossing")
        issuers[mid].add(name)
        groups[(unit["action_url"], unit["window_start_inclusive_utc"], unit["window_end_exclusive_utc"])].append(unit)
    if set(issuers) != set(by_id) or any(value != set(CONTRACTS) for value in issuers.values()):
        raise ValueError("Each measurement unit must be crossed with both canonical issuers")
    if len(units) != manifest["counts"]["issuer_query_units"] or len(measurements) != manifest["counts"]["measurement_units"]:
        raise ValueError("Frozen cohort count mismatch")
    if len(groups) != manifest["counts"]["unique_action_urls"]:
        raise ValueError("Action/window membership inconsistent")
    return units, dict(sorted(groups.items(), key=lambda item: (item[0][1], item[0][0])))


class StopCollection(ValueError):
    pass


def validate_existing_captures(out):
    """Validate stored request/response hashes before any resumed network work."""
    for directory in (out / "captures").glob("*"):
        payload = (directory / "request.json").read_bytes()
        if digest(payload).split(":")[1] != directory.name:
            raise ValueError("Existing content-addressed request mismatch")
        for attempt in directory.glob("attempt_*"):
            if attempt.name not in {"attempt_1", "attempt_2"}:
                raise ValueError("Existing capture exceeds attempt allowance")
            started = read_json(attempt / "started.json")
            if started["request_sha256"] != digest(payload):
                raise ValueError("Existing started request hash mismatch")
            if (attempt / "capture.json").exists():
                record = read_json(attempt / "capture.json")
                if record["request_sha256"] != digest(payload) or record["response_body_sha256"] != digest((attempt / "response.body").read_bytes()):
                    raise ValueError("Existing capture hash mismatch")


class Session:
    def __init__(self, out, config, transport=http_once, sleep=time.sleep, clock=time.monotonic):
        self.out, self.config, self.transport = out, config, transport
        self.sleep, self.clock, self.last_started = sleep, clock, None
        self.rows, self.blocks = {}, {}
        self.rate_error = False
        self.consecutive_gaps = 0

    def query(self, method, params):
        if method not in READS:
            raise ValueError("Only endpoint-state read methods are allowlisted")
        payload = encoded({"jsonrpc": "2.0", "id": 1, "method": method, "params": params})
        qid = digest(payload).split(":")[1]
        directory = self.out / "captures" / qid
        if qid in self.rows:
            return self.rows[qid]
        if not directory.exists() and len(list((self.out / "captures").glob("*"))) >= self.config["logical_query_budget"]:
            raise StopCollection("Predeclared logical RPC query budget exhausted")
        immutable(directory / "request.json", payload, raw=True)
        attempts, result = [], None
        for number in (1, 2):
            location = directory / f"attempt_{number}"
            meta_path = location / "capture.json"
            if location.exists():
                if not (location / "started.json").exists():
                    raise ValueError("Inconsistent attempt directory; refusing to overwrite")
                started = read_json(location / "started.json")
                if started["request_sha256"] != digest(payload):
                    raise ValueError("Interrupted/cached request hash mismatch")
                if not meta_path.exists():
                    attempts.append({"number": number, "status": "interrupted_capture_attempt_consumed"})
                    continue
                record = read_json(meta_path)
                body = (location / "response.body").read_bytes()
                if digest(body) != record["response_body_sha256"] or record["request_sha256"] != digest(payload):
                    raise ValueError("Capture hash mismatch; refusing to overwrite")
            else:
                if self.rate_error:
                    raise StopCollection("Material rate error; automatic continuation disabled")
                delay = self.config["minimum_request_interval_seconds"]
                if self.last_started is not None:
                    delay = max(0, delay - (self.clock() - self.last_started))
                self.sleep(delay)
                immutable(location / "started.json", {"at_utc": utc_now(), "request_sha256": digest(payload)})
                self.last_started = self.clock()
                response = self.transport(self.config["endpoint"], payload)
                body = response["body"]
                record = {key: value for key, value in response.items() if key != "body"}
                record.update(retrieved_at_utc=utc_now(), request_sha256=digest(payload),
                              response_body_sha256=digest(body), response_bytes=len(body))
                immutable(location / "response.body", body, raw=True)
                immutable(meta_path, record)
            try:
                data = json.loads(body)
            except (ValueError, UnicodeError):
                data = None
            rate = record["http_status"] == 429 or (isinstance(data, dict) and "error" in data and (
                data["error"].get("code") in (429, -32005) if isinstance(data["error"], dict) else False))
            rate = rate or bool(re.search(r"rate.?limit|too many requests|request limit|compute units per second", str(data.get("error", "") if isinstance(data, dict) else ""), re.I))
            self.rate_error = self.rate_error or rate
            try:
                if record["http_status"] != 200 or record.get("transport_error"):
                    raise ValueError(record.get("transport_error") or f"HTTP {record['http_status']}")
                if not isinstance(data, dict) or data.get("jsonrpc") != "2.0" or data.get("id") != 1 or "error" in data or "result" not in data:
                    raise ValueError("Invalid JSON-RPC envelope or RPC error")
                result = validate_result(method, data["result"])
                attempts.append({"number": number, "status": "valid_rpc_response"})
                break
            except (ValueError, TypeError, KeyError) as exc:
                attempts.append({"number": number, "status": "gap", "error": str(exc), "material_rate_error": bool(rate)})
                if rate:
                    break
        row = {"query_id": qid, "method": method, "params": params, "result": result,
               "status": "valid_rpc_response" if result is not None else "gap", "attempts": attempts}
        immutable(directory / "result.json", row)
        self.rows[qid] = row
        self.consecutive_gaps = 0 if result is not None else self.consecutive_gaps + 1
        if self.rate_error:
            raise StopCollection("Material provider rate error captured; no further requests")
        if self.consecutive_gaps >= 3:
            raise StopCollection("Three consecutive logical RPC gaps; bounded provider failure stop")
        return row

    def block(self, number):
        if number not in self.blocks:
            row = self.query("eth_getBlockByNumber", [hex(number), False])
            if row["status"] != "valid_rpc_response" or int(row["result"]["number"], 16) != number:
                raise ValueError(f"Historical block dependency missing/wrong number: {number}")
            block = row["result"]
            for other_number, other in self.blocks.items():
                if (number - other_number) * (int(block["timestamp"], 16) - int(other["timestamp"], 16)) <= 0:
                    raise ValueError("Non-monotone block timestamps across captured boundary dependencies")
            self.blocks[number] = block
        return self.blocks[number]

    def boundary(self, at, bracket):
        for number in bracket:
            self.block(number)
        lower = [n for n, b in self.blocks.items() if int(b["timestamp"], 16) < at]
        upper = [n for n, b in self.blocks.items() if int(b["timestamp"], 16) >= at]
        if not lower or not upper:
            raise ValueError("Frozen search bracket does not enclose timestamp")
        low, high, steps = max(lower), min(upper), 0
        while high - low > 1:
            tl, th = (int(self.block(n)["timestamp"], 16) for n in (low, high))
            middle = (low + high) // 2 if steps % 4 == 3 else low + ((at - tl) * (high - low) // (th - tl))
            middle = min(high - 1, max(low + 1, middle))
            if int(self.block(middle)["timestamp"], 16) < at:
                low = middle
            else:
                high = middle
            steps += 1
        before, after = self.block(low), self.block(high)
        if not int(before["timestamp"], 16) < at <= int(after["timestamp"], 16):
            raise ValueError("Adjacent boundary check failed")
        return {"requested_timestamp": at, "before_block": low, "at_or_after_block": high,
                "before_hash": before["hash"], "at_or_after_hash": after["hash"],
                "before_timestamp": int(before["timestamp"], 16), "at_or_after_timestamp": int(after["timestamp"], 16)}


def address_word(row):
    if row["status"] == "valid_rpc_response" and row["result"][2:26] == "0" * 24:
        return "0x" + row["result"][26:].lower()
    return None


def prerequisites(session, issuer, number):
    at, contract = hex(number), CONTRACTS[issuer]["address"]
    rows = [session.query("eth_getCode", [contract, at])]
    metadata, error = {}, None
    if issuer == "usdc":
        row = session.query("eth_getStorageAt", [contract, PROXY_SLOT, at])
        rows.append(row)
        address = address_word(row)
        metadata["implementation_address"] = address
        if address and int(address, 16):
            rows.append(session.query("eth_getCode", [address, at]))
        else:
            error = "Missing or malformed nonzero implementation address"
    else:
        deprecated = session.query("eth_call", [{"to": contract, "data": "0x0e136b19"}, at])
        upgraded = session.query("eth_call", [{"to": contract, "data": "0x26976e3f"}, at])
        rows.extend([deprecated, upgraded])
        metadata.update(upgraded_address=address_word(upgraded), deprecated_word=int(deprecated["result"], 16) if deprecated["status"] == "valid_rpc_response" else None)
        if metadata["deprecated_word"] != 0 or metadata["upgraded_address"] is None:
            error = "Historical forwarding unresolved/deprecated"
    return {"pass": error is None and all(r["status"] == "valid_rpc_response" for r in rows),
            "error": error, "metadata": metadata, "query_ids": [row["query_id"] for row in rows],
            "historical_implementation_bytecode_reproduced": False}


def _collect(out, cohort, panel, *, resume=False, transport=http_once, query_budget=1400,
            pacing=0.15, bracket=(14000000, 24500000), sleep=time.sleep, clock=time.monotonic):
    units, groups = load_cohort(cohort)
    if not read_json(panel).get("pilot_contract_prerequisites_met"):
        raise ValueError("Canonical source/interface prerequisites unavailable")
    if not 1 <= query_budget <= 1400 or pacing < 0.15 or bracket[0] >= bracket[1]:
        raise ValueError("Invalid request budget, pacing, or bracket")
    config = {"status": STATUS, "version": VERSION, "endpoint": ENDPOINTS["alchemy_public"],
              "logical_query_budget": query_budget, "max_attempts_per_query": 2,
              "maximum_http_attempts": query_budget * 2, "minimum_request_interval_seconds": pacing,
              "boundary_search_bracket": list(bracket), "planned_measurement_units": len(units) // 2,
              "planned_issuer_query_units": len(units), "planned_action_windows": len(groups),
              "planned_endpoint_snapshots": len(units) * 2,
              "candidate_bundle_index_sha256": digest((cohort / "bundle.sha256.json").read_bytes()),
              "panel_sha256": digest(panel.read_bytes()), "collector_sha256": digest(Path(__file__).read_bytes()),
              "transport_source_sha256": digest(Path(__file__).with_name("measurement_pilot.py").read_bytes()),
              "measurement_scope": "Post-block state at first block timestamp >= inclusive window start and last block timestamp < exclusive end. No intervening action, action time, response absence, causation, or human eligibility inferred.",
              "failure_rule": "Stop on any HTTP/RPC rate-limit signal or three consecutive logical RPC gaps. At most two captured attempts per query; interrupted attempts consume allowance.",
              **LIMITS}
    if out.exists() and not resume:
        raise ValueError("Existing run requires explicit --resume; never overwritten")
    if resume and not out.exists():
        raise ValueError("Cannot resume missing run")
    if resume:
        existing = read_json(out / "collection_manifest.json")
        if existing["configuration"] != config:
            raise ValueError("Immutable resume configuration/code/input hash mismatch")
        validate_existing_captures(out)
    else:
        out.mkdir(parents=True)
        immutable(out / "collection_manifest.json", {"created_before_outcome_queries_at_utc": utc_now(), "configuration": config})
    for name, source in (("collector_source.py", Path(__file__)), ("transport_source.py", Path(__file__).with_name("measurement_pilot.py")),
                         ("candidate_bundle.sha256.json", cohort / "bundle.sha256.json"), ("candidate_manifest.json", cohort / "manifest.json"),
                         ("issuer_query_units.jsonl", cohort / "issuer_query_units.jsonl"), ("panel.json", panel)):
        immutable(out / name, source.read_bytes(), raw=True)
    session = Session(out, config, transport, sleep, clock)
    snapshots, windows, failure = [], [], None
    try:
        if session.query("eth_chainId", [])["status"] != "valid_rpc_response":
            raise StopCollection("Ethereum mainnet identity not established")
        for (action, start, end), members in groups.items():
            wid = digest(encoded([action, start, end])).split(":")[1][:24]
            window = {"window_id": wid, "action_url": action, "start_inclusive_utc": start, "end_exclusive_utc": end}
            try:
                boundaries = {"start": session.boundary(stamp(start), bracket), "end": session.boundary(stamp(end), bracket)}
                immutable(out / "boundaries" / f"{wid}.json", boundaries)
                points = {"window_first_block": boundaries["start"]["at_or_after_block"], "window_last_block": boundaries["end"]["before_block"]}
                for unit in sorted(members, key=lambda u: u["issuer_query_id"]):
                    issuer = unit["issuer"]["symbol"].lower()
                    for label, number in points.items():
                        prereq = prerequisites(session, issuer, number)
                        immutable(out / "prerequisites" / f"{issuer}_{number}.json", prereq)
                        state, qid, word = "not_attempted_historical_prerequisite_gap", None, None
                        if prereq["pass"]:
                            row = session.query("eth_call", [{"to": CONTRACTS[issuer]["address"], "data": CONTRACTS[issuer]["selector"] + unit["normalized_address"][2:].rjust(64, "0")}, hex(number)])
                            state, qid = row["status"], row["query_id"]
                            if state == "valid_rpc_response":
                                word = int(row["result"], 16)
                                if word not in (0, 1):
                                    state, word = "gap_invalid_boolean_return", None
                        block = session.block(number)
                        snapshot = {"issuer_query_id": unit["issuer_query_id"], "measurement_unit_id": unit["measurement_unit_id"],
                                    "window_id": wid, "action_url": action, "issuer": issuer, "target_address": unit["normalized_address"],
                                    "snapshot": label, "block_number": number, "block_hash": block["hash"], "timestamp": int(block["timestamp"], 16),
                                    "state_query_status": state, "state_query_id": qid, "returned_blacklist_word": word,
                                    "rpc_code_and_forwarding_prerequisites_pass": prereq["pass"], **LIMITS}
                        immutable(out / "snapshots" / f"{unit['issuer_query_id']}_{label}.json", snapshot)
                        snapshots.append(snapshot)
                window["status"] = "endpoint_collection_attempted"
            except (StopCollection, IntegrityError):
                raise
            except (ValueError, KeyError) as exc:
                window.update(status="window_dependency_gap", reason=str(exc))
            windows.append(window)
            immutable(out / "windows" / f"{wid}.json", window)
            print(json.dumps({"action_url": action, "finished_windows": len(windows), "planned_windows": len(groups), "recorded_snapshots": len(snapshots), "logical_queries_used": len(session.rows)}), flush=True)
    except (ValueError, KeyError, OSError) as exc:
        failure = str(exc)
    # Derived summaries are versioned by captured evidence; completed captures never change.
    snapshot_files = sorted((out / "snapshots").glob("*.json"))
    snapshots = [read_json(path) for path in snapshot_files]
    valid_by_unit = defaultdict(int)
    for row in snapshots:
        if row["state_query_status"] == "valid_rpc_response":
            valid_by_unit[row["issuer_query_id"]] += 1
    complete_ids = {uid for uid, count in valid_by_unit.items() if count == 2}
    complete_measurements = {mid for mid in {u["measurement_unit_id"] for u in units}
                             if all(u["issuer_query_id"] in complete_ids for u in units if u["measurement_unit_id"] == mid)}
    query_dirs = list((out / "captures").glob("*"))
    started = list((out / "captures").glob("*/attempt_*/started.json"))
    captured = list((out / "captures").glob("*/attempt_*/capture.json"))
    summary = {"status": STATUS, "logical_queries_reserved": len(query_dirs), "http_attempts_started": len(started),
               "http_attempts_captured": len(captured), "recorded_snapshots": len(snapshots),
               "valid_endpoint_snapshots": sum(r["state_query_status"] == "valid_rpc_response" for r in snapshots),
               "issuer_units_with_two_valid_snapshots": len(complete_ids), "measurement_units_with_four_valid_snapshots": len(complete_measurements),
               "planned_issuer_query_units": len(units), "planned_measurement_units": len(units) // 2,
               "issuer_units_incomplete_or_gap": sorted(set(u["issuer_query_id"] for u in units) - complete_ids),
               "measurement_units_incomplete_or_gap": sorted(set(u["measurement_unit_id"] for u in units) - complete_measurements),
               "action_window_records": len(list((out / "windows").glob("*.json"))),
               "endpoint_snapshot_campaign_complete": len(complete_ids) == len(units),
               "failure_or_stop_reason": failure, **LIMITS}
    summary_hash = digest(encoded(summary)).split(":")[1]
    immutable(out / "summaries" / f"{summary_hash}.json", summary)
    if summary["endpoint_snapshot_campaign_complete"]:
        immutable(out / "summary.json", summary)
    return summary


def collect(out, cohort, panel, **kwargs):
    """Only one process can extend a run; the lock does not alter its evidence."""
    out.parent.mkdir(parents=True, exist_ok=True)
    with (out.parent / f".{out.name}.lock").open("a") as lock:
        try:
            fcntl.flock(lock.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError as exc:
            raise ValueError("Another process holds this collection run lock") from exc
        return _collect(out, cohort, panel, **kwargs)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out-dir", type=Path, default=ROOT / "analysis/issuer_candidate_snapshots/cohort_endpoint_v1")
    parser.add_argument("--cohort", type=Path, default=ROOT / "analysis/issuer_candidate_manifest")
    parser.add_argument("--panel", type=Path, default=ROOT / "sources/measurement_panel/verified_panel.json")
    parser.add_argument("--resume", action="store_true")
    args = parser.parse_args()
    print(json.dumps(collect(args.out_dir, args.cohort, args.panel, resume=args.resume), indent=2))


if __name__ == "__main__":
    main()
