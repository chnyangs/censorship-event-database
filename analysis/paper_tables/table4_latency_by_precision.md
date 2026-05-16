# Table 4 · Latency evidence surface (precision-filtered)

Dataset snapshot: **v0.2.0-rc-dryrun-2** · cutoff `2026-05-16` · commit `f8dc941` · generated `2026-05-16T12:00:00Z`

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

## Panel B · Day-precision triggers (n=43)

Day-precision triggers cannot support hour-granularity latency claims. The event's `time_to_first_change_hours` is converted into a conservative interval `[max(0, H-24), H]`; rows crossing a day-band boundary are reported as `ambiguous_boundary`. Per-event hour values in the CSV dump are **record-level artifacts** (timestamp arithmetic) and must not enter any hour-bucketed paper claim.

| day-granularity interval band | count | events |
| --- | ---: | --- |
| ≤1d | 27 | `alphabay-hansa-doj-2017`, `binance-4framework-2023`, `bitzlato-doj-2023`, `blockfi-sec-lending-2022`, `btc-e-doj-2017`, `canada-convoy-freeze-2022`, `chipmixer-doj-2023`, `cryptex-ofac-2024`, `dprk-usdt-network-ofac-2025`, `eu-12th-russia-sanctions-2023`, `eu-mica-2023`, `eu-russia-crypto-wallet-cap-2022`, `funnull-cdn-ofac-2025`, `garantex-ofac-2022`, `grinex-garantex-successor-ofac-2025`, `hydra-doj-2022`, `hydra-ofac-2022`, `korea-travel-rule-2022`, `kraken-sec-staking-2023`, `kucoin-doj-2024`, `nigeria-cbn-crypto-ban-2021`, `nydfs-bitlicense-2015-06`, `samourai-doj-2024`, `sec-beaxy-platform-shutdown-2023`, `silk-road-doj-seizure-2013`, `tornado-cash-ofac-delisting-2025`, `uk-fca-binance-markets-2021` |
| (1d, 30d] | 6 | `blender-ofac-2022`, `china-pboc-crypto-ban-2013-12`, `coinbase-india-exit-2022`, `sec-v-binance-2023`, `suex-ofac-2021`, `turkey-cbrt-crypto-ban-2021` |
| >30d | 6 | `cftc-v-ooki-dao-2022`, `india-rbi-crypto-ban-2018`, `russia-election-interference-ofac-2020`, `russian-cyber-theft-ofac-2020`, `sec-v-coinbase-2023`, `tornado-cash-ofac-redesignation-2022` |
| ambiguous_boundary | 4 | `aeza-group-ofac-2025`, `chatex-ofac-2021`, `lockbit-affiliates-ofac-2024`, `semenov-ofac-2023` |
| **total** | **43** | |

## Panel C · Excluded from both panels — `trigger_is_action` (n=5)

| event_id | trigger_type |
| --- | --- |
| `circle-usdc-tornado-2022` | `corporate_policy_change` |
| `tether-doj-pig-butchering-freeze-2023` | `corporate_policy_change` |
| `tether-dprk-precommit-freeze-2025` | `corporate_policy_change` |
| `tether-retroactive-sweep-2023` | `corporate_policy_change` |
| `uniswap-frontend-delisting-2023` | `corporate_policy_change` |
