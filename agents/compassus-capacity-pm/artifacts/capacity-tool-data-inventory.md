# Capacity Tool — Data Inventory (Phase A)

> **Purpose.** Enumerate *every bit of data* a home health capacity tool would need to exist, so the team can
> go find the content and war-list its source. This is the demand/supply data dictionary behind the
> "Capacity Management Scoping" next step in the discovery ([`../knowledge/discovery-session.md`](../knowledge/discovery-session.md), Next Step #4).
>
> **Status.** Grounded in the Compassus discovery docs + standard HCHB / Workday data models + the tool's
> stated purpose. The `invisiblegears.com` mockup could not be loaded from the build environment (network
> policy blocked the host), so field names below are the *functional* data elements the tool implies —
> **to be reconciled against the actual mockup screen-by-screen.** Anything the mockup shows that isn't here
> gets added; anything here the mockup doesn't need gets flagged.
>
> **Source column is a hypothesis, not a finding.** The operator + team will confirm/replace during source
> war-listing. `Cadence` = how fresh the data must be. `Grain` = the level each row represents.

## How to read this

The tool is fundamentally a **matching engine**: it holds **supply** (clinician capacity), **demand**
(patients + referrals), the **currency** that both are denominated in (the point system), the **constraints**
(geography, licensure, compliance, preferences), and the **derived outputs** (open slots, gaps, forecast).
The inventory is organized along exactly those lines. Domains A–D are the master/dynamic feeds; E–H are the
constraint/reference layers; I is the net-new static data to be gathered; J is what the tool *computes* rather
than ingests.

Candidate sources abbreviated: **HCHB** (Homecare Homebase), **WD** (Workday), **CM** (Commure – intake/referral),
**NM** (NestMed – documentation), **PU** (Pulse – utilization), **CIR** (Circadia – patient calling),
**CODE** (external ICD-10 coding vendor), **STATIC** (new config/preference store to be built), **DERIVED**
(computed by the tool).

---

## A. Clinician / Workforce Master (the supply side — mostly static)

Grain: one row per clinician. This is the roster the whole capacity calculation stands on.

| # | Data element | Grain / detail | Candidate source | Cadence |
|---|---|---|---|---|
| A1 | Clinician ID | Canonical employee identifier (join key across HCHB↔WD) | WD / HCHB | Static |
| A2 | Name / display name | — | WD | Static |
| A3 | Discipline | RN, LPN/LVN, PT, PTA, OT, COTA, SLP, MSW, HHA/aide | HCHB / WD | Static |
| A4 | Licenses & certifications | License type, number, **state**, expiration date | WD | Slow-changing |
| A5 | Specialty competencies | Wound care, IV/infusion, lymphedema, cath, ventilator, wound-vac, etc. | STATIC / HCHB | Slow-changing |
| A6 | **SOC-eligibility flag** | Whether this clinician can perform a Start of Care (the binding-constraint dimension, CP-3) | STATIC / HCHB | Slow-changing |
| A7 | Employment type | Full-time / part-time / PRN / contract / agency | WD | Slow-changing |
| A8 | FTE value | 1.0, 0.5, etc. | WD | Slow-changing |
| A9 | **Pay model** | Per-visit / salaried / hybrid (drives scheduling incentives & the earnings story) | WD | Slow-changing |
| A10 | Productivity target | Points/week (and/or visits/week) expected — benchmark heard: **30 pts/week min** | STATIC / HCHB | Slow-changing |
| A11 | Max caseload / capacity ceiling | Hard limit on concurrent patients or daily visits | STATIC | Slow-changing |
| A12 | Home base / branch | Branch of assignment | HCHB / WD | Slow-changing |
| A13 | Assigned territory / zones | Zip codes or zones the clinician covers | HCHB / STATIC | Slow-changing |
| A14 | Standard availability | Working days & hours; standard days off | WD / STATIC | Slow-changing |
| A15 | Hire date / tenure | Drives change-management segmentation (tenured = hardest to change) | WD | Static |
| A16 | Ramp / orientation status | New hire not yet at full productivity | WD / HCHB | Dynamic |
| A17 | Languages spoken | For patient matching | STATIC / WD | Static |
| A18 | Home/base location | Start point for drive-time calc (address or geocode) | WD / STATIC | Slow-changing |
| A19 | Employment status | Active / LOA / terminated (with effective dates) | WD | Dynamic |

## B. Clinician Availability & Load (the supply side — dynamic)

Grain: one row per clinician per day/week. This converts the roster into *actual reachable capacity*.

| # | Data element | Grain / detail | Candidate source | Cadence |
|---|---|---|---|---|
| B1 | Approved PTO | Dates off (the Workday↔HCHB integration is **currently OFF** — flagged in discovery) | WD | Daily |
| B2 | Requested / pending PTO | Not yet approved | WD | Daily |
| B3 | Other unavailability | Training, meetings, jury duty, FMLA blocks | WD / HCHB | Daily |
| B4 | On-call / after-hours assignment | Who is on-call and the recovery burden it creates | HCHB / STATIC | Weekly |
| B5 | Current caseload count | Active patients presently assigned | HCHB | Real-time-ish |
| B6 | Points plotted this week | Scheduled points vs. target (utilization signal) | HCHB console | Daily |
| B7 | Points completed | Actual delivered vs. plotted | HCHB | Daily |
| B8 | Visits scheduled / completed | Count + type, per day | HCHB | Daily |
| B9 | Utilization % | Completed ÷ available capacity | DERIVED (from B6/B7) | Daily |
| B10 | Overtime hours | OT incurred / trending | WD / HCHB | Weekly |
| B11 | Sick / call-out events | Unplanned unavailability | WD / HCHB | Real-time |
| B12 | Current-day accepted visits | Once accepted, back office **cannot pull** — hard scheduling constraint | HCHB | Real-time |

## C. Patient / Census (the demand side — current book of business)

Grain: one row per active patient (often per patient × discipline). What the branch is already carrying.

| # | Data element | Grain / detail | Candidate source | Cadence |
|---|---|---|---|---|
| C1 | Patient ID | Join key (operational only — minimize PHI; see guardrail note) | HCHB | Real-time |
| C2 | Branch / territory / zip | Where the patient is served | HCHB | Static per episode |
| C3 | Geocode / service location | For drive-time & zone assignment | HCHB / DERIVED | Static per episode |
| C4 | Disciplines on the plan of care | RN/PT/OT/etc. ordered for this patient | HCHB | Per episode |
| C5 | Ordered visit frequency | Per discipline (e.g., 2w9 = 2×/wk for a week then 9 total) | HCHB | Per episode |
| C6 | Episode / period day | Position within the 30-day PDGM period / 60-day cert | HCHB | Daily |
| C7 | Cert period start / end | Drives recert timing | HCHB | Per episode |
| C8 | **Recert due date** | Upcoming demand spike | HCHB | Per episode |
| C9 | Scheduled discharge date | Capacity that will free up | HCHB | Dynamic |
| C10 | Payer | Medicare / MA / commercial / Medicaid / private | HCHB | Per episode |
| C11 | Acuity / complexity | Visit weight beyond raw count (undefined today) | PU / HCHB | Per episode |
| C12 | Plan-of-care status | Draft / pending DCS / locked / on hold | HCHB | Real-time |
| C13 | Assigned primary clinician(s) | For continuity (CP-10) | HCHB | Dynamic |
| C14 | Upcoming scheduled visits | Forward visit slate, per discipline | HCHB | Daily |
| C15 | Compliance visits due | 30-day reassessment, 14-day HHA supervisory, discharge/recert visits | HCHB | Daily |
| C16 | Patient preferences | Preferred visit time window, preferred caregiver, access constraints | STATIC / CIR | Per episode |

## D. Referral / Intake Pipeline (the demand side — incoming, the growth lever)

Grain: one row per referral. This is the inflow that SOC capacity either absorbs or turns away (CP-3, CP-8).

| # | Data element | Grain / detail | Candidate source | Cadence |
|---|---|---|---|---|
| D1 | Referral ID | — | CM / HCHB | Real-time |
| D2 | Referral source | Hospital / SNF / physician / ACO / other (and the specific partner) | CM | Real-time |
| D3 | Referral received date/time | Starts the **TIC clock** (from referral date) | CM / HCHB | Real-time |
| D4 | Patient location / zip | To test against territory capacity | CM | Real-time |
| D5 | Disciplines ordered | What skills the referral will demand | CM | Real-time |
| D6 | Payer + auth requirement | Medicare (auto-auth) vs. non-Medicare (auth needed) | CM / HCHB | Real-time |
| D7 | Expected SOC date | When the demand actually lands | CM / HCHB | Real-time |
| D8 | Facility expected discharge date | When patient becomes available | CM | Real-time |
| D9 | Referral status | Pending / accepted / declined / pending-auth | CM / HCHB | Real-time |
| D10 | Acceptance decision + reason | Especially **decline reasons** (capacity vs. clinical vs. geography) | CM / HCHB | Real-time |
| D11 | Face-to-face / order documentation status | Missing F2F → coding discrepancy → POC hold (blocks scheduling) | NM / CODE | Dynamic |

## E. Visit / Scheduling Operations (the execution record)

Grain: one row per visit / task. Feeds the point/utilization math and surfaces the friction the tool must ease.

| # | Data element | Grain / detail | Candidate source | Cadence |
|---|---|---|---|---|
| E1 | Visit ID | — | HCHB | Real-time |
| E2 | Visit type | SOC, routine, recert, ROC, reassessment, discharge, HHA supervisory | HCHB | Real-time |
| E3 | Assigned clinician | — | HCHB | Real-time |
| E4 | Scheduled date + time window | — | HCHB | Real-time |
| E5 | Visit status | Plotted / accepted / completed / missed / declined / reassigned / rescheduled | HCHB | Real-time |
| E6 | Missed-visit reason + MD-notified timestamp | 48-hour MD notification (Medicare) | HCHB | Real-time |
| E7 | Coordination notes | Clinician→scheduler change requests | HCHB | Real-time |
| E8 | **Auth-off notifications** | The 50–60/day, mostly non-actionable queue | HCHB | Real-time |
| E9 | Point value assigned to the visit | Depends on the (undefined) point system | HCHB | Real-time |
| E10 | Actual visit duration / travel | If captured — needed to weight true load | HCHB / NM | Daily |

## F. Point System (the shared currency — OPEN QUESTION #1)

The single most important thing to define; both capacity and scheduling are denominated in it (CP-5). Today it
is referenced everywhere and defined nowhere. **This block is a definition to be authored, not a feed to pull.**

| # | Data element | Grain / detail | Candidate source | Cadence |
|---|---|---|---|---|
| F1 | Point value by visit type × discipline | The core lookup table (e.g., SOC RN = X pts) | STATIC (to define) | Config |
| F2 | Daily / weekly point targets by clinician type | The productivity standard | STATIC (to define) | Config |
| F3 | Travel treatment | Whether/how drive time earns or offsets points | STATIC (to define) | Config |
| F4 | Non-visit-activity (NVA) treatment | Documentation, admin, supervisory time | STATIC (to define) | Config |
| F5 | Acuity/duration weighting | How a "hard" visit counts vs. a routine one | STATIC (to define) | Config |
| F6 | Market / discipline variation | Whether targets differ by region/discipline | STATIC (to define) | Config |

## G. Geography & Territory (constraint layer — partly to be built)

| # | Data element | Grain / detail | Candidate source | Cadence |
|---|---|---|---|---|
| G1 | Territory / zone definitions | The list of zones and their boundaries | STATIC | Slow-changing |
| G2 | Zip → zone mapping | Assigns patients/referrals to a zone | STATIC | Slow-changing |
| G3 | Branch service-area boundaries | What each branch will/won't accept | STATIC / HCHB | Slow-changing |
| G4 | Drive-time / distance matrix | Zone-to-zone or point-to-point travel cost | DERIVED (mapping API) | Computed |
| G5 | Clinician↔zone coverage | Which clinicians serve which zones (links A13) | STATIC / HCHB | Slow-changing |

## H. Authorization & Payer Rules (constraint layer)

| # | Data element | Grain / detail | Candidate source | Cadence |
|---|---|---|---|---|
| H1 | Payer master | List of payers + Medicare/non-Medicare flag | HCHB | Slow-changing |
| H2 | Auth requirement by payer | Whether/what auth is needed before scheduling | HCHB / payer | Slow-changing |
| H3 | Authorized visit counts | Visits granted per auth | HCHB | Dynamic |
| H4 | Auth expiration / window | When re-auth is required | HCHB | Dynamic |
| H5 | Compliance-window rules | 48h missed-visit MD notice, 30-day reassess, 14-day HHA supervisory, TIC, buddy codes by state, CoP physical-calendar | STATIC (rules) | Config |

## I. Static / Configuration / Preferences (NET-NEW — the "employee preferences, etc." to gather)

This is the layer the operator explicitly called out as "static information we'll need to figure out." Most of
it does not exist in any system today and must be gathered.

| # | Data element | Grain / detail | Candidate source | Cadence |
|---|---|---|---|---|
| I1 | Clinician zone preferences | Preferred / acceptable / refused zones | STATIC | Gathered |
| I2 | Willingness to cross territory | The exact lever that broke Alabama Smart Scheduling | STATIC | Gathered |
| I3 | Willingness to take SOC / extra visits | Especially on pay-per-visit (the earnings story) | STATIC | Gathered |
| I4 | Max visits/day & preferred load | Sustainable daily ceiling per clinician | STATIC | Gathered |
| I5 | Preferred days off / schedule shape | Beyond formal PTO | STATIC | Gathered |
| I6 | Continuity assignments | Standing patient↔clinician pairings to preserve | STATIC | Gathered |
| I7 | Branch capacity parameters | Target ~40–50 patients per RN+LPN team pair; reserve-capacity policy; caseload limits by discipline | STATIC | Config |
| I8 | Business rules | SN-first-if-ordered on SOC; urgency tiers; fallback acceptability (proximity/discipline/continuity); decline rights | STATIC | Config |
| I9 | Slot definition | What counts as an "open slot" (visit? block? point? admission?) — open question | STATIC (to define) | Config |
| I10 | Patient preferences store | Preferred windows, caregiver continuity, communication channel | STATIC / CIR | Gathered |

## J. Derived / Computed Outputs (what the tool produces, not ingests)

These are the answers the tool exists to give — built from A–I. Listed so the team knows which numbers are
*calculated* (and therefore depend on defining the point system and slot first).

| # | Output | Built from | Notes |
|---|---|---|---|
| J1 | Available productive visit-hours / points by discipline × zone | A + B + F + G | The real capacity number (not headcount) |
| J2 | Open SOC slots & open routine slots | J1 + I9 + A6 | The growth-gating count (CP-3) |
| J3 | Capacity-to-census coverage ratio | J1 + C | Over/under-staffed by zone & discipline |
| J4 | Demand forecast 30/60/90-day | C + D + recert/discharge timing | Demand as a *shape over time*, front-loaded |
| J5 | Capacity-vs-demand gap map | J1 + J4 | Heat map with dollar sizing |
| J6 | LUPA / visit-count risk watch | C + E | Periods trending below thresholds |
| J7 | Utilization & workload balance | B + F | Variance across clinicians (burnout signal) |
| J8 | Referral-acceptance capacity signal | J2 + D | Can we say yes to this referral? |
| J9 | Projected admissions capacity | J2 + D7/D8 | Forward SOC absorption |

---

## Known gaps, dependencies & sequencing

1. **Define the point system (F) and the slot (I9) first.** Almost every computed output (J) is denominated in
   them. This is open question #1 — nothing downstream is trustworthy until it's pinned.
2. **The Workday↔HCHB PTO integration is OFF (B1).** Availability data is manually entered today; the tool needs
   this feed activated or it inherits stale availability.
3. **Employee-preference data (I) largely does not exist.** It's the operator's stated "static information to
   figure out" — plan a gathering mechanism (survey / onboarding capture / manager entry).
4. **Territory & drive-time (G) is partly unbuilt.** Zone definitions and a drive-time matrix must be created;
   they don't fall out of HCHB.
5. **Acuity weighting (C11) is undefined.** Raw visit counts overstate/understate real load without it.
6. **PHI minimization.** The capacity tool runs on aggregates and operational signals. Patient-level joins (C1)
   should carry the minimum-necessary identifier; no diagnoses, addresses, or names beyond what capacity math
   requires. Confirm the BAA-covered surface before any patient-level data lands (see the intake-brief posture).

## Next step — source war-listing template

For the working session, take each row above and fill:

| Data element (#) | Confirmed source system | Report / table / screen | Owner who can pull it | Refresh mechanism | Exists today? (Y/N/partial) | Notes |
|---|---|---|---|---|---|---|

Rows that come back **N / partial** are the build backlog. Rows in domains **F, G, I** are expected to be mostly
net-new — that's where the real work is.

---

*Reconciled against the actual mockup source (read from `worker-max/invisiblegears`, branch `capacity-tool`).
The mockup is narrower than this broad vision — a workforce-productivity measurement tool. The precise,
source-read data model for what the mockup actually uses is in
[`capacity-tool-mockup-data-spec.md`](./capacity-tool-mockup-data-spec.md); this document remains the
full-capacity-vision inventory the tool can grow into.*
