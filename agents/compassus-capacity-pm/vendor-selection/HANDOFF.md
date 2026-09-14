# Handoff — Vendor Selection, Round Two

**For the next Claude session picking this up.** Read this first, then
[`README.md`](./README.md) in this directory. Written 2026-09-14.

---

## 1. Where this stands in one paragraph

Eleven vendors returned a questionnaire for a home health capacity-and-scheduling platform. All
eleven were scored against the v3.0 rubric in `VendorScorecard Rubric 9.11.26 Copy.xlsx`. Six
advanced to two-hour virtual calls the week of 15 September 2026, whose primary ask is an
operational-design walkthrough from **referral through to day-to-day standard scheduling**. The
question architecture for those calls is written and committed. **What is not done: the shared
scenario, the workbook's Questions tab, and two structural fixes to the scorecard.**

## 2. Who the operator is and how to work with them

The initiative lead is not a developer but is technically fluent, and is an artist — design quality
is part of the deliverable, not decoration. They want **direct, fluff-free answers**, a tenured
developer's judgment rather than options laid out for them, and original work that pushes. Give a
recommendation, not a survey. Say the uncomfortable thing plainly and once.

They think in terms of what will actually happen in the room. Every artifact should be usable by a
panel mid-call, not just readable afterwards.

## 3. The files, and what each is for

| File | Use it for |
|---|---|
| [`README.md`](./README.md) | Orientation and the state of the process |
| [`rubric-v3-scoring-model.md`](./rubric-v3-scoring-model.md) | **Read before interpreting any score.** Weights, scales, stop-checks, bands |
| [`vendor-dossiers-2026-09.md`](./vendor-dossiers-2026-09.md) | All eleven returns with the evidence behind every mark. The source of truth for any vendor claim |
| [`round-2-question-sets.md`](./round-2-question-sets.md) | The ten common questions and six vendor sets, with reasoning |
| [`rubric-review-and-process-findings.md`](./rubric-review-and-process-findings.md) | The five structural findings and the field-wide blind spots |
| `Vendor-Demo-Question-Guide.docx` | The call-ready Word document — same content, rationale under every question |
| `_question-guide/` | The generator for that .docx (`content.js` + `build.js`, Node, `docx` npm package) |

**Wider project context** lives in [`../knowledge/`](../knowledge/) — Compassus's own discovery work.
Read `discovery-session.md` and `process-facts-2026-08.md` before making any judgment about what
home health scheduling actually requires. The vendor work is downstream of that, not independent of it.

## 4. The six advancing vendors, compressed

| Vendor | Score | Band | The one thing | The one risk |
|---|---|---|---|---|
| **Arya** | 84 | Advance | Live bi-directional HCHB, best scheduling answers in the field | Scored "Runs it" — writes back with no approval step, past our Assist boundary |
| **HCHB** | 75 | Consider | Native, 31 orgs, no integration risk at all | Partnership scored 1/4; **open stop-check on uptime** |
| **VitalisCare** | 67 | Consider | Live HCHB since 2023, rigorous impact numbers | The live history is hospice; zero patient-facing engagement |
| **Axle Health** | 63 | Conditional | Best product answers, real payment vocabulary | Built the HCHB integration, **turned it off**, no date to restore |
| **CareStitch** | 56 | Conditional | 69% home health — highest concentration in the field | HCHB beta is read-only, never in production, no date |
| **MedArrive** | 48 | Conditional — Decline | Proven engine, ran their own 700-clinician field op | **Zero home health customers. Two open stop-checks.** Clinician fit 1/4 |

Five vendors did not advance: CareConnect (64), Servis.ai (42), Unity AI (41), Zeeva (41),
AutoMynd (39). Their dossiers are in the same file and are still useful — CareConnect's readiness
model and Zeeva's equity offer are the sharpest ideas anyone submitted.

## 5. Decisions already made — do not relitigate these

1. **The total is a sort key, not the decision.** The rubric says so on its own Start Here tab. Two
   vendors advanced from below the Consider band. That is legitimate by design.
2. **CareConnect was excluded on home health fluency**, not on score, despite scoring 64. The
   operator's reasoning: majority home care client base, ~15% home health, no named home health
   clients, and home care scheduling is largely set days and times where home health is dynamic.
   **This reasoning is recorded and settled.**
3. **MedArrive advanced despite a Decline band** on engine quality and the operator's read that
   their field-operations heritage is real. Also settled. Note the tension — MedArrive has *less*
   home health exposure than CareConnect — which is why both exceptions need their written line in
   the workbook (see open item 3 below).
