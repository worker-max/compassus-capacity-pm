const fs = require("fs");
const {
  Document, Packer, Paragraph, TextRun, HeadingLevel, AlignmentType,
  BorderStyle, PageOrientation, convertInchesToTwip,
} = require("docx");

const C = JSON.parse(fs.readFileSync("content.json", "utf8"));

const INK = "1F2A37", MUTED = "5B6572", BAND = "1F3B57", QUOTE = "3A4652";

const quoteBorder = {
  left: { style: BorderStyle.SINGLE, size: 18, space: 12, color: "C7B37A" },
};

// Evan's words, verbatim: bordered, indented, and visually distinct from our reply.
const quote = (t, last) => new Paragraph({
  children: [new TextRun({ text: t, italics: true, color: QUOTE, size: 21, font: "Calibri" })],
  border: quoteBorder,
  indent: { left: convertInchesToTwip(0.22) },
  spacing: { before: 60, after: last ? 140 : 60, line: 264 },
});

const reply = (t, first) => new Paragraph({
  children: [
    ...(first ? [new TextRun({ text: "Our response.  ", bold: true, color: BAND, size: 21, font: "Calibri" })] : []),
    new TextRun({ text: t, color: INK, size: 21, font: "Calibri" }),
  ],
  spacing: { before: first ? 0 : 100, after: 100, line: 276 },
  indent: { left: convertInchesToTwip(0.22) },
});

const rule = () => new Paragraph({
  text: "",
  border: { bottom: { style: BorderStyle.SINGLE, size: 6, space: 10, color: "DDE1E6" } },
  spacing: { before: 160, after: 160 },
});

const bullet = (t) => new Paragraph({
  children: [new TextRun({ text: t, color: INK, size: 21, font: "Calibri" })],
  bullet: { level: 0 },
  spacing: { before: 60, after: 60, line: 276 },
});

const kids = [];

kids.push(new Paragraph({
  children: [new TextRun({ text: "COMPASSUS HOME HEALTH", bold: true, color: MUTED, size: 17, font: "Calibri" })],
  spacing: { after: 60 },
}));
kids.push(new Paragraph({
  children: [new TextRun({ text: C.title, bold: true, color: INK, size: 40, font: "Calibri Light" })],
  spacing: { after: 60 },
}));
kids.push(new Paragraph({
  children: [new TextRun({ text: C.subtitle, color: MUTED, size: 21, font: "Calibri" })],
  border: { bottom: { style: BorderStyle.SINGLE, size: 8, space: 12, color: BAND } },
  spacing: { after: 200 },
}));
kids.push(new Paragraph({
  children: [new TextRun({ text: C.intro, color: INK, size: 21, font: "Calibri" })],
  spacing: { after: 240, line: 276 },
}));

for (const sec of C.sections) {
  kids.push(new Paragraph({
    heading: HeadingLevel.HEADING_1,
    children: [new TextRun({ text: sec.h, bold: true, color: BAND, size: 26, font: "Calibri" })],
    spacing: { before: 260, after: 140 },
  }));
  sec.items.forEach((it, i) => {
    it.q.forEach((q, j) => kids.push(quote(q, j === it.q.length - 1)));
    it.a.forEach((a, j) => kids.push(reply(a, j === 0)));
    if (i < sec.items.length - 1) kids.push(rule());
  });
}

kids.push(new Paragraph({
  heading: HeadingLevel.HEADING_1,
  children: [new TextRun({ text: "Also changed, not from the list", bold: true, color: BAND, size: 26, font: "Calibri" })],
  spacing: { before: 320, after: 140 },
}));
C.changed.forEach((t) => kids.push(bullet(t)));

kids.push(new Paragraph({
  heading: HeadingLevel.HEADING_1,
  children: [new TextRun({ text: "Open for the meeting", bold: true, color: BAND, size: 26, font: "Calibri" })],
  spacing: { before: 320, after: 140 },
}));
C.open.forEach((t) => kids.push(bullet(t)));

const doc = new Document({
  styles: { default: { document: { run: { font: "Calibri", size: 21, color: INK } } } },
  sections: [{
    properties: {
      page: {
        size: { width: 12240, height: 15840, orientation: PageOrientation.PORTRAIT },
        margin: {
          top: convertInchesToTwip(0.85), bottom: convertInchesToTwip(0.85),
          left: convertInchesToTwip(1.0), right: convertInchesToTwip(1.0),
        },
      },
    },
    children: kids,
  }],
});

Packer.toBuffer(doc).then((b) => {
  fs.writeFileSync("Capacity-Scheduling-Feedback-Response.docx", b);
  console.log("wrote Capacity-Scheduling-Feedback-Response.docx");
});
