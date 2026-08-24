# Day-Before Confirmation — the variable map

> **What this is.** Everything that has to be considered when an assistant confirms tomorrow's visits,
> drawn from the project's own knowledge base rather than from generic scheduling theory. Three parts:
> **(A)** the variables that already exist and are scored, **(B)** the constraints that gate the
> sequence, **(C)** the variables the operator's specification opens that **do not exist in the
> inventory yet.**
>
> **Companion:** [`day-before-confirmation-protocol.md`](./day-before-confirmation-protocol.md) — the
> operator's specification this map serves.
>
> **Source of truth is the workbook.** IDs, constraint classes, MVP flags and automation postures in
> Part A are quoted from the `Variable Inventory` tab of the 8.13 workbook (via
> [`../knowledge/workbook-2026-08-13.md`](../knowledge/workbook-2026-08-13.md) and the CSV export). If
> the workbook changes, change this file — never the other way round.

## How to read the columns

- **Constraint** — Hard = the visit fails if it is not honoured · Soft = optimise toward it, bend under
  pressure · Structural = a fixed fact · Derived = computed · Config = policy-set · Event = a trigger.
- **Posture** — **Control** = the system may decide and act · **Assist** = it proposes, a person confirms ·
  **Read** = it surfaces only, a person decides. **Read is not weakness; it is a boundary.** Every `Read`
  row below is a place where an assistant that decides would do harm.
- **MVP** — day-one must-have for the software (Yes / Maybe / No).

**One standing caveat: `DE-03` — Phase 1 is visualisation only.** These postures describe the target, not
release 1.

---

# Part A — variables already in the inventory

## A1. The anchor — the sequence itself

| ID | Variable | Constraint | MVP | Posture | What it means here |
|---|---|---|---|---|---|
| `CO-01` | **Day-before / same-day visit confirmation** | Soft | Yes | **Assist** | The protocol *is* this row. Workbook note: *"the call can surface changes, so prompt and let a person confirm"* — *"the human touch catches what a reminder can't — assist, don't fully automate"* |
| `CO-02` | Automated appointment reminders | Soft | Yes | **Control** | The one clean automation win in the band. A reminder is deterministic. **A reminder is not a confirmation** — do not let the protocol collapse the two |
| `CO-05` | **Communication channel & preference management** | Soft | Maybe | **Assist** | The channel choice of §2. Currently scored `Maybe` — the operator's specification promotes it to a must-have **at two scopes**, which the row does not model |
| `CO-06` | Availability confirmation before booking | Hard | Yes | **Read** | *"Depends on fluctuating patient and caregiver windows; surface, a person owns it"* |
| `CO-07` | Reschedule coordination | Soft | Maybe | **Read** | *"Relational negotiation; the system can propose slots, a person owns the outcome"* — the ceiling on how far the assistant may go when the patient says no |
| `CO-03` | En-route / on-my-way notification | Soft | Maybe | **Control** | Downstream of this sequence, but it is what an arrival window makes credible |
| `CO-08` | Failed-visit / no-show follow-up & rebooking | Hard | Yes | **Assist** | Where the sequence goes when it fails |
| `CO-12` | Coordination time load | Derived | Maybe | **Read** | The capacity cost of the confirmation work. **This is the ROI meter for the whole protocol** — measure it before, or the benefit is unprovable |

## A2. The window and the clock

| ID | Variable | Constraint | MVP | Posture | What it means here |
|---|---|---|---|---|---|
| `S-20` | **Appointment window (time of day)** | Hard/Soft | Yes | **Assist** | The arrival window. Workbook note: *"standardizing this concept can have significant impact on patient satisfaction and overall clinical team efficiency"* — and *"enforceable once captured; capture is where reality leaks in"* |
| `S-02` | Visit type | Hard | Yes | Control | Drives visit duration — **the input the window cascade needs and the inventory does not carry in minutes** (see C, `E-06`) |
| `S-03` | Ordered-frequency compliance window | Hard | Yes | Control | A reschedule can break it |
| `S-35` | SOC timing window | Hard | Yes | Control | 48-hour regulatory clock |
| `S-36` | Recert / face-to-face window | Hard | Yes | Control | Days 56–60; binds only recertifying disciplines |
| `S-37` | Supervisory visit dependency | Hard | Yes | Control | Cadence dependency a reschedule can violate |
| `SH-07` | Productivity points per visit type | Config | Yes | Control | **A weighting, not a duration.** Do not compute arrival windows from points |

