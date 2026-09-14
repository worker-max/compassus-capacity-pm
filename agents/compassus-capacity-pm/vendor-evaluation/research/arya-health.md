# Arya Health — research dossier

Researched 2026-09-09 · sources retrieved 2026-09-09 · confidence: **high**

*Confidence note.* High. The company's own homepage, security page, industries page, privacy
policy, terms of service and three product blog posts were read directly, along with its own seed
and Series A releases and its own customer-results release. **The identity is pinned from the
company's own legal documents**, which is the strongest pin on the roster. Two limits, both stated
where they bite: the only source that names HCHB is a press-aggregator page that refuses both of our
fetchers, and the headcount is an aggregator estimate because the company publishes none. Written
before reading the vendor's return.

**Identity.** The trading name is **Arya**; the domain is `aryahealth.ai`; the product runs at
`app.aryaworks.com`. The legal entity in both the privacy policy and the terms of service is
**Arya for Work, Inc., a Delaware corporation** — *not* "Arya Health, Inc." Governing law and
arbitration venue are New York, New York. **Confirm the return's contact email domain is
`aryahealth.ai` or `aryaworks.com`** — both are this company; anything else is not.
**Not Arya Health of Vancouver** (Arya EHR, launched Jan 2020, founded 2016 by Sam Gharbi, Richard
Sztramko and Richard Vandegriend), which is a different company that several aggregators merge with
this one. Not Arya.ai (Mumbai, financial services). Not Arya by Leoforce (recruiting).

---

## At a glance

The machine-readable face of this dossier. `_research-matrix.gen.py` reads these rows to
build `Vendor-Research-Matrix.xlsx`; the prose below is the record. Bracketed numbers are
source ids from the *Sources* list at the foot of this file. *Not found* is a finding.

