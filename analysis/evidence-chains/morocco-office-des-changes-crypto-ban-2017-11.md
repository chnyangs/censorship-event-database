# Evidence chain — `morocco-office-des-changes-crypto-ban-2017-11`

**Status**: `admitted` · **Stratum**: `S4_nation_state` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `210aa10` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-31` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T04:23:47Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> Morocco's Office des Changes and Bank Al-Maghrib declared on 2017-11-21 that
> cryptocurrency transactions are banned and punishable by fines under the foreign-exchange
> regulations. Effect carried at offramp_cex (observed_change, plausible) at class level.

## 1. Trigger

- **Type**: `regulatory_enforcement`
- **Actor**: `MA_OFFICE_DES_CHANGES`
- **Timestamp**: `2017-11-21 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`semi_primary_wayback`**
  - URL: <https://www.moroccoworldnews.com/2017/11/234382/bitcoin-morocco-cryptocurrencies-economy/>
  - Wayback: <https://web.archive.org/web/20171209152107/https://www.moroccoworldnews.com/2017/11/234382/bitcoin-morocco-cryptocurrencies-economy/>
  - body_hash: `sha256:6b2d52b9a56def12ee6f42bd90a723cb6e26a01d688600e74191f0c98c3c6609`
  - body_path: `sources/http_captures/morocco-office-des-changes-crypto-ban-2017-11/primary/web.archive.org__web-20171209152107-https-www.moroccoworldnews.com-2017-11-234382-bitcoin-morocco-cryptocurrencies-economy__be7ba8bf29.html`
  > Morocco World News, 2017-11-21 (archived 2017-12-09), "Bye-Bye Bitcoin:
> Morocco Bans Cryptocurrencies." Contemporaneous report that Morocco's Office
> des Changes (Foreign Exchange Office) and Bank Al-Maghrib issued a public
> statement declaring that transactions made via cryptocurrencies are banned and
> will be punishable by fines, because they violate the foreign-exchange
> regulations requiring transactions with foreign countries to pass through
> authorized intermediaries and in currencies listed by Bank Al-Maghrib.
> body_hash captured 2026-05-31.
- **`supporting_tracker`**
  - URL: <https://freemanlaw.com/cryptocurrency/morocco/>
  - Wayback: <https://web.archive.org/web/20220629151654/https://freemanlaw.com/cryptocurrency/morocco/>
  - body_hash: `sha256:e2ce724fd9274b01b6432b03be523bb8ec39ed5abdbcd8a588665432f49eeae8`
  - body_path: `sources/http_captures/morocco-office-des-changes-crypto-ban-2017-11/tracker/web.archive.org__web-20220629151654-https-freemanlaw.com-cryptocurrency-morocco__5028aded5e.html`
  > Freeman Law jurisdiction tracker corroborating that the Office des Changes
> declared cryptocurrency transactions an infraction of Morocco's foreign-
> exchange regulations, subject to penalties. Retrospective secondary tracker;
> body_hash captured 2026-05-31.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Moroccan crypto users / businesses (class)
- **Chains**: `bitcoin`

> Moroccan-resident cryptocurrency users and businesses as a class. The Office des
> Changes statement declares any transaction in virtual currency an infraction of the
> foreign-exchange regulations, subject to fines; it does not enumerate specific
> exchanges. Class-level subset framing matches sibling FX-control prohibition events;
> canonical_domains is empty.

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `plausible` · Δt = Noneh

**Event label**: `crypto_transactions_declared_illegal_with_fines_by_office_des_changes`

**Timestamp**: `2017-11-21 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`semi_primary_wayback`**
  - URL: <https://www.moroccoworldnews.com/2017/11/234382/bitcoin-morocco-cryptocurrencies-economy/>
  - Wayback: <https://web.archive.org/web/20171209152107/https://www.moroccoworldnews.com/2017/11/234382/bitcoin-morocco-cryptocurrencies-economy/>
  - body_hash: `sha256:6b2d52b9a56def12ee6f42bd90a723cb6e26a01d688600e74191f0c98c3c6609`
  - body_path: `sources/http_captures/morocco-office-des-changes-crypto-ban-2017-11/primary/web.archive.org__web-20171209152107-https-www.moroccoworldnews.com-2017-11-234382-bitcoin-morocco-cryptocurrencies-economy__be7ba8bf29.html`
  > Morocco World News 2017-11-21 (archived 2017-12-09): Office des Changes and
> Bank Al-Maghrib declared crypto transactions banned and punishable by fines
> under the FX regulations. attribution=plausible per §1.5 (contemporaneous
> report; official communiqué primary text not captured in this pass).
- **`supporting_tracker`**
  - URL: <https://freemanlaw.com/cryptocurrency/morocco/>
  - Wayback: <https://web.archive.org/web/20220629151654/https://freemanlaw.com/cryptocurrency/morocco/>
  - body_hash: `sha256:e2ce724fd9274b01b6432b03be523bb8ec39ed5abdbcd8a588665432f49eeae8`
  - body_path: `sources/http_captures/morocco-office-des-changes-crypto-ban-2017-11/tracker/web.archive.org__web-20220629151654-https-freemanlaw.com-cryptocurrency-morocco__5028aded5e.html`
  > Freeman Law tracker corroborating the FX-regulation infraction framing and
> penalties.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`vietnam-sbv-payment-prohibition-2017-10`](./vietnam-sbv-payment-prohibition-2017-10.md)
- [`nepal-nrb-bitcoin-ban-2017-08`](./nepal-nrb-bitcoin-ban-2017-08.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `210aa10`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

