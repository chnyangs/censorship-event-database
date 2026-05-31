# Evidence chain — `dydx-tornado-account-block-2022-08`

**Status**: `admitted` · **Stratum**: `S5_corporate` · **Shape**: `comparison` (2 changed layer(s): `l4_frontend`, `offramp_cex`) · **Tier**: `anchor_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `ec5c516` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-21` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "dYdX's 2022-08-11 block of accounts whose wallets had any
> historical interaction with the OFAC-designated Tornado Cash
> contracts — implemented via a third-party compliance vendor
> flag at the dYdX-operated trading UI, with funds remaining
> withdrawable from flagged accounts — documents an L4-frontend
> + offramp_cex dual-layer corporate-compliance action and the
> first major operator-acknowledged history-based 'guilt by
> association' block downstream of the 2022-08-08 OFAC trigger
> (related event tornado-cash-ofac-2022). Paper-relevant as the
> hybrid-CEX vertex of the S5_corporate cascade (alongside
> aave-tornado-frontend-block-2022-08 at L4 and
> uniswap-balancer-tornado-frontend-block-2022-08 at L4)."

## 1. Trigger

- **Type**: `corporate_policy_change`
- **Actor**: `dydx_trading_inc`
- **Timestamp**: `2022-08-11 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_corporate`**
  - URL: <https://dydx.exchange/blog/tornado-cash-update>
  - Wayback: <https://web.archive.org/web/2022/https://dydx.exchange/blog/tornado-cash-update>
  > dYdX Trading Inc. official blog post of 2022-08-11 confirming that
> the platform's compliance vendor flagged accounts associated with
> Tornado Cash following the 2022-08-08 OFAC SDN designation (see
> related event tornado-cash-ofac-2022) and that flagged accounts
> had been blocked from the dYdX platform. The post explicitly
> acknowledges that "this sudden influx of flags affected many
> account holders that never directly engaged with Tornado Cash"
> — i.e. the first major operator-acknowledged history-based
> "guilt by association" block in the dataset. DRYRUN: pinned
> Wayback snapshot and body_hash for the dYdX blog revision are
> deferred to the human-audit pass; marked
> evidence_use=contextual_unarchived per validator policy for
> unarchived sources.
- **`supporting_journalism`**
  - URL: <https://www.coindesk.com/business/2022/08/11/crypto-exchange-dydx-blocked-accounts-that-received-even-small-amounts-from-tornado-cash>
  - Wayback: <https://web.archive.org/web/2022/https://www.coindesk.com/business/2022/08/11/crypto-exchange-dydx-blocked-accounts-that-received-even-small-amounts-from-tornado-cash>
  > CoinDesk contemporaneous coverage (2022-08-11) of the dYdX
> account-block action, naming the history-based "guilt by
> association" mechanism — accounts blocked because their wallets
> received even small amounts traceable to Tornado Cash, regardless
> of whether the holder knowingly used the mixer. Triangulation
> source for day-level timing and the "history-based not
> current-state-based" mechanism. DRYRUN: pinned Wayback snapshot
> deferred to human audit.
- **`supporting_journalism`**
  - URL: <https://www.theblock.co/post/162928/dydx-confirms-blocking-user-accounts-tied-to-tornado-cash>
  - Wayback: <https://web.archive.org/web/2022/https://www.theblock.co/post/162928/dydx-confirms-blocking-user-accounts-tied-to-tornado-cash>
  > The Block contemporaneous coverage (2022-08-11) of the dYdX
> compliance action, documenting the compliance-vendor mechanism
> and dYdX's same-day statement that funds in blocked accounts
> remained available for withdrawal while trading and other
> platform functions were restricted. Triangulation source for
> the layer split (l4_frontend block vs offramp_cex withdrawal
> constraint). DRYRUN: pinned Wayback snapshot deferred to human
> audit.
- **`supporting_journalism`**
  - URL: <https://cointelegraph.com/news/dydx-confirms-blocking-and-unblocking-some-accounts-linked-to-tornado-cash>
  - Wayback: <https://web.archive.org/web/2022/https://cointelegraph.com/news/dydx-confirms-blocking-and-unblocking-some-accounts-linked-to-tornado-cash>
  > Cointelegraph contemporaneous coverage (2022-08-11) of the dYdX
> action and the partial rollback (some accounts unblocked after
> the platform acknowledged the compliance-vendor flag was
> over-inclusive). Triangulation source for the rollback note.
> DRYRUN: pinned Wayback snapshot deferred to human audit.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Protocol**: `dydx_v3`
- **Actor name**: dYdX Trading Inc.
- **Chains**: `ethereum`
- **Canonical domains**: `dydx.exchange`, `trade.dydx.exchange`

