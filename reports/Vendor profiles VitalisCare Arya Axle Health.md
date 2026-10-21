---
title: "Vendor Profiles: VitalisCare, Arya Health, Axle Health"
subtitle: "Partner due diligence — prepared October 2026"
---

# Scope and method

- Public-source research on three home health / hospice software vendors as potential product-build partners.
- Sources: company websites, press releases, SEC EDGAR, trade press (Home Health Care News, Hospice News, HomeCare Magazine), Y Combinator, aggregators.
- Crunchbase, PitchBook, Tracxn and LinkedIn blocked access; figures from those sites come from search snippets only.
- No court-records (PACER) search was run.
- Labels: **Confirmed** = stated in a cited source. **Vendor claim** = company's own marketing, not independently verified. **Estimated** = aggregator figure, inference, or conflicting sources. **Not found** = searched, not located.

# Summary comparison

| | VitalisCare | Arya Health | Axle Health |
|---|---|---|---|
| Website | vitaliscare.ai | aryahealth.ai (app: app.aryaworks.com) | axlehealth.com |
| Legal entity | VitalisCare Ltd., Jerusalem, Israel (Confirmed). US entity: Not found | Possibly "Arya, LLC" (Estimated) | Possibly "Axle Health, Inc." (Estimated) |
| HQ | Jerusalem (legal address); parent studio in Lakewood, NJ (Estimated) | New York City | Santa Monica / Los Angeles |
| Founded | ~2024–25 (Estimated); parent studio ~2020 | ~2022 (Estimated) | 2020 (Confirmed) |
| CEO | Dr. Dina Yankelewitz | Kunal Sarda | Adam Stansell |
| Headcount | 11–50 (Estimated) | Not disclosed | ~25–28, flat (Estimated) |
| Total funding | None disclosed | ~$25M (Confirmed) | ~$14.4M disclosed; aggregators $14.3M–$16.8M |
| Last round | None found | $18.2M Series A, Oct 2025, led by ACME Capital | $10M Series A, May 2025, led by F-Prime |
| Revenue | Not disclosed; parent studio ~$1M (Estimated, low confidence) | Not disclosed; claims >6x growth to Oct 2025 | Not disclosed; claims >$1M ARR within 12 months of 2023 launch, ~10x growth FY2024 |
| Care segments | Hospice only | Home health, home care, hospice, pediatrics, private duty | Home health, health systems, pediatrics, value-based care, other field care |
| Product type | 7 hospice AI apps | AI agent with 8 administrative skills | Scheduling, routing, dispatch, patient engagement, APIs |
| HCHB integration | Named; claims "fully integrated" (Vendor claim) | None named | HCHB appears in a customer testimonial; depth unknown |
| Other EMRs named | None | None | Epic, athenahealth, WellSky, Netsmart, Statewise |
| Public API | Not found | Not found | Yes (developers.axlehealth.com) |
| Security | HIPAA, SOC 2 Type II (Vendor claim; no report linked) | SOC 2 Type I & II, HIPAA, pen tests, Trust Center (Vendor claim) | SOC 2 Type II, HIPAA, pen tests, SSO/SAML, trust portal (Vendor claim) |
| HITRUST | Not found | Not found | Not found |
| Named customers | Moments Hospice, Anchor Hospice | TheKey, Team Select Home Care, Thrive Skilled Pediatric Care, Connect Pediatrics | Cityblock Health, Penn Medicine, Imagine Pediatrics, Grand Care |
| Pricing | Per patient census; no setup fee; auto-renew | Not disclosed; integration billed separately (Estimated) | Based on estimated customer savings |

**Common facts across all three**

- All sell software that sits on top of the EMR. None replaces Homecare Homebase.
- None names a large Medicare-certified hospice or home health chain as a customer.
- Performance results are almost entirely self-reported.
- Each has a name-collision or legal-entity question that must be resolved before a BAA or contract.

# VitalisCare

## Identity and structure

