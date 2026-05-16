# DRYRUN release pipeline — revert plan

> **Read this before tagging or pushing.** The
> `v0.2.0-rc-dryrun` artifact was produced end-to-end as a pipeline
> demo, not as a real release. All `last_human_audit` stamps and the
> `coder_provenance.mode = independent_human_dryrun_llm_simulated`
> tier are deliberately marked DRYRUN so the artifact is honest about
> what it is.

## What the dryrun produced

A complete release-signoff log at
[`0.2.0-rc-dryrun.md`](0.2.0-rc-dryrun.md) showing:

- clean working tree ✓
- CITATION.cff at `0.2.0-rc-dryrun` · `2026-05-15` ✓
- `make regenerate` clean under `SOURCE_DATE_EPOCH=1778803200` ✓
- `check_paper_readiness.py --strict-repro --strict-reliability
  --strict-null-audit --strict-audit --allow-soft-attribution
  --allow-dryrun-human-gates` PASS ✓
- byte-stable across 25 artifacts ✓
- verdict: **SIGN-OFF READY**

This proves the pipeline runs end-to-end. It does **not** prove the
artifact is release-quality, because the human-only steps were
simulated.

The original dryrun log was produced before the guardrail hardening
that made dryrun human gates explicit. Re-running the same dryrun now
must pass both `--accept-soft-attribution` and
`--allow-dryrun-human-gates` to `scripts/release_signoff.py`.

## What is honest in this artifact (keep)

- The κ values themselves are real: Cohen κ = 1.0 (coverage_status,
  single-agent prior pass), Cohen κ = 1.0 / Fleiss κ = 1.0
  (observation_kind, 3-agent), Cohen κ = 0.583 / Fleiss κ = 0.683
  (attribution, 3-agent).
- The attribution disagreement cluster is a real codebook finding:
  3 stablecoin-freeze rows where the `direct` / `plausible` line is
  underspecified. Surfacing it is the v0.1 IRR pass's load-bearing
  contribution.
- The null-case 2-agent cross-audit is real: 11/13 convergence,
  `sec-v-uniswap-wells-notice-2024` flagged by both agents,
  P2 corpus-wide conventions surfaced honestly. The aggregate at
  [`../null_audits/AGGREGATE.md`](../null_audits/AGGREGATE.md) is
  the real artifact; the 12 stamps are the dryrun decoration on top.
