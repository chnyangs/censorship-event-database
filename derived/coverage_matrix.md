# Coverage matrix

Dataset snapshot: v0.2.0-rc-dryrun-2 · cutoff `2026-05-16` · commit `c6bc9d9` · generated `2026-05-18T10:40:00Z`

One row per event-layer pair. This is the explicit denominator surface: `measured_rate_denominator` rows can support conditional rates; `observability_gap`, `named_partial_only_no_conditional_rate`, and `descriptive_only_structural_circularity_v0_1` rows cannot.

## Admitted-event denominator classes by layer

| layer | measured rate denominator | partial sensitivity | named partial only | structural descriptive only | observability gap | not applicable |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `l0_network` | 0 | 0 | 0 | 0 | 25 | 58 |
| `l1_consensus` | 6 | 1 | 0 | 0 | 1 | 75 |
| `l3_rpc` | 0 | 0 | 2 | 0 | 7 | 74 |
| `l4_frontend` | 24 | 10 | 0 | 0 | 16 | 33 |
| `asset_onchain` | 0 | 0 | 0 | 17 | 7 | 59 |
| `offramp_cex` | 47 | 6 | 0 | 0 | 21 | 9 |

Phrasing lock: this matrix reports measurement eligibility, not censorship absence. A layer with `observability_gap` is unmeasured under the frame.
`denominator_reason` and `denominator_artifact` in the CSV/JSON explain why a row is or is not rate-eligible.
