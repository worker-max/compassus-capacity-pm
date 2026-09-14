const fs = require('fs');
const path = require('path');
const D = require('docx');
const {
  Document, Packer, Paragraph, TextRun, HeadingLevel, AlignmentType,
  BorderStyle, PageBreak, PageOrientation, Footer, PageNumber, TabStopType,
  Table, TableRow, TableCell, WidthType, ShadingType,
} = D;

const C = require('./content.js');

const INK   = '16212B';
const ACC   = '1F5C6B';
const GREY  = '6B7680';
const RULE  = 'C9D2D6';
const SERIF = 'Georgia';
const SANS  = 'Calibri';

const P = (o) => new Paragraph(o);
const run = (text, o = {}) => new TextRun(Object.assign({ text }, o));

function rule(space = 200, color = RULE, size = 6) {
  return P({ spacing: { before: space, after: space },
    border: { bottom: { style: BorderStyle.SINGLE, size, color, space: 1 } } });
}

function eyebrow(text, o = {}) {
  return P({ spacing: { after: o.after == null ? 120 : o.after, before: o.before || 0 },
    children: [run(text.toUpperCase(), {
      font: SANS, size: 16, bold: true, color: o.color || ACC, characterSpacing: 60 })] });
}

function h1(text) {
  return P({ heading: HeadingLevel.HEADING_1, spacing: { before: 0, after: 180 },
    children: [run(text, { font: SERIF, size: 40, bold: true, color: INK })] });
}

function h2(text) {
  return P({ heading: HeadingLevel.HEADING_2, spacing: { before: 360, after: 140 },
    children: [run(text, { font: SERIF, size: 26, bold: true, color: INK })] });
}

function body(text, o = {}) {
  return P({ spacing: { after: o.after == null ? 140 : o.after, line: 300 },
    indent: o.indent, alignment: o.alignment,
    children: [run(text, { font: SANS, size: o.size || 21, color: o.color || INK, italics: o.italics })] });
}

// One question block: number + title, the question, and the rationale.
function questionBlock(num, title, question, rationale) {
  const label = String(num).padStart(2, '0');
  return [
    P({ spacing: { before: 340, after: 100 }, keepNext: true, children: [
      run(label, { font: SERIF, size: 24, bold: true, color: ACC }),
      run('   ', { size: 24 }),
      run(title, { font: SERIF, size: 24, bold: true, color: INK }) ] }),
    P({ spacing: { before: 0, after: 130, line: 300 }, keepNext: true,
      indent: { left: 340 },
      border: { left: { style: BorderStyle.SINGLE, size: 14, color: ACC, space: 14 } },
      children: [run(question, { font: SERIF, size: 22, italics: true, color: INK })] }),
    P({ spacing: { before: 0, after: 40 }, keepNext: true, indent: { left: 340 },
      children: [run('WHY WE’RE ASKING', { font: SANS, size: 14, bold: true, color: ACC, characterSpacing: 50 })] }),
    P({ spacing: { after: 220, line: 290 }, indent: { left: 340 },
      children: [run(rationale, { font: SANS, size: 19, color: GREY })] }),
  ];
}

function metaTable(rows) {
  const W = [1900, 7460];
  return new Table({
    columnWidths: W,
    borders: {
      top: { style: BorderStyle.NONE }, bottom: { style: BorderStyle.NONE },
      left: { style: BorderStyle.NONE }, right: { style: BorderStyle.NONE },
      insideHorizontal: { style: BorderStyle.SINGLE, size: 4, color: RULE },
      insideVertical: { style: BorderStyle.NONE },
    },
    rows: rows.map(([k, v]) => new TableRow({ children: [
      new TableCell({ width: { size: W[0], type: WidthType.DXA },
        margins: { top: 90, bottom: 90, right: 120 },
        children: [P({ children: [run(k.toUpperCase(), { font: SANS, size: 15, bold: true, color: ACC, characterSpacing: 40 })] })] }),
      new TableCell({ width: { size: W[1], type: WidthType.DXA },
        margins: { top: 90, bottom: 90 },
        children: [P({ children: [run(v, { font: SANS, size: 19, color: INK })] })] }),
    ] })),
  });
}

const children = [];

/* ---------- Cover ---------- */
children.push(
  P({ spacing: { before: 900, after: 0 },
    children: [run('COMPASSUS  ·  HOME HEALTH', { font: SANS, size: 17, bold: true, color: ACC, characterSpacing: 90 })] }),
  P({ spacing: { before: 260, after: 0 },
    children: [run('Vendor Demo', { font: SERIF, size: 62, bold: true, color: INK })] }),
  P({ spacing: { before: 0, after: 220 },
    children: [run('Question Guide', { font: SERIF, size: 62, bold: true, color: INK })] }),
  P({ spacing: { after: 300 }, children: [run(
    'Capacity & Scheduling Platform — round two', { font: SERIF, size: 26, italics: true, color: GREY })] }),
  rule(0, ACC, 10),
  body('Ten questions asked identically to all six vendors, so the field can be compared on one axis — followed by a set unique to each vendor, built from what their own return left open. A rationale sits under every question so whoever asks it knows why it is there.', { after: 300 }),
  metaTable([
    ['Prepared', '14 September 2026'],
    ['Format', 'Two-hour virtual call, one per vendor'],
    ['Primary ask', 'Operational design walkthrough — referral through day-to-day scheduling'],
    ['Vendors', 'Arya · HCHB · VitalisCare · Axle Health · CareStitch · MedArrive'],
    ['Source', 'Vendor Scorecard v3.0, questionnaire form_version 2026-08-19'],
  ]),
  P({ children: [new PageBreak()] }),
);

