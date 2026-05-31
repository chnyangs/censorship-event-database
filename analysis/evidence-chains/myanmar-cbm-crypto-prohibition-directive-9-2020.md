# Evidence chain — `myanmar-cbm-crypto-prohibition-directive-9-2020`

**Status**: `admitted` · **Stratum**: `S4_nation_state` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `cc05a9c` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-31` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "On 2020-05-15 the Central Bank of Myanmar issued Notification No. 9/2020
> prohibiting all persons residing in Myanmar from the sale, purchase, or
> exchange of unregulated digital currencies (Bitcoin, Litecoin, Ethereum,
> Perfect Money), with enforcement via account closure and legal action under
> the AML Law and Financial Institutions Law. The offramp_cex layer carries the
> load-bearing plausible-attribution observation at class level."

## 1. Trigger

- **Type**: `nation_state_block`
- **Actor**: `MM_CBM`
- **Timestamp**: `2020-05-15 00:00:00+00:00` (precision: `day`)

### Trigger citations

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
> Law-firm secondary analysis reproducing the directive; the CBM's own
> Notification No. 9/2020 instrument text was not located on a stable
> English-language web page in this draft pass.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Myanmar crypto users / exchanges / financial institutions (class)

> All persons residing in Myanmar and financial institutions barred from the
> sale, purchase, or exchange of unregulated digital currencies (Bitcoin,
> Litecoin, Ethereum, Perfect Money named as a non-exhaustive list). No
> specific exchange or platform enumerated; class-level prohibition matching
> the sibling nation-state-prohibition convention (Cambodia 2018, Nepal 2017).

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `plausible` · Δt = 0h

**Event label**: `crypto_sale_purchase_exchange_prohibited_directive_9_2020`

**Timestamp**: `2020-05-15 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`supporting_journalism`**
  - URL: <https://web.archive.org/web/20260120112720/https://www.tilleke.com/insights/myanmars-central-bank-issues-further-warning-against-crypto-trading/>
  - Wayback: <https://web.archive.org/web/20260120112720/https://www.tilleke.com/insights/myanmars-central-bank-issues-further-warning-against-crypto-trading/>
  - body_hash: `sha256:0cd2cf34c9e091564c0875bfbf30099d5b3dda95acdd2a35738889da5bae2e48`
  - body_path: `sources/http_captures/myanmar-cbm-crypto-prohibition-directive-9-2020/primary/web.archive.org__web-20260120112720-https-www.tilleke.com-insights-myanmars-central-bank-issues-further-warning-against-crypto-trading__53bb7afc72.html`
  > attribution=plausible per codebook §1: the action is causally
> consistent with the named CBM Notification No. 9/2020, but the
> load-bearing captured evidence is law-firm secondary analysis (Tilleke
> & Gibbins) reproducing the directive rather than the CBM instrument
> text, and the prohibition is class-level (names no specific exchange).
> A primary CBM Notification No. 9/2020 capture would be required to
> elevate to direct.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`cambodia-nbc-joint-crypto-prohibition-2018-05`](./cambodia-nbc-joint-crypto-prohibition-2018-05.md)
- [`nepal-nrb-bitcoin-ban-2017-08`](./nepal-nrb-bitcoin-ban-2017-08.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `cc05a9c`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

