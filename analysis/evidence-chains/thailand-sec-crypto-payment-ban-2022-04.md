# Evidence chain — `thailand-sec-crypto-payment-ban-2022-04`

**Status**: `admitted` · **Stratum**: `S4_nation_state` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `97f58fa` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-31` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> SEC Thailand Notification No. Gor Tor. 5/2565 (announced 23 March 2022, effective 1 April
> 2022) prohibited all licensed Thai digital-asset business operators from supporting or
> facilitating the use of digital assets as a means of payment for goods or services,
> severing the licensed crypto-as-payment channel in Thailand. The offramp_cex layer carries
> the load-bearing direct-attribution observation.

## 1. Trigger

- **Type**: `nation_state_block`
- **Actor**: `TH_SEC`
- **Timestamp**: `2022-04-01 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_government`**
  - URL: <https://web.archive.org/web/20220716015641/https://www.sec.or.th/EN/Pages/News_Detail.aspx?SECID=9366>
  - Wayback: <https://web.archive.org/web/20220716015641/https://www.sec.or.th/EN/Pages/News_Detail.aspx?SECID=9366>
  - body_hash: `sha256:11a67a6d0eafe3d93ddcda40594af9082fb4e8c3892bffa2cf9bdd7bef454da3`
  - body_path: `sources/http_captures/thailand-sec-crypto-payment-ban-2022-04/primary/web.archive.org__web-20220716015641-https-www.sec.or.th-EN-Pages-News_Detail.aspx__b7b092d9f9.html`
  > SEC Thailand press release "SEC issues regulation prohibiting digital asset
> business operators from facilitating the use of digital assets as a means of
> payment", dated Bangkok 23 March 2022 (No. 39/2022). Captured body verifies the
> operative text: the SEC issued regulation requiring "digital asset business
> operators to avert support or promotion of the use of digital assets as a means
> of payment for goods and services. This is to prevent potential impacts on the
> country's financial system and economy." Existing operators "are required to
> comply with the regulations within 30 days as from 1 April 2022." The body also
> records that "The BOT [Bank of Thailand] and the SEC previously discussed and
> reviewed the benefits and risks of digital assets" — confirming the joint
> SEC/BOT origin. The regulation is SEC Notification No. Gor Tor. 5/2565.
> Effective date 1 April 2022 used as the trigger timestamp.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Thai licensed digital-asset business operators (SEC Gor Tor 5/2565 class)

> Canonical target is SEC Notification No. Gor Tor. 5/2565, addressed as a class-level
> prohibition to all licensed Thai digital-asset business operators (cryptocurrency and
> digital-token exchanges, brokers, dealers, fund managers and advisors), barring them
> from providing services that support the use of digital assets as a means of payment
> for goods or services. The notification does not name specific operators, addresses,
> or domains; enumeration=subset because the prohibition addresses a licensed-operator
> class without a fixed enumerated roster, matching the China 2013 / Nigeria 2021
> payment-rail-severance convention.

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `direct` · Δt = 0h

**Event label**: `crypto_as_means_of_payment_services_prohibited_class_wide`

**Timestamp**: `2022-04-01 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_government`**
  - URL: <https://web.archive.org/web/20220716015641/https://www.sec.or.th/EN/Pages/News_Detail.aspx?SECID=9366>
  - Wayback: <https://web.archive.org/web/20220716015641/https://www.sec.or.th/EN/Pages/News_Detail.aspx?SECID=9366>
  - body_hash: `sha256:11a67a6d0eafe3d93ddcda40594af9082fb4e8c3892bffa2cf9bdd7bef454da3`
  - body_path: `sources/http_captures/thailand-sec-crypto-payment-ban-2022-04/primary/web.archive.org__web-20220716015641-https-www.sec.or.th-EN-Pages-News_Detail.aspx__b7b092d9f9.html`
  > SEC Thailand press release (No. 39/2022, 23 March 2022): the SEC issued
> regulation requiring digital-asset business operators "to avert support or
> promotion of the use of digital assets as a means of payment for goods and
> services", effective 1 April 2022 with a 30-day compliance window.
> attribution=direct because the SEC press release is the regulatory mandate
> and names the licensed-operator payment-service prohibition.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`thailand-sec-binance-bybit-c-and-d-2021`](./thailand-sec-binance-bybit-c-and-d-2021.md)
- [`thailand-bot-bitcoin-prohibition-2013`](./thailand-bot-bitcoin-prohibition-2013.md)
- [`nigeria-cbn-crypto-ban-2021`](./nigeria-cbn-crypto-ban-2021.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `97f58fa`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

