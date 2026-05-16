# Review D · Paper-claims and corpus-impact assessment of the n=53 → n=84 convert-all proposal

Generated `2026-05-16` · sources: `analysis/temporal_ledger/yearly_collection_plan.csv`,
`docs/paper_claims.md`, `derived/admission_sensitivity.md`,
`derived/event_archetypes.csv`, `analysis/trigger_registry/trigger_registry.md`,
`analysis/null_audits/AGGREGATE.md`, `analysis/paper_tables/table7_jurisdiction_distribution.md`.

The "convert-all" proposal: promote 4 `observation_closed` rows + 28
`candidate` stubs → `admitted`, moving the paper denominator from 52 to
84. The load-bearing question is whether that move is corpus-shape
neutral, mechanically defensible, or scope-creep dangerous.

The structural finding before any number: **all 28 candidate stubs + 4
observation_closed stubs lack `observations:` and `coverage:` blocks in
their YAML** (verified: `grep -l "^observations:" candidate_triggers/*.yaml`
returns 0; same for `coverage:`). Every one of the 52 admitted events
has both. That asymmetry drives §§1–4.

## 1. Corpus-shape shift (n=52 → n=84)

Two interpretive paths: **Path A** (status flip only, no new
observations/coverage authored) and **Path B** (convert-all + full
coverage/observation YAML authoring for the 32 rows).

### 1a. C1 layer-observability rates

| layer | n=52 current rubric | Path A n=84 | Path B n=84 (full auth) | Δ direction |
| --- | --- | --- | --- | --- |
| `l0_network` | — / 0 = — | — / 0 = — | likely — / 0 (no OONI denominators in candidate stubs) | unchanged |
| `l1_consensus` | 1/6 = 0.17 | 1/6 = 0.17 | ~1–3 / 6–9 ≈ 0.10–0.30 | flat-to-down |
| `l3_rpc` | 2 named obs · no rate | same | same | unchanged |
| `l4_frontend` | 10/13 = 0.77 | 10/13 = 0.77 | ~17–22 / 28–32 ≈ 0.55–0.70 | **roughly −10 to −20pp** |
| `asset_onchain` | retracted (circular) | retracted | retracted | unchanged |
| `offramp_cex` | 15/25 = 0.60 | 15/25 = 0.60 | ~22–28 / 45–50 ≈ 0.45–0.55 | **roughly −5 to −15pp** |

Path A leaves rates literally unchanged but bloats the C0 selection-
narrative denominator. Path B drops L4 and CEX rates because the 28
stubs skew toward enforcement actions with softer/absent front-end and
off-ramp reactions (historical S3 like `bitfinex-cftc-retail-commodity-2016`,
multi-platform S4 like `india-fiu-offshore-vda-block-2023` where the
FIU notice has no clean per-target outcome). L4 is already
`sensitive` (Δ = 0.13 strict→permissive per
`derived/admission_sensitivity.md`); a 10–15pp drop reframes the
headline from "concentrated upper-stack admissible evidence" to
"concentrated only on confirmed Tornado-family + OFAC SDN cases".

### 1b. C2 archetype distribution

25 of 28 candidate stubs carry the standard `expected_layers:
[l4_frontend, asset_onchain, offramp_cex]` triple; historically ≈ 40-50%
of admitted OFAC events evidence ≥ 2 layers. The 4 observation_closed
rows are null by construction.

| archetype | n=52 | projected n=84 (Path B) | share Δ |
| --- | ---: | ---: | --- |
| `asset_only` | 13 (25%) | ~22–26 (27–31%) | flat-slight up |
| `cex_only` | 15 (29%) | ~22–25 (27–30%) | flat |
| `frontend_only` | 8 (15%) | ~10–13 (12–15%) | flat-slight down |
| `multi_layer` | 4 (8%) | ~5–7 (6–8%) | **stays thin** |
| `null_event` | 12 (23%) | ~17–21 (20–25%) | flat |

**Multi-layer grows roughly proportionally, not faster.** C2 stays
PARKED at n=84: the κ gate, not n, is the promotion barrier.

### 1c. Jurisdictional composition

Candidate-stub jurisdictions (from `^jurisdiction:` grep): 19 US-touching
(17 US-only + 2 multi), 11 non-US. Assume 4 observation_closed are US.
Projection: (39 + 23) / 84 = **62/84 ≈ 73.8%** US-touching — down ≈ 1pp
from 75.0%. Cosmetic shift, not a reframing. The 2008-2016 historical
candidates are heavily US-DOJ-anchored (silk-road, ripple, coinbase-IRS,
shrem-faiella); they cancel most of the 2024-2025 international gain.

