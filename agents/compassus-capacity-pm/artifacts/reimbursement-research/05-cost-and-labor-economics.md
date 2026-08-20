# Home Health Cost Structure and Clinician Labor Economics

Research file 05. Compiled 2026-08-18. Purpose: give a capacity-and-scheduling platform a defensible way to attach a cost number to (a) a single home health visit and (b) a 30-day payment period.

Every figure below carries its year and a source URL. Anything computed rather than published is labeled **ILLUSTRATIVE** with its assumptions listed. Where a number is practitioner-reported rather than survey-grade, it says so.

---

## 0. The three anchors everything else hangs from

Before the discipline-by-discipline detail, three published numbers do most of the work. They are the most defensible starting points available, and they are all government or MedPAC sources.

**Anchor 1 — CMS's own fully-loaded clinician cost method.** In the Paperwork Reduction Act section of the CY 2026 HH PPS final rule, CMS states its method plainly: take the BLS May 2024 median hourly wage for the occupation, then *double it* to account for fringe benefits and overhead (CMS writes "To account for other indirect costs such as overhead and fringe benefits (100 percent), we have doubled the hourly wage"). Using that method CMS derives a **weighted OASIS clinician cost of $91.72 per hour, fully loaded** — built from a loaded RN rate of $90.00/hr, a loaded PT rate of $97.14/hr, and $93.15/hr for other therapists, weighted by who actually completes SOC/ROC assessments (RN 75.42%, PT 23.71%, other therapists 0.87%, from 2023 data). Source: [CY 2026 HH PPS final rule, 90 FR 55560](https://www.federalregister.gov/documents/2025/12/02/2025-21767/medicare-and-medicaid-programs-calendar-year-2026-home-health-prospective-payment-system-hh-pps-rate) (published 2025-12-02).

That 2.0× multiplier is the single most citable loading factor in this entire file. It is not a benchmark of what agencies actually spend — it is CMS's regulatory convention — but it is defensible, it is federal, and it is the number CMS itself uses when it prices clinician time.

**Anchor 2 — CMS's own claims-derived visit minutes by discipline.** To set the LUPA add-on factors, CMS analyzed 100% of LUPA periods and 100% of non-LUPA first periods from **CY 2023 claims** (data as of 2024-09-11) and published average visit lengths. This is the best public per-visit time data that exists, and it is the empirical justification for weighting admissions above routine visits.

| Discipline | Avg minutes, routine (non-first) visit | Excess minutes on the first visit | Implied first-visit minutes | CMS LUPA add-on factor |
|---|---|---|---|---|
| Skilled nursing (SN) | 41.54 | 29.91 | 71.45 | 1.7200 |
| Physical therapy (PT) | 45.11 | 28.08 | 73.19 | 1.6225 |
| Occupational therapy (OT) | 45.98 | 33.28 | 79.26 | 1.7238 |
| Speech-language pathology (SLP) | 47.15 | 31.57 | 78.72 | 1.6696 |

