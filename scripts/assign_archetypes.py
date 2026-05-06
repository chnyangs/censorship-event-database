#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Rule-based event-archetype classifier.

Deterministic, priority-ordered if/else — no clustering. Fits a project
whose whole philosophy is auditable, reproducible, explicit. The 6 classes
are defined by *which* layer(s) changed, not by *how many*, because the
dataset is heavily dominated by single-layer cases (35/53) and clustering
on `changed_layer_count` alone collapses to a trivial partition.

Classification rules (priority-ordered, first match wins):

  1. null_event        : 0 observed_change layers
  2. multi_layer       : ≥ 2 observed_change layers
  3. asset_only        : changed layers == {asset_onchain}
  4. frontend_only     : changed layers == {l4_frontend}
  5. cex_only          : changed layers == {offramp_cex}
  6. other_single_layer: 1 observed_change layer NOT in {asset, frontend, cex}
                         — safety class for L0 / L1 / L3 singletons should
                         they appear in future data.

Additional derived fields per event:
  - changed_layer_signature  "asset_onchain+offramp_cex" (alphabetised join)
  - latency_regime           {synchronous, acute, delayed, lagged, none}
      synchronous ≤ 1h
      acute       1h < t ≤ 30h
      delayed     30h < t ≤ 720h (30 days)
      lagged      > 720h
      none        no timed observed_change
  - has_recovery_signal      any recovery row with resolved=true OR resolved=false
  - is_upper_layer_only      changed ⊆ {l4_frontend, asset_onchain, offramp_cex}
  - is_base_layer_observed   changed ∩ {l0_network, l1_consensus} ≠ ∅
  - trigger_is_action        true when BOTH (a) trigger.type is
      `corporate_policy_change` AND (b) the first observed_change
      timestamp coincides with the trigger timestamp (|delta| ≤ 1h).
      A corporate_policy_change event where the observation is genuinely
      later (e.g. corporate retreat 3 days after an initial corporate
      launch, prompted by external pressure) does NOT carry the flag —
      its delta_hours is a real measurement, not a record-level
      artifact, and it should enter the latency analysis via Panel A/B
      of Table 4 rather than being silenced in Panel C. Paper claims
      about cascade latency should report rows with `trigger_is_action
      = false` separately from those with `trigger_is_action = true`.

Decoupled on purpose: this script does NOT mutate event_metrics.json.
Downstream consumers wanting joined data should join on `event_id`.

Output (under derived/):
  - event_archetypes.csv
  - event_archetypes.json
  - event_archetypes.meta.json
  - archetype_distribution.md   — human-readable report (rules + counts +
                                   exemplars + edge-cases)
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


UPPER_LAYERS = {"l4_frontend", "asset_onchain", "offramp_cex"}
BASE_LAYERS = {"l0_network", "l1_consensus"}
LAYER_ORDER = [
    "l0_network", "l1_consensus", "l3_rpc",
    "l4_frontend", "asset_onchain", "offramp_cex",
]

# Latency regime thresholds (hours). Inclusive-right on each band.
LAT_SYNCHRONOUS = 1.0
LAT_ACUTE = 30.0
LAT_DELAYED = 30.0 * 24.0   # 30 days = 720h

GENERATOR_VERSION = "0.1.0"

REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent
EVENTS_DIR = REPO_ROOT / "events"
DEFAULT_OUT_DIR = REPO_ROOT / "derived"

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from _dataset_meta import load_meta, now_utc_iso  # noqa: E402


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Assign event archetypes.")
    p.add_argument("--events-dir", default=str(EVENTS_DIR))
    p.add_argument("--out-dir", default=str(DEFAULT_OUT_DIR))
    p.add_argument(
        "--exemplars-per-class", type=int, default=5,
        help="max exemplar events listed per archetype in the Markdown report",
    )
    return p.parse_args()


def parse_ts(value: Any) -> datetime | None:
    if value is None:
        return None
    if isinstance(value, datetime):
        return value if value.tzinfo else value.replace(tzinfo=timezone.utc)
    try:
        return datetime.fromisoformat(str(value).replace("Z", "+00:00"))
    except ValueError:
        return None


def _obs_delta_h(obs: dict, trigger_ts: datetime | None) -> float | None:
    dh = obs.get("delta_hours")
    if dh is not None:
        try:
            return float(dh)
        except (TypeError, ValueError):
            pass
    ts = parse_ts(obs.get("timestamp"))
    if ts is None or trigger_ts is None:
        return None
    return (ts - trigger_ts).total_seconds() / 3600.0


