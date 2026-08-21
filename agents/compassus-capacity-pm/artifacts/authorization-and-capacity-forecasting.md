# Authorisation as a Capacity Forecasting Input

> **What this is.** How authorisation enters the capacity forecast, which parts of it are tractable,
> which are genuinely unpredictable, and what to build for each. Companion to
> [`reimbursement-linked-variables.md`](./reimbursement-linked-variables.md).
>
> **The short version.** Most of the authorisation forecasting problem is deterministic and ignored,
> not stochastic and hard.

## 1. Three separate mechanisms

| Mechanism | What it does to demand | How predictable |
|---|---|---|
| Front-door latency | Shifts when demand lands. Nothing is schedulable until eligibility is verified, pending auth is keyed and intake gives final approval | Stochastic, payer-specific, unmeasured. The genuinely hard one |
| Ceiling truncation | Changes how much demand exists. Frequency is written to clinical need, authorisation allows less | Deterministic once the payer rule is known, invisible at the moment it matters |
| Gate events | Creates administrative demand mid-episode at computable points | Arithmetic, not forecasting |

The forecast today is built on ordered frequency, and authorisation then truncates it. The demand
curve is therefore systematically overstated for managed patients, and the error is invisible
because nobody compares ordered visits to authorised visits.

## 2. The tractable part is larger than it feels

**The reauthorisation calendar.** A plan gating at 30 units with a five-visit lead time produces a
known workflow event on a known date once burn rate is known. Across a census that is a forecastable
administrative load curve rather than a stream of surprises.

**The truncation gap.** Ordered visits minus authorised visits, per discipline, per patient,
aggregated to the branch. That single number states how much of the forecast is fiction, and it is
computable the day the plan of care is written.

**Floor-protected demand.** Visits required rather than planned, because the period would otherwise
reprice. Committed demand with a deadline, which should be reserved before discretionary work is
scheduled.

None of that requires predicting payer behaviour. It requires the payer rule and a counter.

## 3. What is genuinely hard

**Front-door turnaround.** Nobody in the discovery session knew the queue time, and no public source
has it for home health. It is payer-specific, it drifts, and it sits upstream of the scheduler's
queue where the current process map does not look. It has to be measured before it can be forecast,
and measuring it is a few weeks of instrumented data rather than a project.

**The initial-assessment squeeze.** The federal condition of participation requires the initial
assessment within 48 hours of referral, which is faster than many plans' authorisation turnaround.
The branch is structurally forced either to work at risk or to delay. That is a policy decision
needing an approver, and it distorts the forecast because at-risk visits exist in a state nothing
counts.

**Rule change with no notification.** Contracts renegotiate irregularly. The largest Medicare
Advantage plan removed home health prior authorisation across 36 states in April 2025, flipping a
large slice of the book from managed to unmanaged, and the widely cited prevalence figure has still
not been recalculated. That cannot be forecast. It can only be detected.

**January 1.** Annual caps reset, deductibles reset, and members switch plans after annual
enrollment. For a non-episodic book that is a hard discontinuity in both benefit availability and
payer mix, hitting every branch at once. A forecast trained on a trailing 13 weeks walks into it.

**Delegated vendor changes.** When a plan moves authorisation to a utilisation vendor mid-year, the
portal, the turnaround and often the allowance change together, with the contract unchanged.

## 4. The design answer to the unforecastable part

Treat the payer rules library as a monitored feed, not a static configuration.

- Every rule carries a source and a last-verified date, and ages visibly.
- Observed behaviour is compared against the stored rule. When the allowance issued stops matching
  the allowance on file, or turnaround drifts, that is an alert: the rule changed and nobody told
  us.
- Drift is detectable long before a contract amendment is read. The authorisation team already sees
  it patient by patient; the system's job is to notice the pattern.

That converts "we cannot stay ahead of payer changes" into "we detect them in days rather than
quarters." It is the same posture as the CMS reference data with a different failure mode: CMS
changes on a schedule and publishes; payers change without warning and do not.

## 5. What the forecast should emit

Three curves rather than one, because they behave differently.

| Layer | Definition | Use |
|---|---|---|
| Committed | Authorised, scheduled, floor-protected | Capacity genuinely spoken for |
| Probable | Pending authorisation, weighted by payer approval rate and turnaround | Demand that will land, with a date distribution |
| Blocked | Referrals held upstream in verification and final approval | Accepted demand the branch cannot yet serve |

The blocked layer would change the conversation most, because it is currently nobody's number. It
is the quantified version of *we know we have the referral, but it is just not in my workflow to
schedule yet*.

## 6. Leading indicators

- Authorisation queue age by payer, by day. Rising queue age today is delayed starts next week.
- Turnaround drift week over week. The earliest signal of a payer or vendor change.
- Truncation gap trend. A widening gap means either plans of care are drifting from payer reality or
  the payer tightened.
- Burn rate against window, per patient. Feeds the reauthorisation trigger and catches pooled
  discipline competition early.
- Backdating exposure. Visits delivered against pending authorisation still inside their payable
  window, and those that have fallen outside it. Real dollars, currently held on a sticky note.
- Pending-auth inventory as a share of census. If it grows, the capacity read is getting less
  accurate.

## 7. One timing note

The electronic prior authorisation requirement effective 1 January 2027 is a step change in
front-door latency, and it lands inside this initiative's scale phase. Design the authorisation
state model so turnaround is a measured input rather than a hard-coded assumption, and the forecast
improves on its own when it arrives instead of needing a rebuild.
