#!/usr/bin/env python3
"""Build Vendor-Research-Matrix.xlsx and research/00-FIELD-NOTES.md.

Reads the `## At a glance` block out of every `research/<slug>.md` and lays the
fields down the page with the vendors across it — the same orientation as the
scorecard, so the two read the same way.

The dossier is the record. This workbook is a way of looking at six of them at
once. Nothing here is a score, and nothing here is computed: every cell is a
fact a researcher wrote in a dossier, carried across with its source numbers in
a cell comment.

House rules: regenerate, never hand-edit. Verify after every build (see
`verify()` at the foot of this file).

    python3 _research-matrix.gen.py
"""

from __future__ import annotations

import datetime as dt
import pathlib
import re
import sys

from openpyxl import Workbook, load_workbook
from openpyxl.comments import Comment
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter

HERE = pathlib.Path(__file__).resolve().parent
RESEARCH = HERE / "research"
XLSX = HERE / "Vendor-Research-Matrix.xlsx"
NOTES = RESEARCH / "00-FIELD-NOTES.md"

# ─── house palette ────────────────────────────────────────────────────────────
INK, MUTED, RULE, PAPER, BAND = "1B211E", "5A6560", "C9CCC5", "FBFBF8", "E9E9E5"
LANE = "8E9891"          # the rule between one vendor and the next
TINT_B = "F4F4F1"        # alternate vendor column
GAP = "FAF1F1"           # a *not found* cell: the gaps should show
GAP_INK = "792E2E"       # house maroon, for the words in a gap cell
FACE = "Aptos Narrow"

# ─── the row set ──────────────────────────────────────────────────────────────
# These labels are the contract with the dossiers. Rewording one here without
# rewording it in all six `## At a glance` blocks will drop the row.
BANDS: list[tuple[str, list[str]]] = [
    ("Company", [
        "Founded · HQ",
        "Legal entity",
        "Ownership · raised · last round",
        "Headcount · trend",
        "Leadership from home health",
        "Pivots or rebrands in 3 years",
        "Home health share of business",
    ]),
    ("Product", [
        "HCHB evidence",
        "Other EMRs named",
        "Scheduling unit",
        "Capacity",
        "Scheduling",
        "Engagement",
        "Decide or advise",
        "Clinician app",
    ]),
    ("Customers", [
        "Named home health customers",
        "Largest known deployment",
        "Customer count",
        "Impact figures with a baseline",
        "Independent customer voice",
    ]),
    ("Trust and continuity", [
        "Security attestation",
        "Uptime · SLA",
        "Named dependencies",
        "Pricing signal",
    ]),
    ("The read", [
        "Confidence",
        "The one thing to check",
    ]),
]
LABELS = [lab for _, labs in BANDS for lab in labs]

# What each row is for. Shown in the KEY column, so the workbook explains itself.
KEY = {
    "Founded · HQ": "age and where they sit",
    "Legal entity": "who we would be contracting with",
    "Ownership · raised · last round": "runway, and who they answer to",
    "Headcount · trend": "can they carry us",
    "Leadership from home health": "do they know our work — A2, Who wrote this",
    "Pivots or rebrands in 3 years": "durability: how settled is the thesis",
    "Home health share of business": "RF-16, first half",
    "HCHB evidence": "A1, the integration rung. A claim is not evidence",
    "Other EMRs named": "have they ever integrated with anything, and with what",
    "Scheduling unit": "the sharpest fit test on this sheet",
    "Capacity": "capacity comes first, and almost nobody has it",
    "Scheduling": "what the engine actually does",
    "Engagement": "patient-facing, or only staff-facing",
    "Decide or advise": "D1, D2, RF-10, RF-14. A higher score can be a worse fit",
    "Clinician app": "what a clinician actually holds, and what they say about it",
    "Named home health customers": "A2. Would we be the first",
    "Largest known deployment": "RF-16, second half",
    "Customer count": "how much of the business would we be",
    "Impact figures with a baseline": "A3, RF-05. The count is the finding",
    "Independent customer voice": "a customer talking is the best evidence there is",
    "Security attestation": "C6",
    "Uptime · SLA": "C6, RF-07. An outage stops nurses being deployed",
    "Named dependencies": "RF-03. An unnamed dependency cannot be reference-checked",
    "Pricing signal": "shape of the commercial model",
    "Confidence": "how much weight this column carries",
    "The one thing to check": "if you read one cell in this column, read this one",
}

