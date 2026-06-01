# Evidence chain — `opensea-iran-cuba-sanctions-block-2022`

**Status**: `admitted` · **Stratum**: `S5_corporate` · **Shape**: `comparison` (1 changed layer(s): `l4_frontend`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `24d80a4` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-21` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T01:03:45Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> *(no scoped_claim recorded — event not paper-ready)*

## 1. Trigger

- **Type**: `corporate_policy_change`
- **Actor**: `OPENSEA_OPERATOR`
- **Timestamp**: `2022-03-03 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_corporate`**
  - URL: <https://opensea.io/blog>
  - Wayback: <https://web.archive.org/web/2022*/opensea.io/blog>
  > OpenSea corporate blog / Help Center 2022-03 TOS update — OpenSea
> publicly confirmed via Twitter on 2022-03-03 that as a US-based
> company it complies with US sanctions law and blocks users in
> OFAC-sanctioned jurisdictions (Iran, Cuba, etc.). Reports of mass
> Iranian-account terminations begin same day. Replayable Wayback
> anchors pinned in observation sources (CoinDesk + Decrypt).

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

### l4_frontend · attribution: `direct` · Δt = Noneh

**Event label**: `opensea_terminated_cuban_artist_accounts_including_diaspora_passport_holders`

**Timestamp**: `2022-12-20 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_corporate`**
  - URL: <https://opensea.io/blog>
  - Wayback: <https://web.archive.org/web/2022*/opensea.io/blog>
  > OpenSea spokesperson statement (2022-12): "We comply with U.S.
> sanctions law. Our terms of service explicitly prohibit
> sanctioned individuals, individuals in sanctioned jurisdictions,
> or services from using OpenSea." Direct corporate attribution for
> the Cuban-artist account terminations — including Cuban-passport
> holders resident outside Cuba (diaspora over-blocking).
- **`supporting_journalism`**
  - URL: <https://decrypt.co/117869/nft-marketplace-opensea-confirms-ban-on-cuban-artists>
  - Wayback: <https://web.archive.org/web/2022*/decrypt.co/117869/*>
  > Decrypt 2022-12 — OpenSea confirms ban on Cuban artists; ~30 artists / collectors affected.
- **`supporting_journalism`**
  - URL: <https://news.artnet.com/market/nft-marketplace-opensea-delisting-cuban-artists-us-sanctions-2235440>
  - Wayback: <https://web.archive.org/web/2022*/news.artnet.com/*opensea*cuban*>
  > Artnet News 2022-12 — names diaspora cases (NFTcuba.ART founder
> Gianni D'Alerta resident in the US; Gabriel Bianchini Swiss-
> Italian resident in Spain). Documents over-blocking of
> Cuban-passport holders living outside Cuba.
- **`supporting_journalism`**
  - URL: <https://www.washingtontimes.com/news/2022/dec/20/cuban-artists-blocked-from-once-promising-nft-trad/>
  - Wayback: <https://web.archive.org/web/2022*/washingtontimes.com/news/2022/dec/20/cuban-artists-blocked-from-once-promising-nft-trad/>
  > Washington Times 2022-12-20 — Cuban artists blocked from OpenSea.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `24d80a4`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

