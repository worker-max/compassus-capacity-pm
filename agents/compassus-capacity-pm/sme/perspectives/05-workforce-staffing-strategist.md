# SME Perspective — Workforce / Staffing Strategist (the model math)

> Seeded v0 perspective (AI-generated from the workforce/staffing-strategist lens, grounded in the operator's
> strategy download). **To be validated with a real workforce strategist + Compassus's actual numbers.**
> Preserved verbatim per the [SME discovery framework](../sme-discovery-framework.md). All numbers below are
> **hypotheses to replace with real Compassus values.**

# Staffing-Model Logic for Market-Governed Capacity — Workforce/Staffing-Strategist Lens

Framing note: capacity is not a headcount, it is a **weighted-visit throughput** the staffing model can absorb and convert into bookable slots. Every element below is written so the 9-tab tool can compute it and an AI agent can reason from it. Units are standardized on the **weighted visit-point (WVP)** so SOCs, routines, and recerts are commensurable.

**Standard visit-point weights (default; market-tunable):**
| Visit type | WVP |
|---|---|
| SOC (RN) | 2.0 |
| SOC (PT, nursing-not-on-case) | 1.75 |
| ROC | 1.75 |
| Recert / reassessment | 1.5 |
| Routine skilled visit | 1.0 |
| Discharge visit | 1.0 |
| PRN/urgent add-on | 1.25 |

> Note: the operator's tool currently uses SOC=2.5, recert=1.75, eval=1.5, reassess=1.25, dc=1.75, routine=1.0
> (confirmed by Colin, Jul 2026). Reconcile this SME's proposed weights against the tool's confirmed table —
> the tool's values are the ones in production; treat these as a cross-check, not an override.

**Standard full-time productivity targets (WVP/clinician/week, tunable per market):**
| Discipline | Target WVP/wk | Notes |
|---|---|---|
| RN (field, blended) | 27–30 | ~25 routine-equiv |
| LPN | 30–33 | routine-heavy, no assessment load |
| SOC-dedicated RN | 22–26 | fewer visits, all high-weight + admit admin |
| PT | 27–30 | |
| PTA | 30–33 | |

---

## 1. Case-Mix-Derived Discipline Mix (RN:LPN)

- **Element:** *Assessment-Load Ratio.* Derive RN:LPN from the split between assessment/high-acuity work (RN-only) and routine skilled nursing (LPN-eligible), not from habit.
- **Trigger:** Branch design; re-run whenever payer/case mix shifts >10% or census crosses a staffing tier.
- **Why it works:** LPNs are ~15–25% cheaper per visit and cannot be the bottleneck resource — but every SOC/ROC/recert/OASIS event is RN-locked. Under-staff LPNs and RNs spend routine-visit time they can't spend admitting; admit throughput collapses.
- **Encode as system logic:**
  - Classify weekly nursing WVP into `RN_locked_WVP` (all SOC, ROC, recert, OASIS, wound/IV-high-acuity, insulin-teaching) and `LPN_eligible_WVP` (routine skilled, stable teaching, routine wound).
  - `RN_FTE_min = RN_locked_WVP / 27`
  - `LPN_FTE = LPN_eligible_WVP / 31`
  - Target **LPN coverage ratio** `L = LPN_eligible_WVP / total_nursing_WVP`. Flag if RNs are executing >20% of LPN-eligible WVP → "RN routine bleed."
  - Typical outputs: routine-heavy Medicare chronic market → RN:LPN ≈ 1:0.8–1:1.2; high-acuity/specialty market → 1:0.3.
- **Train the AI agent:** Compute RN-locked vs LPN-eligible WVP from the visit-type distribution, never from patient headcount. If RN routine-bleed >20%, recommend LPN adds before RN adds — an RN hour spent on a routine visit is an admit slot destroyed. Show the admit slots recoverable per LPN FTE added.

## 2. Case-Mix-Derived Therapy Mix (PT:PTA)

- **Element:** *Eval-Lock Ratio for therapy.* PT evals, re-evals, and the therapy SOC (when nursing not on case) are PT-locked; routine therapy visits are PTA-delegable within state practice-act limits and supervision rules.
- **Why it works:** Ortho-heavy suburban markets are eval-front-loaded then routine-tapered — ideal for PTA leverage. Under-staffing PTA drowns the PT in routine gait/strengthening and starves therapy-SOC capacity.
- **Encode as system logic:**
  - `PT_locked_WVP` = evals + re-evals + therapy-SOC + supervisory visits (per state 30-day/13th-visit reassessment rules).
  - `PT_FTE_min = PT_locked_WVP / 27`; `PTA_FTE = PTA_eligible_WVP / 31`.
  - Enforce state supervisory cadence as a hard constraint. Default cap `PTA:PT ≤ 2:1` field visits unless state allows higher.
  - Flag PT overtime + PTA idle simultaneously → mis-delegation, not under-staffing.
