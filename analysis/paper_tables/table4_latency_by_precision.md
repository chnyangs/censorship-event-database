# Table 4 · Latency distribution (precision-filtered)

Dataset snapshot: **v0.1.0** · cutoff `2026-04-22` · commit `573838c` · generated `2024-04-24T23:06:40Z`

Supports **C3** (`docs/paper_claims.md §1`). Only triggers with hour-or-better precision contribute to the hour-granularity panel; day-precision triggers are reported separately. `trigger_is_action` events (C4) are excluded from both panels and surfaced in Panel C — their t≈0 is a record-level artifact, not a measured delta.

## Panel A · Hour-precision triggers (n=2)

| band | count | events |
| --- | ---: | --- |
| t=0 | 0 | — |
| (0, 1]h | 0 | — |
| (1, 6]h | 1 | `tornado-cash-ofac-2022` |
| (6, 24]h | 1 | `china-pboc-crypto-ban-2021` |
| (24, 168]h (≤1w) | 0 | — |
| >168h (>1w) | 0 | — |
| **total** | **2** | |

## Panel B · Day-precision triggers (n=33)

Day-precision triggers cannot support hour-granularity latency claims. The event's `time_to_first_change_hours` is reported rounded down to a ≤1-day or >1-day classifier, not a scalar hour value. Per-event hour values in the CSV dump are **record-level artifacts** (timestamp arithmetic) and must not enter any hour-bucketed paper claim.

| day-granularity band | count | events |
| --- | ---: | --- |
| ≤1d | 19 | `binance-4framework-2023`, `bitzlato-doj-2023`, `btc-e-doj-2017`, `canada-convoy-freeze-2022`, `chipmixer-doj-2023`, `cryptex-ofac-2024`, `dprk-usdt-network-ofac-2025`, `eu-12th-russia-sanctions-2023`, `eu-mica-2023`, `funnull-cdn-ofac-2025`, `garantex-ofac-2022`, `grinex-garantex-successor-ofac-2025`, `hydra-doj-2022`, `hydra-ofac-2022`, `korea-travel-rule-2022`, `nigeria-cbn-crypto-ban-2021`, `samourai-doj-2024`, `sec-v-coinbase-2023`, `tornado-cash-ofac-delisting-2025` |
| (1d, 30d] | 9 | `aeza-group-ofac-2025`, `blender-ofac-2022`, `chatex-ofac-2021`, `coinbase-india-exit-2022`, `lockbit-affiliates-ofac-2024`, `sec-v-binance-2023`, `semenov-ofac-2023`, `suex-ofac-2021`, `turkey-cbrt-crypto-ban-2021` |
| >30d | 5 | `cftc-v-ooki-dao-2022`, `india-rbi-crypto-ban-2018`, `russia-election-interference-ofac-2020`, `russian-cyber-theft-ofac-2020`, `tornado-cash-ofac-redesignation-2022` |
| **total** | **33** | |

## Panel C · Excluded from both panels — `trigger_is_action` (n=5)

| event_id | trigger_type |
| --- | --- |
| `circle-usdc-tornado-2022` | `corporate_policy_change` |
| `tether-doj-pig-butchering-freeze-2023` | `corporate_policy_change` |
| `tether-dprk-precommit-freeze-2025` | `corporate_policy_change` |
| `tether-retroactive-sweep-2023` | `corporate_policy_change` |
| `uniswap-frontend-delisting-2023` | `corporate_policy_change` |
