# Evidence chain — `kraken-sec-staking-2023`

**Status**: `admitted` · **Stratum**: `S3_doj_sec_cftc_fiod` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `c3fb0ae` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-16` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "The 2023-02-09 SEC Kraken staking settlement is coded only as a U.S.-scoped
> centralized exchange service shutdown; it does not claim protocol-level
> staking censorship or token delisting."

## 1. Trigger

- **Type**: `sec_action`
- **Actor**: `US_SEC`
- **Timestamp**: `2023-02-09 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://www.sec.gov/newsroom/press-releases/2023-25>
  - body_hash: `sha256:dbcde40b85e3ff9d67c56327cfa5144cb2177688e67541bf1c706097719c3bb2`
  - body_path: `sources/http_captures/kraken-sec-staking-2023/primary/www.sec.gov__newsroom-press-releases-2023-25__60bb01826e.html`
  > SEC press release 2023-25 (2023-02-09): Kraken subsidiaries Payward
> Ventures and Payward Trading agreed to discontinue unregistered
> crypto asset staking-as-a-service offers and sales and pay $30M.
- **`primary_corporate`**
  - URL: <https://blog.kraken.com/news/settlement>
  - body_hash: `sha256:5ee3db50eb12a5d305663c016587b0b3be2c94fbb4e6da470b31101dbeddf41e`
  - body_path: `sources/http_captures/kraken-sec-staking-2023/primary/blog.kraken.com__news-settlement__d26530fc20.html`
  > Kraken's same-day platform statement says U.S. clients would no longer
> be able to stake new assets, enrolled non-ETH assets would be
> automatically unstaked, and those assets would no longer earn staking
> rewards.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Kraken / Payward Ventures and Payward Trading
- **Chains**: `ethereum`, `cardano`, `solana`, `polkadot`
- **Canonical domains**: `kraken.com`

> Kraken U.S. staking service. This is a service-level target, not a token
> delisting or chain-level consensus event.

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `direct` · Δt = 0h

**Event label**: `us_onchain_staking_service_discontinued`

**Timestamp**: `2023-02-09 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_legal`**
  - URL: <https://www.sec.gov/newsroom/press-releases/2023-25>
  - body_hash: `sha256:dbcde40b85e3ff9d67c56327cfa5144cb2177688e67541bf1c706097719c3bb2`
  - body_path: `sources/http_captures/kraken-sec-staking-2023/primary/www.sec.gov__newsroom-press-releases-2023-25__60bb01826e.html`
  > SEC release states the Kraken entities agreed to immediately cease
> offering or selling securities through crypto asset staking services
> or staking programs.
- **`primary_corporate`**
  - URL: <https://blog.kraken.com/news/settlement>
  - body_hash: `sha256:5ee3db50eb12a5d305663c016587b0b3be2c94fbb4e6da470b31101dbeddf41e`
  - body_path: `sources/http_captures/kraken-sec-staking-2023/primary/blog.kraken.com__news-settlement__d26530fc20.html`
  > Kraken says U.S. clients cannot stake new assets and non-ETH assets
> in the on-chain staking program would be automatically unstaked.

## 5. Honest coverage gaps

- **l4_frontend** (`not_measured`): No admission-grade historical frontend diff is retained in this file.

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `c3fb0ae`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

