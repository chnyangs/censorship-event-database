# Evidence chain — `bitcoin-maven-tetley-doj-2018`

**Status**: `admitted` · **Stratum**: `S3_doj_sec_cftc_fiod` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-08` · **Source commit**: `ee7bf1a` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-31` · **Tool version**: `0.1.0` · **Generated**: `2026-06-25T23:48:26Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "On 2018-07-09 DOJ USAO-CDCA announced that Theresa Lynn Tetley, a/k/a
> 'Bitcoin Maven,' was sentenced for operating an unlicensed bitcoin-for-cash
> money-transmitting business advertised on LocalBitcoins and for money
> laundering. This draft models only the termination of Tetley's individual
> P2P off-ramp service; it does not claim a LocalBitcoins platform shutdown,
> frontend block, asset freeze, or consensus/RPC effect."

## 1. Trigger

- **Type**: `doj_indictment`
- **Actor**: `US_DOJ_CDCA`
- **Timestamp**: `2018-07-09 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://www.justice.gov/usao-cdca/pr/bitcoin-maven-sentenced-one-year-federal-prison-bitcoin-money-laundering-case>
  - Wayback: <https://web.archive.org/web/20180711091804/https://www.justice.gov/usao-cdca/pr/bitcoin-maven-sentenced-one-year-federal-prison-bitcoin-money-laundering-case>
  - body_hash: `sha256:9635191abc6428fe45c63c676552aba881abc8e42190373ac2aae53ddea46dc7`
  - body_path: `sources/http_captures/bitcoin-maven-tetley-doj-2018/primary/web.archive.org__web-20180711091804-https-www.justice.gov-usao-cdca-pr-bitcoin-maven-sentenced-one-year-federal-prison-bitcoin-money-laundering-case__66dc046376.html`
  > DOJ USAO-CDCA press release, archived by Wayback on 2018-07-11 and
> captured locally on 2026-05-31. The body states that Theresa Lynn
> Tetley, known as "Bitcoin Maven," admitted to operating an unlicensed
> bitcoin-for-cash exchange business, was sentenced on 2018-07-09 to
> 12 months and one day in federal prison, pleaded guilty to operating
> an unlicensed money transmitting business and money laundering, used
> localbitcoins.com, exchanged between $6M and $9.5M for customers, and
> was ordered to forfeit 40 Bitcoin, $292,264 in cash, and gold bars.
> Direct live-page capture on 2026-05-31 returned a DOJ Akamai
> interstitial, so the replayable body anchor is the Wayback memento.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Theresa Lynn Tetley a/k/a Bitcoin Maven
- **Chains**: `bitcoin`
- **Canonical domains**: `localbitcoins.com`

> Single named individual P2P bitcoin-for-cash exchanger Theresa Lynn Tetley
> a/k/a "Bitcoin Maven." The DOJ source identifies LocalBitcoins as the
> advertising surface and gives aggregate transaction volume, but it does not
> enumerate a customer list, wallet set, or business domain controlled by
> Tetley. The target is therefore the individual unlicensed MSB/off-ramp
> service, not LocalBitcoins as a platform.

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `direct` · Δt = 0h

**Event label**: `tetley_bitcoin_for_cash_msb_terminated_by_doj_sentencing`

**Timestamp**: `2018-07-09 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_legal`**
  - URL: <https://www.justice.gov/usao-cdca/pr/bitcoin-maven-sentenced-one-year-federal-prison-bitcoin-money-laundering-case>
  - Wayback: <https://web.archive.org/web/20180711091804/https://www.justice.gov/usao-cdca/pr/bitcoin-maven-sentenced-one-year-federal-prison-bitcoin-money-laundering-case>
  - body_hash: `sha256:9635191abc6428fe45c63c676552aba881abc8e42190373ac2aae53ddea46dc7`
  - body_path: `sources/http_captures/bitcoin-maven-tetley-doj-2018/primary/web.archive.org__web-20180711091804-https-www.justice.gov-usao-cdca-pr-bitcoin-maven-sentenced-one-year-federal-prison-bitcoin-money-laundering-case__66dc046376.html`
  > The official DOJ source records the 2018-07-09 sentence, guilty plea
> posture, LocalBitcoins-advertised bitcoin-for-cash service, aggregate
> exchange volume, and forfeiture. Attribution is direct because the
> legal action and incarceration/forfeiture are the terminating act for
> the individual off-ramp service; the row does not claim a shutdown of
> LocalBitcoins itself.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`shrem-faiella-bitcoin-exchange-2014`](./shrem-faiella-bitcoin-exchange-2014.md)
- [`powell-unlicensed-bitcoin-exchange-2014`](./powell-unlicensed-bitcoin-exchange-2014.md)
- [`fincen-eric-powers-p2p-exchanger-2019-04`](./fincen-eric-powers-p2p-exchanger-2019-04.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `ee7bf1a`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

