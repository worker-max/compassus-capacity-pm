# Home Health Staffing Model — Full Context & Design

> **What this is:** the complete design, decisions, and demo calibration for the
> per-discipline, per-branch home health staffing model developed for the
> Compassus capacity initiative. This is the durable memory record — a future
> session should be able to pick up the model from this file alone.
>
> **Where the working tool lives (different repo):** the interactive workbook,
> the Excel version, and the source design spec are committed in
> **`worker-max/Aethergrid`**, branch `claude/home-health-staffing-model-e7j6q6`,
> under **`docs/staffing-model/`**:
> - `staffing-workbook.html` — self-contained interactive calculator (live recompute, ADC hero, demo-populate button, per-diem/waterfall, CSV export).
> - `staffing-workbook.xlsx` — live-formula spreadsheet (opens in Excel; upload to Google Drive → Google Sheets to run live).
> - `README.md` — the design spec (source of the tables below).
>
> The Compassus repo (this repo) holds the **knowledge/PM context**; Aethergrid
> holds the **built tool**. Keep them in sync.

---

## 1. The problem (in the user's own framing)

Capacity is fundamentally a **staffing** problem. The goal is the **"Goldilocks"
headcount per discipline per market**:

- **Understaffed** → can't manage current caseloads, no room for growth, can't absorb turnover/PTO.
- **Overstaffed** → any discipline with too-high headcount runs low visits-per-clinician → poor productivity, worse branch economics, **and lower clinician income** (home clinicians are largely paid per visit/per unit of work — they bear the brunt when referrals drop or census dips).

The model **recommends; the regional leader decides.** Pull in as many factors as
possible but always leave a deliberate override lane for regional leadership to
make the final call per branch.

**Census nuance that breaks naive ratios:** branch size is measured by **average
daily census (ADC)**, but ADC overstates clinical demand. A census of 500 does
*not* mean 500 patients seen by nursing or therapy — some are PT-only elective
joints (3–4 wk), some nursing-only biweekly maintenance (catheter changes). The
averaging window for ADC is itself a philosophy choice. Census is a good starting
point, not the whole story.

---

## 1a. Connection to Compassus discovery ground truth

This model is not free-floating — it lands directly on the discovery findings in
`capacity-scheduling-summary.md` / `discovery-session.md`:

- **Answers open question #1.** Discovery flags "the point system is the undefined
  shared currency of both capacity and scheduling (CP-5)" as the gating open
  question. **§2 below defines that currency** (routine 1.0 → SOC/ROC 2.5).
- **Matches the documented benchmark.** Discovery records **30 points/week** as the
  productivity minimum and **~40–50 patients per FT RN+LPN team pair** — this model
  uses 30 pts/FTE/wk as the standard and RN 27 + LPN 24 caseload caps (≈ combined
  50), consistent with that benchmark.
- **Operationalizes CP-3.** Discovery: "SOC-capable clinician availability is the
  binding constraint on growth, distinct from routine visit capacity." The point
  weights (SOC 2.5, ROC 2.5, recert 1.75) and the growth-staging note encode the
  admission/SOC spike that precedes census build.
- **Respects the change-management reality.** Regional-leader override lane +
  "recommends, doesn't dictate" framing matches finding #6 (clinician buy-in needs
  "personal assistant, not control mechanism" + an earnings story on pay-per-visit).

## 2. Visit-Equivalent Point System (LOCKED — user-specified)

Raw visit counts hide load; weight every visit to a common currency.

| Visit type | Points |
|---|---:|
| Routine visit | 1.00 |
| Evaluation (PT/OT/ST eval) | 1.50 |
| SOC — Start of Care | 2.50 |
| Recert (OASIS primary recert) | 1.75 |
| ROC — Resumption of Care | 2.50 |
| Therapy reassessment | 1.25 |

**Productivity standard: 30 points / FTE / productive week** (user-set; may update).
Basis default: 30 = a week *actually worked*; time off handled separately at
waterfall L2.

---

## 3. Demand translation (census → discipline visit demand)

```
patients_d       = ADC × attach_rate_d × seasonality
visits_d/wk      = patients_d × visits_per_patient_per_week_d   (BLENDED across caseload)
pts_per_visit_d  = Σ (visit_type_mix_d[t] × point_weight[t])
weighted_points_d= visits_d × pts_per_visit_d × case_mix_weight
```

- **Attach rate** = % of census that discipline actually touches (solves the "500 ≠ 500 nursing" problem). Attach rates do NOT sum to 1 — one patient is counted by every discipline that touches them.
- **visits/patient/week must be BLENDED across the whole attached caseload** (includes biweekly/maintenance), NOT the active-episode peak. (See §7 correction.)
- Two intake paths: **(A) true historical patterns** (weighted ledger over a trailing window, e.g. 13 wks) or **(B) benchmark/recommended utilization** from payer-mix + case-weight (for new/data-poor branches).

