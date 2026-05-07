# L0 / L3 Denominator Appendix

Dataset snapshot: `v0.1.0` · cutoff `2026-05-06`.

This appendix is the paper-facing interpretation layer for two otherwise
easy-to-misread results: `l0_network` and `l3_rpc` currently have no
measured conditional-rate denominator. That is not a zero result. It is
an audited absence of a measurement substrate under the v0.1 admission
protocol.

## Denominator Semantics

The corpus separates four states that are often conflated in prose:

| state | meaning | rate eligible |
| --- | --- | --- |
| `measured` | the event has a scoped, replayable layer denominator that can count both changes and non-changes | yes |
| `partially_measured` | a named surface is replayable, but the layer universe is incomplete | sensitivity only, if the table allows it |
| `named_partial_only_no_conditional_rate` | a named observation is valid, but there is no measured provider or venue universe | no |
| `observability_gap` / `not_measured` | the public evidence substrate is absent or insufficient | no |

The consequence for the paper is simple: Table 2 emits `—` for a zero
denominator and never converts an observability gap into a negative
observation.

## L0 Network Layer

Current generated artifacts:

| artifact | current result | interpretation |
| --- | --- | --- |
| [`derived/coverage_matrix.md`](../derived/coverage_matrix.md) | 22 applicable L0 event-layer rows, 0 measured denominators, 22 observability gaps | no event can support an L0 conditional rate |
| [`derived/layer_observability.csv`](../derived/layer_observability.csv) | `l0_network`: `measured_count=0`, `not_measured_count=22` | Table 2 must report `—` |
| [`derived/l0_coverage_summary.md`](../derived/l0_coverage_summary.md) | 23 archived OONI query rows across 14 L0-applicable events, all `no_ooni_measurements` | the public OONI API returned no measurements for these queried domain/window cells |

The 23 OONI rows are still useful: each records an explicit query cell
(`event_id`, domain, input URL, probe country, window, query hash, body
path, and body hash). A zero-result OONI query proves that this public
measurement source did not provide a denominator for the query cell. It
does not prove that the domain was reachable, that no ISP blocked it, or
that a different measurement platform would also be empty.

Eight L0-applicable events have no archived OONI query row in v0.1 and
are separately labeled `not_queried_yet`: `bitzlato-doj-2023`,
`grinex-garantex-successor-ofac-2025`, `hydra-ofac-2022`,
`iran-ransomware-ofac-2018`, `semenov-ofac-2023`,
`tornado-cash-ofac-delisting-2025`,
`tornado-cash-ofac-redesignation-2022`, and `zservers-ofac-2025`.
All 22 L0-applicable events also carry `cp_not_ingested_v0_1`; Censored
Planet is specified in the method but not yet committed as a derived
denominator artifact.

An L0 event becomes rate-eligible only if one of the following exists:

| eligible denominator source | minimum replay fields |
| --- | --- |
| OONI `web_connectivity` measurements | measurement IDs, probe countries, input URLs, query window, body hash |
| Censored Planet or comparable raw slice | vantage universe, country/window coverage, query or export hash |
| primary ISP / regulator block notice | named target, jurisdiction, effective time, archived source |

Until then, the paper may say "L0 was not measured under this public
evidence frame." It may not say "no L0 censorship occurred."

## L3 RPC Layer

Current generated artifacts:

| artifact | current result | interpretation |
| --- | --- | --- |
| [`derived/coverage_matrix.md`](../derived/coverage_matrix.md) | 9 applicable L3 event-layer rows, 0 measured denominators, 2 named partial rows, 7 observability gaps | the layer has named observations but no provider-universe denominator |
| [`analysis/paper_tables/table2_layer_observability.md`](../analysis/paper_tables/table2_layer_observability.md) | `l3_rpc`: `changed/measured=—`, `changed/measured+partial=named-only; no rate` | do not cite an L3 conditional rate |
| [`derived/l3_provider_census.md`](../derived/l3_provider_census.md) | provider/event-window cells for Flashbots, MEV Blocker, Infura, Alchemy, QuickNode, and long-tail public RPC providers | no provider-event cell is rate-eligible in v0.1 |
| [`analysis/operator_census/README.md`](../analysis/operator_census/README.md) | 8 public operator repositories surveyed; only `flashbots/rpc-endpoint` has a confirmed OFAC filter-file substrate | public source control is a narrow measurement channel |

The two L3 changed rows are the Flashbots bookends:

| event | observed substrate | denominator class |
| --- | --- | --- |
| `tornado-cash-ofac-2022` | `flashbots/rpc-endpoint::server/ofacblacklist.go` adds Tornado Cash pool addresses | named partial only |
| `tornado-cash-ofac-delisting-2025` | the same filter-list substrate is removed after OFAC delisting | named partial only |

These observations are valid mechanism evidence because the git history
is replayable. They are not a provider-rate denominator because v0.1
does not probe or enumerate a complete public-RPC provider universe for
the same targets, windows, and methods.

## L3 Provider Census Frame

The v0.1 frame distinguishes a provider being listed as measurable from
a provider having an event-specific denominator:

| provider / surface | v0.1 substrate | event-specific denominator | current use |
| --- | --- | --- | --- |
| Flashbots Protect / `flashbots/rpc-endpoint` | public git history plus archived docs | yes for two Tornado bookend observations; no provider-universe denominator | mechanism exemplar only |
| MEV Blocker | archived public documentation snapshots | no target-specific rejection or filter-list denominator | background substrate only |
| Infura | docs / ToS / API-test target in `docs/data-sources.md` | no archived v0.1 event-window probe set | future measurement target |
| Alchemy | docs / ToS / API-test target in `docs/data-sources.md` | no archived v0.1 event-window probe set | future measurement target |
| QuickNode | docs / ToS / API-test target in `docs/data-sources.md` | no archived v0.1 event-window probe set | future measurement target |
| Ankr / Chainstack / Pocket / GetBlock / BlastAPI | listed as possible public providers | no archived v0.1 event-window probe set | future measurement target |

To promote L3 from named partial observations to a measured layer, v0.2
needs a provider-by-target-by-method matrix:

| required field | purpose |
| --- | --- |
| provider universe | denominator: which providers are counted |
| target set | address / contract / transaction class being tested |
| RPC method | reproducible call shape, e.g. `eth_call`, `eth_sendRawTransaction`, `trace_*` |
| bracketing window | trigger-relative before / after timestamps |
| request / response archive | body hash or measurement ID for every probe |
| exclusion rule | how unavailable paid/private endpoints are marked |

Only after that matrix exists can the paper report an L3 rate. Until
then, L3 remains "named Flashbots mechanism evidence; no conditional
provider rate."

## Paper Phrasing Lock

Permitted:

- "L0 and L3 have zero measured denominators in v0.1."
- "The L0 OONI query cells returned no public measurements; this is an
  observability gap, not an attested negative."
- "The L3 Flashbots rows are named partial observations and support a
  mechanism case, not a provider-universe rate."

Forbidden:

- "No L0 censorship was observed" unless an event has a measured L0
  denominator and an admitted `observed_no_change` row.
- "L3 changed in 2/9 applicable cases" because the denominator is not
  measured.
- "Public RPC providers generally censor / do not censor" because v0.1
  has no complete provider census.
