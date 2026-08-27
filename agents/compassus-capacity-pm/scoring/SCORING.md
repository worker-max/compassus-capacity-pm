# How to score a returned vendor questionnaire

**You need nothing but the returned workbook and this file.** No other document, no prior
context, no questions to anyone. Roughly ten vendors, one row each.

**What this produces, and what it does not.** It produces a *shape* — what a vendor covers,
what they do not, and what they claim that cannot be checked on paper. It is built entirely
from vendor self-report in a competitive bid, so it measures breadth of claim, not quality,
evidence or fit. **Do not rank on the coverage total alone.** In testing, a model that scored
this field produced its highest score for the weakest vendor: one with no capacity management
at all and a stated posture of "designed to decide". The named columns are what carry meaning;
the total is a tiebreaker.

---

## Step 1 — Pull four facts, verbatim

From the **Questionnaire** tab.

| Field | Where | What to record |
|---|---|---|
| **HCHB** | A1 | `Live-write` · `Live-read` · `Building` · `None` — see the boundaries below |
| **Scale** | A2 | production home-health customers, and the census of the largest deployment |
| **Impact** | A3 | one measured result, or `none given` |
| **Continuity** | C6 | uptime figure and what a customer can do during an outage, or `none given` |

**HCHB boundaries.** `Live-write` — in production with a named customer and writes back to
HCHB. `Live-read` — in production but read-only, no write-back. `Building` — committed work
with a date. `None` — nothing built, or "we would need an extract from you". A read-only feed
is not the same as an integration; record it as `Live-read` and say so.

---

## Step 2 — The coverage string

Part B is the eleven-area grid on the Questionnaire tab. Read `IN SCOPE` (column D) and
`STATUS` (column E) for each area and write one digit per area, **in this fixed order**:

`1` Workforce supply · `2` Availability & reach · `3` The capacity math · `4` Demand ·
`5` Matching · `6` Routing & the week · `7` Exceptions · `8` Before the visit ·
`9` When plans change · `10` Incentives & offers · `11` Across the care team

| Digit | When |
|---|---|
| **2** | `IN SCOPE = Yes` **and** `STATUS` is either Production value |
| **1** | `IN SCOPE = Yes` but status is In development, Roadmap, Other, or blank — **or** `IN SCOPE = Through a partner`, any status — **or** `IN SCOPE = Other` |
| **0** | `IN SCOPE = No`, or `IN SCOPE` left blank |

Every area gets equal weight. Do not weight by anything. Write the string and the total out
of 22, then **list the areas scoring 0 by name** — that list matters more than the total.

---

## Step 3 — Automation flags

Column F, `HOW IT'S DONE`. Flag any area where the vendor selected **"Automated end to end"**
and we expect a person in the loop. Name the areas; do not count them.

Expect a person in the loop in: **Matching** (24 of 27 variables), **When plans change** (3/3),
**Across the care team** (3/3), **Incentives & offers** (2/2), **Routing & the week** (6/9),
**Exceptions** (3/4). A flag in **Matching** is the serious one.

Not flags: **Demand** and **The capacity math**, where we asked for automation.

**Areas 1–3 cannot be flagged from the grid.** Their column F offers a data-provenance list,
not an automation list, so "Automated end to end" is not selectable there. For those, read
D1 and D2 instead.

**Then read D1 and D2 regardless.** A vendor whose D2 says the product is designed to decide
is making a posture claim the grid will not show. Record it in plain words.

---

## Step 4 — Three questions for the call

Write the three claims this vendor made that **cannot be verified on paper**, each tagged with
the question it came from. This is the only judgment call in the process, and it is the output
that decides whether the call is worth having.

---

## Step 5 — Add the row

Append to `vendor-comparison.md` in this folder. Sort by HCHB, then scale, then coverage total.

---

## Do not score these

We never asked about them, so a vendor strong on them looks identical to one who is not:
**consent and contactability**, **territory currency and geography realism**, **queue depth and
add-on orders**, **clinician safety**. If a vendor volunteers any of them, note it as a credit
in their row — never as a deduction against one who did not.

Likewise **do not deduct for the sixteen prose answers being thin**. Only A1, A2, A3, C6, D1
and D2 carry consequences here. The rest are read for the call, not for the row.
