#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Freeze source-only issuer measurement candidates before querying outcomes.

Machine proposal, not human-adjudicated eligibility or a finalized gold frame.
Existing bundles are immutable; --verify checks an existing bundle's integrity.
"""
from __future__ import annotations

import argparse
import collections
import csv
from datetime import datetime, timedelta, timezone
import hashlib
import io
import json
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
VERSION = "1.0.0"
PROTOCOL_VERSION = "issuer-source-candidate-window-v1"
CONTRACTS = (
    {"symbol": "USDC", "chain_id": 1, "contract_address": "0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48",
     "official_identity_source": "https://developers.circle.com/stablecoins/usdc-contract-addresses"},
    {"symbol": "USDT", "chain_id": 1, "contract_address": "0xdac17f958d2ee523a2206206994597c13d831ec7",
     "official_identity_source": "https://tether.to/en/supported-protocols/"},
)
FAMILY_NAME = re.compile(r"\bTORNADO\s+CASH\b", re.I)
FAMILY_CONTEXT = re.compile(r"tornado[. ]cash|\b(?:SEMENOV|STORM|PERTSEV)\b", re.I)


def canonical(value):
    return json.dumps(value, sort_keys=True, ensure_ascii=False, separators=(",", ":"))


def sha(raw):
    return "sha256:" + hashlib.sha256(raw).hexdigest()


def identifier(value):
    return hashlib.sha256(canonical(value).encode()).hexdigest()[:24]


def iso(value):
    return value.isoformat().replace("+00:00", "Z")


def window_for_day(day):
    start = datetime.strptime(day, "%Y-%m-%d").replace(tzinfo=timezone.utc)
    return {"trigger_precision": "day", "trigger_earliest_utc": iso(start),
            "trigger_latest_exclusive_utc": iso(start + timedelta(days=1)),
            "window_start_inclusive_utc": iso(start - timedelta(days=7)),
            "window_end_exclusive_utc": iso(start + timedelta(days=31)),
            "horizon_deadline_intervals": [
                {"days": horizon, "earliest_utc": iso(start + timedelta(days=horizon)),
                 "latest_exclusive_utc": iso(start + timedelta(days=horizon + 1))}
                for horizon in (1, 7, 14, 30)]}


def csv_text(rows, fields):
    out = io.StringIO(newline="")
    writer = csv.DictWriter(out, fieldnames=fields, lineterminator="\n")
    writer.writeheader(); writer.writerows(rows)
    return out.getvalue()


def classify_source_rows(rows):
    """Filter on explicit source fields only. Updates/ambiguity stay pending."""
    named_family_addresses = {r.get("normalized_address", "").lower() for r in rows
                              if FAMILY_NAME.search(r.get("target_entry_prefix_candidate", ""))}
    classified = []
    for index, row in enumerate(rows, 1):
        record = {"source_row_number_1based": index,
                  "source_row_hash": sha(canonical(row).encode()),
                  "source_row_id": identifier([index, row]), "source_record": row}
        address = row.get("normalized_address", "").lower()
        if FAMILY_NAME.search(row.get("target_entry_prefix_candidate", "")):
            state, reason = "pilot_family_excluded", "explicit_tornado_cash_target_name"
        elif FAMILY_CONTEXT.search(row.get("entry_text", "")) or address in named_family_addresses:
            state, reason = "pending_family_adjudication", "possible_pilot_family_name_domain_or_shared_address"
        elif row.get("proposed_action_type") not in ("addition", "removal"):
            state, reason = "pending_action_adjudication", "update_or_unclassified_direction_not_resolved"
        elif row.get("proposed_list_scope") != "sdn" or row.get("chain_marker") != "ETH":
            state, reason = "pending_scope_adjudication", "requires_explicit_sdn_and_eth_markers"
        elif not re.fullmatch(r"0x[0-9a-f]{40}", address):
            state, reason = "pending_address_adjudication", "malformed_address"
        elif row.get("release_date") != row.get("date_candidate") or not re.fullmatch(r"202[2-5]-\d{2}-\d{2}", row.get("release_date", "")):
            state, reason = "pending_date_adjudication", "date_disagreement_or_outside_window"
        else:
            try:
                window_for_day(row["release_date"])
                state, reason = "machine_candidate", "explicit_sdn_eth_addition_or_removal_outside_identified_pilot_family"
            except ValueError:
                state, reason = "pending_date_adjudication", "invalid_calendar_date"
        record.update({"machine_disposition": state, "reason": reason})
        classified.append(record)
    return classified


def build_units(classified):
    groups = collections.defaultdict(list)
    for item in classified:
        if item["machine_disposition"] == "machine_candidate":
            row = item["source_record"]
            groups[(row["action_url"], row["normalized_address"].lower(), row["proposed_action_type"])].append(item)
    units = []
    for key, originals in sorted(groups.items()):
        row = originals[0]["source_record"]
        dates = {x["source_record"]["release_date"] for x in originals}
        if len(dates) != 1:
            raise ValueError(f"Conflicting dates within proposed measurement unit: {key}")
        unit = {"measurement_unit_id": identifier(key), "action_url": key[0],
                "action_slug": row["action_slug"], "normalized_address": key[1], "proposed_direction": key[2],
                "trigger_date": row["release_date"], **window_for_day(row["release_date"]),
                "status": "machine_frozen_not_human_adjudicated", "target_adjudication": "pending",
                "eligibility_basis": "source_markers_only_no_balance_or_outcome_selection",
                "balance_policy": "retain_zero_unknown_and_positive_pretrigger_balances",
                "source_row_ids": [x["source_row_id"] for x in originals],
                "source_row_hashes": [x["source_row_hash"] for x in originals],
                "source_body_hashes": sorted({x["source_record"]["body_hash"] for x in originals}),
                "source_paths": sorted({x["source_record"]["source_path"] for x in originals}),
                "target_entry_prefix_candidates": sorted({x["source_record"]["target_entry_prefix_candidate"] for x in originals})}
        units.append(unit)
    return sorted(units, key=lambda u: (u["trigger_date"], u["action_url"], u["normalized_address"], u["proposed_direction"]))


def prepare(frame_dir, protocol, script_path, frozen_at):
    summary_path = frame_dir / "summary.json"
    proposals_path = frame_dir / "ethereum_entry_proposals.csv"
    unknown_path = frame_dir / "unclassified_hex_strings.csv"
    frame = json.loads(summary_path.read_text())
    if frame.get("listing_years_exhausted") != 4 or frame.get("unretrieved_action_pages") != 0:
        raise ValueError("Require four reconciled listing years and all enumerated pages retrieved before freezing")
    rows = list(csv.DictReader(io.StringIO(proposals_path.read_text())))
    # A bundle must refer to the actual bytes behind every source row.
    for source_path, expected in {(r["source_path"], r["body_hash"]) for r in rows}:
        path = pathlib.Path(source_path)
        if not path.is_absolute():
            path = ROOT / path
        if sha(path.read_bytes()) != expected:
            raise ValueError(f"Source hash mismatch: {source_path}")
    classified = classify_source_rows(rows)
    units = build_units(classified)
    queries = []
    for unit in units:
        for issuer in CONTRACTS:
            queries.append({"issuer_query_id": identifier([unit["measurement_unit_id"], issuer["symbol"]]),
                            "measurement_unit_id": unit["measurement_unit_id"], "issuer": issuer,
                            **{k: unit[k] for k in ("action_url", "action_slug", "normalized_address", "proposed_direction",
                                                   "trigger_date", "trigger_precision", "trigger_earliest_utc", "trigger_latest_exclusive_utc",
                                                   "window_start_inclusive_utc", "window_end_exclusive_utc", "horizon_deadline_intervals", "source_row_ids")},
                            "status": "machine_frozen_not_human_adjudicated", "execution_status": "not_executed",
                            "target_adjudication": "pending", "balance_policy": unit["balance_policy"]})
    first_action = (units[0]["trigger_date"], units[0]["action_url"]) if units else None
    first_batch = [q for q in queries if (q["trigger_date"], q["action_url"]) == first_action]
    ledger_fields = ["source_row_id", "source_row_number_1based", "machine_disposition", "reason", "action_url",
                     "normalized_address", "proposed_action_type", "target_entry_prefix_candidate", "source_path", "body_hash"]
    ledger = [{**{k: item[k] for k in ledger_fields if k in item},
               **{k: item["source_record"].get(k, "") for k in ledger_fields if k not in item}}
              for item in classified]
    unknown = list(csv.DictReader(io.StringIO(unknown_path.read_text()))) if unknown_path.exists() else []
    input_hashes = {"source_frame_summary_sha256": sha(summary_path.read_bytes()),
                    "source_frame_input_hash": frame["source_input_hash"],
                    "source_proposals_sha256": sha(proposals_path.read_bytes()),
                    "unclassified_hex_queue_sha256": sha(unknown_path.read_bytes()) if unknown_path.exists() else None,
                    "protocol_sha256": sha(protocol.read_bytes()), "script_sha256": sha(script_path.read_bytes())}
    manifest = {"schema_version": "1.0.0", "script_version": VERSION, "protocol_version": PROTOCOL_VERSION,
                "frozen_at_utc": frozen_at, "status": "machine_frozen_not_human_adjudicated",
                "inputs": input_hashes, "source_frame_directory": str(frame_dir.relative_to(ROOT)) if frame_dir.is_relative_to(ROOT) else str(frame_dir),
                "protocol_path": str(protocol.relative_to(ROOT)) if protocol.is_relative_to(ROOT) else str(protocol),
                "measurement_unit": "action_url x normalized_address x proposed_direction",
                "source_row_retention": "All input rows retained with canonical row hash and 1-based data-row number; aliases only collapsed for measurement, never claimed target-deduplicated.",
                "pilot_rule": "Exclude explicit Tornado Cash target names; reserve related-name/domain/shared-address ambiguities pending family adjudication.",
                "issuers": list(CONTRACTS),
                "issuer_identity_status": "Canonical Ethereum contracts checked against linked official issuer documentation; historical ABI/proxy verification required by collection adapter.",
                "window_rule": "Day trigger [d,d+1); query [d-7,d+31), UTC; no invented exact trigger time.",
                "horizon_rule": "For h in 1,7,14,30 the deadline lies in [d+h,d+h+1). Preserve both endpoints; changes in that interval have timing ambiguity, not an exact h-day classification.",
                "balance_policy": "No holdings or balance-based eligibility filter; zero and unknown balances stay in the measurement denominator.",
                "counts": {"source_rows": len(classified), "source_row_dispositions": dict(sorted(collections.Counter(x['machine_disposition'] for x in classified).items())),
                           "measurement_units": len(units), "issuer_query_units": len(queries),
                           "unique_action_urls": len({u['action_url'] for u in units}),
                           "first_batch_query_units": len(first_batch), "unclassified_hex_rows_pending": len(unknown)},
                "first_batch_selection": "Earliest trigger date then action URL among source-eligible nonpilot candidates; all addresses/directions of that action crossed with both issuers.",
                "human_gold": False, "outcome_queries_executed": 0}
    def jsonl(values):
        return "".join(canonical(row) + "\n" for row in values)
    outputs = {"manifest.json": json.dumps(manifest, indent=2, sort_keys=True) + "\n",
               "source_rows.jsonl": jsonl(classified), "measurement_units.jsonl": jsonl(units),
               "issuer_query_units.jsonl": jsonl(queries),
               "first_batch.json": json.dumps({"selection_rule": manifest["first_batch_selection"],
                                                "status": "machine_frozen_not_human_adjudicated", "query_units": first_batch}, indent=2, sort_keys=True) + "\n",
               "pilot_exclusions.csv": csv_text([r for r in ledger if r["machine_disposition"] == "pilot_family_excluded"], ledger_fields),
               "pending_queue.csv": csv_text([r for r in ledger if r["machine_disposition"].startswith("pending_")], ledger_fields),
               "unclassified_hex_pending.jsonl": jsonl([{**r, "manifest_disposition": "pending_chain_and_action_adjudication"} for r in unknown]),
               "README.md": """# Frozen issuer candidate execution manifest

