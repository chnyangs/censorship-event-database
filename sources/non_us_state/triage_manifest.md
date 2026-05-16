# Non-US-State Crypto Censorship Triage Manifest — Phase A.4 Discovery

- **Generated:** 2026-05-16
- **Frame:** `non_us_state_crypto_censorship_2017_2025`
- **Scope window:** 2017-01-01 → 2025-12-31
- **Stratum:** `S4_nation_state`
- **Method:** Agent-enumerated from domain knowledge, cross-checked against `events/*.yaml` and `candidate_triggers/*.yaml`. No automated scraper used.
- **Output state:** Discovery only — no `events/*.yaml` files written.
- **Candidate totals:** 25 total → **P0: 12**, **P1: 11**, **P2: 2**
- **Geographic diversity:** 19 distinct countries — AE, AR, AU, BR, CH, DE, FR, HK, ID, IL, IR, JP, KR, RU, SG, TH, TR, UK, ZA

## Existing S4 events (already in corpus — out of scope for this pass)

`india-rbi-crypto-ban-2018`, `china-pboc-crypto-ban-2021`, `china-pboc-crypto-ban-2013-12`, `nigeria-cbn-crypto-ban-2021`, `turkey-cbrt-crypto-ban-2021`, `canada-convoy-freeze-2022`, `korea-travel-rule-2022`, `uk-fca-binance-markets-2021`, `malaysia-sc-binance-disable-2021`, `singapore-mas-binance-services-2021`, `netherlands-dnb-binance-warning-2021`, `belgium-fsma-binance-cease-2023`, `canada-csa-binance-withdrawal-2023`, `philippines-sec-binance-block-2024` (draft), `india-fiu-offshore-vda-block-2023`.

## Exclusion notes

- EU-level supranational instruments (MiCA, 12th sanctions, wallet cap, full crypto-wallet ban) already in corpus and are not S4 nation-state events.
- OFAC and US federal actions covered by `sources/federal_enforcement/triage_manifest` and out of scope here.
- South Korea 2017 ICO ban included (P0) — the FSC verbal announcement on 2017-09-29 was followed by a written press communiqué that is the load-bearing primary anchor.
- Iran 2018 'crypto-banking-prohibition' Central Bank directive included as P1; subsequent IRGC-linked 2024 exchange-seizure rumors held P2 / not enumerated because unverified open-source.
- Russia 2020 'On Digital Financial Assets' law excluded — permits rather than censors crypto issuance. The 2022 CBR consultation paper proposing a full ban is the upstream censorship event included.
- Japan Coincheck 2018 hack is a private breach; the regulatory cascade — FSA 業務改善命令 series 2018-03 / 2018-06 across Coincheck / Quoine / Tech Bureau / Bitstation / others — is the load-bearing S4 event.
- Argentina CNV 2024 PSAV registration enforcement (RG 994/2024) is the primary anchor within the 2017-2025 scope window.
- UK FCA 2024 stablecoin framework consultation (CP24/20) excluded because as of the scope cutoff it is a consultation paper not a binding rule; the 2023 promotion-rule extension (FSMA s.137FBA) is included instead.
- Singapore MAS 2022 retail-crypto restrictions distinct from 2021 Binance warning — included separately (P1) as a cohort-wide rule.
- Hong Kong Bitfinex 2018 SFC cease-and-desist excluded because it lacked ISP / app-store cascade; the 2023 JPEX collapse and 2024 Bybit warning are stronger anchors.

## Candidate table

