# Evidence chain — `circle-usdc-cryptex-freeze-2024`

**Status**: `admitted` · **Stratum**: `S5_corporate` · **Shape**: `comparison` (1 changed layer(s): `asset_onchain`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `a09b90d` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-21` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> Circle's 2024-09-27 03:00 UTC USDC blacklist of the OFAC-named Cryptex ETH address
> 0x0931cA4D13BB4ba75D9B7132AB690265D749a5E7 (~27h after the 2024-09-26 SDN) constitutes a
> distinct corporate-policy-change event documenting Circle's compliance response to a
> single-address OFAC SDN, sibling to the cryptex-ofac-2024 cascade.

## 1. Trigger

- **Type**: `corporate_policy_change`
- **Actor**: `CIRCLE_USDC_ISSUER`
- **Timestamp**: `2024-09-26 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://ofac.treasury.gov/recent-actions/20240926>
  - Wayback: <https://web.archive.org/web/2024/https://ofac.treasury.gov/recent-actions/20240926>
  > OFAC Recent Actions 2024-09-26: CRYPTEX SDN entry enumerates four digital-currency
> addresses including USDC-on-Ethereum address 0x0931cA4D13BB4ba75D9B7132AB690265D749a5E7.
> This is the upstream trigger that the Circle USDC corporate-policy freeze responds to;
> captured here as contextual_unarchived because the canonical OFAC capture body_hash is
> pinned in the sibling event cryptex-ofac-2024.
- **`primary_onchain`**
  - URL: <https://etherscan.io/tx/0xa10d4e1a29a6eb30579b8cba5e1316d27ab120eff5944cce6836c8a837ffd8da>
  - Wayback: <https://web.archive.org/web/2024/https://etherscan.io/tx/0xa10d4e1a29a6eb30579b8cba5e1316d27ab120eff5944cce6836c8a837ffd8da>
  - tx_hash: `0xa10d4e1a29a6eb30579b8cba5e1316d27ab120eff5944cce6836c8a837ffd8da`
  > Circle USDC Blacklisted() transaction freezing the OFAC-named Cryptex ETH address
> 0x0931cA4D13BB4ba75D9B7132AB690265D749a5E7 at 2024-09-27 03:00 UTC, approximately
> 27 hours after the OFAC SDN designation. On-chain receipt of the corporate-policy
> compliance action.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Protocol**: `cryptex_exchange`
- **Actor name**: Cryptex
- **Chains**: `ethereum`
- **Addresses**: 1 total (enumerated in event YAML)

> Single Cryptex-controlled USDC-on-Ethereum address (0x0931cA4D13BB4ba75D9B7132AB690265D749a5E7)
> pre-named on the OFAC SDN Cryptex entry. Subset because Cryptex's full address universe is
> larger than the one ETH address OFAC enumerated; Circle's freeze action targeted only the
> SDN-named ETH address (no broader cluster sweep observed at this event date).

## 3. Changed-layer observations (supports the scoped claim)

### asset_onchain · attribution: `direct` · Δt = 27.0h

**Event label**: `usdc_blacklist_cryptex_sdn_address_within_27h`

**Timestamp**: `2024-09-27 03:00:00+00:00` (precision: `minute`)

**Sources**:

- **`primary_onchain`**
  - URL: <https://etherscan.io/tx/0xa10d4e1a29a6eb30579b8cba5e1316d27ab120eff5944cce6836c8a837ffd8da>
  - Wayback: <https://web.archive.org/web/2024/https://etherscan.io/tx/0xa10d4e1a29a6eb30579b8cba5e1316d27ab120eff5944cce6836c8a837ffd8da>
  - tx_hash: `0xa10d4e1a29a6eb30579b8cba5e1316d27ab120eff5944cce6836c8a837ffd8da`
  > Circle USDC Blacklisted() tx freezing Cryptex ETH address 0x0931cA... at
> 2024-09-27 03:00 UTC, 27 hours after the 2024-09-26 OFAC SDN designation.
> Direct on-chain receipt of the corporate-policy compliance action.
- **`supporting_community`**
  - URL: <https://usdtbanlist.com/address/0x0931cA4D13BB4ba75D9B7132AB690265D749a5E7>
  - Wayback: <https://web.archive.org/web/2024/https://usdtbanlist.com/address/0x0931cA4D13BB4ba75D9B7132AB690265D749a5E7>
  - body_hash: `sha256:145f410f6a396bd596c3dda51ea5040b505b08b5712f23edf8744fe438c48faa`
  - body_path: `sources/http_captures/cryptex-ofac-2024/asset-layer-check/usdtbanlist.com__address-0x0931cA4D13BB4ba75D9B7132AB690265D749a5E7__169bb88c26.html`
  > usdtbanlist community tracker page for the Cryptex ETH address. Confirms both
> Tether and Circle blacklist transactions; reused from the sibling cryptex-ofac-2024
> capture bundle (same evidence_group_id for both issuer-side rows).

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`cryptex-ofac-2024`](./cryptex-ofac-2024.md)
- [`circle-usdc-tornado-2022`](./circle-usdc-tornado-2022.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `a09b90d`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

