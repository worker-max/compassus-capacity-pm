# Capacity Tool — Mockup Data Spec (read from source)

> ### ⟳ As-built update (re-reviewed against `invisiblegears` `main` @ `6dba163`)
> The tool has been built out well beyond the version first reviewed below. It is now **9 tabs** with a real
> capacity-matching brain, and the **point system is resolved** (the visit-weight table). The authoritative
> field-level model is now the operator's **`ClinicianCapacityTool_DataIndex.xlsx`**. The original 4-tab
> description that follows is kept as history; **the current review is the "As-built review" section at the
> bottom of this file.**

> **What this is.** The exact data model of the operator's mockup, read directly from its source at
> `worker-max/invisiblegears`, branch `capacity-tool`, file `public/capacity-tool/index.html` (a self-contained
> HTML/JS artifact). This supersedes the inferred [`capacity-tool-data-index.md`](./capacity-tool-data-index.md)
> for *this* tool: that data index was the broad capacity-forecasting vision; **the mockup is a narrower, sharper
> thing** — see the reconciliation at the end.
>
> **What the tool is.** A **Clinician Capacity Management Tool** the wrapper describes as a *"re-creation of
> CenterWell's Worker Productivity Tool."* Four tabs: **Worker Productivity** (roster grid) · **Productivity
> Trends** (line chart) · **Visit Capacity Program** (compensation reference) · **Implications** (stakeholder
> scorecards). It imports a weekly roster (CSV/JSON), computes productivity vs. target, and reports it.
>
> **The big finding.** This tool *is* an operational instantiation of "the point system" — the shared currency
> that the Compassus discovery flagged as **open question #1, undefined, gating everything**
> ([`../knowledge/capacity-scheduling-summary.md`](../knowledge/capacity-scheduling-summary.md) §9.1). The
> mockup doesn't resolve that question; it *assumes it solved* by taking daily points as an input. That gap is
> the most important row in this document (see Gap G1).

---

## Entity 1 — Worker Weekly Productivity Record

The core entity. **One row per clinician per week.** These are the fields the import schema actually accepts,
plus the fields the tool computes from them.

### 1a. Raw / ingested fields (the import contract — CSV & JSON §8.1)

| # | Field | Type / values | Notes | Candidate source |
|---|---|---|---|---|
| W1 | `lastName` | string | Grid freezes on "Last, First" | HCHB / Workday |
| W2 | `firstName` | string | — | HCHB / Workday |
| W3 | `discipline` | enum: **LPN, PTA, PT, RN, OT, COTA** (extensible) | Drives filters + pills | HCHB / Workday |
| W4 | `fteStatus` | enum: **FT, PT, Contractor** | Filter + PT/contract expected-points logic | Workday |
| W5 | `payMethod` | enum: **PPV, FEE_BASED, CONTRACT, SALARY, SALARY_PLUS** (labels: PPV / Fee Based / Contract / Salary / Salary Plus) | Contract ⇒ no target | Workday |
| W6 | `weeklyExpectedPoints` | number (e.g. **30** FT, **24** PT, **0** contract) | The productivity target | Config/policy → see Gap G5 |
| W7 | `pointsByDay.sun … .sat` | 7 numbers (points earned per day) | The heart of the data — daily productivity | HCHB visit/productivity report → see Gap G1 |
| W8 | `comments` | free text (e.g. "pto all week", "off mon", "prn", "baylor", "pto thu–fri", "part b", "rotates fri/mon off") | Explains variance | HCHB scheduler notes / manual |
| W9 | *week context* ("Week Of") | date (snapshot period, e.g. Jul 21 2024) | Which week this row is | Pay-period calendar → Gap G7 |

### 1b. Derived fields (computed by the tool — do NOT source; but the *rules* must be agreed)

| # | Field | Formula in mockup | Notes |
|---|---|---|---|
| D1 | `dailyAvgExpected` | `weeklyExpectedPoints / 5` | Assumes a 5-day expectation |
| D2 | `totalPointsEarned` | `sum(pointsByDay)` | — |
| D3 | `variance` | `earned − expected` (null if contract) | Shown as (x) negative / x positive |
| D4 | `productivityPct` | `round(earned / expected × 100)` (0 if contract) | — |
| D5 | `contract` (flag) | `payMethod==CONTRACT` **or** `expected==0` | Excludes from targets/KPIs |
| D6 | `statusTier` | **Critical <25% · In Progress 25–89% · On Target 90–110% · Exceeded >110% · Not Set** | Handoff §3.3 thresholds — exact |

