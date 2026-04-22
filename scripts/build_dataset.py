#!/usr/bin/env python3
"""Build a simple JSON and CSV release artifact from event YAML files."""

from __future__ import annotations

import argparse
import csv
import json
from datetime import date, datetime
from pathlib import Path

import yaml


REPO_ROOT = Path(__file__).resolve().parent.parent
EVENTS_DIR = REPO_ROOT / "events"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build dataset artifacts.")
    parser.add_argument("--json-out", default=str(REPO_ROOT / "dataset.json"))
    parser.add_argument("--csv-out", default=str(REPO_ROOT / "dataset.csv"))
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


def main() -> int:
    args = parse_args()
    events = load_events()

    json_out = Path(args.json_out)
    csv_out = Path(args.csv_out)
    json_out.write_text(json.dumps(events, indent=2, sort_keys=True, default=json_default))

    rows = [summarize_event(event) for event in events]
    fieldnames = list(rows[0].keys()) if rows else [
        "id",
        "status",
        "research_stratum",
        "empirical_shape",
        "admission_tier",
        "trigger_type",
        "trigger_actor",
        "trigger_timestamp",
        "jurisdiction",
        "changed_layer_count",
        "changed_layers",
        "source_file",
    ]
    with csv_out.open("w", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"Wrote {len(events)} events to {json_out} and {csv_out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
