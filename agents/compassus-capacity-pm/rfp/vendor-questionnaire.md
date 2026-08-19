# Capacity & Scheduling Platform — Vendor Questionnaire

**Compassus Home Health**

---

## Part A — Company and product

**A1. Home Care Home Base integration.**
Have you built an integration with Home Care Home Base (HCHB)? Please cover: whether it is live in production with customers today and since when; what it reads from HCHB and what it writes back; how it is implemented (published API, HL7/FHIR, flat file, database, screen automation, other); and how you handle sync latency when data changes on both sides. If you have not built it, tell us your path, what it would need from us, and your timeline.

**A2. Where your product is today.**
Give us a picture of maturity. What is in production with customers today, what is in active development and when it lands, and what is on the roadmap but not yet started?

**A3. Customers and references.**
How many organizations run your product in production today, and how many of those are Medicare-certified home health? Describe your largest deployment by census, branches and clinicians. Please provide two or three references we may contact.

**A4. Market focus.**
What share of your business is Medicare-certified home health, versus hospice, private duty or home care, or other verticals? How does PDGM shape your product, if at all?

---

## Part B — Coverage self-assessment

Mark where you stand on each area. Options: **Production** · **In development** · **Roadmap** · **Not offered**.

| # | Area | | Status | Notes |
|---|---|---|---|---|
| | **Capacity Management** | | | |
| 1 | Workforce supply | Roster, disciplines, roles, competencies, ramp, float pool | | |
| 2 | Availability & reach | Availability and time off, territory, drive-time reachability | | |
| 3 | The capacity math | Visit weighting, targets and ceilings, committed load vs. open room | | |
| | **Scheduling Engine** | | | |
| 4 | Demand | Ingesting ordered visits, authorization, readiness, compliance windows | | |
| 5 | Matching | Discipline and competency fit, clinician and patient needs, clinical timing, continuity | | |
| 6 | Routing & the week | Routing, sequencing, front-loading, week balancing | | |
| 7 | Exceptions | Missed visits, reassignment, coverage, rebooking | | |
| | **Engagement** | | | |
| 8 | Before the visit | Welcome call, availability capture, reminders, confirmation, en-route | | |
| 9 | When plans change | Reschedule, coverage coordination and clinician outreach, urgent same-day needs | | |
| 10 | Across the care team | Multi-discipline coordination, clinician and office updates | | |

---

## Part C — How your product works

**C1. Capacity.**
How does your product determine how much capacity a branch has and how much is left? Cover the unit you measure in and where the inputs come from. Add anything else you think we should understand about how you approach this.

**C2. Capacity in use.**
A branch leader is deciding whether to accept a referral today. What can your product tell them?

**C3. Assignment.**
Walk us through how your product decides which clinician should take a given visit — what it considers, how it weighs those factors, and what a customer can configure.

**C4. Readiness.**
What does your product do with a visit that has been ordered but is not yet schedulable — for example because authorization is still pending, consent from a power of attorney is outstanding, or the clinician it will be assigned to has not yet been determined?

**C5. The week.**
How does your product plan across a week or an episode rather than a single day — and what does it do when that plan breaks mid-week?

**C6. Communication.**
Describe how your product communicates with patients, with clinicians, and with the office. Which of those are automated today, and which still need a person?

---

## Part D — The clinician's place in the model

Scheduling in home health is operationally critical and personally consequential. Many clinicians come to home health for the control it gives them over their own day and week, and any change to how visits get assigned lands on people who feel strongly about it. In our experience adoption, more than algorithm quality, decides whether tools like this succeed. These questions are about how your product treats the clinician.

**D1. What the clinician decides.**
Which scheduling decisions does the clinician make in your product, and which are made for them? Be specific about what they can change, what requires approval, and what they cannot change at all.

**D2. Disagreement.**
When your product proposes an assignment and the clinician disagrees, what happens? Does anything change as a result — for that clinician, or in the model?

**D3. Resistance.**
Describe a deployment where clinicians resisted your product. What did you learn, and what did you change — in the product, or in how you rolled it out?

**D4. Decide or advise.**
Some organizations want the system to decide; others want it to advise. Where was your product designed to sit on that spectrum, and how much of that can a customer change?

---

## Part E — Fit and perspective

**E1. What we did not ask.**
What do you do that we have not asked about, and that you believe would matter to an organization like ours?

**E2. Where a design partner helps.**
We are open to partnering with a product that is strong today and still building. Which parts of what we have described are you actively building, and where would a committed design partner be genuinely useful to you?

**E3. What you chose not to build.**
What have you deliberately chosen not to build, and why?
