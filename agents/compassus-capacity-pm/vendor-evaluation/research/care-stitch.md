# CareStitch — research dossier

Researched 2026-09-05 · sources retrieved 2026-09-05 · confidence: **medium**

*Confidence note.* Product facts are high: the site, the app listings and a dated press release were
read directly, and the product is described in the right vocabulary for our problem. Company facts
are medium: the founding year, location, founder and bootstrapped status agree across three
databases and an industry-association listing, but the only revenue figure found is five years old
and the headcount comes from database bands rather than a count. Customer facts are **low**: not one
customer is named anywhere, and the site's testimonials are unreplaced template placeholders.
Written before reading the vendor's return.

**Identity.** The questionnaire roster says *Carestitch*. The company writes itself **CareStitch**
and files as **CareStitch, Inc.**, San Diego, California. Site `carestitch.com`; app package
`com.carestitch.clinician_app`. Founder and CEO **Peter Yang**; COO **Shelley Ackerman, PT, DPT**.
Confirm the return's contact email domain is `carestitch.com`. **No close name collisions were
found** — CareStar, Caremark and CareSource are unrelated and will not be confused by anyone
reading carefully.

---

## At a glance

The machine-readable face of this dossier. `_research-matrix.gen.py` reads these rows to
build `Vendor-Research-Matrix.xlsx`; the prose below is the record. Bracketed numbers are
source ids from the *Sources* list at the foot of this file. *Not found* is a finding.

| Fact | Finding |
|---|---|
| **COMPANY** | |
| Founded · HQ | 2019 · San Diego, California [7] [8] [9] |
| Legal entity | CareStitch, Inc. [6] |
| Ownership · raised · last round | **Bootstrapped — $0 raised.** $143K revenue in 2021, nothing since [9] |
| Headcount · trend | **4** (Apr 2026) · 2 in 2021 [8] [9] |
| Leadership from home health | **Yes — COO Shelley Ackerman, PT, DPT** [2] [6] |
| Pivots or rebrands in 3 years | **None — the only vendor on the roster that has never repositioned** |
| Home health share of business | All of it, since 2019 [10] [1] |
| **PRODUCT** | |
| HCHB evidence | *not found* |
| Other EMRs named | WellSky — once, in a blog post, with no mechanism [11] |
| Scheduling unit | A visit for a patient [1] |
| Capacity | **The most on the roster, and still thin** — MAPS forecasts visit volume by region and shows under- and over-utilised areas; overtime exposure [2] [1] |
| Scheduling | Real — assess, dispatch, assign; broadcast to eligible clinicians; drive-time optimisation [1] |
| Engagement | Clinician-side only; no patient capability [3] |
| Decide or advise | **Advise** — the scheduler dispatches, the clinician accepts what fits [1] [3] |
| Clinician app | Android 3.12 · 25 ratings · ~3,500 lifetime installs · iOS 3.3 · 22 ratings [4] [5] |
| **CUSTOMERS** | |
| Named home health customers | **none named anywhere** |
| Largest known deployment | *not found* — bounded by ~3,500 lifetime installs across all customers [4] |
| Customer count | *not found* |
| Impact figures with a baseline | **0 of 1** — “a 60% drop in missed visits”, no agency, period or baseline [11] |
| Independent customer voice | App-store reviews only — one agency, nearly three years, “our agency's infrastructure” [4] [5] |
| **TRUST AND CONTINUITY** | |
| Security attestation | HIPAA claimed; **nothing else found** [1] |
| Uptime · SLA | *not found* |
| Named dependencies | none visible |
| Pricing signal | *not found*; $143K revenue in 2021 implies small agencies [1] [9] |
| **THE READ** | |
| The one thing to check | Four employees. We would be larger than everything they have ever done. |
| Ask them first | We are about three thousand clinicians and there are four of you. Name one customer, and tell us what you would do differently at our size. [8] |
| Would we be their largest customer | **Yes, overwhelmingly.** Everything they have ever run is bounded by about 3,500 lifetime app installs across all customers [4] [8] |
| Red flags to test | **RF-06 STOP-CHECK** not one customer is named anywhere · **RF-16** we would be their largest by orders of magnitude · **RF-07 STOP-CHECK** · RF-05 [1] [4] |
| Where their own sources disagree | *none found* — one impact figure and no counts to contradict. **But the site's testimonials are unreplaced template placeholders with fictional names** [1] |
| Confidence | medium |

