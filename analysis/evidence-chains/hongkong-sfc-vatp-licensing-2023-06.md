# Evidence chain — `hongkong-sfc-vatp-licensing-2023-06`

**Status**: `admitted` · **Stratum**: `S4_nation_state` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-02` · **Source commit**: `60f1d90` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-21` · **Tool version**: `0.1.0` · **Generated**: `2026-06-02T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> *(no scoped_claim recorded — event not paper-ready)*

## 1. Trigger

- **Type**: `nation_state_block`
- **Actor**: `HK_SFC`
- **Timestamp**: `2023-06-01 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://www.sfc.hk/-/media/EN/files/ER/PDF/23CP2_Consultation-Conclusions-on-VATP_eng.pdf>
  - Wayback: <https://web.archive.org/web/2023/https://www.sfc.hk/-/media/EN/files/ER/PDF/23CP2_Consultation-Conclusions-on-VATP_eng.pdf>
  > Hong Kong Securities and Futures Commission (SFC) "Consultation
> Conclusions on the Proposed Regulatory Requirements for Virtual
> Asset Trading Platform Operators Licensed by the SFC" published
> 2023-05-23, with the VATP licensing regime coming into force
> 2023-06-01. All centralised VATPs carrying on business in Hong
> Kong or actively marketing to HK investors must be licensed by
> the SFC. Existing platforms with "meaningful and substantial
> presence" in HK prior to 2023-06-01 had until 2024-05-31 to
> apply for a licence or wind down operations.
- **`supporting_journalism`**
  - URL: <https://www.davispolk.com/insights/client-update/hong-kong-licensing-regime-virtual-asset-trading-platforms-comes-force>
  - Wayback: <https://web.archive.org/web/2023/https://www.davispolk.com/insights/client-update/hong-kong-licensing-regime-virtual-asset-trading-platforms-comes-force>
  > Davis Polk client update "Hong Kong licensing regime for virtual
> asset trading platforms comes into force" describing the
> 2023-06-01 effective date and the dual-licensing framework
> (SFC Type 1 / Type 7 plus AMLO VATP licence).

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Hong Kong SFC VATP licensing regime
- **Canonical domains**: `binance.com`, `www.okx.com`, `bybit.com`, `hashkey.com`, `osl.com`

> Subset enumeration: named major offshore CEXs (Binance, OKX, Bybit,
> HTX/Huobi) that were effectively excluded by the VATP regime's
> mainland-China-residents bar and other requirements, plus the two
> SFC-licensed VATPs (HashKey, OSL) that were authorized at the
> transition. Full universe of HK-marketing VATPs is broader; this
> subset is the defensible analytic slice.

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `direct` · Δt = 0h

**Event label**: `vatp_licensing_regime_in_force_hashkey_osl_authorized`

**Timestamp**: `2023-06-01 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_legal`**
  - URL: <https://www.sfc.hk/en/Regulatory-functions/Intermediaries/Licensing/Virtual-asset-trading-platforms-operators>
  - Wayback: <https://web.archive.org/web/2023/https://www.sfc.hk/en/Regulatory-functions/Intermediaries/Licensing/Virtual-asset-trading-platforms-operators>
  > SFC public landing page for the VATP licensing regime, listing
> licensed VATP operators (HashKey, OSL) authorized at the
> 2023-06-01 effective date. Sources contextual_unarchived in
> this draft.
- **`primary_government`**
  - URL: <https://www.ifec.org.hk/web/en/financial-products/fintech/ico-bitcoin/new-vatp-regime.page>
  - Wayback: <https://web.archive.org/web/20231119135320/https://www.ifec.org.hk/web/en/financial-products/fintech/ico-bitcoin/new-vatp-regime.page>
  - body_hash: `sha256:96e7da0e040e51a454b4eb57abab5cf35580ace925c88384d7238902f754a22f`
  - body_path: `sources/http_captures/hongkong-sfc-vatp-licensing-2023-06/primary/web.archive.org__web-20231119135320-https-www.ifec.org.hk-web-en-financial-products-fintech-ico-bitcoin-new-vatp-regime.page__e418ac1162.html`
  > IFEC (HK Investor and Financial Education Council, SFC-affiliated)
> page on the new VATP regime commencing 2023-06-01. Primary
> government anchor. Wayback memento 20231119135320 captured 2026-05-21.
- **`semi_primary_wayback`**
  - URL: <https://www.davispolk.com/insights/client-update/hong-kong-licensing-regime-virtual-asset-trading-platforms-comes-force>
  - Wayback: <https://web.archive.org/web/20230921190548/https://www.davispolk.com/insights/client-update/hong-kong-licensing-regime-virtual-asset-trading-platforms-comes-force>
  - body_hash: `sha256:d4f6a70def3037c543d77a39af0997dbd0fea3c3f259e7bf3db5b2fc2ce7bbe0`
  - body_path: `sources/http_captures/hongkong-sfc-vatp-licensing-2023-06/primary/web.archive.org__web-20230921190548-https-www.davispolk.com-insights-client-update-hong-kong-licensing-regime-virtual-asset-trading-platforms-comes-force__c4768876b5.html`
  > Davis Polk client update on the VATP licensing regime entering
> force. Independent semi-primary anchor.

### offramp_cex · attribution: `plausible` · Δt = Noneh

**Event label**: `offshore_platforms_excluded_or_withdrew_applications`

**Timestamp**: `?` (precision: `day`)

**Sources**:

- **`semi_primary_wayback`**
  - URL: <https://www.scmp.com/tech/policy/article/3250996/sfc-reminds-crypto-investors-be-wary-unlicensed-platforms-final-month-apply-under-hong-kong-scheme>
  - Wayback: <https://web.archive.org/web/20240205111144/https://www.scmp.com/tech/policy/article/3250996/sfc-reminds-crypto-investors-be-wary-unlicensed-platforms-final-month-apply-under-hong-kong-scheme>
  - body_hash: `sha256:36418382445551270ee9e18f52c9dd56442d2eda7f9be52295d07814a4356b6b`
  - body_path: `sources/http_captures/hongkong-sfc-vatp-licensing-2023-06/primary/web.archive.org__web-20240205111144-https-www.scmp.com-tech-policy-article-3250996-sfc-reminds-crypto-investors-be-wary-unlicensed-platforms-final-month-apply-under-hon__ef9e45a855.html`
  > SCMP reporting on the final month for unlicensed platforms
> to apply under the SFC VATP scheme; documents the exclusion /
> withdrawal pattern. Wayback memento 20240205111144.
- **`semi_primary_wayback`**
  - URL: <https://cointelegraph.com/news/hong-kong-crypto-exchanges-license-scrutiny>
  - Wayback: <https://web.archive.org/web/20240822141337/https://cointelegraph.com/news/hong-kong-crypto-exchanges-license-scrutiny>
  - body_hash: `sha256:423f7ed91e40a619a4ea831391ba1ef23b5d1974b594b53ba94cbf61d8267528`
  - body_path: `sources/http_captures/hongkong-sfc-vatp-licensing-2023-06/primary/web.archive.org__web-20240822141337-https-cointelegraph.com-news-hong-kong-crypto-exchanges-license-scrutiny__744820c7f3.html`
  > Cointelegraph reporting on HK targeting non-compliant crypto
> exchanges in the licensing push and the withdrawals by
> mainland-China-linked exchanges.

## 5. Honest coverage gaps

- **l4_frontend** (`not_measured`): Unlicensed offshore platforms (Binance, OKX, Bybit, HTX) responded

## 7. Related events

- [`china-pboc-crypto-ban-2021`](./china-pboc-crypto-ban-2021.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `60f1d90`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

