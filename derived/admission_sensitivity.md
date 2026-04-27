# Admission-protocol sensitivity ablation

Generated: `2026-04-25T09:22:35Z` · generator `scripts/build_admission_sensitivity.py` · corpus n = 53 events.

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
| `l3_rpc` | — / 0 = — | — / 0 = — | 2/9 = 0.222 | — | **undefined** |
| `l4_frontend` | 9/16 = 0.562 | 11/16 = 0.688 | 13/19 = 0.684 | 0.1217 | **sensitive** |
| `asset_onchain` | 17/17 = 1.000 | 17/17 = 1.000 | 17/17 = 1.000 | 0.0 | **robust** |
| `offramp_cex` | 15/25 = 0.600 | 15/25 = 0.600 | 16/26 = 0.615 | 0.0154 | **robust** |

## Interpretation

- A **robust** layer means the rate does not depend on the partially_measured admission decision; a reader cannot accuse the authors of inflating the ratio by relaxing coverage.
- A **sensitive** layer means the rate moves substantially (≥ 10 percentage points) between strict and permissive. The paper must report both rates and disclose the admission choice in the claim's phrasing.
- A layer with `—` denominator under *strict* means no events have `measured` coverage at that layer (the `l0_network` and `l3_rpc` cases at v0.1). For those layers the paper should phrase the rate as an observability gap, not a conditional rate.

This ablation is the reviewer-facing answer to "can you inflate changed_given_measured by labeling events `partially_measured` loosely?". If every paper-cited rate is in the `robust` tier, the answer is defensibly no.