## One paragraph

CareStitch is a seven-year-old, **bootstrapped, four-person** San Diego company that sells exactly
one thing: scheduling and dispatch for home health and hospice agencies, sitting beside the agency's
EMR rather than replacing it. It is the only vendor on this roster whose product was built for our
problem and nothing else — the vocabulary is visits, clinicians, regions, drive time, case requests
and broadcast, and the founding COO is a practising-background physical therapist. Its MAPS module
maps clinicians and patients in real time to show under- and over-utilised areas and forecast visit
volume by region, which is the closest thing to a **capacity** capability found on this roster so
far. It has never raised outside capital; the one public revenue figure is **$143K, from 2021**. It
names **no customer anywhere**, its website still carries **unreplaced Lorem ipsum and fictional
testimonial names**, and its clinician app has **25 ratings on Android and 11 on iOS**. It names
**WellSky** — through a customer quote, not a partner page — and does not name HCHB. Compassus is
roughly three thousand clinicians. This company has four employees.

## The company

| Fact | Finding | Source · date |
|---|---|---|
| Founded | **2019.** Agreed by Crunchbase, Tracxn and Latka; the first product release found is Apr 2023. | [7] · [8] · [9] |
| Headquarters, offices | **San Diego, California.** Three addresses appear across records: 11440 W Bernardo Ct Ste 300, San Diego 92127 (association listing); 3711 Grim Ave, San Diego 92104 (association listing, second address); and 11835 Carmel Mountain Rd Ste 1304148, San Diego 92128 (business databases). A suite number of that form is a mailbox. **No office of record is established**; treat the company as distributed. | [6] · [8] |
| Ownership and funding | **Bootstrapped. $0 raised.** "Founded in 2019, CareStitch has grown… without raising any venture capital or outside funding." No investor, no round, no valuation, no accelerator found. | [7] · [9] |
| Headcount, and trend | **Four**, per a business database as of 30 Apr 2026. LinkedIn's company page shows the **2–10** band. Latka recorded **two** employees in 2021. So: two in 2021, about four in 2026 — real but very slow growth. LinkedIn shows one hire named publicly, Natalie Bell, Customer Operations Manager, 2024. | [8] · [10] · [9] |
| Leadership | **Peter Yang**, founder and CEO. **Shelley Ackerman, PT, DPT**, Chief Operating Officer — **a physical therapist, and the second-best home health clinical signal on this roster.** **Ernesto Ackerman** also appears as a contact on the industry-association listing; role not found. **Natalie Bell**, Customer Operations Manager (2024). **No CTO, no head of engineering and no engineer is named anywhere.** Peter Yang's background before CareStitch was **not found**. | [3] · [6] · [10] |
| Acquisitions, mergers, pivots, rebrands | **None found.** Same name, same market, same product since 2019. **That is worth saying plainly: it is the only vendor on this roster that has not repositioned.** | search, 2026-09-05 |
| Litigation, breaches, regulatory actions | **Not found.** | search, 2026-09-05 |
| Lines of business, and the share that is home health | **One line: scheduling and care coordination for home health and hospice.** LinkedIn: "a proprietary scheduling & care coordination platform" for "home health and hospice agencies". No other vertical, no other product, no other market. **Home health share: all of it.** | [10] · [1] |

## The product

