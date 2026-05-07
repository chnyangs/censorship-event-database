#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Backfill query-cell metadata into legacy archived OONI artifacts."""
from __future__ import annotations

import argparse
import hashlib
import json
import pathlib
import sys
import urllib.parse
from typing import Any

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from ooni_batch_query import query_hash  # noqa: E402


REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent
DEFAULT_SUMMARY = REPO_ROOT / "sources" / "l0_datasets" / "_summary.json"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Backfill OONI query-cell metadata.")
    parser.add_argument("--summary", default=str(DEFAULT_SUMMARY))
    return parser.parse_args()


def load_json(path: pathlib.Path) -> Any:
    return json.loads(path.read_text())


def body_path(row: dict[str, Any], repo_root: pathlib.Path = REPO_ROOT) -> pathlib.Path:
    raw = row.get("body_path")
    if not raw:
        raise SystemExit(f"missing body_path for row {row!r}")
    path = pathlib.Path(str(raw))
    return path if path.is_absolute() else repo_root / path


def infer_params(row: dict[str, Any], data: dict[str, Any]) -> dict[str, Any]:
    query_url = row.get("query_url") or data.get("_query_url")
    if not query_url:
        raise SystemExit(f"{row.get('body_path')}: missing query_url")
    parsed = urllib.parse.urlparse(str(query_url))
    qs = urllib.parse.parse_qs(parsed.query)

    def first(name: str, fallback: Any = "") -> str:
        values = qs.get(name)
        if values:
            return str(values[0])
        return str(fallback or "")

    input_url = row.get("input_url") or first("input", f"https://{row.get('domain')}/")
    domain = row.get("domain") or first("domain") or urllib.parse.urlparse(input_url).hostname or ""
    params: dict[str, Any] = {
        "input": input_url,
        "since": row.get("since") or first("since"),
        "until": row.get("until") or first("until"),
        "limit": int(first("limit", 100) or 100),
        "test_name": first("test_name", "web_connectivity"),
        "domain": domain,
    }
    probe_cc = row.get("probe_cc") or first("probe_cc")
    if probe_cc and probe_cc != "*":
        params["probe_cc"] = probe_cc
    return params


def backfill_summary(summary_path: pathlib.Path = DEFAULT_SUMMARY) -> int:
    rows = load_json(summary_path)
    if not isinstance(rows, list):
        raise SystemExit(f"{summary_path}: expected JSON array")

    updated = 0
    out_rows: list[dict[str, Any]] = []
    for row in rows:
        if not isinstance(row, dict):
            continue
        path = body_path(row)
        data = load_json(path)
        if not isinstance(data, dict):
            raise SystemExit(f"{path}: expected JSON object")

        params = data.get("_query_params") if isinstance(data.get("_query_params"), dict) else infer_params(row, data)
        q_hash = data.get("_query_hash") or query_hash(params)
        data["_query_params"] = params
        data["_query_hash"] = q_hash
        data["_query_urls"] = data.get("_query_urls") or [data.get("_query_url") or row.get("query_url")]
        data["_pagination_complete"] = (
            data.get("_pagination_complete")
            if data.get("_pagination_complete") is not None
            else not bool((data.get("metadata") or {}).get("next_url"))
        )
        data["_page_count"] = data.get("_page_count") or 1

        serialized = json.dumps(data, indent=2, sort_keys=True) + "\n"
        path.write_text(serialized)
        body_hash = hashlib.sha256(serialized.encode()).hexdigest()

        out = dict(row)
        out["event_id"] = out.get("event_id") or out.get("slug")
        out["input_url"] = params.get("input") or ""
        out["probe_cc"] = params.get("probe_cc") or "*"
        out["query_hash"] = q_hash
        out["pagination_complete"] = data["_pagination_complete"]
        out["page_count"] = data["_page_count"]
        out["body_hash"] = body_hash
        out_rows.append(out)
        updated += 1

    summary_path.write_text(json.dumps(out_rows, indent=2, sort_keys=True) + "\n")
    return updated


def main() -> int:
    args = parse_args()
    count = backfill_summary(pathlib.Path(args.summary))
    print(f"[backfill_l0_query_metadata] updated {count} OONI artifact row(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
