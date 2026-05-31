# Evidence chain — `tether-tron-philippines-pdea-freeze-2024`

**Status**: `admitted` · **Stratum**: `S5_corporate` · **Shape**: `null_event` (0 changed layer(s): none) · **Tier**: `null_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `cd67682` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-21` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> As of 2026-05-21, no primary public source enumerates a Tether-executed
> USDT-TRC20 freeze of PDEA-flagged Philippine drug-payment wallets; the
> architectural preconditions (CICC's 2024 entry into crypto-payment
> tracing for drug cases; PDEA-CICC MoA signed 2025-01-28) are documented,
> but the discrete freeze event is not. The offramp_cex layer therefore
> carries an observation_kind=observed_no_change row with attribution=none,
> anchored by the Newsbytes.ph Wayback memento (which contains no freeze
> description) over the 2024-01-01 .. 2025-01-29 window.

## 1. Trigger

- **Type**: `corporate_policy_change`
- **Actor**: `tether_usdt_issuer`
- **Timestamp**: `2025-01-28 00:00:00+00:00` (precision: `week`)

### Trigger citations

- **`supporting_journalism`**
  - URL: <https://newsbytes.ph/2025/01/29/cicc-pdea-say-crypto-now-being-used-in-local-drug-trade/>
  - Wayback: <https://web.archive.org/web/20250217174116/https://newsbytes.ph/2025/01/29/cicc-pdea-say-crypto-now-being-used-in-local-drug-trade/>
  - body_hash: `sha256:c4c66b42427128eb7827ea27b2e6ac6c024d29bfc8430ea7e35bbf729dbf76d9`
  - body_path: `sources/http_captures/tether-tron-philippines-pdea-freeze-2024/primary/web.archive.org__web-20250217174116-https-newsbytes.ph-2025-01-29-cicc-pdea-say-crypto-now-being-used-in-local-drug-trade__c952bb35a1.html`
  > Philippine journalism (Newsbytes.ph, 2025-01-29) reporting PDEA and
> CICC's joint disclosure that USDT is being used in the Philippine
> drug trade, published the day after the PDEA-CICC memorandum of
> agreement was signed. Article notes CICC began assisting drug-related
> cybercrime investigations "early last year" (i.e. early 2024).
> Article does NOT enumerate any specific Tether freeze coordinated
> with PDEA; it documents the architectural precondition (CICC/PDEA
> joint workflow + acknowledgement that USDT is drug-payment rail) but
> not a discrete freeze action. The captured Wayback memento contains
> zero occurrences of "freeze", consistent with the scoped claim that
> no USDT-Tron freeze is documented. Wayback memento 20250217174116
> captured 2026-05-21 with replayable body_hash.
- **`supporting_journalism`**
  - URL: <https://www.pna.gov.ph/articles/1242821>
  > Philippine News Agency (2025-01-28) coverage of the PDEA-CICC
> memorandum of agreement, the institutional anchor for any Tether-
> PDEA freeze workflow. The MoA itself dates 2025-01-28; CICC's
> operational involvement is reported to have begun in 2024. No
> Tether-PDEA-specific freeze transaction or press release is cited.
> The live page returns HTTP 403 and the Wayback availability API
> reports no archived snapshot for this URL (queried 2026-05-21), so
> it is retained as a contextual_unarchived institutional pointer
> rather than a replayable anchor.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: PDEA-flagged Philippine drug-payment USDT-TRC20 wallet cluster
- **Chains**: `tron`

> PDEA-flagged USDT-TRC20 wallets associated with Philippine domestic
> drug-payment cohorts. Class-level enumeration only: no public source
> enumerates the specific TRC-20 addresses, no Tether blog post names
> PDEA as the requesting authority, and no PDEA press release names
> Tether as the freezing party. Listed as subset per §7 codebook
> convention (class-level rationale documented here, value=subset).

## 3. Changed-layer observations (supports the scoped claim)

*No observed_change entries. This is a `null_event`; see §4 for observed_no_change evidence supporting the null claim.*

## 4. No-change observations (where applicable)

### offramp_cex — `no_documented_tether_pdea_directed_usdt_trc20_freeze`

**Window**: `2024-01-01 00:00:00+00:00` → `2025-01-29 23:59:59+00:00`

**Sources**:

- **`semi_primary_wayback`**
  - URL: <https://newsbytes.ph/2025/01/29/cicc-pdea-say-crypto-now-being-used-in-local-drug-trade/>
  - Wayback: <https://web.archive.org/web/20250217174116/https://newsbytes.ph/2025/01/29/cicc-pdea-say-crypto-now-being-used-in-local-drug-trade/>
  - body_hash: `sha256:c4c66b42427128eb7827ea27b2e6ac6c024d29bfc8430ea7e35bbf729dbf76d9`
  - body_path: `sources/http_captures/tether-tron-philippines-pdea-freeze-2024/primary/web.archive.org__web-20250217174116-https-newsbytes.ph-2025-01-29-cicc-pdea-say-crypto-now-being-used-in-local-drug-trade__c952bb35a1.html`
  > Philippine reporting confirms PDEA/CICC awareness that USDT is
> used in local drug trade, that CICC began tracing crypto payments
> in 2024, and that PDEA and CICC formalised the workflow via a
> memorandum of agreement signed 2025-01-28. The article documents
> no discrete Tether-executed freeze at PDEA's direction; the
> captured Wayback memento contains zero occurrences of "freeze".
> This is the replayable null anchor for the observed_no_change row:
> no documented USDT-Tron freeze transaction exists across the
> 2024-01-01 .. 2025-01-29 window. attribution=none per codebook
> §1.1 for observed_no_change rows. Later Wayback memento
> 20250217174116 captured 2026-05-21 with replayable body_hash.
- **`semi_primary_wayback`**
  - URL: <https://newsbytes.ph/2025/01/29/cicc-pdea-say-crypto-now-being-used-in-local-drug-trade/>
  - Wayback: <https://web.archive.org/web/20250129102610/https://newsbytes.ph/2025/01/29/cicc-pdea-say-crypto-now-being-used-in-local-drug-trade/>
  - body_hash: `sha256:b755f2f03ded7670e09c50e14fafc926a7c399381c10a949c2d4c5c7e33583de`
  - body_path: `sources/http_captures/tether-tron-philippines-pdea-freeze-2024/primary/web.archive.org__web-20250129102610-https-newsbytes.ph-2025-01-29-cicc-pdea-say-crypto-now-being-used-in-local-drug-trade__748e1a8d36.html`
  > Independent same-day Wayback memento 20250129102610 of the same
> Newsbytes.ph report, captured on the 2025-01-29 publication date.
> This contemporaneous capture is a second independent archival
> group and likewise contains zero occurrences of "freeze",
> corroborating that the public record around the 2025-01-28 PDEA-
> CICC MoA signing documents no discrete Tether-executed USDT-Tron
> freeze. Memento captured to repo 2026-05-21 with replayable
> body_hash.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`tether-doj-pig-butchering-freeze-2023`](./tether-doj-pig-butchering-freeze-2023.md)
- [`tether-pig-butchering-second-wave-2024`](./tether-pig-butchering-second-wave-2024.md)
- [`tether-retroactive-sweep-2023`](./tether-retroactive-sweep-2023.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `cd67682`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

