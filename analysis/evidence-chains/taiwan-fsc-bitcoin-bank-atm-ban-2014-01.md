# Evidence chain — `taiwan-fsc-bitcoin-bank-atm-ban-2014-01`

**Status**: `admitted` · **Stratum**: `S4_nation_state` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `b3ed1c5` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-31` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "Taiwan's FSC on 2014-01-06 barred banks and financial institutions from
> bitcoin conversion/acceptance and from operating bitcoin ATMs, and refused
> Robocoin ATM installation. Effect carried at the offramp_cex
> (payment-rail) layer at institution-class level."

## 1. Trigger

- **Type**: `nation_state_block`
- **Actor**: `TW_FSC`
- **Timestamp**: `2014-01-06 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`semi_primary_wayback`**
  - URL: <http://www.taipeitimes.com/News/biz/archives/2014/01/07/2003580688>
  - Wayback: <https://web.archive.org/web/20140109163139/http://www.taipeitimes.com/News/biz/archives/2014/01/07/2003580688>
  - body_hash: `sha256:a5fb9b0d0ff23f4f567c245dfa54e12c0917c75388d5a15412753c81034a801d`
  - body_path: `sources/http_captures/taiwan-fsc-bitcoin-bank-atm-ban-2014-01/primary/web.archive.org__web-20140110000000-http-www.taipeitimes.com-News-biz-archives-2014-01-07-2003580688__46d53f886c.html`
  > Taipei Times report "FSC bans banks using bitcoins" (published
> 2014-01-07, reporting the FSC's 2014-01-06 announcement). The
> Financial Supervisory Commission "barred local banks and financial
> institutions from bitcoin conversion or using the virtual currency as
> a payment tool via automated teller machines (ATMs)" and stated that
> "financial institutions may not accept bitcoins or provide conversion
> in an effort to avoid consumer disputes and related trading risks."
> This was issued jointly with the central bank, which ruled bitcoin "a
> virtual commodity, not a currency." The announcement followed
> Robocoin's plan to install bitcoin ATMs in Taiwan; the FSC stated such
> installation would require FSC approval, which would not be given.
> Wayback snapshot 20140109163139 (contemporaneous, ~3 days post-event)
> captured replayable body_hash. Snapshot timestamp to be re-pinned
> during human audit.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Taiwan banks / financial institutions + Robocoin bitcoin ATM (class)
- **Chains**: `bitcoin`

> Canonical target is the class of Taiwan banks and financial institutions
> barred from accepting/converting bitcoin or operating bitcoin ATMs, plus
> the specific Robocoin bitcoin-ATM deployment whose installation the FSC
> refused to approve. Class-level target (no enumerated roster of banks);
> enumeration=subset because the FSC order addresses the financial-
> institution population class and the named Robocoin ATM deployment without
> a fixed entity list.

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `plausible` · Δt = 0h

**Event label**: `fsc_barred_banks_from_bitcoin_conversion_and_atms`

**Timestamp**: `2014-01-06 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`semi_primary_wayback`**
  - URL: <http://www.taipeitimes.com/News/biz/archives/2014/01/07/2003580688>
  - Wayback: <https://web.archive.org/web/20140109163139/http://www.taipeitimes.com/News/biz/archives/2014/01/07/2003580688>
  - body_hash: `sha256:a5fb9b0d0ff23f4f567c245dfa54e12c0917c75388d5a15412753c81034a801d`
  - body_path: `sources/http_captures/taiwan-fsc-bitcoin-bank-atm-ban-2014-01/primary/web.archive.org__web-20140110000000-http-www.taipeitimes.com-News-biz-archives-2014-01-07-2003580688__46d53f886c.html`
  > Taipei Times 2014-01-07 "FSC bans banks using bitcoins": the FSC
> barred banks/financial institutions from bitcoin conversion or using
> bitcoin as a payment tool via ATMs, and stated "financial
> institutions may not accept bitcoins or provide conversion."
> attribution=plausible (per codebook §1.5/§8.4): the action is
> carried by contemporaneous press (semi_primary_wayback) quoting the
> FSC, not the FSC's own primary_legal order text; the primary FSC
> instrument has not been pinned in this draft pass.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`russia-cbr-bitcoin-information-letter-2014`](./russia-cbr-bitcoin-information-letter-2014.md)
- `jordan-cbj-crypto-banking-ban-2014` (not found; no rendered admitted-chain link)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `b3ed1c5`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

