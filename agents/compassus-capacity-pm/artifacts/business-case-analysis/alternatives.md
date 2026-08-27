# Alternatives Assessment — Capacity and Scheduling

> **Question this document answers.** The proposed capacity-and-scheduling platform is the expensive
> option. Before it is bought, what fraction of its claimed value can be captured without it — by
> configuration, deletion, policy, labour arbitrage, reorganisation, hiring, or internal build — and
> what does the platform have to deliver *over and above* the best of those to earn its premium?
>
> **Posture.** The platform is the defendant, not the plaintiff. Every alternative below is credited
> with everything it can plausibly deliver, and the platform is charged with everything it costs.
> Where an alternative wins, this document says so.
>
> **Status.** 21 August 2026. Sources: the Compassus discovery corpus
> (`compassus-capacity-pm/agents/compassus-capacity-pm/knowledge/`), the initiative's own
> `business-case-register.md` and `constraint-register.md`, and external research. **Every dollar
> figure is illustrative unless marked otherwise.** The convention of the register is kept: where a
> number cannot be sourced, the document names what to measure rather than inventing one.

---

## 0. The single most important finding, stated first

**Compassus's own functional scorecard already says the incumbent covers most of the requirement.**

From `business-case-and-kpis.md` §3, the `Footprint & Fit` tab of the 13 August workbook:

| | HCHB Web Scheduling | HCHB Smart Scheduling | Combined |
|---|---:|---:|---:|
| Overall weighted rating | 62.1 | **71.2** | — |
| Average category coverage (footprint) | 32.6 | 54.8 | **57.4** |
| Categories covered | — | — | **26** |
| Categories still a gap | — | — | **6** |

Two products are scored in that workbook. **Both of them are HCHB.** The combination Compassus already
licences — or can licence from its incumbent — covers 26 of 32 functional categories at an average
footprint of 57.4, and leaves six gaps: capacity ramp status, referral-volume context, SOC/recert/F2F
compliance windows, patient preference, caregiver availability, and coordination-time load.

The initiative's own artifact therefore establishes the correct framing for the whole business case:

> **The platform is not being bought to cover the requirement. It is being bought to cover six
> categories, and to fix nine constraints that HCHB cannot configure away.** Everything else on the
> claimed benefit list is available at configuration cost, policy cost, or labour cost.

That is not an argument against the platform. It is an argument that the platform's business case must
be rewritten to charge itself only with the incremental value, and that the alternatives below must be
run **first** regardless of the platform decision — because they are cheaper, faster, and several of
them are prerequisites for the platform working at all.

---

## 1. What the platform claims, and how much of it is contestable

Taken from `artifacts/business-case-register.md`. The right-hand column is this document's assessment
of whether the lever survives without a platform.

| Lever | Register's sizing | Available without a platform? |
|---|---|---|
| **W1** Scheduler capacity released (~300 → ~100) | ~$12M/yr | **Partly, and by two rival routes.** Offshoring attacks the same $12M directly. Configuration and deletion remove some of the work itself. Neither reaches 200 roles alone. |
| **W2** Auth notification noise (~11 FTE) | inside W1, ~$0.66M | **No — not by configuration.** `CN-23` is classified a *product limit*: HCHB regenerates the workflow daily and cannot be told to notify on state change only. Requires a vendor change or a filter layer (Option G). |
| **W3/W4** Premium labour and overtime offset | input missing | **Partly.** Forward visibility is the mechanism; analysts with the HCHB data warehouse produce forward visibility (Option G/F). |
| **W5** PTO collision avoidance | "committed, near zero cost" | **Yes, entirely.** The Workday↔HCHB interface exists and is switched off. This lever is already an alternative — it is in the platform case only because nobody has turned it on. |
| **W6** Travel and drive time | directional | **No.** Requires a routing engine. HCHB suggests a route today; quality is the gap. |
| **W7** Unpaid evening confirmation work (~3,000 clinicians × 30 min/day) | directional | **Partly.** Patient-engagement messaging is separable from capacity and scheduling and is procurable as a point solution. |
| **R1** Non-billable visits avoided | input missing | **Partly.** Surfacing payer rules at POC creation (`CN-33`) is a policy change; the data is already captured. |
| **R2** LUPA leakage, clinically gated | ~$2.2M/yr | **Partly.** `CN-34` — the daily LUPA report from Pulse already exists as policy and is inconsistently run. Enforcement is free. Event-driven alerting is not. |
| **U1** Discipline/role match (PT→PTA, RN→LPN) | ~$1.9M/yr | **Mostly yes.** `DE-08` is a *policy default*, not a product feature. HCHB filters the assignable list; it does not push work down. Policy + audit captures most of it, leakily. |
| **U3** Rebook waste | input missing | **Partly.** A defined call-out recovery protocol is a standard-work change. |
| **G1** SOC throughput / growth | upside, ~$11M on a 2% lift | **Partly.** Freed PT/RN start capacity comes largely from U1, which is a policy lever. |
| **Q1** Value-based performance | ~$1.3M at the house 0.5% convention | **Indirect either way.** Not attributable to the platform without an instrumented baseline that does not exist today. |

**Reading of the table.** Of the register's levers, the ones that *require* a platform are W2, W6, and
the measurement infrastructure behind W3/W4 and R1. The ones that do not are W5, U1, most of R2, and a
large share of R1 and U3. **The largest lever of all, W1, is contested by an alternative that is
cheaper and faster than the platform — offshoring — and that is the central commercial fact of this
assessment.**

---

## 2. Option A — Turn on what is already owned

### A.1 What is switched off

Four items are named explicitly in the corpus as existing, owned or licensable, and not in use.

| Item | Source | What it does | Class |
|---|---|---|---|
| **Workday → HCHB PTO interface** | Discovery §5; register W5 | Approved PTO in Workday creates unavailability in HCHB automatically. Today PTO is hand-keyed by scheduling staff, and five of seven nurses can be approved off the same day. | Integration exists, not activated |
| **Shift Finder** (self-service open visits) | `CN-19` | Clinicians see uncovered visits with a patient snapshot and distance, and can accept one; acceptance generates a back-office approval task. | HCHB feature, not enabled |
| **Visit dispatching / Smart Scheduling recommendation** | `CN-20` | Recommends the next best assignee for a declined or uncovered visit and returns it to the scheduler for approval. **It deliberately does not auto-assign.** | HCHB feature, not enabled |
| **Rapid reschedule flag** | `process-facts-2026-08.md` | Branch-level configuration flag. When on, a clinician moving **their own** visit inside the Medicare week generates **no scheduler workflow at all.** | Branch config, inconsistently set |

Plus the module-level question: **HCHB Smart Scheduling itself**, piloted in Alabama and abandoned.

### A.2 The three findings that matter here

**Finding A-1 — the interaction model the initiative designed already exists in the product.**
`DE-09` is "the tool recommends; the human accepts." `CN-43` is the documented failure mode that makes
that non-negotiable. `CN-20` records that HCHB's visit dispatching **already works exactly that way and
deliberately does not auto-assign.** The initiative is not designing an interaction model HCHB lacks.
It is designing a better recommendation behind an interaction model HCHB already ships.

> The gap is *quality of recommendation*, not the interaction model. That is a much narrower — and much
> more testable — claim than "we need a scheduling platform."

**Finding A-2 — Smart Scheduling was never actually piloted, so its failure is not evidence.**
The discovery record is unambiguous: the Alabama pilot failed because leaders constrained the system to
mirror manual process, clinicians rejected out-of-territory assignments, and leadership allowed the
resistance. *"It was never truly piloted."* A business case that uses that failure to justify buying a
different system is using a change-management failure as a technology verdict. **The same change
management that sank Smart Scheduling will sink the platform** — and it is cheaper to discover that on
a module already owned.

**Finding A-3 — Shift Finder and dispatching are free options on the platform's own hypotheses.**
The constraint register says this outright: two of the four configurable items "would let us **test
demand for capabilities we are otherwise planning to build**." Enabling Shift Finder answers, for
roughly the cost of a configuration project, whether clinicians will self-serve open visits at all —
the load-bearing assumption under the platform's call-out-recovery and marketplace features. The
register also names the failure mode honestly: *the good visits get taken and the awkward one is left.*

### A.3 Cost

| Line | Estimate | Basis |
|---|---:|---|
| Workday↔HCHB interface activation, testing, cutover | $80k–$200k one-off | Interface exists; cost is HCHB professional services + internal integration/testing. **Estimate.** |
| Shift Finder + visit dispatching enablement | $50k–$150k one-off | Configuration, policy design, clinician comms. **Estimate.** |
| Rapid-reschedule flag standardisation across ~80 branches | <$25k one-off | Branch config plus a policy decision. **Estimate.** |
| HCHB Smart Scheduling module licence, if not already held | unknown — must be obtained from HCHB | HCHB does not publish pricing. **Named as an information gap, not estimated.** |
| Configuration + change-management team, 12 months | $600k–$900k | 3 FTE (config analyst, clinical change lead, comms) fully loaded, plus training delivery across 80 branches. **Estimate.** |
| **Year-1 total, excluding any Smart Scheduling licence** | **$0.75M–$1.3M** | |
| **Recurring** | **$0.2M–$0.4M/yr** plus licence | Sustaining config and training |

