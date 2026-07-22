# Initiative Playbook — Compassus Capacity & Scheduling

> The operating plan the Home Health Expert Project Manager runs. Where [`AGENT.md`](./AGENT.md)
> defines *who the agent is and how it thinks*, this playbook is *what it executes* — the
> phase-by-phase program from planning through scaled rollout to standing governance.

This is a living document. The agent updates it as the initiative moves and as reality corrects
the plan.

---

## The shape of the program

A five-phase, gated program. Nothing advances past a gate until its exit criteria are evidenced.
The unit of proof is deliberately small: **one branch, the binding discipline, a pre-registered
metric** — then scale only what clears the gate.

```
A. Discover ──▶ B. Design ──▶ C. Pilot ──▶ D. Scale ──▶ E. Sustain
   baseline       plan          prove         replicate     govern
   (gate A/B)     (gate B/C)     (gate C/D)     (gate D/E)     (steady state)
```

---

## Phase A — Discover / Baseline

**Goal:** an honest, quantified starting picture of capacity vs. demand across programs,
disciplines, and zones. No optimization yet — just make the current system legible.

**Key activities**
- Pull 13-week trailing data from HCHB / MatrixCare: scheduled vs. completed visits, points,
  mileage, missed-visit reasons, OASIS/recert cycles, on-call load.
- Pull referral/intake logs (volume by source, acceptance, auth status, SOC dates) and HR/
  staffing rosters (FTEs, disciplines, credentials/zones, PTO, per-visit vs. salaried).
- Build the **discipline-by-zone capacity baseline** in productive visit-hours — not headcount.
- Compute baseline KPIs: utilization %, missed/declined-visit rate, LUPA rate,
  referral-to-SOC time (median + tail), overtime %, PRN/agency spend, points attainment.
- Structured interviews with schedulers and branch directors to surface tribal workarounds and
  the *invisible* capacity leaks (drive time, doc burden, rework, orientation drag).
- Identify the top 3 capacity leak points per branch and the likely **binding discipline**.

**Exit criteria (Gate A→B)**
- Signed baseline pack with documented data provenance and agreed metric definitions.
- A shortlist of 2–3 lighthouse-branch candidates, ranked by opportunity size × readiness.

**Watch for:** dirty data presented as truth; branches whose "capacity" number is really an
unmeasured assumption; metric definitions that differ silently branch to branch.

---

## Phase B — Design / Plan

**Goal:** convert baseline gaps into a concrete operating model and a *testable* pilot.

**Key activities**
- Build the **capacity model** (FTEs × productivity × availability, net of PTO/travel/on-call
  recovery) and the **demand forecast** (30/60/90-day visit demand from referral trends, census,
  admissions, recert/OASIS cycles, seasonality) — demand modeled as a *shape over time*.
- Design **staffing-to-census ratios** and trigger bands by discipline and acuity, including the
  per-visit / salaried mix and the PRN/agency call thresholds.
- Draft **scheduling & routing policies**: zone assignment, visit clustering, PT/OT
  front-loading, recert/OASIS window protection, continuity-vs-routing weighting, on-call
  coverage.
- Write the **pilot charter**: scope, hypotheses, the pre-registered primary metric, success
  thresholds, and — committed *in advance* — the stop/scale (kill) criteria.
- Stand up the **RACI** and **risk register**; validate every data feed end-to-end.
- Model expected **financial + workforce impact**: points-attainment lift, PRN/agency offset, OT
  reduction, margin per episode, and the retention risk the plan must not create.

**Exit criteria (Gate B→C)**
- Steering-committee-approved charter and pilot design.
- Lighthouse branch selected; success thresholds and kill criteria pre-committed.
- Data feeds validated; scorecard wired to real sources.

**Watch for:** a plan that only works if utilization runs at 100%; policies that push complexity
onto an already-drowning scheduler; targets that are margin wins borrowed from next quarter's
turnover.

---

## Phase C — Pilot (Lighthouse Branch)

**Goal:** prove the model moves the metrics in one branch **without harming quality or
clinicians**. This is a reversible experiment, not a launch.

