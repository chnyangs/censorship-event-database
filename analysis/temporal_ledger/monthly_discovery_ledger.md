# Monthly Discovery Ledger

Dataset snapshot: v0.2.0-rc-dryrun-9 · cutoff `2026-05-16` · generated `2026-05-23T00:00:00Z`

This ledger covers every declared source frame for every month from `sampling/frame.yaml::snapshot_scope.historical_start` through the dataset cutoff. A `pending` row means the month has not yet been triaged; it is not evidence that no candidate exists.

- Source frames: 6
- Monthly rows: 1326
- Rows with candidates/events: 151

## Status Distribution

| ledger_status | rows |
| --- | ---: |
| `candidate_found` | 151 |
| `pending` | 732 |
| `source_unavailable` | 443 |

## Temporal Tier Distribution

| temporal_tier | rows |
| --- | ---: |
| `comparable_main_2017_present` | 678 |
| `discovery_only_2008_2012` | 360 |
| `historical_baseline_2013_2016` | 288 |

## Contract

- `discovery_only_2008_2012` rows are discovery-ledger rows by default.
- `historical_baseline_2013_2016` rows may become full event YAMLs, but stay out of 2017+ comparable denominators unless a claim explicitly separates the historical baseline.
- `comparable_main_2017_present` is the only default tier for current cross-layer comparable analysis.
- Empty months remain visible as `pending`, `searched_no_candidate`, `not_applicable_pre_market`, or `source_unavailable` rather than disappearing.
