# Capacity Tactics Library (v0 — SME-seeded)

> **What this is.** The consolidated corpus of capacity-management tactics, synthesized from five SME-persona
> briefs ([`perspectives/`](./perspectives/)) and organized by the capacity stack
> ([`../strategy/capacity-strategy-foundation.md`](../strategy/capacity-strategy-foundation.md)). Each tactic is
> a candidate to become **tool logic** and/or an **AI-agent training example**, per the
> [SME discovery framework](./sme-discovery-framework.md).
>
> **Status: v0, seeded not validated.** These are AI-generated hypotheses grounded in the operator's strategy
> download. They are the *starting hypotheses to validate with real SMEs* and to reconcile against Compassus's
> actual numbers — not settled truth. Confidence is marked per tactic.
>
> **The convergence.** Five independent lenses agreed on a small set of load-bearing truths. Where all five
> converge, confidence is highest and the tactic should be built first.

## The five things every SME lens converged on

1. **Capacity is created at the SOC/assessment slot, and most often lost because the assistant tier (LPN/PTA) is understaffed.** *Never diagnose "we're full" without decomposing skilled clinicians' days by visit type.* (ED, DCS, Scheduler, Strategist)
2. **SOC capacity is protected inventory, routed by clinical law** — RN for any SOC where nursing is on the case; PT only when nursing is not. Raiding SOC slots for routine overflow silently kills growth. (All five)
3. **Capacity ≠ visit count.** True load = visit + drive + documentation + coordination + acuity. Visit-point-only math overloads the efficient clinician and looks balanced doing it. (DCS, Scheduler, RN, Strategist)
4. **Discretionary effort is a borrowed, exhaustible resource governed by reciprocity and fairness.** The naive optimizer burns the reliable clinician first; protect them or lose them on a turnover lag. (ED, DCS, Scheduler, RN)
5. **The tool/agent is part of the culture and can't be neutral.** Propose don't dispose; show the cost; enforce scope and compliance as hard rails; never manipulate. (All five)

---

## Layer 1 — Staffing model (primary effector)

| # | Tactic | Encode as (system) | Agent behavior / guardrail | Source · confidence |
|---|---|---|---|---|
| L1-1 | **Discipline-balance / RN-routine-bleed** — LPN/PTA absorb routine so RN/PT stay on assessment | Per-clinician `% routine (assistant-eligible) WVP`; flag RN routine-bleed >~20%; live RN:LPN / PT:PTA vs market band | Recommend **assistant hire before assessing hire**; express fix as "SOCs unlocked"; never default to "hire more RNs" | ED, DCS, Scheduler, Strategist · **high** |
| L1-2 | **SOC-dedicated known slots** — a nurse/PT who sees only SOC/ROC = bookable admit inventory | Model SOC capacity as a *separate reservable pool*; "admit slots today/this week" headline; role-erosion counter when pulled to routine | Treat SOC slots as protected inventory; solve routine overflow elsewhere; only raid with shown cost + manager sign-off | ED, DCS, RN, Strategist · **high** |
| L1-3 | **SOC assignment rule (clinical law)** — RN if nursing on case; PT only if no nursing (ROC same) | `nursing_on_case` field; hard routing rule; cross-discipline SOC = hard-fail w/ reason | Ask "is nursing tied?" first; never trade an RN-SOC to a PT to balance load; escalate shortage, don't mis-assign | DCS, RN, ED, Strategist · **high (operator-confirmed)** |
| L1-4 | **Market-unique model sizing** — no copy-paste ratios; size to the market's potential | `MarketProfile` (DriveFactor, payer/case mix, referral profile, seasonality); per-market target bands; plan-vs-actual variance | Read MarketProfile first; explain equal-census/different-model via market factors, never "over-staffed" | ED, Strategist · **med** |
| L1-5 | **Census-to-staffing solve + marginal growth** — FTE by discipline from census × util × freq × weight | `Required_FTE_d = Weekly_WVP_d / target`; `ΔFTE` per +N census | Never quote staffing without stating util/freq assumptions; name the discipline that caps growth | Strategist · **med** |
| L1-6 | **Binding-constraint capacity** — true capacity = min slack across disciplines | `Slack_d`; `headroom = min_d Slack_d`; name `BindingDiscipline`; re-solve after each hire | Report one number (the constraint) + which discipline sets it; show the *next* bottleneck after a hire | Strategist · **med** |
| L1-7 | **Ramp + attrition = effective FTE** — plan on steady-state, not roster | `RampFactor(week)`; `Effective_FTE`; preceptor drag; `attrition_drag` | Quote steady-state capacity; add attrition-replacement hires just to hold census | Strategist · **med** |
| L1-8 | **PRN as bounded flex, not chassis** — over-reliance = a core-staffing diagnosis | `PRN_dependency` bands (≤10 healthy / >15 core gap → convert to core hire); cap PRN SOC share ≤10% | If PRN dependency >15% for 3+ wks, recommend core hires by the borrowed discipline, stop papering the gap | Strategist, ED · **med** |
| L1-9 | **Financial/tier lens** — margin per skilled hour; cheapest capacity is often an LPN/PTA | Loaded cost + reimbursement per visit type; skilled-hours-leakage $; tier comparison on any hire rec | Compare tiers on cost + SOCs-unlocked; default to lowest-cost tier that frees skilled slots | ED · **med** |

