# Publication-Quality Review - 2026-04-24

Scope: current repository state after regenerating `status`, `review`,
`staleness`, `dataset`, and `derived` artifacts on 2026-04-24. This review
answers one question: what would make the current 53-case dataset defensible as
an open dataset plus paper artifact?

## Bottom line

The repo is structurally strong enough to release as a curated dataset
framework: 53/53 events validate, 53/53 are admitted, 53/53 have scoped release
claims, and there are no draft gap markers.

It is not yet strong enough to claim broad hour-precision measurement of
cross-layer censorship cascades. The defensible paper framing is narrower:
an evidence-chained event catalog, schema, admission protocol, and descriptive
taxonomy showing that most public reactions are single-layer or null, while
full cascades are rare and concentrated in a small number of anchor cases.

## Automated review results

Commands run:

```sh
make check
make regenerate
make validate-archives TIMEOUT=5
git diff --check
```

Results:

- `make check` passes: schema / field consistency / draft-gap / status /
  review reports are clean.
- `make regenerate` rebuilt the current dataset, static site, review, staleness, and derived
  artifacts: 53 events, dataset v0.1.0, cutoff 2026-04-22.
- `make validate-archives TIMEOUT=5` now passes. Wayback reachability failures
  remain as warnings only when a local `body_hash + body_path` replay artifact
  has already verified.
- `git diff --check` passes after normalizing generated CSV line endings and
  removing Markdown trailing-space line breaks from the staleness report.

Blocking archive cases: none.

## 53-case corpus shape

| Dimension | Counts |
| --- | --- |
| Status | 53 admitted |
| Strata | S1 OFAC SDN 26; S3 DOJ/SEC/CFTC/FIOD 12; S4 nation-state 6; S5 corporate 6; S6 supranational 2; S2 OFAC removal 1 |
| Empirical shape | 38 comparison; 13 null_event; 2 cascade |
| Admission tier | 35 empirical_case; 13 null_case; 5 anchor_case |
| Target enumeration | 29 complete; 24 subset |
| Trigger precision | 48 day; 3 minute; 1 second; 1 hour |
| Human audit | 5 present; 48 missing; only 2/5 anchor cases have human-audit dates |
| Scoped claims | 53 present |
| Scoped knowledge notes | 5 present; all 5 anchor cases covered |

Changed-layer distribution:

| Distinct changed layers | Count | Role |
| ---: | ---: | --- |
| 0 | 13 | null controls / catalog completeness |
| 1 | 35 | empirical single-layer datapoints |
| 2 | 3 | comparison cases with multi-layer evidence |
| 3 | 1 | cascade anchor |
| 4 | 1 | cascade anchor |

Archetype distribution from `derived/archetype_distribution.md`:

| Archetype | Count |
| --- | ---: |
| `asset_only` | 13 |
| `frontend_only` | 8 |
| `cex_only` | 14 |
| `multi_layer` | 5 |
| `null_event` | 13 |
| `other_single_layer` | 0 |

## Layer observability

| Layer | Current signal |
| --- | --- |
| L0 network | 22 `not_measured`, 31 `not_applicable`, 0 observations |
| L1 consensus | 6 `measured`, 1 `partially_measured`, 45 `not_applicable`, 2 observed changes |
| L3 RPC | 8 `partially_measured`, 45 `not_applicable`, 0 observed changes |
| L4 frontend | 16 `measured`, 3 `partially_measured`, 8 `not_measured`, 26 `not_applicable`, 13 observed changes |
| Asset on-chain | 17 `measured`, 6 `not_measured`, 30 `not_applicable`, 21 observed changes |
| Off-ramp CEX | 25 `measured`, 1 `partially_measured`, 21 `not_measured`, 6 `not_applicable`, 17 observed changes |

Interpretation: the repo is currently a six-layer accounting framework, not a
six-layer uniformly measured panel. The strongest measured surfaces are asset
freezes, CEX/off-ramp actions, and frontend changes. L0 and L3 are mostly
explicit absence-of-measurement surfaces.

## Main quality risks

1. **Archive replay blockers were removed.** The previous 14 Wayback-only
   sources across nine events have either been replaced with local
   `body_hash + body_path` artifacts or removed where they were redundant
   supporting sources. `validate-archives` now has zero blocking errors.

2. **The README/paper thesis overstates timestamp precision.** The dataset
   currently has 48 day-precision triggers. Either upgrade the trigger timing
   for paper-critical cases or reframe the claim as precision-aware timelines,
   with hour-level precision only where sources support it.

3. **The corpus supports "cascade rarity" better than "cascade prevalence."**
   Only 2/53 events meet the schema-level `cascade` definition. That is not a
   weakness if the paper frames it as a finding: public evidence of full
   cross-layer cascade is rare; most reactions are single-layer or null.

4. **Adversarial audit coverage is too low for paper submission.** Only 5/53
   cases have `last_human_audit`. The current staleness report correctly flags
   48 cases as never adversarially audited.

