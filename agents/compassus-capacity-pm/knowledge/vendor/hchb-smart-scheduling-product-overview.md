# HCHB Smart Scheduling — Product Mechanics (Vendor Reference)

> **What this is.** A faithful, structured distillation of *Smart Scheduling Product Overview and User Guide*,
> **Homecare Homebase, LLC — Version 8, last updated 11/2024** (39 pp., marked "Private and Confidential").
> It is the **vendor's own description** of how the Smart Scheduling engine, Visit Dispatching, and Shift
> Manager work: timing, cost model, continuity model, constraints, exclusions, configuration, and reports.
>
> **Why it lives here.** This is **the same HCHB Smart Scheduling feature that was piloted — and mis-piloted —
> in Alabama** (see [`../discovery-session.md` §"Why Smart Scheduling Failed"](../discovery-session.md) and
> [`../README.md` distilled fact #2](../README.md)). To assess whether any of its logic meets the initiative's
> criteria we first have to know precisely what it does. This document is the *what*; the *so-what* lives in
> [`../../artifacts/hchb-smart-scheduling-feature-assessment.md`](../../artifacts/hchb-smart-scheduling-feature-assessment.md).
>
> **Provenance & status.** Vendor product documentation, **not Compassus discovery**. Rendered from the source
> PDF; no PHI. Section names track the source. Where the guide says "contact HCHB / Client Success / enter a
> ticket," the capability is gated behind a vendor-configured setting — noted inline because that gating is
> itself material to the assessment.

---

## 0. One-paragraph orientation

Smart Scheduling (SS) is the optimization module of the **HCHB Intelligence Suite**. It **auto-assigns
clinicians to routine visits** to reduce visit-related cost while managing continuity of care. It runs as an
**overnight batch** over a forward window, chooses the lowest-cost *qualified* worker for each eligible visit,
optimizes each clinician's daily route, and respects a large set of hard/soft constraints. **Visit Dispatching
(VD)** is a real-time extension that assigns visits *inside* the near-term lock window (including same-day) as
workflow events fire. **Shift Manager / Find Shifts** lets clinicians self-request extra visits from mobile.
Together HCHB claims SS+VD "intelligently optimize and schedule **99% of Home Health and 97% of Hospice
visits.**"

**Critical framing for this repo:** SS is a **scheduling-execution optimizer** — it decides *who performs which
already-ordered visit, when, in what order*. It is **not a capacity-planning system**: it does not project the
branch's forward ability to absorb referrals, does not model an SOC admit-slot pool, and (by its own scope
note) **does not touch SOC/ROC visits at all**. Hold that distinction throughout — it is the crux of the
assessment.

---

## 1. The engine: timing, window, and churn control

- **Nightly batch.** Runs each night starting **11 pm CT**; all SS-eligible visits are assigned before PSCs
  arrive. By default each run assigns clinicians **8–14 days out** — a **7-day scheduling window that excludes
  the next 7 days** after the run.
- **Dispatching / lock window.** That excluded near-term period (default **7 days**, configurable per branch to
  **3 or 5**) is the **Dispatching Window**. SS **will never change** visits inside it (they can still be
  changed manually). Purpose: minimize last-minute reassignment **"churn"** and protect clinician satisfaction.
- **Re-optimization.** Every run re-solves for the most optimal schedule for each day. **Already-scheduled
  eligible visits can be reassigned** on a later run — including **overriding manually scheduled visits** —
  unless explicitly prevented (see §7).
- **Split jobs (24.1+).** For large agencies (recommended at **2,500+ visits/week**), the nightly job can be
  split into parallel sub-jobs via Split Visit Settings (Split Visits Start / Group Size, Split Workers Start /
  Group Size). Best-practice cap: **≤5,000 visits/week per super branch.**

## 2. Visit scope — what SS will and won't touch

**Eligible** (optimized when in *Requested* status, or *Scheduled* within the 7-day window):

- **Home Health:** Subsequent, Aide, Discharge, Discipline-only Discharge, Follow-up, Update, Medical Treatment*,
  Recert** / Recert Therapy Add-on** / Recert Add-on**, Phone Visit.
- **Hospice:** Hospice Subsequent, Hospice Aide, Hospice Add-on, Hospice Phone Visit, Hospice Discharge (with
  visit), Hospice Medical Treatment*.

**Explicitly out of scope:** **"SOC, ROCs, and other visit types not listed above are not updated by Smart
Scheduling."** (Admission/SOC and Resumption-of-Care are handled — if at all — only through **Visit
Dispatching**, §10, and even there can be excluded.)

