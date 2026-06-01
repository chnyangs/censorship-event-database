# 📍 State of the corpus — 2026-05-31 (continuation snapshot)

**Authoritative current snapshot.** Supersedes `MORNING_REVIEW_2026_05_31.md` (which is now stale at 259).
Detailed tick-by-tick log: `analysis/overnight_collection_notes_2026_05_31.md`.

## Headline
- **405 events**: **365 admitted** / 30 draft / 10 rejected.
- **Integrity**: `scripts/validate.py` passes **405 / 405 [OK]**; `make check` passes. All changes remain local, never pushed.
- **This session continuation delivered +104 net admitted** (corpus 261 → 365), plus codebook **4.0.0** (`evidence_tier`).

### 2026-06-01 quality-loop addendum
- `analysis/review-report.*` now scores observation reliability and direct
  attribution against **claim-usable evidence** only: replayable sources whose `evidence_use` is not
  `contextual_unarchived` or `non_admission`.
- Under that stricter operational review, release-ready cases are **276** (11 complete / 265 scoped) and
  admitted-but-blocked cases are **89**. This is a deliberate paper-risk surfacing change, not a corpus
  shrink: low/medium cases remain in the dataset, but their paper use is now more visibly gated until the
  underlying source rows are upgraded or narrowed.
- Current admitted-case reliability distribution after the stricter pass and subsequent quality-loop repairs:
  observation reliability **287 high / 78 medium / 0 low**; attribution reliability
  **245 high / 120 medium / 0 low**. Current admitted paper roles are
  **264 aggregate_datapoint / 97 null_control / 1 appendix_only / 3 paper_anchor**.
  Paper-anchor promotion is now gated on release readiness: blocked `anchor_case` rows remain admitted but are
  reported as `appendix_only` until their blockers are cleared.
