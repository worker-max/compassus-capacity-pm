# -*- coding: utf-8 -*-
"""Capacity & Scheduling business case model — live formulas, editable drivers."""
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation

BLUE = Font(name="Arial", size=10, color="0000FF")          # editable input
BLACK = Font(name="Arial", size=10)                          # formula
GREEN = Font(name="Arial", size=10, color="008000")          # cross-sheet link
BOLD = Font(name="Arial", size=10, bold=True)
H1 = Font(name="Arial", size=14, bold=True)
H2 = Font(name="Arial", size=11, bold=True, color="FFFFFF")
NOTE = Font(name="Arial", size=9, italic=True, color="595959")
HDRFILL = PatternFill("solid", fgColor="1F3864")
FLAG = PatternFill("solid", fgColor="FFFF00")
SUBFILL = PatternFill("solid", fgColor="D9E2F3")
THIN = Border(bottom=Side(style="thin", color="BFBFBF"))

CUR = '$#,##0;($#,##0);-'
CUR2 = '$#,##0.0,,"M";($#,##0.0,,"M");-'
PCT = '0.0%'
NUM = '#,##0'

wb = openpyxl.Workbook()


def hdr(ws, row, cols, labels):
    for c, lab in zip(cols, labels):
        cell = ws.cell(row=row, column=c, value=lab)
        cell.font = H2
        cell.fill = HDRFILL
        cell.alignment = Alignment(horizontal="center", wrap_text=True)


def section(ws, row, text, width=6):
    c = ws.cell(row=row, column=1, value=text)
    c.font = BOLD
    for i in range(1, width + 1):
        ws.cell(row=row, column=i).fill = SUBFILL


# ────────────────────────────────────────────────────────────── README
ws = wb.active
ws.title = "README"
ws.column_dimensions["A"].width = 22
ws.column_dimensions["B"].width = 95
ws["A1"] = "Capacity & Scheduling — Business Case Model"
ws["A1"].font = H1
rows = [
    ("Purpose", "Size the initiative from editable drivers rather than from a fixed conclusion. Change any blue cell and every downstream number moves."),
    ("", ""),
    ("Color legend", "BLUE = an input you may edit.  BLACK = a formula, do not overwrite.  GREEN = a link to another sheet.  YELLOW FILL = unresolved or invented, must be replaced before external use."),
    ("", ""),
    ("Sheets", "Inputs — every driver, with source and confidence.  Levers — the seven value levers, min/mod/max.  Cost — three-year cost of ownership.  Summary — net position, payback, and the waterfall.  Baseline — what must be measured before any of this is committed."),
    ("", ""),
    ("Scenario", "Two independent selectors on Inputs: B60 sets the BENEFIT scenario, B63 sets the COST scenario. They are deliberately separate — an ambitious benefit case does not require an ambitious spend case, and the honest question is usually Mod benefit against Max cost. Levers always shows all three columns."),
    ("", ""),
    ("Conventions", "Where the 8.13 workbook has an assumption, this model uses it, so the two reconcile. Where it does not, the source is named on the Inputs sheet."),
    ("", ""),
    ("Two attribution rules", "1. Admissions and routine-visit throughput are SEPARATE pools — SOC-capable clinicians versus paraprofessionals — and are additive, not double counted.  2. Routine throughput is valued on the NON-EPISODIC book only. Above the LUPA floor an extra episodic visit earns nothing."),
    ("", ""),
    ("Health warning", "Three inputs are unresolved and are marked yellow: network admissions per year, episodic period count, and annual mileage spend. The admissions lever scales linearly with the first. Do not present externally until they are replaced with actuals."),
]
r = 3
for a, b in rows:
    ws.cell(row=r, column=1, value=a).font = BOLD
    c = ws.cell(row=r, column=2, value=b)
    c.font = BLACK
    c.alignment = Alignment(wrap_text=True, vertical="top")
    ws.row_dimensions[r].height = 30 if b else 8
    r += 1

# ────────────────────────────────────────────────────────────── INPUTS
ws = wb.create_sheet("Inputs")
for col, w in zip("ABCDEF", (46, 16, 12, 40, 14, 30)):
    ws.column_dimensions[col].width = w
ws["A1"] = "Inputs — every driver"
ws["A1"].font = H1
ws["A2"] = "Edit blue cells only. Yellow = unresolved, replace before external use."
ws["A2"].font = NOTE

