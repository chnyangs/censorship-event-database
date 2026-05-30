# S4 nation-state census — morning prep (overnight tick 10, 2026-05-31)

The S4 nation-state stratum is the **largest census gap (106 candidates** in `census_gap_candidates.tsv`).
Most are blocked overnight by the `controlled_vocab.yaml` jurisdiction enum. This doc prepares the
whole S4 batch so the morning can: (1) bless the ISO-code additions, (2) batch-author, (3) dedup.

## 1. Vocabulary: ISO-3166 codes to ADD to schema/controlled_vocab.yaml
The current enum has ~42 codes. The S4 candidates need these **~25 additional** codes
(all valid ISO-3166 alpha-2; additive, low-risk):

```
CR (Costa Rica)  DK (Denmark)   DZ (Algeria)   EC (Ecuador)   EG (Egypt)
IQ (Iraq)        JO (Jordan)    KE (Kenya)     KH (Cambodia)  KW (Kuwait)
LB (Lebanon)     LK (Sri Lanka) MA (Morocco)   MM (Myanmar)   MX (Mexico)
NO (Norway)      NP (Nepal)     PK (Pakistan)  QA (Qatar)     SA (Saudi Arabia)
TN (Tunisia)     TW (Taiwan)    VE (Venezuela) VN (Vietnam)   ZW (Zimbabwe)
```
(Already in vocab, no action: AE/AR/KZ etc.)

## 2. Authorable NOW (jurisdiction already in vocab) — 20 jurisdictions
`BD BE BO CA CN FR ID IN IR JP KG KR MY NG PH RU SG TH UA US`
→ These S4 candidates can be authored without any vocab change. BUT many are **multi-stage /
near-dups of existing corpus events** (same country, different year/action) — dedup first
(see §3). Cleanest net-new authorable: countries with a candidate that has no corpus sibling.

## 3. Dedup-density map (countries with multiple S4 candidates → multi-stage or dup)
`US(9) CN(6) IN(5) ID(5) KR(5) NP(4) PK(4) TH(4)` and others. These need dedup review against
the corpus (e.g. China already has 6 corpus events 2013-2022; India has the 2013 caution +
2018 ban + 2022 tax + 2024 FIU). Treat each distinct *action* as one event; collapse
duplicate gap-discovery rows (already caught: Jordan/Iraq/Bangladesh/Vietnam ×2 each).

## 4. Scope tagging (feeds the inclusion-boundary decision)
Within S4, separate (per the scope-boundary flag in overnight_collection_notes):
- **HARD BANS / blocks / account-closures / seizures** → CENSORSHIP (include). e.g. China bank-account
  closure 2014, Vietnam/Ecuador/Jordan/Nepal/Morocco/Iraq/Bangladesh prohibitions, Nigeria CBN 2021.
- **SOFT WARNINGS / "not legal tender" / non-recognition statements** → context/null only. e.g. India RBI
  2013 caution, the EU central-bank "not-currency" cluster (France/Norway/Belgium/Denmark 2013-14),
  Mexico/Malaysia/Taiwan statements.

## 5. Recommended morning workflow for S4
1. Add the §1 ISO codes to controlled_vocab.yaml (one additive commit).
2. Apply the scope rule (§4) — drop pure soft-warnings or mark them null/context.
3. Batch-author the deduped hard-ban set using a same-stratum template (e.g. nigeria-cbn-crypto-ban-2021,
   thailand-bot-bitcoin-prohibition-2013, india-rbi-crypto-ban-2018). The S4 offramp_cex/l0/l4 patterns
   are well-established in the corpus.
4. Spot-verify each candidate's source URL (agent-provided, may be off) before authoring — capture via
   Wayback, body_hash-pin.

Expected net-new S4 events after dedup + scope: roughly **50-70** (of 106 candidates), heavily
weighted to the under-collected 2013-2020 era.
