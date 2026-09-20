# IMC submission compliance plan

Status checked: 2026-09-21.
The final working-draft PDF was compiled and checked on 2026-09-21.

## Target and evidence basis

The primary target is the **ACM Internet Measurement Conference (IMC) 2027
main-track full-paper category**.  The paper's measurement arm, its explicit
observation-error analysis, and the joint reappraisal of domain conclusions fit
the IMC scope better than a dataset-only framing.  The domain arm remains part
of the same paper because it supplies the behavioral object whose observability
is being evaluated.

No official IMC 2027 call or submission-instruction page was located on
2026-09-21.  Dates and rules for 2027 are therefore **unknown**, not inferred
from the prior cycle.  Until the 2027 call appears, formatting decisions use the
latest official IMC 2026 instructions as an explicitly provisional proxy:

- [IMC 2026 submission instructions](https://conferences.sigcomm.org/imc/2026/submission-instructions/)
- [IMC 2026 call for papers](https://conferences.sigcomm.org/imc/2026/cfp/)

## Provisional full-paper checks

| Requirement in the 2026 proxy | Current manuscript state | Required action |
| --- | --- | --- |
| Full paper: at most 13 pages of technical content; references and appendices excluded | Main content ends and Appendix A begins on page 8; references begin on page 9; the PDF has 9 pages total | Recheck boundaries after later content edits |
| Double-blind review | The PDF renders `Anonymous Author(s)`, has no Author metadata, and contains none of the source author names, affiliations or email addresses | Recheck the frozen submission PDF and artifact links for identifying repository paths or metadata |
| Letter paper, two columns, at least 10-point body font | The PDF is 612 by 792 points and uses the 10-point two-column proxy class; inline contract identifiers use the template's 9-point small text | Retest against the official 2027 template when available |
| Abstract no longer than 200 words | The final macro-expanded abstract contains 173 words | Recount after any abstract edit |
| Appendix section titled `Ethics` | Appendix A is titled exactly `Ethics` | Retain the title and verify any new collection is covered |
| Paper number and body/total page count in the author block | No paper number exists before registration | Add only after the 2027 submission is registered; do not invent a placeholder number in a release PDF |
| PDF below 15 MB, pages numbered, readable/embedded fonts | The PDF is approximately 0.52 MB, pages 1--9 are numbered, all 18 reported fonts are embedded, and included-figure minimum text sizes are 10.01, 9.39 and 9.13 points | Repeat visual and grayscale checks on the frozen submission PDF |
| Artifact-availability declaration | The manuscript describes the working artifact and correctly says the submitted snapshot is not frozen | Freeze the exact submitted snapshot before release |
| Plain-text references/BBL upload | `submission-references.bbl` mirrors the inline bibliography as a provisional upload artifact | Recheck synchronization and the actual 2027 portal requirement after every reference edit |
| Generative-AI disclosure | The manuscript contains an AI-use statement | Reconcile the final statement with the official 2027 wording once published |

## Scientific blockers before submission

The following are research-completeness blockers rather than formatting
problems:

1. independent human source-support, applicability, and action-stage review;
2. independent reference labels and inter-rater reliability for the held-out
   validation units;
3. corrected RQ1 estimates and RQ3 correction effects computed only after the
   reference labels exist;
4. final anonymization audit, frozen submission artifact, and author release
   sign-off.

Machine extraction, endpoint contrasts, archive searches, and raw-data
retrieval can establish collection coverage and measurement behavior before
human review.  They cannot substitute for the independent semantic labels
needed for validated enforcement rates or causal attribution.

## Recheck trigger

As soon as an official IMC 2027 call or submission-instruction page is
published, replace this proxy audit with the actual track, deadlines, template,
page accounting, anonymity, ethics, artifact, and disclosure requirements.
The 2026 dates must never be presented as 2027 dates.