- `*` **Medical Treatment = "buddy codes":** not cost-optimized — matched to the corresponding routine visit by
  patient+day and given the **same worker**. If a buddy code collides with >1 routine visit that day, SS skips
  the buddy visit (primary still schedules).
- `**` **Recert** is **off by default**; enabling requires the vendor `ScheduleRecertVisits` setting.

## 3. The cost model (primary driver #1)

SS minimizes total schedule **cost**, categorized as **labor + overtime/bonus + mileage**.

- **Labor rates** loaded by **Job Code × Branch** for hourly, per-visit, and salaried-overtime-bonus; HCHB
  defaults to **national-average** rates. Workers grouped by **Payment Method** → Salaried / Hourly /
  Per-Visit-Contract / Custom. Multi-job-code workers are costed at their **most expensive** rate.
- **Overtime / over-productivity penalty.** Artificial penalty added to hourly OT and salaried
  over-productivity to suppress both.
- **Mileage cost** = route distance × configurable **mileage rate (default $0.50/mi)**.
- **Rejected Visit Cost.** An artificial $ cost to *reject* a visit — lets the optimizer choose to leave a visit
  unassigned when no worker is genuinely available rather than force a bad assignment.

### 3.1 Caregiver Optimization — Job Code Priority Hierarchy
Prefer the **lower-cost qualified** worker (LPN over RN, PTA over PT) where clinically allowed. Never assigns a
clinically ineligible worker (Service Code still governs eligibility). HCHB flags this as a **large ROI lever**
and ships a **Caregiver Optimization** stock dashboard in HCHB Analytics.

## 4. The continuity model (primary driver #2)

Continuity is encoded as an **artificial cost offset** so the optimizer trades cost against caregiver
consistency:

- **Discontinuity Penalty** (per branch) — extra $ on a worker inconsistent with the patient's prior care,
  **weighted by how many times each worker has seen the patient.**
- **Minimum Continuity Score** — a floor that gives the *most* continuous worker a decisive edge over
  near-equals.
- **New Job Code Continuity Penalty** — small penalty when a brand-new job code enters the care plan (so
  new-patient visits don't outrank continuous ones); paired with defined **New Job Code Handling** (first run:
  visits viewed independently; subsequent runs: first chronological visit's worker is treated as continuous).
- **Continuity exceptions** (branch settings / system function): exclude SOC/ROC clinicians from the continuity
  calc; **weight** the admission visit (e.g., ×0.5); exclude an individual past/future visit from the calc; and
  **weekend/holiday** continuity exclusions.
- **Continuity is visible:** the Scheduling Console exposes a **`% Continuous`** per visit and a **"% Continuous
  Less Than"** filter to hunt low-continuity visits.

## 5. Routing & travel (driver #3, usually smaller)

- Shortest driving distance via **OpenStreetMaps**, from the worker's **home address or Alternate Starting
  Point** (a settable lat/long — can be an intersection, not a real address). Branch address is the fallback
  for un-geocoded workers/patients.
- SS **orders each clinician's day** for minimum drive and suggests start times; **PointCare does not enforce
  the order** (deviating forfeits the modeled mileage savings). Phone visits are dropped to end-of-day (no drive).
- **Miles vs. Minutes** per branch: rural → **Miles**; urban → **Travel-Time Minutes** (bridges/traffic).
  For **fully discontinuous (0% continuity)** workers a cap is enforceable — **Mileage Cap / Max Miles /
  Over-mileage Penalty**, or **Minute Cap / Max Minutes / Over-Minute Penalty** — with a matching rejection
  reason ("Exceeds Travel Time Limitation"). Non-optimized visits use a preset drive time and don't inform the
  rest of the route.

## 6. Worker capacity, availability & constraints

**Eligibility (Worker Console):** Active status, "Able to Perform Visits" = Y, and (optionally) a valid,
state-matched **license** per job code.

**Visit matching (hard constraints):** Job Code (primary/alternate) = visit's Service Code; **Branch** (or
shared branch) = patient branch **and** matching Service Line; **Team**; **Location** (optional); **Skills**;
**Qualifiers**; not marked **Incompatible**.

