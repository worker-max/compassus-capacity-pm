# -*- coding: utf-8 -*-
"""Build the vendor questionnaire workbook.

Emits two files from one source:
  Compassus-Vendor-Questionnaire.xlsx         vendor-facing  (Instructions, Questionnaire, Overview)
  Compassus-Vendor-Questionnaire-MASTER.xlsx  internal       (+ Coverage-Expanded, Additional, Vetting)

Column plan (all sheets share it so the eye does not have to re-learn):
  A gutter · B number · C question/area · D status (grid only) · E answer/notes · F gutter

Two rules that are easy to get wrong:
  * A wrapped paragraph must be MERGED across the columns it visually spans, or Excel
    wraps it inside one narrow column. Merged cells never auto-fit, so every merged
    paragraph also needs an explicit computed height.
  * Four openpyxl flags are INVERTED from how they read. Commented at each use site.
"""
import math
import re

from PIL import ImageFont
from openpyxl import Workbook
from openpyxl.styles import Alignment, Border, Font, PatternFill, Protection, Side
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.utils import get_column_letter
from openpyxl.workbook.defined_name import DefinedName
from openpyxl.cell.rich_text import CellRichText, TextBlock
from openpyxl.cell.text import InlineFont

import _content as C

# ---------------------------------------------------------------- palette
INK, MUTED, BAND = "FF1F2A37", "FF5B6572", "FF1F3B57"
TINT, RULE = "FFEEF2F6", "FFD8DEE6"
ANS_FILL, ANS_EDGE, WHITE = "FFFDFBF3", "FFC7B37A", "FFFFFFFF"

BODY = "Calibri"

f_title  = Font(name=BODY, size=16, bold=True, color=INK)
f_band   = Font(name=BODY, size=11, bold=True, color=WHITE)
f_q      = Font(name=BODY, size=11, color=INK)
f_qid    = Font(name=BODY, size=10, bold=True, color=MUTED)
f_qlabel = Font(name=BODY, size=11, bold=True, color=INK)
f_hdr    = Font(name=BODY, size=9, bold=True, color=MUTED)
f_ans    = Font(name=BODY, size=11, color=INK)
f_note   = Font(name=BODY, size=10.5, italic=True, color=MUTED)

edge = Side(style="thin", color=ANS_EDGE)
ANS_BORDER = Border(left=edge, right=edge, top=edge, bottom=edge)
RULE_BOTTOM = Border(bottom=Side(style="thin", color=RULE))

A_WRAP  = Alignment(wrap_text=True, vertical="top")
A_WRAPI = Alignment(wrap_text=True, vertical="top", indent=1)
A_TOP   = Alignment(vertical="top")
A_CTR   = Alignment(vertical="center")

# columns
W = [("A", 2.5), ("B", 7), ("C", 42), ("D", 16), ("E", 68), ("F", 2.5)]
COL_N, COL_Q, COL_S, COL_A = 2, 3, 4, 5
ANSW = 68                    # answer column width, in Excel character units

EXPECTED = {
    "A1": 170, "A2": 140, "A3": 110, "A4": 85,
    "C1": 140, "C2": 95, "C3": 140, "C4": 130, "C5": 130, "C6": 130,
    "D1": 140, "D2": 110, "D3": 140, "D4": 110,
    "E1": 130, "E2": 130, "E3": 95,
}


# ---------------------------------------------------------------- text metrics
# Character counts lie: Calibri "M" is ~3.7x the width of "i", and these strings run
# 30-400 characters. Every merged paragraph needs an explicit height (merged cells
# never auto-fit), so the height has to come from measured glyph advances.
# Liberation Sans stands in for Calibri and is ~8% wider, which biases every row
# slightly tall — the safe direction, since too short clips text with no recourse.
TTF = "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"
TTFB = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
SS = 8                              # supersample so getlength keeps sub-pixel accuracy
MDW = 7                             # max digit width, Calibri 11 Normal style
LEAD = 1.34
_fcache = {}


def _font(pt, bold=False):
    key = (round(pt * 100), bold)
    if key not in _fcache:
        _fcache[key] = ImageFont.truetype(TTFB if bold else TTF, round(pt * 96 / 72 * SS))
    return _fcache[key]


def text_px(s, pt, bold=False):
    return _font(pt, bold).getlength(s) / SS


def col_px(w):
    return w * MDW + 5


