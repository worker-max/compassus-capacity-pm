# The Affirmative Case for the Capacity and Scheduling Initiative

**An independent, evidence-based sizing.** Built 21 August 2026 from primary material: the Compassus
discovery and whiteboard sessions, the seven-file sourced reimbursement corpus, and federal and
peer-reviewed sources retrieved directly — MedPAC's March 2026 Report to Congress (Chapters 8 and 14),
the CY2026 HH PPS final rule and CY2027 proposed rule, 42 CFR, CMS QSO-26-11, the 2024 CAQH Index, BLS
OEWS and ECEC, HHS OIG, and the published home health workforce literature.

**Method.** Every lever carries a mechanism, arithmetic you can check, a source, a confidence grade and
a time-to-value. Where the existing `business-case-register.md` reached a number I re-derived it
independently rather than inheriting it. Where I land somewhere different I say so and say why — and
**two of my corrections make the case smaller, not bigger.**

**What this is not.** It is not the balanced view. It is the strongest case that survives contact with
the evidence. Section 12 is the closest thing to a counter-case, and it is genuine.

---

## 1. Anchors, and the one that does not reconcile

### 1.1 Given organisational facts

| Anchor | Value |
|---|---|
| Home health revenue | ~$549M |
| Episodic (traditional Medicare) | ~$260M (47%) |
| Non-episodic (MA / commercial / Medicaid) | ~$289M (53%) |
| Field clinicians | ~3,000, of whom ~70% paid **per visit** |
| Schedulers | ~300 |
| Systems | HCHB (system of record), Commure (intake), Workday, Pulse (utilisation review) |

**A caveat that must be stated first.** In the source transcript both the 3,000-clinician and
300-scheduler figures are hedged conversational estimates from one speaker — *"what do we have like
3000 clinicians in home health **or like nurses in home health**"* and *"**if** there's 300 of them
today, like maybe there's 100 of them in the future."* Neither is a Workday extract; one is explicitly
ambiguous about scope. Both multiply through the largest lever in this case. Verify before committing.

### 1.2 Derived volumes — the working, so it can be checked

**Average payment per full 30-day period.** MedPAC reports $2,057 actual for 2024 (Ch. 8, Table 8-7).
CY2026's national standardized rate is $2,038.22 with an aggregate CY2026 impact of −1.3%. Use ~$2,030.

**LUPA drag.** MedPAC: ~7% of 30-day periods were LUPAs in 2024; 93% were full periods. A LUPA period
pays roughly $480–$700 (two SN visits at $176.96 plus the $304.37 first-visit add-on).

```
Blended payment per episodic period = 0.93 × $2,030 + 0.07 × $600 = $1,888 + $42 = $1,930
Episodic periods = $260,000,000 ÷ $1,930 = 134,700          → ~134,000/year
  Full periods  = 134,000 × 0.93 = 124,600
  LUPA periods  = 134,000 × 0.07 =   9,380
```

**Episodic visits.** MedPAC 2024: 8.4 in-person visits per full 30-day period, down 18.0% from 10.2 in
2019. Discipline split per full period: SN 4.1, PT/OT/SLP 3.8, MSW/aide 0.5.

```
Full periods:  124,600 × 8.4  = 1,046,600
LUPA periods:    9,380 × 3    =    28,100
Episodic total               ≈ 1,075,000 visits/year
  Skilled nursing ≈ 525,000  ·  Therapy ≈ 486,000  ·  MSW + aide ≈ 64,000
```

**Episodic admissions.** MedPAC: 3.1 thirty-day periods per FFS user per year; ~2.7–2.9 per stay.

```
134,000 ÷ 2.9 ≈ 46,000 episodic admissions/year
```

**Non-episodic volumes — the weakest derivation here, and I flag it as such.** No public source gives
an MA or commercial home health per-visit rate. HHS OIG states plainly that "information about what
MAOs pay to different types of providers is not available." The only bracket available is the CY2026
Medicare per-visit schedule (SN $176.96, PT $193.42, OT $194.74, SLP $210.25, MSW $283.64, aide $80.12)
against the peer-reviewed but unquantified finding that MA pays below traditional Medicare. Use a
blended $110–$180, base $140.

```
$289,000,000 ÷ $140 = 2,064,000 visits    (1.61M at $180; 2.63M at $110)
At ~20 visits per non-episodic stay: ~103,000 non-episodic admissions
```

**Totals.**

```
Total visits     ≈ 3,140,000/year   (range 2.7M – 3.7M)
Total admissions ≈   149,000/year   (46,000 episodic + 103,000 non-episodic)
Visits per clinician = 3,140,000 ÷ 3,000 = 1,047/year ≈ 22.8/week over 46 weeks
```

**Cross-check one — workload.** A full-time clinician carries a 30-point weekly expectation in the HCHB
worker profile (0.5/0.6/0.7/0.8 FTE map to 30/28/26/20/12 points). An average of 22.8 visits/week
across a workforce mixing full-time, part-time, per-diem and aide staff is 76% of a full-time load.
Plausible.

**Cross-check two — cost.** CMS's own CY2025 rulemaking estimates the cost of a 30-day period at
**$1,532.84**, stating the CY2025 base rate was "approximately 34 percent more than" that cost
(91 FR 41226). Independently, MedPAC's 2024 payment per visit of $245 × (1 − 0.212 margin) = **$193**
fully-allocated cost per visit; and $2,057 per period × (1 − 0.212) ÷ 8.4 visits = **$193**. Three
routes, one answer. The episodic arithmetic holds.

**Cross-check three — the marginal visit.** A bottom-up build from BLS OEWS May 2025 home health wages
(RN $44.99/hr mean), a BLS ECEC compensation multiplier of 1.515 for RN occupations, CMS's own claims-
measured in-home minutes (SN routine 41.54 min), assumed documentation and travel time, and 11 miles
per visit at the IRS 2026 second-half rate of 76.0¢, produces a **direct cost of ~$95 for a routine
skilled nursing visit** and ~$138 fully allocated. My marginal-cost assumption of $95 is therefore not
a guess; it lands on an independently constructed figure.

### 1.3 The anchor that does not reconcile — finance must settle this first

The existing workbook models **600 admissions per branch per year across ~80 branches = 48,000 network
admissions**, at **$1,200 contribution margin per recovered admission**. That cannot carry $549M:
$549M ÷ 48,000 = $11,437 of revenue per admission, roughly double a full traditional-Medicare stay and
about four times a non-episodic one.

The most likely explanation is that 600/branch counts **episodic admissions only** — which lands almost
exactly on my derived 46,000. If so, the workbook's growth lever is sized against **31% of the actual
admission base**, and the $7.9M headline rests on a denominator roughly a third of the real one.

Two documents inside the same initiative are threefold apart on the most basic operating denominator in
the business. This is the first thing a competent CFO will find, and it is the main reason my base case
is materially larger than the workbook's.

---

## 2. Three facts that set the frame

Before any lever: three dated, external facts that determine how this initiative should be argued.

**One — growth cannot be bought.** CMS imposed a **nationwide six-month moratorium on new Medicare
enrolment for home health agencies and hospices effective 13 May 2026**, extendable in six-month
increments, reaching certain majority ownership changes requiring re-enrolment (CMS QSO-26-11-HHA/
Hospice, 20 May 2026; Federal Register, 15 May 2026). While it holds, the company cannot add locations
and cannot acquire its way to volume. **Throughput is the only growth mechanism available.**

**Two — the base rate is under active downward pressure.** MedPAC's March 2026 Report recommends that
**Congress reduce the 2026 home health base payment rate by 7 percent for CY2027**, voted 17–0,
estimating $750M–$2B of savings in year one and $10–25B over five. On $260M of episodic revenue a 7%
cut removes **$18.2M** — more than the entire base-case net benefit of this initiative, arriving in a
single rate year. MedPAC additionally projects the freestanding FFS margin falling from 21.2% (2024) to
19% (2026), and CMS still has **$4.76 billion** of temporary behaviour adjustment to recover.

**Three — demand is arriving harder and later.** HHS OIG found the three largest MA organisations deny
post-acute placement at high rates — **65% for long-term acute care hospitals, 54% for inpatient rehab**
— frequently on the reasoning that "a lower level of care (home health services) could meet the
beneficiary's needs." When an MA plan denies IRF or LTCH placement, **the hospital still has to
discharge the patient.** Home health absorbs higher-acuity patients on compressed, short-notice
timelines. Those figures are *not* home health denial rates — they are partly the mechanism generating
home health referrals.

**The honest framing is therefore not "this initiative earns $23M."** It is: the operating environment
is removing roughly that much revenue over the same horizon, the referral stream is getting heavier and
less predictable, and this is the only lever set inside the company's control while new-site growth is
legally unavailable.

**And the strongest single argument that operations is the variable:** MedPAC's 2024 freestanding FFS
margin distribution runs from **5.7% at the 25th percentile to 31.0% at the 75th**, with the largest
volume quintile at 23.2% against 14.4% for the smallest. Payment rates are identical across that
distribution. Operating discipline is what separates those two agencies.

---

## 3. What per-visit pay does to the argument — read this before the levers

Seventy percent of clinicians are paid per visit. This is not a footnote. It **reverses the sign** on
several standard home-health scheduling arguments and **strengthens** several others. Getting it wrong
is the fastest way to lose a CFO.

