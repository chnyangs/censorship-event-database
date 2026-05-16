# L0 OONI coverage summary

Dataset snapshot: v0.2.0-rc-dryrun-4 · cutoff `2026-05-16` · commit `a0d61e2` · generated `2026-05-20T00:00:00Z`

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
| `not_queried_yet` | 14 |
| `cp_not_ingested_v0_1` | 28 |

`not_queried_yet` events: `bitzlato-doj-2023`, `grinex-garantex-successor-ofac-2025`, `hydra-ofac-2022`, `india-fiu-offshore-vda-block-2023`, `iran-ransomware-ofac-2018`, `malaysia-sc-binance-disable-2021`, `ofac-recent-action-20240111`, `philippines-sec-binance-block-2024`, `sec-beaxy-platform-shutdown-2023`, `semenov-ofac-2023`, `sinbad-doj-2024`, `tornado-cash-ofac-delisting-2025`, `tornado-cash-ofac-redesignation-2022`, `zservers-ofac-2025`.


## Phrasing lock

- A zero-result OONI query is an observability gap, not evidence of no L0 censorship.
- Any L0 rate must be scoped to returned measurements, countries, domains, and time windows.
- Event YAML `coverage.status` remains authoritative; this artifact only summarizes attached raw query surfaces.
