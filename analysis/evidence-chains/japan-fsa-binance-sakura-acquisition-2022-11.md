# Evidence chain — `japan-fsa-binance-sakura-acquisition-2022-11`

**Status**: `admitted` · **Stratum**: `S4_nation_state` · **Shape**: `null_event` (0 changed layer(s): none) · **Tier**: `null_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `8726393` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-21` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:13:27Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "Japan FSA's registered-VASP regime under the Payment Services Act
> permitted Binance's 2022-11-30 acquisition of 100% of Sakura
> Exchange BitCoin (SEBC), a JFSA-registered Crypto-Asset Exchange
> Service Provider, enabling Binance's re-entry into the Japanese
> market via licensed-VASP change-of-control. As of the 2026-05-17
> authoring date no enforcement-driven JP-resident-access restriction
> attributable specifically to the 2022-11-30 trigger has been
> observed. Coded null_event / null_case as the permissive counter-
> example to JP_FSA enforcement actions against Binance
> (japan-fsa-binance-warning-2018) and to non-US national regulator
> Binance-market-access denials (france-amf-binance-psan-2022,
> germany-bafin-binance-licence-withdrawal-2023), and as a
> S4_nation_state permissive denominator control."

## 1. Trigger

- **Type**: `regulatory_enforcement`
- **Actor**: `JP_FSA`
- **Timestamp**: `2022-11-30 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_corporate`**
  - URL: <https://www.binance.com/en/blog/markets/binance-acquires-sakura-exchange-bitcoin-marking-its-official-entry-into-japan-3556095942303204167>
  - Wayback: <https://web.archive.org/web/2022/https://www.binance.com/en/blog/markets/binance-acquires-sakura-exchange-bitcoin-marking-its-official-entry-into-japan-3556095942303204167>
  > Binance corporate blog post dated 2022-11-30 announcing the
> acquisition of a 100% stake in Sakura Exchange BitCoin (SEBC), a
> Japan Financial Services Agency (JFSA)-registered Crypto-Asset
> Exchange Service Provider (CAESP). Sakura was at the time one of
> ~31 CAESPs registered under the Payment Services Act (資金決済法)
> with the JFSA. The acquisition is the permissive counter-example
> to the 2018-03-23 JFSA public warning against Binance
> (japan-fsa-binance-warning-2018): rather than refusing market
> access, the JFSA-registered-VASP regime permitted Binance to
> re-enter Japan via acquisition of an already-licensed local
> operator. The trigger is the FSA-permitted change-of-control of
> a registered CAESP (not a public-warning / business-improvement
> order), and is coded as the regulatory_enforcement family per
> codebook §5.1 because the underlying authority is the JFSA's
> registered-CAESP supervisory perimeter. DRYRUN: pinned snapshot
> timestamp and body_hash capture for the Binance blog post is
> deferred to non-DRYRUN release.
- **`semi_primary_wayback`**
  - URL: <https://www.coindesk.com/business/2022/11/30/binance-enters-japan-with-acquisition-of-regulated-crypto-exchange-sakura>
  - Wayback: <https://web.archive.org/web/20221130111500/https://www.coindesk.com/business/2022/11/30/binance-enters-japan-with-acquisition-of-regulated-crypto-exchange-sakura>
  - body_hash: `sha256:88253a63121aaed9d78e9b9045eeeef8a4ee4c128f795e71b8a413853136812f`
  - body_path: `sources/http_captures/japan-fsa-binance-sakura-acquisition-2022-11/primary/web.archive.org__web-20221130111500-https-www.coindesk.com-business-2022-11-30-binance-enters-japan-with-acquisition-of-regulated-crypto-exchange-sakura__bcff3ae886.html`
  > CoinDesk contemporaneous reporting dated 2022-11-30 corroborates
> the acquisition date and notes Binance's prior FSA warning
> history (2018, 2021). DRYRUN pinned snapshot anchor deferred to
> human audit.
- **`semi_primary_wayback`**
  - URL: <https://decrypt.co/116013/binance-acquires-japanese-crypto-exchange-sakura>
  - Wayback: <https://web.archive.org/web/20221130173511/https://decrypt.co/116013/binance-acquires-japanese-crypto-exchange-sakura>
  - body_hash: `sha256:205cd9e88ea4329762d96523055f9f4b0645f62fc816429e8b15afcbfaad2a82`
  - body_path: `sources/http_captures/japan-fsa-binance-sakura-acquisition-2022-11/primary/web.archive.org__web-20221130173511-https-decrypt.co-116013-binance-acquires-japanese-crypto-exchange-sakura__757ca5c37b.html`
  > Decrypt contemporaneous reporting dated 2022-11-30 corroborating
> the acquisition and JFSA-registered status of Sakura Exchange
> BitCoin. DRYRUN pinned snapshot anchor deferred to human audit.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Binance Holdings + Sakura Exchange BitCoin (SEBC)
- **Canonical domains**: `binance.com`, `sebcoin.co.jp`

