# Capacity & Scheduling Platform — Vendor Questionnaire

**Compassus Home Health**

Please return this completed document by **Friday, September 4, 2026**.

**A note on how to answer.** This is a first-round questionnaire. We are trying to understand the
shape of your product and how you think about this problem — not to score a feature checklist. We
will go deeper with a smaller group on a call.

**We are not screening for "everything is already built."** We would rather partner with a product
that is strong and working today and still developing in places, than with one that claims complete
coverage. Tell us plainly what is live, what is in progress, and what is still an idea. A candid gap
costs you nothing here; an overstated capability will cost you later.

Most answers should run a short paragraph. There is no advantage in volume. Twenty questions and
one table.

---

## Part A — Company and product

**A1. Home Care Home Base integration.**
Have you built an integration with Home Care Home Base (HCHB)? Please cover: whether it is live in
production with customers today and since when; what it reads from HCHB and what it writes back;
how it is implemented (published API, HL7/FHIR, flat file, database, screen automation, other); and
how you handle sync latency when data changes on both sides. **If you have not built it**, tell us
your path, what it would need from us, and your honest timeline.

**A2. Where your product actually is.**
Give us an honest picture of maturity. What is in production with customers today, what is in
active development and when it lands, and what is on the roadmap but not yet started? Use the
labels **(P)** production · **(D)** in development · **(R)** roadmap throughout this document,
including in the table in Part B.

**A3. Customers and references.**
How many organizations run your product in production today, and how many of those are
Medicare-certified home health? Describe your largest deployment by census, branches and
clinicians. Please provide two or three references we may contact.

**A4. Company maturity.**
Year founded, current headcount, and where you are in your funding cycle (bootstrapped, seed,
Series A/B/C, PE-backed, profitable), including your most recent raise and date. We are not asking
for cap-table detail — we are trying to understand the durability of a multi-year partnership.

**A5. Market focus.**
What share of your business is Medicare-certified home health, versus hospice, private duty/home
care, or other verticals? How does PDGM shape your product, if at all?

**A6. Deployment and security.**
Hosting model, SOC 2 and/or HITRUST status, willingness to sign a BAA, and how PHI is handled.
Roughly what does implementation look like for an organization of our size?

---

## Part B — Coverage self-assessment

The one-page overview we sent describes three areas and the sections inside them. Mark where you
stand on each. Use **(P)** production · **(D)** in development · **(R)** roadmap ·
**(N)** not offered · **(PT)** delivered through a named partner — say who.

| # | Area | Status | Notes — anything you want us to understand |
|---|---|---|---|
| **Capacity Management** ||||
| 1 | Workforce supply — roster, disciplines, roles, competencies, ramp, float pool | | |
| 2 | Availability & reach — availability and time off, territory, drive-time reachability | | |
| 3 | The capacity math — visit weighting, targets and ceilings, committed load vs. open room | | |
| **Scheduling Engine** ||||
| 4 | Demand — ingesting ordered visits, authorization, readiness, compliance windows | | |
| 5 | Matching — discipline and competency fit, clinician and patient needs, clinical timing, continuity | | |
| 6 | Routing & the week — routing, sequencing, front-loading, week balancing | | |
| 7 | Exceptions — missed visits, reassignment, coverage, rebooking | | |
| **Engagement** ||||
| 8 | Before the visit — welcome call, availability capture, reminders, confirmation, en-route | | |
| 9 | When plans change — reschedule, coverage coordination and clinician outreach, urgent same-day needs | | |
| 10 | Across the care team — multi-discipline coordination, clinician and office updates | | |

---

## Part C — How your product works

**C1. Capacity.** How does your product determine how much capacity a branch has and how much is
left? Cover the unit you measure in, where the inputs come from, who maintains them, and how you
represent the fact that clinicians are not interchangeable.

**C2. Capacity in use.** A branch leader is deciding whether to accept a referral today. What can
your product tell them? If it cannot answer that question, say so.

**C3. Assignment.** Walk us through how your product decides which clinician should take a given
visit — what it considers, how it weighs those factors, and what a customer can configure.

**C4. Readiness.** What does your product do with a visit that has been ordered but is not yet
schedulable — for example because authorization, consent or an order is outstanding?

**C5. The week.** How does your product plan across a week or an episode rather than a single day —
and what does it do when that plan breaks mid-week?

**C6. Communication.** Describe how your product communicates with patients, with clinicians, and
with the office. Which of those are automated today, and which still need a person?

---

## Part D — The clinician's place in the model

Scheduling in home health is operationally critical and personally consequential. Many clinicians
come to home health for the control it gives them over their own day and week, and any change to
how visits get assigned lands on people who feel strongly about it. In our experience adoption,
more than algorithm quality, decides whether tools like this succeed. These four questions are
about how your product treats the clinician.

**D1.** Which scheduling decisions does the clinician make in your product, and which are made for
them? Be specific about what they can change, what requires approval, and what they cannot change
at all.

**D2.** When your product proposes an assignment and the clinician disagrees, what happens? Does
anything change as a result — for that clinician, or in the model?

**D3.** Describe a deployment where clinicians resisted your product. What did you learn, and what
did you change — in the product, or in how you rolled it out?

**D4.** Some organizations want the system to decide; others want it to advise. Where was your
product designed to sit on that spectrum, and how much of that can a customer change?

---

## Part E — Fit and perspective

**E1.** Across the three areas in Part B, where is your product genuinely strongest, and where is
it weakest? We are mapping a market, not scoring a test.

**E2.** **What do you do that we have not asked about, and that you believe would matter to an
organization like ours?** This is one of the most useful questions here — please give it real
thought.

**E3.** We are open to partnering with a product that is strong today and still building. Which
parts of what we have described are you actively building, and where would a committed design
partner be genuinely useful to you?

**E4.** What have you deliberately chosen *not* to build, and why?

---

### Returning this document

Send your completed response to **[sender email]** by **Friday, September 4, 2026**.

If anything here is ambiguous, or you would like to talk something through before you write, reply
and we will make time. We would rather you ask than guess.