### 3.1 The central asymmetry

For a **per-visit** clinician, labour cost is a straight line through the origin. Visit 1 and visit 21
cost the same. There is no capacity to "fill" and no idle cost to absorb. Margin per visit is fixed by
the spread between reimbursement and the per-visit rate, and **scheduling optimisation cannot improve
it. Better routing saves the clinician's evening, not the agency's money.**

For a **salaried** clinician the marginal cash cost of an additional visit is approximately zero up to
the capacity ceiling. A $95,000 fully-loaded RN over 230 productive days costs $103/visit at 4.0 visits
per day, $83 at 5.0 and $75 at 5.5 — a 27% swing in unit cost from a 37% swing in volume, with no
change in what anyone is paid. There, **every unfilled slot is a realised loss, not a foregone gain.**

**At ~70% per visit, only about 900 salaried-equivalent clinicians carry the classic
capacity-utilisation argument — not 3,000.** A company that has quietly shifted to per-visit pay to
control cost has also removed most of the value a scheduling optimiser can create through utilisation,
and has usually bought a turnover problem in exchange. This must be said out loud in the room, because
if a vendor pitches the classic story and someone in the audience knows the pay model, the whole case
loses credibility in one question.

### 3.2 Levers that per-visit pay strengthens

| Lever | Why |
|---|---|
| **Discipline / role match** | The PT-to-PTA and RN-to-LPN differentials are paid per visit, so a shifted visit is immediate cash. Under salary it is real only if headcount mix actually changes. |
| **Avoiding uneconomic episodic visits** | In a 4-threshold period, visits 5–15 earn **zero** incremental revenue. Under per-visit pay each one costs real cash (~$95). Under salary that cost is sunk. |
| **Growth / throughput** | Incremental capacity has **no fixed-cost step**. Clinicians already state willingness above the contractual floor — *"I don't want to do less than 40 points… the expectation is 30."* Growth requires no hiring ahead of demand. |
| **LUPA floor protection** | Recovered contribution is $1,258–$1,386; the marginal cost of the one recovering visit is one visit rate. Roughly 13:1. |
| **Scheduler and coordinator time** | Unaffected — schedulers are salaried. Pure cash. |
| **Wage-index-aware territory design** | Works on revenue, not labour cost. Completely immune to the pay model. |

### 3.3 Levers that per-visit pay weakens or kills outright

| Standard argument | What actually happens |
|---|---|
| **"Route optimisation lowers labour cost per visit"** | **Dead.** You pay the same per visit whether the clinician drove 4 miles or 24. Only mileage and the clinician's own time improve. Do not put routing in the cost column. |
| **"Idle capacity is a realised loss"** | **Dead for 70% of the workforce.** An unbooked per-visit clinician costs nothing. |
| **"A rebooked visit consumes two slots to deliver one"** | **Roughly 70% smaller than stated.** The failed attempt generates no visit and therefore no pay. The real cost is wasted travel ($10–$17) plus coordinator rework ($8–$15), not a duplicate visit. *Corrects U3 in the existing register.* |
| **"A missed visit costs the visit's revenue"** | **Overstated by roughly half on the non-episodic book.** The cost was also avoided. The loss is contribution (~$45–$75), not revenue (~$140). *Corrects the register's payer-comparison table.* |
| **"Automating evening confirmation calls saves 30 min × 3,000 clinicians of payroll"** | **Zero payroll saving** — that work was never paid. It converts into retention or, on per-visit pay, into sellable capacity. It belongs inside the growth and retention levers, not as its own bar. |

### 3.4 The compensating insight, and it is a real one

One clinician-computed figure in the corpus resolves a **$44.16 headline point rate to $30.06 per
actual hour worked — a ~32% gap**, because travel, documentation and case management sit outside the
point. That gap is simultaneously the FLSA exposure, the turnover driver, and the reason clinicians
describe points as "scammy."

**A platform that gives that time back is selling the clinician's time back to the clinician.** That is
a recruitment and retention product, priced against a **$7,499 average RN sign-on bonus** — not a
labour-cost-reduction product. Section 4's L4 is where that value lands, and it is the lever the
evidence supports best.

### 3.5 The consequence for how the platform must be built

Under a per-visit contract the incremental visit carries **positive** contribution; under PDGM it
carries **negative** contribution. A platform applying one utilisation policy across a mixed 47/53 book
systematically destroys value on one side of it. **Payer type must be a first-class field in the
scheduling model, not a reporting attribute.** That is a design requirement with a dollar consequence,
and it is the cleanest technical justification for buying rather than configuring.

---

## 4. The levers, sized

Categories are kept separate deliberately. They are not equivalent to a CFO.

- **Cost removed** — cash that stops leaving the business.
- **Revenue captured** — money already earned that is not currently collected.
- **Revenue grown** — new volume, valued at *contribution margin*, never at revenue.
- **Loss avoided** — a penalty or write-off that does not occur. Never a waterfall bar.
- **Capacity released** — hours freed. Only cash if headcount or premium spend actually changes.

---

### L1. Scheduler and coordinator administrative capacity — **cost removed**

**Mechanism.** Three named, system-deterministic sources of clerical load.

**Component A — authorisation notification noise.** HCHB generates a pending-auth workflow *every day
per patient*, plus another on any auth-screen edit. Confirmed in session at ~50/day per scheduler, with
"almost none carry an available action." The behavioural cost is worse than the time cost: bulk-clearing
becomes habit and the one actionable item goes with the rest.

```
50/day × 300 schedulers × 250 days              = 3,750,000 notifications/year
At 20 / 30 / 45 seconds each                    = 20,833 / 31,250 / 46,875 hours
÷ 1,800 productive hours per FTE                = 11.6 / 17.4 / 26.0 FTE
× 80% suppressible (notify on state change only)=  9.3 / 13.9 / 20.8 FTE
× $60,000 loaded                                = $0.56M / $0.83M / $1.25M
```

**Component B — per-discipline task duplication.** The highest-confidence system behaviour in the whole
discovery: *"you're getting 4 tasks every single time that workflow gets pushed to you. And then when
they approve the plan of care, you get it again for every single discipline. So I've got 8 tasks."*
Care-team-at-referral (DE-05) collapses it.

```
Trigger events = 149,000 admissions + ~60,000 recert/ROC/new-order = 209,000/year
Tasks removed per event (avg 2.2 disciplines, 8→2 pattern)          = 3
Tasks removed                                                       = 627,000/year
At 2 / 3 / 5 min = 20,900 / 31,350 / 52,250 hours = 11.6 / 17.4 / 29.0 FTE
× $60,000        = $0.70M / $1.04M / $1.74M
```

**Component C — everything else.** Auth chasing, readiness calls, PTO hand-keying, coverage brokering
over Teams, coordination-note handling, sticky-note tracking of pending-auth visits, missed-visit
compliance workflow. Leadership's stated target is 300 → ~100 with the air-traffic-control function
preserved.

**The honest position.** A + B is 21–46 FTE and bottom-up defensible today. The remaining ~155 FTE
implied by the 300→100 target is an aspiration, not a work study — and **there is no published
scheduler caseload benchmark anywhere in home health** against which to check it. That absence was
verified across the entire research corpus. I therefore size L1 well below the register's $12M.

| | Low | Base | High |
|---|---:|---:|---:|
| FTE released | 45 | 90 | 170 |
| **Value** | **$2.7M** | **$5.4M** | **$10.2M** |

**Confidence: Medium (0.55).** Mechanism high; magnitude unverifiable externally.
**Time to value: months 6–30**, phased with rollout. Not a month-3 lever.
**Per-visit pay: neutral.** Schedulers are salaried; this is pure cash.

---

### L2. Throughput growth — **revenue grown, at contribution**

**Mechanism.** Referral acceptance today is a manually maintained spreadsheet cross-referenced against
separately-run productivity reports: *"the PCC has to add every pending patient to that scheduling
grid, and then they keep up with the productivity, and then it tells them how many referrals they can
take."* Committed load is systematically understated because pending-auth visits sit on no calendar and
count toward no productivity measure — *"if you can't see it, you can't plan."* Branches carry 50
pending referrals unscheduled. One territory was measured at ~30 patients across a full-time RN and a
full-time LPN while the adjacent territory declined starts. Clinicians have stopped calling in for
backup work and "just have one less patient." Branches that decline to use per-diem staff, in the
session's own words, "forfeit the ability to grow."

**Contribution margin per admission.** Marginal cost is the visit rate plus payroll tax, mileage and
supplies — **not** the $193 fully-allocated figure, since branch overhead, DCS, scheduling and G&A do
not scale with the marginal visit. Use $80–$115, base $95 (validated in §1.2, cross-check three).

```
Episodic stay:      2.9 periods × $1,930          = $5,597 revenue
                    2.9 × 8.4 = 24.4 visits × $95 = $2,318 direct cost
                    Contribution                  = $3,279   (58.6%)

Non-episodic stay:  20 visits × $140              = $2,800 revenue
                    20 × $95                      = $1,900 direct cost
                    Contribution                  =   $900   (32.1%)

Blended, weighted 46,000 : 103,000:
  (46,000 × $3,279 + 103,000 × $900) ÷ 149,000    = $1,634 per admission
```

