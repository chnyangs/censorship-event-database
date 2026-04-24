#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Build dataset release artifacts from event YAML files.

Emits three files at the repo root:
  - dataset.json       full events, pretty-printed, sort_keys for reproducibility
  - dataset.csv        per-event summary row (one line per event)
  - dataset.meta.json  stable metadata sidecar: version, cutoff, counts, schema,
                       commit sha, generator. This is the file external consumers
                       (citation tooling, downstream pipelines, the static site,
                       evidence-chain / comparable-case reports) should pin
                       against when they claim a particular dataset snapshot.

dataset.meta.json schema (stable, do not break without a CHANGELOG entry):
  {
    "dataset_name":      "censorship-event-database",
    "dataset_version":   "0.1.0",                 # CITATION.cff `version`
    "schema_version":    "0.2.0",                 # unique across events, fails otherwise
    "cutoff_date":       "2026-04-21",            # max(last_verified, last_human_audit) across events;
                                                  # canonical definition in docs/limitations-and-use.md §2.5
    "generated_at":      "2026-04-23T10:20:30Z",  # UTC ISO-8601
    "source_commit":     "abc1234",               # short sha, "" if not in a git checkout
    "event_count":       53,
    "counts_by_status":  {"admitted": 53, ...},
    "counts_by_stratum": {"S1_ofac_sdn": 26, ...},
    "counts_by_shape":   {"cascade": 2, ...},
    "counts_by_tier":    {"anchor_case": 5, ...},
    "generator": {
      "script":  "scripts/build_dataset.py",
      "version": "1.0.0",
      "python":  "3.12.x"
    },
    "citation_hint":
      "Yang X. (2026). Cross-Layer Censorship Event Database (version 0.1.0). [DOI placeholder]. https://github.com/chnyangs/censorship-event-database"
  }
