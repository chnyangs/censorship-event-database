# Evidence chain — `sec-kik-interactive-kin-unregistered-offering-2020-10`

**Status**: `admitted` · **Stratum**: `S3_doj_sec_cftc_fiod` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-02` · **Source commit**: `3f1a9f2` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-31` · **Tool version**: `0.1.0` · **Generated**: `2026-06-02T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "The 2020-10-21 SDNY final judgment on consent in SEC v. Kik
> Interactive Inc. is recorded as a single-layer offramp_cex issuer-
> conduct restriction: a §5 injunction, $5M civil penalty, and 3-year
> prior-notice obligation on Kin / new-digital-asset offerings,
> attribution=direct. The row does not claim ISP-level blocking, a
> frontend takedown, or an on-chain Kin freeze (no such on-chain
> receipt exists)."

## 1. Trigger

- **Type**: `sec_action`
- **Actor**: `US_SEC`
- **Timestamp**: `2020-10-21 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://www.sec.gov/news/press-release/2020-262>
  - Wayback: <https://web.archive.org/web/20201024175913/https://www.sec.gov/news/press-release/2020-262>
  - body_hash: `sha256:6332c524c28b2de0cf159b37ee280a698c5cf22ffb6d12052c5775edad41b1b2`
  - body_path: `sources/http_captures/sec-kik-interactive-kin-unregistered-offering-2020-10/primary/web.archive.org__web-20201022000000-https-www.sec.gov-news-press-release-2020-262__bc9a3c2def.html`
  > SEC press release 2020-262 (2020-10-21): "SEC Obtains Final
> Judgment Against Kik Interactive For Unregistered Offering." The
> U.S. District Court for the Southern District of New York entered
> a final judgment on consent against Kik Interactive Inc. resolving
> the SEC's charges (complaint filed 2019-06-04) that Kik's 2017
> unregistered offering of digital "Kin" tokens violated the federal
> securities laws. The court granted the SEC's motion for summary
> judgment on 2020-09-30, finding that Kik's sales of "Kin" were
> sales of investment contracts and therefore securities, and that
> the private and public token sales were a single integrated
> offering. The final judgment permanently enjoins Kik from §5(a)/
> §5(c) Securities Act violations, requires a $5 million civil
> penalty, and requires Kik for three years to give the Commission
> prior notice before participating in any issuance/offer/sale/
> transfer of Kin or any new digital asset. Wayback 20201024175913
> pinned. Verified facts present in captured HTML: title, "Kin",
> "Final Judgment Against Kik", "$5 million", "Unregistered Offering",
> summary-judgment date 2020-09-30, complaint date 2019-06-04.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `complete`
- **Actor name**: Kik Interactive Inc.
- **Canonical domains**: `kin.org`, `kik.com`

> Kik Interactive Inc. (the corporate issuer named in SEC v. Kik
> Interactive Inc., No. 19-cv-5244, SDNY). Subject-matter scope: the
> Kin token and the 2017 ~$100M offering (the SEC complaint alleged
> Kik raised over $100 million selling Kin to U.S. and other investors
> in a private pre-sale and a public sale). enumeration=complete: the
> row enumerates the single named issuer entity and the Kin instrument
> as the offering enjoined at the issuer level. No on-chain addresses
> are enumerated: the final judgment is a securities-law remedy against
> the issuer (injunction + $5M penalty + 3-year prior-notice
> obligation), not an on-chain freeze of any Kin contract address.

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `direct` · Δt = 0h

**Event label**: `sec_final_judgment_enjoins_kik_kin_offering_and_imposes_5m_penalty_and_3yr_prior_notice`

**Timestamp**: `2020-10-21 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_legal`**
  - URL: <https://www.sec.gov/news/press-release/2020-262>
  - Wayback: <https://web.archive.org/web/20201024175913/https://www.sec.gov/news/press-release/2020-262>
  - body_hash: `sha256:6332c524c28b2de0cf159b37ee280a698c5cf22ffb6d12052c5775edad41b1b2`
  - body_path: `sources/http_captures/sec-kik-interactive-kin-unregistered-offering-2020-10/primary/web.archive.org__web-20201022000000-https-www.sec.gov-news-press-release-2020-262__bc9a3c2def.html`
  > SEC press release 2020-262 (2020-10-21): SDNY final judgment on
> consent permanently enjoins Kik from §5 Securities Act
> violations, imposes a $5 million civil penalty, and imposes a
> 3-year prior-notice obligation on any Kin or new-digital-asset
> issuance/offer/sale/transfer. attribution=direct: the SDNY
> judgment is the direct legal instrument restricting the issuer's
> conduct around the Kin asset, and the SEC press release names the
> issuer and the restriction. Facts verified present in captured
> HTML (title, "Kin", "$5 million", summary-judgment 2020-09-30).

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`sec-v-telegram-ton-2020`](./sec-v-telegram-ton-2020.md)
- [`sec-v-ripple-2020`](./sec-v-ripple-2020.md)
- [`blockfi-sec-lending-2022`](./blockfi-sec-lending-2022.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `3f1a9f2`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