## Entity 2 — Reference / Configuration data

Small controlled lists and rules the tool needs to exist. Mostly config, not feeds — but each must be **agreed
and owned.**

| # | Reference set | Values in mockup | Candidate source |
|---|---|---|---|
| R1 | Disciplines | LPN, PTA, PT, RN, OT, COTA | Config (align to HCHB) |
| R2 | Pay methods | PPV, Fee Based, Contract, Salary, Salary Plus | Config (align to Workday/comp) |
| R3 | FTE statuses | FT, PT, Contractor | Config |
| R4 | Productivity status thresholds | 25% / 90% / 110% breakpoints (§3.3) | Policy (to ratify) |
| R5 | Week / pay-period list | Jul 21, Jul 14, Jul 07, Jun 30 2024 … | Pay-period calendar → Gap G7 |
| R6 | Region → Area hierarchy | North→{Metro North, Lakeshore}; South→{Gulf Coast, Piedmont}; West→{High Desert, Bay} | Org hierarchy → Gap G2 |
| R7 | Trend pay periods | Feb, Mar, Apr, May, Jun, Jul, Aug | Pay-period calendar |
| R8 | "Top 10 branches" cohort | benchmark comparison set | Branch ranking → Gap G3 |

## Entity 3 — Visit Capacity Program (VCP) compensation reference

The comp-policy layer the tool documents (Tab 3). Reference data today; a live tool would also need the
**actuals** (Gap G6).

**NVA Code Table**

| Field | Values in mockup |
|---|---|
| NVA Code | **5001** — Visit Capacity Adjustment; **5003** — Visit Capacity Adjustment |
| Payment Method | 5001 → Fee-Based Pay, Pay Per Visit · 5003 → Salary Plus |
| Weight | 0.25 unit |
| Who Enters | Branch Admin |

**Tier Threshold Table**

| Tier | Eligible Visits | Additional Comp |
|---|---|---|
| 1 | Up to 6 units above productivity target | 0.25 unit per applicable visit |
| 2 | 6+ units above productivity target | 0.50 unit per applicable visit |
| 3 (SOC) | All SOCs above productivity target | 0.50 unit per applicable visit |

**Business Rules to Enforce** (as written)
- NVA code entered by **branch admin or branch leader ONLY** — never the clinician.
- Branch **payroll designee reviews HCHB payroll reports** each pay period.
- **BD and/or Clinical Manager must approve each NVA entry in HCHB before Monday payroll close.**
- Codes **5001 / 5003** may be reported multiple times per pay period.
- **Eligibility:** clinician must already be **at or above weekly productivity target** before any tier applies.

## Entity 4 — Aggregations / KPIs (derived; recomputed under the active filter)

The Tab 1 KPI strip. All computed from Entity 1.

| KPI | Definition in mockup |
|---|---|
| Clinicians | count of workers (with "N on a target") |
| Avg Productivity | mean `productivityPct` across non-contract workers |
| At / Above 90% | count ≥90% (+ % of roster) |
| Critical <25% | count <25% |
| **Open Capacity** | `Σ expected − Σ earned` = **unearned points this week** → *"~points/6 visits of headroom"* |

> **Open Capacity is the whole point.** It reframes a productivity shortfall as *available capacity for new
> admissions* — the direct bridge to the growth/referral story (CP-3).

## Entity 5 — Productivity Trends series (aggregate)

Tab 2. Filters: **Region, Area, EE Type (All/FT/PT), Compare Top 10** (toggle).

| Data element | Detail | Candidate source |
|---|---|---|
| % of clinicians in **Low / Med / High** productivity group | per pay period (Feb–Aug), division-wide | Aggregation of Entity 1 across history |
| **Top 10** high-productivity series | benchmark overlay | Entity 1 filtered to Top-10 cohort (Gap G3) |
| Insights narrative | computed (division vs Top 10, headroom to close) | Derived |

## Entity 6 — Implications scorecards (derived per stakeholder)

Tab 4. One card per stakeholder group, computed live from the roster.

| Scorecard | Metric it computes |
|---|---|
| Clinician Experience | avg productivity; % at/above target |
| Scheduler / Leader | data completeness (% with visits logged this week) |
| Sales & Referral | open-capacity points → visit headroom |
| Workforce Management | % on FBP / salary (points-based) plans vs hourly |
| Culture Shift | week-over-week productivity trend |