## A3. The clinician's own pattern — the autonomy zone

**Read the postures in this block before designing anything that touches them.** Four of the eight are
`Read` or `Low` confidence, and they are the rows the operator's autonomy requirement (§4.3) is protecting.

| ID | Variable | Constraint | MVP | Posture | What it means here |
|---|---|---|---|---|---|
| `S-05` | Preferred start time | Soft | Maybe | **Assist** | The day-start input of §4.2. Workbook note: *"Preferred vs Possible are 2 different things. Many clinicians struggle with scheduling 1st visit of day 8am/9am even if they want to. Requires very strategic planning and motivating patients"* |
| `S-06` | Start-time flexibility | Soft | Maybe | **Read** | *"a wrong assumption damages trust"* |
| `S-07` | **Lunch / documentation pattern** | Soft | Maybe | **Assist** | The inter-visit gaps of §4.3 |
| `S-08` | Mid-day documentation block | Soft | Maybe | **Assist** | Same |
| `S-09` | Split-shift / mid-day personal break | Soft | Maybe | **Read** | *"the clinician's own daily rhythm — a strange attractor; small control inputs distort it"* |
| `S-10` | Preferred end time / hard stop | Hard/Soft | Yes | **Assist** | *"Firm once known, but knowing it depends on the clinician telling you"* — the cascade must respect it |
| `S-11` | Max consecutive visits / daily volume | Soft | Maybe | Assist | The ceiling on a day the grid can build |
| `S-12` | Elasticity / willingness to flex | Soft | Maybe | **Read** | *"the act of automating it changes what it measures"* |
| `S-13` | Overtime / extra-visit willingness | Soft | Maybe | **Read** | *"surface, never presume"* |
| `S-04` | Preferred working days | Soft | Maybe | Assist | Rotations and swaps are informal |
| `SH-05` | Approved time off / availability | Hard | Yes | Control | A firm blackout |

## A4. Route, geography and sequence

| ID | Variable | Constraint | MVP | Posture | What it means here |
|---|---|---|---|---|---|
| `S-14` | Home base (start/end location) | Structural | Yes | Control | Where the day starts — slot one's drive time comes from here |
| `S-17` | Proximity to existing route | Soft | Maybe | Control | The recommendation basis of §4.1. *"Geometry — safe optimization"* |
| `S-18` | Optimized-route mileage | Derived | Yes | Control | Deterministic routing math |
| `S-19` | **Intra-day sequencing** | Soft | Maybe | **Assist** | The drag-to-reorder of §4.2. *"Legible skeleton pinned by tacit anchors; propose, let the human place the anchors"* — an exact description of the interface the operator specified |
| `C-03` | Clinician territory assignment (zip) | Structural | Yes | Assist | Bounds who can be on the day at all |
| `SH-06` | Territory / service area | Structural | Yes | Assist | Same |

## A5. What the patient brings — the pushback taxonomy

The day-before negotiation panel splits patient pushback into **HARD** (accept it, build around it) and
**SOFT** (negotiable, worth holding the line on). The inventory rows underneath that split:

**HARD — the assistant accepts and reschedules**

| ID | Variable | Constraint | MVP | Posture | Note |
|---|---|---|---|---|---|
| `S-27` | Day-of-week constraint | Hard | Yes | Assist | Standing commitments; *"patient-reported, so trust but verify"* |
| `S-32` | Competing medical appointments | Hard | Yes | Assist | *"surfaces in conversation, not the record"* — a large share of what this sequence will actually discover |
| `S-28` | **Caregiver-present requirement** | Hard | Yes | **Read** | *"Danger quadrant — hard rule, fluctuating tacit input, patient harm. The clearest 'read, never control'"* |
| `S-29` | Cognitive / dementia constraint | Hard | Yes | **Read** | *"system surfaces, a person decides"* |
| `S-30` | Caregiver schedule / fluctuating availability | Hard | Yes | **Read** | *"two moving calendars, undocumented — the purest sensitive dependence in the system"* |
| `S-31` | Diagnosis-driven timing | Hard | Yes | **Read** | *"clinical judgment with patient harm; flag, never decide"* |
| `S-34` | Infection-control sequencing | Soft | Maybe | Assist | Constrains order, not just time |
| `S-21` | Clinician restrictions | Hard | Yes | Control | Documented firm restriction |

