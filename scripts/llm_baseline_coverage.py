"""Optional LLM reference runner; importing this module never calls an LLM.

Usage: python scripts/llm_baseline_coverage.py MODEL MODE [CUTOFF] [WORKERS]
The codebook_v2 prompt is neutral: only grounded mode receives training priors.
Existing frozen outputs used an earlier prompt and have NOT been regenerated.
A chronological corpus split does not establish an LLM's knowledge cutoff or
exclude pretraining contamination. Gold labels remain curator/LLM-assisted.
"""
import argparse
import collections
import hashlib
import json
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import numpy as np

from benchmark_coverage_prediction import (
    COVER, LAYERS, METRIC_VERSION, cond_quality, load as load_events,
    macro_f1, scope_f1,
)

NA = "not_applicable"
INVALID = "__invalid__"
PROMPT_VERSION = "codebook_v2"


def load():
    rows = load_events()
    return [{**r, "labels": {layer: value[0] for layer, value in r["labels"].items()}}
            for r in rows]


BASE = """Predict the recorded coverage state for each stack layer from the trigger descriptor. Coverage describes the availability of public evidence in a study; it does not itself establish whether an enforcement reaction occurred.

Six stack layers:
- l0_network: ISP, IP, DNS, or other network reachability restrictions.
- l1_consensus: transaction inclusion by block builders, relays, or validators.
- l3_rpc: access restrictions at RPC providers or endpoints.
- l4_frontend: web or app access restrictions, takedowns, app-store removals, or domain seizures.
- asset_onchain: token-issuer freezes or blacklists recorded on-chain.
- offramp_cex: centralized-exchange access, delistings, jurisdiction exits, or account restrictions.

Coverage states:
- measured: a replayable measurement artifact exists for this event's layer and scope.
- partially_measured: a replayable measurement artifact exists but does not exhaust the scope.
- not_measured: no replayable measurement artifact has been captured for the in-scope layer.
- not_applicable: the layer does not meaningfully apply to this event.

Use these definitions without assuming a layer's typical coverage or how many layers are applicable."""

CLOSE = """

TRIGGER DESCRIPTOR:
- research stratum: %(stratum)s
- trigger type: %(trigger_type)s
- touches US jurisdiction: %(us)s
- target kind: %(target_kind)s
- year: %(year)s

Reply with ONLY a JSON object mapping each of the six layer names to one coverage state."""


def build_priors(train):
    """Complete per-stratum counts, computed only from the supplied train set."""
    lines = []
    for stratum in sorted({r["feat"]["stratum"] for r in train}):
        events = [r for r in train if r["feat"]["stratum"] == stratum]
        counts = {layer: dict(collections.Counter(r["labels"][layer] for r in events))
                  for layer in LAYERS}
        lines.append(f"{stratum} (n={len(events)}): {json.dumps(counts, sort_keys=True)}")
    return "\n".join(lines)


def make_prompt(feat, priors="", cutoff=None):
    prompt = BASE
    if priors:
        window = f" (trigger year < {cutoff})" if cutoff is not None else ""
        prompt += f"\n\nTRAINING-SPLIT COVERAGE COUNTS{window}:\n" + priors
    return prompt + (CLOSE % feat)


def llm_predict(task):
    model, prompt = task
    try:
        out = subprocess.run(["claude", "-p", prompt, "--model", model,
                              "--output-format", "json"], check=True,
                             capture_output=True, text=True, timeout=180)
        result = json.loads(out.stdout)["result"]
        obj = json.loads(result[result.index("{"):result.rindex("}") + 1])
        if not isinstance(obj, dict):
            raise ValueError("expected a JSON object")
        return {layer: obj[layer] if obj.get(layer) in COVER else INVALID
                for layer in LAYERS}
    except (subprocess.SubprocessError, ValueError, KeyError, TypeError, OSError) as exc:
        sys.stderr.write(f"prediction failed ({type(exc).__name__}); scored as invalid, not NA\n")
        return {layer: INVALID for layer in LAYERS}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("model")
    parser.add_argument("mode", choices=("zeroshot", "grounded"))
    parser.add_argument("cutoff", type=int, nargs="?", default=2025)
    parser.add_argument("workers", type=int, nargs="?", default=8)
    args = parser.parse_args(argv)
    rows = load()
    train = [r for r in rows if r["year"] < args.cutoff]
    test = [r for r in rows if r["year"] >= args.cutoff]
    if not train or not test or args.workers < 1:
        parser.error("nonempty train/test splits and positive workers are required")
    priors = build_priors(train) if args.mode == "grounded" else ""
    prompts = [make_prompt(r["feat"], priors, args.cutoff) for r in test]
    print(f"train={len(train)} test={len(test)} prompt={PROMPT_VERSION}", flush=True)
    with ThreadPoolExecutor(max_workers=args.workers) as executor:
        predictions = list(executor.map(llm_predict, [(args.model, p) for p in prompts]))
    gold = {layer: [r["labels"][layer] for r in test] for layer in LAYERS}
    pred = {layer: [r[layer] for r in predictions] for layer in LAYERS}
    artifact = {
        "gold": gold, "pred": pred, "model": args.model, "mode": args.mode,
        "n": len(test), "cutoff": args.cutoff, "event_ids": [r["event_id"] for r in test],
        "train_event_ids": [r["event_id"] for r in train],
        "prompt_version": PROMPT_VERSION, "metric_version": METRIC_VERSION,
        "prompt_sha256": [hashlib.sha256(p.encode()).hexdigest() for p in prompts],
        "caveat": "curated labels; independent validation and pretraining contamination unverified",
    }
    path = Path(f"/tmp/llmpred_{args.model}_{args.mode}_{args.cutoff}_{PROMPT_VERSION}.json")
    path.write_text(json.dumps(artifact, indent=2, allow_nan=False) + "\n")
    scores = [np.mean([metric(gold[layer], pred[layer]) for layer in LAYERS])
              for metric in (macro_f1, scope_f1)]
    print(f"Fixed-class coverage F1={scores[0]:.3f}; scope F1={scores[1]:.3f}; saved {path}")
    print("Reference only: chronological splitting does not prove absence of LLM contamination.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
