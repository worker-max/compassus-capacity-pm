# Ledger — repo side

**Written by:** the repo Claude (`worker-max/compassus-capacity-pm`). **I am the only writer of this
file.** The Compassus Claude reads it but never edits it — see
[`../HANDOFF-0-establish-the-channel.md`](../HANDOFF-0-establish-the-channel.md) §2.

**Last sync:** 2026-08-19

`Ver` is the first 6 characters of the file's md5. If a file's current md5 no longer matches the
value here, I read an older version and it needs re-ingesting.

| Drive ID | File | Ver | Read | Disposition | For | Note |
|---|---|---|---|---|---|---|
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
| `ingested` | 20 |
| `staged` — **needs Colin's decision** | 2 |
| unread by anyone | 1 |

## What I am waiting on

1. **The `S-43` ruling.** Two unrelated claims on one code, plus `SH-12`/`S-45` describing the same
   object from two sides. Nothing is written to the workbook yet, so it is still cheap to fix — but
   Handoff 1 Tier A cannot be applied until this is settled.
2. **`Evan _ Colin.docx`** — 452KB, dropped 19 August, unopened by either instance. Whoever reads it
   first should log it and say what it is.

## Repo-owned files in this Drive folder

The nine PDFs marked *repo-owned render* above are generated from `_*.gen.py` in the repository. **The
repo is upstream for those** — regenerate there and republish here. Editing the PDF in Drive puts it
out of sync with its generator, and the librarian will flag it as drift rather than adopt it.
