# Whiteboard Session — 13 August 2026

> **Source:** `8.13.26 Whiteboard Session Executive Summary and Transcript.docx` — Google Drive
> `1ElkCTRvJkv5lCFC5s10hFGHCZn1Y8OJH`, folder `1RPI1ogTdyDeEf64OBRmaRQ0ESNWp5k5o`.
> Companion workbook: `8.13 Compassus Capacity & Scheduling Workbook.xlsx` — Drive
> `1tVEkPO2FJMFVyqLZP1TrzqbmjX0qEDgv`.
>
> **Purpose of the session:** validate the current-state scheduling process map and variable
> inventory against operational reality, then move from current state into target-state design.
>
> **Attendees.** Colin — field-clinical/operations leader, author of the process maps and variable
> inventory, owns all map revisions. Laci — the system-of-record SME, answering "how does it
> actually work" at HCHB-level specificity; the highest-density source in the session. Evan —
> executive and initiative lead, owns vendor relationships.
>
> **Note.** This document is the Executive Summary plus Part A plus the raw transcript. It cites
> Parts B–J and `source/transcript-lines.txt`; those are separate documents still to come. The
> `[T:###]` citations are retained so they resolve once those land.

---

## Decisions register

| # | Decision |
|---|---|
| **DE-01** | Split the current-state map into four flows — SOC/recert/ROC/new order; routine visit scheduling; the auth cycle; exception and recovery. Layerable into one composite. |
| **DE-02** | **Adopt a three-module target architecture: Capacity Management, Scheduling Engine, Patient Engagement.** |
| **DE-03** | **Capacity is Phase 1, and Phase 1 is visualization only — no automation in the first release.** Territory and service area belong in the same phase, probably the same dashboard. |
| **DE-04** | The capacity tool replaces the scheduling grid. They are the same object; do not build both. |
| **DE-05** | Care team is assigned **at referral**, not per visit. System recommends the full team; a human approves or edits; visits thereafter route to the established team. |
| **DE-06** | Map auth only at its interface with scheduling. A deep map of the auth team's internal workflow is not required. |
| **DE-07** | Correct the map legend — yellow = human task, purple = genuine system action, green = patient-supplied. Genuine automation in HCHB is approximately nil. |
| **DE-08** | Discipline-role match **defaults to the paraprofessional, with explicit opt-out**. "They have to opt out versus opt in." |
| **DE-09** | **The tool recommends; the human accepts.** Clinicians supply their own availability windows and preferences. The system does not drop work onto a calendar unilaterally. |
| **DE-10** | Preserve a human scheduling role at reduced scale — fewer schedulers, but a retained function for urgency, local knowledge, and relationship-based coverage. |

## The organizing idea

**Separate HCHB constraints from actual requirements.** Several of the most painful constraints are
Home Care Home Base design choices, not Medicare requirements: routing every physician order to a
DCS for approval; hiding pending-auth visits from the clinician's calendar; blocking a nurse from
handing a visit to her own LPN; blocking an RN from seeing her supervisee's schedule.

> "We have to be really careful that we're just not reinventing Home Care Home Base."
> — and the sharper corollary: *"That workflow shouldn't exist to begin with for the scheduler."*

Some workflows should not be automated. They should not exist.

## The bottlenecks named

**Authorization — and most of the pain is self-inflicted.** Plans of care are written without regard
to payer limits, then the team is frustrated when auth does not materialise. UHC gives 5 nursing
visits and requires 4 of 5 completed plus supporting documentation before visit 6. Indiana Medicaid
pays 30 days from the *discharge* date, not the admit date, with 8 visits shared across PT/OT/ST.
Ohio Medicaid caps similarly. *"UHC was never going to give you more auth. We're not creating our
plans of care based on the insurance."* The data already exists — the auth team writes it into a
coordination note at verification. **Surfacing payer rules at plan-of-care creation is a high-value,
low-complexity win**, and a patient-care win, not only a throughput one: abrupt discharges happen
because nobody planned for the real visit budget.

