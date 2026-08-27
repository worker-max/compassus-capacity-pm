# DRAFT scoring model — for critique, not yet built

## Purpose
A returned vendor questionnaire arrives. A Claude session that has never seen this project
must be able to score it and add it to a running comparison, without asking anyone questions.

## Inputs
- The returned workbook (tabs: Instructions, Questionnaire, Overview, Lists, Meta)
- Part B on the Questionnaire tab: 11 areas, each marked IN SCOPE / STATUS / HOW IT'S DONE / NOTES
- 17 prose answers (A1-A3, C1-C7, D1-D3, E1-E4)

## Proposed outputs per vendor
1. **Footprint %** — weighted coverage. Area weights come from the variable inventory:
   each area's weight is the sum of MVP weights (Yes=3, Maybe=1, No=0) of the variables behind it.

   | Area | Vars | Weight | Share |
   |---|---|---|---|
   | Matching | 27 | 51 | 26.4% |
   | Workforce supply | 11 | 25 | 13.0% |
   | Demand | 8 | 24 | 12.4% |
   | Availability & reach | 9 | 22 | 11.4% |
   | The capacity math | 8 | 21 | 10.9% |
   | Before the visit | 9 | 21 | 10.9% |
   | Routing & the week | 9 | 12 | 6.2% |
   | Exceptions | 4 | 7 | 3.6% |
   | When plans change | 3 | 7 | 3.6% |
   | Across the care team | 3 | 3 | 1.6% |
   | Incentives & offers | 2 | 0 | 0.0% |

   Scope factor: Yes=1.0, Through a partner=0.5, No=0
   Status factor: Production multiple=1.0, Production one=0.85, In development=0.5, Roadmap=0.2
   Area score = scope x status. Footprint = weighted mean.

2. **Knockouts** — areas containing gating variables where the vendor marked IN SCOPE = No.
3. **Posture overreach count** — areas where the vendor says "Automated end to end" but our
   posture for the variables behind it is Surface or Assist. Cross-checked against D1 and D2.
4. **HCHB integration verdict** from A1: Live / Building / None.
5. **A short written read** — 5 sentences.

## Proposed process for the tallying session
1. Open the returned workbook, read Part B and the 17 answers.
2. Fill one row in a running comparison sheet.
3. Write the 5-sentence read.
4. Flag anything that contradicts itself between Part B and the prose.

## Known issues to resolve
- "Incentives & offers" has weight 0 because both its variables carry MVP = "--". It would
  contribute nothing to the footprint despite being a real ask.
- 17 variables have a blank Constraint, so Gating computes N for them and they cannot knock out.
- We never asked about consent, geography realism, queue depth or clinician safety, so those
  must not be scored.