**Key activities**
- Run the **daily capacity huddle** (open visits, at-risk LUPAs, no-fills, over/under-loaded
  clinicians, on-call gaps) and the **weekly pilot standup** (scorecard vs. baseline, blockers,
  decisions).
- Track the live **pilot scorecard** against baseline and against the pre-committed thresholds.
- Run **LUPA-risk and missed-visit monitoring** in near-real-time — flag the cliff, force the
  clinical-vs-financial call into the open, never pad visits silently.
- **Change management** with schedulers: new SOPs, coaching, escalation paths; track adoption
  and friction, not just compliance.
- Maintain the **decision log** (decisions, rationale, reversals). Run a **mid-pilot
  course-correction** review.

**Exit criteria (Gate C→D)**
- Pre-set KPI thresholds met and **sustained ≥ 4–6 weeks**.
- No quality/CoP degradation (SOC timeliness, OASIS windows, acute-care utilization).
- Clinician-experience signal neutral-to-positive.
- A documented, **repeatable** playbook — the mechanism, not a heroic manager.

**Watch for:** the pilot that succeeds because of one exceptional person; local metric wins
masking a system metric loss; scheduler burnout hiding under a green scorecard.

---

## Phase D — Scale / Rollout

**Goal:** replicate the *proven* model across programs in controlled waves — no faster than
readiness and support can sustain.

**Key activities**
- Sequence branches into **rollout waves** by readiness, region, and EMR instance.
- **Localize** the playbook per branch (zones, referral mix, pay model, tacit local judgment)
  — central standards with local judgment, not a uniform override.
- Run a **readiness checklist** and a **go/no-go** per wave.
- Train schedulers and branch directors; stand up the escalation/support model before go-live.
- Track **adoption and metric conformance** across the fleet; maintain a cross-branch
  **leaderboard** to spread what's working and surface laggards early.

**Exit criteria (Gate D→E)**
- Target % of branches live and holding KPIs within tolerance.
- Central dashboard operational; escalation/support model working.
- No systemic quality or workforce red flags across the fleet.

**Watch for:** scaling speed outrunning support capacity; over-centralizing and amputating the
branch judgment the system still needs; adoption theater (SOPs signed, behavior unchanged).

---

## Phase E — Sustain / Govern

**Goal:** make the new capacity discipline the permanent way of working — off PMO life support.

**Key activities**
- Transition to a **monthly ops-governance** rhythm; hand ownership to standing branch/regional
  accountability.
- Run **drift detection**: metric backslide, staffing shifts, seasonality; trigger
  re-forecasting on referral-mix or census changes.
- Own the **runbook** and the **quarterly model refresh** (re-baseline capacity/demand, refresh
  targets).
- Feed a continuous-improvement backlog.

**Exit criteria (steady state)**
- Initiative absorbed into standing operations; owner accountability assigned.
- Drift-detection and refresh cadence running without the PMO holding it up.

**Watch for:** silent backslide once attention moves on; a model that ages out of date against a
changed referral mix; governance that becomes a status meeting instead of a control system.

---

## Cadence summary

| Cadence | Rhythm | Phases | Agent produces |
|---|---|---|---|
| Capacity huddle | Daily, 15 min, branch | Pilot, Scale | Agenda + action capture |
| Initiative standup | Weekly, cross-functional | All active | Scorecard review + decision log |
| Change/adoption review | Bi-weekly | Pilot, Scale | Adoption + friction report |
| Steering committee | Monthly, sponsors + exec | All | Executive readout |
| Phase-gate review | At each gate / wave | Boundaries | Exit-criteria evidence + go/no-go |
| Model refresh | Quarterly | Sustain | Re-baselined capacity/demand model |

## Decision-gate discipline

Every gate is a *stop-and-decide*, not a formality. The agent brings: the exit-criteria evidence,
the risks, a clear recommendation, and the one question — *what does advancing optimize, and what
does it silently trade against?* A gate that can't be evidenced is a gate that hasn't been passed,
and the agent says so plainly.
