# Coverage matrix

Dataset snapshot: v0.2.0-rc-dryrun-11 · cutoff `2026-06-02` · commit `6678414` · generated `2026-06-04T04:52:47Z`

One row per event-layer pair. This is the explicit denominator surface: `measured_rate_denominator` rows can support conditional rates; `observability_gap`, `named_partial_only_no_conditional_rate`, and `descriptive_only_structural_circularity_v0_1` rows cannot.

## Admitted-event denominator classes by layer

| layer | measured rate denominator | partial sensitivity | named partial only | structural descriptive only | observability gap | not applicable |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `l0_network` | 0 | 3 | 0 | 0 | 19 | 343 |
| `l1_consensus` | 8 | 8 | 0 | 0 | 2 | 347 |
| `l3_rpc` | 1 | 0 | 6 | 0 | 6 | 352 |
| `l4_frontend` | 55 | 21 | 0 | 0 | 48 | 241 |
| `asset_onchain` | 0 | 0 | 0 | 20 | 19 | 326 |
| `offramp_cex` | 242 | 44 | 0 | 0 | 20 | 59 |

Phrasing lock: this matrix reports measurement eligibility, not censorship absence. A layer with `observability_gap` is unmeasured under the frame.
`denominator_reason` and `denominator_artifact` in the CSV/JSON explain why a row is or is not rate-eligible.
