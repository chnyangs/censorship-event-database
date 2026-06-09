"""
llm_baseline_coverage.py — LLM reference baselines for the coverage-prediction task.

Calls the local `claude` CLI (subscription auth) as a PREDICTOR: given only a
trigger descriptor (zero-shot) or descriptor + train-set coverage priors
(grounded), the model predicts the 6-layer coverage-state vector. Scored with the
SAME metrics as the simple baselines (scope-F1 / cond-qual / 4-class macro-F1) on
a recent holdout (year >= 2025; the model's cutoff is earlier so it cannot recall
these events). CLI calls run in parallel to amortise cold-start.

Usage:  python scripts/llm_baseline_coverage.py <haiku|sonnet> <zeroshot|grounded> [workers]
Writes per-event predictions to /tmp/llmpred_<model>_<mode>.json for later compile.

CAVEATS (printed): (1) gold labels are LLM-coded -> shared-process bias; read as a
REFERENCE, not ground truth. (2) LLM-prior baseline, not a strict temporal-holdout
learner. (3) grounded mode is in-context learning on the train split only.
"""

import glob, json, subprocess, sys, collections
from concurrent.futures import ThreadPoolExecutor
import numpy as np
import yaml

MODEL = sys.argv[1] if len(sys.argv) > 1 else "haiku"
MODE = sys.argv[2] if len(sys.argv) > 2 else "zeroshot"
CUTOFF = int(sys.argv[3]) if len(sys.argv) > 3 else 2025
WORKERS = int(sys.argv[4]) if len(sys.argv) > 4 else 8
LAYERS = ["l0_network", "l1_consensus", "l3_rpc", "l4_frontend",
          "asset_onchain", "offramp_cex"]
COVER = ["measured", "partially_measured", "not_measured", "not_applicable"]
NA = "not_applicable"
STRATA = ["S1_ofac_sdn", "S2_ofac_removal", "S3_doj_sec_cftc_fiod",
          "S4_nation_state", "S5_corporate", "S6_supranational"]


def load():
    rows = []
    for f in sorted(glob.glob("events/*.yaml")):
        d = yaml.safe_load(open(f))
        if not isinstance(d, dict) or d.get("status") != "admitted":
            continue
        trig = d.get("trigger") or {}
        ts = str(trig.get("timestamp") or "")
        if not ts[:4].isdigit():
            continue
        jur = d.get("jurisdiction") or []
        jur = [jur] if isinstance(jur, str) else jur
        cov = {c["layer"]: c.get("status") for c in (d.get("coverage") or [])
               if isinstance(c, dict)}
        rows.append({
            "feat": {"stratum": d.get("research_stratum") or "?",
                     "trigger_type": trig.get("type") or "?",
                     "us": "US" in jur,
                     "target_kind": (d.get("target") or {}).get("kind") or "?",
                     "year": int(ts[:4])},
            "labels": {L: (cov.get(L, NA) if cov.get(L, NA) in COVER else NA) for L in LAYERS},
            "year": int(ts[:4])})
    return rows


def macro_f1(gold, pred):
    f1s = []
    for c in set(gold) | set(pred):
        tp = sum(g == c and p == c for g, p in zip(gold, pred))
        fp = sum(g != c and p == c for g, p in zip(gold, pred))
        fn = sum(g == c and p != c for g, p in zip(gold, pred))
        pr = tp / (tp + fp) if tp + fp else 0.0
        rc = tp / (tp + fn) if tp + fn else 0.0
        f1s.append(2 * pr * rc / (pr + rc) if pr + rc else 0.0)
    return float(np.mean(f1s)) if f1s else 0.0


def scope_f1(g, p):
    return macro_f1(["na" if x == NA else "app" for x in g],
                    ["na" if x == NA else "app" for x in p])


def cond_quality(g, p):
    idx = [i for i, x in enumerate(g) if x != NA]
    return macro_f1([g[i] for i in idx], [p[i] for i in idx]) if idx else float("nan")


