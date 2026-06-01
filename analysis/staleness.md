# Staleness report

Generated at: `2026-06-01T03:34:29Z`
Red threshold: audits / verifications older than `90` days.
Most recent agent activity in `candidate_triggers/`: `none recorded`.

## Coverage snapshot

Two dimensions tracked per event; missing values surface as explicit gaps, never masked.

- **Adversarial audit** (`last_human_audit`): {'no_audit_recorded': 289, 'ok': 116}
- **Verification** (`last_verified`): {'ok': 405}
- **Row-level summary** (worst of the two): {'no_audit_recorded': 289, 'ok': 116}

## Flag legend

- `ok` — within the red threshold
- `red` — older than 90 days
- `no_audit_recorded` — no last_human_audit on record — event has never been through an adversarial audit
- `no_verification_recorded` — no last_verified on record — event has never been re-verified
- `error` — event YAML failed to parse

## Per-event table

| Event | Status | Origin | last_human_audit | Audit age | Audit flag | last_verified | Verification age | Verif flag | Summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `1inch-us-geofence-2021-09` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-21 | 11 | ok | no_audit_recorded |
| `1mdc-egold-account-freeze-2007-04` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-31 | 1 | ok | no_audit_recorded |
| `aave-arc-fireblocks-whitelist-2022-01` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-21 | 11 | ok | no_audit_recorded |
| `aave-tornado-frontend-block-2022-08` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-21 | 11 | ok | no_audit_recorded |
| `aeza-group-ofac-2025` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-22 | 40 | ok | no_audit_recorded |
| `al-law-hezbollah-crypto-ofac-2024-03` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-31 | 1 | ok | no_audit_recorded |
| `algeria-finance-law-2018-crypto-prohibition` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-31 | 1 | ok | no_audit_recorded |
| `alphabay-hansa-doj-2017` | `admitted` | `human_reviewed` | 2026-05-16 | 16 | ok | 2026-05-16 | 16 | ok | ok |
| `apple-india-crypto-exchange-removal-2024-01` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-21 | 11 | ok | no_audit_recorded |
| `apple-uniswap-wallet-app-store-rejection-2023-03` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-31 | 1 | ok | no_audit_recorded |
| `argentina-bcra-banks-crypto-services-ban-2022-05` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-31 | 1 | ok | no_audit_recorded |
| `argentina-cnv-psav-registration-2024` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-21 | 11 | ok | no_audit_recorded |
| `argentina-uif-resolution-300-2014` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-21 | 11 | ok | no_audit_recorded |
| `augur-v2-us-uk-geofence-2020-07` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-21 | 11 | ok | no_audit_recorded |
| `australia-asic-binance-derivatives-2023` | `admitted` | `human_reviewed` | 2026-05-16 | 16 | ok | 2026-05-16 | 16 | ok | ok |
| `bangladesh-bank-fepd-virtual-assets-prohibition-2022-09` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-31 | 1 | ok | no_audit_recorded |
| `bangladesh-bb-bitcoin-warning-2014` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-21 | 11 | ok | no_audit_recorded |
| `bcbs-cryptoasset-prudential-standard-sco60-2022` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-31 | 1 | ok | no_audit_recorded |
| `belgium-fsma-binance-cease-2023` | `admitted` | `human_reviewed` | 2026-05-16 | 16 | ok | 2026-05-16 | 16 | ok | ok |
| `binance-4framework-2023` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-22 | 40 | ok | no_audit_recorded |
| `binance-busd-wind-down-2024` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-21 | 11 | ok | no_audit_recorded |
| `binance-cftc-2023` | `admitted` | `human_reviewed` | 2026-05-16 | 16 | ok | 2026-05-16 | 16 | ok | ok |
| `binance-com-us-customer-geofence-2019-06` | `admitted` | `human_reviewed` | 2026-05-31 | 1 | ok | 2026-05-31 | 1 | ok | ok |
| `binance-dex-29-country-geoblock-2019-07` | `admitted` | `human_reviewed` | 2026-05-31 | 1 | ok | 2026-05-31 | 1 | ok | ok |
| `binance-eea-usdt-spot-delisting-2025-03` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-31 | 1 | ok | no_audit_recorded |
| `binance-hamas-account-freeze-israel-2023-10` | `admitted` | `human_reviewed` | 2026-05-31 | 1 | ok | 2026-05-31 | 1 | ok | ok |
| `binance-monero-global-delisting-2024-02` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-31 | 1 | ok | no_audit_recorded |
| `binance-netherlands-exit-2023-07` | `admitted` | `human_reviewed` | 2026-05-31 | 1 | ok | 2026-05-31 | 1 | ok | ok |
| `binance-nigeria-naira-services-end-2024-03` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-31 | 1 | ok | no_audit_recorded |
| `binance-palestinian-accounts-seizure-israel-2023-11` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-31 | 1 | ok | no_audit_recorded |
| `binance-privacy-coin-delisting-2023` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-06-01 | 0 | ok | no_audit_recorded |
| `binance-russia-exit-commex-2023` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-06-01 | 0 | ok | no_audit_recorded |
| `binance-russia-gunmaker-asset-freeze-ukraine-2022-08` | `admitted` | `human_reviewed` | 2026-05-31 | 1 | ok | 2026-05-31 | 1 | ok | ok |
| `binance-uk-new-user-halt-2023-10` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-31 | 1 | ok | no_audit_recorded |
| `binance-us-staking-end-2023` | `rejected` | `human_reviewed` | — | — | no_audit_recorded | 2026-06-01 | 0 | ok | no_audit_recorded |
| `bitcoin-fog-sterlingov-doj-2024` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-31 | 1 | ok | no_audit_recorded |
| `bitcoin-maven-tetley-doj-2018` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-31 | 1 | ok | no_audit_recorded |
| `bitcoinica-shutdown-2012-05` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-21 | 11 | ok | no_audit_recorded |
| `bitfinex-cftc-retail-commodity-2016` | `admitted` | `human_reviewed` | 2026-05-16 | 16 | ok | 2026-05-16 | 16 | ok | ok |
| `bitfinex-tether-cftc-2021` | `admitted` | `human_reviewed` | 2026-05-16 | 16 | ok | 2026-05-16 | 16 | ok | ok |
| `bitfinex-tether-nyag-2021` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-21 | 11 | ok | no_audit_recorded |
| `bitfinex-us-retail-customer-exit-2017-11` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-31 | 1 | ok | no_audit_recorded |
| `bitfloor-capital-one-debanking-2013-04` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-31 | 1 | ok | no_audit_recorded |
| `bitmex-cftc-doj-2020` | `admitted` | `human_reviewed` | 2026-05-16 | 16 | ok | 2026-05-16 | 16 | ok | ok |
| `bitmex-fincen-2024` | `admitted` | `human_reviewed` | 2026-05-20 | 12 | ok | 2026-05-20 | 12 | ok | ok |
| `bitriver-russia-mining-ofac-2022-04` | `admitted` | `human_reviewed` | 2026-05-31 | 1 | ok | 2026-05-31 | 1 | ok | ok |
| `bitstamp-greece-portugal-exit-2023` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-21 | 11 | ok | no_audit_recorded |
| `bittrex-global-shutdown-2023-11` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-31 | 1 | ok | no_audit_recorded |
| `bittrex-privacy-coin-delisting-2021-01` | `admitted` | `human_reviewed` | 2026-05-31 | 1 | ok | 2026-05-31 | 1 | ok | ok |
| `bitzlato-doj-2023` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-21 | 41 | ok | no_audit_recorded |
| `blender-ofac-2022` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-21 | 41 | ok | no_audit_recorded |
| `blockfi-multistate-cease-desist-bia-2021-07` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-31 | 1 | ok | no_audit_recorded |
| `blockfi-sec-lending-2022` | `admitted` | `human_reviewed` | 2026-05-16 | 16 | ok | 2026-05-16 | 16 | ok | ok |
| `bolivia-bcb-crypto-prohibition-2014` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-21 | 11 | ok | no_audit_recorded |
| `botnet-911-s5-ofac-2024-05` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-31 | 1 | ok | no_audit_recorded |
| `brazil-bacen-stablecoin-restriction-2023` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-21 | 11 | ok | no_audit_recorded |
| `brazil-bcb-comunicado-25306-2014` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-21 | 11 | ok | no_audit_recorded |
| `btc-e-doj-2017` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-22 | 40 | ok | no_audit_recorded |
| `bybit-canada-exit-2023-05` | `admitted` | `human_reviewed` | 2026-05-31 | 1 | ok | 2026-05-31 | 1 | ok | ok |
| `bybit-france-exit-2024-12` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-31 | 1 | ok | no_audit_recorded |
| `bybit-singapore-exit-2022` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-17 | 15 | ok | no_audit_recorded |
| `cambodia-nbc-joint-crypto-prohibition-2018-05` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-31 | 1 | ok | no_audit_recorded |
| `canada-convoy-freeze-2022` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-22 | 40 | ok | no_audit_recorded |
| `canada-csa-binance-withdrawal-2023` | `admitted` | `human_reviewed` | 2026-05-16 | 16 | ok | 2026-05-16 | 16 | ok | ok |
| `celsius-bankruptcy-mashinsky-doj-2023` | `admitted` | `human_reviewed` | 2026-05-16 | 16 | ok | 2026-05-16 | 16 | ok | ok |
| `celsius-multistate-cease-desist-earn-2021-09` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-31 | 1 | ok | no_audit_recorded |
| `cftc-defi-opyn-zeroex-deridex-2023-09` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-31 | 1 | ok | no_audit_recorded |
| `cftc-v-ftx-2022` | `admitted` | `human_reviewed` | 2026-05-20 | 12 | ok | 2026-05-20 | 12 | ok | ok |
| `cftc-v-ooki-dao-2022` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-22 | 40 | ok | no_audit_recorded |
| `chatex-ofac-2021` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-22 | 40 | ok | no_audit_recorded |
| `china-fentanyl-network-ofac-2023-10` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-31 | 1 | ok | no_audit_recorded |
| `china-ico-ban-2017-09` | `admitted` | `human_reviewed` | 2026-05-16 | 16 | ok | 2026-05-21 | 11 | ok | ok |
| `china-inner-mongolia-mining-ban-2021-05` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-21 | 11 | ok | no_audit_recorded |
| `china-ndrc-mining-eliminated-industry-notice-2021-09` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-31 | 1 | ok | no_audit_recorded |
| `china-nft-secondary-trading-self-discipline-2022-06` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-21 | 11 | ok | no_audit_recorded |
| `china-pboc-banks-alipay-payment-channel-block-2021-06` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-31 | 1 | ok | no_audit_recorded |
| `china-pboc-banks-close-exchange-accounts-2014-04` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-31 | 1 | ok | no_audit_recorded |
| `china-pboc-crypto-ban-2013-12` | `admitted` | `human_reviewed` | 2026-05-16 | 16 | ok | 2026-05-16 | 16 | ok | ok |
| `china-pboc-crypto-ban-2021` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-21 | 41 | ok | no_audit_recorded |
| `china-pboc-exchange-access-block-2019-06` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-31 | 1 | ok | no_audit_recorded |
| `china-pboc-exchange-shutdown-2017-09` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-21 | 11 | ok | no_audit_recorded |
| `china-search-engine-social-keyword-exchange-block-2021-06` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-31 | 1 | ok | no_audit_recorded |
| `china-sichuan-mining-ban-2021-06` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-21 | 11 | ok | no_audit_recorded |
| `china-state-council-mining-crackdown-2021-05` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-21 | 11 | ok | no_audit_recorded |
| `china-weibo-crypto-exchange-purge-2021-03` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-21 | 11 | ok | no_audit_recorded |
| `chinyong-kim-sang-man-dprk-it-worker-ofac-2023-05` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-31 | 1 | ok | no_audit_recorded |
| `chipmixer-doj-2023` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-22 | 40 | ok | no_audit_recorded |
| `circle-usdc-cryptex-freeze-2024` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-21 | 11 | ok | no_audit_recorded |
| `circle-usdc-multichain-hack-freeze-2023-07` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-31 | 1 | ok | no_audit_recorded |
| `circle-usdc-sealed-civil-case-16-address-freeze-2026-03` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-31 | 1 | ok | no_audit_recorded |
| `circle-usdc-svb-policy-statement-2023` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-21 | 11 | ok | no_audit_recorded |
| `circle-usdc-tornado-2022` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-22 | 40 | ok | no_audit_recorded |
| `cloudflare-ethereum-gateway-tornado-block-2022-08` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-21 | 11 | ok | no_audit_recorded |
| `coin-mx-doj-murgio-2015` | `admitted` | `human_reviewed` | 2026-05-20 | 12 | ok | 2026-05-20 | 12 | ok | ok |
| `coinbase-eu-usdt-stablecoin-delisting-2024-12` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-31 | 1 | ok | no_audit_recorded |
| `coinbase-india-exit-2022` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-22 | 40 | ok | no_audit_recorded |
| `coinbase-irs-john-doe-summons-2016` | `admitted` | `human_reviewed` | 2026-05-16 | 16 | ok | 2026-05-16 | 16 | ok | ok |
| `coinbase-japan-exit-2023` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-21 | 11 | ok | no_audit_recorded |
| `coinflip-cftc-derivabit-2015` | `admitted` | `human_reviewed` | 2026-05-16 | 16 | ok | 2026-05-16 | 16 | ok | ok |
| `colonial-pipeline-darkside-ransom-clawback-doj-2021` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-31 | 1 | ok | no_audit_recorded |
| `consensys-metamask-infura-rpc-data-collection-2022-11` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-21 | 11 | ok | no_audit_recorded |
| `cryptex-ofac-2024` | `admitted` | `human_authored` | 2026-04-22 | 40 | ok | 2026-04-21 | 41 | ok | ok |
| `cryptex-uaps-pm2btc-ivanov-shakhmametov-doj-2024` | `admitted` | `human_reviewed` | 2026-05-31 | 1 | ok | 2026-05-31 | 1 | ok | ok |
| `crypto-capital-fowler-doj-2019` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-31 | 1 | ok | no_audit_recorded |
| `crypto-com-eu-usdt-stablecoin-delisting-2025-01` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-31 | 1 | ok | no_audit_recorded |
| `datacell-v-valitor-iceland-district-court-2012-07` | `admitted` | `human_reviewed` | 2026-05-20 | 12 | ok | 2026-05-20 | 12 | ok | ok |
| `derakhshan-alivand-irgc-crypto-ofac-2025-09` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-31 | 1 | ok | no_audit_recorded |
| `dkba-burma-scam-compound-ofac-2025-11` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-31 | 1 | ok | no_audit_recorded |
| `dprk-usdt-network-ofac-2025` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-22 | 40 | ok | no_audit_recorded |
| `dydx-canada-frontend-wind-down-2023-04` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-31 | 1 | ok | no_audit_recorded |
| `dydx-tornado-account-block-2022-08` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-21 | 11 | ok | no_audit_recorded |
| `eba-virtual-currencies-opinion-eba-op-2014-08` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-21 | 11 | ok | no_audit_recorded |
| `ebullion-doj-fbi-seizure-2008-08` | `admitted` | `human_reviewed` | 2026-05-20 | 12 | ok | 2026-05-20 | 12 | ok | ok |
| `ecuador-national-assembly-bitcoin-ban-2014-07` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-31 | 1 | ok | no_audit_recorded |
| `egold-doj-guilty-plea-2008-07` | `admitted` | `human_reviewed` | 2026-05-20 | 12 | ok | 2026-05-20 | 12 | ok | ok |
| `egold-doj-indictment-2007-04` | `admitted` | `human_reviewed` | 2026-05-31 | 1 | ok | 2026-05-31 | 1 | ok | ok |
| `egypt-cbe-banking-law-194-2020` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-31 | 1 | ok | no_audit_recorded |
| `ens-eth-domain-tornado-resolution-2022` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-21 | 11 | ok | no_audit_recorded |
| `etherscan-tornado-cash-ui-label-2022` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-17 | 15 | ok | no_audit_recorded |
| `etoro-us-ada-trx-delisting-2021-12` | `admitted` | `human_reviewed` | 2026-05-31 | 1 | ok | 2026-05-31 | 1 | ok | ok |
| `eu-12th-russia-sanctions-2023` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-22 | 40 | ok | no_audit_recorded |
| `eu-14th-russia-sanctions-spfs-2024` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-21 | 11 | ok | no_audit_recorded |
| `eu-15th-russia-sanctions-2024` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-21 | 11 | ok | no_audit_recorded |
| `eu-16th-russia-sanctions-2025` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-31 | 1 | ok | no_audit_recorded |
| `eu-18th-russia-sanctions-casp-spfs-2025` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-31 | 1 | ok | no_audit_recorded |
| `eu-19th-russia-sanctions-a7a5-crypto-ban-2025` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-31 | 1 | ok | no_audit_recorded |
| `eu-20th-russia-sanctions-crypto-sectoral-ban-2026` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-31 | 1 | ok | no_audit_recorded |
| `eu-8th-package-russia-crypto-services-ban-2022-10` | `admitted` | `human_reviewed` | 2026-05-31 | 1 | ok | 2026-05-31 | 1 | ok | ok |
| `eu-amla-anti-money-laundering-authority-regulation-2024` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-21 | 11 | ok | no_audit_recorded |
| `eu-amlr-eu-single-rulebook-2024` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-21 | 11 | ok | no_audit_recorded |
| `eu-belarus-crypto-services-ban-2022` | `admitted` | `human_reviewed` | 2026-05-21 | 11 | ok | 2026-05-21 | 11 | ok | ok |
| `eu-dac8-crypto-asset-reporting-directive-2023` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-21 | 11 | ok | no_audit_recorded |
| `eu-mica-2023` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-22 | 40 | ok | no_audit_recorded |
| `eu-russia-crypto-wallet-cap-2022` | `admitted` | `human_reviewed` | 2026-05-16 | 16 | ok | 2026-05-16 | 16 | ok | ok |
| `eu-russia-full-crypto-wallet-ban-2022` | `admitted` | `human_reviewed` | 2026-05-16 | 16 | ok | 2026-05-16 | 16 | ok | ok |
| `eu-tfr-recast-2023` | `admitted` | `human_reviewed` | 2026-05-16 | 16 | ok | 2026-05-16 | 16 | ok | ok |
| `evil-corp-ofac-2024-10` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-31 | 1 | ok | no_audit_recorded |
| `fatf-grey-list-crypto-related-actions-2023-2024` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-21 | 11 | ok | no_audit_recorded |
| `fatf-r15-vasp-travel-rule-2019` | `admitted` | `human_reviewed` | 2026-05-16 | 16 | ok | 2026-05-16 | 16 | ok | ok |
| `fatf-targeted-update-va-vasp-2021` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-21 | 11 | ok | no_audit_recorded |
| `fatf-targeted-update-va-vasp-2023` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-21 | 11 | ok | no_audit_recorded |
| `fatf-virtual-currencies-key-definitions-2014` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-21 | 11 | ok | no_audit_recorded |
| `fayzimatov-alqaeda-syria-ofac-2021-07` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-31 | 1 | ok | no_audit_recorded |
| `fbi-bitcoin-intelligence-assessment-2012-04` | `rejected` | `human_reviewed` | 2026-05-20 | 12 | ok | 2026-05-20 | 12 | ok | ok |
| `fincen-eric-powers-p2p-exchanger-2019-04` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-31 | 1 | ok | no_audit_recorded |
| `fincen-virtual-currency-msb-guidance-2013` | `admitted` | `human_reviewed` | 2026-05-20 | 12 | ok | 2026-05-20 | 12 | ok | ok |
| `france-amf-binance-psan-2022` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-21 | 11 | ok | no_audit_recorded |
| `fsb-crypto-asset-recommendations-2023` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-21 | 11 | ok | no_audit_recorded |
| `ftx-bankman-fried-doj-2022` | `admitted` | `human_reviewed` | 2026-05-16 | 16 | ok | 2026-05-16 | 16 | ok | ok |
| `funnull-cdn-ofac-2025` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-22 | 40 | ok | no_audit_recorded |
| `g20-roadmap-crypto-asset-policy-2023` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-21 | 11 | ok | no_audit_recorded |
| `g7-hiroshima-crypto-statement-2023` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-21 | 11 | ok | no_audit_recorded |
| `garantex-besciokov-mira-serda-doj-2025` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-31 | 1 | ok | no_audit_recorded |
| `garantex-ofac-2022` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-21 | 41 | ok | no_audit_recorded |
| `gate-io-privacy-coin-perpetuals-delisting-2024-12` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-31 | 1 | ok | no_audit_recorded |
| `gemini-netherlands-exit-2023-11` | `admitted` | `human_reviewed` | 2026-05-31 | 1 | ok | 2026-05-31 | 1 | ok | ok |
| `genesis-market-ofac-2023-04` | `admitted` | `human_reviewed` | 2026-05-31 | 1 | ok | 2026-05-31 | 1 | ok | ok |
| `genesis-sec-gemini-earn-2023` | `admitted` | `human_reviewed` | 2026-05-16 | 16 | ok | 2026-05-16 | 16 | ok | ok |
| `germany-bafin-binance-licence-withdrawal-2023` | `admitted` | `human_reviewed` | 2026-05-16 | 16 | ok | 2026-06-01 | 0 | ok | ok |
| `goldage-ny-state-indictment-2006-07` | `rejected` | `agent_draft` | — | — | no_audit_recorded | 2026-05-31 | 1 | ok | no_audit_recorded |
| `google-play-india-crypto-exchange-removal-2024-01` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-21 | 11 | ok | no_audit_recorded |
| `grinex-garantex-successor-ofac-2025` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-21 | 41 | ok | no_audit_recorded |
| `hanafin-huriya-russia-evasion-ofac-2023-05` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-31 | 1 | ok | no_audit_recorded |
| `helix-doj-mixer-2020` | `admitted` | `human_reviewed` | 2026-05-16 | 16 | ok | 2026-05-16 | 16 | ok | ok |
| `hongkong-hkma-stablecoins-ordinance-2025` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-21 | 11 | ok | no_audit_recorded |
| `hongkong-sfc-bybit-warning-2024` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-21 | 11 | ok | no_audit_recorded |
| `hongkong-sfc-jpex-block-2023` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-21 | 11 | ok | no_audit_recorded |
| `hongkong-sfc-vatp-licensing-2023-06` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-21 | 11 | ok | no_audit_recorded |
| `huobi-htx-privacy-coin-delisting-2024` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-06-01 | 0 | ok | no_audit_recorded |
| `hydra-doj-2022` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-22 | 40 | ok | no_audit_recorded |
| `hydra-ofac-2022` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-21 | 41 | ok | no_audit_recorded |
| `iceland-cbi-foreign-exchange-bitcoin-2014` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-16 | 16 | ok | no_audit_recorded |
| `india-fiu-offshore-vda-block-2023` | `admitted` | `human_reviewed` | 2026-05-16 | 16 | ok | 2026-06-01 | 0 | ok | ok |
| `india-rbi-crypto-ban-2018` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-22 | 40 | ok | no_audit_recorded |
| `indonesia-bappebti-illegal-exchange-block-2023` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-21 | 11 | ok | no_audit_recorded |
| `indonesia-bi-bitcoin-warning-2014` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-21 | 11 | ok | no_audit_recorded |
| `indonesia-bi-payment-instrument-prohibition-2018-01` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-31 | 1 | ok | no_audit_recorded |
| `indonesia-kominfo-exchange-social-account-block-2024-07` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-31 | 1 | ok | no_audit_recorded |
| `infura-alchemy-tornado-rpc-block-2022` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-06-01 | 0 | ok | no_audit_recorded |
| `infura-metamask-donetsk-luhansk-block-2022-03` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-21 | 11 | ok | no_audit_recorded |
| `iran-cbi-crypto-banking-prohibition-2018` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-21 | 11 | ok | no_audit_recorded |
| `iran-cbi-exchange-payment-gateway-block-2024-12` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-31 | 1 | ok | no_audit_recorded |
| `iran-government-mining-electricity-restriction-2021` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-21 | 11 | ok | no_audit_recorded |
| `iran-ransomware-ofac-2018` | `admitted` | `human_authored` | 2026-05-15 | 17 | ok | 2026-04-22 | 40 | ok | ok |
| `iraq-cbi-cryptocurrency-prohibition-2017-12` | `rejected` | `agent_draft` | — | — | no_audit_recorded | 2026-05-31 | 1 | ok | no_audit_recorded |
| `irgc-ransomware-ofac-2022` | `admitted` | `human_authored` | 2026-05-15 | 17 | ok | 2026-04-22 | 40 | ok | ok |
| `israel-nbctf-hamas-crypto-addresses-2021` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-21 | 11 | ok | no_audit_recorded |
| `japan-fsa-binance-sakura-acquisition-2022-11` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-21 | 11 | ok | no_audit_recorded |
| `japan-fsa-binance-warning-2018` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-21 | 11 | ok | no_audit_recorded |
| `japan-fsa-coincheck-orders-2018` | `admitted` | `human_reviewed` | 2026-05-16 | 16 | ok | 2026-06-01 | 0 | ok | ok |
| `japan-fsa-dmm-bitcoin-order-2024-09` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-21 | 11 | ok | no_audit_recorded |
| `japan-fsa-ftx-japan-suspension-2022-11` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-21 | 11 | ok | no_audit_recorded |
| `japan-fsa-margin-leverage-cap-2x-2020-05` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-06-01 | 0 | ok | no_audit_recorded |
| `japan-fsa-six-exchange-orders-2018-06` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-21 | 11 | ok | no_audit_recorded |
| `japan-fsa-stablecoin-psa-effective-2023-06` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-16 | 16 | ok | no_audit_recorded |
| `japan-fsa-travel-rule-effective-2023-06` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-21 | 11 | ok | no_audit_recorded |
| `japan-fsa-zaif-orders-2018-09` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-21 | 11 | ok | no_audit_recorded |
| `jordan-cbj-bank-crypto-prohibition-2014` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-31 | 1 | ok | no_audit_recorded |
| `karpeles-arrest-tokyo-mtgox-2015` | `admitted` | `human_reviewed` | 2026-05-20 | 12 | ok | 2026-05-20 | 12 | ok | ok |
| `kazakhstan-digital-assets-law-2023-02` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-21 | 11 | ok | no_audit_recorded |
| `kazakhstan-internet-shutdown-mining-2022-01` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-21 | 11 | ok | no_audit_recorded |
| `kb-vostok-russia-drone-ofac-2024-08` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-31 | 1 | ok | no_audit_recorded |
| `kenya-cbk-virtual-currency-circular-2015-12` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-31 | 1 | ok | no_audit_recorded |
| `kingdom-trust-fincen-2021` | `admitted` | `human_reviewed` | 2026-05-20 | 12 | ok | 2026-05-20 | 12 | ok | ok |
| `korea-fiu-isms-real-name-exchange-shutdown-2021-09` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-31 | 1 | ok | no_audit_recorded |
| `korea-fsc-ico-ban-2017` | `admitted` | `human_reviewed` | 2026-05-16 | 16 | ok | 2026-06-01 | 0 | ok | ok |
| `korea-fsc-institutional-restriction-2017` | `admitted` | `human_reviewed` | 2026-05-17 | 15 | ok | 2026-05-21 | 11 | ok | ok |
| `korea-fsc-privacy-coin-delisting-mandate-2021-03` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-31 | 1 | ok | no_audit_recorded |
| `korea-travel-rule-2022` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-22 | 40 | ok | no_audit_recorded |
| `kraken-monero-eu-delisting-2024` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-17 | 15 | ok | no_audit_recorded |
| `kraken-sec-staking-2023` | `admitted` | `human_reviewed` | 2026-05-16 | 16 | ok | 2026-05-16 | 16 | ok | ok |
| `kraken-sec-unregistered-exchange-2023` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-06-01 | 0 | ok | no_audit_recorded |
| `kraken-uk-derivatives-exit-2021` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-17 | 15 | ok | no_audit_recorded |
| `kucoin-canada-exit-2023` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-17 | 15 | ok | no_audit_recorded |
| `kucoin-doj-2024` | `admitted` | `human_reviewed` | 2026-05-16 | 16 | ok | 2026-05-16 | 16 | ok | ok |
| `kucoin-netherlands-exit-2023` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-21 | 11 | ok | no_audit_recorded |
| `kuwait-cma-virtual-assets-prohibition-2023-07` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-31 | 1 | ok | no_audit_recorded |
| `kyrgyzstan-nbkr-virtual-currency-payment-warning-2014-07` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-31 | 1 | ok | no_audit_recorded |
| `lazarus-entity-ofac-2019` | `admitted` | `human_authored` | 2026-05-15 | 17 | ok | 2026-04-22 | 40 | ok | ok |
| `lazarus-laundering-ofac-2020` | `admitted` | `human_authored` | 2026-05-15 | 17 | ok | 2026-04-22 | 40 | ok | ok |
| `lebanon-bdl-bitcoin-warning-2013-12` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-31 | 1 | ok | no_audit_recorded |
| `liberty-reserve-coordinated-takedown-2013-05` | `admitted` | `human_reviewed` | 2026-05-31 | 1 | ok | 2026-05-31 | 1 | ok | ok |
| `liberty-reserve-costa-rica-license-denial-2011-03` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-21 | 11 | ok | no_audit_recorded |
| `lockbit-affiliates-ofac-2024` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-22 | 40 | ok | no_audit_recorded |
| `lockbit-leader-ofac-2024` | `admitted` | `human_authored` | 2026-05-15 | 17 | ok | 2026-04-22 | 40 | ok | ok |
| `magic-eden-ofac-sanctioned-country-block` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-06-01 | 0 | ok | no_audit_recorded |
| `makerdao-emergency-shutdown-contingency-2022-08` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-21 | 11 | ok | no_audit_recorded |
| `malaysia-sc-binance-disable-2021` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-06-01 | 0 | ok | no_audit_recorded |
| `matveev-ofac-2023` | `admitted` | `human_authored` | 2026-05-15 | 17 | ok | 2026-04-22 | 40 | ok | ok |
| `media-land-volosovik-bulletproof-ofac-2025-11` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-31 | 1 | ok | no_audit_recorded |
| `metamask-eth-phishing-detect-tornado-additions-2022` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-17 | 15 | ok | no_audit_recorded |
| `metamask-snaps-region-restrictions-2023-09` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-17 | 15 | ok | no_audit_recorded |
| `mica-l2-esma-eba-rts-2024` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-21 | 11 | ok | no_audit_recorded |
| `morocco-office-des-changes-crypto-ban-2017-11` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-31 | 1 | ok | no_audit_recorded |
| `mtgox-bankruptcy-tokyo-2014` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-21 | 11 | ok | no_audit_recorded |
| `mtgox-coinlab-civil-2013` | `admitted` | `human_reviewed` | 2026-05-20 | 12 | ok | 2026-05-20 | 12 | ok | ok |
| `mtgox-dhs-dwolla-wells-fargo-seizure-2013` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-20 | 12 | ok | no_audit_recorded |
| `mtgox-june-2011-hack-trading-suspension` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-21 | 11 | ok | no_audit_recorded |
| `mtgox-mizuho-wire-pressure-2012` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-21 | 11 | ok | no_audit_recorded |
| `mtgox-usd-withdrawal-suspension-2013-06` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-21 | 11 | ok | no_audit_recorded |
| `myanmar-cbm-crypto-prohibition-directive-9-2020` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-31 | 1 | ok | no_audit_recorded |
| `nemesis-parsarad-darknet-ofac-2025-03` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-31 | 1 | ok | no_audit_recorded |
| `nepal-nrb-bitcoin-ban-2017-08` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-31 | 1 | ok | no_audit_recorded |
| `nepal-nrb-comprehensive-crypto-ban-2021-09` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-31 | 1 | ok | no_audit_recorded |
| `netex24-bitpapa-russia-crypto-ofac-2024-03` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-31 | 1 | ok | no_audit_recorded |
| `netherlands-dnb-binance-warning-2021` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-06-01 | 0 | ok | no_audit_recorded |
| `netwalker-vachon-desjardins-doj-2022` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-31 | 1 | ok | no_audit_recorded |
| `nigeria-binance-network-block-2024-02` | `admitted` | `human_reviewed` | 2026-05-31 | 1 | ok | 2026-05-31 | 1 | ok | ok |
| `nigeria-cbn-crypto-ban-2021` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-22 | 40 | ok | no_audit_recorded |
| `nydfs-bitlicense-2015-06` | `admitted` | `human_reviewed` | 2026-05-16 | 16 | ok | 2026-05-16 | 16 | ok | ok |
| `nydfs-bitlicense-bitfinex-kraken-shapeshift-exit-2015` | `rejected` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-20 | 12 | ok | no_audit_recorded |
| `nydfs-bittrex-bitlicense-denial-2019-04` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-31 | 1 | ok | no_audit_recorded |
| `oasis-app-wormhole-counter-exploit-2023-02` | `rejected` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-20 | 12 | ok | no_audit_recorded |
| `oecd-carf-2022` | `admitted` | `human_reviewed` | 2026-05-16 | 16 | ok | 2026-05-16 | 16 | ok | ok |
| `ofac-dprk-it-worker-sim-hyon-sop-2023-04` | `admitted` | `human_reviewed` | 2026-05-20 | 12 | ok | 2026-05-20 | 12 | ok | ok |
| `ofac-hamas-buy-cash-msb-2023-10` | `admitted` | `human_reviewed` | 2026-05-20 | 12 | ok | 2026-05-20 | 12 | ok | ok |
| `ofac-hamas-gaza-now-2024-03` | `admitted` | `human_reviewed` | 2026-05-20 | 12 | ok | 2026-05-20 | 12 | ok | ok |
| `ofac-hamas-irgc-virtual-currency-network-2024-01` | `rejected` | `human_reviewed` | 2026-05-20 | 12 | ok | 2026-05-20 | 12 | ok | ok |
| `ofac-houthi-al-jamal-crypto-refresh-2024-12` | `admitted` | `human_reviewed` | 2026-05-20 | 12 | ok | 2026-05-20 | 12 | ok | ok |
| `ofac-recent-action-20240111` | `admitted` | `human_reviewed` | 2026-05-20 | 12 | ok | 2026-05-20 | 12 | ok | ok |
| `ofac-trickbot-conti-eleven-2023-09` | `admitted` | `human_reviewed` | 2026-05-20 | 12 | ok | 2026-05-20 | 12 | ok | ok |
| `ofac-zhdanova-russian-elite-launderer-2023-11` | `admitted` | `human_reviewed` | 2026-05-20 | 12 | ok | 2026-05-20 | 12 | ok | ok |
| `okex-privacy-coin-delisting-2019-09` | `admitted` | `human_reviewed` | 2026-05-31 | 1 | ok | 2026-05-31 | 1 | ok | ok |
| `oko-design-bureau-russia-drone-ofac-2024-05` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-31 | 1 | ok | no_audit_recorded |
| `okx-aux-cayes-doj-guilty-plea-2025` | `admitted` | `human_reviewed` | 2026-05-31 | 1 | ok | 2026-05-31 | 1 | ok | ok |
| `okx-canada-exit-2023` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-31 | 1 | ok | no_audit_recorded |
| `okx-india-exit-2024-03` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-31 | 1 | ok | no_audit_recorded |
| `okx-monero-global-delisting-2024` | `rejected` | `agent_draft` | — | — | no_audit_recorded | 2026-05-17 | 15 | ok | no_audit_recorded |
| `okx-nigeria-exit-2024-08` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-31 | 1 | ok | no_audit_recorded |
| `okx-privacy-token-delist-2024` | `admitted` | `human_reviewed` | 2026-05-16 | 16 | ok | 2026-05-16 | 16 | ok | ok |
| `opensea-iran-cuba-sanctions-block-2022` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-06-01 | 0 | ok | no_audit_recorded |
| `orca-dex-us-frontend-block-2023-03` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-31 | 1 | ok | no_audit_recorded |
| `pakistan-sbp-crypto-prohibition-2018-04` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-31 | 1 | ok | no_audit_recorded |
| `pancakeswap-sanctioned-country-frontend-geofence-2022` | `admitted` | `human_reviewed` | 2026-05-31 | 1 | ok | 2026-05-31 | 1 | ok | ok |
| `paxos-busd-nydfs-minting-stop-2023` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-21 | 11 | ok | no_audit_recorded |
| `paxos-canada-exit-2023-04` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-31 | 1 | ok | no_audit_recorded |
| `pecunix-bullion-transfer-2008` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-21 | 11 | ok | no_audit_recorded |
| `pertsev-nl-arrest-2022` | `admitted` | `human_authored` | 2026-05-15 | 17 | ok | 2026-04-22 | 40 | ok | ok |
| `philippines-bsp-vasp-license-moratorium-2022-09` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-31 | 1 | ok | no_audit_recorded |
| `philippines-sec-binance-block-2024` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-21 | 11 | ok | no_audit_recorded |
| `poloniex-circle-us-token-geofence-2019-05` | `admitted` | `human_reviewed` | 2026-05-31 | 1 | ok | 2026-05-31 | 1 | ok | ok |
| `polymarket-cftc-geofence-2022-01` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-20 | 12 | ok | no_audit_recorded |
| `polynonce-bittrex-fincen-2022` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-20 | 12 | ok | no_audit_recorded |
| `powell-unlicensed-bitcoin-exchange-2014` | `admitted` | `human_reviewed` | 2026-05-16 | 16 | ok | 2026-05-16 | 16 | ok | ok |
| `prince-group-chen-zhi-ofac-2025-10` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-31 | 1 | ok | no_audit_recorded |
| `pump-fun-uk-fca-geofence-2024-12` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-17 | 15 | ok | no_audit_recorded |
| `qatar-qcb-qfcra-virtual-asset-ban-2019-12` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-31 | 1 | ok | no_audit_recorded |
| `ren-protocol-shutdown-alameda-ftx-2022-12` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-17 | 15 | ok | no_audit_recorded |
| `revil-vasinskyi-polyanin-doj-2021` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-31 | 1 | ok | no_audit_recorded |
| `ripple-fincen-xrp-2015` | `admitted` | `human_reviewed` | 2026-05-16 | 16 | ok | 2026-05-16 | 16 | ok | ok |
| `russia-cbr-bitcoin-information-letter-2014` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-21 | 11 | ok | no_audit_recorded |
| `russia-cbr-crypto-payment-ban-2022` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-21 | 11 | ok | no_audit_recorded |
| `russia-dfa-law-2020` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-21 | 11 | ok | no_audit_recorded |
| `russia-election-interference-ofac-2020` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-22 | 40 | ok | no_audit_recorded |
| `russia-mining-legalization-law-2024-08` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-21 | 11 | ok | no_audit_recorded |
| `russia-mining-regional-ban-2024-12` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-21 | 11 | ok | no_audit_recorded |
| `russia-rosfinmonitoring-binance-russia-rails-2022` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-21 | 11 | ok | no_audit_recorded |
| `russian-cyber-theft-ofac-2020` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-22 | 40 | ok | no_audit_recorded |
| `russian-cybercrime-infra-ofac-2025` | `admitted` | `human_authored` | 2026-05-15 | 17 | ok | 2026-04-22 | 40 | ok | ok |
| `salame-ftx-campaign-finance-doj-2023` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-20 | 12 | ok | no_audit_recorded |
| `samourai-doj-2024` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-22 | 40 | ok | no_audit_recorded |
| `saudi-standing-committee-virtual-currency-warning-2018-08` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-31 | 1 | ok | no_audit_recorded |
| `sec-abra-plutus-earn-cease-2024-08` | `admitted` | `human_reviewed` | 2026-05-31 | 1 | ok | 2026-05-31 | 1 | ok | ok |
| `sec-beaxy-platform-shutdown-2023` | `admitted` | `human_reviewed` | 2026-05-16 | 16 | ok | 2026-05-16 | 16 | ok | ok |
| `sec-burnside-bitcoin-stock-exchange-2014` | `admitted` | `human_reviewed` | 2026-05-16 | 16 | ok | 2026-05-16 | 16 | ok | ok |
| `sec-consensys-metamask-staking-swaps-2024-06` | `admitted` | `human_reviewed` | 2026-05-31 | 1 | ok | 2026-05-31 | 1 | ok | ok |
| `sec-etherdelta-coburn-unregistered-exchange-2018-11` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-31 | 1 | ok | no_audit_recorded |
| `sec-etoro-cease-crypto-trading-2024-09` | `admitted` | `human_reviewed` | 2026-05-31 | 1 | ok | 2026-05-31 | 1 | ok | ok |
| `sec-garza-gaw-miners-zenminer-2015` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-20 | 12 | ok | no_audit_recorded |
| `sec-kik-interactive-kin-unregistered-offering-2020-10` | `admitted` | `human_reviewed` | 2026-05-31 | 1 | ok | 2026-05-31 | 1 | ok | ok |
| `sec-lbry-lbc-unregistered-securities-2021-03` | `admitted` | `human_reviewed` | 2026-05-31 | 1 | ok | 2026-05-31 | 1 | ok | ok |
| `sec-nexo-earn-lending-product-cease-2023-01` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-31 | 1 | ok | no_audit_recorded |
| `sec-poloniex-unregistered-exchange-2021-08` | `admitted` | `human_reviewed` | 2026-05-31 | 1 | ok | 2026-05-31 | 1 | ok | ok |
| `sec-shavers-btcst-2013` | `admitted` | `human_reviewed` | 2026-05-16 | 16 | ok | 2026-05-16 | 16 | ok | ok |
| `sec-tokenlot-unregistered-broker-2018-09` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-31 | 1 | ok | no_audit_recorded |
| `sec-tradestation-crypto-lending-cease-2024-02` | `admitted` | `human_reviewed` | 2026-05-31 | 1 | ok | 2026-05-31 | 1 | ok | ok |
| `sec-v-binance-2023` | `admitted` | `human_authored` | 2026-05-06 | 26 | ok | 2026-05-06 | 26 | ok | ok |
| `sec-v-bittrex-2023` | `admitted` | `human_reviewed` | 2026-05-16 | 16 | ok | 2026-05-16 | 16 | ok | ok |
| `sec-v-coinbase-2023` | `admitted` | `human_authored` | 2026-05-06 | 26 | ok | 2026-05-06 | 26 | ok | ok |
| `sec-v-coinbase-staking-wells-2023` | `rejected` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-21 | 11 | ok | no_audit_recorded |
| `sec-v-ftx-2022` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-21 | 11 | ok | no_audit_recorded |
| `sec-v-ripple-2020` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-06-01 | 0 | ok | no_audit_recorded |
| `sec-v-telegram-ton-2020` | `admitted` | `human_reviewed` | 2026-05-16 | 16 | ok | 2026-05-16 | 16 | ok | ok |
| `sec-v-uniswap-wells-notice-2024` | `rejected` | `human_authored` | — | — | no_audit_recorded | 2026-05-06 | 26 | ok | no_audit_recorded |
| `sec-voorhees-satoshidice-2014` | `admitted` | `human_reviewed` | 2026-05-16 | 16 | ok | 2026-05-16 | 16 | ok | ok |
| `semenov-ofac-2023` | `admitted` | `human_authored` | 2026-04-22 | 40 | ok | 2026-04-21 | 41 | ok | ok |
| `shapeshift-mandatory-kyc-anonymity-end-2018-09` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-31 | 1 | ok | no_audit_recorded |
| `shrem-faiella-bitcoin-exchange-2014` | `admitted` | `human_reviewed` | 2026-05-16 | 16 | ok | 2026-05-16 | 16 | ok | ok |
| `sichuan-silence-ofac-2024` | `admitted` | `human_authored` | 2026-05-15 | 17 | ok | 2026-04-22 | 40 | ok | ok |
| `silk-road-doj-seizure-2013` | `admitted` | `human_reviewed` | 2026-05-16 | 16 | ok | 2026-05-16 | 16 | ok | ok |
| `sinbad-doj-2024` | `admitted` | `human_reviewed` | 2026-05-16 | 16 | ok | 2026-05-16 | 16 | ok | ok |
| `sinbad-ofac-2023` | `admitted` | `human_authored` | 2026-05-15 | 17 | ok | 2026-04-21 | 41 | ok | ok |
| `singapore-mas-binance-services-2021` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-06-01 | 0 | ok | no_audit_recorded |
| `singapore-mas-retail-crypto-restriction-2022` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-21 | 11 | ok | no_audit_recorded |
| `south-africa-fsca-crypto-financial-product-2022` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-21 | 11 | ok | no_audit_recorded |
| `sri-lanka-cbsl-crypto-warning-fx-directive-2021` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-31 | 1 | ok | no_audit_recorded |
| `storm-semenov-doj-2023` | `admitted` | `human_authored` | 2026-05-15 | 17 | ok | 2026-04-22 | 40 | ok | ok |
| `suex-ofac-2021` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-21 | 41 | ok | no_audit_recorded |
| `switzerland-finma-tezos-zg-2018` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-21 | 11 | ok | no_audit_recorded |
| `t3-bybit-hack-usdt-freeze-2025-03` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-06-01 | 0 | ok | no_audit_recorded |
| `t3-financial-crime-unit-launch-2024-09` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-31 | 1 | ok | no_audit_recorded |
| `taiwan-fsc-aml-vasp-regime-2021-2024` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-31 | 1 | ok | no_audit_recorded |
| `taiwan-fsc-bitcoin-bank-atm-ban-2014-01` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-31 | 1 | ok | no_audit_recorded |
| `task-force-rusich-ofac-2022-09` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-31 | 1 | ok | no_audit_recorded |
| `tengyue-chemical-fentanyl-ofac-2025-09` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-31 | 1 | ok | no_audit_recorded |
| `teraexchange-cftc-bitcoin-swap-2015` | `admitted` | `human_reviewed` | 2026-05-16 | 16 | ok | 2026-05-16 | 16 | ok | ok |
| `terror-financing-crypto-seizure-doj-2020` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-31 | 1 | ok | no_audit_recorded |
| `tether-doj-pig-butchering-freeze-2023` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-22 | 40 | ok | no_audit_recorded |
| `tether-dprk-precommit-freeze-2025` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-22 | 40 | ok | no_audit_recorded |
| `tether-garantex-usdt-freeze-2025-03` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-31 | 1 | ok | no_audit_recorded |
| `tether-ofac-iran-economic-fury-344m-freeze-2026-04` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-31 | 1 | ok | no_audit_recorded |
| `tether-okx-doj-pig-butchering-225m-freeze-2025-06` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-31 | 1 | ok | no_audit_recorded |
| `tether-pig-butchering-second-wave-2024` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-21 | 11 | ok | no_audit_recorded |
| `tether-retroactive-sweep-2023` | `admitted` | `human_authored` | 2026-04-22 | 40 | ok | 2026-04-22 | 40 | ok | ok |
| `tether-tron-philippines-pdea-freeze-2024` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-21 | 11 | ok | no_audit_recorded |
| `thailand-bot-bitcoin-prohibition-2013` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-21 | 11 | ok | no_audit_recorded |
| `thailand-sec-binance-bybit-c-and-d-2021` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-21 | 11 | ok | no_audit_recorded |
| `thailand-sec-crypto-payment-ban-2022-04` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-31 | 1 | ok | no_audit_recorded |
| `thailand-sec-meme-fan-nft-exchange-token-ban-2021-06` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-31 | 1 | ok | no_audit_recorded |
| `tornado-cash-frontend-tornado-cash-eth-block-2022-04` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-17 | 15 | ok | no_audit_recorded |
| `tornado-cash-github-takedown-2022-08` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-17 | 15 | ok | no_audit_recorded |
| `tornado-cash-ofac-2022` | `admitted` | `human_authored` | 2026-04-22 | 40 | ok | 2026-04-21 | 41 | ok | ok |
| `tornado-cash-ofac-delisting-2025` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-21 | 41 | ok | no_audit_recorded |
| `tornado-cash-ofac-redesignation-2022` | `admitted` | `human_authored` | 2026-04-22 | 40 | ok | 2026-04-21 | 41 | ok | ok |
| `tornado-cash-pertsev-doj-indictment-2023` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-21 | 11 | ok | no_audit_recorded |
| `tornado-cash-storm-conviction-2025` | `admitted` | `human_reviewed` | 2026-05-16 | 16 | ok | 2026-05-16 | 16 | ok | ok |
| `tornado-cash-tornadocash-org-seizure-2022` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-17 | 15 | ok | no_audit_recorded |
| `tradehill-dwolla-payment-cutoff-2012-02` | `admitted` | `human_reviewed` | 2026-05-31 | 1 | ok | 2026-05-31 | 1 | ok | ok |
| `trustwallet-sanctioned-token-ui-update-2022` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-21 | 11 | ok | no_audit_recorded |
| `turkey-cbrt-crypto-ban-2021` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-22 | 40 | ok | no_audit_recorded |
| `turkey-cmb-casp-licensing-law-7518-2024` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-21 | 11 | ok | no_audit_recorded |
| `uae-sca-crypto-asset-activities-regulation-decision-23-2020` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-31 | 1 | ok | no_audit_recorded |
| `uae-vara-licence-issuance-regime-2023` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-21 | 11 | ok | no_audit_recorded |
| `uk-fca-binance-markets-2021` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-06-01 | 0 | ok | no_audit_recorded |
| `uk-fca-crypto-promotion-rule-2023` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-21 | 11 | ok | no_audit_recorded |
| `uk-hmrc-bitcoin-vat-brief-09-14-2014` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-21 | 11 | ok | no_audit_recorded |
| `ukraine-virtual-assets-law-2022-03` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-21 | 11 | ok | no_audit_recorded |
| `uniswap-balancer-tornado-frontend-block-2022-08` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-21 | 11 | ok | no_audit_recorded |
| `uniswap-frontend-delisting-2023` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-22 | 40 | ok | no_audit_recorded |
| `uniswap-token-list-curation-default-2021` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-21 | 11 | ok | no_audit_recorded |
| `uniswap-tokenized-stocks-delisting-2021-07` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-21 | 11 | ok | no_audit_recorded |
| `unsc-resolution-2371-dprk-crypto-2017` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-21 | 11 | ok | no_audit_recorded |
| `upbit-bithumb-regulatory-delisting-purge-2021-06` | `admitted` | `human_reviewed` | 2026-05-31 | 1 | ok | 2026-05-31 | 1 | ok | ok |
| `upbit-privacy-coin-delisting-2019-09` | `admitted` | `human_reviewed` | 2026-05-31 | 1 | ok | 2026-05-31 | 1 | ok | ok |
| `uzbekistan-napp-vasp-licensing-2022-07` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-21 | 11 | ok | no_audit_recorded |
| `venezuela-sunacrip-mining-exchange-halt-2023-03` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-31 | 1 | ok | no_audit_recorded |
| `vietnam-sbv-bitcoin-prohibition-statement-2014-02` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-31 | 1 | ok | no_audit_recorded |
| `vietnam-sbv-payment-prohibition-2017-10` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-31 | 1 | ok | no_audit_recorded |
| `voyager-bankruptcy-doj-objection-2023` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-21 | 11 | ok | no_audit_recorded |
| `wang-hongfei-fentanyl-precursor-ofac-2023-04` | `admitted` | `human_reviewed` | 2026-05-31 | 1 | ok | 2026-05-31 | 1 | ok | ok |
| `webmoney-ukraine-tax-police-freeze-2013-06` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-31 | 1 | ok | no_audit_recorded |
| `welcome-to-video-doj-2019` | `admitted` | `human_reviewed` | 2026-05-16 | 16 | ok | 2026-05-16 | 16 | ok | ok |
| `wikileaks-amazon-aws-eviction-2010-12` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-21 | 11 | ok | no_audit_recorded |
| `wikileaks-bank-of-america-block-2010-12` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-21 | 11 | ok | no_audit_recorded |
| `wikileaks-everydns-domain-termination-2010-12` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-21 | 11 | ok | no_audit_recorded |
| `wikileaks-mastercard-suspension-2010-12` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-21 | 11 | ok | no_audit_recorded |
| `wikileaks-paypal-freeze-2010-12` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-21 | 11 | ok | no_audit_recorded |
| `wikileaks-postfinance-account-closure-2010-12` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-21 | 11 | ok | no_audit_recorded |
| `wikileaks-visa-europe-suspension-2010-12` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-21 | 11 | ok | no_audit_recorded |
| `wikileaks-wau-holland-tax-status-challenge-2010-12` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-21 | 11 | ok | no_audit_recorded |
| `wikileaks-western-union-interdiction-2010-12` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-21 | 11 | ok | no_audit_recorded |
| `zheng-yan-fentanyl-ofac-2019-08` | `admitted` | `human_reviewed` | 2026-05-31 | 1 | ok | 2026-05-31 | 1 | ok | ok |
| `zimbabwe-rbz-circular-2-2018-golix-ban` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-31 | 1 | ok | no_audit_recorded |
| `zimbabwe-rbz-circular-2-2018-golix` | `admitted` | `human_reviewed` | — | — | no_audit_recorded | 2026-05-31 | 1 | ok | no_audit_recorded |
| `zservers-ofac-2025` | `admitted` | `human_authored` | 2026-05-15 | 17 | ok | 2026-04-22 | 40 | ok | ok |