| Fact | Finding |
|---|---|
| **COMPANY** | |
| Founded · HQ | 2022 · **Princeton, NJ — corrected 2026-09-09 from their own SEC filings**, 19 Kent Court, on both Form Ds signed by the CEO. Their terms set New York law and venue and the release is datelined New York [S1] [5] [9] |
| Legal entity | **Arya for Work, Inc., a Delaware corporation** — *not* “Arya Health, Inc.”; the app runs at `aryaworks.com` [5] [4] [1] |
| Ownership · raised · last round | **$25.31M actually sold, per SEC Form D.** Series A **$18,079,306 sold** of $18,179,303 offered, first sale **18 Aug 2025** — 72 days before the 29 Oct announcement — 13 investors, ACME Capital led. Seed **$7,234,996 sold, 100% of offering, 17 investors**, first sale 10 May 2024 — **the announced “$4M seed” understated it by $3.23M**. Revenue range on both filings: “Decline to Disclose” [S1] [9] [8] |
| Headcount · trend | **11–50, aggregator estimate — the company publishes no number.** Revenue “more than 6x in 2025” [13] [9] |
| Leadership from home health | **One, and she was hired for it** — Melinda Phillips, former CEO of Thrive Skilled Pediatric Care, leads the “Care@Home Center of Excellence”. **Neither founder is from home health**: Kunal Sarda, CEO, was VP Customer Engagement at Smartling; Arunram Kalaiselvan, CTO [9] [13] |
| Pivots or rebrands in 3 years | **Two shifts in 24 months, and the legal name still says the first one.** Sep 2024 they were “the most flexible workforce automation product on the market” for **Home Care, Hospice and SNF — home health was not on that list**; by 2026 Home Health leads the list and the framing is “AI agents for post-acute care administration”. The entity is still *Arya for Work, Inc.* [8] [3] [9] [5] |
| Home health share of business | ***not established*** — Home Health is listed first of six settings, but **the only named customer is pediatric private-duty nursing** and the seed-round list omitted home health entirely [3] [8] [10] |
| **PRODUCT** | |
| HCHB evidence | **Weak, and it is not theirs.** HCHB is named nowhere on Arya's own site — the homepage says only “EMR, ATS, HRIS” and the Series A release says “leading EMRs”. The one source naming HCHB is a press-aggregator page **gated to both our fetchers**. **Arya is not on HCHB's Recommended Partner Solutions page** [1] [9] [11] [G1] |
| Other EMRs named | ***none by Arya***. The gated aggregator names WellSky, HCHB and AlayaCare; **every own-source mention is generic** [1] [9] [G1] |
| Scheduling unit | **An hourly shift on a case — not a visit in an episode.** Throughput is quoted as “~3,000 hrs/month” per scheduler [6] |
| Capacity | ***not found*** — no forecast, no demand model, no caseload model, no authorization concept on any page read. **PDGM, LUPA, episode and recert appear nowhere** [6] [7] |
| Scheduling | **Real, and the core skill** — “It makes the match, contacts the caregiver, confirms the assignment, and updates the EMR” [6] |
| Engagement | **Staff-facing only.** The “Engagement” skill is caregiver retention; no patient-facing product found [1] [3] |
| Decide or advise | **Decide — explicitly, and sold as the point.** “It **doesn't** present a list of options for a coordinator to choose from”; “The agent **makes and executes** scheduling decisions rather than presenting options”; “The agents don't wait to be triggered. They monitor conditions, take action, and push updates to the EMR **on their own**.” **No override language found anywhere** [6] [7] |
| Clinician app | ***not found*** — no app on either store, no portal described. The caregiver is **contacted by the agent**; the named voice-call subprocessor is Bland AI [4] [1] [6] |
| **CUSTOMERS** | |
| Named home health customers | **One, and it is pediatric private duty** — Connect Pediatrics, Texas, founded 2014, ~$7M revenue 2025. **No Medicare-certified home health agency is named anywhere** [10] [12] |
| Largest known deployment | **12 locations, 150+ clinicians** — the Connect Pediatrics staffing deployment [10] [7] |
| Customer count | ***not found*** — no agency or customer count published in any own source [1] [9] |
| Impact figures with a baseline | **1 of 7.** Only “~3,000 hrs/month per scheduler” carries a before-value (“versus ~2,000”). Without one: 25% scheduler capacity · 50% time-to-first-staffing · 70% less administrative effort · 60% less human effort · 6x revenue · “25 cents of every dollar” [6] [9] [10] |
| Independent customer voice | **A named CEO — but the words are inside the vendor's own release.** Ezra Kuenzi, co-founder and CEO, Connect Pediatrics. **Person and agency both verified real and independent of Arya** [10] [12] |
| **TRUST AND CONTINUITY** | |
| Security attestation | **SOC 2 Type I *and* Type II claimed, HIPAA claimed, annual third-party pen test claimed, “continuously monitored by Secureframe”. No auditor named, no report, no Trust Center — and the privacy policy names no attestation at all.** BAAs offered on request [2] [4] |
| Uptime · SLA | ***not found*** — no uptime figure, no status page, no SLA on any page read [1] [2] [5] |
| Named dependencies | **Named — a credit, and a concern.** Supabase (database), Cloudflare (hosting), **Bland AI (voice calls to caregivers)**, **n8n (workflow automation)**. The autonomous agent runs on a third-party workflow engine and a third-party voice vendor [4] |
| Pricing signal | ***not found*** on the site. The Series A release frames the agents at “approximately 10% the cost of a full-time hire” — a headcount-replacement model, not a per-visit or per-clinician one [9] [13] |
| **THE READ** | |
| The one thing to check | **They advertise that the agent decides and deliberately does not offer the coordinator options. That is the exact inverse of our settled principle that the tool recommends and the human accepts.** |
| Ask them first | Show us one **Medicare-certified** home health agency, on HCHB, where your agent schedules **visits in an episode** — not hourly shifts on a case. [6] [10] |
| Would we be their largest customer | **Yes, by roughly twenty times.** Their largest known deployment is 150+ clinicians across 12 locations; we are about 3,000 clinicians across about 80 branches. The company itself is 11–50 people [10] [13] |
| Red flags to test | **RF-10 STOP-CHECK** the system decides and no override is described — and it is the sales pitch, not an accident · **RF-06 STOP-CHECK** one named customer, in a different payer world · **RF-07 STOP-CHECK** no uptime or SLA · **RF-01** HCHB named only by a gated third party, never by Arya, and absent from HCHB's own partner page · **RF-19** hours and shifts throughout; no authorization or episode concept · **RF-16** we would be ~20× their largest deployment · **RF-05** 6 of 7 impact figures carry no baseline · **RF-03** the agent's voice and workflow layers are outsourced [1] [4] [6] [10] [11] |
| Where their own sources disagree | **Four.** Security page claims SOC 2 Type I and II; **the privacy policy names no attestation at all** · the seed release sold Home Care, Hospice and SNF and **omitted home health**; the site now leads with it · the site says “EMR, ATS, HRIS” generically while a press page names HCHB, WellSky and AlayaCare · **the company is “Arya Health” everywhere except its own contracts, where it is “Arya for Work, Inc.”** [2] [4] [3] [8] [5] [G1] |
| Confidence | high |

