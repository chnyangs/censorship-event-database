# Coverage-label prediction diagnostics

This exploratory appendix predicts the corpus's recorded coverage labels. It
is not an independent test of enforcement, censorship prevalence, measurement
quality, or whether the recorded scope is correct. The labels and features
reflect curatorial choices; human validation and leakage analysis remain open.

## Current evaluator (`fixed_classes_v2`)

All three scripts import the same scoring functions from
`scripts/benchmark_coverage_prediction.py`:

- Coverage macro-F1 always averages the four codebook coverage classes.
- Scope macro-F1 always averages applicable and not applicable.
- Conditional quality averages the three in-scope coverage classes, evaluated
  only on gold-applicable cells. Predicting not applicable is an error there.
- Absent classes contribute zero (`zero_division=0`). Thus perfect prediction
  on a layer with only one gold class is 0.25 for four-class macro-F1, not 1.
  Read scores alongside class support; do not compare them with the former
  union-of-observed-classes scores.
- Invalid LLM outputs count as invalid predictions, never implicit
  `not_applicable`. Missing/invalid gold coverage raises an error.

The rolling-origin baseline script separately reports reaction accuracy and
fixed two-class F1 on the same gold measured/partially-measured cells that carry
reaction labels. **Oracle coverage** ignores the predicted coverage label;
**end-to-end** treats a predicted unmeasured/not-applicable layer as an
abstention/error. Neither scores invented reaction labels on gold unmeasured
cells. Full coverage scores also penalize falsely predicting measurement there.

```sh
python scripts/benchmark_coverage_prediction.py
python scripts/compile_llm_comparison.py 2025
```

The first command uses rolling-origin folds with train years strictly earlier
than each test year (2017 onwards). Its per-layer coverage confidence intervals
resample events. The second uses a fixed cutoff, with event-level bootstrap
resampling jointly across all six layers. It reports statistical baselines by
default. Both run offline and perform no LLM calls. Their scores are diagnostics
of the selected corpus, not population estimates.

## Frozen legacy LLM artifacts

Every `llmpred_*.json` currently stored in this directory is **legacy**, generated
before `codebook_v2`. These files are preserved unchanged. Their earlier prompts
contained corpus-derived hints, including claims about the best/worst observed
layers and the typical number of applicable layers. Their stored arrays lack
event IDs and prompt hashes. An independent-human reliability pass would not
by itself fix prompt contamination or prove event alignment.

The evaluator therefore does not join legacy prediction positions to the live
corpus. To re-score each saved snapshot against its own saved gold labels:

```sh
python scripts/compile_llm_comparison.py 2025 --include-legacy
python scripts/compile_llm_comparison.py 2023 --include-legacy
```

These print a separate, explicitly legacy section. An evaluator rerun changes
scoring only: it does **not** rerun an LLM or retroactively neutralize the prompt.
They are not results of the new prompt and are not comparable to live-corpus
baselines unless a matching historical event/split manifest is recovered.

## Optional future LLM runs

`llm_baseline_coverage.py` now uses a neutral `codebook_v2` zero-shot prompt.
Grounded mode alone injects counts computed from the requested training split.
New files are written to `/tmp` with the prompt version in the filename and
include event IDs, training IDs, cutoff, prompt hashes, and metric version.
Chronological splitting does not establish a model's training cutoff or exclude
pretraining contamination. Model aliases and nondeterministic execution remain
limitations of any future run. **No new LLM runs were performed for this fix.**

The optional runner makes external CLI calls only when explicitly executed;
imports and `--help` are side-effect free. New outputs can be passed with
`compile_llm_comparison.py CUTOFF --predictions PATH`. The compiler requires
matching unique event IDs, matching gold labels, and declared prompt provenance.
