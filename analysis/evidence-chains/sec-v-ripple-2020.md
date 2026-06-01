# Evidence chain — `sec-v-ripple-2020`

**Status**: `admitted` · **Stratum**: `S3_doj_sec_cftc_fiod` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `1c9c65c` · **Schema**: `0.2.0` · **Event last_verified**: `2026-06-01` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T12:19:10Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "The 2020-12-22 SEC v. Ripple Labs Inc. civil securities-law action is
> retained as a narrowed CEX/off-ramp comparison: Coinbase and Bitstamp each
> issued official, replayably captured announcements restricting XRP trading
> for U.S. customers after the SEC action/filing against Ripple. The row does
> not claim a Ripple.com L4 frontend change, Binance.US/Kraken coverage, L0
> network blocking, L1 consensus impact, L3 RPC filtering, or asset-onchain
> freezes."

## 1. Trigger

- **Type**: `sec_action`
- **Actor**: `US_SEC`
- **Timestamp**: `2020-12-22 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://www.sec.gov/news/press-release/2020-338>
  - body_hash: `sha256:5bea8f0f40ef78c32abd795f49ac508529e2d0bc6dee88ff110596007f4b910e`
  - body_path: `sources/http_captures/sec-v-ripple-2020/primary/www.sec.gov__news-press-release-2020-338__1549f335ea.html`
  > SEC press release 2020-338, dated 2020-12-22, announcing the civil
> action against Ripple Labs Inc., Bradley Garlinghouse, and Christian
> Larsen for an alleged unregistered ongoing digital-asset securities
> offering of XRP. Captured locally 2026-06-01 with replayable
> body_hash/body_path.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Ripple Labs Inc / Garlinghouse / Larsen
- **Canonical domains**: `coinbase.com`, `bitstamp.net`

> Ripple Labs Inc. corporate entity plus individual co-defendants Bradley
> Garlinghouse and Christian Larsen are the legal targets named by the SEC.
> The retained downstream observation scope is narrowed to the two
> US-facing centralized-exchange actions with replayable official
> corporate sources pinned in this repair pass: Coinbase and Bitstamp. The
> row no longer admits the prior Binance.US, Kraken, or Ripple.com L4
> observations because those load-bearing sources were not replayably
> anchored in the retained evidence.

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `direct` · Δt = 144h

**Event label**: `coinbase_announced_xrp_trading_suspension_citing_sec_ripple_action`

**Timestamp**: `2020-12-28 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_corporate`**
  - URL: <https://www.coinbase.com/en-ca/blog/coinbase-will-suspend-trading-in-xrp-on-january-19>
  - body_hash: `sha256:e74df8a12efb71d5a738a46138d3f27cce630d5fcee4f2cc63c91676c7cacd79`
  - body_path: `sources/http_captures/sec-v-ripple-2020/primary/www.coinbase.com__en-ca-blog-coinbase-will-suspend-trading-in-xrp-on-january-19__0087ac7275.html`
  > Coinbase official blog post by Paul Grewal, dated 2020-12-28,
> states that, in light of the SEC's action/lawsuit against Ripple
> Labs, Coinbase would move XRP trading to limit-only and fully
> suspend XRP trading on 2021-01-19 at 10:00 PST. Captured locally
> 2026-06-01 from the current Coinbase canonical blog URL. This
> supports direct attribution for Coinbase's own listing action.

### offramp_cex · attribution: `direct` · Δt = 72h

**Event label**: `bitstamp_announced_xrp_trading_and_deposit_halt_for_us_customers_citing_sec_filing`

**Timestamp**: `2020-12-25 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_corporate`**
  - URL: <https://blog.bitstamp.net/post/xrp-trading-and-deposits-be-halted-us-customers/>
  - body_hash: `sha256:3ce5db1098cc44bdd69d0789c8cf64831997eb016487650b25667f290f7dbc3e`
  - body_path: `sources/http_captures/sec-v-ripple-2020/primary/blog.bitstamp.net__post-xrp-trading-and-deposits-be-halted-us-customers__e9c675f146.html`
  > Bitstamp official blog post dated 2020-12-25 states that, in
> light of the recent SEC filing against Ripple Labs alleging XRP is
> a security, Bitstamp would halt all XRP trading and deposits for
> U.S. customers on 2021-01-08 at 21:00 UTC while preserving
> withdrawals. Captured locally 2026-06-01 from Bitstamp's current
> blog URL. This supports direct attribution for Bitstamp's own
> U.S.-customer trading/deposit restriction.

## 5. Honest coverage gaps

- **l4_frontend** (`not_measured`): The previous row treated a Ripple.com litigation-response page as a

## 7. Related events

- [`sec-v-coinbase-2023`](./sec-v-coinbase-2023.md)
- [`sec-v-binance-2023`](./sec-v-binance-2023.md)
- [`blockfi-sec-lending-2022`](./blockfi-sec-lending-2022.md)
- [`kraken-sec-staking-2023`](./kraken-sec-staking-2023.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `1c9c65c`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

