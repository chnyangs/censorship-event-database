# Evidence chain — `south-africa-fsca-crypto-financial-product-2022`

**Status**: `admitted` · **Stratum**: `S4_nation_state` · **Shape**: `null_event` (0 changed layer(s): none) · **Tier**: `null_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-02` · **Source commit**: `b6c6fae` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-21` · **Tool version**: `0.1.0` · **Generated**: `2026-06-02T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "FSCA Declaration 2022-10-19 (Government Notice 1350, Government
> Gazette 47334) declares crypto assets a financial product under
> the South African FAIS Act, bringing persons providing FAIS-defined
> advice and intermediary services in respect of crypto assets into
> the FSP licensing perimeter, with a transitional exemption pending
> licence-application disposition (window 2023-06-01 to 2023-11-30).
> As of the 2026-05-17 authoring date no class-level offramp_cex
> behavioral change at the ZA CASP cohort attributable specifically
> to the Declaration has been observed — coded null_event / null_case
> as a S4_nation_state denominator control on the African-continent
> axis, sibling to MiCA (eu-mica-2023) and a downstream national-
> implementation companion to FATF R.15 (fatf-r15-vasp-travel-rule-
> 2019)."

## 1. Trigger

- **Type**: `regulatory_enforcement`
- **Actor**: `ZA_FSCA`
- **Timestamp**: `2022-10-19 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://www.fsca.co.za/News%20Documents/FSCA%20Press%20Release_Declaration%20of%20Crypto%20Assets%20As%20A%20Financial%20Product_20%20October%202022.pdf>
  - Wayback: <https://web.archive.org/web/20221020111559id_/https://www.fsca.co.za/News%20Documents/FSCA%20Press%20Release_Declaration%20of%20Crypto%20Assets%20As%20A%20Financial%20Product_20%20October%202022.pdf>
  - body_hash: `sha256:0f579222fa6be388b44e5da80e9db25d9e0355ad30fd0413220acaa9a5bb4a16`
  - body_path: `sources/http_captures/south-africa-fsca-crypto-financial-product-2022/primary/web.archive.org__web-20221020111559id_-https-www.fsca.co.za-News-20Documents-FSCA-20Press-20Release_Declaration-20of-20Crypto-20Assets-20As-20A-20Financial-20Product_20__5f7f2aad27.bin`
  > Financial Sector Conduct Authority (FSCA, South Africa) press
> release dated 2022-10-20 announcing the declaration of crypto
> assets as a financial product under the Financial Advisory and
> Intermediary Services Act, 37 of 2002 (FAIS Act). The Declaration
> itself was issued by the FSCA on 2022-10-19 and published as
> Government Notice 1350 in Government Gazette 47334 (2022-10-19).
> The Declaration brings persons providing financial services
> ("advice" and / or "intermediary services" under FAIS) in respect
> of crypto assets into the FAIS licensing perimeter, requiring
> such persons to be authorised as Financial Services Providers
> (FSPs). Crypto assets are defined as a digital representation of
> value that is not issued by a central bank, but is capable of
> being traded, transferred or stored electronically by natural and
> legal persons for the purpose of payment, investment and other
> forms of utility. A general transitional exemption from
> section 7(1) of the FAIS Act applies until licence applications
> are approved or declined; the licence application window ran
> 2023-06-01 to 2023-11-30. DRYRUN contextual_unarchived stub;
> replace with verified Wayback + body_hash / body_path capture of
> the FSCA PDF during real human audit.
- **`semi_primary_wayback`**
  - URL: <https://www.cliffedekkerhofmeyr.com/en/news/publications/2022/Practice/Finance/finance-and-banking-alert-20-october-2022-fsca-declares-crypto-assets-as-a-financial-product-.html>
  - Wayback: <https://web.archive.org/web/20221020162123/https://www.cliffedekkerhofmeyr.com/en/news/publications/2022/Practice/Finance/finance-and-banking-alert-20-october-2022-fsca-declares-crypto-assets-as-a-financial-product-.html>
  - body_hash: `sha256:94f1ed48eca9ff3f8965ce073354af5c45d109adbe830b19f6693266e884bdac`
  - body_path: `sources/http_captures/south-africa-fsca-crypto-financial-product-2022/primary/web.archive.org__web-20221020162123-https-www.cliffedekkerhofmeyr.com-en-news-publications-2022-Practice-Finance-finance-and-banking-alert-20-october-2022-fsca-declares__2d5d94e2e1.html`
  > Cliffe Dekker Hofmeyr Finance and Banking Alert (2022-10-20)
> analysing the FSCA Declaration. Documents the Government Notice
> 1350 / Government Gazette 47334 publication, the FAIS Act
> framing, and the transitional-exemption structure. Used as a
> secondary contextual anchor for the trigger date and scope.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: South-Africa-operating Crypto Asset Service Providers and FAIS advisers (FSCA-FAIS-regulated)

> All persons providing financial services (furnishing of "advice" and /
> or rendering of "intermediary services", each as defined in the FAIS
> Act) in relation to crypto assets to South African clients. Population
> substantively covers South-Africa-operating Crypto Asset Service
> Providers (CASPs) — including local exchanges (Luno, VALR, AltCoinTrader,
> Ovex), South-Africa-facing operations of global exchanges (Binance ZA,
> Coinbase ZA-facing, Kraken ZA-facing), brokers, and crypto-asset
> investment advisers — plus their key individuals and representatives.
> Class-level scope: licensing perimeter applies at the FSP / FAIS-
> licensee level rather than at any specific on-chain address set; per
> codebook §7 coded as `subset` (no `class_level` enumeration value).
> Self-custody and peer-to-peer activity outside the FAIS advice /
> intermediary perimeter is not directly captured.

## 3. Changed-layer observations (supports the scoped claim)

*No observed_change entries. This is a `null_event`; see §4 for observed_no_change evidence supporting the null claim.*

## 4. No-change observations (where applicable)

### offramp_cex — `fsca_crypto_financial_product_declaration_no_observed_casp_change_yet`

**Window**: `2022-10-19 00:00:00+00:00` → `2026-05-17 00:00:00+00:00`

**Sources**:

- **`primary_legal`**
  - URL: <https://www.fsca.co.za/News%20Documents/FSCA%20Press%20Release_Declaration%20of%20Crypto%20Assets%20As%20A%20Financial%20Product_20%20October%202022.pdf>
  - Wayback: <https://web.archive.org/web/20221020111559id_/https://www.fsca.co.za/News%20Documents/FSCA%20Press%20Release_Declaration%20of%20Crypto%20Assets%20As%20A%20Financial%20Product_20%20October%202022.pdf>
  - body_hash: `sha256:0f579222fa6be388b44e5da80e9db25d9e0355ad30fd0413220acaa9a5bb4a16`
  - body_path: `sources/http_captures/south-africa-fsca-crypto-financial-product-2022/primary/web.archive.org__web-20221020111559id_-https-www.fsca.co.za-News-20Documents-FSCA-20Press-20Release_Declaration-20of-20Crypto-20Assets-20As-20A-20Financial-20Product_20__5f7f2aad27.bin`
  > FSCA Declaration 2022-10-19 brings ZA-operating CASPs and FAIS
> advisers into the FAIS Act licensing perimeter. Effect is
> prospective: transitional exemption from FAIS s.7(1) applies
> until licence applications are approved or declined; the
> licence application window ran 2023-06-01 to 2023-11-30. As of
> the 2026-05-17 authoring date no class-level offramp_cex
> behavioral change at the ZA CASP cohort attributable
> specifically to the Declaration has been observed. attribution=
> none is required by schema (observed_no_change rows).
> observed_no_change reflects the null-event posture; revisit
> when the FSCA licensed-CASP register and any subsequent
> licence-refusal / enforcement actions surface.
- **`supporting_journalism`**
  - URL: <https://www.cliffedekkerhofmeyr.com/en/news/publications/2022/Practice/Finance/finance-and-banking-alert-20-october-2022-fsca-declares-crypto-assets-as-a-financial-product-.html>
  - Wayback: <https://web.archive.org/web/20221020162123/https://www.cliffedekkerhofmeyr.com/en/news/publications/2022/Practice/Finance/finance-and-banking-alert-20-october-2022-fsca-declares-crypto-assets-as-a-financial-product-.html>
  > Cliffe Dekker Hofmeyr alert anchors the Government Notice
> 1350 / Government Gazette 47334 publication and the FAIS-Act
> framing. Used here as a second contextual_unarchived pointer
> for the null-event posture; no observed CASP-level change to
> date.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`eu-mica-2023`](./eu-mica-2023.md)
- [`fatf-r15-vasp-travel-rule-2019`](./fatf-r15-vasp-travel-rule-2019.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `b6c6fae`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

