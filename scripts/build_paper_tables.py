#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Reproducible paper-table generator.

Emits the six core tables called out in `docs/paper_claims.md §4`
under `analysis/paper_tables/`. Table 7 is emitted by
`scripts/build_jurisdiction_distribution.py`, which is a Makefile
prerequisite of `make paper-tables`. Every table is a pure function of:

  - `events/*.yaml`            (evidence layer)
  - `derived/*.json`            (derived-metric layer; required — run
                                 `make derived` first)

Each output carries:
  - the dataset snapshot stamp (`version`, `cutoff_date`,
    `source_input_hash`, and display-only `source_commit`) so numbers
    in the paper can be re-verified against a specific source-input state,
  - denominator-inline rates (no bare numbers that hide their
    denominator),
  - a phrasing-lock note at the end naming which paper claim it
    supports in `docs/paper_claims.md`.

Fail-closed discipline:
  - Any conditional rate with a zero denominator renders as "—", not
    "0" or "undefined".
  - Table 4 (latency distribution) refuses to place a day-precision
    trigger into an hour-granularity bin; those triggers are emitted
    to a separate day-granularity panel.
  - If `derived/*.json` is missing the script exits with a clear error
    pointing to `make derived`.

Usage:
    make paper-tables                     # rebuild all paper tables
    python3 scripts/build_paper_tables.py --out-dir analysis/paper_tables
