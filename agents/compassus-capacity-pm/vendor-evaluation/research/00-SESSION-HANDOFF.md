# Vendor research — session handoff

**Written:** 2026-09-05, end of the first research session
**For:** the next Claude session doing vendor research, and the PM
**Branch:** `claude/vendor-research-brief-review-tvi3au`. Nothing vendor-related is on `main`.
Check this branch out first; without it you have no brief, no pack, no dossiers, no CLAUDE.md.

---

## 1. Where things stand

Two of about ten dossiers are done, committed and pushed:

| Vendor | File | Confidence | One line |
|---|---|---|---|
| UnityAI | `unity-ai.md` | medium | Nashville, ex-HCA data scientists, voice agents for outpatient clinics; no home health, no HCHB, voice layer on Vapi, $15M raised, ~22 staff |
| CareConnect | `care-connect.md` | medium | Port Washington NY, Brodsky-owned (Sandata founder), aide-shift matching for home care agencies; no skilled home health customer named, no HCHB, integrations are SSO, no outside funding, ~92 staff |

Both were written **before** reading the vendor's return, per brief rule 7. Neither has had its
second pass.

Both are medium confidence for one reason: the session that wrote them could not open any web page
directly. Its cloud environment was on the **Trusted** network level, which blocks vendor sites,
trade press, HCHB partner pages, app stores and job boards. Every fact came from search-engine
indexing, cross-checked across outlets. The PM has since set the Default environment to **Full**.
A session started after that change reads pages directly.

## 2. First job for the new session

Before the third vendor, spend twenty minutes upgrading the two existing dossiers:

- **UnityAI.** Re-read sources 1, 4, 8, 13 and 20 in full (vendor site, Series A release, Fierce
  scheduling-agents article, Peregrine release, Rippling job board). Confirm the "22 employees"
  figure, the four-agent metrics, and whether any EMR is named anywhere on the site. Look for a
  trust or security page and an uptime figure. Raise confidence to high if nothing contradicts.
- **CareConnect.** Read careconnectmobile.com/team (leadership names, any CTO), /partners (full
  list and any integration detail), and the HHAeXchange Partner Connect page. Open the StatusGator
  page and settle whether it is this company. Open the Google Play and App Store listings for the
  current rating and count. Raise confidence to high if nothing contradicts.

Add a dated line under *Confidence note* in each saying what the second read changed.

## 3. Then the next vendor

The PM names the vendor. Follow `handoff/10-VENDOR-RESEARCH-BRIEF.md` exactly. Use the two
existing dossiers as the pattern, including the tables with header separator rows, the *not found*
list and the numbered sources with dates.

Things learned in the first session that the brief does not yet say:

- **Check identity first.** "Care Connect" matched five companies. Pin the legal entity, site and
  address before researching, write an *Identity* paragraph under the header, and tell the PM to
  confirm against the return's contact email domain.
- **Slug is the company's own spelling, lowercased, hyphenated:** `unity-ai`, `care-connect`.
- **Look for the founder's other companies.** CareConnect's "partnerships" were mostly with sister
  companies. Ownership explains a partner list.
- **Cite red-flag ids in the outside-view section** (RF-01, RF-03, RF-05, RF-07, RF-12, RF-16,
  RF-18 came up for both vendors). The catalogue is `handoff/07-RED-FLAGS.md`.
- **Gated sources are written as gated, not as not found:** LinkedIn, PitchBook, Crunchbase, Axios
  Pro, state registries behind a search form. Headcount trend and valuation will usually stay open.
- **Count the impact figures.** "N of M figures carry a period, baseline or site count" is the most
  useful single line for the leader. Both vendors so far are 0 of N.
- **Map the product to the three arenas in one cell**, and say what the scheduling unit is (a
  visit in an episode, a shift on a case, a clinic slot). Both vendors so far are not visit-based.

## 4. The cross-vendor matrix (agreed, not built)

The PM agreed the plan on 2026-09-05 and saw a mock:
https://claude.ai/code/artifact/77f74f83-3084-449d-b165-837522928b1d

- Each dossier gets a short structured header block, about twenty-four fields, above the prose.
- `_research-matrix.gen.py` in `vendor-evaluation/` reads every `research/*.md`, writes
  `Vendor-Research-Matrix.xlsx` (facts down, vendors across, same orientation as the scorecard;
  source numbers in cell comments; *not found* tinted; fact column frozen) and
  `research/00-FIELD-NOTES.md` (one line per vendor, the disagreements, the commonplaces).
- Separate workbook, not a tab in `Vendor-Scorecard.xlsx`, because the scorecard is hand-filled
  and regenerating it would wipe marks.
- Rows in the mock are a first cut. The PM has not yet confirmed or edited them.
- House rules apply: generator not hand edits, verify with pycel, house palette, no charts, plain.

Do not build it until the PM confirms the row set. When they do, retrofit `unity-ai.md` and
`care-connect.md` with the header block first, then write the generator.

## 5. Brief edits still pending

From the review of `10-VENDOR-RESEARCH-BRIEF.md` on 2026-09-05, not yet applied. The PM has seen
the list and not yet said which to take:

1. Who reconciles dossier and highlight brief. The reading Claude is forbidden from using anything
   outside the return (`00-START-HERE.md` §4.3); the research brief says the dossier informs A1,
   A2 and Durability. Nobody is named to merge them. Proposed: the PM, side by side, into the
   Durability and Section A notes.
2. A vendor roster with fixed slugs (`research/00-ROSTER.md`).
3. Red-flag ids in the §5 watch-list.
4. A one-line rubric for high / medium / low confidence.
5. Gated sources written as gated.
6. A named owner for the field-notes hand-back (a fresh session reading the dossiers).
7. Small: table separator rows in the template, a written date and version stamp, a recency window
   on press, a depth cap so dossiers stay comparable.

## 6. Starter prompt for the new session

```
Check out branch claude/vendor-research-brief-review-tvi3au and work on it.
Read CLAUDE.md, then agents/compassus-capacity-pm/vendor-evaluation/research/00-SESSION-HANDOFF.md
and follow it. Then read handoff/00-START-HERE.md §1–4, 01-INITIATIVE-BRIEF.md and
10-VENDOR-RESEARCH-BRIEF.md. Do the second-read upgrade of unity-ai.md and care-connect.md
first. Then research the next vendor: <name>. Public sources only, primary pages read
directly, every fact dated and sourced, not found written as not found, gated written as
gated. Do not read the vendor's return first. Write research/<slug>.md, commit, push.
```

## 7. Working notes

- Commit messages end with the co-author and session trailers; no model identifier in any file.
- The PM's voice preference: plain, professional, no dashboard theatrics. Short declaratives.
  Lead with the finding. Say what to do about a doubt.
- The PM reviews dossiers as they land. Send the file when it is committed, with a one-line
  caption, and give the headline and the five scorecard-row reads in the message.
