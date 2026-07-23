# HH Scheduling Discovery Session — Compassus

> **Source:** Google Drive — "HH Scheduling Discovery Session" (Compassus capacity & scheduling initiative).
> Full-day cross-functional discovery (scheduling operations leaders, clinical staff, technology/data analysts)
> mapping the home health scheduling process from referral intake through clinician–patient visit execution.
> Rendered here faithfully as the agent's primary ground truth. Do not paraphrase away the specifics.

## Executive Summary

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

## 1. What Schedulers Actually Do

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

## 2. The End-to-End Workflow Chain

Many sequential handoffs must occur before a scheduler can act on a single patient. For a three-discipline
patient (Nursing, PT, OT), **7+ separate workflow tasks** are generated — each requiring the scheduler to
open, review, and act or close.

### Start of Care → Scheduler Assignment

| Step | Owner | Action |
|---|---|---|
| 1 | Clinician | Completes start-of-care visit; syncs documentation from point-of-care device |
| 2 | DCS | Receives workflow; completes 4-task checklist: plan-of-care review, calendar accuracy check, pending auth management, plan-of-care lock |
| 3 | Auth Team | Adds authorization for non-Medicare payers (Medicare auto-authorizes) |
| 4 | Scheduler | Receives "Complete Requested Schedule – Week 1" task; assigns clinician to plotted visits for next 7–10 days |
| 5 | Scheduler | Once plan of care locked, receives recertification task; schedules full episode (30–60 days), checking Medicare compliance requirements |

### The Authorization Notification Problem

Schedulers receive **50–60 pending authorization notifications per day**. The majority are non-actionable —
triggered every time the auth team updates an authorization field, even if the actual authorized visits
haven't changed. Schedulers must open each one individually to determine if any action is required.
**This is widely cited as the most frustrating aspect of the scheduler's daily workflow.**

## 3. Capacity Management vs. Scheduling

> **Critical Distinction.** Capacity management and scheduling are two distinct problem statements.
> **Capacity management must be solved first** — it is the foundation on which any scheduling optimization
> tool must be built. Running Smart Scheduling without it is why prior attempts failed.

### Capacity Management (Currently Manual)

Leaders currently manage capacity through experience, Excel spreadsheets, and scheduling grids. Key inputs
that must be tracked:

- **Census per territory/zip code** — roughly **40–50 patients per full-time RN+LPN team pair**
- **Referral pipeline** — what is coming, from which partners, with what payer mix
- **Clinician FTE, PTO, and specialty** (wound care, IV, lymphedema, etc.)
- **Utilization rates via Pulse** — whether visit frequencies are over- or under-plotted
- **Start-of-care pipeline** — how many are expected each day or week

None of these inputs currently feed into a single system. They exist across **HCHB, Pulse, Workday, Excel
grids, and individual manager knowledge.**

### Why Smart Scheduling Failed

A prior pilot of HCHB's Smart Scheduling feature in Alabama failed **not because the technology was flawed**, but because:

- Leaders constrained the system to mirror existing manual processes — locking clinicians to specific zip codes, refusing to allow autonomous assignment decisions
- When the system tried to optimize (e.g., assigning a slightly out-of-territory nurse who had availability), clinicians rejected the assignment
- Leadership allowed the resistance, effectively pulling the smart logic out of Smart Scheduling
- The system was never allowed to do what it was designed to do — **it was never truly piloted**

## 4. Clinician Dynamics & Buy-In Challenges

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

## 5. Technology Landscape & Integration Points

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

## 6. Patient Engagement Opportunity

Explored replacing the physical patient admission calendar with a digital interface (via QR code) providing:

- Visit time ranges (not exact times) for upcoming weeks
- Real-time notifications when schedule changes occur
- Ability for patients/caregivers to flag conflicts and request reschedules
- Caregiver visibility — particularly valuable for out-of-state family (e.g., Florida JV patients)

> Note: The physical calendar remains a **Medicare Conditions of Participation** requirement and must be
> maintained in the home. A digital interface would supplement, not replace, it.

## Next Steps (from the session)

