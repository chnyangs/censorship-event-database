# Evidence chain — `unsc-resolution-2371-dprk-crypto-2017`

**Status**: `admitted` · **Stratum**: `S6_supranational` · **Shape**: `null_event` (0 changed layer(s): none) · **Tier**: `null_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-02` · **Source commit**: `b524247` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-21` · **Tool version**: `0.1.0` · **Generated**: `2026-06-02T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "UN Security Council Resolution 2371, adopted unanimously on
> 2017-08-05, is the foundational 2017 DPRK-sanctions instrument
> whose expanded financial-institution reach (Foreign Trade Bank
> asset freeze; financial-services-as-financial-institution
> clarification) supplies the legal scaffolding subsequently used
> by the 1718 Sanctions Committee and US OFAC to frame DPRK
> crypto-laundering as sanctions evasion. Coded as null_event /
> null_case at the corpus's resolution: 2371 does not itself
> enumerate cryptocurrency addresses or virtual-asset service
> providers, and no per-event observed_change cascade is directly
> attributable to the 2017-08-05 adoption date; downstream
> Lazarus / DPRK-USDT enforcement actions are tracked as separate
> child events."

## 1. Trigger

- **Type**: `non_us_sanctions`
- **Actor**: `UN_SECURITY_COUNCIL`
- **Timestamp**: `2017-08-05 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://main.un.org/securitycouncil/en/s/res/2371-(2017)>
  - Wayback: <https://web.archive.org/web/2017/https://main.un.org/securitycouncil/en/s/res/2371-(2017)>
  > UN Security Council Resolution 2371 (2017), adopted
> unanimously by the Security Council at its 8019th meeting
> on 2017-08-05 in response to the DPRK's 2017-07-03 and
> 2017-07-28 intercontinental ballistic missile tests. The
> resolution tightens the DPRK sanctions regime by (i)
> prohibiting export of DPRK coal, iron, iron ore, seafood,
> lead and lead ore; (ii) banning new or expanded joint
> ventures and cooperative commercial entities with DPRK;
> (iii) capping the number of overseas DPRK laborers; and
> (iv) expanding financial-sector reach by clarifying that
> companies performing financial services are treated as
> financial institutions for sanctions purposes and by
> adding the DPRK Foreign Trade Bank to the asset-freeze
> list. The resolution does NOT explicitly name
> "cryptocurrency" or "virtual currency" — that explicit
> framing appears in later DPRK-track resolutions (2397
> of 2017-12-22, 2407 of 2018-03, and the 1718 Panel of
> Experts reports from 2018 onward). 2371 is included here
> as the foundational 2017 financial-sanctions instrument
> whose expanded financial-institution definition and
> Foreign Trade Bank designation supply the legal
> scaffolding subsequently used to frame DPRK crypto-
> laundering (Lazarus / APT38) as sanctions-evasion under
> the 1718 regime. Note: framing as "first UN resolution
> explicitly mentioning DPRK cryptocurrency" is NOT
> supported by the text of 2371 itself — coded conservatively
> as null_event with the historical-scaffolding rationale
> documented in analysis_notes.
- **`primary_legal`**
  - URL: <https://www.un.org/press/en/2017/sc12945.doc.htm>
  - Wayback: <https://web.archive.org/web/20170811165745/https://www.un.org/press/en/2017/sc12945.doc.htm>
  - body_hash: `sha256:7f70b59ebc0d092dc661a7dbcb88868eceb9d5485e8fb7ef7b6f6d5fedf52b2d`
  - body_path: `sources/http_captures/unsc-resolution-2371-dprk-crypto-2017/primary/web.archive.org__web-20170811165745-https-www.un.org-press-en-2017-sc12945.doc.htm__dac9628ca4.html`
  > UN Meetings Coverage SC/12945 (2017-08-05): "Security
> Council Toughens Sanctions Against Democratic People's
> Republic of Korea, Unanimously Adopting Resolution 2371
> (2017)". Press release accompanying the resolution;
> enumerates the export bans, joint-venture prohibition,
> labor cap, and financial-system tightening (Foreign Trade
> Bank asset freeze; financial-institution clarification).
> Wayback memento 20170811165745 (contemporaneous, 2017)
> captured 2026-05-21.
- **`supporting_tracker`**
  - URL: <https://www.armscontrol.org/factsheets/un-security-council-resolutions-north-korea>
  - Wayback: <https://web.archive.org/web/20240810065619/https://www.armscontrol.org/factsheets/un-security-council-resolutions-north-korea>
  - body_hash: `sha256:bd055f3a303db593e5df9bdd6c9465674dcf715aaa497d9780fb373999ae64e8`
  - body_path: `sources/http_captures/unsc-resolution-2371-dprk-crypto-2017/primary/web.archive.org__web-20240810065619-https-www.armscontrol.org-factsheets-un-security-council-resolutions-north-korea__e7136327a9.html`
  > Arms Control Association factsheet on UN Security Council
> resolutions on North Korea. Provides the canonical
> chronology placing 2371 (2017-08-05) within the DPRK
> sanctions track that subsequently extended to virtual-
> asset / cryptocurrency sanctions-evasion framing in 2018+
> Panel of Experts work. Wayback memento 20240810065619
> captured 2026-05-21.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Democratic People's Republic of Korea (DPRK)

> Class-level UNSC sanctions resolution targeting the Democratic
> People's Republic of Korea (DPRK) as the sanctioned state and,
> by operation of the 1718 Sanctions Committee framework, DPRK-
> affiliated entities and persons engaged in proliferation
> finance and sanctions-evasion. Per §7 codebook, class-level
> sanctions instruments are encoded as enumeration=subset with
> the class-level rationale documented here. Named entity
> additions in 2371 include the DPRK Foreign Trade Bank
> (asset-freeze designation). 2371 itself does not enumerate
> cryptocurrency addresses or virtual-asset service providers;
> downstream DPRK crypto-laundering operations (Lazarus Group,
> APT38) are designated under derivative US/UN actions tracked
> as separate child events (lazarus-entity-ofac-2019, lazarus-
> laundering-ofac-2020, dprk-usdt-network-ofac-2025).

## 3. Changed-layer observations (supports the scoped claim)

*No observed_change entries. This is a `null_event`; see §4 for observed_no_change evidence supporting the null claim.*

## 4. No-change observations (where applicable)

### offramp_cex — `unsc_2371_dprk_sanctions_adoption_2017`

**Window**: `2017-08-05 00:00:00+00:00` → `2018-12-31 23:59:59+00:00`

**Sources**:

- **`primary_legal`**
  - URL: <https://www.un.org/press/en/2017/sc12945.doc.htm>
  - Wayback: <https://web.archive.org/web/20170811165745/https://www.un.org/press/en/2017/sc12945.doc.htm>
  - body_hash: `sha256:7f70b59ebc0d092dc661a7dbcb88868eceb9d5485e8fb7ef7b6f6d5fedf52b2d`
  - body_path: `sources/http_captures/unsc-resolution-2371-dprk-crypto-2017/primary/web.archive.org__web-20170811165745-https-www.un.org-press-en-2017-sc12945.doc.htm__dac9628ca4.html`
  > UNSC Resolution 2371 (2017-08-05) is a class-level
> DPRK-sanctions coordination instrument. No per-event
> observed_change cascade at the offramp_cex or
> asset_onchain layers is directly attributable to the
> 2017-08-05 adoption date at the corpus's resolution.
> Downstream effects on DPRK crypto-laundering off-ramp
> flows manifest via subsequent OFAC SDN actions (Lazarus
> 2019, Lazarus laundering 2020, DPRK USDT network 2025)
> tracked as separate child events. observed_no_change /
> attribution=none per §1.1 codebook. UN press release
> SC/12945 Wayback memento 20170811165745 captured
> 2026-05-21.

## 5. Honest coverage gaps

- **asset_onchain** (`not_measured`): Class-level UNSC sanctions resolution. 2371 does not name

## 7. Related events

- [`lazarus-entity-ofac-2019`](./lazarus-entity-ofac-2019.md)
- [`lazarus-laundering-ofac-2020`](./lazarus-laundering-ofac-2020.md)
- [`dprk-usdt-network-ofac-2025`](./dprk-usdt-network-ofac-2025.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `b524247`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

