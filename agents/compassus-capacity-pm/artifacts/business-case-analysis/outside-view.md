# The Outside View

**Reference-class evidence on workforce capacity-and-scheduling initiatives in healthcare**

Prepared 21 August 2026. This document deliberately ignores the specifics of the proposed
initiative. It answers one question: *when organisations like this build things like this, what
actually happens?*

A note on method. Reference-class forecasting works only if the reference class is real. For
several of the questions below, it is not — the evidence is thin, vendor-controlled, or
methodologically weak. Where that is true this document says so rather than manufacturing a
number. **An honest "we don't know, and here is why nobody knows" is more useful to a business
case than a confident figure with no foundation.**

Throughout, evidence is tagged:

- **[IND]** — independent: peer-reviewed, government, or non-sponsored evaluation
- **[SELF]** — self-reported by the implementing organisation
- **[VENDOR]** — published or sponsored by a party selling the product
- **[CONSULT]** — consultancy or analyst survey, usually self-selected sample

*On links: every URL below was checked on 21 August 2026. Publisher domains (Wiley, SAGE, Oxford,
Annals, Health Affairs, ScienceDirect, INFORMS) return 403 to automated requests but resolve
normally in a browser; DOIs are given as the canonical reference, with an open-access PMC mirror
where one exists.*

---

## 1. Workforce scheduling and capacity optimisation in healthcare

### 1.1 The headline finding: the academic literature is large and the implementation record is small

The single most important fact about healthcare scheduling optimisation is that an enormous
research literature has produced very few documented deployments.

**[IND]** Kellogg and Walczak reviewed 50 nurse-scheduling models and methods published
1985–2005 and traced what happened to them. Only 15 of the 50 were ever implemented — a 30%
implementation rate. Of those 15, seven ran in a single hospital, two in a single ward or nursing
unit, four in multiple hospitals, and two became commercial packages. The authors identify a
large research–application gap.
*Kellogg, D.L. & Walczak, S. (2007), "Nurse Scheduling: From Academia to Implementation or Not?",
Interfaces 37(4), 355–369.*
https://www.researchgate.net/publication/220249866_Nurse_Scheduling_From_Academia_to_Implementation_or_Not

That is the base rate for the *technique*, before you ask whether it delivered anything. Roughly
two thirds of published scheduling optimisation approaches never reach practice at all, and of
those that do, the modal outcome is a single-site deployment that never scales.

The reasons documented in the follow-on literature are consistent and are *not* algorithmic:
lack of early engagement with nurses and schedulers, absence of nurse-centred design, weak links
between academics and scheduling software vendors, and — critically — that constraints and rules
differ between institutions, between wards in the same institution, and even between planning
horizons within the same ward.
*Cited in "The Nurse Scheduling Problem in Real-Life", Journal of Medical Systems (2014).*
https://link.springer.com/article/10.1007/s10916-014-0160-8

**Read that constraint finding carefully.** It is the mechanism behind most scheduling-project
disappointment: the optimiser is not wrong, the constraint model is incomplete, and the
constraint model is incomplete because the real rules were never written down anywhere.

### 1.2 What the systematic reviews actually say

Three recent systematic reviews cover rostering and scheduling interventions in nursing. All
three reach the same conclusion about evidence quality.

**[IND]** Wynendaele et al. (2021), *Journal of Advanced Nursing* — systematic review of
self-scheduling, 23 studies retained, quality assessed with the Mixed Methods Appraisal Tool.
Conclusion, verbatim: *"The evidence base is limited. Several studies confirmed the positive
impact of self-scheduling on the nurse and the organization. However, other studies found
negative outcomes or no change."* The review notes outcomes *"are influenced by the
implementation process and the sustainability of the self-scheduling system, which are still
major challenges for healthcare management."*
https://doi.org/10.1111/jan.14579 (published 2021; PMID 33016472)

**[IND]** O'Connell et al. (2024), *Journal of Clinical Nursing* 33:2374–2387 — mixed-method
systematic review of electronic and self-rostering systems. Eighteen studies included: **10
quantitative descriptive, 7 non-randomised, 1 qualitative. Zero randomised trials.** Reported
improvements in roster efficiency, staff satisfaction, work–life balance, retention and absence
rates. The one substantial quantitative finding cited is from D'souza et al. (2021): time to
complete nurses' schedules fell from 45 minutes to 10 minutes per day after implementing the ROTA
automated scheduling system, saving 175 staff hours, equal to 78% of ward managers' scheduling
time, and *"almost 3% savings in the total budget assigned to nursing staff."* The review also
records that self-rostering was *less* fair than fixed rostering and was associated with
**increased overtime** and more shift-change requests.
https://doi.org/10.1111/jocn.17114

**[IND]** Morse et al. (2024), *Nursing Administration Quarterly* — rapid review of centralized
nursing scheduling following Cochrane Rapid Reviews methodology. 446 articles screened, **12
included.** The findings on improved labour productivity (less overtime, less contracted labour,
less floating) come from *"case study reports"* plus one computational experimental study. No
controlled before/after evidence.
https://doi.org/10.1097/naq.0000000000000653

### 1.3 What this means for a business case

Note the shape of the evidence. The best-documented, most reliably realised benefit in the entire
nurse-scheduling literature is **administrative time saved by the scheduler** — the 45→10 minute
finding. That is a real benefit and it is the one that shows up consistently.

The benefits that business cases are usually *built* on — reduced agency spend, higher clinical
utilisation, lower overtime — are the ones the reviews describe as inconsistent, contextual, or
occasionally *negative*. One of the two rostering interventions reviewed by O'Connell was
associated with increased overtime.

**Honest summary of question 1: there is no credible published effect size for agency-spend or
utilisation improvement from healthcare scheduling optimisation.** Anyone quoting one is quoting
either a single uncontrolled case study or a vendor. The reference class is real but the
measurement in it is poor.

### 1.4 Home health scheduling specifically

The home health care routing and scheduling problem (HHCRSP) is a well-developed academic field —
it combines the vehicle routing problem with time windows and the nurse rostering problem. There
are hundreds of papers.

**The independent, real-world outcome evidence is close to non-existent.** A 2025 review of the
field confirms the literature is dominated by problem formulations, algorithms and computational
experiments rather than deployed evaluations.
*"A Concise Review of the Home Health Care Routing and Scheduling Problem", 2025.*
https://www.sciencedirect.com/science/article/pii/S2214716025000235

Where case studies exist they are typically validation exercises for a proposed model against one
agency's data (e.g. a Tehran health centre used to test a bi-objective model), not
before/after evaluations of a live deployment.
https://pmc.ncbi.nlm.nih.gov/articles/PMC7908566/

**This is a genuine gap and it should be stated plainly in any business case: there is no
published, independent, controlled evidence quantifying the operational benefit of scheduling
optimisation in home health.** Benefit estimates in this domain are extrapolations, not
observations.

### 1.5 A cautionary precedent from home health workforce technology: EVV

Electronic Visit Verification is the closest thing to a natural experiment in mandated home-health
workforce tracking technology. The 21st Century Cures Act (2016) required all Medicaid-funded
personal care services to be documented through EVV by January 2020.

**[IND]** *"Most states have asked for extensions due to difficulties in implementation and strong
opposition from consumer advocacy groups."*
*Home Healthcare Now (2022), 40(1).* https://doi.org/10.1097/nhh.0000000000001038

**[IND]** Qualitative interviews with 21 home-based personal assistance consumers and 20 workers
found EVV was perceived as *"intrusive, reduces flexibility"*.
*Disability and Health Journal (2020).* https://doi.org/10.1016/j.dhjo.2020.100938

The lesson is not that EVV was a bad idea. It is that a **federally mandated, funded, universally
required** home-health workforce technology, with no competitive alternative and no option to
decline, still slipped years past its deadline in most states because of implementation
difficulty and frontline opposition. A voluntary internal initiative has fewer levers than that,
not more.

---

## 2. Realised versus promised ROI in healthcare and enterprise technology

### 2.1 The canonical large-sample findings

**[IND/CONSULT]** McKinsey–Oxford study of more than 5,400 IT projects each costing over $15
million: on average they run **45% over budget, 7% over time, and deliver 56% less value than
predicted.** One in six is a "black swan" with an average 200% cost overrun.
*Bloch, Blumberg & Laartz, McKinsey Quarterly, October 2012.*
https://www.mckinsey.com/~/media/McKinsey/dotcom/client_service/BTO/PDF/MOBT_27_Delivering_large-scale_IT_projects_on_time_budget_and_value.ashx

The **56% benefit shortfall** figure is the single most-cited number for realised-versus-promised
IT value and it is the right starting anchor.

**[IND]** Flyvbjerg & Budzier (2011), *Harvard Business Review* 89(9):23–25, analysing 1,471 IT
projects (average cost $167m; 92% public-sector; 83% US-based). Verbatim: *"The average overrun
was 27% — but that figure masks a far more alarming one... Fully one in six of the projects we
studied was a black swan, with a cost overrun of 200%, on average, and a schedule overrun of
almost 70%."*
https://hbr.org/2011/09/why-your-it-project-may-be-riskier-than-you-think
Full text: https://arxiv.org/pdf/1304.0265

### 2.2 The important refinement — and it cuts both ways

**[IND]** Flyvbjerg, Budzier, Lee, Keil, Lunn & Bester (2022), "The Empirical Reality of IT
Project Cost Overruns: Discovering A Power-Law Distribution", *Journal of Management Information
Systems* 39(3):607–639. Sample: **5,392 IT projects** completed 2002 onwards, across 66 countries.
https://ora.ox.ac.uk/objects/uuid:a6ea9269-366c-4c7a-8b05-782f5fa3b0d2

Key findings, which materially change how to read the earlier numbers:

- Mean cost-overrun ratio (actual/estimated) was **1.8**. But the **mode and median are close to
  1.0 — i.e. on budget.** Verbatim: *"contrary to conventional wisdom, there is a strong tendency
  for IT projects to be on budget (mode and median close to 0% overrun)."*
- Overruns and underruns are **about equally frequent.**
- The distribution is power-law with α < 2 in the tail, which means *"the tail is so fat that
  neither mean nor variance exist."* Verbatim: *"the average cost overrun for IT projects does not
  exist (i.e., cannot be calculated), and this should be a sobering thought for anyone concerned
  with the risk associated with financing IT projects."*

**Directly relevant to a workforce platform:** the paper breaks results out by project type. For
**HRM-class projects (n=459)**, mean cost-overrun ratio was **1.5** and **median 1.0**. For ERP
(n=1,612), mean 1.3, median 0.9. So a workforce/HR-type system is more likely than not to land
near budget — with a real tail risk of catastrophic overrun.

