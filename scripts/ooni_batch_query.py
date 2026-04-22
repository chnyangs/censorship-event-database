#!/usr/bin/env python3
"""
Batch-query the OONI public API for a list of domains and persist raw results
for L0-layer observation admission.

For each domain: pull measurements from the OONI public API for a configurable
time window, write per-domain JSON + summary CSV. The output artifacts live at
sources/l0_datasets/<slug>/<domain>__ooni.json with a canonical body_hash so
events can attach them as semi_primary_measurement.
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


OONI_API = "https://api.ooni.io/api/v1/measurements"
DEFAULT_LIMIT = 100


def query_ooni(domain: str, since: str, until: str, limit: int = DEFAULT_LIMIT) -> dict:
    qs = urllib.parse.urlencode({
        "input": f"https://{domain}/",
        "since": since,
        "until": until,
        "limit": limit,
        "test_name": "web_connectivity",
    })
    url = f"{OONI_API}?{qs}"
    req = urllib.request.Request(url, headers={"User-Agent": "p1-event-db ooni-batch"})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            data = json.loads(r.read().decode())
        data["_query_url"] = url
        return data
    except Exception as exc:
        return {"_query_url": url, "_error": str(exc)}


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--domains-file", required=True,
                   help="JSON file mapping domain -> list of event slugs + optional window.")
    p.add_argument("--output-dir", default="sources/l0_datasets",
                   help="Output directory for per-domain JSON.")
    args = p.parse_args()

    domains = json.loads(pathlib.Path(args.domains_file).read_text())
    out_root = pathlib.Path(args.output_dir)
    out_root.mkdir(parents=True, exist_ok=True)

    summary = []
    for domain, cfg in domains.items():
        slugs = cfg["slugs"]
        since = cfg.get("since", "2020-01-01")
        until = cfg.get("until", datetime.now(timezone.utc).strftime("%Y-%m-%d"))
        print(f"[query] {domain} {since}..{until} ({len(slugs)} slug refs)")

        data = query_ooni(domain, since, until)
        result_count = len(data.get("results") or []) if "results" in data else 0

        # Write to first slug directory
        for slug in slugs:
            slug_dir = out_root / slug
            slug_dir.mkdir(parents=True, exist_ok=True)
            out_path = slug_dir / f"{domain.replace('/', '_')}__ooni.json"
            serialized = json.dumps(data, indent=2, sort_keys=True)
            out_path.write_text(serialized)
            body_hash = hashlib.sha256(serialized.encode()).hexdigest()
            summary.append({
                "domain": domain,
                "slug": slug,
                "result_count": result_count,
                "body_hash": body_hash,
                "body_path": str(out_path),
                "since": since,
                "until": until,
                "query_url": data.get("_query_url"),
                "error": data.get("_error"),
            })

    summary_path = out_root / "_summary.json"
    summary_path.write_text(json.dumps(summary, indent=2, sort_keys=True))
    print(f"[done] wrote {len(summary)} entries to {summary_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
