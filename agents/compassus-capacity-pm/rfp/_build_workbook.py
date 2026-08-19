# -*- coding: utf-8 -*-
"""Build the vendor questionnaire workbook.

Emits two files from one source:
  Compassus-Vendor-Questionnaire.xlsx         vendor-facing  (Instructions, Questionnaire, Overview)
  Compassus-Vendor-Questionnaire-MASTER.xlsx  internal       (+ Coverage-Expanded, Additional, Vetting)

Mechanics follow the verified design spec. Four openpyxl flags are INVERTED from
how they read — they are commented at each use site.
"""
import math

from openpyxl import Workbook
from openpyxl.styles import Alignment, Border, Font, PatternFill, Protection, Side
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.worksheet.hyperlink import Hyperlink
from openpyxl.workbook.defined_name import DefinedName

import _content as C

# ---------------------------------------------------------------- palette
INK      = "FF1F2A37"
MUTED    = "FF5B6572"
BAND     = "FF1F3B57"
TINT     = "FFEEF2F6"
RULE     = "FFD8DEE6"
ANS_FILL = "FFFDFBF3"
ANS_EDGE = "FFC7B37A"
WHITE    = "FFFFFFFF"

CAP, SCH, ENG = "FF2C6A55", "FF3A5C86", "FF8C5A2E"
ACCENT = {"cap": CAP, "sch": SCH, "eng": ENG}

BODY = "Calibri"   # metrically stable on Windows and Mac; ships with every Office install

f_title   = Font(name=BODY, size=16, bold=True, color=INK)
f_sub     = Font(name=BODY, size=10.5, color=MUTED)
f_band    = Font(name=BODY, size=11, bold=True, color=WHITE)
f_q       = Font(name=BODY, size=11, color=INK)
f_qid     = Font(name=BODY, size=10, bold=True, color=MUTED)
f_qlabel  = Font(name=BODY, size=11, bold=True, color=INK)
f_hdr     = Font(name=BODY, size=9, bold=True, color=MUTED)
f_ans     = Font(name=BODY, size=11, color=INK)
f_note    = Font(name=BODY, size=10, italic=True, color=MUTED)
f_mod     = Font(name=BODY, size=11, bold=True, color=WHITE)

edge = Side(style="thin", color=ANS_EDGE)
ANS_BORDER = Border(left=edge, right=edge, top=edge, bottom=edge)
hair = Side(style="thin", color=RULE)
RULE_BOTTOM = Border(bottom=hair)

A_WRAP  = Alignment(wrap_text=True, vertical="top")
A_WRAPI = Alignment(wrap_text=True, vertical="top", indent=1)
A_TOP   = Alignment(vertical="top")
A_CTR   = Alignment(vertical="center")
A_CTRW  = Alignment(wrap_text=True, vertical="center")

# expected answer length in words, per question -> drives row height
EXPECTED = {
    "A1": 200, "A2": 150, "A3": 120, "A4": 90,
    "C1": 150, "C2": 100, "C3": 150, "C4": 140, "C5": 140, "C6": 140,
    "D1": 150, "D2": 120, "D3": 150, "D4": 120,
    "E1": 140, "E2": 140, "E3": 100,
}


def answer_height(expected_words, col_width=78, pt=11):
    chars_per_line = col_width - 3
    lines = math.ceil(expected_words * 6.2 / chars_per_line)
    return round(lines * pt * 1.32 + 6)


def set_widths(ws, widths):
    for col, w in widths:
        ws.column_dimensions[col].width = w


def band_row(ws, r, text, first="B", last="D", fill=BAND, font=f_band, height=22):
    for col in range(ord(first) - 64, ord(last) - 64 + 1):
        cell = ws.cell(row=r, column=col)
        cell.fill = PatternFill("solid", fgColor=fill)
        cell.alignment = A_CTR
    c = ws.cell(row=r, column=ord(first) - 64, value=text)
    c.font = font
    c.alignment = Alignment(vertical="center", indent=1)
    ws.row_dimensions[r].height = height


