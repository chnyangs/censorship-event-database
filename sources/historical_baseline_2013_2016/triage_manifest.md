# Historical-Baseline 2013-2016 Triage Manifest — Phase B Discovery

- **Generated:** 2026-05-16
- **Frame:** `historical_baseline_2013_2016`
- **Scope window:** 2013-01-01 → 2016-12-31
- **Method:** Agent-enumerated from domain knowledge, cross-checked against `events/*.yaml` and `candidate_triggers/*.yaml`. Each candidate verified via WebSearch against contemporaneous reporting and, where available, primary DOJ / SEC / CFTC / FinCEN / foreign-regulator pages. No automated scraper used.
- **Output state:** Discovery only — no `events/*.yaml` files written.
- **Candidate totals:** 26 total → **P0: 7**, **P1: 16**, **P2: 3** (1 active + 2 deferred)

## Already-present in this tier (13 events)

`china-pboc-crypto-ban-2013-12`, `silk-road-doj-seizure-2013`, `sec-shavers-btcst-2013`, `shrem-faiella-bitcoin-exchange-2014`, `powell-unlicensed-bitcoin-exchange-2014`, `sec-voorhees-satoshidice-2014`, `sec-burnside-bitcoin-stock-exchange-2014`, `nydfs-bitlicense-2015-06`, `ripple-fincen-xrp-2015`, `coinflip-cftc-derivabit-2015`, `teraexchange-cftc-bitcoin-swap-2015`, `bitfinex-cftc-retail-commodity-2016`, `coinbase-irs-john-doe-summons-2016`.

## Exclusion notes

- **Liberty Reserve 2013-05** was previously screened out in `sources/source_frame_triage/us_federal_enforcement_archives.csv` as `rejected_out_of_scope: non-blockchain digital-currency precursor`. Retained here as **P2 / deferred** for parity (it is the dominant non-bitcoin digital-currency takedown of 2013, frequently cited as a contextual precursor to FinCEN MSB enforcement).
- **BTC-e seizure / Vinnik 2017-07** is already coded as `btc-e-doj-2017`; outside scope window.
- **AlphaBay/Hansa 2017-07** is already coded as `alphabay-hansa-doj-2017`.
- **Mt. Gox creditor proceedings** continue 2014-present; the 2014-02-28 civil rehabilitation filing is enumerated as a single bankruptcy-court-mediated event. The 2014-04-16 conversion to bankruptcy and 2014-11-26 Tibanne (parent) bankruptcy filing are noted in the rationale but not re-enumerated as separate candidates.
- **USMS Silk Road BTC auctions** (Jun 2014, Dec 2014, Mar 2015, Nov 2015) are administrative disposal of seized assets, not censorship events; not enumerated.
- **Ross Ulbricht arrest 2013-10-01** is enumerated separately from `silk-road-doj-seizure-2013` (which covers the 2013-10-02 / 2013-10-25 BTC seizures) only because the arrest itself is the load-bearing operator-takedown trigger. If existing `silk-road-doj-seizure-2013` already covers the arrest scope, fold this candidate in rather than admit.
- **Vietnam SBV 2014** has no clean primary-source publication for that year; the explicit SBV prohibition document is Official Letter 5747/NHNN-PC dated 2017-07, outside this tier. Marked **P2 / deferred**.
- **UK HMRC Brief 09/14 (March 2014)** is tax classification (bitcoin = VAT-exempt currency-equivalent) rather than a censorship/access action; included as **P2** because cascade observability is weak.

## P0 candidates (7)

