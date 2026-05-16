# Japan FSA + OFAC Density Triage Manifest — Phase F Discovery

- **Generated:** 2026-05-16
- **Frame:** `japan_ofac_density_2014_2025`
- **Scope window:** 2014-01-01 → 2025-12-31
- **Temporal tier target:** `comparable_main_2017_present`
- **Analysis use target:** `main_corpus`
- **Method:** Agent-enumerated from domain knowledge, cross-checked against 156 admitted event ids in `events/*.yaml` and against the `candidate_triggers/*.yaml` set. Each candidate verified via WebSearch against primary FSA / Treasury press releases and contemporaneous Reuters / Bloomberg / CoinDesk / Cointelegraph / Chainalysis / TRM / Elliptic reporting.
- **Output state:** Discovery only — no `events/*.yaml` written.
- **Candidate totals:** 15 total → **P0: 10**, **P1: 3**, **P2: 1** (deferred), with one additional Japan FSA active candidate (re-counted below). All P0+P1 active = 13; plus 1 P2 deferred Japan candidate; plus the OFAC Sim Hyon Sop P1 needs_check; total 15.
- **Split:** Japan FSA: 8 (6 × P0, 1 × P1, 1 × P2-deferred). OFAC: 7 (5 × P0, 2 × P1).

## Already-present in this frame

**Japan FSA:** 1 event — `japan-fsa-coincheck-orders-2018.yaml` (the January 2018 NEM-hack business improvement orders).

**OFAC:** 28 events already in corpus (see task brief: tornado-cash, garantex, hydra, suex, sinbad, blender, chatex, lockbit, sichuan-silence, aeza, zservers, funnull, cryptex, dprk-usdt-network, lazarus 2019/2020, iran-ransomware 2018, irgc-ransomware 2022, matveev, semenov, russia-election 2020, russian-cyber-theft 2020, russian-cybercrime-infra 2025, tornado-cash redesignation 2022, tornado-cash delisting 2025, grinex 2025). Plus 21 OFAC Recent-Actions candidate triggers (`ofac-recent-action-*.yaml`) in `candidate_triggers/`. Zero overlap with the 7 OFAC candidates enumerated here — each maps to a distinct Treasury press release number (jy1816, jy2036, jy2213, jy1714, jy1874, jy2752, jy1438).

## Exclusion notes

- **Japan FSA Coincheck NEM hack January 2018** — already in corpus as `japan-fsa-coincheck-orders-2018`. NOT enumerated.
- **Japan FSA general crypto-exchange registration framework launch under PSA April 2017** — class-level legislative event, not an enforcement trigger. Out of scope for this enforcement-density frame.
- **Japan FSA liability-reserve mandate (parliamentary submission 2026)** — still in consultation, no enforcement trigger yet. NOT enumerated.
- **OFAC Garantex 2023 refresh** — sought but no standalone 2023 press release found; the 2022-04-05 original (already in corpus as `garantex-ofac-2022`) and the 2025-03 redesignation (already in corpus as `grinex-garantex-successor-ofac-2025`) bookend the trajectory. NOT enumerated.
- **OFAC Trickbot-Conti February 9 2023 first wave (jy1714 — early-2023 release)** — partial overlap with the September 7 2023 second wave in this manifest. The September wave is the P0 anchor because it covers the larger 11-designee + 9-DOJ-indictment cluster; the February wave can be admitted later as a related_events upstream. NOT separately enumerated.
- **OFAC USDT-on-Tron DPRK refresh 2024** (task-brief candidate) — already in corpus as `dprk-usdt-network-ofac-2025` (full network designation) and `tether-dprk-precommit-freeze-2025` (the on-chain freeze). NOT separately enumerated.

## Stratum terminology note

- **Japan FSA actions** → `S4_nation_state` (sub-stratum: financial-regulator). Match existing `japan-fsa-coincheck-orders-2018.yaml`.
- **OFAC Recent Actions** → `S1_ofac_sdn`. Match all 28 existing OFAC events in corpus.

