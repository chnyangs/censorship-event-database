# Cross-Layer Censorship Events Need Denominators, Not Implicit Zeros

> Draft manuscript wrapper for the v0.1 paper surface. This file is derived
> from [`paper_claims.md`](paper_claims.md) and the generated tables under
> [`analysis/paper_tables/`](../analysis/paper_tables/). If this draft and
> `paper_claims.md` disagree, `paper_claims.md` wins.

> **Status as of 2026-05-14**: working snapshot, not strict release/submission artifact. The draft may describe the current corpus and working gates, but independent-human IRR, H2 null-case audit, and H3 release sign-off remain blockers for strict submission claims.

## Abstract

Legal, regulatory, state, and corporate actions against crypto targets can
produce reactions across several layers of the stack: public network
reachability, consensus-layer filtering, RPC access, frontends, on-chain asset
controls, and exchange off-ramps. Existing work measures important slices of
this problem, including Internet censorship, Ethereum relay censorship,
Tornado Cash event-study effects, and sanctions-compliance intelligence, but
there is no open event corpus that links the trigger to cross-layer reactions
while preserving which layers were actually measurable. We present a
denominator-aware measurement protocol and a 53-event admitted corpus
(`v0.1.0`, cutoff 2026-05-06) that records legal/policy triggers, coverage
status, observations, evidence chains, and paper-facing tables. The main
finding is methodological: absent measurement is not encoded as a zero. In the
current corpus, L0 network has zero measured denominators, L3 RPC has named
partial Flashbots observations but no emitted conditional rate, and
asset-onchain rates are retracted because the admission rule is structurally
circular for that layer. The strongest empirical surface is upper-stack
public evidence: L4 frontend and off-ramp CEX rows have reportable
coverage-matched rates, while layer gaps are surfaced as observability gaps.
The paper also reports a public source-control mechanism case: a Flashbots
RPC filter-list update added Tornado Cash addresses 2h 50m after the 2022
OFAC designation, and a later deletion followed the 2025 OFAC delisting. The
contribution is a forkable measurement protocol, corpus, and reproducible
artifact package, not a prevalence estimate over all crypto censorship.

## 1. Introduction

Crypto censorship is often discussed as if a legal action causes a direct and
fully observable cascade through the stack. That framing is too coarse for
measurement. A sanctions designation, court order, or corporate policy change
may be visible on-chain, in exchange announcements, in frontend snapshots, in
RPC behavior, in relay policy, or in country-level network reachability. It
may also leave no public measurement substrate at several of those layers.
Treating an unmeasured layer as "no reaction" creates a false denominator and
turns an observability problem into a behavioral claim.

This project asks a narrower and more reproducible question:

> Among publicly observable stack layers and under an admission-grade evidence
> substrate, which layers carry detectable reactions to an identified legal or
> policy trigger, and which layers' conditional rates are undefined because
> the public evidentiary denominator does not exist?

The answer is implemented as a six-artifact measurement protocol and a
52-admitted-event paper corpus over a 53-record YAML surface. Each event is a YAML record with a trigger,
target, layer coverage rows, layer observations, and source anchors. The
derived artifacts then compute the coverage matrix, evidence chains, and
paper tables from the same source records. A rate is emitted only when the
numerator is coverage-matched to the same measured or partially measured
denominator. When the denominator is absent, the table reports `—`, not `0`.

The resulting v0.1 corpus is not a population sample. It is a
selection-transparent, US-trigger-dominant, English-indexable public-evidence
corpus. It currently contains 52 admitted events: 2 anchor cases, 38
empirical cases, and 12 null cases. One rejected YAML row is retained in
the registry surface for selection transparency. The corpus is useful because it makes
the evidentiary substrate explicit. It shows where public measurement can
support layer-level claims, where named partial observations exist, and where
the only honest conclusion is an observability gap.

The paper makes four contributions:

1. **A denominator-aware event measurement protocol.** The protocol separates
   `measured`, `partially_measured`, `not_measured`, and `not_applicable`
   coverage and forbids interpreting missing measurement as no reaction.
2. **A reproducible 53-event corpus.** Every admitted event has replayable
   source anchors, evidence chains, and generated paper tables.
3. **A cross-layer observability result.** Upper-stack layers have the
   strongest public evidence surface; L0 and L3 denominator gaps remain
   explicit rather than silently converted into zeros.
