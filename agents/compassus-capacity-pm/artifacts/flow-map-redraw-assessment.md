# Flow Map Redraw — Assessment

> **Purpose.** Assess the existing swimlane map against the 13 Aug session and the clarifying
> document, before any redraw. Nothing here is drawn yet — this is the read.
>
> **Sources**
> - `8.13 capacity scheduling swimlane detail.pdf` — Drive `1SZDHuYYzkMLP-J7uCKdITY3CGZA3qhCx`.
>   One sheet, 2070 × 1380 pt, labelled *Baseline April 2025*, footer *Continues: Home Health Intake
>   Reset · Page 2*.
> - Clarifying document — Drive `1NSHlkaWir6rc7mgZ1ONtwG-sIPsNFayV`. Four flows, each closing with
>   *Refinements for the redraw*, plus an explicit corrections list.
> - [`../knowledge/whiteboard-session-2026-08-13.md`](../knowledge/whiteboard-session-2026-08-13.md) — DE-01…DE-10.

---

## 1. What the map is today

**Seven actors, by colour.** PCC/Scheduler (yellow) · Scheduling System HCHB (purple) · ED/DCS
(maroon) · Clinician (blue) · Per Diem/Float (brown) · Patient (green) · **Insurance & Auth
(orange)**.

**Five phase columns.** Clinician Scheduling Workflow · Capacity Read · Scheduling & Assignment ·
Coordination · Delivery & Outcomes.

**One horizontal spine.** A grey band across all five columns — *"Admitted Episodic Referral — Ready
to Schedule → Delivered Visit (the clean path)"* — carrying the happy path, with exception handling
dropped below it and inputs above it. This is the strongest idea in the drawing and it should
survive.

**The tell:** *Insurance & Auth has a colour in the legend and not one block on the sheet.* The map
knows auth exists and does not draw it.

---

## 2. The blocking decision: the legend means two different things

This has to be settled before anything is recoloured, because every other colour question depends
on it.

| | Legend | Reading |
|---|---|---|
| **Map today** | Colour = **who owns the step** | Purple = "this lives in HCHB" |
| **DE-07** | Colour = **what kind of task it is** | Yellow = human task *(inside or outside the system)*, purple = **genuine** system action, green = patient-supplied |

DE-07 also states the finding that makes this sharp: **genuine automation in HCHB is approximately
nil.** Under DE-07, almost every purple block on the sheet is mislabelled — they are human tasks
performed *inside* HCHB, which is yellow.

Roughly **12 purple blocks** are on the sheet. Three are being corrected now. The other nine face
exactly the same test, and the clarifying document already answers several of them in prose:

- *"Committed load computed and capacity assessed. **PCC.** These are HCHB **reports, not
  workflows** — they must be manually triggered and manually recombined."*
- *"Discipline and specialty matched. HCHB… **This is filtering, not automation.**"*

**This also creates one genuine contradiction to resolve.** The corrections list says the green
*Patient rules* block should become **purple** — because the rule lives in the system as a
coordination note. But the same document's step text says *"Patient rules and needs applied. **PCC**,
via coordination notes and Point of Care visit alerts… The information is in the system, **entered by
a human**."* Under an actor legend, purple is right. Under DE-07, that is a human task entered by the
PCC — **yellow**. The two legends give opposite answers on the same block.

**My read:** DE-07 is the more useful legend, because the whole point of the exercise is to separate
HCHB constraints from real requirements, and an actor legend hides where the human labour actually
sits. But it is a decision, not a detail, and it changes the majority of the sheet. Recommend a
**hybrid**: colour = task type (DE-07), and a small actor tag on each block (`PCC`, `RN`, `DCS`,
`Auth`) so ownership is still legible. That keeps the visual system and answers both questions.

---

## 3. Coverage — the map against the four flows

DE-01 splits the work into four flows. Here is what the current sheet actually carries.

| Flow | On the map today | Verdict |
|---|---|---|
| **1. SOC / recert / ROC / new order** | Partly — starts at the referral reaching the scheduler | **Starts too late.** Three upstream steps missing |
| **2. Routine visit scheduling** | Barely — implied as a scheduler-driven loop | **Structurally wrong.** See §5 |
| **3. Authorization cycle** | **Nothing.** Legend colour, zero blocks | **Absent** |
| **4. Exception & recovery** | Partly — call-out, missed visit, LUPA present but thin | **Wrong in detail** |

**Flow 1 begins in the wrong place.** Three steps sit upstream of the scheduler's first block, and
adding them moves the first bottleneck earlier than the map shows: eligibility verification (auth
team, in Commure, automated today) → pending auth keyed (count set by payer: 1, 3, 5 or 10;
traditional Medicare passes straight through) → return to intake for final approval. Then, and only
then, the referral enters the scheduling workflow. *"We know we have the referral, but it's just not
in my workflow to schedule yet because it's stuck in auth."*

---

## 4. The correction inventory

Everything asked for, sorted by how much drawing it costs.

### A. Recolour — cheap, do first

| Block | Now | Should be | Source |
|---|---|---|---|
| PCC Completes Clinician Scheduling Workflow | purple | **yellow** — PCC does it | you + doc |
| Read open capacity — day · week · discipline · territory | purple | **yellow** — PCC does it | you |
| Day-before confirm | purple | **blue** — the clinician makes that call | you |
| Patient rules — caregiver present · window · day-of-week | green | **purple** *(or yellow)* | doc — **see §2** |
| *All* PCC in-system workflow steps | purple | **yellow** | doc, general sweep |

### B. Relabel — cheap

- **"Missed — unworked" → "Missed visit."** Drop "unworked".
- Annotate the plan-of-care task **"×4 disciplines."**

### C. Restructure — moderate

- **The missed-visit chain is wrong, and it is not a dead end.** Today it terminates in a maroon
  oval. It actually runs: clinician documents missed visit → **scheduler receives workflow to notify
  MD within 48 hours** (a Medicare requirement *and* an HCHB hard stop) → **if not documented in
  time, workflow generates to the DCS.** Compliance chain, not terminus.
- **Visit state needs three values, drawn explicitly:** scheduled · missed · completed. Sequence is
  *scheduled → documentation pending → missed*, not "delivered" as the trigger.
- **The clinician's five dispositions are missing entirely:** accept · reassign · reschedule · miss ·
  decline. This is the clinician's half of scheduling every visit and the map does not show it.
- **The whole bottom-right needs redrawing** — delivery and outcomes, per the two points above.

### D. Net-new — the real work

1. **The authorization cycle**, as its own flow. Verification in Commure before the referral workflow
   starts; anything but traditional Medicare routes to pending auth; branch waits on intake after
   auth; after SOC, re-auth only when the plan of care exceeds what is authorized; additional orders
   need DCS approval *and* more auth. Payer behaviour is specific and worth drawing: UHC 5 nursing
   visits with 4 completed plus documentation before visit 6; Indiana Medicaid 30 days from
   **discharge** date with 8 visits shared across PT/OT/ST.
2. **DCS workflows**, which are named repeatedly and drawn nowhere.
3. **Routine visits as two phases** — see §5.
4. **Pending-auth invisibility** as a first-class failure: visits that do not appear on the
   clinician's calendar, cannot be told to the patient, and count toward nothing. *"If you can't see
   it, you can't plan."*

---

## 5. The single largest structural error

**The map implies routine visits are a continuous scheduler-driven loop. They are not.**

- **Phase One — assignment burst.** The evaluating clinician plots frequency *for their own
  discipline only*. Each submission generates its own scheduler assignment task; nursing at SOC, PT
  and OT one to two days later. Four disciplines produce four tasks, then four more at approval.
