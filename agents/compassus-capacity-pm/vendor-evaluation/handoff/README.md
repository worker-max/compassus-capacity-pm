# Vendor highlights — handoff pack

A self-contained pack that makes a separate Claude an expert on the Compassus capacity &
scheduling initiative, the vendor questionnaire, and the scorecard, so it can read each returned
questionnaire and surface the red flags, the intangible gold, and the questions to go and ask.

**Start with `00-START-HERE.md`.** It carries the reading order, the leader's rules and the guardrails.

## Loading it

- **claude.ai Project (recommended for the PM and the leader):** upload every `.md` file and
  `spec-elements.json` as project knowledge. Put the six-line pointer from `00-START-HERE.md` §6 in
  the project instructions. One conversation per vendor; hand it the transcript or the xlsx.
- **Claude Code:** point a session at this folder and say *read 00-START-HERE.md and follow it*.
- **Drive:** the folder is published to `Merge Tank Folder/from-repo/` for the Compassus Claude, per
  the librarian convention.

## Keeping it in sync

`02-QUESTIONNAIRE.md`, `03-SCORECARD.md` and `09-CALIBRATION.md` are generated. After any change to
the scorecard generator or the form, from the parent folder:

    python3 _handoff.gen.py

The other files are written by hand. `HOUSE-RULES.md` is the PM's and is never regenerated.

## The extractor

    python3 extract_return.py "Vendor - Questionnaire.xlsx" vendor.md

Produces the flat transcript the reading Claude works from, with an appendix of anything in the file
that did not map to a question.
