# Table 1 · Case roles (n=83)

Dataset snapshot: **v0.2.0-rc-dryrun-2** · cutoff `2026-05-16` · commit `c6bc9d9` · generated `2026-05-18T10:40:00Z`

Supports `docs/paper_claims.md §0` (case-role convention). Each event's admission tier determines how it may be cited: `anchor_case` = named in narrative and figures; `empirical_case` = aggregate-count contributor only; `null_case` = denominator for `observed_no_change` claims only.

## Summary

| admission_tier | count |
| --- | ---: |
| `anchor_case` | 2 |
| `empirical_case` | 69 |
| `null_case` | 12 |
| **total** | **83** |

| trigger precision bucket | count |
| --- | ---: |
| `hour` | 5 |
| `day` | 78 |

Only the `hour`-precision subset is admissible for hour-granularity latency claims (Table 4).

## Per-event rows

| event_id | tier | stratum | shape | trigger_type | prec | target_kind | target_enum | Δlayers | archetype | t=action | reversal | last_verified | last_audit |
| --- | --- | --- | --- | --- | --- | --- | --- | ---: | --- | :---: | :---: | --- | --- |
| `aeza-group-ofac-2025` | `empirical_case` | `S1_ofac_sdn` | `comparison` | `ofac_sdn_designation` | `day` | `entity` | `subset` | 1 | `asset_only` | · | · | `2026-04-22` | `—` |
| `alphabay-hansa-doj-2017` | `empirical_case` | `S3_doj_sec_cftc_fiod` | `comparison` | `doj_seizure_order` | `day` | `entity` | `subset` | 1 | `frontend_only` | · | · | `2026-05-16` | `2026-05-16` |
| `belgium-fsma-binance-cease-2023` | `empirical_case` | `S4_nation_state` | `comparison` | `nation_state_block` | `day` | `entity` | `subset` | 2 | `multi_layer` | · | · | `2026-05-16` | `2026-05-16` |
| `binance-4framework-2023` | `empirical_case` | `S3_doj_sec_cftc_fiod` | `comparison` | `doj_indictment` | `day` | `entity` | `subset` | 1 | `cex_only` | · | · | `2026-04-22` | `—` |
| `binance-russia-exit-commex-2023` | `empirical_case` | `S5_corporate` | `comparison` | `corporate_policy_change` | `day` | `entity` | `subset` | 2 | `multi_layer` | ✓ | · | `2026-05-16` | `2026-05-16` |
| `bitfinex-cftc-retail-commodity-2016` | `empirical_case` | `S3_doj_sec_cftc_fiod` | `comparison` | `cftc_action` | `day` | `entity` | `subset` | 1 | `cex_only` | · | · | `2026-05-16` | `2026-05-16` |
| `bitmex-cftc-doj-2020` | `empirical_case` | `S3_doj_sec_cftc_fiod` | `comparison` | `doj_indictment` | `day` | `entity` | `subset` | 2 | `multi_layer` | · | · | `2026-05-16` | `2026-05-16` |
| `bitzlato-doj-2023` | `empirical_case` | `S3_doj_sec_cftc_fiod` | `comparison` | `doj_indictment` | `day` | `entity` | `complete` | 1 | `cex_only` | · | · | `2026-04-21` | `—` |
| `blender-ofac-2022` | `empirical_case` | `S1_ofac_sdn` | `comparison` | `ofac_sdn_designation` | `day` | `address_set` | `complete` | 1 | `frontend_only` | · | · | `2026-04-21` | `—` |
| `blockfi-sec-lending-2022` | `empirical_case` | `S3_doj_sec_cftc_fiod` | `comparison` | `sec_action` | `day` | `entity` | `subset` | 1 | `cex_only` | · | · | `2026-05-16` | `2026-05-16` |
| `btc-e-doj-2017` | `empirical_case` | `S3_doj_sec_cftc_fiod` | `comparison` | `doj_indictment` | `day` | `entity` | `subset` | 1 | `frontend_only` | · | · | `2026-04-22` | `—` |
| `canada-convoy-freeze-2022` | `empirical_case` | `S4_nation_state` | `comparison` | `nation_state_block` | `day` | `entity` | `subset` | 1 | `cex_only` | · | · | `2026-04-22` | `—` |
| `canada-csa-binance-withdrawal-2023` | `empirical_case` | `S4_nation_state` | `comparison` | `nation_state_block` | `day` | `entity` | `subset` | 2 | `multi_layer` | · | · | `2026-05-16` | `2026-05-16` |
| `cftc-v-ooki-dao-2022` | `empirical_case` | `S3_doj_sec_cftc_fiod` | `comparison` | `cftc_action` | `day` | `entity` | `complete` | 1 | `frontend_only` | · | · | `2026-04-22` | `—` |
| `chatex-ofac-2021` | `empirical_case` | `S1_ofac_sdn` | `comparison` | `ofac_sdn_designation` | `day` | `address_set` | `complete` | 2 | `multi_layer` | · | · | `2026-04-22` | `—` |
| `china-pboc-crypto-ban-2013-12` | `empirical_case` | `S4_nation_state` | `comparison` | `nation_state_block` | `day` | `entity` | `subset` | 1 | `cex_only` | · | · | `2026-05-16` | `2026-05-16` |
| `china-pboc-crypto-ban-2021` | `empirical_case` | `S4_nation_state` | `comparison` | `nation_state_block` | `hour` | `entity` | `complete` | 1 | `cex_only` | · | · | `2026-04-21` | `—` |
| `chipmixer-doj-2023` | `empirical_case` | `S3_doj_sec_cftc_fiod` | `comparison` | `doj_seizure_order` | `day` | `entity` | `subset` | 1 | `frontend_only` | · | · | `2026-04-22` | `—` |
| `circle-usdc-tornado-2022` | `empirical_case` | `S5_corporate` | `comparison` | `corporate_policy_change` | `hour` | `address_set` | `subset` | 1 | `asset_only` | ✓ | · | `2026-04-22` | `—` |
| `coinbase-india-exit-2022` | `empirical_case` | `S5_corporate` | `comparison` | `corporate_policy_change` | `day` | `domain` | `complete` | 1 | `cex_only` | · | · | `2026-04-22` | `—` |
| `coinbase-irs-john-doe-summons-2016` | `empirical_case` | `S3_doj_sec_cftc_fiod` | `comparison` | `court_civil_order` | `day` | `entity` | `complete` | 1 | `cex_only` | · | · | `2026-05-16` | `2026-05-16` |
| `coinflip-cftc-derivabit-2015` | `empirical_case` | `S3_doj_sec_cftc_fiod` | `comparison` | `cftc_action` | `day` | `entity` | `complete` | 1 | `frontend_only` | · | · | `2026-05-16` | `2026-05-16` |
| `cryptex-ofac-2024` | `anchor_case` | `S1_ofac_sdn` | `comparison` | `ofac_sdn_designation` | `day` | `address_set` | `complete` | 2 | `multi_layer` | · | · | `2026-04-21` | `2026-04-22` |
| `dprk-usdt-network-ofac-2025` | `empirical_case` | `S1_ofac_sdn` | `comparison` | `ofac_sdn_designation` | `day` | `address_set` | `complete` | 1 | `asset_only` | · | · | `2026-04-22` | `—` |
| `eu-12th-russia-sanctions-2023` | `empirical_case` | `S6_supranational` | `comparison` | `non_us_sanctions` | `day` | `entity` | `subset` | 1 | `cex_only` | · | · | `2026-04-22` | `—` |
| `eu-mica-2023` | `empirical_case` | `S6_supranational` | `comparison` | `supranational_regulation` | `day` | `entity` | `subset` | 1 | `cex_only` | · | · | `2026-04-22` | `—` |
| `eu-russia-crypto-wallet-cap-2022` | `empirical_case` | `S6_supranational` | `comparison` | `non_us_sanctions` | `day` | `entity` | `subset` | 1 | `cex_only` | · | · | `2026-05-16` | `2026-05-16` |
| `eu-russia-full-crypto-wallet-ban-2022` | `empirical_case` | `S6_supranational` | `comparison` | `non_us_sanctions` | `day` | `entity` | `subset` | 1 | `cex_only` | · | · | `2026-05-16` | `2026-05-16` |
| `funnull-cdn-ofac-2025` | `empirical_case` | `S1_ofac_sdn` | `comparison` | `ofac_sdn_designation` | `day` | `entity` | `subset` | 1 | `asset_only` | · | · | `2026-04-22` | `—` |
| `garantex-ofac-2022` | `empirical_case` | `S1_ofac_sdn` | `comparison` | `ofac_sdn_designation` | `day` | `entity` | `complete` | 1 | `cex_only` | · | · | `2026-04-21` | `—` |
| `grinex-garantex-successor-ofac-2025` | `empirical_case` | `S1_ofac_sdn` | `comparison` | `ofac_sdn_designation` | `day` | `address_set` | `complete` | 1 | `asset_only` | · | · | `2026-04-21` | `—` |
| `helix-doj-mixer-2020` | `empirical_case` | `S3_doj_sec_cftc_fiod` | `comparison` | `doj_indictment` | `day` | `entity` | `subset` | 2 | `multi_layer` | · | · | `2026-05-16` | `2026-05-16` |
| `hydra-doj-2022` | `empirical_case` | `S3_doj_sec_cftc_fiod` | `comparison` | `doj_seizure_order` | `day` | `entity` | `subset` | 1 | `frontend_only` | · | · | `2026-04-22` | `—` |
| `hydra-ofac-2022` | `empirical_case` | `S1_ofac_sdn` | `comparison` | `ofac_sdn_designation` | `day` | `entity` | `complete` | 1 | `frontend_only` | · | · | `2026-04-21` | `—` |
| `india-fiu-offshore-vda-block-2023` | `empirical_case` | `S4_nation_state` | `comparison` | `nation_state_block` | `day` | `entity` | `subset` | 2 | `multi_layer` | · | · | `2026-05-16` | `2026-05-16` |
| `india-rbi-crypto-ban-2018` | `empirical_case` | `S4_nation_state` | `comparison` | `nation_state_block` | `day` | `entity` | `subset` | 1 | `cex_only` | · | · | `2026-04-22` | `—` |
| `iran-ransomware-ofac-2018` | `null_case` | `S1_ofac_sdn` | `null_event` | `ofac_sdn_designation` | `day` | `address_set` | `complete` | 0 | `null_event` | · | · | `2026-04-22` | `2026-05-15` |
| `irgc-ransomware-ofac-2022` | `null_case` | `S1_ofac_sdn` | `null_event` | `ofac_sdn_designation` | `day` | `address_set` | `complete` | 0 | `null_event` | · | · | `2026-04-22` | `2026-05-15` |
| `korea-travel-rule-2022` | `empirical_case` | `S4_nation_state` | `comparison` | `nation_state_block` | `day` | `entity` | `subset` | 1 | `cex_only` | · | · | `2026-04-22` | `—` |
| `kraken-sec-staking-2023` | `empirical_case` | `S3_doj_sec_cftc_fiod` | `comparison` | `sec_action` | `day` | `entity` | `subset` | 1 | `cex_only` | · | · | `2026-05-16` | `2026-05-16` |
| `kucoin-doj-2024` | `empirical_case` | `S3_doj_sec_cftc_fiod` | `comparison` | `doj_indictment` | `day` | `entity` | `subset` | 2 | `multi_layer` | · | · | `2026-05-16` | `2026-05-16` |
| `lazarus-entity-ofac-2019` | `null_case` | `S1_ofac_sdn` | `null_event` | `ofac_sdn_designation` | `day` | `entity` | `subset` | 0 | `null_event` | · | · | `2026-04-22` | `2026-05-15` |
| `lazarus-laundering-ofac-2020` | `null_case` | `S1_ofac_sdn` | `null_event` | `ofac_sdn_designation` | `day` | `address_set` | `complete` | 0 | `null_event` | · | · | `2026-04-22` | `2026-05-15` |
| `lockbit-affiliates-ofac-2024` | `empirical_case` | `S1_ofac_sdn` | `comparison` | `ofac_sdn_designation` | `day` | `address_set` | `complete` | 1 | `asset_only` | · | · | `2026-04-22` | `—` |
| `lockbit-leader-ofac-2024` | `null_case` | `S1_ofac_sdn` | `null_event` | `ofac_sdn_designation` | `day` | `address_set` | `complete` | 0 | `null_event` | · | · | `2026-04-22` | `2026-05-15` |
| `malaysia-sc-binance-disable-2021` | `empirical_case` | `S4_nation_state` | `comparison` | `nation_state_block` | `day` | `entity` | `subset` | 2 | `multi_layer` | · | · | `2026-05-16` | `2026-05-16` |
| `matveev-ofac-2023` | `null_case` | `S1_ofac_sdn` | `null_event` | `ofac_sdn_designation` | `day` | `entity` | `subset` | 0 | `null_event` | · | · | `2026-04-22` | `2026-05-15` |
| `netherlands-dnb-binance-warning-2021` | `empirical_case` | `S4_nation_state` | `comparison` | `nation_state_block` | `day` | `entity` | `subset` | 2 | `multi_layer` | · | · | `2026-05-16` | `2026-05-16` |
| `nigeria-cbn-crypto-ban-2021` | `empirical_case` | `S4_nation_state` | `comparison` | `nation_state_block` | `day` | `entity` | `subset` | 1 | `cex_only` | · | · | `2026-04-22` | `—` |
| `nydfs-bitlicense-2015-06` | `empirical_case` | `S3_doj_sec_cftc_fiod` | `comparison` | `court_civil_order` | `day` | `entity` | `subset` | 1 | `frontend_only` | · | · | `2026-05-16` | `2026-05-16` |
| `okx-privacy-token-delist-2024` | `empirical_case` | `S5_corporate` | `comparison` | `corporate_policy_change` | `day` | `asset` | `subset` | 1 | `cex_only` | ✓ | · | `2026-05-16` | `2026-05-16` |
| `pertsev-nl-arrest-2022` | `null_case` | `S3_doj_sec_cftc_fiod` | `null_event` | `doj_indictment` | `day` | `entity` | `complete` | 0 | `null_event` | · | · | `2026-04-22` | `2026-05-15` |
| `powell-unlicensed-bitcoin-exchange-2014` | `empirical_case` | `S3_doj_sec_cftc_fiod` | `comparison` | `doj_indictment` | `day` | `entity` | `subset` | 1 | `cex_only` | · | · | `2026-05-16` | `2026-05-16` |
| `ripple-fincen-xrp-2015` | `empirical_case` | `S3_doj_sec_cftc_fiod` | `comparison` | `fincen_action` | `day` | `entity` | `complete` | 1 | `cex_only` | · | · | `2026-05-16` | `2026-05-16` |
| `russia-election-interference-ofac-2020` | `empirical_case` | `S1_ofac_sdn` | `comparison` | `ofac_sdn_designation` | `day` | `address_set` | `complete` | 1 | `asset_only` | · | · | `2026-04-22` | `—` |
| `russian-cyber-theft-ofac-2020` | `empirical_case` | `S1_ofac_sdn` | `comparison` | `ofac_sdn_designation` | `day` | `address_set` | `complete` | 1 | `asset_only` | · | · | `2026-04-22` | `—` |
| `russian-cybercrime-infra-ofac-2025` | `null_case` | `S1_ofac_sdn` | `null_event` | `ofac_sdn_designation` | `day` | `address_set` | `complete` | 0 | `null_event` | · | · | `2026-04-22` | `2026-05-15` |
| `samourai-doj-2024` | `empirical_case` | `S3_doj_sec_cftc_fiod` | `comparison` | `doj_indictment` | `day` | `entity` | `subset` | 1 | `frontend_only` | · | · | `2026-04-22` | `—` |
| `sec-beaxy-platform-shutdown-2023` | `empirical_case` | `S3_doj_sec_cftc_fiod` | `comparison` | `sec_action` | `day` | `entity` | `subset` | 2 | `multi_layer` | · | · | `2026-05-16` | `2026-05-16` |
| `sec-burnside-bitcoin-stock-exchange-2014` | `empirical_case` | `S3_doj_sec_cftc_fiod` | `comparison` | `sec_action` | `day` | `entity` | `subset` | 2 | `multi_layer` | · | · | `2026-05-16` | `2026-05-16` |
| `sec-shavers-btcst-2013` | `empirical_case` | `S3_doj_sec_cftc_fiod` | `comparison` | `sec_action` | `day` | `entity` | `subset` | 1 | `cex_only` | · | · | `2026-05-16` | `2026-05-16` |
| `sec-v-binance-2023` | `empirical_case` | `S3_doj_sec_cftc_fiod` | `comparison` | `sec_action` | `day` | `entity` | `complete` | 1 | `cex_only` | · | · | `2026-05-06` | `2026-05-06` |
| `sec-v-coinbase-2023` | `empirical_case` | `S3_doj_sec_cftc_fiod` | `comparison` | `sec_action` | `day` | `entity` | `complete` | 1 | `cex_only` | · | · | `2026-05-06` | `2026-05-06` |
| `sec-voorhees-satoshidice-2014` | `empirical_case` | `S3_doj_sec_cftc_fiod` | `comparison` | `sec_action` | `day` | `entity` | `subset` | 2 | `multi_layer` | · | · | `2026-05-16` | `2026-05-16` |
| `semenov-ofac-2023` | `empirical_case` | `S1_ofac_sdn` | `comparison` | `ofac_sdn_designation` | `day` | `address_set` | `complete` | 1 | `asset_only` | · | · | `2026-04-21` | `2026-04-22` |
| `shrem-faiella-bitcoin-exchange-2014` | `empirical_case` | `S3_doj_sec_cftc_fiod` | `comparison` | `doj_indictment` | `day` | `entity` | `subset` | 1 | `cex_only` | · | · | `2026-05-16` | `2026-05-16` |
| `sichuan-silence-ofac-2024` | `null_case` | `S1_ofac_sdn` | `null_event` | `ofac_sdn_designation` | `day` | `entity` | `subset` | 0 | `null_event` | · | · | `2026-04-22` | `2026-05-15` |
| `silk-road-doj-seizure-2013` | `empirical_case` | `S3_doj_sec_cftc_fiod` | `comparison` | `doj_seizure_order` | `day` | `domain` | `subset` | 1 | `frontend_only` | · | · | `2026-05-16` | `2026-05-16` |
| `sinbad-ofac-2023` | `null_case` | `S1_ofac_sdn` | `null_event` | `ofac_sdn_designation` | `day` | `address_set` | `complete` | 0 | `null_event` | · | · | `2026-04-21` | `2026-05-15` |
| `singapore-mas-binance-services-2021` | `empirical_case` | `S4_nation_state` | `comparison` | `nation_state_block` | `day` | `entity` | `subset` | 2 | `multi_layer` | · | · | `2026-05-16` | `2026-05-16` |
| `storm-semenov-doj-2023` | `null_case` | `S3_doj_sec_cftc_fiod` | `null_event` | `doj_indictment` | `day` | `entity` | `complete` | 0 | `null_event` | · | · | `2026-04-22` | `2026-05-15` |
| `suex-ofac-2021` | `empirical_case` | `S1_ofac_sdn` | `comparison` | `ofac_sdn_designation` | `day` | `address_set` | `complete` | 1 | `asset_only` | · | · | `2026-04-21` | `—` |
| `teraexchange-cftc-bitcoin-swap-2015` | `empirical_case` | `S3_doj_sec_cftc_fiod` | `comparison` | `cftc_action` | `day` | `entity` | `complete` | 1 | `cex_only` | · | · | `2026-05-16` | `2026-05-16` |
| `tether-doj-pig-butchering-freeze-2023` | `empirical_case` | `S5_corporate` | `comparison` | `corporate_policy_change` | `day` | `entity` | `subset` | 1 | `cex_only` | ✓ | · | `2026-04-22` | `—` |
| `tether-dprk-precommit-freeze-2025` | `empirical_case` | `S5_corporate` | `comparison` | `corporate_policy_change` | `hour` | `address_set` | `subset` | 1 | `asset_only` | ✓ | · | `2026-04-22` | `—` |
| `tether-retroactive-sweep-2023` | `empirical_case` | `S5_corporate` | `comparison` | `corporate_policy_change` | `hour` | `address_set` | `subset` | 1 | `asset_only` | ✓ | · | `2026-04-22` | `2026-04-22` |
| `tornado-cash-ofac-2022` | `anchor_case` | `S1_ofac_sdn` | `cascade` | `ofac_sdn_designation` | `hour` | `address_set` | `complete` | 5 | `multi_layer` | · | · | `2026-04-21` | `2026-04-22` |
| `tornado-cash-ofac-delisting-2025` | `empirical_case` | `S2_ofac_removal` | `cascade` | `ofac_sdn_removal` | `day` | `address_set` | `complete` | 4 | `multi_layer` | · | ✓ | `2026-04-21` | `—` |
| `tornado-cash-ofac-redesignation-2022` | `empirical_case` | `S1_ofac_sdn` | `comparison` | `ofac_sdn_designation` | `day` | `address_set` | `complete` | 1 | `asset_only` | · | · | `2026-04-21` | `2026-04-22` |
| `turkey-cbrt-crypto-ban-2021` | `empirical_case` | `S4_nation_state` | `comparison` | `nation_state_block` | `day` | `entity` | `subset` | 1 | `cex_only` | · | · | `2026-04-22` | `—` |
| `uk-fca-binance-markets-2021` | `empirical_case` | `S4_nation_state` | `comparison` | `nation_state_block` | `day` | `entity` | `subset` | 2 | `multi_layer` | · | · | `2026-05-16` | `—` |
| `uniswap-frontend-delisting-2023` | `empirical_case` | `S5_corporate` | `comparison` | `corporate_policy_change` | `day` | `entity` | `subset` | 1 | `frontend_only` | ✓ | · | `2026-04-22` | `—` |
| `zservers-ofac-2025` | `null_case` | `S1_ofac_sdn` | `null_event` | `ofac_sdn_designation` | `day` | `address_set` | `complete` | 0 | `null_event` | · | · | `2026-04-22` | `2026-05-15` |
