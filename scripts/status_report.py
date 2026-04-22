#!/usr/bin/env python3
"""Emit a compact repository status report for pilot events."""

from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

import yaml


REPO_ROOT = Path(__file__).resolve().parent.parent
EVENTS_DIR = REPO_ROOT / "events"
OUT_PATH = REPO_ROOT / "analysis" / "pilot-status.json"

# Gap markers must be narrow enough to only catch true placeholder text, not
# analytical prose. Reviewer P2 2026-04-22 flagged that the previous list
# treated "needs " / "requires " as gap markers, which fired on legitimate
# prose like "requires per-relay block-filter-list inspection" and
# "requires explicit enumeration" in follow-up / analysis notes — those are
# descriptions of future research directions, not unresolved evidence
# scaffolding. Keep only markers that are unambiguously placeholder-like.
GAP_MARKERS = (
    "placeholder",
    "fill in",
    "to be collected",
    "before admission",
    "still to be pinned",
    "tbd",
    "todo",
)

# Fields that hold analytical prose rather than retained-observation evidence;
# recursion skips these so gap markers in prose don't count against the event.
# Reviewer P2 2026-04-22.
SKIP_FIELDS_FOR_GAP_SCAN = frozenset({
    "analysis_notes",
    "scoped_claim",
    "scoped_knowledge",
    "follow_on_reaction",
    "enumeration_note",   # target enumeration prose
    "tags",
})


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate a pilot status report.")
    parser.add_argument("--out", default=str(OUT_PATH))
    return parser.parse_args()


def load_events() -> list[dict[str, Any]]:
    events = []
    for path in sorted(EVENTS_DIR.glob("*.yaml")):
        event = yaml.safe_load(path.read_text())
        event["_path"] = str(path.relative_to(REPO_ROOT))
        events.append(event)
    return events


def has_gap_marker(value: str) -> bool:
    lowered = value.lower()
    return any(marker in lowered for marker in GAP_MARKERS)


def collect_gap_count(node: Any) -> int:
    if isinstance(node, dict):
        total = 0
        for key, value in node.items():
            if key in SKIP_FIELDS_FOR_GAP_SCAN:
                continue
            total += collect_gap_count(value)
        return total
    if isinstance(node, list):
        return sum(collect_gap_count(value) for value in node)
    if isinstance(node, str):
        return 1 if has_gap_marker(node) else 0
    return 0


def event_summary(event: dict[str, Any]) -> dict[str, Any]:
    observed_change_layers = sorted(
        {
            obs["layer"]
            for obs in event.get("observations", [])
            if obs.get("observation_kind") == "observed_change"
        }
    )
    return {
        "id": event.get("id"),
        "path": event.get("_path"),
        "status": event.get("status"),
        "research_stratum": event.get("research_stratum"),
        "empirical_shape": event.get("empirical_shape"),
        "admission_tier": event.get("admission_tier"),
        "trigger_type": event.get("trigger", {}).get("type"),
        "changed_layers": observed_change_layers,
        "changed_layer_count": len(observed_change_layers),
        "gap_marker_count": collect_gap_count(event),
    }


def build_report(events: list[dict[str, Any]]) -> dict[str, Any]:
    summaries = [event_summary(event) for event in events]
    by_status = Counter(summary["status"] for summary in summaries)
    by_stratum = Counter(summary["research_stratum"] for summary in summaries)
    by_shape = Counter(summary["empirical_shape"] for summary in summaries)
    by_tier = Counter(summary["admission_tier"] for summary in summaries)
    admitted_ids = [summary["id"] for summary in summaries if summary["status"] == "admitted"]
    draft_with_gaps = [
        {
            "id": summary["id"],
            "gap_marker_count": summary["gap_marker_count"],
        }
        for summary in summaries
        if summary["status"] == "draft" and summary["gap_marker_count"] > 0
    ]

    changed_layer_histogram: dict[int, int] = defaultdict(int)
    for summary in summaries:
        changed_layer_histogram[summary["changed_layer_count"]] += 1

    return {
        "event_count": len(summaries),
        "status_counts": dict(by_status),
        "research_stratum_counts": dict(by_stratum),
        "empirical_shape_counts": dict(by_shape),
        "admission_tier_counts": dict(by_tier),
        "changed_layer_histogram": dict(sorted(changed_layer_histogram.items())),
        "admitted_ids": admitted_ids,
        "drafts_with_gaps": sorted(
            draft_with_gaps,
            key=lambda item: (-item["gap_marker_count"], item["id"]),
        ),
        "events": summaries,
    }


def main() -> int:
    args = parse_args()
    report = build_report(load_events())
    out_path = Path(args.out)
    out_path.write_text(json.dumps(report, indent=2, sort_keys=True))
    print(f"Wrote status report to {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
