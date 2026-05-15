# L0 OONI coverage summary

Dataset snapshot: v0.1.0 · cutoff `2026-05-06` · commit `5b8d353` · generated `2026-05-14T11:24:13Z`

This artifact summarizes archived OONI web-connectivity query outputs for candidate L0 network-layer evidence. It is denominator-aware: `no_ooni_measurements` means the public OONI query returned no measurements for that domain/window, not that blocking was absent.

## Denominator classes

| denominator_class | rows |
| --- | ---: |
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
| `samourai-doj-2024` | 2 | 0 | 2 | 0 |
| `sinbad-ofac-2023` | 1 | 0 | 1 | 0 |
| `suex-ofac-2021` | 1 | 0 | 1 | 0 |
| `tornado-cash-ofac-2022` | 3 | 0 | 3 | 0 |

## Applicable-event coverage

| class | events |
| --- | ---: |
| `queried_no_ooni_measurements` | 14 |
| `not_queried_yet` | 8 |
| `cp_not_ingested_v0_1` | 22 |

`not_queried_yet` events: `bitzlato-doj-2023`, `grinex-garantex-successor-ofac-2025`, `hydra-ofac-2022`, `iran-ransomware-ofac-2018`, `semenov-ofac-2023`, `tornado-cash-ofac-delisting-2025`, `tornado-cash-ofac-redesignation-2022`, `zservers-ofac-2025`.


## Phrasing lock

- A zero-result OONI query is an observability gap, not evidence of no L0 censorship.
- Any L0 rate must be scoped to returned measurements, countries, domains, and time windows.
- Event YAML `coverage.status` remains authoritative; this artifact only summarizes attached raw query surfaces.
