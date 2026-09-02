# -*- coding: utf-8 -*-
"""Content for the review draft. Single source for both the HTML and the Word build."""

FRAMING = [
    "We are paid in two fundamentally different ways depending on the insurer, and the two respond in opposite directions to the same operational change. Traditional Medicare pays a fixed amount for a period of care regardless of how many visits we deliver above a minimum. Every other insurer pays for each visit delivered, but only with permission granted in advance.",
    "Most of our clinicians are paid for each visit they complete rather than by salary. This means efficiency gains do not automatically become savings. They become available capacity, and capacity only becomes money if we fill it.",
    "Clinician capacity is perishable. An open slot on tomorrow's schedule is like an empty seat on tomorrow's flight. If it is not filled, it is gone, and it does not carry forward.",
    "Several of the ways we currently lose money are deadline-driven and invisible until the deadline has already passed. By the time we can see them, nothing can be done.",
    "A branch is either capacity-constrained or demand-constrained, and the correct strategy is opposite in each case. Several levers below only create value in the first state, and would do harm in the second. The system has to know which state a branch is in.",
]

LEVERS = [
    {
        "id": "L1",
        "name": "Admission Throughput",
        "def": "Starting more patients on service using the clinicians we already employ, by shortening the time it takes to confirm that an admission will actually happen.",
        "points": [
            ("connect", "The connection: earlier certainty about which admissions are real means capacity is redirected while the day can still be used, rather than discovered empty the following morning."),
            ("", "A clinician's open slot for tomorrow does not carry over to the next day. If it is not filled, that capacity is permanently lost."),
            ("", "Standardized welcome calls, made as early in the day as possible rather than waiting for office staff to work through a queue, are the single largest source of early warning we have."),
            ("", "Two things routinely change between a referral being accepted and care beginning. Anticipated hospital discharges are delayed, and patients who agreed to a next-day visit when sales confirmed frequently defer once the branch calls."),
            ("", "Both are discovered at the welcome call. The earlier that call happens, the more of the day remains to redirect that capacity to another admission rather than losing it."),
            ("", "This pattern is most pronounced at weekends. Sunday in particular carries a high rate of patients canceling or refusing the start-of-care visit and deferring to Monday."),
            ("", "Weekend admission performance has a disproportionate effect on the following week. A productive Saturday and Sunday materially changes Monday's available capacity and can determine whether a branch meets its admission goal for that week."),
            ("", "Our referral system is improving how many referrals we accept. This lever addresses what happens after acceptance and before care begins."),
        ],
    },
    {
        "id": "L2",
        "name": "Assessment Capacity Release",
        "def": "Freeing clinicians qualified to perform admissions, therapy evaluations, and other assessment visits from routine visit work, by shifting those routine visits to paraprofessional staff who have availability.",
        "points": [
            ("connect", "The connection: assessment-capable clinicians are the true constraint on admissions. Moving routine work off their schedules converts existing staff time into admission capacity without hiring."),
            ("", "Only licensed assessing clinicians can perform admissions, resumptions of care, recertifications, discharges, and therapy evaluations. A large share of routine visits can be performed by a paraprofessional."),
            ("", "When assessing clinicians spend their week on routine visits, the branch forfeits admission capacity it already has and is paying for."),
            ("condition", "Important condition: this only creates value when a branch is at capacity and at risk of declining referrals. If referrals are limited and clinicians are short of visits, shifting work away from them reduces their income and damages retention. That situation calls for a different strategy entirely."),
            ("", "The system therefore has to know which state each branch is in before recommending any shift. Getting this wrong in a demand-constrained branch would be actively harmful."),
            ("", "It also requires knowing paraprofessional availability accurately, which today is not visible in one place."),
        ],
    },
    {
        "id": "L3",
        "name": "Same-Day Schedule Recovery",
        "def": "Refilling a clinician's open time with comparable work when a patient cancels late, rather than losing that portion of the day.",
        "points": [
            ("connect", "The connection: an infrastructure that can identify and offer a suitable replacement visit quickly turns a lost afternoon into a delivered, billable visit."),
            ("", "When a patient cancels, rescheduling that patient is normally handled during the cancellation call. That is not the issue."),
            ("", "The issue is the gap left in the clinician's day. Filling it requires knowing immediately which other patients are due, which are geographically close, which have insurer approval in place, and which visits are flexible enough to move."),
            ("", "Occasionally the right answer is bringing a visit forward from later in the week, which exchanges a gap we cannot fill today for one we have several days to fill."),
            ("", "Because most clinicians are paid per visit, an unfilled gap is lost income for them rather than lost revenue for us. This connects directly to the retention lever below."),
            ("", "This becomes more difficult as scheduling becomes more efficient. A tightly planned week has less slack to absorb a cancellation, so this capability must accompany the optimization rather than follow it."),
        ],
    },
    {
        "id": "L4",
        "name": "Episode Payment Protection",
        "def": "Preventing periods of care from closing below the minimum visit count Medicare requires for full payment, known as a LUPA.",
        "points": [
            ("connect", "The connection: visibility into a period's visit count while days remain converts an after-the-fact write-down into a correctable operational issue."),
            ("", "Medicare pays a fixed amount for a period of care, but only if a minimum number of visits occurs. Fall below it and the period is repriced to a much lower per-visit amount. This is the Low Utilization Payment Adjustment, or LUPA."),
            ("", "Most shortfalls are by a single visit, and typically because a visit was missed or moved rather than because fewer visits were clinically necessary."),
            ("", "We currently discover this after the period has closed, when no remedy exists."),
            ("", "This is a tracking and visibility problem rather than a clinical one."),
            ("", "An important boundary: we would never add a visit a patient does not require in order to avoid a LUPA. Federal auditors specifically examine that pattern, and the only appropriate recoveries are visits that were clinically indicated and lost operationally."),
        ],
    },
    {
        "id": "L5",
        "name": "Reassessment Window Compliance",
        "def": "Ensuring therapy reassessment visits occur inside their required windows, so that visits already delivered remain billable.",
        "points": [
            ("connect", "The connection: holding every episode deadline in one place, surfaced with lead time, prevents care we have already paid to deliver from becoming unbillable."),
            ("", "Therapy requires reassessment visits at defined points in an episode. If the reassessment does not occur within its window, visits already delivered cannot be billed."),
            ("", "This is the most damaging category of loss on this list. The work was performed, the clinician was paid for it, and the revenue is forfeited."),
            ("", "It is currently tracked manually by schedulers, competing for attention with a high volume of other daily tasks."),
            ("", "Structurally it is the same problem as the LUPA threshold: a deadline attached to an episode that no one can see approaching, discovered only after it has passed. One mechanism addresses both."),
            ("", "A useful question for the discussion: do we currently report how often this occurs, or what it costs us annually?"),
        ],
    },
    {
        "id": "L6",
        "name": "Scheduling Administration Cost",
        "def": "The number of staff required to assign visits, once the repetitive portion of that work no longer requires human handling.",
        "points": [
            ("connect", "The connection: removing task volume that exists only because the system generates it reduces the headcount required to process it."),
            ("", "Schedulers currently spend the majority of their time processing a task queue rather than making scheduling decisions."),
            ("", "A single patient generates a separate task for each clinical discipline involved, and again at approval."),
            ("", "The function should not be eliminated entirely. Urgency, local knowledge, and coverage relationships still require judgment."),
        ],
    },
    {
        "id": "L7",
        "name": "Premium Labor Avoidance",
        "def": "Reduced spend on contract clinicians, per diem staff, and incentive payments made to employed clinicians for absorbing additional visits at short notice.",
        "points": [
            ("connect", "The connection: visibility into who has available capacity converts a reactive premium purchase into a planned assignment using staff already on the payroll."),
            ("", "Premium labor here means any spend above our standard visit rate to get a visit covered: contract clinicians, per diem staff, and non-visit activity payments used to incentivize employed clinicians to take on extra work."),
            ("", "When a clinician calls out early in the morning, no one can see who has room, so the branch either buys the most expensive coverage available or loses the visit."),
            ("", "One caveat worth stating plainly. Because most clinicians are paid per visit, the saving is the differential between our standard visit rate and the contract or incentive rate, not the full amount paid. In an organization with salaried clinicians this lever would be considerably larger."),
        ],
    },
    {
        "id": "L8",
        "name": "Clinician Retention",
        "def": "Reduced voluntary turnover, and the replacement cost that accompanies it, through a more predictable schedule, a more predictable income, and earlier visibility of clinicians who are struggling.",
        "points": [
            ("connect", "The connection: a stable weekly schedule produces a stable paycheck, and leadership visibility of productivity identifies a struggling clinician early enough to intervene rather than replace."),
            ("", "Because most of our clinicians are paid per visit, schedule volatility is income volatility."),
            ("", "Published research on home health nurses found that those with the most erratic week-to-week visit counts were significantly more likely to resign, and that stabilizing the schedule measurably reduced that risk."),
            ("", "The effect appeared only among full-time staff, which is consistent with the mechanism being income dependence rather than preference."),
            ("", "Risk is not confined to the first ninety days. It recurs at the six month and one year marks, and each has a different character. A clinician who has survived ramp-up may still leave when the income never quite reaches what was represented."),
            ("", "Leadership visibility of productivity does two things at once. It supports accountability, and it surfaces the early signs of a clinician who is struggling. The second is the one that keeps people."),
            ("", "Built correctly, this data supports and engages clinicians rather than only monitoring them. That distinction determines whether the tool is accepted or resisted."),
            ("", "Automated next-day visit confirmation removes a taxing task performed unpaid, in the evening, that has nothing to do with patient care."),
            ("", "It also removes a task many clinicians find genuinely difficult. Confirming visits well requires negotiation, and not every excellent clinician has the interpersonal strategies to secure the appointment times that make their day work."),
            ("", "A system that can negotiate a reluctant patient into a nine o'clock appointment anchors that clinician's entire day. The value of that, in both work-life balance and clinical efficiency, is difficult to overstate."),
            ("", "This is the same mechanism as L3, viewed from the clinician's side. Every unfilled opening is income a clinician expected and did not receive."),
        ],
    },
    {
        "id": "L9",
        "name": "Travel and Territory Efficiency",
        "def": "Fewer miles driven per visit, through better daily sequencing and territories defined by actual drive times rather than map boundaries.",
        "points": [
            ("connect", "The connection: territories and daily routes built on real travel times reduce reimbursable mileage and return productive time to clinicians."),
            ("", "Territories are currently drawn manually and revised infrequently. A day's visits are grouped by distance rather than by actual travel time."),
            ("", "One caveat that matters for the arithmetic. Because most clinicians are paid per visit, time saved in the car belongs to the clinician, not to the company. What we recover directly is reimbursed mileage."),
            ("", "The time returned to clinicians becomes available capacity, which is captured in L1 and L2. Counting it in both places would overstate the case."),
        ],
    },
]

