# Yearly Collection Plan

Dataset snapshot: v0.2.0-rc-dryrun-5 · cutoff `2026-05-16` · generated `2026-05-19T00:00:00Z`

This is the year-level control surface for the 2008+ tiered frame. It is derived from the monthly discovery ledger and trigger registry; it is not a paper denominator.

| year | tier | source-frame months | candidate-found months | pending months | registry rows | in-frame triggers | admitted | observation_closed | candidates | screened | next action |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 2008 | `discovery_only_2008_2012` | 72 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | resolve source-unavailable receipts |
| 2009 | `discovery_only_2008_2012` | 72 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | resolve source-unavailable receipts |
| 2010 | `discovery_only_2008_2012` | 72 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | resolve source-unavailable receipts |
| 2011 | `discovery_only_2008_2012` | 72 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | resolve source-unavailable receipts |
| 2012 | `discovery_only_2008_2012` | 72 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | resolve source-unavailable receipts |
| 2013 | `historical_baseline_2013_2016` | 72 | 6 | 16 | 9 | 7 | 3 | 0 | 0 | 0 | triage pending source-frame months |
| 2014 | `historical_baseline_2013_2016` | 72 | 9 | 35 | 12 | 9 | 4 | 0 | 0 | 0 | triage pending source-frame months |
| 2015 | `historical_baseline_2013_2016` | 72 | 8 | 56 | 12 | 8 | 4 | 0 | 0 | 2 | triage pending source-frame months |
| 2016 | `historical_baseline_2013_2016` | 72 | 3 | 69 | 4 | 2 | 2 | 0 | 0 | 1 | triage pending source-frame months |
| 2017 | `comparable_main_2017_present` | 72 | 4 | 68 | 6 | 3 | 3 | 0 | 0 | 2 | triage pending source-frame months |
| 2018 | `comparable_main_2017_present` | 72 | 6 | 66 | 9 | 3 | 3 | 0 | 0 | 5 | triage pending source-frame months |
| 2019 | `comparable_main_2017_present` | 72 | 4 | 68 | 6 | 3 | 3 | 0 | 0 | 3 | triage pending source-frame months |
| 2020 | `comparable_main_2017_present` | 72 | 9 | 63 | 15 | 7 | 7 | 0 | 0 | 4 | triage pending source-frame months |
| 2021 | `comparable_main_2017_present` | 72 | 11 | 61 | 16 | 10 | 10 | 0 | 0 | 2 | triage pending source-frame months |
| 2022 | `comparable_main_2017_present` | 72 | 17 | 55 | 30 | 19 | 19 | 0 | 0 | 4 | triage pending source-frame months |
| 2023 | `comparable_main_2017_present` | 72 | 29 | 43 | 45 | 32 | 31 | 0 | 0 | 6 | triage pending source-frame months |
| 2024 | `comparable_main_2017_present` | 72 | 12 | 60 | 24 | 8 | 6 | 0 | 0 | 9 | triage pending source-frame months |
| 2025 | `comparable_main_2017_present` | 72 | 12 | 60 | 24 | 10 | 10 | 0 | 0 | 7 | triage pending source-frame months |
| 2026 | `comparable_main_2017_present` | 30 | 2 | 28 | 2 | 0 | 0 | 0 | 0 | 2 | triage pending source-frame months |

## Use

- Work years top-down from oldest unresolved tier unless a current event requires immediate capture.
- Do not turn a year from `pending` into `searched_no_candidate` without a source-frame triage manifest row.
- Historical-baseline rows can become full YAML events, but stay out of 2017+ comparable denominators.
