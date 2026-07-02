# Evidence chain — `circle-usdc-multichain-hack-freeze-2023-07`

**Status**: `admitted` · **Stratum**: `S5_corporate` · **Shape**: `comparison` (1 changed layer(s): `asset_onchain`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-08` · **Source commit**: `ee7bf1a` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-31` · **Tool version**: `0.1.0` · **Generated**: `2026-06-25T23:48:26Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "Circle's 2023-07-07 16:55:23 UTC USDC-contract blacklist of three Multichain-exploit-
> linked Ethereum addresses (~$63-65M USDC, at DOJ seizure-warrant direction and
> later under SDNY court order) is a single-layer asset_onchain observed_change
> with attribution=plausible; the three source-named address prefixes are
> resolved to full Ethereum addresses by matching USDC Blacklisted(address)
> logs in block 17643245. The row remains draft only because no human
> promotion is claimed."

## 1. Trigger

- **Type**: `corporate_policy_change`
- **Actor**: `circle`
- **Timestamp**: `2023-07-07 16:55:23+00:00` (precision: `minute`)

### Trigger citations

- **`semi_primary_wayback`**
  - URL: <https://www.theblock.co/post/377094/multichain-extends-freeze-stolen-usdc>
  - Wayback: <https://web.archive.org/web/20251129153811/https://www.theblock.co/post/377094/multichain-extends-freeze-stolen-usdc>
  - body_hash: `sha256:7987c110d42af1ce73124dbf1c72d0af5e38345fa0bf1128639ae64ec13d077e`
  - body_path: `sources/http_captures/circle-usdc-multichain-hack-freeze-2023-10/primary/web.archive.org__web-20251129153811-https-www.theblock.co-post-377094-multichain-extends-freeze-stolen-usdc__bc93fd3241.html`
  > The Block (2025, extends-freeze story): "Shortly after the hack, the
> U.S. Department of Justice obtained a seizure warrant and compelled
> Circle to freeze the addresses" holding ~$63 million worth of USDC
> stolen from Multichain; the DOJ later informed the court it could not
> identify the hackers, and Judge David S. Jones (SDNY bankruptcy court)
> ordered Circle to maintain the addresses on its blacklist for the
> Singapore-based Multichain liquidators. Grep of captured body confirms
> "U.S. Department of Justice obtained a seizure warrant and compelled
> Circle to freeze the addresses", "$63 million worth of USDC", "Judge
> David S. Jones", "bankruptcy court". Wayback 20251129153811 pinned.
- **`primary_onchain`**
  - URL: <https://etherscan.io/tx/0x5a6ccaebe4e97298e27a40d8dd3fc59661935694c7a96b28c0de1165a725d3fc>
  - tx_hash: `0x5a6ccaebe4e97298e27a40d8dd3fc59661935694c7a96b28c0de1165a725d3fc`
  > Circle USDC Blacklisted(address) transaction for
> 0x48BeAd89e696eE93B04913CB0006f35ADB844537 in block 17643245 at
> 2023-07-07 16:55:23 UTC. Verified via Ethereum JSON-RPC
> eth_getLogs / eth_getTransactionReceipt against the USDC contract
> 0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48.
- **`primary_onchain`**
  - URL: <https://etherscan.io/tx/0xed97f73fc7c1ae7679b1572b08f16c422445e8ca575c643bd8c9c0ea3e1ad69b>
  - tx_hash: `0xed97f73fc7c1ae7679b1572b08f16c422445e8ca575c643bd8c9c0ea3e1ad69b`
  > Circle USDC Blacklisted(address) transaction for
> 0xefEeF8e968a0db92781ac7B3B7C821909ef10c88 in block 17643245 at
> 2023-07-07 16:55:23 UTC. Verified via Ethereum JSON-RPC
> eth_getLogs / eth_getTransactionReceipt against the USDC contract.
- **`primary_onchain`**
  - URL: <https://etherscan.io/tx/0xd568f3d01f052050efa2b6a0cedf89dd01f9597b6d9972be18996f9a5f5751c5>
  - tx_hash: `0xd568f3d01f052050efa2b6a0cedf89dd01f9597b6d9972be18996f9a5f5751c5`
  > Circle USDC Blacklisted(address) transaction for
> 0x027F1571aca57354223276722DC7b572a5B05cD8 in block 17643245 at
> 2023-07-07 16:55:23 UTC. Verified via Ethereum JSON-RPC
> eth_getLogs / eth_getTransactionReceipt against the USDC contract.

## 2. Target

- **Kind**: `address_set`
- **Enumeration**: `subset`
- **Actor name**: USDC at three Multichain-linked addresses
- **Chains**: `ethereum`
- **Addresses**: 3 total (enumerated in event YAML)

> USDC (Circle stablecoin) held at three Ethereum addresses that received
> outflow funds from the Multichain bridge exploit, blacklisted on the USDC
> contract by Circle. The captured BeInCrypto report publishes three address
> prefixes (0x027F1, 0xefEeF, 0x48BeA); the full addresses below come from
> matching USDC Blacklisted(address) logs in Ethereum block 17643245, queried
> over the 2023-07-07 Multichain-freeze window. Marked subset because this is
> the three-address USDC freeze set named in the source thread, not a complete
> enumeration of every Multichain exploit address or every later legal claim.

## 3. Changed-layer observations (supports the scoped claim)

### asset_onchain · attribution: `plausible` · Δt = 0h

**Event label**: `circle_blacklists_three_multichain_linked_usdc_addresses`

**Timestamp**: `2023-07-07 16:55:23+00:00` (precision: `minute`)

**Sources**:

- **`primary_onchain`**
  - URL: <https://etherscan.io/tx/0x5a6ccaebe4e97298e27a40d8dd3fc59661935694c7a96b28c0de1165a725d3fc>
  - tx_hash: `0x5a6ccaebe4e97298e27a40d8dd3fc59661935694c7a96b28c0de1165a725d3fc`
  > USDC Blacklisted(address) log for
> 0x48BeAd89e696eE93B04913CB0006f35ADB844537 in Ethereum block
> 17643245 at 2023-07-07 16:55:23 UTC.
- **`primary_onchain`**
  - URL: <https://etherscan.io/tx/0xed97f73fc7c1ae7679b1572b08f16c422445e8ca575c643bd8c9c0ea3e1ad69b>
  - tx_hash: `0xed97f73fc7c1ae7679b1572b08f16c422445e8ca575c643bd8c9c0ea3e1ad69b`
  > USDC Blacklisted(address) log for
> 0xefEeF8e968a0db92781ac7B3B7C821909ef10c88 in Ethereum block
> 17643245 at 2023-07-07 16:55:23 UTC.
- **`primary_onchain`**
  - URL: <https://etherscan.io/tx/0xd568f3d01f052050efa2b6a0cedf89dd01f9597b6d9972be18996f9a5f5751c5>
  - tx_hash: `0xd568f3d01f052050efa2b6a0cedf89dd01f9597b6d9972be18996f9a5f5751c5`
  > USDC Blacklisted(address) log for
> 0x027F1571aca57354223276722DC7b572a5B05cD8 in Ethereum block
> 17643245 at 2023-07-07 16:55:23 UTC.
- **`semi_primary_wayback`**
  - URL: <https://www.theblock.co/post/238459/63-million-in-usdc-frozen-by-circle-following-multichain-breach>
  - Wayback: <https://web.archive.org/web/20240418114315/https://www.theblock.co/post/238459/63-million-in-usdc-frozen-by-circle-following-multichain-breach>
  - body_hash: `sha256:e44c9d92b7c87682eb84af4751c8a7f90ab25ddc2f2f6fb9fb88bbf527d96c52`
  - body_path: `sources/http_captures/circle-usdc-multichain-hack-freeze-2023-10/primary/web.archive.org__web-20240418114315-https-www.theblock.co-post-238459-63-million-in-usdc-frozen-by-circle-following-multichain-breach__cc7e8b6324.html`
  > The Block: "$63 million in USDC frozen by Circle following Multichain
> breach"; "Circle blacklisted three wallet addresses that received a
> significant outflow of funds from Multichain." Grep of captured body
> confirms this title + description. Later on-chain repair pinned the
> three matching USDC Blacklisted(address) tx hashes above.
- **`semi_primary_wayback`**
  - URL: <https://beincrypto.com/multichain-hack-circle-tether-freeze-funds/>
  - Wayback: <https://web.archive.org/web/20250806162323/https://beincrypto.com/multichain-hack-circle-tether-freeze-funds/>
  - body_hash: `sha256:44996e62670db992b7d4cf0d07fb672613805b06a77b271a9b6260aed2dd0e2c`
  - body_path: `sources/http_captures/circle-usdc-multichain-hack-freeze-2023-10/primary/web.archive.org__web-20250806162323-https-beincrypto.com-multichain-hack-circle-tether-freeze-funds__6857cb2ee5.html`
  > BeInCrypto: "Circle blacklisted three addresses receiving outflow funds
> from Multichain. The three addresses, 0x027F1, 0xefEeF, and 0x48BeA,
> held $65 million in USDC." Grep of captured body confirms the three
> address prefixes verbatim. attribution=plausible: the blacklist effect
> is directly reported; the legal trigger (DOJ seizure warrant) is
> carried by the trigger citation (The Block 377094).

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`circle-usdc-cryptex-freeze-2024`](./circle-usdc-cryptex-freeze-2024.md)
- [`circle-usdc-tornado-2022`](./circle-usdc-tornado-2022.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `ee7bf1a`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

