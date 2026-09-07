# Vendor research — session handoff

**Written:** 2026-09-07, end of the third research session
**For:** the next Claude session doing vendor research, and the PM
**Branch:** `claude/vendor-list-bpmnil`. All vendor work is on this branch; none is on `main`.
Check it out first; without it you have no brief, no pack, no roster, no dossiers, no CLAUDE.md.

---

## 1. Where things stand

**Ten dossiers are done, of sixteen returns.** `00-ROSTER.md` is the entry point and is now at
version 2.

| Vendor | File | Confidence | One line |
|---|---|---|---|
| UnityAI | `unity-ai.md` | **high** | Nashville, ex-HCA data scientists, voice agents for outpatient clinics; six named customers, none in home-based care; no EMR named anywhere; $15M raised, ~23 staff |
| CareConnect | `care-connect.md` | **high** | Port Washington NY, Brodsky-owned, aide-shift matching for home care agencies; **their partners page claims an HCHB integration with no mechanism**; no outside funding, ~92 staff |
| servis.ai | `servis-ai.md` | medium | Campbell CA, **FreeAgent CRM renamed**; a horizontal business-operations platform with a healthcare landing page; the scheduler moves *reps* to *customers*; $20M raised, nothing since April 2021 |
| Vitalis Care | `vitalis-care.md` | medium | **VitalisCare Ltd., Jerusalem**; seven small apps bolted onto HCHB for **hospice**; real HCHB integration, one named customer, no funding or headcount found; two mileage figures that disagree |
| AutoMynd | `auto-mynd.md` | medium | Reston VA, unfunded, under ten people; an **AI-first home health EMR** — an HCHB replacement; founder out of Bayada operations; **WellSky OEM deal, April 2026**; scheduler explicitly autonomous |
| CareStitch | `care-stitch.md` | medium | San Diego, **bootstrapped, four employees**; home health scheduling and dispatch, the only vendor that had never repositioned; no customer named anywhere |
| **Axle Health** | `axle-health.md` | **high** | Los Angeles, YC W21, **34 people, $10M Series A May 2025** led by F-Prime; ex-Uber logistics founders; scheduling + real patient engagement; **the best HCHB evidence found anywhere on this roster** |
| **AxisCare** | `axis-care.md` | **high** | Waco TX, **founded 2013**, 51–200 staff, **two institutional investors in 26 months** (Frontier 2024, LLR Jun 2026); a full home **care** operating system — **and Medicare is not on their payer list** |
| **MedArrive** | `med-arrive.md` | medium | Littleton CO (**was New York**); ~$40.5M raised to 2023; **abandoned its field-provider network in 2025**, rebuilt as a logistics platform with ChristianaCare, bought a dead competitor's assets and named a new CEO in March 2026 |
| **Zeeva** | `zeeva-connect.md` | **low** | **One web page and a waitlist.** A marketplace selling *to clinicians*, offering visits across multiple agencies at market rates. No person, place, date, funding, customer or privacy policy published |

The network is on **Full**; pages were read directly. Everything below assumes that.

## 2. The five things the PM should know from this session

1. **“Axel Health” is Axle Health.** No company of the PM's spelling exists in this field. Axle
   Health — Los Angeles, YC W21, $10M Series A — is the only reasonable referent, and the roster now
   carries the correction with a stop condition: **if the return comes from an `axelhealth` domain,
   nothing in the dossier applies.**
2. **Axle Health carries the best A1 evidence on the whole roster, and it is not their sentence.**
   A named person at a named, verifiable Medicare-certified home health agency — Jeff Henderson at
   GrandCare Health Services, Southern California — says on Axle's site: *“Integration with HCHB is
   smooth and the route optimization saves my clinicians time every day.”* That is a rung above
   every other HCHB claim we have seen. Two caveats, both worth raising: **HCHB is absent from
   Axle's own integration logo row on the same page**, and **GrandCare was acquired by The Pennant
   Group in July 2025**, so the reference may have moved.
3. **AxisCare is the wrong payer world, and it is the strongest company here.** Thirteen years old,
   fifty states, seven countries, two institutional investors, sixteen named executives — and
   *“Specializing in Private Pay, Medicaid, and VA Billing.”* **Medicare is not on the list**, no EMR
   appears in their integrations marketplace, and there is no forecast of anything. It is the
   servis.ai trap in a much more respectable suit: a genuinely excellent product for a business that
   is not ours.
4. **MedArrive is a new company inside an old one.** It spent about $40m from 2020 to 2023 running a
   network of paramedics and EMTs visiting homes. In 2025 it *“transitioned away from directly
   providing care.”* Founder-CEO out around October 2025; new CEO from Alto Pharmacy and TytoCare in
   March 2026; assets of the shuttered Inbound Health bought the same day; registered address moved
   from New York to Colorado; website rebuilt in August 2026 with **no customer, no EMR and no human
   being named on it.** Its shape is the closest on the roster to our actual problem — it starts at
   the discharge, upstream of scheduling — and almost none of it can be verified yet.
