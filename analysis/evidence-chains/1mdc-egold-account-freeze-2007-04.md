# Evidence chain — `1mdc-egold-account-freeze-2007-04`

**Status**: `admitted` · **Stratum**: `S3_doj_sec_cftc_fiod` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-05` · **Source commit**: `5fba5c6` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-31` · **Tool version**: `0.1.0` · **Generated**: `2026-06-05T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "As a knock-on of the 2007-04-27 e-gold federal indictment, a US court
> order forced e-gold to freeze/liquidate the ~$10-20M pool of e-gold
> accounts backing 1mdc (an e-gold-reserve-backed digital gold
> currency), rendering 1mdc insolvent and ending its service
> (offramp_cex), attribution=plausible. Discovery-period (pre-2013)
> tier; collateral to the e-gold takedown lineage."

## 1. Trigger

- **Type**: `doj_seizure_order`
- **Actor**: `US_DOJ_DC`
- **Timestamp**: `2007-04-27 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://www.justice.gov/archive/criminal/cybercrime/press-releases/2007/egoldIndict.htm>
  - Wayback: <https://web.archive.org/web/20210401004405/https://www.justice.gov/archive/criminal/cybercrime/press-releases/2007/egoldIndict.htm>
  - body_hash: `sha256:61540013bbabcf9330f52f862e9b625f96a821af3ffd882c40631ee17815dd50`
  - body_path: `sources/http_captures/1mdc-egold-account-freeze-2007-04/primary/web.archive.org__web-20210401004405-https-www.justice.gov-archive-criminal-cybercrime-press-releases-2007-egoldIndict.htm__9c96372596.html`
  > DOJ press release (2007-04-27, unsealed): "Digital Currency
> Business E-Gold Indicted For Money Laundering And Illegal Money
> Transmitting." A federal grand jury in the District of Columbia
> indicted e-gold Ltd., Gold & Silver Reserve Inc. and their
> principals; the action precipitated court-mandated restrictions
> on e-gold's operations including the freeze/liquidation of e-gold
> accounts. This is the operative federal state instrument behind
> the collateral freeze of the 1mdc-backing e-gold accounts.
> Wayback 20210401004405 pinned. (This page indicts e-gold; it does
> not itself name 1mdc — the 1mdc-specific freeze is carried by the
> secondary source below.)
- **`supporting_journalism`**
  - URL: <https://en.wikipedia.org/wiki/1mdc>
  - Wayback: <https://web.archive.org/web/20251129151946/https://en.wikipedia.org/wiki/1mdc>
  - body_hash: `sha256:688c3732c0bfff067b7f2cfd6ae537748d47fa42a4880c6d9bd31e9847cf7fca`
  - body_path: `sources/http_captures/1mdc-egold-account-freeze-2007-04/primary/web.archive.org__web-20251129000000-https-en.wikipedia.org-wiki-1mdc__7048e5fe3c.html`
  > Encyclopedic secondary source for the 1mdc-specific effect: "As
> of April 27, 2007, a US court order has forced e-gold to
> liquidate a large number of e-gold accounts totalling some 10 to
> 20 million US dollars' worth of gold." A part of this seizure was
> 1mdc's accounts and assets; "Once e-gold Ltd. was instructed by
> the US government to freeze and liquidate all 1mdc accounts, 1mdc
> became insolvent by default." 1mdc was a digital gold currency
> (2001-2007) whose units were backed by reserves of e-gold rather
> than physical bullion. Wayback 20251129151946 pinned.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: 1mdc (e-gold-backed digital gold currency)

> 1mdc (a digital gold currency, 2001-2007, whose units were backed by
> reserves held in e-gold accounts rather than physical bullion) and
> the pool of e-gold accounts that backed it. Marked subset: targets
> the 1mdc-backing e-gold reserve accounts collaterally frozen/
> liquidated under the 2007-04-27 court order, not an enumerated set of
> individual 1mdc holders. No blockchain / on-chain addresses (1mdc
> units were off-ledger entries backed by the centralized e-gold
> ledger).

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `plausible` · Δt = 0h

**Event label**: `court_order_froze_and_liquidated_1mdc_backing_egold_accounts_ending_service`

**Timestamp**: `2007-04-27 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`supporting_journalism`**
  - URL: <https://en.wikipedia.org/wiki/1mdc>
  - Wayback: <https://web.archive.org/web/20251129151946/https://en.wikipedia.org/wiki/1mdc>
  - body_hash: `sha256:688c3732c0bfff067b7f2cfd6ae537748d47fa42a4880c6d9bd31e9847cf7fca`
  - body_path: `sources/http_captures/1mdc-egold-account-freeze-2007-04/primary/web.archive.org__web-20251129000000-https-en.wikipedia.org-wiki-1mdc__7048e5fe3c.html`
  > "As of April 27, 2007, a US court order has forced e-gold to
> liquidate a large number of e-gold accounts totalling some 10
> to 20 million US dollars' worth of gold." A part of this
> seizure was 1mdc's accounts; the forced freeze/liquidation of
> all 1mdc accounts rendered 1mdc insolvent and ended its
> service. attribution=plausible: the operative state instrument
> is the federal e-gold court order, and the 1mdc-specific freeze
> effect is documented via this encyclopedic secondary source
> (no 1mdc-naming primary legal text captured).
- **`primary_legal`**
  - URL: <https://www.justice.gov/archive/criminal/cybercrime/press-releases/2007/egoldIndict.htm>
  - Wayback: <https://web.archive.org/web/20210401004405/https://www.justice.gov/archive/criminal/cybercrime/press-releases/2007/egoldIndict.htm>
  - body_hash: `sha256:61540013bbabcf9330f52f862e9b625f96a821af3ffd882c40631ee17815dd50`
  - body_path: `sources/http_captures/1mdc-egold-account-freeze-2007-04/primary/web.archive.org__web-20210401004405-https-www.justice.gov-archive-criminal-cybercrime-press-releases-2007-egoldIndict.htm__9c96372596.html`
  > DOJ 2007-04-27 e-gold indictment release ("Digital Currency
> Business E-Gold Indicted For Money Laundering And Illegal Money
> Transmitting"): the federal D.D.C. action that precipitated the
> court-mandated freeze/liquidation of e-gold accounts (the pool
> that included the 1mdc-backing reserves). Primary-legal anchor
> for the operative state instrument.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`egold-doj-guilty-plea-2008-07`](./egold-doj-guilty-plea-2008-07.md)
- `goldage-ny-state-indictment-2006-07` (rejected; no rendered admitted-chain link)
- [`liberty-reserve-coordinated-takedown-2013-05`](./liberty-reserve-coordinated-takedown-2013-05.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `5fba5c6`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

