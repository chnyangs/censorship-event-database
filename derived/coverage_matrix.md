# Coverage matrix

Dataset snapshot: v0.1.0 · cutoff `2026-05-06` · commit `b117153` · generated `2026-05-07T05:00:22Z`

One row per event-layer pair. This is the explicit denominator surface: `measured_rate_denominator` rows can support conditional rates; `observability_gap`, `named_partial_only_no_conditional_rate`, and `descriptive_only_structural_circularity_v0_1` rows cannot.

## Admitted-event denominator classes by layer

| layer | measured rate denominator | partial sensitivity | named partial only | structural descriptive only | observability gap | not applicable |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `l0_network` | 0 | 0 | 0 | 0 | 22 | 31 |
| `l1_consensus` | 6 | 1 | 0 | 0 | 1 | 45 |
| `l3_rpc` | 0 | 0 | 2 | 0 | 7 | 44 |
| `l4_frontend` | 14 | 3 | 0 | 0 | 10 | 26 |
| `asset_onchain` | 0 | 0 | 0 | 17 | 6 | 30 |
| `offramp_cex` | 25 | 1 | 0 | 0 | 21 | 6 |

Phrasing lock: this matrix reports measurement eligibility, not censorship absence. A layer with `observability_gap` is unmeasured under the frame.
`denominator_reason` and `denominator_artifact` in the CSV/JSON explain why a row is or is not rate-eligible.