**SOFT — the assistant may hold the line, with the clinician's authority**

| ID | Variable | Constraint | MVP | Posture | Note |
|---|---|---|---|---|---|
| `S-25` | **Time-of-day refusal** | Soft | Yes | **Assist** | Downgraded Hard → Soft on 8.13. Operator note on the row: *"in my years of experience, this preference is malleable based on relationship"* — **this row is the reason the negotiation-context field of §5.2 exists** |
| `S-26` | Preferred visit window | Soft | Maybe | Assist | *"optimize toward, confirm"* |
| `S-22` | Continuity of care | Soft | Maybe | Assist | *"the relationship is load-bearing but invisible in the data; protect it, don't score it away"* |
| `S-24` | Language / cultural match | Soft | Maybe | Assist | Also a channel question — a text in the wrong language is not a contact |
| `S-23` | Gender preference | Hard/Soft | No | Assist | *"sensitive; surface and confirm"* |

## A6. Where the sequence lands

| ID | Variable | Constraint | MVP | Posture | What it means here |
|---|---|---|---|---|---|
| `S-38` | Missed / unworked visit rescheduling | Hard | Yes | **Assist** | *"Detecting the miss is straightforward; choosing the reschedule pulls in every soft constraint"* |
| `S-39` | Missed-visit documentation | Config | Yes | Control | Starts the 48-hour MD clock |
| `CO-09` | Call-out coverage coordination | Hard | Yes | **Read** | Adjacent: what happens when the *clinician*, not the patient, is the problem |
| `CO-11` | Care-team / office coordination updates | Soft | Maybe | Assist | *"Notification is safe; the escalation judgment is human"* |
| `CO-10` | Multi-discipline visit coordination | Soft | Maybe | Assist | Two clinicians confirming the same patient on the same day |
| `S-41` | Pace vs. schedule | Derived | Maybe | Control | A reschedule moves it |
| `S-40` | Front-loading | Soft | Maybe | Assist | *"A target, not a law; forcing it flattens the clinician's rhythm"* |

**The disposition vocabulary is not a scored row and needs to be** — Accept · Reschedule · Reassign · Miss ·
Decline, chosen the day before in HCHB. The variable backlog carries it as *"Assignment accept / reassign /
decline **+ reason**"*, with the reason named as *"the best training signal in the process."*

## A7. The economics riding underneath — visible to the clinician, never to the patient

| ID | Variable | Layer | Posture | What it means here |
|---|---|---|---|---|
| `SH-11` | Payer class (episodic / per-visit / managed care) | Shared *(backlog)* | Control | Financial risk runs in **opposite directions** by class |
| `SH-12` / `S-45` | **Authorization state & pending-auth allowance** | Shared / Scheduling *(backlog, **ID collision unresolved**)* | Assist | **A visit with no auth is on no calendar and must not be confirmed** |
| `SH-13` | Payment period & case-mix group | Shared *(backlog)* | Control | Two 30-day periods per 60-day cert period |
| `SH-14` | **LUPA threshold** | Shared *(backlog)* | Control | The **floor**. `CN-05`: LUPA risk should surface **at the moment a visit is missed**, with remaining days shown — this sequence is that moment |
| *(TBD)* | Period utilisation against payment — the over-utilisation ceiling | Scheduling *(backlog)* | **Read** | *"show the margin consequence, never weigh it against clinical need"* |
| `S-46` | Add-on orders | Scheduling *(backlog)* | Assist | Awaiting DCS workflow |

**Three ceilings, never conflated:** auth is *permission*, LUPA is the *floor*, utilisation management is
the *ceiling*. A fourth — the annual *cap* — applies to non-episodic payers. **A visit can be authorised
and still be uneconomic.** None of this belongs in anything the patient hears.

---

# Part B — the constraints that gate the sequence

