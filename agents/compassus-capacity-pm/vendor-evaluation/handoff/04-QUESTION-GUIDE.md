# 04 · The question-by-question guide

For every question: what we are really asking, what a strong answer contains, the red flags, the
gold, and what to cross-check it against. Catalogue ids (`RF-nn`, `G-nn`) point into
`07-RED-FLAGS.md` and `08-GOLD.md`.

A rule that applies everywhere: **which half of a two-part question they skipped is more
diagnostic than what they wrote.** Most questions on this form have a hard half and an easy half,
and vendors reliably answer the easy one.

---

## A1 · Home Care Home Base integration

**What we are asking.** Whether a scheduler will have to work two systems, and whether the
integration is an engineering artefact or a slide.

**A strong answer has** a go-live month and year; a count of HCHB customers; what is read and what is
written back, named; the method from the list they were given; and the hard part almost nobody
answers, a conflict rule for sync latency: which system is authoritative for what, and what happens
when both change.

**Red flags.** *Full*, *seamless* or *deep* integration with no method, date or count (RF-01).
Method contradicts claim: bi-directional claimed, a nightly file drop described (RF-01). Read-only
described as integration. Silence on sync latency (RF-02). Screen automation or database access with
no acknowledgement of the maintenance burden. An unnamed partner delivering it (RF-03). A build
timeline with no engineer, scope or dependency list from us.

**Gold.** Naming what HCHB does not expose and how they work around it (G-03). A conflict rule stated
unprompted (G-03). Naming what they need from us: a sandbox, an interface engine, a named HCHB
contact. Honest not-live with a date, a person and a scope (G-05).

**Feeds** the Home Care Home Base row: twenty points and the Conditional gate. **Cross-check** Section
B how-it's-done for areas 1 to 3 (a live HCHB feed in A1 and *maintained by staff in your product* in
B cannot both be true); C1 and C3 (roster, PTO and auth status have to come from somewhere); C6 (an
outage story that never mentions HCHB means the integration is not load-bearing); A2 (customer counts
must agree).

## A2 · Customers, scale and references

**What we are asking.** Product or prototype; and is home health their business or a side of it.

**A strong answer has** a number of production organisations, three census figures, a percentage
split across home health, hospice and private duty, and a plain *yes* on references.

**Red flags.** One customer: STOP-CHECK (RF-06). *References available on request* without
committing: STOP-CHECK (RF-06). Counts given, magnitude refused. Pilots, letters of intent or logos
counted as production. Home health a minority of the business (RF-16). Numbers that do not
reconcile with A1 or E3 (RF-18).

**Gold.** Naming their largest deployment and saying plainly it is smaller than us (G-02).
Volunteering a customer they lost and why. Offering a reference at operator level, a scheduler or
branch director rather than the executive who signed.

**Feeds** the A2 flag row. **Cross-check** A1, A3 (impact from how many sites), E3 (named
deployments), and the Durability intangible (*are we uncomfortably their largest customer?*).

## A3 · Measured impact

**What we are asking.** Whether they measure anything, and whether they are honest about how.

**A strong answer has** a metric, a magnitude, a period, a baseline method, a number of sites. Bonus:
a metric that did not move.

**Red flags.** Any percentage with no baseline or period: Watch (RF-05). *Up to N%*. Vendor-computed
savings models presented as measurement. Every metric improved by a round number. Impact from one
site presented as product performance. Claims against metrics we did not ask about while silent on
the four we did.

**Gold.** Naming the confound (G-04). A metric that did not move, offered unprompted (G-02). Measuring
something we did not ask for that is obviously right: time to fill a call-out, scheduler hours per
hundred visits, the staff time coordination consumes.

**Feeds** the A3 flag row. **Cross-check** A2 (how many sites could this come from), C1 and C5
(is there a mechanism that could produce the gain), D3 (adoption and impact should come from the same
customers).

## Section B · The coverage matrix

**What we are asking.** Their own claim about breadth, made deliberately cheap to give, so that the
gap between B and C becomes the signal.

**A strong answer has** differentiated marks; a *No* somewhere; statuses that vary; notes that carry
a caveat, a partner name or a target date; *Person does it* where a person does it.

