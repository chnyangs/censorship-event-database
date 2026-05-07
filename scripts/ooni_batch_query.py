#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Batch-query the OONI public API and persist denominator-scoped raw results.

The input may be either the legacy mapping format in `scripts/ooni_domains.json`
or a list of query records. Internally every query is normalized to one
`{event_id, domain, input_url, probe_cc, since, until}` cell so repeated
domain/event windows cannot overwrite each other. Output filenames include a
query hash; zero-result queries remain query-attempt artifacts, not
`observed_no_change` evidence.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import pathlib
import sys
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from typing import Any


OONI_API = "https://api.ooni.io/api/v1/measurements"
DEFAULT_LIMIT = 100
DEFAULT_MAX_PAGES = 20


def query_hash(params: dict[str, Any]) -> str:
    payload = json.dumps(params, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(payload.encode()).hexdigest()[:16]


def build_query_params(record: dict[str, Any], limit: int = DEFAULT_LIMIT) -> dict[str, Any]:
    params: dict[str, Any] = {
        "input": record["input_url"],
        "since": record["since"],
        "until": record["until"],
        "limit": limit,
        "test_name": "web_connectivity",
        "domain": record["domain"],
    }
    if record.get("probe_cc"):
        params["probe_cc"] = record["probe_cc"]
    return params


def query_url(params: dict[str, Any]) -> str:
    return f"{OONI_API}?{urllib.parse.urlencode(params)}"


def _fetch_json(url: str) -> dict[str, Any]:
    req = urllib.request.Request(url, headers={"User-Agent": "p1-event-db ooni-batch"})
    with urllib.request.urlopen(req, timeout=30) as r:
        data = json.loads(r.read().decode())
    return data if isinstance(data, dict) else {"results": data}


def query_ooni(record: dict[str, Any], limit: int = DEFAULT_LIMIT, max_pages: int = DEFAULT_MAX_PAGES) -> dict:
    params = build_query_params(record, limit)
    first_url = query_url(params)
    url: str | None = first_url
    pages: list[dict[str, Any]] = []
    results: list[Any] = []
    query_urls: list[str] = []

    try:
        while url and len(pages) < max_pages:
            data = _fetch_json(url)
            pages.append(data.get("metadata") or {})
            query_urls.append(url)
            if isinstance(data.get("results"), list):
                results.extend(data["results"])
            next_url = (data.get("metadata") or {}).get("next_url") or data.get("next_url")
            url = urllib.parse.urljoin(OONI_API, next_url) if next_url else None
        return {
            "_query_url": first_url,
            "_query_urls": query_urls,
            "_query_params": params,
            "_query_hash": query_hash(params),
            "_pagination_complete": url is None,
            "_page_count": len(pages),
            "metadata": pages[0] if pages else {},
            "page_metadata": pages,
            "results": results,
        }
    except Exception as exc:
        return {
            "_query_url": first_url,
            "_query_params": params,
            "_query_hash": query_hash(params),
            "_error": str(exc),
            "results": [],
        }


def normalize_input_url(domain: str, value: str | None) -> str:
    if not value:
        return f"https://{domain}/"
    if value.startswith(("http://", "https://")):
        return value
    return f"https://{value}"


def normalize_query_records(raw: Any) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    if isinstance(raw, dict):
        for domain, cfg in raw.items():
            if not isinstance(cfg, dict):
                raise SystemExit(f"{domain}: expected object config")
            slugs = cfg.get("slugs") or []
            if isinstance(slugs, str):
                slugs = [slugs]
            for slug in slugs:
                records.append(
                    {
                        "event_id": slug,
                        "domain": domain,
                        "input_url": normalize_input_url(domain, cfg.get("input_url")),
                        "probe_cc": cfg.get("probe_cc"),
                        "since": cfg.get("since", "2020-01-01"),
                        "until": cfg.get("until", datetime.now(timezone.utc).strftime("%Y-%m-%d")),
                    }
                )
        return records

    if not isinstance(raw, list):
        raise SystemExit("domains file must be a mapping or a list of query records")
    for cfg in raw:
        if not isinstance(cfg, dict):
            raise SystemExit(f"malformed query record: {cfg!r}")
        event_id = cfg.get("event_id") or cfg.get("slug")
        domain = cfg.get("domain")
        if not event_id or not domain:
            raise SystemExit(f"query record requires event_id and domain: {cfg!r}")
        url_variants = cfg.get("url_variants") or [cfg.get("input_url") or f"https://{domain}/"]
        if isinstance(url_variants, str):
            url_variants = [url_variants]
        probe_ccs = cfg.get("probe_ccs") or [cfg.get("probe_cc")]
        if isinstance(probe_ccs, str):
            probe_ccs = [probe_ccs]
        for input_url in url_variants:
            for probe_cc in probe_ccs:
                records.append(
                    {
                        "event_id": event_id,
                        "domain": domain,
                        "input_url": normalize_input_url(domain, input_url),
                        "probe_cc": probe_cc,
                        "since": cfg.get("since", "2020-01-01"),
                        "until": cfg.get("until", datetime.now(timezone.utc).strftime("%Y-%m-%d")),
                    }
                )
    return records


def output_file_name(record: dict[str, Any], q_hash: str) -> str:
    safe_domain = record["domain"].replace("/", "_")
    scheme = urllib.parse.urlparse(record["input_url"]).scheme or "input"
    probe = (record.get("probe_cc") or "all").lower()
    return f"{safe_domain}__{scheme}__{probe}__{q_hash}__ooni.json"


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--domains-file", required=True,
                   help="JSON mapping or list of OONI query records.")
    p.add_argument("--output-dir", default="sources/l0_datasets",
                   help="Output directory for per-domain JSON.")
    p.add_argument("--limit", type=int, default=DEFAULT_LIMIT)
    p.add_argument("--max-pages", type=int, default=DEFAULT_MAX_PAGES)
    args = p.parse_args()

    records = normalize_query_records(json.loads(pathlib.Path(args.domains_file).read_text()))
    out_root = pathlib.Path(args.output_dir)
    out_root.mkdir(parents=True, exist_ok=True)

    summary = []
    for record in records:
        print(
            f"[query] {record['event_id']} {record['domain']} "
            f"{record['input_url']} {record['since']}..{record['until']} "
            f"probe={record.get('probe_cc') or '*'}"
        )

        data = query_ooni(record, limit=args.limit, max_pages=args.max_pages)
        result_count = len(data.get("results") or []) if "results" in data else 0

        slug_dir = out_root / record["event_id"]
        slug_dir.mkdir(parents=True, exist_ok=True)
        q_hash = data.get("_query_hash") or query_hash(build_query_params(record, args.limit))
        out_path = slug_dir / output_file_name(record, q_hash)
        serialized = json.dumps(data, indent=2, sort_keys=True)
        out_path.write_text(serialized)
        body_hash = hashlib.sha256(serialized.encode()).hexdigest()
        summary.append({
            "domain": record["domain"],
            "input_url": record["input_url"],
            "probe_cc": record.get("probe_cc"),
            "slug": record["event_id"],
            "event_id": record["event_id"],
            "result_count": result_count,
            "body_hash": body_hash,
            "body_path": str(out_path),
            "since": record["since"],
            "until": record["until"],
            "query_hash": q_hash,
            "query_url": data.get("_query_url"),
            "pagination_complete": data.get("_pagination_complete"),
            "page_count": data.get("_page_count"),
            "error": data.get("_error"),
        })

    summary_path = out_root / "_summary.json"
    summary_path.write_text(json.dumps(summary, indent=2, sort_keys=True))
    print(f"[done] wrote {len(summary)} entries to {summary_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
