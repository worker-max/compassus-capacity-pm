# HCHB Web Scheduling (Early Access) — Outline, Cross-Reference & Capacity-Initiative Fit

> **Source document.** *Web Scheduling — Web Scheduling User Guide*, Homecare Homebase (HCHB) knowledge base
> article **KB0025451, v10.0 (Latest)**, revised by Frank Buttafarro, last modified 2025-05-23; captured
> 2026-07-22. 12 pages. This is HCHB's own end-user guide for its **browser-based scheduling application** at
> `https://app.hchb.com/schedule` — the tool that is beginning to replace the Citrix Scheduling Console /
> Workflow Console for Compassus schedulers.
>
> **Why this document matters to us.** Compassus's entire clinical, workflow, and scheduling system of record
> *is* HCHB (see [`../knowledge/discovery-session.md`](../knowledge/discovery-session.md) §5). This guide is the
> first hard evidence of **where the incumbent platform is going natively** in scheduling — and it directly
> touches the two things our initiative is built around: the **point system** and **capacity**. This analysis
> (1) outlines the document in full, (2) cross-references every feature against our capacity & scheduling
> corpus, and (3) states how the product fits into what we are building.

---

## Part 1 — Detailed Outline Summary of the Document

### 1.0 Provenance & framing
- **Product:** "Web Scheduling," an HCHB web application — explicitly labelled **Early Access**.
- **Strategic intent stated in the doc:** as HCHB adds queues, Web Scheduling will enable **"scheduling by
  exception, eventually eliminating the need to visit Citrix"** to run the Scheduling Console, Workflow Console,
  and scheduling-related reports. This is a stated migration path *off* Citrix and *toward* a browser cockpit.
- **Maturity signals:** Chrome-only; date range "not yet editable"; queues "will be added"; several features
  gated on "if Smart Scheduling is enabled." It is a v10 but still early, thin, and expanding.

### 1.1 Logging in / access
- URL `https://app.hchb.com/schedule`; **Google Chrome supported**.
- Same credentials as HCHB-via-Citrix. **Single sign-on** both directions (Citrix ⇄ web).
- **15-minute idle timeout.**

### 1.2 Navigation — two tabs
- **Scheduler tab** (a.k.a. Patient Scheduling): queues, visit list, 7-day patient calendar, Visit Details panel.
- **Search tab:** worker search and patient search.

### 1.3 Scheduler tab

**Scheduling Queues** (saved default filters down the left rail):
1. **Scheduling Status Alerts queue** — visits *returned from the clinician in the field* needing action.
   Statuses: **Rescheduled, Reassigned, Declined, Missed by Clinician.**
2. **Scheduling Status queue** — high-level view of all statuses: **Requested, Scheduled, Missed – Not Needed
   (officially marked Missed by Scheduler), Completed.**
3. **Smart Scheduling Exceptions queue** — *only appears if Smart Scheduling is enabled at the agency.*
   Replaces the **Smart Scheduling Job History** and **Visit Dispatching** reports. Shows visits **rejected by
   the Smart Scheduling engine** within the rolling 7-day calendar, by **exception reason** (example given:
   **"Worker at Max Hours"**). Scheduler picks a reason, views the visits, then **schedules them manually from
   the Citrix application.**

**Visit List & Visit Details:**
- Visit List columns: visit date, patient name, assigned worker (if any), Team Member (if any), service code,
  **Continuity** (if assigned by Smart Scheduling).
- Pencil icon opens **Visit Details:** Authorization, Payor Source, Episode, Program, Service Code Type,
  Service Code, Worker, Visit Date, Visit Start/End time, and **Visit Change History** (Smart Scheduling users).

**Filtering:**
- Default scope: **rolling 8 days (today + 7)** and the scheduler's **Home Branch**. **Date range is not yet
  editable.**
- Filters: **Branch** (limited to branches the user is granted), **Teams** (multi-select), **Continuity
  less than…** (10% increments — only applies to Smart-Scheduling-assigned visits), **Billing**
  (Billable / Non-Billable / All), **PRN visits** (show/hide).

**Sorting & Grouping:** by Patient name, Visit date, or Service line.

**Patient Calendar:** 7-day week view, appears when a visit is selected; shows **all** of that patient's visits
(selected one highlighted); week back/forward + Today; **"Time not set"** vs **"Time set"** sections.

**Visit Icons** (calendar chips):

