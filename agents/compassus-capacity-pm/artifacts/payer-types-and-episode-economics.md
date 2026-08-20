# Payer Types and Episode Economics

> **What this is.** A reference document describing how each payer type pays for home health, what
> each one constrains, and what changes in scheduling as a result. It exists because the variable
> inventory had no payer dimension, and because the workflow was built when the business was
> roughly 90 percent traditional Medicare and has never been rebuilt for a managed book.
>
> **Status.** External reference knowledge, researched August 2026 against published rules, payer
> manuals and federal sources. The supporting corpus with full citations is in
> [`reimbursement-research/`](./reimbursement-research/). This is not Compassus discovery material
> and does not supersede anything in [`../knowledge/`](../knowledge/).
>
> **Standing caution.** Payer-specific rules named here come from published manuals and policies,
> not from contracts. Any rule that will drive a scheduling decision must be confirmed against the
> contract by the authorization team before it is relied on.

## 1. The naming problem, resolved first

"Straight Medicare," "traditional Medicare" and "Medicare fee-for-service" are the same thing. But
in home health, traditional Medicare does not pay fee-for-service in the mechanical sense. It pays a
case-mix-adjusted lump sum for a 30-day period. The only time traditional Medicare pays per visit
for home health is when the period falls below its visit floor, which is the penalty state.

So "fee-for-service" names the program, not the payment mechanic. Three payment mechanics actually
exist: an episodic lump sum, a per-visit payment against an authorization, and a per-visit or
per-unit payment against a benefit cap.

## 2. The two axes

Every payer sits at the intersection of two independent questions.

**Axis one. Episodic or non-episodic. What does payment attach to?**

Episodic: payment attaches to a period of care. Once the visit floor is cleared, revenue is fixed.
Additional visits generate no additional revenue, so visits are cost. Risk runs in two directions.

Non-episodic: payment attaches to the delivered unit of service, whether that unit is a visit, an
hour or a 15-minute increment. Revenue follows the work. Risk runs in one direction.

**Axis two. Managed or unmanaged. Is permission required before the work?**

Managed: an authorization gates delivery. An unauthorized visit is non-billable regardless of
clinical need.

Unmanaged: no authorization. Eligibility and physician orders are the only gate.

| | Unmanaged | Managed |
|---|---|---|
| Episodic | Traditional Medicare under PDGM | Medicare Advantage on an episodic contract |
| Non-episodic | Some commercial products, including federal employee plans with no prior approval | Medicare Advantage on a per-visit fee schedule, most commercial, Medicaid and managed Medicaid |

Traditional Medicare is the only combination with no permission gate. That single fact explains why
a workflow built for a traditional-Medicare book does not fit a managed one.

## 3. Four ceilings, and they are independent

The current model conflates these. They are four separate tests, and a scheduling decision has to
pass all four.

| Ceiling | What it is | Whose rule | Failure if ignored |
|---|---|---|---|
| Permission | Authorization: what the payer allows | The payer contract | The visit is non-billable |
| Floor | LUPA: too few visits reprices the whole period | CMS, by case-mix group | A cliff of roughly 1,300 dollars per period |
| Ceiling | Utilization: visits above the floor earn nothing | The economics of a flat payment | Silent margin erosion |
| Cap | The annual benefit limit | The plan, or the employer | The patient is stranded mid-course |

A visit can be authorized and still be uneconomic. A visit can be economic and still be
unauthorized. A patient can be inside authorization and out of annual benefit.

## 4. Comparison by payer type

