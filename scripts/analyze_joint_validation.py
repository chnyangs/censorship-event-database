#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Two-arm analysis with explicit missingness and reference-readiness gates.

Legacy diagnostics describe stored labels only. The independent evaluation
accepts a separate unit-level CSV; an empty template produces no quality scores.
No labels, reviewer identities, or independent references are synthesized.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import math
import re
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path

import yaml

from _kappa_ci import bootstrap_ci

ROOT = Path(__file__).resolve().parent.parent
LAYERS = ("l0_network", "l1_consensus", "l3_rpc", "l4_frontend", "asset_onchain", "offramp_cex")
OUTCOMES = {"positive", "negative", "unknown"}
FIELDS = [
    "unit_id", "episode_id", "episode_family_id", "target_id", "target_address", "surface", "panel_member_id",
    "action_type", "window_start_utc", "window_end_utc", "split",
    "eligibility", "outcome_definition", "legacy_outcome_definition",
    "revised_outcome_definition", "reference_outcome_definition", "legacy_outcome",
    "revised_outcome", "reference_outcome", "reference_provenance",
    "reference_reviewer_ids", "reference_completed_at_utc", "reference_artifact",
    "legacy_query_seconds", "revised_query_seconds",
]


def ratio(n, d):
    return n / d if d else None


def missingness_summary(outcomes: list[str]) -> dict:
    """Bounds conditional on eligibility and correctness of the supplied labels."""
    if set(outcomes) - OUTCOMES:
        raise ValueError("Unknown outcomes must be explicitly labeled unknown")
    counts = Counter(outcomes)
    n = len(outcomes)
    positive, negative, unknown = (counts[label] for label in ("positive", "negative", "unknown"))
    return {
        "eligible_units": n, "positive": positive, "negative": negative, "unknown": unknown,
        "observation_fraction": ratio(positive + negative, n),
        "positive_fraction_observed_only": ratio(positive, positive + negative),
        "missing_as_zero_fraction": ratio(positive, n),
        "missingness_bounds": [ratio(positive, n), ratio(positive + unknown, n)] if n else None,
        "bound_assumptions": "Fixed supplied eligibility; observed labels correct; no assumption about missing outcomes. Not a confidence interval or a correction for unsupported labels.",
    }


def legacy_diagnostics(events_dir: Path) -> dict:
    events = []
    digest = hashlib.sha256()
    for path in sorted(events_dir.glob("*.yaml")):
        raw = path.read_bytes()
        digest.update(path.name.encode() + b"\0" + raw + b"\0")
        event = yaml.safe_load(raw)
        if isinstance(event, dict) and event.get("status") == "admitted":
            events.append(event)
    rows = []
    for layer in LAYERS:
        outcomes, statuses = [], Counter()
        for event in events:
            coverage = [c.get("status") for c in event.get("coverage", []) if c.get("layer") == layer]
            if len(coverage) > 1:
                raise ValueError(f"duplicate coverage: {event.get('id')} / {layer}")
            status = coverage[0] if coverage else "missing"
            statuses[status] += 1
            if status in {"not_applicable", "missing"}:
                continue
            if status not in {"measured", "partially_measured", "not_measured"}:
                raise ValueError(f"unrecognized coverage: {status}")
            kinds = {o.get("observation_kind") for o in event.get("observations", []) if o.get("layer") == layer}
            if status == "not_measured":
                outcome = "unknown"
            elif "observed_change" in kinds:
                outcome = "positive"
            elif "observed_no_change" in kinds:
                outcome = "negative"
            else:
                outcome = "unknown"
            outcomes.append(outcome)
        rows.append({
            "layer": layer, "registry_admitted_count": len(events),
            "legacy_not_applicable_excluded": statuses["not_applicable"],
            "undeclared_coverage_excluded": statuses["missing"],
            "coverage_label_counts": dict(statuses), **missingness_summary(outcomes),
        })
    return {
        "status": "legacy_label_sensitivity_only_not_validated_behavior",
        "source_input_hash": "sha256:" + digest.hexdigest(),
        "hash_scope": "All event YAML file names and raw bytes; not referenced evidence bodies.",
        "admitted_records": len(events), "rows": rows,
        "limitations": [
            "Eligibility is the legacy coverage label, not independent applicability validation.",
            "Positive means any coded change on a covered event-layer; mixed action stages remain unresolved.",
            "Partial observations concern named subsets, not complete layer observation.",
            "Bounds are algebraic missing-label sensitivity, not validated enforcement-rate bounds.",
            "A gap stays unknown; N/A is not recoded as a negative.",
        ],
    }


