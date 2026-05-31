# Evidence chain — `tornado-cash-github-takedown-2022-08`

**Status**: `admitted` · **Stratum**: `S5_corporate` · **Shape**: `comparison` (1 changed layer(s): `l4_frontend`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `1b889eb` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-17` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "Microsoft / GitHub's 2022-08-08 takedown of the tornadocash
> GitHub organisation (tornado-core, tornado-cli, classic contracts,
> relayer, ui) and suspension of co-founder Roman Semenov's
> developer account — effective the same day as the OFAC SDN
> designation of Tornado Cash (related event tornado-cash-ofac-2022)
> — documents the source-code-distribution sub-layer of the L4
> frontend vertex in the S5_corporate cascade. Paper-relevant as
> the earliest and most foundational source-code-platform
> compliance action in the corpus and as the comparison sibling to
> the application-UI L4 rows (Aave, Uniswap/Balancer, Cloudflare
> Ethereum Gateway)."

## 1. Trigger

- **Type**: `corporate_policy_change`
- **Actor**: `github_microsoft`
- **Timestamp**: `2022-08-08 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`supporting_journalism`**
  - URL: <https://www.theregister.com/AMP/2022/08/24/github_eff_tornado_cash>
  - Wayback: <https://web.archive.org/web/2022/https://www.theregister.com/AMP/2022/08/24/github_eff_tornado_cash>
  > The Register (2022-08-24) reporting that Microsoft-owned GitHub, on
> 2022-08-08 immediately following the OFAC SDN designation of
> Tornado Cash, suspended developer accounts (including Roman
> Semenov) and removed the source-code repositories under the
> tornadocash organisation (tornado-core, tornado-cli, classic
> contracts, relayer, ui). Names the action (account suspension +
> repository takedown) and the trigger (the 2022-08-08 OFAC SDN
> designation of Tornado Cash, captured under related event
> tornado-cash-ofac-2022). DRYRUN: pinned Wayback snapshot and
> body_hash deferred to human-audit pass; marked
> evidence_use=contextual_unarchived per validator policy for
> unarchived sources.
- **`supporting_journalism`**
  - URL: <https://cointelegraph.com/news/github-unbans-tornado-cash-repositories-following-ofac-guidance>
  - Wayback: <https://web.archive.org/web/2022/https://cointelegraph.com/news/github-unbans-tornado-cash-repositories-following-ofac-guidance>
  > Cointelegraph (2022-09-23) coverage of the partial reinstatement
> of the Tornado Cash repositories on GitHub following OFAC's
> 2022-09-13 guidance clarifying that copying or hosting the
> underlying code is not itself sanctioned. Retrospectively
> confirms (a) that the 2022-08-08 takedown occurred and (b) that
> GitHub's stated rationale was sanctions compliance with the
> OFAC SDN designation. DRYRUN: pinned Wayback snapshot deferred
> to human audit.
- **`supporting_journalism`**
  - URL: <https://www.eff.org/deeplinks/2023/04/update-tornado-cash>
  - Wayback: <https://web.archive.org/web/2023/https://www.eff.org/deeplinks/2023/04/update-tornado-cash>
  > Electronic Frontier Foundation (2023-04) retrospective on the
> 2022-08-08 GitHub takedown of the Tornado Cash repositories
> and developer accounts. EFF documents the source-code-layer
> consequences of the OFAC SDN designation, including the
> Microsoft / GitHub takedown rationale and the EFF-coordinated
> re-upload campaign that tested the speech-vs-sanctions
> boundary. DRYRUN: pinned Wayback snapshot deferred to human
> audit.
- **`supporting_journalism`**
  - URL: <https://www.virtualcurrencyreport.com/2022/08/ofac-takes-action-against-virtual-currency-tornado-cashin-novel-application-of-sanctions-authorities/>
  - Wayback: <https://web.archive.org/web/2022/https://www.virtualcurrencyreport.com/2022/08/ofac-takes-action-against-virtual-currency-tornado-cashin-novel-application-of-sanctions-authorities/>
  > Perkins Coie Virtual Currency Report (2022-08) legal-practitioner
> analysis of the 2022-08-08 OFAC SDN designation of Tornado Cash
> and its immediate downstream effects, including the GitHub
> repository removal and developer-account suspensions.
> Triangulation source for the legal-compliance interpretation of
> GitHub's takedown action. DRYRUN: pinned Wayback snapshot
> deferred to human audit.

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

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `1b889eb`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