**Time availability (layered):**
- Recurring Worker Availability = default weekly schedule; absent it, **Mon–Fri all day, no weekends** by default.
- **Individual Worker Availability Parameters** override branch defaults — **Max Hours/Day (≤15)** and/or
  **Visits/Day** (engine stops at whichever fills first).
- **Specific-Day Availability** overrides defaults for a date; **Unavailability** removes hours (must cover the
  full 24h to fully block a day). **NVA** (Non-Visit Activity) can integrate into unavailability.

**Daily constraint:** a per-branch **Max Hours/Day** ceiling counting **in-home + drive + slack** time (unless
Individual params set). **Percentage Time Reserved** carves out a % of the day for admissions/evals/ad-hoc
(configurable per branch and for RN/PT/ST/MSW/CH/Aide). **Slack Minutes after Visits** = wrap-up time added
per visit.

**Weekly constraint:** **salaried** workers stop receiving visits once **>30% over Expected Productivity
Points** for the 7-day Medicare week (OT bonus also added to de-incentivize); **hourly** workers stop at
**>30% over Expected Hours/Week** (rejection `WORKERMAXHOURSORVISITS`; OT rate 1.5). Expected Hours ≤2 or
blank ⇒ treated as per-visit, limit not enforced.

**Productivity Points Model (opt-in).** Schedules to **Expected Points across the whole Medicare week** (not
per-day), letting clinicians work lighter/heavier days while hitting productivity. When ON, the +30% salaried
overage no longer applies (scheduled to exact expected points), branch Max Hours forced to 15, and Individual
Availability Parameters button is disabled. Requires Expected Points + Frequency set or the worker is dropped
from SS/VD.

**Flexible Worker Availability (branch setting).** Lets schedulers **manually** exceed a worker's set
Hours/Visits-per-day with a warning — accommodating clinicians who *want* more than the branch max.

## 7. Exclusions & manual overrides (the "off switches")

- **Worker/Patient exclusion:** assign the Location **`EXCLUDE FROM SMART SCHEDULING`** (or
  `EXCLUDE FROM SMART SCHED AND VISIT DISPATCHING`) → those patients' visits and those workers are skipped.
