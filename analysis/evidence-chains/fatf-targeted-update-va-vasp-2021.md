# Evidence chain — `fatf-targeted-update-va-vasp-2021`

**Status**: `admitted` · **Stratum**: `S6_supranational` · **Shape**: `null_event` (0 changed layer(s): none) · **Tier**: `null_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `ea43eeb` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-21` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T03:45:56Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "FATF's 2021-10-28 'Updated Guidance for a Risk-Based Approach to
> Virtual Assets and Virtual Asset Service Providers' is a class-
> level coverage extension to the 2019 R.15 INR, clarifying the
> application of FATF Standards to DeFi, NFTs, stablecoins, P2P
> transfers, and Travel Rule implementation. Coded as null_event /
> null_case at the corpus's resolution: no per-event observed_change
> cascade is directly attributable to the 2021-10-28 publication
> date; downstream member-state implementations (EU TFR 2023, OECD
> CARF 2022, national VASP rule updates) are tracked as separate
> child events."

## 1. Trigger

- **Type**: `supranational_regulation`
- **Actor**: `FATF`
- **Timestamp**: `2021-10-28 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://www.fatf-gafi.org/en/publications/Fatfrecommendations/Guidance-rba-virtual-assets-2021.html>
  - Wayback: <https://web.archive.org/web/2021*/https://www.fatf-gafi.org/en/publications/Fatfrecommendations/Guidance-rba-virtual-assets-2021.html>
  > FATF "Updated Guidance for a Risk-Based Approach to Virtual Assets
> and Virtual Asset Service Providers" issued 2021-10-28. Major
> targeted update to the 2019 R.15 INR Guidance covering six focus
> areas: (1) clarified definitions of virtual assets and VASPs,
> (2) how FATF Standards apply to stablecoins, (3) ML/TF risks and
> country-level tools for peer-to-peer (P2P) transactions,
> (4) updated VASP licensing/registration guidance, (5) Travel Rule
> implementation guidance for public and private sectors (incl.
> the "sunrise problem" of asymmetric national rollout), and
> (6) information-sharing and co-operation among VASP supervisors.
> The 2021 update also addresses DeFi and NFTs at the standards-
> application layer (functional test: control or sufficient
> influence over a VA arrangement => potential VASP scope).
- **`primary_legal`**
  - URL: <https://www.fatf-gafi.org/content/dam/fatf-gafi/guidance/Updated-Guidance-VA-VASP.pdf>
  - body_hash: `sha256:85240528438654b9adb9d0272675afdd3d4b16962ba0298a7569a4097197371c`
  - body_path: `sources/http_captures/fatf-targeted-update-va-vasp-2021/primary/www.fatf-gafi.org__content-dam-fatf-gafi-guidance-Updated-Guidance-VA-VASP.pdf__f25824de78.bin`
  > Full PDF of the 2021-10-28 Updated Guidance. Live fatf-gafi.org
> capture 2026-05-21 (no Wayback memento for this URL across
> 2021-2024; live PDF is canonical).

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: FATF-jurisdiction VASP / DeFi / stablecoin ecosystem

> Class-level coverage extension to Virtual Asset Service Providers
> (VASPs) and adjacent arrangements (DeFi, NFTs, stablecoin
> arrangements, P2P facilitators) operating in FATF member-state
> jurisdictions. Per §7 codebook, class-level regulatory guidance
> is encoded as enumeration=subset with the class-level rationale
> documented here. No address-level enumeration; binding force is
> via member-state implementation (mutual evaluation + grey-listing
> pressure). Downstream affected entities include centralized
> exchanges and custodians (Binance, Coinbase, Kraken, Upbit,
> Bithumb, Bitstamp, etc.), stablecoin issuers (Tether, Circle,
> Paxos), and any "natural or legal person … with control or
> sufficient influence" over a DeFi protocol or NFT marketplace
> (FATF functional test, 2021 Guidance §B).

## 3. Changed-layer observations (supports the scoped claim)

*No observed_change entries. This is a `null_event`; see §4 for observed_no_change evidence supporting the null claim.*

## 4. No-change observations (where applicable)

### offramp_cex — `fatf_2021_targeted_update_class_level_coverage_extension`

**Window**: `2021-10-28 00:00:00+00:00` → `2023-12-31 23:59:59+00:00`

**Sources**:

- **`primary_legal`**
  - URL: <https://www.fatf-gafi.org/content/dam/fatf-gafi/guidance/Updated-Guidance-VA-VASP.pdf>
  - body_hash: `sha256:85240528438654b9adb9d0272675afdd3d4b16962ba0298a7569a4097197371c`
  - body_path: `sources/http_captures/fatf-targeted-update-va-vasp-2021/primary/www.fatf-gafi.org__content-dam-fatf-gafi-guidance-Updated-Guidance-VA-VASP.pdf__f25824de78.bin`
  > FATF 2021-10-28 Updated Guidance PDF — class-level coverage
> extension to 2019 R.15 INR (DeFi, NFTs, stablecoins, P2P,
> Travel Rule implementation). No per-event observed_change
> cascade attributable at the corpus's resolution; downstream
> effects manifest via national implementations (EU TFR 2023,
> member-state VASP rule updates) tracked as separate child
> events. Live fatf-gafi.org PDF captured 2026-05-21.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`fatf-r15-vasp-travel-rule-2019`](./fatf-r15-vasp-travel-rule-2019.md)
- [`oecd-carf-2022`](./oecd-carf-2022.md)
- [`eu-tfr-recast-2023`](./eu-tfr-recast-2023.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `ea43eeb`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

