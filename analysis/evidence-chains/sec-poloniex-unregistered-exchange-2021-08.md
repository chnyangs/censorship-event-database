# Evidence chain — `sec-poloniex-unregistered-exchange-2021-08`

**Status**: `admitted` · **Stratum**: `S3_doj_sec_cftc_fiod` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-05-31` · **Source commit**: `a331305` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-31` · **Tool version**: `0.1.0` · **Generated**: `2026-05-31T04:56:33Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "The 2021-08-09 settled SEC order against Poloniex LLC (unregistered
> digital asset securities exchange, July 2017 - November 2019; ~$10.4M
> disgorgement + interest + penalty + cease-and-desist) is recorded as a
> single-layer offramp_cex named-operator restriction, attribution=
> direct. The row does not claim ISP-level blocking, a frontend takedown,
> an on-chain freeze, a US-market exit, or specific token delistings
> (none of which are stated in the captured SEC order)."

## 1. Trigger

- **Type**: `sec_action`
- **Actor**: `US_SEC`
- **Timestamp**: `2021-08-09 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://www.sec.gov/news/press-release/2021-147>
  - Wayback: <https://web.archive.org/web/20210809221853/https://www.sec.gov/news/press-release/2021-147>
  - body_hash: `sha256:7a8609e539db3f398d98d4b8c592604766f8fcbb4902355928659020edc57cde`
  - body_path: `sources/http_captures/sec-poloniex-unregistered-exchange-2021-08/primary/web.archive.org__web-20210810000000-https-www.sec.gov-news-press-release-2021-147__07b5f92445.html`
  > SEC press release 2021-147 (2021-08-09): "SEC Charges Poloniex for
> Operating Unregistered Digital Asset Exchange." The SEC announced
> that Poloniex LLC agreed to pay more than $10 million to settle
> charges for operating an unregistered online digital asset
> exchange. The SEC's order finds that from July 2017 through
> November 2019 (when Poloniex sold its platform), Poloniex operated
> a web-based trading platform that facilitated buying and selling
> of digital assets including digital assets that were investment
> contracts and therefore securities, meeting the definition of an
> "exchange" under the securities laws while not registering as a
> national securities exchange or operating under an exemption.
> Poloniex agreed to disgorgement of ~$8.5M, prejudgment interest
> of ~$400K, and a $1.5M civil penalty (~$10.4M total). Wayback
> 20210809221853 pinned (same-day capture). Verified facts present
> in captured HTML: title, "Poloniex" (x19), "Unregistered Digital
> Asset Exchange", "Aug. 9, 2021", "July 2017 through November 2019",
> "sold its platform", "disgorgement", "civil penalty", "$1.5
> million".

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `complete`
- **Actor name**: Poloniex LLC
- **Canonical domains**: `poloniex.com`

> Poloniex LLC (operator of the Poloniex web-based digital asset trading
> platform; respondent in the settled SEC administrative order announced
> 2021-08-09). Subject-matter scope: the Poloniex trading platform's
> operation as an unregistered national securities exchange from July
> 2017 through November 2019 (when the platform was sold). enumeration=
> complete: the row enumerates the single named exchange operator entity
> and the platform's unregistered-exchange operation. No on-chain
> addresses are enumerated: the remedy is a settled monetary order and
> cease-and-desist against the operator, not an on-chain action.

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `direct` · Δt = 0h

**Event label**: `sec_settled_order_charges_poloniex_unregistered_securities_exchange_104m`

**Timestamp**: `2021-08-09 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_legal`**
  - URL: <https://www.sec.gov/news/press-release/2021-147>
  - Wayback: <https://web.archive.org/web/20210809221853/https://www.sec.gov/news/press-release/2021-147>
  - body_hash: `sha256:7a8609e539db3f398d98d4b8c592604766f8fcbb4902355928659020edc57cde`
  - body_path: `sources/http_captures/sec-poloniex-unregistered-exchange-2021-08/primary/web.archive.org__web-20210810000000-https-www.sec.gov-news-press-release-2021-147__07b5f92445.html`
  > SEC press release 2021-147 (2021-08-09): settled administrative
> order finding Poloniex LLC operated an unregistered digital asset
> securities exchange (July 2017 - November 2019), with ~$8.5M
> disgorgement, ~$400K prejudgment interest, and a $1.5M civil
> penalty (~$10.4M total) plus cease-and-desist. attribution=
> direct: the SEC order names the operator and restricts the
> unregistered-exchange operation directly. Facts verified present
> in captured HTML ("Poloniex", "Unregistered Digital Asset
> Exchange", "sold its platform", "$1.5 million", "disgorgement").

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`sec-v-bittrex-2023`](./sec-v-bittrex-2023.md)
- [`sec-beaxy-platform-shutdown-2023`](./sec-beaxy-platform-shutdown-2023.md)
- [`kraken-sec-unregistered-exchange-2023`](./kraken-sec-unregistered-exchange-2023.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `a331305`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

