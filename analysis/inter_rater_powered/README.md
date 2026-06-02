# Powered attribution IRR packet (n=157)

Enlarged blind sample for the **`attribution`** variable only, built because the
n=20 dryrun gave a bootstrap 95% CI of **[0.0, 1.0]** — uninformative. Generated
with `scripts/build_irr_sample.py --n-events 185 --seed 20260602`; the
coverage/observation CSVs from that run were discarded (those variables are
already saturated at κ=1.0 in `../inter_rater/` and need no enlargement).

- `attribution_blind.csv` — 157 rows, blank `recode_value` for independent human
  coders to fill (do not show them `attribution_key.csv`).
- `attribution_key.csv` — gold labels pulled from the corpus (108 `direct`, 49
  `plausible`).
- `sample_manifest.csv`, `meta.yaml` — provenance.

**Target.** At the dryrun's observed agreement structure (κ≈0.58, p_o=0.85), a
simulation puts the bootstrap 95% CI half-width at this n near **±0.14**
(≈[0.44, 0.69]), versus ±0.36 at n=20.

**Honest caveat — read before using.** Enlarging the sample tightens the CI; it
does **not** raise κ. If the true attribution agreement is ≈0.58, even the full
342-observation population yields a CI that still **straddles the 0.6
paper-readiness gate** (simulated [0.48, 0.68] at n=342). So a larger n makes the
gate *decision* defensible but cannot by itself make `attribution` pass: clearing
0.6 requires improving the codebook §1 rubric to raise true coder agreement, not
just more rows. This packet exists to make the eventual human estimate precise,
and to force that rubric-versus-threshold question into the open.

**Use.** After humans fill `recode_value` blind:

```
python3 scripts/compute_irr_kappa.py \
    --dir analysis/inter_rater_powered --variables attribution \
    --coder-mode independent_human --coder-name "<coders>"
```

Cite the resulting κ **with its CI and n** (see `../inter_rater/B1_human_irr_handoff.md`).
