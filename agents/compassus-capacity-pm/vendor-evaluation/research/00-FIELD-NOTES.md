# Field notes — what the 11 dossiers say together

**Generated** 2026-09-09 by `_research-matrix.gen.py` from 11 dossiers. Do not hand-edit; change a dossier and rebuild.

The companion to `Vendor-Research-Matrix.xlsx`. The workbook is for looking across; this is for reading. Nothing here is a score.

---

## One line each

| Vendor | The one thing to check |
|---|---|
| **UnityAI** | Six named customers, none in home-based care. |
| **CareConnect** | Their partners page claims an HCHB integration with no mechanism. |
| **servis.ai** | It is a CRM. No episode, discipline or authorization in the data model. |
| **Vitalis Care** | Real HCHB integration, no visible corporate existence, contradicting figures. |
| **AutoMynd** | It would replace HCHB, and its scheduler is autonomous. |
| **CareStitch** | Four employees. We would be larger than everything they have ever done. |
| **Axle Health** | The HCHB sentence is a customer's, not theirs. Ask GrandCare, not Axle, what it does. |
| **AxisCare** | Private Pay, Medicaid, VA. Medicare is not on their payer list. This is the wrong payer world. |
| **MedArrive** | The company answering the questionnaire is eighteen months old inside a six-year-old shell. Ask what is running in production today, and where. |
| **Zeeva** | It sells to our clinicians, not to us. Ask whether they are bidding for our nurses' hours. |
| **Arya Health** | They advertise that the agent decides and deliberately does not offer the coordinator options. That is the exact inverse of our settled principle that the tool recommends and the human accepts. |

## The commonplaces

Facts every vendor shares. A row that nobody publishes cannot tell one vendor from another, and a gap the whole field has is a question for the demo, not a mark against one company.

**Nobody publishes these.** *Uptime · SLA*.

- No row has an identical value across every vendor.

## Where the field splits

Rows where the vendors give genuinely different answers. These are the rows that will decide anything.

**Scheduling unit**

- UnityAI — A clinic appointment slot
- CareConnect — An hourly shift on a case
- servis.ai — A field rep's visit on a route
- Vitalis Care — A hospice visit in a benefit period
- AutoMynd — A visit in an episode
- CareStitch — A visit for a patient
- Axle Health — A visit for a patient, within a market
- AxisCare — An hourly shift on a client
- MedArrive — A visit dispatched from a discharge or referral
- Zeeva — A single visit a clinician chooses to accept, offered across multiple agencies
- Arya Health — An hourly shift on a case — not a visit in an episode. Throughput is quoted as “~3,000 hrs/month” per scheduler

**Decide or advise**

- UnityAI — Decide — the agents perform the work
- CareConnect — Advise — coordinators retain oversight
- servis.ai — Advise — the human assigns, the engine routes
- Vitalis Care — Advise — “approve, adjust, or decline with a click”
- AutoMynd — Decide — “autonomous”, “chosen automatically”, “0 manual assignments”
- CareStitch — Advise — the scheduler dispatches, the clinician accepts what fits
- Axle Health — Advise, with a strong default — “a fully optimized route and patient schedule — no manual planning needed,” but the clinician “can still make changes”
- AxisCare — They say advise; their investor says decide — the product says “automatically identifies and recommends caregiver matches”; the LLR release says an AI-native platform that “actively and intelligently drives scheduling, compliance, and care decisions”
- MedArrive — Decide — “MedArrive matches the right provider to the right visit automatically”. No override language found
- Zeeva — Neither — the clinician decides. A marketplace, not an engine
- Arya Health — Decide — explicitly, and sold as the point. “It doesn't present a list of options for a coordinator to choose from”; “The agent makes and executes scheduling decisions rather than presenting options”; “The agents don't wait to be triggered. They monitor conditions, take action, and push updates to the EMR on their own.” No override language found anywhere

**HCHB evidence**