| Icon | Meaning |
|---|---|
| **SS Prevented** | User marked this visit to be *prevented* from the Smart Scheduling optimizer. |
| **Warning dot** | Visit was rescheduled, declined, reassigned, or missed by a clinician. |
| **Hazardous Med** | Patient has a hazardous medication in the referral. |
| **Paper Verified** | Visit completed on paper / manually verified in the Back Office. |
| **Locked** | Visit scheduled via the referral → Scheduling tab (**SOC and Add-on visits only**). |
| **Visit Notes** | Documentation complete and available from PointCare. |
| **Patient Visit Reminder** | Patient Received / Patient Confirmed / Primary Caregiver Received / Confirmed. |

### 1.4 Search tab

**Worker search** — min. 3 characters → worker cards: Worker Name, Primary Phone, Worker ID, Primary Job
Description, Home Branch, Status. Each card has a **Folder button → Worker 7-day calendar flyout** showing all
visits **and non-visit activity (NVA)**.

- **The capacity headline (most important line in the whole document):** the Worker Calendar shows the
  **worker's capacity** under the name header — "a clear view of availability and workload, calculated
  dynamically using **Productivity Points** for the selected week (Sunday–Saturday)."
  **Capacity calculation: `(Scheduled + Completed) / Expected`.**

**Patient search** — min. 3 characters → patient cards: Patient Name, DOB, Primary Phone, MR#, Branch, Team,
City, Zip Code, Episode Status.

### 1.5 What the product *is*, in one paragraph
Web Scheduling is HCHB's **browser-native, exception-driven scheduling execution cockpit**: it surfaces visits
that need a scheduler's attention (field returns, status, Smart-Scheduling rejects), lets the scheduler read a
patient's week and a worker's week, and shows a **native, present-tense capacity percentage per worker built on
Productivity Points**. It is an *execution and visibility* surface, not a planning, forecasting, or economic
one — and today it still hands the actual (re)scheduling of exceptions back to Citrix.

---

## Part 2 — Cross-Reference Against Our Capacity & Scheduling Corpus

Mapping each Web Scheduling capability to what we have already documented. Corpus references:
DS = [`discovery-session.md`](../knowledge/discovery-session.md), SUM = [`capacity-scheduling-summary.md`](../knowledge/capacity-scheduling-summary.md),
STRAT = [`../strategy/capacity-strategy-foundation.md`](../strategy/capacity-strategy-foundation.md),
TAC = [`../sme/capacity-tactics-library.md`](../sme/capacity-tactics-library.md),
IDX = [`../artifacts/capacity-tool-data-index.md`](../artifacts/capacity-tool-data-index.md),
ECO = [`../artifacts/capacity-ecosystem-map.md`](../artifacts/capacity-ecosystem-map.md).

### 2.1 The point system — *our open-question #1 has a native answer*
Our corpus repeatedly flagged **the point system as "the single most significant gap… referenced everywhere,
defined nowhere"** (SUM §3.3, §9.1; IDX Domain F). Web Scheduling reveals HCHB's native currency in production:

- **Productivity Points** are the live unit of the capacity readout, and **capacity = `(Scheduled + Completed)
  / Expected`** points for the Sunday–Saturday week.
- This is the *same currency* our tool already adopted as **WVP** (Weighted Visit Points — SOC 2.5 / recert 1.75
  / eval 1.5 / reassess 1.25 / discharge 1.75 / routine 1.0; TAC "open numbers"). **The reconciliation is now
  concrete:** our WVP table must be validated against HCHB's actual Productivity-Point weights and the
  "Expected" denominator (the productivity target — heard as ~30/wk in DS §4, IDX A10). If HCHB's points differ
  from our WVP, HCHB's is the number the branch already lives by and should anchor the tool.
- **Implication:** we do not need to *invent* the point system — we need to *read it out of HCHB and extend it*
  (add travel, documentation, acuity, NVA weighting — the parts SUM §9.1 and TAC L3-2 say HCHB's raw points
  miss). HCHB's Worker Calendar even shows **NVA** on the calendar, confirming NVA is tracked but *not* in the
  capacity formula (the formula is Scheduled+Completed÷Expected only) — exactly the gap TAC L3-2 predicts.

