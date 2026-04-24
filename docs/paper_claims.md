# Paper claims · v0.1 skeleton

> **Status**: skeleton. Every claim below is a candidate; nothing is
> promoted to the paper until (a) the anchor audits for its supporting
> events are complete, and (b) the paper table generator (planned
> `analysis/paper_tables.py`) reproduces the cited numbers from the
> committed dataset snapshot.

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

- Trigger timestamp precision across the corpus:
  48 events are day-precision (e.g. OFAC SDN listings publish to
  day granularity only); 5 events are hour-precision or better.
- **Only the hour-or-better subset may carry an hour-precision latency
  claim.** Day-precision triggers appear in per-event narratives and
  in tables marked as "≤1 day" bucketed; they are excluded from any
  hour-granularity latency distribution.
- The planned paper-table generator filters `time_to_first_change_hours`
  by trigger precision before emitting any hour-granularity bin.

## 1. Candidate claims (ranked by strength of current evidence)

Each claim below names the `derived/` artifact that feeds it, the exact
subset of events admissible, and the phrasing lock.

### C1 · Upper-layer concentration of observed reactions

**Claim (phrasing-locked)**:

> "Across 53 admitted events, observed changes are concentrated on
> the upper layers of the six-layer stack. Under coverage-matched
> denominators, `asset_onchain` shows `changed_given_measured` = 17/17
> (1.00), `l4_frontend` = 11/16 (0.6875), and `offramp_cex` = 15/25
> (0.60). `l0_network` carries no measured denominator, and
> `l3_rpc`'s denominator is partially-measured-only; neither supports
> a comparable rate. This is a description of the admitted evidence
> corpus, not of the underlying phenomenon."

- **Evidence**: `derived/layer_observability.csv`; coverage-matched
  numerator (per P1 fix, 2026-04-23).
- **n**: 53 events across 6 layers.
- **Case role**: all 53 (empirical + null + anchor all contribute
  coverage denominators; only observed_change rows enter the
  numerator).
- **Phrasing lock**:
  - PREFER "are concentrated", "observed changes", "coverage-matched
    conditional rate".
  - FORBID "L0 does not react", "L3 is censorship-resistant", any
    rate built on a null denominator.
- **Not said**: this claim does NOT assert that base layers are not
  censored. That is an observability gap. See
  `docs/chain-coverage-note.md` and `docs/limitations-and-use.md §2.4`.

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

> "Restricted to triggers with hour-or-better precision (n=5), the
> first observed change at any layer occurred within the same hour
> in K cases, within 1–30h in M cases, and beyond 30h in L cases.
> Day-precision triggers (n=48) are reported separately in a
> ≤1-day-bucketed latency table in the appendix; they are excluded
> from the hour-granularity distribution."

- **Evidence**: `derived/event_metrics.csv ::
  time_to_first_change_hours`, **filtered** by trigger precision
  (paper-table generator responsibility; currently computed in
  `scripts/assign_archetypes.py::latency_regime`).
- **n**: 5 hour-precision events + 48 day-precision events (reported
  separately).
- **Case role**: all events with at least one `observed_change`.
- **Phrasing lock**:
  - PREFER "first observed change", "conditional on
    hour-or-better trigger precision".
  - FORBID any latency number expressed in hours that includes a
    day-precision trigger; "reaction time" as a scalar summary
    across all 53 (precision-mixed).
- **Not said**: this is NOT a decomposition by layer speed — that is
  C4 below if promoted.
- **Dependency**: C3 needs `scripts/paper_tables.py` step 4 (latency
  distribution with precision filter) before it can be anchored by
  a citable number. Until then, C3 stays a candidate.

### C4 · Corporate-policy events are trigger-action identical

**Claim**:

> "Five events in the admitted corpus carry
> `trigger.type = corporate_policy_change` and `trigger_is_action =
> true`; the trigger timestamp and the first observed change
> timestamp are identical in the record by construction. These five
> events (Circle-USDC Tornado freeze 2022, three Tether freeze
> events, Uniswap frontend delisting 2023) are reported as their own
> category and excluded from any cross-event latency claim: their
> `time_to_first_change_hours = 0` is a record-level artifact, not a
> measured delay."

- **Evidence**: `derived/event_archetypes.csv :: trigger_is_action`;
  `derived/archetype_distribution.md §4` edge-case note.
- **n**: 5.
- **Case role**: named; cited by event slug.
- **Phrasing lock**:
  - PREFER "record-level artifact", "trigger is the action itself".
  - FORBID "fastest cascade" (t=0 is not speed); "self-executing
    sanctions" (editorializes beyond the record).

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
  trigger-type × latency cross-tab at n=5 per cell is under-powered.
  Parked for v0.2 after more hour-precision events accumulate.
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

The five `corporate_policy_change` events (see C4) are reported as a
distinct category. Cross-event latency statements must aggregate the
two subsets separately.

## 4. Planned paper-table generator (prerequisite for promoting claims)

`analysis/paper_tables.py` (not yet written) must produce:

1. **Case-role table** — per-event `admission_tier` + `research_stratum`
   + `empirical_shape`, one row per event.
2. **Layer-observability table** — direct re-emission of
   `derived/layer_observability.csv`, with denominator bucket
   composition.
3. **Changed-layer distribution** — archetype counts × stratum
   cross-tab.
4. **Latency distribution (precision-filtered)** — hour-bucketed
   latency for hour-or-better-precision triggers only; day-bucketed
   latency for day-precision triggers (separate panel).
5. **Complete-vs-subset stratification** — for events where the target
   is a complete entity address set vs a named subset, a side-by-side
   summary of changed-layer counts.
6. **Null-case denominator table** — the 13 null events with their
   scoped `observed_no_change` window + evidence-anchor type, so the
   denominator is auditable.

Each of C1–C6 is frozen to its exact number by the relevant table.
Numbers not produced by that generator do not enter the paper.

## 5. Phrasing catalog (copy-paste from `docs/limitations-and-use.md §6`)

- **Prefer**: "observed changes", "first observed change",
  "coverage-matched conditional rate", "the admitted corpus",
  "within the scoped window and sources", "historically associated
  with", "plausible vs direct attribution".
- **Forbid**: "causes censorship", "future censorship likelihood",
  "probability of enforcement", "risk score", "did not react" (when
  layer is un-measured), "multi-layer cascade rate" (n=5),
  "recovery rate" (n=1).

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
