# Evidence chain — `cryptex-uaps-pm2btc-ivanov-shakhmametov-doj-2024`

**Status**: `admitted` · **Stratum**: `S3_doj_sec_cftc_fiod` · **Shape**: `comparison` (2 changed layer(s): `l4_frontend`, `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `08595e8` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-31` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T09:49:53Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "The 2024-09-26 DOJ EDVA / U.S. Secret Service coordinated action seized the
> Cryptex.net/Cryptex.one, UAPS, and PM2BTC domains and shut down the Cryptex
> crypto exchange and UAPS/PM2BTC payment-exchange services, producing a
> 2-layer cascade: l4_frontend (domain seizure) and offramp_cex (service
> shutdown), both attribution=direct. comparable_main tier."

## 1. Trigger

- **Type**: `doj_seizure_order`
- **Actor**: `US_DOJ_EDVA`
- **Timestamp**: `2024-09-26 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://www.justice.gov/usao-edva/pr/two-russian-nationals-charged-connection-operating-billion-dollar-money-laundering>
  - Wayback: <https://web.archive.org/web/20240926181943/https://www.justice.gov/usao-edva/pr/two-russian-nationals-charged-connection-operating-billion-dollar-money-laundering>
  - body_hash: `sha256:c5c9eace590dee38f8593a4d597471e844caf7d670e914be663e5d0ff02f9213`
  - body_path: `sources/http_captures/cryptex-uaps-pm2btc-ivanov-shakhmametov-doj-2024/primary/web.archive.org__web-20240926000000-https-www.justice.gov-usao-edva-pr-two-russian-nationals-charged-connection-operating-billion-dollar-money-laundering__a7acbbf27a.html`
  > DOJ EDVA press release (2024-09-26): "Two Russian nationals charged in
> connection with operating billion-dollar money laundering services;
> Justice Department seizes web domains for multiple illicit crypto
> exchanges." The U.S. Secret Service obtained court authorization to
> seize domains associated with the UAPS and PM2BTC websites, and a
> District of Maryland seizure order took the Cryptex.net and Cryptex.one
> domains (the cryptocurrency money-laundering exchange "Cryptex");
> working with Dutch partners the action shut down Cryptex. Sergey
> Sergeevich Ivanov (operator of UAPS / PinPays / PM2BTC, associated with
> Cryptex) and Timur Kamilevich Shakhmametov (Joker's Stash) were charged.
> Wayback 20240926181943 pinned. Grep of the captured body confirms
> "seizes web domains", "Secret Service has obtained court authorization
> to seize domains associated with the UAPS and PM2BTC websites",
> "Cryptex.net", "Cryptex.one", "shut down Cryptex".

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Cryptex / UAPS / PM2BTC (Ivanov & Shakhmametov)
- **Canonical domains**: `cryptex.net`, `cryptex.one`

> Cryptex (Cryptex.net / Cryptex.one cryptocurrency money-laundering
> exchange), the UAPS and PM2BTC payment/exchange services, and named
> operators Sergey Sergeevich Ivanov and Timur Kamilevich Shakhmametov.
> Marked subset: the named operators + their crypto-exchange/payment vehicles
> + the seized domains, not an enumerated set of users. The press release
> references blockchain-traced addresses (~$1.15B in flows) but does not
> enumerate specific on-chain addresses in the captured body, so none are
> asserted here.

## 3. Changed-layer observations (supports the scoped claim)

### l4_frontend · attribution: `direct` · Δt = 0h

**Event label**: `doj_secret_service_seizes_cryptex_uaps_pm2btc_domains`

**Timestamp**: `2024-09-26 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_legal`**
  - URL: <https://www.justice.gov/usao-edva/pr/two-russian-nationals-charged-connection-operating-billion-dollar-money-laundering>
  - Wayback: <https://web.archive.org/web/20240926181943/https://www.justice.gov/usao-edva/pr/two-russian-nationals-charged-connection-operating-billion-dollar-money-laundering>
  - body_hash: `sha256:c5c9eace590dee38f8593a4d597471e844caf7d670e914be663e5d0ff02f9213`
  - body_path: `sources/http_captures/cryptex-uaps-pm2btc-ivanov-shakhmametov-doj-2024/primary/web.archive.org__web-20240926000000-https-www.justice.gov-usao-edva-pr-two-russian-nationals-charged-connection-operating-billion-dollar-money-laundering__a7acbbf27a.html`
  > DOJ EDVA 2024-09-26: Secret Service seized the UAPS and PM2BTC
> domains and a District of Maryland order took Cryptex.net/Cryptex.one.
> attribution=direct: the named state action seized the named
> operational frontend domains.

### offramp_cex · attribution: `direct` · Δt = 0h

**Event label**: `cryptex_uaps_pm2btc_exchange_services_shut_down`

**Timestamp**: `2024-09-26 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_legal`**
  - URL: <https://www.justice.gov/usao-edva/pr/two-russian-nationals-charged-connection-operating-billion-dollar-money-laundering>
  - Wayback: <https://web.archive.org/web/20240926181943/https://www.justice.gov/usao-edva/pr/two-russian-nationals-charged-connection-operating-billion-dollar-money-laundering>
  - body_hash: `sha256:c5c9eace590dee38f8593a4d597471e844caf7d670e914be663e5d0ff02f9213`
  - body_path: `sources/http_captures/cryptex-uaps-pm2btc-ivanov-shakhmametov-doj-2024/primary/web.archive.org__web-20240926000000-https-www.justice.gov-usao-edva-pr-two-russian-nationals-charged-connection-operating-billion-dollar-money-laundering__a7acbbf27a.html`
  > DOJ EDVA 2024-09-26: the coordinated US/Dutch action shut down the
> Cryptex crypto exchange and the UAPS/PM2BTC payment-exchange
> services. attribution=direct: the named state action terminated the
> named exchange services.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `08595e8`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

