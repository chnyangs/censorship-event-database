#!/usr/bin/env python3
"""Offline window matching of indexed issuer events; never a causal classifier."""
from __future__ import annotations

import argparse
from collections import Counter
from datetime import datetime
import json
from pathlib import Path

from measurement_pilot import ROOT, digest, dump, utc_now


def identity(event):
    return (event["transaction_hash"], event["log_index"], event["block_hash"])


def interval_timing(event_timestamp, earliest, latest_exclusive):
    stamps = [datetime.fromisoformat(value.replace("Z", "+00:00")) for value in (event_timestamp, earliest, latest_exclusive)]
    if any(value.tzinfo is None for value in stamps) or stamps[1] >= stamps[2]:
        raise ValueError("Explicit valid trigger interval and timezone-aware event timestamp required")
    event, lower, upper = stamps
    position = "before_interval" if event < lower else "after_interval" if event >= upper else "within_interval"
    return {"trigger_interval_position": position,
            "ordering_within_interval": "indeterminate" if position == "within_interval" else "outside_interval",
            "delay_lower_bound_seconds": int((event - upper).total_seconds()),
            "delay_upper_bound_seconds": int((event - lower).total_seconds()),
            "delay_lower_bound_exclusive": True, "delay_upper_bound_inclusive": True,
            "event_time_source": "index_reported_block_timestamp", "exact_trigger_latency_established": False}


def match_units(units, snapshots, events, issuer_coverage):
    unique, duplicates = {}, 0
    for event in events:
        key = identity(event)
        if key in unique:
            if unique[key] != event:
                raise ValueError("Conflicting duplicate indexed-event identity")
            duplicates += 1
        unique[key] = event
    by_snapshot = {(row["issuer_query_id"], row["snapshot"]): row for row in snapshots}
    if len(by_snapshot) != len(snapshots):
        raise ValueError("Duplicate endpoint snapshot key")
    if len({unit["issuer_query_id"] for unit in units}) != len(units):
        raise ValueError("Duplicate issuer query unit")
    output, matching_keys = [], set()
    for unit in sorted(units, key=lambda u: u["issuer_query_id"]):
        uid, issuer = unit["issuer_query_id"], unit["issuer"]["symbol"].lower()
        first = by_snapshot.get((uid, "window_first_block"))
        last = by_snapshot.get((uid, "window_last_block"))
        sequence = []
        if first and last:
            if first["block_number"] > last["block_number"]:
                raise ValueError("Inverted endpoint block bounds")
            if first["target_address"] != unit["normalized_address"] or last["target_address"] != unit["normalized_address"] or first["issuer"] != issuer or last["issuer"] != issuer:
                raise ValueError("Snapshot/candidate target mismatch")
            sequence = sorted([{**event, **interval_timing(event["block_timestamp"], unit["trigger_earliest_utc"], unit["trigger_latest_exclusive_utc"])} for event in unique.values()
                               if event["issuer"] == issuer and event["affected_address"] == unit["normalized_address"]
                               and first["block_number"] <= event["block_number"] <= last["block_number"]],
                              key=lambda event: (event["block_number"], event["log_index"]))
        matching_keys.update(identity(event) for event in sequence)
        counts = Counter(event["direction"] for event in sequence)
        if set(counts) - {"add", "remove"}:
            raise ValueError("Unknown event direction")
        status, replayed = "not_assessed_missing_or_invalid_endpoint", None
        valid_endpoints = first and last and all(row.get("state_query_status") == "valid_rpc_response"
                           and type(row.get("returned_blacklist_word")) is int and row["returned_blacklist_word"] in (0, 1)
                           and row.get("rpc_code_and_forwarding_prerequisites_pass") is True for row in (first, last))
        if valid_endpoints:
            if not issuer_coverage.get(issuer, False):
                status = "not_assessed_incomplete_index_range"
            else:
                replayed = first["returned_blacklist_word"]
                # Endpoint words are post-block values. Events IN the first
                # endpoint block are matched but already reflected in that word.
                for event in sequence:
                    if event["block_number"] > first["block_number"]:
                        replayed = 1 if event["direction"] == "add" else 0
                status = "consistent_given_indexed_sequence" if replayed == last["returned_blacklist_word"] else "inconsistent_given_indexed_sequence"
        output.append({"issuer_query_id": uid, "measurement_unit_id": unit["measurement_unit_id"],
                       "action_url": unit["action_url"], "issuer": issuer, "normalized_address": unit["normalized_address"],
                       "proposed_source_direction": unit["proposed_direction"],
                       "trigger_earliest_utc": unit["trigger_earliest_utc"],
                       "trigger_latest_exclusive_utc": unit["trigger_latest_exclusive_utc"],
                       "window_start_inclusive_utc": unit["window_start_inclusive_utc"],
                       "window_end_exclusive_utc": unit["window_end_exclusive_utc"],
                       "first_block_inclusive": first["block_number"] if first else None,
                       "last_block_inclusive": last["block_number"] if last else None,
                       "matching_indexed_events": sequence, "matching_indexed_event_count": len(sequence),
                       "add_count": counts["add"], "remove_count": counts["remove"],
                       "events_at_first_post_block_snapshot": sum(event["block_number"] == first["block_number"] for event in sequence) if first else 0,
                       "first_endpoint_word": first.get("returned_blacklist_word") if first else None,
                       "last_endpoint_word": last.get("returned_blacklist_word") if last else None,
                       "replayed_last_word_from_strictly_after_first_block": replayed,
                       "endpoint_word_consistency_given_indexed_sequence": status,
                       "issuer_index_range_coverage_complete": issuer_coverage.get(issuer, False),
                       "zero_matches_is_not_no_action": True, "causal_attribution_performed": False,
                       "independent_chain_completeness_verified": False, "human_reference_complete": False,
                       "response_classification": None})
    timing = Counter(event["trigger_interval_position"] for row in output for event in row["matching_indexed_events"])
    summaries = {"issuer_units": len(output), "measurement_units": len({row["measurement_unit_id"] for row in output}),
                 "issuer_units_with_indexed_events": sum(bool(row["matching_indexed_event_count"]) for row in output),
                 "measurement_units_with_indexed_events": len({row["measurement_unit_id"] for row in output if row["matching_indexed_event_count"]}),
                 "distinct_addresses_with_indexed_events": len({row["normalized_address"] for row in output if row["matching_indexed_event_count"]}),
                 "matching_event_associations": sum(row["matching_indexed_event_count"] for row in output),
                 "unique_matching_event_identities": len(matching_keys),
                 "per_issuer_units_with_indexed_events": dict(Counter(row["issuer"] for row in output if row["matching_indexed_event_count"])),
                 "endpoint_consistency_counts": dict(Counter(row["endpoint_word_consistency_given_indexed_sequence"] for row in output)),
                 "duplicate_input_event_rows_removed": duplicates,
                 "event_trigger_interval_counts": {position: timing[position] for position in ("before_interval", "within_interval", "after_interval")},
                 "within_trigger_interval_order_indeterminate": True,
                 "exact_trigger_latency_established": False,
                 "indexed_stream_coverage_complete": all(issuer_coverage.get(name, False) for name in ("usdc", "usdt")),
                 "zero_is_not_no_action": True, "causal_attribution_performed": False,
                 "independent_chain_completeness_verified": False, "human_reference_complete": False,
                 "full_window_response_classification": None}
    return output, summaries


