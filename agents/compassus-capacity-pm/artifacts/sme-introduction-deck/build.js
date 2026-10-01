// Compassus — Capacity & Scheduling SME Introduction (editable .pptx with branded masters)
const pptxgen = require("pptxgenjs");
const sharp = require("sharp");
const fs = require("fs");

const NAVY = "002554", GOLD = "CE8E00", GOLD_D = "8A5F00", PAPER = "F8F6F1", CARD = "FDFCFA",
  RULE = "E3DED3", RULE2 = "D6D0C2", BODY = "3D4A5C", MUTED = "5A6472", NBODY = "C9D3E0",
  NMUTED = "9AAAC0", NLINE = "2A4A78", TINT = "EFEBE2", NAVY2 = "0F3A73";
const HEAD = "Maven Pro", TEXT = "Arial";
const P = (v) => v / 144;          // canvas px (1920 wide) -> inches (13.333)
const S = (v) => v / 2;            // canvas px -> points
const LOGO_C = "compassus-logo-color.png", LOGO_R = "compassus-logo-reverse.png";
const FOOT = "Capacity & Scheduling · SME Introduction";

async function main() {
  const dotSvg = `<svg xmlns="http://www.w3.org/2000/svg" width="1120" height="1120" viewBox="0 0 560 560"><defs><pattern id="s" width="80" height="80" patternUnits="userSpaceOnUse"><circle cx="40" cy="40" r="12" fill="none" stroke="#2A4A78" stroke-width="2"/></pattern></defs><rect width="560" height="560" fill="url(#s)"/><g fill="#CE8E00">${[[40,520],[120,520],[200,520],[280,520],[360,520],[40,440],[120,440],[200,440],[280,440],[40,360],[120,360],[200,360],[40,280],[120,280],[40,200]].map(([x,y])=>`<circle cx="${x}" cy="${y}" r="14"/>`).join("")}</g><circle cx="440" cy="120" r="14" fill="#F8F6F1"/><circle cx="440" cy="120" r="28" fill="none" stroke="#F8F6F1" stroke-width="2"/></svg>`;
  await sharp(Buffer.from(dotSvg)).png().toFile("dotgrid.png");

  const pres = new pptxgen();
  pres.layout = "LAYOUT_WIDE";
  pres.title = "Capacity & Scheduling — SME Introduction";
  pres.company = "Compassus";

  // ---------- masters ----------
  const footer = (dark, gold) => {
    const c = gold ? NAVY : dark ? NMUTED : MUTED;
    return [
      { image: { path: gold ? LOGO_C : dark ? LOGO_R : LOGO_C, x: P(128), y: P(976), w: P(104), h: P(40) } },
      { text: { text: FOOT, options: { x: P(256), y: P(976), w: P(900), h: P(40), fontFace: TEXT, fontSize: 12, color: c, margin: 0, valign: "middle" } } },
    ];
  };
  const num = (c) => ({ x: P(1592), y: P(976), w: P(200), h: P(40), fontFace: TEXT, fontSize: 12, color: c, align: "right", valign: "middle" });
  const eyebrowPh = (c) => ({ placeholder: { options: { name: "eyebrow", type: "body", x: P(128), y: P(128), w: P(1664), h: P(40), fontFace: TEXT, fontSize: 12, bold: true, color: c, charSpacing: 2, margin: 0, valign: "top" }, text: "EYEBROW LABEL" } });
  const titlePh = (c) => ({ placeholder: { options: { name: "title", type: "title", x: P(128), y: P(176), w: P(1664), h: P(100), fontFace: HEAD, fontSize: 40, color: c, margin: 0, valign: "top", align: "left" }, text: "Slide title" } });

  pres.defineSlideMaster({ title: "Compassus · Light", background: { color: PAPER }, objects: [...footer(false), eyebrowPh(GOLD_D), titlePh(NAVY)], slideNumber: num(MUTED) });
  pres.defineSlideMaster({ title: "Compassus · Navy", background: { color: NAVY }, objects: [...footer(true), eyebrowPh(GOLD), titlePh(PAPER)], slideNumber: num(NMUTED) });
  pres.defineSlideMaster({ title: "Compassus · Gold", background: { color: GOLD }, objects: [...footer(false, true)], slideNumber: num(NAVY) });
  pres.defineSlideMaster({ title: "Compassus · Navy plain", background: { color: NAVY }, objects: [] });
  // template-only masters (with body placeholders)
  const bodyPh = (name, x, y, w, h, c, prompt) => ({ placeholder: { options: { name, type: "body", x: P(x), y: P(y), w: P(w), h: P(h), fontFace: TEXT, fontSize: 14, color: c, margin: 0, valign: "top" }, text: prompt } });
  pres.defineSlideMaster({ title: "Compassus · Section divider", background: { color: NAVY }, objects: [
    { image: { path: LOGO_R, x: P(128), y: P(128), w: P(300), h: P(115) } },
    { image: { path: "dotgrid.png", x: P(1232), y: P(240), w: P(560), h: P(560) } },
    { placeholder: { options: { name: "eyebrow", type: "body", x: P(128), y: P(520), w: P(1040), h: P(40), fontFace: TEXT, fontSize: 12, bold: true, color: GOLD, charSpacing: 2, margin: 0 }, text: "SECTION LABEL" } },
    { placeholder: { options: { name: "title", type: "title", x: P(128), y: P(560), w: P(1040), h: P(260), fontFace: HEAD, fontSize: 52, color: PAPER, margin: 0, valign: "top", align: "left" }, text: "Section title" } },
    { placeholder: { options: { name: "sub", type: "body", x: P(128), y: P(840), w: P(1000), h: P(80), fontFace: TEXT, fontSize: 16, color: NBODY, margin: 0, valign: "top" }, text: "One line that sets up the section" } },
  ] });
  pres.defineSlideMaster({ title: "Compassus · Light + body", background: { color: PAPER }, objects: [...footer(false), eyebrowPh(GOLD_D), titlePh(NAVY), bodyPh("body", 128, 322, 1664, 560, BODY, "Add your content")], slideNumber: num(MUTED) });
  pres.defineSlideMaster({ title: "Compassus · Light two columns", background: { color: PAPER }, objects: [...footer(false), eyebrowPh(GOLD_D), titlePh(NAVY), bodyPh("left", 128, 322, 800, 560, BODY, "Left column"), bodyPh("right", 992, 322, 800, 560, BODY, "Right column")], slideNumber: num(MUTED) });
  const card = (x) => ({ rect: { x: P(x), y: P(322), w: P(533), h: P(540), fill: { color: CARD }, line: { color: RULE, width: 0.75 } } });
  pres.defineSlideMaster({ title: "Compassus · Light three cards", background: { color: PAPER }, objects: [...footer(false), eyebrowPh(GOLD_D), titlePh(NAVY), card(128), card(693), card(1258),
    bodyPh("card1", 176, 370, 437, 444, BODY, "Card one"), bodyPh("card2", 741, 370, 437, 444, BODY, "Card two"), bodyPh("card3", 1306, 370, 437, 444, BODY, "Card three")], slideNumber: num(MUTED) });
  pres.defineSlideMaster({ title: "Compassus · Navy + body", background: { color: NAVY }, objects: [...footer(true), eyebrowPh(GOLD), titlePh(PAPER), bodyPh("body", 128, 322, 1664, 560, NBODY, "Add your content")], slideNumber: num(NMUTED) });
  pres.defineSlideMaster({ title: "Compassus · Gold statement", background: { color: GOLD }, objects: [...footer(false, true),
    { placeholder: { options: { name: "eyebrow", type: "body", x: P(128), y: P(128), w: P(1664), h: P(40), fontFace: TEXT, fontSize: 12, bold: true, color: NAVY, charSpacing: 2, margin: 0 }, text: "EYEBROW LABEL" } },
    { placeholder: { options: { name: "title", type: "title", x: P(128), y: P(300), w: P(1500), h: P(400), fontFace: HEAD, fontSize: 48, color: NAVY, margin: 0, valign: "middle", align: "left" }, text: "A single statement worth a whole slide." } },
  ], slideNumber: num(NAVY) });

  // ---------- helpers ----------
  const T = (s, text, o) => s.addText(text, {
    x: P(o.x), y: P(o.y), w: P(o.w), h: P(o.h), fontFace: o.font || TEXT, fontSize: S(o.size || 24),
    color: o.color || NAVY, bold: !!o.bold, italic: !!o.italic, margin: 0, valign: o.valign || "top",
    align: o.align || "left", lineSpacingMultiple: o.lh || 1.1, charSpacing: o.cs, isTextBox: true,
    paraSpaceAfter: o.psa,
  });
  const R = (s, o) => s.addShape(o.radius ? pres.shapes.ROUNDED_RECTANGLE : pres.shapes.RECTANGLE, {
    x: P(o.x), y: P(o.y), w: P(o.w), h: P(o.h), fill: o.fill ? { color: o.fill } : { type: "none" },
    line: o.line ? { color: o.line, width: o.lw || 0.75, dashType: o.dash || "solid" } : { type: "none" },
    rectRadius: o.radius,
  });
  const L = (s, x, y, w, color, pt = 0.75, dash) => s.addShape(pres.shapes.LINE, { x: P(x), y: P(y), w: P(w), h: 0, line: { color, width: pt, dashType: dash || "solid" } });
  const bullets = (s, items, o) => s.addText(items.map((t, i) => ({ text: t, options: { bullet: { indent: 14 }, breakLine: i < items.length - 1 } })), {
    x: P(o.x), y: P(o.y), w: P(o.w), h: P(o.h), fontFace: TEXT, fontSize: S(o.size || 26), color: o.color || BODY,
    margin: 0, valign: "top", paraSpaceAfter: 6, lineSpacingMultiple: 1.05, isTextBox: true,
  });
  const head = (s, eyebrow, title) => { s.addText(eyebrow.toUpperCase(), { placeholder: "eyebrow" }); s.addText(title, { placeholder: "title" }); };

  // 1 Cover
  let s = pres.addSlide({ masterName: "Compassus · Navy plain" });
  s.addImage({ path: "dotgrid.png", x: P(1232), y: P(240), w: P(560), h: P(560) });
  s.addImage({ path: LOGO_R, x: P(128), y: P(128), w: P(300), h: P(115) });
  T(s, "HOME HEALTH · CAPACITY & SCHEDULING INITIATIVE", { x: 128, y: 340, w: 1040, h: 40, color: GOLD, bold: true, cs: 2.5 });
  s.addText([{ text: "The people closest to the work, ", options: { color: PAPER } }, { text: "shaping the choice.", options: { color: GOLD } }],
    { x: P(128), y: P(396), w: P(1040), h: P(400), fontFace: HEAD, fontSize: 52, margin: 0, valign: "top", lineSpacingMultiple: 0.95, isTextBox: true });
  T(s, "Introducing the subject matter experts guiding vendor identification and selection", { x: 128, y: 830, w: 900, h: 100, size: 32, color: NBODY, lh: 1.25 });
  T(s, "[Presenter name] · [Date]", { x: 128, y: 976, w: 900, h: 40, color: NMUTED, valign: "middle" });
  T(s, "Draft for discussion", { x: 1292, y: 976, w: 500, h: 40, color: NMUTED, align: "right", valign: "middle" });
  s.addNotes("Open with purpose, not technology. This group is here because the people who run branches, coordinate care and see patients every day are the best judges of whether a tool will actually help. The graphic is a grid of visit slots: capacity filled deliberately, with room held open for the next patient.");

  // 2 Purpose
  s = pres.addSlide({ masterName: "Compassus · Light" });
  s.addText("WHY WE'RE HERE", { placeholder: "eyebrow" });
  s.addText(" ", { placeholder: "title" });
  s.addText([
    { text: "Give every branch ", options: {} }, { text: "the clarity to grow.", options: { color: GOLD_D, breakLine: true } },
    { text: "Give PCCs ", options: {} }, { text: "time back", options: { color: GOLD_D } }, { text: " for the work only they can do.", options: { breakLine: true } },
    { text: "Give clinicians ", options: {} }, { text: "an easier start", options: { color: GOLD_D } }, { text: " to every day.", options: {} },
  ], { x: P(128), y: P(250), w: P(1560), h: P(460), fontFace: HEAD, fontSize: 38, color: NAVY, margin: 0, valign: "middle", lineSpacingMultiple: 1.1, paraSpaceAfter: 10, isTextBox: true });
  L(s, 128, 760, 1664, RULE2);
  T(s, "This initiative improves how capacity is managed and visits are scheduled, in the branch and in the field, through automation, clear visuals and practical recommendations.", { x: 128, y: 790, w: 1300, h: 110, size: 32, color: BODY, lh: 1.2 });
  s.addNotes("This is the whole initiative in three sentences. Keep the language on capacity, growth and time back. Branches get the data to manage capacity and grow. PCCs get relief from redundant scheduling steps so they can work at the top of their skills. Clinicians spend less of each day confirming and arranging visits.");

  // 3 Goals
  s = pres.addSlide({ masterName: "Compassus · Light" });
  head(s, "Our goals", "What we set out to improve");
  [["For branches", "See capacity clearly. Grow with confidence.", ["Capacity by discipline and territory, at a glance", "Data to accept referrals with confidence", "Early signals before gaps become missed visits"]],
   ["For PCCs", "Work at the top of their skills.", ["Automation for repetitive, redundant steps", "Visuals and recommendations in one place", "More time for patients, clinicians and care"]],
   ["For clinicians", "Less time arranging. More time caring.", ["Fewer daily calls to confirm and schedule", "Schedules that respect flexibility", "The reasoning behind every request"]]].forEach(([lab, h, items], i) => {
    const x = 128 + i * 565;
    R(s, { x, y: 322, w: 533, h: 560, fill: CARD, line: RULE });
    T(s, lab.toUpperCase(), { x: x + 48, y: 370, w: 437, h: 34, color: GOLD_D, bold: true, cs: 1.5 });
    T(s, h, { x: x + 48, y: 420, w: 437, h: 150, size: 40, font: HEAD, lh: 1.05 });
    L(s, x + 48, 590, 437, RULE);
    bullets(s, items, { x: x + 48, y: 614, w: 437, h: 240 });
  });
  s.addNotes("Three groups, one aim. For branches: visibility and data to manage capacity and drive growth. For PCCs: automation, visuals and recommendations that remove redundant steps. For clinicians: less of the daily back-and-forth of confirming and scheduling visits.");

  // 4 Principles
  s = pres.addSlide({ masterName: "Compassus · Navy" });
  head(s, "Our principles", "What guides every decision");
  [["People decide. Tools assist.", "Recommendations inform the branch's judgment. They never replace it."],
   ["Always show the why.", "Every recommendation explains its reasoning, so it can be trusted or challenged."],
   ["Protect flexibility.", "Autonomy is why clinicians choose home health. We design around it."],
   ["Capacity before scheduling.", "Get the picture right first, then automate on a foundation people trust."]].forEach(([h, p], i) => {
    const x = 128 + (i % 2) * 864, y = 340 + Math.floor(i / 2) * 270;
    L(s, x, y, 800, GOLD, 1.5);
    T(s, h, { x, y: y + 32, w: 800, h: 60, size: 44, font: HEAD, color: PAPER });
    T(s, p, { x, y: y + 104, w: 800, h: 100, size: 28, color: NBODY, lh: 1.2 });
  });
  s.addNotes("These four principles are the filter for every vendor and every design choice. Local knowledge and judgment stay in the branch. Any tool we choose must be transparent, must respect how clinicians work, and must get capacity right before it tries to automate scheduling.");

  // 5 Lessons
  s = pres.addSlide({ masterName: "Compassus · Light" });
  head(s, "Due diligence", "Learning from what came before");
  T(s, "Earlier efforts showed us the technology is rarely the hard part. Fit, trust and adoption are.", { x: 128, y: 330, w: 520, h: 320, size: 44, font: HEAD, lh: 1.1 });
  const hdr = (t) => ({ text: t, options: { bold: true, color: GOLD_D } });
  s.addTable([[hdr("What we learned"), hdr("What we are doing differently")],
    ["Tools were set up to mirror old manual habits", "Mapping how our best branches actually work, first"],
    ["Scheduling was automated before capacity was clear", "Capacity visibility comes before automation"],
    ["Adoption was treated as a rollout step", "Adoption is designed in from day one, with the field"],
    ["Pilots lacked the room and measures to prove out", "A defined pilot, clear measures and honest readouts"]].map((r, i) => i ? r.map((t) => ({ text: t })) : r),
    { x: P(728), y: P(322), w: P(1064), colW: [P(532), P(532)], fontFace: TEXT, fontSize: 13, color: NAVY, border: { type: "solid", pt: 0.75, color: RULE2 }, margin: 0.12, valign: "middle", rowH: P(96) });
  s.addNotes("Acknowledge prior efforts directly and respectfully. The earlier scheduling pilot did not fall short because of the technology; it was configured to mirror existing manual habits, and it never had the conditions to prove itself. That is why this effort starts with capacity, involves the field from the start, and pilots with clear measures.");

  // 6 Diligence
  s = pres.addSlide({ masterName: "Compassus · Light" });
  head(s, "Due diligence", "Our path to a decision");
  [["Complete", "01", "Listen", "Discovery sessions with branch leaders, PCCs and clinicians"],
   ["Complete", "02", "Map", "Current-state workflows, pain points and constraints"],
   ["Under way", "03", "Shortlist", "RFP narrowed the field to six; three advance on-site"],
   ["Next · with you", "04", "Assess", "On-site in Nashville, Oct 21–23, with our SMEs"],
   ["Ahead", "05", "Select, then pilot", "Two finalists, then a pilot led by pilot-branch SMEs"]].forEach(([st, n, h, p], i) => {
    const x = 128 + i * 337.6, hot = i === 3;
    R(s, { x, y: 322, w: 313, h: 440, fill: hot ? NAVY : CARD, line: hot ? NAVY : i === 4 ? RULE2 : RULE, dash: i === 4 ? "dash" : "solid" });
    T(s, st, { x: x + 32, y: 354, w: 250, h: 34, color: hot ? GOLD : MUTED, bold: true });
    T(s, n, { x: x + 32, y: 400, w: 250, h: 70, size: 64, font: HEAD, color: hot ? GOLD : GOLD_D });
    T(s, h, { x: x + 32, y: 484, w: 250, h: 80, size: 32, bold: true, color: hot ? PAPER : NAVY });
    T(s, p, { x: x + 32, y: 572, w: 250, h: 170, size: 24, color: hot ? NBODY : BODY, lh: 1.2 });
  });
  T(s, "No decision is made on a demo alone.", { x: 128, y: 812, w: 1664, h: 60, size: 40, font: HEAD });
  s.addNotes("Walk the path left to right. We have listened and mapped the current state across the branch and the field. The RFP narrowed the field to six, and three advance to on-site sessions in Nashville. That is where this group comes in. Two finalists then move to contract negotiations, and nothing moves forward at scale without a measured pilot, guided by a second group of SMEs from the pilot branches.");

  // 7A Timeline — Gantt
  s = pres.addSlide({ masterName: "Compassus · Light" });
  head(s, "The timeline · Option A", "From concept to pilot");
  R(s, { x: 1068, y: 300, w: 724, h: 556, fill: TINT });
  [[1, NAVY, "Complete", 1440], [2, GOLD, "Ahead", 1640]].forEach(([_, c, t, x]) => { R(s, { x, y: 228, w: 32, h: 14, fill: c, radius: 0.05 }); T(s, t, { x: x + 44, y: 218, w: 140, h: 34, color: BODY }); });
  [368, 668, 868, 1068, 1430].forEach((x) => s.addShape(pres.shapes.LINE, { x: P(x), y: P(300), w: 0, h: P(556), line: { color: RULE, width: 0.75 } }));
  L(s, 128, 350, 1664, RULE2);
  [["Q3 2026", 128], ["Oct 2026", 384], ["Nov", 684], ["Dec", 884], ["Q1 2027", 1084], ["Q2 2027", 1446]].forEach(([t, x]) => T(s, t, { x, y: 310, w: 230, h: 34, color: MUTED, bold: true }));
  const bar = (label, lx, ly, bx, bw, c, bold) => { T(s, label, { x: lx, y: ly, w: 700, h: 34, bold }); if (bw) R(s, { x: bx, y: ly + 36, w: bw, h: 14, fill: c, radius: 0.05 }); };
  bar("Initiative conceptualization", 128, 362, 128, 110, NAVY);
  bar("Vendor identification", 190, 424, 190, 140, NAVY);
  bar("RFP narrows the field to six", 290, 486, 290, 78, NAVY);
  bar("Six narrowed to three for on-site", 368, 548, 372, 150, GOLD);
  s.addShape(pres.shapes.DIAMOND, { x: P(560), y: P(612), w: P(36), h: P(36), fill: { color: GOLD }, line: { type: "none" } });
  T(s, "On-site in Nashville · Wed–Fri, Oct 21–23", { x: 612, y: 612, w: 760, h: 36, bold: true, valign: "middle" });
  bar("Narrow to two finalists · 1–2 weeks", 600, 672, 600, 110, GOLD);
  bar("Contract negotiations", 710, 734, 710, 158, GOLD);
  bar("Product scoping & pilot site identification", 672, 796, 672, 396, GOLD);
  R(s, { x: 368, y: 868, w: 496, h: 3, fill: NAVY });
  T(s, "Selection-phase SMEs · this group", { x: 368, y: 878, w: 496, h: 34, bold: true });
  L(s, 876, 869, 916, GOLD_D, 2, "dash");
  T(s, "Pilot-branch SMEs · named as pilot sites are identified", { x: 876, y: 878, w: 916, h: 34, bold: true, color: GOLD_D });
  s.addNotes("Option A, a Gantt view. Conceptualization, vendor identification and the RFP are behind us. Six narrow to three for on-site sessions in Nashville, Wednesday through Friday, October 21 to 23. Within one to two weeks we narrow to two finalists; contract negotiations run through November, alongside product scoping and pilot site identification through December. The shaded space across Q1 and Q2 2027 is for pilot milestones, led by a second group of pilot-branch SMEs.");

  // 7B Timeline — milestone road
  s = pres.addSlide({ masterName: "Compassus · Navy" });
  head(s, "The timeline · Option B", "The road to a pilot");
  R(s, { x: 128, y: 438, w: 1664, h: 2, fill: NLINE });
  R(s, { x: 128, y: 438, w: 480, h: 2, fill: NBODY });
  const stops = [["Q3 2026", "Complete", "Conceptualize", "Goals, discovery and current-state mapping", 128, "done"],
    ["Aug–Sep", "Complete", "Identify & RFP", "Vendors identified; the RFP narrows the field to six", 368, "done"],
    ["October", "Up next", "Shortlist & on-site", "Three finalists on-site in Nashville, Wed–Fri, Oct 21–23", 608, "now"],
    ["November", "Ahead", "Select & contract", "Two finalists within 1–2 weeks; negotiations in November", 848, "ahead"],
    ["Nov–Dec", "Ahead", "Scope & site", "Product scoping and pilot site identification", 1088, "ahead"]];
  stops.forEach(([d, st, h, p, x, k]) => {
    T(s, d, { x, y: 322, w: 224, h: 34, bold: true, color: GOLD });
    T(s, st, { x, y: 358, w: 224, h: 34, bold: k === "now", color: k === "now" ? PAPER : NMUTED });
    if (k === "now") s.addShape(pres.shapes.OVAL, { x: P(600), y: P(415), w: P(48), h: P(48), fill: { color: GOLD }, line: { type: "none" } });
    else s.addShape(pres.shapes.OVAL, { x: P(x), y: P(423), w: P(32), h: P(32), fill: { color: k === "done" ? NBODY : NAVY }, line: k === "done" ? { type: "none" } : { color: GOLD, width: 1.5 } });
    T(s, h, { x, y: 480, w: 224, h: 76, size: 32, font: HEAD, color: PAPER });
    T(s, p, { x, y: 568, w: 220, h: 170, color: NBODY, lh: 1.2 });
  });
  T(s, "Q1–Q2 2027", { x: 1328, y: 322, w: 464, h: 34, bold: true, color: GOLD });
  T(s, "Ahead", { x: 1328, y: 358, w: 464, h: 34, color: NMUTED });
  s.addShape(pres.shapes.OVAL, { x: P(1328), y: P(423), w: P(32), h: P(32), fill: { color: NAVY }, line: { color: GOLD, width: 1.5, dashType: "dash" } });
  R(s, { x: 1328, y: 480, w: 464, h: 280, line: NLINE, lw: 1.5, dash: "dash" });
  T(s, "Pilot", { x: 1360, y: 500, w: 400, h: 44, size: 32, font: HEAD, color: PAPER });
  T(s, "[Add pilot milestones]", { x: 1360, y: 552, w: 400, h: 34, color: NMUTED });
  R(s, { x: 608, y: 800, w: 464, h: 56, fill: NAVY2 });
  T(s, "Selection-phase SMEs · this group", { x: 632, y: 800, w: 430, h: 56, bold: true, color: PAPER, valign: "middle" });
  R(s, { x: 1088, y: 800, w: 704, h: 56, line: GOLD, lw: 1.5, dash: "dash" });
  T(s, "Pilot-branch SMEs · named as sites are identified", { x: 1112, y: 800, w: 670, h: 56, bold: true, color: GOLD, valign: "middle" });
  s.addNotes("Option B, a milestone road. Read left to right: two stages complete, the Nashville on-site sessions up next, then selection and contract in November, scoping and pilot site identification through December, and the pilot across the first half of 2027. The bands at the bottom show which group of SMEs leads each stretch.");

  // 7C Timeline — quarter cards
  s = pres.addSlide({ masterName: "Compassus · Light" });
  head(s, "The timeline · Option C", "Quarter by quarter");
  R(s, { x: 128, y: 306, w: 316, h: 590, fill: CARD, line: RULE });
  T(s, "Q3 2026 · DONE", { x: 160, y: 338, w: 260, h: 34, bold: true, color: MUTED, cs: 1.5 });
  bullets(s, ["Initiative conceptualization", "Vendor identification", "RFP narrows the field to six"], { x: 160, y: 392, w: 252, h: 300 });
  R(s, { x: 460, y: 306, w: 668, h: 590, fill: NAVY });
  T(s, "Q4 2026 · NOW", { x: 492, y: 338, w: 600, h: 34, bold: true, color: GOLD, cs: 1.5 });
  const month = (m, y, h, items) => {
    L(s, 492, y, 604, NLINE);
    T(s, m, { x: 492, y: y + 16, w: 72, h: 34, bold: true, color: GOLD });
    s.addText(items.map((t, i) => ({ text: t.text || t, options: { bullet: { indent: 14 }, breakLine: i < items.length - 1, bold: !!t.text, color: t.text ? PAPER : NBODY } })),
      { x: P(588), y: P(y + 16), w: P(508), h: P(h), fontFace: TEXT, fontSize: 13, margin: 0, valign: "top", paraSpaceAfter: 6, isTextBox: true });
  };
  month("Oct", 392, 170, ["Six narrowed to three", { text: "Nashville on-site · Wed–Fri, Oct 21–23" }, "Narrow to two · 1–2 weeks"]);
  month("Nov", 586, 110, ["Contract negotiations", "Scoping and site identification begin"]);
  month("Dec", 720, 70, ["Product scoping and pilot site identification"]);
  R(s, { x: 492, y: 828, w: 420, h: 44, fill: GOLD });
  T(s, "Selection-phase SMEs · this group", { x: 508, y: 828, w: 400, h: 44, bold: true, valign: "middle" });
  [[1144, "Q1 2027", true], [1476, "Q2 2027", false]].forEach(([x, q, pilot]) => {
    R(s, { x, y: 306, w: 316, h: 590, fill: CARD, line: RULE2, dash: "dash" });
    T(s, q.toUpperCase(), { x: x + 32, y: 338, w: 252, h: 34, bold: true, color: GOLD_D, cs: 1.5 });
    let y = 392;
    if (pilot) { R(s, { x: x + 32, y, w: 252, h: 44, line: GOLD, lw: 1.5, dash: "dash" }); T(s, "Pilot-branch SMEs", { x: x + 44, y, w: 236, h: 44, bold: true, color: GOLD_D, valign: "middle" }); y += 64; }
    for (let k = 0; k < (pilot ? 5 : 6); k++) { y += 64; L(s, x + 32, y, 252, RULE); }
  });
  s.addNotes("Option C, quarter by quarter. Q3 is done. Q4 is where this group works: three finalists on-site in Nashville October 21 to 23, two finalists within one to two weeks, contract negotiations in November, and product scoping and pilot site identification through December. Q1 and Q2 2027 are open for pilot milestones, led by pilot-branch SMEs.");

  // 8 Why SMEs (gold)
  s = pres.addSlide({ masterName: "Compassus · Gold" });
  T(s, "WHY SUBJECT MATTER EXPERTS", { x: 128, y: 128, w: 1664, h: 40, bold: true, cs: 2 });
  s.addText([{ text: "The best judges of a tool are the people who will " }, { text: "use it every day.", options: { bold: true } }],
    { x: P(128), y: P(300), w: P(1500), h: P(360), fontFace: HEAD, fontSize: 48, color: NAVY, margin: 0, valign: "middle", lineSpacingMultiple: 1.05, isTextBox: true });
  T(s, "Vendors will show us what their products can do. Our subject matter experts will tell us whether they work here.", { x: 128, y: 760, w: 1200, h: 110, size: 32, lh: 1.25 });
  s.addNotes("This is the heart of the deck. The people in this room carry knowledge no vendor demo can show: how branches really run, where scheduling breaks, and what earns a clinician's trust. Their role is to make sure Compassus chooses well.");

  // 9 Phases
  s = pres.addSlide({ masterName: "Compassus · Light" });
  head(s, "Who we need, and when", "Two phases, two groups of experts");
  [[128, true, "NOW · SELECTION PHASE", "Vendor selection SMEs", "This group. You assess the three finalists on-site in Nashville and guide the choice to two platforms.", ["On-site assessments, Oct 21–23", "One shared scorecard and debrief", "Input to the recommendation"]],
   [1048, false, "NEXT · PILOT PHASE", "Pilot-branch SMEs", "A second group, drawn from the branches chosen to pilot one of the two selected platforms.", ["Named once pilot branches are set", "Shape setup and workflows locally", "Lead adoption with their teams"]]].forEach(([x, now, eb, h, p, items]) => {
    R(s, { x, y: 322, w: 744, h: 560, fill: now ? NAVY : CARD, line: now ? NAVY : RULE2, lw: now ? 0.75 : 1.5, dash: now ? "solid" : "dash" });
    T(s, eb, { x: x + 56, y: 378, w: 632, h: 34, bold: true, color: now ? GOLD : GOLD_D, cs: 1.5 });
    T(s, h, { x: x + 56, y: 432, w: 632, h: 64, size: 48, font: HEAD, color: now ? PAPER : NAVY });
    T(s, p, { x: x + 56, y: 516, w: 632, h: 130, size: 28, color: now ? NBODY : BODY, lh: 1.2 });
    bullets(s, items, { x: x + 56, y: 670, w: 632, h: 180, color: now ? PAPER : BODY });
  });
  s.addShape(pres.shapes.RIGHT_ARROW, { x: P(912), y: P(578), w: P(96), h: P(48), fill: { color: GOLD }, line: { type: "none" } });
  s.addNotes("Be clear about scope. This group is here for vendor identification and selection. Once pilot branches are identified, a second group of SMEs from those locations will guide the pilot of one of the two selected platforms. What this group learns is handed forward, so the pilot team starts with the full picture.");

  // 10 Roles
  s = pres.addSlide({ masterName: "Compassus · Light" });
  head(s, "Selection phase · draft roster", "Who is at the table");
  [["Branch Executive Director", "Growth, staffing model and the economics of saying yes"], ["Director of Clinical Services", "Clinical judgment, start-of-care assignment and compliance"], ["Patient Care Coordinator", "The daily scheduling workflow, and exactly where it breaks"],
   ["Field RN / Start-of-Care Nurse", "What earns a clinician's yes, and what a tool must never do"], ["Therapy Lead (PT / OT)", "Discipline mix, visit frequency and continuity of care"], ["Workforce & Staffing", "Capacity models, flex coverage and per-diem engagement"]].forEach(([h, p], i) => {
    const x = 128 + (i % 3) * 565, y = 314 + Math.floor(i / 3) * 284;
    R(s, { x, y, w: 533, h: 260, fill: CARD, line: RULE });
    T(s, h, { x: x + 40, y: y + 32, w: 453, h: 90, size: 36, font: HEAD, lh: 1.05 });
    T(s, p, { x: x + 40, y: y + 130, w: 453, h: 110, size: 26, color: BODY, lh: 1.2 });
  });
  s.addNotes("Each perspective sees a different layer of capacity: the staffing model, clinical operations, the daily schedule and the clinician's day. Together they cover the full picture. Roster is a draft; confirm roles before presenting.");

  // 11 Meet
  s = pres.addSlide({ masterName: "Compassus · Light" });
  head(s, "Selection phase", "Meet our selection-phase experts");
  for (let i = 0; i < 6; i++) {
    const x = 128 + (i % 3) * 565, y = 322 + Math.floor(i / 3) * 268;
    R(s, { x, y, w: 533, h: 240, fill: CARD, line: RULE });
    s.addShape(pres.shapes.OVAL, { x: P(x + 32), y: P(y + 32), w: P(112), h: P(112), fill: { color: RULE }, line: { type: "none" } });
    T(s, "[Name]", { x: x + 168, y: y + 32, w: 333, h: 44, size: 32, font: HEAD });
    T(s, "[Title]", { x: x + 168, y: y + 82, w: 333, h: 34, bold: true });
    T(s, "[Branch · Market]", { x: x + 168, y: y + 118, w: 333, h: 34, color: MUTED });
    T(s, "[What they bring]", { x: x + 168, y: y + 154, w: 333, h: 64, color: BODY, italic: true });
  }
  s.addNotes("Introduce each expert by name, role and years in home health, and say in one line what they bring to the assessment. Replace the circles with headshots if available.");

  // 12 On-site
  s = pres.addSlide({ masterName: "Compassus · Navy" });
  head(s, "On-site · Nashville · Oct 21–23", "What our experts will do");
  [["01", "Bring real scenarios", "Test each product on situations our branches face every week, not a scripted demo."], ["02", "Score it together", "Rate every vendor on the same shared scorecard, so comparisons are fair."],
   ["03", "Find the edges", "Push on the exceptions: call-outs, authorizations, recerts and weekend coverage."], ["04", "Speak for the field", "Tell us what a tool must always do, and what it must never do."]].forEach(([n, h, p], i) => {
    const x = 128 + (i % 2) * 864, y = 340 + Math.floor(i / 2) * 270;
    L(s, x, y, 800, NLINE);
    T(s, n, { x, y: y + 32, w: 96, h: 70, size: 64, font: HEAD, color: GOLD });
    T(s, h, { x: x + 128, y: y + 32, w: 672, h: 56, size: 40, font: HEAD, color: PAPER });
    T(s, p, { x: x + 128, y: y + 98, w: 672, h: 100, size: 28, color: NBODY, lh: 1.2 });
  });
  s.addNotes("Good scenario prompts: a start-of-care request late on a Friday in a full territory; a clinician calling out at 7 a.m.; a pending authorization holding up a visit. Encourage candor. The most valuable input is often \"this would never work in my branch, and here is why.\"");

  // 13 Criteria
  s = pres.addSlide({ masterName: "Compassus · Light" });
  head(s, "The assessment lens", "How we will judge fit");
  s.addTable([[hdr("What we assess"), hdr("The question our experts will ask")],
    ["Real-world fit", "Does it work the way our branches and field actually work?"], ["Capacity first", "Does it show capacity by discipline and territory before it schedules?"],
    ["Transparency", "Does every recommendation show its reasoning?"], ["Human in control", "Can the branch override easily, and does the tool learn from it?"],
    ["Clinician experience", "Does it reduce daily calls and preserve flexibility?"], ["Integration", "Does it work with HCHB and the systems we already use?"],
    ["Ease of adoption", "Could a PCC use it with confidence after a short orientation?"]].map((r, i) => i ? r.map((t) => ({ text: t })) : r),
    { x: P(128), y: P(322), w: P(1664), colW: [P(500), P(1164)], fontFace: TEXT, fontSize: 13, color: NAVY, border: { type: "solid", pt: 0.75, color: RULE2 }, margin: 0.1, valign: "middle", rowH: P(64) });
  s.addNotes("These criteria mirror the functional scorecard every vendor is rated against. Note that a product that tries to decide where we have said people decide is a poor fit, even if it scores well on features.");

  // 14 Success
  s = pres.addSlide({ masterName: "Compassus · Navy" });
  head(s, "The outcome", "What success looks like");
  [["For a branch leader", "Capacity by discipline and territory in one view, and the confidence to say yes."], ["For a PCC", "A morning spent coordinating care, not re-entering the same data in several places."],
   ["For a clinician", "A day that starts confirmed, with fewer calls to make before the first visit."], ["For a patient", "A visit window they can count on, from a clinician they know."]].forEach(([l, p], i) => {
    const x = 128 + (i % 2) * 864, y = 340 + Math.floor(i / 2) * 270;
    L(s, x, y, 800, NLINE);
    T(s, l.toUpperCase(), { x, y: y + 32, w: 800, h: 34, bold: true, color: GOLD, cs: 1.5 });
    T(s, p, { x, y: y + 82, w: 800, h: 140, size: 40, font: HEAD, color: PAPER, lh: 1.1 });
  });
  s.addNotes("Success is described in human terms on purpose. Measures will be set with the pilot design, and our experts will help define what good looks like in their own branches.");

  // 15 Next
  s = pres.addSlide({ masterName: "Compassus · Light" });
  head(s, "Next steps", "What happens next");
  [["Before Oct 21", "SME orientation and scenario prep"], ["Oct 21–23", "On-site vendor assessments in Nashville"], ["Late Oct", "SME debrief and scorecard review"], ["Early Nov", "Two finalists advance to contract negotiations"]].forEach(([d, h], i) => {
    const y = 322 + i * 110;
    L(s, 128, y, 964, RULE2);
    T(s, d, { x: 128, y: y + 28, w: 200, h: 40, bold: true, color: GOLD_D });
    T(s, h, { x: 368, y: y + 24, w: 724, h: 80, size: 32 });
  });
  L(s, 128, 762, 964, RULE2);
  R(s, { x: 1172, y: 322, w: 620, h: 440, fill: CARD, line: RULE });
  T(s, "What we ask of you", { x: 1220, y: 370, w: 524, h: 56, size: 40, font: HEAD });
  bullets(s, ["Wed–Fri, Oct 21–23 in Nashville, plus prep and debrief", "Real examples from your branch or caseload", "Candor, especially when something won't work", "Discretion while evaluations are underway"], { x: 1220, y: 450, w: 524, h: 290 });
  s.addNotes("Narrowing to two takes one to two weeks after the on-site sessions. This group's role concludes with the selection; pilot-branch SMEs pick up from there. Discretion matters because vendor conversations are commercially sensitive.");

  // 16 Close
  s = pres.addSlide({ masterName: "Compassus · Navy plain" });
  s.addText([{ text: "Your experience shapes ", options: { color: PAPER } }, { text: "this decision.", options: { color: GOLD } }],
    { x: P(128), y: P(330), w: P(1400), h: P(260), fontFace: HEAD, fontSize: 56, margin: 0, valign: "bottom", lineSpacingMultiple: 0.95, isTextBox: true });
  T(s, "Thank you for lending it.", { x: 128, y: 630, w: 1200, h: 50, size: 32, color: NBODY });
  s.addImage({ path: LOGO_R, x: P(1532), y: P(916), w: P(260), h: P(100) });
  T(s, "[Initiative lead] · [Email]", { x: 128, y: 976, w: 1000, h: 40, color: NMUTED, valign: "middle" });
  s.addNotes("Close by thanking the group and opening the floor. Invite questions and concerns now, and share how to reach the initiative team afterward.");

  // ---------- blank branded slides for building ----------
  const fill = (master, vals) => { const sl = pres.addSlide({ masterName: master }); Object.entries(vals).forEach(([k, v]) => sl.addText(v, { placeholder: k })); sl.addNotes("Template slide. Replace the sample text, or delete this slide. More slides like it: Home > New Slide > choose a Compassus layout."); };
  fill("Compassus · Section divider", { eyebrow: "SECTION LABEL", title: "Section title", sub: "One line that sets up the section" });
  fill("Compassus · Light + body", { eyebrow: "EYEBROW LABEL", title: "Slide title", body: "Add your content here." });
  fill("Compassus · Light two columns", { eyebrow: "EYEBROW LABEL", title: "Slide title", left: "Left column content", right: "Right column content" });
  fill("Compassus · Light three cards", { eyebrow: "EYEBROW LABEL", title: "Slide title", card1: "Card one content", card2: "Card two content", card3: "Card three content" });
  fill("Compassus · Navy + body", { eyebrow: "EYEBROW LABEL", title: "Slide title", body: "Add your content here." });
  fill("Compassus · Gold statement", { eyebrow: "EYEBROW LABEL", title: "A single statement worth a whole slide." });
  fill("Compassus · Light", { eyebrow: "EYEBROW LABEL", title: "Slide title (open canvas)" });

  await pres.writeFile({ fileName: "Compassus-SME-Introduction.pptx" });
  console.log("written");
}
main().catch((e) => { console.error(e); process.exit(1); });
