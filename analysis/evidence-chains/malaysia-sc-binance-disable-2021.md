# Evidence chain — `malaysia-sc-binance-disable-2021`

**Status**: `admitted` · **Stratum**: `S4_nation_state` · **Shape**: `comparison` (2 changed layer(s): `l4_frontend`, `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-02` · **Source commit**: `3f1a9f2` · **Schema**: `0.2.0` · **Event last_verified**: `2026-06-01` · **Tool version**: `0.1.0` · **Generated**: `2026-06-02T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "Malaysia SC's 2021-07-30 enforcement announcement, corroborated by its 2021
> administrative-actions table, ordered Binance to disable binance.com and
> Binance mobile applications in Malaysia and restrict Malaysian investor
> access to Binance-operated messaging channels within the 14-business-day
> compliance window from 2021-07-26 to 2021-08-16. Binance then announced on
> 2021-08-13 that it would cease MYR trading pairs, MYR payment options, and
> P2P merchant applications in Malaysia on 2021-08-16, with MYR P2P trading
> pairs removed on 2021-08-13. The row does not claim ISP-level blocking,
> independently measured website/app inaccessibility, on-chain asset freezes,
> or broader Malaysian-bank rail restrictions outside Binance's announced MYR
> product surface."

## 1. Trigger

- **Type**: `nation_state_block`
- **Actor**: `MY_SC`
- **Timestamp**: `2021-07-30 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://www.sc.com.my/resources/media/media-release/sc-takes-enforcement-actions-on-binance-for-illegally-operating-in-malaysia>
  - body_hash: `sha256:d1e07086d0475a322fed981f4b58da0be43952f79c9cf24c5bcd8c4f95959514`
  - body_path: `sources/http_captures/malaysia-sc-binance-disable-2021/primary/www.sc.com.my__resources-media-media-release-sc-takes-enforcement-actions-on-binance-for-illegally-operating-in-malaysia__fe876cf7be.html`
  > Securities Commission Malaysia media release dated 2021-07-30,
> announcing enforcement actions against Binance for illegally
> operating a Digital Asset Exchange in Malaysia. The release states
> that the named Binance entities were ordered to disable the Binance
> website and mobile applications in Malaysia within 14 business days
> from 2021-07-26, cease marketing to Malaysian investors, and restrict
> Malaysian investors from accessing Binance's Telegram group. Captured
> and pinned with body_hash/body_path during the 2026-06-01 repair pass.
- **`primary_legal`**
  - URL: <https://www.sc.com.my/regulation/enforcement/actions/administrative-actions/administrative-actions-in-2021>
  - Wayback: <https://web.archive.org/web/20210730101959/https://www.sc.com.my/regulation/enforcement/actions/administrative-actions/administrative-actions-in-2021>
  - body_hash: `sha256:1102ff2a4db7493e59f8be588ce527662436ed6a422639ab8508f05d44cd699e`
  - body_path: `sources/http_captures/malaysia-sc-binance-disable-2021/primary/www.sc.com.my__regulation-enforcement-actions-administrative-actions-administrative-actions-in-2021__c169a0d75c.html`
  > SC administrative-actions page for 2021. The Binance entries identify
> the breach as operating a recognized market / digital asset exchange
> through binance.com and mobile applications without SC registration,
> and record the directive to disable Binance's website and apps in
> Malaysia within 14 business days from 2021-07-26, "being 16 August
> 2021." Captured and pinned with body_hash/body_path; a 2021-07-30
> Wayback snapshot is retained as an additional replay path.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Binance Holdings Ltd. (MY cohort)
- **Canonical domains**: `binance.com`

> Binance group entities and the Malaysia-facing binance.com website, mobile
> applications, Telegram / messaging channels, and MYR payment / P2P product
> surface serving Malaysian retail customers. The SC order names Binance
> Holdings Limited, Binance Digital Limited, Binance UAB, Binance Asia
> Services Pte Ltd, and Zhao Changpeng; operational scope is coded as the
> Binance-Malaysia customer cohort.

## 3. Changed-layer observations (supports the scoped claim)

### l4_frontend · attribution: `direct` · Δt = 0h

**Event label**: `sc_ordered_binance_my_website_apps_and_messaging_disablement`

**Timestamp**: `2021-07-30 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_legal`**
  - URL: <https://www.sc.com.my/resources/media/media-release/sc-takes-enforcement-actions-on-binance-for-illegally-operating-in-malaysia>
  - body_hash: `sha256:d1e07086d0475a322fed981f4b58da0be43952f79c9cf24c5bcd8c4f95959514`
  - body_path: `sources/http_captures/malaysia-sc-binance-disable-2021/primary/www.sc.com.my__resources-media-media-release-sc-takes-enforcement-actions-on-binance-for-illegally-operating-in-malaysia__fe876cf7be.html`
  > SC press release names Binance and orders the Binance website and
> mobile applications disabled in Malaysia within 14 business days
> from 2021-07-26, and separately orders restriction of Malaysian
> investors from Binance's Telegram group. Attribution is direct
> because the primary legal source itself imposes the L4 operator
> obligation.
- **`primary_legal`**
  - URL: <https://www.sc.com.my/regulation/enforcement/actions/administrative-actions/administrative-actions-in-2021>
  - Wayback: <https://web.archive.org/web/20210730101959/https://www.sc.com.my/regulation/enforcement/actions/administrative-actions/administrative-actions-in-2021>
  - body_hash: `sha256:1102ff2a4db7493e59f8be588ce527662436ed6a422639ab8508f05d44cd699e`
  - body_path: `sources/http_captures/malaysia-sc-binance-disable-2021/primary/www.sc.com.my__regulation-enforcement-actions-administrative-actions-administrative-actions-in-2021__c169a0d75c.html`
  > SC administrative-actions table records the legal breach through the
> binance.com website and mobile applications and gives the disablement
> deadline as 2021-08-16. This corroborates the deadline and affected
> frontend/app surfaces; it is not a separate technical reachability
> measurement.

### offramp_cex · attribution: `plausible` · Δt = 336h

**Event label**: `myr_pairs_payment_options_and_p2p_products_restriction_announced`

**Timestamp**: `2021-08-13 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_corporate`**
  - URL: <https://www.binance.com/en/support/announcement/ab37eace9146494d990293d60423a34e>
  - Wayback: <https://web.archive.org/web/20210813165214/https://www.binance.com/en/support/announcement/ab37eace9146494d990293d60423a34e>
  - body_hash: `sha256:1c1f78643b9982e79ed1ca012ff8b5bfc15529b80da2eb157554fbf2eca29a0c`
  - body_path: `sources/http_captures/malaysia-sc-binance-disable-2021/binance/web.archive.org__web-20210813165214-https-www.binance.com-en-support-announcement-ab37eace9146494d990293d60423a34e__159ad87558.html`
  > Archived Binance support announcement titled "Restricting of Product
> Offerings in Malaysia" says Binance would cease MYR trading pairs,
> MYR payment options, and P2P merchant applications in Malaysia on
> 2021-08-16 04:00 UTC, and would remove MYR P2P trading pairs on
> 2021-08-13 13:00 UTC. Attribution is plausible because the Binance
> announcement cites compliance with local regulations but does not
> explicitly name the SC enforcement action in the retained body text.
- **`supporting_journalism`**
  - URL: <https://fxnewsgroup.com/forex-news/cryptocurrency/binance-restricts-product-offering-in-malaysia/>
  - body_hash: `sha256:f964341cd5fe6be2d6191531ae9e83cfde08fdae0e1fa846ac40cd95c9c6873d`
  - body_path: `sources/http_captures/malaysia-sc-binance-disable-2021/secondary/fxnewsgroup.com__forex-news-cryptocurrency-binance-restricts-product-offering-in-malaysia__2580e79382.html`
  > Contemporaneous 2021-08-13 report quoting the Binance announcement's
> Malaysia product-restriction text, including the MYR trading pairs,
> MYR payment options, P2P merchant applications, and MYR P2P removal
> timing. Retained as a secondary corroborating capture only.

## 5. Honest coverage gaps

- **l0_network** (`not_measured`): SC enforcement action is a regulator-directed disable order targeting

## 7. Related events

- [`uk-fca-binance-markets-2021`](./uk-fca-binance-markets-2021.md)
- [`singapore-mas-binance-services-2021`](./singapore-mas-binance-services-2021.md)
- [`netherlands-dnb-binance-warning-2021`](./netherlands-dnb-binance-warning-2021.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `3f1a9f2`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

