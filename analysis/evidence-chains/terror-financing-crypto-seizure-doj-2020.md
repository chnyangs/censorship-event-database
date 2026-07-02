# Evidence chain — `terror-financing-crypto-seizure-doj-2020`

**Status**: `admitted` · **Stratum**: `S3_doj_sec_cftc_fiod` · **Shape**: `comparison` (1 changed layer(s): `l4_frontend`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-08` · **Source commit**: `ee7bf1a` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-31` · **Tool version**: `0.1.0` · **Generated**: `2026-06-25T23:48:26Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "On 2020-08-13 DOJ announced the coordinated disruption of three
> crypto-enabled terrorist-finance campaigns involving al-Qassam Brigades,
> al-Qaeda-affiliated Syria fundraisers, and an ISIS-linked FaceMaskCenter.com
> scheme. This draft codes only the directly documented website/social-page
> seizure at `l4_frontend`; cryptocurrency-account seizures remain
> `asset_onchain: not_measured` until a public tx_hash is pinned."

## 1. Trigger

- **Type**: `doj_seizure_order`
- **Actor**: `US_DOJ_DC`
- **Timestamp**: `2020-08-13 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://www.justice.gov/opa/pr/global-disruption-three-terror-finance-cyber-enabled-campaigns>
  - Wayback: <http://web.archive.org/web/20200814232542/https://www.justice.gov/opa/pr/global-disruption-three-terror-finance-cyber-enabled-campaigns>
  - body_hash: `sha256:000020bc96919db4ef08202b09ed962e69baaf9f707e4049e2859708dbc41ba4`
  - body_path: `sources/http_captures/terror-financing-crypto-seizure-doj-2020/primary/web.archive.org__web-20200814232542-https-www.justice.gov-opa-pr-global-disruption-three-terror-finance-cyber-enabled-campaigns__75dbce79dd.html`
  > DOJ OPA 2020-08-13 release, captured from Wayback on 2026-05-31
> after the live justice.gov page returned an Akamai interstitial.
> The source announces the coordinated disruption of al-Qassam
> Brigades, al-Qaeda-affiliated, and ISIS cyber-enabled terror-finance
> campaigns; states that judicially authorized warrants seized millions
> of dollars, over 300 cryptocurrency accounts, four websites, and four
> Facebook pages; and calls it the government's largest-ever seizure of
> cryptocurrency in the terrorism context.
- **`primary_legal`**
  - URL: <https://www.justice.gov/opa/press-release/file/1304276/download>
  - Wayback: <http://web.archive.org/web/20200903202343if_/https://www.justice.gov/opa/press-release/file/1304276/download>
  - body_hash: `sha256:36f0ba91894de6e4fc6e3b0af59dbdfd47de2074ac175a85fb2939e1d9187b74`
  - body_path: `sources/http_captures/terror-financing-crypto-seizure-doj-2020/primary/web.archive.org__web-20200903202343if_-https-www.justice.gov-opa-press-release-file-1304276-download__e0d6a54488.bin`
  > DOJ-hosted criminal-complaint affidavit for Mehmet Akti and
> Husamettin Karatas, captured as a Wayback PDF. The affidavit links
> the al-Qassam/Hamas donation flow to virtual-currency exchange
> accounts and unlicensed money-transmission activity.
- **`primary_legal`**
  - URL: <https://www.justice.gov/opa/press-release/file/1304296/download>
  - Wayback: <http://web.archive.org/web/20201004114529if_/https://www.justice.gov/opa/press-release/file/1304296/download>
  - body_hash: `sha256:dbc11bf5c0044851d923242086b8c6957a3c77c2c8fea66548147f0bbe2ecfe0`
  - body_path: `sources/http_captures/terror-financing-crypto-seizure-doj-2020/primary/web.archive.org__web-20201004114529if_-https-www.justice.gov-opa-press-release-file-1304296-download__345512e6de.bin`
  > DOJ-hosted civil forfeiture complaint bundle, captured as a Wayback
> PDF. It includes the FaceMaskCenter.com / four-Facebook-page ISIS
> forfeiture complaint and an al-Qaeda-linked BTC forfeiture complaint
> with Attachment A enumerating 155 virtual-currency defendant
> properties.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: al-Qassam / al-Qaeda-affiliated / ISIS cyber-enabled fundraising campaigns
- **Chains**: `bitcoin`, `ethereum`
- **Canonical domains**: `alqassam.net`, `alqassam.ps`, `qassam.ps`, `facemaskcenter.com`, `facebook.com`

> Coordinated DOJ action against three cyber-enabled terrorist-finance
> campaigns: al-Qassam Brigades / Hamas donation sites, al-Qaeda-affiliated
> Syria fundraising networks, and Murat Cakar / ISIS-linked
> FaceMaskCenter.com. The DOJ source gives an aggregate over-300
> cryptocurrency-account figure and names four websites plus four Facebook
> pages. The al-Qaeda civil complaint enumerates 155 virtual-currency
> defendant properties, but this draft does not exhaustively transcribe every
> account across all three campaigns, so target.enumeration remains subset.

## 3. Changed-layer observations (supports the scoped claim)

### l4_frontend · attribution: `direct` · Δt = 0h

**Event label**: `terror_finance_websites_and_social_pages_seized`

**Timestamp**: `2020-08-13 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_legal`**
  - URL: <https://www.justice.gov/opa/pr/global-disruption-three-terror-finance-cyber-enabled-campaigns>
  - Wayback: <http://web.archive.org/web/20200814232542/https://www.justice.gov/opa/pr/global-disruption-three-terror-finance-cyber-enabled-campaigns>
  - body_hash: `sha256:000020bc96919db4ef08202b09ed962e69baaf9f707e4049e2859708dbc41ba4`
  - body_path: `sources/http_captures/terror-financing-crypto-seizure-doj-2020/primary/web.archive.org__web-20200814232542-https-www.justice.gov-opa-pr-global-disruption-three-terror-finance-cyber-enabled-campaigns__75dbce79dd.html`
  > DOJ's public release states that law enforcement seized
> al-Qassam Brigades website infrastructure and subsequently operated
> alqassam.net, and that the ISIS/Cakar forfeiture seized
> FaceMaskCenter.com plus four Facebook pages. This is the narrow
> observed_change layer in this draft.
- **`primary_legal`**
  - URL: <https://www.justice.gov/opa/press-release/file/1304296/download>
  - Wayback: <http://web.archive.org/web/20201004114529if_/https://www.justice.gov/opa/press-release/file/1304296/download>
  - body_hash: `sha256:dbc11bf5c0044851d923242086b8c6957a3c77c2c8fea66548147f0bbe2ecfe0`
  - body_path: `sources/http_captures/terror-financing-crypto-seizure-doj-2020/primary/web.archive.org__web-20201004114529if_-https-www.justice.gov-opa-press-release-file-1304296-download__345512e6de.bin`
  > The civil forfeiture complaint identifies FaceMaskCenter.com and four
> Facebook pages as defendant properties, and the al-Qaeda complaint
> attachment enumerates 155 virtual-currency defendant properties.

## 5. Honest coverage gaps

- **asset_onchain** (`not_measured`): DOJ reports seizure / forfeiture of cryptocurrency accounts and the
- **offramp_cex** (`not_measured`): The Akti/Karatas affidavit documents virtual-currency exchange accounts

## 7. Related events

- [`ofac-hamas-buy-cash-msb-2023-10`](./ofac-hamas-buy-cash-msb-2023-10.md)
- [`israel-nbctf-hamas-crypto-addresses-2021`](./israel-nbctf-hamas-crypto-addresses-2021.md)
- [`fayzimatov-alqaeda-syria-ofac-2021-07`](./fayzimatov-alqaeda-syria-ofac-2021-07.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `ee7bf1a`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