5. **Zeeva is not selling to us.** It is a waitlist for a marketplace that offers home health visits
   from **multiple agencies** to clinicians, at *“market-driven pay rates”*, with the clinician
   arranging the time *directly with the patient*. Read one way that is a new source of capacity.
   Read the other way it puts our own nurses' marginal hours out to competitive bid and removes the
   scheduler from the middle. **It also has no privacy policy and no terms of service**, which is a
   STOP-CHECK shape on C6, not a Watch.

## 3. The scorecard reads, across all ten

Still nobody has a live HCHB integration we can verify from outside. **Three now claim one**
(CareConnect, Vitalis Care, and Axle Health via its customer), and Axle's is the only one attributed
to a named person at a named agency. **A1 remains unresolved for the whole roster and only a live
walk-through will settle it.**

| Vendor | Scheduling unit | Arena it actually plays in | Posture |
|---|---|---|---|
| UnityAI | A clinic appointment slot | Engagement, real | Engine-led |
| CareConnect | An hourly shift on a case | Caregiver engagement, shift fill | Caregiver self-selects |
| servis.ai | A field rep's visit on a route | None of the three, natively | Human schedules, engine routes |
| Vitalis Care | A hospice visit in a benefit period | Scheduling and compliance | **Recommend and accept** |
| AutoMynd | A visit in an episode | Documentation; scheduling claimed | **Autonomous** |
| CareStitch | A visit for a patient | Scheduling; capacity thin but real | **Recommend and accept** |
| Axle Health | A visit for a patient, in a market | **Scheduling and engagement, both real** | Strong default, clinician may change |
| AxisCare | An hourly shift on a client | Scheduling, wrong payer world | **They say advise; their investor says decide** |
| MedArrive | A visit dispatched from a discharge | Transitions, scheduling; capacity claimed | **Automatic** |
| Zeeva | A visit a clinician chooses to take | A labour market, not one of the three | The clinician decides |

**Impact figures that carry a period, baseline or site count: still 1, now of 46.** The
exception remains AutoMynd's WellSky figure. Axle's Cityblock case study is the closest new
contender — it gives a period, *“the three months following its switch to Axle”* — and still no
baseline. **Zeeva is the only vendor that has published no impact claim at all.**

**Two new contradictions to carry into demos.** AxisCare's own release says the scheduler
*recommends*; its investor's release seven months later says the platform *drives care decisions*.
Axle's site says productivity rises *“17%+”*; its funding release says *“up to 30%”*.

## 4. First job for the next session

1. **Confirm the roster.** Six of sixteen returns are still unresearched. Add each vendor to
   `00-ROSTER.md` with a pinned entity **before** researching.
2. **Settle the HCHB partner list.** HCHB's Recommended Partner brochure is a Figma-exported PDF
   with no text layer, hosted on HubSpot, over the fetch size limit. It is recorded as **gated** in
   three dossiers. Rendering its pages as images and reading them would settle whether CareConnect,
   Vitalis Care **and now Axle Health** appear on HCHB's own list. **This is still the
   highest-value single unread source across the whole roster, and it got more valuable this
   session.**
3. Three other gated sources worth buying or borrowing: **Home Health Line (DecisionHealth)** on
   AutoMynd, the **Israeli corporate registry** on VitalisCare Ltd., and **Home Health Care News**
   (403s to direct fetch) on Axle Health.
4. **One cheap, high-value check nobody has run:** search the Delaware and California registries for
   **Zeeva Connect, Inc.** Nothing was located this session and the entity is recorded as unverified
   rather than nonexistent. A registry hit would give a founding date and an agent address, which is
   currently the entire company-facts picture.

## 5. Then the next vendors

The PM names them. Follow `handoff/10-VENDOR-RESEARCH-BRIEF.md` exactly. Use `axle-health.md` and
`axis-care.md` as the pattern — they are the most complete.

What the second and third sessions learned that the brief still does not say:

- **Read the site directly; do not trust the index.** careconnectmobile.com is a JavaScript site and
  its partner cards do not appear in search results at all. **Fetch the sitemap first**
  (`/sitemap.xml`) and enumerate the pages.
- **Some sites 403 a plain fetcher and serve a browser.** axiscare.com returns 403 to WebFetch and
  200 to `curl` with a normal browser user-agent. **A 403 is not a gated source; try the other
  fetcher before writing *gated*.** businesswire.com and homehealthcarenews.com are genuinely gated.
- **Read the privacy policy.** It gave VitalisCare's legal entity and subprocessors; this session it
  gave **MedArrive's Colorado address, its SOC II claim and its move out of New York**, none of which
  appears on any other page. It is the most under-used page on any vendor site.
- **Read the product documentation, not the landing page.** `servis.ai/docs/scheduler/` settled that
  vendor in one read.
- **Check the raw HTML for placeholder text.** CareStitch's testimonials are Lorem ipsum; AutoMynd's
  sitemap carries Webflow template team pages; **Axle Health's sitemap still carries template blog
  posts about personal budgeting.** All three are evidence about stage, not about product.