### 2.2 Native capacity metric vs. our capacity concept — same word, different altitude
| Dimension | HCHB Web Scheduling capacity | Our capacity model (STRAT / IDX-J / TAC) |
|---|---|---|
| Grain | One **worker × one week** | Discipline × zone × forward-time; branch; SOC-slot pool |
| Formula | `(Scheduled + Completed) / Expected` points | Productive visit-hours net of PTO/NVA/travel/acuity; SOC slots as a *separate reservable pool* (TAC L1-2) |
| Time | **Present-tense** (this Sun–Sat) | Forward — 30/60/90-day forecast (IDX J4, ECO 2D) |
| SOC awareness | **None** — SOC is just a service code | SOC is the **binding constraint** (SUM §2.1, CP-3), routed by clinical law (STRAT 1.2, TAC L1-3) |
| Economics | None | LUPA / margin / agency-OT overlay (ECO 1B) |
| Territory | None (worker-week only) | Resting-posture & zone coverage (STRAT L2, TAC L2-*) |

**Read:** HCHB answers *"is this worker full this week?"* Our tool answers *"can the branch grow, where, at what
cost, and will it still be true next month?"* Same vocabulary ("capacity," "points"), **different jobs** — this
is exactly the capacity-vs-scheduling separation that SUM §1 and DS §3 say the branch fatally conflates. HCHB
Web Scheduling lives on the **scheduling-execution** side of that line.

