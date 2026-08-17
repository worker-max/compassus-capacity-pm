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