> Binance (via acquisition vehicle) and Sakura Exchange BitCoin
> (SEBC) — the JFSA-registered Crypto-Asset Exchange Service Provider
> whose 100% equity was acquired by Binance, the change-of-control
> permitted under the Payment Services Act registered-VASP regime.
> Subset enumeration: only the Binance/SEBC entity pair is enumerated
> here. The ~30 other JFSA-registered CAESPs in 2022-11 are not
> enumerated; this row's null_event posture applies specifically to
> the Binance-via-SEBC change-of-control transaction, not to the
> broader CAESP cohort. The acquisition contrasts with the 2018-03-23
> FSA warning to Binance (japan-fsa-binance-warning-2018) under the
> same registered-VASP regime, making the pair a clean permissive /
> enforcement counterfactual for the same regulator-target dyad.

## 3. Changed-layer observations (supports the scoped claim)

*No observed_change entries. This is a `null_event`; see §4 for observed_no_change evidence supporting the null claim.*

## 4. No-change observations (where applicable)

### offramp_cex — `jfsa_permitted_change_of_control_no_observed_restriction`

**Window**: `2022-11-30 00:00:00+00:00` → `2026-05-17 00:00:00+00:00`

**Sources**:

- **`primary_corporate`**
  - URL: <https://www.binance.com/en/blog/markets/binance-acquires-sakura-exchange-bitcoin-marking-its-official-entry-into-japan-3556095942303204167>
  - Wayback: <https://web.archive.org/web/2022/https://www.binance.com/en/blog/markets/binance-acquires-sakura-exchange-bitcoin-marking-its-official-entry-into-japan-3556095942303204167>
  > Binance corporate blog 2022-11-30: acquisition of 100% stake
> in Sakura Exchange BitCoin (JFSA-registered CAESP) is the
> permissive change-of-control under the registered-VASP
> regime. attribution=none is required by schema for
> observed_no_change rows. No JP-resident-access restriction
> or operator-side market exit is asserted — this is the
> counter-example to the 2018-03-23 JFSA Binance warning where
> the same regulator-target dyad produced an exit. The Binance
> blog URL has no Wayback memento; effective-date detail is
> anchored via the two semi_primary_wayback sources below.
> NOTE:
> pinned snapshot anchor deferred to human audit.
- **`supporting_journalism`**
  - URL: <https://www.coindesk.com/business/2022/11/30/binance-enters-japan-with-acquisition-of-regulated-crypto-exchange-sakura>
  - Wayback: <https://web.archive.org/web/2022/https://www.coindesk.com/business/2022/11/30/binance-enters-japan-with-acquisition-of-regulated-crypto-exchange-sakura>
  > CoinDesk 2022-11-30 contemporaneous reporting corroborates
> the acquisition date and Binance's FSA-warning history
> (2018, 2021). DRYRUN pinned snapshot anchor deferred to
> human audit.
- **`supporting_journalism`**
  - URL: <https://decrypt.co/116013/binance-acquires-japanese-crypto-exchange-sakura>
  - Wayback: <https://web.archive.org/web/2022/https://decrypt.co/116013/binance-acquires-japanese-crypto-exchange-sakura>
  > Decrypt 2022-11-30 contemporaneous reporting corroborates
> the acquisition and SEBC's JFSA-registered status. DRYRUN
> pinned snapshot anchor deferred to human audit.
- **`semi_primary_wayback`**
  - URL: <https://www.coindesk.com/business/2022/11/30/binance-enters-japan-with-acquisition-of-regulated-crypto-exchange-sakura>
  - Wayback: <https://web.archive.org/web/20221130111500/https://www.coindesk.com/business/2022/11/30/binance-enters-japan-with-acquisition-of-regulated-crypto-exchange-sakura>
  - body_hash: `sha256:88253a63121aaed9d78e9b9045eeeef8a4ee4c128f795e71b8a413853136812f`
  - body_path: `sources/http_captures/japan-fsa-binance-sakura-acquisition-2022-11/primary/web.archive.org__web-20221130111500-https-www.coindesk.com-business-2022-11-30-binance-enters-japan-with-acquisition-of-regulated-crypto-exchange-sakura__bcff3ae886.html`
  > CoinDesk 2022-11-30 contemporaneous report. Independent
> semi-primary anchor 1 of 2. Wayback memento 20221130111500.
- **`semi_primary_wayback`**
  - URL: <https://decrypt.co/116013/binance-acquires-japanese-crypto-exchange-sakura>
  - Wayback: <https://web.archive.org/web/20221130173511/https://decrypt.co/116013/binance-acquires-japanese-crypto-exchange-sakura>
  - body_hash: `sha256:205cd9e88ea4329762d96523055f9f4b0645f62fc816429e8b15afcbfaad2a82`
  - body_path: `sources/http_captures/japan-fsa-binance-sakura-acquisition-2022-11/primary/web.archive.org__web-20221130173511-https-decrypt.co-116013-binance-acquires-japanese-crypto-exchange-sakura__757ca5c37b.html`
  > Decrypt 2022-11-30 contemporaneous report. Independent
> semi-primary anchor 2 of 2. Wayback memento 20221130173511.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`japan-fsa-binance-warning-2018`](./japan-fsa-binance-warning-2018.md)
- [`france-amf-binance-psan-2022`](./france-amf-binance-psan-2022.md)
- [`germany-bafin-binance-licence-withdrawal-2023`](./germany-bafin-binance-licence-withdrawal-2023.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `8726393`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

