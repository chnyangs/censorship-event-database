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

### Tick 9 — 2026-05-31 03:38 Melbourne — focus: S4 nation-state census (registry, vocab-blocked era)
**+10 S4 registry rows** (deduped, scope+vocab tagged) — the under-collected 2013-2017 national-action era:
- **HARD BANS (censorship)**: china-pboc-bank-account-closure-2014-04 (AUTHORABLE, CN in-vocab; distinct from corpus 2013-12 notice), bangladesh-bb-2017 (AUTHORABLE, BD), vietnam-sbv-2014, ecuador-2014, jordan-cbj-2014, nepal-2017, morocco-2017, iraq-2017 (all VOCAB-BLOCKED -> morning author after ISO-code blessing).
- **SOFT WARNINGS (borderline)**: india-rbi-caution-2013 (soft precursor to the corpus 2018 hard ban), + an EU central-bank "not-currency" warning cluster (France/Norway/Belgium/Denmark 2013-14) -> context-only per scope.
**Dedup discipline:** caught internal gap-discovery dups (Jordan x2, Iraq x2, Bangladesh x2 -> single events each).
**Key for morning:** S4 is the largest gap (~106 cands) but mostly VOCAB-BLOCKED — bulk-add ISO-3166 codes (VN/EC/JO/NP/MA/IQ/CR/KE/LB/MX/NO/DK/...) then batch-author. A handful (CN/BD/IN) are already authorable. Hard-ban vs soft-warning tagging is ready to drive the scope decision. Registry now 39 rows.

### Tick 10 — 2026-05-31 04:08 Melbourne — focus: S4 census PREP (high-value analysis)
Rather than register 106 S4 rows one-by-one (the candidates file already lists them), produced **analysis/s4_census_prep.md** — the complete S4 roadmap for the morning:
- **Exact ISO-code additions** needed (~25: CR/DK/DZ/EC/EG/IQ/JO/KE/KH/KW/LB/LK/MA/MM/MX/NO/NP/PK/QA/SA/TN/TW/VE/VN/ZW) — the one additive controlled_vocab commit that unblocks the whole S4 census.
- **20 jurisdictions already authorable** (BD/BE/BO/CA/CN/FR/ID/IN/IR/JP/KG/KR/MY/NG/PH/RU/SG/TH/UA/US).
- **Dedup-density map** (US×9, CN×6, IN×5, ID×5, KR×5, NP×4, PK×4, TH×4 → multi-stage, dedup vs corpus).
- **Scope rule** (hard-ban=include vs soft-warning=context-only) + recommended workflow + templates.
- Estimate: **~50-70 net-new S4 events** after dedup+scope (of 106 candidates), weighted to 2013-2020.
**Judgment:** this single prep doc is worth more than 10 more registry rows — it converts the biggest gap into a morning batch-authoring plan gated only on your ISO-code + scope blessing. No event authored (analysis tick).

### Tick 11 — 2026-05-31 04:39 Melbourne — focus: S4 author (net-new, OONI-anchored)
**Authored 1 full event (validates [OK]):**
- **nigeria-binance-network-block-2024-02** (S4, comparable, comparison/empirical_case). Nigeria's Feb-2024 crackdown: NCC ordered telcos to BLOCK Binance/Coinbase/Kraken websites (l0_network — OONI-anchored, 4 NG binance.com measurements anomaly=True 2024-02-26..29, re-queried live) + detained 2 Binance executives (offramp_cex). 2-layer comparison, both observed_change/plausible. Sources OONI API (4 measurement_ids) + CoinDesk, body_hash-pinned. DISTINCT from corpus nigeria-cbn-crypto-ban-2021 (the 2021 banking ban). Structurally parallel to philippines-sec-binance-block-2024. audit_id 469. Corpus now 259 admitted.
**Note:** This is the high-quality S4 pattern — an OONI-measurement-anchored l0_network block (satisfies codebook §1.5 without OONI the l0 layer would be unadmittable). Many 2024 S4 nation-state blocks (e.g. India app-store, Pakistan, etc.) may have similar OONI anchoring — worth checking OONI per-event during morning S4 authoring.

