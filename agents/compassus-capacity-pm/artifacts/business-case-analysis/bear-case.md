# Bear Case — Capacity and Scheduling Platform Initiative

**Prepared for:** Finance / Investment Committee
**Date:** 21 August 2026
**Position:** Do not fund the platform. Fund a bounded instrumentation-and-configuration programme instead.
**Target document:** `agents/compassus-capacity-pm/artifacts/business-case-register.md` (first pass, 21 Aug 2026)

---

## 0. Evidence conventions used here

| Label | Meaning |
|---|---|
| **[EVIDENCED]** | Supported by a cited external source or by an internal document's own words |
| **[ARITHMETIC]** | Derived from the proponent's own numbers; the maths is checkable |
| **[UNTESTED CONCERN]** | A reasoned objection with no confirming evidence located. Stated as a concern, not a finding |

Where I quote the proponent against themselves, I cite the internal file. That is deliberate: the strongest case against this programme is largely written inside it.

---

## 1. Executive summary — the case fails on four independent grounds

Any one of these should stop funding. All four are present.

**1. The case contradicts the organisation's own authoritative model by roughly 4×.** **[ARITHMETIC]**
The 13 August workbook — which `business-case-and-kpis.md` explicitly calls "**authoritative**" — models **$7.9M/yr network-wide** at the Moderate scenario, **$4.0M** Conservative, **$14.3M** Hopeful. Eight days later the business case register claims a **single lever** (W1, scheduler headcount) worth **~$12M**, plus $2.2M LUPA, $1.9M discipline match, $11M growth, $1.3M VBP, $2.9M payer leverage — **~$31M of named dollars**. Restricting to waterfall-only levers still gives ~$16M, **2× the authoritative model's Moderate case and above its Hopeful case**. Two documents from the same team, eight days apart, differ by a factor of two to four. Neither has been reconciled. A committee cannot fund a number that the team's own prior model contradicts.

**2. There is no cost side.** **[EVIDENCED]**
Section 10 of the register lays out a waterfall with six named cost bars — platform licence, implementation and integration, capacity steward and analyst roles, payer rules library build and upkeep, change management and training — and **populates none of them**. A grep of the entire repository returns no licence estimate, no implementation estimate, no total cost of ownership, no payback period, no NPV, no IRR. A benefits register with an unpriced denominator is not a business case; it is a benefits register.

**3. Every load-bearing input is admitted missing — including the input the case itself calls decisive.** **[EVIDENCED]**
Section 9 lists eleven required inputs and says of them: "*Nothing below can be sourced externally.*" Among them is "loaded cost of a scheduler role" — the multiplicand in the largest lever. And the register's own words: "**The pay-model split is the highest-value single input**… For a per-visit clinician, cost is linear and **scheduling optimisation cannot create margin**." Roughly **70% of ~3,000 clinicians are paid per visit**. The case therefore concedes that its central margin mechanism does not operate on the majority of the workforce, and does not know the exact split.

**4. The adoption fix and the value case are mutually exclusive.** **[EVIDENCED]**
The prior Alabama Smart Scheduling pilot failed because "*leadership allowed the resistance*" and "*it was never truly piloted*" (`discovery-session.md`). The design response is **DE-09: "The tool recommends; the human accepts,"** clinicians supply their own availability, and the framing is "assistant, not controller." That is not a fix for the failure — it is a formal, permanent concession of the exact authority whose absence caused it. Every modelled dollar assumes assignments actually change. If the clinician can decline and the leader will not enforce, the optimiser is advisory and the gains do not accrue. **You cannot buy optimisation and simultaneously promise nobody will be optimised.**

---

## 2. Attack 1 — The headcount lever (W1, ~$12M) is the weakest number in the case, not the strongest

The register calls W1 "the largest single hard lever in the initiative." It is neither hard nor a lever.

### 2.1 The arithmetic is two unmeasured numbers multiplied together

W1 = 200 roles released × $60,000 loaded cost = $12M. **[ARITHMETIC]**

Both terms are unknown:
- **Loaded cost** appears in §9 as a missing input ("Loaded cost of a scheduler role → unlocks W1, W2"). The case is using a placeholder in its headline lever.
- **200 roles** comes from a single line in a whiteboard session — "*roughly 300 schedulers today, perhaps 100 in target state*" — recorded under "Also material," with the word *perhaps*.

Sensitivity, using only plausible variation in two admitted-unknown inputs: **[ARITHMETIC]**

| Roles released | @ $48k | @ $60k | @ $72k |
|---|---|---|---|
| 100 | $4.8M | $6.0M | $7.2M |
| 150 | $7.2M | $9.0M | $10.8M |
| 200 | $9.6M | **$12.0M** | $14.4M |

The "largest hard lever" spans **$4.8M to $14.4M — a 3× range — before any implementation risk is applied.** The register quotes the top of that range as the headline.

### 2.2 The target state fails a simple staffing reductio

**[ARITHMETIC]** 300 schedulers across ~80 branches ≈ **3.75 per branch**; 3,000 clinicians ≈ **1 scheduler per 10 clinicians**. The target state of 100 is **1.25 schedulers per branch** — approximately one person per branch — at a ratio of **1:30**.

Now hold that against what the same documents say that person must do:
- **DE-10** deliberately preserves the role "for urgency, local knowledge, and relationship-based coverage."
- **CN-48**: "Coverage recovery runs on relationships. Visits get covered because a scheduler has built enough goodwill to ask a favour on a Friday afternoon."
- The call-out "flare button" scenario requires clinical-priority triage with human sign-off.
- Weekend and after-hours scheduling is listed as **explicitly deferred / out of scope** in the whiteboard session — i.e. unexamined.

One person per branch cannot be a 24/7 air-traffic controller with local relationship capital, absorb PTO and their own turnover, and run exception recovery. Either the 100 is wrong, or DE-10 is wrong. Both cannot hold. **[ARITHMETIC + EVIDENCED]**

### 2.3 The named pain point is 6% of the promised saving — and is a configuration fix

W2 (notification noise) is, by the register's own maths, **~11.5 FTE ≈ $690k** at the $60k assumption. That is **5.75% of W1**. **[ARITHMETIC]**

The register calls it "the most-cited frustration in the scheduler's day and the cleanest single demonstration of the problem." It is also, per the whiteboard, an HCHB behaviour: "HCHB generates a pending-auth workflow every day per patient." Suppressing a notification that fires when no authorised visit count has changed is **a filter rule, not a platform**. The single most-cited problem in the discovery record is worth six cents on the dollar of the headline lever and is fixable this quarter for near-zero capex. **[EVIDENCED]**

