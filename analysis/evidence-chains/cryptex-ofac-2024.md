# Evidence chain — `cryptex-ofac-2024`

**Status**: `admitted` · **Stratum**: `S1_ofac_sdn` · **Shape**: `comparison` (2 changed layer(s): `asset_onchain`, `l4_frontend`) · **Tier**: `anchor_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `f1c99dd` · **Schema**: `0.2.0` · **Event last_verified**: `2026-04-21` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "OFAC designation of the Cryptex Russian exchange on 2024-09-26
> co-occurred (same-day) with a US Secret Service judicial seizure of the canonical cryptex.net
> domain (L4 observed_change, direct attribution), while producing no measurable step change in
> Ethereum aggregate OFAC-compliant relay share (L1 null at day granularity)." Other layers
> remain scoped for follow-up.

## 1. Trigger

- **Type**: `ofac_sdn_designation`
- **Actor**: `US_OFAC`
- **Timestamp**: `2024-09-26 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://ofac.treasury.gov/recent-actions/20240926>
  - Wayback: <https://web.archive.org/web/20260421133030/https://ofac.treasury.gov/recent-actions/20240926>
  - body_hash: `sha256:332252f994d819817902ba10b7f79c002be38acf830ea5249cd2b3b09b02da76`
  - body_path: `sources/http_captures/cryptex-ofac-2024/ofac-recent-actions/ofac.treasury.gov__recent-actions-20240926__a282f3595b.html`
  > OFAC Recent Actions page for 2024-09-26. CRYPTEX (a.k.a. INTERNATIONAL PAYMENT SERVICE
> PROVIDER LLC), Saint Vincent and the Grenadines, website cryptex.net, was added to OFAC's
> SDN list with 4 digital-currency addresses (XBT / ETH / LTC / TRX). Same day OFAC also
> designated Sergey Sergeevich IVANOV (a.k.a. Taleon / UAPS), an individual, with no
> digital-currency addresses. Tags [CYBER2] [RUSSIA-EO14024]. The coordinated action also
> involved FinCEN (PM2BTC Section 9714 special measure) and US Secret Service (domain
> seizure) but those legal instruments are separate from the OFAC SDN designation tracked
> by this event's trigger.
- **`primary_legal`**
  - URL: <https://home.treasury.gov/news/press-releases/jy2595>
  > Treasury press release "Treasury Takes Coordinated Actions Against Illicit Russian Virtual Currency Exchanges and Cybercrime Facilitators" (2024-09-26). Describes the coordinated OFAC + FinCEN + USSS + international action.

## 2. Target

- **Kind**: `address_set`
- **Enumeration**: `complete`
- **Protocol**: `cryptex_exchange`
- **Actor name**: Cryptex
- **Chains**: `bitcoin`, `ethereum`, `litecoin`, `tron`
- **Addresses**: 4 total (enumerated in event YAML)
- **Canonical domains**: `cryptex.net`

> Full set of 4 unique digital-currency addresses attached to the CRYPTEX SDN entity entry,
> extracted verbatim from the OFAC Recent Actions page for 2024-09-26. One address per chain
> (XBT, ETH, LTC, TRX). Ivanov / UAPS individual designation (same-day OFAC action) carries
> no on-chain addresses and is not in-scope for this event's target.

## 3. Changed-layer observations (supports the scoped claim)

### l4_frontend · attribution: `direct` · Δt = 16.1h

**Event label**: `canonical_domain_seized_by_US_Secret_Service`

**Timestamp**: `2024-09-26 16:05:01+00:00` (precision: `minute`)

**Sources**:

- **`primary_legal`**
  - URL: <https://web.archive.org/web/20240930052144/https://cryptex.net/>
  - body_hash: `sha256:6d119a270bf818b6ee49a3bc21985f352843d24ede2a378bdf1e6198c91170c7`
  - body_path: `sources/http_captures/cryptex-ofac-2024/frontend-wayback/web.archive.org__web-20240930052144-https-cryptex.net__a56bfd9215.html`
  > Wayback snapshot of cryptex.net on 2024-09-30 carrying the USSS seizure banner
