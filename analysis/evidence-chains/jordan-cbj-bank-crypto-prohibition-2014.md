# Evidence chain — `jordan-cbj-bank-crypto-prohibition-2014`

**Status**: `admitted` · **Stratum**: `S4_nation_state` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-02` · **Source commit**: `84e7c21` · **Schema**: `0.2.0` · **Event last_verified**: `2026-06-02` · **Tool version**: `0.1.0` · **Generated**: `2026-06-02T00:04:45Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> The Central Bank of Jordan Circular No. 1/1/2451 of 2014-02-20 prohibited licensed
> banks, financial companies, exchange companies, and payment-card companies from
> dealing in Bitcoin / virtual currency, exchanging it for any other currency, opening
> customer accounts to deal with it, or sending/receiving transfers against it for
> buying or selling. The offramp_cex layer carries the load-bearing direct-attribution
> observation.

## 1. Trigger

- **Type**: `nation_state_block`
- **Actor**: `JO_CBJ`
- **Timestamp**: `2014-02-20 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_government`**
  - URL: <https://www.cbj.gov.jo/ebv4.0/root_storage/en/eb_list_page/43d7c49d-bc5a-49d0-9706-88c4d2b69c3d.pdf>
  - body_hash: `sha256:ae9d42c14ef10bd12b4e49931a54458ce0c101801b622c7437e5c99d919ec352`
  - body_path: `sources/http_captures/jordan-cbj-bank-crypto-prohibition-2014/primary-cbj-circular-v1/www.cbj.gov.jo__ebv4.0-root_storage-en-eb_list_page-43d7c49d-bc5a-49d0-9706-88c4d2b69c3d.pdf__b9ea6f6884.bin`
  > Official Central Bank of Jordan English translation of Circular No.
> 1/1/2451 dated 2014-02-20. The PDF states that, for the safety of the
> financial and banking system and national economy, the Central Bank
> prohibits all banks and financial companies subject to its supervision,
> exchange companies, and payment card companies from dealing with Bitcoin
> / virtual currency in any form, exchanging it for any other currency,
> opening customer accounts to deal with it, or sending/receiving transfers
> against it for buying or selling. The PDF notes the Arabic version is the
> adopted legal text; the English translation is claim-usable for this
> corpus after local capture.
- **`supporting_journalism`**
  - URL: <https://web.archive.org/web/20140301000000/https://jordantimes.com/news/local/central-bank-warns-against-using-bitcoin>
  - Wayback: <https://web.archive.org/web/20150710120306/http://www.jordantimes.com/news/local/central-bank-warns-against-using-bitcoin>
  - body_hash: `sha256:9f9f631cf97a11196c95f74397f8bcb878d642df7f154cb90368cce2c9ad7377`
  - body_path: `sources/http_captures/jordan-cbj-bank-crypto-prohibition-2014/primary/web.archive.org__web-20140301000000-https-jordantimes.com-news-local-central-bank-warns-against-using-bitcoin__4e33a43799.html`
  > Jordan Times report dated 2014-02-22 ("Central bank warns against using
> bitcoin"). Maha Bahu, executive director of the payment services department
> at the Central Bank of Jordan (CBJ), confirms by phone that the CBJ "issued
> a circular to all banks operating in the Kingdom, currency exchange companies,
> financial companies and the payment service companies prohibiting them from
> dealing with virtual currencies, particularly in bitcoins." Verified in the
> captured body: the circular text is the operative restriction (an institutional
> debanking/dealing prohibition), not merely a non-recognition warning. The
> Retained as contemporaneous corroboration after the official CBJ circular
> PDF was pinned. Wayback date-prefix resolved to the 2015-07-10 memento of
> the same article.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Jordanian banks / exchange / payment-card companies (CBJ circular class)
- **Chains**: `bitcoin`

> Canonical target is the CBJ circular itself, addressed as a class-level
> prohibition to licensed banks, financial companies, exchange companies, and
> payment-card companies operating in Jordan, barring them from dealing in
> Bitcoin / virtual currency, exchanging it for other currency, opening accounts
> to deal with it, or sending/receiving transfers against it for buying or
> selling. The circular does not name specific exchanges, intermediaries,
> addresses, or domains; enumeration=subset because the prohibition addresses a
> regulated-institution class without a fixed enumerated roster, matching the
> China 2013 / Nigeria 2021 banking-rail-severance convention.

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `direct` · Δt = 0h

**Event label**: `banking_and_payment_channel_to_crypto_prohibited_industry_wide`

**Timestamp**: `2014-02-20 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_government`**
  - URL: <https://www.cbj.gov.jo/ebv4.0/root_storage/en/eb_list_page/43d7c49d-bc5a-49d0-9706-88c4d2b69c3d.pdf>
  - body_hash: `sha256:ae9d42c14ef10bd12b4e49931a54458ce0c101801b622c7437e5c99d919ec352`
  - body_path: `sources/http_captures/jordan-cbj-bank-crypto-prohibition-2014/primary-cbj-circular-v1/www.cbj.gov.jo__ebv4.0-root_storage-en-eb_list_page-43d7c49d-bc5a-49d0-9706-88c4d2b69c3d.pdf__b9ea6f6884.bin`
  > Official CBJ Circular No. 1/1/2451 dated 2014-02-20. The circular is
> the load-bearing source for attribution=direct and the corrected
> trigger/observation date.
- **`supporting_journalism`**
  - URL: <https://web.archive.org/web/20140301000000/https://jordantimes.com/news/local/central-bank-warns-against-using-bitcoin>
  - Wayback: <https://web.archive.org/web/20150710120306/http://www.jordantimes.com/news/local/central-bank-warns-against-using-bitcoin>
  - body_hash: `sha256:9f9f631cf97a11196c95f74397f8bcb878d642df7f154cb90368cce2c9ad7377`
  - body_path: `sources/http_captures/jordan-cbj-bank-crypto-prohibition-2014/primary/web.archive.org__web-20140301000000-https-jordantimes.com-news-local-central-bank-warns-against-using-bitcoin__4e33a43799.html`
  > Jordan Times 2014-02-22 report quoting the CBJ payment-services director:
> the CBJ "issued a circular to all banks operating in the Kingdom, currency
> exchange companies, financial companies and the payment service companies
> prohibiting them from dealing with virtual currencies, particularly in
> bitcoins." Retained as contemporaneous corroboration; the official CBJ PDF
> is now the load-bearing replayable anchor.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`china-pboc-crypto-ban-2013-12`](./china-pboc-crypto-ban-2013-12.md)
- [`nigeria-cbn-crypto-ban-2021`](./nigeria-cbn-crypto-ban-2021.md)
- [`india-rbi-crypto-ban-2018`](./india-rbi-crypto-ban-2018.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `84e7c21`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