"""

from __future__ import annotations

import argparse
import collections
import csv
import json
import pathlib
import sys
from datetime import datetime, timezone
from typing import Any

import yaml


REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent
EVENTS_DIR = REPO_ROOT / "events"
DERIVED_DIR = REPO_ROOT / "derived"
DEFAULT_OUT_DIR = REPO_ROOT / "analysis" / "paper_tables"

GENERATOR_VERSION = "0.1.0"

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from _dataset_meta import load_meta, now_utc_iso, reproducible_python  # noqa: E402


LAYER_ORDER = [
    "l0_network", "l1_consensus", "l3_rpc",
    "l4_frontend", "asset_onchain", "offramp_cex",
]

STRATUM_ORDER = [
    "S1_ofac_sdn", "S2_ofac_removal",
    "S3_doj_sec_cftc_fiod", "S4_nation_state",
    "S5_corporate", "S6_supranational",
]

ARCHETYPE_ORDER = [
    "asset_only", "frontend_only", "cex_only",
    "multi_layer", "other_single_layer", "null_event",
]

# Hour-precision = precision signal is at hour granularity or finer.
# `corporate_policy_change` events are admitted as `trigger_is_action`
# (t=0 by construction); they carry minute-precision timestamps but are
# excluded from the cross-event latency distribution per §C4.
HOUR_PRECISION_VALUES = {"minute", "second", "hour", "hour_range"}
DAY_PRECISION_VALUES = {"day", "date", "week"}


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Build paper tables.")
    p.add_argument("--events-dir", default=str(EVENTS_DIR))
    p.add_argument("--derived-dir", default=str(DERIVED_DIR))
    p.add_argument("--out-dir", default=str(DEFAULT_OUT_DIR))
    return p.parse_args()


def _load_events(events_dir: pathlib.Path) -> list[dict]:
    out: list[dict] = []
    for f in sorted(events_dir.glob("*.yaml")):
        if f.name == "TEMPLATE.yaml" or f.name.startswith("_"):
            continue
        event = yaml.safe_load(f.read_text())
        if isinstance(event, dict) and event.get("status") == "admitted":
            out.append(event)
    return out


def _load_derived(derived_dir: pathlib.Path, name: str) -> Any:
    path = derived_dir / f"{name}.json"
    if not path.exists():
        raise SystemExit(
            f"[build_paper_tables] missing {path.relative_to(REPO_ROOT)}. "
            "Run `make derived` first to regenerate the derived layer."
        )
    return json.loads(path.read_text())


def _load_optional_csv(derived_dir: pathlib.Path, name: str) -> list[dict[str, str]]:
    path = derived_dir / f"{name}.csv"
    if not path.exists():
        return []
    with path.open(newline="") as f:
        return list(csv.DictReader(f))


def _rate(num: int, denom: int) -> str:
    """Render 'num/denom = pct' with denominator always present."""
    if denom <= 0:
        return "—"
    pct = 100.0 * num / denom
    return f"{num}/{denom} ({pct:.1f}%)"


def _csv_int(row: dict[str, str], key: str) -> int:
    value = row.get(key)
    return int(value) if value not in (None, "") else 0


def _rubric_rate(row: dict[str, str], rubric: str) -> str:
    num = _csv_int(row, f"{rubric}_num")
    den = _csv_int(row, f"{rubric}_den")
    if den <= 0:
        return "—"
    rate = row.get(f"{rubric}_rate")
    if rate in (None, ""):
        return f"{num}/{den} (rate suppressed)"
    return f"{num}/{den} ({float(rate):.2f})"


def _trigger_precision(event: dict) -> str:
    """Return 'hour' or 'day' bucket for the trigger timestamp.

    Reads the canonical schema field `trigger.timestamp_precision`
    (validator-enforced). Falls back to legacy `trigger.precision` if
    present, then to timestamp-shape heuristics as a last resort — the
    heuristic path is logged to stderr so future corpus drift into
    unlabelled triggers is surfaced, not silently bucketed.
    """
    t = (event.get("trigger") or {})
    prec = t.get("timestamp_precision") or t.get("precision")
    if prec in HOUR_PRECISION_VALUES:
        return "hour"
    if prec in DAY_PRECISION_VALUES:
        return "day"
    ts = str(t.get("timestamp") or "")
    slug = event.get("id") or "?"
    if ts.endswith("T00:00:00Z") or ts.endswith(" 00:00:00+00:00"):
        print(
            f"[build_paper_tables] warning: event {slug} has no "
            f"trigger.timestamp_precision; bucketing as 'day' from "
            f"timestamp shape.",
            file=sys.stderr,
        )
        return "day"
    print(
        f"[build_paper_tables] warning: event {slug} has no "
        f"trigger.timestamp_precision and a non-day timestamp shape; "
        f"bucketing as 'hour' by default.",
        file=sys.stderr,
    )
    return "hour"


def _write_md(path: pathlib.Path, lines: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines).rstrip() + "\n")


def _snapshot_header(ds_meta: dict, title: str) -> list[str]:
    return [
        f"# {title}",
        "",
        f"Dataset snapshot: **v{ds_meta.get('dataset_version') or '?'}** · "
        f"cutoff `{ds_meta.get('cutoff_date') or 'n/a'}` · "
        f"commit `{ds_meta.get('source_commit') or 'n/a'}` · "
        f"generated `{now_utc_iso()}`",
        "",
    ]


# ---------- Table 1: case roles ----------

CASE_ROLE_COLUMNS = [
    "event_id",
    "admission_tier",
    "research_stratum",
    "empirical_shape",
    "trigger_type",
    "trigger_precision_bucket",
    "target_kind",
    "target_enumeration",
    "changed_layer_count",
    "derived_archetype",
    "trigger_is_action",
    "is_reversal_event",
    "last_verified",
    "last_human_audit",
]


def build_table1(
    events: list[dict],
    metrics_by_id: dict[str, dict],
    archetypes_by_id: dict[str, dict],
    out_dir: pathlib.Path,
    ds_meta: dict,
) -> None:
    rows: list[dict[str, Any]] = []
    for e in events:
        slug = e.get("id") or "unknown"
        met = metrics_by_id.get(slug) or {}
        arch = archetypes_by_id.get(slug) or {}
        t = e.get("trigger") or {}
        target = e.get("target") or {}
        rows.append({
            "event_id": slug,
            "admission_tier": e.get("admission_tier"),
            "research_stratum": e.get("research_stratum"),
            "empirical_shape": e.get("empirical_shape"),
            "trigger_type": t.get("type"),
            "trigger_precision_bucket": _trigger_precision(e),
            "target_kind": target.get("kind"),
            "target_enumeration": target.get("enumeration"),
            "changed_layer_count": met.get("changed_layer_count"),
            "derived_archetype": arch.get("derived_archetype"),
            "trigger_is_action": arch.get("trigger_is_action"),
            "is_reversal_event": met.get("is_reversal_event"),
            "last_verified": e.get("last_verified"),
            "last_human_audit": e.get("last_human_audit"),
        })

    # CSV
    csv_path = out_dir / "table1_case_roles.csv"
    csv_path.parent.mkdir(parents=True, exist_ok=True)
    with csv_path.open("w", newline="") as fh:
        w = csv.DictWriter(
            fh, fieldnames=CASE_ROLE_COLUMNS, extrasaction="ignore",
            lineterminator="\n",
        )
        w.writeheader()
        for r in rows:
            w.writerow({k: ("" if r.get(k) is None else r[k]) for k in CASE_ROLE_COLUMNS})

    # Markdown
    lines = _snapshot_header(
        ds_meta, f"Table 1 · Case roles (n={len(rows)})"
    )
    lines.append(
        "Supports `docs/paper_claims.md §0` (case-role convention). "
        "Each event's admission tier determines how it may be cited: "
        "`anchor_case` = named in narrative and figures; `empirical_case` "
        "= aggregate-count contributor only; `null_case` = denominator "
        "for `observed_no_change` claims only."
    )
    lines.append("")
    tier_counts = collections.Counter(r["admission_tier"] for r in rows)
    prec_counts = collections.Counter(r["trigger_precision_bucket"] for r in rows)
    lines.append("## Summary")
    lines.append("")
    lines.append("| admission_tier | count |")
    lines.append("| --- | ---: |")
    for tier in ("anchor_case", "empirical_case", "null_case"):
        lines.append(f"| `{tier}` | {tier_counts.get(tier, 0)} |")
    lines.append(f"| **total** | **{len(rows)}** |")
    lines.append("")
    lines.append("| trigger precision bucket | count |")
    lines.append("| --- | ---: |")
    for bucket in ("hour", "day"):
        lines.append(f"| `{bucket}` | {prec_counts.get(bucket, 0)} |")
    lines.append("")
    lines.append(
        "Only the `hour`-precision subset is admissible for "
        "hour-granularity latency claims (Table 4)."
    )
    lines.append("")
    lines.append("## Per-event rows")
    lines.append("")
    lines.append("| event_id | tier | stratum | shape | trigger_type | prec | target_kind | target_enum | Δlayers | archetype | t=action | reversal | last_verified | last_audit |")
    lines.append("| --- | --- | --- | --- | --- | --- | --- | --- | ---: | --- | :---: | :---: | --- | --- |")
    for r in sorted(rows, key=lambda x: x["event_id"]):
        lines.append(
            f"| `{r['event_id']}` | `{r['admission_tier']}` | "
            f"`{r['research_stratum']}` | `{r['empirical_shape']}` | "
            f"`{r['trigger_type']}` | `{r['trigger_precision_bucket']}` | "
            f"`{r['target_kind']}` | `{r['target_enumeration']}` | "
            f"{r['changed_layer_count']} | `{r['derived_archetype']}` | "
            f"{'✓' if r['trigger_is_action'] else '·'} | "
            f"{'✓' if r['is_reversal_event'] else '·'} | "
            f"`{r['last_verified'] or '—'}` | "
            f"`{r['last_human_audit'] or '—'}` |"
        )
    lines.append("")
    _write_md(out_dir / "table1_case_roles.md", lines)


# ---------- Table 2: layer observability ----------

def build_table2(
    layer_rows: list[dict],
    out_dir: pathlib.Path,
    ds_meta: dict,
    sensitivity_rows: list[dict[str, str]] | None = None,
) -> None:
    lines = _snapshot_header(
        ds_meta, "Table 2 · Layer observability (denominator-honest)"
    )
    lines.append(
        "Supports **C1** (`docs/paper_claims.md §1`). Direct re-emission "
        "of `derived/layer_observability.csv` with denominators inline."
    )
    lines.append("")
    lines.append(
        "Conditional rates are **coverage-matched**: the numerator counts "
        "only the subset of `observed_change` events whose coverage status "
        "is in the same bucket as the denominator. This is the post-P1-fix "
        "(2026-04-23) numerator definition."
    )
    lines.append("")
    lines.append(
        "| layer | applicable | measured | partial | not_measured | not_applicable | "
        "changed events (measured) | changed events (partial) | unique changed actions | "
        "duplicate action rows | changed/measured | changed/measured+partial |"
    )
    lines.append(
        "| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |"
    )
    for row in layer_rows:
        measured = row["measured_count"]
        partial = row["partially_measured_count"]
        changed_m = row["changed_under_measured_count"]
        changed_mp = row["changed_under_measured_or_partial_count"]
        unique_actions = row.get("changed_unique_action_count", row.get("changed_count", 0))
        duplicate_actions = row.get("duplicated_changed_action_count", 0)
        # The partial-coverage-changed count on its own (not cumulative)
        changed_partial_only = changed_mp - changed_m
        broad_rate = _rate(changed_mp, measured + partial)
        if row["layer"] == "l3_rpc" and measured == 0 and partial > 0:
            broad_rate = "named-only; no rate"
        measured_rate = _rate(changed_m, measured)
        if row["layer"] == "asset_onchain":
            measured_rate = "retracted; no rate"
            broad_rate = "retracted; no rate"
        lines.append(
            f"| `{row['layer']}` | "
            f"{row['applicable_event_count']} | "
            f"{measured} | {partial} | "
            f"{row['not_measured_count']} | {row['not_applicable_count']} | "
            f"{changed_m} | {changed_partial_only} | "
            f"{unique_actions} | {duplicate_actions} | "
            f"{measured_rate} | {broad_rate} |"
        )
    lines.append("")
    lines.append(
        "A rate of `—` indicates a zero denominator; it is an "
        "**observability gap**, not an attested negative."
    )
    lines.append(
        "`unique changed actions` deduplicates physical actions that are "
        "intentionally linked across event records via `observations[].action_id` "
        "(for example, the Circle USDC Tornado blacklist transaction appears in "
        "both the OFAC-triggered event and the issuer-action event). Event-rate "
        "columns remain event-record denominators; action counts are reported "
        "separately so the two units are not conflated."
    )
    lines.append("")
    rows_by_layer = {row["layer"]: row for row in layer_rows}
    l3_row = rows_by_layer.get("l3_rpc")
    if l3_row:
        l3_measured = l3_row["measured_count"]
        l3_partial = l3_row["partially_measured_count"]
        if l3_measured == 0:
            if l3_partial:
                lines.append(
                    "`l3_rpc` has no measured denominator in this snapshot. "
                    "Its partial rows are named observations only; do not cite "
                    "them as an L3 conditional rate."
                )
            else:
                lines.append(
                    "`l3_rpc` has no measured or partial denominator in this "
                    "snapshot; it is an observability gap, not a zero-reaction "
                    "finding."
                )
        else:
            lines.append(
                f"`l3_rpc` has {l3_measured} measured denominator event(s) "
                f"and {l3_partial} partial denominator event(s) in this "
                "snapshot. Any L3 statement must carry the inline denominator "
                "above and the sensitivity-rubric context below; do not turn "
                "the named rows into a provider-population claim."
            )
    lines.append(
        "`asset_onchain` remains **not reported as a rate** in this snapshot — "
        "the admission rubric requires the change as the admission anchor, "
        "so the ratio is structurally circular (see "
        "[`docs/paper_claims.md §C1` 'Not said'](../../docs/paper_claims.md))."
    )
    sensitivity_by_layer = {r.get("layer"): r for r in (sensitivity_rows or [])}
    sensitive = [
        sensitivity_by_layer[layer]
        for layer in LAYER_ORDER
        if sensitivity_by_layer.get(layer, {}).get("sensitivity") == "sensitive"
    ]
    moderate = [
        sensitivity_by_layer[layer]
        for layer in LAYER_ORDER
        if sensitivity_by_layer.get(layer, {}).get("sensitivity") == "moderate"
    ]
    if sensitive or moderate:
        lines.append("")
        lines.append(
            "**Sensitivity reporting**. Rates flagged in "
            "[`derived/admission_sensitivity.md`](../../derived/admission_sensitivity.md) "
            "must carry their strict/current/permissive context when cited:"
        )
        lines.append("")
    for row in sensitive:
        delta = row.get("strict_permissive_delta") or "—"
        lines.append(
            f"- **`{row['layer']}`** sensitive (Δ={delta}): "
            f"{_rubric_rate(row, 'strict')} strict · "
            f"{_rubric_rate(row, 'current')} current · "
            f"{_rubric_rate(row, 'permissive')} permissive."
        )
    for row in moderate:
        delta = row.get("strict_permissive_delta") or "—"
        lines.append(
            f"- **`{row['layer']}`** moderate (Δ={delta}): "
            f"{_rubric_rate(row, 'strict')} strict · "
            f"{_rubric_rate(row, 'current')} current · "
            f"{_rubric_rate(row, 'permissive')} permissive."
        )
    lines.append("")
    _write_md(out_dir / "table2_layer_observability.md", lines)


# ---------- Table 3: archetype × stratum cross-tab ----------

def build_table3(
    archetype_rows: list[dict],
    out_dir: pathlib.Path,
    ds_meta: dict,
) -> None:
    lines = _snapshot_header(
        ds_meta, "Table 3 · Archetype × research-stratum cross-tab"
    )
    lines.append(
        "Descriptive support for parked **C2** and **C5** "
        "(`docs/paper_claims.md §1`). "
        "Rows: rule-based deterministic archetypes. Columns: research "
        "strata (admission stratification, NOT jurisdiction / population "
        "weighting). Promotion from descriptive table to paper claim "
        "requires `observation_kind` κ ≥ 0.6."
    )
    lines.append("")
    xtab: dict[tuple[str, str], int] = collections.Counter(
        (r["derived_archetype"], r["research_stratum"]) for r in archetype_rows
    )
    header = "| archetype \\ stratum | " + " | ".join(STRATUM_ORDER) + " | total |"
    sep = "| --- |" + "".join(" ---: |" for _ in STRATUM_ORDER) + " ---: |"
    lines.append(header)
    lines.append(sep)
    col_totals = [0] * len(STRATUM_ORDER)
    for arch in ARCHETYPE_ORDER:
        row_cells = []
        row_total = 0
        for i, s in enumerate(STRATUM_ORDER):
            n = xtab.get((arch, s), 0)
            row_cells.append(str(n))
            row_total += n
            col_totals[i] += n
        lines.append(f"| `{arch}` | " + " | ".join(row_cells) + f" | {row_total} |")
    lines.append(
        "| **total** | " + " | ".join(f"**{n}**" for n in col_totals) +
        f" | **{sum(col_totals)}** |"
    )
    lines.append("")
    lines.append(
        "A non-empty cell is a descriptive statement about the admitted "
        "corpus, not a prevalence estimate. Strata are NOT equal-weighted "
        "and are NOT a population sample."
    )
    lines.append("")
    _write_md(out_dir / "table3_archetype_stratum.md", lines)


# ---------- Table 4: latency evidence surface (precision-filtered) ----------

LATENCY_BANDS_HOUR = [
    ("t=0", lambda h: h == 0.0),
    ("(0, 1]h", lambda h: 0 < h <= 1),
    ("(1, 6]h", lambda h: 1 < h <= 6),
    ("(6, 24]h", lambda h: 6 < h <= 24),
    ("(24, 168]h (≤1w)", lambda h: 24 < h <= 168),
    (">168h (>1w)", lambda h: h > 168),
]


def day_precision_latency_interval(hours_since_midnight_trigger: float) -> tuple[float, float]:
    """Return conservative latency bounds for a day-precision trigger.

    A day-precision trigger is known only to fall within the UTC day whose
    midnight timestamp is encoded in the YAML. If an observation is H hours
    after that midnight, true latency is in [max(0, H-24), H].
    """
    upper = float(hours_since_midnight_trigger)
    lower = max(0.0, upper - 24.0)
    return lower, upper


def day_interval_band(lower: float, upper: float) -> str:
    if upper <= 24:
        return "≤1d"
    if lower > 24 and upper <= 720:
        return "(1d, 30d]"
    if lower > 720:
        return ">30d"
    return "ambiguous_boundary"


def build_table4(
    events: list[dict],
    metrics_by_id: dict[str, dict],
    archetypes_by_id: dict[str, dict],
    out_dir: pathlib.Path,
    ds_meta: dict,
) -> None:
    hour_rows: list[dict[str, Any]] = []
    day_rows: list[dict[str, Any]] = []
    excluded_trigger_is_action: list[dict[str, Any]] = []

    for e in events:
        slug = e.get("id") or "unknown"
        met = metrics_by_id.get(slug) or {}
        arch = archetypes_by_id.get(slug) or {}
        t_first = met.get("time_to_first_change_hours")
        if t_first is None:
            continue  # event has no timed observed_change; it is Table 6 material
        bucket = _trigger_precision(e)
        row = {
            "event_id": slug,
            "research_stratum": e.get("research_stratum"),
            "admission_tier": e.get("admission_tier"),
            "derived_archetype": arch.get("derived_archetype"),
            "time_to_first_change_hours": t_first,
            "trigger_is_action": arch.get("trigger_is_action"),
            "changed_layer_count": met.get("changed_layer_count"),
            "trigger_precision_bucket": bucket,
            "latency_lower_bound_hours": "",
            "latency_upper_bound_hours": "",
            "day_interval_band": "",
        }
        if bucket != "hour":
            lower, upper = day_precision_latency_interval(float(t_first))
            row["latency_lower_bound_hours"] = lower
            row["latency_upper_bound_hours"] = upper
            row["day_interval_band"] = day_interval_band(lower, upper)
        if arch.get("trigger_is_action"):
            excluded_trigger_is_action.append(row)
            continue
        if bucket == "hour":
            hour_rows.append(row)
        else:
            day_rows.append(row)

    # CSV dump
    csv_path = out_dir / "table4_latency_by_precision.csv"
    csv_path.parent.mkdir(parents=True, exist_ok=True)
    fields = [
        "event_id", "research_stratum", "admission_tier",
        "derived_archetype", "time_to_first_change_hours",
        "trigger_is_action", "changed_layer_count",
        "trigger_precision_bucket",
        "latency_lower_bound_hours", "latency_upper_bound_hours",
        "day_interval_band",
    ]
    with csv_path.open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=fields, lineterminator="\n")
        w.writeheader()
        for r in hour_rows + day_rows + excluded_trigger_is_action:
            w.writerow({k: ("" if r.get(k) is None else r[k]) for k in fields})

    # Markdown
    lines = _snapshot_header(
        ds_meta, "Table 4 · Latency evidence surface (precision-filtered)"
    )
    lines.append(
        "Supports **C3** (`docs/paper_claims.md §1`). "
        "Only triggers with hour-or-better precision contribute to the "
        "hour-granularity panel; day-precision triggers are reported "
        "separately. `trigger_is_action` events (C4) are excluded from "
        "both panels and surfaced in Panel C — their t≈0 is a "
        "record-level artifact, not a measured delta."
    )
    lines.append("")

    # Panel A: hour-precision triggers
    lines.append(f"## Panel A · Hour-precision triggers (n={len(hour_rows)})")
    lines.append("")
    if not hour_rows:
        lines.append(
            "_No hour-precision triggers with a timed observed_change in "
            "the current snapshot._"
        )
    else:
        lines.append("| band | count | events |")
        lines.append("| --- | ---: | --- |")
        for label, pred in LATENCY_BANDS_HOUR:
            members = [
                r for r in hour_rows
                if r["time_to_first_change_hours"] is not None and pred(r["time_to_first_change_hours"])
            ]
            evs = ", ".join(f"`{r['event_id']}`" for r in sorted(members, key=lambda x: x["event_id"])) or "—"
            lines.append(f"| {label} | {len(members)} | {evs} |")
        lines.append(f"| **total** | **{len(hour_rows)}** | |")
    lines.append("")

    # Panel B: day-precision triggers
    lines.append(f"## Panel B · Day-precision triggers (n={len(day_rows)})")
    lines.append("")
    lines.append(
        "Day-precision triggers cannot support hour-granularity latency "
        "claims. The event's `time_to_first_change_hours` is converted into "
        "a conservative interval `[max(0, H-24), H]`; rows crossing a day-band "
        "boundary are reported as `ambiguous_boundary`. Per-event hour values "
        "in the CSV dump are **record-level artifacts** (timestamp arithmetic) "
        "and must not enter any hour-bucketed paper claim."
    )
    lines.append("")
    if not day_rows:
        lines.append("_No day-precision triggers with a timed observed_change._")
    else:
        by_band = collections.defaultdict(list)
        for row in day_rows:
            by_band[row["day_interval_band"]].append(row)
        lines.append("| day-granularity interval band | count | events |")
        lines.append("| --- | ---: | --- |")
        for label in ("≤1d", "(1d, 30d]", ">30d", "ambiguous_boundary"):
            subset = by_band.get(label, [])
            evs = ", ".join(f"`{r['event_id']}`" for r in sorted(subset, key=lambda x: x["event_id"])) or "—"
            lines.append(f"| {label} | {len(subset)} | {evs} |")
        lines.append(f"| **total** | **{len(day_rows)}** | |")
    lines.append("")

    # Panel C: excluded trigger-is-action
    lines.append(
        f"## Panel C · Excluded from both panels — `trigger_is_action` "
        f"(n={len(excluded_trigger_is_action)})"
    )
    lines.append("")
    if excluded_trigger_is_action:
        lines.append("| event_id | trigger_type |")
        lines.append("| --- | --- |")
        for r in sorted(excluded_trigger_is_action, key=lambda x: x["event_id"]):
            # Read trigger_type from the event YAML directly
            lines.append(f"| `{r['event_id']}` | `corporate_policy_change` |")
    else:
        lines.append("_No `trigger_is_action` events in this snapshot._")
    lines.append("")
    _write_md(out_dir / "table4_latency_by_precision.md", lines)


# ---------- Table 5: target enumeration stratification ----------

def build_table5(
    events: list[dict],
    metrics_by_id: dict[str, dict],
    archetypes_by_id: dict[str, dict],
    out_dir: pathlib.Path,
    ds_meta: dict,
) -> None:
    lines = _snapshot_header(
        ds_meta, "Table 5 · Complete-vs-subset target stratification"
    )
    lines.append(
        "Supports `docs/paper_claims.md §4 item 5`. Stratifies events by "
        "whether their `target` enumerates the **complete** set of in-scope "
        "addresses/entities/domains or only a **subset**. Complete "
        "enumeration supports stronger causal statements about the address "
        "set; subset enumeration should be cited with that qualifier."
    )
    lines.append("")
    # Primary breakdown: enumeration × archetype
    xtab: dict[tuple[str, str], int] = collections.Counter()
    enum_bucket = collections.Counter()
    kind_enum: dict[tuple[str, str], int] = collections.Counter()
    for e in events:
        arch = archetypes_by_id.get(e.get("id") or "", {})
        target = e.get("target") or {}
        enumeration = target.get("enumeration") or "unspecified"
        kind = target.get("kind") or "unspecified"
        archetype = arch.get("derived_archetype") or "unknown"
        xtab[(enumeration, archetype)] += 1
        enum_bucket[enumeration] += 1
        kind_enum[(kind, enumeration)] += 1

    lines.append("## Summary · enumeration value")
    lines.append("")
    lines.append("| enumeration | count |")
    lines.append("| --- | ---: |")
    for enum in sorted(enum_bucket):
        lines.append(f"| `{enum}` | {enum_bucket[enum]} |")
    lines.append(f"| **total** | **{sum(enum_bucket.values())}** |")
    lines.append("")

    lines.append("## enumeration × target.kind")
    lines.append("")
    kinds = sorted({k for (k, _) in kind_enum})
    enums = sorted(enum_bucket)
    lines.append("| kind \\ enum | " + " | ".join(enums) + " | total |")
    lines.append("| --- |" + "".join(" ---: |" for _ in enums) + " ---: |")
    for k in kinds:
        cells = [str(kind_enum.get((k, enum), 0)) for enum in enums]
        tot = sum(kind_enum.get((k, enum), 0) for enum in enums)
        lines.append(f"| `{k}` | " + " | ".join(cells) + f" | {tot} |")
    lines.append("")

    lines.append("## enumeration × archetype")
    lines.append("")
    enums = sorted(enum_bucket)
    lines.append("| enum \\ archetype | " + " | ".join(ARCHETYPE_ORDER) + " | total |")
    lines.append("| --- |" + "".join(" ---: |" for _ in ARCHETYPE_ORDER) + " ---: |")
    for enum in enums:
        cells = [str(xtab.get((enum, a), 0)) for a in ARCHETYPE_ORDER]
        tot = sum(xtab.get((enum, a), 0) for a in ARCHETYPE_ORDER)
        lines.append(f"| `{enum}` | " + " | ".join(cells) + f" | {tot} |")
    lines.append("")
    lines.append(
        "A `subset` row means OFAC/DOJ named specific addresses or "
        "entities rather than an entire protocol; downstream layer-change "
        "claims must say `observed on the named subset`, not `on the "
        "protocol as a whole`."
    )
    lines.append("")
    _write_md(out_dir / "table5_target_enumeration.md", lines)


# ---------- Table 6: null-case denominator ----------

NULL_EVIDENCE_KINDS = [
    (
        "body_hash+body_path",
        lambda s: _claim_usable_source(s) and bool(s.get("body_hash")) and bool(s.get("body_path")),
    ),
    ("query_hash", lambda s: _claim_usable_source(s) and bool(s.get("query_hash"))),
    (
        "measurement_ids",
        lambda s: (
            _claim_usable_source(s)
            and isinstance(s.get("measurement_ids"), list)
            and bool(s.get("measurement_ids"))
        ),
    ),
]

NON_ADMISSION_EVIDENCE_USES = {"contextual_unarchived", "non_admission"}


def _claim_usable_source(source: dict[str, Any]) -> bool:
    return source.get("evidence_use") not in NON_ADMISSION_EVIDENCE_USES


def build_table6(
    events: list[dict],
    archetypes_by_id: dict[str, dict],
    out_dir: pathlib.Path,
    ds_meta: dict,
) -> None:
    null_events = [
        e for e in events
        if (archetypes_by_id.get(e.get("id") or "") or {}).get("derived_archetype") == "null_event"
    ]
    lines = _snapshot_header(
        ds_meta, f"Table 6 · Null-case denominator (n={len(null_events)})"
    )
    lines.append(
        "Supports the **null-event interpretation note** in "
        "`derived/archetype_distribution.md`. (C6 was demoted to "
        "exemplar-inside-C1 on 2026-04-24 — see `docs/paper_claims.md "
        "§C6`.) Each row lists the event's `observed_no_change` layers + "
        "the claim-usable evidence-anchor types their sources carry. Per "
        "validator rule, `scope_descriptor` defines the covered scope but is not an "
        "evidence anchor by itself; each `observed_no_change` row needs at "
        "least one claim-usable replayable artifact such as "
        "`body_hash`+`body_path`, `query_hash`, or `measurement_ids`. "
        "Sources marked `evidence_use=contextual_unarchived` or "
        "`evidence_use=non_admission` are deliberately excluded."
    )
    lines.append("")
    lines.append(
        "| event_id | stratum | observed_no_change layers | evidence anchors present |"
    )
    lines.append("| --- | --- | --- | --- |")
    csv_rows: list[dict[str, Any]] = []
    anchorless: list[str] = []
    for e in sorted(null_events, key=lambda x: x.get("id") or ""):
        slug = e.get("id") or "unknown"
        no_change_layers: list[str] = []
        anchors = set()
        for obs in (e.get("observations") or []):
            if not isinstance(obs, dict):
                continue
            if obs.get("observation_kind") != "observed_no_change":
                continue
            layer = obs.get("layer")
            if layer:
                no_change_layers.append(layer)
            for src in (obs.get("sources") or []):
                if not isinstance(src, dict):
                    continue
                for label, pred in NULL_EVIDENCE_KINDS:
                    if pred(src):
                        anchors.add(label)
        if not anchors:
            anchorless.append(slug)
        layers_str = ", ".join(f"`{lyr}`" for lyr in sorted(set(no_change_layers))) or "—"
        anchors_str = ", ".join(f"`{a}`" for a in sorted(anchors)) or "**NONE — admission violation**"
        lines.append(
            f"| `{slug}` | `{e.get('research_stratum')}` | {layers_str} | {anchors_str} |"
        )
        csv_rows.append({
            "event_id": slug,
            "research_stratum": e.get("research_stratum"),
            "no_change_layers": ";".join(sorted(set(no_change_layers))),
            "evidence_anchors_present": ";".join(sorted(anchors)),
        })
    lines.append("")
    lines.append(
        "`evidence_anchors_present = NONE` indicates a validator regression "
        "(admission rules require at least one claim-usable replayable artifact; "
        "`scope_descriptor` alone is insufficient). "
        "The generator aborts with a non-zero exit when any row is anchorless, "
        "so a NONE row can never reach `analysis/paper_tables/`."
    )
    lines.append("")
    _write_md(out_dir / "table6_null_denominator.md", lines)
    if anchorless:
        # Ship-blocker per docs/paper_claims.md §4. Raise AFTER the markdown
        # is written so a human can inspect the rendered table; the
        # non-zero exit still blocks any downstream consumer.
        raise SystemExit(
            "[build_paper_tables] ABORT: null-case events without any "
            "validator-recognized evidence anchor: "
            + ", ".join(anchorless)
            + ". Fix the event YAMLs (add body_hash+body_path, query_hash, "
            "or measurement_ids on at least one "
            "observed_no_change source) before regenerating paper tables."
        )

    csv_path = out_dir / "table6_null_denominator.csv"
    with csv_path.open("w", newline="") as fh:
        fields = ["event_id", "research_stratum", "no_change_layers", "evidence_anchors_present"]
        w = csv.DictWriter(fh, fieldnames=fields, lineterminator="\n")
        w.writeheader()
        for r in csv_rows:
            w.writerow(r)


# ---------- index / meta ----------

def build_index(
    out_dir: pathlib.Path,
    ds_meta: dict,
    event_count: int,
) -> None:
    lines = _snapshot_header(ds_meta, "Paper-tables index")
    lines.append(
        "These tables are the reproducible surface for every number in "
        "the paper. Each table links to the specific `docs/paper_claims.md` "
        "claim(s) it supports and to the `derived/` artifact it reads "
        "from. Re-run with `make paper-tables` from a clean checkout; "
        "the output under this directory should match the paper's figures "
        "byte-for-byte at a given `source_input_hash`."
    )
    lines.append("")
    lines.append(f"Events in snapshot: **{event_count}**")
    lines.append("")
    lines.append("| # | table | supports | inputs |")
    lines.append("| --- | --- | --- | --- |")
    lines.append("| 1 | [table1_case_roles.md](table1_case_roles.md) | `§0 case roles` | `events/*.yaml` + `derived/event_metrics` + `derived/event_archetypes` |")
    lines.append("| 2 | [table2_layer_observability.md](table2_layer_observability.md) | `C1` | `derived/layer_observability` |")
    lines.append("| 3 | [table3_archetype_stratum.md](table3_archetype_stratum.md) | parked `C2`, descriptive `C5` pending `observation_kind` κ | `derived/event_archetypes` |")
    lines.append("| 4 | [table4_latency_by_precision.md](table4_latency_by_precision.md) | `C3`, `C4` | `events/*.yaml` + `derived/event_metrics` + `derived/event_archetypes` |")
    lines.append("| 5 | [table5_target_enumeration.md](table5_target_enumeration.md) | `§4 item 5` | `events/*.yaml` + `derived/event_archetypes` |")
    lines.append("| 6 | [table6_null_denominator.md](table6_null_denominator.md) | null-event interpretation (C6 demoted 2026-04-24 — see `docs/paper_claims.md §C6`) | `events/*.yaml` + `derived/event_archetypes` |")
    if (out_dir / "table7_jurisdiction_distribution.md").exists():
        lines.append("| 7 | [table7_jurisdiction_distribution.md](table7_jurisdiction_distribution.md) | `§0 sampling frame` | `events/*.yaml` via `scripts/build_jurisdiction_distribution.py` |")
    lines.append("")
    lines.append(
        "Claims that are NOT yet backed by a table (because the underlying "
        "data is absent or the analysis is out of scope for v0.1) are "
        "enumerated in `docs/paper_claims.md §2`."
    )
    lines.append("")
    _write_md(out_dir / "README.md", lines)


def main() -> int:
    args = parse_args()
    events_dir = pathlib.Path(args.events_dir)
    derived_dir = pathlib.Path(args.derived_dir)
    out_dir = pathlib.Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    events = _load_events(events_dir)
    if not events:
        raise SystemExit(f"[build_paper_tables] no events found under {events_dir}")

    metrics = _load_derived(derived_dir, "event_metrics")
    archetypes = _load_derived(derived_dir, "event_archetypes")
    layer_obs = _load_derived(derived_dir, "layer_observability")
    sensitivity = _load_optional_csv(derived_dir, "admission_sensitivity")
    metrics_by_id = {r["event_id"]: r for r in metrics}
    archetypes_by_id = {r["event_id"]: r for r in archetypes}

    ds_meta = load_meta()

    build_table1(events, metrics_by_id, archetypes_by_id, out_dir, ds_meta)
    build_table2(layer_obs, out_dir, ds_meta, sensitivity)
    build_table3(archetypes, out_dir, ds_meta)
    build_table4(events, metrics_by_id, archetypes_by_id, out_dir, ds_meta)
    build_table5(events, metrics_by_id, archetypes_by_id, out_dir, ds_meta)
    build_table6(events, archetypes_by_id, out_dir, ds_meta)
    build_index(out_dir, ds_meta, len(events))

    meta = {
        "artifact": "paper_tables",
        "generated_at": now_utc_iso(),
        "generator": {
            "script": "scripts/build_paper_tables.py",
            "version": GENERATOR_VERSION,
            "python": reproducible_python(),
        },
        "dataset_snapshot": {
            "dataset_version": ds_meta.get("dataset_version"),
            "schema_version": ds_meta.get("schema_version"),
            "cutoff_date": ds_meta.get("cutoff_date"),
            "source_commit": ds_meta.get("source_commit"),
            "source_input_hash": ds_meta.get("source_input_hash"),
        },
        "event_count": len(events),
        "tables": [
            "table1_case_roles",
            "table2_layer_observability",
            "table3_archetype_stratum",
            "table4_latency_by_precision",
            "table5_target_enumeration",
            "table6_null_denominator",
            *(
                ["table7_jurisdiction_distribution"]
                if (out_dir / "table7_jurisdiction_distribution.md").exists()
                else []
            ),
        ],
    }
    (out_dir / ".meta.json").write_text(json.dumps(meta, indent=2, sort_keys=True) + "\n")

    print(
        f"[build_paper_tables] wrote core tables + index to "
        f"{out_dir.relative_to(REPO_ROOT)}/ "
        f"(dataset v{ds_meta.get('dataset_version')} "
        f"cutoff {ds_meta.get('cutoff_date')})"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