**Auth and DCS QA are hard stops upstream of the scheduler's queue.** Plan-of-care QA must clear
before the first week of visits can be assigned; if QA is behind, an LPN sits idle and three days of
visits compress into one. Before a referral reaches scheduling it must pass eligibility, have
pending auth keyed, then route back to intake for final approval. *"We know we have the referral,
but it's just not in my workflow to schedule yet because it's stuck in auth."*

**The per-discipline task explosion.** The plan-of-care workflow fires once per discipline — four
disciplines produce four tasks, then four more at approval. Eight tasks of clicking for a decision
already made.

**Invisible work is uncounted work.** Pending-auth visits exist nowhere the clinician or leader can
see and do not count toward productivity. A visit appears on Thursday's calendar on Wednesday
afternoon; the scheduler holds it "in her head or on a sticky note." **"If you can't see it, you
can't plan."** Compounding it, HCHB generates a pending-auth workflow every day per patient —
roughly 50 a day per scheduler — training schedulers to bulk-clear without reading, so the one that
mattered gets cleared too.

**Call-out recovery is unmanaged churn.** No established process: all hands, stop workflow,
non-clinical schedulers opening charts one at a time to triage clinical priority, then begging
clinicians. It cascades into the following days. The ask is a **"flare button"** that triages by
clinical priority (SOC, IV, wound, labs due, ortho) and recommends nearby coverage, with clinical
sign-off retained.

**The readiness call is inconsistently done and it causes harm.** At least one scheduler refuses the
call outright. First-hand consequence: a clinician shifted two visits to her PTA to make room for an
SOC, nobody confirmed the patient was home, the patient was still in hospital, and she lost half a
day of income.

## Clinician autonomy is the adoption constraint

Not a feature request — the documented failure mode. Clinicians will refuse an assignment from a
machine that they would have accepted from a scheduler. *"A scheduler could have assigned that exact
same thing to them, but the tool did it, and they're like, well, it must be broken."*

