# Evidence chain — `cftc-v-ftx-2022`

**Status**: `admitted` · **Stratum**: `S3_doj_sec_cftc_fiod` · **Shape**: `null_event` (0 changed layer(s): none) · **Tier**: `null_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-02` · **Source commit**: `3f1a9f2` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-20` · **Tool version**: `0.1.0` · **Generated**: `2026-06-02T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "The 2022-12-13 CFTC civil commodity-fraud complaint against Samuel
> Bankman-Fried, FTX Trading Ltd., and Alameda Research LLC is coded as
> a null_event parallel-agency sibling to ftx-bankman-fried-doj-2022.
> The offramp_cex customer-asset freeze that would otherwise be coded
> here is attributed to the DOJ parent row to avoid double-counting a
> single physical action across the three coordinated 2022-12-13 federal
> enforcement filings. The row carries no observed_change layers and
> serves as a denominator control documenting that parallel-agency
> enforcement on an already-bankrupt platform produces no additional
> cross-layer censorship/disruption observations."

## 1. Trigger

- **Type**: `cftc_action`
- **Actor**: `US_CFTC`
- **Timestamp**: `2022-12-13 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://www.cftc.gov/PressRoom/PressReleases/8638-22>
  - Wayback: <https://web.archive.org/web/2022/https://www.cftc.gov/PressRoom/PressReleases/8638-22>
  > CFTC press release 8638-22 (2022-12-13): "CFTC Charges Sam
> Bankman-Fried, FTX Trading and Alameda with Fraud and Material
> Misrepresentations." Civil enforcement complaint filed in the US
> District Court for the Southern District of New York charging
> Samuel Bankman-Fried, FTX Trading Ltd. (operator of FTX.com), and
> Alameda Research LLC with commodity-fraud violations in connection
> with the sale of digital-asset commodities in interstate commerce.
> Alleged customer losses exceeding $8B. Wayback wildcard pointer in
> lieu of pinned-timestamp snapshot; evidence_use=contextual_unarchived
> pending human-audit re-pin.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Samuel Bankman-Fried / FTX Trading Ltd. / Alameda Research LLC
- **Canonical domains**: `ftx.com`, `ftx.us`

> Samuel Bankman-Fried (individual defendant), FTX Trading Ltd. (operator
> of FTX.com international), and Alameda Research LLC (co-conspirator
> trading firm). The CFTC complaint names these three defendants on
> commodity-fraud counts; it does not enumerate the dozens of additional
> FTX-affiliated entities covered by the Delaware Chapter 11 schedules.
> The load-bearing offramp_cex effect (global withdraw-pause + customer-
> asset freeze) is attributed to the parallel ftx-bankman-fried-doj-2022
> row to avoid double-counting; this CFTC-only row is a parallel-agency
> null_event under the codebook §3 decision rule.

## 3. Changed-layer observations (supports the scoped claim)

*No observed_change entries. This is a `null_event`; see §4 for observed_no_change evidence supporting the null claim.*

## 4. No-change observations (where applicable)

### offramp_cex — `no_incremental_cftc_attributable_offramp_change_after_preexisting_chapter_11_freeze`

**Window**: `2022-12-13 00:00:00+00:00` → `2022-12-27 23:59:59+00:00`

**Sources**:

- **`primary_legal`**
  - URL: <https://www.cftc.gov/PressRoom/PressReleases/8638-22>
  - body_hash: `sha256:a2000c409763286b290961aadc3a541d520bff3f9ea039fa9aadc6670f4d7ada`
  - body_path: `sources/http_captures/cftc-v-ftx-2022/v0_3_primary_repair/www.cftc.gov__PressRoom-PressReleases-8638-22__5a31c2a5d9.html`
  > v0.3 audit 2026-05-20 (c) Batch C-2: observation row recast from
> coverage_gap to observed_no_change for non-draft compliance.
> CFTC's own release anchors the 2022-12-13 civil complaint as a
> parallel enforcement filing against already-bankrupt FTX /
> Alameda defendants. Grep substantiates 18xFTX + 11xAlameda +
> 5xBankman + 5x8638-22 + 3xSam Bankman + 3xDecember 13. The
> null-event row records that this CFTC filing does not supply a
> new exchange/off-ramp operational action beyond the pre-existing
> Chapter 11 freeze captured in the FTX parent row (parallel-
> agency dedup per codebook §3). Wayback CDX returned no mementos
> for the cftc.gov URL form; local capture retained as primary
> anchor (body_hash sha256 verified against local file).

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`ftx-bankman-fried-doj-2022`](./ftx-bankman-fried-doj-2022.md)
- [`sec-v-ftx-2022`](./sec-v-ftx-2022.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `3f1a9f2`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

