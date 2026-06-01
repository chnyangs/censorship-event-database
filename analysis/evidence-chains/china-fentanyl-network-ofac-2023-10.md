# Evidence chain — `china-fentanyl-network-ofac-2023-10`

**Status**: `admitted` · **Stratum**: `S1_ofac_sdn` · **Shape**: `null_event` (0 changed layer(s): none) · **Tier**: `null_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `93a10f9` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-31` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T11:50:49Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "OFAC's 2023-10-03 SDN designation of a China-based fentanyl/synthetic-opioid
> producer network (jy1779, 28 SDNs) named 16 crypto addresses across
> BTC/ETH/Tron. No public CEX cascade was documented in the 14-day window.
> null_case: narcotics-network target with limited measurable cross-layer
> surface at draft time."

## 1. Trigger

- **Type**: `ofac_sdn_designation`
- **Actor**: `US_OFAC`
- **Timestamp**: `2023-10-03 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://home.treasury.gov/news/press-releases/jy1779>
  - Wayback: <https://web.archive.org/web/20231003190525/https://home.treasury.gov/news/press-releases/jy1779>
  - body_hash: `sha256:00f439975eba09e5ac169c4f0d6fea7617063249f1a5d1faa0c03cc6a96d8f67`
  - body_path: `sources/http_captures/china-fentanyl-network-ofac-2023-10/primary/web.archive.org__web-20231003000000-https-home.treasury.gov-news-press-releases-jy1779__c0f71db364.html`
  > Treasury press release jy1779 (2023-10-03) "Treasury Targets Large
> Chinese Network of Illicit Drug Producers". OFAC designated 28
> individuals/entities (a primarily China-based fentanyl/methamphetamine/
> MDMA-precursor network, plus one Canadian national and two Canadian
> firms), identifying crypto addresses used to receive drug-payment
> proceeds. Wayback 20231003190525 pinned; grep verifies 59xfentanyl,
> 4x"October 3, 2023".
- **`primary_legal`**
  - URL: <https://ofac.treasury.gov/recent-actions/20231003>
  - Wayback: <https://web.archive.org/web/20231003190327/https://ofac.treasury.gov/recent-actions/20231003>
  - body_hash: `sha256:1e69d995969b2deee20c842346e86f4d8aa35d0c615e25df287c28cea79f17cc`
  - body_path: `sources/http_captures/china-fentanyl-network-ofac-2023-10/primary/web.archive.org__web-20231003000000-https-ofac.treasury.gov-recent-actions-20231003__09b2bec01f.html`
  > OFAC Recent Actions page for 2023-10-03, the formal SDN-list publication
> accompanying jy1779. Per Chainalysis, 16 crypto addresses across
> Bitcoin / Ethereum / Tron (the EVM/Tron addresses primarily holding
> USDT/USDC) were attached, collectively receiving ~$3.8M. Independent
> primary anchor for the designation.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: China-based fentanyl/synthetic-opioid producer network (28 SDNs)
- **Chains**: `bitcoin`, `ethereum`, `tron`

> A primarily China-based illicit-drug-producer network (28 designated
> individuals/entities; jy1779), with 16 crypto addresses across BTC/ETH/Tron
> used to receive drug-payment proceeds. Subset enumeration: this event treats
> the China fentanyl network as the target aggregate; per-defendant address
> enumeration is deferred (no captured primary_onchain receipts at draft
> time).

## 3. Changed-layer observations (supports the scoped claim)

*No observed_change entries. This is a `null_event`; see §4 for observed_no_change evidence supporting the null claim.*

## 4. No-change observations (where applicable)

### offramp_cex — `no_public_cex_cascade_documented_in_14d_window`

**Window**: `2023-10-03 00:00:00+00:00` → `2023-10-17 23:59:59+00:00`

**Sources**:

- **`primary_legal`**
  - URL: <https://ofac.treasury.gov/recent-actions/20231003>
  - Wayback: <https://web.archive.org/web/20231003190327/https://ofac.treasury.gov/recent-actions/20231003>
  - body_hash: `sha256:1e69d995969b2deee20c842346e86f4d8aa35d0c615e25df287c28cea79f17cc`
  - body_path: `sources/http_captures/china-fentanyl-network-ofac-2023-10/primary/web.archive.org__web-20231003000000-https-ofac.treasury.gov-recent-actions-20231003__09b2bec01f.html`
  > No public CEX policy statement explicitly naming the China fentanyl
> network SDN entries was published by major exchanges in the 14-day
> post-designation window. Records absence of public disclosure; private
> chain-analytics KYT flagging is outside this observation's scope.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `93a10f9`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

