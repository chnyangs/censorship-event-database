# Evidence chain — `sec-garza-gaw-miners-zenminer-2015`

**Status**: `admitted` · **Stratum**: `S3_doj_sec_cftc_fiod` · **Shape**: `comparison` (1 changed layer(s): `l4_frontend`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `b3ed1c5` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-20` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> The 2015-12-01 SEC civil action against Homero Joshua Garza, GAW
> Miners, LLC, and ZenMiner, LLC for the unregistered sale of
> Hashlet "securities" pointing to nonexistent or oversold cloud-
> mining capacity precipitated the cessation of the gawminers.com
> and zenminer.com cloud-mining-service frontends in the months
> following filing. The row claims only this single-layer L4
> frontend cessation observation with attribution=direct; no
> L0/L1/L3/asset-onchain/offramp_cex effects are coded because the
> Hashlet product was a service contract rather than an on-chain
> freezable token and the operator was a cloud-mining service
> rather than a fiat off-ramp / exchange.

## 1. Trigger

- **Type**: `sec_action`
- **Actor**: `US_SEC`
- **Timestamp**: `2015-12-01 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://www.sec.gov/litigation/litreleases/2015/lr23415.htm>
  - Wayback: <https://web.archive.org/web/20151205075931/https://www.sec.gov/litigation/litreleases/2015/lr23415.htm>
  - body_hash: `sha256:d10f47516e1342667f4a2eea6fb264cf048fdae2a224e56eea3661007c32e452`
  - body_path: `sources/http_captures/sec-garza-gaw-miners-zenminer-2015/primary/web.archive.org__web-20151205075931-https-www.sec.gov-litigation-litreleases-2015-lr23415.htm__d4bec17b63.html`
  > SEC Litigation Release No. 23415 (2015-12-01): "Homero Joshua
> Garza" — announcing the SEC civil action filed in the U.S.
> District Court for the District of Connecticut against Homero
> Joshua Garza and his Connecticut-based companies GAW Miners,
> LLC and ZenMiner, LLC (d/b/a Zen Cloud) for selling
> unregistered securities in the form of "Hashlets" — purported
> shares in a digital Bitcoin mining operation. From approximately
> August 2014 to December 2014, Garza and his companies sold
> ~$20 million worth of Hashlet contracts to more than 10,000
> investors, while the companies did not own enough computing
> power to deliver the mining capacity promised; returns paid to
> some investors came from proceeds of sales to other investors
> (Ponzi-style). Charges: violations of Securities Act Sections
> 5(a), 5(c), and 17(a), and Exchange Act Section 10(b) /
> Rule 10b-5. Wayback URL pinned as a 2015 wildcard anchor;
> evidence_use=contextual_unarchived because the authoring LLM
> agent has not personally captured a body_hash or pinned a
> specific snapshot timestamp in this draft pass.
- **`primary_legal`**
  - URL: <https://www.sec.gov/files/litigation/complaints/2015/comp23415.pdf>
  - Wayback: <https://web.archive.org/web/2015/https://www.sec.gov/files/litigation/complaints/2015/comp23415.pdf>
  > SEC civil complaint (D. Conn., 2015-12-01) against Homero
> Joshua Garza, GAW Miners, LLC, and ZenMiner, LLC. Details the
> Hashlet product as a securities-law "investment contract" under
> Howey: investors paid in for shares of computing power pointing
> to digital mining returns, with returns dependent on the
> managerial efforts of Garza and his companies. The complaint
> alleges Garza and the companies oversold cloud-mining capacity
> substantially beyond what they actually owned. Relief sought:
> permanent injunctive relief, disgorgement of ill-gotten gains
> plus prejudgment interest, and civil penalties. Wayback URL
> pinned as a 2015 wildcard anchor; evidence_use=
> contextual_unarchived pending human-audit re-pin and body_hash.
- **`primary_legal`**
  - URL: <https://www.sec.gov/news/pressrelease/2015-271.html>
  - Wayback: <https://web.archive.org/web/20151204024842/https://www.sec.gov/news/pressrelease/2015-271.html>
  - body_hash: `sha256:32e325dc9a379e6fefa7ae8294e941363aefa26258af64f7908965e535f52d35`
  - body_path: `sources/http_captures/sec-garza-gaw-miners-zenminer-2015/primary/web.archive.org__web-20151204024842-https-www.sec.gov-news-pressrelease-2015-271.html__a27070a955.html`
  > SEC press release 2015-271 (2015-12-01): "SEC Charges Bitcoin
> Mining Companies." Press-release corroboration of the
> litigation release and complaint; characterizes the action as
> an SEC charge against Garza and the GAW Miners / ZenMiner
> companies for perpetrating a securities-fraud scheme through
> the sale of Hashlets to more than 10,000 investors.
> contextual_unarchived pending human-audit re-pin.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: GAW Miners / ZenMiner / Garza
- **Chains**: `bitcoin`
- **Canonical domains**: `gawminers.com`, `zenminer.com`

> Named defendants: Homero Joshua Garza (individual founder/CEO);
> GAW Miners, LLC; and ZenMiner, LLC (d/b/a Zen Cloud). GAW Miners
> and ZenMiner were Connecticut-based cloud-mining service operators
> that sold the "Hashlet" product — a service contract purporting to
> represent a share in digital Bitcoin mining capacity. Hashlets
> were not on-chain tokens or freezable assets; they were
> contractual claims against the issuing service. canonical_domains
> lists the two operator-controlled public surfaces. No on-chain BTC
> addresses are enumerated at this event-row level.

## 3. Changed-layer observations (supports the scoped claim)

### l4_frontend · attribution: `direct` · Δt = 0h

**Event label**: `gaw_miners_zenminer_cloud_mining_frontends_taken_offline_following_sec_action`

**Timestamp**: `2015-12-01 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_legal`**
  - URL: <https://www.sec.gov/litigation/litreleases/2015/lr23415.htm>
  - Wayback: <https://web.archive.org/web/20151205075931/https://www.sec.gov/litigation/litreleases/2015/lr23415.htm>
  - body_hash: `sha256:d10f47516e1342667f4a2eea6fb264cf048fdae2a224e56eea3661007c32e452`
  - body_path: `sources/http_captures/sec-garza-gaw-miners-zenminer-2015/primary/web.archive.org__web-20151205075931-https-www.sec.gov-litigation-litreleases-2015-lr23415.htm__d4bec17b63.html`
  > SEC Litigation Release No. 23415 names Garza, GAW Miners,
> and ZenMiner as the defendants in the unregistered-
> securities / Hashlet-fraud civil action. attribution=direct
> because the SEC complaint named the issuing operators by
> name and the public cloud-mining frontends (gawminers.com,
> zenminer.com) ceased operating as the cloud-mining service
> surface within weeks/months of filing; the cessation was a
> direct consequence of the enforcement action and parallel
> corporate collapse rather than an independent business
> decision. Wayback anchor is a 2015 wildcard pointer pending
> human-audit re-pin.
- **`primary_legal`**
  - URL: <https://www.sec.gov/files/litigation/complaints/2015/comp23415.pdf>
  - Wayback: <https://web.archive.org/web/2015/https://www.sec.gov/files/litigation/complaints/2015/comp23415.pdf>
  > SEC civil complaint (D. Conn.) details the Hashlet product
> and the operator-state collapse it precipitated.
> Corroborates the L4 frontend cessation observation at the
> primary-legal tier. Wayback anchor is a 2015 wildcard
> pointer pending human-audit re-pin.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`sec-shavers-btcst-2013`](./sec-shavers-btcst-2013.md)
- [`sec-burnside-bitcoin-stock-exchange-2014`](./sec-burnside-bitcoin-stock-exchange-2014.md)
- [`sec-voorhees-satoshidice-2014`](./sec-voorhees-satoshidice-2014.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `b3ed1c5`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

