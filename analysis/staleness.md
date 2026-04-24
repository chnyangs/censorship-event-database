# Staleness report

Generated at: `2026-04-24T10:11:02Z`
Red threshold: audits / verifications older than `90` days.
Most recent agent activity in `candidate_triggers/`: `2026-04-21T01:42:36.787155Z`.

## Coverage snapshot

Two dimensions tracked per event; missing values surface as explicit gaps, never masked.

- **Adversarial audit** (`last_human_audit`): {'no_audit_recorded': 48, 'ok': 5}
- **Verification** (`last_verified`): {'ok': 53}
- **Row-level summary** (worst of the two): {'no_audit_recorded': 48, 'ok': 5}

## Flag legend

- `ok` — within the red threshold
- `red` — older than 90 days
- `no_audit_recorded` — no last_human_audit on record — event has never been through an adversarial audit
- `no_verification_recorded` — no last_verified on record — event has never been re-verified
- `error` — event YAML failed to parse

## Per-event table

| Event | Status | Origin | last_human_audit | Audit age | Audit flag | last_verified | Verification age | Verif flag | Summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `aeza-group-ofac-2025` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-22 | 2 | ok | no_audit_recorded |
| `binance-4framework-2023` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-22 | 2 | ok | no_audit_recorded |
| `bitzlato-doj-2023` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-21 | 3 | ok | no_audit_recorded |
| `blender-ofac-2022` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-21 | 3 | ok | no_audit_recorded |
| `btc-e-doj-2017` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-22 | 2 | ok | no_audit_recorded |
| `canada-convoy-freeze-2022` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-22 | 2 | ok | no_audit_recorded |
| `cftc-v-ooki-dao-2022` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-22 | 2 | ok | no_audit_recorded |
| `chatex-ofac-2021` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-22 | 2 | ok | no_audit_recorded |
| `china-pboc-crypto-ban-2021` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-21 | 3 | ok | no_audit_recorded |
| `chipmixer-doj-2023` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-22 | 2 | ok | no_audit_recorded |
| `circle-usdc-tornado-2022` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-22 | 2 | ok | no_audit_recorded |
| `coinbase-india-exit-2022` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-22 | 2 | ok | no_audit_recorded |
| `cryptex-ofac-2024` | `admitted` | `human_authored` | 2026-04-22 | 2 | ok | 2026-04-21 | 3 | ok | ok |
| `dprk-usdt-network-ofac-2025` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-22 | 2 | ok | no_audit_recorded |
| `eu-12th-russia-sanctions-2023` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-22 | 2 | ok | no_audit_recorded |
| `eu-mica-2023` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-22 | 2 | ok | no_audit_recorded |
| `funnull-cdn-ofac-2025` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-22 | 2 | ok | no_audit_recorded |
| `garantex-ofac-2022` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-21 | 3 | ok | no_audit_recorded |
| `grinex-garantex-successor-ofac-2025` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-21 | 3 | ok | no_audit_recorded |
| `hydra-doj-2022` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-22 | 2 | ok | no_audit_recorded |
| `hydra-ofac-2022` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-21 | 3 | ok | no_audit_recorded |
| `india-rbi-crypto-ban-2018` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-22 | 2 | ok | no_audit_recorded |
| `iran-ransomware-ofac-2018` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-22 | 2 | ok | no_audit_recorded |
| `irgc-ransomware-ofac-2022` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-22 | 2 | ok | no_audit_recorded |
| `korea-travel-rule-2022` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-22 | 2 | ok | no_audit_recorded |
| `lazarus-entity-ofac-2019` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-22 | 2 | ok | no_audit_recorded |
| `lazarus-laundering-ofac-2020` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-22 | 2 | ok | no_audit_recorded |
| `lockbit-affiliates-ofac-2024` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-22 | 2 | ok | no_audit_recorded |
| `lockbit-leader-ofac-2024` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-22 | 2 | ok | no_audit_recorded |
| `matveev-ofac-2023` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-22 | 2 | ok | no_audit_recorded |
| `nigeria-cbn-crypto-ban-2021` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-22 | 2 | ok | no_audit_recorded |
| `pertsev-nl-arrest-2022` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-22 | 2 | ok | no_audit_recorded |
| `russia-election-interference-ofac-2020` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-22 | 2 | ok | no_audit_recorded |
| `russian-cyber-theft-ofac-2020` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-22 | 2 | ok | no_audit_recorded |
| `russian-cybercrime-infra-ofac-2025` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-22 | 2 | ok | no_audit_recorded |
| `samourai-doj-2024` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-22 | 2 | ok | no_audit_recorded |
| `sec-v-binance-2023` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-22 | 2 | ok | no_audit_recorded |
| `sec-v-coinbase-2023` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-22 | 2 | ok | no_audit_recorded |
| `sec-v-uniswap-wells-notice-2024` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-22 | 2 | ok | no_audit_recorded |
| `semenov-ofac-2023` | `admitted` | `human_authored` | 2026-04-22 | 2 | ok | 2026-04-21 | 3 | ok | ok |
| `sichuan-silence-ofac-2024` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-22 | 2 | ok | no_audit_recorded |
| `sinbad-ofac-2023` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-21 | 3 | ok | no_audit_recorded |
| `storm-semenov-doj-2023` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-22 | 2 | ok | no_audit_recorded |
| `suex-ofac-2021` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-21 | 3 | ok | no_audit_recorded |
| `tether-doj-pig-butchering-freeze-2023` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-22 | 2 | ok | no_audit_recorded |
| `tether-dprk-precommit-freeze-2025` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-22 | 2 | ok | no_audit_recorded |
| `tether-retroactive-sweep-2023` | `admitted` | `human_authored` | 2026-04-22 | 2 | ok | 2026-04-22 | 2 | ok | ok |
| `tornado-cash-ofac-2022` | `admitted` | `human_authored` | 2026-04-22 | 2 | ok | 2026-04-21 | 3 | ok | ok |
| `tornado-cash-ofac-delisting-2025` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-21 | 3 | ok | no_audit_recorded |
| `tornado-cash-ofac-redesignation-2022` | `admitted` | `human_authored` | 2026-04-22 | 2 | ok | 2026-04-21 | 3 | ok | ok |
| `turkey-cbrt-crypto-ban-2021` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-22 | 2 | ok | no_audit_recorded |
| `uniswap-frontend-delisting-2023` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-22 | 2 | ok | no_audit_recorded |
| `zservers-ofac-2025` | `admitted` | `human_authored` | — | — | no_audit_recorded | 2026-04-22 | 2 | ok | no_audit_recorded |

