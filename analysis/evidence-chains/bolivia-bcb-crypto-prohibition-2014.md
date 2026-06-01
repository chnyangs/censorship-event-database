# Evidence chain — `bolivia-bcb-crypto-prohibition-2014`

**Status**: `admitted` · **Stratum**: `S4_nation_state` · **Shape**: `null_event` (0 changed layer(s): none) · **Tier**: `null_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `8726393` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-21` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:13:27Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> Banco Central de Bolivia Board Resolution No. 044/2014 (issued
> 2014-05-06) prohibited the use within Bolivia of any currency not
> issued and regulated by the Bolivian state, explicitly including
> bitcoin and a list of other electronic/virtual currencies, making
> it one of the earliest explicit nation-state-level crypto
> prohibitions. The prohibition is class-level and prospective;
> Bolivia in 2014-05 had no domestically-operated bitcoin exchange of
> meaningful scale and no point-in-time offramp/CEX cessation is
> observable. The load-bearing observation is observed_no_change at
> offramp_cex with a falsifiable 2014-05-06 to 2016-12-31 scope
> window. Historical-baseline tier; not used in main statistical
> denominators.

## 1. Trigger

- **Type**: `regulatory_enforcement`
- **Actor**: `BO_BCB`
- **Timestamp**: `2014-05-06 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_government`**
  - URL: <https://www.bcb.gob.bo/webdocs/files_noticias/NP%2062%20Uso%20de%20Monedas%20Virtuales.pdf>
  - body_hash: `sha256:9bfff6619c90767577289a870b5c5278ae432994e1f019cf510236d51e3e171d`
  - body_path: `sources/http_captures/bolivia-bcb-crypto-prohibition-2014/primary/www.bcb.gob.bo__webdocs-files_noticias-NP-2062-20Uso-20de-20Monedas-20Virtuales.pdf__251b4ea430.bin`
  > Banco Central de Bolivia press release "NP 62 — Uso de Monedas
> Virtuales" (official BCB communiqué reiterating the Resolution
> 044/2014 prohibition on non-state-issued currencies). Live
> bcb.gob.bo capture 2026-05-21 (2-page PDF). The original
> Resolucion_044_2014.pdf URL is no longer live (404) and has no
> Wayback memento; this official BCB press release is the
> primary_government anchor.
- **`primary_legal`**
  - URL: <https://www.bcb.gob.bo/webdocs/resoluciones_directorio/Resolucion_044_2014.pdf>
  - Wayback: <https://web.archive.org/web/2014/https://www.bcb.gob.bo/webdocs/resoluciones_directorio/Resolucion_044_2014.pdf>
  > Banco Central de Bolivia (BCB) Board Resolution No. 044/2014,
> issued 2014-05-06, prohibiting the use within Bolivia of any
> currency, coin, or denomination that is not issued and
> regulated by the Bolivian state (the boliviano, BOB). The
> resolution explicitly names "bitcoin" and a list of other
> electronic/virtual currencies (e.g. namecoin, peercoin,
> primecoin, feathercoin, quark) and bars their use as a means
> of payment, store of value, or unit of account in Bolivian
> commerce. The resolution is issued under BCB authority over
> the national payment system and monetary stability. Bolivia's
> 2014-05 prohibition is one of the earliest explicit nation-
> state-level bans on bitcoin and is commonly cited alongside
> the 2013-07 Thailand Bank of Thailand verbal prohibition and
> the 2013-12 PBOC Notice 2013/289 as one of the first three
> nation-state crypto-prohibition actions globally. BCB Board
> Resolution No. 082/2024 later left without effect the follow-on
> Resolution No. 144/2020 and re-enabled electronic payment
> instruments for virtual-asset purchase/sale operations; this is
> tracked below as a recovery/update anchor for the operative
> payment-system restriction, not as a textual repeal of the
> 2014 instrument itself. The bcb.gob.bo
> URL path for board resolutions is publicly indexed but specific
> Wayback snapshot timestamps for the 2014-05-06 PDF have not
> been pinned in this authoring pass. evidence_use=
> contextual_unarchived pending re-pin in a follow-up human-audit
> pass.
- **`semi_primary_wayback`**
  - URL: <https://www.cityam.com/bitcoin-banned-bolivian-central-bank-threat-national-currency/>
  - Wayback: <https://web.archive.org/web/20201112040703/https://www.cityam.com/bitcoin-banned-bolivian-central-bank-threat-national-currency/>
  - body_hash: `sha256:6562c5b3f764c25e85a4bc68ea10e8cf4af01af1253c37bcaf992f94712144ad`
  - body_path: `sources/http_captures/bolivia-bcb-crypto-prohibition-2014/primary/web.archive.org__web-20201112040703-https-www.cityam.com-bitcoin-banned-bolivian-central-bank-threat-national-currency__d6abb0b57c.html`
  > City A.M. contemporaneous (2014-06) English-language coverage
