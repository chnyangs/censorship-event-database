# Evidence chain — `japan-fsa-stablecoin-psa-effective-2023-06`

**Status**: `admitted` · **Stratum**: `S4_nation_state` · **Shape**: `null_event` (0 changed layer(s): none) · **Tier**: `null_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `08595e8` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-16` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T09:49:53Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "Japan's 2023-06-01 commencement of the Payment Services Act
> Amendment Act established the Electronic Payment Instrument (EPI /
> 電子決済手段) regulatory regime for fiat-referenced stablecoins,
> restricting EPI issuance to JP-licensed banks, fund transfer
> service providers, and trust companies/banks, and requiring
> Electronic Payment Instrument Exchange Service Provider (EPIESP)
> registration for stablecoin intermediation. As the first major
> industrial-democracy stablecoin issuer regime to take legal effect,
> it predates EU MiCA stablecoin provisions (2024-06-30) and the
> HK HKMA Stablecoins Ordinance (2025-08-01). The row does not claim
> any specific 2023-06-01 issuer-side launch, JP-VASP stablecoin
> delisting cascade, on-chain asset-layer freeze, or frontend
> takedown; it documents the regulatory-framework trigger as a
> null_event pending downstream EPIESP-registration and EPI-issuer-
> licence events authored as separate rows."

## 1. Trigger

