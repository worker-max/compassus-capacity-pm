// Compassus — Three pillars & primary variables (single-slide .pptx, same master as the SME deck)
const pptxgen = require("pptxgenjs");

const NAVY = "002554", GOLD = "CE8E00", GOLD_D = "8A5F00", PAPER = "F8F6F1", CARD = "FDFCFA",
  RULE = "E3DED3", BODY = "3D4A5C", MUTED = "5A6472", NBODY = "C9D3E0";
const HEAD = "Maven Pro", TEXT = "Arial";
const P = (v) => v / 144;
const FOOT = "Capacity & Scheduling · SME Introduction";

const pres = new pptxgen();
pres.layout = "LAYOUT_WIDE";
pres.title = "Three pillars — primary variables";
pres.defineSlideMaster({
  title: "Compassus · Light", background: { color: PAPER },
  objects: [
    { image: { path: "compassus-logo-color.png", x: P(128), y: P(976), w: P(104), h: P(40) } },
    { text: { text: FOOT, options: { x: P(256), y: P(976), w: P(900), h: P(40), fontFace: TEXT, fontSize: 12, color: MUTED, margin: 0, valign: "middle" } } },
    { placeholder: { options: { name: "eyebrow", type: "body", x: P(128), y: P(128), w: P(1664), h: P(40), fontFace: TEXT, fontSize: 12, bold: true, color: GOLD_D, charSpacing: 2, margin: 0, valign: "top" }, text: "EYEBROW LABEL" } },
    { placeholder: { options: { name: "title", type: "title", x: P(128), y: P(176), w: P(1664), h: P(100), fontFace: HEAD, fontSize: 40, color: NAVY, margin: 0, valign: "top", align: "left" }, text: "Slide title" } },
  ],
  slideNumber: { x: P(1592), y: P(976), w: P(200), h: P(40), fontFace: TEXT, fontSize: 12, color: MUTED, align: "right", valign: "middle" },
});

const s = pres.addSlide({ masterName: "Compassus · Light" });
s.addText("THE THREE PILLARS", { placeholder: "eyebrow" });
s.addText("What each pillar has to get right", { placeholder: "title" });

const T = (text, o) => s.addText(text, { x: P(o.x), y: P(o.y), w: P(o.w), h: P(o.h), fontFace: o.font || TEXT, fontSize: o.pt, color: o.color || NAVY, bold: !!o.bold, margin: 0, valign: o.valign || "top", align: o.align || "left", charSpacing: o.cs, isTextBox: true });

const pillars = [
  { n: "1", name: "Capacity Management", q: "How much care can we take on, by discipline and territory?", vars: [
    ["Clinicians by discipline", "C-01"],
    ["Territory (county & zip)", "C-02 · C-03"],
    ["Time off & availability", "SH-05"],
    ["Productivity points", "SH-07 · 08"],
    ["Open capacity, day & week", "C-06 · C-07"],
    ["Per-diem & flex capacity", "C-09"],
    ["Referrals & discharges", "SH-09"] ] },
  { n: "2", name: "Scheduling", q: "Who sees which patient, when, and in what order?", vars: [
    ["Visit frequency windows", "S-01 · S-03"],
    ["SOC & recert windows", "S-35 · S-36"],
    ["Insurance authorization", "new"],
    ["Discipline & skill match", "S-15 · S-16"],
    ["Continuity of care", "S-22"],
    ["Route & proximity", "S-17 · S-18"],
    ["Patient & caregiver needs", "S-20 · S-28"] ] },
  { n: "3", name: "Engagement", q: "How do patients and clinicians stay informed and on track?", vars: [
    ["Visit confirmations", "CO-01"],
    ["Reminders & arrival alerts", "CO-02 · 03"],
    ["New-patient welcome call", "CO-04"],
    ["Contact preferences", "CO-05"],
    ["Clinician availability", "CO-06"],
    ["Missed-visit rebooking", "CO-08 · S-38"],
    ["Call-out coverage", "CO-09"] ] },
];

pillars.forEach((p, i) => {
  const x = 128 + i * 565, w = 533, y = 300;
  s.addShape(pres.shapes.RECTANGLE, { x: P(x), y: P(y), w: P(w), h: P(620), fill: { color: CARD }, line: { color: RULE, width: 0.75 } });
  s.addShape(pres.shapes.RECTANGLE, { x: P(x), y: P(y), w: P(w), h: P(176), fill: { color: NAVY }, line: { type: "none" } });
  T(`PILLAR ${p.n}`, { x: x + 36, y: y + 28, w: w - 72, h: 30, pt: 11, bold: true, color: GOLD, cs: 1.5 });
  T(p.name, { x: x + 36, y: y + 60, w: w - 72, h: 50, pt: 22, font: HEAD, color: PAPER, valign: "middle" });
  T(p.q, { x: x + 36, y: y + 112, w: w - 72, h: 52, pt: 11.5, color: NBODY });
  p.vars.forEach(([name, id], k) => {
    const ry = y + 196 + k * 58;
    if (k) s.addShape(pres.shapes.LINE, { x: P(x + 36), y: P(ry - 6), w: P(w - 72), h: 0, line: { color: RULE, width: 0.75 } });
    T(name, { x: x + 36, y: ry, w: w - 72 - 140, h: 46, pt: 13, color: NAVY, valign: "middle" });
    T(id, { x: x + w - 36 - 136, y: ry, w: 136, h: 46, pt: 10, color: MUTED, align: "right", valign: "middle" });
  });
});

s.addNotes("Three pillars, each answering one question. Capacity Management is the supply side: how much care the branch can take on, by discipline and territory. Scheduling is the allocation: who sees which patient, when, and in what order, inside the clinical and payer windows. Engagement keeps patients and clinicians informed and on track, from confirmations to missed-visit recovery. These are the primary variables, not the full list; the full inventory has 76 numbered variables, and the codes on the right trace each line to the vendor scorecard. Insurance authorization is tracked but not yet numbered.");

pres.writeFile({ fileName: "Compassus-Three-Pillars.pptx" }).then(() => console.log("written"));
