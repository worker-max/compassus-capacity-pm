# Ledger — repo side

**Written by:** the repo Claude (`worker-max/compassus-capacity-pm`). **I am the only writer of this
file.** The Compassus Claude reads it but never edits it — see
[`../HANDOFF-0-establish-the-channel.md`](../HANDOFF-0-establish-the-channel.md) §2.

**Last sync:** 2026-08-25

`Ver` is the first 6 characters of the file's md5. If a file's current md5 no longer matches the
value here, I read an older version and it needs re-ingesting.

**Rows added 25 Aug carry `size/mtime` instead of an md5.** The Drive tooling available to this side
does not expose md5 without downloading the whole file, so those rows record byte size and modified
time — a weaker fingerprint, but a real one. Re-hash them when the file next passes through a side
that can.

| Drive ID | File | Ver | Read | Disposition | For | Note |
|---|---|---|---|---|---|---|
| (uploaded) | 8.19 Compassus Capacity & Scheduling Workbook.xlsx | 442472/08-19 | 08-25 | ingested | both | **Supersedes the 8.13 workbook.** 87 numbered variables (was 76 + 3 unnumbered); purely additive — zero changes to the existing 76 rows. Adds a populated **Module** column assigning every variable to one of the three arenas. CSV snapshot of all 14 tabs → knowledge/source/workbook-2026-08-19/. Supplied by Colin directly, not via Drive — **confirm which Drive copy is current** |
| 1iuXRbKOrvrQ | Compassus Capacity & Scheduling Vendor Questionnaire.xlsx | 42859/08-21 13:50 | 08-25 | ingested (partial) | both | **The `Overview` tab only** -> knowledge/vendor-questionnaire-overview-2026-08.md. The current vendor-facing one-pager. Other seven tabs summarised, not ingested. Note: its Meta tab still says form_version 2026-08-19 |
| 137YIaYkKXly | Compassus RFP One_Pager.pdf | 148968/08-19 17:44 | 08-25 | superseded | both | One-pager v2, the first vendor-facing rewrite. Superseded 21 Aug by the Overview tab. Logged as the lineage midpoint; not separately ingested |
| 1LnAbz9jXIDj | Questionnaire Feedback (Doc) | 4630/08-20 13:26 | 08-25 | staged | repo | Read. Four of its points landed in the 21 Aug Overview. **The rest are unactioned** - maturity as a scored column, customer counts + top-3 census, measured customer impact, discrete status options. Needs a decision |
| 1-ji7fpnkQmh | Pass Through Material Temp (Doc) | 53876/08-24 15:53 | 08-25 | UNREAD | ? | Skimmed only. Running flow-map corrections from Colin, edited 24 Aug. **Live and likely affects the flow sheets** - read properly next |
| 159-3GQzFbub | CompassusVendorQuestionnaireMASTER 2.0.xlsx | 42880/08-20 14:30 | - | superseded | - | Superseded by the 21 Aug questionnaire |
| 1Xoo926ayT57 | CompassusVendorQuestionnaireMASTER.xlsx | 37646/08-19 18:17 | - | superseded | - | Superseded |
| 1d-SMfjOIqVG | CompassusVendorQuestionnaire.xlsx | 28557/08-19 18:17 | - | superseded | - | Superseded |
| 1lfv3tCgpcVe | Capacity Scheduling Evan Feedback.docx | 16377/08-20 14:29 | - | UNREAD | ? | Merge Tank, from-employer side. Unopened by this side |
| 1tAILpvwtEzL | Business use cases (Doc) | 298150/08-21 20:42 | - | UNREAD | ? | Merge Tank. Unopened by this side |
| 1rx5XCr28qFO | HH Scheduling_Master Project Plan_July 2026.xlsx | 580054/08-21 21:43 | - | UNREAD | ? | Merge Tank. Unopened by this side |
| 1y0X3TLKuG4H | HANDOFF-1-variable-additions.md | f180b0 | 08-19 | staged | repo | Read. Recommends 76 -> 92 variables in tiers A/B/C. Tier A collides with the S-43 reservation. Not applied - needs Colin |
| 1lFw02FQEteL | HANDOFF-2-target-architecture.md | aeb41e | 08-19 | staged | repo | Read. Three-module construct keyed to the inventory; consistent with DE-02. Not applied - depends on the same ID ruling |
| 1c_SFJDmZF_j | Evan _ Colin.docx | 92d203 | - | UNREAD | ? | UNREAD - nobody on either side has opened this |
| 1tVEkPO2FJMF | 8.13 Compassus Capacity & Scheduling Workbook.xlsx | 159dbf | 08-18 | ingested | both | Authoritative, stays in Drive. Index -> knowledge/workbook-2026-08-13.md; CSV snapshot of all 14 tabs in knowledge/source/workbook-2026-08-13/ |
| 1SZDHuYYzkML | 8.13 capacity scheduling swimlane detail.pdf | 9cd450 | 08-18 | ingested | both | The original hand-built map -> artifacts/Source-Original-Swimlane-Detail.pdf |
| 1ElkCTRvJkv5 | 8.13.26 Whiteboard Session Executive Summary and Transcript.docx | 4b32f1 | 08-18 | ingested | both | -> knowledge/whiteboard-session-2026-08-13.md + source/whiteboard-exec-summary-and-part-a-2026-08-13.md |
| 1X-KEBygDws3 | 8.17.26 Bottleneck Identification.docx | 6086a1 | 08-18 | ingested | both | -> knowledge/bottleneck-dossiers.md (12 dossiers) |
| 1xHiWUoZVmBL | 8.17.26 Capacity Scheduling Variable Lists.pdf | ec0ecc | 08-18 | ingested | both | Repo-owned render of artifacts/Capacity-Scheduling-Variable-Reference.pdf |
| 12kNpfOEem62 | 8.17.26 Constraint Register.docx | ce513a | 08-18 | ingested | both | -> knowledge/constraint-register.md (CN-01..CN-51) |
| 1NSHlkaWir6r | 8.17.26 Current State Flow Map Revisions.docx | c78f12 | 08-18 | ingested | both | -> source/flow-clarifying-2026-08-17.md; distilled into knowledge/process-facts-2026-08.md |
| 1_7kh1uX_ru- | 8.18 Full Episode Flow - Current State.pdf | 43bfd9 | 08-18 | ingested | both | Repo-owned render of artifacts/Primary-Flow-Map.pdf |
| 1bv2iOHAQUbt | 8.18 Full SOC_ROC Flow Updated - Current State.pdf | 767d60 | 08-18 | ingested | both | Repo-owned render of artifacts/Detailed-Flow-Composite.pdf |
| 1Er-XhCgtRDb | 8.18 HAND OFF DOCUMENT FOR PAYER AND HH EPISODE ECONOMICS.docx | 807660 | 08-18 | ingested | both | -> knowledge/payer-and-episode-economics.md. Proposes SH-10..SH-14 + S-43; S-43 contested |
| 19JBJ1zQ0sZR | 8.18 Recert and DIscharge Flow - Current State.pdf | d12f88 | 08-18 | ingested | both | Repo-owned render of artifacts/Flow-Recert-Discharge.pdf |
| 1075tGPK9KQX | 8.18.26 Auth Flow Process within Capacity and Scheduling Map - Current State.pdf | 9b1933 | 08-18 | ingested | both | Repo-owned render of artifacts/Flow-Authorization.pdf |
| 1LrxdSrd5VNS | 8.18.26 DCS and Scheduler Flow Map - Current State.pdf | aac44a | 08-18 | ingested | both | Repo-owned render of artifacts/Flow-DCS-Scheduler.pdf |
| 1s0lmYmKa6mR | 8.18.26 Routine Clinician Visit Flow Map.pdf | bc6cf3 | 08-18 | ingested | both | Repo-owned render of artifacts/Flow-Routine-Visits.pdf |
| 1nRLnwWnj-ql | Capacity Scheduling One Pager 8.17.26.pdf | e92aa6 | 08-18 | ingested | both | Repo-owned render of artifacts/Capacity-Scheduling-One-Pager.pdf |
| 1nIzfzDMTlCI | Nurse Scheduling Day-in-the-Life.pdf | 1633a6 | 08-18 | ingested | both | -> artifacts/Scenario-Clinician-Day-In-The-Life.pdf. Illustrative |
| 1ADmFLii4xIg | Nurse Territory Reviews.pdf | 6280a6 | 08-18 | ingested | both | -> artifacts/Scenario-Branch-Leader-Territory-Review.pdf. Illustrative |
| 1YJcfDe_nnyf | SCHEDULING INITIATIVE WHITEBOARD SESSION.docx | f37e54 | 08-18 | ingested | both | Raw transcript. Re-numbered -> source/transcript-lines-2026-08-13.txt so every [T:###] citation resolves |
| 10Nahc3qcv6h | capacity_scheduling_elemental.pdf | 4e94c9 | 08-18 | ingested | both | -> artifacts/Capacity-Scheduling-Elemental.pdf. Earlier six-category framing |
| 1Er6moqHI9-E | scheduler_recovery with RN Call-Out Flow.pdf | ab947b | 08-18 | ingested | both | -> artifacts/Scenario-Scheduler-Callout-Recovery.pdf. Illustrative |

## Summary

| Disposition | Count |
|---|---:|
| `ingested` | 21 + 1 partial (the questionnaire `Overview` tab) |
| `staged` — **needs Colin's decision** | 3 |
| `superseded` — logged, no action | 4 |
| unread by this side | 5 |

## What I am waiting on

1. **What Engagement means.** Arena names in the variable workbook are the Module column's own,
   with one change: **"Patient Engagement" → "Engagement"** (Colin, 25 Aug). "Scheduling Engine"
   stays for now, by his call. The rename is not cosmetic — the old label actively misleads:
   engagement is the contact work that
   turns a schedule into delivered visits *whoever it is with*: office to clinician, clinician back
   to the office, clinician to clinician, care team to each other, as well as patient and caregiver.
   Finding coverage for a call-out is engagement. The one-pager already has this right — "with
   patients, clinicians and the office" — the workbook label does not.

2. **Write Colin's 25 Aug coordination ruling back to the workbook.** `CO-09`–`CO-12` (call-out
   coverage, multi-discipline coordination, care-team updates, coordination time load) are
   **engagement**, not scheduling: all four are carried by contact with a patient or a clinician.
   The 19 Aug workbook's Module column still has them under Scheduling Engine. The variable
   workbook carries the ruling and flags the divergence on every affected row; **the workbook is
   upstream and has to be updated for real**, or the two drift apart. Ruled by Colin, 25 Aug.