- **Train the AI agent:** Separate the practice-act constraint from the economic optimum. Recommend the PTA-heavy mix only up to the legal supervisory ceiling. In ortho markets push PTA leverage; in neuro/complex markets pull it back.

## 3. Census-to-Staffing Core Equation

- **Element:** *Census Staffing Solve.* The base function converting a target census into per-discipline FTE.
- **Why it works:** Census alone is meaningless without visit frequency and discipline utilization — 100 patients in a high-frequency wound market needs ~40% more nursing FTE than 100 chronic-stable patients.
- **Encode as system logic:** For each discipline *d*:
  - `Weekly_WVP_d = Census × Util_d × AvgVisitFreq_d × AvgWeight_d` (Util_d = fraction of patients using *d*, e.g. nursing 0.85, PT 0.55, OT 0.25).
  - `Required_FTE_d = Weekly_WVP_d / ProductivityTarget_d`
  - **Marginal growth staffing:** `ΔFTE_d = (ΔCensus × Util_d × AvgVisitFreq_d × AvgWeight_d) / ProductivityTarget_d`. Present as "each +25 census in *this* market requires +X.X RN, +Y.Y LPN, +Z.Z PT."
  - Round FTE **up** on assessing disciplines (RN, PT); allow fractional on PRN-backable (LPN, PTA, HHA).
- **Train the AI agent:** Never quote a staffing number without stating the utilization and visit-frequency assumptions. When asked "can we take more census," answer in marginal FTE by discipline and identify which single discipline caps the answer.

## 4. SOC-Capacity Sizing & the Known-Slots Model

- **Element:** *Dedicated SOC Capacity (bookable admit slots).* Size a protected pool of SOC-RNs (and SOC-PTs for nursing-absent referrals) so admits are scheduled slots, not scrambled interruptions.
- **Trigger:** Any market with steady referral inflow; mandatory once daily referrals ≥ ~3 or SOC same-day-compliance <90%.
- **Why it works:** SOC is the conversion event — a referral is only capacity once admitted within the timeliness window. Dedicating SOC clinicians turns admit capacity into **known, bookable daily slots** territory management can promise to referral sources.
- **Encode as system logic:**
  - `Weekly_SOC_demand = ReferralInflow/wk × AcceptRate × (1 + ROC_rate)`.
  - Apply the **SOC rule**: `RN_SOC = SOC_demand × P(nursing_on_case)`; `PT_SOC = SOC_demand × (1 − P(nursing_on_case))`.
  - SOC-RN daily capacity: `k` admits/day (default 2.5–3, includes OASIS + coordination). `SOC_RN_FTE = RN_SOC / (k × 5)`.
  - **Known-slots publish:** `DailyBookableSOCSlots = floor(SOC_RN_FTE × k) + PT_SOC_slots`, minus a reserved surge buffer (default 15%). Publish as the branch's daily admit promise.
  - Trigger a SOC-staffing add when `SOC_same_day_rate < 90%` OR `avg_admit_lag > timeliness_window` for 2+ weeks.
- **Train the AI agent:** Treat SOC capacity as inventory. Every morning surface remaining bookable admit slots and their discipline routing per the SOC rule. If lag is breaching, recommend adding SOC-dedicated capacity before generalist capacity — a bumped SOC is a lost episode. When nursing is not on a referral, route the SOC to a SOC-PT rather than defaulting to RN.

## 5. Market-Uniqueness Adjustment Factors

- **Element:** *Market Coefficient Vector.* Per-branch multipliers that bend the generic staffing solve to the specific market so the same census yields a different model.
- **Why it works:** Density, payer mix, referral-source profile, and rurality change effective productivity and mix. A rural RN drives 90 min between visits (productivity ~25–35% lower); a dense urban MA branch has lower visit frequency but higher auth friction.
- **Encode as system logic — multipliers applied to the §3 solve:**
  - **Geography/density:** `DriveFactor = productive_visit_time / (visit_time + travel_time)`. Rural `DriveFactor ≈ 0.6–0.7` → divide productivity targets by it (rural RN target may fall to ~18–20 WVP/wk).
  - **Payer/case mix:** MA/managed → `AuthFriction` (adds ~0.1–0.2 WVP/patient/wk); traditional Medicare PDGM front-loads → raise early-episode `AvgVisitFreq`.
  - **Referral-source profile:** hospital-discharge-heavy → higher acuity, higher RN-lock, higher ROC; physician-office/community → lower acuity, more LPN/PTA leverage.
  - **Seasonality:** `SeasonIndex` (snowbird +30% winter census, flu/CHF Q1 acuity spike) scales census and RN-lock; feed into per-diem reserve (§7).
  - Output a single `MarketProfile` object the cockpit stores and every other formula reads.
