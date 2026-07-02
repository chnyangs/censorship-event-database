# Evidence chain — `nigeria-sec-binance-cease-solicitation-2023-07`

**Status**: `admitted` · **Stratum**: `S4_nation_state` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-08` · **Source commit**: `ee7bf1a` · **Schema**: `0.2.0` · **Event last_verified**: `2026-06-08` · **Tool version**: `0.1.0` · **Generated**: `2026-06-25T23:48:26Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "Nigeria's SEC (2023-07-28) ordered Binance to cease soliciting Nigerian
> investors; an off-ramp/market-access restriction (plausible, attested_secondary)."

## 1. Trigger

- **Type**: `regulatory_enforcement`
- **Actor**: `Nigeria Securities and Exchange Commission (SEC)`
- **Timestamp**: `2023-07-28 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`supporting_journalism`**
  - URL: <https://www.coindesk.com/policy/2023/07/31/binances-activities-are-illegal-in-nigeria-securities-regulator-says>
  - body_hash: `sha256:9b414bbfc09b859b9b27450827b2d44df416cb78033737f1a10f4116e931a8d6`
  - body_path: `sources/http_captures/nigeria-sec-binance-cease-solicitation-2023-07/source/www.coindesk.com__policy-2023-07-31-binances-activities-are-illegal-in-nigeria-securities-regulator-says__47223dcc95.html`
  > Captured 2026-06-08 with body_hash; replayable contemporaneous secondary source.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `plausible` · Δt = Noneh

**Event label**: `nigeria_sec_binance_cease_solicitation_2023_07_reaction`

**Timestamp**: `2023-07-28 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`supporting_journalism`**
  - URL: <https://www.coindesk.com/policy/2023/07/31/binances-activities-are-illegal-in-nigeria-securities-regulator-says>
  - body_hash: `sha256:9b414bbfc09b859b9b27450827b2d44df416cb78033737f1a10f4116e931a8d6`
  - body_path: `sources/http_captures/nigeria-sec-binance-cease-solicitation-2023-07/source/www.coindesk.com__policy-2023-07-31-binances-activities-are-illegal-in-nigeria-securities-regulator-says__47223dcc95.html`
  > Off-ramp access restriction documented by the captured contemporaneous secondary source; attribution plausible (no first-party operator/primary statement captured).

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `ee7bf1a`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

