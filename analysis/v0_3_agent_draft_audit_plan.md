# v0.3 agent_draft audit execution plan

> Plan generated 2026-05-20 after Session 2 evidence_repair_plan completion
> (commit `6a741c3`). Captures the remaining 156 `origin: agent_draft` /
> `internal_status: candidate` events that need full v0.3 primary-source
> verification before they can join the verified corpus.

## Starting state (2026-05-20, post-commit `6a741c3`)

- **262 events total** in the corpus
- **105 verified** (`primary_source_verified=1` semantics; queue `resolved`):
  - 83 events with `internal_status=verified` and queue `resolved`
  - 1 event (`sec-v-uniswap-wells-notice-2024`) `internal_status=retracted` and queue `resolved`
  - 22 events with `internal_status=verified` but queue still `needs_recheck` (Session 1 machine-triage residual)
- **156 candidate** events with `internal_status=candidate` and queue `needs_recheck` — **this plan's scope**
- **1 retracted** event (the Wells-notice case noted above)

Out of the 179 `needs_recheck` queue rows:
- 156 are the agent_draft set in scope here
- 23 are Session 1 / 2 NO decisions that have already been remediated
  through commits up to `6a741c3` (queue status not refreshed post-repair —
  cosmetic, not analytic)

## What "agent_draft" means

Each of the 156 candidate event YAMLs was authored by an LLM agent during
the Wave 2 expansion (2026-04 to 2026-05-16) and shares this signature:

- `status: draft` + `origin: agent_draft` + `primary_source_verified: false`
- DRYRUN note in `analysis_notes` acknowledging "authored by LLM agent
  without personally verifying Wayback/body_hash; origin=agent_draft and
  status=draft pending human review"
- Every citation has **wildcard wayback URLs** of the form
  `https://web.archive.org/web/<YYYY>/<live_url>` (e.g. `web/2021/...`)
  rather than a pinned `<timestamp>/...` memento
- Every citation carries `evidence_use: contextual_unarchived`
- **No `body_hash` / `body_path` anchors** — the
  `sources/http_captures/<event-id>/` directories are empty

This means the YAML structure exists (target/trigger/coverage/observation)
but the evidentiary chain is **not yet pinned to disk**. Promoting any
single event from `draft → admitted` requires re-running the audit
pipeline that the (b) repair cycle just demonstrated for 5 events.

## Per-event audit pipeline (gold standard, demonstrated in commit `6a741c3`)

The (b) commit established a 5-step pipeline that each of the 156 events
must traverse:

1. **CDX lookup** — `curl https://web.archive.org/cdx/search/cdx?url=<live_url>&output=json&limit=10`
   to find available Wayback mementos with non-trivial body size
2. **Raw Wayback fetch** — `curl https://web.archive.org/web/<timestamp>if_/<live_url>` (the `if_` suffix returns raw content, bypassing the Wayback HTML viewer wrapper that would otherwise wrap PDFs/binaries in a Wayback Machine title page)
3. **`capture_http_artifact.py --output-dir sources/http_captures/<event-id>/<source-class>/`** to save body + manifest + compute body_hash (HTML paths) or `curl -o file.pdf` + `shasum` for PDFs
4. **YAML patch** — replace wildcard wayback URL with pinned `web/<timestamp>` form, swap `evidence_use: contextual_unarchived` for `body_hash + body_path`, add grep-verified content note
5. **Human audit decision** via `scripts/review_queue.py --decision '{...}'`
   with explicit reason text, grep evidence, repair classification

**Per-event cost** (observed during Block D + (b)): 6–12 min of focused
human work + 1–3 min of network/computation time. Network latency on
Wayback fetches dominates wall-clock time.

## Triage stratification

The 156 events break down by classification axes the audit workflow already
uses for batching:

### By research stratum (matches Session 2 Block A–D structure)

| Stratum | Count | Notes |
| --- | ---: | --- |
| `S4_nation_state` | 55 | Largest; spans India/China/Korea/Japan/Turkey etc. regional clusters |
| `S5_corporate` | 54 | Issuer/exchange/DeFi unilateral policy; spans 1inch/Aave/Coinbase/etc. |
| `S3_doj_sec_cftc_fiod` | 22 | US federal enforcement + MLAT companions; smallest "all-US" batch |
| `S6_supranational` | 17 | EU / UN / G7 actions (MiCA, EU Russia sanctions) |
| `S1_ofac_sdn` | 8 | OFAC SDN designations not yet audited |

### By temporal tier

| Tier | Count | Notes |
| --- | ---: | --- |
| `comparable_main_2017_present` | 118 | Main analytic corpus; ≥1 captured peer per cluster usually exists |
| `historical_baseline_2013_2016` | 20 | Pre-OFAC-crypto-SDN era; Wayback coverage thinner |
| `discovery_only_2008_2012` | 18 | Pre-stablecoin / pre-Tornado era; many URLs likely 404 or rebranded |

### Recommended execution batching

- **Batch C-1 (S1 OFAC SDN, 8 events)** — smallest stratum; follows the
  cryptex/tornado-cash gold-standard pattern (OFAC RA URL → CDX → Wayback
  fetch). Estimated 1–2 hours; ideal warm-up for the first (c) session.
