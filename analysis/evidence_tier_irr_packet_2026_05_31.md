# Evidence-tier IRR packet — codebook 4.0.0

Purpose: prepare, but not complete, the required IRR pass for the
`evidence_tier=attested_secondary` rule added in codebook 4.0.0.

This packet is intentionally blank for coder decisions. Do not compute kappa
from this file until two independent human coders have filled the decision
columns without seeing each other's labels.

Machine-readable worksheet: `analysis/evidence_tier_irr_packet_2026_05_31.csv`.
After both coders fill the `coder_a_*` and `coder_b_*` columns, run
`make evidence-tier-irr-kappa`. The command intentionally fails while the
worksheet is incomplete.

Blinding note: do not distribute the raw event YAMLs as-is for this pass,
because they contain `evidence_tier`, `evidence_caveat`, and admission notes
that leak the current label. Provide redacted event/source packets to the
coders, or have them code from independently rendered source artifacts where
the current `attested_secondary` assignment is hidden.

## Coding task

For each sampled event, independently decide:

1. `tier_ok`: should the event remain `attested_secondary` rather than
   `admission_grade` or `reject/draft`?
2. `section9_clear`: is the restriction clearly in scope under codebook §9?
3. `single_source_ok`: is the evidence caveat acceptable for the lower tier
   (at least one contemporaneous source, no direct-attribution primary-source
   requirement waived, no §1.6 asset_onchain waiver)?

Allowed values: `yes`, `no`, `unclear`.

## Stratified sample

| id | stratum | jurisdiction | trigger_type | sample_reason | coder_a_tier_ok | coder_a_section9_clear | coder_a_single_source_ok | coder_b_tier_ok | coder_b_section9_clear | coder_b_single_source_ok | notes |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `cambodia-nbc-joint-crypto-prohibition-2018-05` | S4 | KH | `nation_state_block` | flagged national ban |  |  |  |  |  |  |  |
| `china-pboc-banks-alipay-payment-channel-block-2021-06` | S4 | CN | `nation_state_block` | payment-rail restriction |  |  |  |  |  |  |  |
| `china-search-engine-social-keyword-exchange-block-2021-06` | S4 | CN | `nation_state_block` | search/social frontend restriction |  |  |  |  |  |  |  |
| `egypt-cbe-banking-law-194-2020` | S4 | EG | `nation_state_block` | legal text / ban boundary |  |  |  |  |  |  |  |
| `korea-fiu-isms-real-name-exchange-shutdown-2021-09` | S4 | KR | `regulatory_enforcement` | regulator exchange shutdown |  |  |  |  |  |  |  |
| `korea-fsc-privacy-coin-delisting-mandate-2021-03` | S4 | KR | `regulatory_enforcement` | privacy-coin mandate |  |  |  |  |  |  |  |
| `morocco-office-des-changes-crypto-ban-2017-11` | S4 | MA | `regulatory_enforcement` | flagged national ban |  |  |  |  |  |  |  |
| `taiwan-fsc-bitcoin-bank-atm-ban-2014-01` | S4 | TW | `nation_state_block` | early bank/ATM restriction |  |  |  |  |  |  |  |
| `vietnam-sbv-payment-prohibition-2017-10` | S4 | VN | `regulatory_enforcement` | official payment prohibition |  |  |  |  |  |  |  |
| `binance-uk-new-user-halt-2023-10` | S5 | UK | `corporate_policy_change` | major exchange jurisdiction restriction |  |  |  |  |  |  |  |
| `binance-eea-usdt-spot-delisting-2025-03` | S5 | EU | `corporate_policy_change` | MiCA stablecoin delisting |  |  |  |  |  |  |  |
| `bybit-canada-exit-2023-05` | S5 | CA | `corporate_policy_change` | market exit |  |  |  |  |  |  |  |
| `crypto-com-eu-usdt-stablecoin-delisting-2025-01` | S5 | EU | `corporate_policy_change` | stablecoin delisting |  |  |  |  |  |  |  |
| `okx-canada-exit-2023` | S5 | CA | `corporate_policy_change` | market exit |  |  |  |  |  |  |  |
| `orca-dex-us-frontend-block-2023-03` | S5 | US | `corporate_policy_change` | frontend geofence |  |  |  |  |  |  |  |

## Completion checklist

- [ ] Coder A completes all 45 cells.
- [ ] Coder B completes all 45 cells independently.
- [ ] Disagreements are adjudicated with written rationale.
- [ ] Cohen's kappa is computed separately for `tier_ok`, `section9_clear`,
      and `single_source_ok`.
- [ ] `analysis/NEXT_STEPS.md` is updated with the actual IRR result.