section(ws, 4, "A.  ORGANIZATION AND SCALE")
hdr(ws, 5, [1, 2, 3, 4, 5], ["Driver", "Value", "Unit", "Source", "Confidence"])
org = [
    ("Branches", 80, "count", "8.13 workbook, ROI tab", "Good"),
    ("Field clinicians", 3000, "count", "Whiteboard session 13 Aug", "Good"),
    ("Share of clinicians paid per visit", 0.70, "%", "Colin, 26 Aug", "Given"),
    ("Schedulers today", 300, "count", "Whiteboard session 13 Aug", "Stated"),
    ("Home health revenue", 549000000, "$", "Coding business case, upside panel", "Good"),
    ("Medicare fee-for-service revenue", 260000000, "$", "Coding business case, VBP lever (HHVBP base)", "Good"),
]
r = 6
for name, val, unit, src, conf in org:
    ws.cell(row=r, column=1, value=name).font = BLACK
    c = ws.cell(row=r, column=2, value=val); c.font = BLUE
    c.number_format = PCT if unit == "%" else (CUR if unit == "$" else NUM)
    ws.cell(row=r, column=3, value=unit).font = BLACK
    ws.cell(row=r, column=4, value=src).font = NOTE
    ws.cell(row=r, column=5, value=conf).font = NOTE
    r += 1
ws.cell(row=r, column=1, value="All other payer revenue").font = BLACK
c = ws.cell(row=r, column=2, value="=B10-B11"); c.font = BLACK; c.number_format = CUR
ws.cell(row=r, column=3, value="$").font = BLACK
ws.cell(row=r, column=4, value="Derived").font = NOTE
r += 1

unresolved = [
    ("Admissions per year, all branches (new starts of care)", 48000, "count",
     "600/branch x 80 (workbook). UNRESOLVED: cannot carry $549M", "Weak"),
    ("Medicare 30-day payment periods per year, all branches", 80000, "count",
     "1,000/branch x 80 (workbook). Derived alternative is 128,000", "Weak"),
    ("Total visits per year", 3000000, "count", "Estimate: 3,000 clinicians x ~1,000 visits", "Weak"),
    ("Non-episodic visits per year", 1900000, "count", "Estimate from non-FFS revenue", "Weak"),
]
for name, val, unit, src, conf in unresolved:
    ws.cell(row=r, column=1, value=name).font = BLACK
    c = ws.cell(row=r, column=2, value=val); c.font = BLUE; c.number_format = NUM; c.fill = FLAG
    ws.cell(row=r, column=3, value=unit).font = BLACK
    ws.cell(row=r, column=4, value=src).font = NOTE
    ws.cell(row=r, column=5, value=conf).font = NOTE
    r += 1

section(ws, 18, "B.  UNIT ECONOMICS")
hdr(ws, 19, [1, 2, 3, 4, 5], ["Driver", "Value", "Unit", "Source", "Confidence"])
econ = [
    ("Margin per additional admission (revenue less variable cost)", 1200, "$", "8.13 workbook", "Workbook", False),
    ("Revenue protected per avoided LUPA", 1400, "$", "8.13 workbook", "Workbook", False),
    ("Contribution per non-episodic visit", 65, "$", "Derived: ~$150 revenue less per-visit pay and variable", "Modeled", False),
    ("Loaded cost per scheduler", 60000, "$", "BLS home health scheduler $38,090 median x 1.43", "Good", False),
    ("Replacement cost per clinician", 40000, "$", "8.13 workbook", "Workbook", False),
    ("Clinician departures per branch per year (all causes)", 5, "count", "8.13 workbook", "Workbook", False),
    ("Premium labor spend per branch per year (contract, per diem, overtime)", 120000, "$", "8.13 workbook", "Workbook", False),
    ("Annual mileage spend, network", 16000000, "$", "INVENTED: 3,000 x 8,000 miles x $0.67. Replace", "Invented", True),
]
r = 20
for name, val, unit, src, conf, flag in econ:
    ws.cell(row=r, column=1, value=name).font = BLACK
    c = ws.cell(row=r, column=2, value=val); c.font = BLUE
    c.number_format = CUR if unit == "$" else NUM
    if flag:
        c.fill = FLAG
    ws.cell(row=r, column=3, value=unit).font = BLACK
    ws.cell(row=r, column=4, value=src).font = NOTE
    ws.cell(row=r, column=5, value=conf).font = NOTE
    r += 1

