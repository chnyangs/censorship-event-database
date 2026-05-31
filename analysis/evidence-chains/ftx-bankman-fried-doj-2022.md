# Evidence chain — `ftx-bankman-fried-doj-2022`

**Status**: `admitted` · **Stratum**: `S3_doj_sec_cftc_fiod` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `71b6d3d` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-16` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "The 2022-12-13 coordinated US DOJ SDNY + SEC + CFTC enforcement action
> against Samuel Bankman-Fried, FTX Trading Ltd., and Alameda Research LLC,
> cascading on top of the 2022-11-11 FTX Chapter 11 bankruptcy filing,
> produced a one-layer admitted observation in the dataset: an offramp_cex
> global withdraw-pause and Chapter 11 customer-asset freeze affecting
> FTX.com international, FTX.US, and Alameda Research assets. Attribution
> is plausible (not direct) to the 2022-12-13 federal trigger because the
> off-ramp shutdown was proximately effected by the prior corporate
> Chapter 11 filing. The row does not claim L0 network, L1 consensus, L3
> RPC, asset_onchain, or admission-grade L4 frontend effects; the FTX.com
> US-user geofencing well predates the trigger and is not coded as an
> attributable observation."

## 1. Trigger

- **Type**: `doj_indictment`
- **Actor**: `US_DOJ_SDNY`
- **Timestamp**: `2022-12-13 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://www.justice.gov/usao-sdny/pr/united-states-attorney-announces-charges-against-ftx-founder-samuel-bankman-fried>
  - Wayback: <https://web.archive.org/web/2022/https://www.justice.gov/usao-sdny/pr/united-states-attorney-announces-charges-against-ftx-founder-samuel-bankman-fried>
  > DOJ SDNY press release (2022-12-13): "United States Attorney Announces
> Charges Against FTX Founder Samuel Bankman-Fried." Indictment was filed
> 2022-12-09 and unsealed 2022-12-13. Eight-count indictment charging
> Bankman-Fried with wire fraud, wire fraud conspiracy, securities fraud,
> securities fraud conspiracy, money laundering conspiracy, and
> conspiracy to defraud the United States and violate campaign finance
> laws. Marked evidence_use=contextual_unarchived because in this DRYRUN
> the authoring LLM agent did not personally pin a Wayback snapshot
> timestamp or compute a body_hash; the DOJ press-release URL slug is
> stable and routinely captured by Wayback in 2022-2023 and remains the
> canonical SDNY anchor for the criminal-side trigger. Pinned snapshot
> timestamp + body_hash to be re-anchored during human audit before this
> citation may serve as an admission anchor in its own right.
- **`primary_legal`**
  - URL: <https://www.sec.gov/news/press-release/2022-219>
  - Wayback: <https://web.archive.org/web/2022/https://www.sec.gov/news/press-release/2022-219>
  > SEC press release 2022-219 (2022-12-13): "SEC Charges Samuel
> Bankman-Fried with Defrauding Investors in Crypto Asset Trading
> Platform FTX." Same-day civil complaint filed in SDNY alleging
> Bankman-Fried orchestrated a multi-year scheme to defraud FTX equity
> investors of more than $1.8B while diverting customer funds to Alameda
> Research. Companion civil action to the DOJ criminal indictment;
> documents the SEC side of the coordinated multi-agency action.
> Wayback wildcard pointer in lieu of pinned-timestamp snapshot;
> evidence_use=contextual_unarchived pending human-audit re-pin.
- **`primary_legal`**
  - URL: <https://www.cftc.gov/PressRoom/PressReleases/8638-22>
  - Wayback: <https://web.archive.org/web/2022/https://www.cftc.gov/PressRoom/PressReleases/8638-22>
  > CFTC press release 8638-22 (2022-12-13): "CFTC Charges Sam
> Bankman-Fried, FTX Trading and Alameda with Fraud and Material
> Misrepresentations." Same-day civil enforcement action in SDNY
> charging Bankman-Fried, FTX Trading Ltd. (the operator of FTX.com),
> and Alameda Research LLC with fraud and material misrepresentations
> in connection with the sale of digital-asset commodities in interstate
> commerce. Third pillar of the 2022-12-13 coordinated DOJ + SEC + CFTC
> action. Wayback wildcard pointer in lieu of pinned-timestamp snapshot;
> evidence_use=contextual_unarchived pending human-audit re-pin.
- **`primary_corporate`**
  - URL: <https://www.ftx.com/en/press-releases/ftx-trading-ltd-voluntary-chapter-11-cases>
  - Wayback: <https://web.archive.org/web/2022/https://www.ftx.com/en/press-releases/ftx-trading-ltd-voluntary-chapter-11-cases>
  > FTX Trading Ltd. corporate announcement of voluntary Chapter 11