4. **A public operator-source-control mechanism case.** An 8-repo v0.1 public-source-control scan
   shows that git-history compliance substrates are real but structurally
   narrow in the v0.1 public-repo frame.

## 2. Related Work

Internet censorship measurement systems such as OONI and Censored Planet
establish the model for public, auditable network measurement. This project
borrows their denominator discipline for L0: a query with no measurements is
an observability gap, not evidence of reachability. The project does not
extend OONI or Censored Planet probe infrastructure; it consumes them as
external measurement substrates and records when they fail to provide a
denominator.

The closest blockchain-censorship work is Wahrstätter et al.,
"Blockchain Censorship" (ACM WebConf 2024), which measures L1 relay and
builder filtering on Ethereum. That work is a block- and transaction-level
L1 census. This paper is an event-level cross-layer corpus. L1 inputs in
this corpus are treated as semi-primary evidence derived from that
measurement lineage; the paper does not compete on L1 prevalence.

Tornado Cash event-study work analyzes economic, flow-level, and
settlement-layer effects after the OFAC designation. Those studies provide
important sanity checks on event windows and persistence, but their unit of
analysis is not the same as this paper's stack-layer event record. We keep
transaction-flow effects separate from stack-reaction coding.

MEV Watch, relayscan-style dashboards, and censorship.pics provide live or
historical relay-policy surfaces. They are useful for sanity-checking L1
relay exposure, especially around Tornado-family events, but relay share is
not equivalent to event-specific transaction censorship and does not validate
RPC, frontend, asset, or CEX observations.

Compliance-intelligence sources such as Chainalysis, Elliptic, and TRM, and
transparency systems such as Lumen, inform entity normalization and
source-limit language. They do not substitute for replayable public
evidence. Proprietary labels, redacted records, and private compliance feeds
are supporting context only unless the specific event claim is public and
replayable.

The external benchmark crosswalk is recorded in
[`analysis/external_crosschecks/`](../analysis/external_crosschecks/). It is
an external-validity layer, not a seventh admission artifact.

## 3. Measurement Protocol

The measurement protocol has six artifacts:

| Artifact | Role |
| --- | --- |
| Trigger registry | Selection surface for admitted, candidate, promoted, and screened triggers. |
| Event corpus | Source-of-truth YAML records for trigger, target, coverage, observations, and sources. |
| Coverage matrix | Event-by-layer denominator eligibility and L0 query-denominator summary. |
| Evidence chains | Per-event rendering from claim to observation to source to archive/hash to limitation. |
| Paper-table generator | Admitted-only fail-closed numerical surface. |
| Audit/sensitivity package | Human audit queue, admission-sensitivity ablation, IRR/self-consistency, and staleness checks. |

Each event has one or more layer coverage rows. A layer can be `measured`,
`partially_measured`, `not_measured`, or `not_applicable`. Observations are
separate from coverage: a measured layer can have `observed_change`, a
scoped `observed_no_change`, or a `coverage_gap`. A null observation requires
an evidence anchor such as `body_hash` plus `body_path`, `query_hash`, or
`measurement_ids`; a prose scope descriptor is not sufficient.

The paper-table generator is fail-closed. It aborts on anchorless null cases,
precision ambiguity, or denominator mismatch. For layer rates, the numerator
is filtered to the same coverage subset as the denominator. This avoids the
common error of reporting "changed / all events" when most events lack a
measurement substrate for the layer.

The v0.1 sampling frame is public, English-indexable crypto censorship
events with an identifiable legal, regulatory, state, or corporate trigger
and at least one independently archivable evidence surface. This frame is
US-trigger-dominant by construction and should not be read as a global
prevalence sample.

## 4. Corpus

The current snapshot contains 52 admitted events. Table 1 reports three
paper roles: 2 anchor cases, 38 empirical cases, and 12 null cases. The case
role controls how an event may be cited. Anchor cases can appear in narrative
spotlights and figures. Empirical cases contribute to aggregate tables. Null
cases support denominator and observed-no-change interpretation only.

Trigger precision is also uneven. Only 5 of the 52 admitted events have hour-level
trigger precision, while 48 have day-level precision. Hour-granularity
latency claims are therefore restricted to the hour-precision subset, and
day-precision events are reported in interval buckets.

