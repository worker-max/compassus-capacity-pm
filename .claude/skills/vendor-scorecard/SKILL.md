---
name: vendor-scorecard
description: Deep-dive, score and summarise a returned Compassus Capacity & Scheduling vendor questionnaire. Produces a footprint percentage against the 41-element spec (overall and per arena — capacity, scheduling, engagement), a five-part score out of 100, a differentiator list, flags and unknowns. Use when a vendor questionnaire, RFP response or completed workbook comes back and needs analysing, scoring, comparing or shortlisting.
---

# Vendor scorecard

Score a returned questionnaire against the Compassus rubric — **auditably**, so every mark can be
traced back to a sentence the vendor wrote.

The rubric is [`vendor-evaluation/scoring-guide.md`](../../../agents/compassus-capacity-pm/vendor-evaluation/scoring-guide.md).
**Read it before scoring.** This file is the procedure; that file is the law.

## The shape of the job

```
returned .xlsx  →  extract answers  →  score with citations  →  assessment JSON
                                                                      ↓
                          scorecard .md  ←  assets/score.py  →  workbook column
```

`score.py` owns all arithmetic. Never compute a total by hand — the point of the script is that
the sheet, the skill and the guide cannot drift apart.

## 1 · Extract

The questionnaire has five sections. Pull every answer into a working file before scoring anything.

```python
import openpyxl
wb = openpyxl.load_workbook(path, data_only=True)
ws = wb["Questionnaire"]
for r in ws.iter_rows():
    for c in r:
        if c.value not in (None, ""):
            print(c.coordinate, repr(c.value)[:400])
```

| Where | What it holds |
|---|---|
| `Questionnaire` C-column | The questions (A1–A3, C1–C7, D1–D3, E1–E4) |
| `Questionnaire` D-column | **Their free-text answers**, on the row below each question |
| `Questionnaire` D:G rows 20–32 | The Section B self-assessment — *In scope · Status · How it's done · Notes* for 11 areas |
| `Overview` | Our spec. Already extracted to `assets/spec-elements.json` — 41 elements |
| `Meta` B4 | The question IDs, so you can check nothing is missing |

Vendors return these in every possible state: merged cells, answers in the wrong row, a Word
document attached instead. **If Section B is blank but Section C is rich, score from C and say so.**
If an answer is missing entirely, that is a `0` and an entry on the unknowns list — never a
charitable guess.

## 2 · Read before you score

Read the whole return once without scoring. You are looking for three things a rubric cannot see:

- **What they lead with.** The first thing a vendor explains is what they think they are.
- **Where the language changes.** Marketing prose in Section C and specifics in Section E usually
  means the product is thinner than the pitch. The reverse means an engineer wrote it, and those
  are the good ones.
- **What they raised that we did not ask.** E1 and E4 are the highest-signal answers on the form.
  This is where "factors at play we haven't considered" actually live.

## 3 · Score

Copy `assets/assessment-template.json` and fill it in. It is pre-populated with all 41 element ids
in sheet order.

**Part 1 — HCHB.** Set `hchb.rung` to one of `25 / 20 / 12 / 6 / 2 / 0` and quote the sentence you
picked it from in `note`. Ambiguous answer → take the lower rung and add a flag. A1 also asks how
they handle data changing on both sides; silence there does not change the rung, but it is a
yellow flag — two systems that both believe they own the schedule is the failure mode that
hurts most.

**Part 2 — Footprint.** For each of the 41 elements set `mark` to `covered` / `partial` / `none`,
plus a `cite` (question id) and a short `quote` in their words.

> **The rule that keeps this honest: cite or don't score.** `score.py` silently demotes an uncited
> `covered` to `partial` and marks it on the scorecard. Do not fight it — find the citation or
> accept the partial. Section B is their *claim*; Section C is the *evidence*. B says "automated
> end to end" and no C answer describes the mechanism → **partial**.