- Brand: Vitalis Care. Website: vitaliscare.ai.
- Legal entity per privacy policy (updated March 24, 2025): **VitalisCare Ltd.**, Divrei Khayim 14, Jerusalem, Israel. No US state of incorporation listed. ([Privacy Policy](https://vitaliscare.ai/privacy-policy/))
- Portfolio company of **Integralytic**, a healthtech venture studio. Integralytic builds products, then raises funding after an MVP. ([Integralytic](https://integralytic.com/))
- Integralytic's other companies: DolphinCare (SNF MDS/reimbursement), 1Dose, Exclugo.
- Integralytic location: Lakewood, NJ; founded ~2020 (Estimated, directory sites).
- No US subsidiary, Israeli registration number, or formal Ltd.–studio relationship found.

## Name collisions ruled out

- Vitalis Care (France) — Marseille home care provider; owns the "vitalis-care" LinkedIn page.
- VitalCaring Group — US home health/hospice operator, not a vendor.
- Vitalis Health and Home Care — Australian care provider.
- Vali Health — separate home care AI startup ($6M raised).
- Other "Vitalis" records on PitchBook/Tracxn — different companies; their funding data does not apply.

## History

| Date | Event |
|---|---|
| ~2020 | Integralytic founded (Estimated) |
| ~2024–25 | Vitalis Care launched |
| Jul 16, 2025 | CEO on Husch Blackwell hospice AI podcast; said company started with scheduling, compliance and reimbursement |
| Aug 19, 2026 | Nominated for Hospice News Product of the Year (community vote). Press release says company "began as a single end-of-life prediction tool"; now seven apps. Outcome of award: Not found |

- Observation: the two accounts of which product came first conflict.

## Leadership

- **Dr. Dina Yankelewitz** — founder and CEO. Doctorate in mathematics education; former professor; prior work at Pearson; data analytics/AI. Also founder of Integralytic and CEO of 1Dose (Estimated).
- No hospice operator or EHR vendor background disclosed.
- CTO, clinical lead, board, advisors: Not found. Product pages say built with "hospice clinical leaders, medical directors, and HCHB operations experts" — none named.

## Size and financials

- Headcount: Crunchbase 11–50 (Estimated). Integralytic: ZoomInfo 1–10; RocketReach 41; Integralytic self-claims "150+".
- Funding rounds, investors, valuation, grants: Not found.
- SEC EDGAR: zero Form D filings for "Vitalis Care." An Israeli Ltd. could raise capital without a US filing.
- Revenue: Integralytic ~$1M (Estimated, low confidence).

## Products (7 apps, 4 suites)

| Suite | App | Function | Claims |
|---|---|---|---|
| Care | **Vantage** | Flags patients likely to die within 7–10 days; refreshes every 10 minutes | 94% accuracy vs ~67% "typical EMR tools" (no source); "50+ billion clinical signals"; "fully integrated" with HCHB |
| Care | **Ray** | HOPE assessment timeline tracking; flags missed SFVs and overdue HUVs | Anchor Hospice: 97–99% HOPE compliance, ~1.5 hrs saved per morning |
| Coordination | **Sync** | AI visit scheduling with human approval; includes original HCHB schedule view | Homepage: 55–65% less drive time. Sync page: ~30%. Inconsistent |
| Coordination | **Sync360** | Field staff app; GPS mileage tracking; mileage fraud detection | — |
| Compliance | **Align** | Scans documentation for compliance gaps | "Prevents up to 90% of audit denials" |
| Compliance | **Guide** | Bedside documentation prompts; voice-to-text | — |
| Collaboration | **Bridge** | Hospice–SNF room-and-board reconciliation dashboard | Payment turnaround 30–60 days → 6–14 days |

- No home health product.
- No EMR named other than HCHB. No public API.
- Pricing: per patient census, no setup fees, auto-renewing.

## Customers

- **Moments Hospice** — Director of HCHB Operations quoted on homepage.
- **Anchor Hospice** — Ray case study.
- Other testimonials use initials only. No customer count or census figures published.

## Security

- Claims HIPAA and SOC 2 Type II. No report or trust center linked.
- HITRUST, ONC certification, hosting region, subprocessor list: Not found.

## Observations

- Closest functional match to Compassus hospice operations on HCHB.
- Least corporate transparency of the three: foreign legal entity, no disclosed funding, one named executive who also runs other portfolio companies.
- Possible PHI access from Israel; not addressed publicly.
- Studio model creates IP-ownership risk if products are spun into new companies.
- Headline accuracy and savings figures are unsourced or inconsistent.

# Arya Health

## Identity and structure

- Brand: "Arya." Websites: aryahealth.ai; app at app.aryaworks.com. New York City.
- Builds AI agents for administrative work at home health, home care and hospice providers. ([PR Newswire](https://www.prnewswire.com/news-releases/arya-health-secures-18-2m-series-a-to-power-the-next-generation-of-ai-agents-for-post-acute-care-administration-302597627.html))
- Founded ~2022 (Estimated). Named after founder's daughter.
- Legal entity: possibly "Arya, LLC" (Estimated, from seed-round listing). A priced Series A normally requires a C-corp, so the current entity may differ.
- No SEC Form D found for Arya's own entity. Not a Y Combinator company.

## Name collisions ruled out

- **Yuvo, Inc.** (CIK 0001907652) — unrelated Delaware company in NYC whose SEC filings list its former name as **"Arya Health, Incorporated."** CEO Cesar Herrera. Form Ds: $8.17M (2024), $4.26M (2026). **These filings are not Arya's.** Highest-risk collision in this report.
- ARYA Sciences SPACs and other "Arya" EDGAR filers.
- Arya.ag (India, agriculture); Arya Home Healthcare LLC (Virginia care provider); Arya by Leoforce (recruiting AI); Arya.ai (banking AI).
- "Arya, Philadelphia" on VCBacked — same investors as Arya Health's seed; probably a duplicate record with wrong city.

## History

| Date | Event |
|---|---|
| ~2022 | Founded (Estimated) |
| Sep 2024 | $4M seed; positioned as "healthcare workforce automation platform" (scheduling, payroll, onboarding, compliance) |
| Oct 29, 2025 | $18.2M Series A; repositioned as AI "system of action"; Intake Agent announced with design partners |
| Jan 2026 | Launched free Emergency Response Agent nationwide |
| Apr 2026 | Connect Pediatrics results published |
| 2026 | MedTech Breakthrough Award |

## Leadership

- **Kunal Sarda** — CEO and co-founder (Confirmed). Per aggregators: co-founded VerbalizeIt (appeared on Shark Tank; acquired by Smartling 2016); Smartling through 2020; Wharton MBA (Estimated).
- "Arunram Kalaiselvan" listed as co-founder by one aggregator only; uncorroborated.
- **Melinda Phillips** — leads Care@Home Center of Excellence; former CEO of Thrive Skilled Pediatric Care (acquired by Aveanna).
- CTO, full executive team, board: Not found. ACME partner Aike Ho (Series A lead) is a likely board member — not confirmed.

## Size and financials

- Headcount: Not disclosed.
- Open roles (Oct 2026), all in-person NYC: enterprise customer success lead, principal platform engineer, deployment specialist.

| Round | Date | Amount | Investors | Status |
|---|---|---|---|---|
| Pre-seed / angel | Before 2024 | ~$2.8M (implied) | Likely Ridge, Oceans | Estimated |
| Seed | Sep 2024 | $4.0M | Twelve Below (lead), Nebular, Oceans, Ridge; VCBacked also lists f7 Ventures, Operator Partners | Confirmed (additions Estimated) |
| Series A | Oct 29, 2025 | $18.2M | ACME Capital (lead), Ridge, Twelve Below, OpenAI executives, unnamed "leading post-acute care providers" | Confirmed |
| **Total** | | **~$25M** | | Confirmed |

- Revenue: Not disclosed. Claims >6x growth in 12 months to Oct 2025, "pacing toward 10x."
- Valuation: Not found.
- Some Series A investors are post-acute providers — possibly Compassus competitors.

## Products

"One Agent with eight skills":

| Skill | Function | Claims |
|---|---|---|
| Scheduling | Shift/visit scheduling and fill | Connect Pediatrics: +25% scheduler capacity, no added headcount |
| Compliance | License/credential tracking | Deploys in under a week |
| Talent | Recruiting | 60% less recruiting effort |
| Onboarding | New-hire onboarding | 50% faster time-to-first-staffing; 70% less admin work |
| Intake | Referral intake | Newer; launched with design partners |
| Payroll | Payroll support | — |
| Engagement | Caregiver/patient outreach | — |
| Front Desk | Inbound calls and messages | Newer |

- Plus a free **Emergency Response Agent**: local number per location, triages after-hours calls/texts, escalates to on-call staff; no access to detailed medical histories.
- Modes: co-pilot or autopilot. Channels: text, voice, email. Audit trails.
- Integration: claims read/write to "EMRs, ATS, HRIS in near-real time" — **names no EMR**. One aggregator reports "no verified bidirectional EHR connection."
- Underlying tech (aggregator, Estimated): Google Gemini; earlier Anthropic Claude via AWS Bedrock. Subprocessors: Supabase, Cloudflare, Bland AI (voice), n8n.
- No clinical documentation, OASIS, coding, or hospice-specific workflows (IDG, HOPE, bereavement).

## Customers

- TheKey, Team Select Home Care, Thrive Skilled Pediatric Care, Connect Pediatrics.
- No Medicare-certified hospice or home health customer named.

## Security and contract terms

- Claims SOC 2 Type I and II, HIPAA, annual pen tests, Trust Center. BAAs offered; SOC 2 report under NDA (aggregator).
- Reported terms (Estimated): 30-day auto-renewal notice; 60-day notice for price increases; integration work billed separately.

## Observations

- Best funded and best documented of the three.
- Product is administrative only; furthest from Compassus clinical and HCHB workflows.
- Integration with HCHB, or any named EMR, is unproven publicly.
- Customer base skews to home care and pediatrics.
- Yuvo/"Arya Health, Incorporated" collision must be cleared in writing before contracting.

# Axle Health

## Identity and structure

- Axle Health, axlehealth.com. Santa Monica / Los Angeles. Founded 2020. Y Combinator Winter 2021. ([YC](https://www.ycombinator.com/companies/axle-health))
- Law firm: Gunderson Dettmer.
- Legal name "Axle Health, Inc." appears only on a third-party listing (Estimated). No Form D under "Axle Health" — likely files under a different legal name.
- Website footer misspells name as "Axle Heath."

## Name collisions ruled out

- Axle (open-insurance API company); Axle (bank corporate-access software); "Axel Health" on CB Insights.

## History

| Date | Event |
|---|---|
| 2020 | Founded |
| 2020–21 | Services business: own phlebotomists, MAs and nurses doing in-home COVID testing for telehealth companies; largest partner Sameday Health |
| 2021–22 | Expanded to 50-state in-home visit network; "a couple million dollars" revenue |
| Winter 2021 | Y Combinator |
| 2023 | Shut down services business; began selling internal scheduling/dispatch tool as SaaS |
| ~2024 | Passed $1M ARR within 12 months of software launch (secondary source) |
| Feb 2024 | $4.2M seed |
| May 22, 2025 | $10M Series A |

## Leadership

- **Adam Stansell** — founder and CEO. Prior: Uber Eats, Motive, consulting, investment banking. Columbia BA, Economics-Math.
- **Connor Hailey** — co-founder per third-party source (prior: ZocDoc, Uber). Not on YC page; current status unknown.
- Neither founder has clinical training.
- CTO, clinical leadership, board: Not found.
- F-Prime venture partner Julia McDowell quoted on Series A.

## Size and financials

- Headcount ~25–28 (Estimated); Simplify shows -3% over two years.
- Hiring Senior Software Engineer, Interoperability ($170–200K) — EHR integration still being built.

| Round | Date | Amount | Investors | Status |
|---|---|---|---|---|
| Pre-seed | ~2020–21 | ~$0.2M | Y Combinator and others | Estimated |
| Seed | Feb 2024 | $4.2M (total to date $4.4M) | Press release: "led by Pear VC, with an additional round led by TRAC VC." One secondary source names TRAC as lead and cites $7M | Confirmed; conflicting secondary |
| Series A | May 22, 2025 | $10M | F-Prime (lead), Y Combinator, Pear VC, Lightbank | Confirmed |
| **Total** | | **~$14.4M disclosed**; CB Insights $14.33M; Simplify $16.8M | | Estimated range |

- About page also shows Pioneer and Soma Capital logos.
- Revenue: Not disclosed beyond $1M ARR milestone; ~900% growth FY2024 (Vendor claim).
- Valuation: Not found.
- No 2026 round found. Based on typical 18–30 month runway, a new raise around late 2026–2027 is likely (inference).

## Products

| Module | Function |
|---|---|
| **AI Scheduling** | Patient–clinician matching; adapts to cancellations; office-led or clinician-led; inputs include traffic, credentials, patient needs, geography |
| **Route Optimization** | Optimized daily routes; live re-routing |
| **Real-Time Visibility** | Clinician location, adherence, coverage gaps |
| **Patient Engagement** | SMS and voice reminders, live ETAs, confirmations |
| **Clinician mobile app** | Field-staff app |
| **Operations dashboard** | Office view |
| **Developer APIs** | Public docs at developers.axlehealth.com |
| **Advanced scheduling module** | Complements EMR "without changing downstream workflows" |

- Integrations named: Epic, athenahealth, WellSky, Statewise, Netsmart. HCHB appears in a testimonial. Axxess, MatrixCare, KanTime: Not found.
- Cityblock deployment used Axle API and "custom integration platform"; clinicians kept documenting in EMR.
- Pricing based on estimated customer savings; dedicated implementation manager per customer.
- Patent status described both as "patented" and "patent-pending."
- No intake/referral module. No hospice-specific workflows.
- Generative-AI and voice engagement promised May 2025: shipped status Not found.
- Discontinued: in-home testing / visit services (2023).

## Customers

- Cityblock Health (17%+ clinician productivity gain over three months, case study), Penn Medicine, Imagine Pediatrics, Grand Care.
- Site-wide claims (Vendor claim): 32% driving savings, 55% fewer missed visits, 70%+ less manual scheduling.

## Security

- Claims SOC 2 Type II and HIPAA (independent audit), pen testing, SSO/SAML, role-based access. Trust portal: security.axlehealth.com. Status page: status.axlehealth.com.
- HITRUST: Not found.

## Observations

- Most developed scheduling/routing engine and integration layer of the three; only one with public APIs.
- Directly relevant to the capacity and scheduling initiative.
- Customer base is value-based care, health systems and pediatrics — not certified hospice chains. Compassus would likely be its largest home health/hospice deployment: more influence on roadmap, more implementation risk.
- Hospice and home health rules (OASIS, LUPA thresholds, IDG, on-call) unproven.
- Small, flat team; may be fundraising during a build.
- Minor inconsistencies in public figures (seed amount, patent status).

# Overlap between vendors

- Scheduling is the only area where products compete directly: VitalisCare Sync vs. Axle Health.
- Otherwise the products do not overlap: hospice clinical-operations prediction (VitalisCare), administrative AI agents (Arya), field scheduling and routing (Axle).

# Due-diligence questions

## For all three vendors

- Exact legal entity, state/country of formation, EIN — verify against registry records.
- SOC 2 Type II report (date, auditor, scope) and BAA naming the contracting entity.
- Full subprocessor and LLM list; where PHI is hosted and processed.
- Data ownership and model-training terms — does Compassus data train models used for other customers?
- IP ownership and licensing for co-built features.
- Financial statements, runway, cap table.
- Reference calls with a hospice or Medicare home health customer running HCHB.
- Re-validation of outcome claims on Compassus data before scale-up.
- Litigation history (no court search was run for this report).

## VitalisCare

- Which entity contracts and signs the BAA: VitalisCare Ltd. (Israel), Integralytic, or a US entity?
- Formal ownership link between VitalisCare Ltd. and Integralytic.
- Do Israel-based staff access PHI? Under what controls?
- How does the HCHB integration work (API, partner program, RPA, flat files)? Is Vitalis an official HCHB partner?
- Validation method behind Vantage 94% accuracy and the 67% comparator. Willing to back-test on Compassus data?
- Which drive-time figure is correct: 55–65% or 30%?
- Staff dedicated to Vitalis vs. shared from the studio. Who are the CTO and clinical lead?
- What happens to co-built IP if the studio spins it out?
- CEO succession, given roles across multiple companies.
- Any capital raised, including Israeli grants?
- Home health product (OASIS, PDGM) on the roadmap?

## Arya Health

- Legal entity and EIN; did "Arya, LLC" convert to a corporation?
- Written confirmation of no relationship to Yuvo, Inc. (formerly "Arya Health, Incorporated").
- Is there a production HCHB integration? Read-only or read/write? API or RPA? Which EMRs are live?
- Which post-acute providers invested in the Series A? Any Compassus competitors?
- CTO and board members.
- Are Bland AI, n8n, Supabase and the LLM providers covered by BAAs?
- Maturity of Intake and Front Desk skills; who were the design partners?
- Any hospice-specific workflows or hospice references?
- Current ARR and runway.
- Renewal, price-increase and integration-billing terms.

## Axle Health

- Legal entity name and state; why no Form D under "Axle Health"?
- Is Connor Hailey still with the company? Who is the CTO?
- How many HCHB customers live in production? Does the integration read and write visits? Was the HCHB testimonial one customer or several?
- Can it encode hospice visit frequency, IDG, on-call dispatch, and LUPA thresholds?
- Can it scale to thousands of clinicians?
- Has the generative-AI / voice patient engagement shipped?
- Patented or patent-pending? Patent number.
- Correct seed amount and lead investor.
- Current ARR, runway, and 2026–27 fundraising plans.
- How the savings baseline is defined for ROI-based pricing.
- SLAs and uptime history (status.axlehealth.com).

# Recommended next steps

1. Resolve legal entity for each vendor before any BAA or NDA exchange.
2. Request SOC 2 Type II reports and subprocessor lists.
3. Request HCHB integration technical documentation and live HCHB customer references.
4. Run a paid pilot (2–3 months) against a pre-agreed KPI baseline before any build agreement.
5. Run a court-records and UCC lien search on each entity.
