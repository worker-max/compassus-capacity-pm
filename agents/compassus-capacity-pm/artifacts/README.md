# Artifacts — Capacity, Scheduling & Engagement

> **Start here if you are a new session.** This folder holds the working artifacts for the capacity
> and scheduling model. The three-arena model below is the current shared framing; the documents in
> this folder are all views onto it at different depths.

## The model in one paragraph

**Capacity Management** is the envelope — how much work a branch can deliver, given people, hours,
disciplines and territory, netted against what is already booked. The **Scheduling Engine** fills
that envelope: which clinician, which day, which route. **Patient Engagement** defends it: the
confirmation, coverage and rebooking work that turns a schedule into delivered visits. The latter
two are grouped inside a shaded **Coordination** zone, because both are activities performed
*against* the envelope rather than parts of it. Only a completed visit becomes revenue; a discharge hands room back to
capacity.

## Source of truth

| | |
|---|---|
| **Primary workbook** | `8.13 Compassus Capacity & Scheduling Workbook.xlsx` — Google Drive `1tVEkPO2FJMFVyqLZP1TrzqbmjX0qEDgv`. Supersedes the 2026-08-11 version (`15rus_8HKOoXkeZmEBvEP51TCNuu_sOzf`). Columns **G (Notes)** and **S (Additional Context)** now carry pain-point, bottleneck and road-bump commentary — read them, they are where the operational truth is |
| Tabs that drive these documents | `The Concepts That Matter` (the 15-factor distillation → prominence) and `Variable Inventory` (79 scored variables → priority) |
| Data-model workbook | `Clinician-Capacity-Tool_Data-Index.xlsx` — Drive `1BFxo6k3tSDyoJZxmm7_gFxmnuEm4S_fW` |
| Drive folder | `1WEf_6FN7963y-MGwP3S3GaaPvqJ2RNF3` |
| Original flow map | `8.13 capacity scheduling swimlane detail.pdf` — Drive `1SZDHuYYzkMLP-J7uCKdITY3CGZA3qhCx` (page 2 of a set; page 1 is *Home Health Intake Reset*) |
| Flow clarifying document | Drive `1NSHlkaWir6rc7mgZ1ONtwG-sIPsNFayV` — four flows with redraw refinements |
| On-site whiteboard session | [`../knowledge/whiteboard-session-2026-08-13.md`](../knowledge/whiteboard-session-2026-08-13.md) — decisions DE-01…DE-10 |
| Discovery ground truth | [`../knowledge/`](../knowledge/) |

**The workbook is authoritative. These documents are downstream of it** — if a variable changes
there, change it here, not the other way round.

### How priority was derived

Straight from the `Variable Inventory` scoring, not from judgment:

- **Weight** — MVP Req. `Yes` = 3, `Maybe` = 1, `No` = 0
- **Gating** — `Constraint` is Hard or Structural **and** MVP Req. is `Yes`. A knockout: a product
  that cannot do it should be disqualified however well it scores elsewhere.
- **Conflict risk** — the vendor's built-in way of working could contradict how Compassus operates.

Variable IDs (`SH-`, `C-`, `S-`, `CO-`) are the join key back to the workbook and are never
renumbered.

## The documents

