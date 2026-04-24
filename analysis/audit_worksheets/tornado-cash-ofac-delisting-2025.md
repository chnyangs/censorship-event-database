# Audit worksheet — `tornado-cash-ofac-delisting-2025`

Dataset snapshot: **v0.1.0** · cutoff `2026-04-22` · commit `8cadf3a` · generated `2026-04-24T00:30:31Z`

- **admission_tier**: `anchor_case`
- **research_stratum**: `S2_ofac_removal`
- **empirical_shape**: `cascade`
- **status**: `admitted`
- **last_verified**: `2026-04-21`
- **last_human_audit**: `—`  ← update after sign-off

## 0. How to use this worksheet

Work top-to-bottom. For each row: (a) open the cited source in a browser (or `body_path` on disk) and confirm the passage supports the claim; (b) confirm the timestamp precision is appropriate for the claim; (c) confirm the attribution (`direct` / `plausible` / `none`) is not over-stated; (d) check that `observation_kind` is correct (no-change vs change vs gap). Mark the checkbox when satisfied. Leave a NOTE line if you changed anything. Reject the row (uncheck) if the claim needs revision — do NOT stamp `last_human_audit` until every row is checked.

## 1. Trigger

- **type**: `ofac_sdn_removal`
- **actor**: `US_OFAC`
- **timestamp**: `2025-03-21 00:00:00+00:00` · precision=`—`

### Trigger citations

- [ ] citation[0]: type=`primary_legal` · url=<https://ofac.treasury.gov/recent-actions/20250321> · wayback=<https://web.archive.org/web/20260421111710/https://ofac.treasury.gov/recent-actions/20250321> · body_hash=`sha256:bb3a6660…64e4` · body_path=`sources/http_captures/tornado-cash-ofac-delisting-2025/ofac-recent-actions/ofac.treasury.gov__recent-actions-20250321__a54f76a3e2.html`  · hash_check=`ok`
- [ ] citation[1]: type=`primary_legal` · url=<https://home.treasury.gov/news/press-releases/sb0057>  · hash_check=`—`

Sign-off rules for the trigger: timestamp precision must match the citation granularity. If the SDN publishes to day precision, **do not** assert hour precision in any downstream observation's `delta_hours`.

## 2. Scoped claim (read carefully)

> "OFAC delisting of Tornado Cash on 2025-03-21 (Van Loon-litigation driven)
> is the first reverse-cascade event in the dataset, producing observed_change
> on 3 layers: L1 consensus censoring-relay share dropped ≈25pp within 14
> days; Circle USDC unblacklisted at least one historical address; and L4
> frontend access/listing partially reemerged via maintained UI paths while
> canonical-domain restoration remained incomplete. Establishes structural
> asymmetry between cascade and reverse-cascade shapes: rollback is slower and
> patchier than the original cascade."
> 

- [ ] Scoped claim does NOT overread the evidence (e.g. "the SDN caused X" when attribution is `plausible`).
- [ ] Scoped claim uses the dataset's controlled vocabulary (`observed_change` / `observed_no_change` / `plausible` / `direct`).

## 3. Observations

### 3.1 · `l4_frontend` · actor=`frontend:community_and_protocol_UIs` · event=`access_or_listing_reemerges`

