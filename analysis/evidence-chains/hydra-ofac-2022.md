# Evidence chain — `hydra-ofac-2022`

**Status**: `admitted` · **Stratum**: `S1_ofac_sdn` · **Shape**: `comparison` (1 changed layer(s): `l4_frontend`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `210aa10` · **Schema**: `0.2.0` · **Event last_verified**: `2026-04-21` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T04:23:47Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "OFAC designation of Hydra Market on 2022-04-05 (parallel to German BKA
> takedown) documents a Tor-hidden-service darknet-market removal with
> 120+ address enumeration. L4 onion frontend was seized by BKA same day
> (direct attribution), while asset-layer cascade was absent because
> XBT-only targets have no stablecoin-issuer freeze primitive."

## 1. Trigger

- **Type**: `ofac_sdn_designation`
- **Actor**: `US_OFAC`
- **Timestamp**: `2022-04-05 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://ofac.treasury.gov/recent-actions/20220405>
  - Wayback: <https://web.archive.org/web/20260421105315/https://ofac.treasury.gov/recent-actions/20220405>
  - body_hash: `sha256:ec142cf1769df2bcd14d092b808673b0c5f2d3d643d0cc4590d76aafc3cb87ec`
  - body_path: `sources/http_captures/hydra-ofac-2022/backfill-1.3/ofac.treasury.gov__recent-actions-20220405__594c05f6bc.html`
  > OFAC Recent Actions entry for the 2022-04-05 Hydra Market designation
- **`primary_legal`**
  - URL: <https://home.treasury.gov/news/press-releases/jy0701>
  - Wayback: <https://web.archive.org/web/20260421105351/https://home.treasury.gov/news/press-releases/jy0701>
  - body_hash: `sha256:c89cf47b10bfcbc59e21337ede7ffbe862daadee7544b32f927aab1778d0e398`
  - body_path: `sources/http_captures/hydra-ofac-2022/backfill-1.3/home.treasury.gov__news-press-releases-jy0701__1d13c92377.html`
  > Treasury press release announcing sanctions on Hydra and Garantex

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `complete`
- **Chains**: `bitcoin`
- **Canonical domains**: `hydram6esdjf6otepmr5c3vjyndsoddz22afphbbjznwb5ln2c6op7ad.onion`, `hydraclubbioknikokex7njhwuahc2l67lfiz7z36md2jvopda7nchid.onion`

> Single named entity (Hydra Market) fully specified; onion-address set is included under canonical_domains but is not claimed to be the complete SDN-listed set.

## 3. Changed-layer observations (supports the scoped claim)

### l4_frontend · attribution: `direct` · Δt = Noneh

**Event label**: `marketplace_disrupted_or_unavailable`

**Timestamp**: `2022-04-05 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_legal`**
  - URL: <https://home.treasury.gov/news/press-releases/jy0701>
  - Wayback: <https://web.archive.org/web/20260421105351/https://home.treasury.gov/news/press-releases/jy0701>
  - body_hash: `sha256:c89cf47b10bfcbc59e21337ede7ffbe862daadee7544b32f927aab1778d0e398`
  - body_path: `sources/http_captures/hydra-ofac-2022/backfill-1.3/home.treasury.gov__news-press-releases-jy0701__1d13c92377.html`
  > Treasury states German authorities shut down Hydra servers in Germany on the same day
- **`primary_legal`**
  - URL: <https://ofac.treasury.gov/recent-actions/20220405>
  - Wayback: <https://web.archive.org/web/20260421105315/https://ofac.treasury.gov/recent-actions/20220405>
  - body_hash: `sha256:ec142cf1769df2bcd14d092b808673b0c5f2d3d643d0cc4590d76aafc3cb87ec`
  - body_path: `sources/http_captures/hydra-ofac-2022/backfill-1.3/ofac.treasury.gov__recent-actions-20220405__594c05f6bc.html`
  > OFAC designation lists Hydra Market and associated onion addresses

## 5. Honest coverage gaps

- **l0_network** (`not_measured`): Onion-service and jurisdictional access effects have not been queried against Censored Planet / OONI for this event; eligible jurisdictions include RU, DE but no measurement artifact is attached
- **asset_onchain** (`not_measured`): Associated addresses are listed, but no issuer-freeze evidence has been attached yet
- **offramp_cex** (`not_measured`): Chain-analytics anchors pinned 2026-04-22 as primary_corporate

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `210aa10`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

