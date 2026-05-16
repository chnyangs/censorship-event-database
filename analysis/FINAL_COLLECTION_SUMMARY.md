# FINAL_COLLECTION_SUMMARY — 2026-05-16 lean-run multi-Phase pipeline

**Session date**: 2026-05-16
**Starting state**: 87 admitted events at `v0.2.0-rc-dryrun-3` (commit `8948e69`)
**Ending state**: 167 admitted events at `v0.2.0-rc-dryrun-9` (commit `eee9eeb`)
**Net delta**: **+80 admitted events** (92% growth) across 6 lean-run Phases and 6 DRYRUN sign-off cycles.

---

## Per-Phase event counts

| Phase | Frame | Discovery candidates | Authored | Net admitted | DRYRUN | Cumulative |
|-------|-------|---------------------|----------|--------------|--------|------------|
| **A** | comprehensive (us_federal_enforcement, corporate_policy, supranational, non_us_state) | 24+24+17+25 = 90 | 22 | +22 | -4 | 87 → 109 |
| **B** | historical_baseline 2013-2016 | 26 (7 P0 + 16 P1 + 3 P2) | 13 | +13 | -5 | 109 → 122 |
| **D** | DeFi + wallet + app-store + L3 RPC | 22 (13 P0 + 7 P1 + 2 P2) | 12 | +12 | -6 | 122 → 134 |
| **C** | China + Russia + CIS frames | 17 (12 P0 + 4 P1 + 1 P2) | 12 | +12 | -7 | 134 → 146 |
| **E** | pre-Bitcoin baseline 2008-2012 | 22 (10 P0 + 7 P1 + 5 P2) | 10 | +10 | -8 | 146 → 156 |
| **F** | Japan FSA + OFAC RA density | 15 (10 P0 + 3 P1 + 2 P2) | 11 | +11 | -9 | 156 → 167 |
| **Total** | | **192 candidates** | **80 admitted** | **+80** | 4→9 | **+92%** |

---

## Decision-gate verdicts (all 6 DRYRUNs)

Every Phase passed:
- Clean-tree status ✓
- `SOURCE_DATE_EPOCH`-pinned regeneration (exit 0) ✓
- Strict paper-readiness gate (`--strict-repro --strict-reliability --strict-null-audit --strict-audit --allow-soft-attribution --allow-dryrun-human-gates`): exit 0 ✓
- Byte-stable round-trip across 25 artifacts ✓
- **Verdict**: `SIGN-OFF READY` ✓

Three documented WARNs persist across all DRYRUN cycles (intentional pipeline-rehearsal markers, not blocking):
1. 12 null-denominator cases carry DRYRUN `last_human_audit` stamps (pipeline-rehearsal markers, not real human audit).
2. IRR `coder_provenance.mode = independent_human_dryrun_llm_simulated` (LLM-simulated reliability, not real independent-human reliability).
3. Attribution κ=0.5833 below 0.6 threshold (soft attribution gating: claims depending on attribution must stay at named-row / audit level).

---

## Agent-quality observations

### Net positive

1. **Schema convergence**: Each phase's authoring agents independently discovered the same enum constraints (target.kind=`entity`, target.enumeration=`subset`, observation_kind must be `observed_change`/`observed_no_change`/`coverage_gap`). Resolution time per phase dropped (Phase A agents ~6 min each; Phase F agents ~3 min each).

2. **Sibling-pattern learning**: Late-phase authoring agents proactively templated from prior-phase siblings (Phase F DMM agent referenced Phase A coincheck event; Phase F OFAC Gaza Now agent referenced Phase A aeza-group + Phase F sibling DMM-bitcoin). Cross-phase pattern transfer worked without explicit instruction.

3. **Honesty discipline preserved**: Zero invented body_hash. All citations marked `evidence_use: contextual_unarchived` where no real archive captured. All Phase A-F events at `status: draft` + `origin: agent_draft` per validator hard rule.

4. **Cross-phase deduplication**: Discovery agents consistently checked against `events/*.yaml` to avoid duplicates. Two duplicates flagged and skipped:
   - Phase C: `china-pboc-ten-agencies-crypto-illegal-2021-09` already covered by existing `china-pboc-crypto-ban-2021`.
   - Phase E: `egold-secret-service-indictment-2007-04` deferred (outside 2008-2012 tier).

### Surfaced issues (resolved)