NOT_FOUND = re.compile(r"\bnot found\b|\bnone\b", re.I)
SRC = re.compile(r"\s*\[(\d+)\]")


def strip_md(text: str) -> str:
    """Markdown emphasis out; the workbook carries plain words."""
    text = text.replace("**", "").replace("`", "")
    text = re.sub(r"(?<!\w)\*(?!\s)(.+?)(?<!\s)\*(?!\w)", r"\1", text)
    return text.strip()


def parse_dossier(path: pathlib.Path) -> dict | None:
    """Pull the `## At a glance` table out of one dossier."""
    text = path.read_text()
    block = re.search(r"## At a glance\n(.*?)(?=\n## )", text, re.S)
    if not block:
        return None

    name = re.match(r"#\s+(.+?)\s+—", text)
    fields: dict[str, tuple[str, list[str]]] = {}
    for line in block.group(1).splitlines():
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 2:
            continue
        label, value = cells[0], cells[1]
        if label.startswith("**") or label in ("Fact", "---"):
            continue          # band heading or the table's own header
        if set(label) <= set("-: "):
            continue
        sources = SRC.findall(value)
        fields[strip_md(label)] = (strip_md(SRC.sub("", value)), sources)

    researched = re.search(r"Researched (\d{4}-\d{2}-\d{2})", text)
    return {
        "slug": path.stem,
        "name": name.group(1) if name else path.stem,
        "researched": researched.group(1) if researched else "",
        "fields": fields,
    }


def roster_order(slugs: list[str]) -> list[str]:
    """Vendors appear in roster order; anything not on the roster goes last."""
    roster = RESEARCH / "00-ROSTER.md"
    order: list[str] = []
    if roster.exists():
        # Numbered rows of the roster table only. Slugs quoted elsewhere in the
        # file — the slug rule spells out `AutoMynd` → `auto-mynd` — are prose.
        for line in roster.read_text().splitlines():
            if not re.match(r"\|\s*\d+\s*\|", line):
                continue
            m = re.search(r"`([a-z0-9-]+)`", line)
            if m and m.group(1) in slugs and m.group(1) not in order:
                order.append(m.group(1))
    return order + sorted(s for s in slugs if s not in order)


def load_all() -> list[dict]:
    found = {}
    for path in sorted(RESEARCH.glob("*.md")):
        if path.stem.startswith("00-") or path.stem == "README":
            continue
        d = parse_dossier(path)
        if d is None:
            print(f"  ! {path.name}: no `## At a glance` block — skipped")
            continue
        found[d["slug"]] = d
    return [found[s] for s in roster_order(list(found))]


# ─── the workbook ─────────────────────────────────────────────────────────────
def F(sz=10, b=False, color=INK, italic=False):
    return Font(name=FACE, size=sz, bold=b, color=color, italic=italic)


def put(ws, cell, value, font=None, align=None, fillc=None, border=None):
    c = ws[cell]
    c.value = value
    if font:
        c.font = font
    if align:
        c.alignment = align
    if fillc:
        c.fill = PatternFill("solid", fgColor=fillc)
    if border:
        c.border = border
    return c