- Latest automated repairs: `sec-shavers-btcst-2013` now has local SEC complaint and press-release
  `body_hash` / `body_path` replay anchors, and its scoped claim is narrowed to the SEC civil filing and
  relief sought rather than an unanchored post-filing receivership timeline. `sec-v-telegram-ton-2020`
  now replaces stale SEC 2020-69 / telegram.org pointers with SDNY Document 227, SEC 2020-146, and Pavel
  Durov's Telegraph termination post. `bitfinex-cftc-retail-commodity-2016` now has local CFTC press-release
  and administrative-order replay anchors, and its scoped claim is narrowed from a specific mandated
  actual-delivery model transition to the order-supported actual-delivery violation finding, penalty,
  cease-and-desist, and recorded business-practice changes. `bitfinex-tether-cftc-2021` now has local CFTC
  press-release plus both CFTC order PDFs pinned; its Tether-side claim is narrowed from a CFTC-created
  quarterly-reporting regime to the order-supported reserve-misrepresentation penalty, cease-and-desist, and
  recorded remediation posture. `coinflip-cftc-derivabit-2015` now has local CFTC press-release and
  administrative-order replay anchors, and its scoped claim is narrowed from an independently verified
  Derivabit frontend shutdown to the order-supported unregistered Bitcoin-options facility finding,
  commodity-classification holding, and cease-and-desist / operator-state observation.
  `sec-burnside-bitcoin-stock-exchange-2014` now has local SEC newsroom press-release and corrected
  Administrative Proceeding Order 33-9685 PDF replay anchors; its claim is narrowed to the order-supported
  Commission-staff-triggered website/trading winddown and 2014 settlement remedies.
  `eu-russia-crypto-wallet-cap-2022` and `eu-russia-full-crypto-wallet-ban-2022` now have local EUR-Lex
  replay anchors for Regulations 2022/576 and 2022/1904, and both rows are narrowed from unpinned named-CASP
  implementation claims to the source-supported EU CASP custody/account legal obligations.
  `eba-virtual-currencies-opinion-eba-op-2014-08` now has the official EBA Opinion PDF pinned locally and is
  narrowed to the EBA supervisory recommendation itself, not unenumerated downstream banking de-risking.
  `canada-csa-binance-withdrawal-2023` now has the OSC-hosted CSA Staff Notice 21-332 PDF and official Binance
  X announcement pinned locally, and is narrowed from an unpinned 2-layer Binance.com/CAD-rail claim to a
  replayable single-layer Binance Canada marketplace-withdrawal observation.
  `uk-fca-binance-markets-2021` now has the FCA consumer-warning page and First Supervisory Notice PDF pinned
  locally, and is narrowed from an unpinned bank-payment-rail cascade to the FCA-supported BML regulated-business
  restriction plus required notice / promotion-removal compliance.
  `germany-bafin-binance-licence-withdrawal-2023` now has BaFin crypto-custody guidance plus PYMNTS and
  Reuters-syndicated reports pinned locally, is explicitly `evidence_tier=attested_secondary`, and is narrowed
  from an unpinned BaFin/Binance/L4 claim to the reported Binance Germany licence-application withdrawal under
  the BaFin/KWG regime.
  `japan-fsa-coincheck-orders-2018` now has Kanto Local Finance Bureau disposition pages plus Coincheck
  staged-service-restoration notices pinned locally, and is narrowed from an overclaimed Coincheck
  business-suspension / regulator-ordered freeze narrative to the source-supported business-improvement-order
  and remediation-gated withdrawal/sale restoration path.
  `korea-fsc-ico-ban-2017` now has the official FSC 2017-09-29 Korean press-release PDF pinned locally and is
  narrowed from a drifted English index plus unpinned exchange-frontend cascade to the source-supported ICO /
  credit-extension prohibition itself.
  `binance-us-staking-end-2023` is now rejected as an unsupported false-positive / duplicate-scope row: the
  replayable Binance.US and Guardian anchors support the SEC-v-Binance platform/off-ramp reaction already
  admitted in `sec-v-binance-2023`, not a standalone 2023-06-09 Binance.US all-staking shutdown.
  `kraken-sec-unregistered-exchange-2023` now has local SEC and Kraken replay anchors and is recoded from a
  positive empirical observed-change row to a null-control no-service-withdrawal comparator for the November
  2023 SEC unregistered-exchange complaint.
  `sec-v-ripple-2020` now has local SEC, Coinbase, and Bitstamp replay anchors and is narrowed from a broad
  two-layer/four-exchange cascade to the source-supported Coinbase/Bitstamp CEX/off-ramp comparison; the
  previously unanchored Ripple.com L4, Binance.US, and Kraken observations are no longer load-bearing.
  `binance-russia-exit-commex-2023` now has a local PRNewswire/Binance release replay anchor and is narrowed
  from an unpinned Binance/CommEX L4 plus RUB-rails cascade to the source-supported Binance Russia-market
  sale, user off-boarding, CommEX migration, and exchange-service sunset observation.
  `binance-privacy-coin-delisting-2023` is now narrowed from an unverified Binance support pointer and
  inaccurate eight-asset cohort to the final five-asset EU4 restriction cohort supported by local Wayback
  captures of contemporaneous The Block / Blockworks reporting; it is explicitly `evidence_tier=attested_secondary`
  and remains blocked only for a missing replayable first-party Binance notice.
  `singapore-mas-binance-services-2021` now replaces generic MAS news-index citations with a replayable
  2021-09-02 CNA trigger report plus first-party Binance Wayback captures for the 2021-09-05 SGD/app-store
  restriction announcement and the 2021-09-27 regulated-payment-services restriction announcement. The row is
  narrowed away from the unpinned 2022 binance.sg exit cascade, is explicitly `evidence_tier=attested_secondary`,
  and remains blocked only for a missing replayable official MAS primary trigger artifact.
  `malaysia-sc-binance-disable-2021` now replaces generic SC media-index citations with pinned SC media-release
  and administrative-actions captures plus a 2021 Wayback capture of Binance's Malaysia product-restriction
  support announcement. The row is release-ready scoped and narrowed to the SC website/app/messaging disable
  directive plus Binance-announced MYR product restrictions, with no broader bank-rail or live-URL-only claim.
  `netherlands-dnb-binance-warning-2021` now replaces generic DNB homepage / contextual Wayback patterns with
  pinned official DNB warning, enforcement-page, and fine-decision PDF captures. The row is recoded as
  `regulatory_enforcement`, narrowed to DNB's warning/fine for unregistered Binance exchange and custody
  services in the Netherlands, and no longer carries the unpinned 2022/2023 market-exit cascade already modeled
  by `binance-netherlands-exit-2023-07`.
  `opensea-iran-cuba-sanctions-block-2022` now replaces its generic OpenSea blog / wildcard Wayback scaffold
  with dated 2022 OpenSea TOS Wayback captures plus local Decrypt, Artnet, and Washington Times/AP Cuba
  reporting captures. The Cuba row is relabeled `plausible`, the event is explicitly
  `evidence_tier=attested_secondary`, and the case moves from appendix-only / blocked to release-ready scoped
  aggregate use while staying filterable for strict evidence-tier analyses.
  `ftx-bankman-fried-doj-2022` now replaces contextual DOJ/SEC/CFTC/FTX pointers with local DOJ indictment PDF,
  SEC, CFTC, and FTX-sourced PRNewswire replay anchors, and is recoded from a positive empirical_case to a
  release-ready null_control: the 2022-12-13 DOJ indictment is preserved as the trigger, but the FTX off-ramp
  freeze is treated as already in place under the 2022-11-11 Chapter 11 estate rather than as a new
  DOJ-attributable observed_change.
  Table 6 now applies the same claim-usable evidence rule as `analysis/review-report.*`: null-denominator
  anchors ignore sources marked `contextual_unarchived` or `non_admission`. Under that stricter rule,
  `ens-eth-domain-tornado-resolution-2022` is demoted back to a draft candidate because its retained ENS
  app / eth.limo bodies are current-state scoping artifacts, not claim-usable 2022 no-change evidence. It
  can be reconsidered only after timestamped 2022 Wayback or equivalent ENS governance/operator evidence is
  pinned and human re-admission happens.
  The admitted low-observation queue is now cleared: `mtgox-dhs-dwolla-wells-fargo-seizure-2013` has a
  replayable primary-legal warrant copy; `oecd-carf-2022` has a replayable official OECD CARF standards PDF;
  `voyager-bankruptcy-doj-objection-2023` is explicitly `evidence_tier=attested_secondary` with attribution
  narrowed from direct to plausible; and `tornado-cash-storm-conviction-2025` is demoted to draft because the
  retained chilling-effect observation lacks a concrete operator/repository/on-chain artifact.
  The latest primary-trigger repairs pin official Bybit and Paxos Canada-withdrawal notices, Coinbase's
  official MiCA non-compliant stablecoin help article, Uniswap Labs' first-party early-access post for the
  Apple App Store rejection, the ShapeShift-authored Medium mirror of Erik Voorhees' original ShapeShift
  Membership announcement, and the official Binance Support mirror for the 2024 global XMR delisting.
  Bybit/Paxos are upgraded out of `attested_secondary`; Coinbase moves from blocked to release-ready scoped
  with trigger/observation/attribution all high; Uniswap Wallet moves from blocked to release-ready scoped with
  trigger/observation high while attribution stays plausible because Apple gave no public rationale; ShapeShift
  moves from blocked to release-ready scoped with trigger/observation/attribution all high while preserving the
  no-named-enforcement-action rationale as contextual; Binance Monero moves from blocked to release-ready
  scoped with trigger/observation/attribution all high after using `binance.info` as a replayable official
  mirror because `binance.com` returned a WAF challenge on this network path. The CSA/OSC, MiCA,
  app-store-review, regulatory-environment, and privacy-coin/regulatory rationales remain scoped to the
  source-supported policy actions, with trade-press mementos retained only as corroboration where relevant.
  The next primary/source repair batch moves three more rows out of the blocked queue:
  `ecuador-national-assembly-bitcoin-ban-2014-07` now cites the official COMF PDF at trigger level while
  preserving plausible attribution for the bitcoin-specific legal interpretation; `russia-dfa-law-2020` now
  cites a replayable Russian Prosecutor General Office mirror page plus its image-based 259-FZ PDF after the
  `publication.pravo.gov.ru` live endpoint timed out from this network; and
  `bittrex-privacy-coin-delisting-2021-01` now cites the official Bittrex Global Zendesk notice and uses
  direct attribution for the market-removal action while leaving the AML/KYC/regulatory rationale contextual.
  The latest continuation repair pins three more government primary-trigger anchors:
  `russia-mining-legalization-law-2024-08` now uses a replayable Rosfinmonitoring release for Federal Law
  No. 221-FZ after live Kremlin/pravo endpoints timed out from this network; `uae-sca-crypto-asset-activities-regulation-decision-23-2020`
  now uses the official SCA 2020 track-record page for Decision No. 23 of 2020 after the direct PDF endpoint
  drifted to an empty 500/page-not-found response; and
  `thailand-sec-meme-fan-nft-exchange-token-ban-2021-06` now uses the official Thai SEC No. 114/2021 Wayback
  memento, removing its `evidence_tier=attested_secondary` caveat and upgrading trigger, observation, and
  attribution reliability to high.

