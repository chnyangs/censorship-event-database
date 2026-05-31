# Evidence chain — `cloudflare-ethereum-gateway-tornado-block-2022-08`

**Status**: `admitted` · **Stratum**: `S5_corporate` · **Shape**: `comparison` (1 changed layer(s): `l3_rpc`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `661a63f` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-21` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "The August 2022 Cloudflare Ethereum Gateway (cloudflare-eth.com)
> access restriction against the 2022-08-08 OFAC Tornado Cash SDN
> address set constitutes the CDN-gateway subtype of L3 censorship
> in the corpus — structurally distinct from the managed-RPC
> subtype (Infura, Alchemy, sibling event
> infura-alchemy-tornado-rpc-block-2022). The row does not claim
> ISP-level connectivity blocking, consensus-layer (PBS) effect,
> on-chain asset freeze, or off-ramp severance — those are sibling
> rows under tornado-cash-ofac-2022 / circle-usdc-tornado-2022."

## 1. Trigger

- **Type**: `corporate_policy_change`
- **Actor**: `cloudflare`
- **Timestamp**: `2022-08-12 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_corporate`**
  - URL: <https://blog.cloudflare.com/cloudflare-ethereum-gateway/>
  - Wayback: <https://web.archive.org/web/2022/https://blog.cloudflare.com/cloudflare-ethereum-gateway/>
  > Cloudflare blog post "Cloudflare's Ethereum Gateway" describes the
> cloudflare-eth.com Ethereum Gateway product (Cloudflare-Workers-fronted
> JSON-RPC + CDN cache for public Ethereum queries). Used here as the
> canonical operator-defined description of the perimeter that
> Cloudflare narrowed in August 2022 in response to the 2022-08-08
> OFAC Tornado Cash SDN designation. DRYRUN: pinned snapshot and
> body_hash for the specific August 2022 policy revision must be
> captured in human audit; marked evidence_use=contextual_unarchived.
- **`primary_corporate`**
  - URL: <https://www.cloudflare.com/transparency/>
  - Wayback: <https://web.archive.org/web/2023/https://www.cloudflare.com/transparency/>
  > Cloudflare Transparency Report H2 2022 (PDF on cf-assets domain)
> documents the Ethereum-Gateway access-restriction program: in
> 2H 2022 Cloudflare disabled access through its
> cloudflare-eth.com gateway to 99 items on the Ethereum network,
> explicitly framed as a response to the U.S. Treasury OFAC
> sanctions against Tornado Cash. Primary corporate disclosure of
> the gateway-level enforcement perimeter. DRYRUN: pinned PDF
> body_hash + body_path deferred to human audit; marked
> evidence_use=contextual_unarchived.
- **`supporting_journalism`**
  - URL: <https://www.coindesk.com/tech/2022/08/17/tornado-cash-fallout-can-ethereum-be-censored>
  - Wayback: <https://web.archive.org/web/2022/https://www.coindesk.com/tech/2022/08/17/tornado-cash-fallout-can-ethereum-be-censored>
  > CoinDesk contemporaneous coverage of the August 2022 OFAC
> Tornado Cash cascade across infrastructure operators, including
> the Cloudflare Ethereum Gateway response. Triangulation source
> for day-level timing. DRYRUN: pinned Wayback snapshot deferred
> to human audit; marked evidence_use=contextual_unarchived.
- **`supporting_journalism`**
  - URL: <https://torrentfreak.com/cloudflare-blocks-abusive-content-on-its-ethereum-gateway-231121/>
  - Wayback: <https://web.archive.org/web/2023/https://torrentfreak.com/cloudflare-blocks-abusive-content-on-its-ethereum-gateway-231121/>
  > TorrentFreak (2023-11-21) summarization of Cloudflare's H2 2022
> Transparency Report disclosure of the 99 Ethereum-Gateway items
> disabled in connection with the OFAC Tornado Cash sanctions.
> Retained for retroactive disclosure timing and the explicit
> quote from Cloudflare that the gateway restrictions are
> sanctions-driven. DRYRUN: pinned Wayback snapshot deferred to
> human audit; marked evidence_use=contextual_unarchived.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Cloudflare, Inc.
- **Chains**: `ethereum`
- **Canonical domains**: `cloudflare-eth.com`, `cloudflare.com`, `blog.cloudflare.com`

> Target is the Cloudflare Ethereum Gateway product (cloudflare-eth.com)
> as the entity whose corporate-policy change narrowed gateway access
> to the OFAC Tornado Cash SDN address set (per tornado-cash-ofac-2022
> target.addresses). Subset because the corporate disclosure does not
> enumerate the 99 blocked items verbatim and the operational block
> was implemented against the OFAC SDN list as a moving reference;
> the Tornado Cash address universe is the documented enforcement
> perimeter.

## 3. Changed-layer observations (supports the scoped claim)

### l3_rpc · attribution: `direct` · Δt = 0h

**Event label**: `cloudflare_ethereum_gateway_blocked_ofac_tornado_cash_addresses`

**Timestamp**: `2022-08-12 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_corporate`**
  - URL: <https://blog.cloudflare.com/cloudflare-ethereum-gateway/>
  - Wayback: <https://web.archive.org/web/20221108223358/https://blog.cloudflare.com/cloudflare-ethereum-gateway/>
  - body_hash: `sha256:76ab7b0289d3674f65c98ada320dc61700f4f5158cf278b1139b5ef4d545e0d0`
  - body_path: `sources/http_captures/cloudflare-ethereum-gateway-tornado-block-2022-08/primary/web.archive.org__web-20221122000000-https-blog.cloudflare.com-cloudflare-ethereum-gateway__74e43bbfd4.html`
  > Cloudflare official blog describing its Ethereum Gateway and the
> abuse/content-filtering policy applied to it (the substrate by which
> Tornado-Cash-related content is blocked at the RPC-gateway layer).
> primary_corporate anchor; attribution=direct. Wayback 20221108223358
> pinned.

## 5. Honest coverage gaps

- **l4_frontend** (`not_measured`): Cloudflare-fronted UIs that proxy JSON-RPC through the

## 7. Related events

- [`tornado-cash-ofac-2022`](./tornado-cash-ofac-2022.md)
- [`infura-alchemy-tornado-rpc-block-2022`](./infura-alchemy-tornado-rpc-block-2022.md)
- [`aave-tornado-frontend-block-2022-08`](./aave-tornado-frontend-block-2022-08.md)
- [`uniswap-balancer-tornado-frontend-block-2022-08`](./uniswap-balancer-tornado-frontend-block-2022-08.md)
- [`circle-usdc-tornado-2022`](./circle-usdc-tornado-2022.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `661a63f`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

