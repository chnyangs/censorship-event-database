# Evidence chain — `egypt-cbe-banking-law-194-2020`

**Status**: `admitted` · **Stratum**: `S4_nation_state` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-02` · **Source commit**: `c736a32` · **Schema**: `0.2.0` · **Event last_verified**: `2026-06-02` · **Tool version**: `0.1.0` · **Generated**: `2026-06-02T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "On 2020-09-15 Egypt promulgated Central Bank and Banking System Law No. 194 of
> 2020, whose Article 206 strictly prohibits the issuance, trading, promotion, or
> operation of cryptocurrency/electronic-money platforms or related activities
> without the required board license, backed by penalties that include
> imprisonment and fines up to EGP 10 million. The offramp_cex layer carries the
> load-bearing direct-attribution observation at class level."

## 1. Trigger

- **Type**: `nation_state_block`
- **Actor**: `EG_CBE`
- **Timestamp**: `2020-09-15 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_government`**
  - URL: <https://fra.gov.eg/regulations/%D9%82%D8%A7%D9%86%D9%88%D9%86-%D8%B1%D9%82%D9%85-194-%D9%84%D8%B3%D9%86%D8%A9-2020/>
  - body_hash: `sha256:3010c9baac36284c3fbf1aeb04f9f859d6a4ab80af0fbe3c2255aa2aeb93393a`
  - body_path: `sources/http_captures/egypt-cbe-banking-law-194-2020/primary-fra-law-v1/fra.gov.eg__regulations-D9-82-D8-A7-D9-86-D9-88-D9-86--D8-B1-D9-82-D9-85-194--D9-84-D8-B3-D9-86-D8-A9-2020__059ec583b5.html`
  > Official Egyptian Financial Regulatory Authority regulations page for
> Law No. 194 of 2020 on the Central Bank and banking system. The captured
> page identifies the law and links the official PDF used below.
- **`primary_legal`**
  - URL: <https://fra.gov.eg/wp-content/uploads/2025/01/%D9%82%D8%A7%D9%86%D9%88%D9%86-%D8%A7%D9%84%D8%A8%D9%86%D9%83-%D8%A7%D9%84%D9%85%D8%B1%D9%83%D8%B2%D9%8A-%D8%A8%D8%A7%D9%84%D8%A7%D8%B3%D8%AA%D8%AF%D8%B1%D8%A7%D9%83.pdf>
  - body_hash: `sha256:349b17f58a17f3025a35747f9fafa5739eb0ed01e02ffdf050fadf0671f8706a`
  - body_path: `sources/http_captures/egypt-cbe-banking-law-194-2020/primary-fra-law-v1/fra.gov.eg__wp-content-uploads-2025-01-D9-82-D8-A7-D9-86-D9-88-D9-86--D8-A7-D9-84-D8-A8-D9-86-D9-83--D8-A7-D9-84-D9-85-D8-B1-D9-83-D8-B2-D9-8A--D8-A8-D8-A7-D9-84-D8-A7__298496545b.bin`
  > Official image-only PDF of Law No. 194 of 2020, linked from the FRA
> regulations page. Rendered PDF page 102 shows Article 206 prohibiting,
> without a board-issued license, the issuance, trading, promotion,
> platform creation/operation, or related activities for cryptocurrency
> and electronic money. Rendered PDF page 110 shows the penalties chapter
> including violations of Article 206, with imprisonment and fines from
> EGP 1 million to EGP 10 million.
- **`supporting_journalism`**
  - URL: <https://web.archive.org/web/20260117012007/https://youssrysaleh.com/en/cryptocurrency-legality-in-egypt/>
  - Wayback: <https://web.archive.org/web/20260117012007/https://youssrysaleh.com/en/cryptocurrency-legality-in-egypt/>
  - body_hash: `sha256:9bd42acfbb503ff79c5319ca30f3deb48f4ce3f831236bf0b7057b2f9519efea`
  - body_path: `sources/http_captures/egypt-cbe-banking-law-194-2020/primary/web.archive.org__web-20260117012007-https-youssrysaleh.com-en-cryptocurrency-legality-in-egypt__07ac104a1e.html`
  > Youssry Saleh Law Firm (Egypt) analysis "Cryptocurrency legality in
