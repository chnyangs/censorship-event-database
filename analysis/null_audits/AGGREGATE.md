# Null-case cross-audit aggregate

> 2-agent independent audit of the 13 paper-critical `null_case`
> events still lacking `last_human_audit`. Neither agent stamped
> `last_human_audit` — that remains a strictly human decision.
> This aggregate diffs the two verdicts and surfaces the cases the
> human reviewer must adjudicate first.

Source artifacts:

- [`agent_a/`](agent_a/) — per-event reports + INDEX.
- [`agent_b/`](agent_b/) — per-event reports + INDEX.
- Codebook reference: [`scripts/build_audit_worksheet.py`](../../scripts/build_audit_worksheet.py) + anchor worksheets at [`analysis/audit_worksheets/`](../audit_worksheets/).

## Verdict diff

| event | agent A | agent B | converge? | priority |
| --- | --- | --- | --- | --- |
| `sec-v-uniswap-wells-notice-2024` | **needs_human_review** (high conf) | **needs_human_review** (high conf) | ✓ both flag | **P0** |
| `sinbad-ofac-2023` | pass (high) | pass (high) | ✓ both pass | sign-off ready |
| `iran-ransomware-ofac-2018` | pass_with_concerns | pass | partial | P2 |
| `irgc-ransomware-ofac-2022` | pass_with_concerns | pass_with_concerns | ✓ | P2 (corpus-conv) |
| `lazarus-entity-ofac-2019` | pass_with_concerns | pass_with_concerns | ✓ | P2 (corpus-conv) |
| `lazarus-laundering-ofac-2020` | pass_with_concerns | pass_with_concerns | ✓ | P1 (textual self-contradiction) |
| `lockbit-leader-ofac-2024` | pass_with_concerns | pass_with_concerns | ✓ | P2 (corpus-conv) |
| `matveev-ofac-2023` | pass_with_concerns | pass_with_concerns | ✓ | P2 (corpus-conv) |
| `russian-cybercrime-infra-ofac-2025` | pass_with_concerns | pass_with_concerns | ✓ | P2 (corpus-conv) |
| `sichuan-silence-ofac-2024` | pass_with_concerns | pass_with_concerns | ✓ | P2 (corpus-conv) |
| `zservers-ofac-2025` | pass_with_concerns | pass_with_concerns | ✓ | P2 (L0 substrate absent) |
| `pertsev-nl-arrest-2022` | needs_human_review | pass | **diverge** | P1 (window confounding) |
| `storm-semenov-doj-2023` | needs_human_review | pass | **diverge** | P1 (window confounding) |

**Convergence count**: 11 / 13 verdicts match at bucket level
(85% agreement; equivalent to observed agreement, not κ since the
buckets are ordinal).

## P0 — sign-off blocker (both agents agree)

### `sec-v-uniswap-wells-notice-2024`

- **Both agents** mark `needs_human_review` with high confidence.
- **Root issue**: the Wells notice is a procedural pre-enforcement
  staff letter that was later **withdrawn 2025-02-25** without a
  formal SEC complaint ever being filed. Treating it as a
  `null_case` trigger is harder to defend than the agents found in
  any other event.
- **Substrate gap**: the L4 anchor is the Uniswap blog post + an
  SEC newsroom index of "no formal action notice exists" — not a
  direct measurement of `app.uniswap.org` persistence over the
  10½-month window.
- **Three resolution options** (proposed in both agents' per-event
  reports):
  1. **Withdraw from the null-set** — drop the case to `excluded`
     and document why a withdrawn Wells notice is not a comparable
     enforcement trigger.
  2. **Tighten the L4 substrate** — capture 3+ Wayback snapshots of
     `app.uniswap.org` across the window (e.g. 2024-04, 2024-08,
     2025-02) before and after the withdrawal, anchor them with
     `body_hash`+`body_path`, then re-audit.
  3. **Reframe the trigger** — make the trigger the 2025-02-25 SEC
     drop (a real action), not the 2024 Wells notice (a procedural
     letter), and re-scope the null window accordingly.
- **Until the human picks one of these**, the case should not be
  stamped `last_human_audit` and remains in the paper-readiness
  WARN list.

## P1 — divergent verdicts (human adjudicates)

### `pertsev-nl-arrest-2022` (A: needs_human_review · B: pass)

- **Why agents diverge**: the null window overlaps the 2022-08-08
  OFAC Tornado Cash designation by 2 days. Agent A reads this as
  "structurally confounded — any cascade attributable to *this*
  trigger is hard to separate from the SDN cascade"; agent B reads
  it as "the null is correctly scoped to the developer-arrest
  trigger surface (Dutch DPP custody decision), and the OFAC
  cascade is a separately-admitted event".
- **Human adjudication needed**: is the `analysis_notes` framing
  of "incremental cascade attributable to the arrest itself,
  beyond the SDN cascade already underway" defensible?
- **Recommended human action**: review the scoped_claim language;
  if it does NOT explicitly exclude the SDN-cascade-attributable
  portion, tighten or downgrade the case.

