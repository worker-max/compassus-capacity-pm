# Artifacts — Capacity, Scheduling & Engagement

> **Start here if you are a new session.** This folder holds the working artifacts for the capacity
> and scheduling model. The three-arena model below is the current shared framing; the documents in
> this folder are all views onto it at different depths.

## The model in one paragraph

**Capacity** is the envelope — how much work a branch can deliver, given people, hours, disciplines
and territory, netted against what is already booked. **Scheduling** fills that envelope: which
clinician, which day, which route. **Engagement** defends it: the confirmation, coverage and
rebooking work that turns a schedule into delivered visits. Scheduling and Engagement are grouped
inside a shaded **Coordination** zone, because both are activities performed *against* the envelope
rather than parts of it. Only a completed visit becomes revenue; a discharge hands room back to
capacity.

## Source of truth

| | |
|---|---|
| **Primary workbook** | `Compassus Capacity & Scheduling Workbook 2026-08-11.xlsx` — Google Drive `15rus_8HKOoXkeZmEBvEP51TCNuu_sOzf` |
| Tabs that drive these documents | `The Concepts That Matter` (the 15-factor distillation → prominence) and `Variable Inventory` (76 scored variables → priority) |
| Data-model workbook | `Clinician-Capacity-Tool_Data-Index.xlsx` — Drive `1BFxo6k3tSDyoJZxmm7_gFxmnuEm4S_fW` |
| Drive folder | `1WEf_6FN7963y-MGwP3S3GaaPvqJ2RNF3` |
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
| `capacity-scheduling-board.html` | 4 pages — the three boxes, then every variable per box | The working list |
| `capacity-scheduling-diagram.html` | Flow figure, sketch-to-model mapping, and per-variable detail (constraint, MVP, posture, current state) | The reference / supporting document |
| `capacity-tool-data-index.md` | Full capacity-vision data dictionary (domains A–J) | Field-level data planning |
| `capacity-tool-mockup-data-spec.md` | The built tool's actual data model + as-built review | What exists today |
| `capacity-ecosystem-map.md` | Coverage scan — the structural gaps (1A readiness, 1B economics, 1C quality) | What the model still cannot see |
| `source-war-list-worksheet.{md,csv}` | Where each data element actually comes from | Source war-listing sessions |

**Editing rule:** the one-pager, the board and the diagram carry the same variable set at three
depths. Change one, change all three, or they drift.

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

1. **Engagement vs. Coordination naming.** The workbook uses *Coordination* for the `CO-` layer.
   In these documents that layer is drawn as **Engagement**, and *Coordination* names the shaded
   zone holding both Scheduling and Engagement. Variable codes are unchanged.
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

## Open items

- **`S-43` / `S-44` are proposed here, not yet in the workbook.** They need adding to the
  `Variable Inventory` tab to flow through the `Functional Scorecard`, which is what vendor scoring
  reads from. Until then the workbook says 76 variables and these documents say 78.
- **The *Readiness* group is deliberately near-empty.** Authorization holds, plan-of-care locks and
  face-to-face / coding holds are the same "stuck before it is schedulable" family and would land
  there. This is ecosystem gap **1A**, the largest structural blind spot in the model. Not added
  without a decision.
- **Three further net-new items from the sketch have no variable behind them:** traffic and physical
  obstructions (bridges — routing is mileage and straight-line proximity today, not drive-time), the
  shift/visit-finder incentive surface, and the hand-off / accept-decline loop.
- **Counts to keep in sync when variables change:** one-pager and board box footers, board page
  headings ("All 22 / 44 / 12 variables"), and the diagram's provenance line.

## Related

- [`../knowledge/README.md`](../knowledge/README.md) — the ten load-bearing discovery findings
- [`../MASTER-capacity-and-scheduling.md`](../MASTER-capacity-and-scheduling.md) — the assembled master document
- [`../AGENT.md`](../AGENT.md) — the PM agent definition
