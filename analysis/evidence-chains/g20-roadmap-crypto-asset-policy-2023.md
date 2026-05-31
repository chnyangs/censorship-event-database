# Evidence chain — `g20-roadmap-crypto-asset-policy-2023`

**Status**: `admitted` · **Stratum**: `S6_supranational` · **Shape**: `null_event` (0 changed layer(s): none) · **Tier**: `null_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `ad93b7f` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-21` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "The G20 Roadmap on Crypto-Asset Policy, endorsed at the New Delhi
> Leaders' Summit on 2023-09-09 together with the IMF-FSB Synthesis
> Paper 'Policies for Crypto-Assets' (7 September 2023), is a
> class-level G20 coordination instrument endorsing the FSB high-
> level recommendations on crypto-asset activities and global
> stablecoin arrangements. Coded as null_event / null_case at the
> corpus's resolution: no per-event observed_change cascade is
> directly attributable to the 2023-09-09 endorsement date;
> downstream FSB, FATF, and national implementations are tracked
> as separate child events."

## 1. Trigger

- **Type**: `supranational_regulation`
- **Actor**: `G20`
- **Timestamp**: `2023-09-09 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://www.fsb.org/2023/09/imf-fsb-synthesis-paper-policies-for-crypto-assets/>
  - body_hash: `sha256:cdcd8299e4fda612e3ce9d6b9433c02cec7b44c2d50aa029059ece90257d1333`
  - body_path: `sources/http_captures/g20-roadmap-crypto-asset-policy-2023/primary/www.fsb.org__2023-09-imf-fsb-synthesis-paper-policies-for-crypto-assets__8208cb3562.html`
  > G20 New Delhi Leaders' Declaration (endorsed 2023-09-09)
> endorsed the FSB high-level recommendations for the
> regulation, supervision and oversight of crypto-asset
> activities and markets and of global stablecoin
> arrangements, alongside the IMF-FSB Synthesis Paper
> "Policies for Crypto-Assets" (7 September 2023) which sets
> out an implementation roadmap. All 83 paragraphs of the
> declaration were passed unanimously (G20 consensus,
> including China and Russia). Foundational G20-level
> coordination instrument for cross-jurisdictional crypto-
> asset regulation; downstream effects cascade via FSB R1
> recommendations, FATF R.15 INR updates, and national
> implementation.
- **`primary_legal`**
  - URL: <https://www.fsb.org/uploads/R070923-1.pdf>
  - body_hash: `sha256:e0953161ceb157baf2c39b79167183c9adec9f2fbd995c3a5ac1cb8969309826`
  - body_path: `sources/http_captures/g20-roadmap-crypto-asset-policy-2023/primary/www.fsb.org__uploads-R070923-1.pdf__ea35302ca6.bin`
  > IMF-FSB Synthesis Paper "Policies for Crypto-Assets"
> (7 September 2023). Live fsb.org capture 2026-05-21.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: G20-jurisdiction crypto-asset ecosystem

> Class-level G20-coordination instrument addressing crypto-asset
> activities and markets and global stablecoin arrangements in
> G20-member jurisdictions and (per the IMF-FSB Synthesis Paper's
> implementation roadmap) beyond G20 via capacity-building and
> coordination work. Per §7 codebook, class-level regulatory
> coordination is encoded as enumeration=subset with the class-
> level rationale documented here. No address-level enumeration;
> binding force is via FSB / FATF / IOSCO / IMF standard-setter
> work programs and national implementation. Downstream affected
> entities include centralized exchanges and custodians,
> stablecoin issuers (Tether, Circle, Paxos), and DeFi
> arrangements whose governance bodies are within FSB/FATF
> standards scope.

## 3. Changed-layer observations (supports the scoped claim)

*No observed_change entries. This is a `null_event`; see §4 for observed_no_change evidence supporting the null claim.*

## 4. No-change observations (where applicable)

### offramp_cex — `g20_2023_roadmap_crypto_asset_policy_endorsement`

**Window**: `2023-09-09 00:00:00+00:00` → `2024-12-31 23:59:59+00:00`

**Sources**:

- **`primary_legal`**
  - URL: <https://www.fsb.org/2023/09/imf-fsb-synthesis-paper-policies-for-crypto-assets/>
  - body_hash: `sha256:cdcd8299e4fda612e3ce9d6b9433c02cec7b44c2d50aa029059ece90257d1333`
  - body_path: `sources/http_captures/g20-roadmap-crypto-asset-policy-2023/primary/www.fsb.org__2023-09-imf-fsb-synthesis-paper-policies-for-crypto-assets__8208cb3562.html`
  > G20 New Delhi Leaders' Declaration endorsement of the
> IMF-FSB Synthesis Paper and FSB high-level recommendations
> on crypto-assets and global stablecoin arrangements is a
> class-level coordination instrument. No per-event
> observed_change cascade attributable to this trigger at
> the corpus's resolution; downstream effects manifest via
> FSB / FATF / national implementations tracked as separate
> child events. Live fsb.org capture 2026-05-21.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`fsb-crypto-asset-recommendations-2023`](./fsb-crypto-asset-recommendations-2023.md)
- [`fatf-targeted-update-va-vasp-2023`](./fatf-targeted-update-va-vasp-2023.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `ad93b7f`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