# ---- build prompt ----
BASE = """You predict, for a NEW crypto-censorship enforcement trigger, which stack layers will carry PUBLIC, REPLAYABLE evidence of a reaction — the COVERAGE STATE per layer. You are NOT predicting whether enforcement happens; you predict WHERE observable public evidence will exist.

Six stack layers:
- l0_network: ISP/DNS/national network blocking, app-store/geo removals (poorest public evidence).
- l1_consensus: relay/builder/validator OFAC filtering on Ethereum.
- l3_rpc: node-provider (Infura/Alchemy/Flashbots) endpoint or address blocks.
- l4_frontend: web/app UI geoblock, takedown, app-store removal, domain seizure.
- asset_onchain: token-issuer on-chain freeze/blacklist (USDC/USDT); needs an on-chain tx.
- offramp_cex: centralized-exchange delisting, KYC gating, jurisdiction exit, account freeze (by far the largest public-evidence denominator).

Coverage states:
- measured: this layer is systematically observed for this kind of event, with replayable evidence.
- partially_measured: partially observed / a named partial denominator only.
- not_measured: this layer could be relevant but is typically NOT publicly observed (an observability GAP).
- not_applicable: this trigger's instrument does not act on this layer at all.

Most triggers touch only 1-2 layers; the rest are not_applicable."""

GROUND_HEADER = """

CORPUS PRIORS (from training events before 2025 — use these base rates to calibrate, especially which layers are usually not_applicable or not_measured):
"""

CLOSE = """

TRIGGER DESCRIPTOR:
- research stratum: %(stratum)s
- trigger type: %(trigger_type)s
- touches US jurisdiction: %(us)s
- target kind: %(target_kind)s
- year: %(year)s

Reply with ONLY a JSON object mapping each layer to one coverage state, nothing else:
{"l0_network":"...","l1_consensus":"...","l3_rpc":"...","l4_frontend":"...","asset_onchain":"...","offramp_cex":"..."}"""


def build_priors(train):
    """Per-stratum per-layer coverage-state distribution from the train split."""
    lines = []
    for s in STRATA:
        ev = [r for r in train if r["feat"]["stratum"] == s]
        if not ev:
            continue
        parts = []
        for L in LAYERS:
            c = collections.Counter(r["labels"][L] for r in ev)
            top = c.most_common(2)
            frac = "/".join(f"{k.split('_')[0] if k!=NA else 'na'}:{v}" for k, v in top)
            parts.append(f"{L.split('_')[0]}={frac}")
        lines.append(f"  {s} (n={len(ev)}): " + "; ".join(parts))
    return "\n".join(lines)


def make_prompt(feat, priors):
    p = BASE
    if priors:
        p += GROUND_HEADER + priors
    return p + (CLOSE % feat)


def llm_predict(args):
    feat, prompt = args
    try:
        out = subprocess.run(["claude", "-p", prompt, "--model", MODEL,
                              "--output-format", "json"],
                             capture_output=True, text=True, timeout=180)
        res = json.loads(out.stdout)["result"]
        obj = json.loads(res[res.index("{"):res.rindex("}") + 1])
        return {L: (obj.get(L) if obj.get(L) in COVER else NA) for L in LAYERS}
    except Exception as e:
        sys.stderr.write(f"  parse fail ({e})\n")
        return {L: NA for L in LAYERS}


rows = load()
train = [r for r in rows if r["year"] < CUTOFF]
test = [r for r in rows if r["year"] >= CUTOFF]
priors = build_priors(train) if MODE == "grounded" else ""
print(f"corpus={len(rows)} train={len(train)} test={len(test)} model={MODEL} mode={MODE} workers={WORKERS}")
if priors:
    print("--- injected corpus priors ---\n" + priors)

tasks = [(r["feat"], make_prompt(r["feat"], priors)) for r in test]
print(f"running {len(tasks)} parallel CLI calls...", flush=True)
with ThreadPoolExecutor(max_workers=WORKERS) as ex:
    llm_preds = list(ex.map(llm_predict, tasks))

gold = {L: [r["labels"][L] for r in test] for L in LAYERS}
pred = {L: [p[L] for p in llm_preds] for L in LAYERS}
json.dump({"gold": gold, "pred": pred, "model": MODEL, "mode": MODE, "n": len(test)},
          open(f"/tmp/llmpred_{MODEL}_{MODE}_{CUTOFF}.json", "w"))

f1 = np.mean([macro_f1(gold[L], pred[L]) for L in LAYERS])
sc = np.mean([scope_f1(gold[L], pred[L]) for L in LAYERS])
cq = np.nanmean([cond_quality(gold[L], pred[L]) for L in LAYERS])
print(f"\nRESULT  LLM {MODEL}/{MODE} cutoff>={CUTOFF}  4cls-F1={f1:.3f}  scope-F1={sc:.3f}  cond-qual={cq:.3f}  (n={len(test)})")
print(f"saved /tmp/llmpred_{MODEL}_{MODE}_{CUTOFF}.json")
