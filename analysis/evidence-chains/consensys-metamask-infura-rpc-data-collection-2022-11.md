# Evidence chain — `consensys-metamask-infura-rpc-data-collection-2022-11`

**Status**: `admitted` · **Stratum**: `S5_corporate` · **Shape**: `null_event` (0 changed layer(s): none) · **Tier**: `null_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `96a9483` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-21` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "On 2022-11-23 ConsenSys updated the MetaMask privacy policy to
> publicly disclose that Infura, when used as the MetaMask default
> RPC provider, collects user IP addresses and Ethereum wallet
> addresses on every RPC request. This is a disclosure of pre-
> existing data-collection practice rather than a behavioral
> cutover at the L3 RPC layer; no new availability filter, address-
> set screen, or IP-geographic block is introduced. The single
> recorded observation is an observed_no_change row at L3 with
> attribution=none. The row does not claim any L0/L1/L4/asset/off-
> ramp cascade."

## 1. Trigger

- **Type**: `corporate_policy_change`
- **Actor**: `CONSENSYS_INC`
- **Timestamp**: `2022-11-23 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_corporate`**
  - URL: <https://consensys.io/privacy-policy>
  - Wayback: <https://web.archive.org/web/2022/https://consensys.io/privacy-policy>
  > ConsenSys privacy policy revision dated 2022-11-23 disclosing
> that when a MetaMask user uses Infura as the default RPC
> provider, Infura will collect the user's IP address and the
> Ethereum wallet address whenever the user makes a transaction.
> The disclosure is explicitly framed as a transparency update
> about a pre-existing data-collection practice rather than an
> introduction of a new collection. Wayback anchor is a 2022
> calendar-folder pointer rather than a pinned snapshot of the
> specific revision; pinned snapshot and body_hash are deferred
> to the human-audit pass. Marked
> evidence_use=contextual_unarchived per validator policy for
> unarchived sources.
- **`supporting_journalism`**
  - URL: <https://www.theblock.co/post/189717/consensys-says-it-collects-ip-addresses-of-metamask-users-via-infura>
  - Wayback: <https://web.archive.org/web/20221124110546/https://www.theblock.co/post/189717/consensys-says-it-collects-ip-addresses-of-metamask-users-via-infura>
  - body_hash: `sha256:9e7e1de2017082950f81267d77f69693828cc587d3b226ba018e6f039245c8fb`
  - body_path: `sources/http_captures/consensys-metamask-infura-rpc-data-collection-2022-11/primary/web.archive.org__web-20221124110546-https-www.theblock.co-post-189717-consensys-says-it-collects-ip-addresses-of-metamask-users-via-infura__bb63c07635.html`
  > The Block contemporaneous coverage of the 2022-11-23 ConsenSys
> privacy-policy update disclosing Infura IP+wallet-address
> collection. Day-level timing triangulation. DRYRUN: pinned
> Wayback snapshot deferred to human audit.
- **`supporting_journalism`**
  - URL: <https://decrypt.co/115486/infura-collect-metamask-users-ip-ethereum-addresses-after-privacy-policy-update>
  - Wayback: <https://web.archive.org/web/2022/https://decrypt.co/115486/infura-collect-metamask-users-ip-ethereum-addresses-after-privacy-policy-update>
  > Decrypt contemporaneous coverage of the same ConsenSys
> privacy-policy revision, noting the opt-out path (use a
> self-hosted node or third-party RPC) by which the IP and
> Ethereum-address collection can be avoided. Triangulation
> source. DRYRUN: pinned Wayback snapshot deferred to human
> audit.
- **`supporting_journalism`**
  - URL: <https://cryptoslate.com/consensys-updates-policy-to-collect-metamask-ip-data/>
  - Wayback: <https://web.archive.org/web/2022/https://cryptoslate.com/consensys-updates-policy-to-collect-metamask-ip-data/>
  > CryptoSlate contemporaneous coverage of the ConsenSys privacy-
> policy update, retained for community-reaction context (the
> wallet-user concern about RPC-layer surveillance). DRYRUN:
> pinned Wayback snapshot deferred to human audit.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: MetaMask end-users using Infura as default RPC provider
- **Chains**: `ethereum`
- **Canonical domains**: `infura.io`, `metamask.io`

> The disclosure addresses the class of MetaMask end-users who use
> Infura as the default RPC provider — i.e., the dominant default-
> configuration MetaMask population that has not opted into a
> self-hosted Ethereum node or a third-party RPC endpoint.
> enumeration=subset because (a) the corporate-policy statement
> addresses the user class collectively rather than enumerating
> specific user accounts and (b) the opt-out path (self-hosted
> node or third-party RPC) carves a documented exclusion from
> the collection perimeter.

## 3. Changed-layer observations (supports the scoped claim)

*No observed_change entries. This is a `null_event`; see §4 for observed_no_change evidence supporting the null claim.*

## 4. No-change observations (where applicable)

### l3_rpc — `privacy_policy_disclosure_of_preexisting_ip_and_ethereum_address_collection`

**Window**: `2022-11-23 00:00:00+00:00` → `2023-02-23 00:00:00+00:00`

**Sources**:

- **`primary_corporate`**
  - URL: <https://consensys.io/privacy-policy>
  - Wayback: <https://web.archive.org/web/2022/https://consensys.io/privacy-policy>
  > ConsenSys privacy-policy revision of 2022-11-23 disclosing
> that Infura (the MetaMask default RPC provider) collects
> user IP and Ethereum wallet addresses on every RPC request.
> observation_kind=observed_no_change with attribution=none
> because the policy revision discloses a pre-existing data-
> collection practice rather than introducing a new
> behavioral cutover at the RPC layer; no observable
> availability cascade or new filter is triggered by the
> disclosure itself. The opt-out path (self-hosted Ethereum
> node or third-party RPC endpoint) is named in the policy
> text. Codebook §1.1: attribution=none is reserved for
> observed_no_change rows; codebook §3: 0 observed_change
> layers → empirical_shape=null_event. DRYRUN: pinned
> Wayback snapshot and body_hash for the specific 2022-11-23
> revision are deferred to human audit; marked
> evidence_use=contextual_unarchived per validator policy.
- **`supporting_journalism`**
  - URL: <https://www.theblock.co/post/189717/consensys-says-it-collects-ip-addresses-of-metamask-users-via-infura>
  - Wayback: <https://web.archive.org/web/20221124110546/https://www.theblock.co/post/189717/consensys-says-it-collects-ip-addresses-of-metamask-users-via-infura>
  - body_hash: `sha256:9e7e1de2017082950f81267d77f69693828cc587d3b226ba018e6f039245c8fb`
  - body_path: `sources/http_captures/consensys-metamask-infura-rpc-data-collection-2022-11/primary/web.archive.org__web-20221124110546-https-www.theblock.co-post-189717-consensys-says-it-collects-ip-addresses-of-metamask-users-via-infura__bb63c07635.html`
  > The Block contemporaneous coverage (2022-11-24) of the
> ConsenSys privacy-policy disclosure, retained for day-level
> timing triangulation and for the framing that the
> disclosure is a transparency update about pre-existing
> collection rather than a new collection practice. DRYRUN:
> pinned Wayback snapshot deferred to human audit.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`infura-alchemy-tornado-rpc-block-2022`](./infura-alchemy-tornado-rpc-block-2022.md)
- [`infura-metamask-donetsk-luhansk-block-2022-03`](./infura-metamask-donetsk-luhansk-block-2022-03.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `96a9483`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

