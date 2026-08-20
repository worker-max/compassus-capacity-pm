# Utilization Management of Clinician Visits Under PDGM, and How It Drives Home-Health Agency Margin

Research file 04 · CCSI payer research · Compiled 2026-08-18

**How to read this file.** Every figure is labeled. **[VERIFIED]** means the number was pulled from the cited primary or named-industry source on 2026-08-18 and the URL is inline. **[MODELED — ILLUSTRATIVE]** means I built the number; its assumptions are listed immediately beneath it and it must never be presented to a client as an observed benchmark. Where a source is vendor marketing rather than a study or a regulator, I say so.

---

## 1. The mechanism in one paragraph

Under the Patient-Driven Groupings Model, Medicare pays a home health agency a single case-mix-adjusted amount for a 30-day period of care. That amount does not move with the number of visits delivered, with one exception at the bottom (the LUPA threshold) and one exception at the top (the outlier threshold). Between those two points the revenue line is perfectly flat and the cost line rises with every visit. So visit utilization is not a revenue lever at all — it is a pure cost lever, and it is the largest cost lever an agency has. The entire discipline of home-health utilization management exists because of the shape of that payment curve. The clinical risk is that the same flat curve rewards under-service, which is why the counter-evidence in Section 10 has to sit inside the same model as the arithmetic in Section 3.

---

## 2. Visit utilization under PDGM

### 2.1 National averages, traditional Medicare

**[VERIFIED]** MedPAC's March 2026 Report to the Congress, Chapter 8, Table 8-4 — [Mar26_Ch8_MedPAC_Report_To_Congress_SEC.pdf](https://www.medpac.gov/wp-content/uploads/2026/03/Mar26_Ch8_MedPAC_Report_To_Congress_SEC.pdf), published March 2026. Figures are per **full** 30-day period (a period that met or exceeded its LUPA threshold). 2019 services were delivered under 60-day episodes and were recalculated by MedPAC as 30-day periods for comparability.

| In-person visits per full 30-day period | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | Change 2019–2024 |
|---|---|---|---|---|---|---|---|
| **Total** | 10.2 | 9.2 | 8.8 | 8.6 | 8.5 | **8.4** | **−18.0%** |
| Physical, occupational, speech therapy (combined) | 4.9 | 3.9 | 3.9 | 4.0 | 3.9 | **3.8** | −21.5% |
| Skilled nursing | 4.6 | 4.6 | 4.3 | 4.1 | 4.1 | **4.1** | −11.8% |
| Medical social services + home health aide (combined) | 0.8 | 0.7 | 0.6 | 0.5 | 0.5 | **0.5** | −41.6% |
| Total in-person visits, all HHAs (millions) | 99.7 | 81.1 | 76.8 | 69.5 | 66.8 | **65.4** | −34.4% |

