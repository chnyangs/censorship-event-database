# Evidence chain — `circle-freeze-zama-cusdc-court-order-2026`

**Status**: `admitted` · **Stratum**: `S5_corporate` · **Shape**: `null_event` (0 changed layer(s): none) · **Tier**: `null_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-08` · **Source commit**: `ee7bf1a` · **Schema**: `0.2.0` · **Event last_verified**: `2026-06-08` · **Tool version**: `0.1.0` · **Generated**: `2026-06-25T23:48:26Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "Circle froze Zama's cUSDC (~$12.5M) under an NDCA TRO on ~2026-05-29 and reversed it
> ~2026-06-01; reported by a single secondary source, no tx_hash captured. attested_secondary
> null_case."

## 1. Trigger

- **Type**: `corporate_policy_change`
- **Actor**: `Circle (on TRO from NDCA federal court)`
- **Timestamp**: `2026-05-29 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`supporting_journalism`**
  - URL: <https://www.cryptotimes.io/2026/06/02/court-lifts-freeze-on-zamas-cusdc-contract-restoring-12-5m-usdc/>
  - body_hash: `sha256:56527f13529c94018c8afcad416835d8e605067036fddcf50dec5155757f4b99`
  - body_path: `sources/http_captures/circle-freeze-zama-cusdc-court-order-2026/source/www.cryptotimes.io__2026-06-02-court-lifts-freeze-on-zamas-cusdc-contract-restoring-12-5m-usdc__166d0be9ad.html`
  > Captured 2026-06-08 with body_hash; replayable contemporaneous secondary source
> (CryptoTimes) for the reported freeze and its reversal.

## 2. Target

- **Kind**: `asset`
- **Enumeration**: `subset`

## 3. Changed-layer observations (supports the scoped claim)

*No observed_change entries. This is a `null_event`; see §4 for observed_no_change evidence supporting the null claim.*

## 4. No-change observations (where applicable)

### offramp_cex — `no_public_cex_cascade_documented_in_14d_window`

**Window**: `2026-05-29 00:00:00+00:00` → `2026-06-12 23:59:59+00:00`

**Sources**:

- **`supporting_journalism`**
  - URL: <https://www.cryptotimes.io/2026/06/02/court-lifts-freeze-on-zamas-cusdc-contract-restoring-12-5m-usdc/>
  - body_hash: `sha256:56527f13529c94018c8afcad416835d8e605067036fddcf50dec5155757f4b99`
  - body_path: `sources/http_captures/circle-freeze-zama-cusdc-court-order-2026/source/www.cryptotimes.io__2026-06-02-court-lifts-freeze-on-zamas-cusdc-contract-restoring-12-5m-usdc__166d0be9ad.html`
  > null_event anchor (attested_secondary): CryptoTimes reports Circle froze Zama's cUSDC
> contract under an NDCA TRO (~2026-05-29) and the freeze was lifted ~2026-06-01. No
> primary_onchain tx_hash is captured; per §1.6 no asset_onchain change is claimed.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `ee7bf1a`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

