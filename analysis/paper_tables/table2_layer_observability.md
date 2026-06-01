# Table 2 · Layer observability (denominator-honest)

Dataset snapshot: **v0.2.0-rc-dryrun-11** · cutoff `2026-06-01` · commit `7c0cb78` · generated `2026-06-01T04:09:15Z`

Supports **C1** (`docs/paper_claims.md §1`). Direct re-emission of `derived/layer_observability.csv` with denominators inline.

Conditional rates are **coverage-matched**: the numerator counts only the subset of `observed_change` events whose coverage status is in the same bucket as the denominator. This is the post-P1-fix (2026-04-23) numerator definition.

| layer | applicable | measured | partial | not_measured | not_applicable | changed events (measured) | changed events (partial) | unique changed actions | duplicate action rows | changed/measured | changed/measured+partial |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `l0_network` | 41 | 0 | 3 | 38 | 325 | 0 | 3 | 3 | 0 | — | 3/3 (100.0%) |
| `l1_consensus` | 19 | 8 | 8 | 3 | 347 | 2 | 8 | 10 | 0 | 2/8 (25.0%) | 10/16 (62.5%) |
| `l3_rpc` | 16 | 1 | 6 | 9 | 350 | 1 | 5 | 6 | 0 | 1/1 (100.0%) | 6/7 (85.7%) |
| `l4_frontend` | 133 | 54 | 23 | 56 | 233 | 49 | 20 | 75 | 0 | 49/54 (90.7%) | 69/77 (89.6%) |
| `asset_onchain` | 46 | 18 | 2 | 26 | 320 | 18 | 1 | 22 | 1 | retracted; no rate | retracted; no rate |
| `offramp_cex` | 313 | 237 | 49 | 27 | 53 | 157 | 39 | 204 | 0 | 157/237 (66.2%) | 196/286 (68.5%) |

A rate of `—` indicates a zero denominator; it is an **observability gap**, not an attested negative.
`unique changed actions` deduplicates physical actions that are intentionally linked across event records via `observations[].action_id` (for example, the Circle USDC Tornado blacklist transaction appears in both the OFAC-triggered event and the issuer-action event). Event-rate columns remain event-record denominators; action counts are reported separately so the two units are not conflated.

`l3_rpc` has no measured denominator in this release. Its two partial rows are named Flashbots git-history observations only; do not cite them as an L3 conditional rate.
`asset_onchain` remains **not reported as a rate** at v0.1 — the admission rubric requires the change as the admission anchor, so the ratio is structurally circular (see [`docs/paper_claims.md §C1` 'Not said'](../../docs/paper_claims.md)).

**Sensitivity reporting**. Rates flagged in [`derived/admission_sensitivity.md`](../../derived/admission_sensitivity.md) must carry their strict/current/permissive context when cited:

- **`l1_consensus`** sensitive (Δ=0.625): 0/8 (0.00) strict · 2/8 (0.25) current · 10/16 (0.62) permissive.
- **`l3_rpc`** sensitive (Δ=-0.1429): 1/1 (1.00) strict · 1/1 (1.00) current · 6/7 (0.86) permissive.
- **`l4_frontend`** sensitive (Δ=0.3405): 30/54 (0.56) strict · 49/54 (0.91) current · 69/77 (0.90) permissive.
- **`offramp_cex`** sensitive (Δ=0.2929): 93/237 (0.39) strict · 157/237 (0.66) current · 196/286 (0.69) permissive.
