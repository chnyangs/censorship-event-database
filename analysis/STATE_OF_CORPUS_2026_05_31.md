# 📍 State of the corpus — 2026-05-31 (session close)

**Authoritative current snapshot.** Supersedes `MORNING_REVIEW_2026_05_31.md` (which is now stale at 259).
Detailed tick-by-tick log: `analysis/overnight_collection_notes_2026_05_31.md`.

## Headline
- **385 events**: **368 admitted** / 10 draft / 7 rejected.
- **Integrity**: `scripts/validate.py` passes **385 / 385 [OK]**. All changes are **local commits, never pushed**.
- **This session continuation delivered +107 admitted** (corpus 261 → 368), plus codebook **4.0.0** (`evidence_tier`).

## Admitted composition (368)
| dimension | breakdown |
|---|---|
| **research_stratum** | S4_nation_state 110 · S5_corporate 97 · S3_doj_sec_cftc_fiod 78 · S1_ofac_sdn 52 · S6_supranational 30 · S2_ofac_removal 1 |
| **temporal_tier** | comparable_main_2017_present 308 · historical_baseline_2013_2016 40 · discovery_only_2007_2012 20 |
| **evidence_tier** | admission_grade 334 · **attested_secondary 34** (lower-tier, filterable — see codebook §10) |
| **admission_tier** | empirical_case 267 · null_case 96 · anchor_case 5 |
| **empirical_shape** | comparison 270 · null_event 96 · cascade 2 |

**Reading the table:** the census is dominated by single/low-layer `comparison` and `null` events (expected — most
censorship actions are observed at 1–2 layers; OFAC designations are `null_case` denominators). The **34
`attested_secondary`** rows are the well-documented single-source national bans + corporate restrictions admitted
below the strict source floor — they are explicitly tagged so any IRR / κ / headline-census computation can
exclude or down-weight them with `evidence_tier == attested_secondary`.

## What this session changed (261 → 368)
1. **Waves 1–3 fully processed** (S1/S3/S4/S5/S6 bulk authoring → adversarial verify → admit), corpus → 322.
2. **Task 1 — VERIFY-FLAG refinement** (+9): 5 OFAC null_cases + 4 non-OFAC; softened SDN-entry/penalty
   over-claims to match captured sources; 2 held with corrected flags. → 331.
3. **Task 2 — source-strengthening** (+37): +3 via official-PDF capture (philippines-bsp / argentina-bcra /
   ecuador-COMF, all Wayback-archived); +34 via the new **`evidence_tier=attested_secondary`** lower tier
   (25 clean + 9 flagged national bans). → 368.
4. **Codebook 4.0.0** — added `evidence_tier` (orthogonal source-strength grade) + §10 + validator support;
   regression 385/385.

## Method invariants proven this session (keep using)
- **Dry-run admission gating**: simulate draft→admitted in a temp file, run validate, admit ONLY if it passes;
  auto-revert on failure. No broken event is ever committed.
- **Independent source-rendering tiebreak**: the adversarial verifier OVER-flags (binance-dex, sec-tradestation,
  uae-sca all checked out fully); render+grep the pinned HTML/PDF to confirm load-bearing claims before trusting
  a FIX label — but it also catches REAL over-claims (sec-abra $1.65M), so every specific is grep-verified.
- **Capture yield rule**: only official PDFs / static pages on standard URLs capture cleanly; JS-gated exchange
  pages (Binance) return empty bodies and bot-protected gov sites reset — don't rely on them.

## Held drafts (10) — all honest, documented holds (NOT source-count)
- **6 need a `primary_onchain` tx_hash** (§1.6 binds; the lower tier does NOT apply): circle-usdc-hack,
  circle-usdc-sealed, ren-protocol (the §1.6 terminal-draft precedent — off-chain mechanism), t3,
  tether-iran-fury, tether-okx-doj.
- **4 semantic holds**: iraq-cbi (§9 warning-vs-ban ruling pending), goldage-2006 (pre-2007 boundary),
  task-force-rusich (real crypto designation but captured jy0954 has no crypto nexus — needs a crypto source),
  bitfinex-us-exit-2017 (captured page is a JS shell — needs a real capture).

→ Remaining work is tracked in **`analysis/NEXT_STEPS.md`**.
