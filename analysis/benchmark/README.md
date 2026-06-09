# Coverage-prediction benchmark — frozen LLM reference outputs

Frozen per-event LLM coverage predictions for Table VII (§VIII) of the paper,
produced by `scripts/llm_baseline_coverage.py` via the local `claude` CLI
(subscription auth; non-deterministic). Filenames: `llmpred_<model>_<mode>_<cutoff>.json`
(model ∈ {haiku, sonnet}; mode ∈ {zeroshot, grounded}; cutoff = train/test year split).
Compile the comparison with `scripts/compile_llm_comparison.py <cutoff>`.
These are REFERENCE baselines and are void pending the independent-human IRR pass.
