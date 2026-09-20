"""
Exploratory coverage-label prediction diagnostics for the curated corpus.

TASK (denominator-honest, two-stage):
  Input  : a trigger descriptor  (stratum, trigger_type, US-touch, target_kind, year)
  Output : a 6-element COVERAGE-STATE vector, one per layer, each in
           {measured, partially_measured, not_measured, not_applicable};
           then, ONLY on layers predicted measured/partial, a binary REACTION
           prediction (observed_change vs observed_no_change).

Scores describe predictions of curated corpus labels, not independently
measured enforcement or the missingness mechanism. Reaction scores use the
same gold measured/partial cells: oracle-coverage scores ignore the predicted
coverage, whereas end-to-end scores count a predicted coverage gap as an
abstention/error. Coverage errors are additionally scored over every layer.

EVALUATION: rolling-origin chronological CV. For each test year T,
train ONLY on events with trigger year < T; predict events in year T; pool the
(gold, pred) pairs across test years from 2017 and report per-layer macro-F1
with bootstrap 95% CIs. Chronological rows do not prove that retrospectively
curated descriptors are free from hindsight or other feature leakage.

Baselines (honest, immediately reproducible):
  B0 majority         : per-layer global modal coverage state (training split)
  B1 stratum_mode     : per-layer modal coverage state | stratum
  B2 stratum+trigger  : per-layer modal coverage state | (stratum, trigger_type)
  Always measured     : diagnostic that predicts measured coverage everywhere.

Run:  python scripts/benchmark_coverage_prediction.py
"""

import glob
import collections
from pathlib import Path

import numpy as np
import yaml

REPO = Path(__file__).resolve().parent.parent
EVENTS = REPO / "events"
LAYERS = ["l0_network", "l1_consensus", "l3_rpc", "l4_frontend",
          "asset_onchain", "offramp_cex"]
COVER = ["measured", "partially_measured", "not_measured", "not_applicable"]
REACTION = ["observed_change", "observed_no_change"]
OBSERVED = {"measured", "partially_measured"}
ABSTAIN = "__abstain__"
METRIC_VERSION = "fixed_classes_v2"
SEED = 20260609


# --------------------------------------------------------------------------
# 1. Build the labelled dataset from admitted events
# --------------------------------------------------------------------------
def load():
    rows = []
    for f in sorted(glob.glob(str(EVENTS / "*.yaml"))):
        d = yaml.safe_load(open(f))
        if not isinstance(d, dict) or d.get("status") != "admitted":
            continue
        trig = d.get("trigger") or {}
        ts = str(trig.get("timestamp") or "")
        year = int(ts[:4]) if ts[:4].isdigit() else None
        if year is None:
            continue
        jur = d.get("jurisdiction") or []
        jur = [jur] if isinstance(jur, str) else jur
        cov = {c["layer"]: c.get("status") for c in (d.get("coverage") or [])
               if isinstance(c, dict)}
        react = collections.defaultdict(set)
        for o in (d.get("observations") or []):
            if isinstance(o, dict):
                react[o.get("layer")].add(o.get("observation_kind"))
        feat = {
            "stratum": d.get("research_stratum") or "?",
            "trigger_type": (trig.get("type") or "?"),
            "us": "US" in jur,
            "target_kind": (d.get("target") or {}).get("kind") or "?",
            "year": year,
        }
        labels = {}
        for L in LAYERS:
            cs = cov.get(L)
            if cs not in COVER:
                raise ValueError(f"{f}: missing or invalid coverage state for {L}: {cs!r}")
            r = react.get(L, set())
            reaction = ("observed_change" if "observed_change" in r
                        else ("observed_no_change" if "observed_no_change" in r
                              else None))
            labels[L] = (cs, reaction)
        rows.append({"event_id": d.get("id") or Path(f).stem,
                     "feat": feat, "labels": labels, "year": year})
    return rows


# --------------------------------------------------------------------------
# 2. Baselines: each returns a per-layer predictor coverage(feat) -> state
# --------------------------------------------------------------------------
def _mode(counter):
    return counter.most_common(1)[0][0] if counter else "not_applicable"


def fit_majority(train):
    pred = {}
    for L in LAYERS:
        c = collections.Counter(r["labels"][L][0] for r in train)
        pred[L] = _mode(c)
    return lambda feat, L: pred[L]


