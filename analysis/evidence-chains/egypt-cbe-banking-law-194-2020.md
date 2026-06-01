# Evidence chain — `egypt-cbe-banking-law-194-2020`

**Status**: `admitted` · **Stratum**: `S4_nation_state` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `db44253` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-31` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T04:52:47Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "On 2020-09-15 Egypt promulgated Central Bank and Banking System Law No. 194 of
> 2020, whose Article 206 strictly prohibits the issuance, trading, promotion, or
> operation of any crypto-asset platform without prior CBE approval (no license
> issued), backed by imprisonment and fines up to EGP 10 million. The offramp_cex
> layer carries the load-bearing plausible-attribution observation at class
> level."

## 1. Trigger

- **Type**: `nation_state_block`
- **Actor**: `EG_CBE`
- **Timestamp**: `2020-09-15 00:00:00+00:00` (precision: `day`)

### Trigger citations

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
> law-firm secondary analysis reproducing the statutory prohibition; the
> official gazette / CBE primary instrument text was not captured in this
> draft pass.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Egyptian crypto users / exchanges / platform operators (class)

> All persons and platforms in Egypt barred from issuing, trading, promoting,
> or operating any crypto-asset platform without prior CBE approval (Article
> 206, Law No. 194 of 2020). No CBE license has been issued, making the
> provision a de facto prohibition. No specific exchange enumerated;
> class-level prohibition matching the sibling nation-state-prohibition
> convention (Myanmar 2020, Cambodia 2018).

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `plausible` · Δt = 0h

**Event label**: `crypto_issuance_trading_promotion_platform_prohibited_article_206`

**Timestamp**: `2020-09-15 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`supporting_journalism`**
  - URL: <https://web.archive.org/web/20260117012007/https://youssrysaleh.com/en/cryptocurrency-legality-in-egypt/>
  - Wayback: <https://web.archive.org/web/20260117012007/https://youssrysaleh.com/en/cryptocurrency-legality-in-egypt/>
  - body_hash: `sha256:9bd42acfbb503ff79c5319ca30f3deb48f4ce3f831236bf0b7057b2f9519efea`
  - body_path: `sources/http_captures/egypt-cbe-banking-law-194-2020/primary/web.archive.org__web-20260117012007-https-youssrysaleh.com-en-cryptocurrency-legality-in-egypt__07ac104a1e.html`
  > attribution=plausible per codebook §1: the action is causally
> consistent with the named Article 206 of Law No. 194 of 2020, but the
> load-bearing captured evidence is law-firm secondary analysis (Youssry
> Saleh) reproducing the statute rather than the official gazette
> instrument text, and the prohibition is class-level (names no specific
> platform). A primary gazette / CBE instrument capture would be required
> to elevate to direct.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`myanmar-cbm-crypto-prohibition-directive-9-2020`](./myanmar-cbm-crypto-prohibition-directive-9-2020.md)
- [`cambodia-nbc-joint-crypto-prohibition-2018-05`](./cambodia-nbc-joint-crypto-prohibition-2018-05.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `db44253`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

