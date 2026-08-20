# Medicare Advantage: How MA Plans Pay for Home Health and What They Require

Research file for the CCSI branch capacity-and-scheduling platform.
Compiled **2026-08-18**. Every claim carries an inline source URL and a date.

**How to read the confidence labels used throughout:**

| Label | Meaning |
|---|---|
| **[PRIMARY]** | Verified against a government, regulatory, or payer-published primary document that I fetched and read. |
| **[PRIMARY-DERIVED]** | Rigorous analysis of government data by a named research organization (KFF, MedPAC analyses of CMS data). |
| **[PEER-REVIEWED]** | Published academic study. |
| **[INDUSTRY]** | Trade press, association, or vendor reporting. Directionally useful; not authoritative. |
| **[ANECDOTAL]** | Quoted operator experience, single-informant claims, or interview testimony. Real, but not generalizable. |
| **[UNVERIFIED — DO NOT CITE]** | Figures circulating in the market that I could not trace to any source with a stated methodology. |

A recurring caution for this whole file: **MA home health rules are contract-level and plan-level artifacts, not national policy.** Almost nothing below is uniform across plans, states, or even across two contracts with the same parent insurer. Where I say "typically," treat it as a modal pattern with wide variance, not a rule.

---

## 1. The Structural Picture

### 1.1 MA penetration as of 2026

