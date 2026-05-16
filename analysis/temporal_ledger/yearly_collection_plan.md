# Yearly Collection Plan

Dataset snapshot: v0.2.0-rc-dryrun-2 · cutoff `2026-05-16` · generated `2026-05-16T12:00:00Z`

This is the year-level control surface for the 2008+ tiered frame. It is derived from the monthly discovery ledger and trigger registry; it is not a paper denominator.

| year | tier | source-frame months | candidate-found months | pending months | registry rows | in-frame triggers | admitted | observation_closed | candidates | screened | next action |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 2008 | `discovery_only_2008_2012` | 72 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | resolve source-unavailable receipts |
| 2009 | `discovery_only_2008_2012` | 72 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | resolve source-unavailable receipts |
| 2010 | `discovery_only_2008_2012` | 72 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | resolve source-unavailable receipts |
| 2011 | `discovery_only_2008_2012` | 72 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | resolve source-unavailable receipts |
| 2012 | `discovery_only_2008_2012` | 72 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | resolve source-unavailable receipts |
| 2013 | `historical_baseline_2013_2016` | 72 | 3 | 16 | 4 | 3 | 2 | 0 | 1 | 0 | triage pending source-frame months |
| 2014 | `historical_baseline_2013_2016` | 72 | 3 | 38 | 4 | 4 | 0 | 0 | 4 | 0 | triage pending source-frame months |
| 2015 | `historical_baseline_2013_2016` | 72 | 5 | 59 | 6 | 4 | 1 | 0 | 3 | 2 | triage pending source-frame months |
| 2016 | `historical_baseline_2013_2016` | 72 | 3 | 69 | 3 | 2 | 0 | 0 | 2 | 1 | triage pending source-frame months |
| 2017 | `comparable_main_2017_present` | 72 | 3 | 69 | 5 | 2 | 2 | 0 | 0 | 2 | triage pending source-frame months |
| 2018 | `comparable_main_2017_present` | 72 | 5 | 67 | 8 | 2 | 2 | 0 | 0 | 5 | triage pending source-frame months |
| 2019 | `comparable_main_2017_present` | 72 | 2 | 70 | 4 | 1 | 1 | 0 | 0 | 3 | triage pending source-frame months |
| 2020 | `comparable_main_2017_present` | 72 | 7 | 65 | 12 | 5 | 3 | 0 | 2 | 4 | triage pending source-frame months |
| 2021 | `comparable_main_2017_present` | 72 | 10 | 62 | 14 | 9 | 6 | 0 | 3 | 2 | triage pending source-frame months |
| 2022 | `comparable_main_2017_present` | 72 | 16 | 56 | 27 | 16 | 15 | 0 | 1 | 4 | triage pending source-frame months |
| 2023 | `comparable_main_2017_present` | 72 | 23 | 49 | 33 | 22 | 16 | 0 | 5 | 6 | triage pending source-frame months |
| 2024 | `comparable_main_2017_present` | 72 | 12 | 60 | 24 | 8 | 6 | 0 | 1 | 9 | triage pending source-frame months |
| 2025 | `comparable_main_2017_present` | 72 | 10 | 62 | 22 | 8 | 8 | 0 | 0 | 7 | triage pending source-frame months |
| 2026 | `comparable_main_2017_present` | 30 | 2 | 28 | 2 | 0 | 0 | 0 | 0 | 2 | triage pending source-frame months |

## Use

- Work years top-down from oldest unresolved tier unless a current event requires immediate capture.
- Do not turn a year from `pending` into `searched_no_candidate` without a source-frame triage manifest row.
- Historical-baseline rows can become full YAML events, but stay out of 2017+ comparable denominators.
