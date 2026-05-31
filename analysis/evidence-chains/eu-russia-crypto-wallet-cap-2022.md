# Evidence chain — `eu-russia-crypto-wallet-cap-2022`

**Status**: `admitted` · **Stratum**: `S6_supranational` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-05-31` · **Source commit**: `b34ad1c` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-16` · **Tool version**: `0.1.0` · **Generated**: `2026-05-31T15:13:25Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "EU Council Regulation 2022/576 of 2022-04-08 (fifth sanctions package)
> inserted Article 5b into Regulation 833/2014, prohibiting EU operators
> from providing crypto-asset wallets, accounts, or custody services to
> Russian nationals / residents / Russian-established entities above an
> EUR 10,000 per-person threshold. EU-registered CASPs (Bitstamp,
> Kraken-EU, Coinbase-EU, Binance EU entities) implemented the cap within
> days. The offramp_cex layer carries the load-bearing direct-attribution
> observation; L4 frontend reactions are consistent with the cascade but
> require a Wayback-capture pass before they may anchor a separate
> observed_change row. The cap was superseded 2022-10-06 by the 8th-
> package full ban (Regulation 2022/1904)."

## 1. Trigger

- **Type**: `non_us_sanctions`
- **Actor**: `EU_Council`
- **Timestamp**: `2022-04-08 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32022R0576>
  - Wayback: <https://web.archive.org/web/2022/https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32022R0576>
  > Council Regulation (EU) 2022/576 of 8 April 2022 amending Regulation
> (EU) No 833/2014 concerning restrictive measures in view of Russia's
> actions destabilising the situation in Ukraine. Fifth EU sanctions
> package against Russia. Key crypto-relevant provision: new Article 5b
> of Regulation 833/2014 prohibits EU operators from providing crypto-
> asset wallets, accounts or custody services to Russian nationals,
> Russian residents, or legal persons / entities / bodies established
> in Russia, where the total value of crypto-assets per natural or
> legal person exceeds EUR 10,000. EUR-Lex CELEX URL is stable but
> the specific Wayback / body-hash capture has not been pinned in
> this DRYRUN authoring pass; evidence_use=contextual_unarchived
> pending re-pinning during human audit. Wayback anchor uses the
> year-prefix lookup form; the specific snapshot timestamp requires
> re-pinning during human audit before this citation may serve as
> an admission anchor in its own right. The companion eli-style URL
> https://eur-lex.europa.eu/eli/reg/2022/576/oj is equivalent.
- **`primary_legal`**
  - URL: <https://www.consilium.europa.eu/en/press/press-releases/2022/04/08/eu-adopts-fifth-round-of-sanctions-against-russia-over-its-military-aggression-against-ukraine/>
  - Wayback: <https://web.archive.org/web/2022/https://www.consilium.europa.eu/en/press/press-releases/2022/04/08/eu-adopts-fifth-round-of-sanctions-against-russia-over-its-military-aggression-against-ukraine/>
  > EU Council press release of 2022-04-08 announcing adoption of the
> fifth sanctions package. Names the EUR 10,000 crypto-asset wallet/
> account/custody cap among the new measures. Used as a corroborating
> primary anchor to Regulation 2022/576 alongside the EUR-Lex
> publication. Snapshot pinning deferred to human audit; marked
> evidence_use=contextual_unarchived. Wayback anchor uses the
> year-prefix lookup form; the specific snapshot timestamp requires
> re-pinning during human audit.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Russian nationals / residents above EUR 10,000 crypto threshold (EU CASP customers)

> Russian nationals, Russian residents, and legal persons / entities /
> bodies established in Russia, where the value of crypto-assets per
> person exceeded EUR 10,000, addressed via EU-operating crypto-asset
> service providers (CASPs / VASPs). The target is a user class
> identified through CASP KYC rather than wallet-level addresses;
> no on-chain address enumeration. Named EU-operating CASPs that
> implemented the cap within days include Bitstamp, Kraken's EU
> operations, Coinbase's EU operations, and Binance via its EU
> entities. These are recorded as implicit second-order targets
> in observations.scope_descriptor rather than enumerated in
> canonical_domains, matching the sibling eu-12th-russia-sanctions-2023
> convention.

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `direct` · Δt = 0h

**Event label**: `eu_casps_implemented_eur_10k_crypto_wallet_account_custody_cap_for_russian_persons`

**Timestamp**: `2022-04-08 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_legal`**
  - URL: <https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32022R0576>
  - Wayback: <https://web.archive.org/web/2022/https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32022R0576>
  > Council Regulation (EU) 2022/576 inserting Article 5b into
> Regulation 833/2014 is the legal instrument. The Regulation
> mandates by name that EU operators not provide crypto-asset
> wallets / accounts / custody services to Russian persons where
> total holdings per person exceed EUR 10,000. EU CASPs
> (Bitstamp, Kraken-EU, Coinbase-EU, Binance EU entities)
> implemented the cap within days, with some preemptively
> freezing affected accounts. attribution=direct because the
> Regulation text names the regulatory mandate. The
> observation window closes at 2022-10-06 when the 8th-package
> Regulation 2022/1904 superseded the EUR 10K threshold with a
> full ban (sibling event eu-russia-full-crypto-wallet-ban-2022).
> Wayback anchor uses the year-prefix lookup form; the specific
> snapshot timestamp requires re-pinning in human audit before
> this anchor may carry an admission anchor on its own;
> evidence_use=contextual_unarchived in the interim.
- **`primary_legal`**
  - URL: <https://www.consilium.europa.eu/en/press/press-releases/2022/04/08/eu-adopts-fifth-round-of-sanctions-against-russia-over-its-military-aggression-against-ukraine/>
  - Wayback: <https://web.archive.org/web/2022/https://www.consilium.europa.eu/en/press/press-releases/2022/04/08/eu-adopts-fifth-round-of-sanctions-against-russia-over-its-military-aggression-against-ukraine/>
  > EU Council 2022-04-08 press release announcing the fifth
> sanctions package; explicitly names the EUR 10,000 crypto-asset
> wallet/account/custody cap as a new measure. Corroborates the
> regulatory mandate behind the observed EU CASP implementation
> cascade. Wayback anchor uses the year-prefix lookup form; the
> specific snapshot timestamp requires re-pinning in human audit;
> evidence_use=contextual_unarchived pending that re-pin.

## 5. Honest coverage gaps

- **l4_frontend** (`not_measured`): EU-operating CASPs (Bitstamp, Kraken-EU, Coinbase-EU, Binance EU

## 7. Related events

- [`eu-12th-russia-sanctions-2023`](./eu-12th-russia-sanctions-2023.md)
- [`eu-mica-2023`](./eu-mica-2023.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `b34ad1c`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

