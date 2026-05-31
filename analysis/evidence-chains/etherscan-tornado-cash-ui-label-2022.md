# Evidence chain — `etherscan-tornado-cash-ui-label-2022`

**Status**: `admitted` · **Stratum**: `S5_corporate` · **Shape**: `comparison` (1 changed layer(s): `l4_frontend`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `3b37c3e` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-17` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "Etherscan's circa-2022-08-10 application of 'OFAC Blocked' /
> 'OFAC SDN' public nametags on the address-page headers of the
> OFAC-designated Tornado Cash contracts documents a UI / discovery-
> layer corporate-compliance action by the dominant Ethereum block-
> explorer operator downstream of the 2022-08-08 OFAC trigger
> (related event tornado-cash-ofac-2022). Paper-relevant as a
> third class of L4 frontend action — discovery-layer annotation
> rather than access-gating — that propagates the sanctions signal
> to the on-chain-discovery surface used by most users."

## 1. Trigger

- **Type**: `corporate_policy_change`
- **Actor**: `etherscan`
- **Timestamp**: `2022-08-10 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_corporate`**
  - URL: <https://etherscan.io/address/0x7ff9cfad3877f21d41da833e2f775db0569ee3d9>
  - Wayback: <https://web.archive.org/web/2022/https://etherscan.io/address/0x7ff9cfad3877f21d41da833e2f775db0569ee3d9>
  > Live Etherscan address page for the Tornado Cash 0.1 ETH pool
> contract (0x7Ff9...3D9), displaying the "OFAC Blocked"
> public-label nametag in the address header — the canonical
> artifact of Etherscan's UI-layer compliance label applied to
> OFAC-designated Tornado Cash contracts after the 2022-08-08
> OFAC SDN designation (see related event
> tornado-cash-ofac-2022). DRYRUN: pinned Wayback snapshot and
> body_hash deferred to human audit; marked
> evidence_use=contextual_unarchived per validator policy.
- **`primary_corporate`**
  - URL: <https://etherscan.io/address/0xa0e1c89ef1a489c9c7de96311ed5ce5d32c20e4b>
  - Wayback: <https://web.archive.org/web/2022/https://etherscan.io/address/0xa0e1c89ef1a489c9c7de96311ed5ce5d32c20e4b>
  > Live Etherscan address page for another OFAC-listed Tornado
> Cash contract (0xa0e1...E4B), also showing the "OFAC Blocked"
> nametag. Triangulation citation confirming Etherscan applied
> the label class-wide across the OFAC-listed Tornado Cash
> address universe rather than to a single contract. DRYRUN:
> pinned Wayback snapshot deferred to human audit.
- **`primary_corporate`**
  - URL: <https://info.etherscan.com/public-name-tags-labels/>
  - Wayback: <https://web.archive.org/web/2022/https://info.etherscan.com/public-name-tags-labels/>
  > Etherscan Information Center page describing the public
> name-tags / labels system that supports the OFAC label class
> applied at the UI layer. Documents the mechanism (operator-
> applied public nametag visible on the address page header)
> through which the Tornado Cash labels are surfaced. DRYRUN:
> pinned Wayback snapshot deferred to human audit.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Protocol**: `etherscan`
- **Actor name**: Etherscan (etherscan.io)
- **Chains**: `ethereum`
- **Canonical domains**: `etherscan.io`

> Etherscan (etherscan.io) is the dominant Ethereum block-explorer
> operator. After the 2022-08-08 OFAC SDN designation of Tornado
> Cash (see related event tornado-cash-ofac-2022), Etherscan
> applied "OFAC Blocked" / "OFAC SDN" public nametags on the
> address-page headers of the OFAC-listed Tornado Cash contracts,
> surfacing the sanctioned status to users browsing the addresses
> via the UI. The label is a UI/discovery-layer signal: it does
> not prevent on-chain interaction or RPC access; it warns users
> encountering the contract via the explorer. Target is the
> operator entity (Etherscan) rather than an enumerated address
> set because the label policy applies class-wide to the OFAC SDN
> list (Tornado Cash contracts are the in-scope subset for this
> event); subset because only the Etherscan-operated UI is in
> scope here (the underlying Tornado Cash smart contracts on-chain
> and other block explorers are out of scope).

## 3. Changed-layer observations (supports the scoped claim)

### l4_frontend · attribution: `direct` · Δt = 0h

**Event label**: `etherscan_applied_ofac_blocked_nametag_on_tornado_cash_contract_pages`

**Timestamp**: `2022-08-10 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_corporate`**
  - URL: <https://etherscan.io/address/0xa0e1c89ef1a489c9c7de96311ed5ce5d32c20e4b>
  - Wayback: <https://web.archive.org/web/20221011000838/https://etherscan.io/address/0xa0e1c89ef1a489c9c7de96311ed5ce5d32c20e4b>
  - body_hash: `sha256:d4fabeddcc224dac5f5c4a27288f8c83639a0cd8888d1e695e6fabdb5dd95dbe`
  - body_path: `sources/http_captures/etherscan-tornado-cash-ui-label-2022/primary/web.archive.org__web-20221101000000-https-etherscan.io-address-0xa0e1c89ef1a489c9c7de96311ed5ce5d32c20e4b__08a9651b65.html`
  > Etherscan address page for a Tornado-Cash-related address,
> 2022-10-11 snapshot showing the OFAC-sanctioned UI label applied at
> the Etherscan frontend. primary_corporate direct evidence of the UI
> label; attribution=direct. Wayback 20221011000838 pinned.
- **`primary_corporate`**
  - URL: <https://info.etherscan.com/public-name-tags-labels/>
  - Wayback: <https://web.archive.org/web/20220930202433/https://info.etherscan.com/public-name-tags-labels/>
  - body_hash: `sha256:cbcbc71fc222f13c54a5ae46c2f469336bd9c8b5846f9474e699864d025c5bac`
  - body_path: `sources/http_captures/etherscan-tornado-cash-ui-label-2022/primary/web.archive.org__web-20221001000000-https-info.etherscan.com-public-name-tags-labels__3000416fbc.html`
  > Etherscan public name-tags / labels documentation page describing
> the labeling system by which OFAC/SDN tags are applied. Corroborating
> primary_corporate anchor. Wayback 20220930202433 pinned.
- **`semi_primary_wayback`**
  - URL: <https://www.coindesk.com/tech/2022/08/17/tornado-cash-fallout-can-ethereum-be-censored>
  - Wayback: <https://web.archive.org/web/20220817122318/https://www.coindesk.com/tech/2022/08/17/tornado-cash-fallout-can-ethereum-be-censored/>
  - body_hash: `sha256:eb14e16c338197232bb7a1ef02ae0ec7263a14a279d13c960b329603b9daf861`
  - body_path: `sources/http_captures/etherscan-tornado-cash-ui-label-2022/primary/web.archive.org__web-20220818000000-https-www.coindesk.com-tech-2022-08-17-tornado-cash-fallout-can-ethereum-be-censored__340cca4a5f.html`
  > CoinDesk 2022-08-17 analysis of the Tornado-Cash censorship
> fallout. Independent semi-primary anchor.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`tornado-cash-ofac-2022`](./tornado-cash-ofac-2022.md)
- [`tornado-cash-frontend-tornado-cash-eth-block-2022-04`](./tornado-cash-frontend-tornado-cash-eth-block-2022-04.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `3b37c3e`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

