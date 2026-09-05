# AutoMynd — research dossier

Researched 2026-09-05 · sources retrieved 2026-09-05 · confidence: **medium**

*Confidence note.* Product facts are high: nine product and policy pages were read directly and the
company publishes more detail about its security posture than most vendors ten times its size.
Customer facts are medium-high and unusually good for a company this small: two named home health
customers with named executives quoted, plus a named integration into a major EMR vendor's product,
corroborated by a third-party trade outlet. Company facts are **low**: founding year is given as
2022 in one database and 2023 in another, headcount is a range from a database rather than a count,
and no funding record exists to check. Written before reading the vendor's return.

**Identity.** The questionnaire roster says *AutoMynd* and the company writes it **AutoMynd**, one
word, capital M. Site `automynd.com` (an app subdomain, `cloud.automynd.com`, also exists).
Headquarters Reston, Virginia. Founder and CEO **Rohit Shetty**. Confirm the return's contact email
domain is `automynd.com`. **No close name collisions were found**, which makes this the cleanest
identity on the roster.

---

## At a glance

The machine-readable face of this dossier. `_research-matrix.gen.py` reads these rows to
build `Vendor-Research-Matrix.xlsx`; the prose below is the record. Bracketed numbers are
source ids from the *Sources* list at the foot of this file. *Not found* is a finding.

| Fact | Finding |
|---|---|
| **COMPANY** | |
| Founded · HQ | 2022 or 2023 — **sources disagree** · Reston, Virginia [8] [9] |
| Legal entity | AutoMynd [8] |
| Ownership · raised · last round | **Unfunded** — no round, investor or valuation [8] [9] |
| Headcount · trend | 2–10 · nine named on the about page [8] [9] [2] |
| Leadership from home health | **Yes — founder ran automation services at Bayada; two PTs, an OT and a home health RN on staff** [2] [7] |
| Pivots or rebrands in 3 years | 1 — documentation co-pilot → full EMR [10] [11] |
| Home health share of business | All of it, since founding [1] [3] |
| **PRODUCT** | |
| HCHB evidence | *not found*, and structurally unlikely — **they sell an EMR, so HCHB is a competitor** |
| Other EMRs named | **WellSky** — OEM, embedded in WellSky Personal Care, 30 Apr 2026 [12] [13] |
| Scheduling unit | A visit in an episode [4] |
| Capacity | **Absent** — no envelope, target or forecast [1] [4] |
| Scheduling | MyndShift — proximity, drive time, patient history, acuity, live availability [4] |
| Engagement | Clinician-facing (Martha); Patient360 is a portal, not outreach [1] [4] |
| Decide or advise | **Decide** — “autonomous”, “chosen automatically”, “0 manual assignments” [4] |
| Clinician app | Implied; **no app-store listing found** |
| **CUSTOMERS** | |
| Named home health customers | Butte Home Health & Hospice, 150+ staff; Ohioans Home Healthcare, unsized [5] [6] |
| Largest known deployment | Butte, about 150 staff [5] |
| Customer count | 2 named [5] [6] |
| Impact figures with a baseline | **1 of ~5 — the only one on the roster.** Three hours → about one hour per client, WellSky early adopters. No period or agency count [12] |
| Independent customer voice | Tim Ashe, WellSky's Chief Clinical Officer [12] [13] |
| **TRUST AND CONTINUITY** | |
| Security attestation | HIPAA · SOC 2 Type II with annual audits · AES-256 · TLS 1.2+ · RBAC — **the best documented on the roster** [15] |
| Uptime · SLA | *not found* [15] |
| Named dependencies | none named — **no LLM or speech provider disclosed**, for an ambient-AI product [15] |
| Pricing signal | Three tiers published, no prices on them [14] |
| **THE READ** | |
| Confidence | medium |
| The one thing to check | It would replace HCHB, and its scheduler is autonomous. |

## One paragraph

