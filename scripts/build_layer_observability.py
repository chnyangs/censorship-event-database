#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Coverage-aware per-layer observability table.

Turns "L0/L1/L3 had zero observed_change entries" from a potentially
misleading bare count into a **coverage-aware empirical claim** by always
reporting the denominator a reader would need to evaluate it:

  - measured_count / partially_measured_count / not_measured_count /
    not_applicable_count — the coverage composition for this layer
    across the admitted corpus
  - changed_count / no_change_count / coverage_gap_count — the
    observation composition
  - changed_given_measured — change rate conditioned on the layer being
    flagged as measured
  - changed_given_measured_or_partial — broader denominator including
    partially_measured coverage

The Paper claim this artifact enables:
    "Across 53 admitted events, observed_change entries are concentrated
     on L4 frontend, asset_onchain, and offramp_cex. L0 and L3 show
     zero changes, but with {not_measured: X / applicable: Y} denominators
     — this is an observability gap in the evidence corpus, not proof
     of absence of censorship at those layers."

Output (under derived/):
  - layer_observability.csv    one row per layer
  - layer_observability.json   richer structured form (same rows + per-event drilldown)
  - layer_observability.meta.json  snapshot identity
"""

from __future__ import annotations

import argparse
import collections
import csv
import json
import pathlib
import platform
import sys
from datetime import datetime, timezone
from typing import Any

import yaml


LAYER_ORDER = [
    "l0_network", "l1_consensus", "l3_rpc",
    "l4_frontend", "asset_onchain", "offramp_cex",
]
GENERATOR_VERSION = "0.1.0"

REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent
EVENTS_DIR = REPO_ROOT / "events"
DEFAULT_OUT_DIR = REPO_ROOT / "derived"

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from _dataset_meta import load_meta  # noqa: E402


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Build layer observability table.")
    p.add_argument("--events-dir", default=str(EVENTS_DIR))
    p.add_argument("--out-dir", default=str(DEFAULT_OUT_DIR))
    return p.parse_args()


def load_events(events_dir: pathlib.Path) -> list[dict]:
    out = []
    for f in sorted(events_dir.glob("*.yaml")):
        if f.name == "TEMPLATE.yaml" or f.name.startswith("_"):
            continue
        out.append(yaml.safe_load(f.read_text()))
    return out


def compute_row(layer: str, events: list[dict]) -> dict[str, Any]:
    total = len(events)
    cov_status = collections.Counter()
    changed_events: list[str] = []
    changed_under_measured: list[str] = []
    changed_under_measured_or_partial: list[str] = []
    no_change_events: list[str] = []
    gap_events: list[str] = []

    for e in events:
        slug = e.get("id") or "unknown"

        # coverage status for this layer (None if not declared — treated
        # as "missing", which is a data-quality issue surfaced separately).
        status = None
        for c in e.get("coverage") or []:
            if isinstance(c, dict) and c.get("layer") == layer:
                status = c.get("status")
                break
        cov_status[status or "missing"] += 1

        # observation composition on this layer
        kinds_here = {
            obs.get("observation_kind")
            for obs in e.get("observations") or []
            if isinstance(obs, dict) and obs.get("layer") == layer
        }
        is_changed = "observed_change" in kinds_here
        if is_changed:
            changed_events.append(slug)
            if status == "measured":
                changed_under_measured.append(slug)
            if status in ("measured", "partially_measured"):
                changed_under_measured_or_partial.append(slug)
        elif "observed_no_change" in kinds_here:
            no_change_events.append(slug)
        if "coverage_gap" in kinds_here:
            gap_events.append(slug)

    measured = cov_status.get("measured", 0)
    partial = cov_status.get("partially_measured", 0)
    not_measured = cov_status.get("not_measured", 0)
    not_applicable = cov_status.get("not_applicable", 0)
    missing = cov_status.get("missing", 0)
    applicable = total - not_applicable - missing

    def safe_ratio(num: int, denom: int) -> float | None:
        return None if denom == 0 else num / denom

    changed_n = len(changed_events)
    # Coverage-matched numerators: only count a `changed` row if its
    # coverage status is in the same subset as the denominator. Mixing
    # `partially_measured`-coverage rows into the `measured`-only
    # denominator inflates the ratio (see P1 in the 2026-04-23 review).
    changed_m = len(changed_under_measured)
    changed_mp = len(changed_under_measured_or_partial)
    return {
        "layer": layer,
        "total_events": total,
        "applicable_event_count": applicable,
        "measured_count": measured,
        "partially_measured_count": partial,
        "not_measured_count": not_measured,
        "not_applicable_count": not_applicable,
        "missing_coverage_count": missing,
        "changed_count": changed_n,
        "changed_under_measured_count": changed_m,
        "changed_under_measured_or_partial_count": changed_mp,
        "no_change_count": len(no_change_events),
        "coverage_gap_count": len(gap_events),
        "changed_given_measured": safe_ratio(changed_m, measured),
        "changed_given_measured_or_partial": safe_ratio(changed_mp, measured + partial),
        "changed_given_applicable": safe_ratio(changed_n, applicable),
        # event lists for drilldown (JSON only)
        "changed_event_ids": sorted(changed_events),
        "changed_under_measured_event_ids": sorted(changed_under_measured),
        "changed_under_measured_or_partial_event_ids": sorted(changed_under_measured_or_partial),
        "no_change_event_ids": sorted(no_change_events),
        "coverage_gap_event_ids": sorted(gap_events),
    }


CSV_COLUMNS = [
    "layer",
    "total_events",
    "applicable_event_count",
    "measured_count",
    "partially_measured_count",
    "not_measured_count",
    "not_applicable_count",
    "missing_coverage_count",
    "changed_count",
    "changed_under_measured_count",
    "changed_under_measured_or_partial_count",
    "no_change_count",
    "coverage_gap_count",
    "changed_given_measured",
    "changed_given_measured_or_partial",
    "changed_given_applicable",
]


def _fmt(value: Any) -> Any:
    if isinstance(value, float):
        return round(value, 4)
    if isinstance(value, bool):
        return "true" if value else "false"
    if value is None:
        return ""
    return value


def main() -> int:
    args = parse_args()
    events_dir = pathlib.Path(args.events_dir)
    out_dir = pathlib.Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    events = load_events(events_dir)
    rows = [compute_row(layer, events) for layer in LAYER_ORDER]

    csv_path = out_dir / "layer_observability.csv"
    with csv_path.open("w", newline="") as fh:
        writer = csv.DictWriter(
            fh, fieldnames=CSV_COLUMNS, extrasaction="ignore", lineterminator="\n"
        )
        writer.writeheader()
        for r in rows:
            writer.writerow({k: _fmt(r.get(k)) for k in CSV_COLUMNS})

    json_path = out_dir / "layer_observability.json"
    json_path.write_text(json.dumps(rows, indent=2, sort_keys=True) + "\n")

    ds_meta = load_meta()
    meta = {
        "artifact": "layer_observability",
        "generated_at": datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z"),
        "generator": {
            "script": "scripts/build_layer_observability.py",
            "version": GENERATOR_VERSION,
            "python": platform.python_version(),
        },
        "dataset_snapshot": {
            "dataset_version": ds_meta.get("dataset_version"),
            "schema_version": ds_meta.get("schema_version"),
            "cutoff_date": ds_meta.get("cutoff_date"),
            "source_commit": ds_meta.get("source_commit"),
        },
        "total_events": len(events),
        "csv_columns": CSV_COLUMNS,
        "interpretation_notes": [
            "`changed_given_measured` and `changed_given_measured_or_partial`",
            "are the only ratios that support coverage-aware empirical claims",
            "about a layer. Both are coverage-matched: the numerator counts",
            "only the subset of observed_change events whose coverage status",
            "is in the same bucket as the denominator. Mixing partially_measured",
            "rows into a measured-only denominator would inflate the ratio.",
            "Bare `changed_count` without a denominator is meaningful only",
            "in combination with the coverage composition.",
            "A layer with changed_count = 0 and not_measured_count large is",
            "an observability gap — NOT evidence that censorship does not",
            "occur at that layer.",
        ],
    }
    (out_dir / "layer_observability.meta.json").write_text(
        json.dumps(meta, indent=2, sort_keys=True) + "\n"
    )

    print(
        f"[build_layer_observability] wrote 6 rows (one per layer) to "
        f"{csv_path.name} + {json_path.name} + layer_observability.meta.json "
        f"(dataset v{ds_meta.get('dataset_version')} cutoff {ds_meta.get('cutoff_date')})"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
