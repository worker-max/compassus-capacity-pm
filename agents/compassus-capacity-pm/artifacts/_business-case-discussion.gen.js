const fs = require("fs");
const {
  Document, Packer, Paragraph, TextRun, HeadingLevel, AlignmentType,
  LevelFormat, PageOrientation, BorderStyle,
} = require("docx");

const FONT = "Arial";

const H1 = (t) => new Paragraph({
  heading: HeadingLevel.HEADING_1,
  spacing: { before: 360, after: 160 },
  children: [new TextRun({ text: t, font: FONT, size: 30, bold: true, color: "1F3864" })],
});

const H2 = (t) => new Paragraph({
  heading: HeadingLevel.HEADING_2,
  spacing: { before: 300, after: 100 },
  children: [new TextRun({ text: t, font: FONT, size: 24, bold: true, color: "1F3864" })],
});

const H3 = (t) => new Paragraph({
  spacing: { before: 200, after: 80 },
  children: [new TextRun({ text: t, font: FONT, size: 21, bold: true })],
});

const P = (t, opts = {}) => new Paragraph({
  spacing: { after: 120 },
  children: [new TextRun({ text: t, font: FONT, size: 21, italics: !!opts.i, bold: !!opts.b })],
});

const B = (t) => new Paragraph({
  numbering: { reference: "dot", level: 0 },
  spacing: { after: 80 },
  children: [new TextRun({ text: t, font: FONT, size: 21 })],
});

const RULE = () => new Paragraph({
  spacing: { before: 120, after: 200 },
  border: { bottom: { style: BorderStyle.SINGLE, size: 6, color: "BFBFBF" } },
  children: [new TextRun({ text: "", font: FONT, size: 2 })],
});

