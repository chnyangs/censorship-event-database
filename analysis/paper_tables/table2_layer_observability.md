# Table 2 · Layer observability (denominator-honest)

Dataset snapshot: **v0.1.0** · cutoff `2026-04-22` · commit `c81d8bb` · generated `2026-04-24T10:12:43Z`

Supports **C1** (`docs/paper_claims.md §1`). Direct re-emission of `derived/layer_observability.csv` with denominators inline.

Conditional rates are **coverage-matched**: the numerator counts only the subset of `observed_change` events whose coverage status is in the same bucket as the denominator. This is the post-P1-fix (2026-04-23) numerator definition.

| layer | applicable | measured | partial | not_measured | not_applicable | changed events (measured) | changed events (partial) | unique changed actions | duplicate action rows | changed/measured | changed/measured+partial |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `l0_network` | 22 | 0 | 0 | 22 | 31 | 0 | 0 | 0 | 0 | — | — |
| `l1_consensus` | 8 | 6 | 1 | 1 | 45 | 1 | 1 | 2 | 0 | 1/6 (16.7%) | 2/7 (28.6%) |
| `l3_rpc` | 9 | 0 | 9 | 0 | 44 | 0 | 2 | 2 | 0 | — | 2/9 (22.2%) |
| `l4_frontend` | 27 | 16 | 3 | 8 | 26 | 11 | 2 | 13 | 0 | 11/16 (68.8%) | 13/19 (68.4%) |
| `asset_onchain` | 23 | 17 | 0 | 6 | 30 | 17 | 0 | 20 | 1 | 17/17 (100.0%) | 17/17 (100.0%) |
| `offramp_cex` | 47 | 25 | 1 | 21 | 6 | 15 | 1 | 17 | 0 | 15/25 (60.0%) | 16/26 (61.5%) |

A rate of `—` indicates a zero denominator; it is an **observability gap**, not an attested negative.
`unique changed actions` deduplicates physical actions that are intentionally linked across event records via `observations[].action_id` (for example, the Circle USDC Tornado blacklist transaction appears in both the OFAC-triggered event and the issuer-action event). Event-rate columns remain event-record denominators; action counts are reported separately so the two units are not conflated.
