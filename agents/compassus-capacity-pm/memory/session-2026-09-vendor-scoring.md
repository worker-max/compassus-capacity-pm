# Session record — vendor scoring, September 2026

The full record of the session that produced Scorecard v3.0, the one-page rubric, the handoff pack
and the project memory. Written so a later session can understand not just what exists but why it
is shaped this way and what was rejected on the way.

Branch: `claude/compassus-vendor-scoring-gvteqz`. All work committed there.

---

## 1. What the user asked for, in sequence

1. A simple scoring guide and scorecard for sixteen returned vendor questionnaires. Priorities:
   HCHB integration weighted heavily; free text matched against the one-pager scope (capacity,
   scheduling, engagement); a sophistication score; a partnership score; a differentiators list. Also
   a Claude skill for uploading questionnaires and producing a deep-dive, summary and footprint
   percentages (this became the `vendor-scorecard` skill, rubric v1.0, now superseded for scoring).
2. *"What do you mean by budget? Show me all this cleanly before building any document."* The word
   *budget* was rejected as jargon; we say *points*. Visuals before builds became a standing rule.
3. *"Every question has a way of being scored also?"* Yes; the questionnaire became the rubric.
4. *"This has to be easy for me to explain and for my team to understand without a lot of effort."*
5. *"Tell me about sophistication."* Sophistication is how much of the work the product does, on the
   Read / Assist / Control ladder. Their leader specifically asked for it by that name; a later
   draft that softened it to *product quality* was rejected.
6. One document: legend and summary on the first tab. Then *"press a reset button"* and build a more
   straightforward scorecard as a backup, starting from the primary workbook's example scorecard for
   the two HCHB scheduling products.
7. One-pager: portrait, top and bottom sections for the two options, no subheadings or footers.
8. Do not penalise vendors for lacking space to explain how; summaries must not seem contrived.
9. *"Were you overly biased by the example I gave you? Is there a better type of rubric?"* Led to a
   questionnaire-ordered rubric rather than a category-ordered one.
10. *"Is there a clean way so that the questions we had on the questionnaire are part of the
    rubric?"* Yes: rows are the questionnaire, in order.
11. *"How do we get the missing 25 for clinician fit and partnership added so it is easy for us?"*
12. *"Give me a visual of the rubric before creating the document."*
13. *"I'll share the more complicated tool later but I need to get this simplified scorecard rubric
    to my leader this afternoon. Set up the one-pager as a companion. Don't feel you have to fill the
    whole page. Keep it simple, no spicy headings or footnotes."*
14. Confusion over clinician-fit ratings and a wish for more points to play with on scope, because
    *"covers most of it"* and *"all of it"* would never be an answer.
15. *"For clinician fit we need to be scoring it based on our own perception of fit. You don't need
    to lead us to what equals a 4. For scope your 4 and 5 can be the same. Maybe lower HCHB points.
    Live via partner is fine enough. The one above can be Live, small customer base."*
16. Partnership redefined: *"a company that has the willingness and environment to work with us on
    this product based on our needs and open to offering equity to us so that a product for the
    generalized market could be a potential."*
17. *"Confirm this marries up with the order of the questionnaire and the scope tied to the
    one-pager specs is easy to apply."*
18. Show the rubric as HTML; show the one-pager in final form before the file; one-pager sections
    felt out of line; remove remarks about how long grading takes.
19. Example filled out on tab one, blank ready to go on tab two. One-pager as PDF too. Workbook as a
    download.
20. *"Scope is confusing. None of the cells have dropdowns. Scoring on a 0–5 scale that equals 12
    points per section feels off."* Then: *"Are there subcategories for capacity, scheduling,
    engagement that could have part of the 12 points?"* Then: *"The subcategories on the one-pager
    were not baked strongly enough. Each section should hold the same weight, even if it means
    grouping two subcategories. I'm fine with a few more marks if it allows honest granularity."*
    Result: three marks of 0–4 per arena, twelve points each.
21. Leader's feedback, relayed, with *"perform no action, let's talk through the best approach"*:
    weights as per-section grades with optional preliminary weighting for sorting; justification
    readable without reading every questionnaire; be skeptical of sales BS; do not over-rely on
    Claude for judgment; keep a follow-up-questions list.
22. Decisions on the five proposals: weights as adjustable parameters (*"love it"*); leave the A1
    ladder as-is; two columns per vendor, score and notes with decent writing space; claim versus
    evidence lives in that notes column; a Questions tab in questionnaire order with twenty columns
    and blank space per section. Plus a new intangibles section; the user chose five dimensions and
    dropped *did they engage with us* because they would be watching for it already.
23. The actual key for how to score in each section, and dropdowns on the real tab that look like
    the example tab.
