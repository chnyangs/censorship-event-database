# Codebook — coding rules for fuzzy edges

**Purpose**: This codebook formalizes coding decisions for fields where κ < 0.6 in
the latest IRR run, or where Phase A-F authoring agents independently surfaced
ambiguity. It is the **canonical reference** that LLM authoring agents and human
coders MUST consult before assigning these fields.

**Version**: 3.0.0.

**Effective**: 2026-05-31 (3.0.0); 2026-05-30 (2.0.0); 2026-05-19 (1.0.1). Codebook updates require:
1. A new IRR pass on at least 10 events covering the edge case.
2. A `**CODEBOOK CHANGE — YYYY-MM-DD**` entry in this file's changelog.
3. Re-coding of all events touching the changed field, with `last_human_audit`
   stamp refresh.
4. **Worked-example corrections (vs decision-rule changes) = minor version bump**;
   decision-rule changes = major bump. A minor bump (e.g., 1.0.0 → 1.0.1) means
   no mandatory re-extraction queue, but reviewers consulting the codebook for
   the corrected example must use the corrected version.

**Authority**: This file binds both human coders and LLM authoring agents. When
a citation in this codebook contradicts agent intuition, the codebook wins.

---

## Changelog

- **CODEBOOK CHANGE — 2026-05-31** — **§9 added (inclusion boundary) + temporal-tier rename +
  jurisdiction vocab expansion** (comprehensive since-2007 census; user-blessed 2026-05-31).
  (1) **§9 inclusion boundary**: a case is in scope only if it is a deliberate *censorship action*
  (deny/block/seize/freeze/delist/geofence/debank a legitimate platform/asset/user); EXCLUDES
  platform failures (fraud/hack/insolvency), fraud/Ponzi prosecutions of scams, and soft
  warnings/non-recognition statements; soft governance frameworks are context-only unless they
  mandate a restriction. (2) **temporal_tier rename** `discovery_only_2008_2012` →
  `discovery_only_2007_2012` (schema/controlled_vocab.yaml + event.schema.json + validate.py +
  build scripts + 19 events) so the census can represent 2007 (e.g. the e-gold 2007 indictment).
  (3) **+25 ISO-3166 jurisdiction codes** added to controlled_vocab.yaml (CR/DK/DZ/EC/EG/IQ/JO/KE/
  KH/KW/LB/LK/MA/MM/MX/NO/NP/PK/QA/SA/TN/TW/VE/VN/ZW) to unblock the S4 nation-state census.
  **Version 2.0.0 → 3.0.0 (major)** per the §"Effective" convention (decision-rule addition).
  Re-coding: the tier rename is mechanical (events keep their tier, renamed in place — all 268
  events validate); the §9 boundary governs *future* authoring + the morning audit of borderline
  candidates (tagged in census_gap_registry). IRR precondition N/A (mechanical rename + an
  inclusion rule that is a definitional scope choice, not a κ-driver). Existing events keep their
  `codebook_version`.
- **CODEBOOK CHANGE — 2026-05-30** — **§1.6 added: `asset_onchain` evidence floor
  & off-chain-mechanism exception**. Codifies the validator-enforced rule
  (`scripts/validate.py`: every non-draft `asset_onchain` observation needs ≥1
  `primary_onchain` `tx_hash`) plus the routing for effects whose mechanism is
  structurally off-chain (no tx can ever exist): carry at another layer, or stay
  `draft`; never reclassify a non-custodial bridge to `offramp_cex`; never
  fabricate a `tx_hash`. Surfaced by the C-5 audit (audit_id 460-462):
  `ren-protocol-shutdown-alameda-ftx-2022-12` is the terminal-`draft` precedent
  (off-chain RenVM darknode signature cessation), `makerdao-emergency-shutdown-
  contingency-2022-08` the representative-receipt null precedent, `binance-busd` /
  `paxos-busd` / `circle-usdc-svb` the route-to-another-layer precedents.
  **Version 1.0.1 → 2.0.0 (major).** Per the §"Effective" convention, any
  decision-rule change — here a decision-rule ADDITION — is a major bump. The two
  process preconditions are satisfied/N-A for this specific change: (3) re-coding
  is *vacuously satisfied* — zero events change coding, because §1.6 documents
  behavior `scripts/validate.py` already enforces and the routing precedents
  (binance-busd, paxos-busd, circle-usdc-svb, makerdao, ren-protocol) are already
  applied; (1) the IRR-pass precondition is N/A — the edge case is mechanically
  determined (a `tx_hash` either exists or cannot exist), not an interpretive
  κ-driver. Existing events keep their current `codebook_version` (per the 1.0.1
  precedent).
