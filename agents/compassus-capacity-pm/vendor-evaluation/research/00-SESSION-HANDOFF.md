# Vendor research — session handoff

**Written:** 2026-09-05, end of the second research session
**For:** the next Claude session doing vendor research, and the PM
**Branch:** `claude/vendor-list-bpmnil`, fast-forwarded from
`claude/vendor-research-brief-review-tvi3au`. All vendor work is on this branch; none is on `main`.
Check it out first; without it you have no brief, no pack, no roster, no dossiers, no CLAUDE.md.

---

## 1. Where things stand

**Six dossiers are done.** The roster is now a file, `00-ROSTER.md`, and it is the entry point.

| Vendor | File | Confidence | One line |
|---|---|---|---|
| UnityAI | `unity-ai.md` | **high** | Nashville, ex-HCA data scientists, voice agents for outpatient clinics; six named customers, none in home-based care; no EMR named anywhere; $15M raised, ~23 staff |
| CareConnect | `care-connect.md` | **high** | Port Washington NY, Brodsky-owned, aide-shift matching for home care agencies; **their partners page now claims an HCHB integration with no mechanism**; no outside funding, ~92 staff |
| servis.ai | `servis-ai.md` | medium | Campbell CA, **FreeAgent CRM renamed**; a horizontal business-operations platform with a healthcare landing page; the scheduler moves *reps* to *customers*; $20M raised, nothing since April 2021 |
| Vitalis Care | `vitalis-care.md` | medium | **VitalisCare Ltd., Jerusalem**; seven small apps bolted onto HCHB for **hospice**; real HCHB integration, one named customer, no funding or headcount found; two mileage figures that disagree |
| AutoMynd | `auto-mynd.md` | medium | Reston VA, unfunded, under ten people; an **AI-first home health EMR** — an HCHB replacement; founder out of Bayada operations, four home health clinicians on staff; **WellSky OEM deal, April 2026**; scheduler is explicitly autonomous |
| CareStitch | `care-stitch.md` | medium | San Diego, **bootstrapped, four employees**; home health scheduling and dispatch, the only vendor that has never repositioned; no customer named anywhere; ~3,500 lifetime app installs |

The second read of `unity-ai.md` and `care-connect.md` is **done**, and both are raised to high.
The network is on **Full**; pages were read directly this session. Everything below assumes that.

## 2. The five things the PM should know

1. **CareConnect's own partners page names Homecare Homebase.** The first session wrote *not found*;
   that was wrong. The card is a claim with no mechanism, no direction, no frequency, no date and
   no named customer, and there is no HCHB-side listing to check it against. It is **RF-01** and it
   belongs at the top of their demo agenda.
2. **Vitalis Care is a hospice company with a real HCHB integration and no visible corporate
   existence.** No founding date, no headcount, no funding, no investor, no US entity. Its legal
   entity is registered in Jerusalem. It publishes its subprocessors, which is to its credit, and
   one of them is the **OpenAI API**.
3. **AutoMynd wants to replace HCHB, not integrate with it.** That is probably disqualifying on A1
   and it is the most interesting company on the roster anyway: a founder who ran automation at
   Bayada, four home health clinicians on staff, the best-documented security posture of any vendor
   here, and an OEM deal inside WellSky Personal Care. Its scheduler markets itself as
   **autonomous** — "0 manual assignments" — which is the opposite of our settled position.
4. **servis.ai is a CRM.** Read `servis.ai/docs/scheduler/` before the demo. The objects are Rep,
   Customer, Route Planner and Visit Telemetry. There is no episode, no discipline, no
   authorization and no visit frequency in the data model. It is the trap in brief §5, first
   bullet, in its pure form.
5. **CareStitch has four employees and no named customer.** The product is the right shape — it is
   the only one on the roster with a real capacity feature (MAPS forecasts visit volume by region)
   and it has never repositioned. Compassus is about three thousand clinicians. The question is not
   whether they would say yes.

## 3. The scorecard reads, across all six

Nobody has a live HCHB integration we can verify. Two claim one (CareConnect, Vitalis Care) and
neither publishes a mechanism. **A1 is unresolved for the whole roster and only a live walk-through
will settle it.**

| Vendor | Scheduling unit | Arena it actually plays in | Posture |
|---|---|---|---|
| UnityAI | A clinic appointment slot | Engagement, real | Engine-led |
| CareConnect | An hourly shift on a case | Caregiver engagement, shift fill | Caregiver self-selects, coordinator oversees |
| servis.ai | A field rep's visit on a route | None of the three, natively | Human schedules, engine routes |
| Vitalis Care | A hospice visit in a benefit period | Scheduling and compliance | **Recommend and accept** |
| AutoMynd | A visit in an episode | Documentation; scheduling claimed | **Autonomous** |
| CareStitch | A visit for a patient | Scheduling; capacity thin but real | **Recommend and accept** |

**Impact figures that carry a period, baseline or site count: 1 of roughly 30.** The exception is
AutoMynd's WellSky figure — three hours to about one hour per client — which has both ends of the
comparison and still has no period or agency count. Every other number on this roster is a bare
percentage. **Vitalis Care publishes two mileage figures that contradict each other**, 30% on the
site and 55–65% from the CEO on a podcast: **RF-18 before the return is even opened.**

## 4. First job for the next session

1. **Confirm the roster.** More vendors are coming. Add each to `00-ROSTER.md` with a pinned entity
   before researching. Sixteen returned the questionnaire; six are researched.
