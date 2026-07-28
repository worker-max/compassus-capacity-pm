# HCHB Web Scheduling — Home Health Operational Spec Sheet

> **Prepared as:** an independent consultant's operational teardown of the product, for a home health operator
> evaluating where it fits, what it wins, what it risks, and where the holes are — across **schedule
> management, capacity management, clinician experience, patient experience, compliance/quality, and the
> economics.** Not a marketing summary and not a rebuild of the vendor's own docs — an operator's decision aid.
>
> **Product under review:** HCHB **Web Scheduling** (browser application, `app.hchb.com/schedule`),
> **Early Access**, KB0025451 v10.0, last modified 2025-05-23; assessed 2026-07.
> **Evidence base:** the Web Scheduling User Guide + the Compassus capacity/scheduling discovery corpus
> ([`../knowledge/`](../knowledge/), [`../sme/`](../sme/), [`../artifacts/`](../artifacts/), [`../strategy/`](../strategy/)).
> **Companions:** [full fit analysis](./hchb-web-scheduling-analysis.md) · [overflow/coverage fit](./hchb-web-scheduling-overflow-coverage-fit.md) · [prototype spec](./overflow-coverage-prototype-spec.md) · [pilot charter](./overflow-coverage-pilot-charter.md).

---

## 0. Executive assessment (read this first)

**What it is.** A browser-native, **exception-driven scheduling cockpit** that lifts the HCHB scheduler out of
Citrix for the *review and triage* of visits — field returns, status, and Smart-Scheduling rejects — and adds a
**per-worker weekly capacity readout**. It is an early, expanding surface on top of the HCHB system of record.

**What it is not.** It is **not** a capacity-planning system, **not** a forecasting tool, **not** an economic or
quality instrument, and **not** a clinician- or patient-facing surface. It shows visits that are *already
schedulable*; it does not see the intake→SOC readiness pipeline that determines whether they become schedulable.

**Consultant's one-line verdict.** *A genuine, overdue upgrade to scheduling **execution** and worker-level
visibility — adopt it — but it operates almost entirely in the "day-to-day scheduling" layer. Treat it as the
execution surface and the data spine, and plan to build or buy the capacity-planning, readiness, economic, and
engagement layers **around** it, because it does not attempt them.*

**Fit-for-purpose scorecard** (Strong = does it well · Moderate = partial/emerging · Thin = minimal · Absent = not attempted):

| Operational domain | Rating | One-line |
|---|---|---|
| Schedule **execution** & exception triage | **Strong** | Its core; clean, native, browser-based |
| Real-time field visibility | **Moderate** | Live *view*, but field truth is gated by PointCare sync |
| **Capacity measurement** (worker-week) | **Moderate** | Native `(Sched+Comp)/Expected` — real, but present-tense & shallow |
| **Capacity planning / forecasting** | **Absent** | No forward view, no SOC-slot model, no demand forecast |
| Readiness gauntlet (DCS/auth/POC/F2F/coding/TIC) | **Absent** | Shows post-readiness visits only — the discovery's #1 blind spot |
| Clinician experience | **Thin (indirect)** | No clinician surface; helps only via a better back office |
| Patient experience | **Thin (indirect)** | Visit-reminder flags only; no patient surface |
| Compliance & quality | **Thin** | Hazardous-med flag + status; no compliance-window engine |
| Financial / economic | **Absent** | Points & visits only; no dollars, LUPA, or agency/OT cost |
| Workforce / flex (per-diem, overflow) | **Moderate (as feed)** | Great demand signal + headroom gate; no marketplace |
| Integration / data trust | **Moderate** | Same system of record; inherits manual-sync latency |

---

## 1. Product profile & access

| Attribute | Detail | Operator implication |
|---|---|---|
| Delivery | Web app, **Google Chrome supported** | Browser-based = no Citrix session needed for supported tasks; browser-standardization matters |
| Auth | Same HCHB credentials; **SSO both directions** with Citrix | Frictionless; no new identity to manage |
| Session | **15-minute idle timeout** | Fine for active desks; annoyance for interrupt-driven multitaskers |
| Maturity | **Early Access**, actively expanding ("more queues will be added," goal to "eliminate the need to visit Citrix") | Roadmap-dependent; expect gaps to close over releases — and to move |
| Scope of record | Reads/acts on the **HCHB system of record** | No data migration; single source of truth preserved |

---

## 2. Functional breakdown (module by module)

For each module: **what it does**, the **benefit**, and the **risk/hole** an operator should log.

