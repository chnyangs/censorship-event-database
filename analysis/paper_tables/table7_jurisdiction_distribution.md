# Table 7 · Jurisdictional composition of the admitted corpus

Generated: `2026-05-18T10:40:00Z`.

**US-trigger share** (events with `US` in `jurisdiction`): 58/83 (69.9%) · **non-US-trigger share**: 25/83 (30.1%).

The v0.1 corpus is US-trigger-dominant (69.9% of admitted events have `US` in their jurisdiction list); second-most-touched region (under inclusive multi-jurisdiction counting): **Rest of World** (19 events). Non-Western state-actor jurisdictions (RU / CN / IN / KR / NG / TR) account for ~15.7% of country-level mentions. **Region row counts use inclusive multi-jurisdiction membership** — an event with `[UK, US]` is counted in both the US and Europe rows; do not read region shares as a partition. This concentration is a property of the sampling frame, not of the underlying phenomenon, and is driven by the frame's public-English-language-archival requirement combined with the high absolute volume of OFAC / DOJ / SEC activity in 2022-2025. The paper's landscape claims must be bounded accordingly; see `docs/paper_claims.md §0 Sampling frame` and `docs/datasheet.md §3` for the honest statement.

## Distribution by region (inclusive)

| region | events touching | share of corpus |
| --- | ---: | ---: |
| US | 58 | 69.9% |
| Europe (EU+UK+CH+non-bloc) | 18 | 21.7% |
| Rest of World | 19 | 22.9% |
| Corporate (no jurisdiction) | 6 | 7.2% |
| Other | 3 | 3.6% |
| **CORPUS TOTAL** | **83** | — |
_Region rows are inclusive — an event with jurisdictions `[UK, US]` counts in both US and Europe, so column sum (104) ≥ corpus total (83). Share column shows what fraction of admitted events touched the region, not the region's exclusive share._

## Distribution by country / bloc (all codes)

| jurisdiction code | events |
| --- | ---: |
| `US` | 58 |
| `EU` | 7 |
| `UK` | 6 |
| `corporate_global` | 6 |
| `RU` | 5 |
| `NL` | 4 |
| `DE` | 4 |
| `AU` | 4 |
| `IN` | 3 |
| `CA` | 2 |
| `CN` | 2 |
| `BE` | 1 |
| `PL` | 1 |
| `CH` | 1 |
| `KR` | 1 |
| `MY` | 1 |
| `NG` | 1 |
| `PT` | 1 |
| `IS` | 1 |
| `SG` | 1 |
| `TR` | 1 |

## What this table says (phrasing-lock)

- PREFER: "the v0.1 corpus is US-trigger-dominant and English-indexable", "~75% of admitted events have `US` in their jurisdiction list", "events outside the US/Europe block are thinner in the v0.1 frame".
- FORBID: "censorship is concentrated in the US", "non-Western jurisdictions do not censor crypto", "US is the primary site of crypto censorship". All three inversions confuse the sampling frame for the phenomenon.
- FORBID treating region shares as a partition that sums to 100% — they sum higher because of multi-jurisdiction events.
