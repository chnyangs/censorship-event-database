# Evidence chain — `thailand-bot-bitcoin-prohibition-2013`

**Status**: `admitted` · **Stratum**: `S4_nation_state` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `1c9c65c` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-21` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T12:19:10Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> On 2013-07-29 the Bank of Thailand Foreign Exchange Administration and
> Policy Department issued a verbal administrative advisement to Bitcoin
> Co. Ltd that bitcoin trading was illegal under Thai law given the
> Exchange Control Act B.E. 2485 framework; Bitcoin Co. Ltd suspended
> operations the same day and resumed approximately 6.5 months later
> (2014-02-15) following a BOT clarification letter. The offramp_cex
> layer carries the single direct-attribution observed_change row;
> L0/L1/L3/asset_onchain are not_applicable on construct or scope
> grounds and L4 frontend is not_measured pending Wayback capture.

## 1. Trigger

- **Type**: `regulatory_enforcement`
- **Actor**: `TH_BOT`
- **Timestamp**: `2013-07-29 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_corporate`**
  - URL: <https://bitcoin.co.th/trading-suspended-due-to-bank-of-thailand-advisement/>
  - Wayback: <https://web.archive.org/web/20140212082550/https://bitcoin.co.th/trading-suspended-due-to-bank-of-thailand-advisement/>
  - body_hash: `sha256:b46d45646e9277ed4f8fe35c60c07463533d93e8da63edc85ffbbc289c16ddef`
  - body_path: `sources/http_captures/thailand-bot-bitcoin-prohibition-2013/v0_3_primary_repair/web.archive.org__web-2013-https-bitcoin.co.th-trading-suspended-due-to-bank-of-thailand-advisement__cb8eeb9d82.html`
  > Bitcoin Co. Ltd's original corporate statement, "Trading
> suspended due to Bank of Thailand advisement", captured from
> Wayback at 2014-02-12 while the 2013-07-29 suspension was still
> in force. The archived page states the operator's reason for
> suspending services and quotes the BOT Foreign Exchange
> Administration and Policy Department advisement. v0.3 repair
> note: the current live URL returned 404, so the replayable
> anchor is the timestamped Wayback body_hash/body_path.
- **`supporting_journalism`**
  - URL: <https://www.coindesk.com/markets/2013/07/29/bank-of-thailand-allegedly-declares-bitcoin-illegal-thai-exchange-suspends-trading>
  - Wayback: <https://web.archive.org/web/2013/https://www.coindesk.com/markets/2013/07/29/bank-of-thailand-allegedly-declares-bitcoin-illegal-thai-exchange-suspends-trading>
  > CoinDesk contemporaneous reporting dated 2013-07-29 documenting
> Bitcoin Co. Ltd's posted statement that the Bank of Thailand
> (BOT) had held a meeting earlier that day, at which senior
> members of the BOT Foreign Exchange Administration and Policy
> Department advised that — due to lack of existing applicable
> laws, capital controls, and the multi-facet nature of Bitcoin —
> Bitcoin-related activities (purchase / sale of bitcoins,
> purchase / sale of goods or services in bitcoins, sending or
> receiving bitcoins from outside the country) were illegal in
> Thailand. The BOT statement was verbal / informal and was not
> issued as a published regulation; Bitcoin Co. Ltd had originally
> approached the BOT seeking clearance for its bitcoin-exchange
> business and was advised to suspend trading. Evidence
> contextual_unarchived: no published BOT primary instrument was
> captured in this authoring pass and the verbal nature of the BOT
> statement means the load-bearing primary anchor is the
> contemporaneous Bitcoin Co. Ltd corporate statement reproduced
> in CoinDesk reporting. Specific Wayback snapshot timestamp
> requires re-pinning during human audit.
- **`supporting_journalism`**
  - URL: <https://www.bangkokpost.com/business/362222/bitcoin-declared-illegal-in-thailand>
  - Wayback: <https://web.archive.org/web/2013/https://www.bangkokpost.com/business/362222/bitcoin-declared-illegal-in-thailand>
  > Bangkok Post 2013-07 contemporaneous coverage titled "Virtual
> currency Bitcoin banned" documenting the BOT's informal
> prohibition and the Bitcoin Co. Ltd operational suspension.
> Domestic Thai-press corroboration of the CoinDesk anchor.
> Marked evidence_use=contextual_unarchived pending Wayback
> snapshot re-pin during human audit.
- **`supporting_journalism`**
  - URL: <https://reason.com/2013/07/31/thailands-central-bank-outlaws-bitcoin-t/>
  - Wayback: <https://web.archive.org/web/2013/https://reason.com/2013/07/31/thailands-central-bank-outlaws-bitcoin-t/>
  > Reason magazine 2013-07-31 secondary commentary noting that the
> BOT prohibition was an informal verbal advisement rather than a
> published regulation, and that the BOT lacks the constitutional
> authority to outlaw Bitcoin outright. Useful for documenting
> the contemporaneous English-language framing of the BOT action
> as administrative-advisement rather than statutory ban.
> Marked evidence_use=contextual_unarchived pending Wayback
> re-pin during human audit.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Bitcoin Co. Ltd (Thailand)
- **Chains**: `bitcoin`

> Bitcoin Co. Ltd, a Thailand-incorporated Bitcoin exchange that had
> formally approached the Bank of Thailand seeking clearance for its
> bitcoin-exchange business. The BOT's 2013-07-29 verbal advisement
> directly addressed Bitcoin Co. Ltd's planned operations; Bitcoin
> Co. Ltd suspended its exchange services in compliance. Contemporary
> Thai bitcoin-trading activity at Bahtcoin and Coinmill is reported
> to have continued in the immediate aftermath, so the named target
> enumeration is the Bitcoin Co. Ltd entity rather than the entire
> class of Thai bitcoin exchanges. Subset (not complete) per codebook
> §7: the BOT advisement was framed as broadly applicable to bitcoin
> activity in Thailand but operational compliance was concentrated at
> the one entity that had sought clearance.

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `direct` · Δt = 0h

**Event label**: `bitcoin_co_ltd_thailand_exchange_services_suspended_per_bot_advisement`

**Timestamp**: `2013-07-29 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_corporate`**
  - URL: <https://bitcoin.co.th/trading-suspended-due-to-bank-of-thailand-advisement/>
  - Wayback: <https://web.archive.org/web/20140212082550/https://bitcoin.co.th/trading-suspended-due-to-bank-of-thailand-advisement/>
  - body_hash: `sha256:b46d45646e9277ed4f8fe35c60c07463533d93e8da63edc85ffbbc289c16ddef`
  - body_path: `sources/http_captures/thailand-bot-bitcoin-prohibition-2013/v0_3_primary_repair/web.archive.org__web-2013-https-bitcoin.co.th-trading-suspended-due-to-bank-of-thailand-advisement__cb8eeb9d82.html`
  > Primary operator-side observation anchor. The archived Bitcoin
> Co. Ltd statement says the purpose of the statement is to
> inform users about the company's choice to suspend services,
> identifies the 2013-07-29 BOT meeting, enumerates the
> bitcoin activities the BOT department advised were illegal,
> and states Bitcoin Co. Ltd had no choice but to suspend
> operations until Thai law accounted for Bitcoin. This anchors
> the observed offramp_cex suspension; it does not convert the
> BOT verbal advisement into a published primary legal
> instrument.
- **`semi_primary_wayback`**
  - URL: <https://www.coindesk.com/markets/2013/07/29/bank-of-thailand-allegedly-declares-bitcoin-illegal-thai-exchange-suspends-trading>
  - Wayback: <https://web.archive.org/web/20211020132827/https://www.coindesk.com/markets/2013/07/29/bank-of-thailand-allegedly-declares-bitcoin-illegal-thai-exchange-suspends-trading>
  - body_hash: `sha256:08c86630fd782a881e0738342dc88392d4c57b5d3845b77044177adae0a008dd`
  - body_path: `sources/http_captures/thailand-bot-bitcoin-prohibition-2013/primary/web.archive.org__web-20211020132827-https-www.coindesk.com-markets-2013-07-29-bank-of-thailand-allegedly-declares-bitcoin-illegal-thai-exchange-suspends-trading__b8cd63044c.html`
  > CoinDesk 2013-07-29 article reproducing Bitcoin Co. Ltd's
> corporate statement that the operator had no choice but to
> suspend operations following the BOT Foreign Exchange
> Administration and Policy Department verbal advisement.
> attribution=direct under codebook §1.4-analogous reasoning:
> the operator publicly cites the BOT advisement as the cause
> of its suspension, and the BOT advisement explicitly named
> Bitcoin Co. Ltd's planned exchange business as the addressee.
> DRYRUN: Wayback snapshot timestamp deferred to human audit.
- **`supporting_journalism`**
  - URL: <https://www.bangkokpost.com/business/362222/bitcoin-declared-illegal-in-thailand>
  - Wayback: <https://web.archive.org/web/2013/https://www.bangkokpost.com/business/362222/bitcoin-declared-illegal-in-thailand>
  > Bangkok Post domestic-press corroboration of the Bitcoin Co.
> Ltd suspension and the BOT advisement. DRYRUN: Wayback
> snapshot timestamp deferred to human audit.

## 5. Honest coverage gaps

- **l4_frontend** (`not_measured`): Bitcoin Co. Ltd's customer-facing site (bitcoin.co.th) posted the

## 7. Related events

- [`china-pboc-crypto-ban-2013-12`](./china-pboc-crypto-ban-2013-12.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `1c9c65c`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

