# Evidence chain — `ftx-bankman-fried-doj-2022`

**Status**: `admitted` · **Stratum**: `S3_doj_sec_cftc_fiod` · **Shape**: `null_event` (0 changed layer(s): none) · **Tier**: `null_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-02` · **Source commit**: `c736a32` · **Schema**: `0.2.0` · **Event last_verified**: `2026-06-01` · **Tool version**: `0.1.0` · **Generated**: `2026-06-02T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "The 2022-12-13 DOJ SDNY criminal indictment of Samuel Bankman-Fried is
> coded as a null-control federal-enforcement row: the FTX.com / FTX.US /
> Alameda off-ramp surface was already under the FTX Chapter 11 estate from
> the 2022-11-11 bankruptcy filing, and the DOJ trigger produced no new
> measured exchange/off-ramp, frontend, network, RPC, consensus, or
> issuer-freeze access change. The row is a denominator-control sibling to
> the same-day SEC and CFTC FTX rows."

## 1. Trigger

- **Type**: `doj_indictment`
- **Actor**: `US_DOJ_SDNY`
- **Timestamp**: `2022-12-13 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://www.justice.gov/d9/press-releases/attachments/2022/12/13/u.s._v._bankman-fried_indictment_0.pdf>
  - body_hash: `sha256:78f9ce2e758d146f6d6f48a3d14dde095b7eb64c693b13adca9474f9409b4719`
  - body_path: `sources/http_captures/ftx-bankman-fried-doj-2022/primary/www.justice.gov__d9-press-releases-attachments-2022-12-13-u.s._v._bankman-fried_indictment_0.pdf__ad5b705de1.bin`
  > DOJ-hosted U.S. v. Bankman-Fried indictment PDF for the 2022-12-13
> SDNY criminal case. The current DOJ HTML press-release surface
> returned an Akamai interstitial during automated capture, so the
> replayable official PDF is the load-bearing DOJ trigger anchor.
- **`primary_legal`**
  - URL: <https://www.sec.gov/newsroom/press-releases/2022-219>
  - body_hash: `sha256:4908c20f3da88e9cb492819dbe55fdfd731ccaa997491de955ef8de480a47276`
  - body_path: `sources/http_captures/ftx-bankman-fried-doj-2022/primary/www.sec.gov__newsroom-press-releases-2022-219__923a9a0e93.html`
  > SEC press release 2022-219, captured locally, corroborates the same
> 2022-12-13 multi-agency FTX enforcement date and states that the
> U.S. Attorney's Office for SDNY and CFTC announced parallel charges
> against Bankman-Fried.
- **`primary_legal`**
  - URL: <https://www.cftc.gov/PressRoom/PressReleases/8638-22>
  - body_hash: `sha256:0be01c582e41a2ffd9042074660125186626665220ff6128dc6c0d021317d220`
  - body_path: `sources/http_captures/ftx-bankman-fried-doj-2022/primary/www.cftc.gov__PressRoom-PressReleases-8638-22__5a31c2a5d9.html`
  > CFTC press release 8638-22, captured locally, corroborates the
> same-day parallel CFTC and DOJ/SEC actions and names Bankman-Fried,
> FTX Trading Ltd. d/b/a FTX.com, and Alameda Research LLC.
- **`primary_corporate`**
  - URL: <https://www.prnewswire.com/news-releases/ftx-receives-court-approval-for-first-day-motions-301685748.html>
  - body_hash: `sha256:00d80a76a9f51da40965a60afc9327f10f2f2bbd3375ee900b39a7582ebdf3d6`
  - body_path: `sources/http_captures/ftx-bankman-fried-doj-2022/primary/www.prnewswire.com__news-releases-ftx-receives-court-approval-for-first-day-motions-301685748.html__ebf96d93a3.html`
  > FTX-sourced PRNewswire release on first-day bankruptcy motions.
> It anchors that FTX Trading Ltd. and affiliated debtors filed
> Chapter 11 petitions on 2022-11-11, before the 2022-12-13 DOJ
> trigger, and that Kroll was the claims agent for official court
> documents.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Samuel Bankman-Fried / FTX Trading Ltd. / Alameda Research LLC
- **Canonical domains**: `ftx.com`, `ftx.us`