def load_units(path: Path) -> list[dict]:
    with path.open(newline="") as fh:
        reader = csv.DictReader(fh)
        missing = set(FIELDS) - set(reader.fieldnames or [])
        if missing:
            raise ValueError(f"Missing columns: {sorted(missing)}")
        rows = [{key: (row[key] or "").strip() for key in FIELDS} for row in reader]
    seen, natural_keys = set(), set()
    episode_families, family_splits = {}, {}
    for row in rows:
        uid = row["unit_id"]
        if not uid or uid in seen:
            raise ValueError(f"Missing or duplicate unit_id: {uid}")
        seen.add(uid)
        for key in ("episode_id", "episode_family_id", "target_id", "surface", "panel_member_id", "action_type", "outcome_definition"):
            if not row[key]:
                raise ValueError(f"{uid}: {key} required")
        dates = []
        for key in ("window_start_utc", "window_end_utc"):
            try:
                stamp = datetime.fromisoformat(row[key].replace("Z", "+00:00"))
                if stamp.utcoffset() is None or stamp.utcoffset().total_seconds() != 0:
                    raise ValueError("not UTC")
                dates.append(stamp)
            except ValueError as exc:
                raise ValueError(f"{uid}: {key} must be UTC") from exc
        if dates[0] > dates[1]:
            raise ValueError(f"{uid}: observation window is reversed")
        if row["target_address"] and not re.fullmatch(r"0x[0-9a-fA-F]{40}", row["target_address"]):
            raise ValueError(f"{uid}: target_address must be a canonical Ethereum hex address")
        identity = ("address", row["target_address"].lower()) if row["target_address"] else ("target", row["target_id"])
        natural_key = tuple(row[k] for k in ("episode_id", "surface", "panel_member_id", "action_type", "outcome_definition")) + (identity, *dates)
        if natural_key in natural_keys:
            raise ValueError(f"{uid}: duplicate underlying unit despite different ID")
        natural_keys.add(natural_key)
        if row["split"] not in {"pilot", "evaluation"}:
            raise ValueError(f"{uid}: split must be pilot or evaluation")
        family = row["episode_family_id"]
        if episode_families.setdefault(row["episode_id"], family) != family:
            raise ValueError(f"{uid}: one episode cannot have conflicting families")
        if family_splits.setdefault(family, row["split"]) != row["split"]:
            raise ValueError(f"{uid}: pilot family leaks into evaluation")
        if row["eligibility"] not in {"eligible", "ineligible", "unknown"}:
            raise ValueError(f"{uid}: invalid eligibility")
        for method in ("legacy", "revised", "reference"):
            outcome = row[f"{method}_outcome"]
            if outcome not in OUTCOMES:
                raise ValueError(f"{uid}: invalid {method} outcome; use explicit unknown")
            if outcome != "unknown" and row[f"{method}_outcome_definition"] != row["outcome_definition"]:
                raise ValueError(f"{uid}: unmatched {method} outcome definition/stage")
        for key in ("legacy_query_seconds", "revised_query_seconds"):
            if row[key]:
                value = float(row[key])
                if not math.isfinite(value) or value < 0:
                    raise ValueError(f"{uid}: invalid nonnegative finite query duration")
        if row["reference_outcome"] != "unknown" and row["reference_provenance"] == "independent_human_adjudication":
            reviewers = {s.strip() for s in row["reference_reviewer_ids"].split(";") if s.strip()}
            if len(reviewers) < 2 or not row["reference_artifact"]:
                raise ValueError(f"{uid}: independent reference needs >=2 reviewer IDs and an artifact locator")
            try:
                stamp = datetime.fromisoformat(row["reference_completed_at_utc"].replace("Z", "+00:00"))
                if stamp.utcoffset() is None or stamp.utcoffset().total_seconds() != 0:
                    raise ValueError("not UTC")
            except ValueError as exc:
                raise ValueError(f"{uid}: completed reference needs a UTC timestamp") from exc
    return rows


