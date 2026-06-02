# Evidence chain — `infura-alchemy-tornado-rpc-block-2022`

**Status**: `admitted` · **Stratum**: `S5_corporate` · **Shape**: `comparison` (1 changed layer(s): `l3_rpc`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-02` · **Source commit**: `84e7c21` · **Schema**: `0.2.0` · **Event last_verified**: `2026-06-01` · **Tool version**: `0.1.0` · **Generated**: `2026-06-02T00:04:45Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "On 2022-08-09, contemporaneous reporting stated that Infura and Alchemy
> were blocking Ethereum API access for Tornado Cash users through affected
> front-end paths after the 2022-08-08 OFAC designation. In this dataset the
> row is a one-layer S5 corporate l3_rpc/API observed_change with
> attribution=plausible and evidence_tier=attested_secondary; it does not
> claim provider-primary attribution, a complete RPC-network block, a fixed
> address-set block, L0/L1/asset/off-ramp effects, or a separately measured
> L4 frontend cascade."

## 1. Trigger

- **Type**: `corporate_policy_change`
- **Actor**: `infura_and_alchemy`
- **Timestamp**: `2022-08-09 11:41:30+00:00` (precision: `hour`)

### Trigger citations

- **`primary_corporate`**
  - URL: <https://infura.io/terms>
  > Current Infura / ConsenSys terms are retained only as corporate-policy
> context for sanctions-compliance screening by a managed Ethereum
> infrastructure provider. This URL is not used as a specific
> August-2022 Tornado Cash block anchor because no pinned historical
> provider-controlled revision is attached in this row.
- **`primary_corporate`**
  - URL: <https://docs.alchemy.com/reference/compliance-program>
  > Current Alchemy compliance documentation is retained only as
> corporate-policy context. This URL is not used as a specific
> August-2022 Tornado Cash block anchor because no pinned historical
> provider-controlled revision is attached in this row.
- **`supporting_journalism`**
  - URL: <https://www.theblock.co/post/162402/infura-and-alchemy-blocking-access-to-tornado-cash>
  - body_hash: `sha256:558d879c7918b26d44647717640d85a2da7b46fb7183755c2172c36cf5f6e385`
  - body_path: `sources/http_captures/infura-alchemy-tornado-rpc-block-2022/primary/www.theblock.co__post-162402-infura-and-alchemy-blocking-access-to-tornado-cash__96bfbc9227.html`
  > Captured The Block article published 2022-08-09 7:41AM EDT reports
> that Infura and Alchemy were blocking Ethereum API access for Tornado
> Cash users after the OFAC designation. The article is the load-bearing
> event-specific source for this lower-tier row; it is not a
> provider-controlled primary source.

## 2. Target

- **Kind**: `protocol`
- **Enumeration**: `subset`
- **Protocol**: `tornado_cash`
- **Actor name**: Infura (ConsenSys) and Alchemy Insights
- **Chains**: `ethereum`
- **Canonical domains**: `infura.io`, `alchemy.com`

> Tornado Cash users interacting through the Tornado Cash front-end path
> with Infura or Alchemy Ethereum API endpoints. The captured source says
> the restriction was limited to front-end code / API access and that direct
> command-line method calling remained possible. This row therefore does
> not claim a complete protocol block, a full RPC-network block, or a fixed
> provider-enumerated address set.

## 3. Changed-layer observations (supports the scoped claim)

### l3_rpc · attribution: `plausible` · Δt = 0h

**Event label**: `infura_alchemy_tornado_cash_api_access_block`

**Timestamp**: `2022-08-09 11:41:30+00:00` (precision: `hour`)

**Sources**:

- **`supporting_journalism`**
  - URL: <https://www.theblock.co/post/162402/infura-and-alchemy-blocking-access-to-tornado-cash>
  - body_hash: `sha256:558d879c7918b26d44647717640d85a2da7b46fb7183755c2172c36cf5f6e385`
  - body_path: `sources/http_captures/infura-alchemy-tornado-rpc-block-2022/primary/www.theblock.co__post-162402-infura-and-alchemy-blocking-access-to-tornado-cash__96bfbc9227.html`
  > The captured article states that Infura and Alchemy were blocking
> Ethereum API access for Tornado Cash users and that users relying on
> Alchemy or Infura endpoints were unable to use the privacy service
> through the affected front-end path. attribution=plausible because
> the retained source is contemporaneous journalism, not a
> provider-controlled block notice or a replayed RPC/API rejection.

## 5. Honest coverage gaps

- **l4_frontend** (`not_measured`): The captured article describes the restriction as operating through

## 7. Related events

- [`tornado-cash-ofac-2022`](./tornado-cash-ofac-2022.md)
- [`tornado-cash-ofac-delisting-2025`](./tornado-cash-ofac-delisting-2025.md)
- [`circle-usdc-tornado-2022`](./circle-usdc-tornado-2022.md)
- [`metamask-eth-phishing-detect-tornado-additions-2022`](./metamask-eth-phishing-detect-tornado-additions-2022.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `84e7c21`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

