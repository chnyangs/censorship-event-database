#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Compute the evidence-tier IRR kappa after two human coders fill the packet.

This is deliberately separate from the H1 coverage/observation/attribution IRR
because codebook 4.0.0 introduced a new event-level decision rule:
`evidence_tier=attested_secondary`.
"""
from __future__ import annotations

import argparse
import csv
import json
import pathlib
import sys
from typing import Any

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from _dataset_meta import now_utc_iso, repo_relative_path  # noqa: E402

REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent
DEFAULT_PACKET = REPO_ROOT / "analysis" / "evidence_tier_irr_packet_2026_05_31.csv"
DEFAULT_JSON = REPO_ROOT / "analysis" / "evidence_tier_irr_report_2026_05_31.json"
DEFAULT_MD = REPO_ROOT / "analysis" / "evidence_tier_irr_report_2026_05_31.md"

DECISION_FIELDS = ("tier_ok", "section9_clear", "single_source_ok")
ALLOWED_VALUES = ("yes", "no", "unclear")
REQUIRED_COLUMNS = (
    "id",
    "stratum",
    "jurisdiction",
    "trigger_type",
    "sample_reason",
    "coder_a_tier_ok",
    "coder_a_section9_clear",
    "coder_a_single_source_ok",
    "coder_b_tier_ok",
    "coder_b_section9_clear",
    "coder_b_single_source_ok",
    "notes",
)


class PacketError(ValueError):
    """Raised when the evidence-tier IRR packet cannot be scored."""


def read_packet(path: pathlib.Path) -> list[dict[str, str]]:
    if not path.exists():
        raise PacketError(f"missing packet: {repo_relative_path(path)}")
    with path.open(newline="") as f:
        reader = csv.DictReader(f)
        fieldnames = tuple(reader.fieldnames or ())
        missing = [col for col in REQUIRED_COLUMNS if col not in fieldnames]
        if missing:
            raise PacketError(f"packet missing column(s): {', '.join(missing)}")
        rows = list(reader)
    if not rows:
        raise PacketError("packet has no rows")
    ids = [row["id"].strip() for row in rows]
    if any(not event_id for event_id in ids):
        raise PacketError("packet contains blank id values")
    dupes = sorted({event_id for event_id in ids if ids.count(event_id) > 1})
    if dupes:
        raise PacketError(f"packet contains duplicate id(s): {', '.join(dupes)}")
    return rows


def _validate_value(row_id: str, column: str, value: str) -> str:
    normalized = value.strip().lower()
    if normalized and normalized not in ALLOWED_VALUES:
        raise PacketError(
            f"{row_id} {column}={value!r}; expected one of "
            f"{', '.join(ALLOWED_VALUES)} or blank"
        )
    return normalized


def cohens_kappa(pairs: list[tuple[str, str]]) -> dict[str, Any]:
    coded = [(a, b) for a, b in pairs if a and b]
    if not coded:
        return {
            "kappa": None,
            "observed_agreement": None,
            "expected_agreement": None,
            "n_coded": 0,
            "label_set": [],
            "confusion": {},
            "reason": "no fully coded rows",
        }
    labels = sorted({label for pair in coded for label in pair})
    confusion = {a: {b: 0 for b in labels} for a in labels}
    for a, b in coded:
        confusion[a][b] += 1
    n = len(coded)
    observed = sum(confusion[label][label] for label in labels) / n
    marg_a = {label: sum(confusion[label].values()) / n for label in labels}
    marg_b = {label: sum(confusion[a][label] for a in labels) / n for label in labels}
    expected = sum(marg_a[label] * marg_b[label] for label in labels)
    kappa = 1.0 if expected >= 1.0 else (observed - expected) / (1.0 - expected)
    return {
        "kappa": round(kappa, 4),
        "observed_agreement": round(observed, 4),
        "expected_agreement": round(expected, 4),
        "n_coded": n,
        "label_set": labels,
        "confusion": confusion,
    }


def build_report(
    rows: list[dict[str, str]],
    *,
    packet_path: pathlib.Path = DEFAULT_PACKET,
    allow_incomplete: bool = False,
) -> dict[str, Any]:
    variables: dict[str, Any] = {}
    incomplete: dict[str, list[str]] = {}
    for field in DECISION_FIELDS:
        pairs: list[tuple[str, str]] = []
        missing_ids: list[str] = []
        for row in rows:
            row_id = row["id"].strip()
            a_value = _validate_value(row_id, f"coder_a_{field}", row.get(f"coder_a_{field}", ""))
            b_value = _validate_value(row_id, f"coder_b_{field}", row.get(f"coder_b_{field}", ""))
            if not (a_value and b_value):
                missing_ids.append(row_id)
            pairs.append((a_value, b_value))
        stats = cohens_kappa(pairs)
        stats["n_total"] = len(rows)
        stats["n_incomplete"] = len(missing_ids)
        variables[field] = stats
        if missing_ids:
            incomplete[field] = missing_ids

    if incomplete and not allow_incomplete:
        details = "; ".join(f"{field}: {len(ids)} incomplete" for field, ids in incomplete.items())
        raise PacketError(f"packet is incomplete ({details})")

    return {
        "generated_at": now_utc_iso(),
        "packet": repo_relative_path(packet_path),
        "coder_provenance": {
            "mode": "independent_human" if not incomplete else "independent_human_pending",
            "note": (
                "Computed only from filled coder_a_* and coder_b_* cells. "
                "Blank cells mean the IRR pass is not complete."
            ),
        },
        "allowed_values": list(ALLOWED_VALUES),
        "n_events": len(rows),
        "status": "complete" if not incomplete else "incomplete",
        "variables": variables,
        "incomplete_rows": incomplete,
    }


def render_markdown(report: dict[str, Any]) -> str:
    lines = [
        "# Evidence-Tier IRR Report",
        "",
        f"Generated: `{report['generated_at']}`",
        f"Status: `{report['status']}`",
        f"Coder provenance: `{report['coder_provenance']['mode']}`",
        "",
        "| variable | coded | incomplete | kappa | observed | expected | labels |",
        "| --- | ---: | ---: | ---: | ---: | ---: | --- |",
    ]
    for field, stats in report["variables"].items():
        labels = ", ".join(f"`{label}`" for label in stats.get("label_set") or [])
        kappa = "NA" if stats.get("kappa") is None else f"{stats['kappa']:.4f}"
        observed = "NA" if stats.get("observed_agreement") is None else f"{stats['observed_agreement']:.4f}"
        expected = "NA" if stats.get("expected_agreement") is None else f"{stats['expected_agreement']:.4f}"
        lines.append(
            f"| `{field}` | {stats['n_coded']} / {stats['n_total']} | "
            f"{stats['n_incomplete']} | {kappa} | {observed} | {expected} | {labels} |"
        )
    if report["incomplete_rows"]:
        lines.extend(["", "## Incomplete Rows", ""])
        for field, ids in report["incomplete_rows"].items():
            lines.append(f"- `{field}`: {', '.join(f'`{event_id}`' for event_id in ids)}")
    lines.append("")
    return "\n".join(lines)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--packet", type=pathlib.Path, default=DEFAULT_PACKET)
    parser.add_argument("--out-json", type=pathlib.Path, default=DEFAULT_JSON)
    parser.add_argument("--out-md", type=pathlib.Path, default=DEFAULT_MD)
    parser.add_argument(
        "--allow-incomplete",
        action="store_true",
        help="Validate and summarize a partially blank packet without treating it as a completed IRR pass.",
    )
    parser.add_argument("--no-write", action="store_true", help="Print status without writing report files.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        rows = read_packet(args.packet)
        report = build_report(rows, packet_path=args.packet, allow_incomplete=args.allow_incomplete)
    except PacketError as exc:
        print(f"[evidence-tier-irr] FAIL: {exc}", file=sys.stderr)
        return 1

    status = report["status"].upper()
    summary = ", ".join(
        f"{field} {stats['n_coded']}/{stats['n_total']} coded"
        for field, stats in report["variables"].items()
    )
    print(f"[evidence-tier-irr] {status}: {summary}")

    if not args.no_write and (report["status"] == "complete" or args.allow_incomplete):
        args.out_json.parent.mkdir(parents=True, exist_ok=True)
        args.out_md.parent.mkdir(parents=True, exist_ok=True)
        args.out_json.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
        args.out_md.write_text(render_markdown(report))
        print(
            f"[evidence-tier-irr] wrote {repo_relative_path(args.out_json)} "
            f"and {repo_relative_path(args.out_md)}"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
