# Evaluation-profile schema (v0.1)

> **Status**: schema definition only. No per-stack profile is populated
> yet. This document defines the rubric dimensions and the ordinal
> grading convention that `derived/evaluation_profile.{csv,json}` will
> carry once v0.1 stack features are recorded.

## 1. Framing: history-calibrated exposure rubric

We are **not** producing a single "censorship-resistance score". We are
producing a **rubric** of exposure dimensions, each graded ordinally, each
calibrated against the empirical archetype frequencies from the event
panel. Consumers read the rubric as a vector / radar, never as a rank.

Inputs:
- **Stack features** (architectural facts, v0.1 per-stack snapshot) —
  see [`stack-features-schema.md`](stack-features-schema.md)
- **Archetype frequencies** (how often each layer-pattern cascade has
  been observed in the evidence corpus) — see
  `derived/event_archetypes.*` and `derived/layer_observability.*`
- **Coverage denominators** (what we've measured vs what's an
  observability gap) — see `derived/layer_observability.*`

Output:
- A per-stack row in `derived/evaluation_profile.csv` with five ordinal
  dimension grades + an Evidence Confidence qualifier.

## 2. Why ordinal, not numeric

Three reasons, in decreasing order of importance:

1. **Sample size**. 51 admitted events across 5–6 archetypes; many
   archetype × stack-type cells will have n < 5. Numeric scores invite
   downstream arithmetic (averaging, ratio-taking) that the cells do
   not support.
2. **Incommensurability**. Frontend exposure and off-ramp exposure
   operate through different mechanisms. Aggregating them into a scalar
   forces an implicit weighting that neither the data nor the
   methodology can defend.
3. **Reviewer skepticism**. A numeric "resistance score" is the exact
   pattern that has been criticised in adjacent dataset literature
   (Freedom House press-freedom indices, ESG scores, etc.). Ordinal
   profile grades + sample-count disclosure sidestep the entire
   criticism.

Ordinal levels used uniformly across dimensions:

| Level | Meaning |
| --- | --- |
| `high` | Feature pattern strongly present + archetype frequency supports the mapping |
| `medium` | Feature pattern partially present OR archetype frequency is sparse |
| `low` | Feature pattern largely absent + archetype frequency low |
| `insufficient` | Evidence too thin to grade (e.g. `evidence_confidence: insufficient`) — explicitly NOT "low" |

## 3. Dimensions (v0.1)

Exactly five. Recoverability is **intentionally excluded** from v0.1
because the corpus carries a single reversal event (n=1).

### A. Frontend Enforcement Exposure

**Claim form**: "Stack X is historically associated with *high / medium /
low* exposure to frontend-layer enforcement, measured as: (1) archetype
frequency of `frontend_only` + `multi_layer`-with-l4 signatures in
stack-matched events, and (2) presence of the frontend-control
architectural features that those events exploited."

**Inputs**:
- Event-side: `frontend_only` count + multi-layer with-`l4_frontend`
  signature count, scoped to events whose target matches this stack
- Feature-side: `canonical_frontend_dependency`,
  `dns_domain_chokepoint_dependency`, `client_requires_operator_backend`,
  `frontend_operator_jurisdiction` (US / EU vs offshore)

**Grading heuristic** (explicit, for v0.1):
- `high` = at least one event of each type (frontend_only + with-l4
  multi-layer) present in evidence for this stack's target profile
  AND ≥ 2 high-graded features in frontend family
- `medium` = one class of events observed OR ≥ 1 high-graded feature
- `low` = neither events nor high-graded features

### B. Asset Enforcement Exposure

**Claim form**: "Stack X is historically associated with *level* exposure
to asset-layer enforcement, based on (1) `asset_only` + with-`asset_onchain`
multi-layer archetype frequency, and (2) freezeable-asset dependency +
primary_asset_admin_scope."

**Inputs**:
- Event-side: `asset_only` count + multi-layer-with-`asset_onchain`
  signature count
- Feature-side: `primary_asset_admin_scope` (contains `freeze`?),
  `freezeable_asset_dependency`, `issuer_freeze_power`,
  `primary_asset_admin_jurisdiction`

**Grading heuristic**:
- `high` = `freezeable_asset_dependency` high AND admin scope contains
  `freeze` AND ≥ 1 asset-archetype event matches target profile
- `medium` = one of the three
- `low` = none

The layer-observability data (100% conditional change on measured
asset layers) means *any* freeze-capable dependency in the stack should
be taken seriously — this heuristic is deliberately conservative.

### C. Off-ramp Enforcement Exposure

**Claim form**: "Stack X is historically associated with *level* exposure
to off-ramp enforcement, based on `cex_only` + with-`offramp_cex`
multi-layer archetype frequency and `cex_exit_dependency`."

**Inputs**:
- Event-side: `cex_only` count (the dataset's largest single bucket at
  n = 14) + multi-layer-with-`offramp_cex` signatures