- **observation_kind**: `observed_change`
- **attribution**: `direct`
- **timestamp**: `2025-03-25 14:31:33+00:00` · precision=`minute` · delta_hours=`110.53`
- **sources** (5):
  - [ ] src[0]: type=`primary_corporate` · url=<https://git.tornado.ws/tornadocash/classic-ui/commit/2437ecc426> · body_hash=`sha256:61113286…5eda` · body_path=`sources/operator_commits/tornado-cash-ofac-delisting-2025/2437ecc426.diff`  · hash_check=`ok`
  - [ ] src[1]: type=`semi_primary_measurement` · url=<https://app.tornado.cash> · wayback=<https://web.archive.org/web/20260421105831/https://tornadocash.eth.limo/> · body_hash=`sha256:7b7a330a…e216` · body_path=`sources/http_captures/tornado-cash-ofac-delisting-2025/backfill-1.3/app.tornado.cash__capture__b2ee302b2f.html`  · hash_check=`ok`
  - [ ] src[2]: type=`semi_primary_measurement` · url=<https://tornadocash.eth.limo/> · wayback=<https://web.archive.org/web/20260421105831/https://tornadocash.eth.limo/> · body_hash=`sha256:7b7a330a…e216` · body_path=`sources/http_captures/tornado-cash-ofac-delisting-2025/backfill-1.3/tornadocash.eth.limo__capture__158c013abd.html`  · hash_check=`ok`
  - [ ] src[3]: type=`semi_primary_measurement` · url=<https://github.com/tornadocash> · wayback=<https://web.archive.org/web/20260421105622/https://github.com/tornadocash> · body_hash=`sha256:d690ed08…fc7a` · body_path=`sources/http_captures/tornado-cash-ofac-delisting-2025/backfill-1.3/github.com__tornadocash__7f33190afd.html`  · hash_check=`ok`
  - [ ] src[4]: type=`semi_primary_measurement` · url=<https://github.com/tornadocash/tornado-core> · wayback=<https://web.archive.org/web/20260421105714/https://github.com/tornadocash/tornado-core> · body_hash=`sha256:eae716bb…8900` · body_path=`sources/http_captures/tornado-cash-ofac-delisting-2025/backfill-1.3/github.com__tornadocash-tornado-core__9430a15343.html`  · hash_check=`ok`

Audit checks:
- [ ] Passage in each cited source supports `observed_change` for this layer.
- [ ] Attribution `direct` is not over-stated (`direct` requires primary_* source corroborating the causal link).
- [ ] Timestamp precision is sufficient for any `delta_hours` downstream claim (day-precision → NO hour claim).
- [ ] The cited evidence rules out the observed change being caused by an unrelated ecosystem-level shift (especially for `direct` attribution).
- [ ] NOTE: _free-form audit note (if the row was revised)_

### 3.2 · `asset_onchain` · actor=`circle_usdc` · event=`address_unblacklisted`

- **observation_kind**: `observed_change`
- **attribution**: `direct`
- **timestamp**: `2025-03-22 01:22:00+00:00` · precision=`minute` · delta_hours=`25.37`
- **sources** (2):
  - [ ] src[0]: type=`primary_onchain` · url=<https://etherscan.io/tx/0x1c2fbd8b25f201327e0b469164ab753c89a802de7e0768e4e278d224cc10b25a>  · hash_check=`—`
  - [ ] src[1]: type=`supporting_community` · url=<https://usdtbanlist.com/address/0x47CE0C6eD5B0Ce3d3A51fdb1C52DC66a7c3c2936> · wayback=<https://web.archive.org/web/20260421105924/https://usdtbanlist.com/address/0x47CE0C6eD5B0Ce3d3A51fdb1C52DC66a7c3c2936> · body_hash=`sha256:796e5667…3363` · body_path=`sources/http_captures/tornado-cash-ofac-delisting-2025/backfill-1.3/usdtbanlist.com__address-0x47CE0C6eD5B0Ce3d3A51fdb1C52DC66a7c3c2936__a06f6feca5.html`  · hash_check=`ok`

Audit checks:
- [ ] Passage in each cited source supports `observed_change` for this layer.
- [ ] Attribution `direct` is not over-stated (`direct` requires primary_* source corroborating the causal link).
- [ ] Timestamp precision is sufficient for any `delta_hours` downstream claim (day-precision → NO hour claim).
- [ ] The cited evidence rules out the observed change being caused by an unrelated ecosystem-level shift (especially for `direct` attribution).
- [ ] NOTE: _free-form audit note (if the row was revised)_

### 3.3 · `l3_rpc` · actor=`mev_blocker_rpc_provider` · event=`mev_blocker_filter_list_in_effect_no_step_change_attributable_to_this_event`

- **observation_kind**: `observed_no_change`
- **attribution**: `none`
- **timestamp**: `2025-03-21 00:00:00+00:00` · precision=`day` · delta_hours=`0`
- **window**: `2025-03-21 00:00:00+00:00` → `2025-03-21 23:59:59+00:00`
- **sources** (2):
  - [ ] src[0]: type=`primary_corporate` · url=<https://web.archive.org/web/20250111000329/https://mevblocker.io/> · wayback=<https://web.archive.org/web/20250111000329/https://mevblocker.io/> · body_hash=`sha256:0d2b4d7e…bda3` · body_path=`sources/http_captures/_shared/l3-rpc-filter-list/web.archive.org__web-20250601000000-mevblocker.io__8282802587.html` · scope_descriptor=(3 keys)  · hash_check=`ok`
  - [ ] src[1]: type=`primary_corporate` · url=<https://docs.flashbots.net/flashbots-protect/quick-start> · body_hash=`sha256:b937ed96…7282` · body_path=`sources/http_captures/_shared/l3-rpc-filter-list/docs.flashbots.net__flashbots-protect-quick-start__362faba1ef.html`  · hash_check=`ok`

