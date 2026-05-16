# Pre-Bitcoin Baseline 2008-2012 Triage Manifest — Phase E Discovery

- **Generated:** 2026-05-16
- **Frame:** `pre_bitcoin_baseline_2008_2012`
- **Scope window:** 2007-04-01 → 2012-12-31 (with note on the 2007-04-27 e-Gold indictment lower-bound edge case)
- **Temporal tier target:** `discovery_only_2008_2012`
- **Analysis use target:** `discovery_only`
- **Method:** Agent-enumerated from domain knowledge, cross-checked against 146 admitted event ids and `candidate_triggers/*.yaml`. Each candidate verified via WebSearch against contemporaneous Reuters / AP / Bloomberg / Al Jazeera / CNN / TechCrunch / Wired reporting, primary DOJ / FinCEN / Treasury press releases, and the WikiLeaks Banking-Blockade archive (`wikileaks.org/Banking-Blockade.html`).
- **Output state:** Discovery only — no `events/*.yaml` written.
- **Candidate totals:** 22 total → **P0: 10**, **P1: 7**, **P2: 5** (2 active + 3 deferred).

## Already-present in this tier

**Zero events.** No event in the 146-id corpus carries a trigger date in 2008-01-01 → 2012-12-31. The closest related ids are post-tier: `mtgox-*-2013/2014`, `shrem-faiella-bitcoin-exchange-2014`, `silk-road-doj-seizure-2013`, `btc-e-doj-2017`. Phase E is purely additive for the pre-Bitcoin baseline.

## Exclusion notes

- **DigiCash / E-Cash (1999 era)** is outside tier by ~9 years; the conceptual successor is Liberty Reserve, captured here.
- **Pecunix winding-down 2008-2011** — only the 2008 bullion transfer is locatable, and it is an internal corporate move, not a regulator-side trigger. Marked P2 / `needs_check`.
- **GoldMoney KYC tightening 2008-2010** has no contemporaneous primary regulator filing — corporate-blog and customer-review trails only. **NOT enumerated.**
- **Liberty Reserve §311 designation 2013-05-28 + DOJ takedown** are **outside this tier** (post-2012). The endpoint of the 2009-2012 Liberty Reserve trajectory should be carried in the `historical_baseline_2013_2016` tier, where it is already noted as P2 / deferred. The in-tier anchor for Liberty Reserve here is the **2011-03 SUGEF license denial + criminal investigation**.
- **Silk Road pre-arrest 2011-2012 LE attention** is documented only via post-hoc DOJ filings (Ulbricht complaint Sep 2013); no contemporaneous 2011-2012 enforcement publication exists. Not enumerated separately.
- **Iran-sanctions / DPRK-sanctions 2008-2011 financial-system actions** are broad sanctions-policy actions outside this dataset's chain-censorship scope, except for the 2012 SWIFT disconnection (kept as P2 deferred for cross-domain comparator value only).
- **Operation Payback DDoS retaliation against Visa / MasterCard / PostFinance / Amazon (2010-12-08 onward)** is a third-party cyber response to the blockade, not a censorship action itself. Documented in context but not enumerated.

## Stratum terminology note

Existing corpus uses `S1_ofac_sdn`, `S3_doj_sec_cftc_fiod`, `S4_nation_state`, `S5_corporate`. Mapping for the pre-Bitcoin baseline:

- **Corporate financial-intermediary actions** (PayPal, Visa Europe, MasterCard, Bank of America, Western Union, PostFinance, Amazon AWS, EveryDNS) → `S5_corporate`
- **DOJ / Secret Service criminal actions** (e-Gold 2007/2008, e-Bullion 2008) → `S3_doj_sec_cftc_fiod`
- **FBI intelligence assessments** (April 2012 Bitcoin assessment) → `S3_doj_sec_cftc_fiod` (policy/intelligence class)
- **Iceland court rulings on the blockade** (Reykjavik District Court 2012, Supreme Court 2013) → `S4_nation_state` (judicial sub-stratum)
- **Mt. Gox 2011 hack / Bitcoinica 2012** are operator-self-inflicted compromises → treat as `S5_corporate` operator-collapse precedents alongside the 2016 Bitfinex / Cryptsy cases already in corpus.

