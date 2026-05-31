# Evidence chain — `tether-retroactive-sweep-2023`

**Status**: `admitted` · **Stratum**: `S5_corporate` · **Shape**: `comparison` (1 changed layer(s): `asset_onchain`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `80b0ca3` · **Schema**: `0.2.0` · **Event last_verified**: `2026-04-22` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "Tether executed a retroactive batch freeze of historical OFAC-SDN ETH addresses on
> 2023-12-09 04:34-05:36 UTC, affecting addresses across ≥4 prior SDN events
> (SUEX 2021, Chatex 2021, Russia-election 2020, Russian-cyber-theft 2020). The
> minute-level timestamp clustering across distinct SDN events rules out coincidental
> action and establishes the batch as a single Tether policy operation."

## 1. Trigger

- **Type**: `corporate_policy_change`
- **Actor**: `tether_usdt_issuer`
- **Timestamp**: `2023-12-09 04:30:00+00:00` (precision: `minute`)

### Trigger citations

- **`primary_corporate`**
  - URL: <https://usdtbanlist.com/address/0x19aa5fe80d33a56d56c78e82ea5e50e5d80b4dff>
  - body_hash: `sha256:e946a8a44c3614815c900592d087e55c382e967d681383737473c72702df1cce`
  - body_path: `sources/http_captures/suex-ofac-2021/asset-layer-check/usdtbanlist.com__address-0x19aa5fe80d33a56d56c78e82ea5e50e5d80b4dff.html`
  > On 2023-12-09 between ~04:34 and ~05:36 UTC, Tether executed a **retroactive
> sweep** of historical OFAC-SDN-listed addresses that it had not previously frozen
> on USDT (ERC-20). The sweep affected at least 10 addresses across 4 known SDN events:
> - SUEX-ofac-2021 (all 4 ETH, frozen 04:34-05:36 UTC)
> - Chatex-ofac-2021 (5 of 6 ETH, frozen 04:35-05:31 UTC)
> - Russia-election-interference-ofac-2020 (2 of 2 ETH, frozen 05:17 UTC)
> - Russian-cyber-theft-ofac-2020 (2 of 2 ETH, frozen 04:43 / 05:15 UTC)
> All these addresses had been sanctioned 2-3 years earlier; Circle had previously
> blacklisted them on USDC but Tether had not acted on USDT until this single sweep
> operation. Tether's blog / transparency page does not publicly announce this batch
> action, but the minute-level timestamp clustering (all within a ~1-hour window on
> one day) is unambiguous.
- **`supporting_community`**
  - URL: <https://usdtbanlist.com/address/0x67d40EE1A85bf4a4Bb7Ffae16De985e8427B6b45>
  - body_hash: `sha256:307d2114e16ee087eb53d9c0cf5b72e19d064338dc6da708abb08fb92a3cc7e7`
  - body_path: `sources/http_captures/chatex-ofac-2021/asset-layer-check/usdtbanlist.com__address-0x67d40EE1A85bf4a4Bb7Ffae16De985e8427B6b45.html`
  > Second-event address (Chatex cluster) anchoring the same 2023-12-09 batch.

## 2. Target

- **Kind**: `address_set`
- **Enumeration**: `subset`
- **Actor name**: Historical OFAC SDN ETH cluster
- **Chains**: `ethereum`
- **Addresses**: 13 total (enumerated in event YAML)

> 13 ETH addresses confirmed via 2026-04 usdtbanlist batch scan: 4 SUEX + 5 Chatex + 2
> Russia-election + 2 Russian-cyber-theft. Full enumeration of the 2023-12-09 Tether batch
> would require scanning every SDN'd ETH address listed on OFAC prior to that date; the
> 13 addresses attached here are the known members, not claimed exhaustive — hence
> enumeration: subset.

## 3. Changed-layer observations (supports the scoped claim)

### asset_onchain · attribution: `direct` · Δt = 0h

**Event label**: `retroactive_batch_freeze_historical_sdn_eth_cluster`

**Timestamp**: `2023-12-09 04:30:00+00:00` (precision: `minute`)

**Sources**:

- **`primary_onchain`**
  - URL: <https://etherscan.io/tx/0x26f25d8c2e8239252c9a1f7abf01c17f328c68700afa71027e8b5a93b3f63f25>
  - tx_hash: `0x26f25d8c2e8239252c9a1f7abf01c17f328c68700afa71027e8b5a93b3f63f25`
  > Tether addBlackList tx for SUEX address 0x19aa5fe8... at 2023-12-09 04:34 UTC. First tx in the retroactive sweep batch.
- **`primary_corporate`**
  - URL: <https://usdtbanlist.com/address/0x19aa5fe80d33a56d56c78e82ea5e50e5d80b4dff>
  - body_hash: `sha256:e946a8a44c3614815c900592d087e55c382e967d681383737473c72702df1cce`
  - body_path: `sources/http_captures/suex-ofac-2021/asset-layer-check/usdtbanlist.com__address-0x19aa5fe80d33a56d56c78e82ea5e50e5d80b4dff.html`
  > SUEX address 0x19aa... frozen 2023-12-09 04:34 UTC. First anchor of the batch.
- **`primary_corporate`**
  - URL: <https://usdtbanlist.com/address/0x67d40EE1A85bf4a4Bb7Ffae16De985e8427B6b45>
  - body_hash: `sha256:307d2114e16ee087eb53d9c0cf5b72e19d064338dc6da708abb08fb92a3cc7e7`
  - body_path: `sources/http_captures/chatex-ofac-2021/asset-layer-check/usdtbanlist.com__address-0x67d40EE1A85bf4a4Bb7Ffae16De985e8427B6b45.html`
  > Chatex address 0x67d4... frozen 2023-12-09 04:36 UTC. Second-anchor across events.
- **`primary_corporate`**
  - URL: <https://usdtbanlist.com/address/0x8576acc5c05d6ce88f4e49bf65bdf0c62f91353c>
  - body_hash: `sha256:eb18a808c950839bcd99569230708f68b0fbe8f85c8950deb587d45f9ce44c7b`
  - body_path: `sources/http_captures/russia-election-interference-ofac-2020/asset-layer-check/usdtbanlist.com__address-0x8576acc5c05d6ce88f4e49bf65bdf0c62f91353c.html`
  > Russia-election address 0x8576... frozen 2023-12-09 05:17 UTC. Third-event anchor.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`chatex-ofac-2021`](./chatex-ofac-2021.md)
- [`suex-ofac-2021`](./suex-ofac-2021.md)
- [`russia-election-interference-ofac-2020`](./russia-election-interference-ofac-2020.md)
- [`russian-cyber-theft-ofac-2020`](./russian-cyber-theft-ofac-2020.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `80b0ca3`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