// ─────────────────────────────────────────────── the levers
const levers = [
  {
    name: "1.  We start more patients on service",
    points: [
      "A clinician's open slot for tomorrow is like an empty seat on tomorrow's flight. If it does not get filled, it is gone. It does not carry over to the next day.",
      "Today the answer to whether we can take a patient is slow, so slots expire while we are still working it out.",
      "The referral system is getting better at accepting referrals. This picks up where that leaves off and turns an acceptance into a started episode before the capacity to serve it disappears.",
      "The faster we can say yes or no, the more chances we get to fill or replace the slot before it stops existing.",
      "This only works if there are referrals to take. There are, because we currently decline some for lack of capacity.",
    ],
  },
  {
    name: "2.  We replace a canceled visit before the clinician's day is lost",
    points: [
      "A patient cancels, usually the evening before or the same morning. Rescheduling that patient is normally handled during the cancellation call. That part is not the problem.",
      "What is left behind is a hole in the clinician's day, and today we often cannot fill it fast enough for a replacement to actually fit their schedule and their driving.",
      "Filling it means knowing straight away which other patients are due, which are near enough, who is approved, and which visits are flexible enough to move.",
      "Sometimes the right answer is pulling a visit forward from later in the week. That trades a hole we cannot fill today for one we have several days to fill.",
      "With most clinicians paid per visit, that lost slot is lost income for them, not lost revenue for us. This is one of the clearest links between how well we schedule and why people leave.",
      "This gets harder as scheduling gets better. A tightly planned week has less slack to absorb a cancellation than a loose one, so the ability to replace has to arrive with the optimization, not after it.",
    ],
  },
  {
    name: "3.  Fewer Medicare periods fall short on visits",
    points: [
      "Medicare pays a fixed amount for a period of care, but only if a minimum number of visits happen. Miss it and the payment for the whole period drops sharply.",
      "Most misses are by a single visit, and usually because a visit was missed or moved rather than because fewer visits were needed.",
      "Today we find out after the period closes, when nothing can be done about it.",
      "Seeing it coming while days remain is the entire difference. That is a tracking and visibility problem, not a clinical one.",
      "The line we do not cross: we would never add a visit a patient does not need in order to reach a number. Federal auditors are actively looking for exactly that pattern.",
    ],
  },
  {
    name: "4.  Fewer therapy reassessment write-offs",
    points: [
      "Therapy requires reassessment visits at set points in an episode. If the reassessment does not happen inside its window, visits we already delivered cannot be billed.",
      "This is the worst kind of loss. We did the work, we paid the clinician for it, and we cannot bill for it.",
      "It is tracked by hand today, by schedulers, alongside dozens of other daily tasks competing for the same attention.",
      "It is the same shape of problem as the Medicare visit count: a deadline attached to an episode that nobody can see approaching, discovered only after it has passed.",
      "That is why the two belong together. One mechanism fixes both, which is holding every episode deadline in one place and surfacing it with enough lead time to act.",
      "Worth asking in the room: does anyone currently report how often this happens, or what it costs us?",
    ],
  },
  {
    name: "5.  Scheduling takes fewer people",
    points: [
      "Schedulers today spend most of their day working a task list rather than making scheduling decisions.",
      "The same patient generates a separate task for every discipline involved, and again when it is approved.",
      "Remove that repetitive work and the roles are no longer needed at the same number.",
      "Two honest caveats. Some of this work should not exist at all, so we cannot claim credit for removing all of it. And published examples of this kind of software elsewhere have freed far fewer roles than the figure discussed on site.",
      "The role should not disappear entirely. Someone still has to handle urgency, local knowledge, and the relationships that make coverage happen.",
    ],
  },
  {
    name: "6.  We buy less premium labor",
    points: [
      "Premium labor is anything we pay above our normal rate to get a visit covered. Agency and contract clinicians, per diem staff at premium rates, overtime, and bonuses for picking up extra work.",
      "When someone calls out early in the morning, nobody can see who has room, so the branch reaches for the most expensive option or loses the visit.",
      "Seeing available capacity turns an emergency purchase into a planned assignment by someone already on the payroll.",
      "One caveat. Because most of our clinicians are paid per visit, the saving is the difference between our rate and the agency rate, not the whole agency bill. In an organization with salaried clinicians this lever would be much larger.",
    ],
  },
  {
    name: "7.  Fewer clinicians leave",
    points: [
      "Most of our clinicians are paid per visit, so an unpredictable schedule is an unpredictable paycheck.",
      "Published research on home health nurses found that those with the most erratic week-to-week visit counts were markedly more likely to quit, and that steadying the schedule reduced it.",
      "The effect showed up only in full-time staff, which fits. It is people who depend on the income who leave over it.",
      "It bites hardest in the first year, when a clinician is slower, does not know the territory, and is deciding whether the job pays what they were told it would.",
      "This is the same mechanism as lever two, seen from the other side. Every unfilled slot is income the clinician expected and did not get.",
    ],
  },
  {
    name: "8.  Less driving",
    points: [
      "Territories today are drawn by hand and rarely redrawn. A day's visits are grouped by distance rather than by how long the drive actually takes.",
      "Better grouping and territories built on real drive times reduce miles.",
      "One caveat worth being straight about. With most clinicians paid per visit, the time saved belongs to them, not to us. What we save is the mileage we reimburse.",
      "The time they get back becomes capacity, which is counted in lever one. Counting it in both places would be the easiest mistake to make in this whole case.",
    ],
  },
];

const future = [
  {
    name: "Easier to recruit clinicians",
    points: [
      "Clinicians currently spend part of every evening, unpaid, calling tomorrow's patients to confirm. That goes away.",
      "A recruit who is quoted an expected income is far more likely to actually earn it when their week is protected and a canceled visit gets replaced.",
      "Left without a number because we do not yet track how long a vacancy takes to fill, how often offers are accepted, or what a hire costs us.",
    ],
  },
  {
    name: "The same approach applied to hospice",
    points: [
      "The prior working session concluded hospice needs a few added rules rather than a different product.",
      "It would extend what this is worth at little additional cost. Left out until home health proves it.",
    ],
  },
  {
    name: "Care we deliver and cannot bill because approval came late",
    points: [
      "Insurers allow only a short window to backdate an approval. Care delivered outside it is written off.",
      "Nobody counts this today. It could be immaterial or it could be the largest item on this page.",
      "It is the first thing worth measuring, precisely because we have no idea which it is.",
    ],
  },
];

