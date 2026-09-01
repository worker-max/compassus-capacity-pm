# Capacity and Scheduling — An Adversarial Business Case

> **What this is.** A business case built to be argued with rather than sold. Six independent
> analyses were run against the initiative — an affirmative case, a case built to kill it, an
> outside view on what comparable programs actually deliver, a search for cheaper alternatives, a
> full cost of ownership, and a forensic audit of the arithmetic in
> [`business-case-register.md`](./business-case-register.md). None was told what conclusion to
> reach. The affirmative analysis was explicitly instructed to treat the existing register as a
> claim to be tested rather than as evidence.
>
> **Status.** 26 Aug 2026. Supersedes the register's headline numbers. The register remains useful
> as a lever inventory; several of its figures were wrong and are corrected here and there.
>
> **The finance case of record** remains
> [`../knowledge/business-case-and-kpis.md`](../knowledge/business-case-and-kpis.md), rendered from
> the 8.13 workbook. This document does not replace it. It tests it.

## 1. The answer in one paragraph

The diagnosis is sound and survived every attack: capacity and scheduling are two functions forced
through one spreadsheet, authorization is the real bottleneck, pending-auth work is invisible, and
payer rules exist in writing but never reach the moment of decision. The proposed *solution shape*
did not survive. We already own a scheduling optimizer that covers most of the requirement on our
own scorecard, we piloted it once, and it failed for reasons no vendor can sell us a fix for. The
honest recommendation is to **fund measurement and configuration now, and defer the platform
decision by two quarters** — not because the initiative is wrong, but because the precondition for
any optimizer working is data we do not yet have, and because that first phase is the same
regardless of which platform decision we eventually make.

## 2. Why the estimates range tenfold, and what to do about it

Five analyses produced answers between **$1.9M and $23M a year**. That is not factual
disagreement. It is four unstated conventions, each worth millions:

| Convention | Choice A | Choice B | Worth |
|---|---|---|---|
| Attribution | Gross benefit | Benefit incremental to cheaper alternatives | ~$6M/yr |
| Revenue base | Medicare fee-for-service (~$260M) | Whole book ($549M) | ~2x on every percentage lever |
| Lever count | The workbook's 4 | The affirmative analysis's 15 | ~$15M |
| Config-achievable value | Credited to the platform | Deducted from it | 15–28% haircut |

**No number should be presented without these four stated on its face.** A CFO shown a single
figure is being asked to trust conventions they cannot see. This is the single most important
formatting rule for the eventual readout.

### The range, under each convention

| Source | Steady-state annual | Convention |
|---|---|---|
| Alternatives analysis | **$1.9M** | Incremental to the cheaper stack |
| Workbook (authoritative) | **$7.9M** | 4 levers, Moderate scenario, ~80 branches, probably episodic-only base |
| Affirmative analysis | **$23M** base ($1M low / $41M high) | 15 levers, whole book, net of run cost and a config haircut |

The workbook's own base may understate: 600 admissions per branch across 80 branches is 48,000
network admissions, which cannot carry $549M of revenue. It is almost certainly episodic-only,
meaning the $7.9M is sized on roughly 31% of the real book.

## 3. What the outside view does to all of it

- Large IT projects deliver **56% less value than predicted** (McKinsey–Oxford, n>5,400).
- Under **30%** of digital transformations succeed; only **16%** succeed and sustain.
- Flyvbjerg (n=5,392): median cost overrun is near zero but the distribution is power-law —
  *"the average cost overrun for IT projects does not exist."* **Cost is not the risk. Benefit is.**
- Estimated probability of delivering a stated business case as written **and demonstrating it:
  10–15%**. For a material majority of the benefit: **25–35%**.
- The modal outcome is neither success nor failure. **40–60% of these programs are never tested
  against outcomes at all.**

Apply the McKinsey–Oxford haircut to the affirmative base case and $23M becomes about $10M a year,
which against a base-case three-year cost of ownership of **$21.7M** is roughly break-even over
three years, turning positive in year four or five, with very wide variance.