- **Phase Two — steady state.** **No scheduler workflow at all**, unless a visit must be reassigned.
  The assigned clinician moves any non-OASIS visit within the Medicare week, inside the 60-day
  certification period, running their own undocumented weekly logic: own capacity → clinical
  prioritisation → geographic grouping → hard constraints (wound timing, catheter, IV, competing
  appointments) → confirm with patient → route.

Two consequences worth drawing loudly:

- **Reassignment is the *only* recurring scheduler trigger in steady state** — and the clinician
  cannot do it themselves. An RN cannot hand a visit to her own LPN without routing it back through
  the scheduler. This is an HCHB restriction, not a Medicare rule. Remove it and essentially all
  recurring scheduler involvement in routine visits disappears.
- **The RN manages aide frequency** — a supervision relationship the map does not represent at all —
  while being unable to see the aide's calendar.

---

## 6. What "keep the design" can and cannot survive

**Keeps working, reuse everywhere:** the actor colour vocabulary, the phase columns, the grey
clean-path spine with exceptions dropped below it, decision diamonds, terminal ovals, the
dashed-feedback convention.

**Does not survive:** one sheet. DE-01 already decided four flows, and Flow 1 alone gains an upstream
auth sequence, a ×4 discipline multiplier and a DCS lane. Flow 3 does not exist yet. Forcing four
flows onto this sheet would produce something nobody can read in a room.

**Recommendation:** keep the design language exactly, change the number of sheets — **four flows,
one visual system, layerable into the composite** DE-01 asked for. Each flow keeps the spine idea:
clean path along the middle, exceptions below, inputs above.

**Worth noting:** the five phase columns already map cleanly onto the three-arena model, so the flow
maps and the variable documents can share one vocabulary rather than drifting apart.

| Phase columns | Arena |
|---|---|
| Clinician Scheduling Workflow · Capacity Read | **Capacity Management** |
| Scheduling & Assignment | **Scheduling Engine** |
| Coordination · Delivery & Outcomes | **Patient Engagement** |

---

## 7. Open questions

1. **Legend — actor, task type, or hybrid?** §2. Everything else waits on this.
2. **Patient rules — purple or yellow?** Falls out of question 1, but it is the one place the
   corrections list and the step text disagree outright.
3. **Where does the upstream auth sequence live** — added to Flow 1, or on page 1, the *Home Health
   Intake Reset* map this sheet continues?
4. **Current state only, or current and target side by side?** The session deferred the future-state
   map but flagged it as needed before bringing partners in.
5. **What tool holds the redraw?** This assessment is format-neutral. If the four flows are to stay
   editable by Colin, that constrains the answer.

---

## 8. Suggested sequence

1. Settle the legend (§2). One decision, unblocks everything.
2. Apply recolours and relabels to the existing sheet — cheap, visible, no structural change.
3. Redraw the bottom-right: visit states, the five clinician dispositions, the missed-visit
   compliance chain.
4. Split Flow 1 out and extend it upstream through verification, pending auth and intake approval.
5. Draw Flow 3 (auth) from scratch — the largest gap.
6. Draw Flow 2 as two phases, making the Phase Two silence obvious.
7. Rework Flow 4 with call-out recovery, LUPA watch, decline, and Shift Finder.
8. Compose the four into the layered composite.

---

## 9. Resolved in conversation (17 Aug)

**Legend stays role-based for iteration 1.** Everyone from the meeting is comfortable reading colour
as role. The DE-07 task-type legend becomes a *second* iteration — a back-up flow built once this
one is right — so the room is not asked to re-learn the sheet. Consequence: the green **Patient
rules** block becomes **purple**, because the rule lives in the system as a coordination note.

**Branch leadership splits out of the ED/DCS chip.** Branch leadership gets its own high-contrast
treatment — black block, white text — to separate a *joint leadership assessment* from an individual
DCS clinical role. The existing maroon *ED / DCS review — reopen zip · add per-diem · adjust patterns
· defer* block is branch leadership, not DCS, and moves to black.

**Plan-of-care QA is drawn as DCS.** DCS performs QA in the majority of markets. The
"DCS-or-separate-QA-team" variation is parked as a reference point for the connected future-state
map rather than drawn as a fork now.

**DCS scope for iteration 1 is deliberately narrow.** In: the two hard gates (plan-of-care QA, order
approval) and the missed-visit backstop, which the corrections list requires. Out for now, parked for
the future-state map: DCS as last-resort clinician, the daily afternoon huddle, the daily Pulse LUPA
report, and PTO cross-approval. Rationale — too much to carry into the first read.

### Still open

- **Order-approval scope.** Does *every* physician order pass the DCS gate, or only add-on /
  subsequent orders after the 485? Working assumption: all orders gate, and only frequency-changing
  ones additionally generate scheduler workflow.
- **Recert / ROC.** Does the QA gate behave the same as on SOC? The clarifying document treats them
  as one trigger class and records the differences as unknown.

---

## 10. Order approval — resolved

**Every physician order passes the DCS gate.** No exceptions, no bypass.

**The scheduler is only pulled in when the order generates visits to assign.** That is the split —
not whether the order changes frequency, but whether it produces assignable visits. DCS approval is
universal; scheduler workflow is conditional on visit generation.

### The five triggers

The scheduler's entire workload in this flow is **one repeating pattern fired by five triggers**:

| # | Trigger | Note |
|---|---|---|
| 1 | **Start of care** — initial assessment at first admission | The clinician plots their own discipline |
| 2 | **Add-on order** — any new order inside the 60-day certification | Routes DCS → auth → scheduler |
| 3 | **Recertification** — OASIS timestamp | Only the disciplines continuing past day 60 |
| 4 | **Resumption of care** — hospitalisation during the episode | OASIS timestamp |
| 5 | **Missed visit** | Different shape — a compliance chain, not an assignment |

Triggers 1–4 all resolve to the same sequence: clinician submits → **DCS gate** → visits generate →
**auth gate** → scheduler assigns to the care team → visits land on the clinician's calendar.
Trigger 5 runs a separate path: clinician documents the miss → scheduler workflow to notify MD
within 48 hours → if not documented in time, workflow to DCS.

**Why this matters for the drawing.** The current map implies scheduler work is continuous. It is
not — it is five discrete triggers hitting one repeating pattern. Drawing the pattern once and
showing five entry points into it is both more accurate and far easier to read than drawing the
work five times.

---

## 11. Agreed next artifact — the simplified DCS / Scheduler map

A cut-down flow covering only the DCS and scheduler roles, to be drawn **before** the full redraw.

**Purpose.** Prove the conventions cheaply, and give the room a legible picture of the handoff that
carries the pending executive decision on DCS order approval.

**Rule that keeps it safe.** It must be a strict *subset* of the full map, never a different map —
same colours, same spine idea, same block labels, same shapes. Then it expands into the full flow
rather than needing reconciliation. This is the "layerable" property DE-01 already asked for.

**Proposed contents**

- Actors: Clinician (blue) · DCS (maroon) · PCC/Scheduler (yellow) · HCHB (purple, minimal) ·
  Insurance & Auth (orange, as a gate only)
- Five trigger entry points stacked on the left, feeding one spine
- **Spine A — orders to visits:** clinician submits → DCS gate (diamond: approved?) → visits generate
  → auth gate (diamond: auth exists?) → scheduler assigns → clinician calendar
- **Spine B — missed visit:** clinician documents miss → scheduler MD-notification workflow →
  diamond: notified inside 48h? → No → DCS backstop
- Failure branches drop below the spine, as in the original