| # | Slug | Actor | Date | Target | Layers | Pri | Rationale |
|---|------|-------|------|--------|--------|-----|-----------|
| 1 | `mtgox-dhs-dwolla-wells-fargo-seizure-2013` | US_DHS_HSI | 2013-05-14 | Mutum Sigillum LLC (Mt. Gox US subsidiary) Dwolla + Wells Fargo accounts | offramp_cex | **P0** | First major US federal action against a bitcoin exchange. $5M seized May-Aug 2013. Predicate for the 2013-06 Mt. Gox USD-withdrawal cascade and the entire FinCEN-MSB enforcement era. |
| 2 | `mtgox-bankruptcy-tokyo-2014` | JP_TOKYO_DISTRICT_COURT | 2014-02-28 | Mt. Gox K.K. — civil rehabilitation 2014 (fu) 3830 | offramp_cex, asset_onchain | **P0** | Largest crypto-exchange collapse of the tier; 850k BTC (~7% of supply) lost. Permanent freeze on all customer USD/BTC withdrawals. Largest cross-border crypto insolvency 2013-2016. |
| 3 | `coin-mx-doj-murgio-2015` | US_DOJ_SDNY | 2015-07-21 | Anthony Murgio + Yuri Lebedev — unlicensed Bitcoin exchange + HOPE FCU takeover | offramp_cex | **P0** | Major post-Shrem SDNY unlicensed-exchange case; >$10M processed via phony "Collectors Club" front + captured federal credit union. Murgio sentenced 5.5 yrs. Distinct from `shrem-faiella-bitcoin-exchange-2014`. |
| 4 | `fincen-virtual-currency-msb-guidance-2013` | US_FINCEN | 2013-03-18 | Class-level: convertible virtual currency exchangers/administrators | offramp_cex | **P0** | FIN-2013-G001 declared VC exchangers/administrators are money transmitters subject to BSA. Foundational US regulatory frame for the entire tier; cited as predicate for nearly every subsequent bitcoin enforcement. Policy-class trigger. |
| 5 | `nydfs-bitlicense-bitfinex-kraken-shapeshift-exit-2015` | US_NYDFS | 2015-08-10 | Bitfinex, Kraken, ShapeShift, Poloniex, BitQuick, BTCGuild, Eobot, Genesis Mining, GoCoin, LocalBitcoins, Paxful — NY geofencing exodus | l4_frontend, offramp_cex | **P0** | L4-frontend cascade of NY-state geofencing across 10+ platforms triggered by 2015-08-10 expiration of BitLicense grace period. Distinct from `nydfs-bitlicense-2015-06` (rulemaking) — this is the platform-exit cascade. |
| 6 | `sec-garza-gaw-miners-zenminer-2015` | US_SEC | 2015-12-01 | Homero Joshua Garza + GAW Miners + ZenMiner — $20M Hashlet cloud-mining Ponzi | offramp_cex, asset_onchain | **P0** | Major 2015 SEC bitcoin-mining securities action (D. Conn. 15-cv-01760). $11M default judgment Jun 2017. Cloud-mining-as-security doctrine case; distinct from Shavers (Ponzi) and Voorhees (unreg offering). |
| 7 | `ulbricht-arrest-fbi-silk-road-2013-10-01` | US_FBI_SF | 2013-10-01 | Ross William Ulbricht (Dread Pirate Roberts) — Silk Road operator arrest | l4_frontend, asset_onchain, offramp_cex | **P0** | Operator-arrest leg of Silk Road takedown distinct from `silk-road-doj-seizure-2013`. 26k BTC initial seizure rolled to 144,336 BTC after laptop forensics. Verify if existing event already covers arrest scope; if so, fold in rather than admit. |

## P1 candidates (16)

