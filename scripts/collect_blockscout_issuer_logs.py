#!/usr/bin/env python3
"""Freeze and collect bounded Blockscout issuer-event streams, without targets.

The four canonical add/remove event topics are fixed before page requests.
Index pagination coverage does not establish independent chain completeness.
"""
from __future__ import annotations

import argparse
import json
import re
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime
from pathlib import Path

from measurement_pilot import CONTRACTS, ROOT, digest, dump, save_attempt, utc_now

HOST = "eth.blockscout.com"
SOURCE_ROOT = ROOT / "analysis/public_blockchain_discovery/blockscout_v1/captures"
COHORT = ROOT / "analysis/issuer_candidate_snapshots/cohort_endpoint_v1"
HEX32 = re.compile(r"0x[0-9a-fA-F]{64}")


def frozen(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("x") as handle:
        handle.write(json.dumps(value, indent=2, sort_keys=True) + "\n")


class SameHostRedirects(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, request, fp, code, message, headers, newurl):
        target = urllib.parse.urlsplit(newurl)
        if target.scheme != "https" or target.hostname != HOST or target.port not in (None, 443):
            raise urllib.error.HTTPError(newurl, code, "Cross-host or non-HTTPS redirect refused", headers, fp)
        return super().redirect_request(request, fp, code, message, headers, newurl)


def fetch(url):
    parsed = urllib.parse.urlsplit(url)
    if parsed.scheme != "https" or parsed.hostname != HOST or parsed.port not in (None, 443):
        raise ValueError("Only the frozen HTTPS Blockscout host is allowed")
    start = time.monotonic()
    request = urllib.request.Request(url, headers={"Accept": "application/json", "User-Agent": "CensorshipCorpusBoundedIndexCollection/1.0"})
    try:
        with urllib.request.build_opener(SameHostRedirects()).open(request, timeout=20) as response:
            length = int(response.headers.get("Content-Length", "0"))
            if length > 1048576:
                body, error = b"", "Page Content-Length exceeds predeclared1MiBguard; body not read"
            else:
                body = response.read(1048577)
                error = "Page body exceeds predeclared1MiBguard" if len(body) > 1048576 else None
            return {"http_status": response.status, "final_url": response.url, "headers": dict(response.headers.items()),
                    "body": body, "transport_error": error, "elapsed_seconds": round(time.monotonic() - start, 3)}
    except urllib.error.HTTPError as exc:
        return {"http_status": exc.code, "final_url": exc.url, "headers": dict(exc.headers.items()),
                "body": exc.read(1048576), "transport_error": str(exc), "elapsed_seconds": round(time.monotonic() - start, 3)}
    except (urllib.error.URLError, OSError, TimeoutError) as exc:
        return {"http_status": None, "final_url": url, "headers": {}, "body": b"",
                "transport_error": str(exc), "elapsed_seconds": round(time.monotonic() - start, 3)}


def prepare(out, cohort=COHORT, max_pages_per_stream=3):
    if out.exists() or not 1 <= max_pages_per_stream <= 200:
        raise ValueError("New output and page cap1..200 required")
    summary = json.loads((cohort / "summary.json").read_text())
    if not summary.get("endpoint_snapshot_campaign_complete"):
        raise ValueError("Completed source-frozen boundary campaign required")
    snapshots = [json.loads(p.read_text()) for p in sorted((cohort / "snapshots").glob("*.json"))]
    if not snapshots or len(snapshots) != summary["recorded_snapshots"]:
        raise ValueError("Snapshot membership/count mismatch")
    first = min(r["block_number"] for r in snapshots)
    last = max(r["block_number"] for r in snapshots)
    sources = {}
    for name in ("current_docs", "current_official_controller", "official_chain_query"):
        path = SOURCE_ROOT / name / "attempt_1/response.body"
        capture = json.loads(path.with_name("capture.json").read_text())
        if capture["http_status"] != 200 or capture["response_body_sha256"] != digest(path.read_bytes()):
            raise ValueError("Required official source capture unavailable or changed")
        sources[name] = {"path": str(path.relative_to(ROOT)), "sha256": digest(path.read_bytes())}
    streams = [{"id": name + "_" + direction, "issuer": name, "contract": spec["address"],
                "event_signature": spec["event_signatures"][i], "topic": spec["topics"][i],
                "direction": direction, "seed_cursor": {"block_number": last + 1, "index": 0, "items_count": 50}}
               for name, spec in CONTRACTS.items() for i, direction in enumerate(("add", "remove"))]
    manifest = {"created_before_page_queries_at_utc": utc_now(), "study_role": "source_defined_issuer_event_index_collection_human_reference_pending",
                "cohort_manifest_sha256": digest((cohort / "collection_manifest.json").read_bytes()),
                "cohort_units_sha256": digest((cohort / "issuer_query_units.jsonl").read_bytes()),
                "snapshot_records_sha256": digest(json.dumps(snapshots, sort_keys=True).encode()),
                "official_sources": sources, "collector_sha256": digest(Path(__file__).read_bytes()),
                "transport_library_sha256": digest(Path(__file__).with_name("measurement_pilot.py").read_bytes()),
                "endpoint_origin": "https://" + HOST, "first_block_inclusive": first, "last_block_inclusive": last,
                "streams": streams, "max_pages_per_stream": max_pages_per_stream,
                "maximum_page_requests": max_pages_per_stream * 4, "max_attempts_per_page": 1,
                "minimum_delay_seconds": 1.0, "maximum_page_bytes": 1048576,
                "selection": "All four predeclared issuer add/remove topics over the global source-cohort block span; no target addresses or observed response labels in request filters",
                "cursor_rule": "Official implementation orders(block_number,index)descending and excludes the cursor; seed(maxBlock+1,0)includes all declared upper-bound logs. Preserve server next_page_params exactly except enforcing the unchanged topic.",
                "termination_rule": "Stop on null next_page_params or after a valid descending page reaches below the declared lower block; cap or any invalid page leaves the stream incomplete",
                "upstream_operator_independence_verified": False, "independent_chain_completeness_verified": False,
                "human_reference_complete": False, "full_window_response_classification": None}
    out.mkdir(parents=True)
    frozen(out / "plan.json", manifest)
    (out / "collector_source.py").write_bytes(Path(__file__).read_bytes())
    (out / "transport_source.py").write_bytes(Path(__file__).with_name("measurement_pilot.py").read_bytes())
    frozen(out / "plan.sha256.json", {"plan_sha256": digest((out / "plan.json").read_bytes())})
    return {"streams": 4, "max_pages_per_stream": max_pages_per_stream, "maximum_page_requests": 4 * max_pages_per_stream,
            "first_block_inclusive": first, "last_block_inclusive": last}


def page_url(stream, cursor):
    params = {**cursor, "topic": stream["topic"]}
    return "https://" + HOST + "/api/v2/addresses/" + stream["contract"] + "/logs?" + urllib.parse.urlencode(params)


def validate_page(data, stream, cursor):
    if not isinstance(data, dict) or not isinstance(data.get("items"), list) or "next_page_params" not in data or len(data["items"]) > 50:
        raise ValueError("Malformed or oversized page")
    previous = (cursor["block_number"], cursor["index"])
    rows = []
    for item in data["items"]:
        if not isinstance(item, dict) or not isinstance(item.get("address"), dict) or str(item["address"].get("hash", "")).lower() != stream["contract"]:
            raise ValueError("Wrong event emitter")
        block, index = item.get("block_number"), item.get("index")
        if type(block) is not int or type(index) is not int or block < 0 or index < 0 or (block, index) >= previous:
            raise ValueError("Page order or cursor exclusion violated")
        previous = (block, index)
        for key in ("block_hash", "transaction_hash"):
            if not isinstance(item.get(key), str) or not HEX32.fullmatch(item[key]):
                raise ValueError("Missing/invalid event identity hash")
        topics = item.get("topics")
        if not isinstance(topics, list):
            raise ValueError("Malformed topics")
        topics = list(topics)
        while topics and topics[-1] is None:
            topics.pop()
        indexed = CONTRACTS[stream["issuer"]]["indexed_address"]
        if len(topics) != (2 if indexed else 1) or any(not isinstance(t, str) or not HEX32.fullmatch(t) for t in topics) or topics[0].lower() != stream["topic"]:
            raise ValueError("Wrong or malformed topic/ABI signature")
        word = topics[1] if indexed else item.get("data")
        if not isinstance(word, str) or not HEX32.fullmatch(word) or word[2:26] != "0" * 24 or (indexed and item.get("data") != "0x"):
            raise ValueError("Malformed event address/data word")
        stamp = item.get("block_timestamp")
        if not isinstance(stamp, str) or datetime.fromisoformat(stamp.replace("Z", "+00:00")).tzinfo is None:
            raise ValueError("Missing timezone-aware block timestamp")
        rows.append({"issuer": stream["issuer"], "direction": stream["direction"], "topic": stream["topic"],
                     "block_number": block, "log_index": index, "block_hash": item["block_hash"].lower(),
                     "transaction_hash": item["transaction_hash"].lower(), "block_timestamp": stamp,
                     "affected_address": "0x" + word[-40:].lower(), "raw_item": item})
    next_cursor = data["next_page_params"]
    if next_cursor is not None:
        if not isinstance(next_cursor, dict) or set(next_cursor) - {"block_number", "index", "items_count", "topic"}:
            raise ValueError("Unknown cursor schema")
        if not rows or any(type(next_cursor.get(k)) is not int or next_cursor[k] < 0 for k in ("block_number", "index", "items_count")):
            raise ValueError("Malformed or nonterminating empty-page cursor")
        if (next_cursor["block_number"], next_cursor["index"]) != previous or next_cursor.get("topic", stream["topic"]) != stream["topic"]:
            raise ValueError("Cursor does not match final item or changed topic")
    return rows, next_cursor


def run(out, transport=fetch):
    manifest = json.loads((out / "plan.json").read_text())
    if json.loads((out / "plan.sha256.json").read_text())["plan_sha256"] != digest((out / "plan.json").read_bytes()):
        raise ValueError("Frozen plan hash mismatch")
    if manifest["collector_sha256"] != digest(Path(__file__).read_bytes()) or manifest["transport_library_sha256"] != digest(Path(__file__).with_name("measurement_pilot.py").read_bytes()):
        raise ValueError("Code changed after plan freeze")
    summaries, accepted, globally_stopped = [], {}, False
    for stream in manifest["streams"]:
        cursor = stream["seed_cursor"]
        summary = {"stream": stream["id"], "pages_processed": 0, "index_range_complete": False,
                   "stop_reason": "global_rate_limit_stop" if globally_stopped else "page_cap", "accepted_logs": 0}
        if globally_stopped:
            summaries.append(summary)
            continue
        for page in range(1, manifest["max_pages_per_stream"] + 1):
            url = page_url(stream, cursor)
            directory = out / "captures" / stream["id"] / f"page_{page}"
            try:
                if not directory.exists():
                    if transport is fetch:
                        time.sleep(manifest["minimum_delay_seconds"])
                    save_attempt(directory, transport(url), None, url)
                meta = json.loads((directory / "capture.json").read_text())
                body = (directory / "response.body").read_bytes()
                if meta["request_url"] != url or meta["response_body_sha256"] != digest(body):
                    raise ValueError("Frozen page URL/response hash mismatch")
                if meta["http_status"] == 429:
                    globally_stopped = True
                    raise ValueError("rate_limit_stop")
                if meta["http_status"] != 200 or meta["transport_error"]:
                    raise ValueError(meta["transport_error"] or "HTTP gap")
                rows, following = validate_page(json.loads(body), stream, cursor)
                local = {}
                for row in rows:
                    if row["block_number"] > manifest["last_block_inclusive"]:
                        raise ValueError("Upper bound violated")
                    if row["block_number"] < manifest["first_block_inclusive"]:
                        continue
                    key = (row["transaction_hash"], row["log_index"], row["block_hash"])
                    if key in accepted and accepted[key] != row:
                        raise ValueError("Conflicting duplicate identity")
                    local[key] = row
                accepted.update(local)
                summary["pages_processed"] += 1
                summary["accepted_logs"] += len(local)
                summary["last_cursor"] = following
                summary["last_page_lowest_block"] = rows[-1]["block_number"] if rows else None
                if following is None or any(row["block_number"] < manifest["first_block_inclusive"] for row in rows):
                    summary.update(index_range_complete=True, stop_reason="endpoint_exhausted" if following is None else "declared_lower_bound_reached")
                    break
                cursor = following
            except (ValueError, TypeError, KeyError, OSError) as exc:
                summary["stop_reason"] = str(exc)
                break
        summaries.append(summary)
        dump(out / "stream_progress.json", summaries)
    rows = sorted(accepted.values(), key=lambda r: (r["block_number"], r["log_index"]))
    dump(out / "accepted_logs.json", rows)
    summary = {"streams": summaries, "pages_captured": len(list((out / "captures").rglob("capture.json"))),
               "all_four_index_ranges_complete": len(summaries) == 4 and all(s["index_range_complete"] for s in summaries),
               "accepted_unique_logs": len(rows), "maximum_page_requests": manifest["maximum_page_requests"],
               "independent_chain_completeness_verified": False, "upstream_operator_independence_verified": False,
               "human_reference_complete": False, "full_window_response_classification": None}
    dump(out / "summary.json", summary)
    return summary


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    p = sub.add_parser("prepare")
    p.add_argument("--out-dir", required=True, type=Path)
    p.add_argument("--cohort", type=Path, default=COHORT)
    p.add_argument("--max-pages-per-stream", type=int, default=3)
    p = sub.add_parser("run")
    p.add_argument("--plan-dir", required=True, type=Path)
    args = parser.parse_args()
    value = prepare(args.out_dir, args.cohort, args.max_pages_per_stream) if args.command == "prepare" else run(args.plan_dir)
    print(json.dumps(value, indent=2))


if __name__ == "__main__":
    main()