24. Screenshot: *"Use subagents to assess for a better UI. This seems off and hard to use, no legend,
    and eyes are crossed looking at this."* Then: *"No, just make the design cleaner and better."*
    (no restructuring into per-vendor tabs).
25. *"Do we have a tab for vendor-specific questions?"* Then the spec: sections pre-established,
    three questions per section, twenty columns, one vendor per column.
26. Screenshot from Google Sheets: scope cells not dropdowns; header too large to freeze.
    *"I just care about Excel versioning."*
27. *"Where is the key to make cross-referencing easy as I score?"*
28. *"I need a large line-itemed partner column for every vendor next to the scores. We had
    something, but you took it away. Each vendor should have two parallel columns. Every other
    vendor a slightly different colour. The second column wide enough for a detailed note. Each
    section can have a merged note cell rather than a note for every row."* Then *"Oh, love that,
    no work needed"* (they had found the collapsed columns); the rework was delivered anyway.
29. Set up another Claude instance to read the vendor answers and highlight the most important
    pieces for the PM and leader, with knowledge of the project and the rubric; a fleet of handoff
    documents; use subagents to plan.
30. Commit everything to project memory so other sessions have full context; a new session will
    research each vendor.

## 2. The decisions, and what was rejected

| Decision | Rejected alternatives | Why |
|---|---|---|
| Rows are the questionnaire, in order | Category-ordered rubric; the workbook's own functional scorecard | The team reads a return top to bottom; the rubric should follow the page |
| Seven weighted sections; weights live on Start Here as cells | Fixed weights; no weights | Leader wanted per-section grades with optional weighting for sorting; user loved adjustable parameters |
| A1 six-rung ladder 20/16/12/6/2/0 | Twelve-point middle rungs; a *brittle method* rung | User: *"live via partner is fine enough"*; lower HCHB points; brittle-method demoted to a flag |
| Scope: three marks of 0–4 per arena, mark equals points | One 0–5 mark per arena scaled to 12; 41-element footprint counts | Twelve points per arena must hold equal weight; the mark must be the points so nothing feels off; the 41 elements are too many to mark by hand |
| Scope pairing: B4+B5 into SCH1, B9+B10 into ENG2 | Inventing a fourth sub-area | Capacity has three areas; Scheduling and Engagement have four; pair rather than invent |
| Sophistication: one mark, Shows / Checks / Recommends / Runs | Five sub-marks per C question; *product quality* | Named as sophistication because the leader asked for it by name; one mark keeps it simple |
| Clinician fit: 0–4 with no descriptions | Descriptive rungs that say what earns a 4 | User: *"we need to be scoring it based on our own perception of fit"* |
| Partnership: 0–4 topping out at open to equity | Four sub-marks; a discount counted as partnership | User's definition of partnership; *"a discount is a discount"* |
| A2, A3, C6 as flags | Point deductions | A missing continuity commitment should stop and ask, not dock points |
| Five intangibles, no points | Six, including *did they engage with us* | User dropped the sixth |
| Two columns per vendor; notes merged per section | One column; a note per row; collapsed notes by default | User wants a large line-itemed partner column; merged cells give more room; collapsed read as *gone* |
| Questions tab: six sections × three slots × twenty vendors | A shared tick-list with a *what would prove it* column | User's explicit spec |
| Frozen KEY column beside the criteria | Key only on Start Here and in dropdown prompts | Prompts do not show in every app and Start Here is another tab |
| One data validation per row | One validation covering all nine scope rows | A long cell list was silently dropped in Google Sheets; short lists survive everywhere |
| Workbook opens on Scorecard; Example is read-only, no password | Opens on Example | Audit found people would type into the example |
| Five-row frozen header | Eleven-row masthead | User: *"looking through half-closed eyes"* |
| Keep a single Scorecard tab | Sixteen per-vendor tabs | User: *"no, just make the design cleaner and better"* |
| Handoff pack as fifteen markdown files, three generated | A single long document; a skill | Generated files cannot drift from the workbook; a Project can hold files; a pack can be published to Drive |
| The reading Claude never scores | Claude suggests all marks | Leader: do not over-rely on Claude for judgment |

## 3. The user's standing preferences, as learned

- Show a visual or a plan before building a document. Do not send files first.
- Museum-quality design. House palette and type. No spicy headings, no footnotes.
- Clear and concise. They learn by seeing the thing, not by reading about it.
- Plain words. *Points*, not *budget*. *Sophistication*, not *product quality*.
- Do not remark on how long something will take to grade or fill in.
- Do not prescribe judgment calls that belong to the team (clinician fit).
- Do not penalise brevity; the form gave no room.
- Excel is the target. Google Sheets remarks are noise to them.
- When they say *love it, no work needed* mid-build, finish the build if it matches their spec and
  say plainly the previous version is one message away.

