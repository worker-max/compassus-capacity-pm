# Current-State Process Facts — established during flow mapping, Aug 2026

> **What this is.** The distilled, source-confirmed process facts that came out of the flow-mapping
> sessions of 17–18 Aug 2026 with PB. Every flow sheet in [`../artifacts/`](../artifacts/) draws
> from these; if a sheet and this file disagree, one of them is wrong — fix it, don't shrug.
> Full derivation and the correction-by-correction history live in
> [`../artifacts/flow-map-redraw-assessment.md`](../artifacts/flow-map-redraw-assessment.md) (§1–26).

## Admission (SOC / ROC)

- **Sequence:** intake receives the referral in Commure → auth team verifies eligibility and keys
  pending auth → back to intake for **final approval** → DCS reviews the referral → scheduler makes
  the **welcome / intake call** → scheduler books the SOC/ROC visit and the discipline evals → the
  clinicians perform them. RN at the SOC; PT/OT/ST at their own evals 1–2 days later.
- **Intake and the auth team are different actors.** Traditional Medicare has no pending auth and
  passes straight through; every other payer routes to the auth team, which keys a pending-auth
  visit count **set by the payer, not by clinical need** (1, 3, 5 or 10).
- **The welcome/intake call is the scheduler's one true judgment call**: is the patient actually
  home — not still inpatient, not deferring home-health admission to a later date. It happens
  *before* the SOC and evals are assigned, so clinicians are never sent to a patient who is not
  there.
- **Every SOC/ROC is time-sensitive** — seen within 48 hours under Medicare guidelines. "Urgent"
  therefore does not mean time-sensitive; it means a clinical diagnosis or another factor deserving
  a **priority flag**.

## The plan of care

- Each discipline plots its **own** frequency, written to clinical need — payer limits are not
  visible at that moment. The RN also plots aide frequency and MSW/ST initial evals.
- The plan-of-care workflow fires **once per discipline** at submission and again at approval —
  the per-discipline task explosion (four disciplines ≈ eight tasks for a decision already made).
- **The 485 is a moment, not a sequence of gates**: QA acceptance, POC lock, 485 submission, and
  orders finalised/sent to the MD for signature all happen **alongside one another**.
- **Assignment is one pass**: the scheduler receives one assignment task per discipline, and one
  working of that task assigns **every visit the frequency generates**. "One task per discipline,
  twice" is wrong; "plotted by frequency, assigned in one pass" is right.

## Authorization — two interfaces only (DE-06)

- **At SOC, auth is a gate**: nothing schedules until eligibility is verified, pending auth is
  keyed, and intake gives final approval. *"We know we have the referral, but it's just not in my
  workflow to schedule yet — it's stuck in auth."*
- **Inside the plan of care, auth is a ceiling**: checked **per visit** by HCHB, silently. No auth →
  the visit sits pending — not on the clinician's calendar, not counted toward productivity, held in
  the scheduler's head or on a sticky note.
- **Every add-on order, recertification and ROC is a new auth question** and re-enters the loop.
- **Three different ceilings on one episode, never conflate them**: auth is *permission* (what the
  payer allows), LUPA is the *floor* (too few visits → per-visit payment), utilisation management is
  the *ceiling* (extra visits earn nothing). A visit can be authorised and still be uneconomic.
- **A fourth ceiling applies to non-episodic payers**: the *cap* — an annual benefit limit set by
  the plan or, on a self-funded plan, by the employer. A commercial or Medicaid patient can be
  inside authorisation and out of benefit. Detail in
  [`../artifacts/payer-types-and-episode-economics.md`](../artifacts/payer-types-and-episode-economics.md).
- The payer's rules already exist in writing — the auth team puts them in a **coordination note at
  verification**, days before anyone writes the plan of care. Surfacing them at POC creation is the
  highest-value, lowest-complexity win identified.

## The clinician's own week (steady state)

- After the 485, routine visits have **no scheduler workflow at all**. The clinician evaluates their
  own capacity → prioritises clinical need → groups geographically (drive time, not distance) →
  tests against hard constraints → **confirms with the patient the day before** → routes (HCHB
  suggests, clinician adjusts).
- Patient preferences are **not a patient lane** — they live as a **coordination note** in HCHB
  (caregiver present, time window, day-of-week). A person wrote the note; the scheduler and
  clinician act on it. The system only houses it.
- **The day-before negotiation**: HARD constraints (dialysis, MD appointments, caregiver hours,
  patient genuinely not home) are accepted and built around. SOFT preferences ("after lunch",
  "not Mondays", a preference with no reason behind it) are negotiable and worth holding the line
  on. *The first visit at 8–9am is the single largest lever on an individual clinician's capacity*;
  over-accommodating clinicians push the cost onto the rest of the team.
- **Visit confirmation coordination (SMS / voice) is the clinician's work, done the day before.
  HCHB does not send reminders.**

## The five dispositions

- Chosen **the day before**, straight after the confirmation call — not at the door — and **selected
  in HCHB**. This makes the recovery window a day wide, not an hour.
- **Accept is the confirmed path**: a confirmed visit is an accepted visit and flows to tomorrow's
  schedule. On the sheets, Accept sits on the Confirmed?→delivered segment, apart from the others.
- If not confirmed: **Reschedule** (the most likely outcome — the "No" branch points here),
  **Reassign**, **Miss**, **Decline**.