**Red flags.** All eleven *Yes*, all *Production — multiple customers*, all *Automated end to end*
(RF-04). Claims Section C does not support (RF-04). *Through a partner* with no partner named
(RF-03). *Other — see notes* with empty notes. A value not on the dropdown list, meaning the cell was
typed over.

**Gold.** A *No* or *Roadmap — no date yet* on an area they could easily have claimed (G-02). A note
that says what a status means in their case. *Derived from FT/PT allocation* chosen honestly for the
capacity math rather than claiming a live feed.

**Feeds** the nine scope marks, thirty-six points. Do not demote a plain claim for lacking
elaboration; that penalises the form, not the product. **Cross-check** every claim against the C
answer that would evidence it: B1–B3 with C1; B4–B5 with C2 and C3; B6 with C4; B7 with C5; B8 with
C7; B9–B10 with C5 and C7; B11 with D1 and D3. Count the areas claimed and the areas C supports, and
report the two numbers.

## C1 · Capacity

**What we are asking.** Whether they have a capacity model or only a calendar. The embedded test, *a
branch leader is deciding whether to accept a referral today*, is forward-looking and a calendar
cannot answer it.

**A strong answer has** a named unit; a target and a ceiling against it; named input sources;
committed versus open by day, week, discipline and territory; and an answer to the referral question
that is an impact, not a report.

**Red flags.** Capacity that means unfilled calendar slots. Headcount times visits per day with no
weighting. The referral question answered with *the leader can view the schedule*, which is a 1
whatever else is claimed. No mention of SOC-capable clinicians as distinct capacity, the commonest
home health blind spot. Marketing register where a mechanism belongs (RF-17).

**Gold.** Envelope impact shown before a referral is accepted (G-08). Referral inflow and discharge
outflow both modelled. Ramp status as fractional capacity. Per diem as elastic supply. Drive-time
reachability as a capacity input. Capacity and scheduling distinguished unprompted (G-09). Naming
LUPA thresholds, productivity ceilings, the target-versus-ceiling distinction (G-01).

**Feeds** Sophistication, and evidences CAP1–CAP3. **Cross-check** B1–B3 and their how-it's-done
values, A1, A3, C4 (a capacity model with no week view is a day tool wearing a capacity label).

## C2 · Assignment

**What we are asking.** Engine or filter. The three parts rise in difficulty: listing factors is easy,
describing weighting is hard, describing configurability separates product from demo.

**A strong answer has** named factors mapped onto the spec; a named mechanism; which factors are hard
constraints and which are soft weights; and what a customer can change, at what granularity, by whom.

**Red flags.** A factor list with no weighting and no hard/soft distinction (*over forty factors*).
*AI-powered matching* as the whole mechanism (RF-17). *Fully configurable* with no default.
Continuity of care absent. Supervisory-visit dependencies absent. The questionnaire's own words
handed back in the questionnaire's own order. *Removes the scheduler from the loop* (RF-14).

**Gold.** A factor we did not list (G-13). Infection-control sequencing raised unprompted. The
continuity-versus-drive-time tension acknowledged and resolved. A case where the engine deliberately
does not assign and hands to a person. A named substrate: the map data, the cost function.

**Feeds** Sophistication and SCH1. **Cross-check** B5, C7 (does patient availability reach the
matcher), D1 (what the clinician may override), D2 (posture must match mechanism), C5 (same
machinery under pressure, or a cruder one).

## C3 · Readiness

**What we are asking.** Whether they understand that ordered is not schedulable. The most
home-health-specific question on the form and the cheapest way to tell an outsider from an insider.

**A strong answer has** a named state for not-yet-schedulable with reason codes; a release mechanism
when the auth arrives; the compliance window as a hard constraint; and a distinction between held,
released-but-unassigned, and assigned.

**Red flags.** The distinction not made at all: every ordered visit is schedulable, the answer of a
product built for another industry (RF-19). Auth handled as a note field a human watches. *The
scheduler decides when it is ready.* Consent and POA ignored. Compliance windows as a reminder.

**Gold.** Auto-release on auth arrival that then proposes a slot (G-10). *Not yet authorised*
distinguished from *authorised but visits exhausted*. What happens when the window is about to expire
and the visit is still held. Recert or LUPA implications raised unprompted (G-01).

