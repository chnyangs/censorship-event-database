# Staleness report

Generated at: `2026-05-17T00:00:00Z`
Red threshold: audits / verifications older than `90` days.
Most recent agent activity in `candidate_triggers/`: `none recorded`.

## Coverage snapshot

Two dimensions tracked per event; missing values surface as explicit gaps, never masked.

- **Adversarial audit** (`last_human_audit`): {'no_audit_recorded': 187, 'ok': 75}
- **Verification** (`last_verified`): {'ok': 262}
- **Row-level summary** (worst of the two): {'no_audit_recorded': 187, 'ok': 75}

## Flag legend

- `ok` — within the red threshold
- `red` — older than 90 days
- `no_audit_recorded` — no last_human_audit on record — event has never been through an adversarial audit
- `no_verification_recorded` — no last_verified on record — event has never been re-verified
- `error` — event YAML failed to parse

## Per-event table

| Event | Status | Origin | last_human_audit | Audit age | Audit flag | last_verified | Verification age | Verif flag | Summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `1inch-us-geofence-2021-09` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-16 | 1 | ok | no_audit_recorded |
| `aave-arc-fireblocks-whitelist-2022-01` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-16 | 1 | ok | no_audit_recorded |
| `aave-tornado-frontend-block-2022-08` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-16 | 1 | ok | no_audit_recorded |
| `aeza-group-ofac-2025` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-22 | 25 | ok | no_audit_recorded |
| `alphabay-hansa-doj-2017` | `admitted` | `human_reviewed` | 2026-05-16 | 1 | ok | 2026-05-16 | 1 | ok | ok |
| `apple-india-crypto-exchange-removal-2024-01` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-16 | 1 | ok | no_audit_recorded |
| `argentina-cnv-psav-registration-2024` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-17 | 0 | ok | no_audit_recorded |
| `argentina-uif-resolution-300-2014` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-17 | 0 | ok | no_audit_recorded |
| `augur-v2-us-uk-geofence-2020-07` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-17 | 0 | ok | no_audit_recorded |
| `australia-asic-binance-derivatives-2023` | `admitted` | `human_reviewed` | 2026-05-16 | 1 | ok | 2026-05-16 | 1 | ok | ok |
| `bangladesh-bb-bitcoin-warning-2014` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-17 | 0 | ok | no_audit_recorded |
| `belgium-fsma-binance-cease-2023` | `admitted` | `human_reviewed` | 2026-05-16 | 1 | ok | 2026-05-16 | 1 | ok | ok |
| `binance-4framework-2023` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-22 | 25 | ok | no_audit_recorded |
| `binance-busd-wind-down-2024` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-17 | 0 | ok | no_audit_recorded |
| `binance-cftc-2023` | `admitted` | `human_reviewed` | 2026-05-16 | 1 | ok | 2026-05-16 | 1 | ok | ok |
| `binance-privacy-coin-delisting-2023` | `admitted` | `human_reviewed` | 2026-05-16 | 1 | ok | 2026-05-16 | 1 | ok | ok |
| `binance-russia-exit-commex-2023` | `admitted` | `human_reviewed` | 2026-05-16 | 1 | ok | 2026-05-16 | 1 | ok | ok |
| `binance-us-staking-end-2023` | `admitted` | `human_reviewed` | 2026-05-16 | 1 | ok | 2026-05-16 | 1 | ok | ok |
| `bitcoinica-shutdown-2012-05` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-17 | 0 | ok | no_audit_recorded |
| `bitfinex-cftc-retail-commodity-2016` | `admitted` | `human_reviewed` | 2026-05-16 | 1 | ok | 2026-05-16 | 1 | ok | ok |
| `bitfinex-tether-cftc-2021` | `admitted` | `human_reviewed` | 2026-05-16 | 1 | ok | 2026-05-16 | 1 | ok | ok |
| `bitfinex-tether-nyag-2021` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-17 | 0 | ok | no_audit_recorded |
| `bitmex-cftc-doj-2020` | `admitted` | `human_reviewed` | 2026-05-16 | 1 | ok | 2026-05-16 | 1 | ok | ok |
| `bitmex-fincen-2024` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-17 | 0 | ok | no_audit_recorded |
| `bitstamp-greece-portugal-exit-2023` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-17 | 0 | ok | no_audit_recorded |
| `bitzlato-doj-2023` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-21 | 26 | ok | no_audit_recorded |
| `blender-ofac-2022` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-21 | 26 | ok | no_audit_recorded |
| `blockfi-sec-lending-2022` | `admitted` | `human_reviewed` | 2026-05-16 | 1 | ok | 2026-05-16 | 1 | ok | ok |
| `bolivia-bcb-crypto-prohibition-2014` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-17 | 0 | ok | no_audit_recorded |
| `brazil-bacen-stablecoin-restriction-2023` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-17 | 0 | ok | no_audit_recorded |
| `brazil-bcb-comunicado-25306-2014` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-17 | 0 | ok | no_audit_recorded |
| `btc-e-doj-2017` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-22 | 25 | ok | no_audit_recorded |
| `bybit-singapore-exit-2022` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-17 | 0 | ok | no_audit_recorded |
| `canada-convoy-freeze-2022` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-22 | 25 | ok | no_audit_recorded |
| `canada-csa-binance-withdrawal-2023` | `admitted` | `human_reviewed` | 2026-05-16 | 1 | ok | 2026-05-16 | 1 | ok | ok |
| `celsius-bankruptcy-mashinsky-doj-2023` | `admitted` | `human_reviewed` | 2026-05-16 | 1 | ok | 2026-05-16 | 1 | ok | ok |
| `cftc-v-ftx-2022` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-17 | 0 | ok | no_audit_recorded |
| `cftc-v-ooki-dao-2022` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-22 | 25 | ok | no_audit_recorded |
| `chatex-ofac-2021` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-22 | 25 | ok | no_audit_recorded |
| `china-ico-ban-2017-09` | `draft` | `agent_draft` | 2026-05-16 | 1 | ok | 2026-05-16 | 1 | ok | ok |
| `china-inner-mongolia-mining-ban-2021-05` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-16 | 1 | ok | no_audit_recorded |
| `china-nft-secondary-trading-self-discipline-2022-06` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-16 | 1 | ok | no_audit_recorded |
| `china-pboc-crypto-ban-2013-12` | `admitted` | `human_reviewed` | 2026-05-16 | 1 | ok | 2026-05-16 | 1 | ok | ok |
| `china-pboc-crypto-ban-2021` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-21 | 26 | ok | no_audit_recorded |
| `china-pboc-exchange-shutdown-2017-09` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-16 | 1 | ok | no_audit_recorded |
| `china-sichuan-mining-ban-2021-06` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-16 | 1 | ok | no_audit_recorded |
| `china-state-council-mining-crackdown-2021-05` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-16 | 1 | ok | no_audit_recorded |
| `china-weibo-crypto-exchange-purge-2021-03` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-17 | 0 | ok | no_audit_recorded |
| `chipmixer-doj-2023` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-22 | 25 | ok | no_audit_recorded |
| `circle-usdc-cryptex-freeze-2024` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-17 | 0 | ok | no_audit_recorded |
| `circle-usdc-svb-policy-statement-2023` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-17 | 0 | ok | no_audit_recorded |
| `circle-usdc-tornado-2022` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-22 | 25 | ok | no_audit_recorded |
| `cloudflare-ethereum-gateway-tornado-block-2022-08` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-16 | 1 | ok | no_audit_recorded |
| `coin-mx-doj-murgio-2015` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-16 | 1 | ok | no_audit_recorded |
| `coinbase-india-exit-2022` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-22 | 25 | ok | no_audit_recorded |
| `coinbase-irs-john-doe-summons-2016` | `admitted` | `human_reviewed` | 2026-05-16 | 1 | ok | 2026-05-16 | 1 | ok | ok |
| `coinbase-japan-exit-2023` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-17 | 0 | ok | no_audit_recorded |
| `coinflip-cftc-derivabit-2015` | `admitted` | `human_reviewed` | 2026-05-16 | 1 | ok | 2026-05-16 | 1 | ok | ok |
| `consensys-metamask-infura-rpc-data-collection-2022-11` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-17 | 0 | ok | no_audit_recorded |
| `cryptex-ofac-2024` | `admitted` | `human_authored` | 2026-04-22 | 25 | ok | 2026-04-21 | 26 | ok | ok |
| `datacell-v-valitor-iceland-district-court-2012-07` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-16 | 1 | ok | no_audit_recorded |
| `dprk-usdt-network-ofac-2025` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-22 | 25 | ok | no_audit_recorded |
| `dydx-tornado-account-block-2022-08` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-16 | 1 | ok | no_audit_recorded |
| `eba-virtual-currencies-opinion-eba-op-2014-08` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-16 | 1 | ok | no_audit_recorded |
| `ebullion-doj-fbi-seizure-2008-08` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-17 | 0 | ok | no_audit_recorded |
| `egold-doj-guilty-plea-2008-07` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-16 | 1 | ok | no_audit_recorded |
| `ens-eth-domain-tornado-resolution-2022` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-17 | 0 | ok | no_audit_recorded |
| `etherscan-tornado-cash-ui-label-2022` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-17 | 0 | ok | no_audit_recorded |
| `eu-12th-russia-sanctions-2023` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-22 | 25 | ok | no_audit_recorded |
| `eu-14th-russia-sanctions-spfs-2024` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-17 | 0 | ok | no_audit_recorded |
| `eu-15th-russia-sanctions-2024` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-17 | 0 | ok | no_audit_recorded |
| `eu-amla-anti-money-laundering-authority-regulation-2024` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-17 | 0 | ok | no_audit_recorded |
| `eu-amlr-eu-single-rulebook-2024` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-17 | 0 | ok | no_audit_recorded |
| `eu-belarus-crypto-services-ban-2022` | `draft` | `agent_draft` | 2026-05-17 | 0 | ok | 2026-05-17 | 0 | ok | ok |
| `eu-dac8-crypto-asset-reporting-directive-2023` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-17 | 0 | ok | no_audit_recorded |
| `eu-mica-2023` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-22 | 25 | ok | no_audit_recorded |
| `eu-russia-crypto-wallet-cap-2022` | `admitted` | `human_reviewed` | 2026-05-16 | 1 | ok | 2026-05-16 | 1 | ok | ok |
| `eu-russia-full-crypto-wallet-ban-2022` | `admitted` | `human_reviewed` | 2026-05-16 | 1 | ok | 2026-05-16 | 1 | ok | ok |
| `eu-tfr-recast-2023` | `admitted` | `human_reviewed` | 2026-05-16 | 1 | ok | 2026-05-16 | 1 | ok | ok |
| `fatf-grey-list-crypto-related-actions-2023-2024` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-17 | 0 | ok | no_audit_recorded |
| `fatf-r15-vasp-travel-rule-2019` | `admitted` | `human_reviewed` | 2026-05-16 | 1 | ok | 2026-05-16 | 1 | ok | ok |
| `fatf-targeted-update-va-vasp-2021` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-17 | 0 | ok | no_audit_recorded |
| `fatf-targeted-update-va-vasp-2023` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-17 | 0 | ok | no_audit_recorded |
| `fatf-virtual-currencies-key-definitions-2014` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-16 | 1 | ok | no_audit_recorded |
| `fbi-bitcoin-intelligence-assessment-2012-04` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-17 | 0 | ok | no_audit_recorded |
| `fincen-virtual-currency-msb-guidance-2013` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-16 | 1 | ok | no_audit_recorded |
| `france-amf-binance-psan-2022` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-17 | 0 | ok | no_audit_recorded |
| `fsb-crypto-asset-recommendations-2023` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-17 | 0 | ok | no_audit_recorded |
| `ftx-bankman-fried-doj-2022` | `admitted` | `human_reviewed` | 2026-05-16 | 1 | ok | 2026-05-16 | 1 | ok | ok |
| `funnull-cdn-ofac-2025` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-22 | 25 | ok | no_audit_recorded |
| `g20-roadmap-crypto-asset-policy-2023` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-17 | 0 | ok | no_audit_recorded |
| `g7-hiroshima-crypto-statement-2023` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-17 | 0 | ok | no_audit_recorded |
| `garantex-ofac-2022` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-21 | 26 | ok | no_audit_recorded |
| `genesis-sec-gemini-earn-2023` | `admitted` | `human_reviewed` | 2026-05-16 | 1 | ok | 2026-05-16 | 1 | ok | ok |
| `germany-bafin-binance-licence-withdrawal-2023` | `admitted` | `human_reviewed` | 2026-05-16 | 1 | ok | 2026-05-16 | 1 | ok | ok |
| `google-play-india-crypto-exchange-removal-2024-01` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-16 | 1 | ok | no_audit_recorded |
| `grinex-garantex-successor-ofac-2025` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-21 | 26 | ok | no_audit_recorded |
| `helix-doj-mixer-2020` | `admitted` | `human_reviewed` | 2026-05-16 | 1 | ok | 2026-05-16 | 1 | ok | ok |
| `hongkong-hkma-stablecoins-ordinance-2025` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-16 | 1 | ok | no_audit_recorded |
| `hongkong-sfc-bybit-warning-2024` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-17 | 0 | ok | no_audit_recorded |
| `hongkong-sfc-jpex-block-2023` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-17 | 0 | ok | no_audit_recorded |
| `hongkong-sfc-vatp-licensing-2023-06` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-16 | 1 | ok | no_audit_recorded |
| `huobi-htx-privacy-coin-delisting-2024` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-17 | 0 | ok | no_audit_recorded |
| `hydra-doj-2022` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-22 | 25 | ok | no_audit_recorded |
| `hydra-ofac-2022` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-21 | 26 | ok | no_audit_recorded |
| `iceland-cbi-foreign-exchange-bitcoin-2014` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-16 | 1 | ok | no_audit_recorded |
| `india-fiu-offshore-vda-block-2023` | `admitted` | `human_reviewed` | 2026-05-16 | 1 | ok | 2026-05-16 | 1 | ok | ok |
| `india-rbi-crypto-ban-2018` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-22 | 25 | ok | no_audit_recorded |
| `indonesia-bappebti-illegal-exchange-block-2023` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-17 | 0 | ok | no_audit_recorded |
| `indonesia-bi-bitcoin-warning-2014` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-17 | 0 | ok | no_audit_recorded |
| `infura-alchemy-tornado-rpc-block-2022` | `admitted` | `human_reviewed` | 2026-05-16 | 1 | ok | 2026-05-16 | 1 | ok | ok |
| `infura-metamask-donetsk-luhansk-block-2022-03` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-16 | 1 | ok | no_audit_recorded |
| `iran-cbi-crypto-banking-prohibition-2018` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-17 | 0 | ok | no_audit_recorded |
| `iran-government-mining-electricity-restriction-2021` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-17 | 0 | ok | no_audit_recorded |
| `iran-ransomware-ofac-2018` | `admitted` | `human_authored` | 2026-05-15 | 2 | ok | 2026-04-22 | 25 | ok | ok |
| `irgc-ransomware-ofac-2022` | `admitted` | `human_authored` | 2026-05-15 | 2 | ok | 2026-04-22 | 25 | ok | ok |
| `israel-nbctf-hamas-crypto-addresses-2021` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-17 | 0 | ok | no_audit_recorded |
| `japan-fsa-binance-sakura-acquisition-2022-11` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-17 | 0 | ok | no_audit_recorded |
| `japan-fsa-binance-warning-2018` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-17 | 0 | ok | no_audit_recorded |
| `japan-fsa-coincheck-orders-2018` | `admitted` | `human_reviewed` | 2026-05-16 | 1 | ok | 2026-05-16 | 1 | ok | ok |
| `japan-fsa-dmm-bitcoin-order-2024-09` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-16 | 1 | ok | no_audit_recorded |
| `japan-fsa-ftx-japan-suspension-2022-11` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-16 | 1 | ok | no_audit_recorded |
| `japan-fsa-six-exchange-orders-2018-06` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-16 | 1 | ok | no_audit_recorded |
| `japan-fsa-stablecoin-psa-effective-2023-06` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-16 | 1 | ok | no_audit_recorded |
| `japan-fsa-travel-rule-effective-2023-06` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-16 | 1 | ok | no_audit_recorded |
| `japan-fsa-zaif-orders-2018-09` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-16 | 1 | ok | no_audit_recorded |
| `karpeles-arrest-tokyo-mtgox-2015` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-16 | 1 | ok | no_audit_recorded |
| `kazakhstan-digital-assets-law-2023-02` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-16 | 1 | ok | no_audit_recorded |
| `kazakhstan-internet-shutdown-mining-2022-01` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-16 | 1 | ok | no_audit_recorded |
| `kingdom-trust-fincen-2021` | `draft` | `agent_draft` | 2026-05-17 | 0 | ok | 2026-05-17 | 0 | ok | ok |
| `korea-fsc-ico-ban-2017` | `admitted` | `human_reviewed` | 2026-05-16 | 1 | ok | 2026-05-16 | 1 | ok | ok |
| `korea-fsc-institutional-restriction-2017` | `draft` | `agent_draft` | 2026-05-17 | 0 | ok | 2026-05-17 | 0 | ok | ok |
| `korea-travel-rule-2022` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-22 | 25 | ok | no_audit_recorded |
| `kraken-monero-eu-delisting-2024` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-17 | 0 | ok | no_audit_recorded |
| `kraken-sec-staking-2023` | `admitted` | `human_reviewed` | 2026-05-16 | 1 | ok | 2026-05-16 | 1 | ok | ok |
| `kraken-sec-unregistered-exchange-2023` | `admitted` | `human_reviewed` | 2026-05-16 | 1 | ok | 2026-05-16 | 1 | ok | ok |
| `kraken-uk-derivatives-exit-2021` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-17 | 0 | ok | no_audit_recorded |
| `kucoin-canada-exit-2023` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-17 | 0 | ok | no_audit_recorded |
| `kucoin-doj-2024` | `admitted` | `human_reviewed` | 2026-05-16 | 1 | ok | 2026-05-16 | 1 | ok | ok |
| `kucoin-netherlands-exit-2023` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-17 | 0 | ok | no_audit_recorded |
| `lazarus-entity-ofac-2019` | `admitted` | `human_authored` | 2026-05-15 | 2 | ok | 2026-04-22 | 25 | ok | ok |
| `lazarus-laundering-ofac-2020` | `admitted` | `human_authored` | 2026-05-15 | 2 | ok | 2026-04-22 | 25 | ok | ok |
| `liberty-reserve-costa-rica-license-denial-2011-03` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-17 | 0 | ok | no_audit_recorded |
| `lockbit-affiliates-ofac-2024` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-22 | 25 | ok | no_audit_recorded |
| `lockbit-leader-ofac-2024` | `admitted` | `human_authored` | 2026-05-15 | 2 | ok | 2026-04-22 | 25 | ok | ok |
| `makerdao-emergency-shutdown-contingency-2022-08` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-17 | 0 | ok | no_audit_recorded |
| `malaysia-sc-binance-disable-2021` | `admitted` | `human_reviewed` | 2026-05-16 | 1 | ok | 2026-05-16 | 1 | ok | ok |
| `matveev-ofac-2023` | `admitted` | `human_authored` | 2026-05-15 | 2 | ok | 2026-04-22 | 25 | ok | ok |
| `metamask-eth-phishing-detect-tornado-additions-2022` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-17 | 0 | ok | no_audit_recorded |
| `metamask-snaps-region-restrictions-2023-09` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-17 | 0 | ok | no_audit_recorded |
| `mica-l2-esma-eba-rts-2024` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-17 | 0 | ok | no_audit_recorded |
| `mtgox-bankruptcy-tokyo-2014` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-16 | 1 | ok | no_audit_recorded |
| `mtgox-coinlab-civil-2013` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-16 | 1 | ok | no_audit_recorded |
| `mtgox-dhs-dwolla-wells-fargo-seizure-2013` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-16 | 1 | ok | no_audit_recorded |
| `mtgox-june-2011-hack-trading-suspension` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-17 | 0 | ok | no_audit_recorded |
| `mtgox-mizuho-wire-pressure-2012` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-17 | 0 | ok | no_audit_recorded |
| `mtgox-usd-withdrawal-suspension-2013-06` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-16 | 1 | ok | no_audit_recorded |
| `netherlands-dnb-binance-warning-2021` | `admitted` | `human_reviewed` | 2026-05-16 | 1 | ok | 2026-05-16 | 1 | ok | ok |
| `nigeria-cbn-crypto-ban-2021` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-22 | 25 | ok | no_audit_recorded |
| `nydfs-bitlicense-2015-06` | `admitted` | `human_reviewed` | 2026-05-16 | 1 | ok | 2026-05-16 | 1 | ok | ok |
| `nydfs-bitlicense-bitfinex-kraken-shapeshift-exit-2015` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-16 | 1 | ok | no_audit_recorded |
| `oasis-app-wormhole-counter-exploit-2023-02` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-17 | 0 | ok | no_audit_recorded |
| `oecd-carf-2022` | `admitted` | `human_reviewed` | 2026-05-16 | 1 | ok | 2026-05-16 | 1 | ok | ok |
| `ofac-dprk-it-worker-sim-hyon-sop-2023-04` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-17 | 0 | ok | no_audit_recorded |
| `ofac-hamas-buy-cash-msb-2023-10` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-16 | 1 | ok | no_audit_recorded |
| `ofac-hamas-gaza-now-2024-03` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-16 | 1 | ok | no_audit_recorded |
| `ofac-hamas-irgc-virtual-currency-network-2024-01` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-16 | 1 | ok | no_audit_recorded |
| `ofac-houthi-al-jamal-crypto-refresh-2024-12` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-17 | 0 | ok | no_audit_recorded |
| `ofac-recent-action-20240111` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-16 | 1 | ok | no_audit_recorded |
| `ofac-trickbot-conti-eleven-2023-09` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-16 | 1 | ok | no_audit_recorded |
| `ofac-zhdanova-russian-elite-launderer-2023-11` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-16 | 1 | ok | no_audit_recorded |
| `okx-monero-global-delisting-2024` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-17 | 0 | ok | no_audit_recorded |
| `okx-privacy-token-delist-2024` | `admitted` | `human_reviewed` | 2026-05-16 | 1 | ok | 2026-05-16 | 1 | ok | ok |
| `opensea-iran-cuba-sanctions-block-2022` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-16 | 1 | ok | no_audit_recorded |
| `paxos-busd-nydfs-minting-stop-2023` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-16 | 1 | ok | no_audit_recorded |
| `pecunix-bullion-transfer-2008` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-17 | 0 | ok | no_audit_recorded |
| `pertsev-nl-arrest-2022` | `admitted` | `human_authored` | 2026-05-15 | 2 | ok | 2026-04-22 | 25 | ok | ok |
| `philippines-sec-binance-block-2024` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-16 | 1 | ok | no_audit_recorded |
| `polymarket-cftc-geofence-2022-01` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-16 | 1 | ok | no_audit_recorded |
| `polynonce-bittrex-fincen-2022` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-17 | 0 | ok | no_audit_recorded |
| `powell-unlicensed-bitcoin-exchange-2014` | `admitted` | `human_reviewed` | 2026-05-16 | 1 | ok | 2026-05-16 | 1 | ok | ok |
| `pump-fun-uk-fca-geofence-2024-12` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-17 | 0 | ok | no_audit_recorded |
| `ren-protocol-shutdown-alameda-ftx-2022-12` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-17 | 0 | ok | no_audit_recorded |
| `ripple-fincen-xrp-2015` | `admitted` | `human_reviewed` | 2026-05-16 | 1 | ok | 2026-05-16 | 1 | ok | ok |
| `russia-cbr-bitcoin-information-letter-2014` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-16 | 1 | ok | no_audit_recorded |
| `russia-cbr-crypto-payment-ban-2022` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-17 | 0 | ok | no_audit_recorded |
| `russia-dfa-law-2020` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-17 | 0 | ok | no_audit_recorded |
| `russia-election-interference-ofac-2020` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-22 | 25 | ok | no_audit_recorded |
| `russia-mining-legalization-law-2024-08` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-17 | 0 | ok | no_audit_recorded |
| `russia-mining-regional-ban-2024-12` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-16 | 1 | ok | no_audit_recorded |
| `russia-rosfinmonitoring-binance-russia-rails-2022` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-17 | 0 | ok | no_audit_recorded |
| `russian-cyber-theft-ofac-2020` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-22 | 25 | ok | no_audit_recorded |
| `russian-cybercrime-infra-ofac-2025` | `admitted` | `human_authored` | 2026-05-15 | 2 | ok | 2026-04-22 | 25 | ok | ok |
| `salame-ftx-campaign-finance-doj-2023` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-17 | 0 | ok | no_audit_recorded |
| `samourai-doj-2024` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-22 | 25 | ok | no_audit_recorded |
| `sec-beaxy-platform-shutdown-2023` | `admitted` | `human_reviewed` | 2026-05-16 | 1 | ok | 2026-05-16 | 1 | ok | ok |
| `sec-burnside-bitcoin-stock-exchange-2014` | `admitted` | `human_reviewed` | 2026-05-16 | 1 | ok | 2026-05-16 | 1 | ok | ok |
| `sec-garza-gaw-miners-zenminer-2015` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-16 | 1 | ok | no_audit_recorded |
| `sec-shavers-btcst-2013` | `admitted` | `human_reviewed` | 2026-05-16 | 1 | ok | 2026-05-16 | 1 | ok | ok |
| `sec-v-binance-2023` | `admitted` | `human_authored` | 2026-05-06 | 11 | ok | 2026-05-06 | 11 | ok | ok |
| `sec-v-bittrex-2023` | `admitted` | `human_reviewed` | 2026-05-16 | 1 | ok | 2026-05-16 | 1 | ok | ok |
| `sec-v-coinbase-2023` | `admitted` | `human_authored` | 2026-05-06 | 11 | ok | 2026-05-06 | 11 | ok | ok |
| `sec-v-coinbase-staking-wells-2023` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-17 | 0 | ok | no_audit_recorded |
| `sec-v-ftx-2022` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-17 | 0 | ok | no_audit_recorded |
| `sec-v-ripple-2020` | `admitted` | `human_reviewed` | 2026-05-16 | 1 | ok | 2026-05-16 | 1 | ok | ok |
| `sec-v-telegram-ton-2020` | `admitted` | `human_reviewed` | 2026-05-16 | 1 | ok | 2026-05-16 | 1 | ok | ok |
| `sec-v-uniswap-wells-notice-2024` | `rejected` | `human_authored` | — | — | no_audit_recorded | 2026-05-06 | 11 | ok | no_audit_recorded |
| `sec-voorhees-satoshidice-2014` | `admitted` | `human_reviewed` | 2026-05-16 | 1 | ok | 2026-05-16 | 1 | ok | ok |
| `semenov-ofac-2023` | `admitted` | `human_authored` | 2026-04-22 | 25 | ok | 2026-04-21 | 26 | ok | ok |
| `shrem-faiella-bitcoin-exchange-2014` | `admitted` | `human_reviewed` | 2026-05-16 | 1 | ok | 2026-05-16 | 1 | ok | ok |
| `sichuan-silence-ofac-2024` | `admitted` | `human_authored` | 2026-05-15 | 2 | ok | 2026-04-22 | 25 | ok | ok |
| `silk-road-doj-seizure-2013` | `admitted` | `human_reviewed` | 2026-05-16 | 1 | ok | 2026-05-16 | 1 | ok | ok |
| `sinbad-doj-2024` | `admitted` | `human_reviewed` | 2026-05-16 | 1 | ok | 2026-05-16 | 1 | ok | ok |
| `sinbad-ofac-2023` | `admitted` | `human_authored` | 2026-05-15 | 2 | ok | 2026-04-21 | 26 | ok | ok |
| `singapore-mas-binance-services-2021` | `admitted` | `human_reviewed` | 2026-05-16 | 1 | ok | 2026-05-16 | 1 | ok | ok |
| `singapore-mas-retail-crypto-restriction-2022` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-17 | 0 | ok | no_audit_recorded |
| `south-africa-fsca-crypto-financial-product-2022` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-17 | 0 | ok | no_audit_recorded |
| `storm-semenov-doj-2023` | `admitted` | `human_authored` | 2026-05-15 | 2 | ok | 2026-04-22 | 25 | ok | ok |
| `suex-ofac-2021` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-21 | 26 | ok | no_audit_recorded |
| `switzerland-finma-tezos-zg-2018` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-17 | 0 | ok | no_audit_recorded |
| `teraexchange-cftc-bitcoin-swap-2015` | `admitted` | `human_reviewed` | 2026-05-16 | 1 | ok | 2026-05-16 | 1 | ok | ok |
| `tether-doj-pig-butchering-freeze-2023` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-22 | 25 | ok | no_audit_recorded |
| `tether-dprk-precommit-freeze-2025` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-22 | 25 | ok | no_audit_recorded |
| `tether-pig-butchering-second-wave-2024` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-17 | 0 | ok | no_audit_recorded |
| `tether-retroactive-sweep-2023` | `admitted` | `human_authored` | 2026-04-22 | 25 | ok | 2026-04-22 | 25 | ok | ok |
| `tether-tron-philippines-pdea-freeze-2024` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-17 | 0 | ok | no_audit_recorded |
| `thailand-bot-bitcoin-prohibition-2013` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-17 | 0 | ok | no_audit_recorded |
| `thailand-sec-binance-bybit-c-and-d-2021` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-17 | 0 | ok | no_audit_recorded |
| `tornado-cash-frontend-tornado-cash-eth-block-2022-04` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-17 | 0 | ok | no_audit_recorded |
| `tornado-cash-github-takedown-2022-08` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-17 | 0 | ok | no_audit_recorded |
| `tornado-cash-ofac-2022` | `admitted` | `human_authored` | 2026-04-22 | 25 | ok | 2026-04-21 | 26 | ok | ok |
| `tornado-cash-ofac-delisting-2025` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-21 | 26 | ok | no_audit_recorded |
| `tornado-cash-ofac-redesignation-2022` | `admitted` | `human_authored` | 2026-04-22 | 25 | ok | 2026-04-21 | 26 | ok | ok |
| `tornado-cash-pertsev-doj-indictment-2023` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-17 | 0 | ok | no_audit_recorded |
| `tornado-cash-storm-conviction-2025` | `admitted` | `human_reviewed` | 2026-05-16 | 1 | ok | 2026-05-16 | 1 | ok | ok |
| `tornado-cash-tornadocash-org-seizure-2022` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-17 | 0 | ok | no_audit_recorded |
| `trustwallet-sanctioned-token-ui-update-2022` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-17 | 0 | ok | no_audit_recorded |
| `turkey-cbrt-crypto-ban-2021` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-22 | 25 | ok | no_audit_recorded |
| `turkey-cmb-casp-licensing-law-7518-2024` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-17 | 0 | ok | no_audit_recorded |
| `uae-vara-licence-issuance-regime-2023` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-17 | 0 | ok | no_audit_recorded |
| `uk-fca-binance-markets-2021` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-05-16 | 1 | ok | no_audit_recorded |
| `uk-fca-crypto-promotion-rule-2023` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-17 | 0 | ok | no_audit_recorded |
| `uk-hmrc-bitcoin-vat-brief-09-14-2014` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-17 | 0 | ok | no_audit_recorded |
| `ukraine-virtual-assets-law-2022-03` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-16 | 1 | ok | no_audit_recorded |
| `uniswap-balancer-tornado-frontend-block-2022-08` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-16 | 1 | ok | no_audit_recorded |
| `uniswap-frontend-delisting-2023` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-22 | 25 | ok | no_audit_recorded |
| `uniswap-token-list-curation-default-2021` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-17 | 0 | ok | no_audit_recorded |
| `uniswap-tokenized-stocks-delisting-2021-07` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-16 | 1 | ok | no_audit_recorded |
| `unsc-resolution-2371-dprk-crypto-2017` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-17 | 0 | ok | no_audit_recorded |
| `uzbekistan-napp-vasp-licensing-2022-07` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-17 | 0 | ok | no_audit_recorded |
| `voyager-bankruptcy-doj-objection-2023` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-17 | 0 | ok | no_audit_recorded |
| `welcome-to-video-doj-2019` | `admitted` | `human_reviewed` | 2026-05-16 | 1 | ok | 2026-05-16 | 1 | ok | ok |
| `wikileaks-amazon-aws-eviction-2010-12` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-16 | 1 | ok | no_audit_recorded |
| `wikileaks-bank-of-america-block-2010-12` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-16 | 1 | ok | no_audit_recorded |
| `wikileaks-everydns-domain-termination-2010-12` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-16 | 1 | ok | no_audit_recorded |
| `wikileaks-mastercard-suspension-2010-12` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-16 | 1 | ok | no_audit_recorded |
| `wikileaks-paypal-freeze-2010-12` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-16 | 1 | ok | no_audit_recorded |
| `wikileaks-postfinance-account-closure-2010-12` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-16 | 1 | ok | no_audit_recorded |
| `wikileaks-visa-europe-suspension-2010-12` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-16 | 1 | ok | no_audit_recorded |
| `wikileaks-wau-holland-tax-status-challenge-2010-12` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-17 | 0 | ok | no_audit_recorded |
| `wikileaks-western-union-interdiction-2010-12` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-16 | 1 | ok | no_audit_recorded |
| `zservers-ofac-2025` | `admitted` | `human_authored` | 2026-05-15 | 2 | ok | 2026-04-22 | 25 | ok | ok |

