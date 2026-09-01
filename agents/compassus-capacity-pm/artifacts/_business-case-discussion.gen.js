const fs = require("fs");
const {
  Document, Packer, Paragraph, TextRun, HeadingLevel, AlignmentType,
  LevelFormat, BorderStyle,
} = require("docx");

const FONT = "Arial";

const TITLE = (t, sub) => ([
  new Paragraph({
    spacing: { after: 60 },
    children: [new TextRun({ text: t, font: FONT, size: 40, bold: true, color: "1F3864" })],
  }),
  new Paragraph({
    spacing: { after: 300 },
    children: [new TextRun({ text: sub, font: FONT, size: 24, color: "595959" })],
  }),
]);

const H1 = (t) => new Paragraph({
  heading: HeadingLevel.HEADING_1,
  spacing: { before: 360, after: 180 },
  children: [new TextRun({ text: t, font: FONT, size: 30, bold: true, color: "1F3864" })],
});

const LEVER = (num, t) => new Paragraph({
  heading: HeadingLevel.HEADING_2,
  spacing: { before: 340, after: 60 },
  children: [
    new TextRun({ text: `${num}.  `, font: FONT, size: 24, bold: true, color: "8C8C8C" }),
    new TextRun({ text: t, font: FONT, size: 24, bold: true, color: "1F3864" }),
  ],
});

const SUB = (t) => new Paragraph({
  heading: HeadingLevel.HEADING_3,
  spacing: { before: 240, after: 60 },
  children: [new TextRun({ text: t, font: FONT, size: 21, bold: true, color: "1F3864" })],
});

const DEF = (t) => new Paragraph({
  spacing: { after: 140 },
  indent: { left: 200 },
  children: [new TextRun({ text: t, font: FONT, size: 21, italics: true, color: "404040" })],
});

const MINI = (t) => new Paragraph({
  spacing: { before: 140, after: 60 },
  children: [new TextRun({ text: t, font: FONT, size: 20, bold: true, color: "404040" })],
});

const P = (t, opts = {}) => new Paragraph({
  spacing: { after: 140 },
  children: [new TextRun({ text: t, font: FONT, size: 21, italics: !!opts.i })],
});

const B = (t) => new Paragraph({
  numbering: { reference: "dot", level: 0 },
  spacing: { after: 80 },
  children: [new TextRun({ text: t, font: FONT, size: 21 })],
});

const RULE = () => new Paragraph({
  spacing: { before: 160, after: 220 },
  border: { bottom: { style: BorderStyle.SINGLE, size: 6, color: "BFBFBF" } },
  children: [new TextRun({ text: "", font: FONT, size: 2 })],
});

// ─────────────────────────────────────────────────────── framing
const framing = [
  "We are paid in two fundamentally different ways depending on the insurer, and the two respond in opposite directions to the same operational change. Traditional Medicare pays a fixed amount for a period of care regardless of how many visits we deliver above a minimum. Every other insurer pays for each visit delivered, but only with permission granted in advance.",
  "Most of our clinicians are paid for each visit they complete rather than by salary. This means efficiency gains do not automatically become savings. They become available capacity, and capacity only becomes money if we fill it.",
  "Clinician capacity is perishable. An open slot on tomorrow's schedule is like an empty seat on tomorrow's flight. If it is not filled, it is gone, and it does not carry forward.",
  "Several of the ways we currently lose money are deadline-driven and invisible until the deadline has already passed. By the time we can see them, nothing can be done.",
  "These four facts are why scheduling is a financial system and not an administrative one, and they explain why the levers below behave differently from one another.",
];

