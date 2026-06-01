# Evidence chain — `uniswap-balancer-tornado-frontend-block-2022-08`

**Status**: `admitted` · **Stratum**: `S5_corporate` · **Shape**: `comparison` (1 changed layer(s): `l4_frontend`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-02` · **Source commit**: `fd81985` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-21` · **Tool version**: `0.1.0` · **Generated**: `2026-06-02T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "The 2022-08-12 Uniswap Labs and Balancer Labs frontend-
> screening blocks of TRM-Labs-flagged wallets (seeded by the
> 2022-08-08 OFAC Tornado Cash SDN address set) constitute a
> paired L4 frontend-operator corporate-policy-change event,
> with two named operators (Uniswap Labs, Balancer Labs)
> applying the block to their hosted UIs (app.uniswap.org,
> balancer.fi) while the underlying smart-contract protocols
> remain fully functional. The row does not claim OFAC-
> compelled action, ISP-level connectivity blocking,
> consensus-layer effect, or asset-layer freeze — those are
> sibling-event rows under tornado-cash-ofac-2022 / infura-
> alchemy-tornado-rpc-block-2022 / circle-usdc-tornado-2022."

## 1. Trigger

- **Type**: `corporate_policy_change`
- **Actor**: `uniswap_labs_and_balancer_labs`
- **Timestamp**: `2022-08-12 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`supporting_journalism`**
  - URL: <https://www.theblock.co/post/162680>
  - Wayback: <https://web.archive.org/web/2022/https://www.theblock.co/post/162680>
  > The Block contemporaneous coverage of the 2022-08-12 DeFi frontend
> cascade naming Uniswap Labs and Balancer Labs as having begun
> blocking Tornado-Cash-tainted addresses from app.uniswap.org and
> balancer.fi via TRM Labs API screening. Day-level timing anchor.
> DRYRUN: pinned Wayback snapshot and body_hash deferred to human
> audit; marked evidence_use=contextual_unarchived per validator
> policy for unarchived sources.
- **`supporting_journalism`**
  - URL: <https://www.coindesk.com/tech/2022/08/22/popular-uniswap-frontend-blocks-over-250-crypto-addresses-related-to-defi-crimes>
  - Wayback: <https://web.archive.org/web/2022/https://www.coindesk.com/tech/2022/08/22/popular-uniswap-frontend-blocks-over-250-crypto-addresses-related-to-defi-crimes>
  > CoinDesk retrospective coverage (2022-08-22) reporting that the
> Uniswap-Labs-operated frontend blocked 253 crypto addresses via
> the TRM Labs API across seven risk categories including Tornado
> Cash / privacy-mixer-tainted addresses, following the 2022-08-08
> OFAC SDN designation. Triangulation source for the TRM Labs
> integration mechanism. DRYRUN: pinned Wayback snapshot and
> body_hash deferred to human audit.
- **`supporting_journalism`**
  - URL: <https://blockworks.co/news/defi-web-apps-block-users-hit-by-tornado-cash-dust-attack>
  - Wayback: <https://web.archive.org/web/2022/https://blockworks.co/news/defi-web-apps-block-users-hit-by-tornado-cash-dust-attack>
  > Blockworks coverage of the DeFi-frontend cascade following the
> 2022-08-09 Tornado Cash "dust attack" (small ETH amounts sent
> from a Tornado pool to public-figure addresses, propagating the
> OFAC taint to bystanders). Names Aave, Uniswap, Balancer, dYdX
> as having activated frontend-block screening within days.
> Day-level timing triangulation. DRYRUN: pinned Wayback snapshot
> and body_hash deferred to human audit.
- **`supporting_journalism`**
  - URL: <https://thedefiant.io/news/defi/defi-bans-tornado-addresses>
  - Wayback: <https://web.archive.org/web/2022/https://thedefiant.io/news/defi/defi-bans-tornado-addresses>
  > The Defiant aggregator-level coverage of the growing DeFi
> frontend ban list for Tornado Cash-tainted addresses
> (mid-August 2022). Triangulation source for the cascade
> pattern across multiple DeFi frontends including
> balancer.fi. DRYRUN: pinned Wayback snapshot deferred to
> human audit.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Uniswap Labs (app.uniswap.org) and Balancer Labs (balancer.fi)
- **Chains**: `ethereum`
- **Canonical domains**: `app.uniswap.org`, `balancer.fi`

> The frontend block applies to addresses flagged by the TRM Labs
> risk-screening API across seven categories (sanctions, stolen
> funds, privacy mixers, terrorist wallets, CSAM-linked wallets,
> and other categories), with the 2022-08-08 OFAC Tornado Cash SDN
> address set forming the seed enforcement perimeter. By 2022-08-22
> (CoinDesk reporting) Uniswap Labs had blocked 253 addresses via
> the TRM Labs integration. The target is `entity` (not address_set)
> because the enforcement is a two-firm corporate-policy action
> against a moving TRM-flagged address universe rather than a
> fixed enumerated address list; the firms blocked are the named
> target. Subset because the TRM-flagged address universe is not
> publicly enumerated by either firm in real time, and the 253
> figure is a 2022-08-22 retrospective snapshot.

## 3. Changed-layer observations (supports the scoped claim)

### l4_frontend · attribution: `direct` · Δt = 0h

**Event label**: `uniswap_labs_trm_screening_block_of_tornado_tainted_addresses`

**Timestamp**: `2022-08-12 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_corporate`**
  - URL: <https://blog.uniswap.org/trm>
  - Wayback: <https://web.archive.org/web/20230330015248/https://blog.uniswap.org/trm>
  - body_hash: `sha256:97cbcdcf1912c8c37ea25ea4e4e09081e581b792e758e84ca4551c35926414e2`
  - body_path: `sources/http_captures/uniswap-balancer-tornado-frontend-block-2022-08/primary/web.archive.org__web-20220824000000-https-blog.uniswap.org-trm__6bc512d432.html`
  > Uniswap Labs official blog announcing TRM Labs wallet-screening
> at the app.uniswap.org frontend, blocking addresses flagged for
> Tornado-Cash/OFAC exposure. primary_corporate; attribution=direct.
> Wayback 20230330015248 pinned.
- **`semi_primary_wayback`**
  - URL: <https://www.theblock.co/post/143036/uniswap-labs-now-blocks-crypto-wallets-frontend>
  - Wayback: <https://web.archive.org/web/20220815231904/https://www.theblock.co/post/143036/uniswap-labs-now-blocks-crypto-wallets-frontend>
  - body_hash: `sha256:5f565d9df6ffe166766c152d4046138c4b026b965ef071055f92b1f4be52e1e9`
  - body_path: `sources/http_captures/uniswap-balancer-tornado-frontend-block-2022-08/primary/web.archive.org__web-20220824000000-https-www.theblock.co-post-143036-uniswap-labs-now-blocks-crypto-wallets-frontend__c337ab2c5e.html`
  > The Block 2022-08 coverage of Uniswap Labs frontend wallet
> blocking. Independent semi-primary anchor.

### l4_frontend · attribution: `plausible` · Δt = 0h

**Event label**: `balancer_labs_trm_screening_block_of_tornado_tainted_addresses`

**Timestamp**: `2022-08-12 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`semi_primary_wayback`**
  - URL: <https://cryptoslate.com/defi-protocols-aave-uniswap-balancer-ban-users-following-ofac-sanctions-on-tornado-cash/>
  - Wayback: <https://web.archive.org/web/20220822183816/https://cryptoslate.com/defi-protocols-aave-uniswap-balancer-ban-users-following-ofac-sanctions-on-tornado-cash/>
  - body_hash: `sha256:445e6b4735bf986668eeda286f43605db6d77772208bdbaee517c2b1086564d9`
  - body_path: `sources/http_captures/uniswap-balancer-tornado-frontend-block-2022-08/primary/web.archive.org__web-20220823000000-https-cryptoslate.com-defi-protocols-aave-uniswap-balancer-ban-users-following-ofac-sanctions-on-tornado-cash__172b99b064.html`
  > CryptoSlate 2022-08-22 coverage naming Balancer (alongside Aave,
> Uniswap) among the DeFi frontends restricting Tornado-tainted wallets.
> Semi-primary anchor for the Balancer leg.
- **`semi_primary_wayback`**
  - URL: <https://blockworks.co/news/defi-web-apps-block-users-hit-by-tornado-cash-dust-attack>
  - Wayback: <https://web.archive.org/web/20221121141935/https://blockworks.co/news/defi-web-apps-block-users-hit-by-tornado-cash-dust-attack>
  - body_hash: `sha256:7ea8212b396eca5a79b78ed6f9ff434089f02e7a5041169d3cb79b8d1be2c42a`
  - body_path: `sources/http_captures/uniswap-balancer-tornado-frontend-block-2022-08/primary/web.archive.org__web-20220823000000-https-blockworks.co-news-defi-web-apps-block-users-hit-by-tornado-cash-dust-attack__eb071a4a2e.html`
  > Blockworks coverage of DeFi web apps (incl. Balancer) blocking
> users hit by the Tornado-Cash dust attack. Independent second
> semi-primary anchor for the Balancer leg.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`tornado-cash-ofac-2022`](./tornado-cash-ofac-2022.md)
- [`infura-alchemy-tornado-rpc-block-2022`](./infura-alchemy-tornado-rpc-block-2022.md)
- [`aave-tornado-frontend-block-2022-08`](./aave-tornado-frontend-block-2022-08.md)
- [`circle-usdc-tornado-2022`](./circle-usdc-tornado-2022.md)
- [`uniswap-frontend-delisting-2023`](./uniswap-frontend-delisting-2023.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `fd81985`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