1. **Kazakhstan L0 honesty downgrade** (Phase C): The `kazakhstan-internet-shutdown-mining-2022-01` agent initially coded `l0_network: partially_measured` based on NetBlocks/Cloudflare Radar/Access Now documentation, but the paper-readiness gate's `derived/l0_coverage_summary.csv` denominator-pinning constraint rejected this (no `sources/l0_datasets/<event>/` slice was captured this session). **Resolution**: Downgraded L0 to `not_measured`, removed L0 observation row and L0 recovery entry. L0 cascade evidence retained in `trigger.citation` block but not promoted to observation-row status. Event remains L1-anchored (KZ bitcoin hashrate collapse). Committed as `5e28a89`.

2. **Schema enum mismatches** (recurring across Phase A-F): Multiple agents specified enum values not in the schema:
   - `regulatory_enforcement` (not in trigger.type enum) → mapped to `nation_state_block` (for non-US regulators) or `fincen_action` / `sec_action` (for US-equivalent administrative flows).
   - `class_level` (not in target.enumeration enum) → mapped to `subset` with class-level rationale in `enumeration_note`.
   - `exchange` (not in target.kind enum) → mapped to `entity` + `actor_type` carrying the exchange-specific descriptor.
   - `contextual_baseline` (not in analysis_use enum) → mapped to `historical_baseline` (Phase B) or `discovery_ledger_only` (Phase E).
   - `case_study` (not in empirical_shape enum) → mapped to `comparison` or `null_event` based on observed_change count.
   - `S3_doj_sec_cftc_fiod` for non-US regulators → corrected to `S4_nation_state` per validator's stratum-actor map (S3 reserved for US DOJ/SEC/CFTC/FinCEN).

3. **anchor_case admission tier requirements**: `dydx-tornado-account-block-2022-08` qualified for anchor_case based on 2 distinct observation layers (l4_frontend + offramp_cex hybrid CEX architecture). All other agent_draft events admitted at `empirical_case` or `null_case`.

4. **Schema additions for previously-uncovered jurisdictions** (Phase C): HK, KZ, UA jurisdiction enums added to `schema/event.schema.json` + `schema/controlled_vocab.yaml` via authoring-agent edits.

---

## Layer coverage outcomes

Per-phase layer cascade documentation (approximate counts of `observed_change` rows by layer):

| Layer | Phase A | Phase B | Phase C | Phase D | Phase E | Phase F | Direction |
|-------|---------|---------|---------|---------|---------|---------|-----------|
| l0_network | 0 | 0 | 0 (KZ honesty-fix) | 1 (Infura geo-block) | 0 | 0 | Under-documented; needs real OONI capture |
| l1_consensus | 0 | 0 | 4 (CN mining + KZ hashrate) | 0 | 0 | 0 | Now populated via Phase C |
| l3_rpc | 1 | 0 | 0 | 3 (Infura geo, Cloudflare gateway, Metamask) | 0 | 0 | Now populated via Phase D |
| l4_frontend | 2 | 1 | 4 | 10 (DeFi+app-store cluster) | 2 (Amazon AWS + EveryDNS) | 0 | Phase D was load-bearing |
| asset_onchain | 6 | 1 | 1 | 1 (Aave Arc) | 1 (e-Gold) | 5 (OFAC wallet designations) | Continuously populated |
| offramp_cex | 18 | 11 | 8 | 5 | 7 (WikiLeaks blockade) | 11 (Japan FSA + OFAC) | Always best-documented |

**Net**: L4_frontend and L3_rpc cascade columns now have meaningful population; L0_network remains under-documented (1 row, awaiting real OONI capture for KZ + others); L1_consensus newly populated via Phase C CN mining + KZ hashrate cluster.

---

## Schema constraint summary (validator hard-rules surfaced across Phases A-F)

1. `status: draft` REQUIRED when `origin: agent_draft` (cannot admit LLM-authored events without human review).
2. `target.kind: entity` (no `exchange` / `regulatory_class` / `domain` outside specific cases).
3. `target.enumeration: subset` (no `class_level`).
4. `empirical_shape`: `comparison` (≥1 observed_change) | `null_event` (0 observed_change) — no `case_study`.
5. `observation_kind`: `observed_change` | `observed_no_change` | `coverage_gap` — no `not_observed`.
6. `observed_no_change` requires `attribution: none` + `window` + coverage `measured`/`partially_measured`.
7. `coverage_gap` requires `attribution` in `{unknown, none}`.
8. `not_measured` coverage cannot have observations on that layer.
9. `analysis_use`: `historical_baseline` | `comparable_analysis` | `discovery_ledger_only` — no `contextual_baseline`/`discovery_only`.
10. `trigger.type` enum strictly enforced — `regulatory_enforcement` NOT a valid enum (use `nation_state_block`/`fincen_action`/`sec_action`/`court_civil_order`/`corporate_policy_change`/`ofac_sdn_designation`/`supranational_regulation`/`doj_indictment`/`doj_seizure_order`).
11. Validator stratum-actor map: `S3_doj_sec_cftc_fiod` restricted to US DOJ/SEC/CFTC/FinCEN actors. Non-US regulators (JP FSA, KZ NBK, etc.) → `S4_nation_state` + trigger.type=`nation_state_block`.
12. **L0 coverage `partially_measured` / `measured`**: requires corresponding row in `derived/l0_coverage_summary.csv` derived from real `sources/l0_datasets/<event>/` slice. **Cannot bluff with documented-but-uncaptured measurement claims** (Kazakhstan-2022 lesson).
13. `wayback:` URL required on `primary_legal` source-type even with `evidence_use: contextual_unarchived` (year-prefix wildcard `https://web.archive.org/web/YYYY/<url>` acceptable).