### A.4 Realistic benefit capture

| Register lever | Captured by Option A | Reasoning |
|---|---|---|
| W5 PTO | **100%** | This is literally the lever. Free, immediate. |
| W1 scheduler release | **10–20%** of the 200 roles | Rapid reschedule removes in-week reassignment workflow, the highest-frequency routine touch. Shift Finder removes part of coverage brokering. Neither touches the SOC/recert burst or auth chasing. |
| W3/W4 premium labour | **10–20%** | Shift Finder surfaces open visits to per-diem and float before a contract call is made — `CN-47` says per-diem capacity is "the biggest available weapon against capacity constraint, and it is being left on the table." |
| U3 rebook waste | **20–30%** | Self-service coverage shortens the recovery loop. |
| W2, W6, R1, capacity forecasting | **0%** | Product limits and absent capability. Configuration cannot reach them. |

**Indicative value: $1.5M–$3.0M/yr**, against $0.75M–$1.3M year-1 cost. **ROI is strong and the payback
is inside a year.**

### A.5 Time to value and risk

- **Time to value:** PTO interface 60–90 days. Rapid reschedule 30 days. Shift Finder and dispatching
  90–180 days including clinician communication. **All of it inside 6 months.**
- **Risks.** (1) The Alabama failure mode repeats — clinicians reject machine-suggested assignments and
  leadership permits it. This risk is *identical* for the platform, which is the point. (2) Shift
  Finder cherry-picking leaves the hard visits stranded; needs a rule that pairs an awkward visit with
  an attractive one or attaches an incentive (`CN-46` warns about holdout behaviour). (3) Turning on
  live location (`CN-21`) is a leadership decision with a clinician-trust cost and should be excluded
  from this package.
- **Dependency the platform case must acknowledge:** if Option A is not run, the platform inherits an
  unvalidated assumption that clinicians will self-serve. If Option A *is* run and fails, the platform
  should not be bought in its current shape.

### A.6 Verdict

**Run this regardless.** It is the cheapest, fastest, lowest-risk item on the list; it captures a
lever the platform case already counts (W5); and it de-risks or kills the platform's core adoption
assumption for around 1–3% of the platform's likely lifetime cost. **No platform decision should be
taken before Shift Finder and visit dispatching have been enabled and measured.**

---

## 3. Option B — Delete the workflow rather than automate it

The organisation's own session reached this conclusion before any vendor did:

> *"That workflow shouldn't exist to begin with for the scheduler."*
> **Some workflows should not be automated. They should not exist.**

### B.1 The three named candidates, correctly classified

This is where a naive alternatives analysis goes wrong. Two of the three "just switch it off" items are
**not ours to switch off.** The constraint register already made that call.

| Candidate | Constraint register class | Can we delete it? |
|---|---|---|
| **Routing every physician order to a DCS for approval** | `CN-18` — **HCHB configurable, within our control today** | **Yes.** An HCHB toggle, not a Medicare requirement, and not done at other agencies. |
| **Per-discipline task duplication** (4 disciplines → 8 tasks) | `CN-26` — **HCHB product limit** | **No.** Requires a vendor change or a replacement system. Care-team-at-referral (`DE-05`) is the design answer, and it needs a product that supports it. |
| **50–60 daily non-actionable auth notifications** | `CN-23` — **HCHB product limit** | **No.** *"Notify on state change, never on state persistence"* is not configurable. Requires an HCHB enhancement or an external filter layer (Option G). |

**This is a material correction to the alternatives thesis.** "Delete the workflow" is a genuine and
powerful strategy, but as scoped by the corpus it delivers **one** of the three headline items by
configuration. The other two are exactly the kind of thing you buy a platform — or commission a vendor
change — to fix.

### B.2 What deletion is genuinely available

| Deletion | Mechanism | Value | Risk |
|---|---|---|---|
| **DCS approval on physician orders** (`CN-18`) | HCHB toggle; options are full off, selective off for clinicians with a demonstrated record, or AI adjudication of black-and-white cases with escalation | Named as **the largest single source of DCS workflow backlog, which delays visit addition**. Removing it unblocks a hard stop upstream of scheduling — it accelerates every add-on order in the business. | **This is a company-level risk decision, already flagged as such.** The retained benefit is utilisation oversight, better served by reviewing utilisation reports than clicking every order. Mitigation: retrospective sampling audit plus a utilisation report the DCS actually reads. |
| **The hour-long daily afternoon huddle** (`CN-38`) | It is *"the manual compensation for the absence of a shared capacity view"* — so it cannot be deleted until a capacity view exists. **The session's own estimate with one: 15 minutes.** | 45 min/day × DCS + clinical managers + schedulers across ~80 branches. At 4 attendees × 80 branches × 45 min × 250 days ≈ 30,000 hours ≈ **14 FTE ≈ $0.9M/yr.** *Estimate.* | Cannot be banked until the capacity view exists. **This is a platform-dependent deletion, and it belongs in the platform's case, not the alternatives' case.** |
| **The discretionary daily LUPA report** (`CN-34`) | Policy exists; compliance is inconsistent. Either enforce it or replace it with event-driven alerting. | Enforcement is free and feeds R2. | Enforcement without alerting is fragile — `section 12` of the register forbids any saving that depends on a specific manager working weekends. |
| **Bulk-clear behaviour** (`CN-39`) | Cannot be deleted while `CN-23` persists. Schedulers bulk-clear *because* the notifications are noise. | — | **The behavioural cost exceeds the time cost.** 11 FTE of reading time is ~$0.66M; the cost of clearing the one actionable item is unmeasured and larger. |

### B.3 Cost and benefit

| Line | Estimate |
|---|---:|
| Risk assessment, legal/compliance sign-off, control design for DCS order-approval removal | $75k–$150k one-off |
| Retrospective utilisation-audit capability (sampling, reporting, 1 FTE UR analyst) | $120k–$160k/yr |
| Policy enforcement and audit for the LUPA report | inside Option C |
| **Total** | **~$0.2M one-off, ~$0.15M/yr** |

**Indicative value: $0.5M–$1.5M/yr**, almost entirely as *throughput* (orders reaching scheduling
faster → visits added sooner → fewer non-billable and fewer LUPA-adjacent periods) rather than as
removable headcount. The DCS time released is real but is clinical-leadership time, which is
redeployed rather than removed.

### B.4 Time to value and risk

- **Time to value: 90–180 days**, gated entirely on the executive risk decision, which is already
  sitting in the open-decisions document.
- **The risk is real and should not be minimised.** Order approval is a clinical-governance control.
  Turning it off transfers oversight from prospective to retrospective. In Review Choice Demonstration
  states the documentation exposure is higher. The mitigation — selective removal for clinicians with a
  demonstrated record — is the correct middle path and is already on the table.

### B.5 Verdict

**High value per dollar, but smaller than it first appears, and it is a governance decision rather than
an investment decision.** Run it. But be honest in the business case: two of the three headline
deletions are HCHB product limits, and they are part of the *argument for* the platform, not part of
the argument against it.

---

## 4. Option C — Process and policy change with no technology

This is the option the corpus itself rates highest per unit of complexity, and it is the one most
likely to be under-credited in a vendor-led business case.

### C.1 The interventions

**C-1. Surface payer rules at plan-of-care creation.** `CN-33`, and named twice in the corpus as *"the
highest-value, lowest-complexity win."* The auth team already captures payer specifics in a
coordination note at verification, days before anyone writes the plan of care, using a template snippet
introduced early last year. **The data exists. It is simply not in front of the clinician at the moment
frequency is written.**

- Mechanism today: plans of care are written to clinical need with no visibility of the payer's visit
  budget. UHC gives 5 nursing visits and requires 4 of 5 completed plus documentation before visit 6.
  Indiana Medicaid pays 30 days from the *discharge* date with 8 visits shared across PT/OT/ST. *"UHC
  was never going to give you more auth. We're not creating our plans of care based on the insurance."*
- Zero-technology implementation: a per-payer one-page rules card, maintained by the auth team,
  attached to the referral packet and required to be acknowledged at POC creation; plus the existing
  coordination-note snippet promoted to a mandatory field in the eval workflow.
- Why it is also a **patient-care** win, not only a throughput win: abrupt discharges happen because
  nobody planned for the real visit budget.
- **Ceiling on the manual version:** a card is a document, not a constraint. It informs; it does not
  enforce. Adherence will decay. The structured version — payer rules as a checked constraint at POC
  creation — is a platform capability.

**C-2. Standard work for the readiness call.** `CN-31` and `CN-40`. The policy already exists and is
required everywhere; it is not universally performed, and *at least one scheduler refuses it outright,
reasoning that confirmation is growth's job.* The documented consequence: a clinician shifted two visits
to her PTA to make room for an SOC, nobody confirmed the patient was home, the patient was still in
hospital, **and she lost half a day of income.**

