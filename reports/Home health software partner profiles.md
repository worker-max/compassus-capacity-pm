# Three AI vendors compete for Compassus's HCHB layer

Of the three candidates, **VitalisCare is the closest functional fit for Compassus's hospice business and the weakest on corporate transparency**. **Arya is the best-funded and best-documented company but the furthest from HCHB**. **Axle Health is the most mature scheduling engine, and HCHB appears among the EMRs it names**. All three sell software that sits on top of the EMR and leaves it as the system of record, and none replaces Homecare Homebase. They solve different problems, though:

- **VitalisCare** sells seven hospice-only apps (end-of-life prediction, HOPE tracking, scheduling, compliance, SNF room-and-board). Homecare Homebase (HCHB) is the only EMR it names. Its legal entity is an Israeli company (VitalisCare Ltd.) inside a New Jersey venture studio. It has **no disclosed funding and only one named executive**.
- **Arya Health** has raised about **$25M** (Series A led by ACME Capital, October 2025). Its AI agents handle non-clinical back-office work: scheduling, recruiting, onboarding, credential compliance, intake and payroll. It **names no EMR integration at all**, and its customers are mostly home care and pediatric providers.
- **Axle Health** is a Y Combinator company that has raised about **$14.4M** (Series A led by F-Prime, May 2025). It sells AI scheduling, routing and dispatch. It has the most developed integration story (Epic, athenahealth, WellSky, Netsmart, HCHB) and public developer APIs. It became a software company only in 2023, after shutting down an in-home testing services business.

None of the three has a named large Medicare-certified hospice or home health chain as a customer. All three rely mainly on self-reported results. Each also has a name or legal-entity ambiguity that Compassus legal must resolve before signing a BAA or a co-development agreement. Absent the vendor's own disclosures, the right choice depends on the use case. VitalisCare fits hospice clinical-operations intelligence on HCHB. Arya fits workforce and intake capacity. Axle fits visit scheduling and routing across home health and hospice.

Evidence labels used throughout: **Confirmed** means stated in a cited primary or vendor source. **Vendor claim** means the company's own marketing, not independently checked. **Estimated** means an aggregator figure, an analyst inference, or a point where sources conflict. **Not found** means searched for and not located. Several aggregator pages (Crunchbase, PitchBook, Tracxn, LinkedIn) were blocked during research, so some estimates rest on search snippets.

## Side-by-side: the three vendors at a glance

| Dimension | VitalisCare | Arya Health | Axle Health |
|---|---|---|---|
| Domain | vitaliscare.ai (Confirmed) | aryahealth.ai; app.aryaworks.com (Confirmed) | axlehealth.com (Confirmed) |
| Legal entity | VitalisCare Ltd., Jerusalem, Israel (Confirmed, privacy policy); US entity Not found | Possibly "Arya, LLC" (Estimated); not verified | Possibly "Axle Health, Inc." (Estimated); state Not found |
| HQ | Jerusalem legal address (Confirmed); Lakewood, NJ studio (Estimated) | New York City (Confirmed) | Santa Monica / Los Angeles (Confirmed) |
| Founded | About 2024–25 (Estimated); parent studio about 2020 (Estimated) | 2022 (Estimated) | 2020 (Confirmed, YC) |
| CEO | Dr. Dina Yankelewitz (Confirmed) | Kunal Sarda (Confirmed) | Adam Stansell (Confirmed) |
| Headcount | 11–50 (Estimated); depends on studio's shared pool | About 20–60 (Estimated, unsourced inference) | About 25–28, flat (Estimated) |
| Total funding | None disclosed (Not found) | About $25M (Confirmed) | About $14.4M disclosed; aggregators say $14.3M–$16.8M (Estimated) |
| Last round | None found | $18.2M Series A, Oct 2025, ACME Capital (Confirmed) | $10M Series A, May 2025, F-Prime (Confirmed) |
| Revenue signal | Studio revenue about $1M (Estimated, low confidence) | More than 6x growth in 12 months to Oct 2025 (Vendor claim) | Over $1M ARR within 12 months of launch; about 10x growth in FY2024 (Vendor claim) |
| Care segments | Hospice only | Home health, home care, hospice, SNF, private duty and others | Home health, health systems, pediatrics, mobile phlebotomy and other field care |
| Product type | Seven hospice AI apps | One AI agent with eight administrative skills, plus a free emergency agent | Scheduling, routing, dispatch, patient engagement, APIs |
| HCHB evidence | Named on product pages; HCHB-operator customer (Confirmed) | None (Not found) | HCHB named in a website testimonial (Confirmed); depth unknown |
| Other EMRs named | None | None named | Epic, athenahealth, WellSky, Netsmart, Statewise |
| Public API docs | Not found | Not found | developers.axlehealth.com exists (Confirmed) |
| Security claims | HIPAA, SOC 2 Type II (Vendor claim, no trust center) | SOC 2 Type I and II, HIPAA, annual pen tests, Trust Center (Vendor claim) | SOC 2 Type II, HIPAA, pen tests, SSO/SAML, trust portal (Vendor claim) |
| HITRUST | Not found | Not found | Not found |
| Named customers | Moments Hospice, Anchor Hospice | TheKey, Team Select, Thrive, Connect Pediatrics | Cityblock, Penn Medicine, Imagine Pediatrics, Grand Care |
| Pricing model | By patient census, no setup fees, auto-renewing | Not disclosed; integration billed separately (Estimated) | Based on ROI savings, with an implementation manager per customer |

