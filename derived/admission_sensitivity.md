# Admission-protocol sensitivity ablation

Generated: `2026-06-25T23:48:26Z` · generator `scripts/build_admission_sensitivity.py` · corpus n = 398 events.

Three admission rubrics applied to the coverage-matched `changed_given_coverage` rate per layer:

- **strict** — numerator and denominator over `measured` only; attribution `direct` only.
- **current** — numerator and denominator over `measured` only; attribution `direct` or `plausible`.
- **permissive** — numerator and denominator over `measured` or `partially_measured`; attribution `direct` or `plausible`.

The `strict_permissive_delta` column is the absolute change in rate from strict to permissive. Sensitivity tier: **robust** (< 0.05), **moderate** (0.05–0.10), **sensitive** (≥ 0.10). A sensitive rate must be reported under all three rubrics in the paper; a robust rate may be reported under the `current` rubric only.

## Table

| layer | strict (num/den = rate) | current | permissive | Δ | sensitivity |
| --- | --- | --- | --- | --- | --- |
| `l0_network` | — / 0 = — | — / 0 = — | 5/5 = 1.000 | — | **undefined** |
| `l1_consensus` | 0/8 = 0.000 | 2/8 = 0.250 | 10/16 = 0.625 | 0.625 | **sensitive** |
| `l3_rpc` | 1/1 = 1.000 | 1/1 = 1.000 | 6/7 = 0.857 | -0.1429 | **sensitive** |
| `l4_frontend` | 34/57 = 0.597 | 52/57 = 0.912 | 70/78 = 0.897 | 0.3009 | **sensitive** |
| `asset_onchain` | 20/23 = retracted | 23/23 = retracted | 26/27 = retracted | — | **retracted_structural** |
| `offramp_cex` | 120/257 = 0.467 | 167/257 = 0.650 | 208/308 = 0.675 | 0.2084 | **sensitive** |

## Interpretation

- A **robust** layer means the rate does not depend on the partially_measured admission decision; a reader cannot accuse the authors of inflating the ratio by relaxing coverage.
- A **sensitive** layer means the rate moves substantially (≥ 10 percentage points) between strict and permissive. The paper must report both rates and disclose the admission choice in the claim's phrasing.
- For `asset_onchain`, counts are retained but rates are retracted because measured admission requires an asset-layer change anchor.
- A layer with `—` denominator under *strict/current* has no `measured` coverage under those rubrics (`l0_network` in this snapshot). Phrase those cells as observability gaps; permissive partial-coverage counts are sensitivity-only unless a paper table explicitly emits a matched denominator.

This ablation is the reviewer-facing answer to "can you inflate changed_given_measured by labeling events `partially_measured` loosely?". If every paper-cited rate is in the `robust` tier, the answer is defensibly no.
