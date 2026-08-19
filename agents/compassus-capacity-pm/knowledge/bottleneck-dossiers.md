# Bottleneck Dossiers — the twelve, ranked by leverage

> **Source:** `8.17.26 Bottleneck Identification.docx` — Google Drive `1X-KEBygDws3VR5aA97C2G7FRPtbw2vub`,
> folder `1RPI1ogTdyDeEf64OBRmaRQ0ESNWp5k5o`. Rendered faithfully.
> `[T:###]` citations resolve against [`source/transcript-lines-2026-08-13.txt`](./source/transcript-lines-2026-08-13.txt).
> `CN-##` refers to [`constraint-register.md`](./constraint-register.md).
>
> **Ordering.** By **leverage** — the product of how much capacity the bottleneck consumes and how
> tractable it is. **The first four are the ones worth solving first.**
>
> **On missing numbers.** Where a dossier says impact is not quantified, that is deliberate. The
> session produced very few hard numbers, and inventing them would undermine the business case rather
> than support it. Each dossier names **what to measure** instead.

| # | Bottleneck | Why here |
|---:|---|---|
| 1 | The authorization cycle | Largest structural consumer, and most of it is self-inflicted — which makes it unusually tractable |
| 2 | Pending-auth invisibility | The clearest capacity-measurement defect. Prerequisite to measuring anything else honestly |
| 3 | DCS QA and order approval | A hard stop on care delivery, half of which is a toggle we already control |
| 4 | Per-discipline task duplication | Pure clerical waste with a design pattern already agreed |
| 5 | Territory and service area management | |
| 6 | Discipline-role match | |
| 7 | Call-out recovery | |
| 8 | Clinician confirmation calls | |
| 9 | The readiness call | |
| 10 | Workflow noise | |
| 11 | Per diem and contract capacity | |
| 12 | POA identification | |

---

## 1. The Authorization Cycle

**Mechanism.** Any referral other than traditional Medicare routes to the auth team for eligibility
verification and pending-auth keying **before scheduling ever sees it**, then back to intake for final
approval `[T:557-562]`. The pending-auth count — 1, 3, 5 or 10 depending on payer — caps how many
visits can be scheduled `[T:569]`. Beyond that allowance, each additional block of visits requires the
clinician to write an order, the DCS to approve it, workflow to generate to the auth team, and the auth
team to submit to the payer `[T:461]`. When the visit is imminent and auth has not returned, the
scheduler files an urgent request against a queue that is already behind `[T:462]`. Where the payer
will not pay against pending auth, a leader decides whether to see the patient non-billable `[T:463-464]`.

**The reframe that matters.** *Most of the pain is self-inflicted.* Plans of care are written without
regard to payer limits, and the frustration arrives at week three. *"UHC was never going to give you
more auth. We're not creating our plans of care based on the insurance"* `[T:445]`. The payer
information **already exists** — the auth team writes it into a coordination note at verification, and
has been asked to include a template snippet of what the clinician needs to know since an initiative
launched early the prior year `[T:449-450]`. Nobody reads it at the moment it would matter.

**Compounding factors.** The auth team is structurally under-resourced — *"there's never enough people,
they're always behind"* `[T:459]`. A false constraint circulates among schedulers, that auth cannot be
requested until the day before or day of, which reflects a misunderstanding of the system rather than a
rule `[T:460]`. And the root cause is architectural: HCHB was built when the business was roughly **90%
traditional Medicare**, where none of this mattered, and the workflow was never rebuilt for a majority
managed-care book `[T:35-36]`.

**Downstream effects.** Referrals stall before entering the scheduling queue at all — *"we know we have
the referral, but it's just not in my workflow to schedule yet because it's stuck in auth"* `[T:560]`.
Frequency gets plotted that cannot be delivered. And the patient-care cost is real: plans of care end in
abrupt discharge, sometimes without a final visit, because nobody planned against the actual visit
budget. *"You're not approaching the visits in the way that you would if you knew that next week was
your last visit"* `[T:452-453]`.

**What to measure.** Days from referral receipt to entry in the scheduling queue, split by payer class ·
percentage of plotted visits that were authorized · urgent auth request volume · non-billable visits
authorized by exception · abrupt-discharge rate.

**Candidate remedies.** Surface payer rules at plan-of-care creation — **highest value, lowest
complexity, and the data is already being captured**. Automate pending-auth keying from the payer rather
than having a person enter a knowable number `[T:568]`. Correct the day-before misconception through
training. Make pending visits visible (dossier 2). Continue the auth-side automation already underway
`[T:459]`.