section(ws, 30, "C.  SCENARIO DRIVERS")
hdr(ws, 31, [1, 2, 3, 4, 5], ["Driver", "Min", "Mod", "Max", "Basis"])
drivers = [
    ("Increase in admissions", 0.02, 0.04, 0.07, PCT, "LeanTaaS 2% acute; field service 4-15%"),
    ("Fill-rate percentage points recovered (non-episodic)", 0.01, 0.02, 0.035, PCT, "Industry fill rates 88-90%"),
    ("LUPA reduction, points of periods", 0.005, 0.01, 0.02, PCT, "8.13 workbook scenario drivers"),
    ("Scheduler FTE released", 27, 60, 90, NUM, "Vendor comparable 27-44; bottom-up build 90"),
    ("Share of premium labor converted to planned coverage", 0.15, 0.30, 0.50, PCT, "8.13 workbook scenario drivers"),
    ("Clinician turnover reduction", 0.05, 0.10, 0.20, PCT, "8.13 workbook; Bergman 9.2pp worst quartile"),
    ("Travel and mileage reduction", 0.05, 0.08, 0.12, PCT, "Field service 5-15%; UPS ORION 8-10%"),
]
r = 32
for name, lo, mo, hi, fmt, basis in drivers:
    ws.cell(row=r, column=1, value=name).font = BLACK
    for col, v in zip((2, 3, 4), (lo, mo, hi)):
        c = ws.cell(row=r, column=col, value=v); c.font = BLUE; c.number_format = fmt
    ws.cell(row=r, column=5, value=basis).font = NOTE
    r += 1

section(ws, 41, "D.  COST OF OWNERSHIP DRIVERS")
hdr(ws, 42, [1, 2, 3, 4, 5], ["Driver", "Min", "Mod", "Max", "Basis"])
costs = [
    ("Implementation and integration (one-time)", 1000000, 3400000, 8000000),
    ("Data readiness (one-time)", 500000, 1300000, 4000000),
    ("Go-live productivity dip (one-time)", 400000, 1000000, 3000000),
    ("Software license (per year)", 400000, 720000, 1500000),
    ("Internal program labor (per year)", 1200000, 3300000, 7000000),
    ("Change management (per year)", 350000, 830000, 2200000),
    ("Run and support (per year)", 220000, 350000, 700000),
]
r = 43
for name, lo, mo, hi in costs:
    ws.cell(row=r, column=1, value=name).font = BLACK
    for col, v in zip((2, 3, 4), (lo, mo, hi)):
        c = ws.cell(row=r, column=col, value=v); c.font = BLUE; c.number_format = CUR
    r += 1
ws.cell(row=50, column=5, value="License is ~10% of total; internal labor ~42%").font = NOTE

section(ws, 52, "E.  BENEFIT RAMP")
hdr(ws, 53, [1, 2, 3, 4, 5], ["Driver", "Year 1", "Year 2", "Year 3", "Basis"])
ws.cell(row=54, column=1, value="Share of steady-state benefit realized").font = BLACK
for col, v in zip((2, 3, 4), (0.20, 0.60, 1.00)):
    c = ws.cell(row=54, column=col, value=v); c.font = BLUE; c.number_format = PCT
ws.cell(row=54, column=5, value="Phased rollout across ~80 branches").font = NOTE
ws.cell(row=55, column=1, value="Outside-view benefit haircut").font = BLACK
c = ws.cell(row=55, column=2, value=0.00); c.font = BLUE; c.number_format = PCT
ws.cell(row=55, column=5, value="Set to 56% to apply the McKinsey-Oxford shortfall").font = NOTE

section(ws, 58, "F.  SCENARIO SELECTOR")
ws.cell(row=59, column=1, value="Scenario driving the Summary sheet").font = BOLD
c = ws.cell(row=60, column=1, value="Selected scenario"); c.font = BLACK
c = ws.cell(row=60, column=2, value="Mod"); c.font = BLUE
c.fill = PatternFill("solid", fgColor="FFF2CC")
dv = DataValidation(type="list", formula1='"Min,Mod,Max"', allow_blank=False)
ws.add_data_validation(dv)
dv.add(ws["B60"])
ws.cell(row=61, column=1, value="Column index (1=Min, 2=Mod, 3=Max)").font = BLACK
c = ws.cell(row=61, column=2, value='=MATCH(B60,{"Min","Mod","Max"},0)'); c.font = BLACK
ws.cell(row=61, column=5, value="Used by INDEX on the Levers pick").font = NOTE

c = ws.cell(row=63, column=1, value="Selected COST scenario"); c.font = BLACK
c = ws.cell(row=63, column=2, value="Mod"); c.font = BLUE
c.fill = PatternFill("solid", fgColor="FFF2CC")
dv2 = DataValidation(type="list", formula1='"Min,Mod,Max"', allow_blank=False)
ws.add_data_validation(dv2)
dv2.add(ws["B63"])
ws.cell(row=64, column=1, value="Cost column index").font = BLACK
c = ws.cell(row=64, column=2, value='=MATCH(B63,{"Min","Mod","Max"},0)'); c.font = BLACK
ws.cell(row=63, column=5, value="Set independently of the benefit scenario. An ambitious benefit case does not require an ambitious spend case").font = NOTE

