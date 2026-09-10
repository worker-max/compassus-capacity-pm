# servis.ai — research dossier

Researched 2026-09-05 · sources retrieved 2026-09-05 · confidence: **medium**

*Confidence note.* Product facts are high: the company publishes its own product documentation
openly and it was read directly, including the Scheduler docs, which is the most useful source in
this dossier. Company facts — founding, funding, leadership — are medium: they come from funding
databases and press, and the leadership page and the databases disagree about who the CEO is.
Customer and scale facts are low: no customer count, no revenue, no headcount was found, and the
review sites still file the company under its old name. Written before reading the vendor's return.

**Identity.** The questionnaire roster says *Servis.ai*. The company writes itself **servis.ai**,
lowercase, and it is **FreeAgent CRM renamed** — the same entity, founded 2016 in Campbell,
California, rebranded in or around November 2024. Review-site listings are still filed under
*FreeAgent Network* and *FreeAgent CRM*. Confirm the return's contact email domain is `servis.ai`
or `freeagentcrm.com`. There is no collision with another company of this name.

---

## At a glance

The machine-readable face of this dossier. `_research-matrix.gen.py` reads these rows to
build `Vendor-Research-Matrix.xlsx`; the prose below is the record. Bracketed numbers are
source ids from the *Sources* list at the foot of this file. *Not found* is a finding.

| Fact | Finding |
|---|---|
| **COMPANY** | |
| Founded · HQ | 2016 · Campbell, California; development office Aguascalientes, Mexico [4] [3] |
| Legal entity | servis.ai — **formerly FreeAgent CRM**, the same entity [1] [8] |
| Ownership · raised · last round | Venture · ~$19–20.2M · **$12.6M, April 2021, Pelion; nothing since** [4] [7] |
| Headcount · trend | *not found* |
| Leadership from home health | *not found* — nobody from healthcare is named anywhere [3] |
| Pivots or rebrands in 3 years | 1 — FreeAgent CRM → servis.ai, ~Nov 2024 [1] [8] |
| Home health share of business | *not found* — one landing page among a dozen verticals [1] [9] |
| **PRODUCT** | |
| HCHB evidence | *not found* |
| Other EMRs named | **none — not one EMR is named on any page** [2] [10] |
| Scheduling unit | A field rep's visit on a route [10] |
| Capacity | **Absent** — no envelope, target, discipline mix or forecast [10] |
| Scheduling | Route optimisation, three algorithms; a human picks the rep and the date [10] |
| Engagement | CRM outreach; no patient agent [2] |
| Decide or advise | **Advise** — the human assigns, the engine routes [10] |
| Clinician app | *not found* |
| **CUSTOMERS** | |
| Named home health customers | Revival Health, unsized. Mansfield Hall is not home health [2] |
| Largest known deployment | *not found* |
| Customer count | *not found* — none published at all |
| Impact figures with a baseline | **0 of 4** [2] |
| Independent customer voice | *not found* — reviews praise support, not a capability [9] |
| **TRUST AND CONTINUITY** | |
| Security attestation | *not found* — a Head of Security & Compliance is named, no attestation is [1] [3] |
| Uptime · SLA | *not found* |
| Named dependencies | none visible |
| Pricing signal | No public price; a free edition [1] |
| **THE READ** | |
| The one thing to check | It is a CRM. No episode, discipline or authorization in the data model. |
| Ask them first | Show us where an episode, a discipline, an authorization and a visit frequency live in your data model. [10] |
| Would we be their largest customer | ***not found*** — no customer count, seat count or site count is published anywhere at all [2] |
| Red flags to test | **RF-16** home health is one landing page among a dozen verticals · **RF-19** ordered treated as schedulable; no authorization or readiness state exists · **RF-07 STOP-CHECK** · RF-05 [1] [10] |
| Where their own sources disagree | **The landing page sells an “In-Home Healthcare Operations Platform”; the product documentation's objects are Rep, Customer and Route Planner** [1] [10] |
| Confidence | medium |

