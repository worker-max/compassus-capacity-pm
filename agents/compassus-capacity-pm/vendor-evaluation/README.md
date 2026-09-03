# Vendor Evaluation

Scoring the returned **Capacity & Scheduling** vendor questionnaires — 16 vendors down to a
shortlist, on evidence rather than impression.

## Two workbooks

| | | |
|---|---|---|
| [`Vendor-Scorecard.xlsx`](./Vendor-Scorecard.xlsx) | **The scorecard.** Five parts, 100 points, 41 spec elements. | ~10 min a vendor |
| [`Vendor-Scorecard-SIMPLE.xlsx`](./Vendor-Scorecard-SIMPLE.xlsx) | **The backup.** 12 rows a vendor, two marks each. | ~3 min a vendor |

**Both are self-contained** — the first tab of each carries the why, the what, the how, and the
full legend for every dropdown. Nothing else needs to be read first, and there is no second
document to keep in sync.

Use the full scorecard when the shortlist is close and you have to defend the order. Use the
backup for a fast read across the field, or when the full sheet is more precision than a decision
needs.

## The full scorecard

Every part is a percentage times the points it is worth — and the sheet does that maths, not you.
One exception, deliberately: **HCHB integration is a checkbox ladder**, so the priority leadership
named cannot drift as scorers tire.

| Part | Points | From |
|---|---:|---|
| 1 · HCHB Integration | 25 | A1 — one rung, ticked |
| 2 · Scope Footprint | 30 | The 41 elements on the Overview tab, 10 points per arena |
| 3 · Sophistication | 20 | Section C, plus A2/A3 |
| 4 · Clinician & Adoption | 10 | Section D |
| 5 · Partnership | 15 | Section E |

Alongside the number, three lists that carry what a score cannot: **differentiators**, **flags**,
**unknowns**.

## The backup

Follows the shape of the **Functional Scorecard** in the primary workbook — Status, Rating,
Comments, with Footprint and Coverage rolling up — so it reads like something the team has seen
before. It scores the 11 areas the vendor already self-assessed in Section B, plus HCHB.

- **Status** — what they have. Copy it from their own Section B answer; Section C wins where they differ.
- **Rating 0–100** — how good it is. 90+ proven with numbers · 70+ mechanism explained · 50+ described · 25+ asserted.
- **Notes** — what stands out, what worries you, what you could not tell.

Rolls up to footprint %, in-production %, an average rating, and a rating per arena.

It has no partnership or clinician-adoption score, so Sections D and E do not reach the number —
read them and put what matters in Notes.

## Everything else here

| Path | What it is |
|---|---|
| [`Vendor-Scoring-Options.pdf`](./Vendor-Scoring-Options.pdf) | One portrait page for leadership — option one and option two, process and rationale each. Not a working document. |
| [`example/`](./example/) | A fully worked scorecard, so the shape is obvious before the first real return arrives. |
| [`verify-agreement.py`](./verify-agreement.py) | Proves the workbook and the scoring engine compute the same score. |
| [`scoring-guide.md`](./scoring-guide.md) | The rubric in prose — what the `/vendor-scorecard` skill scores against. Not a hand-out; the workbook's first tab is. |
| `_scorecard-workbook.gen.py` · `_simple-scorecard.gen.py` · `_options-onepager.gen.py` | The generators. Regenerate rather than hand-edit — a hand edit is lost on the next run. |

The 41 spec elements live in
[`.claude/skills/vendor-scorecard/assets/spec-elements.json`](../../../.claude/skills/vendor-scorecard/assets/spec-elements.json),
extracted from the questionnaire's Overview tab. Everything derives from that one file.

## The skill

`/vendor-scorecard` — hand Claude a returned questionnaire and it produces the deep dive, the
summary, the footprint percentages and a full scorecard in this rubric, with every mark cited back
to a sentence the vendor wrote. Use it for the first pass and to check your own, not to replace the
read.

The skill and the workbook agree exactly. `verify-agreement.py` evaluates the workbook's real
formulas and compares them part by part — run it after touching either.

## The rules that keep it honest

1. **Section B is their claim; Section C is the evidence.** A claim with no mechanism is a partial.
2. **Cite or don't score.** An uncited *covered* is demoted to *partial*, and the scorecard says so.
3. **An unanswered question is a zero** and goes on the unknowns list — never a charitable guess.
4. **Ambiguous HCHB answer → the lower rung**, plus a flag. Never average.
5. **This scores a questionnaire, not a product.** It decides who gets a demo, and nothing more.

## First run

Score the first three vendors **twice, independently**, then compare and argue. Write down what you
decided — those become house rules, and the remaining thirteen go faster and straighter for them.

---

*Rubric v1.0 · questionnaire form_version 2026-08-19.*
