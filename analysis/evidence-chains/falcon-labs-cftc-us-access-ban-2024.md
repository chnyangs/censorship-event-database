# Evidence chain — `falcon-labs-cftc-us-access-ban-2024`

**Status**: `admitted` · **Stratum**: `S3_doj_sec_cftc_fiod` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-08` · **Source commit**: `ee7bf1a` · **Schema**: `0.2.0` · **Event last_verified**: `2026-06-08` · **Tool version**: `0.1.0` · **Generated**: `2026-06-25T23:48:26Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "The CFTC's 2024 order barred Falcon Labs from giving U.S. persons access to
> digital-asset derivatives platforms; an off-ramp access restriction (direct,
> primary_government)."

## 1. Trigger

- **Type**: `cftc_action`
- **Actor**: `CFTC`
- **Timestamp**: `2024-05-13 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_government`**
  - URL: <https://www.cftc.gov/PressRoom/PressReleases/8909-24>
  - body_hash: `sha256:5b3d4aaa1ddfce44aacd5c80eb85c89437453ebc2718606215dcb5dff8418d0e`
  - body_path: `sources/http_captures/falcon-labs-cftc-us-access-ban-2024/source/www.cftc.gov__PressRoom-PressReleases-8909-24__3cd34ddae4.html`
  > Captured 2026-06-08 with body_hash; replayable local primary for the action.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `direct` · Δt = Noneh

**Event label**: `falcon_labs_cftc_us_access_ban_2024_reaction`

**Timestamp**: `2024-05-13 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_government`**
  - URL: <https://www.cftc.gov/PressRoom/PressReleases/8909-24>
  - body_hash: `sha256:5b3d4aaa1ddfce44aacd5c80eb85c89437453ebc2718606215dcb5dff8418d0e`
  - body_path: `sources/http_captures/falcon-labs-cftc-us-access-ban-2024/source/www.cftc.gov__PressRoom-PressReleases-8909-24__3cd34ddae4.html`
  > Captured primary source documents the offramp-layer restriction; attribution direct.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `ee7bf1a`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

