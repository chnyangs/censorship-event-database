# Temporal-ledger systematic review — aggregate

> 4-agent independent review of the 2008-2026 temporal-ledger
> collection pass (161 registry raw rows, 84 distinct in-frame
> triggers, 52 admitted, 4 observation_closed, 28 candidate stubs,
> 47 screened). Per-agent reports linked below; this aggregate
> diffs convergent findings, surfaces divergences, and answers
> the maintainer's follow-up question on **converting all 84
> in-frame triggers to admitted paper cases**.

Source reports:

- [`review_a_sampling_frame.md`](review_a_sampling_frame.md) — sampling-frame coherence (Agent A)
- [`review_b_historical_completeness.md`](review_b_historical_completeness.md) — 2008-2016 completeness (Agent B)
- [`review_c_pipeline_state.md`](review_c_pipeline_state.md) — stubs + screened pipeline health (Agent C)
- [`review_d_paper_claims_impact.md`](review_d_paper_claims_impact.md) — corpus-impact + convert-all feasibility (Agent D)

## Severity table

| ID | Severity | Issue | Source(s) |
| --- | --- | --- | --- |
| **F1** | **fatal** | All 5 source frames are slugged `_2017_2026` but carry `date_range: 2008-01-01 → 2026-12-31`, producing 300 monthly cells (2008-2012) that no declared `source_artifact` can reach. OFAC RA extractor's first entry is 2015-04; 4/5 triage manifests are header-only stubs. **300 pending cells are structurally misframed, not honestly unsearched.** | A.F1 |
| **F2** | **fatal-equivalent for v0.2 framing** | **Convert-all (84/84 admitted) actively weakens C1.** Path B (full-evidence) drops L4 from 0.77 → ~0.55-0.70 (−10 to −20pp) and offramp_cex from 0.60 → ~0.45-0.55. The load-bearing C1 headline weakens; C0's "admitted-only paper tables" contract breaks (32/84 rows would lack `observations` / `coverage`); ~170h authoring inherits unresolved codebook (attribution κ=0.58). | D.verdict |
| **M1** | major | `not_applicable_pre_market` and `source_unavailable` statuses are declared and counted in code but never assigned — `pending` does the work of three distinct statuses. Obscures "haven't searched" vs "source can't reach this window". | A.M1 |
| **M2** | major | **Source-frame design gaps** for non-US-state + US-state-regulator activity. 2013-2016 P0 misses (china-pboc-2013, NYDFS-bitlicense-2015) are NOT candidate-ledger backlog — they have no frame slot at all. Frame is `planned:` not ingested for non-US-state; US-state-regulator has no frame. | B.verdict |
| **M3** | major | **Pipeline is backlogging, not flowing**: 28 open stubs vs 30 historically-closed (51.7% conversion). 2023 alone holds 6 stubs (43% candidate-to-admitted ratio — highest comparable year). All 28 stubs are stuck at ONE mechanical gate (HTTP capture + coverage + `validate.py`), not methodology. | C.verdict |
| **M4** | major | **All 28 candidate stubs are UNTRACKED working-tree files.** Only 25 OFAC audit shells were committed 2026-05-07. Stub age is invisible to git history; no stub-retirement policy in `candidate_triggers/README.md` or `process-checklist.md`. | C.critical |
| **m1** | minor | `historical_baseline_2013_2016` has 0 admitted across 4 years despite 14 candidate stubs — a parking lot, not a denominator-eligible window. Promote 2 anchors before v0.2 or rename. | A.m1 |
| **m2** | minor | 4 observation_closed events (alphabay-hansa-2017, blockfi-2022, kraken-staking-2023, beaxy-2023) are admission-ready pending **one human-review pass** against `process-checklist.md §4`. | C.observation_closed |

## Convergent findings across agents

### Convergence 1 — the frame is partly imaginary in 2008-2016

Agents A and B independently identify the same root cause from different angles:

- A: source frames slug as `_2017_2026` but `date_range` extends 2008-2026; pre-artifact cells get tagged `pending` instead of `source_unavailable`. **300 cells are structurally misframed.**
- B: china-pboc-2013 + NYDFS-bitlicense-2015 are not even in the candidate ledger because non-US-state + US-state-regulator frames are missing. **Frame-design gap, not backlog gap.**

Together they say: **the 2008-2016 "pending" count overstates how much honest searching is required.** A fair fraction of pending = "no source-frame artifact reaches this window" or "no frame slot exists for this trigger type" — not "we haven't gotten around to it."

Joint fix: A's `source_artifact_first_available_date` field + B's expansion of frame slots for non-US-state + US-state-regulator triggers. After both, the pending count for 2008-2016 should drop sharply.

### Convergence 2 — convert-all is undefensible (Agents D + C + A m1)

Three independent angles converge:

- D quantifies the weakening: L4 −10 to −20pp, offramp_cex −5 to −15pp, US-share −1pp (cosmetic).
- C documents the operational reality: stubs are stuck at HTTP-capture, not methodology — converting them adds rows without observations, breaking the C0 admitted-only-tables contract.
- A documents the historical_baseline emptiness: 12 candidate stubs / 0 admitted is a methodology problem, not a manpower problem.

Joint verdict: **STAGED** release, not convert-all.

### Convergence 3 — H2 conventions block expansion

D and C both note that the offramp_cex.measured-on-OFAC-only-substrate convention (H2 P2 from the last review cycle, 7-8 events affected at n=53) scales **2-3×** to 14-22 events at n=84 if OFAC stubs are converted en masse. The attribution κ=0.58 codebook gap (H1 P0) similarly scales. **Resolving H2 BEFORE expanding the corpus is the right ordering.**

