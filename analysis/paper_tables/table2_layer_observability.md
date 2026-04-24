# Table 2 · Layer observability (denominator-honest)

Dataset snapshot: **v0.1.0** · cutoff `2026-04-22` · commit `573838c` · generated `2024-04-24T23:06:40Z`

Supports **C1** (`docs/paper_claims.md §1`). Direct re-emission of `derived/layer_observability.csv` with denominators inline.

Conditional rates are **coverage-matched**: the numerator counts only the subset of `observed_change` events whose coverage status is in the same bucket as the denominator. This is the post-P1-fix (2026-04-23) numerator definition.

| layer | applicable | measured | partial | not_measured | not_applicable | changed (measured) | changed (partial) | changed/measured | changed/measured+partial |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `l0_network` | 22 | 0 | 0 | 22 | 31 | 0 | 0 | — | — |
| `l1_consensus` | 8 | 6 | 1 | 1 | 45 | 1 | 1 | 1/6 (16.7%) | 2/7 (28.6%) |
| `l3_rpc` | 9 | 0 | 9 | 0 | 44 | 0 | 2 | — | 2/9 (22.2%) |
| `l4_frontend` | 27 | 16 | 3 | 8 | 26 | 11 | 2 | 11/16 (68.8%) | 13/19 (68.4%) |
| `asset_onchain` | 23 | 17 | 0 | 6 | 30 | 17 | 0 | 17/17 (100.0%) | 17/17 (100.0%) |
| `offramp_cex` | 47 | 25 | 1 | 21 | 6 | 15 | 1 | 15/25 (60.0%) | 16/26 (61.5%) |

A rate of `—` indicates a zero denominator; it is an **observability gap**, not an attested negative.