### Two reference points that bound the claims

**The headcount claim sits outside the observed distribution.** Non-clinical healthcare headcount
*rose* 12.4% between 2010 and 2022 while EHR adoption went from 9% to 99%. Gartner found 80% of AI
pilots cut staff with no correlation to ROI. And the best published comparable — a multi-branch
home health provider that deployed HCHB Smart Scheduling across 18 live branches — reports **10
roles and ~$700,000 a year**, which scales to roughly **27–44 roles and $1.6–2.6M** at our branch
count. The register's 200 roles and $12M is five to seven times that.

**Field service gives the honest ceiling on optimization gains:** 5–15% travel reduction, 4–15%
productivity. UPS ORION — the best-funded route optimization program in the world — landed at
8–10% after thirteen years. Vendors claim 20–40%. Divide by two to three.

**And the evidence base we would be buying into does not exist.** There is not one peer-reviewed or
quasi-experimental evaluation of any home health scheduling product. Every vendor case study is
n=1 with no control, and several measure across the COVID trough-to-rebound. The vendor publishes
input metrics — "70% of visits auto-scheduled" — never visits per clinician per day.

## 4. The cost, which the register never carried

| Scenario | Year 1 | Year 2 | Year 3 | Total |
|---|---|---|---|---|
| Low | $3.16M | $3.19M | $2.05M | **$8.4M** |
| Base | $8.21M | $8.04M | $5.48M | **$21.7M** |
| High | $20.07M | $17.77M | $11.41M | **$49.3M** |

**Software licensing is ~10% of total cost in every scenario.** Internal program labor is 42% of
the base case — four times the license. Two of the four largest spread drivers are operating-model
choices we control today: whether the capacity steward is net-new headcount, and how much branch
champion time is real.

If it stalls at eighteen months, **$12.2M is spent and $11.2M is unrecoverable.**

**HCHB is a costly integration partner.** No public API, developer portal or sandbox — the
documented path is HL7v2 and CCD over SFTP. It sells a competing optimizer. 44% Medicare market
share and 97.6% retention mean no substitution leverage. Its own license agreement bills
implementation per trainer-day at roughly 20 trainer-days per branch, so implementation scales with
**branch count**, not census. Its partner marketplace with self-serve activation and read/write
FHIR APIs launches in **2027** — which materially changes the cost of a third-party integration
depending on when we move.

## 5. What survived every attack

These were attacked directly and held. They are the initiative's real foundation.

- **Capacity must be solved before scheduling.** Two functions, one spreadsheet, and no forward view.
- **Authorization is the bottleneck**, sitting upstream of the scheduler's queue where the process
  map does not look.
- **Pending-auth work is invisible and uncounted** — the clearest capacity-measurement defect we have.
- **Payer rules exist in writing days before they are needed and never reach the plan of care.**
  Independently supported: 81.7% of appealed prior-auth denials are overturned, meaning the
  information needed to get it right existed and was not at the point of decision.
- **The notification storm is a safety finding, not an annoyance.** Published evidence shows cutting
  low-value alerts raises acceptance of the alerts left standing, with no safety events attributable
  to the suppressed ones.
- **Discipline and role match** is real, episodic-only, and worth low single-digit millions.
- **Schedule volatility predicts quit risk** — 3,716 nurses, payroll-grade data, 9.2 percentage
  points between the 75th and 25th percentile for full-time RNs. Computable from data we already
  hold. Honest caveat: no study anywhere isolates scheduling optimization as the *cause* of a
  measured turnover reduction.

## 6. What did not survive

- **The 300-to-100 scheduler claim.** A hedged verbal aside, contradicted by the best comparable and
  by the sector's own headcount history.
- **The margin-lift framing.** Built on a national all-payer benchmark applied to us, comparing
  cost-report margins to EBITDA margins. Illegitimate as stated.
- **Route and efficiency optimization as a cost lever.** With 70% of clinicians paid per visit, we
  pay the same per visit either way. This kills the standard industry pitch outright.
