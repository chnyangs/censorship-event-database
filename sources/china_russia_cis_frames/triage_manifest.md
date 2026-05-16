# Phase C Triage Manifest — China + Russia + CIS Regulatory Frames

- Frame: `china_russia_cis_frames`
- Discovery date: 2026-05-16
- Stratum: S4_nation_state
- Scope window: 2017-01-01 → 2025-12-31

## Method

Agent-enumerated from domain knowledge, cross-checked against the 134 admitted events at `v0.2.0-rc-dryrun-6` and all `candidate_triggers/*.yaml`. Primary regulators in this frame issue documents in Chinese and Russian; for this lean Phase C pass, anchors are verified via English secondary sources (Reuters, CoinDesk, Bloomberg, SCMP, TASS English, CNBC, Library of Congress Global Legal Monitor, law-firm client alerts). Multilingual primary-document scraping is a documented follow-up requirement before admission.

## Already in corpus — DO NOT duplicate

- `china-pboc-crypto-ban-2013-12`
- `china-pboc-crypto-ban-2021`
- `russia-cbr-bitcoin-information-letter-2014`
- `russia-cbr-crypto-payment-ban-2022`
- `garantex-ofac-2022`, `grinex-garantex-successor-ofac-2025`
- `hydra-ofac-2022`, `hydra-doj-2022`
- `binance-russia-exit-commex-2023`
- `eu-russia-crypto-wallet-cap-2022`, `eu-russia-full-crypto-wallet-ban-2022`, `eu-12th-russia-sanctions-2023`

## Counts

| Priority | Count |
|---|---|
| P0 | 12 |
| P1 | 4 |
| P2 | 1 |
| **Total** | **17** |

Plus 4 deferred-for-followup items (Belarus PR8 permissive; RU Rosfinmonitoring diffuse; KG / TJ low-tier secondary).

## P0 candidates (12)

| Slug | Date | Actor | Verification | Layer |
|---|---|---|---|---|
| china-ico-ban-2017-09 | 2017-09-04 | CN PBOC + 7 ministries | verified | offramp_cex, asset_issuance |
| china-pboc-exchange-shutdown-2017-09 | 2017-09-29 | CN PBOC | verified | offramp_cex |
| china-state-council-mining-crackdown-2021-05 | 2021-05-21 | CN State Council FSDC | verified | mining_hashpower |
| china-inner-mongolia-mining-ban-2021-05 | 2021-05-25 | CN Inner Mongolia NDRC | verified | mining_hashpower |
| china-sichuan-mining-ban-2021-06 | 2021-06-18 | CN Sichuan NDRC | verified | mining_hashpower |
| china-pboc-ten-agencies-crypto-illegal-2021-09 | 2021-09-24 | CN PBOC + 9 agencies | needs_check (potential overlap with china-pboc-crypto-ban-2021) | offramp_cex |
| china-nft-secondary-trading-self-discipline-2022-06 | 2022-06-30 | CN Cultural Industry Assoc + Tencent/Ant/JD | verified | l4_frontend |
| hongkong-sfc-vatp-licensing-2023-06 | 2023-06-01 | HK SFC | verified | offramp_cex, l4_frontend |
| hongkong-hkma-stablecoins-ordinance-2025 | 2025-08-01 | HK HKMA + LegCo | verified | stablecoin_issuance |
| russia-mining-regional-ban-2024-12 | 2024-12-23 | RU Council of Ministers | verified | mining_hashpower |
| kazakhstan-internet-shutdown-mining-2022-01 | 2022-01-05 | KZ Govt (Tokayev) | verified | network_layer |
| kazakhstan-digital-assets-law-2023-02 | 2023-02-06 | KZ President Tokayev | verified | mining_hashpower, offramp_cex |

## P1 candidates (4)

| Slug | Date | Notes |
|---|---|---|
| china-weibo-crypto-exchange-purge-2021-03 | 2021-03-11 | Cleanest L4 social-media censorship — Weibo deactivates Binance/Huobi/OKEx |
| russia-dfa-law-2020 | 2020-07-31 | Mixed permissive/prohibitive; payment-prohibition prong is censorship-relevant |
| russia-mining-legalization-law-2024-08 | 2024-08-08 | Mostly permissive but authorises CBR regional-ban + miner-registry |
| ukraine-virtual-assets-law-2022-03 | 2022-03-16 | Wartime VASP registration; sanctions-screening obligation |

## P2 candidates (1)

| Slug | Date | Notes |
|---|---|---|
| uzbekistan-napp-vasp-licensing-2022-07 | 2022-07-14 | Licence-fee-as-barrier-to-entry; lower-tier secondary |

## Top 5 P0 rationales

1. **china-pboc-ten-agencies-crypto-illegal-2021-09** — The "comprehensive ban" notice declaring offshore-exchange service to PRC residents illegal; most-cited single PRC crypto event after 2021-05-21. NEEDS_CHECK whether already pinned by the existing `china-pboc-crypto-ban-2021` event YAML.
2. **china-sichuan-mining-ban-2021-06** — Province-level State Grid power-cut that dropped global hashrate ~37% within days; canonical close of the China-mining era.
3. **russia-mining-regional-ban-2024-12** — Council of Ministers 6-year mining ban in 10 regions including occupied Ukrainian oblasts — cross-jurisdictional contested-sovereignty mining censorship.
4. **kazakhstan-internet-shutdown-mining-2022-01** — Pure network-layer national censorship with measurable on-chain effect; unique non-financial-regulator nation-state action in the corpus.
5. **hongkong-hkma-stablecoins-ordinance-2025** — First HKMA-licensed stablecoin regime; HK$5M fine + 7yr imprisonment for unlicensed issuance; forecloses offshore stablecoin issuance to HK persons.

## Exclusion notes

- **Belarus Decree No. 8 (2017-12-21)** — Permissive HTP framework; legalised smart contracts. Documented `deferred=true`.
- **Russia DFA 2020 law** — Dual-character; included only on payment-prohibition prong.
- **Bitzlato 2023-01** — US DOJ + FinCEN action against RU-linked exchange; belongs in `federal_enforcement` frame, not RU-domestic.
- **Russia Rosfinmonitoring 'Transparent Blockchain'** — Diffuse, no discrete enforcement trigger pinned. Deferred.
- **Tajikistan / Turkmenistan / Kyrgyzstan** — In-scope-window restrictions are predominantly energy-driven temporary shutdowns or permissive regimes; Turkmenistan 2025-11 VA law is post-scope. Deferred or held as P2-needs-check.
- **Weibo 2021-08** — Specific August 2021 event in original brief could not be anchored via English secondary; load-bearing Weibo event is the 2021-03-11 deactivation cascade.

## Follow-up requirements

- Original-language primary-document retrieval (PRC PBOC notices, Russian Federation Council of Ministers decrees, Kazakh AIFC announcements) before admission.
- Verification that `china-pboc-ten-agencies-crypto-illegal-2021-09` does not duplicate the existing `china-pboc-crypto-ban-2021` event YAML — read that file's `primary_source` to confirm which notice it anchors.
- WeChat / Alipay crypto-keyword bans flagged in task brief: no discrete English secondary anchor surfaced; defer to multilingual scraper.
- Russia FSB-led KYC enforcement: no discrete event-shaped anchor; held as deferred-followup.