def span_px(ws, c1, c2, pad=9):
    """Pixel width of a merged run of columns on THIS sheet, less Excel's cell padding.

    Read from the sheet, not from W — the Vetting tab overrides the column plan.
    """
    total = 0.0
    for c in range(c1, c2 + 1):
        total += col_px(ws.column_dimensions[get_column_letter(c)].width or 8.43)
    return total - pad


def wrap_lines(runs, avail_px):
    """Line count for a list of (text, pt, bold) runs. Honours explicit newlines."""
    n, cur = 1, 0.0
    for text, pt, bold in runs:
        for i, seg in enumerate(text.split("\n")):
            if i:
                n += 1
                cur = 0.0
            for w in re.findall(r"\S+\s*", seg):
                ww = text_px(w, pt, bold)
                if cur + ww > avail_px and cur:
                    n += 1
                    cur = text_px(w.lstrip(), pt, bold)
                else:
                    cur += ww
    return n


def block_height(ws, runs, c1, c2, pt=11, pad=6, floor=0):
    return max(floor, round(wrap_lines(runs, span_px(ws, c1, c2)) * pt * LEAD + pad))


# Average advance of one word of ordinary prose, measured rather than assumed —
# "responsiveness" is 3x the width of "the", so a single specimen word would be wrong.
PROSE = ("we plan the week against available capacity and confirm each visit with the "
         "patient before the clinician leaves for it ")


def word_px(pt):
    return text_px(PROSE, pt) / len(PROSE.split())


def answer_height(words, col_width=ANSW, pt=11):
    """Room for a prose answer of roughly `words` words, in a column `col_width` wide."""
    lines = math.ceil(words * word_px(pt) / (col_px(col_width) - 9))
    return round(lines * pt * LEAD + 6)


def set_widths(ws, widths=W):
    for col, w in widths:
        ws.column_dimensions[col].width = w


def para(ws, r, text, c1, c2, font, pt=10.5, pad=6):
    """A wrapped paragraph merged across c1..c2, with a height that fits it."""
    ws.merge_cells(start_row=r, end_row=r, start_column=c1, end_column=c2)
    c = ws.cell(row=r, column=c1, value=text)
    c.font = font
    c.alignment = A_WRAP
    ws.row_dimensions[r].height = block_height(ws, [(text, pt, False)], c1, c2, pt=pt, pad=pad)
    return r + 1


def band_row(ws, r, text, c1=COL_N, c2=COL_A, height=22):
    for col in range(c1, c2 + 1):
        ws.cell(row=r, column=col).fill = PatternFill("solid", fgColor=BAND)
    ws.merge_cells(start_row=r, end_row=r, start_column=c1, end_column=c2)
    c = ws.cell(row=r, column=c1, value=text)
    c.font = f_band
    c.alignment = Alignment(vertical="center", indent=1)
    ws.row_dimensions[r].height = height
    return r + 1


def answer_cell(ws, r, col, height=None):
    a = ws.cell(row=r, column=col)
    a.fill = PatternFill("solid", fgColor=ANS_FILL)
    a.border = ANS_BORDER
    a.alignment = A_WRAPI
    a.font = f_ans
    a.protection = Protection(locked=False)   # the only unlocked cells in the sheet
    if height:
        ws.row_dimensions[r].height = height
    return a


def col_headers(ws, r, labels):
    for col, txt in labels:
        c = ws.cell(row=r, column=col, value=txt)
        c.font = f_hdr
        c.border = RULE_BOTTOM
    ws.row_dimensions[r].height = 15
    return r + 1


