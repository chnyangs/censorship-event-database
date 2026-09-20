#!/usr/bin/env python3
"""Retry every incomplete query from a frozen OONI daily-frame run.

The retry set is selected only from retrieval status, never from anomaly or
blocking fields.  Original attempts remain immutable in the source run.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from collect_ooni_daily_frame import RateLimiter, atomic_json, collect_one, digest


ROOT = Path(__file__).resolve().parents[1]
VERSION = "1.0.0"


def load_retry_set(source_dir: Path) -> tuple[list[dict], dict]:
    manifest_path = source_dir / "manifest.json"
    summaries_path = source_dir / "query_summaries.json"
    report_path = source_dir / "summary.json"
    for path in (manifest_path, summaries_path, report_path):
        if not path.is_file():
            raise ValueError(f"Completed source-run artifact missing: {path}")
    manifest = json.loads(manifest_path.read_text())
    summaries = json.loads(summaries_path.read_text())
    report = json.loads(report_path.read_text())
    if len(summaries) != manifest["query_count"] or report["query_count"] != len(summaries):
        raise ValueError("Source-run query count mismatch")
    by_id = {}
    retry = []
    for row in summaries:
        query = row.get("query")
        if not isinstance(query, dict) or query.get("query_id") in by_id:
            raise ValueError("Malformed or duplicate source query summary")
        qid = query["query_id"]
        by_id[qid] = row
        original = source_dir / "captures" / qid / "summary.json"
        if not original.is_file() or json.loads(original.read_text()) != row:
            raise ValueError(f"Aggregate/original query summary mismatch: {qid}")
        if row.get("pagination_complete") is not True:
            retry.append(query)
    if len(retry) != report["failed_or_incomplete_queries"]:
        raise ValueError("Source-run incomplete count mismatch")
    retry.sort(key=lambda q: (q["event_id"], q["since"], q["domain"], q["query_id"]))
    inputs = {
        "source_manifest_sha256": digest(manifest_path.read_bytes()),
        "source_query_summaries_sha256": digest(summaries_path.read_bytes()),
        "source_summary_sha256": digest(report_path.read_bytes()),
    }
    return retry, inputs


def run(source_dir: Path, out_dir: Path, *, timeout: float = 60.0,
        interval: float = 1.0, attempts: int = 1) -> dict:
    if timeout < 25 or interval < 0.5 or attempts != 1:
        raise ValueError("Retry profile requires timeout>=25, interval>=0.5 and one new attempt")
    queries, inputs = load_retry_set(source_dir)
    source_hash = digest(Path(__file__).read_bytes())
    manifest = {
        "procedure_version": VERSION,
        "status": "frozen_before_retry_requests",
        "selection_rule": "Every and only pagination-incomplete query in the completed source run; outcome and anomaly fields are ignored.",
        "source_directory": str(source_dir),
        **inputs,
        "retry_collector_sha256": source_hash,
        "imported_collector_sha256": digest(Path(__file__).with_name("collect_ooni_daily_frame.py").read_bytes()),
        "retry_query_count": len(queries),
        "queries": queries,
        "timeout_seconds": timeout,
        "minimum_request_start_interval_seconds": interval,
        "new_attempts_per_page": attempts,
        "page_limit": 500,
        "max_rows_per_day_domain": 5000,
        "interpretation": "A successful retry repairs metadata-frame retrieval only; raw measurement review remains separate.",
    }
    out_dir.mkdir(parents=True, exist_ok=True)
    manifest_path = out_dir / "manifest.json"
    if manifest_path.exists():
        if json.loads(manifest_path.read_text()) != manifest:
            raise ValueError("Refusing to resume a changed retry manifest or collector")
    else:
        atomic_json(manifest_path, manifest)
    captures = out_dir / "captures"
    captures.mkdir(exist_ok=True)
    limiter = RateLimiter(interval)
    summaries = [collect_one(query, captures, limiter, timeout, attempts, 500, 5000)
                 for query in queries]
    complete = [row for row in summaries if row.get("pagination_complete") is True]
    report = {
        "status": "complete" if len(complete) == len(summaries) else "partial",
        "retry_query_count": len(summaries),
        "completed_retries": len(complete),
        "still_incomplete": len(summaries) - len(complete),
        "metadata_rows": sum(row.get("retrieved_rows", 0) for row in complete),
        "anomaly_rows": sum(row.get("anomaly_rows", 0) for row in complete),
        "confirmed_rows": sum(row.get("confirmed_rows", 0) for row in complete),
        "raw_measurements_retrieved": 0,
        "human_review": False,
        "conclusion": "Retry results concern metadata availability; they do not establish blocking or non-blocking.",
    }
    atomic_json(out_dir / "query_summaries.json", summaries)
    atomic_json(out_dir / "summary.json", report)
    return report


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-dir", type=Path,
                        default=ROOT / "analysis/evidence_repairs/l0_ooni_daily_v1")
    parser.add_argument("--out-dir", type=Path,
                        default=ROOT / "analysis/evidence_repairs/l0_ooni_daily_retry_v1")
    parser.add_argument("--timeout", type=float, default=60.0)
    parser.add_argument("--request-interval", type=float, default=1.0)
    args = parser.parse_args()
    print(json.dumps(run(args.source_dir, args.out_dir, timeout=args.timeout,
                         interval=args.request_interval), indent=2))


if __name__ == "__main__":
    main()
