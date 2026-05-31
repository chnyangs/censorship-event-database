# Evidence chain — `irgc-ransomware-ofac-2022`

**Status**: `admitted` · **Stratum**: `S1_ofac_sdn` · **Shape**: `null_event` (0 changed layer(s): none) · **Tier**: `null_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-05-31` · **Source commit**: `939a17f` · **Schema**: `0.2.0` · **Event last_verified**: `2026-04-22` · **Tool version**: `0.1.0` · **Generated**: `2026-05-31T14:50:46Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "OFAC designation of 11 IRGC-affiliated individuals + 1 entity
> (AFKAR SYSTEM YAZD COMPANY) on 2022-09-14, with 6 unique Bitcoin
> addresses concentrated among 2 of the 11 individuals (KHATIBI
> AGHADA Ahmad: 3 XBT; NIKAEEN RAVARI Amir Hossein: 4 XBT, with 1
> address `1H939dom7i4WDLCKyGbXUp3fs9CSTNRzgL` shared between both
> listings = 7 raw DCA entries deduplicating to 6 unique). Cross-
> layer cascade structurally unmeasurable (BTC native, individuals,
> event falls 1 day before The Merge). Datapoint for Iran-related
> individual-BTC-sanction class. v0.3 audit 2026-05-19: scoped_claim
> repaired per audit_log row 233 (qid=116 needs_recheck) which
> flagged original wording for `6 IRGC-affiliated individuals` count
> factual error vs OFAC RA 11 individuals + 1 entity."

## 1. Trigger

- **Type**: `ofac_sdn_designation`
- **Actor**: `US_OFAC`
- **Timestamp**: `2022-09-14 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://ofac.treasury.gov/recent-actions/20220914>
  - Wayback: <https://web.archive.org/web/20260421142243/https://ofac.treasury.gov/recent-actions/20220914>
  - body_hash: `sha256:07f9e6b2bc857376834c2188f539a03aeb009ef55a20e7e313d34cdc8d0c7b2d`
  - body_path: `sources/http_captures/irgc-ransomware-ofac-2022/ofac-recent-actions/ofac.treasury.gov__recent-actions-20220914__66d8577259.html`
  > OFAC Recent Actions page for 2022-09-14. Multiple Iranian IRGC-affiliated individuals
> designated for ransomware conduct: KHATIBI AGHADA Ahmad (3 XBT), NIKAEEN RAVARI Amir
> Hossein (4 XBT — one address duplicates KHATIBI's), plus 4 other individuals with no
> addresses. Entity AFKAR SYSTEM YAZD COMPANY also designated. Tags [IRGC] [IFSR]
> [CYBER2]. 6 unique XBT addresses total. Event occurred 1 day before The Merge
> (Ethereum Merge: 2022-09-15) — structurally in the pre-PBS liminal window.
- **`primary_legal`**
  - URL: <https://home.treasury.gov/news/press-releases/jy0948>
  > Treasury press release "Treasury Sanctions IRGC-Affiliated Cyber Actors for Roles in Ransomware Activity" (2022-09-14).

## 2. Target

- **Kind**: `address_set`
- **Enumeration**: `complete`
- **Actor name**: IRGC-affiliated ransomware actors
- **Chains**: `bitcoin`
- **Addresses**: 6 total (enumerated in event YAML)

> 6 unique Bitcoin addresses across 2 of the 6 designated individuals (KHATIBI 3, NIKAEEN 4, one address overlap).

## 3. Changed-layer observations (supports the scoped claim)

*No observed_change entries. This is a `null_event`; see §4 for observed_no_change evidence supporting the null claim.*

## 4. No-change observations (where applicable)

### offramp_cex — `no_public_cex_cascade_documented_in_14d_window`

**Window**: `2022-09-14 00:00:00+00:00` → `2022-09-28 23:59:59+00:00`

**Sources**:

- **`primary_legal`**
  - URL: <https://ofac.treasury.gov/recent-actions/20220914>
  - body_hash: `sha256:07f9e6b2bc857376834c2188f539a03aeb009ef55a20e7e313d34cdc8d0c7b2d`
  - body_path: `sources/http_captures/irgc-ransomware-ofac-2022/ofac-recent-actions/ofac.treasury.gov__recent-actions-20220914__66d8577259.html`
  > No public CEX policy statement referencing 6 IRGC-affiliated BTC addresses was published by major
> exchanges (Binance, Kraken, Coinbase, Bybit) in the 14-day post-designation
> window. Observation records the absence of public disclosure; private
> chain-analytics flagging workflows (Chainalysis / Elliptic / TRM) are outside
> the scope of this observation and may have produced unpublished KYT flags.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `939a17f`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