### Open questions for this artifact

- **Is plan-of-care QA the same DCS workflow object as order approval, or two distinct gates?** The
  4-task checklist — POC review, calendar accuracy, pending-auth management, POC lock — reads like a
  fuller review than a routine add-on order approval.
- **Do recert and ROC fire the full 4-task QA, or only order approval?**
- **The daily Pulse LUPA report** — still parked, or in?

---

## 12. DCS answers — gates, and the utilisation ceiling

**Plan-of-care QA and order approval are technically the same workflow object.** One maroon gate
shape, not two. But it fires **once per discipline** — the DCS approves each discipline's plan of
care separately. The `×N disciplines` annotation therefore belongs on the **DCS gate as well as** the
scheduler assignment task. The task explosion is doubled: N approvals and N assignment tasks for a
care-team decision made once.

**Recert and ROC fire the same gates as SOC.** No variation to draw.

**The daily Pulse LUPA report is in** for this flow.

### The pair that matters: floor and ceiling

The DCS also owns **utilisation management for each episode**, and it belongs *inside* plan-of-care
approval rather than beside it. Under PDGM the 30-day period pays a fixed, case-mix-adjusted amount
regardless of how many visits are delivered. That creates two thresholds, and the DCS steers both:

| | Threshold | What happens if crossed | Owner |
|---|---|---|---|
| **Floor** | **LUPA** — minimum visits in the period | Period reverts to per-visit payment; the period's revenue collapses | DCS runs the daily Pulse report |
| **Ceiling** | **Utilisation management** — visits beyond clinical need | Payment does not increase, so every extra visit is pure cost; margin erodes and clinician capacity is consumed for nothing | DCS steers via plan-of-care approval |

**The plan-of-care approval is where the episode's visit budget is set.** That is the single reason
this gate deserves prominence: it is not administrative box-ticking, it is the control point for
both thresholds at once. Approving each discipline's plan of care *is* the act of setting the band.

### Consequence for the capacity model

This qualifies what "open capacity" means. Our capacity documents currently frame open capacity as
headroom to be filled. Under PDGM there is an **economically optimal band per episode**, not a
maximum — a branch that fills every open slot with visits above clinical need destroys margin while
looking productive. This is ecosystem gap **1B** (the economic layer) arriving from a new direction,
and it should be reflected when the capacity documents next change.

### How to draw the pair

The existing sheet already carries a *Period at LUPA risk?* diamond with a *Recover / front-load*
follow-on. Draw the ceiling as its **mirror image** — a second diamond beside it, same shape, same
maroon owner — so the pair reads as one idea:

- `Period at LUPA risk?` → **Yes** → recover / front-load *(existing)*
- `Period over utilisation target?` → **Yes** → DCS reviews plan of care, adjusts frequency

Both feed back to the DCS plan-of-care gate, which is where the band was set in the first place.
Two diamonds, one symmetry, no new vocabulary.

---

## 13. Correction — SOC and ROC run two passes, not one

The first draft of the simplified map was wrong. It started every trigger at "clinician submits
plan of care", which is only true *after* the discipline-specific assessment has happened.

**Start of care and resumption of care run a referral pass first.** Initial orders arrive on the
referral, and before any clinician writes a plan of care:

1. **Office verifies** eligibility
2. **DCS reviews the referral**
3. DCS sends workflow to the **scheduler**
4. Scheduler books the **SOC / ROC visit and the secondary discipline evaluation visits**
5. Those clinicians perform their visits

Only then does the pattern I originally drew begin.

**Recertification and add-on orders skip pass 1 entirely.** They start at the discipline level:

- **Recertification** — each discipline performs either the **recertification OASIS visit** or a
  **discipline recertification evaluation visit, which is not OASIS**.
- **Add-on orders** — **no OASIS attached.** Usually a change in patient status requiring a
  frequency adjustment: adding visits, *reducing* visits when the patient is progressing better
  than expected, or redistributing frequency **without changing the episode total**. All of those
  are processed as an add-on order.

So the five triggers are not peers. They are **two classes converging on one shared pattern**, and
the map now draws them that way — a referral pass for SOC/ROC, direct entry for recert and add-on,
all meeting on a single bus into the discipline plan-of-care pattern.

**Why this matters beyond accuracy.** The scheduler appears *twice* for a start of care — once to
book the SOC and evaluation visits, and again per discipline to assign the ongoing visits. The
original map showed only the second. That understates scheduler load at admission, which is exactly
the point in the episode where load is heaviest.

### Canvas note

Adding pass 1 makes the sheet taller. The canvas is now 1600 × 1250, a ratio of **1.28** against
A4 landscape's 1.414, so it prints landscape with side margins rather than filling the sheet. Three
options if that matters: accept the margins, move to a wider canvas that matches the original sheet's
1.5 ratio, or move the missed-visit chain onto Flow 4 where it arguably belongs. Not decided.

### Canvas decision — resolved

Option 2 taken: **wider canvas at sheet scale**, missed-visit chain stays on this map because the
scheduler and DCS both carry real load in that workflow.

The finalised sheet is **2200 × 1620 pt (30.6 × 22.5 in)**, the same class of large-format sheet as
the original 2070 × 1380.

**The rule that came out of it:** canvas units are points on the output sheet, so a 16-unit label
prints at 16pt. The earlier A4-scale canvas was printing block text at roughly **4.5pt** — legible on
screen, useless on paper. Drawing at sheet scale and letting the sheet be large is the only way to
get type that reads in a room. Apply this to all four flows.

### Intake and the auth team are different actors

Confirmed. The single *Office verifies eligibility* block was wrong. Pass 1 now runs:

1. **Intake** receives the referral, in Commure
2. **Auth team** verifies eligibility and keys pending auth — *traditional Medicare passes straight
   through; any other payer routes to the auth team*
3. **Intake** gives final approval
4. **DCS** reviews the referral
5. **Scheduler** books the SOC / ROC visit and the discipline evaluations
6. **Clinicians** perform those visits

**Intake is a new actor on the legend**, drawn teal `#1F6F78`. It now appears in all four flows.

## 14. Remaining work on the bottom-right corner

The original correction had three parts. Only one is done.

| Part | State |
|---|---|
| Missed-visit chain — document → scheduler notifies MD in 48h → DCS on breach; "unworked" removed | **done** |
| Visit states drawn explicitly — scheduled · missed · completed, sequenced *scheduled → documentation pending → missed* | **not drawn** |
| The clinician's five dispositions — accept · reassign · reschedule · miss · decline | **not drawn anywhere** |

Underneath all three sits a cause nothing draws yet: **the sync gap.** HCHB runs over Citrix, so the
back office cannot see a visit until the clinician syncs. A Tuesday visit synced on Friday reads as
undocumented. A started visit usually means the patient was seen — but not always; the example given
is a clinician who called 911. Visit state cannot be drawn as a clean trichotomy without showing it.

**Recommended order for the remaining flows:** Flow 4 (exception and recovery) first, because it
closes the above and the missed-visit chain relocates into it; then Flow 1, whose spine is already
drawn here; then Flow 3 (auth), which feeds Pass 1; then the composite last, assembled from four
sheets that are already trusted.

**Open for Flow 4:** on a clinician decline, does a distinct workflow generate, or does it land back
in the same reassignment queue as everything else?

## 15. Flow 2 drawn — routine visit scheduling

`flow-routine-visits.html` / `Flow-Routine-Visits.pdf`. 2200 × 1420 pt.

