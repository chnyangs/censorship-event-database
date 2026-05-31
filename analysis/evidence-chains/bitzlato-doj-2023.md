# Evidence chain — `bitzlato-doj-2023`

**Status**: `admitted` · **Stratum**: `S3_doj_sec_cftc_fiod` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-05-31` · **Source commit**: `b34ad1c` · **Schema**: `0.2.0` · **Event last_verified**: `2026-04-21` · **Tool version**: `0.1.0` · **Generated**: `2026-05-31T15:13:25Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "DOJ indictment of Bitzlato and its founder on 2023-01-18 — paired with
> FinCEN's Section 9714 special measure designation of Bitzlato as a
> 'primary money laundering concern' — directly disrupted Bitzlato's
> exchange operations at the offramp_cex layer (observed_change, direct
> attribution via FinCEN 9714 order). First application of FinCEN
> Section 9714 to a crypto exchange; structurally distinct from
> pure-OFAC or pure-DOJ paths. L4 frontend takedown of bitzlato.com is
> hypothesized but not asserted in this release: coverage.l4_frontend
> status is `not_measured` and no L4 observation row is attached.
> Future revision should add l4_frontend pre/post Wayback bracketing of
> bitzlato.com to test the FinCEN-9714 + DOJ-indictment frontend
> seizure pattern. v0.3 audit 2026-05-20: scoped_claim repaired per
> Session 2 Block D NO decision (qid=26 bitzlato needs_recheck) which
> flagged original wording for asserting L4 same-day seizure without
> supporting observation row — same defect class as garantex-ofac-2022
> audit_log row 218."

## 1. Trigger

- **Type**: `doj_indictment`
- **Actor**: `US_DOJ`
- **Timestamp**: `2023-01-18 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://www.justice.gov/opa/pr/founder-and-majority-owner-cryptocurrency-exchange-charged-processing-over-700-million>
  - body_hash: `sha256:f329a65084549262222dbcdba541f48123bff56247cbe0f932e3e025f70f1318`
  - body_path: `sources/http_captures/bitzlato-doj-2023/backfill-1.3/www.justice.gov__opa-pr-founder-and-majority-owner-cryptocurrency-exchange-charged-processing-over-700-million__a42e944c97.html`
  > DOJ Office of Public Affairs press release announcing the Bitzlato action on 2023-01-18
- **`primary_legal`**
  - URL: <https://www.justice.gov/usao-edny/pr/founder-and-majority-owner-bitzlato-cryptocurrency-exchange-charged-unlicensed-money>
  > EDNY press release for the same enforcement action
- **`primary_legal`**
  - URL: <https://www.fincen.gov/news/news-releases/fincen-identifies-virtual-currency-exchange-bitzlato-primary-money-laundering>
  - Wayback: <https://web.archive.org/web/20260421105235/https://www.fincen.gov/news/news-releases/fincen-identifies-virtual-currency-exchange-bitzlato-primary-money-laundering>
  - body_hash: `sha256:bf2c40b29895e11a97510321b0a33003b56802ad3349fac1357f4b927cf143e6`
  - body_path: `sources/http_captures/bitzlato-doj-2023/backfill-1.3/www.fincen.gov__news-news-releases-fincen-identifies-virtual-currency-exchange-bitzlato-primary-money-laundering__c4a9bf0d08.html`
  > Concurrent FinCEN order describing Bitzlato as a primary money laundering concern

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `complete`
- **Chains**: `bitcoin`, `ethereum`

> Single named entity (Bitzlato) fully specified; no address-level enumeration claim is made at this event level.

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `direct` · Δt = Noneh

**Event label**: `exchange_operations_disrupted_by_enforcement`

**Timestamp**: `2023-01-18 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_legal`**
  - URL: <https://www.justice.gov/opa/pr/founder-and-majority-owner-cryptocurrency-exchange-charged-processing-over-700-million>
  - body_hash: `sha256:f329a65084549262222dbcdba541f48123bff56247cbe0f932e3e025f70f1318`
  - body_path: `sources/http_captures/bitzlato-doj-2023/backfill-1.3/www.justice.gov__opa-pr-founder-and-majority-owner-cryptocurrency-exchange-charged-processing-over-700-million__a42e944c97.html`
  > DOJ describes the Bitzlato disruption and arrest
- **`primary_legal`**
  - URL: <https://www.fincen.gov/news/news-releases/fincen-identifies-virtual-currency-exchange-bitzlato-primary-money-laundering>
  - Wayback: <https://web.archive.org/web/20260421105235/https://www.fincen.gov/news/news-releases/fincen-identifies-virtual-currency-exchange-bitzlato-primary-money-laundering>
  - body_hash: `sha256:bf2c40b29895e11a97510321b0a33003b56802ad3349fac1357f4b927cf143e6`
  - body_path: `sources/http_captures/bitzlato-doj-2023/backfill-1.3/www.fincen.gov__news-news-releases-fincen-identifies-virtual-currency-exchange-bitzlato-primary-money-laundering__c4a9bf0d08.html`
  > FinCEN order prohibits certain transmittals involving Bitzlato

## 5. Honest coverage gaps

- **l0_network** (`not_measured`): No network-layer measurement plan attached yet for this event
- **l3_rpc** (`not_measured`): Public RPC provider substrate anchors exist for adjacent OFAC-aware
- **l4_frontend** (`not_measured`): Frontend/operator availability is not asserted in this release
- **asset_onchain** (`not_measured`): This trigger is not primarily an issuer blacklist event

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `b34ad1c`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