## Admitted composition (365)
| dimension | breakdown |
|---|---|
| **research_stratum** | S4_nation_state 111 · S5_corporate 95 · S3_doj_sec_cftc_fiod 76 · S1_ofac_sdn 52 · S6_supranational 30 · S2_ofac_removal 1 |
| **temporal_tier** | comparable_main_2017_present 305 · historical_baseline_2013_2016 40 · discovery_only_2007_2012 20 |
| **evidence_tier** | admission_grade 329 · **attested_secondary 36** (lower-tier, filterable — see codebook §10) |
| **admission_tier** | empirical_case 264 · null_case 97 · anchor_case 4 |
| **empirical_shape** | comparison 266 · null_event 97 · cascade 2 |

**Reading the table:** the census is dominated by single/low-layer `comparison` and `null` events (expected — most
censorship actions are observed at 1–2 layers; OFAC designations are `null_case` denominators). The **36
`attested_secondary`** rows are the well-documented single-source national bans + corporate restrictions admitted
below the strict source floor — they are explicitly tagged so any IRR / κ / headline-census computation can
exclude or down-weight them with `evidence_tier == attested_secondary`.

## What this session changed (261 → 365 net)
1. **Waves 1–3 fully processed** (S1/S3/S4/S5/S6 bulk authoring → adversarial verify → admit), corpus → 322.
2. **Task 1 — VERIFY-FLAG refinement** (+9): 5 OFAC null_cases + 4 non-OFAC; softened SDN-entry/penalty
   over-claims to match captured sources; 2 held with corrected flags. → 331.
3. **Task 2 — source-strengthening** (+37 before later false-positive rejection): +3 via official-PDF capture (philippines-bsp / argentina-bcra /
   ecuador-COMF, all Wayback-archived); +34 via the new **`evidence_tier=attested_secondary`** lower tier
   (25 clean + 9 flagged national bans; two of those were later upgraded to admission-grade by item 11 and the
   2026-06-01 quality-loop repair). → 368.
4. **Codebook 4.0.0** — added `evidence_tier` (orthogonal source-strength grade) + §10 + validator support;
   current validator regression 405/405.
5. **Continuation P1/P2 cleanup** — resolved US-state regulator stratum policy (state/subnational
   administrative actions stay `regulatory_enforcement` / `S4_nation_state`), recoded NYDFS BitLicense
   accordingly, rejected Iraq as warning/context-only, rejected GoldAge as pre-2007 out-of-frame, and
   repaired source anchors for Task Force Rusich + Bitfinex US exit (both still human-only drafts), pinned the
   Circle/Multichain USDC blacklist tx hashes while correcting its trigger date to 2023-07-07, and repaired the
   Tether/OKX/DOJ 2025 row with DOJ primary legal anchors plus seven 2025 USDT DestroyedBlackFunds txs.
6. **Continuation P2 asset-onchain repair** — repaired the Tether/OFAC/Iran 2026 row with an OFAC primary-legal
   SDN update naming the two Central Bank of Iran TRON addresses plus two TronGrid-verified USDT
   AddedBlackList tx hashes in block 82092618. It remains a human-only draft.
7. **Continuation P2 partial Circle repair (superseded)** — resolved the public 0x61f...e543 Goated.com wallet in the
   Circle sealed-civil-case row to one USDC Blacklisted(address) tx plus the matching UnBlacklisted(address)
   recovery tx. This was the conservative interim repair before AMLBot's complete 16-address list was captured
   and verified in item 9 below.
