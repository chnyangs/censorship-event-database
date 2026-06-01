# Evidence chain — `cambodia-nbc-joint-crypto-prohibition-2018-05`

**Status**: `admitted` · **Stratum**: `S4_nation_state` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-02` · **Source commit**: `3f1a9f2` · **Schema**: `0.2.0` · **Event last_verified**: `2026-06-01` · **Tool version**: `0.1.0` · **Generated**: `2026-06-02T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "On 2018-05-11 the NBC, SECC and General-Commissariat of National Police
> issued a joint statement declaring the propagation, circulation, buying,
> selling, trading and settlement of cryptocurrencies illegal without a license
> from competent Cambodian authorities and subject to penalties under applicable
> laws. The offramp_cex layer carries the load-bearing direct-attribution
> observation at class level."

## 1. Trigger

- **Type**: `nation_state_block`
- **Actor**: `KH_NBC`
- **Timestamp**: `2018-05-11 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_government`**
  - URL: <https://www.nbc.gov.kh/download_files/news_and_events/news_eng/5223Joint_statement_NBC_SECC_POLICE_ENG.pdf>
  - Wayback: <https://web.archive.org/web/20260601125313/https://www.nbc.gov.kh/download_files/news_and_events/news_eng/5223Joint_statement_NBC_SECC_POLICE_ENG.pdf>
  - body_hash: `sha256:21ea89870f7dc2410603614d23f78f5d9e7cedf1de7d51151ecb05f275f54d7c`
  - body_path: `sources/http_captures/cambodia-nbc-joint-crypto-prohibition-2018-05/primary-nbc-pdf/www.nbc.gov.kh__download_files-news_and_events-news_eng-5223Joint_statement_NBC_SECC_POLICE_ENG.pdf__3b5478c840.bin`
  > Official NBC-hosted English PDF of the joint statement between the
> National Bank of Cambodia, the Securities and Exchange Commission of
> Cambodia, and the General-Commissariat of National Police. The PDF is
> dated Phnom Penh, 2018-05-11, and states that propagation, circulation,
> buying, selling, trading and settlement of cryptocurrencies without a
> license from competent authorities are illegal activities; unlicensed
> persons or legal entities shall be penalized under applicable laws.
- **`primary_government`**
  - URL: <https://www.nbc.gov.kh/english/news_and_events/news_info.php?id=380>
  - Wayback: <https://web.archive.org/web/20260601125236/https://www.nbc.gov.kh/english/news_and_events/news_info.php?id=380>
  - body_hash: `sha256:8c8215744a74e3fdbb52d7c302ae874eb2c212820cf4a59b5f681c1bfd444d7b`
  - body_path: `sources/http_captures/cambodia-nbc-joint-crypto-prohibition-2018-05/primary-nbc-page/www.nbc.gov.kh__english-news_and_events-news_info.php__8390f78670.html`
  > Official NBC news page for the same joint statement, published
> 2018-07-13, with the attached PDF download. The page restates the
> warning and penalty language for unlicensed cryptocurrency propagation,
> buying, selling, trading and settlement.
- **`supporting_journalism`**
  - URL: <https://web.archive.org/web/20180620031123/https://www.phnompenhpost.com/business/cryptos-illegal-kingdom-regulators>
  - Wayback: <https://web.archive.org/web/20180620031123/https://www.phnompenhpost.com/business/cryptos-illegal-kingdom-regulators>
  - body_hash: `sha256:c8acdc033a4946eef66dde5c4d2ae7858c2aec180a64696a3ba09b74ac99edb6`
  - body_path: `sources/http_captures/cambodia-nbc-joint-crypto-prohibition-2018-05/primary/web.archive.org__web-20180620031123-https-www.phnompenhpost.com-business-cryptos-illegal-kingdom-regulators__3512288dd1.html`
  > Phnom Penh Post, "Cryptos illegal in the Kingdom: regulators" (June 2018),