The two strata together cover the enforcement-heaviest regulator pair in the corpus.

## P0 candidates (10)

| # | Slug | Actor | Date | Target | Layers | Pri | Rationale |
|---|------|-------|------|--------|--------|-----|-----------|
| 1 | `japan-fsa-zaif-orders-2018-09` | JP_FSA | 2018-09-25 | Tech Bureau Inc. / Zaif | offramp_cex | **P0** | Third FSA business improvement order to Zaif following 2018-09-14 $62.5M hot-wallet theft. Prior orders 2018-03 and 2018-06 had flagged system + governance + AML gaps. Cleanest Japan-FSA post-hack enforcement analogue to the Coincheck January 2018 action already in corpus. |
| 2 | `japan-fsa-six-exchange-orders-2018-06` | JP_FSA | 2018-06-22 | bitFlyer + Quoine + BTC Box + Bit Bank + BitPoint + Tech Bureau | offramp_cex | **P0** | Largest post-Coincheck FSA enforcement wave: simultaneous orders to six registered exchanges for AML/CFT + customer-ID + governance failures. bitFlyer voluntarily suspended new-account opening; Quoine's order lifted only July 2021. Predicate for the 2018-2019 Japanese crypto-exchange compliance retrofit. |
| 3 | `japan-fsa-dmm-bitcoin-order-2024-09` | JP_FSA | 2024-09-26 | DMM Bitcoin Co. Ltd. | offramp_cex, asset_onchain | **P0** | FSA business improvement order following 2024-05-31 hack drained 4,502.9 BTC (~$305-482M, largest 2024 crypto exchange hack worldwide). Entry vector: Ginco wallet-vendor compromise. Cited concentration of system-and-security ops + lack of independent audits. Order required improvement plan by 2024-10-28; DMM Bitcoin halted operations and transferred assets to SBI VC Trade by Q1 2025. |
| 4 | `japan-fsa-ftx-japan-suspension-2022-11` | JP_FSA | 2022-11-10 | FTX Japan Inc. | offramp_cex | **P0** | Kanto LFB issued simultaneous Business Suspension Order + Business Improvement Order under PSA + FIEA, effective immediately through 2022-12-09. Triggers: (i) withdrawal halt without timeline, (ii) parent FTX Trading Ltd. solvency uncertainty. Cleanest Japan FSA cross-border-parent-cascade enforcement. |
| 5 | `japan-fsa-travel-rule-effective-2023-06` | JP_FSA | 2023-06-01 | All registered VASPs | offramp_cex | **P0** | APTCP amendment implementing FATF R.16 Travel Rule entered into force 2023-06-01. Japan was first major developed nation to enact Travel Rule in primary legislation. Cleanest Japan parallel to `korea-travel-rule-2022` (corpus) and `fatf-r15-vasp-travel-rule-2019` (candidate_triggers/). |
| 6 | `japan-fsa-stablecoin-psa-effective-2023-06` | JP_FSA | 2023-06-01 | Stablecoin issuers (all chains) | asset_onchain, offramp_cex | **P0** | PSA amendment creating 'Electronic Payment Instruments' category effectively pre-emptively excluded USDT/USDC/DAI from regulated Japanese retail issuance. Issuance restricted to banks + money-transfer providers + trust companies. Sibling to `hongkong-hkma-stablecoins-ordinance-2025` (candidate_triggers/) as the second major APAC stablecoin framework. Same-day pair with the Travel Rule candidate. |
| 7 | `ofac-hamas-buy-cash-msb-2023-10` | US_OFAC | 2023-10-18 | Hamas operatives + Buy Cash MSB (Gaza) | offramp_cex, asset_onchain | **P0** | Treasury jy1816 — first post-Oct-7 OFAC action. Ten Hamas operatives + Gaza-based Buy Cash MSB (virtual-currency exchange including Bitcoin) + operator Ahmed M. M. Alaqad designated under EO 13224. Most paper-impactful single-day Hamas-crypto designation. NOT covered by any candidate_trigger. |
| 8 | `ofac-hamas-irgc-virtual-currency-network-2024-01` | US_OFAC | 2024-01-22 | Hamas-IRGC-QF crypto facilitators (Shamlakh family + Al-Markaziya) | offramp_cex, asset_onchain | **P0** | Treasury jy2036 — fifth Hamas wave. 13 individuals + 6 entities + 2 aircraft. Gaza-based moneychangers moving tens of millions in USDT from IRGC-Qods Force to Hamas + PIJ. Coordinated OFAC + UK OFSI + Australia DFAT. NOT covered by candidate_trigger ofac-recent-action-* set. |
| 9 | `ofac-hamas-gaza-now-2024-03` | US_OFAC | 2024-03-27 | Gaza Now / Al-Qureshi Executives / Aakhirah Ltd | offramp_cex, asset_onchain | **P0** | Treasury jy2213 — Gaza Now social-media fundraising network. Received ~$21K direct crypto donations post-Oct-7; aggregate deposit addresses received >$4.4M cumulative. Joint OFAC + UK OFSI same-day action. Third member of the Hamas-crypto-network OFAC cascade together with #7 (Buy Cash) and #8 (Shamlakh-IRGC). |
| 10 | `ofac-trickbot-conti-eleven-2023-09` | US_OFAC | 2023-09-07 | 11 Trickbot/Conti members (Galochkin / Rudenskiy / Tsarev) | offramp_cex, asset_onchain | **P0** | Treasury jy1714 — second wave following Feb 9 2023 first wave. 11 administrators + managers + developers + coders of Russia-based Trickbot/Conti. Concurrent DOJ unsealing of 9 indictments overlapping 7 of the 11 designees. UK NCA estimates $180M+ extortion. Joint OFAC + UK NCA action. |
| 11 | `ofac-zhdanova-russian-elite-launderer-2023-11` | US_OFAC | 2023-11-03 | Ekaterina Zhdanova (Russian national) | offramp_cex, asset_onchain | **P0** | Treasury jy1874 — first major individual Russia-related crypto-launderer designation under post-invasion EO 14024. Three BTC addresses added. Cases: March 2022 $2.3M to Western Europe; oligarch $100M to UAE. Primary rail: Garantex. Strong related_events anchor for `garantex-ofac-2022`, `grinex-garantex-successor-ofac-2025`, `russian-cybercrime-infra-ofac-2025`. |

