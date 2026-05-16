# Comprehensive collection plan v0.2 → v1.0 (~600 events, 18 months)

> Plan generated 2026-05-16 in response to user request "帮我制定一个 plan,
> 我需要一个 comprehensive 的 events collection". User-confirmed scope:
> ~600 events including pre-Bitcoin baseline; solo maintainer + LLM agents;
> DRYRUN-discipline preserved; paper and dataset tracked as equal-priority
> deliverables.

## Starting state (2026-05-16)

- **87 events on disk** (83 admitted + 3 draft + 1 rejected)
- 6 source frames defined; **1 ingested** (OFAC RA), **5 planned**
- 47 screened-out (rejected) stubs with `triage_notes`
- v0.2.0-rc-dryrun-3 sign-off ready; pipeline green
- 5 H2 human gates still open (~80 min budget to clear)
- DRYRUN-discipline established + reverting plan documented

## Target end-state (v1.0)

- **~600 admitted events**, geographically + temporally comprehensive
- 6 source frames **all ingested** + 3 new non-English frames live
- DeFi-protocol-governance + wallet/app-store layers in scope
- Pre-Bitcoin (2008-2012) baseline grounded with explicit scope rules
- Real (non-DRYRUN) `last_human_audit` on every paper-cited event
- Real `independent_human` IRR pass for paper-readiness
- Paper-table generator + 6-layer admission protocol unchanged
- Coverage estimate (per stratum): ~70-85% of well-documented major actions

## Critical scoping decisions (made by user before this plan)

1. **Pre-Bitcoin (2008-2012)**: in scope. Includes payment-rail-Wikileaks actions, e-Gold 2007 DOJ, Liberty Reserve 2013-05, Mt. Gox 2014 bank-account freezes. Pre-Bitcoin events require a clear scoping rule (see Phase E).
2. **Non-English**: in scope. Top-3 languages by enforcement-activity volume: Chinese, Russian, Japanese. Korean / Spanish / Portuguese deferred to v1.1.
3. **DeFi / wallet / app-store**: in scope. New source-frame design needed.
4. **DRYRUN markers**: preserved throughout. Only real human audit can flip to non-DRYRUN.
5. **Paper + dataset**: equal-priority. Each phase has a paper-table impact assessment.

## Capacity budget (solo maintainer + LLM agents)

- **Maintainer time**: ~5h/week real human audit + decision-making.
- **At ~15 min / event for real audit**: ~20 events / week audited. Over 78 weeks (~18 months) → ~1560-event audit capacity. **Audit is NOT the bottleneck**.
- **The real bottleneck**: source-frame infrastructure (multilingual scrapers, OONI/Censored Planet pulls, custom YAML authoring). Each new source frame is 1-2 weeks of setup work.
- **Per-event agent cost**: ~30 min wall-clock per agent including review. Parallel batches of 10-20 agents/wave is sustainable.

## Phase outline (78 weeks total)

| phase | weeks | scope | events added | corpus end | paper deliverable |
| ---: | ---: | --- | ---: | ---: | --- |
| A | 1-12 | Ingest 4 planned source frames | +90-110 | ~190 | IMC 2027-1 (Mar): submission decision |
| B | 13-24 | 2013-2016 historical baseline completion | +40-60 | ~240 | IMC 2027-1 submission (if A on-track) |
| C | 25-36 | Non-English: Chinese + Russian | +80-100 | ~330 | IMC 2027-2 (Aug): submission |
| D | 37-48 | DeFi / wallet / app-store layer | +70-90 | ~410 | AFT 2027: secondary submission |
| E | 49-60 | 2008-2012 pre-Bitcoin baseline | +40-60 | ~460 | extension paper / dataset paper |
| F | 61-72 | Density passes + Japanese frame + real IRR | +100-120 | ~570 | v1.0 dataset paper |
| G | 73-78 | v1.0 release + DRYRUN-revert | 0 | ~570-600 | venue retargeting |

Total: ~480-560 new events admitted. End-state ~570-600 admitted, consistent with the user's ~600 target.

---

## Phase A · Source-frame ingestion (weeks 1-12, ~3 months)