| File | What it is | Use it for |
|---|---|---|
| `Capacity-Scheduling-One-Pager.pdf` | One A4 landscape page: three categories, primary variables only | The handout. Meetings, email, print |
| `capacity-scheduling-one-pager.html` | Source for the PDF above | Edit here, then re-render |
| `Capacity-Scheduling-Variable-Reference.pdf` | Three A4 landscape pages, one per category, carrying every variable | The supporting handout. Pairs with the one-pager as a 4-page set |
| `capacity-scheduling-full-lists.html` | Source for the reference above | Edit here, then re-render |
| `capacity-scheduling-board.html` | 4 pages — the three boxes, then every variable per box | The working list |
| `capacity-scheduling-diagram.html` | Flow figure, sketch-to-model mapping, and per-variable detail (constraint, MVP, posture, current state) | The reference / supporting document |
| `capacity-tool-data-index.md` | Full capacity-vision data dictionary (domains A–J) | Field-level data planning |
| `capacity-tool-mockup-data-spec.md` | The built tool's actual data model + as-built review | What exists today |
| `capacity-ecosystem-map.md` | Coverage scan — the structural gaps (1A readiness, 1B economics, 1C quality) | What the model still cannot see |
| `source-war-list-worksheet.{md,csv}` | Where each data element actually comes from | Source war-listing sessions |
| `Primary-Flow-Map.pdf` | **The primary current-state map** — the whole episode in four phases, with the detail flows condensed | The wall sheet. Orientation for anyone new, and the map the detail flows hang off |
| `flow-primary-map.html` | Source. Regenerate with `_flow-primary-map.gen.py` | Editing the primary map |
| `Flow-Routine-Visits.pdf` | Flow 2 — routine visits, two phases, the day-before negotiation panel (hard vs. soft) and the five day-before dispositions | The clinician's own week |
| `flow-routine-visits.html` | Source. Regenerate with `_flow-routine-visits.gen.py` | Editing flow 2 |
| `Flow-Authorization.pdf` | Flow 3 — auth at its two interfaces: the gate at start of care and the ceiling inside the plan of care | Explaining why a referral cannot be scheduled, and why a plan of care outruns its budget |
| `flow-authorization.html` | Source. Regenerate with `_flow-authorization.gen.py` | Editing flow 3 |
| `Flow-DCS-Scheduler.pdf` | One A4 landscape page: the DCS / scheduler handoff | Demonstrating the handoff; testing the conventions |
| `flow-dcs-scheduler.html` | Source for the above. Regenerate the SVG with `_flow-dcs-scheduler.gen.py`, then swap it into the `<svg>` block | Editing the flow |
| `flow-map-redraw-assessment.md` | Assessment of the swimlane map against the four flows, with the correction inventory and the open legend decision | Planning the flow-map redraw |
| `variable-backlog.md` | **Running list of variables not yet numbered in the workbook** | Append here as new ones surface; work it down when updating the workbook |

**Flow-map palette** (sampled from the original sheet, do not re-guess): Intake `#1F6F78` *(new, added
17 Aug — intake and the auth team are different actors)* · PCC/Scheduler `#C6A01F` ·
HCHB `#795CA7` · DCS `#792E2E` · Clinician `#2E599D` · Per Diem/Float `#795933` · Patient `#4E8A5B`
· Insurance & Auth `#DF751D` · Branch Leadership `#1A1A1A` with white text.

**Size convention:** large block = happens every time · small block = conditional · pill = watch
condition, not a step. Introduced so weight on the page matches weight in the process.

**Variable chips are OFF.** The generators support a light chip under each step naming the deciding
variables, but `SHOW_VCHIPS = False` until the variable IDs are settled. More capacity and scheduling
variables are still to be added, and five existing rows have no ID yet — see
[`variable-backlog.md`](./variable-backlog.md). Printing IDs on a sheet before they are stable means
they go silently wrong on renumber. Flip the flag once the backlog has landed.

**Flow-map canvas rule.** Canvas units are **points on the output sheet**, so a 16-unit label prints
at 16pt. Draw at sheet scale (the original is 2070 × 1380 pt) rather than at A4 and shrinking —
A4-scale canvases print block text at about 4.5pt, which is unreadable. Always landscape, one
unbroken spine, canvas width follows the content.

**Editing rule:** the one-pager, the full lists, the board and the diagram carry the same variable
set at different depths. Change one, change all four, or they drift.

**The handout set** is the one-pager (page 1, summary) plus the variable reference (pages 2–4, one
per category). Both are A4 landscape and print as a matched 4-page set.

### Re-rendering the PDF

The PDF is generated from the HTML with headless Chromium. The artifact host wraps a published file
in a `<!doctype><head><body>` skeleton, so the renderer must do the same or the print CSS will not
apply:

```python
# wrap raw file in <!doctype html><html><head>…</head><body> … </body></html> first
page.emulate_media(media="print", color_scheme="light")
page.pdf(path=out, format="A4", landscape=True, print_background=True,
         prefer_css_page_size=True, margin={"top":"9mm","bottom":"9mm",
                                            "left":"9mm","right":"9mm"})
```

