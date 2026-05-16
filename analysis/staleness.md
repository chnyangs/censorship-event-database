# Staleness report

Generated at: `2026-05-18T10:40:00Z`
Red threshold: audits / verifications older than `90` days.
Most recent agent activity in `candidate_triggers/`: `none recorded`.

## Coverage snapshot

Two dimensions tracked per event; missing values surface as explicit gaps, never masked.

- **Adversarial audit** (`last_human_audit`): {'no_audit_recorded': 38, 'ok': 49}
- **Verification** (`last_verified`): {'ok': 87}
- **Row-level summary** (worst of the two): {'no_audit_recorded': 38, 'ok': 49}

## Flag legend

- `ok` — within the red threshold
- `red` — older than 90 days
- `no_audit_recorded` — no last_human_audit on record — event has never been through an adversarial audit
- `no_verification_recorded` — no last_verified on record — event has never been re-verified
- `error` — event YAML failed to parse

## Per-event table

| Event | Status | Origin | last_human_audit | Audit age | Audit flag | last_verified | Verification age | Verif flag | Summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `aeza-group-ofac-2025` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-22 | 26 | ok | no_audit_recorded |
| `alphabay-hansa-doj-2017` | `admitted` | `human_reviewed` | 2026-05-16 | 2 | ok | 2026-05-16 | 2 | ok | ok |
| `belgium-fsma-binance-cease-2023` | `admitted` | `human_reviewed` | 2026-05-16 | 2 | ok | 2026-05-16 | 2 | ok | ok |
| `binance-4framework-2023` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-22 | 26 | ok | no_audit_recorded |
| `binance-russia-exit-commex-2023` | `admitted` | `human_reviewed` | 2026-05-16 | 2 | ok | 2026-05-16 | 2 | ok | ok |
| `bitfinex-cftc-retail-commodity-2016` | `admitted` | `human_reviewed` | 2026-05-16 | 2 | ok | 2026-05-16 | 2 | ok | ok |
| `bitmex-cftc-doj-2020` | `admitted` | `human_reviewed` | 2026-05-16 | 2 | ok | 2026-05-16 | 2 | ok | ok |
| `bitzlato-doj-2023` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-21 | 27 | ok | no_audit_recorded |
| `blender-ofac-2022` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-21 | 27 | ok | no_audit_recorded |
| `blockfi-sec-lending-2022` | `admitted` | `human_reviewed` | 2026-05-16 | 2 | ok | 2026-05-16 | 2 | ok | ok |
| `btc-e-doj-2017` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-22 | 26 | ok | no_audit_recorded |
| `canada-convoy-freeze-2022` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-22 | 26 | ok | no_audit_recorded |
| `canada-csa-binance-withdrawal-2023` | `admitted` | `human_reviewed` | 2026-05-16 | 2 | ok | 2026-05-16 | 2 | ok | ok |
| `cftc-v-ooki-dao-2022` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-22 | 26 | ok | no_audit_recorded |
| `chatex-ofac-2021` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-22 | 26 | ok | no_audit_recorded |
| `china-pboc-crypto-ban-2013-12` | `admitted` | `human_reviewed` | 2026-05-16 | 2 | ok | 2026-05-16 | 2 | ok | ok |
| `china-pboc-crypto-ban-2021` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-21 | 27 | ok | no_audit_recorded |
| `chipmixer-doj-2023` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-22 | 26 | ok | no_audit_recorded |
| `circle-usdc-tornado-2022` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-22 | 26 | ok | no_audit_recorded |
| `coinbase-india-exit-2022` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-22 | 26 | ok | no_audit_recorded |
| `coinbase-irs-john-doe-summons-2016` | `admitted` | `human_reviewed` | 2026-05-16 | 2 | ok | 2026-05-16 | 2 | ok | ok |
| `coinflip-cftc-derivabit-2015` | `admitted` | `human_reviewed` | 2026-05-16 | 2 | ok | 2026-05-16 | 2 | ok | ok |
| `cryptex-ofac-2024` | `admitted` | `human_authored` | 2026-04-22 | 26 | ok | 2026-04-21 | 27 | ok | ok |
| `dprk-usdt-network-ofac-2025` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-22 | 26 | ok | no_audit_recorded |
| `eu-12th-russia-sanctions-2023` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-22 | 26 | ok | no_audit_recorded |
| `eu-mica-2023` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-22 | 26 | ok | no_audit_recorded |
| `eu-russia-crypto-wallet-cap-2022` | `admitted` | `human_reviewed` | 2026-05-16 | 2 | ok | 2026-05-16 | 2 | ok | ok |
| `eu-russia-full-crypto-wallet-ban-2022` | `admitted` | `human_reviewed` | 2026-05-16 | 2 | ok | 2026-05-16 | 2 | ok | ok |
| `funnull-cdn-ofac-2025` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-22 | 26 | ok | no_audit_recorded |
| `garantex-ofac-2022` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-21 | 27 | ok | no_audit_recorded |
| `grinex-garantex-successor-ofac-2025` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-21 | 27 | ok | no_audit_recorded |
| `helix-doj-mixer-2020` | `admitted` | `human_reviewed` | 2026-05-16 | 2 | ok | 2026-05-16 | 2 | ok | ok |
| `hydra-doj-2022` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-22 | 26 | ok | no_audit_recorded |
| `hydra-ofac-2022` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-21 | 27 | ok | no_audit_recorded |
| `india-fiu-offshore-vda-block-2023` | `admitted` | `human_reviewed` | 2026-05-16 | 2 | ok | 2026-05-16 | 2 | ok | ok |
| `india-rbi-crypto-ban-2018` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-22 | 26 | ok | no_audit_recorded |
| `iran-ransomware-ofac-2018` | `admitted` | `human_authored` | 2026-05-15 | 3 | ok | 2026-04-22 | 26 | ok | ok |
| `irgc-ransomware-ofac-2022` | `admitted` | `human_authored` | 2026-05-15 | 3 | ok | 2026-04-22 | 26 | ok | ok |
| `korea-travel-rule-2022` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-22 | 26 | ok | no_audit_recorded |
| `kraken-sec-staking-2023` | `admitted` | `human_reviewed` | 2026-05-16 | 2 | ok | 2026-05-16 | 2 | ok | ok |
| `kucoin-doj-2024` | `admitted` | `human_reviewed` | 2026-05-16 | 2 | ok | 2026-05-16 | 2 | ok | ok |
| `lazarus-entity-ofac-2019` | `admitted` | `human_authored` | 2026-05-15 | 3 | ok | 2026-04-22 | 26 | ok | ok |
| `lazarus-laundering-ofac-2020` | `admitted` | `human_authored` | 2026-05-15 | 3 | ok | 2026-04-22 | 26 | ok | ok |
| `lockbit-affiliates-ofac-2024` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-22 | 26 | ok | no_audit_recorded |
| `lockbit-leader-ofac-2024` | `admitted` | `human_authored` | 2026-05-15 | 3 | ok | 2026-04-22 | 26 | ok | ok |
| `malaysia-sc-binance-disable-2021` | `admitted` | `human_reviewed` | 2026-05-16 | 2 | ok | 2026-05-16 | 2 | ok | ok |
| `matveev-ofac-2023` | `admitted` | `human_authored` | 2026-05-15 | 3 | ok | 2026-04-22 | 26 | ok | ok |
| `netherlands-dnb-binance-warning-2021` | `admitted` | `human_reviewed` | 2026-05-16 | 2 | ok | 2026-05-16 | 2 | ok | ok |
| `nigeria-cbn-crypto-ban-2021` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-22 | 26 | ok | no_audit_recorded |
| `nydfs-bitlicense-2015-06` | `admitted` | `human_reviewed` | 2026-05-16 | 2 | ok | 2026-05-16 | 2 | ok | ok |
| `ofac-recent-action-20240111` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-16 | 2 | ok | no_audit_recorded |
| `okx-privacy-token-delist-2024` | `admitted` | `human_reviewed` | 2026-05-16 | 2 | ok | 2026-05-16 | 2 | ok | ok |
| `paxos-busd-nydfs-minting-stop-2023` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-16 | 2 | ok | no_audit_recorded |
| `pertsev-nl-arrest-2022` | `admitted` | `human_authored` | 2026-05-15 | 3 | ok | 2026-04-22 | 26 | ok | ok |
| `philippines-sec-binance-block-2024` | `draft` | `agent_draft` | — | — | no_audit_recorded | 2026-05-16 | 2 | ok | no_audit_recorded |
| `powell-unlicensed-bitcoin-exchange-2014` | `admitted` | `human_reviewed` | 2026-05-16 | 2 | ok | 2026-05-16 | 2 | ok | ok |
| `ripple-fincen-xrp-2015` | `admitted` | `human_reviewed` | 2026-05-16 | 2 | ok | 2026-05-16 | 2 | ok | ok |
| `russia-election-interference-ofac-2020` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-22 | 26 | ok | no_audit_recorded |
| `russian-cyber-theft-ofac-2020` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-22 | 26 | ok | no_audit_recorded |
| `russian-cybercrime-infra-ofac-2025` | `admitted` | `human_authored` | 2026-05-15 | 3 | ok | 2026-04-22 | 26 | ok | ok |
| `samourai-doj-2024` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-22 | 26 | ok | no_audit_recorded |
| `sec-beaxy-platform-shutdown-2023` | `admitted` | `human_reviewed` | 2026-05-16 | 2 | ok | 2026-05-16 | 2 | ok | ok |
| `sec-burnside-bitcoin-stock-exchange-2014` | `admitted` | `human_reviewed` | 2026-05-16 | 2 | ok | 2026-05-16 | 2 | ok | ok |
| `sec-shavers-btcst-2013` | `admitted` | `human_reviewed` | 2026-05-16 | 2 | ok | 2026-05-16 | 2 | ok | ok |
| `sec-v-binance-2023` | `admitted` | `human_authored` | 2026-05-06 | 12 | ok | 2026-05-06 | 12 | ok | ok |
| `sec-v-coinbase-2023` | `admitted` | `human_authored` | 2026-05-06 | 12 | ok | 2026-05-06 | 12 | ok | ok |
| `sec-v-uniswap-wells-notice-2024` | `rejected` | `human_authored` | — | — | no_audit_recorded | 2026-05-06 | 12 | ok | no_audit_recorded |
| `sec-voorhees-satoshidice-2014` | `admitted` | `human_reviewed` | 2026-05-16 | 2 | ok | 2026-05-16 | 2 | ok | ok |
| `semenov-ofac-2023` | `admitted` | `human_authored` | 2026-04-22 | 26 | ok | 2026-04-21 | 27 | ok | ok |
| `shrem-faiella-bitcoin-exchange-2014` | `admitted` | `human_reviewed` | 2026-05-16 | 2 | ok | 2026-05-16 | 2 | ok | ok |
| `sichuan-silence-ofac-2024` | `admitted` | `human_authored` | 2026-05-15 | 3 | ok | 2026-04-22 | 26 | ok | ok |
| `silk-road-doj-seizure-2013` | `admitted` | `human_reviewed` | 2026-05-16 | 2 | ok | 2026-05-16 | 2 | ok | ok |
| `sinbad-ofac-2023` | `admitted` | `human_authored` | 2026-05-15 | 3 | ok | 2026-04-21 | 27 | ok | ok |
| `singapore-mas-binance-services-2021` | `admitted` | `human_reviewed` | 2026-05-16 | 2 | ok | 2026-05-16 | 2 | ok | ok |
| `storm-semenov-doj-2023` | `admitted` | `human_authored` | 2026-05-15 | 3 | ok | 2026-04-22 | 26 | ok | ok |
| `suex-ofac-2021` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-21 | 27 | ok | no_audit_recorded |
| `teraexchange-cftc-bitcoin-swap-2015` | `admitted` | `human_reviewed` | 2026-05-16 | 2 | ok | 2026-05-16 | 2 | ok | ok |
| `tether-doj-pig-butchering-freeze-2023` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-22 | 26 | ok | no_audit_recorded |
| `tether-dprk-precommit-freeze-2025` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-22 | 26 | ok | no_audit_recorded |
| `tether-retroactive-sweep-2023` | `admitted` | `human_authored` | 2026-04-22 | 26 | ok | 2026-04-22 | 26 | ok | ok |
| `tornado-cash-ofac-2022` | `admitted` | `human_authored` | 2026-04-22 | 26 | ok | 2026-04-21 | 27 | ok | ok |
| `tornado-cash-ofac-delisting-2025` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-21 | 27 | ok | no_audit_recorded |
| `tornado-cash-ofac-redesignation-2022` | `admitted` | `human_authored` | 2026-04-22 | 26 | ok | 2026-04-21 | 27 | ok | ok |
| `turkey-cbrt-crypto-ban-2021` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-22 | 26 | ok | no_audit_recorded |
| `uk-fca-binance-markets-2021` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-05-16 | 2 | ok | no_audit_recorded |
| `uniswap-frontend-delisting-2023` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-22 | 26 | ok | no_audit_recorded |
| `zservers-ofac-2025` | `admitted` | `human_authored` | 2026-05-15 | 3 | ok | 2026-04-22 | 26 | ok | ok |

