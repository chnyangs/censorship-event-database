# Evidence chain — `eu-russia-full-crypto-wallet-ban-2022`

**Status**: `admitted` · **Stratum**: `S6_supranational` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `4ee1e3c` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-16` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T03:53:57Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "EU Council Regulation 2022/1904 of 2022-10-06 (eighth sanctions
> package) amended Article 5b of Regulation 833/2014 to remove the
> prior EUR 10,000 per-person threshold (5th-package Regulation
> 2022/576) and impose a FULL prohibition on EU operators providing
> crypto-asset wallets, accounts, or custody services to Russian
> nationals / residents / Russian-established entities. The load-bearing
> observation is the regulation-created EU CASP custody/account
> obligation at the offramp_cex layer; named-CASP frontend or
> account-closure implementation remains out of scope until separately
> pinned. The full-ban regime continued through the 12th-package
> Regulation 2023/2878 (2023-12-18) Article 5aa extension."

## 1. Trigger

- **Type**: `non_us_sanctions`
- **Actor**: `EU_Council`
- **Timestamp**: `2022-10-06 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32022R1904>
  - Wayback: <https://web.archive.org/web/2022/https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32022R1904>
  - body_hash: `sha256:b5db24a051dcc8184b6ac1b5a549fdeedbe07255bb476109e6db61b4edca9472`
  - body_path: `sources/http_captures/eu-russia-full-crypto-wallet-ban-2022/primary/eur-lex.europa.eu__legal-content-EN-TXT__c4d6e513a2.html`
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
> holding value. EUR-Lex CELEX URL captured locally and pinned with
> body_hash/body_path during the 2026-06-01 source-repair pass. The
> companion eli-style URL
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
> addresses; no on-chain address enumeration. Named downstream CASP
> implementation notices are outside this source-repair scope unless
> independently pinned; this row's target set is the legal user class
> covered by the amended Article 5b.

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `direct` · Δt = 0h

**Event label**: `eu_regulation_2022_1904_removed_crypto_wallet_threshold_for_russian_persons`

**Timestamp**: `2022-10-06 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_legal`**
  - URL: <https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32022R1904>
  - Wayback: <https://web.archive.org/web/2022/https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32022R1904>
  - body_hash: `sha256:b5db24a051dcc8184b6ac1b5a549fdeedbe07255bb476109e6db61b4edca9472`
  - body_path: `sources/http_captures/eu-russia-full-crypto-wallet-ban-2022/primary/eur-lex.europa.eu__legal-content-EN-TXT__c4d6e513a2.html`
  > Council Regulation (EU) 2022/1904 amending Article 5b of
> Regulation 833/2014 is the legal instrument. The Regulation
> mandates by name that EU operators not provide crypto-asset
> wallets / accounts / custody services to Russian persons,
> residents, or Russian-established entities, with the EUR 10,000
> threshold removed (i.e. full prohibition). attribution=direct
> because the Regulation text names the
> regulatory mandate. The observation window closes at 2023-12-18
> when the 12th-package Regulation 2023/2878 amended Article 5aa
> to restate and extend the full prohibition (sibling event
> eu-12th-russia-sanctions-2023). The EUR-Lex text is captured
> locally and pinned with body_hash/body_path.

## 5. Honest coverage gaps

- **l4_frontend** (`not_measured`): EU-operating CASPs (Bitstamp, Kraken-EU, Coinbase-EU, Binance EU

## 7. Related events

- [`eu-russia-crypto-wallet-cap-2022`](./eu-russia-crypto-wallet-cap-2022.md)
- [`eu-12th-russia-sanctions-2023`](./eu-12th-russia-sanctions-2023.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `4ee1e3c`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

