# Evidence chain — `voyager-bankruptcy-doj-objection-2023`

**Status**: `admitted` · **Stratum**: `S3_doj_sec_cftc_fiod` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `128e1e1` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-21` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "The 2023-03-08 DOJ (U.S. Trustee) objection and appeal of Voyager
> Digital's Chapter 11 plan-confirmation order, citing AML /
> sanctions-enforcement grounds against the plan's third-party
> releases and the Binance.US acquisition route, codifies a
> single-layer offramp_cex observation: it blocked the planned
> Binance.US acquisition (formally abandoned 2023-04-25) and forced
> Voyager into self-liquidation distributions. M&A-cancellation
> variant of the lender-bankruptcy twin; distinct from the criminal
> Voyager / Alameda executive investigations."

## 1. Trigger

- **Type**: `court_civil_order`
- **Actor**: `US_TRUSTEE_SDNY`
- **Timestamp**: `2023-03-08 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`supporting_journalism`**
  - URL: <https://www.coindesk.com/policy/2023/03/10/us-doj-appeals-new-york-judges-decision-to-approve-voyagers-sale-to-binanceus>
  - Wayback: <https://web.archive.org/web/20230310074649/https://www.coindesk.com/policy/2023/03/10/us-doj-appeals-new-york-judges-decision-to-approve-voyagers-sale-to-binanceus>
  - body_hash: `sha256:f8816fac4d1f5efb338f42a3323e2fc6d5b7cebe4d109d061b951df8a41dc709`
  - body_path: `sources/http_captures/voyager-bankruptcy-doj-objection-2023/primary/web.archive.org__web-20230310074649-https-www.coindesk.com-policy-2023-03-10-us-doj-appeals-new-york-judges-decision-to-approve-voyagers-sale-to-binanceus__27eaea0eee.html`
  > CoinDesk (2023-03-10): "U.S. Justice Dept. Appeals New York Judge's
> Decision to Approve Voyager's Sale to Binance.US." Reports that the
> DOJ (via the U.S. Trustee's Office, an arm of DOJ overseeing
> bankruptcies) filed an appeal on 2023-03-08 challenging
> Bankruptcy Judge Michael Wiles's 2023-03-07 confirmation order
> approving Voyager Digital's Chapter 11 plan and asset sale to
> Binance.US. Wayback memento 20230310074649 captured 2026-05-21
> with replayable body_hash. The bankruptcy docket entry for the
> U.S. Trustee's objection is at cases.stretto.com (Case No.
> 22-10943, S.D.N.Y. Bankr.).
- **`primary_legal`**
  - URL: <https://cases.stretto.com/Voyager/court-docket>
  - body_hash: `sha256:9521dc8f420e8bdf5c011d45c49a92e91878c79b0254c6fc3c92e91bf742a993`
  - body_path: `sources/http_captures/voyager-bankruptcy-doj-objection-2023/v0_3_repair/cases.stretto.com__Voyager-court-docket__16ccfbf7a0.html`
  > Voyager Digital Holdings bankruptcy docket (Case No. 22-10943,
> S.D.N.Y. Bankr.). Houses the U.S. Trustee's objection to plan
> confirmation and the subsequent notice of appeal of the
> 2023-03-07 confirmation order. DRYRUN pin; specific docket
> entry numbers not retained in this draft.
- **`supporting_journalism`**
  - URL: <https://cointelegraph.com/news/us-officials-appeal-protections-for-voyager-execs-in-binance-us-sale>
  - Wayback: <https://web.archive.org/web/20260517000000/https://cointelegraph.com/news/us-officials-appeal-protections-for-voyager-execs-in-binance-us-sale>
  > Cointelegraph: U.S. Trustee William Harrington and other
> government attorneys filed motion 2023-03-14 in S.D.N.Y.
> bankruptcy court arguing the court "improperly exceeded its
> statutory authority" in approving third-party release provisions
> that would impede the government's "ability to enforce its
> police and regulatory powers" — including AML / sanctions
> enforcement against persons carrying out the sale. Wayback
> capture for this URL not retained in this session (Cointelegraph
> URL returned no CDX mementos).

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Voyager Digital + Binance.US (BAM Trading)
- **Chains**: `bitcoin`, `ethereum`
- **Canonical domains**: `investvoyager.com`, `binance.us`

