# SOURCE — Current State Flow Map Revisions, 17 Aug 2026

> Verbatim text extraction of `8.17.26 Current State Flow Map Revisions.docx` — Google Drive
> `1NSHlkaWir6rc7mgZ1ONtwG-sIPsNFayV`. This is the **flow clarifying document**: flows one to four
> written out step by step with the refinements the redraw had to apply.
>
> **Held as source, not as truth.** The distilled, corrected current state lives in
> [`../process-facts-2026-08.md`](../process-facts-2026-08.md); the correction-by-correction history
> lives in [`../../artifacts/flow-map-redraw-assessment.md`](../../artifacts/flow-map-redraw-assessment.md).
> Where this file and those disagree, **those win** — this one records what was said on 17 Aug.

---

Flow One — Start of Care, Recert, ROC, and New Frequency Order
Trigger. A referral is received [T:20-21]. The same flow shape applies to recerts, ROCs, and new orders [T:240].
Where the flow actually begins. The map currently opens at the referral reaching the scheduler [T:21]. Two auth-team steps and one intake step sit upstream of that point, and adding them moves the first bottleneck earlier than the map currently shows [T:557-560].
Step sequence
Referral received. Intake, in Commure. [T:20-21]
Eligibility verification. Auth team. They verify the insurance and write a coordination note recording the insurance type and what auth will look like for this payer [T:557-558]. In Commure, eligibility is automated today [T:566].
Pending auth keyed. Auth team. They enter the number of pending auths the payer allows — some permit 1, some 3, some 5, some 10 [T:562, 569]. Traditional Medicare passes straight through; any other insurance routes to the auth team [T:561]. Not yet automated, though the allowance is knowable from the payer [T:568].
Return to intake for final approval. Completing the auth task generates a task back to intake, who final-approve the referral before it reaches scheduling [T:562, 566].
Referral enters the scheduling workflow. PCC. [T:22]
Readiness call. PCC. Standard procedure everywhere, though not universally performed [T:89-91]. The script confirms home health orders, sets an arrival window, and gathers logistics — pets, competing doctor's appointments [T:100-101]. Growth should have made first contact already, but in some markets does not, so the PCC's call becomes the patient's first contact with Compassus [T:97-98]. Script content varies by region: Washington/Providence requires safety screening questions — firearms in the home, others present, mental illness — instituted after a clinician was killed in a patient's home [T:106-109].
Scheduling grid maintained. PCC, in a spreadsheet outside HCHB [T:110]. Every pending patient is added, productivity tracked, and the number of referrals the branch can accept derived from it [T:114]. Updated manually several times a day so growth has visibility into what can be accepted [T:117].
Committed load computed and capacity assessed. PCC. These are HCHB reports, not workflows — they must be manually triggered and manually recombined [T:125, 129-130]. Branches pull several reports and retype them onto the scheduling grid [T:126]. One report carries roughly 20 columns; an Excel macro was built in the field to make it legible [T:126-127].
Discipline and specialty matched. HCHB. The clinician profile (PT vs PTA, RN vs LPN) filters the assignable list — PTs can do assessing visits, PTAs cannot [T:171-172]. Payer rules are enforced here too: some payers will not permit an SN visit and require an LPN visit [T:174]. This is filtering, not automation [T:172-173].
Patient rules and needs applied. PCC, via coordination notes and Point of Care visit alerts — POA on file, caregiver must be present, dialysis on Wednesdays [T:175-176]. The information is in the system, entered by a human [T:175].
Continuity of care applied. HCHB can surface who saw the patient last [T:178].
SOC visit assigned and scheduled, plus piggyback add-ons. PCC. If the referral orders nursing, PT, and OT, those three are the only visits schedulable at this point [T:154].
The evaluating clinician establishes the plan of care for their own discipline only. At the SOC visit the RN establishes the nursing plan of care and frequency — not the patient's whole plan of care. The clinician, not the scheduler and not QA, writes the frequency and creates the order for physician signature [T:156-158]. If the RN identifies a need beyond the referral, they also plot HHA frequency (which remains RN-managed) and/or the initial eval visit for MSW or ST. Disciplines already ordered on the referral — here PT and OT — establish their own plans of care and frequencies at their own eval visits, normally within 1-2 days of the SOC.
Clinician syncs; visits generate on the patient calendar and route to the scheduler [T:158].
Plan-of-care QA. DCS or a separate QA team depending on market [T:82, 84]. Reviews the calendar for correctness and confirms plan-of-care approval [T:83].
QA pushes to scheduling. PCC schedules the first week of visits, within the pending auth allowance [T:83, 27].
Assignment to clinician gated on auth. Visits are visible to the scheduler but cannot be assigned to a clinician until auth exists [T:158].
Steps 13 through 17 repeat once per discipline. Nursing at the SOC, then PT, OT, and any newly added discipline at their own evals. Each discipline's submission generates its own scheduler assignment task, and each discipline's plan of care functions independently as a subset of the overall plan — a social worker can request one more visit in the same week PT requests three [T:586-591].
Cycle repeats for additional visits. Beyond the pending auth allowance, more visits require completed visits and supporting documentation, which returns the case to the Authorization Cycle [T:28, 576].
Hard stops
Plan-of-care QA must clear before the first week of visits can be scheduled. If the QA team is behind, scheduling cannot proceed at all [T:82].
Plan-of-care approval must be obtained before moving forward [T:83].
Auth must exist before visits can be assigned to a clinician [T:158].
Where it breaks
QA backlog compresses care. An LPN waits on two visits, then three days' worth gets crammed into one instead of being spread as ordered [T:84].
Coordination cost shifts to the RN. Because the LPN cannot see the visits, the RN must hand off verbally what the system would otherwise have shown [T:87-88].
Per-discipline task explosion. The plan-of-care workflow fires once per discipline. Four disciplines produce four "complete requested schedule" tasks, then four more at approval — eight tasks for a decision already made [T:587-591].
Referrals stall invisibly upstream. "We know we have the referral, but it's just not in my workflow to schedule yet because it's stuck in auth" [T:560].
Refinements for the redraw
Add the upstream verification, pending-auth, and intake-final-approval sequence ahead of the scheduler's first step, and name the "stuck in auth" wait as a bottleneck [T:560]. Recolor PCC in-system workflow steps to yellow. Annotate the plan-of-care task with "×4 disciplines" [T:590].
Need to add DCS workflows and Auth Process
Review Ower of task Corrections:
The PCC Completes Clinician Scheduling Workflow should be Yellow based on legend(currently purple)
The Green Patient rules should be purple as even though that comes from patient, it is in the system as a coordination note technically.
The Missed visit mapping is not correct(also remove unworked label so it just lists missed visit).  When clinician documents a missed visit, scheduler receives workflow to notify MD within 48 hours.  If MD not notified in that timeline, workflow is created for DCS.
The bottom -Right portion of the flow map needs revisioning in addition to missed visit flow—enunciating visits as scheduled, missed, completed and also detailing the clinician piece of the worklow as part of scheduling each visit with option for reassigning, accepting, rescheduling, missing, or declining.
Auth workflow map:
Verification ocures in Commure before scheduling and starting the referral workflow.  Any insurance besides medicare requires it to go through pending auth to note how many visits are authorized.  Branch has to wait for intake after auth is provided.
After SOC, only need to submit re-auth if POC goes beyond what is authorized.  Authorized routine visits only get scheduled in HCHB for clinician to see.
If additional orders are written—DCS has to approve via workflow, additional auth is needed.
Flow Two — Routine Visit Scheduling
Trigger. Admission to home health services. Routine visits are first plotted by the evaluating clinician at the SOC or eval visit — not by the scheduler.
Character. This flow has two phases that are best drawn separately, since drawing them together is what makes it hard to follow:
Phase One — Frequency plotting and initial assignment. A burst of scheduler workflow, one task per discipline, concentrated in the first few days after admission.
Phase Two — Steady-state clinician self-management. No scheduler workflow at all, unless a visit must be reassigned to a different clinician.
The most important structural fact here: the scheduler's involvement in routine visits is front-loaded and then effectively ends. The recurring work is done by the assigned clinician.
Phase One — Frequency plotting and initial assignment
1. The evaluating clinician plots their own discipline's frequency.
Taking the common case where SN, PT, and OT are ordered on the referral: the RN performs the SOC visit and establishes the plan of care for nursing, beyond the RN SOC visit already scheduled. The admitting RN decides nursing frequency — for example 1x/week for 1 week (to add an additional visit within the current Medicare week), then 2w3, then 1w2 — entirely dependent on patient need.
The admitting RN does not plot visits for the other disciplines already ordered on the referral. PT and OT plot their own.
2. Exception — additional services identified at the SOC.
If the admitting RN determines the patient needs a service beyond what was referred (MSW, ST, HHA), the RN plots that too:
HHA — the RN plots aide frequency, and aide visits remain RN-managed.
MSW or ST — the RN plots the initial eval visit only. That clinician then goes out, evaluates, and develops their own discipline plan of care and frequency.
3. Submitted nursing frequency generates a scheduler assignment task.
The plotted frequencies create a workflow task for the scheduler to assign the subsequent visits to the RN or LPN care team member who will be following the patient.
4. PT and OT evaluate, normally within 1-2 days of the RN SOC visit.
Each plots and submits visit frequencies for their own discipline — for example PT 1w3, 2w3, 1w1 and OT 1w4.
5. Each discipline's submission generates its own scheduler assignment task.
Every time a discipline submits frequencies, the scheduler receives a separate task to assign those visits to the assigned care team. This is the per-discipline task explosion seen from the routine-visit side [T:587-591].
6. After the 485 is submitted, further orders are add-on or subsequent orders.
Any new order within the plan of care is an add-on / subsequent order. If it includes a change to visit frequency, it generates additional scheduler workflow. Add-on orders also route through DCS approval and, where applicable, auth before returning to the scheduler [T:584].
Phase Two — Steady-state clinician self-management
Once the initial assignment burst is complete, no additional scheduler workflow is required unless a visit needs to be reassigned to a different clinician.
Within steady state the assigned clinician may move any non-OASIS visit within the Medicare week (Sunday through Saturday) to suit their own needs and the patient's — provided the date they move it to does not fall outside the certification period, 60 days from SOC.
So for a routine visit already plotted for the week, the process actually starts with the assigned clinician, and runs roughly:
Evaluate own capacity for the week.
Prioritize against the clinical needs of the other patients on their schedule.
Look for geographic grouping opportunities — can these patients be seen together.
Test that grouping against hard scheduling requirements that cannot move:
strict wound care timing
catheter schedules
IV timing
patient preferences, and competing appointments both inside home health (other disciplines) and outside it (MD follow-ups, dialysis)
Confirm with the patient — the day-before confirmation call [T:85].
Route — HCHB recommends a route; the clinician may use it or not, and typically adjusts for patient-imposed time windows [T:334-335].
Boundaries governing clinician self-management
OASIS visits are not freely movable. Only non-OASIS visits shift at clinician discretion.
The Medicare week is Sunday through Saturday. Movement is within the week.
The certification period is 60 days from SOC. A visit cannot be moved past it.
Auth still gates assignment. See the Authorization Cycle.
Where it breaks
Reassignment is the only recurring scheduler trigger — and the clinician cannot do it themselves. An RN cannot reassign a visit to her own LPN, or flip a plotted RN visit to an LPN, without routing it back to the scheduler [T:370-373]. These are the most common reassign workflow tasks the scheduler receives [T:474-476]. This is an HCHB restriction, not a Medicare requirement, and most EMRs do not impose it [T:372]. Because steady state otherwise requires no scheduler workflow, removing this one restriction removes essentially all recurring scheduler involvement in routine visits.
Supervisors cannot see supervisee schedules. An RN cannot see her LPN's schedule, a PT cannot see the PTA's, an RN case manager cannot see the aide's — while remaining responsible for supervising them [T:378-379]. This directly undercuts Phase Two, since the clinician managing aide frequency cannot see the aide's calendar. Cited as one of the biggest dissatisfiers for JV clinicians who came from systems that allowed it [T:377].
The Phase One task burst is overhead. Four disciplines submitting frequencies produce four separate assignment tasks for a care team decision that could have been made once at referral.
Confirmation calls are unpaid evening work. Clinicians make next-day confirmation calls from home, on Sunday evenings, in pajama time or by clocking out early or by dropping the last visit of the day [T:412-415]. Patients do not answer, or call back at 9pm [T:413].
Newer clinicians lack the schedule-negotiation skill. They allow patients and caregivers to dictate timing more than they should, which makes them over-accommodating and pushes cost onto the rest of the team [T:387-390]. Getting the first visit of the day at 8 or 9am is described as the single largest lever on individual capacity [T:391-393].
The weekly planning logic is undocumented and unassisted. Everything in Phase Two steps 1 through 4 — capacity, clinical prioritization, geographic grouping, hard-constraint checking — happens in the clinician's head with no system support and no visibility to anyone else.
Discipline-role mismatch persists. PTs retain routine visits that PTAs should take, which both costs more per visit and consumes the PT capacity needed for starts [T:479-483].
Refinements for the redraw
Draw Phase One and Phase Two as separate segments; the current map implies a continuous scheduler-driven loop.
Annotate each discipline's frequency submission as its own scheduler assignment task, and show that they arrive staggered — nursing at SOC, PT and OT 1-2 days later.
Show the 485 as a boundary marker: before it, the initial plan of care; after it, add-on / subsequent orders.
Mark reassignment as the only steady-state scheduler trigger, so it is visually obvious that this is the one thing pulling the scheduler back in.
Show the RN as the manager of aide frequency — a supervision relationship the current map does not represent.
Design implication
The target-state value here concentrates in two changes already agreed as decisions. Care team at referral collapses the Phase One task burst: if the team is established once, each discipline's frequency submission can assign automatically to the known care team member instead of generating a task. Clinician reassignment authority removes the only recurring scheduler trigger in Phase Two. Together they would take routine visit scheduling from four-plus scheduler tasks per admission plus ongoing reassignment traffic to approximately zero.
Flow Three — Authorization Cycle
Trigger. Any payer other than traditional Medicare [T:561]; and thereafter any request for visits beyond the current allowance [T:575].
Step sequence
Verification and eligibility. Auth team, upstream of scheduling [T:557].
Payer requirements recorded. A coordination note describes the insurance type and what auth will look like [T:558]. Since an initiative launched early the prior year, the auth team is asked to add a template snippet of what the clinician needs to know about that payer [T:449-450].
Pending auth keyed. Count set by payer — 1, 3, 5, or 10 [T:569]. Pending auth means: see the patient, submit documentation, and the actual auth follows [T:570].
First week scheduled within the pending allowance. [T:27]
Additional visits requested. Clinician writes the order, DCS approves, workflow generates to the auth team, auth team submits to the payer [T:461].
Urgent auth request. When the visit is imminent and auth has not returned, the scheduler files an urgent request. The auth team has usually already submitted it and is behind [T:462].
Pending-auth or non-billable decision. Some payers permit use of pending auth; some do not. Where they do not, a leader decides whether to see the patient as a non-billable visit [T:463-464].
Actual auth issued. The payer supplies an authorization number and pending auths convert to real auth [T:575].
Where it breaks
Most auth pain is self-inflicted. Plans of care are written without regard to payer limits, and the frustration arrives at week three [T:445, 456]. "UHC was never going to give you more auth. We're not creating our plans of care based on the insurance" [T:445]. The payer information already exists in a coordination note the clinician is supposed to reference [T:450].
Pending-auth visits are invisible. They do not appear on the clinician's calendar, the patient cannot be told when the next visit is, leaders cannot see them, and the system does not count them toward productivity [T:29, 43-44]. The scheduler holds them "in their head or on a sticky note." "If you can't see it, you can't plan" [T:44].
A visit surfaces with one day's notice. "All of a sudden it shows up for Friday and it's Thursday" [T:31].
Workflow noise trains schedulers to ignore it. HCHB generates a pending-auth workflow every single day per patient, and any auth-screen change generates another scheduler workflow [T:33-34]. Roughly 50 a day. The scheduler has already scheduled everything schedulable, so the task carries no action — and bulk-clearing becomes habit, including the one that mattered [T:34-35].
The root cause is architectural. HCHB was built when the business was roughly 90% traditional Medicare, where this was not an issue; the workflow was never rebuilt for a majority managed-care book [T:35-36].
The auth team is structurally under water. "There's never enough people. They're always behind" [T:459].
A false constraint circulates. Schedulers believe they cannot request additional auth until the day before or day of. That is not true — it reflects a misunderstanding of the system [T:460].
The loop only closes when more visits are needed than were authorized. If 12 were ordered and 5 granted, the cycle re-fires at visit 5 [T:575-576].
Payer behavior established in session
UHC — 5 nursing visits; 4 of the 5 must be completed with documentation supporting need before visit 6 [T:443, 468].
Indiana Medicaid — pays 30 days from the hospital discharge date, not the admit date, so a five-day gap consumes five days of the benefit [T:446]. Nursing effectively unlimited within the window; 8 visits total shared across PT, OT, and ST [T:453-454].
Ohio Medicaid — cited as a case where the discharge date is knowable 30 days out and capacity can be projected accordingly [T:137].
Some payers grant one auth at a time, which caps the week regardless of ordered frequency [T:468].
Additional notes for Auth workflow map:
Verification ocures in Commure before scheduling and starting the referral workflow.  Any insurance besides medicare requires it to go through pending auth to note how many visits are authorized.  Branch has to wait for intake after auth is provided.
After SOC, only need to submit re-auth if POC goes beyond what is authorized.  Authorized routine visits only get scheduled in HCHB for clinician to see.
If additional orders are written—DCS has to approve via workflow, additional auth is needed.
Flow Four — Exception and Recovery
Missed visit
Clinician disposition. At a scheduled visit the clinician may accept, reassign, reschedule, miss, or decline [T:216-218]. Reassignment may be RN to LPN, PT to PTA, or PTA back to PT if a reassessment turns out to be required [T:217].
Sync required for visibility. Because HCHB is delivered over Citrix, the back office cannot see anything about a visit until the clinician syncs — only that it was started, or is incomplete [T:209-210].
Sync delay creates false state. A Tuesday visit may be performed and not synced until Friday, so it reads as undocumented [T:210]. A started visit usually means the patient was seen, but not always — a visit where the clinician called 911 is not a visit [T:211].
Missed visit routes to the scheduler, who determines whether the MD was notified. 48 hours is a Medicare requirement and an HCHB hard stop [T:224].
If notification is not documented, workflow generates to the DCS [T:225].
Sequence refinement for the map: visit scheduled → documentation pending → missed, rather than treating "delivered" as the trigger [T:212-213].
Clinician decline
HCHB visit dispatching, part of smart scheduling, recommends the next best assignee but does not auto-assign, deliberately — a last-minute visit should not land on someone without a conversation [T:510-511]. The capability exists and is not enabled; it returns to the scheduler for approval [T:514].
Declines are genuinely hard to resolve. The clinician is at productivity and cannot be compelled, and the scheduler had not planned to find anyone else [T:515-516].
Shift Finder exists in HCHB and is not turned on. It lets clinicians view uncovered visits with a patient snapshot and distance, and accept one; acceptance generates a back-office approval task [T:346-347].
Call-out recovery
There is no established process [T:202].
Scheduler checks who has availability and whether any PRN is willing to work [T:203].
Scheduler escalates to the clinical manager; everyone stops what they are doing, including workflow [T:203].
The team reviews patients chart by chart to determine who can safely move to tomorrow and who must be seen today — labs due, ortho, IV, wound [T:193-194, 203].
The scheduler is non-clinical and cannot make that call, so either the clinical manager is pulled in or it takes a long time [T:192, 504-506].
Clinicians are called and asked to pick up more, on the strength of relationships [T:204].
If nothing else works, the DCS goes and sees the patients [T:204].
Patients who cannot be covered are called and rescheduled — ideally early in the day, not at the end [T:521-522].
Where it breaks:
It cascades. Visits pushed to the next day compress that day, and the nurse may still be out [T:195]. "The goal should be to not affect capacity of Thursday and Friday based on something that the nurse falls out on" [T:196].
Clinicians have stopped calling in for backup visits because they do not trust the branch to respond efficiently — either they will be sent far away, or it will take two hours by which time their own schedule is fixed. So they absorb the gap and take one less patient [T:197-198].
A daily huddle absorbs the residue. Every afternoon the DCS, clinical managers, and schedulers review all next-day starts against the reports; it can run an hour or more [T:551-552].
LUPA watch
If a clinician returns a visit as missed and the system detects LUPA exposure, HCHB alerts the scheduler [T:233].
The alert is only partly retrospective. A Tuesday miss still leaves Wednesday, Thursday, and Friday to make it up; a miss because the patient is in the hospital is a different case [T:235].
The scheduler notifies the leader, who decides whether to add frequency, coach the clinician, or retry the next day [T:236].
Separately, the DCS is responsible for running a LUPA report out of Pulse daily [T:230, 237]. Compliance is inconsistent — "supposed to" [T:230].
Observations across all four flows
Coordination notes function as a substitute for missing workflow. "We've utilized coordination notes as a workaround because we don't have workflow in the system. So we're like, well, let's create a coord note, and that generates a task" [T:186].
They are less fragile than they first appear. Notes are titled and routed: a scheduler-titled note creates a scheduler task, and a Point of Care visit alert forces the clinician to view it before opening the visit [T:183-185]. There are hundreds when viewed from the back office, but they are not an undifferentiated pile [T:185].
Reports, not workflows, carry most capacity information. Committed load, productivity, and LUPA exposure all live in reports that must be manually triggered and manually recombined [T:125-130, 230].
Productivity data cannot be a daily batch. It changes every time the scheduler works a piece of workflow; a once-a-day load to a dashboard will not support the decisions being made off it [T:307-308].
Per diem and contract capacity is the least visible and most underused. Full-time status drives point expectations (0.5, 0.6, 0.7, 0.8 → 30, 28, 26, 20, 12 points) and is held in the HCHB worker profile [T:139-140]. Contract clinicians are paid regardless and should be filled first, then full-time, then part-time [T:145-146]. Per diem availability fluctuates weekly and lives nowhere in the system [T:135]. Branches that decline to use per diem staff at all forfeit their ability to grow [T:144-145].
What this record does not yet cover
Recert, ROC, and new-order variations. Treated as one trigger class with SOC [T:240]. Any material differences in the QA or auth path per trigger type are unrecorded.
Aide, social work, and speech therapy paths. Referenced only as additional disciplines multiplying the plan-of-care task [T:586-587]. Not separately traced.
Weekend and after-hours scheduling. Touched only in passing — large branches run close to 24/7, smaller branches struggle with weekends [T:321-323].
Future state. Explicitly out of time in session: "I don't think we've got time to do that necessarily right now, but we should definitely think through how does this process change" [T:546-547].