## Events flagged (any non-`ok` summary)

- `aeza-group-ofac-2025` — audit=no_audit_recorded, verification=ok, verif_age=26d
- `binance-4framework-2023` — audit=no_audit_recorded, verification=ok, verif_age=26d
- `bitzlato-doj-2023` — audit=no_audit_recorded, verification=ok, verif_age=27d
- `blender-ofac-2022` — audit=no_audit_recorded, verification=ok, verif_age=27d
- `btc-e-doj-2017` — audit=no_audit_recorded, verification=ok, verif_age=26d
- `canada-convoy-freeze-2022` — audit=no_audit_recorded, verification=ok, verif_age=26d
- `cftc-v-ooki-dao-2022` — audit=no_audit_recorded, verification=ok, verif_age=26d
- `chatex-ofac-2021` — audit=no_audit_recorded, verification=ok, verif_age=26d
- `china-pboc-crypto-ban-2021` — audit=no_audit_recorded, verification=ok, verif_age=27d
- `chipmixer-doj-2023` — audit=no_audit_recorded, verification=ok, verif_age=26d
- `circle-usdc-tornado-2022` — audit=no_audit_recorded, verification=ok, verif_age=26d
- `coinbase-india-exit-2022` — audit=no_audit_recorded, verification=ok, verif_age=26d
- `dprk-usdt-network-ofac-2025` — audit=no_audit_recorded, verification=ok, verif_age=26d
- `eu-12th-russia-sanctions-2023` — audit=no_audit_recorded, verification=ok, verif_age=26d
- `eu-mica-2023` — audit=no_audit_recorded, verification=ok, verif_age=26d
- `funnull-cdn-ofac-2025` — audit=no_audit_recorded, verification=ok, verif_age=26d
- `garantex-ofac-2022` — audit=no_audit_recorded, verification=ok, verif_age=27d
- `grinex-garantex-successor-ofac-2025` — audit=no_audit_recorded, verification=ok, verif_age=27d
- `hydra-doj-2022` — audit=no_audit_recorded, verification=ok, verif_age=26d
- `hydra-ofac-2022` — audit=no_audit_recorded, verification=ok, verif_age=27d
- `india-rbi-crypto-ban-2018` — audit=no_audit_recorded, verification=ok, verif_age=26d
- `korea-travel-rule-2022` — audit=no_audit_recorded, verification=ok, verif_age=26d
- `lockbit-affiliates-ofac-2024` — audit=no_audit_recorded, verification=ok, verif_age=26d
- `nigeria-cbn-crypto-ban-2021` — audit=no_audit_recorded, verification=ok, verif_age=26d
- `ofac-recent-action-20240111` — audit=no_audit_recorded, verification=ok, verif_age=2d
- `paxos-busd-nydfs-minting-stop-2023` — audit=no_audit_recorded, verification=ok, verif_age=2d
- `philippines-sec-binance-block-2024` — audit=no_audit_recorded, verification=ok, verif_age=2d
- `russia-election-interference-ofac-2020` — audit=no_audit_recorded, verification=ok, verif_age=26d
- `russian-cyber-theft-ofac-2020` — audit=no_audit_recorded, verification=ok, verif_age=26d
- `samourai-doj-2024` — audit=no_audit_recorded, verification=ok, verif_age=26d
- `sec-v-uniswap-wells-notice-2024` — audit=no_audit_recorded, verification=ok, verif_age=12d
- `suex-ofac-2021` — audit=no_audit_recorded, verification=ok, verif_age=27d
- `tether-doj-pig-butchering-freeze-2023` — audit=no_audit_recorded, verification=ok, verif_age=26d
- `tether-dprk-precommit-freeze-2025` — audit=no_audit_recorded, verification=ok, verif_age=26d
- `tornado-cash-ofac-delisting-2025` — audit=no_audit_recorded, verification=ok, verif_age=27d
- `turkey-cbrt-crypto-ban-2021` — audit=no_audit_recorded, verification=ok, verif_age=26d
- `uk-fca-binance-markets-2021` — audit=no_audit_recorded, verification=ok, verif_age=2d
- `uniswap-frontend-delisting-2023` — audit=no_audit_recorded, verification=ok, verif_age=26d
