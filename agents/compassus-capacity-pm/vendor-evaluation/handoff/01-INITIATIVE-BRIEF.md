# 01 · The initiative

What Compassus is buying, why, and what it already knows. This is the whole of what you know about
the project. Do not extend it. Where a fact is quoted, it is the project's own wording.

---

## 1. The problem in one paragraph

Compassus is a home health provider running roughly eighty branches, about three thousand
clinicians and about three hundred schedulers. The initiative exists to make *"finite,
geographically-distributed clinical capacity reliably meet variable, time-sensitive demand — without
harming patients, clinicians, quality, or margin."* The system of record is **Home Care Home Base
(HCHB)**: the plan of care, orders, authorization state, scheduling workflow and visit record all
live there, it is not real-time, and its clinician app requires a manual sync. A platform that
cannot read and write HCHB either duplicates that data or asks schedulers to work two systems, which
is the cost this initiative exists to remove.

## 2. The findings the team has already reached

These are settled. A vendor who understands them is worth more than one who does not; a vendor who
contradicts them without noticing has not read our problem.

1. **The scheduling problem is not a scheduling problem.** Schedulers spend most of their day on
   administrative workflow inside HCHB. The real inefficiencies are upstream: documentation delays,
   the DCS review bottleneck, authorization holds and fragmented capacity management. *"Scheduling
   gets blamed because it is the final visible touchpoint."*
2. **Capacity and scheduling are different functions.** *"Capacity is a planning function — what the
   branch can absorb. Scheduling is an execution function — who goes where, when."* Today both run
   through one manually maintained spreadsheet grid, so neither is done well. **Capacity must be
   solved first.**
3. **The scheduler is an administrator.** *"The only true scheduling decision a scheduler makes is
   the start-of-care intake call."* Clinicians plot their own visits; the scheduler assigns a name to
   pre-plotted blocks, processes missed-visit tasks, and clears fifty to sixty authorization
   notifications a day, almost none actionable.
4. **Clinicians run their own week.** They call patients the evening before, confirm or reschedule,
   and accept their slate each morning. In steady state *"there is no scheduler workflow at all
   unless a visit must be reassigned."* Many chose home health for exactly this control.
5. **Pending-authorization work is invisible.** *"A visit that has been ordered but not authorized
   exists in no view."* It is carried in the scheduler's head or on a sticky note. This is *"the
   clearest capacity-measurement defect in the current state."*
6. **Notification storms breed bulk-clearing.** HCHB regenerates a pending-auth task every day per
   patient. The design rule that came out of it: **notify on state change, never on state
   persistence.**
7. **The Alabama pilot failed on change management, not technology.** HCHB's Smart Scheduling was
   constrained to mirror the manual process, clinicians rejected machine assignment, leadership let
   them, and *"the system was never allowed to do what it was designed to do."*
8. **A higher score can be a worse fit.** The product that rates highest on the team's functional
   scorecard also overreaches the automation posture on sixteen variables. *"That is the Alabama
   failure expressed as a number."*
9. **Route optimisation as a cost lever is dead here.** About seventy percent of clinicians are paid
   per visit, so mileage saved does not become money saved the way the standard pitch assumes.
10. **Vendors overclaim optimisation gains.** Field-service evidence puts the honest ceiling at five
    to fifteen percent travel reduction. *"Vendors claim 20–40%. Divide by two to three."* There is no
    peer-reviewed evaluation of any home health scheduling product; every case study is one site with
    no control.
11. **The first job of the product is measurement, not optimisation.** *"The MVP does not build the
    schedule … it is to make capacity measurable and observable."* Several of the initiative's own
    primary metrics do not exist as a live number today.
12. **The decision of record is caution.** The adversarial review of the business case concluded:
    *"Do not fund a platform purchase now. Fund a two-quarter measurement and configuration phase, and
    set gates."* Licensing is about ten percent of three-year cost of ownership.

## 3. The target state, in the project's words

- **Three modules:** Capacity Management, Scheduling Engine, Patient Engagement. Capacity is Phase 1,
  and *"Phase 1 is visualization only — no automation in the first release."*
- **The capacity tool replaces the scheduling grid.** *"They are the same object; do not build both."*
- **Care team assigned at referral, not per visit.** The system recommends the full team; a human
  approves or edits.
- **The tool recommends; the human accepts.** *"Clinicians supply their own availability windows and
  preferences. The system does not drop work onto a calendar unilaterally."*
- **Discipline-role match defaults to the paraprofessional** (LPN, PTA, COTA) with explicit opt-out.
  Assessing clinicians (RN, PT, OT, SLP) are the scarce, capacity-governing resource.