# ================================================================ Instructions
def build_instructions(wb, vendor_facing=True):
    ws = wb.create_sheet("Instructions")
    ws.sheet_view.showGridLines = False
    set_widths(ws)

    ws.merge_cells(start_row=2, end_row=2, start_column=COL_N, end_column=COL_A)
    ws.cell(row=2, column=COL_N, value="Compassus Home Health").font = Font(
        name=BODY, size=10, bold=True, color=MUTED)
    ws.merge_cells(start_row=3, end_row=3, start_column=COL_N, end_column=COL_A)
    ws.cell(row=3, column=COL_N, value="Capacity & Scheduling Platform — Vendor Questionnaire"
            ).font = f_title
    ws.row_dimensions[3].height = 24

    r = 5
    for head, body in [
        ("How to use this workbook",
         "Answer in the cream-coloured cells. Everything else is locked so the layout stays intact as "
         "the file travels — the password is “review” if you ever need it. The protection is only "
         "there to keep the document readable when it comes back."),
        ("Practical notes",
         "Press Alt+Enter to start a new paragraph inside a cell. Press Ctrl+Shift+U to expand the "
         "formula bar if you would rather write there. You can drag any row taller if you need more "
         "room."),
        ("Working as a team",
         "If several people need to contribute, put the file in your own SharePoint or Drive to "
         "co-author it, then send the completed workbook back."),
        ("The Overview tab",
         "The Overview tab reproduces the one-page summary of what we are looking for. It is there "
         "for reference while you answer."),
    ]:
        ws.merge_cells(start_row=r, end_row=r, start_column=COL_N, end_column=COL_A)
        ws.cell(row=r, column=COL_N, value=head).font = f_qlabel
        r += 1
        r = para(ws, r, body, COL_N, COL_A, f_q, pt=11) + 1

    ws.merge_cells(start_row=r, end_row=r, start_column=COL_N, end_column=COL_A)
    ws.cell(row=r, column=COL_N, value="Progress").font = f_qlabel
    r += 1
    ws.merge_cells(start_row=r, end_row=r, start_column=COL_N, end_column=COL_A)
    p = ws.cell(row=r, column=COL_N, value="— of — questions answered")
    p.font = Font(name=BODY, size=12, bold=True, color=BAND)
    ws.row_dimensions[r].height = 20
    ws._progress_cell = p.coordinate      # filled in once the question rows are known
    r += 1
    para(ws, r, "Updates as you type. Counts the answer cells only, not the coverage grid.",
         COL_N, COL_A, f_note)

    ws.sheet_properties.tabColor = "FF9AA5B1"
    setup_print(ws)
    return ws


# ================================================================ Questionnaire
def set_progress(instructions, answer_rows):
    """Point the counter at the answer cells by name.

    COUNTA over the whole column would also count the section header labels that
    live in E, so the count has to name the 17 cells.
    """
    refs = ",".join(f"Questionnaire!E{r}" for r in answer_rows)
    instructions[instructions._progress_cell] = (
        f'=COUNTA({refs}) & " of {len(answer_rows)} questions answered"')


def build_questionnaire(wb):
    ws = wb.create_sheet("Questionnaire")
    ws.sheet_view.showGridLines = False
    set_widths(ws)

    ws.merge_cells(start_row=1, end_row=1, start_column=COL_N, end_column=COL_A)
    ws.cell(row=1, column=COL_N, value="Compassus Home Health  ·  Capacity & Scheduling Platform"
            ).font = Font(name=BODY, size=10, bold=True, color=MUTED)
    ws.row_dimensions[1].height = 15

    ws.merge_cells(start_row=2, end_row=2, start_column=COL_N, end_column=COL_A)
    ws.cell(row=2, column=COL_N, value="Vendor Questionnaire").font = f_title
    ws.row_dimensions[2].height = 24
    ws.row_dimensions[3].height = 8

    for i, label in enumerate(("Vendor", "Completed by / date")):
        rr = 4 + i
        c = ws.cell(row=rr, column=COL_Q, value=label)
        c.font = f_hdr
        c.alignment = Alignment(horizontal="right", vertical="center")
        answer_cell(ws, rr, COL_A, 20)
    ws.row_dimensions[6].height = 8

    answer_rows, status_rows = [], []
    r = 7

    for key, title, framing, qs in C.SECTIONS:
        r = band_row(ws, r, f"{key}.   {title.upper()}")
        if framing:
            r = para(ws, r, framing, COL_N, COL_A, f_note)
        r = col_headers(ws, r, [(COL_N, "#"), (COL_Q, "QUESTION"), (COL_A, "YOUR ANSWER")])

        for qid, label, text in qs:
            n = ws.cell(row=r, column=COL_N, value=qid)
            n.font = f_qid
            n.alignment = A_TOP
            qc = ws.cell(row=r, column=COL_Q)
            qc.value = CellRichText(
                TextBlock(InlineFont(rFont=BODY, sz=11, b=True, color="1F2A37"), label + "\n"),
                TextBlock(InlineFont(rFont=BODY, sz=11, color="1F2A37"), text),
            )
            qc.alignment = A_WRAP
            h = max(answer_height(EXPECTED.get(qid, 110)),
                    block_height(ws, [(label + "\n", 11, True), (text, 11, False)],
                                 COL_Q, COL_Q, pad=8))
            answer_cell(ws, r, COL_A, h)
            answer_rows.append(r)
            r += 1
            ws.row_dimensions[r].height = 5
            r += 1

        if key == "A":
            r, srows = build_coverage(
                ws, r + 1, C.COVERAGE_STANDARD, "B.   COVERAGE SELF-ASSESSMENT",
                "Mark where you stand on each area, then use the notes column for anything you want "
                "us to understand — a partner delivering it, a caveat, or what “in development” "
                "actually means for you.")
            status_rows += srows
        r += 1

    ws._status_rows = status_rows
    ws.freeze_panes = "A3"        # title only — deliberately shallow so the reading field stays deep
    ws.print_title_rows = "1:2"
    ws.sheet_properties.tabColor = BAND
    setup_print(ws)
    return ws, answer_rows


