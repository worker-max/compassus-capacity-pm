const fs = require("fs");
const {
  Document, Packer, Paragraph, TextRun, HeadingLevel, AlignmentType,
  LevelFormat, BorderStyle, ShadingType,
} = require("docx");

const C = JSON.parse(fs.readFileSync("content.json", "utf8"));
const FONT = "Arial";
const NAVY = "1F3864";

const TITLE = (t, sub) => ([
  new Paragraph({
    spacing: { after: 60 },
    children: [new TextRun({ text: t, font: FONT, size: 40, bold: true, color: NAVY })],
  }),
  new Paragraph({
    spacing: { after: 300 },
    children: [new TextRun({ text: sub, font: FONT, size: 24, color: "595959" })],
  }),
]);

const H1 = (t) => new Paragraph({
  heading: HeadingLevel.HEADING_1,
  spacing: { before: 380, after: 180 },
  children: [new TextRun({ text: t, font: FONT, size: 30, bold: true, color: NAVY })],
});

const LEVER = (num, t) => new Paragraph({
  heading: HeadingLevel.HEADING_2,
  spacing: { before: 360, after: 60 },
  keepNext: true,
  children: [
    new TextRun({ text: `${num}.  `, font: FONT, size: 24, bold: true, color: "9AA3B0" }),
    new TextRun({ text: t, font: FONT, size: 24, bold: true, color: NAVY }),
  ],
});

const SUB = (t) => new Paragraph({
  heading: HeadingLevel.HEADING_3,
  spacing: { before: 260, after: 60 },
  keepNext: true,
  children: [new TextRun({ text: t, font: FONT, size: 21, bold: true, color: NAVY })],
});

const DEF = (t) => new Paragraph({
  spacing: { after: 150 },
  indent: { left: 220 },
  keepNext: true,
  children: [new TextRun({ text: t, font: FONT, size: 21, italics: true, color: "404040" })],
});

const MINI = (t) => new Paragraph({
  spacing: { before: 170, after: 70 },
  keepNext: true,
  children: [new TextRun({
    text: t, font: FONT, size: 19, bold: true, color: "5F6672",
    allCaps: true, characterSpacing: 20,
  })],
});

const P = (t, opts = {}) => new Paragraph({
  spacing: { after: 150 },
  children: [new TextRun({ text: t, font: FONT, size: 21, italics: !!opts.i })],
});

const B = (t, kind) => new Paragraph({
  numbering: { reference: "dot", level: 0 },
  spacing: { after: kind === "condition" ? 130 : 85, before: kind === "condition" ? 110 : 0 },
  shading: kind === "condition"
    ? { type: ShadingType.CLEAR, color: "auto", fill: "FBEFEE" } : undefined,
  children: [new TextRun({
    text: t, font: FONT, size: 21,
    bold: kind === "connect" || kind === "condition",
  })],
});

const RULE = () => new Paragraph({
  spacing: { before: 170, after: 230 },
  border: { bottom: { style: BorderStyle.SINGLE, size: 6, color: "BFBFBF" } },
  children: [new TextRun({ text: "", font: FONT, size: 2 })],
});

// ───────────────────────────────────────────────────────── assemble
const kids = [];
kids.push(...TITLE("Capacity and Scheduling",
  "Value levers and measurement requirements"));

kids.push(P("A discussion document. It contains no figures by design. The first section sets out how this program creates financial value. The second sets out what we would need to request in order to size each item and to track it once underway.", { i: true }));

kids.push(RULE());
kids.push(H1("Why scheduling is a financial system"));
kids.push(P("Five characteristics of this business determine how the levers behave. They are worth establishing before the list, because several of the items below read as counterintuitive without them."));
C.framing.forEach((f) => kids.push(B(f)));

kids.push(RULE());
kids.push(H1("Section one:  value levers"));
C.levers.forEach((l, i) => {
  kids.push(LEVER(i + 1, l.name));
  kids.push(DEF(l.def));
  l.points.forEach((p) => kids.push(B(p.text, p.kind)));
});

kids.push(H1("Identified but not yet quantified"));
kids.push(P("Each of these is credible and deliberately carries no figure, because the data required to value it does not exist today."));
C.future.forEach((l) => {
  kids.push(SUB(l.name));
  kids.push(DEF(l.def));
  l.points.forEach((p) => kids.push(B(p)));
});

kids.push(new Paragraph({
  children: [new TextRun({ text: "", font: FONT })],
  pageBreakBefore: true,
}));

kids.push(H1("Section two:  measurement requirements"));
kids.push(P("Two categories for each lever. Baseline data is required once, to establish current performance and size the opportunity. Ongoing data is what we would monitor thereafter to confirm the result. These are different requests: the first is a one-time extract, the second is a reporting commitment that requires an owner.", { i: true }));

C.data.forEach((d, i) => {
  kids.push(LEVER(i + 1, d.name));
  kids.push(MINI("Baseline"));
  d.baseline.forEach((p) => kids.push(B(p)));
  kids.push(MINI("Ongoing measurement"));
  d.ongoing.forEach((p) => kids.push(B(p)));
});

kids.push(H1("For the items not yet quantified"));
C.futureData.forEach((d) => {
  kids.push(SUB(d.name));
  kids.push(MINI("Baseline"));
  d.baseline.forEach((p) => kids.push(B(p)));
  kids.push(MINI("Ongoing measurement"));
  d.ongoing.forEach((p) => kids.push(B(p)));
});

kids.push(RULE());
kids.push(H1("On the scale of this request"));
C.closing.forEach((t) => kids.push(B(t)));

const doc = new Document({
  numbering: {
    config: [{
      reference: "dot",
      levels: [{
        level: 0,
        format: LevelFormat.BULLET,
        text: "\u2022",
        alignment: AlignmentType.LEFT,
        style: { paragraph: { indent: { left: 470, hanging: 260 } } },
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