### Tick 12 — 2026-05-31 05:09 Melbourne — focus: S4 dedup + distinct authorable cases
**+5 S4 registry rows** (dedup-disciplined):
- **DUP CAUGHT**: philippines-ntc-sec-binance-app-isp-block-2024-04 = corpus philippines-sec-binance-block-2024 (the OONI-anchored NTC ISP block I audited in C-5) -> DROP-as-dup.
- **NET-NEW AUTHORABLE** (in-vocab, dedup-noted vs corpus): indonesia-kominfo-social-account-block-2024-07 (the 2024 Instagram block — the kumparan source from my C-5 indonesia re-date belongs HERE), indonesia-bi-payment-prohibition-2018-01, philippines-bsp-vasp-moratorium-2022-09, canada-csa-pre-registration-exodus-2023-02 (relates to corpus kucoin-canada-exit-2023).
- Deduped 3 more internal gap-discovery dups (Indonesia-BI/Canada-CSA ×2 each).
**Judgment:** continued cross-checking candidates against corpus events I personally audited this session (Philippines/Indonesia/Canada Binance cases) — high-confidence dedup. These 4 distinct S4 cases are clean morning-author targets. Registry now 44 rows. No event authored (dedup/registry tick).

### Tick 13 — 2026-05-31 05:38 Melbourne — focus: consolidation (morning-review dashboard)
Endgame approaching (~1.4h to 7am). Checked OONI for indonesia-kominfo-2024-07 -> MIXED anomaly (the action was social-media-account blocking, not a clean website block) -> messy to author cleanly; left registered (author with care in morning).
Instead produced the high-value endgame deliverable: **analysis/MORNING_REVIEW_2026_05_31.md** — a single prioritized action plan consolidating: (A) the 3 decisions I need (scope-boundary, 2007-tier, ISO-codes) each with recommendation; (B) the gated bulk-authoring order (S4 ~50-70 first, then S1/S3/S6/S5); (C) the 5 events authored tonight to spot-check; (D) artifact index; (E) the dedup catches (philippines-ntc/infura-venezuela/huobi-2022 = corpus dups). This makes the morning review fast + mechanical once the 3 decisions are blessed.

### Tick 14 — 2026-05-31 06:08 Melbourne — focus: S6 author (clearest supranational censorship)
**Authored 1 full event (validates [OK]):**
- **eu-8th-package-russia-crypto-services-ban-2022-10** (S6, comparable, comparison/empirical_case). EU 8th sanctions package (2022-10-06): COMPLETE ban on crypto wallet/account/custody services to Russian persons, removing the 5th-package EUR 10k threshold. The clearest S6 supranational CENSORSHIP action (a direct legal prohibition — distinct from the soft FATF/IOSCO/FSB governance frameworks I tagged earlier). offramp_cex observed_change/direct, primary EU source + CoinDesk, body_hash-pinned, verified. audit_id 470. Corpus now 260 admitted.
**Note:** Later EU packages (18th 2025-07, 19th 2025-10, 20th 2026-04) expanded the crypto bans (registered) — author as distinct events in the morning. This 8th-package event sets the EU-sanctions template.

### Tick 15 — 2026-05-31 06:39 Melbourne — focus: validation sweep + EU-sanctions series (user "继续")
- **FULL VALIDATION SWEEP: 268 OK / 0 FAIL.** All 6 overnight-authored events + the whole corpus validate clean. Tally 260 admitted / 1 draft (ren) / 7 rejected. Git clean.
- Did NOT author BitFloor (only 1 cleanly-verified source near the deadline — left registered; thin for a dedicated event).
- **+3 EU-sanctions registry rows** (author-ready, EU in-vocab, template = the 8th-package event authored tonight): eu-5th-package-crypto-cap-2022-04 (the FOUNDATIONAL first EU crypto restriction), eu-18th-package-2025-07, eu-19th-package-a7a5-2025-10. These form a clean EU-sanctions-escalation series for fast morning authoring.
- User awake (~06:39). The 3 gating decisions (scope-boundary, 2007-tier, ISO-codes) in MORNING_REVIEW are ready — blessing them unblocks the big S4/S1 batch-authoring.

