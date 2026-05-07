# Paper claims · v0.1 A-class submission lock

> **Status**: submission-lock draft. Every promoted claim below must stay
> bounded by its table source, case-role scope, denominator class, and audit
> gate. The current working snapshot is not strict-submission-ready until the
> Human-Expert-Audit items in [`../human-audit.md`](../human-audit.md) are
> completed and
> `python3 scripts/check_paper_readiness.py --strict-audit --strict-null-audit --strict-repro --strict-reliability`
> passes from a clean intended source tree.

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

**Dataset snapshot**: v0.1.0 · cutoff 2026-05-06 · 53 YAML records, 53 admitted events.

### Primary finding (headline) and primary estimand

**Headline finding**:

> **Cross-layer censorship measurement needs explicit denominators, not
> implicit zeros.** This corpus packages a six-artifact measurement
> protocol, 53 admitted event records, and fail-closed paper tables that
> connect legal / policy triggers to observed stack-layer reactions only
> where a replayable evidence substrate exists. The Flashbots
> `rpc-endpoint::ofacblacklist.go` bookend is the worked mechanism case:
> PR #90 adds Tornado Cash pool addresses **2h 50m** after the 2022-08-08
> OFAC SDN, and PR #173 removes the 132-address blacklist eleven days
> after OFAC's 2025-03-21 delisting. The point is a denominator-aware,
> reproducible event-measurement protocol, not a population claim about
> operator behavior or global censorship prevalence.

**Primary estimand (supporting)**:

> **Among publicly observable stack layers *and under an
> admission-grade evidence substrate*, which layers carry detectable
> reactions to an identified legal / policy trigger, and which layers'
> conditional rates are undefined because the public evidentiary
> denominator does not exist?**

The re-framing matters: the estimand's numerator is "observed changes
that the admission protocol admits", and its denominator is "events
where the layer has `measured` or `partially_measured` coverage" — NOT
"events where the layer could hypothetically react." A layer with zero
`measured` denominators (L0 in the current corpus) renders `—`, not
`0`; this is a measurement contribution in its own right.

Why this framing, not the alternatives:

- "**Full cascade is rare — why?**" is motivating background but the
  `multi_layer` archetype count (see Table 3) is too thin for a
  standalone prevalence claim; furthermore, two of those events are
  Tornado forward/reverse on the same target and are not independent.
  Reserved as secondary framing.
- "**Reaction speed by issuer / frontend / CEX**" is downstream of the
  primary estimand (a sub-breakdown). Primary estimand answers layer
  *selection and observability*; speed is a column of the same table
  and is under-powered in Panel A of Table 4 at the current corpus
  size.
- "**Six-layer cascade dataset**" (earlier framing) over-sold: two of
  six layers have zero measured denominators at v0.1.0. The honest
  framing is *upper-stack observability under coverage-denominator
  discipline, with a worked mechanism case on operator source code*.

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
| `anchor_case` | hand-audited exemplars; figures + narrative spotlight | see Table 1 |
| `empirical_case` | aggregate-count contributors (distributions, tables) | see Table 1 |
| `null_case` | denominator for "we looked and observed no change" | see Table 1 |

A claim may NOT cite an `empirical_case` for a narrative spotlight
role, nor a `null_case` for a "changed-layer" count. The paper-table
generator is live and emits the case-role surface in Table 1.

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

**Plausible and direct observations are not collapsed into a causal
claim.** Tables may aggregate row counts, but paper prose must preserve
the distinction. Attribution-dependent comparative claims remain
parked until `attribution` κ clears the reliability gate.

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

### Six artifact measurement protocol

The paper's primary contribution is a measurement protocol plus a
reproducible corpus, not a hand-picked case list. The protocol is
implemented as six artifacts that must be cited together:

| artifact | live path | role |
| --- | --- | --- |
| Trigger registry | [`analysis/trigger_registry/trigger_registry.md`](../analysis/trigger_registry/trigger_registry.md) | pre-admission surface for all event YAML records plus candidate/rejected trigger stubs; makes expansion gaps visible |
| Event corpus | [`events/*.yaml`](../events/) | ground-truth trigger, coverage, observation, and source records |
| Coverage matrix | [`derived/coverage_matrix.md`](../derived/coverage_matrix.md), [`derived/l0_coverage_summary.md`](../derived/l0_coverage_summary.md) | event-by-layer denominator eligibility; distinguishes measured denominators from observability gaps, including zero-result OONI query windows |
| Evidence chains | [`analysis/evidence-chains/`](../analysis/evidence-chains/) | claim -> observation -> source -> archive/hash -> limitation rendering per admitted event |
| Paper-table generator | [`scripts/build_paper_tables.py`](../scripts/build_paper_tables.py) | admitted-only, fail-closed table surface for paper-facing numbers |
| Audit and sensitivity package | [`analysis/audit_worksheets/`](../analysis/audit_worksheets/), [`derived/admission_sensitivity.md`](../derived/admission_sensitivity.md), [`analysis/inter_rater/kappa_report.md`](../analysis/inter_rater/kappa_report.md), [`analysis/staleness.md`](../analysis/staleness.md) | human-audit, rubric sensitivity, recoding consistency, and freshness gates |

### Trigger registry

The trigger registry is the selection-bias guard. It currently contains
the 53 admitted YAML event records plus the first OFAC recent-actions
backfill: 73 candidate/promoted/screened stubs generated from cached
triage output. It is designed to absorb
`candidate_triggers/*.yaml` and `candidate_triggers/rejected/*.yaml`
before promotion to `events/`.
The registry reports raw audit rows separately from distinct in-frame
triggers. The v0.2 target is 150-250 distinct in-frame triggers and
80-120 admitted events under the declared frame in
[`sampling/frame.yaml`](../sampling/frame.yaml). Registry gaps are
expansion backlog, not paper results.

### Sampling frame

The v0.1 sampling frame is **publicly documented, English-indexable
crypto censorship events with an identifiable legal, regulatory,
state, or corporate trigger and at least one independently
archivable evidence surface**. This is an evidence-bearing research
frame, not a population sample.

**Jurisdictional composition (v0.1)**: 40/53 admitted events
(**75.5%**) carry `US` in their `jurisdiction` list. Region
membership is **inclusive of multi-jurisdiction events** so the
shares do not sum to 100%: 13/53 (24.5%) touch Europe (UK / EU /
DE / NL / PL / PT / CH / IS), 13/53 (24.5%) touch Rest-of-World
(RU / CN / IN / KR / NG / TR / AU / CA), 4/53 (7.5%) are
corporate-global with no jurisdiction. See
[`analysis/paper_tables/table7_jurisdiction_distribution.md`](../analysis/paper_tables/table7_jurisdiction_distribution.md)
for the inclusive-counting caveat (column sum exceeds corpus
total). This concentration is a property of the frame, not the
phenomenon: the public-English-language-archival requirement plus
the high absolute volume of OFAC / DOJ / SEC activity in 2022-2025
drives the US share. The paper's abstract and §1 **must** carry
the phrase "US-trigger-dominant" or equivalent; landscape claims
beyond that are out of scope at v0.1.

In scope:

- legal / regulatory / state / corporate actions with a concrete
  crypto target (`address_set`, `entity`, `domain`, `protocol`, or
  equivalent);
- events where the trigger and at least one layer-level observation can
  be archived with `body_hash` / `body_path`, `query_hash`,
  `measurement_ids`, or a primary on-chain identifier;
- null cases where a scoped `observed_no_change` row has an admissible
  evidence anchor. For off-ramp CEX nulls, this is a public-evidence
  disclosure denominator, not proof that no private exchange compliance
  action occurred; see `analysis/llm_expert_audit/null_case_pre_audit.md`
  for the LLM pre-audit triage that must be resolved by Human-Expert-Audit
  before narrative spotlight use.

Out of scope:

- private compliance signals unavailable to public verification;
- rumor-only or anonymous social-media claims;
- general crypto-market policy changes without a concrete target;
- population prevalence claims over "all censorship events";
- non-English-indexable events (Russian-language VTB/RBK filings,
  Chinese-language PBOC implementation circulars beyond the 2021
  anchor, Iranian IRGC internal materials). These are named open
  work for v0.2 scope expansion.

### Claim-to-table-source matrix

Every paper claim must land in this matrix before it appears in prose.
If a claim cannot name a table, source fields, and an uncertainty
boundary, it stays out of v0.1.