- **2026-05-19** — **§1.3 example #2 self-correction**. v0.3 review-queue audit
  of `semenov-ofac-2023` (audit_id 226 rolling back 225) verified the OFAC RA
  HTML at `sources/http_captures/semenov-ofac-2023/ofac-recent-actions/` and
  found **8 explicit "Digital Currency Address - ETH" entries** for Roman
  Semenov — same explicit format as KONDRATIEV (lockbit-affiliates-ofac-2024)
  and AEZA GROUP (aeza-group-ofac-2025). Codebook 1.0.0 claim that "OFAC SDN
  designation 2023-08-23 names Roman Semenov (person), not specific addresses"
  was **factually wrong**. §1.2 (A) is fully satisfied; combined with on-chain
  Tether blacklist transactions satisfying (B), **`direct`** is the correct
  attribution. Codebook example #2 corrected below. IRR κ=0.5833 driver is not
  codebook ambiguity on (A) — likely is interpretive variation on (B) public-
  confirmation reading (on-chain blacklist tx vs press release statement).
  Codebook version bumped 1.0.0 → 1.0.1 (minor; worked-example correction, no
  decision-rule change). No event YAMLs re-bump codebook_version; existing
  1.0.0 events stay at 1.0.0 (their attribution coding was correct under 1.0.0
  too — the example, not the rule, was wrong).
- **2026-05-17** — initial codebook (Phase A-F dryrun pipeline aftermath).
  Source: attribution κ=0.5833 (moderate) in IRR run dated 2026-05-15 with
  3 disagreement rows, all on `asset_onchain` stablecoin freezes
  (cryptex-ofac-2024 row 3, semenov-ofac-2023 rows 9-10).

---

## §1 Attribution (the κ=0.5833 driver)

### §1.1 Canonical definitions

| Value | Definition |
|-------|------------|
| `direct` | The named actor publicly references the trigger as the cause **and** the trigger names the target (specific actor / wallet / domain) being acted upon. |
| `plausible` | The action is causally consistent with the trigger but the actor either does not publicly reference the trigger, or the trigger does not name the specific target (class-level inference required). |
| `unknown` | An observed transition whose linkage to the named trigger is unresolved. May enter evidence chains but MUST NOT enter strong-attribution numerators or causal prose. |
| `none` | Reserved for `observed_no_change` and `coverage_gap` rows. |

### §1.2 Stablecoin-issuer compliance freezes (RULES, not aliases)

**Decision rule for `asset_onchain` freezes after an OFAC SDN designation:**

`direct` is REQUIRED when **both** of the following hold:
- (A) The OFAC SDN designation explicitly names addresses controlled by the
  freezing issuer's asset (e.g., USDT-on-Tron addresses for Tether,
  USDC-on-Ethereum addresses for Circle).
- (B) The freezing issuer (Tether, Circle, Paxos, etc.) publicly confirms the
  freeze on the named SDN addresses within the publicly-knowable compliance
  window (typically ≤ 24h post-SDN).

`plausible` is REQUIRED when **only one** of (A) or (B) holds:
- The SDN designation names a *person/entity* but does NOT pre-publish the
  specific asset-issuer addresses, AND the issuer freezes addresses inferred
  by Chainalysis / Elliptic / TRM to be controlled by the SDN'd target.
- OR: The SDN designation names addresses but the issuer's public statement is
  generic ("we comply with OFAC") and does not confirm freeze of the specific
  named addresses.

`unknown` is REQUIRED when:
- The SDN designation names neither the specific addresses nor the asset
  class, and the freeze is observed (via on-chain blacklist transactions) but
  the issuer has not made any public statement linking the freeze to the
  trigger.

### §1.3 Worked examples (from existing corpus)