# ────────────────────────────────────────────────────────────── LEVERS
ws = wb.create_sheet("Levers")
for col, w in zip("ABCDEF", (44, 16, 16, 16, 52, 10)):
    ws.column_dimensions[col].width = w
ws["A1"] = "Value levers — annual, at steady state"
ws["A1"].font = H1
ws["A2"] = "Gross of platform cost. Formulas reference Inputs; edit drivers there, not here."
ws["A2"].font = NOTE
hdr(ws, 4, [1, 2, 3, 4, 5], ["Lever", "Min", "Mod", "Max", "Formula in words"])

levers = [
    ("1  Speed to answer -> admissions (SOC-capable pool)",
     "=Inputs!$B$13*Inputs!{c}32*Inputs!$B$20",
     "Admissions x lift x contribution per admission"),
    ("2  Routine throughput and fill rate (paraprofessional pool)",
     "=Inputs!$B$16*Inputs!{c}33*Inputs!$B$22",
     "Non-episodic visits x fill points x contribution per visit"),
    ("3  LUPA as a scheduling gear",
     "=Inputs!$B$14*Inputs!{c}34*Inputs!$B$21",
     "Periods x reduction points x revenue protected"),
    ("4  Scheduler capacity released",
     "=Inputs!{c}35*Inputs!$B$23",
     "FTE released x loaded cost"),
    ("5  Premium and contract labor recovered",
     "=Inputs!$B$6*Inputs!$B$26*Inputs!{c}36",
     "Branches x premium pool x recovery rate"),
    ("6  Clinician retention",
     "=Inputs!$B$6*Inputs!$B$25*Inputs!{c}37*Inputs!$B$24",
     "Branches x departures x reduction x replacement cost"),
    ("7  Travel and mileage",
     "=Inputs!$B$27*Inputs!{c}38",
     "Mileage spend x reduction rate"),
]
r = 5
for name, f, words in levers:
    ws.cell(row=r, column=1, value=name).font = BLACK
    for col, letter in zip((2, 3, 4), ("$B$", "$C$", "$D$")):
        cell = ws.cell(row=r, column=col, value=f.replace("{c}", letter))
        cell.font = GREEN
        cell.number_format = CUR
    ws.cell(row=r, column=5, value=words).font = NOTE
    ws.cell(row=r, column=1).border = THIN
    r += 1

ws.cell(row=r, column=1, value="TOTAL, gross of platform cost").font = BOLD
for col in (2, 3, 4):
    cell = ws.cell(row=r, column=col,
                   value=f"=SUM({get_column_letter(col)}5:{get_column_letter(col)}{r-1})")
    cell.font = BOLD
    cell.number_format = CUR
TOTROW = r

r += 2
ws.cell(row=r, column=1, value="NOT YET VALUED — future-year case").font = BOLD
r += 1
ws.cell(row=r, column=1, value="8  Clinician attraction (recruiting advantage)").font = BLACK
for col in (2, 3, 4):
    c = ws.cell(row=r, column=col, value="Not yet valued"); c.font = NOTE
ws.cell(row=r, column=5, value="Two mechanisms: the day-before confirmation burden moves off the clinician, and income becomes predictable. Both are recruiting arguments, not just retention ones").font = NOTE
r += 1
ws.cell(row=r, column=1, value="9  Hospice extension of the same instrument").font = BLACK
for col in (2, 3, 4):
    c = ws.cell(row=r, column=col, value="Not yet valued"); c.font = NOTE
ws.cell(row=r, column=5, value="The 8.13 workbook states four hospice mechanics need rules added, not new products").font = NOTE
r += 1
ws.cell(row=r, column=1, value="10  Authorization write-offs avoided").font = BLACK
for col in (2, 3, 4):
    c = ws.cell(row=r, column=col, value="Unmeasured"); c.font = NOTE
ws.cell(row=r, column=5, value="Visits delivered outside the payer backdating window. Could be immaterial or the largest single lever").font = NOTE

r += 2
ws.cell(row=r, column=1, value="Attribution notes").font = BOLD
notes = [
    "Levers 1 and 2 are separate capacity pools — SOC-capable clinicians and paraprofessionals — and are additive.",
    "Lever 2 is valued on the non-episodic book only. Above the LUPA floor an extra episodic visit earns no revenue.",
    "Lever 3 recovers only clinically indicated visits lost to operational failure. It never adds a visit to clear a threshold.",
    "Lever 7 counts mileage reimbursement only. Under per-visit pay the saved drive time accrues to the clinician, and converts to capacity in lever 1.",
    "Lever 4 excludes severance, which sits on the Cost sheet.",
]
for n in notes:
    r += 1
    ws.cell(row=r, column=1, value="- " + n).font = NOTE