## P0 candidates (10)

| # | Slug | Actor | Date | Target | Layers | Pri | Rationale |
|---|------|-------|------|--------|--------|-----|-----------|
| 1 | `wikileaks-paypal-freeze-2010-12` | PAYPAL_OPERATOR | 2010-12-04 | Wau-Holland-Stiftung WikiLeaks donations account | offramp_cex, l4_frontend | **P0** | Foundational corporate payment-censorship event. Notice 2010-12-03, public effect 2010-12-04. PayPal VP Osama Bedier publicly named the State Department as cited cause at LeWeb Paris 2010-12-08. Most paper-impactful pre-Bitcoin baseline event. |
| 2 | `wikileaks-mastercard-suspension-2010-12` | MASTERCARD_OPERATOR | 2010-12-06 | WikiLeaks donations via MasterCard rails | offramp_cex, l4_frontend | **P0** | Card-network leg of blockade. Triggered Operation Payback DDoS. No specific statutory violation cited. |
| 3 | `wikileaks-visa-europe-suspension-2010-12` | VISA_EUROPE_OPERATOR | 2010-12-07 | DataCell ehf merchant agreement (Teller A/S + Korta hf.) | offramp_cex, l4_frontend | **P0** | Visa leg of card-network blockade. Direct trigger for the DataCell v. Valitor litigation 2012-2013 (P0). 95% revenue drop for WikiLeaks per Assange Oct 2011 statement. |
| 4 | `wikileaks-bank-of-america-block-2010-12` | BANK_OF_AMERICA_OPERATOR | 2010-12-18 | WikiLeaks-related transactions on BoA rails | offramp_cex | **P0** | Only US-domiciled commercial-bank leg of the blockade. BoA "reasonable belief" language; later context for the HBGary/BoA leak-strategy memos 2011. |
| 5 | `wikileaks-western-union-interdiction-2010-12` | WESTERN_UNION_OPERATOR | 2010-12-21 | WikiLeaks remittance recipients | offramp_cex | **P0** | Remittance-network leg of blockade. **`needs_check`**: WU never issued contemporaneous press statement; documented only via internal Interdiction-List leaks + WikiLeaks archive. Admit with `evidence_use: contextual_unarchived`. |
| 6 | `wikileaks-postfinance-account-closure-2010-12` | SWISSPOST_POSTFINANCE_OPERATOR | 2010-12-06 | Julian Assange / WikiLeaks Defence Fund Swiss account | offramp_cex | **P0** | Only European-state-postal-banking leg of blockade. Cited "false residency" rationale. Triggered Operation Payback DDoS against postfinance.ch same day. |
| 7 | `wikileaks-amazon-aws-eviction-2010-12` | AMAZON_AWS_OPERATOR | 2010-12-01 | WikiLeaks hosting on AWS | l4_frontend | **P0** | Hosting / L4-infrastructure leg of blockade. Lieberman office staff inquiry was cited cause. EFF "weakest intermediary" framing — paper-impactful precedent for 2022 Cloudflare / Infura actions already in corpus. |
| 8 | `wikileaks-everydns-domain-termination-2010-12` | EVERYDNS_OPERATOR | 2010-12-02 | wikileaks.org + wikileaks.ch DNS resolution | l4_frontend | **P0** | DNS-resolver leg of blockade. Arguably the strongest L0/L1-infrastructure-layer precedent in 2008-2012 for the 2022 Cloudflare-Tornado and Infura-Donetsk events. |
| 9 | `egold-doj-guilty-plea-2008-07` | US_DOJ_DC | 2008-07-21 | e-Gold Ltd. + Gold & Silver Reserve Inc. + Douglas Jackson + Reid Jackson + Barry Downey | offramp_cex | **P0** | Foundational pre-Bitcoin digital-currency takedown. Most-cited 2007-2008 precedent for FinCEN MSB framework later applied to bitcoin. |
| 10 | `datacell-v-valitor-iceland-district-court-2012-07` | IS_REYKJAVIK_DISTRICT_COURT | 2012-07-12 | Valitor hf. (Visa Iceland) Datacell credit-card gateway | offramp_cex, l4_frontend | **P0** | First judicial finding worldwide that a card-network WikiLeaks blockade was unlawful. Daily fine ordered. Supreme Court affirmation 2013-04 (P2 deferred). |