## Answer to the maintainer's question: 把这些 cases 全部转换成 admitted paper cases?

**No — execute STAGED instead.** Agent D's verdict is supported by both pipeline operational reality (Agent C) and methodology-gate state (Agent A m1, H2 attribution κ).

### Recommended ordering (highest leverage first)

**Phase 0 — pipeline hygiene** (1-2 days, no scope shift):

1. **Commit the 28 candidate stubs to git** (`git add candidate_triggers/*.yaml`) so stub age becomes visible.
2. Write a `candidate_triggers/RETIREMENT_POLICY.md` setting a stub-age threshold (e.g. 180 days) and a screened-out path. Currently stubs can sit indefinitely with no signal.
3. Clear the 4 `observation_closed` events to admitted (single human-review pass each — they're admission-ready per Agent C). **Result: 52 → 56 admitted, with H2-style provenance discipline.**

**Phase 1 — frame fixes** (1-2 days, no event admission):

4. Patch the sampling frame per A.F1: add `source_artifact_first_available_date` to each frame in `sampling/frame.yaml`; re-emit pre-artifact cells as `source_unavailable` not `pending`. This drops the 300 misframed pending cells and makes the 2008-2012 denominator honest.
5. Assign A.M1's unused statuses (`not_applicable_pre_market`, `source_unavailable`) in `scripts/build_temporal_discovery_ledger.py`. The ledger then reports five distinct states instead of one.
6. Add the missing frame slots per B.M2: non-US-state + US-state-regulator. This brings china-pboc-2013 and NYDFS-bitlicense-2015 into the candidate-ledger surface (not the events surface yet — that's Phase 2).

**Phase 2 — historical_baseline anchor admission** (3-5 days):

7. Admit Agent B's top-3 P0 historical-baseline events:
   - `china-pboc-crypto-ban-2013-12` — direct cross-temporal sibling to admitted china-pboc-2021; same S4 stratum.
   - `silk-road-doj-seizure-2013-10` — already a candidate stub; highest-evidence-density of the period.
   - `nydfs-bitlicense-2015-06` — clean L4 cascade in Wayback (ShapeShift / Kraken / Bitfinex / Poloniex NY-exits).

   **Result: 56 → 59 admitted; historical_baseline tier no longer a parking lot.**

8. Carry an explicit scope-limitation paragraph in `paper_claims.md §0` naming what 2008-2016 events are documented in the corpus, what are documented as frame-gaps, and what was discovery-only.

**Phase 3 — H2 resolution before further expansion** (parallel with Phase 2; ~1 week):

9. Run a real independent-human IRR pass on the attribution κ=0.58 codebook ambiguity (the 3 stablecoin-freeze disagreement rows). Either tighten the codebook or accept the moderate κ.
10. Pick the corpus-wide offramp_cex.measured-on-OFAC-only-substrate convention (the three options in `analysis/null_audits/AGGREGATE.md` P2).
11. Adjudicate the 2 H2-divergent verdicts (pertsev-nl-arrest-2022, storm-semenov-doj-2023).

**Phase 4 — Agent C's top-5 promotion sprint** (3-5 days, only after Phase 3):

12. Capture + admit the 5 highest-leverage stubs (KuCoin-DOJ-2024, Paxos-BUSD-NYDFS-2023, UK-FCA-Binance-2021, EU-Russia-crypto-wallet-cap-2022, Philippines-SEC-Binance-2024). **Result: 59 → 64 admitted.**

**Phase 5 — v0.2 release** (after Phases 0-4 land):

13. Re-run all paper-readiness gates at n=64. Update C1/C2/C3 numbers in `paper_claims.md`. Run `scripts/release_signoff.py --version 0.2.0 --date <date>` (real, not dryrun).

**Phase 6 — v0.3 candidate-stub conversion** (deferred 3-6 months):

14. Process the remaining 12 stubs (28 − 11 promoted in Phases 0+2+4 = ~17 left) under the refined codebook + admission protocol. Each requires full evidence capture per Agent D's "full-evidence authoring" path.

### Phase-by-phase corpus shape

| phase | admitted | new evidence work |
| ---: | ---: | --- |
| current | 52 | — |
| after Phase 0 | 56 | observation_closed → admitted, 4 events |
| after Phase 2 | 59 | 3 historical_baseline anchors (P0 trio) |
| after Phase 4 | 64 | 5 P0 comparable_main stubs |
| after Phase 6 (v0.3) | ~76-81 | the remaining ~12-17 stubs |
| convert-all (rejected) | 84 | not recommended at any phase |

## Verdict

**Yes-with-conditions to v0.2 release after Phase 2; no to convert-all at any phase.**

The frame defects (F1, M1, M2) and the pipeline-hygiene issues (M3, M4) are all fixable in <1 week. After those fixes plus Phase 2 (the 3-event historical anchor admission), the corpus tells a cleaner story than v0.1: the L4 / offramp_cex rates are robust to the staged expansion (because the 3 new admits hit different layers), the historical_baseline tier earns its name, and the sampling frame statement matches what the ledger actually shows.

Convert-all weakens the paper's most defensible claim (C1 upper-layer concentration) by 10-20pp at L4 and breaks the C0 admitted-only-tables contract. It also forces resolution of H2 codebook ambiguity across 2-3× more events. There is no v0.2 reading under which convert-all is the right move.
