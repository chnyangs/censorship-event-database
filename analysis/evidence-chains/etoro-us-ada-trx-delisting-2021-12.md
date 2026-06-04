# Evidence chain — `etoro-us-ada-trx-delisting-2021-12`

**Status**: `admitted` · **Stratum**: `S5_corporate` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-02` · **Source commit**: `f54a8ae` · **Schema**: `0.2.0` · **Event last_verified**: `2026-06-01` · **Tool version**: `0.1.0` · **Generated**: `2026-06-04T09:44:11Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "eToro's 2021-12-26 removal of US-customer access to Cardano (ADA) and
> Tron (TRX) — no new positions, staking removed, citing the evolving US
> regulatory environment — severed the eToro brokerage off-ramp for these
> assets for US users; single-layer offramp_cex observed_change,
> attribution=direct for eToro's own access limitation (the regulatory
> rationale is generic context, not a named order)."

## 1. Trigger

- **Type**: `corporate_policy_change`
- **Actor**: `etoro`
- **Timestamp**: `2021-11-23 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_corporate`**
  - URL: <https://www.etoro.com/en-us/news-and-analysis/etoro-updates/important-update-regarding-ada-and-trx/>
  - Wayback: <https://web.archive.org/web/20211124005443/https://www.etoro.com/en-us/news-and-analysis/etoro-updates/important-update-regarding-ada-and-trx/>
  - body_hash: `sha256:708cafdf381ecc0a944adce3d02eca6a4630f9c1f7045828a0ea7bde6567a547`
  - body_path: `sources/http_captures/etoro-us-ada-trx-delisting-2021-12/official-etoro-20211124/web.archive.org__web-20211124005443-https-www.etoro.com-en-us-news-and-analysis-etoro-updates-important-update-regarding-ada-and-trx__e5607995f5.html`
  > eToro first-party update, Wayback memento 2021-11-24 00:54:43
> UTC. The captured page is titled "Important update regarding ADA
> and TRX" and records publication on 2021-11-23. It states that
> US users would no longer be able to open new Cardano (ADA) or
> TRON (TRX) positions from 2021-12-26, that staking for those
> assets would end on 2021-12-31, and that the changes were due
> to business-related considerations in the evolving regulatory
> environment.
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

### offramp_cex · attribution: `direct` · Δt = Noneh

**Event label**: `etoro_removes_us_customer_access_to_ada_trx`

**Timestamp**: `2021-12-26 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_corporate`**
  - URL: <https://www.etoro.com/en-us/news-and-analysis/etoro-updates/important-update-regarding-ada-and-trx/>
  - Wayback: <https://web.archive.org/web/20211124005443/https://www.etoro.com/en-us/news-and-analysis/etoro-updates/important-update-regarding-ada-and-trx/>
  - body_hash: `sha256:708cafdf381ecc0a944adce3d02eca6a4630f9c1f7045828a0ea7bde6567a547`
  - body_path: `sources/http_captures/etoro-us-ada-trx-delisting-2021-12/official-etoro-20211124/web.archive.org__web-20211124005443-https-www.etoro.com-en-us-news-and-analysis-etoro-updates-important-update-regarding-ada-and-trx__e5607995f5.html`
  > eToro first-party update: US users would no longer be able to
> open new ADA or TRX positions starting 2021-12-26, staking for
> both assets would end on 2021-12-31, and final staking rewards
> would be paid on 2022-01-15. attribution=direct for eToro's
> own US-customer ADA/TRX access limitation; the regulatory
> rationale remains scoped to eToro's generic "evolving
> regulatory environment" language, not a named US order.
- **`semi_primary_wayback`**
  - URL: <https://www.newsbtc.com/news/cardano/etoro-announces-cardano-ada-and-tron-trx-delisting-points-to-regulatory-concerns/>
  - Wayback: <https://web.archive.org/web/20250617083522/https://www.newsbtc.com/news/cardano/etoro-announces-cardano-ada-and-tron-trx-delisting-points-to-regulatory-concerns/>
  - body_hash: `sha256:bd4e428548456eb5bfe69c831125cae7fea120dd4ef9e2b39261b3d901b68c40`
  - body_path: `sources/http_captures/etoro-us-ada-trx-delisting-2021-12/primary/web.archive.org__web-20250617083522-https-www.newsbtc.com-news-cardano-etoro-announces-cardano-ada-and-tron-trx-delisting-points-to-regulatory-concerns__9e6c9d8a83.html`
  > NewsBTC: eToro to remove US-customer access to ADA and TRX on
> 2021-12-26 (no new positions; staking removed), citing the
> evolving regulatory environment. Retained as corroborating
> contemporaneous coverage; the first-party eToro capture added on
> 2026-06-01 supersedes the earlier lower-tier source posture.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`sec-etoro-cease-crypto-trading-2024-09`](./sec-etoro-cease-crypto-trading-2024-09.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `f54a8ae`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

