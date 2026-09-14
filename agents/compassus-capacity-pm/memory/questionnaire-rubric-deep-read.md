# Questionnaire and rubric — deep read

What was learned from reading the blank questionnaire cell by cell and the two rubric versions side
by side. The per-question reading guide, the exact rubric and the calibration examples live in the
handoff pack (`vendor-evaluation/handoff/` files 02, 03, 04, 09); this file holds what is not
there.

---

## 1. The form's structure

File: `Compassus_Capacity__Scheduling_Vendor_Questionnaire_2.xlsx`, form_version 2026-08-19,
audience internal, issued by Compassus Home Health. Sheets: Overview (visible), Questionnaire
(visible), Current State Flow Map (visible, empty), Lists (hidden), Meta (hidden).

- Meta lists seventeen question ids: A1–A3, C1–C7, D1–D3, E1–E4. Section B is an eleven-row matrix,
  not a question id.
- Question id in column B, text in column C (bold title, newline, body), answer in merged D:G on
  the same row. Vendor in D4, completed-by in D5. Column headers repeat at rows 8, 35, 53, 62.
- Section B occupies rows 19–32: arena bands at B19, B23, B28; area rows 20–22, 24–27, 29–32; answer
  columns D In scope, E Status, F How it's done, G Notes.
- Dropdowns via defined names: `InScopeList` (Yes · Through a partner · No · Other — see notes);
  `StatusList` (Production — multiple customers · Production — one customer · In development —
  target date in notes · Roadmap — no date yet · Other — see notes); `CapacityInputList` for areas
  1–3 (Live feed from a source system · Imported on a schedule · Maintained by staff in your
  product · Entered by the clinician · Derived from FT/PT allocation · Other — see notes);
  `DeliveryList` for areas 4–11 (Automated end to end · Automated, person approves · System
  prepares it, person does it · Person does it · Other — see notes).
- The asymmetry: for Capacity areas, *how it's done* asks where the data comes from; for the other
  eight, how much of the work is automated. A delivery value on a capacity row means the cell was
  typed over. `DeliveryList` maps almost one to one onto the Sophistication ladder.
- The Overview carries a 42nd bullet with no group: *"The staff time coordination consumes today."*
  It is not in `spec-elements.json` and not scored anywhere.
- Section D carries a preamble: *"Scheduling in home health is operationally critical and personally
  consequential. Many clinicians come to home health for the control it gives them … In our
  experience adoption, more than algorithm quality, decides whether tools like this succeed."*

## 2. Two rubrics, compared

| | v3.0 — `_scorecard.gen.py`, the workbook, the one-pager | v1.0 — `scoring-guide.md`, `vendor-scorecard` skill, `score.py`, Meridian example |
|---|---|---|
| Shape | 7 weighted section grades, 20/12/12/12/20/12/12 | 5 parts, 25/30/20/10/15 |
| Scope | 3 marks of 0–4 per arena from Section B | 41 elements marked covered / partial / none |
| HCHB | 6 rungs, top 20 | 6 rungs, top 25 |
| Sophistication | one mark 0–4 | five marks S1–S5 from C1, C2, C4, C3, C5 |
| Clinician | one mark, undescribed | three marks D1–D3, ÷12 ×10 |
| Partnership | one mark, equity at the top | four marks P1–P4, ÷16 ×15 |
| Conditional | HCHB grade under 60% | Part 1 under 12 |
| Unscored | 3 flags, 5 intangibles, 3 notes rows | differentiators, flags, unknowns |

The workbook and the pack are v3.0. The v1.0 material is still useful for its reading discipline:
cite or don't score; an unanswered question is a zero on the unknowns list, never a charitable
guess; ambiguous HCHB answer takes the lower rung plus a flag, never an average; never invent a
citation; say when a low score looks like a writing problem rather than a product one; a low
footprint is not automatically a loss; anything on five vendors' lists is not a differentiator.

`vendor-evaluation/README.md` once pointed at files that do not exist (`Vendor-Scorecard-SIMPLE.xlsx`,
`_simple-scorecard.gen.py`, `_options-onepager.gen.py`); it now carries a banner naming v3.0 and
the handoff pack. `Vendor-Scoring-Options.pdf` is at the repo root.

## 3. The maths, exactly

- HCHB grade: `VLOOKUP(rung, Lists!$B$2:$C$7, 2, FALSE) / 20`.
- Arena grade: `(VALUE(LEFT(m1,1)) + VALUE(LEFT(m2,1)) + VALUE(LEFT(m3,1))) / 12`.
- Sophistication, clinician fit, partnership: `VALUE(LEFT(m,1)) / 4`.
- Total: Σ grade × `'Start Here'!$C$row`.
- Band: `IF(NOT(HCHB ≥ 0.6), "Conditional — ", "") & IF(total ≥ 80, "Advance", IF(≥ 65, "Consider",
  IF(≥ 50, "Hold", "Decline")))`. Live through a partner is exactly 0.6 and passes.
- Stop-checks: count of A2, A3, C6 equal to `STOP-CHECK`.
- Everything gated on A1 being non-blank.

## 4. Vendor archetypes

The three fictional examples are three corners of the rubric.

**Arbor Health Logistics, the credible operator thin on the new part.** Live established HCHB;
Capacity 4/3/4; Scheduling 4/4/3; Engagement 2/2/1; Sophistication 4; Clinician 3; Partnership 3;
A3 Watch; three Strongs and a Neutral. The strength is consistent across sections and the weakness
is declared. The trap is rounding Engagement up because the mechanics are so good. The open question
is ownership, which they never raised: *"E2 was the shortest answer they gave."*

