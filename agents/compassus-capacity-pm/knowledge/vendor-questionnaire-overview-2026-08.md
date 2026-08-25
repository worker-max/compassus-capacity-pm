# The Vendor-Facing One-Pager — Questionnaire `Overview` Tab

> **Source of truth for this document:** the **`Overview`** tab (sheet 3 of 8) of
> `Compassus Capacity & Scheduling Vendor Questionnaire.xlsx` — Google Drive
> `1iuXRbKOrvrQa4lKWyDw92t_ziIx0ZEqD`, folder `1RPI1ogTdyDeEf64OBRmaRQ0ESNWp5k5o`.
> Modified **21 Aug 2026 13:50 UTC**, 42,859 bytes. Ingested 25 Aug 2026.
>
> **This is the current one-pager.** It supersedes both earlier renders. It is the version vendors
> actually read, and it is **employer-owned upstream** — it lives in the workbook, not in this repo.
> Do not treat `../artifacts/Capacity-Scheduling-One-Pager.pdf` as current; see §4.

## 1. Lineage — three versions, in order

| # | Artifact | Drive ID | Date | What it is |
|---|---|---|---|---|
| 1 | `Capacity Scheduling One Pager 8.17.26.pdf` | `1nRLnwWnj-ql…` | 17 Aug | **Internal.** Numbered variable names + counts (`01 Staff supply…`, "22 variables in full"). Repo-owned render of `../artifacts/Capacity-Scheduling-One-Pager.pdf` (md5 `e92aa6…`, 136,900 bytes — repo and Drive copies identical) |
| 2 | `Compassus RFP One_Pager.pdf` | `137YIaYkKXly…` | 19 Aug | **First vendor-facing edit.** Codes and counts stripped, replaced with plain-language explanation; ten named group headers introduced; opens "What we are looking to build", closes with the platform ask. 148,968 bytes |
| 3 | **`Overview` tab, questionnaire workbook** | `1iuXRbKOrvrQa4lKWyDw92t_ziIx0ZEqD` | 21 Aug | **Current.** Version 2 rebuilt as a spreadsheet tab inside the questionnaire, plus four substantive additions answering the 20 Aug review (§3) |

The 17 Aug version is an *inventory*; from 19 Aug onward it is an *ask*. That is the point of the
rewrite: a vendor reading it should be able to answer Part B without ever seeing the numbered
variable inventory.

## 2. The one-pager, as it now reads

**Header:** COMPASSUS · HOME HEALTH — Capacity & Scheduling
**Standfirst:** *What we are looking to build. Three connected capabilities decide whether a referral
becomes a delivered visit — and a platform has to serve all three.*

The two right-hand arenas sit inside a shaded **COORDINATION** zone, as in every other artifact.

### THE ENVELOPE · Capacity Management
*How much work a branch can deliver, and how much room is left.*

- **Workforce supply** — *Who we have, and what each of them is qualified to do.*
  - Roster by discipline, role (assessing vs. assistant), FTE and employment type
  - Start-of-care capable clinicians, measured as their own distinct capacity
  - Specialty competencies, plus orientation and ramp status
  - Per-diem and float pool
  - On-call and weekend rotation load
- **Availability & reach** — *When each clinician works, and where they can actually get to.*
  - Approved time off and working availability
  - Clinician territory assignment by zip, against branch coverage area
  - Reachability from the clinician's home base, measured by drive time
- **The capacity math** — *What is committed, what is open, and what is arriving.*
  - Visit weighting — the point value per visit type, and the productivity target and ceiling it is measured against
  - Committed load vs. open room, by day, week, discipline and territory
  - Referral inflow and discharge outflow against the envelope

### FILLING THE ENVELOPE · Scheduling Engine
*Which clinician, which day, which route.*

- **Demand** — *Everything the engine must know about what has been ordered.*
  - Plan-of-care orders, ordered frequency and visit types, from the EMR (Home Care Home Base) and the intake platform
  - Authorization status and payer rules attached to each visit
  - Order, consent and readiness state — what is schedulable, not merely ordered
  - The compliance window each visit has to fall inside
- **Matching** — *Putting the right clinician with the right patient.*
  - Discipline and role match, specialty competency, acuity to skill level
  - Clinician working pattern, needs and restrictions
  - Patient and caregiver needs, restrictions and availability, sourced from the patient
  - Clinical timing — diagnosis-driven cadence, competing appointments, infection-control sequencing
  - Continuity of care, and supervisory visit dependencies
- **Routing & the week** — *A day that works, inside a week that holds.*
  - Home base start and end, route proximity, mileage
  - Appointment time windows and intra-day sequencing
  - Front-loading, pace against the plan of care, day-by-day balancing
- **Exceptions** — *What happens when the plan breaks.*
  - Missed-visit management and tracking — and reducing the occurrence
  - Reassignment, coverage, and rebooking inside the window

### MAKING IT HAPPEN · Engagement
*Turning a schedule into delivered visits — with patients, clinicians and the office.*

- **How this should run** — *Our expectation of the platform, not of our staff.*
  - Outreach carried by the platform itself — agentic voice, text and email — rather than queued up for a coordinator to work
  - Staff able to see it, intervene, override, and take any conversation back
- **Before the visit** — *Securing the visit before the clinician drives.*
  - New-patient welcome call
  - Patient availability captured before the visit is booked
  - Automated reminders and en-route notification
  - The day-before confirmation round automated for every patient, every day
  - The schedule staying pliable until that confirmation, so clinician and capacity changes can land before the patient is told
  - Channel and communication-preference management
