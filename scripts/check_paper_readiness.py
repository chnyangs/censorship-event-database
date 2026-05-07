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
CITATION_CFF = REPO_ROOT / "CITATION.cff"
IRR_REPORT = REPO_ROOT / "analysis" / "inter_rater" / "kappa_report.json"
TRIGGER_REGISTRY_DIR = REPO_ROOT / "analysis" / "trigger_registry"
SOURCE_MANIFEST_PREFIX = REPO_ROOT / "sources" / "source_manifest"

HOUR_PRECISION_VALUES = {"second", "minute", "hour"}
DAY_PRECISION_VALUES = {"day", "date"}

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

REQUIRED_SOURCE_MANIFEST = [
    "sources/source_manifest.csv",
    "sources/source_manifest.json",
    "sources/source_manifest.md",
    "sources/source_manifest.meta.json",
]

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
        "--strict-repro",
        action="store_true",
        help="fail if release reproducibility metadata indicates a dirty source tree",
    )
    parser.add_argument(
        "--strict-reliability",
        action="store_true",
        help="fail unless κ provenance is independent_human",
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

    try:
        dataset_meta = load_json(DATASET_META)
        check_citation_metadata(dataset_meta, errors, warnings, args.strict_repro)
        current_input_hash, _current_input_count = source_input_hash()
        if dataset_meta.get("source_input_hash") and dataset_meta.get("source_input_hash") != current_input_hash:
            errors.append(
                f"dataset.meta.json source_input_hash={dataset_meta.get('source_input_hash')} "
                f"but current source_input_hash={current_input_hash}; run `make dataset`"
            )
        if head and dataset_meta.get("source_commit") != head:
            warnings.append(
                f"dataset.meta.json source_commit={dataset_meta.get('source_commit')} "
                f"but HEAD={head}; source_commit is display metadata only, "
                "source_input_hash is the self-verifying gate"
            )
        if dataset_meta.get("source_tree_dirty"):
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
        if table_meta.get("event_count") != len(events):
            errors.append(
                f"paper table event_count={table_meta.get('event_count')} "
                f"but admitted event count={len(events)}"
            )
        snapshot = table_meta.get("dataset_snapshot") or {}
        if head and snapshot.get("source_commit") != head:
            warnings.append(
                f"analysis/paper_tables/.meta.json source_commit={snapshot.get('source_commit')} "
                f"but HEAD={head}; source_commit is display metadata only, "
                "source_input_hash gates the dataset snapshot"
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

    unaudited_nulls = [
        event["id"]
        for event in events
        if event.get("admission_tier") == "null_case"
        and not event.get("last_human_audit")
    ]
    if unaudited_nulls:
        warnings.append(
            f"{len(unaudited_nulls)} null denominator cases lack last_human_audit "
            "(allowed for aggregate/null tables; not eligible for narrative spotlight): "
            + ", ".join(unaudited_nulls)
        )

    try:
        irr = load_json(IRR_REPORT)
        provenance = irr.get("coder_provenance") or {}
        mode = provenance.get("mode")
        if mode != "independent_human":
            msg = (
                f"IRR coder_provenance.mode={mode!r}; κ may be cited only as "
                "self-consistency, not independent-human reliability"
            )
            if args.strict_reliability:
                errors.append(msg)
            else:
                warnings.append(msg)
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
                errors.append(f"{variable} κ={value} is below 0.6")
    except FileNotFoundError:
        errors.append("missing analysis/inter_rater/kappa_report.json — run `make irr-kappa`")

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