| Fact | Finding | Source · date |
|---|---|---|
| What it does, in their words | "Simplified Home Healthcare Scheduling." Mission: "Stitch together the gaps created by operational inefficiencies in home health to lower the cost of healthcare delivery." "A proprietary scheduling platform that allows schedulers to assess, dispatch and assign cases in as few steps as possible." Nine named features: **MAPS** (Map-based Appointment Productivity System), HIPAA-compliant chat, **Automated Case Assignment** ("time- and location-based algorithm"), **Resource Utilization Dashboard** (staffing and overtime exposure), **Region Management** (zip-code-based coverage), **Live Case Request Tracking** with alerts, **Broadcast Visit Requests** ("automatic distribution to eligible clinicians"), Custom Properties (tagging users and patients), and **Schedule-Stitch** (optimising drive time between appointments). | [1] · [2] |
| What it does, in a customer's words | **Nothing usable.** The website's testimonials are **unreplaced template placeholders**: five Lorem ipsum blocks and two fictional names, "Kim Wexler" and "Billy Jackson", verified in the raw HTML of both the home page and the clinicians page. The only real customer voices found anywhere are **app-store reviews**, and two of them are substantive: *"Our agency's infrastructure"* after nearly three years of use, praising a responsive development team; and *"the BEST app… the user interface is clean and easy to navigate."* One blog post carries a quote — "It feels like CareStitch plugs directly into WellSky's blind spots" — with no attribution. | [1] · [4] · [5] · [11] |
| Capacity, scheduling, engagement — which arenas the public material covers | **Capacity: the most of any vendor researched so far, and still thin.** MAPS gives "a real-time view of where clinicians and patients are located", identifies "underutilized or overutilized areas", supports reallocating resources, and **forecasts visit volumes by region**. The Resource Utilization Dashboard monitors staffing and **overtime exposure**. Region Management is geographic coverage by zip code. That is genuine capacity vocabulary. What is absent: a capacity envelope by discipline, productivity targets, episode demand, recert and SOC scheduling windows, staffing-to-census. **Scheduling: real, and correctly shaped.** The unit is a **case or visit for a patient**, assigned to a clinician, by a scheduler, with an automated time-and-location assignment algorithm underneath and drive-time optimisation on top. **Coverage escalation exists as a named feature** — Broadcast Visit Requests distributed automatically to eligible clinicians, with live tracking and alerts — which is more than most vendors publish, though **what happens when nobody accepts is still not described**. **Engagement: clinician-side only.** Clinicians "get notified when there are new requests for patient care, and accept cases that fit you best" — accept-or-decline self-selection, plus a Personalized Daily Digest. **No patient-facing capability at all.** | [1] · [2] · [3] · [12] |
| Evidence of an HCHB integration | **Not found.** No HCHB mention on any page, in any post, in the app listings, or in any release. | site + search, 2026-09-05 |
| Other EMR integrations named | **WellSky, once, and not on a partner page.** A June 2025 blog post says the platform "integrates with existing EMRs like WellSky" and carries the unattributed quote about WellSky's "blind spots". The MAPS release says only that the software complements "agency EMRs". **No integration mechanism, direction, frequency or named customer anywhere. There is no partners page on the site at all.** | [11] · [2] |
| Agentic or automated patient outreach | **Absent.** No patient outreach, confirmation, intake or follow-up of any kind. Broadcast is clinician-facing. | site, 2026-09-05 |
| Clinician-facing app | **Exists, on both platforms, and it is small.** Android `com.carestitch.clinician_app`: **3.12 stars on 25 ratings**, about **3,500 lifetime downloads**, about 97 in the last 30 days, v4.5.7, updated 30 Apr 2026. iOS *CareStitch* by CareStitch, Inc.: **3.3 stars on 22 ratings** (AppBrain gives 4.27 on 11), v4.6.7, updated 19 Aug 2026. Version history shows steady real maintenance — iPad iOS 26+ support, patient alerts, faster PDF viewing, navigation reliability, data sync. One specific usability complaint: the messaging field shows a single line while typing. **3,500 lifetime installs is the whole user base. Compassus has about three thousand clinicians.** | [4] · [5] · [13] |
| Pricing signals | **Not found.** "Get Pricing" links, no numbers. Latka records **$143K revenue in 2021** with two employees, which implies a small number of small agencies at a low price point. | [1] · [9] |
| Security and continuity | **"HIPAA-compliant" is claimed throughout and is the only claim.** **No SOC 2, HITRUST or ISO attestation found. No security page. No uptime figure, no SLA, no status page.** For a four-person company this is expected and it is still a gap that has to be closed before anything is signed. | [1] · site, 2026-09-05 |

