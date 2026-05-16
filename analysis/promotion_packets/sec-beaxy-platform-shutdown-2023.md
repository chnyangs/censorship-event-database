# Promotion review — sec-beaxy-platform-shutdown-2023

## Verdict
- **promotion_recommendation**: `admit_with_minor_fixes`
- **confidence**: medium
- **one-sentence justification**: Trigger and observations are anchored by two locally captured SEC primary_legal artifacts with body_hash + body_path on every citation and the press release literally contains the wording each observation row cites, but the `admission_tier: anchor_case` claim is structurally inconsistent with the YAML's own `empirical_shape: comparison` and only two strong-attribution layers, both sourced to the same single SEC release — so promotion is appropriate only after either a tier downgrade or a second independent layer/source is added.

## Trigger gate
- citation count + tier: two `primary_legal` citations (YAML L20-34) — SEC press release 2023-64 (L21) and the underlying SEC complaint PDF in N.D. Ill. No. 1:23-cv-1962 (L29). One primary_legal is sufficient by §5; two are present.
- archive anchors present: yes — both citations carry `body_hash` and `body_path` (L22-23, L30-31) and the local files exist under `sources/http_captures/sec-beaxy-platform-shutdown-2023/primary/` with a matching `manifest.json` (sha256s align: `67f588f1…` for the HTML and `e46031…` for the PDF).
- timestamp + precision honest: `2023-03-29T00:00:00Z` at `timestamp_precision: day` (L17-18). SEC press release 2023-64 is dated 2023-03-29; day-level precision is appropriate for a press-release/announcement trigger per §3.1 (point 4). `timestamp_sources` row at L35-37 declares day-level timing.
- verdict: **pass**

## Per-observation gates (one block per observation row)

- **Row 1 — L4 frontend** (L81-96): `observation_kind: observed_change`, `attribution: direct`. Anchor types present on the single source: `body_hash` + `body_path` (L92-93) plus the primary_legal `url` (L91). Meets §5 (one primary suffices) and the schema's `primary_legal → body_hash+body_path OR wayback` rule. Verdict: **pass**.
- **Row 2 — offramp_cex** (L97-114): `observation_kind: observed_change`, `attribution: direct`. Anchor types present: `body_hash` + `body_path` (L108-109) plus primary_legal `url` (L107). Verdict: **pass on schema**, with one caveat noted below (same source as Row 1 — the SEC press release is the sole supporting artifact for both observation rows; the complaint PDF cited at trigger level is not echoed at the observation level).

## Coverage status honesty
- `l0_network: not_measured` (L54-58): consistent — no L0 measurement substrate is cited, scope limited to `beaxy.com`. Honest.
- `l1_consensus: not_applicable` (L59-60): consistent — SEC platform shutdown does not implicate validator/relay behavior.
- `l3_rpc: not_applicable` (L61-62): consistent — Beaxy was a centralized CEX, not a chain RPC target.
- `l4_frontend: measured` (L63-69): the scope is `beaxy.com` and the note is careful: "supports a platform/frontend observed_change at the public trading-platform surface, without claiming ISP blocking." Per §3.5, a `measured` coverage row requires either a `denominator_artifact` or a same-layer observation source with a replayable anchor — the Row-1 source carries `body_hash` + `body_path`, satisfying the anchor requirement. Honest, and the validator confirms this (script run is clean).
- `asset_onchain: not_applicable` (L70-71): consistent — no token-level freeze claim is made (BXY token destruction is noted in the press release wording but is not coded as an asset-onchain row, which is the conservative coding).
- `offramp_cex: measured` (L72-78): scope `beaxy_platform_customer_assets`. Same anchor analysis as L4. Honest.

## Attribution discipline
- **Row 1 (L4) — direct**: source note (L94-96) reproduces the press-release language "settling parties agreed to shut down the Beaxy Platform." Spot-check against the locally captured HTML confirms the phrase "shutting down the Beaxy Platform" is in the SEC source text. The named-link tying the layer effect to the named SEC trigger is explicit in the source — `direct` is justified.
- **Row 2 (offramp_cex) — direct**: source note (L110-114) reproduces "transferring customer assets and funds to each respective customer" plus the cease-and-desist obligations. Spot-check confirms the SEC HTML contains "transferring all customer assets and funds to each respective customer." Named-link present — `direct` is justified.

## Scoped claim
The `scoped_claim` (L121-124) reads: "The 2023-03-29 SEC Beaxy action is coded as a Beaxy Platform shutdown plus cessation/return obligations at the centralized platform layer; it is not coded as network blocking or an on-chain asset freeze." This stays squarely inside what the SEC source language and the two `direct`/`observed_change` rows can support. It does not over-attribute to L0 (network blocking is explicitly disclaimed), does not over-attribute to asset_onchain (asset freeze explicitly disclaimed), and confines the claim to the centralized-platform layers. Attribution-tier and scope are aligned; no over-reach.

