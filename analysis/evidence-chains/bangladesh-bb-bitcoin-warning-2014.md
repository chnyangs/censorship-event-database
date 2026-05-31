# Evidence chain — `bangladesh-bb-bitcoin-warning-2014`

**Status**: `admitted` · **Stratum**: `S4_nation_state` · **Shape**: `null_event` (0 changed layer(s): none) · **Tier**: `null_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `128e1e1` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-21` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> Bangladesh Bank's 2014-09-15 warning stated that bitcoin
> transactions could constitute unauthorised acts under the
> Foreign Exchange Regulation Act 1947 and the AML/CFT statutes
> (Money Laundering Prevention Act 2012, Anti-Terrorism Act
> 2009), carrying up to 12 years' imprisonment. The cascade
> surface is class-level on Bangladeshi residents; no exchange-
> side Bangladesh-resident cutoff or falsifiable null-observation
> query is documented in this authoring pass, so offramp_cex carries
> a draft-only observation_kind=coverage_gap row with
> attribution=none.

## 1. Trigger

- **Type**: `regulatory_enforcement`
- **Actor**: `BD_BB`
- **Timestamp**: `2014-09-15 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`supporting_journalism`**
  - URL: <https://www.coindesk.com/markets/2014/09/16/bangladesh-central-bank-cryptocurrency-use-is-a-punishable-offense>
  - Wayback: <https://web.archive.org/web/2014/https://www.coindesk.com/markets/2014/09/16/bangladesh-central-bank-cryptocurrency-use-is-a-punishable-offense>
  > CoinDesk report dated 2014-09-16 ("Bangladesh Central Bank:
> Cryptocurrency Use is a 'Punishable Offense'") summarising the
> Bangladesh Bank (BB) warning issued on or around 2014-09-15.
> Core content: BB stated that transactions involving bitcoin
> and other virtual currencies could constitute unauthorised
> acts under the Foreign Exchange Regulation Act, 1947 and the
> Money Laundering Prevention Act, 2012 and the Anti-Terrorism
> Act, 2009, and that such activity could be punishable by up
> to 12 years' imprisonment. The CoinDesk article is the most
> widely cited English-language anchor for the 2014 BB warning;
> the original BB press release was not widely reproduced in
> the local Bangladeshi press in 2014. evidence_use=
> contextual_unarchived; specific Wayback snapshot timestamp
> requires re-pinning during human audit before this citation
> may serve as an admission anchor.
- **`supporting_tracker`**
  - URL: <https://www.thedailystar.net/law-our-rights/law-analysis/bitcoin-legality-in-bangladesh-bank-1602583>
  - Wayback: <https://web.archive.org/web/2020/https://www.thedailystar.net/law-our-rights/law-analysis/bitcoin-legality-in-bangladesh-bank-1602583>
  > The Daily Star (Bangladesh) law-analysis column "Bitcoin
> legality in Bangladesh Bank", providing a retrospective
> Bangladeshi-press summary of the 2014 BB warning and the
> legal-interpretation theory underpinning it. Confirms that
> BB framed bitcoin transactions as potentially violating the
> Foreign Exchange Regulation Act 1947 and the AML/CFT statutes
> (Money Laundering Prevention Act 2012, Anti-Terrorism Act
> 2009) with up-to-12-year prison exposure, but stopped short
> of declaring bitcoin per se criminal. evidence_use=
> contextual_unarchived; specific Wayback snapshot timestamp
> requires re-pinning during human audit.
- **`supporting_journalism`**
  - URL: <https://futrlaw.org/bangladesh-bank-issues-cautionary-notice-bitcoin/>
  - Wayback: <https://web.archive.org/web/2022/https://futrlaw.org/bangladesh-bank-issues-cautionary-notice-bitcoin/>
  > FutureLaw retrospective summary "Bangladesh Bank issues
> cautionary notice against Bitcoin", corroborating the BB
> 2014 warning content (Foreign Exchange Regulation Act 1947
> + AML/CFT prison exposure framing). Used as a corroborating
> secondary tracker source. evidence_use=contextual_unarchived;
> specific Wayback snapshot timestamp requires re-pinning
> during human audit.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Bangladesh-resident bitcoin transacting parties
- **Chains**: `bitcoin`

> Target is the class of Bangladeshi residents and entities
> contemplating bitcoin transactions, and by extension the
> off-ramp / centralized-exchange surface that would serve
> Bangladeshi-resident bitcoin purchases. The BB warning does
> not enumerate specific exchanges or specific resident
> counterparties; it states a legal-interpretation that applies
> to the entire class of Bangladeshi-resident bitcoin
> transacting parties under the Foreign Exchange Regulation
> Act 1947 and the AML/CFT statutes. No specific exchange is
> named as a target, so canonical_domains is empty. This
> class-level subset framing matches the sibling iceland-cbi-
> foreign-exchange-bitcoin-2014 treatment.

## 3. Changed-layer observations (supports the scoped claim)

*No observed_change entries. This is a `null_event`; see §4 for observed_no_change evidence supporting the null claim.*

## 4. No-change observations (where applicable)

### offramp_cex — `bangladesh_exchange_side_cutoff_observation_gap_after_bb_warning`

**Window**: `2014-09-15 00:00:00+00:00` → `2014-12-14 00:00:00+00:00`

**Sources**:

- **`semi_primary_wayback`**
  - URL: <https://www.coindesk.com/markets/2014/09/16/bangladesh-central-bank-cryptocurrency-use-is-a-punishable-offense>
  - Wayback: <https://web.archive.org/web/20210919030841/https://www.coindesk.com/markets/2014/09/16/bangladesh-central-bank-cryptocurrency-use-is-a-punishable-offense>
  - body_hash: `sha256:96c7da53fb1a0a7081e45e4e407866603287c96e5c9e85fa039161071f59a792`
  - body_path: `sources/http_captures/bangladesh-bb-bitcoin-warning-2014/primary/web.archive.org__web-20210919030841-https-www.coindesk.com-markets-2014-09-16-bangladesh-central-bank-cryptocurrency-use-is-a-punishable-offense__fb15df6a48.html`
  > CoinDesk 2014-09-16 report is the primary contemporaneous
> English-language anchor for the BB warning. It states the
> FX-Act and AML/CFT legal-interpretation theory and the
> up-to-12-years prison-exposure framing, but does not name
> any specific exchange as having implemented a Bangladesh-
> resident cutoff in response. The observation_kind=
> coverage_gap row records that the cascade surface at
> offramp_cex is class-level (Bangladeshi residents as a
> class) rather than exchange-specific in the available
> public record. attribution=none per §1.1 codebook for observed_no_change. Specific Wayback snapshot timestamp requires
> re-pinning in human audit.
- **`semi_primary_wayback`**
  - URL: <https://www.thedailystar.net/law-our-rights/law-analysis/bitcoin-legality-in-bangladesh-bank-1602583>
  - Wayback: <https://web.archive.org/web/20181206154558/https://www.thedailystar.net/law-our-rights/law-analysis/bitcoin-legality-in-bangladesh-bank-1602583>
  - body_hash: `sha256:80e0eac9de65abb067104aa1e5172622e2cd4856c18fdbc47603ff5c8aee0223`
  - body_path: `sources/http_captures/bangladesh-bb-bitcoin-warning-2014/primary/web.archive.org__web-20181206154558-https-www.thedailystar.net-law-our-rights-law-analysis-bitcoin-legality-in-bangladesh-bank-1602583__e4c833f165.html`
  > The Daily Star retrospective law-analysis column
> corroborates that BB framed bitcoin transactions as
> potentially violating the Foreign Exchange Regulation Act
> 1947 and the AML/CFT statutes with up-to-12-year prison
> exposure, but stopped short of declaring bitcoin per se
> criminal. Confirms class-level rather than exchange-
> specific cascade surface. Specific Wayback snapshot
> timestamp requires re-pinning in human audit.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`thailand-bot-bitcoin-prohibition-2013`](./thailand-bot-bitcoin-prohibition-2013.md)
- [`china-pboc-crypto-ban-2013-12`](./china-pboc-crypto-ban-2013-12.md)
- [`bolivia-bcb-crypto-prohibition-2014`](./bolivia-bcb-crypto-prohibition-2014.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `128e1e1`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

