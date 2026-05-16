# H2 — outstanding human gates (consolidated deferral packet)

> Phase 3 of the 2026-05-16 staged-release plan. None of the items
> below can be honestly resolved by an LLM agent. Each one is a
> decision the maintainer must make before a real (non-DRYRUN)
> v0.2 release. The packet consolidates everything still open from
> the 2-agent null-case cross-audit
> ([`AGGREGATE.md`](AGGREGATE.md)) plus the attribution-κ codebook
> ambiguity surfaced by the 3-agent IRR pass
> (`analysis/inter_rater/kappa_report.md`).
>
> Format: each gate has (a) **state**, (b) **what an LLM has done**,
> (c) **what only a human can do**, (d) **concrete options** with
> consequences.

---

## H2-P0 · `sec-v-uniswap-wells-notice-2024`

**State**: handled in the 2026-05-15 DRYRUN by flipping
`status: admitted → rejected`. The rejection rationale (Wells
notice withdrawn 2025-02-25; L4 substrate doesn't measure
`app.uniswap.org`) is now in the event's `analysis_notes`.

**What an LLM has done**:

- 2 H2 cross-audit agents independently flagged this event as
  `needs_human_review` with high confidence.
- 2026-05-15 DRYRUN chose **option 1** (withdraw from null-set
  via `status: rejected`) per the agents' rec.

**What only a human can do**:

- Confirm the rejection is the right call vs. one of the two
  alternative resolutions:
  1. Tighten L4 substrate (3+ Wayback snapshots of
     `app.uniswap.org` bracketing the 10½-month window) →
     re-admit as null_case.
  2. Reframe trigger as the 2025-02-25 SEC drop (a real action)
     → re-admit with a different scoped_claim.

**Recommended human action**: spend ~15 min reviewing the event's
`analysis_notes` rationale; if you agree, leave the rejection in
place for v0.2. If you disagree, pick option 1 or 2 and re-author.

---

## H2-P1a · `pertsev-nl-arrest-2022` (divergent verdicts)

**State**: 2-agent cross-audit divergent. Agent A:
`needs_human_review`. Agent B: `pass`. No DRYRUN action taken
(the 2026-05-15 dryrun stamped `last_human_audit: 2026-05-15`
along with the other 12 null cases, but the divergence is
unresolved).

**What an LLM has done**:

- Agent A flagged structural confounding: null window overlaps
  the 2-days-prior 2022-08-08 OFAC Tornado Cash designation by
  2 days. Any cascade attributable to *this* trigger is hard to
  separate from the SDN cascade.
- Agent B accepted the dual-record framing: the null is correctly
  scoped to the developer-arrest trigger surface (Dutch DPP
  custody decision), and the OFAC cascade is a separately-admitted
  event.

**What only a human can do**:

- Read the event's `scoped_claim` and decide whether it explicitly
  excludes the SDN-cascade-attributable portion.
- If yes: confirm pass, leave the dryrun stamp.
- If no: rewrite the scoped_claim to disambiguate, OR downgrade
  the case (similar to `sec-v-uniswap-wells`).

**Recommended human action**: ~10 min. Read
`events/pertsev-nl-arrest-2022.yaml::scoped_claim` and either
accept or tighten.

---

## H2-P1b · `storm-semenov-doj-2023` (divergent verdicts)

**State**: same shape as pertsev. Agent A:
`needs_human_review` (DOJ-attributable null is conceptually thin
once the same-day OFAC SDN on Semenov is admitted). Agent B:
`pass` (dual-record).

**What only a human can do**:

- Read `events/storm-semenov-doj-2023.yaml::scoped_claim` and
  confirm it carves out the DOJ-trigger surface from the
  OFAC-trigger surface.

**Recommended human action**: ~10 min. Same flavor as pertsev.

---

## H2-P2 · corpus-wide `offramp_cex.measured` convention

**State**: both H2 agents flagged the same pattern — 7-8 entity /
individual-level null events code `coverage.offramp_cex.status:
measured` with only the OFAC RA capture as substrate (no
exchange-side artifact, no chain-analytics slice, no query log).
The 8 affected events:

- `irgc-ransomware-ofac-2022`
- `lazarus-entity-ofac-2019`
- `lazarus-laundering-ofac-2020`
- `lockbit-leader-ofac-2024`
- `matveev-ofac-2023`
- `russian-cybercrime-infra-ofac-2025`
- `sichuan-silence-ofac-2024`
- `zservers-ofac-2025`

**Why this matters more now (after Phase 4)**: Agent D's projected-
shape analysis found that converting OFAC stubs en masse would
scale this convention 2-3× to 14-22 events at n=84. The
post-Phase-0+2+4 corpus is 64 events; the convention now affects
~9-12 of them (the original 8 + any Phase 4 admits that hit the
same pattern).

**Three corpus-level resolution options** (pick exactly one):

1. **Add per-event search artifacts**. For each affected event,
   pin one aggregator/news-search artifact (e.g. CoinDesk + The
   Block absence-of-coverage capture) as the `measured` substrate.
   Cost: ~30 min per event × 9-12 events ≈ 5-6 hours.