AutoMynd is a three- or four-year-old, unfunded, sub-ten-person Virginia company building an
**AI-first EMR for skilled home health** — a replacement for the system of record, not an add-on to
one. Its founder, Rohit Shetty, spent three years as director of automation services at **Bayada**,
where he built more than a hundred back-office automations, and the team he has assembled is the
only one on this roster with home health clinicians in it: two physical therapists, an occupational
therapist and a home health RN, all named as clinical subject-matter experts. The platform is seven
modules covering an episode end to end — IntakeIQ (referral and intake), **MyndShift** (scheduling),
Martha (a pre-visit voice assistant), Copilot (ambient clinical documentation), QAgent (OASIS and
PDGM coding review), MyndSight (compliance and education) and Patient360 (a patient portal). Two
home health agencies are named as customers — **Butte Home Health & Hospice** (about 150 staff,
Chico, California) and **Ohioans Home Healthcare** — and in April 2026 **WellSky** launched an
ambient-documentation product inside WellSky Personal Care "enabled by AutoMynd", which is the
strongest third-party validation any vendor on this roster has. Nothing connects them to Homecare
Homebase. Their scheduler is explicitly **autonomous** — "the right clinician, chosen
automatically", "0 manual assignments" — which is the opposite of the operating posture Compassus
has settled on.

## The company

| Fact | Finding | Source · date |
|---|---|---|
| Founded | **2022 or 2023 — the sources disagree** and neither the site nor any release settles it. Tracxn says 2022; a second database profile says 2023. Written as unresolved. | [8] · [9] |
| Headquarters, offices | **Reston, Virginia.** No other office found. | [8] · [9] |
| Ownership and funding | **Unfunded.** "AutoMynd has not raised any funding yet" as of the most recent database snapshot (April 2026). No round, no investor, no valuation, no accelerator found. Privately held by the founder is the reasonable read; the cap table is **not found**. | [8] · [9] |
| Headcount, and trend | **2–10 employees** per two databases; no exact count published, and the about page names nine people without stating a total. Twelve-month trend **not found**. | [8] · [9] · [2] |
| Leadership | **Rohit Shetty**, founder and CEO. Before AutoMynd he spent about three years at **Bayada Home Health Care** as **director of automation services**, where he "built more than 100 automations… mainly focused on back office and administrative tasks in revenue cycle and payroll." The rest of the named team, and this is the point: **Cody Quinlan, Head of Clinical Innovations (home health PT)**; **Lane McCoy, Clinical SME (home health PT)**; **Sarah Blair, Program Manager (OT)**; **Danielle Bress, Home Health RN SME**; Jason Revuelta, Head of Strategy & Growth; Hillary Severson, Head of Marketing; Ahzam Fawmee, Sr. Software Engineer; Amelia Castaneda, Customer Success Manager. **Four named clinicians who have practised in home health. No other vendor on this roster has one.** No CTO and only one named engineer. | [2] · [7] |
| Acquisitions, mergers, pivots, rebrands | No acquisitions found. **One clear widening of scope:** the company began as an AI documentation co-pilot ("AI Co-Pilot for Home Health Clinicians to automate visit documentation") and now sells a full EMR ("AutoMynd launches AI-first EMR for home health, automating episodes from referral to reimbursement"). An `/old-home` page from the co-pilot era is still live on the site. The name has not changed. | [1] · [10] · [11] |
| Litigation, breaches, regulatory actions | **Not found.** | search, 2026-09-05 |
| Lines of business, and the share that is home health | **Home-based care only, and mostly skilled home health.** "Who we serve" is home health, health plans and coding support. Blog output is almost entirely skilled home health: OASIS-E, PDGM, LUPA-adjacent billing, star ratings, CMS proposed rules. Hospice appears as an expansion at Butte. The WellSky work is **personal care**, which is a different market from ours. **Home health share: the majority, and the company has never sold anything else.** | [1] · [3] · [5] · [6] |

## The product

