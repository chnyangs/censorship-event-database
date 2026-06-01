# Table 2 · Layer observability (denominator-honest)

Dataset snapshot: **v0.2.0-rc-dryrun-11** · cutoff `2026-06-01` · commit `558ea65` · generated `2026-06-01T01:29:23Z`

Supports **C1** (`docs/paper_claims.md §1`). Direct re-emission of `derived/layer_observability.csv` with denominators inline.

Conditional rates are **coverage-matched**: the numerator counts only the subset of `observed_change` events whose coverage status is in the same bucket as the denominator. This is the post-P1-fix (2026-04-23) numerator definition.

| layer | applicable | measured | partial | not_measured | not_applicable | changed events (measured) | changed events (partial) | unique changed actions | duplicate action rows | changed/measured | changed/measured+partial |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `l0_network` | 41 | 0 | 2 | 39 | 326 | 0 | 2 | 2 | 0 | — | 2/2 (100.0%) |
| `l1_consensus` | 19 | 8 | 8 | 3 | 348 | 2 | 8 | 10 | 0 | 2/8 (25.0%) | 10/16 (62.5%) |
| `l3_rpc` | 16 | 2 | 5 | 9 | 351 | 2 | 4 | 7 | 0 | 2/2 (100.0%) | 6/7 (85.7%) |
| `l4_frontend` | 136 | 54 | 27 | 55 | 231 | 49 | 23 | 78 | 0 | 49/54 (90.7%) | 72/81 (88.9%) |
| `asset_onchain` | 46 | 18 | 2 | 26 | 321 | 18 | 1 | 22 | 1 | retracted; no rate | retracted; no rate |
| `offramp_cex` | 313 | 236 | 51 | 26 | 54 | 157 | 41 | 206 | 0 | 157/236 (66.5%) | 198/287 (69.0%) |

A rate of `—` indicates a zero denominator; it is an **observability gap**, not an attested negative.
`unique changed actions` deduplicates physical actions that are intentionally linked across event records via `observations[].action_id` (for example, the Circle USDC Tornado blacklist transaction appears in both the OFAC-triggered event and the issuer-action event). Event-rate columns remain event-record denominators; action counts are reported separately so the two units are not conflated.

`l3_rpc` has no measured denominator in this release. Its two partial rows are named Flashbots git-history observations only; do not cite them as an L3 conditional rate.
`asset_onchain` remains **not reported as a rate** at v0.1 — the admission rubric requires the change as the admission anchor, so the ratio is structurally circular (see [`docs/paper_claims.md §C1` 'Not said'](../../docs/paper_claims.md)).

**Sensitivity reporting**. Rates flagged in [`derived/admission_sensitivity.md`](../../derived/admission_sensitivity.md) must carry their strict/current/permissive context when cited:

- **`l1_consensus`** sensitive (Δ=0.625): 0/8 (0.00) strict · 2/8 (0.25) current · 10/16 (0.62) permissive.
- **`l3_rpc`** sensitive (Δ=-0.1429): 2/2 (1.00) strict · 2/2 (1.00) current · 6/7 (0.86) permissive.
- **`l4_frontend`** sensitive (Δ=0.3333): 30/54 (0.56) strict · 49/54 (0.91) current · 72/81 (0.89) permissive.
- **`offramp_cex`** sensitive (Δ=0.3001): 92/236 (0.39) strict · 157/236 (0.67) current · 198/287 (0.69) permissive.
