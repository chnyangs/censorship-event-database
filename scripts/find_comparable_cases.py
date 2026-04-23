#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""
Layer B of the framework: given a proposed action (or a current event as a
reference), find the top-N most similar historical events in the dataset.

**CASE-BASED RETRIEVAL — NOT A PREDICTIVE MODEL.** See
`docs/limitations-and-use.md` §2.1. With 53 events, the tool returns
comparable precedents for human expert judgment, not probability forecasts.

Similarity is a transparent weighted sum of discrete matches — not a
learned model — so the reader can always see WHY a case ranked where it
did. Ranking breakdown is part of every output.

Usage (query mode — describe a proposed action):
    python3 scripts/find_comparable_cases.py \\
        --trigger-type ofac_sdn_designation \\
        --actor US_OFAC \\
        --stratum S1_ofac_sdn \\
        --chains bitcoin,ethereum \\
        --actor-type mixer_service \\
        --target-kind address_set \\
        --top 5

Usage (event mode — find cases similar to an existing event):
    python3 scripts/find_comparable_cases.py --like sinbad-ofac-2023 --top 5

Output is Markdown with per-case similarity breakdown, ranked list, and
the "divergence factors" each reader should weigh before treating the
precedent as applicable.
"""

from __future__ import annotations

import argparse
import json
import pathlib
import subprocess
import sys
from datetime import datetime, timezone
from typing import Any

import yaml


TOOL_VERSION = "0.1.0"
REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent
EVENTS_DIR = REPO_ROOT / "events"

# Shared dataset-identity accessor (see scripts/_dataset_meta.py).
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from _dataset_meta import load_meta  # noqa: E402


# ----------------------------------------------------------------------
# Similarity scoring — transparent, weighted discrete matches.
# Each feature has an explicit weight. Readers see the per-feature
# contribution. No ML, no hidden factors.
# ----------------------------------------------------------------------

FEATURE_WEIGHTS = {
    "trigger_type": 3.0,        # identical trigger.type
    "research_stratum": 2.5,    # same stratum (S1–S6)
    "actor": 2.0,               # identical trigger.actor
    "actor_family": 1.0,        # actor prefix match (US_DOJ_* family etc.)
    "chain_overlap": 2.0,       # fraction of chain overlap
    "target_kind": 1.5,         # same target.kind
    "actor_type": 1.5,          # same target.actor_type
    "protocol": 2.0,            # same protocol (if both set)
    "empirical_shape": 1.0,     # same cascade shape (post-hoc, optional)
    "jurisdiction_overlap": 1.0, # jurisdiction intersection
}
MAX_SCORE = sum(FEATURE_WEIGHTS.values())


def git_hash() -> str:
    try:
        r = subprocess.run(
            ["git", "rev-parse", "--short", "HEAD"],
            cwd=REPO_ROOT, capture_output=True, text=True, timeout=5,
        )
        return r.stdout.strip() or "unknown"
    except Exception:
        return "unknown"


def load_events() -> dict[str, dict]:
    return {f.stem: yaml.safe_load(f.read_text()) for f in EVENTS_DIR.glob("*.yaml")}


def query_from_event(event: dict) -> dict:
    """Build a similarity-query dict from an existing event."""
    trig = event.get("trigger") or {}
    tgt = event.get("target") or {}
    return {
        "trigger_type": trig.get("type"),
        "actor": trig.get("actor"),
        "research_stratum": event.get("research_stratum"),
        "empirical_shape": event.get("empirical_shape"),
        "chains": tgt.get("chains") or [],
        "target_kind": tgt.get("kind"),
        "actor_type": tgt.get("actor_type"),
        "protocol": tgt.get("protocol"),
        "jurisdiction": event.get("jurisdiction") or [],
    }


def score_similarity(query: dict, candidate: dict) -> tuple[float, dict]:
    """Return (total_score, per-feature breakdown)."""
    breakdown: dict[str, float] = {}
    c = query_from_event(candidate)

    def match(key):
        if query.get(key) is None or c.get(key) is None:
            return 0.0
        return 1.0 if query[key] == c[key] else 0.0

    breakdown["trigger_type"] = match("trigger_type") * FEATURE_WEIGHTS["trigger_type"]
    breakdown["research_stratum"] = match("research_stratum") * FEATURE_WEIGHTS["research_stratum"]
    breakdown["actor"] = match("actor") * FEATURE_WEIGHTS["actor"]
    breakdown["target_kind"] = match("target_kind") * FEATURE_WEIGHTS["target_kind"]
    breakdown["actor_type"] = match("actor_type") * FEATURE_WEIGHTS["actor_type"]
    breakdown["protocol"] = match("protocol") * FEATURE_WEIGHTS["protocol"]
    breakdown["empirical_shape"] = match("empirical_shape") * FEATURE_WEIGHTS["empirical_shape"]

    # Actor family: prefix match (US_DOJ_SDNY & US_DOJ_EDPA share "US_DOJ_")
    a1, a2 = str(query.get("actor") or ""), str(c.get("actor") or "")
    if a1 and a2 and a1 != a2:
        # find longest underscore-aligned common prefix
        parts1, parts2 = a1.split("_"), a2.split("_")
        prefix_len = 0
        for p1, p2 in zip(parts1, parts2):
            if p1 == p2:
                prefix_len += 1
            else:
                break
        if prefix_len >= 2:  # at least 2 tokens common (e.g. US_DOJ)
            breakdown["actor_family"] = 0.7 * FEATURE_WEIGHTS["actor_family"]
        else:
            breakdown["actor_family"] = 0.0
    else:
        breakdown["actor_family"] = 0.0

    # Chain overlap: Jaccard
    q_chains, c_chains = set(query.get("chains") or []), set(c.get("chains") or [])
    if q_chains and c_chains:
        jac = len(q_chains & c_chains) / len(q_chains | c_chains)
        breakdown["chain_overlap"] = jac * FEATURE_WEIGHTS["chain_overlap"]
    else:
        breakdown["chain_overlap"] = 0.0

    # Jurisdiction overlap: Jaccard
    q_j, c_j = set(query.get("jurisdiction") or []), set(c.get("jurisdiction") or [])
    if q_j and c_j:
        jac = len(q_j & c_j) / len(q_j | c_j)
        breakdown["jurisdiction_overlap"] = jac * FEATURE_WEIGHTS["jurisdiction_overlap"]
    else:
        breakdown["jurisdiction_overlap"] = 0.0

    total = sum(breakdown.values())
    return total, breakdown


def divergence_factors(query: dict, candidate: dict) -> list[str]:
    """
    Enumerate the structural differences that the reader should weigh
    before treating the precedent as applicable. These are the 'but this
    case differs because...' bullets — the antidote to naive precedent
    application.
    """
    c = query_from_event(candidate)
    diffs = []

    q_chains = set(query.get("chains") or [])
    c_chains = set(c.get("chains") or [])
    if q_chains != c_chains and q_chains and c_chains:
        missing = q_chains - c_chains
        extra = c_chains - q_chains
        if missing:
            diffs.append(f"query targets chain(s) {sorted(missing)} not in this precedent")
        if extra:
            diffs.append(f"precedent targets extra chain(s) {sorted(extra)} not in query")

    if query.get("actor") and c.get("actor") and query["actor"] != c["actor"]:
        diffs.append(f"different actor: query={query['actor']} vs precedent={c['actor']}")

    if query.get("target_kind") != c.get("target_kind"):
        diffs.append(f"different target kind: query={query.get('target_kind')} vs precedent={c.get('target_kind')}")

    if query.get("protocol") and c.get("protocol") and query["protocol"] != c["protocol"]:
        diffs.append(f"different protocol context: {query['protocol']} vs {c['protocol']}")

    # Pre-Merge vs post-Merge: relevant if one is before 2022-09-15 and the other after
    cand_ts = str((candidate.get("trigger") or {}).get("timestamp", ""))[:10]
    # (already str-wrapped above — keep defensive)
    if cand_ts and cand_ts < "2022-09-15":
        diffs.append(f"precedent is pre-Merge ({cand_ts}); L1/L3 constructs may not apply")

    q_j = set(query.get("jurisdiction") or [])
    c_j = set(c.get("jurisdiction") or [])
    if q_j and c_j and q_j != c_j:
        diffs.append(f"different jurisdiction set: query={sorted(q_j)} vs precedent={sorted(c_j)}")

    return diffs


def summarize_cascade(event: dict) -> dict:
    """Descriptive summary of what actually happened in this event (per-layer)."""
    obs = event.get("observations") or []
    per_layer: dict[str, list[str]] = {}
    for o in obs:
        layer = o.get("layer", "?")
        kind = o.get("observation_kind", "?")
        attr = o.get("attribution", "?")
        dh = o.get("delta_hours")
        per_layer.setdefault(layer, []).append(f"{kind}/{attr}/Δt={dh}h")
    return per_layer


def render_report(
    query: dict,
    reference_slug: str | None,
    ranked: list[tuple[str, float, dict]],
    all_events: dict[str, dict],
    top_n: int,
) -> str:
    meta = load_meta()
    dv = meta.get("dataset_version") or "unknown"
    cutoff = meta.get("cutoff_date") or "n/a"
    commit = meta.get("source_commit") or ""
    out = []
    out.append("# Comparable-case retrieval")
    out.append("")
    out.append(
        f"**Dataset version**: `{dv}` · **Cutoff**: `{cutoff}`"
        + (f" · **Commit**: `{commit}`" if commit else "")
        + f" · **Schema**: `{meta.get('schema_version') or '0.2.0'}` · "
        f"**Tool version**: `{TOOL_VERSION}` · "
        f"**Generated**: `{datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')}` · "
        f"**Universe**: {len(all_events)} admitted events"
    )
    out.append("")
    out.append("> ⚠️ **This is case-based retrieval, not a predictive model.** "
               "The ranked list below shows historical events structurally similar "
               "to the query by transparent feature weights. It does **NOT** "
               "estimate the probability of any specific outcome for any future "
               "action. Read [`docs/limitations-and-use.md`](../docs/limitations-and-use.md) "
               "before citing this output.")
    out.append("")

    out.append("## Query")
    out.append("")
    if reference_slug:
        out.append(f"Using existing event `{reference_slug}` as reference.")
        out.append("")
    for k in ["trigger_type", "actor", "research_stratum", "empirical_shape",
              "target_kind", "actor_type", "protocol", "chains", "jurisdiction"]:
        v = query.get(k)
        if v:
            out.append(f"- **{k}**: `{v}`")
    out.append("")

    out.append("## Similarity feature weights")
    out.append("")
    for feat, w in FEATURE_WEIGHTS.items():
        out.append(f"- `{feat}`: {w}")
    out.append(f"- **max possible raw score**: {MAX_SCORE}")
    out.append("")

    out.append(f"## Top {top_n} comparable cases")
    out.append("")
    for rank, (slug, score, breakdown) in enumerate(ranked[:top_n], 1):
        cand = all_events[slug]
        pct = 100.0 * score / MAX_SCORE
        out.append(f"### {rank}. `{slug}` — score {score:.2f} / {MAX_SCORE:.2f} "
                   f"({pct:.0f}% match)")
        out.append("")
        out.append(f"**Stratum**: `{cand.get('research_stratum','?')}` · "
                   f"**Shape**: `{cand.get('empirical_shape','?')}` · "
                   f"**Tier**: `{cand.get('admission_tier','?')}` · "
                   f"**Trigger**: `{str((cand.get('trigger') or {}).get('timestamp','?'))[:10]}`")
        out.append("")
        # Feature contribution breakdown
        out.append("**Why this ranked here** (feature → contribution):")
        contribs = sorted(breakdown.items(), key=lambda x: (-x[1], x[0]))
        for feat, contrib in contribs:
            if contrib > 0:
                out.append(f"- `{feat}`: +{contrib:.2f}")
        zero_contribs = [f for f, c in contribs if c == 0]
        if zero_contribs:
            out.append(f"- zero-contribution features: {', '.join(f'`{f}`' for f in zero_contribs)}")
        out.append("")
        # Cascade summary
        cascade = summarize_cascade(cand)
        if cascade:
            out.append("**What happened in this precedent** (per-layer):")
            for layer, entries in sorted(cascade.items()):
                out.append(f"- `{layer}`: {'; '.join(entries)}")
            out.append("")
        # Scoped claim of precedent
        sc = (cand.get("scoped_claim") or "").strip()
        if sc:
            out.append("**Precedent's scoped claim**:")
            for line in sc.split("\n"):
                out.append(f"> {line}")
            out.append("")
        # Divergence factors
        diffs = divergence_factors(query, cand)
        if diffs:
            out.append("**⚠ Divergence factors** — read these before treating this "
                       "precedent as applicable to the query:")
            for d in diffs:
                out.append(f"- {d}")
            out.append("")
        # Link to evidence chain
        out.append(f"**Full evidence chain**: [`analysis/evidence-chains/{slug}.md`](../analysis/evidence-chains/{slug}.md)")
        out.append("")
        out.append("---")
        out.append("")

    # Honest notes
    out.append("## How to read this output")
    out.append("")
    out.append("1. **A high match score does not mean high applicability.** Two "
               "events can share structural features but diverge on a factor "
               "that dominates outcomes (e.g., foreign-operator vs US-operator "
               "frontend determines L4 cascade shape). Read the divergence "
               "factors for each ranked case.")
    out.append("2. **The tool reports what historically happened; it does not "
               "forecast what will happen.** With 53 events, some structural "
               "slots contain only 1–2 precedents. Any statistical claim "
               "derived downstream must report sample size.")
    out.append("3. **If all top candidates have score < 40% of max, the query "
               "is structurally novel.** The correct response is to document "
               "that, not to force-fit the closest partial match.")
    out.append("4. **Primary sources remain the authority.** Every event links "
               "to its `body_hash`'d primary sources. Do not cite the "
               "summary above; cite the sources.")
    out.append("")

    return "\n".join(out) + "\n"


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    p.add_argument("--like", help="existing event slug to use as reference query")
    p.add_argument("--trigger-type")
    p.add_argument("--actor")
    p.add_argument("--stratum", dest="research_stratum")
    p.add_argument("--shape", dest="empirical_shape")
    p.add_argument("--chains", help="comma-separated list")
    p.add_argument("--target-kind")
    p.add_argument("--actor-type")
    p.add_argument("--protocol")
    p.add_argument("--jurisdiction", help="comma-separated list")
    p.add_argument("--top", type=int, default=5)
    p.add_argument("--output", default="-", help="output path or '-' for stdout")
    args = p.parse_args()

    events = load_events()

    if args.like:
        if args.like not in events:
            sys.exit(f"no event {args.like!r}")
        query = query_from_event(events[args.like])
        ref = args.like
        # Exclude the reference from its own top-N
        candidates = {k: v for k, v in events.items() if k != args.like}
    else:
        query = {
            "trigger_type": args.trigger_type,
            "actor": args.actor,
            "research_stratum": args.research_stratum,
            "empirical_shape": args.empirical_shape,
            "chains": [c.strip() for c in (args.chains or "").split(",") if c.strip()],
            "target_kind": args.target_kind,
            "actor_type": args.actor_type,
            "protocol": args.protocol,
            "jurisdiction": [j.strip() for j in (args.jurisdiction or "").split(",") if j.strip()],
        }
        ref = None
        candidates = events

    scored = []
    for slug, ev in candidates.items():
        score, breakdown = score_similarity(query, ev)
        scored.append((slug, score, breakdown))
    scored.sort(key=lambda x: (-x[1], x[0]))

    report = render_report(query, ref, scored, events, args.top)

    if args.output == "-":
        sys.stdout.write(report)
    else:
        pathlib.Path(args.output).parent.mkdir(parents=True, exist_ok=True)
        pathlib.Path(args.output).write_text(report)
        print(f"[find_comparable_cases] wrote {args.output}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
