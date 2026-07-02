# Evidence chain — `bitfinex-us-retail-customer-exit-2017-11`

**Status**: `admitted` · **Stratum**: `S5_corporate` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-08` · **Source commit**: `ee7bf1a` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-31` · **Tool version**: `0.1.0` · **Generated**: `2026-06-25T23:48:26Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "Bitfinex's termination of trading/deposit/withdrawal functionality for all
> US retail customers (effective ≤2017-11-09, dropping US users from ICO/ERC-20
> tokens after the SEC ICO warning) severed the Bitfinex off-ramp for the US
> retail segment; single-layer offramp_cex observed_change, attribution=direct
> (Bitfinex publicly cited the US ICO-securities backdrop)."

## 1. Trigger

- **Type**: `corporate_policy_change`
- **Actor**: `bitfinex`
- **Timestamp**: `2017-08-11 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_corporate`**
  - URL: <https://www.bitfinex.com/posts/216>
  - Wayback: <https://web.archive.org/web/20170811184809/https://www.bitfinex.com/posts/216>
  - body_hash: `sha256:3aeb5ddb3641fbc4a7d1aa5a473832b0e0e2c9c3bd94bbb50ea213e600d2daa5`
  - body_path: `sources/http_captures/bitfinex-us-retail-customer-exit-2017-11/official_bitfinex/web.archive.org__web-20170811184809-https-www.bitfinex.com-posts-216__bcdcdd5a39.html`
  > Official Bitfinex announcement "Service Changes for U.S. Customers",
> pinned to the first successful Wayback memento found for /posts/216
> (2017-08-11 18:48:09Z). The captured body states that Bitfinex was
> making changes to services for U.S. individuals, would stop accepting
> U.S. individual verification requests immediately, had decided to
> begin disengaging from U.S. retail customers, and would discontinue
> services to existing U.S. individual customers over the next 90 days.
> It also ties the ERC20/ICO-token trading restriction to the SEC DAO
> report.
- **`semi_primary_wayback`**
  - URL: <https://news.bitcoin.com/bitfinex-to-terminate-services-to-us-retail-customers-by-november-9/>
  - Wayback: <https://web.archive.org/web/20171018121607/https://news.bitcoin.com/bitfinex-to-terminate-services-to-us-retail-customers-by-november-9/>
  - body_hash: `sha256:5a26060a406b8a6b4c8e5459d177802d17c18a8b1b445994531b2c008a140fd9`
  - body_path: `sources/http_captures/bitfinex-us-retail-customer-exit-2017-11/primary/web.archive.org__web-20171018121607-https-news.bitcoin.com-bitfinex-to-terminate-services-to-us-retail-customers-by-november-9__f781837006.html`
  > Bitcoin.com 2017-10-18: Bitfinex announced it would "terminate all
> services to U.S. retail customers" no later than 2017-11-09, and
> barred US-based customers from ERC-20/ICO tokens within a week of the
> SEC's July-2017 ICO-as-securities warning. Bitfinex cited having "for
> some time considered pulling away from the retail marketplace in the
> U.S." Body grep-confirmed: "Terminate Services to US Retail Customers",
> "terminate all services for U.S. individual customers", "no later than
> November 9, 2017", and "August 11". Wayback 20171018121607 pinned.
> Trigger anchored to the 2017-08-11 first disclosure of the plan.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `complete`
- **Actor name**: Bitfinex US retail customers
- **Chains**: `ethereum`

> Single class: Bitfinex US retail customers. The action terminated trading,
> deposit, and withdrawal functionality for all US retail users (and dropped
> US users from ERC-20/ICO tokens), geofencing the US retail segment off the
> Bitfinex off-ramp.

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `direct` · Δt = 2160h

**Event label**: `bitfinex_terminates_us_retail_access`

**Timestamp**: `2017-11-09 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_corporate`**
  - URL: <https://www.bitfinex.com/posts/227>
  - Wayback: <https://web.archive.org/web/20171017060118/https://www.bitfinex.com/posts/227>
  - body_hash: `sha256:e4cea1f8dd6de3168fac04cae27a079065b4d9711898a7c8864c804ddb74585c`
  - body_path: `sources/http_captures/bitfinex-us-retail-customer-exit-2017-11/official_bitfinex/web.archive.org__web-20171017060118-https-www.bitfinex.com-posts-227__440056aa06.html`
  > Official Bitfinex update "U.S. Individual Users", pinned to the first
> successful Wayback memento found for /posts/227 (2017-10-17
> 06:01:18Z). The captured body says Bitfinex was terminating trading,
> deposit, and withdrawal functionality for U.S. individual customers
> by no later than 2017-11-09, and that all U.S. individual users had
> to arrange withdrawal of digital tokens by November 9.
- **`semi_primary_wayback`**
  - URL: <https://news.bitcoin.com/bitfinex-to-terminate-services-to-us-retail-customers-by-november-9/>
  - Wayback: <https://web.archive.org/web/20171018121607/https://news.bitcoin.com/bitfinex-to-terminate-services-to-us-retail-customers-by-november-9/>
  - body_hash: `sha256:5a26060a406b8a6b4c8e5459d177802d17c18a8b1b445994531b2c008a140fd9`
  - body_path: `sources/http_captures/bitfinex-us-retail-customer-exit-2017-11/primary/web.archive.org__web-20171018121607-https-news.bitcoin.com-bitfinex-to-terminate-services-to-us-retail-customers-by-november-9__f781837006.html`
  > Bitfinex terminated all services to US retail customers by 2017-11-09
> and barred US users from ICO/ERC-20 tokens within a week of the SEC's
> ICO-as-securities warning. attribution=direct: Bitfinex publicly
> announced the termination and cited the US ICO-securities regulatory
> backdrop in its own statement (§1.1 — actor references the trigger
> and the action names the US-retail target class it acted upon).

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`bitfinex-cftc-retail-commodity-2016`](./bitfinex-cftc-retail-commodity-2016.md)
- [`coinbase-india-exit-2022`](./coinbase-india-exit-2022.md)
- [`bybit-singapore-exit-2022`](./bybit-singapore-exit-2022.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `ee7bf1a`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