## The customers

| Fact | Finding | Source · date |
|---|---|---|
| Named home health customers, with size | **None. Not one, anywhere.** No customer name appears on the site, in the blog, in the press releases, in the association listing or in any database. | search, 2026-09-05 |
| Largest known deployment | **Not found**, and bounded from above by the app data: about 3,500 lifetime Android installs and 97 in the last 30 days across the entire customer base. One app-store reviewer describes nearly three years of daily use and calls it "our agency's infrastructure", so at least one agency is deeply committed. | [4] · [5] |
| Customers lost or churned | **Not found.** | search, 2026-09-05 |
| Case studies — what was measured, period, baseline | No case study document found. Figures, all without period, baseline, agency count or method, and all from the company's own blog: **"a 60% drop in missed visits"** among "agencies that moved to automated, real-time scheduling with CareStitch" — the only claimed result about their own product, and it names no agency; plus problem statistics presented as context, not results — schedulers spending "20–30% of their day on redundant, manual tasks", agencies losing "16–24 hours of productivity every week", "$30,000/year in preventable admin costs". **The 60% figure is the one to press on.** | [11] |

## What the outside view says about the questionnaire

Written 2026-09-05, before reading the return.

- **A1.** Expect no HCHB integration. WellSky is the only EMR they have ever named, once, in a blog
  post, with no mechanism — and there is no partners page on the site to check. The honest rung is
  *Will build*. **RF-01** if a live HCHB claim appears, and **RF-03** is worth watching too: a
  four-person company shipping an integration to a system with no public API will be leaning on
  somebody, and we should know who.
- **A2. RF-06 and RF-16, and this is the headline.** **Four employees. No named customer. About
  3,500 lifetime app installs.** Compassus would not merely be their largest customer — we would be
  larger than everything they have ever done, by an order of magnitude, and the question is not
  whether they would say yes but whether they could survive saying yes. Ask for three references at
  branch-director or scheduler level and treat a hedge as decisive. Ask, plainly, how many agencies
  and how many clinicians are on the platform today.
- **A3.** One claimed result — 60% fewer missed visits — with no agency, no period, no baseline.
  **RF-05.** Ask which agency, over what period, against what.
- **B versus C.** Do not expect **RF-04** here, and do not read brevity as thinness. A four-person
  company that has built exactly one product will probably describe it accurately. **Penalising
  brevity is already ruled out; this is the vendor where that rule earns its keep.**
- **C5.** They publish a coverage mechanism — Broadcast Visit Requests, automatic distribution to
  eligible clinicians, live tracking, alerts. **They do not publish what happens when nobody
  accepts.** **RF-20**, and it is worth asking well rather than as a gotcha, because they are closer
  to having a real answer than most.
- **C6. This is the stop-check.** HIPAA-compliant and nothing else. No attestation, no uptime, no
  SLA, no status page, no named security owner. **RF-07** as written. A four-person company can
  answer this honestly and still not pass it; that is the finding, not a failure of candour.
- **D1, D2.** The public posture is right: the scheduler assesses and dispatches, an algorithm
  assists, and the clinician accepts cases that fit. That is recommend-and-accept, which is our
  settled position. **Record it as a point in their favour.** Confirm at the demo that the automated
  case assignment does not lock.
- **E2. The interesting one.** Bootstrapped, four people, no investors, a founder-CEO and a
  clinician COO. There is no board and no venture investor to answer to, so a co-development or
  equity conversation is structurally simpler here than anywhere else on the roster — and the risk
  that we become the company is correspondingly higher. Watch **RF-12** less than usual and **RF-22**
  more.
- **Who wrote this.** A PT, DPT as COO and seven years on one product. Expect a return that knows
  what a scheduler's day looks like. Judge it on capacity and durability, not on fluency.

