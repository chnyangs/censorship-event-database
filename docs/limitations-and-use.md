# Limitations and Intended Use

This document is read first. The tools built on top of this dataset
(`render_evidence_chain.py`, `find_comparable_cases.py`,
`decision-rubric.md`) inherit every limitation stated here. If you use
any of these outputs in a paper, brief, memo, or risk model, you are
asserting that you have read and agreed to what follows.

## 1. What this dataset is

A coverage-denominator-disciplined admitted catalog of **publicly documented crypto censorship
events** from 2017-07-26 (BTC-e seizure) through 2025-11-19 (Russian
cybercrime infrastructure SDN). Each event YAML captures: a trigger with
primary-source citations (sha256 `body_hash`); a concrete target
(addresses / entity / domain); per-layer coverage status; observations
with admission-grade evidence; and an explicit `scoped_claim` that the
retained observations support.

Current working snapshot: **52 admitted events**, 1 rejected registry row, and no working drafts; every event validates
under [`scripts/validate.py`](../scripts/validate.py) at schema version
0.2.0. Paper-facing tables use admitted events only. This is not a strict
release/submission artifact until the full human/release gate passes.

### 1.1 Sampling frame

The v0.1 dataset is not an attempt to enumerate every possible
crypto-censorship event. Its sampling frame is narrower and deliberately
auditable: **publicly documented crypto censorship events with an
identifiable legal, regulatory, state, or corporate trigger and at least
one independently archivable evidence surface**.

"Admitted" is the paper-count boundary: included rows satisfy the schema,
source, and evidence-chain gates for this release. Selection transparency
is handled separately by the trigger registry
([`analysis/trigger_registry/trigger_registry.md`](../analysis/trigger_registry/trigger_registry.md))
under the declared expansion frame
([`sampling/frame.yaml`](../sampling/frame.yaml)). Registry gaps are
backlog, not results.

Included events must have a concrete crypto target and a trigger source
that can be archived or replayed. Layer-level claims enter the paper only
when their source chain can be checked through local hashes, primary
on-chain identifiers, measurement query hashes, or pinned measurement
artifacts. This makes the corpus usable as a reproducible measurement
asset, but row counts must not be read as population prevalence over all
censorship events.

Layer-rate denominators are visible in
[`derived/coverage_matrix.md`](../derived/coverage_matrix.md). Rows marked
as `observability_gap`, `named_partial_only_no_conditional_rate`, or
`descriptive_only_structural_circularity_v0_1` cannot support conditional
rates.

Rollup / sequencer L2 is excluded from the current sampling frame rather
than represented as a measured layer. It has no row in the coverage matrix
and no denominator in the paper tables. See
[`l2-scope-boundary.md`](l2-scope-boundary.md).

Events are excluded or left as future work when the only evidence is
private compliance telemetry, rumor-only social media, inaccessible paid
KYT systems, or a broad policy change without a concrete target.

## 2. What this dataset is **not**

The tools wrap the dataset and amplify its limits. Read these before
using any output for anything consequential.

### 2.1 Not a predictive model

