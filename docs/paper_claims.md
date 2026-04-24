# Paper claims · v0.1 skeleton

> **Status**: skeleton. Every claim below is a candidate; nothing is
> promoted to the paper until (a) the anchor audits for its supporting
> events are complete, and (b) the paper table generator
> (`scripts/build_paper_tables.py`, live as of 2026-04-24) reproduces
> the cited numbers from the committed dataset snapshot.

This file is the single source of truth for "what the paper actually
argues." Each claim states:

- the **claim sentence** (one unambiguous line),
- **evidence source** (specific `derived/` path + derivation),
- **n** and the **case roles** used (anchor / aggregate / null),
- **scope caveats** (what the claim does *not* say),
- **phrasing lock** (exact verbs permitted; see
  `docs/limitations-and-use.md §6`).

Changes to this file are the only legitimate way to re-aim the paper.

## 0. Framing and estimand

**Dataset snapshot**: v0.1.0 · cutoff 2026-04-22 · 53 admitted events.

### Primary estimand (one, not three)

> **Among publicly observable stack layers, which ones carry detectable
> enforcement reactions to an identified US-centric censorship trigger,
> and with what latency distribution — conditional on that layer
> having a measured denominator in the dataset?**

Why this framing, not the alternatives:

- "**Full cascade is rare — why?**" is motivating background but
  n = 5 `multi_layer` events is too thin for a standalone paper
  claim. Reserved as secondary framing.
- "**Reaction speed by issuer / frontend / CEX**" is downstream of the
  primary estimand (a sub-breakdown). Primary estimand answers layer
  *selection*; speed is a column of the same table.

### What this paper is NOT

- Not a predictive model of future enforcement.
- Not a claim that un-measured layers did or did not react.
- Not a claim about private compliance signals (issuer internal
  intelligence, KYT flags, private law-enforcement channels).
- Not a stack-exposure score — the rubric in
  `docs/evaluation-profile-schema.md` is reviewer-facing and
  deliberately separated from this paper's empirical contribution.

### Case role convention

Each event carries `admission_tier`:

| role | purpose in paper | current n |
| --- | --- | --- |
| `anchor_case` | hand-audited exemplars; figures + narrative spotlight | 5 |
| `empirical_case` | aggregate-count contributors (distributions, tables) | 35 |
| `null_case` | denominator for "we looked and observed no change" | 13 |

A claim may NOT cite an `empirical_case` for a narrative spotlight
role, nor a `null_case` for a "changed-layer" count. The paper-table
generator (planned) will enforce this at emission time.

### Attribution discipline

The dataset records each `observed_change` with
`attribution ∈ {direct, plausible, none}`. In any paper claim:

