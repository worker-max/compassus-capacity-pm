# HCHB Smart Scheduling — Executive Brief & Capacity-Tool Fit

> **Two parts.** **Part 1** is a one-page executive overview of what HCHB Smart Scheduling is and whether it
> meets this initiative's bar. **Part 2** evaluates how it could support the capacity tool we've built
> (`invisiblegears` capacity cockpit) — feed its visuals, execute its directives, and validate what it surfaces.
> Grounded in the [feature assessment](./hchb-smart-scheduling-feature-assessment.md), the
> [vendor mechanics](../knowledge/vendor/hchb-smart-scheduling-product-overview.md), the
> [capacity-tool spec](./capacity-tool-mockup-data-spec.md), and the [ecosystem map](./capacity-ecosystem-map.md).

---

# Part 1 — Executive Overview (one page)

**What it is.** HCHB Smart Scheduling (SS) is the optimization module of the HCHB Intelligence Suite — an
**overnight batch** that auto-assigns clinicians to *already-ordered routine visits* to minimize cost while
managing continuity, plus **Visit Dispatching (VD)**, a real-time arm that assigns visits inside the near-term
lock window (including same-day), and **Shift Manager/Find Shifts**, a clinician self-service for extra visits.
HCHB claims SS+VD schedule **99% of Home Health / 97% of Hospice** visits. **This is the same product Compassus
piloted and abandoned in Alabama.**

