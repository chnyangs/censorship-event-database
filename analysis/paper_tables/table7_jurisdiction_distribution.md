# Table 7 · Jurisdictional composition of the admitted corpus

Generated: `2026-04-24T09:59:02Z`.

**US-trigger share** (events with `US` in `jurisdiction`): 40/53 (75.5%) · **non-US-trigger share**: 13/53 (24.5%).

The v0.1 corpus is US-trigger-dominant (75.5% of admitted events have `US` in their jurisdiction list); second-most-touched region (under inclusive multi-jurisdiction counting): **Europe (EU+UK+CH+non-bloc)** (13 events). Non-Western state-actor jurisdictions (RU / CN / IN / KR / NG / TR) account for ~15.1% of country-level mentions. **Region row counts use inclusive multi-jurisdiction membership** — an event with `[UK, US]` is counted in both the US and Europe rows; do not read region shares as a partition. This concentration is a property of the sampling frame, not of the underlying phenomenon, and is driven by the frame's public-English-language-archival requirement combined with the high absolute volume of OFAC / DOJ / SEC activity in 2022-2025. The paper's landscape claims must be bounded accordingly; see `docs/paper_claims.md §0 Sampling frame` and `docs/datasheet.md §3` for the honest statement.

## Distribution by region (inclusive)

| region | events touching | share of corpus |
| --- | ---: | ---: |
| US | 40 | 75.5% |
| Europe (EU+UK+CH+non-bloc) | 13 | 24.5% |
| Rest of World | 13 | 24.5% |
| Corporate (no jurisdiction) | 4 | 7.5% |
| **CORPUS TOTAL** | **53** | — |
_Region rows are inclusive — an event with jurisdictions `[UK, US]` counts in both US and Europe, so column sum (70) ≥ corpus total (53). Share column shows what fraction of admitted events touched the region, not the region's exclusive share._

## Distribution by country / bloc (all codes)

| jurisdiction code | events |
| --- | ---: |
| `US` | 40 |
| `UK` | 5 |
| `EU` | 5 |
| `DE` | 4 |
| `corporate_global` | 4 |
| `AU` | 4 |
| `IN` | 2 |
| `NL` | 2 |
| `RU` | 2 |
| `CA` | 1 |
| `CN` | 1 |
| `PL` | 1 |
| `CH` | 1 |
| `KR` | 1 |
| `NG` | 1 |
| `PT` | 1 |
| `IS` | 1 |
| `TR` | 1 |

## What this table says (phrasing-lock)

- PREFER: "the v0.1 corpus is US-trigger-dominant and English-indexable", "~75% of admitted events have `US` in their jurisdiction list", "events outside the US/Europe block are thinner in the v0.1 frame".
- FORBID: "censorship is concentrated in the US", "non-Western jurisdictions do not censor crypto", "US is the primary site of crypto censorship". All three inversions confuse the sampling frame for the phenomenon.
- FORBID treating region shares as a partition that sums to 100% — they sum higher because of multi-jurisdiction events.
