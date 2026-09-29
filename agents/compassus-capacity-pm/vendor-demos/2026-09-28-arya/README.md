# Arya — vendor demo, 28 Sep 2026

Round-two demo against the Vendor Demo Question Guide. Teams recording, 2:03:50 (the call ends at 1:56:27).
Scorecard going in: **84 · Advance · no open stop-checks** (highest in the field).

| File | What it is |
|---|---|
| `index.html` | Visual report: process flow with large screens, question-by-question scoring, considerations, next steps |
| `transcript.md` | Full Teams transcript with speaker labels, timestamped |
| `screens/HHMMSS.jpg` | 45 product screens at full resolution, named by time into the recording. `-d` files are zoomed detail crops of the panel that matters |
| `Arya-Demo-Readout.pdf` | Landscape PDF of the report for sharing. Generated only after the HTML is approved |

## Bottom line

**Hold at Advance.** Arya is an agent, not a workspace. It was the only vendor to run the whole loop live:
- it picks up the referral;
- texts the patient to confirm discharge;
- ranks eligible clinicians with a match score and a suggested time;
- gets office approval (and the clinician's yes by text for part-timers);
- writes the SOC back to HCHB.

Clinicians work with it by text and short links, with no app.

What to test before the on-site:
- **Integration.** Citrix screen automation, 15–20 min reads and about 15 min writes, versus under five minutes in the return.
- **Capacity.** The branch accept/decline view was described but not shown ("we don't have good data").
- **Rules governance.** Free-text rejections become rules, and the tool to see them is still being built.
- **Autonomy.** Approval is framed as a phase; it needs to be a permanent option for each action.

## Scoring (question guide)

Answered 3 · partly 8 · not answered 1 · not asked 5 (10 common + 7 Arya-specific). Detail in `index.html`.

## Method notes

- Screens are cropped to the app, with the browser chrome, dock and participant strip removed. Phone screens are cropped to the phone.
- One frame (0:33:39) showed what looked like another customer's live escalation (a caregiver's name and a patient's initial) in the presenter's inbox. It was removed from the package and is flagged under Considerations.
- The frame picks (`picks.txt`) and crop boxes are reproducible with `.claude/skills/vendor-demo-breakdown/scripts/grab_frames.py`.