- Zero-technology implementation: a scripted call with a checklist, a completion field that gates SOC
  assignment, a weekly compliance report by branch, and a named owner. Plus resolution of `CN-32` — is
  first patient contact owned by growth or by scheduling? Today it is assumed, not verified.
- This is the cheapest intervention in the entire assessment and it directly protects the most
  expensive asset in the business: a clinician's productive day.

**C-3. A defined call-out recovery protocol.** Bottleneck #7. *"There is no established process."*
Today everyone stops, including workflow, and non-clinical schedulers open charts one at a time to
triage clinical priority. It cascades into the following days.

- Zero-technology implementation: a written triage tier (SOC → IV → wound → labs due → ortho →
  routine), owned by the DCS, published in advance so the scheduler can act without pulling a clinician
  in; a pre-agreed coverage call list by territory; a same-day escalation clock with a defined timeout
  before the patient must be called; and a rule that the patient is notified **early in the day**, not
  at the end.
- Secondary, and larger: `CN-41` — clinicians have stopped calling in for backup visits because they do
  not trust the branch to respond efficiently, so **they absorb the gap and take one less patient.**
  Latent capacity is being lost to a trust deficit, and *the fix is response speed before it is any
  feature.* A published protocol with a response-time commitment addresses that directly.

**C-4. Front-loading policy.** The published evidence in the register supports it: one to two visits per
week outperformed higher frequencies, and a delayed first visit carried four times the rehospitalisation
odds. This is a clinical-policy change expressed in the plan-of-care standard, not a product feature.
It is also the one lever in this section that touches quality-linked revenue (Q1) and it costs nothing
but clinical governance time.

**C-5. Discipline-role match defaults.** `DE-08` / `CN-45`. Default routine therapy visits to the PTA
and routine nursing to the LPN, **with explicit opt-out** — *"they have to opt out versus opt in."*

- **This is a policy lever, not a product lever.** HCHB filters the assignable list by profile but does
  not push work down. The register sizes it at **~$1.9M/yr** on episodic revenue alone (30 dollar loaded
  cost differential, therapy at ~40% of 1.07M episodic visits, 15% shift) *before* counting the freed
  evaluation capacity, which is worth more because starts are where growth is blocked.
- **The manual version leaks.** Without a system default, the change depends on a leader making it every
  time — which is exactly what `CN-45` says is failing today, *"partly habit, partly protecting their own
  volume."* Realistic manual capture: **40–60%** of the modelled value, with decay.
- **A hard open question the corpus flags:** paraprofessional supply. LPNs are getting harder to hire
  and some markets have no workable PTA-to-PT ratio. **Check market by market before switching the
  default on.**

### C.2 Cost

| Line | Estimate |
|---|---:|
| Standard-work design team (1 clinical ops lead, 1 process analyst, 12 months) | $280k–$350k |
| Payer rules card build and maintenance (auth team, 0.5 FTE ongoing) | $45k/yr |
| Training delivery and audit across ~80 branches | $200k–$350k year 1, $100k/yr after |
| Compliance reporting (built on existing HCHB reports) | inside Option F/G |
| **Year 1** | **$0.5M–$0.75M** |
| **Recurring** | **$0.25M–$0.35M/yr** |

### C.3 Realistic benefit capture

| Lever | Register sizing | Captured manually | Indicative |
|---|---|---|---|
| U1 discipline/role match | $1.9M/yr | 40–60%, decaying | **$0.8M–$1.1M/yr** |
| R1 non-billable visits avoided | unsized | payer-rules card catches the gross cases | **$0.3M–$0.8M/yr**, *unverifiable until R1 is measured* |
| U3 rebook waste / call-out cascade | unsized | protocol + response-time commitment | **$0.3M–$0.6M/yr** |
| Latent capacity recovered from `CN-41` trust deficit | unsized | clinicians resume calling in for backfill | **not valued — name it, do not price it** |
| Q1 quality / front-loading | $1.3M at the house convention | attribution impossible without a baseline | **not valued** |

**Indicative value: $1.4M–$2.5M/yr** against $0.5M–$0.75M year-1 cost.

### C.4 Time to value and risk

- **Time to value: 60–120 days for design, 6–12 months for adoption.** Faster to start than anything
  else here; slower to fully land than a configuration change, because it is behaviour.
- **The risk is decay, and it is the specific risk the register already legislates against:** *"Any
  saving that depends on a specific manager working weekends… If it is not encoded as standard work, it
  is not a business case."* Policy captured in a document, audited by a report someone must remember to
  run, degrades. `CN-34` is the proof — the daily LUPA report is *policy today* and compliance is
  inconsistent.
- **The second risk is the paraprofessional supply constraint on C-5**, which is a labour-market fact,
  not an execution failure.

### C.5 Verdict

**The highest return on invested dollar of any option in this document, and the one most likely to be
skipped because it is unglamorous and has no vendor to champion it.** It also happens to be the option
whose principal weakness — decay — is precisely what a platform fixes, by converting policy into an
enforced default. That makes Option C both the strongest alternative *and* the clearest articulation of
what the platform is actually for.

---

## 5. Option D — Outsource or offshore the scheduling function

**This is the platform's real commercial competitor, and the business case does not currently
acknowledge it.**

W1 — releasing ~200 of ~300 scheduler roles at ~$60k loaded, ~$12M/yr — is the largest hard lever in
the whole initiative. A BPO contract attacks that identical number, contractually, in 9–12 months,
with no adoption risk from clinicians and no dependence on HCHB's roadmap. Any steering committee that
sees the platform case without seeing this one has not been given the choice.

### D.1 The economics

| Delivery model | Indicative fully-loaded cost per FTE per year | Note |
|---|---:|---|
| Compassus in-house scheduler (today) | **~$60,000** | The register's own assumption; must be replaced with the actual loaded cost (register §9) |
| US-domestic healthcare BPO | **~$50,000–$75,000** | Rarely a saving on a self-performed function; bought for elasticity and management, not price |
| Nearshore (LatAm — Colombia, Mexico, Costa Rica, Dominican Republic) | **~$28,000–$45,000** | Time-zone overlap and English fluency; the practical option for anything voice-facing |
| Offshore (Philippines, India) | **~$18,000–$32,000** | The headline arbitrage; typical vendor claims of 40–60% saving against US cost |

*All figures are indicative market ranges for dedicated healthcare RCM, prior-authorisation and patient-access
FTEs. Treat as estimates for scoping only; obtain quoted rate cards before any number reaches a
business case.*

**Gross arithmetic, before overheads.** If 200 of 300 roles are offshorable at a $30k differential:
**~$6.0M/yr gross.** At a $40k differential: **~$8.0M/yr gross.**

**Net arithmetic, after the costs that get left out.** The consistently under-budgeted lines are:

| Line | Typical load | Effect |
|---|---|---|
| Transition and knowledge transfer (3–6 months of parallel running) | one-off, 15–25% of first-year contract | Delays payback into year 2 |
| Retained vendor-management function (contract, SLA, QA, escalation) | 5–10% of contract value, ongoing | Roughly 8–15 retained FTE |
| Quality assurance and rework | 5–15% effective loss | The dominant hidden cost in payer-specific work |
| Attrition and re-ramp | offshore BPO attrition commonly **30–50%/yr** | Payer-rule knowledge is re-learned continuously |
| Technology, access, security, connectivity | one-off plus ongoing | HCHB access provisioning, Citrix, VDI |

**Realistic net capture: 50–70% of the gross**, i.e. **~$3.5M–$5.5M/yr recurring** on a 200-role scope,
after a year-1 transition cost of roughly **$1.5M–$3.0M**.

> **That is the same order of magnitude as the register's W1 lever, achievable faster, with contractual
> certainty rather than adoption risk. It is the strongest single-lever challenge to the platform's
> economics in this document.**

### D.2 The four objections, taken seriously

**1. It makes the waste cheaper; it does not remove it.**
This is the decisive strategic objection and it should be stated plainly. Offshoring 55 non-actionable
auth notifications a day means paying less per notification. `CN-23` still regenerates them daily.
`CN-26` still fires eight tasks for a decision already made. **The BPO buys a lower unit cost on a
process the organisation has already concluded should not exist** — *"That workflow shouldn't exist to
begin with for the scheduler."* Every dollar of arbitrage also entrenches the workflow, because a vendor
paid per FTE has no incentive to reduce the FTE count and a contract priced per FTE makes future
automation a commercial renegotiation rather than an operational decision.

**Mitigation, and it is a real one:** price the contract **per transaction or per admission**, not per
FTE, with a scheduled unit-price decline. That aligns the vendor with volume reduction and preserves the
option to automate. Most healthcare BPO contracts are FTE-priced; transaction pricing must be
negotiated deliberately and is the single most important term in the deal.

