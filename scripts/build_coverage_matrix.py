#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Emit event x layer coverage matrix with denominator eligibility labels."""
from __future__ import annotations

import argparse
import collections
import csv
import json
import pathlib
import sys
from datetime import date, datetime
from typing import Any

import yaml

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from _dataset_meta import load_meta, now_utc_iso, reproducible_python  # noqa: E402


REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent
EVENTS_DIR = REPO_ROOT / "events"
DEFAULT_OUT_DIR = REPO_ROOT / "derived"
SAMPLING_FRAME = REPO_ROOT / "sampling" / "frame.yaml"
L0_SUMMARY = REPO_ROOT / "sources" / "l0_datasets" / "_summary.json"

GENERATOR_VERSION = "0.1.0"

LAYER_ORDER = [
    "l0_network",
    "l1_consensus",
    "l3_rpc",
    "l4_frontend",
    "asset_onchain",
    "offramp_cex",
]

COLUMNS = [
    "event_id",
    "status",
    "research_stratum",
    "admission_tier",
    "trigger_type",
    "jurisdiction",
    "layer",
    "coverage_status",
    "denominator_class",
    "denominator_reason",
    "denominator_artifact",
    "rate_reportable",
    "observed_change_count",
    "observed_no_change_count",
    "coverage_gap_count",
    "direct_attribution_count",
    "plausible_attribution_count",
    "first_change_timestamp",
    "source_file",
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build event x layer coverage matrix.")
    parser.add_argument("--events-dir", default=str(EVENTS_DIR))
    parser.add_argument("--out-dir", default=str(DEFAULT_OUT_DIR))
    return parser.parse_args()


def scalar(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, (date, datetime)):
        return value.isoformat()
    return str(value)


def csv_join(values: Any) -> str:
    if not values:
        return ""
    if isinstance(values, str):
        return values
    return ",".join(scalar(value) for value in values)


def display_path(path: pathlib.Path) -> str:
    resolved = path.resolve()
    try:
        return str(resolved.relative_to(REPO_ROOT))
    except ValueError:
        return str(path)


def json_default(value: Any) -> str:
    if isinstance(value, (date, datetime)):
        return value.isoformat()
    return str(value)


def load_events(events_dir: pathlib.Path) -> list[tuple[pathlib.Path, dict[str, Any]]]:
    events: list[tuple[pathlib.Path, dict[str, Any]]] = []
    for path in sorted(events_dir.glob("*.yaml")):
        if path.name == "TEMPLATE.yaml" or path.name.startswith("_"):
            continue
        event = yaml.safe_load(path.read_text())
        if isinstance(event, dict):
            events.append((path, event))
    return events


def denominator_class(layer: str, coverage_status: str) -> str:
    if coverage_status == "not_applicable":
        return "not_applicable"
    if coverage_status == "not_measured":
        return "observability_gap"
    if layer == "asset_onchain" and coverage_status in {"measured", "partially_measured"}:
        return "descriptive_only_structural_circularity_v0_1"
    if layer == "l3_rpc" and coverage_status == "partially_measured":
        return "named_partial_only_no_conditional_rate"
    if coverage_status == "measured":
        return "measured_rate_denominator"
    if coverage_status == "partially_measured":
        return "partial_sensitivity_denominator"
    return "unknown"


def l0_query_index(summary_path: pathlib.Path = L0_SUMMARY) -> dict[str, dict[str, int]]:
    if not summary_path.exists():
        return {}
    raw = json.loads(summary_path.read_text())
    if not isinstance(raw, list):
        return {}
    index: dict[str, dict[str, int]] = {}
    for row in raw:
        if not isinstance(row, dict):
            continue
        event_id = row.get("slug") or row.get("event_id")
        if not event_id:
            continue
        bucket = index.setdefault(str(event_id), {"query_rows": 0, "result_count": 0, "query_errors": 0})
        bucket["query_rows"] += 1
        try:
            bucket["result_count"] += int(row.get("result_count") or 0)
        except (TypeError, ValueError):
            pass
        if row.get("error"):
            bucket["query_errors"] += 1
    return index


def denominator_detail(
    event_id: str,
    layer: str,
    coverage_status: str,
    denom_class: str,
    l0_queries: dict[str, dict[str, int]],
) -> tuple[str, str, str]:
    """Return reason, artifact, and primary-rate eligibility for a layer row."""
    if denom_class == "measured_rate_denominator":
        return "coverage_status_measured_under_layer_protocol", "events/*.yaml", "yes"
    if denom_class == "partial_sensitivity_denominator":
        return "partially_measured_sensitivity_only", "events/*.yaml", "sensitivity_only"
    if denom_class == "not_applicable":
        return "layer_not_applicable_to_trigger_target", "events/*.yaml", "no"
    if layer == "l0_network" and denom_class == "observability_gap":
        query = l0_queries.get(event_id)
        if query and query.get("query_rows", 0) > 0:
            return (
                "ooni_queried_no_measurements; cp_not_ingested_v0_1",
                "derived/l0_coverage_summary.md",
                "no",
            )
        return (
            "not_queried_yet; cp_not_ingested_v0_1",
            "derived/coverage_matrix.md",
            "no",
        )
    if layer == "l3_rpc" and denom_class == "named_partial_only_no_conditional_rate":
        return (
            "named_public_git_observation_no_provider_universe_denominator",
            "derived/l3_provider_census.md",
            "no",
        )
    if layer == "l3_rpc" and denom_class == "observability_gap":
        return (
            "no_event_specific_rpc_provider_artifact_or_probe_denominator",
            "derived/l3_provider_census.md",
            "no",
        )
    if layer == "asset_onchain" and denom_class == "descriptive_only_structural_circularity_v0_1":
        return (
            "positive_onchain_receipts_only_no_independent_no_change_denominator",
            "docs/paper_claims.md#c1--upper-layer-concentration-of-observed-reactions",
            "no",
        )
    if denom_class == "observability_gap":
        return "not_measured_no_rate_denominator", "events/*.yaml", "no"
    return "unknown_denominator_class", "events/*.yaml", "no"


def first_timestamp(observations: list[dict[str, Any]]) -> str:
    timestamps = [
        scalar(observation.get("timestamp"))
        for observation in observations
        if observation.get("observation_kind") == "observed_change"
        and observation.get("timestamp")
    ]
    return sorted(timestamps)[0] if timestamps else ""


def row_for_layer(
    path: pathlib.Path,
    event: dict[str, Any],
    layer: str,
    l0_queries: dict[str, dict[str, int]] | None = None,
) -> dict[str, Any]:
    coverage_by_layer = {
        coverage.get("layer"): coverage
        for coverage in event.get("coverage", [])
        if isinstance(coverage, dict)
    }
    if layer not in coverage_by_layer:
        raise SystemExit(f"{event.get('id')}: missing coverage row for {layer}")

    coverage_status = coverage_by_layer[layer].get("status") or ""
    denom_class = denominator_class(layer, coverage_status)
    reason, artifact, rate_reportable = denominator_detail(
        str(event.get("id") or ""),
        layer,
        coverage_status,
        denom_class,
        l0_queries or {},
    )
    observations = [
        observation
        for observation in event.get("observations", [])
        if observation.get("layer") == layer
    ]
    kind_counts = collections.Counter(observation.get("observation_kind") for observation in observations)
    attribution_counts = collections.Counter(observation.get("attribution") for observation in observations)
    trigger = event.get("trigger") or {}
    return {
        "event_id": event.get("id"),
        "status": event.get("status"),
        "research_stratum": event.get("research_stratum"),
        "admission_tier": event.get("admission_tier"),
        "trigger_type": trigger.get("type"),
        "jurisdiction": csv_join(event.get("jurisdiction")),
        "layer": layer,
        "coverage_status": coverage_status,
        "denominator_class": denom_class,
        "denominator_reason": reason,
        "denominator_artifact": artifact,
        "rate_reportable": rate_reportable,
        "observed_change_count": kind_counts.get("observed_change", 0),
        "observed_no_change_count": kind_counts.get("observed_no_change", 0),
        "coverage_gap_count": kind_counts.get("coverage_gap", 0),
        "direct_attribution_count": attribution_counts.get("direct", 0),
        "plausible_attribution_count": attribution_counts.get("plausible", 0),
        "first_change_timestamp": first_timestamp(observations),
        "source_file": display_path(path),
    }


def build_rows(events_dir: pathlib.Path = EVENTS_DIR) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    l0_queries = l0_query_index()
    for path, event in load_events(events_dir):
        for layer in LAYER_ORDER:
            rows.append(row_for_layer(path, event, layer, l0_queries))
    return rows


def write_csv(path: pathlib.Path, rows: list[dict[str, Any]]) -> None:
    with path.open("w", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=COLUMNS, lineterminator="\n")
        writer.writeheader()
        for row in rows:
            writer.writerow({key: scalar(row.get(key)) for key in COLUMNS})


def build_markdown(rows: list[dict[str, Any]]) -> list[str]:
    meta = load_meta()
    admitted = [row for row in rows if row["status"] == "admitted"]
    layer_counts = collections.defaultdict(collections.Counter)
    for row in admitted:
        layer_counts[row["layer"]][row["denominator_class"]] += 1

    lines = [
        "# Coverage matrix",
        "",
        f"Dataset snapshot: v{meta.get('dataset_version') or '?'} · "
        f"cutoff `{meta.get('cutoff_date') or 'n/a'}` · "
        f"commit `{meta.get('source_commit') or 'n/a'}` · "
        f"generated `{now_utc_iso()}`",
        "",
        "One row per event-layer pair. This is the explicit denominator surface: "
        "`measured_rate_denominator` rows can support conditional rates; "
        "`observability_gap`, `named_partial_only_no_conditional_rate`, and "
        "`descriptive_only_structural_circularity_v0_1` rows cannot.",
        "",
        "## Admitted-event denominator classes by layer",
        "",
        "| layer | measured rate denominator | partial sensitivity | named partial only | structural descriptive only | observability gap | not applicable |",
        "| --- | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for layer in LAYER_ORDER:
        counts = layer_counts[layer]
        lines.append(
            f"| `{layer}` | "
            f"{counts.get('measured_rate_denominator', 0)} | "
            f"{counts.get('partial_sensitivity_denominator', 0)} | "
            f"{counts.get('named_partial_only_no_conditional_rate', 0)} | "
            f"{counts.get('descriptive_only_structural_circularity_v0_1', 0)} | "
            f"{counts.get('observability_gap', 0)} | "
            f"{counts.get('not_applicable', 0)} |"
        )
    lines.extend([
        "",
        "Phrasing lock: this matrix reports measurement eligibility, not censorship absence. "
        "A layer with `observability_gap` is unmeasured under the frame.",
        "`denominator_reason` and `denominator_artifact` in the CSV/JSON explain why a row is or is not rate-eligible.",
    ])
    return lines


def write_outputs(out_dir: pathlib.Path, rows: list[dict[str, Any]]) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    write_csv(out_dir / "coverage_matrix.csv", rows)
    payload = {
        "meta": {
            "generated_at": now_utc_iso(),
            "generator": {
                "script": "scripts/build_coverage_matrix.py",
                "version": GENERATOR_VERSION,
                "python": reproducible_python(),
            },
            "dataset_snapshot": load_meta(),
            "sampling_frame": str(SAMPLING_FRAME.relative_to(REPO_ROOT)),
        },
        "rows": rows,
    }
    (out_dir / "coverage_matrix.json").write_text(
        json.dumps(payload, indent=2, sort_keys=True, default=json_default) + "\n"
    )
    (out_dir / "coverage_matrix.md").write_text("\n".join(build_markdown(rows)).rstrip() + "\n")


def main() -> int:
    args = parse_args()
    rows = build_rows(pathlib.Path(args.events_dir))
    out_dir = pathlib.Path(args.out_dir)
    write_outputs(out_dir, rows)
    print(f"[build_coverage_matrix] wrote {len(rows)} event-layer rows to {display_path(out_dir)}/")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