8. **Continuation P2 T3 repair** — pinned two same-day TronGrid-verified USDT `AddedBlackList(address)` txs for
   the T3 Financial Crime Unit launch row. The row is now an explicit representative subset rather than a
   tx-less aggregate claim; it remains `partially_measured` / `status=draft` because the public launch source
   does not enumerate the full "over USDT 12M" frozen-address set and automation cannot promote
   `origin=agent_draft` events.
9. **Continuation P2 Circle full-list repair** — superseded the earlier one-address Circle sealed-civil partial
   repair by capturing AMLBot's 2026-03-26 full 16-address list and verifying all 16 addresses against cached
   USDC `Blacklisted(address)` receipts from the 2026-03-23 batch. The row is now
   `target.enumeration=complete` / `asset_onchain=measured`, but remains `status=draft` because automation
   cannot promote `origin=agent_draft` events.
10. **Continuation P4 admitted-row source strengthening** — pinned Poloniex's official Medium post for
    `poloniex-circle-us-token-geofence-2019-05`, upgrading the trigger and observed_change from
    semi-primary trade-press anchors to a primary_corporate replayable source. The row remains admitted;
    attribution is now direct for the Poloniex geofence action while the regulatory rationale stays scoped
    as generic U.S. securities-classification uncertainty.
11. **Continuation P4 lower-tier source strengthening** — pinned Binance's official support article
    (`Terms of Use Review`) and same-day Terms of Use Wayback capture for
    `binance-com-us-customer-geofence-2019-06`. The row now meets the strict admission-grade source
    floor, no longer uses `evidence_tier=attested_secondary`, and has a concrete
    `target.entity` for the U.S.-person Binance.com customer class.
