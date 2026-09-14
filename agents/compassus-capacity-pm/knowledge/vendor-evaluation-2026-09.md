# Vendor Evaluation — September 2026

> **What this is.** The full read of the eleven completed *Capacity & Scheduling Vendor Questionnaires*
> (form dated 2026-08-19), plus supporting proposals, cover letters and the HCHB / VitalCaring Smart
> Scheduling case study. Every questionnaire was read in full, not skimmed.
>
> **Status of the figures.** All vendor numbers are **as submitted and none are independently verified.**
> Where a vendor's coverage-grid marking and their narrative answer disagree, **the narrative is reported
> and the discrepancy is flagged.** References, demos and security review were outstanding for all eleven
> at the time of writing.
>
> Companion: [`vendor-process-2026-09.md`](./vendor-process-2026-09.md) — the selection process, timeline,
> stage gates and vendor communications.

---

## 1. The field at a glance

Ordered by depth of proven home health operating experience.

| Vendor | Where they operate today | HH in production | HCHB live with customers | Capacity & scheduling | Patient engagement |
|---|---|---|---|---|---|
| **Homecare Homebase** (Smart Scheduling) | 31 orgs on Smart Scheduling · 90% HH · top 3 = 100k ADC | Yes | Native — no integration | Both in production | Texting only |
| **Axle Health** | ~25 orgs · 80% HH · 11k / 5k / 2k ADC | Yes | Built, **switched off** | Both in production | Production |
| **Arya** | ~60 orgs · 4 of 10 largest post-acute · 30k+ census | Yes | **Live since mid-2025** (Citrix RPA) | Both in production | Production (voice/text) |
| **CareStitch** | 79 orgs / ~144 branches · 69% HH · 5.4k patients | Yes | Read-only beta, no write-back | Decision support only | None automated |
| **Vitalis Care** (Sync / Sync360) | 6 orgs · **100% hospice** · 4k / 2.5k / 1.5k ADC | No | **Production since 2023**, write-back | Production, visit-count based | None |
| **Servis.ai** | ~200 orgs · ~18% HH · 6k visits/mo largest | Partial | Not built | Single-clinician, single-day | None automated |
| **Care Connect** | ~80% non-medical home care · 22.9k / 12.4k caregivers | No | Not built, scoped | Shift engine in production | Clinician-facing only |
| **AutoMynd** | HH via other products · 12k / 8k / 4k census | Unclear | Blueprint only | Claims need testing | Described, untested |
| **MedArrive** | **Hospital-at-home, SNF-at-home, at-home primary care** · ~1k visits/mo | No | Not built, no HH EMR at all | Per-clinician production; branch view Q4 | SMS only |
| **UnityAI** | Radiology, behavioral health, 70-hospital capacity mgmt | No | Not built | Matching only, one customer | **Strongest evidence in field** |
| **Zeeva** | 100% HH focus · **no production customers** | No | Not built | In development | Q1–Q2 2027 |

---

## 2. The five conclusions that hold across the field

1. **The real question is not which vendor is best.** HCHB Smart Scheduling is the only response with home
   health scale, no integration risk, and capacity *and* scheduling both in production. Its gap is
   engagement. So the question is whether **Smart Scheduling plus an engagement partner beats replacing
   the layer entirely.**
2. **There is no clean challenger.** No external vendor has all three legs proven in home health on HCHB.
   Axle has the domain and the metrics but switched HCHB off. Arya has the scale and a live HCHB
   integration, on Citrix RPA. Vitalis has the most credible HCHB write-back and has never run a home
   health episode.
3. **Integration is a decision to make *before* choosing a vendor, not after.** Six of the ten external
   vendors need Compassus sponsorship into HCHB's partner program or legal cover for RPA; only Arya and
   Vitalis are live on it. Native / log ship / RPA / warehouse-first / wait-for-HCHB's-Databricks-migration
   is the fork in the road.
4. **Engagement thins fast.** Only Axle, Arya, UnityAI and Care Connect have automated outreach at any
   scale — and Care Connect's is clinician-facing only. HCHB has texting. CareStitch, Vitalis and Servis.ai
   have none; MedArrive has ruled it out. **HCHB is itself shopping for an engagement partner**, which
   tells us the capability is buyable separately.
5. **Decide or advise — choose it, don't inherit it.** HCHB, CareStitch, Vitalis and Servis.ai are built to
   *advise* a scheduler. Axle, Arya, Care Connect and Zeeva are built to *decide*. That choice determines
   what the Compassus scheduling organization looks like in three years.

---

## 3. Per-vendor records

Each record uses the same eight fields: home health experience · capacity · scheduling · engagement ·
HCHB · in development · what we would build alongside them · risk.

### Homecare Homebase — Smart Scheduling *(incumbent, native)*

- **Home health.** The largest footprint in the field. **31 organizations** running Smart Scheduling in
  production; top three clients hold a combined **100,000 ADC**. 90% home health / 9% hospice / 1% private
  duty — private duty is harder for them because of per-patient orientation. **Live since 2020.**
  References offered.
- **Capacity.** Production, multiple customers. Evaluates available workforce capacity against scheduled and
  outstanding demand using configured visit weights, productivity targets and ceilings, and committed load
  vs remaining room by day, week, discipline and territory. **Referral and discharge activity count only
  once entered into HCHB — Smart Scheduling does not independently forecast inflow or outflow.**
- **Scheduling.** Production, multiple customers, automated end to end across demand, matching, routing and
  exceptions. Plans and balances **22 days forward** against ordered frequency and episode dates. Nightly
  optimization plus real-time visit dispatching when CRS workflow generates. Eligibility filter → agency
  guardrails → optimization across feasible options. Front-loading supported. Anything blocked by a hard
  constraint lands on an exception report for a scheduler.