That is 36% above the workbook's $1,200 — and on the episodic book alone nearly three times it.

```
1.0% lift on 149,000 admissions = 1,490 × $1,634 = $2.44M
2.5% lift                       = 3,725 × $1,634 = $6.09M
5.0% lift                       = 7,450 × $1,634 = $12.17M
```

**Why the percentage cannot be evidenced today.** Referral turn-down rate for lack of capacity is
marked *"Available today? No"* on the organisation's own KPI sheet. It has never been measured. The
only external conversion figure available is a vendor claim from HCHB itself — referral conversion
falling from 77% (2018) to 64% (Q2 2025), with median referral-entry-to-SOC exceeding 69 hours and more
than 13 hours inside intake alone. Directional only; that is the client's own system-of-record vendor
marketing its RCM service.

| | Low | Base | High |
|---|---:|---:|---:|
| Admission lift | 1.0% | 2.5% | 5.0% |
| **Value** | **$2.4M** | **$6.1M** | **$12.0M** |

**Confidence: Medium-Low (0.45)** — high on mechanism and on the contribution arithmetic, low on the lift.
**Time to value: months 12–24.** The capacity measure must exist and be trusted first.
**Per-visit pay: strongly positive.** Supply is elastic and growth requires no hiring step.

---

### L3. Discipline and role match — **cost removed, episodic only**

**Mechanism.** *"If you're a PT, you're doing starts, recerts, reassessments, ROCs — things that a PTA
can't do. If it's a routine visit, we shouldn't be paying PTs to do routine visits. Our PTA should be
full first."* HCHB filters the assignable list by profile but does not push work down. DE-08 already
sets policy: default to the paraprofessional with **explicit opt-out**, so the change does not depend
on a leader making it.

**Substitution differentials**, derived from BLS OEWS May 2025 national mean wages with a labour burden
multiplier and stated visits-per-day productivity: **RN→LPN $31/visit (28%)**, **PT→PTA $31/visit
(30%)**, **OT→COTA $25/visit (25%)**.

```
Therapy: 486,000 episodic therapy visits × 80% routine = 389,000 eligible
         Shift 10% / 15% / 25% = 38,900 / 58,400 / 97,300
         × $31                 = $1.21M / $1.81M / $3.02M

Nursing: 525,000 episodic SN visits × 75% routine      = 394,000 eligible
         Shift 10% / 15% / 25% = 39,400 / 59,100 / 98,500
         × $31                 = $1.22M / $1.83M / $3.05M
```

**Corroboration.** MedPAC names LPN and therapy-assistant substitution as a leading reason cost per
30-day period rose only 0.2% in 2024 despite rising wages. Independent modelling in the corpus puts
combined discipline-mix improvement at **2–4 margin points**, which on $260M episodic would be
$5.2M–$10.4M — above my range. I deliberately use the visit-level derivation because it is checkable.

**Why episodic only.** Under a per-visit non-episodic contract, substituting an LPN for an RN cuts the
*revenue* as well as the cost, and the net depends on a contracted rate differential that is not
published for any payer. Excluded until contracts are read. (Some payers already *mandate* LPN
substitution, so part of the shift is forced regardless.)

**Two hard ceilings.** PTAs and COTAs may not perform the initial evaluation, establish or modify the
plan of care, or perform the discharge assessment. And the comprehensive assessment — the single most
payment-consequential visit in the period, since case-mix group, functional level and comorbidity
adjustment all flow from it — **must** be completed by a registered nurse (42 CFR 484.55(b)). Push
substitution too far and you create a therapist and RN bottleneck at exactly the evaluation points that
gate admissions. Separately, the session flagged unprompted that LPNs "are getting harder and harder to
hire" and that some markets have no workable paraprofessional ratio. **Check market by market before
switching the default on.**

| | Low | Base | High |
|---|---:|---:|---:|
| **Value** | **$2.4M** | **$3.6M** | **$6.1M** |

**Confidence: Medium-High (0.65)** — the mechanism is an agreed policy default and the wage ratios are
BLS-primary. The risk is paraprofessional supply, not logic.
**Time to value: months 6–12.**
**Per-visit pay: strongly positive.** The differential is paid per visit and lands as cash immediately.
**Second-order:** the freed PT and RN capacity is the supply side of L2. Counted once, in L2.

---

### L4. Clinician retention through schedule stability — **loss avoided**

**This lever has the best single citation in the entire evidence base, and the existing register
understates it badly.**

**Mechanism, with a measured effect size.** Bergman, Song, David, Spetz and Candon (*Medical Care
Research and Review*, 2021; n = 3,716 nurses, 30+ states, payroll and visit-level data from a top-five
US home health organisation, Jan 2016–Mar 2019) operationalised **schedule volatility as the
coefficient of variation of daily visit count over the prior 28 days** and found:

- **Full-time RNs at the 75th percentile of volatility were 16% more likely to quit** than average;
  full-time LPNs **34% more likely**.
- **Moving a full-time RN from the 75th to the 25th percentile of volatility cut annual quit
  probability by 9.2 percentage points.**
- The relationship **disappeared entirely for part-time nurses** — the mechanism is income instability
  for people dependent on the job.

Two things make this exceptional. First, the independent variable is **directly computable from data
the platform already holds and directly manipulable by the product** — this is not a soft
"engagement" claim. Second, the mechanism is exactly the per-visit pay problem: under per-visit pay the
branch's scheduling failures cut the clinician's income directly. The clearest case in the discovery is
first-hand — a clinician moved two visits to her PTA to make room for a start of care, nobody confirmed
the patient was home, the patient was still in hospital, and *"she had half a day of no productivity…
her income is affected because the branch didn't confirm that patient was home."*

**Turnover baseline.** Home care/home health **RN turnover is 25.46%** (HCS *Home Care Salary &
Benefits Report* 2025, n = 1,111 agencies, 52,200+ employees), against 17.6% hospital RN turnover. The
peer-reviewed payroll data puts full-time RN voluntary separation at 27.14% and full-time LPN at
20.15%. **The workbook's implied 13.3% is roughly half the published rate.** *(Do not use the 75%
home-care caregiver turnover figure that circulates — it measures personal-care aides, not skilled
clinicians, and using it here would be a misrepresentation.)*

**Replacement cost.** No home-health-specific figure exists in the published literature; every credible
dollar figure is hospital-derived. The defensible construction is the peer-reviewed systematic review's
**~1.3× annual salary**. A home health RN at the BLS mean of $44.99/hr is ~$93,600 salary → ~$121,600
replacement. I discount that substantially for home health's shorter onboarding and lighter benefit
load and use **$60k / $85k / $120k**.

```
Full-time nurses ≈ 3,000 × 55% FT × 60% nursing ≈ 990
Reached with a meaningful volatility reduction: 20% / 33% / 50% = 198 / 327 / 495
× 9.2 pp quit-probability reduction (scaled 80% / 100% / 120% of the study effect)
= 15 / 30 / 55 avoided departures
× $60k / $85k / $120k = $0.90M / $2.55M / $6.60M
```

**Segment the claim, or it breaks.** The effect is null for part-time nurses. Do not sell schedule
stabilisation to a per-diem pool. And the corroborating finding matters: home health agencies with good
work environments have **lower nurse burnout and better patient outcomes** — lower acute
hospitalisation, higher discharge to community. That is the bridge from the labour case to L11.

| | Low | Base | High |
|---|---:|---:|---:|
| **Value** | **$0.9M** | **$2.6M** | **$6.0M** |

**Confidence: Medium (0.45)** — up from the register's treatment, because the effect size is
peer-reviewed, payroll-grade, in the right setting, and the driver is a variable the product controls.
Attribution to the platform specifically is still the soft part.
**Time to value: months 18–36.**

---

### L5. LUPA leakage, clinically gated — **revenue captured**

**Mechanism.** A 30-day period falling below its case-mix group's visit threshold (2–5 visits in
CY2026) reprices entirely to national per-visit amounts. The recovery window is days wide, not hours —
HCHB already alerts the scheduler when a missed visit would create a LUPA, and the DCS is *supposed to*
run a daily LUPA report from Pulse, which the session confirms is inconsistently done. Replacing a
discretionary daily report with an event-driven alert is the whole intervention.

```
Episodic periods = 134,000  ×  7% national LUPA rate (MedPAC 2024) = 9,380 LUPA periods/year

Contribution destroyed per LUPA (CY2026 rates):
  Initial period      $2,038.22 − $674.75 = $1,363 lost, less ~$105 cost avoided = $1,258
  Subsequent period   $2,038.22 − $547.34 = $1,491 lost, less ~$105 cost avoided = $1,386
Gross annual exposure ≈ 9,380 × $1,320 = $12.4M
```

**Recoverable share.** McBee's analysis of CMS PDGM claims finds **81.12% of subsequent-period LUPAs
were exactly one visit short**. Weighting for the ~60% of LUPAs that are subsequent-period gives ~71%
one-short overall — roughly **6,660 periods a year one visit away from full payment**. The share that
was operationally caused (a miss, a reschedule past the period boundary, an authorisation hold) **and**
clinically indicated has never been measured anywhere. Use 15% / 25% / 40%.

