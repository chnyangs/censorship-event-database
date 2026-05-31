# Evidence chain — `etoro-us-ada-trx-delisting-2021-12`

**Status**: `admitted` · **Stratum**: `S5_corporate` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `dbf5e31` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-31` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "eToro's 2021-12-26 removal of US-customer access to Cardano (ADA) and
> Tron (TRX) — no new positions, staking removed, citing the evolving US
> regulatory environment — severed the eToro brokerage off-ramp for these
> assets for US users; single-layer offramp_cex observed_change,
> attribution=plausible (generic 'regulatory concerns', no named order)."

## 1. Trigger

- **Type**: `corporate_policy_change`
- **Actor**: `etoro`
- **Timestamp**: `2021-11-23 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`semi_primary_wayback`**
  - URL: <https://www.newsbtc.com/news/cardano/etoro-announces-cardano-ada-and-tron-trx-delisting-points-to-regulatory-concerns/>
  - Wayback: <https://web.archive.org/web/20250617083522/https://www.newsbtc.com/news/cardano/etoro-announces-cardano-ada-and-tron-trx-delisting-points-to-regulatory-concerns/>
  - body_hash: `sha256:bd4e428548456eb5bfe69c831125cae7fea120dd4ef9e2b39261b3d901b68c40`
  - body_path: `sources/http_captures/etoro-us-ada-trx-delisting-2021-12/primary/web.archive.org__web-20250617083522-https-www.newsbtc.com-news-cardano-etoro-announces-cardano-ada-and-tron-trx-delisting-points-to-regulatory-concerns__9e6c9d8a83.html`
  > NewsBTC (announced 2021-11-23 per the Wayback capture banner
> "23 Nov 2021"): eToro will "no longer offer access to these digital
> assets [Cardano (ADA) and Tron (TRX)] for users in the United
> States on December 26th, 2021" and "will also remove staking
> features for US users for both Cardano (ADA) and [TRX]", citing the
> evolving regulatory environment. Wayback 20250617083522 pinned;
> the US-only December 26 2021 cutoff and staking removal are
> grep-verified in the captured body.

## 2. Target

- **Kind**: `asset`
- **Enumeration**: `complete`
- **Actor name**: Cardano (ADA) + Tron (TRX) on eToro for US users
- **Chains**: `cardano`, `tron`

> Two assets delisted for US users on eToro: Cardano (ADA) and Tron
> (TRX). Complete enumeration of the affected asset set; the action
> removes US-customer access (no new positions, staking removed) on the
> eToro brokerage off-ramp, not the underlying chains.

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `plausible` · Δt = Noneh

**Event label**: `etoro_removes_us_customer_access_to_ada_trx`

**Timestamp**: `2021-12-26 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`semi_primary_wayback`**
  - URL: <https://www.newsbtc.com/news/cardano/etoro-announces-cardano-ada-and-tron-trx-delisting-points-to-regulatory-concerns/>
  - Wayback: <https://web.archive.org/web/20250617083522/https://www.newsbtc.com/news/cardano/etoro-announces-cardano-ada-and-tron-trx-delisting-points-to-regulatory-concerns/>
  - body_hash: `sha256:bd4e428548456eb5bfe69c831125cae7fea120dd4ef9e2b39261b3d901b68c40`
  - body_path: `sources/http_captures/etoro-us-ada-trx-delisting-2021-12/primary/web.archive.org__web-20250617083522-https-www.newsbtc.com-news-cardano-etoro-announces-cardano-ada-and-tron-trx-delisting-points-to-regulatory-concerns__9e6c9d8a83.html`
  > NewsBTC: eToro to remove US-customer access to ADA and TRX on
> 2021-12-26 (no new positions; staking removed), citing the
> evolving regulatory environment. attribution=plausible: the
> delisting and its US-only scope are directly observed and eToro
> cited "regulatory concerns" generically, but no named US
> regulatory order designates ADA/TRX, so the securities-regulatory
> motive is class-level contextual inference (§1.1), not a
> per-target stated cause.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`sec-etoro-cease-crypto-trading-2024-09`](./sec-etoro-cease-crypto-trading-2024-09.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `dbf5e31`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

