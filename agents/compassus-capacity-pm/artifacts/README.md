# Artifacts — Capacity, Scheduling & Engagement

> **Start here if you are a new session.** This folder holds the working artifacts for the capacity
> and scheduling model. The three-arena model below is the current shared framing; the documents in
> this folder are all views onto it at different depths.
>
> **Status (18 Aug 2026, corrected 24 Aug): current-state process flow mapping is DONE** — seven
> sheets, all regenerable from the `_*.gen.py` beside them. The distilled process facts behind every
> sheet live in [`../knowledge/process-facts-2026-08.md`](../knowledge/process-facts-2026-08.md) —
> **read that file before touching any flow sheet.** The correction-by-correction history is
> `flow-map-redraw-assessment.md` §1–28; Laci's 24 Aug pass is §28.

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
| Tabs that drive these documents | `The Concepts That Matter` (the 15-factor distillation → prominence) and `Variable Inventory` (79 scored variables → priority). **79 scored rows = 76 numbered + 3 unnumbered**; only the numbered ones roll up. Full tab-by-tab index and the complete ID list: [`../knowledge/workbook-2026-08-13.md`](../knowledge/workbook-2026-08-13.md) |
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
| `Detailed-Flow-Composite.pdf` | **The original swimlane sheet, redrawn with all corrections** — five columns, the grey clean path, feeders above, recovery below | The wall sheet in the design the team already knows. Page 2 of the set (page 1 is the Intake Reset) |
| `flow-detailed-composite.html` | Source. Regenerate with `_flow-detailed-composite.gen.py` | Editing the detailed composite |
| `Primary-Flow-Map.pdf` | **The primary current-state map** — the whole episode in four phases, with the detail flows condensed | The wall sheet. Orientation for anyone new, and the map the detail flows hang off |
| `flow-primary-map.html` | Source. Regenerate with `_flow-primary-map.gen.py` | Editing the primary map |
| `Flow-SOC-Full.pdf` | Flow 1 — the full SOC/ROC flow: referral pass, then the per-discipline plan-of-care pattern, with the welcome call and the 485 moment | The detailed admission flow, in the shape the team already knows |
| `flow-soc-full.html` | Source. Regenerate with `_flow-soc-full.gen.py` | Editing flow 1 |
| `Flow-Routine-Visits.pdf` | Flow 2 — routine visits, two phases, the day-before negotiation panel (hard vs. soft) and the five day-before dispositions | The clinician's own week |
| `flow-routine-visits.html` | Source. Regenerate with `_flow-routine-visits.gen.py` | Editing flow 2 |
| `Flow-Authorization.pdf` | Flow 3 — auth at its two interfaces: the gate at start of care and the ceiling inside the plan of care | Explaining why a referral cannot be scheduled, and why a plan of care outruns its budget |
| `flow-authorization.html` | Source. Regenerate with `_flow-authorization.gen.py` | Editing flow 3 |
| `Flow-Recert-Discharge.pdf` | Flow 5 — recert & discharge through a worked example: SN discharges at day 52–53 (non-OASIS, outside the window), PT carries the OASIS recert, OT does a non-OASIS eval, next-period orders PT 2w3→1w3 · OT 1w4 | The end-of-episode teaching sheet; the primary map's phase 4 expanded |
| `flow-recert-discharge.html` | Source. Regenerate with `_flow-recert-discharge.gen.py` | Editing flow 5 |
| `Flow-SOC-Target-State.pdf` | **Flow 1T — start of care, TARGET STATE (v1.0)**. The same flow as the current-state sheet, every step marked Automate / Assist / Surface / Manual | The future-state conversation. Pairs with `Flow-SOC-Full.pdf` side by side |
| `flow-soc-target.html` | Source. Regenerate with `_flow-soc-target.gen.py` | Editing the SOC target state |
| `Episode-Target-State.pdf` | **The episode end to end, TARGET STATE (v1.0)**. Four phases, same as the primary map, posture-marked | The future-state wall sheet. Pairs with `Primary-Flow-Map.pdf` |
| `flow-episode-target.html` | Source. Regenerate with `_flow-episode-target.gen.py` | Editing the episode target state |
| `Flow-Routine-Visits-Target-State.pdf` | **Flow 2T — routine visit scheduling, TARGET STATE (v1.0)**. Positional clone of `Flow-Routine-Visits`; the per-discipline assignment-task burst is ghosted | Pairs with `Flow-Routine-Visits.pdf` side by side |
| `flow-routine-visits-target.html` | Source. Regenerate with `_flow-routine-visits-target.gen.py` | Editing flow 2T |
| `Flow-Authorization-Target-State.pdf` | **Flow 3T — authorization, TARGET STATE (v1.0)**. Positional clone of `Flow-Authorization`; pending auth is derived rather than keyed, and the pending visit stays visible and counted | Pairs with `Flow-Authorization.pdf` side by side |
| `flow-authorization-target.html` | Source. Regenerate with `_flow-authorization-target.gen.py` | Editing flow 3T |
| `Flow-DCS-Scheduler-Target-State.pdf` | **Plan of care → assignment, TARGET STATE (v1.0)**. Positional clone of `Flow-DCS-Scheduler`; DCS approval per discipline is unchanged, the pending-auth dead end is ghosted | Pairs with `Flow-DCS-Scheduler.pdf` side by side |
| `flow-dcs-scheduler-target.html` | Source. Regenerate with `_flow-dcs-scheduler-target.gen.py` | Editing the DCS/scheduler target state |
| `Flow-Recert-Discharge-Target-State.pdf` | **Flow 5T — recert & discharge, TARGET STATE (v1.0)**. Positional clone of `Flow-Recert-Discharge`; same worked example, same timeline, the no-auth dead end is ghosted | Pairs with `Flow-Recert-Discharge.pdf` side by side |
| `flow-recert-discharge-target.html` | Source. Regenerate with `_flow-recert-discharge-target.gen.py` | Editing flow 5T |
| `business-case-register.md` | **Every financially-connected case tied to the initiative** — workforce and administrative cost, revenue capture, utilisation and margin, growth, quality-linked revenue, risk avoided and option value, with sizing formulas and the inputs needed to commit them | Building the business case. Start here |
| `reimbursement-linked-variables.md` | The factors reimbursement adds to the logic, organised by where each binds — the payer spine, the authorisation object, capacity additions, derived fields and postures | Requirements and data-model work |
| `authorization-and-capacity-forecasting.md` | How authorisation enters the capacity forecast: what is deterministic and ignored, what is genuinely unpredictable, and the three curves the forecast should emit | Forecasting design |
| `Flow-Payer-Economics.pdf` | Payer economics against the schedule: the gate that is payer-dependent, the plan of care where payer limits are invisible, the five values one delivered visit can carry, the four meanings of one missed visit, and the new period as a new authorisation question | Explaining why the same operational event costs differently in every payer class |
| `flow-payer-economics.html` | Source. Regenerate with `_flow-payer-economics.gen.py` | Editing the payer economics sheet |
| `payer-types-and-episode-economics.md` | Reference document: episodic vs non-episodic, managed vs unmanaged, the four ceilings, CY2026 amounts, the authorisation object, and where the Blues land | The payer reference. Pairs with the sheet |
| `reimbursement-research/` | The sourced research corpus behind both: PDGM mechanics and rates, Medicare Advantage, commercial and Medicaid, utilisation and margin, cost and labour, authorisation operations, value-based and policy | Checking a figure, or its source |
| `Flow-DCS-Scheduler.pdf` | One A4 landscape page: the DCS / scheduler handoff | Demonstrating the handoff; testing the conventions |
| `flow-dcs-scheduler.html` | Source for the above. Regenerate the SVG with `_flow-dcs-scheduler.gen.py`, then swap it into the `<svg>` block | Editing the flow |
| `flow-map-redraw-assessment.md` | The full working record of the redraw, §1–26: correction inventory, every conversational decision, the eight answers, and each sheet's build notes | The history; the distilled facts are in `../knowledge/process-facts-2026-08.md` |
| `variable-backlog.md` | **Running list of variables not yet numbered in the workbook** | Append here as new ones surface; work it down when updating the workbook |
| `Source-Original-Swimlane-Detail.pdf` | **The original hand-built swimlane map**, before the redraw. Page 2 of a set; page 1 is *Home Health Intake Reset* | Checking what the composite was redrawn *from* |
| `Capacity-Scheduling-Elemental.pdf` | The six-category plain-terms view — Workforce · Capacity · Demand · Scheduling · Coordination · Results — with primary variables per category | Explaining the model to someone in one page, without the arena vocabulary |
| `Scenario-Clinician-Day-In-The-Life.pdf` | One SN, five visits, 7.25 points against a ~7.0 ceiling — every constraint tagged by class | Showing what the variables *feel like* in a real day |
| `Scenario-Scheduler-Callout-Recovery.pdf` | The same day after a 6:45am call-out: one must-cover, four reschedulable, with the DCS escalation contingency | The worked companion to bottleneck 7 (call-out recovery) |
| `Scenario-Branch-Leader-Territory-Review.pdf` | The ED's quarterly read — four territories classified, then the read-then-lever decision | The worked companion to bottleneck 5 (territory) |

