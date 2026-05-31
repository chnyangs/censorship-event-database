# Evidence chain — `sec-voorhees-satoshidice-2014`

**Status**: `admitted` · **Stratum**: `S3_doj_sec_cftc_fiod` · **Shape**: `comparison` (2 changed layer(s): `l4_frontend`, `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `661a63f` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-16` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "The 2014-06-03 SEC settlement with Erik Voorhees (SatoshiDICE +
> FeedZeBirds unregistered Bitcoin-denominated securities offerings) is
> the earliest SEC enforcement in the dataset directly tied to a
> Bitcoin-denominated equity offering. The row claims only the
> operator-level offering shutdown (offramp_cex, direct) and the
> pre-codified US-user frontend geofence / Voorhees operator divestment
> (l4_frontend, plausible); no L0/L1/L3/asset-onchain effects are
> claimed."

## 1. Trigger

- **Type**: `sec_action`
- **Actor**: `US_SEC`
- **Timestamp**: `2014-06-03 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://www.sec.gov/news/press-release/2014-111>
  - Wayback: <https://web.archive.org/web/20170509181147/https://www.sec.gov/news/press-release/2014-111>
  > SEC Press Release 2014-111 (2014-06-03): "SEC Charges Bitcoin
> Entrepreneur With Offering Unregistered Securities." Erik T. Voorhees
> agreed to pay $50,000 in disgorgement plus civil penalty to settle SEC
> charges that he publicly offered shares in two Bitcoin-denominated
> ventures — SatoshiDICE (an online gambling site) and FeedZeBirds
> (a service paying Bitcoin to Twitter users who forwarded sponsored
> tweets) — without registering the offerings under the Securities
> Act. First SEC settlement directly tied to a Bitcoin-denominated
> securities offering. Wayback memento 2017-05-09 is the nearest
> replayable capture of the canonical press-release URL anchored in
> this DRYRUN authoring pass; no body_hash was independently captured.
- **`primary_legal`**
  - URL: <https://www.sec.gov/litigation/admin/2014/33-9592.pdf>
  - Wayback: <https://web.archive.org/web/20140611091119/http://www.sec.gov/litigation/admin/2014/33-9592.pdf>
  > SEC Order Instituting Cease-and-Desist Proceedings, Release
> No. 33-9592 (2014-06-03), In the Matter of Erik T. Voorhees.
> Administrative-law-judge order detailing the SatoshiDICE share
> offering (May 2012 – Aug 2012, ~50,600 BTC raised) and the
> FeedZeBirds share offering (Aug 2012 – Apr 2013), both deemed
> unregistered securities under §5 of the Securities Act of 1933.
> Settlement: disgorgement of $15,843.98 plus $1,776.06 prejudgment
> interest plus $35,000 civil penalty (~$50,000 total). Two-year
> bar on participating in unregistered securities issuance.
> Wayback memento 2014-06-11 (8 days post-event) is the load-bearing
> archive anchor; no body_hash was independently captured in this
> DRYRUN pass.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Erik T. Voorhees / SatoshiDICE / FeedZeBirds
- **Chains**: `bitcoin`
- **Canonical domains**: `satoshidice.com`, `feedzebirds.com`

> Erik T. Voorhees as the operator/issuer of two Bitcoin-denominated
> securities offerings: (a) SatoshiDICE shares (S.DICE), the operator-
> equity instrument of the SatoshiDICE Bitcoin gambling site previously
> accessible at satoshidice.com, and (b) FeedZeBirds shares. The SEC
> action is personal to Voorhees as issuer; SatoshiDICE the operating
> site was the load-bearing real-world surface (its US-IP blocking and
> operator-status change anchor the observable censorship effect).

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `direct` · Δt = 0h

**Event label**: `us_unregistered_securities_offering_ceased_via_sec_settlement`

**Timestamp**: `2014-06-03 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_legal`**
  - URL: <https://www.sec.gov/news/press-release/2014-111>
  - Wayback: <https://web.archive.org/web/20170509181147/https://www.sec.gov/news/press-release/2014-111>
  > SEC press release names the settlement and the cessation of the
> unregistered SatoshiDICE / FeedZeBirds Bitcoin-denominated
> securities offerings. attribution=direct because the SEC source
> itself names Voorhees as issuer and quantifies the offering
> shutdown. Wayback memento 2017-05-09 is the nearest replayable
> anchor for the canonical press-release URL pinned in this
> DRYRUN pass; body_hash deferred.
- **`primary_legal`**
  - URL: <https://www.sec.gov/litigation/admin/2014/33-9592.pdf>
  - Wayback: <https://web.archive.org/web/20140611091119/http://www.sec.gov/litigation/admin/2014/33-9592.pdf>
  > SEC administrative order Release No. 33-9592 — the operative
> legal instrument codifying cessation, disgorgement, and the
> two-year unregistered-issuance bar. Wayback memento 2014-06-11
> (8 days post-event) is the load-bearing archive anchor in this
> DRYRUN pass; body_hash deferred.

### l4_frontend · attribution: `plausible` · Δt = 0h

**Event label**: `satoshidice_us_user_geofence_and_voorhees_divestment_codified_by_sec_settlement`

**Timestamp**: `2014-06-03 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_legal`**
  - URL: <https://www.sec.gov/litigation/admin/2014/33-9592.pdf>
  - Wayback: <https://web.archive.org/web/20140611091119/http://www.sec.gov/litigation/admin/2014/33-9592.pdf>
  > The SEC administrative order documents that SatoshiDICE blocked
> US-IP access in mid-2013 and that Voorhees divested operator
> interest in July 2013, prior to the 2014-06-03 settlement that
> formally codified the US-investor offering withdrawal at the
> issuer level. attribution=plausible because the L4 frontend
> surface change predates the trigger; the SEC order is the
> load-bearing primary-legal source naming the surface change.
> Wayback memento 2014-06-11 is the load-bearing replayable
> anchor.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`nydfs-bitlicense-2015-06`](./nydfs-bitlicense-2015-06.md)
- [`silk-road-doj-seizure-2013`](./silk-road-doj-seizure-2013.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `661a63f`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

