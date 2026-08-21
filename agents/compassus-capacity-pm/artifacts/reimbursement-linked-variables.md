# Reimbursement-Linked Factors for Capacity and Scheduling Logic

> **What this is.** The factors and variables that reimbursement adds to the capacity and scheduling
> model, organised by where each one binds in the logic rather than by topic. Companion to
> [`payer-types-and-episode-economics.md`](./payer-types-and-episode-economics.md) and to the
> `Flow-Payer-Economics` sheet.
>
> **On identifiers.** Written with descriptive names rather than variable IDs. The payer handoff
> document assigns SH-10 through SH-14 and S-43 to payer variables, while
> [`variable-backlog.md`](./variable-backlog.md) reserves S-43 and S-44 for consent and power of
> attorney and proposes S-45 for insurance authorisation. Those assignments collide and the 8.13
> workbook has to adjudicate. Names do not go stale on a renumber; IDs do.

## The organising principle

Four ceilings act on one episode, and the current model conflates them.

| Ceiling | What it is | Whose rule | Failure if ignored |
|---|---|---|---|
| Permission | Authorisation: what the payer allows | The payer contract | The visit is non-billable |
| Floor | LUPA: too few visits reprices the period | CMS, by case-mix group | A cliff, roughly 1,200 to 1,400 dollars |
| Ceiling | Utilisation: visits above the floor earn nothing | The economics of a flat payment | Silent margin erosion |
| Cap | The annual benefit limit | The plan, or the employer | The patient is stranded mid-course |

These are independent tests. A visit can be authorised and still be uneconomic. A visit can be
economic and still be unauthorised. A patient can be inside authorisation and out of benefit.

## 1. Payer and episode spine

Read by every module. Most of it does not exist in structured form today.

| Factor | Why the logic needs it | Source |
|---|---|---|
| Payment basis: episodic, per visit, per unit | Determines whether a delivered visit generates revenue at all | Referral, via intake |
| Permission required, yes or no | Independent of payment basis. One large plan dropped home health authorisation in 36 states in 2025 | Payer rules library |
| Plan and product line | Rules vary inside one payer brand | Referral |
| Funding type: fully insured or self-funded | The employer sets the cap on 67 percent of covered workers | Eligibility verification |
| Governing plan versus paying plan | Out-of-state members: the home plan's policy governs, the host plan pays | Eligibility verification |
| Delegated utilisation vendor | Network, authorisation and claim may sit with a vendor | Payer rules library |
| Payment period number and boundaries | Two 30-day periods per certification period, independently classified | Computed |
| Day n of 30 | Period state is what makes a missed visit cost 25 dollars or 1,300 | Computed |
| Admission source, community or institutional | Case-mix driver | Claims and referral |
| Timing, early or late | Resets after a 60-day gap | Computed |
| Clinical grouping, functional level, comorbidity subgroup | Together they set the case-mix group | OASIS and coding |
| Case-mix weight | Sets the period payment | Reference lookup |
| LUPA threshold for the group | 2 to 5 visits in CY2026, recalibrated annually | Reference lookup |
| Outlier threshold | Where visits become revenue again, roughly 15.8 nursing visits | Computed |
| Rate year selector | Keys off the claim Through date, not start of care | Computed |
| Annual cap and visits consumed to date | Non-episodic only | Payer rules plus internal history |

## 2. The authorisation object

An authorisation is a per-discipline quantity inside a dated window. It is never a scalar, and a
single "visits remaining" integer cannot represent any of the following.

| Field | Detail |
|---|---|
| Scope | A discipline, or a pool of disciplines sharing one allowance |
| Quantity | The allotment |
| Unit | Visits, hours, or 15-minute increments. Not interchangeable |
| Window length | 30 days, a rolling 7-day week, a certification period, a calendar year |
| Window start rule | At least six variants: hospital discharge, discharge to residence, start of care, first service date, authorisation start day, calendar year |
| Pending-auth allowance | Visits schedulable before authorisation is in hand. Observed at 1, 3, 5 and 10 |
| Backdating window | Zero to five days at most payers. The real answer to whether pending-auth work is payable |
| Completion gate | The proportion that must be delivered before more is granted |
| Documentation gate | What must be documented to support continuation |
| Reauthorisation lead time | A plan gating at 30 units and expecting contact at 25 fires the workflow five visits early |
| Discipline substitution mandate | Some payers require an LPN visit rather than an RN visit |
| Observed turnaround | Measured internally. No public source exists for home health |
| Source and last verified | A stale rule produces confident wrong advice |