**Constraints.** CN-12 … CN-17, CN-22, CN-33.

**Open questions.** Which payers permit use of pending auth, and whether that list is maintained
anywhere authoritative · whether Commure can key pending auth end to end without human touch · **what
the auth team's actual queue time is — nobody in the session knew.**

## 2. Pending-Auth Invisibility

**Mechanism.** A visit that has been ordered but not authorized **exists in no view**. Not on the
clinician's calendar, not visible to leaders, cannot be communicated to the patient, and does not count
toward productivity. The scheduler carries it in her head or on a sticky note `[T:43-44]`.

**Evidence.** *"Leaders can't see it. Maybe the scheduler has it in their head or on a sticky note that
others pending auth… But if you can't see it, you can't plan"* `[T:44]`.

**Downstream effects.** Clinicians forget pending visits exist, because they have grown used to working
from their calendar — *"a lot of times clinicians will forget they even have that visit that's pending"*
`[T:30]`. Then it lands with a day's notice: *"all of a sudden it shows up for Friday and it's
Thursday"* `[T:31]`. The patient is left wondering when the next visit is and nobody calls `[T:32]`.
Capacity reads falsely light, because uncounted work is invisible work. And the knowledge is **personal
rather than institutional** — when a single-scheduler branch loses its scheduler for a day, nobody knows
what was in her head `[T:56]`.

**Impact.** The clearest capacity-measurement defect in the current state, and arguably the sentence
that captures the whole initiative: **if you can't see it, you can't plan.**

**What to measure.** Count and age of pending-auth visits by branch · percentage of visits assigned to a
clinician with less than 48 hours' notice · variance between reported capacity and delivered capacity.

**Candidate remedies.** Represent a pending visit as a **first-class object**: visible on the clinician's
calendar, attributable to a clinician, counted as committed load, and clearly marked as awaiting auth.
The session noted another system might show the visit to the clinician flagged as pending rather than
hiding it — they could see it and simply not open it `[T:43]`.

**Constraints.** CN-22.

**Open question.** Whether counting pending visits toward productivity creates a **payroll or
expectation problem**. Needs a finance and HR view before it is designed.

## 3. DCS QA and Order Approval Backlog

**Mechanism.** Two distinct things the conversation ran together, **and separating them matters**.

- **Plan-of-care QA is a hard stop.** SOC, recert and ROC plans must clear a review workflow before
  visits reach scheduling. Depending on market this is the DCS or a separate QA team. Laci's read is
  that this one **cannot** be turned off `[T:81-84]`.
- **Physician order approval is a toggle.** Every order routes to a DCS for approval. An HCHB
  configuration, not a Medicare requirement, and not done at other agencies `[T:58, 61-63]`.

**Evidence.** *"So we've been seeing the patient for six weeks and I need an order to add three more
visits. And the DCS has 50 of them to approve, and they're behind"* `[T:429-430]`. On the
product-versus-regulation distinction: *"that is something that is a Home Care Home Base restraint,
because when they built the system, it was, we're going to be compliant"* `[T:61]`.

**Downstream effects.** An LPN waits on two visits, and then three days' worth get crammed into one
instead of spread as ordered `[T:84]`. The clinician, having plotted visits with the patient at the SOC,
cannot see those visits and cannot make the confirmation call until QA clears `[T:85-87]`. The RN
absorbs coordination the system would otherwise have shown, because the LPN cannot see the visits
`[T:87-88]`. And the DCS spends the day pushing workflow instead of managing utilisation and team
performance `[T:436]`.

**What to measure.** QA queue depth and age · hours from plan-of-care submission to scheduling release ·
order-approval queue depth · DCS time on workflow versus time on management.

**Candidate remedies.** For **plan-of-care QA**, the hard stop stays — the opportunity is throughput and
queue visibility, not removal. For **order approval**, three options were raised: turn it off outright;
turn it off selectively for clinicians with a demonstrated record of writing good orders, so the reward
for quality is autonomy `[T:437-438]`; or have AI adjudicate the black-and-white cases and escalate the
gray ones `[T:62-63]`. The retained benefit of approval is utilisation oversight, better served by
reviewing utilisation reports than by clicking every order.

**Constraints.** CN-07, CN-18.