| Fact | Finding | Source · date |
|---|---|---|
| What it does, in their words | "AI First EMR for Home-Health Agencies. From Referral to Reimbursement, in One Complete AI platform." Seven modules: **IntakeIQ** ("AI-powered referral and intake platform"), **MyndShift** ("Autonomous AI scheduling that matches every visit to the right clinician"), **Martha** ("Pre-Visit Voice Assistant… prepares clinicians on the go"), **Copilot** ("AI for Clinical Documentation"), **QAgent** ("AI-Assisted OASIS & Coding… expert-level reviews"), **MyndSight** ("Clinical Compliance & Education"), **Patient360** ("Patient Engagement Portal… one longitudinal view"). | [1] · [4] |
| What it does, in a customer's words | **Two named customers with named executives, which is rare on this roster.** **Robert Love, Executive Director, Butte Home Health & Hospice:** "With Medicare home health budget cuts looming, we knew we couldn't respond by reducing patient care—so we chose to reduce administrative burden instead." **Josh Adams, CEO, Ohioans Home Healthcare:** "AutoMynd is putting a facelift on the entire clinician experience." **Caitlin Lipper, Quality Program Manager, Ohioans:** "We truly see AutoMynd as our partner in clinical innovation." Both posts are on AutoMynd's own blog and read as co-written, so they are **strong claims, not independent evidence**. The one independent voice is **Tim Ashe, WellSky's Chief Clinical Officer**, in the WellSky release. | [5] · [6] · [12] |
| Capacity, scheduling, engagement — which arenas the public material covers | **Capacity: absent.** No capacity envelope, no staffing-to-census model, no productivity target, no discipline-mix planning, no demand forecast. The word does not appear as a product concept. **Scheduling: present, visit-based, and autonomous.** MyndShift assigns "every visit" using **proximity and drive time, patient history, acuity level, and live availability**, ranking candidates on axes like "Closest · PT continuity · lightest caseload", with "Auto re-scheduling". **The unit is a visit and the entities are clinicians, disciplines and caseloads — the correct shape, and the only vendor on this roster whose scheduling object matches ours.** **Engagement: partial.** Martha is clinician-facing, not patient-facing; Patient360 is a portal, which is a place patients go, not outreach that reaches them. No voice or SMS patient outreach found. | [4] · [1] |
| Evidence of an HCHB integration | **Not found**, and structurally unlikely: AutoMynd sells an EMR, so HCHB is a competitor, not a partner. No HCHB mention on any page, in any release, or in any blog post — and they blog about competing EMRs by name in the abstract ("AI-native EMR vs traditional EMR", "comparing skilled home health EMRs"). | site + search, 2026-09-05 |
| Other EMR integrations named | **One, and it is significant: WellSky.** On 30 Apr 2026 WellSky launched "WellSky Ambient Documentation for Personal Care, **enabled by AutoMynd**", with AutoMynd's ambient AI "embedded directly within the WellSky Personal Care platform". Commercial terms, exclusivity and duration are **not found**. No other EMR named. | [12] · [13] |
| Agentic or automated patient outreach | **Absent as patient outreach.** Martha is a pre-visit voice assistant for clinicians. Patient360 is a portal. No outbound patient calling, confirmation, reminder or rebooking agent found. | [1] · [4] |
| Clinician-facing app | Implied by Martha ("prepares clinicians on the go") and by an app subdomain, `cloud.automynd.com`. **No Apple App Store or Google Play listing found**, so ratings and review counts are **not found**. | search, 2026-09-05 |
| Pricing signals | **Three published tiers exist as pages — Basic, Pro, Elite — but no prices were found on them.** That is further than most vendors go and still not a number. | [14] |
| Security and continuity | **Better documented than any other vendor on this roster, including the funded ones.** A dedicated security page claims "HIPAA-compliant and **SOC 2 Type II certified**" with "**Annual SOC 2 Type II Audits**", **AES-256 at rest, TLS 1.2+ in transit**, **RBAC** limited to HIPAA-trained personnel, 24/7 monitoring with anomaly detection and automated threat response, and audit trails logging "user identity, timestamp, and purpose" on every access to ambient AI output. On retention: "We retain only the processed and structured documentation outputs, **not raw recordings**, unless compliance requires it." **But: no uptime figure, no SLA, no status page, and no subprocessor or model-provider list** — no LLM vendor is named anywhere, which for an ambient-AI product is the gap to press on. | [15] |

## The customers