---

## One paragraph

Arya is a four-year-old New York company that sells one AI agent with eight named skills —
Scheduling, Compliance, Talent, Onboarding, Intake, Payroll, Engagement, Front Desk — to
post-acute care organisations, and it is the best-funded vendor on the roster after AxisCare's
investors. It raised $18.2M in October 2025 behind a claim that is stated more plainly than any
other vendor has dared: the agent does not hand a coordinator a shortlist, it makes the match,
calls the caregiver, confirms the assignment and writes to the EMR itself. That is a genuine
product and a real differentiator. It is also, as written, the opposite of the principle this
initiative has already settled — that the tool recommends and the human accepts — and it is the
first thing to put to them. The rest of the picture is thinner than the funding suggests. The
scheduling unit is an hourly shift on a case, quoted in hours per scheduler per month, which is
home *care* shape rather than home *health*; nothing in the material forecasts capacity; PDGM,
LUPA, episode, recert and authorization appear nowhere. One customer is named — Connect
Pediatrics, a real Texas pediatric private-duty agency of about $7M revenue whose CEO is a real
person — and that deployment, twelve locations and 150-plus clinicians, is about a twentieth of us.
HCHB is named by a press aggregator we cannot reach and by nobody at Arya; HCHB's own partner page
does not list them.

## The company

Founded 2022 by Kunal Sarda (CEO, previously VP Customer Engagement at Smartling) and Arunram
Kalaiselvan (CTO). Neither comes from home health. The company raised $4M in September 2024 led by
Twelve Below, with Oceans, Ridge Ventures and Nebular VC, and $18.2M on 29 October 2025 led by ACME
Capital with Ridge Ventures, Twelve Below and unnamed OpenAI executives — $25M in total. Revenue
grew "more than 6x in 2025" and is "on track for 10x year-over-year growth by year-end"; no absolute
revenue, customer count or headcount is published, and 11–50 is an aggregator's estimate.

The headquarters is worth pinning because three sources give three answers. Their own terms of
service set New York law and arbitration in New York, New York; their own Series A release is
datelined NEW YORK; PitchBook and one press summary say Princeton, New Jersey; another says
Philadelphia. **Take New York** — the company's own contract is the better source, and the release
it wrote agrees with it.

**The name is not settled either.** Every public surface says *Arya* or *Arya Health*. Both legal
documents say **Arya for Work, Inc.**, and the application is served from `aryaworks.com`. A
company that still contracts under a generic workplace name while marketing a healthcare product
is telling you something about how recently the healthcare thesis arrived.

The September 2024 seed release names its market as **Home Care, Hospice and Skilled Nursing
Facilities**. Home health is absent. Two years later Home Health Care heads the list of six
settings. The intervening hire is the tell: Melinda Phillips, former CEO of Thrive Skilled
Pediatric Care (acquired by Aveanna), was brought in to lead a "Care@Home Center of Excellence".
That is a company buying the domain knowledge it did not have, which is more than most of the
roster has done — and also an admission of where it started.

## The product

One agent, eight skills. The scheduling skill is described with unusual precision, and the
precision is the finding:

> "It makes the match, contacts the caregiver, confirms the assignment, and updates the EMR."
> "It doesn't present a list of options for a coordinator to choose from."
> "The agent makes and executes scheduling decisions rather than presenting options."
> "The agents don't wait to be triggered. They monitor conditions, take action, and push updates
> to the EMR on their own."

No page read describes an override, an approval step, a confidence threshold, an escalation path or
a scheduler's veto. This is not a vendor hedging between *decide* and *advise* the way AxisCare
does; it is a vendor that has chosen *decide* and put it in the marketing copy. **That makes the
question easy to ask and the answer easy to check.**

