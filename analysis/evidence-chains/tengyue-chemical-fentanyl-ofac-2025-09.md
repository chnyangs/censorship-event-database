# Evidence chain — `tengyue-chemical-fentanyl-ofac-2025-09`

**Status**: `admitted` · **Stratum**: `S1_ofac_sdn` · **Shape**: `null_event` (0 changed layer(s): none) · **Tier**: `null_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `8e29b8d` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-31` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "The 2025-09-03 OFAC designation of Guangzhou Tengyue Chemical Co. +
> Huang Xiaojun (Treasury sb0235, fentanyl/nitazenes trafficking)
> attached a Bitcoin address (enumerated in the SDN-list entry); native BTC has no issuer freeze
> primitive and no public CEX cascade was pinned in the 14-day window.
> null_case: limited measurable cross-layer surface."

## 1. Trigger

- **Type**: `ofac_sdn_designation`
- **Actor**: `US_OFAC`
- **Timestamp**: `2025-09-03 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://home.treasury.gov/news/press-releases/sb0235>
  - Wayback: <https://web.archive.org/web/20250904044418/https://home.treasury.gov/news/press-releases/sb0235>
  - body_hash: `sha256:b4a273bb22051aab7f78752e0405a3b03e28421dd3b9efe0d20b7c1699abc486`
  - body_path: `sources/http_captures/tengyue-chemical-fentanyl-ofac-2025-09/primary/web.archive.org__web-20250904044418-https-home.treasury.gov-news-press-releases-sb0235__79c9bfd038.html`
  > U.S. Treasury press release sb0235 (2025-09-03): OFAC designated
> Guangzhou Tengyue Chemical Co., Ltd. (China-based) and company
> representatives Huang Xiaojun and Huang Zhanpeng pursuant to
> E.O. 14059 for the international proliferation of illicit drugs
> (fentanyl / nitazenes / precursors) into the United States. The
> SDN entry for Huang Xiaojun lists one Bitcoin address used to
> receive crypto payments (~$1.26M received Jan 2021–Jan 2025).
> Wayback memento 20250904044418 pinned.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Guangzhou Tengyue Chemical Co. + Huang Xiaojun / Huang Zhanpeng
- **Chains**: `bitcoin`

> Guangzhou Tengyue Chemical Co., Ltd. plus representatives Huang
> Xiaojun and Huang Zhanpeng, designated as SDNs. The OFAC entry for
> Huang Xiaojun lists one Bitcoin address. Marked subset because the
> action targets the named persons/entity and a single attached
> address rather than an enumerated complete address set.

## 3. Changed-layer observations (supports the scoped claim)

*No observed_change entries. This is a `null_event`; see §4 for observed_no_change evidence supporting the null claim.*

## 4. No-change observations (where applicable)

### offramp_cex — `no_public_cex_cascade_documented_in_14d_window`

**Window**: `2025-09-03 00:00:00+00:00` → `2025-09-17 23:59:59+00:00`

**Sources**:

- **`primary_legal`**
  - URL: <https://home.treasury.gov/news/press-releases/sb0235>
  - Wayback: <https://web.archive.org/web/20250904044418/https://home.treasury.gov/news/press-releases/sb0235>
  - body_hash: `sha256:b4a273bb22051aab7f78752e0405a3b03e28421dd3b9efe0d20b7c1699abc486`
  - body_path: `sources/http_captures/tengyue-chemical-fentanyl-ofac-2025-09/primary/web.archive.org__web-20250904044418-https-home.treasury.gov-news-press-releases-sb0235__79c9bfd038.html`
  > No public CEX policy statement referencing the Guangzhou
> Tengyue / Huang Xiaojun designation was pinned in the 14-day
> post-designation window in this authoring pass. Records the
> absence of pinned public disclosure; private KYT flagging is
> outside scope. The on-chain footprint is a single native-BTC
> address (no issuer freeze primitive), limiting the measurable
> cross-layer surface.

## 5. Honest coverage gaps

- **asset_onchain** (`not_measured`): One Bitcoin address is attached to the Huang Xiaojun SDN entry, but

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `8e29b8d`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

