# Table 6 · Null-case denominator (n=13)

Dataset snapshot: **v0.1.0** · cutoff `2026-05-06` · commit `5b8d353` · generated `2026-05-14T11:24:13Z`

Supports the **null-event interpretation note** in `derived/archetype_distribution.md`. (C6 was demoted to exemplar-inside-C1 on 2026-04-24 — see `docs/paper_claims.md §C6`.) Each row lists the event's `observed_no_change` layers + the evidence-anchor types their sources carry. Per validator rule, `scope_descriptor` defines the covered scope but is not an evidence anchor by itself; each `observed_no_change` row needs at least one replayable artifact such as `body_hash`+`body_path`, `query_hash`, or `measurement_ids`.

| event_id | stratum | observed_no_change layers | evidence anchors present |
| --- | --- | --- | --- |
| `iran-ransomware-ofac-2018` | `S1_ofac_sdn` | `l4_frontend` | `body_hash+body_path` |
| `irgc-ransomware-ofac-2022` | `S1_ofac_sdn` | `offramp_cex` | `body_hash+body_path` |
| `lazarus-entity-ofac-2019` | `S1_ofac_sdn` | `offramp_cex` | `body_hash+body_path` |
| `lazarus-laundering-ofac-2020` | `S1_ofac_sdn` | `offramp_cex` | `body_hash+body_path` |
| `lockbit-leader-ofac-2024` | `S1_ofac_sdn` | `offramp_cex` | `body_hash+body_path` |
| `matveev-ofac-2023` | `S1_ofac_sdn` | `offramp_cex` | `body_hash+body_path` |
| `pertsev-nl-arrest-2022` | `S3_doj_sec_cftc_fiod` | `offramp_cex` | `body_hash+body_path` |
| `russian-cybercrime-infra-ofac-2025` | `S1_ofac_sdn` | `offramp_cex` | `body_hash+body_path` |
| `sec-v-uniswap-wells-notice-2024` | `S3_doj_sec_cftc_fiod` | `l4_frontend` | `body_hash+body_path` |
| `sichuan-silence-ofac-2024` | `S1_ofac_sdn` | `offramp_cex` | `body_hash+body_path` |
| `sinbad-ofac-2023` | `S1_ofac_sdn` | `l4_frontend` | `body_hash+body_path` |
| `storm-semenov-doj-2023` | `S3_doj_sec_cftc_fiod` | `offramp_cex` | `body_hash+body_path` |
| `zservers-ofac-2025` | `S1_ofac_sdn` | `offramp_cex` | `body_hash+body_path` |

`evidence_anchors_present = NONE` indicates a validator regression (admission rules require at least one replayable artifact; `scope_descriptor` alone is insufficient). The generator aborts with a non-zero exit when any row is anchorless, so a NONE row can never reach `analysis/paper_tables/`.
