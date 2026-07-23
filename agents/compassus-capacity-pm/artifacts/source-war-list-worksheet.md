# Source War-List Worksheet — Capacity Tool

> **What this is.** Every data element the capacity tool needs, as a row to be *sourced*. The mockup spec
> ([`capacity-tool-mockup-data-spec.md`](./capacity-tool-mockup-data-spec.md)) says *what* data the tool uses;
> this worksheet is where the team records *where each piece actually comes from*. Fill the blank columns in a
> working session. Rows that come back **N / Partial** are the build backlog.
>
> **Two copies, same rows.** [`source-war-list-worksheet.csv`](./source-war-list-worksheet.csv) is the fill-in
> instrument — open it in Excel / Google Sheets. This Markdown mirror is for reading on GitHub. Keep the CSV as
> the source of truth once the team starts editing.

## Columns to fill

| Column | Who fills it | Meaning |
|---|---|---|
| Candidate Source | *pre-filled* | A hypothesis to **confirm or replace** — not a finding |
| Confirmed Source System | team | HCHB / Workday / Commure / policy / warehouse / etc. |
| Report / Table / Screen | team | The exact report name, table, or screen the data lives in |
| Owner | team | The person who can actually pull it |
| Refresh Cadence | team | How fresh it must be (real-time / daily / weekly / config) |
| Exists Today? | team | **Y** (pullable now) / **Partial** / **N** (must be built) |

**Priority key:** **P0** = define before anything else (policy decision, gates the tool) · **P1** = core feed for v1 ·
**P2** = needed for full function (trends/segmentation) · **P3** = reference/comp layer · **—/N/A** = derived, no source.

---

## Section 1 — Worker record (raw / imported)

The core entity: one row per clinician per week. This is the import contract the tool already accepts.

| Ref | Data element | What it is | Candidate source | Priority | Notes |
|---|---|---|---|---|---|
| W1 | Worker last name | per clinician | HCHB / Workday | P1 | Join key; grid shows "Last, First" |
| W2 | Worker first name | per clinician | HCHB / Workday | P1 | |
| W3 | Discipline | LPN/PTA/PT/RN/OT/COTA | HCHB / Workday | P1 | Align enum to HCHB |
| W4 | FTE status | FT/PT/Contractor | Workday | P1 | Drives expected-points logic |
| W5 | Payment method | PPV/Fee Based/Contract/Salary/Salary Plus | Workday | P1 | Contract ⇒ no target |
| W6 | Weekly expected points (target) | per clinician per week | Policy/config (see G5) | **P0** | Where does 30 / 24 / 0 come from? |
| W7 | Points earned by day (Sun–Sat) | per clinician per day | HCHB payroll/productivity report (see G1) | P1 | THE richest feed; rules in G1 |
| W8 | Comments | per clinician per week | HCHB notes / manual | P2 | Explains variance (PTO/PRN/baylor/part b) |
| W9 | "Week Of" period | snapshot boundary | Pay-period calendar (see G7) | P1 | |

## Section 2 — Reference / configuration

Controlled lists and rules the tool needs. Mostly config — but each must be agreed and owned.

| Ref | Data element | What it is | Candidate source | Priority | Notes |
|---|---|---|---|---|---|
| R1 | Disciplines list | controlled list | Config (align HCHB) | P2 | |
| R2 | Pay methods list | controlled list | Config (align Workday/comp) | P2 | |
| R3 | FTE statuses list | controlled list | Config | P3 | |
| R4 | Productivity status thresholds | 25% / 90% / 110% | Policy — ratify (§3.3) | **P0** | Ratify with ops leadership |
| R5 | Week / pay-period list | snapshot periods | Payroll calendar | P2 | |
| R6 | Region → Area hierarchy | org geography | Org hierarchy (see G2) | P2 | Trends tab filters on this |
| R7 | Trend pay periods | Feb–Aug rolling | Payroll calendar | P3 | |
| R8 | Top 10 branches cohort | benchmark set | Branch ranking (see G3) | P2 | |

## Section 3 — Visit Capacity Program (comp reference)

| Ref | Data element | What it is | Candidate source | Priority | Notes |
|---|---|---|---|---|---|
| V1 | NVA code table | 5001 / 5003 Visit Capacity Adjustment | HCHB payroll + comp policy | P3 | Reference/config today |
| V2 | Tier threshold table | Tiers 1 / 2 / 3-SOC + comp | Comp policy | P3 | |
| V3 | Business rules | 5 rules (entry / approval) | Comp + ops policy | P3 | |

## Section 4 — Gaps (the real war-list targets)

Data the mockup *assumes* but a live tool must actually source. This is where the work is.

| Ref | Data element | What it is | Candidate source | Priority | Notes |
|---|---|---|---|---|---|
| **G1** | **Point-earning rules** | visit type × discipline × weight → daily points | HCHB visits + points/weight config | **P0** | The undefined "point system" — define FIRST |
| G2 | Worker→Branch→Area→Region mapping | per-clinician org placement | HCHB / Workday org hierarchy | P2 | Record has no region field today |
| G3 | Top 10 branch designation | branch flag / ranking | Derived from productivity + policy | P2 | |
| G4 | Weekly history (≥13 weeks) | per-clinician weekly snapshots | Warehoused HCHB extracts | P1 | Drawer trend + Tab 2 faked today |
| **G5** | **Weekly expected-points derivation** | target rule by FTE × discipline | Productivity-target policy | **P0** | Policy before feed |
| G6 | NVA / tier actuals | per clinician per period | HCHB payroll reports | P3 | Tab 3 reference-only now |
| G7 | Pay-period / Week-Of calendar | snapshot + Monday-close boundaries | Payroll calendar | P1 | |
| G8 | Handoff spec (§3.3 / §8.1) | authoritative schema + thresholds | External doc — obtain | P1 | Not in any repo; file in knowledge/ |

## Section 5 — Derived (computed by the tool — no source needed)

Listed so nothing is lost, but these are **outputs, not inputs** — the team does not source them. They do depend
on the rows above (noted).

`dailyAvgExpected`, `totalPointsEarned`, `variance`, `productivityPct`, `contract flag`, `status tier` (uses R4);
KPIs (`Clinicians`, `Avg Productivity`, `≥90%`, `Critical <25%`, **`Open Capacity`**); trend group %/Top-10 series
(need G3+G4); the five implications scorecards. All recompute live from the worker records.

---

## How to run the session

1. **Settle P0 first** — G1 (point-earning rules), G5 (expected-points rule), R4 (thresholds). These are
   *policy decisions before they are data feeds*; nothing the tool shows is trustworthy until they're agreed.
2. **Then chase the P1 feeds** — starting with **W7 → the actual "HCHB payroll report"** the VCP business rules
   already name. That one report likely delivers W1–W8 together.
3. **Fill Confirmed Source / Report / Owner / Refresh / Exists** for each row. Flag every **N / Partial**.
4. **Hand the N/Partial rows back to me** (or your local session) — those become the integration/build plan.