**Structure.** Phase 1 is the assignment burst at admission — each discipline plots its own
frequency, each submission generates its own assignment task, `× N disciplines` on both. The **485
is drawn as a hard boundary**: after it, every order is an add-on and routes through DCS approval and
auth. Phase 2 is steady state, banded and labelled **NO SCHEDULER WORKFLOW**, carrying the six steps
of the clinician's weekly logic that the clarifying document records as entirely undocumented today.

**The five dispositions are now drawn** — accept · reschedule · reassign · miss · decline — with
reassign marked as *the only recurring scheduler trigger*. That closes the second of the three
bottom-right corrections.

**Variable chips at level 2.** A light chip under each step naming the deciding variables. This is
what finally joins the flow maps to the variable reference: roughly 30 of the 47 scheduling variables
sit inside Phase 2.

Also carried: the boundaries strip (OASIS visits do not move · Medicare week Sunday–Saturday · inside
the 60-day certification period · auth still gates), and the four named breaks.

**Still open:** on a decline, does a distinct workflow generate, or does it land back in the ordinary
reassignment queue? Drawn as "back to scheduler" for now.

**Deferred by agreement:** an annotated companion sheet with fuller commentary, to be built only once
the flow itself is right.

### Decline is not reassign

Confirmed 17 Aug, and the two are now drawn as distinct dispositions:

- **Reassign** — back to the scheduler, and typically **RN to her own LPN**. A discipline-role
  handoff inside the care team. It routes through the scheduler only because HCHB forbids the
  clinician doing it directly.
- **Decline** — back to the scheduler, and the visit **must go to a clinician other than the original
  one**. The scheduler can see that it was declined.

**The decline flag already exists.** That changes the variable-backlog entry: the *fact* of a decline
is captured today. What is missing is the **reason**, and the accept side of the loop. The fact alone
trains nothing — the reason is the signal any later optimisation would learn from.

### Variable chips switched off

The chips are removed from the flow sheets. Reason: **the variable IDs are not stable yet.** More
capacity and scheduling variables are still to be added, and five existing rows carry no ID at all.
An ID printed on a sheet goes silently wrong the moment the inventory is renumbered, and nobody
notices because the sheet still looks correct.

The capability is retained behind `SHOW_VCHIPS` in each generator, so chips can come back in one line
once the backlog has landed and numbering is settled. The exercise was still worth doing — it showed
what the annotated companion should eventually look like, and it is the reason we now know roughly 30
of the scheduling variables sit inside Phase 2.

**Rule going forward:** flow sheets name steps, not IDs. The variable reference names variables.
Nothing downstream depends on an ID until the ID is stable.

---

## 16. Plain-language lists replace the chips — and the day-before negotiation

The space the chips left behind is now worth more than the chips were. Each of the six Phase 2 steps
carries a short list of **what the clinician is actually working around at that step**, in the words
an operator would use rather than in IDs:

| Step | What the clinician is working around |
|---|---|
| Evaluate own capacity for the week | Points already committed · days off, PTO, on-call · documentation still owed |
| Prioritise clinical need across the caseload | Who is unstable · wound, IV, catheter due · labs due · who can safely wait |
| Group visits geographically | Who sits near whom · **drive time, not distance** · bridges, rivers, crossings · where the day starts |
| Test against hard constraints | Wound care timing · catheter and IV schedules · caregiver must be present · dialysis and MD appointments |
| Confirm with the patient — day before | "Can you come later?" · "Not Mondays" · patient not home |
| Route — HCHB suggests, clinician adjusts | The suggested route · patient time windows · traffic and time of day · where the day must end |

These are descriptive, not scored. They survive a renumber, which is the whole point — see §15.

### The day-before negotiation panel

The confirm step is where the schedule is actually won or lost, so it gets its own panel below the
band: **THE DAY-BEFORE NEGOTIATION — what the clinician has to hold.** Two columns, because the two
kinds of pushback demand opposite responses:

- **HARD — accept it and build the day around it.** Dialysis days and times · MD and specialist
  appointments · the caregiver's working hours · the patient genuinely not being home. These are
  facts about the world. Arguing with them wastes the call.
- **SOFT — negotiable, and worth holding the line on.** "Can you come after lunch?" · "Not first
  thing" · "Not Mondays" · a preferred time with no reason behind it. These are preferences. They
  are movable, and the clinician has to find the firmness to move them.

The panel carries the reason it matters, stated plainly on the sheet:

> **The first visit at 8 or 9am is the single largest lever on an individual clinician's capacity.**
> Newer clinicians let the patient set the time, become over-accommodating, and push the cost onto
> the rest of the team.

That last sentence is the adoption argument in miniature. The cost of over-accommodation is real, it
is paid by somebody other than the person who accepted it, and nothing in the system today makes it
visible. A capacity tool that surfaces the soft/hard distinction at the moment of the call is doing
something the current process cannot do at all.

**Canvas is now 2200 × 1540** (ratio 1.429) to hold the panel. The Phase 2 → disposition connector
routes down the right-hand side at x≈1865 and back left below the highlight line, so it clears the
panel rather than crossing it.

---

## 17. The dispositions sit before the visit, not at it

Corrected 18 Aug. The five dispositions are **not** what happens when the clinician arrives. They are
chosen **the day before**, straight after the confirmation call, and selected by the clinician **in
HCHB**. The band is relabelled `THE DAY BEFORE · THE CLINICIAN'S FIVE DISPOSITIONS`, carries
`SELECTED IN HCHB`, and states the timing plainly on the sheet: *chosen the day prior, straight after
the confirmation call — not at the door on the day of the visit.*

This matters more than a caption. If the disposition is picked the day before, then the scheduler's
recovery window is a full day wide, not an hour wide. Anything the tool could do with a decline or a
reassign, it has a day to do it in.

### Accept is the default path

The connector out of the steady-state band now lands on **Accept**, not on Reassign. Accept is the
overwhelmingly common disposition, and drawing the spine into an exception made the exception look
like the norm. The other four hang off the same band as alternatives.

### Reassign and Decline are both scheduler triggers

The earlier sheet called Reassign *"the only recurring scheduler trigger."* That was wrong. Both are
clinician selections in HCHB, and both return the visit to the scheduler. The difference is **whether
a recommendation comes with it**:

| | Returns to scheduler | Carries a plan | Who resolves it |
|---|---|---|---|
| **Reassign** | Yes | **Yes** — the clinician recommends who should take it | The scheduler executes the recommendation |
| **Decline** | Yes | **No** | The branch manages the placement, and it must go to a clinician other than the original |

So the pair is one decision with two levels of assistance. A clinician who knows the answer supplies
it; a clinician who does not hands the problem back. That is a useful shape for a capacity tool,
because the reassign path is already the clinician doing the tool's job by hand.

### Rapid reschedule removes the scheduler entirely

**If rapid reschedule is turned on in HCHB, a reschedule inside the week generates no scheduler
workflow at all.** The clinician moves the visit and nobody else touches it. Noted under the
Reschedule block on the sheet.

This is a configuration flag, not a process fact, which makes it a branch-by-branch variable: the
same disposition costs the scheduler nothing in one branch and a queue item in the next. Added to the
variable backlog.

**Canvas is now 2200 × 1680.** The disposition band grew to hold the per-disposition notes and the
Reassign/Decline statement, and the spine into Accept routes down the left of the band so it clears
the timing note.

---

## 18. Flow 3 drawn — authorization at its two interfaces

Flow 3 exists. It was the largest gap in the set: the original swimlane gave *Insurance & Auth* a
colour in the legend and not one block on the sheet.

Drawn to **DE-06** — auth is mapped only where it meets scheduling, not as a map of the auth team's
internal work. That constraint is what makes the sheet simple, and it is stated in the footer so
nobody reads the omission as an oversight.

