#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Emit a staleness report focused on `last_human_audit` age.

The report tracks two independent dimensions and **never substitutes one for
the other** — the previous logic folded a missing audit into `last_verified`,
which silently converted "no audit has ever happened" into an `ok` flag.
That masked the very gap the report is supposed to surface.

Dimensions:
  - **audit** — based on `last_human_audit`. Missing = `no_audit_recorded`
    (NOT `ok`). This is the report's primary signal.
  - **verification** — based on `last_verified`. Missing = `no_verification_recorded`.
    Diagnostic field; does not substitute for audit age.

Each row carries both dimensions and a `summary` flag that is the worst of
the two, so a reader scanning for red rows catches both kinds of gap.
"""

from __future__ import annotations

import argparse
import json
import sys
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

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _dataset_meta import now_utc_iso, source_date_epoch_is_set, today_utc_date  # noqa: E402

RED_THRESHOLD_DAYS = 90

# Severity ordering: more-severe wins when folding audit + verification into
# the summary column. Keep "no_*_recorded" strictly worse than "red" so a
# missing audit is never masked by a merely-old one.
SEVERITY = {
    "ok": 0,
    "red": 1,
    "no_verification_recorded": 2,
    "no_audit_recorded": 3,
    "error": 4,
}


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
    if source_date_epoch_is_set():
        return None
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


def _age_and_flag(
    anchor: date | None, today: date, missing_flag: str
) -> tuple[int | None, str]:
    """Compute age + flag for a single anchor. Missing anchor returns
    (None, missing_flag) — never silently-ok."""
    if anchor is None:
        return None, missing_flag
    age = (today - anchor).days
    return age, "red" if age > RED_THRESHOLD_DAYS else "ok"


def _summary_flag(audit_flag: str, verification_flag: str) -> str:
    """Fold two independent dimensions into one row-level signal. Severity
    ordering guarantees a missing audit is never hidden behind a fresher
    `last_verified`."""
    return (
        audit_flag
        if SEVERITY.get(audit_flag, 0) >= SEVERITY.get(verification_flag, 0)
        else verification_flag
    )


def build_report(today: date) -> dict[str, Any]:
    cases: list[dict[str, Any]] = []
    for path in sorted(EVENTS_DIR.glob("*.yaml")):
        if path.name == "TEMPLATE.yaml":
            continue
        try:
            event = yaml.safe_load(path.read_text())
        except Exception as exc:  # pragma: no cover — defensive
            cases.append({
                "id": path.stem,
                "error": f"failed to parse: {exc}",
                "audit_flag": "error",
                "verification_flag": "error",
                "summary_flag": "error",
            })
            continue
        if not isinstance(event, dict):
            continue

        last_audit = parse_date(event.get("last_human_audit"))
        last_verified = parse_date(event.get("last_verified"))
        audit_age, audit_flag = _age_and_flag(last_audit, today, "no_audit_recorded")
        verif_age, verif_flag = _age_and_flag(last_verified, today, "no_verification_recorded")

        cases.append({
            "id": event.get("id", path.stem),
            "status": event.get("status"),
            "origin": event.get("origin"),
            "last_human_audit": str(event.get("last_human_audit")) if event.get("last_human_audit") else None,
            "last_verified": str(event.get("last_verified")) if event.get("last_verified") else None,
            "audit_age_days": audit_age,
            "audit_flag": audit_flag,
            "verification_age_days": verif_age,
            "verification_flag": verif_flag,
            "summary_flag": _summary_flag(audit_flag, verif_flag),
        })

    last_agent_run = most_recent_candidate_mtime()
    return {
        "generated_at": now_utc_iso(),
        "red_threshold_days": RED_THRESHOLD_DAYS,
        "flag_legend": {
            "ok": "within the red threshold",
            "red": f"older than {RED_THRESHOLD_DAYS} days",
            "no_audit_recorded": "no last_human_audit on record — event has never been through an adversarial audit",
            "no_verification_recorded": "no last_verified on record — event has never been re-verified",
            "error": "event YAML failed to parse",
        },
        "last_agent_run": last_agent_run.isoformat().replace("+00:00", "Z") if last_agent_run else None,
        "cases": cases,
    }


def _counts(cases: list[dict[str, Any]], key: str) -> dict[str, int]:
    out: dict[str, int] = {}
    for c in cases:
        v = c.get(key)
        if v is None:
            continue
        out[v] = out.get(v, 0) + 1
    return dict(sorted(out.items()))


def render_markdown(report: dict[str, Any]) -> str:
    cases = report["cases"]
    audit_counts = _counts(cases, "audit_flag")
    verif_counts = _counts(cases, "verification_flag")
    summary_counts = _counts(cases, "summary_flag")

    lines = [
        "# Staleness report",
        "",
        f"Generated at: `{report['generated_at']}`",
        f"Red threshold: audits / verifications older than `{report['red_threshold_days']}` days.",
        f"Most recent agent activity in `candidate_triggers/`: `{report.get('last_agent_run') or 'none recorded'}`.",
        "",
        "## Coverage snapshot",
        "",
        "Two dimensions tracked per event; missing values surface as explicit gaps, never masked.",
        "",
        f"- **Adversarial audit** (`last_human_audit`): {audit_counts}",
        f"- **Verification** (`last_verified`): {verif_counts}",
        f"- **Row-level summary** (worst of the two): {summary_counts}",
        "",
        "## Flag legend",
        "",
    ]
    for flag, desc in report["flag_legend"].items():
        lines.append(f"- `{flag}` — {desc}")
    lines += [
        "",
        "## Per-event table",
        "",
        "| Event | Status | Origin | last_human_audit | Audit age | Audit flag | last_verified | Verification age | Verif flag | Summary |",
        "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    for c in cases:
        if "error" in c:
            lines.append(f"| `{c['id']}` | ERROR | — | — | — | error | — | — | error | error |")
            continue
        lines.append(
            "| `{id}` | `{status}` | `{origin}` | {audit} | {aa} | {af} | {verified} | {va} | {vf} | {sf} |".format(
                id=c["id"],
                status=c.get("status") or "—",
                origin=c.get("origin") or "—",
                audit=c.get("last_human_audit") or "—",
                aa=c["audit_age_days"] if c["audit_age_days"] is not None else "—",
                af=c["audit_flag"],
                verified=c.get("last_verified") or "—",
                va=c["verification_age_days"] if c["verification_age_days"] is not None else "—",
                vf=c["verification_flag"],
                sf=c["summary_flag"],
            )
        )

    gaps = [c for c in cases if c.get("summary_flag") not in {"ok", None}]
    if gaps:
        lines += ["", "## Events flagged (any non-`ok` summary)", ""]
        for c in gaps:
            detail_bits = [f"audit={c['audit_flag']}", f"verification={c['verification_flag']}"]
            if c["audit_age_days"] is not None:
                detail_bits.append(f"audit_age={c['audit_age_days']}d")
            if c["verification_age_days"] is not None:
                detail_bits.append(f"verif_age={c['verification_age_days']}d")
            lines.append(f"- `{c['id']}` — {', '.join(detail_bits)}")
    return "\n".join(lines).rstrip() + "\n"


def main() -> int:
    args = parse_args()
    ANALYSIS_DIR.mkdir(parents=True, exist_ok=True)
    report = build_report(today_utc_date())
    Path(args.json_out).write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    Path(args.md_out).write_text(render_markdown(report))
    print(f"Wrote staleness report to {args.json_out} and {args.md_out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
