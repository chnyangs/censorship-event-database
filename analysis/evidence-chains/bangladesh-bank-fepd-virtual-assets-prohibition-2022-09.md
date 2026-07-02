# Evidence chain — `bangladesh-bank-fepd-virtual-assets-prohibition-2022-09`

**Status**: `admitted` · **Stratum**: `S4_nation_state` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-08` · **Source commit**: `ee7bf1a` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-31` · **Tool version**: `0.1.0` · **Generated**: `2026-06-25T23:48:26Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> On 2022-09-15, Bangladesh Bank's Foreign Exchange Policy Department issued FE
> Circular No. 24 prohibiting transactions made in/from/to Bangladesh for
> obtaining virtual assets or virtual currencies and prohibiting facilitation of
> business, activities, and operations associated with their
> exchange/transfer/trading. This draft models the action as a single-layer S4
> nation-state foreign-exchange / financial-rail restriction at offramp_cex; no
> L0/L1/L3/L4 or asset-onchain effect is claimed.

## 1. Trigger

- **Type**: `nation_state_block`
- **Actor**: `BD_BB_FEPD`
- **Timestamp**: `2022-09-15 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://www.bb.org.bd/mediaroom/circulars/fepd/sep152022fepd24e.pdf>
  - body_hash: `sha256:f88145cd6358c849b0e23c1ea2453392d2b2e917152aeb670aad7005868c81d8`
  - body_path: `sources/http_captures/bangladesh-bank-fepd-virtual-assets-prohibition-2022-09/primary/www.bb.org.bd__mediaroom-circulars-fepd-sep152022fepd24e.pdf__a437219e06.bin`
  > Bangladesh Bank Foreign Exchange Policy Department FE Circular No. 24,
> dated 2022-09-15, titled "Prohibition regarding virtual assets, virtual
> currencies and facilitating their exchange/transfer/trading." The
> circular is addressed to scheduled banks, authorized dealers of foreign
> exchange, MFS providers, financial institutions, other concerns, and all
> stakeholders associated with foreign-exchange dealings in Bangladesh.
> `pdftotext` on the captured PDF confirms the load-bearing provisions:
> virtual currencies are not recognized as currency, are not approved
> foreign exchange/currency or approved transaction/investment forms, any
> transaction made in/from/to Bangladesh for obtaining virtual assets or
> virtual currencies is not permitted by Bangladesh Bank, facilitation of
> virtual-asset exchange/transfer/trading is not permitted, and violations
> are treated as contraventions of the Foreign Exchange Regulation Act,
> 1947 subject to cognizance under Section 23(1).
- **`primary_government`**
  - URL: <https://www.bb.org.bd/pub/annual/bfiu/bfiu_2021-2022.pdf>
  - body_hash: `sha256:c46b2f47c8c2fe0bdad07cc1ab35a7039915762c2f2d9886557d929a45299e7f`
  - body_path: `sources/http_captures/bangladesh-bank-fepd-virtual-assets-prohibition-2022-09/primary/www.bb.org.bd__pub-annual-bfiu-bfiu_2021-2022.pdf__5f0c377ee2.bin`
  > Bangladesh Financial Intelligence Unit Annual Report 2021-22, hosted by
> Bangladesh Bank. The report corroborates the 2022-09-15 FEPD circular
> and describes the policy as a prohibition of virtual assets, virtual
> currencies, and facilitation of exchange/transfer/trading. It also
> documents BFIU reporting context: 107 STR/SARs related to virtual
> currency and online forex trading as of June 2022, and law-enforcement
> activity involving detected cases and arrests during the preceding
> five-year period. Used as official corroboration and operational
> context, not as a separate trigger.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Bangladesh virtual-asset dealing and facilitation class

> Bangladesh scheduled banks, authorized foreign-exchange dealers, mobile
> financial service providers, financial institutions, other concerns, and
> stakeholders associated with foreign-exchange dealings, plus the class of
> individuals/entities/institutions operating in Bangladesh that might deal in
> or facilitate exchange/transfer/trading of virtual assets or virtual
> currencies. The circular is class-level and does not enumerate specific
> exchanges, banks, MFS providers, user accounts, domains, tokens, or
> blockchain addresses.

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `direct` · Δt = 0h

**Event label**: `virtual_asset_dealing_and_facilitation_not_permitted_by_bangladesh_bank`

**Timestamp**: `2022-09-15 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_legal`**
  - URL: <https://www.bb.org.bd/mediaroom/circulars/fepd/sep152022fepd24e.pdf>
  - body_hash: `sha256:f88145cd6358c849b0e23c1ea2453392d2b2e917152aeb670aad7005868c81d8`
  - body_path: `sources/http_captures/bangladesh-bank-fepd-virtual-assets-prohibition-2022-09/primary/www.bb.org.bd__mediaroom-circulars-fepd-sep152022fepd24e.pdf__a437219e06.bin`
  > FE Circular No. 24 is the direct legal anchor for the observed_change.
> It states that virtual-asset / virtual-currency obtaining
> transactions in/from/to Bangladesh and facilitation of their
> exchange/transfer/trading are not permitted by Bangladesh Bank and
> identifies FERA contravention consequences. attribution=direct because
> the regulator's own circular names the restricted activity class and
> addressees.
- **`primary_government`**
  - URL: <https://www.bb.org.bd/pub/annual/bfiu/bfiu_2021-2022.pdf>
  - body_hash: `sha256:c46b2f47c8c2fe0bdad07cc1ab35a7039915762c2f2d9886557d929a45299e7f`
  - body_path: `sources/http_captures/bangladesh-bank-fepd-virtual-assets-prohibition-2022-09/primary/www.bb.org.bd__pub-annual-bfiu-bfiu_2021-2022.pdf__5f0c377ee2.bin`
  > BFIU Annual Report 2021-22 corroborates the circular, repeats the
> prohibition framing, and provides official AML/FIU context for
> reporting and enforcement activity around virtual-currency and online
> forex trading. It does not add a distinct platform shutdown or
> on-chain action.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`bangladesh-bb-bitcoin-warning-2014`](./bangladesh-bb-bitcoin-warning-2014.md)
- [`vietnam-sbv-payment-prohibition-2017-10`](./vietnam-sbv-payment-prohibition-2017-10.md)
- [`pakistan-sbp-crypto-prohibition-2018-04`](./pakistan-sbp-crypto-prohibition-2018-04.md)
- [`turkey-cbrt-crypto-ban-2021`](./turkey-cbrt-crypto-ban-2021.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `ee7bf1a`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

