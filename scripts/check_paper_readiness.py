#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Paper-readiness checks for the v0.1 measurement-paper surface.

This is intentionally narrower than `scripts/validate.py`: it checks whether
the paper-facing claims, generated paper tables, and audit gates are coherent
enough to cite. It does not stamp `last_human_audit`; human sign-off remains a
separate action.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import pathlib
import re
import subprocess
import sys
from datetime import datetime
from typing import Any

import yaml

from build_dataset import source_input_hash


REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent
EVENTS_DIR = REPO_ROOT / "events"
PAPER_TABLES_DIR = REPO_ROOT / "analysis" / "paper_tables"
DERIVED_DIR = REPO_ROOT / "derived"
PAPER_CLAIMS = REPO_ROOT / "docs" / "paper_claims.md"
DATASET_META = REPO_ROOT / "dataset.meta.json"
DATASET_JSON = REPO_ROOT / "dataset.json"
DATASET_CSV = REPO_ROOT / "dataset.csv"
CITATION_CFF = REPO_ROOT / "CITATION.cff"
IRR_REPORT = REPO_ROOT / "analysis" / "inter_rater" / "kappa_report.json"
EVIDENCE_TIER_IRR_REPORT = REPO_ROOT / "analysis" / "evidence_tier_irr_report_2026_05_31.json"
SAMPLING_FRAME = REPO_ROOT / "sampling" / "frame.yaml"
TRIGGER_REGISTRY_DIR = REPO_ROOT / "analysis" / "trigger_registry"
TEMPORAL_LEDGER_DIR = REPO_ROOT / "analysis" / "temporal_ledger"
SOURCE_MANIFEST_PREFIX = REPO_ROOT / "sources" / "source_manifest"

HOUR_PRECISION_VALUES = {"second", "minute", "hour", "hour_range"}
DAY_PRECISION_VALUES = {"day", "date", "week"}

REQUIRED_TABLES = [
    "README.md",
    ".meta.json",
    "table1_case_roles.csv",
    "table1_case_roles.md",
    "table2_layer_observability.md",
    "table3_archetype_stratum.md",
    "table4_latency_by_precision.csv",
    "table4_latency_by_precision.md",
    "table5_target_enumeration.md",
    "table6_null_denominator.csv",
    "table6_null_denominator.md",
    "table7_jurisdiction_distribution.md",
]

# Derived artifacts that paper_claims.md cites by name; these must
# exist after `make regenerate` so the reproduction path stays
# consistent with the paper claims.
REQUIRED_DERIVED = [
    "admission_sensitivity.md",
    "admission_sensitivity.csv",
    "admission_sensitivity.meta.json",
    "action_registry.md",
    "action_registry.csv",
    "action_registry.json",
    "action_registry.meta.json",
    "coverage_matrix.md",
    "coverage_matrix.csv",
    "coverage_matrix.json",
    "l0_coverage_summary.md",
    "l0_coverage_summary.csv",
    "l0_coverage_summary.json",
    "l3_provider_census.md",
    "l3_provider_census.csv",
    "l3_provider_census.json",
    "l3_provider_census.meta.json",
    "jurisdiction_distribution.md",
    "jurisdiction_distribution.csv",
]

REQUIRED_TRIGGER_REGISTRY = [
    "trigger_registry.csv",
    "trigger_registry.json",
    "trigger_registry.md",
]

REQUIRED_TEMPORAL_LEDGER = [
    "monthly_discovery_ledger.csv",
    "monthly_discovery_ledger.json",
    "monthly_discovery_ledger.md",
    "yearly_collection_plan.csv",
    "yearly_collection_plan.json",
    "yearly_collection_plan.md",
]

REQUIRED_SOURCE_MANIFEST = [
    "sources/source_manifest.csv",
    "sources/source_manifest.json",
    "sources/source_manifest.md",
    "sources/source_manifest.meta.json",
]

TEMPORAL_LEDGER_STATUSES = {
    "searched_no_candidate",
    "candidate_found",
    "not_applicable_pre_market",
    "source_unavailable",
    "pending",
}

EVIDENCE_TIER_IRR_VARIABLES = ("tier_ok", "section9_clear", "single_source_ok")
MIN_EVIDENCE_TIER_IRR_EVENTS = 10
MIN_KAPPA = 0.6