> verbatim: "This domain for Cryptex has been seized by the United States Secret Service
> pursuant to a seizure warrant issued by the United States District Court for the
> District of Maryland as part of law enforcement operations by the United States Secret
> Service, the U.S. Attorney's Office for the District of Maryland, and the U.S.
> Department of Justice's Computer Crime and Intellectual Property Section." The banner
> also credits Netherlands Police, Dutch FIOD, and German BKA under Operation Endgame.
> This is a primary_legal source because the seizure banner itself is the legal notice
> of the seizure warrant.

### asset_onchain · attribution: `direct` · Δt = 3.62h

**Event label**: `usdt_blacklist_same_day_event`

**Timestamp**: `2024-09-26 03:37:00+00:00` (precision: `minute`)

**Sources**:

- **`primary_onchain`**
  - URL: <https://etherscan.io/tx/0x55c457da2bac2555c666e9948baaa4a5ba66d730033b3684a4aa3c21a964b815>
  - tx_hash: `0x55c457da2bac2555c666e9948baaa4a5ba66d730033b3684a4aa3c21a964b815`
  > Tether USDT blacklist transaction for Cryptex ETH address 0x0931cA... executed
> 2024-09-26 03:37 UTC — same day as OFAC designation, preceding the 16:05 UTC
> USSS domain seizure by 12.5 hours. attribution=direct because Tether's
> publicly-stated policy is to freeze OFAC-listed address balances; full 64-char
> tx hash extracted from usdtbanlist.com explorer-link href and cross-referenced.
- **`supporting_community`**
  - URL: <https://usdtbanlist.com/address/0x0931cA4D13BB4ba75D9B7132AB690265D749a5E7>
  - body_hash: `sha256:145f410f6a396bd596c3dda51ea5040b505b08b5712f23edf8744fe438c48faa`
  - body_path: `sources/http_captures/cryptex-ofac-2024/asset-layer-check/usdtbanlist.com__address-0x0931cA4D13BB4ba75D9B7132AB690265D749a5E7__169bb88c26.html`
  > usdtbanlist.com community tracker confirms the address is on both USDT and USDC
> blacklists with Tether freeze recorded 2024-09-26 03:37 UTC and Circle freeze
> 2024-09-27 03:00 UTC. Serves as supporting archival anchor for the on-chain
> observation; upgrade to primary_onchain requires direct tx-hash verification.

### asset_onchain · attribution: `direct` · Δt = 3.58h

**Event label**: `usdt_trc20_blacklist_same_day_event`

**Timestamp**: `2024-09-26 03:35:00+00:00` (precision: `minute`)

**Sources**:

- **`primary_onchain`**
  - URL: <https://tronscan.org/#/transaction/dad0d1dabad6f1727c6ebb3961053f66dd2add3b78def6360e5c2a2a6121cad9>
  - tx_hash: `dad0d1dabad6f1727c6ebb3961053f66dd2add3b78def6360e5c2a2a6121cad9`
  > Tether USDT-TRC20 addBlackList transaction on TRON for address TTUDyVhhpCC1xJoPmWzdjLAzeoPwbSABdr, executed 2024-09-26 03:35 UTC. 2 minutes before the ETH USDT freeze (03:37 UTC); batch action across chains.
- **`supporting_community`**
  - URL: <https://usdtbanlist.com/address/TTUDyVhhpCC1xJoPmWzdjLAzeoPwbSABdr>
  - body_hash: `sha256:fcabacd285697808aa10ed9de3cbe9030acb295aa8e1c3a30cbbbdd2d4b50cf0`
  - body_path: `sources/http_captures/cryptex-ofac-2024/asset-layer-check/usdtbanlist.com__address-TTUDyVhhpCC1xJoPmWzdjLAzeoPwbSABdr.html`
  > usdtbanlist.com community tracker anchor for the TRX freeze above.
