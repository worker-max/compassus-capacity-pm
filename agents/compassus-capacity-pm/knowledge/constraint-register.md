# Constraint Register — CN-01 … CN-51

> **Source:** `8.17.26 Constraint Register.docx` — Google Drive `12kNpfOEem62UwZWI6xU0E-bsGA79PngB`,
> folder `1RPI1ogTdyDeEf64OBRmaRQ0ESNWp5k5o`. Rendered faithfully; do not paraphrase away the specifics.
> `[T:###]` citations resolve against
> [`source/transcript-lines-2026-08-13.txt`](./source/transcript-lines-2026-08-13.txt).
>
> **What it is.** What blocks scheduling today, classified by whether we can change it. The organizing
> discipline of the whole initiative is separating what **Home Care Home Base imposes** from what
> **regulation actually requires** — several of the most painful constraints are product design
> choices, and a few things assumed to be product choices are in fact regulatory. Getting that
> boundary right determines what we design around, what we design out, and what we simply encode.
>
> Entries marked **(confirm)** are classifications inferred from the session rather than stated
> outright, and should be settled with Laci before the register is used to scope a vendor conversation.

## Classes

| Class | Meaning |
|---|---|
| **Regulatory** | Medicare, CMS or state requirement. Not changeable. Encode and comply. |
| **Payer** | Contractual behaviour of a specific payer. Not changeable. Encode and plan against. |
| **HCHB configurable** | Already within our control today; no new system required. |
| **HCHB product limit** | Requires a vendor change or a replacement system. **This class is the substantive case for the initiative.** |
| **Compassus policy** | Our own standard or practice. Changeable by us. |
| **Cultural and behavioural** | Changeable, but by leadership and change management, not software. |
| **Labor agreement** | Changeable only through negotiation. |

---

## Regulatory — not changeable

| ID | Constraint | Design implication |
|---|---|---|
| **CN-01** | **MD notification of a missed visit within 48 hours.** A Medicare requirement, enforced as an HCHB hard stop; if notification is not documented, workflow generates to the DCS. `[T:224]` | The tool should track and prompt the 48-hour clock rather than depend on the scheduler noticing. |
| **CN-02** | **OASIS visits are date-bound.** Unlike routine visits, they cannot be freely moved by the assigned clinician. | Any self-service visit-moving capability must distinguish OASIS from non-OASIS and refuse the former. |
| **CN-03** | **The certification period is 60 days from SOC.** A visit cannot be moved past it. | A hard boundary on any rescheduling or optimisation logic. |
| **CN-04** | **The Medicare week runs Sunday through Saturday.** Frequency is expressed and consumed against it. | The scheduling engine's week must be the Medicare week, not a calendar or business week. |
| **CN-05** | **LUPA thresholds.** Visit-count minimums below which the period is paid per-visit rather than as an episode. Not changeable; exposure is manageable. `[T:227-237]` | LUPA risk should be forward-looking and surfaced **at the moment a visit is missed**, with the remaining days shown — not delivered as a next-day report. |
| **CN-06** | **The plan of care requires a physician order and signature.** The clinician writes the frequency and creates the order the physician signs. `[T:158]` | **The clinician is the originator of frequency; no tool should generate frequency independently.** |
| **CN-07** | **Plan-of-care review before scheduling.** Laci's read is explicit — unlike order approval, this one cannot be turned off. SOC, recert and ROC plans must clear a review workflow before visits reach scheduling. `[T:81-83]` | The hard stop stays; the opportunity is throughput and queue visibility, not removal. **(confirm** whether the requirement is regulatory or an HCHB structural constraint**)** |
| **CN-08** | **Discipline scope of practice.** PTs can perform assessing visits, PTAs cannot; RN and LPN scopes differ. HCHB filters the assignable list accordingly. `[T:171-172]` | Scope filtering is a **correctness** requirement, not an optimisation preference. |
| **CN-09** | **Text and email contact requires signed consent.** Compassus holds separate text, email and share-with-family consents, none usable until signed **at the SOC visit**. `[T:533-536]` | Automated reminder flows cannot begin before the SOC, so the readiness call remains a voice call. Open question: can consent capture move earlier — into the hospital or the Commure intake flow? |
| **CN-10** | **Outbound automated calling is regulated.** California treats any call not manually triggered by a human as a robocall; batch-triggered calls fall under that treatment. `[T:537-541]` | Patient-engagement design depends on resolving this; open item with Colin. The session's read that a voice call is a voice call whether or not a human places it needs **legal** confirmation, not operational judgment. |
| **CN-11** | **An active POA must sign admission consents.** Where a POA exists the POA signs; the patient's own agreement is not sufficient. Some POAs require that the patient not be contacted at all. `[T:495-500]` | POA status has to be surfaced at the **front** of the scheduling view — discovering it at the door wastes an SOC visit. |

