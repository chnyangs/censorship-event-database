# Candidate Triggers

Watcher jobs may drop unreviewed trigger stubs here before they become full events.

## Workflow

1. Watcher creates `candidate_triggers/YYYY-MM-DD-<slug>.yaml`.
2. Reviewer triages:
   - accept: promote into `events/<slug>.yaml`
   - reject: move into `candidate_triggers/rejected/`
   - defer: keep here with updated notes

This directory is optional for the historical-backfill phase, but keeping it in the repo structure makes the methodology concrete.
