# Evidence chain — `mtgox-usd-withdrawal-suspension-2013-06`

**Status**: `admitted` · **Stratum**: `S5_corporate` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `cc05a9c` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-21` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "Mt. Gox suspended all USD withdrawals globally on 2013-06-20, framed
> as a voluntary corporate verification-procedure update but causally
> downstream of the 2013-05-14 DHS Dwolla seizure (mtgox-dhs-dwolla-
> wells-fargo-seizure-2013). The row claims only this single-layer
> offramp_cex operator-announcement observation. Historical-baseline
> tier; not used in main statistical denominators."

## 1. Trigger

- **Type**: `corporate_policy_change`
- **Actor**: `MTGOX_OPERATOR`
- **Timestamp**: `2013-06-20 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_corporate`**
  - URL: <https://www.mtgox.com/press_release_20130620.html>
  - Wayback: <https://web.archive.org/web/20140122193202/https://www.mtgox.com/press_release_20130620.html>
  > Mt. Gox 2013-06-20 press release announcing the temporary suspension
> of all USD withdrawals pending implementation of an upgraded USD-
> transaction processing system in cooperation with its banking
> partner. Officially framed as a voluntary corporate verification-
> procedure update; in context, downstream of the 2013-05-14 DHS/HSI
> Dwolla account seizure (mtgox-dhs-dwolla-wells-fargo-seizure-2013)
> and the parallel Wells Fargo / Mutum Sigillum banking-rail
> difficulties. mtgox.com is dead — Wayback memento 2014-01-22
> retained as the only available archive vector. evidence_use=
> contextual_unarchived: no body_hash captured into
> sources/http_captures/ in this session.
- **`supporting_journalism`**
  - URL: <https://www.coindesk.com/markets/2013/06/20/mt-gox-temporarily-suspends-usd-withdrawals>
  - Wayback: <https://web.archive.org/web/20211016054018/https://www.coindesk.com/markets/2013/06/20/mt-gox-temporarily-suspends-usd-withdrawals/>
  > Contemporary CoinDesk coverage (2013-06-20) reporting Mt. Gox's
> announcement of a temporary suspension of USD withdrawals, framed
> by the exchange as a response to growing transaction volume that
> was straining its banking partner's processing capacity. Wayback
> memento 2021-10-16 (closest stable snapshot). evidence_use=
> contextual_unarchived: no body_hash captured into
> sources/http_captures/ in this session.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Mt. Gox K.K.
- **Chains**: `bitcoin`
- **Canonical domains**: `mtgox.com`

> All Mt. Gox USD-balance customers globally. USD withdrawals were
> suspended pending banking-partner review and verification process
> changes; USD deposits and non-USD withdrawals continued. No on-chain
> BTC addresses are enumerated at this event level; the action is a
> fiat-rail offramp suspension at the operator layer.

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `direct` · Δt = 0h

**Event label**: `usd_withdrawal_suspended_globally`

**Timestamp**: `2013-06-20 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_corporate`**
  - URL: <https://www.mtgox.com/press_release_20130620.html>
  - Wayback: <https://web.archive.org/web/20130811014059/https://www.mtgox.com/press_release_20130620.html>
  - body_hash: `sha256:15d00b9c99e54bc0889f7ced1f774c2e2905913fec715d5b0abdaf4bb0a8d389`
  - body_path: `sources/http_captures/mtgox-usd-withdrawal-suspension-2013-06/primary/web.archive.org__web-20130621000000-https-www.mtgox.com-press_release_20130620.html__f599d08286.html`
  > Mt. Gox operator press release (2013-06-20) announcing the
> temporary suspension of USD withdrawals (citing the need to upgrade
> systems amid banking/AML pressure). Operator primary-corporate anchor;
> attribution=direct. Wayback 20130811014059 pinned.
- **`semi_primary_wayback`**
  - URL: <https://www.coindesk.com/markets/2013/06/20/mt-gox-temporarily-suspends-usd-withdrawals>
  - Wayback: <https://web.archive.org/web/20211016054018/https://www.coindesk.com/markets/2013/06/20/mt-gox-temporarily-suspends-usd-withdrawals/>
  - body_hash: `sha256:3fb6024595c6527ebd04ed9583e270751efd285f71435bf763f3ea9bde362c0c`
  - body_path: `sources/http_captures/mtgox-usd-withdrawal-suspension-2013-06/primary/web.archive.org__web-20130622000000-https-www.coindesk.com-markets-2013-06-20-mt-gox-temporarily-suspends-usd-withdrawals__d98ee82f20.html`
  > CoinDesk 2013-06-20 coverage corroborating the USD-withdrawal
> suspension. Independent semi-primary anchor.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`mtgox-dhs-dwolla-wells-fargo-seizure-2013`](./mtgox-dhs-dwolla-wells-fargo-seizure-2013.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `cc05a9c`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