def reference_ready(row: dict) -> bool:
    # Provenance is a required external assertion, not proof of actual human work.
    return row["reference_outcome"] != "unknown" and row["reference_provenance"] == "independent_human_adjudication"


def quality_metrics(rows: list[dict], method: str) -> dict | None:
    if not rows:
        return None
    counts = Counter()
    for row in rows:
        prediction = row[f"{method}_outcome"]
        if method == "naive":
            raise ValueError("use explicit naive outcomes before scoring")
        reference = row["reference_outcome"]
        if prediction == "unknown":
            counts["abstained"] += 1
        else:
            counts["classified"] += 1
            counts["correct"] += int(prediction == reference)
            counts["tp"] += int(prediction == "positive" and reference == "positive")
            counts["fp"] += int(prediction == "positive" and reference == "negative")
            counts["tn"] += int(prediction == "negative" and reference == "negative")
            counts["fn"] += int(prediction == "negative" and reference == "positive")
    return {
        "reference_units": len(rows),
        "abstained": counts["abstained"], "classified": counts["classified"],
        "tp": counts["tp"], "fp": counts["fp"], "tn": counts["tn"], "fn": counts["fn"],
        "accuracy_on_classified": ratio(counts["correct"], counts["classified"]),
        "end_to_end_correct_fraction": ratio(counts["correct"], len(rows)),
        "unsupported_positive_fraction": ratio(counts["fp"], counts["tp"] + counts["fp"]),
        "incorrect_negative_fraction": ratio(counts["fn"], counts["tn"] + counts["fn"]),
        "scope": "Reference-ready subset only; unreviewed units remain reported separately.",
    }


def evaluate_units(rows: list[dict], n_boot: int = 2000) -> dict:
    eligible = [r for r in rows if r["split"] == "evaluation" and r["eligibility"] == "eligible"]
    groups = defaultdict(list)
    for row in eligible:
        # Never mix additions/removals, operators, surfaces or measurement objects.
        groups[(row["surface"], row["panel_member_id"], row["action_type"], row["outcome_definition"])].append(row)
    output = []
    for key, group in sorted(groups.items()):
        ready = [r for r in group if reference_ready(r)]
        common = [r for r in group if r["legacy_outcome"] != "unknown" and r["revised_outcome"] != "unknown"]
        def delta(sample):
            return sum((r["revised_outcome"] == "positive") - (r["legacy_outcome"] == "positive") for r in sample) / len(sample) if sample else None
        ci = bootstrap_ci(common, delta, n_boot=n_boot, cluster_ids=[r["episode_id"] for r in common]) if common else None
        if ci:
            ci["resampling_unit"] = "legal_episode"
        naive = [{**r, "legacy_outcome": "negative" if r["legacy_outcome"] == "unknown" else r["legacy_outcome"]} for r in ready]
        costs = {}
        for method in ("legacy", "revised"):
            durations = [float(r[f"{method}_query_seconds"]) for r in group if r[f"{method}_query_seconds"]]
            costs[method] = {"units_with_duration": len(durations), "mean_query_seconds": ratio(sum(durations), len(durations))}
        output.append({
            "surface": key[0], "panel_member_id": key[1], "action_type": key[2], "outcome_definition": key[3],
            "eligible_units": len(group), "episodes": len({r["episode_id"] for r in group}),
            "legacy": missingness_summary([r["legacy_outcome"] for r in group]),
            "revised": missingness_summary([r["revised_outcome"] for r in group]),
            "paired_change": {"common_observed_units": len(common), "revised_minus_legacy": delta(common), "cluster_bootstrap_ci": ci, "scope": "Intersection with both methods observed; descriptive, not a claim of correctness."},
            "reference_ready_units": len(ready), "reference_pending_units": len(group) - len(ready),
            "query_cost": costs,
            "quality_status": "reference_subset_only" if ready else "pending_independent_reference",
            "quality": {"legacy": quality_metrics(ready, "legacy"), "revised": quality_metrics(ready, "revised"), "naive_missing_as_zero": quality_metrics(naive, "legacy")},
        })
    ready_total = sum(g["reference_ready_units"] for g in output)
    status = ("no_evaluation_units" if not eligible else "pending_independent_reference"
              if ready_total == 0 else "partially_referenced" if ready_total < len(eligible)
              else "references_complete_for_supplied_units")
    return {
        "status": status,
        "reference_ready_units": ready_total,
        "reference_pending_units": len(eligible) - ready_total,
        "input_units": len(rows), "pilot_units_excluded": sum(r["split"] == "pilot" for r in rows),
        "unknown_eligibility_units": sum(r["split"] == "evaluation" and r["eligibility"] == "unknown" for r in rows),
        "ineligible_units": sum(r["split"] == "evaluation" and r["eligibility"] == "ineligible" for r in rows),
        "eligible_evaluation_units": len(eligible), "groups": output,
        "limitations": ["External reference provenance is declared by the input; this program cannot certify that a human actually performed review.", "Quality estimates apply to the reviewed subset; unequal review probabilities require a separately declared weighted analysis.", "Bootstrap sampling uncertainty does not resolve selection, support, or applicability errors.", "Missingness bounds condition on supplied eligibility and label correctness."],
    }


