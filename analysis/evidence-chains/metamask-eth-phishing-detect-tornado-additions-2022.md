# Evidence chain — `metamask-eth-phishing-detect-tornado-additions-2022`

**Status**: `admitted` · **Stratum**: `S5_corporate` · **Shape**: `comparison` (1 changed layer(s): `l4_frontend`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `661a63f` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-17` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "ConsenSys / MetaMask's 2022-08-12 (DRYRUN-estimated)
> extension of the public eth-phishing-detect blocklist
> (consumed by the MetaMask wallet UI to surface phishing / risk
> warnings) with Tornado Cash interaction entries — following
> the 2022-08-08 OFAC SDN designation of Tornado Cash (related
> event tornado-cash-ofac-2022) — documents an L4 wallet-UI
> warning-layer corporate-compliance action distinct from the
> L3 Infura RPC block (related event
> infura-alchemy-tornado-rpc-block-2022). Paper-relevant as the
> wallet-UI warning-layer vertex of the ConsenSys-operated
> compliance stack (Infura RPC + MetaMask wallet UI) downstream
> of the 2022-08-08 OFAC trigger."

## 1. Trigger

- **Type**: `corporate_policy_change`
- **Actor**: `CONSENSYS_METAMASK`
- **Timestamp**: `2022-08-12 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_corporate`**
  - URL: <https://github.com/MetaMask/eth-phishing-detect>
  - Wayback: <https://web.archive.org/web/2022/https://github.com/MetaMask/eth-phishing-detect>
  > Canonical repository pointer for the ConsenSys / MetaMask
> `eth-phishing-detect` blocklist used by the MetaMask browser-
> extension wallet to surface phishing / risk warnings in the
> wallet UI. Following the 2022-08-08 OFAC SDN designation of
> Tornado Cash (related event tornado-cash-ofac-2022), the
> repository's blocklist was extended to include Tornado Cash
> interaction domains and address references as a wallet-UI
> warning-layer compliance step distinct from the L3
> Infura/Alchemy RPC block (related event
> infura-alchemy-tornado-rpc-block-2022). DRYRUN: pinned
> Wayback snapshot and body_hash for the specific
> commit/PR that added the Tornado Cash entries are deferred
> to the human-audit pass; the date 2022-08-12 is an LLM-
> estimated day-precision anchor consistent with the
> contemporaneous Tornado Cash compliance wave and MUST be
> replaced with the actual commit timestamp from the GitHub
> repository history during human audit. Marked
> evidence_use=contextual_unarchived per validator policy.
- **`supporting_journalism`**
  - URL: <https://www.coindesk.com/tech/2022/08/17/tornado-cash-fallout-can-ethereum-be-censored>
  - Wayback: <https://web.archive.org/web/2022/https://www.coindesk.com/tech/2022/08/17/tornado-cash-fallout-can-ethereum-be-censored>
  > CoinDesk contemporaneous coverage (2022-08-17) of the
> downstream cascade following the 2022-08-08 OFAC Tornado Cash
> SDN designation, including ConsenSys-operated wallet- and
> RPC-layer compliance actions. Triangulation source for the
> actor (ConsenSys / MetaMask) and the compliance window.
> DRYRUN: pinned Wayback snapshot deferred to human audit.
- **`supporting_journalism`**
  - URL: <https://davidgerard.co.uk/blockchain/2022/08/09/us-sanctions-tornado-cash-and-crypto-shrieks-in-horror/>
  - Wayback: <https://web.archive.org/web/2022/https://davidgerard.co.uk/blockchain/2022/08/09/us-sanctions-tornado-cash-and-crypto-shrieks-in-horror/>
  > David Gerard contemporaneous coverage (2022-08-09) of the
> broad-spectrum web3 compliance response to the 2022-08-08
> OFAC Tornado Cash designation, naming the MetaMask /
> ConsenSys wallet UI as one of the surfaces affected.
> DRYRUN: pinned Wayback snapshot deferred to human audit.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: ConsenSys / MetaMask (eth-phishing-detect blocklist maintainer)
- **Chains**: `ethereum`
- **Canonical domains**: `github.com/MetaMask/eth-phishing-detect`

> ConsenSys-operated MetaMask wallet UI (browser-extension and
> mobile) consumes the `eth-phishing-detect` blocklist
> (https://github.com/MetaMask/eth-phishing-detect) to surface
> phishing / risk warnings to end users. Following the 2022-08-08
> OFAC SDN designation of Tornado Cash (related event
> tornado-cash-ofac-2022), the blocklist was extended to include
> Tornado Cash interaction references. Target is the
> operator entity (ConsenSys / MetaMask wallet UI layer) rather
> than an enumerated address set because the blocklist is a
> moving reference maintained in a public GitHub repository, not
> a static published roster; subset because only the MetaMask-
> operated wallet UI warning layer is in scope here (this row is
> distinct from the L3 Infura RPC block under
> infura-alchemy-tornado-rpc-block-2022 and from the L3
> Donetsk/Luhansk Infura block under
> infura-metamask-donetsk-luhansk-block-2022-03).

## 3. Changed-layer observations (supports the scoped claim)

### l4_frontend · attribution: `plausible` · Δt = 0h

**Event label**: `metamask_eth_phishing_detect_blocklist_added_tornado_cash_interaction_entries`

**Timestamp**: `2022-08-12 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_corporate`**
  - URL: <https://github.com/MetaMask/eth-phishing-detect>
  - Wayback: <https://web.archive.org/web/20220905130930/https://github.com/MetaMask/eth-phishing-detect>
  - body_hash: `sha256:c31db18fe0de9bf2b1773b211fd425f3190e95e9ba48dab20e1684c8494dbb19`
  - body_path: `sources/http_captures/metamask-eth-phishing-detect-tornado-additions-2022/primary/web.archive.org__web-20220820000000-https-github.com-MetaMask-eth-phishing-detect__876c00a1f3.html`
  > MetaMask eth-phishing-detect open-source blocklist repository (the
> ConsenSys-maintained config that added Tornado-Cash-related domains/
> addresses to the wallet warning/blocklist). primary_corporate anchor.
> Wayback 20220905130930 pinned.
- **`semi_primary_wayback`**
  - URL: <https://www.coindesk.com/tech/2022/08/17/tornado-cash-fallout-can-ethereum-be-censored>
  - Wayback: <https://web.archive.org/web/20220817122318/https://www.coindesk.com/tech/2022/08/17/tornado-cash-fallout-can-ethereum-be-censored/>
  - body_hash: `sha256:eb14e16c338197232bb7a1ef02ae0ec7263a14a279d13c960b329603b9daf861`
  - body_path: `sources/http_captures/metamask-eth-phishing-detect-tornado-additions-2022/primary/web.archive.org__web-20220818000000-https-www.coindesk.com-tech-2022-08-17-tornado-cash-fallout-can-ethereum-be-censored__340cca4a5f.html`
  > CoinDesk 2022-08-17 analysis of the Tornado-Cash censorship fallout
> across the wallet/RPC/frontend stack. Independent semi-primary anchor.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`tornado-cash-ofac-2022`](./tornado-cash-ofac-2022.md)
- [`infura-metamask-donetsk-luhansk-block-2022-03`](./infura-metamask-donetsk-luhansk-block-2022-03.md)
- [`infura-alchemy-tornado-rpc-block-2022`](./infura-alchemy-tornado-rpc-block-2022.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `661a63f`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

