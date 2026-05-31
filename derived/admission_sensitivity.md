# Admission-protocol sensitivity ablation

Generated: `2026-06-01T00:00:00Z` · generator `scripts/build_admission_sensitivity.py` · corpus n = 368 events.

Three admission rubrics applied to the coverage-matched `changed_given_coverage` rate per layer:

- **strict** — numerator and denominator over `measured` only; attribution `direct` only.
- **current** — numerator and denominator over `measured` only; attribution `direct` or `plausible`.
- **permissive** — numerator and denominator over `measured` or `partially_measured`; attribution `direct` or `plausible`.

The `strict_permissive_delta` column is the absolute change in rate from strict to permissive. Sensitivity tier: **robust** (< 0.05), **moderate** (0.05–0.10), **sensitive** (≥ 0.10). A sensitive rate must be reported under all three rubrics in the paper; a robust rate may be reported under the `current` rubric only.

## Table

| layer | strict (num/den = rate) | current | permissive | Δ | sensitivity |
| --- | --- | --- | --- | --- | --- |
| `l0_network` | — / 0 = — | — / 0 = — | 2/2 = 1.000 | — | **undefined** |
| `l1_consensus` | 0/8 = 0.000 | 2/8 = 0.250 | 10/16 = 0.625 | 0.625 | **sensitive** |
| `l3_rpc` | 2/2 = 1.000 | 2/2 = 1.000 | 6/7 = 0.857 | -0.1429 | **sensitive** |
| `l4_frontend` | 33/56 = 0.589 | 51/56 = 0.911 | 79/88 = 0.898 | 0.3084 | **sensitive** |
| `asset_onchain` | 18/18 = retracted | 18/18 = retracted | 19/20 = retracted | — | **retracted_structural** |
| `offramp_cex` | 93/233 = 0.399 | 155/233 = 0.665 | 199/287 = 0.693 | 0.2943 | **sensitive** |

## Interpretation

- A **robust** layer means the rate does not depend on the partially_measured admission decision; a reader cannot accuse the authors of inflating the ratio by relaxing coverage.
- A **sensitive** layer means the rate moves substantially (≥ 10 percentage points) between strict and permissive. The paper must report both rates and disclose the admission choice in the claim's phrasing.
- A layer with `—` denominator under *strict* means no events have `measured` coverage at that layer (the `l0_network` and `l3_rpc` cases at v0.1). For those layers the paper should phrase the rate as an observability gap, not a conditional rate.
- For `l3_rpc`, the permissive counts are retained only as two named Flashbots git-history observations; the rate is suppressed because the layer has no measured denominator.
- For `asset_onchain`, counts are retained but rates are retracted because measured admission requires an asset-layer change anchor.

This ablation is the reviewer-facing answer to "can you inflate changed_given_measured by labeling events `partially_measured` loosely?". If every paper-cited rate is in the `robust` tier, the answer is defensibly no.
