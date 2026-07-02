# Evidence chain — `uniswap-labs-trm-address-screening-2022-04`

**Status**: `admitted` · **Stratum**: `S5_corporate` · **Shape**: `comparison` (1 changed layer(s): `l4_frontend`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-08` · **Source commit**: `ee7bf1a` · **Schema**: `0.2.0` · **Event last_verified**: `2026-06-05` · **Tool version**: `0.1.0` · **Generated**: `2026-06-25T23:48:26Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "Uniswap Labs' 2022-04-19 Address Screening Update documents an
> L4-only corporate-policy change: the Uniswap Labs App blocked wallet
> addresses associated with illicit activity, using TRM Labs screening,
> while the underlying Uniswap Protocol remained reachable through other
> portals or direct contract interaction. The row does not claim a
> 2022-08-12 Tornado-specific Uniswap action, a Balancer Labs action,
> network/RPC censorship, consensus-layer effect, asset freeze, or CEX
> off-ramp restriction."

## 1. Trigger

- **Type**: `corporate_policy_change`
- **Actor**: `uniswap_labs`
- **Timestamp**: `2022-04-19 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_corporate`**
  - URL: <https://blog.uniswap.org/trm>
  - Wayback: <https://web.archive.org/web/20230330015248/https://blog.uniswap.org/trm>
  - body_hash: `sha256:97cbcdcf1912c8c37ea25ea4e4e09081e581b792e758e84ca4551c35926414e2`
  - body_path: `sources/http_captures/uniswap-labs-trm-address-screening-2022-04/primary/web.archive.org__web-20220824000000-https-blog.uniswap.org-trm__6bc512d432.html`
  > Uniswap Labs official "Address Screening Update" blog post, dated
> 2022-04-19 in the captured page. The post states that the Uniswap
> Labs App had long blocked addresses on the OFAC sanctions list and
> that, with TRM Labs, Uniswap Labs was now blocking wallet addresses
> associated with illicit activity from interacting with the Uniswap
> Labs App. It also states that Uniswap Labs does not control user
> access to the Uniswap Protocol through any portal other than its own
> app. Primary corporate trigger and mechanism anchor.
- **`semi_primary_wayback`**
  - URL: <https://www.theblock.co/post/143036/uniswap-labs-now-blocks-crypto-wallets-frontend>
  - Wayback: <https://web.archive.org/web/20220815231904/https://www.theblock.co/post/143036/uniswap-labs-now-blocks-crypto-wallets-frontend>
  - body_hash: `sha256:5f565d9df6ffe166766c152d4046138c4b026b965ef071055f92b1f4be52e1e9`
  - body_path: `sources/http_captures/uniswap-labs-trm-address-screening-2022-04/primary/web.archive.org__web-20220824000000-https-www.theblock.co-post-143036-uniswap-labs-now-blocks-crypto-wallets-frontend__c337ab2c5e.html`
  > The Block article published 2022-04-22, captured in a 2022 Wayback
> memento, reporting that Uniswap Labs had begun blocking crypto
> wallet addresses found to be engaged in illegal activity from the
> app frontend; it identifies the TRM Labs partnership, risk
> categories including sanctions and stolen funds, and the
> frontend/protocol split. Used as contemporaneous corroboration for
> the day-level Uniswap Labs address-screening rollout.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Uniswap Labs (app.uniswap.org)
- **Chains**: `ethereum`
- **Canonical domains**: `app.uniswap.org`

> The target is the Uniswap Labs App wallet-screening perimeter:
> addresses flagged by TRM Labs risk intelligence and addresses already
> on the OFAC sanctions list. The exact moving address universe is not
> publicly enumerated by Uniswap Labs, so the target remains `entity`
> rather than a fixed address_set and enumeration is `subset`.

## 3. Changed-layer observations (supports the scoped claim)

### l4_frontend · attribution: `direct` · Δt = 0h

**Event label**: `uniswap_labs_trm_screening_block_of_illicit_wallets`

**Timestamp**: `2022-04-19 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_corporate`**
  - URL: <https://blog.uniswap.org/trm>
  - Wayback: <https://web.archive.org/web/20230330015248/https://blog.uniswap.org/trm>
  - body_hash: `sha256:97cbcdcf1912c8c37ea25ea4e4e09081e581b792e758e84ca4551c35926414e2`
  - body_path: `sources/http_captures/uniswap-labs-trm-address-screening-2022-04/primary/web.archive.org__web-20220824000000-https-blog.uniswap.org-trm__6bc512d432.html`
  > Uniswap Labs' own post records the app-level block: with TRM Labs,
> wallet addresses associated with illicit activity were blocked from
> interacting with the Uniswap Labs App. attribution=direct for the
> Uniswap Labs frontend policy and mechanism.
- **`semi_primary_wayback`**
  - URL: <https://www.theblock.co/post/143036/uniswap-labs-now-blocks-crypto-wallets-frontend>
  - Wayback: <https://web.archive.org/web/20220815231904/https://www.theblock.co/post/143036/uniswap-labs-now-blocks-crypto-wallets-frontend>
  - body_hash: `sha256:5f565d9df6ffe166766c152d4046138c4b026b965ef071055f92b1f4be52e1e9`
  - body_path: `sources/http_captures/uniswap-labs-trm-address-screening-2022-04/primary/web.archive.org__web-20220824000000-https-www.theblock.co-post-143036-uniswap-labs-now-blocks-crypto-wallets-frontend__c337ab2c5e.html`
  > The Block 2022-04-22 corroborates that Uniswap Labs had begun
> blocking crypto wallet addresses from the app frontend, identifies
> the TRM Labs partnership, and states that the Uniswap Protocol
> remained usable through alternative hosted websites or direct
> protocol interaction.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`tornado-cash-frontend-tornado-cash-eth-block-2022-04`](./tornado-cash-frontend-tornado-cash-eth-block-2022-04.md)
- [`aave-tornado-frontend-block-2022-08`](./aave-tornado-frontend-block-2022-08.md)
- [`uniswap-frontend-delisting-2023`](./uniswap-frontend-delisting-2023.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `ee7bf1a`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