The correct reading for a business case: **do not plan against the mean.** The median project
hits its cost estimate. A minority of projects destroy the programme. Ask "what is our exposure
if we are in the tail?" not "what is the expected overrun?"

### 2.3 Healthcare-specific project failure rates

**[IND]** Kaplan, B. & Harris-Salamone, K.D. (2009), "Health IT Success and Failure:
Recommendations from Literature and an AMIA Workshop", *JAMIA* 16(3):291–299. Verbatim findings
compiled by the authors:

- *"at least 40% of such generic IT projects either are abandoned or fail to meet business
  requirements"*
- *"fewer than 40% of large systems purchased from vendors meet their goals"*
- *"as few as one in eight information technology projects is considered truly successful"*
- Citing Standish CHAOS data: *"only 35% of IT projects were completed on time, on budget, and met
  user requirements"*; roughly two-thirds of projects had significant problems, including 19% that
  *"failed outright"*
- On healthcare specifically: *"Similar failure rates have been reported specifically for health
  IT"*, citing Heeks (2006), whose *"best estimate that most HIS [health information systems] fail
  in some way."*

https://pmc.ncbi.nlm.nih.gov/articles/PMC2732244/

*Caveat you should apply: the Standish CHAOS numbers embedded in this paper are widely used and
also widely criticised on methodology — self-selected respondents, shifting definitions of
"success", and no published sampling frame. Treat 35%/19% as directionally indicative, not as
measurements.*

### 2.4 Digital transformation success rates

**[CONSULT]** McKinsey global survey on digital transformations: *"less than 30 percent
succeed."* Only **16%** of respondents said their organisation's digital transformation had both
improved performance **and** equipped the organisation to sustain the change long-term. A further
**7%** said performance improved but the improvement was **not sustained**. Even in digitally
sophisticated industries (high tech, media, telecom) success rates did **not exceed 26%**.
*McKinsey, "Unlocking success in digital transformations", October 2018.*
https://www.mckinsey.com/capabilities/people-and-organizational-performance/our-insights/unlocking-success-in-digital-transformations

The 16%/7% split is the most decision-relevant number in this document. **Roughly a third of the
programmes that do produce a performance improvement then fail to hold it.** Sustainment is a
separate hurdle from delivery, and it is cleared less often than delivery is.

*Caveat: self-reported survey of executives about their own programmes. Both optimism bias
(inflating success) and hindsight/attribution problems apply. But note the direction of the
likely bias — executives grading their own transformations should over-report success, and they
still only reached 16%.*

### 2.5 Enterprise system benefits realisation

**[CONSULT]** Panorama Consulting, *The 2024 ERP Report*. n=131 respondents; **median project
cost $450,000; median timeline 15.5 months.** More than half stayed within expected budget and
more than half completed within expected timeline. Among those over budget, the most common cause
was *"the unexpected need for additional technology"* (up from 32.8% the prior year). Among those
over schedule, the most common cause was **resource constraints** (up from 37.7%).
https://4439340.fs1.hubspotusercontent-na1.net/hubfs/4439340/Reports/ERP%20Report/2024-erp-report-panorama-consulting-group.pdf

*Heavy caveat: Panorama is an ERP consultancy reporting on a self-selected sample of its own
market, and much of the report's data sits in chart images rather than text. It is directionally
useful for **causes** of overrun, not for base rates.*

Earlier editions of the same series reported that **41% of organisations realised less than half
the benefits they anticipated, and a further 16% realised no measurable benefit at all** — i.e.
roughly 57% materially missed their business case. Same caveats apply; treat as indicative.
https://www.panorama-consulting.com/resource-center/erp-report-archives/

### 2.6 The finding that matters most, and is least discussed

**Most healthcare organisations never measure realised ROI at all.**

**[IND]** National Academy of Medicine, "Return on Information: A Standard Model for Assessing
Institutional Return on Electronic Health Records", 6 January 2014. Verbatim: *"it remains
difficult to measure the return on investment (ROI) in information systems"* and *"a commonly
accepted framework is lacking for identifying and quantifying costs and benefits."* Of the
positive reports that do exist at scale, *"the methodologies used have not been generalizable
across provider organizations... each one has used different and, consequently, incomparable
methods."*
https://nam.edu/perspectives/return-on-information-a-standard-model-for-assessing-institutional-return-on-electronic-health-records/

**[IND]** Cresswell, Sheikh, Franklin et al. (2022), "Benefits realization management in the
context of a national digital transformation initiative in English provider organizations",
*JAMIA* 29(4). Independent national evaluation of the NHS Global Digital Exemplar Programme: 36
longitudinal case studies, 628 interviews, 499 documents, 190 observations.
https://doi.org/10.1093/jamia/ocab283 (open access: https://pmc.ncbi.nlm.nih.gov/articles/PMC8800528/)

Findings directly applicable here:

- Central benefit-tracking requirements *"had limited perceived local value and were seen to
  impose an unnecessary burden on provider organizations."*
- There were *"tensions between the desire for early evidence of outcomes and the slow processes
  of infrastructural change (which created problems of attribution of benefits to causes as
  benefits emerged gradually and over long timeframes)."*
- And tensions *"between reporting immediately visible local changes and showing how these flowed
  through to high level organization wide benefits (eg, in terms of health outcomes or cost
  savings/return on investment). The attempt to fulfill these diverging agendas... within a single
  reporting tool had limited success."*
- Conclusion: *"benefits may materialize over long timeframes and in unanticipated ways."*

**[IND]** Tursunbayeva, Bunduchi & Pagliari (2020), "'Planned benefits' can be misleading in
digital transformation projects: Insights from a case study of Human Resource Information Systems
implementation in healthcare", *SAGE Open* 10(2). A national-scale healthcare HRIS programme —
the closest published analogue to a workforce platform. The authors find planned-benefits
approaches need review at regular intervals, benefits must be assessed *per module and per user
group* rather than only organisation-wide, and that data preparation, training, communication and
process analysis are the gating actions for realisation.
https://doi.org/10.1177/2158244020933881

**The practical consequence: a business case that promises a benefit but does not specify who will
measure it, against what baseline, and when, will not be falsified. It will simply stop being
discussed.** That is the modal outcome, and it is worse than failure because it is invisible.

### 2.7 The counter-example, for balance

**[IND]** Jang, Lortie & Sanche (2014), "Return on Investment in Electronic Health Records in
Primary Care Practices: A Mixed-Methods Study", *JMIR Medical Informatics* 2(2):e25. Of 17
sampled primary care clinics, **16 (94%) achieved positive financial returns**, recovering EHR
investment in an average of **10 months (95% CI 6.2–17.4)**. Active-patients-per-clinician-FTE
rose 27%; active-patients-per-clinical-support-staff-FTE rose 10%.
https://pmc.ncbi.nlm.nih.gov/articles/PMC4288109/

Authors' own conclusion, verbatim: *"A positive ROI does not happen automatically upon
implementing an EHR package, and a clinic's ability to leverage EHR for process changes plays a
role in achieving a positive ROI."*

*Caveat: n=17, self-selected, single jurisdiction (Quebec), no control group. Strong survivorship
risk. Cited here because it is the best-case end of the distribution and because even its authors
attribute the return to process change rather than to the software.*

---

## 3. Failure rates and failure modes

### 3.1 Rates

Consolidating the credible estimates:

| Measure | Figure | Source | Type |
|---|---|---|---|
| Generic IT projects abandoned or failing business requirements | ≥40% | Kaplan & Harris-Salamone 2009 | [IND] |
| Large vendor-purchased systems meeting their goals | <40% | Kaplan & Harris-Salamone 2009 | [IND] |
| Large IT projects: value delivered vs predicted | −56% | McKinsey–Oxford 2012, n=5,400+ | [IND/CONSULT] |
| Digital transformations that succeed | <30% | McKinsey 2018 | [CONSULT] |
| Digital transformations that succeed *and* sustain | 16% | McKinsey 2018 | [CONSULT] |
| Nurse-scheduling methods reaching implementation | 30% | Kellogg & Walczak 2007, n=50 | [IND] |
| IT projects: median cost overrun | ~0% | Flyvbjerg et al. 2022, n=5,392 | [IND] |
| IT projects: proportion that are catastrophic outliers | ~1 in 6 | Flyvbjerg & Budzier 2011 | [IND] |

### 3.2 What actually kills them

The evidence is consistent across sources and it is **not** primarily technological.

**Documented causes, ranked by weight of evidence:**

1. **Constraint and rule fidelity — the scheduling-specific killer.** The nurse-scheduling
   literature converges on this: real operating rules differ by institution, by ward, and by
   planning horizon, and are largely undocumented. An optimiser built on an incomplete constraint
   set produces schedules that are mathematically optimal and operationally unusable, which
   destroys frontline trust in a single cycle.
   https://link.springer.com/article/10.1007/s10916-014-0160-8

2. **Failure to engage the people who currently do the work.** Kellogg & Walczak name *"the lack
   of early communication with the nurses and those in charge of scheduling"* and *"lack of
   nurse-centered solutions"* as primary causes of the implementation gap. Note that the incumbent
   schedulers are usually the same people whose roles a business case proposes to reduce. That
   conflict is structural, not attitudinal.

3. **Process change not made.** Both Jang et al. (2014) and the NAM framework attribute realised
   return to the organisation's *"ability to leverage [the system] for process changes"*, not to
   deployment. Deployment without process change returns zero.

4. **Attribution and measurement collapse.** Cresswell et al. (2022): benefits emerge *"gradually
   and over long timeframes"*, creating *"problems of attribution of benefits to causes."* In
   practice the programme cannot prove it worked, funding attention moves on, and the benefit is
   never booked.

5. **Resource constraints during delivery.** The most-cited cause of schedule overrun in the
   Panorama 2024 sample — staffing and budget, i.e. the organisation could not free the people it
   needed. [CONSULT]

6. **Unanticipated additional technology.** Most-cited cause of budget overrun in the same sample
   — integration surface discovered during rather than before implementation. [CONSULT]

7. **Frontline resistance where the technology monitors work.** The EVV precedent: perceived as
   *"intrusive"* and as reducing flexibility, contributing to multi-year national delay.
   https://doi.org/10.1016/j.dhjo.2020.100938

