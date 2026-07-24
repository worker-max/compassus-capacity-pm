# Home Health Capacity & Scheduling — Master Document

*Compassus Capacity & Scheduling Initiative · consolidated reference*

## Table of Contents
*This document uses heading styles. In Google Docs choose Insert → Table of contents for a live, clickable, auto-updating TOC. A two-level outline is below.*

- Part I — Orientation
  - How to use this document
  - Executive summary
- Part II — The Problem: Discovery Ground Truth
  - HH Scheduling Discovery Session — Compassus
  - Home Health Capacity & Scheduling — Consolidated Summary
- Part III — The Strategy: Battle-Plan Logic
  - Capacity Strategy Foundation — the Battle-Plan Logic
- Part IV — SME Knowledge & Tactics
  - Capacity Tactics Library (v0 — SME-seeded)
  - SME Discovery Framework — sourcing tactics, building the agents
- Part V — The Capacity Management Tool
  - Capacity Tool — Mockup Data Spec (read from source)
  - As-built review (invisiblegears main @ 6dba163, re-read from source)
  - Capacity Tool — Data Index (Phase A)
- Part VI — Ecosystem & Roadmap
  - Home Health Capacity Ecosystem — Coverage Scan
- Part VII — Appendices
  - SME Perspective — Branch Executive Director
  - Home Health Capacity Tactics — Branch ED Lens
  - SME Perspective — DCS / Clinical Manager
  - Home Health Capacity Tactics — DCS / Clinical Manager Lens
  - SME Perspective — Senior Scheduler / Staffing Coordinator
  - Day-to-Day Capacity Execution Tactics — Scheduler / Staffing-Coordinator Lens
  - SME Perspective — Field RN / SOC Nurse (the clinician ground truth)
  - Field RN / SOC-Nurse Ground Truth: How Capacity Is Actually Protected and Expanded
  - SME Perspective — Workforce / Staffing Strategist (the model math)
  - Staffing-Model Logic for Market-Governed Capacity — Workforce/Staffing-Strategist Lens
  - Source War-List Worksheet — Capacity Tool

# Part I — Orientation

## How to use this document

This is the **single master reference** for the Compassus capacity & scheduling initiative. It consolidates
every work product to date into one place, organized so each kind of reader can find their level:

- **Executives / sponsors** — read Part I and the top of Part III (the capacity stack).
- **Product / build team** — Parts III (rules), IV (tactics → system logic), V (the tool + data model).
- **Operators / SMEs** — Parts II (discovery), IV (tactics + the discovery framework), and the Appendices.

A **dynamic Table of Contents** follows. In Google Docs it updates automatically from the heading styles in
this document (Insert → Table of contents → with page numbers/links). A static outline is included below it for
immediate navigation.

## Executive summary

**Capacity and scheduling are two different functions, and conflating them is the root problem.** Capacity is a
*planning* function — what a branch can absorb. Scheduling is an *execution* function — who goes where, when.
Branches run both through one manual spreadsheet, so neither is done well.

**The discovery's core finding: the scheduling problem is not a scheduling problem.** Schedulers are
administrators; the real inefficiency is upstream (clinical documentation, DCS workflow, authorization holds)
and structural (the staffing model). **Capacity must be solved before scheduling** — the reason a prior "Smart
Scheduling" pilot failed was change management, not technology.

**The capacity stack (the battle-plan logic):** referrals are the precondition; the **staffing model** is the
primary effector (balanced at every discipline level, unique to each market, with SOC capacity as known slots);
**territory** pre-positions capacity into an automatic "resting posture"; **day-to-day** management absorbs
variance; and **culture/leadership** is the multiplier that turns protection into discretionary effort.

**The load-bearing rules** (validated across five SME lenses): capacity is created at the SOC/assessment slot
and lost to an understaffed assistant tier; SOC is protected inventory routed by clinical law (**RN for any SOC
where nursing is on the case; PT only when nursing is not**); capacity is *time* (visit + drive + documentation
+ acuity), not visit count; discretionary effort is borrowed and must not be exploited; and any AI agent
proposes rather than disposes, enforces scope/compliance as hard rails, and never manipulates.

**The tool** — a 9-tab Clinician Capacity Management Tool with a real matching/directive brain — is the
day-to-day surface. Its data model (the data index) and its open correctness gaps (restriction enforcement, the
SOC rule, time-based capacity) are documented in Part V.

> **Document status.** The discovery material (Part II) is operator-sourced ground truth. The strategy (Part
> III) is grounded in the operator's SME download. The tactics (Part IV) and the quantitative parameters are
> **AI-seeded hypotheses to validate with real SMEs** — confidence is marked throughout. This is a living
> document.



# Part II — The Problem: Discovery Ground Truth

## HH Scheduling Discovery Session — Compassus

> **Source:** Google Drive — "HH Scheduling Discovery Session" (Compassus capacity & scheduling initiative).
> Full-day cross-functional discovery (scheduling operations leaders, clinical staff, technology/data analysts)
> mapping the home health scheduling process from referral intake through clinician–patient visit execution.
> Rendered here faithfully as the agent's primary ground truth. Do not paraphrase away the specifics.

### Executive Summary

**Core Finding — the scheduling problem is not a scheduling problem.** Schedulers at Compassus spend the
majority of their time on administrative workflow tasks inside Home Care Home Base (HCHB). The true
inefficiencies lie upstream: clinical documentation delays, DCS workflow bottlenecks, authorization holds,
and fragmented capacity management.

Key conclusions:

- **Schedulers are administrators, not schedulers.**
- **The only true scheduling decision a scheduler makes is the start-of-care intake call.**
- Two separate but interdependent solution tracks are needed:
  - Workflow automation to eliminate repetitive admin tasks
  - AI/optimization engine for clinician–patient matching and schedule optimization
- **Capacity management forecasting is the critical foundation** — without it, any scheduling optimization
  tool is built on unstable ground.
- **Clinician buy-in requires the tool be positioned as a personal assistant** that increases flexibility
  and earnings, not a top-down control mechanism.

### 1. What Schedulers Actually Do

Schedulers do not determine visit dates, frequencies, or clinical priorities. Their function is:

- Receiving workflow tasks from HCHB **after the DCS has completed their review**
- Clicking on pre-plotted visit blocks on a calendar (plotted by the clinician) and assigning the correct clinician
- Managing coordination notes from clinicians requesting changes
- Processing missed-visit tasks — notifying the MD within 48 hours, documenting, and determining if a reschedule is required
- Handling authorization ("off") notifications — **up to 50–60 per day, most non-actionable**
- Making one direct patient call: the **start-of-care welcome call**

> **Key Insight.** When clinicians say "my schedule is a mess," they are almost never describing a scheduler
> failure. The visit is typically stuck in DCS workflow, pending authorization, or waiting on the clinician's
> own documentation to be submitted. **Scheduling gets blamed because it is the final visible touchpoint.**

### 2. The End-to-End Workflow Chain

Many sequential handoffs must occur before a scheduler can act on a single patient. For a three-discipline
patient (Nursing, PT, OT), **7+ separate workflow tasks** are generated — each requiring the scheduler to
open, review, and act or close.

#### Start of Care → Scheduler Assignment

| Step | Owner | Action |
|---|---|---|
| 1 | Clinician | Completes start-of-care visit; syncs documentation from point-of-care device |
| 2 | DCS | Receives workflow; completes 4-task checklist: plan-of-care review, calendar accuracy check, pending auth management, plan-of-care lock |
| 3 | Auth Team | Adds authorization for non-Medicare payers (Medicare auto-authorizes) |
| 4 | Scheduler | Receives "Complete Requested Schedule – Week 1" task; assigns clinician to plotted visits for next 7–10 days |
| 5 | Scheduler | Once plan of care locked, receives recertification task; schedules full episode (30–60 days), checking Medicare compliance requirements |

#### The Authorization Notification Problem

Schedulers receive **50–60 pending authorization notifications per day**. The majority are non-actionable —
triggered every time the auth team updates an authorization field, even if the actual authorized visits
haven't changed. Schedulers must open each one individually to determine if any action is required.
**This is widely cited as the most frustrating aspect of the scheduler's daily workflow.**

### 3. Capacity Management vs. Scheduling

> **Critical Distinction.** Capacity management and scheduling are two distinct problem statements.
> **Capacity management must be solved first** — it is the foundation on which any scheduling optimization
> tool must be built. Running Smart Scheduling without it is why prior attempts failed.

#### Capacity Management (Currently Manual)

Leaders currently manage capacity through experience, Excel spreadsheets, and scheduling grids. Key inputs
that must be tracked:

- **Census per territory/zip code** — roughly **40–50 patients per full-time RN+LPN team pair**
- **Referral pipeline** — what is coming, from which partners, with what payer mix
- **Clinician FTE, PTO, and specialty** (wound care, IV, lymphedema, etc.)
- **Utilization rates via Pulse** — whether visit frequencies are over- or under-plotted
- **Start-of-care pipeline** — how many are expected each day or week

None of these inputs currently feed into a single system. They exist across **HCHB, Pulse, Workday, Excel
grids, and individual manager knowledge.**

#### Why Smart Scheduling Failed

A prior pilot of HCHB's Smart Scheduling feature in Alabama failed **not because the technology was flawed**, but because:

- Leaders constrained the system to mirror existing manual processes — locking clinicians to specific zip codes, refusing to allow autonomous assignment decisions
- When the system tried to optimize (e.g., assigning a slightly out-of-territory nurse who had availability), clinicians rejected the assignment
- Leadership allowed the resistance, effectively pulling the smart logic out of Smart Scheduling
- The system was never allowed to do what it was designed to do — **it was never truly piloted**

### 4. Clinician Dynamics & Buy-In Challenges

The primary reason clinicians choose home health is **flexibility** — control over their schedule, ability to
manage personal commitments, autonomy in structuring their day. Any scheduling tool must lead with this reality.

- Clinicians manage their own days: they call patients the evening before, confirm or reschedule, and accept their visit slate each morning
- They plot visits on their device calendar — the scheduler only assigns the clinician to those pre-plotted blocks
- On **pay-per-visit** models, clinicians are motivated to do more visits — route optimization and better matching could increase daily counts and earnings
- Tenured clinicians (10–20 years) are the hardest to change; **newer clinicians and new integration offices offer the cleanest pilot opportunity**
- Smart Scheduling in Alabama failed partly because experienced clinicians refused to cross zip-code boundaries and leadership didn't enforce it

> **Recommended Framing for Clinician Rollout.** Position the scheduling tool as a "personal assistant" — not
> a control mechanism. Message: *"This tool does the legwork for you. You keep all your flexibility. And if
> you're on a pay-per-visit model, optimized routing likely means you can fit in more visits per day."*

### 5. Technology Landscape & Integration Points

Most systems do not communicate in real time.

| System | Role & Status |
|---|---|
| **Home Care Home Base (HCHB)** | Core clinical and workflow system. All tasks, plan of care, scheduling workflow, and visit records live here. Not real-time; requires manual sync. |
| **Commure** | Newly deployed intake and referral management tool. Provides referral pipeline visibility. Does not yet push real-time patient workflow status to schedulers. |
| **NestMed** | Clinical documentation platform. Provides real-time documentation visibility — a significant improvement over point-of-care devices. Face-to-face authentication module under evaluation. |
| **Pulse** | Utilization review tool. DCS team uses for plan-of-care review and visit-frequency management. |
| **Workday** | HR/PTO system. Integration with HCHB exists but is **NOT currently activated** — PTO is manually entered into HCHB by scheduling staff. |
| **Coding (External)** | Outsourced ICD-10 coding vendor. Discrepancies between face-to-face documentation and coded diagnoses create plan-of-care holds that block downstream scheduling. |
| **Circadia Health** | Patient engagement / AI calling platform. Used for welcome calls in some California locations. Under evaluation for broader use. |

### 6. Patient Engagement Opportunity

Explored replacing the physical patient admission calendar with a digital interface (via QR code) providing:

- Visit time ranges (not exact times) for upcoming weeks
- Real-time notifications when schedule changes occur
- Ability for patients/caregivers to flag conflicts and request reschedules
- Caregiver visibility — particularly valuable for out-of-state family (e.g., Florida JV patients)

> Note: The physical calendar remains a **Medicare Conditions of Participation** requirement and must be
> maintained in the home. A digital interface would supplement, not replace, it.

### Next Steps (from the session)

1. **Vendor Evaluation** — Continue with 6–7 scheduling/capacity vendors (MedArrive, Circadia, Aria Health, others). Develop a shared requirements list covering both capacity forecasting and scheduling optimization before next vendor meetings.
2. **Pilot Site Selection** — Target a new integration or brand-new branch go-live as the first pilot. Consider a pay-per-visit office (Providence, Ohio Health, BSMH) for clinician buy-in testing where existing habits won't conflict with new tooling.
3. **Scheduler Pain Point Session** — Focused session with schedulers: biggest pain points, wish-list items, what would make their job easier. Observe end-of-day workflow.
4. **Capacity Management Scoping** — Define all demand-side inputs (census by territory, referral pipeline, new orders, pending auth, planned discharges) and capacity-side inputs (FTE, PTO, specialties, zip-code coverage) needed to build a capacity forecasting model.
5. **Commure Scheduling Grid View** — Add a scheduling-grid-style view within Commure (below referral tasks) showing pending referrals with payer, expected discharge date, discipline ordered, and status — to replace Excel scheduling grids.
6. **Workday ↔ HCHB Integration** — Activate the existing interface so approved PTO in Workday automatically creates unavailability in HCHB. Eliminates manual entry, prevents scenarios like 5 of 7 nurses approved off the same day.
7. **NestMed Face-to-Face Module** — Evaluate routing referral documents from Commure to NestMed for automated face-to-face validation. Reduces downstream coding discrepancies that create POC holds.
8. **Patient Engagement Interface** — Explore a QR-code patient scheduling portal (time ranges, reschedule requests, caregiver visibility).
9. **Steerco Email Update** — Michael to finalize stakeholder email (positive reception callout; groups covered: referral coordinators, growth, insurance ops, operations; add due-dates column).

### Processes Identified

#### Process 1 — Start of Care Workflow (Per Discipline)
Triggered when a new patient is admitted. For a three-discipline patient (Nursing, PT, OT), it runs three times in parallel and generates 7+ scheduler tasks total.

1. Intake schedules initial visit → Clinician completes SOC → Syncs documentation from device
2. DCS receives workflow → 4-task checklist: POC review, calendar accuracy, pending auth management, POC lock
3. Auth team adds auth for non-Medicare payers (Medicare auto-authorized)
4. Scheduler receives "Complete Requested Schedule – Week 1" → Assigns clinician to pre-plotted visits for next 7–10 days
5. Once POC locked/approved: Scheduler receives "Start of Care Recertification" task → Schedules full 30–60 day episode, verifying Medicare compliance: 30-day reassessments, HHA supervisory visits every 14 days, buddy codes, discharge/recert visit codes

> **Medicare Compliance Note.** Schedulers must verify: (1) 30-day therapy reassessments plotted within window,
> (2) HHA supervisory visits every 14 days, (3) each discipline ends in a discharge, recertification, or
> reassessment visit — not a routine visit. Missing these has billing and compliance consequences.

#### Process 2 — Ongoing Visit Management
Runs continuously through the episode as needs evolve.

- **New Order:** Clinician calls physician → verbal order → enters order in HCHB → goes to DCS for approval (cannot bypass) → scheduler receives task → assigns additional visits
- **Authorization (Off) Notifications:** 50–60/day, majority non-actionable; must open each to check if additional visits can now be scheduled; triggered on any auth-screen update
- **Missed Visit Workflow:** Clinician syncs missed visit → scheduler notified → must notify MD within 48 hours (Medicare) → documents → determines reschedule; if a 30-day reassessment is involved, verify next visit maintains compliance window
- **Other Visit Actions:** Declined / reassigned / rescheduled — clinician-triggered on device at sync; scheduler handles resulting coordination notes and system tasks

#### Process 3 — Clinician Daily Scheduling
Largely independent of the back-office scheduler.

- Evening before: reviews 7-day rolling calendar; calls patients to confirm or reschedule for next day
- Reassigns/reschedules/notes missed visits — synced to HCHB on next sync
- Morning of: long-presses device to bulk-accept all visits for the day
- Throughout the day: adjusts as needed — pulls forward visits if others cancel, handles urgent PRN needs, coordinates via coordination notes

> **Important Constraint.** Once a clinician accepts a visit for the day in HCHB, **the back office cannot
> remove it from their device to reassign it.** This is a hard system stop. All same-day changes require
> direct phone coordination between scheduler and clinician.

#### Process 4 — Capacity Management (Current Manual State)
Managed via leader experience, Excel scheduling grids, and HCHB reports — no single system view.

- Track census per territory/zip — target ~40–50 patients per full-time RN+LPN team pair at **30 pts/week productivity minimum**
- Monitor referral pipeline from grid or Commure to anticipate incoming SOC volume
- Review utilization via Pulse — adjust visit frequency if teams over-plotted
- DCS leadership holds weekly cross-approval PTO meetings to prevent all clinicians being off simultaneously
- Scheduling grid (Excel) tracks pending referrals, expected discharge dates, payer mix, discipline ordered, available SOC slots per day — manually updated in parallel with HCHB

> Once teams trust Commure, the Excel scheduling grids will likely become redundant — Commure holds the same
> information in a more accessible, up-to-date form.

### Appendix — Key Terms

| Term | Definition |
|---|---|
| **Start of Care (SOC)** | Initial evaluation visit when a patient is admitted. Skilled nursing must always go first if ordered. |
| **DCS** | Director of Clinical Services. Reviews/approves plan-of-care documentation before it moves to scheduling. |
| **TIC (Time to Initial Care)** | Time from referral acceptance to first patient visit. Medicare/payer compliance clock starts at referral date. |
| **Plan of Care (POC)** | Physician-approved treatment plan specifying visit frequency, disciplines, goals for the cert period (typically 60 days). |
| **Auth / Off** | Authorization from a non-Medicare payer for a specific number of visits. Required before those visits can be scheduled. |
| **POSFC** | Physician Order for Start of Care — resets the TIC clock when a patient isn't available within the 48-hour window. |
| **Recertification (ROC)** | Renewing a patient's plan of care at the end of a cert period if continued home health is needed. |
| **Buddy Codes** | Medicare billing codes required in certain states (e.g., cosign codes for therapy in Ohio and California). |
| **Smart Scheduling** | HCHB feature to auto-assign clinicians by skills, proximity, availability. Previously piloted and failed due to change management, not technology. |
| **Pulse** | Compassus's utilization review tool — DCS ensures visit frequency is clinically appropriate and Medicare-aligned before POC finalized. |
| **Point Care** | HCHB's clinician-facing mobile app. Runs on Citrix. Requires manual sync — changes are not real-time. |

## Home Health Capacity & Scheduling — Consolidated Summary

> **Source:** Google Drive — "HH_Capacity_Scheduling_Summary." Consolidated meeting summary and foundational
> knowledge base, from a working-session transcript plus multi-perspective expert extrapolation. Purpose:
> foundation for functional requirements of a scheduling & capacity automation platform. Rendered faithfully.
> A lighter earlier draft ("Foundational Knowledge for Home Health Capacity and Scheduling") and the raw
> four-perspective chat log are the same material at lower fidelity — this document supersedes them.

### Executive Summary

Capacity and scheduling are treated as a **single undifferentiated problem** in current branch practice, and
that conflation is itself a root cause of the operational failures. **Capacity is a planning function** — what
the branch can absorb. **Scheduling is an execution function** — who goes where, when. They operate on
different time horizons, are owned by different roles, respond to different inputs, and fail in different ways.
Because branches manage both through the **same artifact — a manually maintained spreadsheet grid** — neither
function is performed well, and the connection points between them are invisible.

#### Principal Findings

- **SOC clinician availability is the binding constraint on branch growth.** When SOC-capable clinicians are fully consumed by routine visit volume, the branch cannot admit new patients regardless of referral demand.
- A **self-reinforcing stagnation cycle**: full caseloads prevent admissions, absence of admissions prevents caseload turnover, and the branch stays locked at its current volume indefinitely.
- Capacity is calculated manually, in spreadsheets, at branch-level discretion. No standardized method, no shared definition of an open slot, no real-time view of where capacity exists.
- Scheduling operates on a **weekly build with continuous mid-week disruption.** The plan is finalized early; last-minute orders, cancellations, and condition changes then force continuous manual reconstruction.
- **Branch-to-branch variability is extreme and unmanaged.** High performers reassign coverage in minutes; low performers take hours, during which clinicians idle and patients wait.
- The **intake-to-scheduling handoff** is the most consistently cited communication failure.
- Productivity data exists but is **not actionable in native form** — it must be exported and manually reprocessed in Excel.
- **Clinician retention is materially affected by scheduling quality.** Overload, unpredictable additions, excessive reassignment travel, and repeated calls to the branch are burnout contributors.
- **Patients evaluate the agency almost entirely through scheduling reliability** — punctuality, caregiver consistency, and proactive communication of change.

### 1. Why Capacity and Scheduling Must Be Separated

| Dimension | Capacity Function | Scheduling Function |
|---|---|---|
| Question answered | How much can this branch absorb, and where? | Who performs which visit, when, in what order? |
| Time horizon | Forward-looking — weeks to months | Immediate — current week, day, next hour |
| Primary owner | Branch leadership; clinical management | Scheduler; branch coordinator |
| Core inputs | Clinician roster, discipline mix, SOC eligibility, territory coverage, caseload census, productivity targets | Confirmed orders, visit frequency, clinician daily availability, geography, patient preference |
| Core output | A stated ability to accept referrals — the open-slot count | A confirmed visit assignment on a specific clinician's day |
| Failure signature | Stagnant growth; declined/missed referrals; unused clinician time | Missed visits; late arrivals; idle hours; excess travel; patient dissatisfaction |
| Current artifact | Manual scheduling grid (spreadsheet) | Manual scheduling grid (spreadsheet) + scheduling console |

**The final row is the crux.** Both functions run through the same spreadsheet, so capacity planning collapses
into day-to-day scheduling reaction and the branch has no forward view of its ability to grow.