## Events flagged (any non-`ok` summary)

- `1inch-us-geofence-2021-09` — audit=no_audit_recorded, verification=ok, verif_age=11d
- `1mdc-egold-account-freeze-2007-04` — audit=no_audit_recorded, verification=ok, verif_age=1d
- `aave-arc-fireblocks-whitelist-2022-01` — audit=no_audit_recorded, verification=ok, verif_age=11d
- `aave-tornado-frontend-block-2022-08` — audit=no_audit_recorded, verification=ok, verif_age=11d
- `aeza-group-ofac-2025` — audit=no_audit_recorded, verification=ok, verif_age=40d
- `al-law-hezbollah-crypto-ofac-2024-03` — audit=no_audit_recorded, verification=ok, verif_age=1d
- `algeria-finance-law-2018-crypto-prohibition` — audit=no_audit_recorded, verification=ok, verif_age=1d
- `apple-india-crypto-exchange-removal-2024-01` — audit=no_audit_recorded, verification=ok, verif_age=11d
- `apple-uniswap-wallet-app-store-rejection-2023-03` — audit=no_audit_recorded, verification=ok, verif_age=1d
- `argentina-bcra-banks-crypto-services-ban-2022-05` — audit=no_audit_recorded, verification=ok, verif_age=1d
- `argentina-cnv-psav-registration-2024` — audit=no_audit_recorded, verification=ok, verif_age=11d
- `argentina-uif-resolution-300-2014` — audit=no_audit_recorded, verification=ok, verif_age=11d
- `augur-v2-us-uk-geofence-2020-07` — audit=no_audit_recorded, verification=ok, verif_age=11d
- `bangladesh-bank-fepd-virtual-assets-prohibition-2022-09` — audit=no_audit_recorded, verification=ok, verif_age=1d
- `bangladesh-bb-bitcoin-warning-2014` — audit=no_audit_recorded, verification=ok, verif_age=11d
- `bcbs-cryptoasset-prudential-standard-sco60-2022` — audit=no_audit_recorded, verification=ok, verif_age=1d
- `binance-4framework-2023` — audit=no_audit_recorded, verification=ok, verif_age=40d
- `binance-busd-wind-down-2024` — audit=no_audit_recorded, verification=ok, verif_age=11d
- `binance-eea-usdt-spot-delisting-2025-03` — audit=no_audit_recorded, verification=ok, verif_age=1d
- `binance-monero-global-delisting-2024-02` — audit=no_audit_recorded, verification=ok, verif_age=1d
- `binance-nigeria-naira-services-end-2024-03` — audit=no_audit_recorded, verification=ok, verif_age=1d
- `binance-palestinian-accounts-seizure-israel-2023-11` — audit=no_audit_recorded, verification=ok, verif_age=1d
- `binance-privacy-coin-delisting-2023` — audit=no_audit_recorded, verification=ok, verif_age=0d
- `binance-russia-exit-commex-2023` — audit=no_audit_recorded, verification=ok, verif_age=0d
- `binance-uk-new-user-halt-2023-10` — audit=no_audit_recorded, verification=ok, verif_age=1d
- `binance-us-staking-end-2023` — audit=no_audit_recorded, verification=ok, verif_age=0d
- `bitcoin-fog-sterlingov-doj-2024` — audit=no_audit_recorded, verification=ok, verif_age=1d
- `bitcoin-maven-tetley-doj-2018` — audit=no_audit_recorded, verification=ok, verif_age=1d
- `bitcoinica-shutdown-2012-05` — audit=no_audit_recorded, verification=ok, verif_age=11d
- `bitfinex-tether-nyag-2021` — audit=no_audit_recorded, verification=ok, verif_age=11d
- `bitfinex-us-retail-customer-exit-2017-11` — audit=no_audit_recorded, verification=ok, verif_age=1d
- `bitfloor-capital-one-debanking-2013-04` — audit=no_audit_recorded, verification=ok, verif_age=1d
- `bitstamp-greece-portugal-exit-2023` — audit=no_audit_recorded, verification=ok, verif_age=11d
- `bittrex-global-shutdown-2023-11` — audit=no_audit_recorded, verification=ok, verif_age=1d
- `bitzlato-doj-2023` — audit=no_audit_recorded, verification=ok, verif_age=41d
- `blender-ofac-2022` — audit=no_audit_recorded, verification=ok, verif_age=41d
- `blockfi-multistate-cease-desist-bia-2021-07` — audit=no_audit_recorded, verification=ok, verif_age=1d
- `bolivia-bcb-crypto-prohibition-2014` — audit=no_audit_recorded, verification=ok, verif_age=11d
- `botnet-911-s5-ofac-2024-05` — audit=no_audit_recorded, verification=ok, verif_age=1d
- `brazil-bacen-stablecoin-restriction-2023` — audit=no_audit_recorded, verification=ok, verif_age=11d
- `brazil-bcb-comunicado-25306-2014` — audit=no_audit_recorded, verification=ok, verif_age=11d
- `btc-e-doj-2017` — audit=no_audit_recorded, verification=ok, verif_age=40d
- `bybit-france-exit-2024-12` — audit=no_audit_recorded, verification=ok, verif_age=1d
- `bybit-singapore-exit-2022` — audit=no_audit_recorded, verification=ok, verif_age=15d
- `cambodia-nbc-joint-crypto-prohibition-2018-05` — audit=no_audit_recorded, verification=ok, verif_age=1d
- `canada-convoy-freeze-2022` — audit=no_audit_recorded, verification=ok, verif_age=40d
- `celsius-multistate-cease-desist-earn-2021-09` — audit=no_audit_recorded, verification=ok, verif_age=1d
- `cftc-defi-opyn-zeroex-deridex-2023-09` — audit=no_audit_recorded, verification=ok, verif_age=1d
- `cftc-v-ooki-dao-2022` — audit=no_audit_recorded, verification=ok, verif_age=40d
- `chatex-ofac-2021` — audit=no_audit_recorded, verification=ok, verif_age=40d
- `china-fentanyl-network-ofac-2023-10` — audit=no_audit_recorded, verification=ok, verif_age=1d
- `china-inner-mongolia-mining-ban-2021-05` — audit=no_audit_recorded, verification=ok, verif_age=11d
- `china-ndrc-mining-eliminated-industry-notice-2021-09` — audit=no_audit_recorded, verification=ok, verif_age=1d
- `china-nft-secondary-trading-self-discipline-2022-06` — audit=no_audit_recorded, verification=ok, verif_age=11d
- `china-pboc-banks-alipay-payment-channel-block-2021-06` — audit=no_audit_recorded, verification=ok, verif_age=1d
- `china-pboc-banks-close-exchange-accounts-2014-04` — audit=no_audit_recorded, verification=ok, verif_age=1d
- `china-pboc-crypto-ban-2021` — audit=no_audit_recorded, verification=ok, verif_age=41d
- `china-pboc-exchange-access-block-2019-06` — audit=no_audit_recorded, verification=ok, verif_age=1d
- `china-pboc-exchange-shutdown-2017-09` — audit=no_audit_recorded, verification=ok, verif_age=11d
- `china-search-engine-social-keyword-exchange-block-2021-06` — audit=no_audit_recorded, verification=ok, verif_age=1d
- `china-sichuan-mining-ban-2021-06` — audit=no_audit_recorded, verification=ok, verif_age=11d
- `china-state-council-mining-crackdown-2021-05` — audit=no_audit_recorded, verification=ok, verif_age=11d
- `china-weibo-crypto-exchange-purge-2021-03` — audit=no_audit_recorded, verification=ok, verif_age=11d
- `chinyong-kim-sang-man-dprk-it-worker-ofac-2023-05` — audit=no_audit_recorded, verification=ok, verif_age=1d
- `chipmixer-doj-2023` — audit=no_audit_recorded, verification=ok, verif_age=40d
- `circle-usdc-cryptex-freeze-2024` — audit=no_audit_recorded, verification=ok, verif_age=11d
- `circle-usdc-multichain-hack-freeze-2023-07` — audit=no_audit_recorded, verification=ok, verif_age=1d
- `circle-usdc-sealed-civil-case-16-address-freeze-2026-03` — audit=no_audit_recorded, verification=ok, verif_age=1d
- `circle-usdc-svb-policy-statement-2023` — audit=no_audit_recorded, verification=ok, verif_age=11d
- `circle-usdc-tornado-2022` — audit=no_audit_recorded, verification=ok, verif_age=40d
- `cloudflare-ethereum-gateway-tornado-block-2022-08` — audit=no_audit_recorded, verification=ok, verif_age=11d
- `coinbase-eu-usdt-stablecoin-delisting-2024-12` — audit=no_audit_recorded, verification=ok, verif_age=1d
- `coinbase-india-exit-2022` — audit=no_audit_recorded, verification=ok, verif_age=40d
- `coinbase-japan-exit-2023` — audit=no_audit_recorded, verification=ok, verif_age=11d
- `colonial-pipeline-darkside-ransom-clawback-doj-2021` — audit=no_audit_recorded, verification=ok, verif_age=1d
- `consensys-metamask-infura-rpc-data-collection-2022-11` — audit=no_audit_recorded, verification=ok, verif_age=11d
- `crypto-capital-fowler-doj-2019` — audit=no_audit_recorded, verification=ok, verif_age=1d
- `crypto-com-eu-usdt-stablecoin-delisting-2025-01` — audit=no_audit_recorded, verification=ok, verif_age=1d
- `derakhshan-alivand-irgc-crypto-ofac-2025-09` — audit=no_audit_recorded, verification=ok, verif_age=1d
- `dkba-burma-scam-compound-ofac-2025-11` — audit=no_audit_recorded, verification=ok, verif_age=1d
- `dprk-usdt-network-ofac-2025` — audit=no_audit_recorded, verification=ok, verif_age=40d
- `dydx-canada-frontend-wind-down-2023-04` — audit=no_audit_recorded, verification=ok, verif_age=1d
- `dydx-tornado-account-block-2022-08` — audit=no_audit_recorded, verification=ok, verif_age=11d
- `eba-virtual-currencies-opinion-eba-op-2014-08` — audit=no_audit_recorded, verification=ok, verif_age=11d
- `ecuador-national-assembly-bitcoin-ban-2014-07` — audit=no_audit_recorded, verification=ok, verif_age=1d
- `egypt-cbe-banking-law-194-2020` — audit=no_audit_recorded, verification=ok, verif_age=1d
- `ens-eth-domain-tornado-resolution-2022` — audit=no_audit_recorded, verification=ok, verif_age=11d
- `etherscan-tornado-cash-ui-label-2022` — audit=no_audit_recorded, verification=ok, verif_age=15d
- `eu-12th-russia-sanctions-2023` — audit=no_audit_recorded, verification=ok, verif_age=40d
- `eu-14th-russia-sanctions-spfs-2024` — audit=no_audit_recorded, verification=ok, verif_age=11d
- `eu-15th-russia-sanctions-2024` — audit=no_audit_recorded, verification=ok, verif_age=11d
- `eu-16th-russia-sanctions-2025` — audit=no_audit_recorded, verification=ok, verif_age=1d
- `eu-18th-russia-sanctions-casp-spfs-2025` — audit=no_audit_recorded, verification=ok, verif_age=1d
- `eu-19th-russia-sanctions-a7a5-crypto-ban-2025` — audit=no_audit_recorded, verification=ok, verif_age=1d
- `eu-20th-russia-sanctions-crypto-sectoral-ban-2026` — audit=no_audit_recorded, verification=ok, verif_age=1d
- `eu-amla-anti-money-laundering-authority-regulation-2024` — audit=no_audit_recorded, verification=ok, verif_age=11d
- `eu-amlr-eu-single-rulebook-2024` — audit=no_audit_recorded, verification=ok, verif_age=11d
- `eu-dac8-crypto-asset-reporting-directive-2023` — audit=no_audit_recorded, verification=ok, verif_age=11d
- `eu-mica-2023` — audit=no_audit_recorded, verification=ok, verif_age=40d
- `evil-corp-ofac-2024-10` — audit=no_audit_recorded, verification=ok, verif_age=1d
- `fatf-grey-list-crypto-related-actions-2023-2024` — audit=no_audit_recorded, verification=ok, verif_age=11d
- `fatf-targeted-update-va-vasp-2021` — audit=no_audit_recorded, verification=ok, verif_age=11d
- `fatf-targeted-update-va-vasp-2023` — audit=no_audit_recorded, verification=ok, verif_age=11d
- `fatf-virtual-currencies-key-definitions-2014` — audit=no_audit_recorded, verification=ok, verif_age=11d
- `fayzimatov-alqaeda-syria-ofac-2021-07` — audit=no_audit_recorded, verification=ok, verif_age=1d
- `fincen-eric-powers-p2p-exchanger-2019-04` — audit=no_audit_recorded, verification=ok, verif_age=1d
- `france-amf-binance-psan-2022` — audit=no_audit_recorded, verification=ok, verif_age=11d
- `fsb-crypto-asset-recommendations-2023` — audit=no_audit_recorded, verification=ok, verif_age=11d
- `funnull-cdn-ofac-2025` — audit=no_audit_recorded, verification=ok, verif_age=40d
- `g20-roadmap-crypto-asset-policy-2023` — audit=no_audit_recorded, verification=ok, verif_age=11d
- `g7-hiroshima-crypto-statement-2023` — audit=no_audit_recorded, verification=ok, verif_age=11d
- `garantex-besciokov-mira-serda-doj-2025` — audit=no_audit_recorded, verification=ok, verif_age=1d
- `garantex-ofac-2022` — audit=no_audit_recorded, verification=ok, verif_age=41d
- `gate-io-privacy-coin-perpetuals-delisting-2024-12` — audit=no_audit_recorded, verification=ok, verif_age=1d
- `goldage-ny-state-indictment-2006-07` — audit=no_audit_recorded, verification=ok, verif_age=1d
- `google-play-india-crypto-exchange-removal-2024-01` — audit=no_audit_recorded, verification=ok, verif_age=11d
- `grinex-garantex-successor-ofac-2025` — audit=no_audit_recorded, verification=ok, verif_age=41d
- `hanafin-huriya-russia-evasion-ofac-2023-05` — audit=no_audit_recorded, verification=ok, verif_age=1d
- `hongkong-hkma-stablecoins-ordinance-2025` — audit=no_audit_recorded, verification=ok, verif_age=11d
- `hongkong-sfc-bybit-warning-2024` — audit=no_audit_recorded, verification=ok, verif_age=11d
- `hongkong-sfc-jpex-block-2023` — audit=no_audit_recorded, verification=ok, verif_age=11d
- `hongkong-sfc-vatp-licensing-2023-06` — audit=no_audit_recorded, verification=ok, verif_age=11d
- `huobi-htx-privacy-coin-delisting-2024` — audit=no_audit_recorded, verification=ok, verif_age=0d
- `hydra-doj-2022` — audit=no_audit_recorded, verification=ok, verif_age=40d
- `hydra-ofac-2022` — audit=no_audit_recorded, verification=ok, verif_age=41d
- `iceland-cbi-foreign-exchange-bitcoin-2014` — audit=no_audit_recorded, verification=ok, verif_age=16d
- `india-rbi-crypto-ban-2018` — audit=no_audit_recorded, verification=ok, verif_age=40d
- `indonesia-bappebti-illegal-exchange-block-2023` — audit=no_audit_recorded, verification=ok, verif_age=11d
- `indonesia-bi-bitcoin-warning-2014` — audit=no_audit_recorded, verification=ok, verif_age=11d
- `indonesia-bi-payment-instrument-prohibition-2018-01` — audit=no_audit_recorded, verification=ok, verif_age=1d
- `indonesia-kominfo-exchange-social-account-block-2024-07` — audit=no_audit_recorded, verification=ok, verif_age=1d
- `infura-alchemy-tornado-rpc-block-2022` — audit=no_audit_recorded, verification=ok, verif_age=0d
- `infura-metamask-donetsk-luhansk-block-2022-03` — audit=no_audit_recorded, verification=ok, verif_age=11d
- `iran-cbi-crypto-banking-prohibition-2018` — audit=no_audit_recorded, verification=ok, verif_age=11d
- `iran-cbi-exchange-payment-gateway-block-2024-12` — audit=no_audit_recorded, verification=ok, verif_age=1d
- `iran-government-mining-electricity-restriction-2021` — audit=no_audit_recorded, verification=ok, verif_age=11d
- `iraq-cbi-cryptocurrency-prohibition-2017-12` — audit=no_audit_recorded, verification=ok, verif_age=1d
- `israel-nbctf-hamas-crypto-addresses-2021` — audit=no_audit_recorded, verification=ok, verif_age=11d
- `japan-fsa-binance-sakura-acquisition-2022-11` — audit=no_audit_recorded, verification=ok, verif_age=11d
- `japan-fsa-binance-warning-2018` — audit=no_audit_recorded, verification=ok, verif_age=11d
- `japan-fsa-dmm-bitcoin-order-2024-09` — audit=no_audit_recorded, verification=ok, verif_age=11d
- `japan-fsa-ftx-japan-suspension-2022-11` — audit=no_audit_recorded, verification=ok, verif_age=11d
- `japan-fsa-margin-leverage-cap-2x-2020-05` — audit=no_audit_recorded, verification=ok, verif_age=0d
- `japan-fsa-six-exchange-orders-2018-06` — audit=no_audit_recorded, verification=ok, verif_age=11d
- `japan-fsa-stablecoin-psa-effective-2023-06` — audit=no_audit_recorded, verification=ok, verif_age=16d
- `japan-fsa-travel-rule-effective-2023-06` — audit=no_audit_recorded, verification=ok, verif_age=11d
- `japan-fsa-zaif-orders-2018-09` — audit=no_audit_recorded, verification=ok, verif_age=11d
- `jordan-cbj-bank-crypto-prohibition-2014` — audit=no_audit_recorded, verification=ok, verif_age=1d
- `kazakhstan-digital-assets-law-2023-02` — audit=no_audit_recorded, verification=ok, verif_age=11d
- `kazakhstan-internet-shutdown-mining-2022-01` — audit=no_audit_recorded, verification=ok, verif_age=11d
- `kb-vostok-russia-drone-ofac-2024-08` — audit=no_audit_recorded, verification=ok, verif_age=1d
- `kenya-cbk-virtual-currency-circular-2015-12` — audit=no_audit_recorded, verification=ok, verif_age=1d
- `korea-fiu-isms-real-name-exchange-shutdown-2021-09` — audit=no_audit_recorded, verification=ok, verif_age=1d
- `korea-fsc-privacy-coin-delisting-mandate-2021-03` — audit=no_audit_recorded, verification=ok, verif_age=1d
- `korea-travel-rule-2022` — audit=no_audit_recorded, verification=ok, verif_age=40d
- `kraken-monero-eu-delisting-2024` — audit=no_audit_recorded, verification=ok, verif_age=15d
- `kraken-sec-unregistered-exchange-2023` — audit=no_audit_recorded, verification=ok, verif_age=0d
- `kraken-uk-derivatives-exit-2021` — audit=no_audit_recorded, verification=ok, verif_age=15d
- `kucoin-canada-exit-2023` — audit=no_audit_recorded, verification=ok, verif_age=15d
- `kucoin-netherlands-exit-2023` — audit=no_audit_recorded, verification=ok, verif_age=11d
- `kuwait-cma-virtual-assets-prohibition-2023-07` — audit=no_audit_recorded, verification=ok, verif_age=1d
- `kyrgyzstan-nbkr-virtual-currency-payment-warning-2014-07` — audit=no_audit_recorded, verification=ok, verif_age=1d
- `lebanon-bdl-bitcoin-warning-2013-12` — audit=no_audit_recorded, verification=ok, verif_age=1d
- `liberty-reserve-costa-rica-license-denial-2011-03` — audit=no_audit_recorded, verification=ok, verif_age=11d
- `lockbit-affiliates-ofac-2024` — audit=no_audit_recorded, verification=ok, verif_age=40d
- `magic-eden-ofac-sanctioned-country-block` — audit=no_audit_recorded, verification=ok, verif_age=0d
- `makerdao-emergency-shutdown-contingency-2022-08` — audit=no_audit_recorded, verification=ok, verif_age=11d
- `malaysia-sc-binance-disable-2021` — audit=no_audit_recorded, verification=ok, verif_age=0d
- `media-land-volosovik-bulletproof-ofac-2025-11` — audit=no_audit_recorded, verification=ok, verif_age=1d
- `metamask-eth-phishing-detect-tornado-additions-2022` — audit=no_audit_recorded, verification=ok, verif_age=15d
- `metamask-snaps-region-restrictions-2023-09` — audit=no_audit_recorded, verification=ok, verif_age=15d
- `mica-l2-esma-eba-rts-2024` — audit=no_audit_recorded, verification=ok, verif_age=11d
- `morocco-office-des-changes-crypto-ban-2017-11` — audit=no_audit_recorded, verification=ok, verif_age=1d
- `mtgox-bankruptcy-tokyo-2014` — audit=no_audit_recorded, verification=ok, verif_age=11d
- `mtgox-dhs-dwolla-wells-fargo-seizure-2013` — audit=no_audit_recorded, verification=ok, verif_age=12d
- `mtgox-june-2011-hack-trading-suspension` — audit=no_audit_recorded, verification=ok, verif_age=11d
- `mtgox-mizuho-wire-pressure-2012` — audit=no_audit_recorded, verification=ok, verif_age=11d
- `mtgox-usd-withdrawal-suspension-2013-06` — audit=no_audit_recorded, verification=ok, verif_age=11d
- `myanmar-cbm-crypto-prohibition-directive-9-2020` — audit=no_audit_recorded, verification=ok, verif_age=1d
- `nemesis-parsarad-darknet-ofac-2025-03` — audit=no_audit_recorded, verification=ok, verif_age=1d
- `nepal-nrb-bitcoin-ban-2017-08` — audit=no_audit_recorded, verification=ok, verif_age=1d
- `nepal-nrb-comprehensive-crypto-ban-2021-09` — audit=no_audit_recorded, verification=ok, verif_age=1d
- `netex24-bitpapa-russia-crypto-ofac-2024-03` — audit=no_audit_recorded, verification=ok, verif_age=1d
- `netherlands-dnb-binance-warning-2021` — audit=no_audit_recorded, verification=ok, verif_age=0d
- `netwalker-vachon-desjardins-doj-2022` — audit=no_audit_recorded, verification=ok, verif_age=1d
- `nigeria-cbn-crypto-ban-2021` — audit=no_audit_recorded, verification=ok, verif_age=40d
- `nydfs-bitlicense-bitfinex-kraken-shapeshift-exit-2015` — audit=no_audit_recorded, verification=ok, verif_age=12d
- `nydfs-bittrex-bitlicense-denial-2019-04` — audit=no_audit_recorded, verification=ok, verif_age=1d
- `oasis-app-wormhole-counter-exploit-2023-02` — audit=no_audit_recorded, verification=ok, verif_age=12d
- `oko-design-bureau-russia-drone-ofac-2024-05` — audit=no_audit_recorded, verification=ok, verif_age=1d
- `okx-canada-exit-2023` — audit=no_audit_recorded, verification=ok, verif_age=1d
- `okx-india-exit-2024-03` — audit=no_audit_recorded, verification=ok, verif_age=1d
- `okx-monero-global-delisting-2024` — audit=no_audit_recorded, verification=ok, verif_age=15d
- `okx-nigeria-exit-2024-08` — audit=no_audit_recorded, verification=ok, verif_age=1d
- `opensea-iran-cuba-sanctions-block-2022` — audit=no_audit_recorded, verification=ok, verif_age=0d
- `orca-dex-us-frontend-block-2023-03` — audit=no_audit_recorded, verification=ok, verif_age=1d
- `pakistan-sbp-crypto-prohibition-2018-04` — audit=no_audit_recorded, verification=ok, verif_age=1d
- `paxos-busd-nydfs-minting-stop-2023` — audit=no_audit_recorded, verification=ok, verif_age=11d
- `paxos-canada-exit-2023-04` — audit=no_audit_recorded, verification=ok, verif_age=1d
- `pecunix-bullion-transfer-2008` — audit=no_audit_recorded, verification=ok, verif_age=11d
- `philippines-bsp-vasp-license-moratorium-2022-09` — audit=no_audit_recorded, verification=ok, verif_age=1d
- `philippines-sec-binance-block-2024` — audit=no_audit_recorded, verification=ok, verif_age=11d
- `polymarket-cftc-geofence-2022-01` — audit=no_audit_recorded, verification=ok, verif_age=12d
- `polynonce-bittrex-fincen-2022` — audit=no_audit_recorded, verification=ok, verif_age=12d
- `prince-group-chen-zhi-ofac-2025-10` — audit=no_audit_recorded, verification=ok, verif_age=1d
- `pump-fun-uk-fca-geofence-2024-12` — audit=no_audit_recorded, verification=ok, verif_age=15d
- `qatar-qcb-qfcra-virtual-asset-ban-2019-12` — audit=no_audit_recorded, verification=ok, verif_age=1d
- `ren-protocol-shutdown-alameda-ftx-2022-12` — audit=no_audit_recorded, verification=ok, verif_age=15d
- `revil-vasinskyi-polyanin-doj-2021` — audit=no_audit_recorded, verification=ok, verif_age=1d
- `russia-cbr-bitcoin-information-letter-2014` — audit=no_audit_recorded, verification=ok, verif_age=11d
- `russia-cbr-crypto-payment-ban-2022` — audit=no_audit_recorded, verification=ok, verif_age=11d
- `russia-dfa-law-2020` — audit=no_audit_recorded, verification=ok, verif_age=11d
- `russia-election-interference-ofac-2020` — audit=no_audit_recorded, verification=ok, verif_age=40d
- `russia-mining-legalization-law-2024-08` — audit=no_audit_recorded, verification=ok, verif_age=11d
- `russia-mining-regional-ban-2024-12` — audit=no_audit_recorded, verification=ok, verif_age=11d
- `russia-rosfinmonitoring-binance-russia-rails-2022` — audit=no_audit_recorded, verification=ok, verif_age=11d
- `russian-cyber-theft-ofac-2020` — audit=no_audit_recorded, verification=ok, verif_age=40d
- `salame-ftx-campaign-finance-doj-2023` — audit=no_audit_recorded, verification=ok, verif_age=12d
- `samourai-doj-2024` — audit=no_audit_recorded, verification=ok, verif_age=40d
- `saudi-standing-committee-virtual-currency-warning-2018-08` — audit=no_audit_recorded, verification=ok, verif_age=1d
- `sec-etherdelta-coburn-unregistered-exchange-2018-11` — audit=no_audit_recorded, verification=ok, verif_age=1d
- `sec-garza-gaw-miners-zenminer-2015` — audit=no_audit_recorded, verification=ok, verif_age=12d
- `sec-nexo-earn-lending-product-cease-2023-01` — audit=no_audit_recorded, verification=ok, verif_age=1d
- `sec-tokenlot-unregistered-broker-2018-09` — audit=no_audit_recorded, verification=ok, verif_age=1d
- `sec-v-coinbase-staking-wells-2023` — audit=no_audit_recorded, verification=ok, verif_age=11d
- `sec-v-ftx-2022` — audit=no_audit_recorded, verification=ok, verif_age=11d
- `sec-v-ripple-2020` — audit=no_audit_recorded, verification=ok, verif_age=0d
- `sec-v-uniswap-wells-notice-2024` — audit=no_audit_recorded, verification=ok, verif_age=26d
- `shapeshift-mandatory-kyc-anonymity-end-2018-09` — audit=no_audit_recorded, verification=ok, verif_age=1d
- `singapore-mas-binance-services-2021` — audit=no_audit_recorded, verification=ok, verif_age=0d
- `singapore-mas-retail-crypto-restriction-2022` — audit=no_audit_recorded, verification=ok, verif_age=11d
- `south-africa-fsca-crypto-financial-product-2022` — audit=no_audit_recorded, verification=ok, verif_age=11d
- `sri-lanka-cbsl-crypto-warning-fx-directive-2021` — audit=no_audit_recorded, verification=ok, verif_age=1d
- `suex-ofac-2021` — audit=no_audit_recorded, verification=ok, verif_age=41d
- `switzerland-finma-tezos-zg-2018` — audit=no_audit_recorded, verification=ok, verif_age=11d
- `t3-bybit-hack-usdt-freeze-2025-03` — audit=no_audit_recorded, verification=ok, verif_age=0d
- `t3-financial-crime-unit-launch-2024-09` — audit=no_audit_recorded, verification=ok, verif_age=1d
- `taiwan-fsc-aml-vasp-regime-2021-2024` — audit=no_audit_recorded, verification=ok, verif_age=1d
- `taiwan-fsc-bitcoin-bank-atm-ban-2014-01` — audit=no_audit_recorded, verification=ok, verif_age=1d
- `task-force-rusich-ofac-2022-09` — audit=no_audit_recorded, verification=ok, verif_age=1d
- `tengyue-chemical-fentanyl-ofac-2025-09` — audit=no_audit_recorded, verification=ok, verif_age=1d
- `terror-financing-crypto-seizure-doj-2020` — audit=no_audit_recorded, verification=ok, verif_age=1d
- `tether-doj-pig-butchering-freeze-2023` — audit=no_audit_recorded, verification=ok, verif_age=40d
- `tether-dprk-precommit-freeze-2025` — audit=no_audit_recorded, verification=ok, verif_age=40d
- `tether-garantex-usdt-freeze-2025-03` — audit=no_audit_recorded, verification=ok, verif_age=1d
- `tether-ofac-iran-economic-fury-344m-freeze-2026-04` — audit=no_audit_recorded, verification=ok, verif_age=1d
- `tether-okx-doj-pig-butchering-225m-freeze-2025-06` — audit=no_audit_recorded, verification=ok, verif_age=1d
- `tether-pig-butchering-second-wave-2024` — audit=no_audit_recorded, verification=ok, verif_age=11d
- `tether-tron-philippines-pdea-freeze-2024` — audit=no_audit_recorded, verification=ok, verif_age=11d
- `thailand-bot-bitcoin-prohibition-2013` — audit=no_audit_recorded, verification=ok, verif_age=11d
- `thailand-sec-binance-bybit-c-and-d-2021` — audit=no_audit_recorded, verification=ok, verif_age=11d
- `thailand-sec-crypto-payment-ban-2022-04` — audit=no_audit_recorded, verification=ok, verif_age=1d
- `thailand-sec-meme-fan-nft-exchange-token-ban-2021-06` — audit=no_audit_recorded, verification=ok, verif_age=1d
- `tornado-cash-frontend-tornado-cash-eth-block-2022-04` — audit=no_audit_recorded, verification=ok, verif_age=15d
- `tornado-cash-github-takedown-2022-08` — audit=no_audit_recorded, verification=ok, verif_age=15d
- `tornado-cash-ofac-delisting-2025` — audit=no_audit_recorded, verification=ok, verif_age=41d
- `tornado-cash-pertsev-doj-indictment-2023` — audit=no_audit_recorded, verification=ok, verif_age=11d
- `tornado-cash-tornadocash-org-seizure-2022` — audit=no_audit_recorded, verification=ok, verif_age=15d
- `trustwallet-sanctioned-token-ui-update-2022` — audit=no_audit_recorded, verification=ok, verif_age=11d
- `turkey-cbrt-crypto-ban-2021` — audit=no_audit_recorded, verification=ok, verif_age=40d
- `turkey-cmb-casp-licensing-law-7518-2024` — audit=no_audit_recorded, verification=ok, verif_age=11d
- `uae-sca-crypto-asset-activities-regulation-decision-23-2020` — audit=no_audit_recorded, verification=ok, verif_age=1d
- `uae-vara-licence-issuance-regime-2023` — audit=no_audit_recorded, verification=ok, verif_age=11d
- `uk-fca-binance-markets-2021` — audit=no_audit_recorded, verification=ok, verif_age=0d
- `uk-fca-crypto-promotion-rule-2023` — audit=no_audit_recorded, verification=ok, verif_age=11d
- `uk-hmrc-bitcoin-vat-brief-09-14-2014` — audit=no_audit_recorded, verification=ok, verif_age=11d
- `ukraine-virtual-assets-law-2022-03` — audit=no_audit_recorded, verification=ok, verif_age=11d
- `uniswap-balancer-tornado-frontend-block-2022-08` — audit=no_audit_recorded, verification=ok, verif_age=11d
- `uniswap-frontend-delisting-2023` — audit=no_audit_recorded, verification=ok, verif_age=40d
- `uniswap-token-list-curation-default-2021` — audit=no_audit_recorded, verification=ok, verif_age=11d
- `uniswap-tokenized-stocks-delisting-2021-07` — audit=no_audit_recorded, verification=ok, verif_age=11d
- `unsc-resolution-2371-dprk-crypto-2017` — audit=no_audit_recorded, verification=ok, verif_age=11d
- `uzbekistan-napp-vasp-licensing-2022-07` — audit=no_audit_recorded, verification=ok, verif_age=11d
- `venezuela-sunacrip-mining-exchange-halt-2023-03` — audit=no_audit_recorded, verification=ok, verif_age=1d
- `vietnam-sbv-bitcoin-prohibition-statement-2014-02` — audit=no_audit_recorded, verification=ok, verif_age=1d
- `vietnam-sbv-payment-prohibition-2017-10` — audit=no_audit_recorded, verification=ok, verif_age=1d
- `voyager-bankruptcy-doj-objection-2023` — audit=no_audit_recorded, verification=ok, verif_age=11d
- `webmoney-ukraine-tax-police-freeze-2013-06` — audit=no_audit_recorded, verification=ok, verif_age=1d
- `wikileaks-amazon-aws-eviction-2010-12` — audit=no_audit_recorded, verification=ok, verif_age=11d
- `wikileaks-bank-of-america-block-2010-12` — audit=no_audit_recorded, verification=ok, verif_age=11d
- `wikileaks-everydns-domain-termination-2010-12` — audit=no_audit_recorded, verification=ok, verif_age=11d
- `wikileaks-mastercard-suspension-2010-12` — audit=no_audit_recorded, verification=ok, verif_age=11d
- `wikileaks-paypal-freeze-2010-12` — audit=no_audit_recorded, verification=ok, verif_age=11d
- `wikileaks-postfinance-account-closure-2010-12` — audit=no_audit_recorded, verification=ok, verif_age=11d
- `wikileaks-visa-europe-suspension-2010-12` — audit=no_audit_recorded, verification=ok, verif_age=11d
- `wikileaks-wau-holland-tax-status-challenge-2010-12` — audit=no_audit_recorded, verification=ok, verif_age=11d
- `wikileaks-western-union-interdiction-2010-12` — audit=no_audit_recorded, verification=ok, verif_age=11d
- `zimbabwe-rbz-circular-2-2018-golix-ban` — audit=no_audit_recorded, verification=ok, verif_age=1d
- `zimbabwe-rbz-circular-2-2018-golix` — audit=no_audit_recorded, verification=ok, verif_age=1d
