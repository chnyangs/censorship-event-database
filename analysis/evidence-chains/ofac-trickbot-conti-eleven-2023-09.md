# Evidence chain — `ofac-trickbot-conti-eleven-2023-09`

**Status**: `admitted` · **Stratum**: `S1_ofac_sdn` · **Shape**: `null_event` (0 changed layer(s): none) · **Tier**: `null_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-02` · **Source commit**: `b524247` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-20` · **Tool version**: `0.1.0` · **Generated**: `2026-06-02T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "OFAC press release jy1714 of 2023-09-07, jointly with UK NCA designations
> and DOJ indictment unsealings, designated 11 Russian nationals connected
> to the Trickbot/Conti cybercrime gang — the first major US-UK joint
> cyber-financial sanctions package — producing a comparison-shape cascade
> with observed_change at offramp_cex (sanctioned-person ramp blocking)
> and asset_onchain (per-individual SDN wallet attachments)."

## 1. Trigger

- **Type**: `ofac_sdn_designation`
- **Actor**: `US_OFAC`
- **Timestamp**: `2023-09-07 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://home.treasury.gov/news/press-releases/jy1714>
  - Wayback: <https://web.archive.org/web/20230907134103/https://home.treasury.gov/news/press-releases/jy1714>
  - body_hash: `sha256:12dc6c434283c19acfc560c6883a486cd6fcca16e2121433f6ebf6bc49cc6994`
  - body_path: `sources/http_captures/ofac-trickbot-conti-eleven-2023-09/primary/web.archive.org__web-20230907134103-https-home.treasury.gov-news-press-releases-jy1714__e5c3eed7aa.html`
  > Treasury press release jy1714 (2023-09-07): "United States and
> United Kingdom Sanction Additional Members of the Russia-Based
> Trickbot Cybercrime Gang." US-UK joint action designating 11
> Russian nationals materially assisting Trickbot (with downstream
> operational ties to Conti ransomware). Concurrent DOJ unsealing
> of indictments against 9 individuals (7 overlapping with OFAC
> SDN). v0.3 audit 2026-05-20 (c) Batch C-1: Wayback memento
> 20230907134103 pinned (166112 bytes), grep verifies 52xTrickbot
> + 14xjy1714 + 6xconti + 2xTRICKBOT + 2xConti + 3xSeptember 7 +
> 3x2023-09-07. NOTE: Treasury narrative discusses crypto-extorted
> ransoms ($180M+ cumulative; £27M from 149 UK victims) but does
> NOT enumerate per-individual crypto wallet addresses.
- **`primary_legal`**
  - URL: <https://ofac.treasury.gov/recent-actions/20230907>
  - Wayback: <https://web.archive.org/web/20230907131120/https://ofac.treasury.gov/recent-actions/20230907>
  - body_hash: `sha256:1adf2e8a22657565f11873aa9d3be06aac6e764f59f691e136ff8cb4ed6503a1`
  - body_path: `sources/http_captures/ofac-trickbot-conti-eleven-2023-09/primary/web.archive.org__web-20230907131120-https-ofac.treasury.gov-recent-actions-20230907__7c77224a99.html`
  > OFAC Recent Actions page for 2023-09-07. v0.3 audit 2026-05-20:
> Wayback memento 20230907131120 pinned (85228 bytes), confirms
> SDN entries for 10 of 11 named individuals (Zhuykov, Rudenskiy,
> Putilin, Mozhaev, Loguntsov, Kurov, Khaliullin, Tsarev,
> Valiakhmetov + 1 missing/case variant). CRITICAL FINDING:
> direct grep confirms ZERO `Digital Currency Address` entries
> for any of the 11 individuals on this RA page. OFAC's standard
> practice of attaching digital-currency identifiers to SDN
> entries was NOT applied to this 2023-09-07 designation —
> likely because the per-wallet enumeration was held in OFAC's
> internal SDN-XML feed but not published on the RA page, OR
> because OFAC chose not to enumerate individual ransomware-actor
> wallets at all for this action. Either way, this event lacks
> per-wallet asset_onchain evidence and is classified as null_case.
- **`primary_legal`**
  - URL: <https://www.nationalcrimeagency.gov.uk/news/russian-ransomware-group-hit-with-new-sanctions>
  - Wayback: <https://web.archive.org/web/20230907180310/https://www.nationalcrimeagency.gov.uk/news/russian-ransomware-group-hit-with-new-sanctions>
  - body_hash: `sha256:caa78dde4a9d3e7f4dce24c93436b21573d1a24a9952446c8da0775d661b5c73`
  - body_path: `sources/http_captures/ofac-trickbot-conti-eleven-2023-09/primary/web.archive.org__web-20230907180310-https-www.nationalcrimeagency.gov.uk-news-russian-ransomware-group-hit-with-new-sanctions__517cbff75c.html`
  > UK National Crime Agency (NCA) 2023-09-07 press release
> announcing the parallel UK sanctions designation. v0.3 audit
> 2026-05-20: Wayback memento 20230907180310 pinned (16275 bytes).
- **`primary_legal`**
  - URL: <https://www.justice.gov/opa/pr/us-and-uk-disrupt-trickbot-malware>
  - Wayback: <https://web.archive.org/web/2023/https://www.justice.gov/opa/pr/us-and-uk-disrupt-trickbot-malware>
  > DOJ Office of Public Affairs 2023-09-07 press release on unsealed
> indictments. v0.3 audit 2026-05-20: CDX query returned no
> mementos for this URL form (Akamai-DOJ corpus-wide capture defect
> — see Block D evidence_repair_plan for the 5-event sister cluster
> of btc-e/hydra-doj/storm-semenov/binance/bitzlato/ripple-fincen).
> Retained as evidence_use=contextual_unarchived pending future
> URL research.
- **`supporting_journalism`**
  - URL: <https://www.bleepingcomputer.com/news/security/us-and-uk-sanction-11-trickbot-and-conti-cybercrime-gang-members/>
  - Wayback: <https://web.archive.org/web/2023/https://www.bleepingcomputer.com/news/security/us-and-uk-sanction-11-trickbot-and-conti-cybercrime-gang-members/>
  > BleepingComputer 2023-09-07 coverage corroborating the 11-designee
> US-UK joint Trickbot/Conti sanctions package, including the named
> roles (administrators, managers, developers) and the
> Trickbot-to-Conti operational transition context.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Trickbot/Conti gang — 11 Russian nationals (Andrey Zhuykov, Maksim Galochkin, Maksim Rudenskiy, Mikhail Tsarev, Dmitry Putilin, Maksim Khaliullin, Sergey Loguntsov, Alexander Mozhaev, Vadym Valiakhmetov, Artem Kurov, Mikhail Chernov)

> 11 Russian nationals materially assisting the Trickbot cybercrime group
> (with downstream Conti ransomware operational ties), designated as
> individuals on the OFAC SDN List on 2023-09-07. Subset enumeration
> because (a) per-individual digital-currency address attachments
> (if any) live in the SDN XML entries rather than the press-release page
> and have not been cross-referenced into an address_set here, and (b) the
> target population is the 11 named individuals — not the wider Trickbot
> or Conti membership. The 7-of-11 overlap with the DOJ indictments
> is referenced in the trigger note. UK NCA parallel designations against
> the same individuals create coordinated UK-side sanctioned-person
> blocking, but jurisdiction is recorded as [US] here per the per-event
> constraint scoping to the OFAC SDN designation as the trigger.

## 3. Changed-layer observations (supports the scoped claim)

*No observed_change entries. This is a `null_event`; see §4 for observed_no_change evidence supporting the null claim.*

## 4. No-change observations (where applicable)

### offramp_cex — `no_public_cex_cascade_documented_for_individual_trickbot_designees_in_14d_window`

**Window**: `2023-09-07 00:00:00+00:00` → `2023-09-21 23:59:59+00:00`

**Sources**:

- **`primary_legal`**
  - URL: <https://home.treasury.gov/news/press-releases/jy1714>
  - Wayback: <https://web.archive.org/web/20230907134103/https://home.treasury.gov/news/press-releases/jy1714>
  - body_hash: `sha256:12dc6c434283c19acfc560c6883a486cd6fcca16e2121433f6ebf6bc49cc6994`
  - body_path: `sources/http_captures/ofac-trickbot-conti-eleven-2023-09/primary/web.archive.org__web-20230907134103-https-home.treasury.gov-news-press-releases-jy1714__e5c3eed7aa.html`
  > v0.3 audit 2026-05-20: observation row recast from draft's
> observed_change direct (sanctioned-person blocking obligation)
> to observed_no_change attribution=none. Treasury jy1714 + OFAC
> RA 20230907 + UK NCA denominators substantiate the trigger
> event (11 individuals SDN-designated, USD 180M+ ransomware
> context, US-UK joint action) but absence of per-wallet
> enumeration + absence of fresh public CEX policy statement in
> 14d window = null finding. Generic sanctioned-person blocking
> obligation IS legally compelled but is not a per-event
> observable cascade (matches industry private-KYT-flagging
> pattern for individual-target SDN events).
- **`supporting_journalism`**
  - URL: <https://www.bleepingcomputer.com/news/security/us-and-uk-sanction-11-trickbot-and-conti-cybercrime-gang-members/>
  - Wayback: <https://web.archive.org/web/2023/https://www.bleepingcomputer.com/news/security/us-and-uk-sanction-11-trickbot-and-conti-cybercrime-gang-members/>
  > BleepingComputer 2023-09-07 coverage corroborating the SDN
> package. Wayback pinning deferred.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`lockbit-leader-ofac-2024`](./lockbit-leader-ofac-2024.md)
- [`matveev-ofac-2023`](./matveev-ofac-2023.md)
- [`suex-ofac-2021`](./suex-ofac-2021.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `b524247`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