- **Train the AI agent:** Never port one branch's ratios to another. Read the MarketProfile first. When two branches have equal census but different models, explain the difference via DriveFactor, payer mix, and referral-source acuity — not "one is over-staffed."

## 6. Leading Indicators of a Mis-Staffed Branch

- **Element:** *Pre-Stall Signal Panel.* Metrics that move **before** census plateaus, so the tool warns while it's still fixable.
- **Why it works:** Census is a lagging indicator — by the time it stalls, referral relationships are already damaged.
- **Encode as system logic — alert thresholds:**
  - **Referral rejection/turn-down rate** > 8% (or rising 3 wks) → capacity-limited intake. *Earliest signal.*
  - **SOC same-day/timely rate** < 90% or admit lag trending up → SOC under-capacity.
  - **RN routine-bleed** > 20% of RN WVP on LPN-eligible visits → LPN gap.
  - **Assessing-clinician utilization** > 100% of target for 2+ wks → assessment bottleneck.
  - **Missed/rescheduled visit rate** > 5% → capacity fragility.
  - **PRN dependency ratio** > 15% → core-staffing gap.
  - **Recert-on-time rate** slipping → downstream overload, revenue leak.
  - Composite `MisStaffScore` = weighted sum; RN routine-bleed and referral-reject weighted highest.
- **Train the AI agent:** Watch referral-rejection rate and SOC timeliness as the two earliest tells. Alert when the *combination* fires — high rejects + rising admit lag = capacity-limited, recommend staffing; high rejects + open SOC slots = intake/relationship problem, do NOT recommend staffing. Distinguish the two before prescribing.

## 7. Per-Diem / PRN as a Managed Flex Layer

- **Element:** *Flex Reserve Sizing.* Hold a deliberate, bounded PRN pool to absorb variance — and treat over-reliance as a diagnostic for a core-staffing hole.
- **Why it works:** PRN covers seasonality, PTO, and admit surges without carrying idle core FTE. But PRN clinicians admit less reliably and cost more per visit — structural reliance signals under-hired core, especially on assessing disciplines.
- **Encode as system logic:**
  - **Target flex reserve** = `max(SeasonalPeakΔ, PTO_coverage, SOC_surge_buffer)`, default **8–12% of core WVP capacity**.
  - `PRN_dependency = PRN_WVP / total_WVP`. Bands: **≤10% healthy**, **10–15% watch**, **>15% core gap** → `Core_FTE_to_hire = (PRN_WVP − 0.10×total_WVP) / ProductivityTarget_d`.
  - Cap PRN share of **SOC/assessment** WVP hard (default ≤10%).
  - Track PRN fill-rate; if <80%, the reserve is nominal not real → treat as unstaffed.
- **Train the AI agent:** PRN is a shock absorber, not a chassis. If PRN dependency >15% for 3+ weeks, stop scheduling flex and recommend converting the recurring PRN volume into core hires, disciplined by which discipline is chronically borrowed. Never let PRN carry more than 10% of SOC work.

## 8. New-Hire Ramp Curve (Effective vs Nominal Capacity)

- **Element:** *Productivity Ramp Discount.* Count a new hire's capacity at their ramped productivity, not full target.
- **Why it works:** New field clinicians reach full productivity over 8–16 weeks (longer for OASIS-competent SOC-RNs). Planning at full target day one causes the "hired ahead of census but still missing visits" trap and burns preceptor capacity.
- **Encode as system logic:**
  - `RampFactor(week)`: **W1–2: 0.30, W3–4: 0.50, W5–8: 0.70, W9–12: 0.85, W13+: 1.0** (SOC-RN ramp ~50% longer).
  - `Effective_FTE = Σ nominal_FTE × RampFactor(current_week)`.
  - **Preceptor drag:** deduct `0.15–0.25 FTE` from the assigned senior clinician during W1–4.
  - Feed Effective_FTE (not nominal) into §3/§4 capacity and the known-slots publish.
- **Train the AI agent:** Always plan on Effective_FTE. When a manager asks when new capacity lands, give the ramp-adjusted date, and remind them of the preceptor drag on the senior clinician during weeks 1–4.