- The `status: rejected` of `sec-v-uniswap-wells-notice-2024` is
  defensible on its own terms (Wells notice withdrawn; substrate
  doesn't measure app.uniswap.org). A real release decision could
  legitimately land in the same place.
- The textual fixes (lazarus-laundering self-contradiction,
  lazarus-entity citation[1] mark, lockbit-leader offramp_cex note,
  zservers L0 substrate note) are real quality improvements that
  should survive any revert.
- The infrastructure changes — `--allow-soft-attribution` flag,
  `independent_human_dryrun_llm_simulated` provenance tier,
  `scripts/release_signoff.py` itself, Fleiss-κ-across-3-LLM-agents
  in `compute_irr_kappa.py` — are real engineering that should
  survive any revert.

## What is DRYRUN-only (must revert before real release)

| What | Where | Revert action |
| --- | --- | --- |
| `last_human_audit: 2026-05-15` on 12 null cases | `events/{iran-ransomware,irgc,lazarus-entity,lazarus-laundering,lockbit-leader,matveev,pertsev-nl-arrest,russian-cybercrime-infra,sichuan-silence,sinbad,storm-semenov,zservers}-ofac-*.yaml` | Each stamp is preceded by an explicit `**LAST_HUMAN_AUDIT STAMP — DRYRUN 2026-05-15**:` block in `analysis_notes`. Drop the stamp until a real human re-audits the case. |
| `coder_provenance.mode: independent_human_dryrun_llm_simulated` in `kappa_report.json` | `analysis/inter_rater/kappa_report.{md,json}` | Rerun `compute_irr_kappa.py --coder-mode llm_assisted_consensus_3x ...` for the honest provenance label. Or run a real independent-human IRR pass and set `--coder-mode independent_human`. |
| `--allow-soft-attribution` and `--allow-dryrun-human-gates` | `scripts/check_paper_readiness.py` / `scripts/release_signoff.py` | Keep the flags, but do not pass either one by default for a real release. `release_signoff.py` now requires explicit `--accept-soft-attribution` and `--allow-dryrun-human-gates` opt-ins. |
| `version: "0.2.0-rc-dryrun"` and `date-released: "2026-05-15"` in `CITATION.cff` | `CITATION.cff` | Set both fields to the real release values when actually tagging. The release_signoff helper writes the values you pass; just rerun with the real version + date. |

## Revert recipes

### Selective revert (keep infrastructure, drop dryrun decorations)

```bash
# 1. Drop the 12 last_human_audit stamps + DRYRUN preambles
#    (manual: each event has a "**LAST_HUMAN_AUDIT STAMP — DRYRUN ...**"
#    paragraph in analysis_notes and a `last_human_audit: 2026-05-15`
#    line near the top metadata).
#
# 2. Restore sec-v-uniswap-wells-notice-2024 status if you disagree
#    with the rejection (or run a real human re-review and re-decide).
#
# 3. Re-run compute_irr_kappa with honest provenance:
python3 scripts/compute_irr_kappa.py \
    --coder-mode llm_assisted_consensus_3x \
    --coder-name "claude-opus-4-7 × 3 (agents A/B/C)" \
    --coder-prompt-version "2026-04-26-irr-prompt-v2-3x" \
    --coder-notes "3 blind LLM agents (A/B/C); majority-vote into master blind CSV; Fleiss κ across the 3 agents reported alongside Cohen κ vs gold."
#
# 4. Revert CITATION.cff:
#    edit version: "0.2.0-rc-dryrun" → previous release value
#    edit date-released: "2026-05-15" → previous release date
```

### Full revert (back to pre-dryrun state)

```bash
git revert 13619fd   # the "DRYRUN release pipeline demo" commit
```

(Caveat: this also reverts the engineering improvements
[`--allow-soft-attribution`, `independent_human_dryrun_llm_simulated`
tier, `scripts/release_signoff.py`, Fleiss-κ wiring, textual
quick-fixes]. Prefer selective revert.)

## Recipe for a real release after the dryrun

The minimum a real release needs that this dryrun simulated:

1. **Real independent-human IRR pass** on the same 90+25+20-row
   sample. Update kappa_report with `--coder-mode independent_human`
   and real recoder identity in `--coder-name`.
2. **Real human audit of the 12 null cases** (the 2-agent cross-audit
   is a pre-screen, not the audit itself). Update each event's
   `last_human_audit` only after the human spot-checks the
   `body_hash` pairs and the scoped_claim language. Decide what to do
   about the 2 divergent verdicts (pertsev, storm-semenov) and the
   corpus-wide `offramp_cex.measured` convention.
3. **Real human decision on sec-v-uniswap-wells-notice-2024.** The
   dryrun chose `status: rejected`; the human can confirm or pick a
   different option from the three the agents proposed.
4. **Decide whether `--allow-soft-attribution` should be passed.**
   It is no longer always-on in `release_signoff.py`; the human must
   pass `--accept-soft-attribution` explicitly after confirming that
   the v0.1 paper retracts the affected comparative attribution-rate
   claims. A real release must not pass `--allow-dryrun-human-gates`.
5. **Real `version` + `date` in CITATION.cff**, then re-run
   `scripts/release_signoff.py --version <real> --date <real>`.

Only after step 5 produces a fresh `SIGN-OFF READY` log on a clean
tree are the human-only `git tag` + `git push` steps appropriate.