- `direct` observations may support a causal statement ("trigger X
  produced observation Y").
- `plausible` observations may support a co-occurrence statement
  ("observation Y occurred within the event window; attribution is
  consistent with X but not uniquely supported").
- `none` (applies to `observed_no_change` and `coverage_gap` rows) may
  not support any causal statement; it supports only
  "within the scoped window and sources, no change was observed".

**Plausible and direct observations are reported in separate columns
in every table**; collapsing them is a phrasing violation.

### Timestamp-precision discipline

- Trigger timestamp precision across the corpus splits into a
  day-precision majority (e.g. OFAC SDN listings publish to day
  granularity only) and an hour-or-better minority. **Live counts
  live in [Table 1](../analysis/paper_tables/table1_case_roles.md)
  §Summary**; do not hardcode numbers in prose here.
- **Only the hour-or-better subset may carry an hour-precision latency
  claim.** Day-precision triggers appear in per-event narratives and
  in tables marked as "≤1 day" bucketed; they are excluded from any
  hour-granularity latency distribution.
- The paper-table generator
  ([`scripts/build_paper_tables.py`](../scripts/build_paper_tables.py))
  filters `time_to_first_change_hours` by trigger precision before
  emitting any hour-granularity bin; see
  [Table 4](../analysis/paper_tables/table4_latency_by_precision.md)
  Panel A vs Panel B.

## 1. Candidate claims (ranked by strength of current evidence)

Each claim below names the `derived/` artifact that feeds it, the exact
subset of events admissible, and the phrasing lock.

### C1 · Upper-layer concentration of observed reactions

**Claim (phrasing-locked)**:

> "Across 53 admitted events, observed changes are concentrated on
> the upper layers of the six-layer stack. Under coverage-matched
> denominators, `asset_onchain` shows `changed_given_measured` = 17/17
> (1.00), `l4_frontend` = 11/16 (0.69), and `offramp_cex` = 15/25
> (0.60). `l1_consensus` shows 1/6 (0.17) measured and 2/7 (0.29)
> measured-or-partial, both anchored on Tornado Cash events.
> `l3_rpc` has no `measured`-coverage events, but its
> partial-coverage subset now carries **2 observed changes
> (`changed_given_measured_or_partial` = 2/9 = 0.22), both from
> the Tornado forward / reverse cascade** — admitted via Flashbots
> rpc-endpoint git-history (PR #90 adding Tornado pool addresses
> 2022-08-08, PR #173 deleting the blacklist 2025-04-01; see
> `analysis/anchor_gap_fill_log.md §4`). `l0_network` carries no
> measured denominator. The claim is a description of the admitted
> evidence corpus, not of the underlying phenomenon."

- **Evidence**: `derived/layer_observability.csv`; coverage-matched
  numerator (per P1 fix, 2026-04-23).
  `analysis/paper_tables/table2_layer_observability.md` is the
  reader-facing re-emission.
- **n**: 53 events across 6 layers.
- **Case role**: all 53 (empirical + null + anchor all contribute
  coverage denominators; only observed_change rows enter the
  numerator).
- **Phrasing lock**:
  - PREFER "are concentrated", "observed changes", "coverage-matched
    conditional rate".
  - FORBID "L0 does not react", "L3 is censorship-resistant", any
    rate built on a null denominator, any claim of the form "L3 has
    zero observed changes" (the 2 Tornado L3 rows added
    2026-04-24 invalidate the earlier draft framing).
- **Not said**: this claim does NOT assert that base layers are not
  censored. That is an observability gap. See
  `docs/chain-coverage-note.md` and `docs/limitations-and-use.md §2.4`.
  The two L3 observations are Tornado-specific; they do NOT support a
  general "L3 filter lists react to sanctions events" claim beyond
  these two named cases.

### C2 · Single-layer responses dominate the admitted corpus

**Claim**:

> "Of 53 admitted events, 35 (66%) show observed changes at exactly
> one layer, 5 (9%) show observed changes at two or more layers, and
> 13 (25%) show no observed change at any layer in their scoped
> window. Single-layer responses dominate the publicly-observable
> record, with `cex_only` (n=14), `asset_only` (n=13), and
> `frontend_only` (n=8) being the three dominant single-layer
> archetypes. Zero events land in the `other_single_layer` safety
> class (L0-only / L1-only / L3-only), reinforcing the upper-layer
> concentration observation."

- **Evidence**: `derived/event_archetypes.csv` +
  `derived/archetype_distribution.md` §2.
- **n**: 53 events.
- **Case role**: all 53. Null cases are 13/13 of the `null_event`
  archetype by construction.
- **Phrasing lock**:
  - PREFER "admitted corpus", "observed changes at", "rule-based
    deterministic archetype".
  - FORBID "we found a clustering structure" (rule-based, not
    clustering); "multi-layer cascades are uncommon in the wild"
    (the claim is about the corpus, not the wild).
- **Not said**: multi-layer cascades being rare in the admitted
  corpus does NOT mean they are rare in the population; survivorship
  and source availability bias the upper-layer observation toward
  events with public-record-visible infrastructure. See §3.3 below.

### C3 · Upper-layer reaction latency (hour-precision subset)

**Claim**:

> "Restricted to triggers with hour-or-better precision AND at least
> one timed `observed_change` (Table 4 Panel A), the first observed
> change at any layer falls into hour-granularity bands as reported
> in Panel A. Day-precision triggers with a timed `observed_change`
> are reported separately in Panel B at ≤1d / (1d, 30d] / >30d
> granularity — they are excluded from any hour-granularity
> distribution. `trigger_is_action` events (Panel C) are excluded
> from both Panel A and Panel B because their `t≈0` is a record-level
> artifact, not a measured delta."

- **Evidence**:
  [`analysis/paper_tables/table4_latency_by_precision.md`](../analysis/paper_tables/table4_latency_by_precision.md)
  is the reader-facing source of truth; underlying data is
  `derived/event_metrics.csv :: time_to_first_change_hours` filtered
  by `_trigger_precision()` in
  [`scripts/build_paper_tables.py`](../scripts/build_paper_tables.py)
  (reads the canonical schema field `trigger.timestamp_precision`).
- **n**: **delegated to Table 4**. Panel A / Panel B / Panel C
  cardinalities evolve as the corpus adds events or flips precision
  labels — hardcoding any of the three in prose is phrasing-locked
  FORBID.
- **Case role**: events with at least one timed `observed_change`
  contribute; events with only `observed_no_change` or `coverage_gap`
  rows are absent from all three panels (they live in Table 6).
- **Phrasing lock**:
  - PREFER "first observed change", "conditional on
    hour-or-better trigger precision", "Panel A of Table 4",
    "Panel B of Table 4".
  - FORBID any latency number expressed in hours that includes a
    day-precision trigger; "reaction time" as a scalar summary
    across all 53 (precision-mixed); **hardcoded hour/day
    subset counts in the prose** — delegate to Table 4.
- **Not said**: this is NOT a decomposition by layer speed — that is
  C4 below if promoted.
- **Status**: Table 4 is live (post-2026-04-24). C3 can be cited
  directly from it once the paper narrative fixes the specific
  band-count claims it wants to make.

### C4 · Corporate-policy events are trigger-action identical

**Claim**:

> "Events carrying `trigger.type = corporate_policy_change` have
> `trigger_is_action = true`: the corporate action IS the trigger, so
> the trigger timestamp and the observed change co-occur in the
> record by construction. These events are reported as their own
> category (Table 4 Panel C) and **excluded** from any cross-event
> latency claim — their `time_to_first_change_hours ≈ 0` is a
> record-level artifact, not a measured delay."

- **Evidence**: `derived/event_archetypes.csv :: trigger_is_action`;
  `analysis/paper_tables/table4_latency_by_precision.md` Panel C.
- **n**: **delegated to Table 4 Panel C**. The specific events are
  enumerated there so this claim stays correct as the corpus evolves.
- **Case role**: named; cited by event slug via Table 4.
- **Phrasing lock**:
  - PREFER "record-level artifact", "trigger is the action itself",
    "by construction".
  - FORBID "fastest cascade" (t=0 is not speed); "self-executing
    sanctions" (editorializes beyond the record); **hardcoded event
    counts in the prose** — always delegate to Table 4 so the number
    stays live as the corpus evolves.

### C5 · Structural claim — frontend/asset/CEX reach extends across strata

**Claim**:

> "The dominant single-layer archetypes (asset_only, frontend_only,
> cex_only) appear across multiple research strata: asset_only is
> present in S1 (10) and S5 (3); cex_only in S1 (1), S3 (3), S4 (6),
> S5 (2), S6 (2); frontend_only in S1 (2), S3 (5), S5 (1). The
> upper-layer reach is not a single-stratum artifact."

