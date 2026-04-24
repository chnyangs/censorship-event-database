#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Admission-protocol sensitivity ablation.

Addresses reviewer finding: "Authors choose `measured` vs
`partially_measured` vs `not_measured`; can that choice be audited
for rate-inflation risk?"

This script recomputes the coverage-matched layer-observability
table under three progressively looser admission rubrics:

1. **strict** — numerator counts *only* changes on `measured`
   layers (excludes `partially_measured`); attribution must be
   `direct`. Denominator = `measured_count`.
2. **current** — the status quo. Numerator counts `measured`
   changes for the strict rate, and `measured + partially_measured`
   changes for the broader rate; all attribution tiers in their own
   columns.
3. **permissive** — numerator counts changes on all covered layers
   including `partially_measured`; denominator broadens to
   `measured + partially_measured`.

Output:
    derived/admission_sensitivity.csv
    derived/admission_sensitivity.md
    derived/admission_sensitivity.meta.json

Interpretation (paper-facing): if the strict-vs-permissive delta
on `changed_given_measured` for a given layer is large (> 0.10
absolute) the rate is sensitive to the admission rubric and the
paper must report all three. If the delta is small (< 0.05), the
rate is robust and the `current` column suffices.
"""
from __future__ import annotations

import argparse
import csv
import json
import pathlib
import sys
from collections import Counter
from typing import Any

import yaml

REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent
EVENTS_DIR = REPO_ROOT / "events"
DEFAULT_OUT_DIR = REPO_ROOT / "derived"

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from _dataset_meta import load_meta, now_utc_iso  # noqa: E402

LAYER_ORDER = [
    "l0_network", "l1_consensus", "l3_rpc",
    "l4_frontend", "asset_onchain", "offramp_cex",
]

# Three admission rubrics. Each produces a (numerator set,
# denominator set, attribution filter) triple.
RUBRICS = {
    "strict": {
        "numerator_coverage": {"measured"},
        "denominator_coverage": {"measured"},
        "attribution_filter": {"direct"},
    },
    "current": {
        # Two numerators reported (measured-only, measured+partial),
        # both over their matched denominator. Attribution kept
        # split (direct vs plausible) — the current behavior.
        "numerator_coverage": {"measured"},
        "denominator_coverage": {"measured"},
        "attribution_filter": {"direct", "plausible"},
    },
    "permissive": {
        "numerator_coverage": {"measured", "partially_measured"},
        "denominator_coverage": {"measured", "partially_measured"},
        "attribution_filter": {"direct", "plausible"},
    },
}


def _load_events() -> list[dict]:
    events = []
    for f in sorted(EVENTS_DIR.glob("*.yaml")):
        if f.name == "TEMPLATE.yaml" or f.name.startswith("_"):
            continue
        events.append(yaml.safe_load(f.read_text()))
    return events


def _layer_status(event: dict, layer: str) -> str | None:
    for c in event.get("coverage") or []:
        if isinstance(c, dict) and c.get("layer") == layer:
            return c.get("status")
    return None


def _has_change(event: dict, layer: str,
                attribution_filter: set[str]) -> bool:
    for obs in event.get("observations") or []:
        if not isinstance(obs, dict):
            continue
        if obs.get("layer") != layer:
            continue
        if obs.get("observation_kind") != "observed_change":
            continue
        attr = obs.get("attribution") or "direct"
        if attr in attribution_filter:
            return True
    return False


def _compute_rubric(events: list[dict], layer: str,
                    rubric: dict) -> dict[str, Any]:
    num_covset = rubric["numerator_coverage"]
    den_covset = rubric["denominator_coverage"]
    attr_filter = rubric["attribution_filter"]

    denom_events = 0
    num_events = 0
    for e in events:
        status = _layer_status(e, layer)
        if status in den_covset:
            denom_events += 1
        if status in num_covset and _has_change(e, layer, attr_filter):
            num_events += 1
    rate = None if denom_events == 0 else round(num_events / denom_events, 4)
    return {
        "layer": layer,
        "numerator": num_events,
        "denominator": denom_events,
        "rate": rate,
    }


def _compute_all(events: list[dict]) -> list[dict[str, Any]]:
    rows = []
    for layer in LAYER_ORDER:
        row: dict[str, Any] = {"layer": layer}
        results: dict[str, dict] = {}
        for rubric_name, rubric in RUBRICS.items():
            r = _compute_rubric(events, layer, rubric)
            results[rubric_name] = r
            row[f"{rubric_name}_num"] = r["numerator"]
            row[f"{rubric_name}_den"] = r["denominator"]
            row[f"{rubric_name}_rate"] = r["rate"]
        # Sensitivity: strict → permissive delta on rate.
        strict_r = results["strict"]["rate"]
        perm_r = results["permissive"]["rate"]
        if strict_r is None or perm_r is None:
            row["strict_permissive_delta"] = None
            row["sensitivity"] = "undefined"
        else:
            delta = round(perm_r - strict_r, 4)
            row["strict_permissive_delta"] = delta
            row["sensitivity"] = (
                "robust" if abs(delta) < 0.05
                else "moderate" if abs(delta) < 0.10
                else "sensitive"
            )
        rows.append(row)
    return rows


def _write_csv(rows: list[dict[str, Any]], path: pathlib.Path) -> None:
    if not rows:
        path.write_text("")
        return
    fields = [
        "layer",
        "strict_num", "strict_den", "strict_rate",
        "current_num", "current_den", "current_rate",
        "permissive_num", "permissive_den", "permissive_rate",
        "strict_permissive_delta", "sensitivity",
    ]
    with path.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)


def _write_md(rows: list[dict[str, Any]], path: pathlib.Path,
              event_count: int) -> None:
    md = [
        "# Admission-protocol sensitivity ablation",
        "",
        f"Generated: `{now_utc_iso()}` · generator "
        "`scripts/build_admission_sensitivity.py` · corpus "
        f"n = {event_count} events.",
        "",
        "Three admission rubrics applied to the coverage-matched "
        "`changed_given_coverage` rate per layer:",
        "",
        "- **strict** — numerator and denominator over `measured` only; "
        "attribution `direct` only.",
        "- **current** — numerator and denominator over `measured` only; "
        "attribution `direct` or `plausible`.",
        "- **permissive** — numerator and denominator over `measured` "
        "or `partially_measured`; attribution `direct` or `plausible`.",
        "",
        "The `strict_permissive_delta` column is the absolute change "
        "in rate from strict to permissive. Sensitivity tier: "
        "**robust** (< 0.05), **moderate** (0.05–0.10), **sensitive** "
        "(≥ 0.10). A sensitive rate must be reported under all three "
        "rubrics in the paper; a robust rate may be reported under "
        "the `current` rubric only.",
        "",
        "## Table",
        "",
        "| layer | strict (num/den = rate) | current | permissive | Δ | sensitivity |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for r in rows:
        def cell(n: int, d: int, rate) -> str:
            if d == 0:
                return "— / 0 = —"
            return f"{n}/{d} = {rate:.3f}" if rate is not None else f"{n}/{d} = —"
        md.append(
            f"| `{r['layer']}` | "
            f"{cell(r['strict_num'], r['strict_den'], r['strict_rate'])} | "
            f"{cell(r['current_num'], r['current_den'], r['current_rate'])} | "
            f"{cell(r['permissive_num'], r['permissive_den'], r['permissive_rate'])} | "
            f"{r['strict_permissive_delta'] if r['strict_permissive_delta'] is not None else '—'} | "
            f"**{r['sensitivity']}** |"
        )
    md.extend([
        "",
        "## Interpretation",
        "",
        "- A **robust** layer means the rate does not depend on the "
        "partially_measured admission decision; a reader cannot "
        "accuse the authors of inflating the ratio by relaxing "
        "coverage.",
        "- A **sensitive** layer means the rate moves substantially "
        "(≥ 10 percentage points) between strict and permissive. "
        "The paper must report both rates and disclose the "
        "admission choice in the claim's phrasing.",
        "- A layer with `—` denominator under *strict* means no "
        "events have `measured` coverage at that layer (the "
        "`l0_network` and `l3_rpc` cases at v0.1). For those layers "
        "the paper should phrase the rate as an observability gap, "
        "not a conditional rate.",
        "",
        "This ablation is the reviewer-facing answer to "
        "\"can you inflate changed_given_measured by labeling events "
        "`partially_measured` loosely?\". If every paper-cited rate "
        "is in the `robust` tier, the answer is defensibly no.",
        "",
    ])
    path.write_text("\n".join(md))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out-dir", default=str(DEFAULT_OUT_DIR))
    args = parser.parse_args()

    out_dir = pathlib.Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    events = _load_events()
    rows = _compute_all(events)

    _write_csv(rows, out_dir / "admission_sensitivity.csv")
    _write_md(rows, out_dir / "admission_sensitivity.md", len(events))

    meta = load_meta()
    meta_out = {
        "generated_at": now_utc_iso(),
        "generator": "build_admission_sensitivity.py",
        "generator_version": "0.1.0",
        "dataset_version": meta.get("dataset_version"),
        "source_commit": meta.get("source_commit"),
        "cutoff_date": meta.get("cutoff_date"),
        "event_count": len(events),
        "rubrics": list(RUBRICS.keys()),
    }
    (out_dir / "admission_sensitivity.meta.json").write_text(
        json.dumps(meta_out, indent=2, sort_keys=True))
    print(f"[admission-sensitivity] wrote "
          f"{out_dir}/admission_sensitivity.{{csv,md,meta.json}}",
          file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
