# L0 OONI coverage summary

Dataset snapshot: v0.2.0-rc-dryrun-11 · cutoff `2026-06-01` · commit `00764cd` · generated `2026-06-01T00:00:00Z`

This artifact summarizes archived OONI web-connectivity query outputs for candidate L0 network-layer evidence. It is denominator-aware: `no_ooni_measurements` means the public OONI query returned no measurements for that domain/window, not that blocking was absent.

## Denominator classes

| denominator_class | rows |
| --- | ---: |
| `measurement_denominator` | 2 |
| `no_ooni_measurements` | 23 |

## Event coverage

| event_id | domain rows | measurement-denominator rows | no-measurement rows | query-error rows |
| --- | ---: | ---: | ---: | ---: |
| `aeza-group-ofac-2025` | 3 | 0 | 3 | 0 |
| `binance-4framework-2023` | 1 | 0 | 1 | 0 |
| `blender-ofac-2022` | 2 | 0 | 2 | 0 |
| `btc-e-doj-2017` | 1 | 0 | 1 | 0 |
| `chatex-ofac-2021` | 1 | 0 | 1 | 0 |
| `china-pboc-crypto-ban-2021` | 1 | 0 | 1 | 0 |
| `chipmixer-doj-2023` | 1 | 0 | 1 | 0 |
| `cryptex-ofac-2024` | 1 | 0 | 1 | 0 |
| `funnull-cdn-ofac-2025` | 4 | 0 | 4 | 0 |
| `garantex-ofac-2022` | 1 | 0 | 1 | 0 |
| `nigeria-binance-network-block-2024-02` | 1 | 1 | 0 | 0 |
| `philippines-sec-binance-block-2024` | 1 | 1 | 0 | 0 |
| `samourai-doj-2024` | 2 | 0 | 2 | 0 |
| `sinbad-ofac-2023` | 1 | 0 | 1 | 0 |
| `suex-ofac-2021` | 1 | 0 | 1 | 0 |
| `tornado-cash-ofac-2022` | 3 | 0 | 3 | 0 |

## Applicable-event coverage

| class | events |
| --- | ---: |
| `queried_no_ooni_measurements` | 16 |
| `not_queried_yet` | 26 |
| `cp_not_ingested_v0_1` | 42 |

`not_queried_yet` events: `bitriver-russia-mining-ofac-2022-04`, `bitzlato-doj-2023`, `china-pboc-exchange-access-block-2019-06`, `china-search-engine-social-keyword-exchange-block-2021-06`, `genesis-market-ofac-2023-04`, `grinex-garantex-successor-ofac-2025`, `hydra-ofac-2022`, `india-fiu-offshore-vda-block-2023`, `indonesia-bappebti-illegal-exchange-block-2023`, `iran-ransomware-ofac-2018`, `kazakhstan-internet-shutdown-mining-2022-01`, `malaysia-sc-binance-disable-2021`, `media-land-volosovik-bulletproof-ofac-2025-11`, `netex24-bitpapa-russia-crypto-ofac-2024-03`, `ofac-hamas-buy-cash-msb-2023-10`, `ofac-recent-action-20240111`, `sec-beaxy-platform-shutdown-2023`, `semenov-ofac-2023`, `sinbad-doj-2024`, `task-force-rusich-ofac-2022-09`, `thailand-sec-binance-bybit-c-and-d-2021`, `tornado-cash-ofac-delisting-2025`, `tornado-cash-ofac-redesignation-2022`, `wang-hongfei-fentanyl-precursor-ofac-2023-04`, `zheng-yan-fentanyl-ofac-2019-08`, `zservers-ofac-2025`.


## Phrasing lock

- A zero-result OONI query is an observability gap, not evidence of no L0 censorship.
- Any L0 rate must be scoped to returned measurements, countries, domains, and time windows.
- Event YAML `coverage.status` remains authoritative; this artifact only summarizes attached raw query surfaces.