### 2.1 Scheduling Queues (the left rail)
- **Scheduling Status Alerts** — visits *returned from the field*: **Rescheduled, Reassigned, Declined, Missed
  by Clinician.**
  - *Benefit:* a native "these went sideways / need attention" worklist — the exceptions that actually need a
    human, surfaced without running a report.
  - *Risk/hole:* population depends on the clinician having **synced** (PointCare is manual, not real-time), so
    the queue is only as current as the last sync; no SLA/aging indicator on how stale a row is.
- **Scheduling Status** — high-level view: **Requested, Scheduled, Missed – Not Needed (Missed by Scheduler),
  Completed.**
  - *Benefit:* one place to see the state distribution of the week's visits.
  - *Risk/hole:* status only — no *why*, no time-in-state, no bottleneck analytics.
- **Smart Scheduling Exceptions** (only if Smart Scheduling enabled) — visits the optimizer **rejected**, by
  reason (e.g. **"Worker at Max Hours"**); replaces the Job History and Visit Dispatching reports.
  - *Benefit:* turns two static reports into a live, reason-coded overflow worklist; **this is the single best
    hook for overflow/flex-pool work.**
  - *Risk/hole:* **the fix still happens in Citrix** — the scheduler views the exception here but "schedules as
    needed from the Citrix application." The loop isn't closed in the browser. Requires Smart Scheduling to be
    on at all.

### 2.2 Visit List & Visit Details
- Columns: visit date, patient, worker, team member, service code, **Continuity %** (Smart-Scheduling-assigned).
  Details: Authorization, Payor Source, Episode, Program, Service Code Type/Code, Worker, Date, Start/End, and
  **Visit Change History** (SS users).
  - *Benefit:* enough context to triage a visit without hopping screens; Continuity and Change History are
    genuinely useful.
  - *Risk/hole:* Authorization/Payor are *shown*, but there is **no readiness state** (DCS review, POC lock,
    F2F/coding hold) — so the list can't tell you *why* a visit isn't ready, only that it exists.

