# Evidence chain — `canada-csa-binance-withdrawal-2023`

**Status**: `admitted` · **Stratum**: `S4_nation_state` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-02` · **Source commit**: `8dbd685` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-16` · **Tool version**: `0.1.0` · **Generated**: `2026-06-02T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "The 2023-02-22 CSA Staff Notice 21-332 enhanced pre-registration-undertaking
> framework, including off-boarding / access-restriction expectations for
> platforms unable or unwilling to provide enhanced PRUs, was followed by
> Binance's official 2023-05-12 announcement that it would proactively withdraw
> from the Canadian marketplace. This row is scoped to the replayable operator
> market-withdrawal announcement and does not assert a separately measured
> binance.com geo-block, CAD-rail shutdown timeline, or withdraw-only account
> transition."

## 1. Trigger

- **Type**: `nation_state_block`
- **Actor**: `CA_CSA`
- **Timestamp**: `2023-02-22 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://www.osc.ca/sites/default/files/2023-02/csa_20230222_21-332_crypto-trading-platforms-pre-reg-undertakings.pdf>
  - body_hash: `sha256:98feda91a13238ce5af49cb958314fed8c98f8297acff5e390cf240f56089fb1`
  - body_path: `sources/http_captures/canada-csa-binance-withdrawal-2023/primary/www.osc.ca__sites-default-files-2023-02-csa_20230222_21-332_crypto-trading-platforms-pre-reg-undertakings.pdf__a38823bba3.bin`
  > CSA Staff Notice 21-332, "Crypto Asset Trading Platforms:
> Pre-Registration Undertakings - Changes to Enhance Canadian Investor
> Protection" (2023-02-22). The notice required CTPs operating in
> Canada while seeking registration to file enhanced PRUs and included
> restrictions on leverage/margin, custody and segregation, stablecoins
> / value-referenced crypto assets, proprietary tokens, and investor
> protection commitments. It also states that an unregistered CTP that
> is unable or unwilling to provide an enhanced PRU is expected to
> identify and off-board existing Canadian users and impose access
> restrictions. The OSC-hosted PDF was captured live and pinned with
> body_hash/body_path during the 2026-06-01 source-repair pass.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Binance (Canada user cohort)
- **Canonical domains**: `binance.com`

> Canada-registered crypto-trading-platform cohort regulated by the CSA's
> pre-registration-undertaking framework. Binance is the load-bearing
> target for the observable cascade because its official X account
> announced a proactive withdrawal from the Canadian marketplace on
> 2023-05-12 after the 2023-02-22 Staff Notice. Other Canadian-active
> platforms either filed PRUs and remained or exited on different
> timelines; this row treats the Binance-Canada cohort as the focal
> cascade leg while flagging the class-wide CSA posture as the trigger.

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `plausible` · Δt = 1896h

**Event label**: `binance_canada_market_withdrawal_announcement`

**Timestamp**: `2023-05-12 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_corporate`**
  - URL: <https://x.com/binance/status/1657099651210969088>
  - body_hash: `sha256:76e74a1dc89e79f326dd3d4de04e7465fa897a0941f19840a62826b8af2cf456`
  - body_path: `sources/http_captures/canada-csa-binance-withdrawal-2023/binance-x/x.com__binance-status-1657099651210969088__017fd8e815.html`
  > Binance's official X account announced on 2023-05-12 that
> Binance would join other crypto businesses in proactively
> withdrawing from the Canadian marketplace and thanked regulators
> who had worked with Binance on Canadian-user needs. This is the
> load-bearing first-party observation for the operator market-exit
> action. The captured live X HTML includes the tweet text in
> `window.__INITIAL_STATE__`; it does not by itself enumerate
> stablecoin / investor-limit terms, so attribution is kept
> plausible rather than direct.
- **`primary_legal`**
  - URL: <https://www.osc.ca/sites/default/files/2023-02/csa_20230222_21-332_crypto-trading-platforms-pre-reg-undertakings.pdf>
  - body_hash: `sha256:98feda91a13238ce5af49cb958314fed8c98f8297acff5e390cf240f56089fb1`
  - body_path: `sources/http_captures/canada-csa-binance-withdrawal-2023/primary/www.osc.ca__sites-default-files-2023-02-csa_20230222_21-332_crypto-trading-platforms-pre-reg-undertakings.pdf__a38823bba3.bin`
  > CSA Staff Notice 21-332 is the replayable legal trigger for the
> February 2023 enhanced-PRU framework. It supports the regulatory
> context and the off-boarding/access-restriction expectation for
> CTPs unable or unwilling to provide enhanced PRUs; it is not used
> as a first-party Binance operational notice.

## 5. Honest coverage gaps

- **l4_frontend** (`not_measured`): No replayable Binance.com page-state, geo-block, or account-access

## 7. Related events

- [`uk-fca-binance-markets-2021`](./uk-fca-binance-markets-2021.md)
- [`netherlands-dnb-binance-warning-2021`](./netherlands-dnb-binance-warning-2021.md)
- [`malaysia-sc-binance-disable-2021`](./malaysia-sc-binance-disable-2021.md)
- [`binance-4framework-2023`](./binance-4framework-2023.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `8dbd685`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

