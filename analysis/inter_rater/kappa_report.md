# Inter-rater reliability report

Generated: `2026-06-02T03:49:00Z` · computer `scripts/compute_irr_kappa.py` · blind/key inputs from `analysis/inter_rater/`.

## Coder provenance

- **Mode**: `independent_human_dryrun_llm_simulated` (one of `independent_human`, `llm_assisted_blinded`, `llm_assisted_consensus_3x`, `independent_human_dryrun_llm_simulated`, `author_self_recode_60d_gap`, `unspecified` — published κ requires non-`unspecified` provenance, and reliability claims require `independent_human`).
- **Coder**: `[DRYRUN-LLM] 3 blind LLM agents (claude-opus-4-7 ×3) labeled as independent_human for pipeline-demo only`
- **Prompt / rubric version**: `2026-04-26-irr-prompt-v2-3x · DRYRUN labeled`
- **Notes**: DRYRUN 2026-05-15: 3 LLM agents (A/B/C) ran the blind recode. coder_mode set to independent_human_dryrun_llm_simulated specifically so a dryrun release pipeline can accept the artifact only when --allow-dryrun-human-gates is passed, while making it visually obvious to any future reader that this is NOT a real independent-human pass. A real release decision must (a) run an actual independent human IRR pass, (b) revert this mode to independent_human, and (c) re-run scripts/release_signoff.py without --allow-dryrun-human-gates. Until then, all κ values must be cited as self-consistency / consensus, not reliability.

| variable | n coded / n total | observed agreement | Cohen's κ (vs gold) [95% CI] | Fleiss' κ (across LLM agents) | label |
| --- | --- | --- | --- | --- | --- |
| `coverage_status` | 90 / 90 | 1.0 | 1.0 [1.0, 1.0] | — | almost perfect |
| `observation_kind` | 25 / 25 | 1.0 | 1.0 [1.0, 1.0] | 1.0 (3r) | almost perfect |
| `attribution` | 20 / 20 | 0.85 | 0.5833 [0.0, 1.0] | 0.6825 (3r) | moderate |

## `coverage_status` detail

- n_coded: **90** of 90 rows (remaining rows are missing `recode_value` — coder-incomplete)
- observed agreement p_o = 1.0
- expected agreement p_e = 0.44
- Cohen's κ = **1.0** (almost perfect)
- 95% CI (bootstrap, B=2000): **[1.0, 1.0]**, SE = 0.0

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
- 95% CI (bootstrap, B=2000): **[1.0, 1.0]**, SE = 0.0

### Confusion matrix

| recode \ original | observed_change | observed_no_change |
| --- | --- | --- |
| **observed_change** | 20 | 0 |
| **observed_no_change** | 0 | 5 |

## `attribution` detail

- n_coded: **20** of 20 rows (remaining rows are missing `recode_value` — coder-incomplete)
- observed agreement p_o = 0.85
- expected agreement p_e = 0.64
- Cohen's κ = **0.5833** (moderate)
- 95% CI (bootstrap, B=2000): **[0.0, 1.0]**, SE = 0.2218

### Confusion matrix

| recode \ original | direct | plausible |
| --- | --- | --- |
| **direct** | 14 | 0 |
| **plausible** | 3 | 3 |

## Interpretation

Cohen's κ thresholds (Landis & Koch 1977 — still the most cited convention despite known limitations with skewed marginals): < 0.2 slight, 0.2–0.4 fair, 0.4–0.6 moderate, 0.6–0.8 substantial, > 0.8 almost perfect on the Landis & Koch scale.

**Read κ with its CI, not as a point.** Each κ above carries a seeded nonparametric bootstrap 95% CI (B=2000 resamples of the coded cells). On the small coded-n of this subset those intervals are wide, so a point estimate near the 0.6 paper-readiness gate is not a clean pass/fail: a variable whose CI straddles 0.6 has not been shown to clear it. Perfect-agreement variables yield a degenerate [1.0, 1.0] interval (every resample agrees), which is honest but reflects the easy variables, not the contested ones. Any published κ must be cited with its CI and coded-n.

**What this κ does and does not establish — read before citing.** Under the Landis & Koch scale, κ ≥ 0.8 is labeled *almost perfect agreement*. That label applies to **inter-coder agreement under the protocol's coder-provenance mode** (see `coder_provenance.mode` above). It does NOT establish *inter-rater reliability* in the audited-research sense unless that mode is `independent_human` and the second coder is demonstrably blind to the gold coder's reasoning.

- `independent_human`: the published κ is a reliability   estimate; cite as such.
- `llm_assisted_blinded`: the published κ is a   **self-consistency check** — the recoder is from the same   model family / training distribution as a likely   author-assist substrate, and the gold and recode share   systematic biases. Cite as `self-consistency, single-coder   LLM-assisted recode` and treat the κ floor as a *lower bound*   on consistency, not a reliability estimate.
- `llm_assisted_consensus_3x`: same caveat, with three blind   LLM agents majority-voted into the master recode and Fleiss'   κ reported across agents. Cite as consensus self-consistency,   not independent-human reliability.
- `independent_human_dryrun_llm_simulated`: dryrun-only   pipeline rehearsal label. Do not cite as reliability and do   not use for a real release unless the paper-readiness gate is   being run with an explicit dryrun allowance.
- `author_self_recode_60d_gap`: similar caveat (residual   recall risk); cite the gap length explicitly.
- `unspecified`: do not cite the κ in the paper.

**Paper-readiness threshold** for this project: a `current` rubric C1 rate that depends on a variable with κ < 0.6 (under the strictest available provenance mode) is blocked. C1 depends on `coverage_status`; C2 (PARKED v0.1) depends on `observation_kind`; the attribution-tier phrasing lock depends on `attribution`. Variables with no `independent_human` pass are the largest open validity threat for the v0.1 paper and are tracked in `docs/paper_claims.md §0` ('Reliability discipline').
