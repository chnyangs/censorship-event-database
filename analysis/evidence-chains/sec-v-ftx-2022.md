# Evidence chain — `sec-v-ftx-2022`

**Status**: `admitted` · **Stratum**: `S3_doj_sec_cftc_fiod` · **Shape**: `null_event` (0 changed layer(s): none) · **Tier**: `null_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-02` · **Source commit**: `c736a32` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-21` · **Tool version**: `0.1.0` · **Generated**: `2026-06-02T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "The 2022-12-13 SEC civil securities-fraud complaint against Samuel
> Bankman-Fried (Case 1:22-cv-10501, SDNY) — filed in parallel with the
> DOJ SDNY criminal indictment and CFTC civil complaint — produced no new
> cross-layer cascade attributable to the SEC trigger specifically. The
> FTX.com / FTX.US offramp was already administratively frozen by the
> 2022-11-11 voluntary Chapter 11 filing approximately one month earlier,
> and the broader 2022-12-13 multi-agency offramp_cex observation is
> booked under the sibling ftx-bankman-fried-doj-2022 row. This row is
> coded as empirical_shape=null_event / admission_tier=null_case to serve
> as a denominator-control sibling documenting that parallel-agency civil
> enforcement on top of a pre-collapsed platform produces no incremental
> observed_change."

## 1. Trigger

- **Type**: `sec_action`
- **Actor**: `US_SEC`
- **Timestamp**: `2022-12-13 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://www.sec.gov/news/press-release/2022-219>
  - Wayback: <https://web.archive.org/web/2022/https://www.sec.gov/news/press-release/2022-219>
  > SEC press release 2022-219 (2022-12-13): "SEC Charges Samuel
> Bankman-Fried with Defrauding Investors in Crypto Asset Trading
> Platform FTX." Same-day civil complaint filed in SDNY (Case No.
> 1:22-cv-10501) alleging Bankman-Fried orchestrated a multi-year
> scheme to defraud FTX equity investors of more than $1.8B while
> diverting customer funds to Alameda Research and providing Alameda
> with a virtually unlimited line of credit funded by FTX customer
> deposits. Charges securities fraud against Bankman-Fried in his
> capacity as CEO/co-founder of FTX Trading Ltd. Wayback wildcard
> pointer in lieu of pinned-timestamp snapshot;
> evidence_use=contextual_unarchived pending human-audit re-pin.
- **`primary_legal`**
  - URL: <https://www.sec.gov/files/litigation/complaints/2022/comp-pr2022-219.pdf>
  - Wayback: <https://web.archive.org/web/2022/https://www.sec.gov/files/litigation/complaints/2022/comp-pr2022-219.pdf>
  > SEC civil complaint document (Case 1:22-cv-10501, filed 12/13/22,
> SDNY). 28-page complaint enumerating the securities-fraud counts
> against Bankman-Fried. Wayback wildcard pointer in lieu of
> pinned-timestamp snapshot; evidence_use=contextual_unarchived
> pending human-audit re-pin.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Samuel Bankman-Fried / FTX Trading Ltd.
- **Canonical domains**: `ftx.com`, `ftx.us`

> Samuel Bankman-Fried (individual defendant in the SEC civil complaint,
> Case 1:22-cv-10501, SDNY) and FTX Trading Ltd. (the operator of the
> FTX.com international exchange, referenced as the corporate vehicle
> through which the alleged securities-fraud scheme was executed). The
> target slice does not enumerate Alameda Research LLC (named in the
> parallel CFTC complaint but central to the SEC complaint as the
> diversion destination for FTX customer funds) or the dozens of
> additional FTX-affiliated entities in the Delaware Chapter 11
> schedules. Parallel-agency sibling row to ftx-bankman-fried-doj-2022
> (DOJ criminal) and cftc-v-ftx-2022 (CFTC civil); same physical
> defendants, distinct statutory authority (federal securities laws vs.
> federal criminal code vs. Commodity Exchange Act).

## 3. Changed-layer observations (supports the scoped claim)

*No observed_change entries. This is a `null_event`; see §4 for observed_no_change evidence supporting the null claim.*

## 4. No-change observations (where applicable)

### offramp_cex — `no_incremental_sec_attributable_offramp_change_after_preexisting_chapter_11_freeze`

**Window**: `2022-12-13 00:00:00+00:00` → `2022-12-31 23:59:59+00:00`

**Sources**:

- **`primary_legal`**
  - URL: <https://www.sec.gov/newsroom/press-releases/2022-219>
  - body_hash: `sha256:042642a33be6d8349b1e21bc8b600593bccdec31bb6dd91a61bfdbb24b54bddb`
  - body_path: `sources/http_captures/sec-v-ftx-2022/v0_3_primary_repair/www.sec.gov__newsroom-press-releases-2022-219__923a9a0e93.html`
  > SEC's own release anchors the 2022-12-13 securities-fraud civil
> complaint as a parallel filing against Bankman-Fried / FTX. The
> row-local observation is observed_no_change: the SEC filing does
> not itself provide a new off-ramp operational action beyond the
> pre-existing Chapter 11 freeze captured in the sibling DOJ row
> ftx-bankman-fried-doj-2022. Live sec.gov capture pre-pinned in
> v0_3_primary_repair/.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`ftx-bankman-fried-doj-2022`](./ftx-bankman-fried-doj-2022.md)
- [`cftc-v-ftx-2022`](./cftc-v-ftx-2022.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `c736a32`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

