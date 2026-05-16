# Supranational Crypto Censorship Triage Manifest — Phase A.3 Discovery

- **Generated:** 2026-05-16
- **Frame:** `supranational_crypto_censorship_2017_2025`
- **Scope window:** 2017-01-01 → 2025-12-31
- **Stratum:** S6_supranational
- **Method:** Agent-enumerated from domain knowledge of EU OJ publications, FATF plenary outputs, UNSC resolutions, G7 / G20 communiqués, and OECD CARF publications; cross-checked against `events/*.yaml` and `candidate_triggers/*.yaml`. No automated scraper used.
- **Output state:** Discovery only — no `events/*.yaml` files written.
- **Candidate totals:** 17 total → **P0: 7**, **P1: 7**, **P2: 3**

## Already in scope (existing S6 events)

| Slug | Actor | Date | Note |
| --- | --- | --- | --- |
| `eu-mica-2023` | EU_Council | 2023-06-09 | Regulation 2023/1114; CASP/ART/EMT framework |
| `eu-russia-crypto-wallet-cap-2022` | EU_Council | 2022-04-08 | 5th-package Regulation 2022/576; EUR 10K cap |
| `eu-russia-full-crypto-wallet-ban-2022` | EU_Council | 2022-10-06 | 8th-package Regulation 2022/1904; full ban |
| `eu-12th-russia-sanctions-2023` | EU_Council | 2023-12-18 | 12th-package Regulation 2023/2878; Article 5aa extension |

## Exclusion notes

- **EU 1st-4th Russia packages (2014-2015):** pre-scope-window and pre-crypto-explicit (no crypto clauses in 833/2014 until 5th package).
- **EU 6th, 7th Russia packages (2022-06, 2022-07):** no new crypto-specific provisions beyond 5th-package Article 5b; 8th package is the structural pivot.
- **EU 9th-11th Russia packages (Dec 2022 / Feb 2023 / Jun 2023):** extend non-crypto restrictions and tweak Article 5aa wording; no fresh crypto-services pivot. Not enumerated.
- **EU 13th package (Feb 2024):** minor crypto-adjacent text; subsumed under the 14th/15th-package enumerations below.
- **EU Iran sanctions (267/2012 + amendments):** no explicit crypto-services clauses through 2025-12.
- **EU Belarus crypto-services:** mirrors Russia clauses; only the lead Belarus event (2022-03 5th-package analogue) enumerated, as P2.
- **UN DPRK Panel of Experts reports (S/2019/171, S/2020/151, etc.):** reporting documents, not censorship triggers; not enumerated.
- **Council of Europe:** no crypto-specific convention through 2025-12.
- **WTO:** no crypto-services regime statements with censorship effect.
- **G7 statements:** included only as P2 collective-action anchors due to thin observable cascade (non-binding).
- **MiCA secondary legislation (ESMA / EBA / ESAs RTS/ITS Jul-Dec 2024):** enumerated as a single P1 bundle entry to avoid 12-13 per-RTS atomization; per-RTS split is a P3 follow-up if needed.

## Candidate table

