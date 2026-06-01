# Evidence chain — `salame-ftx-campaign-finance-doj-2023`

**Status**: `admitted` · **Stratum**: `S3_doj_sec_cftc_fiod` · **Shape**: `null_event` (0 changed layer(s): none) · **Tier**: `null_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `4b6ca9a` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-20` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T01:54:35Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "The 2023-09-07 DOJ SDNY guilty plea by Ryan Salame (former co-CEO,
> FTX Digital Markets) to campaign-finance and unlicensed
> money-transmitting conspiracies — a downstream individual-defendant
> accountability action in the FTX-collapse enforcement cascade —
> produces zero observed_change layers in the cross-layer
> censorship-substrate frame. The row is retained as a null_case
> denominator control in the S3 us-federal-enforcement cluster; the
> load-bearing offramp_cex shutdown is coded on the parent
> ftx-bankman-fried-doj-2022 row at the 2022-11-11 Chapter 11 +
> 2022-12-13 federal-enforcement trigger, ~9 months prior."

## 1. Trigger

- **Type**: `doj_indictment`
- **Actor**: `US_DOJ_SDNY`
- **Timestamp**: `2023-09-07 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://www.justice.gov/usao-sdny/pr/statement-us-attorney-damian-williams-guilty-plea-ryan-salame-former-ceo-ftx>
  - Wayback: <https://web.archive.org/web/2023/https://www.justice.gov/usao-sdny/pr/statement-us-attorney-damian-williams-guilty-plea-ryan-salame-former-ceo-ftx>
  > DOJ SDNY press release (2023-09-07): "Statement Of U.S. Attorney
> Damian Williams On The Guilty Plea Of Ryan Salame, Former CEO Of
> FTX." Salame, former co-CEO of FTX Digital Markets (the Bahamas
> FTX entity), pled guilty before Judge Lewis Kaplan to a two-count
> information charging (1) conspiracy to make unlawful political
> contributions and defraud the Federal Election Commission, and
> (2) conspiracy to operate an unlicensed money transmitting
> business. Salame admitted that from fall 2021 to November 2022
> he made tens of millions of dollars of political contributions
> in his own name that were in fact funded by Alameda Research,
> with Bankman-Fried's support. Plea agreement included forfeiture
> of approximately $1.5B and restitution of more than $5.5M to FTX
> debtors. DRYRUN contextual_unarchived stub; the URL slug is
> stable on justice.gov and routinely captured by Wayback, but the
> authoring LLM agent did not personally pin a snapshot timestamp
> or compute a body_hash. Real release must replace with a pinned
> Wayback timestamp + body_hash during human audit.
- **`primary_legal`**
  - URL: <https://content.govdelivery.com/attachments/USDOJUSAO/2023/09/07/file_attachments/2607934/U.S.%20v.%20Salame%20Information.pdf>
  - Wayback: <https://web.archive.org/web/2023/https://content.govdelivery.com/attachments/USDOJUSAO/2023/09/07/file_attachments/2607934/U.S.%20v.%20Salame%20Information.pdf>
  > Charging Information (U.S. v. Salame), filed SDNY 2023-09-07,
> distributed via DOJ govdelivery PDF attachment. Two-count
> information that Salame pled guilty to the same day. DRYRUN
> contextual_unarchived stub; replace with a pinned Wayback /
> body_hash anchor during real human audit.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Ryan Salame

> Ryan Salame (individual defendant — former co-CEO of FTX Digital
> Markets, the Bahamas FTX entity). The plea is a downstream
> individual-accountability action in the FTX-collapse enforcement
> cascade, with the corporate-entity defendants (FTX Trading Ltd.,
> Alameda Research LLC) and the lead individual defendant
> (Bankman-Fried) addressed in the parent ftx-bankman-fried-doj-2022,
> sec-v-ftx-2022, and cftc-v-ftx-2022 rows. The plea names Alameda
> Research as the source of the unlawfully-funneled political
> contributions but Alameda is not coded as a target here; it is the
> funding-source entity within Salame's admitted conduct rather than
> a defendant on this charging instrument. Class-level rationale per
> codebook §7: subset (not complete) because the broader FTX-collapse
> individual-defendant cluster (Caroline Ellison, Gary Wang, Nishad
> Singh) is not enumerated here even though those individuals also
> pled guilty in the SDNY FTX cases on separate dockets.

## 3. Changed-layer observations (supports the scoped claim)

*No observed_change entries. This is a `null_event`; see §4 for observed_no_change evidence supporting the null claim.*

## 4. No-change observations (where applicable)

### offramp_cex — `no_incremental_offramp_change_from_downstream_salame_guilty_plea`

**Window**: `2023-09-07 00:00:00+00:00` → `2023-09-30 23:59:59+00:00`

**Sources**:

- **`primary_legal`**
  - URL: <https://www.justice.gov/usao-sdny/pr/statement-us-attorney-damian-williams-guilty-plea-ryan-salame-former-ceo-ftx>
  - body_hash: `sha256:2cf716cef8f7b2649cc8cc7e4ae1c882619214b11a88a55dd067ec6e710862c0`
  - body_path: `sources/http_captures/salame-ftx-campaign-finance-doj-2023/v0_3_primary_repair/www.justice.gov__usao-sdny-pr-statement-us-attorney-damian-williams-guilty-plea-ryan-salame-former-ceo-ftx__a4f6faa1da.html`
  > DOJ's own plea announcement anchors this as a downstream
> individual-defendant accountability action. The row-local
> observation is observed_no_change: the Salame plea does not
> itself document a new exchange/off-ramp operational restriction
> beyond the FTX bankruptcy/off-ramp freeze captured in the parent
> row. Live justice.gov capture (v0_3_primary_repair) pre-pinned
> 2026-05-17.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`ftx-bankman-fried-doj-2022`](./ftx-bankman-fried-doj-2022.md)
- [`sec-v-ftx-2022`](./sec-v-ftx-2022.md)
- [`cftc-v-ftx-2022`](./cftc-v-ftx-2022.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `4b6ca9a`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

