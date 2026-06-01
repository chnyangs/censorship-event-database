# Evidence chain — `gemini-netherlands-exit-2023-11`

**Status**: `admitted` · **Stratum**: `S5_corporate` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-02` · **Source commit**: `892a0b7` · **Schema**: `0.2.0` · **Event last_verified**: `2026-06-02` · **Tool version**: `0.1.0` · **Generated**: `2026-06-02T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "Gemini's 2023-11-17 effective closure of affected Netherlands accounts,
> leaving Dutch users unable to access Gemini exchange or custody services and
> citing DNB requirements on crypto exchanges, is a single-layer offramp_cex
> observed_change with direct attribution, part of the 2023 Dutch exchange
> exodus (cf. Binance/KuCoin)."

## 1. Trigger

- **Type**: `corporate_policy_change`
- **Actor**: `gemini`
- **Timestamp**: `2023-11-17 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_corporate`**
  - URL: <https://support.gemini.com/hc/en-us/articles/19053340588187-Gemini-closing-accounts-in-the-Netherlands-Everything-you-need-to-know>
  - Wayback: <https://web.archive.org/web/20231208060627/https://support.gemini.com/hc/en-us/articles/19053340588187-Gemini-closing-accounts-in-the-Netherlands-Everything-you-need-to-know>
  - body_hash: `sha256:2c3471a8fb196710e613f237bc94f72cf068094491acdecc77c61ab1c4a2e9fd`
  - body_path: `sources/http_captures/gemini-netherlands-exit-2023-11/primary-gemini-wayback-v1/web.archive.org__web-20231208060627-https-support.gemini.com-hc-en-us-articles-19053340588187-Gemini-closing-accounts-in-the-Netherlands-Everything-you-need-to-know__23d44b8427.html`
  > Gemini Help Center Wayback memento captured 2023-12-08 for "Gemini
> closing accounts in the Netherlands - Everything you need to know".
> The first-party page states that Gemini is no longer offering crypto
> services to the Dutch market from 2023-11-17 due to requirements
> imposed by De Nederlandsche Bank (DNB), and that all affected accounts
> were closed as of 2023-11-17 with Dutch users no longer able to access
> Gemini exchange or custody services. Grep-confirmed: Netherlands,
> 17th November 2023, DNB, affected accounts closed, exchange or custody
> services.
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

### offramp_cex · attribution: `direct` · Δt = 0h

**Event label**: `gemini_netherlands_market_exit_effective`

**Timestamp**: `2023-11-17 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_corporate`**
  - URL: <https://support.gemini.com/hc/en-us/articles/19053340588187-Gemini-closing-accounts-in-the-Netherlands-Everything-you-need-to-know>
  - Wayback: <https://web.archive.org/web/20231208060627/https://support.gemini.com/hc/en-us/articles/19053340588187-Gemini-closing-accounts-in-the-Netherlands-Everything-you-need-to-know>
  - body_hash: `sha256:2c3471a8fb196710e613f237bc94f72cf068094491acdecc77c61ab1c4a2e9fd`
  - body_path: `sources/http_captures/gemini-netherlands-exit-2023-11/primary-gemini-wayback-v1/web.archive.org__web-20231208060627-https-support.gemini.com-hc-en-us-articles-19053340588187-Gemini-closing-accounts-in-the-Netherlands-Everything-you-need-to-know__23d44b8427.html`
  > Gemini first-party support-page memento: Gemini no longer offered
> crypto services to the Dutch market from 2023-11-17 due to DNB
> requirements; all affected accounts were closed as of 2023-11-17
> and Dutch users could no longer access Gemini exchange or custody
> services. Direct attribution is structurally earned by the
> primary_corporate source.
- **`semi_primary_wayback`**
  - URL: <https://www.coindesk.com/policy/2023/09/29/gemini-to-cease-offering-crypto-services-in-netherlands-in-november>
  - Wayback: <https://web.archive.org/web/20240615053708/https://www.coindesk.com/policy/2023/09/29/gemini-to-cease-offering-crypto-services-in-netherlands-in-november/>
  - body_hash: `sha256:18d5f55197f40afa004b6ed0a8bbd240cbefac4e140233e5c52c886a9079ecda`
  - body_path: `sources/http_captures/gemini-netherlands-exit-2023-11/primary/web.archive.org__web-20240615053708-https-www.coindesk.com-policy-2023-09-29-gemini-to-cease-offering-crypto-services-in-netherlands-in-november__7aed9116c7.html`
  > CoinDesk 2023-09-29: Gemini to cease Netherlands crypto services in
> November due to DNB requirements; users to withdraw by 2023-11-17.
> Retained as contemporaneous semi-primary context for the earlier
> customer-notice/reporting window; not load-bearing for direct
> attribution after the Gemini support-page repair.
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

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `892a0b7`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

