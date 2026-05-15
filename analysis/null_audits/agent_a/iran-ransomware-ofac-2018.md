# Null-case audit · iran-ransomware-ofac-2018 · agent A

## Summary verdict
- **agent_verdict**: `pass_with_concerns`
- **confidence**: high
- **one-sentence justification**: The L4 frontend null is properly anchored by two Wayback snapshots that bracket the designation window, but the `enexchanger.com` redirect-shell snapshots evidence only "domain still redirects" and the wording "redirect-shell shape" should be re-read by a human to confirm structural equivalence (the digests admittedly differ).

## Trigger
- type / actor / timestamp / precision: `ofac_sdn_designation` / `US_OFAC` / 2018-11-28T00:00:00Z / day
- citation admissibility (primary / semi-primary count): 2 primary_legal citations (OFAC Recent Actions page with wayback + body_hash + body_path; Treasury press release sm556 with note only, no body_hash). The OFAC RA page is fully anchored.
- verdict: pass

## Scoped claim
- which layers were scoped: L4 frontend (`partially_measured`, enexchanger.com); L0 marked `not_measured`; offramp_cex `not_measured`; all other layers structurally `not_applicable` (Bitcoin native, pre-Merge).
- is the null-case claim properly bounded (not a corpus-wide claim)? Yes — the `scoped_claim` is limited to the enexchanger.com 20-day bracket and explicitly notes L1/L3 Ethereum layers do not yet exist for this event. It does not over-generalize.

## Observation anchors
- layer `l4_frontend` / `observed_no_change` / attribution `none` / anchors present: 2 × `body_hash + body_path` Wayback snapshots (pre 2018-11-23 and post 2018-12-12). No `scope_descriptor` on the observation (relies on direct artifact comparison).
  - verdict: pass — direct Wayback artifacts replay the absence claim for the redirect shell. This is one of only two cases in the 13 with direct frontend artifacts (per `null_case_pre_audit.md`).

## Coverage status honesty
- `l4_frontend`: `partially_measured` — defensible. Two Wayback snapshots are pinned but the redirect-shell body carries no rich application state; the YAML correctly down-weights to `partially_measured`.
- `l0_network`: `not_measured` — honest; no OONI / probe data.
- `offramp_cex`: `not_measured` — honest; chain-analytics substrate anchors are noted but no per-event slice is pinned.
- `l1_consensus`, `l3_rpc`, `asset_onchain`: `not_applicable` — defensible (Bitcoin native, pre-Merge).

## Issues / concerns
- The two Wayback snapshots have different digests (one is enexchanger.com bare, the other www.enexchanger.com — different Host headers). The note flags this honestly. Human should manually compare the two captures to confirm the "redirect-shell shape" is genuinely the same and not a hidden state transition.
- Treasury press-release citation [1] has only a `note` and no `body_hash + body_path`. This is a corroborating second citation, not the primary anchor, so admissibility is preserved by citation[0], but tightening would help.
- No `scope_descriptor` on the L4 observation; this is fine because the artifact pair *is* the anchor.

## Recommendation for human reviewer
The human reviewer should open both `web.archive.org__web-20181123094507-http-enexchanger.com__cf3a7b8821.html` and `web.archive.org__web-20181212063124-http-www.enexchanger.com__b9cb6763bc.html`, confirm both are 303 redirects with structurally-equivalent shape (i.e. the Host-header variation is the only material delta), and then stamp `last_human_audit`. If the post-event capture turns out to be substantively different (e.g. final-state content vs. redirect), the L4 observation needs revision.