| Dimension | Traditional Medicare | Medicare Advantage | Commercial | Medicaid |
|---|---|---|---|---|
| Field name | Straight Medicare, traditional, fee-for-service | Managed Medicare, MA, Part C | Commercial, private, employer | Medicaid, managed Medicaid, MCO |
| Episodic or non-episodic | Episodic | Mixed, and per-visit is the larger share. Roughly 60 percent of stays were per-visit in the only published multi-branch dataset. A visible minority drift toward 30-day episodic windows aligned to PDGM | Non-episodic | Non-episodic |
| Managed or unmanaged | Unmanaged | Usually managed, but no longer universally. The largest plan removed home health prior authorization across 36 states and the District of Columbia in April 2025 | Usually managed. Some products require no prior approval at all | Managed |
| Unit of payment | The 30-day payment period, case-mix adjusted | The authorized window, or the authorized visit | The visit | The visit, the hour, or the 15-minute unit |
| Amount, CY2026 | 2,038.22 dollars base, adjusted by case-mix group. Weights range 0.5364 to 1.9558 | Contracted, not published. Reported below traditional Medicare, never quantified in a public primary source | Contracted per-visit rate, plan specific | State fee schedule or MCO contract |
| What generates revenue | The period itself, once above the visit floor. Delivering more visits does not increase it | The authorized, delivered and documented visit or window | The delivered visit, until the annual benefit is exhausted | The delivered unit, inside the authorized quantity and window |
| Prior authorization | None. Automatically authorized | Required by most plans, adjudicated by portal. Median standard response ranges from under one day to two days at the large plans | Varies. Federal employee products publish no prior approval requirement | Required, and metered in units or hours |
| What sets the visit ceiling | Economics. The payment is flat above the floor | The payer, per discipline, per window | The annual benefit cap, and the employer where the plan is self-funded | The state or MCO cap |
| Floor risk | Real and severe. Below the group's threshold, 2 to 5 visits in CY2026, the entire period reprices to national per-visit amounts | None inherent, unless the plan's own episode construct carries one | None | None |
| Ceiling risk | Severe and invisible. In a period with a 4-visit threshold, the fourth visit is worth 1,363.47 dollars and visits five through fifteen are worth nothing. The outlier threshold is not reached until roughly 15.8 nursing visits | Capped by authorization before it becomes an economic question | Capped by benefit | Capped by units |
| Direction of financial risk | Two directions. Too few visits triggers the floor, too many erodes margin | One direction, and the constraint sits upstream and administrative | One direction, plus a cap that can strand a patient mid-course | One direction, plus pooled disciplines competing for one allowance |
| Cost of one missed visit | About 25 dollars mid-period, or 1,258 to 1,386 dollars if it drops the period below the floor. A hundredfold swing determined entirely by period state | The revenue for that visit, plus risk to the completion gate for the next authorization | The revenue for that visit | The revenue for that unit |
| Cost of a rebooked visit | Two slots consumed to deliver one visit. Under a fixed period payment that waste lands directly on margin | Two slots, one billable visit | Two slots, one billable visit | Two slots, one billable unit |
| Who publishes the rules | CMS, in the annual rule, including a machine-readable 432-row case-mix and threshold file | Nobody publicly. CMS plan-reported data cannot tell you a given plan's home health rule. Captured per contract, per branch, at implementation | The plan document or summary plan description. 67 percent of covered workers are self-funded, so the employer sets it | The state provider manual, plus the MCO's own overlay |
| Refresh cadence | Annually with the final rule, effective by calendar year | On contract renegotiation. Irregular and easy to miss | On plan year and on renegotiation | On state plan amendment and MCO contract |
| Primary scheduling consequence | Plan the clinically right number of visits, above the floor and no higher than the period payment supports | Secure authorization before the visit, and keep the completion and documentation gates fed | Track cumulative visits against the annual cap from day one | Track units against a pooled allowance inside a dated window |

## 5. CY2026 reference amounts

Verified against the final rule. These are reference data on an annual cadence, not configuration.

