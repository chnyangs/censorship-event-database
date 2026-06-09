"""
compile_llm_comparison.py — final 4-group comparison for the coverage-prediction
task on the recent holdout (year >= 2025), with event-level bootstrap 95% CIs.

Groups: simple baselines (B0 majority / B1 stratum) + 3 LLM configs loaded from
/tmp/llmpred_<model>_<mode>.json (haiku zeroshot / sonnet zeroshot / sonnet grounded).
"""
import glob, json, collections, sys
import numpy as np
import yaml

CUTOFF = int(sys.argv[1]) if len(sys.argv) > 1 else 2025

LAYERS = ["l0_network", "l1_consensus", "l3_rpc", "l4_frontend", "asset_onchain", "offramp_cex"]
COVER = ["measured", "partially_measured", "not_measured", "not_applicable"]
NA = "not_applicable"
rng = np.random.default_rng(20260609)


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
        cov = {c["layer"]: c.get("status") for c in (d.get("coverage") or []) if isinstance(c, dict)}
        rows.append({"feat": {"stratum": d.get("research_stratum") or "?"},
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
    return macro_f1(["na" if x == NA else "app" for x in g], ["na" if x == NA else "app" for x in p])


def cond_quality(g, p):
    idx = [i for i, x in enumerate(g) if x != NA]
    return macro_f1([g[i] for i in idx], [p[i] for i in idx]) if idx else float("nan")


def metrics(gold, pred, ev_idx):
    """gold/pred: {layer:[per-event...]}. ev_idx: event indices to include."""
    f1, sc, cq = [], [], []
    for L in LAYERS:
        g = [gold[L][i] for i in ev_idx]
        p = [pred[L][i] for i in ev_idx]
        f1.append(macro_f1(g, p)); sc.append(scope_f1(g, p)); cq.append(cond_quality(g, p))
    return np.mean(f1), np.mean(sc), np.nanmean(cq)


rows = load()
train = [r for r in rows if r["year"] < CUTOFF]
test = [r for r in rows if r["year"] >= CUTOFF]
n = len(test)

# B0 / B1 predictions on test (fit on train)
maj = {L: collections.Counter(r["labels"][L] for r in train).most_common(1)[0][0] for L in LAYERS}
strat_tab = {L: collections.defaultdict(collections.Counter) for L in LAYERS}
for L in LAYERS:
    for r in train:
        strat_tab[L][r["feat"]["stratum"]][r["labels"][L]] += 1
def b1(s, L):
    c = strat_tab[L].get(s); return c.most_common(1)[0][0] if c else maj[L]

gold = {L: [r["labels"][L] for r in test] for L in LAYERS}
methods = {
    "B0 majority":      {L: [maj[L]] * n for L in LAYERS},
    "B1 stratum":       {L: [b1(r["feat"]["stratum"], L) for r in test] for L in LAYERS},
}
for tag, fn in [("LLM haiku (zero-shot)", "haiku_zeroshot"),
                ("LLM sonnet (zero-shot)", "sonnet_zeroshot"),
                ("LLM sonnet (grounded)", "sonnet_grounded")]:
    try:
        methods[tag] = json.load(open(f"/tmp/llmpred_{fn}_{CUTOFF}.json"))["pred"]
    except FileNotFoundError:
        pass

print(f"Coverage-prediction · recent holdout (trigger year >= {CUTOFF}, n={n}); train(<{CUTOFF})={len(train)}")
print(f"event-level bootstrap 95% CI (1000 resamples)\n")
print(f"{'method':24s}{'4cls-F1 [95% CI]':>22s}{'scope-F1 [95% CI]':>22s}{'cond-qual [95% CI]':>22s}")
allidx = list(range(n))
for name, pred in methods.items():
    pt = metrics(gold, pred, allidx)
    boots = np.array([metrics(gold, pred, list(rng.choice(allidx, n, replace=True))) for _ in range(1000)])
    lo, hi = np.nanpercentile(boots, 2.5, axis=0), np.nanpercentile(boots, 97.5, axis=0)
    cells = "".join(f"{f'{pt[k]:.3f} [{lo[k]:.2f},{hi[k]:.2f}]':>22s}" for k in range(3))
    print(f"{name:24s}{cells}")

print("\nCAVEATS: LLM rows are REFERENCE baselines — (1) gold is LLM-coded so they carry")
print("shared-process bias; (2) n=42 is small (wide CIs); (3) LLM-prior, not a trained")
print("temporal learner. CHEAT-baseline honesty check (separate run): 4cls-F1 ~0.05 << B0.")