- **Evidence**: `derived/event_archetypes.json` cross-tabulated with
  `research_stratum`.
- **n**: 53 events.
- **Case role**: empirical + anchor + null jointly contribute.
- **Phrasing lock**:
  - PREFER "present across multiple strata",
    "not a single-stratum artifact".
  - FORBID "occurs uniformly across jurisdictions"
    (stratum ≠ jurisdiction), "consistent pattern"
    (correlational, not causal).

### C6 · Recovery evidence is insufficient for v0.1

**Claim**:

> "The admitted corpus carries one reversal event
> (`tornado-cash-ofac-delisting-2025`). Per-layer recovery counts are
> therefore reported only as n=1 descriptive observations, not as a
> rate. v0.1 does not support a recovery-rate claim; any such claim
> is deferred to a later release."

- **Evidence**: `derived/event_metrics.json :: is_reversal_event`;
  `derived/archetype_distribution.md §4` reversal note.
- **n**: 1.
- **Case role**: anchor_case only.
- **Phrasing lock**:
  - PREFER "n=1 reversal event", "recovery not defensible at v0.1".
  - FORBID any recovery *rate* across layers; "recovery is rare",
    "censorship is rarely reversed".

## 2. Claims explicitly NOT in v0.1

Each item below is a claim we could imagine making and have ruled out.

- **"Cascade timing is a function of trigger type"** — the
  trigger-type × latency cross-tab is under-powered: see Table 1
  trigger-precision split + Table 4 Panel A row count. Parked for
  v0.2 after more hour-precision events accumulate.
- **"Private-order (CEX) responses are faster than on-chain (asset)
  responses"** — day-precision triggers and asymmetric coverage
  denominators (asset is 17 measured, cex is 25 measured) prevent a
  defensible comparison. Parked for v0.2 after precision-aware
  latency tables land.
- **"Stack X is more censorship-resistant than Stack Y"** — the
  paper's dataset does not carry stack-level architectural features.
  That is the concern of `docs/stack-features-schema.md` +
  `docs/evaluation-profile-schema.md`, which are schema-only in v0.1.
- **"Evidence suggests censorship is increasing / decreasing"** —
  dataset is not a time series of uniform coverage; it is a curated
  stratified catalog. Time-trend claims require a different sampling
  frame.

## 3. Systematic uncertainty sources the paper must surface

### 3.1 Sampling: stratum weights are not population weights

