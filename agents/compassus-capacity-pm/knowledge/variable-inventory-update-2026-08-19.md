# Variable Inventory Update — 19 Aug 2026

> **What this is.** The record of what changed in the workbook when the two 19-Aug handoff documents
> were applied. Read it before touching the `Variable Inventory` tab again — it is the authority on
> which IDs are now taken, which are reserved, and which downstream tabs must be re-synced.
>
> **Input documents (Drive).**
> [`HANDOFF-1-variable-additions.md`](https://drive.google.com/file/d/1y0X3TLKuG4H_W6vpPxQ8opW-HZblfXfD/view) ·
> [`HANDOFF-2-target-architecture.md`](https://drive.google.com/file/d/1lFw02FQEteLoDZf_L_OIl78SbaRvqe8z/view)
>
> **Input workbook.** `8.13 Compassus Capacity & Scheduling Workbook.xlsx`, Drive
> `1tVEkPO2FJMFVyqLZP1TrzqbmjX0qEDgv`, as modified 17 Aug.
>
> **Output workbook.** `8.19 Compassus Capacity & Scheduling Workbook.xlsx` —
> [`source/8.19 Compassus Capacity & Scheduling Workbook.xlsx`](./source/8.19%20Compassus%20Capacity%20%26%20Scheduling%20Workbook.xlsx),
> CSV snapshot in [`source/workbook-2026-08-19/`](./source/workbook-2026-08-19/).

## Headline

**76 numbered variables + 3 unnumbered placeholders → 87 numbered variables.** Every one of the 87 is
now visible to the sheet's own Weight and Gating formulas, carries a rollup key, and is assigned to
one of the three target modules.

| | Before | After |
|---|---|---|
| Numbered variables | 76 | **87** |
| Unnumbered rows carrying scores | 3 | **0** |
| Variables invisible to the Scorecard | 3 | **0** |
| Variables in the Functional Scorecard | 76 | **87** |
| Variables in the concept dictionary | 76 | **87** |

## 1. The defect, fixed

Three rows Colin had inserted — **Insurance Authorization**, **Add-On Orders**, **Clinician Safety** —
carried a constraint, an MVP flag and a posture, but no `Row Type` and no `Rollup Key`. Both are
inputs the sheet's own formulas depend on, so all three were excluded from the Weight and Gating
formulas and from every category rollup. Three **Hard** variables, two of them **MVP-Yes**, were
invisible to vendor scoring.

They now carry `Row Type = Variable`, a rollup key, and the full attribute set. `Clinician Safety`
was additionally missing its Weight and Gating formulas entirely; those are now present.

## 2. IDs assigned — and the collision, resolved

`artifacts/variable-backlog.md` had flagged an unresolved **`S-43` collision** between the backlog's
own reservations and the 18-Aug payer/economics handoff. Handoff 1 settles it. No ID had been written
into the workbook, so nothing needed renumbering.

**Handoff 1's assignment is what landed. It supersedes every earlier reservation.**

| ID | Variable | Was reserved as | Resolution |
|---|---|---|---|
| `S-43` | Insurance Authorization | backlog `S-45`; also claimed as payer `SH-12` | **Authorization is a scheduling variable, not a shared-spine one.** The pending-auth allowance is an attribute of this row, not a separate variable |
| `S-44` | Add-On Orders | backlog `S-46` | — |
| `S-45` | Clinician Safety | backlog `S-47` | — |
| `S-47` | POA status and signing authority | backlog `S-43` + `S-44` (two rows) | Merged into one row. Signing authority and availability-to-sign are the same concept |
| `CO-14` | Consent state by channel | backlog `S-43` (consent half) | Consent moved to the Coordination layer — it gates a **channel**, not a visit |

## 3. What was added

### Tier A — IDs assigned to Colin's three existing rows

His constraint, MVP, posture, notes and additional context are preserved verbatim. Only the fields
the formulas need were filled in.

| ID | Variable | Layer | Block | Constraint · MVP · Posture |
|---|---|---|---|---|
| `S-43` | Insurance Authorization | Scheduling | `SCH-B` Compliance | Hard · Yes · Assist |
| `S-44` | Add-On Orders | Scheduling | `SCH-B` Compliance | Hard · Yes · Assist |
| `S-45` | Clinician Safety | Scheduling | `SCH-D` Routing | Hard · Maybe · Assist |

### Tier B — eight new variables

Each traces to an annotation Colin had already written, or to the whiteboard session record.

| ID | Variable | Block | Constraint · MVP · Posture | Traces to |
|---|---|---|---|---|
| `C-14` | Territory currency | `CAP-B` | Structural · Yes · Assist | Colin on `C-03` — territories are static, with no dynamic relationship to present-day distribution |
| `S-46` | Achievable first-visit time | `SCH-C` | Soft · Maybe · **Read** | Colin on `S-05` — *"Preferred vs Possible are 2 different things"* |
| `S-47` | POA status and signing authority | `SCH-J` | Hard · Yes · Assist | Colin on `S-28` — *"POA alert--service failure avoidance, liability"* |
| `S-48` | Rehospitalization risk | `SCH-K` | Soft · Maybe · **Read** | Colin on `S-31` — *"PULSE INTEGRATION?--Risk for rehospitalization"* |
| `S-49` | Review queue state | `SCH-B` | Hard · Yes · **Read** | Plan-of-care QA is a hard stop nobody downstream can see |
| `S-50` | Documentation sync latency | `SCH-M` | Derived · Maybe · **Read** | Citrix delivery — a started visit is not a completed one |
| `CO-13` | Patient & caregiver contact channel | `CRD-A` | Hard · Yes · Control | Colin on `S-28` — *"Phone Number for scheduling"* |
| `CO-14` | Consent state by channel | `CRD-A` | Hard · Yes · Control | Consents signed at SOC; a legal gate, not a preference |

**`C-14` and `S-46` are the two with the most leverage** — each records whether something is
*working* rather than what it *is*.

Rows are ordered by category block, not by ID, so the new IDs sit non-sequentially inside their
blocks. That is deliberate: category rollups must reference contiguous child rows.

### Tier C — recorded, deliberately NOT adopted

Five reimbursement-dependent variables are **parked on `Decisions & Parking Lot`, not added to the
inventory**, because managed Medicare behaviour across UHC, Humana and others is still under separate
research and a single financial rule cannot be applied across the book.

`SH-10` payer class · `SH-11` hospital discharge date · `SH-12` payment period & case-mix group ·
`SH-13` LUPA threshold · `S-51` period utilization against payment.

**These five IDs are reserved. Do not reuse them.** The new Shared-layer category they would need
(*Authorization & Payer*) has deliberately not been created.

No payment or margin logic has entered the Scorecard, the ROI tab, or any KPI. Standing decisions to
that effect are now recorded on `Decisions & Parking Lot` rows 7–10.

### Not variables

Five items that are real but are capabilities, product limits or process defects rather than factors
in the equation are recorded on the Parking Lot so they are not re-litigated: clinician reassignment
authority, supervisee schedule visibility, per-discipline task multiplication, the seven-day clinician
schedule horizon, and authorization notification volume.

## 4. Module grouping added

Handoff 2's three modules are now a column on the inventory (`T`), the dictionary (`N`) and the
Scorecard (`Q`), with a dropdown on the inventory. **Module is an additional grouping — it does not
replace Layer or Rollup Key, and every join still joins on ID.**

| Module | Variables | What it holds |
|---|---|---|
| Capacity Management | **34** | `SH-01`–`SH-09`, `C-01`–`C-14`, `S-04`–`S-13` (clinician declarations), `S-46` |
| Scheduling Engine | **33** | demand, compliance, matching, routing, dependency, exception, distribution, `CO-09`–`CO-12` |
| Patient Engagement | **20** | `S-23`–`S-30`, `S-32`, `S-47`, `CO-01`–`CO-08`, `CO-13`, `CO-14` |

Every variable sits in exactly one module, so the three cover the requirement universe once.
`Footprint & Fit` rows 42–45 now roll coverage up by module alongside the existing category rows.

Note the deliberate crossings: `S-04`–`S-13` sit in the Scheduling *layer* but the Capacity
Management *module*, because they are clinician declarations kept current there. `CO-09`–`CO-12` sit
in the Coordination layer but the Scheduling Engine, because they are the office-and-clinician half
of coordination.

## 5. Sync defects found and corrected

The `Functional Scorecard` is a hand-maintained mirror of the inventory, and it had drifted. Both were
already on the backlog's watch list as "applied to our documents" — they had never reached the
Scorecard.

| Row | Field | Was | Now | Why |
|---|---|---|---|---|
| `S-23` Gender preference | MVP Req. / Weight | `Yes` / 3 | `No` / 0 | Inventory is the source of truth |
| `S-25` Time-of-day refusal | Gating? | `Y` | `N` | Constraint is `Soft`, so the gating formula returns N |
| `S-25` Time-of-day refusal | Constraint *(dictionary)* | `Hard` | `Soft` | Handoff 2 settles it: *"not a hard constraint — it is a negotiation"* |
| `S-07`, `S-43`, `S-44`, `S-45` | Name *(dictionary)* | shortened variants | inventory names | Colin authored the inventory names |

**Every mirrored column on the Scorecard — MVP Req., Our Posture, Gating?, Conflict Risk, Weight,
Rollup Key — was re-derived from the inventory, so the two tabs are byte-identical on those fields as
of this update.** They are still literal values, not formulas, so **they will drift again**: re-sync
whenever a variable is added or changed. A note to that effect is on the Scorecard column key.

## 6. What this does to the vendor scores

**Footprint drops, and that is the correct behaviour.**

| Measure | HCHB Web Scheduling | HCHB Smart Scheduling |
|---|---|---|
| Footprint % — before | 35.7% | 70.8% |
| Footprint % — **after** | **31.6%** | **62.7%** |
| Overall weighted rating | 62.1 → **62.1** | 71.2 → **71.2** |

The requirement universe grew by eleven variables that neither product has been scored against, so
footprint dilutes. Nothing about either product's assessment changed — the overall weighted rating is
untouched, because it averages only over rated rows.

**35 of 87 variables are now unscored against both products, up from 24 of 76.** The eleven new rows
are the addition. Scoring them is the next scorecard action — `S-43` Insurance Authorization most of
all, since it is the largest single bottleneck in the process and no product has been asked about it.

Module coverage on the new `Footprint & Fit` band: Capacity Management 70.5, Scheduling Engine 75.1,
Patient Engagement 64.6 (combined, selected products). Read it **against** the category rows, not
instead of them — a module average masks the six categories still showing as GAP.

## 7. Integrity checks run

- All 14 tabs recalculated; **zero formula errors** before and after.
- **Nine of fourteen tabs are byte-identical** to the source: `Big Picture`, `The Process`,
  `The Concepts That Matter`, the four stakeholder registers, `KPIs & Baseline`, `ROI & Finance Case`.
- Every pre-existing variable row diffed field-by-field: **zero content changes** outside the new
  Module column and the per-row Weight/Gating formulas, which were rewritten so their references
  follow the shifted rows.
- All 32 category rollup formulas on the Scorecard rebuilt from their actual child rows.
- Data validation dropdowns rebuilt across the new row ranges, including a new Module dropdown.
- Inventory and dictionary cross-audited on name, constraint, posture, confidence and source:
  87 = 87, no orphans either way, all discrepancies resolved (§5).

## 8. Next free IDs

**`C-15` · `CO-15`** — and for the Shared and Scheduling layers, the next free codes are **`SH-14`**
and **`S-52`**, because `SH-10`–`SH-13` and `S-51` are reserved for Tier C.

## 9. Open questions carried forward

Recorded on `Decisions & Parking Lot`:

1. Does Pulse expose rehospitalization risk at patient level in a form scheduling can consume? (`S-48`)
2. Legal confirmation on outbound automated calling before any Patient Engagement design (`CO-14`).
   At least one state treats a call not manually triggered by a human as a robocall.
3. The reimbursement research itself — until it closes, Tier C stays parked and no payment logic
   enters the Scorecard, the ROI tab or any KPI.