**Dual ceiling:** effective need per discipline =
`max(points-driven FTE, caseload-driven FTE)`. Each clinician also has a
**caseload cap** (max patients they can *case-manage* regardless of visit
frequency) — a visit-light, coordination-heavy branch is capped by caseload, not
visits.

---

## 4. The Turnover Waterfall (per discipline)

Turnover is not a single national fudge factor — it cascades per discipline with a
**strict non-overlap contract** so layers never double-count.

```
L0  weighted demand points (per discipline)
L1  raw_work_FTE = L0 / (productivity_standard × geography_factor)   [geography folded into productivity]
     binding     = max(raw_work_FTE, caseload_FTE)                    [dual ceiling]
L2  ÷ availability          (time off for TENURED staff: PTO+holiday+sick+CEU)
L3  × (1 + ramp × turnover) (new-hire onboarding drag, SCALED BY CHURN — see §7)
L4  ÷ (1 − vacancy)         (structural open-seat share)
     = effective FT need
L5  split → FT core + Flex (per-diem/PT/contract), Flex capped by continuity-of-care
```

**Non-overlap contract:**
- **L2** = time off for people who already work here (tenured availability).
- **L3** = extra productivity loss that exists *only because* a seat turned over (new-hire ramp + preceptor drag). **Must scale with churn**, not apply flat to all staff.
- **L4** = the open seat itself.
- Orientation time counts in **L3 only**, never also L2.

**FT vs Flex split (as implemented):**
```
buffer   = eff_FT_need − binding
flex     = min(buffer × flex_share_of_buffer, eff_FT_need × continuity_cap)
FT_core  = eff_FT_need − flex
perdiem_heads = (flex × (effective_productivity / pts_per_visit)) / keepwarm_floor
final_FT = override if set, else FT_core
```

**Why per-discipline matters:** the binding risk is **time-to-fill, not turnover
frequency**. PT/OT/ST have modest turnover but long fill times → need a *deeper*
flex buffer. HHA churns hard but fills fast. RN turnover runs structurally high.

---

## 5. Modifiers, layers, and the flex pool

- **Geography / rurality** is the **single biggest lever** — a productivity multiplier on visits/day (metro ×1.00 / mixed ×0.85 / rural ×0.68). Moves headcount more than a 10-pt turnover swing. Measure via coverage sq-mi + census-tract population density (handles mixed metro/rural branches); density ↔ drive-time (windshield tax).
- **Case-mix weight** (PDGM index) scales per-visit intensity — two same-ADC branches differ by referral partnerships + demographics.
- **Seasonality** (peak/trough census multiplier; snowbird markets swing hardest).
- **On-call / 7-day coverage** = fixed obligation, ADC-independent (still to be modeled).
- **Maintain vs Grow (two-layer output):** (1) staff to protect quality at current ADC; (2) increment for budgeted growth. Grow = need at `ADC×(1+growth)` minus Maintain.
- **Growth staging (to formalize):** new census arrives as an admission/SOC spike *before* steady caseload builds, so the Grow increment should ride **PT/per-diem/contract first**, converting to FT only after demand sustains (~10 wks above flex capacity). Convert too early → strand FT clinicians on low visits when referrals dip.
- **Per-diem pool is PERISHABLE:** hire per-diem but under-utilize them → commitment decays. Size the pool from two opposing constraints: it must cover the concurrent-vacancy + PTO gap AND keep each per-diem above a **keep-warm floor** (~5 visits/wk) or they disengage. The turnover waterfall's buffer is what *sizes* this pool — the two problems solve together.
- **HHA is a DIFFERENT CURRENCY** — aide-visit units, not clinical points. Kept OUT of the clinical FTE total by design.

---

## 6. Demo defaults (researched norms — mid-size mixed metro/rural, ADC ≈ 450)

> Directionally-sane placeholders, NOT verified benchmarks. These are the values
> shipped in the tool after calibration. Ranges/rationale in the Aethergrid spec
> and the source research.

**Globals:** ADC 450 · geography 0.85 (mixed) · case-mix 1.03 · seasonality 1.00 ·
growth 7%/yr · productivity 30 pts/FTE/wk · per-diem keep-warm 5 visits/wk ·
flex share of buffer 60% · continuity flex cap 30%.

