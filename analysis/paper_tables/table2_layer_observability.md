# Table 2 · Layer observability (denominator-honest)

Dataset snapshot: **v0.2.0-rc-dryrun-11** · cutoff `2026-06-02` · commit `137626c` · generated `2026-06-02T00:00:00Z`

Supports **C1** (`docs/paper_claims.md §1`). Direct re-emission of `derived/layer_observability.csv` with denominators inline.

Conditional rates are **coverage-matched**: the numerator counts only the subset of `observed_change` events whose coverage status is in the same bucket as the denominator. This is the post-P1-fix (2026-04-23) numerator definition.

| layer | applicable | measured | partial | not_measured | not_applicable | changed events (measured) | changed events (partial) | unique changed actions | duplicate action rows | changed/measured | changed/measured+partial |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `l0_network` | 41 | 0 | 3 | 38 | 324 | 0 | 3 | 3 | 0 | — | 3/3 (100.0%) |
| `l1_consensus` | 19 | 8 | 8 | 3 | 346 | 2 | 8 | 10 | 0 | 2/8 (25.0%) | 10/16 (62.5%) |
| `l3_rpc` | 16 | 1 | 6 | 9 | 349 | 1 | 5 | 6 | 0 | 1/1 (100.0%) | 6/7 (85.7%) |
| `l4_frontend` | 132 | 54 | 22 | 56 | 233 | 49 | 19 | 74 | 0 | 49/54 (90.7%) | 68/76 (89.5%) |
| `asset_onchain` | 45 | 18 | 2 | 25 | 320 | 18 | 1 | 22 | 1 | retracted; no rate | retracted; no rate |
| `offramp_cex` | 312 | 242 | 44 | 26 | 53 | 162 | 34 | 204 | 0 | 162/242 (66.9%) | 196/286 (68.5%) |

A rate of `—` indicates a zero denominator; it is an **observability gap**, not an attested negative.
`unique changed actions` deduplicates physical actions that are intentionally linked across event records via `observations[].action_id` (for example, the Circle USDC Tornado blacklist transaction appears in both the OFAC-triggered event and the issuer-action event). Event-rate columns remain event-record denominators; action counts are reported separately so the two units are not conflated.

`l3_rpc` has 1 measured denominator event(s) and 6 partial denominator event(s) in this snapshot. Any L3 statement must carry the inline denominator above and the sensitivity-rubric context below; do not turn the named rows into a provider-population claim.
`asset_onchain` remains **not reported as a rate** in this snapshot — the admission rubric requires the change as the admission anchor, so the ratio is structurally circular (see [`docs/paper_claims.md §C1` 'Not said'](../../docs/paper_claims.md)).

**Sensitivity reporting**. Rates flagged in [`derived/admission_sensitivity.md`](../../derived/admission_sensitivity.md) must carry their strict/current/permissive context when cited:

- **`l1_consensus`** sensitive (Δ=0.625): 0/8 (0.00) strict · 2/8 (0.25) current · 10/16 (0.62) permissive.
- **`l3_rpc`** sensitive (Δ=-0.1429): 1/1 (1.00) strict · 1/1 (1.00) current · 6/7 (0.86) permissive.
- **`l4_frontend`** sensitive (Δ=0.3391): 30/54 (0.56) strict · 49/54 (0.91) current · 68/76 (0.89) permissive.
- **`offramp_cex`** sensitive (Δ=0.2308): 110/242 (0.45) strict · 162/242 (0.67) current · 196/286 (0.69) permissive.
