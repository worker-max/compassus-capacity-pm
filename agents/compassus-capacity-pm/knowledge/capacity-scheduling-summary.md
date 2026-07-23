# Home Health Capacity & Scheduling — Consolidated Summary

> **Source:** Google Drive — "HH_Capacity_Scheduling_Summary." Consolidated meeting summary and foundational
> knowledge base, from a working-session transcript plus multi-perspective expert extrapolation. Purpose:
> foundation for functional requirements of a scheduling & capacity automation platform. Rendered faithfully.
> A lighter earlier draft ("Foundational Knowledge for Home Health Capacity and Scheduling") and the raw
> four-perspective chat log are the same material at lower fidelity — this document supersedes them.

## Executive Summary

Capacity and scheduling are treated as a **single undifferentiated problem** in current branch practice, and
that conflation is itself a root cause of the operational failures. **Capacity is a planning function** — what
the branch can absorb. **Scheduling is an execution function** — who goes where, when. They operate on
different time horizons, are owned by different roles, respond to different inputs, and fail in different ways.
Because branches manage both through the **same artifact — a manually maintained spreadsheet grid** — neither
function is performed well, and the connection points between them are invisible.

### Principal Findings

- **SOC clinician availability is the binding constraint on branch growth.** When SOC-capable clinicians are fully consumed by routine visit volume, the branch cannot admit new patients regardless of referral demand.
- A **self-reinforcing stagnation cycle**: full caseloads prevent admissions, absence of admissions prevents caseload turnover, and the branch stays locked at its current volume indefinitely.
- Capacity is calculated manually, in spreadsheets, at branch-level discretion. No standardized method, no shared definition of an open slot, no real-time view of where capacity exists.
- Scheduling operates on a **weekly build with continuous mid-week disruption.** The plan is finalized early; last-minute orders, cancellations, and condition changes then force continuous manual reconstruction.
- **Branch-to-branch variability is extreme and unmanaged.** High performers reassign coverage in minutes; low performers take hours, during which clinicians idle and patients wait.
- The **intake-to-scheduling handoff** is the most consistently cited communication failure.
- Productivity data exists but is **not actionable in native form** — it must be exported and manually reprocessed in Excel.
- **Clinician retention is materially affected by scheduling quality.** Overload, unpredictable additions, excessive reassignment travel, and repeated calls to the branch are burnout contributors.
- **Patients evaluate the agency almost entirely through scheduling reliability** — punctuality, caregiver consistency, and proactive communication of change.

## 1. Why Capacity and Scheduling Must Be Separated

| Dimension | Capacity Function | Scheduling Function |
|---|---|---|
| Question answered | How much can this branch absorb, and where? | Who performs which visit, when, in what order? |
| Time horizon | Forward-looking — weeks to months | Immediate — current week, day, next hour |
| Primary owner | Branch leadership; clinical management | Scheduler; branch coordinator |
| Core inputs | Clinician roster, discipline mix, SOC eligibility, territory coverage, caseload census, productivity targets | Confirmed orders, visit frequency, clinician daily availability, geography, patient preference |
| Core output | A stated ability to accept referrals — the open-slot count | A confirmed visit assignment on a specific clinician's day |
| Failure signature | Stagnant growth; declined/missed referrals; unused clinician time | Missed visits; late arrivals; idle hours; excess travel; patient dissatisfaction |
| Current artifact | Manual scheduling grid (spreadsheet) | Manual scheduling grid (spreadsheet) + scheduling console |

**The final row is the crux.** Both functions run through the same spreadsheet, so capacity planning collapses
into day-to-day scheduling reaction and the branch has no forward view of its ability to grow.