def classify(changed_layers: set[str]) -> str:
    """Deterministic priority-ordered classifier. See module docstring."""
    if not changed_layers:
        return "null_event"
    if len(changed_layers) >= 2:
        return "multi_layer"
    # exactly one
    (only,) = tuple(changed_layers)
    if only == "asset_onchain":
        return "asset_only"
    if only == "l4_frontend":
        return "frontend_only"
    if only == "offramp_cex":
        return "cex_only"
    # Safety class: L0 / L1 / L3 singletons land here.
    return "other_single_layer"


def latency_regime(time_to_first_change_h: float | None) -> str:
    if time_to_first_change_h is None:
        return "none"
    t = time_to_first_change_h
    if t <= LAT_SYNCHRONOUS:
        return "synchronous"
    if t <= LAT_ACUTE:
        return "acute"
    if t <= LAT_DELAYED:
        return "delayed"
    return "lagged"


TRIGGER_IS_ACTION_TYPES = {"corporate_policy_change"}
# Coincidence tolerance: how close the first observed_change must be to the
# trigger timestamp for `trigger_is_action` to fire. Set to 1h so that minute-
# precision corporate-policy-change events (Circle, Tether, Uniswap) still
# trigger the flag even when the source-of-truth timestamps are logged to
# slightly different seconds, while day-level retreats like Coinbase's
# India exit (delta = 72h) are correctly classified as measured reactions.
TRIGGER_IS_ACTION_MAX_DELTA_H = 1.0


def derive_event(event: dict) -> dict[str, Any]:
    slug = event.get("id") or "unknown"
    trigger = event.get("trigger") or {}
    trigger_ts = parse_ts(trigger.get("timestamp"))
    trigger_type = trigger.get("type") or ""

    changed: set[str] = set()
    first_deltas: list[float] = []
    for obs in event.get("observations") or []:
        if not isinstance(obs, dict):
            continue
        if obs.get("observation_kind") != "observed_change":
            continue
        layer = obs.get("layer")
        if layer in LAYER_ORDER:
            changed.add(layer)
            dh = _obs_delta_h(obs, trigger_ts)
            if dh is not None:
                first_deltas.append(dh)

    time_to_first = min(first_deltas) if first_deltas else None

    recovery = event.get("recovery") or []
    has_recovery_signal = any(
        isinstance(r, dict) and ("resolved" in r) for r in recovery
    )

    archetype = classify(changed)
    signature = "+".join(sorted(changed)) if changed else "none"

    return {
        "event_id": slug,
        "research_stratum": event.get("research_stratum"),
        "empirical_shape": event.get("empirical_shape"),
        "admission_tier": event.get("admission_tier"),
        "changed_layer_count": len(changed),
        "changed_layers": sorted(changed),
        "changed_layer_signature": signature,
        "derived_archetype": archetype,
        "latency_regime": latency_regime(time_to_first),
        "time_to_first_change_hours": time_to_first,
        "has_recovery_signal": has_recovery_signal,
        "is_upper_layer_only": bool(changed) and changed.issubset(UPPER_LAYERS),
        "is_base_layer_observed": bool(changed.intersection(BASE_LAYERS)),
        "trigger_is_action": (
            trigger_type in TRIGGER_IS_ACTION_TYPES
            and time_to_first is not None
            and abs(time_to_first) <= TRIGGER_IS_ACTION_MAX_DELTA_H
        ),
    }


CSV_COLUMNS = [
    "event_id",
    "research_stratum", "empirical_shape", "admission_tier",
    "derived_archetype", "changed_layer_signature",
    "changed_layer_count",
    "latency_regime", "time_to_first_change_hours",
    "trigger_is_action",
    "has_recovery_signal",
    "is_upper_layer_only", "is_base_layer_observed",
]


def _fmt(v: Any) -> Any:
    if isinstance(v, float):
        return round(v, 4)
    if isinstance(v, bool):
        return "true" if v else "false"
    if v is None:
        return ""
    if isinstance(v, list):
        return ",".join(v)
    return v


ARCHETYPE_ORDER = [
    "asset_only",
    "frontend_only",
    "cex_only",
    "multi_layer",
    "other_single_layer",
    "null_event",
]


