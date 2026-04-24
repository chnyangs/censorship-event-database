# Table 1 · Case roles (n=53)

Dataset snapshot: **v0.1.0** · cutoff `2026-04-22` · commit `dd67577` · generated `2026-04-24T09:59:02Z`

Supports `docs/paper_claims.md §0` (case-role convention). Each event's admission tier determines how it may be cited: `anchor_case` = named in narrative and figures; `empirical_case` = aggregate-count contributor only; `null_case` = denominator for `observed_no_change` claims only.

## Summary

| admission_tier | count |
| --- | ---: |
| `anchor_case` | 5 |
| `empirical_case` | 35 |
| `null_case` | 13 |
| **total** | **53** |

| trigger precision bucket | count |
| --- | ---: |
| `hour` | 5 |
| `day` | 48 |

Only the `hour`-precision subset is admissible for hour-granularity latency claims (Table 4).

## Per-event rows

| event_id | tier | stratum | shape | trigger_type | prec | target_kind | target_enum | Δlayers | archetype | t=action | reversal | last_verified | last_audit |
| --- | --- | --- | --- | --- | --- | --- | --- | ---: | --- | :---: | :---: | --- | --- |
| `aeza-group-ofac-2025` | `empirical_case` | `S1_ofac_sdn` | `comparison` | `ofac_sdn_designation` | `day` | `entity` | `subset` | 1 | `asset_only` | · | · | `2026-04-22` | `—` |
| `binance-4framework-2023` | `empirical_case` | `S3_doj_sec_cftc_fiod` | `comparison` | `doj_indictment` | `day` | `entity` | `subset` | 1 | `cex_only` | · | · | `2026-04-22` | `—` |
| `bitzlato-doj-2023` | `empirical_case` | `S3_doj_sec_cftc_fiod` | `comparison` | `doj_indictment` | `day` | `entity` | `complete` | 1 | `cex_only` | · | · | `2026-04-21` | `—` |
| `blender-ofac-2022` | `empirical_case` | `S1_ofac_sdn` | `comparison` | `ofac_sdn_designation` | `day` | `address_set` | `complete` | 1 | `frontend_only` | · | · | `2026-04-21` | `—` |
| `btc-e-doj-2017` | `empirical_case` | `S3_doj_sec_cftc_fiod` | `comparison` | `doj_indictment` | `day` | `entity` | `subset` | 1 | `frontend_only` | · | · | `2026-04-22` | `—` |
| `canada-convoy-freeze-2022` | `empirical_case` | `S4_nation_state` | `comparison` | `nation_state_block` | `day` | `entity` | `subset` | 1 | `cex_only` | · | · | `2026-04-22` | `—` |
| `cftc-v-ooki-dao-2022` | `empirical_case` | `S3_doj_sec_cftc_fiod` | `comparison` | `cftc_action` | `day` | `entity` | `complete` | 1 | `frontend_only` | · | · | `2026-04-22` | `—` |
| `chatex-ofac-2021` | `anchor_case` | `S1_ofac_sdn` | `comparison` | `ofac_sdn_designation` | `day` | `address_set` | `complete` | 2 | `multi_layer` | · | · | `2026-04-22` | `—` |
| `china-pboc-crypto-ban-2021` | `empirical_case` | `S4_nation_state` | `comparison` | `nation_state_block` | `hour` | `entity` | `complete` | 1 | `cex_only` | · | · | `2026-04-21` | `—` |
| `chipmixer-doj-2023` | `empirical_case` | `S3_doj_sec_cftc_fiod` | `comparison` | `doj_seizure_order` | `day` | `entity` | `subset` | 1 | `frontend_only` | · | · | `2026-04-22` | `—` |
| `circle-usdc-tornado-2022` | `empirical_case` | `S5_corporate` | `comparison` | `corporate_policy_change` | `hour` | `address_set` | `subset` | 1 | `asset_only` | ✓ | · | `2026-04-22` | `—` |
| `coinbase-india-exit-2022` | `empirical_case` | `S5_corporate` | `comparison` | `corporate_policy_change` | `day` | `domain` | `complete` | 1 | `cex_only` | · | · | `2026-04-22` | `—` |
| `cryptex-ofac-2024` | `anchor_case` | `S1_ofac_sdn` | `comparison` | `ofac_sdn_designation` | `day` | `address_set` | `complete` | 2 | `multi_layer` | · | · | `2026-04-21` | `2026-04-22` |
| `dprk-usdt-network-ofac-2025` | `empirical_case` | `S1_ofac_sdn` | `comparison` | `ofac_sdn_designation` | `day` | `address_set` | `complete` | 1 | `asset_only` | · | · | `2026-04-22` | `—` |
| `eu-12th-russia-sanctions-2023` | `empirical_case` | `S6_supranational` | `comparison` | `non_us_sanctions` | `day` | `entity` | `subset` | 1 | `cex_only` | · | · | `2026-04-22` | `—` |
| `eu-mica-2023` | `empirical_case` | `S6_supranational` | `comparison` | `supranational_regulation` | `day` | `entity` | `subset` | 1 | `cex_only` | · | · | `2026-04-22` | `—` |
| `funnull-cdn-ofac-2025` | `empirical_case` | `S1_ofac_sdn` | `comparison` | `ofac_sdn_designation` | `day` | `entity` | `subset` | 1 | `asset_only` | · | · | `2026-04-22` | `—` |
| `garantex-ofac-2022` | `empirical_case` | `S1_ofac_sdn` | `comparison` | `ofac_sdn_designation` | `day` | `entity` | `complete` | 1 | `cex_only` | · | · | `2026-04-21` | `—` |
| `grinex-garantex-successor-ofac-2025` | `empirical_case` | `S1_ofac_sdn` | `comparison` | `ofac_sdn_designation` | `day` | `address_set` | `complete` | 1 | `asset_only` | · | · | `2026-04-21` | `—` |
| `hydra-doj-2022` | `empirical_case` | `S3_doj_sec_cftc_fiod` | `comparison` | `doj_seizure_order` | `day` | `entity` | `subset` | 1 | `frontend_only` | · | · | `2026-04-22` | `—` |
| `hydra-ofac-2022` | `empirical_case` | `S1_ofac_sdn` | `comparison` | `ofac_sdn_designation` | `day` | `entity` | `complete` | 1 | `frontend_only` | · | · | `2026-04-21` | `—` |
| `india-rbi-crypto-ban-2018` | `empirical_case` | `S4_nation_state` | `comparison` | `nation_state_block` | `day` | `entity` | `subset` | 1 | `cex_only` | · | · | `2026-04-22` | `—` |
| `iran-ransomware-ofac-2018` | `null_case` | `S1_ofac_sdn` | `null_event` | `ofac_sdn_designation` | `day` | `address_set` | `complete` | 0 | `null_event` | · | · | `2026-04-22` | `—` |
| `irgc-ransomware-ofac-2022` | `null_case` | `S1_ofac_sdn` | `null_event` | `ofac_sdn_designation` | `day` | `address_set` | `complete` | 0 | `null_event` | · | · | `2026-04-22` | `—` |
| `korea-travel-rule-2022` | `empirical_case` | `S4_nation_state` | `comparison` | `nation_state_block` | `day` | `entity` | `subset` | 1 | `cex_only` | · | · | `2026-04-22` | `—` |
| `lazarus-entity-ofac-2019` | `null_case` | `S1_ofac_sdn` | `null_event` | `ofac_sdn_designation` | `day` | `entity` | `subset` | 0 | `null_event` | · | · | `2026-04-22` | `—` |
| `lazarus-laundering-ofac-2020` | `null_case` | `S1_ofac_sdn` | `null_event` | `ofac_sdn_designation` | `day` | `address_set` | `complete` | 0 | `null_event` | · | · | `2026-04-22` | `—` |
| `lockbit-affiliates-ofac-2024` | `empirical_case` | `S1_ofac_sdn` | `comparison` | `ofac_sdn_designation` | `day` | `address_set` | `complete` | 1 | `asset_only` | · | · | `2026-04-22` | `—` |
| `lockbit-leader-ofac-2024` | `null_case` | `S1_ofac_sdn` | `null_event` | `ofac_sdn_designation` | `day` | `address_set` | `complete` | 0 | `null_event` | · | · | `2026-04-22` | `—` |
| `matveev-ofac-2023` | `null_case` | `S1_ofac_sdn` | `null_event` | `ofac_sdn_designation` | `day` | `entity` | `subset` | 0 | `null_event` | · | · | `2026-04-22` | `—` |
| `nigeria-cbn-crypto-ban-2021` | `empirical_case` | `S4_nation_state` | `comparison` | `nation_state_block` | `day` | `entity` | `subset` | 1 | `cex_only` | · | · | `2026-04-22` | `—` |
| `pertsev-nl-arrest-2022` | `null_case` | `S3_doj_sec_cftc_fiod` | `null_event` | `doj_indictment` | `day` | `entity` | `complete` | 0 | `null_event` | · | · | `2026-04-22` | `—` |
| `russia-election-interference-ofac-2020` | `empirical_case` | `S1_ofac_sdn` | `comparison` | `ofac_sdn_designation` | `day` | `address_set` | `complete` | 1 | `asset_only` | · | · | `2026-04-22` | `—` |
| `russian-cyber-theft-ofac-2020` | `empirical_case` | `S1_ofac_sdn` | `comparison` | `ofac_sdn_designation` | `day` | `address_set` | `complete` | 1 | `asset_only` | · | · | `2026-04-22` | `—` |
| `russian-cybercrime-infra-ofac-2025` | `null_case` | `S1_ofac_sdn` | `null_event` | `ofac_sdn_designation` | `day` | `address_set` | `complete` | 0 | `null_event` | · | · | `2026-04-22` | `—` |
| `samourai-doj-2024` | `empirical_case` | `S3_doj_sec_cftc_fiod` | `comparison` | `doj_indictment` | `day` | `entity` | `subset` | 1 | `frontend_only` | · | · | `2026-04-22` | `—` |
| `sec-v-binance-2023` | `anchor_case` | `S3_doj_sec_cftc_fiod` | `comparison` | `sec_action` | `day` | `entity` | `subset` | 2 | `multi_layer` | · | · | `2026-04-22` | `—` |
| `sec-v-coinbase-2023` | `empirical_case` | `S3_doj_sec_cftc_fiod` | `comparison` | `sec_action` | `day` | `entity` | `subset` | 1 | `cex_only` | · | · | `2026-04-22` | `—` |
| `sec-v-uniswap-wells-notice-2024` | `null_case` | `S3_doj_sec_cftc_fiod` | `null_event` | `sec_action` | `day` | `entity` | `complete` | 0 | `null_event` | · | · | `2026-04-22` | `—` |
| `semenov-ofac-2023` | `empirical_case` | `S1_ofac_sdn` | `comparison` | `ofac_sdn_designation` | `day` | `address_set` | `complete` | 1 | `asset_only` | · | · | `2026-04-21` | `2026-04-22` |
| `sichuan-silence-ofac-2024` | `null_case` | `S1_ofac_sdn` | `null_event` | `ofac_sdn_designation` | `day` | `entity` | `subset` | 0 | `null_event` | · | · | `2026-04-22` | `—` |
| `sinbad-ofac-2023` | `null_case` | `S1_ofac_sdn` | `null_event` | `ofac_sdn_designation` | `day` | `address_set` | `complete` | 0 | `null_event` | · | · | `2026-04-21` | `—` |
| `storm-semenov-doj-2023` | `null_case` | `S3_doj_sec_cftc_fiod` | `null_event` | `doj_indictment` | `day` | `entity` | `complete` | 0 | `null_event` | · | · | `2026-04-22` | `—` |
| `suex-ofac-2021` | `empirical_case` | `S1_ofac_sdn` | `comparison` | `ofac_sdn_designation` | `day` | `address_set` | `complete` | 1 | `asset_only` | · | · | `2026-04-21` | `—` |
| `tether-doj-pig-butchering-freeze-2023` | `empirical_case` | `S5_corporate` | `comparison` | `corporate_policy_change` | `day` | `entity` | `subset` | 1 | `cex_only` | ✓ | · | `2026-04-22` | `—` |
| `tether-dprk-precommit-freeze-2025` | `empirical_case` | `S5_corporate` | `comparison` | `corporate_policy_change` | `hour` | `address_set` | `subset` | 1 | `asset_only` | ✓ | · | `2026-04-22` | `—` |
| `tether-retroactive-sweep-2023` | `empirical_case` | `S5_corporate` | `comparison` | `corporate_policy_change` | `hour` | `address_set` | `subset` | 1 | `asset_only` | ✓ | · | `2026-04-22` | `2026-04-22` |
| `tornado-cash-ofac-2022` | `anchor_case` | `S1_ofac_sdn` | `cascade` | `ofac_sdn_designation` | `hour` | `address_set` | `complete` | 5 | `multi_layer` | · | · | `2026-04-21` | `2026-04-22` |
| `tornado-cash-ofac-delisting-2025` | `anchor_case` | `S2_ofac_removal` | `cascade` | `ofac_sdn_removal` | `day` | `address_set` | `complete` | 4 | `multi_layer` | · | ✓ | `2026-04-21` | `—` |
| `tornado-cash-ofac-redesignation-2022` | `empirical_case` | `S1_ofac_sdn` | `comparison` | `ofac_sdn_designation` | `day` | `address_set` | `complete` | 1 | `asset_only` | · | · | `2026-04-21` | `2026-04-22` |
| `turkey-cbrt-crypto-ban-2021` | `empirical_case` | `S4_nation_state` | `comparison` | `nation_state_block` | `day` | `entity` | `subset` | 1 | `cex_only` | · | · | `2026-04-22` | `—` |
| `uniswap-frontend-delisting-2023` | `empirical_case` | `S5_corporate` | `comparison` | `corporate_policy_change` | `day` | `entity` | `subset` | 1 | `frontend_only` | ✓ | · | `2026-04-22` | `—` |
| `zservers-ofac-2025` | `null_case` | `S1_ofac_sdn` | `null_event` | `ofac_sdn_designation` | `day` | `address_set` | `complete` | 0 | `null_event` | · | · | `2026-04-22` | `—` |