**[PRIMARY-DERIVED]** As of February 1, 2026, **35.2 million people are enrolled in Medicare Advantage — 55% of the 64.2 million Medicare beneficiaries with both Part A and Part B.** That is up 1.1 million (3%) from 2025. Special Needs Plans account for 8.2 million enrollees (23% of MA), and SNP growth drove roughly 83% of all MA enrollment growth over the year. — [KFF, "Medicare Advantage in 2026: Enrollment Update and Key Trends," published June 5, 2026, updated July 1, 2026](https://www.kff.org/medicare/medicare-advantage-in-2026-enrollment-update-and-key-trends/)

**[PRIMARY-DERIVED]** Market concentration, 2026 (share of national MA enrollment):

| Insurer | 2026 share | Change |
|---|---|---|
| UnitedHealth Group | 26% (9.3M) | down from 29%; lost 647,000 enrollees |
| Humana | 20% (7.0M) | up from 17%; gained 1.3M enrollees |
| CVS Health (Aetna) | 12% | — |
| Kaiser Permanente | 6% | — |
| Elevance Health | 5% | — |
| **UHG + Humana combined** | **46%** | — |

— [KFF, June 5 / July 1, 2026](https://www.kff.org/medicare/medicare-advantage-in-2026-enrollment-update-and-key-trends/)

**Decision-relevant:** two companies control 46% of the national MA book. For a branch scheduling platform, the payer-rules surface is dominated by UHC and Humana, but the *long tail* matters more than the share suggests, because the tail is where the rules are most idiosyncratic and least automatable.

**[PRIMARY-DERIVED]** MA penetration varies enormously by geography — SNP enrollment alone ranges from 0% (Alaska, Vermont) to 46% (Mississippi). County-level MA penetration variance is the single biggest driver of how much of this file applies to any given branch. — [KFF, June 5 / July 1, 2026](https://www.kff.org/medicare/medicare-advantage-in-2026-enrollment-update-and-key-trends/)

### 1.2 MA share of home health volume

This is the weakest-documented number in the whole domain, and I want to be blunt about it: **there is no authoritative published figure for "MA share of national home health volume."** What exists:

**[PRIMARY]** MedPAC found that in 2021, **2.2 million MA enrollees** had a home health encounter or OASIS record, versus **2.7 million FFS beneficiaries**. That is roughly a 45/55 MA/FFS split of home-health *users* in a year when MA was only 46% of Part A+B enrollment. — [MedPAC, "Initial estimates of home health care use among Medicare Advantage enrollees," public meeting presentation, October 11, 2024, slides 17–19](https://www.medpac.gov/wp-content/uploads/2023/10/HH-in-MA-MedPAC-Oct-2024-SEC.pdf)

Given that MA is now 55% of enrollment (2026 vs. 46% in 2021), the naive extrapolation is that MA is now the **majority** of home health patient volume nationally. I am flagging that as an inference, not a verified fact.

**[PRIMARY]** MedPAC's March 2026 report notes in passing that **HHAs serving only FFS Medicare beneficiaries accounted for just 8 percent of agencies nationwide** — i.e., 92% of Medicare-certified HHAs serve a mix of MA and FFS. — [MedPAC, March 2026 Report to the Congress, Chapter 8 "Home health care services," p. 259](https://www.medpac.gov/wp-content/uploads/2026/03/Mar26_Ch8_MedPAC_Report_To_Congress_SEC.pdf)

**[PRIMARY]** Fewer agencies serve MA than serve FFS: **4,600 HHAs treated at least 20 MA enrollees; 7,000 HHAs treated at least 20 FFS beneficiaries; 4,300 treated both** (2021 data). HHAs serving higher shares of MA patients were more likely to be large agencies and more likely to be urban. — [MedPAC, June 2025 Report to the Congress, Chapter 3, p. 166](https://www.medpac.gov/document/june-2025-report-to-the-congress-medicare-and-the-health-care-delivery-system/)

**Decision-relevant:** the MA-heavy agency is a *large, urban* agency. A capacity-and-scheduling platform selling into MA-heavy branches is selling into multi-payer, multi-portal complexity by definition.

### 1.3 The MA-vs-FFS differential: what is actually documented

Here is where the industry narrative and the evidence base diverge. The commonly repeated claim is that MA pays materially less per episode. That claim is **directionally supported but has never been quantified in a public primary source with a stated methodology.** What is documented is the *utilization* gap and MedPAC's characterization of the *rate* gap.

#### Utilization gap — VERIFIED

**[PRIMARY]** Unadjusted, 2021 data:

| Metric | MA | FFS | Gap |
|---|---|---|---|
| Home health use rate (all counties) | 9.1% | 10.1% | −1.0 pt |
| Visits per beneficiary | **20.0** | **25.8** | **−22%** |
| Minutes per visit | **35.0** | **47.0** | **−26%** |
| Months with at least one visit | 3.0 | 3.8 | −21% |

FFS figures were geographically standardized to where MA enrollees live; not adjusted for other beneficiary differences. All differences significant at the 1% level. — [MedPAC, October 11, 2024 presentation, slides 21–23](https://www.medpac.gov/wp-content/uploads/2023/10/HH-in-MA-MedPAC-Oct-2024-SEC.pdf)

**[PRIMARY]** After multivariable adjustment for beneficiary characteristics (MedPAC's published June 2025 version):

- Overall home health use rate: **MA 8.3% vs. FFS 8.6%**
- Visits per user per year: **MA 18.2 vs. FFS 20.4 — a difference of 2.1 visits, or 11.0%**
- Among beneficiaries *with* a hospitalization: MA use rate was **3.2% higher** than FFS (41.7% vs. 40.4%) — consistent with MA substituting home health for SNF
- Among beneficiaries *without* a hospital stay: MA use rate was **13.7% lower** (3.7% vs. 4.2%)
- Controlling for the specific HHA treating the patient, MA users received **1.8 fewer visits** than FFS users

— [MedPAC, June 2025 Report to the Congress, Chapter 3, executive summary pp. xv–xvi and p. 166](https://www.medpac.gov/document/june-2025-report-to-the-congress-medicare-and-the-health-care-delivery-system/); trade summary: [Home Health Care News, June 2025](https://homehealthcarenews.com/2025/06/medpac-report-medicare-advantage-enrollees-receive-11-fewer-home-health-visits/)

**[PRIMARY]** MedPAC also found that **MA plans with home health cost sharing** had both lower use rates and fewer visits per user than plans without it, and that **PPO enrollment was associated with more visits per user than HMO enrollment** with no difference in the probability of any use. — [MedPAC, June 2025, Chapter 3](https://www.medpac.gov/document/june-2025-report-to-the-congress-medicare-and-the-health-care-delivery-system/)

MedPAC's own caveat, verbatim in the report: *"it is not possible to draw conclusions on the appropriateness of care based solely on observing differences in use (and most of the differences we observed are relatively modest)."* Do not overclaim from these numbers.

#### Rate gap — ACKNOWLEDGED BUT NOT QUANTIFIED

**[PRIMARY / meeting record]** At MedPAC's April 9–10, 2026 public meeting, staff analyst **Dr. Betty Fout** identified three mechanisms by which MA affects post-acute spending: steering patients to lower-cost settings, **negotiating lower payment rates relative to fee-for-service**, and reducing utilization. Commission discussion included the fact that **"home health agencies report receiving lower rates from MA than from Medicare fee-for-service"** and that **home health providers are being affected more than other PAC providers, with effects stronger in recent years.** — [MedPAC April 9–10, 2026 public meeting](https://www.medpac.gov/meeting/april-9-10-2026/); reported in [Home Health Care News, April 14, 2026](https://homehealthcarenews.com/2026/04/medpac-no-statistically-significant-impact-from-medicare-advantage-growth-on-home-health-margins/)

**[PRIMARY-DERIVED]** MedPAC's econometric result, same meeting: a **10% increase in MA penetration** was associated with a **2.7% decline in all-payer revenues and costs** for home health agencies, and a small decline in all-payer margin that was **not statistically significant**. Smaller HHAs showed larger declines than larger HHAs. MedPAC's headline framing was *"no statistically significant impact of MA growth on provider margins across hospitals and post-acute care."* The home health industry disputes this framing. — [Home Health Care News, April 14, 2026](https://homehealthcarenews.com/2026/04/medpac-no-statistically-significant-impact-from-medicare-advantage-growth-on-home-health-margins/)

**Decision-relevant and worth saying out loud:** the strongest public authority on Medicare payment has looked for an MA-driven margin effect in home health and *did not find a statistically significant one*, while simultaneously acknowledging that agencies report lower MA rates. Any pitch built on "MA pays 40% less" is resting on operator anecdote, not on a citable primary figure. The defensible framing is: **fewer authorized visits per patient, more administrative work per patient, and lower negotiated rates that vary by contract — with the volume effect better documented than the rate effect.**

**[UNVERIFIED — DO NOT CITE]** Widely circulated figures such as "MA pays 30–40% below Medicare FFS for home health" appear only in vendor blogs and conference decks with no stated methodology. I could not trace any of them to a primary source.

**[PEER-REVIEWED]** The closest thing to a peer-reviewed statement of the rate gap comes from Prusynski et al. (§2.3a), and it is qualitative rather than numeric: *"the agency's total HH payment is typically less from an Episodic MA insurer compared to TM."* — [AJMC, November 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC13137865/)

**The better argument, and it is fully documented (see §7.4).** The Senate PSI obtained internal UnitedHealthcare/naviHealth documents describing a home health utilization management model whose stated savings mechanism was **"reducing home health visits/episode."** In the same period, UHC's home health *denial rate declined* while its home health authorization *volume quadrupled*. **The revenue compression in MA home health runs primarily through authorized-visit reduction inside approved episodes, not through denials and not necessarily through headline rate cuts.** That mechanism is absent from every published denial-rate and margin statistic, which is why the quantitative literature keeps coming up empty while operators are certain they are being squeezed.

### 1.4 The FFS benchmark you are comparing against

**[PRIMARY]** Traditional Medicare home health economics, 2024 actuals:

| Metric | 2024 value |
|---|---|
| Average payment per full 30-day period | **$2,057** (up 1.6% from 2023) |
| Total in-person visits per full 30-day period | **8.4** (down 18.0% from 2019's 10.2) |
| Implied average Medicare payment per in-person visit | **$245** (up from $180 in 2019) |
| Aggregate FFS Medicare HH payments | **$16.0 billion** |
| FFS Medicare margin, freestanding HHAs | **21.2%** (25th pct 5.7%, 75th pct 31.0%) |
| Full 30-day periods | 8.3 million |
| 30-day periods per FFS home health user | 3.1 |

— [MedPAC, March 2026 Report to the Congress, Chapter 8, Tables 8-2, 8-7, 8-8 and accompanying text](https://www.medpac.gov/wp-content/uploads/2026/03/Mar26_Ch8_MedPAC_Report_To_Congress_SEC.pdf)

**[PRIMARY]** MedPAC projects a **19% FFS Medicare margin for freestanding HHAs in 2026** and recommends that **Congress reduce the 2026 base payment rate by 7% for 2027.** — [MedPAC, March 2026, Chapter 8, p. 254](https://www.medpac.gov/wp-content/uploads/2026/03/Mar26_Ch8_MedPAC_Report_To_Congress_SEC.pdf)

**[PRIMARY]** CY 2026 HH PPS final rule (CMS-1828-F), published **December 2, 2025** (delayed by the 43-day government shutdown): net **−1.3% aggregate payment change (−$220 million)** versus CY 2025, composed of a +2.4% payment update, a **−1.023% permanent behavior adjustment**, a **−3.0% temporary adjustment** applied to the CY 2026 base rate only, and −0.1% from the outlier FDL ratio. The rule also recalibrates PDGM case-mix weights, updates LUPA thresholds, and broadens the face-to-face encounter policy at 42 CFR 424.22(a)(1)(v). — [CMS fact sheet, CY 2026 HH PPS final rule (CMS-1828-F)](https://www.cms.gov/newsroom/fact-sheets/calendar-year-cy-2026-home-health-prospective-payment-system-final-rule-cms-1828-f); [Federal Register, 90 FR, December 2, 2025, doc. 2025-21767](https://www.federalregister.gov/documents/2025/12/02/2025-21767/medicare-and-medicaid-programs-calendar-year-2026-home-health-prospective-payment-system-hh-pps-rate)

For historical anchoring, the actual CY 2024 national standardized 30-day base rate was **$2,038.13** and CY 2023 was **$2,010.69**. — [CY 2026 HH PPS final rule text, sections II.C.1 discussion](https://www.federalregister.gov/documents/2025/12/02/2025-21767/medicare-and-medicaid-programs-calendar-year-2026-home-health-prospective-payment-system-hh-pps-rate)

---

## 2. Payment Models MA Plans Use for Home Health

### 2.1 The governing fact: MA is not required to use PDGM

**[PRIMARY]** This is the single most important structural point in the entire file, and it comes straight from MedPAC:

> "under MA, HHA claim submission, adjudication, and payment occur between the HHA and Medicare Advantage organization (MAO) and do not involve CMS... The process may differ across plans and by whether the HHA is within the MAO's network. **Payment may or may not be based on the home health PPS used by FFS and instead can be made per visit or according to another agreed-upon payment mechanism.**"

— [MedPAC, June 2025 Report to the Congress, Chapter 3, p. 145 and Figure 3-2, p. 146](https://www.medpac.gov/document/june-2025-report-to-the-congress-medicare-and-the-health-care-delivery-system/)

MA plans **must cover** the Medicare home health benefit. They are **not** required to pay for it the way traditional Medicare does. Everything about episode structure, unit of service, and rate is contractual.

MedPAC also notes that some MA plans **do** use OASIS items to case-mix adjust payment using the home health PPS — so a subset of MA contracts are genuine PDGM mirrors. — [MedPAC, June 2025, Chapter 3, p. 145](https://www.medpac.gov/document/june-2025-report-to-the-congress-medicare-and-the-health-care-delivery-system/)

### 2.2 The four models in the wild

The best systematic evidence on which model appears where is **Thomas KS, Daus M, Jones C, et al., "Prior authorization and utilization management for post-acute home health in Medicare Advantage: the motivations, players, processes, unique challenges, and impacts on patient care," *Health Affairs Scholar* 3(3):qxaf020, published February 4, 2025 (March 2025 collection).** Methodology: **44 semi-structured interviews** conducted **March 2023 – June 2024** with 18 individuals from 14 MA plans (collectively >20 million MA members, >62.4% of the 2023 MA market), 5 leaders from 5 PAC management companies, and 21 individuals from 19 HHAs, across 6 US markets with moderate-to-high MA penetration. Brown University; not classified as human-subjects research. — [Health Affairs Scholar via Oxford Academic](https://academic.oup.com/healthaffairsscholar/article/3/3/qxaf020/7997917) · [full text, PMC11886789](https://pmc.ncbi.nlm.nih.gov/articles/PMC11886789/)

**[PEER-REVIEWED]** The paper's Theme 3b finding, verbatim: *"Home health is episode-based; but there is no standard for what is considered an episode or unit of service across MA plans."* And: *"Unlike traditional Medicare where episodes (and payment) are based on 30 and 60 days, MA plans have discretion about whether they pay for services on an episodic basis and what they define as an episode."*

| Model | How it works | Where it shows up | Economics for the agency |
|---|---|---|---|
| **Per-visit fee schedule** | Flat or discipline-tiered fee per completed visit. Some plans pay one rate regardless of discipline. | Most common in HMO/delegated and PAC-management-company arrangements. **[ANECDOTAL]** One HHA: *"there are some that pay us per visit... and they pay a flat rate no matter what the discipline is... it's the same whether it's a physical therapist, a physical therapy assistant, an RN or an LPN."* | Revenue is a **direct linear function of authorized visit count**. Utilization management *is* the rate. Every denied reauth is lost revenue, not just lost margin. |
| **Episodic / case rate mirroring PDGM** | 30-day or 60-day period payment, sometimes case-mix adjusted using OASIS, sometimes a flat case rate with no case-mix adjustment. | **[ANECDOTAL]** Reported more often in PPO products: *"When you have the particular payers that are maybe PPO, they pay you by episode. Once you get approved for all the services, you pretty much have your approval up front."* And: *"The HMOs or the episodic payers really do not put a limit on how many visits you can order."* | Risk sits with the agency on visit count but revenue is predictable. A **flat case rate with no comorbidity/acuity adjustment** is the worst of both worlds — you carry PDGM-style utilization risk without PDGM's case-mix protection. |
| **PMPM / capitation, usually delegated** | Plan pays a delegated medical group or PAC management company a capitated PMPM; that entity subcontracts HHAs, typically on per-visit rates, and performs UM. | **[PEER-REVIEWED]** MA plan interviewee: *"We contract with large medical groups and as part of that contract, we pay them a capitated fee per member per month… we delegate a utilization management function to them... for them to make authorization decision, either approval or denial for inpatient stay, skilled nursing facility stay, [DME], and also home health."* | The agency never sees the capitation. It sees the downstream per-visit rate net of the intermediary's margin. |
| **Value-based / shared savings** | Episodic payment with quality or readmission gates; explicitly described by one plan as pushing visit-count decisions back to clinicians. | **[PEER-REVIEWED]** MA plan: *"Now that we've moved to episodic... as long as they're homebound and approved and they submit the OASIS... whether or not they do six visits or 15 visits, they're on the hook to get better care for my members. And so, I've pushed the decision of how many visits they should do to the clinicians."* | The only model in which utilization decisions return to the agency. Rare. |

### 2.3 What a per-visit MA contract does to the economics versus a PDGM 30-day period

Under **PDGM**, the agency is paid roughly **$2,057 per full 30-day period** and delivered **8.4 in-person visits** on average in 2024 — an implied **~$245 per visit** ([MedPAC March 2026, Ch. 8](https://www.medpac.gov/wp-content/uploads/2026/03/Mar26_Ch8_MedPAC_Report_To_Congress_SEC.pdf)). Critically, **that payment is fixed regardless of whether the agency delivers 5 visits or 12** (above the LUPA threshold and below the outlier threshold). The agency captures the full margin of efficient care delivery.

Under a **per-visit MA contract**, four things invert:

1. **Efficiency stops paying.** Delivering fewer visits reduces revenue one-for-one. The PDGM incentive to front-load and discharge efficiently is replaced by a fee-for-service incentive — but with the plan, not the agency, holding the authorization lever.
2. **The payer sets your volume.** **[PEER-REVIEWED]** *"Our plan of care may call for 15 visits in a 60-day episode. They may only give us authorization for six visits and then we've got to go back and get reauthorization."* Revenue per patient becomes an output of the UM process, not of the clinical assessment.
3. **The discipline mix stops mattering to revenue but still drives cost.** A flat per-visit rate across RN/LPN/PT/PTA means the agency eats the full cost differential of sending an RN instead of an LPN. This is a direct, quantifiable scheduling-optimization opportunity.
4. **Unauthorized work becomes write-off, not margin.** Under PDGM, a visit delivered before paperwork clears still counts toward the period payment. Under per-visit MA, it is uncompensated unless retro-authorized. **[ANECDOTAL]** *"We were writing off way too much money each year because of the authorization process."*

**Decision-relevant for a capacity-and-scheduling platform:** the unit of scheduling economics differs by contract type. In a PDGM branch the scarce resource is *clinician time against a fixed period payment*; in a per-visit MA branch the scarce resource is *authorized visits*, and the scheduling system's job shifts to (a) never scheduling an unauthorized visit, (b) never leaving an authorized visit unused before it expires, and (c) matching the cheapest qualified discipline to a flat-rate visit. **These are opposite optimizations, and a branch running mixed payers is running both at once.** That mixed state is the normal state — 92% of Medicare-certified HHAs serve both MA and FFS ([MedPAC March 2026, p. 259](https://www.medpac.gov/wp-content/uploads/2026/03/Mar26_Ch8_MedPAC_Report_To_Congress_SEC.pdf)).

### 2.3a The best quantitative evidence on episodic vs. per-visit MA — and it is directly on point

**[PEER-REVIEWED]** Prusynski RA, D'Alonzo A, Johnson MP, Smith JM, Mroz TM. **"Medicare Advantage reimbursement structures impact home health delivery and outcomes."** *American Journal of Managed Care* 2025 Nov;31(11):677–685. DOI [10.37765/ajmc.2025.89819](https://doi.org/10.37765/ajmc.2025.89819) · PMID 41289257 · [full text, PMC13137865](https://pmc.ncbi.nlm.nih.gov/articles/PMC13137865/)

**Why this is the single most useful paper in this file for CCSI:** the data come from *"a large national non-profit company that provided de-identified data on HH stays from **102 locations in 19 states**"* — i.e., a multi-branch operator of exactly the shape the platform serves. Payment model was taken from the partner's own billing system, with the company indicating **whether its local contract with each MA insurer was structured episodic or per-visit.** 285,297 home health stays, January 2019 – December 2022, patients 65+, inverse probability of treatment weighting on demographics, OASIS clinical factors, social risk, and environment, with year and office-location fixed effects.

**The authors' own definitions match §2.2 exactly:**

> "Similar to TM, **Episodic MA plans** pay agencies a lump sum to cover all costs anticipated during an authorized 60-day episode. While the agency's total HH payment is typically less from an Episodic MA insurer compared to TM, episodic payments allow the agency to determine the number of visits, distribution of visits across the stay, and which disciplines… are necessary for each patient's care plan. In contrast, **Per-Visit MA plans dictate the total number of visits — and the number of visits per discipline — that are covered during a specified duration of days, and the agency must seek re-authorization for additional visits or to add covered days.**"

Note the parenthetical: *"the agency's total HH payment is typically less from an Episodic MA insurer compared to TM."* That is a peer-reviewed statement of the rate gap, though unquantified.

**The closest thing that exists to a payment-model mix figure:**

| Payer group | Stays | Share of total | Share of MA stays |
|---|---|---|---|
| Traditional Medicare | 178,195 | 62.5% | — |
| **Episodic MA** | 43,299 | 15.2% | **40.4%** |
| **Per-Visit MA** | 63,803 | 22.4% | **59.6%** |

**In this operator's book, roughly 60% of MA home health stays were per-visit.** That is one company's contract portfolio across 19 states, not a national estimate — the authors say plainly: *"because each individual HH company has separate negotiations with MA insurers, **it is unknown how frequently MA contracts include episodic versus per-visit payments**."* But it is the only such figure I could find anywhere, and it is the right order of magnitude to plan around.

**Care-delivery findings (adjusted, vs. Traditional Medicare):**

| Measure | Episodic MA vs. TM | Per-Visit MA vs. TM |
|---|---|---|
| Length of stay | **−0.98 days (−2.1%)** | **−1.99 days (−4.3%)** |
| Nursing and all therapy visits | fewer | fewer |
| Social work visits | **+3.8%** | **−3.3%** |
| Home health aide visits | **−9.6%** | **−8.1%** |

**Head-to-head, per-visit MA vs. episodic MA:** per-visit had **1.02 days shorter LOS**, **3.0% more physical therapy visits**, and **6.8% fewer social work visits**; no significant difference in nursing or other therapy visits, and similar aide visits.

**Outcome findings — this is the part with teeth:**

| Outcome | Episodic MA vs. TM | Per-Visit MA vs. TM | **Per-Visit vs. Episodic MA** |
|---|---|---|---|
| Inpatient transfer during HH stay | **5% lower** odds (0.90–0.99) | **6% higher** odds (1.02–1.10) | **12% higher** odds (1.06–1.18) |
| Mobility function improvement | 8% lower odds (0.87–0.98) | no difference | n.s. |
| Self-care function improvement | 6% lower odds (0.88–0.99) | no difference | n.s. |
| Community discharge | no difference | 6% higher odds (1.02–1.10) | n.s. |

Authors' conclusion, verbatim: *"Episodic MA plans, which allow HH agencies flexibility in determining visit delivery, may have fewer adverse inpatient transfer outcomes compared with MA plans that dictate the amount and type of care provided."*

**Decision-relevant, and this is a genuinely strong commercial argument.** The only statistically significant *outcome* difference between the two MA payment models is a **12% higher likelihood of mid-stay inpatient transfer under per-visit contracts** — the exact outcome MA plans are financially motivated to avoid. The mechanism the paper implies is that **removing the agency's discretion over visit mix and timing degrades outcomes.** A capacity-and-scheduling platform that improves visit timing and discipline matching inside per-visit constraints is intervening precisely where the harm is measured.

Author caveats worth carrying: patient mix differed materially across groups (TM patients were the most clinically complex; MA patients had higher social risk), results were sensitive to adjustment specification, and 2022-only sensitivity analyses did not reproduce all effects.

**[PEER-REVIEWED — conference abstract]** A companion abstract, "Differences in home health services and outcomes for Medicare Advantage plans with episodic vs. per-visit payments," *Innovation in Aging* Dec 2024, DOI [10.1093/geroni/igae098.3835](https://doi.org/10.1093/geroni/igae098.3835).

### 2.4 Mid-episode plan switching

**[PEER-REVIEWED / ANECDOTAL]** A specific operational failure mode worth designing for: patients switching between MA plans, or between FFS and MA, mid-episode during open enrollment. *"a patient was admitted under traditional Medicare, well open enrollment started and this patient is still receiving care from us… It's like going through an admission process all over again... They may not be able to have three days a week... now because... the insurance inability to cover all three visits, it becomes only two days."* — [Thomas et al., Health Affairs Scholar, Feb 4, 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC11886789/)

Note this interacts with the **90-day continuity-of-care protection** in CMS-4201-F (see §6.2), which the interviewees do not appear to have been getting the benefit of.

### 2.5 The "convenor" / PAC management company layer

**[PEER-REVIEWED]** These are third parties contracted by MA plans "to interface with care providers to manage services and payments, and sometimes referred to as 'convenors.'" They sit between plan and agency, typically taking capitation from the plan and paying agencies per visit while performing UM. — [Thomas et al., Feb 4, 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC11886789/)

**[ANECDOTAL]** The most vivid operator description in the literature, from an HHA leader in the same study:

> "the MAs typically go capitated with [name of PAC management company] then they don't actually do anything other than siphon money off the top. They go out and they contract with all sorts of agencies in the area at these ridiculously low per-visit rates. And then they do utilization management on top of it and limit the number of visits... It increases my overhead admin to deal with these yahoos by 25%. And then they're paying these ridiculously hideous rates that I lose money even if it was the same administrative overhead."

Treat the "25%" as one operator's estimate, not a benchmark.

---

## 3. Authorization Mechanics: the Cross-Payer Pattern

Before the payer-specific sections, here is the pattern that recurs across plans — this is the part a scheduling platform actually has to model.

**[PRIMARY-DERIVED]** **In 2024, 90% of MA enrollees were in a plan that required prior authorization for home health care.** (For context, 99% of MA enrollees were in a plan with *some* prior authorization requirement.) — [Thomas et al. abstract, citing KFF, "Medicare Advantage in 2024: Premiums, Out-of-Pocket Limits, Supplemental Benefits, and Prior Authorization"](https://www.kff.org/medicare/issue-brief/medicare-advantage-in-2024-premiums-out-of-pocket-limits-supplemental-benefits-and-prior-authorization/)

**⚠️ That 90% figure is 2024 and is now materially stale.** UnitedHealthcare — 26% of the national MA market — **removed home health prior authorization entirely across 36 states and D.C. effective April 1, 2025** (§4.1, verified against UHC's own notice). Humana has separately been reducing prior authorization (§5). **Nobody has recalculated the home health PA prevalence figure since these changes.** Do not present "90% of MA enrollees need home health prior authorization" as a current fact — it was true in 2024 and is very likely lower now. The direction of travel matters more than the number: **MA home health prior authorization is being dismantled at the top of the market while risk migrates to post-payment audit.**

**[PRIMARY]** MedPAC independently confirms the near-universality: *"Almost all plans required some sort of prior authorization for home health care use, so there was too little variation to assess its association with home health care use."* MedPAC also found that plan-reported fields describing the *type* of PA were poorly populated — some plans indicated PA was required only after 60 days, or only for certain therapy or social work services, but most plans did not describe the type at all. — [MedPAC, June 2025, Chapter 3, p. 154](https://www.medpac.gov/document/june-2025-report-to-the-congress-medicare-and-the-health-care-delivery-system/)

**Decision-relevant:** even CMS's own plan-reported data cannot tell you what a given MA plan's home health PA rule is. The rules are only discoverable at the contract and portal level. That is a durable structural problem — and a durable product opportunity.

### 3.1 The typical flow

Synthesized from [Thomas et al., Feb 4, 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC11886789/):

1. **Referral** from hospital discharge planner or physician.
2. **Initial visit** — practice varies sharply. Some plans auto-approve it. **[PEER-REVIEWED]** One plan: *"that initial home care visit is always approved."* Other plans require authorization before any visit.
3. **OASIS start-of-care assessment** completed. Federal COP at **42 CFR 484.55** requires the initial assessment within 48 hours of referral or the patient's return home — which is *faster than many plans' authorization turnaround*, forcing agencies to work at risk.
4. **Authorization request submitted**, almost always via a payer- or vendor-specific web portal, usually with the OASIS and the plan of care uploaded.
5. **Adjudication** — either algorithmic (near-instant) or human clinical review (1–3 days historically).
6. **A visit allotment is issued** — a number of visits or "units," often well below the plan of care.
7. **Reauthorization gate** at the allotment boundary, typically requiring re-submission of documentation and sometimes an InterQual-style checklist.

**[PEER-REVIEWED]** Plan-side description of the algorithmic path: *"Our process used to be a home care agency would go into our provider portal. They'd fill out a 45-minute survey... they would fax in all of their clinical documentation, and then a nurse would look at the clinical survey... take one to three days... Now we're just collecting the OASIS, we run algorithms on that and within two minutes they get approval right in the system."*

**[PEER-REVIEWED]** Another plan's unit-based model with self-service initial approval and a gated reauth: *"They just go into our portal and they plug the 30 units in themselves, and it spits out an approval number... And then they have to go back into the portal and request additional time after that, so we usually hear from them around unit 25 being used... And at that time, they fill out InterQual, which is like an algorithm... 'Is this member in fact homebound? Are they under the direction of a physician? Is the goal short term?'"*

### 3.2 Visit allotments and reauth intervals — what the evidence actually shows

**[ANECDOTAL — but consistent across informants]** Reported patterns from HHA leaders in Thomas et al.:

- **"Here's two visits. Send us your documentation and we'll give you two more"** — the most aggressive pattern described.
- **6 visits authorized against a 15-visit plan of care**, with reauth required to continue.
- **Every-two-week reauthorization cycles**: *"Every two weeks, we're having to get authorization for them to review."*
- **Week-by-week authorization** for some plans: *"sometimes it's week by week getting those visits authorized so we can schedule them out."*
- **30-day case rates** with a hard reauth gate at day 30, sometimes leaving the agency unable to even perform a discharge visit.
- **30-unit blocks** with reauth triggered around unit 25.

I want to be precise about the epistemic status here: **there is no published, systematic dataset of MA home health initial visit allowances or reauthorization intervals.** Not from CMS, not from OIG, not from KFF, not from MedPAC, not from any trade association I could find. Everything in the list above is interview testimony from a qualitative study with 19 HHAs. It is the best evidence that exists, and it is not a benchmark.

**Decision-relevant:** the reauth interval — 2 visits, 30 units, 2 weeks, 30 days — is the single most important payer variable a scheduling system needs, because it determines the cadence at which the schedule can be locked. **It is not published anywhere. It has to be captured per contract at implementation.** That is a product requirement, and a data asset if captured well.

### 3.3 Portal proliferation

**[PEER-REVIEWED]** *"Depending on the insurance, you have to go into that payer's portal and request authorization for visits... Most of the time, it requires uploading our OASIS documentation and our plan of care and it really, really just depends on the payer which portal you're going into, so I think we have four or five different portals."* The study reports HHAs using **as many as 10+ distinct portals**. — [Thomas et al., Feb 4, 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC11886789/)

### 3.4 Working at risk

**[PEER-REVIEWED]** Agencies described three postures, all costly:

- **Serve then chase:** *"We never say, 'No, we're not going to see you until we get your authorization,' because it's critical timing for a patient, those first 14 days, 20 days, but we run a risk of a lot of write-offs if that comes back denied."*
- **Hold service:** *"we're holding up visits now, and we're telling the patients, we're telling the referral sources, 'It's not us.'"* — from an agency that reported *"We may not get authorization for 14 days from the Medicare Advantage plan."*
- **72-hour notice then discharge:** *"we don't stop seeing a patient just because we don't have an auth. We still give them 72 hours' notice... but in 72 hours, we're going to have to move forward to a different solution for you."*

**[PEER-REVIEWED]** The paper's own framing: HHAs *"often provide care without prior authorization, risking further financial instability if services aren't approved or reimbursed."*

**Decision-relevant:** the "authorized vs. delivered vs. billable" three-way reconciliation is where MA revenue leaks. A scheduling platform that can hard-gate or flag unauthorized visits at the point of scheduling is addressing a documented, quantified-by-operators loss.

---

## 4. UnitedHealthcare

### 4.1 The headline finding — and it inverts the industry's mental model

**[PRIMARY — I fetched and read the notice]** **UnitedHealthcare eliminated prior authorization *and* concurrent review for Medicare Advantage home health services effective April 1, 2025.**

Verbatim from the notice, dated **March 1, 2025**, titled *"Home health prior authorization review process no longer required"*:

> "Starting April 1, 2025, we'll no longer require prior authorization or concurrent review processes for home health services managed by Home & Community (formerly naviHealth)."

> "Although prior authorizations are no longer required for dates of service starting April 1, 2025, you are expected to provide home health services according to Centers for Medicare & Medicaid Services coverage guidelines."

— [UHCprovider.com, March 1, 2025, doc PCA-1-25-00265-Clinical-NN_02182025](https://www.uhcprovider.com/en/resource-library/news/2025/home-health-prior-auth-changing.html)

**Scope, verified by direct extraction of the notice's own list — 36 states plus D.C., not all 50:**
Alabama, Alaska, Arkansas, California, Colorado, Connecticut, Florida\*, Georgia, Idaho, Illinois, Indiana, Iowa, Kansas, Kentucky, Louisiana, Maine, Maryland, Massachusetts, Nebraska, Nevada, New Mexico, North Carolina, North Dakota, Ohio, Oklahoma, Oregon, Pennsylvania, Rhode Island, South Carolina, Tennessee\*, Texas, Utah, Virginia, Washington, Wisconsin, Wyoming, Washington D.C.

\* *"In Florida and Tennessee, continue to follow existing requirements for D-SNP plans not managed by Home & Community."*

**Notably absent from that list:** Arizona, Delaware, Hawaii, Michigan, Minnesota, Mississippi, Missouri, Montana, New Hampshire, New Jersey, New York, South Dakota, Vermont, West Virginia. **A widely repeated "41 states + D.C." figure is wrong** — the notice enumerates 36 states + D.C. and states no total.

**Two things this does NOT mean:**

1. **Risk did not disappear — it moved from pre-service review to post-claim medical review.** UHC's own instruction is to follow CMS coverage guidelines; enforcement shifts to post-payment audit.
2. It applies to **home health services managed by Home & Community (formerly naviHealth)**. Delegated groups, excluded plans, and the carve-out populations below are unaffected.

Context UHC gave: the change represented *"nearly 10% of our total prior authorization volume,"* following a 2023 removal of codes accounting for ~20% of volume. — [same notice](https://www.uhcprovider.com/en/resource-library/news/2025/home-health-prior-auth-changing.html)

**This reconciles cleanly with the Senate PSI findings in §7.4.** UHC built home health prior authorization from **19,283 requests in 2019 to 356,606 in 2022** — an 18-fold expansion — then, under congressional and litigation pressure, dismantled it for most of its book in April 2025. **Both facts are true, and most secondary commentary is stuck on the 2022 picture.** Any research or vendor material describing UHC MA home health authorization workflow that predates March 2025 should be treated as historical.

### 4.2 What the current PA list actually says

**[PRIMARY — I downloaded and text-extracted the PDF]** [UnitedHealthcare Medicare Advantage / Dual Complete / Peoples Health prior authorization requirements, **effective August 1, 2026**](https://www.uhcprovider.com/content/dam/provider/docs/public/prior-auth/pa-requirements/medicare/Med-Adv-Dual-Eff-8-1-26.pdf) (doc PCA-4-26-00416-Clinical-QRG_03022026).

Home health appears in exactly **three rows**, all narrow. There is **no general home health prior authorization row**:

| Population | Status | Codes |
|---|---|---|
| **Erickson Advantage only** | PA required | Contact the MSR / prior-auth number on the back of the member ID card |
| **Tennessee D-SNP only** | PA required | S9122, S9123, T1000 |
| **Peoples Health only** (Louisiana) | PA required | Nursing G0299, G0300, S9123, S9124 · PT G0151, G0157, S9131 · OT S9122, S9123, S9124, T1000 · ST G0153, S9128 · HHA G0156, S9122 · MSW G0155, S9127 |

**[INDUSTRY — one-source diff, worth watching]** A researcher diff of the [June 1, 2026 list](https://www.uhcprovider.com/content/dam/provider/docs/public/prior-auth/pa-requirements/medicare/Med-Adv-Dual-Eff-6-1-26.pdf) against the August 1 list found **two** home health rows in June and **three** in August — i.e., the **Peoples Health row appears to be new as of August 1, 2026**. If UHC is re-expanding home health PA plan by plan, this is the leading indicator. **Diff the PA list monthly.** I have verified the August list directly; I have not independently verified the June list.

### 4.3 What IS still required nationally: advance notification

**[PRIMARY]** From the [2026 UnitedHealthcare Care Provider Administrative Guide](https://www.uhcprovider.com/content/dam/provider/docs/public/admin-guides/2026-UHC-Administrative-Guide.pdf):

> "Following a facility discharge, advance notification for home health services and DME is required within 2 business days after the start of service."

This is a **notification, not a clinical coverage review** — UHC's guide distinguishes them explicitly (*"Services that require prior authorization require a clinical coverage review based on medical necessity"*). But notification failure has claim consequences. In the **River Valley** entity supplement (parts of AR, GA, IA, IL, TN, VA, WI), the guide states preauthorization *is* required for home health and: *"If you do not notify us, we will deny your claim. You may not bill the member for the service."*

**Decision-relevant:** for a scheduling platform, the UHC MA trigger is **not** an authorization request — it is a **2-business-day post-start-of-care notification clock** that begins at the first visit. That is a different workflow object entirely, and it is easy to miss precisely because everyone is looking for a PA gate that no longer exists.

### 4.4 The gate that actually terminates care now: the NOMNC

**[PRIMARY]** From the 2026 Administrative Guide, Chapter 11:

> "You must deliver required notice to members at least **2 calendar days before termination** of skilled nursing care, **home health care** or comprehensive rehabilitation facility services. If the member's services are expected to be fewer than 2 calendar days in duration, the notice should be delivered at the time of admission or commencement of services in a non-institutional setting. **In a non-institutional setting, if the span of time between services exceeds 2 calendar days, the notice should be given no later than the next to last time services are furnished.**"

Signature and date required; the current CMS-approved **Notice of Medicare Non-Coverage (NOMNC)** must be used with no text modification. Appeals are **fast-track appeals reviewed by the QIO**, and records must be provided to UHC or the QIO **no later than the close of the calendar day you are notified — including weekends and holidays.**

**That last clause is the sharpest single operational risk in UHC's MA home health documentation.** A QIO fast-track appeal filed on a Saturday creates a same-day records obligation. A scheduling and capacity system that knows which visit is the "next to last" visit is directly serving this requirement.

### 4.5 Optum / naviHealth / Home & Community Care — home health is NOT in scope

**[PRIMARY]** From the same August 1, 2026 PA list, the **"Inpatient admissions – Post-acute services"** row, verbatim:

> Prior authorization and notification of admission date required for these facilities providing post-acute inpatient services: • Acute care hospitals • Acute inpatient rehabilitation • Critical access hospitals • Long-term acute care hospitals • Skilled nursing facilities
>
> **"Home & Community Care (formerly naviHealth) manages prior authorization for in-scope membership. Phone: 855-851-1127"**

**Home health is absent from that facility list.** The vendor's current scope is **facility-based post-acute only**. Home health agencies should **not** call 855-851-1127.

Carve-outs stated in the same document:
- *"Peoples Health does not use Home & Community Care (formerly naviHealth). Enter authorization request using the UnitedHealthcare Provider Portal."*
- *"AIP DSNP plans should not route to naviHealth and are serviced by the Optum PACM team"*
- UHC Nursing Home Plan (I-SNP) is excluded from the SNF PA requirement entirely

**Branding as of 2026 — four names in simultaneous use, which is itself a research hazard:**

| Name | Where it appears |
|---|---|
| "Home & Community Care (formerly naviHealth)" | August 2026 MA PA list |
| "Home & Community Care Transitions" | 2026 Administrative Guide — **"naviHealth" appears zero times in the Admin Guide** |
| "Optum Home & Community Care" / "Post-Acute Care Solutions" | [business.optum.com](https://business.optum.com/en/access/home-and-community/post-acute-care.html) |
| "Optum PACM" | separate internal team serving AIP D-SNP |
| **"naviHealth"** | **still used by HHS OIG in June 2026** ([OEI-09-24-00330](https://oig.hhs.gov/documents/audit/11693/OEI-09-24-00330.pdf)) and by the federal court docket |

Corporate history: Optum acquired naviHealth from Clayton Dubilier & Rice in **May 2020** (~$2.5B); [STAT News, October 23, 2023](https://www.statnews.com/2023/10/23/unitedhealth-optum-navihealth-rebranding-algorithm/) reported the rebrand decision amid congressional scrutiny; legal rename effective January 1, 2024. **navihealth.com now 301-redirects** to Optum's post-acute page.

**Scope has contracted, not expanded.** Beyond the April 2025 home health removal: effective **January 1, 2026**, Medicare UM for **Michigan Dual Complete HIDE (H2247-005-000)**, **Texas Dual Complete HIDE (H3868-001-000)**, and **Indiana PathWays FIDE (H2385-003/004-000)** moved from Care Transitions to **UnitedHealthcare directly**. — [UHCprovider notice, December 1, 2025](https://www.uhcprovider.com/en/resource-library/news/2025/medicare-post-acute-care-management-change.html)

### 4.6 nH Predict and the Lokken litigation

**[INDUSTRY / investigative]** nH Predict is a **facility** length-of-stay and discharge-date prediction tool (SNF principally, plus IRF and LTACH), matching a patient against roughly 6 million prior records to set a target discharge date. — [STAT News, March 13, 2023](https://www.statnews.com/2023/03/13/medicare-advantage-plans-denial-artificial-intelligence/) (the STAT series was a **2024 Pulitzer Prize finalist**)

**There is no evidence nH Predict was ever applied to home health**, and with the April 2025 removal of home health from Home & Community's scope there is no current pathway for it to be. A product name "nH Coordinate" circulates in some secondary coverage and **could not be verified** — the documented family is nH Predict, nH Access, nH Pulse, nH Discharge, nH Intake.

**[PRIMARY — docket]** *Estate of Gene B. Lokken et al. v. UnitedHealth Group, Inc., UnitedHealthcare Inc., naviHealth Inc.*, **D. Minn. No. 0:23-cv-03514**, Judge **John R. Tunheim**, filed **November 14, 2023**. — [Georgetown Health Care Litigation Tracker](https://litigationtracker.law.georgetown.edu/litigation/estate-of-gene-b-lokken-the-et-al-v-unitedhealth-group-inc-et-al/)

**Motion-to-dismiss ruling, February 13, 2025 — partial:**

| Outcome | Claims |
|---|---|
| **Dismissed** (Medicare Act preemption) | Insurance bad faith, unjust enrichment, negligence per se, unfair and deceptive insurance practices, unfair competition — because adjudicating them required analyzing *"covered benefits and confirming the reasonableness of coverage decisions."* |
| **Survived** | **Breach of contract** and **breach of the implied covenant of good faith and fair dealing** — narrowed to whether UHC *"complied with its own written documents,"* not to the substantive coverage determination. |

The court **waived Medicare Act exhaustion** on allegations of irreparable injury and futility, given claimed deficiencies in the appeals process itself. On nH Predict specifically, the court noted UHC's coverage documents referenced *"clinical services staff"* and *"physicians"* with **no AI disclosure**. — [DLA Piper analysis, 2025](https://www.dlapiper.com/en/insights/publications/ai-outlook/2025/lawsuit-over-ai-usage-by-medicare-advantage-plans-allowed-to-proceed)

**Status as of August 2026 — active discovery, no class certified, no settlement, no trial date.** Docket milestones: motion to compel filed January 28, 2026 with an order March 9, 2026; motion to substitute parties granted July 6, 2026; order on motion to seal July 21, 2026; defendants' motion to amend August 10, 2026 with response August 17, 2026, briefing ongoing. **Deadline for class certification declarations: September 14, 2026.**

**[INDUSTRY]** Parallel case: *Barrows v. Humana* (also nH Predict) **survived dismissal in August 2025**. — [McKnight's](https://www.mcknights.com/news/humana-must-face-class-action-suit-over-use-of-ai-in-denying-post-acute-care/)

**Decision-relevant:** the litigation is about **facility** post-acute denials, not home health. Its relevance to a home health platform is indirect but real — it is a live legal constraint on algorithmic UM generally, and it is one of the pressures that produced UHC's 2025 home health PA removal.

### 4.7 Submission channels

**[PRIMARY]** From the 2026 Administrative Guide and the PA list:

| Channel | Detail |
|---|---|
| **Portal** | **UnitedHealthcare Provider Portal** — the "Link" branding is fully retired. Prior Authorization and Notification tool. **One Healthcare ID** required (UHCprovider.com/access); portal at secure.uhcprovider.com. 24/7 chat. |
| **Phone** | **877-842-3210** (Erickson Advantage: number on the back of the member ID card) |
| **Fax** | **855-352-1206 — severely restricted**, commercial only in MA, NV, NM, TX. The June 2026 MA PA list contains **zero occurrences of "fax."** UHC is deprecating fax by omission rather than by dated policy. |
| **EDI 278** | 005010X217, real-time and batch. [Companion Guide v15.0, dated March 30, 2025](https://www.uhcprovider.com/content/dam/provider/docs/public/resources/edi/EDI-278-Companion-Guide-005010X217.pdf) |
| **EDI 278N** | 005010X216 — **hospital admission notification only, flagged Non-HIPAA. Not a home health channel.** |
| **EDI 278I** | status inquiry |

**[PRIMARY]** The 278 **explicitly supports home health**. Under **POS 12 (HOME)**, the companion guide accepts UM03 service types **AG** (skilled nursing), **PT** (physical therapy), **AD** (occupational therapy), **AF** (speech therapy), **74** (private duty nursing), **45** (hospice), **72** (inhalation therapy), and **12/18** (DME purchase/rental) — the full discipline set.

Clearinghouse: *"Most transactions go through the Optum clearinghouse, OptumInsight, the managed gateway for UnitedHealthcare EDI transactions."* Payer IDs **87726** (UHC commercial + government), **06111 / 061118515** (Oxford). Availity is not named in UHC's EDI documentation. **Integration gotcha:** the companion guide notes that timeout responses return in **batch** mode, so a real-time 278 build must also stand up a batch connection.

**FHIR / CMS-0057-F readiness — the marketing outruns the reality.** On UHC's own [API catalog](https://www.uhcprovider.com/en/resource-library/Application-Programming-Interface.html), **"Real Prior Authorization" is listed as *Coming soon* with no launch date**, alongside Real Provider Access and Payer to Payer. Live today: Pre-Service Eligibility, Patient Benefit Check, Referral Actions, Claim Pre-Check/Actions/Inquiry, Document Search, Patient Access, Provider Demographics, TrackIt. UHC's PA landing page separately says *"API status check is now available for prior authorization"* — best reading is that **status inquiry is live, submission is not.**

**[INDUSTRY]** **Da Vinci CRD went live via Epic on August 17, 2026**, with UnitedHealthcare, Aetna, and Network Health named as participating plans. **CRD only — DTR and PAS are not reported live.** — [HIT Consultant, August 17, 2026](https://hitconsultant.net/2026/08/17/epic-deploys-real-time-crd-prior-authorization-apis-ochsner-froedtert/)

### 4.8 Visit allowances and reauthorization gates — the honest answer

**UHC publishes no initial visit allowance and no reauthorization schedule for MA home health.** Verified absences:

- The [MA medical policy index](https://www.uhcprovider.com/en/policies-protocols/medicare-advantage-policies/medicare-advantage-medical-policies.html) has **no standalone home health policy.** The nearest is "Skilled Nursing Facility, Rehabilitation, Long-Term Acute Care Hospital, and Private Duty Nursing" (last published 06.01.2026).
- Probes of likely coverage-summary paths return HTTP 200 but serve a 7,615-byte error template — **soft-404s. No such document exists.**
- The 2026 Administrative Guide contains **zero occurrences of "OASIS"** and zero of "consolidated billing." "Homebound" appears once, in a glossary aside.

With PA and concurrent review removed for the 36 states + D.C. above, **there is no visit-count gate and no reauth cycle to manage** for standard UHC MA / D-SNP membership in those states. **The commonly cited "UHC approves N visits then you reauthorize" describes the pre-April-2025 naviHealth-managed regime.** Treat any such figure as industry-anecdotal and now largely obsolete for UHC specifically. No UHC-published number exists, historical or current.

**Face-to-face encounter, OASIS, CMS-485 plan of care, and homebound attestation** remain **CMS conditions of payment** under 42 CFR 424.22 and the Medicare Benefit Policy Manual, and UHC's "follow CMS coverage guidelines" instruction incorporates them by reference. But **UHC does not restate them in any document I could find** — meaning they are enforceable at post-payment audit rather than at a pre-service gate. That is a materially different risk profile: quieter, later, and larger.

### 4.9 UHC's published home health reimbursement policy

**[PRIMARY]** [**Home Health Services Policy, Professional and Facility**, Policy Number **2026R9067A**](https://www.uhcprovider.com/content/dam/provider/docs/public/policies/medadv-reimbursement/MEDADV-Home-Health-Services-Policy-Professional-and-Facility.pdf), last published **07.01.2026** (new policy 10/1/2024; anniversary reviews 7/1/2025 and 7/1/2026).

**Despite the title, this policy does exactly one thing: it denies home health on days overlapping an inpatient stay.**

> "To align with the Centers for Medicare and Medicaid Services, if both home health services (POS 12 on a CMS-1500 claim form or type of bill 321-329, 341-345, or 347-349 on a UB-04 claim form) and inpatient care are billed for the same dates of service, UnitedHealthcare will reimburse the inpatient care only."

**Exception: admission and discharge dates remain eligible.** Grounded in CMS Pub. 100-04, Ch. 10, §30.B. Applies to participating and non-participating providers where the plan has out-of-network benefits.

Two disclaimers in the policy that matter more than the policy itself:
- *"UnitedHealthcare's Medicare Advantage reimbursement policies do not include notations regarding prior authorization requirements."* — **never infer PA status from a reimbursement policy.**
- *"Other factors affecting reimbursement may supplement, modify or, in some cases, supersede this policy… legislative mandates, **the facility or other provider contracts**, the enrollee's benefit coverage documents."*

**What UHC does NOT publish anywhere** (reviewed the full [MA reimbursement policy index](https://www.uhcprovider.com/en/policies-protocols/medicare-advantage-policies/medicare-advantage-reimbursement-policies.html)):

- **Per-visit vs. episodic/PDGM methodology** — not addressed. This is **contract-specific and not discoverable from public documents.** Anyone claiming to know "UHC's MA home health rate structure" as a general fact is describing their own contract.
- **Notice of Admission (NOA)** — zero occurrences in the Admin Guide. UHC MA does not appear to impose traditional Medicare's NOA requirement, but this is an argument from silence.
- **Home health consolidated billing** — zero occurrences. Not adopted in any published policy.
- **HIPPS code requirements** — not addressed.

**HHVBP:** the expanded Home Health Value-Based Purchasing model applies to **Medicare fee-for-service** agencies, not MA. No UHC MA home health value-based or episodic bundled program with published terms was found.

**[UNVERIFIED — DO NOT CITE]** No percent-of-Medicare rate benchmark for UHC MA home health could be verified from any source.

### 4.10 State, plan-type, and delegation variation

This is where the real complexity sits, and it is the part a platform has to model.

**Separate published PA lists.** UHC publishes **plan-family-specific** lists, not per-state ones:
- [MA / UHC West MA / Dual Complete / Peoples Health / Rocky Mountain, eff. 8/1/2026](https://www.uhcprovider.com/content/dam/provider/docs/public/prior-auth/pa-requirements/medicare/Med-Adv-Dual-Eff-8-1-26.pdf)
- [Preferred Care Network (Florida Medicare), eff. 8/1/2026](https://www.uhcprovider.com/content/dam/provider/docs/public/prior-auth/pa-requirements/pcn/UHC-Preferred-Care-Florida-Medicare-Eff-8-1-26.pdf)

**Plans excluded from the national PA program entirely:** Preferred Care Network and Preferred Care Partners (Florida), and UHC MedicareDirect PFFS. *"However, these benefit plans may have separate notification or prior authorization requirements."*

**Florida — a genuinely inverted regime.** From the PCN Florida PA list, verbatim: *"Home health care services — Prior authorization is only required for members residing in and receiving services in **Alabama and Georgia**. All requests for home health services should be directed to a health plan contracted vendor."* Codes Q5001, Q5002, Q5009 (Alabama only). The 2026 Admin Guide Florida supplements route home health PA to **MedCare Home Health, 305-883-2940** (24/7), expedited 72 hours / standard 14 calendar days. Service areas: Preferred Care Network — Broward and Miami-Dade; Preferred Care Partners — Broward, Miami-Dade, Palm Beach.

**Plan-type variation:**

| Plan type | Home health treatment |
|---|---|
| HMO / HMO-POS / PPO / Regional PPO | No home health PA. Referral may be required if the ID card says "Referral Required." |
| D-SNP | No PA except **Tennessee D-SNP** (S9122/S9123/T1000). In states requiring a Medicare denial before Medicaid authorization, submit via the portal. |
| C-SNP | Included in the national list; no home health PA. |
| **I-SNP** (UHC Nursing Home Plan, UHC Care Advantage) | Excluded from SNF PA and from outpatient therapy PA. SNF admissions must be authorized by an **Optum NP or PA**, not Home & Community. Also excluded from the DME $1,000 threshold. |
| **Group / employer retiree MA** | **Private duty nursing (T1000) PA applies only to an enumerated list of 100+ specific employer group plan codes**, and is expressly excluded for *"All individual Medicare Advantage plans."* Group retiree plans carry **more** UM here, not less. |
| **Erickson Advantage** (HMO-POS, C-SNP, I-SNP) | Its own PA chart, its own phone number, PA required for home health, SNF, and outpatient therapy tied to LTC residence. |
| PFFS (MedicareDirect) | Outside the PA program entirely. |

**Delegated and capitated arrangements — the single biggest practical variable.** The August 2026 PA list names delegated groups by state:

- **OptumCare** — AZ, CO, GA, ID, IN, KS, KY, MO, NV, NJ, NM, NY, OH, OR, SC, TN, UT, VA, WA, WI (20 states — by far the widest footprint)
- **WellMed** — FL, TX, NM
- **HealthTexas Medical Groups** — TX · **Banner Health Network** — AZ · **Intermountain Health** — NV · **PHP Prime** — CO · **Advantage Plus Network-CT** — CT · **MDX Hawaii** — HI · **Independent Clinics of Washington**, **Seattle Medical Group** — WA
- **California** — no group list published; instruction is *"Submit requests to the medical provider group shown on the front of the member's ID card,"* discoverable via portal → Eligibility → Plan Requirements → Prior Authorizations

Governing rule, verbatim: *"If you are a network health care professional who is contracted directly with a delegated medical group/Independent Practice Association (IPA), then you must follow the delegate's protocols. **Delegates may use their own systems and forms.**"*

The Admin Guide's Capitation and/or Delegation supplement confirms UHC may delegate **Utilization Management, Disease Management, Special Needs Plan, Complex Case Management, Credentialing, and Claims**. Whether home health risk sits with the delegate is set by the **Division of Financial Responsibility (DOFR) grid in the delegate's Agreement**: *"Refer to the Division of Financial Responsibility grid in your Agreement for a detailed listing of capitated services."* **The DOFR is contract-private. There is no public way to determine home health risk allocation for a given delegated group.**

**Decision-relevant:** in 20+ states, "what are UHC's rules?" is the wrong question. The operative question is "which delegate holds this member, and what does its DOFR say?" — and that is answerable only per-contract, per-branch, at implementation.

### 4.11 UHC's broader 2026 PA posture

**[PRIMARY]** On **May 5, 2026**, UnitedHealth Group announced elimination of prior authorization for a further **~30% of remaining services** by end of 2026 — named targets are select outpatient surgeries, echocardiograms, certain outpatient therapies, and chiropractic. **Home health and post-acute are not mentioned**, which is unsurprising since home health was already removed. Stated metrics: PA now applies to ~2% of medical services; 92% approval rate; average decision under 24 hours; ~1,500 rural hospitals and CAHs exempted by fall 2026. — [UnitedHealth Group newsroom, May 5, 2026](https://www.unitedhealthgroup.com/newsroom/2026/2026-05-05-uhc-cuts-prior-authorization-requirements-by-30-percent.html)

**[PRIMARY]** **UHC Gold Card** is live and national. Automatic at TIN level with no application; requires in-network status, **≥10 eligible PAs/year for 2 consecutive years**, and a **≥92.0% approval rate**. Gold-carded providers submit **advance notification, which eliminates clinical documentation review** — but note the trap: **notification is still required for claims to pay.** Separate state lists exist for GA, LA, MI. **Home health is not among the eligible code sets**, and is moot given PA removal. — [UHC Gold Card page](https://www.uhcprovider.com/en/prior-auth-advance-notification/gold-card.html)

### 4.12 Home health routing decision tree for UHC MA

1. **MA / D-SNP in the 36 listed states + D.C.** → no PA, no concurrent review. Post-discharge: **advance notification within 2 business days after start of service**, via the portal.
2. **Erickson Advantage** → number on the member ID card, *not* 877-842-3210.
3. **Tennessee D-SNP** → PA (S9122 / S9123 / T1000), portal or 877-842-3210.
4. **Peoples Health (Louisiana)** → PA as of 8/1/2026, full G-code set, via the UnitedHealthcare Provider Portal (**not** Home & Community Care); authorizations line 866-273-9444.
5. **Preferred Care Network / Preferred Care Partners (Florida)** → **MedCare Home Health, 305-883-2940**, 24/7.
6. **River Valley entity** (parts of AR, GA, IA, IL, TN, VA, WI) → preauthorization required; after-hours notification within 24 hours or next business day; failure to notify = claim denial with **no member billing permitted**.
7. **Delegated IPA / medical group** → **follow the delegate's protocols. This overrides everything above.**
8. **Facility post-acute (SNF/IRF/LTCH)** → Home & Community Care, 855-851-1127. **Not the home health line.**

---

## 5. Humana

*(section populated below from dedicated payer research)*

---

## 6. Prior Authorization Regulation Now in Force

### 6.1 CMS-0057-F — the Interoperability and Prior Authorization final rule

**[PRIMARY]** Final rule **CMS-0057-F**, issued **January 17, 2024**, published in the Federal Register **February 8, 2024**. Impacted payers: **MA organizations, state Medicaid and CHIP fee-for-service programs, Medicaid managed care plans, CHIP managed care entities, and QHP issuers on the Federally Facilitated Exchanges.** **Every provision excludes prescription drugs.** — [CMS fact sheet, January 17, 2024](https://www.cms.gov/newsroom/fact-sheets/cms-interoperability-prior-authorization-final-rule-cms-0057-f) · [full rule text PDF](https://www.cms.gov/files/document/cms-0057-f.pdf)

#### What took effect January 1, 2026 (operational provisions)

| Requirement | Detail | Source |
|---|---|---|
| **Standard PA decision: 7 calendar days** | Down from the prior MA standard of **14 calendar days** at 42 CFR 422.568(b)(1). This is the headline change for home health. | [CMS fact sheet](https://www.cms.gov/newsroom/fact-sheets/cms-interoperability-prior-authorization-final-rule-cms-0057-f) |
| **Expedited PA decision: 72 hours** | **Unchanged** — MA was already at 72 hours under 42 CFR 422.572. | [CMS-0057-F rule text](https://www.cms.gov/files/document/cms-0057-f.pdf) |
| **Specific denial reason required** | Payers must give a **specific reason** for every denial, *"regardless of the method used to send the prior authorization request"* — portal, fax, email, mail, or phone. | [CMS fact sheet](https://www.cms.gov/newsroom/fact-sheets/cms-interoperability-prior-authorization-final-rule-cms-0057-f) |
| **Public PA metrics on payer website** | Annual public posting. **First set was due March 31, 2026**, covering calendar year 2025. | [CMS fact sheet](https://www.cms.gov/newsroom/fact-sheets/cms-interoperability-prior-authorization-final-rule-cms-0057-f) |
| **Patient Access API usage metrics to CMS** | Annual reporting began January 1, 2026. | [CMS fact sheet](https://www.cms.gov/newsroom/fact-sheets/cms-interoperability-prior-authorization-final-rule-cms-0057-f) |

**The extension caveat that matters most in practice.** **[PRIMARY]** The rule preserves existing extension authority. For MA standard organization determinations under **42 CFR 422.568(b)(1)(i)**, extensions are still permitted; the rule's own discussion of Medicaid FFS notes standard-decision extensions of **up to 14 calendar days**, and analogous extension provisions remain for MA. — [CMS-0057-F rule text, p. ~460 discussion of extension authority](https://www.cms.gov/files/document/cms-0057-f.pdf)

**Practically: "7 calendar days" is a ceiling on a clean, complete request, not a guarantee of a 7-day answer.** A plan that requests additional documentation restarts the practical clock. For a home health agency this means the CMS-0057-F timeframe does not by itself solve the start-of-care problem, because the binding constraint is the **48-hour initial assessment COP at 42 CFR 484.55**, and 7 days is still late relative to 48 hours.

#### What takes effect January 1, 2027 (the APIs)

**[PRIMARY]** All four APIs are due **January 1, 2027**, and all must be built on **HL7 FHIR Release 4.0.1** with US Core IG STU 3.1.1, SMART App Launch 1.0.0, FHIR Bulk Data Access STU 1, and OpenID Connect Core 1.0:

| API | What it must do |
|---|---|
| **Patient Access API** | Add prior authorization information (excluding drugs) to the existing patient-facing API. |
| **Provider Access API** | Share claims, encounter data, USCDI data elements, and PA information with **in-network providers with a treatment relationship**. Requires an attribution process and a patient **opt-out**. |
| **Payer-to-Payer API** | Share the same data classes on plan switch, for dates of service within **five years**. Requires patient **opt-in**. |
| **Prior Authorization API** | Must be populated with the payer's list of covered items/services, **identify documentation requirements for approval**, support the request and response, and communicate approval (with the date or circumstance under which authorization ends), denial **with a specific reason**, or a request for more information. |

CMS strongly recommends — but does not require — the Da Vinci implementation guides: **CRD (Coverage Requirements Discovery) STU 2.0.1**, **DTR (Documentation Templates and Rules) STU 2.0.0**, and **PAS (Prior Authorization Support) STU 2.0.1**. — [CMS fact sheet](https://www.cms.gov/newsroom/fact-sheets/cms-interoperability-prior-authorization-final-rule-cms-0057-f)

**[PRIMARY]** **HIPAA X12 278 enforcement discretion:** HHS will not enforce the X12 278 prior authorization transaction standard against covered entities that implement an all-FHIR Prior Authorization API under this rule. Payers may use FHIR-only, FHIR + X12, or X12-only. — [CMS fact sheet](https://www.cms.gov/newsroom/fact-sheets/cms-interoperability-prior-authorization-final-rule-cms-0057-f)

**[PRIMARY]** **Provider-side incentive:** a new attestation measure, **"Electronic Prior Authorization,"** is added to the Health Information Exchange objective for the MIPS Promoting Interoperability category and the Medicare Promoting Interoperability Program, beginning with the **CY 2027 performance period** (CY 2029 MIPS payment year) for clinicians and the **CY 2027 EHR reporting period** for hospitals and CAHs. Note: home health agencies are **not** MIPS eligible clinicians or eligible hospitals, so this measure does not apply to HHAs directly — it applies to the referring physicians and discharging hospitals. — [CMS fact sheet](https://www.cms.gov/newsroom/fact-sheets/cms-interoperability-prior-authorization-final-rule-cms-0057-f)

#### What CMS-0057-F does NOT do

- It does **not** require metrics reported **by service category**. There is no home health breakout in the mandated disclosures. **[PRIMARY-DERIVED]** KFF states this explicitly. — [KFF, August 13, 2026](https://www.kff.org/patient-consumer-protections/prior-authorization-metrics-provide-new-insights-into-insurer-practices-but-gaps-remain/)
- It does **not** require a standardized reporting template, which is why the first year of disclosures was hard to locate and hard to compare. — [KFF, August 13, 2026](https://www.kff.org/patient-consumer-protections/prior-authorization-metrics-provide-new-insights-into-insurer-practices-but-gaps-remain/)
- It does **not** reduce the *number* of services requiring prior authorization.
- It does **not** apply to Part D drugs.
- It does **not** obligate payers to accept a FHIR request before January 1, 2027 — so through 2026, portals, fax, and phone remain the operative channels.

**Decision-relevant:** for a platform being built now, the 2027 Prior Authorization API is the integration target worth designing toward, and the **DTR IG ("identify documentation requirements for prior authorization approval") is the piece that would let a scheduling system know, programmatically, what a given plan needs before a visit is scheduled.** But it is a 2027 capability at the earliest, adoption will be uneven, and CMS made the Da Vinci IGs recommended rather than required — so payer-by-payer variance will persist even after the deadline.

### 6.2 The 2024 MA final rule (CMS-4201-F) — coverage-criteria constraints

**[PRIMARY]** Final rule **CMS-4201-F**, issued **April 5, 2023**, effective for **contract year 2024**. Provisions relevant to home health:

- **MA plans must comply with NCDs, LCDs, and general coverage and benefit conditions in Traditional Medicare regulations.** Where Medicare coverage criteria are *not fully established*, MA organizations may create internal coverage criteria — but only based on current evidence in widely used treatment guidelines or clinical literature, and those criteria must be **made publicly available to CMS, enrollees, and providers.**
- **Prior authorization may only be used** to confirm the presence of diagnoses or other medical criteria and/or to ensure an item or service is medically necessary.
- **90-day continuity-of-care transition period** when an enrollee undergoing an active course of treatment switches to a new MA plan — during which the new plan **may not require prior authorization** for that active course of treatment.
- **Approval of a PA request for a course of treatment must be valid for as long as medically reasonable and necessary** to avoid disruptions in care, judged against applicable coverage criteria, the patient's medical history, and the treating provider's recommendation.
- **Every MA plan must establish a Utilization Management Committee** to review UM policies annually for consistency with traditional Medicare's national and local coverage decisions and guidelines.

— [CMS fact sheet, "2024 Medicare Advantage and Part D Final Rule (CMS-4201-F)," April 5, 2023](https://www.cms.gov/newsroom/fact-sheets/2024-medicare-advantage-and-part-d-final-rule-cms-4201-f)

**Two of these are directly weaponizable by a home health agency and are underused:**

1. **The "valid for as long as medically reasonable and necessary" provision** is a direct regulatory argument against 2-visit and 2-week reauthorization gates. If a plan approves a course of home health treatment, the approval is supposed to run the length of the medically necessary course — not an arbitrary visit block. I found no evidence of enforcement action on this point for home health.
2. **The 90-day continuity provision** directly addresses the mid-episode plan-switching failure mode described in §2.4.

**Did it work? The post-rule evidence is not encouraging.** See §7.

### 6.3 WISeR — and why it does *not* apply to home health

**[PRIMARY]** The **Wasteful and Inappropriate Service Reduction (WISeR) Model** is a six-year CMS Innovation Center model running **January 1, 2026 – December 31, 2031** in six states: **New Jersey, Ohio, Oklahoma, Texas, Arizona, and Washington.** It introduces prior authorization with AI-assisted review into **Traditional Medicare** for a narrow set of services. — [CMS WISeR model page](https://www.cms.gov/priorities/innovation/innovation-models/wiser)

**[PRIMARY]** The services in scope are **skin and tissue substitutes, implantation of electrical nerve stimulators, and knee arthroscopy for knee osteoarthritis.** The model **excludes inpatient-only services, emergency services, and services that would pose a substantial risk to patients if delayed.** All non-payment recommendations are made by licensed clinicians. Participants must meet a **72-hour turnaround** for requests submitted through a participant electronic portal, effective January 5, 2026 for dates of service on or after January 15, 2026. — [CMS WISeR model page](https://www.cms.gov/priorities/innovation/innovation-models/wiser) · [CMS WISeR FAQ](https://www.cms.gov/priorities/innovation/files/document/wiser-model-frequently-asked-questions)

**Home health is not in the WISeR service list.** For a home health capacity platform, WISeR is context, not a requirement. Its significance is as a **precedent**: CMS has now imported MA-style algorithmic prior authorization into traditional Medicare. If the model is judged successful, service-list expansion is the obvious next move — and home health, which MedPAC has repeatedly flagged for overpayment and which has documented fraud concentration (e.g., Los Angeles County, [MedPAC March 2026 Ch. 8, p. 259](https://www.medpac.gov/wp-content/uploads/2026/03/Mar26_Ch8_MedPAC_Report_To_Congress_SEC.pdf)), is a plausible candidate. That is speculation and should be labeled as such.

Congressional resolution of disapproval against WISeR was introduced; **the Senate declined to overturn the model.** — [Fierce Healthcare](https://www.fiercehealthcare.com/regulatory/legislators-introduce-resolution-seek-congressional-disapproval-cms-wiser-ai-prior-auth)

### 6.4 Gold carding and the voluntary industry pledge

**[PRIMARY — I fetched and read the AHIP release]** On **June 23, 2025**, AHIP and the Blue Cross Blue Shield Association announced voluntary industry commitments on prior authorization, explicitly *"being implemented across insurance markets, including for those with Commercial coverage, **Medicare Advantage** and Medicaid managed care consistent with state and federal regulations,"* covering a claimed **257 million Americans**. — [AHIP, "Health Plans Take Action to Simplify Prior Authorization," June 23, 2025](https://www.ahip.org/news/press-releases/health-plans-take-action-to-simplify-prior-authorization)

The six commitments, verbatim in substance:

| Commitment | Deadline |
|---|---|
| **Standardizing electronic prior authorization** — common, transparent submissions using **FHIR APIs**, with standardized data and submission requirements | Framework operational **January 1, 2027** |
| **Reducing the scope of claims subject to PA** — each plan commits to specific reductions "as appropriate for the local market each plan serves" | Demonstrated reductions by **January 1, 2026** |
| **Continuity of care on plan change** — the new plan honors existing prior authorizations for benefit-equivalent in-network services during a **90-day transition period** | **January 1, 2026** |
| **Clearer determination explanations**, including appeal support and next steps | Operational for **fully insured and commercial** by January 1, 2026; MA expansion only "with a focus on supporting regulatory changes" |
| **Real-time responses** — at least **80% of electronic PA approvals** (with all needed clinical documentation) answered in real time, with FHIR API adoption across all markets | **2027** |
| **Medical review of all clinical non-approvals** | "In effect now" |

**Signatories relevant here** (the release lists ~29): **UnitedHealthcare, Humana, CVS Health Aetna, Elevance Health, Centene, The Cigna Group, Kaiser Permanente**, plus Highmark, HCSC, GuideWell, Molina, SCAN Health Plan, Point32Health, Healthfirst, L.A. Care, Horizon BCBS NJ, and numerous Blues plans.

**Read the fine print carefully, because two of the six are weaker than they look for a home health agency:**

1. The **scope-reduction** commitment is explicitly *"as appropriate for the local market each plan serves"* — there is no floor, no service-line specificity, and **home health is nowhere named.**
2. The **clearer-determinations** commitment is operational for **fully insured and commercial** coverage only; MA expansion is conditioned on "supporting regulatory changes."
3. The **90-day continuity** commitment **duplicates a requirement MA plans have already been legally bound to since CY 2024** under CMS-4201-F (§6.2). For Medicare Advantage this is not a new commitment; it is a restatement of existing law.

**Decision-relevant:** the pledge is a real signal of direction — and UHC's April 2025 home health PA removal and Humana's reductions are consistent with it — but **it is voluntary, unenforced, unaudited, and contains no home-health-specific obligation.** Do not build a product roadmap on it. Build on CMS-0057-F, which is enforceable.

**[PRIMARY]** UnitedHealthcare's Gold Card program is live and national, but **home health is not among the eligible code sets** and the point is moot for UHC given its 2025 removal of home health PA (§4.11). — [UHC Gold Card](https://www.uhcprovider.com/en/prior-auth-advance-notification/gold-card.html)

### 6.5 State prior-authorization reform laws generally do NOT reach Medicare Advantage

**[PRIMARY — statute]** This is a point worth getting right because it is frequently assumed the other way. **42 U.S.C. §1395w-26(b)(3)**, verbatim:

> "The standards established under this part shall supersede any State law or regulation (other than State licensing laws or State laws relating to plan solvency) with respect to MA plans which are offered by MA organizations under this part."

— [42 U.S.C. §1395w-26(b)(3)](https://www.law.cornell.edu/uscode/text/42/1395w-26) (Social Security Act §1856(b)(3), as amended by Pub. L. 108-173 §232(a), December 8, 2003)

**Practical consequence:** state gold-carding mandates (e.g., Texas HB 3459), state AI-in-utilization-management statutes (e.g., California SB 1120), and state prior-authorization turnaround-time laws are, as a general matter, **preempted as applied to Medicare Advantage plans.** They govern commercial and often Medicaid managed care lines, not MA.

For a home health agency, this means **the same insurer can be operating under two different rule sets in the same state** — a state-mandated turnaround on its commercial book and the federal 7-day CMS-0057-F standard on its MA book. A platform that models "payer rules" without modeling *line of business* will get this wrong.

**Caveat on confidence:** the statutory text is verified and unambiguous. The *application* of preemption to any specific state statute is a litigated question I have not researched, and courts have carved exceptions. Treat the general rule as sound and any specific state-law question as requiring counsel.

---

## 7. Denial Rates, Appeal Overturns, and Turnaround Times

### 7.1 The 2026 breakthrough: OIG's post-acute data briefs

**[PRIMARY]** In **June 2026** (OEI-09-24-00331 is dated **June 11, 2026** in its companion's citation), HHS OIG issued two data briefs using **request-level prior authorization data from June 2024**, covering the **19 largest MAO parent companies (29.3 million enrollees, 86% of MA enrollment).** These are the strongest primary-source post-acute denial figures ever published. I read OEI-09-24-00330 in full; figures below are verbatim from it.

**OEI-09-24-00330 — LTCH and IRF** — [report page](https://oig.hhs.gov/reports/all/2026/the-three-largest-medicare-advantage-organizations-denied-requests-for-long-term-acute-care-and-inpatient-rehabilitation-at-some-of-the-highest-rates/) · [data brief PDF](https://oig.hhs.gov/documents/audit/11693/OEI-09-24-00330.pdf)

| Setting | Denial rate | Appealed | Overturned on appeal |
|---|---|---|---|
| **LTCH** | **65%** (~2,100 of 3,200) | 36% | 36% |
| **IRF** | **54%** (~10,500 of 19,400) | 31% | 43% |

By MAO — **LTCH**: CVS Health 80%, Highmark 73%, **Humana 72%**, **UnitedHealth 71%**, Elevance 63%, BCBS Michigan 44%, Cigna 33%, Centene 24%, UPMC 8%; all other 16 MAOs 42%.
By MAO — **IRF**: **UnitedHealth 66%**, Molina 64%, Highmark 60%, **Humana 54%**, **CVS 51%**, BCBS MI 50%, Kaiser 49%, Elevance 49%, Cigna 45%, HCSC 38%, Centene 33%, UPMC 20%, Devoted 12%, Corewell 6%, Healthfirst 4%.

For-profit vs. nonprofit contracts: LTCH **67% vs. 39%**; IRF **55% vs. 44%**.

**naviHealth specifically** — it processed **more than one third of all LTCH + IRF requests across all 19 MAOs**:

| Processor | LTCH denial rate | IRF denial rate |
|---|---|---|
| **naviHealth** | **73.5%** | **67.9%** |
| MAO internal | 64% | 46% |
| Other contractors | 51% | 47% |

**[PRIMARY]** OIG records UnitedHealth Group's own characterization, verbatim: *"naviHealth is an indirect wholly owned subsidiary of UnitedHealth Group… naviHealth is a first tier downstream contractor and delegate of various UnitedHealthcare entities and also an affiliated entity through common indirect ownership by UnitedHealth Group."* **81% of the requests naviHealth reviewed were for UnitedHealth Group**; it also processed requests for BCBS of Michigan and other MAOs. Note that OIG, writing in June 2026 about June 2024 data, still refers to the entity as **naviHealth** — see §4 on the current branding. — [OEI-09-24-00330, footnote 29 and Exhibit 7](https://oig.hhs.gov/documents/audit/11693/OEI-09-24-00330.pdf)

**OEI-09-24-00331 — SNF** — [report page](https://oig.hhs.gov/reports/all/2026/medicare-advantage-organizations-overturned-nearly-all-appealed-prior-authorization-denials-for-skilled-nursing-facility-admission-raising-concerns-about-initial-denials/)

- **12%** of SNF admission requests denied (range across MAOs: 23% to 0.4%)
- **18%** of SNF denials appealed
- **95% of appealed SNF denials were overturned.** OIG's own language: the *"extremely high overturn rate indicates that some enrollees were initially denied medically necessary care."*
- naviHealth processed **half of all SNF requests**, denied **14%**, and had **97%** of its SNF denials overturned on appeal
- **SNF requests for people who were already nursing home residents were denied at 40%**, versus 11% for other enrollees

**OEI-09-24-00332 — in progress.** A medical-record case-file review of whether denied post-acute requests actually met Medicare coverage rules — the "was the denial appropriate?" question the June 2026 briefs explicitly could not answer. Work plan item SRS-E-26-004; **estimated completion FY 2028.** — [OIG work plan](https://oig.hhs.gov/reports/work-plan/browse-work-plan-projects/srs-e-26-004/)

**The critical caveat: none of these three OIG reports covers home health.** They are LTCH, IRF, and SNF only.

**[PRIMARY]** OIG's own cost framing, from OEI-09-24-00330 Exhibit 4 (sourced to MedPAC's July 2025 Data Book and March 2025 Report to the Congress), average cost per episode in original Medicare, 2023: **home health $6,000 · SNF $16,000 · IRF $24,000 · LTCH $49,000.** OIG explicitly notes that **"information about what MAOs pay to different types of providers is not available"** — the same rate-transparency gap flagged in §1.3. This is the structural reason home health denial rates are almost certainly *lower* than SNF/IRF/LTCH — plans concentrate denial effort where the dollars are — while the *volume* of home health authorization transactions and downstream visit-reduction pressure is far higher.

### 7.2 The 2022 OIG baseline

**[PRIMARY]** Report **OEI-09-18-00260**, issued **April 27, 2022**. Stratified random sample of 500 denials (250 PA + 250 payment) from the 15 largest MAOs, drawn from June 1–7, 2019.

- **13%** of prior authorization denials **met Medicare coverage rules** — i.e., would have been approved in traditional Medicare
- **18%** of payment denials met Medicare coverage and MAO billing rules
- MAOs issued 1.5 million PA denials in 2018 (5% of requests)
- OIG named **post-acute facility stays** among the prominent service types denied despite meeting Medicare coverage rules, but published **no post-acute-specific denial rate** — the gap the 2026 briefs fill

— [OIG report page](https://oig.hhs.gov/reports/all/2022/some-medicare-advantage-organization-denials-of-prior-authorization-requests-raise-concerns-about-beneficiary-access-to-medically-necessary-care/) · [full PDF](https://oig.hhs.gov/oei/reports/OEI-09-18-00260.pdf)

**[PRIMARY]** For trend context, a **2018** OIG report (OEI-09-16-00410) found MAOs overturned **~75%** of their own PA and payment denials on appeal, 2014–2016.

### 7.3 The plan-reported numbers: two different denominators, do not mix them

There are now **two** distinct MA prior-authorization denial statistics in circulation, from two different data collections. Confusing them is the most common error in this space.

**(a) CMS plan-reported PA determinations — the long-running series.**
**[PRIMARY-DERIVED]** For **2024**: **52.8 million** prior authorization determinations; **4.1 million denied in full or in part = 7.7%** (up from 6.4% in 2023); **11.5% of denials appealed**; **80.7% of appealed denials overturned**; 1.7 requests per enrollee. By insurer: UnitedHealth Group **12.8%** denial rate at 1.0 requests/enrollee; Humana **5.8%** at 2.2 requests/enrollee; Elevance **4.2%** at 3.0 requests/enrollee. — [KFF, published January 28, 2026](https://www.kff.org/medicare/medicare-advantage-insurers-made-nearly-53-million-prior-authorization-determinations-in-2024/)

**(b) The new CMS-0057-F public disclosures — first year, calendar year 2025 data, posted by March 31, 2026.**
**[PRIMARY-DERIVED]** KFF collected these from the largest insurers (≥2.5% market share), covering **25 million MA enrollees = 69% of MA enrollment**, enrollment-weighted:

| Metric | Medicare Advantage | Medicaid MC | ACA FFM |
|---|---|---|---|
| Standard PA requests denied | **12%** | 14% | 18% |
| Expedited PA requests denied | **10%** | 12% | 16% |
| Standard denials overturned on appeal | **67%** | 47% | 43% |
| Median response time, standard | **0.9 days (~22 hrs)** | 0.9 days | 0.9 days |
| Median response time, expedited | **0.4 days (~10 hrs)** | 0.8 days | 1 day |

MA denial rate by insurer, standard requests: **Elevance 5%** (lowest) to **UnitedHealth Group 17%** (highest). Expedited: Elevance 3% to **Centene 13%**. Overturn rates ranged from **Kaiser 40%** to **Centene >90%**.
Median standard response time by MA insurer: **under 1 day (CVS, Humana, Kaiser)** to **2 days (Centene)**.
— [KFF, "Prior Authorization Metrics Provide New Insights into Insurer Practices, but Gaps Remain," published August 13, 2026](https://www.kff.org/patient-consumer-protections/prior-authorization-metrics-provide-new-insights-into-insurer-practices-but-gaps-remain/)

**Read the median response time with extreme care.** KFF is explicit that **insurers are not required to report by service category or to report ranges**, so the 0.9-day median is an all-services aggregate dominated by high-volume, easily automated requests. **It is not the home health experience and should never be presented as such.** KFF's own qualifier: *"other research and media reports demonstrate that some patients experience much longer response times."*

Note also that the 2025 reporting year predates the 7-day requirement — in 2025 the MA standard was still 14 calendar days.

**[PRIMARY-DERIVED]** KFF's structural criticism, which is the most decision-relevant point for a platform: *"gaps in how... and what metrics (e.g., denominators and breakouts by service category) must be reported limit the usability of this information."* Also relevant: in Medicare Advantage, **if the plan upholds its original denial the case is automatically sent to an independent review entity** — a protection that does not exist in Medicaid managed care or the ACA Marketplace, and one OIG has suggested explains MA's higher overturn rates.

### 7.4 Senate PSI, "Refusal of Recovery," October 17, 2024

**[PRIMARY / congressional — majority staff report. I downloaded the 150 MB PDF and extracted the full text; quotations below are verbatim from the report.]** Covers **2019–2022**, built on documents obtained from UnitedHealthcare, Humana, and CVS/Aetna. — [Senate PSI report PDF](https://www.hsgac.senate.gov/wp-content/uploads/2024.10.17-PSI-Majority-Staff-Report-on-Medicare-Advantage.pdf) · [Blumenthal release, October 17, 2024](https://www.blumenthal.senate.gov/newsroom/press/release/senate-permanent-subcommittee-on-investigations-releases-majority-staff-report-exposing-medicare-advantage-insurers-refusal-of-care-for-vulnerable-seniors)

**⚠️ Scope correction that almost every secondary summary gets wrong.** PSI's post-acute denial-rate data covers **skilled nursing facilities, inpatient rehabilitation facilities, and long-term acute care hospitals — not home health.** Verbatim: *"PSI collected data from the three companies on their annual use of prior authorization for Medicare Advantage beneficiaries in skilled nursing facilities, inpatient rehabilitation facilities, and long-term acute care hospitals."* **The headline 22.7% / 24.6% / 25.9% post-acute denial rates do not include home health.**

**UnitedHealthcare — verified from the report text**
- Post-acute care denial rate: **8.7% (2019) → 10.9% (2020) → 16.3% (2021) → 22.7% (2022)** — *"an increase of 172 percent"*
- Meanwhile its **overall** PA denial rate barely moved: **7.3% (2019) → 7.6% (2022)**. PAC was roughly **3x** overall in 2022.
- **Home health, verbatim:** *"The insurer's prior authorization denial rates for home health services **declined** during the period covered by this report. But there was a vast increase in the number of Medicare Advantage beneficiaries using these services: in naviHealth's first full year of managing post-acute care for UnitedHealthcare, the insurer processed **more than four times as many home health prior authorization requests as it did the year before**, far beyond the company's growth in enrollment."*
- **UHC's own explanation to PSI:** growth in PA requests came from business strategies unconnected to SNF adverse determinations; *"In some instances, UnitedHealthcare began imposing prior authorization on the provision home health services for which it previously was not required,"* and it *"expanded its presence in the field in response to CMS's decision to change the standard unit of payment for home health care, beginning Jan. 1, 2020, from 60 days to 30 days"* — i.e., **PDGM itself triggered the MA home health authorization build-out.**

**The most decision-relevant passage in the entire report, and it is about home health specifically.** PSI obtained internal documents describing a **"home health management solution"** that naviHealth launched for UHC's MA members **in Georgia**, planned to expand to other markets:

> a *"technology centered Home Health [utilization management] model"* that would create savings by **"reducing home health visits/episode."** Early metrics from Georgia indicated *"changes in provider behavior,"* and naviHealth's *"prior authorization oversight"* had enabled it to identify instances of **"excess" home health services.**

**Read those two findings together.** UHC's home health *denial rate went down* while its home health *authorization volume went up four-fold, and the explicit design goal of the tooling was reducing visits per episode.* **This is the mechanism by which MA compresses home health revenue: not denial, but authorized-visit reduction inside an approved episode.** It is invisible in every denial-rate statistic ever published, and it is precisely what a scheduling-and-capacity platform is positioned to measure.

PSI also documented that a January 2022 naviHealth presentation included a sample patient journey in which a *"naviHealth Care Coordinator completes nH Predict… to determine optimal [post-acute care] placement"* while the patient was still hospitalized, and that in April 2022 naviHealth instructed pre-service coordinators: *"IMPORTANT: Do NOT guide providers or give providers answers to the questions"* used to collect prior authorization information.

**Humana — verified from the report text**
- 2022 post-acute denial rate was **over 16 times higher** than its overall denial rate — the widest gap of the three insurers by a large margin
- **LTACH denial rate grew 54% between 2020 and 2022**, after training sessions devoted to LTACH prior authorization requests
- In fall 2019 Humana modified reviewer decision templates; a lead medical director noted changes for two post-acute facility types were *"important for denial purposes"* and would enhance the company's ability *"to uphold a denial on appeal."*

**CVS / Aetna — verified from the report text**
- 2022 post-acute denial rate roughly **3x** its overall rate
- A March 2022 internal presentation on prior authorization automation stated CVS had **"de-prioritized"** a plan to reduce overall PA volume, concluding the impact on lost savings was **"too large to move forward."**

**[INDUSTRY — secondary, could not verify against report text]** The specific figures **Humana 24.6%** and **CVS 25.9%** post-acute denial rates, UHC SNF denials **1.4% (3,016) in 2019 → 12.6% (34,359) in 2022**, UHC home health PA requests **19,283 (2019) → 356,606 (2022)**, and CVS PA volume **+57.5%** circulate widely but appear in the report as charts rather than extractable text. Sourced via [LeadingAge analysis](https://leadingage.org/analysis-senate-report-on-ma-plans-reveals-troubling-data/) and [McKnight's](https://www.mcknights.com/news/senate-report-hits-top-3-medicare-advantage-insurers-over-refusal-of-of-skilled-nursing-other-coverage/). They are consistent with the verified narrative text but should be attributed to those secondary readings, not quoted as PSI figures.

### 7.5 Measured post-acute turnaround — the only real timing data

**[PRIMARY]** From OIG OEI-09-24-00330 (June 2024 data):

- Median time from initial request to **appeal decision**: **6 days (LTCH)**, **5 days (IRF)**
- Median IRF path: Day 0 request → Day 2 denial → Day 3 appeal filed → Day 5 appeal decision
- **16% of LTCH appeals and 8% of IRF appeals took 10 or more days**
- OIG notes the patient is typically occupying an acute-care hospital bed throughout, and links delay to reduced functional recovery, hospital-acquired complication risk, and unreimbursable avoidable days

— [OEI-09-24-00330 PDF](https://oig.hhs.gov/documents/audit/11693/OEI-09-24-00330.pdf)

**[INDUSTRY — vendor, treat as directional]** Homecare Homebase reports median **referral-entry-to-start-of-care exceeding 69 hours**, with more than 13 hours inside intake alone, and referral conversion falling from **77% (2018) to 64% (Q2 2025)**. — [Homecare Homebase, February 9, 2026](https://hchb.com/home-healthcare-in-2026-demand-isnt-the-problem-capacity-is/)

**[UNVERIFIED — DO NOT CITE]** Trade-press claims of "7–10 day MA home health authorization waits" and a "28% increase in referral-to-SOC time 2022–2025" could not be traced to a primary or named-methodology source. The 28% figure did not appear on the vendor page it is attributed to.

### 7.6 Home-health-specific denial data — the gap, stated plainly

I searched OIG, CMS, KFF, MedPAC, AHA, and The National Alliance for Care at Home. **There is no published, primary-source Medicare Advantage prior-authorization denial rate for home health.** Not from any source. The specific gaps:

- OIG's post-acute work covers **LTCH, IRF, SNF only**
- CMS's new CMS-0057-F transparency metrics have **no service-category breakout**
- KFF's analyses inherit that limitation
- No **days-in-A/R comparison** for MA vs. traditional Medicare in home health with a stated methodology
- No credible **administrative cost per authorization** figure for home health
- No association survey quantifying MA home health denial rates or authorization turnaround
- No verified figure for **% of HHAs declining MA referrals**, or staff hours per authorization

**This absence is itself a finding, and arguably the most commercially interesting one in the file.** Every operator knows MA home health authorization is the problem; nobody has ever measured it. A platform that instruments authorization request → decision → visit allotment → reauth at scale would be generating the first dataset of its kind. OIG's first recommendation in OEI-09-24-00330 is that **CMS begin regularly collecting request-level PA data including standardized service type and contractor name** — CMS **did not explicitly concur**, and the recommendation is open with a status update due **December 7, 2026**.

### 7.7 Did CMS-4201-F change anything? The evidence says no

**[PRIMARY-DERIVED]** The overall MA denial rate **rose** after the rule took effect: **6.4% (2023) → 7.7% (2024)**, with denial volume rising from 3.2M to 4.1M. — [KFF, January 28, 2026](https://www.kff.org/medicare/medicare-advantage-insurers-made-nearly-53-million-prior-authorization-determinations-in-2024/)

**[PRIMARY]** Post-acute denial rates measured in **June 2024 — six months into the rule** — were 65% LTCH, 54% IRF, 12% SNF, with a **95% SNF appeal overturn rate.** A 95% overturn rate is not the signature of a plan applying criteria aligned with traditional Medicare. — [OEI-09-24-00330 / -00331, June 8, 2026](https://oig.hhs.gov/documents/audit/11693/OEI-09-24-00330.pdf)

**[PRIMARY]** OIG's structural finding: CMS *"did not regularly collect request-level prior authorization data that included standardized service types or contractor names"* — meaning **CMS lacked the data to enforce CMS-4201-F's central promise.** CMS did not explicitly concur with the recommendation to fix this.

**[INDUSTRY]** AHA reports that MA patients face **9.6% longer hospital stays** before discharge to post-acute care versus comparable traditional Medicare patients, and that average length of stay before PAC discharge **doubled relative to traditional Medicare between 2019 and 2024**. AHA also reports MA claim denials rose **55.7% from 2022 to 2023**. — [AHA 2025 Cost of Caring Report, published March 9, 2026](https://www.aha.org/guides-and-reports/2026-03-09-2025-cost-caring-report) · [AHA on the OIG reports, June 11, 2026](https://www.aha.org/news/headline/2026-06-11-hhs-oig-reports-highlight-ma-insurer-denials-long-term-care-rehab-services-and-snf-admissions)

**[INDUSTRY SURVEY]** Home Health Care News 2026 reader survey: **37.5%** named prior authorizations and delays among top challenges; **43.8%** said reducing prior authorization requirements would most improve their financial burden. — [Home Health Care News, June 2026](https://homehealthcarenews.com/2026/06/medicare-advantage-medicaid-persist-as-top-concern-among-home-based-care-leaders/) *(page returned 403 to direct fetch; figures via search index — verify before using in a client deliverable)*

**[UNVERIFIED — DO NOT CITE]** A "denials jumped 56% in 2026" claim circulating on medical-billing vendor blogs has no stated methodology and no primary source. The defensible trend statement is: **MA PA denial rate rose from 6.4% to 7.7% between 2023 and 2024, and post-acute denial rates remain multiples of the overall rate.**

### 7.8 One organizational correction for the record

**[PRIMARY]** NAHC and NHPCO signed their affiliation agreement in **June 2024**, effective **July 1, 2024**; the name **"The National Alliance for Care at Home"** was unveiled in **September 2024** — not 2025. Site: [allianceforcareathome.org](https://allianceforcareathome.org/). — [Home Health Care News, September 2024](https://homehealthcarenews.com/2024/09/nahc-nhpco-merger-becomes-national-alliance-for-care-at-home/)

---

## 8. What This Means for a Branch Capacity-and-Scheduling Platform

Deliberately short, and separated from the research so the sourcing above stands on its own.

1. **Payer rules are contract-level data, not reference data.** Nothing published — not by CMS, not by the plans — tells you a given MA contract's visit allotment or reauth interval. It must be captured at implementation, per contract, per branch. That is a cost to onboarding and a moat once built.
2. **The scheduling optimization inverts by payment model.** PDGM branches optimize clinician time against a fixed period payment. Per-visit MA branches optimize authorized-visit utilization and discipline-cost matching. A mixed-payer branch — the normal case, at 92% of agencies — runs both simultaneously. In the one multi-branch operator dataset that has been published (102 locations, 19 states), **roughly 60% of MA stays were per-visit** ([Prusynski et al., AJMC, November 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC13137865/)).
2b. **Per-visit contracts carry a measured clinical penalty, and that is the strongest sales argument in this file.** Per-visit MA stays had **12% higher odds of mid-stay inpatient transfer than episodic MA stays** — the outcome the plan most wants to avoid — with the implied mechanism being loss of agency discretion over visit mix and timing ([Prusynski et al., AJMC, November 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC13137865/)). A platform that recovers timing and discipline-match quality inside per-visit constraints is intervening exactly where the harm is documented, and the beneficiary of the improvement is the payer as much as the agency.
3. **Authorization state must be a first-class scheduling constraint,** not a billing-side reconciliation. The documented loss is agencies delivering care at risk to meet the 48-hour initial-assessment COP and writing it off when authorization does not land.
4. **Reauth is a scheduling event with a lead time.** A plan that gates at 30 units and expects contact at unit 25 is telling you the reauth workflow needs to fire five visits early. Same for 2-week and 30-day cycles.
5. **The 2027 FHIR Prior Authorization API is the integration horizon**, with the Da Vinci DTR IG as the specific piece that would make documentation requirements machine-readable. Design toward it; do not depend on it, because CMS made the IGs recommended rather than required.
6. **The measurement gap is the opportunity.** No one has ever published MA home health denial rates, turnaround times, or authorization administrative cost. An instrumented platform would hold the first such dataset — and OIG has an open, unconcurred recommendation asking CMS to start collecting exactly this.

---
