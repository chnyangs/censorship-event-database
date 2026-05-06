# Datasheet: Cross-Layer Censorship Event Database

Follows the template of Gebru et al., "Datasheets for Datasets" (CACM 2021).
Intended to be read alongside [../README.md](../README.md) and
[methodology.md](methodology.md). Length is deliberately short; each section
points at the authoritative source of truth in the repo rather than restating it.

## 1. Motivation

- **Purpose**: a curated catalog of crypto censorship events with cross-layer,
  precision-aware, multi-source-verified observations of how each event
  propagated through network (L0), consensus (L1), RPC (L3), frontend (L4),
  asset on-chain, and CEX off-ramp layers.
- **Intended tasks**: event-study analysis of regulatory cascades; empirical
  baseline for censorship-resistance claims; reference for journalism, policy,
  and systems research. Not for compliance, legal determination, or predictive
  sanction-screening (see [limitations-and-use.md](limitations-and-use.md)).
- **Funder / creator**: human-maintained by Xiangwen Yang; agent-assisted
  ingestion allowed at `origin=agent_draft` stage, admission is human-only.

## 2. Composition

- **Instances**: each row is a single censorship event defined by a trigger
  action (OFAC SDN, DOJ indictment, corporate policy, nation-state block, etc.)
  and one or more layer-level observations.