// ─────────────────────────────────────────────── the data asks
const data = [
  {
    name: "1.  We start more patients on service",
    baseline: [
      "New patient starts per year, by branch and by month.",
      "Time stamps at each step between accepting a referral and the first visit: referral accepted, insurance verified, intake approved, patient contacted, visit scheduled, visit delivered.",
      "Referrals we declined, with the reason, separating those declined for lack of capacity from all other reasons.",
      "Start-of-care visits offered to clinicians against those actually filled.",
      "Which clinicians are qualified and available to admit a new patient, as opposed to only doing routine visits.",
    ],
    ongoing: [
      "Median and worst-case time from referral accepted to first visit, weekly.",
      "Referrals declined for capacity, weekly, by branch.",
      "Start-of-care slots available against filled, weekly.",
      "Admissions per branch against the prior period.",
    ],
  },
  {
    name: "2.  We replace a canceled visit before the clinician's day is lost",
    baseline: [
      "Canceled and missed visits: how many, and how long before the visit the cancellation came.",
      "The reason for each cancellation, separating patient-initiated from clinician-initiated.",
      "Of those cancellations, how many left a gap in the clinician's day that was never filled. This is the actual loss and it is the number nobody currently has.",
      "Where a gap was filled, how long it took from cancellation to a replacement being assigned.",
      "How often a visit is pulled forward from later in the week to cover a gap, and whether the later gap then got filled.",
      "Which visit types are genuinely flexible on timing, from clinical leadership rather than from the system.",
    ],
    ongoing: [
      "Cancellations per week, and the share that left an unfilled gap.",
      "Average time from cancellation to replacement assigned.",
      "Clinician slots lost to cancellation, per branch, per week.",
      "Visits moved forward to cover a gap, and how often that created a second gap that also went unfilled.",
    ],
  },
  {
    name: "3.  Fewer Medicare periods fall short on visits",
    baseline: [
      "How often periods close below the visit threshold, by branch.",
      "For those that fell short, by how many visits.",
      "For the ones that missed by a single visit, whether a visit was missed, moved, or held waiting on approval.",
      "What a period costs us to deliver, so the loss can be stated as margin rather than revenue.",
    ],
    ongoing: [
      "Periods currently open that are tracking below threshold, with days remaining.",
      "Periods that closed short in the last month, with the cause coded.",
      "Share of short periods that were preventable, meaning a needed visit was lost rather than not needed.",
    ],
  },
  {
    name: "4.  Fewer therapy reassessment write-offs",
    baseline: [
      "How many therapy reassessments were completed outside their required window, by branch and by discipline.",
      "The value of visits written off as a result.",
      "How far past the window the late ones typically fell, since a day late and three weeks late are different problems.",
      "Whether the miss was a scheduling failure, a clinician availability failure, or a documentation failure.",
      "How reassessment deadlines are tracked today, and by whom.",
    ],
    ongoing: [
      "Reassessments coming due in the next two weeks, with status.",
      "Share completed inside the window, monthly.",
      "Write-off dollars attributed to missed reassessment windows, monthly.",
    ],
  },
  {
    name: "5.  Scheduling takes fewer people",
    baseline: [
      "Ninety days of scheduler task records with start and finish times, grouped by task type.",
      "How many people currently work in scheduling, by branch, and what they are paid including benefits.",
      "How the task load is distributed across them, since averages hide who is drowning.",
      "Which tasks are genuinely non-actionable, meaning they are opened and closed with nothing done.",
    ],
    ongoing: [
      "Tasks per scheduler per day, and time spent per task type.",
      "Share of tasks closed with no action taken.",
      "Scheduler headcount against branch volume.",
    ],
  },
  {
    name: "6.  We buy less premium labor",
    baseline: [
      "Agency, contract, per diem and overtime spend for the last twelve months, by branch and by discipline.",
      "How much of that spend was booked with less than twenty-four hours notice, which is the reactive portion this lever targets.",
      "The rate difference between our own per-visit rate and what we pay agency for the same visit.",
      "How often a visit went uncovered entirely rather than being covered at premium.",
    ],
    ongoing: [
      "Premium spend per branch, monthly, split between planned and reactive.",
      "Visits covered at premium rates, weekly.",
      "Visits that went uncovered, weekly.",
    ],
  },
  {
    name: "7.  Fewer clinicians leave",
    baseline: [
      "Who left, when, and how long they had been here, for the last twenty-four months.",
      "The share of departures that happened inside the first year.",
      "What it costs us to replace a clinician, by discipline.",
      "Each clinician's visit count by week for the last twelve months, which lets us calculate how steady each person's week actually is.",
      "Pay quoted at hire against pay actually earned in the first ninety days.",
      "Reasons people gave for leaving, coded consistently rather than in free text.",
    ],
    ongoing: [
      "Turnover rate, monthly, split by discipline and by tenure.",
      "Week-to-week variability in visit counts per clinician, as an early warning of who is at risk.",
      "New hires whose earnings in the first ninety days fell short of what they were quoted.",
    ],
  },
  {
    name: "8.  Less driving",
    baseline: [
      "Miles and drive time per visit, by branch and by discipline.",
      "Total mileage reimbursement paid, for the last twelve months.",
      "How territories are currently defined, and when each was last reviewed.",
      "Visits delivered outside the assigned clinician's normal territory.",
    ],
    ongoing: [
      "Miles per visit, monthly, by branch.",
      "Mileage reimbursement against visit volume.",
      "Share of visits falling outside the assigned territory.",
    ],
  },
];

