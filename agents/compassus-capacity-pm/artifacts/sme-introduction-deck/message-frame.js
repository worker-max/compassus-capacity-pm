// Compassus — Message Frame: anchor words, four-column view, and story (3 slides, same masters as the SME deck)
const pptxgen = require("pptxgenjs");

const NAVY = "002554", GOLD = "CE8E00", GOLD_D = "8A5F00", PAPER = "F8F6F1", CARD = "FDFCFA",
  RULE = "E3DED3", RULE2 = "D6D0C2", BODY = "3D4A5C", MUTED = "5A6472", NBODY = "C9D3E0", NMUTED = "9AAAC0", NLINE = "2A4A78";
const HEAD = "Maven Pro", TEXT = "Arial";
const P = (v) => v / 144;
const FOOT = "Capacity & Scheduling · SME Introduction";

const pres = new pptxgen();
pres.layout = "LAYOUT_WIDE";
pres.title = "Message Frame — Our Anchor Words";
const master = (title, bg, logo, foot, eb, tt) => pres.defineSlideMaster({
  title, background: { color: bg },
  objects: [
    { image: { path: logo, x: P(128), y: P(976), w: P(104), h: P(40) } },
    { text: { text: FOOT, options: { x: P(256), y: P(976), w: P(900), h: P(40), fontFace: TEXT, fontSize: 12, color: foot, margin: 0, valign: "middle" } } },
    { placeholder: { options: { name: "eyebrow", type: "body", x: P(128), y: P(128), w: P(1664), h: P(40), fontFace: TEXT, fontSize: 12, bold: true, color: eb, charSpacing: 2, margin: 0, valign: "top" }, text: "EYEBROW LABEL" } },
    { placeholder: { options: { name: "title", type: "title", x: P(128), y: P(176), w: P(1664), h: P(100), fontFace: HEAD, fontSize: 40, color: tt, margin: 0, valign: "top", align: "left" }, text: "Slide title" } },
  ],
  slideNumber: { x: P(1592), y: P(976), w: P(200), h: P(40), fontFace: TEXT, fontSize: 12, color: foot, align: "right", valign: "middle" },
});
master("Compassus · Light", PAPER, "compassus-logo-color.png", MUTED, GOLD_D, NAVY);

const F = {
  problem: { label: "Problem", word: "DECISIONS", lead: "Today, every branch runs on", pts: ["Hard: too many visits, windows, authorizations and territories to weigh by hand", "Disjointed: spread across HCHB, spreadsheets, Workday and memory", "Complex: every choice ripples across patients, clinicians and compliance"] },
  solution: { label: "Solution", word: "OPTIMIZED", lead: "Our solution must be", pts: ["Capacity visible by discipline and territory", "Repetitive scheduling steps automated", "Recommendations that show their reasoning"] },
  approach: { label: "Approach", word: "CLINICIAN-\nCENTERED", word1: "CLINICIAN-CENTERED", lead: "Our approach is", pts: ["Field experts help choose the tool", "Flexibility and continuity protected", "Capacity first, then a measured pilot before scaling"] },
  result: { label: "Result", word: "GROWTH", lead: "The result is", pts: ["Business growth: more referrals accepted with confidence", "Employee retention: time back for PCCs and clinicians", "More patients served"] },
};

const T = (s, text, o) => s.addText(text, { x: P(o.x), y: P(o.y), w: P(o.w), h: P(o.h), fontFace: o.font || TEXT, fontSize: o.pt, color: o.color || NAVY, bold: !!o.bold, margin: 0, valign: o.valign || "top", align: o.align || "left", charSpacing: o.cs, lineSpacingMultiple: o.lh, isTextBox: true });
const bullets = (s, items, o) => s.addText(items.map((t, i) => ({ text: t, options: { bullet: { indent: 14 }, breakLine: i < items.length - 1 } })), { x: P(o.x), y: P(o.y), w: P(o.w), h: P(o.h), fontFace: TEXT, fontSize: o.pt || 12.5, color: o.color || BODY, margin: 0, valign: o.valign || "middle", paraSpaceAfter: 6, isTextBox: true });

