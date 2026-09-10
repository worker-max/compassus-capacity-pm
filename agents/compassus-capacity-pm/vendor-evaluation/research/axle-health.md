# Axle Health — research dossier

Researched 2026-09-07 · sources retrieved 2026-09-07 · confidence: **high**

*Confidence note.* Company facts are high: founding year, batch, location, founder, investors and
headcount agree across the company's own site, its Y Combinator listing, a dated wire release and
two trade-press reports. Product facts are high: every product page was read directly. Customer
facts are **medium-high** — three customers are named on the site with two full case studies, and
the fourth (GrandCare) was confirmed as a real Medicare home health agency with a real employee of
that name, but no customer has been reached and no customer count is published. Written before
reading the vendor's return.

**Identity.** The roster first spelled this *Axel Health*. **No such company exists in this field.**
The company is **Axle Health**, Los Angeles, Y Combinator Winter 2021, founded 2020 by Adam Stansell
(CEO) and Connor Hailey out of Uber and Motive. Site `axlehealth.com`; app package
`com.axlehealth.axlehealth`. Confirm the return's contact email domain is `axlehealth.com`. **If it
is not, stop — nothing here applies.** Not Axelera AI; not the two unrelated car-maintenance apps
also called *axle*.

---

## At a glance

The machine-readable face of this dossier. `_research-matrix.gen.py` reads these rows to
build `Vendor-Research-Matrix.xlsx`; the prose below is the record. Bracketed numbers are
source ids from the *Sources* list at the foot of this file. *Not found* is a finding.

| Fact | Finding |
|---|---|
| **COMPANY** | |
| Founded · HQ | 2020 · Los Angeles, California; office in Santa Monica, five days a week on site [6] [8] [9] |
| Legal entity | Axle Health — no incorporation record found; Y Combinator W21 [6] [7] |
| Ownership · raised · last round | **$10M Series A, 22 May 2025**, led by F-Prime; Y Combinator, Pear VC, Lightbank, Pioneer Fund, TRAC AI [7] [2] [9] |
| Headcount · trend | **34** (Apr 2026) · 28 (2024) · **rising** [6] [8] |
| Leadership from home health | ***not found*** — CEO from Uber, Motive, consulting and banking; no clinical or home health operations name published [6] [7] |
| Pivots or rebrands in 3 years | **None** — same name, same problem, since 2020 [6] [7] |
| Home health share of business | All of it by positioning; **but the two published case studies are a Medicaid value-based primary care company and a paediatric complex-care company, neither of them a home health agency** [3] [4] [10] |
| **PRODUCT** | |
| HCHB evidence | **The strongest on the roster, and it is a customer's sentence, not the vendor's** — “Integration with HCHB is smooth and the route optimization saves my clinicians time every day,” Jeff Henderson, Director of Operations, GrandCare. **HCHB is not in the integration logo row** [2] [5] |
| Other EMRs named | Epic, athenahealth, WellSky, Axxess, Statewise — logos on the office-staff page [2] [1] |
| Scheduling unit | A visit for a patient, within a market [1] [4] |
| Capacity | **Claimed, not shown** — “Predictive Staffing & Scheduling”, “predictive demand insights”, “forecasting tools”; no forecast horizon, unit or method published [2] |
| Scheduling | Real and central — AI matching, route optimisation, real-time reroute, live map, schedule-adherence and utilisation tracking; centralised **or** clinician-driven, configurable [1] [2] |
| Engagement | **Real and patient-facing** — automated reminders, live ETAs, feedback capture by SMS and phone; a patient booking solution [1] [6] |
| Decide or advise | **Advise, with a strong default** — “a fully optimized route and patient schedule — no manual planning needed,” but the clinician “can still make changes” [11] |
| Clinician app | iOS (id 6445966671) and Android (`com.axlehealth.axlehealth`); **iOS has too few ratings to display an average** [12] [13] |
| **CUSTOMERS** | |
| Named home health customers | **GrandCare Health Services** (Southern California Medicare home health; acquired by The Pennant Group, Jul 2025) — named only in a testimonial. Cityblock, Imagine Pediatrics and Penn Medicine are named but **are not home health agencies** [2] [3] [4] [5] |
| Largest known deployment | Cityblock — “over 100,000 Medicaid and Medicare-Medicaid dually eligible beneficiaries” in “15 markets across 7 states”, though not all on Axle [3] |
| Customer count | *not found* [7] |
| Impact figures with a baseline | **0 of 6** — 17%+ productivity, 32% driving saved, 55% fewer missed visits, 70%+ less manual scheduling, 900% growth FY2024, “up to 30%” productivity. The Cityblock study gives a period (“the three months following its switch”) and **no baseline**; the site's 17% and the wire's “up to 30%” are the same claim at two sizes [1] [2] [3] [7] |
| Independent customer voice | **Yes — the only one on the roster** — a named individual at a named, verifiable Medicare home health agency, on the vendor's own page; plus Cityblock's CPO quoted by name [3] [5] |
| **TRUST AND CONTINUITY** | |
| Security attestation | ***not found*** — no SOC 2, HITRUST or trust page found [1] [6] |
| Uptime · SLA | *not found* |
| Named dependencies | *not found* — “proprietary logistics algorithms”, “patent-pending logistics engine”; no cloud, model or API vendor named [6] [7] |
| Pricing signal | **Savings-based** — “Axle's cost is based on your estimated savings — our team will conduct an ROI analysis for you and use that to determine the price”; a public ROI calculator [1] |
| **THE READ** | |
| The one thing to check | The HCHB sentence is a customer's, not theirs. Ask GrandCare, not Axle, what it does. |
| Ask them first | Put us on a reference call with Jeff Henderson at GrandCare — and tell us why HCHB is not in your own integration row. [2] [5] |
| Would we be their largest customer | **In home health, probably yes.** Cityblock is larger and is not a home health agency; no home health customer count is published [3] [7] |
| Red flags to test | **RF-18** “17%+” on the site, “up to 30%” in their own funding release · **RF-01** HCHB appears in a testimonial and not in their integration row · **RF-07 STOP-CHECK** no attestation, no uptime, no SLA · **RF-08** capacity claimed as “predictive”, never shown [1] [2] [7] |
| Where their own sources disagree | **RF-18** — clinician productivity rises **“17%+”** on their site and **“up to 30%”** in their own May 2025 funding release [1] [7] |
| Confidence | high |