**The four scenario / elemental sheets are illustrative.** Fictional patients, territories and figures;
the decision logic is real. They predate the 13 Aug on-site and use the earlier six-category framing —
the plain-terms ancestor of the three-arena model (DE-02), not a contradiction. Provenance for all of
them is in [`../knowledge/DRIVE-INDEX.md`](../knowledge/DRIVE-INDEX.md).

**Drawing a new sheet or correcting one? Use the `process-flow-map` skill**
([`.claude/skills/process-flow-map/`](../../../.claude/skills/process-flow-map/)) — it carries the
palette, the type scale, the `flowkit` drawing primitives, the render/PDF build script, and the
collision checklist. Do not re-derive the conventions by hand.

**Flow-map palette** (sampled from the original sheet, do not re-guess): Intake `#1F6F78` *(new, added
17 Aug — intake and the auth team are different actors)* · PCC/Scheduler `#C6A01F` ·
HCHB `#795CA7` · DCS `#792E2E` · Clinician `#2E599D` · Per Diem/Float `#795933` · Patient `#4E8A5B`
· Insurance & Auth `#DF751D` · Branch Leadership `#1A1A1A` with white text.

**Colour = actor, and the person beats the system.** A workflow item in HCHB worked by a person
carries the person's colour — purple appears only where HCHB acts by itself (generates tasks,
applies rules, checks auth, suggests a route). Every sheet is current state; nothing on them is a
proposal, and each footer says so.

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