- **Type**: `regulatory_enforcement`
- **Actor**: `JP_FSA`
- **Timestamp**: `2023-06-01 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://www.fsa.go.jp/en/newsletter/weekly2023/540.html>
  - Wayback: <https://web.archive.org/web/20230608144659/https://www.fsa.go.jp/en/newsletter/weekly2023/540.html>
  - body_hash: `sha256:0d10b62ea6b24448602ee0707c59ef7494256cb83a277ded8eaa83d48740d7b0`
  - body_path: `sources/http_captures/japan-fsa-stablecoin-psa-effective-2023-06/primary/web.archive.org__web-20230608144659-https-www.fsa.go.jp-en-newsletter-weekly2023-540.html__1b6ee49783.html`
  > Japan Financial Services Agency (金融庁 / FSA) Weekly Review No.540
> (English edition), dated 2023-06-08, which covers the week of the
> 2023-06-01 commencement of the Amendment Act to the Payment
> Services Act (資金決済に関する法律 / Shikin Kessai ni Kansuru
> Hōritsu). The Amendment Bill was submitted to the Diet on
> 2022-03-04, enacted 2022-06-03, and commenced operation on
> 2023-06-01. It introduces the "electronic payment instrument"
> (電子決済手段 / EPI) category corresponding to fiat-referenced
> stablecoins, restricts EPI issuance to (a) licensed banks, (b)
> fund transfer service providers (資金移動業者), and (c) trust
> companies / trust banks (信託会社・信託銀行) in Japan, and
> introduces a separate Electronic Payment Instrument Exchange
> Service Provider (EPIESP / 電子決済手段等取引業者) registration
> regime for stablecoin intermediaries (buy/sell/custody/transfer).
> First major industrial-democracy stablecoin issuer regime
> globally. DRYRUN: Wayback pointer is a 2023-calendar-folder
> wildcard; pinned snapshot timestamp and body_hash capture for
> the specific FSA Weekly Review No.540 permalink, plus the FSA's
> Japanese-language press notice for the 2023-06-01 commencement,
> deferred to non-DRYRUN release.
- **`semi_primary_wayback`**
  - URL: <https://cryptoforinnovation.org/policy-brief-summary-of-japanese-fsa-crypto-asset-and-stablecoins-framework/>
  - Wayback: <https://web.archive.org/web/20230923150331/https://cryptoforinnovation.org/policy-brief-summary-of-japanese-fsa-crypto-asset-and-stablecoins-framework/>
  - body_hash: `sha256:287ba1d1b81f0f4ab6da0eb6a0115d119b90d4380e81476f16c6412696a459d6`
  - body_path: `sources/http_captures/japan-fsa-stablecoin-psa-effective-2023-06/primary/web.archive.org__web-20230923150331-https-cryptoforinnovation.org-policy-brief-summary-of-japanese-fsa-crypto-asset-and-stablecoins-framework__989a557b96.html`
  > Crypto Council for Innovation policy brief "Summary of Japanese
> FSA Crypto Asset and Stablecoins Framework" describing the
> 2023-06-01 commencement of the Payment Services Act Amendment
> Act and the EPI licensing regime. Companion explainer anchor
> documenting the three-issuer-class restriction (banks, fund
> transfer service providers, trust companies/banks), the EPIESP
> registration regime for intermediaries, and the foreign-
> stablecoin treatment (domestic EPIESPs may intermediate foreign-
> issued stablecoins subject to JP-side reserve-backing
> requirements). DRYRUN: wildcard Wayback pointer; pinned snapshot
> timestamp and body_hash deferred to human audit.
- **`supporting_journalism`**
  - URL: <https://news.bitcoin.com/japan-stablecoin-regulation-explained-psa-rules-jpy-coins-and-bank-issuers/>
  - Wayback: <https://web.archive.org/web/2023/https://news.bitcoin.com/japan-stablecoin-regulation-explained-psa-rules-jpy-coins-and-bank-issuers/>
  > Bitcoin.com News explainer "Japan Stablecoin Regulation Explained:
> PSA Rules, JPY Coins and Bank Issuers" covering the 2023-06-01
> EPI regime commencement and the three eligible-issuer classes.
> Secondary explainer anchor for the issuer-restriction framing.
> DRYRUN: wildcard Wayback pointer; pinned snapshot deferred.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: JP-jurisdiction stablecoin issuer + EPIESP intermediary ecosystem (FSA-licensed)

> Class-level subset enumeration: (a) all JP-jurisdiction stablecoin
> issuers, restricted under the PSA Amendment to licensed banks, fund
> transfer service providers (資金移動業者), and trust companies /
> trust banks (信託会社・信託銀行); and (b) all JP-resident-facing
> stablecoin intermediaries (buy/sell/custody/transfer operations),
> which must register as Electronic Payment Instrument Exchange
> Service Providers (EPIESP / 電子決済手段等取引業者). Foreign-issued
> stablecoins (e.g. USDT, USDC, DAI) are not directly issuer-licensed
> by JP but may only be intermediated to JP residents through a
> domestic EPIESP that holds a JP-side reserve equal to the
> intermediated stablecoin balance. Address-level enumeration is not
> applicable — this is sector-wide stablecoin issuance-and-intermediation
> licensing.

## 3. Changed-layer observations (supports the scoped claim)

*No observed_change entries. This is a `null_event`; see §4 for observed_no_change evidence supporting the null claim.*

## 4. No-change observations (where applicable)

### offramp_cex — `psa_amendment_act_epi_regime_commenced_no_immediate_listing_cascade`

**Window**: `2023-06-01 00:00:00+00:00` → `2023-12-31 23:59:59+00:00`

**Sources**:

- **`primary_legal`**
  - URL: <https://www.fsa.go.jp/en/newsletter/weekly2023/540.html>
  - Wayback: <https://web.archive.org/web/20230608144659/https://www.fsa.go.jp/en/newsletter/weekly2023/540.html>
  - body_hash: `sha256:0d10b62ea6b24448602ee0707c59ef7494256cb83a277ded8eaa83d48740d7b0`
  - body_path: `sources/http_captures/japan-fsa-stablecoin-psa-effective-2023-06/primary/web.archive.org__web-20230608144659-https-www.fsa.go.jp-en-newsletter-weekly2023-540.html__1b6ee49783.html`
  > PSA Amendment Act commences operation 2023-06-01. From this
> date, EPI issuance to JP residents is restricted to licensed
> banks, fund transfer service providers, and trust companies/
> banks; intermediation requires EPIESP registration.
> observation_kind=observed_no_change with attribution=none
> because the regime activation does not by itself produce a
> measurable JP-VASP stablecoin-listing delta in the
> 2023-06-01 → 2023-12 window — pre-existing JP exchanges
> were not listing USDT/USDC, so there is no observable
> delisting cascade, and no JP-issued EPI was launched at the
> commencement date. DRYRUN: Wayback wildcard pointer; pinned
> snapshot timestamp and body_hash for the specific FSA Weekly
> Review permalink and the FSA Japanese-language commencement
> notice deferred to human audit.
- **`supporting_journalism`**
  - URL: <https://cryptoforinnovation.org/policy-brief-summary-of-japanese-fsa-crypto-asset-and-stablecoins-framework/>
  - Wayback: <https://web.archive.org/web/2023/https://cryptoforinnovation.org/policy-brief-summary-of-japanese-fsa-crypto-asset-and-stablecoins-framework/>
  > Companion policy-brief anchor describing the regime's
> enabling-with-restrictions character: registered JP VASPs may
> intermediate foreign-issued stablecoins post-2023-06-01 under
> the EPIESP regime subject to JP-side reserve backing, rather
> than the regime imposing immediate delisting. Supports the
> observed_no_change coding for the 2023-06-01 → 2023-12 window.

## 5. Honest coverage gaps

- **asset_onchain** (`not_measured`): Stablecoin issuance licensing constrains who may legally issue an

## 7. Related events

- [`eu-mica-2023`](./eu-mica-2023.md)
- [`hongkong-hkma-stablecoins-ordinance-2025`](./hongkong-hkma-stablecoins-ordinance-2025.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `08595e8`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

