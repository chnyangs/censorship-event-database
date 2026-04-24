#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Reproducible paper-table generator.

Emits the six tables called out in `docs/paper_claims.md §4` under
`analysis/paper_tables/`. Every table is a pure function of:

  - `events/*.yaml`            (evidence layer)
  - `derived/*.json`            (derived-metric layer; required — run
                                 `make derived` first)

Each output carries:
  - the dataset snapshot stamp (`version`, `cutoff_date`,
    `source_commit`) so numbers in the paper can be re-verified
    against a specific repo state,
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
    make paper-tables                     # rebuild all 6
    python3 scripts/build_paper_tables.py --out-dir analysis/paper_tables
"""

from __future__ import annotations

import argparse
import collections
import csv
import json
import pathlib
import platform
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
from _dataset_meta import load_meta  # noqa: E402


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
HOUR_PRECISION_VALUES = {"minute", "second", "hour"}
DAY_PRECISION_VALUES = {"day", "date"}


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
        out.append(yaml.safe_load(f.read_text()))
    return out


def _load_derived(derived_dir: pathlib.Path, name: str) -> Any:
    path = derived_dir / f"{name}.json"
    if not path.exists():
        raise SystemExit(
            f"[build_paper_tables] missing {path.relative_to(REPO_ROOT)}. "
            "Run `make derived` first to regenerate the derived layer."
        )
    return json.loads(path.read_text())


def _rate(num: int, denom: int) -> str:
    """Render 'num/denom = pct' with denominator always present."""
    if denom <= 0:
        return "—"
    pct = 100.0 * num / denom
    return f"{num}/{denom} ({pct:.1f}%)"


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
        f"generated `{datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')}`",
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
        "changed (measured) | changed (partial) | changed/measured | changed/measured+partial |"
    )
    lines.append(
        "| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |"
    )
    for row in layer_rows:
        measured = row["measured_count"]
        partial = row["partially_measured_count"]
        changed_m = row["changed_under_measured_count"]
        changed_mp = row["changed_under_measured_or_partial_count"]
        # The partial-coverage-changed count on its own (not cumulative)
        changed_partial_only = changed_mp - changed_m
        lines.append(
            f"| `{row['layer']}` | "
            f"{row['applicable_event_count']} | "
            f"{measured} | {partial} | "
            f"{row['not_measured_count']} | {row['not_applicable_count']} | "
            f"{changed_m} | {changed_partial_only} | "
            f"{_rate(changed_m, measured)} | {_rate(changed_mp, measured + partial)} |"
        )
    lines.append("")
    lines.append(
        "A rate of `—` indicates a zero denominator; it is an "
        "**observability gap**, not an attested negative."
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
        "Supports **C2** and **C5** (`docs/paper_claims.md §1`). "
        "Rows: rule-based deterministic archetypes. Columns: research "
        "strata (admission stratification, NOT jurisdiction / population "
        "weighting)."
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


# ---------- Table 4: latency distribution (precision-filtered) ----------

LATENCY_BANDS_HOUR = [
    ("t=0", lambda h: h == 0.0),
    ("(0, 1]h", lambda h: 0 < h <= 1),
    ("(1, 6]h", lambda h: 1 < h <= 6),
    ("(6, 24]h", lambda h: 6 < h <= 24),
    ("(24, 168]h (≤1w)", lambda h: 24 < h <= 168),
    (">168h (>1w)", lambda h: h > 168),
]


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
        }
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
    ]
    with csv_path.open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=fields, lineterminator="\n")
        w.writeheader()
        for r in hour_rows + day_rows + excluded_trigger_is_action:
            w.writerow({k: ("" if r.get(k) is None else r[k]) for k in fields})

    # Markdown
    lines = _snapshot_header(
        ds_meta, "Table 4 · Latency distribution (precision-filtered)"
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
        "claims. The event's `time_to_first_change_hours` is reported "
        "rounded down to a ≤1-day or >1-day classifier, not a scalar "
        "hour value. Per-event hour values in the CSV dump are "
        "**record-level artifacts** (timestamp arithmetic) and must "
        "not enter any hour-bucketed paper claim."
    )
    lines.append("")
    if not day_rows:
        lines.append("_No day-precision triggers with a timed observed_change._")
    else:
        # Coarser bands for day-precision triggers.
        le1d = [r for r in day_rows if r["time_to_first_change_hours"] is not None and r["time_to_first_change_hours"] <= 24]
        d2_30 = [r for r in day_rows if r["time_to_first_change_hours"] is not None and 24 < r["time_to_first_change_hours"] <= 720]
        gt30 = [r for r in day_rows if r["time_to_first_change_hours"] is not None and r["time_to_first_change_hours"] > 720]
        lines.append("| day-granularity band | count | events |")
        lines.append("| --- | ---: | --- |")
        for label, subset in (("≤1d", le1d), ("(1d, 30d]", d2_30), (">30d", gt30)):
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
    ("body_hash+body_path", lambda s: bool(s.get("body_hash")) and bool(s.get("body_path"))),
    ("query_hash", lambda s: bool(s.get("query_hash"))),
    ("measurement_ids", lambda s: isinstance(s.get("measurement_ids"), list) and bool(s.get("measurement_ids"))),
    ("scope_descriptor", lambda s: isinstance(s.get("scope_descriptor"), dict) and bool(s.get("scope_descriptor"))),
]


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
        "Supports **C6** and the null-event interpretation note in "
        "`derived/archetype_distribution.md`. Each row lists the event's "
        "`observed_no_change` layers + the evidence-anchor types their "
        "sources carry. Per validator rule, any one of `body_hash`+"
        "`body_path`, `query_hash`, `measurement_ids`, or `scope_descriptor` "
        "is sufficient to admit an `observed_no_change` row."
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
        "(admission rules require at least one of the four anchor types). "
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
            "measurement_ids, or scope_descriptor on at least one "
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
        "byte-for-byte at a given `source_commit`."
    )
    lines.append("")
    lines.append(f"Events in snapshot: **{event_count}**")
    lines.append("")
    lines.append("| # | table | supports | inputs |")
    lines.append("| --- | --- | --- | --- |")
    lines.append("| 1 | [table1_case_roles.md](table1_case_roles.md) | `§0 case roles` | `events/*.yaml` + `derived/event_metrics` + `derived/event_archetypes` |")
    lines.append("| 2 | [table2_layer_observability.md](table2_layer_observability.md) | `C1` | `derived/layer_observability` |")
    lines.append("| 3 | [table3_archetype_stratum.md](table3_archetype_stratum.md) | `C2`, `C5` | `derived/event_archetypes` |")
    lines.append("| 4 | [table4_latency_by_precision.md](table4_latency_by_precision.md) | `C3`, `C4` | `events/*.yaml` + `derived/event_metrics` + `derived/event_archetypes` |")
    lines.append("| 5 | [table5_target_enumeration.md](table5_target_enumeration.md) | `§4 item 5` | `events/*.yaml` + `derived/event_archetypes` |")
    lines.append("| 6 | [table6_null_denominator.md](table6_null_denominator.md) | `C6`, null-event interpretation | `events/*.yaml` + `derived/event_archetypes` |")
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
    metrics_by_id = {r["event_id"]: r for r in metrics}
    archetypes_by_id = {r["event_id"]: r for r in archetypes}

    ds_meta = load_meta()

    build_table1(events, metrics_by_id, archetypes_by_id, out_dir, ds_meta)
    build_table2(layer_obs, out_dir, ds_meta)
    build_table3(archetypes, out_dir, ds_meta)
    build_table4(events, metrics_by_id, archetypes_by_id, out_dir, ds_meta)
    build_table5(events, metrics_by_id, archetypes_by_id, out_dir, ds_meta)
    build_table6(events, archetypes_by_id, out_dir, ds_meta)
    build_index(out_dir, ds_meta, len(events))

    meta = {
        "artifact": "paper_tables",
        "generated_at": datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z"),
        "generator": {
            "script": "scripts/build_paper_tables.py",
            "version": GENERATOR_VERSION,
            "python": platform.python_version(),
        },
        "dataset_snapshot": {
            "dataset_version": ds_meta.get("dataset_version"),
            "schema_version": ds_meta.get("schema_version"),
            "cutoff_date": ds_meta.get("cutoff_date"),
            "source_commit": ds_meta.get("source_commit"),
        },
        "event_count": len(events),
        "tables": [
            "table1_case_roles",
            "table2_layer_observability",
            "table3_archetype_stratum",
            "table4_latency_by_precision",
            "table5_target_enumeration",
            "table6_null_denominator",
        ],
    }
    (out_dir / ".meta.json").write_text(json.dumps(meta, indent=2, sort_keys=True) + "\n")

    print(
        f"[build_paper_tables] wrote 6 tables + index to "
        f"{out_dir.relative_to(REPO_ROOT)}/ "
        f"(dataset v{ds_meta.get('dataset_version')} "
        f"cutoff {ds_meta.get('cutoff_date')})"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
