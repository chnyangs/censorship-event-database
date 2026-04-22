# HTTP Capture Bundles

This directory stores local capture bundles for live web evidence that cannot
be reconstructed reliably from static URLs alone.

Use this for cases such as:

- current-state frontend availability
- redirect-chain evidence
- GitHub org / repo reachability at review time
- current policy pages whose content may drift

Preferred workflow:

1. Create an event-specific subdirectory, for example:
   `sources/http_captures/tornado-cash-ofac-delisting-2025/2026-04-21-frontends/`
2. Run `python3 scripts/capture_http_artifact.py --output-dir <dir> <url...>`.
3. Reference the resulting local bundle in the relevant event's `analysis_notes`
   or source notes.

Each bundle should contain:

- one body file per URL
- one metadata JSON per URL
- one `manifest.json` describing the capture set
