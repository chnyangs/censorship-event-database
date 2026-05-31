# Evidence chain — `iceland-cbi-foreign-exchange-bitcoin-2014`

**Status**: `admitted` · **Stratum**: `S4_nation_state` · **Shape**: `null_event` (0 changed layer(s): none) · **Tier**: `null_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-05-31` · **Source commit**: `2f5abab` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-16` · **Tool version**: `0.1.0` · **Generated**: `2026-05-31T13:36:54Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> The Central Bank of Iceland (Seðlabanki Íslands) news release of
> 2014-03-19, "Significant risk attached to use of virtual currency",
> stated the CBI's interpretation that purchases of bitcoin by
> Icelandic residents are prohibited under the Iceland Foreign
> Exchange Act and the post-2008 capital-controls regime. The
> cascade surface is class-level on Icelandic residents; no
> exchange-side Iceland-resident cutoff is documented in this
> authoring pass, so offramp_cex carries an observation_kind=not_observed
> row with attribution=plausible.

## 1. Trigger

- **Type**: `nation_state_block`
- **Actor**: `IS_CBI`
- **Timestamp**: `2014-03-19 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://www.cb.is/publications/news/news/2014/03/19/Significant-risk-attached-to-use-of-virtual-currency/>
  - Wayback: <https://web.archive.org/web/20160805033808/https://www.cb.is/publications/news/news/2014/03/19/Significant-risk-attached-to-use-of-virtual-currency/>
  - body_hash: `sha256:a8490a684ca0d0dc7c6eff4d03bbbe48e886531e5016aaff0be068237083edea`
  - body_path: `sources/http_captures/iceland-cbi-foreign-exchange-bitcoin-2014/primary/web.archive.org__web-20160805033808-https-www.cb.is-publications-news-news-2014-03-19-Significant-risk-attached-to-use-of-virtual-currency__5a6c7ba2df.html`
  > Central Bank of Iceland (Seðlabanki Íslands / CBI) news release
> dated 2014-03-19 titled "Significant risk attached to use of
> virtual currency". The statement, issued in the days leading up
> to the Auroracoin (AUR) airdrop launch, examines the legal
> status of virtual currencies (bitcoin, Auroracoin) under
> Icelandic law and the Iceland Foreign Exchange Act (Act
> No. 87/1992 on Foreign Exchange, as amended after the 2008
> banking-crisis capital-controls regime). Core position
> articulated by the CBI: (1) bitcoin and Auroracoin are not
> recognised currency or legal tender in the sense of Icelandic
> law; (2) it is prohibited to engage in foreign-exchange trading
> with the electronic currency bitcoin under the Foreign Exchange
> Act, because Icelandic-resident purchases of bitcoin from
> foreign counterparties constitute movement of capital out of
> Iceland which is restricted under the post-2008 capital
> controls; (3) Icelandic residents should be cautious about
> using virtual currencies given the absence of consumer
> protection and the foreign-exchange-law exposure. The CBI is
> the only authority with rule-making power under the FX Act,
> so this statement carries the legal interpretation that
> bitcoin purchases by Icelandic residents are restricted by
> existing FX-control law. The cb.is URL path is the canonical
> publication anchor; specific Wayback snapshot timestamp
> requires re-pinning in human audit before this citation may
> serve as an admission anchor.
- **`primary_legal`**
  - URL: <https://www.sedlabanki.is/?PageId=eeebb4db-0460-11e5-93fa-005056bc0bdb&newsid=1fca32cd-af9c-11e3-93f5-005056bc0bdb>
  - Wayback: <https://web.archive.org/web/2014/https://www.sedlabanki.is/?PageId=eeebb4db-0460-11e5-93fa-005056bc0bdb&newsid=1fca32cd-af9c-11e3-93f5-005056bc0bdb>
  > Icelandic-language mirror of the same 2014-03-19 CBI news
> release on the sedlabanki.is domain. Carries identical
> substantive content to the cb.is English statement. Marked
> evidence_use=contextual_unarchived; specific Wayback snapshot
> timestamp requires re-pinning in human audit.
- **`semi_primary_wayback`**
  - URL: <https://www.loc.gov/item/global-legal-monitor/2014-08-12/iceland-national-digital-currency-auroracoin-launched/>
  - Wayback: <https://web.archive.org/web/20210725132621/https://www.loc.gov/item/global-legal-monitor/2014-08-12/iceland-national-digital-currency-auroracoin-launched/>
  - body_hash: `sha256:2ad2cf61ac52cac177460d2c601bb1c038f1edf05cc2fdb08a0598815710007a`
  - body_path: `sources/http_captures/iceland-cbi-foreign-exchange-bitcoin-2014/primary/web.archive.org__web-20210725132621-https-www.loc.gov-item-global-legal-monitor-2014-08-12-iceland-national-digital-currency-auroracoin-launched__ed151a598b.html`
  > US Library of Congress Global Legal Monitor entry titled
> "Iceland: National Digital Currency Auroracoin Launched"
> dated 2014-08-12, providing an English-language summary
> of the CBI 2014-03-19 position and characterising it as an
> interpretation of the Foreign Exchange Act restricting
> Icelandic-resident purchases of bitcoin (since such
> purchases entail capital movement out of Iceland that the
> post-2008 capital-controls regime prohibits). Used here as
> a contextual translation anchor. Specific Wayback snapshot
> timestamp requires re-pinning in human audit.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Iceland-resident bitcoin purchasers
- **Chains**: `bitcoin`

> Target is the class of Icelandic residents engaged in or
> contemplating bitcoin purchases (and by extension other virtual-
> currency purchases). The CBI statement does not enumerate
> specific exchanges or specific resident counterparties; it
> states a legal interpretation that applies to the entire class
> of Icelandic-resident bitcoin purchasers under the Foreign
> Exchange Act. No specific exchange is named as the target,
> so canonical_domains is empty.

## 3. Changed-layer observations (supports the scoped claim)

*No observed_change entries. This is a `null_event`; see §4 for observed_no_change evidence supporting the null claim.*

## 4. No-change observations (where applicable)

### offramp_cex — `no_measured_exchange_side_cutoff_of_iceland_residents`

**Window**: `2014-03-19 00:00:00+00:00` → `2014-06-17 00:00:00+00:00`

**Sources**:

- **`primary_legal`**
  - URL: <https://www.cb.is/publications/news/news/2014/03/19/Significant-risk-attached-to-use-of-virtual-currency/>
  - Wayback: <https://web.archive.org/web/20160805033808/https://www.cb.is/publications/news/news/2014/03/19/Significant-risk-attached-to-use-of-virtual-currency/>
  - body_hash: `sha256:a8490a684ca0d0dc7c6eff4d03bbbe48e886531e5016aaff0be068237083edea`
  - body_path: `sources/http_captures/iceland-cbi-foreign-exchange-bitcoin-2014/primary/web.archive.org__web-20160805033808-https-www.cb.is-publications-news-news-2014-03-19-Significant-risk-attached-to-use-of-virtual-currency__5a6c7ba2df.html`
  > The CBI 2014-03-19 statement is the legal instrument. It
> states the FX-Act interpretation that bitcoin purchases by
> Icelandic residents are prohibited under the capital-controls
> regime, but it does not name any specific exchange as having
> implemented an Iceland-resident-cutoff in response. The
> observation_kind=observed_no_change row records that the cascade
> surface at offramp_cex is class-level (Icelandic residents
> as a class) rather than exchange-specific in the available
> public record. attribution=none per §1.1 for observed_no_change. Wayback memento 20160805033808 captured 2026-05-21.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`china-pboc-crypto-ban-2013-12`](./china-pboc-crypto-ban-2013-12.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `2f5abab`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

