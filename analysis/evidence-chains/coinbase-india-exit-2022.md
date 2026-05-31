# Evidence chain — `coinbase-india-exit-2022`

**Status**: `admitted` · **Stratum**: `S5_corporate` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `f1c99dd` · **Schema**: `0.2.0` · **Event last_verified**: `2026-04-22` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "Coinbase's 2022-04 India market entry was reversed within days through
> informal regulatory pushback via NPCI, illustrating that even after the
> 2020 Supreme Court IAMAI ruling lifting the direct RBI crypto ban,
> informal financial-rail-level pressure can effectively block major
> US-exchange market access. Documents informal-pressure enforcement mode
> alongside the 2018 RBI formal-prohibition mode."

## 1. Trigger

- **Type**: `corporate_policy_change`
- **Actor**: `coinbase_inc`
- **Timestamp**: `2022-04-07 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_corporate`**
  - URL: <https://www.coinbase.com/en-au/blog>
  - body_hash: `sha256:e6a793e115b6bfb11a6b75fbbc86c7cf7179e94ea13503cf4733c0fd23967fc4`
  - body_path: `sources/http_captures/coinbase-india-exit-2022/primary/blog.coinbase.com__where-coinbase-operates-and-how-we-comply-around-the-world-d2f6bbf53d36__2f3902d770.html`
  > Coinbase corporate blog landing (redirected from the specific
> "where-coinbase-operates-and-how-we-comply-around-the-world"
> Medium-era post URL that has since been re-slugged). Primary corporate
> anchor. Captures the period in which Coinbase India UPI-rail access
> was disabled following pushback from NPCI (National Payments
> Corporation of India). Coinbase had launched India app 2022-04-07
> with UPI-rail deposit/withdrawal; within 3 days NPCI issued a
> statement disowning Coinbase's integration, and UPI support was
> suspended. CEO Brian Armstrong subsequently discussed the sequence
> in a May 2022 earnings call (secondary context).

## 2. Target

- **Kind**: `domain`
- **Enumeration**: `complete`
- **Actor name**: Coinbase Inc (India market)
- **Canonical domains**: `app.coinbase.com`

> Coinbase India consumer product (app.coinbase.com — India-rail
> integration). No on-chain addresses; the target is a regulated-market
> withdrawal by a US exchange from a nation-state market following
> domestic regulatory pushback (NPCI disavowal).

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `direct` · Δt = 72.0h

**Event label**: `india_upi_rail_disabled_within_3d_of_launch`

**Timestamp**: `2022-04-10 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_corporate`**
  - URL: <https://www.coinbase.com/en-au/blog>
  - body_hash: `sha256:e6a793e115b6bfb11a6b75fbbc86c7cf7179e94ea13503cf4733c0fd23967fc4`
  - body_path: `sources/http_captures/coinbase-india-exit-2022/primary/blog.coinbase.com__where-coinbase-operates-and-how-we-comply-around-the-world-d2f6bbf53d36__2f3902d770.html`
  > Coinbase corporate blog anchor documenting Coinbase India market-
> retreat sequence. Specific article re-slugged post-2022; landing
> page is the current canonical anchor. attribution=direct because
> Coinbase (the CEX subject to NPCI pushback) itself made the
> feature-disable decision.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`india-rbi-crypto-ban-2018`](./india-rbi-crypto-ban-2018.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `f1c99dd`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