FORBIDDEN_CLAIM_PHRASES = [
    "scripts/paper_tables.py",
    "analysis/paper_tables.py (not yet written)",
    "planned paper-table generator",
    "The five `trigger_is_action`",
    "five `trigger_is_action`",
    "Five events in the admitted corpus carry",
    "Day-precision triggers (n=48)",
    "hour-or-better precision (n=5)",
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Check paper-facing readiness gates.")
    parser.add_argument("--events-dir", default=str(EVENTS_DIR))
    parser.add_argument("--paper-tables-dir", default=str(PAPER_TABLES_DIR))
    parser.add_argument("--derived-dir", default=str(DERIVED_DIR))
    parser.add_argument("--claims", default=str(PAPER_CLAIMS))
    parser.add_argument(
        "--strict-audit",
        action="store_true",
        help="fail if paper-critical events are missing last_human_audit",
    )
    parser.add_argument(
        "--strict-null-audit",
        action="store_true",
        help="fail if null-denominator cases are missing last_human_audit",
    )
    parser.add_argument(
        "--strict-repro",
        action="store_true",
        help="fail if release reproducibility metadata indicates a dirty source tree",
    )
    parser.add_argument(
        "--strict-reliability",
        action="store_true",
        help=("fail unless κ provenance is independent_human; dryrun "
              "provenance requires --allow-dryrun-human-gates"),
    )
    parser.add_argument(
        "--allow-soft-attribution",
        action="store_true",
        help=("downgrade `attribution κ < 0.6` from ERROR to WARN. "
              "Valid only when `docs/paper_claims.md §0 Reliability "
              "discipline` documents that comparative attribution-rate "
              "claims are retracted at the named-row / audit level. "
              "Documented codebook gap, not a regression."),
    )
    parser.add_argument(
        "--allow-dryrun-human-gates",
        action="store_true",
        help=("allow explicitly marked dryrun human-audit stamps and "
              "`independent_human_dryrun_llm_simulated` IRR provenance. "
              "Use only for release-pipeline rehearsals, never for a "
              "real tag/submission release."),
    )
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


def load_all_events(events_dir: pathlib.Path) -> list[dict[str, Any]]:
    events: list[dict[str, Any]] = []
    for path in sorted(events_dir.glob("*.yaml")):
        if path.name == "TEMPLATE.yaml" or path.name.startswith("_"):
            continue
        event = yaml.safe_load(path.read_text())
        if isinstance(event, dict):
            events.append(event)
    return events


def load_json(path: pathlib.Path) -> Any:
    if not path.exists():
        raise FileNotFoundError(path)
    return json.loads(path.read_text())


def sha256_file(path: pathlib.Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def display_path(path: pathlib.Path) -> str:
    try:
        return str(path.relative_to(REPO_ROOT))
    except ValueError:
        return str(path)


def canonical_precision_bucket(event: dict[str, Any]) -> str:
    trigger = event.get("trigger") or {}
    precision = trigger.get("timestamp_precision")
    if precision in HOUR_PRECISION_VALUES:
        return "hour"
    if precision in DAY_PRECISION_VALUES:
        return "day"
    raise ValueError(
        f"{event.get('id')}: missing or unsupported trigger.timestamp_precision={precision!r}"
    )


def read_csv(path: pathlib.Path) -> list[dict[str, str]]:
    with path.open(newline="") as fh:
        return list(csv.DictReader(fh))


def has_crlf(path: pathlib.Path) -> bool:
    return b"\r\n" in path.read_bytes()


def git_head_short() -> str:
    proc = subprocess.run(
        ["git", "rev-parse", "--short=7", "HEAD"],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        check=False,
        timeout=5,
    )
    return proc.stdout.strip() if proc.returncode == 0 else ""


def source_hash_matches_current(recorded_hash: Any, current_hash: str) -> bool:
    return bool(recorded_hash) and recorded_hash == current_hash


def maybe_warn_source_commit_drift(
    *,
    label: str,
    recorded_commit: Any,
    head: str,
    recorded_hash: Any,
    current_hash: str,
    warnings: list[str],
    note: str,
) -> None:
    if (
        head
        and recorded_commit != head
        and not source_hash_matches_current(recorded_hash, current_hash)
    ):
        warnings.append(
            f"{label} source_commit={recorded_commit} but HEAD={head}; {note}"
        )


def parse_iso_date_or_datetime(value: Any) -> datetime | None:
    if not value:
        return None
    try:
        text = str(value)
        if len(text) == 10:
            text = text + "T00:00:00Z"
        return datetime.fromisoformat(text.replace("Z", "+00:00"))
    except ValueError:
        return None


def as_int(value: Any) -> int | None:
    try:
        return int(value)
    except (TypeError, ValueError):
        return None


def nonblank_list(value: Any) -> bool:
    return (
        isinstance(value, list)
        and bool(value)
        and all(isinstance(item, str) and item.strip() for item in value)
    )


def citation_has_replayable_anchor(citation: Any) -> bool:
    if not isinstance(citation, dict):
        return False
    if citation.get("type") == "primary_onchain" and citation.get("tx_hash"):
        return True
    return bool(
        citation.get("wayback")
        or citation.get("query_hash")
        or (citation.get("body_hash") and citation.get("body_path"))
        or nonblank_list(citation.get("measurement_ids"))
    )


def check_trigger_citation_archiving(
    all_events: list[dict[str, Any]],
    errors: list[str],
    warnings: list[str],
    strict_repro: bool,
) -> None:
    for event in all_events:
        event_id = str(event.get("id") or "<unknown>")
        citations = (event.get("trigger") or {}).get("citation") or []
        if not isinstance(citations, list):
            continue
        has_trigger_anchor = any(citation_has_replayable_anchor(c) for c in citations)
        if not has_trigger_anchor:
            msg = (
                f"{event_id}: trigger.citation has no replayable archive anchor "
                "(wayback, body_hash+body_path, query_hash, measurement_ids, or tx_hash)"
            )
            if strict_repro:
                errors.append(msg)
            else:
                warnings.append(msg)
        for idx, citation in enumerate(citations):
            if citation_has_replayable_anchor(citation):
                continue
            evidence_use = citation.get("evidence_use") if isinstance(citation, dict) else None
            if evidence_use not in {"contextual_unarchived", "non_admission"}:
                msg = (
                    f"{event_id}: trigger.citation[{idx}] has no replayable archive "
                    "anchor and is not marked evidence_use=contextual_unarchived "
                    "or non_admission"
                )
                if strict_repro:
                    errors.append(msg)
                else:
                    warnings.append(msg)


def check_temporal_tier_contract(
    all_events: list[dict[str, Any]],
    errors: list[str],
) -> None:
    for event in all_events:
        event_id = str(event.get("id") or "<unknown>")
        temporal_tier = str(event.get("temporal_tier") or "")
        analysis_use = str(event.get("analysis_use") or "")
        if not temporal_tier:
            errors.append(f"{event_id}: missing temporal_tier")
        if not analysis_use:
            errors.append(f"{event_id}: missing analysis_use")
        if (
            temporal_tier in {"discovery_only_2007_2012", "historical_baseline_2013_2016"}
            and analysis_use == "comparable_analysis"
        ):
            errors.append(
                f"{event_id}: {temporal_tier} row cannot enter comparable_analysis"
            )


def check_dataset_surface_contract(
    dataset_meta: dict[str, Any],
    csv_rows: list[dict[str, str]],
    dataset_payload: Any,
    errors: list[str],
) -> None:
    event_count = as_int(dataset_meta.get("event_count"))
    registry_event_count = as_int(dataset_meta.get("registry_event_count"))
    paper_corpus_event_count = as_int(dataset_meta.get("paper_corpus_event_count"))
    counts_by_status = dataset_meta.get("counts_by_status") or {}
    admitted_count = (
        as_int(counts_by_status.get("admitted"))
        if isinstance(counts_by_status, dict)
        else None
    )

    if dataset_meta.get("release_surface_scope") != "all_event_yaml_records":
        errors.append(
            "dataset.meta.json release_surface_scope must be all_event_yaml_records"
        )
    if dataset_meta.get("paper_corpus_statuses") != ["admitted"]:
        errors.append("dataset.meta.json paper_corpus_statuses must be ['admitted']")
    if event_count != len(csv_rows):
        errors.append(
            f"dataset.meta.json event_count={dataset_meta.get('event_count')} "
            f"but dataset.csv has {len(csv_rows)} rows"
        )
    if registry_event_count != event_count:
        errors.append(
            f"dataset.meta.json registry_event_count={dataset_meta.get('registry_event_count')} "
            f"but event_count={dataset_meta.get('event_count')}"
        )
    if isinstance(dataset_payload, list) and event_count != len(dataset_payload):
        errors.append(
            f"dataset.meta.json event_count={dataset_meta.get('event_count')} "
            f"but dataset.json has {len(dataset_payload)} rows"
        )
    elif not isinstance(dataset_payload, list):
        errors.append("dataset.json must contain a list of event records")
    if paper_corpus_event_count != admitted_count:
        errors.append(
            "dataset.meta.json paper_corpus_event_count must equal "
            "counts_by_status.admitted"
        )
    included_rows = [
        row for row in csv_rows
        if str(row.get("paper_corpus_included") or "").lower() == "true"
    ]
    if len(included_rows) != paper_corpus_event_count:
        errors.append(
            f"dataset.csv paper_corpus_included=true rows={len(included_rows)} "
            f"but dataset.meta.json paper_corpus_event_count="
            f"{dataset_meta.get('paper_corpus_event_count')}"
        )
    for row in csv_rows:
        expected = str(row.get("status") or "") == "admitted"
        observed = str(row.get("paper_corpus_included") or "").lower() == "true"
        if expected != observed:
            errors.append(
                f"{row.get('id')}: dataset.csv paper_corpus_included="
                f"{row.get('paper_corpus_included')!r} inconsistent with "
                f"status={row.get('status')!r}"
            )


def month_range(start: datetime, end: datetime) -> list[str]:
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


def check_temporal_ledger(
    dataset_meta: dict[str, Any] | None,
    errors: list[str],
) -> None:
    csv_path = TEMPORAL_LEDGER_DIR / "monthly_discovery_ledger.csv"
    json_path = TEMPORAL_LEDGER_DIR / "monthly_discovery_ledger.json"
    if not csv_path.exists():
        return
    try:
        frame = yaml.safe_load(SAMPLING_FRAME.read_text())
    except FileNotFoundError:
        errors.append("missing sampling/frame.yaml")
        return
    if not isinstance(frame, dict):
        errors.append("sampling/frame.yaml must parse as a mapping")
        return
    snapshot = frame.get("snapshot_scope") or {}
    start = parse_iso_date_or_datetime(snapshot.get("historical_start") or "2008-01-01")
    cutoff = parse_iso_date_or_datetime((dataset_meta or {}).get("cutoff_date"))
    if not start or not cutoff:
        errors.append("temporal ledger needs sampling historical_start and dataset cutoff_date")
        return
    source_frame_ids = {
        str(spec.get("source_frame_id") or "")
        for spec in (frame.get("source_frames") or {}).values()
        if isinstance(spec, dict) and spec.get("source_frame_id")
    }
    if not source_frame_ids:
        errors.append("sampling/frame.yaml source_frames missing source_frame_id values")
        return
    months = set(month_range(start, cutoff))
    expected = {
        (source_frame_id, discovery_month)
        for source_frame_id in source_frame_ids
        for discovery_month in months
    }
    rows = read_csv(csv_path)
    observed = {
        (row.get("source_frame_id") or "", row.get("discovery_month") or "")
        for row in rows
    }
    missing = sorted(expected - observed)
    if missing:
        preview = ", ".join(f"{source}:{month}" for source, month in missing[:10])
        suffix = "..." if len(missing) > 10 else ""
        errors.append(
            f"temporal ledger missing {len(missing)} source-frame/month rows: "
            f"{preview}{suffix}"
        )
    if len(rows) != len(observed):
        errors.append("temporal ledger has duplicate source-frame/month rows")
    for row in rows:
        status = row.get("ledger_status") or ""
        if status not in TEMPORAL_LEDGER_STATUSES:
            errors.append(
                f"{row.get('source_frame_id')} {row.get('discovery_month')}: "
                f"invalid temporal ledger status={status!r}"
            )
        tier = row.get("temporal_tier") or ""
        analysis_use = row.get("analysis_use") or ""
        if (
            tier in {"discovery_only_2007_2012", "historical_baseline_2013_2016"}
            and analysis_use == "comparable_analysis"
        ):
            errors.append(
                f"{row.get('source_frame_id')} {row.get('discovery_month')}: "
                f"{tier} row cannot use comparable_analysis"
            )
    if json_path.exists():
        payload = load_json(json_path)
        meta = payload.get("meta") if isinstance(payload, dict) else {}
        row_count = as_int((meta or {}).get("row_count"))
        if row_count != len(rows):
            errors.append(
                f"monthly_discovery_ledger.json meta.row_count={row_count} "
                f"but CSV has {len(rows)} rows"
            )


def check_citation_metadata(
    dataset_meta: dict[str, Any],
    errors: list[str],
    warnings: list[str],
    strict_repro: bool,
) -> None:
    try:
        citation = yaml.safe_load(CITATION_CFF.read_text())
    except FileNotFoundError:
        errors.append("missing CITATION.cff")
        return
    if not isinstance(citation, dict):
        errors.append("CITATION.cff must parse as a mapping")
        return

    citation_version = str(citation.get("version") or "")
    dataset_version = str(dataset_meta.get("dataset_version") or "")
    if citation_version and dataset_version and citation_version != dataset_version:
        errors.append(
            f"CITATION.cff version={citation_version} but "
            f"dataset.meta.json dataset_version={dataset_version}; run `make dataset`"
        )

    citation_date = parse_iso_date_or_datetime(citation.get("date-released"))
    cutoff = parse_iso_date_or_datetime(dataset_meta.get("cutoff_date"))
    if citation_date and cutoff and citation_date < cutoff:
        msg = (
            f"CITATION.cff date-released={citation.get('date-released')} predates "
            f"dataset cutoff_date={dataset_meta.get('cutoff_date')}; allowed for "
            "working snapshots, blocked for release/submission mode"
        )
        if strict_repro:
            errors.append(msg)
        else:
            warnings.append(msg)


def check_source_manifest(errors: list[str]) -> None:
    csv_path = SOURCE_MANIFEST_PREFIX.with_suffix(".csv")
    json_path = SOURCE_MANIFEST_PREFIX.with_suffix(".json")
    meta_path = SOURCE_MANIFEST_PREFIX.with_suffix(".meta.json")
    if not (csv_path.exists() and json_path.exists() and meta_path.exists()):
        return

    csv_rows = read_csv(csv_path)
    payload = load_json(json_path)
    meta = load_json(meta_path)
    if not isinstance(payload, dict):
        errors.append("sources/source_manifest.json must contain a mapping")
        return
    json_rows = payload.get("rows")
    json_meta = payload.get("meta")
    if not isinstance(json_rows, list):
        errors.append("sources/source_manifest.json missing rows[]")
        return
    if not isinstance(json_meta, dict):
        errors.append("sources/source_manifest.json missing meta{}")
        return

    row_count = as_int(meta.get("row_count"))
    json_row_count = as_int(json_meta.get("row_count"))
    if row_count != len(csv_rows):
        errors.append(
            f"sources/source_manifest.meta.json row_count={meta.get('row_count')} "
            f"but CSV has {len(csv_rows)} rows"
        )
    if row_count != len(json_rows):
        errors.append(
            f"sources/source_manifest.meta.json row_count={meta.get('row_count')} "
            f"but JSON has {len(json_rows)} rows"
        )
    if json_row_count != row_count:
        errors.append(
            f"sources/source_manifest.json meta.row_count={json_meta.get('row_count')} "
            f"but sidecar meta row_count={meta.get('row_count')}"
        )

    total_bytes = sum(as_int(row.get("bytes")) or 0 for row in csv_rows)
    meta_total_bytes = as_int(meta.get("total_bytes"))
    json_total_bytes = as_int(json_meta.get("total_bytes"))
    if meta_total_bytes != total_bytes:
        errors.append(
            f"sources/source_manifest.meta.json total_bytes={meta.get('total_bytes')} "
            f"but CSV rows sum to {total_bytes}"
        )
    if json_total_bytes != meta_total_bytes:
        errors.append(
            f"sources/source_manifest.json meta.total_bytes={json_meta.get('total_bytes')} "
            f"but sidecar meta total_bytes={meta.get('total_bytes')}"
        )

    json_paths = {
        str(row.get("path"))
        for row in json_rows
        if isinstance(row, dict) and row.get("path")
    }
    csv_paths = {row.get("path") for row in csv_rows if row.get("path")}
    if csv_paths != json_paths:
        errors.append("sources/source_manifest.csv and .json list different paths")

    for row in csv_rows:
        rel = row.get("path") or ""
        if not rel:
            errors.append("sources/source_manifest.csv has a row with blank path")
            continue
        path = (REPO_ROOT / rel).resolve()
        try:
            path.relative_to(REPO_ROOT)
        except ValueError:
            errors.append(f"sources/source_manifest.csv path escapes repo root: {rel}")
            continue
        if not path.is_file():
            errors.append(f"sources/source_manifest.csv path is missing: {rel}")
            continue
        expected_bytes = as_int(row.get("bytes"))
        actual_bytes = path.stat().st_size
        if expected_bytes != actual_bytes:
            errors.append(
                f"{rel}: manifest bytes={row.get('bytes')} but file has {actual_bytes}"
            )
        expected_sha = str(row.get("sha256") or "").strip().lower()
        if len(expected_sha) != 64 or any(c not in "0123456789abcdef" for c in expected_sha):
            errors.append(f"{rel}: manifest sha256 is not 64 lowercase hex characters")
            continue
        actual_sha = sha256_file(path)
        if actual_sha != expected_sha:
            errors.append(
                f"{rel}: manifest sha256={expected_sha[:12]}... "
                f"but current file sha256={actual_sha[:12]}..."
            )


def kappa_value(report: dict[str, Any], variable: str) -> float | None:
    variables = report.get("variables") or {}
    value = (variables.get(variable) or {}).get("kappa")
    return value if isinstance(value, (int, float)) else None


def human_audit_is_dryrun(event: dict[str, Any]) -> bool:
    notes = str(event.get("analysis_notes") or "")
    return (
        bool(event.get("last_human_audit"))
        and "LAST_HUMAN_AUDIT STAMP" in notes
        and "DRYRUN" in notes
    )


def handle_dryrun_audit_stamps(
    *,
    ids: list[str],
    gate_name: str,
    strict: bool,
    allow_dryrun: bool,
    errors: list[str],
    warnings: list[str],
) -> None:
    if not ids:
        return
    msg = (
        f"{len(ids)} {gate_name} cases carry DRYRUN last_human_audit "
        "stamps; these are pipeline-rehearsal markers, not real human "
        "audit: " + ", ".join(ids)
    )
    if strict and not allow_dryrun:
        errors.append(msg + " (pass --allow-dryrun-human-gates only for dry runs)")
    else:
        warnings.append(msg)


def handle_irr_provenance(
    *,
    mode: str | None,
    strict_reliability: bool,
    allow_dryrun: bool,
    errors: list[str],
    warnings: list[str],
) -> None:
    if mode == "independent_human_dryrun_llm_simulated":
        msg = (
            "IRR coder_provenance.mode is "
            "independent_human_dryrun_llm_simulated; this is a "
            "pipeline rehearsal, not independent-human reliability"
        )
        if strict_reliability and not allow_dryrun:
            errors.append(
                msg + " (pass --allow-dryrun-human-gates only for dry runs)"
            )
        else:
            warnings.append(msg)
    elif mode != "independent_human":
        msg = (
            f"IRR coder_provenance.mode={mode!r}; κ may be cited only as "
            "self-consistency, not independent-human reliability"
        )
        if strict_reliability:
            errors.append(msg)
        else:
            warnings.append(msg)


def _reliability_message(
    *,
    strict_reliability: bool,
    errors: list[str],
    warnings: list[str],
    message: str,
) -> None:
    if strict_reliability:
        errors.append(message)
    else:
        warnings.append(message)


def check_evidence_tier_irr(
    *,
    events: list[dict[str, Any]],
    report_path: pathlib.Path = EVIDENCE_TIER_IRR_REPORT,
    strict_reliability: bool,
    errors: list[str],
    warnings: list[str],
) -> None:
    attested_ids = sorted(
        event["id"]
        for event in events
        if event.get("evidence_tier") == "attested_secondary"
    )
    if not attested_ids:
        return

    if not report_path.exists():
        _reliability_message(
            strict_reliability=strict_reliability,
            errors=errors,
            warnings=warnings,
            message=(
                f"{len(attested_ids)} admitted events use "
                "evidence_tier=attested_secondary, but the evidence-tier "
                f"IRR report is missing at {display_path(report_path)}; "
                "run `make evidence-tier-irr-kappa` only after two independent "
                "human coders complete the worksheet"
            ),
        )
        return

    try:
        report = load_json(report_path)
    except (OSError, json.JSONDecodeError) as exc:
        _reliability_message(
            strict_reliability=strict_reliability,
            errors=errors,
            warnings=warnings,
            message=f"could not read evidence-tier IRR report {report_path}: {exc}",
        )
        return

    status = report.get("status")
    provenance = report.get("coder_provenance") or {}
    mode = provenance.get("mode")
    if status != "complete":
        _reliability_message(
            strict_reliability=strict_reliability,
            errors=errors,
            warnings=warnings,
            message=(
                f"evidence-tier IRR report status={status!r}; "
                "attested_secondary release/submission claims require a "
                "completed two-human-coder pass"
            ),
        )
    if mode != "independent_human":
        _reliability_message(
            strict_reliability=strict_reliability,
            errors=errors,
            warnings=warnings,
            message=(
                f"evidence-tier IRR coder_provenance.mode={mode!r}; "
                "attested_secondary release/submission claims require "
                "independent_human provenance"
            ),
        )

    n_events = report.get("n_events")
    if not isinstance(n_events, int) or n_events < MIN_EVIDENCE_TIER_IRR_EVENTS:
        _reliability_message(
            strict_reliability=strict_reliability,
            errors=errors,
            warnings=warnings,
            message=(
                "evidence-tier IRR report covers "
                f"{n_events!r} events; expected at least "
                f"{MIN_EVIDENCE_TIER_IRR_EVENTS}"
            ),
        )

    variables = report.get("variables") or {}
    for variable in EVIDENCE_TIER_IRR_VARIABLES:
        stats = variables.get(variable) or {}
        n_incomplete = stats.get("n_incomplete")
        n_coded = stats.get("n_coded")
        n_total = stats.get("n_total")
        value = stats.get("kappa")
        if n_incomplete not in (0, None):
            _reliability_message(
                strict_reliability=strict_reliability,
                errors=errors,
                warnings=warnings,
                message=(
                    f"evidence-tier IRR variable {variable} has "
                    f"{n_incomplete} incomplete row(s)"
                ),
            )
        if not isinstance(n_coded, int) or n_coded < MIN_EVIDENCE_TIER_IRR_EVENTS:
            _reliability_message(
                strict_reliability=strict_reliability,
                errors=errors,
                warnings=warnings,
                message=(
                    f"evidence-tier IRR variable {variable} has "
                    f"{n_coded!r}/{n_total!r} coded rows; expected at least "
                    f"{MIN_EVIDENCE_TIER_IRR_EVENTS}"
                ),
            )
        if not isinstance(value, (int, float)) or value < MIN_KAPPA:
            _reliability_message(
                strict_reliability=strict_reliability,
                errors=errors,
                warnings=warnings,
                message=(
                    f"evidence-tier IRR variable {variable} κ={value!r}; "
                    f"expected >= {MIN_KAPPA}"
                ),
            )


def main() -> int:
    args = parse_args()
    events_dir = pathlib.Path(args.events_dir)
    paper_tables_dir = pathlib.Path(args.paper_tables_dir)
    derived_dir = pathlib.Path(args.derived_dir)
    claims_path = pathlib.Path(args.claims)

    errors: list[str] = []
    warnings: list[str] = []

    events = load_events(events_dir)
    all_events = load_all_events(events_dir)
    events_by_id = {event["id"]: event for event in events}
    all_event_ids = {event["id"] for event in all_events}
    head = git_head_short()
    dataset_meta: dict[str, Any] | None = None
    current_input_hash, _current_input_count = source_input_hash()

    check_trigger_citation_archiving(
        all_events,
        errors,
        warnings,
        args.strict_repro,
    )
    check_temporal_tier_contract(all_events, errors)

    try:
        dataset_meta = load_json(DATASET_META)
        check_citation_metadata(dataset_meta, errors, warnings, args.strict_repro)
        recorded_input_hash = dataset_meta.get("source_input_hash")
        dataset_source_hash_matches = source_hash_matches_current(
            recorded_input_hash,
            current_input_hash,
        )
        if recorded_input_hash and not dataset_source_hash_matches:
            errors.append(
                f"dataset.meta.json source_input_hash={recorded_input_hash} "
                f"but current source_input_hash={current_input_hash}; run `make dataset`"
            )
        maybe_warn_source_commit_drift(
            label="dataset.meta.json",
            recorded_commit=dataset_meta.get("source_commit"),
            head=head,
            recorded_hash=recorded_input_hash,
            current_hash=current_input_hash,
            warnings=warnings,
            note="source_commit is display metadata only; source_input_hash is the self-verifying gate",
        )
        if dataset_meta.get("source_tree_dirty") and not dataset_source_hash_matches:
            msg = (
                "dataset.meta.json was generated from a dirty source-input tree; "
                "allowed for working snapshots, blocked for release/submission mode"
            )
            if args.strict_repro:
                errors.append(msg)
            else:
                warnings.append(msg)
        generated = parse_iso_date_or_datetime(dataset_meta.get("generated_at"))
        cutoff = parse_iso_date_or_datetime(dataset_meta.get("cutoff_date"))
        if generated and cutoff and generated < cutoff:
            errors.append(
                f"dataset.meta.json generated_at={dataset_meta.get('generated_at')} "
                f"predates cutoff_date={dataset_meta.get('cutoff_date')}; "
                "use SOURCE_DATE_EPOCH at or after the dataset cutoff"
            )
    except FileNotFoundError:
        errors.append("missing dataset.meta.json — run `make dataset`")

    for path in (DATASET_JSON, DATASET_CSV):
        if not path.exists():
            errors.append(f"missing tracked release dataset artifact: {path.name} — run `make dataset`")

    if dataset_meta is not None:
        try:
            check_dataset_surface_contract(
                dataset_meta,
                read_csv(DATASET_CSV),
                load_json(DATASET_JSON),
                errors,
            )
        except FileNotFoundError:
            pass

    for rel in REQUIRED_TABLES:
        path = paper_tables_dir / rel
        if not path.exists():
            errors.append(f"missing paper table artifact: {path.relative_to(REPO_ROOT)}")

    for rel in REQUIRED_DERIVED:
        path = derived_dir / rel
        if not path.exists():
            errors.append(
                f"missing derived artifact cited by paper claims: "
                f"{path.relative_to(REPO_ROOT)} — run "
                "`make derived`")

    for rel in REQUIRED_TRIGGER_REGISTRY:
        path = TRIGGER_REGISTRY_DIR / rel
        if not path.exists():
            errors.append(
                f"missing trigger-registry artifact: {path.relative_to(REPO_ROOT)} — "
                "run `make trigger-registry`"
            )

    for rel in REQUIRED_TEMPORAL_LEDGER:
        path = TEMPORAL_LEDGER_DIR / rel
        if not path.exists():
            errors.append(
                f"missing temporal-ledger artifact: {path.relative_to(REPO_ROOT)} — "
                "run `make temporal-ledger`"
            )
    check_temporal_ledger(dataset_meta, errors)

    for rel in REQUIRED_SOURCE_MANIFEST:
        path = REPO_ROOT / rel
        if not path.exists():
            errors.append(
                f"missing source manifest artifact: {path.relative_to(REPO_ROOT)} — "
                "run `make source-manifest`"
            )
    check_source_manifest(errors)

    try:
        registry_rows = read_csv(TRIGGER_REGISTRY_DIR / "trigger_registry.csv")
        registry_event_ids = {
            row.get("event_id")
            for row in registry_rows
            if row.get("source_type") == "event_yaml" and row.get("event_id")
        }
        missing_from_registry = sorted(all_event_ids - registry_event_ids)
        if missing_from_registry:
            errors.append(
                "trigger registry missing event YAML records: "
                + ", ".join(missing_from_registry)
            )
        if len(registry_rows) < len(all_events):
            errors.append(
                f"trigger registry has {len(registry_rows)} rows; "
                f"expected at least {len(all_events)} event rows"
            )
    except FileNotFoundError:
        pass

    try:
        coverage_rows = read_csv(derived_dir / "coverage_matrix.csv")
        expected_rows = len(all_events) * 6
        if len(coverage_rows) != expected_rows:
            errors.append(
                f"coverage_matrix.csv has {len(coverage_rows)} rows; "
                f"expected {expected_rows} event-layer rows"
            )
        l0_summary_rows = read_csv(derived_dir / "l0_coverage_summary.csv")
        for row in l0_summary_rows:
            if not row.get("input_url"):
                errors.append(
                    f"{row.get('event_id')}/{row.get('domain')}: "
                    "l0_coverage_summary.csv missing input_url"
                )
            if not row.get("query_hash"):
                errors.append(
                    f"{row.get('event_id')}/{row.get('domain')}: "
                    "l0_coverage_summary.csv missing query_hash"
                )
        l0_denominator_events = {
            row.get("event_id")
            for row in l0_summary_rows
            if row.get("denominator_class") == "measurement_denominator"
        }
        for row in coverage_rows:
            if row.get("layer") != "l0_network":
                continue
            if row.get("coverage_status") in {"measured", "partially_measured"}:
                event_id = row.get("event_id")
                if event_id not in l0_denominator_events:
                    errors.append(
                        f"{event_id}: l0_network coverage={row.get('coverage_status')} "
                        "but derived/l0_coverage_summary.csv has no measurement_denominator row"
                    )
    except FileNotFoundError:
        pass

    try:
        layer_rows = read_csv(derived_dir / "layer_observability.csv")
        for row in layer_rows:
            not_measured = int(row.get("not_measured_count") or 0)
            if not_measured > 0 and row.get("changed_given_applicable"):
                errors.append(
                    f"{row.get('layer')}: changed_given_applicable must be blank "
                    "when applicable rows include not_measured coverage"
                )
    except FileNotFoundError:
        pass

    try:
        table_meta = load_json(paper_tables_dir / ".meta.json")
        expected_paper_event_count = (
            as_int(dataset_meta.get("paper_corpus_event_count"))
            if dataset_meta is not None
            else len(events)
        )
        if table_meta.get("event_count") != expected_paper_event_count:
            errors.append(
                f"paper table event_count={table_meta.get('event_count')} "
                f"but paper corpus event count={expected_paper_event_count}"
            )
        snapshot = table_meta.get("dataset_snapshot") or {}
        snapshot_input_hash = snapshot.get("source_input_hash")
        expected_snapshot_hash = (
            dataset_meta.get("source_input_hash")
            if dataset_meta is not None
            else current_input_hash
        )
        if snapshot_input_hash and snapshot_input_hash != expected_snapshot_hash:
            errors.append(
                "analysis/paper_tables/.meta.json "
                f"source_input_hash={snapshot_input_hash} but "
                f"dataset.meta.json source_input_hash={expected_snapshot_hash}; "
                "run `make paper-tables`"
            )
        maybe_warn_source_commit_drift(
            label="analysis/paper_tables/.meta.json",
            recorded_commit=snapshot.get("source_commit"),
            head=head,
            recorded_hash=snapshot_input_hash,
            current_hash=current_input_hash,
            warnings=warnings,
            note="source_commit is display metadata only; source_input_hash gates the dataset snapshot",
        )
        generated = parse_iso_date_or_datetime(table_meta.get("generated_at"))
        cutoff = parse_iso_date_or_datetime(snapshot.get("cutoff_date"))
        if generated and cutoff and generated < cutoff:
            errors.append(
                f"analysis/paper_tables/.meta.json generated_at={table_meta.get('generated_at')} "
                f"predates cutoff_date={snapshot.get('cutoff_date')}"
            )
    except FileNotFoundError:
        pass

    try:
        table1_rows = read_csv(paper_tables_dir / "table1_case_roles.csv")
        if len(table1_rows) != len(events):
            errors.append(
                f"table1_case_roles.csv has {len(table1_rows)} rows; "
                f"expected {len(events)} admitted events"
            )
        for row in table1_rows:
            event = events_by_id.get(row.get("event_id", ""))
            if not event:
                errors.append(f"table1 has unknown event_id={row.get('event_id')}")
                continue
            if row.get("admission_tier") != event.get("admission_tier"):
                errors.append(
                    f"{event['id']}: table1 admission_tier={row.get('admission_tier')} "
                    f"but event YAML has {event.get('admission_tier')}"
                )
            expected = canonical_precision_bucket(event)
            if row.get("trigger_precision_bucket") != expected:
                errors.append(
                    f"{event['id']}: table1 precision={row.get('trigger_precision_bucket')} "
                    f"but trigger.timestamp_precision implies {expected}"
                )
    except FileNotFoundError:
        pass

    try:
        event_metrics = load_json(derived_dir / "event_metrics.json")
        archetypes = load_json(derived_dir / "event_archetypes.json")
        metrics_by_id = {row["event_id"]: row for row in event_metrics}
        archetypes_by_id = {row["event_id"]: row for row in archetypes}
        expected_trigger_action = 0
        expected_hour = 0
        expected_day = 0
        for event in events:
            slug = event["id"]
            metric = metrics_by_id.get(slug, {})
            archetype = archetypes_by_id.get(slug, {})
            if metric.get("time_to_first_change_hours") is None:
                continue
            if archetype.get("trigger_is_action"):
                expected_trigger_action += 1
                continue
            if canonical_precision_bucket(event) == "hour":
                expected_hour += 1
            else:
                expected_day += 1

        table4_md = (paper_tables_dir / "table4_latency_by_precision.md").read_text()
        panel_counts = {
            "A": re.search(r"Panel A .*\(n=(\d+)\)", table4_md),
            "B": re.search(r"Panel B .*\(n=(\d+)\)", table4_md),
            "C": re.search(r"Panel C .*\(n=(\d+)\)", table4_md),
        }
        observed = {
            key: int(match.group(1)) if match else None
            for key, match in panel_counts.items()
        }
        expected = {"A": expected_hour, "B": expected_day, "C": expected_trigger_action}
        for key in ("A", "B", "C"):
            if observed[key] != expected[key]:
                errors.append(
                    f"Table 4 Panel {key} n={observed[key]} but expected {expected[key]}"
                )

        table4_rows = read_csv(paper_tables_dir / "table4_latency_by_precision.csv")
        csv_trigger_action = sum(
            1 for row in table4_rows if str(row.get("trigger_is_action")).lower() == "true"
        )
        if csv_trigger_action != expected_trigger_action:
            errors.append(
                f"table4 CSV trigger_is_action rows={csv_trigger_action}; "
                f"expected {expected_trigger_action}"
            )
    except FileNotFoundError as exc:
        errors.append(f"missing derived or paper-table artifact for Table 4 check: {exc}")

    try:
        null_rows = read_csv(paper_tables_dir / "table6_null_denominator.csv")
        anchorless = [row["event_id"] for row in null_rows if not row.get("evidence_anchors_present")]
        if anchorless:
            errors.append(
                "Table 6 has null cases without evidence anchors: " + ", ".join(anchorless)
            )
    except FileNotFoundError:
        pass

    for rel in (
        "table1_case_roles.csv",
        "table4_latency_by_precision.csv",
        "table6_null_denominator.csv",
        "sources/source_manifest.csv",
    ):
        path = (REPO_ROOT / rel) if rel.startswith("sources/") else (paper_tables_dir / rel)
        if path.exists() and has_crlf(path):
            errors.append(f"{path.relative_to(REPO_ROOT)} contains CRLF line endings")

    if claims_path.exists():
        claims = claims_path.read_text()
        for phrase in FORBIDDEN_CLAIM_PHRASES:
            if phrase in claims:
                errors.append(f"paper_claims.md contains forbidden stale phrase: {phrase}")
        required_markers = [
            "Six artifact measurement protocol",
            "Trigger registry",
            "Claim-to-table-source matrix",
            "Sampling frame",
            "Uncertainty-to-analysis mapping",
        ]
        for marker in required_markers:
            if marker not in claims:
                errors.append(f"paper_claims.md missing required section marker: {marker}")
    else:
        errors.append(f"missing {claims_path.relative_to(REPO_ROOT)}")

    anchor_missing_scoped = [
        event["id"]
        for event in events
        if event.get("admission_tier") == "anchor_case" and not event.get("scoped_knowledge")
    ]
    if anchor_missing_scoped:
        errors.append(
            "anchor cases missing scoped_knowledge: " + ", ".join(anchor_missing_scoped)
        )

    unaudited_anchors = [
        event["id"]
        for event in events
        if event.get("admission_tier") == "anchor_case"
        and not event.get("last_human_audit")
    ]
    if unaudited_anchors:
        msg = (
            f"{len(unaudited_anchors)} paper-spotlight anchor cases lack "
            "last_human_audit: " + ", ".join(unaudited_anchors)
        )
        if args.strict_audit:
            errors.append(msg)
        else:
            warnings.append(msg)

    dryrun_audited_anchors = [
        event["id"]
        for event in events
        if event.get("admission_tier") == "anchor_case"
        and human_audit_is_dryrun(event)
    ]
    handle_dryrun_audit_stamps(
        ids=dryrun_audited_anchors,
        gate_name="paper-spotlight anchor",
        strict=args.strict_audit,
        allow_dryrun=args.allow_dryrun_human_gates,
        errors=errors,
        warnings=warnings,
    )

    unaudited_nulls = [
        event["id"]
        for event in events
        if event.get("admission_tier") == "null_case"
        and not event.get("last_human_audit")
    ]
    if unaudited_nulls:
        msg = (
            f"{len(unaudited_nulls)} null denominator cases lack last_human_audit "
            "(allowed for working snapshots; blocked by --strict-null-audit): "
            + ", ".join(unaudited_nulls)
        )
        if args.strict_null_audit:
            errors.append(msg)
        else:
            warnings.append(msg)

    dryrun_audited_nulls = [
        event["id"]
        for event in events
        if event.get("admission_tier") == "null_case"
        and human_audit_is_dryrun(event)
    ]
    handle_dryrun_audit_stamps(
        ids=dryrun_audited_nulls,
        gate_name="null-denominator",
        strict=args.strict_null_audit,
        allow_dryrun=args.allow_dryrun_human_gates,
        errors=errors,
        warnings=warnings,
    )

    try:
        irr = load_json(IRR_REPORT)
        provenance = irr.get("coder_provenance") or {}
        mode = provenance.get("mode")
        handle_irr_provenance(
            mode=mode,
            strict_reliability=args.strict_reliability,
            allow_dryrun=args.allow_dryrun_human_gates,
            errors=errors,
            warnings=warnings,
        )
        coverage_kappa = kappa_value(irr, "coverage_status")
        if coverage_kappa is None or coverage_kappa < 0.6:
            errors.append(
                "coverage_status κ is missing or below 0.6; C1 coverage-matched "
                "rates are not paper-ready"
            )
        for variable in ("observation_kind", "attribution"):
            value = kappa_value(irr, variable)
            if value is None:
                warnings.append(
                    f"{variable} κ is missing; claims depending on {variable} "
                    "must remain parked/descriptive"
                )
            elif value < 0.6:
                # WARN-by-default, ERROR under --strict-reliability,
                # downgrade back to WARN under
                # --allow-soft-attribution (only for `attribution`
                # because `paper_claims.md §0 Reliability discipline`
                # documents the comparative-rate retraction for that
                # variable specifically; `observation_kind` has no
                # such retraction so the strict-reliability gate
                # still fires).
                msg = (
                    f"{variable} κ={value} is below 0.6; claims "
                    f"depending on {variable} must stay at named-row / "
                    "audit level (no corpus-level comparative rate)"
                )
                soft = (variable == "attribution"
                        and args.allow_soft_attribution)
                if args.strict_reliability and not soft:
                    errors.append(msg)
                else:
                    warnings.append(msg)
    except FileNotFoundError:
        errors.append("missing analysis/inter_rater/kappa_report.json — run `make irr-kappa`")

    check_evidence_tier_irr(
        events=events,
        strict_reliability=args.strict_reliability,
        errors=errors,
        warnings=warnings,
    )

    for warning in warnings:
        print(f"WARN: {warning}")
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print(
        "[check_paper_readiness] OK: paper claims, paper tables, precision "
        "buckets, null anchors, and line endings are coherent"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
