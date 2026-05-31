# Evidence chain — `okx-aux-cayes-doj-guilty-plea-2025`

**Status**: `admitted` · **Stratum**: `S3_doj_sec_cftc_fiod` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `3067f79` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-31` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "The 2025-02-24 DOJ SDNY resolution — Aux Cayes Fintech (OKX) pleading guilty
> to operating an unlicensed money transmitting business and paying >$504M,
> with controls to prevent US persons from transacting — is a single-layer
> offramp_cex restriction on a legitimate major exchange's US-market access,
> attribution=direct. comparable_main tier."

## 1. Trigger

- **Type**: `doj_indictment`
- **Actor**: `US_DOJ_SDNY`
- **Timestamp**: `2025-02-24 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://www.justice.gov/usao-sdny/pr/okx-pleads-guilty-violating-us-anti-money-laundering-laws-and-agrees-pay-penalties>
  - Wayback: <https://web.archive.org/web/20250224212930/https://www.justice.gov/usao-sdny/pr/okx-pleads-guilty-violating-us-anti-money-laundering-laws-and-agrees-pay-penalties>
  - body_hash: `sha256:9a71e4203f28303ac9ef8fb8f4670358c52e5ba48efb287dfc2884e412e4cf9b`
  - body_path: `sources/http_captures/okx-aux-cayes-doj-guilty-plea-2025/primary/web.archive.org__web-20250224000000-https-www.justice.gov-usao-sdny-pr-okx-pleads-guilty-violating-us-anti-money-laundering-laws-and-agrees-pay-penalties__4a9f16c414.html`
  > DOJ SDNY press release (2025-02-24): "OKX Pleads Guilty To Violating
> U.S. Anti-Money Laundering Laws And Agrees To Pay Penalties Totaling
> More Than $500 Million." Aux Cayes Fintech Co. Ltd. (operator of the
> OKX exchange) pleaded guilty to operating an unlicensed money
> transmitting business and agreed to pay >$504M (a $84M penalty +
> ~$421M forfeiture). The release states OKX served US retail and
> institutional customers who engaged in >$1 trillion of transactions,
> and that OKX was used to facilitate >$5 billion of suspicious
> transactions/criminal proceeds; in early 2024 OKX retained an external
> compliance consultant to advise on controls to prevent US persons from
> transacting on the platform. Wayback 20250224212930 pinned. Grep of
> the captured body confirms "OKX", "Aux Cayes", "guilty", "unlicensed
> money transmitting", "504", "421", "five billion", "trillion",
> "U.S. customers", "prevent U.S. persons".

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Aux Cayes Fintech Co. Ltd. (OKX)
- **Canonical domains**: `okx.com`

> Aux Cayes Fintech Co. Ltd. (Seychelles entity operating the OKX
> cryptocurrency exchange). Marked subset: the named corporate operator + the
> OKX platform's US-customer access surface, not an enumerated set of
> customers. No on-chain addresses named in the captured release (a
> money-transmission guilty plea, not an on-chain freeze).

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `direct` · Δt = 0h

**Event label**: `okx_aux_cayes_guilty_plea_unlicensed_money_transmission_us_restriction`

**Timestamp**: `2025-02-24 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_legal`**
  - URL: <https://www.justice.gov/usao-sdny/pr/okx-pleads-guilty-violating-us-anti-money-laundering-laws-and-agrees-pay-penalties>
  - Wayback: <https://web.archive.org/web/20250224212930/https://www.justice.gov/usao-sdny/pr/okx-pleads-guilty-violating-us-anti-money-laundering-laws-and-agrees-pay-penalties>
  - body_hash: `sha256:9a71e4203f28303ac9ef8fb8f4670358c52e5ba48efb287dfc2884e412e4cf9b`
  - body_path: `sources/http_captures/okx-aux-cayes-doj-guilty-plea-2025/primary/web.archive.org__web-20250224000000-https-www.justice.gov-usao-sdny-pr-okx-pleads-guilty-violating-us-anti-money-laundering-laws-and-agrees-pay-penalties__4a9f16c414.html`
  > DOJ SDNY 2025-02-24: Aux Cayes Fintech (OKX) pleaded guilty to
> operating an unlicensed money transmitting business, agreed to
> >$504M, and (per the release) engaged a compliance consultant to
> prevent US persons from transacting on the platform.
> attribution=direct: the named state action names the specific target
> (Aux Cayes / OKX) and its US-customer access being restricted.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `3067f79`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

