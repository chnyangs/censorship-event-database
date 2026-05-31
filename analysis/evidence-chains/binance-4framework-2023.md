# Evidence chain — `binance-4framework-2023`

**Status**: `admitted` · **Stratum**: `S3_doj_sec_cftc_fiod` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `22e4579` · **Schema**: `0.2.0` · **Event last_verified**: `2026-04-22` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "The 2023-11-21 DOJ + FinCEN + OFAC + CFTC $4.3B settlement with Binance
> Holdings and CEO Changpeng Zhao represents the only 4-framework coordinated
> enforcement in the dataset. The canonical binance.com frontend remained
> operational post-settlement (observed_no_change); compliance-remediation
> regime under 5-year monitorship (observed_change, direct). Structurally
> distinct from SDN-listing / domain-seizure enforcement paths."

## 1. Trigger

- **Type**: `doj_indictment`
- **Actor**: `US_DOJ_FinCEN_OFAC_CFTC`
- **Timestamp**: `2023-11-21 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://www.justice.gov/archives/opa/pr/binance-and-ceo-plead-guilty-federal-charges-4b-resolution>
  - body_hash: `sha256:fe6c94a854a7600c6a431a88677f4566b02413935b8111aa421c8e0e29c2bafe`
  - body_path: `sources/http_captures/binance-4framework-2023/primary/www.justice.gov__archives-opa-pr-binance-and-ceo-plead-guilty-federal-charges-4b-resolution__1d3bf7f1b0.html`
  > DOJ OPA press release "Binance and CEO Plead Guilty to Federal Charges in
> $4B Resolution" (2023-11-21). Historic settlement: Binance + CEO Changpeng
> Zhao plead guilty to operating unlicensed money-transmitting business,
> BSA violations, sanctions violations (IEEPA). $4.3B total resolution —
> the largest corporate resolution with a crypto company in history.
> **Four-framework coordinated action**: DOJ (criminal), FinCEN (BSA
> civil), OFAC (sanctions civil), CFTC (commodities enforcement).
- **`primary_legal`**
  - URL: <https://home.treasury.gov/news/press-releases/jy1925>
  - body_hash: `sha256:ed854249a4a3e2fafbeb93d8e310f7e21456ee7bad51680c6a764b490647c234`
  - body_path: `sources/http_captures/binance-4framework-2023/primary/home.treasury.gov__news-press-releases-jy1925__4346771bca.html`
  > Treasury press release "Treasury Announces Largest Settlements in History
> with World's Largest Virtual Currency Exchange Binance for Violations of
> U.S. Anti-Money Laundering and Sanctions Laws" (2023-11-21). Documents
> the OFAC + FinCEN side: $968M OFAC settlement (sanctions violations
> across Iran, Cuba, Syria, Crimea, North Korea) + $3.4B FinCEN BSA
> penalty. First 4-framework coordinated action against a major exchange
> in the dataset.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Binance Holdings + Changpeng Zhao
- **Canonical domains**: `binance.com`

> Binance Holdings Ltd. (corporate entity) + Changpeng Zhao (individual, CEO
> at time of violations). No OFAC SDN designation (Binance is not on the SDN
> list post-settlement) — the 4-framework action is a civil-criminal
> resolution rather than an SDN listing. Canonical domain binance.com remained
> operational post-settlement (under a monitor).

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `direct` · Δt = 0h

**Event label**: `compliance_remediation_program_mandated`

**Timestamp**: `2023-11-21 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_legal`**
  - URL: <https://home.treasury.gov/news/press-releases/jy1925>
  - body_hash: `sha256:ed854249a4a3e2fafbeb93d8e310f7e21456ee7bad51680c6a764b490647c234`
  - body_path: `sources/http_captures/binance-4framework-2023/primary/home.treasury.gov__news-press-releases-jy1925__4346771bca.html`
  > Treasury / FinCEN settlement mandates 5-year compliance monitorship,
> enhanced KYC/AML controls, retrospective transaction review. Binance
> (as a CEX itself) underwent structural compliance remediation as
> direct consequence of the 4-framework resolution. attribution=direct
> because the settlement documents explicitly name the required
> remediation steps.
- **`primary_legal`**
  - URL: <https://www.justice.gov/archives/opa/pr/binance-and-ceo-plead-guilty-federal-charges-4b-resolution>
  - body_hash: `sha256:fe6c94a854a7600c6a431a88677f4566b02413935b8111aa421c8e0e29c2bafe`
  - body_path: `sources/http_captures/binance-4framework-2023/primary/www.justice.gov__archives-opa-pr-binance-and-ceo-plead-guilty-federal-charges-4b-resolution__1d3bf7f1b0.html`
  > DOJ criminal settlement — sanctions-screening and money-laundering
> monitor appointments; CZ $50M personal fine + 4 month prison sentence.

## 4. No-change observations (where applicable)

### l4_frontend — `canonical_frontend_remained_operational_through_4b_settlement`

**Window**: `2023-11-21 00:00:00+00:00` → `2023-12-05 23:59:59+00:00`

**Sources**:

- **`primary_legal`**
  - URL: <https://www.justice.gov/archives/opa/pr/binance-and-ceo-plead-guilty-federal-charges-4b-resolution>
  - body_hash: `sha256:fe6c94a854a7600c6a431a88677f4566b02413935b8111aa421c8e0e29c2bafe`
  - body_path: `sources/http_captures/binance-4framework-2023/primary/www.justice.gov__archives-opa-pr-binance-and-ceo-plead-guilty-federal-charges-4b-resolution__1d3bf7f1b0.html`
  > DOJ press release explicitly describes ongoing Binance operations with
> compliance monitor; no domain seizure or suspension. binance.com
> remained reachable for global users (US users had been geo-blocked
> since 2019 Binance.US bifurcation); the settlement did not change
> public frontend availability.
- **`primary_legal`**
  - URL: <https://home.treasury.gov/news/press-releases/jy1925>
  - body_hash: `sha256:ed854249a4a3e2fafbeb93d8e310f7e21456ee7bad51680c6a764b490647c234`
  - body_path: `sources/http_captures/binance-4framework-2023/primary/home.treasury.gov__news-press-releases-jy1925__4346771bca.html`
  > Treasury release confirms Binance continues operations subject to
> FinCEN / OFAC monitorship; no frontend takedown.

## 5. Honest coverage gaps

- **l0_network** (`not_measured`): L0 network-layer OONI API query performed 2026-04-22. Searched the

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `22e4579`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

