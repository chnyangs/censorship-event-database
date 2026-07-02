# Evidence chain — `polynonce-bittrex-fincen-2022`

**Status**: `admitted` · **Stratum**: `S3_doj_sec_cftc_fiod` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-08` · **Source commit**: `ee7bf1a` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-20` · **Tool version**: `0.1.0` · **Generated**: `2026-06-25T23:48:26Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "FinCEN + OFAC parallel action against Bittrex (2022-10-11) is recorded
> only for the Bittrex US offramp_cex post-settlement sanctioned-jurisdiction
> deplatforming surface; no replayable Wayback / measurement slice of the
> bittrex.com geoblock has been pinned at draft stage and no L0/L1/L3/L4/
> asset_onchain effect is asserted."

## 1. Trigger

- **Type**: `fincen_action`
- **Actor**: `US_FINCEN`
- **Timestamp**: `2022-10-11 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://www.fincen.gov/news/news-releases/fincen-announces-29-million-enforcement-action-against-virtual-asset-service>
  - body_hash: `sha256:3fad20a38bc90c2e69c4b8cabcc7326e8c01c39c4f264d3842202155851d5d3a`
  - body_path: `sources/http_captures/polynonce-bittrex-fincen-2022/v0_3_repair/www.fincen.gov__news-news-releases-fincen-announces-29-million-enforcement-action-against-virtual-asset-service__19564bb342.html`
  > FinCEN press release (2022-10-11): "FinCEN Announces $29 Million
> Enforcement Action Against Virtual Asset Service Provider Bittrex for
> Willful Violations of the Bank Secrecy Act." Largest FinCEN crypto
> penalty at the time and first FinCEN/OFAC parallel virtual currency
> enforcement. FinCEN found that from Feb 2014 - Dec 2018, Bittrex
> failed to maintain an effective AML program and failed to file SARs
> on suspicious activity, including transactions associated with
> sanctioned jurisdictions (Iran, Cuba, Syria, Sudan, Crimea region of
> Ukraine). Total combined US Treasury penalty ~$53M (FinCEN $29M +
> OFAC $24M; FinCEN credited the $24M OFAC payment against FinCEN's
> penalty so net cash to Treasury was $29M).
- **`primary_legal`**
  - URL: <https://www.fincen.gov/system/files/enforcement_action/2023-04-04/Bittrex_Consent_Order_10.11.2022.pdf>
  - body_hash: `sha256:1800f0add8fa668173861bc695f482bace51868bb6db2f93dd8499bd35e8690e`
  - body_path: `sources/http_captures/polynonce-bittrex-fincen-2022/primary/www.fincen.gov__system-files-enforcement_action-2023-04-04-Bittrex_Consent_Order_10.11.2022.pdf__67076fec6c.bin`
  > Bittrex Inc. FinCEN Consent Order dated 2022-10-11. Documents
> approximately $263 million in virtual-currency-related transactions
> from users in Crimea, Cuba, Iran, Sudan, and Syria between March
> 2014 and December 2017 that Bittrex failed to prevent or report.
> Live fincen.gov PDF captured 2026-05-20 (no Wayback memento exists).
- **`supporting_journalism`**
  - URL: <https://www.cnbc.com/2022/10/11/crypto-company-fined-29point3-million-for-violating-multiple-us-sanctions-.html>
  - body_hash: `sha256:d039a9ba782d9c448f5c8d67ce4c6c2497b920e70ca795352b9ac4c1c071df99`
  - body_path: `sources/http_captures/polynonce-bittrex-fincen-2022/v0_3_repair/www.cnbc.com__2022-10-11-crypto-company-fined-29point3-million-for-violating-multiple-us-sanctions-.html__5dc35e52b2.html`
  > CNBC (2022-10-11) contemporaneous coverage of the parallel
> FinCEN/OFAC settlement: "Treasury fines crypto company $29.3 million
> for violating multiple U.S. sanctions, Bank Secrecy Act."

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Bittrex Inc.
- **Canonical domains**: `bittrex.com`

> Bittrex Inc. is the named entity in the FinCEN Consent Order and the OFAC
> settlement agreement. The Treasury actions enumerate the entity (Bittrex
> Inc.) and the five sanctioned jurisdictions whose users transacted on the
> platform (Crimea region of Ukraine, Cuba, Iran, Sudan, Syria). Coded
> `subset` because the underlying scope is a class of sanctioned-jurisdiction
> users mediated through Bittrex's US offramp surface; no on-chain address
> set or individual customer list is enumerated in the public order.

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `plausible` · Δt = Noneh

**Event label**: `bittrex_us_post_settlement_sanctioned_jurisdiction_deplatforming`

**Timestamp**: `2022-10-11 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_legal`**
  - URL: <https://www.fincen.gov/system/files/enforcement_action/2023-04-04/Bittrex_Consent_Order_10.11.2022.pdf>
  - body_hash: `sha256:1800f0add8fa668173861bc695f482bace51868bb6db2f93dd8499bd35e8690e`
  - body_path: `sources/http_captures/polynonce-bittrex-fincen-2022/primary/www.fincen.gov__system-files-enforcement_action-2023-04-04-Bittrex_Consent_Order_10.11.2022.pdf__67076fec6c.bin`
  > Bittrex Inc. Consent Order (2022-10-11) — primary legal anchor for
> the AML/OFAC failures and the remediation obligations covering
> sanctioned-jurisdiction users. Live fincen.gov PDF captured
> 2026-05-20 (no Wayback memento).

## 5. Honest coverage gaps

- **l4_frontend** (`not_measured`): (no note)

## 7. Related events

- [`sec-v-bittrex-2023`](./sec-v-bittrex-2023.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `ee7bf1a`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

