# Evidence chain — `eu-russia-full-crypto-wallet-ban-2022`

**Status**: `admitted` · **Stratum**: `S6_supranational` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `b4a1731` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-16` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "EU Council Regulation 2022/1904 of 2022-10-06 (eighth sanctions
> package) amended Article 5b of Regulation 833/2014 to remove the
> prior EUR 10,000 per-person threshold (5th-package Regulation
> 2022/576) and impose a FULL prohibition on EU operators providing
> crypto-asset wallets, accounts, or custody services to Russian
> nationals / residents / Russian-established entities. EU-registered
> CASPs (Bitstamp, Kraken-EU, Coinbase-EU, Binance EU entities,
> Bitpanda) implemented the full ban within days/weeks. The offramp_cex
> layer carries the load-bearing direct-attribution observation; L4
> frontend reactions are consistent with the cascade but require a
> Wayback-capture pass before they may anchor a separate observed_change
> row. The full-ban regime continued through the 12th-package
> Regulation 2023/2878 (2023-12-18) Article 5aa extension."

## 1. Trigger

- **Type**: `non_us_sanctions`
- **Actor**: `EU_Council`
- **Timestamp**: `2022-10-06 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32022R1904>
  - Wayback: <https://web.archive.org/web/2022/https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32022R1904>
  > Council Regulation (EU) 2022/1904 of 6 October 2022 amending
> Regulation (EU) No 833/2014 concerning restrictive measures in view
> of Russia's actions destabilising the situation in Ukraine. Eighth
> EU sanctions package against Russia. Key crypto-relevant provision:
> amendment of Article 5b of Regulation 833/2014 removing the prior
> EUR 10,000 per-person threshold (introduced by the 5th-package
> Regulation 2022/576) and imposing a FULL prohibition on EU
> operators providing crypto-asset wallets, accounts, or custody
> services to Russian nationals, Russian residents, or legal
> persons / entities / bodies established in Russia, regardless of
> holding value. EUR-Lex CELEX URL is stable but the specific
> Wayback / body-hash capture has not been pinned in this DRYRUN
> authoring pass; evidence_use=contextual_unarchived pending
> re-pinning during human audit. Wayback anchor uses the year-prefix
> lookup form; the specific snapshot timestamp requires re-pinning
> during human audit before this citation may serve as an admission
> anchor in its own right. The companion eli-style URL
> https://eur-lex.europa.eu/eli/reg/2022/1904/oj is equivalent.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Russian nationals / residents / Russian-established entities (EU CASP customers, full ban, no threshold)

> Russian nationals, Russian residents, and legal persons / entities /
> bodies established in Russia, addressed via EU-operating crypto-asset
> service providers (CASPs / VASPs) without a value threshold (the
> EUR 10,000 cap was removed by this 8th-package amendment). The target
> is a user class identified through CASP KYC rather than wallet-level
> addresses; no on-chain address enumeration. Named EU-operating CASPs
> that implemented the full ban (and announced suspensions / account
> closures for Russian users) within days/weeks include Bitstamp,
> Kraken's EU operations, Coinbase's EU operations, Binance via its EU
> entities, and Bitpanda. These are recorded as implicit second-order
> targets in observations.scope_descriptor rather than enumerated in
> canonical_domains, matching the sibling eu-russia-crypto-wallet-cap-2022
> and eu-12th-russia-sanctions-2023 conventions.

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `direct` · Δt = 0h

**Event label**: `eu_casps_implemented_full_crypto_wallet_account_custody_ban_for_russian_persons`

**Timestamp**: `2022-10-06 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_legal`**
  - URL: <https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32022R1904>
  - Wayback: <https://web.archive.org/web/2022/https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32022R1904>
  > Council Regulation (EU) 2022/1904 amending Article 5b of
> Regulation 833/2014 is the legal instrument. The Regulation
> mandates by name that EU operators not provide crypto-asset
> wallets / accounts / custody services to Russian persons,
> residents, or Russian-established entities, with the EUR 10,000
> threshold removed (i.e. full prohibition). EU CASPs (Bitstamp,
> Kraken-EU, Coinbase-EU, Binance EU entities, Bitpanda)
> implemented the ban within days/weeks, with account closures
> and asset-withdrawal-only modes widely reported.
> attribution=direct because the Regulation text names the
> regulatory mandate. The observation window closes at 2023-12-18
> when the 12th-package Regulation 2023/2878 amended Article 5aa
> to restate and extend the full prohibition (sibling event
> eu-12th-russia-sanctions-2023). Wayback anchor uses the
> year-prefix lookup form; the specific snapshot timestamp
> requires re-pinning in human audit before this anchor may carry
> an admission anchor on its own;
> evidence_use=contextual_unarchived in the interim.

## 5. Honest coverage gaps

- **l4_frontend** (`not_measured`): EU-operating CASPs (Bitstamp, Kraken-EU, Coinbase-EU, Binance EU

## 7. Related events

- [`eu-russia-crypto-wallet-cap-2022`](./eu-russia-crypto-wallet-cap-2022.md)
- [`eu-12th-russia-sanctions-2023`](./eu-12th-russia-sanctions-2023.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `b4a1731`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