# ================================================================ Instructions
def build_instructions(wb, vendor_facing=True):
    ws = wb.create_sheet("Instructions")
    ws.sheet_view.showGridLines = False
    set_widths(ws, [("A", 2.5), ("B", 7), ("C", 44), ("D", 78), ("E", 2.5)])

    ws["B2"] = "Compassus Home Health"
    ws["B2"].font = Font(name=BODY, size=10, bold=True, color=MUTED)
    ws["B3"] = "Capacity & Scheduling Platform — Vendor Questionnaire"
    ws["B3"].font = f_title
    ws.row_dimensions[3].height = 24

    r = 5
    for head, body in [
        ("How to use this workbook",
         "Answer in the cream-coloured cells. Everything else is locked so the layout stays intact "
         "as the file travels — the password is “review” if you ever need it. Nothing here is a "
         "trick; the protection is only there to keep the document readable when it comes back."),
        ("Answering",
         "Answer in your own words. Most answers run a short paragraph. There is no advantage in "
         "volume, and where something does not apply to your product, saying so plainly is a "
         "genuinely useful answer."),
        ("Practical notes",
         "Press Alt+Enter to start a new paragraph inside a cell. Press Ctrl+Shift+U to expand the "
         "formula bar if you would rather write there. You can drag any row taller if you need more "
         "room — the height we set is only a suggestion of length."),
        ("Working as a team",
         "If several people need to contribute, put the file in your own SharePoint or Drive to "
         "co-author it, then send the completed workbook back."),
        ("The Overview tab",
         "The Overview tab reproduces the one-page summary of what we are looking for. It is there "
         "for reference while you answer."),
    ]:
        c = ws.cell(row=r, column=2, value=head)
        c.font = f_qlabel
        ws.merge_cells(start_row=r, start_column=2, end_row=r, end_column=4) if False else None
        r += 1
        c = ws.cell(row=r, column=2, value=body)
        c.font = f_q
        c.alignment = A_WRAP
        ws.row_dimensions[r].height = answer_height(len(body.split()) * 1.0, col_width=125)
        r += 2

    # progress indicator
    ws.cell(row=r, column=2, value="Progress").font = f_qlabel
    r += 1
    p = ws.cell(row=r, column=2,
                value='=COUNTA(Questionnaire!D:D)-1 & " of 17 questions answered"')
    p.font = Font(name=BODY, size=12, bold=True, color=BAND)
    ws.row_dimensions[r].height = 20
    r += 1
    n = ws.cell(row=r, column=2, value="Updates as you type. The count includes only the answer cells.")
    n.font = f_note

    ws.sheet_properties.tabColor = "FF9AA5B1"
    ws.page_setup.orientation = "portrait"
    return ws