Source: [CY 2026 HH PPS final rule, 90 FR 55408–55409](https://www.federalregister.gov/documents/2025/12/02/2025-21767/medicare-and-medicaid-programs-calendar-year-2026-home-health-prospective-payment-system-hh-pps-rate) (2025), restating the analysis finalized in the [CY 2025 HH PPS final rule, 89 FR 88426–88427](https://www.federalregister.gov/documents/2024/11/07/2024-25441/medicare-program-calendar-year-cy-2025-home-health-prospective-payment-system-updates-home-health) (2024). Underlying claims year: **2023**.

Read that table again: **CMS's own data says an admission visit takes ~1.62× to ~1.72× the in-home time of a routine visit.** Any weighted-visit or points system that assigns an SOC 1.5–2.0 routine-visit-equivalents is not arbitrary — it is within a rounding error of what the federal government measured from a full census of claims. This is the strongest defense a platform can offer for a weighted-capacity model.

Two caveats. First, these are *in-home visit* minutes as reported on claims — they exclude travel and they exclude documentation done outside the home, which is where the admission's real cost premium lives (see §5). The true SOC-to-routine ratio, loaded for OASIS and paperwork, is materially higher than 1.72×. Second, they are national averages across all patients and all agencies.

**Anchor 3 — MedPAC's cost per visit and cost per period.** MedPAC's March 2026 report gives the industry-wide arithmetic:

| Metric | 2019 | 2022 | 2023 | 2024 |
|---|---|---|---|---|
| Total in-person visits per full 30-day period | 10.2 | 8.6 | 8.5 | **8.4** |
| — PT + OT + SLP | 4.9 | 4.0 | 3.9 | **3.8** |
| — Skilled nursing | 4.6 | 4.1 | 4.1 | **4.1** |
| — MSS + home health aide | 0.8 | 0.5 | 0.5 | **0.5** |
| Average Medicare payment per full 30-day period | n/a | $2,010 | $2,024 | **$2,057** |
| Medicare payment per in-person visit | $180 | $232 | $237 | **$245** |
| FFS Medicare margin, freestanding HHAs | — | — | — | **21.2%** |
| All-payer margin, freestanding HHAs | — | — | — | **5.0%** |

Source: [MedPAC, *Report to the Congress: Medicare Payment Policy*, March 2026, Chapter 8, Tables 8-4 and 8-7, pp. 261, 265](https://www.medpac.gov/wp-content/uploads/2026/03/Mar26_Ch8_MedPAC_Report_To_Congress_SEC.pdf). Data year: **2024**. MedPAC projects a 19% FFS Medicare margin for freestanding HHAs in **2026** and recommends Congress cut home health base rates **7% for CY 2027**.

**ILLUSTRATIVE derivation — Medicare-allowable cost per visit and per period, 2024.**
Assumptions: (1) margin = (payment − cost) / payment, computed on the same 30-day-period denominator; (2) the per-visit figures are the per-period figures divided by 8.4 visits, so the same ratio applies; (3) "cost" is Medicare-allowable cost as filed on Form CMS-1728-20, which already includes allocated administrative and general overhead.

- Cost per full 30-day period ≈ $2,057 × (1 − 0.212) = **~$1,621** (2024)
- Cost per in-person visit ≈ $245 × (1 − 0.212) = **~$193** (2024)

That ~$193 is a *fully allocated, all-discipline blended* cost per visit — clinician compensation, travel, supervision, intake, QA, billing, rent, software, everything. It is the right order-of-magnitude sanity check for any bottom-up model built in §1. If a bottom-up model lands at $95 or at $340 for a blended visit, the model is wrong somewhere.

Two things about that number matter enormously for the platform's margin logic. First, **the 21.2% FFS Medicare margin sits next to a 5.0% all-payer margin** — meaning non-Medicare business (Medicare Advantage above all) is, in aggregate, at or below breakeven, so the marginal-cost question is not academic for a branch, it is existential. Second, the margin spread is enormous: **5.7% at the 25th percentile and 31.0% at the 75th percentile of freestanding HHAs in 2024** (MedPAC March 2026, Table 8-8). Operating discipline, not payment rates, is what separates those two agencies.

---

## 1. Cost per visit by discipline — building it bottom-up

### 1.1 The build

A fully loaded cost per visit is:

```
Cost per visit =  (clinician hourly cost, fully loaded)
                × (in-home minutes + documentation minutes + travel minutes) / 60
                + (mileage reimbursement per visit)
                + (allocated supervision, intake, QA, scheduling, billing, occupancy, software)
```

Every one of those five terms is agency-specific. Public sources give defensible ranges for the first four; the fifth can only come from the branch's own general ledger (see the final section).

### 1.2 Wage inputs — BLS OEWS, May 2025

Survey reference period **May 2025**, released 2026-05-15 (USDL-26-0725). HH = NAICS 621600 Home Health Care Services. All figures hourly. Sources: [OEWS news release](https://www.bls.gov/news.release/ocwage.nr0.htm); national file [oesm25nat.zip](https://www.bls.gov/oes/special-requests/oesm25nat.zip); industry file [oesm25in4.zip](https://www.bls.gov/oes/special-requests/oesm25in4.zip); interactive at [data.bls.gov/oes industry 621600](https://data.bls.gov/oes/#/industry/621600/2025).

| Occupation | SOC | HH mean | HH median | National mean | National median | HH employment | HH vs national (mean) |
|---|---|---|---|---|---|---|---|
| Registered Nurses | 29-1141 | $44.99 | $40.83 | $48.76 | $46.90 | 198,180 | **−7.7%** |
| LPN / LVN | 29-2061 | $32.49 | $30.57 | $32.24 | $30.96 | 80,990 | +0.8% |
| Physical Therapists | 29-1123 | $56.85 | $55.16 | $50.62 | $49.40 | 30,920 | **+12.3%** |
| Physical Therapist Assistants | 31-2021 | $38.83 | $38.49 | $33.04 | $32.88 | 14,030 | **+17.5%** |
| Occupational Therapists | 29-1122 | $54.24 | $51.11 | $48.69 | $48.24 | 13,190 | **+11.4%** |
| Occupational Therapy Assistants | 31-2011 | $37.40 | $37.17 | $33.99 | $34.76 | 3,560 | +10.0% |
| Speech-Language Pathologists | 29-1127 | $59.04 | $56.43 | $47.20 | $47.05 | 6,350 | **+25.1%** |
| Healthcare Social Workers | 21-1022 | $35.53 | $33.98 | $34.51 | $32.63 | 26,430 | +3.0% |
| Home Health & Personal Care Aides | 31-1120 | $16.69 | $17.42 | $17.36 | $17.21 | 1,079,060 | −3.9% |

**The most consequential finding in this dataset: home health pays a premium for therapy and a discount for nursing.** SLP runs +25.1%, PTA +17.5%, PT +12.3% above the national all-industry mean — while **RN sits 7.7% below the national mean and 12.9% below the national median.** Home health competes for nurses against hospitals and loses on wage; it competes for therapists against outpatient clinics and wins. Any cost model that applies a uniform "home health wage premium/discount" across disciplines will be wrong in opposite directions for nursing and therapy.

Wage dispersion within NAICS 621600, May 2025 — for rate-setting, the spread matters more than the mean:

| | P10 | P25 | Median | P75 | P90 |
|---|---|---|---|---|---|
| RN | $31.90 | $37.62 | $40.83 | $48.66 | $60.62 |
| LPN | $24.20 | $28.28 | $30.57 | $36.12 | $43.73 |
| PT | $39.30 | $48.12 | $55.16 | $64.36 | $77.57 |
| PTA | $28.42 | $32.80 | $38.49 | $44.11 | $49.08 |
| OT | $39.04 | $45.64 | $51.11 | $62.26 | $74.74 |
| OTA | $28.14 | $31.83 | $37.17 | $43.04 | $48.01 |
| SLP | $37.07 | $47.63 | $56.43 | $69.73 | $84.46 |
| Healthcare social workers | $23.69 | $29.13 | $33.98 | $38.86 | $46.79 |
| Aides | $11.20 | $13.66 | $17.42 | $18.91 | $21.11 |

The P10-to-P90 span for an RN is **$31.90 to $60.62 — a 1.9× range.** For SLP it is 2.3×. A national mean is nearly useless as a branch input; the platform must take the branch's actual rates.

**Note on SOC 31-1121:** BLS does not publish home health aides separately. It collapses 31-1121 (Home Health Aides) and 31-1122 (Personal Care Aides) into the broad group **31-1120**. There is no standalone home health aide wage in OEWS, and the blended figure is pulled down substantially by personal care aides.

### 1.3 The loading factor from wage to fully-loaded hourly cost

Three published conventions bracket the answer:

| Convention | Multiplier on base wage | Source and year |
|---|---|---|
| CMS regulatory convention (fringe + overhead) | **2.00×** | [CY 2026 HH PPS final rule, 90 FR 55560](https://www.federalregister.gov/documents/2025/12/02/2025-21767/medicare-and-medicaid-programs-calendar-year-2026-home-health-prospective-payment-system-hh-pps-rate) (2025); same convention used in the [CY 2023 HH PPS final rule, 87 FR 66877](https://www.federalregister.gov/documents/2022/11/04/2022-23722/medicare-program-calendar-year-cy-2023-home-health-prospective-payment-system-rate-update-home-health) (2022) |
| Statutory payroll tax floor (employer FICA only) | 1.0765× | IRS/SSA, 6.2% OASDI + 1.45% Medicare, employer side, unchanged through 2026 |
| Compensation-only (wages + benefits, no overhead) | **1.374× – 1.515×**, see below | BLS Employer Costs for Employee Compensation, March 2026 |

**BLS ECEC, March 2026** (released 2026-06-12, USDL-26-0827). Sources: [news release](https://www.bls.gov/news.release/ecec.nr0.htm), [Table 1](https://www.bls.gov/news.release/ecec.t01.htm), [Table 4](https://www.bls.gov/news.release/ecec.t04.htm).

| Series | Total comp/hr | Wages/hr | Benefits/hr | Benefits % | **Wage → total comp multiplier** |
|---|---|---|---|---|---|
| Private industry, all | $46.60 | $32.60 | $14.01 | 30.1% | 1.429 |
| Service-providing | $46.03 | $32.41 | $13.62 | 29.6% | 1.420 |
| **Health care & social assistance** | **$49.16** | **$34.61** | **$14.55** | **29.6%** | **1.420** |
| — **RN occupations** within HC&SA | $78.37 | $51.74 | $26.64 | 34.0% | **1.515** |
| — Service occupations within HC&SA | $27.42 | $19.95 | $7.47 | 27.2% | **1.374** |
| Nursing & residential care facilities | $33.86 | $24.47 | $9.40 | 27.8% | 1.384 |

Component breakdown, health care & social assistance (Table 4, March 2026):

| Component | $/hr | % of total comp |
|---|---|---|
| Paid leave | $4.10 | 8.3% |
| Supplemental pay | $1.86 | 3.8% |
| Insurance | $3.74 | 7.6% |
| Retirement & savings | $1.44 | 2.9% |
| Legally required | $3.40 | 6.9% |

**Use 1.515× for RNs and 1.374× for aide-type service occupations, not the 1.420× industry average.** ECEC publishes those cuts specifically and they differ materially. RNs carry a heavier benefit load than the industry mean because they are more likely full-time and benefit-eligible.

⚠️ **ECEC does not publish NAICS 6216 separately.** Its finest health cuts are hospitals and nursing/residential care. Home health sits inside "health care and social assistance" only. Given home health's low benefit take-up and heavy part-time and per-visit mix, its true blended multiplier is likely **below 1.420, closer to the 1.374 service-occupation figure** — that is inference, not a published number, and it is exactly the kind of thing a branch's own G/L settles in one query.

**ILLUSTRATIVE — loaded hourly cost, May 2025 wages × March 2026 ECEC multipliers.** Caveat: this mixes a May 2025 wage base with a March 2026 load factor, a ~10-month mismatch that biases the result slightly low.

| Discipline | HH mean wage | × multiplier | Loaded cost/hr (mean) | Loaded cost/hr (median) |
|---|---|---|---|---|
| RN | $44.99 | 1.515 | **$68.15** | $61.84 |
| LPN | $32.49 | 1.420 | $46.15 | $43.42 |
| PT | $56.85 | 1.420 | **$80.75** | $78.35 |
| PTA | $38.83 | 1.420 | $55.15 | $54.67 |
| OT | $54.24 | 1.420 | $77.04 | $72.60 |
| OTA | $37.40 | 1.420 | $53.12 | $52.80 |
| SLP | $59.04 | 1.420 | **$83.86** | $80.15 |
| Healthcare social worker | $35.53 | 1.420 | $50.47 | $48.27 |
| Aide | $16.69 | 1.374 | $22.94 | $23.94 |

**Reconciling with CMS's 2.0× convention.** CMS's loaded RN figure is $90.00/hr (§0); the ECEC-derived compensation-only figure is $68.15/hr. The **$21.85 gap is the overhead component** CMS folds into its doubling — about 24% of the loaded total, or ~49% on top of compensation. That is a plausible overhead load and it is a useful cross-check, but a platform should expose **compensation load and overhead load as two separate, separately-editable inputs**, because they behave completely differently at the margin (§2): compensation load is variable with hours worked, overhead load is not.

### 1.3a Payroll tax load

| Item | 2024 | 2025 | 2026 | Source |
|---|---|---|---|---|
| Social Security wage base | $168,600 | $176,100 | **$184,500** | [SSA](https://www.ssa.gov/oact/cola/cbb.html) |
| Employer Social Security | 6.20% | 6.20% | 6.20% | ibid. |
| Employer Medicare | 1.45% | 1.45% | 1.45% | ibid. |
| **Employer FICA total** | **7.65%** | **7.65%** | **7.65%** | |

The 0.9% Additional Medicare Tax on high earners is employee-only — no employer match.

**Empirically observed statutory burden** (ECEC March 2026, private industry, expressed as % of wages — what employers actually paid, not statutory maximums): Social Security + Medicare 8.53% · FUTA 0.09% · SUTA 0.46% · **workers' compensation 1.29%**. Total ≈ **10.4% of wages.**

⚠️ **Not verified:** NCCI class code 8835 (home health) workers' compensation loss costs or manual rates, and state-level ranges. The 1.29% above is an all-private-industry average; home health's true rate is materially higher given driving exposure and patient-handling injuries, and it varies severalfold by state and loss history. **This must come from the branch** (see final section).

### 1.4 Travel and mileage

IRS standard business mileage rate — the rate most agencies peg reimbursement to:

| Period | Rate (¢/mile) | Source |
|---|---|---|
| 2026, Jul 1 – Dec 31 | **76.0** | IR-2026-29 |
| 2026, Jan 1 – Jun 30 | **72.5** | IR-2025-128 |
| 2025 | 70.0 | IR-2024-312 |
| 2024 | 67.0 | IR-2023-239 |
| 2023 | 65.5 | IR-2022-234 |

Source: [IRS, Standard Mileage Rates](https://www.irs.gov/tax-professionals/standard-mileage-rates), page last reviewed 2026-07-28. Note the **mid-2026 increase from 72.5¢ to 76.0¢** — a platform that hardcodes a mileage rate will be wrong within six months.

Miles per visit: the best national estimate is **~11.0 miles per visit** (national average 10.98; state extremes: Maine 35.2, Virginia 16.71), from the Foundation for Hospice and Homecare / NAHC analysis of **2013** data covering 718 million visits and ~8 billion miles. Source: [PHI summary](https://www.phinational.org/report-home-care-professionals-traveled-8-billion-miles-in-13/) (2015), original [NAHC issue paper (PDF)](https://www.nahc.org/assets/1/7/15_PR_Issue_Paper_Miles_Driven.pdf). **This is a 2013 figure and it is the newest credible national number I could verify** — treat it as an order of magnitude, not a benchmark, and expect it to have risen as agencies consolidated and territories widened.

**ILLUSTRATIVE mileage cost per visit (2026):** 11 miles × $0.76 = **$8.36 per visit**. Assumptions: national average miles per visit from 2013 data; reimbursement at the full IRS rate; every mile reimbursed (many agencies exclude the first and last commute leg, which cuts reimbursable miles materially).

### 1.5 An illustrative bottom-up cost per visit

**ILLUSTRATIVE — do not present as a benchmark.** Assumptions listed under the table.

| | SN routine | SN admission (SOC) | PT routine | PT eval | Aide visit |
|---|---|---|---|---|---|
| In-home minutes (CMS, CY2023 claims) | 41.5 | 71.5 | 45.1 | 73.2 | 45 (assumed) |
| Documentation minutes (assumed) | 15 | 75 | 15 | 45 | 5 |
| Travel minutes (assumed) | 20 | 20 | 20 | 20 | 20 |
| **Total clinician minutes** | **76.5** | **166.5** | **80.1** | **138.2** | **70** |
| Loaded hourly cost (ECEC, compensation only) | $68.15 | $68.15 | $80.75 | $80.75 | $22.94 |
| Labor cost | $86.89 | $189.12 | $107.80 | $185.99 | $26.77 |
| Mileage @ 11 mi x $0.76 | $8.36 | $8.36 | $8.36 | $8.36 | $8.36 |
| **Direct cost per visit (compensation + mileage)** | **~$95** | **~$197** | **~$116** | **~$194** | **~$35** |
| Plus overhead @ 49% of compensation (CMS-implied) | $42.58 | $92.67 | $52.82 | $91.14 | $13.12 |
| **Fully allocated cost per visit** | **~$138** | **~$290** | **~$169** | **~$286** | **~$48** |

Assumptions: (1) in-home minutes from CMS's CY2023 claims analysis (see section 0); (2) documentation minutes are *assumed* -- the 75-minute SOC figure is CMS's 57.3-minute OASIS-E data-entry estimate (section 5.1) plus an allowance for the plan of care, medication reconciliation, and physician communication that CMS's estimate explicitly excludes, and the routine-visit figure has no published basis at all; (3) 20 minutes of travel per visit is assumed and is the single most agency-variable input here; (4) loaded hourly cost uses ECEC compensation-only multipliers (RN 1.515x, PT 1.420x, aide 1.374x) applied to May 2025 OEWS home health mean wages; (5) the overhead line uses the gap between CMS's 2.0x convention and the ECEC compensation load (section 1.3), which is a national inference, not a branch number; (6) no medical supply cost, no supervision or LPN-oversight time, no allocation of PTO/training/meeting hours.

**Sanity check against Anchor 3.** MedPAC's derived blended all-in cost was **~$193 per visit in 2024**, across a mix that is roughly 49% nursing, 45% therapy, 6% aide/MSW. Blending the fully-allocated row above at MedPAC's 2024 discipline mix, assuming 15% of skilled visits are admissions or evals:

- Nursing: 0.49 x (0.85 x $138 + 0.15 x $290) = $76.9
- Therapy: 0.45 x (0.85 x $169 + 0.15 x $286) = $84.0
- Aide/MSW: 0.06 x ~$48 (understates MSW, which is far more expensive) = $2.9
- **Blended ~ $164 per visit**

Against MedPAC's ~$193, the bottom-up model comes in **~15% low** -- about what you would expect, since it omits medical supplies, clinical supervision, non-productive hours, and any corporate allocation above the branch. **A model that lands within 15% of the MedPAC-derived figure using only public inputs is defensible enough to put in front of an operator, provided that 15% gap is shown rather than buried.**

---

## 2. Compensation models and the marginal cost of one more visit

This is the section that determines whether the platform's margin logic is right or wrong.

### 2.1 The models

| Model | How pay is computed | Marginal cost of visit N+1 | FLSA exposure | Where it shows up |
|---|---|---|---|---|
| **Per-visit** | Flat rate per completed visit, rate varies by visit type | **Full rate, every time.** Linear. | Non-exempt in most cases; agency must track hours and pay OT above 40 — a per-visit rate does not exempt anyone | Most common for PRN/part-time field staff and for therapy |
| **Hourly** | Clock hours × rate | **Full hourly rate × visit duration**, plus overtime premium (1.5×) above 40 hrs/week | Non-exempt, straightforwardly | Aides, LPNs, some RNs |
| **Salaried** | Fixed annual/weekly amount | **$0 in cash** until the clinician hits a capacity ceiling or an overtime/exempt boundary | Exempt only if the duties + salary-basis tests are met; misclassification risk is real for field clinicians | Full-time RN case managers, clinical managers |
| **Points / weighted visit** | Points per visit type × dollars per point, with a weekly point target | **Full point value above the target; often $0 up to the target** if the target is embedded in a base salary | Depends entirely on whether points sit on top of a salary or replace hourly pay | Increasingly common; see §3 |
| **Per-diem / PRN** | Per-visit or per-day rate, no benefits, no guaranteed hours | **Full rate, and typically 15–30% above the employed per-visit rate**, with no benefit load | Non-exempt | Surge, weekend, geography gaps |
| **Contract / agency (1099 or staffing firm)** | Negotiated per-visit or hourly bill rate | **Full bill rate**, including the staffing firm's margin. Highest marginal cost of any model | N/A to the agency (the staffing firm is the employer) | Coverage gaps, rural, specialty |

Per-visit pay is described as "extremely commonplace in the homecare industry" and is usually claimed exempt under the professional exemption on a **fee basis** (29 CFR 541.605) — an exemption that is fragile and breaks the moment the agency also pays hourly for meetings or charting ([Fisher Phillips, 2024](https://www.fisherphillips.com/en/insights/insights/biggest-perils-with-per-visit-compensation-plans-homecare-workers-what-employers-can-do)). **Points do not change that analysis** — a points plan is a per-visit plan with normalized units.

### 2.1a Observed pay levels

| Item | Figure | Source | Year |
|---|---|---|---|
| RN average hourly, home care | **$41.79** (up 3.56% from $40.36) | ✅ [HCS *Home Care Salary & Benefits Report*](https://hhcsinc.com/hcs-reports/home-care-salary-benefits-report/) via [HHCN](https://homehealthcarenews.com/2025/11/home-health-worker-retention-improves-as-wages-bonuses-increase-in-2025/) | 2025 |
| RN average sign-on bonus | **$7,499** | ✅ HCS 2025 via HHCN | 2025 |
| HCA/CNA average sign-on bonus | $2,304 (from $2,129) | ✅ HCS 2025 via HHCN | 2025 |
| HCA/CNA hourly, by state | OK $16.52 · AL $17.37 · MA $23.00 · NH $23.55 | ✅ HCS 2025 via HHCN | 2025 |
| HCA/CNA hourly, by agency type | VNA $22.29 · hospital-based $21.19 · not-for-profit $20.22 · for-profit $18.75 | ✅ HCS 2025 via HHCN | 2025 |
| California per-visit rates (RN) | SOC $130 · recert $100 · revisit $80; **admission-only nurses $165–200/SOC**; hourly $50–55; salary $80–95K | [allnurses](https://allnurses.com/pay-per-visit-vs-hourly-t757111/) (practitioner-reported) | 2024 |
| SoCal head-to-head offers | Hourly: $68/hr, 4-day week, 1 on-call shift · Per-visit: SOC $120, ROC $114, follow-up eval $65, travel time $15.50/hr, 3-day week | [allnurses](https://allnurses.com/pay-per-visit-vs-hourly-t757111/) | 2024 |
| Direct cost to serve a patient | 40–50% of total revenue | ⚠️ [Viventium](https://viventium.com/resources/blog/7-benefits-of-per-visit-pay-for-home-health-agencies) (vendor) | — |

Note the agency-type gradient in the HCA/CNA row: **VNAs pay ~19% more per hour than for-profits for the same job title.** Any cost model that uses a single national wage will misprice a not-for-profit or VNA branch badly.

**Prevalence gap — flagged.** No published national split of home health clinicians by pay model (per-visit vs hourly vs salaried vs points) could be located. The **HCS *Home Care Salary & Benefits Report*** is the one source that collects it — its contents include "hourly vs per visit pay modes" and "caseload/productivity" ([hhcsinc.com](https://hhcsinc.com/hcs-reports/home-care-salary-benefits-report/); published Oct 2025, data effective July 2025; 1,111 agencies, 52,200+ employees). It is paywalled at ~$400 for non-participants. **That is the single highest-value purchase for this research file** — it carries pay mode, caseload, and turnover by job code in one instrument, and three separate sections of this document currently rely on forum anecdote where HCS would give survey data.

### 2.2 Why a salaried clinician's marginal visit is fundamentally different

This is the central asymmetry.

For a **per-visit contractor**, cost is a pure variable. Visit 1 and visit 21 cost the same. Total labor cost is a straight line through the origin. There is no capacity to "fill" and no idle cost to absorb. The agency's margin per visit is fixed by the spread between reimbursement and the per-visit rate, and *scheduling optimization cannot improve it.* Better routing saves the clinician's time, not the agency's money. The only levers are rate negotiation and visit mix.

For a **salaried clinician**, cost is a fixed block that has already been paid. The clinician costs the same on a 3-visit day as on a 6-visit day. That means:

- The **marginal cash cost of an additional visit is approximately zero** (mileage and supplies aside) up to the clinician's real capacity ceiling.
- The **average cost per visit falls hyperbolically with visit volume.** A $95,000 fully-loaded RN doing 4.0 visits/day over 230 productive days costs $103 per visit; the same RN at 5.0 visits/day costs $83; at 5.5 she costs $75. That is a 27% swing in unit cost from a 37% swing in volume, with no change in what anyone is paid.
- **Every unfilled slot is a realized loss, not a foregone gain.** This is the inversion that most agencies get emotionally wrong. An idle salaried hour is money already spent for nothing.
- The **capacity ceiling is real and it is soft.** Push past it and cost reappears — as overtime (if non-exempt), as documentation done unpaid at 10pm (which shows up as turnover, §6), as late or inaccurate OASIS (which shows up as case-mix leakage and denials), or as declined visits that get handed to contract labor at 2× the rate.

**The platform's margin logic follows directly:** value is created by moving visits from the high-marginal-cost pool (contract, PRN, overtime) into the zero-marginal-cost pool (unused salaried capacity), and by keeping salaried clinicians close to — but not past — their real ceiling. Every dollar of contract labor displaced by unused salaried capacity is a dollar of contribution margin, and the size of that prize is exactly (contract rate per visit) × (visits moved), not the difference in wage rates.

**ILLUSTRATIVE — the substitution prize.** Assumptions: contract SN visit billed at $140 (the agency's cost) — ⚠️ **this input is unverified; no published source for home health staffing-agency bill rates could be located** (see Known Gaps), and it should be replaced with the branch's actual contract invoices. Salaried RN fully loaded at $95,000/yr, 230 productive days, currently at 4.2 visits/day with a realistic ceiling of 5.2.
- Unused capacity per RN per year: (5.2 − 4.2) × 230 = 230 visits.
- If those 230 visits currently go to contract labor: 230 × $140 = **$32,200 per RN per year** of avoidable spend.
- Across a 20-RN branch, if even half that capacity is real and reachable: **~$322,000/yr.**
This is the number the platform is selling. It is also the number that is *entirely wrong* if the branch's field staff are paid per-visit — which is why the platform must ask the compensation model before it quotes a saving.

### 2.3 The corollary nobody likes

Under per-visit pay, the *agency* has offloaded volume risk onto the clinician. Under salary, the agency holds it. A branch that has quietly shifted to per-visit pay to control cost has also destroyed most of the value a scheduling optimizer can create for it — and has usually created a turnover problem in exchange (§6). The platform should treat "what fraction of field staff are salaried vs per-visit" as its single most important qualifying question.

---

## 3. Points and weighted-visit systems

### 3.1 What they are and why they exist

A points system decouples pay from clock hours and from raw visit counts by assigning each visit type a weight reflecting its expected time and complexity. The clinician has a weekly point target; points above target may earn a bonus, points below may trigger a performance conversation or a pay adjustment. The premise is that a raw "5 visits a day" standard is dishonest, because an admission and a routine follow-up are not the same unit of work.

CMS's own claims data (Anchor 2) confirms the premise: **admissions consume 1.62×–1.72× the in-home minutes of a routine visit before any documentation is counted.** A flat visit count is measurably the wrong unit.

### 3.2 Typical point values

**There is no published national point scale.** Every point value below is practitioner-reported from clinician forums, and should be treated as anecdotal evidence of common practice rather than as a benchmark. As one respondent put it on [allnurses](https://allnurses.com/national-standard-productivity-t695051/) (2022-10-21): there is no standard, and anyone claiming one is selling something.

Reported schedules:

| Reporting agency / location | Year | SOC | ROC | Recert | Routine | Discharge | Notes |
|---|---|---|---|---|---|---|---|
| Unspecified ([allnurses](https://allnurses.com/national-standard-productivity-t695051/)) | 2019 | 2.0 | — | 1.5 | 1.0 (1.5 if >2 cares) | — | 60 miles = 1 point |
| Per-visit agency ([allnurses](https://allnurses.com/national-standard-productivity-t695051/)) | 2019 | 2.0 | 1.5 | 1.5 | 1.0 | 1.5 | Any visit >90 min = 1.5 |
| New England ([allnurses](https://allnurses.com/national-standard-productivity-t695051/)) | 2019 | 2.0 | 2.0 | 1.0 | 1.0 | — | $0.66/mi; $14/hr beeper |
| Tennessee ([allnurses](https://allnurses.com/national-standard-productivity-t695051/)) | 2019 | 2.25 | 1.25 | 1.5 | 0.75 | — | $0.40/mi |
| Connecticut, agency A ([allnurses](https://allnurses.com/national-standard-productivity-t695051/)) | 2022 | 3.0 | 3.0 | 2.0 | 1.0 | — | Heavier documentation load |
| Connecticut, agency B ([allnurses](https://allnurses.com/national-standard-productivity-t695051/)) | 2022 | 2.0 | 2.0 | 2.0 | 1.0 | — | Lighter charting, pays less |
| Home health OT ([OT Potential](https://otpotential.com/blog/ot-productivity-hacks)) | 2021 | — | — | — | 1.0 | — | **Eval 1.5**; +0.5 pt when >50–60 mi/day |

**Consolidated typical values** (modes from the above):

| Visit type | Typical point value |
|---|---|
| Start of Care / admission with OASIS | **2.0 – 3.0** (mode 2.0–2.5) |
| Resumption of Care | **1.25 – 3.0** (mode 1.5–2.0) |
| Recertification | **1.0 – 2.0** (mode 1.5) |
| Discharge visit | **1.5** (thin evidence) |
| Routine follow-up | **0.75 – 1.5** (mode 1.0) |
| Therapy evaluation (PT/OT/ST) | **1.5** (single source) |
| Supervisory visit | **0.5** (single unverified source) |
| Visit exceeding 90 minutes | 1.5 |
| Mileage adder | 1 pt per 60 mi, or +0.5 pt on days >50–60 mi |

Note how closely the field's improvised 2.0–2.5 SOC weight tracks CMS's measured 1.72× in-home ratio, and how the higher 3.0 values come from agencies self-described as having heavier documentation. **The field converged, without data, on approximately the right answer — and the spread between 2.0 and 3.0 is almost exactly the documentation burden that CMS's in-home minutes exclude.**

**Gaps:** no reported point value for LUPA visits, missed/non-admit visits, or PRN/after-hours. Weekend and holiday premiums appear as **dollars, not points** — e.g. a 2025 ConnectRN posting at $55.73/point weekday vs $57.20/point weekend ([listing](https://bebee.com/us/jobs/registered-nurse-rn-certified-home-health-earn-5573-per-point-connectrn-bryan--jobmesh-2f508a7e-ca08-4bc3-beaf-cc3d4fa1bd2c)).

### 3.3 Weekly point targets and dollar-per-point

| Discipline / model | Full-time weekly target | Source (all practitioner-reported unless noted) | Year |
|---|---|---|---|
| SN/RN, salaried | **25** | [allnurses](https://allnurses.com/national-standard-productivity-t695051/) (TN and others) | 2019 |
| SN/RN, salaried | **30** | [allnurses](https://allnurses.com/national-standard-productivity-t695051/) (CT ×2, New England); [Tampa FL](https://allnurses.com/point-system-ft-t543616/) | 2014–2022 |
| RN, per-visit | **30 units** | [allnurses](https://allnurses.com/national-standard-productivity-t695051/) | 2019 |
| RN, Baylor 3×12s | 9 pts/day ≈ **27/wk** | [allnurses](https://allnurses.com/point-system-ft-t543616/) | 2014 |
| PT, salaried | **25** | [r/physicaltherapy](https://www.reddit.com/r/physicaltherapy/comments/1etx3pi/home_health_point_system/) | 2024 |
| PT, salaried | **30** (≈6/day) | [r/physicaltherapy](https://www.reddit.com/r/physicaltherapy/comments/1cmak9o/looking_for_help_understanding_the_point_system/) | 2024 |
| OT | 4–5 pts/day (**~20–25/wk**) | [OT Potential](https://otpotential.com/blog/ot-productivity-hacks) | 2021 |
| ST | *no data found* | — | — |

**25–30 points per week is the de facto full-time standard for both SN and PT.**

Dollar per point, RN:

| Rate | Source | Year |
|---|---|---|
| $55.73 weekday / $57.20 weekend | [ConnectRN job posting](https://bebee.com/us/jobs/registered-nurse-rn-certified-home-health-earn-5573-per-point-connectrn-bryan--jobmesh-2f508a7e-ca08-4bc3-beaf-cc3d4fa1bd2c) | 2025 |
| $44.16/unit at 27 units/wk → clinician-computed **$30.06/hr effective** | [Glassdoor Community](https://www.glassdoor.com/Community/nurses/any-home-health-nurses-that-can-explain-this-getting-paid-by-point-system-it-sounds-scammy-honestly-like-one-home-health) | ~2024 |
| $35–45/point | [r/nursing](https://www.reddit.com/r/nursing/comments/1fzho1l/home_health_rn_pay/) | 2024 |

**Working range: $35–$57 per point for RN.** The middle row is the most instructive datum in this file: **a $44.16 headline point rate resolved to $30.06 per actual hour worked — a ~32% gap**, because travel, documentation, and case management sit outside the point. That gap is simultaneously the FLSA exposure, the turnover driver, and the reason clinicians describe points as "scammy."

### 3.4 Failure modes

| Failure mode | Evidence |
|---|---|
| **The weights are arbitrary and don't track actual labor** | "Points are arbitrary and are not capable of reflecting your actual labor done. Some [routine visits] can be longer than some SOC" — [allnurses](https://allnurses.com/national-standard-productivity-t695051/), 2022. Even a pro-points calculator concedes the point value is arbitrary and the useful number is the per-visit-type rate and its hourly equivalent — [Home Health Course](https://homehealthcourse.com/home-health-pay-calculator-make-sense-of-the-point-madness/), 2023 |
| **Cherry-picking and dumping complex patients** | Clinicians describe the explicit choice between offloading a one-hour wound patient onto peers or absorbing it — [allnurses](https://allnurses.com/national-standard-productivity-t695051/), 2022 |
| **Underweighting SOC shifts burden onto admission and weekend nurses** | [allnurses](https://allnurses.com/point-system-ft-t543616/), 2014 |
| **Documentation shortcuts and, at the extreme, falsification** | [allnurses](https://allnurses.com/national-standard-productivity-t695051/), 2019 |
| **Unpaid non-visit work / charting off the clock** | SOC reported as ~1 hr in home plus **1–3 hrs at home** entering meds, goals, summary — [allnurses](https://allnurses.com/pay-per-visit-vs-hourly-t757111/), 2024. Clinicians who stop charting off the clock get labeled low-productivity |
| **Coercion into unpaid weekend coverage when targets are missed** | [allnurses](https://allnurses.com/point-system-ft-t543616/), 2014 |
| **Points used as a discipline lever even on salaried staff** | Reported as affecting raises and bonuses, with write-up/termination threats — [allnurses](https://allnurses.com/national-standard-productivity-t695051/), 2020 |
| **FLSA and overtime exposure** ✅ | [Fisher Phillips, "The 12 Biggest Perils With 'Per Visit' Compensation Plans," 2024-11-14](https://www.fisherphillips.com/en/insights/insights/biggest-perils-with-per-visit-compensation-plans-homecare-workers-what-employers-can-do) — explicitly covers points-based plans. The twelve: no compliant written plan; inadequate training; exempt/non-exempt misclassification; failing the fee-basis test; not varying rates by activity type; failing to track non-exempt hours; improper regular-rate/OT computation; ignoring the continuous workday rule; meal-break failures; mishandling on-call in the regular rate; skipping audits; poor documentation of adjustments |
| **Hybrid per-visit + hourly voids the exemption** | Paying per-visit for visits and hourly for other work is argued to be unlawful, with exposure of back OT plus liquidated (double) damages, interest, fees, and a 3-year lookback — [Stephan Zouras LLP](https://www.stephanzouras.com/faqs-skilled-care-home-health-clinician-lawsuits/) (plaintiff-side; read directionally) |
| **Visit-to-hour multipliers are themselves a compliance trap** | Using a multiplier to convert visits into hours worked is flagged as likely non-compliant — [Viventium](https://viventium.com/resources/blog/7-benefits-of-per-visit-pay-for-home-health-agencies) (payroll vendor) |
| **California-specific** | Practitioner reports that CA treats per-visit pay as non-compliant for unpaid home charting, missed rest/meal breaks, and unpaid travel, with successful suits against two large CA home health companies — [allnurses](https://allnurses.com/pay-per-visit-vs-hourly-t757111/), 2024. **The specific cases could not be verified.** |

**Implication for the platform.** A points system is a *cost allocation* scheme, not a *cost measurement* scheme. It tells you what the agency chose to pay for a visit type; it does not tell you what that visit type costs. The platform should ingest the branch's point schedule as a pay input, and separately model true time cost from CMS minutes plus the branch's own documentation cycle times — and then show the branch where its point schedule diverges from its actual cost. That divergence *is* the cherry-picking risk, quantified.

---

## 4. Productivity standards

### 4.1 Published and reported visits per day

| Discipline / model | Standard | Source | Year |
|---|---|---|---|
| **SN/RN — national actual, unweighted** | **4.5 visits/day** | ✅ [SimiTree Financial Monitor](https://simitreehc.com/simitree-blog/data-analytics-snapshot-measure-nursing-productivity/) | Q4 2021 |
| SN/RN — legacy "traditional" standard | 6 visits/day | SimiTree, restating the legacy standard | — |
| **RN — nationwide full-time** | **~7 patients/day** | ✅ Fazzi Associates *State of the Industry*, cited in [Jarrín et al., PMC6175632](https://pmc.ncbi.nlm.nih.gov/articles/PMC6175632/) | 2017/2018 |
| RN — practitioner consensus | 5–6/day with a **35-patient caseload** | [allnurses](https://allnurses.com/national-standard-productivity-t695051/) | 2019 |
| Skilled clinicians — high end (per litigation filings) | "8 or more" patients/day | [Stephan Zouras LLP](https://www.stephanzouras.com/faqs-skilled-care-home-health-clinician-lawsuits/) | 2024 |
| **RN at hourly-paying agencies** | **3–4/day** | [allnurses](https://allnurses.com/pay-per-visit-vs-hourly-t757111/) (CA) | 2024 |
| PT | ~7/day; **35 visits/week** | [r/physicaltherapy](https://www.reddit.com/r/physicaltherapy/comments/11rf5up/is_35_visits_a_weekhome_health_overworking_or_is/) | 2023 |
| PT/OT on points | 6 points/day (30/wk) | [r/physicaltherapy](https://www.reddit.com/r/physicaltherapy/comments/1cmak9o/looking_for_help_understanding_the_point_system/) | 2024 |
| OT | 4–5 points/day | [OT Potential](https://otpotential.com/blog/ot-productivity-hacks) | 2021 |
| PT/OT/SLP as % productivity | 55–65% of an 8-hr day ≈ 288 billable min | [productivitycalc.com](https://productivitycalc.com/home-health-productivity-benchmarks/) — unattributed | 2026 |
| **LPN/LVN, PTA, COTA, MSW, HHA** | **No published standard found** | — | — |

### 4.2 The methodological trap that invalidates most benchmark comparisons

**SimiTree's 4.5 visits/day national figure is unweighted — no extra credit for admissions.** Agency internal targets of 5–6/day are usually *weighted*, with an SOC counting 2–3. The two numbers are not comparable, and conflating them is exactly how a branch tells itself "we're at benchmark" while its clinicians are structurally overloaded.

**This is the single most important thing the platform can fix.** Publishing a weighted and an unweighted productivity number side by side, computed from the branch's own visit mix, resolves an argument that agencies currently cannot settle.

Note also the range: the hourly-paid agencies at 3–4 visits/day and the per-visit agencies at 7–8 are not observing different clinicians. They are observing the same clinicians under different incentive structures, with the non-visit work either paid or unpaid. The 3–4 figure is what a visit day looks like when documentation happens on the clock.

### 4.3 What counts as a full caseload

- **35 patients** per case-managing RN at 5–6 visits/day (practitioner-reported, 2019)
- **25–30 points/week** across every points-paying agency reported (§3.3)
- ✅ [Forvis Mazars](https://www.forvismazars.us/forsights/2025/08/benchmarking-kpis-in-home-health-hospice-%E2%80%93-how-does-your-agency-measure-up) (2025-08-22) names *Cost Per Visit*, *Visit Productivity*, *Revenue Per Visit*, and *Gross Margin Per Episode* as the core home health KPIs — **but publishes no benchmark values.** The same pattern holds across McBee, Corridor, and HCP: the metric definitions are public, the numbers sit behind an engagement. This is a genuine market gap and part of why a platform that computes these from a branch's own data has standalone value.

---

## 5. Non-visit time: documentation, OASIS, coordination, travel

### 5.1 OASIS completion burden, as CMS estimates it

CMS builds its OASIS burden estimate bottom-up from the item count, valuing each data element at 0.15–0.30 minutes of clinician time. For **OASIS-E** (released 2023-01-01):

| Assessment timepoint | Data elements | CMS estimated clinician minutes |
|---|---|---|
| Start of Care (SOC) | 203 | **57.3** |
| Resumption of Care (ROC) | 172 | **48.0** |
| Follow-up / Recertification | 37 | **11.1** |
| Transfer of Care | 22 | **6.6** |
| Death at Home | 9 | **2.7** |
| Discharge | 146 | **40.2** |

Source: [CY 2023 HH PPS final rule, 87 FR 66877–66878](https://www.federalregister.gov/documents/2022/11/04/2022-23722/medicare-program-calendar-year-cy-2023-home-health-prospective-payment-system-rate-update-home-health) (published 2022-11-04). These are the OASIS-E estimates and remain CMS's working basis.

Version changes since:
- **OASIS-E1** (effective 2025-01-01) — item refinements; CMS did not publish a headline minutes delta comparable to the OASIS-E table above.
- **OASIS effective 2026-04-01** (finalized in the CY 2026 rule): removes four SDOH items (Living Situation, Food Runs Out, Food Doesn't Last, Utilities) at SOC and ROC, worth **−0.9 minutes per SOC/ROC assessment**, and removes the COVID-19 vaccination item at Transfer / Death at Home / Discharge, worth **−0.3 minutes each**. Aggregate national saving: **194,181 clinician hours/yr, or 16.31 hours per HHA per year** across 11,904 active HHAs. Source: [CY 2026 HH PPS final rule, 90 FR 55560–55564](https://www.federalregister.gov/documents/2025/12/02/2025-21767/medicare-and-medicaid-programs-calendar-year-2026-home-health-prospective-payment-system-hh-pps-rate) (2025).

**Read the size of that saving carefully: 16.31 hours per agency per year.** That is CMS's own accounting of a regulatory burden-reduction win. It is a rounding error against the actual documentation load, which tells you how far CMS's item-count method sits from operational reality.

**The critical caveat:** CMS's estimate is explicitly *"clinical time spent to complete data entry"* — keystroke time for the OASIS instrument alone. It excludes the assessment itself, the medication reconciliation, the plan-of-care build, the physician communication, the wound measurement, and the coordination calls that surround a start of care. Practitioner-reported total SOC documentation time runs far above 57.3 minutes. **A platform should treat 57.3 minutes as a defensible floor for OASIS data entry and should collect the branch's own SOC-to-lock cycle time as the real number.**

### 5.2 Travel and indirect time as a share of the workday

The strongest quantified time-and-motion evidence available is not from US Medicare home health, and this needs saying plainly. A cross-sectional observational study of 18 home health care nurses over 2–3 shifts each (196 observation sheets) in two Finnish municipal home care organizations found that across an 8-hour shift:

| Activity | Mean minutes/shift |
|---|---|
| **Indirect patient contact, total** | **241 (50% of shift)** |
| — Planning | 69 |
| — Documentation | 50 |
| — Travel | 48 |
| — Professional meetings | 42 |
| — Telephone calls | 20 |
| — Other | 40 |
| **Direct patient contact, total** | **~81–162 (38% of shift)**, at 27 min/visit × 3–6 visits |

Source: Näslindh-Ylispangar et al., *Scandinavian Journal of Caring Sciences*, [PMC7754451](https://pmc.ncbi.nlm.nih.gov/articles/PMC7754451/); data collected **autumn 2017**, published 2020.

**Caveat this hard.** Finnish municipal home care is a different service model with shorter visits (27 min mean vs CMS's 41.5–47.2 min for US skilled disciplines) and a different documentation regime. Do not import the absolute minutes. **Do import the structural finding, which is robust across every home care time study I could locate: roughly half of a home care clinician's paid day is not spent in front of a patient.** A companion Nordic study of home care time consumption found driving time at **18%–26% of the day** and visiting time at **40%–62%** ([PMC4263042](https://pmc.ncbi.nlm.nih.gov/articles/PMC4263042/)).

### 5.3 Miles driven

- National average **~11.0 miles per visit** (2013), per the Foundation for Hospice and Homecare / NAHC analysis of 718M visits and ~8B miles ([PHI summary](https://www.phinational.org/report-home-care-professionals-traveled-8-billion-miles-in-13/)). State range: Maine 35.2 mi/trip, Virginia 16.71 mi/trip.
- Practitioner-reported daily mileage clusters around **50–75 miles per shift**, with 25–50 miles common in dense territories and 140–180 miles reported on heavy rural days. These are **anecdotal, forum- and vendor-sourced, not survey-grade** — see [allnurses home health threads](https://allnurses.com/how-many-visits-t214633/) and vendor commentary. Use them to bound a model, never to defend one.

### 5.4 The productive-hours reality

CMS gives one hard, citable ceiling: for outlier cost estimation, CMS **caps countable clinician time at 8 hours (32 fifteen-minute units) per day summed across all six disciplines** ([CY 2017 HH PPS final rule, 81 FR 76725](https://www.federalregister.gov/documents/2016/11/03/2016-26290/medicare-and-medicaid-programs-cy-2017-home-health-prospective-payment-system-rate-update-home-health), 2016). CMS will not pay for more than 8 clinician-hours per patient-day no matter what is documented.

**ILLUSTRATIVE productive-hours build for one FTE clinician.** Assumptions listed below.

| Line | Hours |
|---|---|
| Paid hours per year (40 × 52) | 2,080 |
| Less PTO, holidays, sick (assume 25 days) | −200 |
| Less orientation, training, competencies, staff meetings (assume 60 hrs) | −60 |
| **Available field hours** | **1,820** |
| Less travel (assume 20% of available) | −364 |
| Less documentation and coordination outside the home (assume 25% of available) | −455 |
| **In-home visit hours** | **~1,001** |
| At 45 min average in-home time per visit | **~1,335 visits/yr** |
| Over 228 available field days | **~5.9 visits/day** |

Assumptions: (1) 25 PTO/holiday/sick days; (2) 60 hours of non-clinical training and meetings; (3) travel at 20% and out-of-home documentation at 25% of available time — both drawn from the *structure* of the time-motion literature in §5.2, not from a US benchmark; (4) 45-minute average in-home time, between CMS's SN 41.5 and SLP 47.2; (5) no admissions weighting — a caseload heavy in SOCs produces materially fewer visits.

Note how sensitive this is: move documentation from 25% to 35% of available time and the same clinician drops from 5.9 to 4.9 visits/day — a 17% capacity loss from one assumption. **That sensitivity is the whole argument for the platform collecting real branch data rather than shipping a default.**

---

## 6. Turnover: rates, replacement cost, and the scheduling link

### 6.1 The scheduling-to-turnover link — the best evidence available

Bergman, Song, David, Spetz, and Candon analyzed HR, payroll, and visit-level data from a top-five US home health organization: **3,716 nurses across 30+ states, January 2016 – March 2019.** Schedule volatility was operationalized as the coefficient of variation of daily visit count over the prior 28 days.

Findings:
- **Full-time RNs at the 75th percentile of schedule volatility were 16% more likely to quit than average; full-time LPNs, 34% more likely.**
- **Moving a full-time RN from the 75th to the 25th percentile of volatility cut annual quit probability by 9.2 percentage points.**
- The relationship **disappeared entirely for part-time nurses.** The authors attribute this to the mechanism being income and schedule instability for people who depend on the job.
- Baseline voluntary separation in the same dataset: **FT RN 27.14%, FT LPN 20.15%, PT RN 32.33%, PT LPN 28.18%.**

Sources: [Bergman et al., *Medical Care Research and Review*, 2021 — PMC9122113](https://pmc.ncbi.nlm.nih.gov/articles/PMC9122113/) (primary); [Penn LDI research summary](https://ldi.upenn.edu/our-work/research-updates/smarter-scheduling-in-home-health-care/) (2021-08-02), which frames the same result at the 5th/95th percentiles as 40% less likely and 50% more likely to quit respectively. Data years: **2016–2019**.

This is the single most useful citation in this file for a scheduling platform. It says, from payroll and scheduling data at scale, that *how* you schedule — not just how much you pay — changes retention, and it quantifies the effect. It gives the platform a directly actionable metric: **schedule volatility (coefficient of variation of daily visit count over a trailing 28 days) is a leading indicator of quit risk, computable from data the platform already holds.**

The part-time null result is equally important and cuts against overselling: stabilizing a PRN pool's schedule should not be expected to reduce its turnover. Segment the claim by employment status or it will not survive contact with a customer's data.

### 6.2 Turnover rates

**Skilled home health** — do not conflate these with private-duty home care, which runs three times higher:

| Role | Rate | Source | Year |
|---|---|---|---|
| **RN (home care / home health)** | **25.46%** | ✅ HCS *Home Care Salary & Benefits Report*, via [HHCN](https://homehealthcarenews.com/2025/11/home-health-worker-retention-improves-as-wages-bonuses-increase-in-2025/) | 2025 |
| **Home care aide / CNA** | **34.17%** (down from 36.31% in 2024) | ✅ HCS 2025 via HHCN | 2025 |
| Home health, all staff | 22.18%; **therapist positions 13.88%** | ✅ [HHCN](https://homehealthcarenews.com/2020/10/home-health-turnover-rate-hits-22-18/) | 2020 |
| FT RN, voluntary separation | 27.14% | ✅ [Bergman et al., PMC9122113](https://pmc.ncbi.nlm.nih.gov/articles/PMC9122113/) | 2016–2019 |
| FT LPN | 20.15% | ✅ same | 2016–2019 |
| PT (part-time) RN / LPN | 32.33% / 28.18% | ✅ same | 2016–2019 |
| RN & LPN, home health + hospice | >10% per quarter (≈40%+ annualized) | ✅ Luo, Lin & Castle 2012, via PMC9122113 | 2012 |
| Home health nurse | 28% | ⚠️ [Medbridge](https://www.medbridge.com/blog/breaking-the-home-health-nurse-turnover-cycle) (vendor, secondary) | 2023 |

**Trend read: home health RN turnover sits in a stable 25–28% band; therapy runs roughly half that; aides run 34%+.** For contrast, [NSI's 2026 National Health Care Retention & RN Staffing Report](https://www.nsinursingsolutions.com/documents/library/nsi_national_health_care_retention_report.pdf) puts **hospital** RN turnover at 17.6%, PT at 11.1%, CNA at 32.5% — meaning home health RN turnover runs roughly **8 points above hospital RN**.

**Private-duty home care** (different industry; cited constantly as if it weren't): caregiver turnover **75.5%** in 2025, ~75% in 2024, ~79–80% in 2023, 77% in 2022 — [Activated Insights 2026 Benchmarking Report](https://activatedinsights.com/latest-news/activated-insights-releases-2025-benchmarking-report-unveiling-key-drivers-of-retention-and-revenue-in-home-based-care-industry/); [HHCN 2024](https://homehealthcarenews.com/2024/07/home-cares-industry-wide-turnover-rate-reaches-nearly-80/); [HHCN 2023](https://homehealthcarenews.com/2023/05/after-dipping-for-three-years-home-care-turnover-rate-soared-to-77-in-2022/). **Never use these numbers for a Medicare-certified skilled agency.**

### 6.3 Cost to replace a clinician

| Figure | Role / setting | Basis | Source | Year |
|---|---|---|---|---|
| **$60,000** avg; hospital loses $4.2M–$6.2M/yr | Bedside RN, **hospital** | Annual employer survey | ✅ [NSI 2026](https://www.nsinursingsolutions.com/documents/library/nsi_national_health_care_retention_report.pdf) | 2026 |
| $61,110 (range $49,500–$72,700), +8.6% YoY | Staff RN, **hospital** | NSI-derived | ✅ [WI Center for Nursing](https://wicenterfornursing.org/cost-of-nurse-turnover/) | 2025 |
| **$21,514 – $88,000, ≈1.3× annual salary** | RN, mixed settings | Systematic review of published replacement-cost studies | ✅ [PMC12994890](https://pmc.ncbi.nlm.nih.gov/articles/PMC12994890/) | 2025 |
| >$100,000 inflation-adjusted | RN | Jones 2008 | ✅ via [PMC9122113](https://pmc.ncbi.nlm.nih.gov/articles/PMC9122113/) | 2008 |
| $2,600/caregiver; $171,600/yr per agency | Caregiver, **private duty** | 16% of a $16,300 annual income | ✅ [Activated Insights](https://activatedinsights.com/articles/much-caregiver-turnover-really-costing-business/) | — |
| $951–$1,242 self-reported; avg $2,627; policy estimate $4,200–$5,200 | Home health agency workers | Compilation of 1990s-era studies — **badly dated** | ✅ [PHI, *The Cost of Frontline Turnover in Long-Term Care*](https://www.phinational.org/wp-content/uploads/legacy/clearinghouse/TOCostReport.pdf) | ~2004 |
| >$36,000 per FT nurse | Nurse, home health | **No methodology disclosed** | ⚠️ [Alora Health](https://www.alorahealth.com/preventing-caregiver-turnover/) — unverified | — |

**Flag this clearly: there is no rigorously sourced, home-health-specific RN or therapist replacement cost in the published literature.** Every credible dollar figure is hospital-derived. The defensible construction is the systematic-review multiplier of **≈1.3× annual salary** applied to a home health RN salary, with the transfer stated openly.

**ILLUSTRATIVE — the retention half of the value case.** Assumptions: home health RN fully loaded at ~$95,000; replacement cost at 1.3× salary = ~$124,000; Bergman et al.'s 9.2 percentage-point reduction in annual quit probability from moving an RN from the 75th to the 25th percentile of schedule volatility.
- Avoided replacement cost per FT RN per year = 0.092 × $124,000 ≈ **$11,400**
- Across a 20-RN branch, if the intervention reaches even half the roster: **~$114,000/yr**

Stated conservatively against a base salary rather than fully loaded cost (~$80,000 × 1.3 = $104,000), the per-RN figure is ~$9,600. **Either way, the retention case is roughly a third the size of the contract-labor-substitution case in §2.2 — real, defensible, and worth quoting second, not first.**

### 6.4 Other work-design evidence

| Finding | Source | Strength |
|---|---|---|
| Home health nurses are the **least satisfied group of nurses**, driven by work demands; study participants averaged **7 visits/day**; high productivity requirements, case overload, and time-consuming documentation cited | ✅ [Jarrín et al., "How Home Health Nurses Plan Their Work Schedules," 2018 — PMC6175632](https://pmc.ncbi.nlm.nih.gov/articles/PMC6175632/) | Qualitative but well-cited |
| Home health agencies with **good work environments** have lower nurse burnout **and** better patient outcomes — lower acute hospitalization, higher discharge-to-community | ✅ Jarrín, Flynn, Lake & Aiken 2014, via PMC6175632 | Directly links work design to HHVBP-scored outcomes |
| **Independence and flexibility** are the top drivers of home health nurse job satisfaction | ✅ [McCreary, *Geriatric Nursing*](https://www.sciencedirect.com/science/article/pii/S0029646519300878) | Explains why per-visit pay survives despite its costs — and warns against optimizers that feel like surveillance |
| Wage increases and sign-on bonuses measurably reduced turnover; **36% of agencies reported turnover decreased**, fewer than 21% reported an increase | ✅ HCS 2025 via [HHCN](https://homehealthcarenews.com/2025/11/home-health-worker-retention-improves-as-wages-bonuses-increase-in-2025/) | Survey of 1,111 agencies |

That last row matters commercially: the industry's current retention lever is **money** — the HCS 2025 report puts the average RN sign-on bonus at **$7,499** and average home care RN hourly at **$41.79** (up 3.56% from $40.36). A scheduling intervention that buys a comparable retention effect without a permanent wage increase is competing against a $7,499 one-time cost per hire, and should be priced against it.

---

## 7. Wage index and labor share

### 7.1 What CMS treats as labor

For **CY 2024 and all subsequent years**, CMS sets the home health **labor-related share at 74.9%** and the non-labor-related share at **25.1%**. It was 76.1% / 23.9% under the 2016-based market basket. The 74.9% is the Compensation cost weight (Wages & Salaries plus Benefits, *including direct patient care contract labor*) of the 2021-based home health market basket, derived from **2021 Medicare cost reports on Form CMS-1728-20**.

Sources: [CY 2024 HH PPS final rule, 88 FR 77726–77742](https://www.federalregister.gov/documents/2023/11/13/2023-24455/medicare-program-calendar-year-cy-2024-home-health-hh-prospective-payment-system-rate-update-hh) (2023); reaffirmed in the [CY 2026 HH PPS final rule, 90 FR 55399–55400 and 55405–55406](https://www.federalregister.gov/documents/2025/12/02/2025-21767/medicare-and-medicaid-programs-calendar-year-2026-home-health-prospective-payment-system-hh-pps-rate) (2025).

Two structural details a cost model must get right:

1. **Transportation is a separate market basket cost weight and sits in the non-labor 25.1%.** Mileage and vehicle cost are therefore *not* wage-index-adjusted. An agency in a high-wage-index market gets no extra payment for its fuel; an agency in a low-wage-index market is not docked for it. For a rural branch with long drives and a low wage index, that is a double squeeze.
2. **Commenters on the CY 2024 rule objected that the drop from 76.1% to 74.9% contradicted their lived experience of rising labor cost.** CMS's response: the decline is real in the cost report data and is driven mainly by how direct patient care contract labor was reported, and the labor-related share has been trending downward since 2010. CMS also noted that non-direct-patient-care contract labor reported in the Administrative & General cost center falls into the residual "All Other" weight and is therefore *outside* the labor-related share entirely. **Translation for the platform: a branch that runs heavy on agency/contract labor is systematically underrepresented in the payment formula's labor share.**

### 7.2 How the wage index actually moves payment

The mechanics, per the CY 2026 rule:
- Multiply the national standardized 30-day rate by the case-mix weight.
- Split into labor (74.9%) and non-labor (25.1%).
- Multiply the labor portion by the CBSA wage index for the **beneficiary's site of service** (not the agency's location).
- Add back the non-labor portion.

The wage index used is the **FY 2026 hospital pre-floor, pre-reclassified wage index**, with a **permanent 5% cap on year-over-year wage index decreases**, in effect for CY 2023 and every year since. Source: [CY 2026 HH PPS final rule, 90 FR ~55403–55406](https://www.federalregister.gov/documents/2025/12/02/2025-21767/medicare-and-medicaid-programs-calendar-year-2026-home-health-prospective-payment-system-hh-pps-rate) (2025).

**ILLUSTRATIVE — the compression effect.** Assumption: only the arithmetic of the 74.9/25.1 split; payment multiplier = 0.749 × WI + 0.251.

| Area wage index | Payment multiplier vs national | Wage gap vs national | Payment gap vs national |
|---|---|---|---|
| 0.70 | 0.775 | −30% | −22.5% |
| 0.80 | 0.850 | −20% | −15.0% |
| 0.90 | 0.925 | −10% | −7.5% |
| 1.00 | 1.000 | 0% | 0% |
| 1.20 | 1.150 | +20% | +15.0% |
| 1.40 | 1.300 | +40% | +30.0% |
| 1.60 | 1.449 | +60% | +44.9% |

**This is the cost-to-payment misalignment in one table, and it cuts both ways.** Because 25.1% of payment is held flat, the payment adjustment is always *smaller* than the underlying wage differential. A high-wage market is systematically under-compensated for its wage premium; a low-wage market is systematically over-compensated. Two further wrinkles amplify it:

- The wage index is derived from **hospital** wage data, not home health wage data. Home health labor markets do not move in lockstep with hospital labor markets, and the divergence is largest exactly where it matters — nursing and therapy in metro areas with academic medical centers.
- The index applies to the **patient's location**, so an agency serving a mixed metro/exurban territory has a blended effective wage index that no single number in its budget captures, while paying its clinicians one wage regardless of which patient they drive to.

**Practical consequence for the platform:** margin per visit is not uniform across a branch's territory. Two identical SN visits by the same clinician on the same day can carry payment that differs by 15–30% purely on the patient's county. A capacity model that treats all visits as equally valuable is leaving that on the table; a model that surfaces wage-index-adjusted contribution margin per visit is doing something no scheduling board does today.

### 7.3 CY 2026 payment parameters, for reference

| Parameter | CY 2026 value | Source |
|---|---|---|
| National standardized 30-day period payment | **$2,038.22** | [CMS fact sheet CMS-1828-F](https://www.cms.gov/newsroom/fact-sheets/calendar-year-cy-2026-home-health-prospective-payment-system-final-rule-cms-1828-f) (2025-11-28); [Homecare Homebase summary](https://hchb.com/cms-publishes-2026-home-health-final-rule/) |
| Home health payment update (market basket, net) | +2.4% | same |
| Permanent behavior adjustment | −1.023% (factor 0.98977) | CY 2026 final rule |
| Temporary behavior adjustment (CY 2026 only) | −3.0% (factor 0.97000) | CY 2026 final rule |
| Case-mix recalibration budget neutrality factor | 1.0052 | CY 2026 final rule |
| Wage index budget neutrality factor (non-LUPA / LUPA) | 1.0025 / 1.0005 | CY 2026 final rule |
| Aggregate payment impact vs CY 2025 | −1.3% (−$220M) | CMS fact sheet |
| Labor-related share / non-labor | 74.9% / 25.1% | CY 2024 rule, unchanged |
| Wage index decrease cap | 5% | permanent since CY 2023 |
| LUPA thresholds | 2–5 visits per 30-day period, by payment group | MedPAC Mar 2026 Ch.8 note to Table 8-4 |

**CY 2026 national per-visit (LUPA) rates**, for HHAs submitting quality data:

| Discipline | CY 2026 per-visit rate | LUPA add-on factor | First-visit LUPA amount |
|---|---|---|---|
| Skilled nursing | **$176.96** | 1.7200 | $304.37 |
| Physical therapy | **$193.42** | 1.6225 | $313.82 |
| Occupational therapy | **$194.74** | 1.7238 | $335.69 |
| Speech-language pathology | **$210.25** | 1.6696 | $351.03 |
| Medical social services | **$283.64** | n/a | n/a |
| Home health aide | **$80.12** | n/a | n/a |

Sources: [CY 2026 HH PPS final rule](https://www.federalregister.gov/documents/2025/12/02/2025-21767/medicare-and-medicaid-programs-calendar-year-2026-home-health-prospective-payment-system-hh-pps-rate) Table 16 (2025); values confirmed in [Homecare Homebase's rule summary](https://hchb.com/cms-publishes-2026-home-health-final-rule/) (2025).

These per-visit rates are the closest thing to a **CMS-blessed relative value scale across disciplines**. They are not costs — MSS at $283.64 reflects rarity and payment policy, not that a social work visit costs 3.5× an aide visit — but they are a legitimate, citable relative-weight starting point when a branch has no internal cost accounting, and they are the *actual* revenue for any period that falls below its LUPA threshold.

---

## 8. The capacity math: FTE → defensible weekly visit capacity

### 8.1 The formula

```
Weekly visit capacity (weighted) =
      Available field hours per week
    − Travel hours
    − Non-visit clinical hours (documentation, coordination, OASIS, case conference, on-call follow-up)
    ─────────────────────────────────────────────────────────────
    ÷ Weighted average in-home minutes per visit (weighted by the clinician's actual visit mix)
```

Then convert weighted capacity to raw visit count using the admission/recert/routine mix, because a caseload heavy in SOCs produces fewer visits from the same hours.

### 8.2 The assumptions that go into it

| Assumption | Defensible source | Typical sensitivity |
|---|---|---|
| Paid hours/week | Branch payroll | Low |
| PTO/holiday/training deduction | Branch HR | Moderate — 25 days ≈ 10% of the year |
| In-home minutes per visit by discipline | CMS CY2023 claims: SN 41.5, PT 45.1, OT 46.0, SLP 47.2 (§0) | Low — well-sourced |
| First-visit premium | CMS: 1.62×–1.72× (§0) | Low — well-sourced |
| Travel share of the day | 18%–26% in Nordic time studies (§5.2); no verified US benchmark | **Very high** |
| Documentation/coordination share | ~25%–35% in the same literature; CMS OASIS data-entry floors in §5.1 | **Very high** |
| Visit mix (SOC / ROC / recert / routine / discharge) | Branch's own OASIS and claims data | **Very high** |
| Weekend, on-call, and holiday coverage load | Branch schedule | Moderate |

### 8.3 What people get wrong

1. **Using paid hours instead of available field hours.** 2,080 is never the denominator. After PTO, training, and meetings it is closer to 1,820, and that is before travel or documentation.
2. **Treating all visits as one unit.** CMS's own data says an admission is 1.7 routine visits *in the home* and considerably more once the OASIS and plan of care are counted. A branch that grows its admission share and holds its visits-per-day standard constant has silently cut its clinicians' pay-per-hour and raised its turnover risk.
3. **Modeling travel as a fixed per-visit constant.** Travel is a function of *route density*, which is a function of the schedule the platform is producing. It is endogenous. A capacity model that holds travel constant cannot represent the benefit of better routing — which is the product's whole thesis.
4. **Ignoring documentation lag.** Documentation deferred is not documentation avoided. A capacity model that excludes it will show capacity that exists on paper and is being paid for in unbilled evenings, OASIS accuracy, and attrition.
5. **Assuming the marginal visit has the marginal cost of the average visit.** It does not, in either direction: for a salaried clinician the marginal visit is nearly free until the ceiling and then extremely expensive past it; for a contractor it is flat.
6. **Using national averages for a specific branch.** Every high-sensitivity input in the table above is local. The national numbers in this file are for sanity-checking a branch's own numbers, not for replacing them.
7. **Not accounting for the LUPA cliff.** A 30-day period that comes in one visit below its threshold (thresholds run 2–5 visits) converts from a ~$2,038 case-mix-adjusted payment to a per-visit payment. Capacity decisions that shave a visit off a marginal period can destroy far more revenue than the visit costs. **A capacity optimizer that is LUPA-blind is dangerous.**
8. **Forgetting the wage index varies within the territory.** §7.2.

### 8.4 An illustrative capacity model

**ILLUSTRATIVE.** One full-time SN case manager, employed and salaried, urban-suburban territory.

| Line | Value | Basis |
|---|---|---|
| Paid hours/week | 40.0 | assumption |
| PTO/holiday/training equivalent | −3.8 | 25 days + 60 hrs training, annualized |
| Available field hours/week | 36.2 | derived |
| Travel @ 22% | −8.0 | midpoint of 18–26% (Nordic studies, §5.2) |
| Documentation/coordination @ 28% | −10.1 | assumption informed by §5.1–5.2 |
| **In-home hours/week** | **18.1** | derived |
| Visit mix | 15% SOC/ROC, 10% recert, 70% routine, 5% discharge | assumption |
| Weighted avg in-home minutes | 41.5 × (0.85 + 0.15×1.72) = **~50.9** | CMS §0 |
| **Visits/week** | **~21.3** | derived |
| **Visits/day (4.75-day week)** | **~4.5** | derived |
| Loaded annual compensation cost | $44.99/hr × 1.515 × 2,080 = **$141,700** | OEWS May 2025 mean + ECEC Mar 2026 RN multiplier |
| **Compensation cost per visit** | $141,700 ÷ (21.3 × 46.4 wks) = **~$143** | derived |
| Plus overhead @ 49% of compensation | **+$70** | CMS-implied, §1.3 |
| **Fully allocated cost per visit** | **~$213** | derived |

Assumptions restated: salaried W-2 RN paid at the *national home health mean* of $44.99/hr (the P10–P90 range is $31.90–$60.62, so this number moves ±35% on wage alone); 46.4 productive weeks; travel at 22% and documentation at 28% of available hours, from non-US time-motion literature; visit mix assumed; overhead load inferred nationally, not measured; no supplies, no supervision-of-LPN time, no on-call.

**Reconcile the two illustrative models.** §1.5's bottom-up per-visit build gave ~$138 fully allocated for a routine SN visit; this FTE-down model gives ~$213 for the same clinician's *average* visit. The difference is not an error — it is the two things the per-visit build leaves out: **PTO/training/meeting hours that are paid but produce no visit, and the admission-weighted mix.** The FTE-down number is the honest one for capacity planning; the per-visit number is the honest one for pricing a marginal visit. **A platform needs both, and needs to label which is which**, because presenting the per-visit figure as the cost of a clinician-day understates cost by roughly a third — and that is precisely the error that makes agencies believe they have capacity they do not have.

Sanity check against Anchor 3: MedPAC's blended derived cost was ~$193/visit in 2024 across all disciplines. This model's ~$213 for nursing at the national mean wage sits just above it, which is consistent — MedPAC's blend includes cheaper aide visits and is a year older.

---

## What a branch must supply from its own finance data

No public source can produce these, and the platform's cost engine is guesswork without them. Ask for them explicitly, in this order of importance.

**Compensation structure — ask first, because it changes everything else**
1. For each discipline, the count of field clinicians by pay model: salaried exempt, salaried non-exempt, hourly, per-visit, points/weighted, PRN/per-diem, contract.
2. The actual pay rates: annual salary bands by discipline; hourly rates; per-visit rates *by visit type* (SOC, ROC, recert, routine, discharge, eval, supervisory, weekend/holiday, after-hours).
3. If a points system is in use: the full point schedule by visit type, the dollar value per point, the weekly point target by discipline, and whether points sit on top of a base salary or replace hourly pay.
4. Overtime policy and actual OT hours paid by discipline, last 12 months.
5. Contract/agency labor: bill rates by discipline and visit type, and total contract spend and visit volume by month for the last 12 months.

**Benefit and payroll load**
6. Actual employer benefit cost per FTE by discipline — health, dental, vision, retirement match, life/disability — and the participation rate (an offered benefit that 40% of staff decline costs the branch far less than the sticker).
7. State unemployment insurance (SUTA) rate and workers' compensation rate for its clinical class codes. Workers' comp for field clinicians varies severalfold by state and by loss history.
8. PTO accrual and actual PTO taken by discipline, plus holidays paid.

**Travel**
9. Mileage reimbursement rate and, critically, the **reimbursement policy** — is the first leg from home reimbursed? the last leg back? Policy drives reimbursable miles far more than territory does.
10. Actual miles reimbursed per clinician per month, last 12 months.
11. Whether any clinicians have vehicle allowances or company vehicles rather than mileage.

**Time and productivity — from the EMR, not from policy documents**
12. Actual visits per clinician per day and per week, last 12 months, by discipline, split by visit type.
13. **Visit-to-documentation-lock cycle time** by visit type — the real SOC documentation burden lives here, and it is the number that most contradicts the official productivity standard.
14. The branch's *stated* productivity standard and its actual attainment rate against it.
15. Time-stamped visit start/end from the EMR or EVV feed, if it exists. This is the single highest-value dataset the branch owns.

**Overhead — the hardest ask and the most necessary**
16. Total branch operating expense for the last 12 months, split into: direct field clinician compensation; clinical supervision and clinical management; intake/referral/scheduling; QA/coding/OASIS review; billing/collections/RCM; occupancy; software and EMR; corporate allocation.
17. **The corporate allocation methodology** — how much of the parent's cost lands on this branch, and on what basis (revenue? visits? headcount?). This determines whether "cost per visit" is a real number or an accounting artifact, and it is the number most likely to be internally contested.
18. Medical supply cost per visit type.
19. Total visits and total 30-day periods for the same 12 months, so cost per visit and cost per period can actually be computed.

**Payer and revenue mix — because cost without payment is only half the model**
20. Payer mix by volume and by revenue: Medicare FFS, Medicare Advantage by plan, Medicaid, managed Medicaid, commercial, private pay.
21. **Contracted rates by MA plan**, per-visit or per-episode. MA rates are usually well below FFS, they are the reason the all-payer margin is 5.0% against a 21.2% FFS margin, and no public source has them.
22. The wage index values actually applicable across the branch's service counties, and the share of volume in each.
23. LUPA rate — the share of 30-day periods that came in under threshold — and the revenue lost to it.
24. Case-mix weight distribution across periods, so revenue per period can be modeled rather than assumed at the national $2,038.22.

**Turnover — to size the retention half of the value case**
25. Voluntary and involuntary turnover by discipline for the last 24 months, and tenure at separation.
26. Actual cost to fill an open clinical position: recruiter or agency fee, sign-on bonus, job advertising, orientation hours paid before the first independent visit, preceptor hours consumed, and the contract-labor spend used to cover the vacancy.
27. Average days-to-fill by discipline, and the referral volume declined or diverted during vacancies.

**One framing note for the platform's UX.** Items 12, 13, 15, 19 and 25 are usually retrievable from systems the branch already runs, and should be requested as data exports. Items 16, 17, 21 and 26 usually require a finance person to construct them and will be the slowest part of any onboarding. Design the model to produce a credible answer from the first group alone, with public defaults from this file standing in for the second group — and show the user exactly how much the answer moves when the real overhead and MA rate numbers arrive. The width of that band is an honest and persuasive thing to show a prospect.

---

## Known gaps — what this file could not verify

Stated plainly so nothing here gets quoted as settled when it isn't.

| Gap | Why it matters | Best path to close it |
|---|---|---|
| **No published national split of clinicians by pay model** (per-visit / hourly / salaried / points) | Determines whether the §2.2 margin thesis applies to a given branch at all — the platform's single most important qualifying question | HCS *Home Care Salary & Benefits Report* (~$400 non-participant; 1,111 agencies, 52,200+ employees, data effective July 2025) — it carries pay mode, caseload/productivity, and turnover by job code in one instrument. **Highest-value purchase for this research program.** |
| **No published home health staffing-agency / contract bill rates** for SN, PT, OT, ST | The §2.2 substitution prize is computed against this number | No authoritative source exists. Assemble from branch contract invoices; per-diem marketplace listings are a weak proxy |
| **No home-health-specific RN or therapist replacement cost** in the literature | The §6.3 retention case rests on a hospital-derived 1.3× salary multiplier | Branch HR data (recruiter fees, sign-on, orientation hours, vacancy contract-labor spend) |
| **No published visits-per-day standard** for LPN/LVN, PTA, COTA, MSW, or HHA | Half the disciplines have no capacity anchor at all | Branch EMR visit data |
| **No NCCI class 8835 workers' compensation rates** verified | WC for home health is materially above the 1.29% all-industry ECEC average, driven by driving and patient-handling exposure, and varies severalfold by state | Branch's WC policy declarations page |
| **No US home health time-and-motion study** with travel and documentation shares | §5.2 and the §8 capacity model lean on Nordic studies with a different service model | Branch EVV/EMR timestamps — the branch owns better data than any published study |
| **No newer national miles-per-visit figure than 2013** | Mileage cost per visit and route-density modeling both depend on it | Branch mileage reimbursement records |
| **No published benchmark values from Forvis Mazars, McBee, Corridor, or HCP** | They publish the KPI definitions and withhold the numbers | Paid engagement, or compute from the branch's own data — which is arguably the product |
| **OASIS-E1 (2025-01-01) minutes delta** not published by CMS in comparable form | §5.1's burden table is OASIS-E (2023), one version stale | CMS OASIS information collection package, OMB control 0938-0760 |
| Practitioner-reported California per-visit litigation outcomes | Cited in §3.4 as reported but the specific cases were not confirmed | Court records |

Sources marked ✅ in this file are published or institutional; ⚠️ marks vendor or SEO content usable only directionally; forum and Reddit citations are labeled inline as practitioner-reported and are **not** benchmarks.

---

## Source index

| Source | Data year | URL |
|---|---|---|
| CMS, CY 2026 HH PPS final rule (CMS-1828-F), 90 FR | 2025 (rates), 2023–2024 (claims analyses) | https://www.federalregister.gov/documents/2025/12/02/2025-21767/medicare-and-medicaid-programs-calendar-year-2026-home-health-prospective-payment-system-hh-pps-rate |
| CMS fact sheet, CY 2026 HH PPS final rule | 2025-11-28 | https://www.cms.gov/newsroom/fact-sheets/calendar-year-cy-2026-home-health-prospective-payment-system-final-rule-cms-1828-f |
| CMS, CY 2025 HH PPS final rule, 89 FR 88426–88427 (LUPA add-on minutes) | 2023 claims | https://www.federalregister.gov/documents/2024/11/07/2024-25441/medicare-program-calendar-year-cy-2025-home-health-prospective-payment-system-updates-home-health |
| CMS, CY 2024 HH PPS final rule, 88 FR 77726–77742 (labor-related share rebasing) | 2021 cost reports | https://www.federalregister.gov/documents/2023/11/13/2023-24455/medicare-program-calendar-year-cy-2024-home-health-hh-prospective-payment-system-rate-update-hh |
| CMS, CY 2023 HH PPS final rule, 87 FR 66877–66878 (OASIS-E burden) | 2020 assessment counts | https://www.federalregister.gov/documents/2022/11/04/2022-23722/medicare-program-calendar-year-cy-2023-home-health-prospective-payment-system-rate-update-home-health |
| MedPAC, March 2026 Report to Congress, Chapter 8 | 2024 | https://www.medpac.gov/wp-content/uploads/2026/03/Mar26_Ch8_MedPAC_Report_To_Congress_SEC.pdf |
| IRS, Standard Mileage Rates | 2011–2026 | https://www.irs.gov/tax-professionals/standard-mileage-rates |
| Bergman, Song, David, Spetz, Candon — schedule volatility and HH nurse turnover, *MCRR* | 2016–2019 | https://ldi.upenn.edu/our-work/research-updates/smarter-scheduling-in-home-health-care/ |
| Näslindh-Ylispangar et al., HHC nurse time-and-motion, *Scand J Caring Sci* | 2017 (Finland) | https://pmc.ncbi.nlm.nih.gov/articles/PMC7754451/ |
| Nordic home care time consumption study | — | https://pmc.ncbi.nlm.nih.gov/articles/PMC4263042/ |
| Foundation for Hospice and Homecare / NAHC, miles driven | 2013 | https://www.phinational.org/report-home-care-professionals-traveled-8-billion-miles-in-13/ |
| Homecare Homebase, CY 2026 final rule summary (rate confirmation) | 2025 | https://hchb.com/cms-publishes-2026-home-health-final-rule/ |
| **BLS OEWS national + industry files (NAICS 621600)** | **May 2025** (rel. 2026-05-15) | https://www.bls.gov/oes/special-requests/oesm25nat.zip · https://www.bls.gov/oes/special-requests/oesm25in4.zip · https://data.bls.gov/oes/#/industry/621600/2025 |
| **BLS Employer Costs for Employee Compensation** | **March 2026** (rel. 2026-06-12) | https://www.bls.gov/news.release/ecec.nr0.htm · https://www.bls.gov/news.release/ecec.t01.htm · https://www.bls.gov/news.release/ecec.t04.htm |
| SSA, Social Security wage base | 2024–2026 | https://www.ssa.gov/oact/cola/cbb.html |
| Bergman et al., schedule volatility and turnover (primary, PMC) | 2016–2019 | https://pmc.ncbi.nlm.nih.gov/articles/PMC9122113/ |
| Jarrín et al., how home health nurses plan their work schedules | 2018 | https://pmc.ncbi.nlm.nih.gov/articles/PMC6175632/ |
| Systematic review, RN replacement cost (≈1.3× salary) | 2025 | https://pmc.ncbi.nlm.nih.gov/articles/PMC12994890/ |
| NSI National Health Care Retention & RN Staffing Report | 2026 | https://www.nsinursingsolutions.com/documents/library/nsi_national_health_care_retention_report.pdf |
| HCS *Home Care Salary & Benefits Report* (paywalled; fragments via HHCN) | 2025 (data eff. Jul 2025) | https://hhcsinc.com/hcs-reports/home-care-salary-benefits-report/ · https://homehealthcarenews.com/2025/11/home-health-worker-retention-improves-as-wages-bonuses-increase-in-2025/ |
| SimiTree Financial Monitor, nursing productivity (4.5 visits/day) | Q4 2021 | https://simitreehc.com/simitree-blog/data-analytics-snapshot-measure-nursing-productivity/ |
| Forvis Mazars, home health KPI definitions (no values published) | 2025 | https://www.forvismazars.us/forsights/2025/08/benchmarking-kpis-in-home-health-hospice-%E2%80%93-how-does-your-agency-measure-up |
| Fisher Phillips, 12 perils of per-visit compensation plans (FLSA) | 2024 | https://www.fisherphillips.com/en/insights/insights/biggest-perils-with-per-visit-compensation-plans-homecare-workers-what-employers-can-do |
| Activated Insights Benchmarking Report (private duty — do NOT use for skilled) | 2025/2026 | https://activatedinsights.com/latest-news/activated-insights-releases-2025-benchmarking-report-unveiling-key-drivers-of-retention-and-revenue-in-home-based-care-industry/ |
| PHI, *The Cost of Frontline Turnover in Long-Term Care* (badly dated) | ~2004 | https://www.phinational.org/wp-content/uploads/legacy/clearinghouse/TOCostReport.pdf |
| allnurses / Reddit / OT Potential — points values, per-visit rates, productivity | 2014–2024 | practitioner-reported, cited inline; **not benchmarks** |