| # | Slug | Actor | Trigger | Date | Target | Layers | Load-Bearing | Pri | Rationale |
|---|------|-------|---------|------|--------|--------|--------------|-----|-----------|
| 1 | `fatf-r15-vasp-travel-rule-guidance-2019` | FATF | supranational_regulation | 2019-06-21 | Global VASP ecosystem — R.15 + R.16 (Travel Rule) for VAs | offramp_cex | offramp_cex | **P0** | Foundational global Travel Rule trigger; cited by KR/JP/EU MiCA/UK MLR. Parent of korea-travel-rule-2022; conspicuously absent. |
| 2 | `fatf-targeted-update-va-vasp-2021` | FATF | supranational_regulation | 2021-10-28 | Global VASPs — extended to DeFi developers, stablecoins, P2P/unhosted-wallet treatment | offramp_cex | offramp_cex | **P0** | First FATF guidance extending R.15 to DeFi via the "control or sufficient influence" test; cited by EU MiCA recitals; trigger for 2022-2024 VASP-licensing cascade. |
| 3 | `oecd-carf-crypto-asset-reporting-framework-2022` | OECD | supranational_regulation | 2022-10-10 | Global crypto-reporting ecosystem — CARF automatic tax-info exchange standard | offramp_cex | offramp_cex | **P0** | G20-endorsed binding supranational reporting standard for CASPs; downstream of CRS (2014). EU adopted as DAC8 in 2023-10. Foundational S6 anchor. |
| 4 | `eu-dac8-crypto-asset-reporting-directive-2023` | EU_Council | supranational_regulation | 2023-10-17 | EU CASP ecosystem — Council Directive 2023/2226 (DAC8) | offramp_cex | offramp_cex | **P0** | EU implementation of OECD CARF; applies from 2026-01-01. Tax-reporting axis pairs with MiCA's licensing axis to complete the EU S6 baseline. |
| 5 | `eu-tfr-recast-transfer-of-funds-regulation-2023` | EU_Council | supranational_regulation | 2023-05-31 | EU CASP ecosystem — Regulation 2023/1113 (TFR recast); zero-threshold Travel Rule | offramp_cex | offramp_cex | **P0** | EU Travel Rule companion to MiCA, adopted same legislative package; mandates originator/beneficiary info for every crypto transfer (no threshold) from 2024-12-30. First multi-state binding implementation. |
| 6 | `eu-amla-anti-money-laundering-authority-regulation-2024` | EU_Council | supranational_regulation | 2024-05-30 | EU AML/CFT supervisory ecosystem — Regulation 2024/1620 (AMLA) | offramp_cex | offramp_cex | **P0** | First EU-level AML supervisor with direct (non-NCA-mediated) jurisdiction over high-risk CASPs; Frankfurt-seated; operates 2025-07; direct supervision 2028. Distinct from MiCA. |
| 7 | `eu-amlr-eu-single-rulebook-2024` | EU_Council | supranational_regulation | 2024-05-31 | EU AML/CFT ecosystem — Regulation 2024/1624 (AMLR) single rulebook | offramp_cex | offramp_cex | **P0** | Sets EUR 1,000 CDD threshold for CASP self-hosted-wallet transfers and EUR 10,000 anonymous-payment cap; first binding supranational rules on unhosted-wallet treatment. Applies from 2027-07-10. |
| 8 | `fatf-targeted-update-va-vasp-2023` | FATF | supranational_regulation | 2023-06-27 | Global VASPs — 2023 Targeted Update; 35/151 jurisdictions named as Travel Rule laggards | offramp_cex | offramp_cex | P1 | First public FATF country-level compliance scorecard for crypto; named-and-shamed laggards; directly preceded 2024 implementation wave (CARF, MiCA L2). |
| 9 | `unsc-resolution-2371-dprk-crypto-2017` | UN_SECURITY_COUNCIL | supranational_regulation | 2017-08-05 | DPRK state + DPRK-affiliated actors (precursor framing) | offramp_cex, asset_onchain | offramp_cex | P1 | UNSC 2371 (2017) tightened DPRK sanctions; 1718 Panel of Experts thereafter treats DPRK crypto theft (Lazarus) as 1718-sanctioned activity. Legal substrate for OFAC Lazarus designations + CASP DPRK-screening compliance. Not crypto-explicit in text — P1. |
| 10 | `g20-roadmap-crypto-asset-policy-2023` | G20 | supranational_regulation | 2023-09-09 | G20 member-state crypto regulatory ecosystems — IMF-FSB synthesis paper + New Delhi Declaration | offramp_cex | offramp_cex | P1 | Cleanest G20 collective-action anchor 2017-2025; endorses FSB recommendations + IMF capital-flow guidance + FATF Travel Rule + OECD CARF. Political ceiling for national implementations. |
| 11 | `fsb-crypto-asset-recommendations-2023` | FSB | supranational_regulation | 2023-07-17 | Global crypto-asset + stablecoin issuer ecosystems — FSB CA-R + SC-R recommendations | offramp_cex | offramp_cex | P1 | FSB's first finalized crypto/stablecoin recommendations; G20-endorsed same year; cited by EU MiCA implementation + UK FCA stablecoin rulemaking 2024. Verify FSB actor-enum addition. |
| 12 | `eu-15th-russia-sanctions-2024` | EU_Council | non_us_sanctions | 2024-12-16 | Russian shadow-fleet + sanctions-circumvention CASPs — Regulation 2024/3192 | offramp_cex | offramp_cex | P1 | 15th package; first EU sanctions package adding named crypto-circumvention facilitators under the Russia regime. Supranational analogue to OFAC Garantex/Aeza track. |
| 13 | `eu-14th-russia-sanctions-spfs-2024` | EU_Council | non_us_sanctions | 2024-06-24 | Russian SPFS financial-messaging network + non-EU CASPs using SPFS — Regulation 2024/1739 | offramp_cex | offramp_cex | P1 | 14th package; extraterritorial expansion to non-EU SPFS-using entities; cited by EU CASPs as basis for offboarding third-country counterparts. Crypto-rail-adjacent. |
| 14 | `mica-l2-esma-eba-rts-2024` | EU_ESMA | supranational_regulation | 2024-07-04 | EU CASP ecosystem — ESMA + EBA + EIOPA bundled RTS / ITS under MiCA Titles II-V | offramp_cex | offramp_cex | P1 | MiCA secondary legislation bundle Jul-Dec 2024; operationalizes Level-1. Slot at bundle level (single entry) to avoid 12-13 per-RTS atomization; split is P3 if needed. |
| 15 | `eu-belarus-crypto-services-ban-2022` | EU_Council | non_us_sanctions | 2022-03-09 | Belarus-resident natural / legal persons — Regulation 2022/398 amending 765/2006; EUR 10K cap | offramp_cex | offramp_cex | P2 | Belarus-regime analogue to eu-russia-crypto-wallet-cap-2022. P2 because derivative-mirror; admit only if Belarus-regime granularity is rewarded. |
| 16 | `fatf-grey-list-crypto-related-actions-2023-2024` | FATF | supranational_regulation | 2023-10-27 | FATF grey-listed jurisdictions citing crypto deficiencies (ZA, AE, NG, BG) — Oct-2023 plenary statement | offramp_cex | offramp_cex | P2 | First FATF plenary statements naming crypto-AML deficiencies as load-bearing grey-list reason. P2 because cascade is mediated through national derisking, not direct supranational mandate. |
| 17 | `g7-hiroshima-crypto-statement-2023` | G7 | supranational_regulation | 2023-05-20 | G7 member-state crypto regulatory ecosystems — Hiroshima Leaders' Communiqué | offramp_cex | offramp_cex | P2 | G7 collective endorsement; observable cascade thin (non-binding political commitments). P2 unless dataset benefits from G7-marker distinct from G20-2023. |