### The organising idea: auth is two different things

The sheet's whole structure is one claim — **auth touches scheduling twice, and it behaves
differently each time.**

| | Interface 1 · at start of care | Interface 2 · inside the plan of care |
|---|---|---|
| What auth is | A **gate** | A **ceiling** |
| What it controls | Whether anything can be scheduled at all | How many visits may be delivered |
| Who feels it | Intake and the scheduler | The clinician, the DCS and the scheduler |
| Failure mode | The referral sits, unschedulable | The visit sits, invisible |

### Interface 1 — the gate

Referral arrives → intake receives in Commure → eligibility and benefits verified → pending auth
keyed → back to intake for final approval → DCS reviews the referral → scheduler books the SOC and
the discipline evals. The band is captioned `NOTHING SCHEDULES UNTIL THIS CLEARS`.

Two things are drawn that the old map never showed:

- **The visit count is set by the payer, not by need** — 1, 3, 5 or 10 visits, keyed before anyone
  has seen the patient.
- **Traditional Medicare bypasses the auth team entirely**, drawn as a dashed line that leaves the
  spine after intake and rejoins at final approval. Any other payer takes the long way round.

Under the band, the quote that names the cost: *"We know we have the referral, but it is just not in
my workflow to schedule yet — it is stuck in auth."*

### Interface 2 — the ceiling

Clinician writes the discipline frequency → DCS reviews and approves the plan of care → **auth on
file for these visits?** (a gate, asked per visit and answered by HCHB silently) → scheduler assigns
the authorised visits → visits consume the authorised count → cap approached, re-auth requested with
supporting documentation.

The no-branch drops to its own strip: **NO AUTH — the visit sits pending.** Not on the clinician's
calendar, not counted toward productivity, living in the scheduler's head or on a sticky note.

The whole band sits inside a dashed loop, because it is a loop: *every add-on order, recertification
and resumption of care re-enters it — and each one is a new auth question.*

### The panel: what the payer has already decided

Two columns. The left one carries the real caps — UHC's 5 nursing visits with 4 of 5 completed plus
documentation before visit 6; Indiana Medicaid's 8 visits shared across PT, OT and ST, paid 30 days
from the discharge date rather than the admit date; Ohio Medicaid similar.

The right column separates two ceilings that get conflated constantly:

> **Auth is permission** — how many visits the payer will allow.
> **PDGM is payment** — the economic band for the period.
> LUPA is the floor; utilisation management is the ceiling. **A visit can be authorised and still be
> uneconomic.**

Beneath it, the argument this flow exists to make: *the data already exists.* The auth team writes
the payer's rules into a coordination note at verification, days before anyone writes the plan of
care. Surfacing those rules **at plan-of-care creation** is the highest-value, lowest-complexity win
in this flow — and a patient-care win, because abrupt discharges happen when nobody planned for the
real visit budget.

### Where it breaks

Pending-auth visits are invisible · roughly 50 pending-auth workflows a day per scheduler, which
trains bulk-clearing without reading · plans of care ignore payer limits, then the team is surprised
· abrupt discharge when the visit budget quietly runs out.

**Canvas 2200 × 1540.** Same conventions as flows 2 and 4: role colour, band per phase, sublists
under each step, boundaries strip, named breaks.

**Remaining:** Flow 1 (SOC / ROC / recert / add-on), whose spine is already drawn inside the
DCS/scheduler practice map, then Flow 4 (exception and recovery), then the composite.

---

## 19. Composite build rules — carry these or the composite lies

Recorded 18 Aug, before any composite is attempted.

### The composite is CURRENT STATE

Every block must describe what happens today, including the parts that are wasteful, manual or
plainly wrong. Nothing on the composite is a proposal. The recolours below exist for exactly this
reason: they correct **who actually does the work**, not who ought to.

| Block | Drawn as | Must be | Why |
|---|---|---|---|
| PCC completes clinician scheduling workflow | purple (system) | **yellow — PCC/Scheduler** | A person does this, not HCHB |
| Read open capacity — day · week · discipline · territory | purple (system) | **yellow — PCC/Scheduler** | Same |
| Day-before confirm | purple (system) | **blue — Clinician** | The clinician makes that call, on their own time |
| All PCC in-system workflow steps | purple | **yellow** | A workflow item in HCHB is still a person clearing a queue |

The pattern behind all four: **the original map coloured a step purple whenever it happened inside
HCHB.** That conflates the system with the person operating it, and it systematically hides human
labour — which is the exact labour a capacity tool would relieve. Purple is reserved for what HCHB
does *by itself*: generating tasks, applying rules, checking auth, suggesting a route.

### Still open — the patient lane

The original sheet has a green Patient lane holding *caregiver present · window · day-of-week*.
Flow 2 draws those same facts as **constraints inside the clinician's steps**, not as patient
actions. Both cannot be right on one composite. The choice is:

- **Keep the green lane** — the patient is an actor who imposes constraints, and Flow 2 gets a
  patient lane retro-fitted; or
- **Drop the lane** — patient constraints are attributes of the visit, carried by whichever actor is
  holding it, and the composite drops green.

Flow 2's HARD/SOFT panel is the argument for the second reading: the constraint matters at the
moment the clinician negotiates it, not as a step the patient performs. **Unresolved — decide before
the composite.**

---

## 20. The eight answers — 18 Aug

Every open question from §19 is now closed. These are source facts, not inference.

### 1. The 485 is not a step, it is a moment

**485 submission happens alongside QA acceptance, plan-of-care locking, and orders being finalised
and sent to the MD for signature.** Four things, concurrently, not four gates in sequence.

This resolves the disagreement between our own sheets. Flow 2 drew "485 submitted" as a boundary and
Flow 3 drew DCS approval separately; both were describing parts of the same event. On the primary map
it is drawn as **one block carrying four lines**, badged *all at once*.

### 2. There is no patient lane — the green lane is retired

Patient preferences live as a **coordination note in the system**, holding generalised preferences.
They are **variables the clinician navigates when scheduling**, not actions a patient performs.

Flow 2's reading was right. The composite drops green, and patient constraints stay where Flow 2 put
them — inside the clinician's steps and in the HARD/SOFT panel.

### 3. The SOC welcome call is the scheduler's real decision

**The scheduler performs the SOC welcome / intake call before assigning the SOC and the attached
discipline evals.** Its purpose is concrete: confirm the patient is actually home, so clinicians are
not assigned to a patient who is still inpatient, or who is refusing home-health admission until a
later date.

This is the one judgment call in the scheduler's day, and no version of the map has ever drawn it. It
now sits on the spine, badged.

### 4. Per diem and float are a capacity instrument

They are clinicians in the workforce pool who are **deliberately not assigned to a territory**, which
is what makes them useful. They are tools for **targeted capacity management**, used two ways:

- **Take the SOCs** — absorbing the admission spike directly, or
- **Take coverage visits** — freeing a territory clinician so the branch can accept more referrals.

So float is not an exception path. It is a lever pulled on purpose, and it belongs beside the
capacity decision rather than in the recovery chain.

### 5. Branch leadership has exactly one home

Confirmed: the joint-leadership block is the only spot. It is tied to **territory alignment** and to
**referral and capacity acceptance decisions when capacity starts to get tight** — the same moment
the float lever gets pulled. The two sit together on the map.

### 6. Recert visits are already on the calendar

**Recertification and secondary discipline eval visits happen inside the 5-day recert window at the
end of the episode, and they are already plotted as part of the original plan-of-care assignment.**
They can also arrive mid-episode by add-on order, when progress is slower than anticipated and more
home health is indicated.