| claim | reader-facing table | underlying fields | case role admitted | audit gate | uncertainty boundary |
| --- | --- | --- | --- | --- | --- |
| C0 selection transparency | Trigger registry + coverage matrix | `registry_status`, `research_stratum`, `coverage.status`, `denominator_class` | all YAML events plus candidate/rejected stubs when present | `make trigger-registry`, `make coverage-matrix`, and `make l0-coverage-summary` must pass | expansion gaps are backlog, not results; registry rows outside `admitted` never feed paper counts; zero OONI results are observability gaps |
| C1 upper-stack admissible-evidence concentration | Table 2 `layer_observability` + coverage matrix denominator reasons | `coverage[]`, `observations[].layer`, `observation_kind`, `denominator_reason` | all 53 admitted events for denominators; changed rows for numerators | anchor rows cited by name need `last_human_audit`; aggregate table remains descriptive until independent-human `observation_kind` κ ≥ 0.6 | coverage-matched rates only; no population prevalence; not a layer-propensity comparison; substrate-existence rows do not count as L3 coverage |
| C2 single-layer dominance | Table 3 `archetype_stratum` | `derived_archetype`, `changed_layer_count`, `research_stratum` | all 53 admitted events | parked until independent-human `observation_kind` κ ≥ 0.6 | corpus archetype distribution, not clustering or population rate |
| C3 latency | Table 4 Panels A/B/C | `trigger.timestamp_precision`, `time_to_first_change_hours`, day-precision latency interval bounds, `trigger_is_action` | timed `observed_change` rows only | any named latency exemplar needs audit | hour claims only from Panel A; day rows use interval bands with `ambiguous_boundary`; trigger-is-action panels separate |
| C4 trigger-is-action | Table 4 Panel C | `trigger.type`, `trigger_is_action` | `corporate_policy_change` events | named examples need audit | `t≈0` is record structure, not reaction speed |
| C5 cross-stratum reach | Table 3 | `research_stratum`, `derived_archetype` | all 53 admitted events | descriptive until independent-human `observation_kind` κ ≥ 0.6 | stratum is an admission frame, not jurisdiction or population weight |
| ~~C6 recovery insufficiency~~ **[DEMOTED to exemplar-inside-C1; see §C6 below]** | — | — | — | — | reversal appears only as a narrative exemplar inside the Flashbots bidirectional mechanism finding, never as a standalone claim |

### Uncertainty-to-analysis mapping

| uncertainty source | required treatment |
| --- | --- |
| day-level trigger timestamps | report only in Table 4 Panel B interval buckets; cross-boundary rows become `ambiguous_boundary`; never in hour bins |
| `trigger_is_action` rows | isolate in Table 4 Panel C; never call them fast reactions |
| `plausible` attribution | phrase as co-occurrence / consistency, not direct causation |
| `not_measured` coverage | phrase as observability gap, not no reaction |
| `target.enumeration: subset` | say "named subset" rather than protocol-wide target |
| missing `last_human_audit` | allowed for aggregate tables with warning; blocks narrative spotlight use |

### Prior-art delta (required for §2 of the paper)

#### Methodology ancestors (transplanted, not invented)

| ancestor | year / venue | what it established | how this project uses it |
| --- | --- | --- | --- |
| Filastò & Appelbaum, "OONI: Open Observatory of Network Interference" | 2012 · FOCI | Public, auditable, probe-based network-censorship measurement with per-measurement metadata. | `scripts/ooni_batch_query.py` queries the OONI Explorer API; `derived/l0_coverage_summary.md` records whether a query produced a denominator or only an observability gap. |
| Pearce et al., "Global Measurement of DNS Manipulation" | 2017 · USENIX Sec | Coverage-matched conditional-rate reporting: rates are reported only over measured vantages; nulls-vs-unmeasured are distinguished. | Transplanted as the project's **coverage-denominator discipline** (`§0 Sampling frame`). Every conditional rate in Table 2 is conditional on the layer's denominator being `measured` or `measured_or_partial`. |
| Sundara Raman et al., "Censored Planet" | 2020 · CCS | Global longitudinal connection-tampering observatory; per-jurisdiction coverage tracking; explicit denominator accounting. | Consumed as a semi-primary source for L0 events (`docs/methodology.md §4.1`). Coverage-availability window (2018+) drives the `not_available_pre_2018` status for L0 on older events. |
| Gebru et al., "Datasheets for Datasets" | 2021 · CACM | Dataset documentation template covering motivation, composition, collection, recommended uses, distribution, maintenance. | `docs/datasheet.md` is the templated intake page. |
| Heimbach & Wattenhofer / Kelkar et al. on PBS as a censorship surface | 2022+ · AFT/IMC | Formal framing of proposer-builder separation as a censorship attack surface. | Motivates the L1-consensus layer definition; Wahrstätter et al. 2024 is the measured-data side of the same phenomenon. |

