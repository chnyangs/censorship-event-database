# B1 — Independent-Human IRR: handoff & status

**Blocker B1** (the paper's open reliability blocker): published reliability
requires an *independent-human* inter-rater pass. Everything around that pass is
built and turnkey; the one missing input is human coding, which cannot be
synthesised.

## What is already in place

- **Codebook** `schema/codebook.md` — coding rules with worked examples; §1
  (`attribution`) is annotated as the known low-agreement variable and carries
  resolved dispute cases.
- **Stratified blind sample + packets** — `make irr-sample`, `make irr-packet`;
  blind/key CSVs under `analysis/inter_rater/`; the evidence-tier packet
  (`analysis/evidence_tier_irr_packet_2026_05_31.{md,csv}`) is intentionally
  blank, awaiting two human coders.
- **κ computation with confidence intervals** — `scripts/compute_irr_kappa.py`
  and `scripts/compute_evidence_tier_irr_kappa.py` now attach a seeded
  nonparametric bootstrap 95% CI to every κ (shared helper
  `scripts/_kappa_ci.py`). The CI is deterministic, so regenerating the report
  does not churn the artifact.
- **Release gate** — `scripts/release_signoff.py` +
  `check_paper_readiness.py --strict-reliability` block a real release while the
  provenance mode is anything other than `independent_human` (the current
  `independent_human_dryrun_llm_simulated` only passes with the explicit
  `--allow-dryrun-human-gates` rehearsal flag).

## Current numbers — dryrun only, NOT reliability

From `analysis/inter_rater/kappa_report.md` (mode
`independent_human_dryrun_llm_simulated`, 3× `claude-opus-4-7` blind agents):

| variable | n | κ (vs gold) [95% CI] | reading |
|---|---|---|---|
| `coverage_status` | 90 | 1.0 [1.0, 1.0] | easy variable; degenerate interval |
| `observation_kind` | 25 | 1.0 [1.0, 1.0] | easy variable; degenerate interval |
| `attribution` | 20 | 0.5833 **[0.0, 1.0]** | uninformative at this n |

**The CI is the new, load-bearing fact.** `attribution` κ=0.58 on n=20 has a 95%
bootstrap CI spanning the entire [0, 1] range: the point estimate cannot clear
(or fail) the project's κ≥0.6 gate at this sample size. Before a *publishable*
attribution reliability claim, the attribution IRR sample must be enlarged well
beyond n=20 (size it empirically — re-run the bootstrap on a pilot human batch
until the CI half-width is tolerable, e.g. ≤±0.15). `coverage_status` and
`observation_kind` are saturated at κ=1.0 and need no enlargement.

## Turnkey steps for the real human pass

1. Recruit ≥2 coders independent of the author; give them `schema/codebook.md`
   only (not the event YAMLs, which leak `evidence_tier`/admission labels — use
   the redacted packets / independently rendered source artifacts).
2. Enlarge the `attribution` blind sample (step above) before coding; keep the
   coverage/observation samples as-is.
3. Coders fill `coder_a_*` / `coder_b_*` (evidence-tier packet) and the
   `recode_value` blind CSVs without seeing each other's or the gold labels.
4. Run `make irr-kappa` and `make evidence-tier-irr-kappa`; cite each κ **with
   its CI and coded-n**.
5. In `compute_irr_kappa.py` set `--coder-mode independent_human`; re-run
   `scripts/release_signoff.py` **without** `--allow-dryrun-human-gates`.
6. Update `docs/paper_claims.md §0` (Reliability discipline) and the paper's
   reliability section to cite the human κ + CI.

Until step 5 clears, all κ values remain self-consistency / consensus figures,
not reliability — as the report header already states.