// ─────────────────────────────────────────────────────── levers
const levers = [
  {
    name: "Admission Throughput",
    def: "Starting more patients on service using the clinicians we already employ, by shortening the time it takes to answer whether we can accept a referral.",
    points: [
      "The connection: faster capacity decisions mean fewer clinician openings expire unused, which means more admissions from the same workforce.",
      "A clinician's open slot for tomorrow does not carry over to the next day. If it is not filled, that capacity is permanently lost.",
      "Today the answer to whether we can take a patient moves slowly through several handoffs, so openings expire while we are still working out whether we can use them.",
      "Our referral system is improving how many referrals we accept. This lever addresses what happens after acceptance and before care begins.",
      "This depends on referral demand being available. It is, because we currently decline referrals we cannot staff.",
    ],
  },
  {
    name: "Same-Day Schedule Recovery",
    def: "Refilling a clinician's open time with comparable work when a patient cancels late, rather than losing that portion of the day.",
    points: [
      "The connection: an infrastructure that can identify and offer a suitable replacement visit quickly turns a lost afternoon into a delivered, billable visit.",
      "When a patient cancels, rescheduling that patient is normally handled during the cancellation call. That is not the issue.",
      "The issue is the gap left in the clinician's day. Filling it requires knowing immediately which other patients are due, which are geographically close, which have insurer approval in place, and which visits are flexible enough to move.",
      "Occasionally the right answer is bringing a visit forward from later in the week, which exchanges a gap we cannot fill today for one we have several days to fill.",
      "Because most clinicians are paid per visit, an unfilled gap is lost income for them rather than lost revenue for us. This connects directly to the retention lever below.",
      "This becomes more difficult as scheduling becomes more efficient. A tightly planned week has less slack to absorb a cancellation, so this capability must accompany the optimization rather than follow it.",
    ],
  },
  {
    name: "Episode Payment Protection",
    def: "Preventing periods of care from closing below the minimum visit count Medicare requires for full payment.",
    points: [
      "The connection: visibility into a period's visit count while days remain converts an after-the-fact write-down into a correctable operational issue.",
      "Medicare pays a fixed amount for a period of care, but only if a minimum number of visits occurs. Fall below it and the payment for the entire period drops substantially.",
      "Most shortfalls are by a single visit, and typically because a visit was missed or moved rather than because fewer visits were clinically necessary.",
      "We currently discover this after the period has closed, when no remedy exists.",
      "This is a tracking and visibility problem rather than a clinical one.",
      "An important boundary: we would never add a visit a patient does not require in order to reach a threshold. Federal auditors specifically examine that pattern, and the only appropriate recoveries are visits that were clinically indicated and lost operationally.",
    ],
  },
  {
    name: "Reassessment Window Compliance",
    def: "Ensuring therapy reassessment visits occur inside their required windows, so that visits already delivered remain billable.",
    points: [
      "The connection: holding every episode deadline in one place, surfaced with lead time, prevents care we have already paid to deliver from becoming unbillable.",
      "Therapy requires reassessment visits at defined points in an episode. If the reassessment does not occur within its window, visits already delivered cannot be billed.",
      "This is the most damaging category of loss on this list. The work was performed, the clinician was paid for it, and the revenue is forfeited.",
      "It is currently tracked manually by schedulers, competing for attention with a high volume of other daily tasks.",
      "Structurally it is the same problem as the previous lever: a deadline attached to an episode that no one can see approaching, discovered only after it has passed. One mechanism addresses both.",
      "A useful question for the discussion: do we currently report how often this occurs, or what it costs us annually?",
    ],
  },
  {
    name: "Scheduling Administration Cost",
    def: "The number of staff required to assign visits, once the repetitive portion of that work no longer requires human handling.",
    points: [
      "The connection: removing task volume that exists only because the system generates it reduces the headcount required to process it.",
      "Schedulers currently spend the majority of their time processing a task queue rather than making scheduling decisions.",
      "A single patient generates a separate task for each clinical discipline involved, and again at approval.",
      "Two points of caution for credibility. Some of this work should not exist at all, which means the software cannot claim credit for eliminating all of it. And published results from comparable deployments have produced materially fewer role reductions than the figure discussed in our on-site session.",
      "The function should not be eliminated entirely. Urgency, local knowledge, and coverage relationships still require judgment.",
    ],
  },
  {
    name: "Premium Labor Avoidance",
    def: "Reduced spend on agency staff, overtime, and incentive pay purchased reactively to cover visits at short notice.",
    points: [
      "The connection: visibility into who has available capacity converts an emergency purchase into a planned assignment using staff already on the payroll.",
      "Premium labor is any spend above our standard rate to cover a visit: agency and contract clinicians, per diem staff at premium rates, overtime, and incentive payments for accepting additional work.",
      "When a clinician calls out early in the morning, no one can see who has room, so the branch either buys the most expensive coverage available or loses the visit.",
      "One caveat worth stating plainly. Because most clinicians are paid per visit, the saving is the rate differential between our own staff and agency staff, not the full agency invoice. In an organization with salaried clinicians this lever would be considerably larger.",
    ],
  },
  {
    name: "Clinician Retention",
    def: "Reduced voluntary turnover, and the replacement cost that accompanies it, through a more predictable schedule and therefore a more predictable income.",
    points: [
      "The connection: a stable weekly schedule produces a stable paycheck, and income stability is a documented driver of whether clinicians stay.",
      "Because most of our clinicians are paid per visit, schedule volatility is income volatility.",
      "Published research on home health nurses found that those with the most erratic week-to-week visit counts were significantly more likely to resign, and that stabilizing the schedule measurably reduced that risk.",
      "The effect appeared only among full-time staff, which is consistent with the mechanism being income dependence rather than preference.",
      "The exposure is greatest in the first year of employment, when a clinician is still building speed, does not yet know the territory, and is evaluating whether the role pays what was represented at hire.",
      "This is the same mechanism as the recovery lever above, viewed from the clinician's side. Every unfilled opening is income a clinician expected and did not receive.",
    ],
  },
  {
    name: "Travel and Territory Efficiency",
    def: "Fewer miles driven per visit, through better daily sequencing and territories defined by actual drive times rather than map boundaries.",
    points: [
      "The connection: territories and daily routes built on real travel times reduce reimbursable mileage and return productive time to clinicians.",
      "Territories are currently drawn manually and revised infrequently. A day's visits are grouped by distance rather than by actual travel time.",
      "One caveat that matters for the arithmetic. Because most clinicians are paid per visit, time saved in the car belongs to the clinician, not to the company. What we recover directly is reimbursed mileage.",
      "The time returned to clinicians becomes available capacity, which is captured in the admission throughput lever. Counting it in both places would overstate the case.",
    ],
  },
];

