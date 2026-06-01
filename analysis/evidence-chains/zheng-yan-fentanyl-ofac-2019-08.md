# Evidence chain — `zheng-yan-fentanyl-ofac-2019-08`

**Status**: `admitted` · **Stratum**: `S1_ofac_sdn` · **Shape**: `null_event` (0 changed layer(s): none) · **Tier**: `null_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-02` · **Source commit**: `a888d9d` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-31` · **Tool version**: `0.1.0` · **Generated**: `2026-06-02T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "The 2019-08-21 OFAC Kingpin-Act designation of Fujing Zheng, Guanghua
> Zheng, and Xiaobing Yan (the first OFAC narcotics designation to attach
> crypto addresses) listed Bitcoin addresses (Litecoin additionally per the SDN-list entries); no public CEX
> cascade was documented in the 14-day window. null_case: individual-
> trafficker target with limited measurable cross-layer surface."

## 1. Trigger

- **Type**: `ofac_sdn_designation`
- **Actor**: `US_OFAC`
- **Timestamp**: `2019-08-21 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://home.treasury.gov/news/press-releases/sm756>
  - Wayback: <https://web.archive.org/web/20190821203144/https://home.treasury.gov/news/press-releases/sm756>
  - body_hash: `sha256:1108f8eb463b17c44f4fd50f05350e7d79999a719ada23a6481bac0c291778c6`
  - body_path: `sources/http_captures/zheng-yan-fentanyl-ofac-2019-08/primary/web.archive.org__web-20190821203144-https-home.treasury.gov-news-press-releases-sm756__b1b6b776ea.html`
  > U.S. Treasury press release sm756 (2019-08-21), "Treasury Targets
> Chinese Drug Kingpins Fueling America's Deadly Opioid Crisis."
> OFAC designated Fujing Zheng, Guanghua Zheng, and Xiaobing Yan
> (plus the Zheng Drug Trafficking Organization and Qinsheng
> Pharmaceutical) under the Foreign Narcotics Kingpin Designation
> Act. The SDN entries attached Bitcoin digital-currency
> addresses (with Litecoin additionally listed in the SDN-list entries) controlled by the designees — the FIRST OFAC
> narcotics-related designation to enumerate cryptocurrency
> addresses. Wayback memento 20190821203144 pinned.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Fujing Zheng / Guanghua Zheng / Xiaobing Yan (Zheng DTO)

> Fujing Zheng, Guanghua Zheng, and Xiaobing Yan designated as SDNs
> under the Kingpin Act, with Bitcoin addresses attached to the individual entries
> (Litecoin additionally in the SDN-list entries). Marked subset because the target is the named
> set of individuals/organizations (Zheng DTO, Qinsheng Pharmaceutical)
> rather than an exhaustively enumerated complete address cohort; the
> on-chain addresses are not separately re-listed in this draft pending
> a primary_onchain freeze receipt (deferred per codebook §1.6).

## 3. Changed-layer observations (supports the scoped claim)

*No observed_change entries. This is a `null_event`; see §4 for observed_no_change evidence supporting the null claim.*

## 4. No-change observations (where applicable)

### offramp_cex — `no_public_cex_cascade_documented_in_14d_window`

**Window**: `2019-08-21 00:00:00+00:00` → `2019-09-04 23:59:59+00:00`

**Sources**:

- **`primary_legal`**
  - URL: <https://home.treasury.gov/news/press-releases/sm756>
  - Wayback: <https://web.archive.org/web/20190821203144/https://home.treasury.gov/news/press-releases/sm756>
  - body_hash: `sha256:1108f8eb463b17c44f4fd50f05350e7d79999a719ada23a6481bac0c291778c6`
  - body_path: `sources/http_captures/zheng-yan-fentanyl-ofac-2019-08/primary/web.archive.org__web-20190821203144-https-home.treasury.gov-news-press-releases-sm756__b1b6b776ea.html`
  > No public CEX policy statement referencing the Zheng/Yan cryptocurrency addresses was published by major exchanges in the 14-day post-
> designation window. Observation records the absence of public
> disclosure; private chain-analytics KYT flagging is outside this
> observation's scope.

## 5. Honest coverage gaps

- **l0_network** (`not_measured`): No OONI / Censored Planet probe in scope; the designees are
- **asset_onchain** (`not_measured`): The SDN entries attach cryptocurrency addresses (Bitcoin named in

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `a888d9d`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

