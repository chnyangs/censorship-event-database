# Evidence chain — `binance-us-staking-end-2023`

**Status**: `admitted` · **Stratum**: `S5_corporate` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-05-31` · **Source commit**: `c87d162` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-16` · **Tool version**: `0.1.0` · **Generated**: `2026-05-31T14:17:25Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "The 2023-06-09 Binance.US autonomous discontinuation of its staking-as-
> a-service product, announced four days after the SEC v. Binance complaint
> but executed as an autonomous corporate-policy decision rather than a
> regulator-ordered cessation, produced a single-layer cascade at the
> offramp_cex surface: the U.S.-scoped Binance.US pooled-staking product
> was withdrawn. The row asserts only this offramp_cex observation and
> does not claim L0 network, L1 consensus, L3 RPC, L4 frontend
> delisting/geofence, or asset_onchain issuer-freeze effects. The
> autonomous-vs-forced distinction relative to kraken-sec-staking-2023
> (regulator-ordered twin) is the load-bearing analytical contribution."

## 1. Trigger

- **Type**: `corporate_policy_change`
- **Actor**: `binance_us`
- **Timestamp**: `2023-06-09 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_corporate`**
  - URL: <https://blog.binance.us/end-of-staking-services-on-binance-us/>
  - Wayback: <https://web.archive.org/web/2023/https://blog.binance.us/end-of-staking-services-on-binance-us/>
  > Binance.US corporate blog post (2023-06-09): "End of Staking Services
> on Binance.US." Announces the discontinuation of Binance.US staking
> services across all supported assets, with users directed to unstake
> positions and re-custody assets in spot wallets ahead of the
> sunsetting timeline. The announcement was issued four days after the
> 2023-06-05 SEC v. Binance complaint (sec-v-binance-2023), which named
> Binance Simple Earn, BNB Vault, BUSD staking-product, and BETH as
> unregistered securities offerings against Binance Holdings / BAM
> Trading. Binance.US framed the staking-service shutdown as an
> autonomous corporate-policy decision rather than a regulator-ordered
> cessation; no consent decree, settlement agreement, or court order
> compelled the staking-service withdrawal at the 2023-06-09 timestamp.
> This contrasts structurally with the kraken-sec-staking-2023 twin
> (2023-02-09), where the SEC press release and Kraken platform
> statement co-locate a settlement-ordered staking-service shutdown.
> Marked evidence_use=contextual_unarchived because in this DRYRUN the
> authoring LLM agent did not personally pin a Wayback snapshot
> timestamp or compute a body_hash; the blog.binance.us URL is routinely
> captured by Wayback in 2023 and remains the canonical corporate
> anchor. Pinned snapshot timestamp + body_hash to be re-anchored
> during human audit before this citation may serve as an admission
> anchor in its own right.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Binance.US / BAM Trading Services Inc.
- **Canonical domains**: `binance.us`, `blog.binance.us`

> Binance.US (BAM Trading Services Inc.) staking-as-a-service product
> surface. Service-level target covering the pooled-staking offering
> across all supported assets on the Binance.US platform; not a token
> delisting, not a chain-level consensus event, not a global Binance.com
> staking product (Binance.US is the U.S.-scoped BAM-operated affiliate
> and remained legally and operationally distinct from binance.com in
> 2023).

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `direct` · Δt = 0h

**Event label**: `us_cex_staking_service_discontinued_autonomous`

**Timestamp**: `2023-06-09 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_corporate`**
  - URL: <https://blog.binance.us/end-of-staking-services-on-binance-us/>
  - Wayback: <https://web.archive.org/web/2023/https://blog.binance.us/end-of-staking-services-on-binance-us/>
  > Binance.US corporate blog hosted the 2023-06-09 staking-service
> shutdown announcement. attribution=direct because the Binance.US
> frontend / corporate-blog announcement is the canonical instrument
> executing the staking-service product withdrawal; the corporate
> decision and the staking-service shutdown are co-located in the
> same corporate actor (BAM Trading Services Inc. / Binance.US).
> The SEC v. Binance complaint (2023-06-05, sec-v-binance-2023) is
> the plausible upstream pressure four days prior, but the proximate
> legal instrument here is the Binance.US unilateral corporate-
> policy announcement, not a settlement-ordered cessation. Wayback
> wildcard pointer in lieu of a pinned-timestamp snapshot;
> evidence_use=contextual_unarchived pending human-audit re-pin.

## 5. Honest coverage gaps

- **l4_frontend** (`not_measured`): No admission-grade historical frontend diff is retained in this file.

## 7. Related events

- [`kraken-sec-staking-2023`](./kraken-sec-staking-2023.md)
- [`sec-v-binance-2023`](./sec-v-binance-2023.md)
- [`binance-4framework-2023`](./binance-4framework-2023.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `c87d162`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

