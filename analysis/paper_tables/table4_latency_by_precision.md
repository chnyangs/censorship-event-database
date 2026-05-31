# Table 4 · Latency evidence surface (precision-filtered)

Dataset snapshot: **v0.2.0-rc-dryrun-11** · cutoff `2026-06-01` · commit `e43eea7` · generated `2026-06-01T00:00:00Z`

Supports **C3** (`docs/paper_claims.md §1`). Only triggers with hour-or-better precision contribute to the hour-granularity panel; day-precision triggers are reported separately. `trigger_is_action` events (C4) are excluded from both panels and surfaced in Panel C — their t≈0 is a record-level artifact, not a measured delta.

## Panel A · Hour-precision triggers (n=4)

| band | count | events |
| --- | ---: | --- |
| t=0 | 2 | `china-weibo-crypto-exchange-purge-2021-03`, `kazakhstan-internet-shutdown-mining-2022-01` |
| (0, 1]h | 0 | — |
| (1, 6]h | 1 | `tornado-cash-ofac-2022` |
| (6, 24]h | 1 | `china-pboc-crypto-ban-2021` |
| (24, 168]h (≤1w) | 0 | — |
| >168h (>1w) | 0 | — |
| **total** | **4** | |

## Panel B · Day-precision triggers (n=198)

Day-precision triggers cannot support hour-granularity latency claims. The event's `time_to_first_change_hours` is converted into a conservative interval `[max(0, H-24), H]`; rows crossing a day-band boundary are reported as `ambiguous_boundary`. Per-event hour values in the CSV dump are **record-level artifacts** (timestamp arithmetic) and must not enter any hour-bucketed paper claim.

