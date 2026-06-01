# Evidence chain — `chinyong-kim-sang-man-dprk-it-worker-ofac-2023-05`

**Status**: `admitted` · **Stratum**: `S1_ofac_sdn` · **Shape**: `null_event` (0 changed layer(s): none) · **Tier**: `null_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `24d80a4` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-31` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T01:03:45Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "OFAC's 2023-05-23 SDN designation (with ROK MOFA) of Chinyong IT Cooperation
> Company + Kim Sang Man named six DPRK IT-worker exchange deposit addresses. No
> public CEX cascade was documented in the 14-day window. null_case: DPRK
> IT-worker proxy target with limited measurable cross-layer surface, mirroring
> the Sim Hyon Sop 2023-04 precedent."

## 1. Trigger

- **Type**: `ofac_sdn_designation`
- **Actor**: `US_OFAC`
- **Timestamp**: `2023-05-23 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://home.treasury.gov/news/press-releases/jy1498>
  - Wayback: <https://web.archive.org/web/20230523155510/https://home.treasury.gov/news/press-releases/jy1498>
  - body_hash: `sha256:d62f6b8c04eba2477e1022a7510ad722c2fd81a14b37a030e44a3a96cdb77f76`
  - body_path: `sources/http_captures/chinyong-kim-sang-man-dprk-it-worker-ofac-2023-05/primary/web.archive.org__web-20230523000000-https-home.treasury.gov-news-press-releases-jy1498__dd2b856709.html`
  > Treasury press release jy1498 (2023-05-23) "Treasury Targets DPRK
> Malicious Cyber and Illicit IT Worker Activities". OFAC (with the ROK
> Ministry of Foreign Affairs) designated Chinyong IT Cooperation Company
> (aka Jinyong) and its employee Kim Sang Man (Sang Man Kim) for the DPRK
> overseas IT-worker revenue scheme funding the regime's WMD programs.
> Wayback 20230523155510 pinned; grep verifies 14xChinyong, 2x"Sang Man",
> 7x"May 23, 2023".
- **`primary_legal`**
  - URL: <https://ofac.treasury.gov/recent-actions/20230523>
  - Wayback: <https://web.archive.org/web/20230523144315/https://ofac.treasury.gov/recent-actions/20230523>
  - body_hash: `sha256:361020395af3a02bf7feca792f7a0d84de9d8c1e45a296fd1ebcbd0b6f34d096`
  - body_path: `sources/http_captures/chinyong-kim-sang-man-dprk-it-worker-ofac-2023-05/primary/web.archive.org__web-20230523000000-https-ofac.treasury.gov-recent-actions-20230523__b4eb572e68.html`
  > OFAC Recent Actions page for 2023-05-23, the formal SDN-list publication
> accompanying jy1498. Kim Sang Man's SDN entry lists six cryptocurrency
> deposit addresses (mainstream-exchange deposit addresses; some are ETH
> addresses that also transacted USDT/USDC, so eight identifiers display
> per Chainalysis). Independent primary anchor for the designation.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Chinyong IT Cooperation Company + Kim Sang Man

> Chinyong IT Cooperation Company (aka Jinyong) + employee Kim Sang Man
> (Sang Man Kim). Kim's SDN entry lists six cryptocurrency deposit addresses
> (per public reporting, all deposit addresses at a large mainstream
> exchange; certain ETH addresses also moved USDT/USDC). Subset enumeration:
> Chinyong/Kim is the load-bearing DPRK IT-worker node; companion entities
> on the same RA page are out of this event's target scope.

## 3. Changed-layer observations (supports the scoped claim)

*No observed_change entries. This is a `null_event`; see §4 for observed_no_change evidence supporting the null claim.*

## 4. No-change observations (where applicable)

### offramp_cex — `no_public_cex_cascade_documented_in_14d_window`

**Window**: `2023-05-23 00:00:00+00:00` → `2023-06-06 23:59:59+00:00`

**Sources**:

- **`primary_legal`**
  - URL: <https://ofac.treasury.gov/recent-actions/20230523>
  - Wayback: <https://web.archive.org/web/20230523144315/https://ofac.treasury.gov/recent-actions/20230523>
  - body_hash: `sha256:361020395af3a02bf7feca792f7a0d84de9d8c1e45a296fd1ebcbd0b6f34d096`
  - body_path: `sources/http_captures/chinyong-kim-sang-man-dprk-it-worker-ofac-2023-05/primary/web.archive.org__web-20230523000000-https-ofac.treasury.gov-recent-actions-20230523__b4eb572e68.html`
  > Kim's six addresses are deposit addresses at a large mainstream
> exchange. No public CEX policy statement explicitly naming the
> Chinyong/Kim SDN entry was published by major exchanges in the 14-day
> post-designation window. Following the DPRK-proxy precedent
> (ofac-dprk-it-worker-sim-hyon-sop-2023-04), industry preference for
> private chain-analytics KYT-flag workflows over public per-wallet
> disclosure makes observed_no_change at the public-disclosure level the
> established empirical pattern.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`ofac-dprk-it-worker-sim-hyon-sop-2023-04`](./ofac-dprk-it-worker-sim-hyon-sop-2023-04.md)
- [`dprk-usdt-network-ofac-2025`](./dprk-usdt-network-ofac-2025.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `24d80a4`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