- **Long-term worker exclusion:** Worker-Status table `Include in Smart Scheduling` = Y/N (e.g., medical leave).
- **Service-code exclusion:** per-code "Exclude from Smart Scheduling"; **PRN codes auto-excluded**.
- **Alternate Job Description exclusion:** a per-branch list of alternate job codes SS should ignore (e.g., RN
  with Aide as secondary — don't auto-assign Aide visits).
- **Prevent from Smart Scheduling** (per-visit, gated system function `PREVENT VISITS FROM BEING SMART
  SCHEDULED`): locks a manual assignment so SS won't re-optimize it; requires a configurable **Prevent Reason**.
  HCHB warns overuse erodes the ROI.
- **Manual Holidays** branch setting: SS won't optimize/override visits on defined holidays.

## 8. Patient Schedule Preference

Per-patient, per-discipline preference: Discipline, Start/End date, Preferred Days, Preferred Time Range
(**once / BID / TID**), Start/End time (whole hours, **7 am–7 pm**), comment. SS **uses it to suggest visit
times** (and **overrides AM/PM-specific service codes**); the Scheduling Console **warns** (soft, ignorable)
when a manual change violates it. Multiple non-conflicting preferences allowed.

## 9. Case Management & Team Member Model

Steer SS toward the patient's named care team:

- **Use Case Management Model** — prefer team-listed clinicians, still optimize outside when needed.
- **Case Management Model Penalty (soft):** team members = 0 penalty; non-team = 1× penalty; single eligible
  team member skips the normal discontinuity/new-job-code penalties; multiple eligible team members get normal
  penalties.
- **Restrict to List (hard):** only team-listed clinicians are eligible.
- **Ignore weekends** option. New rejection reason **"Multiple Team Members"** (two workers share the eligible
  primary job code — forces list hygiene, one worker per job code). Per-referral **Smart Scheduling checkbox**
  marks which team members SS may pick up; detailed copy-forward rules across recert/non-admit episodes. HCHB
  note: enabling this **limits eligible workers and may lower ROI.**

## 10. Visit Dispatching (VD) — real-time, inside the lock window

VD assigns visits **in real time** as workflow stages fire, reaching **into the Dispatching Window including
same-day** — the near-term period SS deliberately won't touch. Together they push coverage to 99% HH / 97%
Hospice.

- **Toggle settings (vendor-gated):** Enable VD; **Automate Same-Day Visits** (+ End-Time); **Enable Next-Day
  Cutoff** (+ Next-Day End-Time — freezes next-day schedules after a cutoff for clinician stability);
  **Automate Declined/Reassigned Visits.**
- **Assignment criteria:** drive time, continuity (when applicable), clinical compliance/appropriateness,
  auth validations, clinician & patient availability, labor type & productivity. **Percent Reserve Time is NOT
  applied in VD** — clinicians can be filled to full capacity inside the lock window.
- **Automated workflow stages:** Complete Requested Schedule (+Week One), Complete Requested Hospice Schedule
  (+Week One), Review/Update Hospice Schedule, Process Declined, Process Reassigned — auto-picked-up, delayed up
  to ~10 min while it searches, then auto-closed; falls back to manual with the "Dispatch Visit" button /
  rejection if it can't fully schedule.
- **SOC via VD:** Admission, Add-on, and Rapid Subsequent can be dispatched via the **Assign LP** stage ("Use
  Visit Dispatching" checkbox) — **but** an **"Exclude Admission Visits from Visit Dispatching"** setting exists
  and admissions can be pulled back out. **Declined/Reassigned** visits from PointCare can auto-route to the
  next-best worker (never the clinician who declined), gated on per-reason "Automate Visit Dispatching" flags.
- **Same-day routing caveat:** for *today's* visits VD does **not** re-order the route; the visit is left
  untimed and falls to end-of-day.
- **VD exclusions:** exclude **workers** via `Exclude from Visit Dispatching` Location (patients **cannot** be
  excluded from VD); service-code exclusions shared with SS; exclude admission visits (above).

## 11. Shift Manager — Find Shifts (clinician-initiated)

New Shift Manager product; first feature **Find Shifts** (requires SS **and** VD). Clinicians **self-request
additional visits** on their mobile device over the **next 7 days**, choosing their own day — **fully
automated, no scheduler involvement**, and it **ignores availability/unavailability** (opt-in extra work above
required productivity). Positioned as retention/engagement + revenue, and as after-hours/sick-coverage relief
for schedulers.

## 12. Reporting surface

- **Smart Scheduling Job History Report** — per-run results; filter by run date, #days optimized, agency /
  service line / branch / team / location / patient / job code / visit type / service code, **Rejected (T/F)**,
  **Rejection Reason**, **% Continuous**, Team Member. Fields include **# of visits by other clinicians**,
  **% Continuous**, **New Job Code Penalty Applied**, Rejected + Reason. *Snapshot of the run, not current
  state; Eastern Time.*
- **Rejection reasons (the diagnostic vocabulary):** Workers at max hours · Visit exceeds rejection cost ·
  **Optimizer** ("engine ran out of time — often branch capacity issues or too many excluded workers") ·
  Blocked by hard constraints · No authorization found / **PRE-BATCH NO AUTHORIZATION FOUND** · No visit match ·
  Incompatible buddy job code · Buddy code matches multiple · **Multiple Team Members** · Multiple visits for
  one job code (flag) · Invalid Visit Location · **RECERT PERMISSION** · (VD) Incomplete Schedule · Date is
  Invalid for Visit · Exceeds Travel Time Limitation.
- **Worker Details Report** — skills, qualifiers, locations, teams, assigned facilities, alternate starting
  point, availability/unavailability.
- **Smart Scheduling Prevented Visits Report** — locked visits by patient + prevention reason.
- **Scheduling Requests and Authorizations Report** — compares authorization vs. requested visits (excludes
  Scheduled).
- **Visit Dispatching Report** and **Visit Change History** (audit of every touch: Smart Scheduler / Visit
  Dispatching / User; Eastern Time).

## 13. Structural configuration (all vendor-set at implementation)

Super Branch (share workers across branches; ≤5,000 visits/wk; all member branches inherit the oldest
branch's settings) · Shared Branch Assignments (per-worker, dated) · **Enable Location Matching** · Facility
matching (Limit Smart Scheduling on facilities + Assigned Facilities on workers) · Labor Rates · Mileage Rate ·
Max Hours/Day · Percentage Time Reserved · Discontinuity Penalty · Minimum Continuity Score · Slack Minutes ·
Drive Time for Non-Optimized Visits · New Job Code Continuity Penalty · Rejected Visit Cost.

---

## 14. What the guide *does not* contain (gaps material to this initiative)

Enumerated because absence-of-feature is as decision-relevant as presence:

1. **No capacity planning / forecasting.** Nothing projects a branch's forward ability to absorb referrals. SS
   consumes today's roster and today's orders; it never answers "what can this branch admit in three weeks."
2. **No SOC admit-slot inventory.** SOC/ROC are *out of scope* for SS and *excludable* from VD. There is no
   reservable admit-slot pool, no SOC-capacity headline, no "admits available today/this week" — **exactly the
   binding constraint (CP-3) the initiative names.**
3. **No open-slot / capacity dashboard.** Capacity appears only implicitly (a worker hit max hours → rejection).
   There is no forward, cross-branch, discipline-by-zone capacity view.
4. **The "point" is HCHB's Expected Productivity Points**, a payroll/productivity construct — **not** an
   acuity/travel/documentation-weighted load unit. Travel and slack are counted in *hours*, not points.
5. **No intake→scheduling handoff bridge.** Auth state gates scheduling (rejections), but the guide is silent on
   the intake communication breakdown the initiative flags as most-cited (CP-8).
6. **Heavy vendor gating.** A large share of the useful logic (split jobs, continuity exceptions, VD toggles,
   travel caps, case-management model, recert optimization, super branches) is **"contact HCHB / enter a
   ticket,"** i.e., not self-service branch configuration.
7. **Optimization can overload.** By design it fills to cost/productivity targets; the "point-maximizing
   overloads the reliable clinician" failure mode the initiative warns about is a real risk of naive tuning.

> The feature-by-feature verdict against the initiative's criteria — capacity-vs-scheduling, CP-1…CP-10, the
> nine open questions, and the tactics library — is in
> [`../../artifacts/hchb-smart-scheduling-feature-assessment.md`](../../artifacts/hchb-smart-scheduling-feature-assessment.md).