---

## Remaining backlog (deferred candidates from triage manifests)

### Phase A (us_federal_enforcement, corporate_policy, supranational, non_us_state) backlog: ~68 candidates
- 7 P1/P2 us_federal_enforcement candidates not authored this round
- 11 P1/P2 corporate_policy candidates (smaller cascade)
- 7 P1/P2 supranational candidates (FATF/OECD/G20 updates)
- 13 P1/P2 non_us_state candidates (smaller-jurisdiction enforcement)
- Re-discoverable from `sources/{frame}/triage_manifest.json`.

### Phase B (historical_baseline 2013-2016) backlog: ~13 candidates
- 13 P1 deferred (mostly non-US-state advisories: Bolivia, Bangladesh, Indonesia, Argentina, Brazil, Thailand 2013 — many marked `needs_check` for archive pinning).
- DAO hack (2016-06-17) flagged as schema-edge case (chain-state intervention rather than censorship).

### Phase D (DeFi + wallet + app-store + L3 RPC) backlog: ~10 candidates
- 7 P1 deferred (dydx-tornado-account already admitted; remaining: ConsenSys/MetaMask Infura RPC data collection, Tornado Cash GitHub takedown, MakerDAO emergency shutdown contingency, Ren Protocol shutdown, Oasis Wormhole counter-exploit, Tornado Cash team self-block).
- 3 P2 deferred (Augur v2 US-UK geofence, pump-fun UK FCA geofence — verification deferred).

### Phase C (China + Russia + CIS frames) backlog: ~5 candidates
- 4 P1 deferred (China Weibo crypto-exchange purge, Russia DFA law 2020, Russia mining legalization law 2024-08, Ukraine virtual assets law already admitted).
- 1 P2 deferred (UK HMRC Bitcoin VAT brief 2014 — outside CIS frame, mis-routed).
- Belarus PR8 2017 explicitly deferred as permissive (not censorship-relevant).
- Multilingual scrapers identified as v0.3 infrastructure work.

### Phase E (pre-Bitcoin baseline 2008-2012) backlog: ~12 candidates
- 7 P1 deferred (e-Gold Secret Service indictment 2007-04 — outside tier; Liberty Reserve 2006-2012 ops — most events post-tier; BitInstant 2011-2013; Mt. Gox 2010-2011 early issues; Pecunix winding down 2008 — needs archive).
- 5 P2 deferred (DigiCash 1999 — outside tier; Iran sanctions correspondent severance 2012 — partially captured upstream).

### Phase F (Japan FSA + OFAC RA density) backlog: ~4 candidates
- 3 P1 deferred (Liquid Quoine post-hack orders 2021-08; bitFlyer suspension 2018-06 — partially captured in Phase F six-exchange sweep; Japan-only Tornado Cash designation 2022-12 — needs_check on METI/MOF primary).
- 2 P2 deferred (specific 2024 Lazarus sub-designations; OFAC USDT-on-Tron DPRK refresh 2024 — likely covered by existing `dprk-usdt-network-ofac-2025`).

**Estimated total backlog**: ~100-120 candidates surfaced but not authored in this lean run. Re-discoverable via `sources/{frame}/triage_manifest.json` cross-references.

---

## Critical path to v0.2.0 production release

The 6 lean-run Phases (A-F) preserved the **DRYRUN-discipline contract**: every authored event remains at `status: draft` + `origin: agent_draft`. To progress beyond DRYRUN to a real v0.2.0 release, the following human-required gates remain open:

1. **Human review of 80 new agent_draft events** (real human audit, not LLM-simulated). Promotion sequence:
   - Verify each event's primary URL is reachable and the legal/regulatory content matches the claim.
   - Pin real `body_hash` + `body_path` captures into `sources/http_captures/<slug>/` for primary_legal citations.
   - Run real OONI batch queries for L0-cascade events (KZ, infura-metamask-donetsk-luhansk, others) and pin measurement_ids.
   - Flip `evidence_use` from `contextual_unarchived` to `primary_archived` once body_hash anchored.
   - Flip `origin: agent_draft` → `human_reviewed` and `status: draft` → `admitted` after human audit pass.

2. **Real H1 IRR re-computation** with independent-human coders (not LLM-simulated). Current Cohen's κ (0.5833 attribution, 0.983 coverage_status) is from `independent_human_dryrun_llm_simulated` mode and does NOT satisfy paper-readiness for corpus-level comparative claims.

3. **12 null-denominator cases** require real human audit (currently carry DRYRUN `last_human_audit` stamps as pipeline-rehearsal markers): iran-ransomware-ofac-2018, irgc-ransomware-ofac-2022, lazarus-entity-ofac-2019, lazarus-laundering-ofac-2020, lockbit-leader-ofac-2024, matveev-ofac-2023, pertsev-nl-arrest-2022, russian-cybercrime-infra-ofac-2025, sichuan-silence-ofac-2024, sinbad-ofac-2023, storm-semenov-doj-2023, zservers-ofac-2025.

4. **Attribution κ codebook decision** (still open from prior session's H2 human-gate packet): resolve stablecoin-freeze attribution coding (`direct` vs `plausible` for Tether/Circle compliance freezes per OFAC SDN designation). κ=0.5833 indicates real codebook ambiguity, not just coding noise.

5. **5 H2 human-gates** from prior session still open (sec-v-uniswap-wells confirm reject; pertsev/storm-semenov scoped_claim review; offramp_cex.measured convention pick; attribution κ codebook decision; null-denominator real-audit).

---

## DRYRUN-discipline compliance audit

All 80 new events authored this session carry:
- **Status discipline**: `status: draft` ✓ (validator hard-rule)
- **Origin discipline**: `origin: agent_draft` ✓ (validator hard-rule paired with status=draft)
- **DRYRUN preamble** in `analysis_notes` ✓ (e.g., `**NEW EVENT AUTHORED - DRYRUN 2026-05-16** (Phase X of 2026-05-16 staged-release plan, ...)`)
- **Honest `evidence_use`**: `contextual_unarchived` everywhere — zero invented `body_hash` values ✓
- **Wayback discipline**: year-prefix wildcard URLs `https://web.archive.org/web/YYYY/<url>` to satisfy archive-anchor validator without bluffing pinned-snapshot capture
- **Tags**: `dryrun_2026_05_16` + `phase_{a|b|c|d|e|f}_2026_05_16` tags on all events for downstream grep filtering

These discipline markers ensure that a human reviewer can:
1. Audit all 80 LLM-authored events by greppping `tags: dryrun_2026_05_16`.
2. Validate that NO event was prematurely promoted to `status: admitted` without real human review.
3. Re-author / re-validate any event surgically without disturbing the rest of the corpus.

---

## Reproducibility

To replay this session's work from `8948e69` (Phase 6e DRYRUN-3, 87 events) → `eee9eeb` (Phase F wrap DRYRUN-9, 167 events):

```bash
git checkout 8948e69  # starting point, 87 events
git log --oneline eee9eeb...8948e69  # 24 commits to replay
# Each Phase: discovery commit + authoring commit + wrap commit (3 commits per Phase)
# Plus DRYRUN bump commits and one honesty-fix (Phase C kazakhstan L0 downgrade)
```

Each Phase's authoring is dispatched as **1 discovery agent + 10-13 parallel authoring agents + 1 consolidation step + 1 DRYRUN sign-off run + 1 commit**. The pattern is documented in `analysis/collection_plan_v0.2_to_v1.0.md`.

---

## Closing note

The DRYRUN-9 sign-off at `v0.2.0-rc-dryrun-9` represents the **pipeline-rehearsal terminal state** of the comprehensive lean-run collection plan. Six Phases × six DRYRUN cycles × 80 events × strict-gate byte-stable artifacts demonstrate that the pipeline scales to ~200-event corpus size without infrastructure work. The remaining backlog (~100-120 candidates) and the human-required gates (IRR, null-audit, body_hash captures) are the v0.3 → v1.0 work, not v0.2.

The pipeline rehearsal is complete. Next step is real human authoring/review, not more LLM agent rounds.

— Authored by LLM agent 2026-05-16 (Claude Opus 4.7 1M context) as the closing artifact of the Phase A-F lean-run multi-Phase pipeline. `status: draft` semantics apply to this summary too — please supersede with your own narrative on a real-release human audit.