def fit_conditional(train, keyfn):
    table = {L: collections.defaultdict(collections.Counter) for L in LAYERS}
    glob_ = {}
    for L in LAYERS:
        gc = collections.Counter(r["labels"][L][0] for r in train)
        glob_[L] = _mode(gc)
        for r in train:
            table[L][keyfn(r["feat"])][r["labels"][L][0]] += 1
    def predict(feat, L):
        c = table[L].get(keyfn(feat))
        return _mode(c) if c else glob_[L]
    return predict


def fit_reaction(train, keyfn):
    """Conditional modal reaction | (key, layer), among measured/partial gold."""
    table = {L: collections.defaultdict(collections.Counter) for L in LAYERS}
    glob_ = {}
    for L in LAYERS:
        gc = collections.Counter()
        for r in train:
            cs, rk = r["labels"][L]
            if cs in ("measured", "partially_measured") and rk:
                gc[rk] += 1
                table[L][keyfn(r["feat"])][rk] += 1
        glob_[L] = _mode(gc) if gc else "observed_change"
    def predict(feat, L):
        c = table[L].get(keyfn(feat))
        return _mode(c) if c else glob_[L]
    return predict


# --------------------------------------------------------------------------
# 3. Metrics
# --------------------------------------------------------------------------
def macro_f1(gold, pred, classes=COVER):
    """Fixed-class macro F1; an absent class contributes zero (zero_division=0).

    A prediction outside ``classes`` (e.g. abstention) is an error for its gold
    class, never an extra class that changes the averaging denominator.
    """
    if len(gold) != len(pred):
        raise ValueError("gold/prediction lengths differ")
    if len(gold) == 0:
        return float("nan")
    if not classes or len(set(classes)) != len(classes):
        raise ValueError("classes must be a nonempty fixed set")
    if any(g not in classes for g in gold):
        raise ValueError("gold label outside the fixed class set")
    f1s = []
    for c in classes:
        tp = sum(g == c and p == c for g, p in zip(gold, pred))
        fp = sum(g != c and p == c for g, p in zip(gold, pred))
        fn = sum(g == c and p != c for g, p in zip(gold, pred))
        prec = tp / (tp + fp) if tp + fp else 0.0
        rec = tp / (tp + fn) if tp + fn else 0.0
        f1s.append(2 * prec * rec / (prec + rec) if prec + rec else 0.0)
    return float(np.mean(f1s)) if f1s else 0.0


# Two additional metrics separate the recorded scope from coverage quality:
#   SCOPE-F1  : binary "is this layer in scope for the trigger" (applicable vs
#               not_applicable).
#   COND-QUAL : among gold-applicable layers only, 3-class macro-F1 over the
#               coverage quality {measured, partially_measured, not_measured} --
#               coverage quality. NA is excluded from gold
#               but a model that predicts NA on an applicable layer is still wrong.
def scope_f1(gold, pred):
    gs = ["na" if g == "not_applicable" else "app" for g in gold]
    ps = [("na" if p == "not_applicable" else "app") if p in COVER else "__invalid__"
          for p in pred]
    return macro_f1(gs, ps, classes=("na", "app"))


def cond_quality(gold, pred):
    idx = [i for i, g in enumerate(gold) if g != "not_applicable"]
    if not idx:
        return float("nan")
    return macro_f1([gold[i] for i in idx], [pred[i] for i in idx],
                    classes=COVER[:3])


def boot_ci(gold, pred, n=1000, seed=SEED):
    gold, pred = np.array(gold), np.array(pred)
    if len(gold) < 3:
        return (float("nan"), float("nan"))
    vals = []
    rng = np.random.default_rng(seed)
    idx = np.arange(len(gold))
    for _ in range(n):
        s = rng.choice(idx, len(idx), replace=True)
        vals.append(macro_f1(list(gold[s]), list(pred[s])))
    return (float(np.percentile(vals, 2.5)), float(np.percentile(vals, 97.5)))


