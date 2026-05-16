# Staleness report

Generated at: `2026-05-19T00:00:00Z`
Red threshold: audits / verifications older than `90` days.
Most recent agent activity in `candidate_triggers/`: `none recorded`.

## Coverage snapshot

Two dimensions tracked per event; missing values surface as explicit gaps, never masked.

- **Adversarial audit** (`last_human_audit`): {'no_audit_recorded': 51, 'ok': 71}
- **Verification** (`last_verified`): {'ok': 122}
- **Row-level summary** (worst of the two): {'no_audit_recorded': 51, 'ok': 71}

## Flag legend

- `ok` — within the red threshold
- `red` — older than 90 days
- `no_audit_recorded` — no last_human_audit on record — event has never been through an adversarial audit
- `no_verification_recorded` — no last_verified on record — event has never been re-verified
- `error` — event YAML failed to parse

## Per-event table

| Event | Status | Origin | last_human_audit | Audit age | Audit flag | last_verified | Verification age | Verif flag | Summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `aeza-group-ofac-2025` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-22 | 27 | ok | no_audit_recorded |
| `alphabay-hansa-doj-2017` | `admitted` | `human_reviewed` | 2026-05-16 | 3 | ok | 2026-05-16 | 3 | ok | ok |
| `australia-asic-binance-derivatives-2023` | `admitted` | `human_reviewed` | 2026-05-16 | 3 | ok | 2026-05-16 | 3 | ok | ok |
| `belgium-fsma-binance-cease-2023` | `admitted` | `human_reviewed` | 2026-05-16 | 3 | ok | 2026-05-16 | 3 | ok | ok |
| `binance-4framework-2023` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-22 | 27 | ok | no_audit_recorded |
| `binance-cftc-2023` | `admitted` | `human_reviewed` | 2026-05-16 | 3 | ok | 2026-05-16 | 3 | ok | ok |
| `binance-privacy-coin-delisting-2023` | `admitted` | `human_reviewed` | 2026-05-16 | 3 | ok | 2026-05-16 | 3 | ok | ok |
| `binance-russia-exit-commex-2023` | `admitted` | `human_reviewed` | 2026-05-16 | 3 | ok | 2026-05-16 | 3 | ok | ok |
| `binance-us-staking-end-2023` | `admitted` | `human_reviewed` | 2026-05-16 | 3 | ok | 2026-05-16 | 3 | ok | ok |
| `bitfinex-cftc-retail-commodity-2016` | `admitted` | `human_reviewed` | 2026-05-16 | 3 | ok | 2026-05-16 | 3 | ok | ok |
| `bitfinex-tether-cftc-2021` | `admitted` | `human_reviewed` | 2026-05-16 | 3 | ok | 2026-05-16 | 3 | ok | ok |
| `bitmex-cftc-doj-2020` | `admitted` | `human_reviewed` | 2026-05-16 | 3 | ok | 2026-05-16 | 3 | ok | ok |
| `bitzlato-doj-2023` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-21 | 28 | ok | no_audit_recorded |
| `blender-ofac-2022` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-21 | 28 | ok | no_audit_recorded |
| `blockfi-sec-lending-2022` | `admitted` | `human_reviewed` | 2026-05-16 | 3 | ok | 2026-05-16 | 3 | ok | ok |
| `btc-e-doj-2017` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-22 | 27 | ok | no_audit_recorded |
| `canada-convoy-freeze-2022` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-22 | 27 | ok | no_audit_recorded |
| `canada-csa-binance-withdrawal-2023` | `admitted` | `human_reviewed` | 2026-05-16 | 3 | ok | 2026-05-16 | 3 | ok | ok |
| `celsius-bankruptcy-mashinsky-doj-2023` | `admitted` | `human_reviewed` | 2026-05-16 | 3 | ok | 2026-05-16 | 3 | ok | ok |
| `cftc-v-ooki-dao-2022` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-22 | 27 | ok | no_audit_recorded |
| `chatex-ofac-2021` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-22 | 27 | ok | no_audit_recorded |
| `china-pboc-crypto-ban-2013-12` | `admitted` | `human_reviewed` | 2026-05-16 | 3 | ok | 2026-05-16 | 3 | ok | ok |
| `china-pboc-crypto-ban-2021` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-21 | 28 | ok | no_audit_recorded |
| `chipmixer-doj-2023` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-22 | 27 | ok | no_audit_recorded |
| `circle-usdc-tornado-2022` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-22 | 27 | ok | no_audit_recorded |
| `coin-mx-doj-murgio-2015` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-16 | 3 | ok | no_audit_recorded |
| `coinbase-india-exit-2022` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-22 | 27 | ok | no_audit_recorded |
| `coinbase-irs-john-doe-summons-2016` | `admitted` | `human_reviewed` | 2026-05-16 | 3 | ok | 2026-05-16 | 3 | ok | ok |
| `coinflip-cftc-derivabit-2015` | `admitted` | `human_reviewed` | 2026-05-16 | 3 | ok | 2026-05-16 | 3 | ok | ok |
| `cryptex-ofac-2024` | `admitted` | `human_authored` | 2026-04-22 | 27 | ok | 2026-04-21 | 28 | ok | ok |
| `dprk-usdt-network-ofac-2025` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-22 | 27 | ok | no_audit_recorded |
| `eba-virtual-currencies-opinion-eba-op-2014-08` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-16 | 3 | ok | no_audit_recorded |
| `eu-12th-russia-sanctions-2023` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-22 | 27 | ok | no_audit_recorded |
| `eu-mica-2023` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-22 | 27 | ok | no_audit_recorded |
| `eu-russia-crypto-wallet-cap-2022` | `admitted` | `human_reviewed` | 2026-05-16 | 3 | ok | 2026-05-16 | 3 | ok | ok |
| `eu-russia-full-crypto-wallet-ban-2022` | `admitted` | `human_reviewed` | 2026-05-16 | 3 | ok | 2026-05-16 | 3 | ok | ok |
| `eu-tfr-recast-2023` | `admitted` | `human_reviewed` | 2026-05-16 | 3 | ok | 2026-05-16 | 3 | ok | ok |
| `fatf-r15-vasp-travel-rule-2019` | `admitted` | `human_reviewed` | 2026-05-16 | 3 | ok | 2026-05-16 | 3 | ok | ok |
| `fatf-virtual-currencies-key-definitions-2014` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-16 | 3 | ok | no_audit_recorded |
| `fincen-virtual-currency-msb-guidance-2013` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-16 | 3 | ok | no_audit_recorded |
| `ftx-bankman-fried-doj-2022` | `admitted` | `human_reviewed` | 2026-05-16 | 3 | ok | 2026-05-16 | 3 | ok | ok |
| `funnull-cdn-ofac-2025` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-22 | 27 | ok | no_audit_recorded |
| `garantex-ofac-2022` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-21 | 28 | ok | no_audit_recorded |
| `genesis-sec-gemini-earn-2023` | `admitted` | `human_reviewed` | 2026-05-16 | 3 | ok | 2026-05-16 | 3 | ok | ok |
| `germany-bafin-binance-licence-withdrawal-2023` | `admitted` | `human_reviewed` | 2026-05-16 | 3 | ok | 2026-05-16 | 3 | ok | ok |
| `grinex-garantex-successor-ofac-2025` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-21 | 28 | ok | no_audit_recorded |
| `helix-doj-mixer-2020` | `admitted` | `human_reviewed` | 2026-05-16 | 3 | ok | 2026-05-16 | 3 | ok | ok |
| `hydra-doj-2022` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-22 | 27 | ok | no_audit_recorded |
| `hydra-ofac-2022` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-21 | 28 | ok | no_audit_recorded |
| `iceland-cbi-foreign-exchange-bitcoin-2014` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-16 | 3 | ok | no_audit_recorded |
| `india-fiu-offshore-vda-block-2023` | `admitted` | `human_reviewed` | 2026-05-16 | 3 | ok | 2026-05-16 | 3 | ok | ok |
| `india-rbi-crypto-ban-2018` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-22 | 27 | ok | no_audit_recorded |
| `infura-alchemy-tornado-rpc-block-2022` | `admitted` | `human_reviewed` | 2026-05-16 | 3 | ok | 2026-05-16 | 3 | ok | ok |
| `iran-ransomware-ofac-2018` | `admitted` | `human_authored` | 2026-05-15 | 4 | ok | 2026-04-22 | 27 | ok | ok |
| `irgc-ransomware-ofac-2022` | `admitted` | `human_authored` | 2026-05-15 | 4 | ok | 2026-04-22 | 27 | ok | ok |
| `japan-fsa-coincheck-orders-2018` | `admitted` | `human_reviewed` | 2026-05-16 | 3 | ok | 2026-05-16 | 3 | ok | ok |
| `karpeles-arrest-tokyo-mtgox-2015` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-16 | 3 | ok | no_audit_recorded |
| `korea-fsc-ico-ban-2017` | `admitted` | `human_reviewed` | 2026-05-16 | 3 | ok | 2026-05-16 | 3 | ok | ok |
| `korea-travel-rule-2022` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-22 | 27 | ok | no_audit_recorded |
| `kraken-sec-staking-2023` | `admitted` | `human_reviewed` | 2026-05-16 | 3 | ok | 2026-05-16 | 3 | ok | ok |
| `kraken-sec-unregistered-exchange-2023` | `admitted` | `human_reviewed` | 2026-05-16 | 3 | ok | 2026-05-16 | 3 | ok | ok |
| `kucoin-doj-2024` | `admitted` | `human_reviewed` | 2026-05-16 | 3 | ok | 2026-05-16 | 3 | ok | ok |
| `lazarus-entity-ofac-2019` | `admitted` | `human_authored` | 2026-05-15 | 4 | ok | 2026-04-22 | 27 | ok | ok |
| `lazarus-laundering-ofac-2020` | `admitted` | `human_authored` | 2026-05-15 | 4 | ok | 2026-04-22 | 27 | ok | ok |
| `lockbit-affiliates-ofac-2024` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-22 | 27 | ok | no_audit_recorded |
| `lockbit-leader-ofac-2024` | `admitted` | `human_authored` | 2026-05-15 | 4 | ok | 2026-04-22 | 27 | ok | ok |
| `malaysia-sc-binance-disable-2021` | `admitted` | `human_reviewed` | 2026-05-16 | 3 | ok | 2026-05-16 | 3 | ok | ok |
| `matveev-ofac-2023` | `admitted` | `human_authored` | 2026-05-15 | 4 | ok | 2026-04-22 | 27 | ok | ok |
| `mtgox-bankruptcy-tokyo-2014` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-16 | 3 | ok | no_audit_recorded |
| `mtgox-coinlab-civil-2013` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-16 | 3 | ok | no_audit_recorded |
| `mtgox-dhs-dwolla-wells-fargo-seizure-2013` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-16 | 3 | ok | no_audit_recorded |
| `mtgox-usd-withdrawal-suspension-2013-06` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-16 | 3 | ok | no_audit_recorded |
| `netherlands-dnb-binance-warning-2021` | `admitted` | `human_reviewed` | 2026-05-16 | 3 | ok | 2026-05-16 | 3 | ok | ok |
| `nigeria-cbn-crypto-ban-2021` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-22 | 27 | ok | no_audit_recorded |
| `nydfs-bitlicense-2015-06` | `admitted` | `human_reviewed` | 2026-05-16 | 3 | ok | 2026-05-16 | 3 | ok | ok |
| `nydfs-bitlicense-bitfinex-kraken-shapeshift-exit-2015` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-16 | 3 | ok | no_audit_recorded |
| `oecd-carf-2022` | `admitted` | `human_reviewed` | 2026-05-16 | 3 | ok | 2026-05-16 | 3 | ok | ok |
| `ofac-recent-action-20240111` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-16 | 3 | ok | no_audit_recorded |
| `okx-privacy-token-delist-2024` | `admitted` | `human_reviewed` | 2026-05-16 | 3 | ok | 2026-05-16 | 3 | ok | ok |
| `paxos-busd-nydfs-minting-stop-2023` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-16 | 3 | ok | no_audit_recorded |
| `pertsev-nl-arrest-2022` | `admitted` | `human_authored` | 2026-05-15 | 4 | ok | 2026-04-22 | 27 | ok | ok |
| `philippines-sec-binance-block-2024` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-16 | 3 | ok | no_audit_recorded |
| `powell-unlicensed-bitcoin-exchange-2014` | `admitted` | `human_reviewed` | 2026-05-16 | 3 | ok | 2026-05-16 | 3 | ok | ok |
| `ripple-fincen-xrp-2015` | `admitted` | `human_reviewed` | 2026-05-16 | 3 | ok | 2026-05-16 | 3 | ok | ok |
| `russia-cbr-bitcoin-information-letter-2014` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-16 | 3 | ok | no_audit_recorded |
| `russia-election-interference-ofac-2020` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-22 | 27 | ok | no_audit_recorded |
| `russian-cyber-theft-ofac-2020` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-22 | 27 | ok | no_audit_recorded |
| `russian-cybercrime-infra-ofac-2025` | `admitted` | `human_authored` | 2026-05-15 | 4 | ok | 2026-04-22 | 27 | ok | ok |
| `samourai-doj-2024` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-22 | 27 | ok | no_audit_recorded |
| `sec-beaxy-platform-shutdown-2023` | `admitted` | `human_reviewed` | 2026-05-16 | 3 | ok | 2026-05-16 | 3 | ok | ok |
| `sec-burnside-bitcoin-stock-exchange-2014` | `admitted` | `human_reviewed` | 2026-05-16 | 3 | ok | 2026-05-16 | 3 | ok | ok |
| `sec-garza-gaw-miners-zenminer-2015` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-16 | 3 | ok | no_audit_recorded |
| `sec-shavers-btcst-2013` | `admitted` | `human_reviewed` | 2026-05-16 | 3 | ok | 2026-05-16 | 3 | ok | ok |
| `sec-v-binance-2023` | `admitted` | `human_authored` | 2026-05-06 | 13 | ok | 2026-05-06 | 13 | ok | ok |
| `sec-v-bittrex-2023` | `admitted` | `human_reviewed` | 2026-05-16 | 3 | ok | 2026-05-16 | 3 | ok | ok |
| `sec-v-coinbase-2023` | `admitted` | `human_authored` | 2026-05-06 | 13 | ok | 2026-05-06 | 13 | ok | ok |
| `sec-v-ripple-2020` | `admitted` | `human_reviewed` | 2026-05-16 | 3 | ok | 2026-05-16 | 3 | ok | ok |
| `sec-v-telegram-ton-2020` | `admitted` | `human_reviewed` | 2026-05-16 | 3 | ok | 2026-05-16 | 3 | ok | ok |
| `sec-v-uniswap-wells-notice-2024` | `rejected` | `human_authored` | — | — | no_audit_recorded | 2026-05-06 | 13 | ok | no_audit_recorded |
| `sec-voorhees-satoshidice-2014` | `admitted` | `human_reviewed` | 2026-05-16 | 3 | ok | 2026-05-16 | 3 | ok | ok |
| `semenov-ofac-2023` | `admitted` | `human_authored` | 2026-04-22 | 27 | ok | 2026-04-21 | 28 | ok | ok |
| `shrem-faiella-bitcoin-exchange-2014` | `admitted` | `human_reviewed` | 2026-05-16 | 3 | ok | 2026-05-16 | 3 | ok | ok |
| `sichuan-silence-ofac-2024` | `admitted` | `human_authored` | 2026-05-15 | 4 | ok | 2026-04-22 | 27 | ok | ok |
| `silk-road-doj-seizure-2013` | `admitted` | `human_reviewed` | 2026-05-16 | 3 | ok | 2026-05-16 | 3 | ok | ok |
| `sinbad-doj-2024` | `admitted` | `human_reviewed` | 2026-05-16 | 3 | ok | 2026-05-16 | 3 | ok | ok |
| `sinbad-ofac-2023` | `admitted` | `human_authored` | 2026-05-15 | 4 | ok | 2026-04-21 | 28 | ok | ok |
| `singapore-mas-binance-services-2021` | `admitted` | `human_reviewed` | 2026-05-16 | 3 | ok | 2026-05-16 | 3 | ok | ok |
| `storm-semenov-doj-2023` | `admitted` | `human_authored` | 2026-05-15 | 4 | ok | 2026-04-22 | 27 | ok | ok |
| `suex-ofac-2021` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-21 | 28 | ok | no_audit_recorded |
| `teraexchange-cftc-bitcoin-swap-2015` | `admitted` | `human_reviewed` | 2026-05-16 | 3 | ok | 2026-05-16 | 3 | ok | ok |
| `tether-doj-pig-butchering-freeze-2023` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-22 | 27 | ok | no_audit_recorded |
| `tether-dprk-precommit-freeze-2025` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-22 | 27 | ok | no_audit_recorded |
| `tether-retroactive-sweep-2023` | `admitted` | `human_authored` | 2026-04-22 | 27 | ok | 2026-04-22 | 27 | ok | ok |
| `tornado-cash-ofac-2022` | `admitted` | `human_authored` | 2026-04-22 | 27 | ok | 2026-04-21 | 28 | ok | ok |
| `tornado-cash-ofac-delisting-2025` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-21 | 28 | ok | no_audit_recorded |
| `tornado-cash-ofac-redesignation-2022` | `admitted` | `human_authored` | 2026-04-22 | 27 | ok | 2026-04-21 | 28 | ok | ok |
| `tornado-cash-storm-conviction-2025` | `admitted` | `human_reviewed` | 2026-05-16 | 3 | ok | 2026-05-16 | 3 | ok | ok |
| `turkey-cbrt-crypto-ban-2021` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-22 | 27 | ok | no_audit_recorded |
| `uk-fca-binance-markets-2021` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-05-16 | 3 | ok | no_audit_recorded |
| `uniswap-frontend-delisting-2023` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-22 | 27 | ok | no_audit_recorded |
| `welcome-to-video-doj-2019` | `admitted` | `human_reviewed` | 2026-05-16 | 3 | ok | 2026-05-16 | 3 | ok | ok |
| `zservers-ofac-2025` | `admitted` | `human_authored` | 2026-05-15 | 4 | ok | 2026-04-22 | 27 | ok | ok |