*Second pass after reading the return: to be added below, dated.*

## Durability read — evidence only

- Age seven years. **No pivot, no rebrand, no repositioning — the only vendor on this roster of
  which that is true.**
- Capital: **$0 raised.** No investor, no board, no runway pressure from outside — and no capital to
  absorb a customer twenty times its largest.
- Revenue: **$143K in 2021**, the only figure found, five years stale. Nothing since.
- Headcount: two in 2021, about four in 2026. Growing, barely.
- Main business: home health scheduling, entirely, since 2019.
- Concentration: unknown, and the app numbers bound it. About 3,500 lifetime installs and 97 in the
  last thirty days is a small number of small agencies. If one of them is most of the revenue, the
  company is one churn event from trouble, and we cannot see whether that is true.
- Our size against theirs: **about three thousand clinicians against a four-person vendor whose
  entire installed base is a fraction of that.** This is not RF-16 as a flag; it is the central fact.
- Leadership: founder-CEO with no public background found, and a physical therapist COO. **No
  engineer named anywhere**, though app release notes show real, regular maintenance by somebody.
- Product: the app is maintained, current on both platforms, and one reviewer has run an agency on
  it for three years. The engineering is real. There is just very little of it.
- The website carries **unreplaced Lorem ipsum and fictional testimonial names** on its two main
  product pages. Read it for what it is — a four-person company with no marketing capacity — and
  read it also as the reason there is no public evidence of a single customer.

## Questions the research raises

For the demo or the reference call. One line each.

1. How many agencies are on the platform today, how many clinicians, and how many visits a week?
2. Name three customers who will take a reference call at scheduler and branch-director level. Yes or no.
3. How many people work at CareStitch, and how many of them write code?
4. What is your annual revenue, and is the company profitable?
5. What is the largest agency you have ever run, by clinician count?
6. **We are about three thousand clinicians across eighty branches. What would it take, and what would break first?**
7. What is the WellSky integration, technically, and who is live on it? Where is your partners page?
8. Have you ever integrated with a system that has no public API? Describe how.
9. Give the agency, the period and the baseline behind "a 60% drop in missed visits".
10. Walk the next thirty minutes after a broadcast visit request is sent and nobody accepts.
11. Does Automated Case Assignment lock the assignment, or can a clinician decline and a scheduler override?
12. What is your security attestation, your trailing-twelve-month uptime, and what does the contract commit to?
13. Who is on call at 7am when the app is down?
14. What is Peter Yang's background before CareStitch, and who founded the company with him?
15. Your website still carries placeholder testimonials. Is there a customer who will let us name them?
16. In MAPS, what exactly does "forecast visit volumes by region" mean — what inputs, over what horizon?

## Not found

Looked for and not found, so nobody looks again (as of 2026-09-05):

- **Any customer name, anywhere.** Not on the site, the blog, the releases, the association listing
  or any database.
- Any mention of Homecare Homebase or HCHB.
- A partners or integrations page on the site.
- The mechanism, direction or frequency of the WellSky integration, or a customer on it.
- Any funding round, investor or valuation — the company states it has raised none.
- A revenue figure after 2021.
- An exact headcount from the company itself.
- A CTO, head of engineering or any named engineer.
- Peter Yang's background before founding the company, and the name of any co-founder.
- SOC 2, HITRUST or ISO attestation; a security page; an uptime figure; an SLA; a status page.
- Public pricing.
- Any customer speaking at a conference, on a panel, or in an interview.
- A G2, Capterra or SoftwareAdvice listing.
- Litigation, breaches or regulatory actions.
- Any patient-facing capability.
- Any capacity concept by discipline, or any episode, LUPA, OASIS or recertification concept.

## Gated

