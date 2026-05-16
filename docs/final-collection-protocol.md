# Final Collection Protocol for 2008+ Tiered Discovery

This protocol governs open-ended source-frame discovery before real human
audit, independent-human IRR, and release sign-off. It does not relax the
event admission rules in [`methodology.md`](methodology.md).

## Objective

The collection frame starts at 2008-01-01 and is tiered:

- `discovery_only_2008_2012`: monthly discovery ledger first; rows normally do
  not enter event-rate claims.
- `historical_baseline_2013_2016`: early enforcement, seizure, exchange, and
  darknet-market cases; full event YAMLs are allowed, but they are historical
  baseline unless a claim explicitly separates them.
- `comparable_main_2017_present`: main corpus for comparable cross-layer
  observability claims.

The 150-250 distinct trigger count and 120 admitted-quality event count are
progress milestones, not stop rules or caps.

## Exhaustion Rule

Continue discovery until every declared source frame in
[`sampling/frame.yaml`](../sampling/frame.yaml) has a completed triage manifest
through `snapshot_scope.final_collection_cutoff`, and no remaining candidate
can be admitted without violating the source, coverage, or denominator rules.

Monthly search status is recorded by `make temporal-ledger` in
`analysis/temporal_ledger/`. A missing candidate is not the same thing as an
unsearched month: empty months must be marked as `searched_no_candidate`,
`not_applicable_pre_market`, `source_unavailable`, or `pending`.

## Priority Order

Prioritize gap repair before volume:

| priority | stratum | admitted-quality milestone | reason |
| --- | ---: | ---: | --- |
| P0 | S2 OFAC removals / reversals | 10 | Recovery and bidirectional-mechanism evidence is underpowered. |
| P0 | S4 non-US state actions | 20 | Reduces US-trigger dominance and improves external validity. |
| P1 | S3 federal enforcement | 30 | Large source frame, but promotion needs platform, rail, on-chain, or anchored no-change evidence. |
| P1 | S6 supranational actions | 10 | Tests whether EU/UN-style triggers behave differently from national actions. |
| P2 | S5 corporate policy actions | 15 | Strengthens trigger-is-action and private compliance mechanisms when source chains are explicit. |
| P2 | S1 OFAC SDN designations | 35 | Fill only targeted gaps; avoid simply adding more homogeneous OFAC rows. |

These stratum values are milestones for backlog management. They do not sum to
a freeze target and must not be cited as a population denominator.

## Candidate Path

Every candidate enters the pre-admission registry before promotion:

1. Create or update a `candidate_triggers/*.yaml` stub with `source_frame_id`,
   `research_stratum`, concrete target, trigger citation, and triage notes.
2. Preserve rejected, screened, deferred, and not-measurable candidates with an
   explicit reason under `candidate_triggers/rejected/` or the equivalent
   registry status.
3. Promote only after the event has admission-grade trigger evidence,
   per-layer coverage rows, replayable observation anchors, and valid
   denominator artifacts where required.
4. Run `make trigger-registry temporal-ledger` after each batch so the registry
   and monthly source-frame ledger remain current.

## No-Claim-Expansion Rule

New admitted cases do not automatically create new rate claims. Corpus-level
claims are allowed only when the relevant denominator artifact, coverage row,
paper table, and claim lock all support the same unit of analysis.
