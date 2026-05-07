# Decision Rubric — Structural Checklist

A short, hand-followed rubric derived from the dataset's findings. Given
a proposed action or a new event under observation, walk through the
items below and record a yes/no/unknown for each; the rubric then
surfaces which historical patterns the situation most resembles.

> ⚠️ **This is comparison, not prediction.** The rubric translates
> structural features into "which historical patterns apply"; it does
> not assign probabilities. Read
> [`docs/limitations-and-use.md`](limitations-and-use.md) first.
> If you use this rubric's output in a brief, memo, or risk model, the
> responsibility for that use is yours — the admitted dataset is 53 events and
> will never be large enough to support automated decisions.

---

## How to use

1. Answer each item for the action under analysis. If you don't know,
   mark `unknown` — don't guess.
2. For each `yes`/`no` answer, read the pattern block below the item:
   which historical events fit this branch, and what their cascade
   shapes tell you.
3. At the end, use [`scripts/find_comparable_cases.py`](../scripts/find_comparable_cases.py)
   to retrieve the top-N ranked precedents with full evidence chains.
4. Do not treat the rubric output as an answer. Treat it as a list of
   historical cases you now need to read in detail.

---

## Part 1 — Trigger structure

### 1.1 What kind of actor is taking the action?

- `US_OFAC` → Stratum S1 (SDN designation) or S2 (delisting)
- `US_DOJ` / `US_DOJ_SDNY` / `US_DOJ_EDPA` / etc. → S3; admitted examples include seizure-warrant cases
- `US_SEC` → S3, civil-enforcement axis
- `US_CFTC` → S3, commodities axis
- `EU_Council` → S6, either sanctions or regulatory framework
- Single-country central bank / national regulator → S4
- Stablecoin issuer / exchange / frontend operator (corporate) → S5

**Pattern call-outs:**

- **SEC civil actions** are repair-queue candidates unless platform,
  banking-rail, or frontend artifacts are pinned directly. Binance
  (2023-06-05) and Coinbase (2023-06-06) remain draft candidates after
  the legal-source-only review; the admitted SEC contrast at v0.1 is
  narrow: Uniswap Wells notice (2024-04, no formal filing) → no L4
  cascade in the scoped window.
- **DOJ indictments paired with same-day domain seizure** (Bitzlato,
  ChipMixer, Samourai, Cryptex, BTC-e) are the admitted precedents for
  same-day `measured` L4 observed_change rows.
- **EU regulatory frameworks** (MiCA) vs **EU sanctions packages**
  (12th Russia package) have structurally different observables: the
  admitted examples record phased CASP-compliance rollout for MiCA and
  account-class closure within ~90 days for the 12th Russia package.

### 1.2 Does the action enumerate specific on-chain addresses?

- **Yes**: falls under the OFAC-SDN pattern class (S1), even if the
  triggering authority is not OFAC. Address-level enumeration makes
  the asset-layer cascade directly observable.
- **No, entity-level only** (Lazarus Group 2019, Sichuan Silence,
  Matveev): asset-layer cascade is at most inferential. CEX cascade
  is the only publicly-observable layer.
- **No, user-class** (EU 12th Russia sanctions): no wallet list at all.
  Observable signal is exclusively at the `offramp_cex` layer via CASP
  account-closure compliance.
- **No, jurisdiction-level** (India RBI, Nigeria CBN, Turkey CBRT):
  bank-rail severance is the mechanism, not address blacklisting.

### 1.3 What is the target actor type?

- `mixer_service` (Blender, Tornado, Sinbad, ChipMixer, Samourai):
  admitted examples separate protocol availability from frontend
  availability. Record frontend/protocol decoupling as a comparison cue.
- `exchange` (SUEX, Chatex, Cryptex, Garantex, Grinex, BTC-e):
  canonical domain is a primary cascade target. Foreign-operated
  exchange examples in the corpus retain public-domain artifacts; US
  seizure examples carry different L4 evidence.
- `individual` (Semenov, Pertsev, Storm, LockBit affiliates, Matveev):
  admitted examples in this branch lack a public L4 artifact; asset-layer issuer
  action is visible only when the individual target holds a freezeable
  stablecoin balance. Lazarus-BTC examples have no asset-layer primitive.
- `hosting_provider` (Aeza, Zservers, Funnull): admitted examples show
  hybrid behavior: customer-facing infrastructure may move while the
  provider entity remains observable.
