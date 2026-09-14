# 02 · The questionnaire, verbatim

Every word the vendor saw, in the order they saw it. Extracted from the blank form (`Compassus-Vendor-Questionnaire-blank.xlsx`, form_version 2026-08-19). Question ids are the ones the scorecard uses.

The form has five sheets: **Overview** (the spec the vendor was told to read — the 41 elements in `spec-elements.json`), **Questionnaire** (below), an empty **Current State Flow Map**, and two hidden sheets, **Lists** (the dropdown options) and **Meta** (the question ids).

## How answers sit in the file

- Question id in column **B**, question text in column **C**, the vendor's answer in the merged **D:G** cell on the same row.
- Each question cell is a bold title, a line break, then the question body.
- Section B is a matrix: one row per area, with four answer columns (D–G).
- `Vendor` is in D4 and `Completed by / date` in D5.


## A · COMPANY AND PRODUCT

### A1 — Home Care Home Base integration

> Have you built an integration with Home Care Home Base (HCHB)? Please cover: whether it is live in production with customers today and since when; what it reads from HCHB and what it writes back; how it is implemented (published API, HL7/FHIR, flat file, database, screen automation, other); and how you handle sync latency when data changes on both sides. If you have not built it, tell us your path, what it would need from us, and your timeline.

### A2 — Customers, scale and references

> How many organizations run your product in production today? Give us the census of your three largest deployments. What is the split of your business across home health, hospice and private duty? References will be a significant part of our process. You do not need to supply the detail now, but please tell us whether you expect to be able to provide them.

### A3 — Measured impact

> What has your product measurably changed for customers already running it? We are interested in workforce cost, clinician productivity, mileage and scheduling efficiency, and in anything else you track. Tell us what you measured, over what period, and how you established the baseline.


## B · COVERAGE SELF-ASSESSMENT

> The Overview tab describes each of these areas in full — it is worth reading before you start. Mark each area three ways, then use the notes column for anything the dropdowns cannot carry: a partner delivering it, a caveat, a target date, or what a status means in your case.


**Capacity Management**

1. **Workforce supply** — Roster, disciplines, roles, competencies, ramp, float pool
2. **Availability & reach** — Availability and time off, territory, drive-time reachability
3. **The capacity math** — Visit weighting, targets and ceilings, committed load vs. open room

**Scheduling Engine**

4. **Demand** — Ingesting ordered visits, authorization, readiness, compliance windows
5. **Matching** — Discipline and competency fit, clinician and patient needs, clinical timing, continuity
6. **Routing & the week** — Routing, sequencing, front-loading, week balancing
7. **Exceptions** — Missed visits, call-outs, reassignment, coverage, rebooking

**Engagement**

8. **Before the visit** — Welcome call, availability capture, reminders, confirmation, en-route
9. **When plans change** — Reschedule, coverage coordination and clinician outreach, urgent same-day needs
10. **Incentives & offers** — Surfacing hard-to-fill visits to clinicians, and any incentive or differential attached
11. **Across the care team** — Multi-discipline coordination, clinician and office updates

## C · HOW YOUR PRODUCT WORKS

### C1 — Capacity

> How does your product determine how much capacity a branch has and how much is left? Cover the unit you measure in and where the inputs come from. Then make it concrete: a branch leader is deciding whether to accept a referral today — what can your product tell them? Add anything else you think we should understand about how you approach this.

### C2 — Assignment

> Walk us through how your product decides which clinician should take a given visit — what it considers, how it weighs those factors, and what a customer can configure.

### C3 — Readiness

> What does your product do with a visit that has been ordered but is not yet schedulable — for example because authorization is still pending, consent from a power of attorney is outstanding, or the clinician it will be assigned to has not yet been determined?

### C4 — The week

> How does your product plan across a week or an episode rather than a single day?

### C5 — When the plan breaks

> Walk us through what your product does when a clinician calls out, a visit is missed, or a patient reschedules. Cover how the open need is identified, how coverage is found and offered, how quickly that happens, and what your product does when nobody takes it.

### C6 — When your product is down

> This product would carry work that hundreds of schedulers do today, so an outage does not slow us down — it stops nurses being deployed. How do you think about business continuity? Cover your uptime over the last twelve months, what a customer experiences during an outage, what they are able to do while it lasts, and what you commit to contractually.