---

## One paragraph

Axle Health is a thirty-four-person Los Angeles company, founded in 2020 by Uber and Motive
alumni, that sells scheduling and workforce-management software to organisations sending clinicians
into homes. It is a logistics company that chose healthcare, not a healthcare company that
discovered logistics — and unlike servis.ai, which is the same sentence used as an accusation, Axle
has stayed on that one problem for six years, put a patient-engagement layer on top of it, and won
customers who are recognisably in our business. It raised a $10M Series A in May 2025 led by
F-Prime. Its named reference customers are mostly value-based and paediatric home-visit companies
rather than Medicare-certified home health agencies; the single exception is the one that matters
most to us, and it is the source of the only credible HCHB integration statement found anywhere on
this roster.

## The company

| Fact | Finding | Source · date |
|---|---|---|
| Founded | 2020; Y Combinator Winter 2021 batch | YC company page [6] · retrieved 2026-09-07 |
| Headquarters, offices | Los Angeles, California; the careers page describes “daily lunch at our Santa Monica HQ” and on-site five days a week | axlehealth.com/careers [9], YC [6] · 2026-09-07 |
| Ownership and funding | **$10M Series A announced 22 May 2025**, led by **F-Prime**, with Y Combinator, Pear VC and Lightbank participating; the about page also lists **Pioneer Fund** and **TRAC AI**. Total raised across all rounds *not found* | PR Newswire [7] · 2025-05-22; Home Health Care News [10] · 2025-05; axlehealth.com/about [8] |
| Headcount, and trend | **34** as of 30 Apr 2026, against **28** in 2024 — growing, and small | Company databases [6] [8] · 2026 |
| Leadership | **Adam Stansell**, co-founder and CEO — Uber, Motive (formerly KeepTruckin), management consulting, investment banking. **Connor Hailey**, co-founder. Trade press describes “several former Uber executives”. **No clinician, no home health operator and no HCHB alumnus is named anywhere on the site** | YC [6], PR Newswire [7], HHCN [10] · 2025–2026 |
| Acquisitions, mergers, pivots, rebrands | **None found.** Same name and same problem statement since 2020 — one of only two vendors on the roster of which that is true | [6] [7] |
| Litigation, breaches, regulatory actions | *not found* | — |
| Lines of business, and the share that is home health | One line of business. But read *home health* carefully: the company says “home health providers, hospice organizations, and in-home clinical services companies”, and its two published case studies are neither home health nor hospice | axlehealth.com [1], case studies [3] [4] |

**A small thing worth knowing.** The sitemap still carries Webflow template blog posts — *“10 proven
ways to save more money every month”*, *“Drowning in subscriptions: tips to track and cancel unused
services”*. Leftovers from a marketing-site rebuild, not evidence of anything about the product, but
the same tell as CareStitch's placeholder testimonials and AutoMynd's template team pages: this is a
recently rebuilt site and not everything on it has been checked. Note it and move on.

## The product