**Open questions.** Whether the plan-of-care review requirement is **regulatory or an HCHB structural
constraint** — this changes whether it is permanent · what the company's risk appetite is on order
approval · whether selective per-clinician toggling is actually configurable in HCHB.

## 4. Per-Discipline Task Duplication and Care Team Assignment

**Mechanism.** The plan-of-care workflow fires once per discipline. Four disciplines produce four
"complete requested schedule" tasks, and four more when the plans of care are approved — **eight tasks
for a care team decision that was effectively already made** `[T:587-591]`. Each discipline's plan of
care also operates independently as a subset of the overall plan, so a social worker requesting one
visit and PT requesting three arrive as separate events in the same week `[T:586]`.

Meanwhile **the care team is already knowable at referral**. Today the scheduler does assign a care
team — the COTA, the LPN, the aide, the OT who cover that area get added to the patient's care team when
the referral arrives `[T:326-327]`. The tasks exist anyway.

**Evidence.** *"I've got 8 tasks for every discipline just because the QA team and the DCS have pushed
their workflow"* `[T:591]`. And the remedy stated directly: *"once you create that care team, I don't
need a task every time a new discipline gets pushed through. We've already established, we've already
approved that that is your OT and that's your COTA"* `[T:589]`.

**Downstream effects.** Eight tasks per admission of clerical clicking. The same absence generates the
most common reassign workflow tasks the scheduler receives `[T:474-476]`.

**Candidate remedies.** Establish the care team **once at referral**, with a system recommendation and
human approve-or-edit, and thereafter route each discipline's frequency submission automatically to the
established team member. The session's caveat is important and should be **designed for rather than
around**: the team does change mid-episode — the COTA goes on PTO, a call-out happens, or the patient
turns out to be a catheter patient who requests female clinicians only `[T:329-330]`. The recommendation
is a starting point the branch can override, because they may know something the system does not.

**What to measure.** Tasks per admission · scheduler minutes per admission · reassign task volume.

**Constraints.** CN-26, CN-24.

**Open questions.** What triggers a care-team re-recommendation mid-episode, and who approves the change.

## 5. Territory and Service Area Management

**Mechanism.** **There is no data behind territory design.** Territories are hand-coloured paper maps and
zip-code spreadsheets. A referral arriving in a zip requires someone to look up which PTA covers that
area `[T:165]`.

**Evidence.** *"Territory assignment and how poorly it's done in the industry because there's no data
behind it. Whereas we have the data, we just don't make it visible to the branches to make the
decisions"* `[T:161]`. On why territories go stale: re-colouring a map takes such effort that when
patient distribution shifts three months later, nobody re-cuts it `[T:169]`.

**Downstream effects.** Capacity work starts **after** the visit has landed rather than before —
*"capacity starts with visits landing where they should land before someone even has to think about
it"* `[T:166]`. No designated backup clinician per zip `[T:167]`. Cross-branch coverage requires
referencing a spreadsheet `[T:167-168]`. Growth cannot see where referrals are actually landing, which
is described as pivotal for them `[T:164]`. The failure mode is concrete: one territory carried ~30
patients across a full-time RN and a full-time LPN, while LPNs in the adjacent area were drowning and
starts were being declined `[T:297-298]`.

**Local knowledge the system must encode.** Same-zip is not the same territory. In **Jacksonville** a
bridge divides one zip code and crossing takes an hour `[T:416-417]`. In **California** an interstate
cannot be crossed during certain hours, so clinicians work one side or the other `[T:418]`.

**What to measure.** Mileage per visit · visits per clinician per day · census by zip by discipline ·
referral distribution against clinician distribution · percentage of visits performed outside the
assigned territory.

**Candidate remedies.** **Virtualise territory**: a live census and referral heat map by zip and
discipline, hoverable to show census and discipline mix `[T:424-425]`. Primary and backup clinician per
zip, with auto-assignment on zip match `[T:167]`. Make territory shifts **cheap** so they happen when
distribution changes rather than never. Serve growth and scheduling from the same view with role-based
profiles `[T:425-427]`.

**Constraints.** CN-42, CN-49.

**Open questions.** Whether territory lives in the capacity tool or in Commure — the session leaned
toward the capacity tool with visibility for growth `[T:423-425]` · data source for zip geometry and
drive time.

## 6. Discipline-Role Match

**Mechanism.** PTs retain routine visits that PTAs could perform. HCHB filters the assignable list by
profile but **does not push work down**. Today correcting it requires a human to make each change
`[T:492]`.