- LinkedIn company and person pages (headcount, trend, employee list, Peter Yang's history).
- Crunchbase and Tracxn full profiles; the free tiers gave founding year, location and $0 funding.
- Latka's full profile behind its paywall — it holds the revenue history and would settle whether
  $143K in 2021 has grown.
- California Secretary of State business registry (incorporation date, agent, officers), behind a
  search form for this session.

## Sources

Retrieved 2026-09-05. "Read" means the page was opened directly this session.

1. carestitch.com, home page. "Simplified Home Healthcare Scheduling"; nine named features including MAPS, Automated Case Assignment, Resource Utilization Dashboard, Region Management, Live Case Request Tracking, Broadcast Visit Requests, Schedule-Stitch; "HIPAA-compliant"; "Get Pricing". **Raw HTML confirms five Lorem ipsum blocks and the testimonial names "Kim Wexler" and "Billy Jackson".** Read.
2. **carestitch.com/post/carestitch-unveils-maps-map-based-appointment-productivity-system, 15 Apr 2023.** MAPS: real-time clinician and patient locations, identifying "underutilized or overutilized areas", reallocating resources, **forecasting visit volumes by region**; complements "agency EMRs". Quote: **Shelley Ackerman PT, DPT, COO.** Read. **The best single source on the capacity claim.**
3. carestitch.com/clinicians. Clinician app: "Get notified when there are new requests for patient care, and accept cases that fit you best"; Personalized Daily Digest; drive-time reduction. Placeholder testimonials present here too. Read.
4. Google Play, "CareStitch" (`com.carestitch.clinician_app`), and AppBrain's mirror: **3.12 stars, 25 ratings, ~3,500 downloads, ~97 in 30 days, v4.5.7, updated 30 Apr 2026.** Read.
5. Apple App Store, "CareStitch" (id 1494059864), seller CareStitch, Inc.: **3.3 stars, 22 ratings, v4.6.7, updated 19 Aug 2026**; version history and reviews read. AppBrain's iOS mirror gives 4.27 on 11 ratings — **the two figures do not reconcile and both are recorded.** Read.
6. **Home Care Association of Florida, associate-member listing for CareStitch.** Contacts: **Shelley Ackerman, Chief Operating Officer**; **Peter Yang, Chief Executive Officer**; **Ernesto Ackerman**. Addresses 11440 W Bernardo Ct Ste 300 and 3711 Grim Ave, San Diego. Category Software/Hardware/Information Management. Read.
7. Crunchbase, CareStitch organisation profile. Founded 2019; San Diego; no funding. **HTTP 403 to this session**; facts taken from indexed summary. Partially gated.
8. Tracxn, ZoomInfo and Datanyze CareStitch profiles. San Diego (11835 Carmel Mountain Rd Ste 1304148); **4 employees as of 30 Apr 2026**. Indexed.
9. GetLatka, "How CareStitch hit $143K revenue with a 2 person team". **$143K revenue and 2 employees, 2021**; founded 2019; **$0 raised**; founder Peter Yang. Page last updated 10 Aug 2026; the figures are 2021. Read; full profile paywalled.
10. LinkedIn, CareStitch company page: **2–10 employees**, San Diego, "Hospitals and Health Care", ~1,380 followers; "a proprietary scheduling & care coordination platform" for home health and hospice; Natalie Bell joined as Customer Operations Manager in 2024. Indexed; gated.
11. carestitch.com/b/what-are-the-costs-of-scheduling-inefficiencies-in-home-health (also at /post/…), **21 Jun 2025**. **"Agencies that moved to automated, real-time scheduling with CareStitch reported a 60% drop in missed visits."** Also "integrates with existing EMRs like WellSky" and the unattributed quote "It feels like CareStitch plugs directly into WellSky's blind spots". Problem statistics: 20–30% of a scheduler's day, 16–24 hours a week, $30,000/year. Read.
12. carestitch.com/about. Mission statement only: "Stitch together the gaps created by operational inefficiencies in home health to lower the cost of healthcare delivery"; "assess, dispatch and confirm cases in as few steps as possible". **No founder, no date, no team, no funding on the company's own about page.** Read.
13. carestitch.com/sitemap.xml. Used to enumerate the site: five pages and about twenty blog posts, including a five-part PDGM series and two clinician interviews. Read.
14. Medigy, "CareStitch, Inc." profile. Indexed; thin.
