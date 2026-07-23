# Capacity Tool — Mockup Data Spec (read from source)

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