- **Batch C-2 (S3 federal_enforcement, 22 events)** — same recapture
  pattern as the (b) repair cycle (Akamai-DOJ → Wayback); risk: ~5 events
  will hit the hydra-doj-style "no Wayback memento" wall and need
  per-event URL research. Estimated 3–5 hours.
- **Batch C-3 (S6 supranational, 17 events)** — EU Council / Parliament
  / UN press releases; risk: machine-translated French/German sources may
  need WebFetch + alternative-language anchors. Estimated 2–4 hours.
- **Batch C-4a (S4 nation_state — regional, 55 events split by jurisdiction)**
  — likely 8–12 sub-batches by country (India, China, Korea, Japan,
  Turkey, Russia non-OFAC, etc.). Each country sub-batch ≈ 30–90 min.
  Estimated 10–15 hours total.
- **Batch C-4b (S5 corporate — by actor class, 54 events)** — split
  between DeFi-protocol (1inch, Aave, Uniswap, Curve, etc.) and centralized
  (Coinbase, Kraken, Binance non-enforcement). Each sub-batch ≈ 1–2 hours.
  Estimated 8–12 hours total.

### Recommended cross-cutting filter (apply to ANY batch)

Group each batch by **expected Wayback survival rate**:

- **Group A: Major US/EU government press release** — high Wayback CDX hit
  rate (~95%). Process via standard pipeline.
- **Group B: Corporate blog / DeFi protocol announcement** — medium hit
  rate (~70%); URL changes via CDN migrations common. Often need root-URL
  search on Wayback.
- **Group C: Non-English national regulator** — low hit rate (~40%);
  often need archive.today fallback or in-archive PDFs.
- **Group D: Smart-contract / GitHub / on-chain action** — high hit rate
  (~90%) but different repair class (git permalink + tx_hash anchors,
  not Wayback HTML).

## Known evidence-repair carry-overs from (b)

The (b) commit (`6a741c3`) closed 4 of 5 Block D NO events. The remaining
items expand the (c) worklist:

1. **`hydra-doj-2022`** — CDX returns 0 mementos for both `archives/opa/`
   and pre-archives URL forms; needs **URL research** (was the original
   DOJ release at a different USAO district? Press release archive
   different format?). Treasury jy0701 has Wayback mementos for the
   companion Garantex OFAC release but the DOJ-side Hydra takedown press
   release URL needs separate investigation.
2. **bitzlato / binance-4framework / ripple-fincen DOJ secondary swaps**
   — these 3 events are already verified via primary substitution sources
   (FinCEN / Treasury / FinCEN respectively), so the DOJ-side Akamai stubs
   are supplementary. Lower-priority enrichment.
3. **Codebook L4-vs-offramp_cex methodological clarification** — Beaxy
   (sec-beaxy-platform-shutdown-2023, qid=196) double-counted L4 +
   offramp_cex from a single SEC settlement paragraph; the SEC trilogy
   (sec-v-binance / sec-v-bittrex / sec-v-coinbase) explicitly consolidated
   to offramp_cex only. Needs a written rule in `schema/codebook.md` to
   resolve future ambiguity. Decision needed: when does a trading-platform
   shutdown warrant separate L4 + offramp_cex rows vs consolidated
   single-layer?

## Plan-level open questions for the maintainer

1. **Audit cadence**: Should (c) be one continuous push (estimated 25–40
   hours over 3–5 sessions), or paced (e.g., 1 batch per week alongside
   ongoing collection)?
2. **Bypass option for clearly-Wayback-blocked URLs**: For Group C
   (non-English national regulators with thin Wayback coverage), do we
   accept `archive.today` snapshots as primary_legal substitute, or do
   we require `body_hash` of the live URL with `evidence_use: contextual_unarchived`?
3. **Audit decision threshold**: Should re-extracted agent_draft events
   default to `empirical_case` admission_tier (current Wave 2 setting) or
   should I re-evaluate per-event (some may turn out to be null_case once
   the evidence chain is examined)?

## How to start (c) Batch C-1 (suggested next session)

```bash
# 1. List the 8 S1 OFAC SDN candidate events
sqlite3 .local/ingestion_v03/ingestion.sqlite "
  SELECT event_id FROM events
  WHERE internal_status='candidate'
    AND json_extract(payload_json, '\$.yaml_event.research_stratum')='S1_ofac_sdn'
  ORDER BY event_id;
"

# 2. For each event_id, run the per-event audit pipeline above.
#    Use commit 6a741c3 as the reference for body_path conventions
#    and review_queue.py decision JSON shape.

# 3. After ~8 events, commit + update this plan with executed counts.
```

## Linkages

- Per-event audit pipeline reference: commit [`6a741c3`](https://github.com/chnyangs/censorship-event-database/commit/6a741c3)
  — 5 NO→YES/repair examples
- Session 1 + 2 cumulative audit_log: `analysis/audit_log_session_1.jsonl`
  (305 rows through 2026-05-20)
- Schema reference: [`schema/codebook.md`](../schema/codebook.md) (v1.0.1
  after Codebook 1.0.1 self-correction commit `8fbc428`)
- Controlled vocab: [`schema/controlled_vocab.yaml`](../schema/controlled_vocab.yaml)
- v0.3 ingestion CLI: [`scripts/ingestion_v03.py`](../scripts/ingestion_v03.py)
  — generates the plan/worklist/report artifacts in `analysis/review_queue/`