**That decision is discipline-dependent** — some services discharge before recertification while
others continue, based on whether goals were met.

The scheduling workflow fires **after** the recertifying disciplines establish frequency orders for
the next 60-day certification period. So the recert visit needs no scheduling; the *next period* does.

### 7. Discharge is per-discipline, and the last one out does the OASIS

Each discipline discharges **separately** from the others. The disciplines that finish first perform
**discipline discharges (non-OASIS)**. The **last discipline active on the case performs the agency
discharge with the D/C OASIS** — RN, PT, OT, whoever makes the final visit with the patient.

That is why discharge has never fitted on the primary map: it is not an event, it is a staggered
sequence whose owner is not known until it happens.

### 8. What to build

- **Now:** an updated version of the initial flow map, with every correction applied.
- **Next:** recertification and discharge as **their own flow**, so the primary map can carry them
  condensed. Their complexity is exactly what has been muddying the end of the primary map.

**Where discharge is visualised, answered:** condensed to a single strand at the end of the primary
map — *recert or discharge*, with the loop back into a new certification period drawn — and expanded
in full on its own sheet. Anything more on the primary map buries the spine under a per-discipline
sequence that only matters once the episode is ending.

---

## 21. The primary map, redrawn

`Primary-Flow-Map.pdf` — *The Episode, End to End*. Canvas 2450 × 1970. Four phases on one spine,
with everything from §4's correction inventory applied and every answer from §20 built in.

### The four phases

| Phase | What it covers | The band's claim |
|---|---|---|
| 1 · Referral to admission | Intake → auth → intake approval → DCS → **welcome call** → assign SOC and evals → clinicians perform | *Nothing schedules until auth and intake clear* |
| 2 · The plan of care is established | Frequency per discipline → DCS approval → **the 485 moment** → HCHB generates → scheduler assigns → visits land | *Plotted by frequency, assigned in one pass* |
| 3 · Steady state | The clinician's own week, condensed from Flow 2, with the five dispositions as a strip | *No scheduler workflow* |
| 4 · End of episode | Recert window → next-period frequency → scheduling workflow · **OR** · discipline discharges → agency D/C OASIS | *Condensed — detail in Flow 5* |

### What is new on this sheet

- **The welcome / intake call**, badged `THE ONE JUDGMENT CALL`. It has never been drawn. Its purpose
  is on the block: is the patient actually home, still inpatient, or deferring admission?
- **The 485 moment** as a single double-width block carrying four concurrent lines — QA accepted, POC
  locked, 485 submitted, orders to MD — badged `ALL AT ONCE`. This retires the sequence-of-gates
  reading that our own two sheets had drifted into.
- **The recertification loop**, drawn: a new certification period leaves phase 4 and re-enters phase
  2, because that is literally what happens.
- **Per diem / float and branch leadership**, together, under `PULLED ON PURPOSE WHEN CAPACITY
  TIGHTENS — not recovery, instrument`. Float is a capacity instrument, not an exception path, and
  the leadership block sits beside it because both get used at the same moment.
- **The missed-visit compliance chain** as a chain — document → notify the MD within 48 hours → DCS
  if it is late — instead of the maroon dead-end oval on the original.
- **No patient lane.** Retired per §20.2. Patient preferences appear where they actually bite, in the
  clinician's constraint step: *"preferences sit in a coordination note."*

### The reading panel

Two columns, because a composite gets read by people who were not in the room.

- **Three different ceilings on one episode** — auth is permission, LUPA is the floor, utilisation
  management is the ceiling.
- **What this map is** — current state including the waste; colour is the actor and purple appears
  only where HCHB acts by itself; the detail flows sit behind the condensed steps.

The footer repeats it: *nothing on this sheet is a proposal.*

### Band widths follow content

Each band ends just past its last block rather than running to a common right edge, so phases 3 and 4
do not read as half-empty. Same type scale and conventions as flows 2 and 3.

**Next:** Flow 5 — recertification and discharge — which is the strand phase 4 condenses.

### Correction, 18 Aug — phase 2's claim

"One task per discipline, twice" was wrong. The scheduler assigns **all plotted visits in one
pass** — one working of the assignment task covers every visit the frequency generates
(frequency × weeks of the period). The per-discipline duplication is real but lives on the
plan-of-care workflow side (a task per discipline at submission and again at approval), not on the
assignment side. The band now reads **PLOTTED BY FREQUENCY · ASSIGNED IN ONE PASS**, the scheduler
block reads "assigns all plotted visits — one pass", and the HCHB block notes that frequency becomes
many visits under a single assignment task per discipline.

---

## 22. Flow 1 drawn — the full SOC/ROC flow

`Flow-SOC-Full.pdf` — *Start of Care — the Full Flow*. Canvas 2600 × 1620. This is the flow the team
worked with in the meeting, in the same two-pass shape as the practice map, with every correction
since then built in.

**Pass 1 (from the referral):** intake receives in Commure → auth verifies and keys pending auth →
intake final approval → DCS reviews → **the welcome / intake call** (badged, with its purpose) →
scheduler books SOC/ROC and discipline evals → clinicians perform. Banded *nothing schedules until
auth and intake clear*.

**Pass 2 (the repeating pattern, per discipline):** clinician submits POC → DCS reviews & approves →
Approved? → **THE 485 MOMENT** (QA accepted · POC locked · 485 submitted · orders to MD, `ALL AT
ONCE`) → visits generate in HCHB → Auth on file? → **scheduler assigns all plotted visits — one
pass** (noted: one working of the task assigns every visit the frequency generates) → visits on the
clinician's calendar.

Recertification and add-on orders enter pass 2 directly on the bus, as before. Exceptions (QA
backlog, returned to clinician, pending auth), the episode visit budget panel and the missed-visit
compliance chain all carry over from the practice map.

**What changed relative to the practice map:** the welcome call exists; the 485 is one moment between
approval and visit generation; assignment language corrected to one pass per discipline task.

The practice map (`Flow-DCS-Scheduler.pdf`) remains as the simplified DCS/scheduler teaching sheet.

**Next: Flow 5 — recertification and discharge.**

---

## 23. The detailed flow, redrawn in the original's design

`Detailed-Flow-Composite.pdf` — the sheet the team already knows how to read, corrected. Canvas
2600 × 1780, ratio ≈ 1.46, matching the original's proportions. Same skeleton: five outlined
functional columns (Clinician Scheduling Workflow · Capacity Read · Scheduling & Assignment ·
Coordination · Delivery & Outcomes), the grey **clean path** running through the middle from the
admitted referral to the delivered visit, feeders above the spine, recovery below, centred title,
circle legend.

### Corrections carried onto the original design

| Where | Was | Now |
|---|---|---|
| Spine: PCC completes clinician scheduling workflow | purple | **yellow** — a person works it |
| Spine: Read open capacity | purple | **yellow** |
| Spine: Assign visit | yellow | yellow, labelled **one pass** |
| Spine: Day-before confirm | purple | **blue — by the clinician**, on their own time |
| Patient rules block (col 3) | green, a patient lane | **purple — a coordination note**, badged `WAS A PATIENT LANE` |
| Readiness call (col 1) | plain yellow | badged `THE ONE JUDGMENT CALL`, with its question |
| ED/DCS review (col 2) | maroon | **black — branch leadership review**, badged `WHEN CAPACITY TIGHTENS`, noted territory alignment · referral acceptance |
| Engage per-diem/float (col 2) | plain | noted **no territory, on purpose — the targeted capacity instrument** |
| Insurance & Auth | a legend colour with zero blocks | **two orange blocks** — pending-auth invisible (distorting the capacity read, "the read excludes what it cannot see") and the per-visit auth gate |
| Five dispositions | missing entirely | chip strip in Coordination, day before, selected in HCHB |
| Reschedule → re-slot | purple | **yellow**, badged `RAPID RESCHEDULE`, noted *no scheduler workflow at all if the flag is on* |
| Missed — unworked (dead-end oval) | terminus | **the compliance chain**: missed visit documented → scheduler notifies MD within 48h → late → DCS workflow |
| Visit states | "delivered" as trigger | *scheduled → documentation pending → missed*, with the Citrix sync lag noted under EVV |
| Routing/GPS feeder | plain | noted **straight-line today — not drive time** |