| Fact | Finding | Source · date |
|---|---|---|
| Named home health customers, with size | **Butte Home Health & Hospice** — non-profit, community-owned, founded 1984, Chico, Northern California, serving Butte, Glenn and Tehama counties, **"more than 150 professionals"**. Modules: Copilot with medication reconciliation, OASIS automation, IntakeIQ, expanding into physical therapy and hospice workflows. **Ohioans Home Healthcare** — live since **April 2025**; modules Copilot, IntakeIQ, QAgent; size **not found**. | [5] · [6] |
| Largest known deployment | **Butte, at about 150 staff**, is the largest deployment whose size is public. Compare: Compassus is roughly three thousand clinicians. | [5] |
| Customers lost or churned | **Not found.** | search, 2026-09-05 |
| Case studies — what was measured, period, baseline | No formal case study document found. Figures, and note that only one has a baseline: **WellSky release — "a 66% reduction in documentation time, dropping from three hours to approximately one hour per client"** for early adopters. **That is a before-and-after with both numbers stated, which is better than almost anything else on this roster** — but it has no period, no agency count and no method, and it is personal care, not skilled home health. Elsewhere: "90 minutes to under 10 minutes" for documentation, attributed industry-wide rather than to a customer; "0 Manual assignments" and "96 Clinicians balanced daily" on the MyndShift page, which read as interface mock-ups, not results. The Ohioans post lists **targets**, not measured outcomes — reduced after-hours charting, improved OASIS-E accuracy, faster billing — and is honest about it. One testimonial is attributed to "Melanie, PT at Top Home health agency", which is anonymised to the point of being worthless. | [12] · [5] · [4] · [1] · [6] |

## What the outside view says about the questionnaire

Written 2026-09-05, before reading the return.

- **A1. This is the question that decides them.** They sell an EMR. HCHB is our system of record and
  we are not replacing it. Expect either a candid "we do not integrate with HCHB" — which would be
  worth real credit under **Candor about gaps** — or an integration story built from the WellSky
  precedent. Ask what the WellSky arrangement actually is technically, because if AutoMynd can embed
  a module inside another vendor's platform, that is the only credible path to an HCHB rung here.
  Watch **RF-01** if a bi-directional HCHB claim appears with no mechanism and no customer.
- **A2. RF-16 on the second half, unambiguously.** Their largest public deployment is about 150
  staff. We are about three thousand clinicians across eighty branches. **We would be their largest
  customer by roughly twenty times.** On the first half they are the opposite of the field: home
  health is not a minority of their business, it is all of it. Say both things.
- **A3.** The WellSky documentation figure has a baseline and a before-and-after; most of the rest
  do not. **RF-05** applies to the site figures, not to the WellSky one. Give them credit where the
  baseline exists and press on the rest.
- **C2, C4, D1, D2. This is the sharpest fit problem on the roster and it is not about size.**
  MyndShift is marketed as an **"Autonomous AI Scheduler"** — "the right clinician, chosen
  automatically", "**0 Manual assignments**", "Auto re-scheduling". Our settled position is that the
  tool recommends and the human accepts, and that assignment, coverage and the week are Assist. This
  is **RF-14** in the vendor's own headline, and **RF-10** if a clinician cannot override. It is also
  the case study for the rule that **a higher automation score can be a worse fit**. Ask directly:
  can MyndShift run recommend-only, per branch, today, and has any customer run it that way?
- **C6.** They are ahead of the field on documented controls and behind it on continuity: no uptime,
  no SLA, no status page. **RF-07** on the continuity half only. Then ask the ambient-AI question
  nobody else on this roster raises: **which model provider processes the audio, under what
  agreement, with what training exclusion.** No LLM vendor is named anywhere on the site.
- **E2 and Durability.** Unfunded, under ten people, no capital record. **RF-06** if three references
  are not committed — they may have only two customers to offer. The equity or co-development
  conversation is structurally wide open here in a way it is not with a venture-backed vendor, and
  the WellSky arrangement proves they will do OEM deals.
- **Who wrote this.** A founder who ran automation services inside Bayada, and four home health
  clinicians on staff, is the best home health fluency signal on the roster so far. If the return is
  fluent about OASIS, PDGM, LUPA, recertification and pajama time, believe it — that is the company.
  Judge the gap between that fluency and the thinness of the capacity answers, not the fluency
  itself.

*Second pass after reading the return: to be added below, dated.*

## Durability read — evidence only

- Age three or four years; the founding year does not reconcile across databases.
- Capital: **no funding round found at all.** No investor, no valuation, no runway visible. Either
  revenue-funded or founder-funded; the public record does not say which.