**Goal**: convert the 4 `planned:` source frames to `ingested:` artifacts.
**Events added**: +90-110.
**Corpus at end**: ~190 admitted.

### A.1 us_federal_enforcement (weeks 1-3)

Build ingestion for DOJ press-room + SEC press-releases + CFTC press-releases + FinCEN news + CourtListener / RECAP. Target: ~40 candidate stubs.

- Source artifact: `sources/federal_enforcement/triage_manifest.json`
- Scraper: `scripts/ingest_us_federal_enforcement.py` (DRYRUN-friendly; output structured JSON manifest)
- Per-stub manual triage (~5 min each) → ~25-30 promotions

### A.2 corporate_policy (weeks 4-5)

Build ingestion for exchange blog RSS feeds + issuer press releases + Wayback CDX for exchange/issuer corporate-policy URLs.

- Source artifact: `sources/corporate_policy/triage_manifest.json`
- Scraper: `scripts/ingest_corporate_policy.py`
- Initial blog feeds: Binance, Coinbase, Kraken, Bitstamp, Bitfinex, Tether, Circle, OKX, Paxos, Gemini, BitGo, Fireblocks, Anchorage Digital — 13 feeds, RSS-based
- Target: ~30 stubs → ~20 promotions

### A.3 supranational (weeks 6-7)

EUR-Lex bulk download for crypto-related regulations + FATF document repo + UN Security Council 1267 designations + G7 communiqués.

- Source artifact: `sources/supranational/triage_manifest.json`
- Scraper: `scripts/ingest_supranational.py`
- Target: ~15 stubs → ~10 promotions

### A.4 non_us_state (weeks 8-10)

Manual curation per jurisdiction (Russia, Brazil, India FIU, UK HMRC, Australia AUSTRAC, Singapore MAS, Hong Kong SFC, Korea FSC, Japan FSA, Israel ISA, Switzerland FINMA, UAE VARA, France AMF, Germany BaFin). Per-jurisdiction press-release index + Wayback.

- Source artifact: `sources/non_us_state/triage_manifest.json`
- Scraper: `scripts/ingest_non_us_state.py`
- Target: ~50 stubs → ~30-35 promotions

### A.5 Phase A consolidation (weeks 11-12)

- Bulk-promote agent dispatch (parallel waves of 10-15 each)
- Real `last_human_audit` pass on top-30 events for paper-readiness
- Phase-A REVIEW_AGGREGATE.md
- v0.3.0-rc-dryrun-4 sign-off

### Paper-table impact at end of Phase A

- C1 layer rates: stabilize as more strata fill in. asset_onchain retraction holds; L4/L1 sensitivity may resolve toward middle of range.
- C2 single-layer dominance: still PARKED on observation_kind κ (real IRR pass not done yet)
- Table 7 jurisdictional composition: US-share drops from 75% → ~55-60%
- new admitted events ~half historical-baseline-eligible per A.4

### Phase A decision gate

End of week 12: check whether
- (a) all 4 frames are truly ingested (artifact files exist + manifest validates)
- (b) coverage reaches >150 events
- (c) Phase A consolidation REVIEW_AGGREGATE shows no fatal frame defect

If yes → proceed to Phase B. If no → extend Phase A by 2-4 weeks, defer Phase B.

---

## Phase B · 2013-2016 historical baseline completion (weeks 13-24)

**Goal**: fill the 2013-2016 historical_baseline tier from 13 → ~35-40 events.

**Events added**: +40-60.
**Corpus at end**: ~240 admitted.

### B.1 Known-named-event drafting (weeks 13-18)

LLM-agent drafts for already-named gaps:

- **2013**: Liberty Reserve 2013-05, BitInstant 2013 (pre-Shrem charges), Mt. Gox 2013-05 DHS Dwolla seizure, Bitcoin Foundation 2013 NY subpoena
- **2014**: Mt. Gox 2014-02 bankruptcy + bank-account-freeze cascade, Coin.MX 2014 indictment, Bitcoin Magazine NY-exit cascade
- **2015**: NYDFS BitLicense first-applicant decisions, FinCEN MSB-registration crackdown (~10 events)
- **2016**: BitLicense year-1 follow-on actions, MTGox creditor proceeding milestones

