#!/usr/bin/env python3
"""
Generates `Vendor-Scorecard-SIMPLE.xlsx` — the backup scorecard.

A deliberate reset. Where the main workbook scores 41 elements and 12 judgement items, this
scores the 11 areas the vendor already self-assessed in Section B, plus HCHB. Two marks per
area: what they have (Status) and how good it is (Rating 0-100).

It follows the shape of the Functional Scorecard in the primary workbook — Status, Rating,
Comments, with Footprint and Coverage rolling up automatically — so it reads like something
the team has seen before.

    python3 _simple-scorecard.gen.py [out.xlsx]
"""
import os
import sys

from openpyxl import Workbook
from openpyxl.formatting.rule import ColorScaleRule
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "Vendor-Scorecard-SIMPLE.xlsx")

INK, MUTED, RULE, PAPER, BAND = "1B211E", "5A6560", "C9CCC5", "FBFBF8", "E9E9E5"
CAP, SCH, ENG = "1F6F78", "2E599D", "4E8A5B"
GOLD, MAROON = "C6A01F", "792E2E"

N_VENDORS = 16
FIRST_COL = 4
VCOLS = [get_column_letter(c) for c in range(FIRST_COL, FIRST_COL + N_VENDORS)]

# Status wording is the vendor's own Section B dropdown, so scoring is mostly transcription.
STATUSES = [
    ("Production — multiple customers", 100),
    ("Production — one customer", 100),
    ("Through a partner", 100),
    ("In development — dated", 100),
    ("Roadmap — no date", 100),
    ("Not available", 0),
]
IN_PRODUCTION = ["Production — multiple customers", "Production — one customer"]
REACHED = [s for s, _ in STATUSES if s != "Not available"]

HCHB_STATUS = [
    ("Live — reads and writes, multiple customers", 25),
    ("Live — one customer, or one-way", 20),
    ("Live — via a partner or flat file / screen automation", 12),
    ("In development — dated", 6),
    ("Roadmap — no date", 2),
    ("None, and no path", 0),
]

AREAS = [
    ("CAP", "Capacity Management", CAP, [
        ("1", "Workforce supply", "Roster, disciplines, roles, competencies, ramp, float pool"),
        ("2", "Availability & reach", "Availability and time off, territory, drive-time reachability"),
        ("3", "The capacity math", "Visit weighting, targets and ceilings, committed load vs. open room")]),
    ("SCH", "Scheduling Engine", SCH, [
        ("4", "Demand", "Ingesting ordered visits, authorization, readiness, compliance windows"),
        ("5", "Matching", "Discipline and competency fit, clinician and patient needs, clinical timing, continuity"),
        ("6", "Routing & the week", "Routing, sequencing, front-loading, week balancing"),
        ("7", "Exceptions", "Missed visits, call-outs, reassignment, coverage, rebooking")]),
    ("ENG", "Engagement", ENG, [
        ("8", "Before the visit", "Welcome call, availability capture, reminders, confirmation, en-route"),
        ("9", "When plans change", "Reschedule, coverage coordination and clinician outreach, urgent same-day needs"),
        ("10", "Incentives & offers", "Surfacing hard-to-fill visits to clinicians, and any incentive attached"),
        ("11", "Across the care team", "Multi-discipline coordination, clinician and office updates")]),
]

RATING_BANDS = [
    ("90–100", "Proven at scale", "They gave us numbers — a named customer, a period, a baseline."),
    ("70–89", "Mechanism explained", "We can see how it decides, not just that it exists."),
    ("50–69", "Described", "We can picture the feature. Most answers land here."),
    ("25–49", "Asserted", "They say they do it. Nothing behind it."),
    ("1–24", "Barely touches it", "Adjacent, or a fragment of what we asked for."),
    ("blank", "Not available", "Leave the rating empty. Status carries it."),
]

thin = Side(style="thin", color=RULE)
med = Side(style="medium", color=INK)
BORDER = Border(thin, thin, thin, thin)
LEFT = Alignment(horizontal="left", vertical="center", wrap_text=True)
LEFT_T = Alignment(horizontal="left", vertical="top", wrap_text=True)
CTR = Alignment(horizontal="center", vertical="center", wrap_text=True)
RIGHT = Alignment(horizontal="right", vertical="center")