- `state_sponsored_cyber_group` / `entity` (Lazarus 2019, Sichuan
  Silence): admitted entity-level designations with no on-chain targets
  have negligible public cascade evidence in this corpus.

---

## Part 2 — Target properties

### 2.1 Which chains are targeted?

- Bitcoin only → asset-layer cascade is `not_applicable` (no issuer
  freeze primitive on native BTC). `offramp_cex` is the only asset-
  adjacent observable.
- Ethereum (incl. USDC/USDT on ETH) → Circle + Tether blacklist
  actions are observable via `usdtbanlist.com` tracker and Etherscan
  tx hashes in admitted examples. Use recorded event deltas as
  comparison evidence, not as a forecast.
- TRON (USDT-TRC20) → Tether is the relevant issuer in the admitted
  examples; compare against ETH-USDT rows without importing Circle
  behavior.
- Litecoin / Dash / ZEC / BTG etc. → admitted chain-diverse designations
  record no asset-layer freeze primitive on those minor-chain addresses.

### 2.2 Is there a canonical domain / frontend owned by a US-jurisdiction
entity (or US-compliance-adjacent infrastructure)?

- **Yes, US-jurisdiction**: compare against admitted L4 timing examples
  such as Tornado `tornado.cash` (~22h via compliance-driven CDN drop),
  dYdX (~34h), and Cryptex (same-day USSS seizure).
- **Yes, foreign operator + foreign infrastructure**: compare against
  admitted persistence examples such as Sinbad `sinbad.io` reachable
  10+ days post-event, SUEX `suex.io` remaining up, and Grinex remaining
  up before the Tether freeze.
- **No canonical domain** (individual designations, hosting providers
  with no customer-facing site): L4 is `not_applicable`.

### 2.3 Is the protocol a smart-contract system with operator-
independent execution?

- **Yes** (Tornado, Ooki, Uniswap): the frontend/protocol split is
  observable. US frontend operator may take down the UI, but the
  smart contracts remain callable; users may switch to alternative
  frontends. `uniswap-frontend-delisting-2023` and `cftc-v-ooki-dao-2022`
  are the clearest exemplars.
- **No** (exchange operated by a corporate entity, mixer with
  centralized off-chain components): takedown of the operator ends
  the service. Bitzlato, ChipMixer, Samourai, Cryptex all fit this
  pattern.

---

## Part 3 — Issuer-compliance comparison cues (for stablecoin-holding targets)

### 3.1 Is USDC involved?

In admitted examples, Circle actions can be compared by recorded
`delta_hours`: the 2022-08-08 Circle blacklist action against Tornado
Cash addresses fired at 2022-08-08 19:25 UTC, ~6 hours after OFAC
designation; Semenov 2023, LockBit 2024, Cryptex 2024, Funnull 2025,
and Grinex 2025 are same-day or next-day Circle rows for enumerated
addresses that held USDC.

### 3.2 Is USDT involved?

Tether examples in the admitted corpus are multi-modal:

- **Fast / OFAC-reactive admitted examples**: Cryptex 2024-09-26 03:37 UTC,
  Funnull 2025-05-29 10:15 UTC, Grinex 2025-08-14 21:15 UTC.
- **Retroactive** (pre-2024 targets): SUEX 2021 / Chatex 2021 / Russia-
  election 2020 / Russian-cyber-theft 2020 addresses were all frozen
  by Tether in a single 2023-12-09 04:34–05:36 UTC batch — 2–3 years
  after the original OFAC designations (`tether-retroactive-sweep-2023`).
- **Pre-commit (ahead of OFAC)**: `tether-dprk-precommit-freeze-2025`
  shows Tether freezing DPRK USDT addresses on 2025-04-30 / 05-08,
  188 days *before* the 2025-11-04 OFAC designation.
- **DOJ-request-only**: `tether-doj-pig-butchering-freeze-2023`
  documents Tether freezing $225M USDT at USSS / DOJ request, with
  no OFAC SDN at all.

The pattern call: Tether may act before, after, or without an OFAC
trigger. Do not assume OFAC is the only trigger.

### 3.3 Is the target a smart-contract address (protocol pool) or an
individual-wallet address?

- **Individual wallets**: in admitted asset-freeze examples, issuer action
  appears when the target is an enumerated wallet holding a freezeable
  asset. Treat this as a corpus-scoped pattern, not an issuer-wide
  compliance-rate estimate.
