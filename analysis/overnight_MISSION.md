# OVERNIGHT CENSUS MISSION — operating manual for the autonomous tick

**Authorization.** User Yang Xiangwen, 2026-05-30 ~23:30 Melbourne, explicitly authorized
an UNATTENDED autonomous run until **07:00 Melbourne (AEST) 2026-05-31**: execute every
decision per your own best recommendation (do NOT wait for input), log decisions to the
notes file, user reviews in the morning. This overrides the standing per-item YES/NO rule
**for this overnight window only**.

**Scope is bounded + reversible:** local git commits only, **NEVER `git push`**, never
contact external/outward-facing services beyond read-only WebSearch + Wayback captures.
Everything is reviewable via git history + the notes file.

## DEADLINE — check FIRST every tick
Run: `TZ="Australia/Melbourne" date "+%H%M"`. If it is **≥ 0700** (i.e. HHMM ≥ 0700) on
2026-05-31, the run is OVER:
1. Append a FINAL SUMMARY to `analysis/overnight_collection_notes_2026_05_31.md`
   (totals: registry rows added, events authored, decisions made, what's queued for review).
2. `CronList` → `CronDelete` the overnight cron job (id in progress.json `cron_id`).
3. STOP. Do no more collection.

If before 07:00 Melbourne → proceed with ONE batch (below), then end the tick.

## MISSION
Build a **comprehensive census of crypto-stack censorship cases since 2007** (Hybrid model,
user-approved 2026-05-30): true census of the enumerable strata (S1/S2/S3/S4/S6) +
saturation-bounded S5 corporate. OFAC unit = one **designation-action** (not per address).
Six-layer cascade: l0_network, l1_consensus, l3_rpc, l4_frontend, asset_onchain, offramp_cex.

Current corpus: 262 events (254 admitted / 1 draft / 7 rejected) — see
`analysis/corpus_inventory_2026_05_30.tsv`. Heavy recency bias (54% in 2021-2023); the
**2007-2016 era and S2_ofac_removal are most under-collected**.

## PRIORITY ORDER (advance through this; progress.json tracks the pointer)
1. **2007-2016 back-fill** (proto-crypto e-gold family / Liberty Reserve / early bans /
   exchange collapses / NYDFS BitLicense exits / banking de-risking) — most under-collected,
   the "since 2007" claim's foundation.
2. **S2_ofac_removal** (only 1 in corpus — enumerate all OFAC crypto delistings/general licenses).
3. **S1 OFAC SDN** census (2018-2025 designation-actions), **S3** (DOJ/SEC/CFTC/FinCEN),
   **S4** (nation-state, per-country full timelines), **S6** (FATF/EU/G7/BIS/IOSCO/FSB).
4. **S5 corporate** saturation (exchange delistings/exits/freezes, DeFi/infra blocks).

If `analysis/census_gap_list.md` exists (written when the gap-discovery workflow finishes),
PREFER its prioritized candidates as the work-list.

## PER-TICK PROCEDURE (one batch ≈ 10-20 min of work)
**TIER 1 — extend the gap registry (do this every tick, it is the core deliverable).**
Append verified rows to `analysis/census_gap_registry.tsv` (create with header if absent:
`id\tdate\tactor\tjurisdiction\tstratum\tlayer\tone_line\tsource_url_1\tsource_url_2\tconfidence\tin_corpus`).
For the current focus: WebSearch the universe → pick 5-12 real cases NOT already in the
corpus (diff vs corpus_inventory ids) → for each, find **≥1 REAL archivable source URL**
(verify it exists; prefer ones likely in the Wayback Machine) → append a row. **NEVER
fabricate a URL or a case.** If unsure a case is real, omit it. Mark `in_corpus=false`.

**TIER 2 — author full events for the clearest, best-sourced candidates (opportunistic, 1-3 per tick).**
Only for cases where you have ≥1 real, capturable source. Method:
1. Pick the most structurally-similar existing **admitted** event in the same stratum as a
   TEMPLATE (templates: S1=`zservers-ofac-2025`, S3=`tornado-cash-storm-conviction-2025`,
   S4=`hongkong-hkma-stablecoins-ordinance-2025`, S5=`tether-tron-philippines-pdea-freeze-2024`,
   S6=`mica-l2-esma-eba-rts-2024`). Read it, copy its YAML structure, adapt content.
2. Capture real sources: `python3 scripts/capture_http_artifact.py --output-dir
   sources/http_captures/<id>/primary --user-agent "Mozilla/5.0 (Windows NT 10.0; Win64; x64)
   AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
   "https://web.archive.org/web/<YYYYMMDD000000>/<url>"` (date-prefix auto-resolves to closest
   memento; `<ts>id_/` for PDFs). body_hash = `sha256:<sha256 of the saved file>`, body_path =
   repo-relative path, evidence_use: replayable.
3. Source-type taxonomy + admission floor: 1 `primary_*` OR 2 independent `semi_primary_wayback`/
   `semi_primary_measurement`. `observed_change`+`direct` needs a `primary_*` source (else
   `plausible`). **`asset_onchain` observed_change/observed_no_change REQUIRES a `primary_onchain`
   tx_hash — if the mechanism is off-chain or no tx is pinnable, carry the effect at another
   layer (offramp_cex/l4_frontend) and set asset_onchain not_applicable, OR keep the event
   `draft`** (codebook §1.6).
4. Header for a promotable event: `status: admitted`, `origin: human_reviewed`, `version: "0.2"`,
   `last_verified: 2026-05-31`. If evidence is thin, leave `status: draft` (honest).
5. Forbidden release markers to avoid/scrub: `placeholder`, `PLACEHOLDER`, `before admission`
   (`DRYRUN` is allowed).
6. GATE: `python3 scripts/validate.py events/<id>.yaml` must print `[OK]` before committing.
   If you cannot get [OK] in a few iterations, leave it `draft` or drop it and note why.
7. Append an audit_log row to `analysis/audit_log_session_1.jsonl` (last id was 464; increment).

**COMMIT + LOG (end of every tick):**
- `git add -A && git commit` with a message like `Overnight census tick N — <focus>: +R registry rows, +E events`.
  Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>. **NEVER push.**
- Append to `analysis/overnight_collection_notes_2026_05_31.md`: tick number, focus, what you
  added, every judgment call you made (and why), anything that needs human review, anything
  you SKIPPED and why (e.g. unverifiable source).
- Update `analysis/overnight_progress.json` (advance focus pointer, bump counters, set last_fire).
- Run the full `validate.py` sweep occasionally (every few ticks) to confirm the corpus is clean.

## HARD RULES
- **NEVER fabricate** a source URL, a date, a tx_hash, or a case. Verify before recording.
- **NEVER `git push`.** Local commits only.
- Quality > quantity. A small batch of real, sourced, valid entries beats a large fabricated one.
- If rate-limited mid-tick, the commit may be partial — that's fine; the next tick resumes.
- If anything feels destructive or outward-facing, STOP and log it for human review instead.
- Keep each tick BOUNDED (don't run forever in one tick; one batch then end).