### 2.4 What the literature says about promised versus realised admin headcount reduction

- **McKinsey / University of Oxford, 5,400 large IT projects: deliver 56% less value than predicted** — and, critically, "most sponsors don't know, because they never measured." ([summary](https://thinkpieces.stavros.io/posts/how-organizations-consistently-underinvest-in-the-ability-to/)) **[EVIDENCED]**
- **Cranfield: 47% of large UK companies openly admitted overstating benefits in business cases to get approval.** ([same](https://thinkpieces.stavros.io/posts/how-organizations-consistently-underinvest-in-the-ability-to/)) **[EVIDENCED]**
- **KPMG: only 13% of organisations track benefits until the original business-case commitments are met**; **PMI: only 17%** have real benefits-realisation maturity. ([PMI](https://www.pmi.org/learning/thought-leadership/series/benefits-realization)) **[EVIDENCED]**
- **Deloitte intelligent automation survey: only 3% of organisations have scaled their digital workforce; 63% said time-to-implement expectations were not met; piloted payback expectation 9 months versus 12 months actually achieved.** ([Deloitte](https://www.deloitte.com/us/en/insights/topics/talent/intelligent-automation-2022-survey-results.html)) **[EVIDENCED]**

Applying the McKinsey/Oxford 56% shortfall to W1 at its own midpoint ($9M) gives **~$4M realised** — against an unpriced cost base. **[ARITHMETIC]**

### 2.5 Redistribution, not elimination

**[UNTESTED CONCERN — reasoned, no confirming source located within budget]** The removed work is described as "the SOC/recert/ROC cycle, the per-discipline assignment burst, auth chasing, and exception recovery." Three of those four are *interruption-driven* rather than *queue-driven*. Time released from interruption-driven work is characteristically non-cashable: it disperses across the remaining roster in minutes-per-day increments and never aggregates into a whole post you can remove. The register itself half-concedes this — "the release is phased across the rollout, so year one carries a fraction" — without saying what fraction, or whether the fraction ever reaches one.

The specific failure mode to expect: the schedulers are not made redundant, the work migrates to **DCS clinical managers and branch executive directors**, and the company converts a $60k administrative hour into a $120k clinical-manager hour while booking a saving.

### 2.6 The counterfactual is not "300 forever"

**[UNTESTED CONCERN]** Home health all-staff turnover ran **22.18%** in 2020 ([HHCN](https://homehealthcarenews.com/2020/10/home-health-turnover-rate-hits-22-18/)); scheduler-specific turnover is not in the record. If administrative attrition is anywhere near that, natural attrition removes on the order of 60–70 scheduler posts a year. A hiring freeze plus the configuration changes in §6 below could plausibly reach a large share of a 200-post reduction over three years **with no platform at all**. No counterfactual baseline appears anywhere in the case. Absent one, the platform is being credited with the entire delta from a static 300.

---

## 3. Attack 2 — The LUPA recovery claim (R2, $2.2M) is a four-assumption chain sitting on an active federal enforcement target

### 3.1 The chain

R2 = 128,000 periods × 7% LUPA rate × 81.12% one-visit-short × 25% operationally caused and clinically indicated × $1,200 cliff ≈ $2.2M. **[ARITHMETIC]**

Inspect each multiplicand:

| Term | Status |
|---|---|
| 128,000 periods | **Derived, not actual.** §9 lists "actual episodic period count" as a missing input. The organisation's own workbook implies **80,000** (80 branches × 1,000 periods) — a **60% discrepancy** with the register |
| 7% LUPA rate | National average (MedPAC). §9 lists "actual LUPA rate" as missing. Compassus's own rate is unknown |
| 81.12% one visit short | **Applies to subsequent periods only** (McBee). The register applies it to **all** LUPA periods. This is a category error that inflates the base |
| 25% operationally caused | **The research corpus labels this "assumption — no published basis."** It is invented |
| $1,200 cliff | Register says ~$1,200; the workbook says **$1,400**. Internally inconsistent |

The source itself is a **vendor blog post** (McBee Associates), not peer-reviewed or CMS-published.

Four unmeasured or misapplied terms multiplied together produce a number quoted to two significant figures. **[EVIDENCED]**

### 3.2 The compliance exposure is real, current, and made worse by the platform

- **HHS OIG report A-09-18-03031** (July 2020) sampled 120 claims with visits just above the LUPA threshold: **25 of 120 (21%) did not comply with Medicare requirements**; extrapolated national overpayment **$191.8M**. OIG's stated rationale: "HHAs have an incentive to improperly bill claims with visits slightly above the LUPA threshold." **CMS concurred with all recommendations, including that MACs target such claims for additional review — closed-implemented.** ([OIG](https://oig.hhs.gov/reports/all/2020/cms-could-have-saved-192-million-by-targeting-home-health-claims-for-review-with-visits-slightly-above-the-threshold-that-triggers-a-higher-medicare-payment/)) **[EVIDENCED]**
- **20 of the 25 non-compliant claims would still have been non-compliant under PDGM's variable thresholds** — the exposure did not go away with the payment model. **[EVIDENCED]**
- **The enforcement environment in 2026 is materially hotter than in 2020.** CMS imposed the six-month nationwide home health and hospice enrollment moratorium on **13 May 2026** explicitly as part of an anti-fraud task force, stating it will "intensify targeted investigations, **deploy advanced data analytics**, and accelerate the removal of… providers." ([CMS press release](https://www.cms.gov/newsroom/press-releases/cms-announces-aggressive-nationwide-crackdown-fraud-six-month-hospice-home-health-agency-enrollment); [AHA](https://www.aha.org/news/headline/2026-05-13-cms-announces-6-month-enrollment-moratorium-home-health-agency-enrollment)) **[EVIDENCED]**
- **2026 is a record year for False Claims Act recoveries**, and the 2026 National Health Care Fraud Takedown — the first under DOJ's new National Fraud Enforcement Division — spanned 56 federal districts. ([Paul Hastings](https://www.paulhastings.com/insights/client-alerts/healthcare-enforcement-roundup-what-providers-need-to-know); [OIG](https://oig.hhs.gov/fraud/enforcement/2026-national-health-care-fraud-takedown/)) **[EVIDENCED]**
- **MedPAC has separately found provider-reported OASIS discrepancies "often favouring higher payments"** and cites OIG documentation of under-reported falls with major injury. The regulator's prior is already that agencies' self-reported utilisation data drifts toward revenue. **[EVIDENCED]**

### 3.3 Why the "clinical gate" does not protect you

The register states the gate absolutely: "*Nothing here justifies adding a visit to clear a threshold.*" That is the right policy and I credit it (see §11). It is not a control.

The problem is the **discoverable artifact**. To recover LUPA leakage you must build a view that computes, per patient, *"this period is N visits below its threshold with M days remaining."* That view is functionally identical whether the user's motive is clinical or financial. In an audit or a qui tam action, the existence of a purpose-built, revenue-labelled threshold-proximity alert — commissioned under a business case that booked **$2.2M of LUPA recovery as a benefit** — is the government's exhibit. The business case register itself becomes discoverable evidence of intent.

**[UNTESTED CONCERN]** No published account of an agency being penalised specifically for a LUPA-proximity alerting tool was located. The concern is prospective, not historical. But the asymmetry is stark: **$2.2M of speculative annual upside against a documented 21% non-compliance rate in exactly this claim cluster, in a year of record FCA recovery.** A single extrapolated overpayment finding across ~$260M of episodic revenue dwarfs the lever.

### 3.4 The corpus's own conclusion undercuts the platform

The research file states: "**low LUPA rate and low visit count travel together**… Agencies that manage utilisation well do not LUPA more; they LUPA less, **because they schedule deliberately rather than reactively**." **[EVIDENCED]**

Deliberate scheduling is a management practice. Nothing in that sentence requires a platform.

---

## 4. Attack 3 — The retention claim rests on one observational study that does not transfer to this workforce

### 4.1 What the study actually is

Bergman, Song, David, Spetz and Candon (*Medical Care Research and Review*, 2021; [PMC9122113](https://pmc.ncbi.nlm.nih.gov/articles/PMC9122113/)): 3,716 nurses, one top-five US home health organisation, **January 2016 – March 2019**. Schedule volatility = coefficient of variation of daily visit count over the prior 28 days.

Limitations, several of which the corpus itself flags: **[EVIDENCED]**

1. **Observational, single organisation, no randomisation and no intervention.** It establishes association between a schedule statistic and quit behaviour. It does not establish that *changing* the statistic changes the behaviour.
2. **Directionality is unresolved and the reverse story is at least as plausible.** A nurse who has decided to leave declines visits, calls out more, restricts availability and takes leave — which *mechanically raises the coefficient of variation of her daily visit count in the 28 days before she quits*. Volatility measured on a trailing window ending at separation is contaminated by the separation itself. **[UNTESTED CONCERN — the published paper's identification strategy was not re-derived here, but the confound is structural to the metric's construction.]**
3. **The effect vanishes entirely for part-time nurses.** The authors attribute the mechanism to income and schedule instability for people who *depend on the job*.
4. **Data is 2016–2019 — pre-COVID.** Home health labour markets, wage levels, per-visit prevalence and turnover dynamics all moved substantially after 2020.
5. **Effect size framing is unstable across restatements.** The primary paper gives 75th-vs-25th percentile as 9.2 percentage points; the Penn LDI summary frames 5th/95th percentiles as 40% less / 50% more likely to quit. Which framing you pick moves the dollar value several-fold.

### 4.2 It does not transfer to a 70%-per-visit workforce — and may invert

This is the decisive objection. The study's mechanism is *income instability among nurses who depend on a stable income*. Apply that to this workforce:

- **~70% of ~3,000 clinicians are paid per visit.** For them, income *is* visit count. Reducing the variance of daily visit count means reducing their peak days.
- The corpus records that on per-visit models "clinicians are motivated to do more visits," and that the highest producers are precisely those who load their heavy days.
- **Smoothing a per-visit clinician's schedule is, for the top quartile, a pay cut delivered as a feature.** **[UNTESTED CONCERN]**
- The corpus also records that "**independence and flexibility are the top drivers of home health nurse job satisfaction**" ([McCreary, *Geriatric Nursing*](https://www.sciencedirect.com/science/article/pii/S0029646519300878)) and warns explicitly "against optimizers that feel like surveillance." **[EVIDENCED]**

So the retention lever is being asserted for a population that most resembles the group in which the study found **no effect**, using a mechanism that on this pay model runs backwards.

### 4.3 The counter-evidence on scheduling interventions and turnover

- **Bae 2024, *International Nursing Review* — systematic review of nurse staffing and work schedules on turnover:** concludes staffing and schedules are "among multifaceted factors… worth examining," which is the language of unresolved evidence, not established causation. ([Wiley](https://onlinelibrary.wiley.com/doi/abs/10.1111/inr.12849) / [PubMed](https://pubmed.ncbi.nlm.nih.gov/37216655/)) **[EVIDENCED]**
- **2017 overview of systematic reviews of interventions to reduce adult nursing turnover:** of a large published literature, only seven reviews met inclusion criteria, providing "moderate quality review evidence **from poorly controlled primary studies**," and "strength of evidence is hard to determine despite a plethora of reviews." ([PMC5725565](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5725565/)) **[EVIDENCED]**
- **2025 review of retention interventions for newly graduated nurses:** "current evidence is **insufficient to make recommendations** for nursing management on interventions." ([PMC12907248](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12907248/)) **[EVIDENCED]**

The intervention-level literature does not support a committed financial benefit. It supports a hypothesis.

### 4.4 The dollar value is internally inconsistent by 3× and rests on a hospital number

- Workbook: **$40,000** replacement cost per clinician, 5 departures per branch/yr.
- Research corpus: **~$124,000** (1.3× a $95,000 loaded salary).
- The corpus's own flag: "**there is no rigorously sourced, home-health-specific RN or therapist replacement cost in the published literature. Every credible dollar figure is hospital-derived.**" **[EVIDENCED]**

Three-fold internal disagreement on the multiplicand, on top of an untransferable effect size, on top of an unestablished causal direction.

### 4.5 There is a cheaper substitute that is already working

HCS 2025 (1,111 agencies, 52,200+ employees): wage increases and sign-on bonuses **measurably reduced turnover — 36% of agencies reported turnover decreased**, fewer than 21% reported an increase. Average RN sign-on bonus **$7,499**; average home care RN hourly **$41.79**, up 3.56%. ([HHCN](https://homehealthcarenews.com/2025/11/home-health-worker-retention-improves-as-wages-bonuses-increase-in-2025/)) **[EVIDENCED]**

The corpus draws the right commercial conclusion and the case ignores it: a scheduling intervention "is competing against a $7,499 one-time cost per hire, **and should be priced against it**." At 5 departures per branch across 80 branches (400/yr), the entire retention problem can be attacked directly for roughly $3M/yr in bonuses with a *demonstrated* effect — no integration risk, no adoption risk, reversible next quarter.

---

## 5. Attack 4 — The per-visit pay model guts the value case, and the case knows it

### 5.1 The concession, in the proponent's own research

From `05-cost-and-labor-economics.md`, §2.2, unedited: **[EVIDENCED]**

> "For a **per-visit contractor**, cost is a pure variable… There is no capacity to 'fill' and no idle cost to absorb… **scheduling optimization cannot improve it.** Better routing saves the clinician's time, not the agency's money. The only levers are rate negotiation and visit mix."

And §2.3:

> "A branch that has quietly shifted to per-visit pay to control cost **has also destroyed most of the value a scheduling optimizer can create for it**."

And the substitution prize — the corpus's own headline value construction, **$32,200 per RN per year** — carries this note:

> "This is the number the platform is selling. It is also the number that is **entirely wrong** if the branch's field staff are paid per-visit."

**70% of ~3,000 clinicians are paid per visit.** The platform's headline value mechanism is disclaimed on 2,100 of 3,000 clinicians by the case's own research file.

### 5.2 What is actually left after removing the per-visit population

| Lever | Survives on a per-visit workforce? |
|---|---|
| Reclaim idle salaried capacity → displace contract labour | **No.** No idle capacity exists to reclaim |
| Reduce cost per visit by raising visits/day | **No.** Cost is linear; unit cost is fixed by rate |
| Reduce overtime (W4) | **Largely no.** Per-visit staff do not generate overtime |
| Route optimisation → margin | **No.** Time saved accrues to the clinician, not the agency |
| Retention via schedule smoothing (§4) | **No, and possibly inverts** |
| W7 unpaid evening confirmation | **Pays nothing.** Register concedes: "Automating it does not reduce payroll, because it was never paid" |

The residual on the per-visit half is: **discipline/role match (U1), non-billable-visit avoidance (R1), LUPA (R2, compliance-encumbered), and throughput growth (G1, upside only).** U1 is a policy default (DE-08). R1 is an authorisation-process fix. Neither requires this platform.

### 5.3 The W7 inversion is worse than neutral — it can be margin-destroying

W7 is 3,000 clinicians × 30 min/day ≈ **190 FTE-equivalents of unpaid evening labour**. **[ARITHMETIC]** The register correctly says it converts to either retention value or, on per-visit pay, "additional capacity the clinician can sell."

But an *additional visit sold by a per-visit clinician is an additional cost to the agency.* It is margin-positive only where reimbursement per visit exceeds the per-visit rate plus overhead. MedPAC's March 2026 data puts the **all-payer margin for freestanding HHAs at 5.0%** against a 21.2% FFS Medicare margin — meaning the non-Medicare book, which is **53% of this business ($289M)**, is in aggregate at or below breakeven. **[EVIDENCED]** On that half of the book, converting released clinician time into additional per-visit volume plausibly **destroys** contribution. The register flags the payer-class distinction but does not carry it through to the sign of the number.

### 5.4 The pilot is designed so it cannot answer the question

`discovery-session.md` names the preferred pilot sites: "**a pay-per-visit office (Providence, Ohio Health, BSMH)**" — chosen because "existing habits won't conflict with new tooling."

The register spots the trap and states it in §9: "*The named pilot candidates are the per-visit offices, which are the best sites for adoption and the worst sites for proving a margin case.*"

Correctly identified — then not resolved. As designed, the pilot will produce an adoption result and **no margin result**, and the margin case will be asserted on inference. That is how a programme gets to enterprise rollout without ever having been tested on its own thesis.

### 5.5 The $400 test

The register calls the pay-model split "the highest-value single input." The corpus identifies exactly where to buy it: the **HCS Home Care Salary & Benefits Report, ~$400** for non-participants, carrying pay mode, caseload and turnover by job code across 1,111 agencies. **[EVIDENCED]**

The organisation also holds its own payroll data, which answers the question exactly and for free.

**The committee is being asked to approve an eight-figure programme whose decisive qualifying question could have been answered before the meeting, at zero cost, from internal payroll.** That it was not is the single clearest signal about the case's readiness.

---

## 6. Attack 5 — Attribution: a large share of the claimed benefit is available now, from assets already owned

The whiteboard session is unusually candid about this. It records that "**genuine automation in HCHB is approximately nil**" — not because HCHB lacks the features, but because they are **not switched on**.

### 6.1 The already-owned list

| Item | Status per internal record | Claimed lever it feeds |
|---|---|---|
| **Workday ↔ HCHB PTO integration** | "**exists and is switched off**"; PTO hand-keyed; five of seven nurses can be approved off the same day | **W5 — the register itself calls this "Committed, near zero cost"** |
| **HCHB Shift Finder** (clinician self-serve of open visits) | "**already available and not turned on**" | Exception recovery, call-out coverage, clinician autonomy |
| **HCHB Smart Scheduling** | Already licensed and previously piloted. Scores **71.2** overall in the org's own Functional Scorecard; combined HCHB footprint coverage **57.4%**, 26 of 32 categories covered, **6 gap categories** | Most of the scheduling module |
| **Pending-auth notification storm** | HCHB generates one workflow per patient per day; majority non-actionable | **W2 (~$690k)** — a filter rule |
| **DCS approval on every physician order** | "**An HCHB toggle, not a Medicare requirement**, and not done at other agencies. The largest single source of DCS workflow backlog" | Plan-of-care and order latency |
| **Per-discipline task explosion** | Four disciplines → eight tasks "for a decision already made" | Scheduler workload — HCHB workflow configuration |
| **Payer rules at plan-of-care creation** | "**The data already exists — the auth team writes it into a coordination note at verification.**" Whiteboard calls surfacing it "**high-value, low-complexity**" | R1, R4, abrupt-discharge prevention |
| **Discipline/role match (DE-08)** | A default-and-opt-out **policy**, plus a report | **U1 — $1.9M**, the second-largest waterfall lever |
| **Commure scheduling-grid view** | Named as a next step in the existing Commure deployment | Replaces Excel scheduling grids |

**[EVIDENCED, all internal]**

### 6.2 What the vendor of record already sells

HCHB markets Smart Scheduling as automating "visit planning within configurable agency guardrails such as licensure, productivity standards, territory and mileage limits, patient preferences, and continuity priorities," with "**nightly optimization plus real-time automation for admits, reassignments, declined visits**," up to 22 days of future-visit automation, claims of automating up to 95% of visit types and 64% of workflow tasks, and "**a configurable dashboard… for tracking KPIs**." ([HCHB](https://hchb.com/hchb-smart-scheduling/); [HCHB Smart Scheduling Automation](https://hchb.com/hchb-smart-scheduling-automation/); [PRWeb](https://www.prweb.com/releases/homecare-homebase-smart-scheduling-enhances-efficiency-and-continuity-of-care-setting-new-industry-standards-302171671.html)) **[EVIDENCED]**

Note what DE-03 specifies for Phase 1 of the new platform: "**visualization only — no automation in the first release**," plus territory and service area, "probably the same dashboard." **That is a narrower scope than a product the organisation already licenses and has already declined to use.**

The whiteboard's own warning: "*We have to be really careful that we're just not reinventing Home Care Home Base.*" And, sharper: "*That workflow shouldn't exist to begin with for the scheduler.*"

### 6.3 The attribution conclusion

**W5 is explicitly $0-cost and pre-existing. W2 (~$690k) is a filter. U1 ($1.9M) is a policy default. The payer-rules win is a report against data already keyed.** By the register's own sizing, that is roughly **$2.6M of named annual benefit plus the free items — attributable to configuration and policy, not to a new platform.**

The register makes the honesty note itself and then does not act on it: "*not all of it is attributable to this platform, because part of the reduction comes from workflow automation that should arguably not exist at all.*" **[EVIDENCED]**

A defensible case would net out the configuration counterfactual before drawing the waterfall. This one does not, so **every bar is gross of an unmeasured "we could have done this anyway" deduction.**

---

## 7. Attack 6 — Implementation risk: the base rate is bad, the organisation has already failed once, and nobody has priced failure

### 7.1 The prior failure is not exculpatory — it is diagnostic

The record's framing: Alabama Smart Scheduling failed "**not because the technology was flawed**," because leaders locked clinicians to zip codes, clinicians rejected out-of-territory assignments, "**leadership allowed the resistance**," and "the system was never allowed to do what it was designed to do — **it was never truly piloted**."

Read as a CFO: the organisation ran a controlled experiment on *its own ability to make a scheduling optimiser stick* and the answer was no. The binding constraint is not the tool. **It is management's demonstrated unwillingness to enforce a scheduling decision against tenured clinician objection.** Buying a different tool does not change that variable.

The corroborating constraints are already logged:
- **CN-43**: "Machine-assigned visits get rejected where human-assigned ones would not. **The documented failure mode of prior smart-scheduling attempts.**"
- **CN-42**: "Tenured clinicians resist territory flexibility."
- **CN-49**: A union LPN refused out-of-territory work; the position was held and used as leverage even after being determined unfounded.
- **CN-41**: "**Clinicians have stopped calling in for backup visits. They do not trust the branch to respond.**" — trust capital is already spent.

**[EVIDENCED, all internal]**

### 7.2 The organisation's own scorecard flags the repeat

`business-case-and-kpis.md` records that HCHB Smart Scheduling scores highest **and** "overreaches our stated posture on **16 variables**," and states plainly: "**That is the Alabama failure mode expressed as a number.**"

The proposed answer is DE-09 (recommend/accept) and clinician-supplied availability. That guarantees no repeat of Alabama — by guaranteeing that the optimiser never optimises anything a clinician declines. **The failure is prevented by removing the function whose value was being purchased.**

### 7.3 The external base rate

- **Flyvbjerg & Budzier, 1,471 IT projects: average cost overrun 27%, but one in six is a "black swan" at 200% average cost overrun and ~70% schedule overrun** — and the probability of an IT project running out of control is "20 times greater than the risk predicted by standard risk management models." ([SSRN](https://doi.org/10.2139/ssrn.2229735); [arXiv](https://arxiv.org/abs/1304.0265)) **[EVIDENCED]**
- **Healthcare IT specifically: 30–50% of EHR implementations fail on common estimates, with some analyses putting unsuccessful health IT projects as high as 70%, and 73% of hospital software projects failing to deliver expected value.** Notably, "**the largest, most expensive projects have the highest failure rates.**" ([Artezio](https://www.artezio.com/pressroom/blog/hospital-software-projects/); [topflightapps](https://topflightapps.com/ideas/ehr-implementation/); [PMC11507143](https://pmc.ncbi.nlm.nih.gov/articles/PMC11507143/)) **[EVIDENCED]**
- **Prosci 2025 ERP study: organisations with comprehensive metrics maturity achieve 28% success rates; those with poor metrics achieve 7%.** ([Prosci](https://www.prosci.com/blog/governing-erp-benefits-beyond-go-live)) **[EVIDENCED]** — see §8; this organisation is, by its own KPI table, in the 7% bucket.
- **Algorithmic management research consistently finds workers' negative reactions to algorithmic control exceed positive ones, centred on loss of autonomy**, with documented covert resistance. ([PMC9859016](https://pmc.ncbi.nlm.nih.gov/articles/PMC9859016/); [PMC11672927](https://pmc.ncbi.nlm.nih.gov/articles/PMC11672927/)) That is the Alabama mechanism, generalised. **[EVIDENCED]**

This programme has every high-risk marker: large scale (80 branches, 3,000 clinicians), multi-system integration (HCHB — described as "not real-time; requires manual sync" — plus Commure, NestMed, Pulse, Workday), a workforce with documented resistance, and a prior failure at the same organisation.

### 7.4 What failure costs — nobody has said

**[EVIDENCED — by absence]** No cost estimate exists, therefore no failure cost exists. The knowable components:

1. **Sunk licence, integration and internal programme cost** — unpriced.
2. **Management attention** across the entire branch estate during a year in which MedPAC has recommended a 7% base-rate cut (§9).
3. **A second failed scheduling initiative in the same clinician population.** CN-41 already records a trust deficit that costs latent capacity today. A second failure hardens it, and makes the *third* attempt — which may be the one that matters — substantially harder.
4. **The compliance artifact survives the failure.** If R2 tooling is built and the programme is cancelled, the LUPA-proximity view and the business case that justified it remain discoverable.

---

## 8. Attack 7 — The measurement problem makes this programme structurally unfalsifiable

### 8.1 The organisation's own KPI table

From `business-case-and-kpis.md`, "Available today?":

**Primary KPIs (the scoreboard finance judges results by):**

| KPI | Available today |
|---|---|
| **Quantified capacity & utilisation — "the initiative's core metric"** | **No** |
| Referral turn-down rate (no capacity) | **No** |
| Premium / contract / overtime labour | Partial |
| LUPA rate & revenue leakage | Partial |
| Clinician turnover | Yes |

**Secondary KPIs: six of eight are "No"**, including schedule volatility (the retention lever's entire measurement basis), continuity of care, caseload balance, productivity vs potential, coordination latency, and tool adoption — the last flagged "**MVP-critical: if it is not used, none of the rest happens.**"

The tab's own summary: "*several **primary** metrics do not exist as a live number today. **Capturing the baseline is itself part of the work***" and "*almost none of these exist today as a live, trustworthy, decision-ready number.*" **[EVIDENCED]**

### 8.2 Why this is disqualifying rather than merely inconvenient

1. **You cannot compute a benefit without a baseline.** Every "Modelled" lever in the register substitutes a national benchmark for a Compassus figure. The register says so in its own header: "*built from national benchmarks where Compassus figures do not yet exist.*"
2. **You cannot verify realisation after go-live either.** If the core metric does not exist pre-implementation, there is no pre-period to compare against. The programme can never be proven to have failed. **[ARITHMETIC — this follows directly from the table]**
3. **Post-hoc, any number can be claimed.** This is precisely the McKinsey/Oxford finding: projects deliver 56% less value than predicted "**and most sponsors don't know, because they never measured**."
4. **Prosci's 7%.** Poor metrics maturity → 7% success rate versus 28% for comprehensive. By its own table this organisation is in the low bucket **today**, before a line of code.

### 8.3 The self-referential defect

The register's §13 next step is "**build the assumptions model**" so the case "can be argued at the assumption level rather than the conclusion level." That is exactly right — and it is an admission that **the conclusions currently on the page are not yet arguable.** The document being brought for funding tells you, in its final section, that the artifact that would make it fundable has not been built yet.

### 8.4 Is it ever legitimate to fund an unmeasured programme?

Yes — as **measurement**, at measurement scale, with a gate. It is not legitimate to fund it as a **platform** with an eight-figure implied commitment and a benefits waterfall quoted to two significant figures. The register conflates the two: it uses the absence of measurement as *evidence of opportunity* ("the most under-instrumented dollar in the whole initiative," R1) rather than as *evidence of uncertainty*. Unmeasured is not the same as large.

---

## 9. Attack 8 — Opportunity cost, in a business with 5% all-payer margin and a proposed 7% rate cut

### 9.1 The scale check that should have been run first

**[ARITHMETIC, on MedPAC-published margins]** MedPAC March 2026: freestanding HHA **FFS Medicare margin 21.2%**, **all-payer margin 5.0%** (2024). Applied to this book:
- All-payer profit pool on ~$549M ≈ **$27M**.
- W1 alone ($12M) would be **~44% of total company profit, from scheduling administration**.
- The register's full named benefit (~$31M) would **exceed the entire all-payer profit pool**.

A lever that large, from a support function, in a mature industry, should trigger disbelief on its face. The organisation's own workbook — at $7.9M, or **~29% of the profit pool** — is already aggressive. The register's number is not credible at the scale of the enterprise it is describing.

### 9.2 The competing claim on management attention is larger than the prize

**MedPAC has recommended Congress cut home health base payment rates by 7% for CY2027**, citing margins that "should be lower," worth **$750M–$2B in year one and $10–25B over five years** to the programme. ([McKnight's](https://www.mcknightshomecare.com/news/medpac-to-congress-cut-home-health-payment-rates-by-7-percent-in-2027/); [HHCN](https://homehealthcarenews.com/2025/12/medpac-to-recommend-7-cut-to-2027-home-health-payment-rate/); [MedPAC Ch. 8](https://www.medpac.gov/wp-content/uploads/2026/03/Mar26_Ch8_MedPAC_Report_To_Congress_SEC.pdf)) **[EVIDENCED]**

7% of ~$260M episodic ≈ **$18M/yr** — **larger than the register's entire waterfall**, arriving in ~16 months, and requiring exactly the executive bandwidth this programme would consume.

### 9.3 Where the money and attention should go instead

| Alternative | Size | Basis |
|---|---|---|
| **Configuration and policy sprint** (Workday PTO on, Shift Finder on, notification filter, DCS toggle decision, DE-08 discipline default, payer rules surfaced at POC creation, Commure grid view) | **~$2.6M named + the free items**, at near-zero capex, inside 90 days | §6, all internal-sourced |
| **Non-episodic contracting** — $289M at or below breakeven all-payer. The register's own Q4 prices a 1% rate/mix improvement at **$2.9M** | **$2.9M+ per point**, no technology risk | MedPAC 5.0% all-payer; register Q4 |
| **CY2027 rate-cut defence and case-mix/coding accuracy** | Up to **~$18M** exposure | MedPAC 7% recommendation |
| **Direct retention spend** — wages and sign-on bonuses, the one lever with demonstrated effect | ~$3M/yr covers 400 departures at the $7,499 benchmark | HCS 2025 via HHCN |
| **Instrumentation only** — build the baselines in §9 of the register | Low six figures | Makes every future case fundable, including this one |

Each of these is faster, cheaper, reversible, and does not depend on 3,000 clinicians accepting a machine's recommendation.

### 9.4 The moratorium framing is opportunistic, not strategic

The register calls the CMS enrollment moratorium "the single strongest framing available for the steering committee" because growth "cannot be bought with new locations."

Two problems. **[EVIDENCED]**
1. **The moratorium is six months from 13 May 2026** — it expires in November 2026, extendable in six-month increments and liftable at any time. A multi-year platform programme cannot be justified by a window that may close before Phase 1 ships. ([ACHC](https://achc.org/2026-cms-home-health-and-hospice-enrollment-moratorium/); [Ropes & Gray](https://www.ropesgray.com/en/insights/alerts/2026/06/cms-home-health-and-hospice-moratoria-update-emerging-guidance-and-enforcement-update))
2. **It is a fraud crackdown.** CMS's own framing is intensified investigation and "advanced data analytics." Citing it as a growth tailwind while simultaneously proposing a LUPA-threshold-proximity capability is, at best, tonally reckless.

### 9.5 Freeing scheduler time does not create clinicians

**[UNTESTED CONCERN, with supporting context]** G1 asserts SOC-capable clinician availability is the binding growth constraint, then proposes to relieve it by reducing *scheduler* workload. Those are different resources. Industry reporting puts the constraint on the clinical side — **more than 4.2 million patients did not receive physician-recommended home health services in 2024**, against structural workforce shortage and turnover that "eats hiring gains as fast as they come" ([HCHB](https://hchb.com/home-health-staffing-shortages-why-time-not-hiring-is-the-real-constraint-in-2026/); [CareVoyant](https://www.carevoyant.com/home-health-blog/home-health-recruitment-trends-2026)). On a per-visit workforce the clinician already controls her own volume: if she wanted more visits, she would already be taking them. Better scheduling does not manufacture a nurse.

---

## 10. Consolidated internal-contradiction register

These are the discrepancies a committee should require reconciled before any further work. All are internal to the proponent's own documents. **[ARITHMETIC / EVIDENCED]**

| # | Item | Register | Workbook ("authoritative") | Gap |
|---|---|---|---|---|
| 1 | Total annual benefit | ~$31M named (~$16M waterfall-only) | **$7.9M** Moderate; $14.3M Hopeful | **2–4×** |
| 2 | Episodic payment periods/yr | 128,000 (derived) | 80,000 (80 × 1,000) | **60%** |
| 3 | Revenue per avoided LUPA | ~$1,200 | $1,400 | 17% |
| 4 | LUPA benefit | $2.2M | $1.12M network | ~2× |
| 5 | Clinician replacement cost | ~$124,000 (research corpus) | $40,000 | **3×** |
| 6 | Loaded scheduler cost | $60,000 used in W1 | Listed in §9 as a **missing input** | Placeholder in headline lever |
| 7 | "81.12% one visit short" | Applied to **all** LUPA periods | Source scope: **subsequent periods only** | Category error |
| 8 | MVP capture | Phase 1 is "**visualization only — no automation**" (DE-03); "the MVP does not build the schedule" | **0.60 of full-product impact** assumed | A tool that changes no assignment cannot deliver 60% of benefits that all come from changed assignments |
| 9 | Cost side | Six named cost bars | None populated anywhere in repo | **No denominator** |

Item 8 deserves emphasis. **[ARITHMETIC]** The MVP capture factor of 0.60 is doing enormous work — it produces $4.7M of the workbook's network MVP number — and it is asserted for a release that the same documents define as *deliberately non-operative*.

---

## 11. Where the proponent is actually right

Stated honestly. These are the parts of the case I could not break, and a committee should preserve them.

**1. The diagnosis is better than the solution.** The whiteboard and constraint register are genuinely high-quality operational discovery. The distinction between *capacity management* and *scheduling* — and the insistence that capacity must be solved first — is almost certainly the correct engineering sequence, and it is a real explanation of why Alabama failed. I could not find a flaw in it.

**2. The "these workflows should not exist" insight is the most valuable thing in the record.** "*We have to be really careful that we're just not reinventing Home Care Home Base*" and "*that workflow shouldn't exist to begin with for the scheduler*" are exactly the right instincts. They argue against the platform, but the proponent said them first and in the proponent's own document.

**3. W5 (Workday↔HCHB PTO) is unambiguously correct and should be done this month.** An existing, paid-for integration is switched off, PTO is hand-keyed, and five of seven nurses in a territory can be approved off the same day. Zero cost, immediate, prevents a real class of capacity failure. No counter-argument exists.

**4. U1 (discipline and role match) is real economics.** Under a fixed 30-day period payment, an appropriate paraprofessional substitution converts directly to margin **and** frees higher-licensed capacity for evaluations. The mechanism is sound and CMS's own claims data supports the visit-weighting logic. My objection is attribution, not validity — DE-08 is a policy default plus a report, not a platform. **The $1.9M is probably real; it is just not the platform's.**

**5. R1 (visits delivered against pending authorisation) is a genuine, structural, unmeasured leak.** The federal condition of participation requires initial assessment within 48 hours of referral, while payer backdating windows run zero to five days and authorisation turnaround often exceeds both. The branch is *structurally forced* to work at risk. The register is right that nobody has ever counted it, and right that it may be the most under-instrumented dollar in the business. **This alone justifies an instrumentation project.**

**6. The payer-rules-at-plan-of-care insight is correct and cheap.** "UHC was never going to give you more auth. We're not creating our plans of care based on the insurance." The data already exists in coordination notes. Surfacing it is high-value and low-complexity, and the whiteboard is right that it is a *patient-care* win as much as a throughput one — abrupt discharges happen because nobody planned against the real visit budget.

**7. The notification storm is a genuine safety finding, independent of ROI.** Generating ~55 mostly non-actionable alerts per scheduler per day trains bulk-clearing, "so the one that mattered gets cleared too." That is a patient-safety argument that stands entirely on its own and should be fixed regardless of what happens to this business case.

**8. §12 "What this case must never claim" is unusually disciplined.** Refusing to claim visit-adding to clear a floor, refusing to build ROI on star ratings, refusing to frame fewer visits as the goal, refusing savings that depend on a manager working weekends. Most business cases I review would have claimed all four. This is a proponent arguing in good faith, and the committee should say so.

**9. §11 anti-double-counting and the §9 pay-model caveat are self-incriminating in the best sense.** The register discloses its own weakest point — that the value thesis may not apply to the majority of the workforce, and that the chosen pilot sites cannot test it. That candour is why this bear case could be written at all, and it should not be punished.

**10. Q1 (value-based purchasing) is real and correctly sized.** The measure set change matters, and OASIS functional measures at 40% of the total performance score are genuinely dose-responsive to visit timing. The 0.5% house convention on $260M ($1.3M) is a defensible, deliberately conservative number. I have no objection to it.

**11. The claim that a data asset is being forgone has merit.** No public dataset on home health authorisation turnaround and denial behaviour exists; federal oversight has asked CMS to begin collecting it; the electronic prior authorisation requirement lands 1 January 2027. Instrumenting authorisation state now is genuinely forward-looking. **[UNTESTED as a dollar value — but sound as a reason to instrument.]**

---

## 12. Verdict and recommendation

**Do not fund the platform.**

**Fund instead, with a hard gate:**

**Phase 0 — 90 days, low six figures, no vendor commitment.**
1. Turn on what is already owned and paid for: Workday↔HCHB PTO integration; HCHB Shift Finder; the pending-auth notification filter. Measure the effect.
2. Make DE-08 (paraprofessional default with explicit opt-out) a policy today, with a monthly exception report. Book the result. That is U1.
3. Surface payer authorisation limits at plan-of-care creation from the coordination-note data that already exists.
4. Resolve the DCS order-approval toggle as a documented risk decision.
5. **Instrument the eleven inputs in §9 of the register** — starting with the pay-model split from internal payroll, and the count and value of visits written off against pending authorisation (R1). Buy the $400 HCS report the same week.
6. Establish the baseline for every "No" in the primary KPI table. Nothing else is fundable until this exists.

**Gate criteria for any Phase 1 platform decision:**
- The register and the workbook reconciled to a single number, with the 2–4× discrepancy explained.
- A populated cost side: licence, integration, internal programme, steward and analyst roles, change management — with a payback period.
- The pay-model split published, and the value case restated for the actual salaried/per-visit mix.
- A pilot design that can **falsify the margin thesis**, at a site where salaried capacity exists — not only at the per-visit sites chosen for adoption comfort.
- A written answer to the enforcement question: whether any LUPA-proximity capability will be built, and if so, under what controls and with what counsel sign-off.
- A named executive commitment, in writing, on what happens when a tenured clinician declines a recommended assignment. If the answer is "nothing," the optimisation benefits must be removed from the case.

**If those six gates are met, this is a reasonable programme with an honest proponent. Until they are, it is a well-researched hypothesis wearing a waterfall chart.**

---

### Sources

- [HHS OIG, A-09-18-03031 — home health claims just above the LUPA threshold](https://oig.hhs.gov/reports/all/2020/cms-could-have-saved-192-million-by-targeting-home-health-claims-for-review-with-visits-slightly-above-the-threshold-that-triggers-a-higher-medicare-payment/)
- [CMS — nationwide six-month hospice and home health enrollment moratoria](https://www.cms.gov/newsroom/press-releases/cms-announces-aggressive-nationwide-crackdown-fraud-six-month-hospice-home-health-agency-enrollment) · [AHA](https://www.aha.org/news/headline/2026-05-13-cms-announces-6-month-enrollment-moratorium-home-health-and-hospice-providers) · [ACHC](https://achc.org/2026-cms-home-health-and-hospice-enrollment-moratorium/) · [Ropes & Gray](https://www.ropesgray.com/en/insights/alerts/2026/06/cms-home-health-and-hospice-moratoria-update-emerging-guidance-and-enforcement-update)
- [HHS OIG Spring 2026 Semiannual Report](https://oig.hhs.gov/documents/sar/11794/Spring_2026_SAR.pdf) · [2026 National Health Care Fraud Takedown](https://oig.hhs.gov/fraud/enforcement/2026-national-health-care-fraud-takedown/) · [Paul Hastings, Healthcare Enforcement Roundup](https://www.paulhastings.com/insights/client-alerts/healthcare-enforcement-roundup-what-providers-need-to-know)
- [MedPAC March 2026, Chapter 8](https://www.medpac.gov/wp-content/uploads/2026/03/Mar26_Ch8_MedPAC_Report_To_Congress_SEC.pdf) · [McKnight's Home Care](https://www.mcknightshomecare.com/news/medpac-to-congress-cut-home-health-payment-rates-by-7-percent-in-2027/) · [Home Health Care News](https://homehealthcarenews.com/2025/12/medpac-to-recommend-7-cut-to-2027-home-health-payment-rate/)
- [Flyvbjerg & Budzier, *Why Your IT Project May Be Riskier Than You Think*](https://doi.org/10.2139/ssrn.2229735) · [arXiv](https://arxiv.org/abs/1304.0265)
- [Artezio — hospital software project failure rates](https://www.artezio.com/pressroom/blog/hospital-software-projects/) · [EHR implementation failure/under-delivery rates](https://topflightapps.com/ideas/ehr-implementation/) · [PMC11507143 — leadership and EHR implementation](https://pmc.ncbi.nlm.nih.gov/articles/PMC11507143/)
- [Prosci — governing ERP benefits beyond go-live (metrics maturity 7% vs 28%)](https://www.prosci.com/blog/governing-erp-benefits-beyond-go-live)
- [PMI — Benefits Realization Management](https://www.pmi.org/learning/thought-leadership/series/benefits-realization) · [KPMG/Cranfield/McKinsey-Oxford figures compiled](https://thinkpieces.stavros.io/posts/how-organizations-consistently-underinvest-in-the-ability-to/) · [Benefit shortfall](https://en.wikipedia.org/wiki/Benefit_shortfall)
- [Deloitte — intelligent automation survey](https://www.deloitte.com/us/en/insights/topics/talent/intelligent-automation-2022-survey-results.html)
- [Bergman et al., schedule volatility and home health nurse turnover — PMC9122113](https://pmc.ncbi.nlm.nih.gov/articles/PMC9122113/) · [Penn LDI summary](https://ldi.upenn.edu/our-work/research-updates/smarter-scheduling-in-home-health-care/)
- [Bae 2024, nurse staffing and work schedules on turnover — systematic review](https://onlinelibrary.wiley.com/doi/abs/10.1111/inr.12849) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/37216655/)
- [Interventions to Reduce Adult Nursing Turnover: A Systematic Review of Systematic Reviews — PMC5725565](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5725565/) · [Newly graduated nurse retention interventions — PMC12907248](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12907248/)
- [Algorithmic management and worker well-being — PMC11672927](https://pmc.ncbi.nlm.nih.gov/articles/PMC11672927/) · [Workers' health under algorithmic management — PMC9859016](https://pmc.ncbi.nlm.nih.gov/articles/PMC9859016/)
- [HCS Home Care Salary & Benefits Report via HHCN — turnover, wages, sign-on bonuses](https://homehealthcarenews.com/2025/11/home-health-worker-retention-improves-as-wages-bonuses-increase-in-2025/) · [HHCN 2020 turnover](https://homehealthcarenews.com/2020/10/home-health-turnover-rate-hits-22-18/)
- [HCHB Smart Scheduling](https://hchb.com/hchb-smart-scheduling/) · [HCHB Smart Scheduling Automation](https://hchb.com/hchb-smart-scheduling-automation/) · [PRWeb release](https://www.prweb.com/releases/homecare-homebase-smart-scheduling-enhances-efficiency-and-continuity-of-care-setting-new-industry-standards-302171671.html)
- [HCHB — home health staffing shortages 2026](https://hchb.com/home-health-staffing-shortages-why-time-not-hiring-is-the-real-constraint-in-2026/) · [CareVoyant — 2026 recruitment trends](https://www.carevoyant.com/home-health-blog/home-health-recruitment-trends-2026)
- [McCreary, *Geriatric Nursing* — independence and flexibility as satisfaction drivers](https://www.sciencedirect.com/science/article/pii/S0029646519300878)
- [McBee Associates — PDGM visit utilization / LUPA one-visit-short analysis](https://mcbeeassociates.com/insights/blog/pdgm-best-practice-turn-to-episode-management-to-drive-efficient-visit-utilization/)

**Internal sources attacked:** `artifacts/business-case-register.md`; `artifacts/reimbursement-research/04-utilization-management-and-margin.md`; `artifacts/reimbursement-research/05-cost-and-labor-economics.md`; `knowledge/business-case-and-kpis.md`; `knowledge/whiteboard-session-2026-08-13.md`; `knowledge/discovery-session.md`; `knowledge/constraint-register.md`; `knowledge/README.md` — all under `C:\Users\chigh\compassus-capacity-pm\agents\compassus-capacity-pm\`.
