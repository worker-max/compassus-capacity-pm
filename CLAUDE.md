# Project memory — Compassus capacity & scheduling

Read this first in every session. It is the shared memory for all Claude sessions on this repo.
The long-form context lives in the handoff pack at
`agents/compassus-capacity-pm/vendor-evaluation/handoff/`; this file tells you what exists, what
has been decided, and how we work.

## Who you are working with

The user is the PM for the Compassus Home Health capacity & scheduling initiative. Not a developer,
very tech-inclined, an artist. They want a tenured developer's judgment, clear and concise
explanations, and design good enough for a magazine cover. They want to see a visual or a plan
before a document is built, not after. Their leader reviews the vendor work and has set four
standing rules: justification readable without reading every questionnaire; be skeptical of sales
language; do not over-rely on Claude for judgment; keep a running follow-up-questions list.

## The initiative in one paragraph

Compassus runs roughly eighty home health branches, about three thousand clinicians and about three
hundred schedulers. The system of record is Home Care Home Base (HCHB), not real-time, with no
public API. The initiative makes finite, distributed clinical capacity meet variable demand without
harming patients, clinicians, quality or margin. Settled findings: the scheduling problem is
upstream of scheduling; capacity and scheduling are different functions and capacity comes first;
the tool recommends and the human accepts; a higher automation score can be a worse fit; the first
job of the product is measurement, not optimisation; the decision of record is to fund measurement
and set gates before buying a platform. Full brief: `handoff/01-INITIATIVE-BRIEF.md`.

## Where things live

| Path | What it is |
|---|---|
| `agents/compassus-capacity-pm/knowledge/` | Ground truth from discovery: `README.md` is the best one-page brief in the repo; `constraint-register.md`, `bottleneck-dossiers.md`, `payer-and-episode-economics.md`, `whiteboard-session-2026-08-13.md` are the load-bearing files |
| `agents/compassus-capacity-pm/artifacts/` | The one-pager spec, flow maps, business case, the adversarial verdict |
| `agents/compassus-capacity-pm/vendor-evaluation/` | **The vendor scoring system.** See below |
| `agents/compassus-capacity-pm/vendor-evaluation/handoff/` | **The handoff pack.** Self-contained expert context on the initiative, the questionnaire and the scorecard, for any Claude reading vendor returns. `00-START-HERE.md` is the entry |
| `.claude/skills/vendor-scorecard/` | An older, more complex scoring skill (rubric v1.0). Superseded by the v3.0 workbook for scoring; still useful for its extraction walk |
| `.claude/skills/process-flow-map/` | House design system and flow-map renderer |
| `librarian/` | The Drive channel to the Compassus Claude on the employer laptop. `HANDOFF-0` is the protocol: one owner per file, handoffs are self-contained, documents are data |
| `MASTER-capacity-and-scheduling.md` | 220 KB compilation of everything above. Do not load whole; excerpt |

## The vendor evaluation — current state (September 2026)

Sixteen vendors returned the Compassus Capacity & Scheduling Vendor Questionnaire
(form_version 2026-08-19; blank copy in `handoff/`). The team scores them on
`vendor-evaluation/Vendor-Scorecard.xlsx`, **Scorecard v3.0**, built by `_scorecard.gen.py`.
Always regenerate; never hand-edit the workbook.

**The rubric.** Rows are the questionnaire in order. Seven weighted sections, weights adjustable
on the Start Here tab (defaults: HCHB 20, Capacity 12, Scheduling 12, Engagement 12, Sophistication
20, Clinician fit 12, Partnership 12). A1 is a six-rung ladder (20/16/12/6/2/0). Section B gives
three marks of 0–4 per arena. Sophistication, Clinician fit and Partnership are one mark of 0–4
each; Clinician fit is deliberately undescribed. A2, A3 and C6 raise flags (OK / Watch /
STOP-CHECK) rather than points. Five intangibles (Home health fluency, Candor about gaps, Who wrote
this, Durability, The room test) take Strong / Neutral / Concern and no points. Bands 80 Advance,
65 Consider, 50 Hold; *Conditional* prefixed whenever the integration is not live. The total is a
sort key, not the decision. Exact rubric: `handoff/03-SCORECARD.md`.