## Cross-check notes

- All 17 slugs verified absent from `events/*.yaml` and `candidate_triggers/*.yaml` at generation time.
- Existing in-scope S6 events (`eu-mica-2023`, `eu-russia-crypto-wallet-cap-2022`, `eu-russia-full-crypto-wallet-ban-2022`, `eu-12th-russia-sanctions-2023`) are not re-enumerated.
- `korea-travel-rule-2022` (S4 KR jurisdictional) is the downstream of FATF R.16; the FATF parent (`fatf-r15-vasp-travel-rule-guidance-2019`) is enumerated here as the supranational parent.
- The existing `india-fiu-offshore-vda-block-2023`, `singapore-mas-binance-services-2021`, `nigeria-cbn-crypto-ban-2021`, `turkey-cbrt-crypto-ban-2021` events are S4 jurisdictional, not S6 supranational; they share the FATF-Travel-Rule legal-substrate but the supranational parent is separately enumerated.

## Enum-validation notes

- `actor` values used: `FATF`, `OECD`, `EU_Council`, `EU_ESMA`, `UN_SECURITY_COUNCIL`, `G20`, `G7`, `FSB`. The `FSB` actor is not yet in `controlled_vocab.yaml`; add or migrate to `EU_Council`/`G20` proxy at admission time (preferred: add `FSB` to actor enum; G20 endorses but does not author FSB papers).
- `trigger_type` values used: `supranational_regulation`, `non_us_sanctions` — both present in `controlled_vocab.yaml` line 44-45.
- `jurisdiction` values used: `EU`, `UN`, plus implicit `global` for FATF/OECD/G7/G20/FSB (no `global` enum exists in controlled_vocab.yaml — admission step needs to add or use `[EU, UN]` placeholder + scoped_knowledge note).

## Next steps (out of scope for this discovery pass)

- Promote 7 P0 candidates first (FATF 2019, FATF 2021, OECD CARF 2022, EU DAC8 2023, EU TFR 2023, EU AMLA 2024, EU AMLR 2024). The 4 EU 2023-2024 P0 candidates cluster around the MiCA legislative package and may be reviewed together.
- Resolve the FSB / G20-global enum question with `controlled_vocab.yaml` maintainer before authoring P1 #11.
- Cross-check P2 candidates for derivative-only status before admission.
- For each admitted candidate, follow the existing S6 event-template path established by `eu-mica-2023` and `eu-12th-russia-sanctions-2023`: capture EUR-Lex / FATF / OECD primary HTML, pin body_hash + Wayback, mark L0/L1/L3/asset_onchain as `not_applicable` (construct-not-engaged), carry the load-bearing observation at `offramp_cex`.
