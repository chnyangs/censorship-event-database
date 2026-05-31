# Evidence chain — `shrem-faiella-bitcoin-exchange-2014`

**Status**: `admitted` · **Stratum**: `S3_doj_sec_cftc_fiod` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `c7761c0` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-16` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "The 2014-01-27 DOJ SDNY indictment of BitInstant CEO Charlie Shrem and
> BTCKing operator Robert Faiella on money-laundering and unlicensed-money-
> transmitter counts produced an offramp_cex cascade (BitInstant ceased
> operations after Shrem's arrest and never resumed service following his
> 2014-09-04 guilty plea). The row claims only this single-layer offramp
> shutdown observation with attribution=plausible; no L0/L1/L3/L4/asset-
> onchain effects are coded."

## 1. Trigger

- **Type**: `doj_indictment`
- **Actor**: `US_DOJ_SDNY`
- **Timestamp**: `2014-01-27 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://www.justice.gov/usao-sdny/pr/manhattan-us-attorney-announces-charges-against-bitcoin-exchangers-including-ceo>
  - Wayback: <https://web.archive.org/web/20260516000000/https://www.justice.gov/usao-sdny/pr/manhattan-us-attorney-announces-charges-against-bitcoin-exchangers-including-ceo>
  > DOJ SDNY press release (2014-01-27): "Manhattan U.S. Attorney Announces
> Charges Against Bitcoin Exchangers, Including CEO Of Bitcoin Exchange
> Company." Criminal complaint unsealed in SDNY against Charles "Charlie"
> Shrem (then-CEO of BitInstant and vice-chair of the Bitcoin Foundation)
> and Robert M. Faiella (operating as "BTCKing" on Silk Road) charging
> conspiracy to commit money laundering (18 U.S.C. § 1956) and operating
> an unlicensed money transmitting business (18 U.S.C. § 1960). Shrem is
> further charged with willful failure to file a Suspicious Activity
> Report. Wayback URL pinned as a stub anchor for this DRYRUN row; a real
> release would replace with a verified snapshot timestamp + body_hash.
- **`primary_legal`**
  - URL: <https://www.justice.gov/usao-sdny/pr/bitcoin-exchangers-plead-guilty-manhattan-federal-court-connection-sale-approximately-1>
  - body_hash: `sha256:6162ec33c0cb6d353bf07bd86d04df88ba627da987833f21a9dbc0f375c2856a`
  - body_path: `sources/http_captures/shrem-faiella-bitcoin-exchange-2014/v0_3_repair/www.justice.gov__usao-sdny-pr-bitcoin-exchangers-plead-guilty-manhattan-federal-court-connection-sale-approximately-1__5c540d1fd5.html`
  > DOJ SDNY press release (2014-09-04): "Bitcoin Exchangers Plead Guilty In
> Manhattan Federal Court In Connection With Sale Of Approximately
> $1 Million In Bitcoins For Use On Silk Road." Records Shrem's and
> Faiella's guilty pleas; Shrem sentenced (2014-12) to two years
> imprisonment. Retained as contextual_unarchived corroborating pointer
> for the conviction phase; the 2014-01-27 indictment row above is the
> load-bearing trigger anchor.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Charlie Shrem (BitInstant) + Robert Faiella (BTCKing)
- **Chains**: `bitcoin`
- **Canonical domains**: `bitinstant.com`

> Two named individuals (Charles Shrem; Robert M. Faiella a/k/a "BTCKing")
> plus the corporate vehicle through which Shrem operated (BitInstant LLC).
> Faiella operated BTCKing as a Silk Road-facing Bitcoin vendor that
> sourced BTC inventory via BitInstant. No on-chain BTC addresses are
> enumerated at this event-row level; the SDNY complaint references
> transaction totals (~$1M in Bitcoin) without exhaustive address
> enumeration. canonical_domains lists the BitInstant frontend; BTCKing
> operated as a Silk Road vendor handle with no independent clearnet
> surface.

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `plausible` · Δt = 5280h

**Event label**: `bitinstant_ceases_operations_following_ceo_indictment`

**Timestamp**: `2014-09-04 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_legal`**
  - URL: <https://www.justice.gov/usao-sdny/pr/manhattan-us-attorney-announces-charges-against-bitcoin-exchangers-including-ceo>
  - Wayback: <https://web.archive.org/web/20260516000000/https://www.justice.gov/usao-sdny/pr/manhattan-us-attorney-announces-charges-against-bitcoin-exchangers-including-ceo>
  > DOJ SDNY criminal complaint against BitInstant CEO Charlie Shrem,
> charging conspiracy to commit money laundering and operating an
> unlicensed money transmitter (BitInstant). The indictment of the
> CEO together with the BitInstant-as-conduit narrative made
> continued operations infeasible; BitInstant did not resume service.
> attribution=plausible (not direct) because the DOJ press release
> names the criminal exposure but does not itself order a corporate
> shutdown; the platform wind-down is the downstream corporate
> consequence with strong temporal coincidence to the criminal
> process.
- **`primary_legal`**
  - URL: <https://www.justice.gov/usao-sdny/pr/bitcoin-exchangers-plead-guilty-manhattan-federal-court-connection-sale-approximately-1>
  - Wayback: <https://web.archive.org/web/20260516000000/https://www.justice.gov/usao-sdny/pr/bitcoin-exchangers-plead-guilty-manhattan-federal-court-connection-sale-approximately-1>
  - body_hash: `sha256:6162ec33c0cb6d353bf07bd86d04df88ba627da987833f21a9dbc0f375c2856a`
  - body_path: `sources/http_captures/shrem-faiella-bitcoin-exchange-2014/v0_3_repair/www.justice.gov__usao-sdny-pr-bitcoin-exchangers-plead-guilty-manhattan-federal-court-connection-sale-approximately-1__5c540d1fd5.html`
  > DOJ SDNY guilty-plea press release (2014-09-04) documenting Shrem's
> plea on the unlicensed-money-transmitter count. This conviction is
> the legally definitive end-state that made any BitInstant revival
> legally impossible (Shrem subsequently sentenced 2014-12 to two
> years). Used as the timestamp anchor for the observed_change row
> since the plea is the cleanest publicly-pinnable moment for the
> platform's terminal state. Wayback URL pinned as a stub anchor for
> this DRYRUN row.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`silk-road-doj-seizure-2013`](./silk-road-doj-seizure-2013.md)
- [`btc-e-doj-2017`](./btc-e-doj-2017.md)
- [`nydfs-bitlicense-2015-06`](./nydfs-bitlicense-2015-06.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `c7761c0`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

