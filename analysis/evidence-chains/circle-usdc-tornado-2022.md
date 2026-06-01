# Evidence chain — `circle-usdc-tornado-2022`

**Status**: `admitted` · **Stratum**: `S5_corporate` · **Shape**: `comparison` (1 changed layer(s): `asset_onchain`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-02` · **Source commit**: `60f1d90` · **Schema**: `0.2.0` · **Event last_verified**: `2026-04-22` · **Tool version**: `0.1.0` · **Generated**: `2026-06-02T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "Circle's 2022-08-08 USDC blacklist action against Tornado Cash-adjacent
> addresses (first on-chain tx at 19:25:35 UTC, ~5.93 hours after OFAC
> designation) constitutes a distinct corporate-policy-change event
> documenting fast stablecoin-issuer compliance with OFAC SDN. Paper-
> relevant asymmetry datapoint paired with Tether's 2023-12-09 retroactive
> sweep (~500-day-later compliance)."

## 1. Trigger

- **Type**: `corporate_policy_change`
- **Actor**: `circle_usdc_issuer`
- **Timestamp**: `2022-08-08 19:25:35+00:00` (precision: `second`)

### Trigger citations

- **`primary_corporate`**
  - URL: <https://www.circle.com/blog/ofacs-designation-of-tornado-cash-protocols-privacy-and-a-call-to-action>
  - body_hash: `sha256:fe0c8bbff7b5e96a1c9d94884be7798891926a86beee059268d1377d8ee2e435`
  - body_path: `sources/http_captures/circle-usdc-tornado-2022/primary/www.circle.com__blog-ofacs-designation-of-tornado-cash-protocols-privacy-and-a-call-to-action__f24a980b38.html`
  > Circle blog post "OFAC's Designation of Tornado Cash: The Protocol's
> Privacy and a Call to Action" (2022-08-12). Retroactive explanation of
> Circle's decision to blacklist Tornado Cash USDC addresses on 2022-08-08
> following the OFAC designation. Post confirms: (a) Circle's policy of
> full compliance with OFAC SDN; (b) blacklist action within hours of
> the 2022-08-08 designation; (c) the on-chain Blacklisted() tx
> 0xa61326744a21ce8d5397831d107ee14909b3f4eaaaddbf1f3dce879a19e30dd9 as
> authoritative receipt. Standalone S5 corporate-policy-change event
> capturing the issuer-side compliance action as a distinct datapoint
> from the OFAC trigger.
- **`primary_onchain`**
  - URL: <https://etherscan.io/tx/0xa61326744a21ce8d5397831d107ee14909b3f4eaaaddbf1f3dce879a19e30dd9>
  - tx_hash: `0xa61326744a21ce8d5397831d107ee14909b3f4eaaaddbf1f3dce879a19e30dd9`
  > USDC Blacklisted() tx for Tornado Cash pool address 0x8589427373D6D84E98730D7795D8f6f8731FDA16 at 2022-08-08 19:25:35 UTC (5.93 hours after OFAC designation). First on-chain Circle action.

## 2. Target

- **Kind**: `address_set`
- **Enumeration**: `subset`
- **Protocol**: `tornado_cash`
- **Actor name**: Circle (USDC)
- **Chains**: `ethereum`
- **Addresses**: 1 total (enumerated in event YAML)

> The 2022-08-08 Circle USDC batch blacklisted a subset of the 38-address
> OFAC Tornado Cash SDN list. Subset because not all 38 OFAC Tornado addresses
> held USDC — Circle only needed to freeze those addresses with USDC balances
> (approximately 19 of 38 per usdtbanlist community data). The first tx
> (anchor address) is 0x8589427373D6D84E98730D7795D8f6f8731FDA16 at 19:25:35 UTC.

## 3. Changed-layer observations (supports the scoped claim)

### asset_onchain · attribution: `direct` · Δt = 0h

**Event label**: `usdc_blacklist_tornado_cash_addresses_within_6h`

**Timestamp**: `2022-08-08 19:25:35+00:00` (precision: `second`)

**Sources**:

- **`primary_onchain`**
  - URL: <https://etherscan.io/tx/0xa61326744a21ce8d5397831d107ee14909b3f4eaaaddbf1f3dce879a19e30dd9>
  - tx_hash: `0xa61326744a21ce8d5397831d107ee14909b3f4eaaaddbf1f3dce879a19e30dd9`
  > First Circle USDC Blacklisted() tx for a Tornado Cash pool address
> (0x8589427373D6D84E98730D7795D8f6f8731FDA16) at 2022-08-08 19:25:35
> UTC — approximately 5.93 hours after OFAC designation (13:30 UTC).
> Direct on-chain receipt of the corporate policy action.
- **`primary_corporate`**
  - URL: <https://www.circle.com/blog/ofacs-designation-of-tornado-cash-protocols-privacy-and-a-call-to-action>
  - body_hash: `sha256:fe0c8bbff7b5e96a1c9d94884be7798891926a86beee059268d1377d8ee2e435`
  - body_path: `sources/http_captures/circle-usdc-tornado-2022/primary/www.circle.com__blog-ofacs-designation-of-tornado-cash-protocols-privacy-and-a-call-to-action__f24a980b38.html`
  > Circle's retroactive corporate statement explaining the compliance
> rationale for the on-chain blacklist action. Published 4 days
> post-event; names Tornado Cash explicitly and describes the
> complete-compliance stance. Primary corporate source for the
> issuer-side policy decision.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`tornado-cash-ofac-2022`](./tornado-cash-ofac-2022.md)
- [`tether-retroactive-sweep-2023`](./tether-retroactive-sweep-2023.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `60f1d90`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

