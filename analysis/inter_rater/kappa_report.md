# Inter-rater reliability report

Generated: `2026-05-06T10:26:42Z` · computer `scripts/compute_irr_kappa.py` · blind/key inputs from `analysis/inter_rater/`.

## Coder provenance

- **Mode**: `llm_assisted_blinded` (one of `independent_human`, `llm_assisted_blinded`, `author_self_recode_60d_gap`, `unspecified` — published κ requires non-`unspecified` provenance).
- **Coder**: `GPT-5 worker round 3`
- **Prompt / rubric version**: `2026-05-06 admitted-only repair`
- **Notes**: Blind recode after admitted-only paper surface, SEC pair demotion, L3 rate suppression, validator/source-rule tightening. Coder reported not reading key CSVs or prior kappa reports.

| variable | n coded / n total | observed agreement | Cohen's κ | label |
| --- | --- | --- | --- | --- |
| `coverage_status` | 90 / 90 | 1.0 | 1.0 | almost perfect |
| `observation_kind` | 25 / 25 | 1.0 | 1.0 | almost perfect |
| `attribution` | 20 / 20 | 1.0 | 1.0 | almost perfect |

## `coverage_status` detail

- n_coded: **90** of 90 rows (remaining rows are missing `recode_value` — coder-incomplete)
- observed agreement p_o = 1.0
- expected agreement p_e = 0.44
- Cohen's κ = **1.0** (almost perfect)

### Confusion matrix

| recode \ original | measured | not_applicable | not_measured | partially_measured |
| --- | --- | --- | --- | --- |
| **measured** | 19 | 0 | 0 | 0 |
| **not_applicable** | 0 | 55 | 0 | 0 |
| **not_measured** | 0 | 0 | 13 | 0 |
| **partially_measured** | 0 | 0 | 0 | 3 |

## `observation_kind` detail

- n_coded: **25** of 25 rows (remaining rows are missing `recode_value` — coder-incomplete)
- observed agreement p_o = 1.0
- expected agreement p_e = 0.68
- Cohen's κ = **1.0** (almost perfect)

### Confusion matrix

| recode \ original | observed_change | observed_no_change |
| --- | --- | --- |
| **observed_change** | 20 | 0 |
| **observed_no_change** | 0 | 5 |

## `attribution` detail

- n_coded: **20** of 20 rows (remaining rows are missing `recode_value` — coder-incomplete)
- observed agreement p_o = 1.0
- expected agreement p_e = 0.745
- Cohen's κ = **1.0** (almost perfect)

### Confusion matrix

| recode \ original | direct | plausible |
| --- | --- | --- |
| **direct** | 17 | 0 |
| **plausible** | 0 | 3 |

## Interpretation

Cohen's κ thresholds (Landis & Koch 1977 — still the most cited convention despite known limitations with skewed marginals): < 0.2 slight, 0.2–0.4 fair, 0.4–0.6 moderate, 0.6–0.8 substantial, > 0.8 almost perfect on the Landis & Koch scale.

**What this κ does and does not establish — read before citing.** Under the Landis & Koch scale, κ ≥ 0.8 is labeled *almost perfect agreement*. That label applies to **inter-coder agreement under the protocol's coder-provenance mode** (see `coder_provenance.mode` above). It does NOT establish *inter-rater reliability* in the audited-research sense unless that mode is `independent_human` and the second coder is demonstrably blind to the gold coder's reasoning.

- `independent_human`: the published κ is a reliability   estimate; cite as such.
- `llm_assisted_blinded`: the published κ is a   **self-consistency check** — the recoder is from the same   model family / training distribution as a likely   author-assist substrate, and the gold and recode share   systematic biases. Cite as `self-consistency, single-coder   LLM-assisted recode` and treat the κ floor as a *lower bound*   on consistency, not a reliability estimate.
- `author_self_recode_60d_gap`: similar caveat (residual   recall risk); cite the gap length explicitly.
- `unspecified`: do not cite the κ in the paper.

**Paper-readiness threshold** for this project: a `current` rubric C1 rate that depends on a variable with κ < 0.6 (under the strictest available provenance mode) is blocked. C1 depends on `coverage_status`; C2 (PARKED v0.1) depends on `observation_kind`; the attribution-tier phrasing lock depends on `attribution`. Variables with no `independent_human` pass are the largest open validity threat for the v0.1 paper and are tracked in `docs/paper_claims.md §0` ('Reliability discipline').