### RUN COMPLETE + DECISIONS EXECUTED — 2026-05-31 ~07:30 Melbourne (user awake, drove the decisions)
User woke ~06:40 and **blessed all 3 gating decisions** (enforcement-only scope · rename tier to 2007_2012 · add ISO codes). Executed immediately (no longer "deferred"):
1. **§9 inclusion boundary** added to codebook (enforcement-only: censorship actions IN; platform failures / fraud prosecutions / soft warnings OUT). Codebook 2.0.0 -> 3.0.0.
2. **temporal_tier renamed** discovery_only_2008_2012 -> discovery_only_2007_2012 (schema + validator + 4 scripts + 19 events). **e-gold 2007 indictment is now authorable.**
3. **+25 ISO-3166 codes** added to controlled_vocab.yaml (fixed the NO/Norway YAML-boolean trap). **S4 census (~106 cands, ~50-70 net-new) now unblocked.**
ALL 268 events validate (0 fail). Cron 1ddafe54 RETIRED (CronDelete) — user now driving interactively.

**Overnight final tally:** 6 events authored (254->260 admitted, corpus 262->268), 47-row registry, S4 roadmap, MORNING_REVIEW dashboard, codebook v3.0.0 with §9 scope rule. Next: bulk-author e-gold 2007 + the S4/S1/EU-sanctions batches now that schema is unblocked.

### Bulk-author WAVE 1 (S1 + S4 first 48) — 2026-05-31 morning (user launched workflow)
Workflow: 12 author agents (verified-draft authoring) -> adversarial verify (source real+on-topic? §9 scope? dup? validates?). 24 agents, ~1.74M tokens.
**Result: +36 verified-source census DRAFTS** (status: draft, awaiting admission audit):
- **25 KEEP** (clean): S1 OFAC (genesis-market, hanafin-huriya, chinyong-dprk, china-fentanyl, netex24-bitpapa, al-law-hezbollah, oko/kb-vostok drones, evil-corp, nemesis-parsarad, prince-group, dkba, media-land) + S4 hard-bans (webmoney-ukraine, jordan-cbj, china-pboc-2014-account-closure, ecuador-2014, kenya-2015, nepal-2017, vietnam-2017, algeria-2018, indonesia-bi-2018, pakistan-2018, zimbabwe-golix-2018).
- **11 FIX -> flagged with VERIFY-FLAG** (real designations/bans, but the captured press release does NOT contain the SPECIFIC crypto addresses claimed — those live in the SDN-list entry; refine source before admission): zheng-yan, task-force-rusich, wang-hongfei, botnet-911, tengyue, derakhshan-irgc, taiwan-fsc, iraq-cbi, morocco, cambodia, china-pboc-2019.
**The adversarial verify EARNED ITS KEEP — caught the C-5 fabrication risk:**
- **4 DROPPED** (deleted): fayzimatov + nordic-resistance (FABRICATED crypto nexus — the OFAC press release has ZERO crypto mention; these are terror designations the gap-discovery wrongly tagged as crypto), jordan-cbj dup, kyrgyzstan.
- **33 SKIPPED by authors** (§9 working): soft warnings / non-recognition statements (France/Norway/Lebanon/India-2013/Malaysia/Belgium/Mexico/Denmark/Russia-2014 "not currency" statements), dups, out-of-scope (Kimsuky espionage, Schumer-Manchin letter).
**Lesson confirmed:** parallel fresh agents OVERCLAIM crypto specifics (addresses/asset-types not in the captured source). The author-as-DRAFT + adversarial-verify + human-admission pattern is essential and works. Corpus now 305 events (261 admitted / 37 draft / 7 rejected).

