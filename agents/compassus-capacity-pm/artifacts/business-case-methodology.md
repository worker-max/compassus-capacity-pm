# Capacity and Scheduling: Factors and Methodology

A walk through every factor considered, how each was sized, and why the numbers can be trusted or
not. Written to accompany the model workbook. Read this first if you are being asked to approve
anything.

---

## 1. What this document is

The business case rests on a chain: how home health gets paid, what that means for a schedule, which
factors carry money, how each was sized, and what we still do not know. This walks the chain in
order. Section 8 states the recommendation.

Every figure in the model is one of five kinds, and the model labels which:

| Tier | Meaning |
|---|---|
| Workbook | Taken from the 8.13 Compassus workbook, which is authoritative |
| Published | From CMS, MedPAC, BLS, peer-reviewed research or a payer manual |
| Derived | Calculated from the above, with the calculation shown |
| Modeled | Built from reasonable inputs where no published figure exists |
| Assumed | Chosen because a number was needed. Flagged in yellow |

Nothing is presented as fact that is actually assumption. Three inputs are still marked yellow and
should be replaced before this leaves the building.

---

## 2. The foundation: how we get paid

Almost every disagreement about scheduling value traces back to this, so it comes first.

**There are three payment mechanics, not two.** Traditional Medicare pays a fixed, case-mix adjusted
amount for a 30-day period. Managed care pays per visit, but only with permission granted in
advance. Commercial and Medicaid pay per visit or per unit against a benefit that runs out. The
common shorthand of "fee-for-service versus managed" hides this, because traditional Medicare is
called fee-for-service but does not pay per visit at all.

**Four separate ceilings act on one episode.** These are independent tests, and the current process
treats them as one.

| Ceiling | What it is | Consequence if crossed |
|---|---|---|
| Permission | What the payer authorized | The visit is not billable |
| Floor | The LUPA threshold, 2 to 5 visits by group | The whole period reprices, a cliff near $1,400 |
| Ceiling | Visits above the floor under episodic payment | They earn nothing |
| Cap | The annual benefit limit on commercial and Medicaid | Care becomes unbillable mid-course |

A visit can be authorized and uneconomic. A patient can be inside authorization and out of benefit.

**Roughly 47 percent of revenue is Medicare fee-for-service and 53 percent is everything else.** The
scheduling system was built when the business was about 90 percent traditional Medicare, which is
the one payer type that requires neither authorization discipline nor visit-count discipline. That
gap is the initiative's core diagnosis, and it survived every attempt to knock it down.

**Seventy percent of clinicians are paid per visit.** This single fact changes the sign of several
standard arguments and is the reason this case looks different from a vendor's. It is dealt with
explicitly in section 4.

---

## 3. The factors, grouped

### 3.1 Demand conversion and perishable capacity

Referral acceptance is improving through the intake system. What happens between acceptance and a
started episode is where this initiative lives: eligibility, authorization keying, intake approval,
clinical review, the welcome call, and the booked visit.

The governing idea is that **capacity is perishable inventory**. A clinician's start-of-care slot
tomorrow either fills or it disappears. It does not roll forward. The faster the yes or no arrives,
the more time exists to fill the slot or replace it before it perishes. That is yield management,
and it is the one value mechanism that is unaffected by the pay model, because filling an empty slot
creates revenue without changing what we pay per visit.

Two further points follow. First, a start-of-care slot and a routine slot are different inventories
with different value density: a lost routine slot under episodic payment costs almost nothing, while
a lost start-of-care slot forfeits an entire episode. Second, that asymmetry argues for reserving
start-of-care capacity rather than letting routine volume consume it, which is what the overload
cycle does today.

### 3.2 Routine delivery throughput

A separate pool of people doing separate work. Paraprofessionals carry the bulk of weekly visit
volume, and their throughput has nothing to do with admissions capacity.

The value here is fill rate. Industry fill rates run 88 to 90 percent, meaning roughly one visit in
ten that is authorized and needed never gets staffed. Faster backfill of cancellations and refusals
attacks that gap directly.

Critically, this pays on the non-episodic book only. Under episodic payment an additional routine
visit above the floor earns nothing, so throughput there converts into coverage without premium
labor and into protection of the floor, not into revenue.

### 3.3 Episode economics

Two opposite risks on the same episode.