The KPI feedback loop and the priority-to-scheduling line both survive, re-routed along the bottom
lane. Footer states the reading rule: *colour = actor; a workflow item in HCHB worked by a person
carries the person's colour.*

This sheet supersedes nothing — it IS the redrawn original (page 2 of the set; page 1 remains the
Home Health Intake Reset). The four detail flows stand behind it.

---

## 24. Flow 5 drawn — recertification and discharge, through a worked example

`Flow-Recert-Discharge.pdf` — the last of the detail flows. Canvas 2200 × 1720. This is the flow the
primary map condenses as phase 4, and it is built around a **worked example** rather than an abstract
sequence, because the per-discipline staggering is exactly what abstract boxes fail to convey.

### The example (18 Aug, source: PB)

SN, PT and OT are all active on the case.

| Discipline | Decision | When | Visit type | Next period |
|---|---|---|---|---|
| **SN** | Discharge | **Days 52–53** — 7–8 days before the period ends | **Discipline discharge, non-OASIS** | Off the case |
| **PT** | Recertify | Inside the 5-day window (days 56–60) | **OASIS recert visit** — PT carries the OASIS | **2w3, then 1w3** — 6 + 3 = 9 visits over 6 weeks |
| **OT** | Recertify | Inside the 5-day window | **OT recert eval — non-OASIS** | **1w4** — 4 visits over 4 weeks |

SN's timing is the teaching point: **a discipline that is not recertifying owes no visit inside the
recert window.** It makes its final visit whenever clinically sensible and leaves. Only the
recertifying disciplines are bound to the window — and their window visits were already plotted at
the original plan of care, so nothing needs scheduling to make them happen.

### How the sheet is built

- **Band 1 — the decision.** Each active discipline, separately, against its own goals: goals met →
  discipline discharge (non-OASIS); more care indicated → recertify with a visit inside the window.
  Side notes carry the discipline-dependence and the mid-episode add-on escape hatch (Flow 1).
