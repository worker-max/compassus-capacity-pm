# Vendor RFP package — capacity & scheduling platform

> Built 19 Aug 2026 from the Evan/Colin meeting of 18 Aug (`Evan _ Colin.docx`, Drive
> `1c_SFJDmZF_jFnGuwI_qjYz0Zbf72o1sA`), the 8.13 workbook (Drive `1tVEkPO2FJMFVyqLZP1TrzqbmjX0qEDgv`)
> and the 8.17 one-pager (Drive `1nRLnwWnj-qlF3cTxEr2b5D1APnua4WN-`).

## The package — three things, per Evan

Evan's instruction was that three artifacts is "as much information as they can handle upfront":

| # | Artifact | Where |
|---|---|---|
| 1 | **One-page overview** — what we are looking for, in three areas | `../artifacts/Capacity-Scheduling-One-Pager.pdf` |
| 2 | **Current-state process map** — context for their answers | `../artifacts/` — see the open question below |
| 3 | **Questionnaire** | [`vendor-questionnaire.md`](./vendor-questionnaire.md) |
| + | **Covering email** | [`vendor-intro-email.md`](./vendor-intro-email.md) |

## The process and the timeline

~10 companies → questionnaire → **first cut** (Evan expects 3–4 fall out here) → ~6 for virtual
calls → **second cut** → top 3 to Nashville for deep-dive sessions, where we show more of our hand.

| | |
|---|---|
| Week of Aug 24 | Package goes out |
| **Fri Sept 4** | Responses due |
| Week of Sept 8 | Virtual sessions |
| Week of Sept 14 | On-site invitations confirmed |
| Late September | Nashville on-sites |

**Watch out: September 7 2026 is Labor Day.** Evan sketched calls for "the week of the 7th"; the
email says *week of September 8*, leaving Tue–Fri. That works for a condensed round of five or six,
and gets tight beyond that. Sept 4 is also the Friday of Labor Day weekend, so expect extension
requests — worth deciding in advance whether those are automatic.

---

## What changed on the one-pager, and why

Evan's core note: *"it'd be a lot easier to read these if each of them had 3 major sections within
them, and then bullets under each."* Plus *"all of these could probably just have a little bit more
color added to them, not a ton, but just a little bit more so that an outsider could understand
what we're talking about."*

So: **three to four named sections per module, each with a one-line plain-English descriptor, then
short bullets.** Section names roll up the 8.13 workbook's own subcategories, so we are speaking the
same language as the inventory without exposing it.

| Module | Sections now |
|---|---|
| Capacity Management | Workforce supply · Availability & reach · The capacity math |
| Scheduling Engine | Demand · Matching · Routing & the week · Exceptions |
| Engagement | Before the visit · When plans change · Across the care team |

### Redundancy found and resolved

| Was | Now | Why |
|---|---|---|
| `07 Visit weighting` + `08 Targets & ceiling` | One bullet | Evan: *"seven and eight are kind of the same"* — the currency and the threshold it is measured against belong together |
| `01 Ordered demand` + `02 Authorization & payer rules` + `03 Order & consent readiness` + `04 Compliance windows` | One **Demand** section | Evan: *"squash all four of those things down"* — the engine needs to understand demand arriving from the intake platform, including whether it is actually schedulable. Kept as four bullets under one heading so the content survives the merge |
| `06 Clinician restrictions` + `11 Patient & clinician preference` | Split cleanly: one clinician bullet, one patient/caregiver bullet | Both sides have needs *and* restrictions. Evan: *"permission needs and restrictions… we should also probably have a patient needs and restrictions"* |
| `07 Patient & caregiver availability` + preference | Merged into the patient bullet | Same source, same conversation |
| `12 Week distribution & continuity` | Split — continuity → Matching, distribution → Routing & the week | Two different ideas sharing a line |
| Engagement `01` / `04` / `05` (three confirmation-ish items) | Grouped under **Before the visit** | Distinct moments, but they read as duplicates in a flat list |
| Engagement `02` / `03` / `08` | Grouped under **When plans change** | Same |

### Rewording, per Evan's line-by-line

- **Availability & time off** → *"provided by the clinician"* — we are asking the clinician to
  supply it.
- **Assessing capacity** → *"Start-of-care capable clinicians, measured as their own distinct
  capacity"* — Evan: *"there needs to be a real capacity measure with the start of care flag."*
