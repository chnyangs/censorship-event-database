# Inter-Rater Reliability (IRR) — Coder Packet & Worked Example

**Purpose.** This document is the standard-format instruction packet for an
**independent human coder** performing the blinded double-coding pass that gates
the reliability claim in the paper (blocker **H1** in
[`human-audit.md`](human-audit.md)). The corpus's current agreement evidence is an
LLM self-consistency check under blinded re-coding; it supports *self-consistency*
only, **not** independent-human inter-rater reliability. Until an independent human
coder recodes a stratified sample and a standard agreement coefficient clears the
readiness gate, every aggregate in the paper is working-snapshot grade.

> **Who may code.** The coder must be independent: they must **not** have produced
> the gold labels or the agent-assisted recode, and must **not** have seen the
> event YAML, rendered event pages, existing codes, κ reports, or LLM rationale.
> They receive only the blank packet (blind worksheets + this document + the
> codebook + sample metadata). See `human-audit.md` §H1 for the blinding rules.

---

## 1. What you are coding

You independently assign a label to each row of three blind worksheets. Each row is
one **event × layer** cell. You judge it **only** from the evidence context printed
in the row plus the anchored source(s) it cites — never from prior knowledge of how
the cell was originally coded.

The six stack layers are: `l0_network`, `l1_consensus`, `l3_rpc`, `l4_frontend`,
`asset_onchain`, `offramp_cex`.

| Worksheet | Variable | Allowed labels |
| --- | --- | --- |
| `coverage_status_blind.csv` | **coverage_status** | `measured` / `partially_measured` / `not_measured` / `not_applicable` |
| `observation_kind_blind.csv` | **observation_kind** | `observed_change` / `observed_no_change` / `coverage_gap` |
| `attribution_blind.csv` | **attribution** | `direct` / `plausible` / `none` |

The attribution worksheet contains only rows whose observation is `observed_change`
(attribution is undefined otherwise).

---

## 2. Codebook (decision rules)

These summarize `schema/codebook.md` and `docs/decision-rubric.md`. When a row is
genuinely ambiguous, record your reasoning in `recoder_comment` and pick the label
the rules below force — do **not** leave a row blank.

### 2.1 coverage_status — *did we look, and how well?* (kept separate from what we saw)

- **`measured`** — a public, replayable evidence substrate for this layer was
  queried for this event (e.g. an archived capture, an on-chain log, a repo commit,
  an external measurement vantage).
- **`partially_measured`** — a substrate exists but is named, narrow, or
  single-vantage: it supports a claim about the cited subset only, not a
  layer-population claim.
- **`not_measured`** — an **observability gap**: no public substrate was queried.
  This is the label prior cross-layer tabulations silently overwrite with a zero.
  Code it explicitly; it is rendered `---`, never `0`.
- **`not_applicable`** — the layer cannot react to this trigger by construction
  (e.g. an off-ramp action against an asset with no on-chain control surface).
  `not_applicable` is excluded from every denominator; it is **not** a gap.

> Load-bearing distinction: `not_measured` = "we did not look"; `not_applicable` =
> "there was nothing to look at"; an observed negative is neither (see 2.2).

### 2.2 observation_kind — *what did the substrate show?* (only on measured / partial layers)

- **`observed_change`** — a detectable reaction attributable to the trigger.
- **`observed_no_change`** — a **scoped** negative: the substrate was queried and
  showed no reaction for the named target, vantage, and window. Admissible **only**
  if the row carries a replayable anchor (`body_hash` + `body_path`, a `query_hash`,
  or a set of `measurement_ids`). A prose scope description alone is **not** enough —
  treat an anchorless null as `coverage_gap`.
- **`coverage_gap`** — the layer was nominally in scope but the query returned no
  usable substrate (degrades the row toward `not_measured`).

### 2.3 attribution — *how firmly is the change linked to the trigger?* (only on `observed_change`)

`direct` requires **BOTH** of the following (codebook §1.0, 2026-06-02):

- **(A)** the **trigger names the target** (the designation/order/filing identifies
  the specific address, entity, or asset that reacted), **and**
- **(B)** the **operator links its own action to the trigger** (a public statement,
  commit message, or filing citing the designation/order).

