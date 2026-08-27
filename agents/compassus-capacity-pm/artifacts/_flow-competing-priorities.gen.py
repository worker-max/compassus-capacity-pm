# -*- coding: utf-8 -*-
"""Every Patient Visit — the givens, the decision, and the result.

Foundation sheet for the patient-scheduling engagement maps. Canvas units = points.

Three tiers, because the eight scheduling priorities are not peers: most are fixed before
anyone opens a calendar, a few are genuinely chosen, and one is only ever measured. Inside
each tier, blocks run left to right from what a system already holds to what only a person
holds. Variable counts and the in-system / tacit tags come from the workbook inventory.
"""
import sys
import textwrap

C = dict(pcc="#C6A01F", hchb="#795CA7", dcs="#792E2E", clin="#2E599D",
         auth="#DF751D", intake="#1F6F78", lead="#1A1A1A", pat="#4E8A5B")
INK, MUT, RULE, BAND = "#1B211E", "#5A6560", "#C9CCC5", "#E9E9E5"
PAPER, ENG, ENGD = "#FBFBF8", "#A6E22E", "#5F8A12"

W, H = 2600, 1660
out = []
def add(s): out.append(s)
def esc(t): return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

def lbl(x, y, t, anchor="start", cls="lb"):
    add(f'<text x="{x}" y="{y}" class="{cls}" text-anchor="{anchor}">{esc(t)}</text>')

