#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Build the 2008+ source-frame monthly discovery ledger.

The ledger is a discovery artifact, not a paper denominator. It records one
row per declared source frame per month from the sampling-frame historical
start through the current dataset cutoff, with empty months retained as
`pending` until a triage manifest records actual search status.
"""
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
from _dataset_meta import load_meta, now_utc_iso, repo_relative_path, reproducible_python  # noqa: E402
from build_trigger_registry import (  # noqa: E402
    display_path,
    infer_analysis_use,
    infer_source_frame_id,
    infer_temporal_tier,
    load_candidate_rows,
    load_event_rows,
    load_yaml,
    parse_year_month,
)


REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent
EVENTS_DIR = REPO_ROOT / "events"
CANDIDATE_DIR = REPO_ROOT / "candidate_triggers"
FRAME_PATH = REPO_ROOT / "sampling" / "frame.yaml"
TRIAGE_DIR = REPO_ROOT / "sources" / "source_frame_triage"
DEFAULT_OUT_DIR = REPO_ROOT / "analysis" / "temporal_ledger"
TRIGGER_REGISTRY_CSV = REPO_ROOT / "analysis" / "trigger_registry" / "trigger_registry.csv"

GENERATOR_VERSION = "0.1.0"

LEDGER_STATUSES = {
    "searched_no_candidate",
    "candidate_found",
    "not_applicable_pre_market",
    "source_unavailable",
    "pending",
}

CSV_COLUMNS = [
    "source_frame_id",
    "discovery_month",
    "temporal_tier",
    "analysis_use",
    "ledger_status",
    "event_ids",
    "candidate_ids",
    "promoted_event_ids",
    "triage_rows",
    "source_files",
    "notes",
]

YEARLY_COLUMNS = [
    "year",
    "temporal_tier",
    "months_covered",
    "source_frame_months",
    "candidate_found_months",
    "pending_months",
    "searched_no_candidate_months",
    "not_applicable_pre_market_months",
    "source_unavailable_months",
    "registry_raw_rows",
    "distinct_in_frame_triggers",
    "admitted_events",
    "observation_closed_events",
    "candidate_stubs",
    "screened_rows",
    "next_action",
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build monthly source-frame discovery ledger.")
    parser.add_argument("--events-dir", default=str(EVENTS_DIR))
    parser.add_argument("--candidate-dir", default=str(CANDIDATE_DIR))
    parser.add_argument("--frame", default=str(FRAME_PATH))
    parser.add_argument("--triage-dir", default=str(TRIAGE_DIR))
    parser.add_argument("--out-dir", default=str(DEFAULT_OUT_DIR))
    return parser.parse_args()


def as_date(value: Any) -> date | None:
    if isinstance(value, datetime):
        return value.date()
    if isinstance(value, date):
        return value
    if not value:
        return None
    text = str(value)
    try:
        return datetime.fromisoformat(text[:10]).date()
    except ValueError:
        return None


def parse_month(value: Any) -> tuple[int | None, int | None, str]:
    if isinstance(value, datetime):
        return value.year, value.month, f"{value.year:04d}-{value.month:02d}"
    if isinstance(value, date):
        return value.year, value.month, f"{value.year:04d}-{value.month:02d}"
    _year, month_text = parse_year_month(value)
    if not month_text:
        return None, None, ""
    return _year, int(month_text[5:7]), month_text


def month_range(start: date, end: date) -> list[str]:
    year = start.year
    month = start.month
    months: list[str] = []
    while (year, month) <= (end.year, end.month):
        months.append(f"{year:04d}-{month:02d}")
        month += 1
        if month == 13:
            year += 1
            month = 1
    return months


def tier_for_month(frame: dict[str, Any], discovery_month: str) -> str:
    year = int(discovery_month[:4])
    month = int(discovery_month[5:7])
    probe = date(year, month, 1)
    for tier, spec in (frame.get("temporal_tiers") or {}).items():
        if not isinstance(spec, dict):
            continue
        bounds = spec.get("date_range") or []
        if len(bounds) != 2:
            continue
        start = as_date(bounds[0])
        end = as_date(bounds[1])
        if start and end and start <= probe <= end:
            return str(tier)
    return ""


def analysis_use_for_tier(frame: dict[str, Any], temporal_tier: str) -> str:
    spec = (frame.get("temporal_tiers") or {}).get(temporal_tier) or {}
    return str(spec.get("analysis_use") or "")


def default_status_for_tier(frame: dict[str, Any], temporal_tier: str) -> str:
    spec = (frame.get("temporal_tiers") or {}).get(temporal_tier) or {}
    return str(spec.get("default_month_status") or "pending")


def source_frames(frame: dict[str, Any]) -> list[str]:
    ids = [
        str(spec.get("source_frame_id") or "")
        for spec in (frame.get("source_frames") or {}).values()
        if isinstance(spec, dict) and spec.get("source_frame_id")
    ]
    return sorted(set(ids))


def source_frame_first_available_date(
    frame: dict[str, Any], source_frame_id: str
) -> str | None:
    """Return the ISO date string `source_artifact_first_available_date` for
    the named source-frame, or None if the field is missing.

    Added 2026-05-16 per Agent A F1 from the 4-agent temporal-ledger
    review: pre-artifact months render as `source_unavailable`, not
    `pending`, so the ledger does not claim searched-but-empty
    coverage on a source that nobody could search.
    """
    for spec in (frame.get("source_frames") or {}).values():
        if not isinstance(spec, dict):
            continue
        if str(spec.get("source_frame_id") or "") != source_frame_id:
            continue
        val = spec.get("source_artifact_first_available_date")
        return str(val) if val else None
    return None


def empty_row(frame: dict[str, Any], source_frame_id: str, discovery_month: str) -> dict[str, str]:
    temporal_tier = tier_for_month(frame, discovery_month)
    # Default status from tier; override to `source_unavailable` if
    # the discovery_month precedes the source-frame's
    # `source_artifact_first_available_date` (Agent A F1 fix).
    status = default_status_for_tier(frame, temporal_tier)
    first_avail = source_frame_first_available_date(frame, source_frame_id)
    if first_avail and discovery_month < first_avail[:7]:
        status = "source_unavailable"
    return {
        "source_frame_id": source_frame_id,
        "discovery_month": discovery_month,
        "temporal_tier": temporal_tier,
        "analysis_use": analysis_use_for_tier(frame, temporal_tier),
        "ledger_status": status,
        "event_ids": "",
        "candidate_ids": "",
        "promoted_event_ids": "",
        "triage_rows": "0",
        "source_files": "",
        "notes": "",
    }


def append_csv_value(row: dict[str, str], column: str, value: Any) -> None:
    text = str(value or "").strip()
    if not text:
        return
    values = [part for part in row.get(column, "").split(",") if part]
    if text not in values:
        values.append(text)
    row[column] = ",".join(values)


def append_note(row: dict[str, str], note: Any) -> None:
    text = str(note or "").strip()
    if not text:
        return
    notes = [part for part in row.get("notes", "").split(" | ") if part]
    if text not in notes:
        notes.append(text)
    row["notes"] = " | ".join(notes)


def promote_status(current: str, candidate: str) -> str:
    precedence = {
        "pending": 0,
        "not_applicable_pre_market": 1,
        "searched_no_candidate": 2,
        "source_unavailable": 3,
        "candidate_found": 4,
    }
    if candidate not in LEDGER_STATUSES:
        return current
    return candidate if precedence[candidate] >= precedence.get(current, 0) else current


def apply_event_rows(ledger: dict[tuple[str, str], dict[str, str]], rows: list[dict[str, str]]) -> None:
    for source in rows:
        source_frame_id = source.get("source_frame_id") or ""
        discovery_month = source.get("discovery_month") or ""
        if not source_frame_id or not discovery_month:
            continue
        row = ledger.get((source_frame_id, discovery_month))
        if row is None:
            continue
        row["ledger_status"] = promote_status(row["ledger_status"], "candidate_found")
        append_csv_value(row, "event_ids", source.get("event_id"))
        append_csv_value(row, "source_files", source.get("source_file"))


def apply_candidate_rows(ledger: dict[tuple[str, str], dict[str, str]], rows: list[dict[str, str]]) -> None:
    for source in rows:
        source_frame_id = source.get("source_frame_id") or ""
        discovery_month = source.get("discovery_month") or ""
        if not source_frame_id or not discovery_month:
            continue
        row = ledger.get((source_frame_id, discovery_month))
        if row is None:
            continue
        row["ledger_status"] = promote_status(row["ledger_status"], "candidate_found")
        append_csv_value(row, "candidate_ids", source.get("trigger_id"))
        append_csv_value(row, "promoted_event_ids", source.get("event_id"))
        append_csv_value(row, "source_files", source.get("source_file"))
        append_note(row, source.get("triage_notes"))


def load_triage_manifest_rows(triage_dir: pathlib.Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    if not triage_dir.exists():
        return rows
    for path in sorted(triage_dir.glob("*.csv")):
        with path.open(newline="") as fh:
            for raw in csv.DictReader(fh):
                raw["_source_file"] = display_path(path)
                rows.append(raw)
    for path in sorted(triage_dir.glob("*.json")):
        payload = json.loads(path.read_text())
        raw_rows = payload.get("rows") if isinstance(payload, dict) else payload
        if not isinstance(raw_rows, list):
            continue
        for raw in raw_rows:
            if isinstance(raw, dict):
                item = dict(raw)
                item["_source_file"] = display_path(path)
                rows.append(item)
    return rows


def load_csv_rows(path: pathlib.Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open(newline="") as fh:
        return list(csv.DictReader(fh))


def triage_status(raw: dict[str, Any]) -> str:
    if raw.get("candidate_id") or raw.get("promoted_event_id"):
        return "candidate_found"
    status = str(raw.get("ledger_status") or raw.get("screening_status") or "").strip()
    if status in LEDGER_STATUSES:
        return status
    if status in {"screened_no_extractor_target", "rejected_out_of_scope", "screened_out"}:
        return "searched_no_candidate"
    return "pending"


def apply_triage_rows(ledger: dict[tuple[str, str], dict[str, str]], rows: list[dict[str, Any]]) -> None:
    for raw in rows:
        source_frame_id = str(raw.get("source_frame_id") or "").strip()
        discovery_month = str(raw.get("discovery_month") or "").strip()
        if not discovery_month and raw.get("trigger_date"):
            _year, _month, discovery_month = parse_month(raw.get("trigger_date"))
        if not source_frame_id or not discovery_month:
            continue
        row = ledger.get((source_frame_id, discovery_month))
        if row is None:
            continue
        status = triage_status(raw)
        row["ledger_status"] = promote_status(row["ledger_status"], status)
        row["triage_rows"] = str(int(row.get("triage_rows") or 0) + 1)
        append_csv_value(row, "candidate_ids", raw.get("candidate_id"))
        append_csv_value(row, "promoted_event_ids", raw.get("promoted_event_id"))
        append_csv_value(row, "source_files", raw.get("_source_file"))
        append_note(row, raw.get("screening_reason") or raw.get("notes"))


def build_ledger(
    events_dir: pathlib.Path = EVENTS_DIR,
    candidate_dir: pathlib.Path = CANDIDATE_DIR,
    frame_path: pathlib.Path = FRAME_PATH,
    triage_dir: pathlib.Path = TRIAGE_DIR,
) -> tuple[dict[str, Any], list[dict[str, str]]]:
    frame = load_yaml(frame_path)
    meta = load_meta()
    snapshot = frame.get("snapshot_scope") or {}
    start = as_date(snapshot.get("historical_start")) or date(2008, 1, 1)
    cutoff = as_date(meta.get("cutoff_date")) or date.today()
    months = month_range(start, cutoff)
    source_frame_ids = source_frames(frame)
    ledger = {
        (source_frame_id, discovery_month): empty_row(frame, source_frame_id, discovery_month)
        for source_frame_id in source_frame_ids
        for discovery_month in months
    }

    event_rows = load_event_rows(events_dir)
    for row in event_rows:
        if not row.get("source_frame_id"):
            row["source_frame_id"] = infer_source_frame_id(load_yaml(events_dir / pathlib.Path(row["source_file"]).name))
        if not row.get("temporal_tier"):
            row["temporal_tier"] = infer_temporal_tier(row)
        if not row.get("analysis_use"):
            row["analysis_use"] = infer_analysis_use(row, row.get("temporal_tier") or "")
    apply_event_rows(ledger, event_rows)
    apply_candidate_rows(ledger, load_candidate_rows(candidate_dir))
    apply_triage_rows(ledger, load_triage_manifest_rows(triage_dir))

    rows = [ledger[key] for key in sorted(ledger)]
    return frame, rows


def write_outputs(
    out_dir: pathlib.Path,
    frame: dict[str, Any],
    rows: list[dict[str, str]],
    frame_path: pathlib.Path = FRAME_PATH,
) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    csv_path = out_dir / "monthly_discovery_ledger.csv"
    with csv_path.open("w", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=CSV_COLUMNS, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)

    status_counts = collections.Counter(row["ledger_status"] for row in rows)
    tier_counts = collections.Counter(row["temporal_tier"] for row in rows)
    meta = {
        "generated_at": now_utc_iso(),
        "generator": {
            "script": "scripts/build_temporal_discovery_ledger.py",
            "version": GENERATOR_VERSION,
            "python": reproducible_python(),
        },
        "dataset_snapshot": load_meta(),
        "sampling_frame": repo_relative_path(frame_path),
        "source_frame_count": len(source_frames(frame)),
        "row_count": len(rows),
        "status_counts": dict(sorted(status_counts.items())),
        "temporal_tier_counts": dict(sorted(tier_counts.items())),
    }
    (out_dir / "monthly_discovery_ledger.json").write_text(
        json.dumps({"meta": meta, "rows": rows}, indent=2, sort_keys=True) + "\n"
    )
    (out_dir / "monthly_discovery_ledger.md").write_text(build_markdown(meta, rows))

    yearly_rows = build_yearly_rows(rows, load_csv_rows(TRIGGER_REGISTRY_CSV))
    yearly_meta = {
        **meta,
        "row_count": len(yearly_rows),
        "source": "analysis/temporal_ledger/monthly_discovery_ledger.csv",
    }
    with (out_dir / "yearly_collection_plan.csv").open("w", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=YEARLY_COLUMNS, lineterminator="\n")
        writer.writeheader()
        writer.writerows(yearly_rows)
    (out_dir / "yearly_collection_plan.json").write_text(
        json.dumps({"meta": yearly_meta, "rows": yearly_rows}, indent=2, sort_keys=True) + "\n"
    )
    (out_dir / "yearly_collection_plan.md").write_text(
        build_yearly_markdown(yearly_meta, yearly_rows)
    )


def build_markdown(meta: dict[str, Any], rows: list[dict[str, str]]) -> str:
    status_counts = collections.Counter(row["ledger_status"] for row in rows)
    tier_counts = collections.Counter(row["temporal_tier"] for row in rows)
    candidate_rows = sum(1 for row in rows if row["ledger_status"] == "candidate_found")
    lines = [
        "# Monthly Discovery Ledger",
        "",
        f"Dataset snapshot: v{(meta.get('dataset_snapshot') or {}).get('dataset_version') or '?'} · "
        f"cutoff `{(meta.get('dataset_snapshot') or {}).get('cutoff_date') or 'n/a'}` · "
        f"generated `{meta.get('generated_at')}`",
        "",
        "This ledger covers every declared source frame for every month from "
        "`sampling/frame.yaml::snapshot_scope.historical_start` through the "
        "dataset cutoff. A `pending` row means the month has not yet been "
        "triaged; it is not evidence that no candidate exists.",
        "",
        f"- Source frames: {meta.get('source_frame_count')}",
        f"- Monthly rows: {len(rows)}",
        f"- Rows with candidates/events: {candidate_rows}",
        "",
        "## Status Distribution",
        "",
        "| ledger_status | rows |",
        "| --- | ---: |",
    ]
    for status, count in sorted(status_counts.items()):
        lines.append(f"| `{status}` | {count} |")
    lines.extend([
        "",
        "## Temporal Tier Distribution",
        "",
        "| temporal_tier | rows |",
        "| --- | ---: |",
    ])
    for tier, count in sorted(tier_counts.items()):
        lines.append(f"| `{tier}` | {count} |")
    lines.extend([
        "",
        "## Contract",
        "",
        "- `discovery_only_2008_2012` rows are discovery-ledger rows by default.",
        "- `historical_baseline_2013_2016` rows may become full event YAMLs, but stay out of 2017+ comparable denominators unless a claim explicitly separates the historical baseline.",
        "- `comparable_main_2017_present` is the only default tier for current cross-layer comparable analysis.",
        "- Empty months remain visible as `pending`, `searched_no_candidate`, `not_applicable_pre_market`, or `source_unavailable` rather than disappearing.",
    ])
    return "\n".join(lines).rstrip() + "\n"


def choose_next_action(status_counts: collections.Counter[str], registry_counts: collections.Counter[str]) -> str:
    if status_counts.get("pending", 0):
        return "triage pending source-frame months"
    if registry_counts.get("candidate", 0) or registry_counts.get("observation_closed", 0):
        return "promote/review candidate and observation_closed rows"
    if status_counts.get("source_unavailable", 0):
        return "resolve source-unavailable receipts"
    return "maintain exhausted-year receipts"


def build_yearly_rows(
    ledger_rows: list[dict[str, str]],
    registry_rows: list[dict[str, str]],
) -> list[dict[str, str]]:
    ledger_by_year: dict[str, list[dict[str, str]]] = collections.defaultdict(list)
    for row in ledger_rows:
        year = (row.get("discovery_month") or "")[:4]
        if year:
            ledger_by_year[year].append(row)

    registry_by_year: dict[str, list[dict[str, str]]] = collections.defaultdict(list)
    for row in registry_rows:
        year = (row.get("discovery_month") or row.get("trigger_timestamp") or "")[:4]
        if year:
            registry_by_year[year].append(row)

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
    rows: list[dict[str, str]] = []
    for year in sorted(set(ledger_by_year) | set(registry_by_year)):
        ledger = ledger_by_year.get(year, [])
        registry = registry_by_year.get(year, [])
        status_counts = collections.Counter(row.get("ledger_status") or "" for row in ledger)
        registry_counts = collections.Counter(row.get("registry_status") or "" for row in registry)
        tier_counts = collections.Counter(row.get("temporal_tier") or "" for row in ledger)
        distinct_in_frame = {
            row.get("frame_unit_id") or row.get("trigger_id") or ""
            for row in registry
            if row.get("registry_status") in in_frame_statuses
            and row.get("registry_status") != "promoted_to_event"
        }
        distinct_in_frame.discard("")
        rows.append(
            {
                "year": year,
                "temporal_tier": tier_counts.most_common(1)[0][0] if tier_counts else "",
                "months_covered": str(len({row.get("discovery_month") for row in ledger})),
                "source_frame_months": str(len(ledger)),
                "candidate_found_months": str(status_counts.get("candidate_found", 0)),
                "pending_months": str(status_counts.get("pending", 0)),
                "searched_no_candidate_months": str(status_counts.get("searched_no_candidate", 0)),
                "not_applicable_pre_market_months": str(status_counts.get("not_applicable_pre_market", 0)),
                "source_unavailable_months": str(status_counts.get("source_unavailable", 0)),
                "registry_raw_rows": str(len(registry)),
                "distinct_in_frame_triggers": str(len(distinct_in_frame)),
                "admitted_events": str(registry_counts.get("admitted", 0)),
                "observation_closed_events": str(registry_counts.get("observation_closed", 0)),
                "candidate_stubs": str(registry_counts.get("candidate", 0)),
                "screened_rows": str(registry_counts.get("screened_no_extractor_target", 0)),
                "next_action": choose_next_action(status_counts, registry_counts),
            }
        )
    return rows


def build_yearly_markdown(meta: dict[str, Any], rows: list[dict[str, str]]) -> str:
    lines = [
        "# Yearly Collection Plan",
        "",
        f"Dataset snapshot: v{(meta.get('dataset_snapshot') or {}).get('dataset_version') or '?'} · "
        f"cutoff `{(meta.get('dataset_snapshot') or {}).get('cutoff_date') or 'n/a'}` · "
        f"generated `{meta.get('generated_at')}`",
        "",
        "This is the year-level control surface for the 2008+ tiered frame. "
        "It is derived from the monthly discovery ledger and trigger registry; "
        "it is not a paper denominator.",
        "",
        "| year | tier | source-frame months | candidate-found months | pending months | registry rows | in-frame triggers | admitted | observation_closed | candidates | screened | next action |",
        "| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |",
    ]
    for row in rows:
        lines.append(
            f"| {row['year']} | `{row['temporal_tier']}` | "
            f"{row['source_frame_months']} | {row['candidate_found_months']} | "
            f"{row['pending_months']} | {row['registry_raw_rows']} | "
            f"{row['distinct_in_frame_triggers']} | {row['admitted_events']} | "
            f"{row['observation_closed_events']} | {row['candidate_stubs']} | "
            f"{row['screened_rows']} | {row['next_action']} |"
        )
    lines.extend([
        "",
        "## Use",
        "",
        "- Work years top-down from oldest unresolved tier unless a current event requires immediate capture.",
        "- Do not turn a year from `pending` into `searched_no_candidate` without a source-frame triage manifest row.",
        "- Historical-baseline rows can become full YAML events, but stay out of 2017+ comparable denominators.",
    ])
    return "\n".join(lines).rstrip() + "\n"


def main() -> int:
    args = parse_args()
    frame, rows = build_ledger(
        events_dir=pathlib.Path(args.events_dir),
        candidate_dir=pathlib.Path(args.candidate_dir),
        frame_path=pathlib.Path(args.frame),
        triage_dir=pathlib.Path(args.triage_dir),
    )
    out_dir = pathlib.Path(args.out_dir)
    write_outputs(out_dir, frame, rows, pathlib.Path(args.frame))
    print(f"[temporal-ledger] wrote {len(rows)} rows to {repo_relative_path(out_dir)}/")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