1. **Vendor Evaluation** — Continue with 6–7 scheduling/capacity vendors (MedArrive, Circadia, Aria Health, others). Develop a shared requirements list covering both capacity forecasting and scheduling optimization before next vendor meetings.
2. **Pilot Site Selection** — Target a new integration or brand-new branch go-live as the first pilot. Consider a pay-per-visit office (Providence, Ohio Health, BSMH) for clinician buy-in testing where existing habits won't conflict with new tooling.
3. **Scheduler Pain Point Session** — Focused session with schedulers: biggest pain points, wish-list items, what would make their job easier. Observe end-of-day workflow.
4. **Capacity Management Scoping** — Define all demand-side inputs (census by territory, referral pipeline, new orders, pending auth, planned discharges) and capacity-side inputs (FTE, PTO, specialties, zip-code coverage) needed to build a capacity forecasting model.
5. **Commure Scheduling Grid View** — Add a scheduling-grid-style view within Commure (below referral tasks) showing pending referrals with payer, expected discharge date, discipline ordered, and status — to replace Excel scheduling grids.
6. **Workday ↔ HCHB Integration** — Activate the existing interface so approved PTO in Workday automatically creates unavailability in HCHB. Eliminates manual entry, prevents scenarios like 5 of 7 nurses approved off the same day.
7. **NestMed Face-to-Face Module** — Evaluate routing referral documents from Commure to NestMed for automated face-to-face validation. Reduces downstream coding discrepancies that create POC holds.
8. **Patient Engagement Interface** — Explore a QR-code patient scheduling portal (time ranges, reschedule requests, caregiver visibility).
9. **Steerco Email Update** — Michael to finalize stakeholder email (positive reception callout; groups covered: referral coordinators, growth, insurance ops, operations; add due-dates column).

## Processes Identified

### Process 1 — Start of Care Workflow (Per Discipline)
Triggered when a new patient is admitted. For a three-discipline patient (Nursing, PT, OT), it runs three times in parallel and generates 7+ scheduler tasks total.

1. Intake schedules initial visit → Clinician completes SOC → Syncs documentation from device
2. DCS receives workflow → 4-task checklist: POC review, calendar accuracy, pending auth management, POC lock
3. Auth team adds auth for non-Medicare payers (Medicare auto-authorized)
4. Scheduler receives "Complete Requested Schedule – Week 1" → Assigns clinician to pre-plotted visits for next 7–10 days
5. Once POC locked/approved: Scheduler receives "Start of Care Recertification" task → Schedules full 30–60 day episode, verifying Medicare compliance: 30-day reassessments, HHA supervisory visits every 14 days, buddy codes, discharge/recert visit codes

> **Medicare Compliance Note.** Schedulers must verify: (1) 30-day therapy reassessments plotted within window,
> (2) HHA supervisory visits every 14 days, (3) each discipline ends in a discharge, recertification, or
> reassessment visit — not a routine visit. Missing these has billing and compliance consequences.

### Process 2 — Ongoing Visit Management
Runs continuously through the episode as needs evolve.

- **New Order:** Clinician calls physician → verbal order → enters order in HCHB → goes to DCS for approval (cannot bypass) → scheduler receives task → assigns additional visits
- **Authorization (Off) Notifications:** 50–60/day, majority non-actionable; must open each to check if additional visits can now be scheduled; triggered on any auth-screen update
- **Missed Visit Workflow:** Clinician syncs missed visit → scheduler notified → must notify MD within 48 hours (Medicare) → documents → determines reschedule; if a 30-day reassessment is involved, verify next visit maintains compliance window
- **Other Visit Actions:** Declined / reassigned / rescheduled — clinician-triggered on device at sync; scheduler handles resulting coordination notes and system tasks

### Process 3 — Clinician Daily Scheduling
Largely independent of the back-office scheduler.

- Evening before: reviews 7-day rolling calendar; calls patients to confirm or reschedule for next day
- Reassigns/reschedules/notes missed visits — synced to HCHB on next sync
- Morning of: long-presses device to bulk-accept all visits for the day
- Throughout the day: adjusts as needed — pulls forward visits if others cancel, handles urgent PRN needs, coordinates via coordination notes

> **Important Constraint.** Once a clinician accepts a visit for the day in HCHB, **the back office cannot
> remove it from their device to reassign it.** This is a hard system stop. All same-day changes require
> direct phone coordination between scheduler and clinician.

### Process 4 — Capacity Management (Current Manual State)
Managed via leader experience, Excel scheduling grids, and HCHB reports — no single system view.

- Track census per territory/zip — target ~40–50 patients per full-time RN+LPN team pair at **30 pts/week productivity minimum**
- Monitor referral pipeline from grid or Commure to anticipate incoming SOC volume
- Review utilization via Pulse — adjust visit frequency if teams over-plotted
- DCS leadership holds weekly cross-approval PTO meetings to prevent all clinicians being off simultaneously
- Scheduling grid (Excel) tracks pending referrals, expected discharge dates, payer mix, discipline ordered, available SOC slots per day — manually updated in parallel with HCHB

> Once teams trust Commure, the Excel scheduling grids will likely become redundant — Commure holds the same
> information in a more accessible, up-to-date form.

## Appendix — Key Terms

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