# ================================================================ Questionnaire
def build_questionnaire(wb):
    ws = wb.create_sheet("Questionnaire")
    ws.sheet_view.showGridLines = False
    set_widths(ws, [("A", 2.5), ("B", 7), ("C", 44), ("D", 78), ("E", 2.5)])

    ws["B1"] = "Compassus Home Health  ·  Capacity & Scheduling Platform"
    ws["B1"].font = Font(name=BODY, size=10, bold=True, color=MUTED)
    ws["B2"] = "Vendor Questionnaire"
    ws["B2"].font = f_title
    ws.row_dimensions[2].height = 22

    ws["B3"] = "Vendor"
    ws["B3"].font = f_hdr
    ws["C3"].fill = PatternFill("solid", fgColor=ANS_FILL)
    ws["C3"].border = ANS_BORDER
    ws["C3"].protection = Protection(locked=False)
    ws["D3"] = "Completed by / date"
    ws["D3"].font = f_hdr
    ws["D3"].alignment = Alignment(horizontal="right")
    ws.row_dimensions[3].height = 18

    ws.row_dimensions[4].height = 6
    answer_rows = []
    r = 5

    for key, title, framing, qs in C.SECTIONS:
        band_row(ws, r, f"{key}.   {title.upper()}")
        r += 1
        if framing:
            c = ws.cell(row=r, column=2, value=framing)
            c.font = f_note
            c.alignment = A_WRAP
            ws.row_dimensions[r].height = answer_height(len(framing.split()), col_width=125)
            r += 1
        # column headers
        for col, txt in ((2, "#"), (3, "QUESTION"), (4, "YOUR ANSWER")):
            c = ws.cell(row=r, column=col, value=txt)
            c.font = f_hdr
            c.border = RULE_BOTTOM
        ws.row_dimensions[r].height = 15
        r += 1

        for qid, label, text in qs:
            ws.cell(row=r, column=2, value=qid).font = f_qid
            ws.cell(row=r, column=2).alignment = A_TOP
            qc = ws.cell(row=r, column=3, value=f"{label}\n{text}")
            qc.font = f_q
            qc.alignment = A_WRAP
            a = ws.cell(row=r, column=4)
            a.fill = PatternFill("solid", fgColor=ANS_FILL)
            a.border = ANS_BORDER
            a.alignment = A_WRAPI
            a.font = f_ans
            a.protection = Protection(locked=False)   # INVERTED elsewhere; here locked=False = editable
            h = max(answer_height(EXPECTED.get(qid, 120)),
                    answer_height(len(text.split()) * 1.15, col_width=44))
            ws.row_dimensions[r].height = h
            answer_rows.append(r)
            r += 1
            ws.row_dimensions[r].height = 5
            r += 1

        # Part B goes straight after Part A
        if key == "A":
            r = build_coverage(ws, r, C.COVERAGE_STANDARD, answer_rows,
                               "B.   COVERAGE SELF-ASSESSMENT",
                               "Mark where you stand on each area, then add anything you want us to "
                               "understand in the notes column.")
        r += 1

    ws.freeze_panes = "A5"
    ws.print_title_rows = "1:4"
    ws.sheet_properties.tabColor = BAND
    setup_print(ws)
    return ws, answer_rows


def build_coverage(ws, r, coverage, answer_rows, band_text, intro):
    """Status grid. Returns the next free row."""
    r += 1
    band_row(ws, r, band_text)
    r += 1
    c = ws.cell(row=r, column=2, value=intro)
    c.font = f_note
    c.alignment = A_WRAP
    ws.row_dimensions[r].height = 28
    r += 1
    for col, txt in ((2, "#"), (3, "AREA"), (4, "STATUS  →  then notes")):
        c = ws.cell(row=r, column=col, value=txt)
        c.font = f_hdr
        c.border = RULE_BOTTOM
    r += 1

    n = 0
    status_rows = []
    for module, rows in coverage:
        mod = ws.cell(row=r, column=2, value=module)
        for col in (2, 3, 4):
            ws.cell(row=r, column=col).fill = PatternFill("solid", fgColor=TINT)
        mod.font = Font(name=BODY, size=10.5, bold=True, color=BAND)
        ws.row_dimensions[r].height = 18
        r += 1
        for name, desc in rows:
            n += 1
            ws.cell(row=r, column=2, value=n).font = f_qid
            ws.cell(row=r, column=2).alignment = A_TOP
            qc = ws.cell(row=r, column=3, value=f"{name} — {desc}")
            qc.font = f_q
            qc.alignment = A_WRAP
            a = ws.cell(row=r, column=4)
            a.fill = PatternFill("solid", fgColor=ANS_FILL)
            a.border = ANS_BORDER
            a.alignment = A_WRAPI
            a.font = f_ans
            a.protection = Protection(locked=False)
            ws.row_dimensions[r].height = 30
            status_rows.append(r)
            r += 1
    ws._status_rows = getattr(ws, "_status_rows", []) + status_rows
    return r


