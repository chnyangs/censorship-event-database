# Draft admission adjudication — 2026-06-09

Per-draft adjudication of the 45 draft events against codebook §9 (inclusion
boundary), §10 (evidence_tier), and §1.6 (asset_onchain floor), via three
two-stage workflows (adjudicate / re-adjudicate / fix-plan, each with an
adversarial verify stage) plus maintainer-applied controlled edits.

**§9 policy decision (maintainer):** OFAC SDN designations (research_stratum S1)
are IN SCOPE unconditionally, consistent with 35 existing admitted analogs
(lockbit / lazarus / hamas / fentanyl OFAC designations, many coded null_event).
The first pass wrongly rejected 6 S1 OFAC criminal-designation drafts on an
over-strict scope reading; they were re-adjudicated as in-scope.

**Reliability:** all promotions are LLM-adjudication + maintainer-oversight grade
(`origin: human_reviewed`), NOT independent-human IRR — the corpus-wide
reliability caveat still applies.

## Outcome

Corpus advanced **365 -> 392 admitted** (45 draft -> 12 draft; 10 -> 16 rejected):
**27 promoted, 6 rejected, 12 held draft.**

### Promoted to admitted (27)

Clean (8): bangladesh-bank-fepd-2022, bitcoin-maven-tetley-doj-2018,
bitfinex-us-retail-exit-2017, kuwait-cma-2023, magic-eden-ofac-block,
nydfs-bittrex-2019, circle-usdc-sealed-16-address-freeze-2026,
tether-ofac-iran-344m-freeze-2026.

S1 OFAC designations recoded to null_event (6): fayzimatov-alqaeda-2021,
task-force-rusich-2022, dprk-song-2025, dprk-amnokgang-2026, cambodia-kok-an-2026
(admission_grade); sinaloa-cartel-2026 (attested_secondary). Each mirrors the
china-fentanyl-network-ofac-2023-10 null-anchor template.

Round-1 holds fixed and admitted (13):
- offramp/L4 observed_change kept (captured primary): celsius-multistate-2021,
  ethiopia-nbe-p2p-2026, eu-belarus-wallet-ban-2025, falcon-labs-cftc-2024,
  crypto-capital-fowler-2019.
- asset_onchain issuer freezes with primary_onchain tx_hash kept:
  circle-usdc-multichain-freeze-2023, t3-bybit-usdt-freeze-2025,
  tether-okx-225m-freeze-2025.
- attested_secondary (single contemporaneous secondary source, attribution
  downgraded to plausible): kucoin-cftc-us-ban-2026, nigeria-sec-binance-2023.
- attested_secondary null_event (asset freeze reported but unanchored per §1.6):
  circle-freeze-zama-cusdc-2026.

### Rejected — out of scope per §9 (6)

bittrex-global-shutdown-2023 (voluntary self-shutdown / platform failure);
japan-fsa-leverage-cap-2020 (prudential product rule); kyrgyzstan-nbkr-warning-2014,
lebanon-bdl-warning-2013, saudi-committee-warning-2018, vietnam-sbv-statement-2014
(soft warnings / non-recognition advisories).

### Held draft (12) — fixable, not yet admitted

- bitcoin-fog-sterlingov-2024 — asset_onchain fails §1.6 (no tx_hash) + coverage_gap
  observation; needs null recode.
- ethiopia-nbe-crypto-ban-2022 — advisory; single supporting source, cannot meet
  the rejection-anchor or admission floor.
- ren-protocol-shutdown-ftx-2022 — author-pinned non-promotion draft (off-chain,
  un-anchorable wind-down); left deliberately parked.
- thailand-sec-exchange-block-2025, ethiopia-nbe-website-block-2025 — REAL ISP
  blocks (genuine censorship signal); need controlled coding + precision resolution.
- ens-eth-tornado-2022 — null (ENS took no action); needs the OFAC RA source wired
  into the observation + DRYRUN-note cleanup.
- tornado-cash-storm-conviction-2025 — sole primary_legal source has a Wayback slug
  mismatch; needs a clean replayable capture.
- §9 DOJ-criminal-prosecution group, deferred to a finer §9 pass (5):
  colonial-pipeline-darkside-2021, netwalker-2022, revil-2021,
  terror-financing-seizure-2020, t3-financial-crime-unit-launch-2024.

## Follow-up: §9 consistency audit

The 5 deferred DOJ-criminal drafts lean §9-EXCLUDE under the DOJ clause, but
terror-financing-seizure-2020 has an admitted analog (israel-nbctf-hamas-2021),
and the corpus already admits many OFAC criminal designations. A §9 consistency
sweep of existing admitted DOJ/seizure events is recommended before submission.
