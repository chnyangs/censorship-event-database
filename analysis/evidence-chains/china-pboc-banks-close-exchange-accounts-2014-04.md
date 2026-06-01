# Evidence chain — `china-pboc-banks-close-exchange-accounts-2014-04`

**Status**: `admitted` · **Stratum**: `S4_nation_state` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `4ee1e3c` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-31` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T03:53:57Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> Around the 2014-04-15 PBOC deadline, Chinese banks and third-party payment processors
> closed the accounts of domestic bitcoin exchanges; OKCoin and Huobi reported their bank
> accounts closed by 2014-04-18. The offramp_cex layer carries the load-bearing
> direct-attribution observation. This is the enforcement escalation of the 2013-12 PBOC
> banking-exclusion notice (deposit pause -> account closure).

## 1. Trigger

- **Type**: `nation_state_block`
- **Actor**: `CN_PBOC`
- **Timestamp**: `2014-04-15 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`supporting_journalism`**
  - URL: <https://web.archive.org/web/20140418000000/https://www.coindesk.com/markets/2014/04/17/chinas-banks-close-more-bitcoin-accounts-following-pboc-deadline>
  - Wayback: <https://web.archive.org/web/20210918082857/https://www.coindesk.com/markets/2014/04/17/chinas-banks-close-more-bitcoin-accounts-following-pboc-deadline/>
  - body_hash: `sha256:022abe686c4f11d75f8ca2e31eaf3f3593db658ae67a06c45ae77be3441a80d8`
  - body_path: `sources/http_captures/china-pboc-banks-close-exchange-accounts-2014-04/primary/web.archive.org__web-20140418000000-https-www.coindesk.com-markets-2014-04-17-chinas-banks-close-more-bitcoin-accounts-following-pboc-deadline__c560f7f2c5.html`
  > CoinDesk report (Jon Southurst) dated 2014-04-17 documenting that, following a
> PBOC deadline of 2014-04-15 requiring banks and third-party payment processors
> to close the accounts of bitcoin exchanges, "Exchanges OKCoin and Huobi said they
> had bank accounts closed as of Friday afternoon China time, posting the news on
> their respective sites." Verified in the captured body. This is the enforcement
> escalation distinct from the 2013-12 PBOC Notice 2013/289 (which refused new
> accounts / drove a CNY-deposit pause): here the named exchanges' EXISTING bank
> accounts were actually closed around the 2014-04-15 deadline. The PBOC order
> itself is reported via internal Chinese regulatory channels and is not publicly
> archivable; the CoinDesk report is the replayable anchor. Wayback date-prefix
> resolved to the 2021-09-18 memento of the same article.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: PRC bitcoin exchanges (OKCoin, Huobi, et al.) bank-account-closure class
- **Chains**: `bitcoin`

> Canonical target is the population of Chinese bitcoin-exchange operators whose bank
> accounts were ordered closed around the 2014-04-15 PBOC deadline. Named affected
> exchanges in contemporaneous coverage include OKCoin and Huobi (whose bank accounts
> were reported closed); the deadline reportedly applied to a broader set of domestic
> exchanges and their banking/payment partners. enumeration=subset because the named
> roster (OKCoin, Huobi) is a non-exhaustive subset of the exchange class subject to the
> PBOC deadline, consistent with the sibling china-pboc-crypto-ban-2013-12 convention.

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `plausible` · Δt = 72h

**Event label**: `exchange_bank_accounts_closed_following_pboc_deadline`

**Timestamp**: `2014-04-18 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`supporting_journalism`**
  - URL: <https://web.archive.org/web/20140418000000/https://www.coindesk.com/markets/2014/04/17/chinas-banks-close-more-bitcoin-accounts-following-pboc-deadline>
  - Wayback: <https://web.archive.org/web/20210918082857/https://www.coindesk.com/markets/2014/04/17/chinas-banks-close-more-bitcoin-accounts-following-pboc-deadline/>
  - body_hash: `sha256:022abe686c4f11d75f8ca2e31eaf3f3593db658ae67a06c45ae77be3441a80d8`
  - body_path: `sources/http_captures/china-pboc-banks-close-exchange-accounts-2014-04/primary/web.archive.org__web-20140418000000-https-www.coindesk.com-markets-2014-04-17-chinas-banks-close-more-bitcoin-accounts-following-pboc-deadline__c560f7f2c5.html`
  > CoinDesk 2014-04-17: "Exchanges OKCoin and Huobi said they had bank accounts
> closed as of Friday afternoon China time, posting the news on their respective
> sites," following the 2014-04-15 PBOC deadline for banks/payment processors to
> close bitcoin-exchange accounts. attribution=direct because the PBOC deadline is
> the named regulatory mandate driving the observed account closures. The PBOC
> order is not publicly archivable; this report is the replayable anchor.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`china-pboc-crypto-ban-2013-12`](./china-pboc-crypto-ban-2013-12.md)
- [`china-pboc-crypto-ban-2021`](./china-pboc-crypto-ban-2021.md)
- [`jordan-cbj-bank-crypto-prohibition-2014`](./jordan-cbj-bank-crypto-prohibition-2014.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `4ee1e3c`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