With 52 admitted events across 6 research strata × 6 cascade layers × multiple
time windows, **the statistical power for causal inference is low**. We
publish descriptive patterns ("across N historical OFAC mixer
designations, the canonical frontend was taken down within 48 hours in
K/N cases") — we do not publish probability-of-takedown estimates.

Anything downstream (`find_comparable_cases.py` output, for example)
returns historical precedents for comparison, not forecasts. Treat the
output as a research starting point, not an answer.

### 2.2 Not legal advice

Nothing in this repository is legal advice. The presence of a historical
event that resembles a proposed action does not predict, permit, or
license any specific action by any specific actor. If you are preparing
an amicus brief, an expert report, a compliance decision, or a policy
memo, **you (or your legal counsel) are responsible for judging whether
a given historical precedent is applicable to your situation.**

The dataset's role in *Van Loon v. Treasury* (5th Cir. 2024) was as an
input to expert analysis, not as a directly-cited authority. That is the
appropriate usage pattern.

### 2.3 Not a compliance / risk-scoring service

This dataset is explicitly not a replacement for paid chain-analytics
services (Chainalysis, Elliptic, TRM). We do not publish per-wallet
KYT scores; we do not provide live monitoring; we do not maintain an
operational feed. If you need those, buy them.

### 2.4 Coverage gaps we know about

Documented in [`docs/chain-coverage-note.md`](chain-coverage-note.md)
and in each event's `coverage[].note` fields. Key structural gaps:

- **L0 network layer**: 0 / 23 queried crypto domains had any OONI
  volunteer measurement in the event-bracketing windows. In the current
  corpus, `l0_network` is therefore an **observability gap**, not an
  attested-negative layer: `derived/layer_observability.*` currently
  shows no measured denominator and no admitted `observed_change` or
  `observed_no_change` rows at L0, while
  [`derived/l0_coverage_summary.md`](../derived/l0_coverage_summary.md)
  records all 23 query windows as `no_ooni_measurements`. Any L0
  discussion in downstream tools must be framed as "not measured here",
  not as evidence that network-layer reactions did not occur.
- **Solana / Polygon / BNB Chain**: no events in the dataset target
  addresses on these chains. This is an observed feature of the current
  admitted corpus and source frame, not proof of complete chain-level
  absence; downstream claims should not be extrapolated to those chains.
- **Private compliance signals**: issuer internal intelligence, CEX
  KYT flags, and law-enforcement private channels are outside scope.
  Events coded `observed_no_change` at `offramp_cex` record the
  absence of *publicly-disclosed* cascade, not the absence of private
  action.

### 2.5 Snapshot decay

Every event carries `last_verified: YYYY-MM-DD`. Primary-source URLs rot;
Wayback snapshots can be rate-limited; OFAC SDN list changes. We have
applied 2026-Q2 adversarial audit discipline, but **derived tools must
display the dataset `cutoff_date` prominently**. Do not use a
>6-month-stale comparable-case output without re-checking the dataset.

**Canonical definition (single source of truth):**
`dataset.meta.json :: cutoff_date` = **max** of (`last_verified`,
`last_human_audit`) across all events. This is the **upper bound** of
verification activity in the snapshot — i.e., "the dataset includes
events verified up through this date." It is **not** a uniform freshness
guarantee across events; individual events may carry older
`last_verified` values. Per-event freshness is surfaced in
`analysis/staleness.md`, which flags any event whose verification anchor
is older than the configured red threshold (90 days by default).

Four consumers of this field (`scripts/build_dataset.py`,
`scripts/_dataset_meta.py`, `docs/citing.md`, this document) must stay in
sync; if you change the semantic in one, change it in all.

## 3. Intended use (who this is for)

### 3.1 Primary: Academic research

Event-study methodology, cross-layer censorship measurement papers,
replication packages. Cite the dataset version (git commit hash) and
the specific event slugs you use. Corrections welcome via PR.

### 3.2 Primary: Schema as reusable infrastructure

The six-layer cascade model + admission protocol + field schema are
designed to be forkable by other research groups. If you apply the
schema to events we did not cover (non-US jurisdictions,
privacy-coin-specific actions, NFT-collection takedowns, etc.),
**please publish your dataset under a compatible license so the
methodology remains interoperable**.

### 3.3 Secondary: Legal & policy analysis

For amicus briefs, expert reports, regulatory-comment letters, or
policy white papers. The supported workflow is: identify
comparable historical events via `find_comparable_cases.py`; read the
full event YAMLs; independently verify the primary sources via the
published `body_hash`; then *your own expert* assembles the argument.
The tool is a retrieval-and-assembly aid, not the expert.

### 3.4 Explicitly discouraged

- **Automated compliance decisions** — do not connect any tool here to
  a production KYC / AML / transaction-monitoring pipeline.
- **Automated public accusations** — do not build a news-generation
  pipeline that claims "X is similar to Y sanctioned entity, therefore
  X is sanctioned."
- **Black-box downstream products** — if you build a product on top of
  this dataset, the product must either surface the underlying event
  citations + body_hashes to its users, or explicitly state that it
  does not.

## 4. Reproducibility contract

Every tool output under this framework carries:

- `dataset_version` — semver version from `CITATION.cff :: version`
  (e.g. `0.1.0`). `scripts/build_dataset.py` bakes it into every
  `dataset.meta.json` run so all derived outputs agree.
- `source_commit` — short git SHA at generation time (7 chars);
  resolves the snapshot precisely between tagged releases.
- `cutoff_date` — **max** of (`last_verified`, `last_human_audit`)
  across events. See §2.5 for the canonical definition.
- `schema_version` — currently `0.2.0`. The generator hard-fails if
  events disagree.
- `tool_version` — semantic version of the specific script
  (`render_evidence_chain.py`, `find_comparable_cases.py`, etc.).
- `generated_at` — ISO-8601 UTC timestamp.
- For every cited event: `event_id` + `scoped_claim` + the `body_hash`
  of at least one primary source.

A reader can re-check any claim by: `git checkout v{dataset_version}`
(or `git checkout {source_commit}` between releases) → verify
`body_hash` matches the file at `body_path` → read the original primary
source. No step requires any proprietary service.

## 5. Corrections and dispute resolution

If you believe an event is mis-characterized, a primary source is
mis-cited, or a layer observation overclaims attribution:

1. Open a GitHub issue with the `event_id` and the specific claim.
2. Provide the counter-evidence (ideally a primary source with your own
   archival hash).
3. The adversarial-audit protocol in [`docs/audit-protocol.md`](audit-protocol.md)
   applies: corrections that pass that protocol are merged, with the
   change recorded in `CHANGELOG.md` and the affected event's
   `last_verified` updated.

We do not resolve disputes via email, LinkedIn, or any private channel.
If an objection is not defensible as a public issue with an archival
body_hash, it does not meet the correction bar for an evidence-anchored
dataset.

## 6. License and attribution

This repo ships two artifacts under two different licenses. Both are at
the repo root and authoritative; the machine-readable declarations live
in `CITATION.cff` (dataset) and the `SPDX-License-Identifier` header on
each source file (code). See [`NOTICE`](../NOTICE) for the full
file-list split.

- **Dataset & documentation** — Creative Commons Attribution 4.0
  International (**CC-BY-4.0**). Covers `events/`, `schema/`,
  `analysis/`, `dataset.{json,csv,meta.json}`, `docs/`, `site/`,
  `README.md`, `CHANGELOG.md`, `EVENTS-CHECKLIST.md`, `CITATION.cff`,
  `.zenodo.json`, and the archived bodies under `sources/` to the
  extent they are our copyright. Legal text: [`LICENSE`](../LICENSE).
  SPDX: `CC-BY-4.0`.
- **Source code** — MIT License. Covers `scripts/**/*.py`, `Makefile`,
  `.github/workflows/*.yml`. Every Python file carries an
  `SPDX-License-Identifier: MIT` header. Legal text:
  [`LICENSE-CODE`](../LICENSE-CODE). SPDX: `MIT`.

**Why the split**: Creative Commons explicitly recommends against using
CC licenses for software. MIT is permissive enough for academic +
industry tool reuse without friction; CC-BY-4.0 is the standard for
open research data.

**Attribution**: when you cite the dataset, cite the tagged
`dataset_version` (from `CITATION.cff` / `dataset.meta.json`) and the
specific event slugs you use — see [`citing.md`](citing.md) for
templates. When you cite tool output, cite the tool version + the full
output artifact (including its `dataset_version` stamp). When you
redistribute or modify the code, keep the MIT copyright line + the SPDX
header. Commercial use is not prohibited, but we do not make uptime or
API-stability guarantees.

---

**Summary in one sentence**: this is an open, auditable evidence
catalog — your argument is your responsibility, our contract is
reproducibility.