## 4. Engineering lessons

**openpyxl and Excel**
- Cross-sheet dropdown lists must be defined names (`HCHB_List`, `Scope_List`, `Soph_List`,
  `Clin_List`, `Part_List`). A direct `Lists!$E$2:$E$6` in `formula1` is dropped by Excel.
- Defined names inside formulas break pycel. Weights therefore use direct cross-sheet references
  (`='Start Here'!$C$10`), not names.
- `DataValidation` defaults to `showInputMessage=False` and `showErrorMessage=False`. Set both True,
  or the prompt is invisible and a typo silently scores zero.
- One validation object per row. A single object with 144 cells in its `sqref` was dropped by
  Google Sheets; keeping each list under about 130 characters survives everywhere.
- `ColorScaleRule` with a `containsText` operator is invalid; use `FormulaRule` with `SEARCH`.
- `ws.sheet_properties.pageSetUpPr` may be `None`; assign `PageSetupProperties(fitToPage=True)`.
- Merged cells: style the anchor before merging; `merge_cells` propagates borders to the edges.
- Outline groups: `column_dimensions[col].outlineLevel = 1`; `hidden = True` collapses by default.
  Users read collapsed columns as deleted; leave them open.
- Sheet protection: `ws.protection.sheet = True` with `formatColumns = False` and
  `formatRows = False` so outline buttons still work.
- `wb.active` by index does not clear `tabSelected` on other sheets; set `sheet_view.tabSelected`
  explicitly on every sheet.
- The formula `VALUE(LEFT(mark,1))` reads the leading digit of a dropdown label, which is why
  every scale label starts with its number and why typed values must be refused.
- Section grades gate on `IF(A1="","",…)` so an untouched vendor column stays blank rather than
  showing *0.0 / Conditional — Decline*.
- Rounding: sum unrounded, round once, half-up.

**Verification (run after every build)**
- pycel on `Vendor-Scorecard.xlsx`: example totals 85 / 58 / 67; Northlight band reads
  *Conditional — Consider*; Wayfinder stop-checks 1; a blank column evaluates to `""`.
- Change two weights in the compiler and confirm the totals re-rank (HCHB 8, Partnership 24 gives
  82 / 54.4 / 75.4).
- Every mark on the Example tab is an exact dropdown value.
- Questions tab headers resolve to the Scorecard names.
- LibreOffice cannot open xlsx in this environment; pycel is the check.

**Rendering**
- The one-pager PDF is rendered with the pre-installed Chromium
  (`/opt/pw-browsers/chromium-1194/chrome-linux/chrome`), portrait 1360×1760.
- f-strings with backslashes inside heredocs raise SyntaxError; avoid nested quotes.
- Artifact watch subscriptions are refused in this session type; republish manually.

## 5. Files produced

| File | Purpose |
|---|---|
| `vendor-evaluation/_scorecard.gen.py` | Builds `Vendor-Scorecard.xlsx`. Constants at top are the rubric |
| `vendor-evaluation/Vendor-Scorecard.xlsx` | The workbook, v3.0 |
| `vendor-evaluation/_rubric-onepager.gen.py` | Builds `vendor-scorecard-rubric.html` and `Vendor-Scorecard-Rubric.pdf` |
| `vendor-evaluation/_handoff.gen.py` | Builds handoff files 02, 03, 09 from the form and the scorecard code |
| `vendor-evaluation/handoff/` | The fifteen-file pack; `00-START-HERE.md` is the entry |
| `vendor-evaluation/Vendor-Highlights-Handoff.zip` | The pack, zipped for upload |
| `vendor-evaluation/research/` | Where vendor research dossiers go |
| `CLAUDE.md` | Short project memory |
| `memory/` | This folder |

Stale and superseded: `vendor-evaluation/scoring-guide.md`, `verify-agreement.py`,
`example/meridian-care-logistics.json` and its scorecard, and `.claude/skills/vendor-scorecard/`
describe rubric v1.0. `vendor-evaluation/README.md` carries a banner saying so.

## 6. Open items

- The user said they would share *the more complicated tool* later; the v1.0 skill is not aligned
  with the v3.0 scorecard and may need reworking when that happens.
- The sheet-preview artifact from earlier in the session shows the v2 single-column layout and is
  stale.
- The vendor roster is not in the repo. The research session needs the names from the user.
- `HOUSE-RULES.md` is empty until the first three real vendors are scored.
- The one-pager PDF still carries the long-form Partnership wording, which matches Start Here; the
  workbook dropdown uses shortened labels. Both say the same thing.
