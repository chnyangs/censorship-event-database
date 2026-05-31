# Table 7 · Jurisdictional composition of the admitted corpus

Generated: `2026-05-31T12:31:46Z`.

**US-trigger share** (events with `US` in `jurisdiction`): 159/368 (43.2%) · **non-US-trigger share**: 209/368 (56.8%).

The v0.1 corpus is US-trigger-dominant (43.2% of admitted events have `US` in their jurisdiction list); second-most-touched region (under inclusive multi-jurisdiction counting): **Other** (85 events). Non-Western state-actor jurisdictions (RU / CN / IN / KR / NG / TR) account for ~14.7% of country-level mentions. **Region row counts use inclusive multi-jurisdiction membership** — an event with `[UK, US]` is counted in both the US and Europe rows; do not read region shares as a partition. This concentration is a property of the sampling frame, not of the underlying phenomenon, and is driven by the frame's public-English-language-archival requirement combined with the high absolute volume of OFAC / DOJ / SEC activity in 2022-2025. The paper's landscape claims must be bounded accordingly; see `docs/paper_claims.md §0 Sampling frame` and `docs/datasheet.md §3` for the honest statement.

## Distribution by region (inclusive)

| region | events touching | share of corpus |
| --- | ---: | ---: |
| US | 159 | 43.2% |
| Europe (EU+UK+CH+non-bloc) | 58 | 15.8% |
| Rest of World | 68 | 18.5% |
| Corporate (no jurisdiction) | 49 | 13.3% |
| Other | 85 | 23.1% |
| **CORPUS TOTAL** | **368** | — |
_Region rows are inclusive — an event with jurisdictions `[UK, US]` counts in both US and Europe, so column sum (419) ≥ corpus total (368). Share column shows what fraction of admitted events touched the region, not the region's exclusive share._

## Distribution by country / bloc (all codes)

| jurisdiction code | events |
| --- | ---: |
| `US` | 159 |
| `corporate_global` | 49 |
| `EU` | 28 |
| `RU` | 19 |
| `UK` | 16 |
| `CN` | 14 |
| `JP` | 14 |
| `UN` | 10 |
| `KR` | 9 |
| `NL` | 7 |
| `AU` | 7 |
| `CA` | 7 |
| `IN` | 6 |
| `DE` | 6 |
| `NG` | 4 |
| `IS` | 4 |
| `HK` | 4 |
| `ID` | 4 |
| `IR` | 4 |
| `TH` | 4 |
| `AR` | 3 |
| `IL` | 3 |
| `UA` | 3 |
| `SG` | 3 |
| `CH` | 3 |
| `PH` | 3 |
| `BR` | 2 |
| `FR` | 2 |
| `KZ` | 2 |
| `NP` | 2 |
| `TW` | 2 |
| `TR` | 2 |
| `AE` | 2 |
| `ZW` | 2 |
| `DZ` | 1 |
| `BD` | 1 |
| `BE` | 1 |
| `BO` | 1 |
| `KH` | 1 |
| `PL` | 1 |
| `EC` | 1 |
| `EG` | 1 |
| `JO` | 1 |
| `KE` | 1 |
| `MY` | 1 |
| `MA` | 1 |
| `MM` | 1 |
| `PK` | 1 |
| `QA` | 1 |
| `PT` | 1 |
| `ZA` | 1 |
| `LK` | 1 |
| `UZ` | 1 |
| `VE` | 1 |
| `VN` | 1 |

## What this table says (phrasing-lock)

- PREFER: "the v0.1 corpus is US-trigger-dominant and English-indexable", "~75% of admitted events have `US` in their jurisdiction list", "events outside the US/Europe block are thinner in the v0.1 frame".
- FORBID: "censorship is concentrated in the US", "non-Western jurisdictions do not censor crypto", "US is the primary site of crypto censorship". All three inversions confuse the sampling frame for the phenomenon.
- FORBID treating region shares as a partition that sums to 100% — they sum higher because of multi-jurisdiction events.
