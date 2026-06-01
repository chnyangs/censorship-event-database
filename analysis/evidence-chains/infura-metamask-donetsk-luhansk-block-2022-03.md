# Evidence chain — `infura-metamask-donetsk-luhansk-block-2022-03`

**Status**: `admitted` · **Stratum**: `S5_corporate` · **Shape**: `comparison` (2 changed layer(s): `l3_rpc`, `l4_frontend`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-02` · **Source commit**: `3f1a9f2` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-21` · **Tool version**: `0.1.0` · **Generated**: `2026-06-02T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "The 2022-03-03 ConsenSys IP-geographic block at the Infura RPC
> endpoint layer and at the MetaMask wallet UI layer, applied to
> end-users in the Donetsk and Luhansk regions of Ukraine (plus
> the prior comprehensive-sanctions region set) in response to the
> 2022-02-21 EO 14065, constitutes the first documented S5_corporate
> IP-geo region-block in the corpus, with both L3 (RPC reachability)
> and L4 (wallet UI rendering) rows anchored on ConsenSys's own
> corporate statement (attribution=direct). The row does not claim
> ISP-level connectivity blocking, consensus-layer (PBS) effect,
> on-chain asset freeze, or off-ramp severance. The contemporaneous
> Venezuela/Iran over-block was a transient configuration error
> corrected within ~24h and is recorded as a recovery row on the
> L4 layer."

## 1. Trigger

- **Type**: `corporate_policy_change`
- **Actor**: `consensys_infura_metamask`
- **Timestamp**: `2022-03-03 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_corporate`**
  - URL: <https://consensys.net/blog/news/consensys-and-the-russia-ukraine-conflict/>
  - Wayback: <https://web.archive.org/web/2022/https://consensys.net/blog/news/consensys-and-the-russia-ukraine-conflict/>
  > ConsenSys blog statement of March 2022 describing its compliance
> posture in response to US sanctions arising from the Russia-Ukraine
> conflict, including the IP-geographic restrictions applied to
> Infura and MetaMask for the OFAC-comprehensively-sanctioned
> regions (Crimea, Donetsk, Luhansk) following the 2022-02-21
> Executive Order 14065. Wayback anchor is a 2022 calendar-folder
> pointer; pinned snapshot and body_hash are deferred to human
> audit. Marked evidence_use=contextual_unarchived per validator
> policy for unarchived sources.
- **`supporting_journalism`**
  - URL: <https://www.coindesk.com/policy/2022/03/03/metamask-infura-block-certain-areas-amid-crypto-sanctions-fury>
  - Wayback: <https://web.archive.org/web/2022/https://www.coindesk.com/policy/2022/03/03/metamask-infura-block-certain-areas-amid-crypto-sanctions-fury>
  > CoinDesk contemporaneous coverage (2022-03-03) of the
> Infura/MetaMask IP-geo block of the OFAC-comprehensively-sanctioned
> regions. Day-level timing triangulation source. DRYRUN: pinned
> Wayback snapshot deferred to human audit.
- **`supporting_journalism`**
  - URL: <https://www.coindesk.com/business/2022/03/04/crypto-industrys-sanctions-woes-on-full-display-in-metamasks-venezuela-hiccup>
  - Wayback: <https://web.archive.org/web/2022/https://www.coindesk.com/business/2022/03/04/crypto-industrys-sanctions-woes-on-full-display-in-metamasks-venezuela-hiccup>
  > CoinDesk follow-up coverage (2022-03-04) of the
> misconfiguration in which the IP-geo block applied too broadly
> and inadvertently captured Venezuelan users. Triangulation
> source for the over-blocking side-effect. DRYRUN: pinned
> Wayback snapshot deferred to human audit.
- **`supporting_journalism`**
  - URL: <https://decrypt.co/94315/ethereum-infura-cuts-off-users-separatist-areas-ukraine-accidentally-blocks-venezuela>
  - Wayback: <https://web.archive.org/web/2022/https://decrypt.co/94315/ethereum-infura-cuts-off-users-separatist-areas-ukraine-accidentally-blocks-venezuela>
  > Decrypt contemporaneous coverage of the IP-geo over-block and
> Venezuelan-user side-effect. Triangulation source. DRYRUN:
> pinned Wayback snapshot deferred to human audit.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: ConsenSys (Infura RPC + MetaMask wallet UI)
- **Chains**: `ethereum`
- **Canonical domains**: `infura.io`, `metamask.io`

> The IP-geo block enforcement target is the set of end-users
> located in OFAC-comprehensively-sanctioned regions per Executive
> Order 14065 (Donetsk and Luhansk regions of Ukraine), in
> combination with prior comprehensive-sanctions regions
> (Crimea, Iran, North Korea, Cuba, Syria). enumeration=subset
> because (a) the corporate-policy statement names regions but
> does not enumerate specific user accounts/IPs and (b) the
> operational block was implemented against IP-geolocation
> inferences, which is a moving reference rather than a fixed
> snapshot. The recorded over-block scope additionally captured
> Venezuela and (per some user reports) Iran for a transient
> window of hours-to-days before correction.

## 3. Changed-layer observations (supports the scoped claim)

### l3_rpc · attribution: `plausible` · Δt = 0h

**Event label**: `infura_rpc_ip_geo_block_of_donetsk_luhansk_regions`

**Timestamp**: `2022-03-03 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`semi_primary_wayback`**
  - URL: <https://www.coindesk.com/policy/2022/03/03/metamask-infura-block-certain-areas-amid-crypto-sanctions-fury>
  - Wayback: <https://web.archive.org/web/20220303211454/https://www.coindesk.com/policy/2022/03/03/metamask-infura-block-certain-areas-amid-crypto-sanctions-fury/>
  - body_hash: `sha256:363d4e41a39d936d9906d1658ae98aa633a31519fddb4142d09231eae2cf0f13`
  - body_path: `sources/http_captures/infura-metamask-donetsk-luhansk-block-2022-03/primary/web.archive.org__web-20220304000000-https-www.coindesk.com-policy-2022-03-03-metamask-infura-block-certain-areas-amid-crypto-sanctions-fury__b9e1a64e36.html`
  > CoinDesk 2022-03-03: Infura/MetaMask blocked users in certain
> sanctioned areas (Donetsk/Luhansk) amid Russia-Ukraine sanctions.
> Independent semi-primary anchor.
- **`semi_primary_wayback`**
  - URL: <https://decrypt.co/94315/ethereum-infura-cuts-off-users-separatist-areas-ukraine-accidentally-blocks-venezuela>
  - Wayback: <https://web.archive.org/web/20220303225101/https://decrypt.co/94315/ethereum-infura-cuts-off-users-separatist-areas-ukraine-accidentally-blocks-venezuela>
  - body_hash: `sha256:8eaae4f3355cd364cc4eee6c0a055134e796e8e40152b3e96b2855871cb15199`
  - body_path: `sources/http_captures/infura-metamask-donetsk-luhansk-block-2022-03/primary/web.archive.org__web-20220304000000-https-decrypt.co-94315-ethereum-infura-cuts-off-users-separatist-areas-ukraine-accidentally-blocks-venezuela__3a19ef65b4.html`
  > Decrypt 2022-03-03: Infura cut off users in separatist Ukrainian
> areas (and accidentally over-blocked Venezuela). Independent second
> semi-primary anchor.

### l4_frontend · attribution: `plausible` · Δt = 0h

**Event label**: `metamask_ui_error_state_for_blocked_region_users_including_overblock_venezuela_iran`

**Timestamp**: `2022-03-03 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`semi_primary_wayback`**
  - URL: <https://www.coindesk.com/policy/2022/03/03/metamask-infura-block-certain-areas-amid-crypto-sanctions-fury>
  - Wayback: <https://web.archive.org/web/20220303211454/https://www.coindesk.com/policy/2022/03/03/metamask-infura-block-certain-areas-amid-crypto-sanctions-fury/>
  - body_hash: `sha256:363d4e41a39d936d9906d1658ae98aa633a31519fddb4142d09231eae2cf0f13`
  - body_path: `sources/http_captures/infura-metamask-donetsk-luhansk-block-2022-03/primary/web.archive.org__web-20220304000000-https-www.coindesk.com-policy-2022-03-03-metamask-infura-block-certain-areas-amid-crypto-sanctions-fury__b9e1a64e36.html`
  > CoinDesk 2022-03-03: Infura/MetaMask blocked users in certain
> sanctioned areas (Donetsk/Luhansk) amid Russia-Ukraine sanctions.
> Independent semi-primary anchor.
- **`semi_primary_wayback`**
  - URL: <https://decrypt.co/94315/ethereum-infura-cuts-off-users-separatist-areas-ukraine-accidentally-blocks-venezuela>
  - Wayback: <https://web.archive.org/web/20220303225101/https://decrypt.co/94315/ethereum-infura-cuts-off-users-separatist-areas-ukraine-accidentally-blocks-venezuela>
  - body_hash: `sha256:8eaae4f3355cd364cc4eee6c0a055134e796e8e40152b3e96b2855871cb15199`
  - body_path: `sources/http_captures/infura-metamask-donetsk-luhansk-block-2022-03/primary/web.archive.org__web-20220304000000-https-decrypt.co-94315-ethereum-infura-cuts-off-users-separatist-areas-ukraine-accidentally-blocks-venezuela__3a19ef65b4.html`
  > Decrypt 2022-03-03: Infura cut off users in separatist Ukrainian
> areas (and accidentally over-blocked Venezuela). Independent second
> semi-primary anchor.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`infura-alchemy-tornado-rpc-block-2022`](./infura-alchemy-tornado-rpc-block-2022.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `3f1a9f2`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