8. **Silent non-compliance — the failure mode nobody logs.** This is now the best-quantified item
   on the list, and it comes from outside healthcare. MIT CTL found **three in four deliveries did
   not follow the planned sequence**, rising to four in five in the US, and that deviation was
   *predictable* from route characteristics — systematic behaviour, not noise. Their conclusion:
   routing-tool **"investments are devalued if drivers do not follow the information provided by
   the routing tools."**
   https://medium.com/mitsupplychain/mit-research-learning-from-route-plan-deviations-in-last-mile-delivery-cff1cfa20af6
   Note that this failure mode produces **no error message and no adoption-metric red flag.** The
   system reports that it scheduled the work. Nobody reports that the work was done differently.

9. **Service-time estimation error.** McKinsey's utility work names it directly: scheduled durations
   for short-cycle jobs are *"often several hours more or less than the actual requirement, leading
   to either a schedule backlog or underutilization."* **The limiting factor is the duration
   estimate, not the routing mathematics** — and duration estimates come from the data foundation,
   not the optimiser.

**Note the convergence.** Causes 1, 8 and 9 are the same underlying problem — the model does not
match the world — and they arrive independently from nurse scheduling, last-mile delivery, and
utility field crews. **This is the most robust finding in the document.** In three separate
industries with three separate literatures, what defeats scheduling optimisation is constraint and
duration fidelity, not algorithms and not technology.

**On executive turnover:** it is widely asserted as a failure mode and I could not find a
quantified study isolating its effect on healthcare technology programmes. The adjacent evidence
is Cresswell et al. on benefits materialising over long timeframes — which mechanically means a
programme's payback horizon frequently exceeds the tenure of the executive who sponsored it. The
supporting datapoints are the deployment timelines: **UPS ORION ran 2003–2016**; **HCHB Smart
Scheduling went ~5 years from announcement to any published number**; the **UK shared services
strategy is still undelivered** across multiple NAO reports and successive governments
(https://www.nao.org.uk/reports/update-on-government-shared-services-2026/). That is a structural
inference from timelines, not a measured finding, and should be labelled as such.

**On data quality:** similarly under-measured as an isolated variable. It appears in the evidence
indirectly — Tursunbayeva et al. name *"adequate data preparation"* as a gating action for
benefit realisation, and Panorama names *"understanding data architecture and quality issues"* as
a precondition for staying on budget. No study I found quantifies the share of failures
attributable to data quality specifically.

---

## 4. Administrative headcount reduction from workflow automation

### 4.1 The macro evidence: two decades of healthcare automation did not reduce administrative cost share

This is the cleanest natural experiment available, and the result is unambiguous.

**[IND]** Himmelstein, Campbell & Woolhandler (2020), "Health Care Administrative Costs in the
United States and Canada, 2017", *Annals of Internal Medicine* 172(2).
https://doi.org/10.7326/M19-2818

- Administration accounted for **31% of U.S. health expenditures in 1999**.
- By **2017 it was 34.2%** — $812 billion, $2,497 per capita — versus 17.0% in Canada.
- Hospital administration alone: **$933 per capita** (US) vs $196 (Canada). Nursing home, home
  care and hospice administration: **$255** vs $123.
- Of the 3.2-percentage-point increase since 1999, 2.4 points came from private insurers'
  overhead. **But the provider-side share did not fall either.**
- The authors' own limitation note is important: *"methodological changes probably resulted in an
  underestimate of administrative cost growth since 1999."*

**Frame this correctly.** Between 1999 and 2017 US healthcare absorbed near-universal EHR
adoption, over $30 billion in HITECH incentives (per NAM, 2014), electronic claims submission,
clearinghouses, e-prescribing, and the first two waves of revenue-cycle automation. **The
administrative share of national health expenditure went up by 3.2 points.** Whatever those
technologies did, sector-level administrative displacement was not it.

**[IND]** Himmelstein et al. (2014), "A comparison of hospital administrative costs in eight
nations", *Health Affairs* 33(9). US hospital administrative costs were **25.3% of total hospital
expenditures — "a percentage that is increasing"** — against 19.8% (Netherlands), 15.5% (England),
and lower still in Scotland and Canada. https://doi.org/10.1377/hlthaff.2013.1327

**[IND]** Handlon, Simpson, Leaming & Williams (2025), "Trends in hospital administrative costs",
*Health Affairs Scholar*. Medicare cost report data, 2011–2022, all US short-term acute care
hospitals, plus executive interviews.
https://pmc.ncbi.nlm.nih.gov/articles/PMC12359134/

The key finding is subtle and it matters more than the headline: *"Across all hospital types, A&G
salary costs declined as a share of total expenses while total administrative costs increased,
reflecting a shift toward nonsalary drivers."* Conclusion: *"Rising administrative costs are
primarily driven by systemic and structural demands, rather than salaries."*

**Read that carefully, because it is the single most decision-relevant finding in this section.**
Administrative *salary* share did fall. Total administrative *cost* rose anyway, because the work
migrated to non-salary line items — software, licences, outsourced services, vendors. **The
headcount came down and the cost did not.** A business case that converts an FTE reduction
directly into a cost saving is contradicted by twelve years of Medicare cost report data across
every acute hospital in the country.

### 4.2 The micro evidence: what a well-implemented automation actually saves

The most rigorously measured healthcare automation deployments available right now are ambient AI
scribes. They are the best-case comparator — mature product category, enthusiastic clinicians,
heavy vendor investment, and unusually good measurement. **Their measured effect sizes are an
order of magnitude below what business cases in this space typically promise.**

**[IND]** Preiksaitis, Alvarez, Winkel et al. (2026), "Ambient AI Scribes and Emergency Department
Documentation Burden: Retrospective Cohort Study", *JMIR AI*. 13-month staged rollout, 10,344
encounters, 100 attending physicians, mixed-effects models with physician random intercepts,
negative-control outcomes, and a within-clinician placebo permutation test.
https://doi.org/10.2196/92193

- Ambient AI scribe use was associated with a **72.6-second reduction in on-shift documentation
  time per encounter** (95% CI 63.8–81.4; P<.001).
- *"equivalent to approximately 24 minutes per 8-hour shift if used across 20 encounters"* — i.e.
  **about 5% of a shift.**
- After-shift documentation time **increased** modestly, by 9.1 seconds (P=.004).
- Cohort mean use rate: **18.2%.**

**[IND]** Kashiouris, Miner, Saleh et al. (2026), "The Effect of Ambient AI Documentation on
Clinician Workload, Efficiency, and Patient Experience in a Multisite Emergency Department
Network", *Applied Clinical Informatics*. Retrospective cohort, **14 EDs, 315,242 notes**, May
2024–June 2025, voluntary adoption. https://doi.org/10.1055/a-2939-3038

Three findings that should be read together, because the combination is the lesson:

1. **Adoption: *"Ambient AI was used in 8.6% of 315,242 ED clinical notes."*** Across 14 sites and
   13 months of voluntary rollout of a heavily promoted tool, fewer than one note in eleven used
   it.
2. **Measured task time: no change.** *"Within-clinician paired analysis showed no difference in
   active editing time between AI and conventional notes (median difference +0.17 min; 95% CI,
   −1.00 to +1.55; p = 0.349)."*
3. **Perceived burden: enormous improvement.** *"NASA-TLX workload decreased by 40.2 points (95% CI
   30.4–50.1)."*

> **This is the most important calibration in the document.** A technology that clinicians
> experienced as a dramatic reduction in burden produced **no measurable change in the time the
> task took.** Real benefits existed — earlier note completion (3.4h earlier for admitted, 6.0h
> for discharged), half as much copied-forward content (9.4% vs 18.3%), better patient-reported
> listening — but they were not the benefit a business case would have been written on. Ask users
> whether it helped and you get +40 points. Measure the clock and you get zero.
> **Satisfaction surveys will not tell you whether capacity improved.**

The authors also note the deployment *"introduc[es] new responsibilities for clinicians to review,
edit, and sign machine-generated notes"* — automation adding work at the same time as it removes
work, which is the standard pattern and is almost never in the business case.

### 4.3 RPA applied directly to nurse scheduling — the closest controlled analogue

**[IND]** Jung, Seo, Hong & Doo (2026), "Development of a nurse scheduling program using robotic
process automation in Korea", *Health Informatics Journal*. **102 nurses in a 500-bed hospital,
assigned to experimental or control group** — one of the very few controlled evaluations of
scheduling automation in existence.
https://doi.org/10.1177/14604582251414581

- RPA-based scheduling **significantly improved nurses' work-life balance.**
- **"No significant differences were found in health status or work characteristics."**

**The pattern is identical to the ambient-AI finding.** The experiential and fairness outcomes
moved; the work characteristics did not. This is the most directly relevant controlled study to a
scheduling-automation business case, and its operational result is null.

### 4.4 Healthcare non-clinical headcount rose *during* the EHR build-out

**[IND]** Gottlieb, Mahoney, Rinz & Udalova (October 2025), *The Rise of Healthcare Jobs*, NBER
Working Paper 33583. Census internal Decennial/ACS microdata, 1980–2022.
https://www.gottlieb.ca/papers/HealthCareJobs.pdf | https://www.nber.org/papers/w33583

Non-clinical occupations — all healthcare-industry employees not in a clinical occupation:

| 1980 | 2000 | 2010 | 2022 | Δ 2010–22 |
|---|---|---|---|---|
| 2,820k | 4,415k | 5,547k | **6,237k** | **+12.4%** |