### Target-state sheets — a different contract from the rest of the set

**Six sheets are proposals**, and they invert the set's usual footer. Every one of them says
*TARGET STATE, PROPOSED* and carries the DE-03 horizon line, because phase 1 is held to
visualisation only — nothing on them is release-1 scope. Each is a **positional clone** of one
current-state sheet, so the pair overlays block for block:

| Target sheet | Its current-state twin |
|---|---|
| `Flow-SOC-Target-State` (1T) | `Detailed-Flow-Composite` — **not** `Flow-SOC-Full`; see the warning below |
| `Episode-Target-State` | `Primary-Flow-Map` |
| `Flow-Routine-Visits-Target-State` (2T) | `Flow-Routine-Visits` |
| `Flow-Authorization-Target-State` (3T) | `Flow-Authorization` |
| `Flow-DCS-Scheduler-Target-State` | `Flow-DCS-Scheduler` |
| `Flow-Recert-Discharge-Target-State` (5T) | `Flow-Recert-Discharge` |

**Hash the original before you clone it.** The Drive titles and the repo filenames do not agree, and
a target sheet was once built against the wrong original for exactly that reason. Every pairing above
was confirmed by md5 against the file the team is actually circulating.

**On a positional clone, a better idea that moves a block is a worse sheet.** If the target state
needs to say something different about a step, say it in that block's text, its badge or its fill —
never by splitting it, resizing it or moving it. The cross-reference numbering is decoration the
moment the two sheets stop overlaying.

They add one thing to the drawing grammar, and nothing else changes:

| Posture | How it is drawn | What it means |
|---|---|---|
| **Engine** | solid **`#A6E22E`**, dark text | the engine does it; a person owns the exception |
| **Assist** | engine block with the person's colour as a bar down the right edge | the engine proposes, the named person confirms |
| **Surface** | the person's colour with an engine stripe across the top | the engine shows, the person decides |
| **HCHB** | solid HCHB purple `#795CA7` | **still done inside HCHB — unchanged** |
| **Manual** | plain person's colour | unchanged — hands on the patient |

**The engine colour is `#A6E22E`, and it is the only light block in the set.** Every one of the nine
actor colours is dark and carries white text; the engine carries **dark** text. That is deliberate —
it is the one channel that survives greyscale, photocopying and all three types of colour blindness.
The measured case: the existing palette spans relative luminance 0.010–0.372, and `#A6E22E` sits at
0.70 — a third of the scale clear of anything already in use. A bright pink was tested and rejected:
`#FF1493` lands at 0.239, *inside* the existing range, so it is indistinguishable from Patient green
and Auth orange the moment a sheet is printed in mono. Hue alone cannot carry a tenth colour — a full
sweep of colour space found nothing more than ΔE00 ≈ 19 from the existing nine once colour-blind
simulation is included. Lightness plus dark text is what makes the engine legible.

**HCHB purple keeps its meaning.** A target-state block is purple only where the work still happens
inside HCHB — visit generation, the per-visit auth check, the clinician's calendar. That way the
sheets answer "what did we actually take off HCHB" at a glance.

### The visualise-only sheets — what release 1 actually lights up

The target sheets describe the eventual target. DE-03 holds phase 1 to **visualisation only**, so a
target sheet handed to a vendor or a branch reads as a promise nobody made. `_flow_vis.py` derives
the release-1 sheets from the target generators — same instrumentation trick as `_flow_live.py`, so
they stay positional clones of the current-state sheets for free.

**Two documents per flow, because they answer different questions.**

| Document | Question it answers |
|---|---|
| `*-Visualise-Full-Scenario.pdf` | What does the picture look like when **every report** named on the current-state sheets is feeding it? |
| `*-Visualise-MVP.pdf` | What does **release 1** actually light up? Everything else is drawn `NOT IN MVP`, so the gap between the two documents *is* the release-1 conversation. |

The posture transform, applied to the target sheet:

| Target | Becomes | Why |
|---|---|---|
| **Surface** | VISUALISED — person's colour, engine stripe | the engine only ever showed it; that is already release 1 |
| **Engine** | VISUALISED if `RELEASE` names it, else PHASE 2 | a read or a computation over data we hold can ship; doing the work cannot |
| **Assist** | VISUALISED if `RELEASE` names it, else PHASE 2 | keeps the actor colour it already carries — an assist names whoever decides |
| **Manual / HCHB** | unchanged | hands on the patient, or still inside HCHB |
| **Ghost** | restored where `RESTORE` names it | see the editorial line below |

**Nothing is ever solid green on these sheets.** Solid green means the engine did the work, and in
release 1 it does not. A visualised block keeps the person's colour and takes the engine stripe; a
later-phase block keeps the person's colour and takes a dashed green edge plus a `PHASE 2` badge.
The horizon badge deliberately **overwrites** any posture badge inherited from the target sheet — a
block still reading `ASSIST` here would imply release-1 scope, which is the one thing these sheets
exist to deny.

**The editorial line on restored ghosts: visualisation cures invisibility, it does not cure
workload.** A step ghosted on the target sheet comes back on the visualise-only sheets when fixing
it needs automation, and stays ghosted when simply seeing the thing is the fix. So the per-discipline
assignment-task explosion, the unpaid day-before calls, the undocumented weekly logic and the ~50
daily pending-auth workflows all return, badged `STILL A STEP`; invisible pending-auth visits,
capacity read but never modelled, and plans of care ignoring payer limits stay ghosted, because
release 1 genuinely fixes those by showing them.

