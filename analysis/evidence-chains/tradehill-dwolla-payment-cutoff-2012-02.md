# Evidence chain — `tradehill-dwolla-payment-cutoff-2012-02`

**Status**: `admitted` · **Stratum**: `S5_corporate` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-02` · **Source commit**: `f54a8ae` · **Schema**: `0.2.0` · **Event last_verified**: `2026-06-02` · **Tool version**: `0.1.0` · **Generated**: `2026-06-04T09:44:11Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "TradeHill's 2012-02-13 announcement halted trading/deposits and returned
> client funds after a bundled fiat-rail/compliance shock: money-transmission
> licensing pressure, multiple bank-account closures, Paxum closing Bitcoin
> business accounts, and a payment-processor dispute later litigated as
> TradeHill v. Dwolla. The row claims one directly attributed
> offramp_cex/exchange-service shutdown by TradeHill, while treating Dwolla
> as a documented component rather than the sole proved cause. Discovery-tier
> only; no comparable-analysis use."

## 1. Trigger

- **Type**: `corporate_policy_change`
- **Actor**: `tradehill_exchange`
- **Timestamp**: `2012-02-13 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_corporate`**
  - URL: <https://bitcointalk.org/index.php?topic=63749.0>
  - body_hash: `sha256:fb9e8e442f03e0e98bd80b611fa9cdf969d26aafe133dc6583e6a11e2d9e5417`
  - body_path: `sources/http_captures/tradehill-dwolla-payment-cutoff-2012-02/primary-tradehill-bitcointalk-v1/bitcointalk.org__index.php__864a09c795.html`
  > Primary TradeHill announcement by Jered Kenna (TradeHill) on
> Bitcointalk, 2012-02-13 22:30:57 forum timestamp. The post states
> that TradeHill was immediately shutting down trading/deposits and
> returning client funds because increasing regulation meant it could
> not operate without money-transmission licensing, combined with
> multiple bank-account closures, Paxum closing Bitcoin-business
> accounts, and a payment processor removing more than $100,000
> without notice. A later same-thread Jered Kenna reply clarifies that
> Dwolla's amount was larger than $10k and that the Paxum shutdown was
> separate. Local capture grep-verified the author, timestamp, shutdown
> language, money-transmission-licensing language, Paxum/bank-account
> closures, and payment-processor/Dwolla clarification.
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
- **Actor name**: TradeHill Bitcoin exchange fiat/off-ramp service
- **Canonical domains**: `tradehill.com`

> TradeHill, Inc. (early U.S.-based Bitcoin exchange) as the affected
> entity whose trading/deposit service was halted and client funds were
> returned. Single named affected exchange; no on-chain addresses (the
> action is a fiat off-ramp / exchange-service shutdown shaped by money-
> transmission licensing, bank-account closures, Paxum's Bitcoin-account
> closure, and a Dwolla/payment-processor dispute).

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `direct` · Δt = 0h

**Event label**: `tradehill_halts_trading_deposits_and_returns_client_funds`

**Timestamp**: `2012-02-13 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_corporate`**
  - URL: <https://bitcointalk.org/index.php?topic=63749.0>
  - body_hash: `sha256:fb9e8e442f03e0e98bd80b611fa9cdf969d26aafe133dc6583e6a11e2d9e5417`
  - body_path: `sources/http_captures/tradehill-dwolla-payment-cutoff-2012-02/primary-tradehill-bitcointalk-v1/bitcointalk.org__index.php__864a09c795.html`
  > TradeHill CEO Jered Kenna's primary announcement: TradeHill was
> immediately shutting down trading/deposits and returning client
> funds. The same post gives the causal bundle as increasing
> regulation / money-transmission licensing, multiple bank-account
> closures, Paxum closing Bitcoin-business accounts, and a payment
> processor removing more than $100,000 without notice; a later
> same-thread reply clarifies Dwolla was a larger-than-$10k issue
> while separate from the Paxum shutdown. attribution=direct for the
> TradeHill service shutdown itself; the row does not claim Dwolla
> alone directly caused the shutdown.
- **`semi_primary_wayback`**
  - URL: <https://venturebeat.com/2012/03/07/tradehill-sues-suing-dwolla-bitcoin/>
  - Wayback: <https://web.archive.org/web/20211026183118/https://venturebeat.com/2012/03/07/tradehill-sues-suing-dwolla-bitcoin/>
  - body_hash: `sha256:2a5326490ca22c4e42abdb9d64d4d26038a72ed276c9a8da6b653896fd8f1cb0`
  - body_path: `sources/http_captures/tradehill-dwolla-payment-cutoff-2012-02/primary/web.archive.org__web-20211026183118-https-venturebeat.com-2012-03-07-tradehill-sues-suing-dwolla-bitcoin__512fa258ef.html`
  > VentureBeat 2012-03-07 reporting on TradeHill v. Dwolla:
> Dwolla's reversal/withholding of payments and service cutoff
> contributed to TradeHill's fiat-rail failure. Corroborating
> semi-primary litigation/reporting anchor for the Dwolla component,
> not the sole trigger source.
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

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `f54a8ae`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

