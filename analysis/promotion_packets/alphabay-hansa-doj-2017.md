# Promotion review — alphabay-hansa-doj-2017

## Verdict
- **promotion_recommendation**: `admit_with_minor_fixes`
- **confidence**: medium
- **one-sentence justification**: Trigger and L4 observation gates are met by two replayable primary_legal anchors (FBI body fully readable; DOJ body is an Akamai bot-block stub but its hash and path replay deterministically), but the event needs `target.enumeration` tightening, an `evidence_use: contextual_unarchived` flag on the DOJ stub citation (or a Wayback companion), and a small honesty note on the day-precision being announcement-day rather than seizure-day.

## Trigger gate
- citation count + tier: 2 × `primary_legal` (DOJ OPA press release URL L20–23; FBI news story L28–31). Methodology §3.5 needs only one primary_legal — this exceeds the threshold.
- archive anchors present: yes — both have `body_hash` + `body_path` (L22–23, L30–31). However the DOJ html at `sources/http_captures/alphabay-hansa-doj-2017/primary/www.justice.gov__...html` is a 2,928-byte Akamai bot-block interstitial (`bm-verify` meta-refresh page), not the real DOJ text; the FBI capture at 81,732 bytes is the substantive narrative. The same Akamai-stub pattern exists in the already-admitted `btc-e-doj-2017` event (justice.gov body 2,937 bytes), so this is a known dataset quirk rather than a hard fail, but it should be acknowledged with `evidence_use: contextual_unarchived` on the DOJ row or a Wayback companion URL per §6.
- timestamp + precision honest: `2017-07-20T00:00:00Z` with `timestamp_precision: day` (L17–18). Per the FBI source the AlphaBay servers were seized "in early July" and Cazes was arrested 2017-07-05; 2017-07-20 is the public DOJ/FBI press-conference announcement date. The trigger row should briefly disambiguate "announcement day, not seizure day" — the asymmetry is small (day-precision is honest) but `analysis_notes` does not flag it.
- verdict: **concerns** (admission gate met; small archive-quality and timestamp-semantics notes recommended).

## Per-observation gates (one block per observation row)
- **L4 / observed_change / direct / anchor types: 2 × `body_hash`+`body_path` (L86–100)** — both sources carry replayable anchors per `schema/event.schema.json` §source. Verdict: **pass**. The FBI source body (verified) explicitly names AlphaBay and Hansa as coordinated takedowns; the DOJ body is the Akamai stub (replayable but content-thin), so attribution rests primarily on the FBI capture. One row is technically sufficient — the substantive link is present.

## Coverage status honesty
- **`l0_network: not_applicable`** (L54–58) — correct. Tor hidden-service marketplace; no public-web ISP block surface applies.
- **`l1_consensus: not_applicable`** (L59–60) — correct for a 2017 darknet marketplace seizure pre-PBS.
- **`l3_rpc: not_applicable`** (L61–62) — correct. No RPC surface.
- **`l4_frontend: measured`** (L63–68) — defensible. Per methodology §4.4 the .onion frontends went dark with server seizure; DOJ/FBI primary-legal description is treated as the L4 archival evidence (same logic the admitted `hydra-doj-2022` uses for its Tor frontend). The `scope: [alphabay_market, hansa_market]` is appropriate.
- **`asset_onchain: not_measured`** (L69–73) — honestly disclosed. FBI source mentions "millions of dollars in cryptocurrency" preserved for forfeiture but the YAML correctly does not claim transaction-level receipts.
- **`offramp_cex: not_applicable`** (L74–75) — correct (darknet marketplace, not a CEX).

## Attribution discipline
- L4 `observed_change` `attribution: direct` (L82) — FBI source text (verified) explicitly says "the largest marketplace on the Darknet … has been shut down" and "the operation to seize AlphaBay coincided with efforts by Dutch law enforcement to shut down the Hansa Market." That is named-link evidence connecting trigger (DOJ/Operation Bayonet announcement) to observed state transition (marketplaces seized). The DOJ stub body cannot itself carry the named-link text, but the FBI body does. `direct` is supported.

