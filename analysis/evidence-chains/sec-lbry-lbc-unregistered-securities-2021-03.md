# Evidence chain — `sec-lbry-lbc-unregistered-securities-2021-03`

**Status**: `admitted` · **Stratum**: `S3_doj_sec_cftc_fiod` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-05-31` · **Source commit**: `138003a` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-31` · **Tool version**: `0.1.0` · **Generated**: `2026-05-31T14:34:18Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "The 2021-03-29 SEC charge in SEC v. LBRY, Inc. (D.N.H.) and the
> Court's finding that LBRY's LBC sales were an unregistered securities
> offering are recorded as a single-layer offramp_cex issuer-conduct
> restriction, attribution=direct. The row does not claim ISP-level
> blocking, an SEC-ordered frontend takedown (the 2023 LBRY wind-down was
> the company's own response to the ruling and litigation cost), or an
> on-chain LBC freeze (no such on-chain receipt exists)."

## 1. Trigger

- **Type**: `sec_action`
- **Actor**: `US_SEC`
- **Timestamp**: `2021-03-29 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://www.sec.gov/enforcement-litigation/litigation-releases/lr-25573>
  - Wayback: <https://web.archive.org/web/20241207235421/https://www.sec.gov/enforcement-litigation/litigation-releases/lr-25573>
  - body_hash: `sha256:4b5f930697a111c534f596767de2147c9c3f2457277fba8bd3418c4789451c06`
  - body_path: `sources/http_captures/sec-lbry-lbc-unregistered-securities-2021-03/primary/web.archive.org__web-20241207235421-https-www.sec.gov-enforcement-litigation-litigation-releases-lr-25573__4db1f7573e.html`
  > SEC litigation release LR-25573 (SEC v. LBRY, Inc.): the SEC's
> complaint (filed 2021-03-29 in the U.S. District Court for the
> District of New Hampshire) charged LBRY, Inc. with conducting an
> unregistered offering and sale of crypto asset securities. The
> complaint alleged that from at least July 2016 to February 2021,
> LBRY (a video-sharing application) sold crypto asset securities
> called "LBRY Credits" (LBC) to numerous investors including U.S.
> investors, without filing a registration statement and without an
> exemption. The captured litigation-release page records that LBRY
> received approximately $12.2 million in proceeds in U.S. dollars
> and crypto assets from its LBC sales, and that the Court found
> LBRY violated the charged provisions (reserving relief for a later
> date). Wayback 20241207235421 pinned (the 2021 SEC URL path was
> retired in the 2024 SEC.gov site migration; this is the live
> archived copy at the current /enforcement-litigation/ path).
> Verified facts present in captured HTML: "LBRY", "LBRY Credits",
> "LBC", "unregistered", "July 2016", "February 2021", "$12.2
> million", "the Court found that LBRY violated".

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `complete`
- **Actor name**: LBRY, Inc.
- **Canonical domains**: `lbry.com`, `odysee.com`

> LBRY, Inc. (New Hampshire-based issuer of the LBRY Credits / LBC token
> and operator of the LBRY protocol and the Odysee video platform;
> named in SEC v. LBRY, Inc., No. 21-cv-260, D.N.H.). Subject-matter
> scope: the LBC token and the July 2016 - February 2021 sale of LBC
> (~$12.2M proceeds per the SEC filing). enumeration=complete: the row
> enumerates the single named issuer entity and the LBC instrument as
> the offering charged/ruled unregistered. No on-chain addresses are
> enumerated: the action is a securities-law charge and ruling against
> the issuer, not an on-chain freeze of an LBC address.

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `direct` · Δt = 0h

**Event label**: `sec_charges_lbry_unregistered_lbc_securities_offering_and_court_finds_violation`

**Timestamp**: `2021-03-29 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_legal`**
  - URL: <https://www.sec.gov/enforcement-litigation/litigation-releases/lr-25573>
  - Wayback: <https://web.archive.org/web/20241207235421/https://www.sec.gov/enforcement-litigation/litigation-releases/lr-25573>
  - body_hash: `sha256:4b5f930697a111c534f596767de2147c9c3f2457277fba8bd3418c4789451c06`
  - body_path: `sources/http_captures/sec-lbry-lbc-unregistered-securities-2021-03/primary/web.archive.org__web-20241207235421-https-www.sec.gov-enforcement-litigation-litigation-releases-lr-25573__4db1f7573e.html`
  > SEC litigation release LR-25573: the SEC charged LBRY, Inc. with
> an unregistered offering/sale of LBC crypto asset securities
> (complaint filed 2021-03-29, D.N.H.), and the Court found LBRY
> violated the charged provisions. attribution=direct: the SEC
> charge and ruling are the direct legal instrument acting on the
> named issuer and the named LBC asset. Facts verified present in
> captured HTML ("LBRY", "LBRY Credits", "$12.2 million", "the
> Court found that LBRY violated").

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`sec-v-telegram-ton-2020`](./sec-v-telegram-ton-2020.md)
- [`sec-kik-interactive-kin-unregistered-offering-2020-10`](./sec-kik-interactive-kin-unregistered-offering-2020-10.md)
- [`sec-v-ripple-2020`](./sec-v-ripple-2020.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `138003a`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

