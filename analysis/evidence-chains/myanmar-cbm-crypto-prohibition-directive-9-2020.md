# Evidence chain — `myanmar-cbm-crypto-prohibition-directive-9-2020`

**Status**: `admitted` · **Stratum**: `S4_nation_state` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-02` · **Source commit**: `cdc9fa8` · **Schema**: `0.2.0` · **Event last_verified**: `2026-06-02` · **Tool version**: `0.1.0` · **Generated**: `2026-06-02T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "On 2020-05-15 the Central Bank of Myanmar issued Notification No. 9/2020
> stating that CBM does not allow financial institutions, including banks, to
> deal with digital currency and does not recognize digital currency as legal
> currency; it names Bitcoin, Litecoin, Ethereum, and Perfect Money as examples
> of digital currencies being dealt/exchanged through Facebook accounts or
> websites and states that legal violations may be punished by imprisonment,
> fine, or both. The offramp_cex layer carries the load-bearing
> direct-attribution observation at class level."

## 1. Trigger

- **Type**: `nation_state_block`
- **Actor**: `MM_CBM`
- **Timestamp**: `2020-05-15 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_government`**
  - URL: <https://www.mfiu.gov.mm/sites/default/files/document/files/2020%20Annual%20Report%20%28English%20Version%29.pdf>
  - body_hash: `sha256:34c72f7b4b9149a3da0bf9aa77a26c09b667a458b58dc4b052005d8f9e639a17`
  - body_path: `sources/http_captures/myanmar-cbm-crypto-prohibition-directive-9-2020/primary-mfiu-annual-report-v1/www.mfiu.gov.mm__sites-default-files-document-files-2020-20Annual-20Report-20-28English-20Version-29.pdf__1b0a29a98a.bin`
  > Official Myanmar Financial Intelligence Unit AML/CFT 2020 Annual Report
> PDF. Annex (S) reproduces Central Bank of Myanmar Notification No.
> 9/2020 dated 2020-05-15. Extracted text shows CBM states it does not
> allow financial institutions, including banks, to deal with digital
> currency, does not recognize digital currency as legal currency, names
> Bitcoin, Litecoin, Ethereum, and Perfect Money as examples of digital
> currencies being dealt/exchanged through Facebook accounts or websites,
> and states that legal violations may be punished by imprisonment, fine,
> or both.
- **`supporting_journalism`**
  - URL: <https://web.archive.org/web/20260120112720/https://www.tilleke.com/insights/myanmars-central-bank-issues-further-warning-against-crypto-trading/>
  - Wayback: <https://web.archive.org/web/20260120112720/https://www.tilleke.com/insights/myanmars-central-bank-issues-further-warning-against-crypto-trading/>
  - body_hash: `sha256:0cd2cf34c9e091564c0875bfbf30099d5b3dda95acdd2a35738889da5bae2e48`
  - body_path: `sources/http_captures/myanmar-cbm-crypto-prohibition-directive-9-2020/primary/web.archive.org__web-20260120112720-https-www.tilleke.com-insights-myanmars-central-bank-issues-further-warning-against-crypto-trading__53bb7afc72.html`
  > Tilleke & Gibbins legal-update insight ("Myanmar's Central Bank Issues
> Further Warning against Crypto Trading"). Captured page states verbatim:
> "in May 2020, the CBM issued Notification No. 9/2020, prohibiting all
> persons residing in Myanmar from engaging in the sale, purchase, or
> exchange of unregulated digital currencies. The list of prohibited
> currencies includes widely recognized cryptocurrencies such as Bitcoin
> (BTC), Litecoin (LTD), Ethereum (ETH), and Perfect Money (PM)." The page
> further states that after the 2020 notification the CBM "has pursued
> legal action," that violations "may result in imprisonment, fines, or
> both, in accordance with the Central Bank of Myanmar Law, the Anti-Money
> Laundering Law and the Financial Institutions Law," and that the CBM has
> not granted permission to financial institutions within Myanmar to trade
> digital currencies (the Foreign Exchange Management Law and Financial
> Institutions Law "cement the illegality of cryptocurrency transactions").
> Law-firm secondary interpretation retained as corroboration; no longer
> load-bearing after the official MFIU annual-report reproduction of the
> CBM notification was pinned.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Myanmar financial institutions / digital-currency dealing class

> CBM Notification No. 9/2020 states that CBM does not allow financial
> institutions, including banks, to deal with digital currency or recognize
> digital currency as legal currency. It also names Bitcoin, Litecoin,
> Ethereum, and Perfect Money as examples of digital currencies being
> dealt/exchanged through personal Facebook accounts or websites, and warns
> that legal violations may be punished. No specific exchange or platform is
> enumerated; scoped as a class-level financial-institution / trading-service
> restriction rather than a complete named-provider list.

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `direct` · Δt = 0h

**Event label**: `financial_institution_digital_currency_dealing_not_allowed_directive_9_2020`

**Timestamp**: `2020-05-15 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_government`**
  - URL: <https://www.mfiu.gov.mm/sites/default/files/document/files/2020%20Annual%20Report%20%28English%20Version%29.pdf>
  - body_hash: `sha256:34c72f7b4b9149a3da0bf9aa77a26c09b667a458b58dc4b052005d8f9e639a17`
  - body_path: `sources/http_captures/myanmar-cbm-crypto-prohibition-directive-9-2020/primary-mfiu-annual-report-v1/www.mfiu.gov.mm__sites-default-files-document-files-2020-20Annual-20Report-20-28English-20Version-29.pdf__1b0a29a98a.bin`
  > Official MFIU Annual Report PDF, Annex (S), reproducing CBM
> Notification No. 9/2020 dated 2020-05-15. The extracted text directly
> supports the financial-institution digital-currency dealing
> restriction and the no-legal-currency recognition statement.
- **`supporting_journalism`**
  - URL: <https://web.archive.org/web/20260120112720/https://www.tilleke.com/insights/myanmars-central-bank-issues-further-warning-against-crypto-trading/>
  - Wayback: <https://web.archive.org/web/20260120112720/https://www.tilleke.com/insights/myanmars-central-bank-issues-further-warning-against-crypto-trading/>
  - body_hash: `sha256:0cd2cf34c9e091564c0875bfbf30099d5b3dda95acdd2a35738889da5bae2e48`
  - body_path: `sources/http_captures/myanmar-cbm-crypto-prohibition-directive-9-2020/primary/web.archive.org__web-20260120112720-https-www.tilleke.com-insights-myanmars-central-bank-issues-further-warning-against-crypto-trading__53bb7afc72.html`
  > English-language law-firm interpretation of the same CBM notification.
> Retained as corroboration only; the direct attribution now rests on the
> official MFIU annual-report reproduction of the CBM notification.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`cambodia-nbc-joint-crypto-prohibition-2018-05`](./cambodia-nbc-joint-crypto-prohibition-2018-05.md)
- [`nepal-nrb-bitcoin-ban-2017-08`](./nepal-nrb-bitcoin-ban-2017-08.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `cdc9fa8`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

