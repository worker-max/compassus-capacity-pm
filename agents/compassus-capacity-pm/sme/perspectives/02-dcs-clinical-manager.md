# SME Perspective — DCS / Clinical Manager

> Seeded v0 perspective (AI-generated from the DCS / Clinical Manager lens, grounded in the operator's strategy
> download). **To be validated with a real DCS/Clinical Manager.** Preserved verbatim per the
> [SME discovery framework](../sme-discovery-framework.md).

# Home Health Capacity Tactics — DCS / Clinical Manager Lens

Framing note: capacity in home health is not "open visit slots." It is **protected assessment capacity** (RN/PT hours that can absorb a new SOC) plus **defensible offload capacity** (routine visits an LPN/PTA can legally and safely carry). A great branch manages the *ratio* between these two, not the raw visit count. Everything below serves the operator's hierarchy: staffing model first (the primary effector), territory second, day-to-day third, culture as the multiplier.

---

## TACTIC 1 — The RN→LPN Routine Offload Sweep

**Tactic.** Every week the clinical manager (or the tool) sweeps each RN's upcoming schedule and pulls stable, orders-established routine visits down to an LPN: routine wound care on a healing wound with an established order, scheduled B12/insulin teaching-complete injections, straightforward med administration, ostomy maintenance on a stable patient, catheter changes on a stable Foley. The RN keeps the assessment-dependent visits (SOC, recert, resumption, discharge, any visit where the plan of care may change).

**Trigger/context.** RN caseload weighted-load crosses ~90% of capacity, OR a new SOC lands in that RN's territory and there is no free assessment slot within the required timeframe.

**Why it works.** LPNs cannot assess, evaluate, or change a plan of care — but they can execute an established, stable plan. Shifting the "hands" work off the RN converts her most scarce resource (assessment/judgment time) back into bookable capacity. This is the single highest-leverage day-to-day move a manager makes.

**Encode as system logic.**
- Tag every visit with `visit_type` ∈ {SOC, ROC, recert, discharge, routine-skilled, teaching, supervisory}.
- Tag routine-skilled visits with an `offload_eligible` boolean, computed from: order is established (not new this cert period), patient `clinical_stability` = stable for ≥2 consecutive visits, no unresolved wound deterioration flag, teaching goal status = "return-demo met" for injection/med visits.
- Directive engine fires when `rn_weighted_load ≥ 0.90` AND `offload_eligible_visits > 0`: propose the top-N offloads ranked by lowest acuity, showing the RN hours freed.
- Hard block: `offload_eligible = false` for any visit within a recert window, any wound with a declining trajectory tag, any first-dose/new-medication teaching visit.

**Train the AI agent.** The agent proposes offloads, never auto-executes clinical reassignment. It reasons: "Which of this RN's visits require ongoing assessment vs. execution of a settled plan?" It surfaces the candidate list with the *reason each is safe* and the *reason each freed hour matters*. Guardrail: if stability data is missing or stale (>1 visit old), mark the visit "manager review required," not auto-eligible. Never offload a visit whose last note contains deterioration language — pattern-flag phrases like "increased drainage," "new redness," "SOB at rest" and force RN retention.

---

## TACTIC 2 — PT→PTA Offload with the Reassessment Guardrail

**Tactic.** Same discipline on the therapy side: the PT keeps the eval, the 30-day reassessment, discharge, and any visit where progression of the exercise plan is a clinical decision; the PTA carries the established treatment visits (gait training at a set assist level, established HEP progression, modality delivery) between reassessment points.

**Trigger/context.** PT weighted-load ≥ 90%, or a therapy-only SOC/eval is pending and the PT has no slot. PTA has open capacity.

**Why it works.** In home health the PT *must* personally perform the 30-day functional reassessment and cannot delegate evaluation or POC change. But the interval treatment visits are the PTA's lane. Offloading them protects the PT's eval capacity — the thing that actually converts a therapy referral into an admitted patient.

**Encode as system logic.**
- Track `days_since_last_PT_reassessment` per therapy patient; the mandatory PT reassessment visit is **pinned** to the PT and cannot be offloaded.
- PTA-eligible visits require: eval complete, POC established, patient progressing or stable, and the visit falls *before* the reassessment-due date.
- Directive engine surfaces PTA offload candidates only in the window between reassessment points; auto-locks the reassessment visit to the PT and warns if it drifts past day 30.