# ────────────────────────────────────────────────────────────── COST
ws = wb.create_sheet("Cost")
for col, w in zip("ABCDE", (44, 16, 16, 16, 16)):
    ws.column_dimensions[col].width = w
ws["A1"] = "Cost of ownership — three years"
ws["A1"].font = H1
ws["A2"] = "Scenario follows the selector on Inputs B60."
ws["A2"].font = NOTE
hdr(ws, 4, [1, 2, 3, 4, 5], ["Cost line", "Year 1", "Year 2", "Year 3", "Three-year total"])

cost_rows = [
    ("Implementation and integration", 43, True),
    ("Data readiness", 44, True),
    ("Go-live productivity dip", 45, True),
    ("Software license", 46, False),
    ("Internal program labor", 47, False),
    ("Change management", 48, False),
    ("Run and support", 49, False),
]
r = 5
for name, src, one_time in cost_rows:
    ws.cell(row=r, column=1, value=name).font = BLACK
    pick = f"INDEX(Inputs!$B${src}:$D${src},Inputs!$B$64)"
    ws.cell(row=r, column=2, value=f"={pick}").font = GREEN
    if one_time:
        ws.cell(row=r, column=3, value=0).font = BLACK
        ws.cell(row=r, column=4, value=0).font = BLACK
    else:
        ws.cell(row=r, column=3, value=f"={pick}").font = GREEN
        ws.cell(row=r, column=4, value=f"={pick}").font = GREEN
    ws.cell(row=r, column=5, value=f"=SUM(B{r}:D{r})").font = BLACK
    for col in range(2, 6):
        ws.cell(row=r, column=col).number_format = CUR
    r += 1

ws.cell(row=r, column=1, value="Severance on released scheduler roles").font = BLACK
ws.cell(row=r, column=2, value=0).font = BLUE
ws.cell(row=r, column=3, value="=INDEX(Inputs!$B$35:$D$35,Inputs!$B$61)*Inputs!$B$23*0.25").font = GREEN
ws.cell(row=r, column=4, value=0).font = BLACK
ws.cell(row=r, column=5, value=f"=SUM(B{r}:D{r})").font = BLACK
for col in range(2, 6):
    ws.cell(row=r, column=col).number_format = CUR
ws.cell(row=r, column=6, value="Assumes 3 months per released role, in year 2").font = NOTE
r += 1

ws.cell(row=r, column=1, value="TOTAL COST").font = BOLD
for col in range(2, 6):
    cell = ws.cell(row=r, column=col,
                   value=f"=SUM({get_column_letter(col)}5:{get_column_letter(col)}{r-1})")
    cell.font = BOLD
    cell.number_format = CUR
COSTROW = r

# ────────────────────────────────────────────────────────────── SUMMARY
ws = wb.create_sheet("Summary")
for col, w in zip("ABCDE", (44, 16, 16, 16, 16)):
    ws.column_dimensions[col].width = w
ws["A1"] = "Summary — net position and payback"
ws["A1"].font = H1
ws["A2"] = '=CONCATENATE("Benefit scenario: ",Inputs!B60,"    |    Cost scenario: ",Inputs!B63)'
ws["A2"].font = BOLD

hdr(ws, 4, [1, 2, 3, 4, 5], ["", "Year 1", "Year 2", "Year 3", "Three-year total"])
ws.cell(row=5, column=1, value="Steady-state benefit, gross").font = BLACK
for col in (2, 3, 4):
    ws.cell(row=5, column=col,
            value=f"=INDEX(Levers!$B${TOTROW}:$D${TOTROW},Inputs!$B$61)").font = GREEN
    ws.cell(row=5, column=col).number_format = CUR

ws.cell(row=6, column=1, value="Ramp").font = BLACK
for col, src in zip((2, 3, 4), ("B", "C", "D")):
    ws.cell(row=6, column=col, value=f"=Inputs!${src}$54").font = GREEN
    ws.cell(row=6, column=col).number_format = PCT

ws.cell(row=7, column=1, value="Outside-view haircut").font = BLACK
for col in (2, 3, 4):
    ws.cell(row=7, column=col, value="=Inputs!$B$55").font = GREEN
    ws.cell(row=7, column=col).number_format = PCT

ws.cell(row=8, column=1, value="Benefit realized").font = BOLD
for col in (2, 3, 4):
    L = get_column_letter(col)
    ws.cell(row=8, column=col, value=f"={L}5*{L}6*(1-{L}7)").font = BOLD
    ws.cell(row=8, column=col).number_format = CUR
ws.cell(row=8, column=5, value="=SUM(B8:D8)").font = BOLD
ws.cell(row=8, column=5).number_format = CUR