FUTURE = [
    {
        "id": "U1",
        "name": "Clinician Recruitment Advantage",
        "def": "A hiring proposition improved by removing unpaid administrative burden and by making quoted earnings achievable in practice.",
        "points": [
            "The evening confirmation burden is removed, which is a tangible difference a candidate understands immediately.",
            "A candidate quoted an expected income is considerably more likely to achieve it when their schedule is protected and cancellations are replaced.",
            "Left unquantified because we do not currently track time to fill a vacancy, offer acceptance rates, or cost per hire.",
        ],
    },
    {
        "id": "U2",
        "name": "Hospice Line Extension",
        "def": "Applying the same capacity and scheduling capability to the hospice business.",
        "points": [
            "Our prior working session concluded that hospice requires additional rules rather than a separate system.",
            "This would extend the return at limited incremental cost, and is deliberately excluded until home health demonstrates the result.",
        ],
    },
    {
        "id": "U3",
        "name": "Authorization Timing Write-Offs",
        "def": "Care delivered outside the window an insurer permits for retroactive approval, which cannot be billed.",
        "points": [
            "Insurers allow only a short period in which an approval can be backdated. Care delivered outside that window is written off.",
            "This is not currently measured anywhere. It could prove immaterial, or it could be the largest item on this list.",
            "It is the first item worth measuring, precisely because we do not know which it is.",
        ],
    },
]

