# Table 2 · Layer observability (denominator-honest)

Dataset snapshot: **v0.2.0-rc-dryrun-11** · cutoff `2026-05-17` · commit `1d420be` · generated `2026-05-17T00:00:00Z`

Supports **C1** (`docs/paper_claims.md §1`). Direct re-emission of `derived/layer_observability.csv` with denominators inline.

Conditional rates are **coverage-matched**: the numerator counts only the subset of `observed_change` events whose coverage status is in the same bucket as the denominator. This is the post-P1-fix (2026-04-23) numerator definition.

| layer | applicable | measured | partial | not_measured | not_applicable | changed events (measured) | changed events (partial) | unique changed actions | duplicate action rows | changed/measured | changed/measured+partial |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `l0_network` | 26 | 0 | 0 | 26 | 79 | 0 | 0 | 0 | 0 | — | — |
| `l1_consensus` | 8 | 6 | 1 | 1 | 97 | 1 | 1 | 2 | 0 | 1/6 (16.7%) | 2/7 (28.6%) |
| `l3_rpc` | 10 | 1 | 2 | 7 | 95 | 1 | 2 | 4 | 0 | 1/1 (100.0%) | 3/3 (100.0%) |
| `l4_frontend` | 65 | 27 | 14 | 24 | 40 | 24 | 13 | 39 | 0 | 24/27 (88.9%) | 37/41 (90.2%) |
| `asset_onchain` | 26 | 17 | 0 | 9 | 79 | 17 | 0 | 20 | 1 | retracted; no rate | retracted; no rate |
| `offramp_cex` | 94 | 65 | 7 | 22 | 11 | 55 | 7 | 68 | 0 | 55/65 (84.6%) | 62/72 (86.1%) |

A rate of `—` indicates a zero denominator; it is an **observability gap**, not an attested negative.
`unique changed actions` deduplicates physical actions that are intentionally linked across event records via `observations[].action_id` (for example, the Circle USDC Tornado blacklist transaction appears in both the OFAC-triggered event and the issuer-action event). Event-rate columns remain event-record denominators; action counts are reported separately so the two units are not conflated.

`l3_rpc` has no measured denominator in this release. Its two partial rows are named Flashbots git-history observations only; do not cite them as an L3 conditional rate.
`asset_onchain` remains **not reported as a rate** at v0.1 — the admission rubric requires the change as the admission anchor, so the ratio is structurally circular (see [`docs/paper_claims.md §C1` 'Not said'](../../docs/paper_claims.md)).

**Sensitivity reporting**. Rates flagged in [`derived/admission_sensitivity.md`](../../derived/admission_sensitivity.md) must carry their strict/current/permissive context when cited:

- **`l1_consensus`** sensitive (Δ=0.2857): 0/6 (0.00) strict · 1/6 (0.17) current · 2/7 (0.29) permissive.
- **`l4_frontend`** sensitive (Δ=0.1246): 21/27 (0.78) strict · 24/27 (0.89) current · 37/41 (0.90) permissive.
- **`offramp_cex`** sensitive (Δ=0.1073): 49/65 (0.75) strict · 55/65 (0.85) current · 62/72 (0.86) permissive.