Set against hospital EHR adoption rising from **9% in 2008 to roughly 96–99% by 2018–2021**
(ONC/ASTP; https://healthit.gov/data/quickstats/national-trends-hospital-and-physician-adoption-electronic-health-records/).

**The largest workflow-digitisation programme in US healthcare history coincided with a 12.4%
increase in non-clinical headcount.** This is the single most load-bearing number available for
the outside view on administrative displacement.

**[IND]** Shrank, Rogstad & Parekh (2019), "Waste in the US Health Care System", *JAMA*, 7 October
2019. https://pubmed.ncbi.nlm.nih.gov/31589283/ — Administrative complexity is the **largest** of
six waste domains at **$265.6B/yr**, and potential savings from interventions is listed as **"Not
applicable"**: *"No studies were identified that focused on interventions targeting administrative
complexity."*
*Flag: this quotation was obtained via a secondary summary because the JAMA PDF would not
text-extract. Verify against the original before printing.*

**[IND]** Bessen, Goos, Salomons & van den Berge (2025), "What Happens to Workers at Firms that
Automate?", *Review of Economics and Statistics* 107(1):125–141. Dutch administrative micro-data,
all private non-financial firms, with a direct measure of automation spend.
https://doi.org/10.1162/rest_a_01284
Workers at automating firms suffer a **5-year cumulative wage-income loss of 9% of one year's
earnings**, driven by reduced days worked. **Displacement is gradual and modest — it accumulates
over five years rather than arriving as a step change at go-live.**

**[IND]** Time-to-realisation. Brynjolfsson & Hitt (2003), *Review of Economics and Statistics*
85(4): the productivity contributions of computerisation are **up to 5× greater over 5–7 year
differences than over 1-year differences.**
https://ideas.repec.org/a/tpr/restat/v85y2003i4p793-808.html
Brynjolfsson, Rock & Syverson, "The Productivity J-Curve" (NBER WP 25148): general-purpose
technologies require large, poorly-measured **intangible complementary investment**; measured
productivity is understated early and overstated later.
https://www.nber.org/papers/w25148

### 4.5 RPA and AI programmes: what the surveys actually show

**[CONSULT]** Deloitte Global RPA Survey 2018 (530 leaders, $3.5T combined revenue): **only 4% of
organisations operated more than 50 robots — "a negligible increase from 3% in 2017."** 67% had
begun implementing an RPA strategy.
https://legaltechnology.com/deloitte-rpa-report-admits-surprise-at-lack-of-vision-and-it-readiness/
**This is the canonical "stalls at small scale" finding.** Adoption is broad; scale is almost
nonexistent.

**[CONSULT]** Deloitte, *Automation with intelligence*, 30 June 2022.
https://www.deloitte.com/us/en/insights/topics/talent/intelligent-automation-2022-survey-results.html
- Implementers/scalers report average **32% cost reduction** (vs 31% expected) — **in scope**, not
  organisation-wide
- Average payback **22 months, up from 16 months in 2020** — getting worse, not better
- **">50% have never calculated actual cost reduction and 70% have never calculated revenue
  impact."**

That last line is the finding. **Most "realised savings" claims in this space are unaudited.**

**[CONSULT]** Gartner, reported via *Fortune*, 11 May 2026: of organisations that piloted
AI/autonomous technology, **80% reported workforce reductions — but there was no correlation
between those reductions and ROI.** Reduction rates were nearly equal for high-ROI firms and for
firms with small, zero, or negative returns.
https://fortune.com/2026/05/11/ai-automation-layoffs-gartner-study-roi/

> **Read that carefully. Headcount cuts in this space are largely *decoupled* from realised
> automation benefit.** A business case that derives headcount reduction from automation benefit
> is misspecified in both directions: organisations cut without the benefit, and realise benefit
> without cutting.

**[CONSULT]** MIT NANDA, *The GenAI Divide: State of AI in Business 2025* (July 2025): **95% of
GenAI initiatives produce no measurable P&L return**; only 5% of custom tools survive
pilot-to-production. *Note: the report contains no headcount or layoff data at all — anyone citing
it for workforce effects is over-reading it.*

**[IND]** Current labour-market checks. Yale Budget Lab (2025), 33 months post-ChatGPT: *"the
broader labor market has not experienced a discernible disruption."*
https://budgetlab.yale.edu/research/evaluating-impact-ai-labor-market-current-state-affairs
Challenger, Gray & Christmas, 6 August 2026: 477,033 US cuts YTD 2026, ~24% attributed to AI — and
**"There is only one Health Care cut attributed to AI in Challenger's data: 39 cuts at a California
telehealth provider in October 2025."**
https://www.challengergray.com/blog/challenger-report-layoffs-fall-hiring-picks-up-ai-leads-for-fifth-straight-month/

**[IND]** Administrative automation adoption moves in single-digit points per year. 2025 CAQH Index
(~600 organisations, 63% of insured lives): fully-electronic medical prior authorisation reached
**40%, up from 31% in the 2023 Index**, with most other transactions plateaued and a remaining
savings opportunity of **$18.7B — up 2% year on year, i.e. the opportunity is not shrinking.** That
is roughly thirty years after HIPAA mandated the standards.
*Flag: figures seen via secondary reporting; AJMC blocks automated fetch.*

### 4.6 Redistribution versus elimination — the flagship case

**[IND-authored]** Lacity, Willcocks & Craig (April 2015), "Robotic Process Automation at Telefónica
O2", LSE Outsourcing Unit Working Research Paper 15/02 — the most-cited RPA success in existence.
**Retrieved and read in full.**
https://researchonline.lse.ac.uk/id/eprint/64516/
PDF: https://researchonline.lse.ac.uk/id/eprint/64516/1/OUWRPS_15_02_published.pdf

Table 1, verbatim: 15 core processes automated; 400,000–500,000 RPA transactions per month; >160
robots; **"Number of FTEs saved or redeployed: Hundreds"**; payback period 12 months; 3-year ROI
650–800%. Roughly **35% of all back-office transactions** automated by Q1 2015.

**The load-bearing sentence, verbatim from the paper:**

> *"How many FTEs did automation save? It is difficult to assess the total FTE savings over time
> because some of Telefónica O2's UK-based people were redeployed to other service areas and the
> business continued to grow. But the estimated FTE savings are in the hundreds."*

**Three things follow, and they matter more than the ROI headline.**

1. **The single most celebrated RPA case in the world cannot separate elimination from
   redeployment in its own accounting** — and says so explicitly. Its own summary table collapses
   the two into one cell: *"saved or redeployed."*
2. **Where headcount did measurably fall, it fell at the outsourced provider, not the client.** The
   paper records the Indian BPO provider's FTEs on automated processes *"had been reduced... by a
   few hundred"*, with ~250 FTEs remaining on non-automated back-office work — against a stated
   counterfactual of *"closer to 500 because of Telefónica O2's growth since 2010."*
3. **Growth absorbed much of the saving.** The comparison that produces the impressive number is
   against a counterfactual headcount, not against the starting headcount.

*Correction note: a widely-repeated secondary summary of this case states "no internal layoffs;
FTEs redeployed or managed through natural attrition." That phrasing does not appear in the paper
and should not be cited. The paper's actual position is that the split is indeterminate. This
document reports what the primary source says.*

**The transferable lesson is not "automation never cuts headcount."** It is that **the flagship
case in the entire field could not measure the split, and neither will you, unless you instrument
it deliberately before you start.**

**[IND]** UK government shared services — the cleanest promised-versus-delivered back-office record
available. National Audit Office: two shared service centres delivered **£90m of savings against
£94m of costs** in their first 2.5 years — a net loss. Departments were **unable to deliver** the
£172m–£272m/yr of further back-office efficiencies the strategy assumed.
https://www.nao.org.uk/reports/shared-service-centres/
NAO update, 6 March 2026: the strategy *"will not be delivered to time or budget"* without urgent
action; five cloud shared-service centres targeted for 2028 remain delayed.
https://www.nao.org.uk/reports/update-on-government-shared-services-2026/

**Watch the arithmetic mechanism in vendor claims.** A typical revenue-cycle case reports "5,559
hours saved = the status work of nearly 14 FTEs." That is **14 FTEs of task time on one workflow**,
not 14 positions eliminated. The conversion from task-hours to positions is where business cases
routinely break, and it is almost never shown.

### 4.7 What this implies for a claimed two-thirds back-office reduction

| Claim type | What the evidence shows |
|---|---|
| Sector-level admin displacement from two decades of health IT | None; admin share of NHE rose 31% → 34.2% (1999–2017) |
| Healthcare non-clinical headcount, 2010–2022 | **+12.4%**, while EHR adoption went 9% → ~99% |
| Admin salary share vs total admin cost | Salary share fell, total cost rose — work moved to non-salary lines |
| Best-measured modern automation, time saved | ~5% of a shift (72.6 sec/encounter) |
| Same technology, multisite, measured task time | No change (p = 0.349) |
| Voluntary adoption, well-marketed tool, 14 sites, 13 months | 8.6% of notes |
| Controlled RPA nurse scheduling | Work-life balance improved; work characteristics unchanged |
| RPA programmes operating >50 robots | 4% (2018), up from 3% (2017) |
| RPA adopters who never measured actual cost reduction | >50% |
| Flagship RPA case (Telefónica O2): elimination vs redeployment split | **Indeterminate — the paper cannot separate them** |
| AI pilots with workforce reductions, correlation with ROI | 80% cut; **no correlation** with return |
| Healthcare layoffs attributed to AI, US, YTD 2026 | **One event, 39 people** |

**A ~65% back-office headcount reduction has no support anywhere in this evidence base.** A
targeted search for any organisation that publicly claimed a ~60–70% back-office cut from
automation, and for any follow-up on what happened, returned **zero hits in either direction** —
neither a documented success nor a documented failure. **The claim sits outside the observed
distribution.**

The three mechanisms the evidence actually documents:

1. **Redistribution rather than elimination — by default, and usually unmeasured.** The flagship
   case produced FTE savings "in the hundreds" and could not say how many were eliminated versus
   redeployed. Work also migrates to non-salary line items (Handlon 2025), to outsourced providers
   (Telefónica O2), and into new tasks the automation itself creates (Kashiouris 2026).
2. **Adoption throttling the ceiling.** At 8.6% adoption, even a genuine 100% task-level saving
   yields an 8.6% organisational saving. **Adoption rate, not effect size, is usually the binding
   constraint** — and it is the variable business cases assume rather than forecast.
3. **The denominator does not hold still.** Healthcare administrative work is generated by payer
   complexity, not by the absence of software. Prior authorisation moved 31% → 40% electronic in
   two years, three decades after the standards were mandated.

**A defensible time-phased forecast for a healthcare back-office automation programme:**

| Horizon | Realistic outcome |
|---|---|
| **0–12 months** | ~0% net headcount effect. Deloitte's average payback is 22 months and rising. Complementary intangible investment — process redesign, exception handling, governance — dominates year one. This is the J-curve trough. |
| **12–24 months** | Task-hours removed **within the automated workflows**: 20–35% is the defensible band. Net headcount effect typically **0–5%**, realised through hiring avoidance and attrition rather than separations. |
| **24–60 months** | **5–15% net back-office FTE reduction** for a well-run programme, concentrated in vacancy non-backfill. Bessen et al. find automation's worker effect accumulates over five years and is modest even then. |

**Treat a claimed 65% reduction as roughly 4–6× the realised 90th-percentile outcome.** Centre the
forecast on ~10% net FTE reduction by year 3 and 15–20% by year 5 — and attach a meaningful
probability (call it 50%) that measured net back-office headcount is **flat or higher** at year 3
because of volume growth, payer-complexity growth, and new exception-handling and AI-oversight
roles.

*Evidence limitations, stated plainly: (a) no study directly tracks back-office FTEs before and
after a healthcare workflow-automation programme with a control group; (b) no peer-reviewed study
quantifies the redeployment-versus-elimination split — the only quantified statements are the O2
case at 0% eliminated and consultancy framing of "reduction and redeployment"; (c) the widely
cited "30–50% of initial RPA projects fail" attributed to EY could not be traced to a primary
publication and should not be printed as an EY-sourced fact. **The redeployment split is the
thinnest area of this entire evidence base.***



## 5. Home-health-specific technology outcomes

**This section contains the most important finding in the document, and it is a negative one.**

After systematic search of the peer-reviewed literature, government sources, KLAS, and every
named vendor: **there is not one randomised, quasi-experimental, or peer-reviewed evaluation of
any home health scheduling or routing optimisation product.** Not Homecare Homebase Smart
Scheduling, not WellSky, not Axxess, not MatrixCare. The evidence base does not exist.

Everything below is organised around that fact.

### 5.1 Independent evidence — what actually moved home health productivity

The only rigorously measured change in home health visit productivity in the last decade came
from **payment policy, not software** — and it moved in the opposite direction to a
capacity-expansion thesis.

**[IND]** MedPAC, "Mandated report: The impact of recent changes to the home health prospective
payment system", presented 15 January 2026 (Acumen analysis; interrupted time-series regression,
2016–2023, pre-2020 trend as counterfactual).
https://www.medpac.gov/wp-content/uploads/2025/08/Tab-J-HH-mandate-Jan-2026.pdf