def setup_print(ws, orientation="portrait"):
    ws.page_setup.orientation = orientation
    ws.page_setup.paperSize = ws.PAPERSIZE_A4
    ws.page_setup.fitToWidth = 1
    ws.page_setup.fitToHeight = 0
    ws.sheet_properties.pageSetUpPr.fitToPage = True   # REQUIRED or fitToWidth is ignored
    ws.print_options.horizontalCentered = True
    ws.page_margins.left = ws.page_margins.right = 0.5
    ws.page_margins.top = ws.page_margins.bottom = 0.6
    ws.oddFooter.left.text = "Compassus Home Health — Vendor Questionnaire"
    ws.oddFooter.right.text = "Page &P of &N"


# ================================================================ list sheet + validation
def add_lists(wb):
    lists = wb.create_sheet("Lists")
    for i, v in enumerate(C.STATUS_OPTIONS, start=1):
        lists.cell(row=i, column=1, value=v)
    lists.sheet_state = "hidden"
    wb.defined_names.add(DefinedName("StatusList", attr_text=f"Lists!$A$1:$A${len(C.STATUS_OPTIONS)}"))
    return lists


def attach_status_validation(ws, rows):
    if not rows:
        return
    dv = DataValidation(
        type="list",
        formula1="StatusList",       # NO leading "=" — openpyxl writes this verbatim
        allow_blank=True,
        showDropDown=False,          # INVERTED: False => the arrow IS shown
        showInputMessage=True,
        promptTitle="Select status",
        prompt="Production · In development · Roadmap · Not offered. Add a note after your choice.",
        showErrorMessage=False,      # warn-free: they may want to write a nuanced answer instead
    )
    ws.add_data_validation(dv)       # MUST precede dv.add()
    for r in rows:
        dv.add(f"D{r}")


# ================================================================ protection
def protect(ws):
    ws.protection.sheet = True
    ws.protection.password = "review"
    # INVERTED THROUGHOUT: False = ALLOWED, True = forbidden
    ws.protection.selectLockedCells = False     # can click/copy question text
    ws.protection.selectUnlockedCells = False   # MANDATORY — or nobody can type
    ws.protection.formatCells = False           # can bold a product name
    ws.protection.formatRows = False            # MANDATORY — can drag a row taller
    ws.protection.formatColumns = True
    ws.protection.insertRows = True
    ws.protection.deleteRows = True
    ws.protection.insertColumns = True
    ws.protection.deleteColumns = True
    ws.protection.sort = True
    ws.protection.autoFilter = True
    ws.protection.objects = True
    ws.protection.scenarios = True


# ================================================================ internal sheets
def build_expanded(wb):
    ws = wb.create_sheet("Coverage — Expanded")
    ws.sheet_view.showGridLines = False
    set_widths(ws, [("A", 2.5), ("B", 7), ("C", 62), ("D", 60), ("E", 2.5)])
    ws["B2"] = "Coverage self-assessment — expanded"
    ws["B2"].font = f_title
    ws["B3"] = ("An optional deeper version of the Part B grid, rolled up from the variable "
                "inventory's own subcategories. Use this instead of the 10-row grid if we want more "
                "granularity from vendors. It does not expose the numbered inventory itself.")
    ws["B3"].font = f_note
    ws["B3"].alignment = A_WRAP
    ws.row_dimensions[3].height = 32
    r = 5
    band_row(ws, r, "COVERAGE — EXPANDED")
    r += 1
    for col, txt in ((2, "#"), (3, "AREA"), (4, "STATUS  →  then notes")):
        c = ws.cell(row=r, column=col, value=txt)
        c.font = f_hdr
        c.border = RULE_BOTTOM
    r += 1
    n = 0
    rows = []
    for module, items in C.COVERAGE_EXPANDED:
        for col in (2, 3, 4):
            ws.cell(row=r, column=col).fill = PatternFill("solid", fgColor=TINT)
        m = ws.cell(row=r, column=2, value=module)
        m.font = Font(name=BODY, size=10.5, bold=True, color=BAND)
        ws.row_dimensions[r].height = 18
        r += 1
        for name, desc in items:
            n += 1
            ws.cell(row=r, column=2, value=n).font = f_qid
            qc = ws.cell(row=r, column=3, value=f"{name} — {desc}")
            qc.font = f_q
            qc.alignment = A_WRAP
            a = ws.cell(row=r, column=4)
            a.fill = PatternFill("solid", fgColor=ANS_FILL)
            a.border = ANS_BORDER
            a.alignment = A_WRAPI
            a.protection = Protection(locked=False)
            ws.row_dimensions[r].height = 28
            rows.append(r)
            r += 1
    ws.freeze_panes = "A7"
    ws.sheet_properties.tabColor = "FF6B7C93"
    setup_print(ws)
    return ws, rows


