#!/usr/bin/env python3
"""Freeze observed historical code/address inventory and a six-GET metadata plan.

Default mode is offline preparation. --fetch executes only the frozen read-only
Sourcify lookup plan. It performs no compilation, source expansion or RPC calls.
"""
from __future__ import annotations

import argparse
import json
import time
import urllib.error
import urllib.request
from pathlib import Path

from collect_issuer_cohort_snapshots import encoded, immutable, read_json, validate_existing_captures
from measurement_pilot import CONTRACTS, ROOT, digest, http_once, utc_now

VERSION = "1.0.0"


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


def get_once(url):
    """One HTTP attempt, including redirects as captured gaps, not hidden hops."""
    request = urllib.request.Request(url, headers={"User-Agent": "CensorshipCorpusHistoricalInterface/1.0 (read-only academic measurement)", "Accept": "application/json"})
    try:
        with urllib.request.build_opener(NoRedirect).open(request, timeout=15) as response:
            return {"http_status": response.status, "headers": dict(response.headers.items()), "final_url": response.url,
                    "body": response.read(), "transport_error": None}
    except urllib.error.HTTPError as exc:
        return {"http_status": exc.code, "headers": dict(exc.headers.items()), "final_url": exc.url,
                "body": exc.read(), "transport_error": str(exc)}
    except (urllib.error.URLError, TimeoutError, OSError) as exc:
        return {"http_status": None, "headers": {}, "final_url": url, "body": b"", "transport_error": str(exc)}


def push4_offsets(code, selector):
    raw, expected, offsets, i = bytes.fromhex(code[2:]), bytes.fromhex(selector[2:]), [], 0
    while i < len(raw):
        opcode = raw[i]
        if opcode == 0x63 and raw[i + 1:i + 5] == expected:
            offsets.append(i)
        i += 1 + (opcode - 0x5f if 0x60 <= opcode <= 0x7f else 0)
    return offsets


def inventory(run):
    validate_existing_captures(run)
    if not read_json(run / "summary.json")["endpoint_snapshot_campaign_complete"]:
        raise ValueError("Inventory requires completed endpoint campaign")
    queries = {path.parent.name: read_json(path) for path in (run / "captures").glob("*/result.json")}
    entries = {}
    for path in sorted((run / "prerequisites").glob("*.json")):
        prereq = read_json(path)
        issuer, block = path.stem.split("_")
        wanted = prereq["metadata"]["implementation_address"] if issuer == "usdc" else CONTRACTS[issuer]["address"]
        matching = [queries[qid] for qid in prereq["query_ids"] if queries[qid]["method"] == "eth_getCode" and queries[qid]["params"][0] == wanted]
        if len(matching) != 1 or matching[0]["status"] != "valid_rpc_response":
            raise ValueError("Historical implementation/contract code association missing")
        row = matching[0]
        raw = bytes.fromhex(row["result"][2:])
        code_hash = digest(raw)
        key = (issuer, wanted, code_hash)
        if key not in entries:
            entries[key] = {"issuer": issuer, "address": wanted, "chain_id": 1,
                            "role": "usdc_implementation" if issuer == "usdc" else "usdt_canonical_contract",
                            "runtime_bytes_sha256": code_hash, "runtime_bytecode_length_bytes": len(raw),
                            "expected_read_signature": CONTRACTS[issuer]["read_signature"],
                            "expected_selector": CONTRACTS[issuer]["selector"],
                            "push4_selector_instruction_offsets": push4_offsets(row["result"], CONTRACTS[issuer]["selector"]),
                            "observations": [], "historical_source_association_verified": False,
                            "historical_implementation_bytecode_reproduced": False}
        entries[key]["observations"].append({"block_number": int(block), "code_query_id": row["query_id"],
                                             "prerequisite_path": str(path.relative_to(run)),
                                             "prerequisite_sha256": digest(path.read_bytes())})
    return list(entries.values())


