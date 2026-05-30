# Overnight census collection — running notes (for morning review)

**Run window:** 2026-05-30 ~23:35 → 2026-05-31 07:00 Melbourne (AEST), unattended.
**Authorization:** user explicitly authorized autonomous execution-per-recommendation +
log-for-review; standing per-item YES/NO suspended for this window only.
**Mechanism:** durable cron `7,37 * * * *` (every ~30 min). Each tick reads
`analysis/overnight_MISSION.md` and advances the comprehensive census by one batch
(gap-registry extension + opportunistic full-event authoring), commits locally (never push),
logs here. Self-deletes the cron at ≥07:00 Melbourne.

**Scope (user-approved 2026-05-30):** Hybrid census of crypto-stack censorship since 2007 —
true census of S1/S2/S3/S4/S6 + saturation S5; OFAC unit = per designation-action. Priority:
2007-2016 back-fill + S2 first, then S1/S3/S4/S6 census, then S5 saturation.

**Deliverables:** `analysis/census_gap_registry.tsv` (verified sourced candidate cases) +
new event YAMLs under `events/` (authored when well-sourced) + `analysis/audit_log_session_1.jsonl`
rows. Morning review converts remaining registry rows to full events.

---

## Tick log

(Each cron tick appends an entry below: tick #, time, focus, registry rows added, events
authored, judgment calls + why, skips + why, anything needing human review.)

