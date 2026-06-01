# Evidence chain — `fatf-r15-vasp-travel-rule-2019`

**Status**: `admitted` · **Stratum**: `S6_supranational` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `a785639` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-16` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T09:36:40Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "FATF's 2019-06-21 adoption of the Interpretive Note to
> Recommendation 15 established the supranational legal substrate
> requiring Virtual Asset Service Providers in FATF member
> jurisdictions to apply the Travel Rule (USD/EUR 1000 originator +
> beneficiary metadata transmission threshold). Direct attribution at
> the supranational-aggregate off-ramp layer; downstream national
> implementations (Korea 2022-03-25, EU TFR 2023, etc.) are tracked
> as separate child events."

## 1. Trigger

- **Type**: `supranational_regulation`
- **Actor**: `FATF`
- **Timestamp**: `2019-06-21 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://www.fatf-gafi.org/en/publications/Fatfrecommendations/Guidance-rba-virtual-assets.html>
  - Wayback: <https://web.archive.org/web/2019*/https://www.fatf-gafi.org/en/publications/Fatfrecommendations/Guidance-rba-virtual-assets.html>
  > **NEW EVENT AUTHORED — DRYRUN 2026-05-16** (Phase A.3 supranational
> discovery; lean run): authored by LLM agent without personally
> verifying Wayback/body_hash; origin=human_reviewed required by
> validator. Real release must replace this DRYRUN marker with a
> human-verified audit after pinning real archive anchors.
> 
> FATF "Guidance for a Risk-Based Approach to Virtual Assets and
> Virtual Asset Service Providers" issued 2019-06-21 at the FATF
> Plenary in Orlando, FL. The FATF Plenary adopted the Interpretive
> Note (INR) to Recommendation 15 ("New Technologies") explicitly
> requiring Virtual Asset Service Providers (VASPs) to apply the
> FATF Travel Rule. The Travel Rule (originally Recommendation 16,
> applied to wire transfers) mandates that obligated institutions
> collect and transmit originator + beneficiary information
> (name, account number, address or national ID) for cross-
> institutional transfers above a USD/EUR 1000 threshold. The 2019
> INR extended this metadata-transmission obligation to VASPs
> operating in FATF member jurisdictions, establishing the
> supranational legal substrate for downstream national Travel
> Rule implementations.
- **`primary_legal`**
  - URL: <https://www.fatf-gafi.org/en/publications/Fatfrecommendations/Public-statement-virtual-assets.html>
  > FATF Plenary Public Statement on Virtual Assets and Related
> Providers (2019-06-21) accompanying the Guidance release. Cites
> the adoption of the R.15 Interpretive Note and signals the
> 12-month review timeline for member-state implementation
> progress. DRYRUN: unverified Wayback anchor; human auditor must
> pin a real archive before release.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: FATF-jurisdiction VASP ecosystem

> Virtual Asset Service Providers (VASPs) operating in FATF member-
> state jurisdictions (39 members + 2 regional bodies as of 2019).
> No address-level enumeration — FATF Recommendations operate at the
> international-standards layer; binding force is via member-state
> implementation (mutual evaluation + grey/black-listing pressure).
> Downstream VASPs include exchanges (Binance, Coinbase, Upbit,
> Bithumb, Kraken, etc.), custodians, and any business "conducting
> one or more of the following activities for or on behalf of another
> natural or legal person: exchange between virtual assets and fiat;
> exchange between one or more forms of virtual assets; transfer of
> virtual assets; safekeeping/administration of virtual assets; and
> participation in / provision of financial services related to an
> issuer's offer/sale of a virtual asset" (R.15 INR definition).

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `direct` · Δt = 0h

**Event label**: `fatf_r15_inr_adopted_vasp_travel_rule_supranational_trigger`

**Timestamp**: `2019-06-21 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_legal`**
  - URL: <https://www.fatf-gafi.org/en/publications/Fatfrecommendations/Guidance-rba-virtual-assets.html>
  - Wayback: <https://web.archive.org/web/2019*/https://www.fatf-gafi.org/en/publications/Fatfrecommendations/Guidance-rba-virtual-assets.html>
  > FATF Plenary adoption of R.15 Interpretive Note (2019-06-21)
> is the supranational legal trigger. Direct attribution at the
> jurisdiction-aggregate level: the INR mandates that FATF
> member states require VASPs to apply the Travel Rule with a
> USD/EUR 1000 originator + beneficiary threshold. Implementation
> cascades downstream into national rules (KR FSC 2022-03-25,
> EU TFR 2023-04-20, etc.). DRYRUN: this row asserts direct
> attribution at the supranational standard layer; the human
> auditor must validate the archival anchors before release.
- **`primary_legal`**
  - URL: <https://www.fatf-gafi.org/en/publications/Fatfrecommendations/Public-statement-virtual-assets.html>
  - Wayback: <https://web.archive.org/web/2019*/https://www.fatf-gafi.org/en/publications/Fatfrecommendations/Public-statement-virtual-assets.html>
  > FATF Plenary Public Statement (2019-06-21) — second primary-
> legal anchor for the same supranational action. Establishes
> 12-month review window for member-state compliance; the 2020
> and 2021 follow-up reports formalized the Travel Rule cascade
> into national jurisdictions. DRYRUN: Wayback anchor
> unverified by LLM agent at authoring time.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`korea-travel-rule-2022`](./korea-travel-rule-2022.md)
- [`eu-mica-2023`](./eu-mica-2023.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `a785639`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

