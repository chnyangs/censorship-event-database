# Null-case audit · sec-v-uniswap-wells-notice-2024 · agent B

## Summary verdict
- **agent_verdict**: `needs_human_review`
- **confidence**: high
- **one-sentence justification**: The trigger is a Wells notice — a pre-enforcement private staff letter, not a final or formal enforcement action — and admitting this as a null-case "trigger we measured and observed no change at L4" risks confusing two distinct null-case interpretations: (a) the Wells notice was a real censorship trigger that produced no L4 effect, vs (b) the Wells notice was never a censorship-pressure event in the first place, so observing "no change" is structurally trivial.

## Trigger
- type / actor / timestamp / precision: `sec_action` / `US_SEC` / `2024-04-10T00:00:00Z` / day
- citation admissibility (primary / semi-primary count): 1 primary_corporate (Uniswap Labs blog post "Fighting for DeFi", body_hash+body_path, **no wayback URL**) + 1 primary_legal (SEC newsroom press-releases index — captured as an **absence-of-notice anchor**, body_hash+body_path, no wayback URL)
- verdict: **concerns** — the primary citation comes from the **regulated entity's own disclosure** (Uniswap Labs blog) of having received a private SEC letter. The SEC has not publicly acknowledged the Wells notice anywhere in the record, by design (Wells notices are private). The "primary_legal" SEC newsroom capture is not a primary citation of the trigger event — it is a primary citation of an absence, which is logically a different artifact. There is no third-party corroboration (e.g., news reporting that the Wells notice existed). Practically, this is the lowest-corroboration trigger in the 13-event null set.

## Scoped claim
- which layers were scoped: `l4_frontend` = `measured` (app.uniswap.org persistent through 2024-04-10 → 2025-02-25); all other layers `not_applicable`
- is the null-case claim properly bounded? **Borderline**. The scoped_claim says "SEC pre-enforcement signals alone — without formal complaint filing — do NOT produce measurable censorship effects at the frontend or off-ramp layers." This is a generalizing claim of a single private-letter datapoint, which steps beyond the corpus-narrow rubric. The phrasing "alone" implies a counterfactual that the corpus does not actually contain (SEC formal complaints against frontend operators are themselves "repair queue" and not admitted in this corpus). The null-case substantively folds in a comparative claim ("lowest-enforcement-intensity SEC event in the dataset") without a defensible denominator.

## Observation anchors
- layer=`l4_frontend` / kind=`observed_no_change` / attribution=`none` / anchors: 1 primary_corporate source (Uniswap Labs blog with body_hash+body_path) + 1 primary_legal source (SEC newsroom index with body_hash+body_path) + structured `scope_descriptor`
- verdict per row: **concerns** — the sources establish an "anchor", but **neither source is a direct measurement of app.uniswap.org**. The validator passes because body_hash+body_path qualifies as a replayable anchor, but neither the Uniswap blog nor the SEC index is itself evidence that app.uniswap.org was operational across the 320-day window. To anchor "frontend remained operational through Wells-notice period" properly, the substrate should be either (a) Wayback snapshots of app.uniswap.org at multiple points in the window, or (b) a hash of an app.uniswap.org capture at start and end of window. The current substrate documents only that Uniswap Labs *said* they would continue operating and that the SEC did not press-release the notice — neither directly substantiates L4 persistence.

## Coverage status honesty
- `l0_network` = not_applicable — defensible
- `l1_consensus` = not_applicable — defensible
- `l3_rpc` = not_applicable — defensible
- `l4_frontend` = **measured** with scope `[app.uniswap.org]` — **concern**: the cited substrate does not include any app.uniswap.org capture. The coverage note says "app.uniswap.org remained operational throughout the Wells-notice period" but this is asserted rather than evidenced. Status should be `partially_measured` at most, or the substrate should include actual app.uniswap.org snapshots.
- `asset_onchain` = not_applicable — defensible
- `offramp_cex` = not_applicable — defensible

## Issues / concerns
- **Wells notice framing**: a Wells notice is staff intent-to-recommend; it is not a final or formal SEC action. Admitting it as a `trigger` with `trigger.type: sec_action` is technically defensible (the staff did take an action — they sent the letter), but the YAML's own framing ("lowest-enforcement-intensity SEC event in the dataset") suggests the authors recognize the borderline.
- **Trigger evidentiary base**: the only direct evidence the trigger event occurred is Uniswap Labs' own disclosure. The SEC has not acknowledged it. The "primary_legal" capture is an absence-of-notice, which is methodologically a different kind of anchor.
- **L4 substrate gap**: the `observed_no_change` claim about app.uniswap.org persistence is anchored to documents that do not themselves measure app.uniswap.org. This is the most concerning anchor in the 13-event set.
- **Comparative claim leakage**: the scoped_claim uses the phrase "lowest-enforcement-intensity SEC crypto event in the dataset" — a denominator claim — without the per-claim phrasing-lock discipline `paper_claims.md` requires. The paper's `paper_claims.md` rubric forbids null-case prose from making implicit-zero corpus-wide claims; "alone — without formal complaint filing — do NOT produce measurable censorship effects" reads as such a generalization.
- **No formal SEC action ever filed**: per the YAML's own note, "SEC formally dropped the matter on 2025-02-25 under the new administration". This makes the "trigger" definitionally a procedural artifact, not a censorship-pressure event. Including it as a denominator in a null-case set conflates "we observed a trigger and no change" with "there was no real trigger".

## Recommendation for human reviewer
This is the case that most clearly merits a human override decision. The user's specific concern is well-founded: a Wells notice is procedural, not a final action, and a Wells notice that was later **withdrawn** (SEC dropped on 2025-02-25) is structurally not a censorship-pressure event whose absence-of-L4-change is informative.

Three plausible resolutions:
1. **Demote to repair-queue / withdraw from null-case set**: the cleanest option. The event becomes a documented "pre-enforcement signal that did not become a trigger" — possibly cataloged in a different stratum entirely.
2. **Keep as null-case but tighten substrate**: replace the trigger primary_corporate source's role with proper app.uniswap.org Wayback snapshots at multiple points in the 320-day window, downgrade `l4_frontend.status` to `partially_measured`, and rewrite the scoped_claim to remove the "alone … do NOT produce" generalization. The "no SEC press release" framing should become a substrate-quality note, not the central anchor.
3. **Keep as null-case but reframe the trigger**: re-cast the trigger as the 2025-02-25 SEC drop (which has cleaner primary documentation), not the 2024-04-10 Uniswap disclosure. This pivots the event from "Wells notice → no effect" to "SEC drops → no effect", which is a different and arguably more defensible null observation.

The user's flag is correct. I recommend the human reviewer take option 1 unless option 2's substrate work is already pinned.
