# The Day-Before Confirmation Protocol — operator specification, capture 1

> **What this is.** The operator's stated design for the **patient engagement protocol that confirms
> tomorrow's visits** — the third module of the target architecture (**DE-02**: Capacity Management ·
> Scheduling Engine · **Patient Engagement**). Captured 24 Aug 2026 from the operator's own account of
> how clinicians actually run this today, and how the assistant must behave for them to hand it over.
>
> **Status: OPEN — captures 1–7 of N.** This is a faithful record of what the operator specified plus the
> ground truth it lands on. It is **not** yet a design, a schema, or a prompt. Nothing here is settled
> that the operator has not settled. Open questions are collected in §8 rather than answered.
>
> **Companion:** [`day-before-variable-map.md`](./day-before-variable-map.md) — every variable in the
> knowledge base that bears on this sequence, plus the gaps this specification opens.

---

## 1. The framing constraint — why this is not an automation problem

Two premises the operator set before anything else. Both are load-bearing; a design that violates
either is wrong regardless of how well it performs.

**Coordination of scheduling cannot be fully automated.** The clinician stays in the loop and gives
guidance to the system. The assistant executes an engagement the clinician has authored — it does not
author one.

**Scheduling too far in advance does not work in home health.** There are too many variables in play.
**A clinician's schedule is not truly validated until the day prior.** That is not a process defect to
be engineered away; it is the operating reality the protocol is built around.

Together these set the unit of work: **the next-day confirmation sequence** — one clinician, one day's
assigned visits, run the evening before. Everything in this document is scoped to that sequence. Same-day
recovery, welcome/readiness calls, and multi-week planning are out of scope for these captures.

**This is already the clinician's job today, done by hand.** From the process facts:

> *Visit confirmation coordination (SMS / voice) is the clinician's work, done the day before.
> **HCHB does not send reminders.***

and

> The five dispositions are chosen **the day before, straight after the confirmation call** — not at the
> door. This makes the recovery window a day wide, not an hour wide.

So the protocol is not new work. It is the clinician's evening, handed to an assistant, with the
clinician keeping authorship.

### 1.1 Why confirming far in advance fails — the second framing constraint

*Operator, capture 2.* The day-before boundary is not only about accuracy. **Confirming appointments too
far out is unrealistic for the majority of the home health patient population, and it is actively harmful
to the branch.** Two independent failure paths, and they compound.

**The patient side — the commitment does not survive the wait.** Patients and caregivers do not remember
a commitment made days out. A confirmation obtained too early is not a confirmation; it is a message that
has to be sent again.

**The branch side — an early confirmation spends the branch's ability to maneuver.** Narrowing down a
clinician's commitments too far in advance limits the branch's ability to be nimble — to move visits
around **within the week** as referrals come in and as capacity needs to be opened.

This is the more important of the two, and it is the one nothing in the current model measures.

### 1.2 The Wednesday SOC — the worked example

> A physical therapist is working on **Tuesday**. **Thursday is already fully scheduled, and the patients
> have confirmed.**
>
> On **Wednesday**, a **priority start-of-care** referral comes in.

Thursday now has no give in it. Every available outcome costs something:

| Outcome | What it costs |
|---|---|
| The SOC **goes to another clinician** | Wrong territory, broken continuity, and a per-diem or float call — a capacity lever spent to cover a problem the confirmation created |
| The SOC is **deflected to Friday** | Delay against the SOC timing window (`S-35`) — *every* SOC/ROC is seen within 48 hours under Medicare guidelines, so "priority" here means something worse than merely late |
| **One or two confirmed patients are told their appointment has changed** | **The perception of service failure** |

**The third outcome is the one that accumulates.** A single change is absorbed. The operator's point is
about frequency: *especially if this happens more than once within an episode of care for a patient.*
Service-failure perception is **cumulative across the episode**, not per-event — so the cost of an early
confirmation is not paid at the moment it is broken, it is paid at the second or third break, by the
patient's whole read of the agency.

### 1.3 The design consequence

**A confirmation is a liability as well as an asset.** It protects the visit against a no-show, and in the
same motion it converts flexible capacity into a commitment that costs something to break. Confirm too
early and the branch has sold its maneuvering room; confirm too late and the visit is unprotected.

Three things follow, and they shape everything below:

1. **Confirmation timing is itself a variable**, not a fixed rule. The day-before boundary is the current
   answer; the protocol should hold it as a parameter, not a constant.
2. **The unit of work is right.** The next-day sequence is not merely convenient — it is the point at
   which a commitment can be made without spending the week.
3. **Breaking a confirmation is a tracked event with a cost**, and the count per episode is the thing to
   watch. Nothing in the model counts it today.

---

## 2. Channel — chosen by the clinician, at two scopes

Over the last five years, as smartphones have become regular even in the geriatric patient population,
**texting has become standard** — but **phone calls continue to be a big piece of it.** Neither channel
can be assumed.

The system must let the clinician choose the preferred method of communication at **two independent
scopes**:

| Scope | What it is | Behaviour |
|---|---|---|
| **Standing, per patient** | The default channel for this patient across engagements | Set once, persists, editable |
| **Per engagement sequence** | The channel for *this* next-day confirmation run | Overrides the standing default for this run only; does not rewrite it |

The per-sequence override is the operative requirement. A clinician who normally texts a patient may
decide that tomorrow's ask needs a voice call — because the time is unusual, because the negotiation is
delicate, because the patient sounded off this week. The system must make that a one-tap decision inside
the engagement flow, not a trip into a patient profile.

**Consent gates the channel, not preference.** `CN-09` — text and email contact requires signed consent,
and Compassus holds *separate* text, email and share-with-family consents, none usable until signed **at
the SOC visit**. A clinician preference for SMS cannot override an unsigned text consent. See §8, Q3.

---

## 3. Arrival windows, not appointment times

Because the clinician travels to the patient rather than the patient coming to the clinician, the
appointment has to do two things at once:

- **feel official** — so it holds, and so no-shows fall
- **carry inherent flexibility** — because the day will move

The resolution is the **arrival window**. Clinicians do not schedule exact times; they schedule **one-hour
arrival windows**, and in some cases **two-hour arrival windows**.

### 3.1 A standing rule, individually held

Each clinician sets window granularity as a **global standard for their own practice pattern** — not a
branch policy, not a system default. This is the clinician's own operating rhythm.

### 3.2 An easy in-sequence override

The standing rule must be **easy to change during an engagement sequence**, because the factors that
force wider windows vary day to day. The operator's own field pattern, stated as the worked example:

> One-hour arrival windows for the **first half of the day**; **two-hour** windows for patients scheduled
> **later in the day**, and for patients scheduled **after a start-of-care visit** — because of the
> unpredictable variables in seeing a brand-new patient for the first time, with acuity levels not yet
> fully clear.

Two shaping factors are visible in that example and should be treated as first-class:

1. **Position in the day** — uncertainty accumulates, so later slots earn wider windows.
2. **Preceding visit type** — a visit that follows a SOC inherits that SOC's unpredictability.

The requirement the operator drew from it: **a resting rule overall, tweakable ahead of each day's
scheduling engagement process.** The tweak happens before the sequence runs, not after a patient pushes
back.

---

## 4. The day's grid — recommend, then let the clinician own it

### 4.1 What the system proposes

The system produces a **recommended order** for the next day's assigned visits, taking into account
**home address** and **proximity to other patients**.

This is the recommendation half of **DE-09** — *the tool recommends; the human accepts.* It is an opening
position, not an assignment.

### 4.2 What the clinician does with it

- **Drag to reorder.** The clinician drags the patients into the order they choose. The recommended order
  is a starting point they overrule freely.
- **Set the day's start time.** Like the arrival-window rule, the clinician states the time they want to
  start the next day. The system takes that input and attaches **the first patient listed as slot number
  one**.
- **The rest cascades.** For each subsequent patient the system computes the next arrival window from
  **the visit type** (how long the visit takes) plus **estimated drive time to the next patient** — and
  labels the window next to patient two, then three, and so on.
- **Drag on the calendar grid to shape the day.** The clinician drags visits on the day's calendar grid so
  a gap can carry **extra time or less time** between any two patients.

### 4.3 Why the gaps matter

> Some clinicians need to be able to run errands, or like to have documentation time added between patient
> visits, and we need the clinician to be able to be autonomous in how they approach this.

