# FINAL_COLLECTION_SUMMARY — 2026-05-16/17 lean-run + Wave 2 collect-all-first

**Session window**: 2026-05-16 to 2026-05-17
**Starting state**: 87 admitted events at `v0.2.0-rc-dryrun-3` (commit `8948e69`)
**Ending state**: 262 events at `v0.2.0-rc-dryrun-11` (commit `86a9859`)
**Net delta**: **+175 events (+201% growth)** across 10 lean-run Phases + 11 DRYRUN sign-off cycles.

---

## Two-stage workflow

The session ran a deliberate two-stage workflow, validating both `lean-run-then-audit` and `collect-all-then-audit` strategies:

**Stage 1: Lean-run Phases A-F (2026-05-16)** — 87 → 167 (+80 events)
- Phase A: comprehensive 4-frame discovery + 22 P0 authored (87 → 109; DRYRUN-4)
- Phase B: historical_baseline 2013-2016 — 13 events (109 → 122; DRYRUN-5)
- Phase D: DeFi + wallet + app-store + L3 RPC — 12 events (122 → 134; DRYRUN-6)
- Phase C: China + Russia + CIS frames — 12 events (134 → 146; DRYRUN-7)
- Phase E: pre-Bitcoin baseline 2008-2012 — 10 events (146 → 156; DRYRUN-8)
- Phase F: Japan FSA + OFAC RA density — 11 events (156 → 167; DRYRUN-9)

**Upstream protection checkpoint (2026-05-17)** — DRYRUN-10 at 167 events
- `schema/codebook.md` formalizing attribution decision rules (§1.2 resolves the κ=0.5833 stablecoin-freeze ambiguity)
- Schema freeze: `trigger.type=regulatory_enforcement` added; 14 jurisdictions added (AR, BD, BO, BR, ID, TH, UZ, KG, TJ, TM, IL, AE, FR, ZA); 6 JP FSA events migrated to clean enum
- Per-Phase commit pattern preserved; corpus byte-stable

**Stage 2: Collect-all-first Wave 2 (2026-05-17)** — 167 → 262 (+95 events)
- Wave 2.1: 16 P0 backlog sweep across all frames (167 → 183)
- Wave 2.2A: 13 P1 federal_enforcement + historical_baseline (183 → 196)
- Wave 2.2B: 21 P1 corporate_policy + non_us_state (196 → 217)
- Wave 2.2C: 6 P1 supranational + DeFi (217 → 223; 5 rate-limit partials dropped)
- Wave 2.2D: 19 P1 recovery + remaining (223 → 242)
- Wave 2.3: 20 P2 events across all frames (242 → 262)
- DRYRUN-11 SIGN-OFF READY at 262

---

## Final corpus inventory (262 events)

| Dimension | Distribution |
|-----------|--------------|
| **status** | 105 admitted, 156 draft, 1 rejected |
| **origin** | 54 human_authored, 52 human_reviewed, 156 agent_draft |
| **temporal_tier** | 18 discovery_only_2008_2012, 33 historical_baseline_2013_2016, 211 comparable_main_2017_present |
| **analysis_use** | 18 discovery_ledger_only, 33 historical_baseline, 211 comparable_analysis |
| **research_stratum** | S1 ofac_sdn: 34, S2 ofac_removal: 1, S3 doj/sec/cftc/fincen: 65, S4 nation_state: 73, S5 corporate: 65, S6 supranational: 24 |
| **admission_tier** | 4 anchor_case, 182 empirical_case, 76 null_case |
| **empirical_shape** | 2 cascade, 184 comparison, 76 null_event |

---

## Decision-gate verdicts (all 8 sign-off cycles in this session)

All passed strict paper-readiness gate (`--strict-repro --strict-reliability --strict-null-audit --strict-audit --allow-soft-attribution --allow-dryrun-human-gates`): exit 0, byte-stable across 25 artifacts. Three documented WARNs persist across all DRYRUN cycles (intentional pipeline-rehearsal markers, not blocking):
1. 12 null-denominator cases carry DRYRUN `last_human_audit` stamps (pipeline-rehearsal markers, not real human audit).
2. IRR `coder_provenance.mode = independent_human_dryrun_llm_simulated` (LLM-simulated reliability, not real independent-human reliability).
3. Attribution κ=0.5833 below 0.6 threshold (soft attribution gating per codebook §1.2 disposition).

---

## Codebook + schema freeze (DRYRUN-10 mid-session checkpoint)

User-approved upstream protection installed after the lean-run Stage 1 to prevent codebook drift and schema-gap mass-rework downstream:

### `schema/codebook.md` (NEW)

Formalizes coding rules for fuzzy edges. Key sections:
- **§1.2 Stablecoin-issuer compliance freezes**: Hard decision rule — `direct` requires (A) OFAC names addresses controlled by issuer's asset AND (B) issuer publicly confirms freeze on named addresses within compliance window. Only (A) or only (B) → `plausible`.
- **§1.3 Worked examples** resolving the 3 IRR disagreement rows: cryptex-ofac-2024 row 3 stays `direct`; semenov-ofac-2023 rows 9-10 should flip key to `plausible`.
- **§5/§6/§7**: canonical enum aliasing for `trigger.type`, `analysis_use`, `target.enumeration`.
- **§8**: LLM authoring agent compliance protocol.

