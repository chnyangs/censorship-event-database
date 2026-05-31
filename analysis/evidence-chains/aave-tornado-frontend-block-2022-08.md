# Evidence chain — `aave-tornado-frontend-block-2022-08`

**Status**: `admitted` · **Stratum**: `S5_corporate` · **Shape**: `comparison` (1 changed layer(s): `l4_frontend`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `9964436` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-21` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "Aave's 2022-08-13 integration of a TRM Labs compliance-screening
> API at the app.aave.com frontend — blocking wallets that interacted
> with the OFAC-designated Tornado Cash contracts from the
> Aave-operated UI while leaving the Aave Protocol smart contracts
> on-chain unaffected — documents an L4-only frontend-operator
> corporate-compliance action downstream of the 2022-08-08 OFAC
> trigger (related event tornado-cash-ofac-2022). Paper-relevant as
> the frontend-operator vertex of the S5_corporate cascade triangle
> (Circle asset, Infura/Alchemy RPC, Aave frontend) and as the
> comparison sibling to uniswap-frontend-delisting-2023."

## 1. Trigger

- **Type**: `corporate_policy_change`
- **Actor**: `aave_companies_dao`
- **Timestamp**: `2022-08-13 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_corporate`**
  - URL: <https://twitter.com/AaveAave/status/1558414985380536321>
  - Wayback: <https://web.archive.org/web/2022/https://twitter.com/AaveAave/status/1558414985380536321>
  > Aave official Twitter (@AaveAave) statement of 2022-08-13 acknowledging
> that "TRM API risk parameters identify all wallets that have interacted
> with Tornado Cash contracts" and confirming the frontend at
> app.aave.com integrated a TRM Labs compliance API following the
> 2022-08-08 OFAC SDN designation of Tornado Cash (see related event
> tornado-cash-ofac-2022). The Aave frontend operator's own corporate
> statement names the action and the upstream cause. DRYRUN: pinned
> Wayback snapshot and body_hash for this tweet are deferred to the
> human-audit pass; marked evidence_use=contextual_unarchived per
> validator policy for unarchived sources.
- **`supporting_journalism`**
  - URL: <https://blockworks.co/news/defi-web-apps-block-users-hit-by-tornado-cash-dust-attack>
  - Wayback: <https://web.archive.org/web/2022/https://blockworks.co/news/defi-web-apps-block-users-hit-by-tornado-cash-dust-attack>
  > Blockworks contemporaneous coverage (2022-08-13) of the Aave / Uniswap /
> Balancer frontend blocks following the 2022-08-08 OFAC Tornado Cash
> designation, describing the TRM Labs-driven blocklist and the
> "dust attack" downstream that flagged 600+ wallets including
> Brian Armstrong and Justin Sun. Triangulation source for day-level
> timing. DRYRUN: pinned Wayback snapshot deferred to human audit.
- **`supporting_journalism`**
  - URL: <https://cryptoslate.com/aave-confirms-trm-labs-api-blocked-dusted-ethereum-wallets-access-restored/>
  - Wayback: <https://web.archive.org/web/2022/https://cryptoslate.com/aave-confirms-trm-labs-api-blocked-dusted-ethereum-wallets-access-restored/>
  > CryptoSlate contemporaneous coverage (2022-08-13/14) naming the
> TRM Labs API integration on the Aave IPFS frontend as the
> mechanism, and documenting Aave's response and partial
> rollback of dust-flagged addresses. Triangulation source for
> the actor (TRM Labs) and mechanism (frontend-integrated risk-
> scoring API). DRYRUN: pinned Wayback snapshot deferred to
> human audit.
- **`supporting_journalism`**
  - URL: <https://decrypt.co/107890/meet-the-sleuthing-firm-helping-defi-projects-stay-compliant-with-tornado-cash-sanctions>
  - Wayback: <https://web.archive.org/web/2022/https://decrypt.co/107890/meet-the-sleuthing-firm-helping-defi-projects-stay-compliant-with-tornado-cash-sanctions>
  > Decrypt profile of TRM Labs describing its role as compliance-
> screening provider to DeFi frontends (Aave among the named
> integrators) following the 2022-08-08 OFAC Tornado Cash
> designation. Supports the mechanism description (off-the-shelf
> TRM Labs / Chainalysis screening API integrated at the
> frontend operator's UI layer). DRYRUN: pinned Wayback snapshot
> deferred to human audit.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Protocol**: `aave_v2_v3`
- **Actor name**: Aave Companies / Aave DAO (frontend operator)
- **Chains**: `ethereum`
- **Canonical domains**: `app.aave.com`

> Aave Companies / Aave DAO operates the app.aave.com frontend UI
> (and the IPFS-mirrored frontend deployment). On 2022-08-13 the
> frontend integrated a TRM Labs compliance API whose blocklist
> inherited from the OFAC Tornado Cash address universe (per related
> event tornado-cash-ofac-2022) plus all addresses that had
> interacted with the OFAC-listed Tornado Cash contracts post-
> sanction. Target is the operator entity (Aave frontend) rather
> than an enumerated address set because the blocklist is a moving
> reference maintained by TRM Labs, not a static published roster;
> subset because only the Aave-operated UI is in scope here (the
> Aave Protocol smart contracts on-chain remained unaffected).

## 3. Changed-layer observations (supports the scoped claim)

### l4_frontend · attribution: `plausible` · Δt = 0h

**Event label**: `aave_frontend_integrated_trm_labs_api_blocking_tornado_tainted_wallets`

**Timestamp**: `2022-08-13 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`semi_primary_wayback`**
  - URL: <https://cryptoslate.com/aave-confirms-trm-labs-api-blocked-dusted-ethereum-wallets-access-restored/>
  - Wayback: <https://web.archive.org/web/20220814221048/https://cryptoslate.com/aave-confirms-trm-labs-api-blocked-dusted-ethereum-wallets-access-restored/>
  - body_hash: `sha256:e88c85a98c8a2ac17f71f50577b21f6d792dcdb21c8fcf41a91c92566cfd3c69`
  - body_path: `sources/http_captures/aave-tornado-frontend-block-2022-08/primary/web.archive.org__web-20220815000000-https-cryptoslate.com-aave-confirms-trm-labs-api-blocked-dusted-ethereum-wallets-access-restored__8ef9258569.html`
  > CryptoSlate 2022-08 confirming Aave's TRM Labs API blocked
> Tornado-dusted Ethereum wallets from the app frontend (later restored).
> Independent semi-primary anchor (replaces unarchivable Aave tweet).
- **`semi_primary_wayback`**
  - URL: <https://blockworks.co/news/defi-web-apps-block-users-hit-by-tornado-cash-dust-attack>
  - Wayback: <https://web.archive.org/web/20221121141935/https://blockworks.co/news/defi-web-apps-block-users-hit-by-tornado-cash-dust-attack>
  - body_hash: `sha256:0f471941c9c5143b13e359562ec7e079a06b2291236c22c5776b9f3cbee52baa`
  - body_path: `sources/http_captures/aave-tornado-frontend-block-2022-08/primary/web.archive.org__web-20220815000000-https-blockworks.co-news-defi-web-apps-block-users-hit-by-tornado-cash-dust-attack__e4493a1e17.html`
  > Blockworks coverage of DeFi web apps (incl. Aave) blocking users
> hit by the Tornado-Cash dust attack. Independent second semi-primary.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`tornado-cash-ofac-2022`](./tornado-cash-ofac-2022.md)
- [`infura-alchemy-tornado-rpc-block-2022`](./infura-alchemy-tornado-rpc-block-2022.md)
- [`uniswap-frontend-delisting-2023`](./uniswap-frontend-delisting-2023.md)
- [`circle-usdc-tornado-2022`](./circle-usdc-tornado-2022.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `9964436`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