Grades:

- **`direct`** — (A) **and** (B) hold. Licenses causal phrasing.
- **`plausible`** — co-occurrence consistent with the trigger but (A) or (B) is
  missing. Licenses consistency / co-occurrence language only, never a causal claim.
  *Examples that stay `plausible`:* an inferred-target freeze backed by an on-chain
  tx but where the trigger never named that address (A fails); generic "we comply
  with sanctions" boilerplate with no tie to this trigger (B fails); a
  third-party-only attribution.
- **`none`** — no defensible link; informs coverage/null accounting but supports no
  attributed claim.

> This (A)+(B) split is the rubric sharpening the project adopted after an earlier
> pass scored attribution κ = 0.58 (moderate) — attribution is the one contested
> variable, so code it strictly to the two tests above.

---

## 3. Procedure

1. **Generate the blank packet:** `make irr-packet`
   (wraps `scripts/build_irr_sample.py`; stratified by `admission_tier` across
   anchor / empirical / null cases). The coder receives only
   `site/h1_irr_packet/` — blank worksheets, this doc, the codebook, and sample
   metadata (`sample_manifest.csv`: `event_id, admission_tier, trigger_type`).
2. **Code each worksheet independently.** Fill `recode_value` for every row; use
   `recoder_comment` for any borderline call. Do not consult the other coder, the
   event YAML, the site, or any existing codes.
3. **Return the filled `*_blind.csv` files.** The gold `*_key.csv` files stay
   sealed until your worksheets are committed.
4. **Compute agreement:** `make irr-kappa`
   (wraps `scripts/compute_irr_kappa.py`; writes
   `analysis/inter_rater/kappa_report.{json,md}`).
5. **Set provenance honestly:** mark `coder_provenance.mode = independent_human`
   **only** if the pass was truly independent and blinded.
6. **Gate:** `python3 scripts/check_paper_readiness.py --strict-reliability`
   must stop failing on coder provenance.

**Acceptance (from `human-audit.md` §H1):**
- `coverage_status` κ ≥ 0.6 (required).
- `observation_kind` and `attribution` κ ≥ 0.6 **or** the related paper claims stay
  explicitly parked / descriptive.

---

## 4. Worked example

Canonical pilot event: **Tornado Cash OFAC SDN designation, 2022-08-08**
(`events/tornado-cash-ofac-2022.yaml`; the six-fate fan-out is Figure 1 of the
paper). The rows and codes below are **illustrative** — they show how the rules in
§2 resolve real cells and how κ is computed. When you actually code, use the codes
you read off the blind worksheet, not these.

### 4.1 coverage_status (6 rows, two independent coders)

| row | layer | evidence context (abridged) | Coder A | Coder B |
| --- | --- | --- | --- | --- |
| tc-01 | l0_network | OONI probe query for in-scope domains/window returned **zero** volunteer probes | `not_measured` | `not_measured` |
| tc-02 | l1_consensus | MEV-Boost relay OFAC-filter share, archived dashboard capture | `measured` | `measured` |
| tc-03 | l3_rpc | Flashbots `rpc-endpoint` blacklist commit (single named provider) | `partially_measured` | `partially_measured` |
| tc-04 | l4_frontend | dApp UI geoblock, Wayback capture of the interface | `measured` | `measured` |
| tc-05 | asset_onchain | Circle USDC `Blacklisted(...)` tx, on-chain log | `measured` | `measured` |
| tc-06 | offramp_cex | exchange delisting notice, archived announcement | `measured` | `measured` |

Observed agreement = 6/6. κ = **1.0** (both coders identical). *This matches the
saturated coverage/observation labels reported in the paper.*

### 4.2 attribution (the contested variable — one realistic disagreement)

Only `observed_change` rows appear here.

| row | layer | (A) trigger names target? | (B) operator linked action? | Coder A | Coder B |
| --- | --- | --- | --- | --- | --- |
| at-01 | l1_consensus | yes (SDN addresses) | yes (relay OFAC-filter policy) | `direct` | `direct` |
| at-02 | l3_rpc | yes | yes (commit references designation) | `direct` | `direct` |
| at-03 | l4_frontend | no (UI blocks region, not the named address) | no | `plausible` | `plausible` |
| at-04 | asset_onchain | **contested**: did the designation name the frozen USDC address? | on-chain tx exists; public tie unclear | `direct` | `plausible` |
| at-05 | offramp_cex (exch. X) | yes | yes (delisting cites sanctions) | `direct` | `direct` |
| at-06 | offramp_cex (exch. Y) | no (policy-wide, not this trigger) | no | `plausible` | `plausible` |

