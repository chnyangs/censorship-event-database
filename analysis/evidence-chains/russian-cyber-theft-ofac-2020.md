# Evidence chain — `russian-cyber-theft-ofac-2020`

**Status**: `admitted` · **Stratum**: `S1_ofac_sdn` · **Shape**: `comparison` (1 changed layer(s): `asset_onchain`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `e43eea7` · **Schema**: `0.2.0` · **Event last_verified**: `2026-04-22` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "OFAC individual designation of two Russian cyber-theft actors on 2020-09-16 attached 12
> unique addresses spanning 8 chains, the most chain-diverse single SDN entry in the
> dataset. Cross-layer observational analysis is constrained because event predates the
> Ethereum PBS era by 2 years and targets individuals not service operators."

## 1. Trigger

- **Type**: `ofac_sdn_designation`
- **Actor**: `US_OFAC`
- **Timestamp**: `2020-09-16 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://ofac.treasury.gov/recent-actions/20200916>
  - Wayback: <https://web.archive.org/web/20260421140559/https://ofac.treasury.gov/recent-actions/20200916>
  - body_hash: `sha256:0683b60f1923123a2ee05c76a9fbad6b2e46665acaefc93366f8d2f0eb522cbd`
  - body_path: `sources/http_captures/russian-cyber-theft-ofac-2020/ofac-recent-actions/ofac.treasury.gov__recent-actions-20200916__183a1e9b84.html`
  > OFAC Recent Actions page for 2020-09-16. Two Russian individuals designated for
> virtual-currency theft from exchanges: Dmitrii KARASAVIDI (8-chain address diversity:
> XBT, ETH, XMR, LTC, ZEC, DASH, BTG, ETC — the most chain-diverse single SDN entry in
> the dataset) and Danil POTEKHIN (XBT + ETH). Tag [CYBER2].
- **`primary_legal`**
  - URL: <https://home.treasury.gov/news/press-releases/sm1123>
  > Treasury press release "Treasury Sanctions Russian Cyber Actors for Virtual Currency Theft".

## 2. Target

- **Kind**: `address_set`
- **Enumeration**: `complete`
- **Actor name**: KARASAVIDI + POTEKHIN
- **Chains**: `bitcoin`, `ethereum`, `ethereum_classic`, `monero`, `litecoin`, `zcash`, `dash`, `bitcoin_gold`
- **Addresses**: 11 total (enumerated in event YAML)

> 12 unique digital-currency addresses across 8 chains attached to the KARASAVIDI (9 addrs)
> and POTEKHIN (3 addrs) individual SDN entries. ETH and ETC share the same 0xd882... address
> (Ethereum and Ethereum Classic use identical address format on the same underlying key).

## 3. Changed-layer observations (supports the scoped claim)

### asset_onchain · attribution: `direct` · Δt = 5217.07h

**Event label**: `circle_usdc_blacklist_7_months_after_ofac`

**Timestamp**: `2021-04-21 09:04:00+00:00` (precision: `minute`)

**Sources**:

- **`primary_onchain`**
  - URL: <https://etherscan.io/tx/0x4098800943f50ee7c5b7c7369bba2f3903ae5e59bd057aa00e2f98abed44d4a7>
  - tx_hash: `0x4098800943f50ee7c5b7c7369bba2f3903ae5e59bd057aa00e2f98abed44d4a7`
  > USDC Blacklisted() tx for KARASAVIDI ETH address 0xd882... at 2021-04-21 09:19 UTC. Circle first-responder.
- **`primary_corporate`**
  - URL: <https://usdtbanlist.com/address/0xd882cfc20f52f2599d84b8e8d58c7fb62cfe344b>
  - body_hash: `sha256:3242f21ffc6d0052323d94b6ba90e0de379d38f91f87a0890dc66aa5c19cf259`
  - body_path: `sources/http_captures/russian-cyber-theft-ofac-2020/asset-layer-check/usdtbanlist.com__address-0xd882cfc20f52f2599d84b8e8d58c7fb62cfe344b.html`
  > Circle USDC blacklisted KARASAVIDI's ETH address on 2021-04-21 09:19 UTC (~7
> months after OFAC designation). Second Russian-cyber-theft ETH address (POTEKHIN's
> 0x7F367...) frozen at 2021-04-21 09:04 UTC — 15 minutes earlier, suggesting a
> single batch of 2+ addresses processed sequentially.
- **`primary_corporate`**
  - URL: <https://usdtbanlist.com/address/0x7F367cC41522cE07553e823bf3be79A889DEbe1B>
  - body_hash: `sha256:e70b6cff009eeed8e85496ba730d07734a2664a5d95a6d7863bd81dc3fd83815`
  - body_path: `sources/http_captures/russian-cyber-theft-ofac-2020/asset-layer-check/usdtbanlist.com__address-0x7F367cC41522cE07553e823bf3be79A889DEbe1B.html`
  > Second ETH address frozen in the same 2021-04-21 Circle batch (~09:04 UTC).

## 5. Honest coverage gaps

- **offramp_cex** (`not_measured`): Chain-analytics anchors pinned 2026-04-22 as primary_corporate

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `e43eea7`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

