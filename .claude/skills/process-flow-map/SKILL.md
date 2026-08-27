---
name: process-flow-map
description: Draw or revise a Compassus process flow map / swimlane / current-state workflow sheet in the house design — banded spine or five-column layout, actor colours, plain-language sublists, rendered to a one-page landscape PDF. Use when asked to map, draw, diagram, redraw or correct a workflow, process flow, swimlane, or any of the numbered flows (SOC/ROC, routine visits, authorization, recert & discharge, the primary map, the detailed composite).
---

# Process flow maps

The house style for Compassus current-state process maps. Seven sheets already exist in it; the job
of this skill is to make the eighth look like it belongs, and to make corrections to the existing
seven land without drift.

## Before drawing anything

1. **Read [`knowledge/process-facts-2026-08.md`](../../../agents/compassus-capacity-pm/knowledge/process-facts-2026-08.md).**
   It is the source-confirmed current-state process. Drawing against a stale mental model is the
   most expensive mistake available here.
2. **Skim [`artifacts/flow-map-redraw-assessment.md`](../../../agents/compassus-capacity-pm/artifacts/flow-map-redraw-assessment.md)**
   (§1–26) if the sheet touches ground that has already been corrected once.
3. **Talk the flow through with the operator before drawing it.** Every sheet in the set needed a
   correction pass that a conversation would have caught first: SOC/ROC didn't start where the first
   draft assumed, intake and auth turned out to be different actors, the 485 turned out to be one
   moment rather than four gates. Ask about sequence, ownership and what happens on the unhappy path.
4. **Say what you are unsure of, explicitly**, and let the operator close it. Do not fill a gap with
   a plausible box — a wrong box on a wall sheet outlives the meeting.

## Build loop

```bash
S=.claude/skills/process-flow-map
mkdir -p /tmp/flow && cd /tmp/flow
# 1. write gen.py:  import sys; sys.path.insert(0, "<abs path>/$S/assets"); from flowkit import *
python3 gen.py                       # emits flow.svg + prints canvas, ratio, last content y
python3 $S/assets/build.py flow.svg out.html out.pdf out.png "Sheet Title" 2600 1780
```

Then **open `out.png` and look at it.** Not optional, and not satisfied by the build command
exiting 0. Crop and re-read any region you just edited:

```python
from PIL import Image
Image.open("out.png").crop((x0, y0, x1, y1)).save("crop.png")   # then Read crop.png
```

Work the [`reference/collision-checklist.md`](reference/collision-checklist.md) against the
screenshot. Iterate the generator — never hand-edit the SVG or the HTML, or the next regeneration
silently discards the fix.

## The design

Full detail in [`reference/design-system.md`](reference/design-system.md). The load-bearing parts:

- **Colour = actor.** A workflow item in HCHB *worked by a person* carries the **person's** colour.
  Purple only where HCHB acts by itself. This is the rule most often got wrong, and it matters
  because colouring in-system steps purple hides exactly the human labour a capacity tool relieves.
- **Canvas units are points on the output sheet.** Draw at sheet scale (2000–2900 wide), landscape,
  ratio ~1.25–1.5. An A4-scale canvas prints block text at ~4.5pt.
- **Size = weight.** Large = every time · small = conditional · pill = a watch condition, not a step.
- **Sublists say what the person is working around** in plain language ("drive time, not distance"),
  never variable IDs — IDs go stale on a renumber.
- **Bands size to their own content**, or short ones read half-empty.
- **Current state only.** Include the waste. Footer says *nothing on this sheet is a proposal*.

## Toolkit

`assets/flowkit.py` — `begin` `finish` `masthead` `legend` `band` `row` `spine` `columns` `panel`
`block` `split_block` `chip` `diamond` `oval` `tag` `sublist` `arrow` `path` `conn` `lbl` `footer`,
plus the `C` palette and `BW/BH/GAP/SLOT/BX/IX` geometry constants.

`row()` takes `(colour, lines, subs, badge, slots)` tuples and returns the centreline; pass
`breaks=(i,)` where two steps are alternatives rather than a sequence — an arrow there asserts an
order that doesn't exist.

`assets/build.py` wraps the SVG in the house HTML (`assets/wrapper.html`), screenshots it, and
renders a one-page landscape PDF. Chromium is at `/opt/pw-browsers/chromium-1194/chrome-linux/chrome`;
`pdf()` rejects `pt`, so the script converts to inches at 72pt/in.

## Shipping

1. Copy the generator beside the sheet as `artifacts/_<name>.gen.py` — every sheet must be
   regenerable without archaeology.
2. Add the PDF + HTML rows to `artifacts/README.md`.
3. Record the reasoning in `artifacts/flow-map-redraw-assessment.md`, and any durable process fact
   in `knowledge/process-facts-2026-08.md`.
4. Commit, push to the working branch, and **publish the artifact** — a fresh PDF alone leaves the
   shared link stale. Send the PDF as a file so it can be downloaded.
5. When a correction lands on one sheet, check whether it applies to the others. The set is only
   worth anything if it stays consistent.

## Existing sheets

| File | What it is |
|---|---|
| `Detailed-Flow-Composite` | The original five-column swimlane, corrected. The wall sheet. |
| `Primary-Flow-Map` | The episode in four phases, detail flows condensed. |
| `Flow-SOC-Full` (1) | Referral pass + the per-discipline plan-of-care pattern. |
| `Flow-Routine-Visits` (2) | The clinician's own week + the day-before negotiation. |
| `Flow-Authorization` (3) | Auth as a gate at SOC, a ceiling inside the plan of care. |
| `Flow-Recert-Discharge` (5) | End of episode, through a worked SN/PT/OT example. |
| `Flow-DCS-Scheduler` | The simplified practice sheet. |
| `Flow-Target-State` | **The only proposal sheet.** The envelope, the episode run against it, every step marked release + posture. |

Read the nearest existing sheet's generator before starting a new one — matching an existing sheet
is faster and safer than reasoning the layout out from scratch.