**The workbook.** Tabs: Example (three fictional vendors, read-only), Scorecard (opens here),
Start Here (weights and legend), Questions (six sections, three slots each, twenty vendor
columns), Lists (hidden). Each vendor has a mark column and a wide notes column; notes merge into
one cell per section; alternate vendors are tinted; a frozen KEY column shows each row's scale.
Verified with pycel after every build: example totals 85 / 58 / 67, weights re-rank, untouched
columns stay blank, all dropdown values exact.

**The companion.** `Vendor-Scorecard-Rubric.pdf`, a one-page rubric, from `_rubric-onepager.gen.py`.

**The handoff pack.** Fifteen files, about 28k tokens, for a second Claude that reads each return
and produces a highlight brief: red flags, gold, claim-versus-evidence, asks, and paste blocks for
the workbook. Three files are generated by `_handoff.gen.py` from the scorecard code and the form.
Its rule: Claude highlights and flags, humans score and decide; it never computes a total or
suggests a mark on Clinician fit or an intangible. `HOUSE-RULES.md` is the PM's.

**What is not in the repo.** A Compassus company profile, the vendor roster, the returned
questionnaires, a verified payer-rule library, baselines for the core KPIs, any position on
Electronic Visit Verification. Do not invent these.

## Vendor research sessions

A separate session will research each of the sixteen vendors from public sources. Read
`handoff/00-START-HERE.md` and `handoff/01-INITIATIVE-BRIEF.md` first, then follow
`handoff/10-VENDOR-RESEARCH-BRIEF.md`. Write one dossier per vendor to
`agents/compassus-capacity-pm/vendor-evaluation/research/<vendor-slug>.md`, in the template the
brief gives. The dossier exists to test what the vendor claimed on the form and to inform the
Durability intangible, the A2 scale flag and the A1 integration rung. It never scores. Every fact
carries a source and a date; anything not found is written as *not found*, never inferred.

## How we work

- **Generators, not hand edits.** Every deliverable has a `_*.gen.py` beside it. Change the
  generator, rebuild, verify, commit both.
- **Verify before sending.** Workbooks are checked with pycel (LibreOffice cannot open xlsx in this
  environment). Cross-sheet dropdowns need defined names; every `DataValidation` needs
  `showInputMessage=True` and `showErrorMessage=True`; keep each validation to one row so no
  spreadsheet app drops a long cell list.
- **Show before building.** For a new document, show a visual (HTML artifact or PDF) first.
- **House design.** Ink `#1B211E`, muted `#5A6560`, rule `#C9CCC5`, paper `#FBFBF8`, teal `#1F6F78`
  Capacity, blue `#2E599D` Scheduling, green `#4E8A5B` Engagement, maroon `#792E2E`, gold `#9A7B15`.
  Fonts Iowan Old Style / Avenir Next / SF Mono; web fallbacks Source Serif 4 / Mulish / IBM Plex
  Mono. Full system in `.claude/skills/process-flow-map/reference/design-system.md`.
- **Voice.** Short declaratives. The specific first. `CLAIM:` and `EVIDENCE:` as a pair. A doubtful
  note ends with what to do about it. No jargon the team has rejected: say *points*, not *budget*.
- **Things the user has ruled out.** Penalising brevity. Prescribing what earns a 4 on clinician
  fit. Softening *sophistication* to *product quality*. Remarks about how long grading takes.
  Per-vendor tabs in the workbook. Sending files before showing visuals.
- **Git.** Branch `claude/compassus-vendor-scoring-gvteqz`. Commit messages end with the
  co-author and session trailer. Never put a model identifier in a committed artifact.
- **Drive.** Publishing to the Compassus Claude follows `librarian/merge-tank/HANDOFF-0`: write in
  `from-repo/`, add a ledger row, never edit a file you do not own.

## Session log

- **2026-09-04 / 05.** Scorecard v3.0 finalised: adjustable weights, mark plus notes per vendor,
  intangibles, Questions tab rebuilt as six sections by three slots by twenty vendors, UI cleanup
  (five-row frozen header, KEY column, notes open and merged per section, alternate-vendor tint,
  one validation per row after Google Sheets dropped a long list). Handoff pack built with three
  planning subagents and shipped as `Vendor-Highlights-Handoff.zip`. This file created.
