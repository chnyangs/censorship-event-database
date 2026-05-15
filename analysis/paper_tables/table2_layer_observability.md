# Table 2 · Layer observability (denominator-honest)

Dataset snapshot: **v0.1.0** · cutoff `2026-05-06` · commit `5b8d353` · generated `2026-05-14T11:24:13Z`

Supports **C1** (`docs/paper_claims.md §1`). Direct re-emission of `derived/layer_observability.csv` with denominators inline.

Conditional rates are **coverage-matched**: the numerator counts only the subset of `observed_change` events whose coverage status is in the same bucket as the denominator. This is the post-P1-fix (2026-04-23) numerator definition.

| layer | applicable | measured | partial | not_measured | not_applicable | changed events (measured) | changed events (partial) | unique changed actions | duplicate action rows | changed/measured | changed/measured+partial |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `l0_network` | 22 | 0 | 0 | 22 | 31 | 0 | 0 | 0 | 0 | — | — |
| `l1_consensus` | 8 | 6 | 1 | 1 | 45 | 1 | 1 | 2 | 0 | 1/6 (16.7%) | 2/7 (28.6%) |
| `l3_rpc` | 9 | 0 | 2 | 7 | 44 | 0 | 2 | 2 | 0 | — | named-only; no rate |
| `l4_frontend` | 27 | 14 | 3 | 10 | 26 | 10 | 2 | 12 | 0 | 10/14 (71.4%) | 12/17 (70.6%) |
| `asset_onchain` | 23 | 17 | 0 | 6 | 30 | 17 | 0 | 20 | 1 | retracted; no rate | retracted; no rate |
| `offramp_cex` | 47 | 25 | 1 | 21 | 6 | 15 | 1 | 17 | 0 | 15/25 (60.0%) | 16/26 (61.5%) |

A rate of `—` indicates a zero denominator; it is an **observability gap**, not an attested negative.
`unique changed actions` deduplicates physical actions that are intentionally linked across event records via `observations[].action_id` (for example, the Circle USDC Tornado blacklist transaction appears in both the OFAC-triggered event and the issuer-action event). Event-rate columns remain event-record denominators; action counts are reported separately so the two units are not conflated.

`l3_rpc` has no measured denominator in this release. Its two partial rows are named Flashbots git-history observations only; do not cite them as an L3 conditional rate.
`asset_onchain` remains **not reported as a rate** at v0.1 — the admission rubric requires the change as the admission anchor, so the ratio is structurally circular (see [`docs/paper_claims.md §C1` 'Not said'](../../docs/paper_claims.md)).

**Sensitivity reporting**. Rates flagged in [`derived/admission_sensitivity.md`](../../derived/admission_sensitivity.md) must carry their strict/current/permissive context when cited:

- **`l1_consensus`** sensitive (Δ=0.2857): 0/6 (0.00) strict · 1/6 (0.17) current · 2/7 (0.29) permissive.
- **`l4_frontend`** sensitive (Δ=0.1345): 8/14 (0.57) strict · 10/14 (0.71) current · 12/17 (0.71) permissive.
- **`offramp_cex`** moderate (Δ=0.0954): 13/25 (0.52) strict · 15/25 (0.60) current · 16/26 (0.62) permissive.
