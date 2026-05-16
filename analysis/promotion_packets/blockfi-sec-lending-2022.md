# Promotion review — blockfi-sec-lending-2022

## Verdict
- **promotion_recommendation**: `admit_with_minor_fixes`
- **confidence**: high
- **one-sentence justification**: The event is a tightly-scoped, single-layer SEC enforcement comparison case with two archived primary-legal anchors that directly name BlockFi Interest Accounts and the cease-and-desist obligation; the only blockers are a missing `denominator_artifact` on the `measured` `offramp_cex` coverage row (recommended by §3.5 even though a same-layer observation anchor technically satisfies it) and a `last_verified: 2026-05-16` future-dating relative to `created_at`.

## Trigger gate
- citation count + tier: 2 citations, both `primary_legal` (lines 20-30). Methodology §3.1 requires "machine-checkable primary source at a stable URL"; two primary-legal sources exceeds the bar.
- archive anchors present: yes — both citations carry `body_hash` + `body_path` pairs (lines 22-23, 29-30). The captured files exist at `sources/http_captures/blockfi-sec-lending-2022/primary/` and the SEC press release SHA256 in the capture metadata (`805ea579d1452e64855b30ea674d7e83f960dc40c996dec5b469c24c781bfa01`) matches line 22 verbatim.
- timestamp + precision honest: yes — `2022-02-14T00:00:00Z` with `timestamp_precision: day` (lines 17-18) is consistent with the SEC press release headline "BlockFi Agrees to Pay $100 Million in Penalties..." which is dated 2022-02-14. Day-level precision is appropriate for an SEC press release; methodology §3.1.4 allows day-level for legal/corporate sources when `timestamp_precision: day` is recorded.
- verdict: **pass**

## Per-observation gates (one block per observation row)
- layer `offramp_cex` / kind `observed_change` / attribution `direct` / anchor types present: both sources carry `body_hash` + `body_path` (lines 87-88, 93-95). Schema §observation requires `body_hash + body_path` OR `query_hash` OR `measurement_ids` OR `scope_descriptor` on at least one source — satisfied twice over. / verdict: **pass**

(Only one observation row exists; lines 76-98.)

## Coverage status honesty
- `l0_network: not_applicable` (lines 53-54) — correct. An SEC product-restriction order has no inherent network-layer interpretation.
- `l1_consensus: not_applicable` (lines 55-56) — correct. No on-chain validator policy is implicated by the lending product settlement.
- `l3_rpc: not_applicable` (lines 57-58) — correct. No RPC provider implication.
- `l4_frontend: not_measured` (lines 59-64) — honest. The YAML explicitly states "No historical BlockFi frontend diff is retained here" (lines 62-64); this is consistent with methodology coverage-status table line 143 ("did not have enough source coverage to make a claim").
- `asset_onchain: not_applicable` (lines 65-66) — correct.
- `offramp_cex: measured` (lines 67-73) — defensible but with one process gap. The lending product is the substrate, and the cited primary-legal sources directly establish the product-restriction transition. Per §3.5 lines 245-250, a `measured` coverage row needs **either** a `denominator_artifact` on the row **or** at least one same-layer observation source with a replayable anchor (`body_hash` + `body_path`, `query_hash`, etc.); the observation row at lines 84-98 carries both — so the gate is technically satisfied. The YAML does not add a `denominator_artifact` block to the coverage row itself, which is permitted but is the looser of the two options.

## Attribution discipline
- `offramp_cex` / `observed_change` / `direct` (lines 76-98): the cited SEC press release explicitly names "BlockFi" and the "BlockFi Interest Accounts (BIAs)" product, and states BlockFi "agreed to ... cease its unregistered offers and sales of the lending product, BlockFi Interest Accounts (BIAs)" — verified directly in the archived body at `sources/http_captures/blockfi-sec-lending-2022/primary/www.sec.gov__newsroom-press-releases-2022-26__ae4da616fa.html`. This is a named-link, same-day, primary-legal anchor between trigger and observed change; `direct` attribution is unambiguously supported.

## Scoped claim
The `scoped_claim` (lines 106-109) explicitly disclaims any frontend, L1, L3, or on-chain censorship interpretation and asserts only a product/service restriction at the centralized lending platform. This is strictly narrower than what `direct` attribution on a single `offramp_cex` `observed_change` row could license, so the scoped claim is well inside the evidence envelope. It also matches `empirical_shape: comparison` (line 7) and `admission_tier: empirical_case` (line 8), both correctly chosen for a 1-layer `observed_change` event per methodology §3.2 lines 197-214.

## Self-contradiction check
- No "null_event rather than null_event"-style typos in `analysis_notes` (lines 100-104).
- `analysis_notes` ("No frontend takedown, token delisting, or on-chain asset freeze is asserted", line 104) is consistent with the `not_applicable` / `not_measured` coverage statuses at lines 53-66.
- `scoped_claim` is consistent with `attribution: direct` on the single `offramp_cex` row and does not over-attribute beyond `offramp_cex`.
- `research_stratum: S3_doj_sec_cftc_fiod` (line 4) is consistent with `trigger.type: sec_action` (line 15) and `actor: US_SEC` (line 16), satisfying the §3.2 line 193-195 actor/type coherence rule.
- One minor temporal oddity: `created_at: 2026-05-16T00:00:00Z` (line 11) is the same date as `last_verified: 2026-05-16` (line 12), which is internally consistent today but is the file's own ingestion date, not a substantive issue.

## Specific issues blocking admit_now
- **Missing `denominator_artifact` on `offramp_cex` coverage row** (lines 67-73). Strictly, the same-layer observation anchor at lines 84-98 satisfies §3.5 lines 245-250, so this is not a hard schema failure — but for a `measured` coverage row carrying a paper-grade `comparison` event, adding an explicit `denominator_artifact` block referencing the SEC order PDF would make the denominator declaration self-contained at the coverage row level and remove a reviewer ambiguity.
- **No `timestamp_sources[].url` or anchor on `timestamp_sources` entry** (lines 34-36). The single entry is a bare `type: primary_legal` + `note`; the schema does not require a URL there because the timestamp citation is already provided in `trigger.citation`, but this is a low-effort clarity fix.

## Recommended fixes (if admit_with_minor_fixes)
- Add a `denominator_artifact` block to the `offramp_cex` coverage row (lines 67-73), reusing the administrative-order `body_hash` + `body_path` from line 29-30 and a one-line `note` that the SEC order is the structured product-restriction substrate. This pre-empts any reviewer challenge to `measured` status and makes the coverage row self-contained per §3.5 line 245-247.
- Consider adding `evidence_use: admission_anchor` on both `trigger.citation` entries (lines 20-30). Methodology §3.5 lines 238-242 expects this annotation when distinguishing admission anchors from contextual citations; not strictly required since both are archived, but improves provenance metadata.
- Optionally tighten `timestamp_sources` (lines 34-36) by pointing it at one of the two primary citations explicitly via URL.
- No content change needed to the scoped_claim, analysis_notes, attribution, observation row, or trigger citations — these are already disciplined.