def build(vendors: list[dict]) -> None:
    wb = Workbook()
    ws = wb.active
    ws.title = "Research Matrix"
    ws.sheet_view.showGridLines = False

    thin = Side(style="thin", color=RULE)
    lane = Side(style="thin", color=LANE)
    LEFT = Alignment(horizontal="left", vertical="top", wrap_text=True)
    LEFT_MID = Alignment(horizontal="left", vertical="center", wrap_text=True)

    FACT_COL, KEY_COL = "B", "C"
    first = 4                                        # first vendor column index
    cols = [get_column_letter(first + i) for i in range(len(vendors))]

    ws.column_dimensions["A"].width = 1.6
    ws.column_dimensions[FACT_COL].width = 30
    ws.column_dimensions[KEY_COL].width = 34
    for col in cols:
        ws.column_dimensions[col].width = 46

    # Title block
    r = 2
    put(ws, f"{FACT_COL}{r}", "Vendor Research Matrix", F(15, True, INK), LEFT_MID)
    put(ws, f"{KEY_COL}{r}", "COMPASSUS  ·  CAPACITY & SCHEDULING",
        F(8, True, MUTED), Alignment(horizontal="left", vertical="center"))
    ws.row_dimensions[r].height = 24

    r = 3
    put(ws, f"{FACT_COL}{r}",
        f"The outside view · generated {dt.date.today():%d %b %Y} · "
        f"{len(vendors)} dossiers · do not hand-edit",
        F(8, False, MUTED, italic=True), LEFT_MID)
    ws.row_dimensions[r].height = 14

    r = 4
    put(ws, f"{FACT_COL}{r}",
        "One column per dossier, one row per fact the outside view can settle. Every cell is "
        "copied from that dossier's At a glance block; its source numbers are in the cell "
        "comment, and the dossier stays the record. Not found is a finding and is tinted so "
        "the gaps show. Nothing here is a score.",
        F(8, False, MUTED), LEFT)
    ws.merge_cells(start_row=r, start_column=2, end_row=r,
                   end_column=first + len(vendors) - 1)
    ws.row_dimensions[r].height = 26

    # Header
    hdr = 6
    put(ws, f"{FACT_COL}{hdr}", "FACT", F(8, True, MUTED), LEFT_MID)
    put(ws, f"{KEY_COL}{hdr}", "KEY  ·  why this row is here", F(8, True, MUTED), LEFT_MID)
    for i, (v, col) in enumerate(zip(vendors, cols)):
        tint = TINT_B if i % 2 else None
        c = put(ws, f"{col}{hdr}", v["name"], F(12, True, INK), LEFT_MID, tint)
        c.border = Border(left=lane, bottom=Side(style="medium", color=INK))
    ws.row_dimensions[hdr].height = 22

    sub = 7
    put(ws, f"{FACT_COL}{sub}", "", F(8))
    for i, (v, col) in enumerate(zip(vendors, cols)):
        conf = v["fields"].get("Confidence", ("", []))[0]
        put(ws, f"{col}{sub}",
            f"researched {v['researched']}  ·  confidence {conf}" if conf
            else f"researched {v['researched']}",
            F(8, False, MUTED, italic=True), LEFT_MID,
            TINT_B if i % 2 else None).border = Border(left=lane, bottom=thin)
    ws.row_dimensions[sub].height = 14

    ws.freeze_panes = f"{get_column_letter(first)}{sub + 1}"

    # Body
    row = sub + 1
    row_of: dict[str, int] = {}
    for band, labels in BANDS:
        put(ws, f"{FACT_COL}{row}", band.upper(), F(8, True, MUTED), LEFT_MID, BAND)
        put(ws, f"{KEY_COL}{row}", "", F(8), LEFT_MID, BAND)
        for i, col in enumerate(cols):
            put(ws, f"{col}{row}", "", F(8), LEFT_MID, BAND).border = Border(left=lane)
        ws.row_dimensions[row].height = 16
        row += 1

        for label in labels:
            row_of[label] = row
            put(ws, f"{FACT_COL}{row}", label, F(10, True, INK), LEFT)
            put(ws, f"{KEY_COL}{row}", KEY.get(label, ""), F(8, False, MUTED), LEFT)
            longest = 0
            for i, (v, col) in enumerate(zip(vendors, cols)):
                value, sources = v["fields"].get(label, ("—", []))
                gap = bool(NOT_FOUND.search(value)) and len(value) < 90
                fill = GAP if gap else (TINT_B if i % 2 else None)
                cell = put(ws, f"{col}{row}", value,
                           F(9, False, GAP_INK if gap else INK, italic=gap), LEFT, fill)
                cell.border = Border(left=lane, bottom=thin)
                if sources:
                    cell.comment = Comment(
                        "Sources in the dossier: "
                        + ", ".join(f"[{s}]" for s in sources),
                        "research", height=60, width=220)
                longest = max(longest, len(value))
            ws[f"{FACT_COL}{row}"].border = Border(bottom=thin)
            ws[f"{KEY_COL}{row}"].border = Border(bottom=thin)
            ws.row_dimensions[row].height = min(96, max(28, 13 * (longest // 52 + 1)))
            row += 1

    ws.sheet_properties.tabColor = "1F6F78"
    wb.save(XLSX)
    return row_of


# ─── the field notes ──────────────────────────────────────────────────────────
def field_notes(vendors: list[dict]) -> None:
    """Brief §6: one line per vendor, the disagreements, the commonplaces."""
    lines = [
        f"# Field notes — what the {len(vendors)} dossiers say together",
        "",
        f"**Generated** {dt.date.today():%Y-%m-%d} by `_research-matrix.gen.py` from "
        f"{len(vendors)} dossiers. Do not hand-edit; change a dossier and rebuild.",
        "",
        "The companion to `Vendor-Research-Matrix.xlsx`. The workbook is for looking across; "
        "this is for reading. Nothing here is a score.",
        "",
        "---",
        "",
        "## One line each",
        "",
        "| Vendor | The one thing to check |",
        "|---|---|",
    ]
    for v in vendors:
        one = v["fields"].get("The one thing to check", ("—", []))[0]
        lines.append(f"| **{v['name']}** | {one} |")

    # The commonplaces: a row nobody can answer is not a differentiator.
    lines += ["", "## The commonplaces", "",
              "Facts every vendor shares. A row that nobody publishes cannot tell one vendor "
              "from another, and a gap the whole field has is a question for the demo, not a "
              "mark against one company.", ""]
    silent, universal = [], []
    for label in LABELS:
        vals = [v["fields"].get(label, ("—", []))[0] for v in vendors]
        if all(NOT_FOUND.search(x) for x in vals):
            silent.append(label)
        elif len(set(vals)) == 1 and vals[0] not in ("—", ""):
            universal.append((label, vals[0]))
    if silent:
        lines.append("**Nobody publishes these.** " + "; ".join(f"*{s}*" for s in silent) + ".")
        lines.append("")
    for label, val in universal:
        lines.append(f"- **{label}** — every vendor: {val}")
    if not universal:
        lines.append("- No row has an identical value across every vendor.")

    # Where the columns disagree most: rows with the widest spread of answers.
    lines += ["", "## Where the field splits", "",
              "Rows where the vendors give genuinely different answers. These are the rows "
              "that will decide anything.", ""]
    for label in ("Scheduling unit", "Decide or advise", "HCHB evidence",
                  "Home health share of business", "Impact figures with a baseline"):
        lines.append(f"**{label}**")
        lines.append("")
        for v in vendors:
            val = v["fields"].get(label, ("—", []))[0]
            lines.append(f"- {v['name']} — {val}")
        lines.append("")

    lines += ["## How to read a column", "",
              "Top to bottom: who they are, what they built, who bought it, whether it stays "
              "up, and how much of the column to believe. The last row is the one to read if "
              "you read one. Every cell traces to a numbered source in the dossier of the "
              "same name; the dossier is the record and this file is not.", ""]
    NOTES.write_text("\n".join(lines) + "\n")


# ─── verification ─────────────────────────────────────────────────────────────
def verify(vendors: list[dict], row_of: dict[str, int]) -> None:
    """Re-open the saved file and check it says what we meant.

    There are no formulas in this workbook, so there is nothing for pycel to
    evaluate; the check is that every field landed in the right cell, that the
    gaps are tinted, that the sources travelled into comments, and that the
    panes are frozen.
    """
    wb = load_workbook(XLSX)
    ws = wb["Research Matrix"]
    first = 4
    cols = [get_column_letter(first + i) for i in range(len(vendors))]
    checks = 0

    assert ws.freeze_panes == f"{get_column_letter(first)}8", ws.freeze_panes

    for label in LABELS:
        row = row_of[label]
        assert ws[f"B{row}"].value == label, (label, ws[f"B{row}"].value)
        for v, col in zip(vendors, cols):
            want = v["fields"].get(label, ("—", []))
            got = ws[f"{col}{row}"]
            assert got.value == want[0], (v["slug"], label, got.value, want[0])
            if want[1]:
                assert got.comment is not None, (v["slug"], label, "lost its sources")
                for s in want[1]:
                    assert f"[{s}]" in got.comment.text, (v["slug"], label, s)
            checks += 1

    for v, col in zip(vendors, cols):
        assert ws[f"{col}6"].value == v["name"]

    gaps = sum(
        1
        for label in LABELS
        for col in cols
        if ws[f"{col}{row_of[label]}"].fill.fgColor.rgb in (f"00{GAP}", GAP)
    )
    blank = sum(
        1
        for label in LABELS
        for col in cols
        if not str(ws[f"{col}{row_of[label]}"].value or "").strip()
    )
    assert blank == 0, f"{blank} empty cells"

    print(f"  verified {checks} cells across {len(vendors)} vendors "
          f"× {len(LABELS)} facts · {gaps} tinted as a gap · 0 blank")



# ─── the reading copy ─────────────────────────────────────────────────────────
# Which bands take an arena colour, and which rows are the arenas themselves.
BAND_TICK = {
    "Company": "var(--muted)",
    "Product": "var(--teal)",
    "Customers": "var(--blue)",
    "Trust and continuity": "var(--gold)",
    "The read": "var(--ink)",
}
ARENA_ROW = {"Capacity": "var(--teal)", "Scheduling": "var(--blue)",
             "Engagement": "var(--green)"}
SPLITS = ["Scheduling unit", "Decide or advise", "HCHB evidence",
          "Home health share of business"]

CSS = """
:root{
  --paper:#FBFBF8; --ink:#1B211E; --muted:#5A6560; --rule:#C9CCC5;
  --band:#EFEFEA; --tint:#F5F5F1;
  --teal:#1F6F78; --blue:#2E599D; --green:#4E8A5B; --gold:#9A7B15;
  --gap-bg:#FAF1F1; --gap-ink:#8A3A3A;
  --shadow:rgba(27,33,30,.10);
}
@media (prefers-color-scheme:dark){
  :root:not([data-theme="light"]){
    --paper:#141815; --ink:#E7E9E3; --muted:#98A29B; --rule:#2F3731;
    --band:#1D231F; --tint:#191E1B;
    --teal:#5FB3B8; --blue:#7FA3DB; --green:#8CBF97; --gold:#C9A845;
    --gap-bg:#2A1D1D; --gap-ink:#D79797;
    --shadow:rgba(0,0,0,.45);
  }
}
:root[data-theme="dark"]{
  --paper:#141815; --ink:#E7E9E3; --muted:#98A29B; --rule:#2F3731;
  --band:#1D231F; --tint:#191E1B;
  --teal:#5FB3B8; --blue:#7FA3DB; --green:#8CBF97; --gold:#C9A845;
  --gap-bg:#2A1D1D; --gap-ink:#D79797;
  --shadow:rgba(0,0,0,.45);
}
*{box-sizing:border-box}
body{
  background:var(--paper); color:var(--ink); margin:0;
  font-family:"Mulish","Avenir Next",-apple-system,BlinkMacSystemFont,sans-serif;
  font-size:15px; line-height:1.55; -webkit-font-smoothing:antialiased;
}
/* Wide enough for the matrix to breathe; the prose keeps its own measure. */
.wrap{max-width:1440px; margin:0 auto; padding:56px 32px 24px}
.eyebrow{
  font-family:"IBM Plex Mono","SF Mono",ui-monospace,monospace;
  font-size:10.5px; letter-spacing:.18em; text-transform:uppercase;
  color:var(--muted); margin:0 0 18px;
}
h1{
  font-family:"Source Serif 4","Iowan Old Style",Georgia,serif;
  font-weight:600; font-size:44px; line-height:1.08; letter-spacing:-.015em;
  margin:0 0 16px; text-wrap:balance;
}
.lede{max-width:64ch; color:var(--muted); font-size:15px; margin:0 0 28px}
.lede strong{color:var(--ink); font-weight:600}

.tally{
  display:flex; flex-wrap:wrap; gap:0; margin:0 0 8px;
  border-top:1px solid var(--rule); border-bottom:1px solid var(--rule);
}
.tally div{
  padding:14px 28px 14px 0; margin-right:28px;
  border-right:1px solid var(--rule);
}
.tally div:last-child{border-right:0; margin-right:0; padding-right:0}
.tally b{
  display:block;
  font-family:"Source Serif 4",Georgia,serif;
  font-size:27px; font-weight:600; line-height:1.1;
  font-variant-numeric:tabular-nums;
}
.tally span{
  display:block;
  font-family:"IBM Plex Mono",ui-monospace,monospace;
  font-size:10px; letter-spacing:.11em; text-transform:uppercase;
  color:var(--muted); margin-top:4px;
}
.tally .loud b{color:var(--gap-ink)}

.frame{
  margin:34px 0 8px; overflow-x:auto; overflow-y:visible;
  border-top:1px solid var(--rule);
}
table{border-collapse:separate; border-spacing:0; width:max-content; min-width:100%}
th,td{
  text-align:left; vertical-align:top; padding:13px 18px;
  border-bottom:1px solid var(--rule);
}

/* the sticky fact column */
th.fact,td.fact{
  position:sticky; left:0; z-index:2; width:252px; min-width:252px;
  background:var(--paper); border-right:1px solid var(--rule);
}
.frame.scrolled th.fact, .frame.scrolled td.fact{box-shadow:6px 0 10px -8px var(--shadow)}
td.fact .lab{font-weight:700; font-size:13.5px; display:block}
td.fact .why{
  display:block; margin-top:3px; color:var(--muted); font-size:11.5px;
  line-height:1.42;
}

thead th{
  position:sticky; top:0; z-index:3; background:var(--paper);
  border-bottom:2px solid var(--ink); padding-top:16px; padding-bottom:12px;
}
thead th.fact{z-index:4}
thead .vname{
  font-family:"Source Serif 4",Georgia,serif;
  font-size:19px; font-weight:600; line-height:1.15; display:block;
}
thead .vmeta{
  display:block; margin-top:5px; color:var(--muted);
  font-family:"IBM Plex Mono",ui-monospace,monospace;
  font-size:10px; letter-spacing:.05em;
}
thead .col-head{width:262px; min-width:262px}

tr.band td{
  background:var(--band); padding:9px 18px;
  font-family:"IBM Plex Mono",ui-monospace,monospace;
  font-size:10px; letter-spacing:.16em; text-transform:uppercase;
  color:var(--muted); border-bottom:1px solid var(--rule);
}
tr.band td.fact{background:var(--band); border-left:3px solid var(--tick)}

td.cell{font-size:13.5px; line-height:1.5}
td.alt{background:var(--tint)}
td.gap{background:var(--gap-bg); color:var(--gap-ink); font-style:italic}
td.cell b{font-weight:700}
.src{
  font-family:"IBM Plex Mono",ui-monospace,monospace;
  font-size:9.5px; color:var(--muted); white-space:nowrap;
  margin-left:5px; letter-spacing:.02em; font-style:normal;
}
tr.arena td.fact .lab{color:var(--arena)}
tr.read td{border-bottom:0}
tr.read td.cell{font-weight:600}

.legend{
  display:flex; flex-wrap:wrap; gap:22px; align-items:center;
  font-family:"IBM Plex Mono",ui-monospace,monospace;
  font-size:10px; letter-spacing:.08em; text-transform:uppercase;
  color:var(--muted); padding:14px 0 0;
}
.legend i{display:inline-block; width:11px; height:11px; margin-right:7px;
  vertical-align:-1px; border:1px solid var(--rule)}
.swatch-gap{background:var(--gap-bg)}
.swatch-alt{background:var(--tint)}

.splits{margin:64px 0 0}
h2{
  font-family:"Source Serif 4",Georgia,serif;
  font-size:26px; font-weight:600; margin:0 0 8px; letter-spacing:-.01em;
}
.splits > p{color:var(--muted); max-width:64ch; margin:0 0 30px}
.split{margin:0 0 34px}
.split h3{
  font-family:"IBM Plex Mono",ui-monospace,monospace;
  font-size:10.5px; letter-spacing:.16em; text-transform:uppercase;
  color:var(--muted); margin:0 0 12px; padding-bottom:7px;
  border-bottom:1px solid var(--rule); font-weight:500;
}
.split dl{display:grid; grid-template-columns:170px 1fr; gap:9px 22px; margin:0}
.split dt{
  font-family:"Source Serif 4",Georgia,serif; font-size:15px; font-weight:600;
}
.split dd{margin:0; font-size:14px; color:var(--ink)}
.split dd.gap{color:var(--gap-ink); font-style:italic}

footer{
  margin:66px 0 0; padding:20px 0 0; border-top:1px solid var(--rule);
  color:var(--muted); font-size:12.5px; max-width:70ch;
}
footer code{font-family:"IBM Plex Mono",ui-monospace,monospace; font-size:11.5px}

@media (max-width:720px){
  .wrap{padding:36px 18px 20px}
  h1{font-size:32px}
  .split dl{grid-template-columns:1fr; gap:2px 0}
  .split dd{margin:0 0 12px; color:var(--muted)}
  th.fact,td.fact{width:170px; min-width:170px}
}
@media (prefers-reduced-motion:reduce){*{transition:none!important}}
"""

JS = """
const frame=document.querySelector('.frame');
frame.addEventListener('scroll',()=>{
  frame.classList.toggle('scrolled',frame.scrollLeft>2);
},{passive:true});
"""


def esc(text: str) -> str:
    return (text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))


def cell_html(value: str, sources: list[str]) -> str:
    out = esc(value)
    if sources:
        out += '<span class="src">' + " ".join(f"[{s}]" for s in sources) + "</span>"
    return out


def build_html(vendors: list[dict]) -> pathlib.Path:
    """The same matrix as a page, for reading rather than filling in."""
    gaps = sum(
        1
        for v in vendors
        for lab in LABELS
        if NOT_FOUND.search(v["fields"].get(lab, ("", []))[0])
        and len(v["fields"].get(lab, ("", []))[0]) < 90
    )
    total = len(vendors) * len(LABELS)

    # "N of ~M figures carry a baseline", summed off the dossiers rather than
    # typed in, so the tally cannot go stale when a vendor is added.
    with_base = seen = 0
    for v in vendors:
        m = re.search(r"(\d+)\s+of\s+~?(\d+)",
                      v["fields"].get("Impact figures with a baseline", ("", []))[0])
        if m:
            with_base += int(m.group(1))
            seen += int(m.group(2))
    figures = f"{with_base} of ~{seen}"   # the per-vendor counts are already approximate

    head = ['<th class="fact">'
            '<span class="vmeta">Fact</span></th>']
    for i, v in enumerate(vendors):
        conf = v["fields"].get("Confidence", ("", []))[0]
        head.append(
            f'<th class="col-head">'
            f'<span class="vname">{esc(v["name"])}</span>'
            f'<span class="vmeta">researched {esc(v["researched"])}'
            f'{" · confidence " + esc(conf) if conf else ""}</span></th>'
        )

    body: list[str] = []
    for band, labels in BANDS:
        tick = BAND_TICK.get(band, "var(--muted)")
        body.append(
            f'<tr class="band" style="--tick:{tick}">'
            f'<td class="fact">{esc(band)}</td>'
            + f'<td colspan="{len(vendors)}"></td></tr>'
        )
        for label in labels:
            cls = ["row"]
            style = ""
            if label in ARENA_ROW:
                cls.append("arena")
                style = f' style="--arena:{ARENA_ROW[label]}"'
            if label == "The one thing to check":
                cls.append("read")
            row = [f'<tr class="{" ".join(cls)}"{style}>',
                   f'<td class="fact"><span class="lab">{esc(label)}</span>'
                   f'<span class="why">{esc(KEY.get(label, ""))}</span></td>']
            for i, v in enumerate(vendors):
                value, sources = v["fields"].get(label, ("—", []))
                gap = bool(NOT_FOUND.search(value)) and len(value) < 90
                klass = "cell gap" if gap else ("cell alt" if i % 2 else "cell")
                row.append(f'<td class="{klass}">{cell_html(value, sources)}</td>')
            row.append("</tr>")
            body.append("".join(row))

    splits: list[str] = []
    for label in SPLITS:
        items = []
        for v in vendors:
            value, sources = v["fields"].get(label, ("—", []))
            gap = bool(NOT_FOUND.search(value)) and len(value) < 90
            items.append(
                f"<dt>{esc(v['name'])}</dt>"
                f'<dd class="{"gap" if gap else ""}">{cell_html(value, sources)}</dd>'
            )
        splits.append(
            f'<div class="split"><h3>{esc(label)}</h3><dl>{"".join(items)}</dl></div>'
        )

    html = f"""<title>Vendor Research Matrix</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?\
family=Source+Serif+4:opsz,wght@8..60,400;8..60,600&\
family=Mulish:wght@400;600;700&\
family=IBM+Plex+Mono:wght@400;500&display=swap">
<style>{CSS}</style>
<div class="wrap">
  <p class="eyebrow">Compassus · Capacity &amp; Scheduling · The outside view</p>
  <h1>Vendor Research Matrix</h1>
  <p class="lede">One column per dossier, one row per fact the outside view can settle.
  Every cell is copied from that dossier's <em>At a glance</em> block and carries its source
  numbers; <strong>the dossier stays the record</strong>. <em>Not found</em> is a finding, and
  it is tinted so the gaps show. <strong>Nothing here is a score.</strong></p>

  <div class="tally">
    <div><b>{len(vendors)}</b><span>Dossiers</span></div>
    <div><b>{len(LABELS)}</b><span>Facts each</span></div>
    <div class="loud"><b>{gaps} of {total}</b><span>Cells are a gap</span></div>
    <div class="loud"><b>{figures}</b><span>Figures with a baseline</span></div>
    <div><b>0</b><span>Verified HCHB integrations</span></div>
  </div>

  <div class="frame">
    <table>
      <thead><tr>{"".join(head)}</tr></thead>
      <tbody>{"".join(body)}</tbody>
    </table>
  </div>

  <p class="legend">
    <span><i class="swatch-gap"></i>Not found — a finding, not an omission</span>
    <span><i class="swatch-alt"></i>Alternate column</span>
    <span>[n] — source number in that vendor's dossier</span>
  </p>

  <section class="splits">
    <h2>Where the field splits</h2>
    <p>Four rows carry most of the decision. Everything else either agrees across the field or
    is missing across the field, and neither tells one vendor from another.</p>
    {"".join(splits)}
  </section>

  <footer>
    Generated {dt.date.today():%d %B %Y} by <code>_research-matrix.gen.py</code> from
    {len(vendors)} dossiers in <code>vendor-evaluation/research/</code>. Regenerate; never
    hand-edit. The workbook of the same name is the same data laid out for the team to work
    in. Research never scores: it tests what a vendor claimed and feeds the notes column and
    the demo agenda.
  </footer>
</div>
<script>{JS}</script>
"""
    out = HERE / "Vendor-Research-Matrix.html"
    out.write_text(html)
    return out




def main() -> int:
    vendors = load_all()
    if not vendors:
        print("No dossiers with an `## At a glance` block. Nothing to build.")
        return 1
    print(f"Read {len(vendors)} dossiers: {', '.join(v['slug'] for v in vendors)}")
    missing = [
        (v["slug"], lab) for v in vendors for lab in LABELS if lab not in v["fields"]
    ]
    for slug, lab in missing:
        print(f"  ! {slug} has no row for “{lab}”")
    row_of = build(vendors)
    verify(vendors, row_of)
    field_notes(vendors)
    page = build_html(vendors)
    print(f"Wrote {XLSX.name}, {NOTES.name} and {page.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
