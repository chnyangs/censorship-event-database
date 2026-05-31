# Evidence chain — `tether-pig-butchering-second-wave-2024`

**Status**: `admitted` · **Stratum**: `S5_corporate` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `71ac901` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-21` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "Tether's June 2024 freeze of ~$46.9M-$49.6M USDT linked to a Southeast
> Asia pig-butchering cohort traced by Chainalysis with APAC law-enforcement
> collaboration documents a second, APAC-led wave of issuer-driven scam
> freezes — distinct from the 2023 US-DOJ-led $225M freeze in lead
> jurisdiction, lead intelligence partner, cohort, magnitude, and timing —
> and confirms that the DOJ-request-driven mode of stablecoin compliance
> generalises to non-US national / regional law-enforcement requests."

## 1. Trigger

- **Type**: `corporate_policy_change`
- **Actor**: `tether_usdt_issuer`
- **Timestamp**: `2024-06-01 00:00:00+00:00` (precision: `week`)

### Trigger citations

- **`semi_primary_measurement`**
  - URL: <https://www.chainalysis.com/blog/apac-law-enforcement-freezes-pig-butchering-funds-august-2025/>
  - Wayback: <https://web.archive.org/web/20250901072225/https://www.chainalysis.com/blog/apac-law-enforcement-freezes-pig-butchering-funds-august-2025/>
  - body_hash: `sha256:c71999bbf6bfdb3989d73fcbe74acd37581667887fd42159dc8c06061d8fca04`
  - body_path: `sources/http_captures/tether-pig-butchering-second-wave-2024/primary/web.archive.org__web-20250901000000-https-www.chainalysis.com-blog-apac-law-enforcement-freezes-pig-butchering-funds-august-2025__b74ed93cf2.html`
  > Chainalysis blog (August 2025) disclosing a June 2024 APAC-based
> law-enforcement operation in which Tether froze ~$46.9M (reported
> elsewhere as $49.6M) in USDT linked to a Southeast Asia pig-butchering
> scam cluster. Chainalysis' Crypto Investigations Solution traced
> victim deposits (Nov 2022 - Jul 2023) through intermediary wallets
> to five terminal wallets; Binance and OKX co-developed the
> intelligence; Tether executed the freeze at law-enforcement direction.
> Date split: the freeze event itself occurred in June 2024 — the blog
> states verbatim "Tether froze funds in June 2024 at the agency's
> direction" — whereas the August-2025 dateline of this Chainalysis
> post is only the retroactive public disclosure date, not the freeze
> date. The trigger.timestamp (2024-06-01, week precision) therefore
> records the June-2024 freeze, NOT the August-2025 disclosure; no
> day-level anchor exists because the operation was disclosed only
> retroactively. Distinct from tether-doj-pig-butchering-freeze-2023
> ($225M, US DOJ / USSS / EDVA civil forfeiture lead, 2023-11-20):
> different lead jurisdiction (APAC vs US), different lead intelligence
> partner (Chainalysis vs DOJ), different cohort, different magnitude,
> and different timing (June 2024 vs November 2023).
- **`semi_primary_wayback`**
  - URL: <https://www.infosecurity-magazine.com/news/crypto-freeze-47m-romance-baiting/>
  - Wayback: <https://web.archive.org/web/20250828090302/https://www.infosecurity-magazine.com/news/crypto-freeze-47m-romance-baiting/>
  - body_hash: `sha256:d4301688adf7a0396e366cc0e651035a58d433cc78f636840206edd5b14c1e60`
  - body_path: `sources/http_captures/tether-pig-butchering-second-wave-2024/primary/web.archive.org__web-20250101000000-https-www.infosecurity-magazine.com-news-crypto-freeze-47m-romance-baiting__aca160050e.html`
  > Infosecurity Magazine coverage of the Chainalysis disclosure;
> independent semi-primary anchor. Corroborates the June-2024 freeze
> timing ("froze the funds in June 2024 at its direction") and the
> ~$46.9M / $47M figure with Tether-as-actor framing and APAC law
> enforcement as the lead. Pinned Wayback memento (2025-08-28).
- **`supporting_journalism`**
  - URL: <https://crypto.news/tether-binance-chainalysis-aid-47m-pig-butchering-crackdown-in-apac/>
  - Wayback: <https://web.archive.org/web/20260516203715/https://crypto.news/tether-binance-chainalysis-aid-47m-pig-butchering-crackdown-in-apac/>
  - body_hash: `sha256:a2c10cc9935dd4cbcf9ab9d3ed1a02f4b7620e9560cdd58b2def70274146bde2`
  - body_path: `sources/http_captures/tether-pig-butchering-second-wave-2024/contextual/crypto.news__tether-binance-chainalysis-aid-47m-pig-butchering-crackdown-in-apac__2683c3a529.html`
  > crypto.news coverage of the Chainalysis disclosure; corroborates
> June 2024 freeze timing and ~$47M figure with Tether/Binance/OKX
> as crypto-firm collaborators and APAC law enforcement as the lead.
- **`supporting_journalism`**
  - URL: <https://www.theblock.co/post/368611/chainalysis-tether-binance-okx-police-freeze-nearly-50-million-usd-pig-butchering-scam-funds>
  - Wayback: <https://web.archive.org/web/20250829225833/https://www.theblock.co/post/368611/chainalysis-tether-binance-okx-police-freeze-nearly-50-million-usd-pig-butchering-scam-funds>
  - body_hash: `sha256:fca19f79138c970865c899af01ee45606796c1f02b2f6014203053b5c71516bd`
  - body_path: `sources/http_captures/tether-pig-butchering-second-wave-2024/primary/web.archive.org__web-20250901000000-https-www.theblock.co-post-368611-chainalysis-tether-binance-okx-police-freeze-nearly-50-million-usd-pig-butchering-scam-funds__25f0473f84.html`
  > The Block coverage of the Chainalysis disclosure. States verbatim
> "Tether subsequently froze the funds in June 2024 at the agency's
> direction" and records both the $49.6M total and the $46.9M
> consolidation-wallet figure, with Binance/OKX/APAC police as
> collaborators. Pinned Wayback memento (2025-08-29).
- **`supporting_journalism`**
  - URL: <https://cryptonews.com/news/tether-freezes-49-6m-in-pig-butchering-funds-chainalysis-binance-okx-join-apac-crackdown/>
  - Wayback: <https://web.archive.org/web/20250828210418/https://cryptonews.com/news/tether-freezes-49-6m-in-pig-butchering-funds-chainalysis-binance-okx-join-apac-crackdown/>
  - body_hash: `sha256:0b9424750d1d42fb1e8741b150325dec44eabcab229ab18282c4c95779b9d852`
  - body_path: `sources/http_captures/tether-pig-butchering-second-wave-2024/primary/web.archive.org__web-20250901000000-https-cryptonews.com-news-tether-freezes-49-6m-in-pig-butchering-funds-chainalysis-binance-okx-join-apac-crackdown__19be29660e.html`
  > cryptonews.com coverage of the Chainalysis disclosure. States
> "Tether froze the funds in June 2024 at the request of Asia-Pacific
> (APAC) authorities" and records the $49.6M total and $46.9M
> consolidation-wallet figure. Pinned Wayback memento (2025-08-28).

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Southeast Asia pig-butchering scam cluster (APAC 2024 cohort)
- **Chains**: `tron`, `ethereum`

> Pig-butchering scam cluster operating from Southeast Asia; Chainalysis
> traced funds to five terminal wallets after passing through intermediary
> wallets. Eight victim deposits funded eight scammer-controlled wallets
> between November 2022 and July 2023. Public disclosure does not
> enumerate the specific on-chain addresses, so the target set is
> subset-enumerable in principle (via Chainalysis case file) but not
> primary-source enumerable here. This is the same broad class of target
> (pig-butchering scam wallet cluster) as the 2023 sibling event but a
> distinct cohort identified by a different intelligence lead.

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `plausible` · Δt = 0h

**Event label**: `tether_froze_apac_pig_butchering_cohort_june_2024`

**Timestamp**: `2024-06-01 00:00:00+00:00` (precision: `week`)

**Sources**:

- **`semi_primary_measurement`**
  - URL: <https://www.chainalysis.com/blog/apac-law-enforcement-freezes-pig-butchering-funds-august-2025/>
  - Wayback: <https://web.archive.org/web/20250901072225/https://www.chainalysis.com/blog/apac-law-enforcement-freezes-pig-butchering-funds-august-2025/>
  - body_hash: `sha256:c71999bbf6bfdb3989d73fcbe74acd37581667887fd42159dc8c06061d8fca04`
  - body_path: `sources/http_captures/tether-pig-butchering-second-wave-2024/primary/web.archive.org__web-20250901000000-https-www.chainalysis.com-blog-apac-law-enforcement-freezes-pig-butchering-funds-august-2025__b74ed93cf2.html`
  > Chainalysis blog post explicitly states Tether froze the cohort
> funds in June 2024 at APAC law enforcement's direction following
> Chainalysis-Binance-OKX-developed intelligence. Coded as
> semi_primary_measurement: Chainalysis is the lead intelligence
> partner and measurement/disclosure source, but this is still not
> a Tether-issued primary corporate freeze report. The June-2024
> freeze date is the recorded event date; the August-2025 blog
> dateline is only the retroactive disclosure.
- **`semi_primary_wayback`**
  - URL: <https://www.infosecurity-magazine.com/news/crypto-freeze-47m-romance-baiting/>
  - Wayback: <https://web.archive.org/web/20250828090302/https://www.infosecurity-magazine.com/news/crypto-freeze-47m-romance-baiting/>
  - body_hash: `sha256:d4301688adf7a0396e366cc0e651035a58d433cc78f636840206edd5b14c1e60`
  - body_path: `sources/http_captures/tether-pig-butchering-second-wave-2024/primary/web.archive.org__web-20250101000000-https-www.infosecurity-magazine.com-news-crypto-freeze-47m-romance-baiting__aca160050e.html`
  > Infosecurity Magazine independent corroboration of the June 2024
> freeze (~$46.9M / $47M figure) with Tether-as-actor framing and
> APAC law-enforcement lead. Second independent semi-primary anchor;
> pinned Wayback memento (2025-08-28).

## 5. Honest coverage gaps

- **asset_onchain** (`not_measured`): Tether's June 2024 freeze of ~$46.9M-$49.6M USDT is an asset-layer

## 7. Related events

- [`tether-doj-pig-butchering-freeze-2023`](./tether-doj-pig-butchering-freeze-2023.md)
- [`tether-retroactive-sweep-2023`](./tether-retroactive-sweep-2023.md)
- [`tether-dprk-precommit-freeze-2025`](./tether-dprk-precommit-freeze-2025.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `71ac901`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

