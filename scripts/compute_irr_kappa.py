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
from _kappa_ci import (  # noqa: E402
    bootstrap_ci, cohen_kappa_value, fleiss_kappa_value)

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


def _fleiss_kappa(per_row_votes: list[list[str]]) -> dict:
    """Fleiss' κ across n_raters on each row.

    `per_row_votes[i]` = list of labels the n_raters assigned to row i.
    Rows where any rater produced an empty string are dropped from the
    coded set. Returns kappa + observed/expected agreement + label set.
    """
    coded = [v for v in per_row_votes if all(x and x.strip() for x in v)]
    if not coded:
        return {"fleiss_kappa": None, "p_bar": None, "pe_bar": None,
                "n_coded_rows": 0, "n_total_rows": len(per_row_votes),
                "n_raters": (len(per_row_votes[0]) if per_row_votes else 0),
                "reason": "no fully-coded rows"}
    n_raters = len(coded[0])
    if any(len(v) != n_raters for v in coded):
        return {"fleiss_kappa": None, "reason": "inconsistent rater counts",
                "n_coded_rows": len(coded), "n_total_rows": len(per_row_votes)}
    labels = sorted({label for row in coded for label in row})
    n_rows = len(coded)
    # P_j = proportion of all assignments to label j
    total_assignments = n_rows * n_raters
    label_counts = {lbl: 0 for lbl in labels}
    for row in coded:
        for lbl in row:
            label_counts[lbl] += 1
    p_j = {lbl: label_counts[lbl] / total_assignments for lbl in labels}
    # P_i = agreement among raters on row i
    # P_i = (1 / (n*(n-1))) * (sum_j(n_ij^2) - n)
    p_i_values = []
    for row in coded:
        counts: dict[str, int] = {}
        for lbl in row:
            counts[lbl] = counts.get(lbl, 0) + 1
        s = sum(c * c for c in counts.values())
        if n_raters <= 1:
            p_i = 1.0
        else:
            p_i = (s - n_raters) / (n_raters * (n_raters - 1))
        p_i_values.append(p_i)
    p_bar = sum(p_i_values) / n_rows
    pe_bar = sum(v * v for v in p_j.values())
    if pe_bar >= 1.0:
        fleiss_kappa = 1.0
    else:
        fleiss_kappa = (p_bar - pe_bar) / (1 - pe_bar)
    return {
        "fleiss_kappa": round(fleiss_kappa, 4),
        "p_bar": round(p_bar, 4),
        "pe_bar": round(pe_bar, 4),
        "n_coded_rows": n_rows,
        "n_total_rows": len(per_row_votes),
        "n_raters": n_raters,
        "label_set": labels,
        "kappa_ci": bootstrap_ci(coded, fleiss_kappa_value),
    }


def _load_agent_csvs(base_dir: pathlib.Path, variable: str) -> list[list[dict]]:
    """Load any per-agent CSVs matching `{variable}_agent_*.csv` from
    `base_dir/agent_outputs/`. Each CSV must have `row_id` and
    `recode_value` columns. Returns list of agent recode-lists.
    """
    agent_dir = base_dir / "agent_outputs"
    if not agent_dir.exists():
        return []
    csvs = sorted(agent_dir.glob(f"{variable}_agent_*.csv"))
    out = []
    for p in csvs:
        with p.open() as f:
            out.append(list(csv.DictReader(f)))
    return out


def _majority_vote(agent_csvs: list[list[dict]]) -> dict[str, tuple[str, list[str]]]:
    """For each row_id, return (winning_label, all_votes).
    Ties → '' (empty string, surfaced for human review).
    """
    if not agent_csvs:
        return {}
    by_row: dict[str, list[str]] = {}
    for agent_rows in agent_csvs:
        for r in agent_rows:
            rid = str(r.get("row_id", ""))
            v = (r.get("recode_value") or "").strip()
            by_row.setdefault(rid, []).append(v)
    out: dict[str, tuple[str, list[str]]] = {}
    for rid, votes in by_row.items():
        if any(v == "" for v in votes):
            out[rid] = ("", votes)
            continue
        counts: dict[str, int] = {}
        for v in votes:
            counts[v] = counts.get(v, 0) + 1
        top = sorted(counts.items(), key=lambda kv: (-kv[1], kv[0]))
        if len(top) > 1 and top[0][1] == top[1][1]:
            out[rid] = ("", votes)  # tie → surface
        else:
            out[rid] = (top[0][0], votes)
    return out


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
        "kappa_ci": bootstrap_ci(coded, cohen_kappa_value),
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


