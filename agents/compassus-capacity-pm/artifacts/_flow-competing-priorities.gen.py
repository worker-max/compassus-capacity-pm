# -*- coding: utf-8 -*-
"""Every Patient Visit — the eight competing priorities, replotted.

The source slide draws eight priorities as a symmetrical flower around one hub. Its own title
says they compete; its layout says they are equal, independent and interchangeable. They are
none of those. This sheet plots the same eight against the two axes that decide what actually
happens on a Tuesday, and names the collisions the flower has no room for.

Canvas units = points on the output sheet.
"""
import sys
import textwrap

C = dict(pcc="#C6A01F", hchb="#795CA7", dcs="#792E2E", clin="#2E599D",
         auth="#DF751D", intake="#1F6F78", lead="#1A1A1A", pat="#4E8A5B",
         float="#795933")
INK, MUT, RULE, BAND = "#1B211E", "#5A6560", "#C9CCC5", "#E9E9E5"
PAPER, ENG, ENGD = "#FBFBF8", "#A6E22E", "#5F8A12"

W, H = 2600, 1760
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

def sublist(x, y, items, cls="sub"):
    for i, t in enumerate(items):
        lbl(x, y+i*17, "· " + t, cls=cls)

add(f'<svg viewBox="0 0 {W} {H}" role="img" xmlns="http://www.w3.org/2000/svg">')
add(f'<rect width="{W}" height="{H}" fill="{PAPER}"/>')
add('<style>'
    '.chp{font-family:var(--mono),monospace;font-size:12.5px;font-weight:700;'
    'letter-spacing:.04em;fill:#fff}'
    '.xs{font-family:var(--mono),monospace;font-size:15px;font-weight:700;fill:#792E2E}'
    '.kh{font-family:var(--body),sans-serif;font-size:14.5px;font-weight:700;fill:#1B211E}'
    '</style>')
add('<defs><marker id="ar" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" '
    'markerHeight="6" orient="auto-start-reverse">'
    f'<path d="M 0 0 L 10 5 L 0 10 z" fill="{INK}"/></marker></defs>')

# ---------------- header ----------------
lbl(50, 62, "COMPASSUS HOME HEALTH  ·  PATIENT SCHEDULING  ·  FOUNDATION SHEET", cls="eyebrow")
lbl(50, 104, "Every Patient Visit", cls="title")
lbl(50, 132, "The eight competing priorities, replotted — because a flower cannot show a "
             "collision, and the collisions are the job", cls="deck")

lx = 1400
for nm, col in [("System / HCHB", C["hchb"]), ("Clinician", C["clin"]), ("DCS", C["dcs"]),
                ("Patient", C["pat"]), ("Geography", C["pcc"]), ("Branch", C["lead"])]:
    add(f'<circle cx="{lx}" cy="58" r="9" fill="{col}"/>')
    lbl(lx+16, 63, nm, cls="leg")
    lx += 8.6*len(nm) + 54
lbl(W-50, 104, "COLOUR = WHO OWNS THE TRUTH", "end", "colh")
lbl(W-50, 128, "SIZE = HOW MANY WORKBOOK VARIABLES SIT BEHIND IT", "end", "key")
add(f'<line x1="50" y1="158" x2="{W-50}" y2="158" stroke="{RULE}" stroke-width="1.4"/>')

# ================= band 1 · the plot =================
PY_, PH = 186, 940
add(f'<rect x="50" y="{PY_}" width="{W-100}" height="{PH}" rx="10" fill="{BAND}"/>')
lbl(72, PY_+34, "THE EIGHT, PLOTTED AGAINST THE TWO AXES THAT DECIDE TUESDAY", cls="band")
lbl(W-72, PY_+34, "THE FLOWER GAVE ALL EIGHT THE SAME SIZE AND THE SAME DISTANCE FROM THE MIDDLE",
    "end", "bandhi")

AX0, AY0 = 300, PY_+96          # plot origin (top-left of the field)
AW, AH = 1780, 700

# quadrant washes
add(f'<rect x="{AX0}" y="{AY0}" width="{AW/2}" height="{AH/2}" fill="#792E2E" opacity=".07"/>')
add(f'<rect x="{AX0+AW/2}" y="{AY0}" width="{AW/2}" height="{AH/2}" fill="{ENGD}" opacity=".07"/>')
add(f'<rect x="{AX0+AW/2}" y="{AY0+AH/2}" width="{AW/2}" height="{AH/2}" fill="{ENGD}" opacity=".14"/>')
add(f'<rect x="{AX0}" y="{AY0}" width="{AW}" height="{AH}" fill="none" stroke="{RULE}" stroke-width="1.6"/>')
add(f'<line x1="{AX0+AW/2}" y1="{AY0}" x2="{AX0+AW/2}" y2="{AY0+AH}" stroke="{RULE}" stroke-width="1.6"/>')
add(f'<line x1="{AX0}" y1="{AY0+AH/2}" x2="{AX0+AW}" y2="{AY0+AH/2}" stroke="{RULE}" stroke-width="1.6"/>')