- **Reassign vs Decline** — both are clinician selections in HCHB and both return the visit to the
  scheduler. Reassign carries a **plan** (the clinician recommends who should take it — often RN to
  her own LPN, routed through the scheduler only because HCHB forbids direct handoff). Decline
  carries **no plan**; the branch manages placement, and it must go to a clinician other than the
  original. **Decline is the least used disposition, and some clinicians are instructed never to
  use it.** The decline *fact* is captured today; the *reason* is not — and the reassign
  recommendation is the clinician doing a capacity tool's job by hand, i.e. the best training signal
  in the process.
- **Rapid reschedule** is an HCHB configuration flag about clinicians moving **their own** visits:
  when it is on, an in-week reschedule generates **no scheduler workflow at all**. It is *not* part
  of call-out coverage. Branch-level config → tracked in the variable backlog.

## Missed visits and call-out coverage

- **The missed visit is a compliance chain, not a dead end**: clinician documents the missed visit →
  scheduler workflow to **notify the MD within 48 hours** (a Medicare requirement *and* an HCHB hard
  stop) → if late, a workflow generates to the DCS.
- Visit states run **scheduled → documentation pending → missed** — and the Citrix sync lag means
  the status the office sees can be hours behind.
- **Call-out coverage is owned jointly by the DCS and the scheduler** (drawn as a half-maroon,
  half-yellow block). The chain below it is the scheduler's: coordinate coverage by call / text /
  Teams with FT or per-diem clinicians, then reassign to another clinician or move the visit to
  another day.

## Capacity levers

- **Per diem / float clinicians have no territory on purpose** — that is what makes them a
  *targeted capacity instrument*, used two ways: take the SOCs (absorb the admission spike) or take
  coverage visits (free a territory clinician so the branch can accept more referrals). Not an
  exception path; a lever pulled deliberately.
- **Branch leadership (black on the sheets) has exactly one home**: the joint review pulled when
  capacity tightens — territory alignment (reopen zips, adjust patterns, defer) and referral
  acceptance decisions. It sits beside the float lever because both fire at the same moment.
- **Pending-auth invisibility distorts the capacity read** — those visits are on no calendar and
  count toward nothing. *"If you can't see it, you can't plan."* HCHB also generates ~50
  pending-auth workflows per scheduler per day, training bulk-clearing without reading.
- The scheduler's matching work (territory/zip reference, specialty competency, continuity,
  reading the preferences note) is **human work on information housed in HCHB** — someone wrote it,
  the scheduler acts on it. Only the discipline/role match is a genuine HCHB hard gate.

## Recertification and discharge (end of episode)

- **Each discipline decides separately**, against its own goals. Some services discharge before
  recert; others continue on goals not met. Slow mid-episode progress → add-on order extends care.
- **Recert visits are already on the calendar** — plotted at the original plan of care. The 5-day
  recert window (days 56–60) **binds only recertifying disciplines**.
- A non-recertifying discipline performs a **discipline discharge (non-OASIS)** whenever clinically
  sensible — e.g. 7–8 days before period end — and owes no window visit.
- Among recertifying disciplines, **one carries the OASIS recert**; the others perform non-OASIS
  recert evals. Worked example on the sheet: SN discharges day 52–53; PT does the OASIS recert; OT
  does a non-OASIS eval; next-period orders PT **2w3 → 1w3** (9 visits / 6 weeks), OT **1w4**
  (4 visits / 4 weeks).
- The **scheduling workflow fires only after** the recertifying disciplines establish next-period
  frequency orders — then it is the same pattern as admission pass 2 (DCS approval → HCHB generates
  → **auth gate** → one-pass assignment). **A new certification period is a new auth question.**
- **Agency discharge**: when no discipline recertifies, every discipline still discharges
  separately (non-OASIS), and **the last discipline active performs the agency discharge with the
  D/C OASIS** — RN, PT or OT, whoever makes the final visit. The owner is unknown until it happens.
  A completed discharge hands the episode's capacity back to the branch.

## Drawing conventions (binding on every sheet)

- **Colour = actor.** Intake `#1F6F78` · Insurance & Auth `#DF751D` · PCC/Scheduler `#C6A01F` ·
  DCS `#792E2E` · Clinician `#2E599D` · HCHB `#795CA7` · Per Diem/Float `#795933` · Patient
  `#4E8A5B` · Branch Leadership `#1A1A1A` (white text).
- **A workflow item in HCHB worked by a person carries the person's colour.** Purple only where HCHB
  acts by itself: generating tasks, applying rules, checking auth, suggesting a route.
- Size = weight (large = every time, small = conditional, pill = watch condition). Canvas units are
  points on the output sheet — draw at sheet scale, never at A4-and-shrink. Variable-ID chips stay
  **off** (`SHOW_VCHIPS = False`) until the inventory is renumbered.
- Every sheet is **current state**; nothing on them is a proposal, and each footer says so.

## Status — 18 Aug 2026

**Current-state process flow mapping is DONE** (PB, 18 Aug). The set: `Detailed-Flow-Composite`
(the original five-column sheet, corrected), `Primary-Flow-Map` (the episode in four phases),
`Flow-SOC-Full` (1), `Flow-Routine-Visits` (2), `Flow-Authorization` (3), `Flow-Recert-Discharge`
(5), and `Flow-DCS-Scheduler` (the practice sheet). All regenerable from `_*.gen.py` beside them.
A separate Flow 4 (exception & recovery) was deliberately not drawn — its material lives across the
composite and flows 1–2. Still open elsewhere: the variable backlog
([`../artifacts/variable-backlog.md`](../artifacts/variable-backlog.md)) and the workbook rows it
feeds; an annotated commentary companion for Flow 2 (deferred until wanted).