/* ---------- How to use ---------- */
children.push(
  eyebrow('How to use this'),
  h1('Two layers, on purpose'),
  body('The common ten are the spine. Asking the same question of six vendors produces a spectrum; asking six different questions produces six unrelated conversations. Every one of the ten is built on something the field as a whole left thin — not on one vendor’s weakness.'),
  body('The vendor sets are the depth. Each is drawn from that vendor’s own admissions, contradictions and open items, quoted back to them. None can be answered from a slide.'),
  body('The third purpose is fairness. Every vendor gets the floor to explain where they look weaker than the others, so we measure the field across a spectrum of context rather than on a single return read in isolation. Question ten does this explicitly; the vendor sets do it by being answerable rather than accusatory.'),
  h2('Time budget'),
  metaTable([
    ['75 min', 'The walkthrough, referral → steady state, with common questions 1, 2 and 6 embedded where they fall naturally'],
    ['35 min', 'Common questions 3, 4, 5, 7, 8 and 9, plus the vendor-specific set'],
    ['10 min', 'Common question 10, and the vendor’s own questions'],
  ]),
  body('That is the full two hours with no slack. Send questions 3, 7, 8 and 9 ahead and ask for numbers ready, or the back half gets lost. For MedArrive, CareStitch and Axle Health the first vendor-specific question decides the rest of the call — ask it in the opening fifteen minutes, not at the end.', { after: 200 }),
  h2('Send one shared scenario'),
  body('Give all six the same case 48 hours ahead: one patient, one branch, one week — a Medicare start of care with PT and nursing, a mixed-discipline caseload, a rural-edge ZIP. Six walkthroughs of the same case are comparable. Six walkthroughs of each vendor’s favourite case are not. This is the highest-leverage preparation available to the round.'),
  P({ children: [new PageBreak()] }),
);

/* ---------- Part One ---------- */
children.push(
  eyebrow('Part one'),
  h1('The common ten'),
  body('Asked of every vendor, in these words.', { color: GREY, italics: true, after: 60 }),
  rule(140),
);
C.common.forEach((q, i) => children.push(...questionBlock(i + 1, q.t, q.q, q.r)));

/* ---------- Part Two ---------- */
children.push(
  P({ children: [new PageBreak()] }),
  eyebrow('Part two'),
  h1('Vendor by vendor'),
  body('Ordered by score. Each set is built from that vendor’s own return.', { color: GREY, italics: true, after: 60 }),
);

C.vendors.forEach((v, vi) => {
  children.push(
    P({ children: [new PageBreak()] }),
    eyebrow(v.score, { after: 60 }),
    P({ spacing: { before: 0, after: 150 },
      children: [run(v.name, { font: SERIF, size: 44, bold: true, color: INK })] }),
    P({ spacing: { after: 120, line: 290 },
      children: [run(v.posture, { font: SERIF, size: 22, italics: true, color: GREY })] }),
    rule(120, ACC, 8),
  );
  v.qs.forEach((q, i) => {
    const label = String(i + 1).padStart(2, '0');
    children.push(
      P({ spacing: { before: 300, after: 110 }, keepNext: true,
        indent: { left: 340, hanging: 340 },
        border: { left: { style: BorderStyle.SINGLE, size: 14, color: ACC, space: 14 } },
        children: [
          run(label + '   ', { font: SERIF, size: 22, bold: true, color: ACC }),
          run(q.q, { font: SERIF, size: 22, italics: true, color: INK }) ] }),
      P({ spacing: { before: 0, after: 40 }, keepNext: true, indent: { left: 340 },
        children: [run('WHY WE’RE ASKING', { font: SANS, size: 14, bold: true, color: ACC, characterSpacing: 50 })] }),
      P({ spacing: { after: 200, line: 290 }, indent: { left: 340 },
        children: [run(q.r, { font: SANS, size: 19, color: GREY })] }),
    );
  });
});

/* ---------- Closing ---------- */
children.push(
  P({ children: [new PageBreak()] }),
  eyebrow('After the call'),
  h1('What to write down'),
  body('Three things, while the room is still warm:'),
  metaTable([
    ['The verdict', 'For each question: answered, dodged, or changes the mark. The demo only earns its place if it can move a score.'],
    ['The room test', 'Deliberately left blank on the scorecard until now — would we want these people in our building for two years? Reason and initials.'],
    ['Stop-checks', 'HCHB’s continuity commitment, and MedArrive’s two. Resolved, or still open.'],
  ]),
  body('Then update the scorecard notes columns before the next call, not at the end of the week.', { after: 200 }),
);

const doc = new Document({
  creator: 'Compassus Home Health',
  title: 'Vendor Demo Question Guide',
  description: 'Round-two question architecture for the capacity & scheduling vendor evaluation',
  styles: { default: { document: { run: { font: SANS, size: 21, color: INK } } } },
  sections: [{
    properties: {
      page: {
        size: { width: 12240, height: 15840, orientation: PageOrientation.PORTRAIT },
        margin: { top: 1300, bottom: 1200, left: 1440, right: 1440 },
      },
    },
    footers: {
      default: new Footer({ children: [P({
        alignment: AlignmentType.RIGHT,
        spacing: { before: 200 },
        children: [
          run('Vendor Demo Question Guide   ·   ', { font: SANS, size: 15, color: GREY }),
          new TextRun({ children: [PageNumber.CURRENT], font: SANS, size: 15, color: GREY }),
        ] })] }),
    },
    children,
  }],
});

const out = process.argv[2] || 'Vendor-Demo-Question-Guide.docx';
Packer.toBuffer(doc).then(b => { fs.writeFileSync(out, b); console.log('wrote', out, b.length, 'bytes'); });