- Visits per FFS home health stay: **19.6 (2016) → 19.4 (2019) → 16.0 (2022) → 15.9 (2023)**
- PDGM associated with **−2.9 visits per stay (−15.3%)** in 2023. Therapy −2.4 visits (−21.3%);
  skilled nursing −0.7 (−9.8%); home health aide +0.2.
- *"Difference in FFS Medicare margin associated with PDGM was not statistically significant
  overall."* Freestanding HHA FFS Medicare margin was **21.2% in 2024.**
- MedPAC's own caution: *"Fewer visits per stay for services with new incentives under PDGM
  (therapy) and those with no direct changes (skilled nursing) suggest influence of factors other
  than PDGM."*

**[IND]** MedPAC March 2025 Report to Congress, Chapter 7.
https://www.medpac.gov/wp-content/uploads/2025/03/Mar25_Ch7_MedPAC_Report_To_Congress_SEC.pdf

- Total in-person visits per full 30-day period: **10.2 (2019) → 8.5 (2023)**, cumulative −16.7%.
- Medicare payment per in-person visit rose **$180 (2019) → $237 (2023)**, +7.2%/yr, while total
  in-person visits to FFS beneficiaries *"declined by 9.7 percent per year, on average."*
- Freestanding FFS Medicare margin **20.2% (2023)**, projected **19% for 2025**, averaging 17.1%
  over 2001–2022. 12,057 participating HHAs in 2023.

**Read that combination carefully.** Sector-wide, visits per episode fell, revenue per visit rose,
and margins stayed near 20%. Agencies became *more* profitable while delivering *fewer* visits.
Any business case premised on "more visits per clinician per day equals more margin" is arguing
against the observed direction of the entire sector.

### 5.2 The ceiling on technology-mediated change in this sector

**[IND]** Same MedPAC chapter, p.235. In 2023 — the first year of reporting — **1.2% of 30-day
periods included a telehealth visit or remote patient monitoring, and about 14% of HHAs provided
at least one.** MedPAC's conclusion: *"most clinical care in the home health benefit is still
provided in person."*

This is the hardest available ceiling on tech-mediated capacity change in home health. The
digital penetration of the benefit is close to zero.

### 5.3 Independent product-quality signal: KLAS

**[IND]** Best in KLAS 2026, Home Health & Hospice.
https://klasresearch.com/best-in-klas-ranking/home-health-hospice/2026/232

- Homecare: Home Health winner — **MatrixCare Home Health, 78.5**
- Hospice winner — MatrixCare Hospice, 80.0
- Personal Care Services & Private Duty Nursing winner — AxisCare, 81.9

Calibration matters here. On the same 0–100 scale, the acute-care EHR winner is **Epic at 89.7**,
and services categories reach 99.0. **The best-rated home health EMR in the market scores roughly
11 points below the best-rated acute EHR.** Satisfaction with home health tooling is structurally
lower than the rest of health IT — which is a statement about the difficulty of the domain, not
about any one vendor.

*Note: no public KLAS score exists for Homecare Homebase, WellSky Home Health, or Axxess. Only
category winners are published; full segment tables are paywalled.*

### 5.4 Vendor claims — and what is wrong with each of them

**Every vendor case study located has n=1, no control group, and no adjustment for secular
trend.** Several measure across the 2020–21 COVID trough-and-rebound, which alone can generate the
entire reported effect. They are listed here so the business case can cite them accurately as
marketing, not evidence.

**[VENDOR] Homecare Homebase — Smart Scheduling.** PRWeb, 13 June 2024: *"over 2.2 million visits
successfully scheduled through Smart Scheduling"*; Amedisys *"has experienced greater than 40%
automation in scheduling workflow"*; *"up to 70% of visits are now scheduled via Smart
Scheduling."*
https://www.prweb.com/releases/homecare-homebase-smart-scheduling-enhances-efficiency-and-continuity-of-care-setting-new-industry-standards-302171671.html
Product page (undated): *"automate up to 95% of visit types and 64% of workflow tasks"*; *"up to
22 days of future-visit automation."* Benefit language is entirely unquantified — *"reduced drive
time and burnout," "better balanced utilization," "lowering labor and mileage costs."*

> **The critical observation: every published HCHB metric is an *input* metric — the share of
> visits auto-scheduled, the share of tasks automated. Not one is an outcome metric.** There is no
> visits-per-clinician-per-day figure, no mileage figure, no cost figure. The market leader, at
> its largest customer, markets automation rate as if it were benefit.

**Timeline datapoint, and it is the most forecast-relevant fact in this section:** Smart
Scheduling was announced **July 2019** with a Q1 2020 rollout target.
https://rehabpub.com/clinic-management/software/homecare-homebases-new-smart-scheduling-features-excel-health-data/
The first published usage numbers appeared **June 2024** — a **~5-year gap from announcement to
any quantified result, at the largest customer in the sector.**

Third-party user aggregation (IntuitionLabs): **3.7/5.0 from 25 reviews**, recurring complaints of
*"High implementation and ongoing costs," "Steep learning curve," "back-office interface is not
intuitive," "system freezing or being slow."*

**[VENDOR] WellSky — CareInsights.** Business Wire, 6 June 2023: WellSky's own three-year study of
its own customers found agencies experienced **12% lower risk-adjusted 60-day hospitalisation
rates**; *"consistent and ubiquitous"* users saw rates **26% lower than non-users**.
https://www.businesswire.com/news/home/20230606005152/en/
*Conducted by the vendor, not peer reviewed. The 26% figure compares self-selected heavy users to
non-users — textbook selection bias.*

Patriot Homecare case study (WellSky PDF): Q2 2020 → Q2 2021, quarterly hospitalisation 18.89% →
15.31%; median visits per patient episode **14 → 12**, described as *"a utilization improvement of
14.29%"*; census 485 → 611 (+25.98%).
https://www.patriotathome.org/wp-content/uploads/2023/02/PATRIOT-CASE-STUDY-WELLSKY.pdf
*n=1 agency, no control, and the window runs from the pandemic trough to the rebound. The same
document states Patriot "saw their census drop by over 100 patients" during COVID — so the +26%
census "result" is largely recovery, not effect.*

> **Note the direction of WellSky's headline efficiency metric: fewer visits per episode. The
> marketed win is doing less, not serving more.** That is the opposite of a capacity-expansion
> thesis, and it is being sold by the largest vendor in the space.

Other WellSky claims, all n=1 or unspecified, no control: LTM Group 32.8% reduction in monthly
hospitalisation rate (Business Wire, 17 Jan 2024); Bayou Home Care rehospitalisations down 27%
over three months at one branch. The Concierge Home Care case study (~1,200 patients) **contains
zero numbers** — it is entirely testimonial, which is representative of the genre.

**[VENDOR] Axxess.** UEW Healthcare (axxess.com blog, 4 March 2026): census grew *"about 15%"*;
paper documentation fell from *"more than 37% of our caregivers"* to *"only 11%"*; *"Our weekly
billing of claims has quadrupled."* n=1, no control, no stated baseline period. Axxess CARE
marketing: *"one client doubled revenue in just six months"* — no agency named, no methodology.

**[VENDOR] Forcura.** Munson Home Health success story (PDF created 2022-09-08): *"an average of
30 minutes per referral."*
https://www.forcura.com/hubfs/Resources/Munson%20Healthcare%20Success%20Story.pdf
*Critical flaw: no before number appears anywhere in the document. The headline metric has no
baseline, so no improvement can be computed from it.* Corporate claim of *"at least a 60 percent
reduction on time spent"* on document handling is undated, unsourced, no n.

**[VENDOR] Trella Health.** *"average 46.9% increase in monthly referral volume"*; CRM *"can cut
rep calendar administration by 47%"* and *"give each rep 1 to 1.5 hours back every week."*
Undated. No methodology, sample, period, or comparison group disclosed for any of the three.

**[VENDOR] Medalogix (now rebranded Mosai).** Muse: *"97 percent average accuracy"* predicting
death within 7–12 days. A June 2018 claim that *"Vanderbilt University Medical Center's Health
Economists peer-reviewed Medalogix's models and found them to be more accurate than CMS's publicly
available risk adjustment models"* — **no journal, authors, year, or citation could be located.**
"Peer-reviewed" here appears to mean "reviewed by academics under contract," not published peer
review. Medalogix Touch: rehospitalisation 20.1% → 13.6%, single case study, no n, no control.
*Note: medalogix.com now redirects to mosai.com and the vendor's own "Research-Backed Performance"
page currently 404s.*

**[VENDOR] MatrixCare (ResMed).** Multi-year Best in KLAS winner — that part is independently
confirmed. But its published case-study outcomes are **not home health**: the DRUID AI *"96% case
identification accuracy"* is a customer-support chatbot, and the *"100% on-time submission"* +
*"12% increase in case mix index"* result is a **skilled nursing facility**. **No quantified
MatrixCare home-health scheduling or productivity outcome was found.**

### 5.5 The EVV precedent, quantified

