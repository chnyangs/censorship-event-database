# Evidence chain — `teraexchange-cftc-bitcoin-swap-2015`

**Status**: `admitted` · **Stratum**: `S3_doj_sec_cftc_fiod` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-02` · **Source commit**: `60f1d90` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-16` · **Tool version**: `0.1.0` · **Generated**: `2026-06-02T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "CFTC In re TeraExchange LLC (Order issued 2015-09-24, Docket 15-33)
> is the first CFTC enforcement action against a CFTC-registered Swap
> Execution Facility offering a Bitcoin-referenced derivative product.
> The captured Order imposed a cease-and-desist plus binding
> undertakings on the SEF; the retained observation anchors only the
> regulator-side regime-change action at the offramp_cex layer. No
> civil monetary penalty was imposed in the 2015-09-24 Order, and no
> L0/L1/L3/L4-frontend/asset-onchain effects are claimed."

## 1. Trigger

- **Type**: `cftc_action`
- **Actor**: `US_CFTC`
- **Timestamp**: `2015-09-24 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://www.cftc.gov/PressRoom/PressReleases/7240-15>
  - body_hash: `sha256:158a1dbcad61e5cefa74c75e4f2779b13aa831e8657f4e2203ae7b28bb583d78`
  - body_path: `sources/http_captures/teraexchange-cftc-bitcoin-swap-2015/primary/www.cftc.gov__PressRoom-PressReleases-7240-15__5082f96e2b.html`
  > CFTC Release 7240-15 (2015-09-24): "CFTC Settles with TeraExchange
> LLC for Failing to Enforce Prohibitions on Wash Trading and
> Prearranged Trading in Bitcoin Swap." First CFTC enforcement
> action involving a CFTC-registered Swap Execution Facility (SEF)
> and a Bitcoin-referenced derivative. The CFTC Order requires Tera
> to cease and desist from future violations of its SEF
> rule-enforcement obligations under Section 5h(f)(2) of the CEA
> and CFTC Regulation 37.203. Captured 2026-05-16.
- **`primary_legal`**
  - URL: <https://www.cftc.gov/idc/groups/public/@lrenforcementactions/documents/legalpleading/enfteraexchangeorder92415.pdf>
  - body_hash: `sha256:101633f08b454df506f01ae226361c48cb6a58f2e9e74efca05cca917c88e9c2`
  - body_path: `sources/http_captures/teraexchange-cftc-bitcoin-swap-2015/primary/www.cftc.gov__idc-groups-public-lrenforcementactions-documents-legalpleading-enfteraexchangeorder92415.pdf__be2f47b647.bin`
  > Underlying CFTC Order in In re TeraExchange LLC (CFTC Docket No.
> 15-33, 2015-09-24, 9 pp.). Findings: Tera (provisionally
> registered SEF) self-certified a non-deliverable forward
> referenced to a USD/Bitcoin index ("Bitcoin Swap") on 2014-09-11
> and arranged for the only two onboarded counterparties to
> execute two offsetting USD 500,000-notional trades on
> 2014-10-08, then publicly announced the trades on 2014-10-09
> without disclosing they were prearranged wash sales executed
> "to test the pipes." Order: cease-and-desist under 7 U.S.C.
> § 7b-3(f)(2) and 17 C.F.R. § 37.203, plus undertakings on
> public statements and SEF rule enforcement. **No civil monetary
> penalty was imposed** in this 2015-09-24 Order (the brief's
> "$300K civil penalty" appears to conflate this matter with a
> later 2019 CFTC trade-data reporting action against the same
> SEF). Final URL after redirect adds /sites/default/files/
> prefix; the requested-URL form above is the canonical CFTC
> permalink documented in Release 7240-15.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `complete`
- **Protocol**: `tera_bitcoin_usd_swap`
- **Actor name**: TeraExchange LLC
- **Chains**: `bitcoin`
- **Canonical domains**: `teraexchange.com`

> Single respondent: TeraExchange LLC (then a provisionally registered
> Swap Execution Facility based in Summit, New Jersey). The Order's
> binding effect runs against Tera and its successors and assigns.
> The two anonymized counterparties ("Firm A" and "Firm B") were not
> named respondents and are out of scope; only the SEF operator is
> enumerated as the target.

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `direct` · Δt = 0h

**Event label**: `cftc_order_imposing_cease_and_desist_and_undertakings_on_sef_for_bitcoin_swap`

**Timestamp**: `2015-09-24 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_legal`**
  - URL: <https://www.cftc.gov/idc/groups/public/@lrenforcementactions/documents/legalpleading/enfteraexchangeorder92415.pdf>
  - body_hash: `sha256:101633f08b454df506f01ae226361c48cb6a58f2e9e74efca05cca917c88e9c2`
  - body_path: `sources/http_captures/teraexchange-cftc-bitcoin-swap-2015/primary/www.cftc.gov__idc-groups-public-lrenforcementactions-documents-legalpleading-enfteraexchangeorder92415.pdf__be2f47b647.bin`
  > CFTC Order (Docket 15-33) is the direct, same-day instrument
> of the regime change at the offramp_cex / regulated-venue
> layer: it adjudicates findings against the SEF, orders
> cease-and-desist under 7 U.S.C. § 7b-3(f)(2) and 17 C.F.R.
> § 37.203, and imposes binding undertakings on Tera and its
> successors and assigns. attribution=direct because the
> regulator's own instrument is the action being recorded.
- **`primary_legal`**
  - URL: <https://www.cftc.gov/PressRoom/PressReleases/7240-15>
  - body_hash: `sha256:158a1dbcad61e5cefa74c75e4f2779b13aa831e8657f4e2203ae7b28bb583d78`
  - body_path: `sources/http_captures/teraexchange-cftc-bitcoin-swap-2015/primary/www.cftc.gov__PressRoom-PressReleases-7240-15__5082f96e2b.html`
  > CFTC Release 7240-15 corroborates the Order's substance: SEF
> rule-enforcement failure with respect to wash trading and
> prearranged trading in a Bitcoin swap, cease-and-desist
> remedy, and Tera's status as a provisionally registered SEF.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`nydfs-bitlicense-2015-06`](./nydfs-bitlicense-2015-06.md)
- [`cftc-v-ooki-dao-2022`](./cftc-v-ooki-dao-2022.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `60f1d90`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

