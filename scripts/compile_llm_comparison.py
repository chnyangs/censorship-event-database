"""Score coverage predictors with fixed classes and event-level bootstrap CIs.

Defaults to current-corpus statistical baselines. New LLM artifacts are included
only via --predictions and must align by event ID and gold labels. The optional
--include-legacy view re-scores frozen arrays against THEIR OWN saved labels;
it cannot establish event identity, current-corpus comparability, or a rerun.
"""
import argparse
import json
from pathlib import Path

import numpy as np

from benchmark_coverage_prediction import (
    COVER, LAYERS, METRIC_VERSION, REPO, SEED, cond_quality, fit_conditional,
    fit_majority, macro_f1, scope_f1,
)
from llm_baseline_coverage import INVALID, load


def metrics(gold, pred, ev_idx):
    """Average per-layer scores, resampling each event jointly across layers."""
    values = [[], [], []]
    for layer in LAYERS:
        g = [gold[layer][i] for i in ev_idx]
        p = [pred[layer][i] for i in ev_idx]
        for scores, metric in zip(values, (macro_f1, scope_f1, cond_quality)):
            scores.append(metric(g, p))
    return tuple(float(np.mean([v for v in scores if np.isfinite(v)]))
                 if any(np.isfinite(v) for v in scores) else float("nan")
                 for scores in values)


def validate_snapshot(data):
    n = data.get("n")
    if not isinstance(n, int) or n < 1:
        raise ValueError("artifact must declare a positive n")
    for key in ("gold", "pred"):
        if not isinstance(data.get(key), dict) or set(data[key]) != set(LAYERS):
            raise ValueError(f"{key}: expected all six layers")
        for layer in LAYERS:
            values = data[key][layer]
            if not isinstance(values, list) or len(values) != n:
                raise ValueError(f"{key}/{layer}: wrong length")
            allowed = COVER if key == "gold" else [*COVER, INVALID]
            if any(value not in allowed for value in values):
                raise ValueError(f"{key}/{layer}: invalid labels")
    return n


def align_current_predictions(data, test):
    """Reject positional/legacy joins; even ID-aligned gold must be unchanged."""
    n = validate_snapshot(data)
    ids = data.get("event_ids")
    target_ids = [r["event_id"] for r in test]
    if (not isinstance(ids, list) or len(ids) != n or len(set(ids)) != n
            or len(set(target_ids)) != len(target_ids) or set(ids) != set(target_ids)):
        raise ValueError("event IDs missing, duplicated, or different from current holdout")
    if not data.get("prompt_version"):
        raise ValueError("prompt provenance missing; use the separate legacy view")
    index = {event_id: i for i, event_id in enumerate(ids)}
    for r in test:
        for layer in LAYERS:
            if data["gold"][layer][index[r["event_id"]]] != r["labels"][layer]:
                raise ValueError("saved gold labels differ from current corpus")
    return {layer: [data["pred"][layer][index[r["event_id"]]] for r in test]
            for layer in LAYERS}


def summarize(name, gold, pred, n_boot=1000):
    n = len(gold[LAYERS[0]])
    if not n:
        raise ValueError("empty evaluation set")
    indices = list(range(n))
    point = metrics(gold, pred, indices)
    rng = np.random.default_rng(SEED)
    boots = np.array([metrics(gold, pred, rng.choice(indices, n, replace=True))
                      for _ in range(n_boot)])
    cells = []
    for k in range(3):
        finite = boots[np.isfinite(boots[:, k]), k]
        if n < 2 or len(finite) < 2:
            cells.append(f"{point[k]:.3f} [CI unavailable]")
        else:
            lo, hi = np.percentile(finite, [2.5, 97.5])
            cells.append(f"{point[k]:.3f} [{lo:.3f}, {hi:.3f}] (B={len(finite)}/{n_boot})")
    print(f"{name}: n={n}; " + "; ".join(
        f"{label}={cell}" for label, cell in zip(("4class", "scope", "cond-quality"), cells)))


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("cutoff", type=int, nargs="?", default=2025)
    parser.add_argument("--predictions", action="append", type=Path, default=[])
    parser.add_argument("--include-legacy", action="store_true")
    parser.add_argument("--bootstrap", type=int, default=1000)
    args = parser.parse_args(argv)
    if args.bootstrap < 2:
        parser.error("--bootstrap must be at least 2")
    rows = load()
    train = [r for r in rows if r["year"] < args.cutoff]
    test = [r for r in rows if r["year"] >= args.cutoff]
    if not train or not test:
        parser.error("nonempty train and test splits are required")
    # Shared fitters use (coverage, reaction) pairs; reactions are unused here.
    fit_rows = [{**r, "labels": {layer: (value, None) for layer, value in r["labels"].items()}}
                for r in train]
    gold = {layer: [r["labels"][layer] for r in test] for layer in LAYERS}
    print(f"Current corpus: train<{args.cutoff} n={len(train)}; test>={args.cutoff} n={len(test)}")
    print(f"{METRIC_VERSION}; absent classes contribute 0; event bootstrap resamples all six layers together.")
    for name, fitter in (("B0 majority", fit_majority),
                         ("B1 stratum", lambda tr: fit_conditional(tr, lambda f: f["stratum"]))):
        predictor = fitter(fit_rows)
        pred = {layer: [predictor(r["feat"], layer) for r in test] for layer in LAYERS}
        summarize(name, gold, pred, args.bootstrap)
    for path in args.predictions:
        data = json.loads(path.read_text())
        if data.get("cutoff") != args.cutoff:
            parser.error(f"{path}: cutoff differs from requested split")
        try:
            pred = align_current_predictions(data, test)
        except ValueError as exc:
            parser.error(f"{path}: {exc}")
        summarize(f"LLM reference {path.name} prompt={data['prompt_version']}", gold, pred, args.bootstrap)
    if args.include_legacy:
        print("\nLEGACY FROZEN SNAPSHOTS — independent view, not comparable to current-corpus baselines.")
        print("Old prompts included corpus conclusions; no event IDs/prompt hashes; no LLM rerun occurred.")
        suffix = f"_{args.cutoff}" if args.cutoff != 2025 else ""
        for path in sorted((REPO / "analysis/benchmark").glob(f"llmpred_*{suffix}.json")):
            if args.cutoff == 2025 and path.stem.endswith("_2023"):
                continue
            data = json.loads(path.read_text())
            validate_snapshot(data)
            summarize(f"LEGACY {path.name}", data["gold"], data["pred"], args.bootstrap)
    else:
        print("Frozen legacy LLM outputs excluded; --include-legacy re-scores their saved labels separately.")
    print("All scores are corpus-label prediction diagnostics, not independent validity or censorship estimates.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