**Feeds** Sophistication and SCH1. **Cross-check** A1 (auth status has to come from HCHB), B4, C1
(does held demand count against the envelope), C5.

## C4 · The week

**What we are asking.** Whether the product optimises a day at a time and calls it a schedule.

**A strong answer has** front-loading behaviour; pace against ordered frequency; day-by-day balancing;
the episode as a unit; and what happens when a week is over-committed.

**Red flags.** A weekly view offered as weekly planning. Front-loading absent. *The optimizer runs
nightly for tomorrow*, a day engine. The episode never mentioned. The word *recert* absent from the
whole return.

**Gold.** Re-plan distinguished from repair: what a mid-week re-optimisation will and will not
disturb (G-16). Naming the stability problem, the sign of someone who has shipped an optimiser. Pace
against ordered frequency with visible variance. Handling of the visit that cannot fit inside the
window.

**Feeds** Sophistication and SCH2. **Cross-check** C1, C2, C5, and D1: if the engine re-plans the
week, what happens to the day a clinician already arranged. That is the sharpest tension on the form.

## C5 · When the plan breaks

**What we are asking.** The operational heart of the form. Four parts: how the need is identified,
how coverage is found and offered, how quickly, and what happens when nobody takes it. The last is the
one that separates a product from a workflow diagram.

**A strong answer has** detection; candidate generation, ranked; direct reach to the clinician by a
named channel; a time figure; and an escalation ladder.

**Red flags.** *A task appears in the scheduler's queue* as the whole answer, which is the labour we
are removing and a 1. No time figure. Nothing on *when nobody takes it* (RF-20). Broadcast with no
ranking. Missed-visit prevention ignored; the spec says *and reducing the occurrence*. Rebooking with
no reference to the compliance window.

**Gold.** A measured time to fill (G-11). A named escalation ladder with times (G-11). Incentives
attached to the hard-to-fill offer, a whole Section B area almost nobody covers. The three cases
separated: call-out, missed visit and patient reschedule are different problems. What they do about
the patient while the coverage hunt is on.

**Feeds** Sophistication, SCH3 and ENG2. **Cross-check** C2, B7, B9–B10, C7, D1 (does declining
coverage cost the clinician anything), A3.

## C6 · When your product is down

**What we are asking.** Whether they have understood they would be critical infrastructure. The
question tells them the stakes; boilerplate after that is itself an answer.

**A strong answer has** a trailing-twelve-month uptime figure with the incidents behind it; a degraded
mode a branch can actually use at seven in the morning; recovery objectives; and a contractual
commitment with remedies.

**Red flags.** No uptime figure: STOP-CHECK (RF-07). No contractual commitment: STOP-CHECK (RF-07).
A figure with no period, no incidents and no SLA document: Watch. Hosting architecture offered as
continuity (RF-07). Nothing on what the customer *does* during the outage. A target with no remedy.
Silence on maintenance windows.

**Gold.** A real outage named, with duration and cause (G-02). A degraded mode a customer has actually
used. HCHB being down treated as a different outage from theirs, with what happens then. A commitment
scaled to criticality.

**Feeds** the C6 flag row. **Cross-check** A1: a deep bi-directional integration needs an outage story
that covers in-flight writes and divergence; silence on HCHB here means the integration is shallow or
unexamined. Also A2 (one customer and twelve months of measured uptime), C5, Durability.

## C7 · Talking to the patient

**What we are asking.** Two things bolted together: the availability-versus-clinical-need conflict,
and how far the automation goes. The second is where our ambition is furthest ahead of the market.

**A strong answer has** when availability is captured, ideally before booking; by whom, through what
channel; a named rule for the conflict; then named channels, an explicit scripted-versus-agentic
answer, what it resolves alone, and the handoff boundary.

**Red flags.** Everything staff-initiated and the answer does not say so (RF-09). Automated reminders
offered as agentic outreach. *Agentic* used without saying what the agent may decide. The conflict
half unanswered. Availability captured after booking. No handoff boundary.

**Gold.** The schedule staying pliable until confirmation, so capacity changes land before the
patient is told (G-17). Mid-conversation takeover by staff (G-17). What they will not let the agent
do, and why. The day-before round run for every patient, every day, rather than as a worklist.
Communication-preference management as a real object, including patients with no mobile phone.