| Fact | Finding | Source · date |
|---|---|---|
| What it does, in their words | “Scheduling and workforce management software for home healthcare providers. The Axle platform includes a mobile app for clinicians, an operations dashboard for office teams, proprietary logistics algorithms to optimize scheduling, and a patient engagement and booking solution.” | YC [6] · 2026-09-07 |
| What it does, in a customer's words | “Integration with HCHB is smooth and the route optimization saves my clinicians time every day.” — Jeff Henderson, Director of Operations, GrandCare. And “Our clinicians love it.” | axlehealth.com/office-staff [2], /clinician-experience [11] · 2026-09-07 |
| Which of the three arenas the public material covers | **Scheduling** in full. **Engagement** in full, and patient-facing — reminders, live ETAs, feedback capture, booking. **Capacity** by assertion only: “Predictive Staffing & Scheduling”, “predictive demand insights”, “forecasting tools”, with no horizon, unit, method or screenshot | [1] [2] · 2026-09-07 |
| Evidence of an HCHB integration | **One customer testimonial, quoted above, attributed to a named person at a named agency.** No partner listing, no press release, no HCHB-side confirmation, no mechanism, no direction, no frequency. **And HCHB is absent from the integration logo row on the same page** that carries the testimonial | [2] [5] |
| Other EMR integrations named | Epic, athenahealth, WellSky, Axxess, Statewise — shown as logos, with no customer named against any of them | [1] [2] |
| Agentic or automated patient outreach | **Real, and described concretely** — automated reminders, live ETAs and feedback capture over SMS and phone; the May 2025 wire release says the round funds “generative AI patient engagement solutions”, so the agentic part is roadmap | [1] [7] [10] |
| Clinician-facing app | iOS App Store id 6445966671; Google Play `com.axlehealth.axlehealth`. **The iOS listing has too few ratings to display an average**; Play reviews are mixed, with usability complaints. Install counts *not found* | App Store [12], Google Play [13] · 2026-09-07 |
| Pricing signals | “Axle's cost is based on your estimated savings — our team will conduct an ROI analysis for you and use that to determine the price.” A public ROI calculator sits on the site | axlehealth.com [1], /roi-calculator · 2026-09-07 |

## The customers

| Fact | Finding | Source · date |
|---|---|---|
| Named home health customers | **GrandCare Health Services** — a real Southern California Medicare home health agency specialising in orthopaedic and cardiac recovery, **acquired by The Pennant Group in July 2025**. It appears on Axle's site only as a testimonial, not as a case study or logo | axlehealth.com [2], GrandCare corporate records [5] · 2025–2026 |
| Other named customers | **Cityblock** (value-based primary care, Medicaid and dual-eligible, 100,000+ members, 15 markets, 7 states); **Imagine Pediatrics** (paediatric complex care at home); **Penn Medicine** (logo only) | [1] [3] [4] |
| Largest known deployment | Cityblock, by member count — but the case study does not say how many of those members or markets are on Axle | [3] |
| Customers lost or churned | *not found* | — |
| Case studies | **Cityblock:** “In the three months following its switch to Axle, Cityblock increased completed home visits with reduced drive time; decreased time spent scheduling and managing field teams; and optimized resource allocation across markets and visits,” headlined “increased clinician productivity 17%+”. **A period, no baseline, no site count, no absolute numbers.** Quoted by Adam Weinstein, Chief Product Officer — a general endorsement, no figures of his own. **Imagine Pediatrics:** a second study, same shape | [3] [4] · 2026-09-07 |

## What the outside view says about the questionnaire

- **A1.** Expect a claimed HCHB integration. The outside view **partly supports it** — for the first
  time on this roster, a named person at a named, verifiable Medicare home health agency says it
  works. That is a rung above CareConnect's unattributed partner card and level with Vitalis Care's.
  It is still not proof: no mechanism, no direction, no frequency, no date, and **HCHB is missing
  from Axle's own integration logo row**, which is a strange omission if the integration is a
  product rather than one customer's project. Ask for the GrandCare reference call by name.
- **A2.** Expect scale language. The outside view is thin: thirty-four people, $10M raised, no
  published customer count. Compassus is about three thousand clinicians and about eighty branches.
  **We would very likely be their largest customer.** The 900% FY2024 growth figure is a
  small-base number and should be read as one.
- **A3.** Expect percentages. There are six of them and **not one carries a baseline**. Two of them
  are the same claim at two different sizes — the site says productivity rises “17%+”, the funding
  release says “up to 30%”. Ask which, and over what.
- **C6.** Expect a security answer. **Nothing was found** — no SOC 2, no HITRUST, no trust page, no
  uptime figure, no SLA. For a company that would be dispatching three thousand clinicians, this is
  the gap to press, and it is a gap the whole roster shares.