> Samuel Bankman-Fried, FTX Trading Ltd. d/b/a FTX.com, and Alameda
> Research LLC are the load-bearing entities for the 2022-12-13
> DOJ/SEC/CFTC enforcement triad. The row does not enumerate every FTX
> debtor or affiliated entity in the Delaware Chapter 11 cases; those
> entities are outside this DOJ-indictment trigger unit.

## 3. Changed-layer observations (supports the scoped claim)

*No observed_change entries. This is a `null_event`; see §4 for observed_no_change evidence supporting the null claim.*

## 4. No-change observations (where applicable)

### offramp_cex — `no_incremental_doj_attributable_offramp_change_after_preexisting_chapter_11_freeze`

**Window**: `2022-12-13 00:00:00+00:00` → `2022-12-27 23:59:59+00:00`

**Sources**:

- **`primary_legal`**
  - URL: <https://www.justice.gov/d9/press-releases/attachments/2022/12/13/u.s._v._bankman-fried_indictment_0.pdf>
  - body_hash: `sha256:78f9ce2e758d146f6d6f48a3d14dde095b7eb64c693b13adca9474f9409b4719`
  - body_path: `sources/http_captures/ftx-bankman-fried-doj-2022/primary/www.justice.gov__d9-press-releases-attachments-2022-12-13-u.s._v._bankman-fried_indictment_0.pdf__ad5b705de1.bin`
  > Official DOJ-hosted indictment anchor for the 2022-12-13 criminal
> trigger. It supports the federal enforcement date and target, not
> an incremental platform-access shutdown.
- **`primary_corporate`**
  - URL: <https://www.prnewswire.com/news-releases/ftx-receives-court-approval-for-first-day-motions-301685748.html>
  - body_hash: `sha256:00d80a76a9f51da40965a60afc9327f10f2f2bbd3375ee900b39a7582ebdf3d6`
  - body_path: `sources/http_captures/ftx-bankman-fried-doj-2022/primary/www.prnewswire.com__news-releases-ftx-receives-court-approval-for-first-day-motions-301685748.html__ebf96d93a3.html`
  > FTX-sourced first-day-motions release confirms that the Chapter
> 11 petitions were filed on 2022-11-11, about one month before the
> DOJ indictment. This anchors the null-control decision: the
> exchange/off-ramp freeze was already a bankruptcy-estate condition
> at the DOJ trigger date.
- **`primary_legal`**
  - URL: <https://www.sec.gov/newsroom/press-releases/2022-219>
  - body_hash: `sha256:4908c20f3da88e9cb492819dbe55fdfd731ccaa997491de955ef8de480a47276`
  - body_path: `sources/http_captures/ftx-bankman-fried-doj-2022/primary/www.sec.gov__newsroom-press-releases-2022-219__923a9a0e93.html`
  > Corroborates that the 2022-12-13 SEC filing was a parallel
> enforcement action, consistent with the sibling SEC null-control
> row and with this parent row's no-incremental-change coding.
- **`primary_legal`**
  - URL: <https://www.cftc.gov/PressRoom/PressReleases/8638-22>
  - body_hash: `sha256:0be01c582e41a2ffd9042074660125186626665220ff6128dc6c0d021317d220`
  - body_path: `sources/http_captures/ftx-bankman-fried-doj-2022/primary/www.cftc.gov__PressRoom-PressReleases-8638-22__5a31c2a5d9.html`
  > Corroborates that the 2022-12-13 CFTC filing was a parallel
> enforcement action and that FTX.com / Alameda conduct ran through
> the already-collapsed November 2022 platform state.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`sec-v-ftx-2022`](./sec-v-ftx-2022.md)
- [`cftc-v-ftx-2022`](./cftc-v-ftx-2022.md)
- [`blockfi-sec-lending-2022`](./blockfi-sec-lending-2022.md)
- [`celsius-bankruptcy-mashinsky-doj-2023`](./celsius-bankruptcy-mashinsky-doj-2023.md)
- [`voyager-bankruptcy-doj-objection-2023`](./voyager-bankruptcy-doj-objection-2023.md)
- [`japan-fsa-ftx-japan-suspension-2022-11`](./japan-fsa-ftx-japan-suspension-2022-11.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `c736a32`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