Target: ~30 named-event drafts dispatched in 2 waves of 15 agents.

### B.2 Source-frame-driven discovery (weeks 19-22)

Run the now-ingested `us_federal_enforcement_archives` ingestion against 2013-2016 specifically. Triage the ~30-50 new candidate stubs.

### B.3 Phase B consolidation (weeks 23-24)

- Real human audit on top-15 historical events
- Paper-claim review: does the historical baseline now defensibly support "the regulatory landscape was already this active in 2013-2016"?
- v0.3.1-rc-dryrun-5 sign-off

### Paper-table impact

- Table 1 case roles: historical_baseline tier moves from 13 → 35-40 (substantial)
- Paper §3 motivation: stronger "the censorship surface predates the OFAC era" argument

### Phase B decision gate

End of week 24: corpus ~240 events; **IMC 2027-1 deadline check (typically Mar 25)**. If corpus + paper-claims are submission-ready → submit. If not → defer to IMC 2027-2 (Aug).

---

## Phase C · Non-English expansion (weeks 25-36, ~3 months)

**Goal**: add Chinese + Russian source frames as truly-ingested, capture the 2017-2025 non-English enforcement window.

**Events added**: +80-100.
**Corpus at end**: ~330 admitted.

### C.1 Chinese-language frame (weeks 25-30)

- New source frame: `chinese_state_archives` (PBOC + 公安部 + 中央网信办 + provincial 公安 + SPC court rulings)
- Scraper: `scripts/ingest_chinese_state.py` — uses PBOC press-release archive + gov.cn search + Chinese Wayback (zhongwen.archive.org / archive.org with zh-CN URLs)
- Translation: agent-driven Chinese → English for triage_notes; original Chinese preserved in source body_path
- Coverage: 2013 PBOC + 2017 ICO ban + 2021 PBOC + ~30 provincial-level actions
- Target: ~30-40 events

### C.2 Russian-language frame (weeks 31-34)

- New source frame: `russian_state_archives` (Центробанк России + Roskomnadzor + FSB / FSO + Russian Federation court rulings)
- Scraper: `scripts/ingest_russian_state.py`
- Coverage: post-2022 sanctions-evasion enforcement, VTB rulings, 2024 ruble-payment-blocks
- Target: ~25-35 events

### C.3 Phase C consolidation (weeks 35-36)

- Real human audit on top-20 non-English events (requires the maintainer to actually read Chinese/Russian source bodies)
- IRR pass with multilingual codebook extensions
- Paper-claims update: sampling frame statement no longer says "English-indexable only" if confidently
- v0.4.0-rc-dryrun-6 sign-off

### Phase C decision gate

End of week 36: language extension truly worked vs. degraded to mostly-translation-quality issues. If quality is acceptable → continue. If not → roll back the non-English claims and document the failed expansion.

---

## Phase D · DeFi / wallet / app-store layer (weeks 37-48, ~3 months)

**Goal**: new source-frame designs for previously-uncovered substrates.

**Events added**: +70-90.
**Corpus at end**: ~410 admitted.

### D.1 DeFi protocol governance frame (weeks 37-40)

- New source frame: `defi_protocol_governance_archives`
- Targets: Compound proposal repo, Aave governance forum, MakerDAO governance, Uniswap governance, Lido governance, Curve DAO, Synthetix Spartan Council
- Capture: governance-vote-result + frontend-removal events
- Target: ~25-30 events

### D.2 Wallet / app-store frame (weeks 41-43)

- New source frame: `wallet_app_store_archives`
- Targets: Apple App Store removals, Google Play removals, MetaMask phishing blocklist activity (per `analysis/operator_census/`), Phantom, Coinbase Wallet, Rabby, Trust Wallet
- Coverage: regional app-store unavailability events + wallet-level token-removal events
- Target: ~25-30 events

### D.3 Stablecoin issuer autonomous freezing (weeks 44-46)

- New source frame slot under `corporate_policy_archives` (no new frame, just extended): Tether / Circle autonomous (non-OFAC-triggered) blacklist events on Etherscan / Tronscan
- Capture: autonomous-freeze tx_hash + corporate communication
- Target: ~15-25 events (Tether's pig-butchering sweep series, Circle's "lost funds" recovery freezes)

