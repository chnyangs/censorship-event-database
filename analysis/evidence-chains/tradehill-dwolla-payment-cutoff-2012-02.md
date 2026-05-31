# Evidence chain — `tradehill-dwolla-payment-cutoff-2012-02`

**Status**: `admitted` · **Stratum**: `S5_corporate` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `9964436` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-31` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "Payment processor Dwolla's early-2012 severance of TradeHill's fiat
> payment rail (reversing/withholding payments and cutting off service)
> produced an offramp_cex cascade (TradeHill ceased operations); the
> row claims a single-layer offramp shutdown with attribution=plausible.
> Discovery-tier only; no comparable-analysis use."

## 1. Trigger

- **Type**: `corporate_policy_change`
- **Actor**: `dwolla_payment_processor`
- **Timestamp**: `2012-02-13 00:00:00+00:00` (precision: `week`)

### Trigger citations

- **`semi_primary_wayback`**
  - URL: <https://venturebeat.com/2012/03/07/tradehill-sues-suing-dwolla-bitcoin/>
  - Wayback: <https://web.archive.org/web/20211026183118/https://venturebeat.com/2012/03/07/tradehill-sues-suing-dwolla-bitcoin/>
  - body_hash: `sha256:2a5326490ca22c4e42abdb9d64d4d26038a72ed276c9a8da6b653896fd8f1cb0`
  - body_path: `sources/http_captures/tradehill-dwolla-payment-cutoff-2012-02/primary/web.archive.org__web-20211026183118-https-venturebeat.com-2012-03-07-tradehill-sues-suing-dwolla-bitcoin__512fa258ef.html`
  > VentureBeat (2012-03-07): TradeHill, an early U.S. Bitcoin
> exchange, sued payment processor Dwolla, alleging Dwolla
> reversed/withheld ~$94k of payments and cut off service,
> contributing to TradeHill ceasing operations in early 2012.
> Wayback 20211026183118 pinned.
- **`semi_primary_wayback`**
  - URL: <https://www.americanbanker.com/news/dwolla-put-us-out-of-business-bitcoin-exchange-says-in-suit>
  - Wayback: <https://web.archive.org/web/20260410131031/https://www.americanbanker.com/news/dwolla-put-us-out-of-business-bitcoin-exchange-says-in-suit>
  - body_hash: `sha256:43b4702a95855ad5650bc47a8caa4f51e73b3baf190982878a1421faca89a5fd`
  - body_path: `sources/http_captures/tradehill-dwolla-payment-cutoff-2012-02/primary/web.archive.org__web-20260410131031-https-www.americanbanker.com-news-dwolla-put-us-out-of-business-bitcoin-exchange-says-in-suit__40e7218451.html`
  > American Banker: "Dwolla Put Us Out of Business, Bitcoin
> Exchange Says in Suit." Frames the Dwolla payment-rail cutoff
> of TradeHill in the context of compliance/FinCEN pressure on
> payment processors serving Bitcoin businesses (early
> financial-rail de-risking). Independent semi-primary anchor.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `complete`
- **Actor name**: Dwolla (payment processor) vs TradeHill
- **Canonical domains**: `tradehill.com`

> TradeHill, Inc. (early U.S.-based Bitcoin exchange) as the affected
> entity whose Dwolla-mediated fiat payment rail was severed. Single
> named affected exchange; no on-chain addresses (the action is a
> payment-processor service cutoff at the fiat off-ramp).

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `plausible` · Δt = 0h

**Event label**: `dwolla_severs_tradehill_fiat_payment_rail`

**Timestamp**: `2012-02-13 00:00:00+00:00` (precision: `week`)

**Sources**:

- **`semi_primary_wayback`**
  - URL: <https://venturebeat.com/2012/03/07/tradehill-sues-suing-dwolla-bitcoin/>
  - Wayback: <https://web.archive.org/web/20211026183118/https://venturebeat.com/2012/03/07/tradehill-sues-suing-dwolla-bitcoin/>
  - body_hash: `sha256:2a5326490ca22c4e42abdb9d64d4d26038a72ed276c9a8da6b653896fd8f1cb0`
  - body_path: `sources/http_captures/tradehill-dwolla-payment-cutoff-2012-02/primary/web.archive.org__web-20211026183118-https-venturebeat.com-2012-03-07-tradehill-sues-suing-dwolla-bitcoin__512fa258ef.html`
  > VentureBeat 2012-03-07 reporting on TradeHill v. Dwolla:
> Dwolla's reversal/withholding of payments and service cutoff
> severed TradeHill's fiat rail. attribution=plausible: the
> cutoff is documented but its characterization as
> compliance/regulatory-pressure-driven (vs a private business
> dispute) is the suit's allegation, not a direct admission.
- **`semi_primary_wayback`**
  - URL: <https://www.americanbanker.com/news/dwolla-put-us-out-of-business-bitcoin-exchange-says-in-suit>
  - Wayback: <https://web.archive.org/web/20260410131031/https://www.americanbanker.com/news/dwolla-put-us-out-of-business-bitcoin-exchange-says-in-suit>
  - body_hash: `sha256:43b4702a95855ad5650bc47a8caa4f51e73b3baf190982878a1421faca89a5fd`
  - body_path: `sources/http_captures/tradehill-dwolla-payment-cutoff-2012-02/primary/web.archive.org__web-20260410131031-https-www.americanbanker.com-news-dwolla-put-us-out-of-business-bitcoin-exchange-says-in-suit__40e7218451.html`
  > American Banker coverage framing the Dwolla cutoff within the
> early financial-rail de-risking of Bitcoin businesses.
> Independent second semi-primary anchor.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`bitcoinica-shutdown-2012-05`](./bitcoinica-shutdown-2012-05.md)
- [`bitfloor-capital-one-debanking-2013-04`](./bitfloor-capital-one-debanking-2013-04.md)
- [`mtgox-dhs-dwolla-wells-fargo-seizure-2013`](./mtgox-dhs-dwolla-wells-fargo-seizure-2013.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `9964436`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