**Train the AI agent.** The agent reasons about the reassessment cadence as a hard rail: it may offload treatment visits to a PTA *only* inside a valid reassessment window and *only* for a progressing/stable patient. Guardrail: never let a PTA-only stretch cross the 30-day mark — if the reassessment isn't scheduled, block further PTA offloads and escalate "PT reassessment overdue." Also detect discipline-shortage patterns (too few PTAs → PT overloaded with routine gait training) and raise a staffing-model signal, not just a scheduling fix.

---

## TACTIC 3 — SOC Assignment by the Nursing-Tie Rule

**Tactic.** The tool routes every SOC by the ground-truth rule: **if nursing is on the referral, the RN performs the SOC; PT performs the SOC only when nursing is NOT on the referral.** The great branch never lets a therapy-only SOC consume an RN slot, and never lets a nursing case get opened by PT.

**Trigger/context.** New referral hits the capacity cockpit. The referral's discipline mix (SN ordered? therapy-only?) determines the assessing clinician pool before availability is even considered.

**Why it works.** Comprehensive assessment / OASIS ownership follows the primary discipline. Getting this right prevents rework (a PT can't open a nursing case), protects RN capacity for the cases that legally require it, and lets therapy-only referrals be absorbed by PT without burning nursing capacity — critical in RN-tight markets.

**Encode as system logic.**
- Referral intake field `nursing_on_case` (derived from ordered disciplines). Routing rule:
  - `nursing_on_case = true` → SOC-eligible pool = RNs only.
  - `nursing_on_case = false` → SOC-eligible pool = PTs (therapy SOC).
- Hard fail with explanation if a plan attempts a PT SOC on a nursing case or an RN SOC on a therapy-only referral that has no nursing.
- SOC slot matching then runs against the correct pool's `soc_dedicated` capacity first.

**Train the AI agent.** The agent's first question on any referral is "Is nursing tied to this case?" — and it routes accordingly before looking at who's free. Guardrail: the rule is non-negotiable; the agent cannot "optimize" around an RN shortage by assigning a PT to open a nursing case. If nursing is tied and no RN has SOC capacity in the required window, escalate as a capacity gap rather than mis-assigning.

---

## TACTIC 4 — SOC-Dedicated Slot Protection

**Tactic.** The staffing model designates SOC-dedicated nurses and PTs whose calendars carry **known, bookable SOC slots** (e.g., two protected SOC windows/day). The manager guards these slots — routine visits do not backfill them except as a last resort, and only with manager sign-off.

**Why it works.** Referrals are the precondition for everything; the constraint on converting them is assessment capacity in the right timeframe (SOC generally within 48h; ROC within 48h of hospital discharge). Pre-committing dedicated slots turns referral absorption from a scramble into an almost-automatic posture.

**Encode as system logic.**
- Clinician attribute `soc_dedicated = true` with `protected_soc_slots_per_day = N`.
- Capacity cockpit displays **SOC slots available today/tomorrow** as a first-class number, separate from total open visits.
- Backfilling a protected SOC slot with a routine visit requires an override with `reason:` and drops the branch's "SOC readiness" indicator.
- Alert when protected SOC slots available in the next 48h fall below the branch's rolling referral rate.

**Train the AI agent.** Treat SOC slots as a protected reserve, report them distinctly, and resist filling them with routine work. When referral inflow forecast exceeds protected SOC capacity, proactively propose offloading routine visits (Tactics 1–2) to *manufacture* more SOC slots rather than consuming the reserve. Guardrail: recommend backfilling a protected slot only when every other capacity lever is exhausted, and flag the SOC-readiness degradation.

---

## TACTIC 5 — ROC Timing Protection (the 48-Hour Rail)

**Tactic.** When a patient is hospitalized and discharged back, the branch protects the ROC assessment inside the required window (generally within 48 hours of discharge home or per physician order). The great branch tracks patients *out* to the hospital as pending returns, not as freed capacity.

**Why it works.** A missed or late ROC is a compliance and quality failure and a lost patient. ROCs follow the same nursing-tie rule as SOCs (RN if nursing on case).

**Encode as system logic.**
- Patient status `hospitalized` with `expected_return` flag; on discharge event, spawn a `ROC_due` task with a 48h countdown routed to the correct discipline pool (nursing-tie rule).
- Cockpit reserves anticipated ROC demand against SOC-dedicated capacity so returns don't oversubscribe slots.
- Escalating alerts at 24h / 12h / breach on any un-slotted ROC.

**Train the AI agent.** Maintain a live "pending returns" list and pre-position ROC capacity. On a discharge event immediately route the ROC by the nursing-tie rule and confirm a slot inside 48h. Guardrail: never treat a hospitalized patient's freed visits as durable capacity to give away; flag them "on hold — ROC pending."

---

## TACTIC 6 — Acuity-Weighted Caseload (Kill the Raw Visit Count)

**Tactic.** The manager judges a "full" caseload by **weighted acuity and travel**, not by number of patients or visits. A nurse with 6 high-acuity, complex, geographically spread patients may be fuller than one with 9 stable maintenance patients.

**Why it works.** Home health acuity varies enormously. Weighting by acuity + visit frequency + drive time + documentation burden gives the true picture and is how experienced managers actually decide.

**Encode as system logic.**
- Compute `weighted_caseload = Σ(visit_acuity_score × frequency) + travel_factor + coordination_burden` per clinician, not a headcount.
- Acuity score drivers: wound-vac/complex wounds, new meds/first-dose, IV therapy, unstable vitals trend, high comorbidity count, frequent physician contact, behavioral/social complexity.
- Cockpit shows **weighted load %** as the primary fullness metric; raw visit count is secondary. "Available for SOC" is gated on weighted load, not visit count.

**Train the AI agent.** Always reason in weighted terms. When asked "who can take this?" rank by remaining weighted capacity and territory fit, and explain *why* a clinician with fewer patients is actually fuller. Guardrail: never recommend loading a clinician just because her raw count is low; surface the acuity mix. Detect chronically mis-weighted clinicians as a staffing-model signal.

---

## TACTIC 7 — Recert / Reassessment Windows as Hard Scheduling Constraints

**Tactic.** The branch treats compliance windows as immovable rails that pre-consume capacity: the **60-day recert**, the **PT 30-day functional reassessment**, the **14-day HHA supervisory visit**, and RN supervision of LPNs per state rule. These are scheduled *first*; discretionary capacity is what's left.

**Why it works.** Miss a recert and the episode is jeopardized; miss the 14-day aide supervisory and you have a survey deficiency; let the PT 30-day slip and therapy visits become non-billable. These consume specific clinician types on specific dates — the true baseline load beneath all "open" capacity.

**Encode as system logic.**
- Per patient track: `recert_window` (day 56–60 target), `pt_reassessment_due` (≤ day 30), `hha_supervisory_due` (≤ 14 days), `lpn_supervision_due` (state interval).
- These generate **pinned, discipline-specific tasks** reserved against capacity *before* the cockpit shows "available" slots.
- Directive engine surfaces the end-of-cert-period cluster early ("recert wall in 10 days: 7 RN recerts due") so it's spread, not crammed.

**Train the AI agent.** Reserve compliance-window capacity first, then report discretionary capacity as the remainder — never show a compliance-obligated slot as free. Forecast recert clusters and propose smoothing them. Guardrail: may not schedule a new SOC into capacity owed to a recert/reassessment/supervisory obligation without flagging the conflict. Know *which discipline* each window requires and route accordingly.

---

## TACTIC 8 — Missed-Visit 48-Hour MD Notification Handling

**Tactic.** When a visit is missed, the branch executes the protocol: document, attempt reschedule within the frequency order, and **notify the physician within 48 hours** when the missed visit affects the plan of care. The great branch also treats the missed visit as a capacity signal.

**Encode as system logic.**
- Missed-visit event spawns: (a) `md_notification_due` 48h countdown, (b) reschedule task honoring the ordered frequency, (c) increment on `patient_missed_streak` and `clinician_missed_rate`.
- Escalating alert on the 48h MD notification until documented.
- Pattern flags: patient missed_streak ≥ 2 → willingness/logistics review; clinician missed_rate spike → schedule/territory review.

**Train the AI agent.** On a missed visit immediately open the MD-notification clock and the reschedule task (respecting frequency), and watch for patterns. Guardrail: never silently absorb a missed visit as "freed capacity" — the reschedule obligation persists and the MD notification is mandatory when the POC is affected. Escalate repeated patient refusals as a willingness/logistics issue and clinician missed-rate spikes as a workload/territory issue.

---

## TACTIC 9 — Offload-as-Protection (the Culture Multiplier)

**Tactic.** The manager *proactively* lightens a clinician's week before being asked — pulling two routine visits off an RN who just carried three SOCs — explicitly as protection. The branch banks reciprocity so the clinician says "yes" when it later needs a same-day SOC.

**Why it works.** This is the culture/leadership multiplier. Protection generates discretionary effort and reciprocity. Raw utilization maximization destroys this; deliberate slack builds it.

**Encode as system logic.**
- Track `recent_spike_score` per clinician (SOC count this week, patient deaths, after-hours calls, weekend work, consecutive high-acuity days).
- Directive engine proposes *proactive* offloads for spiked clinicians even when not over threshold, labeled "protection offload."
- Track a lightweight `reciprocity_ledger` so the tool doesn't repeatedly tap the same person; fairness signal.

**Train the AI agent.** Watch for spike patterns and *recommend* relief before burnout, framing it as protection. When it later needs a discretionary same-day SOC, preferentially ask clinicians recently protected and not over-tapped. Guardrail: this is a recommendation to the human manager, never automated schedule manipulation. Never over-optimize a "protected" clinician back into overload the same week; flag if the branch is systematically burning the same few reliable people (a staffing-model gap).

---

## TACTIC 10 — LPN/PTA Utilization Floor (Balance at Every Discipline Level)

**Tactic.** The manager monitors whether assistants are *under-used* — RNs drowning in routine while LPNs sit light means the mix is wrong or the offload discipline is failing.

**Why it works.** This is the primary effector — a balanced staffing model at *all* discipline levels. Under-utilized assistants are wasted capacity and a signal the offload sweep isn't running. Fixing the ratio is often higher-leverage than any day-to-day scheduling move.

**Encode as system logic.**
- Compute per-territory `assessing_vs_assistant_load_ratio`. Alert when RNs > threshold while LPNs < floor (or PT vs PTA).
- Track `offload_capture_rate` = offload-eligible routine visits actually assigned to assistants ÷ total offload-eligible. Low capture = discipline failing.
- Surface as a staffing-model signal, distinct from day-to-day directives.

**Train the AI agent.** Monitor the assessing-vs-assistant balance per territory and flag imbalance as a *staffing-model* recommendation (hire/redeploy an LPN, PTA) rather than solving it visit-by-visit. Report offload capture rate as a branch health metric. Guardrail: distinguish a structural mix problem (needs hiring, escalate to DCS) from a transient one; don't paper over a staffing gap with unsustainable overtime.

---

## TACTIC 11 — Territory Resting Posture for Referral Absorption

**Tactic.** The manager sets clinician territories so that a new referral in any ZIP lands near a clinician who already has capacity and geographic fit — the "resting posture" where absorbing a referral is near-automatic. SOC-dedicated clinicians are positioned to cover the highest-referral geographies.

**Why it works.** A referral in a well-covered ZIP costs little capacity to absorb; one in a gap costs a long drive, a mis-fit clinician, and a burned slot. Good resting posture keeps *travel_factor* on new admits low.

**Encode as system logic.**
- Map clinician territory to referral heat map; compute `referral_absorption_readiness` per ZIP = (nearby clinician capacity × geographic fit).
- Flag ZIPs with high referral rate and low nearby capacity as coverage gaps.
- SOC slot matching includes travel distance; the matching engine ranks candidates by (correct discipline pool × weighted capacity × proximity).

**Train the AI agent.** When matching a referral, optimize jointly for the nursing-tie discipline rule, weighted capacity, and proximity — not availability alone. Surface persistent coverage gaps as a territory-design recommendation. Guardrail: propose territory adjustments to the manager; do not unilaterally rewrite assignments, and never sacrifice the SOC nursing-tie rule for a shorter drive.

---

## Cross-cutting agent guardrails (apply to all tactics)

- **The AI proposes; the clinical manager disposes.** Every reassignment, offload, or protection move is a recommendation with visible reasoning. Licensure-scope and POC decisions belong to licensed clinicians.
- **Scope rules are hard rails, never optimization variables.** Nursing-tie SOC/ROC rule, LPN-can't-assess, PTA-can't-evaluate-or-do-the-30-day, RN-supervises-LPN — the agent may not "route around" a shortage by violating scope. Shortages escalate as capacity gaps.
- **Compliance windows pre-consume capacity.** Recert (60), PT reassessment (30), HHA supervisory (14), 48h MD missed-visit notification, 48h ROC — reserved before any slot is shown "free."
- **Stale or missing clinical data blocks auto-eligibility.** No offload on stability data older than one visit; no offload on any note containing deterioration language.
- **Distinguish structural from transient.** A recurring shortfall is a staffing-model signal to the DCS; a one-off is a day-to-day fix. Label which.
- **Protect the people who protect capacity.** Track relief/reciprocity so the same reliable clinicians aren't chronically burned — flag it as a leadership issue.