## One paragraph

servis.ai is a ten-year-old California software company, formerly FreeAgent CRM, that sells a
general **business operations platform** — a CRM with workflow, service and reporting bolted on,
which the company calls a Business Operations Management Platform. It has raised about $20M, most
recently $12.6M in April 2021, and has not raised since. It is not a healthcare company. It sells
the same platform to trucking, consumer services, education, financial services, media
post-production, manufacturing and distribution, and to five healthcare segments reached through
landing pages: wound care, behavioral health, in-home health, medical devices and healthcare
providers. Its Scheduler module moves a **rep** to a **customer** along an optimised route, using
three route algorithms; the objects in the data model are Rep, Customer, Appointment Profile, Route
Planner and Visit Telemetry. There is no episode, no discipline, no authorization, no visit
frequency and no clinician self-scheduling anywhere in the documentation. Two customers are named
on the in-home healthcare page, one of which is a home-based provider. Nothing connects the company
to Homecare Homebase, or to any EMR by name.

## The company

| Fact | Finding | Source · date |
|---|---|---|
| Founded | **2016**, as FreeAgent CRM, by **Dave Stephens** and a co-founder given variously as **Ryan Lott**, **Ryan Manning** and **Mohan Konyala** across three databases. **The co-founder's name does not reconcile across sources** and is written as unresolved. | [4] · [5] · [6] |
| Headquarters, offices | **Campbell, California** (headquarters) and **Aguascalientes, Mexico** (development office), plus remote. One profile lists the CEO in Bozeman, Montana. | [3] · [6] |
| Ownership and funding | Venture-backed. **Total raised ~$19–20.2M across two rounds**, the figure differing by database. **Last round: $12.6M, April 2021**, led by **Pelion Venture Partners**, with existing investor **BlueRun Ventures**. **No round since — five years and five months as of this dossier.** Valuation not found; PitchBook and Crunchbase are gated. | [4] · [5] · [6] · [7] |
| Headcount, and trend | **Not found.** No headcount figure on the site, and LinkedIn is gated. The company page shows eight named leaders. Twelve-month trend not found. | site, 2026-09-05 |
| Leadership | The company page names **Ram Dodda, CTO**; **Dave Stephens, CPO**; **Dub Price, CRO**; **Sergio Valdivia, Director of Development**; **Karan Shah, Head of Security & Compliance**; **Alan Perez, Head of Customer Support**; **Sharan Murali, Head of Quality Assurance**; **Ruth Strong, Director of Finance**. **No CEO is listed on the page.** Funding databases and LinkedIn describe Dave Stephens as CEO from November 2024; the company's own page calls him Chief Product Officer. **Nobody with a healthcare background is named anywhere.** No clinician, no home health operator, no healthcare product lead. | [3] · [6] |
| Acquisitions, mergers, pivots, rebrands | No acquisitions found. **One rebrand, recent:** FreeAgent CRM → servis.ai, announced around November 2024, positioned as an evolution "from a traditional CRM to a robust Business Operations Management Platform (BOMP)". A `servis.ai/freeagent-crm-transition/` page exists to move existing customers across. | [1] · [2] · [8] |
| Litigation, breaches, regulatory actions | **Not found.** | search, 2026-09-05 |
| Lines of business, and the share that is home health | **One product, many landing pages.** Verticals named on the site: healthcare (wound care, behavioral health, in-home health, healthcare providers), medical devices, financial services, media & post production, manufacturing & distribution. Review aggregators report the platform is "popular in Transportation/Trucking/Railroad, Consumer Services, and Education". **Home health share: not found, and there is no reason from the public record to think it is material.** | [1] · [2] · [9] |

## The product