12. **Continuation P4 registry reconciliation** — `analysis/census_gap_registry.tsv` now matches exact
    `events/*.yaml` ids for non-duplicate rows and records semantic-covered slug mismatches: 185
    verified+scope-tagged registry rows, 118 covered by corpus / duplicate / semantic precedent. Of the
    remaining 67 `in_corpus=false` rows, 66 are reviewed-excluded/context-only/out-of-scope/proposal-only
    under codebook §9 and 1 is an explicit held evidence-floor row; 0 exact-id candidate rows remain to triage from the 264-row
    candidate pool. `bangladesh-bb-crypto-illegality-2017-09` was closed as a
    date-corrected 2017-12-24 cautionary notice rather than a distinct binding restriction; the source
    record supports a warning/request about possible legal risk, not a new service denial, platform block,
    payment-rail prohibition, or binding ban beyond `bangladesh-bb-bitcoin-warning-2014`.
    The broader Bangladesh reaffirmation candidates are now date-corrected to the operative 2022-09-15
    Bangladesh Bank FEPD FE Circular No. 24 and represented by draft
    `bangladesh-bank-fepd-virtual-assets-prohibition-2022-09`, using the official FEPD circular PDF plus
    the BFIU Annual Report 2021-22 as replayable official anchors.
    `saudi-standing-committee-crypto-illegal-2018-08` is now scope-narrowed to draft
    `saudi-standing-committee-virtual-currency-warning-2018-08`: the official SAMA Arabic notice supports
    a no-approval / no-licensed-persons warning, but no replayable hard exchange shutdown or bank-rail
    cutoff, so the draft is modeled as an S4 null_case denominator.
    `india-sc-iamai-rbi-ban-reversal-2020-03` is now closed as a covered recovery anchor on admitted
    `india-rbi-crypto-ban-2018`, using official Supreme Court and RBI sources for the 2020-03-04 reversal
    without creating a separate admitted event.
    The two Bolivia 2024 Resolution 082/2024 ban-lift candidate slugs are now closed as covered by a
    recovery/update block on admitted `bolivia-bcb-crypto-prohibition-2014`; official BCB legal and press
    sources pin the 2024-06-26 payment-channel reopening without claiming measured exchange restoration.
    The two Tunisia 2018 BCT criminalization candidate slugs are now closed as reviewed-excluded/context-only:
    captured claim sources are non-contemporaneous 2025/2026 explainers without a primary BCT/legal
    instrument, while captured Tunisian coverage supports legal ambiguity and later ad hoc enforcement
    concerns rather than a distinct 2018 crypto-stack censorship action.
    Six platform-failure / soft-governance exact candidates are now closed as reviewed-excluded/context-only:
    Bitstamp, Cryptsy, and Bitfinex 2015-2016 hack/insolvency rows are incident-response failures, while
    IOSCO DeFi, FSB EMDE global-stablecoin, and IOSCO investor-education rows are recommendations or
    reporting artifacts with no operative access restriction.
    Eight supranational update/review/report rows are now closed: BCBS 2024 disclosure/amendments and
    FATF 2024 Targeted Update are covered by existing standards arcs, while FATF R16 2025, FATF 2025
    Targeted Update, IOSCO/FSB 2025 thematic reviews, and FATF 2026 risk reports are context-only
    artifacts with no standalone service-denial action.
    Two additional exact candidates are now represented by source-pinned `agent_draft` rows:
    `japan-fsa-margin-leverage-cap-2x-2020-05` and
    `magic-eden-ofac-sanctioned-country-block`. The GitHub sanctioned-country account-restriction row is
    closed as out-of-scope because the captured policy is a non-crypto-specific code-hosting sanctions
    restriction rather than a crypto-stack service-denial action.
    The Japan FSA margin draft has since been source-strengthened with the official Japanese Law Translation
    PDF for the Cabinet Office Order on Financial Instruments Business, directly anchoring the 50/100
    required-deposit formula behind the 2x cap; it remains non-admitted pending human admission/scope review.
    The prior 8-row exact-id queue is now exhausted: Tencent/WeChat NFT and Binance Europe retreat are
    semantic-covered, Tether APAC pig-butchering is exact-covered by admitted `tether-pig-butchering-second-wave-2024`,
    FATF 2022 is context-only, Thailand SEC staking/lending is date/scope-corrected as proposal-policy rather
    than a pinned 2022 operative ban, MetaMask Apple App Store removal is reviewed-excluded after primary
    MetaMask oEmbed capture plus press attribution to an internal operational error, and WazirX/Tether remains
    held until it has asset-onchain tx_hash/address-set evidence. The Bybit/Tether held row is now
    date/scope-corrected into draft `t3-bybit-hack-usdt-freeze-2025-03`, using Tether's 2025-03-26
    primary T3 FCU announcement, the Bybit/LazarusBounty public address API, and 18 USDT blacklist receipts.
    `cftc-bzerox-founders-settlement-2022-09` was added to the registry as semantic-covered by
    `cftc-v-ooki-dao-2022`, which already uses the same CFTC 8590-22 trigger and enumerates bZeroX LLC,
    both founders, and successor Ooki DAO.
    Eight additional candidate-pool rows were triaged: Liberty Reserve takedown/sentencing, e-Bullion
    indictment, and e-Gold sentencing are covered by existing corpus enforcement arcs; Roman Semenov 2025
    is an OFAC authority-tag-only change with no independent access restoration; Centra and BitConnect are
    fraud/Ponzi prosecutions; Mt. Gox Chapter 15 is bankruptcy administration after platform failure.
    A second follow-on S4 triage added 25 exact-slug closures: 18 semantic-covered duplicates
    (Kenya, Nepal, Pakistan, Qatar, Egypt, UAE, Thailand, BlockFi, Taiwan, Korea, Sri Lanka, Jordan,
    and Iraq) and 7 reviewed-excluded soft warning / non-recognition rows (France, Norway, Malaysia,
    Belgium, Mexico, Denmark, and Cambodia).
    A third follow-on triage added 20 more closures: 10 covered slug mismatches/date corrections
    (Algeria, Argentina, Canada CSA, Venezuela SUNACRIP, Nigeria Binance, OKX Canada, Huobi privacy
    coins, and Circle/Multichain) plus 10 reviewed exclusions for political pressure, draft legislation,
    fraud/Ponzi/rug-pull prosecutions, non-binding guidance, administrative framework transfer, and a
    malformed placeholder candidate.
    A fourth follow-on triage added 20 closures: 12 covered/date-corrected rows (Korea privacy-coin
    delistings, Liberty Reserve Costa Rica, BTC-e/Vinnik disposition, Sinbad/Blender DOJ, DOJ/Tether
    pig-butchering forfeiture, Circle sealed-civil freeze, OpenSea/MetaMask sanctions blocks, EU TFR
    application, IMF-FSB synthesis paper, Binance Canada, and Iran CBI exchange-payment-gateway block)
    and 8 reviewed exclusions (FinCEN CVC-mixing NPRM, Mango exploit prosecution, India VDA tax/TDS
    duplicates, Kazakhstan mining tax hike, Pakistan ban-intent statement, and G20 roadmap status report).
    `bittrex-global-shutdown-2023-11` was moved
    from borderline false into a narrow primary-corporate-captured `origin=agent_draft` row; it remains
    non-admitted pending human admission / causation review. `colonial-pipeline-darkside-ransom-clawback-doj-2021`
    was moved from on-chain-gated false into a narrow primary-onchain-pinned `origin=agent_draft` row;
    it remains non-admitted pending human attribution / admission review.
    This continuation added official-source drafts for `nydfs-bittrex-bitlicense-denial-2019-04`
    (NYDFS press release + denial-letter PDF capture) and `kuwait-cma-virtual-assets-prohibition-2023-07`
    (CBK official PDF capture; CMA live page verified but not CLI-captured), and closed the Singapore MAS
    public-advertising plus Nexo eight-state candidates as covered by existing corpus rows.
    It then added `celsius-multistate-cease-desist-earn-2021-09` as a conservative official-source
    draft using New Jersey and Texas 2021-09-17 PDFs; the short-form duplicate is registered as covered,
    and the row remains non-admitted pending OCR/human confirmation of the scanned New Jersey order.
    A fifth follow-on triage added 5 reviewed exclusions for post-hoc SEC/DOJ disposition rows with no
    new platform-access restriction: ShapeShift's 2024 SEC settlement, the Bitfinex hack laundering case,
    the James Zhong Silk Road forfeiture, the Banmeet Singh dark-web vendor forfeiture, and the DPRK
    IT-worker civil forfeiture action.
    A sixth follow-on triage added 4 exact-id closures: Cheil / First Credit Bank is covered by
    `dprk-usdt-network-ofac-2025`; DataCell / Valitor Supreme Court is covered as downstream trajectory
    of `datacell-v-valitor-iceland-district-court-2012-07`; `bitcoin-maven-tetley-doj-2018` was added
    as an official DOJ / Wayback-captured `origin=agent_draft` individual-MSB off-ramp row; and the
    Sim Hyon Sop DOJ indictment was excluded as a same-day criminal-indictment disposition with the
    sanctions/access-denial component already modeled by `ofac-dprk-it-worker-sim-hyon-sop-2023-04`.
    A seventh follow-on triage added 3 OFAC closures: `fayzimatov-alqaeda-syria-ofac-2021-07` was added
    as an official OFAC/Treasury-captured `origin=agent_draft` individual-BTC null_case row; Kimsuky 2023
    and Nordic Resistance Movement 2024 were reviewed-excluded because their official OFAC artifacts do
    not enumerate cryptocurrency addresses or a crypto-platform/payment-rail access restriction.
    An eighth follow-on triage added `crypto-capital-fowler-doj-2019` as an official DOJ / Wayback-captured
    `origin=agent_draft` off-ramp shadow-banking row. The draft models only Fowler / GTS / Crypto Capital's
    fiat-rail service for cryptocurrency exchanges; it does not claim a Bitfinex/Binance exchange shutdown,
    frontend seizure, or on-chain asset freeze.
    A ninth follow-on triage added `terror-financing-crypto-seizure-doj-2020` as an official DOJ /
    Wayback-captured `origin=agent_draft` l4_frontend seizure row. The draft narrowly codes seized
    websites/Facebook pages; reported cryptocurrency-account seizures remain `asset_onchain=not_measured`
    until a public tx_hash is pinned.
    A tenth follow-on triage added `revil-vasinskyi-polyanin-doj-2021` as an official DOJ /
    Wayback-captured `origin=agent_draft` ransomware forfeiture row. The draft records DOJ's USD 6.1M
    seizure and later 39.89138522 BTC final-forfeiture statement, but keeps `asset_onchain=not_measured`
    until a public tx_hash, address-history capture, or body-hashed court complaint enumerating the wallet
    is pinned.
    An eleventh follow-on triage added `netwalker-vachon-desjardins-doj-2022` as an official DOJ + RCMP /
    Wayback-captured `origin=agent_draft` NetWalker ransomware forfeiture row. The draft records the
    official 719 BTC search-seizure and 680 BTC Canadian forfeiture facts, but keeps
    `asset_onchain=not_measured` until a public tx_hash, address-history capture, or body-hashed court
    document enumerating the wallet is pinned.
    A twelfth follow-on triage added `bitcoin-fog-sterlingov-doj-2024` as an official DOJ /
    Wayback-captured `origin=agent_draft` Bitcoin-mixer operator-state row. The draft models only the
    2024 conviction/sentencing criminal-finality endpoint; the DOJ-reported 1,354/1,345 BTC forfeiture
    facts remain `asset_onchain=not_measured` until a public tx_hash, address-history capture, or
    wallet-enumerating court artifact is pinned.
    A thirteenth follow-on triage reviewed `fincen-paxful-bsa-penalty-2025-08` against official FinCEN
    and DOJ sources and closed it as reviewed-excluded: the 2025-12-09 Consent Order / guilty-plea
    resolution imposes monetary, cooperation, record-retention, and successor-assignment terms for past
    AML/BSA failures, but no platform shutdown, user offboarding, geoblock, industry bar, asset freeze,
    or other new service-denial action.
    A fourteenth follow-on triage added `lebanon-bdl-bitcoin-warning-2013-12` as an official BDL-PDF
    captured `origin=agent_draft` historical-baseline row. The draft narrowly models BDL Announcement
    No. 900 as a class-level warning / electronic-money restriction signal addressed to banks, financial
    institutions, exchange institutions, brokerage institutions, and the public; it does not claim a
    specific exchange shutdown, user offboarding, domain block, or on-chain action.
    A fifteenth follow-on triage closed `russia-prosecutor-general-monetary-surrogate-2014-02` as
    semantic-covered by admitted `russia-cbr-bitcoin-information-letter-2014`: the official Prosecutor
    General Wayback page confirms the 2014 monetary-surrogate / no-use posture and interagency
    coordination with CBR, FSB, and MVD, but does not add a distinct exchange shutdown, banking-rail
    cutoff, domain block, asset freeze, or measured off-ramp observation.