#### Concurrent / closest-prior crypto-censorship work — per-axis delta

The single closest paper is Wahrstätter, Ernstberger, Yaish et al.,
**"Blockchain Censorship" (ACM WebConf 2024)**. The paper's §2 must
lift this table rather than write a new one.

| axis | Wahrstätter et al. (WWW 2024) | this project |
| --- | --- | --- |
| **Layer coverage** | L1 relay / builder filtering on Ethereum post-Merge (PBS). | Six-layer span: L0 network, L1 consensus, L3 RPC, L4 frontend, asset_onchain, offramp_cex. |
| **Unit of observation** | Block / transaction (millions per window). | Event (n=53 admitted YAML records) plus, in v0.1, a paired census surface — 8 operator repos with substrate-edit ledger ([`analysis/operator_census/`](../analysis/operator_census/)) — and a fail-closed paper-table generator. |
| **Trigger model** | Implicit (OFAC SDN list as a static block-time filter). | Explicit `trigger.*` with timestamp precision, actor, jurisdiction; precision-aware latency panels separate hour-grade from day-grade. |
| **Coverage discipline** | Per-relay prevalence; denominators are blocks, not events. | Coverage-matched conditional rates over events with `measured / partially_measured / not_measured / not_applicable` as distinct states; rate emission aborts on denominator mismatch (`scripts/build_paper_tables.py` fail-closed). Three-rubric strict/current/permissive ablation reports sensitivity per layer. |
| **Operator substrate** | Not examined as a first-class measurement channel; relay filtering is inferred from block content, not from operator source code. | `analysis/operator_census/` surveys 8 public operator repositories for git-history OFAC edits and **tiers them into `confirmed_filter_file` (n=2) / `glob_swept_matched` (n=2) / `schema_or_index_only` (n=1) / `glob_swept_zero` (n=3)**. Reports two parallel headline numbers: 5 known-channel substrate edits across 1 confirmed-substrate repo (the wide ledger), and 1 OFAC-keyword-subject commit across the entire corpus (the narrow keyword classifier). Treats public git-history of operator compliance as a measurable substrate with minute-level precision where it exists. |
| **Recovery / reversal** | Not addressed (the paper's cutoff predates OFAC's 2025-03-21 Tornado delisting). | Demoted to exemplar-inside-C1 (n=1; not a standalone claim — see §C6). Visible inside the substrate-edit ledger as PR #173 (2025-04-01 deletion). |
| **Reproducibility** | Data + code published. | Pinned `requirements*.txt`, `SOURCE_DATE_EPOCH` byte-stable artifacts, fail-closed paper-table generator, pytest regression suite, blind inter-rater reliability sampler + κ calculator (with provenance taxonomy), CI gate that exercises the reproduction path (`make regenerate` + `make paper-check` + byte-stability round-trip). |
| **Inter-rater reliability** | Not reported (their measurement is programmatic over block data, so κ on author labels is not the applicable check). | `coverage_status`, `observation_kind`, and `attribution` self-consistency κ = 1.0 under `llm_assisted_blinded` provenance (`analysis/inter_rater/kappa_report.md`). Cited as self-consistency, not as inter-rater reliability; an `independent_human` pass is open work for v0.2. |

The clean framing for the paper: **Wahrstätter et al. is an
intra-L1 measurement census; this project is a cross-layer event
corpus where L1 numbers come from Wahrstätter as a semi-primary
input, plus a separately-reported operator-source-control
substrate the block-level frame does not address.** This work does
not compete at the L1-prevalence question.

#### Other crypto-censorship prior art (cited briefly)

- **Nadler & Schär, "Sanctions and the MEV Supply Chain" / Tornado-Cash effects** (2023+): economic / flow-level analysis. Cited as motivation, not overlap.
- **Daian et al., "Flash Boys 2.0"** (2020 · S&P): MEV-as-censorship-surface concept; cited for framing.
- **Piet & Jadliwala / Arnbak-style work on dApp frontend geoblocking** (2023-2024 · PETS): orthogonal substrate; gives vocabulary, not numerical overlap.
- **Chainalysis / Elliptic / TRM compliance reports**: asset-layer freeze reporting under proprietary feeds. Not event-keyed; this project's `asset_onchain` rows come from on-chain logs directly.
- **Censorship.pics (Wahrstätter) / mevwatch / relayscan.io**: live dashboards consumed as semi-primary inputs; credited in `docs/methodology.md §4.2`.
- **Informal blog posts on `ofacblacklist.go`** (Amadeo / Pestritto, 2022-2023): not peer-reviewed. This work's contribution is the reproducible audit + multi-repo census + admission-grade anchoring of the same finding.

