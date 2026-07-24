# Home Health Capacity Ecosystem — Coverage Scan

> **Question answered:** now that the Clinician Capacity Management Tool is well-defined (see the data index),
> what pieces of the home health capacity ecosystem are we *not* yet considering?
>
> **Method:** diffed the tool's data index (`ClinicianCapacityTool_DataIndex.xlsx`) against the full capacity
> ecosystem implied by the Compassus discovery ([`../knowledge/`](../knowledge/)). This lists only genuine
> white space — things the current index does **not** contain — not a re-statement of what it already does well.

> **Re-reviewed against the built-out tool** (`invisiblegears` `main` @ `6dba163`, 9 tabs + capacity cockpit).
> The build now closes the demand-arrival + matching layer (referrals, discharges, proximity, per-diem
> engagement, assessing→assistant offload, a 7-type directive engine). The structural gaps below still stand,
> and 1A is now *more* pressing because the directive engine acts on referrals as if they're schedulable. One
> new **correctness** finding: the matcher ranks/​favors per-diems by capacity + proximity but **does not enforce
> their restrictions** ("No SOC", "No wound care", "No high-acuity"), so it can mis-route. Full read in the
> [as-built review](./capacity-tool-mockup-data-spec.md#as-built-review-invisiblegears-main--6dba163-re-read-from-source).

## What the tool already covers (so we don't re-litigate it)

Supply (clinician capacity net of PTO / per-diem / max-daily-points), the **point system** (visit-weight table —
the previously-open #1 gap, now closed), demand *arrivals* (referrals + pending discharges), geography &
routing (territory, route miles, tracts, capacity map), matching/AI directives (proximity, nearest scheduled
visit), outreach (Twilio channels + welcome call), trends/history (13-wk, front-load, pace, missed-visit), and
the VCP comp layer. This is a strong **supply-measurement + matching** engine.

## The capacity equation — where the gaps sit

```
DEMAND ──▶ [READINESS gauntlet] ──▶ SUPPLY ──▶ [CONSTRAINTS] ──▶ DECISION ──▶ FEEDBACK
referrals   intake/DCS/auth/POC     clinician   geo·acuity·auth   accept /     financial·
+forecast   /F2F/coding/TIC         capacity    ·licensure·qual   assign/staff quality·retention
   │            ▲ GAP (Tier 1A)        ✓ strong      ~partial          ✓ AI directives   ▲ GAP (Tier 1B/C)
   ▲ GAP (Tier 2D forecast)
```

The tool is strong in the middle (supply → match). The white space is at the **two ends**: the *readiness
gauntlet upstream of a schedulable visit*, and the *economic/quality/retention feedback* that tells you whether
a capacity decision was actually good.

---

## Tier 1 — Structural (these change the answer, not just add detail)

### 1A. The pre-scheduling readiness gauntlet — the discovery's central finding, still absent
The index treats a referral as ready-to-assign (`status: unassigned | assigned`). But the discovery's #1
conclusion was that *the inefficiency is upstream of scheduling*: a visit is typically stuck in **DCS review,
pending authorization, a plan-of-care lock, or a face-to-face / coding hold** before a scheduler can act. None
of those states are in the index, and neither is **TIC (time-to-initial-care)** — the referral→SOC clock the
whole intake funnel is measured on.
**Why it matters:** "Can we accept this referral?" is gated by these states as much as by clinician open points.
A capacity tool that can't see the gauntlet will show green capacity while admissions stall upstream — exactly
the blame-lands-on-scheduling trap.
**Attach as:** a Referral *readiness state* (DCS status, auth status, POC lock, F2F/coding hold) + a TIC clock.

### 1B. The economic layer — LUPA, margin, and agency/OT cost
The tool expresses capacity in *points and visits*, and comp in VCP units — but never in *dollars* or *episode
economics*. Missing: **LUPA risk** (periods trending below the visit threshold — a step-function the schedule
directly controls), **margin per 30-day period**, and **PRN / agency / overtime spend** as the cost of covering
a gap.
**Why it matters:** every executive capacity decision (accept? hire? use agency? push overtime?) is ultimately
economic. "Open capacity" of 40 points isn't a dollar figure, and a full schedule that's LUPA-ing is a financial
hole the productivity view can't see.
**Attach as:** a per-episode LUPA watch + a cost overlay on the open-capacity / coverage-outreach flows.

### 1C. Quality & compliance guardrails
`missedVisitPct` and `mvNotesCount` are in; the rest of the quality/compliance frame is not: **HHVBP** measures
(the cohort-relative scoring the org is paid on), **OASIS timeliness**, **recert / 30-day reassessment / 14-day
HHA-supervisory windows**, and **acute-care hospitalization**.
**Why it matters:** capacity utilization pushed without these degrades the exact outcomes reimbursement now
depends on. Compliance windows are also hard scheduling constraints, not soft goals.
**Attach as:** compliance-window flags on the visit/plan-of-care record + a quality guardrail on utilization
targets.

## Tier 2 — Important extensions

### 2D. Predictive demand forecast (the tool is present-tense)
History is captured (13-wk); *forward* demand is not. No referral-source trend, seasonality, or 30/60/90-day
admissions projection. Discharges give near-term reopen, but not a forecast.
**Why it matters:** capacity planning is a forward function; measuring last week can't tell you what to staff
for next month. This was the discovery's explicit aspiration.

### 2E. Patient acuity / complexity (demand-side weighting)
`productivityWeight` is by *visit type*, not *patient acuity*. A high-acuity wound/CHF caseload at "90%
productivity" is loaded very differently from a routine one. `restrictions` capture "no wound care" but there's
no acuity model on demand.
**Why it matters:** acuity-blind matching over-loads clinicians the point system says are fine, and misroutes
complex patients.

### 2F. Aide (HHA) and MSW capacity + supervisory linkage
The discipline enum (RN/LPN/PT/PTA/OT/COTA/SLP) omits **HHA/aides** and **MSW**. Aides are a large capacity pool
with their own scheduling and a **14-day supervisory-visit** dependency on the RN.
**Why it matters:** aide capacity and its supervisory tie-back is real capacity and real compliance load the
tool currently can't see.

### 2G. Back-office capacity — scheduler & DCS throughput
The tool manages *clinician* capacity, but the discovery named the **scheduler and DCS as the actual
bottleneck** (scheduler burnout; the DCS 4-task review chain; the 50–60/day auth-notification noise). Nothing
models back-office throughput.
**Why it matters:** you can have clinician capacity and still not convert it because the constraint is a
drowning scheduler or a DCS queue.

### 2H. Future capacity — hiring/onboarding ramp + retention risk
`tenure` is derived, but there's no **new-hire ramp curve** (reduced early productivity), no **hiring pipeline**
(reqs/offers/start dates = capacity arriving), and no **turnover-risk / burnout signal**.
**Why it matters:** discovery's feedback loop — over-utilization destroys capacity via turnover on a 3–6-month
lag. A tool that only maximizes this week's points can quietly burn down next quarter's capacity.

## Tier 3 — Surfaces & backbone

### 3I. Directive governance + the clinician accept/decline loop (the Alabama lesson)
Outreach exists (channels, message body), but the **clinician's response** — accepted / declined a coverage
offer, and *why* — isn't captured, and there's no approval/override/audit trail on AI directives.
**Why it matters:** the Alabama Smart Scheduling pilot failed on change management, not tech. Capturing accept/
decline + reason is both the buy-in mechanism and the training signal; ungoverned directives repeat that failure.

### 3J. Patient-facing and referral-source-facing surfaces
Leader/scheduler/clinician surfaces exist; the **patient scheduling portal** (visit-window visibility, reschedule
requests — the discovery's QR-code idea) and the **referral-source acceptance loop** (does Roper St. Francis
learn we can/can't take the patient?) are absent.
**Why it matters:** patients judge the agency on scheduling reliability; referral sources route to whoever says
yes fastest. Both are capacity *outputs* with no surface today.

### 3K. Integration & data-trust backbone
The index names the critical field (`visitStatus`, gated by **PointCare manual sync**) and the source systems.
Two backbone realities aren't modeled: **sync latency** (PointCare is not real-time — capacity shown may be
stale) and the **Workday↔HCHB PTO integration the discovery reported is OFF** (so PTO, a load-bearing
availability input, may be manual/stale). Plus master-data identity resolution (WD-ID ↔ HCHB-ID) at scale.
**Why it matters:** every number the tool shows inherits the freshness and identity-match of these feeds; a
capacity call made on stale sync is confidently wrong.

---

## The sibling tools are part of this ecosystem

Two related artifacts already live in `invisiblegears`: **hh-territories** ("The Tract, Not the ZIP" — territory
design) and **hh-scheduling** ("Four outcomes, one schedule"). These are not separate projects; they are the
*territory* and *scheduling-execution* faces of the same capacity ecosystem. Worth an explicit product
architecture so the capacity tool, the territory designer, and the scheduling view share one data spine rather
than three.

## Recommended next moves

1. **Decide scope deliberately.** Not everything above belongs in *this* tool — but each should be a conscious
   "in / adjacent / later," not an accidental omission. The safe default: keep the tool as the supply+match
   engine, and treat 1A (readiness), 1B (economics), and 1C (quality) as the next adjacent modules it must
   *connect to*.
2. **Prioritize 1A.** The readiness gauntlet is the discovery's core thesis and the biggest blind spot — it's
   what turns "green capacity" into real, admittable capacity.
3. **Add the two feedback overlays (1B financial, 1C quality)** before scaling — they're what tell you a capacity
   decision was actually good, and they're what executives and VBP are scored on.
4. **Capture the accept/decline loop (3I) now** — it's cheap, it's the buy-in mechanism, and it's the training
   data every later optimization needs.