def F(sz=10, b=False, color=INK, italic=False):
    return Font(name="Aptos Narrow", size=sz, bold=b, color=color, italic=italic)


def put(ws, cell, value, font=None, align=None, fillc=None, border=None, fmt=None):
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
    if fmt:
        c.number_format = fmt
    return c


def band(ws, row, text, colour, last, height=21):
    ws.row_dimensions[row].height = height
    ws.merge_cells(f"B{row}:{last}{row}")
    put(ws, f"B{row}", text, F(9, True, "FFFFFF"),
        Alignment(horizontal="left", vertical="center", indent=1), colour)


def main():
    wb = Workbook()
    last = VCOLS[-1]

    # ════════════════════════════════════════════════════ 1 · START HERE
    gs = wb.active
    gs.title = "Start Here"
    gs.sheet_view.showGridLines = False
    gs.sheet_properties.tabColor = GOLD
    for col, w in [("A", 4), ("B", 34), ("C", 13), ("D", 104)]:
        gs.column_dimensions[col].width = w

    put(gs, "B2", "COMPASSUS  ·  HOME HEALTH", F(9, True, MUTED))
    gs.row_dimensions[3].height = 32
    put(gs, "B3", "Vendor Scorecard — Simple", F(20, True, INK))
    gs.merge_cells("B4:D4")
    put(gs, "B4", "The backup. Twelve rows a vendor, two marks each. Roughly three minutes per "
                  "questionnaire.", F(10, False, MUTED, italic=True), LEFT)

    rows = [
        ("gap", "", "", ""),
        ("band", "WHAT THIS IS", "", ""),
        ("para", "", "", "The same judgement as the full scorecard, at a coarser grain. Instead of 41 elements "
                         "and 12 questions, you mark the 11 areas the vendor already self-assessed in Section B of the "
                         "questionnaire — plus HCHB integration."),
        ("para", "", "", "Use it when you want a fast read across the field, when two people need to compare "
                         "quickly, or when the full sheet is more precision than a decision needs. Use the full scorecard "
                         "when the shortlist is close and you have to defend the order."),
        ("gap", "", "", ""),
        ("band", "THE TWO MARKS", "", ""),
        ("row", "Status", "grid 1", "WHAT THEY HAVE. Copy it from their own Section B answer — it uses the same "
                                    "words. Where Section C contradicts Section B, believe Section C."),
        ("row", "Rating  0–100", "grid 2", "HOW GOOD IT IS, from what they wrote. Leave it blank where the status "
                                           "is Not available."),
        ("row", "Notes", "grid 3", "One line. What decides this vendor, or what you could not tell."),
        ("gap", "", "", ""),
        ("band", "RATING — WHAT THE NUMBERS MEAN", "", ""),
    ]
    rows += [("row", lo, hi, d) for lo, hi, d in RATING_BANDS]
    rows += [
        ("gap", "", "", ""),
        ("band", "WHAT THE SHEET WORKS OUT", "", ""),
        ("row", "Footprint %", "", "How many of the 11 areas the product reaches at all — any status except "
                                   "Not available. How much of what we care about it even touches."),
        ("row", "In production %", "", "How many of those 11 are live with customers today, rather than promised."),
        ("row", "Average rating", "", "Across the areas they reach. Blank areas do not drag it down — Footprint "
                                      "already carries that."),
        ("row", "Per-arena rating", "", "Capacity, Scheduling and Engagement separately. Which arena a vendor owns "
                                        "tells us more than the average does."),
        ("gap", "", "", ""),
        ("band", "HOW TO READ IT", "", ""),
        ("para", "", "", "Footprint and rating answer different questions, and a vendor can be strong on one and "
                         "weak on the other. High footprint with a low rating is a product that touches everything "
                         "shallowly. Low footprint with a high rating is a specialist — often the more interesting "
                         "conversation, and worth a differentiator note rather than a dismissal."),
        ("para", "", "", "HCHB sits at the top of the grid on its own, because it is the one thing leadership named "
                         "as a priority. A vendor with no HCHB path is a conditional advance whatever else they score: "
                         "advancing them means accepting an integration still to be built, on their timeline, at our risk."),
        ("gap", "", "", ""),
        ("band", "WHAT THIS CANNOT DO", "", ""),
        ("para", "", "", "It cannot separate two vendors who both cover an area but do it very differently — that is "
                         "exactly what the full scorecard's 41 elements and evidence ladder are for. It has no partnership "
                         "or clinician-adoption score, so Section D and Section E do not reach the number at all; read them "
                         "and put what matters in Notes. And like the full sheet, it scores a questionnaire, not a product."),
    ]

    gr = 6
    for kind, a, b, c in rows:
        if kind == "gap":
            gs.row_dimensions[gr].height = 10
        elif kind == "band":
            gs.row_dimensions[gr].height = 22
            gs.merge_cells(f"B{gr}:D{gr}")
            put(gs, f"B{gr}", a, F(9, True, "FFFFFF"),
                Alignment(horizontal="left", vertical="center", indent=1), INK)
        elif kind == "para":
            gs.merge_cells(f"B{gr}:D{gr}")
            gs.row_dimensions[gr].height = 15 + 13 * (len(c) // 150)
            put(gs, f"B{gr}", c, F(10, False, INK), LEFT_T)
        else:
            gs.row_dimensions[gr].height = max(24, 13 * (1 + len(c) // 115) + 10)
            put(gs, f"B{gr}", a, F(10, False, INK), LEFT_T)
            put(gs, f"C{gr}", b, F(10, True, GOLD), CTR)
            put(gs, f"D{gr}", c, F(9, False, MUTED), LEFT_T)
        gr += 1
    put(gs, f"B{gr + 1}", "Backup scorecard v1.0  ·  areas per questionnaire Section B, "
                          "form_version 2026-08-19", F(9, False, MUTED, italic=True))

    # ════════════════════════════════════════════════════ 2 · SCORECARD
    ws = wb.create_sheet("Scorecard")
    ws.sheet_view.showGridLines = False
    ws.sheet_properties.tabColor = INK
    ws.column_dimensions["A"].width = 4
    ws.column_dimensions["B"].width = 30
    ws.column_dimensions["C"].width = 52
    for cl in VCOLS:
        ws.column_dimensions[cl].width = 13

    put(ws, "B2", "COMPASSUS  ·  HOME HEALTH", F(9, True, MUTED))
    ws.row_dimensions[3].height = 26
    put(ws, "B3", "Vendor Scorecard — Simple", F(18, True, INK))
    ws.merge_cells(f"B4:{last}4")
    put(ws, "B4", "Grid 1 is what they have · grid 2 is how good it is · grid 3 is why. "
                  "Everything above the grids is a formula.", F(9, False, MUTED, italic=True), LEFT)

    r = 6
    ws.row_dimensions[r].height = 42
    put(ws, f"B{r}", "VENDOR", F(9, True, MUTED), Alignment(horizontal="left", vertical="bottom"))
    for i, cl in enumerate(VCOLS, 1):
        put(ws, f"{cl}{r}", f"Vendor {i:02d}", F(10, True, INK),
            Alignment(horizontal="center", vertical="bottom", wrap_text=True), PAPER,
            Border(bottom=med))
    r += 2

    # ── summary ──
    band(ws, r, "SUMMARY", INK, last)
    r += 1
    summary = {}
    for label, hint, colour in [
        ("HCHB integration", "the priority", GOLD),
        ("Footprint %", "of the 11 areas, reached at all", INK),
        ("In production %", "live with customers today", INK),
        ("Average rating", "across areas reached", INK),
        ("Capacity", "avg rating, 3 areas", CAP),
        ("Scheduling", "avg rating, 4 areas", SCH),
        ("Engagement", "avg rating, 4 areas", ENG),
    ]:
        ws.row_dimensions[r].height = 19
        put(ws, f"B{r}", label, F(10, label in ("Footprint %", "HCHB integration"), colour), LEFT)
        put(ws, f"C{r}", hint, F(9, False, MUTED), RIGHT)
        summary[label] = r
        r += 1
    r += 1

    # ── grid 1 · status ──
    band(ws, r, "1  ·  STATUS   —   what they have.  Copy it from their Section B answer.", INK, last)
    r += 1
    ws.row_dimensions[r].height = 22
    put(ws, f"B{r}", "HCHB integration", F(10, True, GOLD), LEFT, "FBF6E4")
    put(ws, f"C{r}", "Question A1 — the leadership priority", F(9, False, "8A7220"), RIGHT, "FBF6E4")
    for cl in VCOLS:
        put(ws, f"{cl}{r}", None, F(9), CTR, "FFFDF4", BORDER)
    HCHB_ROW = r
    r += 1
    status_rows, arena_status = {}, {}
    for aid, aname, colour, areas in AREAS:
        ws.row_dimensions[r].height = 18
        ws.merge_cells(f"B{r}:{last}{r}")
        put(ws, f"B{r}", f"{aname.upper()}   ·   {len(areas)} areas", F(9, True, "FFFFFF"),
            Alignment(horizontal="left", vertical="center", indent=1), colour)
        r += 1
        arena_status[aid] = []
        for num, name, desc in areas:
            ws.row_dimensions[r].height = 17
            put(ws, f"B{r}", f"{num}   {name}", F(10, False, INK), LEFT)
            put(ws, f"C{r}", desc, F(9, False, MUTED), LEFT)
            for cl in VCOLS:
                put(ws, f"{cl}{r}", None, F(9), CTR, PAPER, BORDER)
            status_rows[num] = r
            arena_status[aid].append(r)
            r += 1
    r += 1

    # ── grid 2 · rating ──
    band(ws, r, "2  ·  RATING   —   how good it is, 0–100.  Blank where the status is Not available.",
         INK, last)
    r += 1
    rating_rows, arena_rating = {}, {}
    for aid, aname, colour, areas in AREAS:
        ws.row_dimensions[r].height = 18
        ws.merge_cells(f"B{r}:{last}{r}")
        put(ws, f"B{r}", aname.upper(), F(9, True, "FFFFFF"),
            Alignment(horizontal="left", vertical="center", indent=1), colour)
        r += 1
        arena_rating[aid] = []
        for num, name, desc in areas:
            ws.row_dimensions[r].height = 17
            put(ws, f"B{r}", f"{num}   {name}", F(10, False, INK), LEFT)
            put(ws, f"C{r}", "90+ proven · 70+ mechanism · 50+ described · 25+ asserted",
                F(9, False, MUTED), RIGHT)
            for cl in VCOLS:
                put(ws, f"{cl}{r}", None, F(9), CTR, PAPER, BORDER, "0")
            rating_rows[num] = r
            arena_rating[aid].append(r)
            r += 1
    r += 1

    # ── grid 3 · notes ──
    band(ws, r, "3  ·  NOTES   —   one line.  What decides this vendor, or what you could not tell.",
         MAROON, last)
    r += 1
    for label, height in [("What stands out", 66), ("What worries me", 66),
                          ("What I could not tell", 66)]:
        ws.row_dimensions[r].height = height
        put(ws, f"B{r}", label, F(10, True, MAROON), LEFT_T)
        for cl in VCOLS:
            put(ws, f"{cl}{r}", None, F(9), LEFT_T, PAPER, BORDER)
        r += 1
    LAST_ROW = r

    # ── formulas ──
    reached = ",".join(f'"{s}"' for s in REACHED)
    prod = ",".join(f'"{s}"' for s in IN_PRODUCTION)
    all_status = [status_rows[n] for n in status_rows]
    all_rating = [rating_rows[n] for n in rating_rows]
    for cl in VCOLS:
        put(ws, f"{cl}{summary['HCHB integration']}",
            f"=IF({cl}{HCHB_ROW}=\"\",\"—\",{cl}{HCHB_ROW})",
            F(9, True, GOLD), CTR, BAND, BORDER)
        n_reached = "+".join(f'IF(OR({cl}{rr}={{{reached}}}),1,0)' for rr in all_status)
        n_prod = "+".join(f'IF(OR({cl}{rr}={{{prod}}}),1,0)' for rr in all_status)
        put(ws, f"{cl}{summary['Footprint %']}", f"=({n_reached})/{len(all_status)}",
            F(11, True, INK), CTR, BAND, BORDER, "0%")
        put(ws, f"{cl}{summary['In production %']}", f"=({n_prod})/{len(all_status)}",
            F(10, False, MUTED), CTR, BAND, BORDER, "0%")
        rng = ",".join(f"{cl}{rr}" for rr in all_rating)
        put(ws, f"{cl}{summary['Average rating']}", f"=IFERROR(AVERAGE({rng}),0)",
            F(11, True, INK), CTR, BAND, BORDER, "0")
        for aid, label in [("CAP", "Capacity"), ("SCH", "Scheduling"), ("ENG", "Engagement")]:
            cells = ",".join(f"{cl}{rr}" for rr in arena_rating[aid])
            put(ws, f"{cl}{summary[label]}", f"=IFERROR(AVERAGE({cells}),0)",
                F(10, False, {"CAP": CAP, "SCH": SCH, "ENG": ENG}[aid]), CTR, BAND, BORDER, "0")

    # ── validation ──
    dv_hchb = DataValidation(type="list", formula1="=Lists!$B$2:$B$7", allow_blank=True,
                             showDropDown=False, promptTitle="HCHB integration",
                             prompt="From A1. Ambiguous? Take the lower line and say so in Notes.")
    dv_st = DataValidation(type="list", formula1="=Lists!$D$2:$D$7", allow_blank=True,
                           showDropDown=False, promptTitle="Status",
                           prompt="What they have. Their own Section B wording. Section C wins where they differ.")
    dv_rt = DataValidation(type="whole", operator="between", formula1=0, formula2=100,
                           allow_blank=True, promptTitle="Rating 0–100",
                           prompt="90+ proven with numbers · 70+ mechanism explained · 50+ described "
                                  "· 25+ asserted · blank if not available.",
                           error="Ratings run 0 to 100. Leave it blank if the area is not available.")
    for dv in (dv_hchb, dv_st, dv_rt):
        ws.add_data_validation(dv)
    dv_hchb.add(f"{VCOLS[0]}{HCHB_ROW}:{last}{HCHB_ROW}")
    for rr in all_status:
        dv_st.add(f"{VCOLS[0]}{rr}:{last}{rr}")
    for rr in all_rating:
        dv_rt.add(f"{VCOLS[0]}{rr}:{last}{rr}")

    # ── conditional formatting ──
    for rr, hi in [(summary["Footprint %"], "DDEBE0"), (summary["In production %"], "DDEBE0")]:
        ws.conditional_formatting.add(f"{VCOLS[0]}{rr}:{last}{rr}", ColorScaleRule(
            start_type="num", start_value=0, start_color="FFFFFF",
            end_type="num", end_value=1, end_color=hi))
    for label, colour in [("Average rating", "1B211E"), ("Capacity", CAP),
                          ("Scheduling", SCH), ("Engagement", ENG)]:
        ws.conditional_formatting.add(f"{VCOLS[0]}{summary[label]}:{last}{summary[label]}",
                                      ColorScaleRule(start_type="num", start_value=0,
                                                     start_color="FFFFFF", end_type="num",
                                                     end_value=100, end_color=colour))
    for rr in all_rating:
        ws.conditional_formatting.add(f"{VCOLS[0]}{rr}:{last}{rr}", ColorScaleRule(
            start_type="num", start_value=0, start_color="F7E6E6",
            mid_type="num", mid_value=55, mid_color="FBF3DD",
            end_type="num", end_value=95, end_color="DDEBE0"))

    ws.freeze_panes = f"{VCOLS[0]}7"
    ws.sheet_view.zoomScale = 90

    # ════════════════════════════════════════════════════ 3 · LISTS
    ls = wb.create_sheet("Lists")
    ls.sheet_state = "hidden"
    put(ls, "B1", "HCHB", F(9, True, MUTED))
    for i, (label, _) in enumerate(HCHB_STATUS, start=2):
        ls[f"B{i}"] = label
    put(ls, "D1", "Status", F(9, True, MUTED))
    for i, (label, _) in enumerate(STATUSES, start=2):
        ls[f"D{i}"] = label
    ls.column_dimensions["B"].width = 46
    ls.column_dimensions["D"].width = 34

    wb.active = 0
    wb.save(OUT)
    print(f"wrote {OUT}")
    print(f"  Scorecard rows 6–{LAST_ROW} · 12 status rows · 11 rating rows · {N_VENDORS} vendors")


if __name__ == "__main__":
    main()
