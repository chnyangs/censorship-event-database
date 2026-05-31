# 📍 State of the corpus — 2026-05-31 (continuation snapshot)

**Authoritative current snapshot.** Supersedes `MORNING_REVIEW_2026_05_31.md` (which is now stale at 259).
Detailed tick-by-tick log: `analysis/overnight_collection_notes_2026_05_31.md`.

## Headline
- **402 events**: **368 admitted** / 25 draft / 9 rejected.
- **Integrity**: `scripts/validate.py` passes **402 / 402 [OK]**; `make check` passes. All changes remain local, never pushed.
- **This session continuation delivered +107 admitted** (corpus 261 → 368), plus codebook **4.0.0** (`evidence_tier`).

## Admitted composition (368)
| dimension | breakdown |
|---|---|
| **research_stratum** | S4_nation_state 111 · S5_corporate 97 · S3_doj_sec_cftc_fiod 77 · S1_ofac_sdn 52 · S6_supranational 30 · S2_ofac_removal 1 |
| **temporal_tier** | comparable_main_2017_present 308 · historical_baseline_2013_2016 40 · discovery_only_2007_2012 20 |
| **evidence_tier** | admission_grade 334 · **attested_secondary 34** (lower-tier, filterable — see codebook §10) |
| **admission_tier** | empirical_case 267 · null_case 96 · anchor_case 5 |
| **empirical_shape** | comparison 270 · null_event 96 · cascade 2 |

**Reading the table:** the census is dominated by single/low-layer `comparison` and `null` events (expected — most
censorship actions are observed at 1–2 layers; OFAC designations are `null_case` denominators). The **34
`attested_secondary`** rows are the well-documented single-source national bans + corporate restrictions admitted
below the strict source floor — they are explicitly tagged so any IRR / κ / headline-census computation can
exclude or down-weight them with `evidence_tier == attested_secondary`.

## What this session changed (261 → 368)
1. **Waves 1–3 fully processed** (S1/S3/S4/S5/S6 bulk authoring → adversarial verify → admit), corpus → 322.
2. **Task 1 — VERIFY-FLAG refinement** (+9): 5 OFAC null_cases + 4 non-OFAC; softened SDN-entry/penalty
   over-claims to match captured sources; 2 held with corrected flags. → 331.
3. **Task 2 — source-strengthening** (+37): +3 via official-PDF capture (philippines-bsp / argentina-bcra /
   ecuador-COMF, all Wayback-archived); +34 via the new **`evidence_tier=attested_secondary`** lower tier
   (25 clean + 9 flagged national bans). → 368.
4. **Codebook 4.0.0** — added `evidence_tier` (orthogonal source-strength grade) + §10 + validator support;
   current validator regression 402/402.
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
10. **Continuation P4 registry reconciliation** — `analysis/census_gap_registry.tsv` now matches exact
    `events/*.yaml` ids for non-duplicate rows and records semantic-covered slug mismatches: 166
    verified+scope-tagged registry rows, 110 covered by corpus / duplicate / semantic precedent. All
    remaining 56 `in_corpus=false` rows are now reviewed-excluded/context-only under codebook §9, leaving
    0 currently actionable registry rows; 19 exact-id candidate rows remain to triage from the 264-row
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

## Method invariants proven this session (keep using)
- **Dry-run admission gating**: simulate draft→admitted in a temp file, run validate, admit ONLY if it passes;
  auto-revert on failure. No broken event is ever committed.
- **Independent source-rendering tiebreak**: the adversarial verifier OVER-flags (binance-dex, sec-tradestation,
  uae-sca all checked out fully); render+grep the pinned HTML/PDF to confirm load-bearing claims before trusting
  a FIX label — but it also catches REAL over-claims (sec-abra $1.65M), so every specific is grep-verified.
- **Capture yield rule**: only official PDFs / static pages on standard URLs capture cleanly; JS-gated exchange
  pages (Binance) return empty bodies and bot-protected gov sites reset — don't rely on them.

## Held drafts (25) — all honest, documented holds
- **1 partially repaired asset_onchain draft still lacks a complete target set**: t3-financial-crime-unit now pins
  two same-day USDT-on-TRON blacklist txs, but the public launch source does not enumerate the full "over USDT
  12M" frozen-address set.
- **1 terminal asset_onchain draft**: ren-protocol (off-chain RenVM darknode signature cessation; no
  on-chain tx can exist, so keep as documented draft precedent).
- **8 source-repaired human-only drafts**: task-force-rusich now has the official OFAC crypto-address source;
  bitfinex-us-exit-2017 now has a 2017 rendered article capture; circle-usdc-multichain now has full
  addresses + three primary_onchain tx hashes; tether-okx-doj-2025 now has DOJ OPA + D.D.C. complaint
  captures, seven USDT Token Group addresses, seven 2023 AddedBlackList txs, and seven 2025
  DestroyedBlackFunds txs; tether-iran-fury now has OFAC address enumeration plus two Tron
  AddedBlackList tx hashes; circle-usdc-sealed now has a complete 16-address AMLBot list plus 16 cached
  USDC blacklist receipts; bittrex-global-shutdown now has an official primary-corporate Zendesk notice;
  colonial-pipeline-darkside-clawback now has DOJ/Paladin captures plus a primary_onchain Bitcoin tx hash.
  All remain `origin=agent_draft`, so automation does not promote them.
- **15 new official-source agent drafts**: nydfs-bittrex-bitlicense-denial-2019-04,
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
  exchange-shutdown claim.
  All remain non-admitted pending human admission review. Celsius
  additionally needs OCR/human confirmation of the scanned New Jersey order text before any promotion.

## New rejected / context-only rulings
- **iraq-cbi-cryptocurrency-prohibition-2017-12**: rejected as warning/context-only; the captured Arabic page
  supports cautioning against use, not a clean binding ban row.
- **goldage-ny-state-indictment-2006-07**: rejected as out-of-frame; the corpus boundary remains strict at
  2007-01-01.

→ Remaining work is tracked in **`analysis/NEXT_STEPS.md`**.