18. **Sixteenth follow-on triage (Vietnam 2014 split)** — `vietnam-sbv-bitcoin-prohibition-statement-2014-02`
    was added as a conservative `origin=agent_draft` historical-baseline null_case row using VietnamPlus/VNA
    contemporaneous coverage plus an official SBV retrospective page. The older alternate slug now points to
    this draft rather than being collapsed into the admitted 2017 SBV fines/payment-prohibition row.
19. **Seventeenth follow-on triage (Kyrgyzstan 2014 date correction)** —
    `kyrgyzstan-nbkr-virtual-currency-payment-warning-2014-07` was added as a conservative
    `origin=agent_draft` historical-baseline null_case row using the official NBKR English warning page
    plus a confirmed 2026-05-31 Wayback snapshot. The stale
    `kyrgyzstan-nbkr-bitcoin-payment-ban-2014-08` candidate slug now points to this date-corrected draft.
20. **Eighteenth follow-on triage (Bangladesh 2022 FEPD circular)** —
    `bangladesh-bank-fepd-virtual-assets-prohibition-2022-09` was added as a conservative
    `origin=agent_draft` payment-rail restriction row using the official Bangladesh Bank FEPD circular PDF
    and BFIU Annual Report 2021-22. Two stale Bangladesh reaffirmation candidate slugs now point to this
    date-corrected draft rather than to the 2014 warning row.
