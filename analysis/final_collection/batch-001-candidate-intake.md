# Final Collection Batch 001 Candidate Intake

Batch date: 2026-05-16

Purpose: add pre-admission candidates toward the open-ended 2008+ tiered
collection frame without changing admitted paper counts. All rows enter as
`registry_status: candidate`; promotion still requires replayable trigger
archives, per-layer evidence, and coverage-denominator discipline.

## Registry Effect

Before batch:

- Raw registry rows: 126
- Distinct in-frame triggers: 53
- Admitted events: 52
- Admitted-quality milestone gap: 68 events

After batch:

- Raw registry rows: 146
- Distinct in-frame triggers: 73
- Admitted events: 52
- Admitted-quality milestone gap: 68 events

## Intake Rows

| stratum | candidates added | ids |
| --- | ---: | --- |
| S3 federal enforcement | 7 | `alphabay-hansa-doj-2017`, `bitmex-cftc-doj-2020`, `blockfi-sec-lending-2022`, `helix-doj-mixer-2020`, `kraken-sec-staking-2023`, `kucoin-doj-2024`, `sec-beaxy-platform-shutdown-2023` |
| S4 non-US state | 8 | `belgium-fsma-binance-cease-2023`, `canada-csa-binance-withdrawal-2023`, `india-fiu-offshore-vda-block-2023`, `malaysia-sc-binance-disable-2021`, `netherlands-dnb-binance-warning-2021`, `philippines-sec-binance-block-2024`, `singapore-mas-binance-services-2021`, `uk-fca-binance-markets-2021` |
| S5 corporate policy | 3 | `binance-russia-exit-commex-2023`, `okx-privacy-token-delist-2024`, `paxos-busd-nydfs-minting-stop-2023` |
| S6 supranational | 2 | `eu-russia-crypto-wallet-cap-2022`, `eu-russia-full-crypto-wallet-ban-2022` |

## Promotion Blockers

- Capture archived/local trigger anchors for all candidates before promotion.
- Split multi-target candidates, especially `india-fiu-offshore-vda-block-2023`,
  if target-level outcomes differ across Binance, KuCoin, OKX, Kraken, and
  other named offshore providers.
- For S4/S6 jurisdictional access cases, separate legal trigger evidence from
  platform implementation evidence. Do not admit on legal source alone.
- For S5 corporate rows, keep attribution conservative unless the corporate
  source names the legal/policy rationale directly.
- For `singapore-mas-binance-services-2021`, promotion is blocked until a
  replayable MAS or Binance primary/semi-primary source is captured; the current
  candidate uses secondary evidence only.

## Agent-Draft Promotions

On 2026-05-16, four S3 candidates were promoted from candidate stubs to
full `events/*.yaml` records with `status: observation_closed` and
`origin: agent_draft`:

- `kraken-sec-staking-2023`
- `blockfi-sec-lending-2022`
- `sec-beaxy-platform-shutdown-2023`
- `alphabay-hansa-doj-2017`

These rows have local HTTP captures and pass `scripts/validate.py`, but they
are not admitted paper-corpus cases until a human reviewer changes `status` to
`admitted` and `origin` to `human_reviewed`.
