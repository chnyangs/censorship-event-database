# Evidence chain — `metamask-snaps-region-restrictions-2023-09`

**Status**: `admitted` · **Stratum**: `S5_corporate` · **Shape**: `comparison` (2 changed layer(s): `l3_rpc`, `l4_frontend`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `ff0c8be` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-17` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T11:07:46Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "On 2023-09-12 ConsenSys / MetaMask launched the Snaps platform
> in the MetaMask Extension stable channel (v11.0) behind an
> allowlist (npm package name + version + content checksum) curated
> through the MetaMask Snaps directory. Per-Snap regional
> restrictions (some Snaps unavailable in certain jurisdictions)
> propagate to the wallet user through the same L4 directory gate;
> Snap-internal RPC endpoints inherit that gating at L3 indirectly.
> Two observed_change layers (L4 attribution=direct; L3 attribution=
> plausible) → empirical_shape=comparison, admission_tier=
> empirical_case."

## 1. Trigger

- **Type**: `corporate_policy_change`
- **Actor**: `CONSENSYS_METAMASK`
- **Timestamp**: `2023-09-12 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_corporate`**
  - URL: <https://metamask.io/news/snaps-in-metamask-stable-and-where-we-go-from-here>
  - Wayback: <https://web.archive.org/web/2023/https://metamask.io/news/snaps-in-metamask-stable-and-where-we-go-from-here>
  > ConsenSys / MetaMask blog post announcing the 2023-09-12 launch
> of MetaMask Snaps in the public MetaMask Extension stable
> channel (v11.0). The launch ships the Snaps platform behind an
> allowlist: installation on MetaMask stable is restricted to
> Snaps explicitly defined by npm package name, version, and
> content checksum, curated through the MetaMask Snaps directory.
> The allowlist is the corporate-policy filter at the L4 wallet-
> frontend layer that this event records. DRYRUN: Wayback anchor
> is a 2023 calendar-folder pointer rather than a pinned snapshot
> of the specific blog post; pinned snapshot and body_hash are
> deferred to the human-audit pass per validator policy for
> unarchived sources.
- **`primary_corporate`**
  - URL: <https://metamask.io/news/metamask-snaps-our-first-step-on-the-road-to-becoming-fully-permissionless>
  - Wayback: <https://web.archive.org/web/2023/https://metamask.io/news/metamask-snaps-our-first-step-on-the-road-to-becoming-fully-permissionless>
  > Companion MetaMask blog post framing the open-beta allowlist
> as a transitional step on the road to a fully permissionless
> Snaps platform. The post explicitly documents the curated
> directory model and the audit gate as the corporate filter
> through which third-party Snaps must pass before reaching the
> wallet user. DRYRUN: pinned Wayback snapshot deferred to
> human audit.
- **`supporting_journalism`**
  - URL: <https://www.cryptotimes.io/2023/09/13/metamask-launches-snaps-to-enable-in-wallet-enhancements/>
  - Wayback: <https://web.archive.org/web/2023/https://www.cryptotimes.io/2023/09/13/metamask-launches-snaps-to-enable-in-wallet-enhancements/>
  > Contemporaneous (2023-09-13) coverage of the MetaMask Snaps
> open-beta launch confirming the 2023-09-12 trigger date and
> the allowlist-based curation model. Day-level timing
> triangulation. DRYRUN: pinned Wayback snapshot deferred to
> human audit.
- **`supporting_journalism`**
  - URL: <https://bitcoinist.com/metamask-snaps-open-beta-launches/>
  - Wayback: <https://web.archive.org/web/2023/https://bitcoinist.com/metamask-snaps-open-beta-launches/>
  > Bitcoinist contemporaneous coverage of the MetaMask Snaps open-
> beta launch describing the allowlist gating and the 30+ audited
> Snaps in the directory at launch. Triangulation source for the
> L4 corporate-curation filter framing. DRYRUN: pinned Wayback
> snapshot deferred to human audit.
- **`supporting_community`**
  - URL: <https://github.com/MetaMask/snaps/discussions/1411>
  - Wayback: <https://web.archive.org/web/2023/https://github.com/MetaMask/snaps/discussions/1411>
  > MetaMask Snaps Open Beta Readiness Guide GitHub Discussion
> documenting the npm-package + version + checksum allowlist
> constraint as the corporate gate for which Snaps are
> installable on the MetaMask stable channel. Used to anchor the
> L4-wallet-layer regional / jurisdictional filtering mechanism
> in the developer-facing primary-corporate documentation.
> DRYRUN: pinned Wayback snapshot deferred to human audit.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: MetaMask wallet end-users on stable channel (v11.0+) installing Snaps from the MetaMask Snaps directory
- **Chains**: `ethereum`, `non_evm_via_snaps`
- **Canonical domains**: `metamask.io`, `snaps.metamask.io`

> The corporate-policy filter addresses the class of MetaMask
> wallet end-users who attempt to install third-party Snaps from
> the curated Snaps directory. The allowlist mechanism gates Snap
> availability per Snap (by npm package name, version, content
> checksum) and is the substrate through which per-Snap regional /
> jurisdictional restrictions (where a Snap's own developer or the
> MetaMask audit gate declines availability in certain
> jurisdictions) are surfaced to the wallet UI. enumeration=subset
> because (a) the directory at launch enumerated 30+ audited Snaps
> rather than the complete future Snap population and (b) the
> regional-restriction surface is per-Snap, not a single
> enumerable wallet-user cohort.

## 3. Changed-layer observations (supports the scoped claim)

### l4_frontend · attribution: `direct` · Δt = Noneh

**Event label**: `snaps_directory_allowlist_launch_with_per_snap_regional_filtering`

**Timestamp**: `2023-09-12 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_corporate`**
  - URL: <https://metamask.io/news/snaps-in-metamask-stable-and-where-we-go-from-here>
  - Wayback: <https://web.archive.org/web/20250320210842/https://metamask.io/news/snaps-in-metamask-stable-and-where-we-go-from-here>
  - body_hash: `sha256:a42fb7b1bec4fe891e0a7b46d21427527b9cbe4af213f0d77b1f4d0886ce59d8`
  - body_path: `sources/http_captures/metamask-snaps-region-restrictions-2023-09/primary/web.archive.org__web-20230914000000-https-metamask.io-news-snaps-in-metamask-stable-and-where-we-go-from-here__6d3b8ec255.html`
  > MetaMask official news post on the Snaps platform (the permissioned
> extension framework whose availability/region gating defines this
> event). primary_corporate anchor. Wayback 20250320210842 pinned.
- **`semi_primary_wayback`**
  - URL: <https://www.cryptotimes.io/2023/09/13/metamask-launches-snaps-to-enable-in-wallet-enhancements/>
  - Wayback: <https://web.archive.org/web/20240523031402/https://www.cryptotimes.io/2023/09/13/metamask-launches-snaps-to-enable-in-wallet-enhancements/>
  - body_hash: `sha256:7cdf704ab6b184c62af02f7ea09d20d2fe334e543e70d77a4399bbcd62557815`
  - body_path: `sources/http_captures/metamask-snaps-region-restrictions-2023-09/primary/web.archive.org__web-20230914000000-https-www.cryptotimes.io-2023-09-13-metamask-launches-snaps-to-enable-in-wallet-enhancements__d3bd35d805.html`
  > The Crypto Times 2023-09-13 coverage of the MetaMask Snaps launch.
> Independent semi-primary anchor.

### l3_rpc · attribution: `plausible` · Δt = Noneh

**Event label**: `snap_internal_rpc_endpoints_gated_via_l4_directory_allowlist`

**Timestamp**: `2023-09-12 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_corporate`**
  - URL: <https://metamask.io/news/snaps-in-metamask-stable-and-where-we-go-from-here>
  - Wayback: <https://web.archive.org/web/20250320210842/https://metamask.io/news/snaps-in-metamask-stable-and-where-we-go-from-here>
  - body_hash: `sha256:a42fb7b1bec4fe891e0a7b46d21427527b9cbe4af213f0d77b1f4d0886ce59d8`
  - body_path: `sources/http_captures/metamask-snaps-region-restrictions-2023-09/primary/web.archive.org__web-20230914000000-https-metamask.io-news-snaps-in-metamask-stable-and-where-we-go-from-here__6d3b8ec255.html`
  > MetaMask official news post on the Snaps platform (the permissioned
> extension framework whose availability/region gating defines this
> event). primary_corporate anchor. Wayback 20250320210842 pinned.
- **`semi_primary_wayback`**
  - URL: <https://www.cryptotimes.io/2023/09/13/metamask-launches-snaps-to-enable-in-wallet-enhancements/>
  - Wayback: <https://web.archive.org/web/20240523031402/https://www.cryptotimes.io/2023/09/13/metamask-launches-snaps-to-enable-in-wallet-enhancements/>
  - body_hash: `sha256:7cdf704ab6b184c62af02f7ea09d20d2fe334e543e70d77a4399bbcd62557815`
  - body_path: `sources/http_captures/metamask-snaps-region-restrictions-2023-09/primary/web.archive.org__web-20230914000000-https-www.cryptotimes.io-2023-09-13-metamask-launches-snaps-to-enable-in-wallet-enhancements__d3bd35d805.html`
  > The Crypto Times 2023-09-13 coverage of the MetaMask Snaps launch.
> Independent semi-primary anchor.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`infura-metamask-donetsk-luhansk-block-2022-03`](./infura-metamask-donetsk-luhansk-block-2022-03.md)
- [`consensys-metamask-infura-rpc-data-collection-2022-11`](./consensys-metamask-infura-rpc-data-collection-2022-11.md)
- [`infura-alchemy-tornado-rpc-block-2022`](./infura-alchemy-tornado-rpc-block-2022.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `ff0c8be`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

