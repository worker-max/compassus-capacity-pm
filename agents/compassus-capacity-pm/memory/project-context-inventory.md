# Project context inventory

The initiative at full depth, assembled by reading the whole repository in September 2026 for the
handoff pack. Paths are repo-relative from `agents/compassus-capacity-pm/` unless stated. Quoted
text is the project's own wording.

---

## 1. The initiative in 25 facts

**Who, what, scale**

1. Compassus home health. The initiative makes *"finite, geographically-distributed clinical
   capacity reliably meet variable, time-sensitive demand — without harming patients, clinicians,
   quality, or margin"* (`README.md`). Program shape: *"plan it, prove it in a lighthouse branch,
   scale it across the org, then govern it as a standing operating discipline"* across five gated
   phases, Discover → Design → Pilot → Scale → Sustain (`initiative-playbook.md`).
2. Scale: about 80 branches (business case base), about 3,000 clinicians, about 300 schedulers
   today and about 100 in the target state (`knowledge/business-case-and-kpis.md`;
   `artifacts/business-case-register.md`). AGENT.md says the model must *"survive contact with 100+
   branches."* Revenue anchors: about $549M home health, about $260M Medicare fee-for-service.
3. HCHB, Home Care Home Base, is the system of record: *"All tasks, plan of care, scheduling
   workflow, and visit records live here. Not real-time; requires manual sync."* Its clinician app
   is Point Care, on Citrix, manual sync.
4. The rest of the landscape: Commure (intake and referral), NestMed (real-time documentation),
   Pulse (utilization review), Workday (HR and PTO; *"Integration with HCHB exists but is NOT
   currently activated"*), an external ICD-10 coding vendor, Circadia Health (AI patient calling in
   some California locations).
5. *"The scheduling problem is not a scheduling problem."* Schedulers spend most of their time on
   administrative workflow inside HCHB; the inefficiencies are upstream: documentation delays, DCS
   bottlenecks, authorization holds, fragmented capacity management. *"Scheduling gets blamed
   because it is the final visible touchpoint."*
6. *"Capacity is a planning function — what the branch can absorb. Scheduling is an execution
   function — who goes where, when."* Both run through one manually maintained spreadsheet grid, so
   neither is performed well. **Capacity management must be solved first.**

**Branch roles**

7. Scheduler is an administrator: *"The only true scheduling decision a scheduler makes is the
   start-of-care intake call."* Their day: receive HCHB workflow tasks after DCS review; click
   pre-plotted visit blocks and assign a clinician; manage coordination notes; process missed-visit
   tasks (48-hour MD notify); 50–60 auth notifications a day, most non-actionable; one patient
   call, the SOC welcome call.
8. DCS, Director of Clinical Services, reviews and approves plan-of-care documentation before
   scheduling. Four-task checklist: plan-of-care review, calendar accuracy, pending auth
   management, plan-of-care lock. *"Spends the day pushing workflow instead of managing
   utilisation and team performance."*
9. ED, Branch Executive Director: growth and finance lens. Growth is gated by SOC availability;
   the overload cycle halts growth; both overstaffing and underutilization hurt margin.
10. Clinicians run their own week: call patients the evening before, confirm or reschedule, accept
    their slate each morning, plot visits on their own calendar. In steady state *"there is no
    scheduler workflow at all unless a visit must be reassigned."* Their weekly planning logic is
    *"entirely undocumented and unassisted today."*
11. Four audiences, four yardsticks: *"ED → growth/margin; RN → workload/burnout; scheduler →
    execution speed; patient → reliability and continuity."* The patient's line: *"schedule your
    clinicians around us — our care needs, our urgency, and our preference for consistency."*

**Reimbursement mechanics**

12. PDGM pays per 30-day period. *"Two 30-day payment periods sit inside one certification period,
    each independently assigned a case-mix group and therefore its own LUPA threshold and its own
    payment amount."* *"A system that models only the certification period cannot see the payment
    cliff it is walking toward."*
13. 432 case-mix groups: admission source (2) × timing (2) × clinical grouping (12) × functional
    impairment (3) × comorbidity (3).
14. LUPA is the floor and it is a cliff. Below the group's threshold the period is paid per visit.
    Thresholds 2 to 6 visits, recalibrated annually (eighteen groups moved by one visit for CY 2026).
    *"The alert has to carry the remaining days and the visits still needed"*; *"the guard should
    sit above the floor, not at it."*