ws.cell(row=9, column=1, value="Total cost").font = BLACK
for col in (2, 3, 4, 5):
    L = get_column_letter(col)
    ws.cell(row=9, column=col, value=f"=Cost!{L}{COSTROW}").font = GREEN
    ws.cell(row=9, column=col).number_format = CUR

ws.cell(row=10, column=1, value="NET").font = BOLD
for col in (2, 3, 4, 5):
    L = get_column_letter(col)
    ws.cell(row=10, column=col, value=f"={L}8-{L}9").font = BOLD
    ws.cell(row=10, column=col).number_format = CUR

ws.cell(row=11, column=1, value="Cumulative net").font = BLACK
ws.cell(row=11, column=2, value="=B10").font = BLACK
ws.cell(row=11, column=3, value="=B11+C10").font = BLACK
ws.cell(row=11, column=4, value="=C11+D10").font = BLACK
for col in (2, 3, 4):
    ws.cell(row=11, column=col).number_format = CUR

ws.cell(row=13, column=1, value="Three-year ROI").font = BOLD
ws.cell(row=13, column=2, value="=IF(E9=0,0,E10/E9)").font = BOLD
ws.cell(row=13, column=2).number_format = PCT
ws.cell(row=14, column=1, value="Payback").font = BOLD
ws.cell(row=14, column=2,
        value='=IF(D11>0,IF(C11>0,IF(B11>0,"Year 1","Year 2"),"Year 3"),"Beyond year 3")').font = BOLD

ws.cell(row=16, column=1, value="Steady-state annual benefit, by lever (selected scenario)").font = BOLD
r = 17
for i in range(7):
    ws.cell(row=r, column=1, value=f"=Levers!A{5+i}").font = BLACK
    ws.cell(row=r, column=2,
            value=f"=INDEX(Levers!$B${5+i}:$D${5+i},Inputs!$B$61)").font = GREEN
    ws.cell(row=r, column=2).number_format = CUR
    r += 1
ws.cell(row=r, column=1, value="Total").font = BOLD
ws.cell(row=r, column=2, value=f"=SUM(B17:B{r-1})").font = BOLD
ws.cell(row=r, column=2).number_format = CUR

r += 2
ws.cell(row=r, column=1, value="Read this before quoting a number").font = BOLD
for n in [
    "State the four attribution conventions with any figure: gross or incremental; which revenue base; how many levers; whether config-achievable value counts.",
    "Set the outside-view haircut on Inputs B55 to 56% to see the McKinsey-Oxford expected case.",
    "Three inputs are unresolved and marked yellow. The admissions lever scales linearly with network admissions.",
]:
    r += 1
    ws.cell(row=r, column=1, value="- " + n).font = NOTE

# ────────────────────────────────────────────────────────────── BASELINE
ws = wb.create_sheet("Baseline")
for col, w in zip("ABCDEFG", (34, 40, 22, 26, 14, 40, 14)):
    ws.column_dimensions[col].width = w
ws["A1"] = "Baseline measurement plan"
ws["A1"].font = H1
ws["A2"] = "Nothing in this model can be committed until these are measured. Ordered by which lever they gate."
ws["A2"].font = NOTE
hdr(ws, 4, [1, 2, 3, 4, 5, 6, 7],
    ["KPI", "What it measures", "Gates which lever", "Source system", "Available today", "How to obtain", "Effort"])