```
6,660 × 15% = 999   × $1,258 = $1.26M
6,660 × 25% = 1,665 × $1,320 = $2.20M
6,660 × 40% = 2,664 × $1,386 = $3.69M
```

**The gate is absolute, and it is a compliance boundary rather than a preference.** OIG report
A-09-18-03031 found **25 of 120 sampled claims (21%) just above the LUPA threshold non-compliant**,
extrapolated to $191.8M of national overpayment, with CMS concurring that MACs should target claims
with visits slightly above the threshold. **No visit is ever added to clear a floor.** Defensible
product behaviour: flag at admission that an *ordered* plan of care sits at or below threshold so the
practitioner can review it; and flag that a missed visit has put a period below threshold so it can be
**rescheduled**. Recommending "add one visit" is an enforcement exposure.

**The dual-jeopardy point worth carrying.** A period that drops to LUPA is simultaneously a revenue
event *and* an under-dosed functional-improvement episode feeding 40% of the HHVBP score. One missed
visit can do both. A capacity optimiser that is LUPA-blind is not neutral — it is dangerous.

| | Low | Base | High |
|---|---:|---:|---:|
| **Value** | **$1.3M** | **$2.2M** | **$3.7M** |

**Confidence: Medium (0.60)** — exposure is primary-sourced and large; the recoverable share is soft.
**Time to value: months 3–9.** The fastest real lever; most of the data already sits in HCHB.
**Per-visit pay: positive.** $1,320 of contribution recovered against ~$95 of marginal cost.

---

### L6. Payer-aware referral prioritisation under scarcity — **revenue grown / mix**

**Mechanism, and it is new to this analysis.** MedPAC's 2024 figures give freestanding HHAs a **21.2%
FFS Medicare margin against a 5.0% all-payer margin**. At a 47/53 split that implies the non-episodic
book runs at or below break-even on a fully-allocated basis. On a contribution basis the gap is $3,279
(episodic) against $900 (non-episodic) per admission — a **3.6× difference** that the branch cannot see
at the moment of the accept/decline decision. When a branch is at capacity, every non-episodic
admission taken in preference to an episodic one destroys ~$2,379 of contribution, invisibly.

```
Contribution swing per re-prioritised admission = $3,279 − $900 = $2,379
0.33% / 1.0% / 2.0% of 149,000 admissions       = 490 / 1,490 / 2,980
Gross value                                     = $1.17M / $3.54M / $7.09M
Less 40% haircut for overlap with L2 (both draw on the same scarce capacity)
Value                                           = $0.70M / $2.12M / $4.25M
```

**The binding constraint, stated honestly.** Episodic referral supply is shrinking: FFS home health
users fell from 3.3M (2019) to 2.7M (2024) while MA passed 55% of Medicare enrolment. You cannot
prioritise into a pool that is not there. The lever is real where episodic referrals are being turned
away for capacity — which the discovery says happens — and worth nothing where they are not.

**Guardrail.** This is about *where growth recruits referrals and how territory is designed*, not about
declining individual patients by payer. Any implementation that turns into payer-based patient
selection is both an access problem and a regulatory one.

| | Low | Base | High |
|---|---:|---:|---:|
| **Value** | **$0.7M** | **$2.1M** | **$4.3M** |

**Confidence: Low-Medium (0.35).** **Time to value: months 12–24.**

---

### L7. Episodic over-delivery and duplicate visits — **cost removed**

**Mechanism.** Above the LUPA threshold and below the outlier threshold, an episodic period pays the
same whether you deliver 5 visits or 12. Modelled on verified CY2026 rates: in a period with a 4-visit
threshold, **visits 5 through 15 generate exactly zero incremental revenue** — eleven visits, roughly
$1,100 of direct cost, no payment. One additional nursing visit per period reduces period operating
profit by **28%** ($387 → $278). The outlier threshold is not reached until ~15.8 nursing visits.

**Named waste patterns from the corpus, all schedulable:** PT and OT seeing the patient the same day
with overlapping goals; nursing plotted heavily in month one when the patient's goals are functional;
and the characteristic PDGM failure where the first 30-day period is heavily scheduled against a 60-day
comprehensive assessment while the second becomes a LUPA.

```
0.1 / 0.2 / 0.3 avoidable visits per episodic period
134,000 × those rates = 13,400 / 26,800 / 40,200 visits
× $95 marginal cost   = $1.27M / $2.55M / $3.82M
```

**Why this is capped hard, and why the register's $24M framing should not be used.** Industry visits per
period have **already** fallen 18% (10.2 → 8.4) since 2019, and MedPAC's causal analysis finds PDGM cut
visits per stay by 2.9 (15.9 with PDGM against 18.8 without) — while **discharge to community got
worse** (82.8% against 85.2%, statistically significant). Under-dosing is a live risk, and
under-delivery against an ordered frequency is a condition-level survey exposure under 42 CFR 484.60
*and* a false-claims exposure. Peer-reviewed evidence is explicit that intensity is not monotonic:
1–1.99 nursing visits per week outperformed higher frequencies for rehospitalisation, and lower
intensity was associated with *better* ADL improvement. **The defensible lever is placement and
duplication, never volume.**

| | Low | Base | High |
|---|---:|---:|---:|
| **Value** | **$1.3M** | **$2.6M** | **$4.0M** |

**Confidence: Low (0.30)** — mechanism arithmetically certain, magnitude a judgement, guardrails tight.
**Time to value: months 12–18.**
**Per-visit pay: strongly positive** — this is the lever per-visit pay most improves.

---

### L8. Authorisation operations cost — **cost removed**

**Mechanism, and this one has genuine primary cost data.** The 2024 CAQH Index measures the **provider-
side cost of a single medical prior authorisation at $12.88 manual, $8.93 by payer portal, $5.38 fully
electronic**, and the **time at 24 minutes by phone/fax/email and 16 minutes by portal** — the highest
time of any administrative transaction measured, and the only major HIPAA transaction where the portal,
not the standard, is the dominant channel. Manual provider cost rose 17% year over year while
electronic cost fell; the gap is widening.

**Where the addressable money actually is.** Full electronic adoption only halves provider cost
($12.88 → $5.38), because clinical judgement and documentation assembly do not go away — and the
electronic path is gated on FHIR APIs not due until 1 January 2027. What the platform can do **today,
with no payer integration at all**, is the two highest-value automations: **decrement the authorisation
counter, and compute the reauthorisation trigger date.** Neither needs payer cooperation.

**The single most quantifiable operational fact in reauthorisation:** for BCBS plans, *"if ALL clinicals
are not available… the 14 days can start over again when the additional clinicals are uploaded."* An
incomplete packet does not delay the decision by the time taken to complete it — **it can reset the
entire review clock.** First-pass packet completeness is therefore the highest-leverage auth-ops
intervention, and it is a workflow problem, not an integration problem.

```
Non-episodic admissions ≈ 103,000, at 3–5 authorisation transactions per episode
(Anthem/Carelon standardised 30-day review periods; per-discipline vectors; recert cycles)
= 310,000 – 515,000 transactions/year, base 400,000
× $2 / $3.50 / $6 of avoided rework, resubmission and clock-restart per transaction
= $0.80M / $1.40M / $2.40M
```

**Why the whitespace argument is strong.** Across the major home health EMRs, authorisation is modelled
as "a record to be entered and a warning to be shown — not as a constraint on scheduling." The
best-documented vendor shows a warning symbol when scheduled tasks exceed authorised visits and **does
not prevent scheduling**; attaching visits to authorisations is a manual act; there is no documented
automatic decrement. **For HCHB specifically, the published material is marketing-level only, and HCHB
sells Authorizations as a managed service with its own staff resolving pending authorisations.** A
platform vendor selling humans to operate its own authorisation module is a strong indicator of where
the software's boundary sits. Nothing in the published documentation of any major vendor models an
authorisation as a **consumable resource that scheduling must reserve against.** That is the gap.

| | Low | Base | High |
|---|---:|---:|---:|
| **Value** | **$0.8M** | **$1.4M** | **$2.4M** |

**Confidence: Medium (0.50)** — CAQH unit costs are primary and current; the transaction count is derived.
**Time to value: months 6–18.** Partly overlaps L1; the auth-team side is counted here, the scheduler
side in L1.

---

### L9. Non-billable visits delivered against pending authorisation — **revenue captured**

**Mechanism, confirmed as current practice in the client's own words:** *"I know this insurance will not
go back and pay us for the auth that we put in as pending, but we have to go see this patient, so we'll
just make it a non-billable visit and go see the patient anyway."* The branch is structurally forced:
42 CFR 484.55 requires the initial assessment within 48 hours of referral, faster than many plans'
authorisation turnaround. Pending-auth allowances vary by payer at 1, 3, 5 and 10 visits; published
backdating windows run **0 to 5 days** (Anthem Ohio 2 days, Carelon 5 business days, Optum none after
day 14, Montana Medicaid none at all). Texas Medicaid goes further and *requires* delivery from the SOC
date during the authorisation process.

```
Non-episodic visits ≈ 2,064,000; admissions ≈ 103,000 at ~3 visits delivered pending auth
= 309,000 at-risk visits/year
Share falling outside the backdating window and written off: 3% / 5% / 8%
= 9,270 / 15,450 / 24,720 visits × $140 = $1.30M / $2.16M / $3.46M
Less 40% for the shrinking managed pool (below)
= $0.78M / $1.30M / $2.08M
```

