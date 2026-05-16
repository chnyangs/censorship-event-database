# Evidence chain — `cftc-v-ooki-dao-2022`

**Status**: `admitted` · **Stratum**: `S3_doj_sec_cftc_fiod` · **Shape**: `comparison` (1 changed layer(s): `l4_frontend`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-4` · **Dataset cutoff**: `2026-05-16` · **Source commit**: `a0d61e2` · **Schema**: `0.2.0` · **Event last_verified**: `2026-04-22` · **Tool version**: `0.1.0` · **Generated**: `2026-05-20T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "CFTC v. Ooki DAO (2022-09-22 filing; 2023-06-08 default judgment) is
> the first and only CFTC enforcement action against a DAO in the
> dataset. Default judgment mandated US-user frontend geo-blocking with
> the on-chain protocol remaining functional, demonstrating the
> frontend/protocol split under DAO-as-legal-person enforcement."

## 1. Trigger

- **Type**: `cftc_action`
- **Actor**: `US_CFTC`
- **Timestamp**: `2022-09-22 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://www.cftc.gov/PressRoom/PressReleases/8590-22>
  - body_hash: `sha256:a241fc6b6dc9ff3a73c8a9a39fe49032c591a62ca4c84841521b532c26f0ed3d`
  - body_path: `sources/http_captures/cftc-v-ooki-dao-2022/primary/www.cftc.gov__PressRoom-PressReleases-8590-22__bd77d22b3b.html`
  > CFTC press release 8590-22 (2022-09-22): "CFTC Imposes $250,000
> Penalty Against bZeroX, LLC and Its Founders and Charges Successor
> Ooki DAO for Offering Illegal, Off-Exchange Digital-Asset Trading,
> Registration Violations, and Failing to Comply with Bank Secrecy
> Act." Historic action: **first CFTC enforcement action against a
> DAO as a legal person**. Served via the Ooki DAO Help Chat Box
> (accepted as service of process). Charges include offering
> illegal leveraged retail commodity transactions, failing to
> register as FCM/DCO, and BSA/AML violations. Default judgment
> entered 2023-06-08 (Judge Orrick, N.D. Cal).

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `complete`
- **Protocol**: `ooki_protocol`
- **Actor name**: Ooki DAO (formerly bZeroX)
- **Canonical domains**: `ooki.com`, `app.ooki.com`

> Ooki DAO (as legal person) + bZeroX LLC (predecessor entity) +
> co-founders Tom Bean and Kyle Kistner (individuals). No on-chain
> addresses in the CFTC filing — the action targets the DAO-as-person
> legal theory rather than specific addresses. Ooki Protocol smart
> contracts remained on-chain and functional despite the legal action
> against the DAO.

## 3. Changed-layer observations (supports the scoped claim)

### l4_frontend · attribution: `direct` · Δt = 6192.0h

**Event label**: `cftc_enforced_frontend_geo_blocking_us_via_default_judgment`

**Timestamp**: `2023-06-08 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_legal`**
  - URL: <https://www.cftc.gov/PressRoom/PressReleases/8590-22>
  - body_hash: `sha256:a241fc6b6dc9ff3a73c8a9a39fe49032c591a62ca4c84841521b532c26f0ed3d`
  - body_path: `sources/http_captures/cftc-v-ooki-dao-2022/primary/www.cftc.gov__PressRoom-PressReleases-8590-22__bd77d22b3b.html`
  > CFTC primary filing document. Default judgment 2023-06-08 (258 days
> post-CFTC-filing) ordered cessation of Ooki DAO's activities,
> shutdown of US-user frontend access, and $643,542 monetary penalty.
> Direct attribution: the default judgment explicitly mandated US
> user frontend geo-blocking.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-4` (commit `a0d61e2`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