def _ci_str(ci: dict | None) -> str:
    if not ci:
        return ""
    return f" [{ci['ci_low']}, {ci['ci_high']}]"


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
                                 "llm_assisted_consensus_3x",
                                 "independent_human_dryrun_llm_simulated",
                                 "author_self_recode_60d_gap", "unspecified"),
                        default="unspecified",
                        help="Provenance class of the second coder. "
                             "`llm_assisted_consensus_3x` = 3 blind LLM "
                             "agents voted majority into the master "
                             "recode_value column; the report adds Fleiss' "
                             "κ across the 3 agents alongside Cohen's κ "
                             "vs the gold. Still NOT independent-human "
                             "reliability — three same-distribution LLMs "
                             "share biases. Recorded under "
                             "coder_provenance.mode in JSON.")
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
        "`llm_assisted_blinded`, `llm_assisted_consensus_3x`, "
        "`independent_human_dryrun_llm_simulated`, "
        "`author_self_recode_60d_gap`, `unspecified` — published κ "
        "requires non-`unspecified` provenance, and reliability claims "
        "require `independent_human`).",
        f"- **Coder**: `{cp['coder_name'] or '—'}`",
        f"- **Prompt / rubric version**: `{cp['prompt_version'] or '—'}`",
        f"- **Notes**: {cp['notes'] or '—'}",
        "",
        "| variable | n coded / n total | observed agreement | Cohen's κ (vs gold) [95% CI] | Fleiss' κ (across LLM agents) | label |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for var in vars_list:
        # 3-agent aggregation: if `agent_outputs/{var}_agent_*.csv`
        # exist, majority-vote them into the master blind CSV and also
        # compute Fleiss' κ across the n_agents votes.
        agent_csvs = _load_agent_csvs(base, var)
        agent_fleiss: dict | None = None
        if agent_csvs and len(agent_csvs) >= 2:
            agent_fleiss = _fleiss_kappa([
                [(r.get("recode_value") or "").strip()
                 for r in agent_rows]
                for agent_rows in zip(*[list(c) for c in
                                        # align by row_id
                                        [sorted(c, key=lambda r: int(r["row_id"]))
                                         for c in agent_csvs]])
            ])
            # majority-vote → master blind CSV
            master_path = base / f"{var}_blind.csv"
            master_rows = _load_csv(master_path)
            votes = _majority_vote(agent_csvs)
            for r in master_rows:
                rid = str(r.get("row_id", ""))
                winner, all_votes = votes.get(rid, ("", []))
                r["recode_value"] = winner
                r["recoder_comment"] = (
                    f"3-agent votes={','.join(all_votes)}"
                    + (" [TIE — flagged for human]" if winner == "" and all_votes else "")
                ).strip()
            if master_rows:
                with master_path.open("w", newline="") as f:
                    w = csv.DictWriter(f, fieldnames=list(master_rows[0].keys()))
                    w.writeheader()
                    w.writerows(master_rows)
        blind = _load_csv(base / f"{var}_blind.csv")
        key = _load_csv(base / f"{var}_key.csv")
        pairs = _join_blind_key(blind, key)
        res = _cohens_kappa(pairs)
        if agent_fleiss is not None:
            res["fleiss_across_agents"] = agent_fleiss
            res["n_agents"] = agent_fleiss.get("n_raters")
        report_json["variables"][var] = res
        fleiss_str = (
            f"{agent_fleiss['fleiss_kappa']} ({agent_fleiss['n_raters']}r)"
            if agent_fleiss and agent_fleiss.get("fleiss_kappa") is not None
            else "—"
        )
        kappa_cell = ("—" if res['kappa'] is None
                      else f"{res['kappa']}{_ci_str(res.get('kappa_ci'))}")
        md.append(
            f"| `{var}` | {res['n_coded']} / {res['n_total']} | "
            f"{res['observed_agreement'] if res['observed_agreement'] is not None else '—'} | "
            f"{kappa_cell} | "
            f"{fleiss_str} | "
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
            (f"- 95% CI (bootstrap, B={res['kappa_ci']['n_boot']}): "
             f"**[{res['kappa_ci']['ci_low']}, {res['kappa_ci']['ci_high']}]**, "
             f"SE = {res['kappa_ci']['se']}"
             if res.get("kappa_ci")
             else "- 95% CI: — (coded-n too small for a bootstrap interval)"),
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
        "0.6–0.8 substantial, > 0.8 almost perfect on the Landis & "
        "Koch scale.",
        "",
        "**Read κ with its CI, not as a point.** Each κ above carries a "
        "seeded nonparametric bootstrap 95% CI (B=2000 resamples of the "
        "coded cells). On the small coded-n of this subset those intervals "
        "are wide, so a point estimate near the 0.6 paper-readiness gate "
        "is not a clean pass/fail: a variable whose CI straddles 0.6 has "
        "not been shown to clear it. Perfect-agreement variables yield a "
        "degenerate [1.0, 1.0] interval (every resample agrees), which is "
        "honest but reflects the easy variables, not the contested ones. "
        "Any published κ must be cited with its CI and coded-n.",
        "",
        "**What this κ does and does not establish — read before "
        "citing.** Under the Landis & Koch scale, κ ≥ 0.8 is labeled "
        "*almost perfect agreement*. That label applies to **inter-coder "
        "agreement under the protocol's coder-provenance mode** (see "
        "`coder_provenance.mode` above). It does NOT establish *inter-"
        "rater reliability* in the audited-research sense unless that "
        "mode is `independent_human` and the second coder is "
        "demonstrably blind to the gold coder's reasoning.",
        "",
        "- `independent_human`: the published κ is a reliability "
        "  estimate; cite as such.",
        "- `llm_assisted_blinded`: the published κ is a "
        "  **self-consistency check** — the recoder is from the same "
        "  model family / training distribution as a likely "
        "  author-assist substrate, and the gold and recode share "
        "  systematic biases. Cite as `self-consistency, single-coder "
        "  LLM-assisted recode` and treat the κ floor as a *lower bound* "
        "  on consistency, not a reliability estimate.",
        "- `llm_assisted_consensus_3x`: same caveat, with three blind "
        "  LLM agents majority-voted into the master recode and Fleiss' "
        "  κ reported across agents. Cite as consensus self-consistency, "
        "  not independent-human reliability.",
        "- `independent_human_dryrun_llm_simulated`: dryrun-only "
        "  pipeline rehearsal label. Do not cite as reliability and do "
        "  not use for a real release unless the paper-readiness gate is "
        "  being run with an explicit dryrun allowance.",
        "- `author_self_recode_60d_gap`: similar caveat (residual "
        "  recall risk); cite the gap length explicitly.",
        "- `unspecified`: do not cite the κ in the paper.",
        "",
        "**Paper-readiness threshold** for this project: a `current` "
        "rubric C1 rate that depends on a variable with κ < 0.6 (under "
        "the strictest available provenance mode) is blocked. C1 "
        "depends on `coverage_status`; C2 (PARKED v0.1) depends on "
        "`observation_kind`; the attribution-tier phrasing lock depends "
        "on `attribution`. Variables with no `independent_human` pass "
        "are the largest open validity threat for the v0.1 paper and "
        "are tracked in `docs/paper_claims.md §0` "
        "('Reliability discipline').",
        "",
    ])

    (base / "kappa_report.md").write_text("\n".join(md))
    (base / "kappa_report.json").write_text(
        json.dumps(report_json, indent=2, sort_keys=True))
    print(f"[irr] wrote {base}/kappa_report.md and .json", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
