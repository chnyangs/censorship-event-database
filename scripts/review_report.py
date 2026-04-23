#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Generate a case-review report focused on robustness and completeness."""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from pathlib import Path
from typing import Any

# Allow invocation from any working directory (`python3 scripts/review_report.py`
# from the repo root would otherwise fail on the sibling import).
sys.path.insert(0, str(Path(__file__).resolve().parent))
from status_report import collect_gap_count, load_events  # noqa: E402


REPO_ROOT = Path(__file__).resolve().parent.parent
JSON_OUT_PATH = REPO_ROOT / "analysis" / "review-report.json"
MD_OUT_PATH = REPO_ROOT / "analysis" / "review-report.md"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate a case review report.")
    parser.add_argument("--json-out", default=str(JSON_OUT_PATH))
    parser.add_argument("--md-out", default=str(MD_OUT_PATH))
    return parser.parse_args()


def has_primary_sources(observation: dict[str, Any]) -> bool:
    return any(
        str(source.get("type", "")).startswith("primary_")
        for source in observation.get("sources", [])
    )


def has_two_semi_primary_sources(observation: dict[str, Any]) -> bool:
    semi_primary_count = sum(
        1
        for source in observation.get("sources", [])
        if str(source.get("type", "")).startswith("semi_primary_")
    )
    return semi_primary_count >= 2


