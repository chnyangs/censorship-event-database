# Table 3 · Archetype × research-stratum cross-tab

Dataset snapshot: **v0.2.0-rc-dryrun-11** · cutoff `2026-06-08` · commit `ee7bf1a` · generated `2026-06-25T23:48:26Z`

Descriptive support for parked **C2** and **C5** (`docs/paper_claims.md §1`). Rows: rule-based deterministic archetypes. Columns: research strata (admission stratification, NOT jurisdiction / population weighting). Promotion from descriptive table to paper claim requires `observation_kind` κ ≥ 0.6.

| archetype \ stratum | S1_ofac_sdn | S2_ofac_removal | S3_doj_sec_cftc_fiod | S4_nation_state | S5_corporate | S6_supranational | total |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `asset_only` | 10 | 0 | 2 | 0 | 9 | 0 | 21 |
| `frontend_only` | 2 | 0 | 14 | 5 | 25 | 0 | 46 |
| `cex_only` | 2 | 0 | 44 | 71 | 52 | 15 | 184 |
| `multi_layer` | 3 | 1 | 10 | 10 | 5 | 0 | 29 |
| `other_single_layer` | 0 | 0 | 0 | 9 | 2 | 0 | 11 |
| `null_event` | 43 | 0 | 14 | 24 | 10 | 16 | 107 |
| **total** | **60** | **1** | **84** | **119** | **103** | **31** | **398** |

A non-empty cell is a descriptive statement about the admitted corpus, not a prevalence estimate. Strata are NOT equal-weighted and are NOT a population sample.