**Feeds** Sophistication, ENG1 and ENG2, and is the sole evidence for the two platform-posture
elements. **Cross-check** B8–B10 how-it's-done (*automated end to end* claimed, a coordinator
worklist described: believe C7), C2, C5, E4 (a vendor who chose not to build patient voice is
coherent, and coherent-and-honest beats claimed-and-thin).

## D1 · What the clinician decides

**What we are asking.** The control surface, in the three-way split the question names; and the
feedback loop when the clinician disagrees. Most vendors answer the first and skip the second. The
second is the whole question.

**A strong answer has** the split stated per decision type; a named approval path; and a real answer
on disagreement: a decline that is logged, a preference weight that updates, a threshold at which a
pattern of declines reaches a human.

**Red flags.** The system decides and the clinician cannot override: STOP-CHECK (RF-10). The mirror
failure: the clinician can change everything, so the optimiser is decorative. *Clinicians love it* as
the answer to a structural question. The disagreement half unanswered, the commonest evasion in
Section D. Overrides possible but invisible.

**Gold.** A decline that feeds a preference weight (G-07). What is locked and why, a sign they have
had this argument with a real clinician. Sequence control distinguished from assignment control. The
clinician's reason for choosing home health acknowledged thoughtfully rather than parroted.

**Feeds** Clinician fit. You supply the evidence and the tension for this row and never a mark.
**Cross-check** D2, C2 (does the override reach the model), C4 (nightly re-plan versus the day a
clinician arranged), C5, E3 (the resistance story should be about exactly this), D3.

## D2 · Decide or advise

**What we are asking.** Where the product's centre of gravity is, and whether it can be moved. There
is no right answer; the test is whether they know where they sit and whether posture is a setting or
an architecture.

**A strong answer has** a clear statement of design intent; whether it is configurable, at what
granularity, and what moving it costs.

**Red flags.** *Both* or *completely flexible* (RF-21). *Advise* claimed while C2 describes an engine
that publishes the schedule directly. *Decide* claimed while C1 and C2 describe a product that only
surfaces information. The configurability half unanswered.

**Gold.** Granularity below the tenant: a per-branch switch with a migration path (G-07). The
sequence named: start advising, earn the right to decide. *We were designed to decide and that is not
easily moved*, honest and worth more than *both*.

**Feeds** Clinician fit. **Cross-check** Sophistication (this is where a 4 becomes an overreach,
RF-14), D1, E3, C5 (recovery is where products quietly move from advise to decide).

## D3 · Adoption

**What we are asking.** Whether they measure adoption, know what healthy looks like, and have six
months of curve, which only real deployments can produce. And the deliberately separated fourth part:
what a clinician sees about their own results.

**A strong answer has** a definition of adoption; a threshold with a number; a six-month shape
including the dip; and a concrete list of what the clinician sees about themselves.

**Red flags.** A single number with no definition or period (*typically over 90%*). Adoption defined
as logins (RF-11). No six-month data, which means not enough deployments; cross-check A2. The
clinician-facing half skipped. A clinician view that is surveillance: productivity against target,
framed as management.

**Gold.** The dip (G-04). A definition that could embarrass them: override rate, proposals accepted
unchanged. The clinician seeing something they value: mileage saved, continuity with their own
patients (G-14). A customer where adoption never reached healthy, and why (G-02).

**Feeds** Clinician fit. **Cross-check** A2, A3 (same deployments, same period), D1 (if overrides
change nothing, an override-rate metric is decorative), E3.

## E1 · What we did not ask

**What we are asking.** Whether they understand our problem better than our questions did. With E4,
the highest-signal answer on the form.

**A strong answer has** one or two specific things absent from the 41 elements and relevant to a
multi-branch home health operation. It reads like a correction to our thinking, not an addition to
their feature list.

**Red flags.** A feature list: reporting, dashboards, mobile, single sign-on (RF-13). Adjacent product
lines pitched. *Nothing, your questionnaire was thorough*, zero information; combined with a thin E4
it means nobody senior read the form. Something they were asked about, restated.

**Gold.** A domain blind spot in our own spec (G-13): payer-mix-aware sequencing, orientation and
preceptor pairing, clinician safety by zip, weekend and on-call load, interpreter needs, the staff
time coordination consumes. A risk named rather than a capability.