Also partial, always: "configurable", an open API, a partner delivering it, a dated roadmap item,
and any claim with no supporting detail.

`ENG-01` and `ENG-02` have no Section B area — score them from **C7** and **D1**.

**Parts 3–5 — the evidence ladder.** Twelve items, each `0–4`:

| | |
|---:|---|
| 0 | Not addressed — skipped, or answered without answering |
| 1 | Asserted — they say they do it, nothing behind it |
| 2 | Described — we can picture the feature |
| 3 | Mechanism — we can picture *how it decides*: inputs, logic, configuration |
| 4 | Proven — mechanism **plus** evidence: numbers, a named customer, a period, a baseline |

The gap between 2 and 3 is the one that matters, and it is where most of the discrimination in this
rubric lives. "We optimise routes" is a 2. "We minimise drive time subject to compliance windows
and continuity weights, all of which are configurable per branch" is a 3. The same sentence with
*"cut mileage 14% across 22 branches over nine months against a pre-deployment baseline"* is a 4.

Put your reasoning in each item's `note` — one sentence. That note is what a colleague reads when
they disagree with you, so make it the *reason*, not a restatement of the score.

## 4 · The three unscored lists

These decide more conversations than the total does. Do not skimp on them.

**`differentiators`** — 3–5 lines, each one line. Two kinds count: *against the field* (something
nobody else showed) and *against our thinking* (something not on our one-pager that probably should
be). If it would appear on five vendors' lists, cut it. Cite the question.

**`flags`** — `{"level": "red"|"yellow", "text": "..."}`. Red is a stop-check: no HCHB path; no
uptime or contractual commitment (C6); the system decides and the clinician cannot override (D1);
one customer or no references (A2); core scope from an unnamed third party. Yellow is a watch:
home health a minority of their business; impact with no baseline; marketing language where a
mechanism belongs; brittle integration method; silence on sync latency.

**`unknowns`** — what you could not score because they did not answer. This becomes the demo
agenda, so write each one as a question you would actually ask.

**`summary`** — two to four sentences. What the product is, who it is for, and the single thing
that decides whether it fits Compassus. Write it last, after scoring; write it as a person who has
read the whole thing, not as a précis of the numbers.

## 5 · Produce

```bash
S=.claude/skills/vendor-scorecard/assets
python3 $S/score.py assess/<vendor>.json -o <Vendor>-Scorecard.md
python3 $S/score.py assess/*.json --roster Vendor-Comparison.md     # across the field
```

The scorecard carries the band, the five parts, the footprint percentages (overall and per arena),
the full 41-element table with citations, the ladder items with your reasoning, and the three lists.

**Then report to the operator in the chat** — do not just point at the file:

1. The headline: **score, band, and the one sentence that explains it.**
2. The three footprint percentages, and which arena they own versus which they skip.
3. The differentiators.
4. Red flags, if any.
5. The unknowns that would change the score if answered.

Entering it in the workbook is optional and manual: open
`vendor-evaluation/Vendor-Scorecard.xlsx`, pick a vendor column, and set the dropdowns. The
workbook's formulas and `score.py` are verified to agree exactly, so the numbers will match.
The workbook's **Start Here** tab is the hand-out version of this rubric — point colleagues there,
not at this file.

## 6 · Judgement

- **Score the questionnaire, not the vendor.** You are measuring how well they described themselves
  against our spec. Say so when a low score looks like a writing problem rather than a product one —
  that belongs in the summary and in the unknowns.
- **A low footprint is not automatically a loss.** A vendor may have built a different, defensible
  product. That belongs in the differentiator list, and it is exactly the observation the operator
  cannot get from a number.
- **Never invent a citation.** If you cannot find the sentence, the mark is a partial or a zero.
- **Two vendors, same score, different shape** — say which arena each owns. That is the useful
  sentence, not the tie.
- **Flag what surprised you**, including things the rubric has no column for. The rubric is v1.0
  and the field will teach us where it is wrong; that feedback is worth more than a tidy total.