(Total P0 = 10 across the table: rows 1-6 = Japan FSA, rows 7-11 = OFAC. The remaining slugs follow as P1 / P2.)

## P1 candidates (3)

| # | Slug | Actor | Date | Target | Layers | Pri | Rationale |
|---|------|-------|------|--------|--------|-----|-----------|
| 12 | `japan-fsa-binance-sakura-acquisition-2022-11` | JP_FSA | 2022-11-30 | Binance + Sakura Exchange BitCoin | offramp_cex | P1 | Binance 100% acquisition of JFSA-registered SEBC to re-enter Japan as FSA-regulated entity. FSA monitored compliance but consent was not formally required. Structural corporate-perimeter event rather than direct enforcement. Useful related_events anchor for `uk-fca-binance-markets-2021`, `philippines-sec-binance-block-2024`, `belgium-fsma-binance-cease-2023`, `malaysia-sc-binance-disable-2021` (all in candidate_triggers/). |
| 13 | `ofac-houthi-al-jamal-crypto-refresh-2024-12` | US_OFAC | 2024-12-17 | Sa'id al-Jamal (IRGC-QF Houthi financier) | offramp_cex, asset_onchain | P1 | Treasury jy2752 — updated 2021-06-10 designation to add five TRON USDT addresses. Hundreds of millions in stablecoin volumes attributable. Refresh rather than fresh designation, but the on-chain address addition is the load-bearing analytical artifact. Pairs naturally with `iran-ransomware-ofac-2018`, `irgc-ransomware-ofac-2022`. |
| 14 | `ofac-dprk-it-worker-sim-hyon-sop-2023-04` | US_OFAC | 2023-04-24 | Sim Hyon Sop (PRC-based KKBC banking rep) | offramp_cex, asset_onchain | P1 | OFAC 2023-04-24 designated Sim Hyon Sop, KKBC banking rep, for coordinating DPRK financial transfers + IT-worker crypto conversion. Later expanded December 17 2024 (jy2752) with Lu Huaying + Zhang Jian (UAE PRC nationals). Distinct from Lazarus state-sponsored cyber theft (already in corpus); targets the IT-worker revenue-generation channel. **`needs_check`**: confirm jy1438 URL stability — the December 2024 follow-on is the strongest verification pin. |

