# Evidence chain — `germany-bafin-binance-licence-withdrawal-2023`

**Status**: `admitted` · **Stratum**: `S4_nation_state` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `4acc680` · **Schema**: `0.2.0` · **Event last_verified**: `2026-06-01` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T03:34:29Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "Binance's German BaFin crypto-custody licence application was reported
> withdrawn on 2023-07-26. The retained observation is the operator-state
> licensing-path change under Germany's pre-MiCA KWG crypto-custody
> authorisation regime. This repaired row does not claim a published BaFin
> denial, Binance.com Germany-geo frontend restriction, ISP-level block,
> on-chain asset freeze, or German banking-rail severance."

## 1. Trigger

- **Type**: `nation_state_block`
- **Actor**: `DE_BAFIN`
- **Timestamp**: `2023-07-26 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://www.bafin.de/SharedDocs/Veroeffentlichungen/EN/Merkblatt/mb_200302_kryptoverwahrgeschaeft_en>
  - body_hash: `sha256:e6024f8b49411b9a80c6db5d0d97ea71044f8bfa2c6aa8474dd0f8729ffca38f`
  - body_path: `sources/http_captures/germany-bafin-binance-licence-withdrawal-2023/bafin/www.bafin.de__SharedDocs-Veroeffentlichungen-EN-Merkblatt-mb_200302_kryptoverwahrgeschaeft_en__7735676cee.html`
  > BaFin guidance notice on the statutory definition and authorisation
> requirement for crypto custody business under KWG section 1(1a)
> sentence 2 no. 6 / section 32(1). This is the primary legal context
> for the German licence-application path, not a Binance-specific
> denial notice. Captured and pinned with body_hash/body_path during
> the 2026-06-01 source-repair pass.
- **`supporting_journalism`**
  - URL: <https://www.pymnts.com/cryptocurrency/2023/binance-retreats-germany-crypto-landscape-shifts-significantly/>
  - body_hash: `sha256:8ca3964fc655c3f17413afa3602b18b2cb2d19617a6db37e9dd34816dfc00a1a`
  - body_path: `sources/http_captures/germany-bafin-binance-licence-withdrawal-2023/primary/www.pymnts.com__cryptocurrency-2023-binance-retreats-germany-crypto-landscape-shifts-significantly__18947af64a.html`
  > PYMNTS report dated 2023-07-26 carrying a Binance spokesperson
> statement that Binance had proactively withdrawn its BaFin licence
> application and still intended to apply for appropriate licensing in
> Germany. Used as contemporaneous lower-tier attestation; no public
> BaFin Binance-specific notice is available in this row.
- **`supporting_journalism`**
  - URL: <https://www.investing.com/news/stock-market-news/binance-withdraws-application-for-crypto-license-in-germany-3134579>
  - body_hash: `sha256:ae9682d626ce853bb189e6d97a1d17805b966afa53a9c6f0aa81643bff5673a9`
  - body_path: `sources/http_captures/germany-bafin-binance-licence-withdrawal-2023/primary/www.investing.com__news-stock-market-news-binance-withdraws-application-for-crypto-license-in-germany-3134579__73c4dd7dbd.html`
  > Reuters story as syndicated by Investing.com, dated 2023-07-26,
> reporting that Binance withdrew its application for a German crypto
> licence. Used as contemporaneous corroboration for the lower-tier
> operator-withdrawal fact.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Binance (Germany-facing entities)
- **Canonical domains**: `binance.com`

> Binance group entities that had sought authorisation under the German
> KWG crypto-custody licensing regime (Kryptoverwahrgeschaeft, KWG sec.
> 1 para. 1a sentence 2 no. 6). The repaired claim is scoped to the
> application-withdrawal / no-German-licensed-Binance-offering path, not
> to a measured German retail account geofence or bank-rail cutoff.

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `plausible` · Δt = 0h

**Event label**: `binance_de_crypto_custody_licence_application_withdrawn`

**Timestamp**: `2023-07-26 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`supporting_journalism`**
  - URL: <https://www.pymnts.com/cryptocurrency/2023/binance-retreats-germany-crypto-landscape-shifts-significantly/>
  - body_hash: `sha256:8ca3964fc655c3f17413afa3602b18b2cb2d19617a6db37e9dd34816dfc00a1a`
  - body_path: `sources/http_captures/germany-bafin-binance-licence-withdrawal-2023/primary/www.pymnts.com__cryptocurrency-2023-binance-retreats-germany-crypto-landscape-shifts-significantly__18947af64a.html`
  > PYMNTS report dated 2023-07-26 carrying a Binance spokesperson
> statement that Binance had proactively withdrawn its licence
> application with BaFin. Because this is a reported spokesperson
> statement rather than a replayable Binance first-party artifact,
> the event is explicitly marked evidence_tier=attested_secondary
> and attribution is kept plausible.
- **`supporting_journalism`**
  - URL: <https://www.investing.com/news/stock-market-news/binance-withdraws-application-for-crypto-license-in-germany-3134579>
  - body_hash: `sha256:ae9682d626ce853bb189e6d97a1d17805b966afa53a9c6f0aa81643bff5673a9`
  - body_path: `sources/http_captures/germany-bafin-binance-licence-withdrawal-2023/primary/www.investing.com__news-stock-market-news-binance-withdraws-application-for-crypto-license-in-germany-3134579__73c4dd7dbd.html`
  > Reuters story as syndicated by Investing.com, dated 2023-07-26,
> reporting that Binance withdrew its application for a German
> crypto licence.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`uk-fca-binance-markets-2021`](./uk-fca-binance-markets-2021.md)
- [`netherlands-dnb-binance-warning-2021`](./netherlands-dnb-binance-warning-2021.md)
- [`belgium-fsma-binance-cease-2023`](./belgium-fsma-binance-cease-2023.md)
- [`canada-csa-binance-withdrawal-2023`](./canada-csa-binance-withdrawal-2023.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `4acc680`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