const futureData = [
  {
    name: "Easier to recruit clinicians",
    baseline: [
      "How long a vacancy takes to fill, by discipline and branch.",
      "How often offers are accepted, and the reasons given when they are declined.",
      "What a hire costs us in recruiting spend.",
    ],
    ongoing: [
      "Time to fill, monthly.",
      "Offer acceptance rate, monthly.",
    ],
  },
  {
    name: "Care we deliver and cannot bill because approval came late",
    baseline: [
      "Visits delivered that we could not bill because approval arrived outside the allowed window.",
      "Days from our approval request to the insurer's answer, by insurer.",
      "Visits sitting unscheduled while waiting on approval, at a point in time.",
    ],
    ongoing: [
      "Write-offs attributed to late approval, monthly.",
      "Approval turnaround by insurer, monthly.",
      "Visits held waiting on approval, weekly.",
    ],
  },
];

// ─────────────────────────────────────────────── assemble
const kids = [];

kids.push(new Paragraph({
  spacing: { after: 80 },
  children: [new TextRun({ text: "Capacity and Scheduling", font: FONT, size: 40, bold: true, color: "1F3864" })],
}));
kids.push(new Paragraph({
  spacing: { after: 320 },
  children: [new TextRun({ text: "The business case levers, and what we need to measure them", font: FONT, size: 24, color: "595959" })],
}));
kids.push(P("This is a discussion document. It deliberately contains no numbers. The first list is how this program makes or saves money. The second list is what we would need to request in order to put real figures against each one, both to establish where we stand today and to track it afterwards.", { i: true }));
kids.push(RULE());

kids.push(H1("Part one:  the business case levers"));
levers.forEach((l) => {
  kids.push(H2(l.name));
  l.points.forEach((p) => kids.push(B(p)));
});

kids.push(H2("Things we believe are real but have not put a number on"));
future.forEach((l) => {
  kids.push(H3(l.name));
  l.points.forEach((p) => kids.push(B(p)));
});

kids.push(new Paragraph({ children: [new TextRun({ text: "", font: FONT })], pageBreakBefore: true }));

kids.push(H1("Part two:  what we need to measure each one"));
kids.push(P("Two kinds of data for each lever. Baseline is what we need once, to establish where we stand today and size the opportunity. Ongoing is what we would watch afterwards to know whether it is working.", { i: true }));

data.forEach((d) => {
  kids.push(H2(d.name));
  kids.push(H3("To establish the baseline"));
  d.baseline.forEach((p) => kids.push(B(p)));
  kids.push(H3("To measure it on an ongoing basis"));
  d.ongoing.forEach((p) => kids.push(B(p)));
});

kids.push(H2("For the items we have not yet priced"));
futureData.forEach((d) => {
  kids.push(H3(d.name));
  kids.push(P("To establish the baseline", { b: true }));
  d.baseline.forEach((p) => kids.push(B(p)));
  kids.push(P("To measure it on an ongoing basis", { b: true }));
  d.ongoing.forEach((p) => kids.push(B(p)));
});

kids.push(RULE());
kids.push(H2("If asked why we need all of this"));
kids.push(B("Every figure in a business case is one of three things: measured, published, or assumed. Today too many of ours are assumed."));
kids.push(B("This list is what turns the assumed ones into measured ones."));
kids.push(B("Most of it already exists in systems we own. A smaller number of items, particularly around canceled visits and reassessment windows, are not captured anywhere today and would need to be."));

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