2. **Settle the HCHB partner list.** HCHB's Recommended Partner brochure is a Figma-exported PDF
   with no text layer, hosted on HubSpot, over the fetch size limit. It could not be read this
   session and is recorded as **gated** in three dossiers. Rendering its pages as images and reading
   them would settle whether CareConnect and Vitalis Care are on HCHB's own list. **This is the
   highest-value single unread source across the whole roster.**
3. Two other gated sources worth buying or borrowing: **Home Health Line (DecisionHealth)** on
   AutoMynd, and the **Israeli corporate registry** on VitalisCare Ltd.

## 5. Then the next vendors

The PM names them. Follow `handoff/10-VENDOR-RESEARCH-BRIEF.md` exactly. Use `auto-mynd.md` and
`care-stitch.md` as the pattern — they are the most complete.

What the second session learned that the brief still does not say:

- **Read the site directly; do not trust the index.** careconnectmobile.com is a JavaScript site
  and its partner and team cards do not appear in search results at all. The reversed HCHB finding
  was invisible to the first session for that reason alone. **Fetch the sitemap first**
  (`/sitemap.xml`) and enumerate the pages; it found AutoMynd's pricing tiers, its unwritten product
  pages and its placeholder team pages in one call.
- **Read the privacy policy.** It gave VitalisCare's legal entity, its country and its subprocessor
  list — including the OpenAI API — when no other page did. It is the most under-used page on any
  vendor site.
- **Read the product documentation, not the landing page.** `servis.ai/docs/scheduler/` settled that
  vendor in one read. A landing page is written for us; documentation is written for a user.
- **Check the raw HTML for placeholder text.** CareStitch's testimonials are Lorem ipsum with
  fictional names; AutoMynd's sitemap still carries Webflow template team pages. Both are real
  evidence about stage, and both are invisible in a rendered summary.
- **Write gated sources as gated.** Now applied throughout. LinkedIn, PitchBook, Crunchbase's
  403-ing pages, Latka's paywall, state and foreign registries, and the HCHB brochure.
- **Count the impact figures.** "N of M figures carry a period, baseline or site count" is still the
  most useful single line for the leader. The roster stands at 1 of ~30.
- **Say what the scheduling unit is**, in one cell, and say which of the three arenas the public
  material actually covers. The table in §3 above is built from those cells.

## 6. The cross-vendor matrix (agreed, not built)

Unchanged from the first handoff. The PM agreed the plan on 2026-09-05 and saw a mock:
https://claude.ai/code/artifact/77f74f83-3084-449d-b165-837522928b1d

- Each dossier gets a short structured header block, about twenty-four fields, above the prose.
- `_research-matrix.gen.py` in `vendor-evaluation/` reads every `research/*.md`, writes
  `Vendor-Research-Matrix.xlsx` (facts down, vendors across, same orientation as the scorecard;
  source numbers in cell comments; *not found* tinted; fact column frozen) and
  `research/00-FIELD-NOTES.md`.
- Separate workbook, not a tab in `Vendor-Scorecard.xlsx`, because the scorecard is hand-filled and
  regenerating it would wipe marks.
- House rules apply: generator not hand edits, verify with pycel, house palette, no charts, plain.

**Do not build it until the PM confirms the row set.** When they do, retrofit all six existing
dossiers with the header block first, then write the generator. The tables in §3 above are a good
first cut at the rows: they are the cells that turned out to matter across six vendors.

## 7. Brief edits — one is done, six pending

From the review of `10-VENDOR-RESEARCH-BRIEF.md` on 2026-09-05:

1. **Done: a vendor roster with fixed slugs.** `research/00-ROSTER.md`, with identity pins and a
   *names that are not these vendors* section. The brief should point at it.
2. Who reconciles dossier and highlight brief. The reading Claude is forbidden from using anything
   outside the return (`00-START-HERE.md` §4.3); the research brief says the dossier informs A1, A2
   and Durability. Nobody is named to merge them. Proposed: the PM, side by side, into the
   Durability and Section A notes.
3. Red-flag ids in the §5 watch-list.
4. A one-line rubric for high / medium / low confidence. **The second session used one in practice:**
   high means primary pages read directly and corroborated; medium means the company's own claims
   read directly but uncorroborated; low means databases and indexing only. Worth writing down.
5. Gated sources written as gated. **Now done in practice** in all six dossiers; write it into the
   brief.
6. A named owner for the field-notes hand-back (a fresh session reading the dossiers).
7. Small: table separator rows in the template, a written date and version stamp, a recency window
   on press, a depth cap so dossiers stay comparable.

**New, from this session:** add to §4 of the brief, *where to look, in order*: the sitemap, the
privacy policy, the product documentation, and the raw HTML. All four earned their place today.

## 8. Starter prompt for the new session

```
Check out branch claude/vendor-list-bpmnil and work on it.
Read CLAUDE.md, then agents/compassus-capacity-pm/vendor-evaluation/research/00-SESSION-HANDOFF.md
and 00-ROSTER.md, and follow them. Then read handoff/00-START-HERE.md §1–4,
01-INITIATIVE-BRIEF.md and 10-VENDOR-RESEARCH-BRIEF.md. Add the new vendors to the roster with
pinned legal entities first. Then research: <names>. Public sources only, primary pages read
directly, sitemap and privacy policy included, every fact dated and sourced, not found written as
not found, gated written as gated. Do not read the vendor's return first.
Write research/<slug>.md, commit, push.
```

## 9. Working notes

- Commit messages end with the co-author and session trailers; no model identifier in any file.
- The PM's voice preference: plain, professional, no dashboard theatrics. Short declaratives.
  Lead with the finding. Say what to do about a doubt.
- The PM reviews dossiers as they land. Send the file when it is committed, with a one-line
  caption, and give the headline and the five scorecard-row reads in the message.
