# Table 3 · Archetype × research-stratum cross-tab

Dataset snapshot: **v0.2.0-rc-dryrun-3** · cutoff `2026-05-16` · commit `bfb1de7` · generated `2026-05-17T00:00:00Z`

Descriptive support for parked **C2** and **C5** (`docs/paper_claims.md §1`). Rows: rule-based deterministic archetypes. Columns: research strata (admission stratification, NOT jurisdiction / population weighting). Promotion from descriptive table to paper claim requires `observation_kind` κ ≥ 0.6.

| archetype \ stratum | S1_ofac_sdn | S2_ofac_removal | S3_doj_sec_cftc_fiod | S4_nation_state | S5_corporate | S6_supranational | total |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `asset_only` | 10 | 0 | 0 | 0 | 3 | 0 | 13 |
| `frontend_only` | 2 | 0 | 9 | 0 | 1 | 0 | 12 |
| `cex_only` | 1 | 0 | 13 | 7 | 3 | 4 | 28 |
| `multi_layer` | 3 | 1 | 6 | 7 | 1 | 0 | 18 |
| `other_single_layer` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `null_event` | 10 | 0 | 2 | 0 | 0 | 0 | 12 |
| **total** | **26** | **1** | **30** | **14** | **8** | **4** | **83** |

A non-empty cell is a descriptive statement about the admitted corpus, not a prevalence estimate. Strata are NOT equal-weighted and are NOT a population sample.