def write_template(path: Path) -> None:
    stream = io.StringIO(newline="")
    csv.DictWriter(stream, fieldnames=FIELDS, lineterminator="\n").writeheader()
    content = stream.getvalue()
    if path.exists() and path.read_text() != content:
        raise ValueError(f"Refusing to overwrite nonblank input template: {path}")
    path.write_text(content)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--events-dir", type=Path, default=ROOT / "events")
    parser.add_argument("--units", type=Path, help="Separate independent evaluation input CSV; absent means no quality metrics")
    parser.add_argument("--out-dir", type=Path, default=ROOT / "analysis/joint_validation")
    args = parser.parse_args()
    legacy = legacy_diagnostics(args.events_dir)
    units = load_units(args.units) if args.units else []
    evaluation = evaluate_units(units)
    args.out_dir.mkdir(parents=True, exist_ok=True)
    write_template(args.out_dir / "evaluation_units_template.csv")
    (args.out_dir / "legacy_missingness_sensitivity.json").write_text(json.dumps(legacy, indent=2) + "\n")
    if args.units:
        evaluation["input_csv_sha256"] = hashlib.sha256(args.units.read_bytes()).hexdigest()
    (args.out_dir / "joint_evaluation.json").write_text(json.dumps(evaluation, indent=2) + "\n")
    text = ["# Joint analysis execution", "", "Legacy missing-label sensitivity executed; independent-reference evaluation remains pending unless explicitly supplied.", "", "These are diagnostics of stored labels, not validated enforcement rates. N/A is excluded according to the old coding, not independently established applicability. Bounds assume the supplied positive/negative labels are correct and address missing labels only.", "", "| Layer | Legacy applicable | Coded change | Coded negative | Unknown | Legacy N/A excluded |", "| --- | ---: | ---: | ---: | ---: | ---: |"]
    for row in legacy["rows"]:
        text.append(f"| {row['layer']} | {row['eligible_units']} | {row['positive']} | {row['negative']} | {row['unknown']} | {row['legacy_not_applicable_excluded']} |")
    text += ["", "`legacy_missingness_sensitivity.json` includes missing-as-zero, observed-only and worst-case missing-label scenarios. None repairs unsupported existing labels or outcome-dependent applicability.", "", f"Independent evaluation input units: {evaluation['input_units']}; status: `{evaluation['status']}`. An empty CSV template does not produce model-quality scores.", "", "`evaluation_units_template.csv` requires explicit unit/episode IDs, pilot exclusion, eligibility, additions versus removals, matching outcome definitions, and reference provenance. Keep observed effect, public disclosure and source-code changes separate. Duplicate IDs or unmatched outcome definitions are rejected. Episode bootstrap retains correlated units. Quality estimates require a supplied independent-human reference, two reviewer identifiers, completion time and an artifact locator; software cannot certify these assertions.", "", "Run `python scripts/analyze_joint_validation.py` for current legacy diagnostics, or pass `--units PATH --out-dir NEW_DIRECTORY` for a separately prepared validation table. Never prefill reference fields with agent judgments."]
    (args.out_dir / "README.md").write_text("\n".join(text) + "\n")
    print(json.dumps({"legacy_records": legacy["admitted_records"], "independent_evaluation_status": evaluation["status"], "out_dir": str(args.out_dir)}))


if __name__ == "__main__":
    main()
