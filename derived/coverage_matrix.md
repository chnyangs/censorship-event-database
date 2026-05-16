# Coverage matrix

Dataset snapshot: v0.2.0-rc-dryrun-2 · cutoff `2026-05-16` · commit `f8dc941` · generated `2026-05-16T12:00:00Z`

One row per event-layer pair. This is the explicit denominator surface: `measured_rate_denominator` rows can support conditional rates; `observability_gap`, `named_partial_only_no_conditional_rate`, and `descriptive_only_structural_circularity_v0_1` rows cannot.

## Admitted-event denominator classes by layer

| layer | measured rate denominator | partial sensitivity | named partial only | structural descriptive only | observability gap | not applicable |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `l0_network` | 0 | 0 | 0 | 0 | 23 | 39 |
| `l1_consensus` | 6 | 1 | 0 | 0 | 1 | 54 |
| `l3_rpc` | 0 | 0 | 2 | 0 | 7 | 53 |
| `l4_frontend` | 17 | 5 | 0 | 0 | 14 | 26 |
| `asset_onchain` | 0 | 0 | 0 | 17 | 7 | 38 |
| `offramp_cex` | 32 | 1 | 0 | 0 | 21 | 8 |

Phrasing lock: this matrix reports measurement eligibility, not censorship absence. A layer with `observability_gap` is unmeasured under the frame.
`denominator_reason` and `denominator_artifact` in the CSV/JSON explain why a row is or is not rate-eligible.
