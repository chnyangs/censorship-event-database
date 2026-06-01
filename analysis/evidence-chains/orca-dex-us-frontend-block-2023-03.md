# Evidence chain — `orca-dex-us-frontend-block-2023-03`

**Status**: `admitted` · **Stratum**: `S5_corporate` · **Shape**: `comparison` (1 changed layer(s): `l4_frontend`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `24d80a4` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-31` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T01:03:45Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "Orca on 2023-03-16 announced it would add the United States to its
> orca.so restricted regions effective 2023-03-31, blocking US users from
> trading via its web front end (direct contract / SDK access retained) amid
> the US regulatory crackdown — a 1-layer l4_frontend observed_change
> (attribution=plausible; Orca stated no explicit reason). An S5
> corporate-policy frontend geofence in the same 2023 cohort as the Uniswap
> frontend token delisting (uniswap-frontend-delisting-2023)."

## 1. Trigger

- **Type**: `corporate_policy_change`
- **Actor**: `ORCA_DEX`
- **Timestamp**: `2023-03-16 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`semi_primary_wayback`**
  - URL: <https://www.coindesk.com/business/2023/03/16/crypto-exchange-orca-to-block-us-traders-from-website>
  - Wayback: <https://web.archive.org/web/20240526065652/https://www.coindesk.com/business/2023/03/16/crypto-exchange-orca-to-block-us-traders-from-website/>
  - body_hash: `sha256:43df9163760c4dcb1e8a1d3ca3a1bfc4d1892ded404c74b90d7e41a3995f5491`
  - body_path: `sources/http_captures/orca-dex-us-frontend-block-2023-03/primary/web.archive.org__web-20240526065652-https-www.coindesk.com-business-2023-03-16-crypto-exchange-orca-to-block-us-traders-from-website__f580aa3cd0.html`
  > CoinDesk (2023-03-16): Orca, the leading Solana DEX, announced via a
> notice on its website that it is adding the United States to the
> regions / countries restricted from trading on orca.so, effective
> 2023-03-31. The restriction applies to US users trading via the
> orca.so front end; it does NOT block direct smart-contract / SDK
> interaction or liquidity provision. The captured page confirms
> "United States", "restricted", "March 31", and "orca.so" with the
> block scoped to the web front end. Verified via grep of the pinned
> body.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Orca (US user cohort)
- **Chains**: `solana`
- **Canonical domains**: `orca.so`

> Orca US user cohort. Orca (Solana DEX, operator of the orca.so front
> end) is the focal target actor; the affected population is US-located
> users of orca.so. Subset-enumerated because the block affected the US
> cohort via the front end rather than a named address list; US users
> retained the ability to interact directly with Orca's smart contracts /
> SDK and to provide liquidity.

## 3. Changed-layer observations (supports the scoped claim)

### l4_frontend · attribution: `plausible` · Δt = Noneh

**Event label**: `orca_us_frontend_trading_block`

**Timestamp**: `2023-03-31 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`semi_primary_wayback`**
  - URL: <https://www.coindesk.com/business/2023/03/16/crypto-exchange-orca-to-block-us-traders-from-website>
  - Wayback: <https://web.archive.org/web/20240526065652/https://www.coindesk.com/business/2023/03/16/crypto-exchange-orca-to-block-us-traders-from-website/>
  - body_hash: `sha256:43df9163760c4dcb1e8a1d3ca3a1bfc4d1892ded404c74b90d7e41a3995f5491`
  - body_path: `sources/http_captures/orca-dex-us-frontend-block-2023-03/primary/web.archive.org__web-20240526065652-https-www.coindesk.com-business-2023-03-16-crypto-exchange-orca-to-block-us-traders-from-website__f580aa3cd0.html`
  > Orca 2023-03-31 addition of the US to its orca.so restricted
> regions, blocking US web-frontend trading. attribution=plausible:
> the frontend block is directly observed in contemporaneous
> coverage, but the captured anchor is semi-primary (no Orca primary
> notice pinned) and the article notes Orca gave no explicit reason,
> so the US-regulatory-crackdown motive is contextual rather than a
> stated rationale.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`uniswap-frontend-delisting-2023`](./uniswap-frontend-delisting-2023.md)
- [`dydx-canada-frontend-wind-down-2023-04`](./dydx-canada-frontend-wind-down-2023-04.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `24d80a4`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

