# Evidence chain — `samourai-doj-2024`

**Status**: `admitted` · **Stratum**: `S3_doj_sec_cftc_fiod` · **Shape**: `comparison` (1 changed layer(s): `l4_frontend`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `5cd78e4` · **Schema**: `0.2.0` · **Event last_verified**: `2026-04-22` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:23:54Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "DOJ SDNY indictment + domain seizure of Samourai Wallet on 2024-04-24 produced a direct
> L4 observed_change within ~19h of indictment unsealing (canonical samouraiwallet.com
> substituted with an SDNY seizure banner). Joint-action footprint: US + Europol + Portugal +
> Iceland. Other layers pending empirical query."

## 1. Trigger

- **Type**: `doj_indictment`
- **Actor**: `US_DOJ_SDNY`
- **Timestamp**: `2024-04-24 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://www.justice.gov/usao-sdny/pr/founders-and-ceo-cryptocurrency-mixing-service-arrested-and-charged-money-laundering>
  - body_hash: `sha256:4c0bb4581d4e022a235ec932d484403bea011d5379d4686eed71d7138f4fd833`
  - body_path: `sources/http_captures/samourai-doj-2024/doj-press-release/www.justice.gov__usao-sdny-pr-founders-and-ceo-cryptocurrency-mixing-service-arrested-and-charged-money-laundering__9bf8c90adc.html`
  > DOJ SDNY press release for the 2024-04-24 indictment of Keonne Rodriguez and William
> Lonergan Hill, founders and CEO of Samourai Wallet / Whirlpool. Charges: conspiracy
> to commit money laundering and conspiracy to operate an unlicensed money transmitting
> business. Simultaneously, the domain samouraiwallet.com was seized pursuant to a SDNY
> seizure warrant (18 U.S.C. §§ 981, 982; 21 U.S.C. § 853). International cooperation:
> USAO SDNY + FBI + IRS-CI + Europol + Portugal Judiciary Police + Icelandic Police.
- **`primary_legal`**
  - URL: <https://www.justice.gov/usao-sdny/media/1349151/dl>
  > SDNY unsealed indictment (link as discovered on press release); PDF not captured in this draft (separate fetch task).

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Protocol**: `samourai_wallet`
- **Actor name**: Samourai Wallet / Whirlpool
- **Chains**: `bitcoin`
- **Canonical domains**: `samouraiwallet.com`, `whirlpool.samouraiwallet.com`

> Samourai Wallet / Whirlpool was a non-custodial privacy-preserving Bitcoin wallet with
> CoinJoin (Whirlpool) mixer functionality. The indictment alleges the service facilitated
> ≥$100M in illicit transactions and took ≥$2B in fee revenue. Addresses named explicitly
> are fee-collection addresses — not an OFAC SDN-style enumerated address set. This event
> is tracked as a **target.enumeration=subset** with only the canonical domain as the
> anchored identifier; per-address identification would require indictment PDF parsing.

## 3. Changed-layer observations (supports the scoped claim)

### l4_frontend · attribution: `direct` · Δt = 19.66h

**Event label**: `canonical_domain_seized_by_sdny_and_international_partners`

**Timestamp**: `2024-04-24 19:39:38+00:00` (precision: `minute`)

**Sources**:

- **`primary_legal`**
  - URL: <https://web.archive.org/web/20240424193938/https://samouraiwallet.com/>
  - body_hash: `sha256:ee99adbaa188036ca0ad5929e509c229acb2b804c55b24cb81f6ec2978502f2d`
  - body_path: `sources/http_captures/samourai-doj-2024/frontend-wayback/web.archive.org__web-20240424193938-https-samouraiwallet.com__5a0a26a311.html`
  > Wayback snapshot of samouraiwallet.com on 2024-04-24 19:39 UTC carrying the SDNY
> seizure banner verbatim: "This domain has been seized in accordance with a seizure
> warrant issued pursuant to 18 U.S.C. § 981, 18 U.S.C. § 982, and 21 U.S.C. § 853
> issued by the United States District Court for the Southern District of New York as
> part of a joint law enforcement operation and action by: The United States
> Attorney's Office for the Southern District of New York / Federal Bureau of
> Investigation / Internal Revenue Service – Criminal Investigation / Europol /
> Portugal Judiciary Police / Icelandic Police." This is a primary_legal source
> because the banner itself constitutes the judicial notice of seizure.
- **`semi_primary_wayback`**
  - URL: <https://web.archive.org/web/20240420204321/https://www.samouraiwallet.com/>
  - body_hash: `sha256:10b358ebf1fa5fd1768a464d367281d6c55e2a8f97496c0254b84af212607c38`
  - body_path: `sources/http_captures/samourai-doj-2024/frontend-wayback/web.archive.org__web-20240420204321-https-www.samouraiwallet.com__ab4c6f88eb.html`
  > Pre-event Wayback snapshot 2024-04-20 (4 days before seizure). Normal Samourai
> Wallet application: "a bitcoin wallet for the streets / Thwart blockchain based
> surveillance and censorship." Establishes the pre-event state against which the
> seizure banner is a clear observed_change.

## 5. Honest coverage gaps

- **l0_network** (`not_measured`): L0 network-layer OONI API query performed 2026-04-22. Searched the
- **offramp_cex** (`not_measured`): Chain-analytics anchors pinned 2026-04-22 as primary_corporate

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `5cd78e4`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