| Fact | Finding | Source · date |
|---|---|---|
| What it does, in their words | "A business operations platform that unifies CRM, service, and internal workflows – then scales as AI streamlines every step." On the healthcare landing page: an "In-Home Healthcare Operations Platform" that connects "referrals, staffing, documentation, compliance, and supply." | [1] · [2] |
| What it does, in a customer's words | Testimonials on the site are about the vendor, not the product: "outstanding in terms of customization, service, interface, simplicity and elegance"; "truly transformational for our Admissions Department". Review sites echo this — the consistent praise is for **customer support and configurability**, not for a capability. **No customer conference talk, panel or independent interview found.** | [1] · [2] · [9] |
| Capacity, scheduling, engagement — which arenas the public material covers | Read the Scheduler documentation, not the landing page. **Capacity: absent.** No capacity envelope, no productivity target, no discipline mix, no availability planning beyond a rep's shift times and skills. **Scheduling: present, and built for field service.** A *Follow-up Request* is approved into an *Appointment Pool* — "a visit request that is ready to be scheduled… a service that needs to happen at a specific location on a specific date". A human scheduler opens the Route Planner, picks a rep and a date, and applies a system-generated route. Three route algorithms — Shortest Route, Nearest Neighbor, Farthest Neighbor — plus an Auto mode. Inputs are rep lat/long, shift times and skills; customer lat/long and visit notes; and a service profile giving duration and virtual-or-in-person. **Engagement: CRM-shaped.** Outreach exists because it is a CRM; there is no patient outreach, confirmation or intake agent. | [10] |
| Evidence of an HCHB integration | **Not found.** No HCHB mention on any page, in any release, in any job posting. The site's only integration statement is "integrates with your existing systems or runs standalone". | search + site, 2026-09-05 |
| Other EMR integrations named | **None named anywhere.** Not one EMR, EHR, EVV or billing system is named on the healthcare pages. | [2] · [10] |
| Agentic or automated patient outreach | **Claimed in the abstract, not evidenced.** "PRM-driven engagement that automates interactions for better hiring, onboarding, and documentation." *PRM* is the CRM word with the noun swapped. No voice agent, no named channel behaviour, no volume figure. | [2] |
| Clinician-facing app | **Not found** in the Apple App Store or Google Play under servis.ai or FreeAgent. The Scheduler documentation describes *Visit Telemetry* and real-time visit tracking, which implies a mobile client, but no listing was located. | search, 2026-09-05 |
| Pricing signals | No public pricing. "Book a demo" or a **free edition**. A free edition is a self-serve, small-business go-to-market signal. | [1] |
| Security and continuity | **Karan Shah, Head of Security & Compliance**, is named, which is more than most vendors of this size publish. **But no SOC 2, HITRUST, ISO or HIPAA attestation was found on the site**, and no uptime figure, SLA or status page. The badges on the home page are G2, Capterra and GetApp performance badges, not security attestations. | [1] · [3] |

## The customers

| Fact | Finding | Source · date |
|---|---|---|
| Named home health customers, with size | **One, arguably.** **Revival Health** appears on the in-home healthcare page with a testimonial and a "watch their story" link. Size not found. **Mansfield Hall** is also named — it is a supported-living and college-transition programme for young adults, not a home health agency. The "Admissions Department" testimonial fits Mansfield Hall, not a home health agency. | [2] |
| Largest known deployment | **Not found.** No customer count, no seat count, no site count anywhere. | search, 2026-09-05 |
| Customers lost or churned | **Not found.** | search, 2026-09-05 |
| Case studies — what was measured, period, baseline | Four figures on the in-home healthcare page, **all four without period, baseline, site count or method**: "30% more referrals", "50% faster intake", "50% shorter onboarding", "40% less admin time". No case study document behind any of them. | [2] |

## What the outside view says about the questionnaire

Written 2026-09-05, before reading the return.

- **A1.** Expect no HCHB integration and expect no EMR named. The public record names none, and the
  product's own documentation describes a standalone system of record — a CRM — that would sit
  *beside* HCHB, not inside it. The natural rung is *Will build*. Watch **RF-01** if the return
  claims more, and watch **RF-02** hard: this product owns its own schedule object, so the question
  of which system owns the schedule when both change is not hypothetical here, it is structural.
