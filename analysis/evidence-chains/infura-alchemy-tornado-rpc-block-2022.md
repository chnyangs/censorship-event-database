# Evidence chain — `infura-alchemy-tornado-rpc-block-2022`

**Status**: `admitted` · **Stratum**: `S5_corporate` · **Shape**: `comparison` (2 changed layer(s): `l3_rpc`, `l4_frontend`) · **Tier**: `anchor_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `9e851fb` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-16` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "The 2022-08-09 Infura and Alchemy RPC-provider blocks of requests
> touching the 2022-08-08 OFAC Tornado Cash SDN address set constitute
> the first documented L3 RPC-provider sanctions block in the corpus,
> with two named providers' own corporate-policy statements
> (attribution=direct) and a downstream L4 wallet/aggregator UI
> cascade (attribution=plausible, via Infura's MetaMask-default-RPC
> position). The row does not claim ISP-level connectivity blocking,
> consensus-layer (PBS) effect, on-chain asset freeze, or off-ramp
> severance — those are sibling-event rows under tornado-cash-ofac-2022
> / circle-usdc-tornado-2022."

## 1. Trigger

- **Type**: `corporate_policy_change`
- **Actor**: `consensys_infura`
- **Timestamp**: `2022-08-09 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_corporate`**
  - URL: <https://infura.io/terms>
  - Wayback: <https://web.archive.org/web/2022/https://infura.io/terms>
  > Infura (ConsenSys-operated managed-Ethereum-RPC service) updated its
> Terms of Service in August 2022 to assert OFAC-compliance screening
> of RPC requests touching sanctioned addresses; the Tornado Cash
> contract set (per the 2022-08-08 SDN designation, see related event
> tornado-cash-ofac-2022) was the first concrete enforcement target.
> Wayback anchor is a 2022 calendar-folder pointer at infura.io/terms
> rather than a pinned snapshot of the ToS revision; the exact
> revision URL and snapshot timestamp must be re-pinned during human
> audit before this citation may serve as an admission anchor in its
> own right. Marked evidence_use=contextual_unarchived per validator
> policy for unarchived sources.
- **`primary_corporate`**
  - URL: <https://docs.alchemy.com/reference/compliance-program>
  - Wayback: <https://web.archive.org/web/2022/https://docs.alchemy.com/reference/compliance-program>
  > Alchemy Insights support / docs page describing the firm's
> OFAC-compliance screening of managed-RPC requests. Alchemy
> independently confirmed (via support article and customer
> communications, August 2022) that RPC requests targeting the
> 2022-08-08 OFAC Tornado Cash address set would be rejected.
> Wayback anchor is a 2022 calendar-folder pointer; the exact
> revision URL and snapshot timestamp must be re-pinned during
> human audit. Marked evidence_use=contextual_unarchived.
- **`supporting_journalism`**
  - URL: <https://cointelegraph.com/news/infura-blocks-some-areas-from-accessing-ethereum-and-its-testnets>
  - Wayback: <https://web.archive.org/web/2022/https://cointelegraph.com/news/infura-blocks-some-areas-from-accessing-ethereum-and-its-testnets>
  > Cointelegraph contemporaneous coverage of the Infura RPC block
> of Tornado-related requests (August 2022). Triangulation source
> for the day-level timing; not primary. Marked
> evidence_use=contextual_unarchived pending human-audit Wayback pin.
- **`supporting_journalism`**
  - URL: <https://www.theblock.co/post/162680>
  - Wayback: <https://web.archive.org/web/2022/https://www.theblock.co/post/162680>
  > The Block contemporaneous coverage of the joint Infura/Alchemy
> RPC-provider response to the 2022-08-08 Tornado Cash OFAC
> designation. Triangulation source. Marked
> evidence_use=contextual_unarchived pending human-audit Wayback pin.

## 2. Target

- **Kind**: `address_set`
- **Enumeration**: `subset`
- **Protocol**: `tornado_cash`
- **Actor name**: Infura (ConsenSys) and Alchemy Insights
- **Chains**: `ethereum`
- **Addresses**: 8 total (enumerated in event YAML)
- **Canonical domains**: `infura.io`, `alchemy.com`