#### Self-honest gaps

The paper's §2 must also acknowledge what this work does NOT
advance relative to prior art:

- Not a replacement for Wahrstätter et al.'s L1 census — their block-level prevalence is what gives this project's L1 numerator meaning.
- Not a replacement for Chainalysis / TRM at the compliance-tool level — this project says nothing about address-clustering accuracy.
- Not a generalization of OONI's methodology to a new domain — this project consumes OONI; it does not extend its probe infrastructure.
- Not a discovery of operator-layer censorship as a phenomenon — that is well-documented informally. v0.1 adds a **reproducible measurement frame**, a **tiered substrate census**, and an **admission protocol** that places the phenomenon in a coverage-discipline context.

### Reliability discipline (required for §3 of the paper)

Every conditional rate in the paper has a corresponding κ floor.
**Read the provenance mode before citing the κ value as
"reliability"** — the same number is a reliability estimate under
`independent_human` provenance and a *self-consistency check* under
`llm_assisted_blinded` (see
`scripts/compute_irr_kappa.py::main` and the provenance taxonomy in
the kappa report's "Interpretation" section).

Current state (v0.1):

- **`coverage.status`**: κ = 1.0 (n=90 rows, 15 events) under
  `llm_assisted_blinded` provenance.
- **`observation_kind`**: κ = 1.0 (n=25 rows, 15-event blind sample)
  under `llm_assisted_blinded` provenance.
- **`attribution`**: κ = 1.0 (n=20 rows, changed-observation blind
  sample) under `llm_assisted_blinded` provenance.

All three must be cited as a **self-consistency check,
single-coder LLM-assisted blinded recode**, not as independent-human
inter-rater reliability. The Landis & Koch *almost-perfect* label
applies on the scale, but the substantive claim is bounded by
provenance: gold and recode may share systematic biases, so the κ is
a consistency floor, not an independent reliability estimate. An
`independent_human` pass remains open work for v0.2.

**Phrasing lock for the paper**: when citing κ, use
"self-consistency check (LLM-assisted blinded recode), n=90/25/20,
κ=1.0" or equivalent; do **not** use bare "almost perfect inter-
rater agreement" without naming the provenance mode. The paper's
§3 must not report a conditional rate whose underlying variable
sits below κ ≥ 0.6 under any pass. Protocol + provenance taxonomy
implemented in `scripts/build_irr_sample.py` and
`scripts/compute_irr_kappa.py`; live report at
`analysis/inter_rater/kappa_report.md`.

## 1. Candidate claims (ranked by strength of current evidence)

Each claim below names the `derived/` artifact that feeds it, the exact
subset of events admissible, and the phrasing lock.

### C1 · Upper-stack concentration of publicly admissible evidence

**Claim (phrasing-locked)**:

> "Across 53 admitted events, publicly admissible observed-change
> evidence is concentrated on upper-stack substrates. Under coverage-matched
> denominators reported across three admission rubrics
> (strict / current / permissive — see `derived/admission_sensitivity.md`):
>
> - `l4_frontend` = **8/14 (0.57) strict, 10/14 (0.71) current,
>   12/17 (0.71) permissive** — sensitivity Δ=0.13; the rate moves
>   meaningfully under rubric, so all three are reported.
> - `offramp_cex` = **13/25 (0.52) strict, 15/25 (0.60) current,
>   16/26 (0.62) permissive** — moderate sensitivity (Δ=0.095).
> - `l1_consensus` = **0/6 (0.00) strict, 1/6 (0.17) current,
>   2/7 (0.29) permissive** — sensitivity Δ=0.29; both
>   measured-or-partial change rows are anchored on Tornado Cash
>   events.
> - `l3_rpc` has **no `measured`-coverage events** in the corpus;
>   it carries two named Flashbots `rpc-endpoint` git-history
>   observations (PR #90 adding Tornado pool addresses 2022-08-08,
>   PR #173 deleting the blacklist 2025-04-01), but emits **no L3
>   conditional rate**.
> - `l0_network` carries no `measured` denominator.
> - `asset_onchain` is **NOT reported as a rate** at v0.1: see the
>   structural-circularity note in 'Not said' below.
>
> The claim is a description of the admitted evidence corpus and its
> public measurement substrates, not of layer-level reaction propensity
> in the underlying phenomenon."

- **Evidence**: `derived/layer_observability.csv` (per-rubric
  numerators) + `derived/admission_sensitivity.csv` (three-rubric
  recomputation). `analysis/paper_tables/table2_layer_observability.md`
  is the reader-facing re-emission and **must carry all three rubrics
  for `l4_frontend` and `l1_consensus`** in its emitted prose.
  `derived/coverage_matrix.csv` supplies `denominator_reason` and
  `denominator_artifact`; `docs/l0-l3-denominator-appendix.md` explains
  why L0/L3 zero denominators are not negative observations.
- **n**: 53 admitted events across 6 layers.
- **Case role**: all 53 admitted events (empirical + null + anchor all contribute
  coverage denominators; only observed_change rows enter the
  numerator).
- **Phrasing lock**:
  - PREFER "publicly admissible evidence is concentrated",
    "observed changes under the admitted evidence substrate",
    "coverage-matched conditional rate", "across the three admission
    rubrics" (whenever a sensitive layer's rate is cited).
  - FORBID:
    - "L0 does not react", "L3 is censorship-resistant" — rates
      built on a null denominator.
    - "L3 has zero observed changes" — the 2 Tornado L3 rows added
      2026-04-24 invalidate that earlier framing.
    - **citing `l4_frontend` or `l1_consensus` rate without naming
      the rubric** (so "L4 = 0.71" without "current rubric" or
      "10/14 (0.71)" is forbidden — these are the
      sensitive-to-rubric layers per
      `derived/admission_sensitivity.md`).
    - **any `asset_onchain` rate** at v0.1 (see "Not said" below).
- **Not said**:
  - **`asset_onchain` rate is structurally circular at v0.1 and
    therefore retracted.** Every event admitted to
    `asset_onchain.status = measured` (n=17) carries an
    `observed_change` row by construction of the admission rubric:
    Etherscan-recorded `Blacklisted(...)` log on the target address
    is *itself* the evidence that admits the layer as `measured`.
    No event with `measured` coverage and no observed change exists
    in the corpus, so 17/17 = 1.00 is a property of the rubric, not
    a measurement. v0.1 keeps the **descriptive observation**
    ("among 17 events admitted with `asset_onchain.measured`,
    every one carries an Etherscan-anchored issuer blacklist tx
    matching at least one SDN-listed address") but **does not
    report a rate**. Reinstatement requires admitting events under
    a coverage rubric that does not require the change as the
    admission anchor — e.g. `partially_measured` for events whose
    SDN addresses were checked against Circle/Tether and produced
    no hit. Tracked as v0.2 open work.
  - This claim does NOT assert that base layers are not censored.
    That is an observability gap. See `docs/chain-coverage-note.md`
    and `docs/limitations-and-use.md §2.4`.
  - The two L3 observations are Tornado-specific; they do NOT
    support a general "L3 filter lists react to sanctions events"
    claim beyond these two named cases.

### C2 · [PARKED] Single-layer response description pending independent-human reliability

**Descriptive table text (not a promoted central paper claim until an
independent-human reliability pass clears the gate):**

> "Of 53 admitted events, 36 (68%) show observed changes at exactly
> one layer, 4 (8%) show observed changes at two or more layers, and
> 13 (25%) show no observed change at any layer in their scoped
> window. Single-layer responses dominate the publicly-observable
> record, with `cex_only` (n=15), `asset_only` (n=13), and
> `frontend_only` (n=8) being the three dominant single-layer
> archetypes. Zero events land in the `other_single_layer` safety
> class (L0-only / L1-only / L3-only), reinforcing the upper-layer
> concentration observation."

- **Evidence**: `derived/event_archetypes.csv` +
  `derived/archetype_distribution.md` §2.
- **n**: 53 admitted events.
- **Case role**: all 53 admitted events. Null cases are 13/13 of the `null_event`
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
- **Promotion gate**: requires `observation_kind` κ ≥ 0.6 under an
  `independent_human` provenance pass in
  `analysis/inter_rater/kappa_report.md`. The current LLM-assisted blinded
  pass is a self-consistency check, so Table 3 may be shown as descriptive
  QA output but C2 must not be used as a central result.

### C3 · Hour-precision latency exemplars (NOT a distribution)

**Claim**:

> "Two admitted events carry hour-or-better trigger precision AND a
> non-trigger-action observed_change, and are reported individually as
> named exemplars: `tornado-cash-ofac-2022` (first observed change at
> L3 within 2h 50m of the OFAC SDN, via Flashbots rpc-endpoint PR #90)
> and `china-pboc-crypto-ban-2021` (first observed change within 24
> hours at the off-ramp layer). These are **named rows, not a
> distribution**; the corpus does not support a hour-precision latency
> distribution at v0.1.0. Day-precision triggers with a timed
> `observed_change` are reported separately in Panel B as interval
> evidence (`≤1d`, `(1d,30d]`, `>30d`, or `ambiguous_boundary`) and
> are never mixed into any
> hour-granularity claim. `trigger_is_action` events (Panel C) are
> excluded from both A and B because their `t≈0` is a record-level
> artifact, not a measured delta."

- **Evidence**:
  [`analysis/paper_tables/table4_latency_by_precision.md`](../analysis/paper_tables/table4_latency_by_precision.md)
  is the reader-facing source of truth; underlying data is
  `derived/event_metrics.csv :: time_to_first_change_hours` filtered
  by `_trigger_precision()` in
  [`scripts/build_paper_tables.py`](../scripts/build_paper_tables.py)
  (reads the canonical schema field `trigger.timestamp_precision`).
- **n**: Panel A n is delegated to Table 4. The claim explicitly
  presents the rows as named exemplars, not a band distribution, so
  the paper is defensible even when Panel A is very small.
- **Case role**: events with at least one timed `observed_change`
  AND hour-or-better trigger precision contribute to Panel A and may
  be cited by name; Panel B contributes only to the coarse
  ≤1d / (1d, 30d] / >30d claim.
- **Phrasing lock**:
  - PREFER "named exemplars", "individual events", "Panel A row",
    "conditional on hour-or-better trigger precision".
  - FORBID **"distribution"**, **"bands"**, **"histogram"**, or any
    aggregate-statistical vocabulary applied to Panel A — the
    claim is explicitly exemplar-level. Also FORBID any latency
    number expressed in hours that includes a day-precision trigger;
    "reaction time" as a scalar summary across the admitted corpus
    (precision-mixed); hardcoded hour/day subset counts in the prose
    (delegate to Table 4).
- **Not said**: this is NOT a decomposition by layer speed — that is
  C4 below if promoted. This is NOT a distributional latency claim:
  at the current corpus size, Panel A has too few rows to support
  band-conditional frequencies. The purpose is to **establish that
  minute-precise reaction evidence exists** (the Flashbots PR #90
  row is the sharpest case), not to argue about its prevalence.
- **Status**: Table 4 is live. A proper distributional latency claim
  is **parked for v0.2** pending more hour-precision triggers; see
  §2 below.

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

**Status**: descriptive until the independent-human `observation_kind`
IRR gate clears, because the archetype assignment is a deterministic
function of `observed_change` rows. It can guide tables and discussion
but should not be written as an inferential central result in v0.1.

**Claim**:

> "The dominant single-layer archetypes (asset_only, frontend_only,
> cex_only) appear across multiple research strata: asset_only is
> present in S1 (10) and S5 (3); cex_only in S1 (1), S3 (4), S4 (6),
> S5 (2), S6 (2); frontend_only in S1 (2), S3 (5), S5 (1). The
> upper-layer reach is not a single-stratum artifact."

- **Evidence**: `derived/event_archetypes.json` cross-tabulated with
  `research_stratum`.
- **n**: 53 admitted events.
- **Case role**: empirical + anchor + null jointly contribute.
- **Phrasing lock**:
  - PREFER "present across multiple strata",
    "not a single-stratum artifact".
  - FORBID "occurs uniformly across jurisdictions"
    (stratum ≠ jurisdiction), "consistent pattern"
    (correlational, not causal).

### C6 · [DEMOTED TO FUTURE WORK — do not cite in v0.1 paper]

**Status (2026-04-24)**: this claim is demoted from the v0.1
candidate list to the future-work list. Reviewers across the
2026-04-24 four-agent review converged on "n=1 recovery won't
survive a peer-review objection even with careful phrasing". The
paper's v0.1 submission should present the
`tornado-cash-ofac-delisting-2025` reversal as **a worked exemplar
inside the primary mechanism finding** (the Flashbots
`rpc-endpoint` deletion commit `1e9c29c` is the same substrate as
the PR #90 addition commit), not as a standalone claim about
recovery dynamics.

Retained text below for historical record; **do not extract into
the paper body**:

> "The admitted corpus carries one reversal event
> (`tornado-cash-ofac-delisting-2025`). Per-layer recovery counts are
> therefore reported only as n=1 descriptive observations, not as a
> rate. v0.1 does not support a recovery-rate claim; any such claim
> is deferred to a later release."

- **Evidence (retained for the exemplar-inside-C1 role)**:
  `derived/event_metrics.json :: is_reversal_event`;
  `derived/archetype_distribution.md §4` reversal note.
- **Reframing**: the reversal appears *only* in the primary
  mechanism narrative (Flashbots bidirectional exemplar in
  [README §1 point 2](../README.md) and
  [`analysis/evidence-chains/tornado-cash-ofac-delisting-2025.md`](../analysis/evidence-chains/tornado-cash-ofac-delisting-2025.md)),
  never as a standalone numbered claim.
- **v0.2 gate**: C6 may be reinstated only when the corpus admits
  ≥ 3 independent reversal events (OFAC delistings, court
  overturnings, corporate policy reversals). Until then the
  phrasing lock forbids any recovery-rate language in the paper.

## 2. Claims explicitly NOT in v0.1

Each item below is a claim we could imagine making and have ruled out.

- **Hour-precision latency distribution.** Panel A of Table 4 is too
  thin (small row count at v0.1.0) to support any band / histogram /
  frequency claim. C3 admits only named-exemplar statements. A proper
  distributional latency claim is parked for v0.2 until the
  hour-precision subset passes n≥10. Until then the paper can cite
  Panel A rows individually (e.g. the Flashbots PR #90 2h 50m row)
  but MUST NOT report "the median latency was X" or "K% of events
  reacted within Yh."
- **"Cascade timing is a function of trigger type"** — the
  trigger-type × latency cross-tab is under-powered: see Table 1
  trigger-precision split + Table 4 Panel A row count. Parked for
  v0.2 after more hour-precision events accumulate.
- **"Private-order (CEX) responses are faster than on-chain (asset)
  responses"** — day-precision triggers and asymmetric coverage
  denominators (asset is 17 measured, cex is 23 measured) prevent a
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

The 53 admitted events are a selection-transparent evidence corpus under
the v0.1 admission protocol, with candidate/screened triggers retained in
the trigger registry. They are not stratum-complete; the registry explicitly
tracks remaining expansion gaps. A reader should not read row counts as
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

The paper-table surface under `analysis/paper_tables/` is rebuilt by
`make paper-tables` after any change to `events/*.yaml` or
`derived/*`. `scripts/build_paper_tables.py` emits Tables 1-6;
`scripts/build_jurisdiction_distribution.py` emits Table 7 as the
`jurisdiction` prerequisite. Each claim is frozen to its exact number
by the relevant table at a given `source_commit`. Numbers not
produced by this reproducible surface do not enter the paper.

| # | table | file | supports |
| --- | --- | --- | --- |
| 1 | Case roles | [`table1_case_roles.md`](../analysis/paper_tables/table1_case_roles.md) | §0 case-role convention |
| 2 | Layer observability | [`table2_layer_observability.md`](../analysis/paper_tables/table2_layer_observability.md) | C1 |
| 3 | Archetype × stratum | [`table3_archetype_stratum.md`](../analysis/paper_tables/table3_archetype_stratum.md) | parked C2 / descriptive C5 pending `observation_kind` κ |
| 4 | Latency (precision-filtered) | [`table4_latency_by_precision.md`](../analysis/paper_tables/table4_latency_by_precision.md) | C3, C4 |
| 5 | Target enumeration | [`table5_target_enumeration.md`](../analysis/paper_tables/table5_target_enumeration.md) | §4 complete-vs-subset |
| 6 | Null denominator | [`table6_null_denominator.md`](../analysis/paper_tables/table6_null_denominator.md) | null-event interpretation (C6 demoted 2026-04-24, see §C6 below) |
| 7 | Jurisdictional composition | [`table7_jurisdiction_distribution.md`](../analysis/paper_tables/table7_jurisdiction_distribution.md) | §0 sampling frame |

Companion artifacts outside Tables 1-7:

- [`analysis/trigger_registry/trigger_registry.md`](../analysis/trigger_registry/trigger_registry.md) records selection transparency and v0.2 expansion gaps.
- [`derived/coverage_matrix.md`](../derived/coverage_matrix.md) records event-by-layer denominator eligibility; it is the denominator audit surface behind Table 2.

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
