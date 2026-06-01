# Evidence chain — `tornado-cash-tornadocash-org-seizure-2022`

**Status**: `admitted` · **Stratum**: `S5_corporate` · **Shape**: `comparison` (1 changed layer(s): `l4_frontend`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `2bea37a` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-17` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T10:12:12Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "The operator-initiated cessation of the canonical tornadocash.org
> web-domain entrypoint on 2022-08-08 — the same day as the OFAC
> SDN designation of Tornado Cash (related event
> tornado-cash-ofac-2022) — documents the canonical-web-domain
> sub-layer of the L4 frontend vertex in the S5_corporate cascade.
> Distinct from the third-party GitHub source-code-host takedown
> (tornado-cash-github-takedown-2022-08), this row captures the
> project's own DNS / web-entrypoint cessation as an
> operator-self-imposed compliance reaction. Paper-relevant as the
> canonical-domain analogue to the source-code-platform and
> application-UI L4 rows in the 2022-08-08 cascade."

## 1. Trigger

- **Type**: `corporate_policy_change`
- **Actor**: `tornado_cash_team`
- **Timestamp**: `2022-08-08 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`supporting_journalism`**
  - URL: <https://alexbobes.medium.com/crypto-mixers-and-tornado-cash-shutdown-98a6e743b596>
  - Wayback: <https://web.archive.org/web/2022/https://alexbobes.medium.com/crypto-mixers-and-tornado-cash-shutdown-98a6e743b596>
  > Retrospective coverage stating that following the 2022-08-08
> OFAC SDN designation of Tornado Cash, "the project's domain
> was deleted on the same day, and GitHub suspended the
> developers' accounts." Triangulates the operator-initiated
> cessation of tornadocash.org at the DNS / web layer. DRYRUN:
> pinned Wayback snapshot and body_hash deferred to human-audit
> pass; marked evidence_use=contextual_unarchived per validator
> policy for unarchived sources.
- **`supporting_journalism`**
  - URL: <https://www.eff.org/deeplinks/2023/04/update-tornado-cash>
  - Wayback: <https://web.archive.org/web/2023/https://www.eff.org/deeplinks/2023/04/update-tornado-cash>
  > Electronic Frontier Foundation (2023-04) retrospective on the
> 2022-08-08 OFAC SDN designation of Tornado Cash and its
> downstream domain- and code-layer consequences. EFF documents
> the operator-side cessation of the canonical tornadocash.org
> web entrypoint after the SDN listing and the shift of the
> frontend to IPFS / Tor mirrors as a community-sustained
> alternative. DRYRUN: pinned Wayback snapshot deferred to
> human audit.
- **`supporting_journalism`**
  - URL: <https://federal-lawyer.com/ofac-and-tornado-cash-a-timeline-of-the-events-leading-to-and-following-ofacs-sanctions/>
  - Wayback: <https://web.archive.org/web/2022/https://federal-lawyer.com/ofac-and-tornado-cash-a-timeline-of-the-events-leading-to-and-following-ofacs-sanctions/>
  > Federal Lawyer (Oberheiden P.C.) timeline of the OFAC Tornado
> Cash events documenting the 2022-08-08 SDN designation and
> immediate downstream effects including the tornadocash.org
> canonical-domain cessation. Triangulation source for the
> domain-layer cessation. DRYRUN: pinned Wayback snapshot
> deferred to human audit.
- **`supporting_journalism`**
  - URL: <https://www.coindesk.com/policy/2022/08/08/crypto-mixing-service-tornado-cash-blacklisted-by-us-treasury>
  - Wayback: <https://web.archive.org/web/2022/https://www.coindesk.com/policy/2022/08/08/crypto-mixing-service-tornado-cash-blacklisted-by-us-treasury>
  > CoinDesk (2022-08-08) contemporaneous reporting of the OFAC
> SDN designation of Tornado Cash, naming the tornadocash.org
> canonical domain in the OFAC-listed property roster. Anchors
> the day-of timing of the trigger and the named-domain scope.
> DRYRUN: pinned Wayback snapshot deferred to human audit.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Tornado Cash — tornadocash.org canonical domain
- **Canonical domains**: `tornadocash.org`, `app.tornadocash.org`

> Target is the canonical web-domain entrypoint of the Tornado Cash
> project at tornadocash.org, operator-initiated cessation under
> OFAC pressure (not government-seized as in silk-road). subset
> because the action scope covers the canonical apex domain and
> associated subdomain entrypoints (app.tornadocash.org) but is not
> exhaustively enumerated in any single primary source — the
> Tornado Cash team did not publish a domain-shutdown changelog,
> and reliance is on contemporaneous and retrospective journalism.
> Community-mirrored IPFS / Tor frontends are downstream artefacts
> and referenced informationally.

## 3. Changed-layer observations (supports the scoped claim)

### l4_frontend · attribution: `plausible` · Δt = 0h

**Event label**: `tornadocash_org_canonical_domain_rendered_unreachable_after_ofac_sdn`

**Timestamp**: `2022-08-08 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`semi_primary_wayback`**
  - URL: <https://federal-lawyer.com/ofac-and-tornado-cash-a-timeline-of-the-events-leading-to-and-following-ofacs-sanctions/>
  - Wayback: <https://web.archive.org/web/20240222012127/https://federal-lawyer.com/ofac-and-tornado-cash-a-timeline-of-the-events-leading-to-and-following-ofacs-sanctions/>
  - body_hash: `sha256:574912a16f369032c0dbe545c028eecf7ccf3f4e6967665d28cdc9d6de618bc2`
  - body_path: `sources/http_captures/tornado-cash-tornadocash-org-seizure-2022/primary/web.archive.org__web-20230101000000-https-federal-lawyer.com-ofac-and-tornado-cash-a-timeline-of-the-events-leading-to-and-following-ofacs-sanctions__783e1924dd.html`
  > Federal-lawyer.com OFAC/Tornado-Cash timeline documenting the
> 2022-08-08 sanctions and the tornadocash.org domain/frontend takedown.
> Independent semi-primary anchor (replaces unarchivable tornadocash.org
> snapshot).
- **`semi_primary_wayback`**
  - URL: <https://www.eff.org/deeplinks/2023/04/update-tornado-cash>
  - Wayback: <https://web.archive.org/web/20230419014440/https://www.eff.org/deeplinks/2023/04/update-tornado-cash>
  - body_hash: `sha256:dab65362b458b3ea85681d0389282489cacd6a717781f8ed45c8ea90528747a4`
  - body_path: `sources/http_captures/tornado-cash-tornadocash-org-seizure-2022/primary/web.archive.org__web-20230420000000-https-www.eff.org-deeplinks-2023-04-update-tornado-cash__44c1b7fb25.html`
  > EFF 2023-04 analysis of the Tornado Cash sanctions and the
> frontend/domain takedown. Independent second semi-primary anchor.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`tornado-cash-ofac-2022`](./tornado-cash-ofac-2022.md)
- [`tornado-cash-github-takedown-2022-08`](./tornado-cash-github-takedown-2022-08.md)
- `tornado-cash-storm-conviction-2025` (draft; no rendered admitted-chain link)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `2bea37a`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