> of BCB Resolution 044/2014, naming the Banco Central de
> Bolivia, the 2014-05-06 issuance date, the list of explicitly-
> named cryptocurrencies, and the monetary-stability rationale.
> Used here as a contextual English-language anchor on the
> Spanish-language primary instrument. Specific Wayback snapshot
> timestamp requires re-pin during human audit. Marked
> evidence_use=contextual_unarchived pending that re-pin.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Bolivian users and intermediaries of non-state-issued currencies (class)
- **Chains**: `bitcoin`

> Canonical target of Resolution 044/2014 is the class of all users,
> merchants, and intermediaries within Bolivia that might use any
> non-state-issued currency (including but not limited to bitcoin
> and the explicitly-named altcoins). The resolution is class-level
> and prospective: no Bolivian crypto exchanges, payment processors,
> or specific addresses are named or designated. Bolivia in 2014-05
> had no domestically-operated bitcoin exchange of meaningful scale
> in the public record, so the prohibition operates almost entirely
> at the class / prospective level rather than against an enumerated
> set of in-country operators. enumeration=subset per codebook §7
> (class-level regulatory events use subset with rationale in
> enumeration_note; class_level is not a valid enum value).

## 3. Changed-layer observations (supports the scoped claim)

*No observed_change entries. This is a `null_event`; see §4 for observed_no_change evidence supporting the null claim.*

## 4. No-change observations (where applicable)

### offramp_cex — `bolivian_class_level_crypto_prohibition_no_observable_offramp_cascade`

**Window**: `2014-05-06 00:00:00+00:00` → `2016-12-31 23:59:59+00:00`

**Sources**:

- **`primary_government`**
  - URL: <https://www.bcb.gob.bo/webdocs/files_noticias/NP%2062%20Uso%20de%20Monedas%20Virtuales.pdf>
  - body_hash: `sha256:9bfff6619c90767577289a870b5c5278ae432994e1f019cf510236d51e3e171d`
  - body_path: `sources/http_captures/bolivia-bcb-crypto-prohibition-2014/primary/www.bcb.gob.bo__webdocs-files_noticias-NP-2062-20Uso-20de-20Monedas-20Virtuales.pdf__251b4ea430.bin`
  > BCB Resolution 044/2014 is the legal instrument. observation_
> kind=coverage_gap with attribution=none honestly represents
> the empirical posture: the prohibition is class-level and
> prospective, and no domestically-operated Bolivian bitcoin
> exchange of meaningful scale existed in 2014-05 to cease
> operating in response. The scope_descriptor records the
> falsifiable 2014-05-06 to 2016-12-31 window for the class-
> level scope (Bolivian crypto-user class). observed_no_change
> anchors the null_case posture for this event
> stays draft until a human reviewer decides whether to admit
> the row as observed_no_change (which would require an
> admission-grade replayable anchor) or to retire the event
> in favor of the planned thailand-bot-bitcoin-prohibition-
> 2013 and existing china-pboc-crypto-ban-2013-12 siblings
> carrying the historical-baseline first-touch role. Provisional
> year-prefix wayback anchor pending re-pin in a follow-up
> human-audit pass.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`thailand-bot-bitcoin-prohibition-2013`](./thailand-bot-bitcoin-prohibition-2013.md)
- [`china-pboc-crypto-ban-2013-12`](./china-pboc-crypto-ban-2013-12.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `8726393`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