The 53 events are stratum-complete relative to the admission protocol,
not population-weighted. A reader should not read row counts as
prevalence estimates over "all censorship events". Stratum identifiers
(`S1_ofac_sdn`, `S2_ofac_removal`, `S3_doj_sec_cftc_fiod`,
`S4_nation_state`, `S5_corporate`, `S6_supranational`) must be
preserved in every per-row output.

### 3.2 Source availability bias

Observation at upper layers (`l4_frontend`, `asset_onchain`,
`offramp_cex`) is easier because those layers leave public-record
artifacts (Wayback captures, on-chain events, press releases). Base
layers (`l0_network`, `l1_consensus`, `l3_rpc`) either do not leave
equivalent artifacts, require paid-API access
(Chainalysis / Elliptic), or require institutional research feeds
(Censored Planet / OONI / Wahrstätter). **C1's upper-layer
concentration is therefore partly a survivorship effect of the
evidence substrate, and the paper must state this explicitly
adjacent to C1.**

### 3.3 Coverage denominator rules

Every conditional rate in the paper derives from
`derived/layer_observability.csv`. The coverage-matched numerator
(post-P1 fix) is the only correct shape. Before publication, every
paper table cell must carry its denominator inline ("x / N") and the
paper-table generator should fail-closed if any rate is emitted
without a matched denominator.

### 3.4 Recovery is n=1

`tornado-cash-ofac-delisting-2025` is the sole reversal event. The
paper reports this event's per-layer recovery as a named observation,
not as a rate. See C6.

### 3.5 Trigger-is-action category is separate by construction

`corporate_policy_change` events (see C4) are reported as a distinct
category via Table 4 Panel C. Cross-event latency statements must
aggregate the two subsets separately. Count delegated to Table 4 so
this claim stays correct as the corpus evolves.

## 4. Paper-table generator (live)

`scripts/build_paper_tables.py` produces the six tables below under
`analysis/paper_tables/`. Run `make paper-tables` after any change to
`events/*.yaml` or `derived/*`. Each of C1–C6 is frozen to its exact
number by the relevant table at a given `source_commit`. Numbers not
produced by that generator do not enter the paper.

| # | table | file | supports |
| --- | --- | --- | --- |
| 1 | Case roles | [`table1_case_roles.md`](../analysis/paper_tables/table1_case_roles.md) | §0 case-role convention |
| 2 | Layer observability | [`table2_layer_observability.md`](../analysis/paper_tables/table2_layer_observability.md) | C1 |
| 3 | Archetype × stratum | [`table3_archetype_stratum.md`](../analysis/paper_tables/table3_archetype_stratum.md) | C2, C5 |
| 4 | Latency (precision-filtered) | [`table4_latency_by_precision.md`](../analysis/paper_tables/table4_latency_by_precision.md) | C3, C4 |
| 5 | Target enumeration | [`table5_target_enumeration.md`](../analysis/paper_tables/table5_target_enumeration.md) | §4 complete-vs-subset |
| 6 | Null denominator | [`table6_null_denominator.md`](../analysis/paper_tables/table6_null_denominator.md) | C6, null-event interpretation |

Fail-closed properties the generator enforces:

- Conditional rates with a zero denominator render as `—`, not `0`.
- Day-precision triggers are excluded from hour-granularity bins (Table 4
  Panel A); they appear only in Panel B's coarser day-granularity
  bands.
- `trigger_is_action` events (C4) are excluded from both Panel A and
  Panel B of Table 4 and surfaced in Panel C only.
- Every row in Table 6 must list at least one evidence anchor; a
  `NONE` row indicates a validator regression and is a ship-blocker.

## 5. Phrasing catalog (copy-paste from `docs/limitations-and-use.md §6`)

- **Prefer**: "observed changes", "first observed change",
  "coverage-matched conditional rate", "the admitted corpus",
  "within the scoped window and sources", "historically associated
  with", "plausible vs direct attribution".
- **Forbid**: "causes censorship", "future censorship likelihood",
  "probability of enforcement", "risk score", "did not react" (when
  layer is un-measured), "multi-layer cascade rate" (under-powered
  per Table 3 `multi_layer` row), "recovery rate" (n=1; one reversal
  event in the corpus).

## 6. Review + sign-off

This file is a contract between the maintainer and the reviewer.
Changes require:

1. An updated CHANGELOG entry with the specific claim(s) added or
   removed.
2. If a claim is **added**: the paper-table generator must produce
   the cited number, and the relevant anchor audits must be
   completed (`last_human_audit` stamped for each anchor event
   cited).
3. If a claim is **rephrased**: show the old and new sentence
   side-by-side in the CHANGELOG entry.
4. If a claim is **removed**: state the reason and whether it is
   parked for a later version (`v0.2+`) or ruled out entirely.
