# Trigger registry

Dataset snapshot: v0.2.0-rc-dryrun-10 · cutoff `2026-05-16` · commit `36d266a` · generated `2026-05-24T00:00:00Z`

This is the pre-admission registry surface. It includes every YAML event plus any candidate trigger stubs under `candidate_triggers/`, so future case expansion is explicit instead of anecdotal.

## Snapshot counts

| count | value | target | gap |
| --- | ---: | ---: | ---: |
| raw registry rows | 259 | audit surface | — |
| distinct in-frame triggers | 166 | 150-250 milestone | 0 |
| admitted events | 105 | 120 quality milestone | 15 |

## Status distribution

| registry_status | count |
| --- | ---: |
| `admitted` | 105 |
| `draft` | 61 |
| `promoted_to_event` | 45 |
| `rejected` | 1 |
| `screened_no_extractor_target` | 47 |

## Temporal tier distribution

| temporal_tier | rows |
| --- | ---: |
| `comparable_main_2017_present` | 212 |
| `discovery_only_2008_2012` | 10 |
| `historical_baseline_2013_2016` | 37 |

## Analysis-use distribution

| analysis_use | rows |
| --- | ---: |
| `comparable_analysis` | 212 |
| `discovery_ledger_only` | 10 |
| `historical_baseline` | 37 |

## Stratum expansion gaps

| stratum | in-frame triggers | admitted | v0.2 admitted min | min gap | v0.2 admitted milestone | milestone gap | v0.2 candidate min | candidate gap |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `S1_ofac_sdn` | 32 | 26 | 30 | 4 | 35 | 9 | 50 | 18 |
| `S2_ofac_removal` | 1 | 1 | 5 | 4 | 10 | 9 | 10 | 9 |
| `S3_doj_sec_cftc_fiod` | 52 | 42 | 20 | 0 | 30 | 0 | 40 | 0 |
| `S4_nation_state` | 38 | 18 | 10 | 0 | 20 | 2 | 20 | 0 |
| `S5_corporate` | 33 | 11 | 10 | 0 | 15 | 4 | 20 | 0 |
| `S6_supranational` | 10 | 7 | 5 | 0 | 10 | 3 | 10 | 0 |

## Phrasing lock

- The registry gap is an expansion backlog, not a paper result.
- The 120 admitted-event number is a quality milestone, not a stop rule, cap, or freeze target.
- Raw registry rows are an audit surface and include promoted duplicates and extractor-screened rows.
- Candidate target gaps are computed from distinct in-frame triggers only.
- Admitted-only paper tables remain the only source for paper-facing event counts.
- `discovery_only` and `historical_baseline` rows are excluded from 2017+ comparable denominators unless a paper claim explicitly separates them.
- Draft, rejected, deferred, screened, and not-measurable triggers are retained to make selection visible.