| day-granularity interval band | count | events |
| --- | ---: | --- |
| ≤1d | 153 | `1mdc-egold-account-freeze-2007-04`, `algeria-finance-law-2018-crypto-prohibition`, `alphabay-hansa-doj-2017`, `argentina-bcra-banks-crypto-services-ban-2022-05`, `australia-asic-binance-derivatives-2023`, `bcbs-cryptoasset-prudential-standard-sco60-2022`, `belgium-fsma-binance-cease-2023`, `binance-4framework-2023`, `binance-cftc-2023`, `bitfinex-cftc-retail-commodity-2016`, `bitfinex-tether-cftc-2021`, `bitfinex-tether-nyag-2021`, `bitmex-cftc-doj-2020`, `bitzlato-doj-2023`, `blockfi-sec-lending-2022`, `btc-e-doj-2017`, `cambodia-nbc-joint-crypto-prohibition-2018-05`, `canada-convoy-freeze-2022`, `celsius-bankruptcy-mashinsky-doj-2023`, `cftc-defi-opyn-zeroex-deridex-2023-09`, `china-ico-ban-2017-09`, `china-inner-mongolia-mining-ban-2021-05`, `china-ndrc-mining-eliminated-industry-notice-2021-09`, `china-nft-secondary-trading-self-discipline-2022-06`, `china-pboc-banks-alipay-payment-channel-block-2021-06`, `china-pboc-exchange-access-block-2019-06`, `china-pboc-exchange-shutdown-2017-09`, `china-search-engine-social-keyword-exchange-block-2021-06`, `chipmixer-doj-2023`, `coin-mx-doj-murgio-2015`, `coinbase-irs-john-doe-summons-2016`, `coinflip-cftc-derivabit-2015`, `cryptex-ofac-2024`, `cryptex-uaps-pm2btc-ivanov-shakhmametov-doj-2024`, `datacell-v-valitor-iceland-district-court-2012-07`, `dprk-usdt-network-ofac-2025`, `dydx-canada-frontend-wind-down-2023-04`, `eba-virtual-currencies-opinion-eba-op-2014-08`, `ecuador-national-assembly-bitcoin-ban-2014-07`, `egold-doj-guilty-plea-2008-07`, `egold-doj-indictment-2007-04`, `egypt-cbe-banking-law-194-2020`, `eu-12th-russia-sanctions-2023`, `eu-16th-russia-sanctions-2025`, `eu-18th-russia-sanctions-casp-spfs-2025`, `eu-19th-russia-sanctions-a7a5-crypto-ban-2025`, `eu-20th-russia-sanctions-crypto-sectoral-ban-2026`, `eu-8th-package-russia-crypto-services-ban-2022-10`, `eu-mica-2023`, `eu-russia-crypto-wallet-cap-2022`, `eu-russia-full-crypto-wallet-ban-2022`, `eu-tfr-recast-2023`, `fatf-r15-vasp-travel-rule-2019`, `fincen-eric-powers-p2p-exchanger-2019-04`, `ftx-bankman-fried-doj-2022`, `funnull-cdn-ofac-2025`, `garantex-besciokov-mira-serda-doj-2025`, `garantex-ofac-2022`, `genesis-sec-gemini-earn-2023`, `germany-bafin-binance-licence-withdrawal-2023`, `grinex-garantex-successor-ofac-2025`, `helix-doj-mixer-2020`, `hongkong-hkma-stablecoins-ordinance-2025`, `hongkong-sfc-bybit-warning-2024`, `hongkong-sfc-jpex-block-2023`, `hongkong-sfc-vatp-licensing-2023-06`, `hydra-doj-2022`, `hydra-ofac-2022`, `indonesia-bappebti-illegal-exchange-block-2023`, `indonesia-bi-payment-instrument-prohibition-2018-01`, `indonesia-kominfo-exchange-social-account-block-2024-07`, `iran-cbi-crypto-banking-prohibition-2018`, `iran-cbi-exchange-payment-gateway-block-2024-12`, `iran-government-mining-electricity-restriction-2021`, `israel-nbctf-hamas-crypto-addresses-2021`, `japan-fsa-binance-warning-2018`, `japan-fsa-coincheck-orders-2018`, `japan-fsa-dmm-bitcoin-order-2024-09`, `japan-fsa-ftx-japan-suspension-2022-11`, `japan-fsa-six-exchange-orders-2018-06`, `japan-fsa-zaif-orders-2018-09`, `jordan-cbj-bank-crypto-prohibition-2014`, `kenya-cbk-virtual-currency-circular-2015-12`, `korea-fiu-isms-real-name-exchange-shutdown-2021-09`, `korea-fsc-ico-ban-2017`, `korea-fsc-institutional-restriction-2017`, `korea-fsc-privacy-coin-delisting-mandate-2021-03`, `korea-travel-rule-2022`, `kraken-sec-staking-2023`, `kraken-sec-unregistered-exchange-2023`, `kucoin-doj-2024`, `liberty-reserve-coordinated-takedown-2013-05`, `liberty-reserve-costa-rica-license-denial-2011-03`, `malaysia-sc-binance-disable-2021`, `morocco-office-des-changes-crypto-ban-2017-11`, `mtgox-dhs-dwolla-wells-fargo-seizure-2013`, `mtgox-june-2011-hack-trading-suspension`, `myanmar-cbm-crypto-prohibition-directive-9-2020`, `nepal-nrb-comprehensive-crypto-ban-2021-09`, `nigeria-binance-network-block-2024-02`, `nigeria-cbn-crypto-ban-2021`, `nydfs-bitlicense-2015-06`, `oecd-carf-2022`, `ofac-hamas-buy-cash-msb-2023-10`, `okx-aux-cayes-doj-guilty-plea-2025`, `pakistan-sbp-crypto-prohibition-2018-04`, `philippines-bsp-vasp-license-moratorium-2022-09`, `philippines-sec-binance-block-2024`, `polymarket-cftc-geofence-2022-01`, `polynonce-bittrex-fincen-2022`, `powell-unlicensed-bitcoin-exchange-2014`, `qatar-qcb-qfcra-virtual-asset-ban-2019-12`, `ripple-fincen-xrp-2015`, `russia-mining-regional-ban-2024-12`, `samourai-doj-2024`, `sec-abra-plutus-earn-cease-2024-08`, `sec-beaxy-platform-shutdown-2023`, `sec-burnside-bitcoin-stock-exchange-2014`, `sec-consensys-metamask-staking-swaps-2024-06`, `sec-etherdelta-coburn-unregistered-exchange-2018-11`, `sec-etoro-cease-crypto-trading-2024-09`, `sec-garza-gaw-miners-zenminer-2015`, `sec-kik-interactive-kin-unregistered-offering-2020-10`, `sec-lbry-lbc-unregistered-securities-2021-03`, `sec-nexo-earn-lending-product-cease-2023-01`, `sec-poloniex-unregistered-exchange-2021-08`, `sec-shavers-btcst-2013`, `sec-tokenlot-unregistered-broker-2018-09`, `sec-v-ripple-2020`, `sec-voorhees-satoshidice-2014`, `silk-road-doj-seizure-2013`, `sinbad-doj-2024`, `singapore-mas-retail-crypto-restriction-2022`, `sri-lanka-cbsl-crypto-warning-fx-directive-2021`, `taiwan-fsc-bitcoin-bank-atm-ban-2014-01`, `teraexchange-cftc-bitcoin-swap-2015`, `thailand-bot-bitcoin-prohibition-2013`, `thailand-sec-binance-bybit-c-and-d-2021`, `thailand-sec-crypto-payment-ban-2022-04`, `thailand-sec-meme-fan-nft-exchange-token-ban-2021-06`, `tornado-cash-ofac-delisting-2025`, `tornado-cash-storm-conviction-2025`, `uk-fca-binance-markets-2021`, `uk-fca-crypto-promotion-rule-2023`, `ukraine-virtual-assets-law-2022-03`, `venezuela-sunacrip-mining-exchange-halt-2023-03`, `vietnam-sbv-payment-prohibition-2017-10`, `voyager-bankruptcy-doj-objection-2023`, `webmoney-ukraine-tax-police-freeze-2013-06`, `welcome-to-video-doj-2019`, `wikileaks-wau-holland-tax-status-challenge-2010-12`, `zimbabwe-rbz-circular-2-2018-golix`, `zimbabwe-rbz-circular-2-2018-golix-ban` |
| (1d, 30d] | 25 | `binance-dex-29-country-geoblock-2019-07`, `binance-eea-usdt-spot-delisting-2025-03`, `binance-monero-global-delisting-2024-02`, `bittrex-privacy-coin-delisting-2021-01`, `blender-ofac-2022`, `blockfi-multistate-cease-desist-bia-2021-07`, `bybit-france-exit-2024-12`, `china-pboc-banks-close-exchange-accounts-2014-04`, `china-pboc-crypto-ban-2013-12`, `coinbase-india-exit-2022`, `ebullion-doj-fbi-seizure-2008-08`, `india-fiu-offshore-vda-block-2023`, `kucoin-canada-exit-2023`, `okex-privacy-coin-delisting-2019-09`, `okx-canada-exit-2023`, `okx-nigeria-exit-2024-08`, `orca-dex-us-frontend-block-2023-03`, `poloniex-circle-us-token-geofence-2019-05`, `sec-tradestation-crypto-lending-cease-2024-02`, `sec-v-binance-2023`, `sec-v-bittrex-2023`, `singapore-mas-binance-services-2021`, `suex-ofac-2021`, `turkey-cbrt-crypto-ban-2021`, `upbit-privacy-coin-delisting-2019-09` |
| >30d | 14 | `canada-csa-binance-withdrawal-2023`, `cftc-v-ooki-dao-2022`, `etoro-us-ada-trx-delisting-2021-12`, `india-rbi-crypto-ban-2018`, `kazakhstan-digital-assets-law-2023-02`, `nepal-nrb-bitcoin-ban-2017-08`, `netherlands-dnb-binance-warning-2021`, `paxos-canada-exit-2023-04`, `russia-election-interference-ofac-2020`, `russian-cyber-theft-ofac-2020`, `sec-v-coinbase-2023`, `sec-v-telegram-ton-2020`, `shrem-faiella-bitcoin-exchange-2014`, `tornado-cash-ofac-redesignation-2022` |
| ambiguous_boundary | 6 | `aeza-group-ofac-2025`, `chatex-ofac-2021`, `circle-usdc-cryptex-freeze-2024`, `crypto-com-eu-usdt-stablecoin-delisting-2025-01`, `lockbit-affiliates-ofac-2024`, `semenov-ofac-2023` |
| **total** | **198** | |