> reporting the joint statement issued 2018-05-11 by the National Bank of
> Cambodia (NBC), the Securities and Exchange Commission of Cambodia (SECC),
> and the General-Commissariat of National Police. The joint statement
> declared that the propagation, circulation, buying, selling, trading and
> settlement of cryptocurrencies without a license from competent
> authorities is illegal. Contemporaneous reporting captured via Wayback
> memento 2018-06-20; retained as corroboration now that the NBC official
> page and PDF are pinned.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Cambodian crypto exchanges / traders (class)

> Cambodian crypto users, exchanges and ICO/token operators as a class. The
> joint statement does not enumerate specific platforms; it declares
> unlicensed propagation, circulation, buying, selling, trading and settlement
> of cryptocurrencies illegal. Target treated as entity-class-level, matching
> the sibling nation-state prohibition convention (India 2018, Zimbabwe 2018).

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `direct` · Δt = 0h

**Event label**: `crypto_trading_and_settlement_declared_illegal_without_license`

**Timestamp**: `2018-05-11 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_government`**
  - URL: <https://www.nbc.gov.kh/download_files/news_and_events/news_eng/5223Joint_statement_NBC_SECC_POLICE_ENG.pdf>
  - Wayback: <https://web.archive.org/web/20260601125313/https://www.nbc.gov.kh/download_files/news_and_events/news_eng/5223Joint_statement_NBC_SECC_POLICE_ENG.pdf>
  - body_hash: `sha256:21ea89870f7dc2410603614d23f78f5d9e7cedf1de7d51151ecb05f275f54d7c`
  - body_path: `sources/http_captures/cambodia-nbc-joint-crypto-prohibition-2018-05/primary-nbc-pdf/www.nbc.gov.kh__download_files-news_and_events-news_eng-5223Joint_statement_NBC_SECC_POLICE_ENG.pdf__3b5478c840.bin`
  > Official NBC-hosted English PDF of the 2018-05-11 joint statement.
> attribution=direct: the named Cambodian authorities directly declare
> unlicensed cryptocurrency propagation, circulation, buying, selling,
> trading and settlement illegal and subject to penalties.
- **`primary_government`**
  - URL: <https://www.nbc.gov.kh/english/news_and_events/news_info.php?id=380>
  - Wayback: <https://web.archive.org/web/20260601125236/https://www.nbc.gov.kh/english/news_and_events/news_info.php?id=380>
  - body_hash: `sha256:8c8215744a74e3fdbb52d7c302ae874eb2c212820cf4a59b5f681c1bfd444d7b`
  - body_path: `sources/http_captures/cambodia-nbc-joint-crypto-prohibition-2018-05/primary-nbc-page/www.nbc.gov.kh__english-news_and_events-news_info.php__8390f78670.html`
  > Official NBC news page for the statement and PDF attachment; retained
> as the HTML primary-government anchor.
- **`supporting_journalism`**
  - URL: <https://web.archive.org/web/20180620031123/https://www.phnompenhpost.com/business/cryptos-illegal-kingdom-regulators>
  - Wayback: <https://web.archive.org/web/20180620031123/https://www.phnompenhpost.com/business/cryptos-illegal-kingdom-regulators>
  - body_hash: `sha256:c8acdc033a4946eef66dde5c4d2ae7858c2aec180a64696a3ba09b74ac99edb6`
  - body_path: `sources/http_captures/cambodia-nbc-joint-crypto-prohibition-2018-05/primary/web.archive.org__web-20180620031123-https-www.phnompenhpost.com-business-cryptos-illegal-kingdom-regulators__3512288dd1.html`
  > Contemporaneous Phnom Penh Post report retained as corroboration for
> public reception and named affected crypto projects; no longer the
> load-bearing source after the official NBC page and PDF were pinned.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`india-rbi-crypto-ban-2018`](./india-rbi-crypto-ban-2018.md)
- [`zimbabwe-rbz-circular-2-2018-golix-ban`](./zimbabwe-rbz-circular-2-2018-golix-ban.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `3f1a9f2`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

