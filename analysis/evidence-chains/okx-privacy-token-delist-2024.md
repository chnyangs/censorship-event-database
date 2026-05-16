# Evidence chain — `okx-privacy-token-delist-2024`

**Status**: `admitted` · **Stratum**: `S5_corporate` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-8` · **Dataset cutoff**: `2026-05-16` · **Source commit**: `f18bc7a` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-16` · **Tool version**: `0.1.0` · **Generated**: `2026-05-22T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "OKX's 2023-12-29 spot-trading-pair removals at www.okx.com — covering
> privacy-asset pairs (Monero/XMR, Zcash/ZEC, Dash/DASH, Horizen/ZEN) and
> bundled non-privacy pairs in the same delisting operation — narrow the
> centralized-exchange off-ramp surface for the affected privacy assets
> in the OKX corridor. The offramp_cex layer carries the load-bearing
> direct-attribution observation; L0 / L1 / L3 / l4_frontend / asset_onchain
> are not_applicable for an exchange-listing-only action."

## 1. Trigger

- **Type**: `corporate_policy_change`
- **Actor**: `okx_exchange`
- **Timestamp**: `2023-12-29 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_corporate`**
  - URL: <https://www.okx.com/en-us/help/okx-to-delist-several-spot-trading-pairs-12-29>
  - Wayback: <https://web.archive.org/web/2023/https://www.okx.com/en-us/help/okx-to-delist-several-spot-trading-pairs-12-29>
  > OKX customer-help announcement "OKX to delist several spot trading
> pairs" dated 2023-12-29. The notice enumerates a set of spot
> trading-pair removals on www.okx.com that includes privacy-coin and
> privacy-token pairs (Monero/XMR, Zcash/ZEC, Dash/DASH, Horizen/ZEN
> among the cohort), following the broader 2023 corporate-compliance
> pressure on centralized exchanges to delist privacy assets in major
> jurisdictions. Marked evidence_use=contextual_unarchived because the
> live okx.com/help path is subject to platform churn and the specific
> Wayback snapshot timestamp must be re-pinned during human audit
> before this citation may serve as a body-hash-anchored admission
> anchor in its own right. The candidate-ledger stub records the
> canonical date as 2023-12-29 and that date is honored here.

## 2. Target

- **Kind**: `asset`
- **Enumeration**: `subset`
- **Actor name**: OKX (centralized-exchange operator)
- **Chains**: `monero`, `zcash`, `dash`, `horizen`
- **Canonical domains**: `www.okx.com`

> Canonical target is the OKX product-catalogue change itself, namely
> the spot-trading-pair removals announced 2023-12-29. Named affected
> privacy assets in the cohort include Monero (XMR), Zcash (ZEC),
> Dash (DASH), and Horizen (ZEN). Recorded as enumeration=subset
> because the OKX notice covers additional non-privacy spot pairs
> bundled in the same delisting operation and the full pair set is
> not re-enumerated here.

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `direct` · Δt = 0h

**Event label**: `okx_spot_pair_removal_privacy_asset_cohort`

**Timestamp**: `2023-12-29 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_corporate`**
  - URL: <https://www.okx.com/en-us/help/okx-to-delist-several-spot-trading-pairs-12-29>
  - Wayback: <https://web.archive.org/web/2023/https://www.okx.com/en-us/help/okx-to-delist-several-spot-trading-pairs-12-29>
  > OKX customer-help notice is the corporate-policy anchor. The
> notice text names the spot pairs slated for removal in the
> 2023-12-29 batch and gives OKX-direct attribution for the
> off-ramp catalogue change. attribution=direct because OKX is
> both the announcing actor and the operator of the affected
> spot-trading product. Provisional wayback anchor; the
> specific snapshot timestamp must be re-pinned during human
> audit before this citation may carry an admission anchor on
> its own.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`uniswap-frontend-delisting-2023`](./uniswap-frontend-delisting-2023.md)
- [`tether-retroactive-sweep-2023`](./tether-retroactive-sweep-2023.md)
- `paxos-busd-nydfs-minting-stop-2023` (draft; no rendered admitted-chain link)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-8` (commit `f18bc7a`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