The unit is the tell for fit. Throughput is "~3,000 hrs/month" per scheduler against "~2,000"
manually; the market is "agencies staffing 50 to 5,000+ caregivers"; compliance means "credential
verification per visit" and EVV alignment. Hours, shifts, caregivers, EVV. That is the private-duty
and home-care vocabulary. **Episode, authorization, discipline mix, recert window, PDGM and LUPA do
not appear**, and neither does any forecast of demand or capacity. Capacity comes first in this
initiative and Arya does not model it.

Engagement is caregiver retention, not patient contact. There is no clinician app: the caregiver is
reached *by* the agent, and the privacy policy names **Bland AI** as the voice-call subprocessor,
**n8n** as the workflow engine, **Supabase** as the database and **Cloudflare** as the host. Naming
them is better practice than most of the roster manages. It also means the autonomous agent that
would call our nurses is assembled from three vendors we would not be contracting with.

## The customers

One is named, in the vendor's own release of 8 April 2026: **Connect Pediatrics**, Texas — the
Staffing Agent across 12 locations and 150-plus clinicians, "thousands of hours of clinical care
scheduled autonomously", and a 25% gain in scheduler capacity. Per the roster's own rule, the
testimonial was verified rather than repeated: **Ezra Kuenzi is a real person**, co-founder and CEO
of Connect Pediatrics with his wife Gina Kuenzi, RN; they founded it in 2014 after their nephew
Dillon was born needing round-the-clock skilled nursing; the agency does pediatric home nursing and
therapy across Texas and reported about $7M revenue in 2025. The quote is genuine and the customer
is real.

**It is also pediatric private-duty nursing, not Medicare home health.** Hourly shifts on a case,
which is exactly the unit the product is built for. And at roughly $7M of revenue and 150 clinicians
it is about one-twentieth of us.

## What the outside view says about the questionnaire

- If the return claims an HCHB integration, ask for the mechanism and a reference, because **Arya
  has never named HCHB in its own voice** and HCHB does not list Arya as a partner. **RF-01.**
- If the return claims a human stays in control of scheduling, that is worth a slow read against
  their own marketing, which says the opposite in three places. Ask which is current. **RF-10,
  STOP-CHECK.**
- If the return offers capacity forecasting, ask to see it: nothing in the public material forecasts
  anything, and the word does not appear.
- If the return cites the 25% or 50% or 70% figures, ask what the denominator was. Six of the seven
  published figures have no baseline. **RF-05.**
- If the return says SOC 2 Type II, ask for the report and the auditor. The claim is on the security
  page and absent from the privacy policy. **C6.**
- If the return names more customers than Connect Pediatrics, that is new information and the most
  valuable thing in it. **RF-06, STOP-CHECK.**

## The thing this dossier exists to say

Arya is the clearest test the roster has produced of a principle we settled early: **a higher
automation score can be a worse fit.** They will score well on sophistication — the agent is real,
the funding is real, the engineering is credible, and they will demo beautifully. They have then
told us, in writing and on purpose, that the coordinator does not get options. Compassus has three
hundred schedulers whose judgment is the control on a system that touches patients. Either Arya has
an override they do not advertise, or they are selling the one thing we decided not to buy. That is
a single question, and it should be the first one asked.

## Durability read — evidence only

$25M raised, most of it eleven months ago; a named lead investor; 6x revenue growth claimed;
11–50 people; a domain expert hired into the leadership; one named customer in an adjacent segment;
a legal entity still named for the pre-healthcare product; and a market list that changed between
funding rounds. No layoffs, litigation, outage record, acquisition or leadership departure found.

## Questions the research raises

1. Can a Compassus scheduler override, reject or reverse an assignment the agent has already made
   and communicated to a clinician — and what does the clinician see when that happens?
2. What is the mechanism of the HCHB integration: HCHB Connect, Business Connect, a flat-file
   exchange, or screen automation? Who certified it, and when?
3. Are you listed in HCHB's Recommended Partner Solutions? If not, why not, and is an application in
   progress?
4. Name a Medicare-certified home health agency using the Scheduling skill. How many, since when,
   and may we speak to one?
5. Does the product model an episode, an authorization, a recert window, a discipline mix, PDGM or
   LUPA risk in any form? Show us where.
6. What did you forecast for Connect Pediatrics before the deployment, and what was the measured
   baseline the 25% is drawn from?
7. Does the product forecast capacity or demand at all, or does it only fill work that already
   exists?