| ID | Constraint | Effect on this protocol |
|---|---|---|
| **`CN-09`** | **Text and email contact requires signed consent** — separate text, email and share-with-family consents, none usable until signed **at the SOC visit** | **Gates the entire SMS channel.** A clinician's channel preference cannot override it. Open: can consent capture move earlier, into the hospital or the Commure intake flow? |
| **`CN-10`** | **Outbound automated calling is regulated** — California treats any call not manually triggered by a human as a robocall; batch-triggered calls fall under that treatment | **The single largest open risk in the protocol.** Needs **legal** confirmation, not operational judgment. Decides whether the assistant may place the call or only prepare it |
| **`CN-11`** | **An active POA must sign admission consents**; some POAs require that the patient not be contacted at all | Contact routing is a *safety* requirement. `CN-11` says POA status must sit at the **front** of the scheduling view |
| **`CN-02`** | **OASIS visits are date-bound** and cannot be freely moved by the assigned clinician | Any reschedule path must distinguish OASIS from non-OASIS and **refuse the former** |
| **`CN-03`** | The certification period is 60 days from SOC; a visit cannot move past it | A hard boundary on every reschedule the assistant proposes |
| **`CN-04`** | **The Medicare week runs Sunday–Saturday** | Frequency is consumed against it — the week the tool reasons in is the Medicare week, not a calendar week |
| **`CN-05`** | LUPA thresholds | Surface forward-looking LUPA risk *at the miss*, with remaining days shown |
| **`CN-01`** | **MD notification of a missed visit within 48 hours** — Medicare requirement and an HCHB hard stop | A `Miss` disposition starts a clock the tool should track and prompt |
| **`CN-06`** | The plan of care requires a physician order and signature — **the clinician is the originator of frequency** | **No tool generates frequency independently.** The assistant confirms visits; it does not create them |
| **`CN-08`** | Discipline scope of practice — HCHB filters the assignable list | Scope filtering is a **correctness** requirement, not an optimisation preference |
| **`CN-12`** | Pending-auth counts vary by payer (1, 3, 5, 10) | Caps how far ahead anything can be worked |
| **`CN-17`** | Pending auth is not universally payable | The non-billable decision routes to a leader, never to the assistant |

**Decisions that bind:** `DE-09` *the tool recommends; the human accepts* · `DE-02` Patient Engagement is
its own module · `DE-03` Phase 1 is visualisation only · `DE-04` the capacity tool **is** the scheduling
grid — do not build both.

---

# Part C — what the operator's specification opens that does not exist yet

**Fourteen variables the protocol requires and the inventory does not carry.** Proposed as an
**Engagement (`E-`) block** — a fourth layer alongside Shared / Capacity / Scheduling / Coordination,
because these are properties of *the engagement*, not of a clinician, a patient or a schedule.

> **Numbering is deliberately not assigned.** The variable backlog carries an **unresolved ID collision**
> (`S-43` claimed twice; `SH-10`–`SH-14` claimed by the payer handoff). Assigning codes before that is
> settled makes the problem worse. These are proposals to be numbered when the backlog is reconciled.

