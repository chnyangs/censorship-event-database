# Evidence chain — `indonesia-bi-payment-instrument-prohibition-2018-01`

**Status**: `admitted` · **Stratum**: `S4_nation_state` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-02` · **Source commit**: `a7b40fe` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-31` · **Tool version**: `0.1.0` · **Generated**: `2026-06-02T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "Bank Indonesia's 2018-01-13 press release barred Indonesian payment-system and fintech
> operators from processing virtual-currency transactions (and declared crypto a non-legitimate
> payment instrument). Coded as a nation-state off-ramp / payment-rail prohibition at class
> level; primary source is the BI press release."

## 1. Trigger

- **Type**: `nation_state_block`
- **Actor**: `ID_BI`
- **Timestamp**: `2018-01-13 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_government`**
  - URL: <https://www.bi.go.id/id/ruang-media/siaran-pers/Pages/sp_200418.aspx>
  - Wayback: <https://web.archive.org/web/20180315015913/https://www.bi.go.id/id/ruang-media/siaran-pers/Pages/sp_200418.aspx>
  - body_hash: `sha256:2c820cf8d63cd7633b7a94595943adfa4083180af5097dc5042889f6551251bf`
  - body_path: `sources/http_captures/indonesia-bi-payment-instrument-prohibition-2018-01/bi-press-release/web.archive.org__web-20180120000000-https-www.bi.go.id-id-ruang-media-siaran-pers-Pages-sp_200418.aspx__71db8c61ed.html`
  > Bank Indonesia press release No. 20/4/Dkom dated 2018-01-13 ("Bank Indonesia
> Memperingatkan Kepada Seluruh Pihak Agar Tidak Menjual, Membeli atau Memperdagangkan
> Virtual Currency"). The release affirms virtual currency including bitcoin is not a
> legitimate payment instrument under Law No. 7/2011 on Currency, AND — as the payment-
> system authority — PROHIBITS all payment-system service providers (penyelenggara jasa
> sistem pembayaran) and Financial Technology providers in Indonesia, both bank and non-
> bank, from processing transactions with virtual currency (citing PBI No. 18/40/PBI/2016
> and PBI No. 19/12/PBI/2017). Date "13 Januari 2018" and the processing prohibition
> language verified by full-text capture.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Indonesian PJSP / fintech payment operators (class)

> Indonesian payment-system service providers (PJSP) and financial-technology operators
> (bank and non-bank) as a class, barred from processing virtual-currency transactions;
> and the Indonesian public, for whom crypto is declared a non-legitimate payment
> instrument. No specific operator is named in the release. Coded subset at entity-class
> level.

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `direct` · Δt = 0h

**Event label**: `payment_operators_barred_from_processing_virtual_currency_transactions`

**Timestamp**: `2018-01-13 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_government`**
  - URL: <https://www.bi.go.id/id/ruang-media/siaran-pers/Pages/sp_200418.aspx>
  - Wayback: <https://web.archive.org/web/20180315015913/https://www.bi.go.id/id/ruang-media/siaran-pers/Pages/sp_200418.aspx>
  - body_hash: `sha256:2c820cf8d63cd7633b7a94595943adfa4083180af5097dc5042889f6551251bf`
  - body_path: `sources/http_captures/indonesia-bi-payment-instrument-prohibition-2018-01/bi-press-release/web.archive.org__web-20180120000000-https-www.bi.go.id-id-ruang-media-siaran-pers-Pages-sp_200418.aspx__71db8c61ed.html`
  > attribution=direct: Bank Indonesia (the named actor) publicly issues the
> prohibition in its own press release and names the target class (PJSP / fintech
> payment operators) barred from processing virtual-currency transactions. The BI
> release IS the regulatory action. Per codebook §1 the actor's own instrument
> citing the restriction satisfies direct attribution.
- **`supporting_journalism`**
  - URL: <https://www.coindesk.com/markets/2018/01/15/indonesia-central-bank-cryptocurrency-payments-not-legitimate>
  - Wayback: <https://web.archive.org/web/20210917105712/https://www.coindesk.com/markets/2018/01/15/indonesia-central-bank-cryptocurrency-payments-not-legitimate/>
  - body_hash: `sha256:ba12f6f3f0126796bae7064c487431a3816be99df62ddb67691877dfb21c6e3a`
  - body_path: `sources/http_captures/indonesia-bi-payment-instrument-prohibition-2018-01/primary/web.archive.org__web-20180115000000-https-www.coindesk.com-markets-2018-01-15-indonesia-central-bank-cryptocurrency-payments-not-legitimate__524874f33c.html`
  > CoinDesk 2018-01-15 contemporaneous report corroborating the BI 2018-01-13
> announcement: crypto declared not a legitimate payment instrument and payment
> operators barred from processing virtual-currency transactions.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`indonesia-bi-bitcoin-warning-2014`](./indonesia-bi-bitcoin-warning-2014.md)
- [`indonesia-bappebti-illegal-exchange-block-2023`](./indonesia-bappebti-illegal-exchange-block-2023.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `a7b40fe`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