**[IND]** CBO estimated **$290 million in savings over 10 years** from EVV implementation (cited
in MACPAC, February 2019).
https://www.macpac.gov/wp-content/uploads/2019/02/Electronic-Visit-Verification-for-Personal-Care-Services-Status-of-State-Implementation.pdf
Problem baseline (OIG 2010): roughly 1 in 5 PCS claims undocumented, $63 million in undocumented
Medicaid PCS claims that year.

**No realized-savings follow-up has ever been published.** Post-mandate, HHS OIG (2026) found
**$8.0M in overpayments** in Colorado and that *"Colorado implemented an EVV system but did not
verify that all PCS visits were recorded and verified in that system."*
https://oig.hhs.gov/reports/all/2026/colorado-could-improve-its-electronic-visit-verification-system-and-claimed-federal-medicaid-reimbursement-for-millions-of-dollars-in-personal-care-services-that-did-not-comply-with-federal-and-state-requirements/

**Deployment ≠ realized control.** A mandated, funded, universal system was deployed and the
control it existed to provide was still not achieved.

### 5.6 What could not be found — the gaps *are* the finding

1. **Zero peer-reviewed or quasi-experimental evaluations** of any home health scheduling/routing
   product. The academic HHCRSP literature is OR modelling — simulated objective functions, not
   realized agency outcomes.
2. **No published visits-per-clinician-per-day figure attributable to any vendor product**, from
   any source. The only credible visits numbers in existence are CMS/MedPAC claims-derived, and
   they are per-episode, not per-clinician-per-day.
3. **No drive-time or mileage reduction figure with a baseline.** HCHB markets "reduced drive time"
   and "lowering mileage costs" and has never published a number for either.
4. **No realized-vs-projected comparison** for any home health technology deployment, from any
   party. The nearest analogue is the CBO EVV projection, never followed up.
