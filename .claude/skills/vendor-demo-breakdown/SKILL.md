---
name: vendor-demo-breakdown
description: Break a recorded Compassus capacity & scheduling vendor demo (Teams MP4 on Google Drive) into a full evaluation package - transcript, product screen captures, visual report, shareable readout PDF, vendor flow-map overlay, variable-coverage scoring, and an updated cross-vendor comparison. Use when the user shares a vendor demo recording link or asks to evaluate, summarize or compare a vendor demo/meeting.
---

# Vendor demo breakdown

The repeatable pipeline used for Axle Health (22 Sep), CareStitch (23 Sep) and VitalisCare (24 Sep 2026).
Following it on the next recording should produce the same package, in the same shape, so the vendors
compare side by side.

**Read `/CLAUDE.md` first.** Its rules override anything here: HTML is shown to the owner for review
before *any* PDF is generated, shareable documents use the plain internal-memo style, PDF metadata is
stripped, and WorkforceWave never appears in anything shared with Compassus.

## What the owner gets, in order

Deliver in this order and **stop for approval where marked**. The owner asked for the full summary and
visual document first; adjunct documents (flow map, one-pagers) only when asked.

1. Screens + transcript committed (early, so work is not lost).
2. **Visual report** `index.html` published as a private artifact → owner reviews.
3. **Readout PDF** of that report, only after approval.
4. On request: **flow-map overlay** (`artifacts/Flow-Vendor-<Name>.pdf`).
5. On request: vendor one-pager; **update the cross-vendor comparison** (coverage CSV + comparison one-pager),
   HTML first, PDF after approval.

## Where things live

| Thing | Location |
|---|---|
| Per-vendor package | `agents/compassus-capacity-pm/vendor-demos/YYYY-MM-DD-<vendor>/` with `README.md`, `transcript.md`, `index.html`, `screens/HHMMSS.jpg`, `<Vendor>-Demo-Readout.pdf` |
| Report template (copy it) | `vendor-demos/2026-09-22-axle-health/index.html` (full structure + lightbox + tokens) |
| Coverage scoring | `vendor-demos/variable-coverage-by-vendor.csv` + `scripts/coverage.py` |
| Cross-vendor comparison | `vendor-demos/vendor-comparison-one-pager.html` (+ PDF) |
| Flow overlay generators | `artifacts/_flow-vendor-axle.gen.py` (template), `_flow-vendor-carestitch.gen.py`, `_flow-vendor-vitaliscare.gen.py`; drawn with the `process-flow-map` skill toolkit |
| Variable Inventory (79 rows) | `knowledge/source/workbook-2026-08-13/Variable Inventory.csv` |
| Demo question guide | Drive `Vendor-Demo-Question-Guide.docx` (id `1-cvjVv3FA4BctCCAfgI2blnzo0367SLk`): 10 common + a set per vendor |
| Vendor questionnaire returns | Drive folder `Vendors` (id `1vJ0KC-ZhISmEWbsw34x2gB3BP7JkljsK`); search `title contains '<Vendor>'` |
| Scorecard | Drive `VendorScorecard Rubric 9.11.26 Copy.xlsx`; going-in scores so far: VitalisCare 67 Consider, Axle 63 Conditional, CareStitch 56 Conditional |

Work files (video, audio, samples) go in the session scratchpad, never the repo.

## Step 1 — get the recording

```bash
S=.claude/skills/vendor-demo-breakdown/scripts
bash $S/prepare.sh <drive_file_id> <scratchpad>/<vendor>
```
- Get the title, date and size with the Drive connector's `get_file_metadata`. The Drive connector cannot move a
  ~1 GB video; `prepare.sh` downloads it directly, which only works while the file is shared
  **"Anyone with the link"**. If the script says NOT A VIDEO, ask the owner to change sharing; after
  the download, remind them to restrict it again.
- Transcription runs in the background (~35–40 min per 2 h). Watch with
  `until grep -q done transcribe.log; do sleep 30; done` as a background command; don't poll by hand.
- While it runs, pull the vendor's questionnaire return from Drive for context.

## Step 2 — pick and crop screens

- Read the contact sheets `sheets/sNN.jpg` **a few at a time** (large image batches get dropped).
  Find where the screen share starts; skip participant-grid frames. Pick 40–50 distinct product/deck
  screens across the whole demo (setup, core workflow, exceptions, mobile, analytics, key slides).
- Grab one full-res frame, look at the layout, then:
  `python3 $S/extract_screens.py <work> <pkg>/screens <crop> <idx...>` with `auto` or a measured box
  (Axle needed `0,18,1674,1048` to drop the participant strip). Check a montage of the results; recrop if
  browser chrome, taskbars or video tiles show.
- Commit and push the screens right away.

## Step 3 — transcript and reading

- `python3 $S/make_transcript.py <work> <pkg>/transcript.md "<Vendor>" "<date, time>" "<h:mm:ss>" "<Drive title>"`
  then add vendor-specific name fixes (e.g. CareStitch, Axle) with a quick `sed`.