Chromium is at `/opt/pw-browsers/chromium-1194/chrome-linux/chrome`. Expect one page,
MediaBox `841.92 x 594.96` pt. Verify both before committing.

## Decisions taken (do not silently reverse)

1. **Module names follow DE-02 (13 Aug 2026): Capacity Management, Scheduling Engine, Patient
   Engagement.** The workbook still uses *Coordination* for the `CO-` layer; in these documents that
   layer is drawn as **Patient Engagement**, and *Coordination* names the shaded zone holding both
   Scheduling Engine and Patient Engagement. Variable codes are unchanged. Note the on-site framed
   these as three peer modules; the zone is an editorial grouping on top of that, not a contradiction.
2. **"Time preference" moved.** The original sketch starred it under Capacity. The workbook models
   it as scheduling constraints (`S-05`, `S-10`, `S-20`), so it sits in Scheduling.
3. **POA means power of attorney.** Consent must be signed before the first visit, or the POA must
   attend to sign it. Neither state is captured anywhere today, so the block surfaces only once the
   clinician is at the door. Written in as two **proposed** variables under a new *Readiness* group:

   | ID | Variable | Constraint | MVP | Posture |
   |---|---|---|---|---|
   | `S-43` | Consent / POA signature status | Config | Yes | Control |
   | `S-44` | POA availability to sign at the visit | Hard | Yes | Read |

   Split because the flag is rule-based and automatable while the POA's availability is a
   fluctuating third-party calendar — the same shape as `S-30`.
4. **No annotations on the board or one-pager.** GATE/NEW badges, tacit highlighting and posture
   columns were deliberately stripped. Those documents are straight lists; the detail lives in the
   diagram and the workbook.

## Changes from the 13 August on-site

- **Three variables added**, all Hard constraint, Assist posture, and **none has an ID yet**:
  *Insurance Authorization* (MVP Yes), *Add-On Orders* (MVP Yes), *Clinician Safety* (MVP Maybe).
  The first two are gating and sit upstream of the scheduler's queue.
- **`S-23` Gender preference** dropped from MVP `Yes` to **`No`**.
- **`S-25` Time-of-day refusal** softened from `Hard` to **`Soft`** — the note explains why:
  "in my years of experience, this preference is malleable based on relationship."
- **`S-07`** renamed *Lunch / documentation pattern*.
- `The Concepts That Matter` tab is **unchanged**, so the capacity primary list is unchanged.
- **Phase 1 is visualization only, no automation** (DE-03). The automation postures in the diagram
  describe the eventual target, not release 1. Do not let a vendor read them as release-1 scope.

## Open items

- **Five variables have no ID**, so they are invisible to the `Functional Scorecard`. Tracked with
  everything else pending in [`variable-backlog.md`](./variable-backlog.md) — keep appending there.
- **The *Readiness* group is now populated** — authorization and add-on orders joined consent/POA.
  Plan-of-care locks and face-to-face / coding holds are the same family and still have no row.
  This was ecosystem gap **1A**; the 13 Aug session closed most of it.
- **Traffic and drive-time still have no variable.** Confirmed on 13 Aug as real and local: the
  Jacksonville bridge (one zip, two non-interchangeable sides) and the California interstate
  crossing window. Routing today is mileage and straight-line proximity.
- **The shift-finder and hand-off surfaces still have no variable.** Both confirmed on 13 Aug —
  HCHB's Shift Finder already exists and is not turned on, and HCHB blocks a nurse handing a visit
  to her own LPN.
- **Counts to keep in sync when variables change:** one-pager and board box footers, board page
  headings ("All 22 / 44 / 12 variables"), and the diagram's provenance line.

## Related

- [`../knowledge/README.md`](../knowledge/README.md) — the ten load-bearing discovery findings
- [`../MASTER-capacity-and-scheduling.md`](../MASTER-capacity-and-scheduling.md) — the assembled master document
- [`../AGENT.md`](../AGENT.md) — the PM agent definition