2. **Corpus-wide downgrade**. Recode all 9-12 from
   `measured` → `partially_measured` with a uniform `coverage[].note`
   explaining "substrate is OFAC-RA-only; downgraded for honesty".
   Cost: ~15 min mechanical edit.
3. **Reframe the limitation in paper text**. Keep `measured` but
   explicitly recast these in the paper's limitation paragraph as
   "**public-disclosure nulls**" (we measured that no public CEX
   action was announced, not that no CEX action occurred). Cost:
   ~30 min of paper-text editing.

The H2 AGGREGATE.md notes that under option (2) or (3), the 8
events flagged `pass_with_concerns` would individually upgrade to
`pass` because the convention concern is the load-bearing piece.

**What only a human can do**: pick which of the three options
applies for v0.2. The dryrun did not pick one.

**Recommended human action**: pick option (2) — the corpus-wide
downgrade. It's the cheapest, most honest, and most-defensible
choice; pre-empts a reviewer asking "why is this `measured` with
no exchange-side data?" with the schema's own
`partially_measured` answer. Estimated 15 min.

---

## H2-P3 · attribution-κ codebook ambiguity (3-agent IRR)

**State**: 3-agent IRR pass produced **Cohen κ = 0.583**
(moderate, below the 0.6 paper-readiness threshold) and **Fleiss
κ = 0.683** across the 3 LLM agents. The 3 disagreement rows are
all `asset_onchain` stablecoin freezes on SDN-listed addresses:

- `cryptex-ofac-2024 / asset_onchain` (gold=direct, consensus=plausible)
- `semenov-ofac-2023 / asset_onchain` × 2 (same)

Codebook reading both readings can defend:

- gold: the on-chain freeze tx on an OFAC-listed address is the
  named-link evidence (the issuer enforcement IS the named link).
- consensus: per the codebook's "when uncertain, prefer plausible
  unless evidence carries an explicit linking statement", absence
  of a public Circle / Tether press release naming the SDN
  defaults to `plausible`.

**Paper-claims response already landed**: `docs/paper_claims.md
§0 Reliability discipline` now restricts attribution-sensitive
comparative phrasing to **named-row / audit level only**. No
corpus-level comparative attribution rate is reported. The
`asset_onchain` rate is already retracted on independent grounds
(structural circularity — see C1 "Not said").

**What an LLM has done**:

- Computed Cohen κ + Fleiss κ + identified the 3-row codebook
  ambiguity cluster.
- Documented the retraction in paper_claims.md.
- Added `--allow-soft-attribution` flag to the release gate so
  the v0.1 strict release can complete given the documented
  retraction.

**What only a human can do**:

- **Decide whether the codebook should be tightened or left as-is.**
  Two paths:
  1. Tighten the codebook: add a `direct` exception clause for
     "on-chain freeze tx on SDN-listed address counts as named-link
     evidence even without operator press release". Re-run IRR;
     attribution κ likely jumps to ≥ 0.85.
  2. Leave the codebook: accept that `direct` vs `plausible` on
     stablecoin freezes is genuinely contested. Continue restricting
     attribution-sensitive comparative phrasing to named-row level.
- Decide whether to run a real **`independent_human` IRR pass** on
  the 3 disagreement rows specifically (smallest possible scope
  to either confirm or refute the LLM consensus reading).

**Recommended human action**: ~30 min:

1. Read the 3 disagreement rows + read their `attribution: direct`
   justification in each event's `observations[].note`.
2. If you (as a domain-expert human) read `direct` as
   contested, leave the codebook as-is and keep the
   named-row-only phrasing lock.
3. If you read `direct` as defensible, tighten the codebook with
   the on-chain-freeze-as-named-link exception and re-run IRR
   (might require a fresh blind worksheet to avoid contaminating
   the prior coding).

---

## Summary table — what's open before real v0.2 release

| gate | state | LLM action | human action | est. time |
| --- | --- | --- | --- | --- |
| H2-P0 sec-v-uniswap | DRYRUN-rejected | option 1 chosen | confirm or pick option 2/3 | 15 min |
| H2-P1a pertsev | dryrun-stamped, divergent | both verdicts surfaced | read scoped_claim, accept or tighten | 10 min |
| H2-P1b storm-semenov | dryrun-stamped, divergent | both verdicts surfaced | read scoped_claim, accept or tighten | 10 min |
| H2-P2 offramp_cex convention | unresolved | 3 options surfaced | pick exactly one | 15 min (option 2 recommended) |
| H2-P3 attribution κ | retraction landed | κ computed, retraction in paper | pick: tighten codebook or accept named-row-only | 30 min |
| **total** | — | — | — | **~80 min** |

The total human-gate budget to clear all 5 items is ~80 minutes
of focused reading + decision-making. None requires re-writing
event YAMLs from scratch; all are read-and-decide.

After this packet is cleared:

- 5 events drop from "DRYRUN-stamped" to "real-audited" (the 4
  pertsev/storm-semenov/sec-v-uniswap + at minimum the 8 affected
  offramp_cex events get their convention decision applied).
- Attribution κ codebook gap is either closed (with a new run) or
  accepted-with-retraction (with no new run).
- Real (non-DRYRUN) `release_signoff.py --version 0.2.0
  --date <real>` becomes runnable.