## P1 candidates (7)

| # | Slug | Actor | Date | Target | Layers | Pri | Rationale |
|---|------|-------|------|--------|--------|-----|-----------|
| 11 | `egold-secret-service-indictment-2007-04` | US_DOJ_DC | 2007-04-27 | e-Gold Ltd. + GSR + Jackson/Downey | offramp_cex | P1 | Four-count federal indictment unsealed 2007-04-27. 8 months outside strict 2008 lower bound — admit with admission_tier=precursor or reference from the 2008-07-21 plea (P0) via `related_events`. **`needs_check`**: scope-window edge case. |
| 12 | `ebullion-doj-fbi-seizure-2008-08` | US_DOJ_CDCA | 2008-08-01 | Goldfinger Coin and Bullion / e-Bullion / James Fayed | offramp_cex | P1 | DOJ/FBI seized e-Bullion assets August 2008 after Pamela Fayed murder. ~1M users, ~50k oz gold reserves. **`needs_check`**: pin original 2008 seizure warrant via PACER for body_hash. |
| 13 | `mtgox-june-2011-hack-trading-suspension` | MTGOX_OPERATOR | 2011-06-19 | Mt. Gox customers — multi-week trading freeze | offramp_cex, asset_onchain | P1 | $17.50 → $0.01 flash crash, 25k BTC stolen, exchange offline through August. First major bitcoin-exchange compromise + operator-imposed access freeze. Stratum-S0 / operator-action precedent. |
| 14 | `bitcoinica-shutdown-2012-05` | BITCOINICA_OPERATOR | 2012-05-11 | Bitcoinica customers — 18,547 BTC hot-wallet theft | offramp_cex, asset_onchain | P1 | First major margin-trading bitcoin platform collapse. Companion 2012-03 Linode loss (43,554 BTC) and 2012-07 Mt. Gox account hijack (40,000 BTC). Deregistered November 2012. Mt. Gox 2014 creditor claimant. |
| 15 | `fbi-bitcoin-intelligence-assessment-2012-04` | US_FBI | 2012-04-24 | Class-level: bitcoin economy ($35-44M, 8.8M BTC) | offramp_cex | P1 | First FBI intelligence-class document on Bitcoin. Predates FIN-2013-G001 by ~11 months. Policy/intelligence-class trigger — admit only if schema accepts such triggers. |
| 16 | `liberty-reserve-costa-rica-license-denial-2011-03` | CR_SUGEF | 2011-03-07 | Liberty Reserve S.A. — money-transmitter license + criminal investigation | offramp_cex | P1 | In-tier anchor for the Liberty Reserve trajectory. SUGEF refused license citing "lack of transparency about how the business was funded"; criminal investigation opened. Continues operating via 5 shell companies. 2013-05-28 §311 designation is post-tier endpoint. |
| 17 | `wikileaks-wau-holland-tax-status-challenge-2010-12` | DE_FA_KASSEL | 2010-12-15 | Wau-Holland-Stiftung charitable / tax-exempt status | offramp_cex | P1 | Only nation-state-tax-authority leg of the WikiLeaks blockade. Charitable status partially restored ~2 years later, but explicitly NOT for 2010. Documented by WHS and Wikipedia. |

## P2 / Deferred candidates (5)