### C7 — Talking to the patient

> How and when do you capture a patient's availability, and what does your product do when that availability conflicts with clinical need? Where your outreach to patients is automated, how far does it go — the channels, whether the conversation is scripted or agentic, what it resolves on its own, and what it hands to a person.


## D · THE CLINICIAN'S PLACE IN THE MODEL

> *Scheduling in home health is operationally critical and personally consequential. Many clinicians come to home health for the control it gives them over their own day and week, and any change to how visits get assigned lands on people who feel strongly about it. In our experience adoption, more than algorithm quality, decides whether tools like this succeed. These questions are about how your product treats the clinician.*

### D1 — What the clinician decides

> Which scheduling decisions does the clinician make in your product, and which are made for them? Be specific about what they can change, what requires approval, and what they cannot change at all. And when your product proposes an assignment the clinician disagrees with, what happens — does anything change as a result, for that clinician or in the model?

### D2 — Decide or advise

> Some organizations want the system to decide; others want it to advise. Where was your product designed to sit on that spectrum, and how much of that can a customer change?

### D3 — Adoption

> How do you measure clinician adoption, what do you consider healthy, and what does your data show across the first six months? Separately — what can a clinician see in your product about their own results?


## E · FIT AND PARTNERSHIP

### E1 — What we did not ask

> What do you do that we have not asked about, and that you believe would matter to an organization like ours?

### E2 — Sharing in the value

> Compassus will be putting a significant investment into the success of this work, including a dedicated scheduling optimization team, SME support, design partnership, a deep people-centric enterprise deployment, and ongoing enhancement tracking.  We are also willing to be a co-marketing partner; presenting at conferences, interviews, white papers, etc.  Given this material investment, we are looking to share in the value we'll be helping to create.  Please share some detail on your proposed / preferred ways of partnering.

### E3 — Deployment and change management

> Changing how clinician schedules get made is sensitive work. What approaches to deployment and change management have you used with other customers? How do you support a customer through it, what have you learned, and what is critical to get right? Include a deployment where clinicians resisted the product, and what you changed as a result.

### E4 — What you chose not to build

> What have you deliberately chosen not to build, and why?


### Section B dropdowns

The vendor could only pick from these. A value not on the list means the cell was typed over or pasted in.

| Column | Options |
|---|---|
| **IN SCOPE** (all 11 areas) | Yes · Through a partner · No · Other — see notes |
| **STATUS** (all 11 areas) | Production — multiple customers · Production — one customer · In development — target date in notes · Roadmap — no date yet · Other — see notes |
| **HOW IT'S DONE** — areas 1–3, Capacity | Live feed from a source system · Imported on a schedule · Maintained by staff in your product · Entered by the clinician · Derived from FT/PT allocation · Other — see notes |
| **HOW IT'S DONE** — areas 4–11, Scheduling and Engagement | Automated end to end · Automated, person approves · System prepares it, person does it · Person does it · Other — see notes |
| **NOTES** | free text |

The asymmetry matters: for the three Capacity areas, *how it's done* asks where the **data** comes from; for the other eight it asks how much of the **work** is automated. The second list maps almost one-to-one onto the Sophistication ladder (automated end to end ≈ runs it; person approves ≈ recommends it; system prepares ≈ checks it; person does it ≈ shows it).

## Which scorecard row each answer feeds

| Question | Scorecard row | Points |
|---|---|---|
| A1 | Home Care Home Base — one rung of six | 20 |
| A2 | Flag row — OK / Watch / STOP-CHECK | none |
| A3 | Flag row — OK / Watch / STOP-CHECK | none |
| B1, B2, B3 | Capacity — CAP1, CAP2, CAP3, each 0–4 | 12 |
| B4 + B5, B6, B7 | Scheduling — SCH1 (demand and matching together), SCH2, SCH3 | 12 |
| B8, B9 + B10, B11 | Engagement — ENG1, ENG2 (plans change and incentives together), ENG3 | 12 |
| C1–C5, C7 | Sophistication — one mark of 0–4 for the whole section | 20 |
| C6 | Flag row — OK / Watch / STOP-CHECK | none |
| D1–D3 | Clinician fit — one mark of 0–4 | 12 |
| E1–E4 | Partnership — one mark of 0–4 | 12 |
| everything | Five intangibles — Strong / Neutral / Concern | none |