The floor is a cliff. Below the threshold the entire period reprices to national per-visit amounts.
Recovery is legitimate only where the visit was clinically indicated and was lost to an operational
failure. It is never legitimate to add a visit to reach a threshold, and a federal audit found 21
percent of claims just above the threshold non-compliant, with contractors now targeting that
cluster.

The ceiling is invisible. Once above the floor, further visits are cost with no matching revenue
until an outlier threshold that is rarely reached. The correct target is neither as many visits as
authorized nor as few as possible. It is the clinically right number, above the floor and no higher
than the period supports.

### 3.4 Administrative cost

Three named sources of load: the start-of-care and recertification cycle, the per-discipline
assignment burst, and authorization chasing and exception recovery. Routine visits are excluded
because they are already clinician self-managed.

Two cautions carried into the model. The loudest pain may not be the largest cost, since the daily
authorization notifications are frustrating but modest in hours unless handle time is high. And some
of this load should be deleted rather than automated, which means the platform cannot claim credit
for it.

### 3.5 Workforce: turnover, and the attraction case

This section is set out in full because it is the lever most often asserted without a mechanism.

**The structural fact.** Under per-visit pay the agency has moved volume risk onto the clinician. A
branch that cannot supply visits, or a clinician who cannot sustain productivity, produces an income
shortfall rather than an agency cost. It comes back months later as turnover, posted to a different
account, with no visible link to the scheduling defect that caused it. With 70 percent of clinicians
paid per visit, most of our scheduling failures are currently being paid for by clinicians.

**The mechanism.** The income realization gap: pay quoted at hire against pay actually realized at
ninety days. Both inputs are outside the clinician's control. Visits per week depends on branch
census, territory alignment, and whether authorization is holding work in a queue nobody can see.
Effective hourly earnings depend on how much unpaid work sits around the visit: travel,
documentation, the evening confirmation calls, and the drive to a canceled visit. It is worst in
year one, when ramp is slow, territory knowledge is absent, documentation is heaviest, and loyalty
is lowest.

**How the number is built.** Five steps, each traceable.

| Step | Value | Source |
|---|---|---|
| Departures per branch per year | 5 | 8.13 workbook |
| Departures across 80 branches | 400 | Derived |
| Replacement cost per clinician | $40,000 | 8.13 workbook |
| Annual cost of turnover at those figures | $16.0M | Derived |
| Reduction assumed, min / mod / max | 5% / 10% / 20% | 8.13 workbook scenario drivers |
| Value, min / mod / max | $0.8M / $1.6M / $3.2M | Derived |

**A baseline check that matters.** 400 departures against roughly 3,000 clinicians is a 13 percent
turnover rate. Published home health RN turnover runs 25 to 28 percent. Either we materially
outperform the sector, or the workbook's departure assumption is low and this lever is understated
by roughly half. Verifying it is a Workday query and it is on the Baseline sheet.

**Why we believe scheduling moves turnover at all.** The best available evidence is a study of 3,716
nurses at a large home health organization using payroll and visit-level data. Full-time RNs at the
75th percentile of schedule volatility were 16 percent more likely to quit than average, and
full-time LPNs 34 percent more likely. Moving a full-time RN from the 75th to the 25th percentile of
volatility cut annual quit probability by 9.2 percentage points. Volatility was defined as the
coefficient of variation of daily visit count over a trailing 28 days, which is computable from data
we already hold.

Two details make it more useful rather than less. The effect disappeared entirely for part-time
nurses, and the authors attribute the mechanism to income and schedule stability mattering to people
who depend on the job. And that is precisely our population: with 70 percent paid per visit,
schedule volatility is income volatility.

**A triangulation worth knowing.** If we targeted only the worst-scheduled quartile, roughly 500
full-time clinicians, and achieved the study's full effect on that group alone, that is about 46
fewer departures a year. The workbook's moderate assumption is 40. The two arrive at nearly the same
place by different routes, which is the strongest support the moderate case has.

**Honest limits.** The study is observational, single-organization, and pre-pandemic. No study
anywhere isolates scheduling optimization as the cause of a measured turnover reduction. And the 5,
10 and 20 percent reduction figures are the workbook's assumptions, not measurements.

**The attraction case, for future years, deliberately not valued yet.**