- **A2.** No customer count, no seat count, no home health customer of scale in the public record.
  **RF-16** on the first half is near-certain: home health is one landing page among a dozen
  verticals that include trucking and education. Expect **RF-06** if references are hedged; there
  is exactly one plausible home-based reference in public, and it is unsized.
- **A3.** Four percentages, no baselines, no periods. **RF-05** as written. If the return repeats
  these four numbers, ask which customer each came from.
- **B versus C.** This is the vendor most likely to trip **RF-04**. A configurable platform can
  answer *Yes* to almost every capability question in Section B truthfully-in-principle, because
  anything can be built on it. Believe Section C. And expect **RF-08** — *configurable* is this
  product's actual value proposition, and the reviews confirm it is what customers buy.
- **C3, C5.** The Scheduler documentation has no readiness state, no authorization, no compliance
  window, and no escalation path when nobody takes a visit. **RF-19** and **RF-20** should be
  assumed until the demo shows otherwise.
- **C6.** No attestation, no uptime, no SLA found. **RF-07** unless the return supplies a figure and
  a commitment.
- **E2.** Ten years old, $20M raised, nothing new since April 2021, one rebrand in the last two
  years. A partnership conversation is possible but the more useful question is whether home health
  is a vertical they are committing to or a landing page they are testing.
- **Who wrote this.** If the return is fluent about workflow, configurability, automation and
  reporting, and vague about episodes, disciplines, LUPA, recertification and authorization, that is
  not a bad author — that is the company. There is no clinician and no home health operator on the
  leadership page.

*Second pass after reading the return: to be added below, dated.*

## Durability read — evidence only

- Age ten years. One rebrand, in the last two years, from CRM to "business operations platform".
- Capital: about $20M, last raised April 2021. **No new capital in five years.** Either it is
  profitable and self-sustaining, or it is thin; the public record does not say which.
- Main business: a horizontal platform. Healthcare is one of six or seven verticals reached by
  landing page; in-home health is one of four sub-pages inside healthcare. Review aggregators place
  the customer base in trucking, consumer services and education.
- Concentration: unknown. No customer count was found at all, which is itself unusual for a
  ten-year-old venture-backed SaaS company.
- Our size against theirs: unknown, and that is the finding. A vendor who publishes no customer
  count, no headcount and no revenue cannot be checked against **RF-16**'s second half.
- Leadership: a full functional bench — CTO, CPO, CRO, security, support, QA, finance — and **no
  named CEO on their own company page**, with databases and the site disagreeing on Dave Stephens's
  title. Nobody from healthcare.
- Dependency: none visible. The product appears to be theirs.
- The scheduler is a real, working, documented route-optimisation engine. It was built for field
  service. That is a durability fact as much as a fit fact: it will keep being built for field
  service, because that is where the customers are.

## Questions the research raises

For the demo or the reference call. One line each.

1. Who is the CEO? Your company page lists a CTO, a CPO and a CRO, and no chief executive.
2. How many customers do you have, how many are in healthcare, and how many are Medicare-certified home health agencies?
3. Name every EMR you are live with today and the customer who will confirm each one.
4. In your data model, where does an *episode* live? A *discipline*? An *authorization*? A *visit frequency*? Show the schema.
5. Your Scheduler moves a *rep* to a *customer*. What changes when the rep is an RN with a caseload, a territory and a productivity target?
6. What happens to a visit whose authorization arrives after the compliance window has opened?
7. Walk the next thirty minutes after a broadcast visit is offered and nobody takes it.
8. When a scheduler moves a visit in the EMR and your engine has already moved it, who wins and who is told?
9. Give the period, baseline and customer behind "30% more referrals", "50% faster intake", "50% shorter onboarding" and "40% less admin time".
10. Who is Revival Health, how many clinicians do they schedule on your platform, and will they take a reference call?
11. What is your security attestation, your trailing-twelve-month uptime, and what does the contract commit to?
12. You last raised in April 2021. Are you profitable, and what is home health's place in the 2027 roadmap?
13. Has anyone on your team worked in home health, home care or hospice? Name them.

