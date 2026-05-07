#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Build the v0.1 L3 provider denominator census."""
from __future__ import annotations

import argparse
import collections
import csv
import json
import pathlib
import sys
from typing import Any

import yaml


REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent
DEFAULT_INPUT = REPO_ROOT / "sampling" / "l3_provider_census.yaml"
DEFAULT_OUT_DIR = REPO_ROOT / "derived"
GENERATOR_VERSION = "0.1.0"

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from _dataset_meta import load_meta, now_utc_iso, repo_relative_path, reproducible_python  # noqa: E402


COLUMNS = [
    "event_id",
    "provider_id",
    "provider_name",
    "surface_type",
    "public_endpoint",
    "public_replay_possible",
    "docs_bracketed",
    "git_filter_file",
    "event_specific_artifact",
    "artifact_ref",
    "denominator_class",
    "rate_eligible",
    "denominator_reason",
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build L3 provider denominator census artifacts.")
    parser.add_argument("--input", default=str(DEFAULT_INPUT))
    parser.add_argument("--out-dir", default=str(DEFAULT_OUT_DIR))
    return parser.parse_args()


def scalar(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, bool):
        return "true" if value else "false"
    return str(value)


def load_frame(path: pathlib.Path) -> dict[str, Any]:
    data = yaml.safe_load(path.read_text())
    if not isinstance(data, dict):
        raise SystemExit(f"{path}: expected YAML object")
    return data


def build_rows(frame: dict[str, Any]) -> list[dict[str, Any]]:
    events = frame.get("event_windows") or {}
    providers = frame.get("providers") or []
    rows: list[dict[str, Any]] = []
    for provider in providers:
        provider_windows = provider.get("event_windows") or {}
        for event_id in events:
            cell = provider_windows.get(event_id) or {}
            rows.append(
                {
                    "event_id": event_id,
                    "provider_id": provider.get("provider_id") or "",
                    "provider_name": provider.get("provider_name") or "",
                    "surface_type": provider.get("surface_type") or "",
                    "public_endpoint": provider.get("public_endpoint") or "",
                    "public_replay_possible": provider.get("public_replay_possible") or "",
                    "docs_bracketed": bool(cell.get("docs_bracketed")),
                    "git_filter_file": bool(cell.get("git_filter_file")),
                    "event_specific_artifact": bool(cell.get("event_specific_artifact")),
                    "artifact_ref": cell.get("artifact_ref") or "",
                    "denominator_class": cell.get("denominator_class") or "observability_gap",
                    "rate_eligible": bool(cell.get("rate_eligible")),
                    "denominator_reason": " ".join(str(cell.get("denominator_reason") or "").split()),
                }
            )
    rows.sort(key=lambda row: (row["event_id"], row["provider_id"]))
    return rows


def write_csv(rows: list[dict[str, Any]], path: pathlib.Path) -> None:
    with path.open("w", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=COLUMNS, lineterminator="\n")
        writer.writeheader()
        for row in rows:
            writer.writerow({key: scalar(row.get(key)) for key in COLUMNS})


def build_meta(rows: list[dict[str, Any]], input_path: pathlib.Path) -> dict[str, Any]:
    dataset_meta = load_meta()
    return {
        "dataset_version": dataset_meta.get("dataset_version"),
        "cutoff_date": dataset_meta.get("cutoff_date"),
        "source_commit": dataset_meta.get("source_commit"),
        "generated_at": now_utc_iso(),
        "generator": pathlib.Path(__file__).name,
        "generator_version": GENERATOR_VERSION,
        "python": reproducible_python(),
        "input": repo_relative_path(input_path),
        "row_count": len(rows),
        "rate_eligible_count": sum(1 for row in rows if row["rate_eligible"]),
    }


def build_markdown(rows: list[dict[str, Any]], meta: dict[str, Any]) -> str:
    class_counts = collections.Counter(str(row["denominator_class"]) for row in rows)
    provider_count = len({row["provider_id"] for row in rows})
    event_count = len({row["event_id"] for row in rows})
    lines = [
        "# L3 RPC provider denominator census",
        "",
        f"Dataset snapshot: v{meta.get('dataset_version') or '?'} · "
        f"cutoff `{meta.get('cutoff_date') or 'n/a'}` · "
        f"commit `{meta.get('source_commit') or 'n/a'}` · "
        f"generated `{meta.get('generated_at')}`",
        "",
        "This census is a denominator audit, not a provider-rate result. It "
        "records which provider/event-window cells have replayable public "
        "artifacts and whether any cell is rate-eligible.",
        "",
        f"- Providers / provider classes: {provider_count}",
        f"- Event windows: {event_count}",
        f"- Provider-event rows: {len(rows)}",
        f"- Rate-eligible rows: {meta['rate_eligible_count']}",
        "",
        "## Denominator Classes",
        "",
        "| denominator_class | rows |",
        "| --- | ---: |",
    ]
    for klass, count in sorted(class_counts.items()):
        lines.append(f"| `{klass}` | {count} |")
    lines.extend(
        [
            "",
            "## Provider-Event Surface",
            "",
            "| event_id | provider_id | surface | event artifact | denominator_class | rate eligible |",
            "| --- | --- | --- | --- | --- | ---: |",
        ]
    )
    for row in rows:
        lines.append(
            f"| `{row['event_id']}` | `{row['provider_id']}` | "
            f"`{row['surface_type']}` | {scalar(row['event_specific_artifact'])} | "
            f"`{row['denominator_class']}` | {scalar(row['rate_eligible'])} |"
        )
    lines.extend(
        [
            "",
            "## Phrasing Lock",
            "",
            "- `named_partial_only_no_conditional_rate` supports mechanism prose only.",
            "- `observability_gap` means no event-window provider denominator exists in v0.1.",
            "- An L3 conditional rate remains forbidden until provider-event rows become rate-eligible.",
        ]
    )
    return "\n".join(lines) + "\n"


def write_outputs(rows: list[dict[str, Any]], meta: dict[str, Any], out_dir: pathlib.Path) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    write_csv(rows, out_dir / "l3_provider_census.csv")
    (out_dir / "l3_provider_census.json").write_text(
        json.dumps({"meta": meta, "rows": rows}, indent=2, sort_keys=True) + "\n"
    )
    (out_dir / "l3_provider_census.meta.json").write_text(json.dumps(meta, indent=2, sort_keys=True) + "\n")
    (out_dir / "l3_provider_census.md").write_text(build_markdown(rows, meta))


def main() -> int:
    args = parse_args()
    input_path = pathlib.Path(args.input)
    rows = build_rows(load_frame(input_path))
    meta = build_meta(rows, input_path)
    write_outputs(rows, meta, pathlib.Path(args.out_dir))
    print(f"[l3-provider-census] wrote {len(rows)} rows to {repo_relative_path(pathlib.Path(args.out_dir))}/")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
