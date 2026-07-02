# Evidence chain — `voyager-bankruptcy-doj-objection-2023`

**Status**: `admitted` · **Stratum**: `S3_doj_sec_cftc_fiod` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-08` · **Source commit**: `ee7bf1a` · **Schema**: `0.2.0` · **Event last_verified**: `2026-06-02` · **Tool version**: `0.1.0` · **Generated**: `2026-06-25T23:48:26Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "The 2023-04-01 S.D.N.Y. corrected Opinion & Order granting the
> Government's stay pending appeal of Voyager Digital's confirmation
> order is coded as a single-layer offramp_cex observed_change: the
> court stay paused the bankruptcy-court-mediated Binance.US sale /
> crypto-distribution route. Voyager's 2023-04-25 Doc 1345 termination
> notice is retained as the downstream endpoint showing the Binance.US
> asset-purchase route ended and Voyager intended to toggle to direct
> liquidation distributions; the row does not claim that the DOJ
> directly caused Binance.US's termination."

## 1. Trigger

- **Type**: `court_civil_order`
- **Actor**: `US_SDNY_DISTRICT_COURT`
- **Timestamp**: `2023-04-01 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://cases.stretto.com/public/x193/11753/PLEADINGS/1175304172380000000106.pdf>
  - body_hash: `sha256:f3eb8fee30cb73dff15ce6a3fc40c05afd2b3589c76f4952838c1e162494a5ae`
  - body_path: `sources/http_captures/voyager-bankruptcy-doj-objection-2023/primary-legal-stretto-repair-v2/cases.stretto.com__public-x193-11753-PLEADINGS-1175304172380000000106.pdf__7e88393d78.bin`
  > S.D.N.Y. corrected Opinion & Order, United States et al. v.
> Voyager Digital Holdings et al., No. 23 Civ. 02171 (JHR),
> Document 53, filed 2023-04-01. Judge Jennifer H. Rearden
> granted the Government's emergency motion for a stay pending
> appeal of the Bankruptcy Court's confirmation order. The order
> describes the Binance.US asset-purchase route, the exculpation
> provision, KYC/AML and government-enforcement concerns, and the
> harm to Voyager customers from delaying cryptocurrency
> distributions. This is the load-bearing trigger and
> observed-change anchor.
- **`primary_legal`**
  - URL: <https://cases.stretto.com/public/x193/11753/PLEADINGS/1175303152380000000014.pdf>
  - body_hash: `sha256:25ae70bc59ab756fa34542ab9ba52dc5badb911cec7c4b85448208caee6db555`
  - body_path: `sources/http_captures/voyager-bankruptcy-doj-objection-2023/primary-legal-stretto-repair-v2/cases.stretto.com__public-x193-11753-PLEADINGS-1175303152380000000014.pdf__237b8ded26.bin`
  > Bankruptcy Court Doc 1182, filed 2023-03-14: memorandum in
> support of the United States and United States Trustee's
> expedited motion for stay of the March 8 confirmation order
> pending appeal. The filing cites the Government's notice of
> appeal at Dkt. No. 1165 and explains the asserted police,
> regulatory, KYC, and AML-enforcement concerns with the
> exculpation provisions tied to the Voyager/Binance.US plan.
- **`primary_legal`**
  - URL: <https://cases.stretto.com/public/x193/11753/PLEADINGS/1175303272380000000186.pdf>
  - body_hash: `sha256:bf6a39d6e9c7522e93d70b3e8c660bad4f5e24fb604467e515df19a75e40abfd`
  - body_path: `sources/http_captures/voyager-bankruptcy-doj-objection-2023/primary-legal-stretto-repair-v2/cases.stretto.com__public-x193-11753-PLEADINGS-1175303272380000000186.pdf__4ce51b4aba.bin`
  > S.D.N.Y. Document 4, filed 2023-03-17: Government memorandum
> supporting the emergency motion for stay in the district-court
> appeal. It states that the Government had appealed the March 8
> confirmation order, describes the Voyager-Binance.US commercial
> deal, and asks the district court to stay the confirmation order
> or at least the exculpation provision pending appeal.
- **`supporting_journalism`**
  - URL: <https://www.coindesk.com/policy/2023/03/10/us-doj-appeals-new-york-judges-decision-to-approve-voyagers-sale-to-binanceus>
  - Wayback: <https://web.archive.org/web/20230310074649/https://www.coindesk.com/policy/2023/03/10/us-doj-appeals-new-york-judges-decision-to-approve-voyagers-sale-to-binanceus>
  - body_hash: `sha256:f8816fac4d1f5efb338f42a3323e2fc6d5b7cebe4d109d061b951df8a41dc709`
  - body_path: `sources/http_captures/voyager-bankruptcy-doj-objection-2023/primary/web.archive.org__web-20230310074649-https-www.coindesk.com-policy-2023-03-10-us-doj-appeals-new-york-judges-decision-to-approve-voyagers-sale-to-binanceus__27eaea0eee.html`
  > CoinDesk (2023-03-10) reports the preceding 2023-03-08
> Government appeal of Judge Wiles's confirmation order. Retained
> only as contemporaneous corroboration for the appeal sequence;
> the admission-grade anchors are the Stretto legal PDFs above.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Voyager Digital + Binance.US (BAM Trading)
- **Chains**: `bitcoin`, `ethereum`
- **Canonical domains**: `investvoyager.com`, `binance.us`

> Voyager Digital LLC / Voyager Digital Holdings, Inc. (collectively
> the Chapter 11 debtors) and the contemplated asset acquirer
> Binance.US (BAM Trading Services Inc.). The stay order targets the
> Chapter 11 plan-confirmation path and its third-party release /
> exculpation provisions, including the Binance.US acquisition route
> that would have routed Voyager customer balances through Binance.US.
> No on-chain address set is asserted; the cascade surface is the
> bankruptcy-court-mediated off-ramp distribution path for frozen
> Voyager customer balances.

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `direct` · Δt = 0h

**Event label**: `sdny_stay_order_paused_voyager_binance_us_sale_route`

**Timestamp**: `2023-04-01 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_legal`**
  - URL: <https://cases.stretto.com/public/x193/11753/PLEADINGS/1175304172380000000106.pdf>
  - body_hash: `sha256:f3eb8fee30cb73dff15ce6a3fc40c05afd2b3589c76f4952838c1e162494a5ae`
  - body_path: `sources/http_captures/voyager-bankruptcy-doj-objection-2023/primary-legal-stretto-repair-v2/cases.stretto.com__public-x193-11753-PLEADINGS-1175304172380000000106.pdf__7e88393d78.bin`
  > Corrected S.D.N.Y. Opinion & Order, Document 53, filed
> 2023-04-01. It grants the Government's motion for a stay of
> the confirmation order pending appeal, identifies the
> Voyager/Binance.US asset-purchase route and crypto-distribution
> path, and records the public-interest / government-enforcement
> basis for the stay. This primary legal artifact earns direct
> attribution for the stayed court-mediated sale route.
- **`primary_legal`**
  - URL: <https://cases.stretto.com/public/x193/11753/PLEADINGS/1175304252380000000171.pdf>
  - body_hash: `sha256:e276d7288a7e22e2f9f88af54312918f6d523f5667d825b9711a034c6f672932`
  - body_path: `sources/http_captures/voyager-bankruptcy-doj-objection-2023/primary-legal-stretto-repair-v2/cases.stretto.com__public-x193-11753-PLEADINGS-1175304252380000000171.pdf__d67838da04.bin`
  > Bankruptcy Court Doc 1345, filed 2023-04-25, is Voyager's
> notice of receipt of Binance.US's termination notice. The
> filing states that Voyager received a Notice of Termination
> of the Asset Purchase Agreement from BAM Trading Services Inc.
> d/b/a Binance.US and that the Debtors intended to exercise the
> plan toggle to a liquidation transaction returning crypto and
> cash directly to creditors via the Voyager platform. It anchors
> the downstream endpoint without converting the endpoint into a
> direct DOJ-causation claim.
- **`primary_legal`**
  - URL: <https://cases.stretto.com/public/x193/11753/PLEADINGS/1175303152380000000014.pdf>
  - body_hash: `sha256:25ae70bc59ab756fa34542ab9ba52dc5badb911cec7c4b85448208caee6db555`
  - body_path: `sources/http_captures/voyager-bankruptcy-doj-objection-2023/primary-legal-stretto-repair-v2/cases.stretto.com__public-x193-11753-PLEADINGS-1175303152380000000014.pdf__237b8ded26.bin`
  > Bankruptcy Court Doc 1182, filed 2023-03-14, documents the
> Government's stay-pending-appeal motion and the asserted
> police, regulatory, KYC, and AML enforcement concerns that led
> to the district-court stay order.
- **`primary_legal`**
  - URL: <https://cases.stretto.com/public/x193/11753/PLEADINGS/1175303272380000000186.pdf>
  - body_hash: `sha256:bf6a39d6e9c7522e93d70b3e8c660bad4f5e24fb604467e515df19a75e40abfd`
  - body_path: `sources/http_captures/voyager-bankruptcy-doj-objection-2023/primary-legal-stretto-repair-v2/cases.stretto.com__public-x193-11753-PLEADINGS-1175303272380000000186.pdf__4ce51b4aba.bin`
  > S.D.N.Y. Document 4, filed 2023-03-17, is the Government's
> emergency stay memorandum in the district-court appeal. It
> supports the sequence from bankruptcy-court stay request to
> district-court stay order.
- **`supporting_journalism`**
  - URL: <https://www.coindesk.com/policy/2023/03/10/us-doj-appeals-new-york-judges-decision-to-approve-voyagers-sale-to-binanceus>
  - Wayback: <https://web.archive.org/web/20230310074649/https://www.coindesk.com/policy/2023/03/10/us-doj-appeals-new-york-judges-decision-to-approve-voyagers-sale-to-binanceus>
  - body_hash: `sha256:f8816fac4d1f5efb338f42a3323e2fc6d5b7cebe4d109d061b951df8a41dc709`
  - body_path: `sources/http_captures/voyager-bankruptcy-doj-objection-2023/primary/web.archive.org__web-20230310074649-https-www.coindesk.com-policy-2023-03-10-us-doj-appeals-new-york-judges-decision-to-approve-voyagers-sale-to-binanceus__27eaea0eee.html`
  > CoinDesk reports the 2023-03-08 Government appeal of Judge
> Wiles's confirmation order. Retained as contemporaneous
> corroboration for the pre-stay appeal sequence.
- **`supporting_journalism`**
  - URL: <https://www.coindesk.com/policy/2023/04/01/us-government-case-against-voyager-binanceus-deal-has-substantial-merits-judge-says>
  - Wayback: <https://web.archive.org/web/20230401153120/https://www.coindesk.com/policy/2023/04/01/us-government-case-against-voyager-binanceus-deal-has-substantial-merits-judge-says>
  - body_hash: `sha256:ed36d0c9abf3a4b33434a229dd6bfccede2668ba16415ceee144b7e1be2f4916`
  - body_path: `sources/http_captures/voyager-bankruptcy-doj-objection-2023/primary/web.archive.org__web-20230401153120-https-www.coindesk.com-policy-2023-04-01-us-government-case-against-voyager-binanceus-deal-has-substantial-merits-judge-says__52a7d20dbc.html`
  > CoinDesk (2023-04-01): District Judge Jennifer Rearden,
> S.D.N.Y., finds U.S. government case against the
> Voyager-Binance.US deal has "substantial" merits, granting
> emergency stay of the sale. Retained as contemporaneous
> corroboration; Stretto Document 53 is now the load-bearing
> primary legal anchor.
- **`supporting_journalism`**
  - URL: <https://www.investing.com/news/stock-market-news/binanceus-calls-off-13-billion-deal-for-voyagers-assets-3064146>
  - body_hash: `sha256:2a7c1591f24179e1d6b8764565696982dc0491b72557ae1f20a74378ac2feeab`
  - body_path: `sources/http_captures/voyager-bankruptcy-doj-objection-2023/binance-termination/www.investing.com__news-stock-market-news-binanceus-calls-off-13-billion-deal-for-voyagers-assets-3064146__3c5bb35bf4.html`
  > Reuters-syndicated report, captured via Investing.com on
> 2026-06-01, documenting Binance.US's 2023-04-25 termination of
> the Voyager asset-purchase agreement and the stated "hostile and
> uncertain regulatory climate" rationale. Retained as supporting
> context for the downstream endpoint; the direct attribution in
> this row is limited to the court stay.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`celsius-bankruptcy-mashinsky-doj-2023`](./celsius-bankruptcy-mashinsky-doj-2023.md)
- [`ftx-bankman-fried-doj-2022`](./ftx-bankman-fried-doj-2022.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `ee7bf1a`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