## Layer 2 — Territory (controllable preparation)

| # | Tactic | Encode as (system) | Agent behavior / guardrail | Source · confidence |
|---|---|---|---|---|
| L2-1 | **Resting-posture territory design** — caseload band below ceiling, keyed to referral density, so absorption is automatic | Territory + target caseload band w/ headroom; headroom-by-territory (green/amber/red); rebalance flag | Route to in-territory clinician *with real headroom*; protect slack; don't fill everyone to the top | ED, DCS, Scheduler, RN · **high** |
| L2-2 | **Zone coverage floor** — ≥1 admit-capable clinician per active zone; zone slack ≥ expected daily referrals | `Zone_floor_FTE_z`; flag "coverage hole" even when branch aggregate is positive | Check capacity at *zone* level; a positive branch number can hide a leaking corner; cross-cover before hire | Strategist · **med** |
| L2-3 | **Territory-health as a structural signal** — chronic cross-territory routing = the map is wrong | Detect cross-territory routing + unabsorbed referral clusters; surface to leadership | Escalate the *pattern* as a territory-design finding, not more daily stretch-asks | RN, Scheduler · **high** |

## Layer 3 — Day-to-day management (the cockpit)

| # | Tactic | Encode as (system) | Agent behavior / guardrail | Source · confidence |
|---|---|---|---|---|
| L3-1 | **RN→LPN / PT→PTA offload sweep** — shift stable, orders-established routine to assistants to free assessment | `offload_eligible` (order established, stable ≥2 visits, no deterioration flag, goal met); PT 30-day reassessment pinned to PT | Propose, never auto-execute; show why each offload is *safe* + why the freed hour matters; block on stale data or deterioration language | DCS, ED · **high** |
| L3-2 | **Acuity-weighted caseload** — "full" is weighted acuity + travel + doc, not visit count | `weighted_caseload`; weighted-load % as primary fullness metric; "available for SOC" gated on it | Always reason in weighted/time terms; explain why fewer-patients can be fuller; never load on low raw count | DCS, RN, Strategist · **high** |
| L3-3 | **True availability (accepted ≠ pullable)** — `patient_confirmed` is locked; net out PTO/on-call recovery | Visit states w/ locked `patient_confirmed`; availability = open − PTO − recovery − constraints | Compute true availability, never raw white space; state its basis; never free a clinician by pulling a confirmed patient visit | Scheduler, RN · **high** |
| L3-4 | **Last-minute referral decision tree** — in-cluster FT → offload-to-assistant → SOC slot → per-diem → escalate | Engine executes the ordered tree, SOC-gated; assessing→assistant swap detection | Return first viable + next-best, showing why earlier tiers were skipped; never auto-decline; SOC rule inviolable | Scheduler, ED · **high** |
| L3-5 | **Fast backfill on cancel/discharge** — freed slot is perishable; match to same-cluster demand fast | Reverse-matcher keyed on freed slot's time+cluster+clinician; time-decay urgency | Propose backfill in the decay window, prioritizing the freed clinician's cluster; confirm they're still available | Scheduler, ED · **high** |
| L3-6 | **Compliance windows pre-consume capacity** — recert(60)/PT-reassess(30)/HHA-supervisory(14)/48h-ROC/48h-MD | Pinned discipline-specific tasks reserved *before* "available" is shown; recert-wall early warning | Reserve compliance capacity first; never show an obligated slot as free; forecast recert clusters and smooth | DCS · **high** |
| L3-7 | **Per-diem warm list + forecast-the-gap** — engage on cadence; publish the need 5–7 days out | Disengagement flag; nightly gap forecast → publishable slots; per-diem-facing "open slots" view | Draft outreach as an availability *question*, not a booking; forecast and propose; never double-promise a slot | Scheduler, ED · **high** |
| L3-8 | **Per-diem retention/fairness ledger** — repair cancellations; spread hours; per-diems leave over fairness | `hours_promised_vs_delivered`, agency-cancellations, pool-share; debt + fairness flags | Boost owed/under-used per-diems *among eligible*; never book unqualified to settle a debt; flag concentration | Scheduler · **med** |
| L3-9 | **Morning fragility scan** — pre-solve single-points-of-failure before the phone rings | Daily scan (no-backup, hard-window, unconfirmed per-diem); slack score; blast-radius rank | Hand a ranked "3 weak points + a pre-lined backup each"; pre-draft but don't pre-book fallbacks | Scheduler · **med** |
| L3-10 | **Missed-visit handling as signal** — 48h MD notice + reschedule + pattern detection | MD-notify countdown; reschedule honoring frequency; patient-streak / clinician-rate flags | Open the clock + reschedule immediately; never absorb a missed visit as "freed capacity"; escalate patterns | DCS · **high** |
| L3-11 | **SOC-timeliness as a growth KPI** — referral-to-SOC interval by source; diagnose upstream on drift | Track interval by source/discipline/geo; correlate to slot-fill + discipline balance; decline-rate by source | Treat slow SOC as capacity+referral risk, not a compliance flag; recommend the specific staffing fix | ED · **high** |

