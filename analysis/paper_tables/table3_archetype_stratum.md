# Table 3 · Archetype × research-stratum cross-tab

Dataset snapshot: **v0.2.0-rc-dryrun-11** · cutoff `2026-06-01` · commit `4acc680` · generated `2026-06-01T03:34:29Z`

Descriptive support for parked **C2** and **C5** (`docs/paper_claims.md §1`). Rows: rule-based deterministic archetypes. Columns: research strata (admission stratification, NOT jurisdiction / population weighting). Promotion from descriptive table to paper claim requires `observation_kind` κ ≥ 0.6.

| archetype \ stratum | S1_ofac_sdn | S2_ofac_removal | S3_doj_sec_cftc_fiod | S4_nation_state | S5_corporate | S6_supranational | total |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `asset_only` | 10 | 0 | 0 | 0 | 4 | 0 | 14 |
| `frontend_only` | 2 | 0 | 14 | 5 | 24 | 0 | 45 |
| `cex_only` | 2 | 0 | 41 | 65 | 51 | 14 | 173 |
| `multi_layer` | 3 | 1 | 10 | 10 | 5 | 0 | 29 |
| `other_single_layer` | 0 | 0 | 0 | 7 | 2 | 0 | 9 |
| `null_event` | 35 | 0 | 12 | 24 | 10 | 16 | 97 |
| **total** | **52** | **1** | **77** | **111** | **96** | **30** | **367** |

A non-empty cell is a descriptive statement about the admitted corpus, not a prevalence estimate. Strata are NOT equal-weighted and are NOT a population sample.