### 2.3 Filtering, Sorting, Grouping
- Default: **rolling 8 days (today + 7)** and **Home Branch**; **date range not editable.** Filters: Branch,
  Teams (multi), **Continuity less than…** (10% increments; SS only), Billing (Billable/Non/All), PRN
  (show/hide). Sort/group by Patient, Visit date, Service line.
  - *Benefit:* the filters that matter day-to-day (branch, team, continuity, PRN, billable) are present.
  - *Risk/hole:* **the fixed 8-day window is a real constraint** — no month view, no custom range → **no
    forward planning horizon** in the tool. No filter by **worker availability, capacity headroom, or
    proximity** (you can't ask "who's open near here").

### 2.4 Patient Calendar (7-day)
- Shows **all** of a patient's visits for the week; "Time set" vs "Time not set" sections; week navigation.
  - *Benefit:* the patient's week at a glance supports continuity and reduces double-booking a patient.
  - *Risk/hole:* one week only; no multi-week episode view for recert/frequency planning.

### 2.5 Visit Icons (calendar signals)
- **SS Prevented** (human veto on the optimizer), **Warning dot** (rescheduled/declined/reassigned/missed),
  **Hazardous Med**, **Paper Verified**, **Locked** (SOC + Add-on scheduled via referral), **Visit Notes**
  (docs from PointCare), **Patient Visit Reminder** (Received/Confirmed for patient & primary caregiver).
  - *Benefit:* dense, useful at-a-glance safety/status signals; the **Patient Visit Reminder** flags are a real
    patient-experience touch; **Hazardous Med** is a genuine safety cue.
  - *Risk/hole:* **SS Prevented captures the veto but (per the guide) no reason** — the "why" that would be the
    buy-in and training signal is not evidenced. Reminder confirmations imply a notification capability whose
    scope/channel isn't described here.

### 2.6 Search tab — Worker
- Worker search (min 3 chars) → card: Name, **Primary Phone**, Worker ID, Primary Job Description, Home Branch,
  Status. **Folder → Worker 7-day calendar flyout** with all visits **and NVA**, plus the **capacity readout**.
  - **Capacity = `(Scheduled + Completed) / Expected`**, computed dynamically from **Productivity Points**,
    Sunday–Saturday.
  - *Benefit:* **the standout feature.** A native, per-clinician weekly workload/availability number, with NVA
    included on the calendar and a phone number to make the ask — exactly what a coverage/overflow desk needs.
  - *Risk/hole:* **search is by name only** — no query by availability/discipline/geography/employment type.
    "Completed" is **sync-gated**, so the capacity % can read stale. NVA appears on the calendar but the
    capacity **formula** is Scheduled+Completed÷Expected only — so **travel, documentation, acuity, and NVA are
    not weighted into capacity** (it overstates the headroom of an efficient, high-acuity, or high-travel
    clinician). And **"Expected"** — the denominator the whole metric rides on — is undocumented here (flat vs.
    market/discipline-tuned unknown).

### 2.7 Search tab — Patient
- Patient search (min 3 chars) → card: Name, DOB, Primary Phone, MR#, Branch, Team, City, Zip, Episode Status.
  - *Benefit:* fast patient lookup with the operational essentials.
  - *Risk/hole:* surfaces **DOB, MR#, address-level City/Zip** — a **PHI-exposure surface** to govern
    (minimum-necessary); no acuity, no plan-of-care detail.

---

## 3. Domain assessments (the operator's lenses)

### 3.1 Schedule management — **Strong (execution) / the tool's home turf**
- **Benefits:** browser-based exception triage; the three queues cover field returns, overall status, and
  optimizer rejects; visit context and continuity in one place; SSO with Citrix; a real step toward "scheduling
  by exception" instead of report-running.
- **Risks/holes:** the **Smart-Scheduling fix round-trips to Citrix**; **no editable date range** (8-day cap);
  status without root-cause or aging; **no availability/proximity search** to *place* an exception; field truth
  gated by **manual sync**.
- **Verdict:** genuinely improves the scheduler's *execution* loop. It does not change *why* visits fall out
  (which the discovery locates upstream, in DCS/auth/POC — §3.5), so it makes the last-visible-mile faster
  without touching the causes.

### 3.2 Capacity management — **Moderate measurement / Absent planning**
- **Benefits:** a **native capacity currency** (Productivity Points) and a **per-worker weekly capacity %** —
  the first standardized, in-product answer to "is this clinician full?" This retires part of the discovery's
  #1 gap (an *undefined point system*) with a production definition.
- **Risks/holes — this is the biggest strategic gap for a growth-focused operator:**
  - **Present-tense only.** Rolling Sun–Sat; **no forecast**, no 30/60/90-day demand shape, no recert/discharge
    projection. Capacity planning is a *forward* function; this measures last/this week.
  - **No SOC-slot model.** SOC — the **binding constraint on branch growth** — is just a service code here; it
    is not tracked as protected, bookable admit inventory, and the SOC-eligibility clinical rule (RN if nursing
    on case; PT only if not) is not modeled.
  - **Worker-week grain only.** No discipline-by-zone capacity, no branch-level absorb-this-referral number, no
    capacity-to-census ratio.
  - **Unweighted load.** Capacity ignores travel, documentation, acuity, and NVA — it will call an efficient or
    high-acuity clinician "available" when they are not.
- **Verdict:** a useful *sensor*, not a *planning system*. It tells you this week's worker utilization; it does
  not tell you whether the branch can grow, where the constraint is, or what next month needs. Pair it with a
  real capacity model.

### 3.3 Clinician satisfaction / experience — **Thin & indirect**
- **Benefits (indirect):** a faster, less error-prone back office means fewer "your schedule is a mess" moments
  that clinicians wrongly blame on scheduling; the capacity % *could* support fairer load-balancing if a manager
  uses it that way; Continuity % supports caregiver consistency.
- **Risks/holes:** **there is no clinician-facing surface** — clinicians still live in **PointCare** and manage
  their own day (call patients, accept the slate, sync). Web Scheduling does nothing for the clinician directly.
  Because capacity is **unweighted**, a naive manager could over-load the efficient clinician using it — the
  classic burnout-the-reliable-one failure. No fairness/reciprocity ledger, no accept/decline loop, **no
  earnings visibility** (the motivator for extra work).
- **Verdict:** helps clinicians only through a better back office. It carries a **latent risk** of being used to
  push utilization on a blunt (unweighted) number. The discovery's core lesson — position tooling as a *personal
  assistant, not control* — cannot be delivered by this product because it has no clinician touchpoint.

### 3.4 Patient satisfaction / experience — **Thin & indirect**
- **Benefits:** **Patient Visit Reminder** flags (Received/Confirmed, patient + primary caregiver) show a
  reminder capability that supports the punctuality/communication factors patients judge agencies on;
  Continuity % supports caregiver consistency; **Hazardous Med** flag supports safe visits.
- **Risks/holes:** **no patient-facing surface** — none of the discovery's patient asks (visit-window
  visibility, reschedule requests, caregiver visibility, the QR-code portal idea) are addressed; the Medicare
  CoP physical calendar obligation is untouched. Reminder *channel/scope* undocumented.