## P2 / deferred candidates (1)

| # | Slug | Actor | Date | Target | Pri | Rationale |
|---|------|-------|------|--------|-----|-----------|
| 15 | `japan-mof-meti-tornado-cash-designation-2022-12` | JP_METI_MOF | 2022-12-01 | Tornado Cash on Japan-side sanctions list | P2 (**`needs_check`** / **deferred**) | Task brief specified Japan-only Tornado Cash SDN December 2022. WebSearch surfaced Japan's FEFTA amendment approved December 2022 (effective April 2024) bringing crypto + electronic settlements under sanctions scope generally — but NO primary METI/MOF/FSA release specifying a Tornado-Cash-specific Japan designation was located. Defer until a primary MOF or METI Japanese-language release is pinned. If located, candidate would pair naturally with `tornado-cash-ofac-2022` as a non-US sovereign cascade. |

## Cross-check notes

All 14 slugs verified absent from `events/*.yaml` (156 ids) and `candidate_triggers/*.yaml` (`promoted_event_id`). Zero collisions.

The OFAC Recent-Action candidate triggers nearest in time to the OFAC P0 candidates here:
- `ofac-recent-action-20230823.yaml` is 15 days before `ofac-trickbot-conti-eleven-2023-09` (2023-09-07) — distinct release, no overlap.
- `ofac-recent-action-20231129.yaml` is 26 days after `ofac-zhdanova-russian-elite-launderer-2023-11` (2023-11-03) — distinct release, no overlap.
- `ofac-recent-action-20240220.yaml` is 29 days after `ofac-hamas-irgc-virtual-currency-network-2024-01` (2024-01-22) — distinct release, no overlap.
- `ofac-recent-action-20240507.yaml` is 41 days after `ofac-hamas-gaza-now-2024-03` (2024-03-27) — distinct release, no overlap.
- `ofac-recent-action-20241210.yaml` is 7 days before `ofac-houthi-al-jamal-crypto-refresh-2024-12` (2024-12-17) — distinct release, no overlap.

Close-by ids that should appear in `related_events` when these candidates are eventually promoted:
- Japan FSA candidates → `japan-fsa-coincheck-orders-2018`, `korea-travel-rule-2022`, `fatf-r15-vasp-travel-rule-2019` (candidate_triggers/), `hongkong-hkma-stablecoins-ordinance-2025` (candidate_triggers/).
- OFAC Hamas trio (#7-#9) → mutual cross-references; plus `iran-ransomware-ofac-2018`, `irgc-ransomware-ofac-2022`, `tether-dprk-precommit-freeze-2025` (for the on-chain freeze mechanism).
- OFAC Trickbot/Conti #10 → `lockbit-affiliates-ofac-2024`, `lockbit-leader-ofac-2024`, `matveev-ofac-2023`, `russian-cybercrime-infra-ofac-2025`.
- OFAC Zhdanova #11 → `garantex-ofac-2022`, `grinex-garantex-successor-ofac-2025`, `suex-ofac-2021`, `chatex-ofac-2021`.
- OFAC Houthi al-Jamal #13 → `iran-ransomware-ofac-2018`, `irgc-ransomware-ofac-2022`.
- OFAC Sim Hyon Sop #14 → `lazarus-entity-ofac-2019`, `lazarus-laundering-ofac-2020`, `dprk-usdt-network-ofac-2025`.
