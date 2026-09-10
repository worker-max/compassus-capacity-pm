# 03 · The scorecard, exactly

This is the rubric the workbook `Vendor-Scorecard.xlsx` enforces. It is generated from the same code that builds the workbook, so if the two ever disagree, the workbook has moved and this pack is stale — stop and say so.

## The shape

Every question has a row, in questionnaire order. Thirteen rows take a mark. Three raise a flag instead of moving the score. Five are intangibles and carry no points. Each vendor has a mark column and a wide notes column; the notes are one merged cell per section.

**Section grade = marks earned ÷ marks available**, shown as a percentage. **Total = each section grade × its weight, added up.** The weights live on the Start Here tab and can be changed in the working session; the total is a sort key, not the decision.

| Section | Default weight | Graded from |
|---|---:|---|
| Home Care Home Base | 20 | A1 — one rung of six |
| Capacity | 12 | Section B — three marks of 0–4 |
| Scheduling | 12 | Section B — three marks of 0–4 |
| Engagement | 12 | Section B — three marks of 0–4 |
| Sophistication | 20 | Section C — one mark of 0–4 |
| Clinician fit | 12 | D1–D3 — one mark of 0–4 |
| Partnership | 12 | E1–E4 — one mark of 0–4 |
| **Total** | **100** | keep at 100 and the total stays out of 100 |

## A1 · Home Care Home Base — pick one line

Three of the six rungs are live integrations, because live through a partner is still live. Anything not yet live shows as **Conditional** on the band, whatever the total. Ambiguous answer: take the lower rung and say why in the notes.

| Points | Rung |
|---:|---|
| 20 | Live — established customer base |
| 16 | Live — small customer base |
| 12 | Live — through a partner |
| 6 | In development — with a date |
| 2 | On the roadmap — no date |
| 0 | None, and no path to one |

## Section B · Scope — three marks per arena, 0 to 4

Each row names the area and what sits inside it. Where Section C contradicts Section B, believe Section C. Capacity's three areas map one to one; Scheduling and Engagement have four apiece, so the two that belong together are paired.

| Mark | Meaning |
|---|---|
| 4 | Most of it |
| 3 | More than half |
| 2 | About half |
| 1 | A corner of it |
| 0 | Nothing here |

| Row | Area | What it covers | From |
|---|---|---|---|
| CAP1 | Workforce supply | Roster, disciplines, roles, competencies, ramp, float pool | B1 |
| CAP2 | Availability & reach | Availability and time off, territory, drive-time reachability | B2 |
| CAP3 | The capacity math | Visit weighting, targets and ceilings, committed load vs. open room | B3 |
| SCH1 | Demand & matching | Ordered visits, authorization, readiness — and who fits them | B4 + B5 |
| SCH2 | Routing & the week | Routing, sequencing, front-loading, week balancing | B6 |
| SCH3 | Exceptions | Missed visits, call-outs, reassignment, coverage, rebooking | B7 |
| ENG1 | Before the visit | Welcome call, availability capture, reminders, confirmation, en-route | B8 |
| ENG2 | When plans change | Reschedule, coverage outreach, urgent same-day needs, incentives | B9 + B10 |
| ENG3 | Across the care team | Multi-discipline coordination, clinician and office updates | B11 |

## Section C · Sophistication — one mark, 0 to 4

How much of the work the product does — Read / Assist / Control. Score what the product does, not how much the vendor wrote about it. How it does something is a demo question, not a reason to mark it down. A 4 is not automatically what we want: where we set an assist boundary, a product that decides on its own is an overreach to flag.

| Mark | Meaning |
|---|---|
| 4 | Runs it — decides across the whole picture, and re-decides when things change |
| 3 | Recommends it — works out the answer and proposes it; a person confirms |
| 2 | Checks it — applies rules and flags problems; a person still works it |
| 1 | Shows it — surfaces the information; a person does all the work |
| 0 | Not addressed |

## Section D · Clinician fit — one mark, 0 to 4

No descriptions on purpose. The team reads D1 to D3 and gives it their own read — they know how Compassus clinicians work and what they will accept. **The reading Claude supplies the evidence for this row and never the mark.**

| Mark | Label |
|---|---|
| 4 | Strong fit |
| 3 | Good fit |
| 2 | Workable |
| 1 | Poor fit |
| 0 | Not answered |

## Section E · Partnership — one mark, 0 to 4

A company with the willingness and the environment to build this around our needs, and open to us holding equity so a product for the general market becomes possible. Read all four E answers, not only E2. A discount is a discount.

| Mark | Meaning |
|---|---|
| 4 | Open to equity or a stake in what we build, and set up to build it with us |
| 3 | Ready to build to our needs as a design partner; ownership not addressed |
| 2 | Will take our input, but they own the roadmap and the product |
| 1 | A standard customer relationship — we buy what already exists |
| 0 | Not answered |

## The three that raise a flag instead

`OK` · `Watch` · `STOP-CHECK`. A stop-check is resolved before advancing, not traded against points. A vendor can score well and still carry one.

| Question | Trigger |
|---|---|
| A2 Customers, scale and references | Stop-check if one customer, or no references offered |
| A3 Measured impact | Watch if claimed with no baseline or period |
| C6 When your product is down | Stop-check if no uptime figure or contractual commitment |

## The five intangibles — no points, and allowed to disagree with the score

`Strong` · `Neutral` · `Concern`, with the reason and initials in the notes. Filled after the scored sections. If this section never disagrees with the numbers, it is not doing anything. **The reading Claude supplies evidence for these and never the read.**

| Intangible | The prompt on the sheet |
|---|---|
| Home health fluency | Do these read like people who have stood in a branch? Unprompted vocabulary, problems they raise that we did not ask about. |
| Candor about gaps | Did they say 'we don't do that' anywhere? A vendor who claims everything has told us something. |
| Who wrote this | Marketing, sales engineer, or someone who built it. Specificity, and willingness to name a constraint. |
| Durability | Will they exist in three years, and will this still be their main business? Are we uncomfortably their largest customer? |
| The room test | Would we want these people in our building for two years? Leave blank until after the demo — on purpose. |

The room test is left blank until after the demo, on purpose. A document-only reader cannot fill it.

## Bands

| Total | Band |
|---|---|
| 80–100 | Advance |
| 65–79 | Consider |
| 50–64 | Hold |
| under 50 | Decline |
| any | **Conditional —** prefixed whenever the Home Care Home Base grade is below 60%, i.e. any rung below *Live — through a partner* |

Conditional is not elimination. A Conditional vendor can still advance, on an explicit decision that names what is being accepted: an integration to be built, on their timeline, at our risk.

## The notes

One merged note cell per vendor for each of: Section A, Capacity, Scheduling, Engagement, Section C, Section D, Section E, the five intangibles, plus one beside the total and one beside the section grades. Notes are written as `QUESTION-ID: note`, one per line, in the claim-versus-evidence voice shown in `09-CALIBRATION.md`.

Three full-width rows close each vendor: **What stands out** (against the field, or against our own thinking) · **What worries me** (including anything flagged above) · **What to go and ask** (the demo agenda).

## The Questions tab

Twenty vendor columns. Six sections — A, B, C, D, E, Intangibles — with three slots each, for what we make each vendor prove at the demo. The Section B hint is the sharpest instruction on the tab: *anything claimed in scope that Section C did not support.*

---
*Scorecard v3.0 · questionnaire form_version 2026-08-19 · generated from `_scorecard.gen.py` at `fd651c5`*