## Not found

Looked for and not found, so nobody looks again (as of 2026-09-05):

- Any mention of Homecare Homebase or HCHB.
- Any EMR, EHR, EVV or billing system named on any page.
- A headcount, a customer count, a revenue figure or an ARR figure.
- A clinician or field mobile app in the Apple App Store or Google Play.
- SOC 2, HITRUST, ISO or an explicit HIPAA attestation on the site.
- An uptime figure, SLA or status page.
- Litigation, breaches or regulatory actions.
- A named CEO on the company's own page.
- A healthcare-experienced person anywhere in the named leadership.
- Any concept of episode, discipline, authorization, visit frequency, LUPA, OASIS or
  recertification in the product documentation.
- Any customer speaking independently at a conference or in an interview.
- Public pricing.

## Gated

Written as gated, not as not found:

- PitchBook and Crunchbase company profiles (funding history, valuation, headcount trend).
- LinkedIn company page (headcount and twelve-month trend).
- The full Capterra, GetApp and SoftwareAdvice review sets, which are filed under *FreeAgent
  Network* and would give the industry mix of the customer base if read in bulk.

## Sources

Retrieved 2026-09-05. "Read" means the page was opened directly this session.

1. servis.ai, home page. Product description, verticals, testimonials, badges, free edition. Read.
2. servis.ai/in-home-healthcare/. The healthcare landing page: "In-Home Healthcare Operations Platform", four impact percentages, Revival Health and Mansfield Hall testimonials, "integrates with your existing systems or runs standalone". Read.
3. servis.ai/company/. Leadership (eight named), Campbell CA and Aguascalientes MX, mission and values. Read.
4. LinkedIn Pulse / PRWire, "FreeAgent CRM Rebrands to Servis.ai to Transform Customer-Facing Operations with AI-Powered Insights", 2024. The rebrand release.
5. Tracxn, "FreeAgent CRM — 2026 Company Profile, Team, Funding & Competitors", and its founders-and-board page. Founded 2016; founders Dave Stephens and Ryan Lott / Mohan Konyala (sources disagree).
6. Crunchbase, "Dave Stephens — CEO & Co-Founder @ FreeAgent CRM" person profile; SignalHire and RocketReach profiles giving CEO of servis.ai from Nov 2024, Bozeman MT. Partially gated.
7. BlueRun Ventures, "Servis.ai" portfolio page; Pelion Venture Partners as April 2021 lead; total raised given as $19.0M by one source and $20.2M by another.
8. servis.ai/freeagent-crm-transition/. The customer-migration page confirming the rebrand is the same entity.
9. Capterra, GetApp, SoftwareAdvice and Cuspera listings for "servis.ai (formerly FreeAgent CRM)", filed under *FreeAgent Network*. Industry mix: "popular in Transportation/Trucking/Railroad, Consumer Services, and Education"; segments Small Business, Mid Market, Large Enterprise. Reviews consistently praise support and configurability.
10. **servis.ai/docs/scheduler/.** The Scheduler product documentation: Appointment Pool, Follow-up Requests, Events, Rep, Customer, Appointment Profile, Schedule, Schedule Item, Visit Telemetry, Route Planner, Route Agenda, Route Calendar, Route Timeline; Shortest Route / Nearest Neighbor / Farthest Neighbor / Auto. **Read directly; the most load-bearing source here.**
11. servis.ai/blog, "The Shift from Hospital to Home: Revolutionizing Wound Care". Marketing content, used only as evidence of the vertical strategy.
12. PitchBook, servis.ai company profile. Gated.