- **Verdict:** modest, indirect patient benefit via reminders and continuity. The patient-experience layer the
  discovery calls for is out of scope.

### 3.5 The readiness gauntlet — **Absent (the discovery's #1 finding)**
- **The gap:** the discovery's central conclusion is that *the inefficiency is upstream of scheduling* — visits
  stall in **DCS review, authorization holds, plan-of-care lock, and face-to-face/coding discrepancies**, and
  the whole funnel is measured on **TIC (time-to-initial-care)**. Web Scheduling shows Auth/Payor and a
  "Requested" status but models **none** of these states and **no TIC clock.**
- **Consequence:** it can show **green capacity while admissions stall upstream** — the exact
  "blame-lands-on-scheduling" trap. A scheduler using only this tool sees a visit is "Requested" but not *why*
  it can't proceed.
- **Verdict:** the most important thing this product does **not** do. Any serious capacity/growth initiative must
  own this layer elsewhere (Commure/Pulse/NestMed/coding joins).

### 3.6 Compliance & quality — **Thin**
- **Benefits:** Hazardous-Med safety flag; Missed-by-Clinician vs Missed-by-Scheduler distinction (supports the
  48-hour MD-notification workflow); Paper-Verified and Visit-Notes provenance; Locked flag on SOC/Add-on.
- **Risks/holes:** **no compliance-window engine** — recert/60-day, 30-day therapy reassessment, 14-day HHA
  supervisory, OASIS timeliness, buddy codes are not surfaced as scheduling constraints; **no HHVBP/quality
  measures**, no acute-care-hospitalization signal. Compliance windows are hard scheduling constraints the tool
  doesn't enforce.
- **Verdict:** useful safety/status flags, but the compliance *timing* engine that protects reimbursement and
  CoP is not here.

### 3.7 Financial / economic — **Absent**
- **The gap:** capacity is in points and visits; there are **no dollars.** No **LUPA-risk** watch (a
  step-function the schedule directly controls), no margin-per-period, no **agency/PRN/overtime cost** view.
- **Verdict:** every executive capacity decision is ultimately economic; this tool cannot inform the dollar
  side. Pair with an economic overlay.

### 3.8 Workforce / flex (per-diem & overflow coverage) — **Moderate, as a feed**
- **Benefits:** the **two exception queues are a ready-made "visits needing coverage" feed**, and the **worker
  capacity %** is the exact **headroom gate** to decide which full-time clinicians can absorb extra and which
  are maxed. A scheduler-driven overflow desk works today.
- **Risks/holes:** **no clinician-facing open-work/claim board**, **no availability/employment-type/proximity
  search**, **no offer→accept/decline loop or reason capture**, **no earnings story**, **no fairness ledger**,
  and exception fills return to Citrix.
- **Verdict:** an excellent **demand-signal + headroom** layer to harness; the flex **marketplace** itself must
  be built on top (see the [overflow prototype spec](./overflow-coverage-prototype-spec.md)).

### 3.9 Integration & data trust — **Moderate**
- **Benefits:** it *is* the system of record — no migration, no reconciliation, single source of truth; SSO.
- **Risks/holes:** field-originated data (declines, misses, completions, documentation) is gated by
  **PointCare manual sync** — **not real-time**; the **Workday↔HCHB PTO integration is reportedly OFF**, so
  availability inputs may be manual/stale; capacity accuracy inherits both. No documented external API for the
  queues/write-back (an open question, not a stated capability).
- **Verdict:** trustworthy *as a mirror of HCHB*, but every number inherits HCHB's sync freshness — design
  downstream uses (like overflow claiming) for staleness.

---

## 4. Consolidated benefits

1. **Gets schedulers out of Citrix** for exception triage — browser-based, SSO, faster.
2. **Scheduling by exception** — three queues surface only what needs a human; replaces static reports.
3. **A native capacity currency and per-worker weekly capacity %** — the first standardized in-product answer to
   "is this clinician full?" (partial close of the point-system gap).
4. **Smart-Scheduling exceptions as a live, reason-coded worklist** — the best hook for overflow/flex work.
5. **Useful visit signals** — Continuity %, Change History, Hazardous Med, Visit Reminders, Locked/Paper-Verified.
6. **No new system of record** — single source of truth preserved; low integration burden to *read*.
7. **Actively expanding** — an Early-Access roadmap trending toward a fuller browser cockpit.

## 5. Consolidated risks & limitations

