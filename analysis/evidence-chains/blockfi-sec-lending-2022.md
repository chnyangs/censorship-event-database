# Evidence chain — `blockfi-sec-lending-2022`

**Status**: `admitted` · **Stratum**: `S3_doj_sec_cftc_fiod` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `a785639` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-16` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T09:36:40Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "The 2022-02-14 SEC BlockFi settlement is coded only as a BlockFi Interest
> Account product/service restriction, not as a frontend, L1, L3, or on-chain
> censorship event."

## 1. Trigger

- **Type**: `sec_action`
- **Actor**: `US_SEC`
- **Timestamp**: `2022-02-14 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://www.sec.gov/newsroom/press-releases/2022-26>
  - body_hash: `sha256:805ea579d1452e64855b30ea674d7e83f960dc40c996dec5b469c24c781bfa01`
  - body_path: `sources/http_captures/blockfi-sec-lending-2022/primary/www.sec.gov__newsroom-press-releases-2022-26__ae4da616fa.html`
  > SEC press release 2022-26 (2022-02-14): BlockFi agreed to penalties
> and to cease unregistered offers and sales of BlockFi Interest Accounts.
- **`primary_legal`**
  - URL: <https://www.sec.gov/litigation/admin/2022/33-11029.pdf>
  - body_hash: `sha256:1f0a57b3706af2a0f94c4ff3fb5e86db2c2cc8f82eab20093350b82304888a3e`
  - body_path: `sources/http_captures/blockfi-sec-lending-2022/primary/www.sec.gov__litigation-admin-2022-33-11029.pdf__19ddea27cd.bin`
  > SEC administrative order for BlockFi Lending LLC. Captured as the
> legal-order anchor for the product-level restriction.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: BlockFi Lending LLC
- **Chains**: `bitcoin`, `ethereum`
- **Canonical domains**: `blockfi.com`

> BlockFi Interest Account product. This is a lending-product/service target,
> not an on-chain address set.

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `direct` · Δt = 0h

**Event label**: `unregistered_interest_account_offers_and_sales_ceased`

**Timestamp**: `2022-02-14 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_legal`**
  - URL: <https://www.sec.gov/newsroom/press-releases/2022-26>
  - body_hash: `sha256:805ea579d1452e64855b30ea674d7e83f960dc40c996dec5b469c24c781bfa01`
  - body_path: `sources/http_captures/blockfi-sec-lending-2022/primary/www.sec.gov__newsroom-press-releases-2022-26__ae4da616fa.html`
  > SEC release states BlockFi agreed to cease unregistered offers and
> sales of the lending product, BlockFi Interest Accounts.
- **`primary_legal`**
  - URL: <https://www.sec.gov/litigation/admin/2022/33-11029.pdf>
  - body_hash: `sha256:1f0a57b3706af2a0f94c4ff3fb5e86db2c2cc8f82eab20093350b82304888a3e`
  - body_path: `sources/http_captures/blockfi-sec-lending-2022/primary/www.sec.gov__litigation-admin-2022-33-11029.pdf__19ddea27cd.bin`
  > Administrative order anchors the settlement obligation and product
> restriction.

## 5. Honest coverage gaps

- **l4_frontend** (`not_measured`): No historical BlockFi frontend diff is retained here. The retained

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `a785639`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