def build_additional(wb):
    ws = wb.create_sheet("Additional Questions")
    ws.sheet_view.showGridLines = False
    set_widths(ws, [("A", 2.5), ("B", 7), ("C", 110), ("D", 2.5)])
    ws["B2"] = "Additional questions — held for follow-up"
    ws["B2"].font = f_title
    ws["B3"] = ("Internal. Drafted, judged valuable, and deliberately kept out of round one so the "
                "questionnaire stays answerable. Most need a screen, a follow-up or a tone of voice "
                "to be worth anything — which is what the virtual calls are for.")
    ws["B3"].font = f_note
    ws["B3"].alignment = A_WRAP
    ws.row_dimensions[3].height = 32
    r = 5
    for group, items in C.ADDITIONAL:
        band_row(ws, r, group.upper(), last="C")
        r += 1
        for i, q in enumerate(items, start=1):
            ws.cell(row=r, column=2, value=i).font = f_qid
            ws.cell(row=r, column=2).alignment = A_TOP
            c = ws.cell(row=r, column=3, value=q)
            c.font = f_q
            c.alignment = A_WRAP
            ws.row_dimensions[r].height = max(16, answer_height(len(q.split()) * 1.1, col_width=110))
            r += 1
        r += 1
    ws.freeze_panes = "A5"
    ws.sheet_properties.tabColor = "FF8C7A5B"
    setup_print(ws)
    return ws


def build_vetting(wb):
    ws = wb.create_sheet("Vetting — For Leaders")
    ws.sheet_view.showGridLines = False
    set_widths(ws, [("A", 2.5), ("B", 30), ("C", 74), ("D", 44), ("E", 2.5)])
    ws["B2"] = "Vetting questions — for review with leadership"
    ws["B2"].font = f_title
    ws["B3"] = C.VETTING_NOTE
    ws["B3"].font = f_note
    ws["B3"].alignment = A_WRAP
    ws.row_dimensions[3].height = 44
    r = 5
    band_row(ws, r, "SET ASIDE FROM ROUND ONE")
    r += 1
    for col, txt in ((2, "TOPIC"), (3, "QUESTION AS DRAFTED"), (4, "WHY IT IS SET ASIDE")):
        c = ws.cell(row=r, column=col, value=txt)
        c.font = f_hdr
        c.border = RULE_BOTTOM
    r += 1
    for topic, q, why in C.VETTING:
        t = ws.cell(row=r, column=2, value=topic)
        t.font = f_qlabel
        t.alignment = A_WRAP
        qc = ws.cell(row=r, column=3, value=q)
        qc.font = f_q
        qc.alignment = A_WRAP
        w = ws.cell(row=r, column=4, value=why)
        w.font = f_note
        w.alignment = A_WRAP
        ws.row_dimensions[r].height = max(
            answer_height(len(q.split()) * 1.15, col_width=74), 34)
        r += 1
    ws.freeze_panes = "A7"
    ws.sheet_properties.tabColor = "FF7A4E4E"
    setup_print(ws)
    return ws


def build_meta(wb, audience):
    ws = wb.create_sheet("Meta")
    ws["A1"] = "form_version"; ws["B1"] = "2026-08-19"
    ws["A2"] = "audience";     ws["B2"] = audience
    ws["A3"] = "issued_by";    ws["B3"] = "Compassus Home Health"
    ws["A4"] = "question_ids"; ws["B4"] = ",".join(EXPECTED.keys())
    ws.sheet_state = "hidden"
    return ws
