# Evidence chain — `prince-group-chen-zhi-ofac-2025-10`

**Status**: `admitted` · **Stratum**: `S1_ofac_sdn` · **Shape**: `null_event` (0 changed layer(s): none) · **Tier**: `null_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `96a9483` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-31` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "The 2025-10-14 OFAC + U.K. designation of the Prince Group TCO /
> Chen Zhi (Treasury sb0278, pig-butchering crypto fraud) attached
> Bitcoin addresses; native BTC has no issuer freeze primitive and no
> public CEX cascade was pinned in the 14-day window. null_case: limited
> measurable cross-layer surface (parallel DOJ seizure is a separate
> mechanism)."

## 1. Trigger

- **Type**: `ofac_sdn_designation`
- **Actor**: `US_OFAC`
- **Timestamp**: `2025-10-14 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://home.treasury.gov/news/press-releases/sb0278>
  - Wayback: <https://web.archive.org/web/20251016034109/https://home.treasury.gov/news/press-releases/sb0278>
  - body_hash: `sha256:642670e04c720ee94ca468ddd871aeae5858ee29fe6e2bb167ab6102892eb279`
  - body_path: `sources/http_captures/prince-group-chen-zhi-ofac-2025-10/primary/web.archive.org__web-20251016034109-https-home.treasury.gov-news-press-releases-sb0278__4d115ef988.html`
  > U.S. Treasury press release sb0278 (2025-10-14): OFAC, jointly
> with the U.K. (FCDO/OFSI), designated 146 targets within the
> Prince Group Transnational Criminal Organization led by Cambodian
> national Chen Zhi, for large-scale "pig butchering" crypto
> investment fraud run out of forced-labor scam compounds. Chen
> Zhi's SDN entry lists Bitcoin addresses (four at designation;
> 25 more added 2025-10-30); a parallel DOJ civil forfeiture
> targeted ~127,000 BTC (~$15B). Wayback memento 20251016034109
> pinned.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Prince Group TCO + Chen Zhi
- **Chains**: `bitcoin`

> Prince Group TCO (146 targets) led by Chen Zhi, designated as SDNs
> jointly by OFAC and the U.K. Chen Zhi's SDN entry attaches Bitcoin
> addresses (four at the 2025-10-14 designation; 25 added 2025-10-30).
> Marked subset because the action targets the named TCO and a
> non-exhaustive attached address set rather than an enumerated
> complete address set captured in this pass.

## 3. Changed-layer observations (supports the scoped claim)

*No observed_change entries. This is a `null_event`; see §4 for observed_no_change evidence supporting the null claim.*

## 4. No-change observations (where applicable)

### offramp_cex — `no_public_cex_cascade_documented_in_14d_window`

**Window**: `2025-10-14 00:00:00+00:00` → `2025-10-28 23:59:59+00:00`

**Sources**:

- **`primary_legal`**
  - URL: <https://home.treasury.gov/news/press-releases/sb0278>
  - Wayback: <https://web.archive.org/web/20251016034109/https://home.treasury.gov/news/press-releases/sb0278>
  - body_hash: `sha256:642670e04c720ee94ca468ddd871aeae5858ee29fe6e2bb167ab6102892eb279`
  - body_path: `sources/http_captures/prince-group-chen-zhi-ofac-2025-10/primary/web.archive.org__web-20251016034109-https-home.treasury.gov-news-press-releases-sb0278__4d115ef988.html`
  > No public CEX policy statement referencing the Prince Group /
> Chen Zhi designation was pinned in the 14-day post-designation
> window in this authoring pass. Records the absence of pinned
> public disclosure; private KYT flagging is outside scope. The
> on-chain footprint is native-BTC (no issuer freeze primitive);
> the parallel DOJ seizure is a separate enforcement mechanism.

## 5. Honest coverage gaps

- **asset_onchain** (`not_measured`): Bitcoin addresses are attached to Chen Zhi's SDN entry, but native

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `96a9483`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