### 1d. Null-case denominator shift

Current null share: 12/52 (23%). The 4 observation_closed rows push
the admitted-with-observations share to 16/56 = 28.6%; Path B settles
to ~20-25%. **The bigger issue**: of the 28 candidate stubs, 22 are
OFAC SDN designation rows. Under the existing convention they would
each inherit the OFAC-RA-only `coverage.offramp_cex = measured`
substrate that the H2 audit (`analysis/null_audits/AGGREGATE.md` P2)
flagged on 7-8 current events. **The P2 surface scales to 14-22
events at n=84** — a 2-3× scope multiplier on the corpus-wide
convention question.

## 2. Convert-all feasibility · "structurally different" at the artifact level

| artifact | 52 admitted | 28 candidate stubs | 4 observation_closed |
| --- | --- | --- | --- |
| trigger citation + body_hash + body_path | all | URL only on most | yes |
| `coverage:` (per-layer status + denominator_reason + denominator_artifact) | **all** | **absent on all 28** | partial |
| `observations:` (layer + observation_kind + attribution + evidence) | **all (≥1 row)** | **absent on all 28** | scoped null only |
| `admission_tier` (anchor/empirical/null) | all | absent | inferable as null |
| `last_human_audit` stamp | most (13 nulls pending) | absent | absent |
| LLM pre-audit + cross-agent verdict | most | none | none |

This is a fundamental evidence-completeness gap, not a polish gap.
Converting a candidate to admitted requires authoring coverage matrix,
observations, body_hash anchors, LLM pre-audit, and a
`last_human_audit` stamp. Calibrated against the existing
`samourai-doj-2024`-class workflow, ≈ 4-8 h per event → **28 × 6h ≈
170 hours** before H2 follow-ons.

