# -*- coding: utf-8 -*-
"""Content for the vendor questionnaire workbook. Edit here, then re-run _make.py.

Anything added or reworked in the 20 Aug round carries a marker as the last element
of its tuple — "new" or "edit". The builder highlights those cells yellow so the
changes are findable in the meeting. Clear the markers once the round is settled.
"""

# Three discrete dropdowns replace one. In scope answers "do you do this at all",
# status answers "how far along", delivery answers "does a person still do it".
IN_SCOPE_OPTIONS = ["Yes", "Through a partner", "No"]
STATUS_OPTIONS = [
    "Production — multiple customers",
    "Production — one customer",
    "In development — target date in notes",
    "Roadmap — no date yet",
]
DELIVERY_OPTIONS = [
    "Automated end to end",
    "Automated, person approves",
    "System prepares it, person does it",
    "Person does it",
]

# ---------------------------------------------------------------- TAB 1 · questionnaire
SECTIONS = [
    ("A", "Company and product", None, [
        ("A1", "Home Care Home Base integration",
         "Have you built an integration with Home Care Home Base (HCHB)? Please cover: whether it is "
         "live in production with customers today and since when; what it reads from HCHB and what it "
         "writes back; how it is implemented (published API, HL7/FHIR, flat file, database, screen "
         "automation, other); and how you handle sync latency when data changes on both sides. If you "
         "have not built it, tell us your path, what it would need from us, and your timeline."),
        ("A2", "Customers, scale and references",
         "How many organizations run your product in production today, and how many of those are "
         "Medicare-certified home health? Give us the census of your three largest deployments, along "
         "with branch and clinician counts. What share of your business is Medicare-certified home "
         "health, versus hospice, private duty or home care? References will be a significant part of "
         "our process. You do not need to supply the detail now, but please tell us whether you expect "
         "to be able to provide them.", "edit"),
        ("A3", "Measured impact",
         "What has your product measurably changed for customers already running it? We are interested "
         "in workforce cost, clinician productivity, mileage and scheduling efficiency, and in anything "
         "else you track. Tell us what you measured, over what period, and how you established the "
         "baseline.", "new"),
    ]),
    ("C", "How your product works", None, [
        ("C1", "Capacity",
         "How does your product determine how much capacity a branch has and how much is left? Cover "
         "the unit you measure in and where the inputs come from. Add anything else you think we "
         "should understand about how you approach this."),
        ("C2", "Capacity in use",
         "A branch leader is deciding whether to accept a referral today. What can your product tell "
         "them?"),
        ("C3", "Assignment",
         "Walk us through how your product decides which clinician should take a given visit — what it "
         "considers, how it weighs those factors, and what a customer can configure."),
        ("C4", "Readiness",
         "What does your product do with a visit that has been ordered but is not yet schedulable — "
         "for example because authorization is still pending, consent from a power of attorney is "
         "outstanding, or the clinician it will be assigned to has not yet been determined?"),
        ("C5", "The week",
         "How does your product plan across a week or an episode rather than a single day?", "edit"),
        ("C6", "When the plan breaks",
         "Walk us through what your product does when a clinician calls out, a visit is missed, or a "
         "patient reschedules. Cover how the open need is identified, how coverage is found and "
         "offered, how quickly that happens, and what your product does when nobody takes it.", "new"),
        ("C7", "Automated outreach",
         "Where automated outreach exists in your product, how far does it go? Describe the channels, "
         "whether the conversation is scripted or agentic, what it can resolve on its own, what it "
         "hands to a person, and what controls a customer has over all of it.", "edit"),
        ("C8", "Patient availability",
         "How and when do you capture a patient's availability, and what does your product do when "
         "that availability conflicts with clinical need?", "new"),
    ]),
    ("D", "The clinician's place in the model",
     "Scheduling in home health is operationally critical and personally consequential. Many clinicians "
     "come to home health for the control it gives them over their own day and week, and any change to "
     "how visits get assigned lands on people who feel strongly about it. In our experience adoption, "
     "more than algorithm quality, decides whether tools like this succeed. These questions are about "
     "how your product treats the clinician.", [
        ("D1", "What the clinician decides",
         "Which scheduling decisions does the clinician make in your product, and which are made for "
         "them? Be specific about what they can change, what requires approval, and what they cannot "
         "change at all."),
        ("D2", "Disagreement",
         "When your product proposes an assignment and the clinician disagrees, what happens? Does "
         "anything change as a result — for that clinician, or in the model?"),
        ("D3", "Resistance",
         "Describe a deployment where clinicians resisted your product. What did you learn, and what "
         "did you change — in the product, or in how you rolled it out?"),
        ("D4", "Decide or advise",
         "Some organizations want the system to decide; others want it to advise. Where was your "
         "product designed to sit on that spectrum, and how much of that can a customer change?"),
        ("D5", "Adoption",
         "How do you measure clinician adoption, what do you consider healthy, and what does your data "
         "show across the first six months? Separately — what can a clinician see in your product "
         "about their own results?", "new"),
    ]),
    ("E", "Fit and partnership", None, [
        ("E1", "What we did not ask",
         "What do you do that we have not asked about, and that you believe would matter to an "
         "organization like ours?"),
        ("E2", "Where a design partner helps",
         "We are open to partnering with a product that is strong today and still building. Which "
         "parts of what we have described are you actively building, and where would a committed "
         "design partner be genuinely useful to you?"),
        ("E3", "Sharing in the value",
         "We expect to put real weight behind whichever product we choose — subject-matter guidance "
         "from people who run this work every day, deployment effort across our branches, and a "
         "willingness to act as a reference and co-marketing partner in a market where our competitors "
         "are your prospects. That creates value well beyond our subscription. In what ways would you "
         "be open to sharing in it?", "new"),
        ("E4", "Deployment and change management",
         "Changing how clinician schedules get made is sensitive work. What approaches to deployment "
         "and change management have you used with other customers? How do you support a customer "
         "through it, what have you learned, and what is critical to get right?", "new"),
        ("E5", "What you chose not to build",
         "What have you deliberately chosen not to build, and why?"),
    ]),
]