15. There is also a ceiling: above threshold *"every further visit is cost with no matching
    revenue."* Target: *"the clinically right number, above the LUPA threshold and no higher than
    the period payment supports."*
16. Three ceilings, never conflated: auth is permission, LUPA is the floor, utilisation management
    is the ceiling. Fourth for non-episodic payers: the annual benefit cap.
17. Compassus is majority non-traditional Medicare and HCHB was built for a 90% Medicare book,
    *"the root cause of most authorization friction rather than anyone's negligence."*
18. Payer classes run risk in opposite directions: episodic (LUPA below, margin erosion above),
    per-visit (missed visit is lost revenue), managed care (authorization caps delivery).
19. CY2026 rate pressure: permanent −1.023% plus a one-year 3.0% reduction. A CMS six-month
    moratorium on new home health and hospice Medicare enrollment (May 2026) converts the initiative
    *"from an efficiency program into the growth strategy."*
20. Compliance windows pre-consume capacity: 48-hour MD notification on a missed visit; 60-day
    certification; PT 30-day reassessment; 14-day HHA supervisory visit; 48-hour ROC; SOC within 48
    hours; the Medicare week runs Sunday–Saturday; OASIS visits are date-bound.

**Current-state pain**

21. Pending-auth invisibility: *"A visit that has been ordered but not authorized exists in no
    view."* The scheduler carries it in her head or on a sticky note. *"The clearest
    capacity-measurement defect in the current state."*
22. Notification storm: HCHB *"creates a pending-auth workflow every day per patient … roughly 50 a
    day, almost all with no available action."* Bulk-clearing becomes habit. Rule: **notify on state
    change, never on state persistence.**
23. Alabama Smart Scheduling failed on change management: *"Leaders constrained the system to mirror
    existing manual processes … clinicians rejected the assignment … The system was never allowed
    to do what it was designed to do — it was never truly piloted."*
24. Twelve bottlenecks ranked by leverage; the first four worth solving first: the authorization
    cycle, pending-auth invisibility, DCS QA and order approval, per-discipline task duplication;
    then territory, discipline-role match, call-out recovery, clinician confirmation calls, the
    readiness call, workflow noise, per-diem capacity, POA identification.
25. Business case of record: $7.9M/yr moderate across about 80 branches ($4.0M conservative, $14.3M
    hopeful; MVP captures 60%). The adversarial verdict: *"Do not fund a platform purchase now. Fund
    a two-quarter measurement and configuration phase, and set gates."* Three-year cost of
    ownership $21.7M; software licensing about 10% of it.

**Target state**

- Three modules (DE-02): Capacity Management, Scheduling Engine, Patient Engagement. Capacity is
  Phase 1 and Phase 1 is visualization only (DE-03). *"The capacity tool replaces the scheduling
  grid. They are the same object; do not build both"* (DE-04).
- *"The MVP does not build the schedule … The first job of this product is not to optimise
  anything. It is to make capacity measurable and observable."*

**KPIs.** Primary: quantified capacity and utilisation (not available today), referral turn-down
for no capacity (no), premium and contract labor (partial), LUPA rate and leakage (partial),
clinician turnover (yes). Secondary: time to SOC vs 48 hours, missed and rescheduled visit rate,
continuity, schedule churn, caseload balance, productivity vs potential, coordination latency, tool
adoption (*"MVP-critical: if it is not used, none of the rest happens"*). *"Capturing the baseline
is itself part of the work."*

## 2. Vocabulary

