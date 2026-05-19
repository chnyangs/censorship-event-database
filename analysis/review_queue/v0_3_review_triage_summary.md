# v0.3 Review Triage Summary

This is a pre-human LLM/machine triage artifact. It does not constitute human audit, primary-source verification, or release approval.

## Queue State

| State | Count | Meaning |
| --- | ---: | --- |
| `llm_prescreen_no_machine_blocker` | 39 | No machine blocker detected; awaiting human primary-source confirmation. |
| `llm_prescreen_repaired_awaiting_human_audit` | 196 | Earlier LLM flag now has no current machine blocker after evidence repair; awaiting human confirmation. |
| `llm_prescreen_before_human_audit` | 2 | LLM/machine flagged missing anchors or sources before human audit; repair evidence before confirmation. |
| `human_review_recorded` | 25 | A non-agent review decision is already recorded in the local audit log. |

No event was promoted, no human audit was recorded, and no `primary_source_verified` flag was changed by this triage.

## Pending Human Confirmation

| queue_id | bucket | event_id | packet |
| ---: | --- | --- | --- |
| 5 | `legacy_admitted_primary_source_recheck` | `alphabay-hansa-doj-2017` | [packet](packets/0005-alphabay-hansa-doj-2017.md) |
| 13 | `legacy_admitted_primary_source_recheck` | `binance-4framework-2023` | [packet](packets/0013-binance-4framework-2023.md) |
| 26 | `legacy_admitted_primary_source_recheck` | `bitzlato-doj-2023` | [packet](packets/0026-bitzlato-doj-2023.md) |
| 28 | `legacy_admitted_primary_source_recheck` | `blockfi-sec-lending-2022` | [packet](packets/0028-blockfi-sec-lending-2022.md) |
| 32 | `legacy_admitted_primary_source_recheck` | `btc-e-doj-2017` | [packet](packets/0032-btc-e-doj-2017.md) |
| 34 | `legacy_admitted_primary_source_recheck` | `canada-convoy-freeze-2022` | [packet](packets/0034-canada-convoy-freeze-2022.md) |
| 38 | `legacy_admitted_primary_source_recheck` | `cftc-v-ooki-dao-2022` | [packet](packets/0038-cftc-v-ooki-dao-2022.md) |
| 44 | `legacy_admitted_primary_source_recheck` | `china-pboc-crypto-ban-2021` | [packet](packets/0044-china-pboc-crypto-ban-2021.md) |
| 49 | `legacy_admitted_primary_source_recheck` | `chipmixer-doj-2023` | [packet](packets/0049-chipmixer-doj-2023.md) |
| 52 | `legacy_admitted_primary_source_recheck` | `circle-usdc-tornado-2022` | [packet](packets/0052-circle-usdc-tornado-2022.md) |
| 55 | `legacy_admitted_primary_source_recheck` | `coinbase-india-exit-2022` | [packet](packets/0055-coinbase-india-exit-2022.md) |
| 56 | `legacy_admitted_primary_source_recheck` | `coinbase-irs-john-doe-summons-2016` | [packet](packets/0056-coinbase-irs-john-doe-summons-2016.md) |
| 60 | `legacy_admitted_primary_source_recheck` | `cryptex-ofac-2024` | [packet](packets/0060-cryptex-ofac-2024.md) |
| 69 | `legacy_admitted_primary_source_recheck` | `eu-12th-russia-sanctions-2023` | [packet](packets/0069-eu-12th-russia-sanctions-2023.md) |
| 76 | `legacy_admitted_primary_source_recheck` | `eu-mica-2023` | [packet](packets/0076-eu-mica-2023.md) |
| 104 | `legacy_admitted_primary_source_recheck` | `hydra-doj-2022` | [packet](packets/0104-hydra-doj-2022.md) |
| 108 | `legacy_admitted_primary_source_recheck` | `india-rbi-crypto-ban-2018` | [packet](packets/0108-india-rbi-crypto-ban-2018.md) |
| 133 | `legacy_admitted_primary_source_recheck` | `korea-travel-rule-2022` | [packet](packets/0133-korea-travel-rule-2022.md) |
| 135 | `legacy_admitted_primary_source_recheck` | `kraken-sec-staking-2023` | [packet](packets/0135-kraken-sec-staking-2023.md) |
| 159 | `legacy_admitted_primary_source_recheck` | `nigeria-cbn-crypto-ban-2021` | [packet](packets/0159-nigeria-cbn-crypto-ban-2021.md) |
| 160 | `legacy_admitted_primary_source_recheck` | `nydfs-bitlicense-2015-06` | [packet](packets/0160-nydfs-bitlicense-2015-06.md) |
| 177 | `legacy_admitted_primary_source_recheck` | `pertsev-nl-arrest-2022` | [packet](packets/0177-pertsev-nl-arrest-2022.md) |
| 181 | `legacy_admitted_primary_source_recheck` | `powell-unlicensed-bitcoin-exchange-2014` | [packet](packets/0181-powell-unlicensed-bitcoin-exchange-2014.md) |
| 184 | `legacy_admitted_primary_source_recheck` | `ripple-fincen-xrp-2015` | [packet](packets/0184-ripple-fincen-xrp-2015.md) |
| 195 | `legacy_admitted_primary_source_recheck` | `samourai-doj-2024` | [packet](packets/0195-samourai-doj-2024.md) |
| 196 | `legacy_admitted_primary_source_recheck` | `sec-beaxy-platform-shutdown-2023` | [packet](packets/0196-sec-beaxy-platform-shutdown-2023.md) |
| 200 | `legacy_admitted_primary_source_recheck` | `sec-v-binance-2023` | [packet](packets/0200-sec-v-binance-2023.md) |
| 201 | `legacy_admitted_primary_source_recheck` | `sec-v-bittrex-2023` | [packet](packets/0201-sec-v-bittrex-2023.md) |
| 202 | `legacy_admitted_primary_source_recheck` | `sec-v-coinbase-2023` | [packet](packets/0202-sec-v-coinbase-2023.md) |
| 212 | `legacy_admitted_primary_source_recheck` | `silk-road-doj-seizure-2013` | [packet](packets/0212-silk-road-doj-seizure-2013.md) |
| 218 | `legacy_admitted_primary_source_recheck` | `storm-semenov-doj-2023` | [packet](packets/0218-storm-semenov-doj-2023.md) |
| 221 | `legacy_admitted_primary_source_recheck` | `teraexchange-cftc-bitcoin-swap-2015` | [packet](packets/0221-teraexchange-cftc-bitcoin-swap-2015.md) |
| 222 | `legacy_admitted_primary_source_recheck` | `tether-doj-pig-butchering-freeze-2023` | [packet](packets/0222-tether-doj-pig-butchering-freeze-2023.md) |
| 223 | `legacy_admitted_primary_source_recheck` | `tether-dprk-precommit-freeze-2025` | [packet](packets/0223-tether-dprk-precommit-freeze-2025.md) |
| 225 | `legacy_admitted_primary_source_recheck` | `tether-retroactive-sweep-2023` | [packet](packets/0225-tether-retroactive-sweep-2023.md) |
| 231 | `legacy_admitted_primary_source_recheck` | `tornado-cash-ofac-2022` | [packet](packets/0231-tornado-cash-ofac-2022.md) |
| 238 | `legacy_admitted_primary_source_recheck` | `turkey-cbrt-crypto-ban-2021` | [packet](packets/0238-turkey-cbrt-crypto-ban-2021.md) |
| 246 | `legacy_admitted_primary_source_recheck` | `uniswap-frontend-delisting-2023` | [packet](packets/0246-uniswap-frontend-delisting-2023.md) |
| 207 | `legacy_rejected_reference_review` | `sec-v-uniswap-wells-notice-2024` | [packet](packets/0207-sec-v-uniswap-wells-notice-2024.md) |
| 10 | `legacy_admitted_primary_source_recheck` | `australia-asic-binance-derivatives-2023` | [packet](packets/0010-australia-asic-binance-derivatives-2023.md) |
| 12 | `legacy_admitted_primary_source_recheck` | `belgium-fsma-binance-cease-2023` | [packet](packets/0012-belgium-fsma-binance-cease-2023.md) |
| 15 | `legacy_admitted_primary_source_recheck` | `binance-cftc-2023` | [packet](packets/0015-binance-cftc-2023.md) |
| 16 | `legacy_admitted_primary_source_recheck` | `binance-privacy-coin-delisting-2023` | [packet](packets/0016-binance-privacy-coin-delisting-2023.md) |
| 17 | `legacy_admitted_primary_source_recheck` | `binance-russia-exit-commex-2023` | [packet](packets/0017-binance-russia-exit-commex-2023.md) |
| 18 | `legacy_admitted_primary_source_recheck` | `binance-us-staking-end-2023` | [packet](packets/0018-binance-us-staking-end-2023.md) |
| 20 | `legacy_admitted_primary_source_recheck` | `bitfinex-cftc-retail-commodity-2016` | [packet](packets/0020-bitfinex-cftc-retail-commodity-2016.md) |
| 21 | `legacy_admitted_primary_source_recheck` | `bitfinex-tether-cftc-2021` | [packet](packets/0021-bitfinex-tether-cftc-2021.md) |
| 23 | `legacy_admitted_primary_source_recheck` | `bitmex-cftc-doj-2020` | [packet](packets/0023-bitmex-cftc-doj-2020.md) |
| 35 | `legacy_admitted_primary_source_recheck` | `canada-csa-binance-withdrawal-2023` | [packet](packets/0035-canada-csa-binance-withdrawal-2023.md) |
| 36 | `legacy_admitted_primary_source_recheck` | `celsius-bankruptcy-mashinsky-doj-2023` | [packet](packets/0036-celsius-bankruptcy-mashinsky-doj-2023.md) |
| 43 | `legacy_admitted_primary_source_recheck` | `china-pboc-crypto-ban-2013-12` | [packet](packets/0043-china-pboc-crypto-ban-2013-12.md) |
| 58 | `legacy_admitted_primary_source_recheck` | `coinflip-cftc-derivabit-2015` | [packet](packets/0058-coinflip-cftc-derivabit-2015.md) |
| 77 | `legacy_admitted_primary_source_recheck` | `eu-russia-crypto-wallet-cap-2022` | [packet](packets/0077-eu-russia-crypto-wallet-cap-2022.md) |
| 78 | `legacy_admitted_primary_source_recheck` | `eu-russia-full-crypto-wallet-ban-2022` | [packet](packets/0078-eu-russia-full-crypto-wallet-ban-2022.md) |
| 79 | `legacy_admitted_primary_source_recheck` | `eu-tfr-recast-2023` | [packet](packets/0079-eu-tfr-recast-2023.md) |
| 81 | `legacy_admitted_primary_source_recheck` | `fatf-r15-vasp-travel-rule-2019` | [packet](packets/0081-fatf-r15-vasp-travel-rule-2019.md) |
| 89 | `legacy_admitted_primary_source_recheck` | `ftx-bankman-fried-doj-2022` | [packet](packets/0089-ftx-bankman-fried-doj-2022.md) |
| 94 | `legacy_admitted_primary_source_recheck` | `genesis-sec-gemini-earn-2023` | [packet](packets/0094-genesis-sec-gemini-earn-2023.md) |
| 95 | `legacy_admitted_primary_source_recheck` | `germany-bafin-binance-licence-withdrawal-2023` | [packet](packets/0095-germany-bafin-binance-licence-withdrawal-2023.md) |
| 98 | `legacy_admitted_primary_source_recheck` | `helix-doj-mixer-2020` | [packet](packets/0098-helix-doj-mixer-2020.md) |
| 107 | `legacy_admitted_primary_source_recheck` | `india-fiu-offshore-vda-block-2023` | [packet](packets/0107-india-fiu-offshore-vda-block-2023.md) |
| 111 | `legacy_admitted_primary_source_recheck` | `infura-alchemy-tornado-rpc-block-2022` | [packet](packets/0111-infura-alchemy-tornado-rpc-block-2022.md) |
| 120 | `legacy_admitted_primary_source_recheck` | `japan-fsa-coincheck-orders-2018` | [packet](packets/0120-japan-fsa-coincheck-orders-2018.md) |
| 131 | `legacy_admitted_primary_source_recheck` | `korea-fsc-ico-ban-2017` | [packet](packets/0131-korea-fsc-ico-ban-2017.md) |
| 136 | `legacy_admitted_primary_source_recheck` | `kraken-sec-unregistered-exchange-2023` | [packet](packets/0136-kraken-sec-unregistered-exchange-2023.md) |
| 139 | `legacy_admitted_primary_source_recheck` | `kucoin-doj-2024` | [packet](packets/0139-kucoin-doj-2024.md) |
| 147 | `legacy_admitted_primary_source_recheck` | `malaysia-sc-binance-disable-2021` | [packet](packets/0147-malaysia-sc-binance-disable-2021.md) |
| 158 | `legacy_admitted_primary_source_recheck` | `netherlands-dnb-binance-warning-2021` | [packet](packets/0158-netherlands-dnb-binance-warning-2021.md) |
| 163 | `legacy_admitted_primary_source_recheck` | `oecd-carf-2022` | [packet](packets/0163-oecd-carf-2022.md) |
| 173 | `legacy_admitted_primary_source_recheck` | `okx-privacy-token-delist-2024` | [packet](packets/0173-okx-privacy-token-delist-2024.md) |
| 197 | `legacy_admitted_primary_source_recheck` | `sec-burnside-bitcoin-stock-exchange-2014` | [packet](packets/0197-sec-burnside-bitcoin-stock-exchange-2014.md) |
| 199 | `legacy_admitted_primary_source_recheck` | `sec-shavers-btcst-2013` | [packet](packets/0199-sec-shavers-btcst-2013.md) |
| 205 | `legacy_admitted_primary_source_recheck` | `sec-v-ripple-2020` | [packet](packets/0205-sec-v-ripple-2020.md) |
| 206 | `legacy_admitted_primary_source_recheck` | `sec-v-telegram-ton-2020` | [packet](packets/0206-sec-v-telegram-ton-2020.md) |
| 208 | `legacy_admitted_primary_source_recheck` | `sec-voorhees-satoshidice-2014` | [packet](packets/0208-sec-voorhees-satoshidice-2014.md) |
| 210 | `legacy_admitted_primary_source_recheck` | `shrem-faiella-bitcoin-exchange-2014` | [packet](packets/0210-shrem-faiella-bitcoin-exchange-2014.md) |
| 213 | `legacy_admitted_primary_source_recheck` | `sinbad-doj-2024` | [packet](packets/0213-sinbad-doj-2024.md) |
| 215 | `legacy_admitted_primary_source_recheck` | `singapore-mas-binance-services-2021` | [packet](packets/0215-singapore-mas-binance-services-2021.md) |
| 235 | `legacy_admitted_primary_source_recheck` | `tornado-cash-storm-conviction-2025` | [packet](packets/0235-tornado-cash-storm-conviction-2025.md) |
| 241 | `legacy_admitted_primary_source_recheck` | `uk-fca-binance-markets-2021` | [packet](packets/0241-uk-fca-binance-markets-2021.md) |
| 252 | `legacy_admitted_primary_source_recheck` | `welcome-to-video-doj-2019` | [packet](packets/0252-welcome-to-video-doj-2019.md) |
| 1 | `legacy_draft_promotion_review` | `1inch-us-geofence-2021-09` | [packet](packets/0001-1inch-us-geofence-2021-09.md) |
| 2 | `legacy_draft_promotion_review` | `aave-arc-fireblocks-whitelist-2022-01` | [packet](packets/0002-aave-arc-fireblocks-whitelist-2022-01.md) |
| 3 | `legacy_draft_promotion_review` | `aave-tornado-frontend-block-2022-08` | [packet](packets/0003-aave-tornado-frontend-block-2022-08.md) |
| 6 | `legacy_draft_promotion_review` | `apple-india-crypto-exchange-removal-2024-01` | [packet](packets/0006-apple-india-crypto-exchange-removal-2024-01.md) |
| 7 | `legacy_draft_promotion_review` | `argentina-cnv-psav-registration-2024` | [packet](packets/0007-argentina-cnv-psav-registration-2024.md) |
| 8 | `legacy_draft_promotion_review` | `argentina-uif-resolution-300-2014` | [packet](packets/0008-argentina-uif-resolution-300-2014.md) |
| 9 | `legacy_draft_promotion_review` | `augur-v2-us-uk-geofence-2020-07` | [packet](packets/0009-augur-v2-us-uk-geofence-2020-07.md) |
| 11 | `legacy_draft_promotion_review` | `bangladesh-bb-bitcoin-warning-2014` | [packet](packets/0011-bangladesh-bb-bitcoin-warning-2014.md) |
| 14 | `legacy_draft_promotion_review` | `binance-busd-wind-down-2024` | [packet](packets/0014-binance-busd-wind-down-2024.md) |
| 19 | `legacy_draft_promotion_review` | `bitcoinica-shutdown-2012-05` | [packet](packets/0019-bitcoinica-shutdown-2012-05.md) |
| 22 | `legacy_draft_promotion_review` | `bitfinex-tether-nyag-2021` | [packet](packets/0022-bitfinex-tether-nyag-2021.md) |
| 24 | `legacy_draft_promotion_review` | `bitmex-fincen-2024` | [packet](packets/0024-bitmex-fincen-2024.md) |
| 25 | `legacy_draft_promotion_review` | `bitstamp-greece-portugal-exit-2023` | [packet](packets/0025-bitstamp-greece-portugal-exit-2023.md) |
| 29 | `legacy_draft_promotion_review` | `bolivia-bcb-crypto-prohibition-2014` | [packet](packets/0029-bolivia-bcb-crypto-prohibition-2014.md) |
| 30 | `legacy_draft_promotion_review` | `brazil-bacen-stablecoin-restriction-2023` | [packet](packets/0030-brazil-bacen-stablecoin-restriction-2023.md) |
| 31 | `legacy_draft_promotion_review` | `brazil-bcb-comunicado-25306-2014` | [packet](packets/0031-brazil-bcb-comunicado-25306-2014.md) |
| 33 | `legacy_draft_promotion_review` | `bybit-singapore-exit-2022` | [packet](packets/0033-bybit-singapore-exit-2022.md) |
| 37 | `legacy_draft_promotion_review` | `cftc-v-ftx-2022` | [packet](packets/0037-cftc-v-ftx-2022.md) |
| 40 | `legacy_draft_promotion_review` | `china-ico-ban-2017-09` | [packet](packets/0040-china-ico-ban-2017-09.md) |
| 41 | `legacy_draft_promotion_review` | `china-inner-mongolia-mining-ban-2021-05` | [packet](packets/0041-china-inner-mongolia-mining-ban-2021-05.md) |
| 45 | `legacy_draft_promotion_review` | `china-pboc-exchange-shutdown-2017-09` | [packet](packets/0045-china-pboc-exchange-shutdown-2017-09.md) |
| 46 | `legacy_draft_promotion_review` | `china-sichuan-mining-ban-2021-06` | [packet](packets/0046-china-sichuan-mining-ban-2021-06.md) |
| 47 | `legacy_draft_promotion_review` | `china-state-council-mining-crackdown-2021-05` | [packet](packets/0047-china-state-council-mining-crackdown-2021-05.md) |
| 50 | `legacy_draft_promotion_review` | `circle-usdc-cryptex-freeze-2024` | [packet](packets/0050-circle-usdc-cryptex-freeze-2024.md) |
| 51 | `legacy_draft_promotion_review` | `circle-usdc-svb-policy-statement-2023` | [packet](packets/0051-circle-usdc-svb-policy-statement-2023.md) |
| 53 | `legacy_draft_promotion_review` | `cloudflare-ethereum-gateway-tornado-block-2022-08` | [packet](packets/0053-cloudflare-ethereum-gateway-tornado-block-2022-08.md) |
| 54 | `legacy_draft_promotion_review` | `coin-mx-doj-murgio-2015` | [packet](packets/0054-coin-mx-doj-murgio-2015.md) |
| 57 | `legacy_draft_promotion_review` | `coinbase-japan-exit-2023` | [packet](packets/0057-coinbase-japan-exit-2023.md) |
| 59 | `legacy_draft_promotion_review` | `consensys-metamask-infura-rpc-data-collection-2022-11` | [packet](packets/0059-consensys-metamask-infura-rpc-data-collection-2022-11.md) |
| 61 | `legacy_draft_promotion_review` | `datacell-v-valitor-iceland-district-court-2012-07` | [packet](packets/0061-datacell-v-valitor-iceland-district-court-2012-07.md) |
| 63 | `legacy_draft_promotion_review` | `dydx-tornado-account-block-2022-08` | [packet](packets/0063-dydx-tornado-account-block-2022-08.md) |
| 64 | `legacy_draft_promotion_review` | `eba-virtual-currencies-opinion-eba-op-2014-08` | [packet](packets/0064-eba-virtual-currencies-opinion-eba-op-2014-08.md) |
| 65 | `legacy_draft_promotion_review` | `ebullion-doj-fbi-seizure-2008-08` | [packet](packets/0065-ebullion-doj-fbi-seizure-2008-08.md) |
| 66 | `legacy_draft_promotion_review` | `egold-doj-guilty-plea-2008-07` | [packet](packets/0066-egold-doj-guilty-plea-2008-07.md) |
| 67 | `legacy_draft_promotion_review` | `ens-eth-domain-tornado-resolution-2022` | [packet](packets/0067-ens-eth-domain-tornado-resolution-2022.md) |
| 68 | `legacy_draft_promotion_review` | `etherscan-tornado-cash-ui-label-2022` | [packet](packets/0068-etherscan-tornado-cash-ui-label-2022.md) |
| 70 | `legacy_draft_promotion_review` | `eu-14th-russia-sanctions-spfs-2024` | [packet](packets/0070-eu-14th-russia-sanctions-spfs-2024.md) |
| 71 | `legacy_draft_promotion_review` | `eu-15th-russia-sanctions-2024` | [packet](packets/0071-eu-15th-russia-sanctions-2024.md) |
| 72 | `legacy_draft_promotion_review` | `eu-amla-anti-money-laundering-authority-regulation-2024` | [packet](packets/0072-eu-amla-anti-money-laundering-authority-regulation-2024.md) |
| 73 | `legacy_draft_promotion_review` | `eu-amlr-eu-single-rulebook-2024` | [packet](packets/0073-eu-amlr-eu-single-rulebook-2024.md) |
| 74 | `legacy_draft_promotion_review` | `eu-belarus-crypto-services-ban-2022` | [packet](packets/0074-eu-belarus-crypto-services-ban-2022.md) |
| 75 | `legacy_draft_promotion_review` | `eu-dac8-crypto-asset-reporting-directive-2023` | [packet](packets/0075-eu-dac8-crypto-asset-reporting-directive-2023.md) |
| 80 | `legacy_draft_promotion_review` | `fatf-grey-list-crypto-related-actions-2023-2024` | [packet](packets/0080-fatf-grey-list-crypto-related-actions-2023-2024.md) |
| 82 | `legacy_draft_promotion_review` | `fatf-targeted-update-va-vasp-2021` | [packet](packets/0082-fatf-targeted-update-va-vasp-2021.md) |
| 83 | `legacy_draft_promotion_review` | `fatf-targeted-update-va-vasp-2023` | [packet](packets/0083-fatf-targeted-update-va-vasp-2023.md) |
| 84 | `legacy_draft_promotion_review` | `fatf-virtual-currencies-key-definitions-2014` | [packet](packets/0084-fatf-virtual-currencies-key-definitions-2014.md) |
| 85 | `legacy_draft_promotion_review` | `fbi-bitcoin-intelligence-assessment-2012-04` | [packet](packets/0085-fbi-bitcoin-intelligence-assessment-2012-04.md) |
| 86 | `legacy_draft_promotion_review` | `fincen-virtual-currency-msb-guidance-2013` | [packet](packets/0086-fincen-virtual-currency-msb-guidance-2013.md) |
| 87 | `legacy_draft_promotion_review` | `france-amf-binance-psan-2022` | [packet](packets/0087-france-amf-binance-psan-2022.md) |
| 88 | `legacy_draft_promotion_review` | `fsb-crypto-asset-recommendations-2023` | [packet](packets/0088-fsb-crypto-asset-recommendations-2023.md) |
| 91 | `legacy_draft_promotion_review` | `g20-roadmap-crypto-asset-policy-2023` | [packet](packets/0091-g20-roadmap-crypto-asset-policy-2023.md) |
| 92 | `legacy_draft_promotion_review` | `g7-hiroshima-crypto-statement-2023` | [packet](packets/0092-g7-hiroshima-crypto-statement-2023.md) |
| 96 | `legacy_draft_promotion_review` | `google-play-india-crypto-exchange-removal-2024-01` | [packet](packets/0096-google-play-india-crypto-exchange-removal-2024-01.md) |
| 99 | `legacy_draft_promotion_review` | `hongkong-hkma-stablecoins-ordinance-2025` | [packet](packets/0099-hongkong-hkma-stablecoins-ordinance-2025.md) |
| 100 | `legacy_draft_promotion_review` | `hongkong-sfc-bybit-warning-2024` | [packet](packets/0100-hongkong-sfc-bybit-warning-2024.md) |
| 101 | `legacy_draft_promotion_review` | `hongkong-sfc-jpex-block-2023` | [packet](packets/0101-hongkong-sfc-jpex-block-2023.md) |
| 102 | `legacy_draft_promotion_review` | `hongkong-sfc-vatp-licensing-2023-06` | [packet](packets/0102-hongkong-sfc-vatp-licensing-2023-06.md) |
| 103 | `legacy_draft_promotion_review` | `huobi-htx-privacy-coin-delisting-2024` | [packet](packets/0103-huobi-htx-privacy-coin-delisting-2024.md) |
| 106 | `legacy_draft_promotion_review` | `iceland-cbi-foreign-exchange-bitcoin-2014` | [packet](packets/0106-iceland-cbi-foreign-exchange-bitcoin-2014.md) |
| 109 | `legacy_draft_promotion_review` | `indonesia-bappebti-illegal-exchange-block-2023` | [packet](packets/0109-indonesia-bappebti-illegal-exchange-block-2023.md) |
| 110 | `legacy_draft_promotion_review` | `indonesia-bi-bitcoin-warning-2014` | [packet](packets/0110-indonesia-bi-bitcoin-warning-2014.md) |
| 112 | `legacy_draft_promotion_review` | `infura-metamask-donetsk-luhansk-block-2022-03` | [packet](packets/0112-infura-metamask-donetsk-luhansk-block-2022-03.md) |
| 113 | `legacy_draft_promotion_review` | `iran-cbi-crypto-banking-prohibition-2018` | [packet](packets/0113-iran-cbi-crypto-banking-prohibition-2018.md) |
| 114 | `legacy_draft_promotion_review` | `iran-government-mining-electricity-restriction-2021` | [packet](packets/0114-iran-government-mining-electricity-restriction-2021.md) |
| 117 | `legacy_draft_promotion_review` | `israel-nbctf-hamas-crypto-addresses-2021` | [packet](packets/0117-israel-nbctf-hamas-crypto-addresses-2021.md) |
| 118 | `legacy_draft_promotion_review` | `japan-fsa-binance-sakura-acquisition-2022-11` | [packet](packets/0118-japan-fsa-binance-sakura-acquisition-2022-11.md) |
| 119 | `legacy_draft_promotion_review` | `japan-fsa-binance-warning-2018` | [packet](packets/0119-japan-fsa-binance-warning-2018.md) |
| 121 | `legacy_draft_promotion_review` | `japan-fsa-dmm-bitcoin-order-2024-09` | [packet](packets/0121-japan-fsa-dmm-bitcoin-order-2024-09.md) |
| 122 | `legacy_draft_promotion_review` | `japan-fsa-ftx-japan-suspension-2022-11` | [packet](packets/0122-japan-fsa-ftx-japan-suspension-2022-11.md) |
| 123 | `legacy_draft_promotion_review` | `japan-fsa-six-exchange-orders-2018-06` | [packet](packets/0123-japan-fsa-six-exchange-orders-2018-06.md) |
| 124 | `legacy_draft_promotion_review` | `japan-fsa-stablecoin-psa-effective-2023-06` | [packet](packets/0124-japan-fsa-stablecoin-psa-effective-2023-06.md) |
| 125 | `legacy_draft_promotion_review` | `japan-fsa-travel-rule-effective-2023-06` | [packet](packets/0125-japan-fsa-travel-rule-effective-2023-06.md) |
| 126 | `legacy_draft_promotion_review` | `japan-fsa-zaif-orders-2018-09` | [packet](packets/0126-japan-fsa-zaif-orders-2018-09.md) |
| 127 | `legacy_draft_promotion_review` | `karpeles-arrest-tokyo-mtgox-2015` | [packet](packets/0127-karpeles-arrest-tokyo-mtgox-2015.md) |
| 128 | `legacy_draft_promotion_review` | `kazakhstan-digital-assets-law-2023-02` | [packet](packets/0128-kazakhstan-digital-assets-law-2023-02.md) |
| 129 | `legacy_draft_promotion_review` | `kazakhstan-internet-shutdown-mining-2022-01` | [packet](packets/0129-kazakhstan-internet-shutdown-mining-2022-01.md) |
| 130 | `legacy_draft_promotion_review` | `kingdom-trust-fincen-2021` | [packet](packets/0130-kingdom-trust-fincen-2021.md) |
| 132 | `legacy_draft_promotion_review` | `korea-fsc-institutional-restriction-2017` | [packet](packets/0132-korea-fsc-institutional-restriction-2017.md) |
| 134 | `legacy_draft_promotion_review` | `kraken-monero-eu-delisting-2024` | [packet](packets/0134-kraken-monero-eu-delisting-2024.md) |
| 137 | `legacy_draft_promotion_review` | `kraken-uk-derivatives-exit-2021` | [packet](packets/0137-kraken-uk-derivatives-exit-2021.md) |
| 138 | `legacy_draft_promotion_review` | `kucoin-canada-exit-2023` | [packet](packets/0138-kucoin-canada-exit-2023.md) |
| 140 | `legacy_draft_promotion_review` | `kucoin-netherlands-exit-2023` | [packet](packets/0140-kucoin-netherlands-exit-2023.md) |
| 143 | `legacy_draft_promotion_review` | `liberty-reserve-costa-rica-license-denial-2011-03` | [packet](packets/0143-liberty-reserve-costa-rica-license-denial-2011-03.md) |
| 146 | `legacy_draft_promotion_review` | `makerdao-emergency-shutdown-contingency-2022-08` | [packet](packets/0146-makerdao-emergency-shutdown-contingency-2022-08.md) |
| 149 | `legacy_draft_promotion_review` | `metamask-eth-phishing-detect-tornado-additions-2022` | [packet](packets/0149-metamask-eth-phishing-detect-tornado-additions-2022.md) |
| 150 | `legacy_draft_promotion_review` | `metamask-snaps-region-restrictions-2023-09` | [packet](packets/0150-metamask-snaps-region-restrictions-2023-09.md) |
| 151 | `legacy_draft_promotion_review` | `mica-l2-esma-eba-rts-2024` | [packet](packets/0151-mica-l2-esma-eba-rts-2024.md) |
| 152 | `legacy_draft_promotion_review` | `mtgox-bankruptcy-tokyo-2014` | [packet](packets/0152-mtgox-bankruptcy-tokyo-2014.md) |
| 153 | `legacy_draft_promotion_review` | `mtgox-coinlab-civil-2013` | [packet](packets/0153-mtgox-coinlab-civil-2013.md) |
| 154 | `legacy_draft_promotion_review` | `mtgox-dhs-dwolla-wells-fargo-seizure-2013` | [packet](packets/0154-mtgox-dhs-dwolla-wells-fargo-seizure-2013.md) |
| 155 | `legacy_draft_promotion_review` | `mtgox-june-2011-hack-trading-suspension` | [packet](packets/0155-mtgox-june-2011-hack-trading-suspension.md) |
| 156 | `legacy_draft_promotion_review` | `mtgox-mizuho-wire-pressure-2012` | [packet](packets/0156-mtgox-mizuho-wire-pressure-2012.md) |
| 157 | `legacy_draft_promotion_review` | `mtgox-usd-withdrawal-suspension-2013-06` | [packet](packets/0157-mtgox-usd-withdrawal-suspension-2013-06.md) |
| 161 | `legacy_draft_promotion_review` | `nydfs-bitlicense-bitfinex-kraken-shapeshift-exit-2015` | [packet](packets/0161-nydfs-bitlicense-bitfinex-kraken-shapeshift-exit-2015.md) |
| 162 | `legacy_draft_promotion_review` | `oasis-app-wormhole-counter-exploit-2023-02` | [packet](packets/0162-oasis-app-wormhole-counter-exploit-2023-02.md) |
| 164 | `legacy_draft_promotion_review` | `ofac-dprk-it-worker-sim-hyon-sop-2023-04` | [packet](packets/0164-ofac-dprk-it-worker-sim-hyon-sop-2023-04.md) |
| 165 | `legacy_draft_promotion_review` | `ofac-hamas-buy-cash-msb-2023-10` | [packet](packets/0165-ofac-hamas-buy-cash-msb-2023-10.md) |
| 166 | `legacy_draft_promotion_review` | `ofac-hamas-gaza-now-2024-03` | [packet](packets/0166-ofac-hamas-gaza-now-2024-03.md) |
| 167 | `legacy_draft_promotion_review` | `ofac-hamas-irgc-virtual-currency-network-2024-01` | [packet](packets/0167-ofac-hamas-irgc-virtual-currency-network-2024-01.md) |
| 168 | `legacy_draft_promotion_review` | `ofac-houthi-al-jamal-crypto-refresh-2024-12` | [packet](packets/0168-ofac-houthi-al-jamal-crypto-refresh-2024-12.md) |
| 169 | `legacy_draft_promotion_review` | `ofac-recent-action-20240111` | [packet](packets/0169-ofac-recent-action-20240111.md) |
| 170 | `legacy_draft_promotion_review` | `ofac-trickbot-conti-eleven-2023-09` | [packet](packets/0170-ofac-trickbot-conti-eleven-2023-09.md) |
| 171 | `legacy_draft_promotion_review` | `ofac-zhdanova-russian-elite-launderer-2023-11` | [packet](packets/0171-ofac-zhdanova-russian-elite-launderer-2023-11.md) |
| 172 | `legacy_draft_promotion_review` | `okx-monero-global-delisting-2024` | [packet](packets/0172-okx-monero-global-delisting-2024.md) |
| 174 | `legacy_draft_promotion_review` | `opensea-iran-cuba-sanctions-block-2022` | [packet](packets/0174-opensea-iran-cuba-sanctions-block-2022.md) |
| 175 | `legacy_draft_promotion_review` | `paxos-busd-nydfs-minting-stop-2023` | [packet](packets/0175-paxos-busd-nydfs-minting-stop-2023.md) |
| 176 | `legacy_draft_promotion_review` | `pecunix-bullion-transfer-2008` | [packet](packets/0176-pecunix-bullion-transfer-2008.md) |
| 178 | `legacy_draft_promotion_review` | `philippines-sec-binance-block-2024` | [packet](packets/0178-philippines-sec-binance-block-2024.md) |
| 179 | `legacy_draft_promotion_review` | `polymarket-cftc-geofence-2022-01` | [packet](packets/0179-polymarket-cftc-geofence-2022-01.md) |
| 180 | `legacy_draft_promotion_review` | `polynonce-bittrex-fincen-2022` | [packet](packets/0180-polynonce-bittrex-fincen-2022.md) |
| 182 | `legacy_draft_promotion_review` | `pump-fun-uk-fca-geofence-2024-12` | [packet](packets/0182-pump-fun-uk-fca-geofence-2024-12.md) |
| 183 | `legacy_draft_promotion_review` | `ren-protocol-shutdown-alameda-ftx-2022-12` | [packet](packets/0183-ren-protocol-shutdown-alameda-ftx-2022-12.md) |
| 185 | `legacy_draft_promotion_review` | `russia-cbr-bitcoin-information-letter-2014` | [packet](packets/0185-russia-cbr-bitcoin-information-letter-2014.md) |
| 186 | `legacy_draft_promotion_review` | `russia-cbr-crypto-payment-ban-2022` | [packet](packets/0186-russia-cbr-crypto-payment-ban-2022.md) |
| 187 | `legacy_draft_promotion_review` | `russia-dfa-law-2020` | [packet](packets/0187-russia-dfa-law-2020.md) |
| 189 | `legacy_draft_promotion_review` | `russia-mining-legalization-law-2024-08` | [packet](packets/0189-russia-mining-legalization-law-2024-08.md) |
| 190 | `legacy_draft_promotion_review` | `russia-mining-regional-ban-2024-12` | [packet](packets/0190-russia-mining-regional-ban-2024-12.md) |
| 191 | `legacy_draft_promotion_review` | `russia-rosfinmonitoring-binance-russia-rails-2022` | [packet](packets/0191-russia-rosfinmonitoring-binance-russia-rails-2022.md) |
| 194 | `legacy_draft_promotion_review` | `salame-ftx-campaign-finance-doj-2023` | [packet](packets/0194-salame-ftx-campaign-finance-doj-2023.md) |
| 198 | `legacy_draft_promotion_review` | `sec-garza-gaw-miners-zenminer-2015` | [packet](packets/0198-sec-garza-gaw-miners-zenminer-2015.md) |
| 203 | `legacy_draft_promotion_review` | `sec-v-coinbase-staking-wells-2023` | [packet](packets/0203-sec-v-coinbase-staking-wells-2023.md) |
| 204 | `legacy_draft_promotion_review` | `sec-v-ftx-2022` | [packet](packets/0204-sec-v-ftx-2022.md) |
| 216 | `legacy_draft_promotion_review` | `singapore-mas-retail-crypto-restriction-2022` | [packet](packets/0216-singapore-mas-retail-crypto-restriction-2022.md) |
| 217 | `legacy_draft_promotion_review` | `south-africa-fsca-crypto-financial-product-2022` | [packet](packets/0217-south-africa-fsca-crypto-financial-product-2022.md) |
| 220 | `legacy_draft_promotion_review` | `switzerland-finma-tezos-zg-2018` | [packet](packets/0220-switzerland-finma-tezos-zg-2018.md) |
| 224 | `legacy_draft_promotion_review` | `tether-pig-butchering-second-wave-2024` | [packet](packets/0224-tether-pig-butchering-second-wave-2024.md) |
| 226 | `legacy_draft_promotion_review` | `tether-tron-philippines-pdea-freeze-2024` | [packet](packets/0226-tether-tron-philippines-pdea-freeze-2024.md) |
| 227 | `legacy_draft_promotion_review` | `thailand-bot-bitcoin-prohibition-2013` | [packet](packets/0227-thailand-bot-bitcoin-prohibition-2013.md) |
| 228 | `legacy_draft_promotion_review` | `thailand-sec-binance-bybit-c-and-d-2021` | [packet](packets/0228-thailand-sec-binance-bybit-c-and-d-2021.md) |
| 229 | `legacy_draft_promotion_review` | `tornado-cash-frontend-tornado-cash-eth-block-2022-04` | [packet](packets/0229-tornado-cash-frontend-tornado-cash-eth-block-2022-04.md) |
| 230 | `legacy_draft_promotion_review` | `tornado-cash-github-takedown-2022-08` | [packet](packets/0230-tornado-cash-github-takedown-2022-08.md) |
| 234 | `legacy_draft_promotion_review` | `tornado-cash-pertsev-doj-indictment-2023` | [packet](packets/0234-tornado-cash-pertsev-doj-indictment-2023.md) |
| 236 | `legacy_draft_promotion_review` | `tornado-cash-tornadocash-org-seizure-2022` | [packet](packets/0236-tornado-cash-tornadocash-org-seizure-2022.md) |
| 237 | `legacy_draft_promotion_review` | `trustwallet-sanctioned-token-ui-update-2022` | [packet](packets/0237-trustwallet-sanctioned-token-ui-update-2022.md) |
| 239 | `legacy_draft_promotion_review` | `turkey-cmb-casp-licensing-law-7518-2024` | [packet](packets/0239-turkey-cmb-casp-licensing-law-7518-2024.md) |
| 240 | `legacy_draft_promotion_review` | `uae-vara-licence-issuance-regime-2023` | [packet](packets/0240-uae-vara-licence-issuance-regime-2023.md) |
| 242 | `legacy_draft_promotion_review` | `uk-fca-crypto-promotion-rule-2023` | [packet](packets/0242-uk-fca-crypto-promotion-rule-2023.md) |
| 243 | `legacy_draft_promotion_review` | `uk-hmrc-bitcoin-vat-brief-09-14-2014` | [packet](packets/0243-uk-hmrc-bitcoin-vat-brief-09-14-2014.md) |
| 244 | `legacy_draft_promotion_review` | `ukraine-virtual-assets-law-2022-03` | [packet](packets/0244-ukraine-virtual-assets-law-2022-03.md) |
| 245 | `legacy_draft_promotion_review` | `uniswap-balancer-tornado-frontend-block-2022-08` | [packet](packets/0245-uniswap-balancer-tornado-frontend-block-2022-08.md) |
| 247 | `legacy_draft_promotion_review` | `uniswap-token-list-curation-default-2021` | [packet](packets/0247-uniswap-token-list-curation-default-2021.md) |
| 248 | `legacy_draft_promotion_review` | `uniswap-tokenized-stocks-delisting-2021-07` | [packet](packets/0248-uniswap-tokenized-stocks-delisting-2021-07.md) |
| 249 | `legacy_draft_promotion_review` | `unsc-resolution-2371-dprk-crypto-2017` | [packet](packets/0249-unsc-resolution-2371-dprk-crypto-2017.md) |
| 250 | `legacy_draft_promotion_review` | `uzbekistan-napp-vasp-licensing-2022-07` | [packet](packets/0250-uzbekistan-napp-vasp-licensing-2022-07.md) |
| 251 | `legacy_draft_promotion_review` | `voyager-bankruptcy-doj-objection-2023` | [packet](packets/0251-voyager-bankruptcy-doj-objection-2023.md) |
| 253 | `legacy_draft_promotion_review` | `wikileaks-amazon-aws-eviction-2010-12` | [packet](packets/0253-wikileaks-amazon-aws-eviction-2010-12.md) |
| 254 | `legacy_draft_promotion_review` | `wikileaks-bank-of-america-block-2010-12` | [packet](packets/0254-wikileaks-bank-of-america-block-2010-12.md) |
| 255 | `legacy_draft_promotion_review` | `wikileaks-everydns-domain-termination-2010-12` | [packet](packets/0255-wikileaks-everydns-domain-termination-2010-12.md) |
| 256 | `legacy_draft_promotion_review` | `wikileaks-mastercard-suspension-2010-12` | [packet](packets/0256-wikileaks-mastercard-suspension-2010-12.md) |
| 257 | `legacy_draft_promotion_review` | `wikileaks-paypal-freeze-2010-12` | [packet](packets/0257-wikileaks-paypal-freeze-2010-12.md) |
| 258 | `legacy_draft_promotion_review` | `wikileaks-postfinance-account-closure-2010-12` | [packet](packets/0258-wikileaks-postfinance-account-closure-2010-12.md) |
| 259 | `legacy_draft_promotion_review` | `wikileaks-visa-europe-suspension-2010-12` | [packet](packets/0259-wikileaks-visa-europe-suspension-2010-12.md) |
| 260 | `legacy_draft_promotion_review` | `wikileaks-wau-holland-tax-status-challenge-2010-12` | [packet](packets/0260-wikileaks-wau-holland-tax-status-challenge-2010-12.md) |
| 261 | `legacy_draft_promotion_review` | `wikileaks-western-union-interdiction-2010-12` | [packet](packets/0261-wikileaks-western-union-interdiction-2010-12.md) |

## LLM-Prescreen Flagged For Repair

| Blocker | Count |
| --- | ---: |
| `none_detected` | 198 |
| `no_observation_primary_source_detected` | 2 |

## Work Files

- `pending_human_confirmation.csv`: rows ready for human confirmation after LLM/machine prescreen.
- `llm_prescreen_flagged_for_repair.csv`: pre-human LLM/machine flags requiring evidence repair.
- `needs_evidence_repair.csv`: compatibility alias for the same repair list.
- `packets/index.md`: all machine-prepared packets with current queue status.