- **Read the investor's press release, not only the company's.** LLR's release on AxisCare says the
  platform *drives care decisions*; AxisCare's own release seven months earlier says it
  *recommends*. Investor prose is where the aggressive claim lives.
- **Verify the testimonial.** Axle's HCHB sentence was worth an hour on its own: the person is real,
  the agency is real, the agency is genuinely Medicare-certified home health, the title on the site
  differs slightly from the public record, and the agency was acquired last year. **A testimonial is
  a lead, not a fact, until the person and the company are confirmed to exist.**
- **Count the impact figures.** “N of M figures carry a period, baseline or site count” is still the
  most useful single line for the leader. The roster stands at **1 of 46**.

## 6. The cross-vendor matrix — built, and rebuilt each session

Three outputs, one generator, so the workbook and the page cannot drift apart:

| File | What it is |
|---|---|
| `_research-matrix.gen.py` | Reads the `## At a glance` block out of every `research/*.md`. **Change a dossier and rebuild; never hand-edit an output** |
| `Vendor-Research-Matrix.xlsx` | Facts down, vendors across, the same orientation as the scorecard. Fact column and header frozen, source numbers in cell comments, alternate vendors tinted, *not found* tinted |
| `Vendor-Research-Matrix.html` | The same data as a page, house design, for reading rather than filling in |
| `research/00-FIELD-NOTES.md` | Brief §6 — one line per vendor, the commonplaces, where the field splits |

**The row set.** Twenty-six facts in five bands: company, product, customers, trust and continuity,
the read. The labels in `BANDS` at the top of the generator are the contract with the dossiers —
reword one there without rewording it in every `## At a glance` block and the row silently drops.

**Adding a vendor.** Write the dossier with an `## At a glance` block using the same twenty-six
labels, add the row to `00-ROSTER.md` (**the matrix takes its column order from the numbered rows of
the roster table**), and rebuild. The generator warns about any label a dossier is missing.

**Verification.** The build re-opens the saved workbook and checks every cell against the dossier it
came from, that source numbers travelled into comments, and that no cell is blank. Note for the
house rule: **there are no formulas in this workbook, so pycel has nothing to evaluate** — the check
is cell-by-cell equality instead. Current build: **260 cells, 10 vendors × 26 facts, 79 gaps, 0
blank.** Gaps have risen from 31% to 30% of cells with four more vendors — the field is consistently
this opaque.

It is a separate workbook, not a tab in `Vendor-Scorecard.xlsx`, because the scorecard is
hand-filled and regenerating it would wipe the marks. Keep it that way.

## 7. Brief edits — one done, six pending

From the review of `10-VENDOR-RESEARCH-BRIEF.md` on 2026-09-05:

1. **Done: a vendor roster with fixed slugs.** `research/00-ROSTER.md`, now v2, with identity pins
   and a *names that are not these vendors* section. The brief should point at it.
2. Who reconciles dossier and highlight brief. The reading Claude is forbidden from using anything
   outside the return (`00-START-HERE.md` §4.3); the research brief says the dossier informs A1, A2
   and Durability. Nobody is named to merge them. Proposed: the PM, side by side.
3. Red-flag ids in the §5 watch-list.
4. A one-line rubric for high / medium / low confidence. **In practice:** high means primary pages
   read directly and corroborated by a second source; medium means the company's own claims read
   directly but uncorroborated; low means the company publishes almost nothing.
5. Gated sources written as gated. **Now done in practice** in all ten dossiers — **and add the
   403-is-not-gated rule from §5 above.**
6. A named owner for the field-notes hand-back.
7. Small: table separator rows in the template, a written date and version stamp, a recency window
   on press, a depth cap so dossiers stay comparable.

**New, from these sessions:** add to §4 of the brief, *where to look, in order* — the sitemap, the
privacy policy, the product documentation, the raw HTML, **the investor's press release**, and
**the verification of any named testimonial**.

## 8. Starter prompt for the new session

```
Check out branch claude/vendor-list-bpmnil and work on it.
Read CLAUDE.md, then agents/compassus-capacity-pm/vendor-evaluation/research/00-SESSION-HANDOFF.md
and 00-ROSTER.md, and follow them. Then read handoff/00-START-HERE.md §1–4,
01-INITIATIVE-BRIEF.md and 10-VENDOR-RESEARCH-BRIEF.md. Add the new vendors to the roster with
pinned legal entities first. Then research: <names>. Public sources only, primary pages read
directly, sitemap and privacy policy included, every fact dated and sourced, not found written as
not found, gated written as gated. Do not read the vendor's return first.
Write research/<slug>.md, rebuild the matrix, commit, push.
```

## 9. Working notes

- Commit messages end with the co-author and session trailers; no model identifier in any file.
- The PM's voice preference: plain, professional, no dashboard theatrics. Short declaratives.
  Lead with the finding. Say what to do about a doubt.
- The PM reviews dossiers as they land. Send the file when it is committed, with a one-line
  caption, and give the headline and the scorecard-row reads in the message.