- **E2.** Expect “the tool recommends and the human accepts”. The public material is close to our
  position but leans further toward the engine than we do: the clinician gets “a fully optimized
  route and patient schedule — no manual planning needed” and *may* change it. That is a strong
  default with an override, not a recommendation with an acceptance. Worth one question.

## Durability read — evidence only

Six years old, thirty-four people and growing, one product, no rebrand, a named institutional lead
investor in F-Prime, and a founder who has stayed. Against that: $10M is a small Series A for a
company that would be running the schedule for eighty branches; no clinical leadership is published;
and the customer base visible from outside is concentrated in value-based and paediatric home-visit
companies rather than Medicare home health, which means the product's fit with our episode,
discipline and authorization structure is asserted rather than demonstrated. **The one durability
fact that cuts both ways: GrandCare, the source of the HCHB statement, was acquired by The Pennant
Group in July 2025.** A reference customer that has changed owners may no longer be on the product.

## Questions the research raises

1. Put Jeff Henderson at GrandCare on a reference call and ask what the HCHB integration actually
   moves, in which direction, how often, and who built it.
2. Why is HCHB absent from the integration logo row on the same page as the HCHB testimonial?
3. Is GrandCare still a customer after the Pennant acquisition?
4. Productivity: “17%+” or “up to 30%”? Against what baseline, measured how?
5. Show the capacity forecast. What does it forecast, at what horizon, in what unit, and against
   what actuals?
6. Are the “predictive staffing” features shipped, or are they the generative-AI roadmap the Series
   A was raised to build?
7. SOC 2 or HITRUST: held, in progress, or neither? Uptime commitment and SLA?
8. How many customers, and how many are Medicare-certified home health agencies?
9. Named subprocessors — cloud, model provider, SMS carrier — and where PHI sits.
10. What does the clinician actually control? Can they decline a visit, and what happens then?

## Not found

SOC 2, HITRUST or any security attestation. A trust or status page. Uptime or SLA figures. Total
funding raised across all rounds. An incorporation record. Any named subprocessor or model vendor.
Customer count. Any Medicare home health customer named as a case study rather than a testimonial.
App install counts. Any litigation, breach or regulatory action. A published forecast horizon or
method for the “predictive staffing” claim. Any home health clinician or operator in leadership.

## Sources

1. Axle Health — home page, `https://www.axlehealth.com/`. Retrieved 2026-09-07.
2. Axle Health — “Office Staff”, `https://www.axlehealth.com/office-staff`. Carries the HCHB
   testimonial and the integration logo row. Retrieved 2026-09-07.
3. Axle Health — “Cityblock increases clinician productivity”,
   `https://www.axlehealth.com/cityblock-increases-clinician-productivity`. Retrieved 2026-09-07.
4. Axle Health — “Imagine Pediatrics expands access to care at home with Axle Health”,
   `https://www.axlehealth.com/imagine-pediatrics-expands-access-to-care-at-home-with-axle-health`.
   Retrieved 2026-09-07.
5. GrandCare Health Services — corporate and personnel records corroborating Jeffrey Henderson, PT,
   DPT, and GrandCare's acquisition by The Pennant Group, July 2025. Public professional listings.
   Retrieved 2026-09-07. **Note the title differs**: Axle's site says “Director of Operations”;
   public records say “Director of Rehabilitation Services and Interim Corporate Administrator”.
6. Y Combinator — Axle Health company page, `https://www.ycombinator.com/companies/axle-health`.
   Batch W21, founded 2020, team size 28, Los Angeles. Retrieved 2026-09-07.
7. PR Newswire — “Axle Health Secures $10M in Series A Financing to Revolutionize Home Health
   Operations”, 22 May 2025. Retrieved 2026-09-07.
8. Axle Health — “About”, `https://www.axlehealth.com/about`. Investor list. Retrieved 2026-09-07.
9. Axle Health — “Careers”, `https://www.axlehealth.com/careers`. Santa Monica HQ. Retrieved
   2026-09-07.
10. Home Health Care News — “Axle Health Raises $10M To Accelerate AI Home-Based Care Tech
    Development”, May 2025. **Gated to direct fetch (HTTP 403); read through search summary only.**
    Retrieved 2026-09-07.
11. Axle Health — “Clinician experience”, `https://www.axlehealth.com/clinician-experience`.
    Retrieved 2026-09-07.
12. Apple App Store — Axle Health, id 6445966671. “Not enough ratings or reviews to display an
    overview.” Retrieved 2026-09-07.
13. Google Play — Axle Health, `com.axlehealth.axlehealth`. Retrieved 2026-09-07.
