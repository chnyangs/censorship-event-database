# Trigger registry

Dataset snapshot: v0.2.0-rc-dryrun-11 · cutoff `2026-06-01` · commit `5cd78e4` · generated `2026-06-01T00:23:54Z`

This is the pre-admission registry surface. It includes every YAML event plus any candidate trigger stubs under `candidate_triggers/`, so future case expansion is explicit instead of anecdotal.

## Snapshot counts

| count | value | target | gap |
| --- | ---: | ---: | ---: |
| raw registry rows | 497 | audit surface | — |
| distinct in-frame triggers | 395 | 150-250 milestone | 0 |
| admitted events | 367 | 120 quality milestone | 0 |

## Status distribution

| registry_status | count |
| --- | ---: |
| `admitted` | 367 |
| `draft` | 28 |
| `promoted_to_event` | 45 |
| `rejected` | 10 |
| `screened_no_extractor_target` | 47 |

## Temporal tier distribution

| temporal_tier | rows |
| --- | ---: |
| `comparable_main_2017_present` | 420 |
| `discovery_only_2007_2012` | 22 |
| `historical_baseline_2013_2016` | 55 |

## Analysis-use distribution

| analysis_use | rows |
| --- | ---: |
| `comparable_analysis` | 420 |
| `discovery_ledger_only` | 22 |
| `historical_baseline` | 55 |

## Stratum expansion gaps

| stratum | in-frame triggers | admitted | v0.2 admitted min | min gap | v0.2 admitted milestone | milestone gap | v0.2 candidate min | candidate gap |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `S1_ofac_sdn` | 54 | 52 | 30 | 0 | 35 | 0 | 50 | 0 |
| `S2_ofac_removal` | 1 | 1 | 5 | 4 | 10 | 9 | 10 | 9 |
| `S3_doj_sec_cftc_fiod` | 85 | 77 | 20 | 0 | 30 | 0 | 40 | 0 |
| `S4_nation_state` | 120 | 111 | 10 | 0 | 20 | 0 | 20 | 0 |
| `S5_corporate` | 105 | 96 | 10 | 0 | 15 | 0 | 20 | 0 |
| `S6_supranational` | 30 | 30 | 5 | 0 | 10 | 0 | 10 | 0 |

## Phrasing lock

- The registry gap is an expansion backlog, not a paper result.
- The 120 admitted-event number is a quality milestone, not a stop rule, cap, or freeze target.
- Raw registry rows are an audit surface and include promoted duplicates and extractor-screened rows.
- Candidate target gaps are computed from distinct in-frame triggers only.
- Admitted-only paper tables remain the only source for paper-facing event counts.
- `discovery_only` and `historical_baseline` rows are excluded from 2017+ comparable denominators unless a paper claim explicitly separates them.
- Draft, rejected, deferred, screened, and not-measurable triggers are retained to make selection visible.
