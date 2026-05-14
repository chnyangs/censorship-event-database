# Evidence chain — `funnull-cdn-ofac-2025`

**Status**: `admitted` · **Stratum**: `S1_ofac_sdn` · **Shape**: `comparison` (1 changed layer(s): `asset_onchain`) · **Tier**: `empirical_case`

**Dataset version**: `0.1.0` · **Dataset cutoff**: `2026-05-06` · **Source commit**: `5b59b99` · **Schema**: `0.2.0` · **Event last_verified**: `2026-04-22` · **Tool version**: `0.1.0` · **Generated**: `2026-05-08T02:57:52Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "OFAC designation of Funnull CDN on 2025-05-29 attached 2 addresses (ETH + TRX). Four
> canonical domains are available for L4 bracketing; Wayback snapshots pending."

## 1. Trigger

- **Type**: `ofac_sdn_designation`
- **Actor**: `US_OFAC`
- **Timestamp**: `2025-05-29 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://ofac.treasury.gov/recent-actions/20250529>
  - Wayback: <https://web.archive.org/web/20260421144036/https://ofac.treasury.gov/recent-actions/20250529>
  - body_hash: `sha256:4c139e31ffb1c6979e073bd9329234447d50085c09f87dea2879f54555537fe5`
  - body_path: `sources/http_captures/funnull-cdn-ofac-2025/ofac-recent-actions/ofac.treasury.gov__recent-actions-20250529__bf3d7f6173.html`
  > OFAC Recent Actions page for 2025-05-29. FUNNULL (a.k.a. 方能 CDN, FUNNULL CDN, FUNNULL
> INC, FUNNULL LLC), Philippines-registered Chinese-linked CDN / hosting network
> accused of facilitating pig-butchering scams. Multiple websites: funnull.io,
> funnull.com, funnull.app, funnull.buzz. 1 ETH + 1 TRX address attached.
- **`primary_legal`**
  - URL: <https://home.treasury.gov/news/press-releases/sb0144>
  > Treasury press release "Treasury Takes Action Against Major Cyber Scam Facilitator" (2025-05-29).

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Protocol**: `funnull_cdn`
- **Actor name**: Funnull CDN
- **Chains**: `ethereum`, `tron`
- **Addresses**: 2 total (enumerated in event YAML)
- **Canonical domains**: `funnull.io`, `funnull.com`, `funnull.app`, `funnull.buzz`

> 2 digital-currency addresses (ETH + TRX) attached to FUNNULL CDN entity. Entity-level target with 4 named canonical domains.

## 3. Changed-layer observations (supports the scoped claim)

### asset_onchain · attribution: `direct` · Δt = 7.78h

**Event label**: `circle_usdc_blacklist_same_day`

**Timestamp**: `2025-05-29 07:47:00+00:00` (precision: `minute`)

**Sources**:

- **`primary_onchain`**
  - URL: <https://etherscan.io/tx/0x820504809ed1b810498c28dc2fc5fbeb1d753bb5b655ebe83d98cd999c96d2d7>
  - tx_hash: `0x820504809ed1b810498c28dc2fc5fbeb1d753bb5b655ebe83d98cd999c96d2d7`
  > USDC Blacklisted() tx for Funnull ETH address 0xd5ED34b5... at 2025-05-29 07:47 UTC — same day as OFAC designation.
- **`primary_corporate`**
  - URL: <https://usdtbanlist.com/address/0xd5ED34b52AC4ab84d8FA8A231a3218bbF01Ed510>
  - body_hash: `sha256:f08903f1350623e05457f8a561321c8aa3c88ccd71ec04d522c72a00e473a890`
  - body_path: `sources/http_captures/funnull-cdn-ofac-2025/asset-layer-check/usdtbanlist.com__address-0xd5ED34b52AC4ab84d8FA8A231a3218bbF01Ed510.html`
  > usdtbanlist.com community tracker anchor.

### asset_onchain · attribution: `direct` · Δt = 10.25h

**Event label**: `tether_usdt_same_day_eth_and_tron`

**Timestamp**: `2025-05-29 10:15:00+00:00` (precision: `minute`)

**Sources**:

- **`primary_onchain`**
  - URL: <https://etherscan.io/tx/0xd0d30630d1588780f0eda7647a884fb97aed7c5957833599b4754a212280f282>
  - tx_hash: `0xd0d30630d1588780f0eda7647a884fb97aed7c5957833599b4754a212280f282`
  > Tether USDT addBlackList tx for ETH address at 2025-05-29 10:15 UTC. Paired with TRON freeze of 4c0606f5... at 2025-05-29 22:12 UTC.
- **`primary_corporate`**
  - URL: <https://usdtbanlist.com/address/TNmRfnSUXZoWWzxcDDbf95eGQYXt1mJDt8>
  - body_hash: `sha256:8e1729352a755bc5c63efc300f58068bed63e03aa533c507ab7acb408266e9d2`
  - body_path: `sources/http_captures/funnull-cdn-ofac-2025/asset-layer-check/usdtbanlist.com__address-TNmRfnSUXZoWWzxcDDbf95eGQYXt1mJDt8.html`
  > Tron-address archival anchor for the cross-chain Tether action.

## 4. No-change observations (where applicable)

### l1_consensus — `censoring_share_already_zero_post_tornado_delisting_null_shape`

**Window**: `2025-05-15 00:00:00+00:00` → `2025-06-12 23:59:59+00:00`

**Sources**:

- **`semi_primary_measurement`**
  - URL: <https://raw.githubusercontent.com/nerolation/censorship.pics/main/data/relay_censorship_share.csv>
  - body_hash: `sha256:45c1db9ca70491743e2e33c313d7293eed791a82d0ea7313c5241eca9e8b4567`
  - body_path: `sources/l1_datasets/tornado-cash-ofac-2022/relay_censorship_share.csv`
  > Slice [2025-05-15, 2025-06-12]: 58 rows. Censoring-relay share
> all zeros throughout — the Wahrstätter classifier (keyed to
> Tornado Cash SDN addresses) collapsed to 0% after the 2025-03-21
> Tornado delisting. By 2025-05-29 (Funnull designation) there was
> no residual censoring-relay signal to perturb. Structurally
> interesting: the classifier itself is a function of Tornado's SDN
> status; post-delisting the metric loses its subject. Any L1
> observation of a post-2025-03-21 event against this dataset will
> produce a zero baseline.
- **`semi_primary_measurement`**
  - URL: <https://www.relayscan.io>
  - Wayback: <https://web.archive.org/web/20260421114750/https://www.relayscan.io/>
  - body_hash: `sha256:dc39f55922c657cd3caf22cdd77287f707ddec63ec0510091532f5fadc7aa827`
  - body_path: `sources/http_captures/tornado-cash-ofac-2022/l1-relay-dashboards/www.relayscan.io__capture__1a79bf8cec.html`
  > Relayscan independent dashboard — second source consistent with
> the zero-baseline observation post-Tornado-delisting.

## 5. Honest coverage gaps

- **l0_network** (`not_measured`): L0 network-layer OONI API query performed 2026-04-22. Searched the
- **l3_rpc** (`not_measured`): No pinned RPC-provider rejection, docs/status change, or
- **l4_frontend** (`not_measured`): 4 canonical domains; Wayback bracketing not yet fetched in the current release.
- **offramp_cex** (`not_measured`): Chain-analytics anchors pinned 2026-04-22 as primary_corporate

## 8. How to audit this chain

1. Clone the repository at tag `v0.1.0` (commit `5b59b99`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

