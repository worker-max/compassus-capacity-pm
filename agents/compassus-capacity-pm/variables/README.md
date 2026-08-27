# Variable workbook

`8.13-Compassus-Capacity-Scheduling-Workbook.xlsx` — the origin workbook from the 13 August
on-site, pulled from Drive. Fourteen tabs: the Variable Inventory the IDs come from, plus the
Functional Scorecard, Definitions & Concepts, Decisions & Parking Lot, KPIs & Baseline, ROI &
Finance Case, and the four role tabs. Kept here because the team is migrating off it and the
migration has to be checked against something.

`CapacitySchedulingVariableWorkbook.xlsx` — the unabridged variable inventory. One row per
variable, numbered in four layers: `SH-` shared, `C-` capacity, `S-` scheduling, `CO-`
coordination and engagement. The ID is the join key back to the 8.13 workbook, so IDs are
never reused or renumbered.

Sheets: **Start Here** (how to read a row) · **Master List** (the inventory) ·
**Lists** (permitted dropdown values) · **Roles** (role names and flow-map colours).

## State as of 26 Aug 2026

93 numbered rows, sequential with no gaps: SH-01..09, C-01..14, S-01..54, CO-01..16.

Six rows are highlighted yellow and all six need MVP, gating and posture confirmed:

| ID | Variable | Why it is new |
|---|---|---|
| `CO-15` | Incentives and offers on hard-to-fill visits | Existed in this workbook as a row with the literal ID `gap`, so it never rolled up. It is **not** recovered from the 8.13 inventory — that inventory has no incentives row. It originates in the 21 Aug vendor ask |
| `S-51` | The clinician's five dispositions | 13 Aug backlog, confirmed real, never drafted. Refined 18 Aug |
| `S-52` | The clinician's own weekly plan | 13 Aug backlog. The largest undocumented decision process in the model |
| `S-53` | Physical barriers and crossing windows | 13 Aug backlog. Placement decision still open |
| `S-54` | Hand-off to one's own assistant | 13 Aug backlog. HCHB design choice, not a Medicare rule |
| `CO-16` | A self-serve board of open visits | 13 Aug backlog. Overlaps `CO-15` — decide whether they are one row or two |

The descriptive columns on those six are sourced from the 13 and 18 Aug sessions. MVP is set
to `--` and gating left blank deliberately: those are calls for the team, and each row's
*Open question* column names exactly what has to be decided.

## Resolved without a new row

- **Rapid reschedule (HCHB flag)** — captured as a note on `CO-07`, not as its own row. The
  8.13 backlog left open whether branch configuration belongs in the inventory; keeping it as
  a note is that question answered the conservative way.
- **Plan-of-care QA / DCS clearance** — folded into `S-49`.
- **Consent and power of attorney** — landed 19 Aug as `S-47` (who may sign) and `CO-14` (consent to contact). `CO-13` is the verified-number row, which is adjacent but different.

## Restored from the 8.13 inventory — 26 Aug

Nine per-variable columns existed in the 8.13 `Variable Inventory` and had no home here, which
meant retiring that workbook would have lost them. They are appended, suffixed `(8.13)` to mark
provenance, and populated by ID for the 76 legacy rows. The 17 rows added since are blank —
those values were never assessed.

| Column | Why it matters |
|---|---|
| `Constraint (8.13)` | Hard / Soft / Structural / Derived / Config / Event / Context. `Gating` is derived from it, so without it the derivation is unauditable. The single most consequential loss |
| `Conflict risk (8.13)` | 14 rows flagged `Y` — where a vendor's built-in way of working could contradict ours |
| `Weight (8.13)` · `Rollup key (8.13)` | The `Functional Scorecard` formulas key on these. `Rollup key` carries a 32-way category rollup that `One-pager group` collapses to 10 |
| `Automation confidence (8.13)` | **Not the same as this sheet's `Confidence` column.** That one is about where the data lives; this one is how safely software can act on the variable. 32 of 76 values differ — do not read one as the other |
| `Measurability` · `Sourced by` · `Current state` · `Source of truth` | Machine-groupable enums that became free prose here. `Current state` marks 26 rows `Tacit` |

## Known ID hazard

`artifacts/variable-backlog.md` reserved `S-43` and `S-44` for consent and POA availability and
said **do not reuse**. This workbook binds `S-43` to Insurance authorization, `S-44` to Add-on
orders, and shifts `S-45`, `S-46`, `S-47` accordingly. The rebinding happened when this workbook
was first built and is now load-bearing — the fix is to correct the backlog, not the sheet. Any
document citing `S-43` through `S-47` against the backlog's numbering is wrong.
