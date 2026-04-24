# Table 6 · Null-case denominator (n=13)

Dataset snapshot: **v0.1.0** · cutoff `2026-04-22` · commit `930f3d6` · generated `2026-04-24T03:30:13Z`

Supports **C6** and the null-event interpretation note in `derived/archetype_distribution.md`. Each row lists the event's `observed_no_change` layers + the evidence-anchor types their sources carry. Per validator rule, any one of `body_hash`+`body_path`, `query_hash`, `measurement_ids`, or `scope_descriptor` is sufficient to admit an `observed_no_change` row.

| event_id | stratum | observed_no_change layers | evidence anchors present |
| --- | --- | --- | --- |
| `iran-ransomware-ofac-2018` | `S1_ofac_sdn` | `l4_frontend` | `body_hash+body_path` |
| `irgc-ransomware-ofac-2022` | `S1_ofac_sdn` | `offramp_cex` | `body_hash+body_path`, `scope_descriptor` |
| `lazarus-entity-ofac-2019` | `S1_ofac_sdn` | `offramp_cex` | `body_hash+body_path`, `scope_descriptor` |
| `lazarus-laundering-ofac-2020` | `S1_ofac_sdn` | `offramp_cex` | `body_hash+body_path`, `scope_descriptor` |
| `lockbit-leader-ofac-2024` | `S1_ofac_sdn` | `offramp_cex` | `body_hash+body_path`, `scope_descriptor` |
| `matveev-ofac-2023` | `S1_ofac_sdn` | `offramp_cex` | `body_hash+body_path`, `scope_descriptor` |
| `pertsev-nl-arrest-2022` | `S3_doj_sec_cftc_fiod` | `offramp_cex` | `body_hash+body_path`, `scope_descriptor` |
| `russian-cybercrime-infra-ofac-2025` | `S1_ofac_sdn` | `offramp_cex` | `body_hash+body_path`, `scope_descriptor` |
| `sec-v-uniswap-wells-notice-2024` | `S3_doj_sec_cftc_fiod` | `l4_frontend` | `body_hash+body_path`, `scope_descriptor` |
| `sichuan-silence-ofac-2024` | `S1_ofac_sdn` | `offramp_cex` | `body_hash+body_path`, `scope_descriptor` |
| `sinbad-ofac-2023` | `S1_ofac_sdn` | `l4_frontend` | `body_hash+body_path` |
| `storm-semenov-doj-2023` | `S3_doj_sec_cftc_fiod` | `offramp_cex` | `body_hash+body_path`, `scope_descriptor` |
| `zservers-ofac-2025` | `S1_ofac_sdn` | `offramp_cex` | `body_hash+body_path`, `scope_descriptor` |

`evidence_anchors_present = NONE` indicates a validator regression (admission rules require at least one of the four anchor types). The generator aborts with a non-zero exit when any row is anchorless, so a NONE row can never reach `analysis/paper_tables/`.
