# Trigger registry

Dataset snapshot: v0.1.0 · cutoff `2026-05-06` · commit `947f18f` · generated `2026-05-06T10:56:34Z`

This is the pre-admission registry surface. It includes every YAML event plus any candidate trigger stubs under `candidate_triggers/`, so future case expansion is explicit instead of anecdotal.

## Snapshot counts

| count | value | target | gap |
| --- | ---: | ---: | ---: |
| raw registry rows | 126 | audit surface | — |
| distinct in-frame triggers | 54 | 150-250 | 96 |
| admitted events | 53 | 80-120 | 27 |

## Status distribution

| registry_status | count |
| --- | ---: |
| `admitted` | 53 |
| `candidate` | 1 |
| `promoted_to_event` | 25 |
| `screened_no_extractor_target` | 47 |

## Stratum expansion gaps

| stratum | in-frame triggers | admitted | v0.2 admitted min | admitted gap | v0.2 candidate min | candidate gap |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `S1_ofac_sdn` | 27 | 26 | 30 | 4 | 50 | 23 |
| `S2_ofac_removal` | 1 | 1 | 5 | 4 | 10 | 9 |
| `S3_doj_sec_cftc_fiod` | 12 | 12 | 20 | 8 | 40 | 28 |
| `S4_nation_state` | 6 | 6 | 10 | 4 | 20 | 14 |
| `S5_corporate` | 6 | 6 | 10 | 4 | 20 | 14 |
| `S6_supranational` | 2 | 2 | 5 | 3 | 10 | 8 |

## Phrasing lock

- The registry gap is an expansion backlog, not a paper result.
- Raw registry rows are an audit surface and include promoted duplicates and extractor-screened rows.
- Candidate target gaps are computed from distinct in-frame triggers only.
- Admitted-only paper tables remain the only source for paper-facing event counts.
- Draft, rejected, deferred, screened, and not-measurable triggers are retained to make selection visible.