**Evidence.** *"If you're a PT, you're doing starts, recerts, reassessments, ROCs — things that a PTA
can't do. If it's a routine visit, we shouldn't be paying PTs to do routine visits. Our PTA should be
full first"* `[T:479-481]`.

**Downstream effects.** **Two costs simultaneously**: a higher-paid clinician performing a routine visit,
and PT capacity consumed so that starts cannot be accepted. *"That's where we have issues in areas where
we can't get growth because your PTs or your RNs are full doing routine visits. They don't have the
ability to do additional starts"* `[T:483]`.

**What to measure.** Percentage of routine therapy visits performed by PT versus PTA · cost per visit by
discipline · declined starts attributable to PT or RN saturation. *Note: the analogy raised in session —
senior technicians performing work juniors could do, with a large annual saving — is illustrative of the
pattern only and **is not a Compassus figure*** `[T:490-491]`.

**Candidate remedies.** Default assignment to the paraprofessional with **explicit opt-out**, so the
change happens without depending on a leader to make it: *"the default though, it's like they have to opt
out versus opt in to it"* `[T:493]`. Legitimate exceptions must be capturable — a specific diagnosis, a
required reassessment, or a patient request `[T:482]`.

**Constraints.** CN-45, CN-08.

**Open question, and it is a real one.** **Paraprofessional supply.** LPNs are getting harder to hire,
and some areas do not have a workable paraprofessional-to-clinician ratio `[T:486-487]`. Pushing work
down assumes there is someone to push it to. **Check market by market before the default is switched on.**

## 7. Call-Out Recovery

**Mechanism.** **There is no established process** `[T:202]`. The scheduler checks who has availability
and whether any PRN is willing to work, escalates to the clinical manager, and everyone stops what they
are doing — including workflow. The team then reviews patients chart by chart to determine who can safely
move to tomorrow and who must be seen today. Clinicians are called and asked to pick up more. If nothing
else works, the DCS goes and sees the patients `[T:203-204]`.

**Evidence.** *"We're stopping workflow. We're stopping what we're doing. And we have to review these
patients"* `[T:203]`. The triage criteria are **clinical** — labs due today, ortho, IV, wound — and the
scheduler is **not clinical**, so either the clinical manager is pulled in or it takes a long time
`[T:193-194, 192]`.

**Downstream effects.** **It cascades.** Visits pushed to the next day compress that day, and the nurse
may still be out `[T:195]`. *"The goal should be to not affect capacity of Thursday and Friday based on
something that the nurse falls out on"* `[T:196]`. Worse, clinicians have stopped calling in for backup
visits at all, because they do not trust the branch to respond efficiently — either they get sent far
away or it takes two hours, by which point their own schedule is fixed. So they absorb the gap and take
one less patient `[T:197-198]`. And the daily afternoon huddle exists partly to absorb the residue,
running up to an hour every day `[T:551-552]`.

**What to measure.** Uncovered visits per week · percentage covered same day versus pushed · next-day
schedule compression · time from call-out notification to full coverage · visits lost outright.

**Candidate remedies.** The **"flare button"** — one action that triages the affected patients by
clinical priority and recommends nearby available clinicians. *"Nurse called out, press the button, and
let AI in the background sort of prioritize the visits based off of, like, start of care of course have
to get done that day, this is a wound visit"* `[T:191-192]`. It needs diagnosis-level attributes filtered
to the scheduler **with clinical sign-off retained** `[T:504-506]`. Ping several clinicians at once with
first-to-accept, optionally with an incentive attached `[T:520]`. Notify the patient **early in the day**
rather than at the end `[T:521-522]`.

**Constraints.** CN-41, CN-48, CN-21.

**Open questions.** What the escalation timeout should be before the patient must be called — the
session raised the case where three sequential declines put it at 2pm before anyone realises the patient
may not be seen `[T:518]` · whether Pulse can supply the clinical attributes triage needs.

## 8. Clinician Confirmation Calls

**Mechanism.** Each clinician calls their own patients to confirm the following day's visits, typically
in the evening or on Sunday night, **off the clock**.

**Evidence.** *"I hated having to talk to my PTA on a Sunday evening, trying to map out the first day of
the week. My wife dreads making those phone calls at the end of the day to schedule. She hates it. She's
in a bad mood"* `[T:412]`. Patients do not answer, or call back at 9pm `[T:413]`.