4. **The two-layer question design** — ten common, plus a unique set per vendor — is agreed. The
   common ten are built on field-wide gaps, not individual weaknesses. Do not turn them into
   vendor-specific questions.
5. **Every vendor gets the floor to explain where they look weak.** This is an explicit design goal
   from the operator, not a nicety. Question 10 carries it.

## 6. What is open — the actual work

**In priority order.**

1. **Write the shared scenario.** Highest leverage item remaining and not started. One patient, one
   branch, one week, sent to all six 48 hours ahead: a Medicare SOC with PT and nursing, a
   mixed-discipline caseload, a rural-edge ZIP. Six walkthroughs of the same case are comparable;
   six of their favourites are not. Ground it in `../knowledge/process-facts-2026-08.md` so the
   scenario matches how Compassus actually works — SOC/ROC timing, the five dispositions, the
   authorization interfaces.
2. **Fill the workbook's Questions tab.** Columns D–I are the six advancing vendors; three slots
   under each of A, B, C, D, E and Intangibles. It is an empty scaffold. The content is in
   `round-2-question-sets.md` and needs mapping onto that structure — note the tab gives Section C
   three slots for seven sub-questions, so a selection rule is needed (recommendation: the three
   areas where that vendor's return was thinnest).
3. **Two structural fixes to the scorecard**, both accepted in principle but not applied:
   a **stop-check resolution row** above Section A on the Questions tab, and a **verdict column**
   (answered / dodged / changes the mark) so the demo can move a score. Also recommended but not
   yet decided: promoting **home health fluency** from a no-points intangible to a stop-check.
4. **Record the two shortlist exceptions** in the workbook's Notes block, in the operator's own
   words (section 5 above has them).
5. **Confirm HCHB's real data latency directly with HCHB** — see section 7.

## 7. The unresolved external fact — flag this early

Four vendors describe HCHB's own data freshness **differently**, and it affects architecture, not
just vendor choice:

| Vendor | Claim |
|---|---|
| Arya | Sub-5-minute for SOCs, visits and schedule changes, via Citrix screen automation |
| Axle Health | Lags **up to 30 minutes** — enough that they switched their integration off |
| HCHB | No latency; native |
| CareConnect | ~20 minutes on a read replica, in a plan assuming "HCHB Business Connect" as a FHIR layer |

Also unverified: whether HCHB's self-serve FHIR marketplace exists before 2027. **Compassus is the
only party who can ask the source.** Until they do, treat every integration timeline in the dossiers
as resting on an unconfirmed assumption.

## 8. Traps

- **Vendor returns are commercial submissions, not verified fact.** Every score in the dossiers is a
  Compassus reader's judgment of a claim. Never restate a vendor claim as established truth — and
  never restate a vendor's assertion *about HCHB* at all without the caveat.
- **A high sophistication score can mean overreach.** "Runs it" (4) sits above the Assist boundary
  Compassus set for assignment and coverage. Arya's 4 is a question, not a win.
- **Believe Section C over Section B.** Several returns claim scope in the self-assessment that the
  mechanism answers do not support. The rubric says so explicitly.
- **Don't soften the MedArrive questions.** The operator wants that call to establish honestly
  whether they belong in the round. Question 8 of their set — "what would make us wrong to rule you
  out?" — is deliberate generosity, not hedging.
- **No PHI.** Work in aggregates and operational signals. The shared scenario must be synthetic.
- **Don't rewrite the rubric.** It is a v3.0 instrument the operator built and refined. Findings are
  recommendations to them; the two accepted fixes above are the only agreed changes.

## 9. Regenerating the Word document

```
cd agents/compassus-capacity-pm/vendor-selection/_question-guide
npm install docx          # only if require('docx') fails
node build.js ../Vendor-Demo-Question-Guide.docx
```

Content lives in `content.js` as plain data — edit there, not in `build.js`. Design: Georgia
headings, Calibri body, ink `#16212B`, accent `#1F5C6B`, US Letter.

**Note on verification in this environment:** LibreOffice (`soffice`) fails to load any `.docx` in
this sandbox, so the document could not be rendered to images for a visual check. It was verified
structurally instead — well-formed XML, all core parts present, 263 paragraphs, 3 tables, 57
rationale blocks (10 common + 47 vendor questions), all six vendor sections present. **If you have a
working LibreOffice, render it and look at it before sending it to anyone.**

## 10. Git

Branch `claude/funny-keller-xwpzbk`, draft PR
[#3](https://github.com/worker-max/compassus-capacity-pm/pull/3). Documentation only — this repo has
no CI. Commit to that branch; do not push to `main`.