| # | Slug | Actor | Date | Target | Layers | Pri | Rationale |
|---|------|-------|------|--------|--------|-----|-----------|
| 8 | `thailand-bot-bitcoin-prohibition-2013` | TH_BOT | 2013-07-29 | Bitcoin Co Ltd Thailand — capital-control framing | offramp_cex, asset_onchain | P1 | First nation-state bitcoin trading prohibition. Silently reversed 2014-02-15. Useful comparable_main precedent for China 2013-12 and the 2014 nation-state wave. `needs_check`: BoT statement was meeting communication, not gazette notice. |
| 9 | `bolivia-bcb-crypto-prohibition-2014` | BO_BCB | 2014-05-06 | All non-state-issued currencies (Bitcoin, Litecoin, Namecoin, etc.) | offramp_cex, asset_onchain | P1 | BCB Resolutivo del Directorio 044/2014: first explicit nation-state crypto-asset prohibition by central-bank resolution. Longest continuous nation-state crypto ban (10 yrs, lifted Jun 2024 by Resolution 082/2024). |
| 10 | `bangladesh-bb-bitcoin-warning-2014` | BD_BB | 2014-09-15 | Bitcoin users — Foreign Exchange Regulation Act 1947 + MLPA 2012 | offramp_cex | P1 | Bangladesh Bank press release widely reported as criminalization with up to 12-yr sentence. Legal scholars dispute criminalization framing (no statutory notification). `needs_check`: BB press-release URL not archived. |
| 11 | `iceland-cbi-foreign-exchange-bitcoin-2014` | IS_CBI | 2014-03-19 | Bitcoin FX trading under 2008 capital-controls regime | offramp_cex | P1 | CBI 2014-03-19: bitcoin trading prohibited under Foreign Exchange Act (FX-control mechanism). De-facto ban via existing FX controls. Lifted 2017 with capital-control easing. Cleanest "collateral censorship via FX controls" precedent. |
| 12 | `russia-cbr-bitcoin-information-letter-2014` | RU_CBR | 2014-01-27 | All RF persons re bitcoin / virtual currencies | offramp_cex | P1 | CBR information letter "On Using Virtual Currencies, Specifically Bitcoin"; cited Art. 27 of Central Bank Law prohibiting monetary surrogates. First Russian-state crypto position; predecessor to 2014-2022 bill cycle. |
| 13 | `indonesia-bi-bitcoin-warning-2014` | ID_BI | 2014-02-06 | Bitcoin and virtual currencies as payment instruments | offramp_cex | P1 | BI first public warning; hardened into 2017 payment-instrument ban and 2019 Bappebti commodity regime. `needs_check` to pin BI archive snapshot. |
| 14 | `argentina-uif-resolution-300-2014` | AR_UIF | 2014-07-04 | AML-obligated entities — bitcoin transaction reporting | offramp_cex | P1 | First Latin American AML reporting regime explicitly naming "monedas virtuales". Predicate for AFIP tax regime (2015-17) and 2024 CNV VASP regime. |
| 15 | `brazil-bcb-comunicado-25306-2014` | BR_BCB | 2014-02-19 | "Moedas virtuais" risk warning to public | offramp_cex | P1 | First BR central-bank statement on bitcoin. Warning-class. Predicate for 2017 Comunicado 31.379 and 2022 Marco Legal das Criptomoedas (Law 14.478/2022). |
| 16 | `eba-virtual-currencies-opinion-eba-op-2014-08` | EU_EBA | 2014-07-04 | EU credit / payment / e-money institutions vs. virtual currencies | offramp_cex | P1 | EBA/Op/2014/08: 70+ risks identified; national supervisors should discourage credit/payment/e-money institutions from VC activity pending comprehensive regime. Foundational European supranational document; predecessor to 5AMLD and MiCA. |
| 17 | `fatf-virtual-currencies-key-definitions-2014` | FATF | 2014-06-26 | Class-level: convertible VC + ML/TF risks | offramp_cex | P1 | First FATF document on virtual currencies; established the ML/TF taxonomy that became 2015 Risk-Based Approach guidance and ultimately R.15 / Travel Rule. Pairs with EBA opinion as the two 2014 supranational frame-setters. |
| 18 | `mtgox-coinlab-civil-2013` | US_WDWA_COURT | 2013-05-02 | Mt. Gox K.K. — breach of Nov 2012 NA exclusivity agreement | offramp_cex | P1 | 2:13-cv-00777 (W.D. Wash.): $75M breach-of-contract suit; CoinLab claim later inflated to $16B in MTGox bankruptcy, freezing creditor distribution. Codes the US-civil track of the Mt. Gox cascade distinct from federal-enforcement and Japanese-bankruptcy tracks. |
| 19 | `mtgox-usd-withdrawal-suspension-2013-06` | MTGOX_OPERATOR | 2013-06-20 | Mt. Gox customers — USD withdrawal freeze | offramp_cex | P1 | 2-week USD-withdrawal suspension caused by Mizuho Bank refusal to process Mt. Gox international wires (downstream from May DHS Dwolla seizure). Cleanest example of federal-action → bank-derisking → operator-freeze chain. Stratum S0_operator_action. |

(Continued)

| # | Slug | Actor | Date | Target | Layers | Pri | Rationale |
|---|------|-------|------|--------|--------|-----|-----------|
| 20 | `karpeles-arrest-tokyo-mtgox-2015` | JP_TMPD | 2015-08-01 | Mark Karpelès — Mt. Gox operator | offramp_cex | P1 | First criminal action against a major-exchange operator in Japan. Operator-takedown leg distinct from bankruptcy and US tracks. Convicted Mar 2019 on one count data manipulation (30 months suspended). |
| 21 | `cryptsy-collapse-vernon-2016` | CRYPTSY_OPERATOR_PRIVATE_CIVIL | 2016-01-13 | Cryptsy customers — operator absconded to China | offramp_cex | P1 | Cryptsy ceased operations citing alleged Jul-2014 cold-storage hack. Vernon fled to China. SD Fla. class action 2016-04: $8.2M judgment. (DOJ indictment unsealed Jan 2022, outside tier.) Cleanest 2016 operator-collapse alongside Bitfinex hack. |
| 22 | `dao-hack-ethereum-hard-fork-2016` | ETHEREUM_FOUNDATION_VITALIK_OPERATORS | 2016-06-17 | The DAO — reentrancy exploit + Ethereum block 1,920,000 hard fork | asset_onchain, l4_frontend | P1 | Ethereum protocol-developer-mediated state rollback. ETH/ETC split 2016-07-20. First major L1-consensus-layer rollback triggered by smart-contract exploit. Directly relevant to L1 censorship layer; censorship by operators, not state. |
| 23 | `bitfinex-hack-august-2016` | BITFINEX_OPERATOR_PRIVATE | 2016-08-02 | Bitfinex multisig + customer balances (~36% bail-in) | offramp_cex, asset_onchain | P1 | 119,756 BTC stolen in ~3 hrs (BitGo multisig key configuration error). Socialized losses across all customers via BFX token. Largest 2016 exchange compromise; first known forced bail-in cascading onto customer balances. |

