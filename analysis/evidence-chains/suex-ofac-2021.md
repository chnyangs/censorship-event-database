# Evidence chain — `suex-ofac-2021`

**Status**: `admitted` · **Stratum**: `S1_ofac_sdn` · **Shape**: `comparison` (1 changed layer(s): `asset_onchain`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `4b6ca9a` · **Schema**: `0.2.0` · **Event last_verified**: `2026-04-21` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T01:54:35Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "OFAC designation of SUEX OTC on 2021-09-21 — the first
> exchange-level crypto sanction — did not disrupt the canonical suex.io frontend within a
> 5-day post-event window; the Russian-and-Czech-operated exchange continued to serve its
> full application. L1 consensus layer is not_applicable by construction (pre-Merge)."

## 1. Trigger

- **Type**: `ofac_sdn_designation`
- **Actor**: `US_OFAC`
- **Timestamp**: `2021-09-21 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://ofac.treasury.gov/recent-actions/20210921>
  - Wayback: <https://web.archive.org/web/20260421135840/https://ofac.treasury.gov/recent-actions/20210921>
  - body_hash: `sha256:f97fd4561d582baeb726de448689d8297d45a7d12a7df59b1dcae7dcf0f02b45`
  - body_path: `sources/http_captures/suex-ofac-2021/ofac-recent-actions/ofac.treasury.gov__recent-actions-20210921__f3281d8050.html`
  > OFAC Recent Actions page for 2021-09-21. **First crypto exchange ever sanctioned by
> OFAC**. Entity SUEX OTC, S.R.O. (a.k.a. "SUCCESSFUL EXCHANGE"), Moscow + Prague; website
> suex.io. 25 digital-currency addresses attached across XBT×14, ETH×4, USDT×7 (Tether
> addresses include both ERC20-on-Ethereum and OMNI-on-Bitcoin variants). Tag [CYBER2].
- **`primary_legal`**
  - URL: <https://home.treasury.gov/news/press-releases/jy0364>
  > Treasury press release "Treasury Takes Robust Actions to Counter Ransomware" (2021-09-21). Frames SUEX designation as the opening of a new OFAC policy tool against crypto exchanges.

## 2. Target

- **Kind**: `address_set`
- **Enumeration**: `complete`
- **Protocol**: `suex_otc`
- **Actor name**: SUEX OTC S.R.O.
- **Chains**: `bitcoin`, `ethereum`
- **Addresses**: 19 total (enumerated in event YAML)
- **Canonical domains**: `suex.io`

> Full set of 25 unique digital-currency addresses attached to the SUEX OTC SDN entity entry,
> extracted verbatim from the 2021-09-21 Recent Actions page. Mix of chains: 14 XBT, 4 ETH,
> and 7 USDT (3 ETH-based ERC-20 + 4 BTC-based OMNI/Liquid-layer, inferred from address
> format). Several USDT addresses duplicate underlying ETH/XBT addresses (Tether tokens on
> top of those base chains).

## 3. Changed-layer observations (supports the scoped claim)

### asset_onchain · attribution: `direct` · Δt = 49.73h

**Event label**: `circle_batch_blacklisted_all_4_eth_addresses`

**Timestamp**: `2021-09-23 01:44:00+00:00` (precision: `minute`)

**Sources**:

- **`primary_onchain`**
  - URL: <https://etherscan.io/tx/0x2a4fc26c80db5fcc76e3b67b549ca28f2bfe00fd2b1f51c449151453bc74e06e>
  - tx_hash: `0x2a4fc26c80db5fcc76e3b67b549ca28f2bfe00fd2b1f51c449151453bc74e06e`
  > USDC Blacklisted() tx for SUEX ETH address 0x19aa5fe8... at 2021-09-23 01:44 UTC (first of 4 batch entries).
- **`primary_corporate`**
  - URL: <https://usdtbanlist.com/address/0x19aa5fe80d33a56d56c78e82ea5e50e5d80b4dff>
  - body_hash: `sha256:e946a8a44c3614815c900592d087e55c382e967d681383737473c72702df1cce`
  - body_path: `sources/http_captures/suex-ofac-2021/asset-layer-check/usdtbanlist.com__address-0x19aa5fe80d33a56d56c78e82ea5e50e5d80b4dff.html`
  > Circle USDC batch-froze all 4 SUEX ETH addresses on 2021-09-23 01:44 UTC
> (identical minute, single-batch op), ~50 hours after OFAC designation. Full
> per-address data at sources/asset_layer_scan/suex-ofac-2021.json.
- **`primary_corporate`**
  - URL: <https://usdtbanlist.com/address/0x2f389ce8bd8ff92de3402ffce4691d17fc4f6535>
  - body_hash: `sha256:9c3e87bbfa586aab9cd7210d967df191258b6b8e5e292170358cf440dba07a0e`
  - body_path: `sources/http_captures/suex-ofac-2021/asset-layer-check/usdtbanlist.com__address-0x2f389ce8bd8ff92de3402ffce4691d17fc4f6535.html`
  > Second sampled SUEX ETH address, same 2021-09-23 01:44 UTC batch.

## 4. No-change observations (where applicable)

### l4_frontend — `canonical_frontend_remained_operational_post_designation`

**Window**: `2021-09-22 00:00:00+00:00` → `2021-09-26 23:59:59+00:00`

**Sources**:

- **`semi_primary_wayback`**
  - URL: <https://web.archive.org/web/20210922000151/https://suex.io/>
  - body_hash: `sha256:badaa19bd92ce63bdbeaeea803be9f3fdddb2fb6bf931e46c2a5bcb3422d819d`
  - body_path: `sources/http_captures/suex-ofac-2021/frontend-wayback/web.archive.org__web-20210922000151-https-suex.io__8815f4636a.html`
  > Wayback snapshot at 2021-09-22 00:01:51 UTC (≈ 0-half-day post-event). 200 OK, full
> application rendering: "Affiliate Program / Sign In / Sign Up / Buy Cryptocurrencies
> With A Credit Card" — no takedown banner, no degradation.
- **`semi_primary_wayback`**
  - URL: <https://web.archive.org/web/20210926203825/https://suex.io/>
  - body_hash: `sha256:5af7f3e4e4923ef33d22866314e406bda4665f356b42ca9fc6c9aa7b9ba6f743`
  - body_path: `sources/http_captures/suex-ofac-2021/frontend-wayback/web.archive.org__web-20210926203825-https-suex.io__254492f512.html`
  > Second Wayback snapshot 5 days post-event (2021-09-26 20:38 UTC), still full
> application with identical affiliate / sign-in / buy-crypto UI. Same functional
> surface as pre-event. Independent archival anchor for the observed_no_change claim.

## 5. Honest coverage gaps

- **l0_network** (`not_measured`): L0 network-layer OONI API query performed 2026-04-22. Searched the
- **offramp_cex** (`not_measured`): Chain-analytics anchors pinned 2026-04-22 as primary_corporate

## 7. Related events

- [`chatex-ofac-2021`](./chatex-ofac-2021.md)
- [`garantex-ofac-2022`](./garantex-ofac-2022.md)
- [`grinex-garantex-successor-ofac-2025`](./grinex-garantex-successor-ofac-2025.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `4b6ca9a`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