> v0.3 audit 2026-05-20: source type CORRECTED from primary_corporate
> to supporting_community to match the parallel USDT-ETH row's
> treatment of the same source kind (usdtbanlist.com is community-
> maintained, not Tether/Tron-issuer-published).

### asset_onchain · attribution: `direct` · Δt = 27.0h

**Event label**: `usdc_blacklist_next_day_event`

**Timestamp**: `2024-09-27 03:00:00+00:00` (precision: `minute`)

**Sources**:

- **`primary_onchain`**
  - URL: <https://etherscan.io/tx/0xa10d4e1a29a6eb30579b8cba5e1316d27ab120eff5944cce6836c8a837ffd8da>
  - tx_hash: `0xa10d4e1a29a6eb30579b8cba5e1316d27ab120eff5944cce6836c8a837ffd8da`
  > Circle USDC blacklist transaction for Cryptex ETH address executed 2024-09-27
> 03:00 UTC — 27 hours after OFAC designation. Full 64-char tx hash extracted
> from usdtbanlist.com explorer-link href.
- **`supporting_community`**
  - URL: <https://usdtbanlist.com/address/0x0931cA4D13BB4ba75D9B7132AB690265D749a5E7>
  - body_hash: `sha256:145f410f6a396bd596c3dda51ea5040b505b08b5712f23edf8744fe438c48faa`
  - body_path: `sources/http_captures/cryptex-ofac-2024/asset-layer-check/usdtbanlist.com__address-0x0931cA4D13BB4ba75D9B7132AB690265D749a5E7__169bb88c26.html`
  > Same usdtbanlist.com anchor covering both Tether and Circle freeze events for this address.

## 4. No-change observations (where applicable)

### l1_consensus — `ofac_compliant_relay_share_stable_through_cryptex_designation`

**Window**: `2024-09-12 00:00:00+00:00` → `2024-10-10 23:59:59+00:00`

**Sources**:

- **`semi_primary_measurement`**
  - URL: <https://raw.githubusercontent.com/nerolation/censorship.pics/main/data/relay_censorship_share.csv>
  - body_hash: `sha256:45c1db9ca70491743e2e33c313d7293eed791a82d0ea7313c5241eca9e8b4567`
  - body_path: `sources/l1_datasets/tornado-cash-ofac-2022/relay_censorship_share.csv`
  > Slice [2024-09-12, 2024-10-10]: 29 days × 2 categories = 58 rows. Censoring-relay
> share pre-event 14d mean 55.76% ± 1.76, event day 53.95%, post-event 14d mean 53.48%
> ± 0.68. Event-day value within 1.0 sd of pre-event mean; post-event mean effectively
> identical. Null shape: single-wallet exchange designation did not perturb aggregate
> relay OFAC-compliance.
- **`semi_primary_measurement`**
  - URL: <https://www.relayscan.io>
  - Wayback: <https://web.archive.org/web/20260421114750/https://www.relayscan.io/>
  - body_hash: `sha256:dc39f55922c657cd3caf22cdd77287f707ddec63ec0510091532f5fadc7aa827`
  - body_path: `sources/http_captures/tornado-cash-ofac-2022/l1-relay-dashboards/www.relayscan.io__capture__1a79bf8cec.html`
  > Relayscan independent dashboard consistent with Wahrstätter's plateau — second source for the observed_no_change claim.

## 5. Honest coverage gaps

- **l0_network** (`not_measured`): L0 network-layer OONI API query performed 2026-04-22. Searched the
- **l3_rpc** (`not_measured`): No pinned MEV-Blocker / OFAC-compliant RPC filter-list snapshot,
- **offramp_cex** (`not_measured`): Chain-analytics anchors pinned 2026-04-22 as primary_corporate

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `f1c99dd`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