- **When plans change** — *Recovering a visit rather than losing it — with the patient and the clinician.*
  - Reschedule coordination with the patient
  - Coverage coordination — matching potential clinicians to an open need, and reaching them directly
  - Call-out coverage, and the urgent or prioritized needs that surface during the day
  - Incentives or differentials attached to hard-to-fill visits, and offered to the clinicians who can take them
  - Failed-visit and no-show follow-up and rebooking
- **Across the care team** — *Keeping clinicians and the office on the same schedule.*
  - Multi-discipline visit coordination
  - Care-team and office coordination updates
  - A clinician view of their own schedule and their own results — the case for the change, made to the person it lands on
  - The staff time coordination consumes today

**Closing line:** *Capacity sets the envelope. Scheduling and engagement are both performed against
it — which is why we are looking for a platform that treats all three as one system.*

## 3. What changed on 21 Aug, and why it matters

Four additions, each traceable to a specific point in the 20 Aug review
(`Questionnaire Feedback`, Drive `1LnAbz9jXIDjbS0TTBB1hqgmEHsvrBAxYalCUu3ovKWQ`). **These are new
commitments, not rewording** — they change what we are asking vendors to be.

| Addition | Where | The review point it answers |
|---|---|---|
| **"How this should run"** — the whole block. Outreach carried by the platform (agentic voice, text, email), not queued for a coordinator; staff can see, intervene, override, take the conversation back | Engagement, first block | *"We should make clear somewhere that we expect patient engagement to be largely automated by the platform (e.g. agentic voice, text, email)"* |
| **"The schedule staying pliable until that confirmation, so clinician and capacity changes can land before the patient is told"** | Before the visit | *"Shouldn't we be able to schedule visits days or weeks in advance, and use automated outreach to do confirmations and manage churn?"* — reframes the day-before round from a manual chore to be automated into a **deliberate late-binding commit point** |
| **"Incentives or differentials attached to hard-to-fill visits, and offered to the clinicians who can take them"** | When plans change | *"Should we call out the idea on 'surge pricing' or clinician incentives for more challenging visits?"* |
| **"A clinician view of their own schedule and their own results — the case for the change, made to the person it lands on"** | Across the care team | *"having a dashboard for clinicians… demonstrates the benefits to them (e.g. X% increased points over Y period)… will be important"* for adoption / change management |

The 19 Aug PDF (version 2) contains **none of these four.** That is the cleanest test of which version
someone is holding.

## 4. The repo is now behind — a decision, not a bug

`../artifacts/capacity-scheduling-one-pager.html` and its render
`../artifacts/Capacity-Scheduling-One-Pager.pdf` still produce **version 1** — the internal,
numbered-variable page. Nothing in this repo can generate versions 2 or 3; they were built outside it.

So the ownership rule in [`DRIVE-INDEX.md`](./DRIVE-INDEX.md) ("the repo is upstream for the flow
sheets and the one-pager") **no longer holds for the one-pager.** Three options, for Colin to pick:

1. **Split them.** Keep version 1 as the internal variable view (repo-owned, unchanged) and treat the
   vendor one-pager as employer-owned upstream, ingested here as this file. *Lowest effort; the risk
   is two documents with the same name drifting apart.*
2. **Bring it home.** Write a generator for version 3 in `../artifacts/` so the repo can re-render the
   vendor page. *Restores the rule; costs a build and creates a second place the wording can change.*
3. **Retire version 1.** Mark the numbered one-pager superseded and point everything at the Overview
   tab. *Cleanest, but loses the only page that maps the model to the variable IDs.*

**Recommendation: option 1 for now, option 2 if the one-pager gets re-published as a standalone PDF
again.** The wording is currently being edited inside the questionnaire by the people who own the
vendor conversation; a repo generator would compete with that.

## 5. The workbook this tab lives in

Ingested for context only — **the questionnaire itself is not fully ingested.** Eight tabs:

`Instructions` · `Questionnaire` · **`Overview`** · `Lists` · `Coverage — Expanded` ·
`Additional Questions` · `Vetting — For Leaders` · `Meta`

Two things worth carrying forward:

- **Part B is keyed to this one-pager.** The coverage grid's eleven areas are the Overview's own group
  headers, name for name: Workforce supply · Availability & reach · The capacity math / Demand ·
  Matching · Routing & the week · Exceptions / Before the visit · When plans change ·
  **Incentives & offers** · Across the care team. The only structural difference is that Part B breaks
  incentives out as its own scored row, where the Overview carries it as a bullet under *When plans
  change*. The Instructions tab tells vendors to read the Overview first, and Part B repeats it.
  **If the Overview's group headers change, Part B breaks.**
- **`Meta` says `form_version = 2026-08-19`** while the file was modified 21 Aug. The version stamp
  was not bumped with the four additions above. Worth fixing before the workbook goes out, so a
  returned questionnaire can be matched to the version the vendor actually answered.

## 6. What this does not change

The numbered variable inventory in the 8.13 workbook is untouched by any of this — the one-pager
deliberately does not expose it. The `S-43` collision flagged in
[`payer-and-episode-economics.md`](./payer-and-episode-economics.md) is still open and still gates
Handoff 1. Nothing here resolves it.
