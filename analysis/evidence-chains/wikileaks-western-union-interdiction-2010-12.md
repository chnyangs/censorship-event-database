# Evidence chain — `wikileaks-western-union-interdiction-2010-12`

**Status**: `admitted` · **Stratum**: `S5_corporate` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `cd67682` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-21` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> Western Union added WikiLeaks to its money-transfer "Interdiction
> List" on 2010-12-21, blocking WikiLeaks from receiving donations
> through the Western Union rail as one of five legs of the
> December-2010 financial blockade. observation_kind=observed_change
> with attribution=plausible: the action is attested via the WikiLeaks
> Banking Blockade counterparty statement and contemporaneous journalism
> but no primary Western Union corporate disclosure was located. Discovery-
> ledger tier; not used in main statistical denominators.

## 1. Trigger

- **Type**: `corporate_policy_change`
- **Actor**: `WESTERN_UNION_OPERATOR`
- **Timestamp**: `2010-12-21 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_corporate`**
  - URL: <https://wikileaks.org/Banking-Blockade.html>
  - Wayback: <https://web.archive.org/web/2012/https://wikileaks.org/Banking-Blockade.html>
  - body_hash: `sha256:0e508a4de9c98728b2285a4d0bfb66155b1c5f9396dc5765b6c06ac7c71de647`
  - body_path: `sources/http_captures/wikileaks-western-union-interdiction-2010-12/v0_3_primary_repair/wikileaks.org__Banking-Blockade.html__9000597c87.html`
  > WikiLeaks "Banking Blockade" support-campaign page enumerates
> the financial intermediaries that cut off WikiLeaks donation
> rails in December 2010. The enumeration names Bank of America,
> VISA, MasterCard, PayPal, and Western Union, and dates the
> Western Union action to 2010-12-21 as an addition of WikiLeaks
> to a Western Union "Interdiction List". primary_corporate here
> denotes WikiLeaks' first-party statement as the affected
> publishing/donation recipient entity; it is a counter-
> party statement issued by WikiLeaks (the donee), not a
> corporate press release issued by Western Union itself, and
> no primary Western Union corporate disclosure of the action
> was located in this authoring pass. Marked
> evidence_use=contextual_unarchived because (a) the body_hash+
> body_path archival capture was not pinned in this authoring
> pass and (b) the source is the affected party rather than the
> acting party. The citation is the strongest publicly accessible
> anchor for the 2010-12-21 date and is retained here as the
> coverage_gap anchor for the WU leg of the blockade. Provisional
> year-prefix wayback anchor pending re-pin.
- **`supporting_journalism`**
  - URL: <https://www.csmonitor.com/World/Latest-News-Wires/2011/1024/Wikilieaks-says-financial-blockade-could-put-it-out-of-business>
  - Wayback: <https://web.archive.org/web/2012/https://www.csmonitor.com/World/Latest-News-Wires/2011/1024/Wikilieaks-says-financial-blockade-could-put-it-out-of-business>
  > Christian Science Monitor wire piece dated 2011-10-24
> summarising the WikiLeaks financial blockade and the
> enumerated intermediary set (Bank of America, VISA,
> MasterCard, PayPal, Western Union). The piece references the
> 2010-12 trigger window and the ~95%-revenue-loss claim
> WikiLeaks made at the time. Used here as a contemporaneous
> secondary anchor for the WU leg of the blockade, since no
> primary Western Union corporate disclosure was located in
> this authoring pass. evidence_use=contextual_unarchived;
> Wayback snapshot pinning required in human-audit pass.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: WikiLeaks (donation funnel)
- **Canonical domains**: `wikileaks.org`

> Target is the WikiLeaks donation-receipt funnel via the Western
> Union money-transfer rail. WikiLeaks (and affiliated legal-
> defense / publishing entities such as the Wau Holland Foundation
> that channelled donations to WikiLeaks in 2010-2011) is the
> single named donee whose Western Union receipt capability was
> cut. enumeration=subset because the public record does not
> enumerate the specific WikiLeaks-affiliated receiving accounts
> or counterparties named on the Western Union "Interdiction List";
> only the donee-side identity (WikiLeaks) is identified.

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `plausible` · Δt = 0h

**Event label**: `wikileaks_added_to_western_union_interdiction_list`

**Timestamp**: `2010-12-21 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_corporate`**
  - URL: <https://wikileaks.org/Banking-Blockade.html>
  - Wayback: <https://web.archive.org/web/20110630203331/http://wikileaks.org/Banking-Blockade.html>
  - body_hash: `sha256:0e508a4de9c98728b2285a4d0bfb66155b1c5f9396dc5765b6c06ac7c71de647`
  - body_path: `sources/http_captures/wikileaks-western-union-interdiction-2010-12/v0_3_primary_repair/wikileaks.org__Banking-Blockade.html__9000597c87.html`
  > WikiLeaks Banking Blockade page is a first-party WikiLeaks
> statement and the strongest publicly
> accessible anchor for the 2010-12-21 Western Union
> Interdiction-List addition that this authoring pass located.
> observation_kind=coverage_gap with attribution=unknown
> honestly represents the absence of a primary Western Union
> corporate disclosure of the action. The cascade is real but
> the primary acting-party evidence is missing from the public
> record located in this authoring pass; the counterparty-
> statement anchor cannot bear direct acting-party attribution
> weight. Provisional
> year-prefix wayback anchor pending re-pin.
- **`semi_primary_wayback`**
  - URL: <https://www.csmonitor.com/World/Latest-News-Wires/2011/1024/Wikilieaks-says-financial-blockade-could-put-it-out-of-business>
  - Wayback: <https://web.archive.org/web/20111025083916/http://www.csmonitor.com/World/Latest-News-Wires/2011/1024/Wikilieaks-says-financial-blockade-could-put-it-out-of-business>
  - body_hash: `sha256:5e1cf2f9e45d5a8f220ff0d746e115575189a21f7e2a7ea5b20c78fb4812bc23`
  - body_path: `sources/http_captures/wikileaks-western-union-interdiction-2010-12/primary/web.archive.org__web-20111025083916-http-www.csmonitor.com-World-Latest-News-Wires-2011-1024-Wikilieaks-says-financial-blockade-could-put-it-out-of-business__a2679c1080.html`
  > CSMonitor wire piece 2011-10-24 corroborates the WU leg of
> the financial blockade and the WikiLeaks revenue-loss
> claim. Secondary journalism anchor only; does not substitute
> for the missing primary Western Union corporate disclosure.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`wikileaks-paypal-freeze-2010-12`](./wikileaks-paypal-freeze-2010-12.md)
- [`wikileaks-mastercard-suspension-2010-12`](./wikileaks-mastercard-suspension-2010-12.md)
- [`wikileaks-visa-europe-suspension-2010-12`](./wikileaks-visa-europe-suspension-2010-12.md)
- [`wikileaks-bank-of-america-block-2010-12`](./wikileaks-bank-of-america-block-2010-12.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `cd67682`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

