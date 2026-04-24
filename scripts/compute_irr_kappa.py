#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Compute Cohen's κ (and related agreement statistics) between the
blind recode worksheet and the gold key for each variable.

Inputs (default dir `analysis/inter_rater/`):
    <var>_blind.csv  — has `recode_value` column (second coder's answers)
    <var>_key.csv    — has `original_value` column (first coder's gold)

Output:
    analysis/inter_rater/kappa_report.md
    analysis/inter_rater/kappa_report.json

Cohen's κ (two-coder categorical) with notes on cells where the blind
worksheet is incomplete (missing `recode_value`), which are treated
as "coder declined" and tallied separately from agreement.
"""
from __future__ import annotations

import argparse
import csv
import json
import pathlib
import sys
from collections import Counter
from typing import Iterable

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from _dataset_meta import now_utc_iso  # noqa: E402

REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent


def _load_csv(path: pathlib.Path) -> list[dict]:
    if not path.exists():
        return []
    with path.open() as f:
        return list(csv.DictReader(f))


def _join_blind_key(blind: list[dict], key: list[dict]) -> list[tuple[str, str, str, str]]:
    """Return list of (event_id, layer, recode, original).

    Prefers an explicit `row_id` join (sampler v0.2+ writes one). If
    `row_id` is not present in either side, falls back to a stable
    (event_id, layer) zip but **errors loudly** when the two sides
    disagree on the multiset of (event_id, layer) keys — the
    earlier silent-zip behavior could miscount on duplicate
    observations once either CSV got reordered.
    """
    if blind and "row_id" in blind[0] and key and "row_id" in key[0]:
        key_by_id = {r["row_id"]: r for r in key}
        pairs = []
        for b in blind:
            k = key_by_id.get(b["row_id"])
            if k is None:
                raise ValueError(
                    f"row_id {b['row_id']} present in blind but not in key")
            pairs.append((b["event_id"], b["layer"],
                          (b.get("recode_value") or "").strip(),
                          (k.get("original_value") or "").strip()))
        return pairs

    # Backward-compat path for sampler v0.1 outputs without row_id.
    blind_keys = sorted([(r["event_id"], r["layer"]) for r in blind])
    key_keys = sorted([(r["event_id"], r["layer"]) for r in key])
    if blind_keys != key_keys:
        raise ValueError(
            "blind/key (event_id, layer) multisets differ and no "
            "`row_id` is present — regenerate with the v0.2+ sampler "
            "(`make irr-sample`).")
    by_pair: dict[tuple[str, str], list[str]] = {}
    for r in key:
        by_pair.setdefault((r["event_id"], r["layer"]), []).append(
            r.get("original_value", ""))
    pairs = []
    used_idx: dict[tuple[str, str], int] = {}
    for b in blind:
        k = (b["event_id"], b["layer"])
        idx = used_idx.get(k, 0)
        key_vals = by_pair.get(k, [])
        original = key_vals[idx] if idx < len(key_vals) else ""
        used_idx[k] = idx + 1
        pairs.append((b["event_id"], b["layer"],
                      (b.get("recode_value") or "").strip(),
                      (original or "").strip()))
    return pairs


def _cohens_kappa(pairs: list[tuple[str, str, str, str]]) -> dict:
    coded = [(a, b) for _, _, a, b in pairs if a and b]
    if not coded:
        return {"kappa": None, "agreement": None, "n_coded": 0,
                "n_total": len(pairs),
                "confusion": {}, "observed_agreement": None,
                "expected_agreement": None,
                "reason": "no coded cells"}
    labels = sorted({c[0] for c in coded} | {c[1] for c in coded})
    conf: dict[str, dict[str, int]] = {a: {b: 0 for b in labels}
                                       for a in labels}
    for a, b in coded:
        conf[a][b] += 1
    n = len(coded)
    # marginals
    marg_a = {a: sum(conf[a].values()) / n for a in labels}
    marg_b = {b: sum(conf[a][b] for a in labels) / n for b in labels}
    po = sum(conf[x][x] for x in labels) / n
    pe = sum(marg_a[x] * marg_b[x] for x in labels)
    if pe >= 1.0:
        kappa = 1.0
    else:
        kappa = (po - pe) / (1 - pe)
    return {
        "kappa": round(kappa, 4),
        "observed_agreement": round(po, 4),
        "expected_agreement": round(pe, 4),
        "agreement": round(po, 4),  # alias for readability
        "n_coded": n,
        "n_total": len(pairs),
        "confusion": conf,
        "label_set": labels,
    }


def _interpret(k: float | None) -> str:
    if k is None:
        return "—"
    if k < 0:
        return "worse than chance"
    if k < 0.2:
        return "slight"
    if k < 0.4:
        return "fair"
    if k < 0.6:
        return "moderate"
    if k < 0.8:
        return "substantial"
    return "almost perfect"


def _render_confusion(conf: dict[str, dict[str, int]]) -> list[str]:
    if not conf:
        return ["_(no confusion matrix; no coded cells)_"]
    labels = sorted(conf.keys())
    header = "| recode \\ original | " + " | ".join(labels) + " |"
    sep = "| --- | " + " | ".join("---" for _ in labels) + " |"
    lines = [header, sep]
    for a in labels:
        row = f"| **{a}** | " + " | ".join(
            str(conf[a].get(b, 0)) for b in labels) + " |"
        lines.append(row)
    return lines


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dir", default="analysis/inter_rater")
    parser.add_argument("--variables",
                        default="coverage_status,observation_kind,attribution")
    parser.add_argument("--coder-mode",
                        choices=("independent_human", "llm_assisted_blinded",
                                 "author_self_recode_60d_gap", "unspecified"),
                        default="unspecified",
                        help="Provenance class of the second coder. "
                             "Recorded under coder_provenance.mode in JSON.")
    parser.add_argument("--coder-name", default="",
                        help="Recoder name or model id "
                             "(e.g. \"claude-opus-4-7\" or \"J. Smith\").")
    parser.add_argument("--coder-prompt-version", default="",
                        help="Identifier for the prompt template "
                             "or rubric version used by the recoder.")
    parser.add_argument("--coder-notes", default="",
                        help="Free-form notes (date, blindness "
                             "verification, ambiguity flags).")
    args = parser.parse_args()

    base = REPO_ROOT / args.dir
    vars_list = [v.strip() for v in args.variables.split(",") if v.strip()]
    report_json: dict[str, dict] = {
        "generated_at": now_utc_iso(),
        "coder_provenance": {
            "mode": args.coder_mode,
            "coder_name": args.coder_name,
            "prompt_version": args.coder_prompt_version,
            "notes": args.coder_notes,
        },
        "variables": {},
    }
    cp = report_json["coder_provenance"]
    md = [
        "# Inter-rater reliability report",
        "",
        f"Generated: `{now_utc_iso()}` · computer "
        "`scripts/compute_irr_kappa.py` · blind/key inputs from "
        f"`{args.dir}/`.",
        "",
        "## Coder provenance",
        "",
        f"- **Mode**: `{cp['mode']}` (one of `independent_human`, "
        "`llm_assisted_blinded`, `author_self_recode_60d_gap`, "
        "`unspecified` — published κ requires non-`unspecified` "
        "provenance).",
        f"- **Coder**: `{cp['coder_name'] or '—'}`",
        f"- **Prompt / rubric version**: `{cp['prompt_version'] or '—'}`",
        f"- **Notes**: {cp['notes'] or '—'}",
        "",
        "| variable | n coded / n total | observed agreement | Cohen's κ | label |",
        "| --- | --- | --- | --- | --- |",
    ]
    for var in vars_list:
        blind = _load_csv(base / f"{var}_blind.csv")
        key = _load_csv(base / f"{var}_key.csv")
        pairs = _join_blind_key(blind, key)
        res = _cohens_kappa(pairs)
        report_json["variables"][var] = res
        md.append(
            f"| `{var}` | {res['n_coded']} / {res['n_total']} | "
            f"{res['observed_agreement'] if res['observed_agreement'] is not None else '—'} | "
            f"{res['kappa'] if res['kappa'] is not None else '—'} | "
            f"{_interpret(res['kappa'])} |"
        )
    md.append("")
    for var in vars_list:
        res = report_json["variables"][var]
        md.extend([
            f"## `{var}` detail",
            "",
            f"- n_coded: **{res['n_coded']}** of {res['n_total']} rows "
            "(remaining rows are missing `recode_value` — coder-incomplete)",
            f"- observed agreement p_o = {res['observed_agreement']}",
            f"- expected agreement p_e = {res['expected_agreement']}",
            f"- Cohen's κ = **{res['kappa']}** ({_interpret(res['kappa'])})",
            "",
            "### Confusion matrix",
            "",
            *_render_confusion(res.get("confusion") or {}),
            "",
        ])
    md.extend([
        "## Interpretation",
        "",
        "Cohen's κ thresholds (Landis & Koch 1977 — still the most "
        "cited convention despite known limitations with skewed "
        "marginals): < 0.2 slight, 0.2–0.4 fair, 0.4–0.6 moderate, "
        "0.6–0.8 substantial, > 0.8 almost perfect.",
        "",
        "**Paper-readiness threshold** for this project: κ ≥ 0.6 on "
        "all three variables. A variable below 0.6 blocks the "
        "coverage-matched rate claim that depends on it (C1 for "
        "coverage_status, C2 for observation_kind, attribution-tier "
        "phrasing lock for attribution).",
        "",
        "**Honest labeling**: the second coder in this artifact may be "
        "the same author as the gold coder (self-recode) or an "
        "LLM-assisted recoder. The report emits whichever is run. "
        "The protocol is encoded in `scripts/build_irr_sample.py` "
        "and `scripts/compute_irr_kappa.py`.",
        "",
    ])

    (base / "kappa_report.md").write_text("\n".join(md))
    (base / "kappa_report.json").write_text(
        json.dumps(report_json, indent=2, sort_keys=True))
    print(f"[irr] wrote {base}/kappa_report.md and .json", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