## Scoped claim
The `scoped_claim` (L107–110) is appropriately narrow: it asserts only public marketplace/platform shutdown at L4 and explicitly disclaims transaction-level on-chain asset movement. This matches what the FBI capture supports (named takedown of both marketplaces, with crypto context but no enumerated tx hashes retained in this draft). It does not over-attribute beyond `direct` at L4 nor reach into the not_measured asset layer. The claim is well-disciplined.

## Self-contradiction check
- `analysis_notes` (L102–105) and `coverage` (L53–75) are mutually consistent: both call out `asset_onchain` as `not_measured` and frame the event as L4-only.
- `scoped_claim` does not contradict `attribution: direct` — it scopes down (L4 only, no on-chain) rather than up.
- No "null_event rather than null_event"–class typos found. `empirical_shape: comparison` (L7) is consistent with exactly one `observed_change` layer (L4), which is at the lower bound of the `comparison` range (1–2 changed layers per methodology §3.2). `admission_tier: empirical_case` (L8) matches: ≥1 strong-attribution observed_change layer.
- Minor coherence note: `target.chains: [bitcoin, monero, ethereum]` (L48) is broader than the substantive evidence (FBI source names only Bitcoin and "digital currencies" generically; Monero/ETH not explicitly mentioned in the captured body). Not a contradiction per se because the field is target descriptor not observation evidence, but worth tightening.

## Specific issues blocking admit_now
- The DOJ press-release citation body is an Akamai bot-block stub (`body_hash sha256:4f9...` resolves to a 2,928-byte interstitial, not the DOJ narrative). The schema validator and §6 will not flag this (the body_hash is real and replayable), but per §3.5 the admission reviewer should mark the citation `evidence_use: contextual_unarchived` or capture a Wayback companion, because the named-link evidence currently rests on the FBI capture alone. With only one substantive body, the trigger still satisfies the §3.5 primary-legal threshold (one primary_legal suffices) but the YAML reads as if two equivalent primary anchors exist.
- `target.enumeration: subset` (L41) is appropriate, but `enumeration_note` (L42–45) does not name the Hansa Market's distinct legal track (Dutch FIOD covert operation 2017-06-20 → 2017-07-20). Review report's standing blocker on this event is "Tighten target enumeration or target scope" — that blocker is still live.
- Day-precision timestamp is "announcement day" not "seizure day"; the trigger uses 2017-07-20 (press-conference) while AlphaBay servers were seized in early July and Hansa was being covertly operated by FIOD from 2017-06-20. `analysis_notes` should briefly disambiguate.
- `target.chains: [bitcoin, monero, ethereum]` (L48) over-states evidentiary coverage relative to the captured body (FBI mentions Bitcoin and generic "digital currencies").

## Recommended fixes (if admit_with_minor_fixes)
- Add `evidence_use: contextual_unarchived` to the DOJ citation rows (trigger L20–27 and observation L87–93) **or** append a `wayback:` URL to a verified Wayback snapshot of the DOJ press release. Note in the source `note:` that the local body is the Akamai interstitial; the FBI capture is the substantive named-link anchor. (Mirror the `bitzlato-doj-2023` pattern at L26–28.)
- Tighten `enumeration_note` (L42–45) to mention the two distinct legal tracks: DOJ + FBI + Thai authorities for AlphaBay (announced 2017-07-20, servers seized early July, Cazes arrested 2017-07-05), and Dutch FIOD covert operation for Hansa Market (2017-06-20 to 2017-07-20). This addresses the standing review-report blocker.
- Add one sentence to `analysis_notes` (L102–105) noting that 2017-07-20 is the public-announcement day and the underlying AlphaBay server seizure / FIOD Hansa operation predate it; day-precision is honest because the public-cascade clock starts at announcement.
- Reduce `target.chains` (L48) to `[bitcoin]` (with optional note that the marketplace handled other currencies but only Bitcoin is named in the retained admission-grade body), or pin a separate source for the Monero/Ethereum claims.
- Optional: pin a second admission-grade body for Hansa specifically (Dutch politie.nl FIOD page or Europol press release) to harden the Hansa half of the joint claim; the current FBI body asserts Hansa coordination but does not anchor the Dutch operational evidence.