The inter-visit gap is not slack to be optimised out. It is where the clinician's documentation, errands
and personal rhythm live, and the knowledge base already flags this territory as read-only or assist-only
for automation (`S-07`, `S-08`, `S-09`: *"the clinician's own daily rhythm — a strange attractor; small
control inputs distort it"*). **The grid must let the clinician place those gaps and must not reclaim
them.**

This is also the adoption argument. From the whiteboard session:

> *"The reason why clinicians are in home health is because of autonomy — but if you create mechanisms
> that allow them to have more autonomy…"*

---

## 5. Negotiation — stock phrases, then insider information

### 5.1 The fallback layer

The system carries **stock phrases, rearrangeable**, used as fallback when a patient tries to decline the
time the clinician has scheduled. This is the floor of the negotiation capability, not the ceiling.

### 5.2 The context layer — the actual requirement

Stock phrases are not enough. The clinician must be able to add **additional context the system uses when
negotiating times with the patient**, so the assistant has enough to work with to secure the appointment
**using as much insider information as possible**.

**Placement:** on the **right-hand side of the calendar grid**, or **directly below the patient** — beside
the visit it belongs to, entered while the clinician is looking at the day they just built.

**The operator's worked example**, kept intact because it defines the shape of the field:

> The first patient of the day is scheduled for a 9 AM arrival. The nurse notes that she knows this
> patient usually prefers appointments after 11 AM — however, the patient did agree to an earlier time
> just this week, because the nurse has another patient nearby who has to be seen earlier.
>
> That gives enough context for the assistant that if the patient tries to decline, it can remind the
> patient — pleasantly — that this had already been talked about.

Read what that example actually contains, because it is the specification:

| Element in the note | What the assistant does with it |
|---|---|
| The patient's standing preference (after 11 AM) | Knows the pushback is *expected*, not a surprise |
| The exception agreed this week | Has standing to hold the time |
| Who agreed it and when ("just this week") | Can cite it credibly |
| The reason (another patient nearby seen earlier) | Can explain rather than merely insist |
| The register — *pleasantly*, a reminder | Sets the tone; this is not an argument |

The clinician is handing the assistant **a fact the patient already accepted.** That is the difference
between a generic reminder and an engagement that holds.

### 5.3 The doctrine the negotiation must encode

The knowledge base already carries the discipline this context field feeds. From the day-before
negotiation panel:

- **HARD — accept it and build the day around it.** Dialysis days and times · MD and specialist
  appointments · the caregiver's working hours · the patient genuinely not being home. *These are facts
  about the world. Arguing with them wastes the call.*
- **SOFT — negotiable, and worth holding the line on.** *"Can you come after lunch?"* · *"Not first
  thing"* · *"Not Mondays"* · a preferred time with no reason behind it. *These are preferences. They are
  movable, and the clinician has to find the firmness to move them.*

And the reason it is worth the effort, stated plainly on the flow sheet:

> **The first visit at 8 or 9am is the single largest lever on an individual clinician's capacity.**
> Newer clinicians let the patient set the time, become over-accommodating, and push the cost onto the
> rest of the team.

An assistant that holds a soft preference where the clinician has given it standing to do so is doing
something the current process cannot do at all — and it is doing it **with the clinician's authority, not
its own.**

---

## 6. Where the sequence lands

The sequence does not end in a message. It ends in a **disposition**, and the disposition already has a
fixed vocabulary in HCHB — chosen the day before, straight after the confirmation call:

| Disposition | Meaning |
|---|---|
| **Accept** | Confirmed. The overwhelmingly common outcome; flows to tomorrow's schedule |
| **Reschedule** | The most likely outcome when not confirmed |
| **Reassign** | Returns to the scheduler **with** a recommendation (often RN → her own LPN) |
| **Miss** | Documented; starts the 48-hour MD-notification clock (`CN-01`) |
| **Decline** | Returns to the scheduler **without** a plan; least used, and some clinicians are instructed never to use it |

Two consequences for the protocol:

1. **The output contract is the disposition, not a transcript.** Whatever the assistant negotiates has to
   resolve into one of five states the clinician selects.
2. **The decline/reassign *reason* is not captured today.** The variable backlog names this as *"the best
   training signal in the process"* — the clinician doing a capacity tool's job by hand. This protocol is
   the first place that reason could be captured as a by-product of work the clinician is already doing.

---

## 7. What this protocol must not do

Drawn from the constraint register and the automation postures, not invented here.

- **Must not place work on a calendar unilaterally** (`DE-09`).
- **Must not generate frequency** — the clinician originates it; a physician signs it (`CN-06`).
- **Must not move an OASIS visit** — OASIS visits are date-bound and cannot be freely moved (`CN-02`).
- **Must not confirm a visit that is not authorised** — no auth, the visit sits pending, on no calendar
  (`SH-12` / `S-45`).
- **Must not contact a patient where an active POA requires otherwise** — some POAs require the patient
  not be contacted at all (`CN-11`).
- **Must not text or email without the specific signed consent** (`CN-09`).
- **Must not place automated outbound calls where they are regulated as robocalls** — California treats
  any call not manually triggered by a human as a robocall; batch-triggered calls fall under that
  treatment (`CN-10`). **This is unresolved and needs legal confirmation, not operational judgment.**
- **Must not weigh margin against clinical need in what it says to a patient** (`CN-06` in the payer
  handoff; the over-utilisation ceiling is `Read` posture deliberately).
- **Must not reclaim the clinician's inter-visit gaps** (§4.3).

---

## 8. Open questions — for the next session

| # | Question | Why it blocks |
|---|---|---|
| **Q1** | Does the assistant *place the voice call*, or does it prepare the call and the clinician places it? | `CN-10` — the California robocall treatment turns on who triggers the call. Decides whether voice is in scope at all in some markets |
| **Q2** | Is the sequence run per clinician-day as one batch, or per visit? | Shapes the interface and the escalation model |
| **Q3** | What happens when the clinician's chosen channel is not consented? Silent fallback to voice, or surface the block? | `CN-09`. Silent fallback hides a compliance fact from the clinician |
| **Q4** | Where does visit **duration by visit type** come from? Productivity points (`SH-07`) are a weighting, not minutes | The whole window cascade in §4.2 depends on a duration the knowledge base does not yet hold |
| **Q5** | What is the drive-time data source? | Named in the variable backlog as unresolved: *"drive-time vs. straight-line distance — needs a decision on the routing data source before it can be scored"* |
| **Q6** | How far may the assistant hold the line before it escalates to the clinician? Attempts, tone ceiling, stop conditions | This is the difference between an assistant and a liability |
| **Q7** | Does a confirmed window write back to HCHB, and through what interface? | Otherwise the clinician confirms in one place and dispositions in another |
| **Q8** | Contact-attempt policy — how many attempts, over what hours, in what channel order? | Quiet hours, elderly patients, and TCPA-adjacent exposure |
| **Q9** | What happens after confirmation, when the patient calls back to change it? | The sequence has an after-state nobody has specified |
| **Q10** | Does the arrival-window rule live per clinician only, or does the branch get a floor/ceiling? | §3.1 says clinician-owned; branches may disagree |
| **Q11** | How much of the week should stay **deliberately unconfirmed** to preserve maneuvering room, and who decides — the clinician, the branch, or a rule? | §1.1. This is the parameter the whole horizon question turns on |
| **Q12** | When a confirmed visit must be broken to absorb a priority SOC, **who breaks it and how** — the assistant, the clinician, or the scheduler? Does the assistant get a re-contact sequence of its own? | §1.2. Currently unspecified, and it is the most damaging message the system would ever send |
| **Q13** | Should the tool **count and surface confirmation-breaks per patient per episode**, and does a second break in one episode change the branch's behaviour? | §1.3. Service-failure perception is cumulative; nothing measures it today |

---

## 9. Captures 3–7 — the clinician's console, the batch, and the domain rules

*Operator, 25 Aug, condensed. These are records of what was said, not designs.*

### 9.1 Triggers and partial engagement

The tool runs off **triggers and instructions the clinician provides**, including scheduling an engagement
to run later. Typical moment: Tuesday early afternoon, once tomorrow's assignments have stabilised and the
clinician can see everything they have to contend with. The clinician may engage **some or all** of the day —
all five patients, or just the first two, or the first and the last. **The controls have to be dynamic enough
to give that level of autonomy, matching what clinicians already do in real life.**

### 9.2 The routing button and the end-of-day address

An optimize action shows the day ordered on proximity alone — home base, patient-to-patient distance,
nothing else. The clinician can add an **end-of-day address**: a saved one (a child's school) or a **one-time
address for tomorrow only** (errands), so the routing reflects the day they are actually going to have.

### 9.3 The arrival-window shadow

Each visit is a block sized by visit type; behind it sits a **shadow** representing the arrival window.

- Drag the **block** to place the visit — e.g. a mid-morning-optimal SOC moved onto the 2 PM marker.
- Drag the **shadow** independently, in **15-minute increments**, to position the window around the visit:
  1:00–2:00 · 1:15–2:15 · 1:30–2:30 · 1:45–2:45 · 2:00–3:00.
- Dragging the shadow **flush to the visit time** (9:00–9:00, or 8:30–9:00, 8:45–9:15) is how a clinician
  **overrides their own standing window rule for one visit** — used when they know they can hit an exact time.

**Pin / anchor** fixes a visit to its time. An anchored visit is *the rock in the river* — everything else in
the day is scheduled around it.

### 9.4 The two anchors, and why they unlock the day

The clinician anchors two visits first: **the first visit of the day**, and **the new SOC**. Both get confirmed
before anything else is scheduled. The reason this works:

- **The first visit is the hardest placement in the day** if it is before 10 AM. Most refusals sit in the 8
  and 9 o'clock hours. So the system needs an **early-bird tag** — recognised or clinician-applied — because
  that patient is the key that unlocks the rest.
- **Prime treatment time is 10 AM – 3 PM.** Most patients will take a visit in it, absent an MD appointment or
  another variable.
- A **smaller** group dislikes late-day visits — smaller than the morning-averse group.

While the first two engagements run, the clinician can go into a patient visit. They come out to a result.

### 9.5 The flexibility dial and the batch

Each remaining patient tile carries a **note field** and a **flexibility dial**: red/firm on the left, through
medium, to high.

- **Firm patients are contacted first in the batch** — lock the particular ones while there is still room to
  move around them; leave the flexible ones for path-of-least-resistance placement.
- **A red-marked patient requires a clinician context note** before the agent may work it.

**Concurrency, settled for now:** the batch runs **one targeted confirmation at a time, sequentially**, until
all confirm — because parallel outreach lets two patients confirm into the same slot. *Bookmarked as needing
more direction.*

**Mission:** do not push anyone off. When that fails — pull an alternative patient in, move the refusing
patient to the next day, and have the assistant carry their time request forward and work the plan with the
clinician **before** that day.

### 9.6 Reporting back, and escalation

The clinician gets outcomes they can act on: *text sent, no response* · *text sent, patient agreed* · *text
sent, patient requesting 10 AM instead of 9 despite encouragement*. **Call recordings are listenable; text
threads are readable.** Where the protocol escalates (e.g. no text reply after 30 minutes → voice call), the
result names both steps.

Escalation gives the clinician: reference points from every attempt · the power to swap in a patient from a
**waitlist** · a view of what slots are actually open · the system pulling **wish-list coverage patients** that
fit the gaps · help rearranging to make a different area realistic. Plus a channel from clinician to
**scheduler, manager, or same-discipline teammates** who need support or can lend it.

### 9.7 Per-patient engagement protocols

Prefab options in a drop-down plus a custom option, mimicking the tricks of the trade clinicians have learned
for getting a response. *An unanswered text and an unreturned voicemail hold up the entire scheduling process.*
One protocol is the clinician's standard, modifiable per patient:

- **Phone only** — patient does not consent to text, or says text is not optimal for them
- **Text only**
- **Combo** — text first; no response after a configurable interval → phone call with a voicemail; still
  nothing after another interval → a further step, which may be **an alert to the clinician to try themselves**

### 9.8 Domain rules for the scripts

**Who performs the SOC.** Nursing referred in → **nursing must do the SOC** (Medicare); every other discipline
enters afterwards as an **evaluation visit** (PT, OT, ST, MSW). Nursing not referred → **PT does it by default**.
OT can, but rarely. Working rule: **therapy takes the SOC only when nursing is not on the case.**

**The welcome call** precedes all of this — from the office or another AI assistant — to check the patient is
home and available.

**Visit lengths.** Routine 30–45 minutes. Assessment-heavy visits — admissions, discharges — a full hour to
approaching two, depending on differential diagnosis and complexity. *(Dolores' calendar gives real observed
durations: RN SOC 95 min, PT eval 70 min, MSW 69 min, LPN 42 min.)*

**Over-scheduling is deliberate.** Clinicians function best carrying **more than their expected visits** for
the week, because it is rare to have a week without two or three falling out to cancellation or hospital
admission.

**Arrival windows.** One hour is best practice. The goal is always the front of the range; the back half
absorbs the preceding visit and traffic.

### 9.9 The eight competing priorities on every visit

From the Compassus deck: **regulatory timing** (SOC OASIS within 48 hrs of referral) · **prioritisation**
(acuity, instability, diagnosis, rehospitalisation risk, regulatory urgency) · **geography** (cluster to cut
drive time, manage fatigue, protect productivity) · **productivity** (visit count, complexity, travel and
documentation burden balanced into a sustainable day) · **frequency** (spread across the episode, not
compressed) · **care team** (work around the other disciplines' visits) · **MD orders** (wound care, protocols,
labs) · **patient availability** (appointments, caregivers, routines, fatigue patterns, preferences).

### 9.10 The agent behaviour rules

These are recorded in full as addressable rules in [`logic/00-shared-agent-rules.md`](./logic/00-shared-agent-rules.md).
The load-bearing ones, in the operator's own terms:

- **Never promise a return call** unless the clinician gave that context.
- **Never promise a specific clinician** for a future visit — they may have left or changed territories. Take
  the name, tell them the office will be told.
- **Not knowing is a safe place.** *"The assistant isn't always provided all of the information other than who
  needs a visit and what clinician is scheduled — any questions can be answered by the clinician coming out."*
- **Don't add to the confusion.** Early episode, the patient is newly home with new impairments and cannot tell
  who anyone is. If they mention an earlier call, **name it** as the welcome call.
- **Sequencing stop.** Scheduling a therapy evaluation → ask whether the nurse has been out. If not, confirm no
  visit happened and none was scheduled by another clinician, say the message will be passed along and the
  office will coordinate, and disengage.
- **Disengage on doubt**, including adamant refusal of services: a message will be left for the clinician and
  their doctor, and someone will follow up.
- **Coverage visits.** *"I'm not sure why this other clinician is being scheduled, but it's likely your primary
  clinician is unavailable and asked for support just for this one visit."* Continuity of care is why the visit
  still matters.
- **Why a window, not a time.** The clinician is coming to the home and has other patients; unpredictable
  things happen travelling or inside a visit. The range is what lets the clinician recover and still reach
  everyone.
- **Pushback tactics on a critical window** — limited availability, honestly stated (the time was set aside
  around other patients already in that area); and the forward promise (take this first visit at this time, and
  everything after gets scheduled around what works for you and whoever needs to be there).

### 9.11 The governing doctrine

> **Pliable enough to meet patient requests, firm enough to protect the clinician — the assistant works on
> behalf of the clinician who is servicing the patient.**

The ultimate goal is that the clinician's day is as effective and efficient as possible and their **autonomy is
maintained**. The tool follows the clinician's instructions, helps them strategise and optimise, and offloads
the most inherently frustrating part of home health: the back-and-forth of scheduling tomorrow.

---

## Provenance

| | |
|---|---|
| **Operator input** | Colin Highland, 25 Aug 2026 — captures 1–7. §2–§8 the first walkthrough, §1.1–§1.3 the confirmation-horizon argument, §9 the console mechanics, batch logic, domain rules and agent doctrine. More to come |
| **Ground truth drawn on** | [`../knowledge/process-facts-2026-08.md`](../knowledge/process-facts-2026-08.md) · [`../knowledge/constraint-register.md`](../knowledge/constraint-register.md) · [`../knowledge/whiteboard-session-2026-08-13.md`](../knowledge/whiteboard-session-2026-08-13.md) (DE-01…DE-10) · [`../artifacts/flow-map-redraw-assessment.md`](../artifacts/flow-map-redraw-assessment.md) §16–17 · [`../artifacts/variable-backlog.md`](../artifacts/variable-backlog.md) · `Variable Inventory` tab of the 8.13 workbook |
| **Agent logic** | [`logic/`](./logic/) — shared rules, welcome call, SOC confirmation, evaluation confirmation, as addressable states |
| **Not yet done** | Routine / assessment / recert / discharge scripts; prompt build in the Aethergrid Prompt Factory; schema; UI spec; workbook rows for the new `E-` variables |
