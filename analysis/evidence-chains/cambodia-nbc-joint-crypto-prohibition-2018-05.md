# Evidence chain — `cambodia-nbc-joint-crypto-prohibition-2018-05`

**Status**: `admitted` · **Stratum**: `S4_nation_state` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `c3fb0ae` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-31` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "On 2018-05-11 the NBC, SECC and General-Commissariat of National Police
> issued a joint statement declaring the propagation, circulation, buying,
> selling, trading and settlement of cryptocurrencies illegal without a license
> from competent Cambodian authorities; with no licensing pathway opened, this
> operated as a de facto national prohibition on the Cambodian crypto
> exchange/trading surface. The offramp_cex layer carries the load-bearing
> plausible-attribution observation at class level."

## 1. Trigger

- **Type**: `nation_state_block`
- **Actor**: `KH_NBC`
- **Timestamp**: `2018-05-11 00:00:00+00:00` (precision: `day`)

### Trigger citations

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
> authorities is illegal. Because no licensing pathway was opened, the
> statement operated as a de facto prohibition on Cambodian crypto
> exchanges/trading. Contemporaneous reporting captured via Wayback memento
> 2018-06-20; the NBC/SECC joint statement itself was not published on a
> stable English-language web page.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Cambodian crypto exchanges / traders (class)

> Cambodian crypto users, exchanges and ICO/token operators as a class. The
> joint statement does not enumerate specific platforms; it prohibits the
> propagation, circulation, buying, selling, trading and settlement of
> cryptocurrencies without a license. Target treated as entity-class-level,
> matching the sibling nation-state prohibition convention (India 2018,
> Zimbabwe 2018).

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `plausible` · Δt = 0h

**Event label**: `crypto_trading_and_settlement_declared_illegal_without_license`

**Timestamp**: `2018-05-11 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`supporting_journalism`**
  - URL: <https://web.archive.org/web/20180620031123/https://www.phnompenhpost.com/business/cryptos-illegal-kingdom-regulators>
  - Wayback: <https://web.archive.org/web/20180620031123/https://www.phnompenhpost.com/business/cryptos-illegal-kingdom-regulators>
  - body_hash: `sha256:c8acdc033a4946eef66dde5c4d2ae7858c2aec180a64696a3ba09b74ac99edb6`
  - body_path: `sources/http_captures/cambodia-nbc-joint-crypto-prohibition-2018-05/primary/web.archive.org__web-20180620031123-https-www.phnompenhpost.com-business-cryptos-illegal-kingdom-regulators__3512288dd1.html`
  > attribution=plausible per codebook §1: the action is causally
> consistent with the named NBC/SECC/National Police joint statement, but
> the load-bearing captured evidence is contemporaneous journalism
> reproducing the statement rather than the official instrument text, and
> the statement is class-level (names no specific exchange). A primary
> NBC/SECC instrument capture would be required to elevate to direct.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`india-rbi-crypto-ban-2018`](./india-rbi-crypto-ban-2018.md)
- [`zimbabwe-rbz-circular-2-2018-golix-ban`](./zimbabwe-rbz-circular-2-2018-golix-ban.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `c3fb0ae`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

