# Evidence chain — `india-fiu-offshore-vda-block-2023`

**Status**: `admitted` · **Stratum**: `S4_nation_state` · **Shape**: `comparison` (1 changed layer(s): `l0_network`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-05` · **Source commit**: `5fba5c6` · **Schema**: `0.2.0` · **Event last_verified**: `2026-06-01` · **Tool version**: `0.1.0` · **Generated**: `2026-06-05T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "FIU-IND's 2023-12-28 press release issued show-cause notices to nine
> offshore VDA service providers and stated that FIU-IND wrote to MEITY to
> block those entities' URLs. In OONI IN web_connectivity measurements over
> 2024-01-12 to 2024-02-15, https://www.binance.com/ showed confirmed
> DNS-blocking fingerprints on sampled Indian AS55836 measurements on
> 2024-02-11 and 2024-02-13. This row claims only that sampled
> India-vantage L0 subset; it does not claim nationwide blocking across all
> FIU-IND named domains, app-store removals, or INR rail severance."

## 1. Trigger

- **Type**: `nation_state_block`
- **Actor**: `IN_FIU`
- **Timestamp**: `2023-12-28 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://www.pib.gov.in/Pressreleaseshare.aspx?PRID=1991372&reg=3&lang=2>
  - body_hash: `sha256:d9d8feef882663606925889fb566c76b8a271d007809c52607fcc748baa1df3a`
  - body_path: `sources/http_captures/india-fiu-offshore-vda-block-2023/primary/www.pib.gov.in__Pressreleaseshare.aspx__fbb11e0f0b.html`
  > FIU-IND (Financial Intelligence Unit, India) press release dated
> 2023-12-28 announcing compliance show-cause notices issued to nine
> offshore Virtual Digital Asset (VDA) service providers — Binance,
> KuCoin, Huobi, Kraken, Gate.io, Bittrex, Bitstamp, MEXC Global, and
> Bitfinex — for operating in India without registration as Reporting
> Entities under the Prevention of Money Laundering Act (PMLA). The
> release also states that FIU-IND wrote to the Secretary, Ministry of
> Electronics and Information Technology (MEITY), to block the URLs of
> those entities. Captured with a browser user agent because the live
> endpoint returned HTTP 403 to the default capture agent.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Offshore VDA exchanges (FIU-IND show-cause class, IN-vantage access)
- **Canonical domains**: `binance.com`, `kraken.com`, `kucoin.com`, `huobi.com`, `bitstamp.net`, `mexc.com`, `bittrex.com`, `gate.io`, `bitfinex.com`

> Nine named offshore Virtual Digital Asset (VDA) service providers as
> enumerated in the FIU-IND press release: Binance, KuCoin, Huobi,
> Kraken, Gate.io, Bittrex, Bitstamp, MEXC Global, and Bitfinex.
> This repaired parent row measures only a `binance.com` L0 subset from
> Indian OONI probes; Apple App Store and Google Play removals are carried
> by sibling S5 rows rather than duplicated here. OKX appears in app-store
> sibling reporting but is not in the FIU-IND named-nine trigger list.

## 3. Changed-layer observations (supports the scoped claim)

### l0_network · attribution: `plausible` · Δt = 1089h

**Event label**: `in_vantage_dns_blocking_of_binance_domain`

**Timestamp**: `?` (precision: `second`)

**Sources**:

- **`semi_primary_measurement`**
  - URL: <https://api.ooni.io/api/v1/measurements?probe_cc=IN&test_name=web_connectivity&input=https%3A%2F%2Fwww.binance.com%2F&since=2024-01-12&until=2024-02-15&limit=20>
  - body_hash: `sha256:f4a98fc7a093f25a27e9ab6ade83f39a512330077977ea1b7216ca8fe3bdead5`
  - body_path: `sources/http_captures/india-fiu-offshore-vda-block-2023/ooni/api.ooni.io__api-v1-measurements__d2e076e2fe.json`
  > OONI IN web_connectivity query for https://www.binance.com/
> returns confirmed DNS-blocking rows on AS55836 on 2024-02-11
> and 2024-02-13. The query also includes non-anomalous Indian
> rows on other ASNs, so attribution is plausible and coverage is
> partially_measured rather than a universal India blocking claim.
- **`semi_primary_measurement`**
  - URL: <https://api.ooni.io/api/v1/raw_measurement?measurement_uid=20240213092932.061005_IN_webconnectivity_ecdb2dfb8255e767>
  - body_hash: `sha256:658ab21577b5bb8a41140b49ec9d41601418111269896ae510d7e87c5cff02a9`
  - body_path: `sources/http_captures/india-fiu-offshore-vda-block-2023/ooni/api.ooni.io__api-v1-raw_measurement__85fae4fd13.json`
  > Raw OONI measurement body for AS55836. The measurement records
> `blocking=dns`, `accessible=false`, and
> `dns_consistency=inconsistent` for https://www.binance.com/.
- **`semi_primary_measurement`**
  - URL: <https://api.ooni.io/api/v1/raw_measurement?measurement_uid=20240211085150.499106_IN_webconnectivity_0048f0197fac6b4c>
  - body_hash: `sha256:e96be7aa234e9e0f0df730da967a2c6932e07eeb2872421cae426c0263d93918`
  - body_path: `sources/http_captures/india-fiu-offshore-vda-block-2023/ooni/api.ooni.io__api-v1-raw_measurement__765f8b495e.json`
  > Raw OONI measurement body for AS55836. The measurement records
> `blocking=dns`, `accessible=false`, and
> `dns_consistency=inconsistent` for https://www.binance.com/.

## 5. Honest coverage gaps

- **offramp_cex** (`not_measured`): No retained parent-row claim about INR rail severance. Any future

## 7. Related events

- [`india-rbi-crypto-ban-2018`](./india-rbi-crypto-ban-2018.md)
- [`philippines-sec-binance-block-2024`](./philippines-sec-binance-block-2024.md)
- [`turkey-cbrt-crypto-ban-2021`](./turkey-cbrt-crypto-ban-2021.md)
- [`korea-travel-rule-2022`](./korea-travel-rule-2022.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `5fba5c6`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