### Tick 0 (seed) — 2026-05-30 23:31 Melbourne — focus: 2007-2016 backfill (validation seed)
- Created `analysis/census_gap_registry.tsv` (header + 1 verified row).
- **egold-doj-indictment-2007-04** (S3, 2007-04-27): the canonical "since 2007" anchor. DOJ/USSS indictment of e-gold, unsealed 2007-04-27 (verified via justice.gov archive PR #07-301). Corpus had only the 2008 plea. Real DOJ sources pinned. This is the #1 priority full-event to author (highest-value 2007 anchor).
- Pipeline validated: WebSearch -> verify date+source -> registry row, no fabrication.
- Cron 1ddafe54 active; first autonomous tick fires ~23:37 Melbourne.

### Gap-discovery integrated — 2026-05-30 23:40 Melbourne
- Gap-discovery workflow (wf_7fa15316, 12 agents, ~1.06M tokens) finished: **238 raw candidates -> ~230 net new** after dedup.
- Wrote `analysis/census_gap_list.md` (prioritized synthesis) + extracted `analysis/census_gap_candidates.tsv` (**264 structured candidates with source_urls**: S4=106, S5=56, S3=53, S6=24, S1=24, S2=1).
- Key: **S2_ofac_removal is census-complete** (Semenov collapses into tornado-cash-ofac-delisting-2025). Priority back-fill = proto-2007-2012 (13) + early-bitcoin-2013-2016 (23).
- MISSION updated: ticks now work from census_gap_candidates.tsv in priority order, but MUST re-verify each candidate's date+source before trusting (agent URLs may be fabricated, per C-5).

### Tick 1 — 2026-05-30 23:40 Melbourne — focus: 2007-2016 back-fill (S3)
**Authored 1 full event (validates [OK]):**
- **liberty-reserve-coordinated-takedown-2013-05** (S3, historical_baseline, comparison/empirical_case). The seminal 2013-05-28 takedown: DOJ SDNY indicted 7 Liberty Reserve principals (founder Budovsky), seized 5 domains incl. LibertyReserve.com (l4_frontend), + first-ever FinCEN §311 against a virtual-currency provider (offramp_cex). Both observations attribution=direct, real DOJ/Treasury/FinCEN sources body_hash-pinned (verified via WebSearch, no fabrication). Corpus previously had only the 2011 license-denial. audit_id 465.

**⚠️ TWO SCHEMA/VOCAB DECISIONS FLAGGED FOR YOUR BLESSING (not changed overnight):**
1. **No 2007 temporal_tier.** `temporal_tier` enum earliest = `discovery_only_2008_2012` (starts 2008). The "since 2007" census needs a 2007 tier → **RECOMMEND** rename `discovery_only_2008_2012` → `discovery_only_2007_2012` (in schema/event.schema.json + validate.py refs + codebook). The **e-gold 2007 indictment** (egold-doj-indictment-2007-04, THE #1 anchor, sources already captured: 44f71f8a/3f32e6096b) is registered + ready to author the moment you bless this.
2. **controlled_vocab jurisdiction enum too small for S4 census.** Only ~42 country codes; the S4 work-list (~106 candidates) spans many missing (CR, KE, LB, JO, KH, EC, MA, DZ, IQ, EG, QA, SA, ...). I used `US` (lead jurisdiction) for Liberty Reserve 2013 + noted CR in prose. **RECOMMEND** bulk-add the missing ISO-3166 codes before authoring S4 events. Overnight, vocab-blocked S4 cases go to the registry (free-text) for morning authoring; I author only schema-fitting cases (US S1/S3, S5, S6).

**Skips/notes:** kept the tick bounded (1 high-value event + 2 flagged decisions). The registry stays at the e-gold 2007 anchor; future ticks extend it (each verifying its own sources). Next tick will work schema-fitting S3/S5/S6 candidates while the 2007-tier + jurisdiction-vocab decisions await morning blessing.

### Tick 2 — 2026-05-31 00:10 Melbourne — focus: 2007-2016 back-fill (TIER 1 registry breadth)
**+6 verified registry rows** (each source verified live-200 or Wayback-memento; no fabrication):
- liberty-reserve-budovsky-sentencing-2016-05 (S3, high) — completes the LR arc.
- **tradehill-dwolla-payment-cutoff-2012-02** (S5, AUTHOR-READY) — Dwolla cut TradeHill's rails under compliance pressure; early financial-rail debanking.
- **bitfloor-capital-one-debanking-2013-04** (S5) — Capital One debanked BitFloor (Operation-Choke-Point-era).
- cfpb-virtual-currency-consumer-advisory-2014-08 (S3, BORDERLINE — a warning, not a block).
- cryptsy-collapse-insolvency-2016-01 (S5, LIKELY OUT-OF-SCOPE — fraud/theft, not censorship).
- mtgox-chapter-15-us-bankruptcy-recognition-2014-06 (S3, BORDERLINE — bankruptcy recognition).

**⚠️ SCOPE-BOUNDARY DECISION FLAGGED:** the census needs a clear inclusion rule separating CENSORSHIP (state/corporate denial/blocking/seizure/freeze) from exchange FAILURES (fraud/hack/insolvency) and soft WARNINGS. RECOMMEND excluding pure failures/frauds (Cryptsy, Mt.Gox-collapse-as-such) and treating advisories (CFPB) as null/context only. I recorded the borderline cases with explicit scope flags rather than silently in/excluding them. Please bless the boundary in the morning.

**Bounded:** no new event authored this tick (registry breadth prioritized); tradehill-dwolla + bitfloor are author-ready (US, schema-fitting) for a later tick / morning. The 2007-tier + jurisdiction-vocab blocks from tick 1 still await your blessing.

### Tick 3 — 2026-05-31 00:40 Melbourne — focus: 2007-2016 S5 financial-rail debanking
**Authored 1 full event (validates [OK]):**
- **tradehill-dwolla-payment-cutoff-2012-02** (S5, discovery_only_2008_2012, comparison/empirical_case). Payment processor Dwolla severed early US Bitcoin exchange TradeHill's fiat rail (early 2012) -> exchange ceased; TradeHill v. Dwolla suit. Earliest-tier financial-rail de-risking censorship case (offramp_cex/plausible). 2 semi_primary_wayback (VentureBeat + American Banker), body_hash-pinned, verified. audit_id 466. (precision: month not in enum -> used week, coarsest available.)
- bitfloor-capital-one-debanking-2013-04 left registered/author-ready for a later tick (sibling case).
- Corpus now 256 admitted.

### Tick 4 — 2026-05-31 01:08 Melbourne — focus: S6 supranational census (registry breadth)
**+6 verified registry rows** (S6), each tagged by censorship-relevance:
- **DIRECT CENSORSHIP**: eu-russia-sanctions-crypto-services-ban-2022-10 (EU 8th package — total ban on crypto services to Russian persons; offramp_cex). The clearest S6 censorship case — AUTHOR-WORTHY after verifying exact package/date (8th=2022-10; later 16th/18th/19th/20th expanded it).
- **CENSORSHIP-ENABLING**: fatf-updated-rba-guidance-va-vasp-2021-10 (Travel Rule), bcbs-cryptoasset-prudential-sco60-2022 (1250% risk weight -> bank de-risking). Both WB-confirmed.
- **SOFT-GOVERNANCE / WARNING (likely context-only)**: iosco-2023-recommendations, fsb-stablecoin-recs-2023, esa-eu-virtual-currency-warning-2013. Tagged for the scope decision.

**Judgment:** S6 has many soft-governance framework docs (IOSCO/FSB/IMF/BCBS recommendations) — these are censorship-ENABLING infrastructure, not censorship ACTIONS. Recommend the morning scope decision clarify whether soft governance belongs (the existing 24 S6 corpus events set the precedent — e.g. MiCA is included). I tagged each rather than guess. The EU Russia-sanctions crypto bans are the unambiguous S6 censorship events worth authoring (verify exact packages first). No event authored this tick (registry breadth).

### Tick 5 — 2026-05-31 01:38 Melbourne — focus: S1 OFAC SDN census
**Authored 1 full event (validates [OK]):**
- **bitriver-russia-mining-ofac-2022-04** (S1, null_case). The FIRST OFAC designation of a crypto-MINING company (BitRiver AG + 10 RU subsidiaries, 2022-04-20, Treasury jy0731). Coded null_case per S1 convention (entity target, no addresses, offramp_cex observed_no_change/none, 14d window). Sources Treasury jy0731 + The Record, body_hash-pinned, verified. audit_id 467. Corpus now 257 admitted.
**+5 S1 registry rows** (Genesis Market, Netex24/Bitpapa, Evil Corp, Task Force Rusich, + BitRiver-as-authored). Treasury press-release URL pattern (home.treasury.gov/news/press-releases/jyXXXX) is consistent + verifiable; spot-verify each jyXXXX before authoring.
**Note:** S1 events follow a repetitive null_case template (designation = trigger; offramp_cex observed_no_change since downstream CEX cascade is unmeasured). The 24 S1 gaps are well-suited to fast batch-authoring in the morning using bitriver + zservers as templates.

### Tick 6 — 2026-05-31 02:08 Melbourne — focus: S3 DOJ/SEC census (registry breadth)
**+6 S3 registry rows**, scope-tagged:
- **ENFORCEMENT-CENSORSHIP**: sec-etherdelta-coburn-2018 (FIRST SEC action vs a DEX), sec-lbry-2021 (SEC suit forced LBRY to wind down), sec-kik-kin-2020 (token-offering crackdown).
- **ASSET-ONCHAIN SEIZURE**: colonial-pipeline-darkside-clawback-2021 (DOJ/FBI seized 63.7 BTC ransom). AUTHORING NOTE: needs a primary_onchain seizure tx_hash before authoring (codebook §1.6) — flagged in the row.
- **BORDERLINE/SOFT** (scope-boundary lens): onecoin-doj-2019 (fraud prosecution, not censorship of a legit service), sec-dao-report-2017 (regulatory framework report, not an action).
**Judgment:** continued scope-tagging — the S3 stratum mixes genuine enforcement-censorship (DEX/operator shutdowns) with fraud prosecutions (OneCoin/Centra = scams) and regulatory reports (DAO Report). Recommend the morning scope decision: include enforcement that restricts/shuts a *legitimate* platform; exclude pure fraud prosecutions + soft reports. EtherDelta (first DEX enforcement) is a strong author-next candidate.
**Registry now 24 rows** spanning S1/S3/S5/S6 + the 2007-2016 era. S4 nation-state (~106 cands) deferred — vocab-blocked, queued for morning ISO-code blessing then bulk-author.

### Tick 7 — 2026-05-31 02:38 Melbourne — focus: S5 corporate saturation (registry breadth)
**+5 S5 registry rows**, scope/dup-tagged:
- **AUTHOR-READY**: bittrex-privacy-coin-delisting-2021-01 (XMR/ZEC/DASH delisting, clean offramp_cex; template = kraken-monero-eu-delisting-2024).
- **DUPLICATE CAUGHT**: infura-metamask-venezuela-overbroad-geoblock-2022-03 = the corpus event infura-metamask-donetsk-luhansk-block-2022-03 (the Venezuela over-block was part of that same 2022-03-03 Infura geoblock I audited in C-5). Flagged DROP-as-dup (in_corpus=true) — avoids double-counting.
- **asset_onchain issuer freezes (need onchain tx before authoring)**: tether-garantex-usdt-freeze-2025-03 (~$28M frozen post-EU-sanction, clear censorship), tether-okx-225m-freeze (cross-stratum).
- **POLICY/BORDERLINE**: tether-voluntary-ofac-sdn-freeze-policy-2023-12 (a policy announcement, not a single action), bittrex-global-shutdown-2023-11 (SEC-driven vs business wind-down).
**Judgment:** dedup vigilance paid off (caught the Infura-Venezuela near-dup vs corpus). Tether issuer-freeze cases (Garantex etc.) are clear asset_onchain censorship but gated on locating the on-chain freeze tx (§1.6) — queued with explicit notes. Registry now 29 rows.

### Tick 8 — 2026-05-31 03:08 Melbourne — focus: S5 author (privacy delisting)
**Authored 1 full event (validates [OK]):**
- **bittrex-privacy-coin-delisting-2021-01** (S5, comparable, comparison/empirical_case). XMR/ZEC/DASH removed from Bittrex (announced 2021-01-01, effective 2021-01-15) — the FIRST US-exchange privacy-coin delisting, early node in the wave (Kraken/Huobi/OKX/Binance followed). offramp_cex observed_change/plausible (Bittrex stated no explicit reason). 2 semi_primary_wayback (CoinDesk + Decrypt), body_hash-pinned, verified. delta_hours 336 (announce->effective). audit_id 468. Corpus now 258 admitted.
