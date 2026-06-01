# Evidence chain — `gemini-netherlands-exit-2023-11`

**Status**: `admitted` · **Stratum**: `S5_corporate` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-02` · **Source commit**: `a7b40fe` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-31` · **Tool version**: `0.1.0` · **Generated**: `2026-06-02T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "Gemini's 2023-09-29 decision to cease Netherlands crypto services by
> 2023-11-17, citing DNB requirements on crypto exchanges, is a single-layer
> offramp_cex observed_change with attribution=plausible, part of the 2023
> Dutch exchange exodus (cf. Binance/KuCoin)."

## 1. Trigger

- **Type**: `corporate_policy_change`
- **Actor**: `gemini`
- **Timestamp**: `2023-09-29 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`semi_primary_wayback`**
  - URL: <https://www.coindesk.com/policy/2023/09/29/gemini-to-cease-offering-crypto-services-in-netherlands-in-november>
  - Wayback: <https://web.archive.org/web/20240615053708/https://www.coindesk.com/policy/2023/09/29/gemini-to-cease-offering-crypto-services-in-netherlands-in-november/>
  - body_hash: `sha256:18d5f55197f40afa004b6ed0a8bbd240cbefac4e140233e5c52c886a9079ecda`
  - body_path: `sources/http_captures/gemini-netherlands-exit-2023-11/primary/web.archive.org__web-20240615053708-https-www.coindesk.com-policy-2023-09-29-gemini-to-cease-offering-crypto-services-in-netherlands-in-november__7aed9116c7.html`
  > CoinDesk 2023-09-29: "Gemini to Cease Offering Crypto Services in
> Netherlands in November" due to requirements imposed by De Nederlandsche
> Bank (DNB); Dutch users asked to withdraw their crypto and fiat balances
> by Nov. 17. Grep of captured body confirms "Gemini", "Netherlands",
> "requirements imposed by the De Nederlandsche Bank (DNB)", "withdrawn
> their crypto and fiat balances by Nov. 17". Wayback 20240615053708
> pinned.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Gemini (Netherlands market)
- **Canonical domains**: `gemini.com`

> Target is the Gemini Dutch-resident customer access surface. Subset
> enumeration: a national market-access withdrawal (services ceased; balances
> to be withdrawn by 2023-11-17) rather than a complete on-chain address set.
> No address-level targets; a market-level exit by a centralized exchange.

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `plausible` · Δt = 0h

**Event label**: `gemini_netherlands_market_withdrawal_announced`

**Timestamp**: `2023-09-29 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`semi_primary_wayback`**
  - URL: <https://www.coindesk.com/policy/2023/09/29/gemini-to-cease-offering-crypto-services-in-netherlands-in-november>
  - Wayback: <https://web.archive.org/web/20240615053708/https://www.coindesk.com/policy/2023/09/29/gemini-to-cease-offering-crypto-services-in-netherlands-in-november/>
  - body_hash: `sha256:18d5f55197f40afa004b6ed0a8bbd240cbefac4e140233e5c52c886a9079ecda`
  - body_path: `sources/http_captures/gemini-netherlands-exit-2023-11/primary/web.archive.org__web-20240615053708-https-www.coindesk.com-policy-2023-09-29-gemini-to-cease-offering-crypto-services-in-netherlands-in-november__7aed9116c7.html`
  > CoinDesk 2023-09-29: Gemini to cease Netherlands crypto services in
> November due to DNB requirements; users to withdraw by 2023-11-17.
> attribution=plausible: the market withdrawal is directly observed; the
> captured anchor is trade press (not a Gemini primary notice) and the
> DNB-requirement framing is as reported.
- **`semi_primary_wayback`**
  - URL: <https://www.unlock-bc.com/109313/gemini-halts-operations-in-netherlands-amid-regulatory-challenges/>
  - Wayback: <https://web.archive.org/web/20250624003219/https://www.unlock-bc.com/109313/gemini-halts-operations-in-netherlands-amid-regulatory-challenges/>
  - body_hash: `sha256:80960eae95ce4977ed0520f488bab19df5a4bf7227107ad3e0544c51d9f712b7`
  - body_path: `sources/http_captures/gemini-netherlands-exit-2023-11/primary/web.archive.org__web-20250624003219-https-www.unlock-bc.com-109313-gemini-halts-operations-in-netherlands-amid-regulatory-challenges__a86d2a7053.html`
  > Unlock-BC corroboration of the Gemini Netherlands operations halt amid
> DNB regulatory requirements. Independent second semi-primary anchor.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`binance-netherlands-exit-2023-07`](./binance-netherlands-exit-2023-07.md)
- [`kucoin-netherlands-exit-2023`](./kucoin-netherlands-exit-2023.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `a7b40fe`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