> bankruptcy filing (2022-11-11), filed in the District of Delaware
> (Case No. 22-11068). Predates the 2022-12-13 DOJ/SEC/CFTC trigger by
> approximately one month and is the proximate corporate instrument
> that implemented the global withdraw-pause and customer-asset freeze
> on the FTX.com offramp_cex layer. Retained here as the corporate-side
> primary citation that anchors the offramp_cex observation; the
> 2022-12-13 federal enforcement actions are the criminal/civil
> accountability layer on top of an already-bankrupt platform.
> Wayback wildcard pointer in lieu of pinned-timestamp snapshot;
> evidence_use=contextual_unarchived pending human-audit re-pin.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Samuel Bankman-Fried / FTX Trading Ltd. / Alameda Research LLC
- **Canonical domains**: `ftx.com`, `ftx.us`

> Samuel Bankman-Fried (individual defendant in the DOJ criminal indictment,
> SEC civil complaint, and CFTC civil enforcement action) + FTX Trading Ltd.
> (operator of the FTX.com international exchange, named in the SEC and
> CFTC civil complaints) + Alameda Research LLC (named in the CFTC civil
> complaint as the co-conspirator trading firm). The target slice does not
> enumerate the dozens of additional FTX-affiliated entities listed in the
> Delaware Chapter 11 schedules; the load-bearing entities for the
> offramp_cex observation are FTX.com (international) and FTX US
> (US-customer offramp), both administratively frozen at the 2022-11-11
> bankruptcy filing. The criminal-defendant individual (Bankman-Fried) was
> convicted on 2023-11-02 on seven of the eight counts in the superseding
> indictment and sentenced 2024-03-28; that disposition is downstream of
> this row's trigger and not coded as a separate observation here.

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `plausible` · Δt = 0h

**Event label**: `global_withdraw_pause_and_chapter_11_customer_asset_freeze`

**Timestamp**: `2022-12-13 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_corporate`**
  - URL: <https://www.ftx.com/en/press-releases/ftx-trading-ltd-voluntary-chapter-11-cases>
  - Wayback: <https://web.archive.org/web/2022/https://www.ftx.com/en/press-releases/ftx-trading-ltd-voluntary-chapter-11-cases>
  > FTX Trading Ltd. corporate Chapter 11 filing announcement
> (2022-11-11) is the proximate corporate instrument that froze
> customer-asset withdrawals globally across the FTX.com and FTX.US
> platforms. attribution=plausible (not direct) to the 2022-12-13
> DOJ/SEC/CFTC trigger because the offramp shutdown was effected by
> the prior bankruptcy filing; the federal enforcement actions are
> the criminal/civil accountability cascade on top of an
> already-frozen offramp. Wayback wildcard pointer in lieu of
> pinned-timestamp snapshot; evidence_use=contextual_unarchived
> pending human-audit re-pin.
- **`primary_legal`**
  - URL: <https://www.sec.gov/news/press-release/2022-219>
  - Wayback: <https://web.archive.org/web/2022/https://www.sec.gov/news/press-release/2022-219>
  > SEC press release 2022-219 documents that customer funds were
> diverted from FTX to Alameda Research, anchoring the offramp_cex
> observation that customer-asset withdrawals on the FTX.com and
> FTX.US platforms were administratively suspended through the
> bankruptcy proceedings and the federal enforcement cascade.
> Wayback wildcard pointer; evidence_use=contextual_unarchived
> pending human-audit re-pin.
- **`primary_legal`**
  - URL: <https://www.cftc.gov/PressRoom/PressReleases/8638-22>
  - Wayback: <https://web.archive.org/web/2022/https://www.cftc.gov/PressRoom/PressReleases/8638-22>
  > CFTC press release 8638-22 anchors the Alameda Research asset
> freeze pillar of the offramp_cex observation. CFTC complaint
> names FTX Trading Ltd. and Alameda Research LLC alongside
> Bankman-Fried; the Alameda asset freeze is part of the same
> Chapter 11 estate cascading from the 2022-11-11 bankruptcy.
> Wayback wildcard pointer; evidence_use=contextual_unarchived
> pending human-audit re-pin.

## 5. Honest coverage gaps

- **l4_frontend** (`not_measured`): No admission-grade historical frontend diff for ftx.com / ftx.us is

## 7. Related events

- [`blockfi-sec-lending-2022`](./blockfi-sec-lending-2022.md)
- [`binance-4framework-2023`](./binance-4framework-2023.md)
- [`sec-v-coinbase-2023`](./sec-v-coinbase-2023.md)
- [`kraken-sec-staking-2023`](./kraken-sec-staking-2023.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `71b6d3d`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