- **Territory reachability** → split into territory assignment by zip (*"does the product tie into
  a territory assignment map"*) and drive-time reachability from home base.
- **Committed load & open room** → the explicit visual: what is committed versus what space is
  left, by day, week, discipline and territory.
- **Missed-visit exceptions** → its own **Exceptions** section. Evan: *"that's a capability we would
  want to have."* Framed as managing and tracking missed visits *and reducing the occurrence*.

### Added — present in the workbook, missing from the 8.17 one-pager

Referral inflow / discharge outflow · clinician safety alerts by market · channel and
communication-preference management · multi-discipline visit coordination · care-team and office
coordination updates · the coordination time load itself.

Plus, at Evan's explicit request: **automating the day-before outreach clinicians perform manually
today** — *"one of our biggest opportunities is automating the clinician's process, reaching out to
these patients every single day."*

### Removed for the vendor-facing version

- The **"22 / 47 / 12 variables in full"** counts. They advertise a deeper list we are not sharing
  and invite a question we do not want to answer.
- The workbook provenance footer and the DE-02 reference — internal.

### Deliberately held back

Colin's instinct in the meeting was right: the one-pager stays at the level *"anyone who's put any
time at all into thinking about scheduling should be able to review this and understand it."* These
stay in our pocket for the Nashville sessions:

- The full numbered variable inventory and the scoring behind it
- The three-ceilings framing — auth is permission, LUPA is the floor, utilisation management is the
  ceiling, and a visit can be authorised and still be uneconomic
- The hard-versus-soft day-before negotiation, and the first-visit-time capacity lever
- The scheduler's welcome call as the single genuine judgment call in the flow
- The per-discipline task explosion and the DCS QA/lock mechanics
- Rapid reschedule as a branch-level HCHB configuration flag

---

## How the questionnaire is built

Evan wanted *five or six really important* questions plus *ten or fifteen* diagnostic ones, and a
structure that makes it obvious where each vendor sits on the three dimensions.

- **Part A — Company and product (6).** The disqualifiers. **A1 is HCHB integration**, per Evan:
  *"the home care home base integration, obviously, is an absolute."* Then production-vs-roadmap
  labelling, customers and references, funding stage and maturity, home-health focus, and
  security/implementation. A2 makes every later claim carry a P/B/D/R label, which is the antidote
  to *"they're all going to say they've got this stuff."*
- **Part B — Coverage self-assessment.** A ten-row matrix mirroring the one-pager's sections. This
  is the fast cut: it will show immediately who has only a scheduling engine, and who has nothing in
  patient engagement. It uses only vocabulary already public in the one-pager.
- **Part C — How your product works (21).** Open questions, deliberately **non-leading**: *"how do
  you…"*, *"describe…"*, *"walk us through…"* rather than *"do you support X?"* A feature checklist
  would hand them our vocabulary and teach them the answer we want. These are grouped to mirror the
  one-pager so the feature questions "fall out of it," as Evan put it.
- **Part D — Fit and perspective (5).** Including **D2: what do you do that we have not asked about**
  — the "what else are they doing that we haven't thought of" question.

Two questions are doing quiet work worth preserving: **C15** (does the product schedule
autonomously, recommend, or assist — and why) tells us whether their philosophy can survive contact
with clinician autonomy, which is what sank the Alabama pilot. **D4** (what have you deliberately
chosen *not* to build) separates teams with a thesis from teams with a backlog.

---

## Open decisions for Colin and Evan

1. **Which process map goes in the package.** Evan said send the current state *"so they have the
   context of where we're coming from."* But the sheets carry analysis we may not want to hand over:
   the composite's reading panel states the three-ceilings framing, and Flow 2 carries the hard/soft
   negotiation panel. Options: send `Primary-Flow-Map.pdf` (four phases, condensed, least
   analytical), send `Detailed-Flow-Composite.pdf` (richest context, most revealing), or produce a
   trimmed vendor cut with the analytical panels removed. **Recommend the primary map**, and hold the
   detailed composite for Nashville.
2. **Questionnaire format.** Colin floated a single workbook over splitting across three mediums;
   Evan was open, and suggested letting *"what would a really good answer look like"* drive the
   format. This markdown converts cleanly to Word or to a Google Doc with a response column, and
   Part B is already a table. Recommend one editable document rather than a form — the answers we
   want are prose, and forms discourage prose.
3. **Whether to name the response deadline as firm or preferred**, given the Labor Day weekend.

## Files

| File | What it is |
|---|---|
| [`vendor-questionnaire.md`](./vendor-questionnaire.md) | The questionnaire — Parts A–D |
| [`vendor-intro-email.md`](./vendor-intro-email.md) | Covering email draft, plus notes not for sending |
| `../artifacts/Capacity-Scheduling-One-Pager.pdf` | The revised one-pager (source: `capacity-scheduling-one-pager.html`) |
| `../artifacts/capacity-scheduling-full-lists.html` | The full variable reference — **internal**, not for vendors |


---

## Review pass — 19 Aug, column by column

Colin reviewed each column in turn. Applied:

**Capacity Management**
- *Per-diem and float pool* — dropped "held outside territory assignment." It is a capacity
  component the system must manage; the territory mechanics are more detail than a vendor needs.
- *Approved time off and working availability* — dropped "provided by the clinician." In practice
  this would come from the HR platform, and the sheet does not need to be technical about sourcing.

**Scheduling Engine**
- *Demand* — plan-of-care orders come "from the EMR (Home Care Home Base) and the intake platform."
  Naming HCHB here also reinforces the integration requirement that opens the questionnaire.
- *Clinician safety alerts* — removed. Not this system's job; assignment decisions carry safety
  through other branch inputs, and the call-out would only confuse vendors.
- Routing rebalanced to three clean bullets after the removal.

**Engagement (renamed from Patient Engagement)**
- The module is now **Engagement**, to signal that the system engages with **patients, clinicians
  and the office** — not patients alone. The descriptor says so explicitly.
- Coverage coordination lands here rather than in Scheduling's Exceptions, where it was first
  proposed: **matching potential clinicians to an open need and reaching them directly**, plus
  **call-out coverage and the urgent or prioritized needs that surface during the day.** This was
  the one genuine gap in the original sheet.
- *Across the care team* descriptor now reads "keeping clinicians and the office on the same
  schedule."

Questionnaire kept in sync: Part B module renamed and rows 9–10 rewritten; Part C section renamed;
**C17** extended to cover clinician and office communication; **C20** extended to ask how the
product identifies who could take the work, how it reaches them, and whether the same mechanism
handles an urgent mid-day need.

- **Naming note.** *Engagement & Coordination* was tried and reverted 19 Aug: the shaded band that
  wraps Scheduling Engine and this module is itself labelled **Coordination**, so the word was doing
  two jobs on one sheet. The zone keeps the name; the module is just **Engagement**.