## Payer — not changeable, must be encoded

| ID | Constraint | Design implication |
|---|---|---|
| **CN-12** | **Pending-auth counts vary by payer** — some permit 1, some 3, some 5, some 10. This number caps how far ahead the scheduler can work. `[T:562, 569]` | The pending-auth allowance is a first-class field, and should be **derived from the payer** rather than keyed by a person. |
| **CN-13** | **Completion and documentation gates before additional auth.** UHC grants 5 nursing visits and requires 4 of the 5 completed, with documentation supporting continued need, before visit 6. `[T:443, 468]` | This is a **forward-looking scheduling constraint, not a billing one** — it determines what frequency is achievable. |
| **CN-14** | **Benefit windows may be keyed to the hospital discharge date.** Indiana Medicaid pays 30 days from discharge, not admit, so a five-day gap between discharge and SOC consumes five days of benefit. `[T:446]` | **The clock starts before we do.** Discharge date must be captured at referral and drive discharge planning from day one. |
| **CN-15** | **Therapy visit pools may be shared across disciplines.** Indiana Medicaid allows 8 visits total across PT, OT and ST combined. `[T:453-454]` | Allowances cannot be modelled per discipline; they need a **pool** concept. |
| **CN-16** | **Payers may mandate discipline substitution.** Some will not pay an SN visit and require an LPN visit. HCHB already enforces this at scheduling. `[T:174]` | Payer-driven discipline rules sit alongside scope-of-practice rules; both must filter assignment. |
| **CN-17** | **Pending auth is not universally payable.** Some payers will not retroactively pay against a pending auth; where they do not, a leader decides whether to see the patient as a non-billable visit. `[T:463-464]` | Show which payers permit pending auth, and **route the non-billable decision to the right approver** rather than leaving it with the scheduler. |

## HCHB configurable — within our control today

| ID | Constraint | Design implication |
|---|---|---|
| **CN-18** | **DCS approval on physician orders.** Every order routes to a DCS for approval. **An HCHB toggle, not a Medicare requirement**, and not done at other agencies. The largest single source of DCS workflow backlog, which delays visit addition. Options raised: turn it off outright; turn it off selectively for clinicians with a demonstrated record of writing good orders; or have AI adjudicate the black-and-white cases and escalate the gray ones. `[T:58, 61-63, 431-437]` | The retained benefit is utilisation oversight — better served by reviewing utilisation reports than by clicking through every order. **Decided by: a company-level risk decision**, carried in the open decisions document. |
| **CN-19** | **Shift Finder is not enabled.** HCHB already offers clinicians a view of uncovered visits with a patient snapshot and distance, and the ability to accept one, generating a back-office approval task. `[T:346-347]` | A self-service open-visit capability **need not be invented**; enabling it would test clinician appetite before committing to build. Caution: the good visits get taken and the awkward one is left. |
| **CN-20** | **Visit dispatching is not enabled.** HCHB's smart scheduling can recommend the next best assignee for a declined or uncovered visit and return it to the scheduler for approval. It deliberately does **not** auto-assign. `[T:510-514]` | The recommend-then-approve pattern the session settled on **already exists in the product**; the gap is quality of recommendation, not the interaction model. |
| **CN-21** | **Real-time clinician location is not visible.** The back office can infer position from sync events but cannot see live location; verification of presence in the home requires a third-party request. Enabling live location is a leadership decision, not a technical one. `[T:406-410]` | Proactive "running late" detection depends on this, and it carries a **clinician-trust cost** that should be weighed deliberately rather than switched on because it is possible. |

