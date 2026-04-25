#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Build per-event derived metrics from the evidence-layer YAMLs.

Output (under derived/):
  - event_metrics.csv       panel-data surface for statistical work
  - event_metrics.json      full structured record + per-layer breakdowns
  - event_metrics.meta.json sidecar meta (version, cutoff, commit, generator)

This is the first artifact of the **derived research layer**. The evidence
layer (events/*.yaml) stays immutable; every metric here is a pure function
of the event YAML state + the dataset metadata snapshot. Rerun via
`make event-metrics` or `python3 scripts/build_event_metrics.py`.

Archetype classification lives in a separate artifact
(`derived/event_archetypes.json`) so the base-metric logic stays decoupled
from classification logic. Join on `event_id` if you want the merged view.
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


# Canonical layer order — must match scripts/render_site.py.
LAYER_ORDER = [
    "l0_network", "l1_consensus", "l3_rpc",
    "l4_frontend", "asset_onchain", "offramp_cex",
]

# Privacy-tool protocols (conservative list; reviewed 2026-04-23).
# Used by target_is_privacy_tool flag. Narrow on purpose: only protocols
# whose primary purpose is transaction / identity privacy.
PRIVACY_TOOL_PROTOCOLS = {
    "tornado_cash",
    "blender",
    "sinbad",
    "samourai",
    "chipmixer",
    "hydra",     # market with mixer feature; reviewers may prefer to split
    "cryptex",
    "monero",
    "zcash",
    "wasabi",
    "bitmixer",
    "zservers",  # privacy-infrastructure hosting provider
}

LARGE_TARGET_THRESHOLD = 20
GENERATOR_VERSION = "0.1.0"

REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent
EVENTS_DIR = REPO_ROOT / "events"
DEFAULT_OUT_DIR = REPO_ROOT / "derived"

# Shared dataset-identity accessor.
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from _dataset_meta import load_meta, now_utc_iso  # noqa: E402


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Build derived event metrics.")
    p.add_argument("--events-dir", default=str(EVENTS_DIR))
    p.add_argument("--out-dir", default=str(DEFAULT_OUT_DIR))
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


def hours_between(ts_a: datetime | None, ts_b: datetime | None) -> float | None:
    if ts_a is None or ts_b is None:
        return None
    return (ts_a - ts_b).total_seconds() / 3600.0


def _obs_delta_h(obs: dict, trigger_ts: datetime | None) -> float | None:
    """Prefer explicit delta_hours; fall back to (timestamp - trigger)."""
    dh = obs.get("delta_hours")
    if dh is not None:
        try:
            return float(dh)
        except (TypeError, ValueError):
            pass
    return hours_between(parse_ts(obs.get("timestamp")), trigger_ts)


def _observation_action_id(slug: str, obs_idx: int, obs: dict) -> str:
    action_id = obs.get("action_id")
    if isinstance(action_id, str) and action_id.strip():
        return action_id.strip()
    return (
        f"{slug}:{obs_idx}:{obs.get('layer')}:{obs.get('actor')}:"
        f"{obs.get('event')}"
    )


def compute_event_metrics(event: dict) -> dict[str, Any]:
    slug = event.get("id", "unknown")
    trigger = event.get("trigger") or {}
    trigger_ts = parse_ts(trigger.get("timestamp"))
    target = event.get("target") or {}
    addresses = target.get("addresses") or []
    protocol = (target.get("protocol") or "").lower().strip()
    observations = event.get("observations") or []
    recovery = event.get("recovery") or []
    coverage = event.get("coverage") or []

    # ---- coverage tallies ----
    cov_by_status: dict[str, int] = collections.Counter()
    cov_by_layer: dict[str, str] = {}
    for c in coverage:
        if not isinstance(c, dict):
            continue
        cov_by_status[c.get("status") or "unknown"] += 1
        cov_by_layer[c.get("layer")] = c.get("status")

    applicable_count = sum(
        1 for st in cov_by_layer.values() if st and st != "not_applicable"
    )

    # ---- observation tallies ----
    changed_layers: set[str] = set()
    unchanged_layers: set[str] = set()
    direct_layers: set[str] = set()
    plausible_layers: set[str] = set()
    per_layer_first_delta: dict[str, float] = {}
    deltas: list[float] = []
    changed_action_ids: list[str] = []
    duplicate_of_action_ids: list[str] = []

    for obs_idx, obs in enumerate(observations):
        if not isinstance(obs, dict):
            continue
        layer = obs.get("layer")
        kind = obs.get("observation_kind")
        attr = obs.get("attribution")
        if layer not in LAYER_ORDER:
            continue
        if kind == "observed_change":
            changed_layers.add(layer)
            changed_action_ids.append(_observation_action_id(slug, obs_idx, obs))
            dup = obs.get("duplicate_of_action_id")
            if isinstance(dup, str) and dup.strip():
                duplicate_of_action_ids.append(dup.strip())
            if attr == "direct":
                direct_layers.add(layer)
            elif attr == "plausible":
                plausible_layers.add(layer)
            dh = _obs_delta_h(obs, trigger_ts)
            if dh is not None:
                deltas.append(dh)
                prev = per_layer_first_delta.get(layer)
                if prev is None or dh < prev:
                    per_layer_first_delta[layer] = dh
        elif kind == "observed_no_change":
            unchanged_layers.add(layer)

    time_to_first = min(deltas) if deltas else None
    time_to_last = max(deltas) if deltas else None
    cascade_span = (
        time_to_last - time_to_first
        if time_to_first is not None and time_to_last is not None
        else None
    )

    changed_count = len(changed_layers)
    cascade_breadth = (
        changed_count / applicable_count if applicable_count else None
    )

    # ---- recovery ----
    # Only count recovery rows whose layer is actually in changed_layers.
    # A recovery entry for a layer that was never observed to change is
    # either a mis-annotation or a general-state note and must not appear
    # in the resolved/unresolved tallies — otherwise recovered + unresolved
    # + recovery_unknown can exceed changed_layer_count (see P2 in the
    # 2026-04-23 review; tornado-cash-ofac-delisting-2025 had l3_rpc
    # resolved=false despite l3_rpc never being in changed_layers).
    resolved_true: set[str] = set()
    resolved_false: set[str] = set()
    resolved_hours: list[float] = []
    for r in recovery:
        if not isinstance(r, dict):
            continue
        layer = r.get("layer")
        if layer not in changed_layers:
            continue
        if r.get("resolved") is True:
            resolved_true.add(layer)
            rts = parse_ts(r.get("resolved_timestamp"))
            dh = hours_between(rts, trigger_ts)
            if dh is not None and dh >= 0:
                resolved_hours.append(dh)
        elif r.get("resolved") is False:
            resolved_false.add(layer)

    recovery_unknown = changed_layers - resolved_true - resolved_false
    recovered_count = len(resolved_true)
    unrecovered_count = len(resolved_false)
    recovery_rate = (
        recovered_count / changed_count if changed_count else None
    )
    mean_resolved_hours = (
        sum(resolved_hours) / len(resolved_hours) if resolved_hours else None
    )

    # ---- source strength ----
    prim = prim_onchain = semi = supporting = 0
    for obs in observations:
        for src in (obs.get("sources") or []):
            t = str((src or {}).get("type") or "")
            if t == "primary_onchain":
                prim_onchain += 1
                prim += 1
            elif t.startswith("primary_"):
                prim += 1
            elif t.startswith("semi_primary_"):
                semi += 1
            elif t.startswith("supporting_"):
                supporting += 1

    # ---- structural flags ----
    has_large_target = len(addresses) >= LARGE_TARGET_THRESHOLD
    is_reversal = str(trigger.get("type") or "") == "ofac_sdn_removal"
    is_privacy = protocol in PRIVACY_TOOL_PROTOCOLS

    # ---- per-layer enforcement (JSON only — CSV stays flat-readable) ----
    per_layer = {}
    for layer in LAYER_ORDER:
        per_layer[layer] = {
            "coverage_status": cov_by_layer.get(layer),
            "changed": layer in changed_layers,
            "direct": layer in direct_layers,
            "plausible": layer in plausible_layers,
            "observed_no_change": layer in unchanged_layers,
            "resolved": (
                True if layer in resolved_true
                else False if layer in resolved_false
                else None
            ),
            "first_change_hours": per_layer_first_delta.get(layer),
        }

    return {
        "event_id": slug,
        "research_stratum": event.get("research_stratum"),
        "empirical_shape": event.get("empirical_shape"),
        "admission_tier": event.get("admission_tier"),
        "status": event.get("status"),

        "applicable_layer_count": applicable_count,
        "changed_layer_count": changed_count,
        "cascade_breadth": cascade_breadth,

        "time_to_first_change_hours": time_to_first,
        "time_to_last_change_hours": time_to_last,
        "cascade_span_hours": cascade_span,

        "direct_attribution_layer_count": len(direct_layers),
        "plausible_attribution_layer_count": len(plausible_layers),

        "recovered_layer_count": recovered_count,
        "unrecovered_layer_count": unrecovered_count,
        "recovery_unknown_layer_count": len(recovery_unknown),
        "recovery_rate": recovery_rate,
        "mean_resolved_hours": mean_resolved_hours,

        "coverage_measured_count": cov_by_status.get("measured", 0),
        "coverage_partial_count": cov_by_status.get("partially_measured", 0),
        "coverage_gap_count": cov_by_status.get("not_measured", 0),
        "coverage_na_count": cov_by_status.get("not_applicable", 0),

        "primary_source_count": prim,
        "primary_onchain_source_count": prim_onchain,
        "semi_primary_source_count": semi,
        "supporting_source_count": supporting,
        "changed_action_count": len(changed_action_ids),
        "changed_unique_action_count": len(set(changed_action_ids)),
        "duplicate_of_action_ids": sorted(set(duplicate_of_action_ids)),

        "has_large_target_set": has_large_target,
        "is_reversal_event": is_reversal,
        "target_is_privacy_tool": is_privacy,

        "per_layer": per_layer,
    }


CSV_COLUMNS = [
    "event_id",
    "research_stratum", "empirical_shape", "admission_tier",
    "applicable_layer_count", "changed_layer_count", "cascade_breadth",
    "time_to_first_change_hours", "time_to_last_change_hours", "cascade_span_hours",
    "direct_attribution_layer_count", "plausible_attribution_layer_count",
    "recovered_layer_count", "unrecovered_layer_count", "recovery_unknown_layer_count",
    "recovery_rate", "mean_resolved_hours",
    "coverage_measured_count", "coverage_partial_count", "coverage_gap_count",
    "primary_source_count", "semi_primary_source_count", "primary_onchain_source_count",
    "changed_action_count", "changed_unique_action_count",
    "has_large_target_set", "is_reversal_event", "target_is_privacy_tool",
]


def _fmt_for_csv(value: Any) -> Any:
    if isinstance(value, float):
        return round(value, 4)
    if isinstance(value, bool):
        return "true" if value else "false"
    if value is None:
        return ""
    return value


def main() -> int:
    args = parse_args()
    events_dir = pathlib.Path(args.events_dir)
    out_dir = pathlib.Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    events = []
    for f in sorted(events_dir.glob("*.yaml")):
        if f.name == "TEMPLATE.yaml" or f.name.startswith("_"):
            continue
        events.append(yaml.safe_load(f.read_text()))

    metrics = [compute_event_metrics(e) for e in events]

    csv_path = out_dir / "event_metrics.csv"
    with csv_path.open("w", newline="") as fh:
        writer = csv.DictWriter(
            fh, fieldnames=CSV_COLUMNS, extrasaction="ignore", lineterminator="\n"
        )
        writer.writeheader()
        for m in metrics:
            writer.writerow({k: _fmt_for_csv(m.get(k)) for k in CSV_COLUMNS})

    json_path = out_dir / "event_metrics.json"
    json_path.write_text(json.dumps(metrics, indent=2, sort_keys=True) + "\n")

    ds_meta = load_meta()
    meta = {
        "artifact": "event_metrics",
        "generated_at": now_utc_iso(),
        "generator": {
            "script": "scripts/build_event_metrics.py",
            "version": GENERATOR_VERSION,
            "python": platform.python_version(),
        },
        "dataset_snapshot": {
            "dataset_version": ds_meta.get("dataset_version"),
            "schema_version": ds_meta.get("schema_version"),
            "cutoff_date": ds_meta.get("cutoff_date"),
            "source_commit": ds_meta.get("source_commit"),
        },
        "event_count": len(metrics),
        "csv_columns": CSV_COLUMNS,
        "notes": (
            "Derived metrics. Evidence layer (events/*.yaml) is the source of "
            "truth; this artifact is a pure function of it. Regenerate with "
            "`make event-metrics`. Archetype / signature / latency-regime "
            "labels live in derived/event_archetypes.json (join on event_id)."
        ),
    }
    (out_dir / "event_metrics.meta.json").write_text(
        json.dumps(meta, indent=2, sort_keys=True) + "\n"
    )

    print(
        f"[build_event_metrics] wrote {len(metrics)} rows to {csv_path.name} + "
        f"{json_path.name} + event_metrics.meta.json "
        f"(dataset v{ds_meta.get('dataset_version')} cutoff {ds_meta.get('cutoff_date')})"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