- UnityAI — not found — no partner listing, press, customer or job posting
- CareConnect — Claimed on their own partners page — no mechanism, no direction, no customer, no HCHB-side listing
- servis.ai — not found
- Vitalis Care — Claimed on their own pages, and the strongest on the roster — “no double-entry”, an “Original HCHB schedule view”, a customer whose title is Director of HCHB operations. Still no published mechanism
- AutoMynd — not found, and structurally unlikely — they sell an EMR, so HCHB is a competitor
- CareStitch — not found
- Axle Health — The strongest on the roster, and it is a customer's sentence, not the vendor's — “Integration with HCHB is smooth and the route optimization saves my clinicians time every day,” Jeff Henderson, Director of Operations, GrandCare. HCHB is not in the integration logo row
- AxisCare — not found — an Integrations Marketplace exists; no EMR appears in it. The categories are billing, onboarding, CRM, payroll, training
- MedArrive — not found — “fits seamlessly into your existing technology ecosystem”, no vendor named
- Zeeva — not found
- Arya Health — Weak, and it is not theirs. HCHB is named nowhere on Arya's own site — the homepage says only “EMR, ATS, HRIS” and the Series A release says “leading EMRs”. The one source naming HCHB is a press-aggregator page gated to both our fetchers. Arya is not on HCHB's Recommended Partner Solutions page [G1]

**Home health share of business**

- UnityAI — 0% — absent from every page and release
- CareConnect — No evidence of any skilled home health; the business is aide agencies
- servis.ai — not found — one landing page among a dozen verticals
- Vitalis Care — 0% — hospice only
- AutoMynd — All of it, since founding
- CareStitch — All of it, since 2019
- Axle Health — All of it by positioning; but the two published case studies are a Medicaid value-based primary care company and a paediatric complex-care company, neither of them a home health agency
- AxisCare — Home care, not home health — “Specializing in Private Pay, Medicaid, and VA Billing”. Medicare is not on the payer list. A “Skilled Care” module exists
- MedArrive — All of it now, in a business eighteen months old. The first five years were a field-provider network of EMTs and paramedics, and that business is gone from the site entirely
- Zeeva — All of it, by positioning — “home health visits” is the entire proposition
- Arya Health — not established — Home Health is listed first of six settings, but the only named customer is pediatric private-duty nursing and the seed-round list omitted home health entirely

**Impact figures with a baseline**

- UnityAI — 0 of ~14
- CareConnect — 0 of ~6
- servis.ai — 0 of 4
- Vitalis Care — 0 of ~7, and two mileage figures contradict: 30% on the site, 55–65% from the CEO
- AutoMynd — 1 of ~5 — the only one on the roster. Three hours → about one hour per client, WellSky early adopters. No period or agency count
- CareStitch — 0 of 1 — “a 60% drop in missed visits”, no agency, period or baseline
- Axle Health — 0 of 6 — 17%+ productivity, 32% driving saved, 55% fewer missed visits, 70%+ less manual scheduling, 900% growth FY2024, “up to 30%” productivity. The Cityblock study gives a period (“the three months following its switch”) and no baseline; the site's 17% and the wire's “up to 30%” are the same claim at two sizes
- AxisCare — 0 of 1 — “AI-Powered Care Analytics Helps Heavenly Care Improve Care Oversight by 280%”. No baseline, no period, and no unit — “care oversight” is not a measurable quantity
- MedArrive — 0 of 2 — “Teams using MedArrive complete 30% more visits with the same staff”; “14x ROI potential”. No period, no baseline, no site count, no customer
- Zeeva — 0 of 0 — the only vendor on the roster that has published no impact claim at all
- Arya Health — 1 of 7. Only “~3,000 hrs/month per scheduler” carries a before-value (“versus ~2,000”). Without one: 25% scheduler capacity · 50% time-to-first-staffing · 70% less administrative effort · 60% less human effort · 6x revenue · “25 cents of every dollar”

## How to read a column

Top to bottom: who they are, what they built, who bought it, whether it stays up, and how much of the column to believe. The last row is the one to read if you read one. Every cell traces to a numbered source in the dossier of the same name; the dossier is the record and this file is not.

