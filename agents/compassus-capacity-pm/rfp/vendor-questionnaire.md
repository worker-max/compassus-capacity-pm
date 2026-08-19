# Capacity & Scheduling Platform — Vendor Questionnaire

**Compassus Home Health**

Please return this completed document by **Friday, September 4, 2026**.

Answer in your own words. We are deliberately asking open questions rather than a feature
checklist, because we want to understand how you think about this problem, not only what you
have built. Where a question does not apply to your product, say so plainly — "we don't do that"
is a useful and respected answer, and a candid gap costs you far less than an overstated capability.

Length guidance: most answers should run a short paragraph. There is no advantage in volume.

---

## Part A — Company and product

**A1. Home Care Home Base integration.**
Have you built an integration with Home Care Home Base (HCHB)?

- Is it live in production with paying customers today? Since when, and with how many?
- What does the integration read from HCHB, and what does it write back?
- How is it implemented — published API, HL7/FHIR interface, flat-file exchange, database
  connection, screen automation/RPA, or something else?
- How do you handle synchronization latency and conflicts when data changes on both sides?
- If you have not built it: what is your path, what would it require from us, and what is your
  honest timeline?

**A2. In production versus in progress.**
For every capability you describe anywhere in this document, label it:
**(P)** in production with paying customers · **(B)** built, not yet in production ·
**(D)** in active development with a committed release date · **(R)** roadmap or concept.
We will ask to see anything marked (P) working with live data.

**A3. Customers.**
How many Medicare-certified home health organizations run your product in production today?
Describe your largest deployment by census, branch count and clinician count. Please provide two
or three references we may contact.

**A4. Company maturity.**
Year founded, current headcount, and where you are in your funding cycle (bootstrapped, seed,
Series A/B/C, PE-backed, profitable). Most recent raise and date. We are not asking for cap-table
detail — we are trying to understand the durability of a multi-year partnership.

**A5. Market focus.**
What share of your business is Medicare-certified home health, versus hospice, private duty/home
care, or other verticals? How does PDGM shape your product, if at all?

**A6. Deployment, security and implementation.**
Hosting model, SOC 2 and/or HITRUST status, willingness to sign a BAA, and how PHI is handled.
What does a typical implementation look like for an organization of our size — duration, phases,
and what you need from us?

---

## Part B — Coverage self-assessment

Mark your current coverage of each area. Use the same labels as A2:
**(P)** production · **(B)** built, not live · **(D)** in development · **(R)** roadmap ·
**(N)** not offered · **(PT)** delivered through a named partner (say who).

| # | Area | Coverage | Notes |
|---|---|---|---|
| **Capacity Management** ||||
| 1 | Workforce supply — roster, disciplines, roles, competencies, ramp, float pool | | |
| 2 | Availability & reach — clinician-supplied availability, territory, drive-time reachability | | |
| 3 | The capacity math — visit weighting, targets and ceilings, committed load vs. open room | | |
| **Scheduling Engine** ||||
| 4 | Demand — ingesting ordered visits, authorization, readiness, compliance windows | | |
| 5 | Matching — discipline/competency fit, clinician and patient needs, clinical timing, continuity | | |
| 6 | Routing & the week — route optimization, sequencing, front-loading, week balancing | | |
| 7 | Exceptions — missed visits, reassignment, coverage, rebooking | | |
| **Engagement** ||||
| 8 | Before the visit — welcome call, availability capture, reminders, confirmation, en-route | | |
| 9 | When plans change — reschedule, coverage coordination and clinician outreach, call-out and urgent same-day needs, no-show follow-up | | |
| 10 | Across the care team — multi-discipline coordination, clinician and office updates | | |

---

## Part C — How your product works

### Capacity Management

**C1.** Describe how your product represents the supply of clinical labor available in a branch.
What are the inputs, and where does each one come from?

**C2.** Clinicians are not interchangeable. How does your product represent what a given clinician
is and is not able to take on? Walk us through a concrete example.

**C3.** How does a clinician's availability and time off get into your system, who maintains it,
and how current is it in practice?

**C4.** How does geography affect whether a given clinician can serve a given patient in your
product?

**C5.** How do you quantify how full a clinician or a branch is? What unit do you use, who sets
it, and how is it calibrated?

**C6.** A manager wants to know what capacity is available over the next seven days. Describe what
your product shows them, and what decision it is designed to support.

**C7.** What can your product tell a leader about whether the branch can accept a new referral
today? If it cannot answer that question, say so.

### Scheduling Engine

**C8.** How does ordered patient demand enter your system? What do you require in order to treat a
visit as schedulable, and what does your product do with a visit that has been ordered but is not
yet schedulable?

**C9.** Describe how your product decides which clinician should take a given visit. What factors
are considered, how are they prioritized, and can that prioritization be configured — by whom?

**C10.** How do you handle constraints and preferences that belong to the clinician? Separately,
how do you handle those that belong to the patient or their caregiver? Where do those inputs come
from?

**C11.** How does your product handle timing requirements that come from the clinical order or
from regulation, as distinct from preference?

**C12.** Describe your routing capability, including what data it uses to determine travel between
visits.

**C13.** How does your product think about a week or an episode, rather than a single day?

**C14.** What happens in your product when a scheduled visit does not happen?

**C15.** Does your product schedule autonomously, recommend for approval, or assist a human who
decides? Explain the division of labor you intend between your product and a person, and why you
designed it that way.

**C16.** How, if at all, do field clinicians interact with your product directly?

### Engagement

**C17.** List every way your product communicates with a patient about their visits. For each, say
whether it is automated, who triggers it, and what channel it uses. Separately, describe how it
communicates with clinicians and with office staff.

**C18.** How and when does your product capture a patient's availability or scheduling preferences?

**C19.** What happens when a patient wants to change a visit?

**C20.** What happens when a clinician is unavailable at short notice and their day has to be
covered? How does your product identify who could take the work, and how does it reach them? Does
the same mechanism handle an urgent need that appears part-way through a day?

**C21.** How do you handle communication consent, opt-out, language preference, and the applicable
regulations on automated outreach?

---

## Part D — Fit and perspective

**D1.** Of the three areas in Part B, where is your product genuinely strongest, and where is it
weakest? We are mapping a market, not scoring a test — a clear-eyed answer helps both of us.

**D2.** **What do you do that we have not asked about, and that you believe would matter to an
organization like ours?** This is one of the most useful questions on this document — please give
it real thought.

**D3.** What do your best customers get from you that they did not expect when they bought?

**D4.** What have you deliberately chosen *not* to build, and why?

**D5.** Having read our one-page overview and current-state process map, what would you want to
know about our operation that this questionnaire did not ask?

---

### Returning this document

Send your completed response to **[sender email]** by **Friday, September 4, 2026**.

If anything here is ambiguous, or you would like to talk something through before you write, we
are happy to make time — just reply and we will schedule a short call.