**Two headwinds that make this smaller than it was a year ago, and I apply them.** UnitedHealthcare
eliminated MA home health prior authorisation and concurrent review across **36 states and DC effective
1 April 2025** (partially re-adding three shift-nursing codes in February 2026) — the single largest
structural change in home health authorisation in recent years. And **CMS-0057-F cut the MA standard
prior-authorisation decision window from 14 to 7 calendar days effective 1 January 2026**, with the
federal Medicaid MCO ceiling halving on the same date. The at-risk pool is shrinking under its own
momentum. Real, but not growing.

**A named but deliberately unvalued companion.** Across MA overall, **11.5% of denied requests are
appealed and 80.7% of those are overturned** (2024 CMS Part C data; 67% overturn in 2025). Providers
give three reasons for not appealing: 59% do not believe it will succeed, 52% lack staff or time, 49%
say care cannot wait. A high overturn rate against a low appeal rate is a measurable, unexploited
revenue position bounded by the cost of appealing. **It cannot be sized here**, because no
home-health-specific denial rate exists in any primary source, and the 54–65% post-acute denial rates
that circulate are *facility* denials, not home health. Naming it unvalued is more useful than guessing.

| | Low | Base | High |
|---|---:|---:|---:|
| **Value** | **$0.8M** | **$1.3M** | **$2.1M** |

**Confidence: Medium-Low (0.45)** — practice confirmed, volume never counted by anyone.
**Time to value: months 6–12.** Agency-side only; no payer integration required.

---

### L10. Premium labour displaced into unused salaried capacity — **cost removed**

**Mechanism, correctly stated.** The value is **not** the wage differential between a contractor and an
employee. It is that moving a visit out of the high-marginal-cost pool (contract, PRN, overtime) into
genuinely unused salaried capacity captures the **entire contract rate per visit** as contribution. The
size of the prize is (contract rate per visit) × (visits moved).

Contract clinicians are guaranteed 40 hours and "paid no matter what," and the encoded fill order is
contractors → full-time → part-time → per diem, with the explicit counterweight that filling a
contractor by taking visits from full-time staff means the contractor was never needed. Per-diem
availability "fluctuates weekly and lives nowhere in any system." Call-out recovery has **no established
process**: everyone stops, charts are opened one at a time, clinicians are called and begged, and if
nothing works the DCS goes and sees the patients.

**Sizing, and the ceiling that caps it.** No baseline exists — the question was asked directly in
session (*"I know we used a decent amount of contract labor. Do we have… a lot?"*) and never answered.
No published home health staffing-agency bill rates exist anywhere. The workbook assumes a $120,000
premium pool per branch per year; at ~80 branches that is $9.6M, or ~4% of field clinical labour, at
the low end of the 3–8% industry band.

```
$9.6M premium pool × 15% / 25% / 40% conversion to planned coverage = $1.44M / $2.40M / $3.84M
Less ~50%: overtime is not a meaningful component for the 70% paid per visit
= $0.72M / $1.20M / $1.92M
Plus the per-diem opportunity — "your biggest weapon against capacity," currently unmanaged,
and declined outright by some branches
```

**The per-visit pay constraint that caps this lever.** The displacement target is *unused salaried
capacity*, and only ~30% of the workforce is salaried. Roughly 900 clinicians carry this lever, not
3,000. That is why I keep it mid-table despite an attractive mechanism.

| | Low | Base | High |
|---|---:|---:|---:|
| **Value** | **$0.7M** | **$1.9M** | **$3.5M** |

**Confidence: Low (0.30)** — no baseline, no published contract rates.
**Time to value: months 12–24.**
**Per-visit pay: materially weakens this lever.** Per-visit clinicians earn no overtime, so half the
classic argument does not exist here.

---

### L11. Quality-linked revenue (HHVBP) — **loss avoided / revenue at risk**

**Get the measure set right, because it changed.** Acute Care Hospitalization and ED Use Without
Hospitalization were **retired from HHVBP effective the CY2025 performance year**. ED use is no longer
scored at all. Any pitch built on "we lower your ACH and ED-use scores" describes a measure set that no
longer exists. The CY2026 set and weights (larger-volume cohort):

| Category | Measures | Weight |
|---|---|---:|
| OASIS | Discharge Function Score 15% · Oral Medications 11% · Dyspnea 7% · Bathing 3.5% · Upper Body Dressing 1.75% · Lower Body Dressing 1.75% | **40%** |
| Claims | Within-Stay Potentially Preventable Hospitalisation 15% · Discharge to Community–PAC 15% · MSPB–PAC 10% | **40%** |
| HHCAHPS | Overall Rating 10% · Willingness to Recommend 10% | **20%** |

Adjustment range is **−5% to +5%** of Medicare FFS payments, applied at the **CCN level, not the branch
level** — which for a multi-branch operator means branch scheduling behaviour aggregates into one score.
The lag is always two years: CY2026 performance drives CY2028 payment.

**Why scheduling moves it — four direct, evidenced paths.**

