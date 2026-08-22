# The Initiative Onset Playbook

**How the Compassus Home Health Capacity & Scheduling initiative was worked from a blank page to a
vendor questionnaire — and the procedure to repeat it on the next initiative.**

> **What this is.** A step-by-step record of *how we worked the problem*, converted into a reusable
> process and procedure. It covers the onset only: from the moment the problem was named to the
> moment a structured questionnaire went to the market. It stops where the
> [initiative playbook](../agents/compassus-capacity-pm/initiative-playbook.md) picks up — pilot,
> scale, sustain.
>
> **Who it is for.** The next person at Compassus Operational Excellence who is handed a large,
> cross-functional, technology-adjacent operational problem and a blank page. Read Part I for the
> shape, work Part II stage by stage, and lift Part V wholesale.
>
> **Its authority.** Everything in Part II happened. Dates, artifacts, decisions and people are
> real and traceable to the sources named in each stage. Part V is the generalisation — the same
> steps with the Compassus specifics stripped out.
>
> **House anchor.** This entire arc is **one phase** — *Discovery* — of
> `HH Scheduling_Master Project Plan_July 2026.xlsx`
> ([Drive](https://docs.google.com/spreadsheets/d/1rx5XCr28qFOALEO4xiLxOG5mxPcPAhnK/edit)). Six
> phases remain after it. Section 11 maps every deliverable below onto that workbook's own
> vocabulary so the two never drift apart.

---

## Part I — Orientation

### 1. The situation we were handed

The presenting complaint was **"scheduling is broken."** Clinicians said their schedules were a
mess. Branch leaders said they could not grow. Schedulers were drowning. A prior attempt — HCHB's
Smart Scheduling, piloted in Alabama — had already failed. There was budget appetite, executive
sponsorship, and a live vendor conversation with six or seven companies.

There was also a trap. The obvious move was to write a requirements list for a scheduling tool and
send it out. Had we done that, we would have bought a scheduling optimiser for a problem that is
not a scheduling problem, and repeated Alabama at national scale.

**The single most valuable thing this initiative did was refuse to accept the presented problem
statement until it had been tested.** Everything in Part II is downstream of that refusal.

### 2. The arc, in nine stages

```
  0  FRAME          Test the presented problem before accepting it
  1  DISCOVER       Get the process out of people's heads
  2  VALIDATE       Check the narrative against the system of record
  3  STRUCTURE      Turn narrative into registers with IDs
  4  VISUALISE      Draw current state until the room stops correcting it
  5  ECONOMICS      Learn how the money actually works
  6  BUSINESS CASE  Size it in the house format, honestly
  7  ARCHITECT      Decide the target-state shape and the automation posture
  8  MARKET         One-pager → questionnaire → structured comparison
```

Stages 0–4 answer *what is true.* Stage 5–6 answer *what it is worth.* Stages 7–8 answer *what we
should buy or build.* **Do not run them out of order.** The failure mode of every initiative like
this is starting at stage 8.

### 3. The timeline it actually took

Five weeks end to end, with a nine-day sprint doing most of the work once the on-site session
unlocked it.

| When | What happened | Stage |
|---|---|---|
| Jul 2026 | Full-day cross-functional discovery session; operator SME download; capacity strategy foundation; SME discovery framework and five persona briefs; ecosystem coverage scan; master document assembled | 0–1 |
| 24 Jul | Scheduler insight session agenda and question bank drafted | 1 |
| 11–12 Aug | Illustrative scenario set built from the variable model — day-in-the-life, call-out recovery, territory review | 4 (rehearsal) |
| **13 Aug** | **On-site whiteboard session.** Decisions DE-01…DE-10. Companion workbook with 14 tabs and 79 scored variables | 2, 7 |
| 17 Aug | Constraint register (CN-01…CN-51); twelve bottleneck dossiers; flow-map revision document; one-pager and variable reference published | 3 |
| 18 Aug | Current-state flow mapping completed — seven sheets; entire Drive working folder ingested and indexed | 4 |
| 19 Aug | Payer and episode economics reference plus sourced research corpus; **RFP one-pager**; vendor questionnaire v1 and MASTER | 5, 8 |
| 20 Aug | Executive feedback on the questionnaire; **MASTER 2.0** issued | 8 |
| 21 Aug | **Business case register**; house business-case format captured; master project plan surfaced | 6 |

**Read the shape, not the speed.** The nine days from 13 to 21 August were fast because the five
weeks before them had already built the vocabulary, the relationships and the artifact discipline
the sprint ran on. An initiative that tries to compress stages 0–1 pays for it in stage 8, when the
questionnaire asks the wrong questions and nobody notices for a quarter.

### 4. The seven rules that governed everything

These were not written down at the start. They emerged, and they are the transferable part.

**R1 — Separate the vendor's constraint from the regulator's constraint.**
The organising discipline of the whole initiative. Several of the most painful things about the
current process are Home Care Home Base design choices, not Medicare requirements: routing every
physician order to a DCS for approval; hiding pending-auth visits from the clinician's calendar;
blocking a nurse from handing a visit to her own LPN. Of 51 catalogued constraints, **nine cannot be
toggled — and those nine are the entire case for building something.** Four of the loudest
complaints turned out to be Compassus's own policy and needed no new system at all. Sort your
constraints this way early; it tells you what you are actually buying.

**R2 — The last visible touchpoint gets the blame.**
Schedulers were blamed for delays that originate in clinical documentation, DCS review queues and
authorization holds. Ask "where does this actually get stuck?" and follow it upstream until the
answer stops moving. Whoever is closest to the customer at the point of failure is rarely the cause.

**R3 — Some workflows should not be automated. They should not exist.**
Said in the room on 13 August: *"That workflow shouldn't exist to begin with for the scheduler."*
Before specifying automation for a task, ask whether the task is legitimate. The per-discipline task
explosion — eight clicks for one decision already made — is not an automation opportunity. It is
waste to delete.

**R4 — If you cannot see it, you cannot plan it.**
Pending-auth visits exist nowhere a clinician or leader can see and count toward nothing. A visit
appears on Thursday's calendar on Wednesday afternoon because a scheduler was holding it on a sticky
note. The first product job was never optimisation; it was **making capacity observable.** Phase 1
is visualisation only (DE-03).

**R5 — Change management is the risk. Technology is not.**
Alabama did not fail on technology. Leaders constrained the system to mirror the manual process,
clinicians rejected the optimised assignments, leadership permitted the rejection, and the smart
logic was effectively pulled out of Smart Scheduling. **It was never truly piloted.** Every design
decision after that finding was tested against "would this survive contact with a tenured clinician
who does not want it?"

**R6 — Write down what you decided, and what you deliberately did not decide.**
Ten decisions (DE-01…DE-10) were registered from one session. So were the deferrals: no future-state
map yet, no deep auth-side mapping, no weekend or after-hours path, no aide/MSW/ST scheduling paths.
A deferral you recorded is a scope boundary. A deferral you did not record is a surprise in month
four.

**R7 — Name the authoritative source for every fact, and never let a copy outrank it.**
The workbook is authoritative for variables. The repository is authoritative for flow sheets — they
are generated from scripts, published to Drive, and the published PDF is never edited. Every
knowledge document carries its Drive ID and a rule about which direction changes flow. This sounds
like housekeeping. It is what let a nine-day sprint run without anyone re-litigating a number.

---

## Part II — The stages, as executed

Each stage carries the same six headings. **What we did** is history. **The procedure** is the
transferable version — run that on your initiative.

---

### Stage 0 — Frame: test the presented problem before accepting it

**Purpose.** Establish whether the problem you have been handed is the problem you have.

**What we did.**

We took the presented problem — "scheduling is broken" — and ran a full day of cross-functional
discovery *specifically to test it*, with scheduling operations leaders, clinical staff and
technology/data analysts in one room. The finding reframed the entire initiative:

> **The scheduling problem is not a scheduling problem.** Schedulers are administrators, not
> schedulers. Their only true scheduling decision is the start-of-care intake call. Everything else
> is receiving workflow tasks, clicking pre-plotted visit blocks, and clearing notifications.

Two consequences followed immediately, and both changed what we would go on to buy:

1. **Capacity and scheduling are two functions, not one.** Capacity is a planning function on a
   horizon of weeks — what can this branch absorb. Scheduling is an execution function on a horizon
   of hours — who goes where. Different owners, different inputs, different failure signatures. They
   were being run through **the same artifact** — a manually maintained spreadsheet grid — so
   neither was performed well.
2. **Capacity has to be solved first.** A scheduling optimiser built on an unmeasured capacity
   foundation is exactly what failed in Alabama.

**Deliverable.** A written problem statement that differs from the one you were given, with the
evidence for the difference. Ours became the Executive Summary of the discovery session record.

**Exit test.** Can you state, in one sentence, what the real problem is — and does at least one
senior person who briefed you find that sentence surprising? If nobody is surprised, you have not
finished stage 0.

**The procedure.**

1. Write down the presented problem verbatim, with attribution. You will need it later to show what
   changed.
2. Convene one cross-functional working session — operations, clinical, technology/data, and
   whoever actually does the work. Not a steering committee. The people whose hands are on it.
3. Ask three questions and follow each until the answer stops moving:
   - *What does this role actually do all day?* (Not the job description. The day.)
   - *Where does the work actually get stuck?*
   - *What did we try before, and why exactly did it fail?*
4. Test whether the presenting complaint is a **cause** or the **last visible touchpoint** (R2).
5. Look for two functions being run through one artifact. It is the most common root cause of
   "everything is broken" and it is invisible from the org chart.
6. Publish the reframed problem statement before doing anything else.

**The trap.** Sponsors are attached to the problem statement they gave you, and a reframe can read
as scope creep or as blaming the sponsor. Frame it as *narrowing*: we now know which of these two
problems to solve first, and in what order. Ours landed because it came with a reason the last
attempt failed.

---

### Stage 1 — Discover: get the process out of people's heads

**Purpose.** Build a faithful, specific account of how the work is done today — including the parts
nobody has ever written down.

**What we did.**

We ran layered discovery rather than a single pass, because different truths live at different
altitudes:

| Layer | Method | What only this layer gives you |
|---|---|---|
| Cross-functional | Full-day discovery session | The end-to-end chain and where it breaks between functions |
| Operator | SME download from a field-clinical/operations leader | The strategic logic — why capacity behaves as it does |
| Role-by-role | Five persona briefs (Branch ED, DCS/Clinical Manager, Senior Scheduler, Field RN/SOC nurse, Workforce Strategist) | What each role optimises for, and where those conflict |
| Frontline | Dedicated scheduler insight session with an agenda and question bank | The workarounds, the sticky notes, the end-of-day reality |
| Patient | Patient-perspective panel synthesis | The only view that judges the whole system by its output |

We also built a **structured way to harvest tacit knowledge**, on the premise that great branches
already know how to manage capacity and the knowledge is unevenly distributed. The pipeline:

```
SME → tactic captured (structured schema) → validated against data and peers → ┬→ SYSTEM RULE
                                                                                └→ AGENT GUARDRAIL
```

A tactic that cannot become either a system rule or a guardrail is a story. Log it as context and
move on.

The opening question in every interview was the same, and it is worth stealing verbatim:

> *"Think about the best branch you've seen run capacity. What did they actually do differently —
> day to day — that a struggling branch doesn't? Be specific."*

And the closing question, which seeds every guardrail you will later need:

> *"If an AI assistant were helping your scheduler tomorrow, what should it always do, and what
> must it never do?"*

**What this stage surfaced that nothing else would have.**

- **Numbers with teeth.** 50–60 authorization notifications per scheduler per day, the majority
  non-actionable. 7+ scheduler tasks per three-discipline admission, 8 once approval fires. 40–50
  patients per full-time RN+LPN pair. ~3,000 clinicians spending ~30 minutes each evening, unpaid,
  confirming tomorrow's visits.
- **A hard system stop nobody had documented.** Once a clinician accepts a visit for the day,
  **the back office cannot remove it from their device.** Every same-day change is a phone call.
  This single constraint reshapes any target-state design.
- **The real reason the last pilot failed** — and it was cultural, not technical (R5).
- **An entirely undocumented process.** The clinician's own weekly planning logic — their capacity,
  clinical prioritisation across a caseload, geographic grouping, hard timing constraints — is
  unassisted and unrecorded today. You cannot automate what nobody has ever described.

**Deliverable.** A discovery record faithful enough that a participant reads it and says *"yes, that
is what I said"* — including terminology, exceptions and the parts that make the organisation look
bad. Plus a glossary; you will need it in stage 8 when vendors use your words differently than you do.

**Exit test.** You can name the binding constraint on growth, and you can describe at least one
process that had never been written down before you wrote it.

**The procedure.**

1. **Layer your discovery.** One session type will not do it. Cross-functional for the chain,
   role-by-role for the conflicts, frontline for the workarounds, customer for the verdict.
2. **Interview the best performer, not the average one.** You are trying to encode what excellence
   does, not to describe the mean.
3. **Capture tacit tactics in a fixed schema** so they can be validated and converted. Free-text
   notes do not survive contact with a requirements document.
4. **Record verbatim where it matters.** We kept a line-numbered transcript so that every later
   citation resolves to a specific line. This is what makes a claim auditable eight weeks on.
5. **Write the glossary as you go.** SOC, ROC, DCS, TIC, POC, LUPA, buddy codes, points. Vendors and
   executives will each use these differently.
6. **Log the numbers people say out loud, and mark them as estimates.** The 3,000-clinicians and
   30-minutes figures were session estimates. We carried them forward *labelled as estimates needing
   a survey* — which is why they never quietly became a business case line.

**The trap.** Discovery that stops at the level of "the process is inefficient." Push until you have
mechanisms — the specific click, the specific queue, the specific system behaviour. "Authorization
is a bottleneck" is not usable. "HCHB generates a pending-auth workflow per patient per day, roughly
50 a day per scheduler, which trains schedulers to bulk-clear without reading, so the one that
mattered gets cleared too" is a requirement, a metric and a test case.

---

### Stage 2 — Validate: check the narrative against the system of record

**Purpose.** Confirm that what people told you is what the systems actually do. Narrative and
configuration diverge, and the gap is where projects die.

**What we did.**

We convened an on-site working session on **13 August** with three roles deliberately chosen:

- the **author of the process maps and variable inventory**, who owned every revision;
- the **system-of-record SME**, who could answer "how does it *actually* work" at HCHB-field
  specificity — the highest-density source in the session;
- the **executive initiative lead**, who owned the vendor relationships and could make decisions in
  the room.

That third seat is the one people leave out. It is why ten decisions were registered in one day
instead of ten emails over a month.

The session's stated purpose was narrow and correct: **validate the current-state map and the
variable inventory against operational reality, then move to target state.** Validation first.

**What validation changed.** A substantive correction arrived *after* the session, from the map's
author, and it inverted a core assumption:

> Routine visits are **first plotted by the evaluating clinician at admission, not by the
> scheduler.** Each clinician plots frequency for their own discipline only. **In steady state there
> is no scheduler workflow at all unless a visit must be reassigned.**

Everything drawn before that correction had the wrong actor holding the pen. Had we gone to market
without it, we would have specified a scheduling product for work that schedulers do not do.

**Deliverable.** A decisions register with numbered, quotable entries, plus an explicit list of what
was deferred and why.

**Exit test.** At least one thing you believed at the end of stage 1 is now known to be wrong. If
nothing changed, the session was a presentation, not a validation.

**The procedure.**

1. Get the system-of-record expert in the room. Not the system owner — the person who knows what
   the software does when you click the thing.
2. Bring a **draft to be corrected**, never a blank page. People correct far more precisely than
   they generate. Our maps existed specifically to be marked up.
3. Put a decision-maker in the room and **register decisions as they are made**, numbered, in the
   session, in language you could quote in a contract.
4. **Record the deferrals with the same discipline as the decisions** (R6).
5. Assign every open item an owner by name in the session.
6. **Expect and welcome a post-session correction.** Build a channel for it and treat it as
   evidence the validation worked.

**The trap.** Treating the validation session as sign-off. Its output is a corrected draft and a
decisions register — not approval. Approval belongs at the gate, after stage 6.

---

### Stage 3 — Structure: turn narrative into registers with IDs

**Purpose.** Convert prose into objects that can be counted, sorted, scored, assigned and cited.

**What we did.**

Three registers, built in parallel over roughly four days, plus the variable inventory that
underpins all of them.

**3a. The constraint register — CN-01 … CN-51.**
Every constraint on scheduling today, each classified by *whether we can change it*:

| Class | Meaning | What you do with it |
|---|---|---|
| Regulatory | Medicare/CoP requirement | Design around it. Non-negotiable |
| Payer | Contract or plan rule | Encode it as data, not as code |
| HCHB-configurable | A setting that is currently off or wrong | Free win. Separate, faster track |
| **HCHB product limit** | The vendor cannot do it | **This is the case for building** |
| Compassus policy | Our own rule | Free win. Change it; no system needed |
| Cultural | How people work | Change management, not requirements |
| Labour agreement | Contractual with the workforce | Constraint on incentive design |

**The nine product limits (CN-22…CN-30) are the entire argument for a new platform.** Four of the
loudest pain points (CN-18, CN-31, CN-32, CN-33) turned out to be Compassus's own — run those on a
separate track and bank the win early, without waiting for a vendor.

**3b. The bottleneck dossiers — twelve, ranked by leverage.**
Each carries the same seven fields: mechanism · evidence · downstream effects · what to measure ·
candidate remedies · open questions · rank. The first four are the ones worth solving first. A
ranked dossier is what turns "everything is a bottleneck" into a sequenced work plan.

**3c. The connection-point register — CP-1 … CP-10.**
The places where a capacity decision constrains a scheduling action, or a scheduling action changes
the capacity picture. These are precisely where a manual system loses information, and therefore
where automation pays. Three of them carry the initiative:

- **CP-3 — SOC capacity gates admission acceptance.** Capacity gates growth. The highest-value
  connection point in the system.
- **CP-4 — cancellation recovers capacity.** Governs whether the branch wastes what it already has.
- **CP-5 — point totals feed caseload balance.** Underlies both — **and points were undefined.**

**3d. The variable inventory — the spine.**
79 scored rows (76 numbered plus 3 unnumbered) across four ID families: `SH-` shared, `C-` capacity,
`S-` scheduling, `CO-` coordination. IDs are the join key to everything downstream and **are never
renumbered.** Each row scored for:

- **MVP requirement** — Yes / Maybe / No, weighted 3 / 1 / 0
- **Gating** — a hard or structural constraint that is also MVP-required. A knockout: a product that
  cannot do it is disqualified however well it scores elsewhere
- **Conflict risk** — the vendor's built-in way of working could contradict how we operate
- **Automation posture** — what we will permit the system to do: *drive*, *assist*, or *read only*

That last field is quietly the most important thing in the inventory, and stage 8 will show why.

**The nine open questions — ordered by dependency.** We ended stage 3 by writing down what we did
*not* know, ordered so that answering one unblocks the next. **Question 1 was the point system** —
what a point represents, values by visit type and discipline, targets, how travel is treated.
Referenced everywhere, defined nowhere, and the shared currency of both capacity and scheduling.
Almost nothing downstream could be specified until it was pinned.

**Deliverable.** Registers with stable IDs, a scored inventory, and a dependency-ordered list of
open questions.

**Exit test.** You can answer *"what exactly are we buying, and what would disqualify a product?"*
by pointing at rows, not by talking.

**The procedure.**

1. **Give everything an ID before you give it a priority.** IDs are how a claim stays traceable
   across five weeks, three documents and two organisations.
2. **Classify constraints by changeability, not by severity.** Severity tells you what hurts.
   Changeability tells you what to do — and separates the free wins from the build case.
3. **Rank bottlenecks with a fixed dossier schema** so they are comparable rather than merely
   listed.
4. **Find the seams.** The connection points between functions are where automation pays and where
   manual systems leak.
5. **Score for disqualification, not just for preference.** A gating flag is worth more in a vendor
   evaluation than any weighted average.
6. **Record the automation posture per variable, in advance.** Decide what the system may decide
   *before* you meet a product that would like to decide it for you.
7. **Order the unknowns by dependency and publish them.** The foundational one — ours was the point
   system — gates everything else and should be resourced first.

**The trap.** Building an elegant register nobody uses. Ours survived because every downstream
artifact — the flow sheets, the one-pager, the questionnaire, the business case — cites the same
IDs. One vocabulary, used everywhere, is worth more than three better ones used once each.

---

### Stage 4 — Visualise: draw current state until the room stops correcting it

**Purpose.** Produce a shared picture specific enough that disagreement becomes visible and
correctable.

**What we did.**

We drew the current state as **seven flow sheets**, built to a fixed design system and generated
from scripts so any correction could be re-rendered rather than re-drawn:

| Sheet | What it carries |
|---|---|
| Primary flow map | The whole episode in four phases — the orientation sheet |
| Detailed composite | The original hand-built swimlane, redrawn with every correction applied |
| SOC / ROC full flow | The referral pass, then the per-discipline plan-of-care pattern |
| Routine visits | The clinician's own week, the day-before negotiation, the five dispositions |
| Authorization | Auth at its **two** interfaces: the gate at start of care, the ceiling inside the plan of care |
| Recert & discharge | End of episode, through a worked example with staggered per-discipline discharges |
| DCS / scheduler handoff | The single most-cited breakdown, on one page |
| *(added 19 Aug)* Payer economics | Why the same operational event costs differently in every payer class |

Four **illustrative scenario sheets** were built earlier, from the variable model, before the
on-site session — a day in the life, a call-out recovery, a territory review. Fictional patients,
real decision logic. Their job was to make the variables *feel* like a real day, and to give the
room something concrete to argue with.

**The conventions that made the sheets work.** These look cosmetic. They are not — each one encodes
a finding:

- **Colour is the actor, and the person beats the system.** A workflow item inside HCHB worked by a
  human carries the human's colour. Purple — the system colour — appears only where HCHB acts by
  itself. When the legend was corrected on 13 August, the sheets showed what everyone suspected:
  **genuine automation in HCHB is approximately nil.** The colour rule *is* the finding.
- **Size is frequency.** Large block = happens every time. Small block = conditional. Pill = a watch
  condition, not a step. Weight on the page matches weight in the process.
- **Every sheet is current state, and every footer says so.** Nothing on them is a proposal. The
  moment a current-state map carries an aspiration, it stops being evidence.
- **Sheets are generated, never hand-edited.** Source scripts live in the repository; PDFs are
  published to Drive. The published copy is never the master.

**The measure of done.** Twenty-six numbered rounds of corrections are recorded in the redraw
assessment. Actors changed hands; dispositions were split apart (*decline* and *reassign* turned out
to be different things); the day-before dispositions moved from the visit to the evening before.
**Current state is finished when a session produces no new corrections — not when the drawing looks
good.**

**Deliverable.** A set of current-state sheets, regenerable from source, plus a written record of
every correction and who made it.

**Exit test.** Put the primary map in front of someone who does the work daily and they add nothing.

**The procedure.**

1. **Draw before you are ready.** The draft's purpose is to be corrected. A wrong map in the room
   beats a right map in a fortnight.
2. **Fix a design system first** — palette, type scale, block semantics, legend — and write it down
   so it is not re-derived each time. Ours became a reusable skill.
3. **Generate, do not draw.** Corrections arrive in bursts; a sheet you cannot re-render in a minute
   is a sheet that goes stale.
4. **Make the legend carry meaning.** Actor-coloured, frequency-sized, with a rule about who wins
   when a person works inside a system.
5. **Label current state on every page,** and keep proposals off it entirely.
6. **Count the correction rounds.** They are your completeness metric.
7. **Build the "day in the life" companion sheets.** Registers do not convince anyone. A worked
   day — five visits, 7.25 points against a 7.0 ceiling — does.

**The trap.** Drawing the future state too early. It was deliberately deferred here, and that was
right: a target state drawn before the current state stops moving encodes your assumptions instead
of the organisation's reality.

---

### Stage 5 — Economics: learn how the money actually works

**Purpose.** Understand the payment mechanics well enough that no operational recommendation
accidentally destroys revenue or invites an audit.

**What we did.**

We built a payer and episode economics reference plus a seven-part sourced research corpus — PDGM
mechanics and rates, Medicare Advantage, commercial and Medicaid, utilisation management and margin,
cost and labour economics, authorization operations, value-based purchasing and policy. Every figure
carries its source and date.

**Five findings that changed the design.** These are the reason this stage sits *before* the
business case and not after it.

1. **Payment is per 30-day period — not per certification period, and not per visit.** Two payment
   periods sit inside one 60-day certification period, each with its own case-mix group, payment
   amount and LUPA threshold. **A capacity model that only knows the certification period cannot see
   the cliff it is walking toward.** That is a data-model requirement discovered in an economics
   document.
2. **There is a ceiling as well as a floor.** Below the LUPA threshold the period pays per visit
   instead of in full. Above it, under episodic payment, every further visit is cost with no
   revenue. The target is *the clinically right number, above the floor and no higher than the
   period supports* — surfaced to the clinician, **never** weighed against clinical need inside an
   objective function.
3. **The fastest win needs no new data.** The authorization team already writes payer rules into a
   coordination note at verification. Surfacing them at plan-of-care creation is a schema change and
   a surfacing point — not a data-gathering programme. And it is a patient-care win, not only a
   throughput one: abrupt discharges happen because nobody planned against the real visit budget.
4. **The book is majority non-episodic.** Roughly 260M of in-scope episodic revenue against ~549M
   total — so 53% of the business does not behave the way PDGM intuition expects. **Several levers
   invert by payer class.** Automating the clinicians' unpaid evening confirmation calls, for
   instance, creates sellable capacity only where clinicians are paid per visit; under episodic
   payment an additional visit earns nothing.
5. **Policy is a clock you do not control.** A national six-month moratorium on new Medicare home
   health enrollment meant growth could not be bought with new locations while it held — which
   converts this initiative from an efficiency programme into *the* growth strategy. Separately,
   an electronic prior-authorization requirement lands inside the scale phase, so authorization
   state had to be designed as a *measured input*, not a hard-coded assumption.

**Deliverable.** A payer reference document, a sourced research corpus with dates and links, and a
list of the economic facts that constrain the design.

**Exit test.** For any operational change you might propose, you can say who pays, how much, under
which payer class, and what the audit exposure is.

**The procedure.**

1. **Map the payment unit before the operational unit.** If you do not know what the payer buys, you
   cannot know what an operational improvement is worth.
2. **Find the floor and the ceiling.** Most reimbursement schemes have both. Optimising toward
   either without naming the other is how compliance incidents happen.
3. **Segment by payer class and test every lever in each.** A lever that inverts sign across the
   book is a lever that will embarrass you in a readout.
4. **Cite everything, with dates.** Rates and thresholds are recalibrated annually.
5. **Write down what the initiative must never claim** (see stage 6). Do it here, while you are
   reading the compliance literature, not later while you are defending a number.
6. **Check the regulatory calendar against your own timeline.** Requirements arriving during your
   scale phase are design inputs today.

**The trap.** Treating economics as a finance workstream that runs in parallel. It is a *design
input*. Two of the five findings above are data-model requirements, and neither would have been
discovered by an operations team or supplied by a vendor.

---

### Stage 6 — Building the business case

> This is the stage most initiatives do worst, and the one sponsors judge you on. It gets the
> longest treatment here.

**Purpose.** Convert an operational thesis into a number finance will underwrite — with the
mechanism, the arithmetic, and the missing inputs all visible.

#### 6.1 Find the house format before you build anything

We did not invent a format. We found the format the organisation already uses — a worked internal
example (an AI coding business case) — and matched it exactly.

**The house layout is two panels.**

- **Left: the waterfall — "Annual Net Value Build-up."** Three series: value drivers (green), costs
  (red), subtotals and net (navy). Read left to right. Subtotals break the run into named
  workstreams, each with its own net. Costs are drawn explicitly and netted, never hidden — a
  zero-cost item is still drawn as a bar at zero. ROI is stated as a percentage against cost
  alongside the net.
- **Right: the upside panel.** Dark navy, headed **THE UPSIDE**. Probabilistic or
  behaviour-dependent value goes here, each lever expressed as *a percentage of a named revenue
  base, with the base stated*. **One lever is allowed to be "not yet valued"** with a named owner to
  fill it — the house example does exactly this.

**The rule that decides which panel a lever goes in:** hard, countable, removable cost goes on the
waterfall. Probabilistic or behaviour-dependent value goes on the right.

**What reading the house example taught us, beyond layout.** The organisation's home health revenue
base is ~549M, in-scope episodic revenue ~260M, a 0.5% VBP swing is the accepted modelling
convention, and turnover reduction is already accepted as a *waterfall* lever rather than an upside
one. Critically, the coding case already carried a placeholder naming *reduced LUPA risk and
capacity for growth* as unvalued productivity upside — **our initiative's core ground, sitting in
someone else's business case as an unquantified footnote.** Finding that was worth a week.

> **Procedure.** Before drafting, find two or three business cases your organisation has actually
> approved. Copy the layout, the conventions, and the vocabulary. A case that looks like the ones
> that got funded starts several meetings ahead. And read them for *anchors* — the revenue bases and
> modelling conventions your finance team has already blessed are the ones you must use.

#### 6.2 Tier every case honestly

We refused to publish a single headline number without saying how much of it was real. Five tiers:

| Tier | Meaning | Where it goes |
|---|---|---|
| **Committed** | A countable unit exists today and finance can book it | Waterfall, green |
| **Modelled** | Mechanism established, arithmetic sound, but an input is missing | Waterfall, green, **flagged** |
| **Directional** | Real and evidenced, but size depends on behaviour we have not measured | Upside panel |
| **Not yet valued** | Named, credible, deliberately unpriced | Upside panel |
| **Risk avoided** | A loss that does not occur | **Narrative only. Never a waterfall bar** |

The tiering is the credibility mechanism. A modelled number that is *labelled* modelled survives
scrutiny. The same number presented as committed does not survive it twice.

#### 6.3 Build the register before the model

We wrote a **business case register** — every financially connected case, direct or indirect, each
with five fields:

**mechanism · evidence · sizing formula · tier · what must be supplied to commit it**

Organised into seven families:

| Family | Examples | Character |
|---|---|---|
| Workforce & administrative cost | Scheduler capacity released; authorization notification noise; premium-labour offset; overtime; PTO collision avoidance; travel; unpaid evening confirmation work | **The hard core.** Countable, and independent of payer class |
| Revenue capture & leakage | Non-billable visit avoidance; LUPA leakage recovered; recertification capture; benefit and cap management; authorization denial and rework | Mostly modelled; some genuinely uncounted today |
| Utilisation & margin | Discipline and role match; visit distribution and timing; rebook waste | Episodic only |
| Growth & throughput | SOC capacity as the growth constraint; the enrollment moratorium as context; referral-source trust; integration onboarding | **The largest upside** |
| Quality-linked revenue | Value-based purchasing; star ratings | Use the house convention |
| Risk avoided | Threshold-adjacent billing scrutiny; missed compliance windows; wage exposure | Narrative |
| Option value | The payer rules library as a durable moat; first real dataset on authorization behaviour | Narrative |

**Two register entries worth studying as craft.**

*Scheduler capacity released* — the largest single hard lever, on the order of 12M a year. We
published it **with two honesty notes attached**: not all of it is attributable to the platform,
because part of the reduction comes from workflow automation that arguably should not exist at all;
and the release phases across the rollout, so year one carries a fraction. Those two sentences are
what make the 12M believable.

*LUPA leakage recovered* — roughly 10.7M of annual exposure, of which perhaps 2.2M is recoverable.
Published with an **absolute gate**: the recoverable share is *only* visits that were clinically
indicated and lost to an operational failure. Nothing in the case justifies adding a visit to clear
a threshold — and we noted that a federal audit found 21% of claims just above the threshold
non-compliant, with contractors committed to targeting that cluster. **State the gate in the case
itself, not in a footnote.**

#### 6.4 Write the anti-double-counting rules down

Large cases inflate by accident. Ours carries explicit rules, and every one of them removes money:

- Authorization notification noise sits *inside* scheduler capacity released. **Never add them.**
- Discipline-and-role match appears once. The freed evaluation capacity it creates is the growth
  lever, and growth is upside, not waterfall.
- LUPA recovery and rebook waste overlap where a rebooked visit is also the visit that would have
  cleared the floor. Count it once.
- Unpaid evening confirmation work pays only on non-episodic patients. Do not apply it to the whole
  clinician base.
- Growth revenue converts at *contribution* margin, not the blended rate, and must not be added to
  any lever that already assumes the same freed capacity.

> A reviewer who finds a double-count you did not disclose discounts your whole case. A reviewer who
> finds the rule you wrote to prevent it trusts the rest of it.

#### 6.5 Publish what you cannot yet know

The register ends with a table of inputs only finance and operations can supply — loaded cost of a
scheduler role, contract/per-diem/overtime baselines, mileage and drive-time baselines, the count
and value of visits written off for authorization, actual LUPA rate, missed and rebooked visit
rates, loaded cost per visit by discipline, turnover and replacement cost, actual period counts.
**Each row names which case it converts from modelled to committed.**

**One input was flagged as the highest-value single ask: the pay-model split across the estate.**
For a per-visit clinician, cost is linear and scheduling optimisation cannot create margin. For a
salaried clinician, the marginal visit is near-free to the ceiling, so unused capacity is a realised
loss. **The named pilot candidates were the per-visit offices — the best sites for adoption and the
worst sites for proving a margin case.** Naming that tension in the business case, in advance,
rather than discovering it in the pilot readout, is the difference between a controlled trade-off
and a failed pilot.

#### 6.6 Write down what the case must never claim

Ours does, explicitly. This section is not defensive padding; it is what lets clinical leadership
support a financial document:

- That visits will be added to clear a payment floor.
- That margin will enter a scheduling objective function or weigh against clinical need.
- That fewer visits per period is itself the goal — industry utilisation has already fallen ~18%
  while discharge-to-community outcomes worsened.
- That telehealth can substitute for a floor visit.
- That star ratings will deliver referral growth. *(Two published studies put the consumer-choice
  effect at ~0.8 points and a statistically insignificant 0.25 points. We killed our own lever.)*
- **Any saving that depends on a specific manager working weekends.** If it is not encoded as
  standard work, it is not a business case.

#### 6.7 Then build the model

The last step, not the first: **one sheet of named, editable assumptions** feeding the waterfall and
the upside panel, so the case can be argued at the assumption level rather than the conclusion
level. The register's "what must be supplied" table *is* the model's input block; everything else is
a formula.

This matters more than it sounds. A sponsor who disagrees with 7.9M and cannot see why disagrees
with you. A sponsor who can change *capacity gain: 4%* to *2%* and watch it become 4.0M is now
negotiating assumptions with you — which is the conversation you want.

**Deliverable.** A tiered register, an assumptions model, and a two-panel output in the house format.

**Exit test.** A finance reviewer can trace any bar on the waterfall to a formula, to an assumption,
to a named owner for the input.

**The trap.** Leading with the headline. We could have opened with 7.9M. Leading instead with
*"here is the mechanism, here is what we counted, here is what we deliberately did not count, and
here are the eleven numbers we need from you"* is slower in the first meeting and decisive in the
third.

---

### Stage 7 — Architect: decide the target-state shape and the automation posture

**Purpose.** Decide what you are building or buying — at the level of modules, sequencing and
authority — before you describe it to anyone outside the room.

**What we did.** Ten decisions, registered on 13 August. The five that shaped everything downstream:

| # | Decision | Why it mattered |
|---|---|---|
| **DE-02** | **Three-module target architecture: Capacity Management · Scheduling Engine · Patient Engagement** | Became the organising frame of the one-pager, the questionnaire and the vendor comparison |
| **DE-03** | **Capacity is Phase 1, and Phase 1 is visualisation only — no automation in the first release** | The direct answer to Alabama. You cannot optimise what you cannot yet see (R4) |
| **DE-04** | The capacity tool replaces the scheduling grid. They are the same object — do not build both | Prevented shipping a parallel system alongside the spreadsheet it was meant to retire |
| **DE-09** | **The tool recommends; the human accepts.** Clinicians supply their own availability and preferences | The automation posture, stated as policy before any vendor could argue for more |
| **DE-10** | Preserve a human scheduling role at reduced scale — fewer schedulers, retained function | Kept the headcount conversation honest, and kept local judgment in the system |

**The model in one paragraph** — the form it took, and the form it kept:

> **Capacity Management** is the envelope: how much work a branch can deliver, given people, hours,
> disciplines and territory, netted against what is already booked. The **Scheduling Engine** fills
> that envelope — which clinician, which day, which route. **Patient Engagement** defends it: the
> confirmation, coverage and rebooking work that turns a schedule into delivered visits. The latter
> two sit inside a shaded **Coordination** zone, because both are performed *against* the envelope
> rather than being parts of it. Only a completed visit becomes revenue; a discharge hands room back
> to capacity.

**Three changes were identified as high-leverage relative to complexity** and could proceed
independent of any platform decision: discipline-role match defaulting to the paraprofessional with
explicit opt-out; care-team assignment at referral rather than per visit; and data-driven territory
design. Naming these gave the initiative deliverables that did not wait on procurement.

**Deliverable.** A numbered decisions register, a named module architecture, a phase-one scope
boundary, and a written automation posture.

**Exit test.** You can describe the target state in one paragraph without using a vendor's product
name.

**The procedure.**

1. **Decide the module boundaries before you meet products,** or you will inherit whichever
   boundaries the best salesperson uses.
2. **State the automation posture as policy.** *The tool recommends; the human accepts* is a
   sentence you can hold a vendor to. "We want a human in the loop" is not.
3. **Make phase one the smallest thing that creates visibility.** Visualisation before optimisation
   is not timidity; it is the only way to get a baseline, and the baseline is the pilot's evidence.
4. **Refuse to build two systems that are the same object** (DE-04). Look for this explicitly — it
   hides well.
5. **Separate out what can proceed without procurement** and start it. It funds credibility.
6. **Say what happens to the roles.** Ours said it plainly: ~300 schedulers today, perhaps 100 in
   target state, with the air-traffic-control function deliberately preserved. Initiatives that
   avoid this question have it answered for them, badly, by rumour.

**The trap.** Letting the architecture be set by the most impressive demo. The decisions register
existed precisely so that when a product later scored highest *and* overreached the stated posture
on 16 variables, we could see it as a **fit problem** rather than a feature win.

---

### Stage 8 — Market: one-pager → questionnaire → structured comparison

**Purpose.** Get comparable, honest information from vendors without spending goodwill or inviting
overselling.

#### 8.1 The one-pager comes first

Before any questions, we published a single page — *"What we are looking to build"* — laid out in
the same three areas as everything else: **Capacity Management** (the envelope) · **Scheduling
Engine** (filling the envelope) · **Engagement** (making it happen), with Scheduling and Engagement
grouped under **Coordination**.

Its jobs, in order:

1. Give every vendor the same context, so the answers are comparable.
2. Assert the frame. Several vendors do not touch capacity management or engagement at all — the
   one-pager makes that a visible gap in *their* answer rather than an omission in our question.
3. Close with the thesis, in one line: *"Capacity sets the envelope. Scheduling and engagement are
   both performed against it — which is why we are looking for a platform that treats all three as
   one system."*

> **Procedure.** Write the one-page statement of what you are building before you write a single
> question. It is the control variable for the whole exercise, and it doubles as the internal
> alignment document.

#### 8.2 Design the questionnaire to defeat overselling

The instruction from the executive lead was explicit and correct:

> *"These techcos will take every opportunity to oversell what they have here, so we should make
> these status options as discrete and clear as possible — basically try to force as much clarity as
> possible in the way we set up the form."*

The mechanism we built is the **three-dropdown coverage grid**. Every capability area is marked
three ways, with a free-text notes column beside it:

| Column | Options |
|---|---|
| **IN SCOPE** — do you do this at all? | Yes · Through a partner · No |
| **STATUS** — how far along is it? | Production, multiple customers · Production, one customer · In development, target date in notes · Roadmap, no date yet |
| **HOW IT RUNS** — does a person still do the work? | Automated end to end · Automated, person approves · System prepares it, person does it · Person does it |

**Why three columns and not one.** *In scope* separates the vendors who touch capacity or engagement
from those who do not — several genuinely do not. *Status* stops "we have that" from covering a
roadmap item. **And "how it runs" is the automation-posture question in disguise** — it lets you
compare a product's actual behaviour against the posture you set in stage 7, per capability, in a
dropdown a salesperson cannot soften. Free text goes in notes, where it cannot contaminate the
comparison.

**The questionnaire's five sections**, each doing a distinct job:

| Section | Job |
|---|---|
| **A. Company and product** | Integration with the system of record; customers, scale and references; **measured impact on existing customers** — what changed, over what period, how measured |
| **B. Coverage self-assessment** | The three-dropdown grid across the eleven areas of the three-module model, with the one-pager as the reference |
| **C. How your product works** | Eight scenario questions, not feature questions: *"A branch leader is deciding whether to accept a referral today. What can your product tell them?"* · *"Walk us through what your product does when a clinician calls out"* · *"What does it do with a visit that is ordered but not yet schedulable?"* |
| **D. The clinician's place in the model** | What the clinician decides vs. what is decided for them; what happens when they disagree; **a deployment where clinicians resisted, and what changed as a result**; decide-or-advise positioning; adoption measurement |
| **E. Fit and partnership** | What we did not ask; where a design partner helps; **sharing in the value we create**; deployment and change management; **what you deliberately chose not to build** |

**Four design choices worth stealing.**

1. **Section D exists at all.** An entire section on the clinician's place in the model, opening by
   acknowledging that scheduling in home health is *personally consequential* and that clinicians
   come to home health for control over their own week. Asking a vendor to describe a deployment
   where clinicians resisted them — and what they changed — surfaces more than any feature matrix.
   It is stage 1's finding (R5) turned into a procurement instrument.
2. **Ask for measured impact, not capability.** *What did you measure, over what period, and how?*
3. **Ask about value-sharing explicitly.** The reasoning, stated in the questionnaire itself: we are
   about to put subject-matter guidance, deployment effort across the branch estate, and reference
   and co-marketing value into a product whose vendor will sell it to our competitors. The question
   is left deliberately open — *in what ways would you be open to sharing in it?* — because how they
   answer an open question is itself the signal.
4. **Ask what they chose *not* to build.** The best answers to this question are the most
   informative sentences in any vendor response.

#### 8.3 Hold questions back on purpose

Three tabs exist that vendors never see, and they are as deliberate as the questions that shipped:

- **Additional questions — held for follow-up.** Drafted, judged valuable, and kept out of round one
  so the questionnaire stays answerable. *"Most of these need a screen, a follow-up or a tone of
  voice to be worth anything — which is what the virtual calls are for."* Includes an entire
  deep-dive agenda for the finalist session.
- **Vetting — for leaders.** Company maturity, security posture, insurance and contracting.
  Set aside because the shortlist is already assumed vetted, and because these are verifiable
  afterwards — *asking them up front spends goodwill on a low-yield answer.*
- **Coverage — expanded.** A 41-row version of the coverage grid, rolled up from the variable
  inventory's own subcategories, held in reserve if more granularity is wanted. **It does not expose
  the numbered inventory itself.**

> **Two principles.** *Balance detail for us against burden for them* — a questionnaire nobody
> completes properly tells you nothing. And *pricing is deliberately held from round one*: asking
> early anchors the negotiation and invites a sales response rather than a product one.

#### 8.4 Iterate the instrument with the executive who will use the answers

The questionnaire went from v1 → MASTER → MASTER 2.0 in about 36 hours, driven by one round of
written feedback from the executive lead. That feedback produced the maturity/scope split, the
value-sharing question, the change-management question, the measured-impact question, and the
patient-availability question. **The instrument improved more from one reviewer who would have to
act on the answers than it would have from three more drafting passes.**

The workbook also ships with an **Instructions tab** (how to answer, how to co-author, and a pointer
to read the Overview tab first), a **Meta tab** recording form version, audience and question IDs,
and light sheet protection so the layout survives the round trip. Small things. They are why the
answers come back comparable.

**Deliverable.** A one-pager, a versioned questionnaire with controlled vocabularies, a held-back
question bank, and a finalist deep-dive agenda.

**Exit test.** Two completed questionnaires from different vendors can be laid side by side and
compared cell for cell without interpretation.

**The trap.** Free-text questionnaires. They feel thorough and generous, and they produce brochures.
Every place you can force a dropdown, force one — then give the notes column room to carry the
nuance.

---

## Part III — The disciplines that made it hold together

Nine stages in five weeks only works if the supporting machinery is right. Four disciplines did most
of that work, and they are the cheapest thing in this document to copy.

### 9. Artifact discipline

**Every fact has one authoritative home, and the direction of change is written down.**

| Artifact class | Authoritative source | Rule |
|---|---|---|
| Variables and scoring | The workbook, in Drive | The workbook is upstream. Repository documents are read-only renderings; if a figure changes there, change it here — not the reverse |
| Flow sheets | The generator scripts, in the repository | The repository is upstream. Regenerate here, publish to Drive, **never edit the published PDF** |
| Knowledge documents | The repository | Each carries the Drive ID of its source and the date it was ingested |
| Decisions | The decisions register | Numbered, quotable, never renumbered |

Three practices made this cheap to maintain:

- **A Drive index.** Every file in the working folder, mapped to where it lives in the repository,
  with nothing unaccounted for. When someone asks *"do we have that document?"* there is one place
  to look — and when a file has no counterpart, the index says so explicitly rather than letting the
  gap hide.
- **A README at every level** that says what the folder is for and what to read first. The artifacts
  README opens with *"Start here if you are a new session"* and names the one file to read before
  touching a flow sheet.
- **Stable IDs, never renumbered.** `CN-`, `CP-`, `DE-`, `SH-`, `C-`, `S-`, `CO-`. Renumbering an ID
  invalidates every citation in every document written before the renumber.

### 10. Vocabulary discipline

The three-module frame — **Capacity Management · Scheduling Engine · Patient Engagement** — appears
in the decisions register, the flow sheets, the one-pager, the vendor questionnaire's coverage grid,
and the business case's workstream subtotals. **One vocabulary, used everywhere.**

An earlier six-category framing (Workforce · Capacity · Demand · Scheduling · Coordination ·
Results) preceded it. Rather than delete the earlier artifacts, we documented the lineage explicitly
— *"not a contradiction, a lineage"* — so nobody encountering an older sheet concludes the model
changed underneath them.

> **Procedure.** Pick the naming once, at stage 7, and then rename everything upstream to match.
> When the vocabulary does change, write down what it superseded and why.

### 11. Honesty discipline

The initiative's credibility came from what it refused to assert. Collected in one place, because
this is the habit worth transplanting:

- Session estimates carried forward **labelled as estimates needing a survey** — never quietly
  promoted to business case lines.
- Illustrative sheets labelled illustrative: *"fictional patients and figures; the decision logic is
  the real thing."*
- A vendor scoring highest reported **alongside its 16 posture overreaches**, with the plain reading
  attached: *"A higher score is not automatically a better fit."*
- Business case levers tiered, with the missing input named for each.
- A lever of our own killed on the evidence — star ratings will not deliver referral growth.
- Current-state sheets footered as current state, with proposals kept off them entirely.

### 12. Cadence and gate discipline

Every gate is a stop-and-decide, not a formality. The agent or lead brings the exit-criteria
evidence, the risks, a clear recommendation, and one question: **what does advancing optimise, and
what does it silently trade against?** A gate that cannot be evidenced has not been passed, and
somebody has to say so plainly.

| Cadence | Rhythm | Produces |
|---|---|---|
| Working session | As needed during discovery | Corrected drafts, decisions register entries |
| Initiative standup | Weekly, cross-functional | Scorecard review, decision log |
| Steering committee | Monthly, sponsors and executives | Executive readout |
| Phase-gate review | At each boundary | Exit-criteria evidence and a go/no-go |

---

## Part IV — The reusable kit

### 13. The onset checklist

Copy this. Tick it. An unticked box is a known risk, not an oversight.

**Stage 0 — Frame**
- [ ] Presented problem written down verbatim, with attribution
- [ ] Cross-functional working session held with the people whose hands are on the work
- [ ] Prior attempts identified, with the *actual* reason each failed
- [ ] Tested whether the presenting complaint is a cause or the last visible touchpoint
- [ ] Checked for two functions being run through one artifact
- [ ] Reframed problem statement published, and it surprised someone senior

**Stage 1 — Discover**
- [ ] Discovery layered: cross-functional · operator · role-by-role · frontline · customer
- [ ] Best-performing site interviewed, not the average one
- [ ] Tacit tactics captured in a fixed schema, each convertible to a rule or a guardrail
- [ ] Verbatim record kept and line-numbered so citations resolve
- [ ] Glossary started
- [ ] Quantities heard in sessions logged **and labelled as estimates**
- [ ] Binding constraint on growth identified and named
- [ ] At least one previously undocumented process written down

**Stage 2 — Validate**
- [ ] System-of-record expert in the room
- [ ] A draft brought to be corrected, not a blank page
- [ ] A decision-maker present, and decisions registered in-session with numbers
- [ ] Deferrals recorded with the same discipline as decisions
- [ ] Every open item has a named owner
- [ ] At least one stage-1 belief now known to be wrong

**Stage 3 — Structure**
- [ ] Constraint register, classified by **changeability**
- [ ] The subset that cannot be changed isolated — that is the build case
- [ ] The subset that is our own policy isolated — that is the fast track
- [ ] Bottlenecks ranked, each with a full dossier
- [ ] Connection points between functions mapped
- [ ] Variable inventory scored: MVP weight · gating flag · conflict risk · **automation posture**
- [ ] Open questions published in dependency order, foundational one first

**Stage 4 — Visualise**
- [ ] Design system fixed and written down before drawing
- [ ] Sheets generated from source, not hand-drawn
- [ ] Legend encodes actor and frequency
- [ ] Every sheet labelled current state; no proposals on them
- [ ] Correction rounds counted; drawing declared done when a session adds nothing
- [ ] At least one worked "day in the life" companion sheet

**Stage 5 — Economics**
- [ ] Payment unit mapped before the operational unit
- [ ] Floor and ceiling both identified
- [ ] Every lever tested in every payer or customer class; sign inversions named
- [ ] All figures sourced and dated
- [ ] Regulatory calendar checked against the initiative timeline
- [ ] "What this must never claim" drafted

**Stage 6 — Business case**
- [ ] House format found and matched; approved cases read for anchors and conventions
- [ ] Every case tiered: committed · modelled · directional · not yet valued · risk avoided
- [ ] Register written before the model — mechanism, evidence, formula, tier, missing input
- [ ] Anti-double-counting rules written down
- [ ] Missing inputs tabled, each naming the case it converts
- [ ] "What this must never claim" published in the case itself
- [ ] Assumptions model built: one sheet of named, editable inputs
- [ ] Output rendered in the house two-panel format

**Stage 7 — Architect**
- [ ] Module boundaries decided before meeting products
- [ ] Automation posture written as policy, in a sentence you can hold a vendor to
- [ ] Phase one scoped to the smallest thing that creates visibility
- [ ] Checked that no two deliverables are the same object
- [ ] Work that can proceed without procurement identified and started
- [ ] Role and headcount implications stated plainly

**Stage 8 — Market**
- [ ] One-pager published before any question is written
- [ ] Coverage grid uses controlled dropdowns — scope · maturity · **how it runs**
- [ ] Scenario questions, not feature questions
- [ ] A section on the people the change lands on
- [ ] Measured impact requested, with method and period
- [ ] Value-sharing and change-management questions included
- [ ] Round-two questions deliberately held back, and recorded
- [ ] Pricing held from round one
- [ ] Instrument reviewed by the executive who will act on the answers
- [ ] Two responses can be compared cell for cell

### 14. Deliverable specifications

What "done" looks like for each artifact, so the next initiative does not renegotiate it.

| Deliverable | Minimum specification |
|---|---|
| **Reframed problem statement** | One paragraph. States what the problem is *not*. Cites the evidence for the reframe |
| **Discovery record** | Faithful to participants' own words. Includes exceptions and unflattering findings. Carries a glossary. Estimates labelled |
| **Decisions register** | Numbered `DE-nn`. One sentence each, quotable. Deferrals listed separately with reasons |
| **Constraint register** | Numbered `CN-nn`. Classified by changeability. The immovable subset explicitly identified as the build case |
| **Bottleneck dossier** | Ranked. Seven fields each: mechanism · evidence · downstream effects · what to measure · candidate remedies · open questions · rank |
| **Variable inventory** | Stable IDs by family. Scored for MVP weight, gating, conflict risk, automation posture. Never renumbered |
| **Current-state flow sheets** | Generated from source. Actor-coloured, frequency-sized legend. Footered as current state. Correction history retained |
| **Economics reference** | Every figure sourced and dated. Floor and ceiling identified. Sign inversions by class named |
| **Business case register** | Every case tiered. Mechanism, evidence, sizing formula, missing input per case. Anti-double-counting rules. "Must never claim" section |
| **Assumptions model** | One input sheet of named, editable assumptions. Everything else a formula |
| **Vendor one-pager** | A single page. Same vocabulary as everything else. Ends with the thesis in one line |
| **Vendor questionnaire** | Versioned. Controlled dropdowns on every comparable field. Instructions tab. Meta tab with version, audience and question IDs. Held-back questions recorded separately |

### 15. Roles — who has to be in the room

| Role | Stages | Without them |
|---|---|---|
| **Initiative lead / PM** | All | Nothing is registered, sequenced, or finished |
| **Executive sponsor** | 0, 2, 6, 7, 8 | Decisions become emails; the questionnaire asks the wrong things |
| **System-of-record SME** | 2, 3, 4, 7 | The narrative never gets checked against reality |
| **Process author / owner** | 1, 2, 3, 4 | Corrections have nowhere to land and maps go stale |
| **Frontline practitioner** | 1, 4 | You automate the described job instead of the real one |
| **Clinical leadership** | 5, 6, 7 | The case makes a claim clinical staff cannot support |
| **Finance partner** | 5, 6 | Modelled numbers never become committed ones |
| **Change / adoption lead** | 7, 8 | You buy the thing that fails the way the last one failed |

---

## Part V — Where this sits in the master project plan

### 16. Everything above is one phase

`HH Scheduling_Master Project Plan_July 2026.xlsx` carries the house vocabulary on its **List** tab.
The entire arc documented in Part II maps to a single value in the Phase column:

**Phase** — `Discovery` · `Pre-Pilot Development` · `UAT` · `Active Pilot` · `Enterprise Rollout` ·
`Solution Extensions` · `Ongoing Management`

**Stages 0 through 8 are all `Discovery`.** Six phases remain.

**Category** — `Governance` · `Project Team/OpEx` · `Communications` ·
`Team Member Experience Plan + Recognition` · `Training, Materials & Ambassadors` ·
`Measurement - Analytics & Feedback` · `Shared Services (IT, Contracting, Marketing, Legal)` ·
`Workforce` · `Business Continuity` · `Finish the Job Priorities`

**Status** — `Not Started` · `Predecessor Required` · `In Process` · `Need Assist` · `Complete` ·
`At Risk` · `Past Due` · `On Hold` · `Not Applicable`

### 17. Stage-to-category mapping

Use this to file work in the master plan without inventing new categories.

| Stage | Primary category | Also touches |
|---|---|---|
| 0 Frame | Governance | Project Team/OpEx |
| 1 Discover | Project Team/OpEx | Workforce · Measurement |
| 2 Validate | Governance | Project Team/OpEx |
| 3 Structure | Measurement – Analytics & Feedback | Governance |
| 4 Visualise | Project Team/OpEx | Communications |
| 5 Economics | Measurement – Analytics & Feedback | Shared Services (Legal, Contracting) |
| 6 Business case | Governance | Measurement – Analytics & Feedback |
| 7 Architect | Governance | Shared Services (IT) |
| 8 Market | Shared Services (Contracting, Legal) | Governance · Project Team/OpEx |

### 18. What the precedent rollout gives you for free

The same workbook carries a completed intake-platform rollout — a real precedent, already run to
completion across ~70 locations in four waves. **Do not re-derive its mechanics.** Three assets
transfer directly to the phases that come after Discovery:

1. **The date-tracking legend** — a full calendar of communications, training, office hours and
   surveys expressed as offsets from go-live: intro email at GL−42, Teams channel at GL−28, four
   weekly pre-launch meetings, technical training the Friday before, all-day office hours at GL+1,
   daily office hours for two weeks, then 3×/week, then 1×/week, momentum surveys at GL+3 days and
   weeks 2, 4, 6 and 8. **This is a reusable launch template, not a one-off schedule.**
2. **The wave structure** — waves sequenced by state and EMR/portal readiness, with ambassador
   counts per wave, holiday blackout weeks marked explicitly, and a deliberate slow-roll for the
   largest region. Plus the go-live task list itself: a four-week meeting series with a **formal
   go/no-go at week four**, a readiness checklist, and a daily tiered escalation huddle during
   launch.
3. **The action and issue tracker** — one register, `Action or Issue?` as a field, with owner,
   identification date, target date, status and notes. It is the operational log the phase-gate
   evidence is drawn from.

> **The one thing to carry forward above all others.** The precedent rollout's own structure —
> pre-launch meeting series, ambassadors, momentum surveys, tiered escalation, formal go/no-go —
> is a *change-management machine*. Stage 1 found that change management, not technology, is the
> risk on this initiative (R5). **The machine that de-risks it already exists in this workbook.**
> Use it.

---

## Part VI — If you read nothing else

1. **Do not accept the presented problem.** Test it. Ours was wrong, and the reframe was the single
   highest-value output of the initiative.
2. **Separate what the vendor imposes from what the regulator requires.** Nine of fifty-one
   constraints were the whole case for building; four of the loudest complaints needed no system
   at all.
3. **Solve the planning function before the execution function.** Capacity before scheduling. The
   previous attempt failed for skipping this.
4. **Make it visible before you make it clever.** Phase one is visualisation. Optimisation cannot be
   proven without the baseline visualisation creates.
5. **Give everything an ID and never renumber.** It is what lets a five-week arc stay citable.
6. **Draw current state until the room stops correcting it.** Twenty-six rounds. Count them.
7. **Match the house business-case format, tier every lever, and publish what you cannot yet know.**
   Credibility comes from what you decline to assert.
8. **Write the automation posture as policy before you meet a product.** Then hold every product to
   it — including the one that scores highest.
9. **Force dropdowns on everything comparable.** Free text produces brochures.
10. **Change management is the risk.** Design for the tenured clinician who does not want this. If
    the plan does not survive that person, it does not survive.

---

> **Maintenance.** This playbook is current to **21 August 2026** and covers the Discovery phase
> only. When the initiative clears its next gate, extend Part II rather than starting a new
> document — the value is in the unbroken record.
>
> **Related:** [`initiative-playbook.md`](../agents/compassus-capacity-pm/initiative-playbook.md)
> (the five-phase program from pilot onward) ·
> [`knowledge/`](../agents/compassus-capacity-pm/knowledge/) (the empirical ground truth) ·
> [`artifacts/`](../agents/compassus-capacity-pm/artifacts/) (the working artifacts and the business
> case register)
