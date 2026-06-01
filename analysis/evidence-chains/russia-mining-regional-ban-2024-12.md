# Evidence chain — `russia-mining-regional-ban-2024-12`

**Status**: `admitted` · **Stratum**: `S4_nation_state` · **Shape**: `comparison` (1 changed layer(s): `l1_consensus`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `ad910b8` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-21` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:40:01Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> *(no scoped_claim recorded — event not paper-ready)*

## 1. Trigger

- **Type**: `nation_state_block`
- **Actor**: `RU_COUNCIL_OF_MINISTERS`
- **Timestamp**: `2024-12-23 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <http://government.ru/news/53954/>
  - Wayback: <https://web.archive.org/web/2024/http://government.ru/news/53954/>
  > Russian Federation Council of Ministers (Government /
> Pravitelstvo Rossiyskoy Federatsii) decision dated 2024-12-23
> approving the list of regions and territories where
> cryptocurrency mining is prohibited from 2025-01-01 through
> 2031-03-15 (approximately six years). The decision lists ten
> permanently banned regions: six North Caucasus federal subjects
> of the Russian Federation (Dagestan, Ingushetia, Kabardino-
> Balkaria, Karachay-Cherkessia, North Ossetia – Alania,
> Chechnya) and four Russian-administered occupied Ukrainian
> territories (the Donetsk People's Republic, the Lugansk
> People's Republic, the Zaporizhzhia oblast, and the Kherson
> oblast). The decision additionally imposes peak-season
> prohibitions in parts of the Irkutsk oblast, the Republic of
> Buryatia, and the Zabaykalsky Krai during winter peak-load
> windows (2025-01-01 to 2025-03-15 and 2025-11-15 to
> 2031-03-15). Stated rationale is preservation of the regional
> electricity-supply balance against industrial / household
> demand during peak load. The government.ru press release is
> the canonical primary-source URL; the specific Wayback snapshot
> timestamp has not been pinned in this DRYRUN authoring pass.
> Wayback anchor uses the year-prefix lookup form and requires
> human-audit re-pinning before this citation may serve as an
> admission anchor in its own right;
> evidence_use=contextual_unarchived in the interim.
- **`supporting_journalism`**
  - URL: <https://www.coindesk.com/policy/2024/12/24/russia-imposes-6-year-ban-on-crypto-mining-in-10-regions-citing-energy-use-tass>
  - Wayback: <https://web.archive.org/web/2024/https://www.coindesk.com/policy/2024/12/24/russia-imposes-6-year-ban-on-crypto-mining-in-10-regions-citing-energy-use-tass>
  > CoinDesk contemporaneous English-language coverage dated
> 2024-12-24 titled "Russia Imposes 6-Year Ban on Crypto Mining
> in 10 Regions, Citing Energy Use: Tass". Corroborates the
> 2025-01-01 to 2031-03-15 effective window, the ten-region
> enumeration, the seasonal Siberian restrictions, and the
> electricity-balance rationale. Used as a translation /
> triangulation anchor for the Russian-language primary source.
> Wayback anchor uses the year-prefix lookup form and requires
> human-audit re-pinning before any admission-anchor use;
> evidence_use=contextual_unarchived in the interim.
- **`supporting_journalism`**
  - URL: <https://meduza.io/en/news/2024/12/24/russia-bans-cryptocurrency-mining-in-the-caucasus-and-occupied-ukraine>
  - Wayback: <https://web.archive.org/web/2024/https://meduza.io/en/news/2024/12/24/russia-bans-cryptocurrency-mining-in-the-caucasus-and-occupied-ukraine>
  > Meduza English-language coverage dated 2024-12-24 titled
> "Russia bans cryptocurrency mining in the Caucasus and
> occupied Ukraine". Names the ten regions (six North Caucasus
> federal subjects plus the four Russian-administered occupied
> Ukrainian territories) and the 2025-01-01 to 2031-03-15
> window. Retained because Meduza's contemporaneous reporting
> explicitly characterizes the four Ukrainian regions as
> occupied territories under Russian administrative control,
> which is load-bearing for the target / jurisdiction modeling
> of this event. Wayback anchor uses the year-prefix lookup
> form; evidence_use=contextual_unarchived pending human-audit
> re-pinning.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Crypto-mining activity within ten Russia-administered regions (six North Caucasus + four occupied Ukrainian territories)
- **Chains**: `bitcoin`