"""

from __future__ import annotations

import argparse
import collections
import csv
import json
import platform
import subprocess
import sys
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _dataset_meta import now_utc_iso  # noqa: E402


REPO_ROOT = Path(__file__).resolve().parent.parent
EVENTS_DIR = REPO_ROOT / "events"
CITATION_CFF = REPO_ROOT / "CITATION.cff"

GENERATOR_VERSION = "1.0.0"
DATASET_NAME = "censorship-event-database"
DATASET_URL = "https://github.com/chnyangs/censorship-event-database"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build dataset artifacts.")
    parser.add_argument("--json-out", default=str(REPO_ROOT / "dataset.json"))
    parser.add_argument("--csv-out", default=str(REPO_ROOT / "dataset.csv"))
    parser.add_argument("--meta-out", default=str(REPO_ROOT / "dataset.meta.json"))
    return parser.parse_args()


def load_events() -> list[dict]:
    events = []
    for path in sorted(EVENTS_DIR.glob("*.yaml")):
        if path.name == "TEMPLATE.yaml" or path.name.startswith("_"):
            continue
        event = yaml.safe_load(path.read_text())
        event["_source_file"] = path.name
        events.append(event)
    return events


def json_default(value):
    if isinstance(value, (datetime, date)):
        return value.isoformat()
    raise TypeError(f"Object of type {type(value).__name__} is not JSON serializable")


def summarize_event(event: dict) -> dict[str, object]:
    changed_layers = sorted(
        {
            obs["layer"]
            for obs in event.get("observations", [])
            if obs.get("observation_kind") == "observed_change"
        }
    )
    return {
        "id": event.get("id"),
        "status": event.get("status"),
        "research_stratum": event.get("research_stratum"),
        "empirical_shape": event.get("empirical_shape"),
        "admission_tier": event.get("admission_tier"),
        "trigger_type": event.get("trigger", {}).get("type"),
        "trigger_actor": event.get("trigger", {}).get("actor"),
        "trigger_timestamp": event.get("trigger", {}).get("timestamp"),
        "jurisdiction": ",".join(event.get("jurisdiction", [])),
        "changed_layer_count": len(changed_layers),
        "changed_layers": ",".join(changed_layers),
        "source_file": event.get("_source_file"),
    }


def read_cff_version() -> str:
    """Single source of truth for dataset_version is CITATION.cff. If the file
    isn't there yet (pre-release), fall back to '0.0.0-unreleased' so meta
    files generated before the first tag remain parseable."""
    if not CITATION_CFF.exists():
        return "0.0.0-unreleased"
    for line in CITATION_CFF.read_text().splitlines():
        line = line.strip()
        if line.startswith("version:"):
            v = line.split(":", 1)[1].strip().strip("'\"")
            return v or "0.0.0-unreleased"
    return "0.0.0-unreleased"


def git_short_sha() -> str:
    """Best-effort short sha. Returns '' in environments without git."""
    try:
        out = subprocess.run(
            ["git", "rev-parse", "--short=7", "HEAD"],
            cwd=REPO_ROOT, capture_output=True, text=True, timeout=5, check=False,
        )
        if out.returncode == 0:
            return out.stdout.strip()
    except (FileNotFoundError, subprocess.SubprocessError):
        pass
    return ""


def parse_date_value(value: Any) -> date | None:
    if value is None:
        return None
    if isinstance(value, date) and not isinstance(value, datetime):
        return value
    if isinstance(value, datetime):
        return value.date()
    try:
        return datetime.strptime(str(value), "%Y-%m-%d").date()
    except ValueError:
        return None


def build_meta(events: list[dict]) -> dict[str, Any]:
    schema_versions = {e.get("schema_version") for e in events if e.get("schema_version")}
    if len(schema_versions) != 1:
        # Prefer a hard signal: drifted schema_version is a data-quality bug that
        # downstream consumers must never silently accept.
        raise SystemExit(
            f"[build_dataset] inconsistent schema_version across events: {sorted(schema_versions)}. "
            "Every event must declare the same schema_version; resolve before regenerating."
        )
    schema_version = next(iter(schema_versions))

    # cutoff_date = max(last_verified, last_human_audit) across events.
    # Canonical definition: docs/limitations-and-use.md §2.5. MAX (not MIN)
    # because cutoff is the snapshot's upper bound of verification activity
    # — "dataset includes events verified up through this date" — aligning
    # with the paper/arxiv "as of" convention. For per-event freshness floor
    # (lower bound), see analysis/staleness.md.
    cutoff: date | None = None
    for e in events:
        for key in ("last_verified", "last_human_audit"):
            parsed = parse_date_value(e.get(key))
            if parsed is not None and (cutoff is None or parsed > cutoff):
                cutoff = parsed

    def counter(field: str) -> dict[str, int]:
        c: collections.Counter = collections.Counter()
        for e in events:
            v = e.get(field)
            if v:
                c[v] += 1
        return dict(sorted(c.items()))

    dataset_version = read_cff_version()
    dataset_url = DATASET_URL
    meta = {
        "dataset_name": DATASET_NAME,
        "dataset_version": dataset_version,
        "schema_version": schema_version,
        "cutoff_date": cutoff.isoformat() if cutoff else None,
        "generated_at": now_utc_iso(),
        "source_commit": git_short_sha(),
        "event_count": len(events),
        "counts_by_status": counter("status"),
        "counts_by_stratum": counter("research_stratum"),
        "counts_by_shape": counter("empirical_shape"),
        "counts_by_tier": counter("admission_tier"),
        "generator": {
            "script": "scripts/build_dataset.py",
            "version": GENERATOR_VERSION,
            "python": platform.python_version(),
        },
        "dataset_url": dataset_url,
        "citation_hint": (
            f"Yang, Xiangwen. ({now_utc_iso()[:4]}). "
            f"Cross-Layer Censorship Event Database (version {dataset_version}). "
            f"{dataset_url}. See CITATION.cff for canonical BibTeX / APA / DOI."
        ),
    }
    return meta


def main() -> int:
    args = parse_args()
    events = load_events()

    json_out = Path(args.json_out)
    csv_out = Path(args.csv_out)
    meta_out = Path(args.meta_out)

    json_out.write_text(json.dumps(events, indent=2, sort_keys=True, default=json_default))

    rows = [summarize_event(event) for event in events]
    fieldnames = list(rows[0].keys()) if rows else [
        "id", "status", "research_stratum", "empirical_shape", "admission_tier",
        "trigger_type", "trigger_actor", "trigger_timestamp", "jurisdiction",
        "changed_layer_count", "changed_layers", "source_file",
    ]
    with csv_out.open("w", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)

    meta = build_meta(events)
    meta_out.write_text(json.dumps(meta, indent=2, sort_keys=True) + "\n")

    print(f"Wrote {len(events)} events to {json_out} and {csv_out}")
    print(
        f"Wrote metadata to {meta_out} "
        f"(version={meta['dataset_version']}, cutoff={meta['cutoff_date']}, "
        f"commit={meta['source_commit'] or 'n/a'})"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
