# Evidence chain — `russia-dfa-law-2020`

**Status**: `admitted` · **Stratum**: `S4_nation_state` · **Shape**: `null_event` (0 changed layer(s): none) · **Tier**: `null_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `3b37c3e` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-21` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> *(no scoped_claim recorded — event not paper-ready)*

## 1. Trigger

- **Type**: `regulatory_enforcement`
- **Actor**: `RU_FEDERAL_LAW`
- **Timestamp**: `2020-07-31 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`semi_primary_wayback`**
  - URL: <https://www.loc.gov/item/global-legal-monitor/2021-01-11/russian-federation-new-bill-defines-cryptocurrency-proposes-tax-regulations/>
  - Wayback: <https://web.archive.org/web/20210920180643/https://www.loc.gov/item/global-legal-monitor/2021-01-11/russian-federation-new-bill-defines-cryptocurrency-proposes-tax-regulations/>
  - body_hash: `sha256:2847c0f365eaa143a82c41587b75f315230dedf331f56abe3d3aac1c1ea6ae91`
  - body_path: `sources/http_captures/russia-dfa-law-2020/primary/web.archive.org__web-20210920180643-https-www.loc.gov-item-global-legal-monitor-2021-01-11-russian-federation-new-bill-defines-cryptocurrency-proposes-tax-regulations__642ebaba84.html`
  > US Library of Congress Global Legal Monitor entry summarizing
> Russian Federal Law No. 259-FZ "On Digital Financial Assets,
> Digital Currency, and Amendments to Certain Legislative Acts
> of the Russian Federation" signed by President Vladimir Putin
> on 2020-07-31 and effective 2021-01-01. The law defines
> "digital currency" (cryptocurrency) and "digital financial
> assets" (tokenized rights), legalizes their issuance and
> circulation under prescribed conditions, and prohibits the
> use of digital currency as a means of payment for goods,
> works, and services by Russian legal entities, Russian
> individual tax residents, and Russian branches of foreign
> organizations. Provisional Wayback anchor; specific snapshot
> timestamp requires human-audit re-pinning.
- **`semi_primary_wayback`**
  - URL: <https://www.crowdfundinsider.com/2020/08/164885-russia-federal-law-addresses-digital-assets-differentiates-between-digital-securities-and-digital-currencies/>
  - Wayback: <https://web.archive.org/web/20200805224916/https://www.crowdfundinsider.com/2020/08/164885-russia-federal-law-addresses-digital-assets-differentiates-between-digital-securities-and-digital-currencies/>
  - body_hash: `sha256:a533401ce7050a6fd60e799310ca69b893f242294196421b9141e392e3998dbc`
  - body_path: `sources/http_captures/russia-dfa-law-2020/primary/web.archive.org__web-20200805224916-https-www.crowdfundinsider.com-2020-08-164885-russia-federal-law-addresses-digital-assets-differentiates-between-digital-securities__0cc9abda05.html`
  > Crowdfund Insider 2020-08 coverage of Federal Law 259-FZ,
> differentiating "digital financial assets" (tokenized
> securities) from "digital currency" (cryptocurrency) and
> noting the 2021-01-01 effective date and the payment-use
> prohibition. Contextual journalism anchor; Wayback snapshot
> pinning required at human audit.
- **`supporting_journalism`**
  - URL: <https://eurasiangroup.org/en/a-law-on-digital-financial-assets-and-digital-currency-has-been-signed-in-the-russian-federation>
  - Wayback: <https://web.archive.org/web/2020/https://eurasiangroup.org/en/a-law-on-digital-financial-assets-and-digital-currency-has-been-signed-in-the-russian-federation>
  > Eurasian Group on Combating Money Laundering (EAG)
> announcement confirming Putin's signature of the DFA law on
> 2020-07-31. Used as a contextual regional-organization
> anchor. Wayback re-pin required at human audit.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Russia-resident crypto activity (259-FZ regulatory class)
- **Chains**: `bitcoin`, `ethereum`

> Canonical target is the regulatory class of cryptocurrency
> activity within Russia: digital currency issuance, circulation,
> and use as a means of payment by Russian legal entities, Russian
> individual tax residents (including foreigners residing in Russia
> >183 days), and Russian branches/representative offices of
> foreign organizations. The law does not enumerate specific
> exchanges, addresses, or domains as targets; it is a class-level
> foundational regulatory framework. enumeration=subset rather than
> complete because the law addresses an activity class without a
> fixed roster of named entities. Matches the sibling
> russia-cbr-crypto-payment-ban-2022 pattern.

## 3. Changed-layer observations (supports the scoped claim)

*No observed_change entries. This is a `null_event`; see §4 for observed_no_change evidence supporting the null claim.*

## 4. No-change observations (where applicable)

### offramp_cex — `dfa_law_259_fz_payment_ban_enacted_no_per_event_cascade`

**Window**: `2020-07-31 00:00:00+00:00` → `2021-12-31 23:59:59+00:00`

**Sources**:

- **`semi_primary_wayback`**
  - URL: <https://www.loc.gov/item/global-legal-monitor/2021-01-11/russian-federation-new-bill-defines-cryptocurrency-proposes-tax-regulations/>
  - Wayback: <https://web.archive.org/web/20210920180643/https://www.loc.gov/item/global-legal-monitor/2021-01-11/russian-federation-new-bill-defines-cryptocurrency-proposes-tax-regulations/>
  - body_hash: `sha256:2847c0f365eaa143a82c41587b75f315230dedf331f56abe3d3aac1c1ea6ae91`
  - body_path: `sources/http_captures/russia-dfa-law-2020/primary/web.archive.org__web-20210920180643-https-www.loc.gov-item-global-legal-monitor-2021-01-11-russian-federation-new-bill-defines-cryptocurrency-proposes-tax-regulations__642ebaba84.html`
  > Library of Congress Global Legal Monitor summary of
> Federal Law 259-FZ, confirming the 2020-07-31 signing,
> 2021-01-01 effective date, and payment-use prohibition.
> Provisional Wayback anchor; specific snapshot timestamp
> to be re-pinned at human audit.
- **`semi_primary_wayback`**
  - URL: <https://www.crowdfundinsider.com/2020/08/164885-russia-federal-law-addresses-digital-assets-differentiates-between-digital-securities-and-digital-currencies/>
  - Wayback: <https://web.archive.org/web/20200805224916/https://www.crowdfundinsider.com/2020/08/164885-russia-federal-law-addresses-digital-assets-differentiates-between-digital-securities-and-digital-currencies/>
  - body_hash: `sha256:a533401ce7050a6fd60e799310ca69b893f242294196421b9141e392e3998dbc`
  - body_path: `sources/http_captures/russia-dfa-law-2020/primary/web.archive.org__web-20200805224916-https-www.crowdfundinsider.com-2020-08-164885-russia-federal-law-addresses-digital-assets-differentiates-between-digital-securities__0cc9abda05.html`
  > Crowdfund Insider 2020-08 coverage corroborating the
> payment-use prohibition and DFA/digital-currency
> differentiation. Contextual journalism anchor; Wayback
> re-pin required at human audit.

## 5. Honest coverage gaps

- **asset_onchain** (`not_measured`): The 2020-07-31 DFA law defines and circumscribes cryptocurrency

## 7. Related events

- [`russia-cbr-crypto-payment-ban-2022`](./russia-cbr-crypto-payment-ban-2022.md)
- [`russia-mining-regional-ban-2024-12`](./russia-mining-regional-ban-2024-12.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `3b37c3e`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