- `python3 $S/reading_chunks.py <work>`, then **read `txA.txt` and `txB.txt` in full**. Every claim in the report
  needs a timestamp from the transcript; the transcript has no speaker labels, so infer speakers from
  context and say so in the footer.

## Step 4 — the visual report (`index.html`)

Copy the Axle `index.html` (head/CSS, and the lightbox `<dialog>` + script at the end) and replace the body.
Keep this section order so vendors compare:

1. **Masthead**: vendor name, one-paragraph lede, 4 meta tiles (scorecard going in · live footprint ·
   guide questions answered · next touchpoint).
2. **The read**: six numbered findings with timestamps, plus a **suggested scorecard movement** box.
3. **Shape of the call**: proportional timeline bar + legend by topic.
4. **What Compassus told the vendor**: our numbers as stated (census, schedulers, HCHB refresh, timeline).
   Flag anything that differs from what we told other vendors.
5. **Process flow**: 8 clickable stage cards (Live / Partly / Not built / Outside chips), then one
   section per stage: *what it does* · *for Compassus* · a quote · screen gallery with timestamped captions.
6. **Claims / fit table**: impact claims with our read.
7. **Question guide**: all 10 common + the vendor-specific questions, each Answered / Partly /
   Not answered / Not asked, with what we heard and the timestamp. Tally at the top.
8. **Considerations**: High / Medium / In their favour.
9. **Next steps**: agreed on the call vs. recommended for the next meeting.
10. **Who was there**; footer with method note and "Prepared for Compassus Operational Excellence · Internal".

Publish with the `Artifact` tool: `root` = the package dir, `files` = every `screens/*.jpg` the page
references. The page is private and carries the owner's account name, so tell them to **share PDFs, not links**.

## Step 5 — readout PDF (after approval only)

- Print version = same body, lazy-loading removed, "click a stage" removed, plus the print CSS used for the
  existing readouts (`@page 11in 8.5in`, each stage section `break-before:page`, 3-up galleries, fixed
  table layout). Build a temp print HTML and render:
  `python3 $S/render_pdf.py <print.html> <pkg>/<Vendor>-Demo-Readout.pdf "<Vendor> Demo — Readout" --embed-fonts .claude/skills/vendor-demo-breakdown/reference/local-fonts.css`
  (headless Chrome can't reach Google Fonts through the proxy, which is why fonts get embedded).
- Rasterize every page (pypdfium2) into contact sheets and **look**: no near-empty pages, no split
  verdict boxes, no clipped right edge. Fix with print-only CSS and re-render.
- **Style decision:** readouts made before 26 Sep use the editorial report style. `/CLAUDE.md` now
  requires the plain memo style for shareables, so confirm with the owner which to use before rendering.

## Step 6 — scoring (feeds the comparison)

- **Variable coverage**: add a column for the vendor to `variable-coverage-by-vendor.csv` and mark all 79
  rows `S` (shown in software), `D` (discussed, including "roadmap" answers and items only Compassus
  raised) or `-` (not covered). Shared-spine rows count under Capacity; Coordination rows count under
  Engagement. Run `python3 $S/coverage.py <csv>` for the table and the never-covered list.
- **Three ratings, 1–5** (our read, labelled as such):
  - *Product sophistication*: 1 displays data · 2 filters eligibility · 3 recommends some decisions ·
    4 recommends clinician/day/time with reasons and suggests cover · 5 decides autonomously with guardrails.
  - *Scheduler task reduction*: how much of assignment, bulk plotting, coverage and rework it removes,
    net of HCHB dependencies and double-entry risk.
  - *Clinician experience*: evening-call burden, control of own day, one app vs. two, trust (tracking),
    visibility of the "why".
- Also capture: HCHB integration status, home health logic, patient engagement live, footprint,
  scorecard → suggested next step, and what the vendor must prove at the on-site.

## Step 7 — flow-map overlay (on request)

Copy `artifacts/_flow-vendor-axle.gen.py` to `_flow-vendor-<vendor>.gen.py`. Keep the grammar: the same
five bands (A referral to admission · B which clinician · C which day · D day before / day of · E when
the day breaks), vendor colour `#A33A6B`, badges `live / road / build / opp` relabelled for the vendor,
a right panel "Where automation is possible", a second panel on the vendor's standout or the data path,
and a "Where it breaks" row. **Write new band content to a separate file and splice it in**; `re.sub`
with `\u` escapes in the replacement text will fail. Render with the `process-flow-map` skill's
`build.py`, look at the PNG, strip metadata, add README rows and a note in
`flow-map-redraw-assessment.md`. It is labelled *not current state*.

## Commit, PR, hand-off

- Commit per stage (screens → package → PDF → overlay) with the session's attribution lines; push to the
  working branch; keep one draft PR and update its description as vendors are added.
- Every PDF: run `render_pdf.py` (it fails if author/Chrome/WorkforceWave strings leak), then send it with
  `SendUserFile` (attach).
- In chat: short bottom line, the few findings that matter, what's still open. Don't paste the report.