21. **Nineteenth follow-on triage (Saudi 2018 Standing Committee warning)** —
    `saudi-standing-committee-virtual-currency-warning-2018-08` was added as a conservative
    `origin=agent_draft` S4 null_case row using the live official SAMA Arabic notice plus a captured Arab
    News English corroboration. The stale "crypto illegal" candidate slug is now scope-narrowed to this
    no-approval / no-licensed-persons denominator; no exchange shutdown, bank cutoff, frontend block, or
    on-chain action is claimed.
22. **Twentieth follow-on triage (India 2020 RBI-ban reversal)** —
    `india-rbi-crypto-ban-2018` now has official Supreme Court and RBI recovery anchors for the 2020-03-04
    legal reversal of the 2018 RBI banking circular. The exact candidate
    `india-sc-iamai-rbi-ban-reversal-2020-03` is closed as covered by that recovery block rather than
    modeled as a separate admitted event.
23. **Twenty-first follow-on triage (Bolivia 2024 Resolution 082/2024)** —
    `bolivia-bcb-crypto-prohibition-2014` now has official BCB Resolution 082/2024 recovery/update
    anchors. The exact candidates `bolivia-bcb-crypto-ban-lift-resolution-082-2024-06` and
    `bolivia-bcb-crypto-ban-lift-082-2024-06` are closed as covered by that block; the wording stays
    narrow because the captured legal instrument directly leaves Resolution 144/2020 without effect and
    re-enables electronic payment channels for virtual-asset purchase/sale operations.
24. **Twenty-second follow-on triage (Tunisia 2018 BCT criminalization)** —
    `tunisia-central-bank-crypto-criminalization-2018` and `tunisia-cbt-crypto-criminalization-2018`
    are closed as reviewed-excluded/context-only. The review captured the non-contemporaneous claim
    sources plus local Tunisian coverage; no primary BCT directive, legal text, or replayable 2018
    service-denial action was located.
25. **Twenty-third follow-on triage (platform failure / soft governance closures)** —
    Six low-dispute exact candidates are now closed without changing admitted-event counts. Bitstamp,
    Cryptsy, and Bitfinex 2015-2016 rows are reviewed-excluded platform-failure/hack-response cases
    under codebook §9. IOSCO DeFi 2023, FSB EMDE global-stablecoin 2024, and IOSCO investor-education
    2024 are reviewed-context-only recommendations/reporting artifacts with no operative access restriction.
26. **Twenty-fourth follow-on triage (supranational updates/reviews/reports)** —
    Eight exact candidates are now closed without changing admitted-event counts. BCBS 2024 disclosure
    framework/amendments are covered as an update to the admitted 2022 BCBS cryptoasset prudential
    standard, and the FATF 2024 Targeted Update is already pinned inside the admitted FATF 2023-2024
    standards/grey-list arc. FATF R16 2025, FATF 2025 Targeted Update, IOSCO/FSB 2025 thematic reviews,
    and FATF 2026 stablecoin/unhosted-wallet plus offshore-VASP reports are reviewed-context-only:
    official captures show implementation monitoring, risk reporting, or recommendations, not standalone
    crypto-stack service-denial actions.
27. **Twenty-fifth follow-on triage (Japan/Magic Eden drafts + GitHub closure)** —
    Two exact candidates are now represented by `status=draft` / `origin=agent_draft` rows with replayable
    captured sources: Japan FSA's 2020-05-01 retail crypto-asset CFD/margin 2x leverage-cap draft and
    Magic Eden's OFAC-sanctioned-country marketplace/frontend access-restriction draft. Both are deliberately
    kept out of admitted paper counts pending human admission/scope review. `github-sanctioned-country-
    account-restriction-2019-07` is closed as out-of-scope after capturing GitHub's official trade-controls
    policy: it is a general code-hosting sanctions restriction, not a crypto-specific platform, asset, wallet,
    exchange, NFT-marketplace, or protocol restriction. A later source-strengthening pass pinned the
    official Japanese Law Translation PDF for the Cabinet Office Order on Financial Instruments Business to
    the Japan FSA draft, directly anchoring the 50/100 required-deposit formula behind the 2x cap.
28. **Twenty-sixth follow-on triage (exact queue exhausted)** —
    The remaining 8 exact-id candidate rows are now all represented in the registry without changing event
    counts. Three are covered (`china-tencent-wechat-nft-account-purge-2022` by the admitted PRC NFT
    self-discipline cohort; `binance-europe-retreat-cyprus-austria-belgium-2023` by the Binance Europe
    withdrawal/enforcement family; `tether-apac-pig-butchering-freeze-2024-06` by admitted
    `tether-pig-butchering-second-wave-2024`). Two are reviewed non-authorable as currently framed
    (`fatf-targeted-update-va-vasp-2022` context-only and `thailand-sec-staking-lending-ban-2022-09`
    proposal/date-corrected rather than a pinned 2022 operative ban). MetaMask Apple App Store removal is now
    reviewed-excluded after primary MetaMask oEmbed capture and press attribution to an internal operational
    error rather than Apple action. One row remains held, not authored, until it meets the evidence floor:
    `wazirx-tether-usdt-hack-freeze-2025-01` needs asset-onchain tx_hash/address-set anchors. Its
    2026-06-01 follow-up note (`analysis/wazirx_tether_held_investigation_2026_06_01.md`) records that
    date-window ETH USDT blacklist triage found nearby blacklist activity but no public WazirX attribution,
    frozen address set, or blacklist tx anchor.
    `tether-bybit-hack-lazarus-freeze-2025-02` is now date/scope-corrected to the non-admitted draft
    `t3-bybit-hack-usdt-freeze-2025-03`.