Section C is also the **evidence** for every Section B claim. Where they disagree, the scorecard's rule is: believe Section C.

## The 41 elements behind Section B

From `spec-elements.json` — the Overview tab's own bullets. This is the checklist a Section B mark is made against.

### Capacity Management — *The envelope*. How much work a branch can deliver, and how much room is left.

**Workforce supply** (B1)

- `CAP-01` Roster by discipline, role (assessing vs. assistant), FTE and employment type
- `CAP-02` Start-of-care capable clinicians, measured as their own distinct capacity
- `CAP-03` Specialty competencies, plus orientation and ramp status
- `CAP-04` Per-diem and float pool
- `CAP-05` On-call and weekend rotation load

**Availability & reach** (B2)

- `CAP-06` Approved time off and working availability
- `CAP-07` Clinician territory assignment by zip, against branch coverage area
- `CAP-08` Reachability from the clinician's home base, measured by drive time

**The capacity math** (B3)

- `CAP-09` Visit weighting — the point value per visit type, and the productivity target and ceiling it is measured against
- `CAP-10` Committed load vs. open room, by day, week, discipline and territory
- `CAP-11` Referral inflow and discharge outflow against the envelope

### Scheduling Engine — *Filling the envelope*. Which clinician, which day, which route.

**Demand** (B4)

- `SCH-01` Plan-of-care orders, ordered frequency and visit types, from the EMR (Home Care Home Base) and the intake platform
- `SCH-02` Authorization status and payer rules attached to each visit
- `SCH-03` Order, consent and readiness state — what is schedulable, not merely ordered
- `SCH-04` The compliance window each visit has to fall inside

**Matching** (B5)

- `SCH-05` Discipline and role match, specialty competency, acuity to skill level
- `SCH-06` Clinician working pattern, needs and restrictions
- `SCH-07` Patient and caregiver needs, restrictions and availability, sourced from the patient
- `SCH-08` Clinical timing — diagnosis-driven cadence, competing appointments, infection-control sequencing
- `SCH-09` Continuity of care, and supervisory visit dependencies

**Routing & the week** (B6)

- `SCH-10` Home base start and end, route proximity, mileage
- `SCH-11` Appointment time windows and intra-day sequencing
- `SCH-12` Front-loading, pace against the plan of care, day-by-day balancing

**Exceptions** (B7)

- `SCH-13` Missed-visit management and tracking — and reducing the occurrence
- `SCH-14` Reassignment, coverage, and rebooking inside the window

### Engagement — *Making it happen*. Turning a schedule into delivered visits — with patients, clinicians and the office.

**How this should run** (no B area — evidenced from C7 and D1)

- `ENG-01` Outreach carried by the platform itself — agentic voice, text and email — rather than queued up for a coordinator to work
- `ENG-02` Staff able to see it, intervene, override, and take any conversation back

**Before the visit** (B8)

- `ENG-03` New-patient welcome call
- `ENG-04` Patient availability captured before the visit is booked
- `ENG-05` Automated reminders and en-route notification
- `ENG-06` The day-before confirmation round automated for every patient, every day
- `ENG-07` The schedule staying pliable until that confirmation, so clinician and capacity changes can land before the patient is told
- `ENG-08` Channel and communication-preference management

**When plans change** (B9)

- `ENG-09` Reschedule coordination with the patient
- `ENG-10` Coverage coordination — matching potential clinicians to an open need, and reaching them directly
- `ENG-11` Call-out coverage, and the urgent or prioritized needs that surface during the day
- `ENG-13` Failed-visit and no-show follow-up and rebooking

**Incentives & offers** (B10)

- `ENG-12` Incentives or differentials attached to hard-to-fill visits, and offered to the clinicians who can take them

**Across the care team** (B11)

- `ENG-14` Multi-discipline visit coordination
- `ENG-15` Care-team and office coordination updates
- `ENG-16` A clinician view of their own schedule and their own results — the case for the change, made to the person it lands on

One more line sits on the Overview with no group of its own: *"The staff time coordination consumes today."* It is not scored anywhere. A vendor who speaks to it directly has answered a question the spec asked and the scorecard forgot.

---
*Scorecard v3.0 · questionnaire form_version 2026-08-19 · generated from `_scorecard.gen.py` at `fd651c5`*