| # | Slug | Actor | Trigger | Date | Target | Layers | Load-Bearing | Pri | Rationale |
|---|------|-------|---------|------|--------|--------|--------------|-----|-----------|
| 1 | `japan-fsa-coincheck-orders-2018` | JP_FSA | nation_state_block | 2018-03-08 | Coincheck + 7 unregistered JP VC exchanges — FSA 業務改善命令 / 業務停止命令 post-NEM hack | offramp_cex, asset_onchain | offramp_cex | **P0** | First major Asia post-Mt-Gox nation-state exchange supervisory cascade; produced JVCEA self-regulatory consolidation. |
| 2 | `hongkong-sfc-jpex-block-2023` | HK_SFC | nation_state_block | 2023-09-13 | JPEX — SFC warning + HK Police arrests + app-store withdrawal | l4_frontend, offramp_cex | l4_frontend | **P0** | Largest HK retail crypto fraud cascade ($203M+); clean L4 + offramp_cex cascade within 1 week. |
| 3 | `japan-fsa-binance-warning-2018` | JP_FSA | nation_state_block | 2018-03-23 | Binance Holdings — FSA 警告 for unregistered operation under PSA | l4_frontend, offramp_cex | offramp_cex | **P0** | First nation-state regulator action against Binance worldwide; predates UK FCA 2021 by 3 years. Foundational Binance-wave precedent. |
| 4 | `germany-bafin-binance-licence-withdrawal-2023` | DE_BAFIN | nation_state_block | 2023-07-26 | Binance Deutschland — BaFin denial of crypto-custody licence + DE market exit | l4_frontend, offramp_cex | offramp_cex | **P0** | Major EU economy full-market exit 5 months before MiCA effective; pairs with UK/NL/BE Binance events. |
| 5 | `australia-asic-binance-derivatives-2023` | AU_ASIC | nation_state_block | 2023-04-06 | Binance Australia Derivatives — AFSL cancellation + mandatory close-out | offramp_cex | offramp_cex | **P0** | G20-economy derivatives-market exit with clean offramp_cex cascade and Westpac PayID rail severance. |
| 6 | `switzerland-finma-tezos-zg-2018` | CH_FINMA | nation_state_block | 2018-02-16 | Tezos Foundation + ICO issuers (class) — FINMA ICO guidance + tripartite token taxonomy | asset_onchain, offramp_cex | offramp_cex | **P0** | Global tripartite payment/utility/asset-token classification framework; chilled Zug ICO ecosystem. |
| 7 | `russia-cbr-crypto-payment-ban-2022` | RU_CENTRAL_BANK | nation_state_block | 2022-01-20 | RU payment system operators + retail crypto exchanges — CBR consultation proposing full ban | offramp_cex, asset_onchain | offramp_cex | **P0** | CBR proposed full ban 5 weeks before 2022-02-24 invasion of Ukraine; produced VTB/Sberbank/Tinkoff rail-cooling. |
| 8 | `korea-fsc-ico-ban-2017` | KR_FSC | nation_state_block | 2017-09-29 | KR ICO issuers (class) + KR exchanges — FSC blanket ICO prohibition | asset_onchain, offramp_cex | asset_onchain | **P0** | Second nation-state ICO ban worldwide after China 2017-09-04; sibling comparison to existing china-pboc events. |
| 9 | `indonesia-bappebti-illegal-exchange-block-2023` | ID_BAPPEBTI | nation_state_block | 2023-09-21 | 249 named offshore crypto exchanges — BAPPEBTI + Kominfo IP/URL block | l0_network, l4_frontend | l0_network | **P0** | Largest single-batch nation-state crypto domain block worldwide; clean OONI Probe ID measurement opportunity. |
| 10 | `israel-nbctf-hamas-crypto-addresses-2021` | IL_NBCTF | nation_state_block | 2021-07-08 | Hamas-affiliated BTC/USDT/TRX addresses — IL NBCTF TFLA seizure order | asset_onchain | asset_onchain | **P0** | First non-US-OFAC nation-state CTF crypto-address designation regime; direct OFAC-SDN-model comparison. |
| 11 | `japan-fsa-ftx-japan-asset-freeze-2022` | JP_FSA | nation_state_block | 2022-11-10 | FTX Japan + Liquid Japan — FSA 業務改善命令 + asset-segregation freeze | offramp_cex, asset_onchain | offramp_cex | **P0** | Cleanest regulatory-design-driven customer-asset-protection event in FTX collapse; contrast to US Ch.11 track. |
| 12 | `korea-fsc-institutional-restriction-2017` | KR_FSC | nation_state_block | 2017-12-28 | KR exchanges + KR banks (class) — FSC real-name banking mandate | offramp_cex | offramp_cex | **P0** | Foundational KR retail-crypto offramp control event (Upbit/Bithumb/Coinone/Korbit consolidation); precedent before korea-travel-rule-2022. |
| 13 | `thailand-sec-binance-bybit-c-and-d-2021` | TH_SEC | nation_state_block | 2021-07-02 | Binance + Bybit + WorldFanyu + FTX — Thai SEC criminal complaints | l4_frontend, offramp_cex | offramp_cex | P1 | First SEA criminal-track action against offshore exchanges; THB rail severance + binance.com/th geofencing. |
| 14 | `iran-cbi-crypto-banking-prohibition-2018` | IR_CENTRAL_BANK | nation_state_block | 2018-04-22 | IR banks + payment institutions — CBI AML directive cutting IRR crypto rails | offramp_cex | offramp_cex | P1 | Coincident with India RBI 2018-04-06; comparison datapoint for sanctioned-economy crypto-rail severance. |
| 15 | `brazil-bacen-stablecoin-restriction-2023` | BR_BACEN | nation_state_block | 2023-12-13 | BR VASPs (class) — BACEN VASP licensing + USDT/USDC withdrawal restriction | offramp_cex | offramp_cex | P1 | BACEN took over crypto regulation 2023-06; restricted stablecoin self-custody withdrawals at Mercado Bitcoin / Foxbit. |
| 16 | `argentina-cnv-psav-registration-2024` | AR_CNV | nation_state_block | 2024-03-25 | AR PSAV class — CNV RG 994/2024 mandatory registration | offramp_cex | offramp_cex | P1 | Triggered exit of multiple offshore exchanges by 2024-07; top-3 crypto-user-population Latin American economy. |
| 17 | `south-africa-fsca-crypto-financial-product-2022` | ZA_FSCA | nation_state_block | 2022-10-19 | ZA CASPs (class) — FSCA General Notice 1350 declaring crypto as 'financial product' | offramp_cex | offramp_cex | P1 | First African continental nation-state designation; ~50 provisional licences + ~70 rejections by end-2024. |
| 18 | `uae-vara-licence-issuance-regime-2023` | AE_VARA | nation_state_block | 2023-02-07 | Dubai VASPs (class) — VARA 4-Rulebook regime under Law 4/2022 | offramp_cex | offramp_cex | P1 | Forced offshore exchanges to either MVP/full licence or UAE retail exit; first Gulf jurisdiction in corpus. |
| 19 | `france-amf-binance-psan-2022` | FR_AMF | nation_state_block | 2022-05-04 | Binance France SAS — AMF PSAN conditional registration #E2022-031 + 2023 AML probe | offramp_cex | offramp_cex | P1 | Clean longitudinal trajectory through PSAN → 2023 AML probe → MiCA CASP (2024-12-30) multi-stage regulator framework. |
| 20 | `singapore-mas-retail-crypto-restriction-2022` | SG_MAS | nation_state_block | 2022-01-17 | SG licensed/registered DPT providers — MAS retail-marketing & ATM restriction guidelines | l4_frontend, offramp_cex | l4_frontend | P1 | Cohort-wide retail-advertising ban distinct from existing singapore-mas-binance-services-2021 (single-entity). |
| 21 | `hongkong-sfc-bybit-warning-2024` | HK_SFC | nation_state_block | 2024-03-14 | Bybit Fintech Ltd — SFC Notice to Investors warning + app-store removal request | l4_frontend, offramp_cex | l4_frontend | P1 | Largest non-licensed-VATP enforcement under the 2023-06 HK VATP regime; HKD bank-rail severance cascade. |
| 22 | `uk-fca-crypto-promotion-rule-2023` | UK_FCA | nation_state_block | 2023-10-08 | All UK-facing crypto firms (class) — FCA financial-promotion regime extension (FSMA s.137FBA) | l4_frontend, offramp_cex | l4_frontend | P1 | Class-wide UK-geofencing wave (Binance UK retail withdrawal 2023-10-16, PayPal UK suspension 2023-10-01); distinct from 2021 BML event. |
| 23 | `turkey-cmb-casp-licensing-law-7518-2024` | TR_CMB | nation_state_block | 2024-06-26 | Turkish CASPs — Law 7518 amending Capital Markets Law 6362; SPK licensing + stablecoin-payment restriction | offramp_cex | offramp_cex | P1 | Sectoral elaboration of existing turkey-cbrt-crypto-ban-2021; actor is CMB/SPK (capital markets), not CBRT (central bank). |
| 24 | `russia-rosfinmonitoring-binance-russia-rails-2022` | RU_CENTRAL_BANK | nation_state_block | 2022-04-21 | Binance Russia + Advcash + QIWI — CBR / Rosfinmonitoring informal pressure to halt RUB rails | offramp_cex | offramp_cex | P2 | P2: pressure was largely informal (no pinned public order); upstream regulatory trigger to existing binance-russia-exit-commex-2023. |
| 25 | `iran-government-mining-electricity-restriction-2021` | IR_GOVERNMENT | nation_state_block | 2021-05-26 | Crypto-mining operations in Iran — Presidential 4-month ban + Tavanir electricity cutoff | asset_onchain | asset_onchain | P2 | P2: primary anchor is verbal presidential directive (no signed decree pinned); load-bearing CCAF hashrate dataset is third-party. |

