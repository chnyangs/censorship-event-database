#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Build the pre-admission trigger registry from events and candidate stubs."""
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
CANDIDATE_DIR = REPO_ROOT / "candidate_triggers"
FRAME_PATH = REPO_ROOT / "sampling" / "frame.yaml"
DEFAULT_OUT_DIR = REPO_ROOT / "analysis" / "trigger_registry"

GENERATOR_VERSION = "0.1.0"

REGISTRY_COLUMNS = [
    "trigger_id",
    "frame_unit_id",
    "source_frame_id",
    "source_type",
    "registry_status",
    "event_status",
    "event_id",
    "research_stratum",
    "trigger_type",
    "trigger_actor",
    "trigger_timestamp",
    "trigger_timestamp_precision",
    "jurisdiction",
    "target_kind",
    "target_chains",
    "coverage_measured_layers",
    "coverage_partial_layers",
    "coverage_not_measured_layers",
    "coverage_not_applicable_layers",
    "observed_change_layers",
    "empirical_shape",
    "admission_tier",
    "source_file",
    "triage_notes",
]

LAYER_ORDER = [
    "l0_network",
    "l1_consensus",
    "l3_rpc",
    "l4_frontend",
    "asset_onchain",
    "offramp_cex",
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build trigger registry artifacts.")
    parser.add_argument("--events-dir", default=str(EVENTS_DIR))
    parser.add_argument("--candidate-dir", default=str(CANDIDATE_DIR))
    parser.add_argument("--frame", default=str(FRAME_PATH))
    parser.add_argument("--out-dir", default=str(DEFAULT_OUT_DIR))
    return parser.parse_args()


def load_yaml(path: pathlib.Path) -> dict[str, Any]:
    raw = yaml.safe_load(path.read_text())
    if not isinstance(raw, dict):
        raise SystemExit(f"{path}: expected YAML object")
    return raw


def json_default(value: Any) -> str:
    if isinstance(value, (date, datetime)):
        return value.isoformat()
    return str(value)


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


def layers_by_status(event: dict[str, Any], status: str) -> list[str]:
    return sorted(
        coverage.get("layer", "")
        for coverage in event.get("coverage", [])
        if coverage.get("status") == status and coverage.get("layer")
    )


def observed_change_layers(event: dict[str, Any]) -> list[str]:
    return sorted(
        {
            observation.get("layer", "")
            for observation in event.get("observations", [])
            if observation.get("observation_kind") == "observed_change"
            and observation.get("layer")
        }
    )


def infer_source_frame_id(candidate: dict[str, Any]) -> str:
    value = candidate.get("source_frame_id")
    if value:
        return scalar(value)
    extraction = candidate.get("extraction") or {}
    source = str(extraction.get("source") or "")
    if "ofac-recent-actions-triage.json" in source:
        return "ofac_recent_actions_crypto_2017_2026"
    return ""


def frame_unit_id(trigger_id: str, source_frame_id: str, target: dict[str, Any]) -> str:
    target_kind = scalar(target.get("kind"))
    target_id = scalar(target.get("id") or target.get("name") or target.get("protocol") or "")
    if not target_id and target.get("addresses"):
        addresses = target.get("addresses")
        if isinstance(addresses, list) and addresses:
            target_id = f"address_set:{len(addresses)}:{scalar(addresses[0])}"
    base = source_frame_id or "legacy_v0_1_event_yaml"
    return f"{base}:{trigger_id}:{target_kind}:{target_id}".rstrip(":")


def event_row(event: dict[str, Any], source_file: str) -> dict[str, str]:
    trigger = event.get("trigger") or {}
    target = event.get("target") or {}
    trigger_id = scalar(event.get("id"))
    source_frame_id = "legacy_v0_1_event_yaml"
    return {
        "trigger_id": trigger_id,
        "frame_unit_id": frame_unit_id(trigger_id, source_frame_id, target),
        "source_frame_id": source_frame_id,
        "source_type": "event_yaml",
        "registry_status": scalar(event.get("status")),
        "event_status": scalar(event.get("status")),
        "event_id": scalar(event.get("id")),
        "research_stratum": scalar(event.get("research_stratum")),
        "trigger_type": scalar(trigger.get("type")),
        "trigger_actor": scalar(trigger.get("actor")),
        "trigger_timestamp": scalar(trigger.get("timestamp")),
        "trigger_timestamp_precision": scalar(trigger.get("timestamp_precision")),
        "jurisdiction": csv_join(event.get("jurisdiction")),
        "target_kind": scalar(target.get("kind")),
        "target_chains": csv_join(target.get("chains")),
        "coverage_measured_layers": csv_join(layers_by_status(event, "measured")),
        "coverage_partial_layers": csv_join(layers_by_status(event, "partially_measured")),
        "coverage_not_measured_layers": csv_join(layers_by_status(event, "not_measured")),
        "coverage_not_applicable_layers": csv_join(layers_by_status(event, "not_applicable")),
        "observed_change_layers": csv_join(observed_change_layers(event)),
        "empirical_shape": scalar(event.get("empirical_shape")),
        "admission_tier": scalar(event.get("admission_tier")),
        "source_file": source_file,
        "triage_notes": scalar(event.get("scoped_claim") or event.get("analysis_notes", "")).split("\n", 1)[0],
    }


def candidate_row(candidate: dict[str, Any], source_file: str, rejected_dir: bool = False) -> dict[str, str]:
    trigger = candidate.get("trigger") or {}
    target = candidate.get("target") or {}
    status = candidate.get("registry_status") or candidate.get("status")
    if rejected_dir and not status:
        status = "rejected_out_of_scope"
    status = status or "candidate"
    trigger_id = candidate.get("id") or pathlib.Path(source_file).stem
    source_frame_id = infer_source_frame_id(candidate)
    return {
        "trigger_id": scalar(trigger_id),
        "frame_unit_id": frame_unit_id(scalar(trigger_id), source_frame_id, target),
        "source_frame_id": source_frame_id,
        "source_type": "candidate_trigger",
        "registry_status": scalar(status),
        "event_status": "",
        "event_id": csv_join(candidate.get("promoted_event_id") or candidate.get("event_id")),
        "research_stratum": scalar(candidate.get("research_stratum")),
        "trigger_type": scalar(trigger.get("type")),
        "trigger_actor": scalar(trigger.get("actor")),
        "trigger_timestamp": scalar(trigger.get("timestamp")),
        "trigger_timestamp_precision": scalar(trigger.get("timestamp_precision")),
        "jurisdiction": csv_join(candidate.get("jurisdiction")),
        "target_kind": scalar(target.get("kind")),
        "target_chains": csv_join(target.get("chains")),
        "coverage_measured_layers": "",
        "coverage_partial_layers": "",
        "coverage_not_measured_layers": "",
        "coverage_not_applicable_layers": "",
        "observed_change_layers": "",
        "empirical_shape": "",
        "admission_tier": "",
        "source_file": source_file,
        "triage_notes": scalar(candidate.get("triage_notes") or candidate.get("notes")),
    }


def load_event_rows(events_dir: pathlib.Path) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for path in sorted(events_dir.glob("*.yaml")):
        if path.name == "TEMPLATE.yaml" or path.name.startswith("_"):
            continue
        rows.append(event_row(load_yaml(path), display_path(path)))
    return rows


def load_candidate_rows(candidate_dir: pathlib.Path) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    if not candidate_dir.exists():
        return rows
    for path in sorted(candidate_dir.glob("*.yaml")):
        if path.name.startswith("_"):
            continue
        rows.append(candidate_row(load_yaml(path), display_path(path)))
    rejected = candidate_dir / "rejected"
    if rejected.exists():
        for path in sorted(rejected.glob("*.yaml")):
            if path.name.startswith("_"):
                continue
            rows.append(
                candidate_row(
                    load_yaml(path),
                    display_path(path),
                    rejected_dir=True,
                )
            )
    return rows


def validate_rows(rows: list[dict[str, str]], frame: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    allowed_statuses = set(frame.get("trigger_registry_statuses") or [])
    allowed_strata = set((frame.get("strata") or {}).keys())
    allowed_target_kinds = set(frame.get("target_kinds") or [])

    seen: set[str] = set()
    event_ids = {
        row["event_id"]
        for row in rows
        if row.get("source_type") == "event_yaml" and row.get("event_id")
    }
    for row in rows:
        trigger_id = row["trigger_id"]
        if not trigger_id:
            errors.append(f"{row['source_file']}: missing trigger_id")
        elif trigger_id in seen:
            errors.append(f"duplicate trigger_id={trigger_id}")
        seen.add(trigger_id)

        status = row["registry_status"]
        if status and allowed_statuses and status not in allowed_statuses:
            errors.append(f"{trigger_id}: registry_status={status} not in sampling frame")

        stratum = row["research_stratum"]
        if stratum and allowed_strata and stratum not in allowed_strata:
            errors.append(f"{trigger_id}: research_stratum={stratum} not in sampling frame")

        target_kind = row["target_kind"]
        if target_kind and allowed_target_kinds and target_kind not in allowed_target_kinds:
            errors.append(f"{trigger_id}: target_kind={target_kind} not in sampling frame")

        if row.get("source_type") == "candidate_trigger" and status == "promoted_to_event":
            linked_ids = [value for value in row.get("event_id", "").split(",") if value]
            if not linked_ids:
                errors.append(f"{trigger_id}: promoted_to_event requires promoted_event_id")
            missing = sorted(set(linked_ids) - event_ids)
            if missing:
                errors.append(
                    f"{trigger_id}: promoted_event_id references missing event(s): "
                    + ", ".join(missing)
                )

    return errors


def gap(value: int, target: int) -> int:
    return max(target - value, 0)


def build_summary(frame: dict[str, Any], rows: list[dict[str, str]]) -> list[str]:
    meta = load_meta()
    status_counts = collections.Counter(row["registry_status"] for row in rows)
    in_frame_statuses = {
        "admitted",
        "draft",
        "observation_active",
        "observation_closed",
        "candidate",
        "draft_needs_evidence",
        "deferred",
        "not_measurable",
    }
    in_frame_rows = [
        row
        for row in rows
        if row["registry_status"] in in_frame_statuses
        and row["registry_status"] != "promoted_to_event"
    ]
    in_frame_by_stratum = collections.Counter(row["research_stratum"] for row in in_frame_rows)
    admitted_by_stratum = collections.Counter(
        row["research_stratum"] for row in rows if row["registry_status"] == "admitted"
    )
    snapshot = frame.get("snapshot_scope") or {}
    admitted_count = status_counts.get("admitted", 0)
    raw_registry_rows = len(rows)
    distinct_in_frame = len({row.get("frame_unit_id") or row["trigger_id"] for row in in_frame_rows})

    lines = [
        "# Trigger registry",
        "",
        f"Dataset snapshot: v{meta.get('dataset_version') or '?'} · "
        f"cutoff `{meta.get('cutoff_date') or 'n/a'}` · "
        f"commit `{meta.get('source_commit') or 'n/a'}` · "
        f"generated `{now_utc_iso()}`",
        "",
        "This is the pre-admission registry surface. It includes every YAML event "
        "plus any candidate trigger stubs under `candidate_triggers/`, so future "
        "case expansion is explicit instead of anecdotal.",
        "",
        "## Snapshot counts",
        "",
        "| count | value | target | gap |",
        "| --- | ---: | ---: | ---: |",
        (
            f"| raw registry rows | {raw_registry_rows} | audit surface | — |"
        ),
        (
            f"| distinct in-frame triggers | {distinct_in_frame} | "
            f"{snapshot.get('candidate_trigger_registry_target_min', 'n/a')}-"
            f"{snapshot.get('candidate_trigger_registry_target_max', 'n/a')} | "
            f"{gap(distinct_in_frame, int(snapshot.get('candidate_trigger_registry_target_min') or 0))} |"
        ),
        (
            f"| admitted events | {admitted_count} | "
            f"{snapshot.get('admitted_event_target_min', 'n/a')}-"
            f"{snapshot.get('admitted_event_target_max', 'n/a')} | "
            f"{gap(admitted_count, int(snapshot.get('admitted_event_target_min') or 0))} |"
        ),
        "",
        "## Status distribution",
        "",
        "| registry_status | count |",
        "| --- | ---: |",
    ]
    for status, count in sorted(status_counts.items()):
        lines.append(f"| `{status}` | {count} |")

    lines.extend([
        "",
        "## Stratum expansion gaps",
        "",
        "| stratum | in-frame triggers | admitted | v0.2 admitted min | admitted gap | v0.2 candidate min | candidate gap |",
        "| --- | ---: | ---: | ---: | ---: | ---: | ---: |",
    ])
    for stratum, spec in (frame.get("strata") or {}).items():
        admitted = admitted_by_stratum.get(stratum, 0)
        all_rows = len({
            row.get("frame_unit_id") or row["trigger_id"]
            for row in in_frame_rows
            if row["research_stratum"] == stratum
        })
        admitted_min = int(spec.get("v0_2_admitted_min") or 0)
        candidate_min = int(spec.get("v0_2_candidate_min") or 0)
        lines.append(
            f"| `{stratum}` | {all_rows} | {admitted} | {admitted_min} | "
            f"{gap(admitted, admitted_min)} | {candidate_min} | {gap(all_rows, candidate_min)} |"
        )

    lines.extend([
        "",
        "## Phrasing lock",
        "",
        "- The registry gap is an expansion backlog, not a paper result.",
        "- Raw registry rows are an audit surface and include promoted duplicates and extractor-screened rows.",
        "- Candidate target gaps are computed from distinct in-frame triggers only.",
        "- Admitted-only paper tables remain the only source for paper-facing event counts.",
        "- Draft, rejected, deferred, screened, and not-measurable triggers are retained to make selection visible.",
    ])
    return lines


def write_outputs(
    out_dir: pathlib.Path,
    frame: dict[str, Any],
    rows: list[dict[str, str]],
    frame_path: pathlib.Path = FRAME_PATH,
) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    csv_path = out_dir / "trigger_registry.csv"
    with csv_path.open("w", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=REGISTRY_COLUMNS, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)

    payload = {
        "meta": {
            "generated_at": now_utc_iso(),
            "generator": {
                "script": "scripts/build_trigger_registry.py",
                "version": GENERATOR_VERSION,
                "python": reproducible_python(),
            },
            "dataset_snapshot": load_meta(),
            "sampling_frame": display_path(frame_path),
        },
        "rows": rows,
    }
    (out_dir / "trigger_registry.json").write_text(
        json.dumps(payload, indent=2, sort_keys=True, default=json_default) + "\n"
    )
    (out_dir / "trigger_registry.md").write_text("\n".join(build_summary(frame, rows)).rstrip() + "\n")


def build_registry(
    events_dir: pathlib.Path = EVENTS_DIR,
    candidate_dir: pathlib.Path = CANDIDATE_DIR,
    frame_path: pathlib.Path = FRAME_PATH,
) -> tuple[dict[str, Any], list[dict[str, str]]]:
    frame = load_yaml(frame_path)
    rows = load_event_rows(events_dir) + load_candidate_rows(candidate_dir)
    rows.sort(key=lambda row: (row["trigger_timestamp"], row["trigger_id"]))
    errors = validate_rows(rows, frame)
    if errors:
        raise SystemExit("[build_trigger_registry] validation failed:\n" + "\n".join(errors))
    return frame, rows


def main() -> int:
    args = parse_args()
    frame, rows = build_registry(
        pathlib.Path(args.events_dir),
        pathlib.Path(args.candidate_dir),
        pathlib.Path(args.frame),
    )
    out_dir = pathlib.Path(args.out_dir)
    write_outputs(out_dir, frame, rows, pathlib.Path(args.frame))
    print(f"[build_trigger_registry] wrote {len(rows)} rows to {display_path(out_dir)}/")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
