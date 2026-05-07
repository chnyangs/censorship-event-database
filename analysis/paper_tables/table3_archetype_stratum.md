# Table 3 · Archetype × research-stratum cross-tab

Dataset snapshot: **v0.1.0** · cutoff `2026-05-06` · commit `038d4d4` · generated `2026-05-07T02:37:57Z`

Descriptive support for parked **C2** and **C5** (`docs/paper_claims.md §1`). Rows: rule-based deterministic archetypes. Columns: research strata (admission stratification, NOT jurisdiction / population weighting). Promotion from descriptive table to paper claim requires `observation_kind` κ ≥ 0.6.

| archetype \ stratum | S1_ofac_sdn | S2_ofac_removal | S3_doj_sec_cftc_fiod | S4_nation_state | S5_corporate | S6_supranational | total |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `asset_only` | 10 | 0 | 0 | 0 | 3 | 0 | 13 |
| `frontend_only` | 2 | 0 | 5 | 0 | 1 | 0 | 8 |
| `cex_only` | 1 | 0 | 4 | 6 | 2 | 2 | 15 |
| `multi_layer` | 3 | 1 | 0 | 0 | 0 | 0 | 4 |
| `other_single_layer` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `null_event` | 10 | 0 | 3 | 0 | 0 | 0 | 13 |
| **total** | **26** | **1** | **12** | **6** | **6** | **2** | **53** |

A non-empty cell is a descriptive statement about the admitted corpus, not a prevalence estimate. Strata are NOT equal-weighted and are NOT a population sample.