// ---------- Slide 1: the frame ----------
let s = pres.addSlide({ masterName: "Compassus · Light" });
s.addText("MESSAGE FRAME · OUR ANCHOR WORDS", { placeholder: "eyebrow" });
s.addText("Four words every leader can repeat", { placeholder: "title" });
const BW = 380, BH = 210, XL = 520, XR = 1020, YT = 330, YB = 650;
const box = (x, y, f, small) => {
  s.addShape(pres.shapes.RECTANGLE, { x: P(x), y: P(y), w: P(BW), h: P(BH), fill: { color: NAVY }, line: { type: "none" } });
  T(s, f.label.toUpperCase(), { x: x + 32, y: y + 30, w: BW - 64, h: 30, pt: 11, bold: true, color: GOLD, cs: 1.5 });
  T(s, f.word, { x: x + 32, y: y + 64, w: BW - 64, h: 120, pt: small ? 21 : 26, font: HEAD, color: PAPER, valign: "middle", lh: 0.95 });
};
box(XL, YB, F.problem); box(XL, YT, F.solution); box(XR, YT, F.approach, true); box(XR, YB, F.result);
s.addShape(pres.shapes.LINE, { x: P(XL + BW / 2), y: P(YT + BH + 8), w: 0, h: P(YB - YT - BH - 16), line: { color: GOLD, width: 2, beginArrowType: "triangle" } });
s.addShape(pres.shapes.LINE, { x: P(XL + BW + 8), y: P(YT + BH / 2), w: P(XR - XL - BW - 16), h: 0, line: { color: GOLD, width: 2, endArrowType: "triangle" } });
s.addShape(pres.shapes.LINE, { x: P(XR + BW / 2), y: P(YT + BH + 8), w: 0, h: P(YB - YT - BH - 16), line: { color: GOLD, width: 2, endArrowType: "triangle" } });
const LW = XL - 128 - 40, RX = XR + BW + 40, RW = 1792 - RX;
bullets(s, F.problem.pts.map((t) => t.split(":")[0]), { x: 128, y: YB, w: LW, h: BH, pt: 13 });
bullets(s, F.solution.pts, { x: 128, y: YT, w: LW, h: BH, pt: 12 });
bullets(s, F.approach.pts, { x: RX, y: YT, w: RW, h: BH, pt: 12 });
bullets(s, ["Business growth", "Employee retention", "Patients served"], { x: RX, y: YB, w: RW, h: BH, pt: 13 });
s.addNotes("The four anchor words stay the same, always: Decisions, Optimized, Clinician-Centered, Growth. What changes is how you illustrate them for the listener. Problem: decisions are hard, disjointed and complex. Solution: optimized. Approach: clinician-centered. Result: growth, in the business, in employee retention, and in patients served.");

// ---------- Slide 2: four columns ----------
s = pres.addSlide({ masterName: "Compassus · Light" });
s.addText("MESSAGE FRAME · WHAT IT MEANS", { placeholder: "eyebrow" });
s.addText("From hard decisions to growth", { placeholder: "title" });
[F.problem, F.solution, F.approach, F.result].forEach((f, i) => {
  const x = 128 + i * 422, w = 398, y = 300, dark = i % 2 === 0;
  s.addShape(pres.shapes.RECTANGLE, { x: P(x), y: P(y), w: P(w), h: P(610), fill: { color: dark ? NAVY : CARD }, line: { color: dark ? NAVY : RULE, width: 0.75 } });
  T(s, f.label.toUpperCase(), { x: x + 36, y: y + 32, w: w - 72, h: 28, pt: 10.5, bold: true, color: dark ? NMUTED : MUTED, cs: 1.5 });
  T(s, f.lead, { x: x + 36, y: y + 64, w: w - 72, h: 30, pt: 13, color: dark ? NBODY : BODY });
  T(s, f.word, { x: x + 36, y: y + 100, w: w - 72, h: 100, pt: i === 2 ? 22 : 26, font: HEAD, bold: true, color: dark ? GOLD : NAVY, valign: "middle", lh: 0.95 });
  s.addShape(pres.shapes.LINE, { x: P(x + 36), y: P(y + 220), w: P(w - 72), h: 0, line: { color: dark ? NLINE : RULE2, width: 1.5 } });
  bullets(s, f.pts, { x: x + 36, y: y + 248, w: w - 72, h: 330, pt: 12.5, valign: "top", color: dark ? NBODY : BODY });
});
s.addNotes("The same four anchor words, read left to right as one sentence: today every branch runs on decisions that are hard, disjointed and complex; our solution must be optimized; our approach is clinician-centered; the result is growth.");

// ---------- Slide 3: the story ----------
s = pres.addSlide({ masterName: "Compassus · Light" });
s.addText("MESSAGE FRAME · EXAMPLE STORY", { placeholder: "eyebrow" });
s.addText("How it sounds out loud", { placeholder: "title" });
T(s, "The four anchor words stay the same, always. The facts and examples change to fit the listener.", { x: 128, y: 290, w: 1664, h: 34, pt: 13, color: MUTED });
const story = [
  [["“Every day, our branches make hundreds of capacity and scheduling "], ["decisions", 1], [". Today those decisions are hard, disjointed and complex. The information lives in HCHB, spreadsheets, Workday and people's memories, so our PCCs and clinicians spend their time piecing it together."]],
  [["We need those decisions "], ["optimized", 1], [": capacity visible at a glance, the repetitive steps automated, and clear recommendations that show their reasoning."]],
  [["Our approach is "], ["clinician-centered", 1], [". The people who do the work are helping choose the tool, we are protecting the flexibility clinicians value, and we will prove it in a measured pilot before we scale."]],
  [["The result is "], ["growth", 1], [": branches that can say yes to more referrals, teams that want to stay, and more patients served.”"]],
];
s.addText(story.map((para, i) => para.map(([t, b], j) => ({ text: t, options: { ...(b ? { bold: true, color: GOLD_D } : {}), ...(j === para.length - 1 && i < story.length - 1 ? { breakLine: true } : {}) } }))).flat(),
  { x: P(200), y: P(350), w: P(1520), h: P(560), fontFace: HEAD, fontSize: 17, color: NAVY, margin: 0, valign: "middle", lineSpacingMultiple: 1.2, paraSpaceAfter: 12, isTextBox: true });
s.addNotes("Use this as a model, not a script. Keep the four anchor words exactly as they are, and swap in facts and examples from your own branch: a decision that went wrong last week, the spreadsheet you maintain, the clinician who stayed because the schedule worked for them.");

pres.writeFile({ fileName: "Compassus-Message-Frame.pptx" }).then(() => console.log("written"));