**Downstream effects.** Unpaid work, and a genuine work-life-balance cost. Some clinicians **drop the
last visit of the day** to make time for the calls, which is direct capacity loss `[T:415]`. And because
a home health appointment does not feel official the way a doctor's appointment does, no-shows follow:
*"with home health, it doesn't feel official"* `[T:397]`.

**What to measure.** The session's own framing was roughly **3,000 home health clinicians at roughly 30
minutes a day** `[T:413-414]`. **Both figures were estimates offered in conversation and should be
established by survey before they are used in a business case.** Also measure no-show rate and visits
dropped to make time for calls.

**Candidate remedies.** Automated confirmation by text or voice, giving an **arrival range and never a
hard time** — *"don't ever give them a time, give them a time range, because I could go in to the patient
and their wound vac came off, and I'm going to spend an hour and a half in there"* `[T:398]`. Email
confirmation to make it feel official `[T:397]`. Four touchpoints rather than one `[T:404]`. Let the
clinician add context to the outbound message so it is individualised `[T:401-402]`.

**The caution worth designing around.** If accepting or declining is made too easy, patients will decline
visits a clinician would have talked them into. *"If you make it way too easy to not accept, then you're
not helping the clinician at all… I don't feel like doing physical therapy today. I could have gotten
that patient to agree to that"* `[T:402-403]`. Suggested handling: **route a decline back to the
clinician to call** rather than simply cancelling.

**Constraints.** CN-09, CN-10, CN-44.

**Open questions.** Consent timing — reminders cannot begin until consents are signed at the SOC ·
fallback path for patients without a cell phone `[T:401]`.

## 9. The Readiness Call

**Mechanism.** The PCC calls the patient to confirm home health orders, set an arrival window, and gather
logistics — pets, competing appointments. Growth is meant to have made first contact already. Standard
procedure everywhere; **inconsistently performed** `[T:89-101]`.

**Evidence and the harm case.** The clearest consequence given in session: a clinician shifted two visits
to her PTA to make room for an SOC, nobody had confirmed the patient was home, the patient was still in
the hospital, and she lost half a day with no visits to recover — *"her income is affected because the
branch didn't confirm that that patient was home"* `[T:93-95]`.

**Why it gets skipped.** Schedulers cite lack of time, and the same branches carry 50 pending referrals
unscheduled `[T:104]`. Calls made too late in the day get no callback, and roughly half of patients do
not answer `[T:105]`. At least one scheduler declines the call outright, reasoning that discharge
confirmation is growth's job `[T:90-91]`.

**What to measure.** Readiness call completion rate by branch · SOC visits where the patient was not
home · clinician productivity lost to failed SOC visits.

**Candidate remedies.** Automate as **voice AI plus text** — flagged in session as clear low-hanging
fruit, on the grounds that the calls are not clinically difficult `[T:101-103]`. **Precedent already
exists inside Compassus**: Circadia was doing this in Orange County before the integration, with work
underway to turn it back on in California, and Kera is another `[T:102-103]`. **Worth reviewing what
already runs before buying.**

**Constraints.** CN-31, CN-32, CN-37, CN-09, CN-10.

**Open questions.** Whether a patient's first contact with Compassus should be a voice agent — raised as
a genuine judgment call, not a technical one `[T:106]` · how regional script variance is handled,
including the Washington safety questions · robocall treatment of batch-triggered calls.

## 10. Workflow Noise

**Mechanism.** HCHB generates a pending-auth workflow **every single day per patient**, and any change to
the auth screen generates another scheduler workflow. Roughly 50 a day. Almost none carry an available
action, because the scheduler has already scheduled everything schedulable `[T:33-34]`.

**Evidence.** *"The scheduler gets it and there's nothing additional to schedule. I've already scheduled
out the five pending auth. I know we're waiting on more pending auth. I don't need this workflow, but
it's how it's coded in"* `[T:34]`.

**Downstream effect, which is behavioural rather than temporal.** Bulk-clearing becomes habit, and the
one item that did carry an action goes with the rest. *"They get passive about it too… You just go in and
clear it. You go and clear it, but then maybe there actually could be something in there. There could
be"* `[T:34]`.

**What to measure.** Notifications per scheduler per day · percentage cleared without action ·
time-to-clear distribution.

**Candidate remedies.** **Notify on state change, never on state persistence.** Digest rather than
per-item. Separate actionable from informational so that clearing one does not train indifference to the
other. *This is a design rule more than a project.*

**Constraints.** CN-23, CN-39.

## 11. Per Diem and Contract Capacity