### Bulk-author WAVE 2 (S4 remaining + S3 + S6) — 2026-05-31 (user: 继续 wave 2)
Workflow: 23 author agents (anti-fabrication rule strengthened) -> adversarial verify. 43 agents, ~2.67M tokens.
**Result: +42 verified census DRAFTS** (32 clean keep + 10 fix-flagged, after dedup). Corpus now 347 events (261 admitted / 79 draft / 7 rejected).
- **S4 (clean)**: myanmar-2020, egypt-194-2020, qatar-qfcra-2019, korea-fsc-privacy-delisting-2021, uae-sca-2020, sri-lanka-2021, thailand-meme-nft-2021 + thailand-payment-ban-2022, china-2021-cluster (search-engine block, alipay payment-channel block, NDRC mining elimination, FIU real-name shutdown), nepal-comprehensive-2021, taiwan-aml-vasp, argentina-bcra-2022, indonesia-kominfo-2024-07, iran-cbi-2024.
- **S3 (clean, §9 enforcement subset)**: SEC EtherDelta(first DEX)/TokenLot/Kik/LBRY/Poloniex/Nexo/Consensys/eToro/TradeStation/Abra, CFTC DeFi (Opyn/ZeroEx/Deridex), DOJ Cryptex/OKX-plea/Garantex, FinCEN Powers, + goldage-2006 (REVIEW-FLAG: pre-2007) + 1mdc-egold-freeze-2007.
- **S6 (clean, §9 mandating-only)**: BCBS SCO60, EU 16th/18th/19th/20th Russia sanctions crypto bans.
**§9 worked excellently — 88 SKIPPED**: India SC *reversal* 2020 (de-restriction!), Japan leverage cap (prudential), MUI fatwa (religious not state), Celsius/BlockFi US-state stratum-misfits (flagged for a US-enforcement stratum), soft governance (IOSCO/FSB), + many dups.
**Verify caught**: nigeria-binance-detention (DUP of my nigeria-binance-network-block-2024-02), kuwait/shapeshift/eu-tfr drops, egypt/argentina cross-batch dup-variants.
**Note for admission audit**: the 10 wave-2 fix-flags + 11 wave-1 fix-flags need source-refinement (specific addresses in SDN-list not captured press release) before admission. US-state enforcement (Celsius/BlockFi/Coinbase-state) surfaced as a stratum gap — consider an S7 or fold into S3.

### ADMISSION AUDIT + WAVE 3 (S5 corporate) — 2026-05-31 (continuation, user: 继续 / 不需要问我)
**Method upgrade — dry-run admission gating.** Lesson from an over-eager batch: source-content grep is
NOT enough for admission. Built a dry-run checker — simulate the draft→admitted flip in a temp file, run
`validate.py`, admit ONLY if it passes the strict admission floor (1 primary OR 2 independent semi-primary
groups; attribution=direct needs a primary; no placeholders; asset_onchain needs primary_onchain). Every
admission is validation-gated and auto-reverts on any failure, so no broken event is ever committed.

**+48 events admitted this continuation (corpus 261 → 309 admitted):**
- 6 genuine-review landmarks: eu-19th, eu-20th, SEC EtherDelta/LBRY/Kik/Poloniex.
- 2 S4 hard-bans that pass strict validation: nepal-comprehensive-2021, qatar-qfcra-2019 (+ thailand-payment-ban after placeholder reword).
- 38 waves-1/2 admission-ready drafts (passed adversarial-verify clean AND strict validation): e-gold-1mdc-2007, the OFAC SDN cluster (genesis-market/evil-corp/prince-group/media-land/nemesis/cryptex/garantex/netex24/al-law/chinyong/china-fentanyl/oko/kb-vostok/hanafin/dkba), SEC cease (consensys/nexo/etoro/tokenlot), CFTC DeFi (opyn/zerox/deridex), S4 (algeria/pakistan/kenya/indonesia-bi/sri-lanka/zimbabwe-golix/taiwan-vasp), S6 (eu-16th/eu-18th/bcbs-sco60), + webmoney-ukraine, bitfloor-debanking, blockfi-multistate, binance-dex-geoblock, okx-nigeria/india.
- 1 with honest evidence downgrade: coinbase-eu-usdt (direct→plausible — semi-primary only).

**Reverted/held (honest provenance — NOT admitted):**
- 17 fail-on-admit waves-1/2 drafts auto-reverted to draft. ~29 total drafts fail the admission floor
  because they carry only ONE supporting_journalism source (e.g. china-pboc-2014, vietnam-2017, ecuador-2014,
  jordan-2014, korea-fiu-2021, nepal-2017, argentina-2022, china-ndrc-mining, china-alipay-block, bitfinex-us-exit,
  thailand-meme-nft). These need a 2nd INDEPENDENT semi-primary source (or a pinned primary regulatory/exchange
  doc) before admission — genuine per-event research, NOT type-reclassification (reclassifying a CoinDesk article
  as semi_primary_wayback to clear the gate would be gaming the type system → refused).