These resolve the κ=0.5833 cases:

**1. `cryptex-ofac-2024` row 3 (asset_onchain)**:
- OFAC SDN designation 2024-09-26 (jy2570) specifically names USDT addresses
  controlled by Cryptex.net operators.
- Tether published a freeze confirmation in the public press cycle within 24h.
- ⇒ Both (A) and (B) → **`direct`** ✓ (matches gold key; resolves 3-agent
  blind dispute where 1 agent said `plausible`)

**2. `semenov-ofac-2023` rows 9-10 (asset_onchain)** — *corrected 2026-05-19 (v1.0.1)*:
- OFAC SDN designation 2023-08-23 names Roman Semenov **AND lists 8 explicit
  "Digital Currency Address - ETH" entries** (verified against
  `sources/http_captures/semenov-ofac-2023/ofac-recent-actions/ofac.treasury.gov__recent-actions-20230823__371ac1b7ba.html`):
  `0xdcbEfFBECcE100cCE9E4b153C4e15cB885643193`,
  `0x5f48c2a71b2cc96e3f0ccae4e39318ff0dc375b2`,
  `0x5a7a51bfb49f190e5a6060a5bc6052ac14a3b59f`,
  `0xed6e0a7e4ac94d976eebfb82ccf777a3c6bad921`,
  `0x797d7ae72ebddcdea2a346c1834e04d1f8df102b`,
  `0x931546D9e66836AbF687d2bc64B30407bAc8C568`,
  `0x43fa21d92141BA9db43052492E0DeEE5aa5f0A93`,
  `0x6be0ae71e6c41f2f9d0d1a3b8d0f75e6f6a0b46e`.
- Same explicit "Digital Currency Address - ETH" format as KONDRATIEV (LockBit
  affiliate, lockbit-affiliates-ofac-2024) and AEZA GROUP TRX address — both
  verified `direct`.
- Tether/Circle on-chain blacklist transactions (Etherscan tx hashes captured
  and usdtbanlist primary_corporate with body_hash) satisfy (B) under the
  public-confirmation-via-on-chain-tx reading: the issuer's own smart contract
  publicly executed `addBlackList(0x...)` with the named SDN address as
  parameter, which is the strongest possible public confirmation.
- ⇒ Both (A) and (B) → **`direct`** ✓ (matches gold key)
- **PRIOR CODEBOOK 1.0.0 CLAIM WAS FACTUALLY WRONG.** The 1.0.0 statement
  "OFAC SDN designation 2023-08-23 names Roman Semenov (person), not specific
  addresses" was contradicted by the actual OFAC RA HTML. Caught by v0.3
  review-queue self-correction loop (audit_id 226 rolling back 225) on
  2026-05-19. IRR κ=0.5833 driver is NOT codebook (A) ambiguity as 1.0.0
  hypothesized; if there is genuine coder disagreement, it lives elsewhere
  (e.g., variation on (B) public-confirmation reading; or simply
  coder noise).

**3. `tether-retroactive-sweep-2023` (asset_onchain, currently `direct`)**:
- 2023-12 Tether retroactive sweep of historical OFAC-listed addresses.
- OFAC pre-named the addresses (all from prior SDN actions, e.g., 2021-09 SUEX,
  2022-08 Tornado Cash) AND Tether's blog post explicitly enumerates the
  swept addresses with reference to the underlying SDN actions.
- ⇒ Both (A) and (B) → **`direct`** ✓

**4. `dydx-tornado-account-block-2022-08` (offramp_cex)**:
- OFAC SDN 2022-08-08 names Tornado Cash addresses (not dYdX or its users).
- dYdX's 2022-08-11 announcement explicitly cites Tornado Cash interactions
  in account histories as the block trigger.
- ⇒ (A) partially: the OFAC trigger names an upstream protocol, not the
  dYdX customer addresses. (B) holds: dYdX explicitly cites the trigger.
- ⇒ Closest fit: **`direct`** under §1.2 because the actor's public statement
  cites the trigger AND the trigger's protocol-level target is the actor's
  upstream dependency. This is the "guilt-by-association" boundary case.

### §1.4 Frontend-block / RPC-block attribution

For `l3_rpc` and `l4_frontend` blocks after a sanctioning trigger:

`direct` is REQUIRED when **both**:
- The blocking provider (Infura, Cloudflare, Alchemy, Aave UI, Uniswap UI)
  publicly cites the trigger in a blog post, ToS update, or compliance
  statement.
- The block is implemented within the publicly-knowable compliance window
  (typically ≤ 7 days post-trigger).

`plausible` is REQUIRED when:
- The provider does not publicly cite the trigger.
- OR: The block is implemented inferentially based on broader compliance
  policy (no per-trigger announcement).

### §1.5 Nation-state network-block attribution (L0)

For `l0_network` blocks: `direct` requires the blocking authority publicly cite
the trigger (typically the regulator naming the blocked domain or AS-set in
the order itself). Replayable OONI / Censored Planet / Cloudflare Radar
measurement is REQUIRED to elevate L0 coverage to `partially_measured` or
better — without it, the row is `not_measured` and no L0 observation can be
admitted. (See Kazakhstan 2022-01 honesty fix as precedent.)

### §1.6 `asset_onchain` evidence floor & the off-chain-mechanism exception

The on-chain analogue of the §1.5 L0 measurement floor: an on-chain claim must
point at an on-chain receipt.

**Evidence floor (validator-enforced).** Every `asset_onchain` observation —
`observed_change` AND `observed_no_change` — REQUIRES ≥ 1 `primary_onchain`
source carrying a real transaction hash (`tx_hash`). Drafts may defer it;
non-draft (`admitted`) events cannot. NEVER fabricate or guess a `tx_hash` to
clear the floor.

- For `observed_no_change` nulls the floor is met by a *representative* on-chain
  receipt showing the asset/contract operated normally inside the window (the
  absence-of-action anchor). Precedent: `makerdao-emergency-shutdown-
  contingency-2022-08` pins a PSM-USDC-A `sellGem` tx to show the peg module ran
  normally and Emergency Shutdown was NOT triggered.

**Off-chain-mechanism exception.** Some effects manifest in on-chain *state*
(an asset becomes frozen / unredeemable) but are produced by a mechanism with
NO on-chain transaction — e.g. a non-custodial bridge whose off-chain
darknode/relayer network stops signing, or a contract with no on-chain
pause/freeze entrypoint. For these the floor is *structurally unsatisfiable*: no
`tx_hash` can ever exist. Route, in order:

1. If the enforceable effect ALSO manifests at another layer with admission-grade
   evidence, code it THERE and set `asset_onchain: not_applicable`. Precedent:
   `binance-busd-wind-down-2024` / `paxos-busd-nydfs-minting-stop-2023` dropped
   the asset_onchain row and carried the issuer action at `offramp_cex` /
   `l4_frontend`; `circle-usdc-svb-policy-statement-2023` moved its null from
   `asset_onchain` to `offramp_cex` (the claim is about the redemption / off-ramp
   surface, not an on-chain action).
2. A non-custodial bridge is NOT a centralized-exchange off-ramp. Do NOT
   reclassify `asset_onchain → offramp_cex` merely to escape the floor — that
   corrupts the six-layer semantics (a darknode network ≠ a CEX).
3. If no other layer carries the effect with admission-grade evidence, the event
   REMAINS `draft`. This is an honest, structurally-terminal state — NOT a
   backlog item awaiting a `tx_hash` that can never be produced. Record a
   machine-visible `note` on the observation stating the floor is structurally
   unsatisfiable and the event is intentionally un-promotable. Precedent:
   `ren-protocol-shutdown-alameda-ftx-2022-12` (RenVM 1.0 wind-down via off-chain
   `mintAuthority` signature cessation; `MintGatewayLogicV1` has no on-chain
   pause).

---

## §2 Coverage status (κ=1.0 currently; defensive doc)

Coverage status currently has κ=1.0 from the IRR pass. The following rules are
defensive documentation, not codebook-change drivers:

- `measured`: A replayable artifact exists at the layer for this event's
  scope. For L0 this means `sources/l0_datasets/<event>/` slice exists.
- `partially_measured`: A replayable artifact exists but does not exhaust
  the scope. Most non-comprehensive L0/L3 events.
