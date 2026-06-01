# Evidence chain — `bitmex-fincen-2024`

**Status**: `admitted` · **Stratum**: `S3_doj_sec_cftc_fiod` · **Shape**: `null_event` (0 changed layer(s): none) · **Tier**: `null_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `c5a73a6` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-20` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T03:21:56Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "The 2024-07-10 corporate BSA guilty plea by HDR Global Trading Limited
> (BitMEX) and the resulting 2025-01-15 $100M criminal fine are downstream
> resolutions of the 2020-10-01 enforcement chain (see
> bitmex-cftc-doj-2020) and produced no incremental cascade in the
> dataset: US-vantage retail access was already severed in 2020 and the
> 2024 disposition is monetary / probationary only. Recorded as a
> null_event denominator-control row for the 2024-vintage offshore-exchange
> enforcement stratum."

## 1. Trigger

- **Type**: `doj_indictment`
- **Actor**: `US_DOJ_SDNY`
- **Timestamp**: `2024-07-10 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://www.justice.gov/usao-sdny/pr/global-cryptocurrency-exchange-bitmex-pleads-guilty-bank-secrecy-act-offense>
  - Wayback: <https://web.archive.org/web/20240710201047/https://www.justice.gov/usao-sdny/pr/global-cryptocurrency-exchange-bitmex-pleads-guilty-bank-secrecy-act-offense>
  - body_hash: `sha256:0147c00f36bee0d1f22054254864fbc143a476112f6933b5bf05a27dc7605c83`
  - body_path: `sources/http_captures/bitmex-fincen-2024/primary/web.archive.org__web-20240710201047-https-www.justice.gov-usao-sdny-pr-global-cryptocurrency-exchange-bitmex-pleads-guilty-bank-secrecy-act-offense__61d5257c8a.html`
  > DOJ SDNY press release (2024-07-10): "Global Cryptocurrency Exchange
> BitMEX Pleads Guilty To Bank Secrecy Act Offense." HDR Global
> Trading Limited (operating as BitMEX) entered a corporate guilty
> plea for willful failure to establish, implement, and maintain an
> adequate AML program in violation of the Bank Secrecy Act from
> 2015-2020. This is the corporate-defendant resolution that
> followed the 2020-10-01 CFTC + DOJ filings (see related event
> bitmex-cftc-doj-2020) and the 2021-08-10 $100M CFTC + FinCEN
> consent orders, and the 2022 individual-founder BSA plea
> agreements. Sentencing occurred 2025-01-15 with an additional
> $100M criminal fine.
- **`primary_legal`**
  - URL: <https://www.justice.gov/usao-sdny/pr/global-cryptocurrency-exchange-bitmex-fined-100-million-violating-bank-secrecy-act>
  - Wayback: <https://web.archive.org/web/20250115213223/https://www.justice.gov/usao-sdny/pr/global-cryptocurrency-exchange-bitmex-fined-100-million-violating-bank-secrecy-act>
  - body_hash: `sha256:a0f7d164078d4d3ceee2599157e8509a3cdc7254de3ab2c7a5ce3dec5ed41168`
  - body_path: `sources/http_captures/bitmex-fincen-2024/primary/web.archive.org__web-20250115213223-https-www.justice.gov-usao-sdny-pr-global-cryptocurrency-exchange-bitmex-fined-100-million-violating-bank-secrecy-act__9cd27f0931.html`
  > DOJ SDNY press release (2025-01-15): "Global Cryptocurrency
> Exchange BitMEX Fined $100 Million For Violating The Bank
> Secrecy Act." Sentencing judgment imposing the criminal fine
> plus two years' corporate probation, downstream from the
> 2024-07-10 guilty plea.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: BitMEX (HDR Global Trading Limited)
- **Chains**: `bitcoin`
- **Canonical domains**: `bitmex.com`

> HDR Global Trading Limited (the corporate defendant entering the BSA
> guilty plea), operating the BitMEX exchange platform. Related entities
> in the BitMEX integrated common enterprise (100x Holding Limited, ABS
> Global Trading Limited, Shine Effort Inc Limited, HDR Global Services
> (Bermuda) Limited) were the co-respondents in the parent 2020-2021
> CFTC + FinCEN resolutions. The 2024 plea is the corporate-defendant
> resolution tail of the same enforcement chain; named individual
> founders (Hayes, Delo, Reed, Dwyer) already pleaded individually in
> 2022 and are not new defendants in this 2024 action.

## 3. Changed-layer observations (supports the scoped claim)

*No observed_change entries. This is a `null_event`; see §4 for observed_no_change evidence supporting the null claim.*

## 4. No-change observations (where applicable)

### offramp_cex — `bitmex_us_rails_no_incremental_change_after_corporate_bsa_plea`

**Window**: `2024-07-10 00:00:00+00:00` → `2025-01-15 23:59:59+00:00`

**Sources**:

- **`primary_legal`**
  - URL: <https://www.justice.gov/usao-sdny/pr/global-cryptocurrency-exchange-bitmex-pleads-guilty-bank-secrecy-act-offense>
  - Wayback: <https://web.archive.org/web/20240710201047/https://www.justice.gov/usao-sdny/pr/global-cryptocurrency-exchange-bitmex-pleads-guilty-bank-secrecy-act-offense>
  - body_hash: `sha256:0147c00f36bee0d1f22054254864fbc143a476112f6933b5bf05a27dc7605c83`
  - body_path: `sources/http_captures/bitmex-fincen-2024/primary/web.archive.org__web-20240710201047-https-www.justice.gov-usao-sdny-pr-global-cryptocurrency-exchange-bitmex-pleads-guilty-bank-secrecy-act-offense__61d5257c8a.html`
  > DOJ SDNY press release describes the corporate BSA plea and
> forthcoming sentencing. No new rails-level restriction was
> imposed: US-resident retail access was already severed in 2020;
> the 2024 resolution is monetary and probationary. observed_no_change
> row anchors the null-event status of this downstream resolution.

## 5. Honest coverage gaps

- **l4_frontend** (`not_measured`): No new user-facing geo-block or KYC mandate observed in connection

## 7. Related events

- [`bitmex-cftc-doj-2020`](./bitmex-cftc-doj-2020.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `c5a73a6`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