8. Who audited the SOC 2 Type II, when was the report issued, and will you provide it under NDA?
9. Why does the privacy policy name no attestation when the security page names two?
10. Bland AI places voice calls to caregivers. Are those calls disclosed as AI to our clinicians,
    are they recorded, where is that audio stored, and is Bland AI covered by a BAA?
11. n8n runs the workflow automation. Is it self-hosted by Arya or the vendor's cloud, and does PHI
    traverse it?
12. What is your uptime record and what SLA would you sign? A scheduling outage stops nurses being
    deployed.
13. What is the largest agency you have deployed to, by clinicians and by locations?
14. Why is the contracting entity "Arya for Work, Inc." and not a healthcare entity?
15. The September 2024 release named Home Care, Hospice and SNF and not home health. What changed,
    and what in the product changed with it?
16. What is your headcount today, and how many of those people have worked in Medicare home health?
17. What is the pricing model — per agent, per scheduler, per clinician, per visit, or a share of
    the headcount it replaces?

## Not found

Headcount from the company itself · customer count · any agency count · any Medicare-certified home
health customer · uptime, status page or SLA · pricing · a clinician-facing app · any override,
approval or escalation mechanism · any capacity or demand forecast · PDGM, LUPA, episode,
authorization, recert or discipline-mix language · the SOC 2 auditor, report or Trust Center · a
postal address on any own-source page · any named EMR in Arya's own voice.

## Gated

- **`yespress.io/arya-health`** — HTTP 403 to both WebFetch and a browser user-agent. **This is the
  only source found that names HCHB, WellSky and AlayaCare in connection with Arya**, and we could
  not read it in full or establish who wrote it. Treat the HCHB claim as unverified.
- **`mobihealthnews.com`** Series A report — HTTP 403 to both fetchers.
- **PitchBook** company profile — paywalled; it is the source of the Princeton, NJ headquarters.

## Sources

S1. **SEC EDGAR, Form D — Arya for Work, Inc., CIK 0002024148.** Accession
    `0002024148-24-000001`, filed 24 May 2024 (seed) and `0001231919-25-000174`, filed 29 Aug 2025
    (Series A). Retrieved 2026-09-09. Related persons: Kunal Sarda, Arunram Kalaiselvan, Byron Ling
    (Twelve Below) on both; **Aike Ho (ACME Capital) added at the Series A**. No sales commissions or
    finders' fees on either round.

1. `aryahealth.ai` homepage — retrieved 2026-09-09
2. `aryahealth.ai/security` — retrieved 2026-09-09
3. `aryahealth.ai/industries` — retrieved 2026-09-09
4. `aryahealth.ai/privacy-policy` — last updated **20 May 2026**, retrieved 2026-09-09
5. `aryahealth.ai/terms-of-service` — retrieved 2026-09-09
6. `aryahealth.ai/blog/homecare-scheduling-software` — retrieved 2026-09-09
7. `aryahealth.ai/blog/healthcare-workforce-management-software` — retrieved 2026-09-09
8. `aryahealth.ai/blog/arya-health-secures-4-million-…` — **24 Sep 2024**, retrieved 2026-09-09
9. PR Newswire, "Arya Health Secures $18.2M Series A…" — **29 Oct 2025**, retrieved 2026-09-09
10. `homecaremag.com`, "Arya Health Releases Results From Connect Pediatrics Partnership" —
    **8 Apr 2026**, a company release carried as news, retrieved 2026-09-09
11. `hchb.com/hchb-recommended-partner-solutions/` — retrieved 2026-09-09; **Arya is not named**
12. Public record on Connect Pediatrics and Ezra Kuenzi — company LinkedIn, Voyage Dallas and
    Shoutout DFW founder interviews — retrieved 2026-09-09
13. Aggregator profiles (Crunchbase, Tracxn, Getlatka, ZoomInfo — the last filed under
    *arya-for-work-inc*) — retrieved 2026-09-09. **Several of these merge this company with Arya
    Health of Vancouver; the 2016 founding date and the names Gharbi, Sztramko and Vandegriend
    belong to that other company, not this one.**

*Written from public sources only. No contact was made with the vendor. This dossier does not score
and never will; it tests what the vendor claimed and informs the Durability intangible, the A2 scale
flag and the A1 integration rung.*