## HCHB product limits — require a vendor change or a replacement

**This class is the substantive case for the initiative.** Every entry here is a constraint we cannot
configure away and cannot comply our way out of.

| ID | Constraint | Design implication |
|---|---|---|
| **CN-22** | **Pending-auth visits are invisible and uncounted.** They do not appear on the clinician's calendar, are not visible to leaders, cannot be communicated to the patient, and do not count toward productivity. The scheduler carries them in her head or on a sticky note. `[T:29, 31, 43-44]` | The single clearest capacity-measurement defect in the current state — *if you can't see it, you can't plan.* A pending visit must be **visible, attributable, and counted as committed load** even when it cannot yet be assigned. |
| **CN-23** | **Pending-auth workflow regenerates daily.** HCHB creates a pending-auth workflow every day per patient, and any auth-screen change generates another — roughly 50 a day, almost all with no available action. `[T:33-35]` | The behavioural consequence is worse than the time cost: bulk-clearing becomes habit and the one actionable item goes with it. **Notify on state change, never on state persistence.** |
| **CN-24** | **Clinicians cannot reassign their own visits.** An RN cannot hand a visit to her own LPN, or flip a plotted RN visit to an LPN, without routing it back to the scheduler. Not a Medicare requirement; most EMRs do not impose it. `[T:370-373, 474-476]` | Because routine visit scheduling otherwise requires no steady-state scheduler workflow, **this one restriction generates essentially all recurring scheduler involvement in routine visits. Removing it is the highest-yield single change in the routine-visit flow.** |
| **CN-25** | **Supervisors cannot see supervisee schedules.** An RN cannot see her LPN's schedule, a PT cannot see the PTA's, an RN case manager cannot see the aide's — while remaining accountable for supervising them. Cited as one of the biggest dissatisfiers for JV clinicians who came from systems that allowed it. `[T:377-379]` | The RN manages aide frequency without being able to see the aide's calendar — a **supervision gap** as much as a scheduling one. |
| **CN-26** | **Plan-of-care workflow fires once per discipline.** Four disciplines produce four "complete requested schedule" tasks, then four more at approval — eight tasks for a care-team decision already made. Each discipline's plan of care also operates independently. `[T:586-591]` | The mechanical justification for **care-team-at-referral**. Establish the team once and the tasks collapse. |
| **CN-27** | **Documentation is invisible until sync.** Delivered over Citrix, so the back office sees only that a visit was started or is incomplete. A Tuesday visit may not sync until Friday and reads as undocumented; conversely a started visit is not always a completed visit — a clinician who called 911 has started a visit that did not happen. `[T:209-211]` | **Visit state in the current system is unreliable as a real-time input**, which constrains anything built on top of it. |
| **CN-28** | **Capacity information exists only as manually triggered reports.** Committed load, productivity and LUPA exposure all live in reports someone must run and recombine by hand, one of them roughly 20 columns wide. `[T:125-130, 307-308]` | This is why the scheduling grid exists as a spreadsheet, and why the capacity tool **replaces** it rather than feeding it. Productivity changes every time the scheduler works a piece of workflow, so a once-daily load will not support the decisions made off it. |
| **CN-29** | **Clinicians see only seven days of schedule.** They cannot see a pending SOC in their territory next Thursday while planning Tuesday and Wednesday, so they front-load and then get surprised. `[T:68-69]` | **The visibility horizon is itself a capacity constraint** — clinicians make capacity decisions all week through a seven-day window. |
| **CN-30** | **Coordination notes are the only general routing mechanism.** Because the system lacks workflow for many needs, notes were pressed into service to generate tasks. Better structured than they appear — titled and routed, with Point of Care visit alerts forcing clinician acknowledgment before a visit opens — but still a workaround for absent workflow. `[T:183-186]` | **Replicate the routing behaviour, not the note-as-workflow pattern.** |

