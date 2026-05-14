#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Build a corpus-level physical-action registry.

Event records are the primary unit of analysis, but a single physical action
(transaction, commit, takedown, or policy action) can intentionally appear in
more than one event record. This registry is the corpus-level dedupe surface:
it groups observed_change rows by canonical action id and makes duplicated
event rows explicit.
"""

from __future__ import annotations

import argparse
import collections
import csv
import json
import pathlib
import sys
from typing import Any

import yaml


GENERATOR_VERSION = "0.1.0"
REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent
EVENTS_DIR = REPO_ROOT / "events"
DEFAULT_OUT_DIR = REPO_ROOT / "derived"

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from _dataset_meta import load_meta, now_utc_iso, reproducible_python  # noqa: E402


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build physical-action registry.")
    parser.add_argument("--events-dir", default=str(EVENTS_DIR))
    parser.add_argument("--out-dir", default=str(DEFAULT_OUT_DIR))
    return parser.parse_args()


def load_events(events_dir: pathlib.Path) -> list[dict[str, Any]]:
    events: list[dict[str, Any]] = []
    for path in sorted(events_dir.glob("*.yaml")):
        if path.name == "TEMPLATE.yaml" or path.name.startswith("_"):
            continue
        event = yaml.safe_load(path.read_text())
        if isinstance(event, dict) and event.get("status") == "admitted":
            events.append(event)
    return events


def observation_action_id(event_id: str, obs_idx: int, obs: dict[str, Any]) -> str:
    action_id = obs.get("action_id")
    if isinstance(action_id, str) and action_id.strip():
        return action_id.strip()
    return (
        f"{event_id}:{obs_idx}:{obs.get('layer')}:{obs.get('actor')}:"
        f"{obs.get('event')}"
    )


def build_rows(events: list[dict[str, Any]]) -> list[dict[str, Any]]:
    observation_rows: list[dict[str, Any]] = []
    for event in events:
        event_id = str(event.get("id") or "unknown")
        for obs_idx, obs in enumerate(event.get("observations") or []):
            if not isinstance(obs, dict):
                continue
            if obs.get("observation_kind") != "observed_change":
                continue
            action_id = observation_action_id(event_id, obs_idx, obs)
            duplicate_of = obs.get("duplicate_of_action_id")
            is_duplicate_row = isinstance(duplicate_of, str) and bool(duplicate_of.strip())
            canonical_id = (
                duplicate_of.strip()
                if is_duplicate_row
                else action_id
            )
            observation_rows.append({
                "canonical_action_id": canonical_id,
                "action_id": action_id,
                "is_canonical_row": not is_duplicate_row,
                "is_duplicate_row": is_duplicate_row,
                "duplicate_of_action_id": duplicate_of or "",
                "event_id": event_id,
                "observation_index": obs_idx,
                "layer": obs.get("layer") or "",
                "actor": obs.get("actor") or "",
                "event": obs.get("event") or "",
                "attribution": obs.get("attribution") or "",
                "timestamp": str(obs.get("timestamp") or ""),
            })

    grouped: dict[str, list[dict[str, Any]]] = collections.defaultdict(list)
    for row in observation_rows:
        grouped[str(row["canonical_action_id"])].append(row)

    out_rows: list[dict[str, Any]] = []
    for canonical_id, rows in sorted(grouped.items()):
        event_ids = sorted({str(row["event_id"]) for row in rows})
        layers = sorted({str(row["layer"]) for row in rows if row.get("layer")})
        canonical_rows = [row for row in rows if row["is_canonical_row"]]
        duplicate_rows = [row for row in rows if row["is_duplicate_row"]]
        first = canonical_rows[0] if canonical_rows else rows[0]
        out_rows.append({
            "canonical_action_id": canonical_id,
            "row_count": len(rows),
            "duplicate_row_count": len(duplicate_rows),
            "event_count": len(event_ids),
            "event_ids": ";".join(event_ids),
            "layers": ";".join(layers),
            "canonical_event_id": first["event_id"],
            "canonical_layer": first["layer"],
            "canonical_actor": first["actor"],
            "canonical_event": first["event"],
            "canonical_timestamp": first["timestamp"],
            "observation_rows": rows,
        })
    return out_rows


CSV_COLUMNS = [
    "canonical_action_id",
    "row_count",
    "duplicate_row_count",
    "event_count",
    "event_ids",
    "layers",
    "canonical_event_id",
    "canonical_layer",
    "canonical_actor",
    "canonical_event",
    "canonical_timestamp",
]


def render_markdown(rows: list[dict[str, Any]], ds_meta: dict[str, Any]) -> str:
    duplicated = [row for row in rows if row["duplicate_row_count"]]
    lines = [
        "# Physical action registry",
        "",
        f"Dataset snapshot: **v{ds_meta.get('dataset_version')}** · "
        f"cutoff `{ds_meta.get('cutoff_date')}` · "
        f"commit `{ds_meta.get('source_commit')}` · generated `{now_utc_iso()}`",
        "",
        "This registry deduplicates physical actions that appear in more than "
        "one event record. Event-level rates remain event-record denominators; "
        "this table is the corpus-level action denominator.",
        "",
        f"- Canonical physical actions: **{len(rows)}**",
        f"- Duplicated action rows: **{sum(row['duplicate_row_count'] for row in rows)}**",
        f"- Actions with duplicates: **{len(duplicated)}**",
        "",
        "| canonical_action_id | rows | duplicate rows | events | layers | canonical row |",
        "| --- | ---: | ---: | ---: | --- | --- |",
    ]
    for row in rows:
        lines.append(
            f"| `{row['canonical_action_id']}` | {row['row_count']} | "
            f"{row['duplicate_row_count']} | {row['event_count']} | "
            f"{row['layers'] or '—'} | "
            f"`{row['canonical_event_id']}::{row['canonical_layer']}` |"
        )
    return "\n".join(lines) + "\n"


def main() -> int:
    args = parse_args()
    events = load_events(pathlib.Path(args.events_dir))
    out_dir = pathlib.Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    rows = build_rows(events)

    csv_path = out_dir / "action_registry.csv"
    with csv_path.open("w", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=CSV_COLUMNS, extrasaction="ignore", lineterminator="\n")
        writer.writeheader()
        for row in rows:
            writer.writerow({key: row.get(key, "") for key in CSV_COLUMNS})

    json_path = out_dir / "action_registry.json"
    json_path.write_text(json.dumps(rows, indent=2, sort_keys=True) + "\n")

    ds_meta = load_meta()
    md_path = out_dir / "action_registry.md"
    md_path.write_text(render_markdown(rows, ds_meta))

    meta = {
        "artifact": "action_registry",
        "generated_at": now_utc_iso(),
        "generator": {
            "script": "scripts/build_action_registry.py",
            "version": GENERATOR_VERSION,
            "python": reproducible_python(),
        },
        "dataset_snapshot": {
            "dataset_version": ds_meta.get("dataset_version"),
            "schema_version": ds_meta.get("schema_version"),
            "cutoff_date": ds_meta.get("cutoff_date"),
            "source_commit": ds_meta.get("source_commit"),
        },
        "canonical_action_count": len(rows),
        "duplicated_action_row_count": sum(row["duplicate_row_count"] for row in rows),
        "csv_columns": CSV_COLUMNS,
    }
    (out_dir / "action_registry.meta.json").write_text(
        json.dumps(meta, indent=2, sort_keys=True) + "\n"
    )
    print(
        "[build_action_registry] wrote action_registry.csv + "
        "action_registry.json + action_registry.md + action_registry.meta.json"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
