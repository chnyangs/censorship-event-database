# Evidence chain — `coinflip-cftc-derivabit-2015`

**Status**: `admitted` · **Stratum**: `S3_doj_sec_cftc_fiod` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-02` · **Source commit**: `137626c` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-16` · **Tool version**: `0.1.0` · **Generated**: `2026-06-02T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> CFTC Order 15-29 of 2015-09-17 against Coinflip, Inc. (d/b/a
> Derivabit) is the first CFTC enforcement action against a
> cryptocurrency operator and the regulatory artifact that established
> Bitcoin as a "commodity" under CEA Section 1a(9). The cease-and-
> desist targeted the Derivabit Bitcoin-options trading facility as an
> unregistered swap-execution / contract-market facility; the row carries
> a single direct-attribution offramp_cex operator-state observation and
> does not assert public-frontend takedown, ISP-level network blocking,
> or on-chain asset effects.

## 1. Trigger

- **Type**: `cftc_action`
- **Actor**: `US_CFTC`
- **Timestamp**: `2015-09-17 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://www.cftc.gov/PressRoom/PressReleases/7231-15>
  - Wayback: <https://web.archive.org/web/2015/https://www.cftc.gov/PressRoom/PressReleases/7231-15>
  - body_hash: `sha256:920465a3468d985460b819e166c2794fec66a7403645a91ad4aac5a6fab9c45a`
  - body_path: `sources/http_captures/coinflip-cftc-derivabit-2015/cftc-primary/www.cftc.gov__PressRoom-PressReleases-7231-15__baa05c2a12.html`
  > CFTC Press Release 7231-15 (2015-09-17): "CFTC Orders Bitcoin
> Options Trading Platform Operator and its CEO to Cease Illegally
> Offering Bitcoin Options and to Cease Operating a Facility for
> Trading or Processing of Swaps without Registering." The CFTC
> simultaneously issued an Order (CFTC Docket No. 15-29) finding
> that Coinflip, Inc. (d/b/a Derivabit) and its CEO Francisco
> Riordan operated an online facility for trading Bitcoin options
> without registering as a swap execution facility (SEF) or as a
> designated contract market (DCM) under the Commodity Exchange
> Act (CEA). Historic significance: (1) first CFTC enforcement
> action against a cryptocurrency operator, (2) the order formally
> established that Bitcoin and other virtual currencies are
> "commodities" within the meaning of CEA Section 1a(9), 7 U.S.C.
> Section 1a(9). The order required Coinflip / Riordan to cease
> and desist from violating the CEA and CFTC regulations.
> SOURCE-REPAIRED 2026-06-01: the live CFTC press release was
> captured locally and pinned with body_hash/body_path. The
> legacy Wayback year-prefix URL remains only as a supplemental
> historical lookup.
- **`primary_legal`**
  - URL: <https://www.cftc.gov/sites/default/files/idc/groups/public/@lrenforcementactions/documents/legalpleading/enfcoinfliprorder09172015.pdf>
  - Wayback: <https://web.archive.org/web/2015/https://www.cftc.gov/sites/default/files/idc/groups/public/@lrenforcementactions/documents/legalpleading/enfcoinfliprorder09172015.pdf>
  - body_hash: `sha256:259885f773dec60af1936fbd0eee48a5a41e62e56bcaaf7bfb7c35af18bc8ff4`
  - body_path: `sources/http_captures/coinflip-cftc-derivabit-2015/cftc-primary/www.cftc.gov__sites-default-files-idc-groups-public-lrenforcementactions-documents-legalpleading-enfcoinfliprorder09172015.pdf__7fe36a5fcf.bin`
  > CFTC Order Instituting Proceedings, CFTC Docket No. 15-29,
> "In the Matter of: Coinflip, Inc. d/b/a Derivabit, and
> Francisco Riordan" (2015-09-17). The order findings (Section
> III) establish that "Bitcoin and other virtual currencies are
> encompassed in the definition [of commodity] and properly
> defined as commodities" under CEA Section 1a(9). Operative
> provisions: cease-and-desist against further CEA violations.
> SOURCE-REPAIRED 2026-06-01: the live CFTC PDF was captured
> locally and pinned with body_hash/body_path. The legacy Wayback
> year-prefix URL remains only as a supplemental historical lookup.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `complete`
- **Actor name**: Coinflip, Inc. (d/b/a Derivabit)
- **Chains**: `bitcoin`
- **Canonical domains**: `derivabit.com`

> Named respondents in CFTC Order 15-29 are Coinflip, Inc. (d/b/a
> Derivabit) and its CEO Francisco Riordan as the individual
> operator. No on-chain Bitcoin addresses are enumerated in the CFTC
> order; the action targets the unregistered-swap-execution-facility
> legal theory rather than specific addresses. Canonical Derivabit
> domain derivabit.com is enumerated below.

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `direct` · Δt = 0h

**Event label**: `cftc_ordered_coinflip_derivabit_cease_desist_for_unregistered_bitcoin_options_facility`

**Timestamp**: `2015-09-17 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_legal`**
  - URL: <https://www.cftc.gov/PressRoom/PressReleases/7231-15>
  - Wayback: <https://web.archive.org/web/2015/https://www.cftc.gov/PressRoom/PressReleases/7231-15>
  - body_hash: `sha256:920465a3468d985460b819e166c2794fec66a7403645a91ad4aac5a6fab9c45a`
  - body_path: `sources/http_captures/coinflip-cftc-derivabit-2015/cftc-primary/www.cftc.gov__PressRoom-PressReleases-7231-15__baa05c2a12.html`
  > CFTC press release 7231-15 explicitly directs Coinflip /
> Riordan to cease operating the Derivabit facility without
> registering as a SEF or DCM. attribution=direct because the
> observation event is the CFTC cease-and-desist / operator-state
> order for the Derivabit Bitcoin-options facility. Local
> body_hash/body_path capture is the admission-grade replay
> anchor; the legacy Wayback year-prefix URL is supplemental.
- **`primary_legal`**
  - URL: <https://www.cftc.gov/sites/default/files/idc/groups/public/@lrenforcementactions/documents/legalpleading/enfcoinfliprorder09172015.pdf>
  - Wayback: <https://web.archive.org/web/2015/https://www.cftc.gov/sites/default/files/idc/groups/public/@lrenforcementactions/documents/legalpleading/enfcoinfliprorder09172015.pdf>
  - body_hash: `sha256:259885f773dec60af1936fbd0eee48a5a41e62e56bcaaf7bfb7c35af18bc8ff4`
  - body_path: `sources/http_captures/coinflip-cftc-derivabit-2015/cftc-primary/www.cftc.gov__sites-default-files-idc-groups-public-lrenforcementactions-documents-legalpleading-enfcoinfliprorder09172015.pdf__7fe36a5fcf.bin`
  > CFTC Order 15-29 cease-and-desist operative provisions
> establish the legal compulsion behind the Derivabit
> operator-state observation. Local body_hash/body_path capture
> is the admission-grade replay anchor; the legacy Wayback
> year-prefix URL is supplemental.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`btc-e-doj-2017`](./btc-e-doj-2017.md)
- [`cftc-v-ooki-dao-2022`](./cftc-v-ooki-dao-2022.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `137626c`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