The corpus is stratified by research frame rather than population weight.
Table 7 shows that 40 of 53 events include `US` in their jurisdiction list
(75.5%). Region counts are inclusive rather than partitioned; a
multi-jurisdiction event may count in both the US and Europe rows. This is a
property of the public-English-language evidence frame and the high volume of
OFAC, DOJ, and SEC activity in 2022-2025. The paper therefore describes the
corpus as US-trigger-dominant, not as evidence that censorship is globally
concentrated in the United States.

Target enumeration is mixed. Table 5 reports 31 complete target
enumerations and 22 subset enumerations. Subset rows must be phrased as
claims about the named subset, not the entire protocol or ecosystem.

## 5. Results

### 5.1 Layer Observability

Table 2 is the central result. It reports layer-level coverage and
coverage-matched rates:

| Layer | Measured | Partial | Not measured | Strict | Current | Permissive | Reported interpretation |
| --- | ---: | ---: | ---: | --- | --- | --- | --- |
| L0 network | 0 | 0 | 22 | — / 0 = — | — / 0 = — | — / 0 = — | No conditional rate; public measurements are absent in the queried cells. |
| L1 consensus | 6 | 1 | 1 | 0/6 = 0.000 | 1/6 = 0.167 | 2/7 = 0.286 | Sensitive; cite all three rubrics or name the exact one. |
| L3 RPC | 0 | 2 | 7 | — / 0 = — | — / 0 = — | 2 named observations, no rate | Named Flashbots partial observations only; no conditional rate. |
| L4 frontend | 13 | 3 | 10 | 8/13 = 0.615 | 10/13 = 0.769 | 12/16 = 0.750 | Sensitive; cite all three rubrics or name the exact one. |
| Asset on-chain | 17 | 0 | 6 | retracted | retracted | retracted | Rate retracted because the admission rule is structurally circular. |
| Off-ramp CEX | 25 | 1 | 21 | 13/25 = 0.520 | 15/25 = 0.600 | 16/26 = 0.615 | Moderate sensitivity; quote with denominator and rubric context. |

The most important result is not that every upper layer "reacts more". The
defensible result is that public evidence is concentrated in upper-stack
surfaces, while lower-stack or private surfaces often lack a denominator.
L0 has zero measured denominators in v0.1; L3 has two named partial rows but
no measured denominator; asset-onchain rows are visible but cannot support a
rate because the admission anchor often is the asset action itself. The paper
therefore reports frontend and CEX rates with denominator qualifiers, retains
L3 only as named partial evidence, and treats L0 as an observability gap.

Admission-sensitivity checks matter. L1 and L4 are sensitive to strict,
current, and permissive admission rubrics, and the paper must carry that
sensitivity when citing those rates. Off-ramp CEX is moderately sensitive.
No rate should be quoted without its denominator and admission context.

### 5.2 Archetypes and Strata

Table 3 reports deterministic archetypes: 13 asset-only events, 8
frontend-only events, 15 CEX-only events, 4 multi-layer events, and 13 null
events. These counts describe the admitted corpus only. They are not
population prevalence estimates, and the single-layer dominance claim remains
descriptive until independent-human reliability clears the audit gate.

The multi-layer count is especially easy to over-read. Two of the four
multi-layer events are Tornado forward/reverse events on the same target
family. The corpus therefore supports a methodological claim about
cross-layer reconstruction, not a prevalence claim about cascade frequency.

### 5.3 Latency and Trigger Precision

Table 4 separates hour-precision triggers, day-precision triggers, and
`trigger_is_action` rows. Panel A contains only two non-action events with
hour-level precision: `tornado-cash-ofac-2022` in the (1, 6] hour band and
`china-pboc-crypto-ban-2021` in the (6, 24] hour band. Panel B reports 33
day-precision events in interval buckets. Panel C excludes five
`corporate_policy_change` rows where the trigger itself is an action.

The paper can use named latency examples, but it cannot report an
hour-granularity latency distribution for the whole corpus. Most legal and
regulatory triggers publish only dates, not times. Precision is therefore a
data property, not a formatting detail.

### 5.4 Null Cases

The 13 null cases are not evidence of no private reaction. They are scoped
public-evidence nulls. Table 6 lists the null-case event IDs, layers, and
evidence-anchor types. Each row has a replayable `body_hash+body_path`
anchor, and the generator aborts if a null case is anchorless.

