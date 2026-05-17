# Yearly Collection Plan

Dataset snapshot: v0.2.0-rc-dryrun-11 · cutoff `2026-05-17` · generated `2026-05-25T00:00:00Z`

This is the year-level control surface for the 2008+ tiered frame. It is derived from the monthly discovery ledger and trigger registry; it is not a paper denominator.

| year | tier | source-frame months | candidate-found months | pending months | registry rows | in-frame triggers | admitted | observation_closed | candidates | screened | next action |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 2008 | `discovery_only_2008_2012` | 72 | 3 | 0 | 3 | 3 | 0 | 0 | 0 | 0 | resolve source-unavailable receipts |
| 2009 | `discovery_only_2008_2012` | 72 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | resolve source-unavailable receipts |
| 2010 | `discovery_only_2008_2012` | 72 | 2 | 0 | 9 | 9 | 0 | 0 | 0 | 0 | resolve source-unavailable receipts |
| 2011 | `discovery_only_2008_2012` | 72 | 2 | 0 | 2 | 2 | 0 | 0 | 0 | 0 | resolve source-unavailable receipts |
| 2012 | `discovery_only_2008_2012` | 72 | 4 | 0 | 4 | 4 | 0 | 0 | 0 | 0 | resolve source-unavailable receipts |
| 2013 | `historical_baseline_2013_2016` | 72 | 7 | 15 | 10 | 8 | 3 | 0 | 0 | 0 | triage pending source-frame months |
| 2014 | `historical_baseline_2013_2016` | 72 | 13 | 31 | 18 | 15 | 4 | 0 | 0 | 0 | triage pending source-frame months |
| 2015 | `historical_baseline_2013_2016` | 72 | 8 | 56 | 12 | 8 | 4 | 0 | 0 | 2 | triage pending source-frame months |
| 2016 | `historical_baseline_2013_2016` | 72 | 3 | 69 | 4 | 2 | 2 | 0 | 0 | 1 | triage pending source-frame months |
| 2017 | `comparable_main_2017_present` | 72 | 6 | 66 | 10 | 7 | 3 | 0 | 0 | 2 | triage pending source-frame months |
| 2018 | `comparable_main_2017_present` | 72 | 10 | 62 | 14 | 8 | 3 | 0 | 0 | 5 | triage pending source-frame months |
| 2019 | `comparable_main_2017_present` | 72 | 4 | 68 | 6 | 3 | 3 | 0 | 0 | 3 | triage pending source-frame months |
| 2020 | `comparable_main_2017_present` | 72 | 11 | 61 | 17 | 9 | 7 | 0 | 0 | 4 | triage pending source-frame months |
| 2021 | `comparable_main_2017_present` | 72 | 17 | 55 | 29 | 23 | 10 | 0 | 0 | 2 | triage pending source-frame months |
| 2022 | `comparable_main_2017_present` | 72 | 31 | 41 | 64 | 53 | 19 | 0 | 0 | 4 | triage pending source-frame months |
| 2023 | `comparable_main_2017_present` | 72 | 38 | 34 | 77 | 64 | 31 | 0 | 0 | 6 | triage pending source-frame months |
| 2024 | `comparable_main_2017_present` | 72 | 27 | 45 | 48 | 32 | 6 | 0 | 0 | 9 | triage pending source-frame months |
| 2025 | `comparable_main_2017_present` | 72 | 13 | 59 | 25 | 11 | 10 | 0 | 0 | 7 | triage pending source-frame months |
| 2026 | `comparable_main_2017_present` | 30 | 2 | 28 | 2 | 0 | 0 | 0 | 0 | 2 | triage pending source-frame months |

## Use

- Work years top-down from oldest unresolved tier unless a current event requires immediate capture.
- Do not turn a year from `pending` into `searched_no_candidate` without a source-frame triage manifest row.
- Historical-baseline rows can become full YAML events, but stay out of 2017+ comparable denominators.