def block(x, y, w, h, fill, lines, small=False, badge=None, tc="#fff", bc=None):
    add(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="5" fill="{fill}"/>')
    lh = 15.5 if small else 19
    cls = "bt s" if small else "bt"
    cy = y + h/2 - (len(lines)-1)*lh/2 + (5 if small else 6)
    for i, ln in enumerate(lines):
        add(f'<text x="{x+w/2}" y="{cy+i*lh}" class="{cls}" style="fill:{tc}" '
            f'text-anchor="middle">{esc(ln)}</text>')
    if badge:
        bw = 8.3*len(badge)+18
        add(f'<rect x="{x+w-bw-8}" y="{y-14}" width="{bw}" height="23" rx="11.5" fill="#FFFFFF" '
            f'stroke="{bc or fill}" stroke-width="1.8"/>')
        add(f'<text x="{x+w-bw/2-8}" y="{y+2}" class="bdg" text-anchor="middle" '
            f'fill="{bc or fill}">{esc(badge)}</text>')

def sublist(x, y, items):
    for i, t in enumerate(items):
        lbl(x, y+i*17, "· " + t, cls="sub")

add(f'<svg viewBox="0 0 {W} {H}" role="img" xmlns="http://www.w3.org/2000/svg">')
add(f'<rect width="{W}" height="{H}" fill="{PAPER}"/>')
add('<style>'
    '.chp{font-family:var(--mono),monospace;font-size:12.5px;font-weight:700;'
    'letter-spacing:.04em;fill:#fff}'
    '.xs{font-family:var(--mono),monospace;font-size:15px;font-weight:700;fill:#792E2E}'
    '.kh{font-family:var(--body),sans-serif;font-size:14.5px;font-weight:700;fill:#1B211E}'
    '.tier{font-family:var(--mono),monospace;font-size:15px;font-weight:700;'
    'letter-spacing:.14em;fill:#1B211E}'
    '</style>')
add('<defs><marker id="ar" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" '
    'markerHeight="6" orient="auto-start-reverse">'
    f'<path d="M 0 0 L 10 5 L 0 10 z" fill="{INK}"/></marker>'
    '<marker id="arm" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" '
    'markerHeight="6" orient="auto">'
    f'<path d="M 0 0 L 10 5 L 0 10 z" fill="{MUT}"/></marker></defs>')

# ---------------- header ----------------
lbl(50, 62, "COMPASSUS HOME HEALTH  ·  PATIENT SCHEDULING  ·  FOUNDATION SHEET", cls="eyebrow")
lbl(50, 104, "Every Patient Visit", cls="title")
lbl(50, 132, "What is fixed before scheduling begins  ·  what is actually being decided  ·  "
             "what falls out of the decision", cls="deck")

lx = 1500
for nm, col in [("System / HCHB", C["hchb"]), ("Clinical order", C["dcs"]),
                ("Clinician", C["clin"]), ("Patient", C["pat"]),
                ("Scheduler", C["pcc"]), ("Branch", C["lead"])]:
    add(f'<circle cx="{lx}" cy="58" r="9" fill="{col}"/>')
    lbl(lx+16, 63, nm, cls="leg")
    lx += 8.6*len(nm) + 50
lbl(W-50, 104, "COLOUR = WHO OWNS THE TRUTH", "end", "colh")
lbl(W-50, 128, "COUNT = WORKBOOK VARIABLES BEHIND IT", "end", "key")
add(f'<line x1="50" y1="158" x2="{W-50}" y2="158" stroke="{RULE}" stroke-width="1.4"/>')

# ---------------- the one axis ----------------
BX0, BXW = 330, 2220
AXY = 206
lbl(BX0, AXY, "ALREADY IN A SYSTEM", cls="colhb")
lbl(BX0, AXY+20, "HCHB · Workday · the 485 — a tool can read it today", cls="sub")
lbl(BX0+BXW, AXY, "HELD BY ONE PERSON", "end", "pnl")
lbl(BX0+BXW, AXY+20, "tacit, patient-held — a tool can only ask for it", "end", "sub")
lbl(BX0+BXW/2, AXY+2, "EVERY ROW BELOW RUNS LEFT TO RIGHT ALONG THIS LINE", "middle", "key")
add(f'<line x1="{BX0}" y1="{AXY+40}" x2="{BX0+BXW-30}" y2="{AXY+40}" stroke="{MUT}" '
    f'stroke-width="1.6" marker-end="url(#arm)"/>')

# ---------------- the three tiers ----------------
TIERS = [
 ("THE GIVENS", "fixed before scheduling begins",
  "CHANGING ONE NEEDS A NEW ORDER, A PAYER DECISION, OR A CHANGE IN THE PATIENT'S LIFE",
  [(["Regulatory", "Timing"], C["hchb"], "3 VARS · ALL IN SYSTEM",
    ["SOC OASIS inside 48 hours", "The 5-day recert window", "Missed-visit documentation"]),
   (["Ordered", "Frequency"], C["dcs"], "3 VARS · IN THE 485",
    ["2x a week means 2x a week", "Changing it needs a new order",
     "Compliance window per discipline"]),
   (["MD Orders"], C["dcs"], "3 VARS · ALL HARD",
    ["Wound care every 3 days", "Labs before the MD visit", "Protocol-driven timing"]),
   (["Patient hard", "constraints"], C["pat"], "5 VARS · 4 TACIT · 0 IN SYSTEM",
    ["Dialysis · MD appointments", "Caregiver must be present", "Cognitive windows",
     "Day-of-week constraints"])],
  "Ordered frequency is an order, not a preference. Seeing a patient fewer times than "
  "ordered is a compliance problem, not a scheduling choice."),

 ("THE DECISION", "the only real degrees of freedom",
  "THIS IS THE WHOLE OF WHAT A SCHEDULER OR A CLINICIAN ACTUALLY CHOOSES",
  [(["Geography"], C["pcc"], "6 VARS · 4 COMPUTABLE",
    ["Drive time, not distance", "Zip · territory · home base", "Bridges · rivers · crossings"]),
   (["Which", "clinician"], C["dcs"], "4 VARS",
    ["Discipline / role match", "Specialty competency", "Continuity of care",
     "Around other disciplines"]),
   (["Which days inside", "the ordered window"], C["clin"], "3 VARS",
    ["Spread, not compressed", "Front-load vs the LUPA floor", "Day-by-day balancing"]),
   (["Who first when", "the week is tight"], C["clin"], "3 VARS · ALL TACIT",
    ["Who is unstable", "Hospitalisation risk", "Who can safely wait"]),
   (["What time inside", "the patient's window"], C["pat"], "5 VARS · 0 IN SYSTEM",
    ["“Can you come after lunch?”", "“Not first thing”", "A preferred time, no reason given"])],
  "The left of this row is already in a system. The right of it is held by one person "
  "and written down nowhere — and it is where the week is actually won or lost."),
]

TY = 288
for title, sub, right, blocks, note in TIERS:
    TH = 300
    add(f'<rect x="50" y="{TY}" width="{W-100}" height="{TH}" rx="10" fill="{BAND}"/>')
    lbl(72, TY+36, title, cls="tier")
    lbl(72, TY+58, sub, cls="sub")
    lbl(W-72, TY+36, right, "end", "bandhi")
    n = len(blocks)
    gap = 90 if n == 4 else 60
    bw = (BXW - (n-1)*gap) / n
    for i, (lines, col, tag, items) in enumerate(blocks):
        x = BX0 + i*(bw+gap)
        by = TY + 82
        block(x, by, bw, 70, col, lines)
        lbl(x+bw/2, by+88, tag, "middle", "trg")
        sublist(x, by+110, items)
    lbl(72, TY+TH-20, note, cls="hi")
    TY += TH + 26

# ---------------- the result ----------------
RH = 176
add(f'<rect x="50" y="{TY}" width="{W-100}" height="{RH}" rx="10" fill="none" '
    f'stroke="{C["lead"]}" stroke-width="2"/>')
lbl(72, TY+36, "THE RESULT", cls="tier")
lbl(72, TY+58, "derived, not chosen", cls="sub")
block(BX0, TY+30, 480, 70, C["lead"], ["Productivity"])
lbl(BX0+240, TY+118, "6 OF 8 ALREADY IN SYSTEM", "middle", "trg")
sublist(BX0, TY+140, ["Points · target · ceiling", "Committed load · pace vs schedule"])
lbl(BX0+560, TY+56, "Productivity is what is left after the givens are obeyed and the "
    "decision is made.", cls="kh")
lbl(BX0+560, TY+80, "It is measured, not selected — which is why pushing on it directly "
    "moves nothing. It moves when the decision row gets better information.", cls="sub")
lbl(BX0+560, TY+114, "Six of its eight variables are already in a system today. The "
    "constraint is not the data — it is that nobody sees the trade before the day is built.",
    cls="sub")
TY += RH + 30

# ---------------- the collisions ----------------
KH = 290
add(f'<rect x="50" y="{TY}" width="{W-100}" height="{KH}" rx="10" fill="none" '
    f'stroke="{C["dcs"]}" stroke-width="2"/>')
lbl(72, TY+36, "WHERE THE DECISION COLLIDES WITH ITSELF  —  six that happen every week", cls="pnl")
lbl(W-72, TY+36, "EACH ONE IS RESOLVED BY ONE PERSON, THE NIGHT BEFORE", "end", "bandhi")

COL = [
 (("Regulatory Timing", C["hchb"]), ("Geography", C["pcc"]),
  "SOC OASIS due in 48 hours, patient is 50 minutes out",
  "Someone drives it, or the assessment is late. There is no third option."),
 (("Patient window", C["pat"]), ("Geography", C["pcc"]),
  "The 2pm-only patient breaks the cluster",
  "The clinician absorbs the drive, or the patient waits a day."),
 (("Ordered Frequency", C["dcs"]), ("Care team", C["dcs"]),
  "PT and OT are both ordered 2x a week",
  "Both want the same two days. Whoever schedules first wins."),
 (("Who first", C["clin"]), ("Productivity", C["lead"]),
  "The unstable patient takes 90 minutes",
  "Same points as a 40-minute visit. The clinician simply runs late."),
 (("MD Orders", C["dcs"]), ("Patient constraints", C["pat"]),
  "Wound care every 3 days, caregiver only weekends",
  "Negotiated on the phone, agreed verbally, written down nowhere."),
 (("Ordered Frequency", C["dcs"]), ("Regulatory Timing", C["hchb"]),
  "3x a week ordered, recert visit lands the same week",
  "The LUPA floor, the order and the window all bind at once."),
]
cw = (W - 144 - 5*18) / 6
for i, ((a, ca), (b, cb), head, tail) in enumerate(COL):
    x = 72 + i*(cw+18)
    y = TY + 62
    add(f'<rect x="{x}" y="{y}" width="{cw}" height="26" rx="13" fill="{ca}"/>')
    lbl(x+cw/2, y+18, a, "middle", "chp")
    lbl(x+cw/2, y+50, "✕", "middle", "xs")
    add(f'<rect x="{x}" y="{y+58}" width="{cw}" height="26" rx="13" fill="{cb}"/>')
    lbl(x+cw/2, y+76, b, "middle", "chp")
    hl = textwrap.wrap(head, 27)
    for j, ln in enumerate(hl):
        lbl(x+cw/2, y+114+j*17, ln, "middle", "kh")
    base = y + 114 + len(hl)*17 + 10
    for j, ln in enumerate(textwrap.wrap(tail, 33)):
        lbl(x+cw/2, base+j*16, ln, "middle", "sub")
TY += KH + 34

# ---------------- today / the tool / next ----------------
add(f'<line x1="50" y1="{TY}" x2="{W-50}" y2="{TY}" stroke="{RULE}" stroke-width="1.4"/>')
lbl(72, TY+42, "TODAY", cls="trg")
block(190, TY+18, 640, 64, C["clin"],
      ["One clinician resolves all six — the night before,", "in their head, written down nowhere"],
      small=True)
lbl(190, TY+104, "the weekly logic is undocumented and entirely unassisted", cls="sub")

lbl(880, TY+42, "THE TOOL", cls="trg")
block(1010, TY+18, 700, 64, ENG,
      ["It shows the collision before the day is built, and prices",
       "both sides. The clinician still decides."], small=True, tc=INK, bc=ENGD)
lbl(1010, TY+104, "release 1 is visualisation only — seeing the trade is the whole of it", cls="sub")

lbl(1760, TY+42, "NEXT", cls="trg")
block(1860, TY+18, 690, 64, C["pcc"],
      ["Each collision becomes an engagement map: a named", "owner, a named moment, a named ask"],
      small=True)
lbl(1860, TY+104, "what this sheet exists to carry", cls="sub")

add(f'<line x1="50" y1="{H-58}" x2="{W-50}" y2="{H-58}" stroke="{RULE}" stroke-width="1.4"/>')
lbl(50, H-30, "FOUNDATION SHEET · patient scheduling · variable counts and in-system / tacit "
    "tags from the capacity & scheduling workbook inventory", cls="foot")
lbl(W-50, H-30, "Every patient visit", "end", "foot")
add('</svg>')

OUT = sys.argv[1] if len(sys.argv) > 1 else "competing.svg"
open(OUT, "w", encoding="utf-8").write("\n".join(out))
print("emitted", len(out), "| canvas", W, "x", H, "| last y", TY+104)