- **A human scheduling role survives at reduced scale** for urgency, local knowledge and
  relationship-based coverage.

## 4. The three arenas

The questionnaire's Overview tab and Section B are built on these. The 41 elements inside them are in
`02-QUESTIONNAIRE.md` and `spec-elements.json`.

| Arena | Kicker | Definition |
|---|---|---|
| Capacity Management | The envelope | How much work a branch can deliver, and how much room is left |
| Scheduling Engine | Filling the envelope | Which clinician, which day, which route |
| Engagement | Making it happen | Turning a schedule into delivered visits, with patients, clinicians and the office |

*"Capacity sets the envelope; scheduling and engagement are both performed against it."*

The Engagement ambition is the one furthest ahead of the market: outreach *"carried by the platform
itself — agentic voice, text and email — rather than queued up for a coordinator to work,"* with
staff *"able to see it, intervene, override, and take any conversation back."* The team's own market
read: the top candidates understand capacity and scheduling; *"few have thought through patient
engagement."*

## 5. Automation posture: Read, Assist, Control

The team has already decided, variable by variable, how far software may go. The ladder the
scorecard's Sophistication scale uses is the same one.

| Rung | Name | Meaning |
|---|---|---|
| 4 | Runs it | Decides across the whole picture, and re-decides when things change (Control) |
| 3 | Recommends it | Works out the answer and proposes it; a person confirms (Assist) |
| 2 | Checks it | Applies rules and flags problems; a person still works it |
| 1 | Shows it | Surfaces the information; a person does all the work (Read) |
| 0 | Not addressed | |

*"A 4 is not automatically good. Where Compassus set an Assist boundary, a product that decides on
its own is an overreach to flag, not a bonus."* Assignment, coverage and the week are Assist. The
margin and LUPA consequences are Read: *"it may never enter an objective function or weigh against
clinical need."*

## 6. Reimbursement mechanics a serious vendor knows

- **PDGM pays per 30-day period.** Two payment periods sit inside one 60-day certification period,
  each with its own case-mix group. *"A system that models only the certification period cannot see
  the payment cliff it is walking toward."*
- **LUPA is a floor and a cliff.** Below a group-specific visit threshold (two to six visits) the
  period is paid per visit. The guard should sit above the floor, not at it, and the alert must carry
  the remaining days and the visits still needed. **Never by padding clinically unnecessary visits.**
- **There is also a ceiling.** Above threshold, every further visit is cost with no matching revenue.
- **Three ceilings, never conflated:** authorization is permission, LUPA is the floor, utilisation
  management is the ceiling. A visit can be authorised and still be uneconomic.
- **Compassus is majority non-traditional Medicare** and HCHB's workflow was built for a
  ninety-percent Medicare book. That is the root of most authorization friction.
- **Compliance windows pre-consume capacity:** SOC within 48 hours of referral; ROC within 48 hours
  of discharge; 48-hour physician notification on a missed visit; the recert window at days 56–60;
  PT 30-day reassessment; 14-day aide supervisory visit. OASIS visits are date-bound and cannot be
  freely moved. The Medicare week runs Sunday to Saturday.
- **The clinician originates frequency.** *"No tool should generate frequency independently."*

## 7. Constraints a vendor must respect

- **HCHB's own limits.** Clinicians cannot reassign their own visits. Supervisors cannot see
  supervisee schedules. Documentation is invisible until sync. Clinicians see seven days of schedule.
  Once a clinician accepts a visit for the day, *"the back office cannot remove it from their device
  to reassign it."* HCHB has no public API; the documented path is HL7v2 and CCD over SFTP, and its
  self-serve partner marketplace with FHIR APIs is not due until 2027. It also sells a competing
  optimizer.
- **Consent.** Text and email need signed consent, captured at the SOC visit, so automated reminder
  flows cannot begin before it. Some powers of attorney require the patient not be contacted at all.
- **State rules.** California treats any call not manually triggered by a human as a robocall.
  Washington requires safety screening questions on firearms and others present in the home. Buddy
  codes apply in Ohio and California. Local geography matters: a bridge in Jacksonville divides one
  zip code and takes an hour to cross.
- **Labor.** Incentive schemes need union approval where a union exists; salaried and hourly
  populations cannot be incentivised per visit. Incentive holdout is a known risk: if surge pay
  becomes a pattern, clinicians learn to wait for the higher offer.
- **Privacy.** Aggregates and operational signals; minimum-necessary data; no PHI beyond what a task
  requires.