### Schema freeze (`controlled_vocab.yaml` + `event.schema.json` + `validate.py`)

- Added `trigger.type = regulatory_enforcement` for non-US national regulator administrative enforcement (JP FSA, KR FSC, IS CBI, etc.). Validator maps to S4_nation_state.
- Migrated 6 JP FSA events from awkward fallbacks (`nation_state_block` × 3, `sec_action` × 1, `fincen_action` × 2) to canonical `regulatory_enforcement`. Stratum corrected S3→S4 where needed.
- Added 14 jurisdictions: AR, BD, BO, BR, ID, TH, UZ, KG, TJ, TM, IL, AE, FR, ZA.

---

## Honesty discipline preserved (all 156 agent_draft events)

- **Status discipline**: `status: draft` ✓ (validator hard-rule paired with `origin: agent_draft`)
- **DRYRUN preamble** in `analysis_notes` ✓ (Phase A-F + Wave 2.1-2.3 markers for downstream grep filtering)
- **Honest `evidence_use`**: `contextual_unarchived` everywhere — zero invented `body_hash` values ✓
- **Wayback discipline**: year-prefix wildcard URLs `https://web.archive.org/web/YYYY/<url>` per codebook convention
- **L0 honesty rule**: events claiming `partially_measured`/`measured` L0 coverage REQUIRE corresponding `derived/l0_coverage_summary.csv` denominator row. Kazakhstan precedent: documented-but-uncaptured measurement claims downgraded to `not_measured` (commit `5e28a89`).
- **5 rate-limit-partial files dropped** (commit `6fa0631`) rather than fabricating wayback URLs or papering over coverage mismatches; re-authored cleanly in Wave 2.2D.

---

## Agent-quality observations

### Net positive
1. **Schema convergence per phase**: Authoring time dropped Phase A (~6 min/event) → Wave 2.3 (~2-3 min/event) as agents internalized the codebook.
2. **Codebook-aware authoring**: Wave 2.1+ agents proactively cited codebook sections (`§1.2`, `§5.1`) in their reports, reducing schema-enum fallback errors observed in Phase F.
3. **Sibling-pattern learning**: Late-wave authoring agents templated from prior siblings without explicit instruction.
4. **Cross-frame deduplication**: Discovery agents consistently caught duplicates (`china-pboc-ten-agencies-crypto-illegal-2021-09` vs existing `china-pboc-crypto-ban-2021`; `tornado-cash-developer-roman-storm-conviction-2025` vs `tornado-cash-storm-conviction-2025`; `fatf-r15-vasp-travel-rule-guidance-2019` vs existing `fatf-r15-vasp-travel-rule-2019`; `oecd-carf-crypto-asset-reporting-framework-2022` vs existing `oecd-carf-2022`).

### Surfaced issues (resolved)
1. **Wave 2.2C rate-limit blast** (25 parallel agents): hit upstream LLM rate limit, only ~11 of 25 completed; 5 partially-authored files validated as broken. Resolution: drop 5 partials, re-author in Wave 2.2D smaller batches (5 agents each).
2. **Lesson learned**: Wave 2.2D used 5-agent batches consistently, zero rate-limit issues across 19 events.
3. **circle-usdc-cryptex-freeze-2024 self-reference bug**: Agent set `duplicate_of_action_id` equal to its own `action_id`. Fixed surgically (removed field).
4. **Costa Rica jurisdiction gap**: Liberty Reserve 2011 event needed `CR` but it's not in jurisdiction enum. Authoring agent honestly coded `[corporate_global]` with note. Schema-freeze update pending (or accept the workaround).

---

## Layer coverage outcomes (final)

| Layer | Phase A-F | Wave 2 | Final | Direction |
|-------|-----------|--------|-------|-----------|
| l0_network | 1 (after KZ honesty fix) | +0 | 1 | Severely under-documented; requires real OONI capture |
| l1_consensus | 4 (CN mining + KZ hashrate) | +2 (iran-mining, russia-mining-leg context) | 6 | Niche layer, well-anchored |
| l3_rpc | 3 | +2 (consensys-metamask-2022-11, metamask-snaps) | 5 | DRYRUN-pipeline-saturated for this tier |
| l4_frontend | 19 (DeFi+app-store cluster) | +14 | 33 | Best-populated for paper claims |
| asset_onchain | 14 (incl. WikiLeaks blockade) | +10 | 24 | Strong for stablecoin-freeze claims |
| offramp_cex | 60+ (CEX delisting + payment-rail) | +50+ | 100+ | Best-populated cross-frame |

L0 remains the structural gap — no real OONI batch query was run this session for any event. Kazakhstan was the test case for the honesty rule (downgraded from `partially_measured` to `not_measured`).

