# Yearly Collection Plan

Dataset snapshot: v0.2.0-rc-dryrun-11 · cutoff `2026-06-01` · generated `2026-06-01T04:52:47Z`

This is the year-level control surface for the 2008+ tiered frame. It is derived from the monthly discovery ledger and trigger registry; it is not a paper denominator.

| year | tier | source-frame months | candidate-found months | pending months | registry rows | in-frame triggers | admitted | observation_closed | candidates | screened | next action |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 2006 | `` | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | maintain exhausted-year receipts |
| 2007 | `discovery_only_2007_2012` | 72 | 1 | 0 | 2 | 2 | 2 | 0 | 0 | 0 | resolve source-unavailable receipts |
| 2008 | `discovery_only_2007_2012` | 72 | 3 | 0 | 3 | 3 | 3 | 0 | 0 | 0 | resolve source-unavailable receipts |
| 2009 | `discovery_only_2007_2012` | 72 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | resolve source-unavailable receipts |
| 2010 | `discovery_only_2007_2012` | 72 | 2 | 0 | 9 | 9 | 9 | 0 | 0 | 0 | resolve source-unavailable receipts |
| 2011 | `discovery_only_2007_2012` | 72 | 2 | 0 | 2 | 2 | 2 | 0 | 0 | 0 | resolve source-unavailable receipts |
| 2012 | `discovery_only_2007_2012` | 72 | 5 | 0 | 5 | 4 | 4 | 0 | 0 | 0 | resolve source-unavailable receipts |
| 2013 | `historical_baseline_2013_2016` | 72 | 9 | 14 | 14 | 12 | 11 | 0 | 0 | 0 | triage pending source-frame months |
| 2014 | `historical_baseline_2013_2016` | 72 | 14 | 30 | 24 | 21 | 19 | 0 | 0 | 0 | triage pending source-frame months |
| 2015 | `historical_baseline_2013_2016` | 72 | 10 | 54 | 13 | 8 | 8 | 0 | 0 | 2 | triage pending source-frame months |
| 2016 | `historical_baseline_2013_2016` | 72 | 3 | 69 | 4 | 2 | 2 | 0 | 0 | 1 | triage pending source-frame months |
| 2017 | `comparable_main_2017_present` | 72 | 10 | 62 | 16 | 12 | 11 | 0 | 0 | 2 | triage pending source-frame months |
| 2018 | `comparable_main_2017_present` | 72 | 16 | 56 | 24 | 18 | 16 | 0 | 0 | 5 | triage pending source-frame months |
| 2019 | `comparable_main_2017_present` | 72 | 12 | 60 | 17 | 14 | 12 | 0 | 0 | 3 | triage pending source-frame months |
| 2020 | `comparable_main_2017_present` | 72 | 15 | 57 | 23 | 15 | 13 | 0 | 0 | 4 | triage pending source-frame months |
| 2021 | `comparable_main_2017_present` | 72 | 24 | 48 | 47 | 41 | 37 | 0 | 0 | 2 | triage pending source-frame months |
| 2022 | `comparable_main_2017_present` | 72 | 36 | 36 | 76 | 65 | 60 | 0 | 0 | 4 | triage pending source-frame months |
| 2023 | `comparable_main_2017_present` | 72 | 42 | 30 | 100 | 83 | 79 | 0 | 0 | 6 | triage pending source-frame months |
| 2024 | `comparable_main_2017_present` | 72 | 35 | 37 | 70 | 53 | 51 | 0 | 0 | 9 | triage pending source-frame months |
| 2025 | `comparable_main_2017_present` | 72 | 22 | 50 | 42 | 28 | 25 | 0 | 0 | 7 | triage pending source-frame months |
| 2026 | `comparable_main_2017_present` | 36 | 5 | 31 | 5 | 3 | 1 | 0 | 0 | 2 | triage pending source-frame months |

## Use

- Work years top-down from oldest unresolved tier unless a current event requires immediate capture.
- Do not turn a year from `pending` into `searched_no_candidate` without a source-frame triage manifest row.
- Historical-baseline rows can become full YAML events, but stay out of 2017+ comparable denominators.
