# Evidence chain — `sec-beaxy-platform-shutdown-2023`

**Status**: `admitted` · **Stratum**: `S3_doj_sec_cftc_fiod` · **Shape**: `comparison` (2 changed layer(s): `l4_frontend`, `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `00764cd` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-16` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "The 2023-03-29 SEC Beaxy action is coded as a Beaxy Platform shutdown plus
> cessation/return obligations at the centralized platform layer; it is not
> coded as network blocking or an on-chain asset freeze."

## 1. Trigger

- **Type**: `sec_action`
- **Actor**: `US_SEC`
- **Timestamp**: `2023-03-29 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://www.sec.gov/newsroom/press-releases/2023-64>
  - body_hash: `sha256:67f588f1cdc68c76bfe1a131bcc7b00a8e1e98e67ca8565f087d62e3a7cee7bb`
  - body_path: `sources/http_captures/sec-beaxy-platform-shutdown-2023/primary/www.sec.gov__newsroom-press-releases-2023-64__47268803d6.html`
  > SEC press release 2023-64 (2023-03-29): Beaxy Platform and executives
> charged for operating as an unregistered exchange, broker, and clearing
> agency; settling parties agreed to shut down the platform.
- **`primary_legal`**
  - URL: <https://www.sec.gov/files/litigation/complaints/2023/comp-pr2023-64.pdf>
  - body_hash: `sha256:e46031492fe74d5513616cbfd9b0a06311a9067d3af69ef11981aeee9eeaed33`
  - body_path: `sources/http_captures/sec-beaxy-platform-shutdown-2023/primary/www.sec.gov__files-litigation-complaints-2023-comp-pr2023-64.pdf__34db79071e.bin`
  > SEC complaint in Securities and Exchange Commission v. Beaxy Digital,
> Ltd., et al., N.D. Ill. No. 1:23-cv-1962.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Beaxy Platform / Windy Inc.
- **Canonical domains**: `beaxy.com`

> Beaxy.com trading platform and related exchange/broker/clearing service.
> The row does not enumerate every listed token or customer account.

## 3. Changed-layer observations (supports the scoped claim)

### l4_frontend · attribution: `direct` · Δt = 0h

**Event label**: `beaxy_platform_shutdown`

**Timestamp**: `2023-03-29 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_legal`**
  - URL: <https://www.sec.gov/newsroom/press-releases/2023-64>
  - body_hash: `sha256:67f588f1cdc68c76bfe1a131bcc7b00a8e1e98e67ca8565f087d62e3a7cee7bb`
  - body_path: `sources/http_captures/sec-beaxy-platform-shutdown-2023/primary/www.sec.gov__newsroom-press-releases-2023-64__47268803d6.html`
  > SEC release states the settling parties agreed to shut down the Beaxy
> Platform.

### offramp_cex · attribution: `direct` · Δt = 0h

**Event label**: `exchange_broker_clearing_activities_ceased_and_customer_assets_returned`

**Timestamp**: `2023-03-29 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_legal`**
  - URL: <https://www.sec.gov/newsroom/press-releases/2023-64>
  - body_hash: `sha256:67f588f1cdc68c76bfe1a131bcc7b00a8e1e98e67ca8565f087d62e3a7cee7bb`
  - body_path: `sources/http_captures/sec-beaxy-platform-shutdown-2023/primary/www.sec.gov__newsroom-press-releases-2023-64__47268803d6.html`
  > SEC release states the undertakings included ceasing unregistered
> exchange, broker, clearing-agency, and dealer activity; accounting for
> assets and funds; and transferring customer assets and funds to
> customers.

## 5. Honest coverage gaps

- **l0_network** (`not_measured`): No L0 measurement slice is retained for this expansion draft.

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `00764cd`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