Before these cases are used as named narrative examples or stronger
denominator evidence, the human audit queue requires a human review and a
truthful `last_human_audit` stamp. The current working snapshot allows them
in aggregate/null tables with warnings; strict submission mode blocks until
the null-case audit is complete.

### 5.5 Operator Source-Control Mechanism

The Flashbots `rpc-endpoint::server/ofacblacklist.go` file is a worked
mechanism case. PR #90 added Tornado Cash pool addresses 2h 50m after the
2022-08-08 OFAC designation. PR #173 deleted the 132-address blacklist 11
days after the 2025-03-21 OFAC delisting. This bidirectional bookend shows
that public operator source control can sometimes capture compliance
decisions with minute-level precision.

The operator-source-control scan bounds that finding. It scans 8 public
operator repositories and tiers them into confirmed filter files, glob-swept
matches, schema/index-only repos, and glob-zero repos. Only one known-channel
substrate carries the canonical OFAC filter-list edits. The correct claim is
therefore structural narrowness: public git history is a real measurement
channel in one confirmed substrate, but most operator compliance behavior is
likely server-side or absent from public source control.

## 6. Validity and Limitations

### Sampling and Source Bias

The corpus is not a population sample. It is a public-evidence corpus. Events
outside English-indexable sources, public archives, and replayable artifacts
are underrepresented. The US-trigger share reflects that evidence frame and
the high availability of OFAC/DOJ/SEC records, not global prevalence.

Upper-stack evidence is easier to observe than base-layer evidence. Frontend
captures, on-chain events, and exchange announcements are often public. L0,
L1, and L3 require external measurement infrastructure, private operational
data, or continuous telemetry. Table 2's upper-layer concentration must be
read partly as a survivorship effect of the evidence substrate.

### Attribution

The dataset separates `direct`, `plausible`, and `none` attribution. Direct
observations may support causal language. Plausible observations may support
co-occurrence or consistency language only. Null observations do not support
causal statements.

### External Benchmarks

External benchmarks are validity checks, not denominators. OONI and Censored
Planet can support L0 query-denominator language only for the specific
domain, vantage, and window. Tornado Cash event-study work sanity-checks
anchor-case windows but cannot generalize the corpus. MEV Watch can
sanity-check L1 relay exposure but cannot validate RPC, frontend, asset, or
CEX rows. Compliance reports and transparency databases help with entity
normalization and source caveats, but proprietary or redacted claims remain
supporting context.

### Reliability and Human Audit

The current IRR report is a self-consistency check under
`llm_assisted_blinded` provenance, not independent-human reliability. The H1
independent-human IRR packet and H2 null-case denominator audit are prepared,
but strict submission mode remains blocked until the human work lands. The
strict gate also requires release sign-off, updated citation metadata, and a
clean intended source tree.

## 7. Artifact and Reproducibility

The repository is the artifact. The main reproduction path is:

```sh
make check
make paper-check
make render-site
python3 scripts/check_paper_readiness.py --strict-audit --strict-null-audit --strict-repro --strict-reliability
```

The first three commands validate the working snapshot and regenerate the
site. The strict command is expected to fail in the current local state until
human IRR, null-case audit, release metadata, and clean-tree requirements are
complete.

The static dashboard exposes the corpus, evidence chains, paper tables,
external benchmark crosswalk, and human-audit workflow. H1 independent-human
IRR is distributed separately through `site/h1_irr_packet/` to preserve
blinding; H2/H3 auditors use `site/audit.html`.

## 8. Conclusion

This paper argues for a denominator-aware way to study crypto censorship
events. Cross-layer reactions are real and sometimes reconstructable, but the
measurement substrate is uneven. A credible corpus must therefore state not
only what changed, but also which layers could be measured and which layers
could not. The v0.1 database provides a reproducible starting point: 53
admitted events, explicit coverage semantics, fail-closed paper tables,
evidence chains, external benchmark crosschecks, and an audit workflow. Its
long-term contribution is the protocol: future work can expand the sampling
frame, add non-English and non-US-triggered events, ingest richer L0/L1/L3
measurement substrates, and rerun the same denominator-aware tables without
changing the core claim discipline.