- **Count at release time**: see `dataset.csv` header count + `analysis/pilot-status.json`.
- **Sampling frame**: publicly documented crypto censorship events with an
  identifiable legal, regulatory, state, or corporate trigger and at least one
  independently archivable evidence surface. This is not a population sample of
  all censorship events; it is an evidence-bearing frame for reproducible
  measurement. See [limitations-and-use.md §1.1](limitations-and-use.md#11-sampling-frame).
- **Per-instance fields**: governed by [../schema/event.schema.json](../schema/event.schema.json).
- **Labels**: `research_stratum` (S1–S6 trigger family), `empirical_shape`
  (cascade / comparison / null_event), `admission_tier` (anchor / empirical /
  null). Rules for each are in `validate.py::_check_field_consistency`.
- **Null cases**: `null_event` rows with `observed_no_change` observations are
  deliberately included to avoid survivorship bias.
- **Missingness**: every layer is explicitly accounted for — `measured` /
  `partially_measured` / `not_measured` / `not_applicable`. Missing fields are
  a validation error, not a silent gap (README §10.5).

## 3. Collection process

- **Acquisition**: primary sources pulled from OFAC Sanctions List Service,
  court PACER filings, exchange press releases, and on-chain receipts; semi-
  primary from published measurement datasets (Wahrstätter / relayscan CSVs,
  OONI Explorer, Censored Planet) and Wayback snapshots.
- **Admission protocol**: one `primary_*` source OR two independent
  `semi_primary_*` sources per layer-level observation. `supporting_*` never
  satisfies admission alone. `asset_onchain` accepts one `primary_onchain`.
  Rule enforced in `validate.py::_validate_sources`.
- **Attribution gates**: `attribution=direct` requires a primary source
  (enforced 2026-04-22). Two semi-primary measurements downgrade to
  `attribution=plausible`.
- **Archival**: every web source is required to have either a Wayback URL or a
  local `body_hash` + `body_path` pair (plus `query_hash` for measurement API
  pulls). The weekly `freshness.yml` workflow rechecks reachability.
- **Instrumentation**: ingestion scripts live under `scripts/`; the `Makefile`
  wires them into a single `make all` / `make validate` surface.

## 4. Preprocessing / Cleaning / Labeling

- YAML files are the ground truth. `build_dataset.py` emits the JSON and CSV
  release artifacts deterministically from those YAMLs.
- Timestamps stored in UTC ISO-8601; `precision` enum documents the claimed
  granularity (`second`–`week`); the validator ensures `delta_hours` matches
  the trigger-to-observation gap within the stated tolerance.
- No model-derived labels. Stratum / shape / tier are derived from explicit
  admissions-rule counts in validator, not inferred statistically.

## 5. Uses

- **Appropriate**: empirical measurement research on censorship cascades,
  event-study papers, pedagogical examples of cross-layer failure modes,
  contextual journalism that cites specific timelines with provenance.
- **Inappropriate**: sanctions compliance, covered-party determination, legal
  opinion, predictive sanction screening. See
  [limitations-and-use.md](limitations-and-use.md) for the full disclaimer.
- **Known biases**:
  - US-regulator events are over-represented because their provenance is
    easiest to verify (OFAC SDN XML diff + treasury.gov press releases).
  - L0 network observations are sparse where OONI coverage is thin.
  - Off-ramp CEX observations lean on press releases; private API-level
    evidence is rare.

### 5.1 How to use a specific observation in a paper / brief

The dataset is designed for observation-grade quotation. Every observation
you cite should carry four things:

1. **The event slug + layer + observation index**, e.g.
   `tornado-cash-ofac-2022 / l1_consensus / obs[0]`. Event-level citation
   alone is too coarse — a single event often contains both `observed_change`
   and `observed_no_change` observations on different layers.
2. **The `attribution` grade**. `direct` is reserved for observations
   anchored to a primary source that itself names the trigger; `plausible`
   is temporal-proximity + structurally-consistent measurement; `unknown`
   and `none` are weaker. Cite `direct` observations as evidence of
   cause-effect; cite `plausible` as evidence of coincident timing, not
   causation.
3. **The source `body_hash` you depended on**. Footnote it. A reader who
   wants to verify your quote should be able to `sha256` the archived
   body at the recorded `body_path` / Wayback URL and match your hash.
4. **The dataset snapshot pin** — the version + cutoff pair, or the Zenodo
   DOI once one is minted. Without this your citation drifts as the
   catalog grows.

Example citation form (footnote-safe):

> …the Tornado Cash designation produced a 5.9-hour asset-layer reaction
> (`circle_usdc address_blacklisted`, `attribution: direct`, source
> `primary_onchain` tx `0xa613…dd9`, `body_hash sha256:3696…65` [^1]).
>
> [^1]: Cross-Layer Censorship Event Database v0.1.0, cutoff 2026-04-22,
>       event `tornado-cash-ofac-2022`, observation
>       `asset_onchain/circle_usdc/address_blacklisted`. See
>       [CITATION.cff](../CITATION.cff) for the canonical citation record.

### 5.2 Granularity of claim the data supports

Prefer claims of the shape the `scoped_claim` field already asserts —
they've been through admission review. Examples that stay within scope:

- **Timeline claim** — "the OFAC designation of Tornado Cash preceded an
  asset-layer blacklist within 6 hours." Backed by a single primary_onchain
  source + trigger timestamp. Safe.
- **Cascade-shape claim** — "cross-layer reactions were observed on at
  least three layers within 72 hours." Backed by the per-layer observation
  tallies. Safe when restated in layer-count terms.
- **Distribution claim** — "among 51 admitted events, 36 satisfy the
  `comparison` shape (1–2 observed-change layers) and only 2 satisfy the
  `cascade` shape (≥3)." Safe *if* you carry the dataset version + cutoff
  so readers understand which admitted release slice you counted.

What the data does **not** support:

- **Probabilistic forecasts** about future events of the same trigger type.
  With 51 admitted events across 6 strata, the per-cell sample is too small.
- **Individualised covered-party determinations.** The dataset records
  what happened to listed targets; it does not opine on whether a
  particular future action falls under a regulator's authority.
- **Mechanistic causation beyond attribution grade.** A `plausible`
  attribution is not evidence of intent; it is evidence of correlated
  timing under the admission rule.

### 5.3 Audience-specific guidance

- **Paper authors.** Use `scripts/render_evidence_chain.py <slug>` to
  produce a Markdown snapshot of the exact observation / source chain
  behind a claim; include it (or a link to it) as supplementary material.
  The first line of the rendered chain pins the dataset version + cutoff
  so reviewers can verify replayability. See
  [docs/citing.md](citing.md) for BibTeX.
- **Policy / legal analysts.** Use `scripts/find_comparable_cases.py
  --like <slug> --top 5` to surface structurally similar precedents
  with transparent similarity weights. The output is retrieval, not
  prediction; it supports a "prior art" framing in briefs but cannot
  substitute for expert legal judgment.
- **Journalists.** Quote individual observations with the
  event-slug/layer/source chain above. Link to the specific event page
  on the published site (`events/<slug>.html`) so readers can audit
  the archival body_hash themselves.

## 6. Distribution

- Repository: <https://github.com/chnyangs/censorship-event-database>
- Published site: <https://chnyangs.github.io/censorship-event-database/>
- License: CC-BY-4.0 (see [`LICENSE`](../LICENSE) at the repo root).
- Citation: see [citing.md](citing.md) for BibTeX / APA / Chicago templates
  and DOI handling. The canonical record is [`CITATION.cff`](../CITATION.cff);
  tagged releases mint a Zenodo DOI via the GitHub integration (one-time
  setup documented in [releasing.md](releasing.md)).

## 7. Maintenance

- **Editor-in-chief**: Xiangwen Yang (<xwy411@gmail.com>).
- **Cadence**: 5–10 h/month for the first 12 months post-release (see README §10.5).
- **Update protocol**: schema changes bump `schema_version`; breaking changes
  bump the major version and are announced in `CHANGELOG.md`. The `staleness_report.py`
  flags events whose `last_human_audit` date has aged past the audit window
  (see [audit-protocol.md](audit-protocol.md)).
- **Contribution**: external PRs go through two-reviewer approval
  ([contributor-guide.md](contributor-guide.md)). Agent-drafted events are
  admitted only after `origin: human_reviewed`.