# ---------------------------------------------------------------- TAB 1 · coverage grid (standard)
# Capacity rows are measurement, not action, so the delivery column is n/a on them.
COVERAGE_STANDARD = [
    ("Capacity Management", [
        ("Workforce supply", "Roster, disciplines, roles, competencies, ramp, float pool"),
        ("Availability & reach", "Availability and time off, territory, drive-time reachability"),
        ("The capacity math", "Visit weighting, targets and ceilings, committed load vs. open room"),
    ]),
    ("Scheduling Engine", [
        ("Demand", "Ingesting ordered visits, authorization, readiness, compliance windows"),
        ("Matching", "Discipline and competency fit, clinician and patient needs, clinical timing, continuity"),
        ("Routing & the week", "Routing, sequencing, front-loading, week balancing"),
        ("Exceptions", "Missed visits, call-outs, reassignment, coverage, rebooking", "edit"),
    ]),
    ("Engagement", [
        ("Before the visit", "Welcome call, availability capture, reminders, confirmation, en-route"),
        ("When plans change", "Reschedule, coverage coordination and clinician outreach, urgent same-day needs"),
        ("Incentives & offers", "Surfacing hard-to-fill visits to clinicians, and any incentive or differential attached", "new"),
        ("Across the care team", "Multi-discipline coordination, clinician and office updates"),
    ]),
]

# ---------------------------------------------------------------- TAB 3 · coverage grid (expanded)
# Rolled up from the workbook's own subcategories — deeper than the standard grid,
# without exposing the full numbered variable inventory.
COVERAGE_EXPANDED = [
    ("Capacity Management", [
        ("Roster", "Headcount by discipline, role (assessing vs. assistant), FTE and employment type"),
        ("Availability", "Approved time off and working availability"),
        ("Territory & geography", "Branch coverage area, clinician territory assignment by zip"),
        ("Reachability", "Distance and drive time from the clinician's home base"),
        ("Visit weighting", "Point value per visit type — the shared currency of capacity"),
        ("Targets & ceilings", "Productivity target and the ceiling it is measured against"),
        ("Committed load", "Points already scheduled, by clinician, day and week"),
        ("Open room", "Remaining capacity by day, week, discipline and territory"),
        ("Start-of-care capacity", "SOC-capable clinicians measured as a distinct number"),
        ("Specialty competency supply", "Wound, IV, catheter and other competencies available"),
        ("Orientation & ramp", "Clinicians not yet at full load, and their trajectory"),
        ("Per-diem & float buffer", "Flex capacity available to the branch"),
        ("On-call & weekend rotation", "Rotation load carried alongside the weekday schedule"),
        ("Demand inflow", "Referral volume in, discharge volume out, against the envelope"),
    ]),
    ("Scheduling Engine", [
        ("Plan-of-care orders", "Ordered frequency and visit types per discipline"),
        ("Compliance windows", "SOC timing, recertification and face-to-face windows, ordered-frequency windows"),
        ("Authorization", "Authorized visit counts, payer rules, pending-auth state"),
        ("Order & consent readiness", "Signed orders, consent, power-of-attorney signature status"),
        ("Discipline & role match", "Right discipline, and assessing vs. assistant"),
        ("Specialty & acuity match", "Competency and skill level against patient acuity"),
        ("Clinician working pattern", "Preferred days, start and end times, documentation blocks, daily volume"),
        ("Clinician restrictions", "Self-imposed restrictions and individual needs"),
        ("Patient availability & preference", "Preferred windows, day-of-week constraints, time-of-day refusals"),
        ("Caregiver constraints", "Caregiver-present requirements and caregiver availability"),
        ("Clinical timing", "Diagnosis-driven cadence, competing appointments, infection-control sequencing"),
        ("Continuity & dependency", "Continuity of care, supervisory visit dependencies"),
        ("Routing", "Home base start and end, route proximity, mileage, intra-day sequencing"),
        ("Week distribution", "Front-loading, pace against the plan of care, day-by-day balancing"),
        ("Missed-visit handling", "Documentation, notification chain, and rescheduling"),
    ]),
    ("Engagement", [
        ("Welcome call", "New-patient introduction and expectation setting"),
        ("Availability capture", "Asking the patient when they can be seen, before booking"),
        ("Reminders & confirmation", "Automated reminders and day-before confirmation"),
        ("En-route notification", "On-my-way messaging to the patient"),
        ("Channel & preference management", "Text, voice, email, language, consent and opt-out"),
        ("Reschedule coordination", "Patient-initiated and clinician-initiated changes"),
        ("Coverage coordination", "Matching potential clinicians to an open need and reaching them"),
        ("Urgent same-day needs", "Call-outs and priority needs surfacing during the day"),
        ("No-show follow-up", "Failed-visit follow-up and rebooking"),
        ("Multi-discipline coordination", "Sequencing visits across disciplines on one case"),
        ("Care-team & office updates", "Keeping clinicians and the office on the same schedule"),
        ("Coordination time load", "How much staff time coordination consumes"),
    ]),
]