## Multiplier — Culture & leadership

| # | Tactic | Encode as (system) | Agent behavior / guardrail | Source · confidence |
|---|---|---|---|---|
| C-1 | **Offload-as-protection / reciprocity ledger** — proactively lighten a spiked clinician; bank the yes | `recent_spike_score`; proactive "protection offload"; bidirectional reciprocity ledger; fairness skew flag | Recommend relief before burnout; prefer the *un-tapped* clinician for asks; surface imbalance to leadership; **never exploit the reliable yes** | ED, DCS, Scheduler, RN · **high** |
| C-2 | **The ask that gets a yes** — specific, early, honestly-sized (drive+doc), refusable without penalty | Structured ask payload (time, drive delta, doc load, why-you, one-tap penalty-free decline); notice-lead-time flag | Frame concretely/early/honestly; **never** use guilt/urgency/scarcity/patient-welfare-as-leverage; a "no" is data | RN, Scheduler · **high** |
| C-3 | **Clear-policy protection** — encode branch policy so a stretch-ask is always safe & cited | Policy thresholds as config (after-hours, weekend, "at capacity," decline-allowed); asks cite the policy basis | Only ask inside encoded policy, cite it; escalate out-of-policy needs to the manager; never invent expectations | ED · **med** |
| C-4 | **Continuity of caregiver (default, bend at break points)** — protect for wound/decline/psych/EOL/active SOC | `continuity_sensitivity` (protect/flexible); optimizer honors "protect"; continuity as an outcome metric | Default to established caregiver; trade only on flexible-tagged patients w/ stated tradeoff; flag warm-handoff when it must break | RN · **high** |
| C-5 | **Burnout/turnover = capacity decay on a lag** — optimize the quarter | Leading burnout indicators; utilization ceiling requiring override; turnover cost in forecasting | Treat sustained overload as a cost not a success; reduce asks + flag when indicators trip; never grind the best people because they haven't quit yet | RN, ED · **high** |
| C-6 | **Human override is sacred** — clinician ground truth beats the model | Capture every override + reason as training signal; neutral decline logging; override-pattern = model defect | Treat clinician input as authoritative on the ground; never re-ask a considered no, argue, or treat overrides as non-compliance | RN · **high** |