DATA = [
    {
        "id": "D1", "name": "Admission Throughput",
        "baseline": [
            "New patient starts per year, by branch and by month.",
            "Time stamps at each step between accepting a referral and delivering the first visit: referral accepted, insurance verified, intake approved, welcome call completed, visit scheduled, visit delivered.",
            "Time of day the welcome call is completed, and how long after intake approval it occurs.",
            "How often an accepted referral does not convert to an admission on the expected day, split by cause: hospital discharge delayed, patient or caregiver deferred, and all other reasons.",
            "Admission activity by day of week, including Saturday and Sunday, for at least twelve months. Weekend performance is a baseline requirement for this initiative rather than a detail.",
            "Start-of-care visits refused or deferred by day of week, with Sunday reported separately.",
            "The relationship between weekend admission performance and the following week's capacity and admission attainment.",
            "Referrals declined, with reason, separating capacity-driven declines from all others.",
        ],
        "ongoing": [
            "Median and worst-case time from referral acceptance to first visit, weekly.",
            "Welcome calls completed before a defined hour of the day, as a proportion of the total.",
            "Same-day deferral and refusal rate, by day of week.",
            "Weekend admission attainment, and its effect on the following week.",
            "Referrals declined for capacity, weekly, by branch.",
        ],
    },
    {
        "id": "D2", "name": "Assessment Capacity Release",
        "baseline": [
            "Visits by discipline and by visit type, separating assessment visits from routine visits.",
            "Which clinicians are credentialed and available to perform assessment visits, by branch.",
            "The proportion of assessing clinicians' weekly schedules occupied by routine visits that a paraprofessional could have performed.",
            "Paraprofessional availability against routine visit demand, by branch and by week.",
            "Whether each branch is capacity-constrained or demand-constrained, week by week, over at least twelve months. This determines whether the lever applies at all.",
            "Branch-level referral volume against admission capacity, to establish how often each state occurs.",
        ],
        "ongoing": [
            "Share of assessment-capable clinician time spent on routine visits, weekly.",
            "Paraprofessional utilization against available capacity.",
            "Branch state indicator, capacity-constrained or demand-constrained, weekly.",
            "Admissions accepted that would previously have been declined.",
        ],
    },
    {
        "id": "D3", "name": "Same-Day Schedule Recovery",
        "baseline": [
            "Canceled and missed visits: volume, and how far in advance of the visit the cancellation occurred.",
            "Cancellation reason, separating patient-initiated from clinician-initiated.",
            "Of those cancellations, how many left a gap in the clinician's day that was never filled. This is the actual loss, and it is not captured in any current report.",
            "Where a gap was filled, elapsed time from cancellation to replacement assignment.",
            "How often a visit is brought forward from later in the week to cover a gap, and whether the resulting later gap was then filled.",
            "Which visit types are genuinely flexible on timing, defined by clinical leadership rather than inferred from the system.",
        ],
        "ongoing": [
            "Cancellations per week, and the proportion leaving an unfilled gap.",
            "Average elapsed time from cancellation to replacement assignment.",
            "Clinician capacity lost to cancellation, per branch, per week.",
            "Visits moved forward to cover a gap, and how often this created a second unfilled gap.",
        ],
    },
    {
        "id": "D4", "name": "Episode Payment Protection",
        "baseline": [
            "Frequency of periods closing below the LUPA threshold, by branch.",
            "For those that fell short, the size of the shortfall in visits.",
            "For shortfalls of a single visit, whether the visit was missed, moved, or held pending insurer approval.",
            "Cost to deliver a period of care, so the loss can be stated as margin rather than revenue.",
        ],
        "ongoing": [
            "Open periods currently tracking below the threshold, with days remaining.",
            "Periods closing short in the prior month, with cause coded.",
            "Proportion of shortfalls that were preventable, meaning a clinically indicated visit was lost rather than not required.",
        ],
    },
    {
        "id": "D5", "name": "Reassessment Window Compliance",
        "baseline": [
            "Therapy reassessments completed outside the required window, by branch and by discipline.",
            "Value of visits written off as a result.",
            "How far past the window the late reassessments typically fell, since one day late and three weeks late are materially different problems.",
            "Whether the miss originated in scheduling, clinician availability, or documentation.",
            "How reassessment deadlines are tracked today, and by whom.",
        ],
        "ongoing": [
            "Reassessments due within the next two weeks, with status.",
            "Proportion completed inside the window, monthly.",
            "Write-off value attributable to missed reassessment windows, monthly.",
        ],
    },
    {
        "id": "D6", "name": "Scheduling Administration Cost",
        "baseline": [
            "Ninety days of scheduler task records with start and completion times, grouped by task type.",
            "Current scheduling headcount by branch, with fully loaded cost per role.",
            "Distribution of task volume across those staff, since averages conceal where the load actually sits.",
            "Which task types are non-actionable, meaning they are opened and closed with no action taken.",
        ],
        "ongoing": [
            "Tasks per scheduler per day, and time per task type.",
            "Proportion of tasks closed with no action taken.",
            "Scheduling headcount relative to branch volume.",
        ],
    },
    {
        "id": "D7", "name": "Premium Labor Avoidance",
        "baseline": [
            "Contract clinician, per diem, and non-visit activity incentive spend for the trailing twelve months, by branch and discipline.",
            "The proportion of that spend committed with less than twenty-four hours notice, which is the reactive portion this lever addresses.",
            "Rate differential between our standard visit rate and the contract or incentive rate for an equivalent visit.",
            "Frequency of visits going uncovered entirely rather than being covered at premium rates.",
        ],
        "ongoing": [
            "Premium spend per branch, monthly, split between planned and reactive.",
            "Visits covered at premium rates, weekly.",
            "Visits uncovered, weekly.",
        ],
    },
    {
        "id": "D8", "name": "Clinician Retention",
        "baseline": [
            "Departures over the trailing twenty-four months, with date and length of service.",
            "Departures grouped by tenure band: under ninety days, ninety days to six months, six months to one year, and beyond one year.",
            "Replacement cost per clinician, by discipline.",
            "Weekly visit counts per clinician for the trailing twelve months, which allows schedule stability to be calculated per individual.",
            "Income quoted at hire against income actually earned at ninety days, at six months, and at one year.",
            "Time clinicians spend on next-day visit confirmation, and when in the day or evening it occurs.",
            "Visit start times by clinician, to establish how often a day is anchored with an early first visit.",
            "Stated reasons for leaving, coded consistently rather than captured in free text.",
        ],
        "ongoing": [
            "Turnover rate monthly, by discipline and by tenure band.",
            "Week-to-week variability in visit counts per clinician, as an early indicator of resignation risk.",
            "Clinicians whose earnings are tracking below the income quoted at hire, at each of the three tenure marks.",
            "Productivity trend per clinician, surfaced to leadership as a support signal rather than only as an accountability measure.",
        ],
    },
    {
        "id": "D9", "name": "Travel and Territory Efficiency",
        "baseline": [
            "Miles and drive time per visit, by branch and discipline.",
            "Total mileage reimbursement paid over the trailing twelve months.",
            "How territories are currently defined, and when each was last reviewed.",
            "Visits delivered outside the assigned clinician's normal territory.",
        ],
        "ongoing": [
            "Miles per visit, monthly, by branch.",
            "Mileage reimbursement relative to visit volume.",
            "Proportion of visits falling outside the assigned territory.",
        ],
    },
]