# axes
add(f'<line x1="{AX0-40}" y1="{AY0}" x2="{AX0-40}" y2="{AY0+AH}" stroke="{INK}" '
    f'stroke-width="2" marker-start="url(#ar)"/>')
lbl(AX0-56, AY0+8, "CANNOT MOVE", "end", "colh")
lbl(AX0-56, AY0+28, "the schedule bends around it", "end", "sub")
lbl(AX0-56, AY0+AH-16, "MOVES FREELY", "end", "colh")
add(f'<line x1="{AX0}" y1="{AY0+AH+40}" x2="{AX0+AW}" y2="{AY0+AH+40}" stroke="{INK}" '
    f'stroke-width="2" marker-end="url(#ar)"/>')
lbl(AX0+4, AY0+AH+64, "THE TOOL CANNOT COMPUTE IT", cls="colh")
lbl(AX0+4, AY0+AH+84, "tacit, patient-held, low confidence", cls="sub")
lbl(AX0+AW-4, AY0+AH+64, "THE TOOL CAN COMPUTE IT", "end", "colh")
lbl(AX0+AW-4, AY0+AH+84, "in-system, derived, high confidence", "end", "sub")

# quadrant names
lbl(AX0+18, AY0+30, "THE HARD PART", cls="pnl")
lbl(AX0+18, AY0+50, "immovable, and no system holds it — this is the judgment", cls="sub")
lbl(AX0+AW-18, AY0+30, "THE FLOOR", "end", "colhb")
lbl(AX0+AW-18, AY0+50, "immovable, and already known — automate it and stop thinking", "end", "sub")
lbl(AX0+18, AY0+AH/2+30, "NOISE", cls="colh")
lbl(AX0+18, AY0+AH/2+50, "soft and unknowable — nothing to build here", cls="sub")
lbl(AX0+AW-18, AY0+AH/2+30, "THE LEVERS", "end", "colhb")
lbl(AX0+AW-18, AY0+AH/2+50, "movable and computable — where the tool earns its keep", "end", "sub")

# the eight. x, y are fractions of the field; n = variables behind it
ROW = {"a": 105/700, "b": 230/700, "c": 520/700}
P = [
 ("Patient Availability", ["Patient", "Availability"], C["pat"],  .14, ROW["a"], 10, "7 OF 10 HARD",
  ["Dialysis · MD appointments", "Caregiver must be present", "Cognitive windows",
   "“Not Mondays” · “not first thing”"]),
 ("MD Orders", ["MD Orders"], C["dcs"], .63, ROW["a"], 3, "ALL HARD",
  ["Wound care every 3 days", "Labs before the MD visit", "Protocol-driven timing"]),
 ("Regulatory Timing", ["Regulatory", "Timing"], C["hchb"], .87, ROW["a"], 4, "SYSTEM-HELD",
  ["SOC OASIS inside 48h", "The 5-day recert window", "Ordered-frequency compliance"]),
 ("Prioritize", ["Prioritize"], C["clin"], .28, ROW["b"], 3, "TACIT",
  ["Who is unstable", "Hospitalisation risk", "Who can safely wait"]),
 ("Care Team", ["Care Team"], C["dcs"], .44, ROW["b"], 5, "MIXED",
  ["Other disciplines' visits", "Supervisory dependency", "Discipline / role match"]),
 ("Frequency", ["Frequency"], C["clin"], .56, ROW["c"], 4, "MIXED",
  ["Spread, not compressed", "Front-load vs LUPA floor", "Day-by-day balancing"]),
 ("Geography", ["Geography"], C["pcc"], .735, ROW["c"], 7, "0 HARD · ALL COMPUTABLE",
  ["Drive time, not distance", "Zip · territory · home base", "Bridges · rivers · crossings"]),
 ("Productivity", ["Productivity"], C["lead"], .91, ROW["c"], 9, "6 OF 9 DERIVED",
  ["Points · target · ceiling", "Committed load", "Pace vs schedule"]),
]
for key, lines, col, fx, fy, n, tag, items in P:
    bw = 168 + n*7
    bh = 64
    cx = AX0 + fx*AW
    cy = AY0 + fy*AH
    x, y = cx - bw/2, cy - bh/2
    block(x, y, bw, bh, col, lines, badge=f"{n} VARS", bc=col)
    lbl(cx, y+bh+18, tag, "middle", "trg")
    sublist(x, y+bh+38, items)

lbl(72, PY_+PH-22, "Productivity is not the eighth priority — it is what is left after the other "
    "seven have taken their cut. Six of its nine variables are derived, not chosen.", cls="hi")

