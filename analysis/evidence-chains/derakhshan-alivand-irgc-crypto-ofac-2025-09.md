# Evidence chain — `derakhshan-alivand-irgc-crypto-ofac-2025-09`

**Status**: `admitted` · **Stratum**: `S1_ofac_sdn` · **Shape**: `null_event` (0 changed layer(s): none) · **Tier**: `null_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `97f1e7e` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-31` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T10:19:59Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "The 2025-09-16 OFAC designation of the Derakhshan / Alivand Iranian
> shadow-banking network (Treasury sb0248, IRGC-QF / MODAFL crypto
> facilitation) attached cryptocurrency addresses (the SDN entries
> enumerate the largely-USDT set); no per-address
> on-chain freeze receipt or public CEX cascade was pinned in the 14-day
> window. null_case: cross-layer surface deferred for a draft."

## 1. Trigger

- **Type**: `ofac_sdn_designation`
- **Actor**: `US_OFAC`
- **Timestamp**: `2025-09-16 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://home.treasury.gov/news/press-releases/sb0248>
  - Wayback: <https://web.archive.org/web/20250917232322/https://home.treasury.gov/news/press-releases/sb0248>
  - body_hash: `sha256:96de8a340095a2c177c4c798ffe3a930db682b45229a791087af70b2372d1f45`
  - body_path: `sources/http_captures/derakhshan-alivand-irgc-crypto-ofac-2025-09/primary/web.archive.org__web-20250917232322-https-home.treasury.gov-news-press-releases-sb0248__a24adc46a8.html`
  > U.S. Treasury press release sb0248 (2025-09-16): OFAC designated
> an Iranian shadow-banking / financial-facilitator network,
> including Iranian nationals Alireza Derakhshan and Arash Estaki
> Alivand, plus Hong Kong- and UAE-based front companies, for
> coordinating cryptocurrency funds transfers (incl. proceeds of
> Iranian oil sales) benefiting the IRGC-Qods Force and MODAFL.
> Crypto addresses associated with Derakhshan and Alivand (largely
> USDT) are listed on the SDN entries. Wayback memento
> 20250917232322 pinned.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Derakhshan / Alivand Iranian shadow-banking network
- **Chains**: `ethereum`, `tron`

> Iranian financial facilitators Alireza Derakhshan and Arash Estaki
> Alivand plus a network of Hong Kong- and UAE-based front companies
> and individuals, designated as SDNs with associated crypto (largely
> USDT) addresses. Marked subset because the action targets the named
> facilitator network rather than an exhaustively enumerated complete
> address set captured in this pass.

## 3. Changed-layer observations (supports the scoped claim)

*No observed_change entries. This is a `null_event`; see §4 for observed_no_change evidence supporting the null claim.*

## 4. No-change observations (where applicable)

### offramp_cex — `no_public_cex_cascade_documented_in_14d_window`

**Window**: `2025-09-16 00:00:00+00:00` → `2025-09-30 23:59:59+00:00`

**Sources**:

- **`primary_legal`**
  - URL: <https://home.treasury.gov/news/press-releases/sb0248>
  - Wayback: <https://web.archive.org/web/20250917232322/https://home.treasury.gov/news/press-releases/sb0248>
  - body_hash: `sha256:96de8a340095a2c177c4c798ffe3a930db682b45229a791087af70b2372d1f45`
  - body_path: `sources/http_captures/derakhshan-alivand-irgc-crypto-ofac-2025-09/primary/web.archive.org__web-20250917232322-https-home.treasury.gov-news-press-releases-sb0248__a24adc46a8.html`
  > No public CEX policy statement referencing the Derakhshan /
> Alivand designation was pinned in the 14-day post-designation
> window in this authoring pass. Records the absence of pinned
> public disclosure; private KYT flagging is outside scope. The
> asset-layer (USDT-issuer freeze) response is the natural
> experiment but is not yet captured.

## 5. Honest coverage gaps

- **asset_onchain** (`not_measured`): The SDN entries list crypto addresses (largely USDT) associated

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `97f1e7e`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