FUTURE_DATA = [
    {
        "id": "D10", "name": "Clinician Recruitment Advantage",
        "baseline": [
            "Time to fill a vacancy, by discipline and branch.",
            "Offer acceptance rate, with stated reasons where offers are declined.",
            "Recruiting cost per hire.",
        ],
        "ongoing": [
            "Time to fill, monthly.",
            "Offer acceptance rate, monthly.",
        ],
    },
    {
        "id": "D11", "name": "Authorization Timing Write-Offs",
        "baseline": [
            "Visits delivered that could not be billed because approval arrived outside the permitted window.",
            "Elapsed days from our approval request to the insurer's response, by insurer.",
            "Visits held unscheduled pending approval, at a point in time.",
        ],
        "ongoing": [
            "Write-offs attributable to late approval, monthly.",
            "Approval turnaround by insurer, monthly.",
            "Visits held pending approval, weekly.",
        ],
    },
]

CLOSING = [
    "Every figure in a business case is one of three things: measured, published, or assumed. At present too many of ours are assumed.",
    "This list is what converts the assumed figures into measured ones.",
    "The majority already exists within systems we own and can be produced as extracts. A smaller number, particularly around canceled visits, reassessment windows, and weekend admission patterns, is not captured anywhere today and would require new instrumentation.",
    "Those gaps are notable in themselves. They are the areas where we currently cannot see the loss we are attempting to address.",
]