def summarize_case(event: dict[str, Any]) -> dict[str, Any]:
    notes: list[str] = []
    blockers: list[str] = []
    next_actions: list[str] = []
    changed_observations = [
        obs
        for obs in event.get("observations", [])
        if obs.get("observation_kind") == "observed_change"
    ]
    coverage_entries = event.get("coverage", [])
    gap_marker_count = collect_gap_count(event)
    coverage_counts = Counter(entry.get("status") for entry in coverage_entries)
    changed_layer_count = len({obs.get("layer") for obs in changed_observations})

    target = event.get("target", {})
    target_kind = target.get("kind")
    trigger_citations = event.get("trigger", {}).get("citation", [])
    trigger_primary = bool(trigger_citations) and all(
        str(source.get("type", "")).startswith("primary_")
        for source in trigger_citations
    )
    target_is_concrete = (
        (target_kind == "address_set" and bool(target.get("addresses")))
        or (target_kind == "entity" and bool(target.get("entity")))
        or (target_kind == "protocol" and bool(target.get("protocol")))
        or (target_kind == "domain" and bool(target.get("canonical_domains")))
        or (target_kind == "asset" and bool(target.get("asset")))
    )
    trigger_reliability = "high" if trigger_primary and target_is_concrete else "medium"
    if trigger_reliability != "high":
        notes.append("Trigger is primary, but target scope or enumeration still looks coarse.")
        blockers.append("Tighten target enumeration or target scope before treating the trigger as settled.")
        next_actions.append("Pin down the target set more concretely in the event file.")

    observation_reliability = "high"
    if gap_marker_count > 0 or any(
        obs.get("observation_kind") == "coverage_gap"
        for obs in event.get("observations", [])
    ):
        observation_reliability = "low"
        notes.append("At least one retained observation still depends on unresolved evidence scaffolding.")
        blockers.append("Core observations still contain unresolved evidence placeholders or coverage-gap scaffolding.")
        next_actions.append("Replace placeholder notes with archived artifacts, receipts, or concrete measurement outputs.")
    elif any(not has_primary_sources(obs) for obs in changed_observations):
        if any(has_two_semi_primary_sources(obs) for obs in changed_observations):
            observation_reliability = "medium"
            notes.append("At least one changed layer is carried by semi-primary evidence rather than a primary artifact.")
            next_actions.append("Upgrade semi-primary changed-layer evidence to a primary artifact where feasible.")
        else:
            observation_reliability = "low"
            notes.append("At least one changed layer does not clearly meet the source threshold.")
            blockers.append("At least one retained changed layer does not clearly satisfy the admission source rule.")
            next_actions.append("Either strengthen the weak changed layer or drop it from observations.")

    changed_attributions = {obs.get("attribution") for obs in changed_observations}

    def _direct_is_structurally_earned(obs: dict[str, Any]) -> bool:
        """A `direct` label is earned when at least one source is primary_*.

        Methodology §2.5 / §4.1 define `direct` as "a legal or operator source
        names the target or order explicitly", which in the source taxonomy
        maps to primary_legal, primary_corporate, or primary_onchain. Two
        semi-primary sources can satisfy admission but cannot by themselves
        earn direct attribution.
        """
        return any(
            str(source.get("type", "")).startswith("primary_")
            for source in obs.get("sources", [])
        )

    direct_observations = [
        obs for obs in changed_observations if obs.get("attribution") == "direct"
    ]
    unearned_direct = [
        obs for obs in direct_observations if not _direct_is_structurally_earned(obs)
    ]

    if not changed_observations:
        attribution_reliability = "low"
        notes.append("No observed_change entries remain, so attribution cannot be evaluated.")
        blockers.append("The file does not currently retain a stable changed-layer claim.")
    elif unearned_direct:
        attribution_reliability = "medium"
        notes.append(
            "At least one direct-attribution changed layer is backed only by semi-primary sources; "
            "the direct label is not structurally earned."
        )
        blockers.append(
            "A direct-attribution changed layer lacks any primary_legal / primary_corporate / "
            "primary_onchain source."
        )
        next_actions.append(
            "Upgrade the direct-attribution changed layer with a primary source, or relabel its "
            "attribution to plausible."
        )
    elif changed_attributions <= {"direct"}:
        attribution_reliability = "high"
    elif "unknown" in changed_attributions:
        attribution_reliability = "low"
        notes.append("A retained changed layer still carries unknown attribution.")
        blockers.append("Attribution remains too weak for at least one retained changed layer.")
        next_actions.append("Re-scope or drop the changed layer whose attribution is still unknown.")
    else:
        attribution_reliability = "medium"
        notes.append("Some changed layers are plausible rather than direct trigger attributions.")
        next_actions.append("Look for operator-side or first-party artifacts that can move plausible attribution toward direct.")

    applicable_coverage = [
        entry
        for entry in coverage_entries
        if isinstance(entry, dict) and entry.get("status") != "not_applicable"
    ]
    applicable_count = len(applicable_coverage)
    measured_count = sum(1 for entry in applicable_coverage if entry.get("status") == "measured")
    partial_count = sum(
        1 for entry in applicable_coverage if entry.get("status") == "partially_measured"
    )
    not_measured_count = sum(
        1 for entry in applicable_coverage if entry.get("status") == "not_measured"
    )

    if applicable_count == 0:
        coverage_completeness = "low"
        blockers.append("Every layer is not_applicable; no coverage claim is possible.")
    elif not_measured_count == 0 and partial_count == 0:
        coverage_completeness = "high"
    elif not_measured_count == 0 and measured_count / applicable_count >= 0.5:
        coverage_completeness = "high"
        notes.append(
            "Coverage is majority-measured; some layers are only partially_measured."
        )
    elif not_measured_count == 0:
        coverage_completeness = "medium"
        notes.append(
            "No layers are explicitly unmeasured, but fewer than half are fully measured."
        )
        next_actions.append(
            "Upgrade partially_measured layers to measured, or narrow the scoped claim."
        )
    elif not_measured_count == 1:
        coverage_completeness = "medium"
        notes.append("One layer remains explicitly unmeasured.")
        next_actions.append(
            "Either measure the remaining layer or document why it is out of scope."
        )
    else:
        coverage_completeness = "low"
        notes.append("Multiple layers remain explicitly unmeasured; coverage is thin.")
        blockers.append(
            "Multiple layers remain effectively unmeasured, so the case is only complete within a narrow scope."
        )
        next_actions.append(
            "Either measure more layers or explicitly narrow the public claim for this case."
        )

    class_shape_floor = {
        "cascade": 3,
        "comparison": 1,
        "null_event": 0,
    }.get(event.get("empirical_shape"), 1)

    observations_total = len(event.get("observations") or [])

    if gap_marker_count > 0:
        case_shape_completeness = "low"
        notes.append("Retained observations still carry gap markers; case shape is not stable.")
        blockers.append("Core observations still contain unresolved evidence scaffolding.")
    elif changed_layer_count < class_shape_floor:
        case_shape_completeness = "low"
        notes.append(
            f"changed_layer_count ({changed_layer_count}) is below the floor for "
            f"empirical_shape={event.get('empirical_shape')} (floor={class_shape_floor})."
        )
        blockers.append(
            "Retained observed_change count is below the floor for this empirical_shape."
        )
    elif event.get("empirical_shape") == "null_event" and observations_total == 0:
        case_shape_completeness = "low"
        notes.append("null_event has no observations attached (neither observed_change nor observed_no_change).")
        blockers.append("null_event requires at least one observation with admission-grade sources.")
    elif event.get("status") == "admitted":
        if changed_layer_count >= class_shape_floor + 1:
            case_shape_completeness = "high"
        else:
            case_shape_completeness = "medium"
            notes.append(
                "Case is admitted and at its empirical_shape floor; shape is stable but lean."
            )
            next_actions.append(
                "Seek an additional changed-layer observation to move shape from lean to richly fleshed out."
            )
    else:
        case_shape_completeness = "medium"
        notes.append("Case shape is visible but the case is not yet admitted.")
        next_actions.append("Promote to admitted once promotion-gate criteria are met.")

    low_scores = [
        label
        for label, score in {
            "trigger_reliability": trigger_reliability,
            "observation_reliability": observation_reliability,
            "attribution_reliability": attribution_reliability,
            "coverage_completeness": coverage_completeness,
            "case_shape_completeness": case_shape_completeness,
        }.items()
        if score == "low"
    ]

    if event.get("status") == "admitted":
        if all(
            score == "high"
            for score in (
                trigger_reliability,
                observation_reliability,
                attribution_reliability,
                coverage_completeness,
                case_shape_completeness,
            )
        ):
            overall_readiness = "release_ready_complete"
        else:
            overall_readiness = "release_ready_scoped"
    elif not low_scores and gap_marker_count == 0:
        overall_readiness = "candidate_for_admission"
    elif changed_layer_count >= 1:
        overall_readiness = "working_draft"
    else:
        overall_readiness = "needs_re_scoping"

    deduped_blockers: list[str] = []
    for blocker in blockers:
        if blocker not in deduped_blockers:
            deduped_blockers.append(blocker)

    deduped_actions: list[str] = []
    for action in next_actions:
        if action not in deduped_actions:
            deduped_actions.append(action)

    return {
        "id": event.get("id"),
        "status": event.get("status"),
        "research_stratum": event.get("research_stratum"),
        "empirical_shape": event.get("empirical_shape"),
        "admission_tier": event.get("admission_tier"),
        "changed_layer_count": changed_layer_count,
        "gap_marker_count": gap_marker_count,
        "scores": {
            "trigger_reliability": trigger_reliability,
            "observation_reliability": observation_reliability,
            "attribution_reliability": attribution_reliability,
            "coverage_completeness": coverage_completeness,
            "case_shape_completeness": case_shape_completeness,
        },
        "overall_readiness": overall_readiness,
        "blockers": deduped_blockers,
        "next_actions": deduped_actions,
        "notes": notes,
    }