## Events flagged (any non-`ok` summary)

- `aeza-group-ofac-2025` — audit=no_audit_recorded, verification=ok, verif_age=2d
- `binance-4framework-2023` — audit=no_audit_recorded, verification=ok, verif_age=2d
- `bitzlato-doj-2023` — audit=no_audit_recorded, verification=ok, verif_age=3d
- `blender-ofac-2022` — audit=no_audit_recorded, verification=ok, verif_age=3d
- `btc-e-doj-2017` — audit=no_audit_recorded, verification=ok, verif_age=2d
- `canada-convoy-freeze-2022` — audit=no_audit_recorded, verification=ok, verif_age=2d
- `cftc-v-ooki-dao-2022` — audit=no_audit_recorded, verification=ok, verif_age=2d
- `chatex-ofac-2021` — audit=no_audit_recorded, verification=ok, verif_age=2d
- `china-pboc-crypto-ban-2021` — audit=no_audit_recorded, verification=ok, verif_age=3d
- `chipmixer-doj-2023` — audit=no_audit_recorded, verification=ok, verif_age=2d
- `circle-usdc-tornado-2022` — audit=no_audit_recorded, verification=ok, verif_age=2d
- `coinbase-india-exit-2022` — audit=no_audit_recorded, verification=ok, verif_age=2d
- `dprk-usdt-network-ofac-2025` — audit=no_audit_recorded, verification=ok, verif_age=2d
- `eu-12th-russia-sanctions-2023` — audit=no_audit_recorded, verification=ok, verif_age=2d
- `eu-mica-2023` — audit=no_audit_recorded, verification=ok, verif_age=2d
- `funnull-cdn-ofac-2025` — audit=no_audit_recorded, verification=ok, verif_age=2d
- `garantex-ofac-2022` — audit=no_audit_recorded, verification=ok, verif_age=3d
- `grinex-garantex-successor-ofac-2025` — audit=no_audit_recorded, verification=ok, verif_age=3d
- `hydra-doj-2022` — audit=no_audit_recorded, verification=ok, verif_age=2d
- `hydra-ofac-2022` — audit=no_audit_recorded, verification=ok, verif_age=3d
- `india-rbi-crypto-ban-2018` — audit=no_audit_recorded, verification=ok, verif_age=2d
- `iran-ransomware-ofac-2018` — audit=no_audit_recorded, verification=ok, verif_age=2d
- `irgc-ransomware-ofac-2022` — audit=no_audit_recorded, verification=ok, verif_age=2d
- `korea-travel-rule-2022` — audit=no_audit_recorded, verification=ok, verif_age=2d
- `lazarus-entity-ofac-2019` — audit=no_audit_recorded, verification=ok, verif_age=2d
- `lazarus-laundering-ofac-2020` — audit=no_audit_recorded, verification=ok, verif_age=2d
- `lockbit-affiliates-ofac-2024` — audit=no_audit_recorded, verification=ok, verif_age=2d
- `lockbit-leader-ofac-2024` — audit=no_audit_recorded, verification=ok, verif_age=2d
- `matveev-ofac-2023` — audit=no_audit_recorded, verification=ok, verif_age=2d
- `nigeria-cbn-crypto-ban-2021` — audit=no_audit_recorded, verification=ok, verif_age=2d
- `pertsev-nl-arrest-2022` — audit=no_audit_recorded, verification=ok, verif_age=2d
- `russia-election-interference-ofac-2020` — audit=no_audit_recorded, verification=ok, verif_age=2d
- `russian-cyber-theft-ofac-2020` — audit=no_audit_recorded, verification=ok, verif_age=2d
- `russian-cybercrime-infra-ofac-2025` — audit=no_audit_recorded, verification=ok, verif_age=2d
- `samourai-doj-2024` — audit=no_audit_recorded, verification=ok, verif_age=2d
- `sec-v-binance-2023` — audit=no_audit_recorded, verification=ok, verif_age=2d
- `sec-v-coinbase-2023` — audit=no_audit_recorded, verification=ok, verif_age=2d
- `sec-v-uniswap-wells-notice-2024` — audit=no_audit_recorded, verification=ok, verif_age=2d
- `sichuan-silence-ofac-2024` — audit=no_audit_recorded, verification=ok, verif_age=2d
- `sinbad-ofac-2023` — audit=no_audit_recorded, verification=ok, verif_age=3d
- `storm-semenov-doj-2023` — audit=no_audit_recorded, verification=ok, verif_age=2d
- `suex-ofac-2021` — audit=no_audit_recorded, verification=ok, verif_age=3d
- `tether-doj-pig-butchering-freeze-2023` — audit=no_audit_recorded, verification=ok, verif_age=2d
- `tether-dprk-precommit-freeze-2025` — audit=no_audit_recorded, verification=ok, verif_age=2d
- `tornado-cash-ofac-delisting-2025` — audit=no_audit_recorded, verification=ok, verif_age=3d
- `turkey-cbrt-crypto-ban-2021` — audit=no_audit_recorded, verification=ok, verif_age=2d
- `uniswap-frontend-delisting-2023` — audit=no_audit_recorded, verification=ok, verif_age=2d
- `zservers-ofac-2025` — audit=no_audit_recorded, verification=ok, verif_age=2d
