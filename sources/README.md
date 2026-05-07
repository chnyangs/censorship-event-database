# Sources Layout

This directory stores archived or reproducible source artifacts referenced by event files.

## Subdirectories

- `archived_htmls/`: local WARC or HTML fallbacks when Wayback is unavailable
- `http_captures/`: reproducible live-web capture bundles for current-state evidence
- `onchain_receipts/`: cached JSON-RPC receipts and transaction metadata
- `ofac_sdn_diffs/`: local snapshots or diffs of sanctions-list XML
- `source_manifest.{csv,json,md}`: generated SHA-256 manifest for local
  source artifacts included in the release reproduction surface

## Conventions

- Use one subdirectory per event id when storing event-specific artifacts.
- Prefer content-addressed filenames or include a content hash in the event YAML.
- Treat this tree as append-only except for explicit correction / retraction workflows.
- Rebuild the release source manifest with `make source-manifest` after adding
  or removing local capture artifacts.