---

## Cross-cutting agent guardrails (the "never" list — apply to every directive)

Every SME lens produced a version of these; they are the non-negotiable rails for any AI agent operating in the tool.

1. **Propose, don't dispose.** Every reassignment/offload/ask is a recommendation with visible reasoning; licensure-scope and POC decisions belong to licensed clinicians; a human closes anything touching a person's time or a patient commitment.
2. **Scope & the SOC rule are hard rails, never optimization variables.** RN-if-nursing / PT-only-if-not; LPN-can't-assess; PTA-can't-eval-or-do-the-30-day. Shortages escalate as capacity gaps — never route around scope.
3. **Compliance windows pre-consume capacity.** Recert 60 / PT-reassess 30 / HHA-supervisory 14 / 48h ROC / 48h MD-notify — reserved before any slot shows "free."
4. **Never raid SOC/ROC admit slots for routine overflow; never treat an open SOC slot as idle waste.**
5. **Capacity is time, not visit count.** Never offer "room for one more" on points alone — include drive, doc, coordination, acuity.
6. **Protect the reliable clinician.** Spread discretionary load; never punish reliability with more asks; enforce a utilization ceiling; flag when the same few carry the branch.
7. **Never manipulate.** No guilt/urgency/scarcity/patient-welfare leverage; every ask shows its true size and a penalty-free out; a "no" is data.
8. **`patient_confirmed` visits are immovable** without explicit human release.
9. **Distinguish structural from transient.** Recurring shortfall → staffing-model signal to leadership; one-off → day-to-day fix. Label which; never mask a structural gap with silent overtime.
10. **Stale/missing clinical data blocks auto-eligibility.** No offload on stale stability data or any note with deterioration language.

## Parameters to validate (the "open numbers")

These thresholds/ratios are seeded hypotheses — get the real Compassus values from SMEs + data before hard-coding.

| Parameter | Seeded value (hypothesis) | Source |
|---|---|---|
| RN routine-bleed flag threshold | ~20–25% of RN WVP on LPN-eligible visits | ED, Strategist |
| RN:LPN ratio | chronic market ≈ 1:0.8–1.2; high-acuity ≈ 1:0.3 | Strategist |
| PTA:PT field-visit cap | ≤ 2:1 (state supervisory ceiling) | Strategist |
| Visit weights (WVP) | tool-confirmed: SOC 2.5 / recert 1.75 / eval 1.5 / reassess 1.25 / dc 1.75 / routine 1.0 (Colin, Jul 2026) | Tool / operator |
| FT productivity target | RN 27–30, LPN 30–33, SOC-RN 22–26 WVP/wk | Strategist |
| SOC-RN daily admit capacity `k` | 2.5–3 admits/day | Strategist |
| SOC surge buffer | ~15% of bookable slots reserved | Strategist |
| PRN dependency bands | ≤10% healthy / 10–15% watch / >15% core gap | Strategist |
| Referral-rejection alert | >8% or rising 3 wks (earliest pre-stall signal) | Strategist |
| SOC same-day/timely target | ≥90% | Strategist, ED |
| Ramp curve | W1–2 .30 / W3–4 .50 / W5–8 .70 / W9–12 .85 / W13+ 1.0 | Strategist |
| Flex reserve | 8–12% of core WVP | Strategist |
| Front-load gold standard | ~42% of target Mon–Tue (tool value) | Tool |

## How the tool and agents consume this

- **The matching/directive engine** should tag every directive with its **layer** (L1/L2/L3/C) and pass it through the guardrails above before surfacing it. A day-to-day directive that violates a Layer-1 truth (e.g. "just have the RN take the routine") is wrong even if it balances today.
- **Agent training** draws each row's *situation → correct reasoning → recommended action → prohibited action* as an example. The `perspectives/` briefs are the long-form training source; this library is the indexed, deduplicated spec.
- **SME validation** works this table top-down: confirm/correct/kill each tactic, fill the real "open numbers," and promote high-confidence rows into the tool backlog + the strategy's business-rules set.
