# Evidence chain — `ens-eth-domain-tornado-resolution-2022`

**Status**: `admitted` · **Stratum**: `S5_corporate` · **Shape**: `null_event` (0 changed layer(s): none) · **Tier**: `null_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `6293bc1` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-21` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "No ENS-protocol or ENS Labs (app.ens.domains) frontend action
> to block resolution, transfer, or management of the
> tornadocash.eth ENS name or its sub-names is documented in the
> public corpus following the 2022-08-08 OFAC SDN designation of
> Tornado Cash. The name continued to resolve via the public ENS
> resolver and via the eth.limo HTTPS gateway through at least
> end-2022. Recorded as a null_event denominator-control row that
> delineates the perimeter of the 2022-08-08 cascade at the
> ENS-name-service vertex."

## 1. Trigger

- **Type**: `corporate_policy_change`
- **Actor**: `ENS_LABS`
- **Timestamp**: `2022-08-08 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`supporting_journalism`**
  - URL: <https://www.trustnodes.com/2022/08/09/torn-token-dives-as-us-bans-a-smart-contract>
  - Wayback: <https://web.archive.org/web/2022/https://www.trustnodes.com/2022/08/09/torn-token-dives-as-us-bans-a-smart-contract>
  > Trustnodes (2022-08-09) "Torn Token Dives as US Bans a Smart
> Contract, ENS Domain Goes Offline". Headline-level reference to
> an ENS-domain artefact appearing offline in the immediate
> aftermath of the 2022-08-08 OFAC SDN designation. The Trustnodes
> headline refers to the tornado.cash web (DNS) domain captured
> under tornado-cash-tornadocash-org-seizure-2022, not to an
> ENS-protocol-level action on the tornadocash.eth name. Cited
> here as the closest journalistic claim that touches the
> ENS-domain question and as a negative-result anchor: no source
> in the search corpus documents an ENS-protocol or ENS Labs
> frontend (app.ens.domains) action to block resolution,
> transfer, or management of the tornadocash.eth name or
> sub-names following the OFAC SDN designation. DRYRUN: pinned
> Wayback snapshot deferred to human audit.
- **`semi_primary_wayback`**
  - URL: <https://app.ens.domains/tornadocash.eth>
  - Wayback: <https://web.archive.org/web/2022/https://app.ens.domains/tornadocash.eth>
  - body_hash: `sha256:62b82633fa1b228a7ab2e2dcbc3c44b67af6ced6e68810fec347fea1532406f8`
  - body_path: `sources/http_captures/ens-eth-domain-tornado-resolution-2022/v0_3_primary_repair/app.ens.domains__tornadocash.eth__f16003fa65.html`
  > ENS Labs official frontend (app.ens.domains) name-detail page
> for tornadocash.eth. Cited as the canonical artefact whose
> post-2022-08-08 state would be the load-bearing observation if
> an ENS-Labs frontend action had occurred. As of the search
> evidence available, the name remains resolvable and the detail
> page remains rendered by app.ens.domains — i.e. no
> ENS-Labs-level UI block of tornadocash.eth is observed.
> Sub-name sources.tornadocash.eth and the .eth.limo gateway
> (tornadocash.eth.limo / sources.tornadocash.eth.limo) likewise
> continued to resolve. DRYRUN: pinned Wayback snapshot deferred
> to human audit.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: ENS (Ethereum Name Service) — tornadocash.eth name set
- **Chains**: `ethereum`
- **Canonical domains**: `tornadocash.eth`, `sources.tornadocash.eth`, `app.ens.domains`, `tornadocash.eth.limo`

> Hypothetical target set: the tornadocash.eth ENS name and its
> sub-names (sources.tornadocash.eth, docs.tornadocash.eth, etc.)
> that point at Tornado Cash distribution artefacts (IPFS content
> hashes hosting the dapp UI and source-code mirrors). subset
> because the full sub-name graph is not enumerated in any single
> primary source. The target is named here to make the
> null-event scope falsifiable: if an ENS-Labs frontend or
> ENS-DAO governance action had blocked resolution / transfer /
> management of these names, this is the name set it would have
> acted on.

## 3. Changed-layer observations (supports the scoped claim)

*No observed_change entries. This is a `null_event`; see §4 for observed_no_change evidence supporting the null claim.*

## 4. No-change observations (where applicable)

### l4_frontend — `ens_protocol_and_frontend_no_action_on_tornadocash_eth_after_ofac_sdn`

**Window**: `2022-08-08 00:00:00+00:00` → `2022-12-31 23:59:59+00:00`

**Sources**:

- **`semi_primary_wayback`**
  - URL: <https://app.ens.domains/tornadocash.eth>
  - Wayback: <https://web.archive.org/web/2022/https://app.ens.domains/tornadocash.eth>
  - body_hash: `sha256:62b82633fa1b228a7ab2e2dcbc3c44b67af6ced6e68810fec347fea1532406f8`
  - body_path: `sources/http_captures/ens-eth-domain-tornado-resolution-2022/v0_3_primary_repair/app.ens.domains__tornadocash.eth__f16003fa65.html`
  > ENS Labs official frontend (app.ens.domains) tornadocash.eth
> name-detail page remained rendered post-2022-08-08; no UI
> block, transfer freeze, or resolver override was observed.
> observed_no_change row supporting the null-event status.
> Current-state HTTP body was captured in v0.3 source repair;
> human audit should still replace the year-prefix Wayback with
> a timestamped 2022 snapshot before promotion.
- **`semi_primary_wayback`**
  - URL: <https://sources.tornadocash.eth.limo/>
  - Wayback: <https://web.archive.org/web/2022/https://sources.tornadocash.eth.limo/>
  - body_hash: `sha256:78782f9fc183a6149afdef6af622a525f0102720d99801092b0233345091dbd8`
  - body_path: `sources/http_captures/ens-eth-domain-tornado-resolution-2022/v0_3_primary_repair/sources.tornadocash.eth.limo__capture__961748b737.html`
  > sources.tornadocash.eth.limo — the eth.limo HTTPS gateway
> serving the Tornado Cash decentralized-sources surface via
> ENS content-hash resolution — continued to resolve after
> 2022-08-08, evidencing that neither the ENS protocol nor
> ENS Labs (nor the eth.limo gateway operator) imposed a
> resolution-layer block on the tornadocash.eth name set.
> Current-state HTTP body was captured in v0.3 source repair;
> human audit should still replace the year-prefix Wayback with
> a timestamped 2022 snapshot before promotion.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`tornado-cash-ofac-2022`](./tornado-cash-ofac-2022.md)
- [`tornado-cash-frontend-tornado-cash-eth-block-2022-04`](./tornado-cash-frontend-tornado-cash-eth-block-2022-04.md)
- [`tornado-cash-github-takedown-2022-08`](./tornado-cash-github-takedown-2022-08.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `6293bc1`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