- **"Reclaim idle salaried capacity."** There is no idle salaried capacity for 70% of the workforce.
- **The register's arithmetic in six specific places**, now corrected in that document.

## 7. The recommendation

**Do not fund a platform purchase now. Fund a two-quarter measurement and configuration phase, and
set gates.**

The reasoning is not risk-aversion. It is that the single most robust success factor in the outside
view — arriving independently from nurse scheduling, last-mile delivery and utility crews — is
**constraint and duration fidelity, not algorithms**. MIT found three in four deliveries did not
follow the planned sequence; the failure mode produces no error message. The vendor's own reference
customer says the same thing in different words: clean data is the key to automation success, and
heavy scheduler override in the first sixty days extends the transition and poisons attitudes.

That is precisely how Alabama failed. **Buying a second optimizer does not address it.**

So the first phase is identical whichever way the platform decision eventually goes:

1. **Measure.** The task census from HCHB workflow records with real handle times. Authorization
   write-offs. Actual LUPA rate and one-visit-short count. Missed and rebooked visit rates.
   Authorization turnaround by payer. Income realization and schedule volatility per clinician.
2. **Configure what we own.** The Workday-to-HCHB PTO interface. Shift Manager with Find Shifts.
   Notification state-change filtering. The rapid-reschedule flag.
3. **Delete what should not exist.** The DCS order-approval routing is already a live executive
   decision. Note honestly that two of the three named workflow problems are classified in our own
   constraint register as HCHB *product limits*, not toggles.
4. **Install standard work.** Payer rules at plan-of-care creation, the readiness-call gate, a
   call-out protocol, paraprofessional defaults. The evidence for narrow, monitored standard work is
   stronger than the evidence for any platform.
5. **Staff the actual constraint** — authorization — rather than harvesting scheduler headcount
   while the bottleneck is upstream.
6. **Price HCHB Smart Scheduling as a costed comparator** in the vendor evaluation, even if it loses
   on capability. It avoids roughly $1M of integration cost and all of the schedule risk, and it is
   currently not being priced at all.

Spend change management ahead of technology. Programs with excellent change management meet their
objectives 88% of the time against 13% for poor — and the largest single jump is from poor to merely
fair. The first dollar is the highest-return dollar.

## 8. Gates, with a pre-committed kill criterion

Decide on the platform at the end of the phase, against evidence:

- Authorization write-offs and LUPA leakage measured. **If both come back small and the pay-model
  analysis holds, the margin program does not proceed.**
- Configuration and standard work delivered a measurable share of the claimed benefit. If the
  cheaper stack captures most of it, the platform must justify only the remainder.
- Baseline exists for the initiative's core metric — quantified capacity and utilization — which by
  our own KPI table is **not available today**, along with 6 of 8 secondary indicators.
- Scheduler override behavior and data hygiene are demonstrably manageable in one branch.

## 9. What would change this recommendation

Stated in advance, so the decision is falsifiable:

- Authorization write-offs come back materially larger than expected. This is the most
  under-instrumented dollar in the business and it could be the largest single lever.
- The pay-model split turns out to be more salaried than 70/30, which revives the reclaimed-capacity
  argument.
- The 2027 HCHB marketplace materially lowers integration cost and risk, changing the platform's
  cost basis.
- MedPAC's recommended 7% CY2027 rate cut lands. That is roughly $18.2M off the episodic book —
  more than the entire base case — and it changes the cost of doing nothing rather than the return
  on doing something.

## 10. A note on how this document was produced

The register it corrects was written by the same author now recommending against its headline. Six
independent analyses were run adversarially against it and found: a circular validation check, a
72% overstatement from using fully-allocated instead of marginal cost, an invented recoverability
constant, a scope error treating Medicare fee-for-service as episodic, a growth lever built on the
wrong margin, and a headcount claim five to seven times the best available comparable. It also
found an authoritative finance case already in this repository that the register had been written
without reference to.

That is the argument for running the exercise this way, and for running it again before any number
here is presented externally.
