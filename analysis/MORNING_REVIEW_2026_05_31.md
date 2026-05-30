# ☀️ Morning review — overnight census run (2026-05-31)

**TL;DR:** Overnight, the autonomous run authored **5 new events** (corpus 254 → **259 admitted**, all
validate), built a **44-row verified+scope-tagged census gap registry**, and produced an **S4
roadmap**. Everything is local-committed (never pushed), fully reversible. Below is the prioritized
action plan. Full chronological detail: `analysis/overnight_collection_notes_2026_05_31.md`.

---

## A. DECISIONS I NEED FROM YOU (in priority order — they unblock the bulk authoring)

**A1 — Scope boundary (affects every stratum).** Define what counts as a *censorship* case. My
recommendation: **INCLUDE** state/corporate denial/blocking/seizure/freeze/delisting that restricts a
*legitimate* platform/asset/user; **EXCLUDE** (or mark null/context) (a) exchange *failures* —
fraud/hack/insolvency (Cryptsy, OneCoin, Centra), and (b) *soft warnings / non-recognition statements*
(CFPB 2014, ESA 2013, India RBI 2013 caution, IOSCO/FSB recommendations). I tagged every borderline
registry row with this lens so the rule applies mechanically once you bless it.

**A2 — Add a 2007 temporal_tier.** The enum starts at `discovery_only_2008_2012`; the "since 2007"
census can't represent 2007. Recommendation: rename → `discovery_only_2007_2012` (schema/event.schema.json
+ validate.py refs + codebook changelog). Unblocks the **e-gold 2007 indictment** (the #1 "since 2007"
anchor — sources already captured at `sources/http_captures/egold-doj-indictment-2007-04/`).

**A3 — Add ~25 ISO country codes to schema/controlled_vocab.yaml.** Additive, low-risk. The exact list +
rationale: `analysis/s4_census_prep.md`. Unblocks the **S4 nation-state census (~106 candidates)** — the
single biggest coverage gain.

## B. THEN — bulk authoring (gated on A2/A3), in priority order
1. **S4 nation-state (~50-70 net-new after dedup/scope)** — biggest gain. Roadmap + dedup map + templates
   in `analysis/s4_census_prep.md`. Heavily weighted to the under-collected 2013-2020 era.
2. **S1 OFAC SDN (24)** — repetitive `null_case` template (use `bitriver-russia-mining-ofac-2022-04`
   [authored tonight] + `zservers-ofac-2025`). Fast batch.
3. **S3 DOJ/SEC (enforcement-censorship subset)** — EtherDelta(first DEX), LBRY, Kik are author-ready;
   Colonial Pipeline needs an on-chain seizure tx_hash (§1.6).
4. **S6 supranational** — EU Russia-sanctions crypto bans are the clear censorship cases (verify exact
   packages); FATF/BCBS are censorship-enabling; IOSCO/FSB are soft (apply A1).
5. **S5 corporate** — Tether issuer-freezes (Garantex etc.) need on-chain freeze tx_hash; rest are
   delisting/exit templates.

## C. The 5 events I authored tonight (please spot-check)
| event | stratum | why notable |
|---|---|---|
| liberty-reserve-coordinated-takedown-2013-05 | S3 | seminal §311+DOJ takedown; corpus had only the 2011 denial |
| tradehill-dwolla-payment-cutoff-2012-02 | S5 | earliest financial-rail debanking |
| bitriver-russia-mining-ofac-2022-04 | S1 | first OFAC sanction of a crypto-mining company |
| bittrex-privacy-coin-delisting-2021-01 | S5 | first US-exchange privacy-coin delisting |
| nigeria-binance-network-block-2024-02 | S4 | OONI-anchored l0 telco block + exec detention |
All: real verified sources, body_hash-pinned, validate `[OK]`, audit_log ids 465-469.

## D. Artifacts
- `analysis/census_gap_candidates.tsv` — 264 candidates (work-list, agent-sourced — verify before authoring).
- `analysis/census_gap_registry.tsv` — 44 rows I verified + scope-tagged + dedup-checked overnight.
- `analysis/census_gap_list.md` — gap-discovery synthesis (per-stratum×era + coverage estimates).
- `analysis/s4_census_prep.md` — the S4 batch roadmap.
- `analysis/overnight_collection_notes_2026_05_31.md` — chronological tick log + all flagged decisions.

## E. Dedup catches (so you don't double-count)
- philippines-ntc-2024 candidate = corpus `philippines-sec-binance-block-2024` (audited C-5) → drop.
- infura-venezuela candidate = corpus `infura-metamask-donetsk-luhansk-block-2022-03` (audited C-5) → drop.
- huobi-2022 candidate = corpus `huobi-htx-privacy-coin-delisting-2024` (the one we re-dated) → drop.
- Internal gap-discovery dups collapsed: Jordan/Iraq/Bangladesh/Vietnam/Indonesia-BI/Canada-CSA (×2 each).
