# Variable workbook

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
| `CO-15` | Incentives and offers on hard-to-fill visits | Existed as a row but carried no ID, so it never rolled up. Asked of vendors in Part B row 10 from 21 Aug |
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
- **Consent and power of attorney** — landed 19 Aug as `S-47` and `CO-13`.