5. **Target enumeration is mixed.** Twenty-four events use
   `target.enumeration: subset`; aggregate claims must stratify complete vs
   subset targets, especially when computing response rates.

6. **Coverage completeness is mostly scoped.** `review_report.py` finds 19
   low-coverage and 12 medium-coverage cases. This is compatible with a
   scoped dataset release, but the paper must use denominator-honest tables
   rather than imply every layer was measured for every event.

7. **Case knowledge is normalized for anchor cases, not all exemplars.** Every
   case has a `scoped_claim`, and all five anchor cases now have
   `scoped_knowledge`. Non-anchor paper exemplars may still need the same
   treatment if they move from aggregate datapoints into narrative figures.

## Recommended solution

### P0 - Make the dataset release replayable

Goal: `make validate-archives TIMEOUT=5` has zero errors. Warnings are allowed
only for redundant Wayback URLs when the local body hash already verifies.

Status: complete for the 2026-04-24 pass.

Actions completed:

- Removed redundant Wayback-only supporting sources where a primary source
  already satisfied the observation.
- Added local capture metadata for the retained Uniswap token-list source.
- Re-ran `make validate-archives TIMEOUT=5`; the target now passes.

### P1 - Split public-release roles

Add an explicit paper-use convention, either as a derived artifact or a field in
the review report:

| Role | Meaning | Current candidates |
| --- | --- | --- |
| `paper_anchor` | Detailed narrative exemplar | 5 anchor cases |
| `aggregate_datapoint` | Included in descriptive statistics | 35 empirical cases |
| `null_control` | Included as no-change controls | 13 null cases |
| `appendix_only` | Public catalog, not used in main paper claims | cases with unresolved archive/audit/coverage risk |

This avoids treating all 53 admitted cases as equally strong evidence in the
paper.

### P1 - Align claims with precision

Replace any broad "hour-precision for every event" claim with:

"The dataset stores precision-aware UTC timestamps; observations are recorded
at the strongest precision supported by their source, from second-level
on-chain events to day-level legal triggers."

For the paper core, require:

- trigger precision `hour` or better for cascade timing claims, or
- an explicit uncertainty treatment for `day` precision triggers.

### P1 - Audit the paper-critical subset first

Do not try to audit all 53 before writing. Audit in this order:

1. The five `anchor_case` rows.
2. Any row with archive warnings that becomes paper-critical.
3. The 13 `null_case` rows, because null claims are easy to overstate.
4. Any case used as a figure/table exemplar.

After each audit, set `last_human_audit` only if the exact source passages and
body hashes were checked.

### P2 - Improve layer coverage where it changes the story

Highest return targets:

- L0: either ingest Censored Planet for a small number of high-value domains,
  or explicitly label L0 as future work in the paper.
- L3: convert current provider-substrate notes into event-specific
  pre/post snapshots for Tornado, Cryptex, Semenov, Funnull, and delisting
  cases.
- Off-ramp: for CEX-only cases, add API or platform-state snapshots where
  available so the layer is not purely announcement-driven.

Do not chase uniform six-layer completeness for all 53; it is too expensive and
would not change the core result.

### P2 - Normalize case interpretation

Add `scoped_knowledge` to at least the anchor cases and the paper exemplars.
Use a fixed mini-template:

- What changed?
- Which layers did not change or could not be measured?
- Why attribution is direct/plausible/none.
- What this case teaches relative to the nearest comparable cases.

Status: complete for the five anchor cases; still optional for non-anchor
figure/table exemplars selected during writing.

## Paper framing

Defensible title-level claim:

"A precision-aware, evidence-chained dataset and schema for studying
cross-layer crypto censorship events."

Defensible empirical claims:

- Publicly observable reactions concentrate in asset, off-ramp, and frontend
  layers.
- Full 3+ layer cascades are rare in the current corpus: 2/53.
- Null cases are common and methodologically important: 13/53.
- Stablecoin issuer reactions are the cleanest high-integrity timing surface
  because on-chain receipts are independently replayable.
- Frontend/protocol decoupling is central: several cases change at L4 without
  an equivalent protocol-layer change.

Claims to avoid until more work is done:

- "All major events" unless the sampling frame is explicitly bounded.
- "Hour precision" as a blanket property.
- Probability / prediction claims by trigger type.
- Cross-layer causal language for observations marked `plausible`.
- L0/L3 prevalence claims, because those layers are not uniformly measured.

## Immediate next checklist

- [x] Localize or remove the 14 Wayback-only sources and rerun `make validate-archives`.
- [x] Reword README / abstract claims from blanket hour precision to
      precision-aware timestamps.
- [x] Add paper-use roles to `review_report.py` or a new derived artifact.
- [ ] Audit the five anchor cases. There are no archive-blocked cases left, but
      `last_human_audit` still requires human sign-off.
- [x] Add `scoped_knowledge` to the anchor cases.
- [ ] Draft the paper around "framework + evidence catalog + descriptive
      taxonomy", with aggregate tables generated from `derived/`.