| # | Proposed variable | Layer | Constraint | MVP | Posture | Why it is needed | Closest existing row |
|---|---|---|---|---|---|---|---|
| `E-01` | **Channel preference — patient standing default** | Engagement | Soft | **Yes** | Assist | §2. The per-patient default channel | `CO-05` (models one scope, not two) |
| `E-02` | **Channel override — this engagement sequence** | Engagement | Soft | **Yes** | Assist | §2. The operative requirement: one-tap change inside the flow, without rewriting the standing default | — none |
| `E-03` | **Arrival-window granularity — clinician standing rule** | Engagement | Config | **Yes** | Assist | §3.1. 1-hour vs 2-hour, held **per clinician** as a practice pattern | `S-20` (the window itself, not the rule that sets it) |
| `E-04` | **Arrival-window override — per day, per slot** | Engagement | Config | **Yes** | Assist | §3.2. Widen by **position in the day** and by **preceding visit type** (post-SOC). Set *before* the sequence runs | — none |
| `E-05` | **Day start time** | Engagement | Config | **Yes** | Assist | §4.2. The clinician's stated start; anchors slot one and the whole cascade | `S-05` (a preference, not a per-day input) |
| `E-06` | **Visit duration by visit type** | Shared | Config | **Yes** | Control | §4.2. **The cascade cannot compute without it.** `SH-07` productivity points are a *weighting*, not minutes | `SH-07` — insufficient |
| `E-07` | **Estimated drive time between consecutive stops** | Scheduling | Derived | **Yes** | Control | §4.2. Already on the backlog as *"drive-time vs. straight-line distance"* — **blocked on a routing data-source decision** | `S-18` (mileage, not time) |
| `E-08` | **Inter-visit buffer — documentation, errands, personal** | Engagement | Soft | **Yes** | **Read** | §4.3. A **placeable object on the grid**, authored by the clinician. Posture is `Read` on purpose: the system must never reclaim it | `S-07`, `S-08`, `S-09` (habits, not placed blocks) |
| `E-09` | **Clinician negotiation context, per visit** | Engagement | Soft | **Yes** | Assist | §5.2. **The centrepiece of the operator's specification** — the insider information the assistant negotiates with. Free-text, authored beside the visit | — none. Nothing in the inventory holds it |
| `E-10` | **Fallback phrase library + selection rules** | Engagement | Config | **Yes** | Control | §5.1. Stock phrases, rearrangeable, used when the patient declines | — none |
| `E-11` | **Negotiation authority — how hard to hold the line** | Engagement | Soft | **Yes** | **Read** | §5.3. Encodes HARD-accept / SOFT-hold **per visit**, granted by the clinician. Without it the assistant either caves or overreaches | `S-25`, `CO-07` |
| `E-12` | **Contact-attempt policy** — attempts, quiet hours, channel fallback order | Engagement | Config | **Yes** | Control | Q8. Elderly patients, evening runs, TCPA-adjacent exposure | — none |
| `E-13` | **Engagement outcome → disposition write-back** | Engagement | Hard | **Yes** | Assist | §6. The sequence must resolve into one of the five HCHB dispositions — **with the reason**, which is not captured today | Backlog: *"accept / reassign / decline + reason"* |
| `E-14` | **Escalation to clinician** | Engagement | Hard | **Yes** | **Read** | Q6. When the assistant stops and hands back. The boundary between an assistant and a liability | `CO-07` |

**Two more, carried from the backlog because this protocol depends on them:**

| Backlog item | Why it matters here |
|---|---|
| **Consent / POA signature status** + **POA availability** (`S-43` / `S-44`, both reserved, `S-43` **contested**) | Gates channel (`CN-09`) and contact routing (`CN-11`) |
| **Clinician safety — market-specific alerts** (`S-47`) | Washington/Providence requires a safety screening script; market rules must reach the engagement |

---

# Part D — data that does not exist in any system today

The honest list. Each of these is a hole the protocol will fall into if it is designed as though the data
were there.

| Missing | Consequence |
|---|---|
| **Visit duration in minutes by visit type** | The arrival-window cascade (§4.2) has no input. Highest-priority gap |
| **A drive-time source** (vs. mileage / centroid proximity today) | The window cascade and the proximity recommendation are both approximations until this is decided |
| **Patient channel consent state, queryable** | Consents are signed on paper at the SOC (`CN-09`); nothing here says they are readable at engagement time |
| **A legal answer on `CN-10`** | Determines whether automated voice is available at all in some markets |
| **Decline / reassign *reason*** | The fact is captured; the reason is not. Named as the best training signal in the process |
| **The clinician's weekly self-planning logic** | Backlog: *"the largest undocumented decision process in the model."* This protocol touches its output daily |
| **A payer rules library** | Three seed entries exist — UHC, Indiana Medicaid, Ohio Medicaid — **all from conversation, none from contracts.** The largest content gap in the initiative |
| **A baseline for `CO-12` coordination time load** | Without it, the time this protocol gives back to clinicians cannot be proven |

---

## Provenance

Compiled 24 Aug 2026 from the project knowledge base: the `Variable Inventory` and `Definitions &
Concepts` tabs of the 8.13 workbook · [`../knowledge/constraint-register.md`](../knowledge/constraint-register.md)
(CN-01…CN-51) · [`../knowledge/process-facts-2026-08.md`](../knowledge/process-facts-2026-08.md) ·
[`../knowledge/whiteboard-session-2026-08-13.md`](../knowledge/whiteboard-session-2026-08-13.md)
(DE-01…DE-10) · [`../artifacts/variable-backlog.md`](../artifacts/variable-backlog.md) ·
[`../artifacts/flow-map-redraw-assessment.md`](../artifacts/flow-map-redraw-assessment.md) §16–17 ·
[`../knowledge/payer-and-episode-economics.md`](../knowledge/payer-and-episode-economics.md).

**Part C is proposal, not record.** Nothing in it is in the workbook, and nothing in it should be treated
as scored until it is added there and numbered.