## VitalisCare ships fast on HCHB but hides behind a studio

### Identity, structure and history

The hospice software vendor is **Vitalis Care at vitaliscare.ai**. Its privacy policy names the legal entity as **VitalisCare Ltd.** at a Jerusalem, Israel address. The policy was last updated March 24, 2025, and gives no US state of incorporation ([Privacy Policy](https://vitaliscare.ai/privacy-policy/)).

Vitalis Care is a portfolio company of **Integralytic**, a "healthtech venture studio." Integralytic says it designs and launches AI startups and then "secures funding" after building an MVP. Its other portfolio companies are DolphinCare (SNF MDS and reimbursement), 1Dose and Exclugo ([Integralytic](https://integralytic.com/)). Aggregators place Integralytic in Lakewood, NJ, founded in 2020 (Estimated) ([RocketReach](https://rocketreach.co/integralytic-profile_b428c5cec1f99bcf)).

No US subsidiary, Israeli registration number or formal Ltd.–studio relationship was found. Compassus therefore does not yet know **who would sign its BAA or own co-built IP**.

**Name collisions are a real hazard.** The LinkedIn slug "vitalis-care" belongs to a **French home infusion provider in Marseille**, not this company ([LinkedIn FR](https://fr.linkedin.com/company/vitaliscare)). Several other similarly named companies have been ruled out:

- **VitalCaring Group**, a US home health and hospice *operator* ([Constant Therapy](https://constanttherapyhealth.com/vitalcaring-leverages-ai-program-to-improve-outcomes-ease-caregiver-burden/))
- An Australian care provider called Vitalis
- **Vali Health**, a separate home-care AI startup that raised $6M ([HomeCare Magazine](https://www.homecaremag.com/news/vali-health-raises-6m-ease-homecare-workload-ai))
- "Vitalis" entries on PitchBook and Tracxn that point to other entities ([PitchBook](https://pitchbook.com/profiles/company/525844-63))

None of the funding data on those profiles should be attributed to Vitalis Care.

The company is very young. In July 2025 the CEO said it first targeted "scheduling optimization, compliance, and reimbursement" ([Husch Blackwell](https://www.huschblackwell.com/newsandinsights/ai-in-action-exploring-how-ai-is-helping-hospices-do-things-in-new-ways)). An August 2026 release says it "began as a single end-of-life prediction tool," and the CEO said, "When we started, Vitalis was one app. Today it's seven" ([press release](https://vitaliscare.ai/vitalis-care-hospice-news-product-of-the-year-nominee/)). The two accounts of which product came first conflict. The same release announced a nomination for the 2026 Hospice News Product of the Year, a community-voted award. Whether it won is Not found.

### Leadership, size and money

The only named leader is **Dr. Dina Yankelewitz**, founder and CEO. She has a doctorate in mathematics education, is a former professor, and works in data analytics and AI (Confirmed) ([Husch Blackwell](https://www.huschblackwell.com/newsandinsights/ai-in-action-exploring-how-ai-is-helping-hospices-do-things-in-new-ways)). Aggregators also list her as CEO of 1Dose and founder of Integralytic (Estimated) ([RocketReach](https://rocketreach.co/dina-yankelewitz-email_105775381)), which creates **key-person concentration** across several portfolio companies.

Hospice domain expertise comes from unnamed advisors. The Vantage page says it was "built with hospice clinical leaders, medical directors, and HCHB operations experts" but names none ([Vantage](https://vitaliscare.ai/vantage/)). A CTO, clinical lead, board and advisors are all Not found.

Headcount estimates vary widely:

- Crunchbase lists Vitalis Care at **11–50 employees** (Estimated) ([Crunchbase](https://www.crunchbase.com/organization/vitalis-care)).
- For Integralytic, ZoomInfo says 1–10 employees and RocketReach says 41 employees with about $1M revenue ([ZoomInfo](https://www.zoominfo.com/c/integralytic/433681601)).
- Integralytic itself claims a "team of 150+."

**SEC EDGAR returns zero Form D filings for "Vitalis Care"** ([EDGAR](https://efts.sec.gov/LATEST/search-index?q=%22Vitalis%20Care%22&forms=D)). No funding round, investor, valuation or grant was found. An Israeli Ltd. could raise money without a US filing, so this means only that nothing is disclosed, not that nothing was raised.

### Every product

Vitalis sells seven apps in four suites, all positioned as AI layers on top of the EMR ([homepage](https://vitaliscare.ai); [press release](https://vitaliscare.ai/vitalis-care-hospice-news-product-of-the-year-nominee/)).

**Care Suite**
- **Vantage** flags patients likely to die within 7–10 days and refreshes every 10 minutes. It claims **94% accuracy versus about 67% for "typical EMR tools"**, a figure with no published source. It also claims training on "50+ billion clinical signals" and **"full integration" with HCHB** (Vendor claim) ([Vantage](https://vitaliscare.ai/vantage/)).
- **Ray** tracks the HOPE assessment timeline and flags missed symptom follow-up visits (SFVs) and overdue HOPE update visits (HUVs).

**Coordination Suite**
- **Sync** is AI scheduling with human approval of each change, and it includes an "Original HCHB schedule view." The homepage claims 55–65% less drive time, but the Sync page cites only about 30% travel reduction. The two claims are inconsistent ([Sync](https://vitaliscare.ai/sync/)).
- **Sync360** is a field-staff app with GPS mileage tracking and mileage-fraud detection.

**Compliance Suite**
- **Align** scans documentation for gaps and claims it "prevents up to 90% of audit denials."
- **Guide** gives bedside documentation prompts and voice-to-text.

**Collaboration Suite**
- **Bridge** is a shared hospice–SNF room-and-board dashboard. It claims payment turnaround falls from 30–60 days to 6–14 days.

Pricing is **by patient census**, with no setup fees and auto-renewing subscriptions. The company has no home health product, and it names no EMR other than HCHB.

### Customers and security

Named customers are **Moments Hospice** and **Anchor Hospice**:

- Emma Stroup, Moments Hospice's Director of HCHB Operations, is quoted on the homepage ([homepage](https://vitaliscare.ai)).
- Anchor's Ray case study reports 97–99% HOPE compliance and about 1.5 hours saved per morning (Vendor claim) ([case studies](https://vitaliscare.ai/case-studies/)).

Other testimonials give only initials. The company claims **HIPAA and SOC 2 Type II** compliance but links no report or trust center. HITRUST, the hosting region and the subprocessor list are Not found.

## Arya raised $25M for back-office agents, not clinical work

### Identity, structure and history

Arya Health brands itself simply as "Arya." It is a New York company that builds "AI-powered digital agents that reduce administrative work for home health, home care, and hospice providers" ([PR Newswire](https://www.prnewswire.com/news-releases/arya-health-secures-18-2m-series-a-to-power-the-next-generation-of-ai-agents-for-post-acute-care-administration-302597627.html)). The name comes from the founder's daughter ([Arya blog](https://www.aryahealth.ai/blog/arya-series-a-ai-system-of-action-distributed-care)). An aggregator gives 2022 as the founding year (Estimated) ([AI Health Index](https://aihealthindex.io/vendors/arya-health)).

**The most dangerous collision in this report:** SEC filings show that **Yuvo, Inc.** (CIK 0001907652), an unrelated Delaware company in NYC, was **previously named "Arya Health, Incorporated."** Yuvo has a different CEO (Cesar Herrera) and has filed Form Ds of its own, including $8.17M in 2024 and $4.26M in 2026 ([Yuvo 2024 Form D](https://www.sec.gov/Archives/edgar/data/1907652/000190765224000001/primary_doc.xml); [2026 Form D](https://www.sec.gov/Archives/edgar/data/1907652/000190765226000001/primary_doc.xml)). **None of those filings belong to Arya.**

Arya's own legal name may be **"Arya, LLC"**, based on a seed-round listing (Estimated) ([The SaaS News](https://www.thesaasnews.com/news/arya-health-closes-4m-in-seed-round/)). A priced Series A normally requires a C-corporation, so the current entity may differ. Other companies ruled out are:

- Arya.ag, an Indian grain-commerce platform ([AgroSpectrum](https://agrospectrumindia.com/news/5/29321/arya-ag-appoints-jatinder-alagh-as-the-new-chief-technology-officer.html))
- Arya Home Healthcare LLC, a Virginia care provider ([Glassdoor](https://www.glassdoor.com/Overview/Working-at-Arya-Home-Healthcare-EI_IE6037065.11,31.htm))
- The ARYA Sciences SPACs and several other "Arya" filers on EDGAR ([EDGAR](https://www.sec.gov/cgi-bin/browse-edgar?company=arya&match=starts-with&type=D&dateb=&owner=include&count=100&action=getcompany))

A VCBacked record for "Arya, Philadelphia" lists Arya Health's seed investors and is probably the same company recorded in the wrong city (Estimated) ([VCBacked](https://www.vcbacked.co/company/arya-philadelphia)).

Arya's positioning has shifted over time:

- **September 2024:** the company was a "healthcare workforce automation platform" covering scheduling, payroll, onboarding and compliance ([The SaaS News](https://www.thesaasnews.com/news/arya-health-closes-4m-in-seed-round/)).
- **October 2025:** it repositioned as an AI-native "system of action" and planned an Intake Agent "starting with design partners" ([Arya blog](https://www.aryahealth.ai/blog/arya-series-a-ai-system-of-action-distributed-care)).
- **January 2026:** it launched a free Emergency Response Agent nationwide ([HomeCare Magazine](https://www.homecaremag.com/news/expected-outages-inspire-aryas-emergency-response-agent)).
- **2026:** it won a MedTech Breakthrough Award.

### Leadership, size and money

**Kunal Sarda** is CEO and co-founder (Confirmed). According to an aggregator, he co-founded VerbalizeIt, which appeared on Shark Tank and was sold to Smartling in 2016. He then worked at Smartling until 2020 and holds a Wharton MBA (Estimated) ([yespress.io](https://yespress.io/kunal-sarda.md)). Another profile ties him to Verto, Flipkart and Google, but it appears to describe a different person ([highperformr.ai](https://www.highperformr.ai/people/kunalsarda)). The co-founder name "Arunram Kalaiselvan" comes from one aggregator only and is uncorroborated.

Domain depth came through a hire. **Melinda Phillips**, former CEO of Thrive Skilled Pediatric Care (acquired by Aveanna), leads Arya's Care@Home Center of Excellence ([Skilled Nursing News](https://skillednursingnews.com/2025/10/arya-health-lands-18-2m-series-a-aims-to-lessen-post-acute-provider-burden-with-ai/)). The CTO, the full executive team and the board are Not found. ACME partner **Aike Ho**, who led the Series A, is the likely board member, though this is not confirmed.

Headcount is undisclosed. Open roles as of October 2026 are all in-person in NYC: an enterprise customer-success lead, a principal platform engineer and a deployment specialist ([careers](https://www.aryahealth.ai/careers)).

Funding is the best-documented of the three:

| Round | Date | Amount | Investors | Status |
|---|---|---|---|---|
| Pre-seed / angel | Before 2024 | About $2.8M (implied by subtraction) | Probably Ridge and Oceans | Estimated |
| Seed | Sep 2024 | $4.0M | Twelve Below (lead), Nebular, Oceans, Ridge; VCBacked also lists f7 Ventures and Operator Partners | Confirmed, plus Estimated additions |
| Series A | Oct 29, 2025 | $18.2M | ACME Capital (lead), Ridge, Twelve Below, OpenAI executives, "leading post-acute care providers" | Confirmed |
| **Total** | | **About $25M** | | Confirmed |

Sources: [PR Newswire](https://www.prnewswire.com/news-releases/arya-health-secures-18-2m-series-a-to-power-the-next-generation-of-ai-agents-for-post-acute-care-administration-302597627.html); [The SaaS News](https://www.thesaasnews.com/news/arya-health-closes-4m-in-seed-round/).

Arya claims revenue grew **more than 6x** over the 12 months to October 2025 and was "pacing toward 10x" ([Arya blog](https://www.aryahealth.ai/blog/arya-series-a-ai-system-of-action-distributed-care)). Absolute revenue and valuation are Not found. Because some investors are post-acute providers, an Arya partnership may involve Compassus's competitors as shareholders.

### Every product

Arya sells **"One Agent with eight skills"**: Scheduling, Compliance, Talent, Onboarding, Intake, Payroll, Engagement and Front Desk ([homepage](https://www.aryahealth.ai/)). Its vendor claims include:

- **Onboarding:** 50% faster time-to-first-staffing and 70% less administrative work.
- **Talent:** 60% less recruiting effort.
- **Compliance:** automated license tracking that deploys in under a week.

All agents run in either co-pilot or autopilot mode, use text, voice and email, and keep audit trails ([Arya blog](https://www.aryahealth.ai/blog/arya-series-a-ai-system-of-action-distributed-care)).

The free **Emergency Response Agent** answers calls and texts on a local number for each location, triages them, escalates to on-call staff, and "does not access detailed medical histories" ([HomeCare Magazine](https://www.homecaremag.com/news/expected-outages-inspire-aryas-emergency-response-agent)).

Arya says it reads and writes "EMRs, ATS, HRIS in near-real time" but **names no EMR** ([homepage](https://www.aryahealth.ai/)). One aggregator reports "no verified bidirectional EHR connection." The same aggregator lists Google Gemini and earlier Anthropic Claude (via AWS Bedrock) as the language models, and Supabase, Cloudflare, Bland AI (voice) and n8n as subprocessors (Estimated) ([AI Health Index](https://aihealthindex.io/vendors/arya-health)).

Arya has **no clinical documentation, OASIS, coding or hospice-specific workflow** (IDG, HOPE, bereavement). The newer skills (Intake, Front Desk, Engagement) are likely less mature than Scheduling, Talent and Onboarding.

### Customers and security

Named customers are **TheKey, Team Select Home Care, Thrive Skilled Pediatric Care and Connect Pediatrics**. Connect Pediatrics reported a **25% gain in scheduler capacity** with no added headcount ([HomeCare Magazine](https://www.homecaremag.com/news/arya-health-releases-results-connect-pediatrics-partnership)). No Medicare-certified hospice or home health customer is named.

Arya claims SOC 2 Type I and II, HIPAA compliance, annual pen tests and a Trust Center. An aggregator says SOC 2 reports are available under NDA and BAAs are offered. The same source reports a 30-day auto-renewal notice, 60 days' notice for price increases, and integration work billed separately (Estimated) ([AI Health Index](https://aihealthindex.io/vendors/arya-health)).

## Axle pivoted from house calls to a routing engine

### Identity, structure and history

**Axle Health** (axlehealth.com) was founded in 2020, went through Y Combinator in Winter 2021, and is based in Los Angeles with its HQ in Santa Monica ([YC](https://www.ycombinator.com/companies/axle-health)). Its law firm, Gunderson Dettmer, describes it as a Los Angeles healthcare technology company ([Gunderson](https://www.gunder.com/en/news-insights/client-news/axle-health-announces-dollar10m-series-a-to-advance-home-health-operations)). The website footer misspells the name as "Axle Heath."

"Axle Health, Inc." appears only on a third-party insider listing (Estimated) ([MarketScreener](https://de.marketscreener.com/insider/CONNOR-HAILEY-A3DUVG)). **No Form D exists under the name** ([EDGAR](https://efts.sec.gov/LATEST/search-index?q=%22Axle%20Health%22&forms=D)), which suggests it files under a different legal name.

Several unrelated companies share the name:

- "Axle," an open-insurance API company ([theorg](https://theorg.com/org/contrary/org-chart/nihar-parikh))
- "Axle," corporate-access software for banks
- "Axel Health," listed on CB Insights ([CB Insights](https://www.cbinsights.com/company/x-akseli/people))

Disambiguate any Crunchbase or PitchBook pull by the domain.

The history includes a **material pivot**. From 2020 to 2021, Axle ran a network of phlebotomists, medical assistants and nurses doing mostly in-home COVID testing for telehealth partners, with Sameday Health as its largest partner. That network grew to cover all 50 states with "a couple million dollars" of revenue. **In 2023 Axle shut down the services business** to license its internal scheduling tool as SaaS. The software reportedly passed $1M ARR within a year (secondary source) ([healthcarediscovery.ai](https://healthcarediscovery.ai/companies/axle-health/)). Job posts from 2021–22 for mobile phlebotomists confirm the services era ([DirectShifts posting](https://jobs.somacap.com/companies/directshifts/jobs/12748005-mobile-phlebotomist-in-home-patient-calls)).

The upside of this history is that the product was built for Axle's own field clinicians. The downside is that its depth in certified home health rules (OASIS, LUPA visit thresholds, hospice IDG) is unproven.

### Leadership, size and money

**Adam Stansell** is founder and CEO. He previously worked at Uber Eats and Motive, and before that in consulting and investment banking. He has a Columbia BA in Economics-Math ([YC](https://www.ycombinator.com/companies/axle-health)). Co-founder **Connor Hailey** (formerly at ZocDoc and Uber) is **absent from the YC page**, so his current status needs to be checked ([healthcarediscovery.ai](https://healthcarediscovery.ai/companies/axle-health/)). Neither founder has clinical training. The CTO, clinical leadership and board are Not found. F-Prime venture partner **Julia McDowell** is the Series A investor quoted in coverage ([HHCN](https://homehealthcarenews.com/2025/05/axle-health-raises-10m-to-accelerate-ai-home-based-care-tech-development/)).

Headcount is about **25–28** (Estimated) and has been **flat after the Series A**: Simplify shows -3% over two years ([Simplify](https://simplify.jobs/c/9871b511-33dc-45fd-b3f1-5ced0aab99e6)). Axle is still hiring a **Senior Software Engineer, Interoperability** at $170–200K ([YC jobs](https://www.ycombinator.com/companies/axle-health/jobs/0cZvDZx-senior-software-engineer-interoperability)). That suggests EHR integration is still being built out.

| Round | Date | Amount | Investors | Status |
|---|---|---|---|---|
| Pre-seed | About 2020–21 | About $0.2M | YC, among others | Estimated |
| Seed | Feb 2024 | $4.2M (total raised $4.4M) | "Led by Pear VC, with an additional round led by TRAC VC" | Confirmed; one secondary source names TRAC as lead and cites a $7M figure |
| Series A | May 22, 2025 | $10M | F-Prime (lead), Y Combinator, Pear VC, Lightbank | Confirmed |
| **Total** | | **About $14.4M disclosed**; CB Insights says $14.33M, Simplify $16.8M | | Estimated range |

Sources: [HLTH](https://hlth.com/insights/news/axle-health-raises-4-2m-to-expand-home-health-care-software-2024-02-23); [Gunderson](https://www.gunder.com/en/news-insights/client-news/axle-health-announces-dollar10m-series-a-to-advance-home-health-operations); [CB Insights](https://www.cbinsights.com/company/axle-health/financials).

The About page also shows Pioneer and Soma Capital logos ([about](https://www.axlehealth.com/about)). Axle reported **about 900% (10x) growth in FY2024**, with no dollar figure ([healthcarediscovery.ai](https://healthcarediscovery.ai/companies/axle-health/)). Valuation is Not found. If runway runs 18–30 months from May 2025, Axle would **raise again around late 2026 to 2027**. That is an inference, and no 2026 round was found.

### Every product

Axle's current modules are ([axlehealth.com](https://www.axlehealth.com)):

- **AI Scheduling:** patient–clinician matching that adapts to cancellations and supports office-led or clinician-led scheduling
- **Route Optimization**
- **Real-Time Visibility:** location, adherence, coverage gaps and re-routing
- **Patient Engagement:** SMS and voice reminders, live ETAs and confirmations
- **Developer APIs**
- An "advanced scheduling module" designed to complement the EMR "without changing downstream workflows"

Earlier materials also list a **clinician mobile app** and an **operations dashboard** ([HLTH](https://hlth.com/insights/news/axle-health-raises-4-2m-to-expand-home-health-care-software-2024-02-23)). The scheduler uses traffic, credentials, patient needs and geography as inputs ([HHCN](https://homehealthcarenews.com/2025/05/axle-health-raises-10m-to-accelerate-ai-home-based-care-tech-development/)).

The website shows **Epic, athenahealth, WellSky, Statewise and Netsmart** among its integrations, and **HCHB appears in a testimonial**. Axxess, MatrixCare and KanTime are Not found.

In the Cityblock deployment, integration ran through Axle's API and "custom integration platform," and clinicians kept documenting in the EMR ([Cityblock case study](https://www.axlehealth.com/cityblock-increases-clinician-productivity)). Pricing is **based on estimated customer savings**, and each customer gets a dedicated implementation manager.

Patent status is inconsistent: the company has described the technology as both "patented" and "patent-pending." Axle has no intake or referral module and no hospice-specific workflows. Whether the generative-AI and voice engagement promised in May 2025 has shipped is Not found. The in-home testing services were discontinued in 2023.

### Customers and security

Named customers are **Cityblock Health, Penn Medicine, Imagine Pediatrics and Grand Care**. Cityblock reported a **17%+ clinician productivity gain** over three months ([case study](https://www.axlehealth.com/cityblock-increases-clinician-productivity)). The site claims 32% driving savings, 55% fewer missed visits and a 70%+ reduction in manual scheduling, all self-reported ([axlehealth.com](https://www.axlehealth.com)).

The customer base leans toward value-based care, health systems and pediatric programs, not certified hospice chains. **Compassus would likely be Axle's largest pure hospice and home health deployment.** That gives Compassus leverage over the roadmap but also concentrates implementation risk.

Axle claims SOC 2 Type II and HIPAA compliance by independent audit, pen testing, SSO/SAML and RBAC, and runs a trust portal at security.axlehealth.com. HITRUST is Not found.

## Due-diligence questions Compassus should put to each vendor

Some questions apply to all three because the same gaps recur. Each vendor should provide:

- Its **exact legal entity, state or country of formation and EIN**, checked against registry records
- The **SOC 2 Type II report** (date, auditor and scope) and a signed BAA naming the contracting entity
- A full **subprocessor and LLM list**, with where PHI is hosted and processed
- **Data-ownership and model-training terms**, including whether Compassus data trains models used for other customers
- **IP ownership and licensing for co-built features**
- **Financial statements, runway and cap table**
- **Reference calls with a hospice or Medicare home health customer running HCHB**
- Outcome claims **re-validated on Compassus's own data** before scale-up

None of the three has litigation, layoffs or negative reviews on record. That reflects thin public footprints, not a verified clean record, because no PACER or court search was run.

The table below lists the questions specific to each vendor.

| Vendor | Vendor-specific questions |
|---|---|
| **VitalisCare** | Which entity contracts and signs the BAA: VitalisCare Ltd. (Israel), Integralytic, or an undisclosed US entity? What is the formal legal and ownership link between VitalisCare Ltd. and Integralytic? Do Israel-based engineers access PHI, and under what controls? How does the HCHB integration work (API, marketplace partnership, RPA or flat files), and is Vitalis a recognized HCHB partner? What validation methodology supports Vantage's 94% accuracy and the 67% comparator, and will Vitalis run a back-test on Compassus hospice data? Which scheduling savings figure is correct, 55–65% or 30%? How many staff are dedicated to Vitalis versus shared from the studio? Who are the CTO and clinical lead? What happens to co-built IP if the studio spins it into a new startup? Who succeeds the CEO, given her roles across several companies? Has the company raised any capital, including Israeli grants? Is a home health product (OASIS, PDGM scheduling) on the roadmap? |
| **Arya Health** | What are Arya's legal entity and EIN, and did "Arya, LLC" convert to a corporation? Confirm in writing that Arya has no relationship to Yuvo, Inc. (formerly "Arya Health, Incorporated"). Does a production integration with HCHB exist, and is it read-only or read/write, and via API or RPA? Which EMRs are actually live? Which post-acute providers invested in the Series A, and do any compete with Compassus? Who are the CTO and board members? Are Bland AI, n8n, Supabase and the Gemini/Claude models covered by BAAs? How mature are the Intake and Front Desk skills, and who were the design partners? Are there hospice-specific workflows or references? What are absolute ARR and runway, now that the Series A is 12 months old? What do the renewal, price-increase and separately billed integration terms look like? |
| **Axle Health** | What are Axle's legal entity name and state, and why does no Form D exist under "Axle Health"? Is Connor Hailey still with the company, and who is the CTO? How many HCHB customers are live in production, and does the integration read and write visits? Was the HCHB testimonial from one customer or several? Can Axle encode hospice visit-frequency, IDG and on-call dispatch rules, and LUPA thresholds? Can it scale to thousands of clinicians? Has the generative-AI and voice patient engagement promised in 2025 shipped? Is the technology patented or patent-pending, and what is the patent number? Which seed figure is correct, and who led the seed? What are current ARR and runway, and is a 2026–27 raise planned? How is the savings baseline defined for ROI-based pricing? What are the SLAs, and what does the uptime history at status.axlehealth.com show? |

## Conclusion

These are three different bets, not three versions of the same one. Each vendor's weakness is something Compassus could partly offset as a large co-development partner:

- **VitalisCare** already speaks HCHB and hospice, but it would need Compassus to impose corporate discipline: a clear US contracting entity, PHI controls and IP terms that survive the studio model.
- **Arya** has the capital and the hiring momentum, but it would need Compassus to fund and validate the HCHB integration it does not yet show publicly.
- **Axle** has the most engineered integration layer and a real API, but it would need Compassus's hospice domain rules, and it would be building them with a 25-person team that may be fundraising mid-project.

The practical implication is that Compassus does not have to choose one vendor across the board. The products barely overlap: hospice clinical-ops prediction, administrative agents, and field routing. The scheduling layer is the one exception, where Vitalis Sync and Axle compete directly. Run a two-to-three-month paid pilot against a pre-agreed KPI baseline before signing any build agreement. Resolve the entity questions first, because a BAA signed with the wrong "Arya Health" or an unverified Israeli Ltd. is a defect no pilot result can fix.