## Method invariants proven this session (keep using)
- **Dry-run admission gating**: simulate draft→admitted in a temp file, run validate, admit ONLY if it passes;
  auto-revert on failure. No broken event is ever committed.
- **Independent source-rendering tiebreak**: the adversarial verifier OVER-flags (binance-dex, sec-tradestation,
  uae-sca all checked out fully); render+grep the pinned HTML/PDF to confirm load-bearing claims before trusting
  a FIX label — but it also catches REAL over-claims (sec-abra $1.65M), so every specific is grep-verified.
- **Capture yield rule**: only official PDFs / static pages on standard URLs capture cleanly; JS-gated exchange
  pages (Binance) return empty bodies and bot-protected gov sites reset — don't rely on them.

## Held drafts (26) — all honest, documented holds
- **1 partially repaired asset_onchain draft still lacks a complete target set**: t3-financial-crime-unit now pins
  two same-day USDT-on-TRON blacklist txs, but the public launch source does not enumerate the full "over USDT
  12M" frozen-address set.
- **1 terminal asset_onchain draft**: ren-protocol (off-chain RenVM darknode signature cessation; no
  on-chain tx can exist, so keep as documented draft precedent).
- **8 source-repaired human-only drafts**: task-force-rusich now has the official OFAC crypto-address source;
  bitfinex-us-exit-2017 now has official Bitfinex /posts/216 and /posts/227 Wayback captures;
  circle-usdc-multichain now has full
  addresses + three primary_onchain tx hashes; tether-okx-doj-2025 now has DOJ OPA + D.D.C. complaint
  captures, seven USDT Token Group addresses, seven 2023 AddedBlackList txs, and seven 2025
  DestroyedBlackFunds txs; tether-iran-fury now has OFAC address enumeration plus two Tron
  AddedBlackList tx hashes; circle-usdc-sealed now has a complete 16-address AMLBot list plus 16 cached
  USDC blacklist receipts; bittrex-global-shutdown now has an official primary-corporate Zendesk notice;
  colonial-pipeline-darkside-clawback now has DOJ/Paladin captures plus a primary_onchain Bitcoin tx hash.
  All remain `origin=agent_draft`, so automation does not promote them.
- **16 new official-source agent drafts**: nydfs-bittrex-bitlicense-denial-2019-04,
  kuwait-cma-virtual-assets-prohibition-2023-07, and
  celsius-multistate-cease-desist-earn-2021-09 are newly modeled from the P4 queue with replay anchors;
  bitcoin-maven-tetley-doj-2018 is modeled from an official DOJ Wayback capture as an individual-MSB
  off-ramp row; fayzimatov-alqaeda-syria-ofac-2021-07 is modeled from official OFAC/Treasury captures as
  an individual-BTC null_case row; crypto-capital-fowler-doj-2019 is modeled from official DOJ Wayback
  captures as a shadow-banking / fiat-rail off-ramp row; terror-financing-crypto-seizure-doj-2020 is modeled
  from official DOJ Wayback/PDF captures as a narrow website/social-page seizure row; revil-vasinskyi-
  polyanin-doj-2021 is modeled from official DOJ Wayback captures as a ransomware proceeds forfeiture
  row with asset_onchain deliberately held at not_measured; netwalker-vachon-desjardins-doj-2022 is modeled
  from official DOJ + RCMP Wayback captures as a NetWalker ransomware proceeds forfeiture row with
  asset_onchain deliberately held at not_measured; bitcoin-fog-sterlingov-doj-2024 is modeled from
  official DOJ Wayback captures as a Bitcoin-mixer operator-state criminal-finality row, with DOJ-reported
  BTC forfeiture kept at asset_onchain=not_measured until transaction-level evidence is pinned; and
  lebanon-bdl-bitcoin-warning-2013-12 is modeled from the official BDL Announcement No. 900 PDF as a
  historical-baseline class-level central-bank warning / electronic-money restriction signal;
  vietnam-sbv-bitcoin-prohibition-statement-2014-02 is modeled as a distinct 2014 SBV payment-instrument /
  credit-institution warning rather than collapsed into the admitted 2017 fines/payment-prohibition event;
  and kyrgyzstan-nbkr-virtual-currency-payment-warning-2014-07 is modeled from the official NBKR warning
  page as a date-corrected class-level virtual-currency payment warning with no named downstream cutoff;
  and bangladesh-bank-fepd-virtual-assets-prohibition-2022-09 is modeled from official Bangladesh Bank
  FEPD/BFIU PDFs as a date-corrected payment-rail restriction distinct from the 2014 warning row; and
  saudi-standing-committee-virtual-currency-warning-2018-08 is modeled from the official SAMA Arabic
  committee notice as a no-approval / no-licensed-persons null_case denominator rather than a hard
  exchange-shutdown claim; and t3-bybit-hack-usdt-freeze-2025-03 is modeled from Tether's official
  2025-03-26 T3 FCU announcement, the public Bybit/LazarusBounty address API, and 18 pinned USDT
  AddedBlackList receipts as a subset-scoped Bybit-hack freeze row.
  All remain non-admitted pending human admission review. Celsius
  additionally needs OCR/human confirmation of the scanned New Jersey order text before any promotion.

## New rejected / context-only rulings
- **iraq-cbi-cryptocurrency-prohibition-2017-12**: rejected as warning/context-only; the captured Arabic page
  supports cautioning against use, not a clean binding ban row.
- **goldage-ny-state-indictment-2006-07**: rejected as out-of-frame; the corpus boundary remains strict at
  2007-01-01.

→ Remaining work is tracked in **`analysis/NEXT_STEPS.md`**.
