# Pilot Status

This file is the human-readable companion to `analysis/pilot-status.json`.

Use these commands to refresh status after editing event files:

```sh
python3 scripts/validate.py events/*.yaml
python3 scripts/draft_gap_report.py
python3 scripts/status_report.py
```

Interpretation:

- `admitted` events are baseline cases safe to include in release artifacts.
- `draft` events still contain unresolved evidence gaps or placeholder scaffolding.
- `changed_layer_count` is computed from `observed_change` observations only.
- Drafts with the highest `gap_marker_count` should be prioritized for evidence collection.
