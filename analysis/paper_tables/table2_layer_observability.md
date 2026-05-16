# Table 2 · Layer observability (denominator-honest)

Dataset snapshot: **v0.2.0-rc-dryrun-2** · cutoff `2026-05-16` · commit `f8dc941` · generated `2026-05-16T12:00:00Z`

Supports **C1** (`docs/paper_claims.md §1`). Direct re-emission of `derived/layer_observability.csv` with denominators inline.

Conditional rates are **coverage-matched**: the numerator counts only the subset of `observed_change` events whose coverage status is in the same bucket as the denominator. This is the post-P1-fix (2026-04-23) numerator definition.

| layer | applicable | measured | partial | not_measured | not_applicable | changed events (measured) | changed events (partial) | unique changed actions | duplicate action rows | changed/measured | changed/measured+partial |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `l0_network` | 23 | 0 | 0 | 23 | 39 | 0 | 0 | 0 | 0 | — | — |
| `l1_consensus` | 8 | 6 | 1 | 1 | 54 | 1 | 1 | 2 | 0 | 1/6 (16.7%) | 2/7 (28.6%) |
| `l3_rpc` | 9 | 0 | 2 | 7 | 53 | 0 | 2 | 2 | 0 | — | named-only; no rate |
| `l4_frontend` | 36 | 17 | 5 | 14 | 26 | 14 | 4 | 20 | 0 | 14/17 (82.4%) | 18/22 (81.8%) |
| `asset_onchain` | 24 | 17 | 0 | 7 | 38 | 17 | 0 | 20 | 1 | retracted; no rate | retracted; no rate |
| `offramp_cex` | 54 | 32 | 1 | 21 | 8 | 22 | 1 | 24 | 0 | 22/32 (68.8%) | 23/33 (69.7%) |

A rate of `—` indicates a zero denominator; it is an **observability gap**, not an attested negative.
`unique changed actions` deduplicates physical actions that are intentionally linked across event records via `observations[].action_id` (for example, the Circle USDC Tornado blacklist transaction appears in both the OFAC-triggered event and the issuer-action event). Event-rate columns remain event-record denominators; action counts are reported separately so the two units are not conflated.

`l3_rpc` has no measured denominator in this release. Its two partial rows are named Flashbots git-history observations only; do not cite them as an L3 conditional rate.
`asset_onchain` remains **not reported as a rate** at v0.1 — the admission rubric requires the change as the admission anchor, so the ratio is structurally circular (see [`docs/paper_claims.md §C1` 'Not said'](../../docs/paper_claims.md)).

**Sensitivity reporting**. Rates flagged in [`derived/admission_sensitivity.md`](../../derived/admission_sensitivity.md) must carry their strict/current/permissive context when cited:

- **`l1_consensus`** sensitive (Δ=0.2857): 0/6 (0.00) strict · 1/6 (0.17) current · 2/7 (0.29) permissive.
- **`l4_frontend`** sensitive (Δ=0.1123): 12/17 (0.71) strict · 14/17 (0.82) current · 18/22 (0.82) permissive.
- **`offramp_cex`** moderate (Δ=0.072): 20/32 (0.62) strict · 22/32 (0.69) current · 23/33 (0.70) permissive.
