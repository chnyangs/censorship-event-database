# Evidence chain — `binance-busd-wind-down-2024`

**Status**: `admitted` · **Stratum**: `S5_corporate` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `8583894` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-21` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "Binance Holdings Limited's 2024-02-22 global wind-down of BUSD
> product support on binance.com — spot-trading-pair removal and
> auto-conversion of remaining user BUSD balances to FDUSD at 1:1
> — narrows the centralized-exchange off-ramp surface for BUSD to
> zero on its dominant venue. The offramp_cex layer carries the
> load-bearing direct-attribution observation, with the Binance
> customer-support announcement publicly citing the upstream
> NYDFS-directed Paxos cessation of new BUSD minting (2023-02-13)
> as the proximate cause; the event is the cleanest downstream S5
> corporate follow-on to that upstream trigger in the corpus."

## 1. Trigger

- **Type**: `corporate_policy_change`
- **Actor**: `binance_holdings_limited`
- **Timestamp**: `2024-02-22 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_corporate`**
  - URL: <https://www.binance.com/en/support/announcement/notice-regarding-the-removal-of-busd-and-conversion-of-busd-to-fdusd-1c98ce7bb464422dbbaeda7066ae445b>
  - Wayback: <https://web.archive.org/web/20240222000000/https://www.binance.com/en/support/announcement/notice-regarding-the-removal-of-busd-and-conversion-of-busd-to-fdusd-1c98ce7bb464422dbbaeda7066ae445b>
  > Binance customer-support announcement: "Notice Regarding the
> Removal of BUSD and Conversion of BUSD to FDUSD." Binance
> explicitly cites Paxos's NYDFS-directed cessation of new BUSD
> minting (2023-02-13; see related_events:
> paxos-busd-nydfs-minting-stop-2023) as the proximate cause for
> ending BUSD product support, and notifies users that BUSD
> spot-trading pairs will be removed and remaining BUSD balances
> in Spot and Funding Wallets will be auto-converted to FDUSD
> (First Digital USD, FD121 Ltd.) at 1:1. Effective wind-down
> cutoff for ongoing product support is 2024-02-22, after which
> no BUSD spot pairs are listed and BUSD ceases to be a
> Binance-supported trading asset. evidence_use=
> contextual_unarchived: in this DRYRUN the authoring LLM agent
> did not personally pin a body_hash or verified Wayback
> snapshot; the binance.com customer-support announcement slug
> is routinely captured by Wayback through 2023-2024, but the
> precise snapshot timestamp must be re-anchored during human
> audit before this citation may serve as an admission anchor.
- **`primary_corporate`**
  - URL: <https://www.binance.com/en/support/announcement/binance-encourages-users-to-convert-busd-to-other-stablecoins-prior-to-february-2024-d392843e81fd4bc3a5f7e219aa01f34d>
  - Wayback: <https://web.archive.org/web/2023/https://www.binance.com/en/support/announcement/binance-encourages-users-to-convert-busd-to-other-stablecoins-prior-to-february-2024-d392843e81fd4bc3a5f7e219aa01f34d>
  > Earlier (2023-08-30) Binance announcement giving advance notice
> that Binance will end BUSD product support by February 2024
> following Paxos's NYDFS-directed cessation of BUSD minting,
> and encouraging users to convert BUSD to other stablecoins
> (FDUSD, USDT, USDC). Establishes the public corporate-policy
> commitment of which 2024-02-22 is the operational realization.
> Wayback wildcard pointer in lieu of a pinned-timestamp
> snapshot.

## 2. Target

- **Kind**: `asset`
- **Enumeration**: `complete`
- **Actor name**: Binance Holdings Limited (global BUSD product wind-down)
- **Chains**: `ethereum`, `bnb_chain`
- **Canonical domains**: `binance.com`

> Single-asset target: BUSD (Binance USD), the Paxos-issued ERC-20
> stablecoin (contract 0x4Fabb145d64652a948d72533023f6E7A623C7C53 on
> Ethereum mainnet, plus its BEP-20 Binance-Peg representation on
> BNB Chain). The Binance-side wind-down ends product support
> globally on binance.com — spot pairs are removed and remaining
> user balances are auto-converted to FDUSD at 1:1. enumeration=
> complete because the action targets the entire BUSD asset class
> on Binance, not a geofenced subset.

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `direct` · Δt = 0h

**Event label**: `binance_busd_spot_pair_removal_and_balance_auto_conversion_to_fdusd`

**Timestamp**: `2024-02-22 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_corporate`**
  - URL: <https://www.binance.com/en/support/announcement/notice-regarding-the-removal-of-busd-and-conversion-of-busd-to-fdusd-1c98ce7bb464422dbbaeda7066ae445b>
  - Wayback: <https://web.archive.org/web/20231212193137/https://www.binance.com/en/support/announcement/notice-regarding-the-removal-of-busd-and-conversion-of-busd-to-fdusd-1c98ce7bb464422dbbaeda7066ae445b>
  - body_hash: `sha256:64e42f5fc0ebf0b45bb5c80c1bf3f97dc2f5fc1b325f67067637ccf3739848f1`
  - body_path: `sources/http_captures/binance-busd-wind-down-2024/primary/web.archive.org__web-20240101000000-https-www.binance.com-en-support-announcement-notice-regarding-the-removal-of-busd-and-conversion-of-busd-to-fdusd-1c98ce7bb464422db__19fe3d27b2.html`
  > Binance official announcement on removing BUSD and auto-converting
> user BUSD balances to FDUSD (wind-down following Paxos/NYDFS mint
> cessation). primary_corporate anchor; attribution=direct. Wayback
> 20231212193137 pinned.
- **`semi_primary_wayback`**
  - URL: <https://www.theblock.co/post/248301/binance-ends-busd-support-fdusd>
  - Wayback: <https://web.archive.org/web/20231010072759/https://www.theblock.co/post/248301/binance-ends-busd-support-fdusd>
  - body_hash: `sha256:67f027b7c64203a51d4ef876e5d66c8b4d90cd7cbc4198a62e0f9575858f9413`
  - body_path: `sources/http_captures/binance-busd-wind-down-2024/primary/web.archive.org__web-20231215000000-https-www.theblock.co-post-248301-binance-ends-busd-support-fdusd__5d71382cd6.html`
  > The Block coverage of Binance ending BUSD support and converting
> to FDUSD. Independent semi-primary anchor.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `8583894`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