| Discipline | Attach % | Visits/pt·wk (blended) | Caseload cap | Turnover | Availability | Ramp | Vacancy | Time-to-fill |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| SN (RN) | 85 | 1.1 | 27 | 27% | 86% | 20% | 10% | 52 d |
| LPN/LVN | 20 | 1.1 | 24 | 32% | 86% | 15% | 9% | 38 d |
| PT | 65 | 1.4 | 23 | 16% | 86% | 15% | 14% | 85 d |
| PTA | 40 | 1.5 | 22 | 20% | 87% | 12% | 12% | 60 d |
| OT | 30 | 1.2 | 22 | 17% | 86% | 15% | 15% | 90 d |
| COTA | 15 | 1.4 | 20 | 20% | 87% | 12% | 13% | 60 d |
| ST/SLP | 10 | 1.0 | 28 | 16% | 86% | 15% | 16% | 100 d |
| MSW | 12 | 0.35 | 50 | 22% | 86% | 12% | 11% | 50 d |
| HHA (aide) | 30 | 2.0 | 18 | 55% | 88% | 8% | 7% | 18 d |

**Visit-type mix by discipline** (rows ≈ 1.0; RNs carry all OASIS SOC/recert/ROC;
assistants LPN/PTA/COTA legally can't assess → 100% routine; therapy carries its
own eval + reassessment):
- SN: routine .72 / SOC .10 / recert .10 / ROC .08
- PT: routine .75 / eval .13 / SOC .03 / recert .01 / reassess .08
- OT: routine .76 / eval .14 / reassess .10
- ST: routine .72 / eval .16 / reassess .12
- MSW: routine .85 / eval .15
- LPN, PTA, COTA, HHA: routine 1.00

**Other researched context:** payer mix ≈ Medicare FFS 50% / MA 35% / Medicaid 8% /
other 7% (MA runs lower visits/episode + more auth friction — a demand suppressor);
surge coverage target ≈ 85th percentile of weekly demand; stable staffing mix ≈ FT
70% / PT 12% / per-diem 13% / contract 5%; ramp-to-FT-conversion lag ≈ 10 weeks.

---

## 7. Modeling corrections already made (do NOT reintroduce)

1. **Ramp drag MUST scale with turnover.** First draft applied ramp flat to the
   whole workforce (`×(1+ramp)`), inflating totals ~3×. Correct form is
   `×(1 + ramp×turnover)` — only the churning fraction is ramping. This also
   honors the L2/L3/L4 non-overlap contract.
2. **visits/patient/week is BLENDED across caseload**, not active-episode peak.
   Using active-episode frequency (e.g. RN 2.0) over-counts because attach already
   filters to touched patients, many of whom are biweekly/maintenance. Blended RN
   ≈ 1.1.

Sanity check after corrections (demo, ADC 450, mixed geo): SN binding ≈ 22.9 FTE;
clinical FT core ≈ 81 across all 8 clinical disciplines; grow +7% adds ≈ 7 FTE;
±10% ADC swings clinical eff ≈ 87–106.

---

## 8. Decisions registry (defaults set, pending user confirmation)

| # | Item | Status |
|---|---|---|
| D1 | 30 pts = per productive week (L2 availability separate) | default set, confirm |
| D2 | Turnover lands in BOTH a modest FT buffer AND the per-diem pool | default set, confirm |
| D3 | Per-discipline productivity standards | placeholder = global 30 |
| D4 | Path-A trailing window length | placeholder 13 wks |
| D5 | ADC averaging window | placeholder 90 days |
| D6–D14 | Attach rates, caseload caps, skill-mix ratios, all turnover params, geography↔drive-time model, case-mix index construction, growth flex→FT thresholds, per-diem keep-warm floor, new visit-type weights (discharge/PRN/telehealth/HHA/MSW) | placeholders |

---

## 9. Still un-modeled (next work)

- On-call / 7-day coverage floor (fixed, ADC-independent).
- Payer-mix utilization shift (MA auth friction as a demand suppressor).
- Assistant skill-mix optimization (RN:LPN, PT:PTA, OT:COTA routing of high-point visits to licensed tier).
- Growth flex→FT conversion *schedule* (labor-form ramp, not just headcount).
- Formula-bearing xlsx export from the HTML tool (CSV export exists).
- LUPA/PDGM visit-floor dynamics, HHVBP/quality linkage, referral-source concentration risk (identified as factors; not yet in the calc).

---

## 10. How it should wire into a product (Aethergrid) later

Each input becomes a three-lane `MetricIntake` config (paste UI + Excel template +
compliance packet — no metric ships without all three). Geography/density reuse
Aethergrid's census-tract + ZIP + ACS infrastructure (`lib/census.ts`,
`lib/geo-utils.ts`, `lib/geocode.ts`). Roster/turnover intake must respect HIPAA
+ clinician-identity rules (discipline + number only, e.g. `RN-3`, never names).
