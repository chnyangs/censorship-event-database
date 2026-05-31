# Evidence chain — `sri-lanka-cbsl-crypto-warning-fx-directive-2021`

**Status**: `admitted` · **Stratum**: `S4_nation_state` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `a4484c4` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-31` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "Sri Lanka's CBSL Foreign Exchange Act Direction No. 03 of 2021 (publicised
> 2021-04-09) prohibited debit/credit card (EFTC) payments for virtual-currency
> transactions, severing the bank-card payment channel for crypto in Sri Lanka.
> Effect captured at the offramp_cex layer at class level via the binding FX
> Direction text."

## 1. Trigger

- **Type**: `nation_state_block`
- **Actor**: `LK_CBSL`
- **Timestamp**: `2021-04-09 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://www.cbsl.gov.lk/sites/default/files/cbslweb_documents/laws/cdg/Foreign_Exchange_Act_Direction_No_3_of_2021_e.pdf>
  - Wayback: <https://web.archive.org/web/20210629054616id_/https://www.cbsl.gov.lk/sites/default/files/cbslweb_documents/laws/cdg/Foreign_Exchange_Act_Direction_No_3_of_2021_e.pdf>
  - body_hash: `sha256:b0a69b01b22e82e323f5fd477806f7e5c1520f93a437921d5ca6bcefad8f3a2c`
  - body_path: `sources/http_captures/sri-lanka-cbsl-crypto-warning-fx-directive-2021/primary/web.archive.org__web-20210601000000id_-https-www.cbsl.gov.lk-sites-default-files-cbslweb_documents-laws-cdg-Foreign_Exchange_Act_Direction_No_3_of_2021_e.pdf__ac4a9178d0.bin`
  > Central Bank of Sri Lanka, Department of Foreign Exchange, "Directions to
> Authorized Dealers on Electronic Fund Transfer Cards (EFTCs)", Directions
> No. 03 of 2021 under the Foreign Exchange Act, No. 12 of 2017, dated
> 2021-03-18. Paragraph 10.1 enumerates uses for which Authorized Dealers
> (banks) shall ensure EFTCs (debit/credit cards) shall NOT be used; item
> (b) is "Payments related to virtual currency transactions". This is the
> binding payment-rail instrument that prohibits bank-card payments for
> crypto. Captured PDF (8 pages, version 1.7) verified via pdftotext to
> contain the Paragraph 10.1.b virtual-currency restriction text and the
> "Virtual currency" definition (item vii). The CBSL publicised the
> restriction in its 2021-04-09 public-awareness notice (see second
> citation). Archived via Wayback 2021-06-29 (id_ raw capture).

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Sri Lankan banks (Authorized Dealers) / card-holding crypto users (class)

> Sri Lankan banks (Authorized Dealers) and their card-holding crypto users as
> a class. The FX Direction binds all ADs issuing EFTCs; no specific exchange
> or user is enumerated in the instrument. Target treated as entity-class-level.

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `direct` · Δt = 0h

**Event label**: `bank_card_payment_channel_for_crypto_prohibited`

**Timestamp**: `2021-04-09 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_legal`**
  - URL: <https://www.cbsl.gov.lk/sites/default/files/cbslweb_documents/laws/cdg/Foreign_Exchange_Act_Direction_No_3_of_2021_e.pdf>
  - Wayback: <https://web.archive.org/web/20210629054616id_/https://www.cbsl.gov.lk/sites/default/files/cbslweb_documents/laws/cdg/Foreign_Exchange_Act_Direction_No_3_of_2021_e.pdf>
  - body_hash: `sha256:b0a69b01b22e82e323f5fd477806f7e5c1520f93a437921d5ca6bcefad8f3a2c`
  - body_path: `sources/http_captures/sri-lanka-cbsl-crypto-warning-fx-directive-2021/primary/web.archive.org__web-20210601000000id_-https-www.cbsl.gov.lk-sites-default-files-cbslweb_documents-laws-cdg-Foreign_Exchange_Act_Direction_No_3_of_2021_e.pdf__ac4a9178d0.bin`
  > FX Direction No. 03 of 2021 Para 10.1.b is the legal instrument
> prohibiting EFTC (debit/credit card) payments for virtual-currency
> transactions. attribution=direct because the directive explicitly
> mandates the card-payment-channel cut-off.
- **`primary_government`**
  - URL: <https://www.cbsl.gov.lk/en/news/public-awareness-on-risks-in-investing-in-virtual-currencies-in-sri-lanka>
  - Wayback: <https://web.archive.org/web/20210412052323/https://www.cbsl.gov.lk/en/news/public-awareness-on-risks-in-investing-in-virtual-currencies-in-sri-lanka>
  - body_hash: `sha256:1b758b8a26b5417c39f47b62c77d060de13e6676e386160a33fdec7e5f1a464d`
  - body_path: `sources/http_captures/sri-lanka-cbsl-crypto-warning-fx-directive-2021/primary/web.archive.org__web-20210420000000-https-www.cbsl.gov.lk-en-news-public-awareness-on-risks-in-investing-in-virtual-currencies-in-sri-lanka__f675477cdb.html`
  > CBSL public-awareness notice (Wayback 2021-04-12 snapshot, page itself
> dated April 2021) that publicises the EFTC card-payment prohibition,
> states no ICOs/mining/Virtual Currency Exchanges are authorized, and
> that buying virtual currency from abroad violates the Foreign Exchange
> Act. Corroborates the binding FX Direction at the public-notice layer.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`nigeria-cbn-crypto-ban-2021`](./nigeria-cbn-crypto-ban-2021.md)
- [`india-rbi-crypto-ban-2018`](./india-rbi-crypto-ban-2018.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `a4484c4`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