base = [
    ("Network admissions per year", "The denominator for every growth claim", "Lever 1", "HCHB / Commure", "Yes",
     "Count SOC and ROC episodes by branch, 12 months", "Low"),
    ("Referral-to-SOC latency", "Hours from referral acceptance to SOC visit, median and tail", "Lever 1", "Commure + HCHB", "Partial",
     "Timestamp pairs: referral accepted, auth cleared, intake approved, welcome call, SOC scheduled, SOC delivered", "Medium"),
    ("Referral turn-down rate for capacity", "Clinically appropriate referrals declined for lack of capacity", "Lever 1", "Referral log", "No",
     "Requires a turn-down reason code that does not exist today", "High"),
    ("SOC slot utilization", "SOC-capable capacity offered versus filled, per week", "Lever 1", "HCHB scheduling", "No",
     "Needs a definition of an SOC slot before it can be counted", "High"),
    ("Visit fill rate", "Authorized and needed visits that go unstaffed, split episodic and non-episodic", "Lever 2", "HCHB", "Partial",
     "Scheduled versus completed versus canceled, by payer class", "Medium"),
    ("Visit mix by discipline", "RN vs LPN, PT vs PTA, OT vs COTA, aide share of routine visits", "Levers 2 and 5", "HCHB", "Yes",
     "Visit counts by discipline code, 12 months", "Low"),
    ("Cancellation and refusal rate", "Frequency, timing, reason, and who absorbs the cost", "Lever 2", "HCHB dispositions", "Partial",
     "Disposition records; reason codes are captured for some dispositions but not decline", "Medium"),
    ("Backfill latency", "Time from a cancellation to the slot being refilled or lost", "Lever 2", "HCHB", "No",
     "Derived from disposition and reassignment timestamps", "Medium"),
    ("LUPA rate and periods one visit short", "Share of periods below threshold, and how many missed by one", "Lever 3", "Billing / PDGM", "Partial",
     "Claims by case-mix group against the CMS 432-row threshold file", "Medium"),
    ("LUPA cause attribution", "Whether the shortfall was clinical or operational", "Lever 3", "HCHB + billing", "No",
     "Join LUPA periods to missed, rescheduled and auth-held visits", "High"),
    ("Scheduler task census", "Task volume and real handle time by task type", "Lever 4", "HCHB workflow records", "Yes",
     "90 days of workflow items with open and close timestamps, grouped by type. This is a query, not a study", "Low"),
    ("Premium, contract and overtime spend", "Baseline for the labor recovery lever", "Lever 5", "Payroll", "Yes",
     "12 months by branch and discipline", "Low"),
    ("Clinician turnover and tenure at separation", "Departures, first-year share, replacement cost", "Lever 6", "Workday", "Yes",
     "Voluntary and involuntary, 24 months, with tenure", "Low"),
    ("Schedule volatility", "Coefficient of variation of daily visit count, trailing 28 days, per clinician", "Lever 6", "HCHB", "No",
     "Computable today from visit records. Validated predictor of quit risk", "Low"),
    ("Income realization ratio", "Realized pay against quoted pay at 90 days, per new hire", "Lever 6", "Payroll + recruiting", "No",
     "Join offer expectations to actual pay. Critical with 70% per-visit pay", "Medium"),
    ("Mileage and drive time", "Miles and drive hours per visit, by branch", "Lever 7", "HCHB / expense", "Partial",
     "Replaces the invented mileage figure on Inputs", "Medium"),
    ("Authorization write-offs", "Visits delivered outside the payer backdating window", "Not yet a lever", "Billing", "No",
     "The most under-instrumented dollar in the business. Could be immaterial or the largest single lever", "High"),
    ("Authorization turnaround by payer", "Submission to response, by payer and product", "Not yet a lever", "Auth team", "No",
     "Measurable from existing data. Nobody has measured it", "Medium"),
    ("Pay model split", "Per visit, hourly, salaried, points, by branch", "Every margin lever", "Payroll", "Yes",
     "Confirms the 70% figure and locates the exceptions", "Low"),
    ("Time to fill by discipline", "Days from requisition to accepted offer", "Attraction case (future)", "Workday", "Yes",
     "12 months by discipline and branch. Baseline for the recruiting argument", "Low"),
    ("Offer acceptance rate", "Offers accepted as a share of offers made", "Attraction case (future)", "Workday", "Yes",
     "With decline reasons where captured", "Low"),
    ("Cost per hire", "Recruiting spend per accepted hire, by discipline", "Attraction case (future)", "Finance / HR", "Partial",
     "Needed to value faster filling", "Medium"),
    ("Exit reason codes", "Why leavers say they left, coded consistently", "Levers 6 and attraction", "Workday", "Partial",
     "Distinguishes schedule and income causes from everything else", "Medium"),
    ("Cost per period by case-mix group", "The denominator for the utilization ceiling", "Utilization work", "Finance", "No",
     "Without it the ceiling stays directional", "High"),
]
r = 5
for row in base:
    for i, v in enumerate(row, start=1):
        c = ws.cell(row=r, column=i, value=v)
        c.font = BLACK if i != 6 else NOTE
        c.alignment = Alignment(wrap_text=True, vertical="top")
        if i == 5 and v == "No":
            c.fill = FLAG
    ws.row_dimensions[r].height = 28
    r += 1

r += 1
ws.cell(row=r, column=1, value="Sequencing").font = BOLD
for n in [
    "Everything marked Low effort is a query against systems we already own and can be delivered in two weeks.",
    "The scheduler task census, pay model split, visit mix, turnover and premium spend together size five of the seven levers.",
    "By the organization's own KPI table the initiative's core metric — quantified capacity and utilization — is not available today, along with 6 of 8 secondary indicators.",
]:
    r += 1
    ws.cell(row=r, column=1, value="- " + n).font = NOTE


# ────────────────────────────────────────────────────────────── DEFINITIONS
ws = wb.create_sheet("Definitions")
for col, w in zip("ABC", (46, 78, 34)):
    ws.column_dimensions[col].width = w
ws["A1"] = "Definitions — every term used in this model"
ws["A1"].font = H1
ws["A2"] = "If a term is not defined here it should not be in the model."
ws["A2"].font = NOTE
hdr(ws, 4, [1, 2, 3], ["Term", "What it means, in plain language", "Why it matters"])