# --------------------------------------------------------------------------
# 4. Rolling-origin temporal evaluation
# --------------------------------------------------------------------------
def rolling_eval(rows, fit_fn, react_fn=None):
    """Return pooled per-layer (gold,pred) over test years; no future leak."""
    years = sorted({r["year"] for r in rows})
    pool = {L: ([], []) for L in LAYERS}       # coverage gold/pred
    rpool = {L: {"gold": [], "oracle": [], "end_to_end": []} for L in LAYERS}
    for T in years:
        if T < 2017:
            continue
        train = [r for r in rows if r["year"] < T]
        test = [r for r in rows if r["year"] == T]
        if not train or not test:
            continue
        cov_pred = fit_fn(train)
        rcv_pred = react_fn(train) if react_fn else None
        for r in test:
            for L in LAYERS:
                g_cs, g_rk = r["labels"][L]
                pool[L][0].append(g_cs)
                p_cs = cov_pred(r["feat"], L)
                pool[L][1].append(p_cs)
                if g_cs in OBSERVED and g_rk and rcv_pred:
                    p_rk = rcv_pred(r["feat"], L)
                    rpool[L]["gold"].append(g_rk)
                    rpool[L]["oracle"].append(p_rk)
                    rpool[L]["end_to_end"].append(p_rk if p_cs in OBSERVED else ABSTAIN)
    return pool, rpool


def report(name, pool, rpool=None):
    print(f"\n### {name} — rolling-origin temporal CV (test years 2017+, pooled)")
    print(f"{'layer':16s}{'4cls-F1':>9s}{'scope-F1':>10s}{'cond-qual':>11s}{'n_test':>8s}  coverage F1 95% CI")
    f1_all, sc_all, cq_all = [], [], []
    for L in LAYERS:
        g, p = pool[L]
        f1 = macro_f1(g, p)
        sc = scope_f1(g, p)
        cq = cond_quality(g, p)
        f1_all.append(f1)
        sc_all.append(sc)
        if not np.isnan(cq):
            cq_all.append(cq)
        cq_str = f"{cq:.3f}" if not np.isnan(cq) else "  n/a"
        lo, hi = boot_ci(g, p)
        print(f"{L:16s}{f1:>9.3f}{sc:>10.3f}{cq_str:>11s}{len(g):>8d}  [{lo:.3f}, {hi:.3f}]")
        print("  gold support:", {c: g.count(c) for c in COVER})
    print(f"{'MEAN':16s}{np.mean(f1_all):>9.3f}{np.mean(sc_all):>10.3f}{np.mean(cq_all):>11.3f}")
    if rpool:
        print("  Reaction on identical gold measured/partial cells: oracle vs coverage-gated end-to-end")
        for L in LAYERS:
            g = rpool[L]["gold"]
            if g:
                for mode in ("oracle", "end_to_end"):
                    p = rpool[L][mode]
                    acc = np.mean([a == b for a, b in zip(g, p)])
                    f1 = macro_f1(g, p, classes=REACTION)
                    print(f"    {L:16s} {mode:12s} acc={acc:.3f} F1={f1:.3f} "
                          f"n={len(g)} abstentions={p.count(ABSTAIN)}")
    return {"f1": float(np.mean(f1_all)),
            "scope": float(np.mean(sc_all)),
            "cond": float(np.mean(cq_all))}


def main():
    rows = load()
    print(f"Admitted events with a trigger year: {len(rows)}")
    print(f"Metric version: {METRIC_VERSION}; absent fixed classes contribute zero.")
    print("Scores use curated corpus labels, not independent enforcement ground truth.")
    print("Coverage CI resamples events within each layer; events are distinct rows.")
    yc = collections.Counter(r["year"] for r in rows)
    print("Test events per year:", {y: yc[y] for y in sorted(yc) if y >= 2017})
    baselines = [
        ("B0 majority", fit_majority, lambda tr: fit_reaction(tr, lambda f: None)),
        ("B1 stratum", lambda tr: fit_conditional(tr, lambda f: f["stratum"]),
         lambda tr: fit_reaction(tr, lambda f: f["stratum"])),
        ("B2 stratum+trigger",
         lambda tr: fit_conditional(tr, lambda f: (f["stratum"], f["trigger_type"])),
         lambda tr: fit_reaction(tr, lambda f: (f["stratum"], f["trigger_type"]))),
        ("Always measured", lambda tr: lambda feat, layer: "measured", None),
    ]
    for name, fit_fn, react_fn in baselines:
        report(name, *rolling_eval(rows, fit_fn, react_fn))
    print("Reaction metrics are undefined on unmeasured cells; no labels are imputed there.")
    print("This benchmark predicts corpus coding/coverage choices; it does not validate those choices.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