---

## Critical path to v0.2.0 production release

The 11 DRYRUN cycles preserved the **DRYRUN-discipline contract**: every authored event remains at `status: draft` + `origin: agent_draft`. Five human-required gates remain open before a real v0.2.0 release:

1. **Human review of 156 agent_draft events** (real human audit, not LLM-simulated). Promotion sequence:
   - Verify each event's primary URL is reachable; legal/regulatory content matches the claim.
   - Pin real `body_hash` + `body_path` captures into `sources/http_captures/<slug>/` for primary_legal citations.
   - Run real OONI batch queries for L0-cascade events (KZ, infura-metamask-donetsk-luhansk, others) and pin `measurement_ids`.
   - Flip `evidence_use` from `contextual_unarchived` to `primary_archived` once body_hash anchored.
   - Flip `origin: agent_draft` → `human_reviewed` and `status: draft` → `admitted` after human audit pass.

2. **Real H1 IRR re-computation** with independent-human coders (not LLM-simulated). Current Cohen's κ (0.5833 attribution, 1.0 coverage_status, 1.0 observation_kind) is from `independent_human_dryrun_llm_simulated` mode. Codebook §1.2 should be tested against fresh human coders to validate the disposition.

3. **12 null-denominator cases** require real human audit (currently carry DRYRUN `last_human_audit` stamps): iran-ransomware-ofac-2018, irgc-ransomware-ofac-2022, lazarus-entity-ofac-2019, lazarus-laundering-ofac-2020, lockbit-leader-ofac-2024, matveev-ofac-2023, pertsev-nl-arrest-2022, russian-cybercrime-infra-ofac-2025, sichuan-silence-ofac-2024, sinbad-ofac-2023, storm-semenov-doj-2023, zservers-ofac-2025.

4. **Apply codebook §1.2 retroactively**: re-audit `attribution` field on all 24 asset_onchain rows + 100+ offramp_cex rows. Specifically: did the issuer (Tether/Circle) publicly confirm freeze on OFAC-named addresses? If yes → `direct`; if only one of (A)/(B) holds → `plausible`.

5. **5 H2 human-gates** from prior session still open (sec-v-uniswap-wells confirm reject; pertsev/storm-semenov scoped_claim review; offramp_cex.measured convention pick; attribution κ codebook decision applied; null-denominator real-audit).

---

## Remaining backlog (post-Wave-2)

After Wave 2.3, the triage manifests have **0 P0 remaining** and **near-zero P1 remaining**. P2-deferred candidates (~5-10) remain across manifests for genuinely edge-case events (operator hacks coded as not-censorship, framework laws coded as null_event, etc.).

The 600-event target from `analysis/collection_plan_v0.2_to_v1.0.md` requires additional v0.3 work not in scope for this session:
- US state-level regulators (50 states, each with own BitLicense-style framework)
- DePIN governance events (Helium, IoTeX, Render Network)
- Stablecoin protocol-level censorship density (Tether/Circle/Paxos historical per-event sweep)
- ICO-era enforcement (2017-2018) density
- DeFi Summer + DeFi exploit enforcement (2020-2021) density
- 2025+ OFAC RA updates (corpus is snapshot)
- Multilingual primary-source ingest (Chinese, Russian, Japanese)

---

## Reproducibility

To replay this session from `8948e69` (87 events) → `86a9859` (262 events):

```bash
git checkout 8948e69     # starting point
git log --oneline 86a9859 ^8948e69 | wc -l  # ~40 commits to replay
```

Pattern per Phase / Wave: 1 discovery agent → N parallel authoring agents → consolidation → regen → DRYRUN sign-off → commit.

Critical lesson: **batch size matters**. 5-agent batches consistently rate-limit-safe; 25-agent batches hit limits ~50% of the time. Phase A-F used 10-13 routinely (mixed success); Wave 2.2D adopted 5-agent batches as standard.

---

## Closing note

DRYRUN-11 at `v0.2.0-rc-dryrun-11` (262 events) is the **pipeline-rehearsal terminal state** of the collect-all-first workflow. The corpus has grown from 87 → 262 (+201%) in one session while:
- preserving DRYRUN-discipline (156 draft/agent_draft events grep-able by `tags: dryrun_2026_05_16` or `dryrun_2026_05_17`),
- installing schema + codebook upstream protections (DRYRUN-10),
- maintaining strict paper-readiness gate compliance across 11 byte-stable DRYRUN cycles,
- documenting Kazakhstan-style honesty fixes (no fabricated L0 measurements, no fabricated body_hash).

The remaining work is **human-required** (audit + IRR + body_hash pinning), not more LLM agent rounds. Codebook §1.2 + the 14 jurisdiction enum + the `regulatory_enforcement` trigger.type are the durable artifacts that survive the LLM authoring phase and bind future human coders.

— Authored by LLM agent 2026-05-17 (Claude Opus 4.7 1M context) as the closing artifact. `status: draft` semantics apply to this summary — please supersede on real-release human audit.