## Compassus policy — changeable by us

| ID | Constraint | Design implication |
|---|---|---|
| **CN-31** | **The readiness call is standard procedure.** Required everywhere, not universally performed. `[T:89-91]` | The policy is not the problem; enforcement and effort are. Automating the call removes the reason it gets skipped. |
| **CN-32** | **Growth owns first patient contact.** Meant to make the first touch confirming home health orders. Strong in some markets, absent in others, so the scheduler's call becomes the patient's first contact with Compassus. `[T:97-98]` | The handoff needs to be **visible and verifiable**, not assumed. |
| **CN-33** | **The auth team records payer specifics in a coordination note.** Since an initiative launched early the prior year, verification includes a template snippet of what the clinician needs to know about that payer. `[T:449-450]` | **The payer rules data already exists and is already being captured.** Surfacing it structurally at plan-of-care creation is the low-complexity, high-value win. |
| **CN-34** | **The DCS runs a daily LUPA report from Pulse.** Policy exists; compliance is inconsistent — *supposed to.* `[T:230, 237]` | Replace a discretionary daily report with an **event-driven alert**. |
| **CN-35** | **Contract clinicians are paid regardless of volume and should be filled first.** Fill order: contractors → full-time → part-time → per diem. Counterweight: if you can fill contractors only by taking visits from full-time staff, you did not need the contractor. `[T:145-152]` | Fill order is an encodable policy, with a check on whether the contractor is **genuinely additive**. |
| **CN-36** | **Per-diem minimum utilisation expectations vary by branch.** Some enforce a monthly minimum and release clinicians below it; others carry per diems who have not turned on a device in three months. `[T:142-143]` | Inconsistent policy makes per-diem capacity **unforecastable**. |
| **CN-37** | **Regional safety scripts.** Washington/Providence requires screening questions on firearms in the home, others present, and mental illness — instituted after a clinician was killed in a patient's home. `[T:106-109]` | Scripts must be **regionally variable by design**. This one is a corrective-action commitment, not a preference, and it constrains where a voice agent can substitute for a person. |
| **CN-38** | **The daily afternoon huddle.** DCS, clinical managers and schedulers review all next-day starts against the reports; it can run an hour or more. `[T:551-552]` | The huddle is the **manual compensation for the absence of a shared capacity view**. With one, the session's own estimate was 15 minutes. |

## Cultural and behavioural — changeable by leadership, not by software

Recorded because a tool that ignores them will fail, not because a tool can fix them.