| # | Slug | Actor | Date | Target | Pri | Rationale |
|---|------|-------|------|--------|-----|-----------|
| 18 | `bitinstant-operations-launch-2011-09` | BITINSTANT_OPERATOR | 2011-09-01 | BitInstant launch (Shrem + Nelson) | P2 (**deferred**) | Operator-formation precedent for 2014-01-26 Shrem arrest (`shrem-faiella-bitcoin-exchange-2014`). Not a censorship event. Include only as background context in the existing 2014 event's `related_events`. |
| 19 | `datacell-v-valitor-iceland-supreme-court-2013-04` | IS_SUPREME_COURT | 2013-04-24 | Affirms Visa-WikiLeaks blockade unlawful | P2 (**deferred**) | **OUTSIDE strict 2008-2012 tier.** Either admit to `historical_baseline_2013_2016` alongside the 2012-07 District Court ruling (P0), or admit here with admission_tier=precursor_endpoint. |
| 20 | `swift-eu-iran-bank-disconnection-2012-03` | EU_COUNCIL_PLUS_SWIFT_OPERATOR | 2012-03-17 | ~30 Iranian banks incl. Central Bank of Iran | P2 (**deferred**) | Useful non-crypto financial-censorship comparator. Out of scope for direct admission — sanctions-policy action with zero chain-layer cascade. Cite in literature-review / discussion sections rather than as an admitted event. |
| 21 | `pecunix-bullion-transfer-2008` | PECUNIX_OPERATOR | 2008-06-01 | Pecunix gold bullion (Mat Securitas Express AG, Zurich) | P2 (**`needs_check`**) | Internal corporate move framed as regulatory-arbitrage response. No regulator action, no contemporaneous news pin. Useful only as discussion context for post-e-Gold DGC exodus. |
| 22 | `mtgox-mizuho-wire-pressure-2012` | JP_MIZUHO_BANK_OPERATOR | 2012-12-01 | Mt. Gox correspondent account | P2 (**`needs_check`**) | Documented retrospectively only (Wired Nov 2013, class-action 2016+). In-tier predicate for the 2013-06 USD-withdrawal suspension already in corpus. No contemporaneous 2012 Mizuho or Mt. Gox disclosure. |

## Cross-check notes

All 22 slugs verified absent from `events/*.yaml` (146 ids) and from `candidate_triggers/*.yaml` `promoted_event_id`. Zero collisions because the corpus has zero 2008-2012 trigger dates.

Close-by ids that should appear in `related_events` when these candidates are eventually promoted:
- `wikileaks-*-2010-12` → `tornado-cash-ofac-2022`, `infura-metamask-donetsk-luhansk-block-2022-03`, `cloudflare-ethereum-gateway-tornado-block-2022-08`, `circle-usdc-tornado-2022` (all of which are direct conceptual descendants of the WikiLeaks blockade as L4/L5 corporate-intermediary censorship).
- `egold-*-2007/2008` → `fincen-virtual-currency-msb-guidance-2013`, `shrem-faiella-bitcoin-exchange-2014`, `liberty-reserve-doj-takedown-2013` (post-tier P2 deferred candidate).
- `mtgox-june-2011-hack-trading-suspension`, `mtgox-mizuho-wire-pressure-2012` → `mtgox-dhs-dwolla-wells-fargo-seizure-2013`, `mtgox-usd-withdrawal-suspension-2013-06`, `mtgox-bankruptcy-tokyo-2014`, `karpeles-arrest-tokyo-mtgox-2015`.
- `liberty-reserve-costa-rica-license-denial-2011-03` → `liberty-reserve-doj-takedown-2013` (post-tier P2 deferred in historical_baseline_2013_2016).

## Recommended verification before promotion (per candidate)