def build_coverage(ws, r, coverage, band_text, intro):
    """Status grid — status in its own column, notes beside it. Returns (next_row, status_rows)."""
    r = band_row(ws, r, band_text)
    r = para(ws, r, intro, COL_N, COL_A, f_note)
    r = col_headers(ws, r, [(COL_N, "#"), (COL_Q, "AREA"),
                            (COL_S, "STATUS"), (COL_A, "NOTES")])
    n, status_rows = 0, []
    for module, rows in coverage:
        for col in range(COL_N, COL_A + 1):
            ws.cell(row=r, column=col).fill = PatternFill("solid", fgColor=TINT)
        ws.merge_cells(start_row=r, end_row=r, start_column=COL_N, end_column=COL_A)
        m = ws.cell(row=r, column=COL_N, value=module)
        m.font = Font(name=BODY, size=10.5, bold=True, color=BAND)
        m.alignment = Alignment(vertical="center", indent=1)
        ws.row_dimensions[r].height = 18
        r += 1
        for name, desc in rows:
            n += 1
            idc = ws.cell(row=r, column=COL_N, value=n)
            idc.font = f_qid
            idc.alignment = A_TOP
            qc = ws.cell(row=r, column=COL_Q)
            qc.value = CellRichText(
                TextBlock(InlineFont(rFont=BODY, sz=11, b=True, color="1F2A37"), name + "\n"),
                TextBlock(InlineFont(rFont=BODY, sz=10, color="5B6572"), desc),
            )
            qc.alignment = A_WRAP
            answer_cell(ws, r, COL_S)          # status — dropdown attaches here
            answer_cell(ws, r, COL_A)          # notes
            ws.row_dimensions[r].height = block_height(
                ws, [(name + "\n", 11, True), (desc, 10, False)], COL_Q, COL_Q, pad=10, floor=34)
            status_rows.append(r)
            r += 1
    return r, status_rows


def setup_print(ws, orientation="portrait"):
    ws.page_setup.orientation = orientation
    ws.page_setup.paperSize = ws.PAPERSIZE_A4
    ws.page_setup.fitToWidth = 1
    ws.page_setup.fitToHeight = 0
    ws.sheet_properties.pageSetUpPr.fitToPage = True   # required or fitTo* is ignored
    ws.print_options.horizontalCentered = True
    ws.page_margins.left = ws.page_margins.right = 0.4
    ws.page_margins.top = ws.page_margins.bottom = 0.55
    ws.oddFooter.left.text = "Compassus Home Health — Vendor Questionnaire"
    ws.oddFooter.right.text = "Page &P of &N"


# ================================================================ lists + validation
def add_lists(wb):
    lists = wb.create_sheet("Lists")
    for i, v in enumerate(C.STATUS_OPTIONS, start=1):
        lists.cell(row=i, column=1, value=v)
    lists.sheet_state = "hidden"
    wb.defined_names.add(DefinedName("StatusList",
                                     attr_text=f"Lists!$A$1:$A${len(C.STATUS_OPTIONS)}"))
    return lists


def attach_status_validation(ws, rows, col=COL_S):
    if not rows:
        return
    dv = DataValidation(
        type="list",
        formula1="StatusList",       # NO leading "=" — written verbatim into <formula1>
        allow_blank=True,
        showDropDown=False,          # INVERTED: False => the arrow IS shown
        showInputMessage=True,
        promptTitle="Select status",
        prompt="Production · In development · Roadmap · Not offered",
        showErrorMessage=False,
    )
    ws.add_data_validation(dv)       # MUST precede dv.add()
    letter = {4: "D", 5: "E"}[col]
    for r in rows:
        dv.add(f"{letter}{r}")


