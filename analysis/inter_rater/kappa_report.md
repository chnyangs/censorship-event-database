# Inter-rater reliability report

Generated: `2026-04-24T10:12:43Z` · computer `scripts/compute_irr_kappa.py` · blind/key inputs from `analysis/inter_rater/`.

## Coder provenance

- **Mode**: `llm_assisted_blinded` (one of `independent_human`, `llm_assisted_blinded`, `author_self_recode_60d_gap`, `unspecified` — published κ requires non-`unspecified` provenance).
- **Coder**: `claude-opus-4-7 (general-purpose subagent)`
- **Prompt / rubric version**: `2026-04-24-irr-prompt-v1`
- **Notes**: Blind: agent had no prior conversation context; instructed to ignore coverage[].status field and read schema + observation evidence; 90/90 coverage rows coded; observation_kind and attribution worksheets remain unfilled and are reported as parked.

| variable | n coded / n total | observed agreement | Cohen's κ | label |
| --- | --- | --- | --- | --- |
| `coverage_status` | 90 / 90 | 0.9889 | 0.9829 | almost perfect |
| `observation_kind` | 0 / 32 | — | — | — |
| `attribution` | 0 / 25 | — | — | — |

## `coverage_status` detail

- n_coded: **90** of 90 rows (remaining rows are missing `recode_value` — coder-incomplete)
- observed agreement p_o = 0.9889
- expected agreement p_e = 0.3516
- Cohen's κ = **0.9829** (almost perfect)

### Confusion matrix

| recode \ original | measured | not_applicable | not_measured | partially_measured |
| --- | --- | --- | --- | --- |
| **measured** | 20 | 0 | 0 | 0 |
| **not_applicable** | 0 | 46 | 0 | 0 |
| **not_measured** | 0 | 0 | 16 | 0 |
| **partially_measured** | 1 | 0 | 0 | 7 |

## `observation_kind` detail

- n_coded: **0** of 32 rows (remaining rows are missing `recode_value` — coder-incomplete)
- observed agreement p_o = None
- expected agreement p_e = None
- Cohen's κ = **None** (—)

### Confusion matrix

_(no confusion matrix; no coded cells)_

## `attribution` detail

- n_coded: **0** of 25 rows (remaining rows are missing `recode_value` — coder-incomplete)
- observed agreement p_o = None
- expected agreement p_e = None
- Cohen's κ = **None** (—)

### Confusion matrix

_(no confusion matrix; no coded cells)_

## Interpretation

Cohen's κ thresholds (Landis & Koch 1977 — still the most cited convention despite known limitations with skewed marginals): < 0.2 slight, 0.2–0.4 fair, 0.4–0.6 moderate, 0.6–0.8 substantial, > 0.8 almost perfect.

**Paper-readiness threshold** for this project: κ ≥ 0.6 on all three variables. A variable below 0.6 blocks the coverage-matched rate claim that depends on it (C1 for coverage_status, C2 for observation_kind, attribution-tier phrasing lock for attribution).

**Honest labeling**: the second coder in this artifact may be the same author as the gold coder (self-recode) or an LLM-assisted recoder. The report emits whichever is run. The protocol is encoded in `scripts/build_irr_sample.py` and `scripts/compute_irr_kappa.py`.
