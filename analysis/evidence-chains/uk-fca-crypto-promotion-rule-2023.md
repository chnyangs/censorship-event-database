# Evidence chain — `uk-fca-crypto-promotion-rule-2023`

**Status**: `admitted` · **Stratum**: `S4_nation_state` · **Shape**: `comparison` (2 changed layer(s): `l4_frontend`, `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `80b0ca3` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-21` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "The UK FCA's Financial Promotions Regime for cryptoassets
> (Policy Statement PS23/6 + Finalised Guidance FG23/3), effective
> 2023-10-08, required all cryptoasset firms (UK-domiciled and
> overseas) marketing to UK consumers to communicate financial
> promotions via one of four legal routes under FSMA section 21.
> Within the compliance window, Bybit and KuCoin announced UK
> retail-customer restrictions / exits explicitly citing the
> regime; load-bearing observational axis is offramp_cex (Bybit and
> KuCoin UK retail restrictions, attribution=direct), with
> secondary l4_frontend UK-geo banners (attribution=plausible)."

## 1. Trigger

- **Type**: `regulatory_enforcement`
- **Actor**: `UK_FCA`
- **Timestamp**: `2023-10-08 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://www.fca.org.uk/publications/policy-statements/ps23-6-financial-promotion-rules-cryptoassets>
  - Wayback: <https://web.archive.org/web/20230608081306/https://www.fca.org.uk/publications/policy-statements/ps23-6-financial-promotion-rules-cryptoassets>
  - body_hash: `sha256:c60f0383d9bcb946d76c4432feac40de420a9b89cc28990fcc24acc4adb1372c`
  - body_path: `sources/http_captures/uk-fca-crypto-promotion-rule-2023/primary/web.archive.org__web-20230608081306-https-www.fca.org.uk-publications-policy-statements-ps23-6-financial-promotion-rules-cryptoassets__b03d205172.html`
  > **NEW EVENT AUTHORED — DRYRUN 2026-05-17** (Phase E S4 non-US
> regulator administrative-enforcement discovery): authored by
> LLM agent without personally verifying Wayback/body_hash;
> origin=agent_draft and status=draft pending human review.
> 
> UK Financial Conduct Authority Policy Statement PS23/6
> "Financial promotion rules for cryptoassets". The rules
> brought qualifying cryptoasset promotions made to UK
> consumers within the FCA's financial-promotions remit
> effective 2023-10-08. All cryptoasset firms marketing to UK
> consumers (including overseas firms) must comply via one of
> four legal routes; non-compliant promotions are a criminal
> offence under FSMA section 21. The regime is administrative
> enforcement, not a network-level or payment-rail block.
> DRYRUN: Wayback anchor unverified.
- **`primary_legal`**
  - URL: <https://www.fca.org.uk/firms/cryptoassets/marketing-uk-consumers>
  - Wayback: <https://web.archive.org/web/2023/https://www.fca.org.uk/firms/cryptoassets/marketing-uk-consumers>
  > FCA firms-guidance page "Cryptoasset firms marketing to UK
> consumers" enumerating the four legal communication routes
> and the 2023-10-08 effective date. DRYRUN: Wayback anchor
> unverified.
- **`primary_legal`**
  - URL: <https://www.fca.org.uk/publications/finalised-guidance/fg23-3-cryptoasset-financial-promotions>
  - Wayback: <https://web.archive.org/web/2023/https://www.fca.org.uk/publications/finalised-guidance/fg23-3-cryptoasset-financial-promotions>
  > FCA Finalised Guidance FG23/3 on cryptoasset financial
> promotions, the non-handbook guidance published alongside
> PS23/6. DRYRUN: Wayback anchor unverified.
- **`primary_legal`**
  - URL: <https://www.fca.org.uk/news/press-releases/fca-sets-expectations-ahead-incoming-crypto-marketing-rules>
  - Wayback: <https://web.archive.org/web/20230907160645/https://www.fca.org.uk/news/press-releases/fca-sets-expectations-ahead-incoming-crypto-marketing-rules>
  - body_hash: `sha256:05c1ac5fdc5393fdab7c73bf932fa74588426557908ac46a3a904657a6d4fcfb`
  - body_path: `sources/http_captures/uk-fca-crypto-promotion-rule-2023/primary/web.archive.org__web-20230907160645-https-www.fca.org.uk-news-press-releases-fca-sets-expectations-ahead-incoming-crypto-marketing-rules__4e866f9a79.html`
  > FCA press release setting expectations ahead of the
> 2023-10-08 effective date, anchoring the regulator's public
> framing of the regime. DRYRUN: Wayback anchor unverified.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Cryptoasset firms marketing to UK consumers (class)
- **Canonical domains**: `bybit.com`, `kucoin.com`

> Class-level target: all cryptoasset firms (UK-domiciled and
> overseas) communicating financial promotions of qualifying
> cryptoassets to UK consumers. Non-exhaustive enumerated subset
> of observed compliance reactions: Bybit and KuCoin announced
> UK retail restrictions / exits in the days surrounding the
> 2023-10-08 effective date; additional firms (PayPal UK crypto,
> Luno UK, Binance UK retail, others) layered partial
> compliance changes through Q4 2023. Per codebook §7 the
> target is coded `subset` and the class-level rationale is
> documented here.

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `plausible` · Δt = 0h

**Event label**: `bybit_restricted_uk_retail_customers_in_response_to_fca_financial_promotions_regime`

**Timestamp**: `2023-10-08 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_legal`**
  - URL: <https://www.fca.org.uk/news/press-releases/fca-sets-expectations-ahead-incoming-crypto-marketing-rules>
  - Wayback: <https://web.archive.org/web/20230907160645/https://www.fca.org.uk/news/press-releases/fca-sets-expectations-ahead-incoming-crypto-marketing-rules>
  - body_hash: `sha256:05c1ac5fdc5393fdab7c73bf932fa74588426557908ac46a3a904657a6d4fcfb`
  - body_path: `sources/http_captures/uk-fca-crypto-promotion-rule-2023/primary/web.archive.org__web-20230907160645-https-www.fca.org.uk-news-press-releases-fca-sets-expectations-ahead-incoming-crypto-marketing-rules__4e866f9a79.html`
  > FCA press release on the incoming crypto financial-promotions
> regime (effective 2023-10-08) — primary anchor for the
> provider-side UK retail restriction cascade.
- **`primary_corporate`**
  - URL: <https://announcements.bybit.com/en-US/article/important-notice-for-bybit-users-in-the-uk-blt8d6c3a98f0db4f4b/>
  - Wayback: <https://web.archive.org/web/2023/https://announcements.bybit.com/en-US/article/important-notice-for-bybit-users-in-the-uk-blt8d6c3a98f0db4f4b/>
  > Bybit operator announcement to UK users notifying that
> Bybit would suspend new account creation and progressively
> restrict UK retail services to comply with the FCA
> financial-promotions regime effective 2023-10-08.
> attribution=direct under §1.4 (provider publicly cites
> the trigger; block within publicly-knowable compliance
> window). DRYRUN: Wayback anchor unverified.
- **`supporting_journalism`**
  - URL: <https://www.reuters.com/technology/crypto-exchange-bybit-suspend-services-britain-2023-10-02/>
  - Wayback: <https://web.archive.org/web/2023/https://www.reuters.com/technology/crypto-exchange-bybit-suspend-services-britain-2023-10-02/>
  > Reuters contemporaneous coverage of Bybit suspending UK
> services citing the incoming FCA financial-promotions
> rules. DRYRUN: Wayback anchor unverified.

### offramp_cex · attribution: `plausible` · Δt = 0h

**Event label**: `kucoin_restricted_uk_retail_customers_in_response_to_fca_financial_promotions_regime`

**Timestamp**: `2023-10-08 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_legal`**
  - URL: <https://www.fca.org.uk/news/press-releases/fca-sets-expectations-ahead-incoming-crypto-marketing-rules>
  - Wayback: <https://web.archive.org/web/20230907160645/https://www.fca.org.uk/news/press-releases/fca-sets-expectations-ahead-incoming-crypto-marketing-rules>
  - body_hash: `sha256:05c1ac5fdc5393fdab7c73bf932fa74588426557908ac46a3a904657a6d4fcfb`
  - body_path: `sources/http_captures/uk-fca-crypto-promotion-rule-2023/primary/web.archive.org__web-20230907160645-https-www.fca.org.uk-news-press-releases-fca-sets-expectations-ahead-incoming-crypto-marketing-rules__4e866f9a79.html`
  > FCA press release on the incoming crypto financial-promotions
> regime (effective 2023-10-08) — primary anchor for the
> provider-side UK retail restriction cascade.
- **`primary_corporate`**
  - URL: <https://www.kucoin.com/news/en-important-notice-for-our-uk-users>
  - Wayback: <https://web.archive.org/web/2023/https://www.kucoin.com/news/en-important-notice-for-our-uk-users>
  > KuCoin operator announcement to UK users notifying that
> KuCoin would restrict UK retail services in line with the
> FCA financial-promotions regime effective 2023-10-08.
> attribution=direct under §1.4. DRYRUN: Wayback anchor
> unverified.
- **`supporting_journalism`**
  - URL: <https://www.coindesk.com/policy/2023/10/06/kucoin-tells-uk-users-to-close-positions-amid-new-fca-rules/>
  - Wayback: <https://web.archive.org/web/2023/https://www.coindesk.com/policy/2023/10/06/kucoin-tells-uk-users-to-close-positions-amid-new-fca-rules/>
  > CoinDesk coverage of KuCoin instructing UK users to close
> positions ahead of the FCA financial-promotions effective
> date. DRYRUN: Wayback anchor unverified.

### l4_frontend · attribution: `plausible` · Δt = 0h

**Event label**: `uk_geo_frontend_banners_and_kyc_restrictions_added_on_bybit_and_kucoin_uk_vantage`

**Timestamp**: `2023-10-08 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_legal`**
  - URL: <https://www.fca.org.uk/news/press-releases/fca-sets-expectations-ahead-incoming-crypto-marketing-rules>
  - Wayback: <https://web.archive.org/web/20230907160645/https://www.fca.org.uk/news/press-releases/fca-sets-expectations-ahead-incoming-crypto-marketing-rules>
  - body_hash: `sha256:05c1ac5fdc5393fdab7c73bf932fa74588426557908ac46a3a904657a6d4fcfb`
  - body_path: `sources/http_captures/uk-fca-crypto-promotion-rule-2023/primary/web.archive.org__web-20230907160645-https-www.fca.org.uk-news-press-releases-fca-sets-expectations-ahead-incoming-crypto-marketing-rules__4e866f9a79.html`
  > FCA press release on the incoming crypto financial-promotions
> regime (effective 2023-10-08) — primary anchor for the
> provider-side UK retail restriction cascade.
- **`primary_corporate`**
  - URL: <https://announcements.bybit.com/en-US/article/important-notice-for-bybit-users-in-the-uk-blt8d6c3a98f0db4f4b/>
  - Wayback: <https://web.archive.org/web/2023/https://announcements.bybit.com/en-US/article/important-notice-for-bybit-users-in-the-uk-blt8d6c3a98f0db4f4b/>
  > Frontend-layer UK-vantage restriction banners on bybit.com
> and parallel KuCoin frontend banners were posted in the
> compliance window. attribution=plausible under §1.4: the
> per-domain frontend-banner timing is operator-driven and
> not independently anchored to a per-domain regulator
> notice; the offramp_cex announcements (above) carry the
> direct-attribution weight. DRYRUN: Wayback anchor
> unverified.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`uk-fca-binance-markets-2021`](./uk-fca-binance-markets-2021.md)
- [`kraken-uk-derivatives-exit-2021`](./kraken-uk-derivatives-exit-2021.md)
- [`pump-fun-uk-fca-geofence-2024-12`](./pump-fun-uk-fca-geofence-2024-12.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `80b0ca3`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

