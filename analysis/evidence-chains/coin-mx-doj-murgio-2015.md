# Evidence chain — `coin-mx-doj-murgio-2015`

**Status**: `admitted` · **Stratum**: `S3_doj_sec_cftc_fiod` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `143c3a7` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-20` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T12:56:36Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> The 2015-07-21 DOJ SDNY indictment of Anthony R. Murgio and
> Yuri Lebedev for operating Coin.mx as an unlicensed bitcoin
> exchange (with HOPE Federal Credit Union captured as a banking
> conduit and a phony "Collectors Club" front company) produced
> an offramp_cex cascade: Coin.mx shut down post-arrest and the
> USD-rails conduit through HOPE FCU was severed. The row claims
> only this single-layer offramp shutdown observation with
> attribution=direct; no L0/L1/L3/L4/asset-onchain effects are
> coded.

## 1. Trigger

- **Type**: `doj_indictment`
- **Actor**: `US_DOJ_SDNY`
- **Timestamp**: `2015-07-21 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://www.justice.gov/usao-sdny/pr/manhattan-us-attorney-announces-charges-against-two-florida-men-operating-underground>
  - Wayback: <https://web.archive.org/web/20150725142739/https://www.justice.gov/usao-sdny/pr/manhattan-us-attorney-announces-charges-against-two-florida-men-operating-underground>
  - body_hash: `sha256:f7479ed2097ce55639b8d506a5c1ad9fee67a9e6fb1f3489d1fed9ec9411b750`
  - body_path: `sources/http_captures/coin-mx-doj-murgio-2015/primary/web.archive.org__web-20150725142739-https-www.justice.gov-usao-sdny-pr-manhattan-us-attorney-announces-charges-against-two-florida-men-operating-underground__f04043f73f.html`
  > DOJ SDNY press release (2015-07-21): "Manhattan U.S. Attorney
> Announces Charges Against Two Florida Men For Operating An
> Underground Bitcoin Exchange." Criminal complaint unsealed in
> SDNY against Anthony R. Murgio and Yuri Lebedev for operating
> Coin.mx, an unlawful internet-based Bitcoin exchange, in
> violation of federal anti-money-laundering laws (18 U.S.C.
> Sec. 1960 - operating an unlicensed money transmitting
> business). Between approximately October 2013 and January
> 2015, Coin.mx exchanged at least $1.8 million for Bitcoins
> on behalf of tens of thousands of customers. To evade
> scrutiny from financial institutions, in 2014 Murgio and his
> co-conspirators gained control of HOPE Federal Credit Union
> (HOPE FCU), a small New Jersey federal credit union with
> primarily low-income members, after paying more than $150,000
> in bribes. Wayback URL pinned as a wildcard 2015 anchor;
> evidence_use=contextual_unarchived because no body_hash has
> been independently captured in this DRYRUN authoring pass.
- **`primary_legal`**
  - URL: <https://www.justice.gov/usao-sdny/pr/operator-unlawful-bitcoin-exchange-pleads-guilty-multimillion-dollar-money-laundering>
  - Wayback: <https://web.archive.org/web/20170329203707/https://www.justice.gov/usao-sdny/pr/operator-unlawful-bitcoin-exchange-pleads-guilty-multimillion-dollar-money-laundering>
  - body_hash: `sha256:a19d2017ad35b2f12785ac090514862b32e1ffe576c43c32ba734e05550ff47d`
  - body_path: `sources/http_captures/coin-mx-doj-murgio-2015/primary/web.archive.org__web-20170329203707-https-www.justice.gov-usao-sdny-pr-operator-unlawful-bitcoin-exchange-pleads-guilty-multimillion-dollar-money-laundering__60279e0cd1.html`
  > DOJ SDNY press release (2017-01): "Operator Of Unlawful
