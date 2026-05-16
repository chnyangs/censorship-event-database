# US Federal Crypto Enforcement Triage Manifest — Phase A.1 Discovery

- **Generated:** 2026-05-16
- **Frame:** `us_federal_enforcement_crypto_2017_2026`
- **Scope window:** 2017-01-01 → 2026-05-16
- **Method:** Agent-enumerated from domain knowledge, cross-checked against `events/*.yaml` and `candidate_triggers/*.yaml`. No automated scraper used.
- **Output state:** Discovery only — no `events/*.yaml` files written.
- **Candidate totals:** 24 total → **P0: 7**, **P1: 12**, **P2: 5**

## Exclusion notes

- OFAC SDN actions excluded except where they materially extend named-ransomware coverage already in S1; OFAC stratum is densely covered.
- Tornado-cash developer cases (Pertsev, Storm, Semenov) already covered by `pertsev-nl-arrest-2022`, `storm-semenov-doj-2023`, `semenov-ofac-2023` and not re-enumerated (one P2 candidate flags possible SDNY-vs-Storm-document split).
- FTX is split: SBF criminal trial as `ftx-bankman-fried-doj-2022` (P0); SEC v. FTX civil as `sec-v-ftx-2022` (P1); CFTC v. FTX as `cftc-v-ftx-2022` (P1). Bankruptcy court actions (Voyager/Celsius/BlockFi) enumerated separately where federal courts are the legal actor.
- Beaxy already covered by `sec-beaxy-platform-shutdown-2023`, not re-enumerated.
- Welcome to Video 2019 is a Son (CSAM darknet) operator, distinct from Helix/Harmon — both relevant; only Helix is in corpus.

## Candidate table