- Headcount 2–10, nine named on the about page, **one named software engineer**. Building a full
  EMR — intake, scheduling, documentation, QA, coding, billing — with that team is a very large
  scope for a very small company, and scope-to-capacity is the durability question here.
- Main business: skilled home health, entirely, since founding. No adjacent verticals, no landing
  pages for other industries.
- Concentration: two named customers. The larger is about 150 staff. **The WellSky relationship may
  be a bigger share of the business than either customer**, and if so, a single OEM partner is the
  concentration risk — terms, exclusivity and duration are all not found.
- Our size against theirs: about twenty times their largest known deployment.
- Leadership: founder from Bayada operations; four practising-background home health clinicians;
  no CTO named.
- The website carries **Webflow template placeholder team pages** — `/team/john-carter`,
  `/team/sophie-moore`, `/team/amy-smith`, `/team/will-newt`, several duplicated — still live in the
  sitemap, and a `/old-home` page from the documentation-co-pilot era. Minor, and it is the correct
  kind of evidence about stage: this is a company building faster than it is tidying.

## Questions the research raises

For the demo or the reference call. One line each.

1. You sell an EMR. We are not replacing HCHB. What is the integration story, and is there one at all?
2. **What exactly is the WellSky arrangement?** OEM, licence, reseller, exclusive? For how long? What share of your revenue is it? Could the same pattern work with HCHB?
3. Can MyndShift run in recommend-only mode, per branch, today? Has any customer ever run it that way?
4. "0 manual assignments" — what can a clinician change without approval, right now, in your product?
5. What happens to a visit whose authorization arrives after the compliance window has opened?
6. Walk the next thirty minutes after a visit is offered and nobody takes it.
7. Which model provider processes ambient audio, under what agreement, with what retention and what training exclusion? Name it.
8. What is your trailing-twelve-month uptime, and what does the contract commit to? What does a branch do at 7am during an outage?
9. How many customers do you have, how many are Medicare-certified, and what is the largest by clinician count?
10. How many engineers do you have?
11. Have you raised any capital? What funds the next twelve months?
12. Is MyndShift live with a paying customer today, or is it on the roadmap? Which of the seven modules are in production?
13. Give the period, agency count and method behind the 66% documentation reduction. Was it measured in personal care or skilled home health?
14. Will Butte and Ohioans take reference calls at scheduler and branch-director level?
15. Where does capacity live in your product? Not scheduling — capacity.

## Not found

Looked for and not found, so nobody looks again (as of 2026-09-05):

- Any mention of Homecare Homebase or HCHB, anywhere.
- Any funding round, investor, valuation or accelerator.
- An exact headcount or a twelve-month trend.
- A CTO or a head of engineering; only one software engineer is named.
- A clinician app listing in the Apple App Store or Google Play.
- Any LLM, speech or model provider named as a subprocessor.
- An uptime figure, SLA or status page.
- Published prices on the Basic, Pro and Elite tier pages.
- The size of Ohioans Home Healthcare.
- The commercial terms, exclusivity or duration of the WellSky arrangement.
- Any customer speaking independently — no conference talk, panel or review-site listing found on
  G2, Capterra or SoftwareAdvice.
- Litigation, breaches or regulatory actions.
- A settled founding year.
- Any capacity-planning capability.

## Gated