| Item | CY2026 |
|---|---|
| National standardized 30-day period payment | 2,038.22 dollars (1,998.41 without quality reporting) |
| Case-mix weight range | 0.5364 to 1.9558 |
| LUPA threshold range | 2 to 5 visits, by case-mix group |
| Per-visit, skilled nursing | 176.96 dollars |
| Per-visit, physical therapy | 193.42 dollars |
| Per-visit, occupational therapy | 194.74 dollars |
| Per-visit, speech-language pathology | 210.25 dollars |
| Per-visit, medical social services | 283.64 dollars |
| Per-visit, home health aide | 80.12 dollars |
| LUPA add-on, first visit in a period | 304.37 dollars |
| Permanent behavior adjustment | minus 1.023 percent |
| Temporary adjustment | minus 3.0 percent, one year |

Two traps. The rate year is selected by the claim Through date, not by start of care, so a period
spanning New Year prices entirely at the new year's rates. And the temporary adjustment is never
carried forward into the following year's base, so compounding it introduces roughly a three percent
error.

## 6. What changes when the payer is episodic

Three things behave differently, and each breaks a rule currently applied uniformly.

**A missed visit means the opposite thing.** Under non-episodic payment a missed visit is lost
revenue, proportional and intuitive. Under episodic payment it is not a revenue event at all, until
it drops the period below the floor, at which point it is a cliff. Any module reporting financial
risk has to compute it per payer class rather than applying one rule.

**Discipline and role match becomes a margin lever, not only a cost lever.** The episodic period
pays the same regardless of which discipline delivered the visit, so an appropriate paraprofessional
substitution converts directly to margin and frees the higher-licensed clinician for starts. Under
non-episodic payment the same substitution changes both cost and revenue, and the net depends on the
rate differential.

**Utilization management and scheduling stop being separate concerns.** In the flat zone the plan of
care is where margin is set. Industry-wide, visits per 30-day period fell from 10.2 in 2019 to 8.4
in 2024 while discharge to community fell from 85.2 percent to 82.8 percent, so under-dosing is a
live risk rather than a theoretical counterweight.

## 7. The authorization object

The most important structural point in this document. An authorization is not a number. It is a
per-discipline quantity inside a dated window, and every field below has been observed to vary.

| Field | Detail |
|---|---|
| Scope | A discipline, or a pool of disciplines drawing on one allowance |
| Quantity | The allotment |
| Unit | Visits, hours, or 15-minute increments. Not interchangeable |
| Window length | 30 days, a rolling 7-day week, a certification period, a calendar year |
| Window start rule | At least six variants: hospital discharge, discharge to residence, start of care, date services first provided, authorization start day, calendar year |
| Pending-auth allowance | Visits schedulable before authorization is in hand. Observed at 1, 3, 5 and 10 |
| Backdating window | Zero to five days at most payers. This is the real contractual answer to whether pending-auth work is payable |
| Completion gate | The proportion of the allotment that must be delivered before more is granted |
| Documentation gate | What must be documented to support continuation |
| Reauthorization lead time | A plan gating at 30 units and expecting contact at 25 is saying the workflow fires five visits early |
| Discipline substitution mandate | Some payers require an LPN visit rather than an RN visit |
| Observed turnaround | Measured internally. No public source exists for home health |
| Source and last verified | Rules go stale on renegotiation, and a stale rule produces confident wrong advice |

Two failure modes worth naming. Reauthorization at some plans takes up to 14 days and the clock can
restart when missing clinical documentation arrives, which means an incomplete submission is worse
than a late complete one. And the federal condition of participation requires the initial assessment
within 48 hours of referral, which is faster than many plans' authorization turnaround, so the
branch is structurally forced either to work at risk or to delay.

## 8. Where Blue Cross Blue Shield lands

Blue Cross Blue Shield is not a payer class. It is a brand spanning four of them, and the card does
not tell you which.