Retention and recruitment run on the same mechanism, and the recruitment half is currently invisible
in the case. Two arguments will become available once the retention effect is measured:

First, the day-before confirmation burden. Roughly 3,000 clinicians spend about 30 minutes a day,
unpaid and in the evening, confirming tomorrow's visits. Moving that into the system returns
something like two and a half hours of personal time a week to every clinician. That is a recruiting
proposition, not only a retention one, and it speaks directly to why clinicians choose home health
in the first place.

Second, income predictability. A recruit is quoted expected earnings. Whether they realize it
depends today on branch census, cancellation rates, and whether a canceled visit gets backfilled
before the day is lost. A system that protects the clinician's booked week, and that replaces a
canceled visit quickly rather than leaving a hole, converts a recruiting promise into something the
branch can actually stand behind.

It is left unvalued for now because we have no baseline for time to fill, offer acceptance rate, or
cost per hire, and because no published study links scheduling technology to recruiting outcomes.
The four measures needed to value it later are named on the Baseline sheet. This mirrors how the
coding business case handled its own unpriced upside: name the lever, state the mechanism, and leave
the number for when it can be earned.

### 3.6 Geography

Travel is the largest unmeasured capacity leak, and it sits on the non-labor side of the payment,
so it is never wage-index adjusted. Realistic reductions are 5 to 15 percent based on field-service
evidence, where the best-funded route optimization program in the world reached 8 to 10 percent
over thirteen years. Vendor claims of 20 to 40 percent should be divided by two or three.

A related factor nobody had noticed: the wage index applies to the patient's county, not the
agency's, so two identical visits by the same clinician on the same day can differ 15 to 30 percent
in payment. This belongs in territory and capacity planning rather than in a scheduling rule.

### 3.7 Quality-linked revenue

The value-based purchasing band is worth roughly the same as one visit per period, so quality
belongs in the case as a peer of margin rather than a footnote. The measure set changed: acute-care
hospitalisation and emergency department use were retired after the 2025 performance year, and the
functional measures that remain are dose-responsive, which ties them directly to visit timing.

Front-loading is a targeting question, not a volume question. Front-loaded physical therapy is
strongly supported. Front-loaded skilled nursing as a blanket policy is not, having worked for heart
failure and failed for diabetes. First-visit timeliness is well supported independently.

### 3.8 Risk avoided and option value

Neither belongs on a waterfall. Both belong in the narrative. Risk avoided covers threshold-adjacent
billing scrutiny, compliance windows, and wage-and-hour exposure under per-visit and points pay.
Option value covers the extension of the same instrument to hospice, the payer rules library as
proprietary data nobody publishes, and the vendor's partner marketplace opening in 2027.

---

## 4. Methodology

### 4.1 Built adversarially, not advocated

A first case was written, then six independent analyses were run against it: an affirmative case, a
case built to kill the initiative, an outside view on what comparable programs actually deliver, a
search for cheaper alternatives, a full cost of ownership, and a forensic audit of the arithmetic.
None was told what to conclude, and the affirmative analysis was instructed to treat the existing
case as a claim to be tested rather than as evidence.

This matters because the first case was wrong in six specific ways, all found by that process and
all corrected. Section 5 lists them.

### 4.2 Reconciled to the authoritative model

Where the 8.13 workbook has an assumption, the model uses it: contribution per admission,
revenue protected per avoided LUPA, replacement cost per clinician, departures per branch, and the
premium labor pool. This keeps the two models reconcilable rather than competing. Where the
workbook has no assumption, the source is named on the Inputs sheet.

### 4.3 Four attribution conventions, stated openly

Independent analyses produced answers between roughly $2M and $23M a year. The spread is not factual
disagreement. It is four conventions, each worth millions:

| Convention | The two choices |
|---|---|
| Attribution | Gross benefit, or benefit incremental to cheaper alternatives |
| Revenue base | Medicare fee-for-service only, or the whole book |
| Lever count | The workbook's four, or the fuller fifteen |
| Configuration | Value obtainable by configuring what we own, credited or deducted |

No figure should be quoted without these stated alongside it. A reader shown a single number is
being asked to trust conventions they cannot see.

### 4.4 Capacity pools kept separate

