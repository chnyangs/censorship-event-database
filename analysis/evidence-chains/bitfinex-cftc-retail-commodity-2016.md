# Evidence chain — `bitfinex-cftc-retail-commodity-2016`

**Status**: `admitted` · **Stratum**: `S3_doj_sec_cftc_fiod` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-02` · **Source commit**: `2dfaf57` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-16` · **Tool version**: `0.1.0` · **Generated**: `2026-06-02T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "The 2016-06-02 CFTC order In re BFXNA Inc. d/b/a Bitfinex
> (Docket No. 16-19) found that Bitfinex's financed retail bitcoin
> transactions did not result in actual delivery within the statutory
> 28-day window, ordered a $75,000 civil penalty and cease-and-desist,
> and recorded Bitfinex's represented business-practice changes in
> response to the investigation. The row is registered as a single-layer
> offramp_cex operator-state-change observation; it does not assert
> frontend takedown, ISP-level network blocking, or on-chain asset
> effects."

## 1. Trigger

- **Type**: `cftc_action`
- **Actor**: `US_CFTC`
- **Timestamp**: `2016-06-02 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://www.cftc.gov/PressRoom/PressReleases/7380-16>
  - Wayback: <https://web.archive.org/web/2016/https://www.cftc.gov/PressRoom/PressReleases/7380-16>
  - body_hash: `sha256:8671fe9136935077a06ac5155a3ad04076587b7315d4cacd5cd3770edbaf3029`
  - body_path: `sources/http_captures/bitfinex-cftc-retail-commodity-2016/cftc-primary/www.cftc.gov__PressRoom-PressReleases-7380-16__d5a12cecf5.html`
  > CFTC press release 7380-16 (2016-06-02): "CFTC Orders Bitcoin
> Exchange Bitfinex to Pay $75,000 for Offering Illegal Off-Exchange
> Financed Retail Commodity Transactions and Failing to Register as
> a Futures Commission Merchant." Announces simultaneous filing and
> settlement of CFTC administrative action against BFXNA Inc.
> d/b/a Bitfinex (Hong Kong-based crypto exchange operator). Order
> imposes a $75,000 civil monetary penalty and cease-and-desist.
> The release also notes that the CFTC recognized Bitfinex for
> voluntarily making changes to its business practices to attempt
> compliance. SOURCE-REPAIRED 2026-06-01: the live CFTC press
> release was captured locally and pinned with body_hash/body_path.
> The legacy Wayback year-prefix URL remains only as a supplemental
> historical lookup.
- **`primary_legal`**
  - URL: <https://www.cftc.gov/sites/default/files/idc/groups/public/@lrenforcementactions/documents/legalpleading/enfbfxnaorder060216.pdf>
  - Wayback: <https://web.archive.org/web/2016/https://www.cftc.gov/sites/default/files/idc/groups/public/@lrenforcementactions/documents/legalpleading/enfbfxnaorder060216.pdf>
  - body_hash: `sha256:d5de7084ee9f5c4a3e575dda3d6f996ba5e521fed4064674ae9eea1aa4dd9f2c`
  - body_path: `sources/http_captures/bitfinex-cftc-retail-commodity-2016/cftc-primary/www.cftc.gov__sites-default-files-idc-groups-public-lrenforcementactions-documents-legalpleading-enfbfxnaorder060216.pdf__e226b247ff.bin`
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
> registration). The order imposes the $75,000 civil penalty and
> cease-and-desist; it also records that Bitfinex represented it had
> made business-practice changes in response to the investigation to
> attempt compliance. SOURCE-REPAIRED 2026-06-01: the live CFTC PDF
> was captured locally and pinned with body_hash/body_path. The
> legacy Wayback year-prefix URL remains only as a supplemental
> historical lookup.

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

**Event label**: `cftc_ordered_bitfinex_cease_desist_for_financed_retail_bitcoin_transactions`

**Timestamp**: `2016-06-02 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_legal`**
  - URL: <https://www.cftc.gov/PressRoom/PressReleases/7380-16>
  - Wayback: <https://web.archive.org/web/2016/https://www.cftc.gov/PressRoom/PressReleases/7380-16>
  - body_hash: `sha256:8671fe9136935077a06ac5155a3ad04076587b7315d4cacd5cd3770edbaf3029`
  - body_path: `sources/http_captures/bitfinex-cftc-retail-commodity-2016/cftc-primary/www.cftc.gov__PressRoom-PressReleases-7380-16__d5a12cecf5.html`
  > CFTC press release 7380-16 announces the order requiring
> Bitfinex to pay a $75,000 civil penalty and cease and desist
> from CEA violations. It also states that the CFTC recognized
> Bitfinex for voluntarily making business-practice changes to
> attempt compliance. attribution=direct because the observation
> event is the CFTC order and associated compliance posture for
> Bitfinex's financed-margin product line. Local body_hash/body_path
> capture is the admission-grade replay anchor; the legacy Wayback
> year-prefix URL is supplemental.
- **`primary_legal`**
  - URL: <https://www.cftc.gov/sites/default/files/idc/groups/public/@lrenforcementactions/documents/legalpleading/enfbfxnaorder060216.pdf>
  - Wayback: <https://web.archive.org/web/2016/https://www.cftc.gov/sites/default/files/idc/groups/public/@lrenforcementactions/documents/legalpleading/enfbfxnaorder060216.pdf>
  - body_hash: `sha256:d5de7084ee9f5c4a3e575dda3d6f996ba5e521fed4064674ae9eea1aa4dd9f2c`
  - body_path: `sources/http_captures/bitfinex-cftc-retail-commodity-2016/cftc-primary/www.cftc.gov__sites-default-files-idc-groups-public-lrenforcementactions-documents-legalpleading-enfbfxnaorder060216.pdf__e226b247ff.bin`
  > CFTC order In the Matter of BFXNA Inc. d/b/a Bitfinex,
> Docket No. 16-19. Findings of fact describe Bitfinex's
> financed-margin product, the omnibus settlement wallet,
> Bitfinex's retained control of private keys, the failure of
> those transactions to satisfy actual delivery under Section
> 2(c)(2)(D), and the resulting cease-and-desist order. Local
> body_hash/body_path capture is the admission-grade replay
> anchor; the legacy Wayback year-prefix URL is supplemental.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`nydfs-bitlicense-2015-06`](./nydfs-bitlicense-2015-06.md)
- [`coinflip-cftc-derivabit-2015`](./coinflip-cftc-derivabit-2015.md)
- [`cftc-v-ooki-dao-2022`](./cftc-v-ooki-dao-2022.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `2dfaf57`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

