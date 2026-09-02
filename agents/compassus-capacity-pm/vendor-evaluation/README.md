# Vendor Evaluation

Scoring the returned **Capacity & Scheduling** vendor questionnaires — 16 vendors down to a
shortlist, on evidence rather than impression.

## The model

**Every part of the score is a percentage times a budget.** Score the items, take the percentage,
multiply by the points that part is worth. One exception, deliberately: **HCHB integration is a
checkbox ladder, not a judgement** — that is how the leadership priority is protected from scoring
drift.

| # | Part | Points | From |
|---|---|---:|---|
| 1 | HCHB Integration | 25 | A1 — one rung, ticked |
| 2 | Scope Footprint | 30 | The 41 elements on the Overview tab, 10 points per arena |
| 3 | Sophistication | 20 | Section C, plus A2/A3 |
| 4 | Clinician & Adoption | 10 | Section D |
| 5 | Partnership | 15 | Section E |

Alongside the number, three lists that carry what a score cannot: **differentiators**, **flags**,
and **unknowns**.

## What's here

| Path | What it is |
|---|---|
| [`scoring-guide.md`](./scoring-guide.md) | **The rubric — the source of truth.** Read this first. |
| [`Vendor-Scoring-Guide.pdf`](./Vendor-Scoring-Guide.pdf) | The same rubric on one landscape page, for the leadership conversation. |
| [`Vendor-Scorecard.xlsx`](./Vendor-Scorecard.xlsx) | The sheet you score on. One tab, 16 vendors side by side, dropdowns and live formulas. |
| [`example/`](./example/) | A fully worked scorecard, so the shape is obvious before the first real return arrives. |
| [`verify-agreement.py`](./verify-agreement.py) | Proves the workbook and the scoring engine compute the same score. |
| `_scorecard-workbook.gen.py` · `_scoring-guide-sheet.gen.py` | The generators. Regenerate rather than hand-edit — a hand edit is lost on the next run. |

The 41 spec elements live in
[`.claude/skills/vendor-scorecard/assets/spec-elements.json`](../../../.claude/skills/vendor-scorecard/assets/spec-elements.json),
extracted from the questionnaire's Overview tab. Everything derives from that one file.

## Two ways to score

**By hand.** Open `Vendor-Scorecard.xlsx`, pick a vendor column, work the dropdowns top to bottom.
Roughly ten minutes a vendor once you have the rhythm. The summary block at the top stays visible
while you score.

**With the skill.** `/vendor-scorecard` — hand Claude the returned file and it produces the deep
dive, the summary, the footprint percentages and a full scorecard in this rubric, with every mark
cited back to a sentence the vendor wrote. Use it for the first pass and to check your own, not to
replace the read.

The two agree exactly. `verify-agreement.py` evaluates the workbook's real formulas and compares
them to the engine, part by part — run it after touching either.

## Footprint

The Overview tab specifies **41 elements**. A vendor's footprint is how many of them they cover:

| Arena | Elements | Budget |
|---|---:|---:|
| Capacity Management | 11 | 10 |
| Scheduling Engine | 14 | 10 |
| Engagement | 16 | 10 |

Equal budgets, unequal element counts — on purpose, so a vendor who owns scheduling completely and
skips engagement cannot tie one who covers all three shallowly. Every scorecard reports the three
percentages separately, because **which** arena a vendor owns tells us more than the total does.

## The rules that keep it honest

1. **Section B is their claim; Section C is the evidence.** A claim with no mechanism is a partial.
2. **Cite or don't score.** An uncited *covered* is automatically demoted to *partial*, and the
   scorecard says so.
3. **An unanswered question is a zero** and goes on the unknowns list — never a charitable guess.
4. **Ambiguous HCHB answer → the lower rung**, plus a flag. Never average.
5. **This scores a questionnaire, not a product.** It decides who gets a demo, and nothing more.

## First run

Score the first three vendors **twice, independently**, then compare and argue. Write down what you
decided — those decisions become house rules, and the remaining thirteen go faster and straighter
for them.

---

*Rubric v1.0 · questionnaire form_version 2026-08-19.*