Audit checks:
- [ ] Passage in each cited source supports `observed_no_change` for this layer.
- [ ] Attribution `none` is not over-stated (`direct` requires primary_* source corroborating the causal link).
- [ ] Timestamp precision is sufficient for any `delta_hours` downstream claim (day-precision → NO hour claim).
- [ ] `observed_no_change` is bounded by a `window` and at least one falsifiable evidence anchor (query_hash / measurement_ids / body_hash+body_path / scope_descriptor).
- [ ] `attribution` is `none` (no causal claim under null observation).
- [ ] NOTE: _free-form audit note (if the row was revised)_

### 3.4 · `l1_consensus` · actor=`pbs_relay_ecosystem_aggregate` · event=`censoring_relay_share_dropped_post_delisting`

- **observation_kind**: `observed_change`
- **attribution**: `plausible`
- **timestamp**: `2025-03-21 00:00:00+00:00` · precision=`day` · delta_hours=`0`
- **window**: `2025-03-07 00:00:00+00:00` → `2025-04-04 23:59:59+00:00`
- **sources** (2):
  - [ ] src[0]: type=`semi_primary_measurement` · url=<https://raw.githubusercontent.com/nerolation/censorship.pics/main/data/relay_censorship_share.csv> · body_hash=`sha256:45c1db9c…4567` · body_path=`sources/l1_datasets/tornado-cash-ofac-2022/relay_censorship_share.csv` · query_hash=`sha256:e3e309db…ca68` · scope_descriptor=(2 keys)  · hash_check=`ok`
  - [ ] src[1]: type=`semi_primary_measurement` · url=<https://www.relayscan.io> · wayback=<https://web.archive.org/web/20260421114750/https://www.relayscan.io/> · body_hash=`sha256:dc39f559…a827` · body_path=`sources/http_captures/tornado-cash-ofac-2022/l1-relay-dashboards/www.relayscan.io__capture__1a79bf8cec.html`  · hash_check=`ok`

Audit checks:
- [ ] Passage in each cited source supports `observed_change` for this layer.
- [ ] Attribution `plausible` is not over-stated (`direct` requires primary_* source corroborating the causal link).
- [ ] Timestamp precision is sufficient for any `delta_hours` downstream claim (day-precision → NO hour claim).
- [ ] The cited evidence rules out the observed change being caused by an unrelated ecosystem-level shift (especially for `direct` attribution).
- [ ] NOTE: _free-form audit note (if the row was revised)_

## 4. Recovery

- [ ] recovery[0]: layer=`l3_rpc` · resolved=`False` · resolved_timestamp=`—`
  - [ ] recovery layer is in `changed_layers` for this event (derived/event_metrics.json intersects recovery with changed_layers; a recovery row on a non-changed layer is silently ignored — revise or remove).
- [ ] recovery[1]: layer=`asset_onchain` · resolved=`True` · resolved_timestamp=`—`
  - [ ] recovery layer is in `changed_layers` for this event (derived/event_metrics.json intersects recovery with changed_layers; a recovery row on a non-changed layer is silently ignored — revise or remove).

## 5. Sign-off

- [ ] Every checkbox above is checked.
- [ ] Update `events/tornado-cash-ofac-delisting-2025.yaml`: set `last_human_audit: YYYY-MM-DD` to today's UTC date.
- [ ] Run `make validate` after editing; `make derived` regenerates the derived artifacts consuming `last_human_audit` semantically.
- [ ] Log the audit in `CHANGELOG.md` (one line: `audit: <slug> · <auditor-initials> · <date> · <n-row-changes>`).

If any row could not be signed off, **do not stamp** `last_human_audit`; file the specific blocker as a GitHub issue tagged `audit-blocker` and link it from the event YAML's `analysis_notes` field.
