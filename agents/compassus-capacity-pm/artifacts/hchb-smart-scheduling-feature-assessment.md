# HCHB Smart Scheduling — Feature Assessment Against the Capacity & Scheduling Initiative

> **Purpose.** Assess the logic and functionality of HCHB's **Smart Scheduling (SS)**, **Visit Dispatching
> (VD)**, and **Shift Manager / Find Shifts** — as documented in the Nov-2024 vendor guide — and determine
> **which features meet the criteria for this initiative.**
>
> **Inputs.**
> - Source mechanics: [`../knowledge/vendor/hchb-smart-scheduling-product-overview.md`](../knowledge/vendor/hchb-smart-scheduling-product-overview.md) (HCHB v8, 11/2024).
> - Criteria: the capacity-vs-scheduling framing and **CP-1…CP-10** in
>   [`../knowledge/capacity-scheduling-summary.md`](../knowledge/capacity-scheduling-summary.md); the **9 open
>   questions**; the discovery ground truth in [`../knowledge/discovery-session.md`](../knowledge/discovery-session.md);
>   the [`../sme/capacity-tactics-library.md`](../sme/capacity-tactics-library.md).
>
> **Status:** analysis, not settled decision. Verdicts are the PM agent's reasoned read for operator review.
> **Bottom line up front is §1.**

---

## 1. Bottom line up front

**This is the Alabama tool.** The product assessed here is the same HCHB Smart Scheduling that was piloted and
failed in Alabama — and the knowledge base is explicit that it failed **on change management, not technology**
([`discovery-session.md` §"Why Smart Scheduling Failed"](../knowledge/discovery-session.md)). So the question is
not "is the technology any good" (parts of it are genuinely strong) but **"which of its features satisfy *this
initiative's* criteria, and where does it structurally not fit?"**

Three findings govern everything below:

1. **SS is a scheduling-execution optimizer, and the initiative's #1 criterion is that capacity must be solved
   first.** SS answers *"who performs this already-ordered visit, when, in what order?"* It does **not** answer
   *"what can this branch absorb, and where?"* The initiative's foundational thesis — *capacity is a planning
   function that must precede scheduling* — is precisely the layer SS does not provide. **Deploying SS without a
   capacity foundation reproduces the Alabama failure mode.** This is confirmed by the knowledge base
   ([summary §Executive](../knowledge/capacity-scheduling-summary.md); [README fact #2](../knowledge/README.md)).

2. **SS is blind to the binding constraint (CP-3, SOC capacity).** By its own scope note, **"SOC, ROCs, and
   other visit types … are not updated by Smart Scheduling."** SOC can only be dispatched through VD's Assign-LP
   path — and even that is *excludable*. There is **no SOC admit-slot inventory, no "admits available this week,"
   no reserve-capacity policy.** The single highest-value connection point in the system is the one SS does not
   model.

3. **But SS+VD is a strong *execution* engine whose logic is directly reusable** for the initiative's scheduling
   half (CP-1, CP-2, CP-4, CP-7, CP-10) and whose **rejection vocabulary is a ready-made capacity-signal feed.**
   Several features clear the bar. The right posture is **harvest the scheduling logic and the data signals; do
   not treat SS as the capacity solution; and if re-piloted, fix the change-management preconditions first.**

**Verdict legend:** ✅ **Meets** (fit-for-criterion, adopt/reuse) · 🟡 **Partial** (useful but incomplete or
mis-shaped for our unit of analysis) · ❌ **Gap** (criterion not addressed) · ⚠️ **Risk** (feature actively
cuts against an initiative guardrail if used naively).

---

## 2. Scorecard — features against the two functions

The initiative's first cut is **Capacity (planning) vs. Scheduling (execution)**. Sorting SS features that way
is the fastest way to see the fit.

### 2A. Scheduling-execution features — mostly ✅ / 🟡

| SS/VD feature | Initiative criterion it speaks to | Verdict | Note |
|---|---|---|---|
| Overnight optimizer assigns eligible routine visits by cost | §3 Weekly Build; CP-1 (slot→assignment) | ✅ | Automates the manual weekly build for routine volume; removes double-booking risk on eligible visits. |
| **Dispatching / lock window** (3/5/7-day, churn control) | Clinician sustainability CP-9; §3.1 build stability | ✅ | Directly targets the "continuous reconstruction / churn" pain; protects near-term stability. Strong. |
| **Visit Dispatching — real-time, same-day, decline/reassign auto-reroute** | §3.4 last-minute orders; §3.5 cancellations/fallback; CP-4 | ✅ | This is the automated **fallback/last-minute** engine the initiative asks for (tactics **L3-4, L3-5**). Reroutes declines to next-best worker (never the decliner). High-value. |
| **Route optimization** (OSM, miles-vs-minutes, per-day ordering) | §3.7 geography/travel; tactic L2/L3 travel | ✅ | Addresses redundant/long-distance travel — a named burnout factor and (pay-per-visit) an earnings story for clinician buy-in. |
| **Over-mileage / over-minute caps for 0%-continuity workers** | §3.7; patient continuity CP-10 | ✅ | Encodes "don't send a discontinuous clinician too far" — matches the initiative's fallback-acceptability concern. |
| **Continuity model** (discontinuity penalty, min-continuity floor, `% Continuous` filter, weekend/holiday & SOC/ROC exceptions) | CP-10 continuity; patient north-star | ✅ | Continuity is a first-class, tunable, *measurable* cost term with a console filter to hunt low-continuity visits. Best-in-class part of the product. |
| **Caregiver Optimization / Job Code Priority Hierarchy** (LPN<RN, PTA<PT) | Tactics **L1-1, L3-1** (RN→LPN / PT→PTA offload) | ✅ | Exactly the "assistant tier absorbs routine so skilled stay on assessment" lever the SME lenses converged on. Ships with an Analytics dashboard. |
| **Case Management & Team Member Model** (soft penalty / hard restrict) | CP-10; continuity-vs-substitution tension | 🟡 | Good for encoding "prefer the care team." But **hard-restrict lowers ROI** (vendor-stated) and mirrors the Alabama over-constraint anti-pattern if leadership locks it down. Use soft, not hard. |
| **Patient Schedule Preference** (days/time, BID/TID, soft warning) | Patient continuity/reliability CP-10; north-star | 🟡 | Captures patient preference and feeds the optimizer — but **7 am–7 pm, whole-hours** only, and only a soft warning in console. Partial capture of "bind strength" (open question 9.4). |
| **Rapid Reschedule compatibility; Manual Holidays; Prevent-from-SS** | §3.6 mid-week adjust; manual override | 🟡 | Escape hatches exist and are permissioned — good. But over-use of Prevent/exclusions is *how Alabama neutered the engine*. Govern usage. |

### 2B. Capacity-planning features — mostly ❌

| Capacity criterion (initiative) | Does SS provide it? | Verdict |
|---|---|---|
| **CP-3 — SOC-capable capacity as the binding constraint; admit-slot inventory; reserve policy** | SOC/ROC **out of SS scope**; VD-Assign-LP is assignment, not an admit-slot *pool*; excludable. No reserve-capacity model. | ❌ **Core gap.** |
| **Open-slot definition & forward slot count** (open question 9.1) | No slot object, no forward projection. Capacity surfaces only as a *rejection* after the fact. | ❌ |
| **Capacity forecasting / planning horizon** (§2.4; open q 9.2) | None. SS is a nightly optimizer over an 8–14-day window; no demand forecast, seasonality, or gap-days-ahead. | ❌ |
| **Acuity/travel/documentation-weighted caseload load unit** (tactic L3-2; open q 9.1 point system) | SS's unit is **Expected Productivity Points** (payroll construct) + **hours** for time; **not** acuity/doc-weighted. Travel/slack are hours, not load-weighted points. | ❌ / ⚠️ — see §4. |
| **Capacity↔revenue model** (§2.5; open q 9.6) | Cost-minimization only; no missed-admission / idle-hour / turnover cost model. | ❌ |
| **Territory/zone capacity design** (tactics L2-1…L2-3) | Branch/team/location/facility **matching** constraints exist, but no *territory-health* or zone-coverage-floor signal. | 🟡 matching yes, design no. |
| **Census-to-staffing solve, binding-constraint capacity, ramp/attrition** (L1-4…L1-7) | Absent — SS optimizes a given roster; it does not size one. | ❌ |

---

## 3. Feature-by-feature against the 10 Connection Points

The connection points are the initiative's map of *where the manual system loses information*. SS's fit,
point by point:

| CP | The connection point | SS/VD coverage | Verdict |
|---|---|---|---|
| **CP-1** | Open-slot count → visit assignment | SS assigns from availability/constraints, but there is **no explicit slot count** — it reasons in hours/points/penalties, not a published slot. Assignment: yes. Slot authority: no. | 🟡 |
| **CP-2** | Visit assignment → remaining capacity | Each assignment consumes availability in-engine, but that decrement is **not surfaced as a live remaining-capacity number** to humans; you learn it only via next run / rejection. | 🟡 |
| **CP-3** | **SOC capacity → admission acceptance** *(highest value)* | **Not covered.** SOC out of SS scope; VD assignment ≠ admit-slot inventory; excludable. | ❌ **The decisive gap.** |
| **CP-4** | Cancellation → recovered capacity (fallback) | **VD decline/reassign auto-reroute is exactly this** — freed visit → next-best worker, fast. Same-day supported. | ✅ **Strong fit.** |
| **CP-5** | Point totals → caseload balance *(shared currency, undefined)* | SS **uses HCHB Expected Points**, so a point definition *exists* — but it's a productivity/payroll unit, **not** the acuity/travel/doc-weighted currency the initiative needs. Adopting SS's point as-is **hard-codes the wrong definition.** | ⚠️ |
| **CP-6** | Productivity reporting → capacity assessment | **Job History + rejection reasons are a machine-readable capacity-signal feed** ("Workers at max hours," "Optimizer/…capacity issues," "Blocked by hard constraints"). Better than raw Excel export — but still snapshot, Eastern-time, per-run. | 🟡 → ✅ as a *signal source*. |
| **CP-7** | Territory coverage → assignment feasibility | Branch/team/**Location**/facility matching + shared/super-branch enforce geographic eligibility. Design/health signals absent. | 🟡 |
| **CP-8** | Intake order flow → capacity signal *(most-cited failure)* | **Not addressed.** SS reacts to auth state (rejections) but doesn't bridge the intake→scheduling handoff. Commure/Circadia are the relevant systems, not SS. | ❌ |
| **CP-9** | Clinician sustainability → sustained capacity | Lock window (anti-churn), route optimization, over-mileage caps, Next-Day Cutoff, Find-Shifts autonomy all **serve sustainability** — *if tuned for it, not against it.* | ✅ (with ⚠️ tuning) |
| **CP-10** | Patient continuity preference → assignment freedom | Continuity model + Patient Schedule Preference + Case-Management model = **the richest continuity tooling of any system in the landscape.** | ✅ |

**Read:** SS is **excellent on the scheduling-side connection points (CP-4, CP-9, CP-10)**, **partial on the
plumbing (CP-1, CP-2, CP-6, CP-7)**, and **absent on the two that gate growth and cause the most pain (CP-3,
CP-8)** — plus it **mis-defines CP-5**, the shared currency.

---

## 4. The point-system trap (CP-5 / open question #1) — read this before adopting anything

The initiative's **#1 foundational open question** is *"what is a point?"* — the undefined shared currency of
both capacity and scheduling. **SS appears to answer it** (it schedules to *Expected Productivity Points*). It
does not. SS's point is a **productivity/payroll construct**: a target visit-load per Medicare week. The
initiative's required unit is **weighted true load = visit + drive + documentation + coordination + acuity**
(tactic **L3-2**, "capacity ≠ visit count," a *high-confidence, five-lens-convergent* finding).

If we adopt HCHB's point definition because SS already uses it, we **encode the exact failure the tactics
library warns against**: point-maximizing overloads the efficient clinician and *looks balanced doing it*
(⚠️ tactic L3-2, and summary §2.2 "point-maximizing optimization can inadvertently overload clinicians").
**Recommendation: define our weighted load unit independently, then map HCHB points to it — never inherit it.**

---

## 5. What genuinely meets the criteria (adopt / harvest)

Features that clear the initiative's bar and should be **kept, reused, or emulated** in the target platform:

1. **VD decline/reassign auto-reroute (CP-4, L3-4/L3-5)** — the automated fallback engine. Highest reuse value.
2. **Lock/Dispatching window + Next-Day Cutoff (CP-9)** — churn control that directly serves clinician
   sustainability and the "personal assistant, not control mechanism" framing.
3. **Continuity model + `% Continuous` measurement (CP-10)** — first-class, tunable, *observable* continuity.
   Our platform should expose an equivalent continuity score.
4. **Caregiver Optimization / Job-Code Hierarchy (L1-1, L3-1)** — the RN→LPN / PT→PTA offload lever, already
   with an Analytics dashboard to baseline current optimization.
5. **Route optimization + travel caps (CP-9, geography)** — the clinician earnings/wellness story for buy-in.
6. **Rejection-reason feed as a capacity signal (CP-6)** — "Workers at max hours," "Optimizer → capacity
   issues," "Blocked by hard constraints," "PRE-BATCH NO AUTHORIZATION FOUND," "RECERT PERMISSION" are a
   structured, near-real-time diagnostic stream. **This is the single most useful *capacity* by-product of an
   otherwise scheduling tool** — pipe it into the capacity dashboard.
7. **Worker Details / availability data model** — skills, qualifiers, locations, teams, facilities, availability
   — a ready schema for the eligibility half of any matcher we build.

## 6. What does not meet the criteria (do not rely on SS for these)

1. **Capacity planning & forecasting (❌ §2, §4 criteria)** — SS has none. Must be built (the initiative's whole
   premise).
2. **SOC admit-slot inventory & reserve policy (CP-3 ❌)** — the binding constraint is invisible to SS.
3. **Intake→scheduling handoff (CP-8 ❌)** — out of scope; belongs to Commure/intake initiative.
4. **A correct weighted-load point unit (CP-5 ⚠️)** — SS's point is the *wrong* unit; adopting it is a trap.
5. **Cross-branch, forward, discipline-by-zone capacity view** — SS is per-run and per-branch; no forward
   cross-branch capacity picture.

## 7. Risks & guardrails if SS/VD is re-piloted

- ⚠️ **Change-management preconditions first.** Alabama failed because leadership let clinicians reject
  optimization and locked the engine to zip codes. Re-piloting **without** enforced scope + the "personal
  assistant" framing + (pay-per-visit) earnings story repeats the failure. Cleanest pilot = **new-integration /
  pay-per-visit / newer-clinician branch** (discovery + tactics converge here).
- ⚠️ **Don't over-constrain.** Hard "Restrict to Team," heavy Prevent/Exclude usage, and Location-locking
  reproduce Alabama. Prefer **soft penalties**; govern who holds `PREVENT VISITS…` and exclusion Locations.
- ⚠️ **Don't inherit the point definition (see §4).**
- ⚠️ **Optimization overload.** Percent-Reserve is **ignored inside VD** (fills to full capacity in the lock
  window) and Productivity-Points-Model schedules to exact expected points — both can overload the reliable
  clinician if targets aren't sustainability-bounded (tactic L3-2, CP-9).
- ⚠️ **Vendor gating.** Much high-value logic is "enter a ticket" — not branch-self-service. Factor vendor
  dependency and configuration lead time into any plan.
- ⚠️ **Compliance interplay.** SS **excludes SOC/ROC and PRN by default** and treats Recert as opt-in; the
  compliance-window pre-consumption of capacity (recert-60 / PT-reassess-30 / HHA-supervisory-14 / 48h ROC/MD —
  tactic **L3-6**) is **not** modeled by SS and must live in our capacity layer.

---

## 8. Recommendation

**Two-track.** (1) **Build the capacity layer the initiative was founded to build** — SOC admit-slot inventory
(CP-3), weighted-load unit (CP-5, defined *independently* of HCHB points), forward slot count & forecast, and
the intake→capacity bridge (CP-8). SS does **not** meet these and never will. (2) **Harvest SS/VD's
scheduling-execution logic and data signals** — the fallback engine (CP-4), continuity model (CP-10), caregiver
optimization (L1-1/L3-1), lock-window sustainability controls (CP-9), and above all the **rejection-reason feed
as a live capacity signal (CP-6)**. Whether that harvest means *re-enabling SS/VD behind a capacity foundation*
or *rebuilding equivalents in the target platform* is the next decision — and it depends on the pilot-branch
choice and the change-management preconditions in §7, not on the technology, which is adequate.

**In one line:** *Smart Scheduling is a capable scheduling-execution engine wearing a name that overpromises
capacity. It clears the bar on the scheduling connection points, is blind on the capacity ones, and mis-defines
the shared currency. Adopt its execution logic and its signals; build the capacity foundation it presupposes;
and if you re-pilot it, fix the people problem first.*

---

## 9. Traceability

| This assessment's claim | Grounded in |
|---|---|
| SS scope excludes SOC/ROC; buddy-code, recert, exclusions, VD toggles, point/OT rules | Vendor mechanics §2, §6, §7, §10 → [product-overview](../knowledge/vendor/hchb-smart-scheduling-product-overview.md) |
| Capacity must precede scheduling; Alabama failed on change management | [discovery-session §3, §"Why Smart Scheduling Failed", §4](../knowledge/discovery-session.md); [README facts #1,2,6](../knowledge/README.md) |
| CP-1…CP-10 definitions; capacity-vs-scheduling split; point undefined | [capacity-scheduling-summary §1, §4, §9](../knowledge/capacity-scheduling-summary.md) |
| Weighted load ≠ visit count; RN→LPN offload; fallback tree; compliance pre-consume; over-load risk | tactics [L1-1, L3-1, L3-2, L3-4, L3-5, L3-6](../sme/capacity-tactics-library.md) |