Row **at-04** is the instructive disagreement: an on-chain freeze tx exists (part of
(B)), but whether the OFAC action **named** the frozen address (test A) is arguable.
Under §2.3, if A is not clearly satisfied the row stays `plausible` — so Coder B
applied the rubric more strictly. This is exactly the kind of call the (A)+(B) split
is meant to standardize.

**Cohen's κ on this 6-row set:**
- Observed agreement p_o = 5/6 = 0.833.
- Label marginals — Coder A: `direct`×4, `plausible`×2; Coder B: `direct`×3,
  `plausible`×3.
- Chance agreement p_e = (4/6)(3/6) + (2/6)(3/6) = 0.333 + 0.167 = **0.5**.
- κ = (p_o − p_e) / (1 − p_e) = (0.833 − 0.5) / (1 − 0.5) = **0.667**.

κ = 0.667 ≥ 0.6 → passes the gate on this illustrative set. The real pass runs the
full stratified sample (the paper enlarges the attribution blind sample to 157
observations because at small n the bootstrap 95% CI on κ spans [0.0, 1.0]) and
reports κ **with a seeded bootstrap 95% CI**, not a bare point estimate.

---

## 5. Blank coding-sheet template

Coders fill `recode_value` (and optionally `recoder_comment`); leave every other
column as generated. Columns match `scripts/build_irr_sample.py` exactly.

**coverage_status_blind.csv**

```csv
row_id,event_id,layer,coverage_note,event_notes,recode_value,recoder_comment
cov-0001,<event-id>,l0_network,<evidence context for this cell>,<event-level note>,,
```

**observation_kind_blind.csv**

```csv
row_id,event_id,layer,observation_note,source_hint,recode_value,recoder_comment
obs-0001,<event-id>,l4_frontend,<what the substrate showed>,<up to 3 anchored sources>,,
```

**attribution_blind.csv** (observed_change rows only)

```csv
row_id,event_id,layer,observation_note,recode_value,recoder_comment
att-0001,<event-id>,asset_onchain,<change + how it relates to the trigger>,,
```

---

## 6. How agreement is scored

- **Metric:** Cohen's κ for a two-coder pass (`scripts/_kappa_ci.py::cohen_kappa_value`);
  Fleiss' κ if more than two coders. Each κ is reported with a **seeded bootstrap
  95% CI** so a small-n estimate cannot masquerade as precise.
- **Per variable:** κ is computed separately for `coverage_status`,
  `observation_kind`, and `attribution` by joining each `*_blind.csv` to its sealed
  `*_key.csv` on `row_id`.
- **Readiness threshold:** κ ≥ 0.6 (`scripts/compute_irr_kappa.py::_interpret`).
- **If a variable lands below 0.6:** do not inflate it. Either widen the sample and
  re-run, or the paper keeps that variable's claims explicitly parked/descriptive
  (the attribution point-estimate CI at present already straddles 0.6, so this is a
  live possibility — a codebook/power problem, not only a sample-size one).

---

## 7. References

- Blocker & blinding rules: [`human-audit.md`](human-audit.md) §H1
- Full coding rules: [`schema/codebook.md`](schema/codebook.md),
  [`docs/decision-rubric.md`](docs/decision-rubric.md)
- Sampler: [`scripts/build_irr_sample.py`](scripts/build_irr_sample.py)
- κ + bootstrap CI: [`scripts/compute_irr_kappa.py`](scripts/compute_irr_kappa.py),
  [`scripts/_kappa_ci.py`](scripts/_kappa_ci.py)
- Methodology walkthrough for building an event:
  [`6a1d66df502cdc827ad0999d/supplementary/example-tornado-cash-2022.md`](6a1d66df502cdc827ad0999d/supplementary/example-tornado-cash-2022.md)