const future = [
  {
    name: "Clinician Recruitment Advantage",
    def: "A hiring proposition improved by removing unpaid administrative burden and by making quoted earnings achievable in practice.",
    points: [
      "Clinicians currently spend part of every evening, unpaid, contacting the following day's patients to confirm visits. That obligation is removed.",
      "A candidate quoted an expected income is considerably more likely to achieve it when their schedule is protected and cancellations are replaced.",
      "Left unquantified because we do not currently track time to fill a vacancy, offer acceptance rates, or cost per hire.",
    ],
  },
  {
    name: "Hospice Line Extension",
    def: "Applying the same capacity and scheduling capability to the hospice business.",
    points: [
      "Our prior working session concluded that hospice requires additional rules rather than a separate system.",
      "This would extend the return at limited incremental cost, and is deliberately excluded until home health demonstrates the result.",
    ],
  },
  {
    name: "Authorization Timing Write-Offs",
    def: "Care delivered outside the window an insurer permits for retroactive approval, which cannot be billed.",
    points: [
      "Insurers allow only a short period in which an approval can be backdated. Care delivered outside that window is written off.",
      "This is not currently measured anywhere. It could prove immaterial, or it could be the largest item on this list.",
      "It is the first item worth measuring, precisely because we do not know which it is.",
    ],
  },
];