**`RELEASE` and `RESTORE` in `_flow_vis.py` are the editorial surface.** They are keyed on block text
exactly like the vmaps, and an unlisted engine block defaults to PHASE 2 — the conservative direction.
Re-word a block and it silently drops to PHASE 2, so re-read the sheet after any text edit.

### Cross-referencing a target sheet against its current-state twin

| Mark | Meaning |
|---|---|
| a small grey number at the block's top-left | column and position on the current-state sheet — `3.4` = column 3, fourth block; `S2` = second block on the clean-path spine |
| `NEW` | no equivalent on the current-state sheet |
| `5a` / `5b` | one current-state step that splits into two |
| `3·6` | two current-state steps that merge into one |
| a **dashed empty block** with struck-through text | **a step that no longer exists.** It keeps its old number and sits below the spine, so the main arrow visibly passes over it |

Ghosts on the SOC/ROC target sheet:

- **`1.4` PCC creates scheduling grid entry** — killed by **DE-04**: *the capacity tool replaces the
  scheduling grid; they are the same object, do not build both.* The flow routes around it.
- **`2.5` Pending-auth visits invisible — not on calendar, not counted** — killed by making pending
  visits visible. The note beneath it flips from *"the read excludes what it cannot see"* to
  *"the read now includes what is still pending."*

Ghosts on the other target sheets:

