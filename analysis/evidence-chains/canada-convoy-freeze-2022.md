# Evidence chain — `canada-convoy-freeze-2022`

**Status**: `admitted` · **Stratum**: `S4_nation_state` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-10` · **Dataset cutoff**: `2026-05-16` · **Source commit**: `36d266a` · **Schema**: `0.2.0` · **Event last_verified**: `2026-04-22` · **Tool version**: `0.1.0` · **Generated**: `2026-05-24T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "Canada's 2022-02-14 invocation of the Emergencies Act produced the first
> G7 nation-state-level crypto freeze in the dataset, directing Canadian
> regulated crypto exchanges to freeze approximately 253 BTC wallet addresses
> tied to Freedom Convoy funding. The freeze was implemented through private
> RCMP-to-institution circulars rather than a public SDN list, demonstrating
> a non-OFAC-style enforcement mode."

## 1. Trigger

- **Type**: `nation_state_block`
- **Actor**: `CA_Government`
- **Timestamp**: `2022-02-14 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://gazette.gc.ca/rp-pr/p2/2022/2022-02-16-x1/html/sor-dors21-eng.html>
  - body_hash: `sha256:fac09fbd776f03ca74a2a6fbafe17f46caa346a89980ca75e44b1aca40dd9d02`
  - body_path: `sources/http_captures/canada-convoy-freeze-2022/primary/canadagazette.gc.ca__rp-pr-p2-2022-2022-02-16-x1-html-sor-dors21-eng.html__798548451d.html`
  > Canada Gazette Part II, "Emergency Economic Measures Order" SOR/2022-21
> (published 2022-02-16 for effective date 2022-02-15, invoked under the
> Emergencies Act on 2022-02-14 by Prime Minister Trudeau in response to
> the "Freedom Convoy" protests). Order authorized Canadian financial
> service providers (including crypto exchanges) to freeze accounts of
> "designated persons" without court order, including wallet addresses
> tied to convoy funding. First invocation of Emergencies Act since its
> 1988 successor statute to the War Measures Act. Effective for 9 days until
> revocation 2022-02-23.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Freedom Convoy funding network
- **Chains**: `bitcoin`

> ~250+ wallet addresses (approx 253 Bitcoin addresses per RCMP disclosure)
> tied to convoy-funding entities. Not enumerated on the primary legal
> source (Canada Gazette); RCMP issued circulars to banks and crypto
> exchanges with the address list, but those circulars are not public.
> Entity-level targeting (convoy-associated natural/corporate persons) with
> downstream on-chain address propagation via private banker-exchange
> channels.

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `direct` · Δt = 24.0h

**Event label**: `canadian_regulated_exchanges_frozen_convoy_addresses`

**Timestamp**: `2022-02-15 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_legal`**
  - URL: <https://gazette.gc.ca/rp-pr/p2/2022/2022-02-16-x1/html/sor-dors21-eng.html>
  - body_hash: `sha256:fac09fbd776f03ca74a2a6fbafe17f46caa346a89980ca75e44b1aca40dd9d02`
  - body_path: `sources/http_captures/canada-convoy-freeze-2022/primary/canadagazette.gc.ca__rp-pr-p2-2022-2022-02-16-x1-html-sor-dors21-eng.html__798548451d.html`
  > Emergency Economic Measures Order §4 explicitly directs all Canadian
> financial service providers (including "entities engaged in virtual
> currency transactions") to cease dealings with designated persons
> and freeze their property. Regulated Canadian crypto exchanges
> (Bitbuy, Wealthsimple Crypto, Netcoins, Newton) confirmed compliance
> within 24h. Direct attribution: the Order names the compliance
> requirement and designates virtual-currency service providers as
> in-scope.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-10` (commit `36d266a`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

