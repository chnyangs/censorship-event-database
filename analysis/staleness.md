# Staleness report

Generated at: `2026-05-24T00:00:00Z`
Red threshold: audits / verifications older than `90` days.
Most recent agent activity in `candidate_triggers/`: `none recorded`.

## Coverage snapshot

Two dimensions tracked per event; missing values surface as explicit gaps, never masked.

- **Adversarial audit** (`last_human_audit`): {'no_audit_recorded': 95, 'ok': 72}
- **Verification** (`last_verified`): {'ok': 167}
- **Row-level summary** (worst of the two): {'no_audit_recorded': 95, 'ok': 72}

## Flag legend

- `ok` — within the red threshold
- `red` — older than 90 days
- `no_audit_recorded` — no last_human_audit on record — event has never been through an adversarial audit
- `no_verification_recorded` — no last_verified on record — event has never been re-verified
- `error` — event YAML failed to parse

## Per-event table

| Event | Status | Origin | last_human_audit | Audit age | Audit flag | last_verified | Verification age | Verif flag | Summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `1inch-us-geofence-2021-09` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-16 | 8 | ok | no_audit_recorded |
| `aave-arc-fireblocks-whitelist-2022-01` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-16 | 8 | ok | no_audit_recorded |
| `aave-tornado-frontend-block-2022-08` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-16 | 8 | ok | no_audit_recorded |
| `aeza-group-ofac-2025` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-22 | 32 | ok | no_audit_recorded |
| `alphabay-hansa-doj-2017` | `admitted` | `human_reviewed` | 2026-05-16 | 8 | ok | 2026-05-16 | 8 | ok | ok |
| `apple-india-crypto-exchange-removal-2024-01` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-16 | 8 | ok | no_audit_recorded |
| `australia-asic-binance-derivatives-2023` | `admitted` | `human_reviewed` | 2026-05-16 | 8 | ok | 2026-05-16 | 8 | ok | ok |
| `belgium-fsma-binance-cease-2023` | `admitted` | `human_reviewed` | 2026-05-16 | 8 | ok | 2026-05-16 | 8 | ok | ok |
| `binance-4framework-2023` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-22 | 32 | ok | no_audit_recorded |
| `binance-cftc-2023` | `admitted` | `human_reviewed` | 2026-05-16 | 8 | ok | 2026-05-16 | 8 | ok | ok |
| `binance-privacy-coin-delisting-2023` | `admitted` | `human_reviewed` | 2026-05-16 | 8 | ok | 2026-05-16 | 8 | ok | ok |
| `binance-russia-exit-commex-2023` | `admitted` | `human_reviewed` | 2026-05-16 | 8 | ok | 2026-05-16 | 8 | ok | ok |
| `binance-us-staking-end-2023` | `admitted` | `human_reviewed` | 2026-05-16 | 8 | ok | 2026-05-16 | 8 | ok | ok |
| `bitfinex-cftc-retail-commodity-2016` | `admitted` | `human_reviewed` | 2026-05-16 | 8 | ok | 2026-05-16 | 8 | ok | ok |
| `bitfinex-tether-cftc-2021` | `admitted` | `human_reviewed` | 2026-05-16 | 8 | ok | 2026-05-16 | 8 | ok | ok |
| `bitmex-cftc-doj-2020` | `admitted` | `human_reviewed` | 2026-05-16 | 8 | ok | 2026-05-16 | 8 | ok | ok |
| `bitzlato-doj-2023` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-21 | 33 | ok | no_audit_recorded |
| `blender-ofac-2022` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-21 | 33 | ok | no_audit_recorded |
| `blockfi-sec-lending-2022` | `admitted` | `human_reviewed` | 2026-05-16 | 8 | ok | 2026-05-16 | 8 | ok | ok |
| `btc-e-doj-2017` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-22 | 32 | ok | no_audit_recorded |
| `canada-convoy-freeze-2022` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-22 | 32 | ok | no_audit_recorded |
| `canada-csa-binance-withdrawal-2023` | `admitted` | `human_reviewed` | 2026-05-16 | 8 | ok | 2026-05-16 | 8 | ok | ok |
| `celsius-bankruptcy-mashinsky-doj-2023` | `admitted` | `human_reviewed` | 2026-05-16 | 8 | ok | 2026-05-16 | 8 | ok | ok |
| `cftc-v-ooki-dao-2022` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-22 | 32 | ok | no_audit_recorded |
| `chatex-ofac-2021` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-22 | 32 | ok | no_audit_recorded |
| `china-ico-ban-2017-09` | `draft` | `agent_draft` | 2026-05-16 | 8 | ok | 2026-05-16 | 8 | ok | ok |
| `china-inner-mongolia-mining-ban-2021-05` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-16 | 8 | ok | no_audit_recorded |
| `china-nft-secondary-trading-self-discipline-2022-06` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-16 | 8 | ok | no_audit_recorded |
| `china-pboc-crypto-ban-2013-12` | `admitted` | `human_reviewed` | 2026-05-16 | 8 | ok | 2026-05-16 | 8 | ok | ok |
| `china-pboc-crypto-ban-2021` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-21 | 33 | ok | no_audit_recorded |
| `china-pboc-exchange-shutdown-2017-09` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-16 | 8 | ok | no_audit_recorded |
| `china-sichuan-mining-ban-2021-06` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-16 | 8 | ok | no_audit_recorded |
| `china-state-council-mining-crackdown-2021-05` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-16 | 8 | ok | no_audit_recorded |
| `chipmixer-doj-2023` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-22 | 32 | ok | no_audit_recorded |
| `circle-usdc-tornado-2022` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-22 | 32 | ok | no_audit_recorded |
| `cloudflare-ethereum-gateway-tornado-block-2022-08` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-16 | 8 | ok | no_audit_recorded |
| `coin-mx-doj-murgio-2015` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-16 | 8 | ok | no_audit_recorded |
| `coinbase-india-exit-2022` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-22 | 32 | ok | no_audit_recorded |
| `coinbase-irs-john-doe-summons-2016` | `admitted` | `human_reviewed` | 2026-05-16 | 8 | ok | 2026-05-16 | 8 | ok | ok |
| `coinflip-cftc-derivabit-2015` | `admitted` | `human_reviewed` | 2026-05-16 | 8 | ok | 2026-05-16 | 8 | ok | ok |
| `cryptex-ofac-2024` | `admitted` | `human_authored` | 2026-04-22 | 32 | ok | 2026-04-21 | 33 | ok | ok |
| `datacell-v-valitor-iceland-district-court-2012-07` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-16 | 8 | ok | no_audit_recorded |
| `dprk-usdt-network-ofac-2025` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-22 | 32 | ok | no_audit_recorded |
| `dydx-tornado-account-block-2022-08` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-16 | 8 | ok | no_audit_recorded |
| `eba-virtual-currencies-opinion-eba-op-2014-08` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-16 | 8 | ok | no_audit_recorded |
| `egold-doj-guilty-plea-2008-07` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-16 | 8 | ok | no_audit_recorded |
| `eu-12th-russia-sanctions-2023` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-22 | 32 | ok | no_audit_recorded |
| `eu-mica-2023` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-22 | 32 | ok | no_audit_recorded |
| `eu-russia-crypto-wallet-cap-2022` | `admitted` | `human_reviewed` | 2026-05-16 | 8 | ok | 2026-05-16 | 8 | ok | ok |
| `eu-russia-full-crypto-wallet-ban-2022` | `admitted` | `human_reviewed` | 2026-05-16 | 8 | ok | 2026-05-16 | 8 | ok | ok |
| `eu-tfr-recast-2023` | `admitted` | `human_reviewed` | 2026-05-16 | 8 | ok | 2026-05-16 | 8 | ok | ok |
| `fatf-r15-vasp-travel-rule-2019` | `admitted` | `human_reviewed` | 2026-05-16 | 8 | ok | 2026-05-16 | 8 | ok | ok |
| `fatf-virtual-currencies-key-definitions-2014` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-16 | 8 | ok | no_audit_recorded |
| `fincen-virtual-currency-msb-guidance-2013` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-16 | 8 | ok | no_audit_recorded |
| `ftx-bankman-fried-doj-2022` | `admitted` | `human_reviewed` | 2026-05-16 | 8 | ok | 2026-05-16 | 8 | ok | ok |
| `funnull-cdn-ofac-2025` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-22 | 32 | ok | no_audit_recorded |
| `garantex-ofac-2022` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-21 | 33 | ok | no_audit_recorded |
| `genesis-sec-gemini-earn-2023` | `admitted` | `human_reviewed` | 2026-05-16 | 8 | ok | 2026-05-16 | 8 | ok | ok |
| `germany-bafin-binance-licence-withdrawal-2023` | `admitted` | `human_reviewed` | 2026-05-16 | 8 | ok | 2026-05-16 | 8 | ok | ok |
| `google-play-india-crypto-exchange-removal-2024-01` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-16 | 8 | ok | no_audit_recorded |
| `grinex-garantex-successor-ofac-2025` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-21 | 33 | ok | no_audit_recorded |
| `helix-doj-mixer-2020` | `admitted` | `human_reviewed` | 2026-05-16 | 8 | ok | 2026-05-16 | 8 | ok | ok |
| `hongkong-hkma-stablecoins-ordinance-2025` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-16 | 8 | ok | no_audit_recorded |
| `hongkong-sfc-vatp-licensing-2023-06` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-16 | 8 | ok | no_audit_recorded |
| `hydra-doj-2022` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-22 | 32 | ok | no_audit_recorded |
| `hydra-ofac-2022` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-21 | 33 | ok | no_audit_recorded |
| `iceland-cbi-foreign-exchange-bitcoin-2014` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-16 | 8 | ok | no_audit_recorded |
| `india-fiu-offshore-vda-block-2023` | `admitted` | `human_reviewed` | 2026-05-16 | 8 | ok | 2026-05-16 | 8 | ok | ok |
| `india-rbi-crypto-ban-2018` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-22 | 32 | ok | no_audit_recorded |
| `infura-alchemy-tornado-rpc-block-2022` | `admitted` | `human_reviewed` | 2026-05-16 | 8 | ok | 2026-05-16 | 8 | ok | ok |
| `infura-metamask-donetsk-luhansk-block-2022-03` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-16 | 8 | ok | no_audit_recorded |
| `iran-ransomware-ofac-2018` | `admitted` | `human_authored` | 2026-05-15 | 9 | ok | 2026-04-22 | 32 | ok | ok |
| `irgc-ransomware-ofac-2022` | `admitted` | `human_authored` | 2026-05-15 | 9 | ok | 2026-04-22 | 32 | ok | ok |
| `japan-fsa-coincheck-orders-2018` | `admitted` | `human_reviewed` | 2026-05-16 | 8 | ok | 2026-05-16 | 8 | ok | ok |
| `japan-fsa-dmm-bitcoin-order-2024-09` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-16 | 8 | ok | no_audit_recorded |
| `japan-fsa-ftx-japan-suspension-2022-11` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-16 | 8 | ok | no_audit_recorded |
| `japan-fsa-six-exchange-orders-2018-06` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-16 | 8 | ok | no_audit_recorded |
| `japan-fsa-stablecoin-psa-effective-2023-06` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-16 | 8 | ok | no_audit_recorded |
| `japan-fsa-travel-rule-effective-2023-06` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-16 | 8 | ok | no_audit_recorded |
| `japan-fsa-zaif-orders-2018-09` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-16 | 8 | ok | no_audit_recorded |
| `karpeles-arrest-tokyo-mtgox-2015` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-16 | 8 | ok | no_audit_recorded |
| `kazakhstan-digital-assets-law-2023-02` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-16 | 8 | ok | no_audit_recorded |
| `kazakhstan-internet-shutdown-mining-2022-01` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-16 | 8 | ok | no_audit_recorded |
| `korea-fsc-ico-ban-2017` | `admitted` | `human_reviewed` | 2026-05-16 | 8 | ok | 2026-05-16 | 8 | ok | ok |
| `korea-travel-rule-2022` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-22 | 32 | ok | no_audit_recorded |
| `kraken-sec-staking-2023` | `admitted` | `human_reviewed` | 2026-05-16 | 8 | ok | 2026-05-16 | 8 | ok | ok |
| `kraken-sec-unregistered-exchange-2023` | `admitted` | `human_reviewed` | 2026-05-16 | 8 | ok | 2026-05-16 | 8 | ok | ok |
| `kucoin-doj-2024` | `admitted` | `human_reviewed` | 2026-05-16 | 8 | ok | 2026-05-16 | 8 | ok | ok |
| `lazarus-entity-ofac-2019` | `admitted` | `human_authored` | 2026-05-15 | 9 | ok | 2026-04-22 | 32 | ok | ok |
| `lazarus-laundering-ofac-2020` | `admitted` | `human_authored` | 2026-05-15 | 9 | ok | 2026-04-22 | 32 | ok | ok |
| `lockbit-affiliates-ofac-2024` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-22 | 32 | ok | no_audit_recorded |
| `lockbit-leader-ofac-2024` | `admitted` | `human_authored` | 2026-05-15 | 9 | ok | 2026-04-22 | 32 | ok | ok |
| `malaysia-sc-binance-disable-2021` | `admitted` | `human_reviewed` | 2026-05-16 | 8 | ok | 2026-05-16 | 8 | ok | ok |
| `matveev-ofac-2023` | `admitted` | `human_authored` | 2026-05-15 | 9 | ok | 2026-04-22 | 32 | ok | ok |
| `mtgox-bankruptcy-tokyo-2014` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-16 | 8 | ok | no_audit_recorded |
| `mtgox-coinlab-civil-2013` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-16 | 8 | ok | no_audit_recorded |
| `mtgox-dhs-dwolla-wells-fargo-seizure-2013` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-16 | 8 | ok | no_audit_recorded |
| `mtgox-usd-withdrawal-suspension-2013-06` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-16 | 8 | ok | no_audit_recorded |
| `netherlands-dnb-binance-warning-2021` | `admitted` | `human_reviewed` | 2026-05-16 | 8 | ok | 2026-05-16 | 8 | ok | ok |
| `nigeria-cbn-crypto-ban-2021` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-22 | 32 | ok | no_audit_recorded |
| `nydfs-bitlicense-2015-06` | `admitted` | `human_reviewed` | 2026-05-16 | 8 | ok | 2026-05-16 | 8 | ok | ok |
| `nydfs-bitlicense-bitfinex-kraken-shapeshift-exit-2015` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-16 | 8 | ok | no_audit_recorded |
| `oecd-carf-2022` | `admitted` | `human_reviewed` | 2026-05-16 | 8 | ok | 2026-05-16 | 8 | ok | ok |
| `ofac-hamas-buy-cash-msb-2023-10` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-16 | 8 | ok | no_audit_recorded |
| `ofac-hamas-gaza-now-2024-03` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-16 | 8 | ok | no_audit_recorded |
| `ofac-hamas-irgc-virtual-currency-network-2024-01` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-16 | 8 | ok | no_audit_recorded |
| `ofac-recent-action-20240111` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-16 | 8 | ok | no_audit_recorded |
| `ofac-trickbot-conti-eleven-2023-09` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-16 | 8 | ok | no_audit_recorded |
| `ofac-zhdanova-russian-elite-launderer-2023-11` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-16 | 8 | ok | no_audit_recorded |
| `okx-privacy-token-delist-2024` | `admitted` | `human_reviewed` | 2026-05-16 | 8 | ok | 2026-05-16 | 8 | ok | ok |
| `opensea-iran-cuba-sanctions-block-2022` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-16 | 8 | ok | no_audit_recorded |
| `paxos-busd-nydfs-minting-stop-2023` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-16 | 8 | ok | no_audit_recorded |
| `pertsev-nl-arrest-2022` | `admitted` | `human_authored` | 2026-05-15 | 9 | ok | 2026-04-22 | 32 | ok | ok |
| `philippines-sec-binance-block-2024` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-16 | 8 | ok | no_audit_recorded |
| `polymarket-cftc-geofence-2022-01` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-16 | 8 | ok | no_audit_recorded |
| `powell-unlicensed-bitcoin-exchange-2014` | `admitted` | `human_reviewed` | 2026-05-16 | 8 | ok | 2026-05-16 | 8 | ok | ok |
| `ripple-fincen-xrp-2015` | `admitted` | `human_reviewed` | 2026-05-16 | 8 | ok | 2026-05-16 | 8 | ok | ok |
| `russia-cbr-bitcoin-information-letter-2014` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-16 | 8 | ok | no_audit_recorded |
| `russia-election-interference-ofac-2020` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-22 | 32 | ok | no_audit_recorded |
| `russia-mining-regional-ban-2024-12` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-16 | 8 | ok | no_audit_recorded |
| `russian-cyber-theft-ofac-2020` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-22 | 32 | ok | no_audit_recorded |
| `russian-cybercrime-infra-ofac-2025` | `admitted` | `human_authored` | 2026-05-15 | 9 | ok | 2026-04-22 | 32 | ok | ok |
| `samourai-doj-2024` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-22 | 32 | ok | no_audit_recorded |
| `sec-beaxy-platform-shutdown-2023` | `admitted` | `human_reviewed` | 2026-05-16 | 8 | ok | 2026-05-16 | 8 | ok | ok |
| `sec-burnside-bitcoin-stock-exchange-2014` | `admitted` | `human_reviewed` | 2026-05-16 | 8 | ok | 2026-05-16 | 8 | ok | ok |
| `sec-garza-gaw-miners-zenminer-2015` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-16 | 8 | ok | no_audit_recorded |
| `sec-shavers-btcst-2013` | `admitted` | `human_reviewed` | 2026-05-16 | 8 | ok | 2026-05-16 | 8 | ok | ok |
| `sec-v-binance-2023` | `admitted` | `human_authored` | 2026-05-06 | 18 | ok | 2026-05-06 | 18 | ok | ok |
| `sec-v-bittrex-2023` | `admitted` | `human_reviewed` | 2026-05-16 | 8 | ok | 2026-05-16 | 8 | ok | ok |
| `sec-v-coinbase-2023` | `admitted` | `human_authored` | 2026-05-06 | 18 | ok | 2026-05-06 | 18 | ok | ok |
| `sec-v-ripple-2020` | `admitted` | `human_reviewed` | 2026-05-16 | 8 | ok | 2026-05-16 | 8 | ok | ok |
| `sec-v-telegram-ton-2020` | `admitted` | `human_reviewed` | 2026-05-16 | 8 | ok | 2026-05-16 | 8 | ok | ok |
| `sec-v-uniswap-wells-notice-2024` | `rejected` | `human_authored` | — | — | no_audit_recorded | 2026-05-06 | 18 | ok | no_audit_recorded |
| `sec-voorhees-satoshidice-2014` | `admitted` | `human_reviewed` | 2026-05-16 | 8 | ok | 2026-05-16 | 8 | ok | ok |
| `semenov-ofac-2023` | `admitted` | `human_authored` | 2026-04-22 | 32 | ok | 2026-04-21 | 33 | ok | ok |
| `shrem-faiella-bitcoin-exchange-2014` | `admitted` | `human_reviewed` | 2026-05-16 | 8 | ok | 2026-05-16 | 8 | ok | ok |
| `sichuan-silence-ofac-2024` | `admitted` | `human_authored` | 2026-05-15 | 9 | ok | 2026-04-22 | 32 | ok | ok |
| `silk-road-doj-seizure-2013` | `admitted` | `human_reviewed` | 2026-05-16 | 8 | ok | 2026-05-16 | 8 | ok | ok |
| `sinbad-doj-2024` | `admitted` | `human_reviewed` | 2026-05-16 | 8 | ok | 2026-05-16 | 8 | ok | ok |
| `sinbad-ofac-2023` | `admitted` | `human_authored` | 2026-05-15 | 9 | ok | 2026-04-21 | 33 | ok | ok |
| `singapore-mas-binance-services-2021` | `admitted` | `human_reviewed` | 2026-05-16 | 8 | ok | 2026-05-16 | 8 | ok | ok |
| `storm-semenov-doj-2023` | `admitted` | `human_authored` | 2026-05-15 | 9 | ok | 2026-04-22 | 32 | ok | ok |
| `suex-ofac-2021` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-21 | 33 | ok | no_audit_recorded |
| `teraexchange-cftc-bitcoin-swap-2015` | `admitted` | `human_reviewed` | 2026-05-16 | 8 | ok | 2026-05-16 | 8 | ok | ok |
| `tether-doj-pig-butchering-freeze-2023` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-22 | 32 | ok | no_audit_recorded |
| `tether-dprk-precommit-freeze-2025` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-22 | 32 | ok | no_audit_recorded |
| `tether-retroactive-sweep-2023` | `admitted` | `human_authored` | 2026-04-22 | 32 | ok | 2026-04-22 | 32 | ok | ok |
| `tornado-cash-ofac-2022` | `admitted` | `human_authored` | 2026-04-22 | 32 | ok | 2026-04-21 | 33 | ok | ok |
| `tornado-cash-ofac-delisting-2025` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-21 | 33 | ok | no_audit_recorded |
| `tornado-cash-ofac-redesignation-2022` | `admitted` | `human_authored` | 2026-04-22 | 32 | ok | 2026-04-21 | 33 | ok | ok |
| `tornado-cash-storm-conviction-2025` | `admitted` | `human_reviewed` | 2026-05-16 | 8 | ok | 2026-05-16 | 8 | ok | ok |
| `turkey-cbrt-crypto-ban-2021` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-22 | 32 | ok | no_audit_recorded |
| `uk-fca-binance-markets-2021` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-05-16 | 8 | ok | no_audit_recorded |
| `ukraine-virtual-assets-law-2022-03` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-16 | 8 | ok | no_audit_recorded |
| `uniswap-balancer-tornado-frontend-block-2022-08` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-16 | 8 | ok | no_audit_recorded |
| `uniswap-frontend-delisting-2023` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-22 | 32 | ok | no_audit_recorded |
| `uniswap-tokenized-stocks-delisting-2021-07` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-16 | 8 | ok | no_audit_recorded |
| `welcome-to-video-doj-2019` | `admitted` | `human_reviewed` | 2026-05-16 | 8 | ok | 2026-05-16 | 8 | ok | ok |
| `wikileaks-amazon-aws-eviction-2010-12` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-16 | 8 | ok | no_audit_recorded |
| `wikileaks-bank-of-america-block-2010-12` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-16 | 8 | ok | no_audit_recorded |
| `wikileaks-everydns-domain-termination-2010-12` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-16 | 8 | ok | no_audit_recorded |
| `wikileaks-mastercard-suspension-2010-12` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-16 | 8 | ok | no_audit_recorded |
| `wikileaks-paypal-freeze-2010-12` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-16 | 8 | ok | no_audit_recorded |
| `wikileaks-postfinance-account-closure-2010-12` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-16 | 8 | ok | no_audit_recorded |
| `wikileaks-visa-europe-suspension-2010-12` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-16 | 8 | ok | no_audit_recorded |
| `wikileaks-western-union-interdiction-2010-12` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-16 | 8 | ok | no_audit_recorded |
| `zservers-ofac-2025` | `admitted` | `human_authored` | 2026-05-15 | 9 | ok | 2026-04-22 | 32 | ok | ok |