// ─────────────────────────────────────────────────────── data asks
const data = [
  {
    name: "Admission Throughput",
    baseline: [
      "New patient starts per year, by branch and by month.",
      "Time stamps at each step between accepting a referral and delivering the first visit: referral accepted, insurance verified, intake approved, patient contacted, visit scheduled, visit delivered.",
      "Referrals declined, with reason, separating capacity-driven declines from all others.",
      "Admitting visits offered to clinicians against those actually filled.",
      "Which clinicians are qualified and available to admit new patients, as distinct from those who only perform routine visits.",
    ],
    ongoing: [
      "Median and worst-case time from referral acceptance to first visit, weekly.",
      "Referrals declined for capacity, weekly, by branch.",
      "Admitting capacity available against filled, weekly.",
      "Admissions per branch against the prior period.",
    ],
  },
  {
    name: "Same-Day Schedule Recovery",
    baseline: [
      "Canceled and missed visits: volume, and how far in advance of the visit the cancellation occurred.",
      "Cancellation reason, separating patient-initiated from clinician-initiated.",
      "Of those cancellations, how many left a gap in the clinician's day that was never filled. This is the actual loss, and it is not captured in any current report.",
      "Where a gap was filled, elapsed time from cancellation to replacement assignment.",
      "How often a visit is brought forward from later in the week to cover a gap, and whether the resulting later gap was then filled.",
      "Which visit types are genuinely flexible on timing, defined by clinical leadership rather than inferred from the system.",
    ],
    ongoing: [
      "Cancellations per week, and the proportion leaving an unfilled gap.",
      "Average elapsed time from cancellation to replacement assignment.",
      "Clinician capacity lost to cancellation, per branch, per week.",
      "Visits moved forward to cover a gap, and how often this created a second unfilled gap.",
    ],
  },
  {
    name: "Episode Payment Protection",
    baseline: [
      "Frequency of periods closing below the required visit count, by branch.",
      "For those that fell short, the size of the shortfall in visits.",
      "For shortfalls of a single visit, whether the visit was missed, moved, or held pending insurer approval.",
      "Cost to deliver a period of care, so the loss can be stated as margin rather than revenue.",
    ],
    ongoing: [
      "Open periods currently tracking below the threshold, with days remaining.",
      "Periods closing short in the prior month, with cause coded.",
      "Proportion of shortfalls that were preventable, meaning a clinically indicated visit was lost rather than not required.",
    ],
  },
  {
    name: "Reassessment Window Compliance",
    baseline: [
      "Therapy reassessments completed outside the required window, by branch and by discipline.",
      "Value of visits written off as a result.",
      "How far past the window the late reassessments typically fell, since one day late and three weeks late are materially different problems.",
      "Whether the miss originated in scheduling, clinician availability, or documentation.",
      "How reassessment deadlines are tracked today, and by whom.",
    ],
    ongoing: [
      "Reassessments due within the next two weeks, with status.",
      "Proportion completed inside the window, monthly.",
      "Write-off value attributable to missed reassessment windows, monthly.",
    ],
  },
  {
    name: "Scheduling Administration Cost",
    baseline: [
      "Ninety days of scheduler task records with start and completion times, grouped by task type.",
      "Current scheduling headcount by branch, with fully loaded cost per role.",
      "Distribution of task volume across those staff, since averages conceal where the load actually sits.",
      "Which task types are non-actionable, meaning they are opened and closed with no action taken.",
    ],
    ongoing: [
      "Tasks per scheduler per day, and time per task type.",
      "Proportion of tasks closed with no action taken.",
      "Scheduling headcount relative to branch volume.",
    ],
  },
  {
    name: "Premium Labor Avoidance",
    baseline: [
      "Agency, contract, per diem and overtime spend for the trailing twelve months, by branch and discipline.",
      "The proportion of that spend committed with less than twenty-four hours notice, which is the reactive portion this lever addresses.",
      "Rate differential between our own per-visit rate and the agency rate for an equivalent visit.",
      "Frequency of visits going uncovered entirely rather than being covered at premium rates.",
    ],
    ongoing: [
      "Premium spend per branch, monthly, split between planned and reactive.",
      "Visits covered at premium rates, weekly.",
      "Visits uncovered, weekly.",
    ],
  },
  {
    name: "Clinician Retention",
    baseline: [
      "Departures over the trailing twenty-four months, with date and length of service.",
      "Proportion of departures occurring within the first year of employment.",
      "Replacement cost per clinician, by discipline.",
      "Weekly visit counts per clinician for the trailing twelve months, which allows schedule stability to be calculated per individual.",
      "Income quoted at hire against income actually earned in the first ninety days.",
      "Stated reasons for leaving, coded consistently rather than captured in free text.",
    ],
    ongoing: [
      "Turnover rate monthly, by discipline and by tenure band.",
      "Week-to-week variability in visit counts per clinician, as an early indicator of resignation risk.",
      "New hires whose first ninety days of earnings fell short of the income quoted at hire.",
    ],
  },
  {
    name: "Travel and Territory Efficiency",
    baseline: [
      "Miles and drive time per visit, by branch and discipline.",
      "Total mileage reimbursement paid over the trailing twelve months.",
      "How territories are currently defined, and when each was last reviewed.",
      "Visits delivered outside the assigned clinician's normal territory.",
    ],
    ongoing: [
      "Miles per visit, monthly, by branch.",
      "Mileage reimbursement relative to visit volume.",
      "Proportion of visits falling outside the assigned territory.",
    ],
  },
];