| ID | Constraint | Design implication |
|---|---|---|
| **CN-39** | **Schedulers bulk-clear workflow without reading it.** A rational response to CN-23, with the consequence that actionable items get cleared too. `[T:34-35]` | — |
| **CN-40** | **Some schedulers decline the readiness call.** One named case reasons that confirmation is growth's job. `[T:90-91]` | Automation removes the argument. |
| **CN-41** | **Clinicians have stopped calling in for backup visits.** They do not trust the branch to respond efficiently — either they get sent far away or it takes two hours, by which point their own day is fixed — so they absorb the gap and take one less patient. `[T:197-198]` | **Latent capacity is being lost to a trust deficit**, and the fix is response speed before it is any feature. |
| **CN-42** | **Tenured clinicians resist territory flexibility,** often because they have been burned by inefficient coverage before. `[T:294, 299-300]` | If the branch is well managed and the visits offered make sense, resistance largely dissolves. **Showing the clinician why — the census, the distribution — does more than mandating.** |
| **CN-43** | **Machine-assigned visits get rejected where human-assigned ones would not.** The documented failure mode of prior smart-scheduling attempts. `[T:351-352]` | **The central adoption constraint. The tool recommends; the human accepts.** |
| **CN-44** | **Newer clinicians cede schedule control to patients.** They lack the negotiation skill to land the time that works, become over-accommodating, and push cost onto teammates. Getting the first visit at 8 or 9am is described as the single largest lever on individual capacity. `[T:387-393]` | The assist is **helping the clinician get the appointment they want**, not optimising around a schedule they surrendered. |
| **CN-45** | **PTs retain routine visits that PTAs should take** — partly habit, partly protecting their own volume. Two costs: a higher-paid clinician on a routine visit, and PT capacity unavailable for starts, which is exactly where growth gets blocked. `[T:479-483, 488-493]` | Default to the paraprofessional with **explicit opt-out**, so the change does not depend on a leader making it. |
| **CN-46** | **Incentive holdout behaviour.** If surge pay becomes a pattern, clinicians learn to wait for the higher offer — the airline bump-compensation dynamic. `[T:356-358]` | Gate eligibility on meeting baseline productivity first, and watch for the pattern in reporting. |
| **CN-47** | **Some branches decline to use per-diem staff at all** because they are hard to manage and track. Consequence stated plainly: those branches forfeit the ability to grow, because they must burden full-time clinicians until a new full-time position is justified. `[T:143-145]` | **Per-diem capacity is described as the biggest available weapon against capacity constraint, and it is being left on the table.** |
| **CN-48** | **Coverage recovery runs on relationships.** Visits get covered because a scheduler has built enough goodwill to ask a favour on a Friday afternoon. `[T:204, 383]` | A real asset, not just a gap — and a substantial part of the argument for **retaining a local human role**. |

## Labor agreement — changeable only through negotiation

| ID | Constraint | Design implication |
|---|---|---|
| **CN-49** | **Union position on territory assignment.** A union LPN refused work outside her territory citing union requirement, while her territory carried ~30 patients across a full-time RN and a full-time LPN and neighbouring LPNs were drowning. It was subsequently determined that territory assignment is **not** something a union can dictate — but the position was held and used as leverage. `[T:295-299]` | Showing census and distribution data addresses the argument better than asserting authority. |
| **CN-50** | **Incentive schemes require union approval.** Everything done in the union has to go through the union. `[T:363-366]` | Any marketplace or surge design needs a **union-population variant**, not an exception. |
| **CN-51** | **Salaried and hourly populations cannot be incentivised per visit.** The per-visit and per-point mechanisms used elsewhere do not translate. `[T:363-368]` | A separate incentive instrument is required for these populations, and **it is unresolved**. |

---

## Where the leverage is

Fifty-one constraints, distributed as:

| Count | Class | Meaning |
|---:|---|---|
| **17** | fixed — 11 regulatory, 6 payer | Encode and plan against; no negotiation available |
| **4** | within our control today | HCHB toggles; no new system needed. Two of them (Shift Finder, visit dispatching) would let us **test demand for capabilities we are otherwise planning to build** |
| **9** | product limits | Not configurable, not compliable. The substantive case for the initiative, and the nine most-cited pain points in the session |
| **8** | policy | Ours to change; several are already correct on paper and failing in execution |
| **10** | cultural and behavioural | Leadership and change management. A tool that ignores them fails regardless of quality |
| **3** | labor agreement | Negotiation — and incentive design has an unresolved gap for union, salaried and hourly populations |

**Two observations worth carrying forward.**

1. **The nine product limits are the argument.** If someone asks why configuration is not enough, the
   answer is **CN-22 … CN-30**: invisible pending work, notification noise, no clinician reassignment,
   no supervisee visibility, per-discipline task duplication, unreliable visit state, capacity
   available only as manual reports, a seven-day horizon, and coordination notes standing in for
   workflow. **None of those can be toggled.**
2. **Four of the top pain points are ours, not the vendor's.** CN-18 (order approval), CN-33 (payer
   rules already captured but not surfaced), CN-31 and CN-32 (readiness call and first contact) are
   all within Compassus's control and none require a new system. **They are the fastest available
   wins and are worth pursuing on a separate track from the build.**