| Face | Class | Episodic or non-episodic | How it pays home health |
|---|---|---|---|
| Commercial, fully insured | Commercial | Non-episodic | Per visit against an annual benefit cap. Prior authorization varies by plan |
| Self-funded, administered only | Commercial, employer designed | Non-episodic | Per visit. The employer sets the cap. Real plan documents show 40, 45, 60 and 100 visits |
| Medicare Advantage | Managed Medicare | Increasingly episodic | Authorization on 30-day windows. At least one plan moved to 30-day intervals in May 2026 explicitly to align with PDGM |
| Managed Medicaid | Managed Medicaid | Non-episodic | Units and hours against a state-capped, MCO-administered allowance |
| Federal employee program | Commercial, federally negotiated | Non-episodic | Per-visit copay against hard annual caps of 50, 25 and 10 visits by product, with no prior approval requirement |

Two complications specific to these plans. Under the national card program, when the member's plan
is issued out of state, the home plan's policy governs while the host plan pays. And self-funded
employers set their own caps, so two members holding the same card can have different benefits.

## 9. Observed payer patterns

Sourced from conversation and from published manuals, not from contracts. Verify before use.

| Payer | Pattern |
|---|---|
| A national Medicare Advantage plan | Five nursing visits initially, four of five must be completed, and documentation must support the need for the sixth. A plan of care written at twice weekly for four weeks against that allowance guarantees a week-three problem |
| Indiana Medicaid | A 30-day window running from the hospital discharge date rather than the admit date. Therapy disciplines draw on one pooled allowance. Five days between discharge and start of care consumes a sixth of the benefit before the first visit |
| Ohio Medicaid | An 8-hour daily cap across disciplines and a 14-hour weekly cap excluding therapy. Cited as the case where the discharge date is knowable in advance, so capacity can be projected forward |
| Texas Medicaid | Metered against a rolling seven-day week keyed to the authorization start day, with recoupment for overages |
| Montana Medicaid | A genuine shared pool across nursing and therapy under one authorization number, with the reauthorization gate expressed as burn-rate lead time |
| General patterns | Some payers grant one authorization at a time, capping the week regardless of ordered frequency. Some will not pay for a skilled nursing visit and require an LPN visit instead |

## 10. What this binds in scheduling

| Decision point | Payer factors that should be present |
|---|---|
| Referral acceptance | Start-of-care capacity, payer class, expected authorization turnaround, benefit window start rule. If the window runs from hospital discharge, the benefit is already burning before admission |
| Welcome call | Whether the patient is actually home, and how many days of benefit are already consumed |
| Plan of care creation | The highest-value surfacing point. Payer allowance by discipline, pooled disciplines, visit floor, period payment ceiling, annual cap, substitution mandates. Frequency is written here and payer limits are invisible here today |
| Assignment | Authorization availability per visit, discipline and role match, continuity, territory, competency |
| Day-before confirmation | Whether the visit is floor-critical, and whether the authorization window closes before any proposed alternative date |
| Disposition | A floor-critical visit must not be silently rescheduled past a period boundary |
| Missed visit | The 48-hour physician notification, the period floor impact, and the effect on the completion gate for the next authorization |
| Recertification and discharge | A new certification period is a new authorization question, a new case-mix group and a new threshold |

## 11. Guardrails

- No visit is ever added to clear a floor. A federal audit found 21 percent of claims just above the
  threshold non-compliant and CMS committed contractors to targeting that cluster. The defensible
  lever is timing, not volume.
- Margin consequence may be displayed at the moment of decision. It may never enter an objective
  function or weigh against clinical need. The clinician originates frequency.
- Virtual visits do not count toward the floor, the visit count or payment, so telehealth cannot
  substitute for a floor visit.
- No payer's rule generalizes to its own other product lines without checking.

## 12. What we still do not have

- Verified rules for every payer in the book, sourced from contracts rather than recollection. This
  remains the single largest content gap.
- Authorization turnaround by payer. Measurable from existing data, never measured.
- The authoritative list of which payers permit pending authorization to be used.
- Cost per payment period by case-mix group, from finance. Until this exists the utilization ceiling
  stays directional rather than credible.
- Plan-specific rules for the second-largest Medicare Advantage plan, which holds 20 percent of the
  national market.