def build_report(events: list[dict[str, Any]]) -> dict[str, Any]:
    cases = [summarize_case(event) for event in events]
    process = {
        "event_count": len(cases),
        "status_counts": dict(Counter(case["status"] for case in cases)),
        "events_with_gap_markers": [
            case["id"] for case in cases if case["gap_marker_count"] > 0
        ],
        "release_ready_cases": [
            case["id"]
            for case in cases
            if case["overall_readiness"] in {"release_ready_complete", "release_ready_scoped"}
        ],
        "release_ready_complete_cases": [
            case["id"] for case in cases if case["overall_readiness"] == "release_ready_complete"
        ],
        "release_ready_scoped_cases": [
            case["id"] for case in cases if case["overall_readiness"] == "release_ready_scoped"
        ],
        "working_drafts": [
            case["id"] for case in cases if case["overall_readiness"] == "working_draft"
        ],
        "priority_cases": [
            case["id"]
            for case in sorted(
                cases,
                key=lambda case: (
                    case["status"] != "draft",
                    -len(case["blockers"]),
                    -case["gap_marker_count"],
                    case["id"],
                ),
            )
            if case["status"] == "draft"
        ],
        "score_distribution": {
            dimension: dict(Counter(case["scores"][dimension] for case in cases))
            for dimension in (
                "trigger_reliability",
                "observation_reliability",
                "attribution_reliability",
                "coverage_completeness",
                "case_shape_completeness",
            )
        },
    }
    return {"process": process, "cases": cases}


def render_markdown(report: dict[str, Any]) -> str:
    process = report["process"]
    lines = [
        "# Review Report",
        "",
        "This file is the operational summary for the repo's two current priorities:",
        "",
        "1. process completeness and robustness",
        "2. case-design reliability and completeness",
        "",
        "## Process",
        "",
        f"- Event count: `{process['event_count']}`",
        f"- Release-ready cases: `{len(process['release_ready_cases'])}`",
        f"- Fully complete release-ready cases: `{len(process['release_ready_complete_cases'])}`",
        f"- Scope-limited release-ready cases: `{len(process['release_ready_scoped_cases'])}`",
        f"- Working drafts: `{len(process['working_drafts'])}`",
        f"- Cases with gap markers: `{len(process['events_with_gap_markers'])}`",
        f"- Draft priority order: `{', '.join(process['priority_cases']) if process['priority_cases'] else 'none'}`",
        "",
        "## Cases",
        "",
    ]

    for case in report["cases"]:
        scores = case["scores"]
        lines.extend(
            [
                f"### `{case['id']}`",
                "",
                f"- Status: `{case['status']}`",
                f"- Readiness: `{case['overall_readiness']}`",
                f"- Trigger reliability: `{scores['trigger_reliability']}`",
                f"- Observation reliability: `{scores['observation_reliability']}`",
                f"- Attribution reliability: `{scores['attribution_reliability']}`",
                f"- Coverage completeness: `{scores['coverage_completeness']}`",
                f"- Case-shape completeness: `{scores['case_shape_completeness']}`",
            ]
        )
        for note in case["notes"]:
            lines.append(f"- Note: {note}")
        for blocker in case["blockers"]:
            lines.append(f"- Blocker: {blocker}")
        for action in case["next_actions"]:
            lines.append(f"- Next action: {action}")
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def main() -> int:
    args = parse_args()
    report = build_report(load_events())

    json_out = Path(args.json_out)
    md_out = Path(args.md_out)
    json_out.write_text(json.dumps(report, indent=2, sort_keys=True))
    md_out.write_text(render_markdown(report))
    print(f"Wrote review report to {json_out} and {md_out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