**2. It destroys the part of the function that actually works.**
`CN-48` again: *"Coverage recovery runs on relationships… a scheduler has built enough goodwill to ask a
favour on a Friday afternoon."* `DE-10` already decided to preserve a local human role for urgency,
local knowledge and relationship-based coverage. And the readiness call — **the scheduler's one true
judgment call**, the call that determines whether a clinician is sent to a patient who is not home — is
patient-facing, is often the patient's first contact with Compassus (`CN-32`), and in
Washington/Providence carries a **mandated safety screening script instituted after a clinician was
killed in a patient's home** (`CN-37`).

**This draws the scope line for you.** Offshore the transactional: auth chasing and follow-up,
task processing, assignment execution against a plotted plan of care, notification triage, missed-visit
documentation chasing, report production. **Retain onshore and local:** the readiness call, call-out
recovery, clinician relationship, anything with a safety script. That is perhaps **60–70% of the
scheduler workload**, not 100% — which reduces the gross lever proportionally.

**3. HIPAA, BAAs and payer contracts.**
- **HIPAA does not prohibit offshoring PHI.** A business associate agreement can be executed with an
  offshore entity, and the covered entity remains liable for its business associate's conduct. There is
  no federal onshore-only rule for home health.
- **But enforcement reach is materially weaker abroad**, which is why the practical constraints come
  from elsewhere: **Medicare Advantage offshore-subcontractor attestation requirements**, **state
  Medicaid contracts that prohibit offshore PHI access outright in several states**, and
  **onshore-only clauses that appear routinely in commercial payer and health-system JV agreements.**
- Compassus's book is **~53% non-episodic** — commercial, MA and Medicaid. **The payer contracts are
  where this dies, not HIPAA.** A contract review across the payer portfolio and the JV agreements
  (Providence, Ohio Health, BSMH and the Florida JVs are all named in the corpus) is a mandatory
  precondition and will likely carve out a meaningful share of the book.
- **Action:** before any BPO RFP, run a clause review for offshore restrictions across the top payer
  contracts and every JV agreement. *This is a two-week legal task and it determines whether Option D is
  a $5M option or a $2M option.*

**4. Quality and turnover.**
Offshore healthcare BPO attrition is commonly reported in the **30–50%** range annually, against a
process whose difficulty is **payer-specific rules that are not written down anywhere** — the register
calls the payer rules library *"contract-level data that nobody publishes."* Handing that to a workforce
that turns over every two to three years, without first building the rules library (Option C-1 /
Option G), guarantees rework. **Sequence matters: build the payer rules library first, then outsource
against it. Outsourcing into undocumented tribal knowledge is the classic failure.**

### D.3 Cost, capture, time to value, risk

| | |
|---|---|
| **Cost** | Year 1: **$1.5M–$3.0M** transition and parallel running, plus contract. Recurring: contract at ~$4M–$6M/yr replacing ~$9M–$12M of in-house cost on the offshorable scope, plus **$0.6M–$1.0M/yr retained vendor management.** |
| **Realistic net benefit** | **$2.5M–$4.5M/yr** once the readiness call, call-out recovery and payer-restricted book are carved out |
| **Time to value** | **9–15 months** to steady state; first savings in month 6–9 |
| **Risks** | Entrenches workflow that should be deleted · destroys `CN-48` relationship capital · payer and JV contract restrictions may carve out half the book · attrition against undocumented payer rules · reputational and clinician-morale cost of visible offshoring in a workforce already under strain · **very hard to reverse** |

### D.4 Verdict

**Credible, large, and the honest competitor to W1 — but it is a cost strategy, not an operating
strategy, and it forecloses the deletion agenda the organisation has already committed to.** It should
be modelled explicitly in the business case as the alternative use of the same capital, and it should be
scoped as **transactional-only, transaction-priced, and sequenced after the payer rules library exists.**
If the steering committee's objective is purely administrative cost reduction, Option D beats the
platform on speed and certainty and the platform case must say why it is nonetheless the better buy.

---

## 6. Option E — Centralise scheduling into regional or national hubs

*(Centralisation is the in-house form of Option D, and its practical prerequisite: a function that has
been standardised into hubs can be outsourced; 80 idiosyncratic branch practices cannot.)*

### E.1 The case for it, from the corpus

The corpus makes the case for centralisation more strongly than it makes the case for any product:

- **"Branch-to-branch variability is extreme and unmanaged. High performers reassign coverage in
  minutes; low performers take hours, during which clinicians idle and patients wait."**
- Efficient branches update the scheduling grid dynamically through the day; inefficient branches update
  it weekly, by hand.
- HCHB productivity reports are *"applied non-uniformly across branches."*
- Per-diem policy is inconsistent branch to branch (`CN-36`) — some enforce a monthly minimum, others
  carry per diems who *"have not turned on a device in three months"* — which makes per-diem capacity
  unforecastable.
- Some branches decline to use per-diem staff at all, and `CN-47` records the consequence plainly:
  **those branches forfeit the ability to grow.**

**When variance between operating units is that wide and the mechanism is known, consolidation is the
standard remedy and it does not require software.** Moving ~300 schedulers from ~80 branch pools into,
say, 4–6 regional hubs of 50–70 with a single supervisor, one standard operating procedure, one
queueing discipline and one measurement set is a conventional shared-services move.

### E.2 What it plausibly delivers

Consolidation of a fragmented administrative function yields productivity through four mechanisms, all
of which apply here:

1. **Queue pooling.** 80 small independent queues have materially worse utilisation than 5 pooled queues
   of the same total size. This is arithmetic, not opinion: variance in arrival rate is absorbed by the
   pool. The scheduler's day is exactly the shape that benefits — bursty SOC arrivals, unpredictable
   call-outs.
2. **Span of control and supervision.** 80 branch managers supervising 3–4 schedulers each cannot run a
   quality system. 5 hub supervisors can.
3. **Standardisation.** One SOP replaces 80. The high-performer practice becomes the baseline instead of
   an anecdote.
4. **Specialisation.** Split the role: auth chasing, SOC and readiness calls, exception recovery. Today
   one person does all three badly because all three interrupt each other.

**Indicative capture: 15–25% of scheduler FTE**, i.e. **45–75 of 300 roles, ~$2.7M–$4.5M/yr.**
*Estimate. This is the range typically observed when a fragmented back-office function is consolidated;
it must be validated against a Compassus time study before it is committed.*

Note carefully what that means: **centralisation alone delivers a quarter to a third of the platform's
headline W1 lever, with no software purchase.**

### E.3 What it destroys, and this is not a footnote

The corpus contains an unusually explicit warning against naive centralisation:

- **`CN-48`: "Coverage recovery runs on relationships. Visits get covered because a scheduler has built
  enough goodwill to ask a favour on a Friday afternoon."** The register calls this *"a real asset, not
  just a gap — and a substantial part of the argument for retaining a local human role."*
- **`DE-10` already decided this**: preserve a human scheduling role at reduced scale, *"for urgency,
  local knowledge, and relationship-based coverage."*
- **Local knowledge is load-bearing and geographic**: the Jacksonville bridge (one zip, two
  non-interchangeable sides) and the California interstate crossing window. A hub scheduler 800 miles
  away does not know the bridge exists.
- **`CN-37` regional safety scripts** vary by region and are corrective-action commitments, not
  preferences.
- **`CN-42`**: tenured clinicians resist territory flexibility *because they have been burned by
  inefficient coverage before.* Centralisation without visibility recreates exactly that experience and
  hardens the resistance the platform will later need to overcome.

**The synthesis the corpus supports** is not "centralise" or "keep local" but **centralise the
transactional, keep the relational**: hub-based auth chasing, task processing, SOC and recert assignment
and readiness calls; branch-based exception recovery, call-out coverage and clinician relationship.

### E.4 Cost, time to value, risk

| Line | Estimate |
|---|---:|
| Design, site selection, SOP build | $250k–$400k one-off |
| Severance, retention and parallel running during transition | $1.5M–$3.0M one-off *(the dominant cost, and the one usually under-budgeted)* |
| Telephony, queueing and workforce-management tooling for the hubs | $150k–$400k one-off, $100k–$200k/yr |
| Hub management layer (5–6 supervisors, 1 director) | $700k–$900k/yr *(partly offset by branch supervision released)* |
| **Year 1** | **$2.5M–$4.5M** |
| **Recurring net** | roughly neutral to favourable once headcount falls |

- **Time to value: 12–24 months.** Slower than A, B or C. Faster than a full platform implementation.
- **Risks.** Attrition during transition is the big one — schedulers are the institutional memory of the
  branch, and a badly run consolidation loses the good ones first. Service degrades before it improves,
  in a business where *"patients evaluate the agency almost entirely through scheduling reliability."*
  And it is irreversible in practice.

### E.5 Verdict

**A serious competitor on the W1 lever, and the prerequisite that makes Option D viable.** But it is the
highest-risk alternative here, it consumes the same change-management budget the platform will need, and
the corpus already warns that the thing it destroys — relationship-based coverage — is the thing that
currently makes the good branches good. **Recommend the hybrid: centralise the transactional half, and
do it after Options A, B and C have made the work smaller, not before.**

---

## 7. Option F — Hire differently

The cheapest, most reversible, most under-considered option on the list. It attacks the bottleneck the
corpus itself ranks first.