## Notes on cross-checks

All 25 slugs verified absent from `events/*.yaml` and `candidate_triggers/*.yaml` at generation time. Where existing event ids are similar in actor (e.g. `uk-fca-binance-markets-2021`, `singapore-mas-binance-services-2021`, `turkey-cbrt-crypto-ban-2021`, `korea-travel-rule-2022`, `binance-russia-exit-commex-2023`), the rationale field documents the distinction (different agency, different date, different doctrine, or cohort vs. single-entity scope).

## Geographic and stratum diversity

- **Asia (8):** `japan-fsa-coincheck-orders-2018`, `japan-fsa-binance-warning-2018`, `japan-fsa-ftx-japan-asset-freeze-2022`, `korea-fsc-ico-ban-2017`, `korea-fsc-institutional-restriction-2017`, `hongkong-sfc-jpex-block-2023`, `hongkong-sfc-bybit-warning-2024`, `singapore-mas-retail-crypto-restriction-2022`, `thailand-sec-binance-bybit-c-and-d-2021`, `indonesia-bappebti-illegal-exchange-block-2023` (10 entries)
- **Europe (5):** `germany-bafin-binance-licence-withdrawal-2023`, `switzerland-finma-tezos-zg-2018`, `france-amf-binance-psan-2022`, `uk-fca-crypto-promotion-rule-2023`
- **MENA / Gulf (4):** `iran-cbi-crypto-banking-prohibition-2018`, `iran-government-mining-electricity-restriction-2021`, `israel-nbctf-hamas-crypto-addresses-2021`, `uae-vara-licence-issuance-regime-2023`, `turkey-cmb-casp-licensing-law-7518-2024` (5)
- **Oceania (1):** `australia-asic-binance-derivatives-2023`
- **LatAm (2):** `brazil-bacen-stablecoin-restriction-2023`, `argentina-cnv-psav-registration-2024`
- **Africa (1):** `south-africa-fsca-crypto-financial-product-2022`
- **Eurasia (2):** `russia-cbr-crypto-payment-ban-2022`, `russia-rosfinmonitoring-binance-russia-rails-2022`

## Next steps (out of scope for this discovery pass)

- Promote 12 P0 candidates first; verify the 2 P2 items (RU informal pressure pinpoint, IR mining verbal directive).
- For each admitted candidate, follow the existing event-template path: capture canonical citation HTML / PDF, attach OONI L0 query where applicable (especially ID-249-block and HK-JPEX-block events), search Wayback for L4 diffs (app-store regional-availability for HK / ID / IN events), attach chain-analytics anchors at `asset_onchain` for IL-NBCTF address designations and IR mining hashrate impact.