**Wayfinder Scheduling, the logistics product that found a vertical.** HCHB live small base, but
the evidence contradicts the rung (nightly file drop); Capacity 2/1/1; Scheduling 3/4/2; Engagement
1/1/0; Sophistication 3; Clinician 2; Partnership 2; A2 STOP-CHECK; three Concerns. Routing is
genuinely excellent because it transfers from another industry. Section B claims all eleven areas
and Section C supports four. The B-versus-C gap is the diagnostic, and it matters because thirty-six
points ride on the vendor's own self-assessment.

**Northlight Health, honest, ahead on engagement, not yet live.** In development with a date, so
Conditional whatever the total; Capacity 2/2/3; Scheduling 3/3/3; Engagement 3/4/2; Sophistication
3; Clinician 3; Partnership 4 (the only 4); C6 Watch; three Strongs and a Concern on durability.
This is the vendor the total will misrank. *"Let them contradict the number if that is what you
see."*

## 5. Cross-question patterns

1. **The B-versus-C gap.** Areas claimed minus areas C evidences. Report as a count.
2. **Where the language changes.** Which sections read like a mechanism and which like a brochure.
3. **The claims-everything vendor.** Zero *No* in B, zero admitted gaps in C, *nothing* in E4.
4. **The unanswered half.** C7's conflict rule, D1's disagreement loop, D2's configurability, D3's
   clinician view, C5's *when nobody takes it*, C6's *what they can do while it lasts*, A1's sync
   latency, E2's structure. Which half they skipped is more diagnostic than what they wrote.
5. **Scale coherence.** A1 customers, A2 customers, A3 sites, D3 six-month data, E3 named
   deployments must reconcile.
6. **Posture coherence.** C1/C2 sophistication, D2 stated posture, D1 control surface, E3 resistance
   outcome must describe one product.
7. **The Conditional–Partnership inversion.** Not-yet-live vendors are systematically the ones most
   willing to talk about equity, because that is what they have to trade. Expect it; let it read as
   neither a discount nor a bonus.

## 6. The voice

From the examples. Lead with the specific; put claim and evidence side by side; end a doubtful note
with what to do; sign a read with initials; comparative framing where it exists; never restate the
score.

- *"Live since Mar 2024, four HCHB customers, published API both ways. Says HCHB is authoritative
  for orders, they own assignment. CLAIM: bi-directional. EVIDENCE: named the conflict rule, which
  is the hard part — believable."*
- *"One customer, live 8 months. CLAIM: full integration. EVIDENCE: describes a nightly file drop.
  That is not the same thing — ask."*
- *"14% mileage reduction — one site, nine months. CLAIM is big, EVIDENCE is thin. Ask."*
- *"Constraint solver, named weights, shows envelope impact before a referral is accepted. Only
  answer that does this."*
- *"Marked all eleven areas in scope, then Section C covered four of them."*
- *"Volunteered that their capacity model is weaker than their engagement side. Cost them points
  and they said it anyway."*
- *"C5 reads like someone who has been paged at 2am. Named their escalation ladder without being
  asked."*
- *"Coverage offer with a measured median time-to-fill — 4 minutes — rather than a described
  workflow."*
- *"All patient outreach is staff-initiated — the coordinator labour we are trying to remove stays."*
- *"Make them walk the HCHB integration live. A nightly file drop is not what they said."*
- *"What exactly is committed on the Q2 2027 date, and by whom? Get it in writing."*
- *"Impact figures come from one site. Engagement is genuinely thin, not modest."*

## 7. What the rubric deliberately does not do

1. **Penalise brevity.** *"Score the product, not how much the vendor wrote about it. How it does
   something is a demo question, not a reason to mark it down."* *"A three-sentence answer saying
   the engine optimises across drive time, continuity and capacity together is a 4."*
2. **Prescribe what earns a 4 on clinician fit.** *"No descriptions on purpose … we know how our
   clinicians work and what they will accept."*
3. **Let sophistication become product quality, or treat 4 as the goal.** *"Where we set an Assist
   boundary, a product that decides on its own is a risk to note."*
4. **Trade flags for points.** *"A stop-check is resolved before advancing, not traded against
   points."* *"A vendor can score well and still carry one."*
5. **Give intangibles points, or expect them to agree.** *"If this section never disagrees with the
   numbers, it is not doing anything."* The room test is blank until after the demo.
6. **Treat the total as the decision.** *"The total is a sort key … it is not the decision."* When
   two vendors tie, say which arena each owns.
7. **Over-rely on Claude.** *"Use it to do the first pass and to check your own — not to replace
   the read."* Every highlight carries a question id and the vendor's words.
8. **Score a product.** *"This scores a questionnaire, not a product … it is designed to pick who
   gets those, and nothing more."*
9. **Treat low footprint as a loss.** *"41 elements is our spec, not the market's."*
10. **See price.** Commercials enter after the shortlist.
11. **Keep commonplace differentiators.** *"Anything that appears on five vendors' lists is not a
    differentiator. Cut it."*
12. **Treat Conditional as elimination.** *"They can still advance — but only on an explicit
    decision that names what we are accepting."*
13. **Assume the rubric is right.** *"The field will teach us where it is wrong; that feedback is
    worth more than a tidy total."*
