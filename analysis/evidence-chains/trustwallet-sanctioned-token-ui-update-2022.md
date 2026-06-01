# Evidence chain — `trustwallet-sanctioned-token-ui-update-2022`

**Status**: `admitted` · **Stratum**: `S5_corporate` · **Shape**: `null_event` (0 changed layer(s): none) · **Tier**: `null_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-02` · **Source commit**: `2dfaf57` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-21` · **Tool version**: `0.1.0` · **Generated**: `2026-06-02T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> The candidate event "Trust Wallet (Binance-affiliated) UI update
> to display warnings on OFAC-sanctioned tokens following the
> 2022-08-08 OFAC SDN cascade (related event tornado-cash-ofac-2022)"
> could not be verified against any Trust-Wallet-operated corporate
> channel in the authoring and audit passes. The row is coded as an
> admitted null_event/null_case with one observed_no_change row at
> l4_frontend (attribution=none) and l4_frontend coverage.status=
> partially_measured. It is claim-usable only as a bounded denominator
> / no-public-record observation unless Trust Wallet release notes,
> GitHub history, or community discussion later support recoding.

## 1. Trigger

- **Type**: `corporate_policy_change`
- **Actor**: `TRUSTWALLET_BINANCE`
- **Timestamp**: `2022-08-01 00:00:00+00:00` (precision: `week`)

### Trigger citations

- **`primary_corporate`**
  - URL: <https://trustwallet.com/blog/cryptocurrency/tornado-cash-explained>
  - Wayback: <https://web.archive.org/web/2022/https://trustwallet.com/blog/cryptocurrency/tornado-cash-explained>
  - body_hash: `sha256:a6ef7187edf50e4cd5270b866293f01ef215f5283abdefb54472ad832858292d`
  - body_path: `sources/http_captures/trustwallet-sanctioned-token-ui-update-2022/v0_3_primary_repair/trustwallet.com__blog-cryptocurrency-tornado-cash-explained__4e36ebe5e5.html`
  > Trust Wallet's own educational blog post discussing Tornado Cash
> following the 2022-08-08 OFAC SDN designation (related event
> tornado-cash-ofac-2022). This is the closest publicly retrievable
> Trust Wallet corporate-channel anchor located in the present
> authoring pass for any 2022 Trust Wallet UI behaviour change
> relating to OFAC-sanctioned tokens. Evidence repair 2026-06-01:
> the post is locally captured with body_hash/body_path and is
> claim-usable only for the bounded public-record null observation
> and OFAC-context bracketing. It does NOT directly document a
> Trust Wallet UI update that displays warnings on sanctioned
> tokens and is not evidence of an affirmative UI-warning feature.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Trust Wallet (Binance affiliate)
- **Chains**: `ethereum`
- **Canonical domains**: `trustwallet.com`

> Hypothesised target is the class of OFAC-SDN-listed token contracts
> surfaced inside the Trust Wallet mobile UI (asset list, send / swap
> flows). The Trust Wallet asset surface is operator-curated and the
> OFAC-listed Tornado Cash contracts (the 44 Ethereum addresses named
> in the 2022-08-08 designation, per related event
> tornado-cash-ofac-2022) are the candidate target subset. Because the
> UI-warning behaviour itself could not be confirmed from any
> Trust-Wallet-operated corporate channel in this authoring pass,
> enumeration=subset with class-level rationale (per codebook §7); no
> specific UI-warning roster has been pinned.

## 3. Changed-layer observations (supports the scoped claim)

*No observed_change entries. This is a `null_event`; see §4 for observed_no_change evidence supporting the null claim.*

## 4. No-change observations (where applicable)

### l4_frontend — `no_documented_trustwallet_ui_warning_on_ofac_sanctioned_tokens_2022`

**Window**: `2022-08-08 00:00:00+00:00` → `2022-11-08 00:00:00+00:00`

**Sources**:

- **`primary_corporate`**
  - URL: <https://trustwallet.com/blog/cryptocurrency/tornado-cash-explained>
  - Wayback: <https://web.archive.org/web/2022/https://trustwallet.com/blog/cryptocurrency/tornado-cash-explained>
  - body_hash: `sha256:a6ef7187edf50e4cd5270b866293f01ef215f5283abdefb54472ad832858292d`
  - body_path: `sources/http_captures/trustwallet-sanctioned-token-ui-update-2022/v0_3_primary_repair/trustwallet.com__blog-cryptocurrency-tornado-cash-explained__4e36ebe5e5.html`
  > Trust Wallet's own Tornado Cash explainer blog post is the
> closest Trust-Wallet-operated corporate-channel anchor
> located in this authoring pass. It acknowledges the 2022-
> 08-08 OFAC designation as context but does NOT document
> any Trust Wallet UI-warning feature for OFAC-sanctioned
> tokens. Evidence repair 2026-06-01: the local body_hash/body_path
> make this a replayable primary corporate source for the bounded
> public-record null observation, not evidence of an affirmative
> Trust Wallet UI-warning feature. attribution=none per validator
> rule for observed_no_change.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`tornado-cash-ofac-2022`](./tornado-cash-ofac-2022.md)
- [`metamask-eth-phishing-detect-tornado-additions-2022`](./metamask-eth-phishing-detect-tornado-additions-2022.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `2dfaf57`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