## 3. Capacity layer additions

The current capacity read is productive visit-hours by discipline by zone. Reimbursement adds what
it cannot see.

| Factor | What it changes |
|---|---|
| Pending-auth visits as counted capacity | They sit on no calendar and count toward nothing, distorting the read in both directions |
| Period-state distribution of the census | Committed demand is not only visits scheduled, it is visits required to protect floors |
| Auth-blocked backlog | Accepted demand the branch cannot yet serve, invisible on the current map |
| Reauthorisation calendar | Gate dates are computable in advance, so this is forecastable load |
| Payer mix of census and pipeline | Drives administrative load, not only revenue |
| Pay model per clinician | Determines the marginal cost of one more visit, and whether optimisation can produce margin at all |
| Points weights | Admissions run 1.62 to 1.72 times a routine visit in the home |
| Contract and per diem cost tier | The marginal cost of overflow capacity |
| Wage index market | Labour share is about 75 percent, and travel sits on the non-labour side |

## 4. Where each factor binds

| Decision point | Reimbursement factors that should be present |
|---|---|
| Referral acceptance | SOC capacity, payer class, expected authorisation turnaround, benefit window start rule |
| Welcome call | Whether the patient is home, and how many benefit days are already consumed |
| Plan of care creation | The highest-value surfacing point: allowance by discipline, pooled disciplines, floor, ceiling, cap, substitution mandates |
| Assignment | Authorisation availability per visit, discipline and role match, continuity, territory, competency |
| Day-before confirmation | Whether the visit is floor-critical, and whether the window closes before any alternative date |
| Disposition | A floor-critical visit must not be silently rescheduled past a period boundary |
| Missed visit | The 48-hour notification, the floor impact, and the effect on the next completion gate |
| Recert and discharge | A new certification period is a new authorisation question, a new group and a new threshold |

## 5. Derived fields

Where reimbursement becomes operational rather than informational.

| Computed field | Definition |
|---|---|
| Visits to floor | Threshold minus visits delivered, this period |
| Days remaining and recoverability | Whether the floor is still reachable with the days and capacity left |
| Marginal revenue of the next visit | The floor visit carries the full period differential. The next carries zero |
| Marginal cost of the next visit | Pay-model dependent |
| Period contribution to date | Revenue minus delivered visit cost |
| Authorisation burn rate and projected exhaust date | Units consumed per week against units remaining |
| Reauthorisation trigger date | Allotment boundary minus payer lead time |
| Benefit-window days consumed before start of care | Referral-to-SOC latency expressed as benefit lost |
| At-risk delivery flag | Visit delivered before authorisation confirmed, with backdating status |
| Rebook waste | Two slots consumed to deliver one visit |

## 6. Postures

| Posture | Applies to |
|---|---|
| Read, never weighted | Margin consequence and period utilisation against payment. Shown at the moment of decision, never in an objective function |
| Assist | Surfacing payer rules at plan of care, computing reauthorisation dates, decrementing counters, flagging floor risk with days and visits remaining |
| Control, rule-based only | Deriving the pending-auth allowance from the payer, deriving window dates from the start rule |
| Never automated | Frequency, discipline substitution against clinical judgement, assignment without human acceptance |

The two highest-value automations — decrementing the counter and computing the reauthorisation
trigger — need no payer integration at all. Both are agency-side, and no major clinical system does
them today. Everything requiring payer cooperation waits on the electronic prior authorisation
requirement effective 1 January 2027.

## 7. What must never enter the logic

- No visit added to clear a floor. A federal audit found 21 percent of claims just above the
  threshold non-compliant, with contractors committed to targeting that cluster.
- No margin term in an assignment objective function.
- No telehealth substitution for a floor visit. Virtual visits count toward nothing.
- No assumption that one payer's rule generalises to its own other product lines.

## 8. What must be instrumented

Each is a measurement task, not a research task, and each is unknown today.

- Authorisation turnaround by payer, submission to response
- Denial rate and top denial reasons
- Missed-visit rate, and how often a miss becomes a floor event
- Decline reason, and the content of the reassign recommendation
- Rebook rate and its slot cost
- Cost per period by case-mix group, from finance