- `not_measured`: No replayable artifact captured. Coverage gap.
- `not_applicable`: The layer does not meaningfully apply to this event
  (e.g., bitcoin-only events have `l3_rpc: not_applicable`).

**Hard rule (Kazakhstan precedent)**: `partially_measured` or `measured`
REQUIRES the corresponding row in `derived/{layer}_coverage_summary.csv`
where applicable. Documented-but-uncaptured measurement claims must be
coded as `not_measured` until the dataset slice is pinned.

---

## §3 Empirical shape (cascade vs comparison vs null)

| Value | Decision rule |
|-------|---------------|
| `cascade` | ≥ 3 distinct `observed_change` layers (any attribution level). |
| `comparison` | 1 or 2 distinct `observed_change` layers. |
| `null_event` | 0 `observed_change` layers; admission requires `observed_no_change` with admission-grade sources. |

**Phase A-F learning**: Multiple agents wanted a `case_study` value for
single-event narrative exposition. **Decision**: `case_study` is NOT a valid
empirical_shape. Single-event narrative exposition fits inside
`empirical_shape: comparison` or `null_event` depending on cascade count.
For narrative emphasis use `admission_tier: anchor_case` instead.

---

## §4 Admission tier

| Value | Decision rule |
|-------|---------------|
| `anchor_case` | ≥ 2 `observed_change` layers with attribution ∈ {`direct`, `plausible`}. |
| `empirical_case` | ≥ 1 strong-attribution (`direct`/`plausible`) `observed_change` layer. |
| `null_case` | 0 strong-attribution `observed_change` layers (denominator control). |

`unknown` and `none` attribution rows DO NOT count toward strong-attribution
layer counts.

---

## §5 Trigger types (Phase A-F enum-gap learning)

### §5.1 Canonical decision matrix

| Trigger family | Canonical trigger.type | Sub-rules |
|----------------|------------------------|-----------|
| OFAC SDN add | `ofac_sdn_designation` | |
| OFAC SDN remove | `ofac_sdn_removal` | |
| DOJ criminal indictment | `doj_indictment` | |
| DOJ seizure warrant | `doj_seizure_order` | |
| US SEC enforcement | `sec_action` | |
| US CFTC enforcement | `cftc_action` | |
| US FinCEN admin action | `fincen_action` | |
| US court civil order (non-DOJ) | `court_civil_order` | DataCell Iceland 2012-07; consumer-protection class actions. |
| EU/UN/G7 sanctions | `non_us_sanctions` | EU Russia sanctions packages. |
| EU/UN/G7 regulation (non-sanctions) | `supranational_regulation` | MiCA, FATF R15, TFR, AMLA. |
| Corporate unilateral policy | `corporate_policy_change` | Tether/Circle freezes (when issuer-initiated), exchange delistings. |
| Nation-state ISP/DNS block | `nation_state_block` | KZ shutdown, CN PBoC, NG CBN, India RBI, TR CBRT, IR sanctions. |
| **Non-US national regulator administrative enforcement** | `regulatory_enforcement` | **NEW 2026-05-17**: JP FSA business improvement orders, KR FSC institutional restrictions, IS CBI advisories, etc. Use this when the actor is a non-US national regulator AND the action is administrative (not a network/payment-rail block). |

### §5.2 Stratum-actor map (validator-enforced)

| trigger.type | Permitted research_stratum |
|--------------|---------------------------|
| `ofac_sdn_designation` / `ofac_sdn_removal` | `S1_ofac_sdn` / `S2_ofac_removal` |
| `doj_indictment` / `doj_seizure_order` / `sec_action` / `cftc_action` / `fincen_action` / `court_civil_order` | `S3_doj_sec_cftc_fiod` |
| `nation_state_block` / `regulatory_enforcement` | `S4_nation_state` |
| `corporate_policy_change` | `S5_corporate` |
| `non_us_sanctions` / `supranational_regulation` | `S6_supranational` |

---

## §6 Analysis use

Phase B/E agents kept asking for `contextual_baseline` and `discovery_only`
(short forms not in the enum). The canonical values are:

| Temporal tier | Canonical analysis_use | Aliases agents attempted |
|---------------|------------------------|--------------------------|
| `discovery_only_2007_2012` | `discovery_ledger_only` | `discovery_only` |
| `historical_baseline_2013_2016` | `historical_baseline` | `contextual_baseline` |
| `comparable_main_2017_present` | `comparable_analysis` | `comparative_analysis` |

**Aliases are NOT accepted by the validator**. Authoring agents MUST use the
canonical form.

---

## §7 Target enumeration

| Value | Meaning |
|-------|---------|
| `complete` | All targets in scope are enumerated in `target.canonical_*`. |
| `subset` | A non-exhaustive enumeration of named targets. Document the class-level rationale in `enumeration_note`. |
| `pending` | Enumeration not yet captured; coding incomplete. |

**Phase A-F learning**: Multiple agents wanted `class_level` for FATF, MiCA,
and other regulatory-class events. **Decision**: `class_level` is NOT a valid
target.enumeration. Use `subset` and explain class-level rationale in the
`enumeration_note` text field.

---

## §8 Codebook compliance for LLM authoring agents

When an LLM agent authors a new event YAML:

1. **Read this codebook first** if any of the following fields are being set:
   `attribution`, `empirical_shape`, `admission_tier`, `trigger.type`,
   `analysis_use`, `target.enumeration`.
2. **Use ONLY canonical enum values** from §5/§6/§7 and from
   `schema/controlled_vocab.yaml`.
3. **For attribution `direct` vs `plausible`**, apply §1.2-§1.5 decision rules.
   Document the rule applied in `analysis_notes`.
4. **If a coding decision is ambiguous**, default to the more conservative
   value (`plausible` over `direct`; `null_case` over `empirical_case`) and
   flag in `analysis_notes` for human reviewer.
5. **DRYRUN preamble** is REQUIRED in `analysis_notes` for all
   `origin: agent_draft` events: `**NEW EVENT AUTHORED — DRYRUN YYYY-MM-DD**`.

---

## §9 Inclusion boundary — what counts as a *censorship* case

The corpus is a census of **crypto-stack censorship**. A case is IN scope only if it is an
**action that denies, blocks, seizes, freezes, delists, geofences, or debanks** a *legitimate*
crypto platform / asset / user — i.e. a deliberate restriction of access or service by a state
or corporate actor. (User-blessed 2026-05-31.)

**INCLUDE** (censorship actions):
- Nation-state bans / ISP-DNS blocks / payment-rail prohibitions / account-closure orders.
- OFAC SDN designations + sanctions-package service bans (S1/S6).
- DOJ/SEC/CFTC/FinCEN enforcement **that restricts or shuts a legitimate platform/operator**
  (e.g. EtherDelta DEX charge, LBRY suit, Liberty Reserve takedown).
- Corporate denials: exchange delistings, jurisdiction exits/geofences, issuer freezes
  (Tether/Circle/Paxos), frontend/RPC blocks, payment-processor/bank debanking.

**EXCLUDE** (not censorship):
- **Platform FAILURES** — fraud, hacks, theft, insolvency, voluntary collapse (e.g. Cryptsy,
  Mt.Gox-collapse-*as-such*, QuadrigaCX). A platform failing ≠ being censored.
- **Fraud/Ponzi prosecutions** of inherently-illegitimate schemes (e.g. OneCoin, Centra Tech,
  BitConnect, HyperFund). The state is prosecuting a scam, not censoring a legitimate service.
- **Soft warnings / non-recognition statements / consumer advisories** that neither deny nor
  block a service (e.g. CFPB 2014 advisory, ESA 2013 warning, India RBI 2013 caution,
  central-bank "not legal tender" statements). Record only as null/context if at all.

**BORDERLINE — soft governance frameworks** (FATF/IOSCO/FSB/BCBS recommendations): these are
censorship-*enabling* infrastructure, not censorship *actions*. INCLUDE only when the instrument
directly **mandates** a restriction (e.g. FATF Travel Rule operationalization, EU TFR, BCBS
punitive capital weights that force debanking); otherwise context-only.

**Test:** "Did a state/corporate actor deliberately restrict access to or service of a
legitimate crypto platform/asset/user?" If yes → include. If the platform merely failed, or the
target was a pure scam, or the instrument is only advisory → exclude (or null/context).