### `storm-semenov-doj-2023` (A: needs_human_review · B: pass)

- **Why agents diverge**: same structural concern. The DOJ
  indictment was filed the same day as the OFAC SDN designation
  on Semenov; Circle's 24h batch-freeze response is already
  attributed in the SDN event. Agent A flags "DOJ-attributable
  null is conceptually thin once the SDN event is admitted";
  agent B accepts the dual-record framing.
- **Human adjudication needed**: same flavor as pertsev — does
  the scoped_claim explicitly carve out the DOJ-trigger surface
  from the OFAC-trigger surface, or is the null over-attributing?

### `lazarus-laundering-ofac-2020` (both pass_with_concerns, P1 priority)

- **Both agents** flag a self-contradictory phrase in
  `analysis_notes`: *"null_event rather than null_event"*. Clean
  textual fix before sign-off.

## P2 — corpus-wide convention question (both agents flag the same pattern)

**7 of 13 individual/entity-level null events** mark
`coverage.offramp_cex.status: measured` while the only attached
substrate is the OFAC RA capture (no exchange-side artifact, no
chain-analytics slice, no query log). The 7:

- `irgc-ransomware-ofac-2022`
- `lazarus-entity-ofac-2019`
- `lazarus-laundering-ofac-2020`
- `lockbit-leader-ofac-2024`
- `matveev-ofac-2023`
- `russian-cybercrime-infra-ofac-2025`
- `sichuan-silence-ofac-2024`
- `zservers-ofac-2025` (a 7+1 = 8 by agent A's count; counting
  conventions vary by which "individual/entity" boundary you take)

**Three corpus-level resolutions** (pick one before stamping):

1. **Add per-event search artifacts** — for each, pin one
   aggregator/news-search artifact (e.g. CoinDesk + The Block
   absence-of-coverage capture) as the `measured` substrate.
2. **Corpus-wide downgrade** — recode all 7-8 from `measured` to
   `partially_measured` with a uniform note explaining the
   substrate is OFAC-RA-only.
3. **Reframe the limitation** — keep `measured` but explicitly
   recast these in the paper's limitation text as "**public-
   disclosure nulls**" (we measured that no public CEX action was
   announced, not that no CEX action occurred).

Whichever option is taken, **`agent_a/INDEX.md` notes the 8 cases
flagged `pass_with_concerns` would individually upgrade to `pass`
if a consistent convention is applied**.

## P2 — minor textual / archival-hygiene issues (quick fixes)

Per agent B's per-event reports:

- `lazarus-entity-ofac-2019`, `pertsev-nl-arrest-2022`,
  `storm-semenov-doj-2023`: trigger citations missing `wayback`
  URL. (Run `make verify-citations` to confirm; archive if not.)
- `lazarus-laundering-ofac-2020`: `analysis_notes` has the
  contradictory phrase `"null_event rather than null_event"`. Fix
  to a coherent sentence.
- `lockbit-leader-ofac-2024`: `coverage.offramp_cex` lacks any
  `note` field explaining the chosen status.
- `zservers-ofac-2025`: `l0_network = not_measured` lacks any
  substrate; sibling `sinbad-ofac-2023` sets the bar with an
  attested OONI-negative query. Either add an L0 substrate or
  document why none exists.

## P2 — cohort-as-name vs cohort-as-address-set (agent A only)

4 events code `addresses_cohort` labels that are entity/individual
names rather than enumerated addresses: `lazarus-entity-ofac-2019`,
`matveev-ofac-2023`, `sichuan-silence-ofac-2024`, and arguably the
entity side of `storm-semenov-doj-2023`. The "absence search"
reduces to entity-name-mention, which is thinner than an
address-cohort search. Not a sign-off blocker by itself; a v0.2
codebook refinement candidate.

## Sign-off ready (both agents pass with high confidence)

- `sinbad-ofac-2023` — exemplary null event. Two Wayback bracket
  captures anchor `sinbad.io` persistence; honest L0 OONI-negative
  documentation; paper-worthy contrast to Tornado 2022. **Ready to
  stamp `last_human_audit` after the human spot-checks the body_hash
  pair.**

## Methodology and limits of this audit

- **Neither agent modified any `events/*.yaml` file.** The
  agents produced per-event reports only.
- **No `last_human_audit` was stamped anywhere by the agents.**
  That remains strictly human.
- **Both agents are LLMs.** They share training-distribution
  biases. Convergence between them is not equivalent to an
  independent human pass. Treat the convergent verdicts (11/13)
  as *agent-pre-screening*: rows where two independent LLM reads
  agree are lower-priority for human re-audit; rows where they
  diverge are higher-priority.
- **The human pass is still needed** to:
  - resolve `sec-v-uniswap-wells-notice-2024` (P0);
  - adjudicate the 2 divergent verdicts (pertsev, storm-semenov);
  - pick a corpus-wide resolution for the offramp_cex convention;
  - stamp `last_human_audit` on the cases the human re-verifies.