- **Episode (2T's parent):** all four *WHERE IT BROKE* items are ghosted `ADDRESSED ABOVE` — the
  per-discipline explosion, invisible pending-auth visits, the undocumented weekly logic, and
  capacity read but never modelled. No phase step is eliminated: they merge and automate in place.
- **Flow 2T — routine visits:** *Each submission generates its own assignment task* (killed by
  DE-05); the arrow from block 2 routes under the ghost straight into the DCS approval. Two of the
  four *WHERE IT BROKE* items are ghosted `FIXED BY THE ENGINE` — day-before calls as unpaid evening
  work, and the undocumented weekly logic. The other two are HCHB rules the engine cannot repeal, so
  they stay solid.
- **Flow 3T — authorization:** no step is ghosted; all four *WHERE IT BROKE* items are, as
  `ADDRESSED ABOVE`. The NO AUTH panel is retitled *the visit is pending, and visible*.
- **DCS → assignment:** the *pending auth — not on calendar, not counted* dead end below the
  auth-on-file gate.
- **Flow 5T — recert & discharge:** the *no auth → the visit sits pending* dead end, same reason.
  The band header flips to *PENDING VISITS STAY VISIBLE*.

**DCS approval survives everywhere it appears.** Laci's correction — DCS approves each discipline's
plan of care, every time, per discipline — is a real control, not a queue artefact. It is drawn
solid DCS red on 2T, 3T and the DCS/scheduler target, and it is the reason none of those sheets
ghosts the approval step itself.

### The hover layer — a sheet that answers "which variables is this?"

`_flow_live.py` turns any generator in this directory into a hoverable HTML sheet:

```
python3 _flow_live.py <generator.gen.py> <vmap-*.json> <out.html> "<Title>"
```

It runs the generator with its block helpers instrumented, so every block reports its own
geometry, then lays a **transparent hit layer** over the finished drawing. **The drawing itself is
byte-identical to the shipped sheet** — verified, not assumed — and the whole layer is
`display:none` under `@media print`, so the PDF and the printed wall sheet are unaffected. Nothing
in a generator had to change to make this work, and nothing will.

Hover shows the workbook row behind a block: ID, layer, variable name, constraint, MVP flag,
automation posture, gating flag, confidence, current-state handling, source of truth, who it is
sourced by, and the posture note. Click pins the panel, Esc clears it, and the panel flips to
whichever side of the window the block is not on.

**The mapping lives in `vmap-<flow>.json`, keyed on the block's own text** — not on coordinates,
not on an index. Two consequences worth knowing:

- **One map file drives both the current-state sheet and its target-state twin.** Because the twins
  are positional clones with mostly identical wording, `vmap-routine-visits.json` resolves 20/20
  blocks on *both* sheets. Only a block whose wording actually changed needs a second key — there is
  exactly one on Flow 2 (*Confirm with the patient — day before* → *Confirmation — clinician
  directs, engine calls*), and it is aliased to the same ID list.
- **Rewording a block silently unmaps it.** The builder prints every unmapped block by name and the
  hot-spot count, so a mismatch is loud rather than silent. Check that line after any text edit.

An empty list is meaningful: it means *deliberately mapped to nothing* — a trigger, a boundary
pill, a where-it-broke note. That is different from a missing key, which reports as unmapped.

#### Sharing it — the PDFs do not carry the pop-ups

**The shipped PDFs have nothing interactive in them, on purpose.** The hit layer is
`display:none` in print, so the wall sheet stays a wall sheet. Three ways to hand someone the
hover version, in the order they actually work:

| How | Works for | Caveat |
|---|---|---|
| **Share the artifact link** | anyone with the link, desktop or phone, nothing to install | needs a browser and the link |
| **Send the standalone `.html`** | anyone — double-click, no server, no network | ~70 KB; some mail filters strip `.html`, so zip it |
| **`--pdf` annotated PDF** | Acrobat Reader, macOS Preview | **not** Chrome/Edge's built-in viewer, **not** Google Drive's preview |

The HTML file is genuinely self-contained — the only `url()` in it is an internal SVG arrowhead
reference.

**Two output shapes, and they are not interchangeable.** The artifact host supplies its own
`<!doctype><html><head><body>`, so a page published as an artifact must stay a fragment. A file
handed to someone to open off disk must *not* be a fragment — with no doctype every browser drops
into quirks mode. `--standalone` wraps the fragment in a real document with `lang`, `charset` and a
viewport meta. Use it for anything emailed or put on a shared drive.

**Browser support.** Tested across six viewports from 1920×1080 down to 390×844, mouse and touch:
standards mode, panel opens, panel stays inside the viewport, dismiss works, no console errors. The
newest thing the page uses is `??` and `clamp()` (both 2020) and flex `gap` (Safari 14.1, 2021), so
anything from 2021 on is fine. Only Chromium could be driven here — Firefox and WebKit are not
installed in this environment — so that matrix is a Chromium result plus a feature-support audit,
not a WebKit test.

**Touch needs pointer events, not hover.** A tap fires `mouseenter` then `mouseleave` and sends no
click at all, so a hover-only binding opens the panel and shuts it in the same gesture. Binding
`click` *as well as* `pointerup` is the other trap — a tap sends both, so the pin toggles straight
back off. The page therefore pins on `pointerup` for every input type and keeps `pointerenter` /
`pointerleave` gated to `pointerType === 'mouse'`. Under 640px the panel becomes a bottom sheet so
the block being read stays visible above it. Do not reintroduce a `click` handler on `.hit`.

`--pdf` writes the mapping into an existing PDF as one invisible rect annotation per block, and
verifies the page renders pixel-identically afterwards — it prints `render identical: True` and
warns if not. Readers that support markup-annotation popups show the variables on mouse-over.
**Most of the team will be previewing in Drive, where annotations do not render at all**, so treat
the annotated PDF as a bonus for whoever opens it in Acrobat, never as the delivery mechanism.

`variables.json` is generated from `knowledge/source/workbook-2026-08-13/Variable Inventory.csv`
and holds all 76 IDs. **It is the 13 Aug inventory, not the 25 Aug build** — so the panel does not
yet carry the *Future state — the tool's role* or *who decides* columns, and the 11 IDs the build
added are absent. Regenerate it from the newer workbook before this goes in front of the team.

### ⚠️ Which sheet is "the SOC/ROC flow"

**The team's SOC/ROC flow is `Detailed-Flow-Composite` — the five-column sheet — not `Flow-SOC-Full`.**
In Drive that same file is titled **"8.18 Full SOC_ROC Flow Updated - Current State.pdf"**
([`1bv2iOHAQUbtrcnNNvMh99m8rAZ2z3evc`](https://drive.google.com/file/d/1bv2iOHAQUbtrcnNNvMh99m8rAZ2z3evc/view)),
and it is byte-identical to the repo's `Detailed-Flow-Composite.pdf` (md5 `767d603563363a91990c4685d348f29f`).
The name in Drive does not match the name in the repo. **Check the md5 before assuming which sheet
someone means** — a target-state sheet was once built against the wrong original for exactly this reason.

**`Flow-SOC-Target-State` is therefore built on `_flow-detailed-composite.gen.py`'s own geometry** —
the same five columns, the same `colw`/`BW2`/`BH2`, the same grey clean-path spine at the same `SY`,
the same feeders above and recovery below. **Every block sits where its current-state counterpart
sits**, so the two sheets overlay directly. Keep it that way: if they stop overlaying, the
cross-reference numbering is decoration.

**Where the engine touches a patient, name who released it.** Engagement is clinician-*directed*,
not clinician-*replaced*: the engine recommends, the clinician decides each day's visit order and
time window per patient, the clinician triggers the contact, and only then does the engine dial. An
automated contact with no named human trigger is a posture claim, not a design.

**The posture on every block comes from the 25 Aug variable workbook's own *Future state — the
tool's role* column**, not from judgment. That column reads Automate 34 · Assist 33 · Surface 19 ·
Stays manual 1 across 87 variables. Where a sheet and that column disagree, the column wins.

**Colour still means actor.** An Assist or Surface block keeps the colour of the person who
*decides*, taken from the workbook's *Future state — who decides* column — so the sheet answers
"who owns this when the tool cannot" without a separate legend.

### Published artifact links — update these, do not publish new ones

Republishing to the same URL keeps the link the team already has. Publishing without the URL makes
a *second* artifact and leaves the shared one stale, which is how Flow 3 ended up unpublished until
24 Aug.

| Sheet | Artifact |
|---|---|
| `Primary-Flow-Map` (*The Episode, End to End*) | https://claude.ai/code/artifact/33fa34d3-08d7-4324-b7dc-e72c7f07ef46 |
| `Flow-SOC-Full` (1) | https://claude.ai/code/artifact/e967d740-d01b-4926-8edd-abb030210b2f |
| `Flow-Routine-Visits` (2) | https://claude.ai/code/artifact/e0267da0-056d-408a-a245-e768d7c8c428 |
| `Flow-Authorization` (3) | https://claude.ai/code/artifact/cae6d954-45a0-4092-b069-a9cf5e42800c |
| `Flow-DCS-Scheduler` | https://claude.ai/code/artifact/936c2f7b-ef3a-4154-8a7c-806818c21520 |
| `Flow-Recert-Discharge` (5) | https://claude.ai/code/artifact/0c51c8e8-1452-4ddc-969f-748b803de981 |
| `Flow-SOC-Target-State` (1T) | https://claude.ai/code/artifact/ce6afec9-2e56-4aa6-b576-9b16b02fc5d0 |
| `Episode-Target-State` | https://claude.ai/code/artifact/59f82f31-3bde-4bf9-8924-1c2031159733 |
| `Flow-Routine-Visits-Target-State` (2T) | https://claude.ai/code/artifact/87286bfb-2f0b-4d74-b73e-01192c6b38f8 |
| `Flow-Authorization-Target-State` (3T) | https://claude.ai/code/artifact/1cc1f3f9-1135-45e3-bd0d-c5dd03211736 |
| `Flow-DCS-Scheduler-Target-State` | https://claude.ai/code/artifact/012cd1d4-d29e-482b-9fde-e44857e8b8b7 |
| `Flow-Recert-Discharge-Target-State` (5T) | https://claude.ai/code/artifact/4f47bc53-2d30-4f2d-a510-1b8bb272fe5f |
| `flow-routine-visits-target-live` (hover proof, 2T) | https://claude.ai/code/artifact/dfa141e2-865f-4add-9866-f763c9b5f6e5 |
| `flow-routine-visits-live` (hover proof, current state) | https://claude.ai/code/artifact/7edc53bb-f5cc-4f4c-bf78-d0dd62050043 |
| `Detailed-Flow-Composite` (the SOC/ROC sheet) | https://claude.ai/code/artifact/e648db98-7ce3-4f5a-9a9a-aa98c559b107 |

`Flow-Payer-Economics` has no recorded link yet — check `/artifacts`
before publishing one, and add the URL here when you do.

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