### F.1 More authorisation staff

**Authorisation is bottleneck #1 in the organisation's own ranking**, described as *"the largest
structural consumer, and most of it is self-inflicted — which makes it unusually tractable."* And it is
a **hard stop upstream of the scheduler's queue**: *"We know we have the referral, but it's just not in
my workflow to schedule yet because it's stuck in auth."*

The critical observation: **a scheduling platform does not clear an authorisation queue.** It can make
the queue visible. It cannot verify eligibility, key a pending auth, or argue with a payer. If the auth
team is the constraint, adding auth capacity is the direct intervention and adding scheduling software
is an indirect one.

| Line | Estimate |
|---|---:|
| 10–15 additional authorisation specialists, fully loaded | **$650k–$1.0M/yr** *(at $60k–$70k loaded, consistent with the register's scheduler assumption)* |

**What it buys.** Shorter front-door turnaround, therefore faster time to initial care, therefore fewer
referrals lost to slow starts (G3); fewer visits delivered against pending auth outside the backdating
window (**R1, the register's "most under-instrumented dollar in the whole initiative"**); and fewer
periods drifting below LUPA thresholds because visits were held (R2).

**The honest caveat, and it is decisive:** *nobody knows the current queue time.* The corpus says so
explicitly — nobody in the discovery session knew it, and no public source exists. **Adding auth
headcount without measuring the queue is buying capacity for a constraint you have not confirmed is
binding.** A four-week time study costs nothing and must precede this.

### F.2 A utilisation review nurse function

`CN-18` — if DCS order approval is turned off (Option B), the retained benefit is utilisation oversight,
*"better served by reviewing utilisation reports than by clicking through every order."* That review
needs an owner.

| Line | Estimate |
|---|---:|
| 4–6 regional UR nurses | **$450k–$700k/yr** |

**What it buys.** It is the control that *makes Option B safe.* It also owns the LUPA report (`CN-34`),
converting a discretionary daily task nobody reliably performs into a role with accountability, and it
owns front-loading policy adherence (C-4). **This is not a standalone benefit case; it is the mitigation
line for Options B and C and should be budgeted as such.**

### F.3 A capacity analyst function

**This is the option that competes most directly with the platform, and the corpus hands it the
argument.**

`DE-03`: **"Capacity is Phase 1, and Phase 1 is visualization only — no automation in the first
release."** And from the workbook: *"The MVP does not build the schedule… The first job of this product
is not to optimise anything. It is to make capacity measurable and observable."*

**A visualisation-only Phase 1 is substitutable by analysts.** `CN-28` says capacity information exists
today — committed load, productivity and LUPA exposure all live in HCHB reports, one of them roughly 20
columns wide, that someone must run and recombine by hand. That is a data-engineering problem, not a
product problem.

| Line | Estimate |
|---|---:|
| 6–8 regional capacity analysts | **$700k–$950k/yr** |
| 1 analytics lead plus BI tooling | **$200k–$280k/yr** |

**What it buys.** A weekly forward capacity view per branch; a standardised open-slot definition; a
cross-branch comparison that closes the variance the corpus calls extreme and unmanaged; and — most
valuably — **the baseline that does not exist today.** From `business-case-and-kpis.md`: of the five
primary KPIs, two do not exist as a live number at all and two are only partial. *"Capturing the
baseline is itself part of the work."*

**And here is the sharpest point in this document:** the platform cannot prove its own ROI without a
baseline, and the baseline is produced by analysts, not by the platform. **The analyst function is
therefore not an alternative to the platform — it is an unavoidable precondition of buying one.** It
should be hired whether or not the platform is bought, and its cost should move *out* of the platform's
benefit case and *into* its cost case.

### F.4 Cost, capture, time to value, risk

| | |
|---|---|
| **Total cost** | **$1.8M–$2.65M/yr** for all three (auth, UR, capacity analytics) |
| **Realistic capture** | R1 and R2 partial; the whole of the `DE-03` Phase-1 visualisation objective; the baseline; the control layer for Options B and C. **Indicative $1.5M–$3.0M/yr**, most of it revenue protection rather than removable cost. |
| **Time to value** | **90–180 days.** Recruitment is the only lead time. |
| **Risk** | **Low and reversible** — the defining property of this option. Headcount can be unwound; a signed multi-year platform contract cannot. The real risk is the opposite one: hiring becomes permanent and the analyst team institutionalises the manual process the platform was meant to remove. **Sunset criteria must be written at the point of hire.** |

### F.5 Verdict

**Auth headcount is the most direct attack on the number-one bottleneck and must be preceded by a
queue-time study. The capacity analyst function is not optional under any scenario.** Hire it now,
charge it to the platform's cost line, and stop counting Phase-1 visualisation as a platform benefit.

---

## 8. Option G — Build rather than buy

### G.1 What is buildable, and what is not

The workbook already ran and retired the naive version of this — the "daily fresh sheet plus an LLM"
proposal — and its reasoning is correct and should be preserved:

| The daily-sheet approach assumes… | …why it breaks |
|---|---|
| A fresh sheet each morning is fine | **It has amnesia.** No history means it cannot trend, forecast, or prove ROI |
| The AI can just optimise it | The real constraints — licensure, authorisations, LUPA thresholds, drive time, caregiver availability — are not in the sheet |
| It produces the schedule, which is the goal | **The value is not the schedule, it is the measurement** |
| An LLM reshuffling the day is low-risk | Scheduling clinical visits is a **high-harm** process — no constraint enforcement, no audit trail |
| One clever person in Excel can run it | Does not scale, does not survive turnover, creates no shared source of truth |

**All five objections apply to building a scheduling *engine*. None of them apply to building a capacity
*measurement* layer.** That distinction is the whole of Option G.

### G.2 The buildable scope

| Build | Feasibility | Why |
|---|---|---|
| **Capacity dashboard** — committed load, productivity, LUPA exposure, open slots, forward referral pipeline, by branch and territory | **High.** ETL plus BI over the HCHB data warehouse and Commure. | It is `DE-03` Phase 1 in full. `CN-28` says the data exists and only the recombination is manual. |
| **Auth-notification filter** (`CN-23` / W2) | **Medium-high.** Diff the auth state daily; raise a task only on a genuine change. | The product limit is that HCHB *notifies on state persistence.* A layer that reads the auth state and emits only state-change alerts is small, well-bounded software. **This converts a "product limit" into a solved problem for roughly $150k.** |
| **Pending-auth visibility** (`CN-22`) | **Medium.** Surface pending visits as committed load in the dashboard. | It cannot put them on the clinician's HCHB calendar — that is HCHB's calendar. But *"if you can't see it, you can't plan"* is a leadership-visibility problem, and leadership visibility is buildable. |
| **Payer rules library** | **Medium.** Structured store fed by the auth team's existing template snippet (`CN-33`). | The register calls this *"contract-level data that nobody publishes… an onboarding cost and a durable moat."* A moat you build is still a moat. |
| **Cross-branch variance reporting** | **High.** | Directly attacks the extreme-and-unmanaged variance. |
| **Territory and census heat mapping by zip and discipline** | **High.** | Named as a high-leverage change; today it is hand-coloured maps and zip spreadsheets nobody re-cuts. |
| **A scheduling or assignment engine** | **Do not build.** | High-harm, constraint enforcement, audit trail — and HCHB's `CN-20` dispatching already implements recommend-then-approve. Building here duplicates the incumbent badly. |
| **Route optimisation** (W6) | **Do not build.** | Commodity capability; buy it as a component if wanted. |
| **Patient engagement and confirmation** (W7) | **Do not build.** | Separable point solution, and it carries the TCPA, California-robocall and Washington safety-script constraints that make it a legal project as much as a technical one. |

### G.3 Cost

| Line | Estimate |
|---|---:|
| Team: 1 product, 1 data architect, 3 data/analytics engineers, 1 BI developer, 0.5 QA | **$1.4M–$1.9M/yr** fully loaded |
| Cloud, warehouse and BI licensing | **$150k–$350k/yr** |
| HCHB data-warehouse and API access, plus any integration fees | **unknown — must be obtained from HCHB.** *Named as an information gap.* |
| **Year 1** | **$1.6M–$2.3M** |
| **Steady state** | **$1.2M–$1.8M/yr** (smaller team once built, but never zero) |

### G.4 Capture, time to value, risk

- **Capture:** the whole of Phase 1 (`DE-03`); W2 in full via the filter; the visibility that enables
  W3/W4; the baseline for every KPI. **Indicative $2.0M–$3.5M/yr** — and it removes the "capacity
  visualisation" justification from the platform entirely.
- **Time to value: 6–9 months** to a usable capacity dashboard; **3–4 months for the auth filter alone**,
  which is the fastest high-value item in this entire document.
- **Risks.** (1) **You own it forever** — no vendor roadmap, no other customer funding R&D, and the cost
  never reaches zero. (2) HCHB data-warehouse latency and the Citrix sync lag (`CN-27`) mean visit state
  is unreliable as a real-time input *regardless of who builds on top of it* — a constraint the platform
  vendor also inherits and should be asked about directly, in writing. (3) Build teams in provider
  organisations are hard to retain. (4) Scope creep from "dashboard" to "engine" is the classic failure
  mode and must be governed with a written prohibition.

### G.5 Verdict

**Build the measurement layer and the auth filter. Do not build the engine.** The auth-notification
filter in particular deserves funding immediately: it converts the most-cited scheduler frustration in
the business from a product limit into a solved problem, for a fraction of one year's platform licence,
and it does not depend on any vendor decision.

---

## 9. Option H — Do nothing

"Do nothing" is the option every business case is implicitly written against, and it is almost always
mis-stated as "things stay as they are." They do not. The honest question is whether the status quo is
**stable** or **deteriorating**, and in this business the evidence is that it is deteriorating on four
independent fronts at once.

### H.1 Reimbursement is falling in real terms

CMS finalised the CY2026 Home Health PPS rule with an **aggregate 1.3% reduction — about $220M
nationally** — built from a 2.4% payment update, offset by a 0.9% permanent behavioural adjustment, a
2.7% one-year temporary adjustment, and a 0.1% FDL change. The permanent adjustment was finalised at
1.023%, well below the 4.059% proposed, but **the temporary adjustment is a live instrument CMS has now
demonstrated it will use.**

- On the initiative's own anchors, a 1.3% aggregate reduction against ~$260M of in-scope episodic
  revenue is **roughly $3.4M/yr of run-rate erosion, recurring.**
- The register's own utilisation evidence compounds it: industry visits per period fell from 10.2 to 8.4
  between 2019 and 2024 — an 18% reduction — **while discharge-to-community got worse.** The easy
  utilisation savings have already been taken across the industry. There is no further volume cut
  available that is not a quality cut.

> **Do nothing, and the margin compresses by roughly the size of the entire discipline/role-match lever
> (U1, $1.9M) every single year, with no offsetting action.**

Sources: [CMS Finalizes 2026 Home Health Medicare Payment Rule With 1.3% Aggregate Reduction — Home
Health Care News](https://homehealthcarenews.com/2025/11/cms-finalizes-2026-home-health-medicare-payment-rule-with-1-3-aggregate-reduction/) ·
[CY 2026 Home Health Rule Finalizes Smaller Permanent Adjustment and Sets One-Year Temporary 3.0% Rate
Reduction — Applied Policy](https://www.appliedpolicy.com/cy-2026-home-health-rule-finalizes-smaller-permanent-adjustment-and-sets-one-year-temporary-3-0-rate-reduction/) ·
[2026 Home Health Final Rule: 1.3% Cut — Forvis Mazars](https://www.forvismazars.us/forsights/2025/12/2026-home-health-final-rule-1-3-cut) ·
[Home Health Payment Rule CY 2026 — LeadingAge](https://leadingage.org/serialpost/home-health-payment-rule-calendar-year-2026/)

### H.2 Growth cannot be bought, only earned through throughput

`G2` in the register: **CMS imposed a national six-month moratorium on new home health and hospice
Medicare enrolment in May 2026**, including certain ownership changes. While it holds, growth cannot be
purchased with new locations.

This inverts the usual reading of "do nothing." Normally the status quo forgoes an efficiency gain.
Here, **the status quo forgoes the only available growth channel**, because the corpus is explicit that
SOC-capable clinician availability is the binding constraint and that the overload cycle *"locks a branch
at its current volume indefinitely."* A 2% admissions lift on $549M is $11M of revenue at
above-average contribution margin. Doing nothing does not defer that; under the moratorium it forfeits
it.

### H.3 The workforce cost is rising and the mechanism is scheduling

Published turnover evidence for the sector is severe and the direction is wrong:

| Figure | Value | Source |
|---|---|---|
| Home health industry turnover (all roles) | **79%**, up 12 points since 2022 | [Silent Beacon summary of industry data](https://silentbeacon.com/home-health-worker-turnover-safety) |
| Home health **nurse** turnover | **23.9% in 2025**, down from 26.6% | [The Resource Company, Healthcare Turnover Rate 2026](https://www.theresource.com/2025/11/19/healthcare-turnover-rate/) |
| Homecare nurse turnover range | **25–31%** | [Zagrodney et al., *The Cost of Turnover in Home Healthcare*, 2026](https://journals.sagepub.com/doi/10.1177/08404704251412842) |
| Cost to replace an RN (healthcare average) | **>$61,000** | NSI Nursing Solutions 2025, via [Becker's](https://www.beckershospitalreview.com/workforce/the-cost-of-nurse-turnover-in-10-points-2026/) |
| Cost to replace a PT including opportunity cost | **~$70,000** | [Nestmed, "Ending Pajama Time"](https://www.nestmed.com/resources/ending-pajama-time) |

The corpus's own workbook uses **5 clinician departures per branch per year at $40,000 replacement**,
i.e. **$16M/yr of gross turnover cost across 80 branches** — and both of its component assumptions are
*conservative* against the published figures above. The mechanism is named repeatedly in the discovery
material: overload with no fallback, excessive reassignment travel, repeated calls to the branch, and
**~30 minutes a day of unpaid evening confirmation work per clinician** (`W7`) — the "pajama time"
the published literature now names directly as a home health turnover driver.

> **Do nothing, and the single largest cost in the business — clinician replacement — stays on a
> trajectory driven by a cause the initiative has already diagnosed.**

### H.4 The status quo is actively destroying latent capacity

Three findings in the corpus describe deterioration that is already in progress, not risk that might
arrive:

- **`CN-41`** — clinicians **have stopped calling in** for backup visits, because they do not trust the
  branch to respond efficiently. They absorb the gap and take one less patient. *Capacity is being
  silently withdrawn from the system by the people who supply it, and the withdrawal is cumulative.*
- **`CN-39` / `CN-23`** — schedulers have been trained by daily notification noise to bulk-clear without
  reading. The behaviour is rational and getting more entrenched; the actionable item goes with the
  noise.
- **`CN-47`** — branches that decline to use per-diem staff *"forfeit the ability to grow"*, and nothing
  in the status quo corrects that policy divergence.

### H.5 The three-year cost of doing nothing

| Component | Year 1 | Three-year cumulative | Basis |
|---|---:|---:|---|
| Reimbursement erosion on episodic revenue | ~$3.4M | **~$10M+** | CY2026 rule at −1.3%; assumes no further cut, which is optimistic |
| Growth forgone under the moratorium (2% admissions lift, at contribution margin) | ~$2.2M | **~$6.6M+** | $11M revenue × ~20% blended margin, understated because branch infrastructure is already paid for |
| Turnover attributable to scheduling quality (10% of the $16M workbook figure) | ~$1.6M | **~$4.8M** | Workbook's own driver, conservative against published replacement costs |
| Levers already identified and not taken (U1 $1.9M + R2 $2.2M, at 50% realisation) | ~$2.0M | **~$6.0M** | Register's own sizing |
| **Total, order of magnitude** | **~$9M/yr** | **~$27M over three years** | **Illustrative. Every line requires a Compassus input from register §9.** |

Plus one item that cannot be priced and should be named rather than valued: **the electronic prior
authorisation requirement effective 1 January 2027.** Doing nothing means arriving at that date with
authorisation state still held in coordination notes and in schedulers' heads.

### H.6 Verdict

**"Do nothing" is not a low-cost option; it is a roughly $9M/yr option, and it deteriorates.** But that
finding does *not* transfer automatically to the platform. Options A, B, C, F and G capture a
substantial share of the same $9M at a fraction of the platform's cost. **The cost of the status quo is
an argument for acting. It is not, on its own, an argument for buying.**

---

## 10. Comparison of all options

All figures illustrative. Costs are fully loaded. "Capture" is the share of the register's total claimed
annual benefit (waterfall levers only, excluding the upside panel) that the option plausibly reaches.

| # | Option | Year-1 cost | Recurring cost | Indicative annual benefit | Capture of claimed benefit | Time to value | Reversible? | Risk |
|---|---|---:|---:|---:|---:|---|---|---|
| **A** | **Turn on what is owned** — Workday↔HCHB PTO, Shift Finder, visit dispatching, rapid-reschedule flag | $0.75M–$1.3M | $0.2M–$0.4M + unknown HCHB licence | **$1.5M–$3.0M** | **10–20%** | **3–6 months** | Yes | **Low** — worst case you learn the adoption assumption is false, which you needed to know anyway |
| **B** | **Delete workflow** — DCS order approval off; LUPA report enforced; huddle shortened (platform-gated) | $0.2M | $0.15M | **$0.5M–$1.5M** | **5–10%** | 3–6 months | Yes | **Medium** — clinical-governance decision, not an investment decision. Two of the three headline deletions are HCHB product limits and are *not* available |
| **C** | **Process and policy, no technology** — payer rules card, readiness-call standard work, call-out protocol, front-loading, PTA/LPN default | $0.5M–$0.75M | $0.25M–$0.35M | **$1.4M–$2.5M** | **15–25%** | 2 months to start, 6–12 to land | Yes | **Medium** — the risk is decay, and decay is exactly what a platform prevents |
| **D** | **Outsource / offshore** the transactional scheduler workload | $1.5M–$3.0M transition | contract + $0.6M–$1.0M retained management | **$2.5M–$4.5M net** | **25–35%** | 9–15 months | **No** | **High** — entrenches the workflow, destroys `CN-48` relationship capital, payer and JV contracts may carve out half the book |
| **E** | **Centralise** into 4–6 regional hubs | $2.5M–$4.5M | ~neutral once headcount falls | **$2.7M–$4.5M** | **20–30%** | 12–24 months | **No** | **High** — attrition during transition, service degrades before it improves, destroys local knowledge |
| **F** | **Hire differently** — auth specialists, UR nurses, capacity analysts | recruitment only | $1.8M–$2.65M | **$1.5M–$3.0M** | **15–25%**, mostly revenue protection | **3–6 months** | **Yes — fully** | **Low** — the only fully reversible large option. Risk is institutionalising the manual process |
| **G** | **Build** the measurement layer + auth-notification filter (not the engine) | $1.6M–$2.3M | $1.2M–$1.8M | **$2.0M–$3.5M** | **20–30%** | 3–4 months (filter), 6–9 (dashboard) | Partly | **Medium** — you own it forever; scope creep to "engine" is the classic failure |
| **H** | **Do nothing** | $0 | $0 | **−$9M/yr, deteriorating** | — | — | — | **Highest** — reimbursement erosion, forgone growth under the enrolment moratorium, turnover, silent capacity withdrawal |
| **P** | **The platform** (for comparison) | implementation **$2M–$5M** *(estimate; enterprise healthcare implementations commonly run 1–2× year-1 licence)* + internal programme $1.5M–$2.5M/yr | licence **$1.5M–$3.5M/yr** *(estimate — no vendor quote in the corpus)* | workbook's Moderate case **$7.9M/yr** at full product, **$4.7M at MVP** | 100% by construction | **18–36 months** to full value | **No** | **High** — `CN-43` adoption failure is documented, not hypothetical; the Alabama precedent is in the record |

### The overlap warning

**These options are not additive.** A, D, E and G all attack W1. F and G both deliver `DE-03` Phase 1 —
one manually, one systematically. C and the platform both attack U1. Summing the "benefit" column
produces a number that cannot be earned. Every combination must net the overlaps before it goes to
finance, and the register's own §11 anti-double-counting discipline applies with equal force here.

---

## 11. The best alternative — the Operating Discipline Stack

The strongest alternative is not a single option. It is a deliberately sequenced combination of the
cheap, fast and reversible ones, and it is strong enough that **it should be run whether or not the
platform is bought.**

### 11.1 What it contains

| Phase | Contents | Window |
|---|---|---|
| **Phase 0 — measure (weeks 1–8)** | Scheduler time study. Auth queue-time study. Count of visits written off for authorisation (**R1**). Actual LUPA rate and periods-one-visit-short. Missed and rebooked visit rates. Pay-model split across the estate. Payer and JV contract clause review for offshore restrictions. **All of these are register §9 inputs, all are free, and none of them require a vendor.** | 8 weeks |
| **Phase 1 — configure and delete (months 1–6)** | **Option A** in full: Workday↔HCHB PTO interface, Shift Finder, visit dispatching, rapid-reschedule flag standardised across all branches. **Option B**: the DCS order-approval decision taken and executed with a UR control behind it. | 6 months |
| **Phase 2 — standard work (months 2–12)** | **Option C** in full: payer rules card at POC creation, readiness-call standard work with a completion gate, published call-out recovery protocol with a response-time commitment, front-loading policy, PTA/LPN default with explicit opt-out and a market-by-market supply check. | 12 months |
| **Phase 3 — staff the constraint (months 3–9)** | **Option F**: auth specialists sized to the measured queue, 4–6 UR nurses as the Option-B control, a lean capacity analyst function with **written sunset criteria**. | 9 months |
| **Phase 4 — build the two things worth building (months 3–12)** | **Option G, narrow scope only**: the auth-notification state-change filter (`CN-23` / W2) and the capacity measurement layer (`DE-03` Phase 1). **Written prohibition on building an engine.** | 12 months |

Deliberately excluded: **Option D and Option E.** Both are large, irreversible, consume the same change
budget the platform needs, and — critically — both get *cheaper and safer* after Phases 1–4 have made
the work smaller and written the payer rules down. They are year-2 decisions, not year-1 decisions.

### 11.2 What it costs and returns

| | Year 1 | Recurring |
|---|---:|---:|
| Cost | **$4.7M–$6.8M** | **$3.5M–$4.7M/yr** |
| Benefit, after netting overlaps (≈35% haircut on the raw sum) | **$4.5M–$8.5M**, midpoint ~**$6.0M** | same |
| **Net** | roughly break-even in year 1 | **~$1.5M–$2.5M/yr**, ROI ~40–60% |

Plus three things that do not appear as a dollar and are worth more than the dollars:

1. **The baseline.** Two of five primary KPIs do not exist as a live number today. After Phase 0 they do.
   **Nothing can be proven — by any option, including the platform — until they do.**
2. **A tested adoption assumption.** Shift Finder and visit dispatching answer, for ~1–3% of the
   platform's lifetime cost, whether clinicians will accept machine-recommended work. That question sank
   Alabama and it is the platform's single largest risk.
3. **A smaller problem.** Every subsequent option — platform, BPO or hub — is sized against a process
   that has already had its configurable waste, its deletable workflow and its policy leakage removed.

### 11.3 Why this is the benchmark

- It is **the fastest**: material value inside 6 months against the platform's 18–36.
- It is **the most reversible**: nothing in it is a multi-year contract.
- It **cannot be skipped**: Phase 0 is a precondition of the platform's own business case, and Phases 1–2
  are preconditions of the platform working (an unconfigured HCHB and an unwritten payer rules library
  do not get better because a new system arrives).
- It is **already the organisation's own conclusion**, expressed across `DE-03`, `DE-08`, `CN-18`,
  `CN-19`, `CN-20`, `CN-31`, `CN-33`, `CN-34` and W5. This document has not invented an alternative; it
  has collected one that the corpus already contains.

---

## 12. What the platform must deliver to beat the best alternative

### 12.1 The hurdle, stated as arithmetic

The platform's own workbook puts the Moderate case at **$7.9M/yr** at full product and **$4.7M/yr** at
MVP, against ~80 branches. Estimated platform TCO is **$3.5M–$6M/yr** across licence, amortised
implementation and internal programme.

**But the platform is not entitled to the whole $7.9M, because the Operating Discipline Stack will have
already taken $4.5M–$8.5M of the same ground.** Charging the platform only with what it adds:

| | |
|---:|---|
| Workbook Moderate case, full product | **$7.9M/yr** |
| Less: benefit already captured by the Stack (midpoint, after netting) | **−$6.0M/yr** |
| **Incremental benefit attributable to the platform** | **~$1.9M/yr** |
| Platform TCO | **$3.5M–$6.0M/yr** |
| **Incremental net** | **negative** |

> **This is the finding the steering committee has to confront. On the initiative's own Moderate case,
> and with the alternatives credited honestly, the platform does not clear the hurdle.**

Three ways out, and only three:

1. **The Moderate case is understated** because it was built before the register's larger levers (W1 at
   $12M, R1 unsized, G1 at $11M on a 2% lift) were assembled. **Note that the workbook's $7.9M and the
   register's W1 alone at $12M are inconsistent, and that inconsistency must be resolved before either
   number is presented.**
2. **The platform reaches levers the Stack demonstrably cannot** — the list in 12.2 below.
3. **The Stack under-delivers**, most likely through decay (Option C) or through the adoption failure
   that Option A is designed to test early and cheaply.

**The correct decision sequence follows directly: run Phase 0 and Phase 1 first, then re-price the
platform against the residual.** Buying before that is buying without knowing the size of what is left.

### 12.2 The seven specific things the platform must deliver

Each of these is something **no alternative in this document reaches.** They are the platform's entire
incremental case, and each should be written into the RFP as a scripted acceptance demonstration.

**1. Close the nine HCHB product limits — `CN-22` through `CN-30`.**
This is the substantive case for the initiative and the constraint register says so in terms: *"None of
those can be toggled."* Specifically the platform must demonstrate:
- **`CN-22`** pending-auth visits **visible, attributable, and counted as committed load** even while
  unassignable. *"If you can't see it, you can't plan."*
- **`CN-23`** notification **on state change, never on state persistence** *(note: Option G reaches this
  one for ~$150k — the platform must be cheaper than that on a marginal basis or it is not the reason to
  buy)*.
- **`CN-24`** a clinician handing a visit to **her own LPN** without a scheduler round trip — the
  register calls removing this *"the highest-yield single change in the routine-visit flow."*
- **`CN-25`** supervisors seeing supervisee schedules.
- **`CN-26`** care-team-at-referral collapsing the per-discipline task explosion (`DE-05`).
- **`CN-27`** a **reliable real-time visit state** despite the Citrix sync lag — *this one must be
  interrogated hard, because the vendor inherits the same lag and may not be able to solve it.*
- **`CN-28`** live capacity, not manually recombined reports.
- **`CN-29`** a visibility horizon beyond seven days.
- **`CN-30`** structured routing replacing coordination-notes-as-workflow.

**Any of the nine the platform cannot demonstrate must be struck from its benefit case on the spot.**

**2. A forward capacity forecast, not a current-state view.**
The Stack produces a *current* capacity picture. It does not answer **"can this branch absorb this
referral three weeks from now"** — the question `CP-3` calls the highest-value connection point in the
system and the one that governs whether the branch grows. A forecast needs referral pipeline, pending
auth weighted by payer approval rate and turnaround, planned discharges, ramp status and PTO in one
model. **No analyst team assembles that weekly at national scale. This is the platform's strongest
genuine claim and it should lead the case.**

**3. Policy converted from document into enforced default.**
Option C's fatal weakness is decay, and the register already legislates against saving that depends on a
manager remembering. The platform must show:
- **Payer rules as a checked constraint at plan-of-care creation** — not a card, not a coordination
  note, a constraint (`CN-33`, and the register's *"highest-value, lowest-complexity win"*).
- **`DE-08` discipline-role match as a system default with explicit opt-out** and a captured reason —
  HCHB filters the assignable list but *does not push work down*.
- **`CN-34` LUPA exposure as an event-driven alert at the moment a visit is missed**, with remaining days
  shown — not a discretionary daily report.

**4. Recommendation quality that beats HCHB's own dispatching, proven head to head.**
`CN-20` says HCHB already implements recommend-then-approve and deliberately does not auto-assign. *"The
gap is quality of recommendation, not the interaction model."* **The platform must be benchmarked
against enabled HCHB visit dispatching on the same visits, and win.** If it cannot beat a module
Compassus can switch on, there is no case. This is the single most important line in any RFP that comes
out of this initiative.

**5. Survival of `CN-43`.**
*"A scheduler could have assigned that exact same thing to them, but the tool did it, and they're like,
well, it must be broken."* The platform must satisfy `DE-09` — clinicians supply their own availability
and preferences, the tool recommends, the human accepts — **and must show the pilot design that proves
it**, on a new-integration or new-branch site with newer clinicians, per the discovery record. **A
vendor whose product overreaches this posture is disqualified regardless of score.** The workbook already
scores HCHB Smart Scheduling as overreaching on 16 variables and correctly reads that as *"the Alabama
failure mode expressed as a number."* Apply the same test to every vendor.

**6. National comparability, and the closing of branch variance.**
Branch-to-branch variability is *"extreme and unmanaged"*, high performers recover coverage in minutes
and low performers in hours, and there is **no mechanism to close the gap.** A hub (Option E) closes it
by removing the branches; a platform closes it by making every branch measurable on the same terms while
keeping the local relationship `CN-48` depends on. **That is the platform's answer to Option E, and it is
a good one — but it must be a demonstrated capability, not a dashboard screenshot.**

**7. The durable data asset, and 1 January 2027.**
The register's option-value argument stands and is genuinely unavailable elsewhere: an instrumented
platform would hold **the first real dataset on home health authorisation turnaround and denial
behaviour**, which does not exist anywhere today and which federal oversight has asked CMS to begin
collecting. And the **electronic prior authorisation requirement effective 1 January 2027 lands inside
this initiative's scale phase** — authorisation state must be a measured input, not a hard-coded
assumption, by then.

### 12.3 What the platform must stop claiming

To be credible against the alternatives, the business case must **remove** the following from the
platform's benefit column:

| Remove | Because |
|---|---|
| **W5 PTO collision avoidance** | The interface already exists and is switched off. This is Option A's benefit, not the platform's. |
| **`DE-03` Phase-1 capacity visualisation** | Substitutable by analysts (Option F) or a BI build (Option G) at a fraction of the cost. Charge it to the alternative, and charge the analyst team to the platform's *cost* line as the precondition it is. |
| **The full $1.9M of U1** | The policy default captures 40–60% of it manually. The platform earns only the non-decaying remainder plus the durability. |
| **The 45 minutes of daily huddle time** | Real, but it is a *platform-gated deletion* — legitimately the platform's, and it should be moved from Option B into the platform's own case. |
| **Q1 value-based performance** | Not attributable to any option without the baseline, and the baseline is Phase 0's, not the platform's. |

### 12.4 The one-sentence test

> **The platform earns its premium if, and only if, it can (a) demonstrate closure of `CN-22`–`CN-30`,
> (b) produce a forward capacity forecast the branch acts on, (c) beat enabled HCHB visit dispatching
> head to head, and (d) hold `DE-09` posture under clinician pressure — priced against the residual
> benefit that remains after Options A, B, C, F and G have been run, not against the gross.**

---

## 13. Information gaps that would change these conclusions

Stated in the register's own discipline: named, not guessed.

| Gap | Which conclusion it moves |
|---|---|
| **Actual HCHB pricing** — Smart Scheduling module licence, data-warehouse and API access fees, professional-services rates | Options A and G. If Smart Scheduling carries a large per-user fee, Option A's ROI falls; if data-warehouse access is restricted or expensive, Option G becomes much harder. **HCHB publishes nothing; this must come from the account team.** |
| **Actual platform pricing** — no vendor quote appears anywhere in the corpus | Section 12.1 is arithmetic against an estimate. The hurdle calculation cannot be finalised without it. |
| **Scheduler time study** — where the 300 FTE actually go, by task | Every W1 estimate in this document, and the entire scoping of Options D and E |
| **Auth queue time** | Whether Option F's auth hiring is the right intervention at all |
| **Loaded cost of a scheduler, and the pay-model split across the estate** | Register §9 already names the pay-model split as the highest-value single input, because **the sign of several margin levers changes with it** |
| **Payer and JV contract offshore-restriction review** | Whether Option D is a $5M option or a $2M option |
| **Paraprofessional supply by market** | Whether C-5 / U1 can be switched on at all in a given market |
| **Quoted BPO rate cards** | The Option D range in this document is an indicative market estimate, not a quote |

---

## 14. Recommendation

1. **Run Phase 0 now.** Eight weeks, no capital, and it is a precondition of every other decision
   including the platform's own business case.
2. **Execute Options A, B, C, F and the narrow build in G, in parallel, starting immediately.** They are
   cheap, fast, mostly reversible, and the organisation has already reached these conclusions itself.
3. **Do not sign a platform contract before Shift Finder and HCHB visit dispatching have been enabled
   and measured.** That test costs 1–3% of the platform's lifetime cost and de-risks or invalidates its
   largest assumption.
4. **Re-price the platform against the residual**, using the section 12.2 acceptance tests as the RFP.
5. **Hold Options D and E as year-2 decisions.** Both get cheaper, safer and better-scoped after the work
   has been made smaller and the payer rules have been written down.
6. **Resolve the $7.9M / $12M inconsistency between the workbook and the register before either number
   is shown to a steering committee.**

---

## 15. Sources and method

**Internal (primary, and treated as ground truth):**
`compassus-capacity-pm/agents/compassus-capacity-pm/knowledge/` — `discovery-session.md`,
`whiteboard-session-2026-08-13.md`, `process-facts-2026-08.md`, `capacity-scheduling-summary.md`,
`constraint-register.md` (CN-01 … CN-51), `bottleneck-dossiers.md`, `business-case-and-kpis.md`,
`business-case-format-2026-08.md`; and `.../artifacts/business-case-register.md`,
`payer-types-and-episode-economics.md`, `authorization-and-capacity-forecasting.md`.

**External, cited inline:** CMS CY2026 Home Health PPS final rule coverage (Home Health Care News,
Applied Policy, Forvis Mazars, LeadingAge, CHAP); home health and healthcare turnover data (NSI Nursing
Solutions 2025 via Becker's, The Resource Company 2026, Zagrodney et al. 2026 in *Healthcare Management
Forum*, Nestmed, Silent Beacon).

**Marked estimates, not sourced quotes.** The following figures in this document are indicative market
ranges drawn from general industry experience and are explicitly *not* vendor quotes or published
prices. Each must be replaced before it reaches finance:

- HCHB module licensing, data-warehouse access and professional-services rates. **HCHB publishes no
  pricing.** Obtain from the account team.
- Platform licence and implementation cost. **No vendor quote exists anywhere in the corpus.** Section
  12.1's hurdle arithmetic is therefore directional until quotes are in hand.
- Healthcare BPO rate cards (onshore, nearshore, offshore) and offshore attrition rates in Option D.
- The 15–25% consolidation productivity range in Option E.
- All internal team costs (analysts, engineers, UR nurses, auth specialists), which use the register's
  own $60k loaded-cost convention and should be replaced with Compassus actuals per register §9.

**Method note.** Where the corpus and an external source disagreed, the corpus won. Where neither had a
number, this document names what to measure rather than inventing one — the same discipline the
bottleneck dossiers apply, and for the same reason: *inventing figures would undermine the business case
rather than support it.*