## P2 / Deferred candidates (1 active + 2 deferred)

| # | Slug | Actor | Date | Target | Pri | Rationale |
|---|------|-------|------|--------|-----|-----------|
| 24 | `uk-hmrc-bitcoin-vat-brief-09-14-2014` | UK_HMRC | 2014-03-03 | UK bitcoin businesses — VAT classification | P2 | HMRC R&C Brief 09/14: bitcoin mining outside VAT scope; bitcoin/sterling exchanges VAT-exempt as currency-equivalent. Tax-classification action, not censorship/access action — cascade observability is weak. Include only if schema admits tax-classification triggers. |
| 25 | `liberty-reserve-doj-takedown-2013` | US_DOJ_SDNY | 2013-05-28 | Liberty Reserve + Arthur Budovsky — Patriot Act §311 action | P2 (**deferred**) | $6B ML scheme, 5.5M users, first Patriot Act §311 application to digital-currency platform. **PREVIOUSLY SCREENED OUT** in `sources/source_frame_triage/us_federal_enforcement_archives.csv` as "non-blockchain digital-currency precursor". Retained as deferred for parity. Recommend maintaining screen-out unless dataset accepts a `precursor_context` admission tier. |
| 26 | `vietnam-sbv-bitcoin-warning-2014` | VN_SBV | 2014-02-27 | Bitcoin as payment instrument | P2 (**deferred**) | Secondary sources reference SBV 2014 press statement, but the explicit SBV prohibition is Official Letter 5747/NHNN-PC dated 2017-07, **outside this tier**. No clean 2014 primary on sbv.gov.vn located. Deferred until 2014 SBV publication is located. |

## Cross-check notes

All 26 slugs verified absent from `events/*.yaml` (109 ids) and from `candidate_triggers/*.yaml` `promoted_event_id` field (20 values). The closest existing ids and the distinctions:

- `mtgox-*` candidates do not overlap with any existing id; the corpus has zero Mt.-Gox-related events despite Mt. Gox being the dominant 2013-14 cascade.
- `coin-mx-doj-murgio-2015` is distinct from `shrem-faiella-bitcoin-exchange-2014` (different operators, different conduit, different fraud scheme).
- `sec-garza-gaw-miners-zenminer-2015` is distinct from `sec-shavers-btcst-2013` (Ponzi) and `sec-voorhees-satoshidice-2014` (unreg offering); Garza is cloud-mining-as-security doctrine.
- `nydfs-bitlicense-bitfinex-kraken-shapeshift-exit-2015` is distinct from `nydfs-bitlicense-2015-06` (rulemaking event); this is the platform-exit cascade.
- `ulbricht-arrest-fbi-silk-road-2013-10-01` is distinct from `silk-road-doj-seizure-2013` (asset-seizure leg); verify whether the existing event already includes the arrest scope.
- `fincen-virtual-currency-msb-guidance-2013` is a policy-class trigger; the existing source_frame_triage previously screened similar policy-class rows. Admit only if schema/sampling frame accepts class-level triggers with downstream observable cascade evidence.

## Recommended verification before promotion (per candidate)

- For Mt. Gox candidates: PACER for the DHS warrants and the W.D. Wash. CoinLab docket; mtgox.com/Tokyo District Court archive for the 2014 (fu) 3830 records.
- For Bolivia / Indonesia / Brazil / Argentina / Vietnam: pin direct primary-language PDF URLs from central-bank archives (bcb.gob.bo, bi.go.id, bcb.gov.br, infoleg.gob.ar, sbv.gov.vn) and capture wayback snapshots.
- For FinCEN MSB guidance: FIN-2013-G001 PDF on fincen.gov is current; capture body hash.
- For NYDFS BitLicense exit cascade: capture each exchange's contemporaneous blog post (Bitfinex, Kraken, ShapeShift) for the L4-frontend cascade evidence; cross-reference with web.archive.org for the NY-state geofence headers.
- For SEC Garza: SEC press release 2015-271 and the D. Conn. complaint PDF on sec.gov are stable.
- For EBA / FATF: EBA opinion PDF and FATF report PDF are stable on the supranational sites.
- For Karpelès arrest: Japanese National Police Agency / Tokyo MPD source for the primary citation.

## Next steps (out of scope for this discovery pass)

- Promote the 7 P0 candidates first; verify the Ulbricht-arrest scope question (fold-in vs. separate event).
- For each P1, complete the `needs_check` items (BCB, BI, BR-BCB, AR-UIF primary URLs; BoT statement format).
- Maintain the screen-out on Liberty Reserve and Vietnam SBV 2014 unless schema accepts a `precursor_context` / `referenced_but_unarchived` admission tier.