- A few asset_onchain drafts need a primary_onchain tx_hash per §1.6: ren-protocol, circle-usdc-hack-freeze,
  circle-usdc-sealed-civil, tether-iran-fury-freeze.

**WAVE 3 (S5 corporate) — workflow still running at log time.** Stage-1 authored 26 S5 DRAFTS (committed as
status:draft, all validate): exchange jurisdiction-exits (binance NL/UK/nigeria-naira, bybit CA/FR, okx CA/india,
paxos CA, gemini NL, dydx-CA, okx-canada), stablecoin/MiCA delistings (binance-eea-usdt, crypto-com-eu-usdt,
etoro-ada-trx), frontend geofences (orca-dex, pancakeswap, poloniex-circle, binance-com-us, apple-uniswap-rejection),
privacy delistings (binance-monero, gate-io-perps, upbit-bithumb), asset freezes (tether-garantex, tether-okx-doj),
binance-palestinian-seizure, shapeshift-kyc. **HELD from admission pending the adversarial-verify stage verdicts**
(must not admit unverified wave-3 output). Will parse drop/flag/keep when the workflow completes, then dry-run-admit clean ones.

**Corpus state at log time: 385 events — 309 admitted / 69 draft / 7 rejected — sweep 384/384 validate [OK].**

### WAVE 3 (S5 corporate) FULLY PROCESSED + admission audit checkpoint — 2026-05-31
Wave-3 workflow completed (18 agents, ~1.44M tokens, 9 batches). Verdicts: **31 KEEP / 7 FIX / 14 §9-skipped**.
- **§9 scope held perfectly — 14 skipped, ZERO leaked to disk**: platform-FAILURE exclusions (Bitstamp-2015-hack,
  Cryptsy-insolvency, Bitfinex-2016-hack, WazirX-hack-freeze, Bittrex-Global-winddown), general-platform (GitHub
  OFAC), dups (OpenSea/MetaMask=already admitted, binance-canada=S4 dup, tether-voluntary=retroactive-sweep dup,
  tether-apac=second-wave dup, binance-europe-retreat=BaFin/FSMA dups), unverifiable (magic-eden standing-ToS, no
  dated action), MetaMask-Apple-removal (self-inflicted operational error, not Apple gatekeeping). All §9-correct.
- **13 admitted** (KEEP + pass strict validation, validation-gated genuine review): shapeshift-kyc, poloniex-circle,
  apple-uniswap-rejection, dydx-canada, binance-NL, gemini-NL, binance-hamas-freeze, binance-nigeria-naira, okx-india,
  gate-io-perps (Phase A) + binance-monero, tether-garantex, bybit-france (Phase B — see below).
- **Phase B — verifier OVER-FLAGGED 4 as FIX; I independently re-verified by rendering+grepping the pinned HTML.**
  binance-dex-29 (29-country list: US/Albania/Belarus/Iran/Cuba/Syria/Crimea/Venezuela/Zimbabwe/Kosovo ALL present —
  admission correct), binance-monero (Monero/XMR/Feb/30%/20-month/Aragon-ANT/Multichain-MULTI/VAI all present),
  tether-garantex (Tether/Garantex/USDT/27M/sanction/suspend present; asset_onchain honestly not_measured),
  bybit-france (core France-exit supported; AMF causal framing transparently flagged plausible-context per §1.1).
  Lesson: the adversarial verifier under-renders JS/HTML and over-flags — independent source-rendering is the tiebreak.
- **3 genuinely flagged (VERIFY-FLAG, kept draft):** bitfinex-us-exit-2017 (capture is a JS-gated React shell —
  body_hash matches but page has no article text; re-capture needed), circle-usdc-multichain-hack (mis-dated +
  §1.6 tx_hash), tether-iran-fury (§1.6 tx_hash).
