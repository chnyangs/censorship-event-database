# L2 Rollup / Sequencer Scope Boundary

This corpus does **not** measure rollup or sequencer-layer censorship.
`l2_rollup` is intentionally absent from the schema, validator, coverage
matrix, paper tables, and admission-sensitivity outputs.

## Why L2 Was Not Added Initially

The corpus measures event-level reactions to a legal, regulatory, state, or
corporate trigger. Its tracked layers share a common event-layer unit:
for a given trigger, can a public, replayable source show that a network,
consensus, RPC, frontend, asset-issuer, or CEX/off-ramp surface changed?

Rollup and sequencer censorship requires a different measurement unit:
transaction inclusion and ordering, sequencer/batcher/proposer behavior,
forced-inclusion windows, bridge/withdrawal paths, and rollup-specific
governance or operator logs. Those units do not reduce cleanly to the
current event-layer denominator without a separate sampling frame.

The public evidence substrate is also different. Many sequencer decisions
do not have stable public logs, public source-control records, or replayable
measurement feeds. Adding `l2_rollup` to this corpus without that substrate
would mostly create `not_measured` rows. Those rows would not show that L2
did not react; they would only show that the current project did not build
the necessary L2 denominator.

## How To Read The Current Tables

L2 is an **out-of-scope exclusion**, not a measured-zero result.

- It is not counted in `derived/coverage_matrix.*`.
- It is not a `not_measured` row in each event.
- It does not contribute to any denominator in
  `analysis/paper_tables/table2_layer_observability.*`.
- Paper prose must not say that the corpus covers the full crypto stack or
  that rollup/sequencer censorship was absent.

Allowed phrasing:

> The current corpus excludes rollup/sequencer-layer censorship; L2 has no
> denominator in the reported layer tables.

Forbidden phrasing:

> No L2 censorship was observed.

> L2 had zero reactions.

> The corpus covers every stack layer.

## What A Separate L2 Tracker Would Need

A release-grade L2 tracker should define, at minimum:

- rollup-specific event units and trigger linkage rules;
- sequencer, batcher, proposer, bridge, and forced-inclusion surfaces;
- replayable evidence types for inclusion delay, dropped transactions,
  forced transactions, bridge withdrawal impairment, and operator policy
  changes;
- denominator construction for each rollup and observation window;
- validator and paper-table logic that distinguishes missing public telemetry
  from observed no-change.

Until those pieces exist, mixing L2 into this corpus would weaken the
coverage-denominator discipline that the paper is trying to make explicit.
