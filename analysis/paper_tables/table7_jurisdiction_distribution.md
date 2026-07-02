# Table 7 · Jurisdictional composition of the admitted corpus

Generated: `2026-06-25T23:48:26Z`.

**US-trigger share** (events with `US` in `jurisdiction`): 181/398 (45.5%) · **non-US-trigger share**: 217/398 (54.5%).

This snapshot is US-trigger-heavy (45.5% of admitted events have `US` in their jurisdiction list); second-most-touched region (under inclusive multi-jurisdiction counting): **Other** (90 events). Non-Western state-actor jurisdictions (RU / CN / IN / KR / NG / TR) account for ~13.8% of country-level mentions. **Region row counts use inclusive multi-jurisdiction membership** — an event with `[UK, US]` is counted in both the US and Europe rows; do not read region shares as a partition. This concentration is a property of the sampling frame, not of the underlying phenomenon, and is driven by the frame's public-English-language-archival requirement combined with the high absolute volume of OFAC / DOJ / SEC activity in 2022-2025. The paper's landscape claims must be bounded accordingly; see `docs/paper_claims.md §0 Sampling frame` and `docs/datasheet.md §3` for the honest statement.

## Distribution by region (inclusive)

| region | events touching | share of corpus |
| --- | ---: | ---: |
| US | 181 | 45.5% |
| Europe (EU+UK+CH+non-bloc) | 60 | 15.1% |
| Rest of World | 70 | 17.6% |
| Corporate (no jurisdiction) | 53 | 13.3% |
| Other | 90 | 22.6% |
| **CORPUS TOTAL** | **398** | — |
_Region rows are inclusive — an event with jurisdictions `[UK, US]` counts in both US and Europe, so column sum (454) ≥ corpus total (398). Share column shows what fraction of admitted events touched the region, not the region's exclusive share._

## Distribution by country / bloc (all codes)

| jurisdiction code | events |
| --- | ---: |
| `US` | 181 |
| `corporate_global` | 53 |
| `EU` | 29 |
| `RU` | 19 |
| `UK` | 17 |
| `CN` | 14 |
| `JP` | 14 |
| `UN` | 10 |
| `KR` | 9 |
| `CA` | 8 |
| `NL` | 7 |
| `AU` | 7 |
| `IN` | 6 |
| `DE` | 6 |
| `IR` | 6 |
| `NG` | 5 |
| `TH` | 5 |
| `IS` | 4 |
| `HK` | 4 |
| `ID` | 4 |
| `AR` | 3 |
| `IL` | 3 |
| `UA` | 3 |
| `SG` | 3 |
| `CH` | 3 |
| `PH` | 3 |
| `BD` | 2 |
| `BR` | 2 |
| `FR` | 2 |
| `KH` | 2 |
| `ET` | 2 |
| `KZ` | 2 |
| `NP` | 2 |
| `TW` | 2 |
| `TR` | 2 |
| `AE` | 2 |
| `ZW` | 2 |
| `DZ` | 1 |
| `BE` | 1 |
| `BO` | 1 |
| `PL` | 1 |
| `EC` | 1 |
| `EG` | 1 |
| `JO` | 1 |
| `KE` | 1 |
| `KW` | 1 |
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

- PREFER: "the current admitted corpus is US-trigger-heavy and English-indexable (181/398, 45.5%)", "region shares are inclusive, not a partition", "events outside the US/Europe block are thinner in this evidence frame".
- FORBID: "censorship is concentrated in the US", "non-Western jurisdictions do not censor crypto", "US is the primary site of crypto censorship". All three inversions confuse the sampling frame for the phenomenon.
- FORBID treating region shares as a partition that sums to 100% — they sum higher because of multi-jurisdiction events.
