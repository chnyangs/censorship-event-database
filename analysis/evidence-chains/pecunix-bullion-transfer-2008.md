# Evidence chain — `pecunix-bullion-transfer-2008`

**Status**: `admitted` · **Stratum**: `S5_corporate` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `0b7e0bd` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-21` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T09:13:36Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "In 2008, the Pecunix directors transferred the platform's
> gold bullion reserves from Mat Securitas Express AG (Zurich,
> Switzerland) to an undisclosed location — a single
> custody-layer offramp_cex operational-policy change at a
> digital-gold-currency administrator, plausibly responsive to
> the broader 2008 US DOJ digital-gold enforcement cycle
> (e-Gold guilty plea, e-Bullion seizure) though not directly
> triggered by any sanction or order naming Pecunix. The row
> claims only this single-layer custody policy change with
> attribution=plausible; no L0/L1/L3/L4/asset-onchain effects
> are coded. Discovery-tier only: no comparable-analysis use."

## 1. Trigger

- **Type**: `corporate_policy_change`
- **Actor**: `PECUNIX_OPERATOR`
- **Timestamp**: `2008-06-01 00:00:00+00:00` (precision: `week`)

### Trigger citations

- **`supporting_community`**
  - URL: <https://en.wikipedia.org/wiki/Digital_gold_currency>
  - Wayback: <https://web.archive.org/web/2008/https://en.wikipedia.org/wiki/Digital_gold_currency>
  > Wikipedia "Digital gold currency" article documents that
> Pecunix (founded 2002 by Simon "Sidd" Davis, registered in
> Panama) had originally stored its bullion with Mat Securitas
> Express AG in Zurich, Switzerland, and that in 2008 the
> Pecunix directors transferred the bullion to an undisclosed
> location. This operational shift coincides with the broader
> 2008 digital-gold-currency enforcement cycle (e-Gold DC
> guilty plea 2008-07-21; e-Bullion seizure 2008-08-01) and
> represents a corporate-policy operational change at the
> platform's bullion-custody layer. No precise day-level
> anchor is publicly attested; trigger date 2008-06-01 is
> coded with week precision as a mid-2008 approximation
> bracketing the transfer announcement window. evidence_use=
> contextual_unarchived because no body_hash has been pinned
> in this DRYRUN authoring pass; wayback URL is a 2008
> wildcard pointer pending precise snapshot re-pin.
- **`supporting_community`**
  - URL: <https://en-academic.com/dic.nsf/enwiki/1580701>
  - Wayback: <https://web.archive.org/web/2008/https://en-academic.com/dic.nsf/enwiki/1580701>
  > Academic mirror of the historical Wikipedia Pecunix entry
> corroborating the 2008 bullion transfer from Mat Securitas
> Zurich to an undisclosed location. Tertiary corroborating
> reference; not load-bearing. evidence_use=
> contextual_unarchived.
- **`supporting_journalism`**
  - URL: <https://themonetaryfuture.blogspot.com/2010/07/overview-of-pecunix.html>
  - Wayback: <https://web.archive.org/web/2008/https://themonetaryfuture.blogspot.com/2010/07/overview-of-pecunix.html>
  > "The Monetary Future: An Overview of Pecunix" (2010-07)
> retrospective trade-press summary of Pecunix's operating
> model (Panama-incorporated digital gold currency operating
> through third-party exchange agents rather than direct
> retail customers, which distinguished its regulatory
> exposure from e-Gold's). Provides contextual framing for
> why Pecunix's 2008 operational adjustments did not
> culminate in a US-style 18 USC s 1960 enforcement action
> in the same window. Not load-bearing for the bullion-
> transfer trigger itself. evidence_use=contextual_unarchived.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Pecunix
- **Canonical domains**: `pecunix.com`

> Named target entity: Pecunix (Panama-incorporated digital
> gold currency platform founded 2002 by Simon "Sidd" Davis).
> Pecunix operated as a centralized digital-gold-currency
> administrator whose units were redeemable for physical gold
> bullion originally stored with Mat Securitas Express AG in
> Zurich, Switzerland. The 2008 corporate action moved this
> bullion holding to an undisclosed location, an operational/
> custody-layer policy change at the platform operator's
> discretion. Marked subset because the action targets the
> platform's own custodial arrangement (a single internal
> corporate decision) rather than an enumerated set of named
> Pecunix account holders, exchange agents, or upstream
> counterparties. Pecunix units were off-chain ledger entries
> administered by the operator; no blockchain addresses are
> enumerated.

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `plausible` · Δt = Noneh

**Event label**: `pecunix_directors_transfer_bullion_reserves_from_mat_securitas_zurich_to_undisclosed_location`

**Timestamp**: `2008-06-01 00:00:00+00:00` (precision: `week`)

**Sources**:

- **`primary_corporate`**
  - URL: <http://www.pecunix.com/money.refined...ind.goldbars>
  - Wayback: <https://web.archive.org/web/20081014015939/http://www.pecunix.com/money.refined...ind.goldbars>
  - body_hash: `sha256:32bba84329e2bcc83ac181810ae56d27483e4ddae6ef03c6b53c1a6271a81773`
  - body_path: `sources/http_captures/pecunix-bullion-transfer-2008/primary/web.archive.org__web-20081014015939-http-www.pecunix.com-money.refined...ind.goldbars__f0f49c077e.html`
  > Pecunix operator site (2008 Wayback snapshot) documenting the
> gold-bullion-backed digital-currency service. This operator
> primary_corporate anchor establishes the service substrate and
> 2008 memento, but does not independently prove the bullion-transfer
> date.
- **`semi_primary_wayback`**
  - URL: <https://themonetaryfuture.blogspot.com/2010/07/overview-of-pecunix.html>
  - Wayback: <https://web.archive.org/web/20120403064453/http://themonetaryfuture.blogspot.com/2010/07/overview-of-pecunix.html>
  - body_hash: `sha256:51e7ca12d132901dad9cba171796127b8e3ba8e718470ac4ce57b2b932b27efe`
  - body_path: `sources/http_captures/pecunix-bullion-transfer-2008/primary/web.archive.org__web-20110101000000-https-themonetaryfuture.blogspot.com-2010-07-overview-of-pecunix.html__82da1f34dd.html`
  > The Monetary Future overview of Pecunix (digital gold currency).
> Independent semi-primary anchor.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`egold-doj-guilty-plea-2008-07`](./egold-doj-guilty-plea-2008-07.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `0b7e0bd`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