- **Band 2 — the timeline.** A 60-day bar with days 1–50 compressed behind a break mark and days
  51–60 drawn at width (labelled *window expanded — not to scale*), the 5-day window shaded, a heavy
  dashed **DAY 60 → DAY 1** boundary, and the new period's bar beyond it. Three lanes: SN's block at
  days 52–53 ending in an open circle (off the case); PT's OASIS recert visit badged `CARRIES THE
  OASIS`; OT's non-OASIS eval. PT and OT's lanes cross the boundary into their frequency chips.
- **Band 3 — the workflow.** PT and OT establish next-period frequency orders (× 2 disciplines) →
  DCS approves each POC → HCHB generates visits and assignment tasks → scheduler assigns all plotted
  visits in one pass → the new period's visits land. Banded `THE SAME PATTERN AS FLOW 1, PASS 2` —
  recert is not a new process, it is a trigger into the existing one, and the scheduling workflow
  fires **only after** the frequency orders exist.
- **The agency-discharge panel.** If no discipline recertifies: every discipline still discharges
  separately (the earlier ones non-OASIS, exactly like SN above); the last discipline active performs
  the agency discharge with the D/C OASIS — RN, PT or OT, whoever makes the final visit; the owner is
  unknown until it happens, and the episode's capacity returns to the branch.

**The flow set is complete**: the detailed composite (original design, corrected), the primary map
(four phases), and detail flows 1 (SOC full), 2 (routine visits), 3 (authorization), 5 (recert &
discharge), plus the DCS/scheduler practice sheet. Flow 4 (exception & recovery) remains available
as a future sheet if the missed-visit/call-out/Citrix material ever needs its own page — today it
lives distributed across the composite and flows 1–2.

### Auth added to Flow 5 (18 Aug, same day)

The workflow band now carries the **auth gate**, exactly as Flow 3 defines it: HCHB generates the
new period's visits → **Auth on file?** (per visit) → yes, the scheduler assigns in one pass; no, the
visit drops to the orange strip — *sitting pending, not on the calendar, not counted*. The band's
closing line states the reason the gate belongs on this sheet: **a new certification period is a new
auth question** — traditional Medicare passes straight through, any other payer re-enters the auth
cycle (Flow 3) before the recert visits can be assigned. Insurance & Auth joined the sheet's legend.
Canvas grew to 2200 × 1800.

---

## 25. Second correction pass on the composite — 18 Aug

Four corrections from PB's review of the redrawn sheet, all applied:

1. **"from Intake Reset" deleted.** The entry arrow and caption confused more than they oriented.
   The clean path now simply begins at the PCC block.
2. **"Normalize demand → points & timing windows" deleted.** HCHB does not normalize demand — the
   block was an invention. The spine drops straight to the priority question. And the question is
   reworded: **"SOC / ROC urgent?"**, not "time-sensitive?", because *every* SOC/ROC is
   time-sensitive — seen within 48 hours under Medicare guidelines. Urgent means a clinical
   diagnosis or another factor deserving a priority flag. The note under the block says exactly that.
3. **The matching steps are the scheduler's, not the system's.** Specialty competency, continuity,
   and reading the patient-preferences coordination note are all yellow now: the information is
   housed in HCHB, but a person wrote it and the scheduler acts on it before selecting a clinician.
   Only the discipline/role match stays purple, as a genuine HCHB hard gate. **Territory list — zip
   code reference** added to the chain as a scheduler task, between the role gate and specialty
   matching.
4. **HCHB does not send reminders.** The Coordination column's purple "Reminders sent" is gone.
   The chain is now the clinician's: **Visit confirmation coordination (SMS / voice) — day before**
   (blue) → patient confirms / negotiates (green) → into the Confirmed? diamond. The separate
   "day-before confirm" spine block is removed — the confirmation chain *is* the day-before work,
   and it feeds the spine's Confirmed? decision directly.

---

## 26. Third correction pass on the composite — the confirmation outcome and call-out coverage

1. **Accept moved onto the spine.** A confirmed visit *is* an accepted visit: the Accept pill now
   sits on the Yes segment between **Confirmed?** and **Visit delivered**, and the disposition strip
   below carries only the other four. Its heading reads **NOT CONFIRMED — THE OTHER DISPOSITIONS**.
2. **The No branch points at Resched.**, the most likely outcome — not at Decline, which is the
   least used disposition and one some clinicians are instructed never to use. Both facts are now on
   the sheet, and "negotiate" is dropped from the label.
3. **Call-out coverage is jointly owned** — the block is half maroon (DCS), half yellow (scheduler).
4. **The coverage chain is the scheduler's:** *Scheduler coordinates coverage — call · text · Teams —
   with FT or per-diem clinicians* → *Scheduler reassigns to another clinician — or moves the visit
   to another day*. The `RAPID RESCHEDULE` badge and its note are removed from this chain — rapid
   reschedule is about clinicians moving their **own** visits, not about coverage — and the care
   coordination / case conference block is deleted.

**Note for the other sheets:** rapid reschedule remains correctly placed on Flow 2 (the clinician's
own week) and in the variable backlog; it was only wrong here, attached to call-out coverage.

### Same correction applied to the primary map (18 Aug)

Phase 3's disposition strip now matches the composite: **Accept stands apart as the confirmed
path** (*confirmed → accepted*), and the remaining four chips sit behind a `NOT CONFIRMED →` label
with the note *reassign returns with a plan, decline without one — decline is the least used*.

## 27. Payer economics drawn — the eighth sheet, 19 Aug

The first sheet in the set that is not a workflow. It maps **consequence** rather than sequence:
the same operational event, priced differently in every payer class. It was drawn because the
variable inventory carried no payer dimension, and because the episode economics research turned up
facts that change what a scheduling decision means.

**The organising claim.** Four ceilings act on one episode and the current model conflates them —
**permission** is what the payer allows, **floor** is LUPA, **ceiling** is the flat zone above the
floor where visits earn nothing, and **cap** is the annual benefit limit on non-episodic payers. A
visit can be authorised and still be uneconomic. The panel states the four as independent tests.

**Five bands, each a divergence point.**

1. *Referral to schedulable* — the gate is payer-dependent. The auth block carries a `NON-MEDICARE`
   badge and the sublist *traditional Medicare skips this*, rather than a bypass connector: the
   book is majority non-traditional-Medicare, so routing the spine through auth **is** the common
   case, and a bypass line around it would have argued the opposite.
2. *Plan of care* — the grey feeder in the left margin carries the highest-value fact on the sheet:
   the payer rule already exists, in a coordination note written days earlier, and it does not
   surface here. Dashed, because it is reference data nobody reads at this moment, not an input the
   process consumes.
3. *What a delivered visit is worth* — one clinician block, then five white payment-state chips.
   No arrow from the block into the chips: they are alternative values, not a next step. White with
   an ink outline per the convention that outcomes carry no actor colour, with a margin note saying
   so, since this is the first sheet where a reader meets several of them at once.
4. *The missed visit* — the compliance chain, then four value chips. The 100× swing between
   ~25 dollars mid-period and 1,258–1,386 dollars floor-critical is the single most decision-
   relevant number on the sheet.
5. *Period and window end* — a new certification period is a new authorisation question **and** a
   new case-mix group with a new floor.

**Corrections made against the rendered PNG.** Bands 3 and 5 were first drawn at the height of a
band with sublists and read half-empty once the chips replaced them; both were sized down to their
own content and the sheet lost 70 points of height. The payment-state note was added after the
first render, where five white chips appeared with nothing saying why they were not actors.

**Build note.** `assets/build.py` requires playwright and a Linux Chromium path, so the sheet was
rendered with `assets/build_win.py`, a sibling shim that drives installed Chrome via its CLI. Same
arguments, same wrapper, same one-page PDF at canvas size. Chrome refuses to write into the session
temp tree — build in an ordinary directory.

**What this sheet is not.** It is current state, like the rest of the set. It shows what a payer
does to the schedule today, including the parts nobody can see. Nothing on it is a proposal, and
the margin figures are shown to make a consequence visible, never to argue for a visit.

## 28. The episode scenario sheets — and the first target-state material, 2 Sep

Three sheets from one generator: current state, target state, and both side by side. They follow a
single referral from Friday afternoon to the close of the first payment period, and they exist
because the business case levers read as eight separate initiatives when listed and as one problem
when placed on a timeline.

**The organising claim.** Four points where money leaves, and they are the same failure each time:
a deadline nobody can see until it has passed. Two admitting slots expire before the patient is
ready. The plan of care is written blind to the payer budget and the visit floor. A cancellation
leaves a gap the branch cannot fill inside the day. The period closes below the floor with a
reassessment window missed.

**On the narrative.** These are representative composites assembled from patterns documented in the
discovery and whiteboard sessions and from the operator's own account: the Sunday deferral pattern,
hospital discharges slipping, the clinician who shifted visits to her assistant for an admission
where nobody had confirmed the patient was home. They are **not** named cases and the footer says
so. Presenting an invented specific as an audited fact would not survive the first executive who
asks which branch.

**The target-state sheet breaks the set's standing rule deliberately.** Every other sheet carries
*nothing on this sheet is a proposal*. This one carries the opposite, in capitals, because it is the
first proposal material in the repository and the two must never be confused. The rule was not
relaxed; it was inverted and labelled.

**What the target sheet deliberately does not claim.** The patient still defers to Monday. The
system does not change patient behaviour, and a sheet implying otherwise would be dismissed by
anyone who has run a branch. What changes is that the released Saturday and Sunday slots reach
waiting admissions the same morning, instead of expiring.

**Conventions.** Outcome states are white ovals with an ink outline, never actor-coloured — the
terminal states in bands 3 and 4 were actor-coloured in the first draft, which wrongly implied HCHB
was acting when a period reprices. The consequence chips are white with an ink outline and carry
their headline in a non-actor accent, brick for loss and green for gain; the outlines stay neutral
so they cannot be read as a new actor colour.

**On the combined sheet.** 4300 x 1830, a ratio of 2.35, outside the 1.25 to 1.5 guidance. That was
tested rather than assumed: at that width both states fit at full type size with no narrative
removed. Reducing the canvas to a normal ratio would have required cutting a step from each band,
which was the one thing the operator ruled out. The trade is aspect ratio, not legibility. Use the
pair for reading and slides, the comparison for the wall.

**Build note.** `assets/build.py` needs playwright and a Linux Chromium path; on Windows use
`assets/build_win.py`, which drives installed Chrome and takes the same arguments.

## 29. The scenario set completed — four families, twelve sheets, 2 Sep

The episode sheet demonstrated four of the nine value levers. Three more families were added so the
set covers all nine, each family drawn current state, target state, and side by side.

**Why four families rather than one longer sheet.** Each lever has a natural unit of time, and a
sheet that mixes them stops being readable. Admission throughput and the episode deadlines live on
*one patient's episode*. Assessment capacity, retention and travel live on *one clinician's week*.
Administrative cost and premium labor live on *one branch's week*. The weekend effect needs
*Friday to the following Friday*. Forcing all nine onto one timeline would have required the wrong
unit of time for at least six of them.

| Family | Unit of time | Levers |
|---|---|---|
| One referral, one episode | A patient's episode | 1, 3, 4, 5 |
| One clinician's week | Monday to Friday, one nurse | 2, 3, 8, 9 |
| One branch's week | Monday to Friday, one branch | 1, 2, 6, 7 |
| The weekend cascade | Friday to the following Friday | 1, in depth |

**Every sheet now carries a coverage strip** naming its levers. On a wall this tells a reader which
sheet answers which question, and stops any single sheet being mistaken for the whole case.

**A shared kit was extracted.** `_scenario_kit.py` holds the shell — masthead, legend, band loop,
outcome chips, summary panel, coverage strip — and each family is content plus a call. Four copies
of the drawing code would have drifted within a week.

**What the target sheets deliberately refuse to claim.** The patient still defers to Monday on the
episode sheet. The family still defers on the weekend sheet. The clinician still calls out on the
branch sheet. No target sheet claims the system changes what patients or clinicians decide; each
changes only what the branch can see and how quickly it can respond. A sheet claiming otherwise
would be dismissed by anyone who has run a branch, and rightly.

**On the branch sheet's fourth band.** It ends on "the week looks fine" — every number defensible,
every loss invisible. That is the sharpest frame in the set for why measurement precedes any
platform decision, and it is the honest reason the initiative cannot be sized today.