## Self-contradiction check
- **Tier vs shape inconsistency (load-bearing)**: `admission_tier: anchor_case` (L8) requires "≥ 2 observed_change layers with attribution ∈ {direct, plausible}" per methodology §3.2. The event has exactly two: L4 and offramp_cex, both `direct`. By the letter of the rule this just barely qualifies. **However**, `empirical_shape: comparison` (L7) is defined as "1 or 2 distinct layers with observed_change," not the `cascade` shape (≥3 layers) that normally carries anchor_case narrative exposition weight per §3.2 ("anchor_case events carry most of the narrative exposition weight" — implicitly via cascade reach). This is *not a hard validator contradiction* but is a soft inconsistency: a 2-layer comparison event being held up as paper-narrative anchor is unusual.
- **Single underlying source for both observation rows**: both `observed_change` rows cite only the SEC press release HTML capture. The trigger has a second primary_legal artifact (the complaint PDF) but neither observation row lists it. This is technically schema-compliant (§5 allows one primary_legal per observation), but for an `anchor_case` it is thin: the same paragraph in the same SEC release supports both rows, so there is no independent cross-substrate confirmation at the observation level.
- **`analysis_notes`** (L116-119): no internal contradictions found; no "null_event rather than null_event"-style typos; the prose is consistent with the coverage and observation rows.
- **`scoped_claim` vs attribution**: no contradiction — `direct` rows support the scoped claim, and the claim correctly avoids L0/asset_onchain over-reach.

## Anchor-tier extra check
Anchor-tier promotion would mean this event becomes paper-narrative spotlighted. The evidence depth has two strengths and two weaknesses. Strengths: every cited URL has a verified local body_hash + body_path artifact (not just measurement_ids or scope_descriptor), and the source text literally contains the verbatim language each observation row quotes — meeting the "body_hash + body_path on critical observations" anchor-tier gate explicitly named in the task. Weaknesses: (a) `empirical_shape: comparison` with only two `observed_change` rows is the minimum for anchor_case and is far thinner than typical anchor events (Tornado Cash, OFAC mixer designations) which carry 3+ observed_change layers with measurable cross-layer timing — this is a single-day, two-layer settlement, not a cascade; (b) both observation rows draw from a single SEC press release paragraph, so the "evidence trail" is one artifact deep at the observation tier, with the complaint PDF acting as trigger redundancy only. **Recommendation**: downgrade `admission_tier` to `empirical_case`. The event is a valid datapoint for aggregate statistics (it is a clean SEC-induced platform shutdown with documented cessation obligations), but it is not strong enough to anchor paper narrative exposition the way `anchor_case` implies. If the maintainer wishes to retain `anchor_case`, then at minimum the complaint PDF source should be replicated at the observation level so each `direct` row has two independent primary_legal artifacts.

## Specific issues blocking admit_now
- `admission_tier: anchor_case` is on the borderline of the methodology §3.2 definition and is not justified by the comparison-shape, single-source-deep evidence trail. This is the primary blocker for `admit_now`.
- Observation rows only cite the SEC press release HTML; the complaint PDF — which is captured locally and listed as a trigger citation — is not echoed at the observation level. For anchor-tier ambition this thins the evidence trail unnecessarily.
- No corroborating supplementary source documents the actual post-shutdown state of `beaxy.com` (e.g., a Wayback snapshot or operator landing-page capture confirming the platform went dark after 2023-03-29). The `measured` status on L4 rests entirely on the SEC's announcement of an undertaking, not on observed frontend state.

## Recommended fixes (if admit_with_minor_fixes)
- Downgrade `admission_tier` from `anchor_case` to `empirical_case` (L8). Comparison-shape with two `direct` observed_change rows mapped to a single SEC press release is a textbook empirical_case datapoint, not a paper-narrative anchor.
- Add the locally captured complaint PDF (`sources/http_captures/sec-beaxy-platform-shutdown-2023/primary/www.sec.gov__files-litigation-complaints-2023-comp-pr2023-64.pdf__34db79071e.bin`, sha256 `e46031492fe74d5513616cbfd9b0a06311a9067d3af69ef11981aeee9eeaed33`) as a second source under both observation rows (L89-96 and L105-114) so each `direct` row has two independent primary_legal artifacts.
- Optional but strengthens the L4 row: add a semi_primary_wayback or supporting_journalism source documenting beaxy.com's actual post-2023-03-29 state (the §3.5 anchor-tier "stronger evidence trail" point). If this is added, anchor_case becomes defensible again.
- Optional: tighten the `scoped_claim` to name "SEC settling-undertakings" explicitly so readers understand the observed change is a regulatory-undertaking-induced shutdown, not an externally measured ISP/protocol effect.