> Infura and Alchemy applied OFAC-screening filters to RPC requests
> touching the 2022-08-08 Tornado Cash SDN address set (the 38
> Ethereum addresses enumerated under tornado-cash-ofac-2022 /
> target.addresses). This target is the same address universe as the
> OFAC trigger event but the L3 enforcement perimeter is a subset
> because (a) the corporate-policy statements did not enumerate the
> addresses verbatim and (b) the operational block was implemented
> against the SDN list as a moving reference, not a fixed snapshot.
> The flashbots/rpc-endpoint server/ofacblacklist.go commit
> 92ab6b1f (Tornado Cash address additions, see
> tornado-cash-ofac-2022 observations[l3_rpc]) is treated here as
> the canonical address-list reference for the same enforcement
> perimeter applied by Infura and Alchemy; the eight anchor pool
> addresses are listed below as the addresses Infura/Alchemy
> statements demonstrably blocked.

## 3. Changed-layer observations (supports the scoped claim)

### l3_rpc · attribution: `direct` · Δt = 0h

**Event label**: `infura_rpc_block_of_tornado_cash_sdn_addresses`

**Timestamp**: `2022-08-09 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_corporate`**
  - URL: <https://infura.io/terms>
  - Wayback: <https://web.archive.org/web/2022/https://infura.io/terms>
  > Infura (ConsenSys) Terms of Service update of August 2022 is
> the canonical corporate-policy statement of the OFAC-screening
> policy applied to managed-RPC requests touching sanctioned
> addresses. attribution=direct because the corporate-policy
> source is the operator naming the action; the Tornado Cash
> SDN set (per tornado-cash-ofac-2022) is the documented first
> enforcement perimeter. DRYRUN: pinned Wayback snapshot and
> body_hash for the specific ToS revision are deferred to the
> human-audit pass; marked evidence_use=contextual_unarchived
> per validator policy.
- **`supporting_journalism`**
  - URL: <https://cointelegraph.com/news/infura-blocks-some-areas-from-accessing-ethereum-and-its-testnets>
  - Wayback: <https://web.archive.org/web/2022/https://cointelegraph.com/news/infura-blocks-some-areas-from-accessing-ethereum-and-its-testnets>
  > Cointelegraph contemporaneous coverage of the Infura RPC block,
> retained for day-level timing triangulation. DRYRUN: pinned
> Wayback snapshot deferred to human audit.

### l3_rpc · attribution: `direct` · Δt = 0h

**Event label**: `alchemy_rpc_block_of_tornado_cash_sdn_addresses`

**Timestamp**: `2022-08-09 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_corporate`**
  - URL: <https://docs.alchemy.com/reference/compliance-program>
  - Wayback: <https://web.archive.org/web/2022/https://docs.alchemy.com/reference/compliance-program>
  > Alchemy Insights support / docs page describing the firm's
> OFAC-compliance screening of managed-RPC requests, with the
> 2022-08-08 OFAC Tornado Cash address set as the first
> enforcement perimeter. attribution=direct because the source
> is Alchemy's own corporate-policy statement naming the action.
> DRYRUN: pinned Wayback snapshot and body_hash for the specific
> revision are deferred to the human-audit pass; marked
> evidence_use=contextual_unarchived per validator policy.
- **`supporting_journalism`**
  - URL: <https://www.theblock.co/post/162680>
  - Wayback: <https://web.archive.org/web/2022/https://www.theblock.co/post/162680>
  > The Block contemporaneous coverage of the joint Infura/Alchemy
> RPC-provider response, retained for triangulation. DRYRUN:
> pinned Wayback snapshot deferred to human audit.

### l4_frontend · attribution: `plausible` · Δt = 24h

**Event label**: `downstream_wallet_and_aggregator_ui_broke_for_tornado_interactions`

**Timestamp**: `2022-08-10 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_corporate`**
  - URL: <https://infura.io/terms>
  - Wayback: <https://web.archive.org/web/2022/https://infura.io/terms>
  > Infura ToS update is the upstream corporate-policy anchor for
> the downstream L4 cascade: MetaMask (using Infura as default
> Ethereum RPC) and aggregator UIs surfaced broken Tornado
> interactions in the same window. attribution=plausible
> because the L4 effect is a downstream consequence of the L3
> block rather than an independent frontend-operator policy
> decision, and no first-party MetaMask/aggregator corporate
> statement in-this-event explicitly names Tornado Cash as the
> reason for the user-facing breakage. DRYRUN: pinned Wayback
> snapshot and body_hash deferred to human audit.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`tornado-cash-ofac-2022`](./tornado-cash-ofac-2022.md)
- [`tornado-cash-ofac-delisting-2025`](./tornado-cash-ofac-delisting-2025.md)
- [`circle-usdc-tornado-2022`](./circle-usdc-tornado-2022.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `9e851fb`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