## Events flagged (any non-`ok` summary)

- `aeza-group-ofac-2025` — audit=no_audit_recorded, verification=ok, verif_age=27d
- `binance-4framework-2023` — audit=no_audit_recorded, verification=ok, verif_age=27d
- `bitzlato-doj-2023` — audit=no_audit_recorded, verification=ok, verif_age=28d
- `blender-ofac-2022` — audit=no_audit_recorded, verification=ok, verif_age=28d
- `btc-e-doj-2017` — audit=no_audit_recorded, verification=ok, verif_age=27d
- `canada-convoy-freeze-2022` — audit=no_audit_recorded, verification=ok, verif_age=27d
- `cftc-v-ooki-dao-2022` — audit=no_audit_recorded, verification=ok, verif_age=27d
- `chatex-ofac-2021` — audit=no_audit_recorded, verification=ok, verif_age=27d
- `china-pboc-crypto-ban-2021` — audit=no_audit_recorded, verification=ok, verif_age=28d
- `chipmixer-doj-2023` — audit=no_audit_recorded, verification=ok, verif_age=27d
- `circle-usdc-tornado-2022` — audit=no_audit_recorded, verification=ok, verif_age=27d
- `coin-mx-doj-murgio-2015` — audit=no_audit_recorded, verification=ok, verif_age=3d
- `coinbase-india-exit-2022` — audit=no_audit_recorded, verification=ok, verif_age=27d
- `dprk-usdt-network-ofac-2025` — audit=no_audit_recorded, verification=ok, verif_age=27d
- `eba-virtual-currencies-opinion-eba-op-2014-08` — audit=no_audit_recorded, verification=ok, verif_age=3d
- `eu-12th-russia-sanctions-2023` — audit=no_audit_recorded, verification=ok, verif_age=27d
- `eu-mica-2023` — audit=no_audit_recorded, verification=ok, verif_age=27d
- `fatf-virtual-currencies-key-definitions-2014` — audit=no_audit_recorded, verification=ok, verif_age=3d
- `fincen-virtual-currency-msb-guidance-2013` — audit=no_audit_recorded, verification=ok, verif_age=3d
- `funnull-cdn-ofac-2025` — audit=no_audit_recorded, verification=ok, verif_age=27d
- `garantex-ofac-2022` — audit=no_audit_recorded, verification=ok, verif_age=28d
- `grinex-garantex-successor-ofac-2025` — audit=no_audit_recorded, verification=ok, verif_age=28d
- `hydra-doj-2022` — audit=no_audit_recorded, verification=ok, verif_age=27d
- `hydra-ofac-2022` — audit=no_audit_recorded, verification=ok, verif_age=28d
- `iceland-cbi-foreign-exchange-bitcoin-2014` — audit=no_audit_recorded, verification=ok, verif_age=3d
- `india-rbi-crypto-ban-2018` — audit=no_audit_recorded, verification=ok, verif_age=27d
- `karpeles-arrest-tokyo-mtgox-2015` — audit=no_audit_recorded, verification=ok, verif_age=3d
- `korea-travel-rule-2022` — audit=no_audit_recorded, verification=ok, verif_age=27d
- `lockbit-affiliates-ofac-2024` — audit=no_audit_recorded, verification=ok, verif_age=27d
- `mtgox-bankruptcy-tokyo-2014` — audit=no_audit_recorded, verification=ok, verif_age=3d
- `mtgox-coinlab-civil-2013` — audit=no_audit_recorded, verification=ok, verif_age=3d
- `mtgox-dhs-dwolla-wells-fargo-seizure-2013` — audit=no_audit_recorded, verification=ok, verif_age=3d
- `mtgox-usd-withdrawal-suspension-2013-06` — audit=no_audit_recorded, verification=ok, verif_age=3d
- `nigeria-cbn-crypto-ban-2021` — audit=no_audit_recorded, verification=ok, verif_age=27d
- `nydfs-bitlicense-bitfinex-kraken-shapeshift-exit-2015` — audit=no_audit_recorded, verification=ok, verif_age=3d
- `ofac-recent-action-20240111` — audit=no_audit_recorded, verification=ok, verif_age=3d
- `paxos-busd-nydfs-minting-stop-2023` — audit=no_audit_recorded, verification=ok, verif_age=3d
- `philippines-sec-binance-block-2024` — audit=no_audit_recorded, verification=ok, verif_age=3d
- `russia-cbr-bitcoin-information-letter-2014` — audit=no_audit_recorded, verification=ok, verif_age=3d
- `russia-election-interference-ofac-2020` — audit=no_audit_recorded, verification=ok, verif_age=27d
- `russian-cyber-theft-ofac-2020` — audit=no_audit_recorded, verification=ok, verif_age=27d
- `samourai-doj-2024` — audit=no_audit_recorded, verification=ok, verif_age=27d
- `sec-garza-gaw-miners-zenminer-2015` — audit=no_audit_recorded, verification=ok, verif_age=3d
- `sec-v-uniswap-wells-notice-2024` — audit=no_audit_recorded, verification=ok, verif_age=13d
- `suex-ofac-2021` — audit=no_audit_recorded, verification=ok, verif_age=28d
- `tether-doj-pig-butchering-freeze-2023` — audit=no_audit_recorded, verification=ok, verif_age=27d
- `tether-dprk-precommit-freeze-2025` — audit=no_audit_recorded, verification=ok, verif_age=27d
- `tornado-cash-ofac-delisting-2025` — audit=no_audit_recorded, verification=ok, verif_age=28d
- `turkey-cbrt-crypto-ban-2021` — audit=no_audit_recorded, verification=ok, verif_age=27d
- `uk-fca-binance-markets-2021` — audit=no_audit_recorded, verification=ok, verif_age=3d
- `uniswap-frontend-delisting-2023` — audit=no_audit_recorded, verification=ok, verif_age=27d
