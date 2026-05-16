# Trigger registry

Dataset snapshot: v0.2.0-rc-dryrun-2 · cutoff `2026-05-16` · commit `c6bc9d9` · generated `2026-05-18T10:40:00Z`

This is the pre-admission registry surface. It includes every YAML event plus any candidate trigger stubs under `candidate_triggers/`, so future case expansion is explicit instead of anecdotal.

## Snapshot counts

| count | value | target | gap |
| --- | ---: | ---: | ---: |
| raw registry rows | 179 | audit surface | — |
| distinct in-frame triggers | 86 | 150-250 milestone | 64 |
| admitted events | 83 | 120 quality milestone | 37 |

## Status distribution

| registry_status | count |
| --- | ---: |
| `admitted` | 83 |
| `draft` | 3 |
| `promoted_to_event` | 45 |
| `rejected` | 1 |
| `screened_no_extractor_target` | 47 |

## Temporal tier distribution

| temporal_tier | rows |
| --- | ---: |
| `comparable_main_2017_present` | 155 |
| `historical_baseline_2013_2016` | 24 |

## Analysis-use distribution

| analysis_use | rows |
| --- | ---: |
| `comparable_analysis` | 155 |
| `historical_baseline` | 24 |

## Stratum expansion gaps

| stratum | in-frame triggers | admitted | v0.2 admitted min | min gap | v0.2 admitted milestone | milestone gap | v0.2 candidate min | candidate gap |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `S1_ofac_sdn` | 27 | 26 | 30 | 4 | 35 | 9 | 50 | 23 |
| `S2_ofac_removal` | 1 | 1 | 5 | 4 | 10 | 9 | 10 | 9 |
| `S3_doj_sec_cftc_fiod` | 30 | 30 | 20 | 0 | 30 | 0 | 40 | 10 |
| `S4_nation_state` | 15 | 14 | 10 | 0 | 20 | 6 | 20 | 5 |
| `S5_corporate` | 9 | 8 | 10 | 2 | 15 | 7 | 20 | 11 |
| `S6_supranational` | 4 | 4 | 5 | 1 | 10 | 6 | 10 | 6 |

## Phrasing lock

- The registry gap is an expansion backlog, not a paper result.
- The 120 admitted-event number is a quality milestone, not a stop rule, cap, or freeze target.
- Raw registry rows are an audit surface and include promoted duplicates and extractor-screened rows.
- Candidate target gaps are computed from distinct in-frame triggers only.
- Admitted-only paper tables remain the only source for paper-facing event counts.
- `discovery_only` and `historical_baseline` rows are excluded from 2017+ comparable denominators unless a paper claim explicitly separates them.
- Draft, rejected, deferred, screened, and not-measurable triggers are retained to make selection visible.
