// Compassus — Message Frame slide (single-slide .pptx, same master as the SME deck)
const pptxgen = require("pptxgenjs");

const NAVY = "002554", GOLD = "CE8E00", GOLD_D = "8A5F00", PAPER = "F8F6F1",
  BODY = "3D4A5C", MUTED = "5A6472", NBODY = "C9D3E0";
const HEAD = "Maven Pro", TEXT = "Arial";
const P = (v) => v / 144, S = (v) => v / 2;
const FOOT = "Capacity & Scheduling · SME Introduction";

const pres = new pptxgen();
pres.layout = "LAYOUT_WIDE";
pres.title = "Message Frame — Our Key Words";
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
s.addText("MESSAGE FRAME", { placeholder: "eyebrow" });
s.addText("Our key words", { placeholder: "title" });

const T = (text, o) => s.addText(text, { x: P(o.x), y: P(o.y), w: P(o.w), h: P(o.h), fontFace: o.font || TEXT, fontSize: S(o.size || 24), color: o.color || NAVY, bold: !!o.bold, margin: 0, valign: o.valign || "top", align: o.align || "left", charSpacing: o.cs, isTextBox: true });
const bullets = (items, o) => s.addText(items.map((t, i) => ({ text: t, options: { bullet: { indent: 14 }, breakLine: i < items.length - 1 } })),
  { x: P(o.x), y: P(o.y), w: P(o.w), h: P(o.h), fontFace: TEXT, fontSize: 13, color: BODY, margin: 0, valign: o.valign || "middle", align: o.align || "left", paraSpaceAfter: 6, isTextBox: true });

// box geometry (canvas px)
const BW = 380, BH = 210, XL = 540, XR = 1000, YT = 330, YB = 640;
const box = (x, y, n, word, label) => {
  s.addShape(pres.shapes.RECTANGLE, { x: P(x), y: P(y), w: P(BW), h: P(BH), fill: { color: NAVY }, line: { type: "none" } });
  T(`${n}  ·  ${label.toUpperCase()}`, { x: x + 32, y: y + 32, w: BW - 64, h: 34, color: GOLD, bold: true, cs: 1.5 });
  T(word, { x: x + 32, y: y + 82, w: BW - 64, h: 96, size: 52, font: HEAD, color: PAPER, valign: "middle" });
};
box(XL, YB, "1", "Fragmented", "Problem");
box(XL, YT, "2", "Visibility", "Solution");
box(XR, YT, "3", "Field-led", "Approach");
box(XR, YB, "4", "Growth", "Result");

// arrows: Problem -> Solution -> Approach -> Result
const arrow = (x, y, w, h) => s.addShape(pres.shapes.LINE, { x: P(x), y: P(y), w: P(w), h: P(h), line: { color: GOLD, width: 2, endArrowType: "triangle" }, flipV: h < 0 && false });
s.addShape(pres.shapes.LINE, { x: P(XL + BW / 2), y: P(YT + BH + 6), w: 0, h: P(YB - YT - BH - 12), line: { color: GOLD, width: 2, beginArrowType: "triangle" } });
arrow(XL + BW + 6, YT + BH / 2, XR - XL - BW - 12, 0);
arrow(XR + BW / 2, YT + BH + 6, 0, YB - YT - BH - 12);

// supporting points
bullets(["Capacity lives in spreadsheets, systems and memory", "PCCs re-key the same data across tools"], { x: 128, y: YB, w: 370, h: BH, align: "left" });
bullets(["Capacity by discipline and territory in one view", "Automation and recommendations that show their reasoning"], { x: 128, y: YT, w: 370, h: BH });
bullets(["SMEs test vendors on real scenarios", "Capacity first, then a measured pilot"], { x: XR + BW + 40, y: YT, w: 1792 - (XR + BW + 40), h: BH });
bullets(["Branches say yes to referrals with confidence", "PCCs and clinicians get time back every day"], { x: XR + BW + 40, y: YB, w: 1792 - (XR + BW + 40), h: BH });

s.addNotes("Read the frame in order: 1 Problem, 2 Solution, 3 Approach, 4 Result. Problem: capacity information is fragmented across spreadsheets, systems and individual memory, and PCCs and clinicians absorb the cost. Solution: one clear view of capacity, with automation and recommendations that explain themselves. Approach: field-led, with our SMEs testing vendors on real scenarios, capacity first, then a measured pilot. Result: growth, as branches accept referrals with confidence and people get time back for the work that matters.");

pres.writeFile({ fileName: "Compassus-Message-Frame.pptx" }).then(() => console.log("written"));
