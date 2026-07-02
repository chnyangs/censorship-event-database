# Evidence chain — `crypto-capital-fowler-doj-2019`

**Status**: `admitted` · **Stratum**: `S3_doj_sec_cftc_fiod` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-08` · **Source commit**: `ee7bf1a` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-31` · **Tool version**: `0.1.0` · **Generated**: `2026-06-25T23:48:26Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "On 2019-04-30 DOJ USAO-SDNY announced Reginald Fowler's arrest for bank
> fraud and unlicensed money transmission tied to Crypto Capital / Global
> Trading Solutions shadow-banking services for cryptocurrency exchanges.
> This draft models only the enforcement termination of that fiat-rail service
> at `offramp_cex`; it does not claim an exchange shutdown, frontend seizure,
> or on-chain asset freeze."

## 1. Trigger

- **Type**: `doj_indictment`
- **Actor**: `US_DOJ_SDNY`
- **Timestamp**: `2019-04-30 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://www.justice.gov/usao-sdny/pr/arizona-man-and-israeli-woman-charged-connection-providing-shadow-banking-services>
  - Wayback: <http://web.archive.org/web/20190430215003/https://www.justice.gov/usao-sdny/pr/arizona-man-and-israeli-woman-charged-connection-providing-shadow-banking-services>
  - body_hash: `sha256:90592afe8f3a1a8dd129d325448aed5b80880d7543ca29be3fb265c6eb9561e6`
  - body_path: `sources/http_captures/crypto-capital-fowler-doj-2019/primary/web.archive.org__web-20190430215003-https-www.justice.gov-usao-sdny-pr-arizona-man-and-israeli-woman-charged-connection-providing-shadow-banking-services__9305b8f917.html`
  > DOJ USAO-SDNY 2019-04-30 press release, captured via Wayback
> on 2026-05-31 after live justice.gov capture returned an Akamai
> interstitial. The source announces Reginald Fowler's arrest on
> bank-fraud and unlicensed-money-transmitting charges, states that
> Fowler and Ravid Yosef worked with companies providing fiat-currency
> banking services to cryptocurrency exchanges, and describes the
> business as a shadow bank processing hundreds of millions of dollars
> of unregulated transactions for numerous cryptocurrency exchanges.
- **`primary_legal`**
  - URL: <https://www.justice.gov/usao-sdny/pr/former-co-owner-minnesota-vikings-sentenced-75-months-prison-providing-shadow-banking>
  - Wayback: <http://web.archive.org/web/20230605174521/https://www.justice.gov/usao-sdny/pr/former-co-owner-minnesota-vikings-sentenced-75-months-prison-providing-shadow-banking>
  - body_hash: `sha256:d25a49ad36c472595126a5a40fcca4db52e767c9fccb4a59828d41c3186e352d`
  - body_path: `sources/http_captures/crypto-capital-fowler-doj-2019/primary/web.archive.org__web-20230605174521-https-www.justice.gov-usao-sdny-pr-former-co-owner-minnesota-vikings-sentenced-75-months-prison-providing-shadow-banking__998074124d.html`
  > DOJ USAO-SDNY 2023-06-05 sentencing release, captured via Wayback
> on 2026-05-31. The source states that Fowler was sentenced to
> 75 months for arranging to process more than $700M of unregulated
> transactions for cryptocurrency exchanges, and that Global Trading
> Solutions / Crypto Capital processed fiat-to-cryptocurrency
> transactions without MSB licensing.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Reginald Fowler / Global Trading Solutions / Crypto Capital

> The public DOJ sources name Reginald Fowler, Ravid Yosef, Global Trading
> Solutions, and the Crypto Capital-related "Crypto Companies," but do not
> enumerate every exchange customer or bank account. The scoped target is
> Fowler's shadow-banking / payment-processing service for cryptocurrency
> exchanges, not Bitfinex, Binance, or any one exchange as the censored
> platform.

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `direct` · Δt = 0h

**Event label**: `fowler_crypto_capital_shadow_banking_service_terminated_by_doj_enforcement`

**Timestamp**: `2019-04-30 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_legal`**
  - URL: <https://www.justice.gov/usao-sdny/pr/arizona-man-and-israeli-woman-charged-connection-providing-shadow-banking-services>
  - Wayback: <http://web.archive.org/web/20190430215003/https://www.justice.gov/usao-sdny/pr/arizona-man-and-israeli-woman-charged-connection-providing-shadow-banking-services>
  - body_hash: `sha256:90592afe8f3a1a8dd129d325448aed5b80880d7543ca29be3fb265c6eb9561e6`
  - body_path: `sources/http_captures/crypto-capital-fowler-doj-2019/primary/web.archive.org__web-20190430215003-https-www.justice.gov-usao-sdny-pr-arizona-man-and-israeli-woman-charged-connection-providing-shadow-banking-services__9305b8f917.html`
  > The charging release is the operative trigger: DOJ announced Fowler's
> arrest and unsealed charges for bank fraud and unlicensed money
> transmission tied to fiat-currency banking services for cryptocurrency
> exchanges. Attribution is direct for the narrow off-ramp service
> target; this draft does not claim a public shutdown of any exchange.
- **`primary_legal`**
  - URL: <https://www.justice.gov/usao-sdny/pr/former-co-owner-minnesota-vikings-sentenced-75-months-prison-providing-shadow-banking>
  - Wayback: <http://web.archive.org/web/20230605174521/https://www.justice.gov/usao-sdny/pr/former-co-owner-minnesota-vikings-sentenced-75-months-prison-providing-shadow-banking>
  - body_hash: `sha256:d25a49ad36c472595126a5a40fcca4db52e767c9fccb4a59828d41c3186e352d`
  - body_path: `sources/http_captures/crypto-capital-fowler-doj-2019/primary/web.archive.org__web-20230605174521-https-www.justice.gov-usao-sdny-pr-former-co-owner-minnesota-vikings-sentenced-75-months-prison-providing-shadow-banking__998074124d.html`
  > Sentencing-stage corroboration for the same service: DOJ describes
> Fowler as processing more than $700M for cryptocurrency exchanges,
> and says GTS / Crypto Capital provided fiat-to-cryptocurrency
> transaction processing without MSB licensing.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`bitfinex-tether-nyag-2021`](./bitfinex-tether-nyag-2021.md)
- [`fincen-eric-powers-p2p-exchanger-2019-04`](./fincen-eric-powers-p2p-exchanger-2019-04.md)
- [`coin-mx-doj-murgio-2015`](./coin-mx-doj-murgio-2015.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `ee7bf1a`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