## Panel C · Excluded from both panels — `trigger_is_action` (n=68)

| event_id | trigger_type |
| --- | --- |
| `1inch-us-geofence-2021-09` | `corporate_policy_change` |
| `aave-arc-fireblocks-whitelist-2022-01` | `corporate_policy_change` |
| `aave-tornado-frontend-block-2022-08` | `corporate_policy_change` |
| `apple-india-crypto-exchange-removal-2024-01` | `corporate_policy_change` |
| `apple-uniswap-wallet-app-store-rejection-2023-03` | `corporate_policy_change` |
| `augur-v2-us-uk-geofence-2020-07` | `corporate_policy_change` |
| `binance-busd-wind-down-2024` | `corporate_policy_change` |
| `binance-com-us-customer-geofence-2019-06` | `corporate_policy_change` |
| `binance-hamas-account-freeze-israel-2023-10` | `corporate_policy_change` |
| `binance-netherlands-exit-2023-07` | `corporate_policy_change` |
| `binance-nigeria-naira-services-end-2024-03` | `corporate_policy_change` |
| `binance-palestinian-accounts-seizure-israel-2023-11` | `corporate_policy_change` |
| `binance-privacy-coin-delisting-2023` | `corporate_policy_change` |
| `binance-russia-exit-commex-2023` | `corporate_policy_change` |
| `binance-russia-gunmaker-asset-freeze-ukraine-2022-08` | `corporate_policy_change` |
| `binance-uk-new-user-halt-2023-10` | `corporate_policy_change` |
| `binance-us-staking-end-2023` | `corporate_policy_change` |
| `bitcoinica-shutdown-2012-05` | `corporate_policy_change` |
| `bitfloor-capital-one-debanking-2013-04` | `corporate_policy_change` |
| `bybit-canada-exit-2023-05` | `corporate_policy_change` |
| `bybit-singapore-exit-2022` | `corporate_policy_change` |
| `circle-usdc-tornado-2022` | `corporate_policy_change` |
| `cloudflare-ethereum-gateway-tornado-block-2022-08` | `corporate_policy_change` |
| `coinbase-eu-usdt-stablecoin-delisting-2024-12` | `corporate_policy_change` |
| `coinbase-japan-exit-2023` | `corporate_policy_change` |
| `dydx-tornado-account-block-2022-08` | `corporate_policy_change` |
| `etherscan-tornado-cash-ui-label-2022` | `corporate_policy_change` |
| `gate-io-privacy-coin-perpetuals-delisting-2024-12` | `corporate_policy_change` |
| `gemini-netherlands-exit-2023-11` | `corporate_policy_change` |
| `google-play-india-crypto-exchange-removal-2024-01` | `corporate_policy_change` |
| `huobi-htx-privacy-coin-delisting-2024` | `corporate_policy_change` |
| `infura-alchemy-tornado-rpc-block-2022` | `corporate_policy_change` |
| `infura-metamask-donetsk-luhansk-block-2022-03` | `corporate_policy_change` |
| `kraken-monero-eu-delisting-2024` | `corporate_policy_change` |
| `kraken-uk-derivatives-exit-2021` | `corporate_policy_change` |
| `metamask-eth-phishing-detect-tornado-additions-2022` | `corporate_policy_change` |
| `metamask-snaps-region-restrictions-2023-09` | `corporate_policy_change` |
| `mtgox-bankruptcy-tokyo-2014` | `corporate_policy_change` |
| `mtgox-usd-withdrawal-suspension-2013-06` | `corporate_policy_change` |
| `okx-india-exit-2024-03` | `corporate_policy_change` |
| `okx-privacy-token-delist-2024` | `corporate_policy_change` |
| `opensea-iran-cuba-sanctions-block-2022` | `corporate_policy_change` |
| `pancakeswap-sanctioned-country-frontend-geofence-2022` | `corporate_policy_change` |
| `paxos-busd-nydfs-minting-stop-2023` | `corporate_policy_change` |
| `pecunix-bullion-transfer-2008` | `corporate_policy_change` |
| `pump-fun-uk-fca-geofence-2024-12` | `corporate_policy_change` |
| `shapeshift-mandatory-kyc-anonymity-end-2018-09` | `corporate_policy_change` |
| `tether-doj-pig-butchering-freeze-2023` | `corporate_policy_change` |
| `tether-dprk-precommit-freeze-2025` | `corporate_policy_change` |
| `tether-garantex-usdt-freeze-2025-03` | `corporate_policy_change` |
| `tether-pig-butchering-second-wave-2024` | `corporate_policy_change` |
| `tether-retroactive-sweep-2023` | `corporate_policy_change` |
| `tornado-cash-frontend-tornado-cash-eth-block-2022-04` | `corporate_policy_change` |
| `tornado-cash-github-takedown-2022-08` | `corporate_policy_change` |
| `tornado-cash-tornadocash-org-seizure-2022` | `corporate_policy_change` |
| `tradehill-dwolla-payment-cutoff-2012-02` | `corporate_policy_change` |
| `uniswap-balancer-tornado-frontend-block-2022-08` | `corporate_policy_change` |
| `uniswap-frontend-delisting-2023` | `corporate_policy_change` |
| `uniswap-tokenized-stocks-delisting-2021-07` | `corporate_policy_change` |
| `upbit-bithumb-regulatory-delisting-purge-2021-06` | `corporate_policy_change` |
| `wikileaks-amazon-aws-eviction-2010-12` | `corporate_policy_change` |
| `wikileaks-bank-of-america-block-2010-12` | `corporate_policy_change` |
| `wikileaks-everydns-domain-termination-2010-12` | `corporate_policy_change` |
| `wikileaks-mastercard-suspension-2010-12` | `corporate_policy_change` |
| `wikileaks-paypal-freeze-2010-12` | `corporate_policy_change` |
| `wikileaks-postfinance-account-closure-2010-12` | `corporate_policy_change` |
| `wikileaks-visa-europe-suspension-2010-12` | `corporate_policy_change` |
| `wikileaks-western-union-interdiction-2010-12` | `corporate_policy_change` |