| Term | Definition |
|---|---|
| SOC | Start of care. Initial evaluation visit. Skilled nursing goes first if ordered. Seen within 48 hours. |
| ROC | Resumption of care after hospitalisation; same nursing-tie rule; 48-hour rail from discharge. |
| Recertification | Renewing the plan of care at the end of a cert period; window days 56–60; binds only recertifying disciplines. |
| DCS | Director of Clinical Services. |
| PCC | Patient care coordinator; makes the readiness or welcome call. |
| TIC | Time to initial care, from referral acceptance to first visit; the compliance clock starts at referral. |
| POC / 485 | Plan of care and its document. *"The 485 is a moment, not a sequence of gates."* |
| Auth | Non-Medicare payer authorization for a number of visits. |
| Pending auth | See the patient, submit documentation, authorization follows. Not universally payable. |
| Pending-auth allowance | Visits schedulable before further auth; *"some one, some three, some five, some ten"*; set by the payer. |
| Completion gate | Payer requires N of M visits completed and documented before more are granted. |
| Benefit window | Calendar limit, sometimes keyed to hospital discharge date. *"The clock starts before we do."* |
| Shared pool | Several disciplines draw from one allowance. |
| POSFC | Physician order for start of care; resets the TIC clock. |
| Buddy codes | Cosign codes required in some states (Ohio, California). |
| PDGM | Patient-Driven Groupings Model. |
| LUPA | Low Utilization Payment Adjustment; the per-visit floor; a cliff. Never cleared by padding visits. |
| Over-utilisation ceiling | Above threshold, every visit is cost with no revenue. Read posture. |
| OASIS | The date-bound assessment; its visits cannot be freely moved. |
| HHVBP | Value-based purchasing; cohort-relative; OASIS functional measures are 40% of the score. |
| CoP | Conditions of Participation. The physical calendar in the home is a CoP requirement. |
| The envelope | How much work the branch can deliver. |
| The seam | Same data: *"how much can we take?"* is capacity; *"who does this visit?"* is scheduling. |
| The hinge | The capacity decision in the six-step spine: referral → capacity decision → schedule → visit → period revenue. |
| Committed load | Points or visits already scheduled against a clinician; pending-auth visits count. |
| Open room | Σ expected − Σ earned, reframed as available capacity. |
| Open slot | Undefined and named as such. |
| The scheduling grid | The manual spreadsheet the capacity tool replaces. |
| The point system | The undefined shared currency. Tool weights: SOC 2.5, recert 1.75, eval 1.5, reassess 1.25, discharge 1.75, routine 1.0. |
| WVP | Weighted visit point. |
| Assessing vs assistant | RN, PT, OT, SLP versus LPN, PTA, COTA. |
| The SOC rule | RN performs any SOC where nursing is tied; PT only when nursing is not on the referral. *"Clinical law, not a preference."* |
| Routine bleed | Assessing clinician running routine visits while assistant capacity is open. |
| The overload cycle | Full of routine → no SOC bandwidth → no growth → still overloaded. |
| Front-loading | Pace against the plan of care; about 42% of target by Tuesday. |
| Resting posture | Territory set so a nearby referral is absorbed almost automatically. |
| Float pool / per diem | No territory on purpose; the targeted capacity instrument. |
| Fill order | Contractors → full-time → part-time → per diem, checking the contractor is additive. |
| Soft capacity | What a clinician is actually willing to do above or below the formal expectation. |
| The five dispositions | Accept, Reschedule, Reassign, Miss, Decline. Reassign carries a plan; Decline carries none. |
| Rapid reschedule | HCHB flag: an in-week reschedule generates no scheduler workflow. |
| Shift Finder | HCHB capability, not enabled: clinicians see uncovered visits and accept one. |
| Visit dispatching | HCHB smart scheduling recommending the next assignee; does not auto-assign. Not enabled. |
| NVA | Non-visit activity codes 5001 / 5003, weight 0.25. |
| Read / Assist / Control | Software may display; recommend and a human decides; drive it. |
| Posture overreach | The product drives what we said it may only assist or read. |
| Gating variable | Hard or structural constraint in the MVP; a knockout. |
| The flare button | One action on a call-out that triages and recommends. |
| Readiness gauntlet | DCS review, pending auth, POC lock, face-to-face or coding hold. |
| Reciprocity ledger | Discretionary effort is real capacity, borrowed, and must be repaid. |
| POA | Power of attorney; must sign consents; some require no patient contact. |

## 3. The scope taxonomy

The 41 elements are in `.claude/skills/vendor-scorecard/assets/spec-elements.json` and
`vendor-evaluation/handoff/spec-elements.json`, verbatim. CAP 11 + SCH 14 + ENG 16. Two quirks:
ENG-12 (incentives) sits in its own group after ENG-13 in file order; ENG-01 and ENG-02 have no B
area and are evidenced from C7 and D1.

The one-pager (`artifacts/capacity-scheduling-one-pager.html`) is the primary-variables view: 22
capacity variables, 47 scheduling, 12 engagement, from the 8.13 workbook. Behind it sit 76 numbered
variables plus 3 unnumbered scored rows (Insurance Authorization, Add-On Orders, Clinician Safety)
that *"are invisible to the Functional Scorecard rollups."* The authoritative workbook is on Drive,
not in the repo; `knowledge/workbook-2026-08-13.md` indexes it with Constraint / MVP / Posture.

## 4. What our own thinking says a good solution does

