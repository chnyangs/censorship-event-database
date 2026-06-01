# Evidence chain — `circle-usdc-svb-policy-statement-2023`

**Status**: `admitted` · **Stratum**: `S5_corporate` · **Shape**: `null_event` (0 changed layer(s): none) · **Tier**: `null_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `7c0cb78` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-21` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T04:09:15Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "Circle Internet Financial's 2023-03-11 corporate-transparency
> statement disclosing ~$3.3B of USDC cash reserves held at Silicon
> Valley Bank at the time of FDIC receivership — paired with
> Circle's commitment to full 1:1 USDC backing using corporate
> funds and the pre-announcement of redemption / minting resumption
> Monday 2023-03-13 — documents an S5 stablecoin-issuer policy
> posture under acute banking-rail stress. No address-level freeze,
> holder restriction, or off-ramp action is taken; the row carries
> no observed_change and functions as denominator control for the
> S5 corporate-policy-change stratum, scoping the 'transparency
> over restriction' baseline against which S5 OFAC-cascade and
> discretionary-freeze rows can be compared."

## 1. Trigger

- **Type**: `corporate_policy_change`
- **Actor**: `CIRCLE_USDC_ISSUER`
- **Timestamp**: `2023-03-11 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_corporate`**
  - URL: <https://www.circle.com/pressroom/3-3-billion-of-usdc-reserve-risk-removed-dollar-de-peg-closes>
  - Wayback: <https://web.archive.org/web/2023/https://www.circle.com/pressroom/3-3-billion-of-usdc-reserve-risk-removed-dollar-de-peg-closes>
  > Circle press-room statement "$3.3 Billion of USDC Reserve Risk
> Removed, Dollar De-peg Closes" — the corporate-policy
> clarification anchor for the 2023-03-11 / 2023-03-12 SVB-cycle
> statements. Circle publicly discloses that approximately $3.3
> billion of USDC's cash reserves (~8% of total backing) remained
> at Silicon Valley Bank at the time of the FDIC receivership
> (2023-03-10), commits to full 1:1 USDC backing using corporate
> funds if necessary, and pre-announces resumption of normal USDC
> redemption / minting operations through banking channels on
> Monday 2023-03-13 after the Federal Reserve / Treasury / FDIC
> joint backstop (announced 2023-03-12 Sunday). This row codes
> the **corporate-transparency / policy-clarification action
> itself** (Circle voluntarily disclosing reserve-bank exposure
> and committing to peg defense) — not a censorship cascade.
> evidence_use=contextual_unarchived: in this DRYRUN the
> authoring LLM agent did not personally pin a body_hash or
> verified Wayback snapshot of the circle.com press-room slug;
> Wayback wildcard pointer pending human-audit re-pin.
- **`primary_corporate`**
  - URL: <https://www.circle.com/blog/an-update-on-usdc-and-silicon-valley-bank>
  - Wayback: <https://web.archive.org/web/2023/https://www.circle.com/blog/an-update-on-usdc-and-silicon-valley-bank>
  > Companion Circle blog "An Update on USDC and Silicon Valley
> Bank" (2023-03-11) confirming the $3.3B SVB exposure figure,
> the 77% Treasury-bills / 23% cash reserve composition (with
> cash held primarily at BNY Mellon), and Circle's intent to
> cover any SVB shortfall with corporate resources. Wayback
> wildcard pointer; evidence_use=contextual_unarchived pending
> human audit body_hash pinning.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Circle Internet Financial (USDC issuer)
- **Chains**: `ethereum`, `solana`, `avalanche`, `polygon`, `stellar`, `algorand`
- **Canonical domains**: `circle.com`

> Target is Circle Internet Financial (the USDC issuer entity) and
> the USDC stablecoin holder / redemption-counterparty class — the
> population of USDC holders globally that relies on Circle's
> redemption commitment and reserve-backing transparency.
> enumeration=subset because the affected class is an open-ended
> population (all USDC holders during the 2023-03-10 to 2023-03-13
> banking-stress window) rather than a closed enumerable set; the
> policy statement is addressed to that population as a class via
> public press-room / blog channels. This row codes the
> **corporate-transparency / policy-clarification action** —
> Circle's voluntary disclosure of SVB reserve exposure, peg-
> defense commitment, and redemption-resumption schedule — not a
> restriction or freeze. No specific addresses, protocols, or
> domains are targeted; Circle's product policy is preserved
> (USDC remains 1:1 backed, redemption resumes Monday).

## 3. Changed-layer observations (supports the scoped claim)

*No observed_change entries. This is a `null_event`; see §4 for observed_no_change evidence supporting the null claim.*

## 4. No-change observations (where applicable)

### offramp_cex — `circle_resumed_usdc_redemption_no_holder_restriction_or_freeze`

**Window**: `2023-03-10 00:00:00+00:00` → `2023-03-16 23:59:59+00:00`

**Sources**:

- **`primary_corporate`**
  - URL: <https://www.circle.com/pressroom/3-3-billion-of-usdc-reserve-risk-removed-dollar-de-peg-closes>
  - body_hash: `sha256:4739b03851b4414fb95e345b07205848f2213503cf3d0f1eeaf673e88b461811`
  - body_path: `sources/http_captures/circle-usdc-svb-policy-statement-2023/v0_3_primary_repair/www.circle.com__pressroom-3-3-billion-of-usdc-reserve-risk-removed-dollar-de-peg-closes__063c331ff1.html`
  > Circle's own press-room statement frames the SVB episode as a
> reserve-risk disclosure and peg-defense commitment, and confirms
> that Circle-direct USDC redemption / minting resumed Monday
> 2023-03-13 with no holder restriction, no freeze, and no
> off-ramp gate. Across the 2023-03-10 to 2023-03-16 window the
> issuer-direct off-ramp surface shows no_change: Circle imposed
> no address-level blacklist, no holder restriction, and no
> discretionary off-ramp gate. body_hash+body_path anchor the
> captured statement as a replayable null-observation anchor.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `7c0cb78`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