**Consequence of conflation:** the urgent displaces the important ("who can take this visit tomorrow" is asked
dozens of times a day; "what can this branch absorb in three weeks" is never asked). And it becomes impossible
to tell whether a failure is a *capacity* failure (insufficient SOC clinicians → hire/redistribute) or a
*scheduling* failure (available capacity that wasn't located → visibility tooling). The branch can't
distinguish them, so it can't correctly remediate either.

## 2. Capacity Functions

### 2.1 Start-of-Care Capacity — The Binding Constraint
- SOC clinicians are those qualified and available to admit new patients — the critical determinant of growth.
- SOC capability is **distinct from general visit capacity**: a clinician may have room for routine visits and still be unable to accept an admission.
- **The Overload Cycle:** clinicians perpetually full with routine visits → no bandwidth for SOC admissions → no new patients → no growth → no added capacity → still overloaded. Repeats indefinitely. The loss is "unused capacity that halts branch growth" — capacity that exists in principle but can't be reached in practice. A single clinician's inability to admit can cascade into delays across broader schedules.
- **Undefined:** SOC eligibility criteria; the exchange rate between SOC and routine capacity; reserve-capacity thresholds against expected referral volume.

### 2.2 Caseload Balance and Clinician Loading
- Both directions of imbalance carry cost: overloading restricts admissions and drives burnout; underutilization is direct revenue loss.
- Monitoring is intended to be real-time but is in practice **retrospective and manual** (daily productivity reports each branch runs).
- **Point-maximizing optimization can inadvertently overload clinicians** — the target is productivity, not sustainability.
- **Undefined:** productivity expectation standards (market/discipline variation); a visit-type weight table; how caseload weight accounts for acuity/duration/travel; NVA (non-visit activity) policies.

### 2.3 Capacity Visibility and Measurement
- Branches struggle to know where clinicians are and what their capacity is at any moment.
- Capacity is expressed as **open slots** on a grid (SOC slots + routine slots). Once filled, the branch has no further capacity absent cancellations.
- **Undefined:** what a slot *is* (visit? time block? point allocation? admission?); whether slots are discipline-/territory-specific or fungible; the calculation that converts roster + targets into a slot count. Capacity is visible only as a present-tense count; **there is no forward projection.**

### 2.4 Capacity Planning Horizon
- Short-term reaction supplants long-term strategic growth. No forecasting mechanism exists; capacity is assessed reactively against present demand.
- **Aspiration:** predictive analytics in productivity reporting; capacity gaps identified days in advance; dynamic demand forecasting.
- **Undefined:** the planning horizon (week/month/quarter); what a forecast consumes (referral-source trend, seasonality, episode length, discharge rate).

### 2.5 Capacity and Financial Performance
- Branch financial health is tied directly to capacity-management accuracy. Both overstaffing and underutilization are named harms.
- **Undefined:** the cost of a missed admission, an idle clinician hour, or an unbackfilled cancellation. The capacity↔revenue relationship is asserted but not modeled.

## 3. Scheduling Functions

### 3.1 The Weekly Schedule Build
- Schedulers finalize the week early, assigning visits from existing caseloads and grid slots; the plan is a baseline expected to be modified.
- **Failure:** any new order requires manual reconstruction, not incremental addition; the build reserves no capacity for known-coming disruption.
- **Undefined:** the build sequence and decision logic; the day it occurs and horizon covered.

### 3.2 The Scheduling Grid (the single most-referenced artifact)
- A manually maintained spreadsheet listing open slots, updated by clinician availability. Contents: clinician names, open slots, SOC capacity, routine open-slot counts, current assignments.
- Efficient branches update it dynamically through the day; inefficient branches update weekly or by hand.
- **Failures:** manual updates are slow and error-prone (double-booking, delayed slot calc); not synchronized in real time (clinicians can't self-serve); no standardization → no cross-branch view.
- **Undefined:** exact column/row structure; write access and concurrent-edit handling; its relationship to the scheduling console (duplicate? supplement? contradict?).

### 3.3 Real-Time Monitoring and the Scheduling Console
- Tracks clinician assignments and **points** in real time; points adjust dynamically as needs evolve.
- **The point system is undefined — the single most significant gap**, because points are the unit in which both capacity and scheduling decisions are denominated.

### 3.4 Disruption — Last-Minute Orders
- Routine and expected. Scheduler options: redistribute across the team, ask a clinician to absorb more, call clinicians to negotiate, or request help. Resolution depends on scheduler judgment and clinician goodwill, not defined process.
- **Undefined:** the decision tree (order of options, constraints checked, escalation path); acceptable clinician notice period.

### 3.5 Disruption — Cancellations and Fallback
- Cancellations create slots that must be backfilled to avoid idle time. Efficient branches reassign in minutes; inefficient ones take hours (clinicians call in to hunt for fallback visits).
- **Failures:** wasted clinician time, long travel on distant fallback visits; absence of fallback mechanisms is a named burnout contributor.
- **Undefined:** cancellation frequency/timing/reason codes; fallback acceptability rules (proximity, discipline match, continuity); whether a clinician may decline a fallback.

### 3.6 Mid-Week Adjustment and Patient Condition Change
- Deterioration requires urgent unplanned visits; schedulers redistribute dynamically.
- **Undefined:** prioritization rules for whose visit is displaced; clinical urgency tiers and who assigns them.

### 3.7 Geography and Travel
- Reducing redundant/long-distance same-day travel is a named clinician-wellness factor; rural/remote patients face access gaps.
- **Undefined:** how territory is defined/assigned; whether travel time counts toward productivity; distance/drive-time thresholds.

### 3.8 Communication as a Scheduling Function
- The **intake↔scheduling handoff is the most-cited communication breakdown.** Late/absent updates on orders, SOC visits, and cancellations directly slow scheduling and idle clinicians.
- **Undefined:** handoff content/format/channel; expected turnaround between intake receipt and scheduler notification.

## 4. Connection Points Between Capacity and Scheduling

Where a capacity decision constrains a scheduling action, or a scheduling action changes the capacity picture —
the points where the manual system loses information and automation yields the most gain.

| # | Connection Point | Direction & Nature |
|---|---|---|
| CP-1 | Open-slot count → visit assignment | Capacity constrains scheduling. The grid's slot count is the authority; a stale/miscalculated count corrupts every downstream assignment. |
| CP-2 | Visit assignment → remaining capacity | Scheduling consumes capacity. Each assignment should decrement slots in real time; currently a manual, inconsistent recalculation. |
| CP-3 | SOC capacity → admission acceptance | **Capacity gates growth. The highest-value connection point in the system.** |
| CP-4 | Cancellation → recovered capacity | Scheduling restores capacity. Speed of recognition decides whether the slot is reused or lost — where fallback operates. |
| CP-5 | Point totals → caseload balance | Scheduling reports into capacity. Points are the shared currency of both domains — **and are undefined.** |
| CP-6 | Productivity reporting → capacity assessment | Scheduling data informs capacity judgment but needs manual Excel processing to become usable. |
| CP-7 | Territory coverage → assignment feasibility | Capacity is geographically bounded; open points in the wrong territory aren't usable capacity for a given patient. |
| CP-8 | Intake order flow → capacity signal | External demand meets internal capacity — the most-cited communication failure. |
| CP-9 | Clinician sustainability → sustained capacity | Scheduling quality preserves or destroys capacity; burnout → turnover → capacity loss, a slow invisible loop. |
| CP-10 | Patient continuity preference → assignment freedom | Continuity is a patient priority that reduces substitution options during disruption. |

**CP-3 governs whether the branch grows. CP-4 governs whether the branch wastes what it already has. CP-5
underlies both and is undefined.**

## 5. Stakeholder Perspectives (condensed)

- **Branch Executive Director (growth & finance):** growth is gated by SOC availability; the overload cycle halts growth; both overstaffing and underutilization hurt margin; wants central/automated scheduling with forecasting, unified cross-branch protocols, and real-time intake↔exec communication.
- **Tenured RN (workload & sustainability):** perpetual full caseloads leave no bandwidth for admissions; point-maximizing overloads clinicians and risks care quality; burnout (no fallback, long travel, repeated branch calls) drives turnover; wants balanced caseloads, branch-level fallback, and real-time visibility.
- **Senior Scheduler (execution):** lives in productivity reports + availability grids; real-time capacity swings with cancellations/last-minute orders; manual grids are slow and error-prone; branch disparity is stark; wants real-time capacity tracking, automated grid updates, centralized tools, and instant intake→scheduling flow.
- **Patient Panel (experience & trust):** punctuality, caregiver continuity, and proactive communication of change are the determinants of trust; cancellations without notice and lost continuity erode it; rural patients face access gaps. **Closing statement:** *"Schedule your clinicians around us — our care needs, our urgency, and our preference for consistency — not just around branch metrics and tools."*

## 6. Current Tooling Landscape
- **HCHB:** productivity tracking; data must be exported to Excel and manually interpreted; reports applied non-uniformly across branches.
- **Excel / manual processing:** raw data lacks actionable insight until refined; also hosts the scheduling grids; value depends on individual scheduler/manager skill (training crucial).
- **Scheduling console:** real-time tracking of assignments and points against targets.
- **Stated limitations:** reports need refinement; no standardized real-time tool; over-reliance on manual, inconsistent practice; real-time updates and comprehensive reporting don't currently exist.

## 7. Recommendations Surfaced (as stated, unprioritized)
- **Standardization:** automated platforms integrated with real-time capacity tracking; unified cross-branch protocols; a universal capacity-updating pattern; consistent training; dynamic schedule updates.
- **Automation / real-time:** real-time platforms reducing manual load; automated grid updates; auto-adjust for workload and referrals; automated fallback triggers; real-time capacity dashboards.
- **Predictive:** analytics detecting future capacity gaps; proactive capacity/need prediction; gaps identified days ahead; dynamic demand forecasting.
- **Communication:** bridge operational↔clinical; streamline intake↔exec; standardized intake→scheduling→clinician protocols; automated patient/clinician change notifications; scheduling-update alerts.
- **Workforce/training:** analytics training; branch accountability for equitable case distribution; predictive workload tools supporting retention.

## 8. Consolidated Failure Catalog (by domain)

- **Capacity:** SOC scarcity blocks admissions; overload cycle locks volume; underutilization = paid-for-no-revenue; overstaffing = expense without volume; no centralized capacity view; slow error-prone slot calc; grid cadence varies; no forward projection; short-term reaction displaces strategy.
- **Scheduling:** weekly rebuild on disruption; double-booking risk; grid not real-time; last-minute orders with minimal notice; hours-long fallback in low performers; geographically poor fallback assignments; clinicians repeatedly call the branch; intake fails to relay changes; urgent changes displace visits without rules; productivity data needs manual reprocessing; wide branch variance with no closing mechanism.
- **Workforce:** burnout from overload + no fallback; point-maximizing overloads; inequitable case distribution; tool value depends on individual skill.
- **Patient:** cancellation without notice; lost caregiver continuity; missed routine visits harming chronic care; rural access gaps; reduced time per patient under overload.

## 9. Open Questions & Discovery Requirements (ordered by dependency)

**9.1 Foundational — blocks all downstream definition**
- **The point system** — what a point represents; values by visit type & discipline; daily/weekly targets by clinician type; who sets them; how points relate to time; how travel is treated. *Shared currency of capacity and scheduling; referenced everywhere, defined nowhere.*
- **The scheduling grid, reconstructed field by field** — columns, rows, update triggers, ownership, access, embedded calculations. *Becomes the initial data model.*
- **The definition of an open slot** — visit / time block / point allocation / admission; discipline- and territory-specificity; the slot-count formula.

**9.2 Capacity mechanics** — SOC eligibility criteria; SOC↔routine exchange rate; balanced-caseload target ranges & hard limits by discipline; how acuity/duration factor into caseload weight; planning horizon and forecast inputs; reserve-capacity policy.

**9.3 Scheduling mechanics** — weekly build sequence; last-minute-order decision tree; fallback rules (proximity, discipline match, continuity, decline rights); urgency tiering; cancellation data (frequency/timing/reasons); clinician notice-period standards.

**9.4 Constraints & rules** — territory definition/assignment/boundaries; discipline & licensure constraints; visit-type taxonomy (SOC, recert, ROC, routine, discharge) and attached rules; patient-preference capture and binding strength; whether travel counts toward productivity.

**9.5 Interfaces & data flow** — intake→scheduling handoff (fields/channel/format/turnaround); order lifecycle upstream of scheduling; console display/actions vs. grid contents; roles & permissions for schedule changes.

**9.6 Economics** — cost of a missed admission; of an idle clinician hour; of an unbackfilled cancellation; of turnover attributable to scheduling quality. *Not required to design the platform, but required to prioritize what it builds first.*