**The ten decisions, DE-01 to DE-10** (`knowledge/whiteboard-session-2026-08-13.md`). Load-bearing:
DE-02 three modules; DE-03 capacity first, visualization only; DE-04 the tool replaces the grid;
DE-05 care team assigned at referral, system recommends, human approves; DE-08 discipline-role
match defaults to the paraprofessional with opt-out; DE-09 *"The tool recommends; the human
accepts"*; DE-10 a human scheduling role survives at reduced scale.

**HCHB authoritative; the clinician originates frequency.** CN-06: *"no tool should generate
frequency independently."* CN-08: scope filtering is a correctness requirement. CN-02: any
self-service visit moving must refuse OASIS visits. The engine's job on margin is *"to make the
consequence visible at the moment the decision is made"*; it *"may never enter an objective
function or weigh against clinical need."*

**The Read / Assist / Control ladder.** Shows it (1, Read), Checks it (2), Recommends it (3,
Assist), Runs it (4, Control). *"A 4 is not automatically good. Where Compassus set an Assist
boundary, a product that decides on its own is an overreach to flag, not a bonus."*

**The capacity stack** (`strategy/capacity-strategy-foundation.md`): referrals (precondition) →
staffing model (primary effector) → territory (resting posture) → day-to-day (the cockpit) →
culture and leadership (multiplier). *"Fix the stack bottom-up; manage it top-down."*

**The five SME convergences.** Capacity is created at the SOC slot and lost when the assistant tier
is understaffed; SOC capacity is protected inventory; capacity is not visit count (visit + drive +
documentation + coordination + acuity); discretionary effort is borrowed; the tool is part of the
culture and cannot be neutral: propose, don't dispose; show the cost; never manipulate.

**The never list.** Propose, don't dispose. Scope and the SOC rule are hard rails. Compliance
windows pre-consume capacity. Never raid SOC slots for routine overflow. Capacity is time, not
visit count. Protect the reliable clinician. Never manipulate; a *no* is data. `patient_confirmed`
visits are immovable without human release. Distinguish structural from transient. Stale clinical
data blocks auto-eligibility. Never be a black box.

**What the case must never claim.** Visits added to clear a payment floor; margin in an objective
function; fewer visits as a goal; telehealth substituting for a floor visit; star ratings delivering
referral growth; any saving that depends on a manager working weekends.

## 5. Known traps

| Trap | The project's words |
|---|---|
| A higher score can be a worse fit | *"HCHB Smart Scheduling rates highest and overreaches our stated automation posture on 16 variables. That is the Alabama failure expressed as a number."* |
| Configurable is not coverage | *"Also partial, always: 'configurable', an open API, a partner delivering it, a dated roadmap item, and any claim with no supporting detail."* |
| Claim vs evidence | *"Section B is their claim; Section C is the evidence."* |
| Language shift | *"Marketing prose in Section C and specifics in Section E usually means the product is thinner than the pitch. The reverse means an engineer wrote it."* |
| Optimisation gains overclaimed | *"Vendors claim 20–40%. Divide by two to three."* |
| No evidence base | *"Not one peer-reviewed or quasi-experimental evaluation of any home health scheduling product. Every vendor case study is n=1 with no control."* |
| Two systems owning the schedule | *"The failure mode that hurts most."* |
| Route optimisation as cost lever | *"With 70% of clinicians paid per visit, we pay the same per visit either way. This kills the standard industry pitch outright."* |
| The market read | Top candidates understand capacity and scheduling; *"few have thought through patient engagement."* |
| Constraint fidelity beats algorithms | *"The single most robust success factor is constraint and duration fidelity, not algorithms."* |
| Base rates | Large IT projects deliver 56% less value than predicted; under 30% of transformations succeed; 40–60% are never tested against outcomes. |

**Constraints a vendor must respect.** Union: territory is not something a union can dictate but
the position was used as leverage (CN-49); incentives need union approval and a union-population
variant (CN-50); salaried and hourly populations cannot be incentivised per visit (CN-51). Payer:
allowances derived from the payer (CN-12); completion gates are forward-looking scheduling
constraints (CN-13); windows keyed to discharge (CN-14); shared pools (CN-15); mandated discipline
substitution (CN-16); pending auth not universally payable (CN-17). State: California robocall
treatment needs legal confirmation (CN-10); Washington safety screening (CN-37); buddy codes;
Jacksonville bridge, California interstate hours. Consent: text and email need signed consent at
SOC (CN-09); POA (CN-11). Privacy: aggregates, minimum necessary, no PHI beyond the task. EVV:
not in the repo. HCHB product limits CN-22 to CN-30: invisible pending work; daily notification
regeneration; clinicians cannot reassign their own visits; supervisors cannot see supervisee
schedules; per-discipline task duplication; documentation invisible until sync; capacity only as
manual reports; seven-day schedule horizon; coordination notes as the only routing. Once a
clinician accepts a visit for the day, the back office cannot remove it. HCHB as a partner: no
public API; HL7v2 and CCD over SFTP; sells a competing optimizer; 44% Medicare share, 97.6%
retention; FHIR marketplace in 2027.