**Mechanism.** Full-time status drives point expectations and is held in the HCHB worker profile — **0.5,
0.6, 0.7, 0.8 mapping to 30, 28, 26, 20 and 12 points** `[T:139-140]`. Contract clinicians are paid
regardless of volume and should therefore be filled first, then full-time, then part-time `[T:145-146]`.
**Per-diem availability fluctuates weekly and lives nowhere in any system** — the scheduler holds it
`[T:135]`.

**Evidence.** *"There needs to be an interface that allows the branch to — the scheduler probably is the
keeper of all that knowledge — to be able to on a weekly basis modify that as their per diem staff
provide availability, as that fluctuates"* `[T:135]`.

**Downstream effects.** Per-diem capacity is invisible to planning. Branches that decline to use per-diem
staff at all — because they are hard to manage and track — **forfeit their ability to grow**, since they
must burden full-time clinicians until a new full-time position is justified `[T:143-145]`. And filling
contractors by taking visits from full-time staff means the contractor was not needed in the first place
`[T:146-147]`.

**The upside stated plainly.** Per-diem staff *"can be your biggest weapon against capacity if you use
that workforce appropriately"* `[T:144]`.

**What to measure.** Per-diem utilisation · percentage of per-diem clinicians active in the last 30 days
· contract fill rate against full-time utilisation · declined referrals in branches with no per-diem pool.

**Candidate remedies.** A **weekly availability interface** maintained by the per-diem clinician or the
scheduler `[T:135-136]`. Encode the fill order, with a check that the contractor is genuinely additive.
Capture **soft capacity** — the fluctuating amount an individual clinician is actually willing to do,
above or below the formal expectation `[T:133-134]`. Per-point clinicians who want 40 rather than 30
should show as available headroom, which the growth team currently cannot see `[T:277-278]`.

**Constraints.** CN-35, CN-36, CN-47.

**Open questions.** Whether Workday or the HRIS can supply status and rate class · per-diem contract
terms vary by branch, so minimum-utilisation expectations are not uniform.

## 12. POA Identification

**Mechanism.** Where an active POA exists, the POA must sign admission consents. POA status may be on the
referral, may surface on the welcome call, or **may not be discovered until the clinician is at the door**
`[T:494-500]`.

**Evidence.** *"If we have to get the POA to actually sign our admission consents before we go see the
patient, we're wasting start of care visits… It may take us a couple days to get a hold of the POA, but
we need to know right from the beginning"* `[T:495-496]`.

**Downstream effects.** Wasted SOC visits. Days lost obtaining consent. **Service failures when the wrong
party is contacted** — sometimes the person answering is not the POA, and information has been disclosed
to someone who should not have received it `[T:502]`. Sequencing failures where nursing and PT understood
the arrangement and OT did not `[T:502]`. Some POAs specify that the patient not be called at all
`[T:500]`.

**What to measure.** SOC visits delayed or wasted for POA reasons · days from referral to consent
signature where a POA exists.

**Candidate remedies.** Flag POA **at referral in Commure** and carry the flag to the front of the
scheduling and capacity view `[T:497, 501]`. Ask the question on the automated welcome call `[T:501]`.
Send DocuSign to the POA where they cannot be present `[T:497]`.

**Constraints.** CN-11.

**Open questions.** Whether growth can reliably capture POA status at referral · whether Commure has a
field for it today.

---

## Also raised, not yet dossiered

Four items came up with enough substance to record but not enough detail to work up.

| Item | Why it matters | Evidence |
|---|---|---|
| **Staffing models and paraprofessional supply** | Identified as the biggest issue in a number of markets, particularly for paraprofessionals, and specifically LPNs performing functional roles. **This constrains the discipline-role-match remedy and deserves its own analysis.** | `[T:484-487]` |
| **Clinical timing and Pulse integration** | The mechanism by which clinical attributes — wound, wound vac, IV, timing requirements — reach a non-clinical scheduler for call-out triage, filtered appropriately and with the clinical decision retained by a clinician | `[T:503-506]` |
| **Coordination support** | The broader question of what AI could do across the coordination traffic between the office and clinicians; the session flagged it as substantial space and did not open it | `[T:509]` |
| **Coordination notes as a workflow substitute** | Recorded in the current-state document rather than here, because the session's conclusion was that they are better structured than they appear — titled, routed, and in the case of Point of Care visit alerts, enforced. **The design instruction is to replicate the routing behaviour, not the note-as-workflow pattern.** | `[T:180-186]` |