## Events flagged (any non-`ok` summary)

- `1inch-us-geofence-2021-09` — audit=no_audit_recorded, verification=ok, verif_age=8d
- `aave-arc-fireblocks-whitelist-2022-01` — audit=no_audit_recorded, verification=ok, verif_age=8d
- `aave-tornado-frontend-block-2022-08` — audit=no_audit_recorded, verification=ok, verif_age=8d
- `aeza-group-ofac-2025` — audit=no_audit_recorded, verification=ok, verif_age=32d
- `apple-india-crypto-exchange-removal-2024-01` — audit=no_audit_recorded, verification=ok, verif_age=8d
- `binance-4framework-2023` — audit=no_audit_recorded, verification=ok, verif_age=32d
- `bitzlato-doj-2023` — audit=no_audit_recorded, verification=ok, verif_age=33d
- `blender-ofac-2022` — audit=no_audit_recorded, verification=ok, verif_age=33d
- `btc-e-doj-2017` — audit=no_audit_recorded, verification=ok, verif_age=32d
- `canada-convoy-freeze-2022` — audit=no_audit_recorded, verification=ok, verif_age=32d
- `cftc-v-ooki-dao-2022` — audit=no_audit_recorded, verification=ok, verif_age=32d
- `chatex-ofac-2021` — audit=no_audit_recorded, verification=ok, verif_age=32d
- `china-inner-mongolia-mining-ban-2021-05` — audit=no_audit_recorded, verification=ok, verif_age=8d
- `china-nft-secondary-trading-self-discipline-2022-06` — audit=no_audit_recorded, verification=ok, verif_age=8d
- `china-pboc-crypto-ban-2021` — audit=no_audit_recorded, verification=ok, verif_age=33d
- `china-pboc-exchange-shutdown-2017-09` — audit=no_audit_recorded, verification=ok, verif_age=8d
- `china-sichuan-mining-ban-2021-06` — audit=no_audit_recorded, verification=ok, verif_age=8d
- `china-state-council-mining-crackdown-2021-05` — audit=no_audit_recorded, verification=ok, verif_age=8d
- `chipmixer-doj-2023` — audit=no_audit_recorded, verification=ok, verif_age=32d
- `circle-usdc-tornado-2022` — audit=no_audit_recorded, verification=ok, verif_age=32d
- `cloudflare-ethereum-gateway-tornado-block-2022-08` — audit=no_audit_recorded, verification=ok, verif_age=8d
- `coin-mx-doj-murgio-2015` — audit=no_audit_recorded, verification=ok, verif_age=8d
- `coinbase-india-exit-2022` — audit=no_audit_recorded, verification=ok, verif_age=32d
- `datacell-v-valitor-iceland-district-court-2012-07` — audit=no_audit_recorded, verification=ok, verif_age=8d
- `dprk-usdt-network-ofac-2025` — audit=no_audit_recorded, verification=ok, verif_age=32d
- `dydx-tornado-account-block-2022-08` — audit=no_audit_recorded, verification=ok, verif_age=8d
- `eba-virtual-currencies-opinion-eba-op-2014-08` — audit=no_audit_recorded, verification=ok, verif_age=8d
- `egold-doj-guilty-plea-2008-07` — audit=no_audit_recorded, verification=ok, verif_age=8d
- `eu-12th-russia-sanctions-2023` — audit=no_audit_recorded, verification=ok, verif_age=32d
- `eu-mica-2023` — audit=no_audit_recorded, verification=ok, verif_age=32d
- `fatf-virtual-currencies-key-definitions-2014` — audit=no_audit_recorded, verification=ok, verif_age=8d
- `fincen-virtual-currency-msb-guidance-2013` — audit=no_audit_recorded, verification=ok, verif_age=8d
- `funnull-cdn-ofac-2025` — audit=no_audit_recorded, verification=ok, verif_age=32d
- `garantex-ofac-2022` — audit=no_audit_recorded, verification=ok, verif_age=33d
- `google-play-india-crypto-exchange-removal-2024-01` — audit=no_audit_recorded, verification=ok, verif_age=8d
- `grinex-garantex-successor-ofac-2025` — audit=no_audit_recorded, verification=ok, verif_age=33d
- `hongkong-hkma-stablecoins-ordinance-2025` — audit=no_audit_recorded, verification=ok, verif_age=8d
- `hongkong-sfc-vatp-licensing-2023-06` — audit=no_audit_recorded, verification=ok, verif_age=8d
- `hydra-doj-2022` — audit=no_audit_recorded, verification=ok, verif_age=32d
- `hydra-ofac-2022` — audit=no_audit_recorded, verification=ok, verif_age=33d
- `iceland-cbi-foreign-exchange-bitcoin-2014` — audit=no_audit_recorded, verification=ok, verif_age=8d
- `india-rbi-crypto-ban-2018` — audit=no_audit_recorded, verification=ok, verif_age=32d
- `infura-metamask-donetsk-luhansk-block-2022-03` — audit=no_audit_recorded, verification=ok, verif_age=8d
- `japan-fsa-dmm-bitcoin-order-2024-09` — audit=no_audit_recorded, verification=ok, verif_age=8d
- `japan-fsa-ftx-japan-suspension-2022-11` — audit=no_audit_recorded, verification=ok, verif_age=8d
- `japan-fsa-six-exchange-orders-2018-06` — audit=no_audit_recorded, verification=ok, verif_age=8d
- `japan-fsa-stablecoin-psa-effective-2023-06` — audit=no_audit_recorded, verification=ok, verif_age=8d
- `japan-fsa-travel-rule-effective-2023-06` — audit=no_audit_recorded, verification=ok, verif_age=8d
- `japan-fsa-zaif-orders-2018-09` — audit=no_audit_recorded, verification=ok, verif_age=8d
- `karpeles-arrest-tokyo-mtgox-2015` — audit=no_audit_recorded, verification=ok, verif_age=8d
- `kazakhstan-digital-assets-law-2023-02` — audit=no_audit_recorded, verification=ok, verif_age=8d
- `kazakhstan-internet-shutdown-mining-2022-01` — audit=no_audit_recorded, verification=ok, verif_age=8d
- `korea-travel-rule-2022` — audit=no_audit_recorded, verification=ok, verif_age=32d
- `lockbit-affiliates-ofac-2024` — audit=no_audit_recorded, verification=ok, verif_age=32d
- `mtgox-bankruptcy-tokyo-2014` — audit=no_audit_recorded, verification=ok, verif_age=8d
- `mtgox-coinlab-civil-2013` — audit=no_audit_recorded, verification=ok, verif_age=8d
- `mtgox-dhs-dwolla-wells-fargo-seizure-2013` — audit=no_audit_recorded, verification=ok, verif_age=8d
- `mtgox-usd-withdrawal-suspension-2013-06` — audit=no_audit_recorded, verification=ok, verif_age=8d
- `nigeria-cbn-crypto-ban-2021` — audit=no_audit_recorded, verification=ok, verif_age=32d
- `nydfs-bitlicense-bitfinex-kraken-shapeshift-exit-2015` — audit=no_audit_recorded, verification=ok, verif_age=8d
- `ofac-hamas-buy-cash-msb-2023-10` — audit=no_audit_recorded, verification=ok, verif_age=8d
- `ofac-hamas-gaza-now-2024-03` — audit=no_audit_recorded, verification=ok, verif_age=8d
- `ofac-hamas-irgc-virtual-currency-network-2024-01` — audit=no_audit_recorded, verification=ok, verif_age=8d
- `ofac-recent-action-20240111` — audit=no_audit_recorded, verification=ok, verif_age=8d
- `ofac-trickbot-conti-eleven-2023-09` — audit=no_audit_recorded, verification=ok, verif_age=8d
- `ofac-zhdanova-russian-elite-launderer-2023-11` — audit=no_audit_recorded, verification=ok, verif_age=8d
- `opensea-iran-cuba-sanctions-block-2022` — audit=no_audit_recorded, verification=ok, verif_age=8d
- `paxos-busd-nydfs-minting-stop-2023` — audit=no_audit_recorded, verification=ok, verif_age=8d
- `philippines-sec-binance-block-2024` — audit=no_audit_recorded, verification=ok, verif_age=8d
- `polymarket-cftc-geofence-2022-01` — audit=no_audit_recorded, verification=ok, verif_age=8d
- `russia-cbr-bitcoin-information-letter-2014` — audit=no_audit_recorded, verification=ok, verif_age=8d
- `russia-election-interference-ofac-2020` — audit=no_audit_recorded, verification=ok, verif_age=32d
- `russia-mining-regional-ban-2024-12` — audit=no_audit_recorded, verification=ok, verif_age=8d
- `russian-cyber-theft-ofac-2020` — audit=no_audit_recorded, verification=ok, verif_age=32d
- `samourai-doj-2024` — audit=no_audit_recorded, verification=ok, verif_age=32d
- `sec-garza-gaw-miners-zenminer-2015` — audit=no_audit_recorded, verification=ok, verif_age=8d
- `sec-v-uniswap-wells-notice-2024` — audit=no_audit_recorded, verification=ok, verif_age=18d
- `suex-ofac-2021` — audit=no_audit_recorded, verification=ok, verif_age=33d
- `tether-doj-pig-butchering-freeze-2023` — audit=no_audit_recorded, verification=ok, verif_age=32d
- `tether-dprk-precommit-freeze-2025` — audit=no_audit_recorded, verification=ok, verif_age=32d
- `tornado-cash-ofac-delisting-2025` — audit=no_audit_recorded, verification=ok, verif_age=33d
- `turkey-cbrt-crypto-ban-2021` — audit=no_audit_recorded, verification=ok, verif_age=32d
- `uk-fca-binance-markets-2021` — audit=no_audit_recorded, verification=ok, verif_age=8d
- `ukraine-virtual-assets-law-2022-03` — audit=no_audit_recorded, verification=ok, verif_age=8d
- `uniswap-balancer-tornado-frontend-block-2022-08` — audit=no_audit_recorded, verification=ok, verif_age=8d
- `uniswap-frontend-delisting-2023` — audit=no_audit_recorded, verification=ok, verif_age=32d
- `uniswap-tokenized-stocks-delisting-2021-07` — audit=no_audit_recorded, verification=ok, verif_age=8d
- `wikileaks-amazon-aws-eviction-2010-12` — audit=no_audit_recorded, verification=ok, verif_age=8d
- `wikileaks-bank-of-america-block-2010-12` — audit=no_audit_recorded, verification=ok, verif_age=8d
- `wikileaks-everydns-domain-termination-2010-12` — audit=no_audit_recorded, verification=ok, verif_age=8d
- `wikileaks-mastercard-suspension-2010-12` — audit=no_audit_recorded, verification=ok, verif_age=8d
- `wikileaks-paypal-freeze-2010-12` — audit=no_audit_recorded, verification=ok, verif_age=8d
- `wikileaks-postfinance-account-closure-2010-12` — audit=no_audit_recorded, verification=ok, verif_age=8d
- `wikileaks-visa-europe-suspension-2010-12` — audit=no_audit_recorded, verification=ok, verif_age=8d
- `wikileaks-western-union-interdiction-2010-12` — audit=no_audit_recorded, verification=ok, verif_age=8d