- **~18 KEEP-but-under-threshold stay clean drafts** (verified on-topic but only 1 source / asset_onchain needs
  tx_hash): okex/upbit-privacy-delisting, upbit-bithumb, etoro-ada-trx, pancakeswap, binance-russia-gunmaker,
  okx/paxos/bybit-canada, binance-com-us, orca-dex, binance-uk, binance-palestinian, crypto-com/binance-eea-usdt,
  t3, tether-okx-doj, circle-usdc-sealed.

## SESSION-CONTINUATION TOTAL: corpus 261 → **322 admitted** / 56 draft / 7 rejected = 385 events; sweep 385/385 [OK].
**+61 admitted this continuation** (6 SEC/EU landmarks + 38 waves-1/2 + coinbase-eu + 13 wave-3 + 3 re-verified).
All local commits, never pushed. Method upgrade: dry-run admission gating + independent source-rendering tiebreak.

### REMAINING WORK (judgment-heavy — flagged for review, NOT auto-processed):
1. **~24 VERIFY-FLAG drafts** need per-event prose softening to match captured sources. OFAC ones (zheng-yan,
   wang-hongfei, task-force-rusich, tengyue, derakhshan-irgc, botnet-911): captured Treasury press releases
   support the designation + a Bitcoin/crypto nexus, but NOT every specific (e.g. zheng-yan source has "Bitcoin"
   but not "Litecoin"; the full address enumeration lives in the SDN-list entry). Fix = soften the unsupported
   specifics OR pin the SDN-list/Recent-Actions source, then admit. Sensitive sanctions prose — wants human audit.
2. **~32 under-threshold drafts** (1 supporting_journalism source) need a 2nd independent / primary source
   (national-bank circulars, exchange blogs) captured via Wayback before they clear the admission floor. Per-event
   research; Wayback availability for old/foreign gov docs is uncertain.
3. **US-state enforcement stratum** (Celsius/BlockFi/Coinbase-state) — S3/S4 misfit; needs a stratum decision.
4. **goldage-2006** pre-2007 boundary (REVIEW-FLAG).

### TASK 1 — VERIFY-FLAG refinement (user: 先做1) — 2026-05-31
Method: for each flagged draft, render+grep the captured HTML, check the specific against the source,
soften unsupported specifics to match evidence, remove the flag (its forbidden markers also blocked
admission), dry-run-admit (auto-revert on fail). Of 21 flagged drafts, 11 were "flag-only-blocked"
(had primary / 2+ semi-primary sources); the other 10 also fail the source threshold → fold into Task 2.
**+9 admitted (corpus 322 → 331):**
- 5 OFAC null_case: zheng-yan (first OFAC narcotics crypto designation — sm756 has Bitcoin not Litecoin →
  Litecoin re-attributed to SDN entry), wang-hongfei, tengyue, derakhshan-irgc, botnet-911 (specific
  literal-address/coin/count re-attributed to SDN-list entry; captured Treasury release supports the nexus).
- 4 non-OFAC: sec-tradestation + uae-sca-decision-23 (clean — generic flag over-cautious), fincen-eric-powers
  ($35,350 → FinCEN-assessment-doc attribution), sec-abra ($1.65M is a Jan-2025 final-judgment figure absent
  from the captured Aug-2024 release + mis-derived from a "1765" substring → softened to "civil penalty").
**2 held with corrected flags (NOT admitted — honest):**
- task-force-rusich: genuinely crypto (OFAC sanctioned 5 addresses: 2 BTC/2 ETH/1 USDT-TRON, ~$138k; CoinDesk/
  Chainalysis/TRM) BUT captured press release jy0954 contains ZERO crypto terms → needs a crypto-nexus source pinned.
- iraq-cbi: source is the genuine Arabic CBI page but titled "تحذير/WARNING" → §9 ban-vs-warning ruling needed.
**Tiebreak lesson reconfirmed:** the adversarial verifier over-flags (binance-dex, sec-tradestation, uae-sca all
checked out fully); independent source-rendering is the arbiter. But it also catches REAL overclaims (sec-abra
$1.65M, the SDN-entry-only specifics) — so every specific is grep-verified against the captured body, not trusted.