# ---------------------------------------------------------------- TAB 4 · additional questions
ADDITIONAL = [
    ("Capacity", [
        "How does availability and time off actually get into the system, who maintains it, and how current is it in practice?",
        "Show us the seven-day capacity view. What decision is it designed to support, and who looks at it?",
        "How is visit weighting calibrated, and what happens when a customer's weighting is wrong?",
        "How does geography affect whether a clinician can serve a patient — territory, drive time, or straight-line distance?",
    ]),
    ("Scheduling", [
        "Describe your routing capability and the data behind it. Live traffic, historical drive time, or distance?",
        "How do you handle constraints that belong to the clinician versus those that belong to the patient or caregiver, and where do those inputs come from?",
        "How does your product distinguish timing that comes from a clinical order or regulation from timing that is a preference?",
        "What exactly happens when a scheduled visit does not happen? Walk the states.",
    ]),
    ("Engagement", [
        "How and when do you capture a patient's availability, and what do you do when it conflicts with clinical need?",
        "What happens when a patient wants to change a visit after it is booked?",
        "How do you handle communication consent, opt-out, language preference, and the regulations on automated outreach?",
    ]),
    ("The clinician", [
        "Walk us through what a clinician sees and does in your product across a typical week. Demo, not prose.",
        "How do you measure clinician adoption, what do you consider healthy, and what does your data show about the first six months?",
        "What does your product do for clinicians, beyond the organization's efficiency goals?",
    ]),
    ("Fit", [
        "Across the three areas, where is your product genuinely strongest, and where is it weakest?",
    ]),
    ("Commercial", [
        "Pricing and commercial model. Held from round one deliberately — asking early anchors the negotiation and invites a sales response rather than a product one.",
        "What does implementation actually require from us — people, time, and from which roles?",
        "What does your support model look like after go-live?",
    ]),
    ("Nashville — deep dive", [
        "The full variable inventory, walked area by area against their product.",
        "The three ceilings on an episode — authorization as permission, LUPA as the floor, utilisation management as the ceiling — and how their product represents each.",
        "The day-before negotiation: hard constraints versus soft preferences, and whether the product can tell them apart.",
        "Recertification and discharge: how the product handles an episode ending in staggered, per-discipline discharges.",
        "Co-development in concrete terms — what a design-partner arrangement looks like, who does what, on what timeline.",
        "Data model and extensibility: can we get our own data out, and can we build on top?",
        "Failure modes: what happens when the system is down on a Monday morning?",
    ]),
]

