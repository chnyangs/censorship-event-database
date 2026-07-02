# Table 2 · Layer observability (denominator-honest)

Dataset snapshot: **v0.2.0-rc-dryrun-11** · cutoff `2026-06-08` · commit `ee7bf1a` · generated `2026-06-25T23:48:26Z`

Supports **C1** (`docs/paper_claims.md §1`). Direct re-emission of `derived/layer_observability.csv` with denominators inline.

Conditional rates are **coverage-matched**: the numerator counts only the subset of `observed_change` events whose coverage status is in the same bucket as the denominator. This is the post-P1-fix (2026-04-23) numerator definition.

| layer | applicable | measured | partial | not_measured | not_applicable | changed events (measured) | changed events (partial) | unique changed actions | duplicate action rows | changed/measured | changed/measured+partial |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `l0_network` | 24 | 0 | 5 | 19 | 374 | 0 | 5 | 5 | 0 | — | 5/5 (100.0%) |
| `l1_consensus` | 18 | 8 | 8 | 2 | 380 | 2 | 8 | 10 | 0 | 2/8 (25.0%) | 10/16 (62.5%) |
| `l3_rpc` | 13 | 1 | 6 | 6 | 385 | 1 | 5 | 6 | 0 | 1/1 (100.0%) | 6/7 (85.7%) |
| `l4_frontend` | 124 | 57 | 21 | 46 | 274 | 52 | 18 | 75 | 0 | 52/57 (91.2%) | 70/78 (89.7%) |
| `asset_onchain` | 49 | 23 | 4 | 22 | 349 | 23 | 3 | 29 | 1 | retracted; no rate | retracted; no rate |
| `offramp_cex` | 329 | 257 | 51 | 21 | 69 | 167 | 41 | 216 | 0 | 167/257 (65.0%) | 208/308 (67.5%) |

A rate of `—` indicates a zero denominator; it is an **observability gap**, not an attested negative.
`unique changed actions` deduplicates physical actions that are intentionally linked across event records via `observations[].action_id` (for example, the Circle USDC Tornado blacklist transaction appears in both the OFAC-triggered event and the issuer-action event). Event-rate columns remain event-record denominators; action counts are reported separately so the two units are not conflated.

`l3_rpc` has 1 measured denominator event(s) and 6 partial denominator event(s) in this snapshot. Any L3 statement must carry the inline denominator above and the sensitivity-rubric context below; do not turn the named rows into a provider-population claim.
`asset_onchain` remains **not reported as a rate** in this snapshot — the admission rubric requires the change as the admission anchor, so the ratio is structurally circular (see [`docs/paper_claims.md §C1` 'Not said'](../../docs/paper_claims.md)).

**Sensitivity reporting**. Rates flagged in [`derived/admission_sensitivity.md`](../../derived/admission_sensitivity.md) must carry their strict/current/permissive context when cited:

- **`l1_consensus`** sensitive (Δ=0.625): 0/8 (0.00) strict · 2/8 (0.25) current · 10/16 (0.62) permissive.
- **`l3_rpc`** sensitive (Δ=-0.1429): 1/1 (1.00) strict · 1/1 (1.00) current · 6/7 (0.86) permissive.
- **`l4_frontend`** sensitive (Δ=0.3009): 34/57 (0.60) strict · 52/57 (0.91) current · 70/78 (0.90) permissive.
- **`offramp_cex`** sensitive (Δ=0.2084): 120/257 (0.47) strict · 167/257 (0.65) current · 208/308 (0.68) permissive.