## SESSION-CONTINUATION RUNNING TOTAL: corpus 261 → **331 admitted** / 47 draft / 7 rejected = 385; sweep 385/385 [OK]. +70 admitted.

### TASK 2 — source-strengthening (user: Task 2 自动跑) — 2026-05-31
Built a repeatable pipeline: WebSearch primary → capture_http_artifact.py --wayback-submit → extract+grep
to VERIFY content → wire as primary into the observed_change observation → dry-run-admit (auto-revert).
**+2 admitted (corpus 331 → 333):**
- philippines-bsp: official BSP Memorandum **M-2022-035.pdf** (primary_government, PDF text verified, Wayback-archived).
- argentina-bcra: official BCRA **Comunicación A-7506.pdf** (primary_government, Spanish text verified, Wayback-archived).
**YIELD PATTERN (important for the long tail):** the capture approach works ONLY for events whose primary is a
non-bot-protected official English/standard-URL document:
- ✅ Government static pages / PDFs on standard URLs (BSP, BCRA) — clean 200 + archivable.
- ❌ Major-exchange announcement pages (Binance EEA-USDT) — JS-gated, returns 202 + EMPTY body (sha256 of "").
- ❌ Bot-protected gov sites (Korea FSC) — connection reset on direct fetch.
- ❌ Foreign-language gazette / commentary-only (Thailand SEC KorThor 18/2564, Indonesia Kominfo) — searches
  return only law-firm commentary + journalism (supporting_*, which do NOT count toward the admission floor).
**Implication:** of the ~37 under-threshold drafts, only a minority have cleanly-capturable primaries. The bulk
are well-documented single-source national bans (china-2014/vietnam/ecuador/jordan/nepal/morocco/taiwan-2014/
egypt/myanmar/venezuela/iran/the China cluster) whose primaries are old/dead/foreign-gazette or only covered by
journalism. Pure per-event capture for these is low-yield + token-expensive. Cheap-win check (assign distinct
evidence_group_ids to existing independent semi-primary sources) found NONE — morocco/taiwan each have only 1
semi-primary in the observation. 5 more need a primary_onchain tx_hash (different fix). Decision point surfaced to user.

## RUNNING TOTAL: corpus 261 → **333 admitted** / 45 draft / 7 rejected = 385; sweep 385/385 [OK]. +72 admitted this continuation.

### TASK 2 (cont.) — per-event capture, user: 继续 capture 慢慢跑 — 2026-05-31
+1 admitted (corpus 333 → 334): **ecuador** — official Código Orgánico Monetario y Financiero PDF
(primary_legal, 156pp, full text grep-verified: se prohíbe / no autorizado / medios de pago / curso legal /
dólar / junta de política; attribution=plausible, Code doesn't name bitcoin). Wayback-archived.
**Refined yield rule: only official PDFs on standard URLs capture reliably.**
- ✅ Worked (3): philippines-bsp (BSP M-2022-035.pdf), argentina-bcra (A-7506.pdf), ecuador (COMF.pdf) — all direct PDFs.
- ❌ china-pboc-2014: found the correct pbc.gov.cn URL for notice 银发[2013]289号, but the page is a JS stub
  (rendered 490 chars — 比特币/289 present but the notice body absent) + Wayback submit timed out. Chinese gov
  HTML pages don't capture. STAYS DRAFT.
- ❌ Confirmed-hard: korea-fsc/fiu (bot-block reset), binance (JS-gated empty body), thailand/indonesia/egypt/
  nepal (searches return only law-firm commentary + journalism; no clean PDF/standard-URL primary surfaced).
**Task-2 tally this session: +3 admitted (philippines, argentina, ecuador) via official-PDF capture.** The remaining
~34 under-threshold drafts mostly lack a clean capturable PDF primary — they need either (a) patient per-event
hunting for an existing Wayback snapshot / a PDF mirror of the foreign-language law, or (b) the lower-admission-tier
methodology. Per user, continuing the slow capture route as PDF primaries are found; this is an ongoing background effort.

## RUNNING TOTAL: corpus 261 → **334 admitted** / 44 draft / 7 rejected = 385; sweep 385/385 [OK]. +73 admitted this continuation.
