# Coverage matrix

Dataset snapshot: v0.2.0-rc-dryrun-11 · cutoff `2026-06-02` · commit `b6c6fae` · generated `2026-06-02T00:00:00Z`

One row per event-layer pair. This is the explicit denominator surface: `measured_rate_denominator` rows can support conditional rates; `observability_gap`, `named_partial_only_no_conditional_rate`, and `descriptive_only_structural_circularity_v0_1` rows cannot.

## Admitted-event denominator classes by layer

| layer | measured rate denominator | partial sensitivity | named partial only | structural descriptive only | observability gap | not applicable |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `l0_network` | 0 | 3 | 0 | 0 | 35 | 327 |
| `l1_consensus` | 8 | 8 | 0 | 0 | 3 | 346 |
| `l3_rpc` | 1 | 0 | 6 | 0 | 9 | 349 |
| `l4_frontend` | 55 | 21 | 0 | 0 | 56 | 233 |
| `asset_onchain` | 0 | 0 | 0 | 20 | 24 | 321 |
| `offramp_cex` | 242 | 44 | 0 | 0 | 25 | 54 |

Phrasing lock: this matrix reports measurement eligibility, not censorship absence. A layer with `observability_gap` is unmeasured under the frame.
`denominator_reason` and `denominator_artifact` in the CSV/JSON explain why a row is or is not rate-eligible.