The agreed design response: clinicians enter their own availability and preferences; the tool
recommends and the human accepts; the framing is **assistant, not controller**. And it must give
them capability they lack today — hand a visit to their own LPN, see their supervisee's schedule,
self-serve open visits (**HCHB's Shift Finder pattern, already available and not turned on**).

## Three changes that are high-leverage relative to complexity

1. **Discipline-role match** — PTs hold routine visits that PTAs should. Default to the
   paraprofessional with explicit opt-out. Two returns at once: lower cost per visit, and freed PT
   capacity for starts, which is exactly where growth is blocked.
2. **Care team at referral** — assign the full team once, system recommends, human approves. The
   most common reassign task today; it collapses the per-discipline task explosion.
3. **Data-driven territory** — there is no data behind territory design today. Hand-coloured maps
   and zip spreadsheets nobody re-cuts because re-colouring is too much work. A live census and
   referral heat map by zip and discipline serves scheduling and growth. The system must encode
   local knowledge: **the Jacksonville bridge** (one zip, two non-interchangeable sides) and **the
   California interstate crossing window**.

## Patient engagement — largest untapped clinician time-back, with hard constraints

Roughly **3,000 home-health clinicians spending about 30 minutes a day — unpaid, in the evening —
confirming tomorrow's visits.** Automating that is a work-life-balance and productivity win at once.
It also makes appointments feel official (email plus text plus an **arrival range, never a hard
time**), enables four touchpoints instead of one, and eventually "your clinician is on the way."

Constraints that need legal input:

- Text and email consents are **not signed until the SOC visit**.
- **California treats any non-manually-triggered outbound call as a robocall.**
- **Washington/Providence requires a safety screening script**, put in place after a clinician was
  killed in a patient's home — so scripts vary by region.
- A genuine judgment call about whether a patient's first contact with Compassus should be an agent.

## Also material

- **Incentives** — surge/marketplace pay, bundling adjacent visits, first-to-accept. The mechanism
  already exists: HCHB **non-visit-activity (NVA) coding** already pays differentiated percentages,
  and branches reach for it when desperate. Caveats: clinicians will learn to hold out for the
  higher offer; union and salaried populations cannot be incentivised the same way; and a meaningful
  share are not money-motivated at all — *their currency is finishing at 3:00.*
- **Coordination notes** are a workaround but less fragile than assumed — they are titled and
  routed; a Point of Care visit alert forces clinician acknowledgment before the visit opens. Still
  a pattern to design out rather than replicate.
- **Vendor read** — the top four or five candidates understand capacity and scheduling and the
  relationship between them; few have thought through patient engagement. Likely shape is one vendor
  for capacity plus scheduling with a voice AI layer bolted on. Nobody is close to GPS-aware
  proactive re-timing — *"that's like version 5."*
- **Headcount** — stated openly: roughly 300 schedulers today, perhaps 100 in target state, while
  deliberately preserving a human air-traffic-controller role. The workload sits in the
  SOC/recert/ROC cycle, the per-discipline assignment burst, auth chasing, and exception recovery —
  **not** in routine visits, which are largely clinician self-managed once assigned.

## Post-session correction — how routine visits are actually scheduled

Corrected by Colin after the session; substantive, not editorial.

- Routine visits are **first plotted by the evaluating clinician at admission, not by the scheduler.**
- Each clinician plots frequency for their own discipline only. The admitting RN establishes nursing;
  PT and OT establish theirs at their own evals, normally within 1–2 days.
- Exception: the RN plots HHA frequency (which stays RN-managed) and/or the initial eval visit for
  MSW or ST, whose clinicians then develop their own discipline plan of care.
- Each discipline's frequency submission generates its own scheduler assignment task.
- After the 485 is submitted, further orders are add-on orders; those that change frequency generate
  additional scheduler workflow.
- **In steady state there is no scheduler workflow at all unless a visit must be reassigned.** The
  assigned clinician may move any non-OASIS visit within the Medicare week (Sunday–Saturday),
  provided the target date stays inside the 60-day certification period from SOC.
- **The clinician's own weekly planning logic is entirely undocumented and unassisted today** — own
  capacity, clinical prioritisation across the caseload, geographic grouping, and hard constraints
  (strict wound care, catheter, IV timing, patient preferences, competing appointments).

## Open items (owners as recorded)

- Split and redraw the process maps into four flows; add an auth swim lane — **Colin**
- Fix map colour coding per DE-07 — **Colin**
- Correct the missed-visit and documentation-pending section; add the clinician's four dispositions
  (reassign, reschedule, miss, decline) and the 48-hour MD notification rule — **Colin**
- Add the "stuck in auth before it reaches scheduling" bottleneck to the map — **Colin / Laci**
- Investigate robocall and TCPA constraints for outbound voice AI — **Colin**
- Build the future-state process map — **Colin**

Executive decisions carried elsewhere (in the missing Part J): whether the company accepts the risk
of turning off DCS order approval, and where the capacity tool lives relative to Commure.

## Deferred / out of scope

Future-state process map (time). Full variable inventory walkthrough — the **84-row** inventory was
reviewed in a prior Colin/Laci session and not re-walked. Deep auth-side mapping (DE-06). Recert,
ROC and new-order variations — treated as one trigger class with SOC, so per-trigger differences
remain unrecorded. Weekend and after-hours scheduling. Aide, MSW and ST scheduling paths.

## What this changed in the artifacts

See [`../artifacts/README.md`](../artifacts/README.md). In summary: three new gating-level variables
entered the inventory (Insurance Authorization, Add-On Orders, Clinician Safety), the three arenas
were renamed to the DE-02 module names, and four items previously flagged as net-new gaps were
independently confirmed here.

New variables arising from this session are tracked in
[`../artifacts/variable-backlog.md`](../artifacts/variable-backlog.md).