**What it does well (adopt / harvest):**
- **Automated fallback & reassignment** — VD reroutes declined/cancelled visits to the next-best worker in real
  time (the initiative's CP-4). The strongest single capability.
- **Continuity as a measured, tunable cost** — a per-visit `% Continuous` score with penalties and a console
  filter (CP-10). Best-in-class in the current system landscape.
- **Caregiver Optimization** — prefers the lower-cost qualified worker (LPN over RN, PTA over PT) — the exact
  RN→assistant offload lever the SME lenses converged on.
- **Route optimization** and **churn-control lock window** — real drive-distance routing and near-term schedule
  stability that protect clinician sustainability (CP-9).
- **A machine-readable rejection vocabulary** ("Workers at max hours," "No authorization found," "Blocked by
  hard constraints") that is, in effect, a live capacity-signal and reality-check feed.

**Where it does not meet the bar (build ourselves):**
- **Blind to the binding constraint.** By its own scope, SS **does not touch SOC/ROC** — the SOC admit-slot
  capacity that gates branch growth (CP-3) is invisible to it. No slot inventory, no reserve policy, no forecast.
- **No capacity planning.** It is a present-tense optimizer over an 8–14-day window — it never answers "what can
  this branch absorb in three weeks."
- **Mis-defines the shared currency.** Its "point" is a productivity/payroll target, **not** the
  acuity+drive+documentation-weighted load unit the initiative needs. Inheriting it re-encodes the overload
  failure mode.
- **Silent on the most-cited failure** — the intake→scheduling handoff (CP-8).

**Clinician-autonomy read (the capillary test).** It preserves the *"shape my week against a weekly point
target"* freedom (Productivity Points Model) and leaves daily sequencing to the clinician (route order is
suggested, not enforced). It does **not** preserve the deeper *"I build my own caseload and day"* autonomy — the
engine assigns the visits and re-optimizes nightly, and can override a hand-arranged plan. **Whether even the
preserved slice survives is a configuration and leadership-framing choice — which is precisely what Alabama got
wrong** (leadership stripped latitude, then let clinicians reject the tool: worst of both).

**Verdict.** SS is a capable **scheduling-execution engine wearing a name that overpromises capacity.** It
clears the bar on the *execution* connection points and is blind on the *capacity* ones. **Recommended posture:
do not treat SS as the capacity solution; harvest its execution logic and its data/rejection signals; and if it
is ever re-piloted, fix the change-management preconditions first** (enforced scope, "personal assistant, not
control mechanism" framing, and — on pay-per-visit — an earnings story).

---

# Part 2 — Can Smart Scheduling support the capacity tool?

**Short answer: yes, at three specific points — but as the *execution + sensing* layer beneath our capacity
brain, never as the brain itself.** The two systems sit at different stages of the same capacity equation, which
is exactly why they compose instead of compete:

```
DEMAND ──▶ [READINESS] ──▶ SUPPLY ──▶ [CONSTRAINTS] ──▶ DECISION ──▶ EXECUTE ──▶ FEEDBACK
                            └──────── our capacity tool: SEE + DECIDE ────────┘
                                          [CONSTRAINTS]      [EXECUTE]   [FEEDBACK]
                                          └──────── HCHB Smart Scheduling / VD ───────┘
```

Our capacity tool is the **supply-measurement + matching + directive brain** — forward-looking, points/weight
based, *recommend-only* (its Tab 6 emits 7 human-approved directives). Smart Scheduling is the **execution arm
inside HCHB** plus a **constraint validator** and a **feedback sensor**. They meet in three modes.

## Mode 1 — FEED: Smart Scheduling data → the capacity tool's visuals

The tool's most important gaps are *supply-side data feeds SS/HCHB already produces.* This is where SS most
directly "supports the visuals."

| Capacity-tool element (tab / gap) | What Smart Scheduling / HCHB supplies | Strength |
|---|---|---|
| **`pointsByDay` / productivity actuals** — Tab 1, the heart of the data (Gap **G1**, **G5**) | SS schedules to **Expected Productivity Points** and the **Job History / HCHB payroll reports** carry the per-visit, per-day actuals the VCP rules already name | 🟡 supplies the *productivity* points + targets — **but not** the acuity-weighted unit the tool now uses (reconcile, don't merge) |
| **Remaining/open capacity** — Tab 6 supply math, Tab 7 map | SS computes worker availability against **Max Hours/Day, Visits/Day, Expected Points, reserve time**; the **"Workers at max hours"** rejection is a literal capacity-exhausted signal — and SS **debits drive + slack** in its hours math | ✅ closes the tool's finding #2 (points-only headroom) with a **drive-debited** capacity number |
| **Roster attributes** — Tab 2 (skills, territory, restrictions, availability) | **Worker Details Report**: skills, qualifiers, locations, teams, assigned facilities, alternate starting point, availability/unavailability | ✅ near-direct schema match for the Roster tab |
| **Proximity / drive-time** — Tab 6 finding #3, Tab 7 map | SS uses **OpenStreetMaps drive distance** and optimized daily routes | ✅ upgrades the tool's straight-line **haversine → real drive-time** |
| **Continuity** — not yet in tool (CP-10) | Per-visit **`% Continuous`** score + weekend/holiday/SOC-ROC exceptions | ✅ a signal the tool lacks today |
| **13-week history / trends** — Tab 4/5 (Gap **G4**) | Job History run over time (warehoused) | ✅ replaces the tool's seeded trend |
| **Per-diem pool** — Tab 3 | **Find Shifts** self-service engagement (who opted in to extra visits) | 🟡 partial — engagement, not full availability |

**SS does *not* feed:** demand arrivals (referrals = Commure), discharges, the forecast (Gap 2D), or patient
acuity (Gap 2E). Those come from elsewhere.

## Mode 2 — EXECUTE: the tool's directives → Smart Scheduling / VD action

The tool *decides*; SS/VD can be the hands that *do* it in HCHB. Its 7 directive types map cleanly — with one
sharp caveat.

| Capacity-tool directive (Tab 6) | Executes via | Fit |
|---|---|---|
| Offload routine to assistant (RN→LPN, PT→PTA) | SS **Caregiver Optimization / Job Code Priority Hierarchy** | ✅ direct |
| Discharge → backfill nearest referral; reassign behind-pace backlog before it goes missed | VD **decline/reassign + re-optimization** (CP-4) | ✅ direct |
| Route/proximity optimization | SS **routing** | ✅ direct |
| Referral → best-fit clinician (esp. **SOC**) | VD **Assign-LP** dispatch | ⚠️ **weakest exactly where it matters most** — SS excludes SOC/ROC; VD-Assign-LP *can* do SOC but is *excludable* and is an assignment, **not** the admit-slot inventory the tool's growth thesis (CP-3) needs |

**Execution caveats that must be governed:** SS/VD acts only on **ordered, authorized, eligible** visits;
**nightly re-optimization can override** a human's manual assignment unless it's explicitly *Prevented*; SS's
point unit **won't reconcile** with the tool's weight table; and HCHB is **batch + manual PointCare sync**, not
real-time — so execution is periodic, not streaming.

## Mode 3 — VALIDATE: Smart Scheduling constraints → reality-check what the tool surfaces

This is the most elegant fit, because SS's hard constraints are exactly the correctness gaps the ecosystem scan
flagged in the tool:

- Tool **finding #5 — no readiness/auth gate** (ecosystem gap **1A**) → SS's **"No authorization found /
  PRE-BATCH NO AUTHORIZATION FOUND"** rejections tell you *which referrals are actually schedulable.* SS enforces
  at execution the readiness gate the tool can't see.
- Tool **finding #1 — restrictions not enforced** → SS **hard constraints** (Skills, Qualifiers, License) won't
  assign an ineligible worker; **"Blocked by hard constraints"** is the reason code.
- Tool **finding #4 — SOC eligibility ≈ discipline** → SS **"RECERT PERMISSION"** / license checks are a real
  SOC/recert-eligibility gate.

In effect, SS's **rejection vocabulary is a machine-readable "which of your directives are real"** feed back into
the tool — turning green-but-fake capacity into admittable capacity.

## What SS cannot support (leave to the capacity tool / other systems)

Forecast (2D) · SOC admit-slot inventory & reserve (CP-3) · episode economics/LUPA (1B) · quality/HHVBP (1C) ·
back-office scheduler/DCS capacity (2G) · retention/burnout signal (2H) · true real-time (3K) · and the
**accept/decline governance loop** (3I) — SS has decline mechanics but not the *why + audit + buy-in* capture
that the Alabama lesson makes mandatory. **That loop is the capacity tool's job, and it's what keeps SS from
being a black box imposed on clinicians.**

## Synthesis — the architecture this implies

**Capacity tool = the brain that SEES and DECIDES** (forward capacity, open SOC slots, directives, and the
clinician accept/decline governance). **Smart Scheduling/VD = the hands that EXECUTE and the sensors that FEED
BACK** (supply actuals, drive-debited availability, continuity, routing, capacity-exhausted + auth/eligibility
rejections). The integration is a **loop**: HCHB/SS → nightly extract → tool visuals; tool directive → human
approval → optional VD execution; SS rejection → tool marks the directive real/blocked.

This is the sequencing the discovery demanded — **a capacity foundation first, then an execution engine running
*under* it, not instead of it** — and it directly answers the Alabama failure: clinician buy-in and governance
live in our brain, so SS only ever executes decisions the capacity view and the humans already sanctioned.

**One open build-vs-integrate decision:** the sibling **`hh-scheduling`** tool ("Four outcomes, one schedule")
already prototypes a scheduling-execution face. So the choice is whether the *execute* arm is **HCHB SS/VD driven
by API** or **our own execution surface** — a decision to make deliberately, on the same shared data spine the
ecosystem map recommends, not by accident.

---

## The direct answer to the question asked

**Is there any point where Smart Scheduling supports the capacity tool's visuals, or responds to what the tool
surfaces? Yes — three:**

1. **It supports the visuals** — SS/HCHB is the natural source for the tool's *supply-side* visuals it currently
   seeds/fakes: productivity actuals (G1), drive-debited remaining capacity (finding #2), the capacity map's
   real drive-time (finding #3), continuity, the roster, and 13-week history (G4).
2. **It responds to what's seen** — VD is the execution arm that can carry out the tool's directives (offload,
   backfill, reassign) — strong for routine, **weak for the SOC directives that matter most.**
3. **It validates what's seen** — SS's auth/license/max-hours rejections tell the tool *which* directives are
   actually schedulable, patching its readiness and restriction gaps.

**The boundary:** SS supports the tool as an **execution + sensing layer**; it cannot supply the forecast, the
SOC-slot inventory, the economics, or the governance — those are the capacity brain's to own.