- **Engagement.** The thinnest leg. Patient texting only — welcome message, visit reminder, ETA. No voice,
  no agentic conversation. **Patient availability is assumed** on the basis that the patient is homebound;
  what is modeled is *un*availability (dialysis, a doctor's appointment) entered in the back office or by a
  clinician in map view, plus Patient Schedule Preferences. Conflicts surface as a message to the clinician,
  who reschedules in PointCare or messages the scheduler. Their words: *"We will be making this process more
  automated in the future."*
- **HCHB.** Not applicable — **native to HCHB Back Office.** No integration, no sync latency, no partner
  access to negotiate, no RPA. It behaves as if a user were updating the assigned worker. **This is the
  single largest structural difference in the field.**
- **Measured.** Automates up to 95% of HCHB visit types and over 60% of workflow tasks; **~65% of visits
  scheduled automatically.** Schedulers cover up to twice as many patients; one large client moved from 250
  to 350 patients per scheduler in under a year, with a path to 400+ in 2027. VitalCaring case study:
  scheduler bandwidth **+15%**, **7,100 tasks/week** automated across 30+ branches, roughly **10 FTE
  (~$700k/yr)** of scheduling and admin work automated, capped productivity up ~1 point for RNs and 2+ for
  PT/OT/ST — a deliberate trade-off that lowered para-professional utilization. **Mileage is not tracked
  across the client base**; they say so directly, citing geographic variability.
- **In development.** **Visit Finder** — clinicians self-assign open visits inside Care+ — released to
  production **August 2026**; HCHB does not yet know which customers have it enabled. More automated
  patient-availability handling, undated. And notably, **they are actively reviewing vendor partners to
  supply patient engagement rather than building it.**
- **Build with us.** Configuration rather than construction — but the configuration burden is real and they
  flag it repeatedly: *"Agency Configuration will play a vital role in this working as designed"* appears
  against workforce supply, availability and reach, routing, and readiness. Beyond that: the entire
  engagement leg (or a partner to supply it), incentive and differential mechanics beyond surfacing a shift
  in Find Shifts, and referral inflow / discharge outflow forecasting against the envelope.
- **Risk.** Two things. **No uptime figure and no SLA were offered** — the continuity answer describes
  recovery behavior and ends *"I'm unable to answer the contractual part of your question and recommend this
  is directed to Sales."* Second, they are explicit that **our own behavior has to change**: *"Past behaviors
  like front-loading visits early in the week must change for SS to work correctly. Clients must be willing
  to let SS run without manipulating visits too much, which directly impacts ROI."* Also by design, **PRN
  visits are not auto-scheduled** — the system cannot know a change in condition, so they route to Visit
  Finder for pickup.

### Axle Health *(home-health native)*

- **Home health.** ~25 production customers. 80% HH / 20% hospice / 0% private duty. Largest 11,000 / 5,000 /
  2,000 ADC. Measured 3 months pre vs 3 months post-rollout: **+17% clinician productivity, −32% mileage
  cost, +74% scheduler productivity.**
- **Capacity.** Production, multiple customers. **Unit is points.** Forecast at service-code level against
  per-clinician FT/PT/PRN targets; PTO-aware; ordered visits count before authorization. Referral check
  returns eligible clinicians, their forward capacity, and zip-level capacity by discipline.
- **Scheduling.** Production, multiple customers. Every visit carries a fulfillment window; date
  recommendations optimize across the **episode**, not the day. Flags a *missing* recert visit, not just a
  non-compliant one. Ordered-but-unwritable visits are schedulable in Axle and auto-write to the EMR later.
  Call-out flow resolves in seconds across three choices: flip service code, change clinician, change date.
- **Engagement.** Production, multiple customers. Agentic voice, text and email. Confirmations, reminders,
  en-route. Human-in-the-loop recommended where clinical escalation is likely.
- **HCHB.** **Built, then switched off.** No customer live on it today. Read via log ship, write via RPA.
  They judged the 15-minute refresh unreliable and **up to 30-minute staleness below their bar** for visits
  and frequencies.
- **In development.** Dynamic incentive pricing. A visit waitlist and manual incentives exist today.
- **Build with us.** HCHB integration. Point table and productivity targets mapped — these can live in Axle
  as source of truth if HCHB is inadequate. Everything else is configuration.
- **Risk.** The restart of the HCHB integration depends on **HCHB's own Databricks/Snowflake migration** —
  outside their control and ours. They have no plans to re-enable on the current architecture.

### Arya *(scale + live HCHB)*

- **Home health.** ~60 production organizations. **4 of the 10 largest US post-acute providers.** Three
  largest each above 30,000 daily census. Even split across home health, hospice, private duty nursing and
  personal care. Aveanna pilot: **+11% authorized hours delivered with no added administrative headcount**,
  from the customer's operational data.
- **Capacity.** Production, multiple customers. Modeled at clinician level, aggregated to branch. **Unit is
  configurable** — points, visits, hours or weighted visits. Ingests targets from the EMR/HRIS or derives
  them from operating data.
- **Scheduling.** Production, multiple customers, end to end. Hard eligibility gate plus configurable
  heuristics (continuity, productivity, drive time, employment status, RN-vs-LVN, preferences). Exceptions
  detected from the EMR or reported by a clinician over voice, then **restaffed autonomously against a
  5-minute SLA.** Incentives and differentials in production.
- **Engagement.** Agentic voice and text is the primary interface for both clinicians and patients — **there
  is no clinician app.** Patient-facing outreach is production with one customer and deliberately sequenced
  late in every deployment.
- **HCHB.** **Live in production since mid-2025. Read and write.** Citrix screen automation, tuned by data
  criticality rather than one poll interval — sub-5-minute for SOCs, visits and schedule changes. HCHB
  partner status in progress.
- **In development.** Migration to HCHB Marketplace interfaces as they become available (expected 2027).
- **Build with us.** Configuration, not construction: our point system, productivity model, readiness
  criteria and branch guardrails. They are explicit that **data readiness and change management decide the
  outcome, not the algorithm.**
- **Risk.** Citrix RPA at our scale — brittle to UI change, dependent on HCHB's tolerance. Separately, the
  **"no more apps for clinicians" mandate is a decision about our clinicians we would be adopting, not
  configuring.** Uptime given as <2 hrs unplanned in 12 months; no percentage published.

### CareStitch *(scheduler decision support)*

- **Home health.** 79 customer organizations across ~144 branches. 69% home health. Largest ~5,361 active
  patients. Customer-reported and **explicitly not vendor-validated**: −1.27 miles per visit across 104,272
  visits (~$92,700/yr), and census roughly doubled without adding a scheduler.
- **Capacity.** Production, multiple customers. Configurable visit weights totaled against each clinician's
  expected workload, shown as numeric day-level availability plus color coding on calendar and map together.
  Territories by ZIP or custom polygon. Maximum drive distance from home or from the previous visit. **No
  aggregated branch total** — capacity is read through the clinician view.
- **Scheduling.** Production, multiple customers. Constraints remove ineligible clinicians, then a person
  chooses. Self-service custom properties auto-filter clinicians against patient attributes, created by
  agency admins without vendor involvement. Parallel availability requests to configurable priority groups,
  with bonus information attached and private clinician replies. **Advise-only by design.**
- **Engagement.** None automated. Click-to-call with automatic logging, shared notes, care-team chat.
  Welcome calls, reminders, confirmations, en-route and self-service reschedule are all human-led.
- **HCHB.** Read-only beta, screen automation, not in production, **no write-back.** Supported interim
  workflow is agencies manually uploading HCHB reports.
- **In development.** Agentic AI layer on the same decision-support foundation — **no date.** Automated
  patient outreach — **no date.**
- **Build with us.** Production HCHB integration including write-back. Plan-of-care orders, ordered
  frequency, authorization and payer rules — **none ingested today.** Automated compliance-window
  enforcement. The entire engagement leg.
- **Risk.** Philosophical, not technical. CareStitch is built to **help a scheduler do the work, not to do
  it.** If the goal is a platform that carries the work, this is a mismatch rather than a gap.

### Vitalis Care — Sync / Sync360 *(proven HCHB write-back)*

- **Home health.** **None in production.** Six customer organizations, **100% hospice.** Largest 4,000 /
  2,500 / 1,500 ADC. Palliative deployment beginning. **PDGM, LUPA, 30-day payment periods, OASIS and
  authorization are absent from their operating model.**
- **Capacity.** Production, multiple customers, but **visit-count based, not point-weighted.** Per-clinician
  daily visit capacity by discipline against working hours, PTO and credentials, then filtered by real
  drive-time reachability. No consolidated branch-level view yet.
- **Scheduling.** Production, multiple customers. Real drive time, multi-day optimization across the
  scheduling horizon, continuity explicitly prioritized. Call-Off Center ranks replacement clinicians.
  Sync360 mobile gives GPS visit verification comparing actual route and mileage against the optimized plan.
  **Advise-only by design, after an early deployment failed for being too automated.** Results: mileage
  −25.5% / −22.8% / −21% / −18.5% across four clients; overtime 8.3 → 1.4 average hours per worker;
  productivity 64% → 74% of target; 5.1% more visits per day on 4.2% fewer miles.
- **Engagement.** **None.** No patient-facing communication of any kind. Marked *"No / Roadmap — no date
  yet."*
- **HCHB.** **Production since 2023.** Log-shipped replica for high-volume reads, plus **write-back of
  approved visit assignment and reassignment through HCHB interfaces**, with integration errors captured for
  reconciliation. Replication 10–30 minutes; write-backs handled independently of the cycle. **Last HCHB
  update time is displayed in every view.**
- **In development.** Call-Off Center triage separating must-cover-today from deferrable. Branch-level
  capacity view across day, week, discipline and territory. Readiness states — being scoped now. Structured
  clinician-response workflows for coverage offers.
- **Build with us.** Visit point weighting. Authorization and readiness as workflow states. Front-loading
  rules. Compliance-window-aware rebooking priority. Float pool and ramp as distinct constructs. Incentives
  — unsupported. The entire engagement leg. **The home health episodic model.**

### Servis.ai *(single-clinician optimizer)*

- **Home health.** ~200 production organizations, but ~70% healthcare of which about a quarter is home
  health. Largest home health deployment 6,000+ visits/month. Their **"+50% completed work per person" came
  from a 1,000-person operation visiting referral sources, not patients** — they state this themselves. They
  decline to claim a mileage result they cannot evidence.
- **Capacity.** Production, **one** customer. **Unit is time** — minutes and hours of shift, per clinician
  per day. Every open slot carries available-minutes and a can-fit flag; KPIs record shift utilization,
  unallocated time and appointments per hour. No branch-level rollup.
- **Scheduling.** Production, multiple customers, but scoped to **one clinician, one day.** Transparent
  100-point fit score — skills 25, date urgency 20, priority 15, shift fit 15, home proximity 15, preferred
  rep 10; ≥55 considered, ≥85 schedule immediately. Three routing strategies with auto-selection. Break
  compliance, flexible start and end locations, fixed events as hard blocks. Surgical mid-day gap
  re-optimization instead of a full rebuild. Infeasibility panel gives a plain-English reason when a visit
  cannot be placed.
- **Engagement.** None automated. Coordinators enter patient time windows, which the optimizer enforces as
  hard constraints. No welcome calls, reminders, confirmations or en-route notifications.
- **HCHB.** Not built. Live REST-API integrations with other EMRs. Estimate **5–10 weeks once sandbox access
  exists.** Reconciles last-write-wins on the external appointment ID.
- **In development.** Nothing material. Team-week optimization, automatic re-optimization and patient
  engagement are all framed as design-partnership builds, not work underway.
- **Build with us.** Drive-time eligibility — **today reach is scored on straight-line miles from home in
  distance buckets**, and they cite our own current-state critique back to us. Per-clinician maximum drive
  distance (system-wide today). Pending-auth work in the capacity number (invisible by design). Branch
  rollup. Team-week and multi-discipline episode planning. Territory, float pool, incentives. All
  engagement. HCHB.

### Care Connect *(marketplace mechanics)*

See [§4](#4-deep-dive--medarrive-and-careconnect) for the full deep dive.

- **Home health.** ~80% non-medical home care, **15% skilled home health**, 5% hospice. 750,000+ caregiver
  profiles; largest deployments **22,900 / 12,400 / 6,600 active caregivers** (headcount, not patient
  census). They state this *"would be a significant and intentional expansion of our home health
  footprint,"* and that PDGM LUPA avoidance, OASIS/SOC window adherence and episode point-capacity are **not
  in their production measurement library.**
- **Capacity.** Liquidity engine in production — shift demand, rosters, fill rates, surplus and shortfall by
  geography and discipline. But weighted visit points, productivity ceilings, LUPA/PDGM tracking, **territory
  modeling** and provisional pending-auth load are all **scoped builds.**
- **Scheduling.** **ShiftMatch.AI** in production — hard eligibility gate, ranked fit, tunable penalties.
  Predictive acceptance model for PRN and float. Google Maps drive time enforced as a hard constraint that
  consumes capacity. Advisory and automatic modes both live, plus a hybrid review-window mode. **Routing &
  the week is marked Roadmap — no date yet.**
- **Engagement.** Strongest production proof in the field **on the clinician side.** Caregiver Choice fills
  **50% of open shifts by self-selection with zero coordinator outreach** — 6 months at a 5,000-caregiver
  agency, up from 0%; **38% of those visits went to caregivers coordinators had never reached by phone.**
  Multi-channel voice, SMS, email and push in production. **Patient-facing outreach is a scoped build — they
  have never done it.** Incentives marked Roadmap — no date yet.
- **HCHB.** Not live. Scoped only. HL7/FHIR APIs since 2024 and a live HHAeXchange integration. Phase 1
  read-replica at ~90 days (~20 min latency), Phase 2 bidirectional write-back at ~180 days, **contingent on
  us securing partner access.**
- **In development.** Two items in the middle of the scheduling engine carry no date: **routing & the week,
  and incentives.**
- **Build with us.** The entire home health episodic layer, labeled *"Scoped Build"* throughout: point
  weighting, ceilings, LUPA/PDGM, territory, 485 handling, readiness states, week balancing, multi-discipline
  sequencing, supervisory dependencies, assessing-vs-assistant roles, SOC capability as distinct capacity,
  and all patient outreach. Plus HCHB.
- **Risk.** **Highest ratio of "scoped build" to "production" of any respondent.** The engine is real; it
  fills per-visit shifts in non-medical home care. The home health platform around it does not exist yet.

### AutoMynd *(claims need testing)*

- **Home health.** Present through other products — an ambient scribe and an EMR — at 12,000 / 8,000 / 4,000
  census plus EMR partnerships. Of the scheduling product itself: *"Scheduling product is new, and rolling
  out part of our EMR."* No measured scheduling outcomes given; A3 answers with categories, not figures.
- **Capacity.** *Described*: live dashboard by discipline and location, from roster, working schedules, time
  off and the visit calendar. A referral routes from central intake to the clinical manager for
  capacity-based approval, including whether the patient can be seen within 24 hours.
- **Scheduling.** *Described*: hybrid AI + algorithm + rules across roughly a dozen parameters, hard rules
  gating first, weights configurable. Dispatch Map tracks missed visits and call-outs in real time with a map
  view of who is available. Weekly planning is *"plots it and refreshes periodically."*
- **Engagement.** *Described*: voice and text agent captures first-visit availability at intake; clinician
  interface captures patient availability at SOC; agentic scripts configured per agency with exception
  routing; pre-arrival notifications.
- **HCHB.** **Architectural blueprint only.** Explored the log-shipped replica through their Scribe product.
  Proposed hybrid of event-driven and scheduled sync, with a visible "as of" timestamp on every record and
  RPA as backup. Needs replica access and a data dictionary first.
- **In development.** Not stated — a consequence of marking everything production.
- **Build with us.** HCHB integration. Beyond that, **unknowable until the coverage claims are tested.**
- **Risk.** **All eleven coverage areas are marked "Production — multiple customers" with no notes and no
  delivery method**, directly against their own statement that the scheduling product is new. Resolve this
  before assessing anything else. Their strongest idea is upstream: payer-level expectations of how many
  visits will be approved for a condition, fed to intake and the case manager so the plan of care is designed
  around it.

### MedArrive *(higher-acuity home care)*

See [§4](#4-deep-dive--medarrive-and-careconnect) for the full deep dive.

- **Home health.** **None.** No home health, hospice or private duty customers. Production is
  **hospital-at-home, SNF-at-home and at-home primary care**; largest deployments ~1,000 visits/month. Their
  **700-clinician, 11-state scale was their own field business, since wound down** — and they decline to
  present its operating metrics.
- **Capacity.** **Unit is hours and minutes, not points** — shift time minus planned durations, expected
  drive time and blocked time. Per-clinician math is production; **branch capacity view and the referral
  check are in development, Q4.** Points offered only as an alternate display mode, on the roadmap.
- **Scheduling.** Drive-time routing and intra-day resequencing with traffic, production. Two-stage
  assignment: hard feasibility filters, then scoring on drive time and continuity. Multi-clinician visits
  modeled as a **resource requirement** rather than two colliding appointments. Most distinctive: it measures
  **observed visit duration against planned and recalibrates the planning constants** — a 90-minute planned
  admission measured 70, a 45-minute discharge measured 30. Episode/week planning, front-loading and
  LUPA-aware placement are roadmap. Custom trait vocabulary, patient availability and auth/compliance status
  are roadmap.
- **Engagement.** SMS confirmation and en-route only. **Agentic voice is explicitly out of scope** — offered
  as a partner integration or a professional-services build on someone else's API.
- **HCHB.** Not built. **No home health EMR experience at all** — Athena and Elation only. Needs our
  sponsorship into HCHB's partner program, or an RPA fallback they call less preferred and less scalable.
- **In development.** Branch capacity view and referral check — Q4. Demand ingestion from the EMR — Q4,
  dependent on vendor support.
- **Build with us.** The whole home health layer, **which they mark roadmap themselves**: episodic and
  payment-period planning, front-loading, LUPA-aware placement, pace against ordered frequency, compliance
  windows, authorization and readiness states, recert placement, supervisory co-scheduling, patient
  availability, points display, clinician results view. Plus HCHB. Plus engagement, through a third party.
- **Risk.** Their measured results (>10x ROI, +27% volume, >60% cut in third-party staffing spend, 6 months
  vs prior 6) come from a hospital-at-home program where **they volunteer that the platform was one component
  alongside staffing and clinical model change** — not an isolated measure of scheduling.

### UnityAI *(engagement only)*

- **Home health.** None. Their first line: *"UnityAI does not run a product of this nature today."* No home
  health, hospice or private duty customers. What runs elsewhere: outbound patient voice for a national
  radiology provider, staff scheduling across 100+ imaging centers, inpatient capacity management across 70
  hospitals, a behavioral health scheduling agent.
- **Capacity.** **Roadmap — no date yet.** Availability & reach likewise. Workforce supply is production with
  one customer, ingested from Workday.
- **Scheduling.** Matching is production with one customer — filters to hard constraints, ranks, a person
  decides. Routing & the week marked **"No."** Incentives **"No."** Multi-discipline coordination: **"No — we
  have not attempted this before."** Routing exists only as prior proof-of-concept work on Google's Route
  Optimization API.
- **Engagement.** **Strongest evidence submitted on this leg.** 8,000–10,000 outbound patient calls per day.
  Contact rate consistently **65%+** against the same call center's sub-40%; **75–80% of contacted patients**
  resolved to a confirmation or reschedule. Staff scheduling tool moved shift coverage from the mid-70s to
  consistently above **82%**, contingent labor 3% → 2%, no-tech cancellations 5–6% → 4–4.5%.
- **HCHB.** Not built. **Proposes routing around it** — source most data from our enterprise data warehouse,
  intake platform APIs and Workday, reserving RPA for write-back only. Flags that EMRs discourage RPA and
  that they would need our legal cover.
- **In development.** A staff-facing agent fielding call-offs, time-off and swap requests — a roadmap concept
  they want to build with us. Customer-controlled autonomy settings.
- **Build with us.** The capacity math, availability and reach, routing, incentives and care-team
  coordination — plus **the home health ontology itself**, which they are candid will be slow, librarian-like
  work.
- **Risk.** **This is a build engagement, not a purchase.** Architecture is rigorous — FHIR database as a
  workflow state machine, deterministic decision points inside agentic conversations, classical ML for
  decisioning with LLMs confined to conversation. SOC2 Type II, ISO 27001, HIPAA. But there is no product to
  buy on two of the three legs.

### Zeeva *(pre-production)*

- **Home health.** 100% home health focus, **zero production customers.** Platform built over the past year
  with input from industry experts; now opening to *"initial launch partners"* with white-glove engineering
  support. References promised, but no deployment to reference.
- **Capacity.** In development. Unit is a **Fill Confidence Score** — the real-time probability a visit will
  be accepted and completed, from clinician hours, individual acceptance history, rate sensitivity and route
  friction. Not headcount, not open calendar slots. **No other respondent proposed a way to make supply
  itself elastic.**
- **Scheduling.** In development; their own notes read *"READY (pending HCHB integration)."* Two tiers:
  full-timers receive geographic visit clusters sized to point targets, explicitly to break the **territory
  creep** that accumulates as patients admit and discharge; the remainder routes to a per-diem marketplace
  with dynamic pricing, route incentives, challenge bonuses, reliability ratings and radius map search. A
  cancellation on a full-timer's day is backfilled from the marketplace. Full-week planning, re-optimized in
  real time.
- **Engagement.** In development, dated **Q1–Q2 2027.** Design: suggests compliant windows to the patient,
  offers secondary windows if declined, escalates to branch staff if none work. SMS → AI voice → human
  handoff.
- **HCHB.** Not built. Automation-first for immediate deployment, transitioning to HL7/FHIR/APIs as volume
  scales. Reads open visits, patient and clinician detail; writes visit status and clinician assignments.
- **Build with us.** **Everything, plus the proof.** HCHB integration. Demand ingestion — they ask us what
  our intake platform is. Engagement on a 2027 timeline. Production hardening at enterprise scale from a
  standing start. No uptime history exists — their continuity answer describes design intent, not measured
  performance.
- **Risk.** Their stated end state is that *"the customer gradually transitions the entire workforce onto the
  marketplace."* **That is a change to our employment model and our relationship with our clinicians** — a
  workforce strategy decision, not a scheduling configuration.

---

## 4. Deep dive — MedArrive and CareConnect

The two respondents with no home health production. Both would have Compassus fund the home health layer,
and **they fail in opposite directions.** MedArrive has the engineering discipline and no engagement leg.
CareConnect has the engagement mechanics and the largest build list in the field.

### The two companies, on the facts

| | MedArrive | CareConnect |
|---|---|---|
| **What business they are actually in** | Software for hospital-at-home, SNF-at-home and at-home primary care. Pivoted from operating their **own field clinician services business**, since wound down. | Non-medical home care operations — plus recruiting/RPO, eLearning and compliance, and a 750,000+ caregiver talent network. |
| **Home health customers** | **None.** No home health, hospice or private duty. | ~15% skilled home health; ~80% non-medical home care, 5% hospice. **Names no home health customer or census.** |
| **Largest deployments** | 1,052 and 1,006 visits/month. Their own retired operation peaked at 1,121. | 22,900 / 12,400 / 6,600 active caregivers. |
| **HCHB** | Not built. No home health EMR experience at all — Athena and Elation only. | Not built. Scoped. HL7/FHIR APIs since 2024, live HHAeXchange integration. |
| **Capacity unit** | Hours and minutes. Points only as a roadmap display mode. | Weighted visit points — but the point table, ceilings and LUPA logic are all scoped builds. |
| **Patient engagement** | SMS confirmation and en-route. **Agentic voice explicitly out of scope.** | Production voice/SMS/email/push — **to caregivers.** Patient-facing outreach never attempted. |
| **Uptime evidence** | 99.95% trailing 12 months, 100% YTD, 99.9% contractual with service credit. | **99.97%**, ~3 hours across 6 discrete events. 99.9% baseline SLA. |
| **Their own roadmap markings** | Demand ingestion and branch capacity view **Q4**. Incentives roadmap, no date. | Routing & the week and Incentives both **Roadmap — no date yet.** |

### MedArrive — the findings that matter

**Origin.** MedArrive is a software company that used to be a staffing and field-services company. Before the
pivot they ran their own field clinician operation — ED avoidance and gap closure — and built this platform to
run it: **700+ clinicians across 11 states, peaking at 1,121 visits/month.** That business is wound down and
its team has moved on. The origin cuts both ways: the product was built under real operational pressure by
people who paid for their own bad schedules, but the operation is gone, so it is **not a reference** and the
scale it implies is not scale they can point to today.

**Claim vs evidence.**

| Claim | Standing | What it does and does not prove |
|---|---|---|
| >10x ROI, +27% volume, >14% operating cost reduction, >60% cut in third-party staffing spend, −13% admin time | **Qualified** | Measured by the customer's business team, 6 months post-go-live against the 6 prior. MedArrive volunteers the platform was **one component alongside staffing and clinical model changes** and would not present it as an isolated measure of scheduling. Credit for the caveat; the number still cannot be attributed to the product. |
| Planned vs measured visit duration: 90 → 70 min admission, 45 → 30 discharge, 49 → 41 across all types | **Strong** | Platform-instrumented and specific. **The most directly useful finding in either response** — a live test of whether a planning assumption is true, which is exactly what a point value is. |
| Six-month clinician adoption series — five metrics with healthy thresholds and actuals | **Strong** | Computed from platform data, no self-reporting. **The only vendor in the field to submit a full instrumented adoption series.** Non-home-health deployment, but the method is sound and repeatable here. |
| 700 clinicians, 11 states | **Retired** | Their own defunct business; they decline to present its operating metrics. Context, not evidence. |
| 99.95% trailing uptime, 100% YTD | **Unsupported** | See the continuity finding below. |

Their adoption series verbatim: 99% of completed visits closed by the assigned clinician rather than the
office (healthy ≥95%); 89% statused live from the field (healthy ≥85%); arrival median 4 minutes late with 95%
inside an hour; completion median 4 minutes early; 4% of visits canceled for scheduling or availability
reasons (healthy ≤5%).

**The production boundary — their own markings.** Production: per-clinician capacity math, drive-time-aware
scheduling, routing and intra-day resequencing with traffic, multi-clinician/multi-discipline visits as a
resource requirement, exceptions and call-out worklist, offline mobile with GPS auto-arrive/auto-complete and
clinician SOS. **Q4:** branch capacity view and referral capacity check (*the branch leader's answer to "can we
take this referral" does not exist yet*); demand ingestion of orders, frequencies, auth and admission events.
**Roadmap:** readiness states and placeholder visits; the entire episodic and compliance layer (front-loading,
LUPA-aware placement, pace against ordered frequency, recert placement); custom trait vocabulary, patient
availability and compliance/auth in matching; points as a capacity unit; rebook-within-window guarded by LUPA
exposure. **Out of scope by choice:** agentic voice, welcome calls, automated coverage outreach.

**Hours, not points — the one idea worth taking seriously.** MedArrive models capacity in hours and minutes
and argues it directly: the engine works in hours because drive time is real time, and a schedule that ignores
it is not executable. They will add a points *display*, but they will not plan in points. A point value is an
assumption about how long a visit takes — and their platform measures observed duration against planned and
**recalibrates the planning constants from a customer's own operating data.** If Compassus wants to know
whether its point table is true, **this is the only response in the field that offers a mechanism to find
out.** That is a real contribution, and it is also the argument for running them as an **instrumentation
partner** rather than a platform.

**Business continuity — the finding.** C6 asked how they think about business continuity. MedArrive answered
with uptime figures and a link to *MedArrive Disaster Recovery Strategy*. That document was read.

- **It does not support the answer.** Its own scope statement: *"This document focuses on disaster recovery
  and does not detail business continuity or incident response."*
- **Single-region.** Every mechanism described is availability-zone failover inside one AWS region — Aurora
  Serverless multi-AZ, Lambda across AZs, API Gateway and Cognito. **No multi-region failover anywhere.** A
  full region outage has no automated path.
- **Database failover takes 60–120 seconds**, during which *"the application may appear slow or experience
  failures. Failed requests must be retried"* — sometimes with *"an end-user seeing an error message and
  needing to retry."* A scheduler mid-assignment sees errors.
- **Catastrophic recovery is manual and unbounded.** *"A new database instance is manually provisioned from
  the latest PITR snapshot and the application is redirected."* **No RTO or RPO figure appears anywhere.** DR
  is drilled once a year.

None of this makes MedArrive unusually fragile — it is a conventional single-region AWS posture. But their
99.95% and 100% YTD claims sit on an architecture document that names no recovery objective. **Get the RTO/RPO
and the region-failure plan in writing.**

**Clinician model.** Assignment is **manager-mediated by default.** The clinician owns availability and time
off, sees their day and week update live, and advances visit statuses. Disagreement goes to a manager, who can
reassign. Specific clinicians can be granted direct assignment rights; conversely, the right to edit their own
availability can be revoked. Recording that a visit could not happen requires a Compassus-configured reason and
documents an outcome — **explicitly not a way to decline an assignment.** Full audit trail on every change.
Their stated ambition is to mine that trail for recurring patterns and surface them as recommended constraints
— **that is vision, not product.** One deployment lesson worth keeping: field staff resented advancing visit
status through four states, so MedArrive built GPS auto-arrive/auto-complete and made "en route" open Google
Maps. **They changed the product rather than the training.**

**Partnership posture.** Post-acute home health is a deliberate strategic move for them, not a side market.
*"We do not have a queue of enterprise home health customers whose requirements compete with yours. What is
agreed in the design partnership gets built next."* Read one way, that is the strongest design-partnership
argument anyone made. Read the other way, it restates that they have no home health customers at all. **Both
readings are true**, and the second is why commercial terms matter: Compassus would fund a home health product
MedArrive then owns and sells. They say they are open to outcome-linked economics but **decline to propose an
instrument.**

### CareConnect — the findings that matter

**The scoped-build inventory — the headline finding.** CareConnect's response follows one rhetorical structure
in almost every answer: name a capability that runs in production for home care, then list what will be built
for home health. **Their coverage grid marks 10 of 11 areas "Production — multiple customers." Inside the
narrative there are 26 distinct blocks explicitly labeled "Scoped Build," "Scoped Extension," or "scoped for
this deployment" — against 6 passages labeled "In Production Today."** That is the highest ratio of
promised-to-shipped in the field, and it is why **the coverage grid should not be read at face value for this
vendor.**

What is inside those 26 blocks:

| Area | Standing | Scoped for Compassus |
|---|---|---|
| Workforce supply | Scoped | HCHB import, assessing-vs-assistant role mapping across RN/PT/OT/SLP/LPN/PTA/HHA, SOC capability as a distinct attribute, competency and ramp on the record, managed float pool architecture, weekend/on-call rotation tracking. |
| Availability & reach | Scoped | **Territory modeling is "not yet built."** Plus home-base anchored reachability, pre-assignment drive-time filtering, time-aware predictive traffic, zip-to-branch import. |
| The capacity math | Scoped | Visit point weighting, productivity targets and ceilings, LUPA threshold tracking, provisional pending-auth load, inflow/outflow forecasting. The Liquidity engine underneath is production — **for shifts.** |
| Demand | Scoped | The HCHB connector itself. **485 handling is a new data class:** *"home care scheduling does not require it."* |
| Matching | Scoped | Continuity as a first-class ranking input, structured ingestion of HCHB free-text preferences, supervisory visit dependencies, clinical timing rules engine. |
| Routing & the week | **Roadmap — no date** | Multi-day balancing, LUPA front-loading, inter-discipline sequencing. Intra-day commute feasibility is production; week-level planning is not. Mobile turn-by-turn deliberately phased later. |
| Exceptions | Part scoped | Broadcast and claim are production. Missed-visit structured capture, 48-hour documentation and physician-notification tracking, root-cause analytics are scoped. |
| Before the visit | Scoped | **All patient-facing outreach.** Day-before confirmation, provisional assignment locking, en-route alerts, interactive reschedule handling. |
| Incentives & offers | **Roadmap — no date** | Structured differential ingestion, rule-based triggers, cost attribution, approval thresholds. |
| Across the care team | Scoped | Cross-discipline sequencing rules, linked supervisory visits, clinician performance view. |
| Readiness states | Scoped | 485/plan-of-care dependencies, POA consent flags, HCHB field mapping. The state machine underneath is production. |

**What is genuinely proven — and how far it transfers.** Over six months at an agency with 5,000+ active
caregivers: **50% of open coverage visits filled by clinician self-selection with zero coordinator
intervention**, up from 0%, baselined against legacy shift allocation logs; **38% of those completed visits
were claimed by caregivers coordinators had never successfully reached by phone**; 500+ additional completed
visits per week; 25%+ reduction in coordinator time on call-outs and new case allocation, verified by
time-and-motion study; a 293-caregiver at-risk cohort monitored 30 days showed +20% hours worked and attrition
under 10% against a non-monitored control. 99.97% uptime across 6 isolated events — **the most precisely stated
availability figure in the field.**

**The 38% is the number that should carry weight.** It is evidence that broadcast reaches supply that phone
trees structurally cannot — a mechanism, not a marketing number — and it transfers directly to per-diem and PRN
coverage in home health.

**What does not transfer is everything episodic.** Their engine's native unit is a **shift**; ours is an
**episode.** They say so themselves when explaining why cross-discipline sequencing must be built: *"Because
home care does not require multi-discipline interdependencies."* **That same sentence explains the 485 gap, the
LUPA gap, the supervisory-visit gap and the continuity gap. One root cause, not ten.**

**The adjacency question.** Non-medical home care is shift-based, per-visit, high-churn, low-credential, paid by
the hour. Skilled home health is episodic, caseload-based, credentialed, continuity-driven, paid by the 30-day
period. CareConnect is excellent at the first. **The question is whether a marketplace engine built for the
first shape can be extended into the second, or whether the second wants a different engine.**

**How the product works.** *ShiftMatch.AI* in three stages: hard eligibility gate (binary exclusions —
discipline, licensure, competency, authorization, territory), multi-factor ranking, then tunable guardrail
penalties that de-prioritize rather than exclude. **Two ranking modes** — for assigned full-time clinicians the
model scores *fit*; for PRN, float and call-out coverage it scores *predicted likelihood to accept*. **Using a
different objective for employed versus opt-in labor is a genuine insight.** Automation comes as Advisory
(default), Automatic, and a **Hybrid Review Window** (auto-assign with a configurable delay before the clinician
is notified). **Expansion is gated on match-agreement metrics** — how often the top-ranked candidate matches the
coordinator's final choice; divergence prompts recalibration rather than premature automation. Coverage runs a
five-stage pipeline; stages one to four are production, stage five is scoped. **Readiness** is an explicit state
machine — Order Received, Authorization Pending, Consent Outstanding, Patient Readiness Unconfirmed, Ready to
Schedule — where held visits count as provisional load and keep their SLA clock running, and *unready*
(administrative chase-down) is distinguished from *unassigned-ready* (staffing problem).

**The most sophisticated single idea in either response.** CareConnect explicitly guards against **"say-yes
bias"** — the failure mode where a predictive acceptance model over-allocates work to highly compliant
clinicians while quietly routing around frequent decliners. Their answer is to **escalate decline patterns to
branch leadership as workforce performance signals rather than hiding them inside algorithmic weights.** No
other vendor raised this. It is the characteristic pathology of acceptance-prediction models, and knowing about
it is strong evidence they have actually run one at scale.

**The HCHB path.** Not live, never touched. Phase 1 at ~90 days post-agreement — ingest via the HCHB
read-replica at **approximately 20-minute latency**, with an internal state machine processing local updates in
memory to avoid coordinator race conditions. Phase 2 at ~180 days — full bidirectional sync via HCHB's HL7/FHIR
write-back APIs or webhooks. Both contingent on Compassus providing sandbox access, API documentation, a
technical contact, and partner access facilitation, **which they note HCHB restricts.** Conflict resolution
defers to HCHB for clinical orders, authorizations and compliance SLAs. **Worth putting to them directly: Axle
judged 30-minute staleness from the same log-ship mechanism unacceptable and switched off. CareConnect proposes
to build on a ~20-minute read path. Both cannot be right about what home health scheduling tolerates.**

**Partnership posture.** Co-development rather than purchase: reduced upfront implementation fee, tiered
subscription, and openness to **tying a portion of ongoing fees to shared operational milestones** — LUPA
reduction, coordinator labor savings, visit completion, time-to-fill velocity. Executive steering from CEO,
Chief Growth Officer and Head of Engineering; co-marketing at NAHC, HC100 and HCAF with Compassus as flagship
home health reference client. Ownership stated plainly: *"Capabilities developed during this partnership enrich
CareConnect's core product"* — preferred pricing, priority access and first-mover advantage, **but not
ownership.** Of the two, **CareConnect is the more specific about outcome-linked economics**, which is the right
lever to pull.

**What they deliberately did not build.** No EMR or clinical documentation, no standalone EVV, no billing or
claims, and **no open marketplace that displaces existing clinician relationships** — external talent is
strictly an automated fallback after internal FTE and PRN rosters are exhausted. That is the opposite of
Zeeva's end state: **CareConnect is not proposing to change our employment model.**

### Head to head

| Dimension | MedArrive | CareConnect |
|---|---|---|
| Engineering discipline | **Stronger.** Honest roadmap markings, instrumented adoption data, correct resource modeling, volunteers caveats on its own numbers. | Solid architecture, but the response markets a product that is largely a proposal. |
| Supply-side mechanics | Thin. Coverage suggestions are roadmap; no automated outreach. | **Much stronger.** The only production evidence in the field of filling coverage without a coordinator. |
| Relevant scale | ~1,000 visits/month. Very small for us. | 22,900 caregivers at one agency — **but in the wrong workforce shape.** |
| Distance to home health | Roadmap for the whole episodic layer, **honestly marked.** | Same distance, but **presented inside a grid marked "production."** |
| Engagement leg | Declined. Would come from a third party. | Infrastructure exists; patient-facing application never attempted. |
| Continuity evidence | **Weak.** Single-region, no RTO/RPO, DR doc disclaims business continuity. | **Best in field.** 99.97%, 6 named events. |
| Commercial ask | Open to outcome-linked economics; declines to propose an instrument. | Specific about outcome-linked fees and named metrics. |

**The judgment.** Neither is a platform purchase. Both would have Compassus fund the home health layer, and both
are explicit that the resulting product enriches the vendor's own roadmap — which makes the **value-share
conversation more consequential for these two than for any other respondent.** If they go forward at all, they
go forward as different things: **MedArrive as an engineering/instrumentation partner** (the
duration-recalibration capability alone could tell us whether our point table reflects reality), **CareConnect as
a supply-side partner** (the 38%-of-fills-from-unreachable-caregivers finding is the single most transferable
piece of evidence either company submitted). **Neither can carry capacity, scheduling and engagement in home
health on HCHB.**

### The scoped read, for the capacity-and-scheduling question only

When the question is narrowed to *a home health product that fixes capacity and scheduling* — explicitly **not**
a supply-side partner — the argument runs three ways:

1. **The 15% buys nothing.** It is a customer-mix figure, not a capability. CareConnect names no home health
   customer and quotes deployments in caregiver headcount. Their own response calls the plan of care **"a new
   data class for us."**
2. **MedArrive's problem shape is ours.** Hospital-at-home and SNF-at-home schedule multi-discipline visits
   inside clinical windows, with real drive time and co-visits needing two clinicians. CareConnect fills hourly
   shifts. **Adding points to a visit engine is configuration; turning a shift engine into episodic scheduling
   is architecture.**
3. **They report honestly, and we are buying a build.** MedArrive writes "Q4" and "roadmap" where things are
   unbuilt. CareConnect marks 10 of 11 areas "production" while the narrative behind it carries 26 items scoped
   as builds for Compassus.

Against what we need, on each vendor's own status markings:

| What we need | MedArrive | CareConnect |
|---|---|---|
| Territory and drive-time reachability | In production | **Not built** |
| Matching and routing the day | In production | In production |
| Routing the week | Partial | **Roadmap, no date** |
| Branch envelope — load vs open room | In development, Q4 | Scoped build |
| The episode — front-loading, LUPA, windows | Roadmap | Scoped build |
| HCHB integration | Not built | Not built |

---

## 5. Diligence questions to carry into the demos

**MedArrive**

1. What is your RTO and RPO, in writing? Your DR document names neither, describes single-region AZ failover
   only, and states it does not cover business continuity. What happens in a full region outage, and how long
   until schedulers are working again?
2. Q4 is named twice — branch capacity view, referral check, and demand ingestion. What is committed, by whom,
   and what happens to our timeline if HCHB support is not there?
3. Show us the duration-recalibration capability against real data. If we handed you six months of our visit
   history, what would it tell us about our point values?
4. Your largest deployment is roughly 1,000 visits a month. What in the architecture has been tested above
   that, and what have you never run at scale?
5. You have declined the engagement leg. Name the partner you would bring, and tell us who owns the integration
   risk between you.
6. The audit-trail-to-recommended-constraints idea is compelling. Is any of it built?

**CareConnect**

1. Your grid marks ten of eleven areas production, and your narrative names 26 scoped builds. Walk us through
   the grid line by line and tell us what a Compassus branch could use on day one.
2. Routing & the week, and Incentives, are both Roadmap with no date. Routing is the middle of our scope. When?
3. Territory modeling is "not yet built." How do you run a branch coverage area today without it?
4. Axle switched off its HCHB integration because ~30-minute log-ship staleness was below their bar. You propose
   building on a ~20-minute read path. Why are they wrong?
5. Caregiver Choice fills 50% of open shifts in non-medical home care. What is your evidence it behaves the same
   way for a credentialed SOC visit inside a compliance window?
6. You have never sent a message to a patient. What is the first patient-facing workflow you would build, and
   how would we test it before it reaches a real one?
7. Phase 1 at 90 days and Phase 2 at 180 assume partner access we have to secure. What is the plan if HCHB says
   no, and who carries the delay?
8. The say-yes-bias safeguard suggests you have hit this at scale. Tell us what happened.

**Both**

1. You would each build our home health layer and then own it. What specifically do we get for funding it —
   equity, exclusivity, perpetual pricing, ownership of jointly developed capability?
2. Give us a reference operating at our **shape**, not just our scale — episodic care, credentialed staff,
   compliance windows — or tell us plainly that one does not exist.
3. What breaks first when this goes from one pilot branch to fifty?

---

## 6. The scorecard rubric — formula audit

Reviewed: `VendorScorecard Rubric 9.4 (1).xlsx`, Scorecard tab. **The question asked was whether each vendor's
total is comparable. It was not.**

**The bug.** `IFERROR(...,0)` wrapped every section grade, which made an **unscored cell indistinguishable from
a genuine zero**. A part-scored vendor was therefore compared against a fully scored one on a lower base. All
section grades were also gated on a single cell (`G17`, the A1 answer), so a blank A1 blanked sections that had
in fact been marked. Row 8's HCHB divisor was hardcoded to `20` rather than reading the list's own top rung, and
the stop-check row only looked at the A1 answer.

**Observed effect.** Unity AI showed **TOTAL 22 / "Conditional — Decline"** with **44 of 100 weight points
scored as hard zeros** because rows 36, 40 and 43 were blank. **Normalized to assessed weight it was 39.**

**The fix** (delivered as `VendorScorecard Rubric 9.4 - formula fix.xlsx`, generator preserved at
`scratchpad/fix_rubric.py` in the session that produced it):

- **Row 3 (total)** now appears only when all thirteen marks are in: `=IF(count<13,"",full_total)`. Blanks can
  never read as zeros.
- **Row 4 (band)** reports `Incomplete — n/13` until complete, and prefixes `STOP —` when any stop-check is
  open.
- **Row 5 (stop-checks)** counts rows 18, 19 and 37 independently rather than gating on A1.
- **New row 6 ("Scored")** shows `n / 13` plus a **provisional score normalized to the sections actually
  assessed** — so a part-scored column is still readable without being falsely comparable.
- **Row 8** divides by `MAX(Lists!$C$2:$C$7)` instead of a hardcoded 20.
- **Rows 9–14** are each gated on their own marks.
- A note documenting the change was added to the `Start Here` tab.

**Verification.** Example-tab totals were unchanged (85 / 58 / 67), proving the fix does not alter a complete
column. Four defined names (`CapacityInputList`, `DeliveryList`, `InScopeList`, `StatusList` — all `[1]Lists!`
external refs used only by the Unity AI tab) were dropped by the LibreOffice round-trip and were **restored by
re-injecting the original `<definedName>` elements into the output zip.**

> **Open.** The shared workbook's content `modifiedTime` was **2026-09-04**, which predates several
> questionnaire returns, and **only Unity AI carried marks.** No other filled scorecard exists in the accessible
> Drive. The user believed all vendors had been scored — **the correctly-filled workbook has not yet been
> located, and the audit should be re-run against it.**

---

## 7. Sources — Drive folder `1vJ0KC-ZhISmEWbsw34x2gB3BP7JkljsK`

Vendor questionnaire working folder. Owner `worker@workforcewave.com`.

| File | Drive ID |
|---|---|
| `HCHB Compassus Capacity Scheduling Vendor Questionnaire 2026.xlsx` | `1fxFIzs2g7urF-S1f9tyH2BwGCYcom3B1` |
| `Axle HealthCompassus Capacity & Scheduling Vendor Questionnaire.xlsx` | `1hppu0Bho83LcYAwFajlb6jfYnE79h7yW` |
| `[ARYA HEALTH Compassus Capacity & Scheduling Vendor Questionnaire.xlsx` | `1eJpwFWChpfuz3NZMqyWwC3TFdq-GENGn` |
| `Carestitch Capacity & Scheduling Vendor Questionnaire (1).xlsx` | `10o0SVIjwSV9SifsLi2qN_B-13M4M_UtM` |
| `VitalisCare Compassus Capacity & Scheduling Vendor Questionnaire.xlsx` | `1leY3bM-a_nKCw_KLCI2PtgME_sLMt35r` |
| `Servis.ai Completed Compassus Capacity & Scheduling Vendor Questionnaire.xlsx` | `1nccLXHBNGxqivhcCPsr61NCr5FDXiY1Q` |
| `Care Connect Compassus_RFP Final.xlsx` | `1qwaiuTUmJsi9ewIofpRBWAf24OkmqWXZ` |
| `AutoMynd  Compassus Capacity & Scheduling Vendor Questionnaire.xlsx` | `1fUf9uPGNWnPhM5_-MgVqRnKzrQoyLmPi` |
| `MedArrive Compassus Capacity & Scheduling Vendor Questionnaire.xlsx` | `1BA6HQMCsmlPrAv1WSN4CQ5hS1_wplblB` |
| `UnityAI Response to Compassus Capacity & Scheduling Vendor Questionnaire.xlsx` | `1ONlsHQn9dVvnL22UHkxvx3qjTmYH5fMT` |
| `Zeeva Submission - Compassus Questionnaire.xlsx` | `10c5vxS9HIkcjkT_1eWCUE6Zcs8G4idYJ` |
| `VendorScorecard Rubric 9.4 (1).xlsx` — **content modified 2026-09-04; only Unity AI marked** | `1FbLjujC0sgq92crIc3_f2ukt4qxxbZ4f` |
| `HCHB Smart Scheduling - VCG Case Study.pdf` | `19MtR23zhUswlaNp8upx5YzPRkQNShi7C` |
| `HCHB - Smart Scheduling one-pager 2026.pdf` | `1yZrqJFsh0gShUAhfxJI8eWGFtMCRkxvn` |
| `servis ai proposal for compassus.pdf` | `1EnflP_X12nibRD7PjAOo6amLcUs92Rsu` |
| `Servis.ai - Proposal Assessment.docx` | `1GzqqPdLRH_Q_riQ035GGfcj-nWx5bBqv` |
| `Zeeva Cover Letter - Compassus Questionaaire.pdf` | `1mFqCGVigVVrcsxQL2D_Te3Y-LWfiumd1` |
| `Zeeva Team Bios .pdf` | `1Z4PBXK3Q58tAGj1L4WQPxZjVCvzkf02N` |
| `VendorResearchMatrix.xlsx` | `1w2T7eu1_8ytk0mNKvqvnK9jO2S78Uuwe` |
| `Vendor Capital Brief.pdf` | `1TMh0t6wfOzriLEYLU8rW2pqLhiSiVkTI` |

**Deliverables produced from this material and published back to the folder:**

| Deliverable | Drive ID |
|---|---|
| `Compassus Capacity  Scheduling  Vendor Breakdown.docx` — the 11-vendor breakdown, 10 pages | `16cFgEXVzf10r4TXfJ36oDIVlsCSRqWar` |
| `MedArrive vs CareConnect  Vendor Assessment.pdf` — the one-pager for leadership | `1_P1sp4nIc83ZL9wyS0mDQZGXGaawKaW_` |

Also referenced: **MedArrive Disaster Recovery Strategy** (PDF linked from their C6 answer) and the
**CareConnect × HCHB integration architecture tab** inside their workbook.