- **Smart-contract pool addresses** (Tornado redesignation cohort,
  Uniswap pools): current admitted cases show structural asymmetry between
  wallet-level freezes and protocol-contract addresses. Treat this as an
  illustrative mechanism, not a prevalence estimate over all pool contracts.

---

## Part 4 — Cross-layer comparison summary

Given the answers above, use this reference table to identify which
historical pattern class the situation most resembles:

| Pattern class | Example events | Observed layers in admitted precedents |
|---|---|---|
| **US-protocol cascade** (3+ layers, anchor) | `tornado-cash-ofac-2022`, `tornado-cash-ofac-delisting-2025` | L1 + L4 + asset + offramp |
| **US-exchange seizure** | `cryptex-ofac-2024`, `bitzlato-doj-2023`, `samourai-doj-2024` | L4 (USSS banner) + asset |
| **Foreign-operator persistence (null)** | `sinbad-ofac-2023`, `suex-ofac-2021`, `grinex-garantex-successor-ofac-2025` (partial) | asset only; L4 remains up |
| **Individual-wallet (null L4, fast asset)** | `semenov-ofac-2023`, `lockbit-affiliates-ofac-2024` | asset only |
| **Individual-BTC-only (anchored null control)** | `lazarus-laundering-ofac-2020`, `matveev-ofac-2023`, `iran-ransomware-ofac-2018` | offramp_cex null only |
| **Entity-only (null)** | `lazarus-entity-ofac-2019`, `sichuan-silence-ofac-2024` | offramp_cex null only |
| **SEC formal-complaint comparisons** | `sec-v-binance-2023`, `sec-v-coinbase-2023` | admitted only for scoped CEX/platform-service reactions; no L4, asset, L1/L3, or token-delisting claim |
| **SEC low-intensity (null)** | `sec-v-uniswap-wells-notice-2024` | none |
| **Nation-state central bank** | `india-rbi-crypto-ban-2018`, `china-pboc-crypto-ban-2021`, `turkey-cbrt-crypto-ban-2021`, `nigeria-cbn-crypto-ban-2021` | offramp_cex only, via bank-rail severance |
| **Nation-state emergency freeze** | `canada-convoy-freeze-2022` | offramp_cex + private-RCMP channel |
| **EU supranational regulatory** | `eu-mica-2023` | offramp_cex (CASP compliance phased) |
| **EU supranational sanctions** | `eu-12th-russia-sanctions-2023` | offramp_cex (class closure within 90d) |
| **Corporate issuer policy (OFAC-reactive)** | `circle-usdc-tornado-2022` | asset only |
| **Corporate issuer policy (non-OFAC)** | `tether-doj-pig-butchering-freeze-2023`, `tether-retroactive-sweep-2023`, `tether-dprk-precommit-freeze-2025` | asset only |
| **Frontend-only restriction** | `uniswap-frontend-delisting-2023`, `cftc-v-ooki-dao-2022` | L4 only; protocol persists |

---

## Part 5 — Honest red flags

If any of the following apply, stop and consider whether the rubric
applies at all:

1. **The trigger involves a new chain (Solana, Polygon, BNB Chain)**.
   The dataset has zero events on these chains; no historical pattern
   applies. See [`docs/chain-coverage-note.md`](chain-coverage-note.md).
2. **The trigger involves a non-US, non-EU, non-G7 jurisdiction**.
   The admitted dataset has only 53 events; many nation-state slots have a
   single precedent or none. Do not extrapolate.
3. **The top comparable case from `find_comparable_cases.py` has a
   match score below 40% of max**. That is the structural-novelty
   signal. Document the query as "outside dataset coverage".
4. **The trigger involves a novel actor combination** (e.g., a CFTC
   action against a DeFi protocol that has no named operator). Only
   `cftc-v-ooki-dao-2022` speaks to this — and it's N=1.

---

## Part 6 — Next steps

1. Run `scripts/find_comparable_cases.py --like <most-similar-event>`
   (or with your query features) to get the top-5 ranked precedents.
2. For each top-5, read the full evidence chain at
   `analysis/evidence-chains/<slug>.md`.
3. Verify each precedent's `body_hash`'d primary sources match the
   committed file hashes at the current dataset version.
4. Write your own argument, citing the precedents; do not cite the
   rubric.

The rubric's purpose is to shorten the retrieval step, not to
substitute for domain-expert judgment.