def protect(ws):
    ws.protection.sheet = True
    ws.protection.password = "review"
    # INVERTED THROUGHOUT: False = ALLOWED, True = forbidden
    ws.protection.selectLockedCells = False
    ws.protection.selectUnlockedCells = False   # or nobody can type
    ws.protection.formatCells = False
    ws.protection.formatRows = False            # or long answers get clipped with no recourse
    for flag in ("formatColumns", "insertRows", "deleteRows", "insertColumns",
                 "deleteColumns", "sort", "autoFilter", "objects", "scenarios"):
        setattr(ws.protection, flag, True)


# ================================================================ internal sheets
def build_expanded(wb):
    ws = wb.create_sheet("Coverage — Expanded")
    ws.sheet_view.showGridLines = False
    set_widths(ws)
    ws.merge_cells(start_row=2, end_row=2, start_column=COL_N, end_column=COL_A)
    ws.cell(row=2, column=COL_N, value="Coverage self-assessment — expanded").font = f_title
    ws.row_dimensions[2].height = 22
    para(ws, 3,
         "An optional deeper version of the Part B grid, rolled up from the variable inventory's own "
         "subcategories. Use this instead of the 10-row grid if we decide we want more granularity. "
         "It does not expose the numbered inventory itself.",
         COL_N, COL_A, f_note)
    r, rows = build_coverage(ws, 5, C.COVERAGE_EXPANDED, "COVERAGE — EXPANDED",
                             "Same four options as the standard grid.")
    ws.freeze_panes = "A5"
    ws.sheet_properties.tabColor = "FF6B7C93"
    setup_print(ws)
    return ws, rows


def build_additional(wb):
    ws = wb.create_sheet("Additional Questions")
    ws.sheet_view.showGridLines = False
    set_widths(ws)
    ws.merge_cells(start_row=2, end_row=2, start_column=COL_N, end_column=COL_A)
    ws.cell(row=2, column=COL_N, value="Additional questions — held for follow-up").font = f_title
    ws.row_dimensions[2].height = 22
    para(ws, 3,
         "Internal. Drafted, judged valuable, and deliberately kept out of round one so the "
         "questionnaire stays answerable. Most of these need a screen, a follow-up or a tone of "
         "voice to be worth anything — which is what the virtual calls are for.",
         COL_N, COL_A, f_note)
    r = 5
    for group, items in C.ADDITIONAL:
        r = band_row(ws, r, group.upper())
        for i, q in enumerate(items, start=1):
            idc = ws.cell(row=r, column=COL_N, value=i)
            idc.font = f_qid
            idc.alignment = A_TOP
            ws.merge_cells(start_row=r, end_row=r, start_column=COL_Q, end_column=COL_A)
            c = ws.cell(row=r, column=COL_Q, value=q)
            c.font = f_q
            c.alignment = A_WRAP
            ws.row_dimensions[r].height = block_height(ws, [(q, 11, False)], COL_Q, COL_A, pad=8)
            r += 1
        r += 1
    ws.freeze_panes = "A5"
    ws.sheet_properties.tabColor = "FF8C7A5B"
    setup_print(ws)
    return ws


def build_vetting(wb):
    ws = wb.create_sheet("Vetting — For Leaders")
    ws.sheet_view.showGridLines = False
    set_widths(ws, [("A", 2.5), ("B", 26), ("C", 62), ("D", 46), ("E", 2.5)])
    ws.merge_cells("B2:D2")
    ws["B2"] = "Vetting questions — for review with leadership"
    ws["B2"].font = f_title
    ws.row_dimensions[2].height = 22
    para(ws, 3, C.VETTING_NOTE, 2, 4, f_note)
    r = 5
    r = band_row(ws, r, "SET ASIDE FROM ROUND ONE", c1=2, c2=4)
    r = col_headers(ws, r, [(2, "TOPIC"), (3, "QUESTION AS DRAFTED"), (4, "WHY IT IS SET ASIDE")])
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
            block_height(ws, [(q, 11, False)], 3, 3, pad=10, floor=36),
            block_height(ws, [(why, 10.5, False)], 4, 4, pt=10.5, pad=10))
        r += 1
    ws.freeze_panes = "A7"
    ws.sheet_properties.tabColor = "FF7A4E4E"
    setup_print(ws, "landscape")
    return ws


def build_meta(wb, audience):
    ws = wb.create_sheet("Meta")
    for i, (k, v) in enumerate([("form_version", "2026-08-19"), ("audience", audience),
                                ("issued_by", "Compassus Home Health"),
                                ("question_ids", ",".join(EXPECTED.keys()))], start=1):
        ws.cell(row=i, column=1, value=k)
        ws.cell(row=i, column=2, value=v)
    ws.sheet_state = "hidden"
    return ws