Admissions and routine throughput are different people doing different work. Start-of-care capacity
is constrained by qualified clinicians; routine volume is carried largely by paraprofessionals.
These are additive rather than double counted. Productivity improvements are valued once, through
the pool where they actually land.

### 4.5 Every lever tested against payer class and pay model

Each lever was checked twice: does it behave the same under episodic and non-episodic payment, and
does it survive a workforce paid per visit. Several did not.

Route and efficiency optimization does not create margin under per-visit pay, because the same
amount is paid per visit either way. Reclaiming idle salaried capacity does not apply to 70 percent
of the workforce. Rebook waste is smaller than it appears, and the missed-visit loss is roughly
halved. These corrections made the case smaller, and they were kept.

### 4.6 Ranges, not point estimates

Every driver carries a minimum, moderate and maximum, and the model shows all three. The moderate
column is the planning number. The bounds are set by evidence rather than by optimism: the scheduler
lever is capped by the best published comparable, travel by field-service results, admissions by the
only published lift figures available.

### 4.7 The outside view applied as a haircut

Large technology programs deliver materially less than predicted, and the modal outcome is that
the case is never tested at all. The model carries a haircut input so the expected case can be shown
next to the promised case rather than instead of it.

---

## 5. What was corrected, and why it matters

Presented openly because it is the evidence that the method works.

| Correction | Effect |
|---|---|
| A validation check that was circular and could not fail | Removed. It proved nothing |
| Fully-allocated cost used for an incremental visit | $24M became $14M |
| A margin figure described as blended that was fee-for-service only | The growth lever roughly halved |
| A recoverability rate that was assumed rather than sourced | LUPA recovery restated with a band |
| Medicare fee-for-service revenue treated as episodic revenue | Several derived figures rebuilt |
| A headcount claim five to seven times the best comparable | Rebuilt from evidence |

A finance case already existed in the repository that the first pass had been written without
reference to. That is now the reconciliation anchor.

---

## 6. What we do not know

Three inputs are unresolved and marked yellow in the model. The admissions lever scales linearly
with the first.

- **Network admissions per year.** The workbook figure cannot carry the stated revenue, so either
  admissions are higher, branches are more numerous, or the revenue figure covers more than home
  health.
- **Episodic period count.** Two defensible derivations differ by 60 percent.
- **Mileage spend.** The current figure is invented and must be replaced.

Beyond those, the largest genuinely unknown quantity is authorization write-offs: visits delivered
outside a payer's backdating window and written off. Nobody counts it. It could be immaterial or it
could be the largest single lever in the case.

---

## 7. How to use the model

Open the Inputs sheet. Blue cells are editable, black cells are formulas, yellow cells are
unresolved. Set the benefit scenario and the cost scenario independently, because an ambitious
benefit case does not require an ambitious spend case. The Levers sheet always shows all three
columns. The Baseline sheet lists what must be measured before any figure is committed, with the
source system and the effort for each.

One result worth knowing before you start: at maximum benefit against maximum cost the program is
net negative over three years, because cost scales faster than benefit. The leverage is in holding
cost down while pushing benefit, and the two largest cost swings are internal choices rather than
vendor pricing.

---

## 8. The recommendation

Fund measurement and configuration now. Defer the platform decision by two quarters.

The reasoning is not caution. The most robust success factor across three unrelated bodies of
evidence is constraint and duration fidelity in the underlying data, not the quality of the
algorithm. The vendor's own reference customer says the same thing: clean data is the key, and heavy
scheduler override in the first sixty days extends the transition and damages attitudes. That is
precisely how the earlier pilot failed, and it is not something a second tool can fix.

The first phase is therefore identical whichever way the platform decision eventually goes:

1. Measure. The five low-effort items on the Baseline sheet size five of the seven levers and are
   queries against systems we already own.
2. Configure what we already own, and switch on what is switched off.
3. Delete workflow that should not exist, where it is genuinely configurable.
4. Install standard work, starting with payer rules at plan-of-care creation.
5. Staff the actual constraint, which is authorization, rather than harvesting scheduler headcount
   while the bottleneck sits upstream.
6. Price the incumbent system's own scheduling module as a costed comparator in the vendor
   evaluation, even if it loses on capability.

Then decide, against evidence, with a kill criterion committed in advance: if authorization
write-offs and floor leakage come back small and the pay-model analysis holds, the margin program
does not proceed.
