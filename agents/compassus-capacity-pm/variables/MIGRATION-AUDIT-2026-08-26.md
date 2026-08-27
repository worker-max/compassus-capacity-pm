# Migration audit — retiring the 8.13 workbook

Three parallel audits, run 26 Aug, against `8.13-Compassus-Capacity-Scheduling-Workbook.xlsx`
(14 tabs), `CapacitySchedulingVariableWorkbook.xlsx` (4 tabs) and
`rfp/Compassus-Vendor-Questionnaire-MASTER.xlsx`. Every finding below was verified directly
against the files before being recorded.

## Verdict

**The variable inventory migrates cleanly. Everything else in the 8.13 workbook does not.**

All 79 variable rows survive — 76 by ID, plus the 3 the 8.13 sheet carried without IDs, which
landed as `S-43`, `S-44`, `S-45`. Zero variables dropped. MVP values are identical on all 76.

The exposure is in the other thirteen tabs, and in nine per-variable columns.

## Fixed in this pass

| | |
|---|---|
| Nine 8.13 columns had no home here | Restored, suffixed `(8.13)`, populated by ID. See the workbook README |
| `Incentives & offers` was a Part B grid row with **zero** variables behind it | `CO-15` and `CO-16` were filed under `When plans change`; both re-keyed. A coverage rollup would have scored that row 0/0 and silently dropped the vendor's answer |
| README claimed consent landed as `CO-13` | It is `CO-14`. `CO-13` is the verified-number row |
| README implied `CO-15` was recovered from the 8.13 inventory | It was not — that inventory has no incentives row. `CO-15` originates in the 21 Aug vendor ask |
| `Start Here` still read "87 variables… plus 1 flagged gap" | Now states 93 with its composition |
| The backlog's ID reservations contradicted the workbook | Backlog marked superseded, with the authoritative bindings recorded |

## Decisions needed — content that exists in exactly one place

Grep confirms none of the following appears anywhere in this repo, the variable workbook, or
the questionnaire.

**1. Functional Scorecard.** 76 variables scored against HCHB Web Scheduling and Smart
Scheduling. Contains **16 posture-overreach findings** — where a product decides what we said a
human must decide. `S-22`: *"OVERREACH - Continuity is a core optimization: the engine
auto-assigns to maximize a weighted continuity score and can override manual assignments,
exceeding our Assist posture."* This is the evidence behind DE-09 and the sharpest question to
put to any vendor. Also 14 conflict-risk flags and the scoring weights. **The scorecard's
formulas need `Weight`, `Rollup key`, `Conflict risk` and `Row Type` — the first three are now
restored here, so decide whether scoring continues in the 8.13 file or moves.**

**2. Footprint & Fit.** Multi-product combination analysis. **6 categories remain GAP with both
HCHB products selected**, including Scheduling/Compliance — meaning neither incumbent touches
ordered-frequency windows, SOC timing or recert windows, all three MVP=Yes and gating. A
knockout finding about the incumbent, living in one cell.

**3. ROI & Finance Case.** $7.9M/yr moderate across ~80 branches, with the eight-driver
assumptions block it computes from, three scenarios, the four-line per-branch decomposition, the
argued rebuttal to *"why not just a spreadsheet and an AI?"*, the hospice-extension argument, and
the CMS anchors. Without the assumptions block the headline number is unsourced.

**4. KPIs & Baseline.** Primary/secondary tiering, per-metric definition, lever, lead/lag and
source system, and the honest "Available today?" audit — 6 No, 5 Partial, 1 Yes. Four metrics
have no counterpart anywhere, including schedule volatility and tool adoption. The tab calls
capturing this baseline the initiative's first deliverable.

**5. Keep vs. offload.** 49 touchpoints of product-scope boundary in the stakeholder's own
voice. `CL-02`: *"Keep ownership of my availability. Offload only the honoring of it, never the
overriding."* Keyed to variable IDs, so it merges as a column rather than a sheet.

**6. Clinician and patient archetypes.** Seven each, with malleability ratings and system
directives, plus negative resting patterns. Alabama failed on change management, not algorithm
quality — this is the only asset addressing that failure mode. There is no patient perspective
anywhere else in the repo.

**Nothing to rescue** from Decisions & Parking Lot (never filled in — the real record is DE-01
to DE-10 in `knowledge/whiteboard-session-2026-08-13.md`), The Process Step by Step, Big
Picture, or The Concepts That Matter.

## Open items in the vendor ask

- **22 of 93 variables fail the `Placement check`.** The workbook files a variable by whose
  constraint it is; the one-pager by where the engine consumes it. The patient-constraint block
  is the costly seam — 6 MVP=Yes, 5 gating. Recommendation: score coverage off `One-pager group`
  only and treat `Arena` as provenance.
- **Four `Ruled 25 Aug` write-backs** (`CO-09`–`CO-12`) are decided and still undone.
- **The two grids are not supersets of each other.** The expanded 41-row grid has no incentives
  row; the standard 11-row grid does. Its own subtitle tells a reader to use it *instead of* the
  standard grid, which would drop the question entirely.
- **Blind spots with no question and no grid row:** contactability and consent (`CO-13`,
  `CO-14`, `CO-05` — two are MVP=Yes and gating); territory currency and geography realism
  (`C-14`, `C-04`, `S-53`, `S-46`); queue depth and add-on orders (`S-49`, `S-44`). The team's
  own reserve list already carries the first two, held out of round one deliberately.
- **`S-45` Clinician safety** is asked nowhere. The word "safety" appears on no tab of the
  questionnaire.

## Changes worth a human eye

- **Posture changed meaning on 4 rows**, not just wording. `CO-01` day-before confirmation moved
  Assist → **Automate**, which shifts a patient-contact step from person-confirms to tool-does-it.
- **Gating moved N → Y on 4 rows**: `C-04`, `C-06`, `C-08`, `CO-02`. `CO-02` makes automated
  reminders a product disqualifier.
- **Five rows have `Gating` blank** (the 26 Aug additions), so the knockout count is not final.