This immutable bundle freezes machine-proposed source eligibility before outcome
collection. It is NOT a human-adjudicated gold frame. `manifest.json` records
input, protocol and script hashes, UTC freeze time, selection/window rules and
counts. All original source rows remain in `source_rows.jsonl`; measurement-unit
alias collapsing does not adjudicate target identities. Updates, family ambiguity
and unclassified chain strings remain pending rather than being judged ineligible.

`issuer_query_units.jsonl` is the complete candidate queue. `first_batch.json`
selects the earliest nonpilot candidate action independently of outcomes. Both
USDC and USDT are queried for every candidate address, including zero/unknown
balances. No query has been run by this generator. Source eligibility and any
historical ABI/contract-version checks still require validation by the collector.

The trigger is a full UTC day [d,d+1), with query window [d-7,d+31). Horizon
deadlines h=1/7/14/30 are intervals [d+h,d+h+1), not invented exact times.
Do not round timestamps to produce unwarranted causal or latency precision.

Existing frozen directories cannot be regenerated in place. Use
`python scripts/prepare_issuer_candidate_manifest.py --verify` to check file hashes;
use a fresh `--out-dir` for another version. Outcome collectors write separately
and record the hash of `bundle.sha256.json`. Never place outcomes in this bundle.
"""}
    outputs["bundle.sha256.json"] = json.dumps({"status": "machine_frozen_not_human_adjudicated",
                                               "files": {name: sha(text.encode()) for name, text in sorted(outputs.items())}}, indent=2, sort_keys=True) + "\n"
    return outputs


def write_frozen(outputs, out_dir):
    if out_dir.exists():
        raise ValueError(f"Frozen bundle already exists; never overwrite it: {out_dir}")
    out_dir.mkdir(parents=True)
    for name, content in outputs.items():
        (out_dir / name).write_text(content)


def verify_bundle(out_dir):
    index = json.loads((out_dir / "bundle.sha256.json").read_text())
    expected_files = set(index["files"]) | {"bundle.sha256.json"}
    if {p.name for p in out_dir.iterdir()} != expected_files:
        raise ValueError("Frozen bundle file set changed")
    for name, expected in index["files"].items():
        if sha((out_dir / name).read_bytes()) != expected:
            raise ValueError(f"Frozen artifact hash mismatch: {name}")
    return {"status": "verified_immutable_bundle", "bundle_index_hash": sha((out_dir / "bundle.sha256.json").read_bytes()),
            "files_verified": len(index["files"])}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--frame-dir", type=pathlib.Path, default=ROOT / "analysis/validation_frame")
    parser.add_argument("--protocol", type=pathlib.Path, default=ROOT / "docs/two-arm-validation-protocol.md")
    parser.add_argument("--out-dir", type=pathlib.Path, default=ROOT / "analysis/issuer_candidate_manifest")
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if args.verify:
        print(json.dumps(verify_bundle(args.out_dir), indent=2)); return
    if args.out_dir.exists():
        parser.error("Frozen output exists; use --verify or a new --out-dir")
    outputs = prepare(args.frame_dir, args.protocol, pathlib.Path(__file__).resolve(), iso(datetime.now(timezone.utc)))
    write_frozen(outputs, args.out_dir)
    print(outputs["manifest.json"], end="")


if __name__ == "__main__":
    main()
