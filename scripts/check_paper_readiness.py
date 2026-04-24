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
import json
import pathlib
import re
import sys
from typing import Any

import yaml


REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent
EVENTS_DIR = REPO_ROOT / "events"
PAPER_TABLES_DIR = REPO_ROOT / "analysis" / "paper_tables"
DERIVED_DIR = REPO_ROOT / "derived"
PAPER_CLAIMS = REPO_ROOT / "docs" / "paper_claims.md"

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
    return parser.parse_args()


def load_events(events_dir: pathlib.Path) -> list[dict[str, Any]]:
    events: list[dict[str, Any]] = []
    for path in sorted(events_dir.glob("*.yaml")):
        if path.name == "TEMPLATE.yaml" or path.name.startswith("_"):
            continue
        events.append(yaml.safe_load(path.read_text()))
    return events


def load_json(path: pathlib.Path) -> Any:
    if not path.exists():
        raise FileNotFoundError(path)
    return json.loads(path.read_text())


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


def main() -> int:
    args = parse_args()
    events_dir = pathlib.Path(args.events_dir)
    paper_tables_dir = pathlib.Path(args.paper_tables_dir)
    derived_dir = pathlib.Path(args.derived_dir)
    claims_path = pathlib.Path(args.claims)

    errors: list[str] = []
    warnings: list[str] = []

    events = load_events(events_dir)
    events_by_id = {event["id"]: event for event in events}

    for rel in REQUIRED_TABLES:
        path = paper_tables_dir / rel
        if not path.exists():
            errors.append(f"missing paper table artifact: {path.relative_to(REPO_ROOT)}")

    try:
        table_meta = load_json(paper_tables_dir / ".meta.json")
        if table_meta.get("event_count") != len(events):
            errors.append(
                f"paper table event_count={table_meta.get('event_count')} "
                f"but events/*.yaml count={len(events)}"
            )
    except FileNotFoundError:
        pass

    try:
        table1_rows = read_csv(paper_tables_dir / "table1_case_roles.csv")
        if len(table1_rows) != len(events):
            errors.append(
                f"table1_case_roles.csv has {len(table1_rows)} rows; expected {len(events)}"
            )
        for row in table1_rows:
            event = events_by_id.get(row.get("event_id", ""))
            if not event:
                errors.append(f"table1 has unknown event_id={row.get('event_id')}")
                continue
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
    ):
        path = paper_tables_dir / rel
        if path.exists() and has_crlf(path):
            errors.append(f"{path.relative_to(REPO_ROOT)} contains CRLF line endings")

    if claims_path.exists():
        claims = claims_path.read_text()
        for phrase in FORBIDDEN_CLAIM_PHRASES:
            if phrase in claims:
                errors.append(f"paper_claims.md contains forbidden stale phrase: {phrase}")
        required_markers = [
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

    paper_critical = [
        event["id"]
        for event in events
        if event.get("admission_tier") in {"anchor_case", "null_case"}
        and not event.get("last_human_audit")
    ]
    if paper_critical:
        msg = (
            f"{len(paper_critical)} paper-critical anchor/null cases lack "
            "last_human_audit: " + ", ".join(paper_critical)
        )
        if args.strict_audit:
            errors.append(msg)
        else:
            warnings.append(msg)

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