1. *Timely Initiation of Care* (CBE #0526) is a CMS Home Health QRP measure for CY2026. First-visit
   timing is a regulated metric, not an operating preference.
2. **PPH (15%)** counts hospitalisations during the stay. Delayed initiation raises them: patients not
   started within 2 days of discharge had **12% higher odds** of 30-day rehospitalisation or ED visit
   (OR 1.12, CI 1.06–1.18; Topaz et al., JAMDA 2022, across 16,251 delays representing **34% of
   episodes**), rising to a **fourfold** difference at 8–14 days. Sepsis survivors seen within 2 days
   with a further week-1 nursing visit had 30-day rehospitalisation **7 percentage points lower — a 41%
   relative reduction**. Front-loading cut 60-day rehospitalisation from 39.4% to 15.8% in heart-failure
   patients (Rogers 2007) — **and did nothing for diabetic patients.**
3. **OASIS functional measures (40%)** are dose-responsive and computed from paired start and end
   assessments. Visit compression is directly eroding that input: PT/OT/SLP visits per full period fell
   **21.5%** between 2019 and 2024.
4. **HHCAHPS (20%)**: the revised survey retains a question on **whether staff kept the patient informed
   about when they would arrive** — a literal scheduling-reliability item inside the scored weight.

**Sizing.** The payment effect cannot be honestly derived. HHVBP is a relative tournament: the payment
adjustment runs through a linear exchange function whose ratio in CMS's own worked example was 1.931,
meaning an agency needed a TPS near 52 just to break even. **Improving in absolute terms while the
cohort improves faster still produces a negative adjustment.** Compassus's cohort position is unknown.
Use the house convention on in-scope episodic revenue.

```
$260M × 0.25% / 0.5% / 1.0% = $0.65M / $1.30M / $2.60M
(Theoretical maximum swing: $260M × 5% = $13.0M)
```

**The framing that lands in the room.** On this arithmetic the full HHVBP band and one visit per period
are **the same size**. The entire margin available from removing one visit per period can be erased by
a single maximum-downside HHVBP adjustment. That is the strongest available argument for building a
**timing-based** product rather than a volume-based one.

| | Low | Base | High |
|---|---:|---:|---:|
| **Value** | **$0.7M** | **$1.3M** | **$2.6M** |

**Confidence: Low-Medium (0.35)** on magnitude; **High** on mechanism and clinical evidence.
**Time to value: months 24–36.** The two-year performance-to-payment lag cannot be compressed.

---

### L12. Clinical-leader coordination time — **capacity released** (only partly cash)

**Mechanism.** *"Every afternoon, the DCS, so all the clinical managers, the schedulers, all huddle
together and review all the starts for the next day… the huddle can last up to an hour every single
day, if not more."* The session's own estimate with a shared capacity view: **15 minutes**. The huddle
is the manual compensation for the absence of a shared capacity view.

```
Participants 4 / 6 / 8 × duration reduction 25 / 40 / 45 minutes
= 1.67 / 4.00 / 6.00 person-hours per branch per day
× 80 branches × 250 days = 33,400 / 80,000 / 120,000 hours = 18.6 / 44.4 / 66.7 FTE-equivalents
```

**Why I do not book that as a saving.** Reclaimed manager hours are not cash unless headcount changes.
The corpus is explicit that the retained value of DCS oversight is utilisation management — *"I have
the time to review the reports to do the follow-up necessary instead of spending all day pushing
workflow."* So: recognise ~44 FTE-equivalents released, book only the ~30% that converts to cash or
into L7's utilisation work. Schedulers in the huddle are already in L1 and excluded here.

| | Low | Base | High |
|---|---:|---:|---:|
| Released capacity | 19 FTE-eq | 44 FTE-eq | 67 FTE-eq |
| **Cash-equivalent booked** | **$0.3M** | **$0.7M** | **$1.1M** |

**Confidence: Medium-Low (0.40).** **Time to value: months 6–18.**

---

### L13. Late-NOA and NOMNC penalty avoidance — **loss avoided**

**Mechanism — the only cleanly quantified timeliness-to-dollars chain in the entire corpus.** The Notice
of Admission must be submitted to *and accepted by* the MAC **within 5 calendar days** of the SOC date
(42 CFR 484.205(j)(1)). Late filing triggers a **1/30th reduction of the wage- and case-mix-adjusted
period payment for every day** from SOC to filing (42 CFR 484.205(j)(3)) — about **$68 per day** at the
CY2026 base rate. Worse, **no LUPA payments at all are made for visits in the late-NOA window**, and
non-covered days are provider liability that may not be billed to the beneficiary. The NOA cannot be
filed until the first visit has been made, so **the first visit gates the billing clock.**

Separately, failure to deliver a valid NOMNC on termination of services can make the provider
**financially liable for continued services until two days after a valid notice is received**. The
last-visit date and the NOMNC delivery date are coupled, and neither is visible in a schedule today.

```
46,000 episodic admissions × 2% / 4% / 6% late × 3 / 4 / 5 days average × $68/day
= $188k / $500k / $938k
```

| | Low | Base | High |
|---|---:|---:|---:|
| **Value** | **$0.2M** | **$0.5M** | **$0.9M** |

**Confidence: Medium-High (0.60)** — the rule and rate are federal and exact; only the late-filing rate
is unmeasured. **Time to value: months 3–9.**

---

### L14. Wage-index-aware territory and growth targeting — **revenue grown**

**Mechanism, and it is the only lever completely immune to the pay model.** The home health wage index
applies to the **beneficiary's site of service, not the agency's location**, and the payment multiplier
is `0.749 × WI + 0.251` (labour-related share 74.9%). Two identical skilled nursing visits by the same
clinician on the same day can carry payment differing by **15–30% purely on the patient's county**.

| Area wage index | Payment multiplier | Payment vs national |
|---:|---:|---:|
| 0.80 | 0.850 | −15.0% |
| 0.90 | 0.925 | −7.5% |
| 1.00 | 1.000 | 0% |
| 1.20 | 1.150 | +15.0% |
| 1.40 | 1.300 | +30.0% |

No scheduling board surfaces this today. The initiative's own "data-driven territory" workstream — a
live census and referral heat map by zip and discipline, serving scheduling and growth together — is
exactly the vehicle for it.

```
Episodic periods 134,000 × 2% / 5% of volume shifted toward higher-WI parts of a territory
× $2,030 per period × ~8% / ~12% average multiplier gain
= $0.44M / $1.63M    (low case: 1% and 6% → $0.16M)
```

**Guardrail, and it is not optional.** This may inform **where growth recruits referrals and how
territories are drawn**. It may never inform which individual patients are accepted. Any implementation
that becomes payer- or geography-based patient selection is an access problem before it is a compliance
one.

| | Low | Base | High |
|---|---:|---:|---:|
| **Value** | **$0.2M** | **$0.6M** | **$1.6M** |

**Confidence: Low (0.30)** on magnitude; **High** on the mechanism, which is arithmetic on the payment
formula. **Time to value: months 12–24.**

---

### L15. Workday ↔ HCHB PTO integration — **loss avoided, near-zero cost**

**Mechanism.** The integration **exists and is switched off**. PTO is hand-keyed into HCHB by scheduling
staff, and DCS leadership runs weekly cross-approval meetings specifically to prevent five of seven
nurses being approved off the same day.

```
Manual entry removal: 1 / 2 / 3 FTE × $60,000 = $60k / $120k / $180k
Plus the avoided capacity failures, unquantified
```

| | Low | Base | High |
|---|---:|---:|---:|
| **Value** | **$0.06M** | **$0.12M** | **$0.18M** |

**Confidence: High (0.90).** Trivially small in dollars — and it belongs in the case anyway, because it
is free, immediate, and demonstrates the thesis to a sceptical steering committee before a licence is
bought. **Time to value: months 1–3.**

---

### Two enablers with no bar of their own

**Surfacing payer rules at plan-of-care creation.** Not sized separately because its value is realised
inside L5, L7 and L9, and double counting would be dishonest. But it is the most important design point
in the initiative and the cheapest. The authorisation team **already writes payer specifics into a
structured coordination note at verification**, days before anyone writes a plan of care. Nobody reads
it at the moment it would matter. Frequency is written to clinical need with payer limits invisible:
*"UHC was never going to give you more auth. We're not creating our plans of care based on the
insurance… we create a plan of care for twice weekly for eight weeks, and then we get mad by week three
that we have no more auth."* The data exists, is already captured, and is already structured. It is
also a **patient-care** win, because abrupt discharges happen precisely because nobody planned for the
real visit budget.

**Publishing weighted and unweighted productivity side by side.** The published national figure of ~4.5
visits per day for skilled nursing is **unweighted**. Agency internal targets of 5–6/day are usually
**weighted**, with an admission counting 2–3. The two are not comparable, and conflating them is exactly
how a branch tells itself it is at benchmark while its clinicians are structurally overloaded. CMS's own
claims data supports the weighting: a start of care takes **1.72×** the in-home minutes of a routine
nursing visit (71.45 against 41.54), and a therapy evaluation **1.62×** — and those are in-home minutes
only, excluding travel and out-of-home documentation, so the true ratio is higher. The field's
improvised 2.0–2.5 point weights converged, without data, on approximately the right answer. Publishing
both numbers from the branch's own visit mix costs nothing and is pure Phase-1 visualisation, exactly
what DE-03 scopes.

---

## 5. Ranking — by size × confidence, not by size

| Rank | Lever | Type | Base $M | Conf. | Score | Time to value |
|---:|---|---|---:|---:|---:|---|
| **1** | **L1 Scheduler & coordinator admin capacity** | Cost removed | 5.4 | 0.55 | **2.97** | M6–30 |
| **2** | **L2 Throughput growth** | Revenue grown | 6.1 | 0.45 | **2.75** | M12–24 |
| **3** | **L3 Discipline & role match** | Cost removed | 3.6 | 0.65 | **2.34** | M6–12 |
| 4 | L5 LUPA leakage, clinically gated | Revenue captured | 2.2 | 0.60 | 1.32 | M3–9 |
| 5 | L4 Retention via schedule stability | Loss avoided | 2.6 | 0.45 | 1.17 | M18–36 |
| 6 | L7 Episodic over-delivery | Cost removed | 2.6 | 0.30 | 0.78 | M12–18 |
| 7 | L6 Payer-aware prioritisation | Revenue grown | 2.1 | 0.35 | 0.74 | M12–24 |
| 8 | L8 Authorisation operations cost | Cost removed | 1.4 | 0.50 | 0.70 | M6–18 |
| 9 | L9 Non-billable pending-auth visits | Revenue captured | 1.3 | 0.45 | 0.59 | M6–12 |
| 10 | L10 Premium labour displaced | Cost removed | 1.9 | 0.30 | 0.57 | M12–24 |
| 11 | L11 HHVBP / quality-linked | Loss avoided | 1.3 | 0.35 | 0.46 | M24–36 |
| 12 | L13 Late-NOA / NOMNC | Loss avoided | 0.5 | 0.60 | 0.30 | M3–9 |
| 13 | L12 Clinical-leader coordination | Capacity released | 0.7 | 0.40 | 0.28 | M6–18 |
| 14 | L14 Wage-index territory targeting | Revenue grown | 0.6 | 0.30 | 0.18 | M12–24 |
| 15 | L15 Workday PTO sync | Loss avoided | 0.12 | 0.90 | 0.11 | M1–3 |

**Read the ranking, not the dollar column.** Three consequences of ranking this way:

- **L7 (episodic over-delivery) drops from fifth by size to sixth by score**, and it should drop further
  in the room. It sits closest to the compliance guardrails and it is the lever most likely to be argued
  down. It is in the case; it should never lead the case.
- **L4 (retention) rises from a footnote in the existing register to fifth**, because it acquired a
  peer-reviewed, payroll-grade effect size with a directly computable and directly manipulable driver.
  It is the best-evidenced causal claim in the entire document.
- **L3 (discipline match) is third on both axes.** It is the most defensible lever in the set: an agreed
  policy decision already taken, BLS-primary wage ratios, and it lands inside a year.

### By category — because these are not equivalent to a CFO

| Category | Low $M | Base $M | High $M |
|---|---:|---:|---:|
| **Cost removed** (L1, L3, L7, L8, L10, L12) | 8.2 | 15.6 | 27.3 |
| **Revenue captured** (L5, L9) | 2.1 | 3.5 | 5.8 |
| **Revenue grown, at contribution** (L2, L6, L14) | 3.3 | 8.8 | 17.9 |
| **Loss avoided** (L4, L11, L13, L15) | 1.9 | 4.5 | 9.7 |
| **Gross** | **15.5** | **32.4** | **60.7** |

**Just under half the base case is cost removed.** That matters, because it is the half a CFO can book
without believing anything about demand, adoption or payer behaviour.

---

## 6. Costs

| Item | Low $M | Base $M | High $M |
|---|---:|---:|---:|
| Platform licence (3,000 clinicians at $15–$40/user/month) | 0.54 | 0.90 | 1.44 |
| Implementation and integration, amortised over 3 years (HCHB, Commure, Workday) | 0.70 | 1.10 | 1.70 |
| Payer rules library build and upkeep (2–4 FTE) | 0.16 | 0.24 | 0.32 |
| Capacity steward and analyst roles (10–20 FTE) | 0.95 | 1.40 | 1.90 |
| Change management and training (tapering after rollout) | 0.30 | 0.50 | 1.00 |
| **Annual steady-state run cost** | **2.65** | **4.14** | **6.36** |

**One cost line that is really an asset.** The payer rules library is contract-level data that nobody
publishes — not CMS, not the plans. It must be captured per contract, per branch, at implementation.
That is a genuine onboarding cost and a durable competitive asset: an instrumented platform would hold
the first real dataset on home health authorisation turnaround and denial behaviour, which does not
exist anywhere today in any published form.

---

## 7. Net benefit — low, base, high

These are **scenarios**, not arithmetic sums of per-lever extremes. Summing lows across levers
understates the downside, because it assumes every lever at least partly lands. A bad outcome is one
where several land at zero.

### Low — adoption is partial; the programme buys the measurement and little else

Rollout stalls after pilot plus roughly 30% of branches. The prior failure mode repeats in tenured
offices. The scheduler reduction stops at the bottom-up-defensible 45 FTE. Growth lands at 1% and only
where the tool is live. Over-delivery, mix prioritisation, premium labour, wage-index targeting and
HHVBP are not realised inside the window.

| Lever | $M |
|---|---:|
| L1 Scheduler capacity (45 FTE) | 2.7 |
| L2 Growth (1%, 30% of estate) | 0.7 |
| L3 Discipline match (supply-constrained) | 1.2 |
| L4 Retention (partial) | 0.5 |
| L5 LUPA | 1.3 |
| L8 Authorisation operations | 0.5 |
| L9 Non-billable | 0.5 |
| L12 Clinical-leader (cash share) | 0.3 |
| L13 Late-NOA | 0.2 |
| L15 PTO sync | 0.1 |
| Gross | 8.0 |
| Less attribution haircut (15%) | (1.2) |
| Less run cost | (5.6) |
| **Net** | **+1.2** |

### Base — full rollout, good adoption in roughly 70% of branches by year 3

Gross $32.4M, less a 15% attribution haircut for value achievable through HCHB configuration and policy
alone — turning off DCS order approval (an HCHB toggle, not a Medicare requirement), enabling Shift
Finder and visit dispatching (both already in the product and switched off), and activating the Workday
interface (already built and switched off) — less run cost.

    $32.4M − $4.9M attribution − $4.1M run cost = $23.4M

### High — full adoption, the scheduler target largely realised, growth at 4–5%

Gross $60.7M, less a combined 28% haircut for attribution **and correlation** — L2, L3, L6 and L14 all
draw on the same freed capacity pool and cannot all be maximised simultaneously — less run cost.

    $60.7M − $17.0M haircut − $2.7M run cost = $41.0M

### The range

| | Low | Base | High |
|---|---:|---:|---:|
| **Annual steady-state net benefit** | **~$1M** | **~$23M** | **~$41M** |
| As % of $549M revenue | 0.2% | 4.2% | 7.5% |

**Steady state means year 3.** Year 1 realises the fast levers only — L15, L13, L5 and the notification
half of L1 — roughly **$3.6M gross against most of the implementation cost**. The initiative is
cash-negative in year 1 in every scenario, and the case should say so before someone else does.

**The low case is the most useful number in this section.** It says the downside is bounded at roughly
break-even: the programme pays for itself, buys the measurement infrastructure the organisation's own
KPI sheet says does not exist today, and captures the compliance levers. That is a materially easier
thing to approve than a $23M promise.

### What drives the spread — in order of contribution

1. **Depth of the scheduler reduction ($2.7M–$10.2M swing).** Nothing external can validate the 300→100
   target; **no published scheduler caseload benchmark exists in home health**, an absence verified
   across the whole research corpus. This is the single largest unresolved input and it is answerable in
   six weeks with a time-and-motion study on one branch.
2. **The referral turn-down rate ($2.4M–$12.0M swing).** Never measured. Marked "Available today? No" on
   the organisation's own KPI sheet. L2, L6 and L14 all multiply through it.
3. **Adoption (zero or everything).** Not a risk line — a multiplier on every lever except L15. The one
   prior attempt failed, and it failed on exactly this.
4. **The pay-model split by branch.** Section 3 shows the sign changes on at least six levers. The split
   across the branch estate — per visit, per point, hourly, salaried, union — is unknown, and it is a
   one-day Workday extract.
5. **Paraprofessional supply.** L3 is the third-ranked lever and is capped by whether LPNs, PTAs and
   COTAs can actually be hired market by market.

---

## 8. Time to value — the sequence

| Window | Levers | Cumulative gross, base case |
|---|---|---:|
| **Months 1–3** | L15 Workday PTO sync · payer-rule surfacing at plan of care (enabler) · L13 NOA and NOMNC discipline · weighted-vs-unweighted productivity publishing (enabler) | ~$0.6M |
| **Months 3–9** | L5 LUPA event alerts · L1a notification suppression | ~$3.6M |
| **Months 6–18** | L1b task collapse · L3 discipline match · L8 authorisation operations · L9 non-billable avoidance · L12 huddle compression | ~$11.6M |
| **Months 12–30** | L1c remaining scheduler release · L2 growth · L6 payer-aware prioritisation · L7 distribution · L10 premium labour · L14 territory targeting | ~$28.4M |
| **Months 24–36** | L11 HHVBP (two-year performance-to-payment lag) · L4 retention | ~$32.4M |

**The sequencing argument matters as much as the total.** Everything in the first window costs almost
nothing, requires no new system, lands inside a quarter, and is visible to exactly the branch leaders
whose scepticism killed the last attempt. Turning on an integration that already exists, surfacing a
coordination note that is already written, and publishing a productivity number the branch already owns
are not merely the early return — **they are the adoption strategy.**

---

## 9. The three pieces of evidence that most strengthen the case

**1. MedPAC's March 2026 recommendation to cut the CY2027 base rate by 7 percent (Chapter 8, voted 17–0).**

*Why it is decisive:* it removes the "why now" question from the room entirely. On a $260M episodic book
a 7% cut is **$18.2M of revenue gone** — roughly the whole base-case net benefit of this initiative,
arriving in a single rate year, on top of a projected freestanding margin fall from 21.2% to 19% and
$4.76 billion of temporary behaviour adjustment still to be recovered nationally. The same chapter
supplies the entire episodic denominator set — 8.4 visits per full period, the ~7% LUPA rate, $2,057
average period payment, $245 payment per visit — and the 5.7%-to-31.0% margin distribution that proves
operating discipline, not payment rates, is what separates a good agency from a poor one. The case's
arithmetic and its urgency come from one current, primary, federal document. Nobody in the room can
argue with MedPAC and nobody has to look anything up.

**2. The CMS nationwide enrolment moratorium effective 13 May 2026 (QSO-26-11-HHA/Hospice).**

*Why it is decisive:* it converts the initiative from an efficiency programme into the growth strategy.
Six months, extendable in six-month increments, nationwide, and it reaches certain majority ownership
changes requiring re-enrolment. **While it holds, the company cannot buy volume — not a new CCN, not an
acquisition that triggers re-enrolment.** Every dollar of growth must come from throughput inside the
existing licence footprint, which is precisely and only what this initiative produces. Pair it with the
HHS OIG finding that the largest MA organisations deny inpatient-rehab and long-term-acute placement at
54% and 65%, frequently reasoning that home health could meet the need — pushing higher-acuity patients
into home health on compressed, short-notice timelines — and both the demand side and the supply side
of the argument are dated external facts rather than internal assertions.

**3. Bergman et al. (2021), schedule volatility and clinician turnover.**

*Why it is decisive:* it is the only place in the entire evidence base where a **scheduling variable the
product directly controls** is causally linked to a **dollar outcome**, in the **right setting**, with
**payroll-grade data**. Schedule volatility measured as the coefficient of variation of daily visit
count over the prior 28 days; n = 3,716 nurses across 30-plus states at a top-five US home health
organisation; full-time RNs at the 75th percentile 16% more likely to quit and LPNs 34% more likely;
and **moving a full-time RN from the 75th to the 25th percentile cuts annual quit probability by 9.2
percentage points.** Against a published home health RN turnover rate of 25.46% and a defensible
replacement cost near 1.3× salary, that is real money — and unlike every other retention argument it is
falsifiable and measurable from week one. It also answers the hardest question a clinician-facing
rollout faces, *what does this do for me*, in the one currency that matters under per-visit pay: it
stabilises income in a system where the branch's scheduling failures cut the clinician's pay directly.

**Runner-up, and worth carrying in the pack:** the organisation's own finding that the authorisation
team already writes payer rules into a structured coordination note at verification, days before the
plan of care is written — and nobody reads it at the moment it would matter. It is the proof that the
highest-value fix requires no new data acquisition, only surfacing. It turns the initiative from "buy a
platform and hope" into "connect two things we already do," and it carries the patient-care argument
that survives a hostile question about whether this is really just a cost programme.

---

## 10. What this case must never claim

Stated explicitly, because several of these are one careless sentence away from being an enforcement or
clinical exposure.

- **That visits will be added to clear a payment floor.** OIG A-09-18-03031 found 21% of claims just
  above the threshold non-compliant; CMS committed MACs to targeting that cluster. Defensible behaviour
  is surfacing a below-threshold *ordered* plan of care for practitioner review, and rescheduling a
  missed visit — never generating one.
- **That margin enters a scheduling objective function.** Margin consequence may be *displayed* at the
  moment of decision. It may never be *weighted* against clinical need, and it must never be shown to
  the bedside clinician — only to the clinical manager, in aggregate.
- **That fewer visits per period is the goal.** Industry utilisation has already fallen 18% while
  discharge to community deteriorated 2.5 points, and the peer-reviewed evidence says intensity is not
  monotonic — 1 to 1.99 nursing visits per week outperformed higher frequencies. Placement, not volume.
  Under-delivery against an ordered frequency is a condition-level survey exposure under 42 CFR 484.60
  *and* a false-claims exposure.
- **That the tool changes frequency.** Frequency is a physician order. Software may prompt a change; it
  may never make one.
- **That telehealth substitutes for a floor visit.** G0320, G0321 and G0322 count toward nothing — not
  the LUPA add-on, not outlier units, not total visit counts, not the covered-skilled-visit requirement.
  Actual utilisation is 2.2% of periods and under 1% of all visits. Using virtual contact to fill a LUPA
  gap is a compliance trap. (One exception: a telehealth face-to-face encounter *can* satisfy the
  certification requirement.)
- **That star ratings deliver referral growth.** Introducing star ratings moved the probability of
  selecting a high-quality agency by **0.88 percentage points** (n = 186,498), and a natural experiment
  found a market-share effect of **0.25 percentage points with a confidence interval spanning zero**
  (−0.63 to 1.12). The ratings are a *valid* clinical signal — treatment by the highest-rated available
  agency reduced hospitalisation risk by 3.2 points and added 3.75 days independently at home over 180
  days — but they are a *weak* driver of consumer-side volume, and no peer-reviewed quantification of
  the star-to-preferred-network-to-volume link exists. Do not assert a referral-volume ROI you cannot
  source.
- **That route optimisation lowers labour cost.** Under per-visit pay it does not. Section 3.3.
- **That improving HHVBP performance guarantees a positive adjustment.** The linear exchange function
  makes break-even a moving cohort target; in CMS's own worked example an agency needed a Total
  Performance Score near 52 simply to break even. Improving while the cohort improves faster still
  produces a negative adjustment.
- **Any saving that depends on a specific manager working weekends.** If it is not encoded as standard
  work, it is not a business case.

---

## 11. What finance and operations must supply

Nothing below can be sourced externally. Each converts a modelled number into a bookable one.

| Input | Unlocks | Effort |
|---|---|---|
| **Pay-model split across the branch estate** (per visit / per point / hourly / salaried / union) | Every margin lever — the sign changes | 1 day, Workday |
| **Verified scheduler and clinician headcount** | Everything | 1 day, Workday |
| **Actual episodic period count and average period payment** | Replaces the derived 134,000 | Billing extract |
| **Referral turn-down count and reason** | L2, L6, L14 — the largest unmeasured lever | Instrument Commure |
| **Scheduler time-and-motion, one branch, two weeks** | L1 — resolves the largest spread driver | 6 weeks |
| **Time-stamped visit start and end from the EMR or EVV feed** | Travel, documentation, true visit duration | Already held |
| **Visit-to-documentation-lock cycle time by visit type** | The real SOC burden; L4 | Already held |
| **Contract, per-diem and overtime spend and bill rates by discipline** | L10 | Payroll and AP |
| **Loaded cost per visit by discipline, incl. LPN, PTA and COTA differentials** | L3 | Finance |
| **Actual LUPA rate and periods-one-visit-short count** | L5 | HCHB report |
| **Count and value of visits written off for authorisation** | L9 | Billing extract |
| **Missed, rescheduled and rebooked visit rates** | L5, L7 | HCHB report |
| **Late-NOA rate and average days late** | L13 | Billing extract |
| **Contracted MA and commercial per-visit rates** | The entire $289M non-episodic derivation | Contracting |
| **Turnover by discipline, 24 months, with tenure at separation** | L4 | HR |
| **Branch opex split with intake, referral and scheduling as its own line** | L1 attribution | Finance |

**The pay-model split is the highest-value single input, and it is a one-day extract.** For a per-visit
clinician, cost is linear and scheduling optimisation cannot manufacture margin from productivity —
only role substitution, visit mix and rate negotiation can. For a salaried clinician the marginal visit
is nearly free to the ceiling and unused capacity is a realised loss. Six of the fifteen levers here
invert between those two worlds, and the company does not currently know the mix.

**Contracted MA and commercial rates are the second.** They are the reason the all-payer margin is 5.0%
against a 21.2% FFS Medicare margin, they determine whether L6 is worth $2M or $7M, and **no public
source has them.**

---

## 12. The three weakest points in my own case

### 12.1 The entire volume base is derived, and my derivation contradicts the organisation's own

Not one of the numbers that everything multiplies through was counted. Episodic periods (134,000),
episodic visits (1.075M), non-episodic visits (2.06M) and total admissions (149,000) are all revenue
divided by a rate. The non-episodic half is the worst of it: I divided $289M by an assumed $140 blended
per-visit rate that **no public source supports**, because HHS OIG states outright that MA payment rates
to providers are not available anywhere, and the only MA-to-FFS ratio I could find in any source was an
M&A advisory note whose URL now 404s. If the true blended rate is $180 rather than $140, non-episodic
visits fall 22% and L2, L6 and L9 shrink with them.

Worse, my derivation directly contradicts the organisation's own workbook, which models 600 admissions
per branch across roughly 80 branches — 48,000 network admissions against my 149,000. I believe the
workbook counts episodic only, but **I cannot prove that from this material**, and if the workbook is
right in some way I have not seen, my second-ranked lever is overstated threefold. Two documents inside
the same initiative are threefold apart on the most basic operating denominator in the business and
nobody appears to have noticed. That is not a footnote; it is the first thing a competent CFO will find,
and finding it will make every other number in this document suspect until it is resolved.

### 12.2 The largest lever is the least attributable to the platform

L1 is first by size and by score, and it rests on a headcount target — 300 to approximately 100 — that
appears in the source as a hedged verbal aside (*"if there's 300 of them today, like maybe there's 100
of them in the future"*), from a speaker who was not quoting a headcount report. There is **no published
scheduler caseload benchmark in home health** against which to sanity-check it; that absence was
verified independently across the entire labour-economics corpus, which is otherwise a mature
benchmarking field. My own bottom-up arithmetic supports only 21 to 46 FTE of clearly removable work.

Everything above that depends on decisions Compassus can make **without buying anything**: turning off
DCS order approval (an HCHB toggle, not a Medicare requirement, and not done at other agencies),
enabling Shift Finder and visit dispatching (both already in the product and switched off), and
activating the Workday interface (already built and switched off). A CFO is entirely within their rights
to say the platform earns none of that — that this is a policy and configuration programme wearing a
software business case. My 15% attribution haircut is a judgement, not a measurement, and it is probably
too generous.

### 12.3 Adoption is a multiplier, not a risk line, and the only prior evidence is a failure

Every number in Section 7 except L15 assumes the tool is used. The one documented attempt failed, and it
failed on precisely the mechanism this case does nothing to change: *"a scheduler could have assigned
that exact same thing to them, but the tool did it, and they're like, well, it must be broken."* Leaders
constrained the system to mirror manual process, clinicians rejected out-of-territory assignments,
leadership allowed the resistance, and the smart logic was pulled out of Smart Scheduling before it was
ever truly piloted.

The compounding problem is that the two things the organisation needs from a pilot are in direct tension
and nobody has resolved it. The named pilot candidates are the **per-visit offices**, chosen because
per-visit clinicians have the strongest incentive to adopt. But per-visit offices are also where the
classic productivity-and-utilisation savings are *smallest* — Section 3.1 — so **the site most likely to
prove adoption is the site least likely to prove margin.** Whichever result the pilot produces, it will
be arguable, and the losing side of the argument will point at the pilot design. That tension should be
resolved deliberately in advance rather than discovered in the readout. This document does not resolve
it: it sizes the prize without reducing the single largest risk to collecting it.

### A fourth admission, briefer but not minor

Three of my load-bearing inputs are **modelled derivations sitting on verified CMS and BLS inputs, not
observed benchmarks**: the $95 marginal cost per visit, the $1,258–$1,386 LUPA contribution cliff, and
the $31 discipline-substitution differential. The derivations are sound, I have shown them, and two of
them reconcile against MedPAC from independent directions. They are still models. In anything
client-facing they must be labelled as models every single time, because the moment one is quoted back
as a benchmark the whole case becomes contestable on grounds that have nothing to do with whether it is
right.

And one evidentiary hole worth naming even though it does not damage me: **there is no published
operations-research result anywhere in the corpus on how much of the travel-time pool a routing
optimiser actually recovers.** The corpus can size the pool — roughly half of a home care clinician's
paid day is not spent in front of a patient, travel is 18–26% of it, about 11 miles and $8.36 per visit
— but contains zero evidence of the achievable reduction. That gap sits underneath a lever I already
refuse to book, because under per-visit pay a travel saving accrues to the clinician's evening and not
to the P&L. It would matter a great deal to a salaried operator. It does not matter here, and the reason
it does not matter is the single most important thing in this document.