| # | Slug | Actor | Trigger | Date | Target | Layers | Load-Bearing | Pri | Rationale |
|---|------|-------|---------|------|--------|--------|--------------|-----|-----------|
| 1 | `sec-v-telegram-ton-2020` | US_SEC | sec_action | 2020-03-24 | Telegram Group Inc. / TON Issuer Inc. — Gram offering halt | offramp_cex, asset_onchain | offramp_cex | **P0** | Landmark $1.7B SAFT-framework injunction halted Gram distribution pre-mainnet; foundational precedent before Ripple. |
| 2 | `sec-v-ripple-2020` | US_SEC | sec_action | 2020-12-22 | Ripple Labs + Garlinghouse + Larsen — XRP | offramp_cex, asset_onchain | offramp_cex | **P0** | Most-cited US securities action against major token issuer; produced clean cascade of US CEX XRP delistings (Coinbase/Bitstamp/Binance.US/Kraken) within 4 weeks. |
| 3 | `welcome-to-video-doj-2019` | US_DOJ | doj_indictment | 2019-10-16 | Jong Woo Son CSAM darknet; 337 users charged | l4_frontend, asset_onchain, offramp_cex | l4_frontend | **P0** | Largest darknet CSAM bitcoin takedown; coordinated IRS-CI/DOJ/HMRC/Korean NPA; cleanest address-traceability cascade. |
| 4 | `ftx-bankman-fried-doj-2022` | US_DOJ_SDNY | doj_indictment | 2022-12-13 | SBF + FTX Trading + Alameda — wire fraud, money laundering | l4_frontend, offramp_cex, asset_onchain | offramp_cex | **P0** | Highest-profile US crypto exchange criminal indictment of the decade; conv. Nov-2023, sentenced Mar-2024; FTX.com geofencing, Alameda freezes, Ch.11 freeze. |
| 5 | `binance-cftc-2023` | US_CFTC | cftc_action | 2023-03-27 | Binance Holdings + CZ + Samuel Lim — CEA evasion | offramp_cex | offramp_cex | **P0** | CFTC suit predates DOJ 4-framework by 8 months and SEC by 70 days; missing leg of the multi-agency Binance cascade. |
| 6 | `genesis-sec-gemini-earn-2023` | US_SEC | sec_action | 2023-01-12 | Genesis Global Capital + Gemini Trust — Gemini Earn | offramp_cex | offramp_cex | **P0** | Major lending-product enforcement parallel to BlockFi 2022; settled Feb-2024 for $21M + $1.1B returned customer assets. |
| 7 | `celsius-bankruptcy-mashinsky-doj-2023` | US_DOJ_SDNY | doj_indictment | 2023-07-13 | Mashinsky + Celsius — securities/wire/commodities fraud + CEL manipulation | asset_onchain, offramp_cex | offramp_cex | **P0** | Highest-profile crypto-lender criminal indictment alongside SBF; parallel SEC/CFTC/FTC same day; CEL token + withdrawal-freeze cascade. Pleaded guilty Dec-2024. |
| 8 | `sec-v-bittrex-2023` | US_SEC | sec_action | 2023-04-17 | Bittrex Inc. + Bittrex Global + Shihara | l4_frontend, offramp_cex | offramp_cex | P1 | Bittrex announced US exit weeks before SEC suit, filed Ch.11 May-2023; clean regulatory→full-market-exit cascade; $24M settle Aug-2023. |
| 9 | `kraken-sec-unregistered-exchange-2023` | US_SEC | sec_action | 2023-11-20 | Payward Inc. (Kraken) — unregistered exchange/broker/dealer | offramp_cex | offramp_cex | P1 | Distinct from `kraken-sec-staking-2023` (Feb-2023); this is the Nov-2023 unregistered-exchange suit, dismissed Mar-2025 under Atkins SEC — counter-datapoint to SEC retreat. |
| 10 | `sec-v-coinbase-staking-wells-2023` | US_SEC | sec_wells_notice | 2023-03-22 | Coinbase Global — Wells Notice (listed assets + staking + Wallet) | l4_frontend, offramp_cex | offramp_cex | P1 | Predates formal SEC complaint (`sec-v-coinbase-2023`) by 76 days; analogous to `sec-v-uniswap-wells-notice-2024` for early-warning class. |
| 11 | `tornado-cash-developer-roman-storm-conviction-2025` | US_DOJ_SDNY | doj_conviction | 2025-08-06 | Roman Storm — partial guilty verdict on § 1960 | l4_frontend, asset_onchain | asset_onchain | P1 | Conviction phase of `storm-semenov-doj-2023`; key post-OFAC-delisting datapoint that DOJ criminal track survived. |
| 12 | `bitfinex-tether-cftc-2021` | US_CFTC | cftc_action | 2021-10-15 | Tether Holdings + iFinex — false USDT reserves statements | asset_onchain, offramp_cex | asset_onchain | P1 | $42.5M; foundational US federal precedent on USDT issuer accountability; precursor to existing `tether-*-freeze` events. |
| 13 | `bitmex-fincen-2024` | US_FINCEN | fincen_action | 2024-01-10 | HDR Global Trading (BitMEX) — BSA AML willful violations | offramp_cex | offramp_cex | P1 | $100M FinCEN penalty; FinCEN-specific BSA component completed years after `bitmex-cftc-doj-2020`; multi-agency chronology. |
| 14 | `voyager-bankruptcy-doj-objection-2023` | US_DOJ | bankruptcy_court_intervention | 2023-03-08 | Voyager Digital — DOJ stay of Binance.US asset-sale plan | offramp_cex | offramp_cex | P1 | US Trustee/DOJ blocked $1.022B Binance.US deal; federal-court mediated cascade on customer-asset rails. |
| 15 | `sec-v-ftx-2022` | US_SEC | sec_action | 2022-12-13 | SBF + FTX Trading + Alameda — civil fraud / FTT | offramp_cex, asset_onchain | offramp_cex | P1 | Parallel SEC civil filing same day as DOJ criminal; securities-law axis of multi-agency FTX cascade. |
| 16 | `cftc-v-ftx-2022` | US_CFTC | cftc_action | 2022-12-13 | FTX Trading + SBF + Alameda — CEA fraud | offramp_cex | offramp_cex | P1 | Third leg of same-day DOJ/SEC/CFTC tri-charge against SBF; completes multi-agency cascade triangulation. |
| 17 | `kingdom-trust-fincen-2021` | US_FINCEN | fincen_action | 2021-08-10 | Larry Dean Harmon (Helix follow-on) — $60M FinCEN civil penalty | offramp_cex | offramp_cex | P1 | FinCEN's first civil penalty against a mixer operator; pairs with existing `helix-doj-mixer-2020` as multi-agency follow-on. |
| 18 | `sinbad-doj-2024` | US_DOJ | doj_indictment | 2024-02-21 | Sinbad.io infrastructure (joint with Dutch FIOD / Finland NBI) | l4_frontend | l4_frontend | P1 | Existing `sinbad-ofac-2023` is OFAC SDN; this is the DOJ-led seizure-and-operator track; samourai-style takedown banner. |
| 19 | `polynonce-bittrex-fincen-2022` | US_FINCEN | fincen_action | 2022-10-11 | Bittrex Inc. — $29M concurrent FinCEN/OFAC penalty | offramp_cex | offramp_cex | P1 | Joint FinCEN-OFAC action 18 months before `sec-v-bittrex-2023` + Ch.11; cleanest dual-agency exchange BSA/sanctions cascade. |
| 20 | `bitfinex-tether-nyag-2021` | US_NYAG | state_ag_action | 2021-02-23 | iFinex + Tether — $18.5M reserve-misstatement settlement | asset_onchain, offramp_cex | offramp_cex | P2 | State-level, not federal; included as precursor to CFTC 2021 case; admit only if scope window allows NY AG. |
| 21 | `tornado-cash-pertsev-doj-indictment-2023` | US_DOJ_SDNY | doj_indictment | 2023-08-23 | Alexey Pertsev — US criminal indictment parallel to Dutch | asset_onchain | asset_onchain | P2 | Verify whether SDNY indictment is distinct document from `storm-semenov-doj-2023` filing; admit only if distinct. |
| 22 | `binance-fincen-doj-ofac-2023-fincen-component` | US_FINCEN | fincen_action | 2023-11-21 | Binance Holdings — FinCEN $3.4B + 5-yr monitorship | offramp_cex | offramp_cex | P2 | Verify whether `binance-4framework-2023` already subsumes FinCEN-specific monitorship clause; admit only if explicit split warranted. |
| 23 | `salame-ftx-campaign-finance-doj-2023` | US_DOJ_SDNY | doj_plea | 2023-09-07 | Ryan Salame (FTX co-CEO) — campaign-finance + money-transmitter plea | offramp_cex | offramp_cex | P2 | Co-defendant track to SBF; admit only if dataset structure rewards co-defendant granularity. |
| 24 | `tornado-cash-tornadocash-org-seizure-2022` | US_OFAC | ofac_collateral_l4 | 2022-08-08 | tornado.cash domain + GitHub repo | l4_frontend | l4_frontend | P2 | L4 cascade companion to `tornado-cash-ofac-2022`; GitHub takedown + Infura/Alchemy RPC blocking may already be coded within parent. Verify before admission. |

## Notes on cross-checks

All 24 slugs verified absent from `events/*.yaml` at generation time (cross-checked via `os.listdir`). Where existing event ids are similar in name (e.g. `helix-doj-mixer-2020`, `pertsev-nl-arrest-2022`, `storm-semenov-doj-2023`, `tornado-cash-ofac-2022`, `binance-4framework-2023`, `sec-v-binance-2023`, `sinbad-ofac-2023`, `kraken-sec-staking-2023`, `sec-v-coinbase-2023`, `sec-v-uniswap-wells-notice-2024`, `sec-beaxy-platform-shutdown-2023`, `bitmex-cftc-doj-2020`, `blockfi-sec-lending-2022`), the rationale field documents the distinction (different agency, different date, different doctrine, or different cascade scope).

## Next steps (out of scope for this discovery pass)

- Promote P0 candidates first; cross-check the 5 P2 verify-before-admit items.
- For each admitted candidate, follow the existing event-template path: capture canonical citation HTML, attach OONI L0 query, search Wayback for L4 diffs, attach chain-analytics anchors for `offramp_cex`.