### D.4 Phase D consolidation (weeks 47-48)

- Real human audit on top-20 DeFi/wallet events (these require Etherscan domain expertise)
- Paper-claims expansion: 6-layer model may need a 7th layer for "smart-contract governance" or remain at 6 with DeFi events admitted as L4 + L_governance subtype
- v0.4.1-rc-dryrun-7 sign-off

### Phase D decision gate

End of week 48: did the 6-layer model survive DeFi expansion? Or did the schema need a 7th layer? Document either way.

---

## Phase E · 2008-2012 pre-Bitcoin baseline (weeks 49-60, ~3 months)

**Goal**: extend the temporal frame to truly include 2008-2012, with explicit scoping rules for pre-Bitcoin events.

**Events added**: +40-60.
**Corpus at end**: ~460 admitted.

### E.1 Scoping rules (week 49)

Pre-Bitcoin events must satisfy one of:
1. **Direct precursor**: the enforcement target is a Bitcoin or virtual-currency vehicle (Liberty Reserve 2013, Mt. Gox 2013, BitInstant 2012, even though Liberty Reserve was 2013-05, its predicate acts began 2010-2012)
2. **Payment-rail-Bitcoin nexus**: a payment-rail action that targeted Bitcoin-adjacent activity (PayPal-Wikileaks 2010, Visa/MasterCard-Wikileaks 2010, Western Union to specific Bitcoin-related fiat-conversion shops)
3. **Foundational**: e-Gold 2007 DOJ (pre-Bitcoin proper, but it's the canonical "digital-currency-as-money-transmitter" precedent and is cited in every subsequent crypto enforcement)

Out of scope: general fraud cases unrelated to virtual-currency vehicles (e.g. unrelated Ponzis from 2008-2010); pre-2007 events.

Update `docs/methodology.md §3` with the pre-Bitcoin scoping rules.

### E.2 Author the known 2008-2012 events (weeks 50-56)

- e-Gold 2007 DOJ + 2008 plea agreement
- Liberty Reserve precursor acts 2010-2012 + 2013-05 takedown
- PayPal-Wikileaks 2010 + Visa/MasterCard-Wikileaks 2010
- BitInstant 2012 launch + early compliance posture
- Mt. Gox 2010-2012 pre-bankruptcy bank-account events
- E-currency closure cascades 2009-2011 (Pecunix, GoldMoney intermediaries)
- FBI Bitcoin reports 2012-2013 (intelligence-bulletin events)

Target: ~30 events.

### E.3 Phase E consolidation (weeks 57-60)

- Real human audit on every 2008-2012 event (these are paper-critical; need pristine evidence)
- Paper-claims update: explicit pre-Bitcoin scoping rule paragraph in §0
- v0.5.0-rc-dryrun-8 sign-off

### Phase E decision gate

End of week 60: are the pre-Bitcoin events defensible? Or are they too thin / too speculative? Document the boundary.

---

## Phase F · Density passes + real IRR + Japanese frame (weeks 61-72, ~3 months)

**Goal**: deepen coverage within already-covered strata; clear all H2 human gates; conduct real `independent_human` IRR; add Japanese language frame as the 3rd non-English.

**Events added**: +100-120.
**Corpus at end**: ~570 admitted.

### F.1 OFAC RA density pass (weeks 61-64)

- Re-run OFAC RA ingestion at full coverage (currently 26 admitted from ~50-60 in-frame crypto-target actions 2017-2025)
- Target: every OFAC RA with crypto target gets a draft → admission decision
- Add: ~20-25 events

### F.2 Japanese frame (weeks 65-68)

- New source frame: `japanese_state_archives` (金融庁 + 国税庁 + Japanese court system)
- Coverage: Coincheck 2018 hack + 業務改善命令 cascade, Mt. Gox civil rehabilitation milestones, FSA crypto-licensee de-registrations
- Target: ~20-30 events

### F.3 Real `independent_human` IRR (weeks 69-70)

This is the critical paper-readiness gate. Maintainer:
- Recodes 90 coverage_status + 25 observation_kind + 20 attribution rows blind
- After a 60-day gap from the last LLM IRR (so no recall contamination)
- Updates `coder_provenance.mode: independent_human`
- Re-runs `compute_irr_kappa.py`
- If `attribution κ ≥ 0.6`: drop the `--allow-soft-attribution` flag from release_signoff
- If `attribution κ < 0.6`: tighten the codebook OR keep the named-row-only retraction permanent

### F.4 Clear all H2 human gates (week 71)

The 5 outstanding H2 gates from `analysis/null_audits/H2_HUMAN_GATES.md` (~80 min real work) all get human decisions. DRYRUN markers replaced with real audit stamps.

### F.5 Phase F consolidation (week 72)

- v0.6.0-rc-dryrun-9 sign-off
- Drop all `--allow-dryrun-human-gates` flags (real human audits now present)
- Paper-claims final pass

---

## Phase G · v1.0 release (weeks 73-78, ~6 weeks)

**Goal**: real (non-DRYRUN) v1.0 release.

### G.1 DRYRUN-revert sweep (weeks 73-74)

Per `analysis/release_signoff/DRYRUN_REVERT_PLAN.md`:
1. Every `last_human_audit` DRYRUN marker → real human-verified audit
2. `coder_provenance.mode: independent_human_dryrun_llm_simulated` → `independent_human`
3. CITATION.cff version bump to `1.0.0` + real date
4. All `**DRYRUN` markers in `analysis_notes` removed (replaced with real audit-trail blocks)

### G.2 Release sign-off (weeks 75-76)

- `make regenerate` clean
- `make paper-check --strict-repro --strict-reliability --strict-null-audit --strict-audit` — NO `--allow-*` flags
- byte-stability round-trip
- v1.0 sign-off log

### G.3 Tag + push + Zenodo DOI (week 77)

Maintainer-only actions (the script never does these):
- `git tag -a v1.0 -m "..."`
- `git push origin main --tags`
- Wait for Zenodo to mint DOI
- Update CITATION.cff with DOI back-reference if needed

### G.4 Paper submission window (week 78)

- IMC 2028-1 deadline (typically Mar) OR AFT 2027 / 2028 venue retargeting decision
- Submission packet: PDF + supplementary materials + Zenodo DOI

---

## Risk register

| risk | mitigation |
| --- | --- |
| Non-English frame quality degrades | Phase C decision gate; rollback if quality unacceptable |
| OFAC artifact ingestion breaks (Treasury.gov API change) | Backup CSV-based ingestion + Wayback fallback per source frame |
| LLM agent rate-limits hit during bulk waves | Sequential batching; user-configurable concurrency in scripts |
| Pre-Bitcoin events fail admission criteria | Phase E scoping rule + explicit boundary documentation |
| Real human IRR fails (attribution κ < 0.6 even with tighter codebook) | Permanent named-row-only retraction; paper §3 acknowledges as v1.0 limitation |
| Maintainer time slips below 5h/week | Phase-end checkpoint; extend timeline rather than cut scope |
| IMC reviewers reject "dataset paper" framing | AFT secondary submission; v1.1 retarget |
| Schema needs breaking changes (7th layer for DeFi governance) | Schema v0.3 bump in Phase D; backward-compat migration script |
| `agent_draft → admitted` schema check breaks more often | Validator already enforces — accepted as healthy gate |
| Non-English Wayback CDX coverage thin | Captureanchor + body_hash on local mirror; document the gap |

## Decision points

| decision | when | options |
| --- | --- | --- |
| Submit IMC 2027-1 (Mar) or defer to 2027-2 (Aug) | end of week 24 | Submit if corpus ≥ 220, paper-claims pass, IRR ready |
| Continue or roll back non-English Phase C | end of week 36 | Continue if event-quality matches English baseline; roll back to "future work" otherwise |
| Schema v0.3 bump (7th layer) or stay 6-layer | end of week 48 | Bump if DeFi governance can't fit cleanly in L4 |
| Pre-Bitcoin scope rule final | end of week 60 | The 3-rule scope from §E.1 or a tighter / looser variant |
| Real release v1.0 vs defer for v1.1 expansion | end of week 72 | Release if all H2 gates cleared + real IRR done; defer if anything still DRYRUN |

## Infrastructure deliverables

New scripts under `scripts/`:

- `ingest_us_federal_enforcement.py` (Phase A.1)
- `ingest_corporate_policy.py` (Phase A.2)
- `ingest_supranational.py` (Phase A.3)
- `ingest_non_us_state.py` (Phase A.4)
- `ingest_chinese_state.py` (Phase C.1)
- `ingest_russian_state.py` (Phase C.2)
- `ingest_japanese_state.py` (Phase F.2)
- `ingest_defi_governance.py` (Phase D.1)
- `ingest_wallet_app_store.py` (Phase D.2)
- `enrich_ofac_ra_density.py` (Phase F.1)
- `multilingual_codebook_check.py` (Phase C/F)

Each script writes a structured triage manifest JSON. Manifest schema documented in `docs/source_frame_ingestion.md` (to be authored at start of Phase A).

## Per-phase commit + revert pattern

Each phase produces a single milestone commit + DRYRUN sign-off log:

```
git log --oneline (target shape):
  v1.0           — Phase G real release (DRYRUN markers reverted)
  v0.6.0-rc-9   — Phase F dryrun (real IRR + density)
  v0.5.0-rc-8   — Phase E dryrun (2008-2012 added)
  v0.4.1-rc-7   — Phase D dryrun (DeFi/wallet/app-store)
  v0.4.0-rc-6   — Phase C dryrun (Chinese + Russian)
  v0.3.1-rc-5   — Phase B dryrun (2013-2016 fill)
  v0.3.0-rc-4   — Phase A dryrun (4 planned frames ingested)
  v0.2.0-rc-3   ← we are here
```

Each commit is selectively revertable.

## Paper-table tracking

Each phase produces a `analysis/paper_tables_snapshots/v0.X.md` capturing C1/C2/C3/Table1/Table7 values at that snapshot. Comparison across snapshots shows the corpus-shape evolution. Submission decision uses the latest snapshot's stability.

## What this plan does NOT promise

- Population-comprehensiveness. 600 events is **comprehensive within the explicit sampling frame**, not "every event that ever happened". The paper's §0 sampling frame statement remains the boundary.
- Real-time monitoring. The maintainer reviews quarterly; new events post-2026-12 are not in v1.0 scope unless triggered during a phase consolidation.
- DeFi governance schema certainty. Phase D may force a schema v0.3 bump. If so, v1.0 includes both v0.2 and v0.3 records with a migration document.
- Comprehensive non-English. Only Chinese, Russian, Japanese. Korean / Spanish / Portuguese / Arabic are v1.1.

## v1.0 deliverable summary

- **Dataset**: ~570-600 admitted events, 9 source frames (4 + 5 new), 47+ rejected tombstones, ~80 promoted_to_event tombstones, 1 retirement policy. Zenodo DOI. CC-BY-4.0 + MIT.
- **Schema**: v0.2 or v0.3 (TBD per Phase D)
- **Paper-table generator**: 7+ tables; admission protocol; fail-closed; byte-stable under `SOURCE_DATE_EPOCH`
- **IRR**: real `independent_human` pass on 3 variables; κ ≥ 0.6 floor enforced or named-row-only retraction documented
- **Reproducibility**: Docker container, pinned base image digest, CI runs full regenerate
- **Paper**: 1-2 manuscripts targeting IMC 2027-1 / IMC 2027-2 / AFT 2027 / AFT 2028

---

## Immediate next-action (week 1 of Phase A)

1. Author `scripts/ingest_us_federal_enforcement.py`. Initial scope: scrape DOJ press-releases + SEC press-releases + CFTC press-releases for 2017-2025 + filter for crypto-target keywords. Output: structured JSON manifest at `sources/federal_enforcement/triage_manifest.json`.
2. Run the ingestion. Triage the resulting ~30-40 candidate stubs (LLM agent first-pass + maintainer 5-min-per-stub review).
3. Dispatch 5-8 parallel agents for the top stubs (the ones the maintainer marked promote-eligible).
4. Commit Phase A.1 as `Phase A.1 — us_federal_enforcement frame ingested + N events promoted`.

If user agrees with this plan as drafted, **start week 1 next session**.
