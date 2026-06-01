# Evidence chain — `russia-cbr-bitcoin-information-letter-2014`

**Status**: `admitted` · **Stratum**: `S4_nation_state` · **Shape**: `null_event` (0 changed layer(s): none) · **Tier**: `null_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `ff0c8be` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-21` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T11:07:46Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> *(no scoped_claim recorded — event not paper-ready)*

## 1. Trigger

- **Type**: `nation_state_block`
- **Actor**: `RU_CBR`
- **Timestamp**: `2014-01-27 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <http://www.cbr.ru/press/pr/?file=27012014_1825052.htm>
  - Wayback: <https://web.archive.org/web/20170724031011/http://www.cbr.ru/press/pr/?file=27012014_1825052.htm>
  - body_hash: `sha256:6852dfb3f49bb0b1422791e0f08a5d9a7968c2263d31bd28cc75e958d4e876d9`
  - body_path: `sources/http_captures/russia-cbr-bitcoin-information-letter-2014/primary/web.archive.org__web-20170724031011-http-www.cbr.ru-press-pr__f1d7be4e36.html`
  > Central Bank of the Russian Federation (Bank of Russia / CBR)
> information letter dated 2014-01-27 titled "Об использовании при
> совершении сделок «виртуальных валют», в частности, Биткойн"
> ("On Using Virtual Currencies, Specifically Bitcoin, in
> Transactions"). The Bank of Russia warned Russian citizens and
> legal entities (in particular credit and non-credit financial
> organizations) against using virtual currencies for exchange
> into goods, services, or monetary funds in rubles and foreign
> currency. The letter framed virtual-currency exchange activities
> by Russian business entities as "dubious activity" potentially
> constituting involvement in money-laundering and
> terrorism-financing under Russian AML/CFT law, and invoked
> Article 27 of the Federal Law "On the Central Bank of the
> Russian Federation" which prohibits the issuance of monetary
> surrogates in Russia. This was an information letter / advisory
> — not a formal prohibition on residents holding bitcoin — but
> signaled the regulatory disposition that anticipates the later
> CBR-led 2017+ enforcement posture and the 2022 CBR full
> crypto-payments ban. Russian-language original on cbr.ru.
> Wayback wildcard anchor is provisional; specific snapshot
> timestamp must be re-pinned during human audit before this
> citation may carry an admission anchor in its own right. Marked
> evidence_use=contextual_unarchived pending that re-pin.
- **`semi_primary_wayback`**
  - URL: <https://www.loc.gov/item/global-legal-monitor/2014-02-06/russia-bitcoin-exchanges-can-be-penalized/>
  - Wayback: <https://web.archive.org/web/20220808091552/https://www.loc.gov/item/global-legal-monitor/2014-02-06/russia-bitcoin-exchanges-can-be-penalized/>
  - body_hash: `sha256:b78c857b4fd427708b82a0f8f2e1c602b088361d0e2847b56a08b88d4f50f7ef`
  - body_path: `sources/http_captures/russia-cbr-bitcoin-information-letter-2014/primary/web.archive.org__web-20220808091552-https-www.loc.gov-item-global-legal-monitor-2014-02-06-russia-bitcoin-exchanges-can-be-penalized__cd849026c0.html`
  > US Library of Congress Global Legal Monitor entry dated
> 2014-02-06 titled "Russia: Bitcoin Exchanges Can Be Penalized",
> providing English-language summary of the 2014-01-27 Bank of
> Russia information letter and naming Article 27 of the CBR Law
> as the cited legal basis. Used here as a contextual translation
> anchor; specific Wayback snapshot timestamp to be re-pinned
> during human audit. Marked evidence_use=contextual_unarchived.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Russia-resident bitcoin users (CBR advisory class)
- **Chains**: `bitcoin`

> Canonical target is the CBR advisory directed at Russia-resident
> bitcoin users and Russian legal entities (in particular credit
> and non-credit financial organizations). This is a class-level
> advisory, not an enumerated entity list: the letter does not
> name specific exchanges or individual addresses. No Russian
> crypto-exchange ecosystem of the scale of the contemporaneous
> PRC triad (BTC China, OKCoin, Huobi) existed at the time, and
> the advisory's binding force on residents was indirect (an
> AML/CFT-violation warning rather than a banking-rail severance
> directive). Enumeration=subset rather than complete because the
> advisory addresses a population class without a fixed roster.

## 3. Changed-layer observations (supports the scoped claim)

*No observed_change entries. This is a `null_event`; see §4 for observed_no_change evidence supporting the null claim.*

## 4. No-change observations (where applicable)

### offramp_cex — `cbr_aml_cft_advisory_dispersed_cascade`

**Window**: `2014-01-27 00:00:00+00:00` → `2014-12-31 23:59:59+00:00`

**Sources**:

- **`primary_legal`**
  - URL: <http://www.cbr.ru/press/pr/?file=27012014_1825052.htm>
  - Wayback: <https://web.archive.org/web/20170724031011/http://www.cbr.ru/press/pr/?file=27012014_1825052.htm>
  - body_hash: `sha256:6852dfb3f49bb0b1422791e0f08a5d9a7968c2263d31bd28cc75e958d4e876d9`
  - body_path: `sources/http_captures/russia-cbr-bitcoin-information-letter-2014/primary/web.archive.org__web-20170724031011-http-www.cbr.ru-press-pr__f1d7be4e36.html`
  > CBR 2014-01-27 information letter is the legal instrument.
> The letter explicitly warns Russian citizens and legal
> entities (in particular credit and non-credit financial
> organizations) against virtual-currency exchange activity
> and frames such activity by Russian businesses as
> potentially constituting AML/CFT violations. Provisional
> wayback anchor; specific snapshot timestamp requires
> human-audit re-pinning.
- **`semi_primary_wayback`**
  - URL: <https://www.loc.gov/item/global-legal-monitor/2014-02-06/russia-bitcoin-exchanges-can-be-penalized/>
  - Wayback: <https://web.archive.org/web/20220808091552/https://www.loc.gov/item/global-legal-monitor/2014-02-06/russia-bitcoin-exchanges-can-be-penalized/>
  - body_hash: `sha256:b78c857b4fd427708b82a0f8f2e1c602b088361d0e2847b56a08b88d4f50f7ef`
  - body_path: `sources/http_captures/russia-cbr-bitcoin-information-letter-2014/primary/web.archive.org__web-20220808091552-https-www.loc.gov-item-global-legal-monitor-2014-02-06-russia-bitcoin-exchanges-can-be-penalized__cd849026c0.html`
  > Library of Congress Global Legal Monitor 2014-02-06 English
> summary of the CBR 2014-01-27 letter, corroborating the
> advisory's scope and the cited Article 27 of the CBR Law.
> Specific Wayback snapshot timestamp requires re-pinning in
> human audit.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`russia-cbr-crypto-payment-ban-2022`](./russia-cbr-crypto-payment-ban-2022.md)
- [`china-pboc-crypto-ban-2013-12`](./china-pboc-crypto-ban-2013-12.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `ff0c8be`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