def render_report(
    rows: list[dict],
    exemplars_per_class: int,
    ds_meta: dict,
) -> str:
    lines: list[str] = []
    lines.append("# Archetype distribution report")
    lines.append("")
    lines.append(
        f"Dataset snapshot: **v{ds_meta.get('dataset_version') or '?'}** · "
        f"cutoff `{ds_meta.get('cutoff_date') or 'n/a'}` · "
        f"commit `{ds_meta.get('source_commit') or 'n/a'}` · "
        f"generated `{now_utc_iso()}` "
        f"(events: {len(rows)})"
    )
    lines.append("")

    # --- Section 1: classification rules ---
    lines.append("## 1. Classification rules (deterministic, priority-ordered)")
    lines.append("")
    lines.append("```")
    lines.append("if changed_layer_count == 0:")
    lines.append("    → null_event")
    lines.append("elif changed_layer_count >= 2:")
    lines.append("    → multi_layer")
    lines.append("elif changed_layers == {asset_onchain}:")
    lines.append("    → asset_only")
    lines.append("elif changed_layers == {l4_frontend}:")
    lines.append("    → frontend_only")
    lines.append("elif changed_layers == {offramp_cex}:")
    lines.append("    → cex_only")
    lines.append("else:")
    lines.append("    → other_single_layer   # L0 / L1 / L3 singleton safety class")
    lines.append("```")
    lines.append("")
    lines.append(
        "Latency-regime (bands on `time_to_first_change_hours`): "
        "`synchronous` ≤ 1h · `acute` ≤ 30h · `delayed` ≤ 30d · `lagged` > 30d · "
        "`none` = no timed observed_change."
    )
    lines.append("")

    # --- Section 2: distribution counts ---
    lines.append("## 2. Distribution")
    lines.append("")
    by_archetype = collections.Counter(r["derived_archetype"] for r in rows)
    total = len(rows)
    lines.append("| Archetype | Count | % |")
    lines.append("| --- | ---: | ---: |")
    for arch in ARCHETYPE_ORDER:
        n = by_archetype.get(arch, 0)
        pct = 100.0 * n / total if total else 0.0
        lines.append(f"| `{arch}` | {n} | {pct:.1f}% |")
    lines.append(f"| **total** | **{total}** | **100.0%** |")
    lines.append("")

    # signature breakdown within multi_layer
    multi = [r for r in rows if r["derived_archetype"] == "multi_layer"]
    if multi:
        lines.append("### 2a. `multi_layer` signatures")
        lines.append("")
        sig_counts = collections.Counter(r["changed_layer_signature"] for r in multi)
        lines.append("| Signature | Count | Events |")
        lines.append("| --- | ---: | --- |")
        for sig, n in sig_counts.most_common():
            evs = ", ".join(f"`{r['event_id']}`" for r in multi if r["changed_layer_signature"] == sig)
            lines.append(f"| `{sig}` | {n} | {evs} |")
        lines.append("")

    # latency regime breakdown
    lines.append("### 2b. Latency regime")
    lines.append("")
    lat_counts = collections.Counter(r["latency_regime"] for r in rows)
    lines.append("| Regime | Count | % |")
    lines.append("| --- | ---: | ---: |")
    for reg in ("synchronous", "acute", "delayed", "lagged", "none"):
        n = lat_counts.get(reg, 0)
        pct = 100.0 * n / total if total else 0.0
        lines.append(f"| `{reg}` | {n} | {pct:.1f}% |")
    lines.append("")

    # cross-tab archetype × latency
    lines.append("### 2c. Archetype × latency cross-tab")
    lines.append("")
    xtab: dict[tuple[str, str], int] = collections.Counter(
        (r["derived_archetype"], r["latency_regime"]) for r in rows
    )
    lat_cols = ["synchronous", "acute", "delayed", "lagged", "none"]
    header = "| archetype \\ latency | " + " | ".join(lat_cols) + " | total |"
    sep = "| --- |" + "".join(" ---: |" for _ in lat_cols) + " ---: |"
    lines.append(header)
    lines.append(sep)
    for arch in ARCHETYPE_ORDER:
        cells = [str(xtab.get((arch, reg), 0)) for reg in lat_cols]
        tot = sum(xtab.get((arch, reg), 0) for reg in lat_cols)
        lines.append(f"| `{arch}` | " + " | ".join(cells) + f" | {tot} |")
    lines.append("")

    # --- Section 3: exemplars per class ---
    lines.append("## 3. Exemplar cases")
    lines.append("")
    lines.append(f"Up to {exemplars_per_class} events per class, selected by admission tier then slug.")
    lines.append("")
    tier_rank = {"anchor_case": 0, "empirical_case": 1, "null_case": 2}
    for arch in ARCHETYPE_ORDER:
        members = [r for r in rows if r["derived_archetype"] == arch]
        if not members:
            lines.append(f"### `{arch}`  (0 events)")
            lines.append("")
            lines.append("_No events in this class in the current corpus._")
            lines.append("")
            continue
        members_sorted = sorted(
            members,
            key=lambda r: (tier_rank.get(r["admission_tier"], 99), r["event_id"]),
        )[:exemplars_per_class]
        lines.append(f"### `{arch}`  ({len(members)} events)")
        lines.append("")
        for r in members_sorted:
            sig = r["changed_layer_signature"]
            lat = r["latency_regime"]
            t = r["time_to_first_change_hours"]
            t_str = f"{t:.1f}h" if isinstance(t, (int, float)) else "—"
            lines.append(
                f"- `{r['event_id']}` · tier `{r['admission_tier']}` · "
                f"stratum `{r['research_stratum']}` · "
                f"signature `{sig}` · latency `{lat}` (t={t_str})"
            )
        lines.append("")

    # --- Section 4: edge cases / review notes ---
    lines.append("## 4. Edge cases and review notes")
    lines.append("")
    notes: list[str] = []

    # Reversal events
    # (surfaced via the event_metrics.is_reversal_event flag; we re-compute from
    # the archetype data by name because the MD is standalone)
    # Tornado delisting is our one reversal; flag it explicitly if present
    for r in rows:
        if r["event_id"].endswith("-delisting-2025") or "removal" in (r["research_stratum"] or ""):
            notes.append(
                f"- `{r['event_id']}` is the dataset's sole reversal event. Archetype "
                f"`{r['derived_archetype']}` is assigned by the same rule as forward events "
                f"(changed-layer set); direction is NOT encoded in the archetype. Consumers "
                "drawing recovery claims from this row should carry n=1 explicitly."
            )

    # other_single_layer class (will be 0 today, but flag loudly if any)
    other = [r for r in rows if r["derived_archetype"] == "other_single_layer"]
    if other:
        notes.append(
            f"- **{len(other)} event(s)** landed in `other_single_layer` — a singleton change "
            "at L0 / L1 / L3. This class exists as a safety catch; if populated, expand the "
            "taxonomy rather than leave it here: " +
            ", ".join(f"`{r['event_id']}`" for r in other)
        )
    else:
        notes.append(
            "- `other_single_layer` is empty in this snapshot (no L0/L1/L3-only singleton). "
            "The class remains defined so future data with a L0/L1/L3 singleton does not "
            "silently mis-classify."
        )

    # null events with observed_no_change (the "null denominator" reminder)
    nulls_with_evidence = [
        r for r in rows
        if r["derived_archetype"] == "null_event"
    ]
    if nulls_with_evidence:
        notes.append(
            f"- `null_event` count is {len(nulls_with_evidence)}. Each such event carries at "
            "least one `observed_no_change` row whose source supplies a falsifiable evidence "
            "anchor — per validator rule, any one of `query_hash`, `measurement_ids`, "
            "`body_hash`+`body_path`, or a structured `scope_descriptor` is sufficient (not all "
            "four, and not necessarily `scope_descriptor`). Reading the null-event count as "
            "'censorship did not happen' still requires checking the per-layer coverage "
            "composition in `derived/layer_observability.csv` — absence of observation is NOT "
            "absence of phenomenon."
        )

    # multi_layer with only 1 signature type → signature diversity warning
    multi_rows = [r for r in rows if r["derived_archetype"] == "multi_layer"]
    if multi_rows:
        multi_sig_count = len({r["changed_layer_signature"] for r in multi_rows})
        notes.append(
            f"- `multi_layer` contains {len(multi_rows)} events across {multi_sig_count} distinct "
            f"signature(s). If signature diversity is low, claims about 'multi-layer cascade "
            "heterogeneity' should carry that caveat explicitly."
        )

    # synchronous cases: separate the corporate_policy_change rows whose
    # trigger timestamp is identical to the observed-change timestamp from
    # rows with distinct external triggers.
    sync = [r for r in rows if r["latency_regime"] == "synchronous"]
    if sync:
        t_is_a = [r for r in sync if r.get("trigger_is_action")]
        ext_trig = [r for r in sync if not r.get("trigger_is_action")]
        notes.append(
            f"- `synchronous` (≤1h) bucket: {len(sync)} events. "
            f"**{len(t_is_a)} have `trigger_is_action=true`** "
            f"(all `corporate_policy_change` — trigger.timestamp and "
            f"observed_change.timestamp are identical in the record, so t=0 "
            f"is a record-level artifact, not a measured delta): " +
            ", ".join(f"`{r['event_id']}`" for r in t_is_a) + ". "
            f"The remaining {len(ext_trig)} carry distinct external triggers "
            "and observed a change within 1h. When reporting latency "
            "distributions, aggregate the two subsets separately rather than "
            "collapsing them into a single 'synchronous' count."
        )

    # lagged cases: long tail. Descriptive only — no mechanism attribution
    # (the 5 events span OFAC SDN / CFTC court order / nation-state triggers;
    # a single-mechanism label would project beyond the data).
    lagged = [r for r in rows if r["latency_regime"] == "lagged"]
    if lagged:
        strata_here = sorted({r["research_stratum"] for r in lagged})
        notes.append(
            f"- `lagged` (>30d) bucket: {len(lagged)} events spanning "
            f"{len(strata_here)} stratum/strata ({', '.join(strata_here)}). "
            f"The group is heterogeneous in trigger type; consumers citing "
            f"these events should enumerate them individually rather than "
            f"treat the bucket as a single mechanism. Events: " +
            ", ".join(f"`{r['event_id']}`" for r in lagged) + "."
        )

    for n in notes:
        lines.append(n)
    if not notes:
        lines.append("_No edge-case notes for this snapshot._")
    lines.append("")

    # --- Section 5: hand-eyeball checklist ---
    lines.append("## 5. Hand-eyeball checklist")
    lines.append("")
    lines.append("Before promoting this taxonomy to a paper claim, confirm each of the following by reading the exemplars above:")
    lines.append("")
    lines.append("- [ ] Each exemplar is plausibly a member of its assigned class (not mis-labelled by the rules)")
    lines.append("- [ ] No event straddles two classes semantically — if it does, the rules need a tie-breaker")
    lines.append("- [ ] `multi_layer` signature diversity is adequate, or the report is clear about low diversity")
    lines.append("- [ ] `null_event` members are coverage-disciplined (not just 'we didn't look')")
    lines.append("- [ ] `other_single_layer` is empty OR surfaces are genuinely novel and warrant a new class")
    lines.append("- [ ] `synchronous` members are not misleading — trigger ≠ reaction, even when same-hour")
    lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def main() -> int:
    args = parse_args()
    events_dir = pathlib.Path(args.events_dir)
    out_dir = pathlib.Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    events: list[dict] = []
    for f in sorted(events_dir.glob("*.yaml")):
        if f.name == "TEMPLATE.yaml" or f.name.startswith("_"):
            continue
        event = yaml.safe_load(f.read_text())
        if isinstance(event, dict) and event.get("status") == "admitted":
            events.append(event)

    rows = [derive_event(e) for e in events]

    csv_path = out_dir / "event_archetypes.csv"
    with csv_path.open("w", newline="") as fh:
        writer = csv.DictWriter(
            fh, fieldnames=CSV_COLUMNS, extrasaction="ignore", lineterminator="\n"
        )
        writer.writeheader()
        for r in rows:
            writer.writerow({k: _fmt(r.get(k)) for k in CSV_COLUMNS})

    json_path = out_dir / "event_archetypes.json"
    json_path.write_text(json.dumps(rows, indent=2, sort_keys=True) + "\n")

    ds_meta = load_meta()
    meta = {
        "artifact": "event_archetypes",
        "generated_at": now_utc_iso(),
        "generator": {
            "script": "scripts/assign_archetypes.py",
            "version": GENERATOR_VERSION,
            "python": platform.python_version(),
        },
        "dataset_snapshot": {
            "dataset_version": ds_meta.get("dataset_version"),
            "schema_version": ds_meta.get("schema_version"),
            "cutoff_date": ds_meta.get("cutoff_date"),
            "source_commit": ds_meta.get("source_commit"),
        },
        "event_count": len(rows),
        "archetype_order": ARCHETYPE_ORDER,
        "latency_bands_hours": {
            "synchronous_max": LAT_SYNCHRONOUS,
            "acute_max": LAT_ACUTE,
            "delayed_max": LAT_DELAYED,
        },
        "csv_columns": CSV_COLUMNS,
        "notes": (
            "Rule-based deterministic taxonomy. No clustering, no latent-class "
            "assumptions. Rules live in scripts/assign_archetypes.py::classify. "
            "Merging with base metrics: join derived/event_metrics.json on event_id."
        ),
    }
    (out_dir / "event_archetypes.meta.json").write_text(
        json.dumps(meta, indent=2, sort_keys=True) + "\n"
    )

    report = render_report(rows, args.exemplars_per_class, ds_meta)
    (out_dir / "archetype_distribution.md").write_text(report)

    arche_counts = collections.Counter(r["derived_archetype"] for r in rows)
    print(
        f"[assign_archetypes] wrote {len(rows)} rows to "
        f"{csv_path.name} + {json_path.name} + "
        f"archetype_distribution.md + event_archetypes.meta.json"
    )
    for arch in ARCHETYPE_ORDER:
        print(f"  {arch:>20}: {arche_counts.get(arch, 0)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