5. **No documented failed or abandoned home-health scheduling implementation.** This is almost
   certainly publication bias, not absence of failures — vendors don't publish them, and the two
   trade outlets (Home Health Care News, McKnight's Home Care) carry substantial vendor-sponsored
   content. **Treat the failure rate in this sector as unmeasured, not low.**

### 5.7 What this section implies for planning

Against this reference class, assume:

- **~5 years** from product announcement to any published outcome number, even at the largest
  customer in the sector.
- **No independent evidence base will exist** to validate your results against, during or after.
- **The benefit that actually gets measured will be an automation-rate metric, not a
  visits-per-day metric** — because that is what every vendor and every customer in this sector
  has measured so far.

That last point is the trap. It is entirely possible to hit "70% of visits auto-scheduled" and
have no idea whether capacity improved.



## 6. Field-service optimisation outside healthcare

This is where the measurement is best, and it is the most useful calibration available for a
home-health scheduling business case — home health visit routing is structurally the same problem
as field-service dispatch.

**Headline: credible independent evidence clusters at 5–20% travel/distance reduction and roughly
4–15% productivity gain. Vendors claim 20–40%. Almost every large number in this space is either a
modelled improvement never measured after deployment, or a self-reported adopter survey.**

### 6.1 Independent and peer-reviewed evidence

**[IND]** The canonical academic estimate for routing software is **5–20%** reduction in
transportation costs — Toth & Vigo, *The Vehicle Routing Problem* (SIAM, 2002). *Verified through
secondary citation rather than the book itself*, e.g. Gonzalez-Feliu (2008), which restates it as
*"savings ranging from 5% to as much as 20% of the total costs."*
https://shs.hal.science/halshs-00879447/document

**[IND]** Weigel & Cao (1999), "Applying GIS and OR Techniques to Solve Sears
Technician-Dispatching and Home-Delivery Problems", *Interfaces* 29(1):112–130. Result: **>$9
million one-time and >$42 million annual savings.**
https://ideas.repec.org/a/inm/orinte/v29y1999i1p112-130.html
*Note what is absent: dollars only. No percentage, no miles per technician, no jobs per day. This
is the pattern throughout the applied OR literature.*

**[IND]** Blakeley et al. (2003), "Optimizing Periodic Maintenance Operations for Schindler
Elevator Corporation", *Interfaces* 33(1):67–79. Periodic-VRP optimisation across "thousands of
technicians": **"saves over $1 million annually."**
https://ideas.repec.org/a/inm/orinte/v33y2003i1p67-79.html
*Against a service business of that scale, that is a strikingly small realised benefit — well
below how such deployments are typically framed.*

**[IND, UNVERIFIED AT SOURCE]** "Dynamic Workforce Scheduling for British Telecommunications plc",
*Interfaces* 30(1), 2000. https://pubsonline.informs.org/doi/10.1287/inte.30.1.45.11615
Reported: the deployed Dynamic Scheduler improved **productivity by 4% nationwide** across ~20,000
engineers, with manual allocation dropping 40% in the first field trial.

> ⚠️ **This figure could not be verified at source — INFORMS returns 403 to automated requests, and
> the 4% comes from search-result snippets. Obtain the paper before relying on it.** If it holds,
> it is the most important number in this section: a flagship, national-scale telecom
> technician-scheduling deployment delivering **4%** productivity, against vendors selling 20–40%.

**[IND]** Ramos, Lopes & Rocha (2026), *European Transport Research Review* 18:37, on the Amazon
Last-Mile Routing Research Challenge (6,100 historical routes, 3,000+ driver traces, with MIT CTL).
https://link.springer.com/article/10.1186/s12544-026-00795-4
Verbatim: *"there is still a significant gap between the current body of knowledge in theoretical
route planning and real-world route execution"* — because route quality *"is not defined solely by
its duration or cost, but by a multitude of additional factors related to geography,
infrastructure, and customers that are hard or impossible to address with classical optimization
methods."*

**The entire challenge exists because the optimiser's answer was not the answer drivers executed.**

**[IND, but ex-ante]** Waste collection is a literature of simulations, not deployments. Reported
figures — 36.8% distance reduction; *"up to 20%"* (Mexico, *Journal of the Air & Waste Management
Association*, 2021, https://www.tandfonline.com/doi/full/10.1080/10962247.2021.1957040); 23.47%;
25% fuel; 33% fewer routes — are all GIS/model-computed **before** deployment. **No peer-reviewed
study measuring actual fleet miles a year after go-live was found.** Treat the 20–37%
waste-collection band as theoretical optimum, not realised benefit.

### 6.2 Company self-reported results

**[SELF] UPS ORION.** All figures UPS-published; INFORMS' write-up carries them without independent
verification. https://www.informs.org/Impact/O.R.-Analytics-Success-Stories/Optimizing-Delivery-Routes

- ~**100 million miles/yr** and 10 million gallons of fuel avoided at full deployment (2016)
- **$320M+ saved as of December 2015**; $300–400M/yr at full deployment; project cost **$250M**
- 35,000 of 55,000 US drivers deployed by December 2015; average 160 stops/driver/day
- **6–8 fewer miles per route per day** — roughly **8–10%** on a typical route, squarely inside
  Toth & Vigo's 5–20%.
  https://www.bsr.org/en/case-studies/center-for-technology-and-sustainability-orion-technology-ups
- **"Dynamic ORION" (2021) added only 2–4 more miles per driver** — sharply diminishing returns on
  the second optimisation wave.

**Two things to take from ORION.** First, the biggest, best-resourced, most-celebrated route
optimisation deployment in the world landed at **8–10%**, not 30%. Second, it ran from **2003 to
2016** to reach full US deployment — thirteen years.

**[SELF]** DHL Supply Chain (2023 Edelman finalist): routing *"saving more than $98.6 million/year."*
Walmart (2023 Edelman winner): **$75M** in FY2023. Both self-reported inside Edelman submissions;
percentages not disclosed.

### 6.3 Vendor marketing claims, for contrast

**The tell is that the two most established routing vendors claim ~10%, while smaller vendors claim
20–49%.**

| Source | Claim |
|---|---|
| Descartes | *"Reduce **planned** miles by 10%"* — note *planned*, not driven |
| Verizon Connect | *"reduce average mileage by 10%"* |
| Solvice | drive time 20–40% |
| Abelian (Salesforce partner) | *"up to 30% reduction in travel time"* |
| ServiceMax/PTC | *"increase technician utilization by 20%"* |
| IFS | *"up to 20%"* via AI-driven scheduling |
| OverIT | *"25% improvement of first-time-fix rates"* |
| AEX Inc | *"15–25% increases in jobs completed per day, 20–30% reductions in drive time"* |
| Upper | *"28% more stops per day"* |
| PestRouting | *"23% fewer miles per stop. 49% more production per work day"* |

**[CONSULT, vendor-underwritten]** Aberdeen Group, "Service on Time, All the Time", May 2007.
n>175 firms including ABB, Orange, Telstra, Xerox. Adopters **self-reported** 25% improvement in
meeting SLAs, 18% in first-call resolution, **21% decrease in daily miles travelled per
technician**, 24% service cost reduction.
https://www.globenewswire.com/fr/news-release/2007/05/03/993359/0/en/Schedule-and-Route-Optimization-Solutions-Improve-Field-Technician-Productivity-by-25.html
*Caveats: adopter self-report, survivorship-biased, and the report was underwritten by
ClickSoftware, Servigistics, Oracle-SPL, Ventyx and Astea — the vendors selling the product.*

**[CONSULT]** McKinsey, "Smart scheduling for utilities", 25 January 2023. Six-week electric-utility
pilot; headline 20–30% field productivity increase.
https://www.mckinsey.com/industries/electric-power-and-natural-gas/our-insights/smart-scheduling-for-utilities-a-fast-solution-for-todays-priorities

**This source contains the realised-versus-modelled gap in a single sentence.** Crews at one site
were *measured* at **44% of time actually working on jobs**. Under the optimised schedules, crews
**"could expect to spend 65 percent."** That is an expectation derived from the schedule, not a
measurement of execution — and the 20–30% headline rests on it.

### 6.4 The adoption gap: do people actually follow optimised routes?

This is the best-evidenced part of section 6 and the most transferable to home health.

**[IND]** Li & Phillips, MIT Center for Transportation & Logistics, April 2019. One year of delivery
data from a large soft-drinks company across Mexico and the US.
https://medium.com/mitsupplychain/mit-research-learning-from-route-plan-deviations-in-last-mile-delivery-cff1cfa20af6
Thesis: https://dspace.mit.edu/handle/1721.1/118135

- **"Three out of four deliveries did not follow the planned sequence."**
- **~50% of routes deviated in Mexico; 4 out of 5 (80%) deviated in the US.**
- Deviation was *predictable* from route characteristics (71% accuracy in Mexico, 84% in the US) —
  it is systematic behaviour, not noise.
- Their conclusion is the money quote: routing-tool **"investments are devalued if drivers do not
  follow the information provided by the routing tools."**

**[SELF]** UPS's own account of the same problem. BSR's ORION case study records UPS's *"most
significant change-management challenge: many people didn't believe that a computer-generated
algorithm could be an improvement over decades of driver experience"*, and that ORION *"may
recommend route scenarios that, while more efficient, are highly counter-intuitive for a driver."*
UPS's OR group reported that initial algorithms were *"successful in laboratory settings [but] not
easy to implement in practice."*

**On constraint fidelity.** McKinsey names the mechanism directly for utilities: scheduled durations
for short-cycle jobs are *"often several hours more or less than the actual requirement, leading to
either a schedule backlog or underutilization."* **Service-time estimation error, not routing
mathematics, is the limiting factor.** The documented reasons drivers deviate — parking, road
conditions, tolls, narrow streets, familiar sequences, live traffic apps — are precisely the
constraints absent from the optimiser's model.

**This is the same failure mode section 1 identified in nurse scheduling, arriving independently
from a different industry.** Constraint fidelity is the binding constraint in both.

### 6.5 Credible realised ranges

| Metric | Credible realised range | Confidence |
|---|---|---|
| Travel distance / mileage per worker | **5–15%** (ORION ≈8–10%; Toth & Vigo 5–20%; both mature vendors claim 10%) | Moderate–high |
| Travel time | **10–20%**, and only where traffic data is good | Moderate |
| Productivity / jobs per worker per day | **4–15%** — BT's 4% at national scale is the floor | **Low** — no peer-reviewed before/after measurement exists |
| Utilisation / wrench time | **+5–10 percentage points** (e.g. 44%→50–54%, not 44%→65%) | Low–moderate |
| First-time fix rate | **+3–8 points**, and largely *not* attributable to scheduling — it is parts, skills and diagnosis | Low |
| Overtime reduction | **No credible independent evidence found.** Treat all overtime claims as unsupported | — |
| Second-wave optimisation | Sharply diminishing: ORION's dynamic upgrade added only 2–4 miles on top of 6–8 | Moderate |

**Two rules that fall out of this.**

**The discount rule: divide any vendor number by 2–3.** Vendor 20–40% becomes realised 7–15%.

**The execution haircut: apply a second discount for adoption.** If 50–80% of routes are overridden
in practice, the plan's modelled saving is an upper bound the operation may capture only partly.
Modelled benefit × adoption rate × compliance rate is the honest formula, and only the first term
usually appears in a business case.

### 6.6 What could not be found

1. **Any peer-reviewed, measured before/after study of jobs or visits per worker per day** following
   a field-service or routing deployment. **This absence is itself a finding.**
2. Independent evidence on **overtime reduction** — everything located was vendor copy.
3. The **BT 4% figure at source** (INFORMS 403-blocked). Flagged unverified above.
4. Gartner field-service benchmarks — paywalled.
5. Quantified override rates for optimised *schedules* as opposed to delivery *routes*.
6. Any post-deployment **measured** waste-collection result.
7. Service Council / Aberdeen first-time-fix benchmarks — seen only in vendor blog snippets. Marked
   uncertain.
8. **A documented failed or abandoned routing deployment with numbers.** Vendors acknowledge failure
   qualitatively; no rigorous post-mortem exists. Same publication-bias problem as section 5.



## 7. What distinguishes success from failure

### 7.1 A warning about this section

This is the section where the evidence is weakest and the temptation to reach is strongest. Most
published "critical success factors for IT implementation" work is (a) retrospective, (b) based on
interviews with people explaining their own outcomes, and (c) unable to separate causes from
correlates. Success factors identified this way have a habit of being the things successful
organisations *say about themselves*.

I have separated below what is genuinely evidenced from what is widely asserted but not
demonstrated. **The specific propositions in the brief — capacity foundation before optimisation,
phased versus big-bang, pilot-site selection — mostly fall into the second category.** That is
worth knowing before anyone cites them as settled.

### 7.2 What the evidence does support

**1. Process change, not deployment, produces return. [IND, multiple sources, consistent]**

This is the best-supported finding in the whole document and it appears independently in every
strand of the literature.

- Jang et al. (2014): *"A positive ROI does not happen automatically upon implementing an EHR
  package, and a clinic's ability to leverage EHR for process changes plays a role in achieving a
  positive ROI."* https://pmc.ncbi.nlm.nih.gov/articles/PMC4288109/
- The EHR ROI literature summarised by NAM (2014) finds negative results *"associated with
  workflow implications."*
  https://nam.edu/perspectives/return-on-information-a-standard-model-for-assessing-institutional-return-on-electronic-health-records/
- Tursunbayeva et al. (2020) name **process analysis** among the four gating actions for HRIS
  benefit realisation. https://doi.org/10.1177/2158244020933881

**2. Early engagement with the people who currently do the work. [IND]**

Kellogg & Walczak identify *"the lack of early communication with the nurses and those in charge
of scheduling"* and *"lack of nurse-centered solutions"* as primary drivers of the 70%
non-implementation rate in nurse scheduling.
https://www.researchgate.net/publication/220249866_Nurse_Scheduling_From_Academia_to_Implementation_or_Not

**3. Data preparation as a precondition. [IND, but qualitative]**

Tursunbayeva et al. (2020) name *"adequate data preparation"* alongside training, communication
and process analysis as the necessary actions for benefit realisation in a national healthcare
HRIS programme. This is the closest thing in the literature to support for the
"capacity-foundation-first" proposition — see 7.4 for why it is not the same claim.

**4. Benefits measured per module and per user group, not organisation-wide. [IND]**

Tursunbayeva et al. (2020) conclude benefits must be considered *"at the level of individual
modules and user groups, as well as for the organization as a whole"*, and that the benefits plan
must be **reviewed at regular intervals** so the project can adapt. Organisation-level benefit
claims cannot be attributed, and unattributable benefits stop being tracked.

**5. Sustainment is a distinct problem from delivery. [CONSULT, but the numbers are stark]**

McKinsey (2018): 16% succeeded and sustained; a further 7% improved performance and then lost it.
Roughly **three in ten programmes that produce a real improvement subsequently fail to hold it.**
Planning that ends at go-live is planning for the 7%.
https://www.mckinsey.com/capabilities/people-and-organizational-performance/our-insights/unlocking-success-in-digital-transformations

**6. Long benefit horizons need explicit attribution design up front. [IND]**

Cresswell et al. (2022) found benefits *"emerged gradually and over long timeframes"*, producing
*"problems of attribution of benefits to causes"*, and that a single reporting mechanism could not
serve both local operational needs and organisation-level ROI reporting — *"a single integrated
reporting mechanism is unlikely to fulfill both national and local requirements."*
https://doi.org/10.1093/jamia/ocab283 (open access: https://pmc.ncbi.nlm.nih.gov/articles/PMC8800528/)

The operational implication: **you need two measurement systems, not one.** A local one the teams
actually use, and a separate attribution-grade one for the business case. Trying to make one serve
both has been tried at national scale and failed.

### 7.3 On capacity foundation before scheduling optimisation

**Evidence status: mechanistically well-supported, directly unevidenced.**

I found **no study that compares organisations that built a capacity/demand baseline before
deploying scheduling optimisation against those that did not.** That comparison does not exist in
the literature. Anyone asserting it is reasoning from first principles, and should say so.

What *does* support the proposition, indirectly but strongly:

- The dominant documented failure mode in nurse scheduling is **constraint and rule fidelity** —
  real rules differ by institution, by ward, and by planning horizon, and are largely undocumented.
  https://link.springer.com/article/10.1007/s10916-014-0160-8
  An optimiser cannot be better than its constraint model, and the constraint model is exactly
  what a capacity foundation would produce.
- You cannot measure an improvement without a baseline. Section 5.4's Forcura example is the
  cautionary case in miniature: a published headline metric (*"an average of 30 minutes per
  referral"*) with **no before number anywhere in the document**, and therefore no computable
  improvement. That is what happens when measurement is retrofitted.
- The NAM finding that healthcare ROI methods are *"different and, consequently, incomparable"*
  means no external benchmark will rescue a missing internal baseline.

**Honest statement for the business case: building the capacity baseline first is well-reasoned
and cheap insurance against the two most common failure modes. It is not empirically proven to
improve outcomes, because nobody has run that comparison.**

### 7.4 On phased versus big-bang rollout

**Evidence status: weak. Do not cite this as settled.**

The available material on phased-versus-big-bang is dominated by ERP consultancy blogs, which have
a commercial interest in longer engagements. The one substantive point that recurs across
independent-ish sources is that **implementation success depends more on planning, change
management, executive sponsorship, training and testing than on the deployment method itself.**

In healthcare specifically, phased rollout is the professional consensus for EHRs, but the stated
justification is **patient safety and continuity of care**, not superior benefit realisation.
Those are different arguments and should not be conflated.

The genuinely relevant evidence is indirect and comes from Flyvbjerg et al. (2022): IT cost
overruns follow a power law with an infinite-variance tail. **Under a fat-tailed distribution, the
argument for phasing is not that phases perform better on average — it is that phasing caps the
maximum loss on any single commitment.** That is a decision-theoretic argument, and it is much
stronger than the change-management argument usually offered.
https://ora.ox.ac.uk/objects/uuid:a6ea9269-366c-4c7a-8b05-782f5fa3b0d2

### 7.5 On pilot-site selection

**Evidence status: essentially absent, and the known bias runs the wrong way.**

I found no study evaluating pilot-site selection strategy for healthcare workforce technology.

What can be said with confidence is a warning rather than a recommendation. The entire home health
vendor evidence base reviewed in section 5 consists of **n=1 sites with no control group and no
secular-trend adjustment** — which is precisely what a pilot produces. The Patriot Homecare case
is the worked example: a +26% census "result" measured across the COVID trough-to-rebound, where
the same document concedes the site had *"seen their census drop by over 100 patients"*.

**A pilot at a well-run, enthusiastic, self-selected site measures the site, not the software.**
The selection effect that makes a pilot succeed is the same effect that makes it fail to
generalise. If pilot results are going to underwrite a scaled business case, the pilot needs a
concurrent comparison site — and essentially nobody in this sector does that.

### 7.6 The synthesised short list

Ranked by strength of evidence, not by how good they sound:

| Factor | Evidence strength | Source |
|---|---|---|
| Process redesign accompanies deployment | Strong, multi-source | Jang 2014; NAM 2014; Tursunbayeva 2020 |
| Early engagement of incumbent schedulers/clinicians | Strong | Kellogg & Walczak 2007 |
| Complete, validated constraint/rule model | Strong (as failure mode) | JMS 2014; nurse scheduling literature |
| Benefits tracked per module and user group, reviewed periodically | Moderate | Tursunbayeva 2020 |
| Separate operational vs attribution measurement | Moderate | Cresswell 2022 |
| Explicit sustainment plan beyond go-live | Moderate | McKinsey 2018 |
| Baseline captured before change | Inferred, not tested | — |
| Phased over big-bang | Weak on benefits; strong on tail-risk capping | Flyvbjerg 2022 (indirect) |
| Pilot-site selection strategy | Absent | — |



## The base rate this initiative should be judged against

### The headline estimate

**Probability that an initiative of this class delivers its stated business case, as written, on
roughly the stated timeline, and can demonstrate that it did: 10–15%.**

**Probability that it delivers a material majority (≥50%) of the claimed benefit value, allowing
for delay: 25–35%.**

**Probability that it produces real, worthwhile improvement well short of the business case:
30–40%.**

**Probability that it delivers nothing measurable, or is abandoned: 20–30%.**

And the one that matters most, because it is not a failure mode anyone plans for:

**Probability that the business case is never formally tested against outcomes at all — that
benefits are neither proven nor disproven, and the question simply stops being asked: 40–60%.**

That last figure overlaps the others. It is not a fifth outcome; it is a property of how these
programmes end.

### How I got there

**Start with the outside-view anchors.** The large-sample IT evidence puts mean benefit shortfall
at **56%** (McKinsey–Oxford, n>5,400). McKinsey's transformation survey puts full success at
**<30%**, and success-plus-sustainment at **16%**. Kaplan & Harris-Salamone's compilation puts
"truly successful" at **as few as one in eight**. The older Panorama series had **~57%** of ERP
implementations materially missing their benefit case. These cluster in a consistent band: **the
unconditional prior for "delivers what was promised" in enterprise technology is roughly 15–30%.**

**Then apply the domain-specific adjustments.** Every one of them points the same way.

| Adjustment | Direction | Reason |
|---|---|---|
| Scheduling optimisation specifically | **Down** | Only 30% of published nurse-scheduling methods ever reached implementation at all (Kellogg & Walczak 2007); most that did stayed single-site |
| Home health evidence base | **Down** | Zero independent evaluations exist. No external benchmark, no validated effect size, nothing to calibrate a forecast against |
| The headline headcount claim | **Down, hard** | A ~65% back-office reduction has no documented precedent in either direction. Sector admin share *rose* 1999–2017; non-clinical healthcare headcount rose 12.4% during the EHR build-out; the flagship RPA case could not separate elimination from redeployment at all |
| Direction of sector travel | **Down** | Home health visits per episode fell 19.4 → 15.9 (2019→2023) while margins held near 20%. A capacity-expansion thesis argues against the observed trend |
| Two-stage dependency | **Down** | If a capacity foundation must land before optimisation can pay, the probabilities multiply. Two 60% steps is a 36% programme |
| Measurement culture | **Down** | NAM: no accepted ROI framework, methods *"different and, consequently, incomparable."* Cresswell: attribution collapses over long horizons. Over half of RPA adopters never calculated actual cost reduction |
| Adoption and compliance | **Down** | 8.6% voluntary adoption at 14 sites; 75% of deliveries did not follow the planned sequence. Modelled benefit × adoption × compliance is the honest formula; business cases usually carry only the first term |
| Median project lands on budget | **Up, modestly** | Flyvbjerg 2022: mode and median cost overrun ≈ 0%; HRM-class projects median 1.0×. Cost discipline is achievable — it is *benefit* that reliably disappoints |
| Scheduler time-saving is real | **Up, modestly** | The 45→10 min finding is the one benefit that shows up consistently across the literature. Small, but real, and it lands early |
| Routing benefit is real, if modest | **Up, modestly** | Field service gives a genuine measured floor: 5–15% travel reduction, 4–15% productivity. That is a real, bankable benefit — just not the one usually promised |

Net: the domain adjustments are strongly negative against a 15–30% prior, which is why I land at
**10–15% for full delivery as stated** rather than at the generic 20%.

### The three things this base rate is really telling you

**1. Cost is not the risk. Benefit is.** The median IT project hits its budget. What fails is the
benefit side — and it fails quietly, because nobody set the baseline. Flyvbjerg's power-law
finding adds the necessary caveat: *"the average cost overrun for IT projects does not exist."*
Plan for the tail, but do not spend your governance attention there. Spend it on whether the
benefit will be measurable.

**2. The modal outcome is not failure — it is amnesia.** The single most likely end-state is a
system that goes live, works acceptably, is broadly liked, and whose business case is never
revisited. NAM found no accepted framework for measuring return; Cresswell found benefits emerge
*"gradually and over long timeframes"* creating *"problems of attribution of benefits to causes."*
This outcome is worse than visible failure, because nothing is learned and the same case can be
made again in three years.

**3. Adoption is the binding constraint, and business cases treat it as an assumption.** 8.6% of
notes. 18.2% mean use rate. 70% of visits auto-scheduled as a *marketing headline* five years
after launch. Three in four deliveries not following the planned sequence. **At realistic adoption
and compliance, a perfect tool delivers a fraction of its modelled benefit** — and neither
variable usually appears as a line in the model.

### The number to anchor on, if you only take one

**Field service is the best-measured analogue to home health visit scheduling, and its honest
realised range is 5–15% travel reduction and 4–15% productivity gain.** UPS — the largest,
best-funded, most-celebrated route optimisation programme in the world — landed at **8–10%**, over
**thirteen years**. British Telecom's national technician-scheduling deployment reportedly landed
at **4%**.

**If a business case in this class projects benefits materially above ~15%, it is projecting
outside everything that has ever been independently measured in any adjacent industry.** That does
not make it wrong. It makes it an extraordinary claim, and it should carry extraordinary
justification rather than a vendor citation.

### What an organisation could do to beat the base rate

These are ordered by expected effect on the probability of delivering, and each is drawn from a
finding above rather than from general good practice.

**Tier 1 — the ones that actually move the number**

1. **Capture the baseline before anything is built, and keep a concurrent comparison site.**
   Without it you cannot prove benefit, and section 5 shows this entire sector fails to. The
   Forcura case — a published headline metric with no before-number anywhere in the document — is
   what retrofitted measurement looks like. A comparison site is what separates your pilot from
   the n=1, no-control, COVID-rebound case studies that constitute the vendor evidence base.

2. **Scope the programme as process redesign, with software as an input.** This is the single
   best-supported success factor in the literature and it appears in every independent strand:
   Jang 2014 (*"a clinic's ability to leverage EHR for process changes plays a role"*), NAM 2014
   (negative results *"associated with workflow implications"*), Tursunbayeva 2020 (process
   analysis as a gating action). Deployment without process change returns zero.

3. **Forecast adoption explicitly, as a number, with a curve — and hold the business case to it.**
   Take 8.6% and 18.2% as your realistic anchors for voluntary use, not 100%. If the case only
   works at 80% adoption, the case is a bet on adoption, and should be argued as one.

4. **Build and validate the constraint/rule model with incumbent schedulers before optimising
   anything.** The dominant documented failure mode in this exact domain is constraint fidelity —
   rules differ by site, by team, and by planning horizon, and are largely undocumented. An
   optimiser on an incomplete rule set produces unusable schedules and burns frontline trust in a
   single cycle. Note that the incumbent schedulers are the people whose roles the business case
   proposes to reduce; that conflict is structural and must be handled explicitly, not
   optimistically.

**Tier 2 — materially helpful**

5. **Run two measurement systems, not one.** Cresswell et al. found at national scale that a
   single reporting mechanism *"is unlikely to fulfill both national and local requirements."*
   Build a lightweight operational one the teams use, and a separate attribution-grade one for the
   business case.

6. **Track benefits per module and per user group, on a fixed review cadence** (Tursunbayeva 2020).
   Organisation-wide benefit claims cannot be attributed, and unattributable benefits stop being
   tracked.

7. **Phase the commitment — for tail-risk reasons, not change-management reasons.** Under a
   power-law cost distribution, phasing's value is that it caps maximum loss per commitment. That
   argument is sound; the "phases perform better on average" argument is not evidenced and should
   not be used.

8. **Name a sustainment owner and fund the period after go-live.** Roughly three in ten programmes
   that produce a real improvement then lose it (McKinsey 2018: 16% sustained, 7% improved and
   regressed). Planning that ends at go-live is planning for the 7%.

**Tier 3 — cheap, and prevents specific documented failures**

9. **Ban automation-rate metrics from standing in for capacity metrics.** "70% of visits
   auto-scheduled" and "95% of visit types automated" are input metrics. Every vendor in this
   sector reports them *instead of* outcomes. Decide now which outcome metric decides the
   question — visits per clinician per day, travel time, agency spend — and instrument it before
   go-live.

10. **Do not convert FTE reductions to savings without checking where the work went.** Handlon et
    al. (2025) found admin *salary* share fell while total admin cost rose, as work migrated to
    non-salary lines. Budget the licences, vendors and outsourced services the automation creates.

11. **Write the kill criteria before starting.** Specify in advance what result at what date would
    mean stopping. Given a 40–60% chance the question is never asked again, pre-committing to when
    you will ask it is the cheapest available protection.

12. **Assume the benefit lands late.** Homecare Homebase went ~5 years from announcing Smart
    Scheduling to publishing any quantified usage number at its largest customer. Cresswell found
    benefits emerge over long timeframes. A business case whose payback horizon exceeds the likely
    tenure of its sponsor needs institutional ownership, not executive ownership.

### The honest closing statement

**The reference class for this initiative is thin, and where it is not thin it is unflattering.**

There is no independent evidence that scheduling optimisation improves capacity in home health,
because nobody has ever published a controlled evaluation of it. There is good evidence that the
sector is moving toward fewer visits per episode at stable-to-high margins. There is strong
evidence that large administrative headcount reductions from automation do not materialise at the
scale claimed. And there is very strong evidence that most organisations never find out either
way.

None of that means the initiative is a bad idea. It means **the business case cannot be justified
by external evidence, because the external evidence does not exist** — and therefore the case
rests entirely on the quality of the organisation's own baseline, instrumentation, and honesty
about adoption. An organisation that builds those three things first is doing the thing that no
one in this reference class has done, which is the only defensible reason to expect a
better-than-base-rate result.

Everything else in the plan is a bet that this time is different. It usually isn't.

