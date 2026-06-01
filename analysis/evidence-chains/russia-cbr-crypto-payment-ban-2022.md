# Evidence chain — `russia-cbr-crypto-payment-ban-2022`

**Status**: `admitted` · **Stratum**: `S4_nation_state` · **Shape**: `null_event` (0 changed layer(s): none) · **Tier**: `null_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `97f1e7e` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-21` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T10:19:59Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> *(no scoped_claim recorded — event not paper-ready)*

## 1. Trigger

- **Type**: `regulatory_enforcement`
- **Actor**: `RU_CENTRAL_BANK`
- **Timestamp**: `2022-01-20 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://www.cbr.ru/eng/press/event/?id=12627>
  - Wayback: <https://web.archive.org/web/20220121022021/https://www.cbr.ru/eng/press/event/?id=12627>
  - body_hash: `sha256:7e96fa79328d46d820d9c72b7eb5a81113f5d3b8328b1da3808408f56a398b31`
  - body_path: `sources/http_captures/russia-cbr-crypto-payment-ban-2022/primary/web.archive.org__web-20220121022021-https-www.cbr.ru-eng-press-event__d0318360b2.html`
  > Bank of Russia (Central Bank of the Russian Federation / CBR)
> consultation paper "Cryptocurrencies: trends, risks, measures"
> ("Криптовалюты: тренды, риски, меры") published 2022-01-20 by
> the CBR Financial Stability Department under director
> Elizaveta Danilova. The paper proposed a comprehensive ban
> on cryptocurrency issuance and circulation inside Russia,
> including dedicated crypto exchanges, peer-to-peer (P2P)
> platforms, and other financial organizations issuing or
> circulating cryptocurrencies; a ban on crypto mining citing
> electricity-grid and energy-policy concerns; and a prohibition
> on the use of cryptocurrencies as a means of payment. The
> consultation window invited comments until 2022-03-01. The
> proposal was NOT adopted as Russian law in the form proposed:
> the Ministry of Finance (Minfin) published a competing
> regulation-rather-than-ban concept in early February 2022,
> and the subsequent Russian regulatory framework (Federal Law
> On Digital Financial Assets 259-FZ already in force since
> 2021-01-01, plus the 2024 mining law) partially restricts
> crypto payments without enacting the full CBR ban. Wayback
> anchor is provisional; specific snapshot timestamp requires
> human-audit re-pinning.
- **`supporting_journalism`**
  - URL: <https://www.aljazeera.com/economy/2022/1/20/russias-central-bank-proposes-ban-on-crypto-mining-and-trading>
  - Wayback: <https://web.archive.org/web/2022/https://www.aljazeera.com/economy/2022/1/20/russias-central-bank-proposes-ban-on-crypto-mining-and-trading>
  > Al Jazeera English same-day coverage (2022-01-20) of the
> Bank of Russia consultation paper. Reports the CBR proposal
> to ban crypto mining, trading, and use within Russia and
> names Elizaveta Danilova as the Financial Stability
> Department director presenting the report. Used here as a
> contextual journalism anchor. Specific Wayback snapshot
> timestamp requires re-pinning during human audit.
- **`semi_primary_wayback`**
  - URL: <https://www.coindesk.com/policy/2022/01/20/bank-of-russia-calls-for-full-ban-on-crypto/>
  - Wayback: <https://web.archive.org/web/20220120125334/https://www.coindesk.com/policy/2022/01/20/bank-of-russia-calls-for-full-ban-on-crypto/>
  - body_hash: `sha256:d9efb21a618fea2641124ffe7a2b08cfdc98b11a21e52e233bdf033380dc8511`
  - body_path: `sources/http_captures/russia-cbr-crypto-payment-ban-2022/primary/web.archive.org__web-20220120125334-https-www.coindesk.com-policy-2022-01-20-bank-of-russia-calls-for-full-ban-on-crypto__ba6358ebd5.html`
  > CoinDesk 2022-01-20 same-day coverage of the Bank of Russia
> consultation paper "Cryptocurrencies: trends, risks,
> measures". Reports the full-ban proposal scope (mining,
> trading, payments) and the public-comment window through
> 2022-03-01. Contextual journalism anchor; Wayback snapshot
> pinning required at human audit.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Russia-resident crypto activity (CBR proposal class)
- **Chains**: `bitcoin`, `ethereum`

> Canonical target is the proposed regulatory class of
> cryptocurrency activity within Russia: cryptocurrency mining,
> crypto-exchange/P2P-platform issuance and circulation, and the
> use of cryptocurrencies as a means of payment by Russian
> residents and Russian legal entities. The consultation paper
> does not enumerate specific exchanges, addresses, or domains
> as targets; it is a class-level regulatory proposal.
> enumeration=subset rather than complete because the proposal
> addresses an activity class without a fixed roster of named
> entities.

## 3. Changed-layer observations (supports the scoped claim)

*No observed_change entries. This is a `null_event`; see §4 for observed_no_change evidence supporting the null claim.*

## 4. No-change observations (where applicable)

### offramp_cex — `cbr_consultation_paper_proposed_but_not_enacted`

**Window**: `2022-01-20 00:00:00+00:00` → `2022-12-31 23:59:59+00:00`

**Sources**:

- **`primary_legal`**
  - URL: <https://www.cbr.ru/eng/press/event/?id=12627>
  - Wayback: <https://web.archive.org/web/20220121022021/https://www.cbr.ru/eng/press/event/?id=12627>
  - body_hash: `sha256:7e96fa79328d46d820d9c72b7eb5a81113f5d3b8328b1da3808408f56a398b31`
  - body_path: `sources/http_captures/russia-cbr-crypto-payment-ban-2022/primary/web.archive.org__web-20220121022021-https-www.cbr.ru-eng-press-event__d0318360b2.html`
  > CBR English-language press event page for the 2022-01-20
> consultation paper "Cryptocurrency risks and possible
> regulation measures". Provisional Wayback anchor; specific
> snapshot timestamp to be re-pinned at human audit.
- **`semi_primary_wayback`**
  - URL: <https://www.coindesk.com/policy/2022/01/20/bank-of-russia-calls-for-full-ban-on-crypto/>
  - Wayback: <https://web.archive.org/web/20220120125334/https://www.coindesk.com/policy/2022/01/20/bank-of-russia-calls-for-full-ban-on-crypto/>
  - body_hash: `sha256:d9efb21a618fea2641124ffe7a2b08cfdc98b11a21e52e233bdf033380dc8511`
  - body_path: `sources/http_captures/russia-cbr-crypto-payment-ban-2022/primary/web.archive.org__web-20220120125334-https-www.coindesk.com-policy-2022-01-20-bank-of-russia-calls-for-full-ban-on-crypto__ba6358ebd5.html`
  > CoinDesk 2022-01-20 coverage corroborating the full-ban
> scope and consultation-window framing. Contextual
> journalism anchor; Wayback re-pin required at human audit.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`russia-cbr-bitcoin-information-letter-2014`](./russia-cbr-bitcoin-information-letter-2014.md)
- [`russia-mining-regional-ban-2024-12`](./russia-mining-regional-ban-2024-12.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `97f1e7e`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

