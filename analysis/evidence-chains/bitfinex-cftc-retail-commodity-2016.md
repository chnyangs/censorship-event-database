# Evidence chain — `bitfinex-cftc-retail-commodity-2016`

**Status**: `admitted` · **Stratum**: `S3_doj_sec_cftc_fiod` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `80b0ca3` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-16` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "The 2016-06-02 CFTC order In re BFXNA Inc. d/b/a Bitfinex
> (Docket No. 16-19) required Bitfinex to pay a $75,000 civil penalty
> and to discontinue its operating margin-trading pool model in favor
> of an actual-delivery margin model within 28 days, registered here
> as a single-layer offramp_cex operator-state-change observation; the
> row does not assert frontend takedown, ISP-level network blocking,
> or on-chain asset effects."

## 1. Trigger

- **Type**: `cftc_action`
- **Actor**: `US_CFTC`
- **Timestamp**: `2016-06-02 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://www.cftc.gov/PressRoom/PressReleases/7380-16>
  - Wayback: <https://web.archive.org/web/2016/https://www.cftc.gov/PressRoom/PressReleases/7380-16>
  > CFTC press release 7380-16 (2016-06-02): "CFTC Orders Bitcoin
> Exchange Bitfinex to Pay $75,000 for Offering Illegal Off-Exchange
> Financed Retail Commodity Transactions and Failing to Register as
> a Futures Commission Merchant." Announces simultaneous filing and
> settlement of CFTC administrative action against BFXNA Inc.
> d/b/a Bitfinex (Hong Kong-based crypto exchange operator). Order
> imposes $75,000 civil monetary penalty and cease-and-desist;
> Bitfinex required to discontinue its operating margin-trading
> pool model (in which Bitfinex held margin collateral in a single
> omnibus pool) and move to an actual-delivery margin model within
> 28 days. Marked evidence_use=contextual_unarchived because the
> authoring LLM agent did not personally pin a Wayback snapshot
> timestamp or compute a body_hash for the press release; the CFTC
> press-release URL format is stable and routinely captured by
> Wayback, but the specific snapshot timestamp is to be re-pinned
> during human audit before this citation may serve as an admission
> anchor in its own right. Provisional Wayback anchor uses Wayback
> Machine year-prefix lookup.
- **`primary_legal`**
  - URL: <https://www.cftc.gov/sites/default/files/idc/groups/public/@lrenforcementactions/documents/legalpleading/enfbfxnaorder060216.pdf>
  - Wayback: <https://web.archive.org/web/2016/https://www.cftc.gov/sites/default/files/idc/groups/public/@lrenforcementactions/documents/legalpleading/enfbfxnaorder060216.pdf>
  > CFTC order In the Matter of BFXNA Inc. d/b/a Bitfinex,
> CFTC Docket No. 16-19, dated 2016-06-02. Findings: from
> approximately April 2013 through at least February 2016 Bitfinex
> operated an online platform for exchanging and trading
> cryptocurrencies, including Bitcoin, and offered financed retail
> commodity transactions in Bitcoin to U.S. customers without
> registering as a Futures Commission Merchant (FCM) as required
> by the Commodity Exchange Act. Bitfinex's financed-margin
> product was found to violate CEA Section 4(a) (off-exchange
> retail commodity transactions not resulting in actual delivery
> within 28 days) and Section 4d (operating without FCM
> registration). Order requires the $75,000 civil penalty, a
> cease-and-desist, and prospective changes to Bitfinex's
> margin-trading product to satisfy the 28-day actual-delivery
> exception. Marked evidence_use=contextual_unarchived pending
> Wayback re-pin and body_hash capture during human audit.
> Provisional Wayback anchor uses Wayback Machine year-prefix
> lookup.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: BFXNA Inc. d/b/a Bitfinex
- **Chains**: `bitcoin`
- **Canonical domains**: `bitfinex.com`

> BFXNA Inc. d/b/a Bitfinex (the entity named in CFTC Docket No.
> 16-19), the operator of the Bitfinex.com cryptocurrency trading
> platform. The row enumerates only the BFXNA Inc. corporate entity
> and its financed-margin retail commodity product line; it does not
> enumerate individual Bitfinex customer accounts or specific
> on-chain BTC addresses tied to the platform's margin pool. The
> Bitfinex domain (bitfinex.com) is the canonical operator-controlled
> frontend.

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `direct` · Δt = 0h

**Event label**: `cftc_ordered_bitfinex_margin_trading_product_change_to_actual_delivery_model`

**Timestamp**: `2016-06-02 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_legal`**
  - URL: <https://www.cftc.gov/PressRoom/PressReleases/7380-16>
  - Wayback: <https://web.archive.org/web/2016/https://www.cftc.gov/PressRoom/PressReleases/7380-16>
  > CFTC press release 7380-16 announces the order requiring
> Bitfinex to pay a $75,000 civil penalty, cease and desist
> from CEA violations, and modify its margin-trading product
> so that financed retail commodity transactions result in
> actual delivery within 28 days. attribution=direct because
> the CFTC order itself mandates the operator-state change to
> Bitfinex's financed-margin product line. Provisional Wayback
> anchor uses Wayback Machine year-prefix lookup.
- **`primary_legal`**
  - URL: <https://www.cftc.gov/sites/default/files/idc/groups/public/@lrenforcementactions/documents/legalpleading/enfbfxnaorder060216.pdf>
  - Wayback: <https://web.archive.org/web/2016/https://www.cftc.gov/sites/default/files/idc/groups/public/@lrenforcementactions/documents/legalpleading/enfbfxnaorder060216.pdf>
  > CFTC order In the Matter of BFXNA Inc. d/b/a Bitfinex,
> Docket No. 16-19. Findings of fact describe Bitfinex's
> operating margin-trading pool model and the regulator-
> required transition to an actual-delivery model. Marked
> evidence_use=contextual_unarchived pending Wayback re-pin.
> Provisional Wayback anchor uses Wayback Machine year-prefix
> lookup.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`nydfs-bitlicense-2015-06`](./nydfs-bitlicense-2015-06.md)
- [`coinflip-cftc-derivabit-2015`](./coinflip-cftc-derivabit-2015.md)
- [`cftc-v-ooki-dao-2022`](./cftc-v-ooki-dao-2022.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `80b0ca3`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