> Egypt." Captured page states: "The Egyptian regulatory framework on
> cryptocurrencies is based on the Central Bank and Banking System Law No.
> 194 of 2020. Under the letter of Article 206 of this law, the issuance,
> trading, promotion, or operation of any platform that deals with crypto
> assets without prior approval from the Central Bank of Egypt (CBE) is
> strictly prohibited. Violating any of these provisions attracts
> far-reaching penalties, including imprisonment, while fines of up to EGP
> 1 million to EGP 10 million can also apply." Law No. 194 of 2020 was
> promulgated/published 2020-09-15 (entry into force 2020-09-16). Egyptian
> law-firm secondary analysis reproducing the statutory prohibition;
> retained only as English-language corroboration after the official FRA
> law PDF was pinned.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Egyptian crypto users / exchanges / platform operators (class)

> All persons and platforms in Egypt barred from issuing, trading, promoting,
> or operating any crypto-asset platform without the license required by
> Article 206 of Law No. 194 of 2020. No specific exchange is enumerated;
> class-level restriction matching the sibling nation-state-prohibition
> convention (Myanmar 2020, Cambodia 2018).

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `direct` · Δt = 0h

**Event label**: `crypto_issuance_trading_promotion_platform_prohibited_article_206`

**Timestamp**: `2020-09-15 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_government`**
  - URL: <https://fra.gov.eg/regulations/%D9%82%D8%A7%D9%86%D9%88%D9%86-%D8%B1%D9%82%D9%85-194-%D9%84%D8%B3%D9%86%D8%A9-2020/>
  - body_hash: `sha256:3010c9baac36284c3fbf1aeb04f9f859d6a4ab80af0fbe3c2255aa2aeb93393a`
  - body_path: `sources/http_captures/egypt-cbe-banking-law-194-2020/primary-fra-law-v1/fra.gov.eg__regulations-D9-82-D8-A7-D9-86-D9-88-D9-86--D8-B1-D9-82-D9-85-194--D9-84-D8-B3-D9-86-D8-A9-2020__059ec583b5.html`
  > FRA regulations page identifying Law No. 194 of 2020 and linking the
> official law PDF.
- **`primary_legal`**
  - URL: <https://fra.gov.eg/wp-content/uploads/2025/01/%D9%82%D8%A7%D9%86%D9%88%D9%86-%D8%A7%D9%84%D8%A8%D9%86%D9%83-%D8%A7%D9%84%D9%85%D8%B1%D9%83%D8%B2%D9%8A-%D8%A8%D8%A7%D9%84%D8%A7%D8%B3%D8%AA%D8%AF%D8%B1%D8%A7%D9%83.pdf>
  - body_hash: `sha256:349b17f58a17f3025a35747f9fafa5739eb0ed01e02ffdf050fadf0671f8706a`
  - body_path: `sources/http_captures/egypt-cbe-banking-law-194-2020/primary-fra-law-v1/fra.gov.eg__wp-content-uploads-2025-01-D9-82-D8-A7-D9-86-D9-88-D9-86--D8-A7-D9-84-D8-A8-D9-86-D9-83--D8-A7-D9-84-D9-85-D8-B1-D9-83-D8-B2-D9-8A--D8-A8-D8-A7-D9-84-D8-A7__298496545b.bin`
  > Official image-only PDF of Law No. 194 of 2020. Rendered page 102
> shows Article 206's cryptocurrency/electronic-money restriction, and
> rendered page 110 shows Article 225's penalty provision including
> Article 206 violations.
- **`supporting_journalism`**
  - URL: <https://web.archive.org/web/20260117012007/https://youssrysaleh.com/en/cryptocurrency-legality-in-egypt/>
  - Wayback: <https://web.archive.org/web/20260117012007/https://youssrysaleh.com/en/cryptocurrency-legality-in-egypt/>
  - body_hash: `sha256:9bd42acfbb503ff79c5319ca30f3deb48f4ce3f831236bf0b7057b2f9519efea`
  - body_path: `sources/http_captures/egypt-cbe-banking-law-194-2020/primary/web.archive.org__web-20260117012007-https-youssrysaleh.com-en-cryptocurrency-legality-in-egypt__07ac104a1e.html`
  > English-language corroboration of the Article 206 crypto prohibition;
> no longer load-bearing after the official FRA legal PDF was pinned.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`myanmar-cbm-crypto-prohibition-directive-9-2020`](./myanmar-cbm-crypto-prohibition-directive-9-2020.md)
- [`cambodia-nbc-joint-crypto-prohibition-2018-05`](./cambodia-nbc-joint-crypto-prohibition-2018-05.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `c736a32`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