**[VERIFIED]** Counting LUPA periods as well as full periods, the average number of in-person visits per 30-day period was **8.3 in 2024**, essentially flat year over year ([MedPAC Ch. 8](https://www.medpac.gov/wp-content/uploads/2026/03/Mar26_Ch8_MedPAC_Report_To_Congress_SEC.pdf), March 2026).

Two structural points matter for a capacity platform. First, the decline came in two distinct phases. In 2020, the first year of PDGM, therapy visits dropped roughly 1.0 visit per period — almost 20 percent — the year PDGM removed therapy volume from the case-mix calculation, and therapy then stayed flat through 2024. Skilled nursing did **not** move in 2020; it drifted down 0.5 visits between 2020 and 2024, for reasons MedPAC explicitly says it cannot attribute to PDGM (staffing shortages and pandemic aftershocks are its candidate explanations). Second, MSW and aide utilization has collapsed by more than 40 percent and is now a rounding error at half a visit per period. Any product that models six disciplines evenly will misrepresent the real distribution.

**[VERIFIED]** CMS's own analysis for the CY2025 rulemaking cycle found average utilization across all disciplines fell 18.9 percent, from 9.86 to 8.0 visits per 30 days. Strategic Healthcare Programs' four-year PDGM retrospective reported total visits down 9.2 percent since PDGM inception, with physical therapy the one discipline that held roughly stable ([SHP, "PDGM after 4 years – No Big Surprises"](https://www.shpdata.com/blog/pdgm-after-4-years-no-big-surprises/), March 28, 2024). The CMS and MedPAC denominators differ slightly (all periods vs. full periods); the direction and magnitude agree.

### 2.2 The causal estimate, isolated from the pandemic

**[VERIFIED]** MedPAC's congressionally mandated evaluation of PDGM (March 2026 report, Chapter 14 — [Mar26_Ch14](https://www.medpac.gov/wp-content/uploads/2026/03/Mar26_Ch14_MedPAC_Report_To_Congress_SEC.pdf)) used interrupted time-series models with severity adjustment to estimate what utilization would have been *without* PDGM. The unit of analysis is the **home health stay** (linked consecutive claims), not the 30-day period, so these numbers are larger than those in Section 2.1.

| Visits per FFS stay, 2023 | With PDGM | Without PDGM | Difference | % |
|---|---|---|---|---|
| **Total** | **15.9** | **18.8** | −2.9 | **−15.3%** |
| Nursing | 6.4 | 7.1 | −0.7 | −9.8% |
| Therapy | 8.8 | 11.2 | −2.4 | −21.3% |
| Home health aide | 0.6 | 0.3 | +0.2 | +75.6% |

The effect was consistent across every beneficiary subgroup MedPAC tested — urban vs. rural, race, age, dual-eligibility status, and clinical condition — landing between −10.8 percent and −19.1 percent, all statistically significant. Knee (−19.1%), stroke (−18.2%), and neurodegenerative conditions (−18.1%) took the largest cuts. Dual-eligible and low-income-subsidy beneficiaries saw a *smaller* reduction (−11.6%) than others (−16.4%).

MedPAC is careful here and so should we be: nursing visits fell 0.7 per stay even though PDGM never changed how nursing was paid, which means some unknown share of the therapy decline is also attributable to non-PDGM factors (staffing, pandemic) rather than to a payment response.

### 2.3 High performers versus the average

There is no published, credible national distribution of visits-per-period by agency percentile. What exists is the **margin** distribution, which is the closest available proxy because visit cost is the dominant controllable input.

**[VERIFIED]** In 2024 the FFS Medicare margin for freestanding HHAs ranged from **5.7 percent at the 25th percentile to 31.0 percent at the 75th percentile**, against an average of 21.2 percent ([MedPAC Ch. 8](https://www.medpac.gov/wp-content/uploads/2026/03/Mar26_Ch8_MedPAC_Report_To_Congress_SEC.pdf), March 2026). The largest volume quintile earned 23.2 percent; the smallest earned 14.4 percent.

**[MODELED — ILLUSTRATIVE]** Working backwards from that spread, a 75th-percentile agency is operating roughly **1.5 to 2.0 fewer visits per 30-day period** than a 25th-percentile agency at comparable case mix.
*Assumptions:* the 25.3-point margin gap between quartiles is driven principally by visit volume rather than by case-mix or wage-index differences; blended fully-allocated cost per visit of ~$193 (derived in Section 3.2); average period revenue of ~$2,057. 25.3% × $2,057 = $520 of margin difference ÷ $193 ≈ 2.7 visits at fully-allocated cost, or ~1.5–2.0 visits once fixed overhead is held constant. This is a reasoned inference, **not** an observed benchmark, and should be validated against client data before it is asserted anywhere.

### 2.4 Traditional Medicare versus Medicare Advantage

Discipline-level MA visit utilization is not published. What is published:

- **[VERIFIED]** Medicare Advantage penetration held at **55.4 percent** of the Medicare population in 2025, the first flat year in a decade after averaging +2.1 points annually since 2017 ([Trella Health 2025 Post-Acute Care Industry Trend Report](https://www.trellahealth.com/newsroom/press-release/trella-health-releases-2025-post-acute-care-industry-trend-report-highlighting-continued-medicare-advantage-growth-and-shifts-in-care-utilization/), July 2025).
- **[VERIFIED]** In 2025, home health admissions rose in every quarter year over year for the first time in six years, but FFS admissions were declining — the incremental volume came from MA enrollees (same Trella report).
- **[VERIFIED]** MedPAC computes utilization trends from OASIS data covering both MA and FFS, but reports visits-per-period only for FFS. It does not publish an MA visits-per-period figure ([MedPAC Ch. 8](https://www.medpac.gov/wp-content/uploads/2026/03/Mar26_Ch8_MedPAC_Report_To_Congress_SEC.pdf), endnote 5, March 2026).

The operationally important asymmetry is contractual, not clinical: most MA home health contracts pay **per visit**, not per 30-day period. That inverts the entire margin mechanism described in this file. Under a per-visit MA contract the incremental visit carries *positive* contribution; under PDGM it carries *negative* contribution. A branch scheduling platform that applies one utilization policy across a mixed book will systematically destroy value on one side or the other. **Payer type must be a first-class field in the scheduling model, not a reporting attribute.**

---

## 3. The margin arithmetic

### 3.1 Verified payment inputs, CY2026

**[VERIFIED]** All figures from the CY2026 HH PPS final rule (CMS-1828-F, released November 28, 2025, effective January 1, 2026), as summarized in the [Illinois Health and Hospital Association CY2026 HH PPS Final Rule Summary](https://www.team-iha.org/getmedia/26da6c77-bc88-4b05-baf3-95edcf481308/CY-2026-Medicare-HH-PPS-FR-Rule-Summary.pdf) (December 2025) and corroborated by [CHAP](https://chapinc.org/blog-news/final-cy-2026-hh-pps-payment-update-rule-posted/) and the [CMS fact sheet](https://cms.gov/newsroom/fact-sheets/calendar-year-cy-2026-home-health-prospective-payment-system-final-rule-cms-1828-f).

| CY2026 payment parameter | Value |
|---|---|
| National standardized 30-day period rate (QRP-compliant) | **$2,038.22** |
| Same, CY2025 | $2,057.35 (−0.93% year over year) |
| Market basket update | +3.2% |
| Productivity adjustment | −0.8 pp |
| Permanent behavior adjustment | −1.023% |
| Temporary adjustment (one year only) | −3.00% |
| Wage index / labor-share budget neutrality | +0.25% |
| Case-mix recalibration budget neutrality | +0.52% |
| Labor-related share | 74.9% |
| Outlier fixed-dollar-loss (FDL) ratio | 0.37 |
| Number of PDGM payment groups | 432 |
| LUPA thresholds | 2 to 5 visits, set at the 10th percentile of visits in each group |
| Aggregate CY2026 payment impact | −$220M (−1.3%) vs. CY2025 |

**Caution — a common error in circulation.** Several summaries quote **$1,933.61** as the CY2026 base rate. That is the *proposed* rate from the July 2025 proposed rule, which carried a −6.01% cut. CMS finalized a far smaller reduction. The correct final figure is **$2,038.22**.

**[VERIFIED]** CY2026 national per-visit amounts. These pay LUPA periods and drive the outlier cost calculation.

| Discipline | CY2025 per-visit | **CY2026 per-visit** | CY2026 with LUPA add-on | Add-on factor |
|---|---|---|---|---|
| Home health aide | $78.20 | **$80.12** | n/a | — |
| Medical social services | $276.85 | **$283.64** | n/a | — |
| Occupational therapy | $190.08 | **$194.74** | $335.69 | 1.7238 |
| Physical therapy | $188.79 | **$193.42** | $313.82 | 1.6225 |
| Skilled nursing | $172.73 | **$176.96** | $304.37 | 1.7200 |
| Speech-language pathology | $205.22 | **$210.25** | $351.03 | 1.6696 |

The LUPA add-on applies to the first OT, PT, SN, or SLP visit in a LUPA period that is the only period, or the initial period in a sequence of adjacent periods.

### 3.2 Verified cost anchor

There is no reliable public source for home-health cost per visit **by discipline**. The consultant houses that hold it (SimiTree Compass, Forvis Mazars, HealthPivots, McBee) sell it. What can be derived cleanly from a single authoritative source is the blended, fully-allocated figure.

**[VERIFIED]** MedPAC, March 2026, Chapter 8:

- Medicare FFS payment per in-person visit: **$180 (2019) → $245 (2024)**, growing 7.2% annually 2019–2023 and 3.3% in 2024
- Average payment per full 30-day period, 2024: **$2,057**
- FFS Medicare margin, freestanding HHAs, 2024: **21.2%**
- Cost per full 30-day period rose just **0.2% in 2024**, after ~3.4% annual growth in 2022 and 2023 and a −2.9% decline in 2021. MedPAC attributes the 2024 flatness to rising cost per visit being offset by the reduction in visits per period.

**[MODELED — ILLUSTRATIVE] Blended fully-allocated cost per visit, 2024: ~$193.**
*Derivation:* $245 payment per visit × (1 − 0.212 margin) = $193.
*Cross-check via a second route:* $2,057 payment per full period × (1 − 0.212) = $1,621 cost per period ÷ 8.4 visits = $193. The two routes agree.
*Assumptions and limits:* the 21.2% margin is computed across all FFS revenue including LUPA and outlier periods, while $2,057 is payment per *full* period, so the denominators are not perfectly identical; freestanding agencies only (hospital-based HHAs ran a −15.2% FFS margin in 2024 and would produce a materially higher cost figure); no wage-index adjustment.

**[MODELED — ILLUSTRATIVE] Fully-allocated cost per full 30-day period, CY2026: ~$1,651.**
*Derivation:* anchored directly to MedPAC's published projection of a **19 percent** FFS Medicare margin for freestanding HHAs in 2026. $2,038.22 × (1 − 0.19) = $1,651. Using MedPAC's own forward projection rather than an independent cost-trend assumption keeps the model tied to a published number rather than to my inflation guess.

### 3.3 Direct cost per visit by discipline

**[VERIFIED]** Wage inputs, BLS Occupational Employment and Wage Statistics, **May 2025** national data — [Table 1](https://www.bls.gov/news.release/ocwage.t01.htm), U.S. Bureau of Labor Statistics.

| Occupation | Employment | Mean hourly | Mean annual | Median hourly |
|---|---|---|---|---|
| Registered nurses | 3,379,720 | **$48.76** | $101,420 | $46.90 |
| Licensed practical / vocational nurses | 648,410 | **$32.24** | $67,050 | $30.96 |
| Physical therapists | 267,330 | **$50.62** | $105,280 | $49.40 |
| Physical therapist assistants | 112,430 | **$33.04** | $68,730 | $32.88 |
| Occupational therapists | 162,450 | **$48.69** | $101,280 | $48.24 |
| Occupational therapy assistants | 51,290 | **$33.99** | $70,710 | $34.76 |
| Speech-language pathologists | 183,390 | **$47.20** | $98,170 | $47.05 |
| Healthcare social workers | 187,630 | **$34.51** | $71,790 | $32.63 |
| Home health and personal care aides | 4,305,810 | **$17.36** | $36,120 | $17.21 |

**[MODELED — ILLUSTRATIVE] Direct variable cost of one home health visit, by discipline.**

*Assumptions, all stated explicitly:*

1. Productive day of 8 hours, inclusive of travel and documentation.
2. Visits per clinician-day: SN 5.5; PT/OT 6.0; SLP 5.0; MSW 4.0; aide 6.0. These are common operating targets, not a published benchmark.
3. Labor burden multiplier of **1.30** applied to the BLS mean hourly wage, covering employer payroll taxes and benefits.
4. Travel and supplies allowance of **$17 per visit** (approximately 25 miles of reimbursed mileage plus routine consumables).
5. National mean wages, no wage-index or local-market adjustment.
6. This is **direct variable cost only** — it excludes G&A, intake, QA and coding, clinical management, EMR, and unallocated overhead.

| Discipline / role | Hours per visit | Burdened labor | + Travel & supplies | **Direct cost per visit** |
|---|---|---|---|---|
| Skilled nursing — RN | 1.45 | $92 | $17 | **~$109** |
| Skilled nursing — LPN | 1.45 | $61 | $17 | **~$78** |
| Physical therapy — PT | 1.33 | $88 | $17 | **~$105** |
| Physical therapy — PTA | 1.33 | $57 | $17 | **~$74** |
| Occupational therapy — OT | 1.33 | $84 | $17 | **~$101** |
| Occupational therapy — COTA | 1.33 | $59 | $17 | **~$76** |
| Speech-language pathology | 1.60 | $98 | $17 | **~$115** |
| Medical social work | 2.00 | $90 | $17 | **~$107** |
| Home health aide | 1.33 | $30 | $17 | **~$47** |

**Sanity check against the verified anchor.** A national-mix period (from Section 2.1: SN 4.1, therapy 3.8, MSW/aide 0.5) carries about **$874** of direct cost under this model. Fully-allocated cost is ~$1,651. Direct care is therefore **53 percent** of total cost, and overhead is 47 percent — squarely inside the normal home-health cost structure. That internal consistency is the strongest available evidence that the model is calibrated correctly, given no discipline-level cost benchmark is public.

### 3.4 The contribution-margin curve — the core result

**[MODELED — ILLUSTRATIVE, built entirely on verified CY2026 rates]**

Setup: one 30-day period, CY2026, case-mix weight 1.00, wage index 1.00, initial period in a sequence, **LUPA threshold of 4 visits** (mid-range of the 2-to-5 band). Direct costs from Section 3.3; fully-allocated period cost of $1,651 from Section 3.2.

| Visit # | Discipline | Cumulative revenue | **Marginal revenue** | Marginal direct cost | **Marginal contribution** |
|---|---|---|---|---|---|
| 1 | SN (LUPA add-on applies) | $304.37 | +$304.37 | $109 | +$195 |
| 2 | SN | $481.33 | +$176.96 | $109 | +$68 |
| 3 | PT | $674.75 | +$193.42 | $105 | +$88 |
| **4** | **PT — crosses threshold** | **$2,038.22** | **+$1,363.47** | $105 | **+$1,258** |
| 5 | SN | $2,038.22 | **$0.00** | $109 | **−$109** |
| 6 | SN | $2,038.22 | **$0.00** | $109 | **−$109** |
| 7–15 | any | $2,038.22 | **$0.00** | ~$100 each | **~−$100 each** |
| 16 | SN — outlier begins | $2,069.42 | +$31.20 | $109 | −$78 |

**Outlier math.** The FDL amount is 0.37 × $2,038.22 = **$754.14**. The outlier threshold is the period payment plus the FDL = **$2,792.36** of imputed cost, where imputed cost is computed using the national per-visit amounts (subject to an 8-hour/32-unit per-day cap summed across disciplines). At the SN per-visit rate of $176.96 that requires **15.8 visits**. The 16th SN visit is the first to earn anything at all, and it earns 80 percent of the excess — about $31. Outlier payments are capped at 2.5 percent of aggregate national HH PPS payments and at 10 percent of any single agency's payments.

**The finding.** In a period with a 4-visit threshold, **visits 5 through 15 generate exactly zero incremental revenue.** Eleven visits, roughly $1,100 of direct cost, no payment whatsoever. Meanwhile visit number 4 is worth $1,363. The payment curve is a step function with a cliff at the threshold and a plateau eleven visits wide. Everything in Sections 4 through 8 follows from this one shape.

**Period P&L, national-mix period, CY2026:**

| Line | Amount |
|---|---|
| Revenue (CY2026 base rate, CMW 1.00) | $2,038.22 |
| Direct visit cost, 8.4 visits at national mix | −$874 |
| **Contribution margin** | **$1,164 (57.1%)** |
| Allocated overhead / G&A | −$777 |
| **Operating margin** | **$387 (19.0%)** — reconciles to MedPAC's 2026 projection by construction |

**What one extra visit costs:**

| | Baseline | +1 SN visit |
|---|---|---|
| Visits | 8.4 | 9.4 |
| Revenue | $2,038.22 | $2,038.22 |
| Direct cost | $874 | $983 |
| Operating margin | $387 | **$278** |
| Margin % | 19.0% | **13.6%** |

**One additional nursing visit per period reduces period operating profit by 28 percent.** That is the single most decision-relevant number in this file. The symmetry holds in reverse: one visit removed adds roughly 28 percent to period profit — which is exactly why the guardrails in Section 10 are not optional.

**At scale [MODELED — ILLUSTRATIVE]:**

| Agency size (30-day periods per year) | Revenue at $2,038 | Cost of +1 visit/period | Operating profit before | Operating profit after |
|---|---|---|---|---|
| 2,000 (single branch) | $4.08M | $218,000 | $774,000 | $556,000 |
| 10,000 (multi-branch) | $20.4M | $1.09M | $3.87M | $2.78M |
| 40,000 (regional) | $81.5M | $4.36M | $15.5M | $11.1M |

**[MODELED, from a verified base]** Nationally: FFS Medicare paid $16.0 billion for home health in 2024 at an average $2,057 per full period ([MedPAC Ch. 8](https://www.medpac.gov/wp-content/uploads/2026/03/Mar26_Ch8_MedPAC_Report_To_Congress_SEC.pdf)), implying roughly **7.8 million 30-day periods**. One additional visit per period across the industry would consume approximately **$780 million** in direct clinical cost and generate zero additional revenue.

---

## 4. LUPA economics

### 4.1 The national picture

**[VERIFIED]** In 2024, **about 7 percent of 30-day periods were paid as LUPAs**; the remaining 93 percent were full periods ([MedPAC Ch. 8](https://www.medpac.gov/wp-content/uploads/2026/03/Mar26_Ch8_MedPAC_Report_To_Congress_SEC.pdf), March 2026). This is the authoritative national LUPA rate and it should be the reference point, rather than the various low single-digit figures circulating in vendor material.

**[VERIFIED]** LUPA thresholds are set at the 10th percentile of visits within each of the 432 payment groups, floored at 2 visits and capped at 5. For CY2026, recalibrated using CY2024 claims: **389 groups unchanged, 15 groups up one visit, 28 groups down one visit** ([IHA CY2026 rule summary](https://www.team-iha.org/getmedia/26da6c77-bc88-4b05-baf3-95edcf481308/CY-2026-Medicare-HH-PPS-FR-Rule-Summary.pdf), December 2025). The 6-visit thresholds that existed early in PDGM were eliminated in CY2023 ([SHP](https://www.shpdata.com/blog/pdgm-after-4-years-no-big-surprises/), March 2024).

The 10th-percentile construction deserves attention in a multi-year model. Thresholds are recalibrated annually against the industry's own behavior. As agencies drive utilization down, the 10th percentile falls with them and thresholds ratchet downward — which is why 28 groups dropped a visit for CY2026 while only 15 rose. **Industry-wide utilization reduction is partially self-limiting at the LUPA boundary**, and a capacity model projecting several years forward should not treat thresholds as fixed.

### 4.2 The cliff, with CY2026 numbers

**[MODELED — ILLUSTRATIVE, built on verified CY2026 rates]** Case-mix weight 1.00, wage index 1.00, LUPA threshold 4 visits, planned mix SN 2 + PT 2.

**Scenario A — initial period in a sequence, one visit missed (3 delivered):**

| | Amount |
|---|---|
| SN visit 1, with LUPA add-on (1.7200) | $304.37 |
| SN visit 2 | $176.96 |
| PT visit 1 | $193.42 |
| **Total LUPA payment** | **$674.75** |
| Full period payment had the 4th visit occurred | $2,038.22 |
| **Revenue lost** | **−$1,363.47** |
| Direct cost avoided (one PT visit not made) | +$105 |
| **Net contribution destroyed** | **−$1,258** |

**Scenario B — subsequent (non-initial) period, no add-on applies:**

| | Amount |
|---|---|
| SN 2 × $176.96 | $353.92 |
| PT 1 × $193.42 | $193.42 |
| **Total LUPA payment** | **$547.34** |
| Full period payment had the 4th visit occurred | $2,038.22 |
| **Revenue lost** | **−$1,490.88** |
| Direct cost avoided | +$105 |
| **Net contribution destroyed** | **−$1,386** |

Subsequent-period LUPAs are worse, because the add-on that partially cushions an initial LUPA is unavailable. Under PDGM the second 30-day period is both where LUPAs concentrate and where the loss per event is largest.

**[VERIFIED]** McBee's analysis of CMS PDGM claims found that **81.12 percent of subsequent-period LUPAs were exactly one visit short of the threshold**, and reported a correlation between lower LUPA rates, lower average visit counts, and higher star ratings ([McBee Associates, "PDGM Visit Utilization Best Practices using Episode Management Strategies"](https://mcbeeassociates.com/insights/blog/pdgm-best-practice-turn-to-episode-management-to-drive-efficient-visit-utilization/)). McBee also describes the characteristic PDGM failure pattern directly: the first 30-day period is heavily scheduled with disciplines and visits, while the second often becomes a LUPA with a single visit or a non-billable period with none — because the plan of care was built around a 60-day comprehensive assessment but is executed against a 30-day payment clock.

That correlation is the most important single finding in the LUPA literature and it should be read carefully: **low LUPA rate and low visit count travel together.** Agencies that manage utilization well do not LUPA more; they LUPA less, because they schedule deliberately rather than reactively. The two goals are not in tension.

**[MODELED — ILLUSTRATIVE] Expected annual LUPA leakage, 10,000-period agency:**

| Step | Value | Basis |
|---|---|---|
| 30-day periods per year | 10,000 | agency scale assumption |
| LUPA rate at national average | 7% → 700 periods | MedPAC 2024 **[VERIFIED]** |
| Share one visit short of threshold | 81% → 567 periods | McBee **[VERIFIED, subsequent periods]** |
| Share of those clinically avoidable | 50% → 284 periods | **assumption — no published basis** |
| Average cliff per event | ~$1,400 | Scenarios A/B above |
| **Annual recoverable revenue** | **~$397,000** | product of the above |

Every input except the avoidability share is sourced. That one assumption drives the sensitivity: at 25 percent avoidable the figure is ~$199,000; at 75 percent, ~$596,000. Do not present the midpoint without the range.

### 4.3 The compliance line

This is where a scheduling platform can create genuine legal exposure for a client, so it needs to be stated precisely.

**[VERIFIED]** In July 2020 the HHS Office of Inspector General published **report A-09-18-03031**, *CMS Could Have Saved $192 Million by Targeting Home Health Claims for Review With Visits Slightly Above the Threshold That Triggers a Higher Medicare Payment* ([oig.hhs.gov](https://oig.hhs.gov/reports/all/2020/cms-could-have-saved-192-million-by-targeting-home-health-claims-for-review-with-visits-slightly-above-the-threshold-that-triggers-a-higher-medicare-payment/), issued and posted 07/22/2020). Findings:

- OIG sampled 120 claims with 5, 6, or 7 visits in a 60-day episode, drawn from $1.25 billion in 2017 payments.
- **25 of 120 (21 percent) did not comply with Medicare requirements** — 14 improperly paid for part of the episode, 11 for the full episode. Identified overpayments in the sample: $41,613.
- Extrapolated national overpayment: **$191.8 million** for the audit period.
- OIG's stated rationale for the audit: "Because of the large payment increase starting with the fifth visit, HHAs have an incentive to improperly bill claims with visits slightly above the LUPA threshold."
- OIG noted that **20 of the 25 non-compliant claims would still have been non-compliant under PDGM's variable 2-to-6-visit thresholds**.
- CMS concurred with all three recommendations — including that MACs perform data analysis and risk assessments of claims with visits slightly above the applicable LUPA threshold and **target those claims for additional review**. All three recommendations are marked closed-implemented (the second closed 08/09/2021).

**The operative distinction.** OIG did not find that agencies were fabricating visits. It found that a fifth of claims sitting just above the threshold failed medical-necessity or coding review on independent medical review. The regulatory posture that follows is unambiguous: *claims clustered immediately above the LUPA threshold are a designated targeting signal for contractor review.* An agency whose distribution of visits-per-period spikes at the threshold has painted a target on itself, regardless of intent.

That produces a clean design rule for any product in this space:

| Defensible | Indefensible |
|---|---|
| Flagging at admission that an ordered plan of care sits at or below the LUPA threshold, so the clinician can reassess whether ordered frequency matches assessed need | Recommending "add one visit" to clear a threshold |
| Surfacing that a missed visit has put a period below threshold, so the missed visit can be **rescheduled** — restoring care that was already ordered | Scheduling a visit whose clinical purpose is threshold clearance |
| Routing an order-change request to the practitioner when the clinician's assessment supports a different frequency | Changing frequency in the system without a practitioner order |
| Reporting LUPA rate as an outcome of scheduling reliability | Reporting LUPA rate as a target to be minimized at any cost |
| Monitoring the agency's own distribution of visits-per-period for a spike at the threshold, as a self-audit signal | Ignoring that distribution because each individual claim looks defensible |

**[VERIFIED]** The plan of care must specify "the frequency and duration of visits to be made" (42 CFR § 484.60(a)(2)(iv)); it must be reviewed and revised "no less frequently than once every 60 days" (§ 484.60(c)(1)); and orders may be accepted "only by personnel authorized to do so by applicable state laws" (§ 484.60(b)(3)) ([Cornell LII, 42 CFR § 484.60](https://www.law.cornell.edu/cfr/text/42/484.60)). **Frequency is a physician order. Software may prompt a change; it may never make one.**

One asymmetry worth naming: the enforcement literature on *under*-service is thinner than that on over-service, but it is not absent. Failure to deliver the ordered frequency is a condition-level survey exposure under § 484.60 and a false-claims exposure, because the agency accepted payment for a period of care it did not furnish as ordered.

---

## 5. Front-loading

### 5.1 What the evidence actually says

**[VERIFIED]** The foundational review is O'Connor et al., *Frontloading and Intensity of Skilled Home Health Visits: A State of the Science* ([PMC4532304](https://pmc.ncbi.nlm.nih.gov/articles/PMC4532304/)). Key content:

- **The operational definition** most commonly used comes from Rogers et al. (2007): **60 percent of planned skilled nursing visits delivered within the first two weeks** of the home health episode.
- **Rogers et al. (2007)**, prospective descriptive, 246 heart-failure and 84 diabetic patients: front-loaded HF patients had a **15.8 percent 60-day rehospitalization rate versus 39.4 percent** for those not front-loaded (p < .001). **Front-loading was not effective for the diabetic cohort.**
- **Markley et al. (2012)**, prospective cohort across 29 agencies, 5 hospitals and multiple SNFs: 88 percent of participating agencies reported improved 30-day readmission rates.
- **Intensity is not monotonic.** The review found **1–1.99 visits per week superior to higher frequencies for rehospitalization reduction**; *lower* nursing intensity associated with better ADL improvement; and higher intensity (1.51–8.17 visits/week) better only for dyspnea management.

That last point is the one most often lost. The evidence supports **early** visits, not **many** visits. Front-loading is a redistribution of a fixed visit budget toward the front of the period — not an increase in the budget.

**[VERIFIED]** On timing of the first visit specifically:

- Patients whose home health care was delayed had **12 percent higher odds** of rehospitalization or ED visit than those receiving timely care; among patients first seen **8–14 days after discharge, the odds of rehospitalization were four times greater** than among those seen within two days ([AJMC, "After Hospital Discharge, Slow Home Health Care Initiation Increases Risk of Rehospitalization"](https://www.ajmc.com/view/after-hospital-discharge-slow-home-health-care-initiation-increases-risk-of-rehospitalization); underlying study indexed at [PubMed 35931136](https://pubmed.ncbi.nlm.nih.gov/35931136/), 2022).
- For sepsis survivors, 30-day rehospitalization was **7 percentage points lower — a 41 percent relative reduction** — where the patient received a home health nursing visit within 2 days of discharge, at least one further nursing visit in week 1, and outpatient provider follow-up within 7 days.
- The condition-specific effect on 30-day readmission is documented in ["Impact of frontloading of skilled nursing visits on the incidence of 30-day hospital readmission"](https://www.sciencedirect.com/science/article/abs/pii/S0197457214000640), *Applied Nursing Research* (Elsevier).
- **[VERIFIED]** A growing body of evidence indicates that hospitalization among geriatric skilled home health recipients is most likely to occur **within the first two weeks** of the episode (O'Connor et al., PMC4532304). That is why the front two weeks are the leverage point.

### 5.2 The recommended distribution, and who says so

**[VERIFIED]** McBee's stated best practice: **front-load the episode, schedule visits for the entire episode of care up front, then taper as discharge approaches.** Its clinical rationale is to give the patient extra support during "the fragile first seven to 10 days post-acute," then move to discharge planning as the patient stabilizes ([McBee](https://mcbeeassociates.com/insights/blog/pdgm-best-practice-turn-to-episode-management-to-drive-efficient-visit-utilization/)). McBee also recommends that the case manager designate a **lead discipline based on the dominant clinical goal** — if falls risk dominates, PT leads and is heaviest early, while RN may enter at low frequency and taper *up* as PT tapers down.

**[VERIFIED]** Timely Initiation of Care (CBE #0526) is a CMS Home Health Quality Reporting Program measure for CY2026 ([IHA CY2026 rule summary](https://www.team-iha.org/getmedia/26da6c77-bc88-4b05-baf3-95edcf481308/CY-2026-Medicare-HH-PPS-FR-Rule-Summary.pdf), December 2025). First-visit timing is a regulated quality metric, not merely an operating preference.

**[MODELED — ILLUSTRATIVE] A defensible target distribution for a 30-day period at 8–9 total visits:**

| Window | Share of period visits | Grounding |
|---|---|---|
| Days 1–2 | first skilled visit delivered | 4× rehospitalization odds if delayed to days 8–14 **[VERIFIED]** |
| Days 1–7 | ~40% | fragile post-acute window, McBee **[VERIFIED]**; clears most LUPA thresholds by day 7 |
| Days 1–14 | ~60% | Rogers front-loading definition **[VERIFIED]**; highest-risk hospitalization window **[VERIFIED]** |
| Days 15–30 | ~40%, tapering | discharge planning as patient stabilizes, McBee **[VERIFIED]** |

*Assumption:* that the two-week, 60-percent definition, derived from 60-day episodes, transfers to a 30-day period. It is a reasonable transfer but it is a transfer, not a finding.

### 5.3 Why front-loading is simultaneously a margin lever

Front-loading pays three ways and costs nothing extra:

1. **LUPA immunity.** If the threshold is cleared in week 1, no week-3 or week-4 cancellation can convert the period to a LUPA. Given that 81 percent of subsequent-period LUPAs are one visit short, this is the highest-leverage single change available to most agencies. **[VERIFIED premise, modeled conclusion]**
2. **Rehospitalization avoidance.** A rehospitalization during the period ends the period, forfeits the remaining planned care, and scores against the HHVBP claims-based acute-care-hospitalization measure (Section 10.4).
3. **Earlier stabilization and discharge.** Faster stabilization shortens length of stay, which reduces total periods per patient — but note this cuts *revenue* as well as cost. **Front-loading is only a margin strategy inside a branch that is at or near capacity and can refill the freed slot with a new admission.** In an under-referred branch it is purely a quality strategy. That distinction belongs in the platform's logic, not just its marketing.

---

## 6. Discipline and role optimization

### 6.1 Why this is the second-largest lever

**[VERIFIED]** MedPAC names it explicitly as a mechanism agencies used to hold cost flat through PDGM: "in the post-PDGM era HHAs could have expanded their use of lower-cost staff, such as by using licensed practical nurses or therapy assistants in the place of registered nurses or physical, occupational and speech therapists, respectively" ([MedPAC Ch. 14](https://www.medpac.gov/wp-content/uploads/2026/03/Mar26_Ch14_MedPAC_Report_To_Congress_SEC.pdf), March 2026). MedPAC offers this as a leading explanation for why cost per 30-day period rose only 0.2 percent in 2024 despite rising wages.

Under a fixed period payment, revenue is identical whether an RN or an LPN makes the visit. The entire wage differential falls straight to contribution margin.

### 6.2 Wage differentials and modeled savings

**[VERIFIED]** wage ratios from BLS May 2025 (Section 3.3), combined with **[MODELED]** per-visit costs:

| Substitution | Mean hourly | Ratio to senior role | **[MODELED] direct cost per visit** | **Saving per visit** |
|---|---|---|---|---|
| RN → LPN | $48.76 → $32.24 | 66% | $109 → $78 | **$31 (28%)** |
| PT → PTA | $50.62 → $33.04 | 65% | $105 → $74 | **$31 (30%)** |
| OT → COTA | $48.69 → $33.99 | 70% | $101 → $76 | **$25 (25%)** |
| RN → aide (personal care tasks only) | $48.76 → $17.36 | 36% | $109 → $47 | **$62 (57%)** |

**[MODELED — ILLUSTRATIVE] Impact at agency scale.** 10,000 periods × 8.4 visits = 84,000 visits per year. Skilled nursing is 4.1 of 8.4 visits = ~41,000 SN visits. Shifting SN mix from 10 percent LPN to 40 percent LPN moves 12,300 visits at $31 saved = **~$381,000 per year**, on revenue of $20.4M — roughly **1.9 margin points from staffing mix alone**. The equivalent shift in therapy (3.8 visits/period = ~38,000 visits, PTA/COTA share moving from 20% to 50%) yields roughly **$350,000**, another 1.7 points.
*Assumptions:* the current-mix percentages are illustrative placeholders — the real starting mix must come from client data; assumes every substituted visit is clinically appropriate for the assistant's scope; ignores recruitment difficulty and any productivity difference between roles; ignores the supervisory overhead quantified below.

### 6.3 The rules that bound the lever

**[VERIFIED] What cannot be substituted.**

- **The initial assessment visit** must be conducted by a registered nurse, and must occur within 48 hours of referral, within 48 hours of the patient's return home, or on the practitioner-ordered start-of-care date — 42 CFR § 484.55(a)(1). Where rehabilitation therapy (PT, OT, or SLP) is the **only** service ordered, an appropriate rehabilitation professional may perform it — § 484.55(a)(2).
- **The comprehensive assessment** must be completed "in a timely manner, consistent with the patient's immediate needs, but no later than 5 calendar days after the start of care" — § 484.55(b)(1) — and **must be completed by a registered nurse** — § 484.55(b)(2) — with the same therapy-only exception at § 484.55(b)(3). ([Cornell LII, 42 CFR § 484.55](https://www.law.cornell.edu/cfr/text/42/484.55))
- Because OASIS collection is bound to the comprehensive assessment, **the single most expensive and most payment-consequential visit in the entire period is not substitutable to an LPN or an assistant.** Case-mix group assignment, functional impairment level, and comorbidity adjustment all flow from it. An agency that squeezes RN capacity too hard creates a bottleneck precisely at the visit that determines the period's revenue.

**[VERIFIED] Supervision requirements.**

- **LPN**: "furnishes services under the supervision of a qualified registered nurse" — 42 CFR § 484.115(e); "Nursing services are provided under the supervision of a registered nurse" — § 484.75(c)(1).
- **PTA and OTA**: "Rehabilitative therapy services are provided under the supervision of an occupational therapist or physical therapist" — § 484.75(c)(2). Qualifications at § 484.115(g) and (i) require graduation from an ACOTE- or CAPTE-accredited program, passage of the national examination, and state licensure, registration, or certification where applicable. ([Cornell LII, § 484.75](https://www.law.cornell.edu/cfr/text/42/484.75); [§ 484.115](https://www.law.cornell.edu/cfr/text/42/484.115))
- **Home health aide, patient receiving skilled services**: a registered nurse or other appropriate skilled professional familiar with the patient, the plan of care, and the written patient care instructions "must complete a supervisory assessment of the aide services being provided no less frequently than **every 14 days**" — § 484.80(h)(1)(i)(A).
- **Home health aide, patient not receiving skilled services**: "The registered nurse must make an onsite, in person visit **every 60 days** to assess the quality of care and services provided by the home health aide" — § 484.80(h)(2)(i)(A).
- **Annual** onsite visit to observe and assess each aide performing care — § 484.80(h)(1)(iv); **semi-annual** onsite observation for non-skilled care — § 484.80(h)(2)(ii).
- Aide training: at least **75 hours** of classroom and supervised practical training — § 484.80(b)(1); at least **12 hours** of in-service training per 12-month period — § 484.80(d). ([Cornell LII, § 484.80](https://www.law.cornell.edu/cfr/text/42/484.80))

**The hidden cost of aide substitution.** The 14-day RN supervisory assessment is real RN time that is not itself a separately-payable skilled visit unless a skilled service is also furnished during it. A scheduling model that books an aide visit at $47 without carrying the recurring supervisory load will overstate the saving. For a patient receiving aide services across a full 30-day period, budget roughly **two supervisory touches** into that patient's cost.

**Assistants cannot do everything.** PTAs and COTAs may not perform the initial evaluation, establish or modify the plan of care, or perform the discharge assessment; those remain with the licensed therapist. A branch that pushes assistant utilization too high creates a therapist bottleneck at exactly the evaluation and discharge points that gate admissions and throughput. **That is a capacity-planning constraint, not merely a compliance one**, and it is the sort of second-order effect a scheduling platform is uniquely positioned to model.

---

## 7. Utilization management practices at well-run agencies

### 7.1 What the regulation requires

**[VERIFIED]** 42 CFR § 484.60 ([Cornell LII](https://www.law.cornell.edu/cfr/text/42/484.60)):

- § 484.60(a)(2)(iv) — the individualized plan of care must specify **"the frequency and duration of visits to be made."**
- § 484.60(a)(1) — where the plan cannot be completed before the evaluation visit, the physician or allowed practitioner **must be consulted to approve additions or modifications**.
- § 484.60(b)(3) — orders may be accepted "only by personnel authorized to do so by applicable state laws."
- § 484.60(c)(1) — the plan must be **reviewed and revised no less frequently than once every 60 days** from the start-of-care date.
- § 484.60(d) — coordination of care: assure communication with all involved practitioners; **integrate orders** from all practitioners; and **integrate services** to assure identification of patient needs and factors affecting patient safety.

**[VERIFIED]** 42 CFR § 484.75(b) requires skilled professionals to participate in **"ongoing interdisciplinary assessment of the patient"** (§ 484.75(b)(1)) and in **"development and evaluation of the plan of care in partnership with the patient"** (§ 484.75(b)(2)) ([Cornell LII](https://www.law.cornell.edu/cfr/text/42/484.75)).

The interdisciplinary case conference is the operational form of § 484.60(d) and § 484.75(b)(1). Notably, **the CoPs do not prescribe a case-conference frequency, attendee list, or format.** That is the agency's design space — and it is precisely where a platform can add value without displacing regulated clinical judgment.

### 7.2 Practices described by the consulting literature

**[VERIFIED]** McBee's episode-management model ([McBee](https://mcbeeassociates.com/insights/blog/pdgm-best-practice-turn-to-episode-management-to-drive-efficient-visit-utilization/)):

- The **case manager leads** cross-discipline collaboration and recommends the primary disciplines for care.
- The case manager escalates to the **clinical manager / team leader after the initial interdisciplinary review**.
- The lead discipline is selected by dominant clinical goal, with other disciplines coordinating their frequencies around it.
- Two specific waste patterns McBee observes and targets: PT and OT **seeing the patient on the same day with overlapping care goals**, and **nursing plotted heavily in month one when the patient's primary goals are functional**.
- Visits should be scheduled for the **full 60-day episode** at the outset, not one 30-day period at a time — because the comprehensive assessment is built for 60 days while the payment clock runs on 30.

McBee sells Utilization Management and Episode Management as distinct clinical service lines, which is itself evidence that these are recognized, staffed functions rather than ad hoc activity. **I could not verify a published, citable job description or staffing ratio for a home-health utilization review nurse.** Any specific description of that role should be presented as design work, not as a sourced benchmark.

### 7.3 Exception reporting and leading indicators

**[VERIFIED]** Gravity Healthcare Consulting's leading-indicator benchmark set ([gravityhealthcareconsulting.com](https://gravityhealthcareconsulting.com/home-health/what-are-the-6-most-important-kpis-in-home-health-hint-theyre-not-the-ones-you-think/), March 25, 2025). This is consultant guidance rather than survey data, but it is the most concrete published benchmark set on visit-utilization operations that I could locate:

| Indicator | Benchmark | What it predicts |
|---|---|---|
| SOC documentation submitted within 24 hours of the visit | ≥ 90% | timely reimbursement, OASIS accuracy, care coordination |
| Missed visits reported to the office | 100% within 2 hours | continuity, compliance risk, same-day recovery |
| Referrals scheduled after acceptance | ≥ 90% within 2 hours | faster SOC, referral-partner retention, growth capacity |
| **LUPA risk assessed at admission** | **100% of SOCs, with visit plan flagged for review** | episode efficiency, PDGM alignment |
| OASIS assessments still unlocked after 5 days | < 5% | data integrity, survey readiness, payment delay |
| **Visits scheduled but not completed without valid reason** | **< 2%** | operational control, discipline-mix accuracy, utilization integrity |

The design insight Gravity is making — and it is the right one for a capacity platform — is that LUPA rate, star rating, and margin are all **lagging** indicators. By the time they move, the period is closed and the money is gone. The controllable indicators are all **scheduling-reliability** indicators, and every one of them is observable inside a scheduling system in real time.

### 7.4 A period-review cadence

**[MODELED — ILLUSTRATIVE]** No published source prescribes review checkpoints inside a 30-day period. The following synthesizes the LUPA mechanics (Section 4), the front-loading evidence (Section 5), and the § 484.60 order requirements. Present it as a design proposal, not a benchmark.

| Checkpoint | Question | Action if exception |
|---|---|---|
| Admission (day 0–1) | Does the ordered frequency clear this payment group's LUPA threshold within 14 days? Is the discipline mix matched to the dominant clinical goal? | Route a frequency-review request to the practitioner; assign lead discipline per McBee |
| Day 7 | Has the threshold been cleared? Is roughly 40% of the plan delivered? | Reschedule missed visits *inside* the front-loading window, not after it |
| Day 15 | Is remaining planned volume consistent with observed progress? Are PT and OT duplicating visits or goals? | Interdisciplinary case conference; propose taper or discipline change to the practitioner |
| Day 22–25 | Will the period close above threshold? Is a second period clinically indicated, or is the patient ready for discharge? | Confirm continuation or begin discharge planning. **Never add a visit for threshold reasons alone** |
| Period close | Actual vs. ordered frequency variance; LUPA cause code | Feed back into scheduling-reliability metrics, not into individual clinician scorecards |

### 7.5 Changing frequency without undermining clinician authority

The regulation settles the question of authority: frequency is a physician order (§ 484.60(a)(2)(iv), (b)(3)), and the clinician's assessment is the input to it. There is no legitimate design in which a scheduling system changes a frequency. What a system can legitimately do:

- Make the **consequence** of the current plan visible to the clinician at the moment they set it — threshold position, front-load coverage, discipline overlap with another discipline's scheduled visits.
- Make the **order-change request** a two-click action with the clinical rationale pre-populated from the assessment, so that the friction of doing the right thing drops below the friction of leaving a stale frequency in place. Most bad frequencies persist through inertia, not through disagreement.
- Surface variance between ordered and delivered frequency as **an agenda item for the case conference**, not as a performance score for the individual clinician.
- **Never present a dollar figure to the clinician at the point of care.** Present it to the clinical manager in aggregate. The evidence-based framing for the bedside clinician is timing and outcome; the financial framing belongs one level up, where the person receiving it has the authority and the context to act on it without a conflict of interest at the bedside.

---

## 8. Missed visits, no-shows, and reschedules

### 8.1 Correcting a widespread error

The vendor literature quantifies missed visits as lost revenue. **[VERIFIED as published — but wrong for PDGM]** A representative example: "Let's say your agency bills an average of $140 per home health visit. Missing just ten visits per week equals $1,400 in lost revenue weekly … over $67,000 per year" ([Alora Health, "The Financial Impact of Missed Homecare Visits"](https://www.alorahealth.com/blog-the-financial-impact-of-missed-homecare-visits/), May 15). This is vendor marketing content, and the arithmetic only holds for **per-visit payers** — Medicaid, private duty, and MA contracts written on a per-visit basis.

Under PDGM it is materially wrong. A missed visit in a period that remains above its LUPA threshold produces **zero revenue loss**. It may even *increase* reported period margin, by removing a cost with no offsetting revenue. That inversion is precisely why missed visits are dangerous under episodic payment: **the immediate financial signal points the wrong way.** An agency reading its own P&L naively will see missed visits as neutral or mildly favorable right up until the moment a period crosses the threshold, at which point it loses $1,363 in a single event.

### 8.2 What a missed visit actually costs under PDGM

**[MODELED — ILLUSTRATIVE] Cost decomposition of one missed-and-rebooked visit, CY2026:**

| Component | Amount | Basis |
|---|---|---|
| Wasted travel on a failed attempt (patient not home) | $10–$17 | mileage assumption, Section 3.3 |
| Scheduler and coordinator rework | $8–$15 | ~15–20 min of coordinator time at burdened rate |
| The rebooked visit itself | ~$100 direct | Section 3.3 — **not incremental** if it displaces nothing |
| **Opportunity cost of the displaced capacity slot** | **~$100–$250** | the slot could have served a new admission; **binds only at capacity** |
| **Expected LUPA cost** | **P(LUPA) × ~$1,400** | Section 4.2 |
| Outcome / HHVBP risk if inside the front-load window | not directly monetizable | Sections 5.1, 10.3, 10.4 |

**The dominant term is the LUPA probability, and it is entirely conditional on where the period stands.** A missed visit on day 25 of a period already at 9 delivered visits costs approximately $25 of rework and nothing else. The identical missed visit on a period sitting at 3 delivered visits against a 4-visit threshold carries an expected cost in the hundreds of dollars. **The cost of a missed visit varies by roughly two orders of magnitude depending on period state.**

No flat per-missed-visit metric captures this, and none of the published benchmark sets attempt it. A scheduling platform that computes the **LUPA-conditional expected cost of each specific missed visit in real time** is doing something no current tool or benchmark does — and it converts missed-visit recovery from a generic productivity nag into a triaged, ranked work queue.

### 8.3 Measured frequency

The measured evidence here is weak and I want to be explicit about that.

- **[VERIFIED as a benchmark target, not as an observed rate]** Visits scheduled but not completed without valid reason: **< 2%** ([Gravity Healthcare Consulting](https://gravityhealthcareconsulting.com/home-health/what-are-the-6-most-important-kpis-in-home-health-hint-theyre-not-the-ones-you-think/), March 25, 2025). Missed visits reported to the office: **100% within 2 hours** (same source).
- **[UNVERIFIED — vendor claim, do not cite]** An "industry average of about 10 percent of all visits missed" appears in vendor content but I could not trace it to a survey, a claims analysis, or any peer-reviewed source. **This figure should not be used with a client.**
- **[VERIFIED]** McBee identifies "obstacles with managing missed visits and scheduling" as a primary driver of *unintentional* LUPAs, alongside the varying threshold ([McBee](https://mcbeeassociates.com/insights/blog/pdgm-best-practice-turn-to-episode-management-to-drive-efficient-visit-utilization/)).
- **[VERIFIED]** SimiTree's clinical-management findings identify missed visits, inappropriate discharge timing, holding patients too long, and discharging patients too early as the areas providers struggle with most ([SimiTree](https://simitreehc.com/simitree-blog/home-health-proposed-rule-financial-breakdown-cy-2025/)).

**The gap is the opportunity.** There is no authoritative national missed-visit rate for Medicare-certified home health. A platform that measures it reliably across a client base would hold data that nobody currently publishes — and that would be a genuine, defensible differentiator rather than a repackaged benchmark.

---

## 9. Industry margin context

### 9.1 MedPAC's reported margins

**[VERIFIED]** All from [MedPAC March 2026, Chapter 8](https://www.medpac.gov/wp-content/uploads/2026/03/Mar26_Ch8_MedPAC_Report_To_Congress_SEC.pdf).

**FFS Medicare margin, freestanding HHAs:**

| | 2019 | 2020 | 2021 | 2022 | 2023 | **2024** | 2026 (projected) |
|---|---|---|---|---|---|---|---|
| **All** | 15.4% | 20.2% | 24.9% | 22.2% | 19.8% | **21.2%** | **19%** |
| For profit | 17.4 | 22.7 | 26.1 | 23.6 | 21.2 | **23.1** | |
| Nonprofit | 11.4 | 12.4 | 20.2 | 16.4 | 13.3 | **12.2** | |
| Majority urban | 16.1 | 20.0 | 24.8 | 22.3 | 20.0 | **21.3** | |
| Majority rural | 14.2 | 21.6 | 25.2 | 22.0 | 18.6 | **20.5** | |
| Smallest volume quintile | 9.7 | 11.6 | 14.0 | 13.7 | 12.5 | **14.4** | |
| Largest volume quintile | 17.5 | 22.4 | 28.3 | 24.8 | 22.1 | **23.2** | |

Distribution in 2024: **5.7% at the 25th percentile, 31.0% at the 75th percentile.** The long-run average from 2001 to 2023 was **17.2 percent** — payments have exceeded costs every year since the PPS began in 2000. Hospital-based HHAs ran **−15.2 percent** in 2024, which MedPAC attributes chiefly to overhead allocated from the parent hospital.

The volume-quintile gradient is directly relevant to a branch capacity product: the largest quintile earns 8.8 points more than the smallest, and MedPAC attributes this to economies of scale. The largest quintile holds 60 percent of all 30-day periods while representing 20 percent of agencies.

**[VERIFIED]** For CY2027, MedPAC recommends Congress **reduce the 2026 base rate by 7 percent**, estimating $750 million to $2 billion in savings over one year and $10–25 billion over five years, and stating it does not expect adverse effects on beneficiary access or on providers' willingness to serve FFS beneficiaries. The recommendation is explicitly **not additive** to the BBA-of-2018 adjustments already implemented. Under current law CMS's third-quarter 2025 projection indicates a +2.3 percent update for 2027 absent the recommendation.

### 9.2 All-payer margin and MA compression

**[VERIFIED]** In 2024 the **all-payer margin for freestanding HHAs was 5.0 percent**, against a **FFS Medicare margin of 21.2 percent** ([MedPAC Ch. 8](https://www.medpac.gov/wp-content/uploads/2026/03/Mar26_Ch8_MedPAC_Report_To_Congress_SEC.pdf), March 2026).

That single pair of numbers is the cleanest available quantification of Medicare Advantage margin compression, and it is more useful than any operator anecdote.

**[MODELED — ILLUSTRATIVE] What the gap implies.** If FFS Medicare is roughly half of a typical freestanding agency's revenue and earns 21.2 percent, then for the blended all-payer result to be 5.0 percent, **everything that is not FFS Medicare must be earning approximately −11 percent.**
*Derivation:* 0.5 × 21.2% + 0.5 × x = 5.0% → x = −11.2%.
*Assumptions:* a 50/50 revenue split (not measured — actual mix varies enormously by market); no difference in cost-allocation methodology between payers; both margins drawn from the same cost-report population. Sensitivity: at a 60/40 FFS/non-FFS split the implied non-FFS margin is −19.3 percent; at 40/60 it is −5.8 percent. **The sign is robust across every plausible mix; the magnitude is not.** The defensible statement is that non-FFS home health business is, on average, at or below break-even.

**[VERIFIED]** Operator-level corroboration for Q3 2025 ([Mertz Taggart, *Home-Based Care Public Company Roundup Q3 2025*](https://www.mertztaggart.com/post/home-based-care-public-company-roundup-q3-2025), November 17, 2025):

- **Enhabit**: FFS Medicare census down 1.4% year over year (a sharp improvement from −14.1% in Q3 2024); non-Medicare admissions **up 10.4%**; non-Medicare revenue per visit up 2.8% through "continued payor mix management"; adjusted EBITDA margin ~10.2%.
- **Pennant Group**: home health admissions up 36.2% total, 7% same-store; revenue per episode up 2.9%; adjusted EBITDA margin ~8.1%.
- **Addus**: home health same-store revenue down 2.8% year over year.
- **Aveanna**: preferred payer agreements now represent 56% of Private Duty MCO volumes.
- **BrightSpring**: Provider Services revenue up 9%, adjusted EBITDA up 16%; overall adjusted EBITDA margin ~4.8%.

The pattern across operators is consistent and instructive: volume growth is coming from managed care, and the operators are managing it through **rate negotiation and payer selection**, not through utilization reduction. "Payor mix management" and "preferred payer agreements" are the industry's language for declining or repricing unprofitable MA contracts.

Note the gap between the 21.2 percent FFS Medicare *cost-report* margin and the 8–13 percent *adjusted EBITDA* margins these public operators report. They are different measures over different denominators (the cost-report margin is FFS-Medicare-only revenue against allocated Medicare cost; adjusted EBITDA is all-payer, all-segment, after corporate overhead). Both are correct; they must never be compared directly in a client deliverable.

**Why MA compresses margin, mechanically.** Three effects stack: (1) contracted rates below the PDGM period-equivalent; (2) prior authorization, which caps authorized visits and adds unreimbursed administrative labor; and (3) per-visit contract structure, which removes the fixed-payment leverage that makes utilization management profitable in the first place. Under a per-visit MA contract, every practice described in Sections 4 through 8 of this file **reduces revenue** rather than cost. This is the single most important reason payer type cannot be an afterthought in the platform's data model.

---

## 10. The counter-evidence: documented risk of under-utilization

This section exists because the platform must not be capable of pushing margin at the cost of care. The honest reading of the evidence is more nuanced than either side of the debate usually admits.

### 10.1 The reassuring finding

**[VERIFIED]** MedPAC's mandated PDGM evaluation ([Ch. 14](https://www.medpac.gov/wp-content/uploads/2026/03/Mar26_Ch14_MedPAC_Report_To_Congress_SEC.pdf), March 2026) found that a **15.3 percent reduction in visits per stay did not produce broad quality deterioration** in 2023:

| Outcome, 2023 | With PDGM | Without PDGM | Difference |
|---|---|---|---|
| Potentially preventable hospitalization during the stay | **8.2%** | 10.3% | **−2.1 pp (−20.0%)** |
| Stays discharged to the community | **82.8%** | 85.2% | **−2.5 pp (−2.9%)** |
| Change in composite mobility at discharge | 0.89 | 0.86 | +0.03 (+3.7%) |
| Change in composite self-care at discharge | 2.50 | 2.46 | +0.04 (+1.6%) |

MedPAC's conclusion: PDGM "did not have an adverse impact on FFS Medicare beneficiaries and may have re-aligned therapy services to better reflect clinical need while maintaining quality of outcomes."

Corroborating this at the population level, **[VERIFIED]** MedPAC Chapter 8 reports that the median risk-adjusted rate of discharge to community from HHAs was **80.6 percent** for the two years ending December 2023, an **improvement of 1.3 percentage points**, while the median potentially preventable readmission rate was 3.8 percent (25th–75th percentile spread of 3.65% to 4.06%). Patient-experience scores were flat to slightly improved.

### 10.2 The finding that is not reassuring

**Discharge to community got worse.** 82.8 percent versus 85.2 percent, statistically significant, in the same model that found hospitalization improved. MedPAC reports this plainly and does not explain it away. A 2.5-point reduction in the share of stays ending with the patient successfully at home is a real signal that something in the reduced-visit model is failing a subset of patients — and it is exactly the measure that would move if agencies were discharging too early or under-serving the patients least able to compensate.

MedPAC also warns that the functional measures are drawn from **provider-reported OASIS data**; that it has found discrepancies in functional-status reporting across post-acute settings "often favoring higher payments"; and that OIG has documented **under-reporting of falls with major injury** in HHA-completed patient assessments (OIG 2023, cited in [MedPAC Ch. 14](https://www.medpac.gov/wp-content/uploads/2026/03/Mar26_Ch14_MedPAC_Report_To_Congress_SEC.pdf)). The mobility and self-care improvements should therefore carry less evidentiary weight than the claims-based hospitalization and discharge measures, which are not self-reported.

MedPAC's own summary of the −2.1 point hospitalization finding says the limitations of its methods "require interpreting this finding with caution." Both directions of the quality result deserve that caution.

### 10.3 Timing risk is the dominant risk, not volume risk

The strongest evidence of harm is not about how many visits — it is about **when**:

- First home health nursing visit later than 2 days after hospital discharge: **12 percent higher odds** of rehospitalization or ED visit for delayed episodes; **four times greater odds** for patients first seen 8–14 days after discharge ([AJMC](https://www.ajmc.com/view/after-hospital-discharge-slow-home-health-care-initiation-increases-risk-of-rehospitalization); [PubMed 35931136](https://pubmed.ncbi.nlm.nih.gov/35931136/), 2022).
- Sepsis survivors: **7 percentage points lower** 30-day rehospitalization, a **41 percent relative reduction**, with a nursing visit within 2 days plus a further week-1 nursing visit plus outpatient follow-up within 7 days.
- Heart failure, front-loaded at 60 percent of planned SN visits in weeks 1–2: **15.8 percent versus 39.4 percent** 60-day rehospitalization (Rogers et al. 2007, in [O'Connor et al.](https://pmc.ncbi.nlm.nih.gov/articles/PMC4532304/)).

And critically, **more visits is not the intervention.** The same review found 1–1.99 visits per week outperformed higher frequencies for rehospitalization reduction; lower nursing intensity was associated with better ADL improvement; front-loading was ineffective for diabetic patients; and higher intensity helped only for dyspnea management.

**The evidence supports a redistribution strategy, not a volume strategy.** A platform that optimizes *when* and *by whom* is on solid evidentiary ground. A platform that optimizes *how many* — in either direction — is not.

### 10.4 The financial guardrail: HHVBP

**[VERIFIED]** The expanded Home Health Value-Based Purchasing Model applies nationally. CMS determines a payment adjustment "up to the maximum applicable percentage, upward or downward … for each competing home health agency based on the agency's Total Performance Score using a linear exchange function" against its cohort (42 CFR § 484.325, [Cornell LII](https://www.law.cornell.edu/cfr/text/42/484.325)). The applicable percent runs from **−5 percent to +5 percent** of Medicare FFS payments. CY2025 was the first payment year, based on CY2023 performance; CY2026 payment reflects CY2024 performance.

**[VERIFIED]** Measure category weights (42 CFR § 484.360, [Cornell LII](https://www.law.cornell.edu/cfr/text/42/484.360)): **OASIS-based 35 percent, claims-based 35 percent, HHCAHPS Survey-based 30 percent.** An agency must have a minimum of five applicable measures to receive a Total Performance Score; categories are proportionally reweighted where volume is insufficient. The three claims-based measures are **acute care hospitalization during the first 60 days, emergency department use without hospitalization, and discharge to community.**

**[VERIFIED]** CY2026 changes ([IHA CY2026 rule summary](https://www.team-iha.org/getmedia/26da6c77-bc88-4b05-baf3-95edcf481308/CY-2026-Medicare-HH-PPS-FR-Rule-Summary.pdf), December 2025): CMS **removes** three HHCAHPS measures (Care of Patients; Communications Between Providers and Patients; Specific Care Issues) and **adds** Medicare Spending Per Beneficiary–Post-Acute Care plus three OASIS function measures (Improvement in Bathing, Upper Body Dressing, Lower Body Dressing), with corresponding reweighting of individual measure and category weights. CMS also adopted a ninth measure-removal factor ("not feasible to implement the measure specifications") and issued an RFI on adding a Falls with Major Injury measure.

**Why this closes the loop.** The two claims-based measures most sensitive to under-service — acute care hospitalization and discharge to community — sit inside a 35-percent-weighted category. Discharge to community is also the exact measure MedPAC found deteriorated under PDGM's visit reduction. From CY2026, MSPB-PAC joins the set, so an agency whose patients rehospitalize is penalized twice: once on the hospitalization measure and again on spending per beneficiary.

**[MODELED — ILLUSTRATIVE] The two levers are the same size.** For a 10,000-period agency at $2,038 per period ($20.4M of FFS revenue):

| | Annual effect |
|---|---|
| Margin gained by removing one visit per period | **+$1.09M** |
| Margin lost at a −5% HHVBP adjustment | **−$1.02M** |

**The entire margin available from cutting one visit per period can be erased by a single maximum-downside HHVBP adjustment.** That is the honest business case for building the platform around timing and discipline-match rather than volume reduction: the volume strategy is roughly a coin flip against its own quality penalty, while the timing strategy captures the LUPA upside and the rehospitalization upside on both sides of the ledger at once.

---

## 11. Implications for a branch capacity-and-scheduling platform

1. **Payer type is a first-class scheduling variable.** PDGM episodic and MA per-visit have opposite marginal economics. One utilization policy applied across a mixed book destroys value on one side of it.
2. **Period state, not visit count, is the unit of decision.** The value of the next visit is $1,363 or $0 depending entirely on where the period sits relative to its threshold. Any metric that averages across period states is uninformative by construction.
3. **The expected cost of a missed visit is LUPA-conditional and varies by roughly 100×.** Computing it in real time is a capability no published benchmark set offers and no competitor appears to have.
4. **Front-loading is the only intervention that improves margin and outcomes simultaneously.** It is LUPA-protective and rehospitalization-protective and requires no additional visits — but its margin benefit only materialises in a branch that can refill the freed capacity.
5. **Discipline mix is worth roughly 2–4 margin points** and is bounded by hard rules: the RN comprehensive assessment within 5 days, LPN/PTA/COTA supervision, and the 14-day aide supervisory assessment that must be booked as real, non-billable RN cost.
6. **Frequency is a physician order.** The system prompts; the clinician assesses; the practitioner orders. Anything else is a compliance defect regardless of how the UI is worded.
7. **Claims clustered just above the LUPA threshold are a designated MAC targeting signal.** Never surface "add a visit to clear the threshold." Do surface the agency's own visits-per-period distribution as a self-audit view.
8. **Instrument the leading indicators, not the lagging ones.** SOC documentation within 24 hours, missed-visit notification within 2 hours, LUPA risk flagged at 100% of SOCs, scheduled-not-completed under 2 percent.
9. **Model LUPA thresholds as moving, not fixed.** They recalibrate annually to the 10th percentile of industry behavior, so utilization reduction is partially self-limiting over a multi-year horizon.
10. **Carry HHVBP in the same model as margin.** A −5 percent adjustment is the same order of magnitude as the entire margin from a one-visit-per-period reduction. A platform that reports margin without reporting the quality exposure alongside it is giving half an answer.

---

## Appendix A — Verified figure register

| Figure | Value | Source | Date |
|---|---|---|---|
| CY2026 30-day period rate | $2,038.22 | [IHA CY2026 summary](https://www.team-iha.org/getmedia/26da6c77-bc88-4b05-baf3-95edcf481308/CY-2026-Medicare-HH-PPS-FR-Rule-Summary.pdf) / CMS-1828-F | Nov 28, 2025 |
| CY2025 30-day period rate | $2,057.35 | same | — |
| CY2026 SN per-visit / with add-on | $176.96 / $304.37 (1.7200) | same | Nov 2025 |
| CY2026 PT per-visit / with add-on | $193.42 / $313.82 (1.6225) | same | Nov 2025 |
| CY2026 OT per-visit / with add-on | $194.74 / $335.69 (1.7238) | same | Nov 2025 |
| CY2026 SLP per-visit / with add-on | $210.25 / $351.03 (1.6696) | same | Nov 2025 |
| CY2026 MSW / aide per-visit | $283.64 / $80.12 | same | Nov 2025 |
| CY2026 outlier FDL ratio | 0.37 | same | Nov 2025 |
| CY2026 labor-related share | 74.9% | same | Nov 2025 |
| CY2026 LUPA threshold changes | 389 unchanged / 15 up / 28 down | same | Nov 2025 |
| Visits per full 30-day period, 2024 | 8.4 (10.2 in 2019, −18.0%) | [MedPAC Ch. 8, Table 8-4](https://www.medpac.gov/wp-content/uploads/2026/03/Mar26_Ch8_MedPAC_Report_To_Congress_SEC.pdf) | Mar 2026 |
| Visits per 30-day period incl. LUPAs, 2024 | 8.3 | same | Mar 2026 |
| SN visits per full period, 2024 | 4.1 (4.6 in 2019) | same | Mar 2026 |
| PT+OT+SLP per full period, 2024 | 3.8 (4.9 in 2019) | same | Mar 2026 |
| MSW + aide per full period, 2024 | 0.5 (0.8 in 2019) | same | Mar 2026 |
| Total in-person visits, 2024 | 65.4M (99.7M in 2019) | same | Mar 2026 |
| LUPA share of 30-day periods, 2024 | ~7% | same | Mar 2026 |
| Medicare payment per in-person visit, 2024 | $245 ($180 in 2019) | same | Mar 2026 |
| Average payment per full 30-day period, 2024 | $2,057 | same | Mar 2026 |
| FFS Medicare margin, freestanding, 2024 | 21.2% (25th pct 5.7%, 75th pct 31.0%) | same | Mar 2026 |
| FFS Medicare margin, 2001–2023 average | 17.2% | same | Mar 2026 |
| All-payer margin, freestanding, 2024 | 5.0% | same | Mar 2026 |
| Hospital-based FFS Medicare margin, 2024 | −15.2% | same | Mar 2026 |
| Projected FFS Medicare margin, 2026 | 19% | same | Mar 2026 |
| MedPAC CY2027 recommendation | −7% to the 2026 base rate | same | Mar 2026 |
| FFS home health spending, 2024 | $16.0B, 2.7M users | same | Mar 2026 |
| Periods per 100 FFS beneficiaries / per user, 2024 | 24.7 / 3.1 | same | Mar 2026 |
| Median discharge to community (2022–2023) | 80.6%, +1.3 pp | same | Mar 2026 |
| PDGM effect on visits per stay, 2023 | 15.9 vs 18.8 (−2.9, −15.3%) | [MedPAC Ch. 14](https://www.medpac.gov/wp-content/uploads/2026/03/Mar26_Ch14_MedPAC_Report_To_Congress_SEC.pdf) | Mar 2026 |
| PDGM effect, therapy / nursing / aide | −2.4 (−21.3%) / −0.7 (−9.8%) / +0.2 | same | Mar 2026 |
| Preventable hospitalization with/without PDGM | 8.2% vs 10.3% (−2.1 pp) | same | Mar 2026 |
| Discharge to community with/without PDGM | 82.8% vs 85.2% (−2.5 pp) | same | Mar 2026 |
| FFS Medicare margin per home health stay, 2023 | 24.1% | same | Mar 2026 |
| MedPAC on LPN / assistant substitution | named as a post-PDGM cost lever | same | Mar 2026 |
| OIG LUPA audit non-compliance | 25 of 120 claims (21%); $191.8M extrapolated | [OIG A-09-18-03031](https://oig.hhs.gov/reports/all/2020/cms-could-have-saved-192-million-by-targeting-home-health-claims-for-review-with-visits-slightly-above-the-threshold-that-triggers-a-higher-medicare-payment/) | Jul 22, 2020 |
| Subsequent-period LUPAs one visit short | 81.12% | [McBee](https://mcbeeassociates.com/insights/blog/pdgm-best-practice-turn-to-episode-management-to-drive-efficient-visit-utilization/) | — |
| Front-loading operational definition | 60% of planned SN visits in first 2 weeks | [O'Connor et al., PMC4532304](https://pmc.ncbi.nlm.nih.gov/articles/PMC4532304/) | 2015 |
| Front-loaded HF rehospitalization | 15.8% vs 39.4% at 60 days (p<.001) | Rogers et al. 2007, in same | 2007 |
| Optimal intensity for rehospitalization | 1–1.99 visits/week | same | 2015 |
| Delayed first visit (8–14 days) | 4× odds of rehospitalization | [AJMC](https://www.ajmc.com/view/after-hospital-discharge-slow-home-health-care-initiation-increases-risk-of-rehospitalization) / [PubMed 35931136](https://pubmed.ncbi.nlm.nih.gov/35931136/) | 2022 |
| Sepsis survivors, timely HH + follow-up | −7 pp (−41% relative) 30-day rehospitalization | same | 2022 |
| BLS mean hourly, RN / LPN | $48.76 / $32.24 | [BLS OEWS Table 1](https://www.bls.gov/news.release/ocwage.t01.htm) | May 2025 |
| BLS mean hourly, PT / PTA | $50.62 / $33.04 | same | May 2025 |
| BLS mean hourly, OT / OTA | $48.69 / $33.99 | same | May 2025 |
| BLS mean hourly, SLP / healthcare MSW / aide | $47.20 / $34.51 / $17.36 | same | May 2025 |
| HHVBP payment adjustment range | −5% to +5%, linear exchange function | [42 CFR § 484.325](https://www.law.cornell.edu/cfr/text/42/484.325) | current |
| HHVBP category weights | OASIS 35% / claims 35% / HHCAHPS 30% | [42 CFR § 484.360](https://www.law.cornell.edu/cfr/text/42/484.360) | current |
| HHVBP claims-based measures | ACH first 60 days; ED use w/o hospitalization; discharge to community | same | current |
| RN comprehensive assessment, ≤5 days | required, RN only (therapy-only exception) | [42 CFR § 484.55(b)(1)–(3)](https://www.law.cornell.edu/cfr/text/42/484.55) | current |
| RN initial assessment, ≤48 hours | required, RN only (therapy-only exception) | [42 CFR § 484.55(a)(1)–(2)](https://www.law.cornell.edu/cfr/text/42/484.55) | current |
| LPN supervision | under a qualified RN | [42 CFR § 484.115(e)](https://www.law.cornell.edu/cfr/text/42/484.115), [§ 484.75(c)(1)](https://www.law.cornell.edu/cfr/text/42/484.75) | current |
| PTA / OTA supervision | under the PT or OT | [42 CFR § 484.75(c)(2)](https://www.law.cornell.edu/cfr/text/42/484.75) | current |
| Aide supervisory assessment, skilled patient | every 14 days | [42 CFR § 484.80(h)(1)(i)(A)](https://www.law.cornell.edu/cfr/text/42/484.80) | current |
| Aide supervisory visit, non-skilled patient | every 60 days, RN onsite | [42 CFR § 484.80(h)(2)(i)(A)](https://www.law.cornell.edu/cfr/text/42/484.80) | current |
| Aide training / in-service | 75 hours / 12 hours per 12 months | [42 CFR § 484.80(b)(1), (d)](https://www.law.cornell.edu/cfr/text/42/484.80) | current |
| Plan of care must state visit frequency & duration | required; reviewed ≥ every 60 days | [42 CFR § 484.60(a)(2)(iv), (c)(1)](https://www.law.cornell.edu/cfr/text/42/484.60) | current |
| Scheduled-not-completed benchmark | < 2% | [Gravity Healthcare Consulting](https://gravityhealthcareconsulting.com/home-health/what-are-the-6-most-important-kpis-in-home-health-hint-theyre-not-the-ones-you-think/) | Mar 25, 2025 |
| MA penetration of Medicare population | 55.4% (2025, first flat year in a decade) | [Trella Health](https://www.trellahealth.com/newsroom/press-release/trella-health-releases-2025-post-acute-care-industry-trend-report-highlighting-continued-medicare-advantage-growth-and-shifts-in-care-utilization/) | Jul 2025 |
| Public operator adjusted EBITDA margins, Q3 2025 | Enhabit ~10.2%, Pennant ~8.1%, Addus ~12.4%, Aveanna ~12.9%, BrightSpring ~4.8% | [Mertz Taggart](https://www.mertztaggart.com/post/home-based-care-public-company-roundup-q3-2025) | Nov 17, 2025 |
| CMS utilization decline, CY2025 rule data | 9.86 → 8.0 visits per 30 days (−18.9%) | CY2025 HH PPS rulemaking analysis, via [SHP](https://www.shpdata.com/blog/pdgm-after-4-years-no-big-surprises/) | 2024 |

## Appendix B — Known gaps

These could not be verified in this pass and must not be asserted as fact:

1. **Discipline-level cost per visit from a published benchmark.** SimiTree Compass, HealthPivots, McBee, and Forvis Mazars hold this commercially and do not publish it. Section 3.3 is modeled from BLS wages plus stated productivity assumptions and is internally consistent with MedPAC's cost anchor — validate it against client cost reports before any external use.
2. **A national missed-visit rate for Medicare-certified home health.** The ~10 percent figure circulating in vendor content is untraceable to any survey or claims analysis. Only the <2 percent *target* benchmark is sourced.
3. **MA visits-per-period, and MA contract rates as a percentage of the PDGM equivalent.** Not published anywhere I could reach; must come from client contracts. This is likely covered by a sibling payer-research file.
4. **Published visits-per-period by agency percentile.** Section 2.3 is inferred from the margin distribution and is explicitly labeled as inference.
5. **A citable job description, staffing ratio, or caseload standard for a home-health utilization review nurse.** McBee's service-line naming confirms the function exists; nothing published defines it.
6. **Published case evidence that specific agencies cutting visits saw HHVBP or star-rating deterioration.** The mechanism is documented and the measure weights are verified, but no published case study was located.
7. **CY2026 HHVBP individual measure weights** (Table D-22 of the final rule). Category weights are verified via 42 CFR § 484.360; individual measure weights were not retrieved.
8. **Whether the pre-PDGM 13th/19th-visit therapy reassessment requirement was formally eliminated.** Widely stated in secondary sources; not verified here, so it is omitted from Section 6.
9. **HHVBP payment-adjustment distribution for the first payment year (CY2025).** A pre-expansion figure (79 percent of agencies between −2% and +2% in the original nine-state model, 2019) surfaced in search but could not be confirmed against a CMS source and is therefore excluded from the body.

*Research constraints on this pass: the session's shared web-search and Firecrawl budgets were exhausted by concurrent research agents. All primary sources — the two MedPAC March 2026 chapters, the CY2026 final-rule summary, the OIG audit, BLS OEWS, and the CFR sections via Cornell LII — were retrieved and read directly. The gaps above are the residue.*
