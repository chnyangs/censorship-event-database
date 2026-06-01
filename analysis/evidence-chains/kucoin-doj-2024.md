# Evidence chain — `kucoin-doj-2024`

**Status**: `admitted` · **Stratum**: `S3_doj_sec_cftc_fiod` · **Shape**: `comparison` (2 changed layer(s): `l4_frontend`, `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-02` · **Source commit**: `3f1a9f2` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-16` · **Tool version**: `0.1.0` · **Generated**: `2026-06-02T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "The 2024-03-26 DOJ SDNY indictment + CFTC consent order against KuCoin
> and its founders produced a 2-layer cascade in the dataset: an L4
> customer-facing US-off-boarding announcement on kucoin.com and an
> offramp_cex shutdown of US-resident services tied to a $300M CFTC
> penalty and full US market exit. Structurally narrower than the
> 4-framework Binance settlement and broader than the Kraken staking-only
> service shutdown."

## 1. Trigger

- **Type**: `doj_indictment`
- **Actor**: `US_DOJ_SDNY_CFTC`
- **Timestamp**: `2024-03-26 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://www.justice.gov/usao-sdny/pr/founders-and-executives-global-cryptocurrency-exchange-charged-bank-secrecy-act-and>
  - Wayback: <https://web.archive.org/web/20260516000000/https://www.justice.gov/usao-sdny/pr/founders-and-executives-global-cryptocurrency-exchange-charged-bank-secrecy-act-and>
  > DOJ SDNY press release (2024-03-26): "Founders And Executives Of Global
> Cryptocurrency Exchange Charged With Bank Secrecy Act And Unlicensed
> Money Transmission Offenses." Indictments against KuCoin (operated by
> Peken Global Limited / Mek Global Limited) and founders Chun Gan and
> Ke Tang; charges include conspiracy to operate an unlicensed money
> transmitting business and Bank Secrecy Act violations. SDNY action
> coordinates with concurrent CFTC civil enforcement.
- **`primary_legal`**
  - URL: <https://www.cftc.gov/PressRoom/PressReleases/8866-24>
  - Wayback: <https://web.archive.org/web/20260516000000/https://www.cftc.gov/PressRoom/PressReleases/8866-24>
  > CFTC press release 8866-24 (2024-03-26): "CFTC Charges KuCoin with
> Multiple Violations of the Commodity Exchange Act." Civil action
> alleging illegal operation of a digital asset derivatives trading
> platform without registration; ultimately resolved via a consent
> order with a $300M penalty. Companion to the SDNY criminal
> indictment.
- **`primary_legal`**
  - URL: <https://www.fincen.gov/news/news-releases>
  > Concurrent FinCEN engagement on BSA / AML-program / registration
> failures referenced in the SDNY indictment. Pinned here as context;
> no archived FinCEN-specific consent-order page is retained for this
> DRYRUN row.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: KuCoin (Peken Global / Mek Global) + Chun Gan + Ke Tang
- **Canonical domains**: `kucoin.com`

> KuCoin exchange (operated by Peken Global Limited and Mek Global Limited)
> and founders Chun Gan and Ke Tang as named defendants in the SDNY
> indictment. Civil CFTC action targets the KuCoin platform entities for
> unregistered derivatives offerings. Canonical exchange domain kucoin.com
> remained globally operational post-settlement, but US-resident accounts
> were placed in restricted (read-only / withdraw-only) mode.

## 3. Changed-layer observations (supports the scoped claim)

### l4_frontend · attribution: `direct` · Δt = 0h

**Event label**: `kucoin_us_user_offboarding_announcement`

**Timestamp**: `2024-03-26 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_corporate`**
  - URL: <https://www.kucoin.com/news>
  - Wayback: <https://web.archive.org/web/20260516000000/https://www.kucoin.com/news>
  > KuCoin's official news / announcement page hosted the customer-facing
> notice of US-resident off-boarding citing the DOJ + CFTC enforcement
> actions. The announcement informed US residents that their accounts
> would transition to read-only / withdraw-only mode pending resolution.
> attribution=direct because the announcement explicitly references
> the 2024-03-26 DOJ + CFTC actions as the precipitating cause.
- **`primary_legal`**
  - URL: <https://www.justice.gov/usao-sdny/pr/founders-and-executives-global-cryptocurrency-exchange-charged-bank-secrecy-act-and>
  - Wayback: <https://web.archive.org/web/20260516000000/https://www.justice.gov/usao-sdny/pr/founders-and-executives-global-cryptocurrency-exchange-charged-bank-secrecy-act-and>
  > DOJ SDNY indictment names KuCoin's failure to register with FinCEN
> and to maintain an effective AML program, providing the causal
> anchor for the same-day US-user-facing frontend notice.

### offramp_cex · attribution: `direct` · Δt = 0h

**Event label**: `kucoin_exits_us_market_with_300m_cftc_settlement`

**Timestamp**: `2024-03-26 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_legal`**
  - URL: <https://www.cftc.gov/PressRoom/PressReleases/8866-24>
  - Wayback: <https://web.archive.org/web/20260516000000/https://www.cftc.gov/PressRoom/PressReleases/8866-24>
  > CFTC press release describes the platform-level enforcement: KuCoin
> operated as an unregistered futures commission merchant / swap
> execution facility / designated contract market. The eventual
> consent order required KuCoin to pay $300M and exit the US market —
> structural off-ramp shutdown for US residents. attribution=direct
> because the CFTC order is the legal instrument compelling US market
> exit.
- **`primary_legal`**
  - URL: <https://www.justice.gov/usao-sdny/pr/founders-and-executives-global-cryptocurrency-exchange-charged-bank-secrecy-act-and>
  - Wayback: <https://web.archive.org/web/20260516000000/https://www.justice.gov/usao-sdny/pr/founders-and-executives-global-cryptocurrency-exchange-charged-bank-secrecy-act-and>
  > DOJ SDNY indictment + concurrent CFTC civil action together drove
> KuCoin's agreement to discontinue serving US residents. Founder
> indictments (Chun Gan, Ke Tang) constrain corporate willingness to
> continue US operations.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`binance-4framework-2023`](./binance-4framework-2023.md)
- [`bitzlato-doj-2023`](./bitzlato-doj-2023.md)
- [`kraken-sec-staking-2023`](./kraken-sec-staking-2023.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `3f1a9f2`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

