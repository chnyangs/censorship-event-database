# Evidence chain — `powell-unlicensed-bitcoin-exchange-2014`

**Status**: `admitted` · **Stratum**: `S3_doj_sec_cftc_fiod` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `71b6d3d` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-16` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "The 2014-12-04 USDC CDIL sentencing of John D. Powell (48 months for
> two counts of 18 U.S.C. § 1960 operating an unlicensed money service
> business) terminated Powell's individual cash-for-bitcoin MSB off-ramp
> activity, recorded here as a single observed_change at offramp_cex
> with attribution=direct. The row claims only this single-layer
> individual-operator shutdown observation; no L0/L1/L3/L4/asset-onchain
> effects are coded because Powell operated without a named corporate
> vehicle, clearnet domain, or platform footprint identifiable from the
> DOJ trigger artifact."

## 1. Trigger

- **Type**: `doj_indictment`
- **Actor**: `US_DOJ_CDIL`
- **Timestamp**: `2014-12-04 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://www.justice.gov/usao-cdil/pr/mclean-county-man-serve-four-years-prisonfor-operating-unlicensed-internet-bitcoin>
  - Wayback: <https://web.archive.org/web/20141210000000/https://www.justice.gov/usao-cdil/pr/mclean-county-man-serve-four-years-prisonfor-operating-unlicensed-internet-bitcoin>
  - body_hash: `sha256:b78a3318ac70cd09fe1a0b1ba5458d7c2ba6ba8a10892b337724d1b3f2b7cef1`
  - body_path: `sources/http_captures/powell-unlicensed-bitcoin-exchange-2014/primary/www.justice.gov__usao-cdil-pr-mclean-county-man__wayback_20141210__primary.html`
  > DOJ USAO-CDIL press release (dated 2014-12-09, content="2014-12-09T00:00:00-05:00"
> in archived page metadata): "Mclean County Man To Serve Four Years In Prison
> for Operating Unlicensed Internet Bitcoin Exchange." Announces the 2014-12-04
> sentencing of John D. Powell, 55, of Normal, Ill., to 48 months in federal
> prison + 3 years supervised release by Chief U.S. District Judge James E.
> Shadid (USDC CDIL, Peoria). Powell entered an open plea of guilty on
> 2014-07-31 to **two counts of operating an unlicensed money service business**
> (18 U.S.C. § 1960). Investigators received more than $3 million from
> individuals during an 18-month period ending February 2014 by exchanging
> cash for bitcoin. Investigation: IRS Criminal Investigation + U.S. Postal
> Inspection Service; prosecuted by AUSA Bradley W. Murphy. Press release
> notes "the first defendant prosecuted in the Central District of Illinois
> for running an unlicensed internet money service business." Body captured
> from the 2014-12-10 Wayback snapshot (live www.justice.gov enforces
> BotManager challenge that blocks direct curl capture as of 2026-05-16).
> Trigger.type=doj_indictment is the closest schema enum; the load-bearing
> moment for this stub's timestamp is the public sentencing announcement.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: John D. Powell (Normal, IL — individual MSB / cash-for-bitcoin exchanger)
- **Chains**: `bitcoin`

> Single named individual (John D. Powell, of Normal, Ill., McLean County).
> No corporate vehicle, no named exchange platform, no domain/website is
> identified in the DOJ press release; Powell operated as an unregistered
> individual money-service-business person-to-person cash-for-bitcoin
> operator (May 2012 – February 2014, ~$3M handled). No on-chain BTC
> addresses are enumerated in the DOJ release; canonical_domains is empty
> because no clearnet surface was identified in the trigger artifact.

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `direct` · Δt = 0h

**Event label**: `powell_individual_unlicensed_msb_offramp_terminated_by_doj_sentencing`

**Timestamp**: `2014-12-04 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_legal`**
  - URL: <https://www.justice.gov/usao-cdil/pr/mclean-county-man-serve-four-years-prisonfor-operating-unlicensed-internet-bitcoin>
  - Wayback: <https://web.archive.org/web/20141210000000/https://www.justice.gov/usao-cdil/pr/mclean-county-man-serve-four-years-prisonfor-operating-unlicensed-internet-bitcoin>
  - body_hash: `sha256:b78a3318ac70cd09fe1a0b1ba5458d7c2ba6ba8a10892b337724d1b3f2b7cef1`
  - body_path: `sources/http_captures/powell-unlicensed-bitcoin-exchange-2014/primary/www.justice.gov__usao-cdil-pr-mclean-county-man__wayback_20141210__primary.html`
  > DOJ press release directly attests both the 2014-09-30 arrest (with
> pretrial-release revocation, after which Powell was detained pending
> sentencing) and the 2014-12-04 48-month sentencing with immediate
> remand to U.S. Marshals custody. The operational termination of the
> individual MSB off-ramp surface is the direct consequence named in
> the trigger artifact — attribution=direct. delta_hours=0 because
> the trigger.timestamp (2014-12-04 sentencing) and the observation
> timestamp coincide; the press-release publication date 2014-12-09
> is the citation-pinning anchor, kept distinct from the legally
> operative moment.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`shrem-faiella-bitcoin-exchange-2014`](./shrem-faiella-bitcoin-exchange-2014.md)
- [`silk-road-doj-seizure-2013`](./silk-road-doj-seizure-2013.md)
- [`btc-e-doj-2017`](./btc-e-doj-2017.md)
- [`nydfs-bitlicense-2015-06`](./nydfs-bitlicense-2015-06.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `71b6d3d`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

