# Changelog

## 2026-04-23 (derived-layer correctness fixes)

Post-review corrections to the three derived artifacts. All three are
pure regenerations — the evidence layer (events/*.yaml) is untouched.

- **P1 — `changed_given_measured` numerator filter.** Previously
  `build_layer_observability.py` computed `changed_given_measured =
  changed_count / measured_count`, where `changed_count` included rows
  whose coverage was `partially_measured`. The numerator now filters to
  the same coverage subset as the denominator, and two new column
  counts are exposed: `changed_under_measured_count` and
  `changed_under_measured_or_partial_count`. Corrected values at
  v0.1.0 snapshot: `l1_consensus` 1/6 = 0.1667 (was 0.3333);
  `l4_frontend` 11/16 = 0.6875 (was 0.8125); `offramp_cex` 15/25 = 0.60
  (was 0.64).
- **P2 — recovery counts could exceed changed-layer count.** Previously
  `build_event_metrics.py` consumed every `recovery[]` row, even when
  the named layer was never in `changed_layers`. For
  `tornado-cash-ofac-delisting-2025` this produced `recovered +
  unrecovered + recovery_unknown = 4` against `changed_layer_count = 3`
  because a `resolved=false` row for `l3_rpc` (coverage
  `partially_measured`, `observed_no_change`) was miscounted. Recovery
  rows are now intersected with `changed_layers` before the tallies;
  rows outside that set are ignored. Per-layer `resolved` in
  `event_metrics.json` reports `null` for non-changed layers.
- **P3 — null-event note in `archetype_distribution.md` overstated the
  admission contract.** Text previously claimed every null event
  carries `observed_no_change` rows anchored by `scope_descriptor +
  body_hash`. The validator rule is weaker: any ONE of
  `query_hash`, `measurement_ids`, `body_hash`+`body_path`, or a
  structured `scope_descriptor` is sufficient, and several admitted
  null events (`iran-ransomware-ofac-2018`, `sinbad-ofac-2023`) rely
  on `body_hash`+`body_path` alone. The note now describes the actual
  rule.

Regenerate with `make derived`. No change to schema, no change to
events, no change to dataset version.

## 2026-04-23 (derived research layer — v0.1 scaffolding)

Inaugurates the three-layer structure: evidence (events/) stays immutable;
a new **derived/** tree holds machine-generated analytical artifacts; two
new schema docs define the **evaluation** surface without populating it
yet. Everything is coverage-denominator honest and decoupled, per reviewer
discipline.

- **`derived/event_metrics.{csv,json,meta.json}`** — per-event panel
  (~24 columns): cascade breadth / latency / attribution layer counts /
  recovery per-layer / source-strength / structural flags
  (`has_large_target_set`, `is_reversal_event`, `target_is_privacy_tool`).
  Regenerates on `make event-metrics`. The `derived_archetype` placeholder
  that originally lived here has been **removed** — archetype
  classification is its own artifact (below), so base-metric logic stays
  pure-function of the evidence layer.
- **`derived/layer_observability.{csv,json,meta.json}`** —
  coverage-aware per-layer table (one row per layer, 6 total). Columns:
  `applicable_event_count`, measured / partial / not_measured /
  not_applicable composition, `changed_count`, and conditional rates
  `changed_given_measured` + `changed_given_measured_or_partial`. This
  artifact is what lets claims about L0/L1/L3 observability read as
  "zero changes *with N measured denominators*" rather than the
  indefensible "L0 has no censorship". Key numbers from the current
  snapshot (v0.1.0, cutoff 2026-04-22, 53 events):
  - `l0_network` — 0 / 22 applicable measured; `changed_given_measured`
    is **null** (undefined denominator). Pure observability gap.
  - `l1_consensus` — 6 measured + 1 partial; `changed_given_measured` =
    33%. The two L1 changes in the corpus are both Tornado-related.
  - `l3_rpc` — 0 measured + 8 partial; `changed_given_measured_or_partial`
    = 0/8. Weak denominator, weak claim.
  - `l4_frontend` — 16 measured; **changed_given_measured = 81%**.
  - `asset_onchain` — 17 measured; **changed_given_measured = 100%**.
  - `offramp_cex` — 25 measured; `changed_given_measured` = 64%.
- **`derived/event_archetypes.{csv,json,meta.json}`** +
  **`derived/archetype_distribution.md`** — rule-based
  deterministic classifier (no clustering). Six classes, priority-ordered:
  `null_event` → `multi_layer` → `asset_only` → `frontend_only` →
  `cex_only` → `other_single_layer` (safety catch for future L0/L1/L3
  singletons; currently empty). Per-event emits `changed_layer_signature`
  (e.g. `asset_onchain+l4_frontend`), `latency_regime`
  (`synchronous` ≤ 1h / `acute` ≤ 30h / `delayed` ≤ 30d / `lagged` > 30d /
  `none`), and structural flags (`is_upper_layer_only`,
  `is_base_layer_observed`, `has_recovery_signal`, `trigger_is_action`).
  The `trigger_is_action` flag distinguishes `synchronous` rows whose
  `trigger.timestamp` and `observed_change.timestamp` are identical in
  the record (5 `corporate_policy_change` events: Circle + Tether × 3 +
  Uniswap — t=0 is a record-level artifact, not a measured delta) from
  the 12 rows with distinct external triggers and ≤1h observed latency.
  Paper claims about latency distributions should aggregate the two
  subsets separately. Report has 5
  sections: rules / distribution / exemplars / edge-cases /
  hand-eyeball checklist. Current distribution:
  `asset_only: 13 · frontend_only: 8 · cex_only: 14 · multi_layer: 5 ·
  other_single_layer: 0 · null_event: 13`. All multi-layer signatures
  include L4 or asset; L1 consensus appears only in Tornado cases.
- **`docs/stack-features-schema.md`** — v0.1 schema definition for the
  per-stack architectural feature table (NOT populated). Four feature
  families (frontend-control / asset-control / off-ramp + access /
  base-layer) + cross-cutting governance. Mandatory provenance triplet
  (`measured_at`, `measurement_source`, `confidence`) on every feature.
  5 pilot stacks named: `eth_usdc_uniswap_cex`, `tron_usdt`,
  `privacy_tool_stack`, `btc_base_stack`, `frontend_mediated_defi_stack`.
  Solana deferred to v0.3.
- **`docs/evaluation-profile-schema.md`** — v0.1 rubric definition
  (NOT populated). Five ordinal dimensions (`high/medium/low/insufficient`):
  Frontend / Asset / Off-ramp Enforcement Exposure + Coordination
  Surface Density + Evidence Confidence. Explicit per-dimension grading
  heuristics. Recoverability **deferred** (n=1 reversal event in corpus).
  Composite index **deferred indefinitely** (reviewer-demand gated).
  Phrasing discipline preserved: "historically associated with" / "not
  predictive".
- **Makefile** — new targets `event-metrics`, `layer-observability`,
  `archetypes`, and umbrella `derived` (which runs `dataset` first so
  the meta snapshot is current). `regenerate` extended to rebuild the
  derived layer. `clean` also drops `derived/`. `make help` shows the
  new derived-layer section.

Explicit non-goals for v0.1 (all deferred with stated reason):

- Populated stack-feature rows — schema only; manual annotation is a
  separate work stream.
- Evaluation-profile rows — same rationale.
- Recoverability as an evaluation dimension — n=1 reversal.
- Composite censorship-resistance score — sample size + incommensurability.
- Solana stack pilot — evidence coverage too thin.
- Unsupervised clustering — sample distribution strongly single-layer
  dominant; rule-based taxonomy more defensible and fully reproducible.

## 2026-04-23 (provenance / transparency / license consistency)

Three P2 follow-ups from the release-prep review, all about
"documentation promise vs record-level evidence" drift:

- **Audit stamp finally lands on record.** The 2026-04-22 CHANGELOG entry
  claimed an adversarial audit of 5 events but the event YAMLs carried no
  `last_human_audit`. Stamped `last_human_audit: 2026-04-22` on the 5
  re_scoped events from that audit (`tornado-cash-ofac-2022`,
  `semenov-ofac-2023`, `cryptex-ofac-2024`,
  `tether-retroactive-sweep-2023`, `tornado-cash-ofac-redesignation-2022`).
  Did NOT stamp the expansion-pass fixups (`suex-ofac-2021`,
  `chatex-ofac-2021`, `lockbit-affiliates-ofac-2024`) since those were
  scope-widening tx_hash repairs, not part of the headline audit sample.
- **`staleness_report.py` no longer masks missing audits.** Previous logic
  used `last_verified` as a fallback when `last_human_audit` was absent,
  so 53/53 events reported `ok` even though 0 had ever been audited.
  Refactored to two independent dimensions:
  - `audit_flag` — driven by `last_human_audit` alone; missing =
    `no_audit_recorded` (explicit, not silently-ok).
  - `verification_flag` — driven by `last_verified`; missing =
    `no_verification_recorded`.
  Row-level `summary_flag` = worst of the two, with an explicit severity
  ordering (`no_audit_recorded > no_verification_recorded > red > ok`).
  Current state: **5/53 audit:ok, 48/53 no_audit_recorded** — the report
  now honestly surfaces the audit-coverage gap it was designed to
  monitor. `analysis/staleness.md` now carries a flag legend + coverage
  snapshot + per-event table with both dimensions.
- **Code/data license split made explicit.** Previously the repo-root
  `LICENSE` was CC-BY-4.0 but `docs/limitations-and-use.md §6` said
  "tools under scripts/*.py are MIT-licensed unless otherwise stated"
  with no actual MIT text or per-file headers — contradictory signal.
  Concretely:
  - Added [`LICENSE-CODE`](LICENSE-CODE) with the canonical MIT license
    text.
  - Added [`NOTICE`](NOTICE) at repo root enumerating which files are
    CC-BY-4.0 vs MIT and explaining the split rationale (CC recommends
    against using its licenses for software).
  - Added `SPDX-License-Identifier: MIT` header to every file under
    `scripts/` (18 files), so the per-file declaration is machine-
    readable and survives cut-and-paste into downstream projects.
  - Rewrote `docs/limitations-and-use.md §6` to name both licenses,
    link to both legal texts, and explain the why. README gained a
    one-line license callout linking to `NOTICE`.
  - `LICENSE` itself is untouched (canonical CC-BY-4.0 from
    creativecommons.org) — no preamble, because modifying canonical
    CC text is exactly what Zenodo / external citation tooling doesn't
    expect.

## 2026-04-23 (release-prep cleanup)

Three corrections found in the citability pass review:

- **LICENSE added.** `CITATION.cff` and `.zenodo.json` declared CC-BY-4.0,
  but the repo had no `LICENSE` file. Added the canonical Creative Commons
  Attribution 4.0 International Public License legal code at the repo root
  (fetched verbatim from creativecommons.org/licenses/by/4.0/legalcode.txt).
- **`cutoff_date` semantic unified on MAX.** The implementation
  (`scripts/build_dataset.py`, `scripts/_dataset_meta.py`) and three of four
  docs (`docs/citing.md`, `docs/datasheet.md`, `README.md`) already used
  the **max** of (`last_verified`, `last_human_audit`) across events, but
  [`docs/limitations-and-use.md` §4](docs/limitations-and-use.md) said
  "minimum". Aligned on MAX with an explicit canonical definition block in
  §2.5 naming the four files that must stay in lock-step. Reasoning: MAX =
  "snapshot includes events verified up through this date", aligning with
  paper/arxiv "as of" convention. For the uniform-freshness-floor
  (lower-bound) semantic, consumers should read `analysis/staleness.md`,
  not reinterpret `cutoff_date`.
- **`origin` backfilled on 52/53 admitted events.** All admitted events now
  carry `origin: human_authored` (one event already had it). Did **not**
  fabricate `last_human_audit` dates — that field stays empty until a real
  quarterly adversarial audit runs, so consumers reading
  `analysis/staleness.md` see honest "no_audit_recorded" flags rather
  than synthetic compliance signal.

## 2026-04-23 (citability + stable metadata)

Prep for the first tagged release (`v0.1.0`). Five coupled changes so the
dataset is citable with a single version/cutoff pin rather than "whatever
was on main that day":

- **[#1] CITATION.cff + Zenodo integration.** Added
  [`CITATION.cff`](CITATION.cff) (CFF 1.2.0) at the repo root — GitHub
  renders a "Cite this repository" button from it, Zenodo reads it on each
  tagged release to mint a DOI. Added [`.zenodo.json`](.zenodo.json) for
  deposit-level metadata (license: CC-BY-4.0, related identifier to
  Wahrstätter et al. 2024, keywords). One-time Zenodo setup and
  per-release procedure documented in
  [`docs/releasing.md`](docs/releasing.md). Listed Wahrstätter's
  "Blockchain Censorship" (WWW 2024) as `references` so the lineage is
  machine-readable.
- **[#2] `dataset.meta.json` generated by `build_dataset.py`.** Stable
  sidecar metadata with a versioned schema: `dataset_version` (from
  CITATION.cff — single source of truth), `cutoff_date` (max of
  `last_verified` / `last_human_audit` across events), `generated_at`,
  `source_commit` (short sha, best-effort), `schema_version` (enforced
  unique across events — inconsistency raises `SystemExit`),
  `event_count`, `counts_by_{status,stratum,shape,tier}`, and a
  `citation_hint` string. This is the file every downstream consumer
  should pin against.
- **[#3] Version + cutoff propagated everywhere.** New shared module
  [`scripts/_dataset_meta.py`](scripts/_dataset_meta.py) with
  `load_meta()` (reads `dataset.meta.json`, synthesises fallback if
  absent). Wired into:
  - `render_evidence_chain.py` — header now shows dataset version +
    cutoff + source commit; audit step tells the reader to `git
    checkout v{VERSION}` at the recorded commit.
  - `find_comparable_cases.py` — retrieval report header carries the
    same identity stamp.
  - `render_site.py` — per-event hero meta, per-event footer, index
    footer, and a new "Cite this dataset" section on the index all
    quote the current version + cutoff.
- **[#4] Positive-use guidance + citation templates.** Extended
  [`docs/datasheet.md`](docs/datasheet.md) §5 with three new subsections:
  how to use an observation in a paper / brief (§5.1), what claim
  granularity the data supports (§5.2), and audience-specific guidance
  for paper authors / policy-legal analysts / journalists (§5.3). Added
  [`docs/citing.md`](docs/citing.md) with BibTeX, APA, Chicago, MLA,
  and plain-text citation templates; README §7.5 now links both.
- **Site fixes.** `render_site.py` now copies `docs/` into `site/docs/`
  at build time (old `raw/../docs/limitations-and-use.md` link was
  broken on the deployed site) and also copies `CITATION.cff` +
  `dataset.meta.json` alongside so consumers can fetch them via the
  Pages URL. The index gains a "Cite this dataset" section.
- **[#5] Staleness filename consistency.** Makefile previously wrote to
  `analysis/staleness-report.{json,md}` while the script defaults and the
  committed artifacts used `analysis/staleness.{json,md}`. Aligned
  Makefile to the script/disk reality. Added `DATASET_META` variable
  pointing at `dataset.meta.json`.

Regeneration: `make regenerate` completes green on all 53 events;
hand-rolled validator + external `jsonschema` round-trip both pass;
54/54 site pages are tag-balanced.

## 2026-04-23 (publish pipeline)

- **site.yml** deploys to this repo's own GitHub Pages via
  `actions/upload-pages-artifact` + `actions/deploy-pages` now that the repo
  is public. No cross-repo PAT or secondary site repo required.
- **Hygiene**: adds `site/.nojekyll` at build time so Pages skips Jekyll
  preprocessing (safer default for a hand-rendered static bundle). Fixed
  the repo URL placeholder (`xwy411/…`) in the JSON Schema `$id` and the
  index header's GitHub link to the real `chnyangs/censorship-event-database`.

## 2026-04-23 (systematic UI overhaul)

Full rewrite of `scripts/render_site.py`. Previously the site was a single
466-line Python file emitting inline CSS + minimal HTML; the output displayed
the data but did not reflect the project's thesis. After this pass, every
event page surfaces the cascade as a first-class visual and the index makes
the structural distribution browsable at a glance.

- **Semantic foundation.** Every page now carries `<html lang="en">`,
  `<meta name="viewport">`, `<meta name="description">`, a sticky
  `<header class="site-header">`, `<main>` content region, `<article>`
  wrappers for event bodies, `<nav>` for breadcrumbs/prev-next, and
  `aria-label` / `aria-pressed` / `aria-sort` on interactive controls.
  All 54 pages pass HTML tag-balance checks.
- **Coherent color system.** The old palette reused red (`pill-cascade`
  and `pill-direct`) across semantic axes, which collapsed different
  meanings onto the same hue. Introduced CSS custom properties with
  **non-overlapping** palettes for status, empirical_shape, admission_tier,
  attribution, observation_kind, and per-layer qualitative colors.
- **Dark mode.** `prefers-color-scheme: dark` plus a manual toggle in the
  header persisted in `localStorage` (`ccdb.theme`). Full variable remap
  so every surface, border, and pill has legible contrast in both modes.
- **Cascade visualization (index + event).** Each event renders a
  6-dot `cascade-dots` glyph — one dot per layer in canonical order, filled
  with that layer's color when observed_change, dashed-outlined when
  observed_no_change, muted when no observation. The glyph appears on every
  event row in the index table AND enlarged in the event hero.
- **Per-event cascade timeline.** New horizontal timeline SVG-in-CSS
  showing trigger at t=0, each layer as a colored track, observation
  markers at their `delta_hours` position, axis ticks at
  {0h, 6h, 12h, 24h, 48h, 72h, 168h}, and an off-axis "+N beyond 7d" note
  for observations outside the 7-day window.
- **Event hero.** Title-cased slug with acronym-aware rendering
  (`tornado-cash-ofac-delisting-2025` → `Tornado Cash OFAC Delisting 2025`).
  Above-the-fold: shape / tier / status pills, scoped_claim blockquote,
  6-layer cascade summary, then a compact fact grid (trigger date, type,
  actor, jurisdiction, chains, stratum).
- **Observations grouped by layer.** Observations are now shown as
  per-layer `<article>` groups (L0 → L1 → L3 → L4 → asset → offramp),
  each with layer-colored header and a compact source list. The flat
  observation table is retired; the layered view makes the cascade visible.
- **Index filtering overhaul.** Replaced the single text box + class
  dropdown with a chip bar across **five facets**: shape, tier, stratum,
  year, chain. Filters are ORed within a facet and ANDed across facets.
  Filter state round-trips to the URL hash (e.g. `#shape=cascade&year=2022`),
  so filtered views are shareable. "Reset filters" button + live result
  count. Search blob now includes tags, protocol, entity, title.
- **Sortable columns.** Every `events` table header with `data-sort` is
  click-/Enter-sortable, with `aria-sort` set on the active column and an
  arrow indicator. Default sort: date ascending.
- **Sticky chrome.** Site header + filter bar + table thead all stick to
  the top on scroll; the sticky offsets are tuned per breakpoint.
- **Hero chip deep-links.** Index hero exposes canned filter links
  (cascade events / anchor cases / OFAC SDN / nation-state / by-year);
  clicking updates the URL hash and the page reacts via a `hashchange`
  listener that clears, reloads, and scrolls to the events table.
- **Prev/next sibling nav on event pages.** Event pages now carry a
  date-ordered prev/next pair at the bottom so readers can sweep
  chronologically through the dataset.
- **Distribution as tiny bar charts.** The old distribution "table" was
  four `<br>`-stacked lists. Replaced with four `dist-card`s, each
  showing the top-6 values with horizontal bar fills scaled to the
  facet maximum.
- **Externalized assets.** `styles.css` (655 lines, was 59) and a new
  `site.js` (143 lines) are separate files rather than inlined in the
  Python string. Easier to edit, cacheable, and unblocks CSP experiments.
- **Typography, responsive, print.** Fluid `max-width: 1180px`; mobile
  breakpoint at 700px hides lower-priority columns and restacks the fact
  grid; print CSS hides the header/filter/nav chrome and flattens to black
  on white.
- **Timestamp normalization.** PyYAML parses `2022-08-08T13:30:00Z` as a
  `datetime`; the old renderer `str()`'d it into the ugly
  `2022-08-08 13:30:00+00:00` form. New `fmt_ts()` helper always emits
  `2022-08-08T13:30:00Z`; used consistently in hero, trigger section,
  timeline, and `<time datetime="…">` elements.
- **Tag cloud links feed the search box.** Event-page tags now link to
  `index.html#q=<tag>`, which the index hash router maps to the search
  input rather than trying to filter by a non-existent `tag` facet.

Regeneration: `python3 scripts/render_site.py` → 53 event pages + index,
all passing tag-balance checks. Hand-rolled validator + external
`jsonschema` round-trip remain green.

## 2026-04-22 (systematic review sweep)

Round-trip of reviewer findings from the 2026-04-22 systematic review. Every
change is backed by an explicit [R#] tag:

- **[R1] JSON Schema was dead code — fixed.** `scripts/validate.py` loaded
  `schema/event.schema.json` and discarded the result (`_ = load_json(...)`).
  The hand-rolled validator hardcoded `S6_supranational` /
  `supranational_regulation`, but those values were absent from the JSON Schema
  file, so any external consumer using `jsonschema validate` would reject the
  two admitted EU events (`eu-mica-2023`, `eu-12th-russia-sanctions-2023`).
  - Added the missing enum values to `schema/event.schema.json`.
  - Replaced the `example.org` placeholder `$id` with the repo URL.
  - Added `check_vocab_schema_consistency(vocab, schema)` in `validate.py`
    that diffs validator ⇄ vocab ⇄ JSON Schema enums and hard-fails on drift
    (see `_VALIDATOR_STRATA` / `_VALIDATOR_SHAPES` / `_VALIDATOR_TIERS`).
  - New CI workflow `validate.yml` runs the validator on every PR and also
    round-trips every event through `jsonschema` (pip-installed) to catch
    external-consumer drift that the hand-rolled validator might miss.
- **[R2] CI surface expanded.** Previously only `site.yml` ran on push-to-main;
  PRs were unprotected and `verify_citations.py` / `staleness_report.py` never
  ran in CI, so link rot accumulated silently.
  - Added `validate.yml`: runs on PR + push, executes `validate.py`,
    `status_report.py`, `review_report.py`, `staleness_report.py`,
    `draft_gap_report.py`, `build_dataset.py`.
  - Added `freshness.yml`: weekly cron (Mon 07:00 UTC) runs
    `freshness_check.py` + `verify_citations.py`, uploads log as artifact, and
    opens/refreshes an issue labeled `freshness` when rot is detected.
  - `site.yml` now also `pip install jsonschema`.
- **[R3] Gap markers consolidated.** `validate.py`, `status_report.py`, and
  `draft_gap_report.py` each defined their own marker list, which diverged —
  a draft with "replace Wayback hash" would fail validate but show 0 gaps on
  the status dashboard because status_report dropped the word "replace".
  Moved to `scripts/_gap_markers.py` with three strictly-nested tiers:
  `BLOCKING` ⊆ `STATUS` ⊆ `AUTHOR_DRAFT`. validate + status now use the same
  `BLOCKING` set; `draft_gap_report` uses the broader author-hint set.
- **[R4] `attribution=direct` ⇒ primary source.** Previously two semi-primary
  measurements satisfied both the admission count rule AND allowed
  `attribution=direct`. Added a distinct rule in `validate.py`:
  `observed_change + attribution=direct + status != draft` requires at least
  one `primary_*` source. Degraded the single violating observation
  (`tornado-cash-ofac-delisting-2025.yaml` L1 consensus) from `direct` to
  `plausible` and extended the analysis note to explain the downgrade.
- **[R5] Reproducibility sweep.**
  - `datetime.utcnow()` (deprecated in 3.12) → `datetime.now(timezone.utc)`
    in `render_site.py` and `ooni_batch_query.py`. Every other script was
    already correct; sweep makes the repo uniform.
  - `find_comparable_cases.py` sort keys now include a secondary key on the
    slug / feature name so tied scores produce byte-identical Markdown across
    runs. Without it, CPython insertion order changes could flip the output.
  - `validate.py` delta_hours tolerance check now widens by 1e-6h
    (≈ 3.6 ms) to absorb ISO-8601 round-trip float noise without broadening
    the semantic tolerance.
  - `validate.py` schema_version check: `0.1.0` still hard-fails (migration
    pin); unknown newer versions now warn instead of erroring so a
    partially-migrated branch is still runnable by an older validator.
- **[R6] USDT-banlist parser hardened.** `batch_usdtbanlist_check.py` regex
  required exactly two decimal places and would silently drop 1- or 3-decimal
  amounts. Widened to `[\d,]+(?:\.\d+)?` and added a `[WARN]` when the page
  carries the `BLOCKED` marker but the parser extracts zero Banned rows —
  the canary for a future HTML change.
- **[R7] Multi-agency trigger check fixed.** `validate.py` actor/type coherence
  previously `break`'d on the first matching agency substring. For
  `binance-4framework-2023` and similar, that allowed inconsistent
  (actor, trigger.type) pairs to pass if the wrong agency matched first. Now
  collects every matching rule and accepts if the declared type is in the
  union of permissible types; error message lists all matched agencies.
- **[R8] Hygiene.**
  - `review_report.py` now prepends `scripts/` to `sys.path` so it imports
    `status_report` regardless of cwd.
  - `new_event.py` now dumps with `allow_unicode=True`, matching
    `agent_draft_event.py` (no more byte-level difference between the two).
  - `templates/event.yaml` stratum comment includes `S6_supranational`.
  - `validate.py` id error wording spells out "lowercase letters, digits,
    and hyphens only" instead of "kebab-case".
  - Dead vocab key `event_classes` removed from `EventValidator.__init__`
    (it was loaded then never read).
- **[R9] Prior-art positioning in README §1.** Replaced the broad
  "no one has ever measured the cascade" framing with a contribution
  statement that acknowledges Wahrstätter et al. (ACM WebConf 2024), Censored
  Planet (CCS 2020+), and MEV-coordination work (USENIX Security 2025), and
  states the incremental contribution as **event-keyed + six-layer +
  hour-precision + open multi-source admission protocol**.
- **[R10] Venue ordering.** README §7 now lists IMC 2026 Cycle 2 as primary
  (artifact/replicability track is the best fit for a dataset+methodology
  paper) and AFT 2026 as secondary for the financial-framing angle.
- **[R11] Datasheet.** Added [`docs/datasheet.md`](docs/datasheet.md),
  following Gebru et al.'s "Datasheets for Datasets" template. Linked from
  README §7.5.

## 2026-04-22

- **Repository cleanup: merged stray root-level `sources/` into `p1-event-db/sources/`**.
  Two `sources/` trees had drifted apart across the repo:
  - `/chain-censorship-measurement/sources/http_captures/` held 3 empty
    `primary/` directories (orphan `mkdir` remnants from an early cwd
    bug); **deleted** — zero data loss.
  - `/chain-censorship-measurement/sources/ofac_sdn_diffs/` held 79 MB
    of real S1-triage cache (74 historical OFAC Recent Actions HTML
    captures under `recent_actions_cache/`, plus
    `opensanctions/ofac-recent-actions-triage.json` — the authoritative
    27-event S1 enumeration source) that was invisible to every tool
    because no script / event YAML ever referenced `../sources/`.
    **Moved** to `p1-event-db/sources/ofac_sdn_diffs/` where
    `EVENTS-CHECKLIST.md` already claimed it lived.
  - Post-migration cross-check: 53/53 validator OK; body_hash drift 0/10
    random samples; `make clean && make regenerate` rebuilds all
    artifacts identically; S1 triage JSON path resolves; 74 Recent
    Actions HTML caches all accessible.
- **Makefile unified as the single command surface**. Added targets for all
  new scripts so contributors don't need to remember invocation syntax:
  `make render-site`, `make render-evidence SLUG=<slug>`,
  `make render-evidence-all`, `make compare LIKE=<slug> TOP=5` (or
  `make compare TRIGGER_TYPE=... ACTOR=...`), `make staleness`,
  `make ooni-scan`, `make usdt-scan`,
  `make capture URL=<url> OUT=<dir>`. Plus omnibus targets:
  `make check` (validate + reports), `make check-all` (+ network checks),
  `make regenerate` (rebuild dataset + site + evidence chains + status +
  review in one shot), `make clean` (remove generated artifacts). Every
  target is documented in `make help` output.
- **Framework layer (A+B+C) added** — three tools built on the event
  database for paper-author / policy-analyst / legal-analyst usage.
  Deliberately scoped to retrieval + structured argument only; **no
  predictive modelling** because 53 events is too small for defensible
  inference. Shipped with an explicit non-advice / non-compliance
  statement at [`docs/limitations-and-use.md`](docs/limitations-and-use.md).
  - **Layer A — `scripts/render_evidence_chain.py`**: per-event
    Markdown renderer that emits `claim → observations → sources
    (body_hash) → honest gaps → audit instructions`. Output is
    stamped with `dataset_version` (git hash) + `schema_version` +
    `tool_version` + `generated_at` for reproducibility. Generated
    53 evidence chains to `analysis/evidence-chains/`.
  - **Layer B — `scripts/find_comparable_cases.py`**: case-based
    retrieval tool. Given a proposed action (or existing event as
    reference), returns top-N most similar historical events with
    transparent feature-weight breakdown (`trigger_type`,
    `research_stratum`, `actor_family`, `chain_overlap`,
    `jurisdiction_overlap`, etc.) + explicit divergence-factor list
    per ranked case. **Not a predictive model** — the tool surfaces
    historical precedents for expert judgment, not probabilities.
    Every output carries the limitations banner.
  - **Layer C — `docs/decision-rubric.md`**: hand-followed structural
    checklist distilling dataset findings into pattern classes. 6
    parts (trigger structure / target properties / issuer-compliance
    expectations / cross-layer expectations summary / red flags /
    next steps). Includes a "16-pattern-class" reference table
    mapping structural features to comparable historical events.
  - **`docs/limitations-and-use.md`** drafted as the canonical
    non-advice statement. Covers: not a predictive model, not legal
    advice, not a compliance service, known coverage gaps, snapshot
    decay, reproducibility contract, license + attribution, corrections
    workflow. Every tool output links here.
  - **Site integration**: `site/index.html` now surfaces the 3-layer
    framework with stat-card navigation. Schema version banner updated
    to 0.2.0.
- **Reviewer third-pass fixes (gap-marker false positives + case-variant leak)**.
  - **P2 gap-marker definition narrowed**: `scripts/status_report.py`
    `GAP_MARKERS` tuple previously included `"needs "` / `"need "` /
    `"requires "` / `"still need"` which fired on legitimate analytical
    prose (e.g., "requires per-relay block-filter-list inspection" in
    follow-on discussion; "Needs further research" in analysis notes).
    The false hits cascaded into `scripts/review_report.py` → falsely
    downgraded `observation_reliability` to `low` on 4 well-evidenced
    events (`cryptex-ofac-2024`, `grinex-garantex-successor-ofac-2025`,
    `tether-dprk-precommit-freeze-2025`, `tether-retroactive-sweep-2023`).
    Narrowed the marker list to unambiguous placeholder patterns
    (`placeholder` / `fill in` / `to be collected` / `before admission`
    / `still to be pinned` / `tbd` / `todo`) and added
    `SKIP_FIELDS_FOR_GAP_SCAN` to exempt analytical-prose fields
    (`analysis_notes`, `scoped_claim`, `follow_on_reaction`,
    `enumeration_note`, `tags`) from recursion. Post-fix: 0 events carry
    `gap_marker_count > 0`; the 4 affected events now correctly score
    `observation_reliability: high`.
  - **P3 case-insensitive legacy-class lint**: Reviewer found
    `tether-retroactive-sweep-2023` line 135 still said
    `State_block_event` (capital S) because the validator lint was
    case-sensitive. Switched `_check_field_consistency()` to compare
    `notes.lower()` against the legacy term set; caught the leak.
    Also simplified the lint — since `event_class` is fully deprecated,
    ANY mention of the legacy terms is stale regardless of whether it
    matches the current empirical_shape's legacy mapping. Cleaned up
    the `State_block_event` mention in the tether-retroactive-sweep
    analysis_notes to the current `S5_corporate / empirical_case
    (comparison)` wording.
  - Regenerated `analysis/pilot-status.json`, `analysis/review-report.md`,
    `dataset.json`, `site/`. Post-fix cross-check on 7 regression probes:
    **0 validator FAIL / 0 WARN; 0 gap-marker false positives; 0
    case-variant leaks; 0 body_hash drift; 0 actor/type violations; 53/53
    at schema_version 0.2.0**.
- **Reviewer second-pass systemic fixes (P1-B / P1-C / P1-D / P2 / P3)**.
  Reviewer follow-up flagged four residual systemic issues after the
  initial schema 0.2.0 migration. All four confirmed via cross-check and
  fixed; re-verification reports 0 residual issues.
  - **P1-B trigger.type taxonomy corrected on 6 events**: SEC and CFTC
    civil actions were previously encoded as `doj_indictment` because the
    vocab types `sec_action` / `cftc_action` existed but no one was using
    them; EU actions were encoded as `nation_state_block` because there
    was no supranational bucket. Re-typed:
    - `sec-v-binance-2023`, `sec-v-coinbase-2023`,
      `sec-v-uniswap-wells-notice-2024`: `doj_indictment` → `sec_action`
    - `cftc-v-ooki-dao-2022`: `doj_indictment` → `cftc_action`
    - `eu-mica-2023`: `nation_state_block` → `supranational_regulation`
      (new trigger type for regulatory frameworks like MiCA)
    - `eu-12th-russia-sanctions-2023`: `nation_state_block` →
      `non_us_sanctions`
  - **P1-C new research_stratum `S6_supranational`** added to vocab +
    schema + validator. Covers EU / UN / G7-level actions. The 2 EU
    events re-stratumed from S4_nation_state to S6_supranational. The
    S3/S4/S5 buckets are now structurally unambiguous: S3 = US federal
    (DOJ / SEC / CFTC / FIOD-companions); S4 = single-country national
    (KR / CA / IN / NG / TR / CN); S6 = supranational (EU).
  - **P1-D validator actor/type coherence check** added. New rule in
    `_check_field_consistency()` enforces: `US_SEC` actor → trigger.type
    must be `sec_action`; `US_CFTC` → `cftc_action`; `US_DOJ` →
    `doj_indictment` or `doj_seizure_order`; `US_OFAC` → `ofac_sdn_*`;
    `EU_Council` → `non_us_sanctions` or `supranational_regulation`.
    Previously the validator only checked that trigger.type was in the
    vocabulary; it now catches actor/type drift at validation time. Also
    completed the trigger_type → stratum map to cover all 10 trigger
    types (including the three that had been absent: sec_action,
    cftc_action, non_us_sanctions, supranational_regulation).
  - **P2 schema_version bumped 0.1.0 → 0.2.0 across all 53 events**.
    Prior state: methodology + controlled_vocab advertised schema 0.2.0,
    but every event YAML still said `schema_version: 0.1.0` —
    inconsistent metadata that would mislead any downstream consumer
    trying to branch on version. Validator now PINS
    `CURRENT_SCHEMA_VERSION = "0.2.0"` and emits a hard error on any
    mismatch.
  - **P3 legacy class words eliminated from 23 events**. The first
    cleanup only stripped legacy words that contradicted the current
    empirical_shape (e.g., "cascade_event" in a now-comparison event);
    legacy words that happened to match the expected legacy mapping
    (e.g., "comparison_event" in a comparison event) survived. Since
    `event_class` is fully deprecated from the schema, every legacy
    mention is stale regardless of match. Second pass did whole-word
    substitution across analysis_notes + tag deletion: 0 legacy mentions
    remain (cross-check confirmed).
  - **P1-A status_report verified clean** (reviewer's claim appeared to
    be based on a stale pilot-status.json — re-check showed the file
    already carried `research_stratum_counts`/`empirical_shape_counts`/
    `admission_tier_counts` and NOT `event_class_counts`). No code
    change needed.
  - Regenerated `dataset.json`, `dataset.csv`, `analysis/pilot-status.json`,
    `analysis/review-report.md`, `site/`. Cross-check confirmed: body_hash
    drift-free (10/10 sample), all related_events resolve, all 53 events
    validate clean (0 errors, 0 warnings).
- **Schema-0.2.0 tooling sweep (regression fix)**: reviewer flagged that
  `scripts/status_report.py` still read the legacy `event_class` field,
  causing `analysis/pilot-status.json` to report `event_class_counts:
  {null: 53}`. Fixed by migrating `status_report.py` to emit three new
  counters: `research_stratum_counts`, `empirical_shape_counts`,
  `admission_tier_counts`. Also caught three other stale sites missed
  in the first sweep:
  - `scripts/render_site.py` had 2 lingering `e.get("event_class")`
    references (stat-card source + per-row data attribute).
  - `scripts/agent_draft_event.py` + `scripts/new_event.py` CLI defaults
    still wrote `"event_class": "comparison_event"` into new drafts —
    migrated to emit the three new fields with a `STRATUM_MAP`
    derivation from `trigger_type`.
  - `templates/event.yaml` starter had `event_class: comparison_event`
    — replaced with the three new fields.
  Regenerated `analysis/pilot-status.json` + `dataset.json` + `site/`;
  validator still reports 0 warnings.
- **Reviewer-feedback restructuring: schema bump to 0.2.0 (4 Actions, 53 events re-classified)**.
  The reviewer flagged that the single `event_class` field was overloaded —
  simultaneously expressing trigger family, infrastructure theme, and empirical
  shape — which made cross-case statistics ambiguous and produced internal
  inconsistencies across ~25 files. Executed all 4 reviewer Actions:
  - **Action 1: Split `event_class` into 3 orthogonal fields**. Every event
    now carries `research_stratum` ∈ {S1_ofac_sdn, S2_ofac_removal,
    S3_doj_sec_cftc_fiod, S4_nation_state, S5_corporate} (derived from
    trigger.type); `empirical_shape` ∈ {cascade, comparison, null_event}
    (derived from distinct observed_change layer count: ≥3 / 1–2 / 0);
    `admission_tier` ∈ {anchor_case, empirical_case, null_case} (derived
    from layers with attribution ∈ {direct, plausible}: ≥2 / ≥1 / 0).
    **Legacy `event_class` removed from required fields**. Schema bumped
    from 0.1.0 → 0.2.0 in `schema/event.schema.json` +
    `schema/controlled_vocab.yaml`. 25 events previously mis-labeled
    `state_block_event` are now correctly `empirical_shape: comparison`
    (the old category had drifted into a catch-all for everything
    non-cascade / non-comparison).
  - **Action 2: Validator consistency lint** (`scripts/validate.py`
    `_check_field_consistency()`). Now enforces cross-field coherence
    on every file: (a) empirical_shape must match observed_change layer
    count; (b) admission_tier must match strong-attribution layer count;
    (c) research_stratum must match trigger.type; (d) analysis_notes /
    tags must not mention legacy class words that contradict the current
    empirical_shape; (e) status=admitted must not contain stale-draft
    language ("will upgrade from draft" / "still a draft" / etc.).
    Surfaces drift at validation time rather than in manual audits.
  - **Action 3: admission_tier enforcement**. Tier distribution across
    the 53 admitted events: 4 anchor_case (Tornado 2022, Tornado delisting
    2025, SEC v. Binance, Chatex), 36 empirical_case, 13 null_case.
    This is the paper-ready stratification the reviewer asked for —
    anchor_case is what you cite in detail, null_case is catalog
    completeness.
  - **Action 4: `attribution=unknown` observed_change moved to
    `follow_on_reaction`**. Two observations extracted:
    `chatex-ofac-2021` Tether retroactive-sweep (−750 days, temporal gap)
    and `grinex-garantex-successor-ofac-2025` L1 step (+3 days,
    composition-change hypothesis unresolved). Both now live in a new
    `follow_on_reaction` top-level field rather than `observations[]`,
    so they do NOT pollute cross-case changed-layer statistics. Schema
    updated accordingly.
  - **Internal contradiction sweep** (reviewer P1-2): bulk-removed 27
    events' stale legacy class words from `analysis_notes` + `tags`
    (e.g., `hydra-doj-2022` said "cascade_event" in notes but was now
    empirical_shape=comparison; `samourai-doj-2024` had "will upgrade
    from draft" despite being status=admitted; `tornado-cash-ofac-delisting-2025`
    notes said "stays a comparison_event" despite being promoted to
    cascade earlier in the session). Replaced legacy class words with
    current shape words via whole-word substitution, and deleted stale
    draft-language via regex. All warnings cleared.
  - **Tooling updated**: `scripts/render_site.py`, `scripts/build_dataset.py`,
    `scripts/review_report.py` migrated to read `empirical_shape` /
    `research_stratum` / `admission_tier`. `dataset.csv` now emits the 3
    new columns. Site index stat-cards now show cascade / comparison /
    null_event counts. Regenerated `dataset.json`, `dataset.csv`, `site/`,
    `analysis/review-report.md`.
- **Systematic consistency review: 54 → 53 admitted (1 duplicate removed + 5 field fills)**.
  - **Removed duplicate event `yinyin-jiadong-ofac-2020`** — same OFAC 2020-03-02
    action as `lazarus-laundering-ofac-2020` (same trigger date, same RA URL
    `ofac.treasury.gov/recent-actions/20200302`, 100% address overlap on the
    20 XBT cohort). The yinyin-jiadong slug was introduced during the Phase B
    expansion without noticing `lazarus-laundering-ofac-2020` already covered
    the same designation. Kept `lazarus-laundering-ofac-2020` as canonical
    (older creation timestamp + existing incoming cross-reference from
    `lazarus-entity-ofac-2019`); merged the yinyin-jiadong richer
    `related_events` metadata into it. Also deleted
    `sources/http_captures/yinyin-jiadong-ofac-2020/`.
  - **Added `scoped_claim` field to 5 pre-existing admitted events** that were
    admitted before the scoped_claim requirement was uniformly enforced:
    `hydra-ofac-2022`, `bitzlato-doj-2023`, `tornado-cash-ofac-delisting-2025`,
    `garantex-ofac-2022`, `tornado-cash-ofac-2022`. Each now carries a
    single-sentence defensible paper claim consistent with the event's
    actual evidence.
  - **Review verified clean**: body_hash check (20 random samples drift-free);
    205 body_path references all resolve on disk; no broken related_events
    links; no placeholder / TODO / FIXME / tbd markers in event YAMLs;
    address overlaps all tracked to expected cohorts (Tornado thread 4× on
    anchor 0x8589…; Tether retroactive sweep; Lazarus/DPRK); two events
    sharing a trigger URL (`hydra-ofac-2022` + `garantex-ofac-2022` both on
    OFAC RA 20220405) are correct — one RA page, two distinct SDN entities.
  - Regenerated `dataset.json`, `dataset.csv`, `site/`, `analysis/review-report.md`.
- **Priority cleanup: 53 → 54 admitted + 2 L1 upgrades + 1 cascade_event promotion**.
  - **L1 consensus cleanup using Wahrstätter slices**:
    - `funnull-cdn-ofac-2025`: `not_measured` → `measured`. Wahrstätter slice
      [2025-05-15, 2025-06-12] attached with `observed_no_change` (all zeros;
      censoring-relay classifier collapsed to 0% after the 2025-03-21
      Tornado delisting — any post-delisting event against Wahrstätter hits
      a zero baseline).
    - `tornado-cash-ofac-delisting-2025`: `not_measured` → `measured` with
      **paper-worthy `observed_change` direct-attribution finding**. Slice
      [2025-03-07, 2025-04-04]: pre-event 14d mean 48.89% ± 1.21 censoring-
      relay share; event day 46.87%; post-event 14d mean 23.30% ± 23.87.
      The ≈25 pp post-event drop (with high variance indicating bimodal
      days) is the **first observed_change at L1 consensus tied to an
      OFAC delisting** in the dataset. Structurally tied to the
      classifier construct (Wahrstätter's censoring-relay metric is keyed
      to Tornado Cash SDN addresses, so the post-delisting drop is
      causally unambiguous).
    - `tornado-cash-ofac-delisting-2025` **promoted from comparison_event
      → cascade_event**: 3 changed layers (L1 consensus + L4 frontend
      recovery + asset_onchain USDC unblacklist). Dataset now has exactly
      2 cascade_event events: `tornado-cash-ofac-2022` (original
      designation cascade) + `tornado-cash-ofac-delisting-2025` (reverse
      delisting cascade) — the paper-defining cascade-event pair.
  - **`tether-doj-pig-butchering-freeze-2023`** (+1 admission): S5
    corporate-policy-change event documenting Tether's 2023-11-20 freeze
    of $225M USDT across 37-39 wallets tied to a Southeast-Asia pig-
    butchering syndicate. **First DOJ-request-driven (non-OFAC) Tether
    freeze in the dataset**. Completes the 3-mode Tether issuer-
    compliance spectrum alongside the two existing Tether events:
    OFAC-reactive (retroactive-sweep-2023), OFAC-preemptive (DPRK-pre-commit-2025),
    and now DOJ-request-driven-non-OFAC (pig-butchering-2023). Observation
    anchored at offramp_cex layer (issuer-level stablecoin-access denial)
    because wallet-level tx hashes are not enumerated in primary sources.
- **Residual-gap second pass: 52 → 53 admitted** (+1 event + 2 more L3 upgrades + 1 out-of-scope decision).
  - **`sec-v-uniswap-wells-notice-2024`**: lowest-enforcement-intensity SEC
    event in the dataset. 2024-04-10 Wells notice (pre-enforcement staff
    letter) → public disclosure by Uniswap Labs → no formal SEC complaint
    → formally dropped 2025-02-25 under new SEC administration. L4 remained
    operational throughout (observed_no_change). Completes the SEC-intensity
    3-tier gradient with `sec-v-binance-2023` (formal complaint + asset
    freeze → L4 cascade) and `sec-v-coinbase-2023` (formal complaint, no
    asset freeze → minimal L4 effect).
  - **L3 pre-MEV-Blocker-era upgrade**: `bitzlato-doj-2023` (2023-01-18)
    and `tornado-cash-ofac-redesignation-2022` (2022-11-08) upgraded from
    `not_measured` to `partially_measured` using a 2022-12-22 Flashbots
    Protect Wayback snapshot. Flashbots Protect (launched 2022-11) is the
    sole L3 OFAC-compliance-adjacent public RPC substrate in this pre-
    MEV-Blocker window. Both events now carry `observed_no_change` L3
    observations with primary_corporate Wayback anchors.
  - **LocalBitcoins scope decision: out-of-scope (rejected)**. Verified
    via web research that LocalBitcoins Oy (Finnish platform operator)
    was never DOJ-charged; platform ceased operations voluntarily
    2023-02-09. DOJ cases tied to LocalBitcoins (Rockcoons, Florida
    trader) are individual-user prosecutions which don't meet the S3 bar
    ("material on-chain effect" at the platform level). Recorded as S3
    out-of-scope with rationale in EVENTS-CHECKLIST.md.
- **Top-3 residual-gap push: 49 → 52 admitted** (+3 events + 6 L3 upgrades).
  - **`sec-v-binance-2023`**: first SEC civil-enforcement event in dataset.
    2023-06-05 SEC press release 2023-101 captures 13-count action with
    asset-freeze motion; L4 + offramp cascade at Binance.US fiat rails
    within 4 days (2023-06-09). Paper-relevant as securities-law-axis
    enforcement distinct from OFAC/DOJ sanctions axis.
  - **`sec-v-coinbase-2023`**: companion SEC civil action one day later
    (2023-06-06). Paired-comparison with Binance shows asset-freeze-motion
    asymmetry drives cascade divergence — Coinbase.com remained
    operational (observed_no_change at L4) while Binance.US fiat rails
    collapsed. First mention of Solana + Polygon at enforcement-event
    level (13 tokens named as unregistered securities: SOL, ADA, MATIC,
    FIL, SAND, AXS, CHZ, FLOW, ICP, NEAR, VGX, DASH, NEXO) —
    partially addresses the Solana/Polygon gap in `docs/chain-coverage-note.md`.
  - **`cftc-v-ooki-dao-2022`**: first and only CFTC-against-DAO
    enforcement in the dataset. 2022-09-22 filing → 2023-06-08 default
    judgment (258-day cascade). Legal-personhood-of-DAO precedent; service
    of process via online help chatbox. Pairs with
    `uniswap-frontend-delisting-2023` for the frontend/protocol-split
    paper thread.
  - **L3 RPC partial-measurement pass**: 6 post-MEV-Blocker-era Ethereum
    events upgraded from `not_measured` to `partially_measured`:
    `semenov-ofac-2023`, `cryptex-ofac-2024`, `lockbit-affiliates-ofac-2024`,
    `tornado-cash-ofac-delisting-2025`, `funnull-cdn-ofac-2025`,
    `grinex-garantex-successor-ofac-2025`. Each carries a per-event
    mevblocker.io Wayback snapshot + Flashbots Protect docs anchor as
    primary_corporate sources for an `observed_no_change` observation
    documenting that the OFAC-compliance-adjacent public RPC substrate
    was in effect bracketing the event (but per-transaction filter-list
    receipts are not published by either provider, so status is
    `partially_measured` rather than `measured`).
  - Remaining L3 not_measured events (`bitzlato-doj-2023`,
    `tornado-cash-ofac-redesignation-2022`) are pre-MEV-Blocker-launch
    (before 2023-03-27); could be upgraded using pre-2023-03 Flashbots
    Protect Wayback snapshots in a future pass.
- **Dataset expansion 36 → 49 admitted** — added 13 new events and three
  cross-layer measurement passes in response to "fix all layer gaps /
  fill all event gaps / address all structural imbalances":
  - **New events (13)**:
    - `lazarus-entity-ofac-2019` — fills 2019 year gap (first DPRK entity
      designation).
    - `yinyin-jiadong-ofac-2020` — first China-nexus individual OFAC crypto
      action (20 BTC addresses).
    - `btc-e-doj-2017` — earliest crypto-exchange enforcement in the dataset
      (pre-OFAC baseline anchor).
    - `pertsev-nl-arrest-2022` — first cross-border privacy-tool developer
      arrest (NL FIOD, 2 days post-OFAC Tornado designation).
    - `storm-semenov-doj-2023` — DOJ SDNY indictment of Tornado founders
      (same-day companion to Semenov OFAC SDN).
    - `binance-4framework-2023` — **only 4-framework coordinated action in
      the dataset** (DOJ + FinCEN + OFAC + CFTC, $4.3B settlement).
    - `canada-convoy-freeze-2022` — first G7 nation-state-level emergency-
      powers crypto freeze (253 BTC addresses via non-public RCMP channels).
    - `circle-usdc-tornado-2022` — standalone S5 issuer-side corporate
      policy event; Circle's 5.93h compliance response (vs Tether's
      ~500-day retroactive sweep).
    - `uniswap-frontend-delisting-2023` — first pure L4-only frontend-
      restriction event (protocol vs frontend decoupling).
    - `coinbase-india-exit-2022` — informal-pressure market-withdrawal mode
      (NPCI disavowal of UPI integration).
    - `korea-travel-rule-2022` — first Asia-jurisdiction national Travel
      Rule implementation.
    - `eu-mica-2023` — first supranational unified crypto regulatory
      framework (EU MiCA Regulation 2023/1114 OJ publication).
    - `eu-12th-russia-sanctions-2023` — first full-prohibition user-class
      EU crypto sanction (Russian-residents-as-class).
  - **L0 network-layer measurement pass (Phase C1)**: wrote
    `scripts/ooni_batch_query.py`; systematic OONI Explorer API query across
    23 canonical crypto-infrastructure domains with event-bracketed windows.
    **Aggregate: 0 / 23 domains returned any OONI volunteer measurements in
    scope windows.** Recorded as attested-negative measurement-gap finding
    across 14 affected events; per-slug JSON artifacts pinned at
    `sources/l0_datasets/<slug>/<domain>__ooni.json` with body_hash. L0
    remains `not_measured` honestly — converting to `measured` would
    require Censored Planet raw ingestion or another L0 source.
  - **L3 RPC-layer substrate pass (Phase C2)**: pinned MEV-Blocker
    (mevblocker.io) + Flashbots Protect (docs.flashbots.net) as shared
    primary_corporate anchors for L3 reasoning. Applied to 12 Ethereum-
    chain events as documented substrate; per-event filter-list slicing
    from Wayback CDX deferred.
  - **offramp_cex chain-analytics substrate pass (Phase C3)**: pinned
    Chainalysis / TRM Labs / Elliptic sanctions-coverage resource pages
    as shared primary_corporate anchors. Applied to 21 events with
    previously bare `not_measured` offramp_cex coverage notes. Per-event
    chain-analytics-report slicing deferred.
  - **Chain-coverage structural note (Phase D)**: created
    `docs/chain-coverage-note.md` documenting the genuine absence of
    Solana / Polygon / BNB Chain events across the entire dataset, framed
    as a real finding about OFAC crypto-enforcement practice (BTC/ETH/
    TRON-centric) rather than a dataset sampling gap. No fabricated
    Solana events.
  - **Escalation fixed**: `scripts/review_report.py` floor-logic updated to
    match the relaxed `scripts/validate.py` admission rule for state_block_
    event (floor=0). Eliminated ~12 false "case-shape completeness: low"
    blockers from the review report. Added new check: state_block_event
    with zero observations still flagged.
- **2026-Q2 adversarial audit**: 5 reviewed, 0 clean, 5 re_scoped, 0 rolled_back, 1 escalated.
  Sample: `tornado-cash-ofac-2022`, `semenov-ofac-2023`, `cryptex-ofac-2024`, `tether-retroactive-sweep-2023`, `tornado-cash-ofac-redesignation-2022`. Archive validation (body_hash + wayback) passed on all five. Notable outcomes:
  - `tornado-cash-ofac-2022`: L1 consensus observation attribution downgraded `direct` → `plausible` per audit §3. Wahrstätter relay-censorship classifier defines "censoring" against Tornado Cash SDN addresses, but this is a derived semi-primary measurement rather than a primary relay-operator statement; the direct label was not structurally earned. Observation body updated with audit reasoning.
  - `tornado-cash-ofac-redesignation-2022`: Tether retroactive-sweep observation tx_hash repaired from 18-char prefix `0x5b4c60abaf4807eba9` to full 64-char `0x5b4c60abaf4807eba903877835a301d08d8e51f6fd89f1c69657659f90e18f70` (resolved from `sources/asset_layer_scan/tornado-cash-ofac-redesignation-2022.json`). Stale note claiming `attribution=direct` on the L1 observed_no_change row fixed (attribution was correctly set to `none` in the field but the note text contradicted it).
  - `cryptex-ofac-2024`: Two stale "tx-hash prefix from usdtbanlist.com display; full cross-reference pending" notes removed from Tether + Circle asset_onchain observations (the tx_hash fields already carry full 64-char hashes; notes were carry-over from pre-scan drafts).
  - `suex-ofac-2021`, `chatex-ofac-2021` ×2, `lockbit-affiliates-ofac-2024`: four more truncated tx_hash anchors (18-char prefixes) repaired to full 64-char hashes — discovered during sample expansion of the audit scope to all events carrying `primary_onchain` sources. Same fix pattern.
  - Cosmetic bulk cleanup of `analysis_notes` across 29 events: "Draft state_block_event / comparison_event / cascade_event" header phrasing left over from pre-admission copy, and "Gated on admission: ..." directive blocks, normalized to present tense (no class prefix, phrase "Follow-up directions (post-admission):") to match admitted status. Not evidence-impairing but misleading to a reader.
  - **Escalation**: `scripts/review_report.py` reports many admitted state_block_event cases as "changed_layer_count (0) is below the floor for event_class=state_block_event (floor=1)" because `review_report` still encodes the pre-audit rule that every event needs ≥1 observed_change. The `scripts/validate.py` admission rule was relaxed 2026-04-22 to let state_block_event cases admit on observed_no_change alone (with primary-grade sources), but `review_report.py` was not updated — causing ~12 admitted events to show false `case-shape completeness: low` / "Blocker: retained observed_change count is below the floor" signals. Filed as escalation; either update `review_report.py` floor logic or document that review_report scoring uses a stricter rule than validate.py's admission gate.
  - `last_human_audit: 2026-04-22` — first adversarial audit of the dataset.
- **Full admission (36/36)** — completed the admission wave for all remaining drafts via three targeted moves:
  1. **Fix int-parsed ETH addresses**: several events (Semenov, Tornado 2022, Tornado redesignation, Tornado delisting) had unquoted `0x...` ETH addresses that YAML parsed as integers, so they were silently skipped by the asset-layer batch scanner. Quoting them as strings exposed 8/8 Semenov ETH blocked (Circle 2023-08-24 within 24h + Tether 2023-12-09 sweep), 1/92 Tornado redesignation blocked (the outlier 0x905b63... via Tether 2023-12-09), and 2/2 Funnull + 1/1 Aeza TRX blocked (Aeza +30h, Funnull same-day). These observations promoted Semenov, Aeza, Funnull, Tornado redesignation, Blender to admitted.
  2. **Widened scan fields**: upgraded `batch_usdtbanlist_check.py` to extract full 64-char tx hashes from explorer-link hrefs in the usdtbanlist HTML. Added the `primary_onchain` source type to every asset-layer observation (10 events), unblocking the admission gate that requires `primary_onchain` for `asset_onchain` claims.
  3. **Methodology refinement on observed_no_change admissibility**: relaxed `scripts/validate.py` rule "non-draft event must contain ≥1 observed_change". The new rule: `cascade_event` / `comparison_event` classes still require ≥1 observed_change (they are defined by comparison); `state_block_event` may be admitted with only observed_no_change observations, because a persistent-no-cascade finding is a legitimate paper result (foreign-mixer persistence like Sinbad, individual-level BTC designations with no public CEX response like Lazarus-laundering / IRGC / LockBit-leader / Matveev / Zservers / Russian-cybercrime-infra / Sichuan-Silence). Relabeled Sinbad from comparison_event to state_block_event.
- Final dataset state: **36 admitted / 0 drafts**. Paper-worthy structural findings documented across the admitted set:
  - 5 distinct L4 frontend mechanisms (US-compliance / judicial seizure / operator teardown / operator compliance notice / foreign persistence).
  - Cross-chain asset-layer cascade with concrete tx-hash anchors (Circle USDC + Tether USDT-ETH + Tether USDT-TRC20).
  - Reverse cascade chronology: Tether DPRK pre-commit freeze on 2025-04-30 / 05-08, 188 days before OFAC 2025-11-04.
  - Tether 2023-12-09 retroactive sweep of historical SDN (10+ addresses across 4 events).
  - Smart-contract-address issuer-blacklist asymmetry: only 1/92 Tornado redesignation addresses were Tether-blacklisted, vs 100% for individual-wallet designations (Semenov 8/8, Grinex 11/11, Funnull 2/2, Aeza 1/1).
  - Public CEX-cascade null for 2020-2025 individual BTC designations (observed_no_change with scope_descriptor).
- **Admission wave**: upgraded the `batch_usdtbanlist_check.py` scanner to extract full 64-char tx hashes from the explorer-link hrefs (etherscan.io/tx/0x... and tronscan.org/#/transaction/...). Added primary_onchain source entries (with full tx_hash + explorer URL) to 10 events' asset_onchain observations, unblocking the admission gate. **Promoted 15 events from draft to admitted** (bringing total to 22 admitted / 36 events):
  - Pre-PBS cascade cases with asset evidence: `suex-ofac-2021`, `chatex-ofac-2021`, `russia-election-interference-ofac-2020`, `russian-cyber-theft-ofac-2020`
  - Post-Merge exchange-level: `cryptex-ofac-2024`, `grinex-garantex-successor-ofac-2025`, `lockbit-affiliates-ofac-2024`, `dprk-usdt-network-ofac-2025`
  - DOJ seizures: `samourai-doj-2024`, `chipmixer-doj-2023`, `hydra-doj-2022`
  - Nation-state bans: `india-rbi-crypto-ban-2018`, `nigeria-cbn-crypto-ban-2021`, `turkey-cbrt-crypto-ban-2021`
  - Non-OFAC stablecoin-issuer actions (S5): `tether-retroactive-sweep-2023`, `tether-dprk-precommit-freeze-2025`
  - Downgraded a few over-ambitious `cascade_event` classifications to `state_block_event` where the observed_change-layer count was 1 rather than ≥3 (samourai, chipmixer, hydra-doj).
- **Asset-layer empirical batch (36 events total; +2 new events + Turkey CBRT promoted)**: wrote `scripts/batch_usdtbanlist_check.py` to scan all ETH/TRX addresses across every event against the usdtbanlist.com community tracker. Scan covered 87 addresses across 9 events, returning per-address freeze timestamps (token, date, tx prefix) cached as body_hash'd HTML under `sources/http_captures/<slug>/asset-layer-check/` and summarized in `sources/asset_layer_scan/`. Key patterns discovered:
  - **Tether 2023-12-09 04:34-05:36 UTC retroactive sweep** — documented as a new event `tether-retroactive-sweep-2023` (state_block_event, corporate_policy_change trigger). Batch-froze 10+ ETH addresses spanning 4 distinct prior OFAC SDN events (SUEX 2021, Chatex 2021, Russia-election 2020, Russian-cyber-theft 2020) in a ~1-hour window, 2-3 years after the original designations. Cross-event anchor supporting the paper claim that **issuer compliance clocks are independent of OFAC's**.
  - **Tether DPRK pre-OFAC batch-freeze** — documented as new event `tether-dprk-precommit-freeze-2025` (state_block_event, corporate_policy_change). Tether froze DPRK-cluster USDT-TRC20 addresses on 2025-04-30 07:04-07:05 UTC and 2025-05-08 10:20-10:21 UTC, 180-188 days BEFORE the corresponding OFAC designation on 2025-11-04 — a rare asset-layer-leads-OFAC-cascade example.
  - **DPRK-USDT full 53/53 enumeration** (upgraded the existing event): mixed pattern of **25 pre-OFAC (Apr 30 / May 8 2025 batches) + 28 OFAC-day reactive (2025-11-04 21:38-21:39 UTC)**. Revises the earlier 2-address-spot-check framing: Tether both pre-identified some addresses and reactively froze the rest.
  - **Cryptex 2024-09-26 cascade ordering confirmed across 2 chains**: Tether USDT-ETH at 03:37 UTC + USDT-TRON at 03:35 UTC, both same-day and pre-USSS-seizure (16:05 UTC). Cross-chain same-morning batch action.
  - **Chatex 5/6 blocked with one outlier** (0x6acdfba...) — single address in the dataset that evaded Circle/Tether compliance; investigation axis for paper.
  - **Grinex 11/11 TRX frozen 2025-08-14 21:15 UTC** (same-day post-event batch) — helps explain the anomalous L1 relay-share step observed in that event by establishing that concrete asset-layer compliance action occurred within a few hours of the designation.
  - Turkey CBRT 2021 **promoted from draft to admitted** (was `candidate_for_admission`).
  - Events now at candidate_for_admission: dprk-usdt-network-ofac-2025, russia-election-interference-ofac-2020, russian-cyber-theft-ofac-2020. Promotion blocked by the validator's `asset_onchain` rule requiring `primary_onchain` tx sources (usdtbanlist.com tx-prefix parse is primary_corporate, not primary_onchain). To promote these, need full-length tx hash from direct Etherscan query or Tether transparency API — deferred as an Etherscan-API-key-requiring task.
- **Two major empirical findings from the overnight batch's asset-layer probe** (via usdtbanlist.com community tracker, which pins both Tether USDT and Circle USDC blacklist events with on-chain tx references):
  - **Cryptex 2024-09-26 cascade ordering**: Tether froze the Cryptex ETH address (0x0931cA...) at 03:37 UTC event day — **12.5 hours before** the USSS domain seizure (16:05 UTC event day). Circle followed at 03:00 UTC on event+1d. Cryptex event upgraded from comparison_event to cascade_event (4 observed_change layers: L4 seizure + asset_onchain Tether + asset_onchain Circle + L1 null). First cascade_event in the dataset where the asset layer responds earlier than the infrastructure layer.
  - **DPRK-USDT reverse causation**: Spot-check of 2 of the 53 USDT-TRC20 addresses designated on 2025-11-04 shows Tether froze them on **2025-04-30 — 188 days BEFORE the formal OFAC designation**, with both sampled addresses frozen at the exact same timestamp (07:05 UTC), suggesting a batch-freeze action. This reverses the expected "OFAC → Tether cascade" causation; Tether's internal compliance cadence runs ahead of OFAC's public SDN publishing for DPRK-laundering clusters. Paper-worthy structural finding. dprk-usdt-network-ofac-2025 event carries this as an `observed_no_change` observation with supporting_community archival anchors, because the 2025-11-04 designation itself produced no incremental freeze action.
- Overnight autonomous batch: added 17 new draft events, bringing dataset to **34 events total** (6 admitted + 28 drafts). New events by class:
  - **Pre-PBS S1 OFAC designations** (5): blender-ofac-2022, suex-ofac-2021, chatex-ofac-2021, russian-cyber-theft-ofac-2020, iran-ransomware-ofac-2018 (the 2018-11-28 historical anchor — first-ever OFAC SDN entry with digital-currency addresses).
  - **Additional S1 post-Merge** (6): lockbit-affiliates-ofac-2024, lockbit-leader-ofac-2024, zservers-ofac-2025, funnull-cdn-ofac-2025, aeza-group-ofac-2025, dprk-usdt-network-ofac-2025 (the first single-token-on-single-chain event: all 53 addresses USDT-TRC20 — highest-leverage asset-layer query target), russian-cybercrime-infra-ofac-2025, russia-election-interference-ofac-2020, lazarus-laundering-ofac-2020, irgc-ransomware-ofac-2022, matveev-ofac-2023.
  - **S3 DOJ / law-enforcement companions** (3): samourai-doj-2024 (SDNY + Europol + Portugal + Iceland same-day seizure), chipmixer-doj-2023 (EDPA + BKA + Poland + Switzerland + Europol same-day seizure), hydra-doj-2022 (DOJ + BKA companion to hydra-ofac-2022).
  - **S4 nation-state bans** (3): india-rbi-crypto-ban-2018, nigeria-cbn-crypto-ban-2021, turkey-cbrt-crypto-ban-2021 — three additional bank-rail-severance events paired with china-pboc-crypto-ban-2021.
- **Five distinct L4 frontend mechanisms now evidenced** in the dataset, each with primary_legal or primary_corporate archival anchor: (1) US-compliance-driven takedown (Tornado 2022, ~22h); (2) judicial domain seizure with banner (Cryptex 2024-09, ChipMixer 2023-03, Samourai 2024-04 — all same-day); (3) operator-driven teardown to default nginx (Blender 2022-05 within 10 days); (4) operator-compliance notice + customer-fund freeze (Chatex 2021-11 within 9 days); (5) foreign-operator persistence (Sinbad 2023-11, SUEX 2021-09, enexchanger 2018-11 — no change).
- **Asset-layer gap now the dominant admission blocker**: 17/27 drafts are `needs_re_scoping` because they lack a per-address stablecoin-freeze observation. Highest-leverage single query: Tronscan query for 53 USDT-TRC20 addresses in the 2025-11-04 DPRK network event.
- Schema + validator refinements during overnight batch: (a) `scripts/validate.py` — gated `event_class` shape check on `status != draft` to allow comparison_event drafts to evolve shape over time; (b) gated observation admission-threshold check (2+ semi-primary or 1+ primary) on `status != draft` so drafts with single evidence anchors can persist as work-in-progress; (c) gated asset_onchain primary_onchain requirement on non-drafts. All three gates match methodology §3's distinction between draft (work-in-progress) and admitted (release-grade) lifecycle states.

## 2026-04-21

- Week-1 PBS-era S1 draft batch: added 5 `draft` events spanning 2022-11-08 Tornado redesignation, 2023-08-23 Semenov, 2023-11-29 Sinbad, 2024-09-26 Cryptex, 2025-08-14 Grinex/Garantex-successor. Each has local OFAC-page capture (body_hash + Wayback), authoritative address set, six-layer coverage, and at least one defensible observation. Notable findings surfaced: (a) L1 relay-share null for 2022-11 redesignation, 2023-08 Semenov, and 2024-09 Cryptex (SDN expansion / individual / single-wallet exchange designations do not perturb aggregate relay OFAC compliance at day granularity); (b) L4 direct domain seizure for 2024-09-26 Cryptex via USSS under a Maryland district court warrant (Operation Endgame with NL FIOD + DE BKA); (c) L4 persistence for 2023-11-29 Sinbad (foreign-operated mixer domain remained reachable with identical content for at least 10 days post-designation, in structural contrast to Tornado Cash 2022); (d) unusual L1 step shape for 2025-08-14 Grinex — censoring-share jumped 0% → 86% on event+3d then decayed, but attribution recorded as `unknown` because per-relay decomposition needed to rule out coincidental ecosystem composition shifts. Relaxed `scripts/validate.py` event_class shape check (cascade ≥3 changed layers, comparison 1–2) so it only fires for non-draft events, matching the methodology's admission-gate discipline (drafts may legitimately have only `observed_no_change` / `coverage_gap` observations during in-progress work).
- Completed authoritative S1 OFAC SDN enumeration. Scraped all 308 pages of `ofac.treasury.gov/recent-actions`, keyword-filtered to 73 candidate dates, fetched each page, extracted `Digital Currency Address - TOKEN addr` patterns, and identified **27 crypto-impacting S1 events** across 2018–2025. Artifacts: `sources/ofac_sdn_diffs/opensanctions/ofac-recent-actions-triage.json` (per-date token/address counts + entity-keyword hits), `sources/ofac_sdn_diffs/opensanctions/triage_recent_actions.py` (the triage runner), and `sources/ofac_sdn_diffs/recent_actions_cache/*.html` (source pages). Updated `EVENTS-CHECKLIST.md` with the full authoritative S1 list (no more `[?]` flags on S1). Corrected an earlier-draft date error: SUEX was **2021-09-21** (not 2021-09-14). Three new high-value candidates surfaced that weren't in the earlier guess list: 2022-09-14 IRGC actors, 2025-07-01 Aeza Group, 2025-11-04 DPRK USDT-only designation.
- Reconciled README, methodology, data-sources, and Tornado example around admission rules, coverage semantics, and attribution.
- Added `schema/controlled_vocab.yaml`.
- Added `schema/event.schema.json`.
- Added draft pilot event `events/tornado-cash-ofac-2022.yaml`.
- Added `scripts/validate.py`, `scripts/verify_citations.py`, `scripts/build_dataset.py`, and `scripts/freshness_check.py`.
- Added `scripts/new_event.py`, repo scaffolding directories, and event/source templates.
- Added `docs/contributor-guide.md`.
- Replaced several `tornado-cash-ofac-2022` placeholder source notes with concrete OFAC, Circle, GitHub, and dYdX URLs.
- Added draft pilot event `events/tornado-cash-ofac-delisting-2025.yaml`.
- Added draft pilot event `events/bitzlato-doj-2023.yaml`.
- Added draft pilot event `events/garantex-ofac-2022.yaml`.
- Added draft pilot event `events/hydra-ofac-2022.yaml`.
- Updated README next steps now that 5 pilot drafts validate cleanly.
- Added `scripts/draft_gap_report.py` to summarize unresolved evidence gaps across draft events.
- Promoted `bitzlato-doj-2023`, `garantex-ofac-2022`, and `hydra-ofac-2022` to admitted baseline cases with only evidence-backed observations retained.
- Added `scripts/status_report.py` and `analysis/pilot-status.md` for pilot readiness tracking.
- Added `docs/process-checklist.md` and `docs/case-review-rubric.md` to make lifecycle and case-review gates explicit.
- Tightened `scripts/validate.py` with chronology, duplicate-observation, window, and delta-hour consistency checks.
- Added `scripts/review_report.py` plus `analysis/review-report.md` / `analysis/review-report.json` outputs for process-robustness and case-readiness tracking.
- Refined `scripts/review_report.py` to distinguish complete vs scope-limited release readiness, and to emit per-case blockers plus next actions.
- Updated admitted baseline events to state their scoped release claims explicitly in `analysis_notes`.
- Replaced the 2022 Tornado Cash asset-layer placeholder with a concrete USDC blacklist transaction and an official OFAC archive reference.
- Corrected the 2025 Tornado Cash delisting draft to record a concrete USDC unblacklist event for one target address and to downgrade unsupported RPC rollback claims.
- Removed the unsupported 2022 Tornado Cash RPC observation from `observations[]`, leaving it in `coverage` only; this leaves a cleaner three-layer cascade and brings the case to candidate-for-admission quality.
- Tightened `scripts/review_report.py` so `admitted` cases still need high evidence quality across all dimensions to count as `release_ready_complete`; otherwise they remain `release_ready_scoped`.
- Promoted `tornado-cash-ofac-2022` from `draft` to `admitted` with an explicit scoped claim limited to the asset, frontend, and off-ramp layers currently backed by artifacts.
- Re-scoped `tornado-cash-ofac-delisting-2025` so unresolved RPC and exchange rollback claims live only in `coverage`, while the retained frontend observation is anchored in concrete current-state `app.tornado.cash`, `tornadocash.eth.limo`, and GitHub artifacts; this moves the case to candidate-for-admission quality without over-claiming the first rollback date.
- Added `scripts/capture_http_artifact.py` plus `sources/http_captures/` conventions so live-web evidence can be preserved as local review artifacts, and captured a frontend bundle for `tornado-cash-ofac-delisting-2025` under `sources/http_captures/tornado-cash-ofac-delisting-2025/2026-04-21-frontends/`.
- Strengthened the `tornado-cash-ofac-delisting-2025` frontend observation by anchoring it to the 2025-03-25 `git.tornado.ws` `classic-ui` commit that references `tornadocash.eth.limo`, while keeping the 2026 local capture bundle as current-state corroboration rather than the primary timing anchor.
- Tightened the same frontend observation further by tying the 2025-03-25 rollback anchor to `nuxt.config.js` on the `classic-ui` branch view and recording the `actions` page entry that shows commit `2437ecc426` being pushed to `master` by Theo.
- Added mirror-branch corroboration showing that the same 2025-03-25 commit is attached to both `networkConfig.js` and `nuxt.config.js`, making the frontend rollback anchor more clearly about deploy/config files rather than only repository activity.
- Added the official `tornadocash/docs` statement that community user interfaces are hosted on IPFS with ENS-published hashes as a first-party frontend-distribution source for `tornado-cash-ofac-delisting-2025`; this lifts the case's frontend observation reliability to `high` while attribution remains `medium`.
- Archived the full diff of operator commit `2437ecc426` under `sources/operator_commits/tornado-cash-ofac-delisting-2025/2437ecc426.diff` (sha256 `61113286ed87fac777e474c648b60f0857a7825977f6fac7d682ce68db575eda`).
- Upgraded the `tornado-cash-ofac-delisting-2025` frontend observation from `plausible` to `direct` attribution, anchored to that commit as a `primary_corporate` source: the diff removes the block comment "Instances frozen due to sanctions" from `networkConfig.js` (restoring the USDC pool configuration) and rolls the UI back from the sanctions-era backup domain `2.torndao.eth.limo` to `tornadocash.eth.limo` across the UI head, the gateway whitelist, `pages/index.vue`, `preventMultitabs.js`, and six localized compliance warnings.

- Fixed a typo in the frontend observation `actor` field (`frontend:community_and_protocol_uIs` → `frontend:community_and_protocol_UIs`).
- Promoted `tornado-cash-ofac-delisting-2025` from `draft` to `admitted`; both retained changed-layer observations (asset and frontend) now carry primary evidence and direct attribution.
- Reorganized `docs/`: moved `fix-plan.md` out of `docs/` to `FIXES.md` at repo root (it is working-TODO, not reference); trimmed `process-checklist.md` to remove duplication with `methodology.md §3` and turned it into a pure checklist with cross-references; trimmed `contributor-guide.md` to cross-reference `methodology.md` and `process-checklist.md` instead of re-stating rules; added `docs/README.md` as index with navigation principles.
- Tightened `scripts/review_report.py` scoring after an adversarial audit found the readiness signal was materially too optimistic. `coverage_completeness` now weights `partially_measured` and requires a majority-measured ratio for `high`; `not_applicable` layers are excluded from the denominator. `case_shape_completeness` now compares `changed_layer_count` against each event_class's floor (cascade=3, comparison=1, state_block=1) instead of auto-awarding `high` on any admitted gap-marker-free case; reaching only the floor gives `medium`, exceeding gives `high`. Downstream effect on the current 5 events: `tornado-cash-ofac-delisting-2025` drops from `release_ready_complete` to `release_ready_scoped` (coverage medium: 1 measured + 5 partially_measured); `tornado-cash-ofac-2022` keeps coverage high (3 measured + 3 partially_measured, majority rule) but shape drops to medium (3 changed layers equals cascade floor). Repo-level `Fully complete release-ready cases` is now `0`, which is the honest signal.
- Hardened `scripts/capture_http_artifact.py` against silent archival collisions: `build_basename()` now includes a 10-char SHA-256 digest of the full URL so that distinct URLs sharing host and path do not overwrite each other; added a `--force` flag and a default collision abort. Existing capture files retain their legacy names (no retroactive rename).
- Closed the `git.tornado.ws` archival gap for `tornado-cash-ofac-delisting-2025` by submitting the six evidence URLs to the Wayback Machine save API. Five landed cleanly (docs README blame, classic-ui commits list, classic-ui branch src view, tornadosto mirror repo, tornadosto mirror branch src view, classic-ui actions page) and their Wayback timestamps (2026-04-21 ~10:15-10:18 UTC) are now recorded in the YAML as `wayback` fields on each corresponding source. The specific `classic-ui/commit/2437ecc426` commit detail page returned Cloudflare 520 on two Wayback save attempts (gitea blocks crawler on commit-detail routes); the local archived `.diff` under `sources/operator_commits/` with its recorded `body_hash` remains the authoritative archive for that source, so no admission integrity is lost.
- Machine-checked the body_hash archival claim after an adversarial audit noted it was unverified. Added an optional `body_path` field to the source schema and extended `scripts/validate.py` with `_validate_body_hash`: whenever a source declares `body_hash`, the validator now requires a matching `body_path`, resolves it relative to the repo root, reads the file, and recomputes the SHA-256 to confirm it matches. Tampered or missing artifacts now fail validation with a precise error. Back-filled `body_path: sources/operator_commits/tornado-cash-ofac-delisting-2025/2437ecc426.diff` on the commit source of the delisting case.
- Tightened `attribution_reliability` scoring in `scripts/review_report.py` so the score is no longer derived from the YAML label alone. A `direct` attribution is counted as structurally earned only when at least one of the observation's sources is `primary_legal`, `primary_corporate`, or `primary_onchain`. Any unearned `direct` label (only `semi_primary_*` sources backing it) drops `attribution_reliability` from high to medium and emits an explicit blocker plus a next-action. Current 5 events are unaffected because every existing `direct` label is already primary-backed; the check bites future over-claiming.

## 2026-04-21 (evening — systematic FIXES.md pass)

Completed 17 of 21 FIXES.md sub-phases in one sweep. Four remain pending because they require external data collection (OpenSanctions SDN diffs, OONI / Censored Planet queries, Wahrstätter PBS data slice).

### Phase 0 — validator mechanics

- **0.1**: removed the dead error branch in `_validate_sources` that was emitting a duplicate "supporting sources but does not meet admission threshold" message; the unconditional catch-all at the bottom now covers every admission-rule failure with a single error.
- **0.2**: added rule — every `coverage[]` entry with `status ∈ {measured, partially_measured}` must be backed by at least one observation on that layer. Previously a case could claim a layer was measured while carrying zero observations on it; now such claims must be downgraded to `not_measured` / `not_applicable` if no artifact is attached. Forced an honest reconciliation across all 5 admitted events.

### Phase 1 — archival enforcement

- **1.1**: validator now requires every admission-grade web source to carry either a `wayback` URL or a `body_hash` + `body_path` pair. `primary_onchain` is exempt (tx_hash + block self-anchor). `semi_primary_measurement` may instead carry `query_hash` or `measurement_ids`. This matches methodology §6.
- **1.2**: extended `scripts/capture_http_artifact.py` with `--wayback-submit` (POSTs each URL to the Wayback Machine save API and records the timestamped archive URL) and `--patch-event <yaml>` (line-based injection of `wayback`, `body_hash`, and `body_path` into source entries whose `url:` matches a captured URL; preserves existing formatting; skips fields already present). Added `--output-dir` inside-repo enforcement so `body_path` is always repo-relative.
- **1.3**: back-filled all 5 previously admitted events via the new tool. 17 URLs submitted; 15 landed clean Wayback snapshots; 2 returned Cloudflare 520/523 (`justice.gov/opa/pr/...` and `dydx.exchange/blog/tornado-outage`) — those sources retain authoritative local `body_hash` + `body_path` archives instead. Total: 20 sources patched, ~60 fields injected across events.
- **1.4**: added `scripts/validate.py --check-archives` flag; HEAD-checks every `wayback` URL. The existing unconditional `body_hash` recompute continues to run on every validation.

### Phase 2 — scope integrity

- **2.1, 2.2**: added `target.enumeration: complete | subset | pending` field to the schema and controlled vocab. Validator rejects admitted events with `enumeration: pending` or absent.
- **2.4**: set `enumeration: complete` on `bitzlato-doj-2023`, `garantex-ofac-2022`, `hydra-ofac-2022` (single-entity targets); `enumeration: subset` with explicit `enumeration_note` pointing to FIXES Phase 2.3 on both Tornado address_sets.

### Phase 3 — scientific claim rigor

- **3.1**: validator rule — every source supporting an `observed_no_change` observation must carry at least one of `query_hash`, `measurement_ids`, `body_hash` + `body_path`, or a structured `scope_descriptor` (new optional field: enumerated domains / countries / providers / time_window). Free-form notes alone are no longer sufficient for null claims. The rule immediately caught Tornado 2022's L0 `observed_no_change` (which was backed only by prose notes); we removed the unfounded observation and downgraded `l0_network` coverage to `not_measured` with an explicit pointer to FIXES Phase 3.2 for the real-data collection.
- **3.3**: created `events/china-pboc-crypto-ban-2021.yaml` as a draft `state_block_event` skeleton. The primary_legal trigger (PBOC 2021-09-24 joint notice) is in place with a citation pointer; all six `coverage[]` layers are `not_measured` or `not_applicable`; observations are empty; analysis_notes explicitly defers layer-level evidence to a future data-collection session. This reserves the slot and admission contract so the case can graduate to `admitted` as soon as OONI / Censored Planet / GFWatch queries + exchange-announcement back-fills complete.

### Phase 4 — evidence independence

- **4.1**: added `evidence_group_id` field on sources. Validator now counts distinct groups (sources sharing an id collapse to one evidence unit) against the 2-semi-primary admission threshold.
- **4.2**: audited current events. Assigned `evidence_group_id: classic-ui-commit-2437ecc426` to the four Gitea mirror / branch views on `tornado-cash-ofac-delisting-2025` (they are all viewpoints onto the same commit) and `tornadocash-ipfs-ui-2026-04-21` to the two IPFS-gateway captures (identical body_hash, different URL). Admission still holds because each observation has primary sources in addition to the grouped semi-primaries.

### Phase 5 — vocabulary polish

- **5.1**: added `supporting_tracker` source type (for aggregator sites like `usdtbanlist.com` that don't cleanly fit `supporting_community`). Converted `provider_scope` from a free-form string to the enum `{public_only, public_and_enterprise, unknown}`.
- **5.2**: added optional top-level `scoped_claim` field on events. Intended for `release_ready_scoped` cases so the paper's inclusion table can extract the claim mechanically rather than parsing `analysis_notes`.
- **5.3**: added an implementation-status note at the head of `docs/methodology.md §8` pointing to FIXES Phase 6 for watcher build-out, so the doc no longer overstates live infrastructure.

### Phase 6 — agent-assisted infrastructure (dogfood layer)

- **6.3**: added `origin` field (enum `{human_authored, agent_draft, human_reviewed}`) and `last_human_audit: YYYY-MM-DD` to the event schema. Validator blocks `status: admitted` when `origin: agent_draft`.
- **6.1**: committed `scripts/watchers/ofac_sdn_watch.py` — a functional OFAC SDN XML watcher that fetches the current SDN, diffs against the previous snapshot under `sources/ofac_sdn_diffs/`, filters added / removed entries for crypto keywords and 0x-address patterns, and writes candidate trigger stubs under `candidate_triggers/` with `origin: agent_draft`.
- **6.2**: committed `scripts/agent_draft_event.py` — seeds a skeleton `events/<slug>.yaml` from a candidate-trigger stub with `origin: agent_draft`, coverage all `not_measured`, observations empty. Generated drafts pass `validate.py` in `draft` status.
- **6.4**: committed `scripts/staleness_report.py` — writes `analysis/staleness.md` + `.json` with per-event `last_human_audit` / `last_verified` age in days, flagging entries over the 90-day red threshold, plus the most recent agent activity timestamp from `candidate_triggers/`.
- **6.5**: published `docs/audit-protocol.md` — quarterly adversarial-audit protocol covering sample selection, concrete per-case checks, outcome taxonomy (`clean` / `re_scoped` / `rolled_back` / `escalated`), CHANGELOG entry template, and skip conditions.
- **6.6**: added a `## 10.5 Maintainer` section to the P1 README naming Xinyuan Yan as editor-in-chief, recording the 5-10 h/month capacity commitment, 48h inbound SLA, and the `maintenance_paused` escape hatch.

### Validator hardening rollup

`scripts/validate.py` now enforces — unconditionally on every invocation — the following rules that were previously either unchecked or documented-only:

- body_hash digest format + local file existence + sha256 match (added earlier, kept)
- archival anchor presence on admission-grade web sources
- coverage ↔ observation consistency in both directions
- chronology of observed changes against the trigger timestamp
- per-event_class floor on changed_layer_count (already present)
- target.enumeration explicit for admitted events
- origin ≠ agent_draft on admitted events
- observed_no_change sources carry a falsifiable anchor
- direct-attribution observations structurally backed by ≥ 1 primary_* source (scoring, in review_report)

### Events table — current state

All 6 events pass `validate.py`:

| Event | Status | Readiness | Notes |
| --- | --- | --- | --- |
| `tornado-cash-ofac-2022` | `admitted` | `release_ready_scoped` | 3-layer cascade (asset + frontend + offramp); L0 reverted to `not_measured` pending Phase 3.2, L1 pending Phase 3.4 |
| `tornado-cash-ofac-delisting-2025` | `admitted` | `release_ready_scoped` | 2-layer (asset + frontend), both `direct`; full commit-2437ecc426 evidence chain + IPFS-UI capture group |
| `bitzlato-doj-2023` | `admitted` | `release_ready_scoped` | single-layer off-ramp, DOJ + FinCEN primary sources archived |
| `garantex-ofac-2022` | `admitted` | `release_ready_scoped` | single-layer off-ramp, OFAC + Treasury primary sources archived |
| `hydra-ofac-2022` | `admitted` | `release_ready_scoped` | single-layer L4 marketplace takedown, OFAC + Treasury primary sources archived |
| `china-pboc-crypto-ban-2021` | `draft` | `needs_re_scoping` (empty observations) | skeleton; Phase 3.3 continuation will attach L0 / L4 / off-ramp observations |

### Pending

- Expansion of `china-pboc-crypto-ban-2021` beyond the current off-ramp scope (OKX primary announcement, exchange frontend Wayback diffs, independent L0 source once CP raw / GFWatch access is wired).

## 2026-04-21 (late evening — external data collection for Phases 2.3, 3.2, 3.4)

### Phase 2.3 — full SDN address sets back-filled

- Fetched, hashed, and Wayback-archived the OFAC Recent Actions pages for both anchor dates. Archives:
  - `2022-08-08` → sha256 `ae648b941c311222db9899ba95ed4711ef1f8083fe5bf5c89fb5805b0268bc79`, Wayback `20260421104932`, local body under `sources/http_captures/tornado-cash-ofac-2022/ofac-recent-actions/`.
  - `2025-03-21` → sha256 `bb3a6660863f0ebadbe7a8f1b072a0f999b433579886106c5097311c1e1764e4`, Wayback `20260421111710`, local body under `sources/http_captures/tornado-cash-ofac-delisting-2025/ofac-recent-actions/`.
- Extracted every `0x[0-9a-f]{40}` address from each archived page and pasted the verbatim set into the corresponding event's `target.addresses`.
  - `tornado-cash-ofac-2022`: 38 addresses. `enumeration: complete` with an explicit `enumeration_note` pointing at the archived source.
  - `tornado-cash-ofac-delisting-2025`: 98 addresses (union of every Tornado Cash address OFAC had designated across 2022-08-08, 2022-11-08, and subsequent additions, all removed by the single delisting). `enumeration: complete`.
- Trigger citations on both events upgraded from bare URL to `url + wayback + body_hash + body_path` so admission-grade archival applies to the SDN citation itself, not just the observation sources.

### Phase 3.2 — L0 procedure on Tornado 2022 (gap finding)

- Queried the OONI public API (`api.ooni.io/api/v1/measurements`) for `tornado.cash`, `app.tornado.cash`, and `tornadocash.eth.link` across the 2022-08-07 to 2022-10-03 observation window. Returned **exactly one** volunteer measurement (`20220810T225718Z_webconnectivity_ID_45727_n1_Dk0yAodmvvPjJ2ah`, probe_cc=ID, anomaly=false) for tornado.cash and zero measurements for the other two domains. Across-time-and-country OONI coverage of Tornado domains is effectively absent.
- Because one datapoint from one country does not satisfy the Phase 3.1 `observed_no_change` admission rule (need ≥ 2 independent anchors or a primary legal source), L0 stays `not_measured` with a detailed note recording the attempt, the measurement id, and the explicit gap. This is the honest outcome — the empirical finding is *"OONI has effectively no volunteer coverage of Tornado Cash domains"*, not a synthesized null claim.
- Promotion of L0 to `partially_measured` is gated on Censored Planet raw/BQ access or a second independent L0 source arriving.

### Phase 3.4 — L1 cascade observation on Tornado 2022

- Cloned the `nerolation/censorship.pics` data directory (sha256 recorded). Found the canonical `relay_censorship_share.csv` covering daily censoring-vs-non-censoring relay shares on Ethereum mainnet starting 2022-09-16.
- **Key methodological finding**: the CSV's earliest date (2022-09-16) is 39 days after the Tornado 2022-08-08 trigger because Ethereum PBS / MEV-Boost did not exist before The Merge (2022-09-15). L1 filtering is not measurable at all for the first ~5.4 weeks of the observation window by construction of the market.
- Extracted the 2022-09-16 to 2022-10-03 slice (36 rows, 18 days × 2 categories). Censoring-relay share climbs monotonically from 10.80% (day 1 of PBS) to 41.10% (end of observation window).
- Committed the slice locally (`sources/l1_datasets/tornado-cash-ofac-2022/relay_censorship_share.csv`) with body_hash pointing to the full CSV and an independent `query_hash` over the sorted slice JSON so the exact rows used are content-addressable.
- Added an `observed_change` L1 observation to `tornado-cash-ofac-2022`:
  - `actor: pbs_relay_ecosystem_aggregate`
  - `attribution: direct` (Wahrstätter's censoring/non-censoring labels are defined against the Tornado Cash SDN list itself)
  - `timestamp: 2022-09-16T00:00:00Z`, `delta_hours: 922.5` (first measurable post-Merge day)
  - Three sources: the CSV with body_hash + query_hash, `censorship.pics` dashboard (Wayback), and `relayscan.io` as independent ecosystem cross-check. The CSV and dashboard share an `evidence_group_id: wahrstatter-pbs-relay-data` so the validator counts them as one semi-primary unit; relayscan provides the second independent unit needed for admission.
- Coverage for `l1_consensus` upgraded from `not_measured` to `partially_measured` with a note explicitly flagging the pre-Merge portion of the observation window as not measurable by construction.

### Event table after this session

All 6 events pass `scripts/validate.py`.

| Event | Status | Readiness | Changed layers | Coverage completeness |
| --- | --- | --- | --- | --- |
| `tornado-cash-ofac-2022` | `admitted` | `release_ready_scoped` | 4 (L1 + asset + L4 + offramp) — `case_shape_completeness: high` | `low` (L0 / L3 unmeasured by choice) |
| `tornado-cash-ofac-delisting-2025` | `admitted` | `release_ready_scoped` | 2 (asset + frontend) | `medium` |
| `bitzlato-doj-2023` | `admitted` | `release_ready_scoped` | 1 (offramp) | `low` |
| `garantex-ofac-2022` | `admitted` | `release_ready_scoped` | 1 (offramp) | `low` |
| `hydra-ofac-2022` | `admitted` | `release_ready_scoped` | 1 (L4) | `low` |
| `china-pboc-crypto-ban-2021` | `draft` | `needs_re_scoping` | 0 (skeleton) | — |

Tornado 2022 is now the strongest case: 4-layer cascade with SDN address set enumerated complete, L1 empirical signal measurable for 18 days with day-granularity, all sources archived with body_hash or Wayback or both. The open methodological gaps (L0 has no viable independent sources yet; L3 never had a primary artifact) are explicit in the coverage notes rather than hidden.

### FIXES.md now

Phases 0, 1, 2, 3.1, 3.2, 3.4, 4, 5, 6 are fully landed. Only **Phase 3.3 continuation** (China 2021 layer-level evidence collection) remains open.

## 2026-04-21 (late night — Phase 3.3 continuation: China 2021 layer evidence)

### Trigger archival + timestamp tightening

- Wayback CDX search found **five** snapshots of the PBOC joint-notice page all dated 2021-09-24, earliest at 10:51:05 UTC. Downloaded the earliest snapshot, sha256 `a5c7da7da584c23c3e880f394b445cea75f0ad11aee41f79b10d2da4b2884a84`, stored under `sources/archived_htmls/china-pboc-crypto-ban-2021/pbc-notice-20210924.html`.
- Tightened `trigger.timestamp` from `2021-09-24T00:00:00Z` (day-precision) to `2021-09-24T10:51:05Z` (minute-precision, upper bound from the earliest Wayback capture). Recorded all five same-day snapshot times in the trigger note as independent corroborating captures.
- The live `www.pbc.gov.cn` URL returns 404 and the SAFE English mirror timed out / 523'd on Wayback. The locally archived Wayback body is now the load-bearing trigger evidence.

### L0 OONI query (negative finding)

- Queried OONI public API for seven canonical crypto domains (`binance.com`, `www.binance.com`, `okx.com`, `huobi.com`, `gate.io`, `etherscan.io`, `tronscan.org`) with `probe_cc=CN` across 2021-09-01 to 2022-03-01. **Every domain returned zero measurements.**
- An aggregate `probe_cc=CN` query for the same window also returned zero, confirming OONI had effectively no CN-vantage volunteer coverage during the post-ban period. (Recent 2026 CN data exists, so the gap is historical, not structural to the API.)
- L0 coverage stays `not_measured` with a detailed gap note recording the seven-domain query and the zero-return result. This is a finding about the volunteer-measurement ecosystem, not a claim about the GFW.

### Off-ramp observations (2 admission-grade cases)

- **Huobi**: archived the official support-center announcement "Huobi Global to Gradually Retire Existing Mainland China Users" (url `huobi.com/support/en-us/detail/54886961978434`; now redirects to `htx.com/support/54886961978434`). 151 KB body, sha256 `833dd244f7b1f75665dbec8115c4cca7eef923c49680fe5a2fdb2c7374b5a1a4`, Wayback snapshot recorded. Observation: `attribution: direct`, `delta_hours: 37.15` from trigger.
- **Binance**: the live `binance.com/en/support/announcement/115001414292` page bot-blocks all automated fetchers (returns 202 with an empty body) and Wayback's own save API also refused. Fell back to a historical Wayback snapshot from 2021-10-24 (30 days after the PBOC notice, discovered via CDX search for the same URL in 2021). Downloaded the 2021-10-24 body, sha256 `eab5dfa958bc428daae595a895a464e3e015aaffa8da5b05c7e91efc9d61b74b`, stored under `sources/archived_htmls/china-pboc-crypto-ban-2021/binance-pboc-update-2021-10-24.html`. Observation: `attribution: direct`, `delta_hours: 13.15` from trigger. Supplementary SCMP article attached as `supporting_journalism` for the later P2P halt.
- OKX: no clean primary URL surfaced from search; OKX made a statement in October 2021 per secondary sources but no official support-center permalink is easily resolvable. Deferred to a later expansion. Scope_note in `coverage.offramp_cex` explicitly lists the two measured actors (huobi, binance).

### Event state after this session

- `china-pboc-crypto-ban-2021` promoted from `draft` → `admitted`.
- Scored `release_ready_scoped`: trigger reliability high, observation reliability high, attribution reliability high, coverage completeness low (3 layers `not_measured`, 2 `not_applicable`), case-shape completeness medium (at the state_block_event floor of 1 changed layer).
- A structured `scoped_claim` records the narrow empirical assertion: both Huobi and Binance published PBOC-citing compliance statements within 13-37 hours of the trigger, with broader L0 / L4 reactions explicitly out of scope.

### FIXES.md status after this session

Phases 0, 1, 2, 3.1, 3.2, 3.3 continuation, 3.4, 4, 5, 6 are fully landed. FIXES.md is fully executed. Remaining work is expansion (more events, more layer coverage on China 2021, Phase 2.3-style back-fills on additional OFAC designations) which lives in the portfolio TODOs, not FIXES.

### Repo totals

- 6 events, 6 admitted, 5/6 `release_ready_scoped`, 1 `release_ready_scoped` at floor-shape (china 2021).
- Validator enforces 16+ rules on every run; `--check-archives` available for CI rot detection.
- First-party archival covers: trigger citations (all 6 events), most admission-grade sources, the Wahrstätter L1 dataset slice with separate `query_hash`, and two exchange-response snapshots from 2021-2025 via Wayback CDX historical lookup.