### 2.3 Smart Scheduling — the Alabama story, now visible in the UI
DS §3 ("Why Smart Scheduling Failed") and ECO 3I make Smart Scheduling central to our change-management thesis.
This guide shows its operational surface:
- **Smart Scheduling Exceptions queue** = the visits the optimizer *couldn't* place ("Worker at Max Hours").
  This is the exact seam where the machine hands back to the human — **the natural integration point for a
  smarter directive engine** (TAC L3-4 last-minute decision tree; ECO's "directive governance").
- **Continuity %** as a first-class, filterable field ("Continuity less than…") = HCHB already scores continuity
  of care for Smart-Scheduling assignments — maps directly to our continuity concept (CP-10, TAC C-4). We should
  **consume** HCHB's continuity number, not compute a rival one.
- **"SS Prevented" icon** = a human veto on the optimizer. This is the accept/decline/override signal ECO 3I and
  TAC C-6 ("human override is sacred") say we must capture — HCHB already has the flag; the question is whether
  it captures the *reason*.
- The failure mode is still live: exceptions get **kicked back to Citrix to schedule manually.** The optimizer
  is bolted on, not trusted to close the loop — precisely the "never truly piloted" pattern from DS §3.

### 2.4 "Scheduling by exception" = our directive/exception-engine philosophy
The document's stated design goal — **scheduling by exception** — is the same operating model as our
directive engine (ECO "7-type directive engine"; TAC Layer-3 cockpit). HCHB is converging on the same UX
thesis: don't make the scheduler read everything, surface only what needs a decision. That is validation of our
approach *and* a warning that the incumbent is moving into the same conceptual space.

### 2.5 Field returns & visit status = our Process 2/3 and visit-state model
- **Alerts queue (Rescheduled / Reassigned / Declined / Missed by Clinician)** ↔ DS Process 2 (Ongoing Visit
  Management) and Process 3 (Clinician Daily Scheduling); IDX **E5 visit status** enum
  (plotted/accepted/completed/missed/declined/reassigned/rescheduled); TAC **L3-10** (missed-visit handling as
  signal, 48h MD notice).
- **Missed – Not Needed / Missed by Scheduler** ↔ the missed-visit workflow and the 48-hour Medicare MD
  notification clock (DS Process 2, appendix; TAC L3-10). The guide confirms the two *kinds* of miss (by
  clinician vs. by scheduler) our model distinguishes.
- **Warning-dot icon** aggregates exactly these four field-return states — a ready-made "this visit went
  sideways" signal our tool can consume rather than re-derive.

### 2.6 The readiness gauntlet — *still absent, exactly as ECO 1A predicted*
Our single biggest structural gap (ECO **Tier 1A**; DS §1–2 "the scheduling problem is not a scheduling
problem") is the pre-scheduling readiness gauntlet: DCS review, auth hold, POC lock, F2F/coding hold, and the
**TIC clock.** Web Scheduling **does not close this**:
- Visit Details shows **Authorization** and **Payor Source** (a hint of auth state) and a **"Requested"**
  status — but there is **no DCS-review state, no POC-lock state, no F2F/coding-hold state, and no TIC clock.**
- It shows visits *once they are schedulable*, which is downstream of the gauntlet. So HCHB Web Scheduling will
  still **"show green capacity while admissions stall upstream"** — the blame-lands-on-scheduling trap DS §1
  and ECO 1A name. **This is white space HCHB is not filling — and Commure/NestMed/Pulse are where it lives
  (DS §5).** It is a strong candidate for *our* differentiated value.

### 2.7 Data-spine cross-walk (Web Scheduling fields ↔ our data index)
| Web Scheduling field | Our IDX element |
|---|---|
| Worker ID / Name / Primary Job Description / Home Branch / Status | A1, A2, A3, A12, A19 |
| Worker capacity % (Productivity Points, Scheduled+Completed/Expected) | B6, B7, B9, F1–F2, J1, J7 |
| NVA on worker calendar | F4 (NVA treatment — tracked, not yet weighted) |
| Continuity % | C13, CP-10, TAC C-4 |
| Service Code / Service Code Type / Program | E2 visit type, C4 disciplines |
| Authorization / Payor Source | D6, H1–H4 |
| Episode / Episode Status | C6, C7 |
| Visit status + change history + field-return alerts | E5, E6, E7 |
| Patient card: DOB / MR# / City / Zip / Team | C1–C3 (**PHI — minimum-necessary guardrail applies**) |
| Hazardous Med flag | C11 acuity/complexity (a discrete safety flag) |
| PRN filter, Billing filter | E2 / C10 payer-billing |

Nearly every Web Scheduling field maps to a row we already anticipated — confirming our data index is
well-aligned to HCHB's real object model. The **capacity %, Productivity Points, and Continuity %** are the
high-value confirmations; the **absence** of readiness/TIC/economic fields confirms our gap list.

> **PHI note.** The patient search surfaces DOB, MR#, and address-level City/Zip. Our tool's posture (IDX §6,
> CLAUDE.md HIPAA rules) is minimum-necessary and aggregate-first; anything we ingest from this surface must
> respect that — we want the operational signals (capacity, status, zone), not the patient identifiers.

---

## Part 3 — How This Product Fits Into What We Are Building

### 3.1 The core strategic read
**HCHB Web Scheduling is the incumbent, browser-native *scheduling-execution* surface and the system of record
for the point currency and the worker-week capacity number.** It squarely occupies **Layer 3 (day-to-day
scheduling execution)** of our capacity stack (STRAT). It does **not** occupy Layer 1 (staffing model), Layer 2
(territory), the readiness gauntlet, forecasting, economics, or quality/VBP — the layers where our initiative
concentrates its value.

The right posture is therefore **not build-vs-buy but build-*above*-and-integrate**: treat HCHB as the data
spine and execution cockpit, and put our capacity tool *upstream and on top* of it.

### 3.2 Where each system plays (the boundary)
```
        OUR CAPACITY TOOL (planning / forecasting / economics / readiness)         HCHB WEB SCHEDULING (execution)
        ─────────────────────────────────────────────────────────────────         ───────────────────────────────
  L1  Staffing model · RN:LPN / PT:PTA · SOC-slot inventory · market model    ✗ not addressed
  L2  Territory health · resting posture · zone coverage                       ✗ not addressed
   ▲  Readiness gauntlet · DCS/POC/F2F/coding/auth · TIC clock                 ~ shows Auth/Payor + "Requested" only
   ▲  Forecast 30/60/90 · recert/discharge shape · demand seasonality         ✗ present-tense only
   ▲  Economics · LUPA watch · margin · agency/OT cost                         ✗ none
   ▲  Quality/VBP · OASIS/recert/14-day/48h compliance windows                 ~ Hazardous-Med flag only
  L3  Directive/exception engine (proposals)                          ───────▶  ✓ Exception queues, visit list, worker/patient calendars
      Point currency (WVP) — reconcile to ◀───────────────────────────────────  ✓ Productivity Points, (Sched+Comp)/Expected
      Continuity target — consume ◀────────────────────────────────────────────  ✓ Continuity %
      Override/accept-decline capture ◀───────────────────────────────────────  ~ SS-Prevented flag (reason?)
```

### 3.3 Concrete integration seams (what we actually wire up)
1. **Adopt HCHB Productivity Points as the canonical currency.** Reconcile our WVP table to HCHB's point
   weights and the "Expected" target; extend (not replace) with travel/doc/acuity/NVA weighting. Closes IDX
   Domain F against a real, in-production definition.
2. **Consume the worker capacity % as an input, then add the dimensions HCHB lacks** — forward time, SOC-slot
   separation, territory, dollars. Our number *explains and projects*; HCHB's *reports this week*.
3. **Hook the Smart Scheduling Exceptions queue.** Every "Worker at Max Hours" reject is a demand signal our
   directive engine (TAC L3-4) should catch and propose a resolution for — turning HCHB's dead-end ("go do it in
   Citrix") into a next-best-action. This is the highest-leverage, lowest-friction integration.
4. **Consume Continuity % and the field-return alert states** (Rescheduled/Reassigned/Declined/Missed) rather
   than re-deriving them — they feed TAC C-4 continuity and L3-10 missed-visit handling directly.
5. **Capture the SS-Prevented / accept-decline signal** as training data and the buy-in mechanism (ECO 3I,
   TAC C-6). If HCHB stores a *reason*, ingest it; if not, that is a gap our surface can own.
6. **Own the readiness gauntlet + TIC** (ECO 1A) by joining Commure (intake/referral), Pulse (utilization/POC),
   NestMed (documentation/F2F), and coding — the states HCHB Web Scheduling structurally cannot see. This is
   our clearest differentiation.

### 3.4 Build / integrate / watch — decision table
| Capability | Verdict | Rationale |
|---|---|---|
| Scheduling exception queues, visit list, patient/worker calendars | **Integrate (don't build)** | HCHB is delivering this natively, browser-based, as system of record. Rebuilding is waste and fights the spine. |
| Point currency & worker-week capacity % | **Integrate + extend** | Adopt HCHB points; add the weightings and forward/SOC/economic dimensions HCHB omits. |
| Smart Scheduling optimizer & continuity | **Integrate at the exception seam** | The optimizer already exists; our value is governing its exceptions and the change-management loop that sank Alabama, not re-optimizing. |
| Readiness gauntlet + TIC | **Build (differentiate)** | HCHB Web Scheduling does not model it; it is the discovery's #1 finding and our biggest gap. |
| Forecasting, economics (LUPA/margin/OT), quality/VBP | **Build (differentiate)** | Absent from HCHB's scheduling surface; these are the executive/VBP decisions and are Layers we own. |
| Staffing model & territory (L1/L2) | **Build (differentiate)** | Entirely outside HCHB Web Scheduling's scope; the primary effectors of capacity. |

### 3.5 Risks & watch-items this document surfaces
- **Roadmap encroachment.** Web Scheduling is **Early Access and explicitly expanding** ("more queues will be
  added," "eventually eliminating Citrix"). HCHB already ships a *capacity %* and *Productivity Points* — the
  vendor is inching toward our space. **Watch each release.** Our defensible ground is the planning/forecasting/
  economics/readiness layers HCHB shows no sign of building, and the multi-system joins (Commure/Pulse/NestMed)
  HCHB cannot make alone.
- **Present-tense, manual-sync, Chrome-only.** Capacity here is a rolling-8-day, Sunday–Saturday snapshot on
  **PointCare manual sync** (ECO 3K) — any number we consume inherits that latency. Design for staleness.
- **"Expected" is doing a lot of work.** The whole capacity % hinges on the *Expected* productivity target
  (denominator). If that target is a flat branch default rather than market/discipline-tuned (STRAT L1.4,
  TAC L1-4), the metric flatters or punishes clinicians wrongly. **Confirm how HCHB sets "Expected."**
- **Change-management, again.** The optimizer still defers to manual Citrix scheduling on exceptions — the
  Alabama pattern of "bolt on, don't trust" persists. Our accept/decline governance (ECO 3I, TAC C-6) is the
  antidote and should be positioned as the missing half of Smart Scheduling.

### 3.6 Recommended next moves
1. **Pull the real HCHB Productivity-Point weights and the "Expected" target definition** and reconcile against
   our WVP table (TAC open-numbers). This retires open-question #1 with a production-true number.
2. **Confirm what the Smart Scheduling Exceptions API/export exposes** (reasons, cadence) — it is the cheapest,
   highest-value integration and the seam where our directive engine attaches.
3. **Confirm HCHB captures continuity % and SS-Prevented *reasons***; if not, claim the accept/decline-reason
   loop as our surface (the buy-in mechanism).
4. **Position the capacity tool explicitly as "above and upstream of HCHB Web Scheduling."** In stakeholder and
   vendor materials, draw the boundary at §3.2 so we never look like we're rebuilding HCHB — we're completing
   it on the planning, forecasting, economic, and readiness dimensions it doesn't cover.
5. **Add "HCHB Web Scheduling roadmap" to the standing watch list** and re-run this fit analysis on each Early
   Access release.

---

*Prepared for the Compassus Capacity & Scheduling initiative. Cross-references the HCHB Web Scheduling User
Guide (KB0025451 v10.0) against the initiative's discovery, strategy, tactics, data-index, and ecosystem
corpus. Treat HCHB point/capacity specifics quoted here as read from the user guide; validate the underlying
weights and the "Expected" target against Compassus's live HCHB configuration before hard-coding.*
