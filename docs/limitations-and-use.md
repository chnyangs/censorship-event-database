# Limitations and Intended Use

This document is read first. The tools built on top of this dataset
(`render_evidence_chain.py`, `find_comparable_cases.py`,
`decision-rubric.md`) inherit every limitation stated here. If you use
any of these outputs in a paper, brief, memo, or risk model, you are
asserting that you have read and agreed to what follows.

## 1. What this dataset is

A stratified-complete catalog of **publicly documented crypto censorship
events** from 2017-07-26 (BTC-e seizure) through 2025-11-19 (Russian
cybercrime infrastructure SDN). Each event YAML captures: a trigger with
primary-source citations (sha256 `body_hash`); a concrete target
(addresses / entity / domain); per-layer coverage status; observations
with admission-grade evidence; and an explicit `scoped_claim` that the
retained observations support.

Currently **53 admitted events**; every event validates under
[`scripts/validate.py`](../scripts/validate.py) at schema version 0.2.0.

## 2. What this dataset is **not**

The tools wrap the dataset and amplify its limits. Read these before
using any output for anything consequential.

### 2.1 Not a predictive model

With 53 events across 5 research strata × 6 cascade layers × multiple
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
  volunteer measurement in the event-bracketing windows. L0 is
  attested-negative across the dataset. Any L0 claim in derived tools
  is based on domain reachability inferences from L4, not probe data.
- **Solana / Polygon / BNB Chain**: no events in the dataset target
  addresses on these chains. This reflects the actual BTC/ETH/TRON
  dominance of OFAC SDN practice, not a sampling omission — but
  downstream claims should not be extrapolated to those chains.
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
policy white papers. The expected usage pattern is: identify
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

The dataset (YAMLs + captured HTML sources) is published under the
license recorded in the repo root. Tools (`scripts/*.py`) are
MIT-licensed unless otherwise stated in the file. Commercial use is not
prohibited but is strongly discouraged from relying on stability — we
do not make uptime guarantees.

When you cite the dataset, cite the git commit hash (not "latest") and
the specific event slugs you use. When you cite a tool output, cite
the tool version + the full output artifact (including its
`dataset_version` stamp). This is the minimum bar for anything
downstream to be independently verifiable.

---

**Summary in one sentence**: this is an open, auditable evidence
catalog — your argument is your responsibility, our contract is
reproducibility.