const futureData = [
  {
    name: "Clinician Recruitment Advantage",
    baseline: [
      "Time to fill a vacancy, by discipline and branch.",
      "Offer acceptance rate, with stated reasons where offers are declined.",
      "Recruiting cost per hire.",
    ],
    ongoing: [
      "Time to fill, monthly.",
      "Offer acceptance rate, monthly.",
    ],
  },
  {
    name: "Authorization Timing Write-Offs",
    baseline: [
      "Visits delivered that could not be billed because approval arrived outside the permitted window.",
      "Elapsed days from our approval request to the insurer's response, by insurer.",
      "Visits held unscheduled pending approval, at a point in time.",
    ],
    ongoing: [
      "Write-offs attributable to late approval, monthly.",
      "Approval turnaround by insurer, monthly.",
      "Visits held pending approval, weekly.",
    ],
  },
];

// ─────────────────────────────────────────────────────── assemble
const kids = [];
kids.push(...TITLE("Capacity and Scheduling",
  "Value levers and measurement requirements"));

kids.push(P("A discussion document. It contains no figures by design. The first section sets out how this program creates financial value. The second sets out what we would need to request in order to size each item and to track it once underway.", { i: true }));

kids.push(RULE());
kids.push(H1("Why scheduling is a financial system"));
kids.push(P("Four characteristics of this business determine how the levers behave. They are worth establishing before the list, because several of the items below behave counterintuitively without them."));
framing.forEach((f) => kids.push(B(f)));

kids.push(RULE());
kids.push(H1("Section one:  value levers"));
levers.forEach((l, i) => {
  kids.push(LEVER(i + 1, l.name));
  kids.push(DEF(l.def));
  l.points.forEach((p) => kids.push(B(p)));
});

kids.push(H1("Identified but not yet quantified"));
kids.push(P("Each of these is credible and deliberately carries no figure, because the data required to value it does not exist today."));
future.forEach((l) => {
  kids.push(SUB(l.name));
  kids.push(DEF(l.def));
  l.points.forEach((p) => kids.push(B(p)));
});

kids.push(new Paragraph({ children: [new TextRun({ text: "", font: FONT })], pageBreakBefore: true }));

kids.push(H1("Section two:  measurement requirements"));
kids.push(P("Two categories for each lever. Baseline data is required once, to establish current performance and size the opportunity. Ongoing data is what we would monitor thereafter to confirm the result. These are different requests: the first is a one-time extract, the second is a reporting commitment that requires an owner.", { i: true }));

data.forEach((d, i) => {
  kids.push(LEVER(i + 1, d.name));
  kids.push(MINI("Baseline"));
  d.baseline.forEach((p) => kids.push(B(p)));
  kids.push(MINI("Ongoing measurement"));
  d.ongoing.forEach((p) => kids.push(B(p)));
});

kids.push(H1("For the items not yet quantified"));
futureData.forEach((d) => {
  kids.push(SUB(d.name));
  kids.push(MINI("Baseline"));
  d.baseline.forEach((p) => kids.push(B(p)));
  kids.push(MINI("Ongoing measurement"));
  d.ongoing.forEach((p) => kids.push(B(p)));
});

kids.push(RULE());
kids.push(H1("On the scale of this request"));
kids.push(B("Every figure in a business case is one of three things: measured, published, or assumed. At present too many of ours are assumed."));
kids.push(B("This list is what converts the assumed figures into measured ones."));
kids.push(B("The majority already exists within systems we own and can be produced as extracts. A smaller number, particularly around canceled visits and reassessment windows, is not captured anywhere today and would require new instrumentation."));
kids.push(B("Those two gaps are notable in themselves. They are the areas where we currently cannot see the loss we are attempting to address."));

const doc = new Document({
  numbering: {
    config: [{
      reference: "dot",
      levels: [{
        level: 0,
        format: LevelFormat.BULLET,
        text: "\u2022",
        alignment: AlignmentType.LEFT,
        style: { paragraph: { indent: { left: 460, hanging: 260 } } },
      }],
    }],
  },
  sections: [{
    properties: {
      page: {
        size: { width: 12240, height: 15840 },
        margin: { top: 1080, right: 1080, bottom: 1080, left: 1080 },
      },
    },
    children: kids,
  }],
});

Packer.toBuffer(doc).then((buf) => {
  fs.writeFileSync("C:/Users/chigh/Downloads/Capacity-Scheduling-Business-Case-Discussion.docx", buf);
  console.log("written");
});
