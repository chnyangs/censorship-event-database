# Evidence chain — `tornado-cash-github-takedown-2022-08`

**Status**: `admitted` · **Stratum**: `S5_corporate` · **Shape**: `comparison` (1 changed layer(s): `l4_frontend`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-02` · **Source commit**: `cdc9fa8` · **Schema**: `0.2.0` · **Event last_verified**: `2026-06-02` · **Tool version**: `0.1.0` · **Generated**: `2026-06-02T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "Microsoft / GitHub's August 2022 removal of the tornadocash
> GitHub organization from the public GitHub surface is anchored by a
> Wayback before/after pair: the organization page was present with 47
> repositories on 2022-08-08 14:45:05 UTC and returned GitHub's 404 page
> by 2022-08-09 15:42:43 UTC. Contemporaneous reporting ties the takedown
> and related developer-account suspensions to the same-day OFAC SDN
> designation of Tornado Cash; attribution remains plausible because
> GitHub did not publish a standalone takedown rationale."

## 1. Trigger

- **Type**: `corporate_policy_change`
- **Actor**: `github_microsoft`
- **Timestamp**: `2022-08-08 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_corporate`**
  - URL: <https://github.com/tornadocash>
  - Wayback: <https://web.archive.org/web/20220808144505/https://github.com/tornadocash>
  - body_hash: `sha256:2133abf49379a6c9fcc66382c9b454b3482689f234bc3d87a03191c83cc5ebcb`
  - body_path: `sources/http_captures/tornado-cash-github-takedown-2022-08/v0_3_primary_repair/web.archive.org__web-20220808144505-https-github.com-tornadocash__47734842c3.html`
  > GitHub Wayback capture of https://github.com/tornadocash at
> 2022-08-08 14:45:05 UTC. The page title is "Tornado Cash ·
> GitHub"; meta text says the organization had 47 repositories, and
> the body lists the Tornado Cash organization plus repositories such
> as tornado-core and tornado-cli. This is the pre-takedown
> platform-surface anchor for the before/after observation.
- **`primary_corporate`**
  - URL: <https://github.com/tornadocash>
  - Wayback: <https://web.archive.org/web/20220809154243/https://github.com/tornadocash>
  - body_hash: `sha256:e533e007cf7b48ea5b070febcc8add27e624432988710c11effcb496cc6a422c`
  - body_path: `sources/http_captures/tornado-cash-github-takedown-2022-08/v0_3_primary_repair/web.archive.org__web-20220809154243-https-github.com-tornadocash__manual404.html`
  > GitHub Wayback capture of the same https://github.com/tornadocash
> URL at 2022-08-09 15:42:43 UTC. The archived page title is "Page
> not found · GitHub · GitHub" and the selected link remains
> /tornadocash, providing the post-takedown platform-surface anchor.
> The capture is a manually retained 404 body because the capture
> helper recorded the HTTP 404 as an error instead of writing normal
> metadata.
- **`semi_primary_wayback`**
  - URL: <https://www.theregister.com/2022/08/24/github_eff_tornado_cash/>
  - Wayback: <https://web.archive.org/web/20220825093705/https://www.theregister.com/2022/08/24/github_eff_tornado_cash/>
  - body_hash: `sha256:bf2eab81bd1b3e5293bc5dee0f1c2013a0dbebae2eefcaebed196e3d80cf9725`
  - body_path: `sources/http_captures/tornado-cash-github-takedown-2022-08/primary/web.archive.org__web-20220825000000-https-www.theregister.com-2022-08-24-github_eff_tornado_cash__625112de04.html`
  > The Register 2022-08-24 coverage reports that GitHub removed the
> Tornado Cash organization/repositories and developer accounts after
> the OFAC sanctions. Used as contemporaneous context for the action
> and reported rationale; the GitHub before/after captures are the
> primary platform-surface evidence.
- **`semi_primary_wayback`**
  - URL: <https://www.eff.org/deeplinks/2023/04/update-tornado-cash>
  - Wayback: <https://web.archive.org/web/20230419014440/https://www.eff.org/deeplinks/2023/04/update-tornado-cash>
  - body_hash: `sha256:dab65362b458b3ea85681d0389282489cacd6a717781f8ed45c8ea90528747a4`
  - body_path: `sources/http_captures/tornado-cash-github-takedown-2022-08/primary/web.archive.org__web-20230420000000-https-www.eff.org-deeplinks-2023-04-update-tornado-cash__44c1b7fb25.html`
  > EFF 2023-04 retrospective documenting the GitHub takedown and
> partial restoration campaign. Used as secondary context for the
> code-hosting consequence, not as the primary platform-surface
> measurement.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: GitHub (Microsoft) — tornadocash organisation and developer accounts
- **Canonical domains**: `github.com`

> Target is the Tornado Cash open-source organisation and its
> associated developer accounts on github.com (Microsoft / GitHub
> Inc. as platform operator). Named removals on 2022-08-08 include
> the tornadocash GitHub organisation (hosting tornado-core,
> tornado-cli, classic, relayer, and ui repositories) and the
> individual developer account of co-founder Roman Semenov. subset
> because the takedown roster is not exhaustively enumerated in any
> single primary source — contemporaneous reporting names the
> organisation and the Semenov account but does not publish a
> line-by-line repository list. The community-maintained mirror
> organisation tornado-repositories (re-uploaded by EFF-coordinated
> researchers in 2022-08-24) is a downstream artefact of this
> takedown and is referenced informationally.

## 3. Changed-layer observations (supports the scoped claim)

### l4_frontend · attribution: `plausible` · Δt = 0h

**Event label**: `github_microsoft_removed_tornadocash_org_and_semenov_developer_account`

**Timestamp**: `2022-08-08 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_corporate`**
  - URL: <https://github.com/tornadocash>
  - Wayback: <https://web.archive.org/web/20220808144505/https://github.com/tornadocash>
  - body_hash: `sha256:2133abf49379a6c9fcc66382c9b454b3482689f234bc3d87a03191c83cc5ebcb`
  - body_path: `sources/http_captures/tornado-cash-github-takedown-2022-08/v0_3_primary_repair/web.archive.org__web-20220808144505-https-github.com-tornadocash__47734842c3.html`
  > GitHub Wayback before-capture: the tornadocash organization page
> exists on 2022-08-08 14:45:05 UTC with the title "Tornado Cash ·
> GitHub", a meta description saying the organization had 47
> repositories, and visible repository links including tornado-core
> and tornado-cli.
- **`primary_corporate`**
  - URL: <https://github.com/tornadocash>
  - Wayback: <https://web.archive.org/web/20220809154243/https://github.com/tornadocash>
  - body_hash: `sha256:e533e007cf7b48ea5b070febcc8add27e624432988710c11effcb496cc6a422c`
  - body_path: `sources/http_captures/tornado-cash-github-takedown-2022-08/v0_3_primary_repair/web.archive.org__web-20220809154243-https-github.com-tornadocash__manual404.html`
  > GitHub Wayback after-capture: the same URL returns GitHub's "Page
> not found" page at 2022-08-09 15:42:43 UTC. This anchors the
> platform-surface removal window without relying on a later
> GitHub-authored explanation.
- **`semi_primary_wayback`**
  - URL: <https://www.theregister.com/2022/08/24/github_eff_tornado_cash/>
  - Wayback: <https://web.archive.org/web/20220825093705/https://www.theregister.com/2022/08/24/github_eff_tornado_cash/>
  - body_hash: `sha256:bf2eab81bd1b3e5293bc5dee0f1c2013a0dbebae2eefcaebed196e3d80cf9725`
  - body_path: `sources/http_captures/tornado-cash-github-takedown-2022-08/primary/web.archive.org__web-20220825000000-https-www.theregister.com-2022-08-24-github_eff_tornado_cash__625112de04.html`
  > The Register 2022-08-24 coverage of GitHub removing the Tornado
> Cash organization/repositories and developer accounts after the OFAC
> sanctions. Independent semi-primary anchor.
- **`semi_primary_wayback`**
  - URL: <https://www.eff.org/deeplinks/2023/04/update-tornado-cash>
  - Wayback: <https://web.archive.org/web/20230419014440/https://www.eff.org/deeplinks/2023/04/update-tornado-cash>
  - body_hash: `sha256:dab65362b458b3ea85681d0389282489cacd6a717781f8ed45c8ea90528747a4`
  - body_path: `sources/http_captures/tornado-cash-github-takedown-2022-08/primary/web.archive.org__web-20230420000000-https-www.eff.org-deeplinks-2023-04-update-tornado-cash__44c1b7fb25.html`
  > EFF 2023-04 analysis documenting the GitHub takedown of Tornado
> Cash code/accounts and the subsequent partial restoration. Independent
> second semi-primary anchor.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`tornado-cash-ofac-2022`](./tornado-cash-ofac-2022.md)
- [`semenov-ofac-2023`](./semenov-ofac-2023.md)
- [`infura-alchemy-tornado-rpc-block-2022`](./infura-alchemy-tornado-rpc-block-2022.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `cdc9fa8`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