3. **The one-pager's ownership.** The vendor-facing one-pager is now edited inside the questionnaire
   workbook, which this side cannot regenerate — so the "repo is upstream for the one-pager" rule in
   DRIVE-INDEX no longer holds. Three options and a recommendation are laid out in
   `knowledge/vendor-questionnaire-overview-2026-08.md` §4. **Needs Colin.**
4. ~~**The `S-43` ruling.**~~ **CLOSED 25 Aug.** The 19 Aug workbook ruled: `S-43` Insurance
   Authorization, `S-44` Add-On Orders, `S-45` Clinician Safety, with consent/POA landing as `S-47`
   and `CO-14`. The reservations in `artifacts/variable-backlog.md` were overridden; that file now
   carries the ruling. **What replaces it:** `SH-10`–`SH-14` were *not* adopted, so the payer
   dimension — payer class, pending-auth allowance, payment period, LUPA threshold — is still
   missing from the inventory entirely. Needs Colin.
5. **`Evan _ Colin.docx`** — 452KB, dropped 19 August, unopened by either instance. Whoever reads it
   first should log it and say what it is.
6. **`Pass Through Material Temp`** — Colin's running flow-map corrections, last edited 24 August and
   still live. Read properly before the next flow-sheet regeneration; the corrections in it are not
   yet in `process-facts-2026-08.md`.

## Repo-owned files in this Drive folder

The nine PDFs marked *repo-owned render* above are generated from `_*.gen.py` in the repository. **The
repo is upstream for those** — regenerate there and republish here. Editing the PDF in Drive puts it
out of sync with its generator, and the librarian will flag it as drift rather than adopt it.

**One exception, as of 21 Aug: the one-pager.** `Capacity Scheduling One Pager 8.17.26.pdf` is still a
repo-owned render, but it is now the *internal* version. The **vendor-facing** one-pager was rewritten
outside the repo and now lives as the `Overview` tab of the vendor questionnaire — the repo has no
generator for it, so for that page **Drive is upstream and this side ingests.** Do not "correct" the
drift by regenerating; see `knowledge/vendor-questionnaire-overview-2026-08.md` §4.
