#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Collect a bounded daily OONI metadata frame for two unresolved L0 cases.

The OONI API is queried by country, root domain, test and one-day UTC interval.
Successful empty queries establish only that this API query returned no rows.
They do not establish successful access or absence of blocking. Raw measurements
must be reviewed before anomaly/confirmed flags become censorship findings.
"""
from __future__ import annotations

import argparse
import concurrent.futures
import hashlib
import json
import pathlib
import threading
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import date, datetime, timedelta, timezone

ROOT = pathlib.Path(__file__).resolve().parent.parent
API = "https://api.ooni.io/api/v1/measurements"
VERSION = "1.0.0"
USER_AGENT = "CensorshipCorpusResearch/1.0 (bounded academic metadata collection)"
FRAMES = (
    {"event_id": "ethiopia-nbe-exchange-website-block-2025-11", "probe_cc": "ET",
     "start": "2025-09-15", "end_exclusive": "2025-12-07",
     "domains": ("binance.com", "okx.com", "bybit.com")},
    {"event_id": "thailand-sec-unlicensed-exchange-block-2025-06", "probe_cc": "TH",
     "start": "2025-05-15", "end_exclusive": "2025-07-29",
     "domains": ("bybit.com", "1000x.live", "coinex.com", "okx.com", "xt.com")},
)


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def digest(raw: bytes) -> str:
    return "sha256:" + hashlib.sha256(raw).hexdigest()


def atomic_json(path: pathlib.Path, value) -> None:
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n")
    tmp.replace(path)


def build_queries() -> list[dict]:
    rows = []
    for frame in FRAMES:
        current, stop = date.fromisoformat(frame["start"]), date.fromisoformat(frame["end_exclusive"])
        while current < stop:
            following = current + timedelta(days=1)
            for domain in frame["domains"]:
                core = {"event_id": frame["event_id"], "probe_cc": frame["probe_cc"],
                        "domain": domain, "test_name": "web_connectivity",
                        "since": current.isoformat(), "until": following.isoformat()}
                encoded = json.dumps(core, sort_keys=True, separators=(",", ":")).encode()
                rows.append({"query_id": hashlib.sha256(encoded).hexdigest()[:20], **core})
            current = following
    return rows


def query_url(row: dict, limit: int, offset: int) -> str:
    params = {key: row[key] for key in ("probe_cc", "domain", "test_name", "since", "until")}
    params.update(limit=limit, offset=offset, order="asc", order_by="measurement_start_time")
    return API + "?" + urllib.parse.urlencode(params)


class RateLimiter:
    def __init__(self, interval: float):
        self.interval, self.next_start, self.lock = interval, 0.0, threading.Lock()

    def wait(self):
        with self.lock:
            now = time.monotonic()
            delay = max(0.0, self.next_start - now)
            self.next_start = max(now, self.next_start) + self.interval
        if delay:
            time.sleep(delay)


def fetch(url: str, timeout: float, limiter: RateLimiter) -> dict:
    limiter.wait()
    started = utc_now()
    before = time.monotonic()
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT, "Accept": "application/json"})
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            raw = response.read()
            return {"status": "http_response", "http_status": response.status,
                    "final_url": response.url, "body": raw, "error": None,
                    "started_at_utc": started, "finished_at_utc": utc_now(),
                    "elapsed_seconds": round(time.monotonic() - before, 3)}
    except urllib.error.HTTPError as exc:
        return {"status": "http_response", "http_status": exc.code,
                "final_url": exc.url, "body": exc.read(), "error": str(exc),
                "started_at_utc": started, "finished_at_utc": utc_now(),
                "elapsed_seconds": round(time.monotonic() - before, 3)}
    except (urllib.error.URLError, TimeoutError, OSError) as exc:
        return {"status": "transport_error", "http_status": None,
                "final_url": url, "body": b"", "error": f"{type(exc).__name__}: {exc}",
                "started_at_utc": started, "finished_at_utc": utc_now(),
                "elapsed_seconds": round(time.monotonic() - before, 3)}


def validate_page(row: dict, payload: dict) -> list[dict]:
    if not isinstance(payload, dict) or not isinstance(payload.get("metadata"), dict) or not isinstance(payload.get("results"), list):
        raise ValueError("Malformed OONI response")
    start = datetime.fromisoformat(row["since"] + "T00:00:00+00:00")
    end = datetime.fromisoformat(row["until"] + "T00:00:00+00:00")
    for result in payload["results"]:
        if result.get("probe_cc") != row["probe_cc"] or result.get("test_name") != row["test_name"]:
            raise ValueError("Result is outside declared country/test frame")
        value = datetime.fromisoformat(result["measurement_start_time"].replace("Z", "+00:00"))
        if not start <= value < end:
            raise ValueError("Result is outside declared UTC day")
        host = (urllib.parse.urlsplit(result.get("input") or "").hostname or "").lower().rstrip(".")
        domain = row["domain"]
        if host != domain and not host.endswith("." + domain):
            raise ValueError("Result input is outside declared root domain")
    return payload["results"]


def collect_one(row: dict, captures: pathlib.Path, limiter: RateLimiter,
                timeout: float, attempts: int, page_limit: int, max_rows: int) -> dict:
    target = captures / row["query_id"]
    summary_path = target / "summary.json"
    if summary_path.exists():
        saved = json.loads(summary_path.read_text())
        if saved.get("query") != row:
            raise ValueError(f"Existing query identity mismatch: {row['query_id']}")
        for page in saved.get("pages", []):
            body = target / page["body_file"]
            if not body.exists() or digest(body.read_bytes()) != page["body_sha256"]:
                raise ValueError(f"Existing capture hash mismatch: {body}")
        return saved
    target.mkdir(parents=True, exist_ok=False)
    pages, results, offset, expected = [], [], 0, None
    terminal_error = None
    while expected is None or offset < expected:
        if offset >= max_rows:
            terminal_error = f"declared_max_rows_{max_rows}_exceeded"
            break
        url = query_url(row, min(page_limit, max_rows - offset), offset)
        accepted = None
        for attempt in range(1, attempts + 1):
            response = fetch(url, timeout, limiter)
            raw = response.pop("body")
            body_name = f"page_{offset:06d}_attempt_{attempt}.body"
            (target / body_name).write_bytes(raw)
            record = {**response, "attempt": attempt, "request_url": url,
                      "body_file": body_name, "body_sha256": digest(raw), "bytes": len(raw)}
            pages.append(record)
            if response["http_status"] == 200:
                try:
                    payload = json.loads(raw)
                    accepted = (payload, validate_page(row, payload))
                    break
                except (json.JSONDecodeError, KeyError, TypeError, ValueError) as exc:
                    record["validation_error"] = f"{type(exc).__name__}: {exc}"
        if accepted is None:
            terminal_error = "page_unavailable_or_invalid"
            break
        payload, found = accepted
        count = payload["metadata"].get("count")
        if not isinstance(count, int) or count < 0:
            terminal_error = "invalid_metadata_count"
            break
        if expected is None:
            expected = count
        elif expected != count:
            terminal_error = "metadata_count_changed_during_pagination"
            break
        results.extend(found)
        if not found:
            if expected != offset:
                terminal_error = "pagination_ended_before_metadata_count"
            break
        offset += len(found)
    identities = [(r.get("measurement_url"), r.get("report_id"), r.get("input")) for r in results]
    if len(identities) != len(set(identities)):
        terminal_error = terminal_error or "duplicate_measurement_rows"
    complete = terminal_error is None and expected == len(results)
    summary = {"query": row, "status": "complete" if complete else "incomplete",
               "metadata_count": expected, "retrieved_rows": len(results),
               "pagination_complete": complete, "terminal_error": terminal_error,
               "pages": pages, "distinct_report_ids": len({r.get("report_id") for r in results}),
               "distinct_asns": len({r.get("probe_asn") for r in results}),
               "anomaly_rows": sum(bool(r.get("anomaly")) for r in results),
               "confirmed_rows": sum(bool(r.get("confirmed")) for r in results),
               "failure_rows": sum(bool(r.get("failure")) for r in results),
               "measurement_rows": results,
               "interpretation": "Metadata frame only; ASN is not an independent probe count, and flags require raw-measurement review."}
    atomic_json(summary_path, summary)
    return summary


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out-dir", type=pathlib.Path, default=ROOT / "analysis/evidence_repairs/l0_ooni_daily_v1")
    parser.add_argument("--workers", type=int, default=3)
    parser.add_argument("--request-interval", type=float, default=0.5)
    parser.add_argument("--timeout", type=float, default=25)
    parser.add_argument("--attempts", type=int, default=2)
    parser.add_argument("--page-limit", type=int, default=500)
    parser.add_argument("--max-rows-per-day-domain", type=int, default=5000)
    args = parser.parse_args()
    if args.workers < 1 or args.workers > 4 or args.request_interval < 0.25 or args.attempts not in (1, 2):
        raise SystemExit("Refusing unsafe concurrency/rate/retry configuration")
    queries = build_queries()
    query_bytes = json.dumps(queries, sort_keys=True, separators=(",", ":")).encode()
    source_bytes = pathlib.Path(__file__).read_bytes()
    manifest = {"procedure_version": VERSION, "status": "frozen_before_collection",
                "api": API, "api_use": "modest daily metadata queries; not batch raw-data download",
                "official_docs": ["https://api.ooni.org/", "https://github.com/ooni/data"],
                "created_at_utc": utc_now(), "query_count": len(queries), "queries": queries,
                "query_set_sha256": digest(query_bytes),
                "collector_source_sha256": digest(source_bytes),
                "workers": args.workers, "minimum_request_start_interval_seconds": args.request_interval,
                "max_attempts_per_page": args.attempts, "page_limit": args.page_limit,
                "max_rows_per_day_domain": args.max_rows_per_day_domain,
                "interpretation": "Successful zero-count days are coverage gaps, not access-success or no-blocking observations.",
                "human_review": False, "raw_measurement_review_complete": False}
    args.out_dir.mkdir(parents=True, exist_ok=True)
    manifest_path = args.out_dir / "manifest.json"
    if manifest_path.exists():
        old = json.loads(manifest_path.read_text())
        for volatile in ("created_at_utc",):
            old.pop(volatile, None); manifest.pop(volatile, None)
        if old != manifest:
            raise SystemExit("Refusing to resume with a changed frozen manifest")
    else:
        atomic_json(manifest_path, manifest)
    captures = args.out_dir / "captures"
    captures.mkdir(exist_ok=True)
    limiter = RateLimiter(args.request_interval)
    summaries = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures = {pool.submit(collect_one, q, captures, limiter, args.timeout, args.attempts,
                               args.page_limit, args.max_rows_per_day_domain): q for q in queries}
        for index, future in enumerate(concurrent.futures.as_completed(futures), 1):
            summaries.append(future.result())
            if index % 50 == 0:
                print(f"completed {index}/{len(queries)} daily-domain queries", flush=True)
    summaries.sort(key=lambda r: (r["query"]["event_id"], r["query"]["since"], r["query"]["domain"]))
    complete = [r for r in summaries if r["pagination_complete"]]
    rows = sum(r["retrieved_rows"] for r in complete)
    report = {"status": "complete" if len(complete) == len(summaries) else "partial",
              "query_count": len(summaries), "complete_queries": len(complete),
              "failed_or_incomplete_queries": len(summaries) - len(complete),
              "zero_count_complete_queries": sum(r["metadata_count"] == 0 for r in complete),
              "metadata_rows": rows,
              "distinct_report_ids": len({m.get("report_id") for r in complete for m in r["measurement_rows"]}),
              "events": {}, "raw_measurements_retrieved": 0, "human_review": False,
              "conclusion": "This run measures availability of OONI metadata under the frozen daily queries. It does not establish blocking or non-blocking."}
    for event in sorted({q["event_id"] for q in queries}):
        selected = [r for r in summaries if r["query"]["event_id"] == event]
        report["events"][event] = {"queries": len(selected),
            "complete_queries": sum(r["pagination_complete"] for r in selected),
            "metadata_rows": sum(r["retrieved_rows"] for r in selected if r["pagination_complete"]),
            "domains_with_rows": sorted({r["query"]["domain"] for r in selected if r["retrieved_rows"]}),
            "measurement_denominator_status": "metadata_frame_complete_raw_review_pending" if all(r["pagination_complete"] for r in selected) else "retrieval_incomplete"}
    atomic_json(args.out_dir / "query_summaries.json", summaries)
    atomic_json(args.out_dir / "summary.json", report)
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
