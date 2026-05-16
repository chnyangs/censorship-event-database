# Admission-protocol sensitivity ablation

Generated: `2026-05-18T10:40:00Z` · generator `scripts/build_admission_sensitivity.py` · corpus n = 83 events.

Three admission rubrics applied to the coverage-matched `changed_given_coverage` rate per layer:

- **strict** — numerator and denominator over `measured` only; attribution `direct` only.
- **current** — numerator and denominator over `measured` only; attribution `direct` or `plausible`.
- **permissive** — numerator and denominator over `measured` or `partially_measured`; attribution `direct` or `plausible`.

The `strict_permissive_delta` column is the absolute change in rate from strict to permissive. Sensitivity tier: **robust** (< 0.05), **moderate** (0.05–0.10), **sensitive** (≥ 0.10). A sensitive rate must be reported under all three rubrics in the paper; a robust rate may be reported under the `current` rubric only.

## Table

| layer | strict (num/den = rate) | current | permissive | Δ | sensitivity |
| --- | --- | --- | --- | --- | --- |
| `l0_network` | — / 0 = — | — / 0 = — | — / 0 = — | — | **undefined** |
| `l1_consensus` | 0/6 = 0.000 | 1/6 = 0.167 | 2/7 = 0.286 | 0.2857 | **sensitive** |
| `l3_rpc` | — / 0 = — | — / 0 = — | 2 named observations = no rate | — | **undefined** |
| `l4_frontend` | 18/24 = 0.750 | 21/24 = 0.875 | 30/34 = 0.882 | 0.1324 | **sensitive** |
| `asset_onchain` | 17/17 = retracted | 17/17 = retracted | 17/17 = retracted | — | **retracted_structural** |
| `offramp_cex` | 34/47 = 0.723 | 37/47 = 0.787 | 43/53 = 0.811 | 0.0879 | **moderate** |

## Interpretation

- A **robust** layer means the rate does not depend on the partially_measured admission decision; a reader cannot accuse the authors of inflating the ratio by relaxing coverage.
- A **sensitive** layer means the rate moves substantially (≥ 10 percentage points) between strict and permissive. The paper must report both rates and disclose the admission choice in the claim's phrasing.
- A layer with `—` denominator under *strict* means no events have `measured` coverage at that layer (the `l0_network` and `l3_rpc` cases at v0.1). For those layers the paper should phrase the rate as an observability gap, not a conditional rate.
- For `l3_rpc`, the permissive counts are retained only as two named Flashbots git-history observations; the rate is suppressed because the layer has no measured denominator.
- For `asset_onchain`, counts are retained but rates are retracted because measured admission requires an asset-layer change anchor.

This ablation is the reviewer-facing answer to "can you inflate changed_given_measured by labeling events `partially_measured` loosely?". If every paper-cited rate is in the `robust` tier, the answer is defensibly no.