# ---------------------------------------------------------------- TAB 5 · vetting (for leaders)
VETTING_NOTE = (
    "Set aside from the round-one questionnaire for review with leadership. The working assumption is "
    "that the companies on our list have already been vetted for maturity, security posture and "
    "contracting readiness — so asking these up front spends goodwill on answers we may already have. "
    "They remain here so the decision to include or exclude them is deliberate."
)
VETTING = [
    ("Company maturity",
     "Year founded, current headcount, and where you are in your funding cycle (bootstrapped, seed, "
     "Series A/B/C, PE-backed, profitable), including your most recent raise and date. Not asking for "
     "cap-table detail — we are trying to understand the durability of a multi-year partnership.",
     "Was A4. Likely already known for most of the list."),
    ("Security and compliance",
     "Hosting model, SOC 2 and/or HITRUST status, willingness to sign a BAA, and how PHI is handled.",
     "Was A6. Near-certain to be satisfied by anyone we are talking to; verifiable afterwards."),
    ("Implementation shape",
     "Roughly what does implementation look like for an organization of our size — duration, phases, "
     "and what you need from us?",
     "Was part of A6. More useful on a call, where follow-up is possible."),
    ("Insurance and contracting",
     "Cyber liability and professional liability coverage; standard contracting vehicle; any terms you "
     "will not negotiate.",
     "Not previously asked. Procurement territory — likely belongs after selection, not before."),
    ("Product and engineering scale",
     "Size of the product and engineering team, release cadence, and how customers influence the "
     "roadmap.",
     "Not previously asked. Relevant if we pursue a design-partner arrangement (see E2)."),
]

ONE_PAGER = [
    ("Capacity Management", "The envelope",
     "How much work a branch can deliver, and how much room is left.", "cap", [
        ("Workforce supply", "Who we have, and what each of them is qualified to do.", [
            "Roster by discipline, role (assessing vs. assistant), FTE and employment type",
            "Start-of-care capable clinicians, measured as their own distinct capacity",
            "Specialty competencies, plus orientation and ramp status",
            "Per-diem and float pool",
            "On-call and weekend rotation load"]),
        ("Availability & reach", "When each clinician works, and where they can actually get to.", [
            "Approved time off and working availability",
            "Clinician territory assignment by zip, against branch coverage area",
            "Reachability from the clinician's home base, measured by drive time"]),
        ("The capacity math", "What is committed, what is open, and what is arriving.", [
            "Visit weighting — the point value per visit type, and the productivity target and ceiling it is measured against",
            "Committed load vs. open room, by day, week, discipline and territory",
            "Referral inflow and discharge outflow against the envelope"]),
     ]),
    ("Scheduling Engine", "Filling the envelope",
     "Which clinician, which day, which route.", "sch", [
        ("Demand", "Everything the engine must know about what has been ordered.", [
            "Plan-of-care orders, ordered frequency and visit types, from the EMR (Home Care Home Base) and the intake platform",
            "Authorization status and payer rules attached to each visit",
            "Order, consent and readiness state — what is schedulable, not merely ordered",
            "The compliance window each visit has to fall inside"]),
        ("Matching", "Putting the right clinician with the right patient.", [
            "Discipline and role match, specialty competency, acuity to skill level",
            "Clinician working pattern, needs and restrictions",
            "Patient and caregiver needs, restrictions and availability, sourced from the patient",
            "Clinical timing — diagnosis-driven cadence, competing appointments, infection-control sequencing",
            "Continuity of care, and supervisory visit dependencies"]),
        ("Routing & the week", "A day that works, inside a week that holds.", [
            "Home base start and end, route proximity, mileage",
            "Appointment time windows and intra-day sequencing",
            "Front-loading, pace against the plan of care, day-by-day balancing"]),
        ("Exceptions", "What happens when the plan breaks.", [
            "Missed-visit management and tracking — and reducing the occurrence",
            "Reassignment, coverage, and rebooking inside the window"]),
     ]),
    ("Engagement", "Making it happen",
     "Turning a schedule into delivered visits — with patients, clinicians and the office.", "eng", [
        ("How this should run", "Our expectation of the platform, not of our staff.", [
            ("Outreach carried by the platform itself — agentic voice, text and email — rather than queued up for a coordinator to work", "new"),
            ("Staff able to see it, intervene, override, and take any conversation back", "new")]),
        ("Before the visit", "Securing the visit before the clinician drives.", [
            "New-patient welcome call",
            "Patient availability captured before the visit is booked",
            "Automated reminders and en-route notification",
            ("The day-before confirmation round automated for every patient, every day", "edit"),
            ("The schedule staying pliable until that confirmation, so clinician and capacity changes can land before the patient is told", "new"),
            "Channel and communication-preference management"]),
        ("When plans change", "Recovering a visit rather than losing it — with the patient and the clinician.", [
            "Reschedule coordination with the patient",
            "Coverage coordination — matching potential clinicians to an open need, and reaching them directly",
            "Call-out coverage, and the urgent or prioritized needs that surface during the day",
            ("Incentives or differentials attached to hard-to-fill visits, and offered to the clinicians who can take them", "new"),
            "Failed-visit and no-show follow-up and rebooking"]),
        ("Across the care team", "Keeping clinicians and the office on the same schedule.", [
            "Multi-discipline visit coordination",
            "Care-team and office coordination updates",
            ("A clinician view of their own schedule and their own results — the case for the change, made to the person it lands on", "new"),
            "The staff time coordination consumes today"]),
     ]),
]
