# Codebook — coding rules for fuzzy edges

**Purpose**: This codebook formalizes coding decisions for fields where κ < 0.6 in
the latest IRR run, or where Phase A-F authoring agents independently surfaced
ambiguity. It is the **canonical reference** that LLM authoring agents and human
coders MUST consult before assigning these fields.

**Version**: 1.0.0.

**Effective**: 2026-05-17. Codebook updates require:
1. A new IRR pass on at least 10 events covering the edge case.
2. A `**CODEBOOK CHANGE — YYYY-MM-DD**` entry in this file's changelog.
3. Re-coding of all events touching the changed field, with `last_human_audit`
   stamp refresh.

**Authority**: This file binds both human coders and LLM authoring agents. When
a citation in this codebook contradicts agent intuition, the codebook wins.

---

## Changelog

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

**2. `semenov-ofac-2023` rows 9-10 (asset_onchain)**:
- OFAC SDN designation 2023-08-23 names Roman Semenov (person), not specific
  addresses.
- Tether/Circle freezes are observed on inferred-Semenov-controlled Tornado
  Cash-adjacent addresses, but issuer public statements are generic compliance
  language.
- ⇒ Only (A) is partially satisfied (person named, not addresses) → **`plausible`**
- This CONTRADICTS the original gold key (which said `direct`) — codebook
  decision: recode key to `plausible` and re-run IRR.

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
| `discovery_only_2008_2012` | `discovery_ledger_only` | `discovery_only` |
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