> Canonical target is the cryptocurrency-mining activity class
> operating within the ten regions enumerated by the 2024-12-23
> Council of Ministers decision: six North Caucasus federal
> subjects of the Russian Federation (Dagestan, Ingushetia,
> Kabardino-Balkaria, Karachay-Cherkessia, North Ossetia – Alania,
> Chechnya) and four Russian-administered occupied Ukrainian
> territories (the Donetsk People's Republic, the Lugansk People's
> Republic, the Zaporizhzhia oblast, and the Kherson oblast). The
> schema target_kinds enum does not include a "regional_activity"
> or "mining_operator_class" type; entity is the closest enum for
> a regionally scoped activity-class target. enumeration=subset
> rather than complete because (i) the decision addresses a
> population class (all mining within the ten regions) rather than
> an enumerated roster of named mining operators, and (ii) the
> decision explicitly contemplates further additions to the
> restricted-region list, so the ten-region set is the initial
> subset rather than the closed universe. Three Siberian regions
> (Irkutsk, Buryatia, Zabaykalsky Krai) carry peak-season
> restrictions rather than year-round prohibitions; they are
> referenced in analysis_notes / observations but are not part of
> the canonical ten-region enumerated target set.

## 3. Changed-layer observations (supports the scoped claim)

### l1_consensus · attribution: `plausible` · Δt = 0h

**Event label**: `russia_council_of_ministers_prohibits_mining_in_ten_regions_2025_01_2031_03`

**Timestamp**: `2024-12-23 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_legal`**
  - URL: <http://government.ru/news/53954/>
  - Wayback: <https://web.archive.org/web/20250113152211/http://government.ru/news/53954/>
  - body_hash: `sha256:c7d0294cb278ade29aa4daca9a68c091f965a63fb8781f0a81181f9233785a11`
  - body_path: `sources/http_captures/russia-mining-regional-ban-2024-12/primary/web.archive.org__web-20250113152211-http-government.ru-news-53954__07e782326f.html`
  > The 2024-12-23 Council of Ministers decision is the legal
> instrument. The decision text prohibits cryptocurrency-
> mining activity (including participation in mining pools)
> within the ten enumerated regions from 2025-01-01 through
> 2031-03-15. attribution=plausible (not direct) because the
> load-bearing causal chain "policy → regional hashpower
> shutdown → global Bitcoin hashrate redistribution" requires
> quantitative mining-share evidence that has not been
> re-verified in this authoring pass; the decree text itself
> establishes the policy lever but does not by itself
> enumerate the post-ban hashrate transition. Wayback anchor
> uses the year-prefix lookup form and requires human-audit
> re-pinning before any admission-anchor use;
> evidence_use=contextual_unarchived in the interim.
- **`semi_primary_wayback`**
  - URL: <https://www.coindesk.com/policy/2024/12/24/russia-imposes-6-year-ban-on-crypto-mining-in-10-regions-citing-energy-use-tass>
  - Wayback: <https://web.archive.org/web/20241224104001/https://www.coindesk.com/policy/2024/12/24/russia-imposes-6-year-ban-on-crypto-mining-in-10-regions-citing-energy-use-tass>
  - body_hash: `sha256:9438d0dc1b5497740c7113b647c23478b3f52e305b0e60fd5001890d0744755c`
  - body_path: `sources/http_captures/russia-mining-regional-ban-2024-12/primary/web.archive.org__web-20241224104001-https-www.coindesk.com-policy-2024-12-24-russia-imposes-6-year-ban-on-crypto-mining-in-10-regions-citing-energy-use-tass__9ef5702021.html`
  > CoinDesk English-language coverage dated 2024-12-24
> corroborates the ten-region enumeration, the 2025-01-01 to
> 2031-03-15 window, the seasonal Siberian peak-load
> restrictions, and the energy-supply rationale. Retained as
> a contextual triangulation anchor for the Russian-language
> primary source; evidence_use=contextual_unarchived pending
> human-audit re-pinning of the specific Wayback snapshot.
- **`supporting_journalism`**
  - URL: <https://meduza.io/en/news/2024/12/24/russia-bans-cryptocurrency-mining-in-the-caucasus-and-occupied-ukraine>
  - Wayback: <https://web.archive.org/web/2024/https://meduza.io/en/news/2024/12/24/russia-bans-cryptocurrency-mining-in-the-caucasus-and-occupied-ukraine>
  > Meduza English-language coverage dated 2024-12-24 names the
> ten regions and characterizes the four Ukrainian regions
> (Donetsk, Lugansk, Zaporizhzhia, Kherson) as occupied
> territories under Russian administrative control. Used as
> the load-bearing translation / jurisdiction-context anchor
> for the occupied-territories subset of the regional ban.
> evidence_use=contextual_unarchived pending human-audit
> re-pinning of the specific Wayback snapshot.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`russia-cbr-crypto-payment-ban-2022`](./russia-cbr-crypto-payment-ban-2022.md)
- [`russia-cbr-bitcoin-information-letter-2014`](./russia-cbr-bitcoin-information-letter-2014.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `ad910b8`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

