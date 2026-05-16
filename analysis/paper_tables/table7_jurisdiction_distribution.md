# Table 7 · Jurisdictional composition of the admitted corpus

Generated: `2026-05-16T12:00:00Z`.

**US-trigger share** (events with `US` in `jurisdiction`): 46/62 (74.2%) · **non-US-trigger share**: 16/62 (25.8%).

The v0.1 corpus is US-trigger-dominant (74.2% of admitted events have `US` in their jurisdiction list); second-most-touched region (under inclusive multi-jurisdiction counting): **Europe (EU+UK+CH+non-bloc)** (16 events). Non-Western state-actor jurisdictions (RU / CN / IN / KR / NG / TR) account for ~16.1% of country-level mentions. **Region row counts use inclusive multi-jurisdiction membership** — an event with `[UK, US]` is counted in both the US and Europe rows; do not read region shares as a partition. This concentration is a property of the sampling frame, not of the underlying phenomenon, and is driven by the frame's public-English-language-archival requirement combined with the high absolute volume of OFAC / DOJ / SEC activity in 2022-2025. The paper's landscape claims must be bounded accordingly; see `docs/paper_claims.md §0 Sampling frame` and `docs/datasheet.md §3` for the honest statement.

## Distribution by region (inclusive)

| region | events touching | share of corpus |
| --- | ---: | ---: |
| US | 46 | 74.2% |
| Europe (EU+UK+CH+non-bloc) | 16 | 25.8% |
| Rest of World | 15 | 24.2% |
| Corporate (no jurisdiction) | 4 | 6.5% |
| **CORPUS TOTAL** | **62** | — |
_Region rows are inclusive — an event with jurisdictions `[UK, US]` counts in both US and Europe, so column sum (81) ≥ corpus total (62). Share column shows what fraction of admitted events touched the region, not the region's exclusive share._

## Distribution by country / bloc (all codes)

| jurisdiction code | events |
| --- | ---: |
| `US` | 46 |
| `UK` | 6 |
| `EU` | 6 |
| `DE` | 4 |
| `corporate_global` | 4 |
| `AU` | 4 |
| `NL` | 3 |
| `RU` | 3 |
| `CN` | 2 |
| `IN` | 2 |
| `CA` | 1 |
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
