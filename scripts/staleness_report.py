#!/usr/bin/env python3
"""Emit a staleness report based on `last_human_audit` fields.

Surfaces events whose last human adversarial audit is too old, and records
the most recent watcher activity.
"""

from __future__ import annotations

import argparse
import json
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any

import yaml


REPO_ROOT = Path(__file__).resolve().parent.parent
EVENTS_DIR = REPO_ROOT / "events"
CANDIDATE_DIR = REPO_ROOT / "candidate_triggers"
ANALYSIS_DIR = REPO_ROOT / "analysis"
STALENESS_JSON = ANALYSIS_DIR / "staleness.json"
STALENESS_MD = ANALYSIS_DIR / "staleness.md"

RED_THRESHOLD_DAYS = 90


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Staleness report for P1 events.")
    parser.add_argument("--json-out", default=str(STALENESS_JSON))
    parser.add_argument("--md-out", default=str(STALENESS_MD))
    return parser.parse_args()


def parse_date(value: Any) -> date | None:
    if not value:
        return None
    try:
        return datetime.strptime(str(value), "%Y-%m-%d").date()
    except ValueError:
        return None


def most_recent_candidate_mtime() -> datetime | None:
    if not CANDIDATE_DIR.is_dir():
        return None
    newest: datetime | None = None
    for path in CANDIDATE_DIR.rglob("*"):
        if not path.is_file() or path.name.startswith("."):
            continue
        mtime = datetime.fromtimestamp(path.stat().st_mtime, tz=timezone.utc)
        if newest is None or mtime > newest:
            newest = mtime
    return newest


def build_report(today: date) -> dict[str, Any]:
    cases: list[dict[str, Any]] = []
    for path in sorted(EVENTS_DIR.glob("*.yaml")):
        if path.name == "TEMPLATE.yaml":
            continue
        try:
            event = yaml.safe_load(path.read_text())
        except Exception as exc:  # pragma: no cover — defensive
            cases.append({"id": path.stem, "error": f"failed to parse: {exc}"})
            continue
        if not isinstance(event, dict):
            continue

        last_audit = parse_date(event.get("last_human_audit"))
        last_verified = parse_date(event.get("last_verified"))
        anchor = last_audit or last_verified
        if anchor is None:
            age_days = None
            flag = "no_audit_recorded"
        else:
            age_days = (today - anchor).days
            flag = "red" if age_days > RED_THRESHOLD_DAYS else "ok"

        cases.append(
            {
                "id": event.get("id", path.stem),
                "status": event.get("status"),
                "origin": event.get("origin"),
                "last_human_audit": str(event.get("last_human_audit")) if event.get("last_human_audit") else None,
                "last_verified": str(event.get("last_verified")) if event.get("last_verified") else None,
                "age_days": age_days,
                "flag": flag,
            }
        )

    last_agent_run = most_recent_candidate_mtime()
    return {
        "generated_at": datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z"),
        "red_threshold_days": RED_THRESHOLD_DAYS,
        "last_agent_run": last_agent_run.isoformat().replace("+00:00", "Z") if last_agent_run else None,
        "cases": cases,
    }


def render_markdown(report: dict[str, Any]) -> str:
    lines = [
        "# Staleness Report",
        "",
        f"Generated at: `{report['generated_at']}`",
        f"Red threshold: audits older than `{report['red_threshold_days']}` days.",
        f"Most recent agent activity in `candidate_triggers/`: `{report.get('last_agent_run') or 'none recorded'}`.",
        "",
        "| Event | Status | Origin | last_human_audit | last_verified | Age (days) | Flag |",
        "| --- | --- | --- | --- | --- | --- | --- |",
    ]
    for case in report["cases"]:
        if "error" in case:
            lines.append(f"| `{case['id']}` | ERROR | — | — | — | — | {case['error']} |")
            continue
        lines.append(
            "| `{id}` | `{status}` | `{origin}` | {audit} | {verified} | {age} | {flag} |".format(
                id=case["id"],
                status=case.get("status") or "—",
                origin=case.get("origin") or "—",
                audit=case.get("last_human_audit") or "—",
                verified=case.get("last_verified") or "—",
                age=case["age_days"] if case["age_days"] is not None else "—",
                flag=case["flag"],
            )
        )

    reds = [c for c in report["cases"] if c.get("flag") == "red"]
    if reds:
        lines.extend(
            [
                "",
                "## Events past the red threshold",
                "",
            ]
        )
        for c in reds:
            lines.append(f"- `{c['id']}` — {c['age_days']} days since last audit / verification.")
    return "\n".join(lines).rstrip() + "\n"


def main() -> int:
    args = parse_args()
    ANALYSIS_DIR.mkdir(parents=True, exist_ok=True)
    report = build_report(date.today())
    Path(args.json_out).write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    Path(args.md_out).write_text(render_markdown(report))
    print(f"Wrote staleness report to {args.json_out} and {args.md_out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