- Feature-side: `cex_exit_dependency`, `dex_exit_feasibility`
  (inverse — high dex feasibility depresses the dimension),
  `primary_fiat_onramp_jurisdiction`

**Grading heuristic**:
- `high` = high `cex_exit_dependency` AND low `dex_exit_feasibility`
- `medium` = mixed
- `low` = high `dex_exit_feasibility` AND multiple non-US onramps

### D. Coordination Surface Density

**Claim form**: "Stack X exhibits *level* cross-layer coordination
potential — how many upper-layer choke points *co-exist* and could be
triggered by a single action."

**This is the only dimension that reads the *multi_layer* signature
distribution directly**. Not a simple count of features — a measure of
how tightly coupled those features are. If a stack has both issuer
freeze AND canonical frontend AND CEX-dominant off-ramp, **and** we
have observed multi-layer cascades that activate all three, the density
is high.

**Inputs**:
- Event-side: multi-layer archetype count for stack-matched events,
  weighted by signature breadth (a 3-layer signature ≠ 2-layer signature)
- Feature-side: number of upper-layer families with ≥ 1 high-graded
  feature

**Grading heuristic**:
- `high` = multi-layer archetype observed for stack-matched events AND
  ≥ 2 upper-layer families carry high-graded features
- `medium` = one of the two
- `low` = neither

### E. Evidence Confidence

**Claim form**: "The profile above is supported by *level* evidence
strength, based on (1) event-panel sample count in stack-matched
archetype cells, (2) coverage-denominator strength for the layers
referenced, and (3) feature-annotation confidence."

**Inputs**:
- stack-matched event count across all archetypes
- `layer_observability.csv::changed_given_measured` for the layers the
  other four dimensions depend on (high if the layer is
  measured-majority; low if the layer is `not_measured`-majority or has
  zero measured denominator)
- fraction of stack features recorded at `confidence: high`

**Grading heuristic**:
- `high` = ≥ 5 stack-matched events AND ≥ 80% of feeding-layer
  denominators measured AND ≥ 80% of features at `confidence: high`
- `medium` = any one of the three at a lower threshold
- `low` = two or more at a lower threshold
- `insufficient` = any feeding-layer has `changed_given_measured` = null
  (no measured denominator); the per-dimension grade becomes
  `insufficient` rather than `low`

**This dimension can downgrade the others.** If Evidence Confidence is
`insufficient` for a particular stack, the companion-dimension grades
are rendered as "`A: high (evidence: insufficient)`" so the reader
cannot miss the qualifier.

## 4. Why these five and not others

Explicitly excluded from v0.1 and the reason:

- **Recoverability** — n=1 reversal event in the corpus
  (`tornado-cash-ofac-delisting-2025`). Promoted to v0.2 or later when
  n ≥ 3 reversal events accumulate.
- **Bypass Cost (user-side)** — requires per-stack measurement of
  friction costs (DEX slippage, self-hosting friction, privacy-tool
  availability) that are not in the evidence layer. v0.2 candidate
  after bypass-measurement instrumentation is added.
- **Detection Lag** — requires systematic timeline comparison between
  event and public awareness; not structurally encoded in events.
- **Composite index** — explicitly deferred indefinitely pending
  reviewer-driven demand.

## 5. Output shape

`derived/evaluation_profile.csv` columns (one row per stack snapshot):

```
stack_id
measured_at
frontend_enforcement_exposure       {high, medium, low, insufficient}
asset_enforcement_exposure          {high, medium, low, insufficient}
offramp_enforcement_exposure        {high, medium, low, insufficient}
coordination_surface_density        {high, medium, low, insufficient}
evidence_confidence                 {high, medium, low, insufficient}
stack_matched_event_count           numeric
stack_matched_archetypes            comma-separated archetype names
notes                               free-form, ≤ 200 chars
```

`derived/evaluation_profile.json` carries the same fields plus a
`dimensions[]` array with per-dimension inputs (which events matched,
which features dominated the grade) so a reader can trace any grade
back to its evidence.

## 6. Phrasing discipline

Borrowed verbatim from `docs/limitations-and-use.md`:

- **Prefer** "historically associated with", "structurally exposed to",
  "evaluation profile", "grades against rubric"
- **Forbid** "future censorship likelihood", "risk score", "will be
  censored", "probability of enforcement"

The rubric describes *history*, not *future*. The fact that a dimension
is graded `high` means the combination of past events + structural
features places the stack in a historically-high-exposure position; it
does not imply any specific future action.

## 7. Revision and governance

- The rubric definition (this document) is revised with explicit
  CHANGELOG entries, same as the schema versioning policy in
  [`releasing.md`](releasing.md).
- Individual stack-profile rows are append-only (see
  `stack-features-schema.md` §7).
- A rubric revision that changes the meaning of a grade level (e.g.
  "high" now requires n ≥ 7 matched events) triggers a MAJOR dataset
  version bump.