**Path A is undefensible**: it forces the paper-table generator to
discriminate `admitted_with_evidence_chain` from
`admitted_trigger_only`, which is functionally the existing
`candidate` ↔ `admitted` split renamed, while breaking the C0
phrasing-lock ("admitted-only paper tables remain the only source
for paper-facing event counts" — `analysis/trigger_registry/trigger_registry.md`).

## 3. Sampling-frame statement under n=84

The v0.1 frame: "publicly documented English-indexable crypto
censorship events with an identifiable legal/regulatory/state/corporate
trigger AND ≥1 independently archivable evidence surface."

The 28 candidate stubs satisfy the inclusion rule
(`sampling/frame.yaml::inclusion_rule`) on the trigger-identifiability
side; the "evidence surface" clause is technically satisfied by the
archived trigger page itself. The 2013-2016 historical-baseline
candidates are in-frame but carry `analysis_use: historical_baseline`
and stay out of 2017+ comparable denominators — the tier-segregation
discipline already covers this without frame relaxation.

**Frame conclusion**: the 84-event projection still matches v0.1 frame
language. *No relaxation required.* What WOULD require relaxation is
dropping the "English-indexable" clause to admit Russian / Chinese /
Iranian-language sources — that is a v0.3-class move, deferred in
§0 "Out of scope".

## 4. H2 scope-creep risk under convert-all

| H2 item | n=52 surface | n=84 surface | multiplier |
| --- | --- | --- | --- |
| P0 `sec-v-uniswap-wells-notice-2024` resolution | 1 case | 1 case | 1× |
| P1 codebook ambiguity on `direct/plausible` for SDN-asset freezes | 3 / 17 measured-asset events | ~3-7 / ~24-30 measured-asset | **1.5-2×** |
| P2 corpus-wide offramp_cex convention (OFAC-RA-only nulls) | 7-8 events | **14-22 events** | **2-3×** |
| P2 textual / archival-hygiene fixes | 4 events | ~4-12 events | 1-3× |

P2 is the scariest scaling — it governs how the paper interprets
roughly half of all OFAC-SDN null events. P1 cannot improve under
convert-all because its disagreement cluster is *exactly* the
asset_onchain SDN-freeze cohort that grows fastest under convert-all.
Each new event in that cohort is a fresh ambiguous row pending
codebook resolution. **The κ gate on C2 promotion moves further away,
not closer, under convert-all.**

## 5. Recommended ordering for v0.2

**(a)** H2-first, ship at n ≈ 53: stamp `last_human_audit` on the 13
pending null cases, resolve P0 Uniswap-Wells, pick the P2 convention,
fix textual hygiene. ≈ 40-80 h. Output: stronger defensibility,
unchanged headlines.

**(b)** Convert-all (≈ 170+ h authoring + P1/P2 doubling mid-conversion).
Output: 73.8% US-trigger headline (cosmetic), L4/CEX rates −10-15pp
(Path B), no κ resolution, C0 contract broken. **Not defensible.**

**(c)** Staged: H2 first, then admit only the 11 historical-baseline
(2013-2016) candidates with strict tier-segregation, push the 17
comparable-main candidate-stub conversions to v0.3.

**Recommendation: option (c)**, with two modifications:

1. **H2 resolution is a hard gate** before any new admission — P2 in
   particular must be decided (one of the three options in
   `analysis/null_audits/AGGREGATE.md`) because every new OFAC-SDN
   admission inherits it.
2. **Historical-baseline admission is per-stratum, not bulk.** The 11
   candidates split as ~2 S1 OFAC (low marginal value, large H2
   overlap), ~7 S3 DOJ/SEC/CFTC enforcement (high jurisdictional /
   temporal-baseline value), ~1 S4, ~1 S6. Promote the 7 S3 first;
   they give v0.2 a defensible 2008-2016 enforcement-baseline
   narrative without piling more asset_onchain rows onto the
   structural-circularity problem.

This keeps every C0/C1/C2/C3/C4/C5 phrasing-lock intact, preserves
the κ-promotion path for C2, contains P2 to a fixed surface during
resolution, and leaves v0.3 to absorb the comparable-main expansion
under a refined codebook.

## 6. Projected-numbers summary

| metric | n=52 (v0.1) | n=84 Path A | n=84 Path B | comment |
| --- | ---: | ---: | ---: | --- |
| admitted events | 52 | 84 | 84 | |
| L4 frontend (current rubric) | 0.77 | 0.77 | ~0.55-0.70 | **−10 to −20pp** Path B |
| offramp_cex (current rubric) | 0.60 | 0.60 | ~0.45-0.55 | **−5 to −15pp** Path B |
| L1 consensus (current rubric) | 0.17 | 0.17 | ~0.10-0.30 | thin both before and after |
| multi_layer count | 4 (8%) | 4 (5%) | ~5-7 (6-8%) | stays thin; C2 stays PARKED |
| null_event share | 12/52 (23%) | 16/56 (29%) | ~17-21/84 (20-25%) | |
| US-trigger share | 39/52 (75.0%) | 62/84 (73.8%) | 62/84 (73.8%) | ≈ 1pp cosmetic |
| P2 offramp_cex convention surface | 7-8 events | 14-22 events | 14-22 events | **2-3×** |

## 7. Risk table

### Top 3 paper-claim risks if convert-all goes ahead

| # | risk | severity |
| --- | --- | --- |
| 1 | C0 selection-transparency contract breaks: 32/84 admitted events lack observations/coverage. "Admitted-only paper tables" mix evidenced with trigger-only rows. | **high** |
| 2 | C1 L4 / offramp_cex rates drop 10-15pp under Path B; "concentrated upper-stack admissible evidence" reframes to "concentrated on Tornado-family + asset-freeze cases". Sensitive-rubric disclosure burden grows. | **high** |
| 3 | H2 P2 offramp_cex convention scales 2-3×; P1 codebook ambiguity inherits more SDN-freeze rows; C2 κ promotion moves further away. | **medium-high** |

### Top 3 risks if convert-all does NOT happen

| # | risk | severity |
| --- | --- | --- |
| 1 | Reviewer asks "registry has 84 triggers, paper uses 52, what's hidden?" — C0 selection-transparency is exactly the answer; phrasing-lock §0 already covers it ("registry gaps are expansion backlog, not paper results"). | **low** |
| 2 | US-trigger 75.0% headline stays put; no jurisdictional expansion narrative for v0.2. | **medium** |
| 3 | Multi-layer count stays at 4; C2 stays PARKED. **Not fixable by convert-all** — κ gate is codebook, not n. | **low-medium** |

## 8. Verdict

**Staged** (option (c)) with H2-first hard gating.

+ **Convert-all (option (b)) is not defensible at v0.2.** Rate-side
  impact is either cosmetic (Path A) or actively weakens the headline
  (Path B). H2 P2 convention scales 2-3× during the conversion. C0
  contract breaks. 170+ h authoring spent during an unresolved
  codebook.
+ **Option (a) is safe but leaves 2008-2016 baseline on the table.**
+ **Option (c)** (resolve H2 → admit 7 S3 historical-baseline + ≤4
  S4/S6 historical-baseline → push comparable-main stub conversions
  to v0.3) gives v0.2 a real jurisdictional + temporal-coverage win
  while keeping every phrasing-lock intact and every C0-C5 number
  defensible. Convert the full 84 at v0.3 once P1 codebook ambiguity
  is resolved under an `independent_human` reliability pass.