**Feeds** Partnership, and is the richest source for *What stands out* and the Home health fluency
intangible. **Cross-check** E4 (added versus left out, read as a pair), and the whole of Section C
(something raised here that contradicts C is a sales voice writing E and a different voice writing C).

## E2 · Sharing in the value

**What we are asking.** Whether they are structurally capable of a partnership, given what Compassus
is bringing. The partnership ladder tops out at open to equity, so this is in part a question about
ownership.

**A strong answer has** a named structure: design-partner pricing with terms, a co-development lane
with capacity committed, revenue share, equity or warrants, roadmap governance with a named seat; and
evidence they are set up for it, who decides, whether they have done it before.

**Red flags.** A discount (RF-12). *We're open to discussing* (RF-12). Enthusiasm without structure.
Co-marketing accepted, value-share ignored: they took the free half. The shortest answer in an
otherwise expansive return (RF-22). A services contract dressed as partnership.

**Gold.** Ownership raised unprompted (G-12). Naming what they want from us in return, hours, a
branch, data rights: obligations on both sides make it real. A general-market ambition stated
honestly. Naming their constraint: *our board would need to approve equity; here is what we can do
without it.*

**Feeds** Partnership; read all four E answers, not only E2. **Cross-check** A2 and Durability (a
twelve-person company offering equity and a large platform offering a discount are telling us
different things), E3, E1 and E4, A1 (a not-yet-live vendor offering a design-partner structure is
proposing that we fund the build; say so plainly).

## E3 · Deployment and change management

**What we are asking.** Whether they have done this with clinicians who did not want it. The question
cannot be answered abstractly: it asks for a deployment where clinicians resisted, and what they
changed as a result. The trap is the last five words.

**A strong answer has** named deployments with shape; what they learned; what is critical to get
right; and the resistance story with all three parts: who resisted, why, and what the vendor changed
in the product or the method.

**Red flags.** A methodology diagram with no story in it (RF-23). A resistance story resolved by more
training or better communication, meaning the clinicians were right and nothing changed (RF-23).
The failure blamed on the customer. No resistance story at all. Change management described as the
customer's job. Phasing that assumes one branch and one go-live.

**Gold.** A change made to the product because clinicians pushed back (G-06). The role that decides
adoption named, and how they work with them. A deployment that went badly, named as such. A
precondition that costs them time: *we will not go live until X.*

**Feeds** Partnership, and is evidence for Clinician fit. **Cross-check** A2, D1 and D2 (the story is
usually a D1/D2 story), D3 (the curve should show what the story describes), E2.

## E4 · What you chose not to build

**What we are asking.** Product judgment and candour in one question. A vendor with an answer has a
thesis; one without has a backlog.

**A strong answer has** a specific thing, named, and the principle behind leaving it out.

**Red flags.** Roadmap items reframed as choices. *Nothing, we build whatever customers need*, which
is the absence of a product (RF-24). Something they were never going to build anyway. A boundary
that is inside our scope and was marked in scope in Section B (RF-04, a live contradiction).

**Gold.** A boundary with a principle (G-15). Something they built and then removed. A boundary that
costs them this deal and they name it anyway (G-02).

**Feeds** Partnership, and more or less scores the Candor intangible by itself. **Cross-check**
Section B (the sharpest contradiction detector on the form), C7, E1.

---

## The two-halves list

The questions with a hard half vendors skip. Report the skipped half as a fact and an ask.

| Question | The easy half | The hard half |
|---|---|---|
| A1 | What it reads | The conflict rule when both sides change |
| A2 | How many customers | The census of the three largest, and the split |
| A3 | What improved | Over what period, against what baseline |
| C5 | How coverage is offered | What happens when nobody takes it |
| C6 | What happens in an outage | What the customer can do during it, and what is contractual |
| C7 | The channels | The conflict rule, and the handoff boundary |
| D1 | What the clinician can change | What changes when they disagree |
| D2 | Where they sit | Whether a customer can move it |
| D3 | An adoption number | The six-month curve, and what the clinician sees |
| E2 | Enthusiasm | Structure and terms |
| E3 | The method | The resistance story and what changed |