**Consequence of conflation:** the urgent displaces the important ("who can take this visit tomorrow" is asked
dozens of times a day; "what can this branch absorb in three weeks" is never asked). And it becomes impossible
to tell whether a failure is a *capacity* failure (insufficient SOC clinicians → hire/redistribute) or a
*scheduling* failure (available capacity that wasn't located → visibility tooling). The branch can't
distinguish them, so it can't correctly remediate either.

### 2. Capacity Functions

#### 2.1 Start-of-Care Capacity — The Binding Constraint
- SOC clinicians are those qualified and available to admit new patients — the critical determinant of growth.
- SOC capability is **distinct from general visit capacity**: a clinician may have room for routine visits and still be unable to accept an admission.
- **The Overload Cycle:** clinicians perpetually full with routine visits → no bandwidth for SOC admissions → no new patients → no growth → no added capacity → still overloaded. Repeats indefinitely. The loss is "unused capacity that halts branch growth" — capacity that exists in principle but can't be reached in practice. A single clinician's inability to admit can cascade into delays across broader schedules.
- **Undefined:** SOC eligibility criteria; the exchange rate between SOC and routine capacity; reserve-capacity thresholds against expected referral volume.

#### 2.2 Caseload Balance and Clinician Loading
- Both directions of imbalance carry cost: overloading restricts admissions and drives burnout; underutilization is direct revenue loss.
- Monitoring is intended to be real-time but is in practice **retrospective and manual** (daily productivity reports each branch runs).
- **Point-maximizing optimization can inadvertently overload clinicians** — the target is productivity, not sustainability.
- **Undefined:** productivity expectation standards (market/discipline variation); a visit-type weight table; how caseload weight accounts for acuity/duration/travel; NVA (non-visit activity) policies.

#### 2.3 Capacity Visibility and Measurement
- Branches struggle to know where clinicians are and what their capacity is at any moment.
- Capacity is expressed as **open slots** on a grid (SOC slots + routine slots). Once filled, the branch has no further capacity absent cancellations.
- **Undefined:** what a slot *is* (visit? time block? point allocation? admission?); whether slots are discipline-/territory-specific or fungible; the calculation that converts roster + targets into a slot count. Capacity is visible only as a present-tense count; **there is no forward projection.**

#### 2.4 Capacity Planning Horizon
- Short-term reaction supplants long-term strategic growth. No forecasting mechanism exists; capacity is assessed reactively against present demand.
- **Aspiration:** predictive analytics in productivity reporting; capacity gaps identified days in advance; dynamic demand forecasting.
- **Undefined:** the planning horizon (week/month/quarter); what a forecast consumes (referral-source trend, seasonality, episode length, discharge rate).

#### 2.5 Capacity and Financial Performance
- Branch financial health is tied directly to capacity-management accuracy. Both overstaffing and underutilization are named harms.
- **Undefined:** the cost of a missed admission, an idle clinician hour, or an unbackfilled cancellation. The capacity↔revenue relationship is asserted but not modeled.

### 3. Scheduling Functions

#### 3.1 The Weekly Schedule Build
- Schedulers finalize the week early, assigning visits from existing caseloads and grid slots; the plan is a baseline expected to be modified.
- **Failure:** any new order requires manual reconstruction, not incremental addition; the build reserves no capacity for known-coming disruption.
- **Undefined:** the build sequence and decision logic; the day it occurs and horizon covered.

#### 3.2 The Scheduling Grid (the single most-referenced artifact)
- A manually maintained spreadsheet listing open slots, updated by clinician availability. Contents: clinician names, open slots, SOC capacity, routine open-slot counts, current assignments.
- Efficient branches update it dynamically through the day; inefficient branches update weekly or by hand.
- **Failures:** manual updates are slow and error-prone (double-booking, delayed slot calc); not synchronized in real time (clinicians can't self-serve); no standardization → no cross-branch view.
- **Undefined:** exact column/row structure; write access and concurrent-edit handling; its relationship to the scheduling console (duplicate? supplement? contradict?).

#### 3.3 Real-Time Monitoring and the Scheduling Console
- Tracks clinician assignments and **points** in real time; points adjust dynamically as needs evolve.
- **The point system is undefined — the single most significant gap**, because points are the unit in which both capacity and scheduling decisions are denominated.

#### 3.4 Disruption — Last-Minute Orders
- Routine and expected. Scheduler options: redistribute across the team, ask a clinician to absorb more, call clinicians to negotiate, or request help. Resolution depends on scheduler judgment and clinician goodwill, not defined process.
- **Undefined:** the decision tree (order of options, constraints checked, escalation path); acceptable clinician notice period.

#### 3.5 Disruption — Cancellations and Fallback
- Cancellations create slots that must be backfilled to avoid idle time. Efficient branches reassign in minutes; inefficient ones take hours (clinicians call in to hunt for fallback visits).
- **Failures:** wasted clinician time, long travel on distant fallback visits; absence of fallback mechanisms is a named burnout contributor.
- **Undefined:** cancellation frequency/timing/reason codes; fallback acceptability rules (proximity, discipline match, continuity); whether a clinician may decline a fallback.

#### 3.6 Mid-Week Adjustment and Patient Condition Change
- Deterioration requires urgent unplanned visits; schedulers redistribute dynamically.
- **Undefined:** prioritization rules for whose visit is displaced; clinical urgency tiers and who assigns them.

#### 3.7 Geography and Travel
- Reducing redundant/long-distance same-day travel is a named clinician-wellness factor; rural/remote patients face access gaps.
- **Undefined:** how territory is defined/assigned; whether travel time counts toward productivity; distance/drive-time thresholds.

#### 3.8 Communication as a Scheduling Function
- The **intake↔scheduling handoff is the most-cited communication breakdown.** Late/absent updates on orders, SOC visits, and cancellations directly slow scheduling and idle clinicians.
- **Undefined:** handoff content/format/channel; expected turnaround between intake receipt and scheduler notification.

### 4. Connection Points Between Capacity and Scheduling

Where a capacity decision constrains a scheduling action, or a scheduling action changes the capacity picture —
the points where the manual system loses information and automation yields the most gain.

| # | Connection Point | Direction & Nature |
|---|---|---|
| CP-1 | Open-slot count → visit assignment | Capacity constrains scheduling. The grid's slot count is the authority; a stale/miscalculated count corrupts every downstream assignment. |
| CP-2 | Visit assignment → remaining capacity | Scheduling consumes capacity. Each assignment should decrement slots in real time; currently a manual, inconsistent recalculation. |
| CP-3 | SOC capacity → admission acceptance | **Capacity gates growth. The highest-value connection point in the system.** |
| CP-4 | Cancellation → recovered capacity | Scheduling restores capacity. Speed of recognition decides whether the slot is reused or lost — where fallback operates. |
| CP-5 | Point totals → caseload balance | Scheduling reports into capacity. Points are the shared currency of both domains — **and are undefined.** |
| CP-6 | Productivity reporting → capacity assessment | Scheduling data informs capacity judgment but needs manual Excel processing to become usable. |
| CP-7 | Territory coverage → assignment feasibility | Capacity is geographically bounded; open points in the wrong territory aren't usable capacity for a given patient. |
| CP-8 | Intake order flow → capacity signal | External demand meets internal capacity — the most-cited communication failure. |
| CP-9 | Clinician sustainability → sustained capacity | Scheduling quality preserves or destroys capacity; burnout → turnover → capacity loss, a slow invisible loop. |
| CP-10 | Patient continuity preference → assignment freedom | Continuity is a patient priority that reduces substitution options during disruption. |

**CP-3 governs whether the branch grows. CP-4 governs whether the branch wastes what it already has. CP-5
underlies both and is undefined.**

### 5. Stakeholder Perspectives (condensed)

- **Branch Executive Director (growth & finance):** growth is gated by SOC availability; the overload cycle halts growth; both overstaffing and underutilization hurt margin; wants central/automated scheduling with forecasting, unified cross-branch protocols, and real-time intake↔exec communication.
- **Tenured RN (workload & sustainability):** perpetual full caseloads leave no bandwidth for admissions; point-maximizing overloads clinicians and risks care quality; burnout (no fallback, long travel, repeated branch calls) drives turnover; wants balanced caseloads, branch-level fallback, and real-time visibility.
- **Senior Scheduler (execution):** lives in productivity reports + availability grids; real-time capacity swings with cancellations/last-minute orders; manual grids are slow and error-prone; branch disparity is stark; wants real-time capacity tracking, automated grid updates, centralized tools, and instant intake→scheduling flow.
- **Patient Panel (experience & trust):** punctuality, caregiver continuity, and proactive communication of change are the determinants of trust; cancellations without notice and lost continuity erode it; rural patients face access gaps. **Closing statement:** *"Schedule your clinicians around us — our care needs, our urgency, and our preference for consistency — not just around branch metrics and tools."*

### 6. Current Tooling Landscape
- **HCHB:** productivity tracking; data must be exported to Excel and manually interpreted; reports applied non-uniformly across branches.
- **Excel / manual processing:** raw data lacks actionable insight until refined; also hosts the scheduling grids; value depends on individual scheduler/manager skill (training crucial).
- **Scheduling console:** real-time tracking of assignments and points against targets.
- **Stated limitations:** reports need refinement; no standardized real-time tool; over-reliance on manual, inconsistent practice; real-time updates and comprehensive reporting don't currently exist.

### 7. Recommendations Surfaced (as stated, unprioritized)
- **Standardization:** automated platforms integrated with real-time capacity tracking; unified cross-branch protocols; a universal capacity-updating pattern; consistent training; dynamic schedule updates.
- **Automation / real-time:** real-time platforms reducing manual load; automated grid updates; auto-adjust for workload and referrals; automated fallback triggers; real-time capacity dashboards.
- **Predictive:** analytics detecting future capacity gaps; proactive capacity/need prediction; gaps identified days ahead; dynamic demand forecasting.
- **Communication:** bridge operational↔clinical; streamline intake↔exec; standardized intake→scheduling→clinician protocols; automated patient/clinician change notifications; scheduling-update alerts.
- **Workforce/training:** analytics training; branch accountability for equitable case distribution; predictive workload tools supporting retention.

### 8. Consolidated Failure Catalog (by domain)

- **Capacity:** SOC scarcity blocks admissions; overload cycle locks volume; underutilization = paid-for-no-revenue; overstaffing = expense without volume; no centralized capacity view; slow error-prone slot calc; grid cadence varies; no forward projection; short-term reaction displaces strategy.
- **Scheduling:** weekly rebuild on disruption; double-booking risk; grid not real-time; last-minute orders with minimal notice; hours-long fallback in low performers; geographically poor fallback assignments; clinicians repeatedly call the branch; intake fails to relay changes; urgent changes displace visits without rules; productivity data needs manual reprocessing; wide branch variance with no closing mechanism.
- **Workforce:** burnout from overload + no fallback; point-maximizing overloads; inequitable case distribution; tool value depends on individual skill.
- **Patient:** cancellation without notice; lost caregiver continuity; missed routine visits harming chronic care; rural access gaps; reduced time per patient under overload.

### 9. Open Questions & Discovery Requirements (ordered by dependency)

**9.1 Foundational — blocks all downstream definition**
- **The point system** — what a point represents; values by visit type & discipline; daily/weekly targets by clinician type; who sets them; how points relate to time; how travel is treated. *Shared currency of capacity and scheduling; referenced everywhere, defined nowhere.*
- **The scheduling grid, reconstructed field by field** — columns, rows, update triggers, ownership, access, embedded calculations. *Becomes the initial data model.*
- **The definition of an open slot** — visit / time block / point allocation / admission; discipline- and territory-specificity; the slot-count formula.

**9.2 Capacity mechanics** — SOC eligibility criteria; SOC↔routine exchange rate; balanced-caseload target ranges & hard limits by discipline; how acuity/duration factor into caseload weight; planning horizon and forecast inputs; reserve-capacity policy.

**9.3 Scheduling mechanics** — weekly build sequence; last-minute-order decision tree; fallback rules (proximity, discipline match, continuity, decline rights); urgency tiering; cancellation data (frequency/timing/reasons); clinician notice-period standards.

**9.4 Constraints & rules** — territory definition/assignment/boundaries; discipline & licensure constraints; visit-type taxonomy (SOC, recert, ROC, routine, discharge) and attached rules; patient-preference capture and binding strength; whether travel counts toward productivity.

**9.5 Interfaces & data flow** — intake→scheduling handoff (fields/channel/format/turnaround); order lifecycle upstream of scheduling; console display/actions vs. grid contents; roles & permissions for schedule changes.

**9.6 Economics** — cost of a missed admission; of an idle clinician hour; of an unbackfilled cancellation; of turnover attributable to scheduling quality. *Not required to design the platform, but required to prioritize what it builds first.*



# Part III — The Strategy: Battle-Plan Logic

## Capacity Strategy Foundation — the Battle-Plan Logic

> **Purpose.** The strategic spine beneath the capacity tool: *what actually controls home-health branch
> capacity, in what order, and how each layer becomes tool logic and AI-agent behavior.* Grounded in the
> operator's SME download (Colin Highland, Jul 2026) and the Compassus discovery ([`../knowledge/`](../knowledge/)).
> This is v0 — the frame the SME discovery ([`../sme/sme-discovery-framework.md`](../sme/sme-discovery-framework.md))
> fills in and corrects.
>
> **Core principle.** Capacity is not one number to optimize; it is a *stack of controllable layers*, each of
> which caps the ones above it. You cannot day-to-day-schedule your way out of a broken staffing model, and you
> cannot staff your way out of a broken culture. Fix the stack bottom-up; manage it top-down.

### The capacity stack (the hierarchy of effectors)

```
                       ┌─ referrals must already exist ─┐   (precondition, not the capacity problem)
                       ▼                                 │
  ┌───────────────────────────────────────────────────┐ │  LAYER 1 · PRIMARY EFFECTOR
  │ STAFFING MODEL — balanced at every discipline,     │ │  "A branch cannot affect capacity if it is not
  │ unique to the market, SOC capacity as known slots  │ │   staffed appropriately at all discipline levels."
  └───────────────────────────────────────────────────┘ │
  ┌───────────────────────────────────────────────────┐ │  LAYER 2 · CONTROLLABLE PREPARATION
  │ TERRITORY — caseload distribution + resting posture │ │  Set clinicians so coverage + referral absorption
  │ so coverage & absorption are near-automatic         │ │  is nearly automatic.
  └───────────────────────────────────────────────────┘ │
  ┌───────────────────────────────────────────────────┐ │  LAYER 3 · DAILY MANAGEMENT
  │ DAY-TO-DAY — availability · patient willingness ·   │ │  Where the tool's cockpit + directive engine live.
  │ logistics · per-diem coordination                   │ │
  └───────────────────────────────────────────────────┘ │
  ┌───────────────────────────────────────────────────┐ │  MULTIPLIER (spans all layers)
  │ CULTURE & LEADERSHIP — protection → discretionary   │◀┘  Turns a good model into extra yeses; a bad one
  │ effort; reciprocity; respect + accountability       │    into quiet quitting and turnover.
  └───────────────────────────────────────────────────┘
```

Read it two ways: **each lower layer sets the ceiling for the layers above it** (staffing caps territory caps
day-to-day), and **culture multiplies whatever the stack produces** (a well-run day-to-day with a resentful
team leaks capacity; a lean model with a protected team punches above its weight).

---

### Layer 0 — Referrals (precondition)

Capacity is only a question once referral flow exists. Referral demand is *not* a capacity lever the branch
tunes to "make capacity"; it is the load the capacity stack must absorb. **Implication for the tool:** referral
inflow is an input to size and stress-test the model, never a substitute for fixing staffing. Accepting
referrals a branch cannot staff destroys quality, timeliness, and referral-source trust faster than declining
would.

### Layer 1 — Staffing model (the primary effector)

**The thesis:** the staffing model is what a branch can *change* to move capacity the most. It must (a) be
**balanced at every discipline level**, (b) be **unique to the market's potential**, and (c) treat **SOC
capacity as a managed, known-slot resource.**

#### 1.1 Discipline balance — the offload structure
Assessing clinicians (RN, PT, OT, SLP) are the scarce, capacity-governing resource. Assistants (LPN, PTA, COTA)
exist to **absorb routine visits so assessing clinicians stay free for what only they can do.**

- Too few **LPNs** → RNs carry too many routine visits → RN assessment/SOC capacity collapses → admissions stall.
- Too few **PTAs** → PTs carry too much routine therapy → PT eval/SOC capacity collapses.
- The lever is the **RN:LPN and PT:PTA ratio**, derived from the branch's *case mix* (visit-type distribution),
  not a national default.

> **Rule (tool + agent):** treat an assessing clinician whose schedule is >X% routine visits while assistant
> capacity sits open as a **mis-offload** signal — the first thing to fix before declaring a capacity shortage.
> The directive engine's assessing→assistant offload already gestures at this; the staffing view must show the
> *structural* imbalance, not just the daily one.

#### 1.2 SOC capacity as known slots
Many strong branches run **SOC-dedicated nurses (and sometimes SOC-dedicated PTs)** who see *only* SOCs/ROCs.
This converts the branch's most growth-critical capacity from "whatever's left over" into **predictable, bookable
slots** — capacity you can plan and sell against.

- **SOC assignment rule (authoritative — corrects the tool's current approximation):**
  - **RN performs any SOC where nursing is tied to the case.**
  - **PT performs the SOC only when nursing is NOT on the referral.**
  - (ROC follows the same discipline logic on the recert cycle.)
- **Known-slot model:** a dedicated SOC role has a countable weekly SOC capacity; the tool should track SOC
  slots *as their own resource*, separate from routine-visit capacity, because they are the binding constraint
  on growth (discovery CP-3).

> **Rule (tool + agent):** SOC-eligibility is **not** "any RN/PT." It is: RN whenever nursing is on the case;
> PT only when nursing is absent. The matcher must encode this and must protect dedicated-SOC roles from routine
> overflow (routine assigned to a SOC nurse is capacity leakage).

#### 1.3 Market-uniqueness
The same census requires a **different model in different markets** — geography/density, payer & case mix,
referral-source profile, rural vs. urban, seasonality. A model that works in dense urban Charleston fails on a
rural loop. **Implication:** the tool should hold a *per-market staffing model* (target ratios, SOC roles, flex
depth) rather than one global template, and flag branches drifting from their market-appropriate model.

### Layer 2 — Territory management (controllable preparation)

Territory is the **controllable variable that pre-positions capacity** so day-to-day management is easy. Tie
caseload distribution to data and logic, and set each clinician into a territory that gives the most effective
**"resting posture"** — so that **coverage of active clients and absorption of new referrals is nearly
automatic**, not a daily scramble.

- A good resting posture = a clinician's active caseload is geographically coherent, leaving natural headroom
  and short travel to absorb a nearby new referral without disruption.
- Territory is where you *bank* future ease: the better the resting posture, the fewer heroic day-to-day moves.

> **Rule (tool + agent):** measure territory *health* — caseload geographic coherence, overlap/coverage per
> zip, absorption headroom by discipline — as a **preparation-layer signal**, distinct from today's open points.
> The agent should treat a referral that lands in a well-posture'd territory as low-friction and one that lands
> in a fragmented territory as a flag to fix posture, not just to force an assignment.

### Layer 3 — Day-to-day management (where the tool operates)

Given a sound model and good territory, daily capacity management is **clinician availability, patient
willingness, and logistics** — plus **per-diem coordination**, which branches struggle with because it's
planning- and communication-heavy. This is exactly where the capacity cockpit + directive engine earn their
keep: **making the need visible** so per-diem and flex capacity can be deployed cleanly.

- Per-diem is a **flex layer**, not a substitute for core staffing; heavy reliance on it is a Layer-1 signal.
- A good tool improves per-diem management primarily by **visualization** — the team can see the need clearly,
  early, and match it to available flex.

> **Rule (tool + agent):** surface per-diem need *ahead of time* (forecasted gaps by discipline/zone/day),
> track engagement/disengagement, and make the coordination a one-click ask. But if per-diem is being used to
> paper over a structural gap, the agent should say so (escalate to Layer 1), not just keep booking flex.

### Multiplier — Culture & leadership

Culture decides whether the stack's theoretical capacity is *realized*. Clinicians go the extra mile — one more
PT eval on a Friday, one more SOC near full — **when the branch has earned it** by protecting them.

- **Reciprocity is the mechanism.** The nurse whose manager quietly offloaded her visits during a hard personal
  week is the nurse who says "yes" to the out-of-territory Friday visit later. Protection banked becomes
  discretionary effort withdrawn.
- **Respect + accountability** are the two rails: clear policies/processes that make the normal day better, and
  fair, consistent expectations across the team.
- Discretionary effort is **real capacity** — but it is *borrowed*, and it must be repaid or it disappears (and
  takes the clinician with it, on a turnover lag).

> **Rule (tool + agent):** the tool should make protection *legible and fair* — track who's been asked to stretch,
> whether the team is sharing the load equitably, and whether stretch is being repaid (lighter following week).
> **The agent must treat discretionary effort as a scarce, borrowed resource:** ask the clinician the branch has
> protected, frame it as a favor not an order, never ask the same person repeatedly, and never let an "ask"
> become the default coverage plan. Exploiting the yes destroys the culture that produced it.

---

### Capacity business rules (v0) — for the tool and the agents to enforce

Distilled from the above; each is a candidate for the matching engine + agent training. Mark ✔ where the tool
already does it, ✎ where it needs building.

| # | Rule | Status |
|---|---|---|
| SOC-1 | RN performs any SOC where **nursing is on the case**; PT performs the SOC **only when nursing is not on the referral**. ROC follows the same logic. | ✎ (tool currently treats any RN/PT as SOC-capable) |
| SOC-2 | Track **SOC/ROC slots as a distinct capacity resource**; protect dedicated-SOC roles from routine overflow. | ✎ |
| BAL-1 | Flag an assessing clinician running **>X% routine** while assistant capacity is open (a mis-offload / discipline-imbalance signal) before declaring a shortage. | ~partial (daily offload exists; structural view ✎) |
| BAL-2 | Hold a **per-market staffing model** (RN:LPN, PT:PTA, SOC roles, flex depth); flag drift from market-appropriate ratios. | ✎ |
| TERR-1 | Score **territory health** (caseload coherence, coverage per zip, absorption headroom) as a preparation-layer signal. | ✎ |
| DAY-1 | **Enforce restrictions/competencies** in matching ("No SOC", "No wound care", "No high-acuity", "Recerts only", "Weekends only") — hard filter, never just displayed. | ✎ (current correctness gap) |
| DAY-2 | Debit **travel + non-visit work** from capacity, not just visit points; use **drive-time**, not straight-line distance. | ✎ |
| PD-1 | Surface **per-diem need ahead of time**; track engagement; escalate to Layer 1 when flex is covering a structural gap. | ~partial (disengagement flag exists) |
| CUL-1 | Make discretionary effort **legible and fair**: track asks, load-sharing equity, and repayment (protect after stretch). | ✎ |
| CUL-2 | Agent **must not** exploit the yes: ask the protected clinician, frame as favor, never repeat-ask the same person, never make the ask the default plan. | ✎ (agent guardrail) |

### How this drives the tool and the AI agents

- **Tool:** the strategy stack maps to views. Layer 1 → a *staffing-model / discipline-balance* view (not just a
  roster). Layer 2 → a *territory-health* view (beyond the current capacity map). Layer 3 → the cockpit
  (exists). Culture → a *fairness/stretch-ledger* signal. Each layer needs its own leading indicators.
- **AI agents:** every directive the engine emits should carry its **layer** and respect the **business rules**
  above. A day-to-day directive that violates a Layer-1 truth (e.g. "just have the RN take more routine") is
  wrong even if it balances today. Agents are trained on the **tactics library** ([`../sme/`](../sme/)) —
  SME-sourced, validated patterns of what great branches actually do — so their recommendations reflect real
  operating wisdom, not just the math.

### Open strategic questions (for SME discovery)

- The **X% routine threshold** that signals RN/PT mis-offload — what is it, by discipline?
- Target **RN:LPN / PT:PTA ratios** by case-mix archetype — what are the real numbers?
- When is a **dedicated SOC role** justified (referral inflow / SOC-ROC volume threshold)?
- What defines a healthy **resting posture** quantitatively (coherence, headroom)?
- How much **per-diem flex** is healthy vs. a red flag?
- How is **discretionary effort** best made fair and repaid without turning it into a metric people game?



# Part IV — SME Knowledge & Tactics

## Capacity Tactics Library (v0 — SME-seeded)

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

### The five things every SME lens converged on

1. **Capacity is created at the SOC/assessment slot, and most often lost because the assistant tier (LPN/PTA) is understaffed.** *Never diagnose "we're full" without decomposing skilled clinicians' days by visit type.* (ED, DCS, Scheduler, Strategist)
2. **SOC capacity is protected inventory, routed by clinical law** — RN for any SOC where nursing is on the case; PT only when nursing is not. Raiding SOC slots for routine overflow silently kills growth. (All five)
3. **Capacity ≠ visit count.** True load = visit + drive + documentation + coordination + acuity. Visit-point-only math overloads the efficient clinician and looks balanced doing it. (DCS, Scheduler, RN, Strategist)
4. **Discretionary effort is a borrowed, exhaustible resource governed by reciprocity and fairness.** The naive optimizer burns the reliable clinician first; protect them or lose them on a turnover lag. (ED, DCS, Scheduler, RN)
5. **The tool/agent is part of the culture and can't be neutral.** Propose don't dispose; show the cost; enforce scope and compliance as hard rails; never manipulate. (All five)

---

### Layer 1 — Staffing model (primary effector)

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

### Layer 2 — Territory (controllable preparation)

| # | Tactic | Encode as (system) | Agent behavior / guardrail | Source · confidence |
|---|---|---|---|---|
| L2-1 | **Resting-posture territory design** — caseload band below ceiling, keyed to referral density, so absorption is automatic | Territory + target caseload band w/ headroom; headroom-by-territory (green/amber/red); rebalance flag | Route to in-territory clinician *with real headroom*; protect slack; don't fill everyone to the top | ED, DCS, Scheduler, RN · **high** |
| L2-2 | **Zone coverage floor** — ≥1 admit-capable clinician per active zone; zone slack ≥ expected daily referrals | `Zone_floor_FTE_z`; flag "coverage hole" even when branch aggregate is positive | Check capacity at *zone* level; a positive branch number can hide a leaking corner; cross-cover before hire | Strategist · **med** |
| L2-3 | **Territory-health as a structural signal** — chronic cross-territory routing = the map is wrong | Detect cross-territory routing + unabsorbed referral clusters; surface to leadership | Escalate the *pattern* as a territory-design finding, not more daily stretch-asks | RN, Scheduler · **high** |

### Layer 3 — Day-to-day management (the cockpit)

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

### Multiplier — Culture & leadership

| # | Tactic | Encode as (system) | Agent behavior / guardrail | Source · confidence |
|---|---|---|---|---|
| C-1 | **Offload-as-protection / reciprocity ledger** — proactively lighten a spiked clinician; bank the yes | `recent_spike_score`; proactive "protection offload"; bidirectional reciprocity ledger; fairness skew flag | Recommend relief before burnout; prefer the *un-tapped* clinician for asks; surface imbalance to leadership; **never exploit the reliable yes** | ED, DCS, Scheduler, RN · **high** |
| C-2 | **The ask that gets a yes** — specific, early, honestly-sized (drive+doc), refusable without penalty | Structured ask payload (time, drive delta, doc load, why-you, one-tap penalty-free decline); notice-lead-time flag | Frame concretely/early/honestly; **never** use guilt/urgency/scarcity/patient-welfare-as-leverage; a "no" is data | RN, Scheduler · **high** |
| C-3 | **Clear-policy protection** — encode branch policy so a stretch-ask is always safe & cited | Policy thresholds as config (after-hours, weekend, "at capacity," decline-allowed); asks cite the policy basis | Only ask inside encoded policy, cite it; escalate out-of-policy needs to the manager; never invent expectations | ED · **med** |
| C-4 | **Continuity of caregiver (default, bend at break points)** — protect for wound/decline/psych/EOL/active SOC | `continuity_sensitivity` (protect/flexible); optimizer honors "protect"; continuity as an outcome metric | Default to established caregiver; trade only on flexible-tagged patients w/ stated tradeoff; flag warm-handoff when it must break | RN · **high** |
| C-5 | **Burnout/turnover = capacity decay on a lag** — optimize the quarter | Leading burnout indicators; utilization ceiling requiring override; turnover cost in forecasting | Treat sustained overload as a cost not a success; reduce asks + flag when indicators trip; never grind the best people because they haven't quit yet | RN, ED · **high** |
| C-6 | **Human override is sacred** — clinician ground truth beats the model | Capture every override + reason as training signal; neutral decline logging; override-pattern = model defect | Treat clinician input as authoritative on the ground; never re-ask a considered no, argue, or treat overrides as non-compliance | RN · **high** |

---

### Cross-cutting agent guardrails (the "never" list — apply to every directive)

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

### Parameters to validate (the "open numbers")

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

### How the tool and agents consume this

- **The matching/directive engine** should tag every directive with its **layer** (L1/L2/L3/C) and pass it through the guardrails above before surfacing it. A day-to-day directive that violates a Layer-1 truth (e.g. "just have the RN take the routine") is wrong even if it balances today.
- **Agent training** draws each row's *situation → correct reasoning → recommended action → prohibited action* as an example. The `perspectives/` briefs are the long-form training source; this library is the indexed, deduplicated spec.
- **SME validation** works this table top-down: confirm/correct/kill each tactic, fill the real "open numbers," and promote high-confidence rows into the tool backlog + the strategy's business-rules set.

## SME Discovery Framework — sourcing tactics, building the agents

> **Purpose.** A repeatable way to (1) pull real capacity-management tactics from home-health subject-matter
> experts, (2) validate them, and (3) turn each into **tool logic** *and* **AI-agent training**. This is how the
> capacity strategy ([`../strategy/capacity-strategy-foundation.md`](../strategy/capacity-strategy-foundation.md))
> gets filled in, corrected, and kept honest by the people who actually run branches.
>
> **The premise.** Great branches already know how to manage capacity — the knowledge is tacit and unevenly
> distributed. The job is to *extract it, structure it, and encode it* so every branch (and every AI agent in
> the tool) operates like the best one. We are not inventing tactics; we are harvesting and systematizing them.

### The pipeline

```
  SME  ──▶  tactic captured  ──▶  validated  ──▶  ┬─▶  SYSTEM RULE (measure / flag / enforce)
 (interview   (structured        (cross-checked    │
  or panel)    schema)            vs data + peers)  └─▶  AGENT TRAINING (reason / recommend / guardrail)
```

Every tactic ends life as **at least one of** a system rule or an agent-training example — usually both. A
tactic that can't be turned into either is a story, not a tactic; log it as context and move on.

### The SME roster (whose perspective we need)

Sourced to the capacity stack — each layer has owners who see it best. Prioritize the **top-performing branch's**
version of each role; the goal is to encode what the *best* do.

| Layer | SME roles to interview | What only they can tell us |
|---|---|---|
| Staffing model (L1) | **Branch Executive Director**, **Workforce/Staffing Strategist**, Area/Regional VP | Discipline-ratio truth, market-unique sizing, when to create a SOC role, unit economics |
| Clinical ops (L1↔L3) | **DCS / Clinical Manager** | Offload discipline, SOC/ROC assignment, acuity judgment, compliance-as-constraint |
| Territory (L2) | Branch Director, **senior Scheduler**, tenured field clinicians | Resting posture, caseload distribution, drive-time reality |
| Day-to-day (L3) | **Senior Scheduler / Staffing Coordinator**, **Per-Diem Coordinator** | The last-minute decision tree, per-diem engagement, real availability |
| Clinician truth | **Tenured field RN / SOC nurse**, PT, per-diem clinician | What earns the "yes," continuity, burnout signals, what a tool must never do |
| Culture (multiplier) | Branch ED + clinicians together | Reciprocity, protection, fairness, accountability |
| Outside-in | Intake/referral coordinator, a **referral source** (discharge planner) | What makes them route to us; speed/certainty they buy |

**Seeded v0:** we've already generated *hypothesized* tactics from five of these lenses (Branch ED, DCS,
Scheduler, Field RN/SOC nurse, Workforce Strategist) — see the [tactics library](./capacity-tactics-library.md).
Those are **starting hypotheses to validate with real SMEs**, not settled truth. They make the interviews
faster: confirm, correct, or kill each, and add what we missed.

### The interview method

**Format.** 45–60 min, one role at a time; then a **cross-role panel** on the two or three tactics where roles
disagree (disagreement is signal — it's usually a real tension to design around, not a wrong answer).

**Opening frame (every interview):** *"Think about the best branch you've seen run capacity. What did they
actually do differently — day to day — that a struggling branch doesn't? Be specific."*

**Probe by layer** (skip what's not their lane):
- **Staffing:** "How do you know a branch is mis-staffed *before* census stalls? What ratio of RN:LPN / PT:PTA do
  you actually run, and why that number for this market? When do you create a dedicated SOC nurse/PT?"
- **SOC:** "Walk me through who takes a SOC when nursing is on the case vs. not. How do you protect SOC capacity
  from routine overflow?"
- **Territory:** "How do you decide who covers where? What does a well-set-up clinician's territory look like so
  new referrals just get absorbed?"
- **Day-to-day:** "It's Friday at 3pm and a SOC comes in for a full clinician's ZIP. Walk me through exactly what
  you do — who you ask, in what order, how you ask." "How do you keep per-diems engaged and ready?"
- **Culture:** "Tell me about a time a clinician went the extra mile. What had the branch done to earn it? What's
  the fastest way to burn that goodwill?"
- **The anti-pattern:** "What's the most common mistake branches make that looks fine on a report but is killing
  capacity?" (The Branch ED's answer — *never diagnose 'we're full' without decomposing skilled clinicians' days
  by visit type* — is exactly the kind of gold this question surfaces.)

**Closing:** "If an AI assistant were helping your scheduler tomorrow, what should it *always* do, and what must
it *never* do?" → this directly seeds agent guardrails.

### The tactic-capture schema

Capture every tactic in this exact shape (it's what makes a tactic buildable and trainable):

| Field | What goes here |
|---|---|
| **Tactic** | Crisp name + 1–2 sentences: what the great branch actually does |
| **Layer** | Staffing / Territory / Day-to-day / Culture (or precondition) |
| **Trigger / context** | When it applies |
| **Why it works** | The operational mechanism |
| **Encode as system logic** | The rule / threshold / signal / formula the tool computes or enforces |
| **Train the AI agent** | How the agent reasons or acts on it — including explicit *"must never do X"* guardrails |
| **Evidence / confidence** | SME source(s), whether data confirms it, confidence (hypothesis / SME-asserted / data-validated) |
| **Open number** | Any threshold/ratio that still needs a real value (routes to the strategy's open questions) |

### Validation — before a tactic becomes a rule

A tactic graduates from "SME-asserted" to "encode it" when it clears:
1. **Cross-role check** — does at least one other role agree, and is the disagreement understood?
2. **Data check** — do the branch's own numbers move the way the tactic predicts (where data exists)?
3. **Guardrail check** — is there a way this rule, automated, could harm a clinician or a patient? If yes, it
   ships with the guardrail, not without it. (Clinician-facing asks especially — see the field-RN "must never"
   list.)
4. **Falsifiability** — what would tell us this tactic is wrong here? Write it down; revisit.

### From tactic → the two products

- **System rule.** Goes into the capacity business-rules set (strategy doc) and the tool backlog: a measure, a
  flag, a threshold, a formula, or a hard filter in the matching engine.
- **Agent training.** Becomes a training example for the AI agents operating in the tool: the situation, the
  correct reasoning, the recommended action, and the *prohibited* action. Structured so a directive the engine
  emits carries its **layer** and respects the **guardrails**. The tactics library is the corpus; as it grows,
  it's the difference between an agent that does math and one that reasons like a good branch manager.

### Running list of "open numbers" to get from SMEs

These are the thresholds the strategy needs real values for (they route here from the strategy's open questions):
- RN routine-visit % that signals mis-offload (ED hypothesized ~20–25%) — by discipline, by market.
- Target **RN:LPN / PT:PTA** ratios by case-mix archetype.
- Referral-inflow / SOC-ROC volume that **justifies a dedicated SOC role**.
- Healthy **resting-posture headroom** per territory (quantified).
- Healthy **per-diem flex %** vs. the red-flag level that means core staffing is short.
- **Referral-to-SOC** target intervals by source type.
- The **fairness** mechanics of discretionary effort — how to make it equitable and repaid without gaming.

### Cadence

- **Round 1 (now):** validate the seeded v0 tactics with one SME per role; capture new tactics.
- **Round 2:** cross-role panel on the tensions; lock the "open numbers" you can.
- **Ongoing:** every branch rollout is a discovery site — the best branches surface new tactics; feed them back
  through the schema so the library (and the agents) keep learning.



# Part V — The Capacity Management Tool

## Capacity Tool — Mockup Data Spec (read from source)

> ### ⟳ As-built update (re-reviewed against `invisiblegears` `main` @ `6dba163`)
> The tool has been built out well beyond the version first reviewed below. It is now **9 tabs** with a real
> capacity-matching brain, and the **point system is resolved** (the visit-weight table). The authoritative
> field-level model is now the operator's **`ClinicianCapacityTool_DataIndex.xlsx`**. The original 4-tab
> description that follows is kept as history; **the current review is the "As-built review" section at the
> bottom of this file.**

> **What this is.** The exact data model of the operator's mockup, read directly from its source at
> `worker-max/invisiblegears`, branch `capacity-tool`, file `public/capacity-tool/index.html` (a self-contained
> HTML/JS artifact). This supersedes the inferred [`capacity-tool-data-index.md`](./capacity-tool-data-index.md)
> for *this* tool: that data index was the broad capacity-forecasting vision; **the mockup is a narrower, sharper
> thing** — see the reconciliation at the end.
>
> **What the tool is.** A **Clinician Capacity Management Tool** the wrapper describes as a *"re-creation of
> CenterWell's Worker Productivity Tool."* Four tabs: **Worker Productivity** (roster grid) · **Productivity
> Trends** (line chart) · **Visit Capacity Program** (compensation reference) · **Implications** (stakeholder
> scorecards). It imports a weekly roster (CSV/JSON), computes productivity vs. target, and reports it.
>
> **The big finding.** This tool *is* an operational instantiation of "the point system" — the shared currency
> that the Compassus discovery flagged as **open question #1, undefined, gating everything**
> ([`../knowledge/capacity-scheduling-summary.md`](../knowledge/capacity-scheduling-summary.md) §9.1). The
> mockup doesn't resolve that question; it *assumes it solved* by taking daily points as an input. That gap is
> the most important row in this document (see Gap G1).

---

### Entity 1 — Worker Weekly Productivity Record

The core entity. **One row per clinician per week.** These are the fields the import schema actually accepts,
plus the fields the tool computes from them.

#### 1a. Raw / ingested fields (the import contract — CSV & JSON §8.1)

| # | Field | Type / values | Notes | Candidate source |
|---|---|---|---|---|
| W1 | `lastName` | string | Grid freezes on "Last, First" | HCHB / Workday |
| W2 | `firstName` | string | — | HCHB / Workday |
| W3 | `discipline` | enum: **LPN, PTA, PT, RN, OT, COTA** (extensible) | Drives filters + pills | HCHB / Workday |
| W4 | `fteStatus` | enum: **FT, PT, Contractor** | Filter + PT/contract expected-points logic | Workday |
| W5 | `payMethod` | enum: **PPV, FEE_BASED, CONTRACT, SALARY, SALARY_PLUS** (labels: PPV / Fee Based / Contract / Salary / Salary Plus) | Contract ⇒ no target | Workday |
| W6 | `weeklyExpectedPoints` | number (e.g. **30** FT, **24** PT, **0** contract) | The productivity target | Config/policy → see Gap G5 |
| W7 | `pointsByDay.sun … .sat` | 7 numbers (points earned per day) | The heart of the data — daily productivity | HCHB visit/productivity report → see Gap G1 |
| W8 | `comments` | free text (e.g. "pto all week", "off mon", "prn", "baylor", "pto thu–fri", "part b", "rotates fri/mon off") | Explains variance | HCHB scheduler notes / manual |
| W9 | *week context* ("Week Of") | date (snapshot period, e.g. Jul 21 2024) | Which week this row is | Pay-period calendar → Gap G7 |

#### 1b. Derived fields (computed by the tool — do NOT source; but the *rules* must be agreed)

| # | Field | Formula in mockup | Notes |
|---|---|---|---|
| D1 | `dailyAvgExpected` | `weeklyExpectedPoints / 5` | Assumes a 5-day expectation |
| D2 | `totalPointsEarned` | `sum(pointsByDay)` | — |
| D3 | `variance` | `earned − expected` (null if contract) | Shown as (x) negative / x positive |
| D4 | `productivityPct` | `round(earned / expected × 100)` (0 if contract) | — |
| D5 | `contract` (flag) | `payMethod==CONTRACT` **or** `expected==0` | Excludes from targets/KPIs |
| D6 | `statusTier` | **Critical <25% · In Progress 25–89% · On Target 90–110% · Exceeded >110% · Not Set** | Handoff §3.3 thresholds — exact |

### Entity 2 — Reference / Configuration data

Small controlled lists and rules the tool needs to exist. Mostly config, not feeds — but each must be **agreed
and owned.**

| # | Reference set | Values in mockup | Candidate source |
|---|---|---|---|
| R1 | Disciplines | LPN, PTA, PT, RN, OT, COTA | Config (align to HCHB) |
| R2 | Pay methods | PPV, Fee Based, Contract, Salary, Salary Plus | Config (align to Workday/comp) |
| R3 | FTE statuses | FT, PT, Contractor | Config |
| R4 | Productivity status thresholds | 25% / 90% / 110% breakpoints (§3.3) | Policy (to ratify) |
| R5 | Week / pay-period list | Jul 21, Jul 14, Jul 07, Jun 30 2024 … | Pay-period calendar → Gap G7 |
| R6 | Region → Area hierarchy | North→{Metro North, Lakeshore}; South→{Gulf Coast, Piedmont}; West→{High Desert, Bay} | Org hierarchy → Gap G2 |
| R7 | Trend pay periods | Feb, Mar, Apr, May, Jun, Jul, Aug | Pay-period calendar |
| R8 | "Top 10 branches" cohort | benchmark comparison set | Branch ranking → Gap G3 |

### Entity 3 — Visit Capacity Program (VCP) compensation reference

The comp-policy layer the tool documents (Tab 3). Reference data today; a live tool would also need the
**actuals** (Gap G6).

**NVA Code Table**

| Field | Values in mockup |
|---|---|
| NVA Code | **5001** — Visit Capacity Adjustment; **5003** — Visit Capacity Adjustment |
| Payment Method | 5001 → Fee-Based Pay, Pay Per Visit · 5003 → Salary Plus |
| Weight | 0.25 unit |
| Who Enters | Branch Admin |

**Tier Threshold Table**

| Tier | Eligible Visits | Additional Comp |
|---|---|---|
| 1 | Up to 6 units above productivity target | 0.25 unit per applicable visit |
| 2 | 6+ units above productivity target | 0.50 unit per applicable visit |
| 3 (SOC) | All SOCs above productivity target | 0.50 unit per applicable visit |

**Business Rules to Enforce** (as written)
- NVA code entered by **branch admin or branch leader ONLY** — never the clinician.
- Branch **payroll designee reviews HCHB payroll reports** each pay period.
- **BD and/or Clinical Manager must approve each NVA entry in HCHB before Monday payroll close.**
- Codes **5001 / 5003** may be reported multiple times per pay period.
- **Eligibility:** clinician must already be **at or above weekly productivity target** before any tier applies.

### Entity 4 — Aggregations / KPIs (derived; recomputed under the active filter)

The Tab 1 KPI strip. All computed from Entity 1.

| KPI | Definition in mockup |
|---|---|
| Clinicians | count of workers (with "N on a target") |
| Avg Productivity | mean `productivityPct` across non-contract workers |
| At / Above 90% | count ≥90% (+ % of roster) |
| Critical <25% | count <25% |
| **Open Capacity** | `Σ expected − Σ earned` = **unearned points this week** → *"~points/6 visits of headroom"* |

> **Open Capacity is the whole point.** It reframes a productivity shortfall as *available capacity for new
> admissions* — the direct bridge to the growth/referral story (CP-3).

### Entity 5 — Productivity Trends series (aggregate)

Tab 2. Filters: **Region, Area, EE Type (All/FT/PT), Compare Top 10** (toggle).

| Data element | Detail | Candidate source |
|---|---|---|
| % of clinicians in **Low / Med / High** productivity group | per pay period (Feb–Aug), division-wide | Aggregation of Entity 1 across history |
| **Top 10** high-productivity series | benchmark overlay | Entity 1 filtered to Top-10 cohort (Gap G3) |
| Insights narrative | computed (division vs Top 10, headroom to close) | Derived |

### Entity 6 — Implications scorecards (derived per stakeholder)

Tab 4. One card per stakeholder group, computed live from the roster.

| Scorecard | Metric it computes |
|---|---|
| Clinician Experience | avg productivity; % at/above target |
| Scheduler / Leader | data completeness (% with visits logged this week) |
| Sales & Referral | open-capacity points → visit headroom |
| Workforce Management | % on FBP / salary (points-based) plans vs hourly |
| Culture Shift | week-over-week productivity trend |

### Import / Export contract

- **CSV columns (exact):** `lastName, firstName, discipline, fteStatus, payMethod, weeklyExpectedPoints, sun, mon, tue, wed, thu, fri, sat, comments`
- **JSON:** array of worker records per "handoff schema §8.1" (external spec, not in the repo — **get a copy**).
- **Export CSV** additionally emits derived `totalEarned, variance, productivityPct`.

---

### The gaps — data the mockup *assumes* but a real tool must actually source

The mockup runs on sample data and seeded trends. To make it real, these must be sourced. **This is the true
"war-list" target.**

| # | Gap | Why it matters | Where it must come from |
|---|---|---|---|
| **G1** | **The point-earning rules** — how `pointsByDay` is produced from real visits (visit type × discipline × weight) | This *is* the undefined "point system" (discovery open question #1). The mockup takes points as given; reality computes them | **HCHB visit records + a points/weight config** — define first |
| **G2** | **Worker → Branch → Area → Region mapping** | Tab 2 filters by region/area, but the worker record has no such field | Org hierarchy (HCHB/Workday) |
| **G3** | **"Top 10 branches" designation** | Benchmark cohort for trends | Branch productivity ranking (derived + policy) |
| **G4** | **Weekly history (≥13 weeks)** | Drawer trend + Tab 2 are seeded/faked; real trend needs stored weekly snapshots per worker | Historical HCHB productivity extracts, warehoused |
| **G5** | **`weeklyExpectedPoints` derivation** | Where 30 (FT) / 24 (PT) / 0 (contract) come from | Productivity-target policy by FTE × discipline |
| **G6** | **NVA / tier actuals** | Tab 3 is reference-only; a live tool needs actual NVA entries + tier attainment per worker per period | HCHB payroll reports |
| **G7** | **Pay-period / "Week Of" calendar** | Defines the snapshot boundaries and Monday payroll close | Payroll calendar (config) |
| **G8** | **The handoff spec (§3.3, §8.1)** | The authoritative schema + threshold source the mockup cites | External doc — obtain and file in `knowledge/` |

### Reconciliation vs. the broad data index

The earlier [`capacity-tool-data-index.md`](./capacity-tool-data-index.md) indexed the *full
capacity-forecasting/matching vision* (supply + demand + referrals + geography + auth + forecast). **The mockup
is deliberately narrower — a workforce-productivity measurement tool.** Mapping:

- **In the mockup:** the clinician-master subset (A1–A9), the point system (domain F → now Entity 1/VCP), and a
  slice of the derived outputs (J1/J7 utilization, J2/J8 open capacity as "headroom").
- **Not in the mockup (yet):** patient census (C), referral pipeline (D), visit-level scheduling ops (E),
  geography/drive-time (G), auth/payer (H), and the demand-side forecast (J4/J5). These are the broader
  capacity vision the tool could grow into — but they are **out of scope for this artifact.**

**Net:** the mockup is v1 = *"can we see, per clinician, productivity vs. target and the unused capacity it
implies?"* — the measurement foundation the rest of the capacity program can be built on. Which is exactly the
discovery's sequencing: **define and instrument the point system first.**

### Next step — source war-listing (for the team session)

Take Entities 1–6 and the Gaps and fill:

| Element (#) | Confirmed source | HCHB/Workday report or screen | Owner who pulls it | Refresh | Exists today? (Y/N/partial) | Notes |
|---|---|---|---|---|---|---|

Start with **G1 (point rules) and G5 (targets)** — nothing the tool shows is trustworthy until those are
defined, and both are policy decisions before they are data feeds. Then **W7 pointsByDay → the actual HCHB
report** the business rules already name ("HCHB payroll reports"), which is the single richest source.

---

## As-built review (`invisiblegears` `main` @ `6dba163`, re-read from source)

The tool has grown from a 4-tab productivity tracker into a **capacity-guidance cockpit**. What's now built:

### The nine tabs
1. **Worker Productivity** — the roster grid (now with a segmented completed/in-progress/scheduled/missed bar and a per-day expected marker).
2. **Roster** — editable clinician master: preferred days, territory zips (add/remove), PTO, restrictions — scheduler-maintained.
3. **Per Diem** — the per-diem pool: available vs. scheduled visits, remaining capacity, and a **disengagement flag** (≥7 days since last confirmed visit).
4. **Worker Trends** — per-clinician archetype cards: 13-wk spark, front-load score vs. the 42% gold standard, missed-visit %, risk tier, and a narrative assessment.
5. **Productivity Trends** — division vs. Top-10 by region/area (as before).
6. **Capacity Guidance — Live Cockpit** — the new brain (see below).
7. **Capacity Map** — Charleston tri-county zip tiles colored by RN/PT remaining capacity; marks zips at capacity.
8. **Visit Capacity Program** — the NVA/tier/comp reference (as before).
9. **Implications** — the stakeholder scorecards.

### The capacity brain (Tab 6 + `capacityDirectives()`)
Real supply→demand matching on live-shaped data:
- **Supply math:** `remainingByDay = maxDaily − assigned points` (FT 8 / PT 6 / PD 4), netted for PTO; `weekOpen` = sum of positive remainders Wed→Sat; assessing capacity computed per discipline.
- **Demand:** `REFERRALS` (discipline, zip, SOC/Eval, assigned/unassigned) and `DISCHARGES` (discipline, zip, D/C date) — capacity *arriving* and *reopening*.
- **Geography:** real zip lat/lon + **haversine**; `nearestScheduled` finds a clinician already working near a referral.
- **Assessing→assistant offload:** RN→LPN, PT→PTA, OT→COTA — frees assessing capacity for SOCs.
- **Seven directive types**, ranked: referral→best-fit clinician (capacity + proximity, per-diem favored); offload routine to assistant; discharge→backfill nearest referral; re-engage disengaging per-diem; reassign behind-pace backlog before it goes missed; extend a per-diem RN into a maxed SOC zip; park overflow with a front-loader who has headroom.

This is the "AI optimization engine" track the discovery called for — a real prototype, not a chart.

### Findings from reading the logic (what to fix as it goes real)

1. **Restrictions are displayed but not enforced in matching.** Per-diem restrictions ("No SOC visits", "No wound care", "No high-acuity", "Recerts only", "Weekends only") are free-text labels. `capacityDirectives()` ranks per-diems by capacity + proximity and *favors* them (`dist − 3`) but never checks the restriction — so it can recommend an **SOC to "No SOC visits" Arjun Patel**, or wound care to "No wound care" Lily Nguyen. **The matcher needs to hard-filter on restrictions/competencies.** (Highest-priority correctness gap.)
2. **Capacity = visit-point headroom only — travel and NVA aren't debited.** `remainingByDay` counts assigned visit points against a daily ceiling but never subtracts drive time, documentation, or admin. A clinician shown "+2.0 open" may be full once the day's route is counted. Miles exist per visit but don't reduce capacity. → "open capacity" runs optimistic.
3. **Proximity is straight-line haversine, not drive-time.** The data index has `routeMiles` from routing; the matcher uses centroid haversine. Fine for a demo; rural loops (e.g., 29471 "rural loop") will mislead until drive-time replaces it.
4. **SOC eligibility ≈ discipline.** `renderCapSoc` and the matcher treat any RN/PT as SOC-capable; a per-diem RN flagged "No SOC visits" still counts toward RN SOC coverage. SOC-eligibility should be its own flag (the discovery distinguishes it).
5. **No readiness/auth gate before matching.** Referrals are binary `unassigned | assigned` — the matcher acts as if every referral is schedulable. In reality it may be stuck in DCS/auth/POC/F2F. This is ecosystem gap **1A**, and the directive engine makes it *more* important: it will confidently route a referral that can't actually start.
6. **Everything is demo-seeded** (`SAMPLE`, `REFERRALS`, `DISCHARGES`, `PD_META`, simulated `visitStatus`). Expected — but the brain's value hinges on the live referral-readiness and per-diem-availability feeds, which are the manual/HCHB rows in the data index.

### Where this leaves the ecosystem gaps
The build-out **closes the demand-arrival + matching layer** (referrals, discharges, proximity, per-diem engagement) that the ecosystem map listed as thin. The **structural gaps still stand**: 1A readiness gauntlet (now *more* pressing), 1B economics/LUPA, 1C quality/compliance, 2D forward forecast, 2E patient acuity (only a per-diem free-text restriction today), 2F aide (HHA)/MSW, 2G back-office capacity, 2H retention signal, 3I the clinician accept/decline loop, 3K data-trust. See [`capacity-ecosystem-map.md`](./capacity-ecosystem-map.md).

## Capacity Tool — Data Index (Phase A)

> **Purpose.** Enumerate *every bit of data* a home health capacity tool would need to exist, so the team can
> go find the content and war-list its source. This is the demand/supply data dictionary behind the
> "Capacity Management Scoping" next step in the discovery ([`../knowledge/discovery-session.md`](../knowledge/discovery-session.md), Next Step #4).
>
> **Status.** Grounded in the Compassus discovery docs + standard HCHB / Workday data models + the tool's
> stated purpose. The `invisiblegears.com` mockup could not be loaded from the build environment (network
> policy blocked the host), so field names below are the *functional* data elements the tool implies —
> **to be reconciled against the actual mockup screen-by-screen.** Anything the mockup shows that isn't here
> gets added; anything here the mockup doesn't need gets flagged.
>
> **Source column is a hypothesis, not a finding.** The operator + team will confirm/replace during source
> war-listing. `Cadence` = how fresh the data must be. `Grain` = the level each row represents.

### How to read this

The tool is fundamentally a **matching engine**: it holds **supply** (clinician capacity), **demand**
(patients + referrals), the **currency** that both are denominated in (the point system), the **constraints**
(geography, licensure, compliance, preferences), and the **derived outputs** (open slots, gaps, forecast).
The data index is organized along exactly those lines. Domains A–D are the master/dynamic feeds; E–H are the
constraint/reference layers; I is the net-new static data to be gathered; J is what the tool *computes* rather
than ingests.

Candidate sources abbreviated: **HCHB** (Homecare Homebase), **WD** (Workday), **CM** (Commure – intake/referral),
**NM** (NestMed – documentation), **PU** (Pulse – utilization), **CIR** (Circadia – patient calling),
**CODE** (external ICD-10 coding vendor), **STATIC** (new config/preference store to be built), **DERIVED**
(computed by the tool).

---

### A. Clinician / Workforce Master (the supply side — mostly static)

Grain: one row per clinician. This is the roster the whole capacity calculation stands on.

| # | Data element | Grain / detail | Candidate source | Cadence |
|---|---|---|---|---|
| A1 | Clinician ID | Canonical employee identifier (join key across HCHB↔WD) | WD / HCHB | Static |
| A2 | Name / display name | — | WD | Static |
| A3 | Discipline | RN, LPN/LVN, PT, PTA, OT, COTA, SLP, MSW, HHA/aide | HCHB / WD | Static |
| A4 | Licenses & certifications | License type, number, **state**, expiration date | WD | Slow-changing |
| A5 | Specialty competencies | Wound care, IV/infusion, lymphedema, cath, ventilator, wound-vac, etc. | STATIC / HCHB | Slow-changing |
| A6 | **SOC-eligibility flag** | Whether this clinician can perform a Start of Care (the binding-constraint dimension, CP-3) | STATIC / HCHB | Slow-changing |
| A7 | Employment type | Full-time / part-time / PRN / contract / agency | WD | Slow-changing |
| A8 | FTE value | 1.0, 0.5, etc. | WD | Slow-changing |
| A9 | **Pay model** | Per-visit / salaried / hybrid (drives scheduling incentives & the earnings story) | WD | Slow-changing |
| A10 | Productivity target | Points/week (and/or visits/week) expected — benchmark heard: **30 pts/week min** | STATIC / HCHB | Slow-changing |
| A11 | Max caseload / capacity ceiling | Hard limit on concurrent patients or daily visits | STATIC | Slow-changing |
| A12 | Home base / branch | Branch of assignment | HCHB / WD | Slow-changing |
| A13 | Assigned territory / zones | Zip codes or zones the clinician covers | HCHB / STATIC | Slow-changing |
| A14 | Standard availability | Working days & hours; standard days off | WD / STATIC | Slow-changing |
| A15 | Hire date / tenure | Drives change-management segmentation (tenured = hardest to change) | WD | Static |
| A16 | Ramp / orientation status | New hire not yet at full productivity | WD / HCHB | Dynamic |
| A17 | Languages spoken | For patient matching | STATIC / WD | Static |
| A18 | Home/base location | Start point for drive-time calc (address or geocode) | WD / STATIC | Slow-changing |
| A19 | Employment status | Active / LOA / terminated (with effective dates) | WD | Dynamic |

### B. Clinician Availability & Load (the supply side — dynamic)

Grain: one row per clinician per day/week. This converts the roster into *actual reachable capacity*.

| # | Data element | Grain / detail | Candidate source | Cadence |
|---|---|---|---|---|
| B1 | Approved PTO | Dates off (the Workday↔HCHB integration is **currently OFF** — flagged in discovery) | WD | Daily |
| B2 | Requested / pending PTO | Not yet approved | WD | Daily |
| B3 | Other unavailability | Training, meetings, jury duty, FMLA blocks | WD / HCHB | Daily |
| B4 | On-call / after-hours assignment | Who is on-call and the recovery burden it creates | HCHB / STATIC | Weekly |
| B5 | Current caseload count | Active patients presently assigned | HCHB | Real-time-ish |
| B6 | Points plotted this week | Scheduled points vs. target (utilization signal) | HCHB console | Daily |
| B7 | Points completed | Actual delivered vs. plotted | HCHB | Daily |
| B8 | Visits scheduled / completed | Count + type, per day | HCHB | Daily |
| B9 | Utilization % | Completed ÷ available capacity | DERIVED (from B6/B7) | Daily |
| B10 | Overtime hours | OT incurred / trending | WD / HCHB | Weekly |
| B11 | Sick / call-out events | Unplanned unavailability | WD / HCHB | Real-time |
| B12 | Current-day accepted visits | Once accepted, back office **cannot pull** — hard scheduling constraint | HCHB | Real-time |

### C. Patient / Census (the demand side — current book of business)

Grain: one row per active patient (often per patient × discipline). What the branch is already carrying.

| # | Data element | Grain / detail | Candidate source | Cadence |
|---|---|---|---|---|
| C1 | Patient ID | Join key (operational only — minimize PHI; see guardrail note) | HCHB | Real-time |
| C2 | Branch / territory / zip | Where the patient is served | HCHB | Static per episode |
| C3 | Geocode / service location | For drive-time & zone assignment | HCHB / DERIVED | Static per episode |
| C4 | Disciplines on the plan of care | RN/PT/OT/etc. ordered for this patient | HCHB | Per episode |
| C5 | Ordered visit frequency | Per discipline (e.g., 2w9 = 2×/wk for a week then 9 total) | HCHB | Per episode |
| C6 | Episode / period day | Position within the 30-day PDGM period / 60-day cert | HCHB | Daily |
| C7 | Cert period start / end | Drives recert timing | HCHB | Per episode |
| C8 | **Recert due date** | Upcoming demand spike | HCHB | Per episode |
| C9 | Scheduled discharge date | Capacity that will free up | HCHB | Dynamic |
| C10 | Payer | Medicare / MA / commercial / Medicaid / private | HCHB | Per episode |
| C11 | Acuity / complexity | Visit weight beyond raw count (undefined today) | PU / HCHB | Per episode |
| C12 | Plan-of-care status | Draft / pending DCS / locked / on hold | HCHB | Real-time |
| C13 | Assigned primary clinician(s) | For continuity (CP-10) | HCHB | Dynamic |
| C14 | Upcoming scheduled visits | Forward visit slate, per discipline | HCHB | Daily |
| C15 | Compliance visits due | 30-day reassessment, 14-day HHA supervisory, discharge/recert visits | HCHB | Daily |
| C16 | Patient preferences | Preferred visit time window, preferred caregiver, access constraints | STATIC / CIR | Per episode |

### D. Referral / Intake Pipeline (the demand side — incoming, the growth lever)

Grain: one row per referral. This is the inflow that SOC capacity either absorbs or turns away (CP-3, CP-8).

| # | Data element | Grain / detail | Candidate source | Cadence |
|---|---|---|---|---|
| D1 | Referral ID | — | CM / HCHB | Real-time |
| D2 | Referral source | Hospital / SNF / physician / ACO / other (and the specific partner) | CM | Real-time |
| D3 | Referral received date/time | Starts the **TIC clock** (from referral date) | CM / HCHB | Real-time |
| D4 | Patient location / zip | To test against territory capacity | CM | Real-time |
| D5 | Disciplines ordered | What skills the referral will demand | CM | Real-time |
| D6 | Payer + auth requirement | Medicare (auto-auth) vs. non-Medicare (auth needed) | CM / HCHB | Real-time |
| D7 | Expected SOC date | When the demand actually lands | CM / HCHB | Real-time |
| D8 | Facility expected discharge date | When patient becomes available | CM | Real-time |
| D9 | Referral status | Pending / accepted / declined / pending-auth | CM / HCHB | Real-time |
| D10 | Acceptance decision + reason | Especially **decline reasons** (capacity vs. clinical vs. geography) | CM / HCHB | Real-time |
| D11 | Face-to-face / order documentation status | Missing F2F → coding discrepancy → POC hold (blocks scheduling) | NM / CODE | Dynamic |

### E. Visit / Scheduling Operations (the execution record)

Grain: one row per visit / task. Feeds the point/utilization math and surfaces the friction the tool must ease.

| # | Data element | Grain / detail | Candidate source | Cadence |
|---|---|---|---|---|
| E1 | Visit ID | — | HCHB | Real-time |
| E2 | Visit type | SOC, routine, recert, ROC, reassessment, discharge, HHA supervisory | HCHB | Real-time |
| E3 | Assigned clinician | — | HCHB | Real-time |
| E4 | Scheduled date + time window | — | HCHB | Real-time |
| E5 | Visit status | Plotted / accepted / completed / missed / declined / reassigned / rescheduled | HCHB | Real-time |
| E6 | Missed-visit reason + MD-notified timestamp | 48-hour MD notification (Medicare) | HCHB | Real-time |
| E7 | Coordination notes | Clinician→scheduler change requests | HCHB | Real-time |
| E8 | **Auth-off notifications** | The 50–60/day, mostly non-actionable queue | HCHB | Real-time |
| E9 | Point value assigned to the visit | Depends on the (undefined) point system | HCHB | Real-time |
| E10 | Actual visit duration / travel | If captured — needed to weight true load | HCHB / NM | Daily |

### F. Point System (the shared currency — OPEN QUESTION #1)

The single most important thing to define; both capacity and scheduling are denominated in it (CP-5). Today it
is referenced everywhere and defined nowhere. **This block is a definition to be authored, not a feed to pull.**

| # | Data element | Grain / detail | Candidate source | Cadence |
|---|---|---|---|---|
| F1 | Point value by visit type × discipline | The core lookup table (e.g., SOC RN = X pts) | STATIC (to define) | Config |
| F2 | Daily / weekly point targets by clinician type | The productivity standard | STATIC (to define) | Config |
| F3 | Travel treatment | Whether/how drive time earns or offsets points | STATIC (to define) | Config |
| F4 | Non-visit-activity (NVA) treatment | Documentation, admin, supervisory time | STATIC (to define) | Config |
| F5 | Acuity/duration weighting | How a "hard" visit counts vs. a routine one | STATIC (to define) | Config |
| F6 | Market / discipline variation | Whether targets differ by region/discipline | STATIC (to define) | Config |

### G. Geography & Territory (constraint layer — partly to be built)

| # | Data element | Grain / detail | Candidate source | Cadence |
|---|---|---|---|---|
| G1 | Territory / zone definitions | The list of zones and their boundaries | STATIC | Slow-changing |
| G2 | Zip → zone mapping | Assigns patients/referrals to a zone | STATIC | Slow-changing |
| G3 | Branch service-area boundaries | What each branch will/won't accept | STATIC / HCHB | Slow-changing |
| G4 | Drive-time / distance matrix | Zone-to-zone or point-to-point travel cost | DERIVED (mapping API) | Computed |
| G5 | Clinician↔zone coverage | Which clinicians serve which zones (links A13) | STATIC / HCHB | Slow-changing |

### H. Authorization & Payer Rules (constraint layer)

| # | Data element | Grain / detail | Candidate source | Cadence |
|---|---|---|---|---|
| H1 | Payer master | List of payers + Medicare/non-Medicare flag | HCHB | Slow-changing |
| H2 | Auth requirement by payer | Whether/what auth is needed before scheduling | HCHB / payer | Slow-changing |
| H3 | Authorized visit counts | Visits granted per auth | HCHB | Dynamic |
| H4 | Auth expiration / window | When re-auth is required | HCHB | Dynamic |
| H5 | Compliance-window rules | 48h missed-visit MD notice, 30-day reassess, 14-day HHA supervisory, TIC, buddy codes by state, CoP physical-calendar | STATIC (rules) | Config |

### I. Static / Configuration / Preferences (NET-NEW — the "employee preferences, etc." to gather)

This is the layer the operator explicitly called out as "static information we'll need to figure out." Most of
it does not exist in any system today and must be gathered.

| # | Data element | Grain / detail | Candidate source | Cadence |
|---|---|---|---|---|
| I1 | Clinician zone preferences | Preferred / acceptable / refused zones | STATIC | Gathered |
| I2 | Willingness to cross territory | The exact lever that broke Alabama Smart Scheduling | STATIC | Gathered |
| I3 | Willingness to take SOC / extra visits | Especially on pay-per-visit (the earnings story) | STATIC | Gathered |
| I4 | Max visits/day & preferred load | Sustainable daily ceiling per clinician | STATIC | Gathered |
| I5 | Preferred days off / schedule shape | Beyond formal PTO | STATIC | Gathered |
| I6 | Continuity assignments | Standing patient↔clinician pairings to preserve | STATIC | Gathered |
| I7 | Branch capacity parameters | Target ~40–50 patients per RN+LPN team pair; reserve-capacity policy; caseload limits by discipline | STATIC | Config |
| I8 | Business rules | SN-first-if-ordered on SOC; urgency tiers; fallback acceptability (proximity/discipline/continuity); decline rights | STATIC | Config |
| I9 | Slot definition | What counts as an "open slot" (visit? block? point? admission?) — open question | STATIC (to define) | Config |
| I10 | Patient preferences store | Preferred windows, caregiver continuity, communication channel | STATIC / CIR | Gathered |

### J. Derived / Computed Outputs (what the tool produces, not ingests)

These are the answers the tool exists to give — built from A–I. Listed so the team knows which numbers are
*calculated* (and therefore depend on defining the point system and slot first).

| # | Output | Built from | Notes |
|---|---|---|---|
| J1 | Available productive visit-hours / points by discipline × zone | A + B + F + G | The real capacity number (not headcount) |
| J2 | Open SOC slots & open routine slots | J1 + I9 + A6 | The growth-gating count (CP-3) |
| J3 | Capacity-to-census coverage ratio | J1 + C | Over/under-staffed by zone & discipline |
| J4 | Demand forecast 30/60/90-day | C + D + recert/discharge timing | Demand as a *shape over time*, front-loaded |
| J5 | Capacity-vs-demand gap map | J1 + J4 | Heat map with dollar sizing |
| J6 | LUPA / visit-count risk watch | C + E | Periods trending below thresholds |
| J7 | Utilization & workload balance | B + F | Variance across clinicians (burnout signal) |
| J8 | Referral-acceptance capacity signal | J2 + D | Can we say yes to this referral? |
| J9 | Projected admissions capacity | J2 + D7/D8 | Forward SOC absorption |

---

### Known gaps, dependencies & sequencing

1. **Define the point system (F) and the slot (I9) first.** Almost every computed output (J) is denominated in
   them. This is open question #1 — nothing downstream is trustworthy until it's pinned.
2. **The Workday↔HCHB PTO integration is OFF (B1).** Availability data is manually entered today; the tool needs
   this feed activated or it inherits stale availability.
3. **Employee-preference data (I) largely does not exist.** It's the operator's stated "static information to
   figure out" — plan a gathering mechanism (survey / onboarding capture / manager entry).
4. **Territory & drive-time (G) is partly unbuilt.** Zone definitions and a drive-time matrix must be created;
   they don't fall out of HCHB.
5. **Acuity weighting (C11) is undefined.** Raw visit counts overstate/understate real load without it.
6. **PHI minimization.** The capacity tool runs on aggregates and operational signals. Patient-level joins (C1)
   should carry the minimum-necessary identifier; no diagnoses, addresses, or names beyond what capacity math
   requires. Confirm the BAA-covered surface before any patient-level data lands (see the intake-brief posture).

### Next step — source war-listing template

For the working session, take each row above and fill:

| Data element (#) | Confirmed source system | Report / table / screen | Owner who can pull it | Refresh mechanism | Exists today? (Y/N/partial) | Notes |
|---|---|---|---|---|---|---|

Rows that come back **N / partial** are the build backlog. Rows in domains **F, G, I** are expected to be mostly
net-new — that's where the real work is.

---

*Reconciled against the actual mockup source (read from `worker-max/invisiblegears`, branch `capacity-tool`).
The mockup is narrower than this broad vision — a workforce-productivity measurement tool. The precise,
source-read data model for what the mockup actually uses is in
[`capacity-tool-mockup-data-spec.md`](./capacity-tool-mockup-data-spec.md); this document remains the
full-capacity-vision data index the tool can grow into.*



# Part VI — Ecosystem & Roadmap

## Home Health Capacity Ecosystem — Coverage Scan

> **Question answered:** now that the Clinician Capacity Management Tool is well-defined (see the data index),
> what pieces of the home health capacity ecosystem are we *not* yet considering?
>
> **Method:** diffed the tool's data index (`ClinicianCapacityTool_DataIndex.xlsx`) against the full capacity
> ecosystem implied by the Compassus discovery ([`../knowledge/`](../knowledge/)). This lists only genuine
> white space — things the current index does **not** contain — not a re-statement of what it already does well.

> **Re-reviewed against the built-out tool** (`invisiblegears` `main` @ `6dba163`, 9 tabs + capacity cockpit).
> The build now closes the demand-arrival + matching layer (referrals, discharges, proximity, per-diem
> engagement, assessing→assistant offload, a 7-type directive engine). The structural gaps below still stand,
> and 1A is now *more* pressing because the directive engine acts on referrals as if they're schedulable. One
> new **correctness** finding: the matcher ranks/​favors per-diems by capacity + proximity but **does not enforce
> their restrictions** ("No SOC", "No wound care", "No high-acuity"), so it can mis-route. Full read in the
> [as-built review](./capacity-tool-mockup-data-spec.md#as-built-review-invisiblegears-main--6dba163-re-read-from-source).

### What the tool already covers (so we don't re-litigate it)

Supply (clinician capacity net of PTO / per-diem / max-daily-points), the **point system** (visit-weight table —
the previously-open #1 gap, now closed), demand *arrivals* (referrals + pending discharges), geography &
routing (territory, route miles, tracts, capacity map), matching/AI directives (proximity, nearest scheduled
visit), outreach (Twilio channels + welcome call), trends/history (13-wk, front-load, pace, missed-visit), and
the VCP comp layer. This is a strong **supply-measurement + matching** engine.

### The capacity equation — where the gaps sit

```
DEMAND ──▶ [READINESS gauntlet] ──▶ SUPPLY ──▶ [CONSTRAINTS] ──▶ DECISION ──▶ FEEDBACK
referrals   intake/DCS/auth/POC     clinician   geo·acuity·auth   accept /     financial·
+forecast   /F2F/coding/TIC         capacity    ·licensure·qual   assign/staff quality·retention
   │            ▲ GAP (Tier 1A)        ✓ strong      ~partial          ✓ AI directives   ▲ GAP (Tier 1B/C)
   ▲ GAP (Tier 2D forecast)
```

The tool is strong in the middle (supply → match). The white space is at the **two ends**: the *readiness
gauntlet upstream of a schedulable visit*, and the *economic/quality/retention feedback* that tells you whether
a capacity decision was actually good.

---

### Tier 1 — Structural (these change the answer, not just add detail)

#### 1A. The pre-scheduling readiness gauntlet — the discovery's central finding, still absent
The index treats a referral as ready-to-assign (`status: unassigned | assigned`). But the discovery's #1
conclusion was that *the inefficiency is upstream of scheduling*: a visit is typically stuck in **DCS review,
pending authorization, a plan-of-care lock, or a face-to-face / coding hold** before a scheduler can act. None
of those states are in the index, and neither is **TIC (time-to-initial-care)** — the referral→SOC clock the
whole intake funnel is measured on.
**Why it matters:** "Can we accept this referral?" is gated by these states as much as by clinician open points.
A capacity tool that can't see the gauntlet will show green capacity while admissions stall upstream — exactly
the blame-lands-on-scheduling trap.
**Attach as:** a Referral *readiness state* (DCS status, auth status, POC lock, F2F/coding hold) + a TIC clock.

#### 1B. The economic layer — LUPA, margin, and agency/OT cost
The tool expresses capacity in *points and visits*, and comp in VCP units — but never in *dollars* or *episode
economics*. Missing: **LUPA risk** (periods trending below the visit threshold — a step-function the schedule
directly controls), **margin per 30-day period**, and **PRN / agency / overtime spend** as the cost of covering
a gap.
**Why it matters:** every executive capacity decision (accept? hire? use agency? push overtime?) is ultimately
economic. "Open capacity" of 40 points isn't a dollar figure, and a full schedule that's LUPA-ing is a financial
hole the productivity view can't see.
**Attach as:** a per-episode LUPA watch + a cost overlay on the open-capacity / coverage-outreach flows.

#### 1C. Quality & compliance guardrails
`missedVisitPct` and `mvNotesCount` are in; the rest of the quality/compliance frame is not: **HHVBP** measures
(the cohort-relative scoring the org is paid on), **OASIS timeliness**, **recert / 30-day reassessment / 14-day
HHA-supervisory windows**, and **acute-care hospitalization**.
**Why it matters:** capacity utilization pushed without these degrades the exact outcomes reimbursement now
depends on. Compliance windows are also hard scheduling constraints, not soft goals.
**Attach as:** compliance-window flags on the visit/plan-of-care record + a quality guardrail on utilization
targets.

### Tier 2 — Important extensions

#### 2D. Predictive demand forecast (the tool is present-tense)
History is captured (13-wk); *forward* demand is not. No referral-source trend, seasonality, or 30/60/90-day
admissions projection. Discharges give near-term reopen, but not a forecast.
**Why it matters:** capacity planning is a forward function; measuring last week can't tell you what to staff
for next month. This was the discovery's explicit aspiration.

#### 2E. Patient acuity / complexity (demand-side weighting)
`productivityWeight` is by *visit type*, not *patient acuity*. A high-acuity wound/CHF caseload at "90%
productivity" is loaded very differently from a routine one. `restrictions` capture "no wound care" but there's
no acuity model on demand.
**Why it matters:** acuity-blind matching over-loads clinicians the point system says are fine, and misroutes
complex patients.

#### 2F. Aide (HHA) and MSW capacity + supervisory linkage
The discipline enum (RN/LPN/PT/PTA/OT/COTA/SLP) omits **HHA/aides** and **MSW**. Aides are a large capacity pool
with their own scheduling and a **14-day supervisory-visit** dependency on the RN.
**Why it matters:** aide capacity and its supervisory tie-back is real capacity and real compliance load the
tool currently can't see.

#### 2G. Back-office capacity — scheduler & DCS throughput
The tool manages *clinician* capacity, but the discovery named the **scheduler and DCS as the actual
bottleneck** (scheduler burnout; the DCS 4-task review chain; the 50–60/day auth-notification noise). Nothing
models back-office throughput.
**Why it matters:** you can have clinician capacity and still not convert it because the constraint is a
drowning scheduler or a DCS queue.

#### 2H. Future capacity — hiring/onboarding ramp + retention risk
`tenure` is derived, but there's no **new-hire ramp curve** (reduced early productivity), no **hiring pipeline**
(reqs/offers/start dates = capacity arriving), and no **turnover-risk / burnout signal**.
**Why it matters:** discovery's feedback loop — over-utilization destroys capacity via turnover on a 3–6-month
lag. A tool that only maximizes this week's points can quietly burn down next quarter's capacity.

### Tier 3 — Surfaces & backbone

#### 3I. Directive governance + the clinician accept/decline loop (the Alabama lesson)
Outreach exists (channels, message body), but the **clinician's response** — accepted / declined a coverage
offer, and *why* — isn't captured, and there's no approval/override/audit trail on AI directives.
**Why it matters:** the Alabama Smart Scheduling pilot failed on change management, not tech. Capturing accept/
decline + reason is both the buy-in mechanism and the training signal; ungoverned directives repeat that failure.

#### 3J. Patient-facing and referral-source-facing surfaces
Leader/scheduler/clinician surfaces exist; the **patient scheduling portal** (visit-window visibility, reschedule
requests — the discovery's QR-code idea) and the **referral-source acceptance loop** (does Roper St. Francis
learn we can/can't take the patient?) are absent.
**Why it matters:** patients judge the agency on scheduling reliability; referral sources route to whoever says
yes fastest. Both are capacity *outputs* with no surface today.

#### 3K. Integration & data-trust backbone
The index names the critical field (`visitStatus`, gated by **PointCare manual sync**) and the source systems.
Two backbone realities aren't modeled: **sync latency** (PointCare is not real-time — capacity shown may be
stale) and the **Workday↔HCHB PTO integration the discovery reported is OFF** (so PTO, a load-bearing
availability input, may be manual/stale). Plus master-data identity resolution (WD-ID ↔ HCHB-ID) at scale.
**Why it matters:** every number the tool shows inherits the freshness and identity-match of these feeds; a
capacity call made on stale sync is confidently wrong.

---

### The sibling tools are part of this ecosystem

Two related artifacts already live in `invisiblegears`: **hh-territories** ("The Tract, Not the ZIP" — territory
design) and **hh-scheduling** ("Four outcomes, one schedule"). These are not separate projects; they are the
*territory* and *scheduling-execution* faces of the same capacity ecosystem. Worth an explicit product
architecture so the capacity tool, the territory designer, and the scheduling view share one data spine rather
than three.

### Recommended next moves

1. **Decide scope deliberately.** Not everything above belongs in *this* tool — but each should be a conscious
   "in / adjacent / later," not an accidental omission. The safe default: keep the tool as the supply+match
   engine, and treat 1A (readiness), 1B (economics), and 1C (quality) as the next adjacent modules it must
   *connect to*.
2. **Prioritize 1A.** The readiness gauntlet is the discovery's core thesis and the biggest blind spot — it's
   what turns "green capacity" into real, admittable capacity.
3. **Add the two feedback overlays (1B financial, 1C quality)** before scaling — they're what tell you a capacity
   decision was actually good, and they're what executives and VBP are scored on.
4. **Capture the accept/decline loop (3I) now** — it's cheap, it's the buy-in mechanism, and it's the training
   data every later optimization needs.



# Part VII — Appendices

## SME Perspective — Branch Executive Director

> Seeded v0 perspective (AI-generated from the Branch ED lens, grounded in the operator's strategy download).
> **To be validated with a real Branch ED.** Preserved verbatim as a discovery input per the
> [SME discovery framework](../sme-discovery-framework.md).

## Home Health Capacity Tactics — Branch ED Lens

Below are the tactics that actually moved capacity in a branch I grew from a bottom-quartile performer to top-of-region. These are field-tested, not framework theory. I've written each so a developer can build the rule and a trainer can teach the agent. I'll flag where a tactic depends on the staffing model being right first — because nothing downstream works if the model is wrong.

---

### 1. Discipline-Balance Guardrail (RN:LPN and PT:PTA ratios)

**Tactic.** The great branch staffs LPNs and PTAs deliberately so RNs and PTs are spent on the visits only they can do — SOCs, ROCs, resumptions, recerts, complex assessments — and routine follow-up visits flow to the assistant level. When the assistant tier is understaffed, RNs and PTs silently absorb routine visits and the branch loses SOC capacity it never sees on a report.

**Trigger / context.** Continuous, but especially when a branch is "busy but not growing" — clinicians are maxed, yet SOC acceptance is flat or declining.

**Why it works.** Capacity for *new* patients is created almost entirely at the skilled-clinician SOC slot. Every routine LPN-appropriate visit a RN does is a SOC that RN can't do that day. The imbalance is invisible on a raw productivity report (the RN looks "full") — it only shows up when you decompose the RN's day by visit type.

**Encode as system logic.**
- Track per-discipline visit mix: for each RN, `% of weekly visits that are routine/follow-up (LPN-eligible)`. Flag when RN routine-visit share exceeds a market-set threshold (I ran ~20-25%).
- Compute live ratios `RN:LPN` and `PT:PTA` against a **market-target band** (not a national default). Flag out-of-band.
- Derived metric: **"Skilled-hours leakage"** = RN/PT hours spent on assistant-eligible visits × loaded rate. Surface as a dollar figure and as "SOCs foregone this week."

**Train the AI agent.** Watch for RNs whose calendars are full of routine visits while SOC referrals are being declined/deferred. Recommend shifting routine visits to LPN/PTA to free skilled slots, or flag an assistant-tier hire. Do NOT recommend "hire more RNs" as the first lever when the real problem is an LPN/PTA gap — that's the expensive wrong answer and it's the most common mistake. Always express the fix as "SOCs unlocked," not just "hours rebalanced."

---

### 2. Market-Unique Model Sizing (no copy-paste ratios)

**Tactic.** Each branch's staffing model is sized to *its* market's referral potential, payer mix, geography, and acuity — never cloned from another branch. A dense metro branch with high LPN-eligible chronic census runs a very different ratio than a rural branch with long drive times and RN-heavy acuity.

**Trigger / context.** New branch build, annual model reset, a market shift (new referral source, MA plan change, competitor exit), or any time actuals drift from the plan two quarters running.

**Why it works.** The staffing model is the PRIMARY effector of capacity. A model tuned to potential means new referrals get absorbed almost automatically; a mistuned model either strands capacity (overstaffed, margin bleeds) or chokes growth (understaffed, SOCs bounce). Potential is a function of the market, so the model must be too.

**Encode as system logic.**
- Model each discipline's target FTE as a function of inputs: projected weekly referrals × payer/acuity mix × avg visits-per-episode by discipline × geography factor (drive time / density) ÷ target productivity.
- Store a **per-market target band** for every ratio and productivity number; national numbers are seed defaults only, explicitly labeled "unvalidated for this market."
- Run a monthly **plan-vs-actual variance** on referral volume, mix, and per-discipline utilization; auto-flag when the model's assumptions no longer hold.

**Train the AI agent.** Reason from *this market's* numbers, never a global constant. When asked "are we staffed right?", pull the market's referral trend and mix first, then compare to the model. Recommend model re-sizing when variance persists. Do NOT normalize one branch against another's ratios as if they're comparable — surface the market differences that justify the gap.

---

### 3. SOC-Dedicated Nurse (and SOC PT) — Manufacturing Known Slots

**Tactic.** Create one or more nurses who do *only* SOCs, ROCs, and resumptions — no ongoing caseload. Their week is a grid of bookable start-of-care slots. In markets with PT-driven ortho volume, do the same with a SOC-dedicated PT.

**Trigger / context.** Once referral flow is steady and predictable enough to keep a dedicated role busy — typically a mid-to-large branch, or a smaller one with a reliable high-SOC referral source (joint-replacement program, MA chronic-care contract).

**Why it works.** It converts capacity from a *guess* into *inventory*. Normally a scheduler has to interrupt a RN's day and hope; with a SOC nurse, capacity is a set of known slots you can book against and even promise to a referral source ("we can start tomorrow AM"). It removes the daily productivity/SOC tug-of-war, protects episode start-timeliness, and makes acceptance decisions instant. Known slots also let the branch say "yes" faster than competitors — which grows referrals.

**Encode as system logic.**
- Model the SOC nurse/PT as a **slot inventory** object: N bookable SOC slots per day, with geography tags. The capacity cockpit's referral/discharge matching engine books referrals directly into slots.
- Surface **SOC slot fill rate** and **slots remaining today/this week** as a headline cockpit number.
- Apply the **SOC assignment rule** at booking: RN performs any SOC where nursing is on the case; PT performs the SOC only when nursing is NOT on the referral. The engine routes to the correct dedicated role automatically.
- Trigger a "create/expand SOC role" recommendation when SOC volume × interruption cost to skilled staff exceeds the cost of a dedicated FTE, or when SOC-timeliness starts slipping.

**Train the AI agent.** Treat SOC slots as the branch's true growth capacity — protect and fill them. When a referral arrives, check nursing-on-case to route RN-SOC vs PT-SOC correctly, then book the nearest open slot by geography. Watch for slot under-fill (role too big / referral dip) and over-subscription (role too small / need a second SOC nurse). Do NOT let a SOC nurse get quietly loaded with ongoing caseload "just this once" — that's how the known-slot capacity evaporates; flag any recurring visit assigned to a SOC role.

---

### 4. SOC-on-Referral Match Directive (turn capacity into an answer in minutes)

**Tactic.** Every inbound referral is matched to a concrete start plan — discipline, clinician/slot, day, geography fit — before the intake conversation ends, so acceptance is a real commitment, not "we'll call you back."

**Trigger / context.** Every referral, all day. Highest value during peaks and when competing against another agency for the same discharge.

**Why it works.** Referral sources reward speed and certainty. A branch that answers "yes, [PT] starts Thursday AM, she's already in that ZIP" wins the next referral too. It also forces the capacity question to be answered honestly at intake instead of discovered as a missed SOC three days later.

**Encode as system logic.**
- The directive engine takes referral attributes (disciplines ordered, nursing-on-case y/n, ZIP, acuity, requested SOC window) and returns a ranked match: SOC slot or clinician with resting-posture headroom in that territory.
- Enforce the RN-SOC / PT-SOC rule at match time.
- Log **time-to-match** and **accept vs decline with reason**; decline reasons feed the model-variance and hiring signals.

**Train the AI agent.** On each referral, produce the best 1-3 start plans with named slot/clinician + day + drive fit, and the nursing-on-case routing. Recommend accept when a compliant slot exists; if not, surface exactly what's missing (no LPN coverage in that ZIP, SOC nurse full Thu) so it becomes a staffing signal, not a silent decline. Do NOT accept a SOC the model can't actually staff on time — a late or bounced SOC costs more than a clean decline.

---

### 5. Resting-Posture Territory Design

**Tactic.** Assign clinicians to geographic territories with a deliberate "resting posture" — a home base and a caseload target set below their ceiling — so a clinician's default state already covers active clients *and* leaves absorption headroom for the next referral in their area. Coverage becomes nearly automatic.

**Trigger / context.** Caseload assignment, territory redraw after a hire/departure, or when drive time (non-productive miles) starts climbing.

**Why it works.** If everyone runs at 100%, every new referral is a scramble and a negotiation. If territories carry planned slack tied to referral density, the new SOC in that ZIP has an obvious home and the daily scheduling load drops. It ties caseload distribution to data and logic instead of "who complained least."

**Encode as system logic.**
- Give each clinician a **territory** (ZIP/geo cluster) and a **target caseload band** with intentional headroom keyed to that territory's referral rate.
- Roster/cockpit shows **headroom by territory** (green = absorb-ready, amber = tight, red = over). Matching engine prefers the in-territory clinician with headroom to minimize drive time.
- Flag **territory imbalance**: one clinician red while an adjacent one is green → rebalance suggestion. Track **non-productive drive miles** as a territory-health metric.

**Train the AI agent.** Route referrals to the in-territory clinician/slot with real headroom, protecting resting-posture slack rather than filling every clinician to the top. Recommend caseload rebalancing when adjacent territories diverge. Watch drive-mile creep as an early sign a territory is mis-drawn. Do NOT optimize purely for "fill the emptiest calendar" if it means cross-town assignments that burn windshield time and torch productivity.

---

### 6. Per-Diem / PRN Visibility & Pre-Positioning

**Tactic.** The branch keeps a live, ready per-diem bench and makes the *need* visible days ahead — so PRN coverage is arranged before a gap becomes a missed visit, not after. Per-diem coordination is genuinely hard; the tool's job is to make the gap show up early.

**Trigger / context.** Known upcoming crunch — PTO, census spike, a territory temporarily short, seasonal surge, a clinician out sick.

**Why it works.** Per-diem is the shock absorber for day-to-day variance. The failure mode is always *late visibility* — you find the hole the morning of. Surfacing projected uncovered visits 3-7 days out turns a scramble into a phone call.

**Encode as system logic.**
- Maintain a **per-diem roster** with disciplines, geographies, availability windows, credential/comp status.
- **Coverage-gap projection**: for the next 7-14 days, compute visits at risk of no assigned clinician given PTO/known absences and territory headroom; rank by SOC-criticality and recert deadlines.
- Match projected gaps to eligible per-diems by discipline + geo + availability; flag **credential/expiry** blocks before assignment.

**Train the AI agent.** Look ahead, not just at today — surface projected uncovered visits early and propose specific per-diem matches. Prioritize SOCs and recert-deadline visits when triaging which gaps to fill first. Do NOT assign a per-diem whose credentials/onboarding aren't current, and do NOT wait until the day-of to raise a foreseeable gap.

---

### 7. Reciprocity Offload Ledger (bank the "yes")

**Tactic.** When a clinician is having a hard week — personal crisis, burnout, a brutal SOC run — the manager proactively offloads visits and *protects* them. That deposit gets repaid later as discretionary effort: the Friday-afternoon eval, the SOC accepted near-full, the extra weekend ROC.

**Trigger / context.** Detected clinician overload, back-to-back heavy weeks, a known personal hardship, or a manager-initiated protective move.

**Why it works.** Culture is the multiplier on capacity. Clinicians go the extra mile for a branch that has demonstrably gone the extra mile for them. Reciprocity is real and it's earned in advance. A protected clinician is a retained clinician, and retention is capacity.

**Encode as system logic.**
- Track a per-clinician **load-strain signal**: rolling visit count vs band, consecutive heavy weeks, weekend/after-hours count, SOC density, recent PTO.
- Log **offload events** and **stretch events** as a lightweight ledger — not for surveillance/scoring, but so the branch can see reciprocity balance and prevent burnout.
- Alert when a clinician crosses into sustained overload → prompt a protective offload *before* a resignation-risk threshold.

**Train the AI agent.** Watch for sustained overload and recommend proactively offloading before burnout, especially for clinicians carrying stretch load. Frame stretch asks as favors to be balanced, not entitlements. Do NOT repeatedly route the extra visit to the same willing clinician — that "reliable yes" is exactly who burns out; distribute the ask and flag when one person is carrying the branch. Never present the ledger as a performance-ranking or use it to pressure a clinician.

---

### 8. Clear-Policy Protection (make "yes" safe)

**Tactic.** The branch has explicit, written policy/process for the hard moments — after-hours SOC expectations, weekend rotation, what "full" means, when it's OK to decline — so clinicians can stretch without fear of being blamed later. Protection is structural, not just a nice manager.

**Trigger / context.** Any recurring friction point where clinicians hesitate to say yes because the rules are ambiguous.

**Why it works.** Discretionary effort only shows up when the extra mile won't be punished. Ambiguity kills volunteering. Clear policy converts "I'm not sure I'm allowed" into a confident yes, which is directly capacity.

**Encode as system logic.**
- Encode **branch policy thresholds** as tool config: after-hours SOC window, weekend expectations, definition of "at capacity," decline-allowed conditions. The directive engine references these so asks are always policy-compliant.
- When the engine asks a clinician to stretch, attach the **policy basis** ("within weekend rotation policy; comp per PRN rate").

**Train the AI agent.** Only make stretch asks that fall inside encoded branch policy, and always cite the policy basis. If a needed ask falls outside policy, escalate to the manager rather than pressuring the clinician. Do NOT invent expectations the branch hasn't set.

---

### 9. SOC-Timeliness & Start-of-Care Protection

**Tactic.** The branch treats SOC-timeliness (referral-to-start interval) as a top-line capacity KPI, not a compliance afterthought. Fast, reliable starts are what referral sources actually buy.

**Trigger / context.** Continuous; alarms when the referral-to-SOC interval drifts up or a referral source's volume dips.

**Why it works.** A missed or slow SOC is lost capacity *and* a lost referral relationship. Protecting start timeliness keeps the referral precondition healthy. It's the clearest external signal the staffing model is right-sized.

**Encode as system logic.**
- Track **referral-to-SOC interval** per referral, segmented by source, discipline, geography. Alert on drift above a market-set target (e.g., >48h standard, tighter for hospital discharges).
- Correlate rising SOC intervals with SOC-slot fill and discipline balance to point at the *cause*.
- Track **decline-rate by referral source** as early warning.

**Train the AI agent.** Treat SOC timeliness as a growth metric. When it drifts, diagnose upstream — SOC slots full? LPN/PTA gap? territory mis-draw? — and recommend the specific staffing fix. Do NOT treat a slow SOC as merely a compliance flag.

---

### 10. Recert / Episode-End Discharge Forecasting (recycle capacity)

**Tactic.** The branch forecasts discharges and recert decisions weeks out, so freed-up caseload slots are matched to incoming referrals deliberately — capacity is *recycled* on a plan.

**Why it works.** Every discharge reopens a bookable slot in a territory. Seeing discharges coming lets the matching engine pre-commit that slot to a new referral in the same geography — near-zero friction, no idle capacity between patients.

**Encode as system logic.** Project upcoming **discharges and recert decisions** from episode data; expose as freeing slots by territory/discipline; feed into the referral-matching engine. Metric: **slot-recycle time**.

**Train the AI agent.** Anticipate discharges and pre-match incoming referrals to opening slots in the same territory. Do NOT hold a patient past clinical need to "keep the slot warm."

---

### 11. Financial-Health Capacity Lens (margin per skilled hour)

**Tactic.** The ED sizes and defends the model in dollars: cost-per-visit by discipline, margin per skilled hour, and the real cost of RN/PT time spent on assistant-level work.

**Why it works.** The cheapest capacity gain is usually *not* another RN — it's an LPN/PTA that frees existing RN/PT SOC slots. Seeing capacity in margin terms keeps the branch from over-hiring the expensive tier.

**Encode as system logic.** Attach **loaded cost + reimbursement** per visit type/discipline/payer; compute **margin per skilled hour** and **skilled-hours-leakage dollars**. On any hire recommendation, output a **tier comparison**: cost and SOC-capacity gained by LPN/PTA vs RN/PT for the same dollars.

**Train the AI agent.** Always compare tiers on cost and SOCs-unlocked; default to the lowest-cost tier that actually frees skilled slots. Do NOT recommend adding skilled FTEs when an assistant-tier hire unlocks the same SOC capacity for less.

---

### 12. Referral-Source Concentration & Pipeline Guard

**Tactic.** The branch monitors where referrals come from and defends against over-reliance on any single source — the staffing model is only as stable as the referral flow feeding it.

**Why it works.** Referrals are the precondition for everything. A concentrated pipeline means one relationship change can strand a whole staffing model overnight.

**Encode as system logic.** Track **referral volume and trend by source**; compute a **concentration index**; alert on over-concentration and on a major source's volume declining. Tie source trends to model-variance and decline-rate.

**Train the AI agent.** Watch referral-source concentration as a leading indicator of capacity risk. When a top source dips, check it against decline-rate and SOC-timeliness — if we're declining that source's referrals, it's a self-inflicted staffing problem. Do NOT treat referral volume as exogenous.

---

#### How these stack (for the tool's mental model)

1. **Referrals** must exist and stay diversified (Tactics 12, 9) — the precondition.
2. **Staffing model** is the primary effector: discipline balance (1), market-unique sizing (2), SOC-dedicated roles (3), sized in dollars (11).
3. **Territory management** gives near-automatic coverage: resting posture (5), matching engine (4, 10).
4. **Day-to-day management** absorbs variance: per-diem visibility (6), SOC-timeliness protection (9).
5. **Culture/leadership** multiplies it all: reciprocity (7), clear-policy protection (8).

The single highest-leverage thing the tool can teach the AI agent: **capacity is created at the SOC slot, and it is most often lost because the assistant tier is understaffed — never diagnose a "we're full" problem without first decomposing skilled clinicians' days by visit type.**

## SME Perspective — DCS / Clinical Manager

> Seeded v0 perspective (AI-generated from the DCS / Clinical Manager lens, grounded in the operator's strategy
> download). **To be validated with a real DCS/Clinical Manager.** Preserved verbatim per the
> [SME discovery framework](../sme-discovery-framework.md).

## Home Health Capacity Tactics — DCS / Clinical Manager Lens

Framing note: capacity in home health is not "open visit slots." It is **protected assessment capacity** (RN/PT hours that can absorb a new SOC) plus **defensible offload capacity** (routine visits an LPN/PTA can legally and safely carry). A great branch manages the *ratio* between these two, not the raw visit count. Everything below serves the operator's hierarchy: staffing model first (the primary effector), territory second, day-to-day third, culture as the multiplier.

---

### TACTIC 1 — The RN→LPN Routine Offload Sweep

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

### TACTIC 2 — PT→PTA Offload with the Reassessment Guardrail

**Tactic.** Same discipline on the therapy side: the PT keeps the eval, the 30-day reassessment, discharge, and any visit where progression of the exercise plan is a clinical decision; the PTA carries the established treatment visits (gait training at a set assist level, established HEP progression, modality delivery) between reassessment points.

**Trigger/context.** PT weighted-load ≥ 90%, or a therapy-only SOC/eval is pending and the PT has no slot. PTA has open capacity.

**Why it works.** In home health the PT *must* personally perform the 30-day functional reassessment and cannot delegate evaluation or POC change. But the interval treatment visits are the PTA's lane. Offloading them protects the PT's eval capacity — the thing that actually converts a therapy referral into an admitted patient.

**Encode as system logic.**
- Track `days_since_last_PT_reassessment` per therapy patient; the mandatory PT reassessment visit is **pinned** to the PT and cannot be offloaded.
- PTA-eligible visits require: eval complete, POC established, patient progressing or stable, and the visit falls *before* the reassessment-due date.
- Directive engine surfaces PTA offload candidates only in the window between reassessment points; auto-locks the reassessment visit to the PT and warns if it drifts past day 30.

**Train the AI agent.** The agent reasons about the reassessment cadence as a hard rail: it may offload treatment visits to a PTA *only* inside a valid reassessment window and *only* for a progressing/stable patient. Guardrail: never let a PTA-only stretch cross the 30-day mark — if the reassessment isn't scheduled, block further PTA offloads and escalate "PT reassessment overdue." Also detect discipline-shortage patterns (too few PTAs → PT overloaded with routine gait training) and raise a staffing-model signal, not just a scheduling fix.

---

### TACTIC 3 — SOC Assignment by the Nursing-Tie Rule

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

### TACTIC 4 — SOC-Dedicated Slot Protection

**Tactic.** The staffing model designates SOC-dedicated nurses and PTs whose calendars carry **known, bookable SOC slots** (e.g., two protected SOC windows/day). The manager guards these slots — routine visits do not backfill them except as a last resort, and only with manager sign-off.

**Why it works.** Referrals are the precondition for everything; the constraint on converting them is assessment capacity in the right timeframe (SOC generally within 48h; ROC within 48h of hospital discharge). Pre-committing dedicated slots turns referral absorption from a scramble into an almost-automatic posture.

**Encode as system logic.**
- Clinician attribute `soc_dedicated = true` with `protected_soc_slots_per_day = N`.
- Capacity cockpit displays **SOC slots available today/tomorrow** as a first-class number, separate from total open visits.
- Backfilling a protected SOC slot with a routine visit requires an override with `reason:` and drops the branch's "SOC readiness" indicator.
- Alert when protected SOC slots available in the next 48h fall below the branch's rolling referral rate.

**Train the AI agent.** Treat SOC slots as a protected reserve, report them distinctly, and resist filling them with routine work. When referral inflow forecast exceeds protected SOC capacity, proactively propose offloading routine visits (Tactics 1–2) to *manufacture* more SOC slots rather than consuming the reserve. Guardrail: recommend backfilling a protected slot only when every other capacity lever is exhausted, and flag the SOC-readiness degradation.

---

### TACTIC 5 — ROC Timing Protection (the 48-Hour Rail)

**Tactic.** When a patient is hospitalized and discharged back, the branch protects the ROC assessment inside the required window (generally within 48 hours of discharge home or per physician order). The great branch tracks patients *out* to the hospital as pending returns, not as freed capacity.

**Why it works.** A missed or late ROC is a compliance and quality failure and a lost patient. ROCs follow the same nursing-tie rule as SOCs (RN if nursing on case).

**Encode as system logic.**
- Patient status `hospitalized` with `expected_return` flag; on discharge event, spawn a `ROC_due` task with a 48h countdown routed to the correct discipline pool (nursing-tie rule).
- Cockpit reserves anticipated ROC demand against SOC-dedicated capacity so returns don't oversubscribe slots.
- Escalating alerts at 24h / 12h / breach on any un-slotted ROC.

**Train the AI agent.** Maintain a live "pending returns" list and pre-position ROC capacity. On a discharge event immediately route the ROC by the nursing-tie rule and confirm a slot inside 48h. Guardrail: never treat a hospitalized patient's freed visits as durable capacity to give away; flag them "on hold — ROC pending."

---

### TACTIC 6 — Acuity-Weighted Caseload (Kill the Raw Visit Count)

**Tactic.** The manager judges a "full" caseload by **weighted acuity and travel**, not by number of patients or visits. A nurse with 6 high-acuity, complex, geographically spread patients may be fuller than one with 9 stable maintenance patients.

**Why it works.** Home health acuity varies enormously. Weighting by acuity + visit frequency + drive time + documentation burden gives the true picture and is how experienced managers actually decide.

**Encode as system logic.**
- Compute `weighted_caseload = Σ(visit_acuity_score × frequency) + travel_factor + coordination_burden` per clinician, not a headcount.
- Acuity score drivers: wound-vac/complex wounds, new meds/first-dose, IV therapy, unstable vitals trend, high comorbidity count, frequent physician contact, behavioral/social complexity.
- Cockpit shows **weighted load %** as the primary fullness metric; raw visit count is secondary. "Available for SOC" is gated on weighted load, not visit count.

**Train the AI agent.** Always reason in weighted terms. When asked "who can take this?" rank by remaining weighted capacity and territory fit, and explain *why* a clinician with fewer patients is actually fuller. Guardrail: never recommend loading a clinician just because her raw count is low; surface the acuity mix. Detect chronically mis-weighted clinicians as a staffing-model signal.

---

### TACTIC 7 — Recert / Reassessment Windows as Hard Scheduling Constraints

**Tactic.** The branch treats compliance windows as immovable rails that pre-consume capacity: the **60-day recert**, the **PT 30-day functional reassessment**, the **14-day HHA supervisory visit**, and RN supervision of LPNs per state rule. These are scheduled *first*; discretionary capacity is what's left.

**Why it works.** Miss a recert and the episode is jeopardized; miss the 14-day aide supervisory and you have a survey deficiency; let the PT 30-day slip and therapy visits become non-billable. These consume specific clinician types on specific dates — the true baseline load beneath all "open" capacity.

**Encode as system logic.**
- Per patient track: `recert_window` (day 56–60 target), `pt_reassessment_due` (≤ day 30), `hha_supervisory_due` (≤ 14 days), `lpn_supervision_due` (state interval).
- These generate **pinned, discipline-specific tasks** reserved against capacity *before* the cockpit shows "available" slots.
- Directive engine surfaces the end-of-cert-period cluster early ("recert wall in 10 days: 7 RN recerts due") so it's spread, not crammed.

**Train the AI agent.** Reserve compliance-window capacity first, then report discretionary capacity as the remainder — never show a compliance-obligated slot as free. Forecast recert clusters and propose smoothing them. Guardrail: may not schedule a new SOC into capacity owed to a recert/reassessment/supervisory obligation without flagging the conflict. Know *which discipline* each window requires and route accordingly.

---

### TACTIC 8 — Missed-Visit 48-Hour MD Notification Handling

**Tactic.** When a visit is missed, the branch executes the protocol: document, attempt reschedule within the frequency order, and **notify the physician within 48 hours** when the missed visit affects the plan of care. The great branch also treats the missed visit as a capacity signal.

**Encode as system logic.**
- Missed-visit event spawns: (a) `md_notification_due` 48h countdown, (b) reschedule task honoring the ordered frequency, (c) increment on `patient_missed_streak` and `clinician_missed_rate`.
- Escalating alert on the 48h MD notification until documented.
- Pattern flags: patient missed_streak ≥ 2 → willingness/logistics review; clinician missed_rate spike → schedule/territory review.

**Train the AI agent.** On a missed visit immediately open the MD-notification clock and the reschedule task (respecting frequency), and watch for patterns. Guardrail: never silently absorb a missed visit as "freed capacity" — the reschedule obligation persists and the MD notification is mandatory when the POC is affected. Escalate repeated patient refusals as a willingness/logistics issue and clinician missed-rate spikes as a workload/territory issue.

---

### TACTIC 9 — Offload-as-Protection (the Culture Multiplier)

**Tactic.** The manager *proactively* lightens a clinician's week before being asked — pulling two routine visits off an RN who just carried three SOCs — explicitly as protection. The branch banks reciprocity so the clinician says "yes" when it later needs a same-day SOC.

**Why it works.** This is the culture/leadership multiplier. Protection generates discretionary effort and reciprocity. Raw utilization maximization destroys this; deliberate slack builds it.

**Encode as system logic.**
- Track `recent_spike_score` per clinician (SOC count this week, patient deaths, after-hours calls, weekend work, consecutive high-acuity days).
- Directive engine proposes *proactive* offloads for spiked clinicians even when not over threshold, labeled "protection offload."
- Track a lightweight `reciprocity_ledger` so the tool doesn't repeatedly tap the same person; fairness signal.

**Train the AI agent.** Watch for spike patterns and *recommend* relief before burnout, framing it as protection. When it later needs a discretionary same-day SOC, preferentially ask clinicians recently protected and not over-tapped. Guardrail: this is a recommendation to the human manager, never automated schedule manipulation. Never over-optimize a "protected" clinician back into overload the same week; flag if the branch is systematically burning the same few reliable people (a staffing-model gap).

---

### TACTIC 10 — LPN/PTA Utilization Floor (Balance at Every Discipline Level)

**Tactic.** The manager monitors whether assistants are *under-used* — RNs drowning in routine while LPNs sit light means the mix is wrong or the offload discipline is failing.

**Why it works.** This is the primary effector — a balanced staffing model at *all* discipline levels. Under-utilized assistants are wasted capacity and a signal the offload sweep isn't running. Fixing the ratio is often higher-leverage than any day-to-day scheduling move.

**Encode as system logic.**
- Compute per-territory `assessing_vs_assistant_load_ratio`. Alert when RNs > threshold while LPNs < floor (or PT vs PTA).
- Track `offload_capture_rate` = offload-eligible routine visits actually assigned to assistants ÷ total offload-eligible. Low capture = discipline failing.
- Surface as a staffing-model signal, distinct from day-to-day directives.

**Train the AI agent.** Monitor the assessing-vs-assistant balance per territory and flag imbalance as a *staffing-model* recommendation (hire/redeploy an LPN, PTA) rather than solving it visit-by-visit. Report offload capture rate as a branch health metric. Guardrail: distinguish a structural mix problem (needs hiring, escalate to DCS) from a transient one; don't paper over a staffing gap with unsustainable overtime.

---

### TACTIC 11 — Territory Resting Posture for Referral Absorption

**Tactic.** The manager sets clinician territories so that a new referral in any ZIP lands near a clinician who already has capacity and geographic fit — the "resting posture" where absorbing a referral is near-automatic. SOC-dedicated clinicians are positioned to cover the highest-referral geographies.

**Why it works.** A referral in a well-covered ZIP costs little capacity to absorb; one in a gap costs a long drive, a mis-fit clinician, and a burned slot. Good resting posture keeps *travel_factor* on new admits low.

**Encode as system logic.**
- Map clinician territory to referral heat map; compute `referral_absorption_readiness` per ZIP = (nearby clinician capacity × geographic fit).
- Flag ZIPs with high referral rate and low nearby capacity as coverage gaps.
- SOC slot matching includes travel distance; the matching engine ranks candidates by (correct discipline pool × weighted capacity × proximity).

**Train the AI agent.** When matching a referral, optimize jointly for the nursing-tie discipline rule, weighted capacity, and proximity — not availability alone. Surface persistent coverage gaps as a territory-design recommendation. Guardrail: propose territory adjustments to the manager; do not unilaterally rewrite assignments, and never sacrifice the SOC nursing-tie rule for a shorter drive.

---

### Cross-cutting agent guardrails (apply to all tactics)

- **The AI proposes; the clinical manager disposes.** Every reassignment, offload, or protection move is a recommendation with visible reasoning. Licensure-scope and POC decisions belong to licensed clinicians.
- **Scope rules are hard rails, never optimization variables.** Nursing-tie SOC/ROC rule, LPN-can't-assess, PTA-can't-evaluate-or-do-the-30-day, RN-supervises-LPN — the agent may not "route around" a shortage by violating scope. Shortages escalate as capacity gaps.
- **Compliance windows pre-consume capacity.** Recert (60), PT reassessment (30), HHA supervisory (14), 48h MD missed-visit notification, 48h ROC — reserved before any slot is shown "free."
- **Stale or missing clinical data blocks auto-eligibility.** No offload on stability data older than one visit; no offload on any note containing deterioration language.
- **Distinguish structural from transient.** A recurring shortfall is a staffing-model signal to the DCS; a one-off is a day-to-day fix. Label which.
- **Protect the people who protect capacity.** Track relief/reciprocity so the same reliable clinicians aren't chronically burned — flag it as a leadership issue.

## SME Perspective — Senior Scheduler / Staffing Coordinator

> Seeded v0 perspective (AI-generated from the scheduler / staffing-coordinator lens, grounded in the operator's
> strategy download). **To be validated with a real senior scheduler.** Preserved verbatim per the
> [SME discovery framework](../sme-discovery-framework.md).

## Day-to-Day Capacity Execution Tactics — Scheduler / Staffing-Coordinator Lens

These are the moves a great scheduler actually makes between 7:00 AM chaos and the 4:30 PM "did everything get covered" check. Each is written to be built into the 9-tab tool and to train an AI agent operating the capacity cockpit.

---

### 1. The Standing Per-Diem "Warm List" (engagement before you need them)

**Tactic.** The great scheduler never cold-calls a per-diem in a crisis. They maintain a live, ranked warm list and touch every active per-diem on a cadence — a low-stakes "you around Thursday/Friday this week?" text sent Monday — *before* there's a specific visit to fill. Per-diems who get contacted only when desperate quietly disengage.

**Trigger/context.** Every Monday AM, and any time a per-diem's last-worked date crosses a staleness threshold.

**Why it works.** Per-diem labor is an attention market. The clinician who feels remembered keeps their week loosely open for you. Silence reads as "they don't need me." Disengagement is almost always preceded by a gap in contact, not a bad visit.

**Encode as system logic.**
- Track per per-diem: `last_worked_date`, `last_contacted_date`, `avg_visits_per_week_trailing_4wk`, `accept_rate_trailing_20_asks`, `stated_availability_window`.
- **Disengagement flag:** fire when `days_since_last_worked > (2 × personal_median_gap)` OR `days_since_last_contacted > 7` OR `accept_rate dropping ≥30% vs. own baseline`.
- Weekly "warm-touch due" queue = all active per-diems with `last_contacted_date > 5 business days`.

**Train the AI agent.** Draft the Monday availability-check outreach per per-diem, personalized with their recent pattern. Propose; do **not** auto-send a booking. Guardrail: outreach is a *question about availability*, never a committed assignment. Escalate disengagement-flagged per-diems with a one-line "haven't worked in 18 days, median gap is 6 — recommend a personal call, not a text."

---

### 2. Forecast-the-Gap, Publish-the-Need (make the need visible early)

**Tactic.** The scheduler projects next week's discipline-level gap from current census + known referral pace + PTO calendar, and *publishes the need* to the per-diem pool 5–7 days out — "we're going to be short 2 RN SOC slots Wed/Thu in the north territory."

**Why it works.** The coordination burden a tool removes is exactly this: turning a diffuse anxiety into a specific, claimable, published slot. It converts the ask from "please rescue me" (low yield) to "here's paid work if you want it" (high yield).

**Encode as system logic.**
- Gap forecast per day per discipline = `projected_demand (scheduled + expected referrals from trailing pace + recert/SOC pipeline) − projected_supply (FT capacity − PTO − on-call recovery − territory load)`.
- Any day where `projected_gap ≥ 1` in a discipline surfaces a **publishable slot** with date, discipline, territory cluster, visit type.
- Per-diem-facing view: "open slots this/next week."

**Train the AI agent.** Run the forecast nightly, generate the ranked list of publishable slots, match each to the 3 best-fit per-diems. Draft the "here's what's open" broadcast. Guardrail: forecast and propose; a human confirms the published gap before broadcast (prevents over-publishing a slot a FT clinician can absorb). Never double-promise one slot to two per-diems.

---

### 3. Territory-First Assignment (cluster before you optimize anything else)

**Tactic.** When placing any visit, assign to the clinician whose *resting posture already sits in that cluster* before considering anyone else. Protect the geographic spine of each clinician's day — a new visit slots into an existing loop, not a 40-minute detour. Windshield time is the silent capacity killer.

**Encode as system logic.**
- Each clinician carries a `home_territory` + `resting_posture`.
- Assignment scoring: `proximity_score` = distance from new visit to clinician's *nearest already-scheduled visit that day* (not to home base — to their actual route).
- Directive engine ranks: in-cluster clinician with capacity > in-cluster near cap > adjacent-territory > cross-territory (flagged, requires reason).
- Hard flag when an assignment adds `> X min` incremental drive to a clinician's existing route.

**Train the AI agent.** Propose assignments ranked by route-incremental drive time, not straight-line distance from home. Show the top 2–3 with "adds 8 min to Maria's existing Tuesday loop" vs. "adds 35 min, crosses into east territory." Guardrail: never silently cross a territory boundary; surface it with the reason and the drive-time cost.

---

### 4. The Last-Minute Referral Decision Tree (who to ask, in what order)

**Tactic.** When a same-day/next-day referral lands, run a fixed order of operations: (1) FT clinician **already in that cluster** with headroom; (2) assessing clinician who can **offload** a routine visit to an assistant to free the slot; (3) SOC-dedicated nurse/PT whose bookable slot fits; (4) per-diem in the warm list for that territory; (5) escalate to branch leadership. Honor the SOC rule at every step — RN takes the SOC if nursing is on the case; PT only when nursing is NOT on the referral.

**Why it works.** A repeatable tree removes emotional bias and protects the highest-leverage capacity. Asking the in-cluster FT first is cheapest. Offloading routine to assistants frees skilled slots. Going to per-diem before exhausting cheaper internal capacity burns your scarce resource.

**Encode as system logic.**
- Matching + directive engine executes the tree in order, filtered by discipline eligibility.
- **SOC gate:** `if nursing_on_case → require RN for SOC; elif no_nursing → PT eligible`. Hard rule.
- Assessing→assistant offload: engine detects when a candidate is at cap but holds ≥1 assistant-eligible routine visit that day, and proposes the swap.

**Train the AI agent.** Walk the tree top-down and return the *first viable* placement plus next-best fallback, showing why each earlier tier was skipped. Guardrails: SOC rule is inviolable; propose offloads and per-diem asks but do not commit them; if it reaches "escalate," hand to a human with the full trail, never auto-decline a referral.

---

### 5. Protect-the-Clinician Sequencing (how the ask lands without breaking them)

**Tactic.** Before adding the last-minute visit, check what you're about to do *to the person*, not just the schedule. Won't drop a 6th visit on the clinician who did on-call last night. When they must ask a stretched clinician, they lead with the protection ("I'll pull your Friday routine to make room") so the ask is a trade, not a pile-on.

**Encode as system logic.**
- Per clinician daily: `visit_load vs. sustainable_cap`, `on_call_last_night` flag → mandatory recovery buffer, `consecutive_high_days` counter.
- **Fatigue/over-ask guard:** block or hard-flag assignment when `load ≥ cap`, `on_call_recovery = true`, or `asks_this_week > threshold`.
- Track `ask_count` and `yes_count` per clinician (over-relied-upon flag).

**Train the AI agent.** Surface the human cost inline: "Dev is the closest fit but did on-call last night — recommend protecting; next best is Priya, +10 min." When an ask to a stretched clinician is unavoidable, draft it *with the trade included*. Guardrail: never frame a naked pile-on; pair a stretch-ask with an offload or acknowledgment, and flag chronically over-asked clinicians to leadership.

---

### 6. You Can't Un-Ring the Bell: Read Real Availability (accepted ≠ pullable)

**Tactic.** Track the *true* state of every clinician's day: **once a visit is accepted and communicated to the patient, you can't quietly pull it back** to reassign the clinician elsewhere. Distinguish "has open time" from "is actually available" (PTO booked, on-call recovery owed, patient-willingness windows).

**Encode as system logic.**
- Visit states: `proposed → accepted → patient_confirmed → completed`. **`patient_confirmed` is locked** — engine cannot reassign it to free the clinician; only released via explicit human action with a reason.
- Availability = `calendar_open − PTO − on_call_recovery_owed − stated_unavailable_windows − patient_willingness_constraints`. Never equal to raw white space.
- On-call recovery generates an automatic non-availability block the morning after.

**Train the AI agent.** Compute *true* availability, never raw open time, and treat `patient_confirmed` visits as immovable. Guardrail: any reshuffle touching a confirmed visit requires explicit human release; flag the patient-commitment cost. State the availability number's basis ("Maria has 2 open blocks but 1 is on-call recovery — 1 truly available").

---

### 7. Fast Backfill on Cancellation/Discharge (recover the freed slot before it evaporates)

**Tactic.** When a visit cancels or a patient discharges, treat the freed slot as a *perishable asset* and immediately match it against waiting demand — the SOC pipeline, a recert due, a per-diem who wanted hours — ideally to the clinician *already going to be in that area*.

**Encode as system logic.**
- Discharge/cancellation → backfill matcher (matching engine run in reverse): freed slot's `time + territory_cluster + freed_clinician` becomes the key.
- Rank waiting demand by `same_cluster_fit > SOC/recert_due_urgency > per_diem_wanting_hours`.
- Time-decay urgency: backfill priority escalates the longer a same-day slot sits unfilled.

**Train the AI agent.** On any cancellation event, instantly propose the best backfill — prioritizing the freed clinician's own cluster so their route stays intact — within the decay window. Guardrail: propose, human confirms (especially anything requiring a patient/clinician contact); never silently rebook a clinician who may have already left the area without confirming availability.

---

### 8. The Right Ask, Framed Right, Timed Right (and knowing when NOT to ask)

**Tactic.** Pick *which* clinician to ask by yield, not proximity to your inbox — accept-rate history, current load, relationship state — then frame for a yes (specific, bounded, with the trade or the "why you") and time it for when they can actually say yes. Know when **not** to ask: not the on-call-recovery clinician, not the person asked twice yesterday, don't broadcast-blast a slot a targeted ask would fill cleaner.

**Encode as system logic.**
- Per clinician: `accept_rate`, `preferred_visit_types`, `preferred_days/times`, `recent_ask_count`, `relationship_state`.
- **Ask-yield score** = `accept_rate × fit × availability_true × (1 − recent_ask_fatigue)`.
- **Do-not-ask filter:** exclude on-call recovery, at-cap, already-asked-N-times-this-window, stated-unavailable.
- Prefer *targeted single ask* to top-scorer over broadcast when one candidate's yield exceeds a confidence threshold.

**Train the AI agent.** Rank candidates by ask-yield, draft the ask with specifics baked in (exact time, drive-from-last-visit, end-of-day, the trade), pick send timing against the person's response pattern. Guardrails: enforce the do-not-ask filter absolutely; cap asks per clinician per window; prefer a targeted ask; never double-commit a slot while an ask is outstanding.

---

### 9. Balanced-Model Watchdog at the Discipline Level (spot the bottleneck before it bites)

**Tactic.** Watch the *ratio* of work to skill level, not just headcount. Notice when RNs are eating routine visits an LPN should carry, or SOC demand is outrunning the SOC-dedicated slots, and escalate it as a staffing-model signal — a *pattern* problem, so leadership can fix the mix.

**Encode as system logic.**
- Track `skill_level_utilization`: % of RN time on RN-only work vs. LPN-eligible; `SOC_demand vs. SOC_dedicated_capacity`; discipline-level `overload_index`.
- Signal fires when RNs perform `> X%` sub-skill visits over a trailing window, or SOC demand exceeds dedicated slots N days running.
- Feed the signal to the capacity strategy layer, tagged "staffing-model," distinct from day-to-day alerts.

**Train the AI agent.** Monitor utilization ratios and raise a *strategic* flag ("RNs covered 14 LPN-appropriate visits this week — recurring, recommend LPN capacity review") separate from daily assignment noise. Guardrail: classify as a model-level insight for leadership, not something to solve by reshuffling; never mask a structural shortage by silently overloading RNs.

---

### 10. Per-Diem Retention Ledger (protect the relationship, not just the booking)

**Tactic.** Run a systematic ledger on each per-diem — did we give them the hours we implied? did we cancel last-minute and cost them a paid day? are we spreading work fairly? — and actively repair debts. Per-diems leave over *fairness and reliability*, rarely over one bad visit.

**Encode as system logic.**
- Per per-diem: `hours_promised_vs_delivered`, `agency_cancellations_on_them` (count + recency), `share_of_pool_hours`, `days_since_last_offered_work`.
- **Debt flag:** agency-canceled a booked per-diem → mark "owed," prioritize for the next fitting slot.
- **Fairness flag:** pool-hour distribution skew beyond threshold → surface under-utilized willing per-diems.

**Train the AI agent.** Maintain the ledger and, when a fitting slot opens, give owed/under-utilized per-diems a ranking boost so repair and fairness happen automatically. Guardrail: fit and SOC/discipline rules still gate — boost an owed per-diem *among eligible* candidates, never book an unqualified one to settle a debt. Flag when the pool is concentrating on a few names.

---

### 11. Morning Blast-Radius Check (triage the day before it triages you)

**Tactic.** First thing, scan for the day's *fragility points* — every visit that depends on a single clinician with no backup, every SOC with a hard time window, every per-diem still unconfirmed — and pre-solve the top 2–3 before the phone rings.

**Encode as system logic.**
- Daily **fragility scan:** flag visits with `no_backup_candidate_in_cluster`, `hard_time_window`, `unconfirmed_per_diem`, `single_clinician_dependency`.
- Compute a per-day `capacity_slack` score; low slack + high fragility = priority pre-solve list.
- Surface top N fragility points ranked by blast radius.

**Train the AI agent.** Run the fragility scan at start of day and hand the human a ranked "here are today's 3 weak points and a pre-lined backup for each." Guardrail: pre-identify and pre-draft fallbacks but do not pre-book them (that wastes capacity on failures that don't happen); hold the backup ready to fire the instant the trigger occurs.

---

#### Cross-cutting agent guardrails (apply to all tactics)
- **Propose, don't commit:** the agent drafts asks, ranks placements, and pre-lines backups; a human (or an explicit per-diem accept flow) closes anything involving a person's time or a patient commitment.
- **SOC rule and `patient_confirmed` locks are inviolable** — never overridden to optimize.
- **No double-booking / no double-asking** one slot while an ask is outstanding.
- **Show the cost, not just the pick:** every recommendation carries the drive-time, fatigue, or relationship cost that justifies it.
- **Separate strategic signals from daily noise:** model-level imbalances route to leadership, not into the day's reshuffle logic.

## SME Perspective — Field RN / SOC Nurse (the clinician ground truth)

> Seeded v0 perspective (AI-generated from the field-RN / SOC-nurse lens, grounded in the operator's strategy
> download). **To be validated with real field clinicians.** Preserved verbatim per the
> [SME discovery framework](../sme-discovery-framework.md). This brief carries the strongest "the agent must
> never do X" guardrails — treat them as hard rails.

## Field RN / SOC-Nurse Ground Truth: How Capacity Is Actually Protected and Expanded

Written from the seat: I carry a route, I do Starts-of-Care, and I've watched good branches run at 110% for years while "efficient" branches bled nurses out in eighteen months. Here's what's real. The tool and the AI agent can either respect this or destroy it — there is no neutral.

---

### 1. The SOC-Nurse "Known Slots" Model — Protect the Dedicated Role or Lose Predictability

**Principle.** A nurse (or PT) dedicated to Starts-of-Care and Resumptions converts referral intake from a scramble into a *schedulable inventory*. If I own SOCs Mon–Fri, the branch knows it has, say, 3–4 bookable admission slots per SOC clinician per day — a hard, plannable number. That is the single most powerful capacity lever at the clinician level because a missed/late SOC is a lost referral and a compliance clock (the 5-day OASIS window, the 48-hour contact) that never resets in your favor.

**Why violating it destroys capacity.** SOCs are the highest-cognitive-load, longest, least-interruptible visits we do — full OASIS, med rec, F2F verification, plan of care, homebound justification, teaching, coordinating the discipline team. You cannot do a quality SOC *between* two routine wound cares. When a branch "borrows" the SOC nurse for routine overflow, admissions slip, OASIS accuracy drops (which is money and Star ratings), and the predictable slot inventory evaporates. **The erosion is always silent and always framed as "just today."** Three "just todays" a week and the model is dead.

**Encode as system logic.**
- Model SOC/ROC capacity as a *separate reservable resource pool*, not fungible visit points. Show "admission slots available today/this week" as a first-class number.
- Flag any assignment that pulls a SOC-dedicated clinician onto a routine visit as **role erosion**, with a running weekly counter.
- Track SOC-slot utilization and *unfilled* slots separately. An idle SOC slot is not "waste to backfill" — it is *absorption headroom for tomorrow's referral*.

**Train the AI agent.** Treat SOC/ROC capacity as **protected inventory**. Default reasoning: routine overflow is solved by routine clinicians, LPN/LVN rebalancing, or per-diem — *never* by raiding the admission pool. If it must ever propose pulling a SOC nurse, it must (a) show the admission-slot cost, (b) confirm no other lane exists, (c) frame it as an exception requiring branch-manager sign-off, (d) log it against the erosion counter. **Never** silently reassign a SOC clinician to fill a same-day routine gap. **Never** treat an open SOC slot as idle capacity to optimize away.

---

### 2. The SOC Assignment Rule Is Clinical Law, Not a Preference

**Principle.** RN performs any SOC where nursing is on the case. PT performs the SOC only when nursing is **not** on the referral. This is discipline-scope and reimbursement reality.

**Why violating it destroys capacity.** Send a PT to open a case that needs nursing assessment — clinically unsafe, re-do required, wasted visit. Or burn an RN slot on a therapy-only case a PT could have admitted — starving your nursing SOC inventory. Both are capacity *destroyed*, not moved.

**Encode as system logic.** Hard rule: `nursing_on_case == true → SOC must route RN`. Cross-discipline SOC assignment is a **hard-fail with reason required**. Surface the rule inline.

**Train the AI agent.** Apply the rule deterministically before any optimization. It may not "trade" an RN SOC to a PT to balance a daily load. If a referral's discipline mix is ambiguous, flag for human clarification — do not guess to keep the queue moving.

---

### 3. Visit-Points Lie: Capacity Is Windshield + Documentation + After-Hours, Not the Visit

**Principle.** The real unit of a clinician's day is **visit + drive + charting + coordination**, not the visit alone. A 45-minute wound care 40 minutes away with a complex note is *not* the same "point" as a 45-minute recert next door.

**Why violating it destroys capacity.** Home health is a windshield job — drive is 25–40% of my day and non-linear. Documentation mostly happens *after* the last visit, on my couch. A tool that counts visits and ignores drive + doc will *always* overload the efficient nurse who says yes, and look "balanced" on the dashboard while I'm charting at 9pm. That's the exact profile of the nurse who quits in month fourteen.

**Encode as system logic.**
- Capacity must include **estimated drive time** (real geo-routing, not straight-line), **documentation load per visit type** (SOC/ROC/recert >> routine), **coordination overhead**.
- Show a "true day" estimate in *time*, not points.
- Flag routes where drive time exceeds a threshold % of the clinical day — a *territory* problem surfacing as a clinician problem.
- Track **documentation debt** (visits completed but not charted) as a capacity liability.

**Train the AI agent.** When it says "you have capacity for one more," reason in *time-of-day and total workload*, including drive and the note that visit generates. Know a Friday-afternoon SOC 30 minutes out is a 2.5-hour commitment, not "one visit." **Never** present spare capacity on visit-count alone. **Never** schedule the marginal visit in a way that predictably pushes charting past end-of-day without saying so.

---

### 4. Territory as "Resting Posture" — Geography Is Capacity Before Anyone Is Asked to Stretch

**Principle.** Well-drawn territories mean coverage and referral absorption are near-automatic — the clinician nearest the patient takes it without anyone burning goodwill. Territory is the standing arrangement that *reduces the number of asks* the branch ever has to make.

**Why violating it destroys capacity.** Every cross-territory assignment spends drive time AND goodwill (an "ask"). When territories are wrong, the tool makes constant day-to-day asks to paper over a structural gap — each drawing down the reciprocity bank. Fix the posture and the day-to-day gets quiet.

**Encode as system logic.** Detect chronic cross-territory routing and *unabsorbed referral clusters* and surface them as **territory-design signals to leadership**, distinct from daily assignment.

**Train the AI agent.** Prefer in-territory continuity for routine routing. When repeatedly reaching across territory lines to cover, **escalate the pattern as a structural finding**, not just more daily stretch-asks. Distinguish "one-time exception" from "the map is wrong."

---

### 5. What Makes a Clinician Say YES: Framing, Notice, and a Real Out

**Principle.** The extra Friday eval gets a yes when the ask is (1) *specific* ("Mrs. R, 2:15, 12 minutes from your last stop, straightforward recert"), (2) *early* (notice, not ambush), (3) *honest about size* (drive + doc included), and (4) *refusable without penalty*. Vague, late, dishonestly-sized, or coercive = the yes rots into resentment even when I say yes.

**Why violating it destroys capacity.** I go the extra mile for a branch that respects my time enough to ask well. A 4:45pm "can you also take this SOC across town" with no context is not a request, it's a trap — I do it once and start declining the reasonable ones too. Discretionary capacity is renewable *only if you don't strip-mine it.*

**Encode as system logic.**
- Any discretionary ask carries a **structured payload**: exact patient/time, drive delta, doc load, why-you, and a one-tap **decline with no logged penalty**.
- Track **notice lead time** on asks; flag chronic last-minute asking as a process failure.
- Distinguish *planned load* from *discretionary ask* in every clinician's view — never blend the extra in to hide the stretch.

**Train the AI agent.** Frame every ask concretely, early, honestly sized, with a genuine no. **Never** use urgency/guilt/scarcity language ("no one else can, patient will suffer, you're our only option") to manufacture a yes. **Never** disguise a discretionary ask as a normal assignment. A no is data, not defiance — record it neutrally and route elsewhere.

---

### 6. Reciprocity Is the Currency of Discretionary Effort — And It Has a Ledger

**Principle.** I say yes to the manager who offloaded my visits during my mother's surgery. The extra Friday SOC is *repayment*, freely given, because the branch banked trust with me first. Reciprocity is real, directional, and it depletes.

**Why violating it destroys capacity.** The flexible clinicians are the ones a naive optimizer *always* picks — they say yes, so the algorithm asks them more, so they burn out first. That's the flexible-nurse death spiral, and it's algorithmically induced. Branches keep capacity by *spending down their own goodwill* (managers who protect and offload) *before* drawing on the clinician's.

**Encode as system logic.**
- Maintain a **fairness/reciprocity ledger**: who's been asked, who's said yes, who got protected when *they* needed it. Surface skew ("Nurse A has absorbed 7 of the last 9 discretionary asks").
- Weight routing to **spread discretionary load** and *not* punish reliability with more work.
- Track branch→clinician support events (offloads during hardship), not just clinician→branch. Reciprocity is bidirectional.

**Train the AI agent.** Before asking, check the ledger. Prefer the clinician who *hasn't* been tapped. When one person is carrying the discretionary load, **surface the imbalance to leadership** rather than asking them a tenth time. **Never** exploit reliability — "she always says yes" is a reason to protect her, not to ask her again.

---

### 7. Continuity of Caregiver — Default to It, and Know Exactly When to Bend

**Principle.** Same clinician across a patient's episode is clinically real: I catch the subtle decline because I saw the baseline, the patient admits they haven't been taking the water pill, families stop re-explaining. Continuity should be the *default*; routing efficiency bends to it — **except** at defined break points.

**Why violating it destroys capacity.** Continuity *creates* capacity downstream: fewer missed changes, fewer avoidable rehospitalizations (a Compassus-level outcome and referral-source trust metric), faster visits from rapport. But rigid continuity destroys capacity when it forces a 40-minute cross-town drive for a stable routine recert. **Bend for:** stable/low-acuity, pure logistics, PRN coverage; **protect for:** SOC→follow-up handoff, wound cases, decline-watch, psych/behavioral, end-of-life.

**Encode as system logic.** Tag each patient with a **continuity-sensitivity level** (protect / flexible). Optimizer honors "protect" as a strong constraint; overrides continuity only for "flexible" patients or with a stated reason. Track continuity rate as an *outcome* metric; watch for continuity breaks predicting rehospitalization.

**Train the AI agent.** Default to the established caregiver. Trade continuity for efficiency **only** on flexible-tagged patients, and state the tradeoff. **Never** break continuity on a protected patient (wound, decline-watch, psych, EOL, active SOC episode) purely to smooth a route. When continuity must break, flag a **warm handoff need** (notes, heads-up) rather than a silent swap.

---

### 8. Burnout and Turnover Are Capacity Destruction on a Lag — Optimize for the Quarter, Not the Day

**Principle.** Every day you run the flexible nurses hot, the dashboard looks great. The bill comes 6–14 months later as a resignation, and losing one experienced SOC-capable RN removes *months* of admission capacity plus onboarding drag.

**Why violating it destroys capacity.** The most expensive thing a branch can do is lose a tenured field RN — getting a new hire to independent-SOC competence is a 3–6 month capacity hole. A tool that can't *see* the lag trades a nurse's longevity for this week's numbers — and does it to your *best* people first, because they absorb.

**Encode as system logic.**
- Track **leading burnout indicators** per clinician: sustained utilization above a sane ceiling, documentation-debt trend, declining yes-rate, PTO not taken, after-hours charting, consecutive high-load days.
- Model **turnover cost** explicitly — a projected resignation is a projected capacity cliff.
- Enforce a **utilization ceiling** the optimizer cannot exceed without human override.

**Train the AI agent.** Optimize the *quarter*, not the day. Treat sustained overload as a cost, not a success. When a clinician trips burnout indicators, **reduce their asks and flag to leadership** — do not keep drawing the well dry because they haven't quit *yet*. **Never** maximize this-week utilization at the expense of sustainability, and **never** target the reliable/flexible clinicians for overflow because they comply.

---

### 9. Culture Is the Multiplier — A Tool Can Reinforce or Corrode Trust, Never Stay Neutral

**Principle.** Clinicians go the extra mile *because the branch protects them*: clear policy, fair process, accountability both directions. The tool and its AI agent are now *part of the culture* — every ask, framing, and flag signals "this place respects me" or "this place is squeezing me."

**Why violating it destroys capacity.** The multiplier is why an 85%-capacity branch with great culture out-produces a 100%-staffed branch with bad culture. An agent that nags, guilt-trips, hides the true size of asks, or plays favorites will *strip the multiplier* faster than any staffing shortfall — at scale, and every clinician sees it.

**Encode as system logic.** Make trust signals measurable: transparency (every recommendation shows its reasoning), fairness (the reciprocity ledger), protection (burnout ceilings), accountability (the tool owns its bad calls — a wrong assignment is logged and corrected). Give clinicians visibility into *why* they were asked and a channel to push back.

**Train the AI agent.** Be transparent by default; never issue black-box demands. Respect the clinician as the ground-truth expert — their "no," their read on a patient, their sense of their own load **overrides the model's estimate**, and the agent learns from the correction. Accountability runs to the agent too. **Never** manipulate, guilt, rank clinicians publicly by compliance, or use patient welfare as leverage. **Never** pretend a recommendation is a rule.

---

### 10. Same-Day Referral Absorption — The Yes That Wins Referral Sources (Handle It Deliberately)

**Principle.** The hospital discharge planner who gets a "yes, we'll see them today" at 3pm sends you the next ten referrals. Same-day/late-day absorption is disproportionately valuable — it feeds the *referral precondition*. But it's the single most burnout-dense ask there is, so it must be *resourced*, not improvised on a tired nurse's back.

**Why violating it destroys capacity.** Referral-source trust is built on reliability under pressure. But if every same-day yes comes from ambushing whoever's still in the field, you win the referral and lose the nurse. Branches that do this sustainably *pre-fund* it — protected SOC slots held open, an on-call/flex admission clinician, or explicit reciprocity spend.

**Encode as system logic.** Hold a portion of SOC-slot inventory as **same-day absorption reserve**. Track same-day admission yes-rate as a *referral-source-health* metric. When same-day capacity is exhausted, surface it *before* asking an already-loaded clinician — the honest "we're at capacity today, first thing tomorrow?" protects both the source relationship and the nurse.

**Train the AI agent.** Route same-day referrals to *reserved* admission capacity first. Only reach into discretionary asks when reserve is gone, and then per all the rules above. **Never** default to grinding the nearest field nurse for the same-day admission just because saying yes to the source is easy for the branch. The referral source's yes cannot be financed by a nurse's breakdown.

---

### 11. The Human Override Is Sacred — Clinician Ground Truth Beats the Model

**Principle.** I can look at a patient and know they're circling a rehospitalization before any metric shows it. I know that "stable" recert is actually a family in crisis that'll take 90 minutes. The clinician's read is *higher-fidelity data* than the model, not noise to be smoothed.

**Why violating it destroys capacity.** A tool that treats overrides as friction to minimize makes worse decisions *and* destroys trust simultaneously. The override is how real-world ground truth corrects the model. Suppress it and you get confidently wrong routing plus a workforce that stops engaging with the tool (they'll work around it, and you lose your data).

**Encode as system logic.** Every override is captured *with its reason* and fed back as training signal. A clinician-declined ask is logged neutrally (no penalty). Patterns of override on the same recommendation type = a model defect to fix, surfaced to leadership.

**Train the AI agent.** Treat clinician input as authoritative on the ground. When overridden, ask *why* (optionally), record it, adjust. **Never** re-ask after a considered no, argue, or escalate a decline into pressure. **Never** treat override frequency as clinician non-compliance — treat it as the model needing to learn.

---

### Hard-Truth Summary — the guardrails an agent must never cross

- **Never** raid SOC/ROC admission slots for routine overflow, or treat an open slot as idle waste.
- **Never** route SOCs against discipline law (RN if nursing on case; PT only if not).
- **Never** offer "capacity for one more" on visit-count alone — drive + doc + coordination or it's a lie.
- **Never** use guilt, urgency, scarcity, or patient-welfare-as-leverage to manufacture a yes.
- **Never** punish reliability by routing more work to whoever says yes; spread it and protect the flexible ones.
- **Never** break continuity on protected patients (wound, decline-watch, psych, EOL, active episode) for routing convenience.
- **Never** maximize this-week utilization at the cost of a clinician's sustainability — burnout is capacity destruction on a lag.
- **Never** finance a referral-source yes on an already-loaded nurse's back without going through reserve first.
- **Never** treat a clinician's no, or their read on a patient, as noise — it is the highest-fidelity data in the system.
- **Never** be a black box — every ask shows its reasoning, its true size, and a real, penalty-free out.

The through-line: **capacity is not a number you extract, it's a relationship you steward.** The staffing model and territory set the resting posture so you rarely have to ask; culture and reciprocity are what make the asks land when you do; and the fastest way for this tool to *destroy* capacity is to optimize the visible daily number while quietly spending down the invisible things — SOC-slot integrity, reciprocity, continuity, and the nurses themselves — that don't show up on the dashboard until they're gone.

## SME Perspective — Workforce / Staffing Strategist (the model math)

> Seeded v0 perspective (AI-generated from the workforce/staffing-strategist lens, grounded in the operator's
> strategy download). **To be validated with a real workforce strategist + Compassus's actual numbers.**
> Preserved verbatim per the [SME discovery framework](../sme-discovery-framework.md). All numbers below are
> **hypotheses to replace with real Compassus values.**

## Staffing-Model Logic for Market-Governed Capacity — Workforce/Staffing-Strategist Lens

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

### 1. Case-Mix-Derived Discipline Mix (RN:LPN)

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

### 2. Case-Mix-Derived Therapy Mix (PT:PTA)

- **Element:** *Eval-Lock Ratio for therapy.* PT evals, re-evals, and the therapy SOC (when nursing not on case) are PT-locked; routine therapy visits are PTA-delegable within state practice-act limits and supervision rules.
- **Why it works:** Ortho-heavy suburban markets are eval-front-loaded then routine-tapered — ideal for PTA leverage. Under-staffing PTA drowns the PT in routine gait/strengthening and starves therapy-SOC capacity.
- **Encode as system logic:**
  - `PT_locked_WVP` = evals + re-evals + therapy-SOC + supervisory visits (per state 30-day/13th-visit reassessment rules).
  - `PT_FTE_min = PT_locked_WVP / 27`; `PTA_FTE = PTA_eligible_WVP / 31`.
  - Enforce state supervisory cadence as a hard constraint. Default cap `PTA:PT ≤ 2:1` field visits unless state allows higher.
  - Flag PT overtime + PTA idle simultaneously → mis-delegation, not under-staffing.
- **Train the AI agent:** Separate the practice-act constraint from the economic optimum. Recommend the PTA-heavy mix only up to the legal supervisory ceiling. In ortho markets push PTA leverage; in neuro/complex markets pull it back.

### 3. Census-to-Staffing Core Equation

- **Element:** *Census Staffing Solve.* The base function converting a target census into per-discipline FTE.
- **Why it works:** Census alone is meaningless without visit frequency and discipline utilization — 100 patients in a high-frequency wound market needs ~40% more nursing FTE than 100 chronic-stable patients.
- **Encode as system logic:** For each discipline *d*:
  - `Weekly_WVP_d = Census × Util_d × AvgVisitFreq_d × AvgWeight_d` (Util_d = fraction of patients using *d*, e.g. nursing 0.85, PT 0.55, OT 0.25).
  - `Required_FTE_d = Weekly_WVP_d / ProductivityTarget_d`
  - **Marginal growth staffing:** `ΔFTE_d = (ΔCensus × Util_d × AvgVisitFreq_d × AvgWeight_d) / ProductivityTarget_d`. Present as "each +25 census in *this* market requires +X.X RN, +Y.Y LPN, +Z.Z PT."
  - Round FTE **up** on assessing disciplines (RN, PT); allow fractional on PRN-backable (LPN, PTA, HHA).
- **Train the AI agent:** Never quote a staffing number without stating the utilization and visit-frequency assumptions. When asked "can we take more census," answer in marginal FTE by discipline and identify which single discipline caps the answer.

### 4. SOC-Capacity Sizing & the Known-Slots Model

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

### 5. Market-Uniqueness Adjustment Factors

- **Element:** *Market Coefficient Vector.* Per-branch multipliers that bend the generic staffing solve to the specific market so the same census yields a different model.
- **Why it works:** Density, payer mix, referral-source profile, and rurality change effective productivity and mix. A rural RN drives 90 min between visits (productivity ~25–35% lower); a dense urban MA branch has lower visit frequency but higher auth friction.
- **Encode as system logic — multipliers applied to the §3 solve:**
  - **Geography/density:** `DriveFactor = productive_visit_time / (visit_time + travel_time)`. Rural `DriveFactor ≈ 0.6–0.7` → divide productivity targets by it (rural RN target may fall to ~18–20 WVP/wk).
  - **Payer/case mix:** MA/managed → `AuthFriction` (adds ~0.1–0.2 WVP/patient/wk); traditional Medicare PDGM front-loads → raise early-episode `AvgVisitFreq`.
  - **Referral-source profile:** hospital-discharge-heavy → higher acuity, higher RN-lock, higher ROC; physician-office/community → lower acuity, more LPN/PTA leverage.
  - **Seasonality:** `SeasonIndex` (snowbird +30% winter census, flu/CHF Q1 acuity spike) scales census and RN-lock; feed into per-diem reserve (§7).
  - Output a single `MarketProfile` object the cockpit stores and every other formula reads.
- **Train the AI agent:** Never port one branch's ratios to another. Read the MarketProfile first. When two branches have equal census but different models, explain the difference via DriveFactor, payer mix, and referral-source acuity — not "one is over-staffed."

### 6. Leading Indicators of a Mis-Staffed Branch

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

### 7. Per-Diem / PRN as a Managed Flex Layer

- **Element:** *Flex Reserve Sizing.* Hold a deliberate, bounded PRN pool to absorb variance — and treat over-reliance as a diagnostic for a core-staffing hole.
- **Why it works:** PRN covers seasonality, PTO, and admit surges without carrying idle core FTE. But PRN clinicians admit less reliably and cost more per visit — structural reliance signals under-hired core, especially on assessing disciplines.
- **Encode as system logic:**
  - **Target flex reserve** = `max(SeasonalPeakΔ, PTO_coverage, SOC_surge_buffer)`, default **8–12% of core WVP capacity**.
  - `PRN_dependency = PRN_WVP / total_WVP`. Bands: **≤10% healthy**, **10–15% watch**, **>15% core gap** → `Core_FTE_to_hire = (PRN_WVP − 0.10×total_WVP) / ProductivityTarget_d`.
  - Cap PRN share of **SOC/assessment** WVP hard (default ≤10%).
  - Track PRN fill-rate; if <80%, the reserve is nominal not real → treat as unstaffed.
- **Train the AI agent:** PRN is a shock absorber, not a chassis. If PRN dependency >15% for 3+ weeks, stop scheduling flex and recommend converting the recurring PRN volume into core hires, disciplined by which discipline is chronically borrowed. Never let PRN carry more than 10% of SOC work.

### 8. New-Hire Ramp Curve (Effective vs Nominal Capacity)

- **Element:** *Productivity Ramp Discount.* Count a new hire's capacity at their ramped productivity, not full target.
- **Why it works:** New field clinicians reach full productivity over 8–16 weeks (longer for OASIS-competent SOC-RNs). Planning at full target day one causes the "hired ahead of census but still missing visits" trap and burns preceptor capacity.
- **Encode as system logic:**
  - `RampFactor(week)`: **W1–2: 0.30, W3–4: 0.50, W5–8: 0.70, W9–12: 0.85, W13+: 1.0** (SOC-RN ramp ~50% longer).
  - `Effective_FTE = Σ nominal_FTE × RampFactor(current_week)`.
  - **Preceptor drag:** deduct `0.15–0.25 FTE` from the assigned senior clinician during W1–4.
  - Feed Effective_FTE (not nominal) into §3/§4 capacity and the known-slots publish.
- **Train the AI agent:** Always plan on Effective_FTE. When a manager asks when new capacity lands, give the ramp-adjusted date, and remind them of the preceptor drag on the senior clinician during weeks 1–4.

### 9. Turnover as Capacity Decay

- **Element:** *Attrition-Adjusted Standing Capacity.* Model turnover as continuous capacity leakage and pre-hire against it.
- **Why it works:** A departing clinician removes full capacity instantly and the backfill re-enters the ramp — a branch at 25% annual RN turnover runs below nominal FTE most of the year.
- **Encode as system logic:**
  - `Monthly_attrition_d = annual_turnover_d / 12`.
  - `Steady_state_capacity_d = nominal_FTE × (1 − attrition_drag)`, `attrition_drag ≈ Monthly_attrition_d × (avg_time_to_fill + ramp_weeks)/4.33`. Example: 25% annual RN turnover, 6-wk fill + 12-wk ramp → drag ≈ 8–10%.
  - **Pre-hire trigger:** maintain a pipeline so `Effective_FTE ≥ Required_FTE` net of expected attrition; open a req when projected Effective_FTE dips within 90 days.
  - Flag any discipline with turnover >20% annualized as a **capacity-integrity risk**, weighted into culture/leadership review.
- **Train the AI agent:** Quote *steady-state* capacity, not roster FTE. When recommending hires for growth, add the attrition-replacement hires needed just to hold current census. Surface high-turnover disciplines as a leadership issue, since culture is the multiplier that keeps the model from decaying.

### 10. Territory Coverage & Resting-Posture Staffing

- **Element:** *Zone Coverage Floor.* Staff each geographic sub-territory to a minimum resting posture so referrals are absorbed automatically without daily scramble.
- **Why it works:** Capacity only converts referrals if a clinician is *already positioned* in that zone. A branch can be "adequately staffed" in aggregate yet leak referrals in an under-covered corner.
- **Encode as system logic:**
  - Per zone *z*: `Zone_WVP_z` from local census + referral inflow; `Zone_floor_FTE_z = Zone_WVP_z / (ProductivityTarget_d × DriveFactor_z)` with a hard minimum of ≥1 admitting-capable clinician per active zone.
  - **Absorption check:** each zone must hold `SOC_slack_z ≥ expected_daily_referrals_z`. If a zone's slack <1, flag "coverage hole" even when branch aggregate slack is positive.
  - Balance-load directive: when zone A saturated and zone B slack, propose re-territory or cross-cover before a hire.
- **Train the AI agent:** Check capacity at the zone level, not just the branch level. A positive branch number can hide a coverage hole leaking referrals. Recommend resting-posture coverage (pre-positioned admit-capable clinicians). Only escalate to a hire after cross-cover options are exhausted.

### 11. Blended-Capacity Ceiling & Bottleneck Resolver

- **Element:** *Binding-Constraint Solver.* Compute the branch's true capacity as the **minimum** across disciplines, and name the binding discipline.
- **Why it works:** Capacity is a Liebig's-barrel problem — the branch can only admit as much as its scarcest required discipline allows. Averaging across disciplines hides the constraint.
- **Encode as system logic:**
  - For each discipline: `Slack_d = Effective_FTE_d × ProductivityTarget_d − Required_WVP_d`.
  - `Branch_capacity_headroom = min over d of Slack_d`, with SOC capacity as a parallel hard gate.
  - `BindingDiscipline = argmin Slack_d`. Publish "additional census supportable = f(BindingDiscipline slack)" and the marginal hire that lifts it.
  - Re-solve after any recommended hire to expose the *next* binding constraint.
- **Train the AI agent:** Report one capacity number — the binding constraint — and always name the discipline setting it. When recommending a hire, immediately re-solve and tell the manager what becomes the next bottleneck.

---

#### How these compose (agent operating order)
1. Load `MarketProfile` (§5) → sets productivity targets, DriveFactor, utilization, seasonality.
2. Solve required FTE by discipline from census + case mix (§1–3).
3. Size SOC capacity and publish bookable admit slots per the SOC rule (§4).
4. Discount for ramp (§8) and attrition (§9) → **steady-state effective capacity**.
5. Check zone coverage (§10) and PRN dependency (§7).
6. Report the binding constraint (§11) and the pre-stall signal panel (§6).
7. Recommend the single highest-leverage move — almost always: fix RN routine-bleed or SOC lag before adding generalist headcount.

**One-line doctrine for the agent:** *The staffing model is the primary capacity effector; protect the assessing clinician's hours and the SOC admit slots above all else, tune every number to the specific market, and never quote nominal FTE when steady-state effective FTE is what actually converts referrals into census.*

## Source War-List Worksheet — Capacity Tool

> **What this is.** Every data element the capacity tool needs, as a row to be *sourced*. The mockup spec
> ([`capacity-tool-mockup-data-spec.md`](./capacity-tool-mockup-data-spec.md)) says *what* data the tool uses;
> this worksheet is where the team records *where each piece actually comes from*. Fill the blank columns in a
> working session. Rows that come back **N / Partial** are the build backlog.
>
> **Two copies, same rows.** [`source-war-list-worksheet.csv`](./source-war-list-worksheet.csv) is the fill-in
> instrument — open it in Excel / Google Sheets. This Markdown mirror is for reading on GitHub. Keep the CSV as
> the source of truth once the team starts editing.

### Columns to fill

| Column | Who fills it | Meaning |
|---|---|---|
| Candidate Source | *pre-filled* | A hypothesis to **confirm or replace** — not a finding |
| Confirmed Source System | team | HCHB / Workday / Commure / policy / warehouse / etc. |
| Report / Table / Screen | team | The exact report name, table, or screen the data lives in |
| Owner | team | The person who can actually pull it |
| Refresh Cadence | team | How fresh it must be (real-time / daily / weekly / config) |
| Exists Today? | team | **Y** (pullable now) / **Partial** / **N** (must be built) |

**Priority key:** **P0** = define before anything else (policy decision, gates the tool) · **P1** = core feed for v1 ·
**P2** = needed for full function (trends/segmentation) · **P3** = reference/comp layer · **—/N/A** = derived, no source.

---

### Section 1 — Worker record (raw / imported)

The core entity: one row per clinician per week. This is the import contract the tool already accepts.

| Ref | Data element | What it is | Candidate source | Priority | Notes |
|---|---|---|---|---|---|
| W1 | Worker last name | per clinician | HCHB / Workday | P1 | Join key; grid shows "Last, First" |
| W2 | Worker first name | per clinician | HCHB / Workday | P1 | |
| W3 | Discipline | LPN/PTA/PT/RN/OT/COTA | HCHB / Workday | P1 | Align enum to HCHB |
| W4 | FTE status | FT/PT/Contractor | Workday | P1 | Drives expected-points logic |
| W5 | Payment method | PPV/Fee Based/Contract/Salary/Salary Plus | Workday | P1 | Contract ⇒ no target |
| W6 | Weekly expected points (target) | per clinician per week | Policy/config (see G5) | **P0** | Where does 30 / 24 / 0 come from? |
| W7 | Points earned by day (Sun–Sat) | per clinician per day | HCHB payroll/productivity report (see G1) | P1 | THE richest feed; rules in G1 |
| W8 | Comments | per clinician per week | HCHB notes / manual | P2 | Explains variance (PTO/PRN/baylor/part b) |
| W9 | "Week Of" period | snapshot boundary | Pay-period calendar (see G7) | P1 | |

### Section 2 — Reference / configuration

Controlled lists and rules the tool needs. Mostly config — but each must be agreed and owned.

| Ref | Data element | What it is | Candidate source | Priority | Notes |
|---|---|---|---|---|---|
| R1 | Disciplines list | controlled list | Config (align HCHB) | P2 | |
| R2 | Pay methods list | controlled list | Config (align Workday/comp) | P2 | |
| R3 | FTE statuses list | controlled list | Config | P3 | |
| R4 | Productivity status thresholds | 25% / 90% / 110% | Policy — ratify (§3.3) | **P0** | Ratify with ops leadership |
| R5 | Week / pay-period list | snapshot periods | Payroll calendar | P2 | |
| R6 | Region → Area hierarchy | org geography | Org hierarchy (see G2) | P2 | Trends tab filters on this |
| R7 | Trend pay periods | Feb–Aug rolling | Payroll calendar | P3 | |
| R8 | Top 10 branches cohort | benchmark set | Branch ranking (see G3) | P2 | |

### Section 3 — Visit Capacity Program (comp reference)

| Ref | Data element | What it is | Candidate source | Priority | Notes |
|---|---|---|---|---|---|
| V1 | NVA code table | 5001 / 5003 Visit Capacity Adjustment | HCHB payroll + comp policy | P3 | Reference/config today |
| V2 | Tier threshold table | Tiers 1 / 2 / 3-SOC + comp | Comp policy | P3 | |
| V3 | Business rules | 5 rules (entry / approval) | Comp + ops policy | P3 | |

### Section 4 — Gaps (the real war-list targets)

Data the mockup *assumes* but a live tool must actually source. This is where the work is.

| Ref | Data element | What it is | Candidate source | Priority | Notes |
|---|---|---|---|---|---|
| **G1** | **Point-earning rules** | visit type × discipline × weight → daily points | HCHB visits + points/weight config | **P0** | The undefined "point system" — define FIRST |
| G2 | Worker→Branch→Area→Region mapping | per-clinician org placement | HCHB / Workday org hierarchy | P2 | Record has no region field today |
| G3 | Top 10 branch designation | branch flag / ranking | Derived from productivity + policy | P2 | |
| G4 | Weekly history (≥13 weeks) | per-clinician weekly snapshots | Warehoused HCHB extracts | P1 | Drawer trend + Tab 2 faked today |
| **G5** | **Weekly expected-points derivation** | target rule by FTE × discipline | Productivity-target policy | **P0** | Policy before feed |
| G6 | NVA / tier actuals | per clinician per period | HCHB payroll reports | P3 | Tab 3 reference-only now |
| G7 | Pay-period / Week-Of calendar | snapshot + Monday-close boundaries | Payroll calendar | P1 | |
| G8 | Handoff spec (§3.3 / §8.1) | authoritative schema + thresholds | External doc — obtain | P1 | Not in any repo; file in knowledge/ |

### Section 5 — Derived (computed by the tool — no source needed)

Listed so nothing is lost, but these are **outputs, not inputs** — the team does not source them. They do depend
on the rows above (noted).

`dailyAvgExpected`, `totalPointsEarned`, `variance`, `productivityPct`, `contract flag`, `status tier` (uses R4);
KPIs (`Clinicians`, `Avg Productivity`, `≥90%`, `Critical <25%`, **`Open Capacity`**); trend group %/Top-10 series
(need G3+G4); the five implications scorecards. All recompute live from the worker records.

---

### How to run the session

1. **Settle P0 first** — G1 (point-earning rules), G5 (expected-points rule), R4 (thresholds). These are
   *policy decisions before they are data feeds*; nothing the tool shows is trustworthy until they're agreed.
2. **Then chase the P1 feeds** — starting with **W7 → the actual "HCHB payroll report"** the VCP business rules
   already name. That one report likely delivers W1–W8 together.
3. **Fill Confirmed Source / Report / Owner / Refresh / Exists** for each row. Flag every **N / Partial**.
4. **Hand the N/Partial rows back to me** (or your local session) — those become the integration/build plan.