1. **Present-tense, 8-day, worker-grain** — structurally unable to do forward capacity planning.
2. **Unweighted capacity** — ignores travel/doc/acuity/NVA; will overstate real headroom and can drive burnout
   if used naively.
3. **"Expected" denominator undocumented** — the whole capacity % rides on a target whose configuration is
   unknown; if flat rather than market/discipline-tuned, the metric misleads.
4. **Manual-sync latency** — field truth and "Completed" lag reality; capacity can be stale; double-book risk.
5. **Smart-Scheduling fixes round-trip to Citrix** — the exception loop isn't closed in the browser; requires SS
   enabled.
6. **PHI exposure surface** — patient search shows DOB/MR#/address-level City/Zip; governance required.
7. **Early Access volatility** — features (editable dates, write-back, capacity depth) are roadmap promises, and
   the vendor is drifting toward the capacity space you may be building — **roadmap-encroachment watch.**
8. **Change-management inertia unaddressed** — it can't deliver the "personal assistant, not control" framing the
   Alabama failure proved essential, because it has no clinician surface.

## 6. Consolidated holes (what it does not attempt)

| Hole | Domain | Who must own it |
|---|---|---|
| **Readiness gauntlet + TIC** (DCS/auth/POC/F2F/coding) | Capacity/throughput | Commure/Pulse/NestMed/coding joins + a readiness model |
| **Demand forecast** (30/60/90-day, recert/discharge shape, seasonality) | Capacity planning | A capacity/forecasting tool |
| **SOC-slot inventory + SOC clinical routing rule** | Growth constraint | Capacity model |
| **Staffing model & territory** (RN:LPN / PT:PTA, resting posture, zone coverage) | Capacity strategy | Capacity/territory design |
| **Economic layer** (LUPA, margin, agency/OT cost) | Finance | Economic overlay |
| **Compliance-window engine** (recert/30/14/48h, OASIS, HHVBP) | Quality/compliance | Compliance module |
| **Clinician-facing surface** (open-work/claim, accept/decline+reason, earnings, fairness) | Workforce/flex | Flex-marketplace layer |
| **Patient-facing surface** (visit windows, reschedule, caregiver visibility) | Patient experience | Patient portal |
| **Acuity model** on demand | Capacity accuracy | Capacity model |
| **Back-office throughput** (scheduler/DCS load — the real bottleneck) | Ops | Workflow automation |

## 7. Requirements to verify before you rely on it

*(These are decision-blocking unknowns, tracked in the [integration questions](./hchb-integration-discovery-questions.md).)*
1. **How is "Expected" configured** — flat branch default or market/discipline-tuned? (Gates every capacity %.)
2. **Are the exception queues available via API/export** — fields, cadence, latency vs. PointCare sync, reason
   codes? (Determines whether anything can be automated on top.)
3. **Is there assignment write-back**, or does the fix stay in Citrix?
4. **What are HCHB's Productivity-Point values** — to reconcile against a weighted (travel/doc/acuity) model?
5. **PTO source** — is Workday↔HCHB live yet, or is availability still manual?
6. **PHI/BAA surface** — minimum-necessary governance on the patient search fields.
7. **Roadmap** — editable dates, write-back, and any capacity/forecasting additions (encroachment watch).

## 8. Deployment recommendation

- **Adopt it** for what it is: the **scheduling-execution cockpit and worker-visibility layer**, and the **system
  of record** everything else reads from. There is no reason to rebuild this.
- **Do not mistake it for a capacity system.** Stand up the planning, readiness, economic, compliance, and
  engagement layers **around** it — it is the execution surface and data spine, not the strategy.
- **Best immediate high-value use:** harness the **Smart-Scheduling Exceptions + Status Alerts queues** and the
  **worker capacity %** as the demand-signal + headroom engine for an **overflow/per-diem coverage** capability —
  the cleanest, lowest-risk wedge, opt-in and earnings-led (see the [overflow fit](./hchb-web-scheduling-overflow-coverage-fit.md), [prototype spec](./overflow-coverage-prototype-spec.md), and [pilot charter](./overflow-coverage-pilot-charter.md)).
- **Design every downstream use for sync latency**, enforce **scope/SOC/compliance and PHI-minimum** as hard
  rails the product doesn't, and keep a standing **roadmap watch** because the vendor is moving toward your space.

---

*Independent operator's assessment. Product capabilities cited from the Web Scheduling User Guide (KB0025451
v10.0); operational lenses, gaps, and guardrails grounded in the Compassus capacity & scheduling corpus. Verify
the §7 unknowns against Compassus's live HCHB configuration before committing design or spend.*
