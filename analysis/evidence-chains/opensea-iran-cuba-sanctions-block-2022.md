# Evidence chain — `opensea-iran-cuba-sanctions-block-2022`

**Status**: `admitted` · **Stratum**: `S5_corporate` · **Shape**: `comparison` (1 changed layer(s): `l4_frontend`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `a785639` · **Schema**: `0.2.0` · **Event last_verified**: `2026-06-01` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T09:36:40Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> *(no scoped_claim recorded — event not paper-ready)*

## 1. Trigger

- **Type**: `corporate_policy_change`
- **Actor**: `OPENSEA_OPERATOR`
- **Timestamp**: `2022-03-03 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_corporate`**
  - URL: <https://opensea.io/tos>
  - Wayback: <https://web.archive.org/web/20220304231810/https://opensea.io/tos>
  - body_hash: `sha256:aeea5280e258d0b40e119f22cd3e8d1ca096dc1b1364e9809bd11c2321833966`
  - body_path: `sources/http_captures/opensea-iran-cuba-sanctions-block-2022/primary_tos_wayback/web.archive.org__web-20220304231810-https-opensea.io-tos__cdb212d483.html`
  > OpenSea Terms of Service snapshot captured by Wayback on 2022-03-04.
> The page requires users not to be located in a US-embargoed country
> or listed on US prohibited/sanctioned/restricted-party lists. This is
> the primary corporate policy anchor; account-termination observations
> are pinned below through contemporaneous reporting.
- **`primary_corporate`**
  - URL: <https://opensea.io/tos>
  - Wayback: <https://web.archive.org/web/20221218055647/https://opensea.io/tos>
  - body_hash: `sha256:4fd60363b72a08c3e44a6fe3cdeed48fbe8916bf8a18d4a46c2f4f2e574b9cd4`
  - body_path: `sources/http_captures/opensea-iran-cuba-sanctions-block-2022/primary_tos_wayback/web.archive.org__web-20221218055647-https-opensea.io-tos__0b3fdaefb8.html`
  > December 2022 OpenSea TOS snapshot, pinned two days before the Cuban
> artist reporting. It expressly covers users located in, ordinarily
> resident in, or organized under a comprehensively US-embargoed
> jurisdiction, plus persons subject to US/other-government/UN sanctions.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: OpenSea users from / nationals of OFAC-sanctioned countries
- **Canonical domains**: `opensea.io`

> OpenSea NFT-marketplace user accounts based in OFAC-sanctioned
> jurisdictions (primarily Iran, later disclosed Cuba) plus nationals
> of those countries (Iranian / Cuban passport holders) living outside
> the sanctioned territory. Subset enumeration: OpenSea has not
> published the full list of terminated accounts. Reported instances
> include Iranian NFT artist Parin Heidari (Iran-national, resident
> outside Iran 13+ years), ~30 Cuban / Cuban-passport artists and
> collectors (incl. NFTcuba.ART founder Gianni D'Alerta resident in
> the US, Gabriel Bianchini Swiss-Italian resident in Spain).

## 3. Changed-layer observations (supports the scoped claim)

### l4_frontend · attribution: `plausible` · Δt = 0h

**Event label**: `opensea_terminated_iranian_user_accounts_under_ofac_compliance`

**Timestamp**: `2022-03-03 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`semi_primary_wayback`**
  - URL: <https://www.coindesk.com/policy/2022/03/03/opensea-bars-iranian-users-as-us-sanctions-talk-ramps-up>
  - Wayback: <https://web.archive.org/web/20220303190923/https://www.coindesk.com/policy/2022/03/03/opensea-bars-iranian-users-as-us-sanctions-talk-ramps-up/>
  - body_hash: `sha256:9c5c1b99e54c8e83ffcd85a6cd7e174404cb385188ef5aa1d84359c11921ad4f`
  - body_path: `sources/http_captures/opensea-iran-cuba-sanctions-block-2022/primary/web.archive.org__web-20220304000000-https-www.coindesk.com-policy-2022-03-03-opensea-bars-iranian-users-as-us-sanctions-talk-ramps-up__a05d5c04bc.html`
  > CoinDesk 2022-03-03: OpenSea barred Iranian users amid US-sanctions
> pressure. Independent semi-primary anchor (replaces generic opensea.io/blog
> primary).
- **`semi_primary_wayback`**
  - URL: <https://decrypt.co/94365/opensea-deletes-iranian-users-accounts-citing-sanctions>
  - Wayback: <https://web.archive.org/web/20220306181511/https://decrypt.co/94365>
  - body_hash: `sha256:4f995a6ba2f5537b22045a2934c24326aac441910c47d5719a49b76390d3e769`
  - body_path: `sources/http_captures/opensea-iran-cuba-sanctions-block-2022/primary/web.archive.org__web-20220306181511-https-decrypt.co-94365__71d7fa78b7.html`
  > Decrypt 2022-03 coverage of OpenSea deleting Iranian users' accounts
> citing sanctions compliance. Independent second semi-primary anchor.

### l4_frontend · attribution: `plausible` · Δt = Noneh

**Event label**: `opensea_terminated_cuban_artist_accounts_including_diaspora_passport_holders`

**Timestamp**: `2022-12-20 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`supporting_journalism`**
  - URL: <https://decrypt.co/117869/nft-marketplace-opensea-confirms-ban-on-cuban-artists>
  - body_hash: `sha256:00fa3cbeb095628ce453ae5553968f81018b465559bd933e9097034f914efe85`
  - body_path: `sources/http_captures/opensea-iran-cuba-sanctions-block-2022/cuban/decrypt.co__117869-nft-marketplace-opensea-confirms-ban-on-cuban-artists__d8df6e55c5.html`
  > Decrypt 2022-12-23 report carrying an OpenSea spokesperson statement
> that OpenSea's TOS prohibits sanctioned individuals, users in
> sanctioned jurisdictions, or services from using OpenSea.
- **`supporting_journalism`**
  - URL: <https://news.artnet.com/market/nft-marketplace-opensea-delisting-cuban-artists-us-sanctions-2235440>
  - body_hash: `sha256:8ae1e5219d86cccbf0a6512b232717d5de100d8508aad63428222e3f94c5800e`
  - body_path: `sources/http_captures/opensea-iran-cuba-sanctions-block-2022/cuban/news.artnet.com__market-nft-marketplace-opensea-delisting-cuban-artists-us-sanctions-2235440__9207d55e6a.html`
  > Artnet News 2022-12-22 reports more than 30 Cuban creators had
> OpenSea accounts delisted and carries an OpenSea spokesperson email
> saying OpenSea complies with US sanctions law. Names diaspora cases
> including NFTcuba.ART founder Gianni D'Alerta and Gabriel Bianchini.
- **`supporting_journalism`**
  - URL: <https://www.washingtontimes.com/news/2022/dec/20/cuban-artists-blocked-from-once-promising-nft-trad/>
  - body_hash: `sha256:b83bfd970ce64a02a5eda24870081883c6dbff7c7f62241a364e43d17511757c`
  - body_path: `sources/http_captures/opensea-iran-cuba-sanctions-block-2022/cuban/www.washingtontimes.com__news-2022-dec-20-cuban-artists-blocked-from-once-promising-nft-trad__bf3a5d853e.html`
  > Washington Times/AP 2022-12-20 reports Cuban artists blocked from
> NFT trading sites and includes OpenSea email language that the
> NFTcuba.ART account was blocked for activity against the TOS.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `a785639`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