**Cultural traps.** Bulk-clearing (CN-39); schedulers declining the readiness call (CN-40);
clinicians stopped calling in for backup visits, *"latent capacity is being lost to a trust
deficit"* (CN-41); tenured clinicians resist territory flexibility (CN-42); machine-assigned visits
rejected where human-assigned ones would not be, *"the central adoption constraint"* (CN-43); newer
clinicians cede schedule control to patients; the first visit at 8 or 9am is the single largest
lever on individual capacity (CN-44); PTs retain PTA-appropriate visits (CN-45); incentive holdout
(CN-46); branches refusing per diem forfeit growth (CN-47); coverage runs on relationships (CN-48).
Design traps: making decline too easy; never give a hard time, give a range; paraprofessional
supply limits the DE-08 default market by market.

## 6. Source-of-truth map

| Topic | File | Recommendation |
|---|---|---|
| Best one-page brief in the repo | `knowledge/README.md` | Include whole; if only one file can be carried, carry this |
| The 41 elements | `.claude/skills/vendor-scorecard/assets/spec-elements.json` | Include whole, verbatim |
| The one-pager as the vendor saw it | `artifacts/capacity-scheduling-one-pager.html` | Excerpt the markup, strip the CSS |
| Variable inventory with posture | `knowledge/workbook-2026-08-13.md` | Include whole |
| Constraints | `knowledge/constraint-register.md` | Include whole; the class labels are the point |
| Bottlenecks | `knowledge/bottleneck-dossiers.md` | Whole, or dossiers 1–5, 7, 11 |
| Payment mechanics | `knowledge/payer-and-episode-economics.md` | Whole minus the ID-collision box |
| Discovery ground truth | `knowledge/discovery-session.md` | Include whole |
| Capacity vs scheduling framing, open questions | `knowledge/capacity-scheduling-summary.md` | Include whole |
| The ten decisions | `knowledge/whiteboard-session-2026-08-13.md` | Include whole |
| Process facts | `knowledge/process-facts-2026-08.md` | Excerpt through recertification and discharge |
| Business case and KPIs | `knowledge/business-case-and-kpis.md` | Include whole |
| Adversarial verdict | `artifacts/business-case-verdict.md` | Include whole |
| Benefits inventory | `artifacts/business-case-register.md` | Summarise; include §11 and §12 verbatim |
| Design principles corpus | `MASTER-capacity-and-scheduling.md` | Never whole; excerpt the executive summary, the convergences and guardrails, the field-RN hard truths |
| Capacity stack | `strategy/capacity-strategy-foundation.md` | Include whole |
| Tactics | `sme/capacity-tactics-library.md` | Include whole |
| SME long-form | `sme/perspectives/*.md` | Summarise, except the field-RN hard-truth summary |
| Agent identity | `AGENT.md` | Excerpt the grounding block and the mental models |
| Program phases | `initiative-playbook.md` | Summarise to phases and gates |
| Model gaps | `artifacts/capacity-ecosystem-map.md` | Include whole |
| At-risk variables | `artifacts/variable-backlog.md` | Excerpt sections A, C, D |
| Beacon | `CROSS-REFERENCE-BEACON.md` | Omit; a session-identity token |

## 7. Gaps the repo cannot fill

Not in the repo: Electronic Visit Verification; a Compassus company profile; the vendor roster (only
fragments: MedArrive, Circadia, Aria Health, *"top four or five candidates"*); the primary 8.13
workbook and its Drive sources (indexed only); the returned questionnaires. Named as missing by the
project: a verified payer-rule library (*"a schema with three unverified entries"*); authorization
turnaround by payer; the point system; the definition of an open slot; KPI baselines; eleven finance
inputs including the pay-model split and the episodic period count (80,000 vs 128,000, *"resolve
this before any readout"*); the variable-ID collision at S-43; legal answers on robocalls and
consent timing; the future-state process map; weekend, aide, MSW, ST and hospice paths; who is who
(Colin, Laci, Evan appear by first name; no titles, no org chart).