def prepare(out, run):
    if out.exists():
        raise ValueError("Refusing to overwrite frozen historical interface inventory")
    entries = inventory(run)
    queries = []
    for entry in entries:
        address = entry["address"]
        # API v2 includes match status and compiled/onchain bytecode when available;
        # legacy full_match metadata is separately captured without following sources.
        queries.extend([
            {"id": f"{address}_verification", "address": address, "kind": "sourcify_v2_contract_all",
             "url": f"https://sourcify.dev/server/v2/contract/1/{address}?fields=all"},
            {"id": f"{address}_metadata", "address": address, "kind": "sourcify_full_match_metadata",
             "url": f"https://repo.sourcify.dev/contracts/full_match/1/{address}/metadata.json"},
        ])
    if len(queries) > 6:
        raise ValueError("Inventory exceeds approved six logical GET budget; freeze expansion separately")
    frozen = {"version": VERSION, "status": "frozen_before_external_interface_lookup",
              "frozen_at_utc": utc_now(), "source_run": str(run),
              "source_collection_manifest_sha256": digest((run / "collection_manifest.json").read_bytes()),
              "source_collection_summary_sha256": digest((run / "summary.json").read_bytes()),
              "preparation_script_sha256": digest(Path(__file__).read_bytes()),
              "entries": entries, "lookup_not_yet_executed": True,
              "interpretation": "PUSH4 selector occurrence is a structural check, not proof of dispatcher behavior or ABI meaning. Current indexed metadata only links historical captured code if the exact runtime bytecode matches. No local compiler reproduction or human adjudication is implied."}
    immutable(out / "inventory.json", frozen)
    immutable(out / "lookup_plan.json", {"inventory_sha256": digest((out / "inventory.json").read_bytes()),
              "maximum_logical_gets": 6, "maximum_http_attempts": 12, "maximum_attempts_per_get": 2,
              "minimum_request_interval_seconds": 0.5, "queries": queries,
              "stop_rule": "Stop on429; no automatic source downloads, compilation, provider expansion or RPC queries."})
    immutable(out / "preparation_source.py", Path(__file__).read_bytes(), raw=True)
    return {"inventory_entries": len(entries), "unique_usdc_implementation_addresses": len({e["address"] for e in entries if e["issuer"] == "usdc"}),
            "unique_usdt_code_hashes": len({e["runtime_bytes_sha256"] for e in entries if e["issuer"] == "usdt"}),
            "inventory_sha256": digest((out / "inventory.json").read_bytes()), "planned_logical_gets": len(queries)}


def fetch(out, transport=get_once, sleep=time.sleep):
    frozen, plan = read_json(out / "inventory.json"), read_json(out / "lookup_plan.json")
    if frozen["preparation_script_sha256"] != digest(Path(__file__).read_bytes()) or plan["inventory_sha256"] != digest((out / "inventory.json").read_bytes()):
        raise ValueError("Frozen inventory/script hash mismatch")
    rows, stop = [], False
    for query in plan["queries"]:
        directory = out / "captures" / query["id"]
        if (directory / "result.json").exists():
            row = read_json(directory / "result.json")
            for attempt in directory.glob("attempt_*"):
                metadata = read_json(attempt / "capture.json")
                if metadata["response_body_sha256"] != digest((attempt / "response.body").read_bytes()):
                    raise ValueError("Existing lookup capture hash mismatch")
            rows.append(row)
            if row.get("rate_limit_stop"):
                stop = True
                break
            continue
        row = {**query, "attempts": [], "status": "lookup_gap", "rate_limit_stop": False}
        for number in (1, 2):
            attempt = directory / f"attempt_{number}"
            if attempt.exists():
                raise ValueError("Interrupted lookup attempt requires manual accounting; never overwrite")
            sleep(0.5)
            immutable(attempt / "started.json", {"at_utc": utc_now(), "url": query["url"]})
            result = transport(query["url"])
            body = result.pop("body")
            immutable(attempt / "response.body", body, raw=True)
            record = {**result, "retrieved_at_utc": utc_now(), "requested_url": query["url"], "response_body_sha256": digest(body)}
            immutable(attempt / "capture.json", record)
            row["attempts"].append({"number": number, "http_status": record["http_status"], "response_body_sha256": digest(body)})
            if record["http_status"] == 429:
                row["rate_limit_stop"], stop = True, True
                break
            if record["http_status"] == 200 and not record.get("transport_error"):
                try:
                    data = json.loads(body)
                    if not isinstance(data, dict):
                        raise ValueError("Metadata is not a JSON object")
                    row["status"] = "captured_json_pending_exact_code_match_analysis"
                    break
                except (ValueError, UnicodeError):
                    pass
            if record["http_status"] in (301, 302, 303, 307, 308, 400, 404):
                break
        immutable(directory / "result.json", row)
        rows.append(row)
        if stop:
            break
    summary = {"status": "bounded_interface_metadata_capture_not_compiler_reproduction", "logical_gets_processed": len(rows),
               "http_attempts_started": len(list((out / "captures").glob("*/attempt_*/started.json"))),
               "json_captures": sum(r["status"] == "captured_json_pending_exact_code_match_analysis" for r in rows),
               "rate_limit_stop": stop, "results": rows, "historical_implementation_bytecode_reproduced": False,
               "human_reference_complete": False}
    immutable(out / "lookup_summary.json", summary)
    return summary


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--run", type=Path, default=ROOT / "analysis/issuer_candidate_snapshots/cohort_endpoint_v1")
    parser.add_argument("--out-dir", type=Path, default=ROOT / "analysis/historical_interface_verification/v1")
    parser.add_argument("--fetch", action="store_true")
    args = parser.parse_args()
    print(json.dumps(fetch(args.out_dir) if args.fetch else prepare(args.out_dir, args.run), indent=2))


if __name__ == "__main__":
    main()