> Bitcoin Exchange Pleads Guilty In Multimillion-Dollar Money
> Laundering And Fraud Scheme." Records Murgio's guilty plea
> to (1) conspiracy to operate an unlicensed money transmitting
> business, (2) conspiracy to commit bank fraud, and (3)
> conspiracy to obstruct an examination of a financial
> institution. Retained as contextual_unarchived corroborating
> pointer for the conviction phase.
- **`primary_legal`**
  - URL: <https://www.justice.gov/usao-sdny/pr/operator-unlawful-bitcoin-exchange-sentenced-more-5-years-prison-leading-multimillion>
  - Wayback: <https://web.archive.org/web/20170628201601/https://www.justice.gov/usao-sdny/pr/operator-unlawful-bitcoin-exchange-sentenced-more-5-years-prison-leading-multimillion>
  - body_hash: `sha256:7b866d8e7e250f45348dbebda12c6b6e17a39eff340f2ba3f95de1623df2cb7d`
  - body_path: `sources/http_captures/coin-mx-doj-murgio-2015/primary/web.archive.org__web-20170628201601-https-www.justice.gov-usao-sdny-pr-operator-unlawful-bitcoin-exchange-sentenced-more-5-years-prison-leading-multimillion__f3a64c1893.html`
  > DOJ SDNY press release: "Operator Of Unlawful Bitcoin Exchange
> Sentenced To More Than 5 Years In Prison For Leading
> Multimillion-Dollar Money Laundering And Fraud Scheme."
> Murgio sentenced to 66 months imprisonment. Retained as
> contextual_unarchived corroborating pointer for the
> sentencing phase.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Coin.mx
- **Chains**: `bitcoin`
- **Canonical domains**: `coin.mx`

> Named individual defendants Anthony R. Murgio and Yuri Lebedev
> operating the Coin.mx unlicensed bitcoin exchange, with HOPE
> Federal Credit Union (HOPE FCU) used as a captured banking
> conduit and a phony "Collectors Club" front company used to
> disguise USD rails. canonical_domains lists the Coin.mx
> operating domain; no on-chain BTC addresses are enumerated at
> this event-row level (the SDNY complaint cites aggregate volume
> ~$1.8M without exhaustive address enumeration).

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `direct` · Δt = 0h

**Event label**: `coin_mx_ceases_operations_and_hope_fcu_usd_rails_severed_following_indictment`

**Timestamp**: `2015-07-21 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_legal`**
  - URL: <https://www.justice.gov/usao-sdny/pr/manhattan-us-attorney-announces-charges-against-two-florida-men-operating-underground>
  - Wayback: <https://web.archive.org/web/2015/https://www.justice.gov/usao-sdny/pr/manhattan-us-attorney-announces-charges-against-two-florida-men-operating-underground>
  > DOJ SDNY press release announcing the 2015-07-21
> criminal complaint against Anthony R. Murgio and Yuri
> Lebedev for operating Coin.mx as an unlicensed money
> transmitting business in violation of 18 U.S.C. Sec. 1960.
> The complaint also charges bank fraud and obstruction of
> a financial institution examination tied to Murgio's
> capture of HOPE Federal Credit Union as a banking conduit
> for Coin.mx USD flows. attribution=direct: the indictment
> named Coin.mx by name and the USD rails through HOPE FCU
> were directly severed as a consequence of unsealing
> (rather than as a downstream business decision distinct
> from the legal action). The exchange did not resume
> operations after the arrests.
- **`primary_legal`**
  - URL: <https://www.justice.gov/usao-sdny/pr/operator-unlawful-bitcoin-exchange-pleads-guilty-multimillion-dollar-money-laundering>
  - Wayback: <https://web.archive.org/web/2017/https://www.justice.gov/usao-sdny/pr/operator-unlawful-bitcoin-exchange-pleads-guilty-multimillion-dollar-money-laundering>
  > DOJ SDNY guilty-plea press release documenting Murgio's
> plea to conspiracy to operate an unlicensed money
> transmitting business, conspiracy to commit bank fraud,
> and conspiracy to obstruct an examination of a financial
> institution. This conviction is the legally definitive
> end-state confirming Coin.mx's terminal shutdown. Used
> as the secondary corroborating anchor for the offramp_cex
> observation.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`shrem-faiella-bitcoin-exchange-2014`](./shrem-faiella-bitcoin-exchange-2014.md)
- [`ripple-fincen-xrp-2015`](./ripple-fincen-xrp-2015.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `143c3a7`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

