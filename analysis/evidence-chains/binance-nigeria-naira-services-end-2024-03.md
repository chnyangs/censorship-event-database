# Evidence chain — `binance-nigeria-naira-services-end-2024-03`

**Status**: `admitted` · **Stratum**: `S5_corporate` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-02` · **Source commit**: `60f1d90` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-31` · **Tool version**: `0.1.0` · **Generated**: `2026-06-02T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "Binance's 2024-03-05 discontinuation of all Nigerian Naira (NGN)
> services — delisting NGN spot/P2P pairs, ending NGN deposit/withdrawal,
> and auto-converting residual NGN to USDT — severed the Binance NGN fiat
> off-ramp for Nigerian users; single-layer offramp_cex observed_change
> with attribution=direct (Binance's own announced policy)."

## 1. Trigger

- **Type**: `corporate_policy_change`
- **Actor**: `binance`
- **Timestamp**: `2024-03-05 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`semi_primary_wayback`**
  - URL: <https://www.coindesk.com/policy/2024/03/05/binance-will-discontinue-its-nigerian-naira-services-after-government-scrutiny>
  - Wayback: <https://web.archive.org/web/20240305220110/https://www.coindesk.com/policy/2024/03/05/binance-will-discontinue-its-nigerian-naira-services-after-government-scrutiny/>
  - body_hash: `sha256:dd10bee8b0af68a2b04d4902fe606cab0186aaa1d7b2db43005ae7747d16d3f1`
  - body_path: `sources/http_captures/binance-nigeria-naira-services-end-2024-03/primary/web.archive.org__web-20240306000000-https-www.coindesk.com-policy-2024-03-05-binance-will-discontinue-its-nigerian-naira-services-after-government-scrutiny__97537db759.html`
  > CoinDesk 2024-03-05: Binance announced (in a company blog post) it
> will discontinue its Nigerian Naira (NGN) services following
> government scrutiny. Captured body verifies the operative facts:
> Binance "will delist any existing NGN pairs by Thursday, and on
> Friday any remaining NGN balances in a user account will be
> converted to USDT"; "Users are encouraged to withdraw NGN, trade
> their NGN assets or convert NGN into crypto prior to the
> discontinuation." Context: heightened Nigerian regulatory scrutiny
> and the detention of Binance executives. Wayback 20240305220110.
- **`primary_corporate`**
  - URL: <https://www.binance.com/en/support/announcement/binance-to-discontinue-all-nigerian-naira-ngn-services-f9857dc2fea4448ba1fb8815d87d8144>
  - Wayback: <https://web.archive.org/web/20240306114131/https://www.binance.com/en/support/announcement/binance-to-discontinue-all-nigerian-naira-ngn-services-f9857dc2fea4448ba1fb8815d87d8144>
  - body_hash: `sha256:1ece5d57c223b89189c75c3449bb8d0f0ea0fc48b129ff89d10331e7ae8a3a57`
  - body_path: `sources/http_captures/binance-nigeria-naira-services-end-2024-03/primary/web.archive.org__web-20240307000000-https-www.binance.com-en-support-announcement-binance-to-discontinue-all-nigerian-naira-ngn-services-f9857dc2fea4448ba1fb8815d87d814__702cbe50f7.html`
  > Official Binance support announcement "Binance to Discontinue All
> Nigerian Naira (NGN) Services" (issuer's own notice; archived
> memento 2024-03-06). The page body is JS-rendered so the per-step
> NGN-service-end timeline (P2P NGN delisted 2024-02-28; NGN deposits
> stopped 2024-03-05; NGN spot pairs delisted 2024-03-07; residual
> NGN converted to USDT from 2024-03-08) is corroborated by the
> captured CoinDesk report rather than grep-confirmed in this HTML;
> retained as the primary_corporate anchor that this is Binance's own
> policy action.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `complete`
- **Actor name**: Binance Nigerian Naira (NGN) services

> Target is the Binance Nigerian-Naira (NGN) fiat service surface:
> all NGN trading pairs (BTC/NGN, USDT/NGN), NGN P2P, and NGN
> deposit/withdrawal rails on Binance. Complete enumeration of the
> NGN-service set that Binance discontinued; the action removes the
> NGN on/off-ramp for Nigerian users (residual NGN balances
> auto-converted to USDT).

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `direct` · Δt = 0h

**Event label**: `binance_discontinues_all_nigerian_naira_services`

**Timestamp**: `2024-03-05 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`semi_primary_wayback`**
  - URL: <https://www.coindesk.com/policy/2024/03/05/binance-will-discontinue-its-nigerian-naira-services-after-government-scrutiny>
  - Wayback: <https://web.archive.org/web/20240305220110/https://www.coindesk.com/policy/2024/03/05/binance-will-discontinue-its-nigerian-naira-services-after-government-scrutiny/>
  - body_hash: `sha256:dd10bee8b0af68a2b04d4902fe606cab0186aaa1d7b2db43005ae7747d16d3f1`
  - body_path: `sources/http_captures/binance-nigeria-naira-services-end-2024-03/primary/web.archive.org__web-20240306000000-https-www.coindesk.com-policy-2024-03-05-binance-will-discontinue-its-nigerian-naira-services-after-government-scrutiny__97537db759.html`
  > CoinDesk 2024-03-05: Binance to delist NGN pairs and convert
> residual NGN balances to USDT, ending NGN services. attribution=
> direct: the action is Binance's own announced policy (company
> blog post), corroborated by the official Binance notice.
- **`primary_corporate`**
  - URL: <https://www.binance.com/en/support/announcement/binance-to-discontinue-all-nigerian-naira-ngn-services-f9857dc2fea4448ba1fb8815d87d8144>
  - Wayback: <https://web.archive.org/web/20240306114131/https://www.binance.com/en/support/announcement/binance-to-discontinue-all-nigerian-naira-ngn-services-f9857dc2fea4448ba1fb8815d87d8144>
  - body_hash: `sha256:1ece5d57c223b89189c75c3449bb8d0f0ea0fc48b129ff89d10331e7ae8a3a57`
  - body_path: `sources/http_captures/binance-nigeria-naira-services-end-2024-03/primary/web.archive.org__web-20240307000000-https-www.binance.com-en-support-announcement-binance-to-discontinue-all-nigerian-naira-ngn-services-f9857dc2fea4448ba1fb8815d87d814__702cbe50f7.html`
  > Official Binance announcement "Binance to Discontinue All Nigerian
> Naira (NGN) Services" — the issuer's own notice that this is a
> Binance policy action. Body is JS-rendered (per-step timeline not
> grep-confirmed here; carried by the CoinDesk capture).

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`nigeria-binance-network-block-2024-02`](./nigeria-binance-network-block-2024-02.md)
- [`nigeria-cbn-crypto-ban-2021`](./nigeria-cbn-crypto-ban-2021.md)
- [`okx-nigeria-exit-2024-08`](./okx-nigeria-exit-2024-08.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `60f1d90`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