- LinkedIn company and person pages (headcount, trend, employee list, Rohit Shetty's Bayada dates).
- Crunchbase and Tracxn full profiles — the free tiers gave founding year and headcount band and
  disagree with each other on the year.
- Home Health Line (DecisionHealth), "AI, ambient listening poised to revolutionize…" — a paywalled
  trade article that appears to carry the fullest independent profile of the founder and the
  company found anywhere. **Worth buying or borrowing; it is the best single unread source.**
- HCHB's Recommended Partner brochure PDF (a Figma export, no text layer, over the fetch limit).

## Sources

Retrieved 2026-09-05. "Read" means the page was opened directly this session.

1. automynd.com, home page. "AI First EMR for Home-Health Agencies. From Referral to Reimbursement"; seven modules named; "HIPAA & SOC2 compliant"; the "Melanie, PT at Top Home health agency" testimonial. Read.
2. automynd.com/about-us. Mission; nine people named with roles, including four with home health clinical backgrounds. Read.
3. automynd.com/who-we-serve/home-health, /health-plans, /coding-support. Read via sitemap.
4. **automynd.com/product-pages/myndshift.** "Autonomous AI Scheduler"; matching on proximity and drive time, patient history, acuity level, live availability; "Closest · PT continuity · lightest caseload"; "Auto re-scheduling"; "0 Manual assignments"; "96 Clinicians balanced daily"; described as "a core scheduling layer of AutoMynd's AI-Powered EMR". **Read directly; the most load-bearing source here.**
5. automynd.com/blog/butte-home-health-hospice-partners-with-automynd. Butte Home Health & Hospice: non-profit, community-owned, founded 1984, Chico CA, Butte/Glenn/Tehama counties, "more than 150 professionals"; Copilot with medication reconciliation, OASIS automation, IntakeIQ; expanding to PT and hospice. Quotes: Robert Love, Executive Director; Rohit Shetty. Post date not stated. Read.
6. automynd.com/blog/automynd-ohioans-home-health-partnership. Ohioans Home Healthcare, live April 2025; Copilot, IntakeIQ, QAgent; targets listed, not results. Quotes: Josh Adams (CEO), Caitlin Lipper (Quality Program Manager), Rohit Shetty. Read.
7. LinkedIn, Rohit Shetty profile: about three years at Bayada Home Health Care as director of automation services; "built more than 100 automations… back office and administrative tasks in revenue cycle and payroll". Indexed; profile gated.
8. Tracxn, "AutoMynd — 2026 Company Profile, Team & Competitors". Founded **2022**; Reston; **unfunded**; 2–10 employees; Generative AI, NLP, speech recognition. Indexed, partially gated.
9. Crunchbase and Bounce Watch, AutoMynd organisation profiles. Founded **2023**; Reston, Virginia; 2–10 employees; no funding. Indexed, partially gated. **Conflicts with [8] on the founding year.**
10. automynd.com/blog/automynd-launches-ai-first-emr-for-home-health-automating-episodes-from-referral-to-reimbursement. The move from co-pilot to full EMR. Read via sitemap.
11. automynd.com/old-home, "Transforming Home Health Care: AI Co-Pilot for Clinicians & Agencies". The previous positioning, still live. Indexed.
12. **WellSky press release, "WellSky® Launches AI-Powered Ambient Documentation for Personal Care, Enabled by AutoMynd", 30 Apr 2026** (wellsky.com, BusinessWire, Yahoo Finance). Embedded in WellSky Personal Care; captures ADLs, IADLs, client preferences and coordinator observations during intake, populating the care plan for staff review; "a 66% reduction in documentation time, dropping from three hours to approximately one hour per client". Quotes: Tim Ashe (WellSky Chief Clinical Officer), Rohit Shetty. The wellsky.com copy returned 403 to this session; read via HIT Consultant [13] and the wire copy.
13. HIT Consultant, "WellSky and AutoMynd Launch First Ambient AI Documentation for Personal Care Agencies", 30 Apr 2026. Read. Independent trade coverage of [12].
14. automynd.com/product/basic, /pro, /elite. Three tier pages exist; **no prices found on them**. Read via sitemap.
15. **automynd.com/security.** HIPAA; SOC 2 Type II certified with annual audits; AES-256 at rest, TLS 1.2+ in transit; RBAC; 24/7 monitoring, anomaly detection, automated threat response; audit trails with user identity, timestamp and purpose; "we retain only the processed and structured documentation outputs, not raw recordings, unless compliance requires it". No uptime, no SLA, no subprocessor list. Read.
16. automynd.com/sitemap.xml. Used to enumerate the site. Shows the seven product pages, three pricing tiers, thirty-plus blog posts, and **Webflow placeholder team pages** (`/team/john-carter`, `/team/sophie-moore`, `/team/amy-smith`, `/team/will-newt`, several duplicated). Read.
17. Home Health Line (DecisionHealth), "AI, ambient listening poised to revolutionize…". **Paywalled; not read.** Appears to be the fullest independent profile of the founder and the company.
