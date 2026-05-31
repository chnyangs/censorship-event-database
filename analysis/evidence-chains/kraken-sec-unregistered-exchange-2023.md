# Evidence chain — `kraken-sec-unregistered-exchange-2023`

**Status**: `admitted` · **Stratum**: `S3_doj_sec_cftc_fiod` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-05-31` · **Source commit**: `1e151cd` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-16` · **Tool version**: `0.1.0` · **Generated**: `2026-05-31T12:31:46Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "The 2023-11-20 SEC v. Payward (Kraken) unregistered-exchange action is
> admitted only for a scoped offramp_cex platform-stance response: Kraken
> posted a contemporaneous corporate response on blog.kraken.com asserting
> continued operational status of customer products and services and
> framing the action as a registration dispute to be defended. The row
> does not claim a Kraken.com frontend takedown, token delisting, fiat-rail
> disruption, on-chain asset freeze, or L1/L3 effect; it is paired with
> kraken-sec-staking-2023 (sibling, which load-bears at offramp_cex with
> a direct US staking-service shutdown) as the two-case Kraken-SEC
> enforcement cohort."

## 1. Trigger

- **Type**: `sec_action`
- **Actor**: `US_SEC`
- **Timestamp**: `2023-11-20 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://www.sec.gov/news/press-release/2023-237>
  - Wayback: <https://web.archive.org/web/2023/https://www.sec.gov/news/press-release/2023-237>
  > SEC press release 2023-237 (2023-11-20): "SEC Charges Kraken for
> Operating as an Unregistered Securities Exchange, Broker, Dealer,
> and Clearing Agency." Civil action in N.D. Cal. against Payward Inc.
> and Payward Ventures Inc. (collectively Kraken) alleging that since
> at least 2018 Kraken commingled customer assets with corporate funds
> and operated an unregistered national securities exchange, broker,
> dealer, and clearing agency for crypto-asset securities. Distinct
> from the 2023-02-09 SEC settlement of Kraken's staking-as-a-service
> program (see kraken-sec-staking-2023): that earlier matter resolved
> an unregistered-securities-offering theory for the staking product;
> this 2023-11-20 case attacks the underlying exchange / broker /
> clearing registration status. Wayback anchor is a 2023 calendar-
> folder pointer rather than a pinned snapshot timestamp of the
> specific press item. Marked evidence_use=contextual_unarchived
> because the authoring LLM agent did not personally pin a Wayback
> timestamp or compute a body_hash; pinned snapshot + body_hash must
> be re-captured during human audit before this citation may serve
> as an admission anchor in its own right. 2025-03-27 SEC dismissed
> the action with prejudice under the Atkins administration.
- **`primary_corporate`**
  - URL: <https://blog.kraken.com/news/sec-charges>
  - Wayback: <https://web.archive.org/web/2023/https://blog.kraken.com/news/sec-charges>
  > Kraken corporate response posted to blog.kraken.com in November 2023
> (Wayback 2023 calendar-folder anchor) framing the SEC complaint as a
> registration dispute, asserting that Kraken does not list securities,
> committing to defend the case, and stating that customer products
> and services remained operational and unchanged. Marked
> evidence_use=contextual_unarchived because the LLM agent did not
> personally pin a Wayback snapshot or compute a body_hash; the
> platform-side artifact must be re-pinned during human audit. The
> Kraken post is load-bearing for the offramp_cex observed_no_change
> claim below: it records the platform-side assertion that no service
> was withdrawn on or immediately after 2023-11-20.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `complete`
- **Actor name**: Kraken / Payward Inc. + Payward Ventures Inc.
- **Canonical domains**: `kraken.com`

> Payward Inc. and Payward Ventures Inc. (the two Kraken operating
> entities named in the SEC complaint). Securities-law allegations are
> pleaded at the exchange-registration / broker / dealer / clearing-agency
> level, not as a token-by-token securities determination. The complaint
> references multiple crypto-asset securities traded on Kraken (including
> tokens previously named as securities in SEC v. Coinbase and SEC v.
> Binance) but does not constitute a token delisting or chain-level event.
> No on-chain addresses; this is an entity-level securities-enforcement
> target.

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `plausible` · Δt = 0h

**Event label**: `kraken_corporate_response_issued_asserting_continued_us_service`

**Timestamp**: `2023-11-20 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_corporate`**
  - URL: <https://blog.kraken.com/news/sec-charges>
  - Wayback: <https://web.archive.org/web/2023/https://blog.kraken.com/news/sec-charges>
  > Kraken corporate response posted in November 2023 asserting that
> customer products and services remained operational and unchanged
> following the SEC complaint, and framing the action as a
> registration dispute Kraken would defend. Used as the platform-
> side anchor for the observed_change at offramp_cex (issuance of
> the platform-stance response). DRYRUN: Wayback anchor is a 2023
> calendar-folder pointer; pinned snapshot timestamp and body_hash
> deferred to human audit.

## 5. Honest coverage gaps

- **l4_frontend** (`not_measured`): No admission-grade L4 frontend diff is retained. Unlike sec-v-binance-2023

## 7. Related events

- [`kraken-sec-staking-2023`](./kraken-sec-staking-2023.md)
- [`sec-v-coinbase-2023`](./sec-v-coinbase-2023.md)
- [`sec-v-binance-2023`](./sec-v-binance-2023.md)
- [`sec-v-bittrex-2023`](./sec-v-bittrex-2023.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `1e151cd`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