> dYdX Trading Inc. operates the dYdX centralized perpetuals exchange
> (v3 era — centralized matching engine with onchain StarkEx-based
> settlement). On 2022-08-11 dYdX's compliance vendor flagged
> accounts whose wallet history included any interaction with the
> OFAC-listed Tornado Cash contracts (per related event
> tornado-cash-ofac-2022) and dYdX blocked the flagged accounts
> from the platform UI; flagged accounts retained the ability to
> withdraw funds but lost the ability to open new positions or
> otherwise interact with the trading UI. Target is the operator
> entity (dYdX Trading Inc.) rather than an enumerated address set
> because the blocklist is a moving reference maintained by the
> compliance vendor (not a static published roster); subset because
> only the dYdX-operated venue is in scope here (the StarkEx
> settlement contracts on-chain remained unaffected).

## 3. Changed-layer observations (supports the scoped claim)

### l4_frontend · attribution: `direct` · Δt = 0h

**Event label**: `dydx_blocked_accounts_with_any_historical_tornado_cash_interaction`

**Timestamp**: `2022-08-11 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_corporate`**
  - URL: <https://dydx.exchange/blog/tornado-cash-update>
  - Wayback: <https://web.archive.org/web/20220829214213/https://dydx.exchange/blog/tornado-cash-update>
  - body_hash: `sha256:e4f66984122b7e34fb7142f29bb5a9d1805dad6db38242a2383158abad00b817`
  - body_path: `sources/http_captures/dydx-tornado-account-block-2022-08/primary/web.archive.org__web-20220812000000-https-dydx.exchange-blog-tornado-cash-update__c44496f200.html`
  > dYdX official blog (2022-08) confirming it blocked accounts that
> received funds traceable to Tornado Cash (including via dust attacks),
> via its compliance provider. primary_corporate anchor; attribution=
> direct. Wayback 20220829214213 pinned.
- **`semi_primary_wayback`**
  - URL: <https://www.coindesk.com/business/2022/08/11/crypto-exchange-dydx-blocked-accounts-that-received-even-small-amounts-from-tornado-cash>
  - Wayback: <https://web.archive.org/web/20220811213559/https://www.coindesk.com/business/2022/08/11/crypto-exchange-dydx-blocked-accounts-that-received-even-small-amounts-from-tornado-cash/>
  - body_hash: `sha256:4ca9dc3fc04a525ca5af4665e81b714c3df235b3d9f7546a109bb55852cc4157`
  - body_path: `sources/http_captures/dydx-tornado-account-block-2022-08/primary/web.archive.org__web-20220812000000-https-www.coindesk.com-business-2022-08-11-crypto-exchange-dydx-blocked-accounts-that-received-even-small-amounts-from-tornado-cash__641b67aa65.html`
  > CoinDesk 2022-08-11 coverage corroborating the dYdX account blocks.
> Independent semi-primary anchor.

### offramp_cex · attribution: `direct` · Δt = 0h

**Event label**: `dydx_off_ramp_trading_restricted_for_tornado_tainted_accounts`

**Timestamp**: `2022-08-11 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_corporate`**
  - URL: <https://dydx.exchange/blog/tornado-cash-update>
  - Wayback: <https://web.archive.org/web/20220829214213/https://dydx.exchange/blog/tornado-cash-update>
  - body_hash: `sha256:e4f66984122b7e34fb7142f29bb5a9d1805dad6db38242a2383158abad00b817`
  - body_path: `sources/http_captures/dydx-tornado-account-block-2022-08/primary/web.archive.org__web-20220812000000-https-dydx.exchange-blog-tornado-cash-update__c44496f200.html`
  > dYdX official blog (2022-08) confirming it blocked accounts that
> received funds traceable to Tornado Cash (including via dust attacks),
> via its compliance provider. primary_corporate anchor; attribution=
> direct. Wayback 20220829214213 pinned.
- **`semi_primary_wayback`**
  - URL: <https://www.coindesk.com/business/2022/08/11/crypto-exchange-dydx-blocked-accounts-that-received-even-small-amounts-from-tornado-cash>
  - Wayback: <https://web.archive.org/web/20220811213559/https://www.coindesk.com/business/2022/08/11/crypto-exchange-dydx-blocked-accounts-that-received-even-small-amounts-from-tornado-cash/>
  - body_hash: `sha256:4ca9dc3fc04a525ca5af4665e81b714c3df235b3d9f7546a109bb55852cc4157`
  - body_path: `sources/http_captures/dydx-tornado-account-block-2022-08/primary/web.archive.org__web-20220812000000-https-www.coindesk.com-business-2022-08-11-crypto-exchange-dydx-blocked-accounts-that-received-even-small-amounts-from-tornado-cash__641b67aa65.html`
  > CoinDesk 2022-08-11 coverage corroborating the dYdX account blocks.
> Independent semi-primary anchor.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`tornado-cash-ofac-2022`](./tornado-cash-ofac-2022.md)
- [`aave-tornado-frontend-block-2022-08`](./aave-tornado-frontend-block-2022-08.md)
- [`uniswap-balancer-tornado-frontend-block-2022-08`](./uniswap-balancer-tornado-frontend-block-2022-08.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `ec5c516`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