## 9. Turnover as Capacity Decay

- **Element:** *Attrition-Adjusted Standing Capacity.* Model turnover as continuous capacity leakage and pre-hire against it.
- **Why it works:** A departing clinician removes full capacity instantly and the backfill re-enters the ramp — a branch at 25% annual RN turnover runs below nominal FTE most of the year.
- **Encode as system logic:**
  - `Monthly_attrition_d = annual_turnover_d / 12`.
  - `Steady_state_capacity_d = nominal_FTE × (1 − attrition_drag)`, `attrition_drag ≈ Monthly_attrition_d × (avg_time_to_fill + ramp_weeks)/4.33`. Example: 25% annual RN turnover, 6-wk fill + 12-wk ramp → drag ≈ 8–10%.
  - **Pre-hire trigger:** maintain a pipeline so `Effective_FTE ≥ Required_FTE` net of expected attrition; open a req when projected Effective_FTE dips within 90 days.
  - Flag any discipline with turnover >20% annualized as a **capacity-integrity risk**, weighted into culture/leadership review.
- **Train the AI agent:** Quote *steady-state* capacity, not roster FTE. When recommending hires for growth, add the attrition-replacement hires needed just to hold current census. Surface high-turnover disciplines as a leadership issue, since culture is the multiplier that keeps the model from decaying.

## 10. Territory Coverage & Resting-Posture Staffing

- **Element:** *Zone Coverage Floor.* Staff each geographic sub-territory to a minimum resting posture so referrals are absorbed automatically without daily scramble.
- **Why it works:** Capacity only converts referrals if a clinician is *already positioned* in that zone. A branch can be "adequately staffed" in aggregate yet leak referrals in an under-covered corner.
- **Encode as system logic:**
  - Per zone *z*: `Zone_WVP_z` from local census + referral inflow; `Zone_floor_FTE_z = Zone_WVP_z / (ProductivityTarget_d × DriveFactor_z)` with a hard minimum of ≥1 admitting-capable clinician per active zone.
  - **Absorption check:** each zone must hold `SOC_slack_z ≥ expected_daily_referrals_z`. If a zone's slack <1, flag "coverage hole" even when branch aggregate slack is positive.
  - Balance-load directive: when zone A saturated and zone B slack, propose re-territory or cross-cover before a hire.
- **Train the AI agent:** Check capacity at the zone level, not just the branch level. A positive branch number can hide a coverage hole leaking referrals. Recommend resting-posture coverage (pre-positioned admit-capable clinicians). Only escalate to a hire after cross-cover options are exhausted.

## 11. Blended-Capacity Ceiling & Bottleneck Resolver

- **Element:** *Binding-Constraint Solver.* Compute the branch's true capacity as the **minimum** across disciplines, and name the binding discipline.
- **Why it works:** Capacity is a Liebig's-barrel problem — the branch can only admit as much as its scarcest required discipline allows. Averaging across disciplines hides the constraint.
- **Encode as system logic:**
  - For each discipline: `Slack_d = Effective_FTE_d × ProductivityTarget_d − Required_WVP_d`.
  - `Branch_capacity_headroom = min over d of Slack_d`, with SOC capacity as a parallel hard gate.
  - `BindingDiscipline = argmin Slack_d`. Publish "additional census supportable = f(BindingDiscipline slack)" and the marginal hire that lifts it.
  - Re-solve after any recommended hire to expose the *next* binding constraint.
- **Train the AI agent:** Report one capacity number — the binding constraint — and always name the discipline setting it. When recommending a hire, immediately re-solve and tell the manager what becomes the next bottleneck.

---

### How these compose (agent operating order)
1. Load `MarketProfile` (§5) → sets productivity targets, DriveFactor, utilization, seasonality.
2. Solve required FTE by discipline from census + case mix (§1–3).
3. Size SOC capacity and publish bookable admit slots per the SOC rule (§4).
4. Discount for ramp (§8) and attrition (§9) → **steady-state effective capacity**.
5. Check zone coverage (§10) and PRN dependency (§7).
6. Report the binding constraint (§11) and the pre-stall signal panel (§6).
7. Recommend the single highest-leverage move — almost always: fix RN routine-bleed or SOC lag before adding generalist headcount.

**One-line doctrine for the agent:** *The staffing model is the primary capacity effector; protect the assessing clinician's hours and the SOC admit slots above all else, tune every number to the specific market, and never quote nominal FTE when steady-state effective FTE is what actually converts referrals into census.*