## Events flagged (any non-`ok` summary)

- `1inch-us-geofence-2021-09` — audit=no_audit_recorded, verification=ok, verif_age=1d
- `aave-arc-fireblocks-whitelist-2022-01` — audit=no_audit_recorded, verification=ok, verif_age=1d
- `aave-tornado-frontend-block-2022-08` — audit=no_audit_recorded, verification=ok, verif_age=1d
- `aeza-group-ofac-2025` — audit=no_audit_recorded, verification=ok, verif_age=25d
- `apple-india-crypto-exchange-removal-2024-01` — audit=no_audit_recorded, verification=ok, verif_age=1d
- `argentina-cnv-psav-registration-2024` — audit=no_audit_recorded, verification=ok, verif_age=0d
- `argentina-uif-resolution-300-2014` — audit=no_audit_recorded, verification=ok, verif_age=0d
- `augur-v2-us-uk-geofence-2020-07` — audit=no_audit_recorded, verification=ok, verif_age=0d
- `bangladesh-bb-bitcoin-warning-2014` — audit=no_audit_recorded, verification=ok, verif_age=0d
- `binance-4framework-2023` — audit=no_audit_recorded, verification=ok, verif_age=25d
- `binance-busd-wind-down-2024` — audit=no_audit_recorded, verification=ok, verif_age=0d
- `bitcoinica-shutdown-2012-05` — audit=no_audit_recorded, verification=ok, verif_age=0d
- `bitfinex-tether-nyag-2021` — audit=no_audit_recorded, verification=ok, verif_age=0d
- `bitmex-fincen-2024` — audit=no_audit_recorded, verification=ok, verif_age=0d
- `bitstamp-greece-portugal-exit-2023` — audit=no_audit_recorded, verification=ok, verif_age=0d
- `bitzlato-doj-2023` — audit=no_audit_recorded, verification=ok, verif_age=26d
- `blender-ofac-2022` — audit=no_audit_recorded, verification=ok, verif_age=26d
- `bolivia-bcb-crypto-prohibition-2014` — audit=no_audit_recorded, verification=ok, verif_age=0d
- `brazil-bacen-stablecoin-restriction-2023` — audit=no_audit_recorded, verification=ok, verif_age=0d
- `brazil-bcb-comunicado-25306-2014` — audit=no_audit_recorded, verification=ok, verif_age=0d
- `btc-e-doj-2017` — audit=no_audit_recorded, verification=ok, verif_age=25d
- `bybit-singapore-exit-2022` — audit=no_audit_recorded, verification=ok, verif_age=0d
- `canada-convoy-freeze-2022` — audit=no_audit_recorded, verification=ok, verif_age=25d
- `cftc-v-ftx-2022` — audit=no_audit_recorded, verification=ok, verif_age=0d
- `cftc-v-ooki-dao-2022` — audit=no_audit_recorded, verification=ok, verif_age=25d
- `chatex-ofac-2021` — audit=no_audit_recorded, verification=ok, verif_age=25d
- `china-inner-mongolia-mining-ban-2021-05` — audit=no_audit_recorded, verification=ok, verif_age=1d
- `china-nft-secondary-trading-self-discipline-2022-06` — audit=no_audit_recorded, verification=ok, verif_age=1d
- `china-pboc-crypto-ban-2021` — audit=no_audit_recorded, verification=ok, verif_age=26d
- `china-pboc-exchange-shutdown-2017-09` — audit=no_audit_recorded, verification=ok, verif_age=1d
- `china-sichuan-mining-ban-2021-06` — audit=no_audit_recorded, verification=ok, verif_age=1d
- `china-state-council-mining-crackdown-2021-05` — audit=no_audit_recorded, verification=ok, verif_age=1d
- `china-weibo-crypto-exchange-purge-2021-03` — audit=no_audit_recorded, verification=ok, verif_age=0d
- `chipmixer-doj-2023` — audit=no_audit_recorded, verification=ok, verif_age=25d
- `circle-usdc-cryptex-freeze-2024` — audit=no_audit_recorded, verification=ok, verif_age=0d
- `circle-usdc-svb-policy-statement-2023` — audit=no_audit_recorded, verification=ok, verif_age=0d
- `circle-usdc-tornado-2022` — audit=no_audit_recorded, verification=ok, verif_age=25d
- `cloudflare-ethereum-gateway-tornado-block-2022-08` — audit=no_audit_recorded, verification=ok, verif_age=1d
- `coin-mx-doj-murgio-2015` — audit=no_audit_recorded, verification=ok, verif_age=1d
- `coinbase-india-exit-2022` — audit=no_audit_recorded, verification=ok, verif_age=25d
- `coinbase-japan-exit-2023` — audit=no_audit_recorded, verification=ok, verif_age=0d
- `consensys-metamask-infura-rpc-data-collection-2022-11` — audit=no_audit_recorded, verification=ok, verif_age=0d
- `datacell-v-valitor-iceland-district-court-2012-07` — audit=no_audit_recorded, verification=ok, verif_age=1d
- `dprk-usdt-network-ofac-2025` — audit=no_audit_recorded, verification=ok, verif_age=25d
- `dydx-tornado-account-block-2022-08` — audit=no_audit_recorded, verification=ok, verif_age=1d
- `eba-virtual-currencies-opinion-eba-op-2014-08` — audit=no_audit_recorded, verification=ok, verif_age=1d
- `ebullion-doj-fbi-seizure-2008-08` — audit=no_audit_recorded, verification=ok, verif_age=0d
- `egold-doj-guilty-plea-2008-07` — audit=no_audit_recorded, verification=ok, verif_age=1d
- `ens-eth-domain-tornado-resolution-2022` — audit=no_audit_recorded, verification=ok, verif_age=0d
- `etherscan-tornado-cash-ui-label-2022` — audit=no_audit_recorded, verification=ok, verif_age=0d
- `eu-12th-russia-sanctions-2023` — audit=no_audit_recorded, verification=ok, verif_age=25d
- `eu-14th-russia-sanctions-spfs-2024` — audit=no_audit_recorded, verification=ok, verif_age=0d
- `eu-15th-russia-sanctions-2024` — audit=no_audit_recorded, verification=ok, verif_age=0d
- `eu-amla-anti-money-laundering-authority-regulation-2024` — audit=no_audit_recorded, verification=ok, verif_age=0d
- `eu-amlr-eu-single-rulebook-2024` — audit=no_audit_recorded, verification=ok, verif_age=0d
- `eu-dac8-crypto-asset-reporting-directive-2023` — audit=no_audit_recorded, verification=ok, verif_age=0d
- `eu-mica-2023` — audit=no_audit_recorded, verification=ok, verif_age=25d
- `fatf-grey-list-crypto-related-actions-2023-2024` — audit=no_audit_recorded, verification=ok, verif_age=0d
- `fatf-targeted-update-va-vasp-2021` — audit=no_audit_recorded, verification=ok, verif_age=0d
- `fatf-targeted-update-va-vasp-2023` — audit=no_audit_recorded, verification=ok, verif_age=0d
- `fatf-virtual-currencies-key-definitions-2014` — audit=no_audit_recorded, verification=ok, verif_age=1d
- `fbi-bitcoin-intelligence-assessment-2012-04` — audit=no_audit_recorded, verification=ok, verif_age=0d
- `fincen-virtual-currency-msb-guidance-2013` — audit=no_audit_recorded, verification=ok, verif_age=1d
- `france-amf-binance-psan-2022` — audit=no_audit_recorded, verification=ok, verif_age=0d
- `fsb-crypto-asset-recommendations-2023` — audit=no_audit_recorded, verification=ok, verif_age=0d
- `funnull-cdn-ofac-2025` — audit=no_audit_recorded, verification=ok, verif_age=25d
- `g20-roadmap-crypto-asset-policy-2023` — audit=no_audit_recorded, verification=ok, verif_age=0d
- `g7-hiroshima-crypto-statement-2023` — audit=no_audit_recorded, verification=ok, verif_age=0d
- `garantex-ofac-2022` — audit=no_audit_recorded, verification=ok, verif_age=26d
- `google-play-india-crypto-exchange-removal-2024-01` — audit=no_audit_recorded, verification=ok, verif_age=1d
- `grinex-garantex-successor-ofac-2025` — audit=no_audit_recorded, verification=ok, verif_age=26d
- `hongkong-hkma-stablecoins-ordinance-2025` — audit=no_audit_recorded, verification=ok, verif_age=1d
- `hongkong-sfc-bybit-warning-2024` — audit=no_audit_recorded, verification=ok, verif_age=0d
- `hongkong-sfc-jpex-block-2023` — audit=no_audit_recorded, verification=ok, verif_age=0d
- `hongkong-sfc-vatp-licensing-2023-06` — audit=no_audit_recorded, verification=ok, verif_age=1d
- `huobi-htx-privacy-coin-delisting-2024` — audit=no_audit_recorded, verification=ok, verif_age=0d
- `hydra-doj-2022` — audit=no_audit_recorded, verification=ok, verif_age=25d
- `hydra-ofac-2022` — audit=no_audit_recorded, verification=ok, verif_age=26d
- `iceland-cbi-foreign-exchange-bitcoin-2014` — audit=no_audit_recorded, verification=ok, verif_age=1d
- `india-rbi-crypto-ban-2018` — audit=no_audit_recorded, verification=ok, verif_age=25d
- `indonesia-bappebti-illegal-exchange-block-2023` — audit=no_audit_recorded, verification=ok, verif_age=0d
- `indonesia-bi-bitcoin-warning-2014` — audit=no_audit_recorded, verification=ok, verif_age=0d
- `infura-metamask-donetsk-luhansk-block-2022-03` — audit=no_audit_recorded, verification=ok, verif_age=1d
- `iran-cbi-crypto-banking-prohibition-2018` — audit=no_audit_recorded, verification=ok, verif_age=0d
- `iran-government-mining-electricity-restriction-2021` — audit=no_audit_recorded, verification=ok, verif_age=0d
- `israel-nbctf-hamas-crypto-addresses-2021` — audit=no_audit_recorded, verification=ok, verif_age=0d
- `japan-fsa-binance-sakura-acquisition-2022-11` — audit=no_audit_recorded, verification=ok, verif_age=0d
- `japan-fsa-binance-warning-2018` — audit=no_audit_recorded, verification=ok, verif_age=0d
- `japan-fsa-dmm-bitcoin-order-2024-09` — audit=no_audit_recorded, verification=ok, verif_age=1d
- `japan-fsa-ftx-japan-suspension-2022-11` — audit=no_audit_recorded, verification=ok, verif_age=1d
- `japan-fsa-six-exchange-orders-2018-06` — audit=no_audit_recorded, verification=ok, verif_age=1d
- `japan-fsa-stablecoin-psa-effective-2023-06` — audit=no_audit_recorded, verification=ok, verif_age=1d
- `japan-fsa-travel-rule-effective-2023-06` — audit=no_audit_recorded, verification=ok, verif_age=1d
- `japan-fsa-zaif-orders-2018-09` — audit=no_audit_recorded, verification=ok, verif_age=1d
- `karpeles-arrest-tokyo-mtgox-2015` — audit=no_audit_recorded, verification=ok, verif_age=1d
- `kazakhstan-digital-assets-law-2023-02` — audit=no_audit_recorded, verification=ok, verif_age=1d
- `kazakhstan-internet-shutdown-mining-2022-01` — audit=no_audit_recorded, verification=ok, verif_age=1d
- `korea-travel-rule-2022` — audit=no_audit_recorded, verification=ok, verif_age=25d
- `kraken-monero-eu-delisting-2024` — audit=no_audit_recorded, verification=ok, verif_age=0d
- `kraken-uk-derivatives-exit-2021` — audit=no_audit_recorded, verification=ok, verif_age=0d
- `kucoin-canada-exit-2023` — audit=no_audit_recorded, verification=ok, verif_age=0d
- `kucoin-netherlands-exit-2023` — audit=no_audit_recorded, verification=ok, verif_age=0d
- `liberty-reserve-costa-rica-license-denial-2011-03` — audit=no_audit_recorded, verification=ok, verif_age=0d
- `lockbit-affiliates-ofac-2024` — audit=no_audit_recorded, verification=ok, verif_age=25d
- `makerdao-emergency-shutdown-contingency-2022-08` — audit=no_audit_recorded, verification=ok, verif_age=0d
- `metamask-eth-phishing-detect-tornado-additions-2022` — audit=no_audit_recorded, verification=ok, verif_age=0d
- `metamask-snaps-region-restrictions-2023-09` — audit=no_audit_recorded, verification=ok, verif_age=0d
- `mica-l2-esma-eba-rts-2024` — audit=no_audit_recorded, verification=ok, verif_age=0d
- `mtgox-bankruptcy-tokyo-2014` — audit=no_audit_recorded, verification=ok, verif_age=1d
- `mtgox-coinlab-civil-2013` — audit=no_audit_recorded, verification=ok, verif_age=1d
- `mtgox-dhs-dwolla-wells-fargo-seizure-2013` — audit=no_audit_recorded, verification=ok, verif_age=1d
- `mtgox-june-2011-hack-trading-suspension` — audit=no_audit_recorded, verification=ok, verif_age=0d
- `mtgox-mizuho-wire-pressure-2012` — audit=no_audit_recorded, verification=ok, verif_age=0d
- `mtgox-usd-withdrawal-suspension-2013-06` — audit=no_audit_recorded, verification=ok, verif_age=1d
- `nigeria-cbn-crypto-ban-2021` — audit=no_audit_recorded, verification=ok, verif_age=25d
- `nydfs-bitlicense-bitfinex-kraken-shapeshift-exit-2015` — audit=no_audit_recorded, verification=ok, verif_age=1d
- `oasis-app-wormhole-counter-exploit-2023-02` — audit=no_audit_recorded, verification=ok, verif_age=0d
- `ofac-dprk-it-worker-sim-hyon-sop-2023-04` — audit=no_audit_recorded, verification=ok, verif_age=0d
- `ofac-hamas-buy-cash-msb-2023-10` — audit=no_audit_recorded, verification=ok, verif_age=1d
- `ofac-hamas-gaza-now-2024-03` — audit=no_audit_recorded, verification=ok, verif_age=1d
- `ofac-hamas-irgc-virtual-currency-network-2024-01` — audit=no_audit_recorded, verification=ok, verif_age=1d
- `ofac-houthi-al-jamal-crypto-refresh-2024-12` — audit=no_audit_recorded, verification=ok, verif_age=0d
- `ofac-recent-action-20240111` — audit=no_audit_recorded, verification=ok, verif_age=1d
- `ofac-trickbot-conti-eleven-2023-09` — audit=no_audit_recorded, verification=ok, verif_age=1d
- `ofac-zhdanova-russian-elite-launderer-2023-11` — audit=no_audit_recorded, verification=ok, verif_age=1d
- `okx-monero-global-delisting-2024` — audit=no_audit_recorded, verification=ok, verif_age=0d
- `opensea-iran-cuba-sanctions-block-2022` — audit=no_audit_recorded, verification=ok, verif_age=1d
- `paxos-busd-nydfs-minting-stop-2023` — audit=no_audit_recorded, verification=ok, verif_age=1d
- `pecunix-bullion-transfer-2008` — audit=no_audit_recorded, verification=ok, verif_age=0d
- `philippines-sec-binance-block-2024` — audit=no_audit_recorded, verification=ok, verif_age=1d
- `polymarket-cftc-geofence-2022-01` — audit=no_audit_recorded, verification=ok, verif_age=1d
- `polynonce-bittrex-fincen-2022` — audit=no_audit_recorded, verification=ok, verif_age=0d
- `pump-fun-uk-fca-geofence-2024-12` — audit=no_audit_recorded, verification=ok, verif_age=0d
- `ren-protocol-shutdown-alameda-ftx-2022-12` — audit=no_audit_recorded, verification=ok, verif_age=0d
- `russia-cbr-bitcoin-information-letter-2014` — audit=no_audit_recorded, verification=ok, verif_age=1d
- `russia-cbr-crypto-payment-ban-2022` — audit=no_audit_recorded, verification=ok, verif_age=0d
- `russia-dfa-law-2020` — audit=no_audit_recorded, verification=ok, verif_age=0d
- `russia-election-interference-ofac-2020` — audit=no_audit_recorded, verification=ok, verif_age=25d
- `russia-mining-legalization-law-2024-08` — audit=no_audit_recorded, verification=ok, verif_age=0d
- `russia-mining-regional-ban-2024-12` — audit=no_audit_recorded, verification=ok, verif_age=1d
- `russia-rosfinmonitoring-binance-russia-rails-2022` — audit=no_audit_recorded, verification=ok, verif_age=0d
- `russian-cyber-theft-ofac-2020` — audit=no_audit_recorded, verification=ok, verif_age=25d
- `salame-ftx-campaign-finance-doj-2023` — audit=no_audit_recorded, verification=ok, verif_age=0d
- `samourai-doj-2024` — audit=no_audit_recorded, verification=ok, verif_age=25d
- `sec-garza-gaw-miners-zenminer-2015` — audit=no_audit_recorded, verification=ok, verif_age=1d
- `sec-v-coinbase-staking-wells-2023` — audit=no_audit_recorded, verification=ok, verif_age=0d
- `sec-v-ftx-2022` — audit=no_audit_recorded, verification=ok, verif_age=0d
- `sec-v-uniswap-wells-notice-2024` — audit=no_audit_recorded, verification=ok, verif_age=11d
- `singapore-mas-retail-crypto-restriction-2022` — audit=no_audit_recorded, verification=ok, verif_age=0d
- `south-africa-fsca-crypto-financial-product-2022` — audit=no_audit_recorded, verification=ok, verif_age=0d
- `suex-ofac-2021` — audit=no_audit_recorded, verification=ok, verif_age=26d
- `switzerland-finma-tezos-zg-2018` — audit=no_audit_recorded, verification=ok, verif_age=0d
- `tether-doj-pig-butchering-freeze-2023` — audit=no_audit_recorded, verification=ok, verif_age=25d
- `tether-dprk-precommit-freeze-2025` — audit=no_audit_recorded, verification=ok, verif_age=25d
- `tether-pig-butchering-second-wave-2024` — audit=no_audit_recorded, verification=ok, verif_age=0d
- `tether-tron-philippines-pdea-freeze-2024` — audit=no_audit_recorded, verification=ok, verif_age=0d
- `thailand-bot-bitcoin-prohibition-2013` — audit=no_audit_recorded, verification=ok, verif_age=0d
- `thailand-sec-binance-bybit-c-and-d-2021` — audit=no_audit_recorded, verification=ok, verif_age=0d
- `tornado-cash-frontend-tornado-cash-eth-block-2022-04` — audit=no_audit_recorded, verification=ok, verif_age=0d
- `tornado-cash-github-takedown-2022-08` — audit=no_audit_recorded, verification=ok, verif_age=0d
- `tornado-cash-ofac-delisting-2025` — audit=no_audit_recorded, verification=ok, verif_age=26d
- `tornado-cash-pertsev-doj-indictment-2023` — audit=no_audit_recorded, verification=ok, verif_age=0d
- `tornado-cash-tornadocash-org-seizure-2022` — audit=no_audit_recorded, verification=ok, verif_age=0d
- `trustwallet-sanctioned-token-ui-update-2022` — audit=no_audit_recorded, verification=ok, verif_age=0d
- `turkey-cbrt-crypto-ban-2021` — audit=no_audit_recorded, verification=ok, verif_age=25d
- `turkey-cmb-casp-licensing-law-7518-2024` — audit=no_audit_recorded, verification=ok, verif_age=0d
- `uae-vara-licence-issuance-regime-2023` — audit=no_audit_recorded, verification=ok, verif_age=0d
- `uk-fca-binance-markets-2021` — audit=no_audit_recorded, verification=ok, verif_age=1d
- `uk-fca-crypto-promotion-rule-2023` — audit=no_audit_recorded, verification=ok, verif_age=0d
- `uk-hmrc-bitcoin-vat-brief-09-14-2014` — audit=no_audit_recorded, verification=ok, verif_age=0d
- `ukraine-virtual-assets-law-2022-03` — audit=no_audit_recorded, verification=ok, verif_age=1d
- `uniswap-balancer-tornado-frontend-block-2022-08` — audit=no_audit_recorded, verification=ok, verif_age=1d
- `uniswap-frontend-delisting-2023` — audit=no_audit_recorded, verification=ok, verif_age=25d
- `uniswap-token-list-curation-default-2021` — audit=no_audit_recorded, verification=ok, verif_age=0d
- `uniswap-tokenized-stocks-delisting-2021-07` — audit=no_audit_recorded, verification=ok, verif_age=1d
- `unsc-resolution-2371-dprk-crypto-2017` — audit=no_audit_recorded, verification=ok, verif_age=0d
- `uzbekistan-napp-vasp-licensing-2022-07` — audit=no_audit_recorded, verification=ok, verif_age=0d
- `voyager-bankruptcy-doj-objection-2023` — audit=no_audit_recorded, verification=ok, verif_age=0d
- `wikileaks-amazon-aws-eviction-2010-12` — audit=no_audit_recorded, verification=ok, verif_age=1d
- `wikileaks-bank-of-america-block-2010-12` — audit=no_audit_recorded, verification=ok, verif_age=1d
- `wikileaks-everydns-domain-termination-2010-12` — audit=no_audit_recorded, verification=ok, verif_age=1d
- `wikileaks-mastercard-suspension-2010-12` — audit=no_audit_recorded, verification=ok, verif_age=1d
- `wikileaks-paypal-freeze-2010-12` — audit=no_audit_recorded, verification=ok, verif_age=1d
- `wikileaks-postfinance-account-closure-2010-12` — audit=no_audit_recorded, verification=ok, verif_age=1d
- `wikileaks-visa-europe-suspension-2010-12` — audit=no_audit_recorded, verification=ok, verif_age=1d
- `wikileaks-wau-holland-tax-status-challenge-2010-12` — audit=no_audit_recorded, verification=ok, verif_age=0d
- `wikileaks-western-union-interdiction-2010-12` — audit=no_audit_recorded, verification=ok, verif_age=1d