defs = [
    ("Admissions per year, all branches",
     "Every new patient started on service across all 80 branches in a year. A start of care, not a visit and not a referral. One admission generates an episode, which generates one or more payment periods.",
     "It is the denominator for the growth lever. The current figure is unresolved and marked yellow."),
    ("Margin per additional admission",
     "The money left over from one more admission after paying the variable costs of delivering it: clinician visit pay, mileage, supplies. It is NOT revenue, and it excludes fixed overhead the branch pays anyway.",
     "Growth is only worth what it contributes after variable cost. The workbook uses $1,200."),
    ("Increase in admissions",
     "The percentage more admissions we take because capacity is visible and the yes or no arrives faster. 4 percent on 48,000 admissions is about 1,900 more starts a year.",
     "Requires referral supply to exist. We currently decline referrals for lack of capacity, so it does."),
    ("Premium labor",
     "Anything paid above the standard rate to get a visit covered: contract and agency clinicians, per diem or PRN at premium rates, overtime, and incentive pay for picking up extra visits. Contract employees are the most expensive tier of it.",
     "It is bought reactively today because nobody can see who has room. Forward visibility converts reactive premium coverage into planned coverage."),
    ("Share of premium labor converted",
     "The portion of that premium spend that could have been covered by someone already on the payroll with room in their week, had we been able to see it in time.",
     "Not all premium labor is avoidable. Genuine gaps still need contract cover."),
    ("Fill rate",
     "Of the visits that are authorized and clinically needed, the share that actually get staffed and delivered. Industry runs 88 to 90 percent.",
     "The gap is revenue on the non-episodic book. Under episodic payment an unfilled routine visit above the floor costs almost nothing."),
    ("Episodic payment",
     "Traditional Medicare. A fixed, case-mix adjusted amount for a 30-day period regardless of how many visits are delivered above the floor.",
     "Visits are cost, not revenue. About 47 percent of our book."),
    ("Non-episodic payment",
     "Managed care, commercial and Medicaid. Payment follows the delivered visit or unit, usually with prior authorization and often against an annual cap.",
     "Visits are revenue. About 53 percent of our book."),
    ("LUPA",
     "Low Utilization Payment Adjustment. If a 30-day period falls below its case-mix group threshold, 2 to 5 visits, the entire period reprices to national per-visit amounts instead of the full period rate.",
     "A cliff of roughly $1,400, not a gradient. Recovery is legitimate only where the visit was clinically indicated and lost to an operational failure."),
    ("SOC-capable capacity",
     "Clinicians qualified and available to admit a new patient, which is a smaller pool than clinicians available for routine visits.",
     "It is the binding constraint on growth. A branch can have routine capacity and still be unable to admit."),
    ("Paraprofessional pool",
     "LPNs, PTAs, COTAs and aides, who carry the bulk of weekly routine visit volume.",
     "A separate capacity pool from admissions. Their throughput never produces an admission, so the two levers are additive."),
    ("Contribution per non-episodic visit",
     "Revenue for one visit under a per-visit contract, less what we pay the clinician for it and other variable costs. Modeled at $65.",
     "The value of each visit recovered through better fill rate."),
    ("Steady state",
     "The annual benefit once the program is fully deployed across all branches, before ramp. Year 3 in this model.",
     "Year 1 and 2 are discounted by the ramp on the Inputs sheet."),
    ("Outside-view haircut",
     "A discount applied to the whole benefit case to reflect that large technology programs typically deliver materially less than predicted. Set it to 56 percent to see the published expected case.",
     "Lets the expected case be shown next to the promised case rather than instead of it."),
    ("Benefit scenario vs cost scenario",
     "Two independent selectors. Benefit sets how ambitious the value assumptions are; cost sets how expensive the program is assumed to be.",
     "An ambitious benefit case does not require an ambitious spend case. At maximum on both, the program is net negative."),
]
r = 5
for term, meaning, why in defs:
    ws.cell(row=r, column=1, value=term).font = BOLD
    for col, v in ((2, meaning), (3, why)):
        c = ws.cell(row=r, column=col, value=v)
        c.font = BLACK if col == 2 else NOTE
        c.alignment = Alignment(wrap_text=True, vertical="top")
    ws.cell(row=r, column=1).alignment = Alignment(wrap_text=True, vertical="top")
    ws.row_dimensions[r].height = 58
    r += 1

for s in wb.worksheets:
    s.sheet_view.showGridLines = False

out = r"C:\Users\chigh\flowbuild\Capacity-Scheduling-Business-Case-Model.xlsx"
wb.save(out)
print("saved", out)