# ================= band 2 · the collisions =================
KY, KH = PY_ + PH + 46, 336
add(f'<rect x="50" y="{KY}" width="{W-100}" height="{KH}" rx="10" fill="none" '
    f'stroke="{C["dcs"]}" stroke-width="2"/>')
lbl(72, KY+34, "WHERE THEY ACTUALLY COLLIDE  —  the six the flower has no room for", cls="pnl")
lbl(W-72, KY+34, "EVERY ONE IS RESOLVED BY ONE PERSON, THE NIGHT BEFORE", "end", "bandhi")

COL = [
 (("Regulatory Timing", C["hchb"]), ("Geography", C["pcc"]),
  "The 48-hour SOC lands in the wrong zip",
  "Someone drives an hour, or the SOC is late. There is no third option."),
 (("Patient Availability", C["pat"]), ("Geography", C["pcc"]),
  "The 2pm-only patient breaks the cluster",
  "The clinician absorbs the drive, or the patient waits a day."),
 (("Care Team", C["dcs"]), ("Frequency", C["clin"]),
  "PT and OT both want Tuesday",
  "Two visits in one day, none on Thursday. Whoever schedules first wins."),
 (("Prioritize", C["clin"]), ("Productivity", C["lead"]),
  "The unstable patient takes 90 minutes",
  "Same points as a 40-minute visit. The clinician simply runs late."),
 (("MD Orders", C["dcs"]), ("Patient Availability", C["pat"]),
  "Wound care every 3 days, caregiver only weekends",
  "Negotiated on the phone, agreed verbally, written down nowhere."),
 (("Frequency", C["clin"]), ("Regulatory Timing", C["hchb"]),
  "Front-load, LUPA floor and the recert window",
  "Nobody models all three at once, so the period quietly ends short."),
]
cw = (W - 100 - 44 - 5*18) / 6
for i, ((a, ca), (b, cb), head, tail) in enumerate(COL):
    x = 72 + i*(cw+18)
    y = KY + 58
    add(f'<rect x="{x}" y="{y}" width="{cw}" height="26" rx="13" fill="{ca}"/>')
    lbl(x+cw/2, y+18, a, "middle", "chp")
    lbl(x+cw/2, y+50, "✕", "middle", "xs")
    add(f'<rect x="{x}" y="{y+58}" width="{cw}" height="26" rx="13" fill="{cb}"/>')
    lbl(x+cw/2, y+76, b, "middle", "chp")
    hl = textwrap.wrap(head, 26)
    for j, ln in enumerate(hl):
        lbl(x+cw/2, y+114+j*17, ln, "middle", "kh")
    base = y + 114 + len(hl)*17 + 10
    for j, ln in enumerate(textwrap.wrap(tail, 32)):
        lbl(x+cw/2, base+j*16, ln, "middle", "sub")

# ================= band 3 · who resolves it, and what changes =================
FY = KY + KH + 40
add(f'<line x1="50" y1="{FY}" x2="{W-50}" y2="{FY}" stroke="{RULE}" stroke-width="1.4"/>')
lbl(72, FY+40, "TODAY", cls="trg")
block(190, FY+16, 640, 66, C["clin"],
      ["One clinician resolves all six — unpaid, the night before,",
       "in their head, and written down nowhere"], small=True)
lbl(190, FY+104, "this is bottleneck 3: the weekly logic is undocumented and entirely unassisted", cls="sub")

lbl(880, FY+40, "THE TOOL", cls="trg")
block(1000, FY+16, 700, 66, ENG,
      ["It does not resolve the collision. It shows the collision before",
       "the day is built, and prices both sides. The clinician still decides."],
      small=True, tc=INK, bc=ENGD)
lbl(1000, FY+104, "release 1 is visualisation only (DE-03) — seeing the trade is the whole of it",
    cls="sub")

lbl(1750, FY+40, "NEXT", cls="trg")
block(1850, FY+16, 700, 66, C["pcc"],
      ["Engagement maps hang off this sheet: each collision becomes",
       "a conversation, with a named owner and a named moment"], small=True)
lbl(1850, FY+104, "the foundation this sheet exists to give them", cls="sub")

add(f'<line x1="50" y1="{H-64}" x2="{W-50}" y2="{H-64}" stroke="{RULE}" stroke-width="1.4"/>')
lbl(50, H-34, "FOUNDATION SHEET · the eight are the source slide's own; the axes, the sizes and "
    "the collisions are this project's data · variable counts from the workbook inventory", cls="foot")
lbl(W-50, H-34, "Every patient visit · competing priorities", "end", "foot")
add('</svg>')

OUT = sys.argv[1] if len(sys.argv) > 1 else "competing.svg"
open(OUT, "w", encoding="utf-8").write("\n".join(out))
print("emitted", len(out), "| canvas", W, "x", H, "| ratio", round(W/H, 3))