def build(out, cohort, logs):
    if out.exists():
        raise ValueError("Refusing to overwrite frozen matching run")
    units_path, events_path = cohort / "issuer_query_units.jsonl", logs / "accepted_logs.json"
    units = [json.loads(line) for line in units_path.read_text().splitlines() if line]
    snapshot_paths = sorted((cohort / "snapshots").glob("*.json"))
    snapshots = [json.loads(path.read_text()) for path in snapshot_paths]
    events = json.loads(events_path.read_text())
    summary = json.loads((logs / "summary.json").read_text())
    cohort_summary = json.loads((cohort / "summary.json").read_text())
    log_plan = json.loads((logs / "plan.json").read_text())
    if len(units) != cohort_summary["planned_issuer_query_units"] or len(snapshots) != cohort_summary["recorded_snapshots"]:
        raise ValueError("Frozen cohort unit/snapshot count mismatch")
    if any(not log_plan["first_block_inclusive"] <= row["block_number"] <= log_plan["last_block_inclusive"] for row in snapshots):
        raise ValueError("Index collection span does not cover cohort endpoint bounds")
    coverage = {name: all(any(row["stream"] == f"{name}_{direction}" and row["index_range_complete"] for row in summary["streams"])
                         for direction in ("add", "remove")) for name in ("usdc", "usdt")}
    out.mkdir(parents=True)
    dump(out / "matching_manifest.json", {"created_before_matching_at_utc": utc_now(),
         "cohort_units_sha256": digest(units_path.read_bytes()), "indexed_events_sha256": digest(events_path.read_bytes()),
         "indexed_summary_sha256": digest((logs / "summary.json").read_bytes()),
         "collector_plan_sha256": digest((logs / "plan.json").read_bytes()),
         "snapshot_file_hashes": {path.name: digest(path.read_bytes()) for path in snapshot_paths},
         "matcher_sha256": digest(Path(__file__).read_bytes()),
         "rule": "All frozen issuer units, matching issuer/address/inclusive endpoint blocks; order by(block,log_index). Replay only events strictly after first post-block state. Use frozen trigger earliest/latest fields for timing: event minus [earliest,latest) gives(exclusive lower,inclusive upper] delay bounds; within-interval order indeterminate. No exact action-URL-date latency. No matches remains an indexed-observation count, never a no-action/response/causal label."})
    (out / "matcher_source.py").write_bytes(Path(__file__).read_bytes())
    records, report = match_units(units, snapshots, events, coverage)
    (out / "window_matches.jsonl").write_text("".join(json.dumps(row, sort_keys=True) + "\n" for row in records))
    dump(out / "summary.json", report)
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out-dir", required=True, type=Path)
    parser.add_argument("--cohort", type=Path, default=ROOT / "analysis/issuer_candidate_snapshots/cohort_endpoint_v1")
    parser.add_argument("--logs", type=Path, default=ROOT / "analysis/blockscout_issuer_logs/full_streams_v2")
    args = parser.parse_args()
    print(json.dumps(build(args.out_dir, args.cohort, args.logs), indent=2))


if __name__ == "__main__":
    main()