> Voyager Digital LLC / Voyager Digital Holdings, Inc. (collectively
> the Chapter 11 debtors) and the contemplated asset acquirer
> Binance.US (BAM Trading Services Inc.). DOJ objection targets the
> Chapter 11 plan's third-party release / exculpation provisions and
> the Binance.US acquisition structure on AML / sanctions-enforcement
> grounds. No on-chain address set; the cascade surface is the
> bankruptcy-court-mediated off-ramp distribution of frozen Voyager
> customer balances and the M&A deal that would have routed them
> through Binance.US.

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `direct` · Δt = 0h

**Event label**: `voyager_binance_us_acquisition_blocked_by_doj_objection`

**Timestamp**: `2023-03-08 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`supporting_journalism`**
  - URL: <https://www.coindesk.com/policy/2023/03/10/us-doj-appeals-new-york-judges-decision-to-approve-voyagers-sale-to-binanceus>
  - Wayback: <https://web.archive.org/web/20230310074649/https://www.coindesk.com/policy/2023/03/10/us-doj-appeals-new-york-judges-decision-to-approve-voyagers-sale-to-binanceus>
  - body_hash: `sha256:f8816fac4d1f5efb338f42a3323e2fc6d5b7cebe4d109d061b951df8a41dc709`
  - body_path: `sources/http_captures/voyager-bankruptcy-doj-objection-2023/primary/web.archive.org__web-20230310074649-https-www.coindesk.com-policy-2023-03-10-us-doj-appeals-new-york-judges-decision-to-approve-voyagers-sale-to-binanceus__27eaea0eee.html`
  > CoinDesk reports DOJ filed appeal 2023-03-08 of Judge Wiles's
> 2023-03-07 confirmation of the Voyager Chapter 11 plan and
> Binance.US asset sale. Wayback memento 20230310074649
> captured 2026-05-21.
- **`supporting_journalism`**
  - URL: <https://cointelegraph.com/news/us-officials-appeal-protections-for-voyager-execs-in-binance-us-sale>
  - Wayback: <https://web.archive.org/web/20260517000000/https://cointelegraph.com/news/us-officials-appeal-protections-for-voyager-execs-in-binance-us-sale>
  > Cointelegraph: U.S. Trustee Harrington's 2023-03-14 motion
> targets the plan's third-party release provisions on grounds
> that they would impede AML / sanctions enforcement against
> persons carrying out the sale. Wayback capture not retained
> this session (Cointelegraph URL returned no CDX mementos).
- **`supporting_journalism`**
  - URL: <https://www.coindesk.com/policy/2023/04/01/us-government-case-against-voyager-binanceus-deal-has-substantial-merits-judge-says>
  - Wayback: <https://web.archive.org/web/20230401153120/https://www.coindesk.com/policy/2023/04/01/us-government-case-against-voyager-binanceus-deal-has-substantial-merits-judge-says>
  - body_hash: `sha256:ed36d0c9abf3a4b33434a229dd6bfccede2668ba16415ceee144b7e1be2f4916`
  - body_path: `sources/http_captures/voyager-bankruptcy-doj-objection-2023/primary/web.archive.org__web-20230401153120-https-www.coindesk.com-policy-2023-04-01-us-government-case-against-voyager-binanceus-deal-has-substantial-merits-judge-says__52a7d20dbc.html`
  > CoinDesk (2023-04-01): District Judge Jennifer Rearden,
> S.D.N.Y., finds U.S. government case against the
> Voyager-Binance.US deal has "substantial" merits, granting
> emergency stay of the sale. Wayback memento 20230401153120
> captured 2026-05-21.
- **`primary_legal`**
  - URL: <https://cases.stretto.com/Voyager/court-docket>
  - Wayback: <https://web.archive.org/web/20260517000000/https://cases.stretto.com/Voyager/court-docket>
  - body_hash: `sha256:9521dc8f420e8bdf5c011d45c49a92e91878c79b0254c6fc3c92e91bf742a993`
  - body_path: `sources/http_captures/voyager-bankruptcy-doj-objection-2023/v0_3_repair/cases.stretto.com__Voyager-court-docket__16ccfbf7a0.html`
  > Voyager bankruptcy docket (Case No. 22-10943, S.D.N.Y. Bankr.).
> Live cases.stretto.com docket pre-pinned in v0_3_repair/ with
> body_hash. Wayback memento not available for this private
> docket service; live capture is the canonical anchor.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`celsius-bankruptcy-mashinsky-doj-2023`](./celsius-bankruptcy-mashinsky-doj-2023.md)
- [`ftx-bankman-fried-doj-2022`](./ftx-bankman-fried-doj-2022.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `128e1e1`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