## 8. Cultural traps the tool cannot fix but must not ignore

- **Machine-assigned visits get rejected where human-assigned ones would not.** This is *"the
  central adoption constraint."*
- **Latent capacity is being lost to a trust deficit.** Clinicians have stopped calling in for backup
  visits because response is slow. The fix is speed before it is any feature.
- **Making decline too easy helps no one.** Route a decline back to the clinician to call, rather
  than simply cancelling.
- **Never give a patient a time; give a range.** A wound vac coming off turns a thirty-minute visit
  into ninety.
- **Discretionary effort is real capacity, but borrowed.** It must be repaid or it disappears. Never
  manipulate: no guilt, urgency or scarcity leverage. A *no* is data.
- **Never be a black box.** *"Every ask shows its reasoning, its true size, and a real, penalty-free
  out."*

## 9. Vocabulary

| Term | Meaning |
|---|---|
| HCHB | Home Care Home Base, the EMR and system of record. Its clinician app is Point Care. |
| SOC / ROC | Start of care; resumption of care after hospitalisation. Both carry 48-hour rails. RN performs the SOC whenever nursing is on the referral. |
| Recert | Renewing the plan of care at the end of a 60-day certification period; window is days 56–60. |
| DCS | Director of Clinical Services. Reviews and approves plan-of-care documentation before it reaches scheduling. |
| ED | Branch Executive Director. Growth and margin lens. |
| POC / 485 | The physician-signed plan of care and its document. |
| Auth / pending auth | Payer authorization for a number of visits; a visit ordered but not yet authorised is *pending* and is not universally payable. |
| PDGM | Patient-Driven Groupings Model. Fixed case-mix payment per 30-day period. 432 groups. |
| LUPA | Low Utilization Payment Adjustment. The per-visit floor; a cliff, not a gradient. |
| OASIS | The date-bound assessment. Its visits cannot be freely moved. |
| HHVBP | Home Health Value-Based Purchasing; cohort-relative quality scoring. |
| The envelope | What a branch can deliver. Committed load against it is what is scheduled; open room is what is left. |
| Committed load / open room | Points or visits already scheduled; the remainder, by day, week, discipline and territory. |
| Visit points | The shared currency of capacity: SOC 2.5, recert 1.75, eval 1.5, reassessment 1.25, discharge 1.75, routine 1.0. The system is under-defined and the team knows it. |
| Assessing vs assistant | RN, PT, OT, SLP versus LPN, PTA, COTA. Assistants exist to absorb routine visits so assessing clinicians stay free for what only they can do. |
| Routine bleed | An assessing clinician doing routine visits while assistant capacity sits open. |
| The overload cycle | Full of routine visits, no room for SOCs, no new patients, no growth, no added capacity, still overloaded. |
| Front-loading | Pacing visits early against the plan of care; the tool's gold standard is about 42% of the week's target by Tuesday. |
| Resting posture | Territory set so a caseload is geographically coherent and a nearby referral is absorbed almost automatically. |
| Float pool / per diem | Clinicians with no territory on purpose; the targeted capacity instrument for SOCs or coverage. |
| The five dispositions | Chosen the day before, in HCHB: Accept, Reschedule, Reassign, Miss, Decline. |
| Rapid reschedule / Shift Finder / Visit dispatching | HCHB capabilities that are configured off or not enabled. Dispatching recommends and does not auto-assign. |
| Readiness gauntlet | Everything upstream of a schedulable visit: DCS review, pending auth, POC lock, face-to-face or coding hold. |
| Posture overreach | A product driving what we said it may only assist or read. |
| Gating variable | A hard or structural constraint that is in the MVP: a product that cannot do it is disqualified however well it scores elsewhere. |
| The flare button | One action on a call-out that triages affected patients by priority and recommends nearby clinicians. |
| Point Care, Commure, NestMed, Pulse, Workday, Circadia | The clinician app; new intake platform; real-time documentation; utilisation review; HR and PTO (integration to HCHB exists but is not activated); AI patient calling used in some California locations. |

## 10. What is deliberately not known

The team has named its own gaps. A vendor cannot be marked down for our blind spots, and a vendor
who fills one has told us something.

- No defined point system beyond one operator's confirmed weights; no definition of an *open slot*.
- No verified payer-rule library; three entries, all from conversation rather than contract.
- No baseline for the initiative's core metric, quantified capacity and utilisation.
- No position on Electronic Visit Verification.
- Weekend and after-hours scheduling, aide and social-work paths, and hospice mechanics not yet
  mapped.
- Whether batch-triggered calls in California are robocalls: a legal question, still open.
