# Coverage matrix

Dataset snapshot: v0.2.0-rc-dryrun-4 · cutoff `2026-05-16` · commit `a0d61e2` · generated `2026-05-20T00:00:00Z`

One row per event-layer pair. This is the explicit denominator surface: `measured_rate_denominator` rows can support conditional rates; `observability_gap`, `named_partial_only_no_conditional_rate`, and `descriptive_only_structural_circularity_v0_1` rows cannot.

## Admitted-event denominator classes by layer

| layer | measured rate denominator | partial sensitivity | named partial only | structural descriptive only | observability gap | not applicable |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `l0_network` | 0 | 0 | 0 | 0 | 26 | 79 |
| `l1_consensus` | 6 | 1 | 0 | 0 | 1 | 97 |
| `l3_rpc` | 1 | 0 | 2 | 0 | 7 | 95 |
| `l4_frontend` | 27 | 14 | 0 | 0 | 24 | 40 |
| `asset_onchain` | 0 | 0 | 0 | 17 | 9 | 79 |
| `offramp_cex` | 65 | 7 | 0 | 0 | 22 | 11 |

Phrasing lock: this matrix reports measurement eligibility, not censorship absence. A layer with `observability_gap` is unmeasured under the frame.
`denominator_reason` and `denominator_artifact` in the CSV/JSON explain why a row is or is not rate-eligible.