- **WikiLeaks blockade (PayPal, MasterCard, Visa Europe, BoA, Western Union, PostFinance, Amazon, EveryDNS)**: capture Wayback snapshots for all primary URLs; cross-reference WikiLeaks Banking-Blockade archive (which is itself archived) with Bloomberg / Reuters / AP / Al Jazeera same-day reporting. For PayPal specifically, capture the TechCrunch interview with Osama Bedier (LeWeb Paris 2010-12-08) where State Department citation was made on-record.
- **e-Gold 2008-07 plea and 2007-04 indictment**: DOJ press releases are stable on justice.gov archive. Pull PACER for the original D.D.C. indictment + plea agreement docket. USSS Orlando press release is on secretservice.gov.
- **e-Bullion 2008-08 seizure**: pin original warrant via PACER (C.D. Cal.). Primary DOJ press releases are 2014/2015/2019 asset-return announcements, not the original seizure — the 2008 seizure body_hash must come from PACER.
- **DataCell v. Valitor 2012-07 / 2013-04**: Reykjavik District Court + Supreme Court of Iceland records on https://www.haestirettur.is and https://landsrettur.is. Bloomberg, Iceland Grapevine, and The Register all have stable coverage.
- **FBI 2012-04 Bitcoin assessment**: primary PDF is the leaked one (justsecurity.org and uproxx.com mirrors); body_hash can be pinned from any mirror.
- **Mt. Gox 2011 hack**: bitcoin.it/wiki "Mt. Gox/Stolen Bitcoins" and BitMEX retrospective are the cleanest secondary sources. Primary is the Mt. Gox blog post from 2011-06 (need Wayback snapshot).
- **Bitcoinica 2012**: Bitcoin Magazine 2012-08-02 Tihan Seale liquidation announcement is primary; pin Wayback.
- **Liberty Reserve Costa Rica 2011**: Tico Times 2013-05-27 retrospective and La República archive are the most-detailed; primary SUGEF resolution may not be public.
- **Wau-Holland-Stiftung tax challenge 2010-12**: wauland.de/en project page is primary corporate record; Wikipedia and Dawn columns are secondary.

## Top 5 paper-impactful events (recommendation)

For the academic-literature anchor that motivates this entire tier, prioritize promoting these 5 first:

1. **`wikileaks-paypal-freeze-2010-12`** — single most-cited corporate payment-censorship event in the academic literature.
2. **`wikileaks-mastercard-suspension-2010-12`** + **`wikileaks-visa-europe-suspension-2010-12`** — card-network legs; the Pasquale / Lessig / Zittrain literature is built on these two.
3. **`egold-doj-guilty-plea-2008-07`** — foundational pre-Bitcoin digital-currency takedown predating FIN-2013-G001 by ~5 years.
4. **`datacell-v-valitor-iceland-district-court-2012-07`** — first judicial restraint of a card-network blockade; the closing-bookend of the WikiLeaks blockade case study.
5. **`wikileaks-amazon-aws-eviction-2010-12`** + **`wikileaks-everydns-domain-termination-2010-12`** — L4-frontend / L0-DNS infrastructure layers; the direct conceptual ancestors of the 2022 Cloudflare-Tornado and Infura-Donetsk events already in corpus.

## Next steps (out of scope for this discovery pass)

- Promote the 10 P0 candidates first; resolve the scope-window edge case for `egold-secret-service-indictment-2007-04` (admit-as-precursor vs. fold into `egold-doj-guilty-plea-2008-07` via `related_events`).
- Decide whether `datacell-v-valitor-iceland-supreme-court-2013-04` belongs in this tier (as endpoint) or in `historical_baseline_2013_2016` (as in-tier event).
- For each P1, complete the `needs_check` items: e-Bullion 2008 warrant PACER pull, Mt. Gox June-2011 blog Wayback snapshot, FBI 2012-04 PDF body_hash, Wau-Holland-Stiftung FA Kassel correspondence.
- Maintain the screen-out on Pecunix bullion transfer, GoldMoney KYC tightening, and broader Iran/DPRK sanctions (except as discussion-section comparators).