## Import / Export contract

- **CSV columns (exact):** `lastName, firstName, discipline, fteStatus, payMethod, weeklyExpectedPoints, sun, mon, tue, wed, thu, fri, sat, comments`
- **JSON:** array of worker records per "handoff schema §8.1" (external spec, not in the repo — **get a copy**).
- **Export CSV** additionally emits derived `totalEarned, variance, productivityPct`.

---

## The gaps — data the mockup *assumes* but a real tool must actually source

The mockup runs on sample data and seeded trends. To make it real, these must be sourced. **This is the true
"war-list" target.**

| # | Gap | Why it matters | Where it must come from |
|---|---|---|---|
| **G1** | **The point-earning rules** — how `pointsByDay` is produced from real visits (visit type × discipline × weight) | This *is* the undefined "point system" (discovery open question #1). The mockup takes points as given; reality computes them | **HCHB visit records + a points/weight config** — define first |
| **G2** | **Worker → Branch → Area → Region mapping** | Tab 2 filters by region/area, but the worker record has no such field | Org hierarchy (HCHB/Workday) |
| **G3** | **"Top 10 branches" designation** | Benchmark cohort for trends | Branch productivity ranking (derived + policy) |
| **G4** | **Weekly history (≥13 weeks)** | Drawer trend + Tab 2 are seeded/faked; real trend needs stored weekly snapshots per worker | Historical HCHB productivity extracts, warehoused |
| **G5** | **`weeklyExpectedPoints` derivation** | Where 30 (FT) / 24 (PT) / 0 (contract) come from | Productivity-target policy by FTE × discipline |
| **G6** | **NVA / tier actuals** | Tab 3 is reference-only; a live tool needs actual NVA entries + tier attainment per worker per period | HCHB payroll reports |
| **G7** | **Pay-period / "Week Of" calendar** | Defines the snapshot boundaries and Monday payroll close | Payroll calendar (config) |
| **G8** | **The handoff spec (§3.3, §8.1)** | The authoritative schema + threshold source the mockup cites | External doc — obtain and file in `knowledge/` |

## Reconciliation vs. the broad data index

The earlier [`capacity-tool-data-index.md`](./capacity-tool-data-index.md) indexed the *full
capacity-forecasting/matching vision* (supply + demand + referrals + geography + auth + forecast). **The mockup
is deliberately narrower — a workforce-productivity measurement tool.** Mapping:

- **In the mockup:** the clinician-master subset (A1–A9), the point system (domain F → now Entity 1/VCP), and a
  slice of the derived outputs (J1/J7 utilization, J2/J8 open capacity as "headroom").
- **Not in the mockup (yet):** patient census (C), referral pipeline (D), visit-level scheduling ops (E),
  geography/drive-time (G), auth/payer (H), and the demand-side forecast (J4/J5). These are the broader
  capacity vision the tool could grow into — but they are **out of scope for this artifact.**

**Net:** the mockup is v1 = *"can we see, per clinician, productivity vs. target and the unused capacity it
implies?"* — the measurement foundation the rest of the capacity program can be built on. Which is exactly the
discovery's sequencing: **define and instrument the point system first.**

## Next step — source war-listing (for the team session)

Take Entities 1–6 and the Gaps and fill:

| Element (#) | Confirmed source | HCHB/Workday report or screen | Owner who pulls it | Refresh | Exists today? (Y/N/partial) | Notes |
|---|---|---|---|---|---|---|

Start with **G1 (point rules) and G5 (targets)** — nothing the tool shows is trustworthy until those are
defined, and both are policy decisions before they are data feeds. Then **W7 pointsByDay → the actual HCHB
report** the business rules already name ("HCHB payroll reports"), which is the single richest source.

---

# As-built review (`invisiblegears` `main` @ `6dba163`, re-read from source)

The tool has grown from a 4-tab productivity tracker into a **capacity-guidance cockpit**. What's now built:

## The nine tabs
1. **Worker Productivity** — the roster grid (now with a segmented completed/in-progress/scheduled/missed bar and a per-day expected marker).
2. **Roster** — editable clinician master: preferred days, territory zips (add/remove), PTO, restrictions — scheduler-maintained.
3. **Per Diem** — the per-diem pool: available vs. scheduled visits, remaining capacity, and a **disengagement flag** (≥7 days since last confirmed visit).
4. **Worker Trends** — per-clinician archetype cards: 13-wk spark, front-load score vs. the 42% gold standard, missed-visit %, risk tier, and a narrative assessment.
5. **Productivity Trends** — division vs. Top-10 by region/area (as before).
6. **Capacity Guidance — Live Cockpit** — the new brain (see below).
7. **Capacity Map** — Charleston tri-county zip tiles colored by RN/PT remaining capacity; marks zips at capacity.
8. **Visit Capacity Program** — the NVA/tier/comp reference (as before).
9. **Implications** — the stakeholder scorecards.

## The capacity brain (Tab 6 + `capacityDirectives()`)
Real supply→demand matching on live-shaped data:
- **Supply math:** `remainingByDay = maxDaily − assigned points` (FT 8 / PT 6 / PD 4), netted for PTO; `weekOpen` = sum of positive remainders Wed→Sat; assessing capacity computed per discipline.
- **Demand:** `REFERRALS` (discipline, zip, SOC/Eval, assigned/unassigned) and `DISCHARGES` (discipline, zip, D/C date) — capacity *arriving* and *reopening*.
- **Geography:** real zip lat/lon + **haversine**; `nearestScheduled` finds a clinician already working near a referral.
- **Assessing→assistant offload:** RN→LPN, PT→PTA, OT→COTA — frees assessing capacity for SOCs.
- **Seven directive types**, ranked: referral→best-fit clinician (capacity + proximity, per-diem favored); offload routine to assistant; discharge→backfill nearest referral; re-engage disengaging per-diem; reassign behind-pace backlog before it goes missed; extend a per-diem RN into a maxed SOC zip; park overflow with a front-loader who has headroom.

This is the "AI optimization engine" track the discovery called for — a real prototype, not a chart.

## Findings from reading the logic (what to fix as it goes real)

1. **Restrictions are displayed but not enforced in matching.** Per-diem restrictions ("No SOC visits", "No wound care", "No high-acuity", "Recerts only", "Weekends only") are free-text labels. `capacityDirectives()` ranks per-diems by capacity + proximity and *favors* them (`dist − 3`) but never checks the restriction — so it can recommend an **SOC to "No SOC visits" Arjun Patel**, or wound care to "No wound care" Lily Nguyen. **The matcher needs to hard-filter on restrictions/competencies.** (Highest-priority correctness gap.)
2. **Capacity = visit-point headroom only — travel and NVA aren't debited.** `remainingByDay` counts assigned visit points against a daily ceiling but never subtracts drive time, documentation, or admin. A clinician shown "+2.0 open" may be full once the day's route is counted. Miles exist per visit but don't reduce capacity. → "open capacity" runs optimistic.
3. **Proximity is straight-line haversine, not drive-time.** The data index has `routeMiles` from routing; the matcher uses centroid haversine. Fine for a demo; rural loops (e.g., 29471 "rural loop") will mislead until drive-time replaces it.
4. **SOC eligibility ≈ discipline.** `renderCapSoc` and the matcher treat any RN/PT as SOC-capable; a per-diem RN flagged "No SOC visits" still counts toward RN SOC coverage. SOC-eligibility should be its own flag (the discovery distinguishes it).
5. **No readiness/auth gate before matching.** Referrals are binary `unassigned | assigned` — the matcher acts as if every referral is schedulable. In reality it may be stuck in DCS/auth/POC/F2F. This is ecosystem gap **1A**, and the directive engine makes it *more* important: it will confidently route a referral that can't actually start.
6. **Everything is demo-seeded** (`SAMPLE`, `REFERRALS`, `DISCHARGES`, `PD_META`, simulated `visitStatus`). Expected — but the brain's value hinges on the live referral-readiness and per-diem-availability feeds, which are the manual/HCHB rows in the data index.

## Where this leaves the ecosystem gaps
The build-out **closes the demand-arrival + matching layer** (referrals, discharges, proximity, per-diem engagement) that the ecosystem map listed as thin. The **structural gaps still stand**: 1A readiness gauntlet (now *more* pressing), 1B economics/LUPA, 1C quality/compliance, 2D forward forecast, 2E patient acuity (only a per-diem free-text restriction today), 2F aide (HHA)/MSW, 2G back-office capacity, 2H retention signal, 3I the clinician accept/decline loop, 3K data-trust. See [`capacity-ecosystem-map.md`](./capacity-ecosystem-map.md).
