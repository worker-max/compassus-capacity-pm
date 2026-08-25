# -*- coding: utf-8 -*-
"""Flow 5 — Recertification & Discharge. Canvas units = points on the output sheet."""

C = dict(pcc="#C6A01F", hchb="#795CA7", dcs="#792E2E", clin="#2E599D",
         auth="#DF751D", intake="#1F6F78", float_="#795933", lead="#1A1A1A")
INK, MUT, RULE, BAND = "#1B211E", "#5A6560", "#C9CCC5", "#E9E9E5"

out = []
def add(s): out.append(s)
def esc(t): return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

BW, BH, GAP = 250, 90, 28

def block(x, y, w, h, fill, lines, small=False, badge=None):
    add(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6" fill="{fill}"/>')
    lh = 16 if small else 19
    cls = "bt s" if small else "bt"
    cy = y + h/2 - (len(lines)-1)*lh/2 + (5 if small else 6)
    for i, ln in enumerate(lines):
        add(f'<text x="{x+w/2}" y="{cy+i*lh}" class="{cls}" text-anchor="middle">{esc(ln)}</text>')
    if badge:
        bw = 8.3*len(badge)+18
        add(f'<rect x="{x+w-bw-8}" y="{y-14}" width="{bw}" height="23" rx="11.5" fill="#FFFFFF" '
            f'stroke="{fill}" stroke-width="1.8"/>')
        add(f'<text x="{x+w-bw/2-8}" y="{y+2}" class="bdg" text-anchor="middle" fill="{fill}">{esc(badge)}</text>')

def diamond(cx, cy, lines, w=180, h=104):
    add(f'<polygon points="{cx},{cy-h/2} {cx+w/2},{cy} {cx},{cy+h/2} {cx-w/2},{cy}" '
        f'fill="#FFFFFF" stroke="{INK}" stroke-width="1.8"/>')
    y0 = cy - (len(lines)-1)*17/2 + 5
    for i, ln in enumerate(lines):
        add(f'<text x="{cx}" y="{y0+i*17}" class="dt" text-anchor="middle">{esc(ln)}</text>')

def chip(x, y, w, h, lines, stroke, fill="#FFFFFF"):
    add(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{min(h/2,26)}" fill="{fill}" '
        f'stroke="{stroke}" stroke-width="1.8"/>')
    y0 = y + h/2 - (len(lines)-1)*17/2 + 5
    for i, ln in enumerate(lines):
        add(f'<text x="{x+w/2}" y="{y0+i*17}" class="ct" text-anchor="middle" fill="{stroke}">{esc(ln)}</text>')

def arrow(x1, y1, x2, y2, dash=False):
    d = ' stroke-dasharray="7 5" opacity=".68"' if dash else ''
    add(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" class="ln"{d} marker-end="url(#ar)"/>')

def path(dd, dash=False, label=None, lx=None, ly=None, anchor="middle"):
    d = ' stroke-dasharray="7 5" opacity=".68"' if dash else ''
    add(f'<path d="{dd}" fill="none" class="ln"{d} marker-end="url(#ar)"/>')
    if label:
        add(f'<text x="{lx}" y="{ly}" class="lb" text-anchor="{anchor}">{esc(label)}</text>')

def lbl(x, y, t, anchor="start", cls="lb"):
    add(f'<text x="{x}" y="{y}" class="{cls}" text-anchor="{anchor}">{esc(t)}</text>')

def sublist(x, y, items):
    for i, t in enumerate(items):
        add(f'<text x="{x+6}" y="{y+i*17}" class="sub">{esc("·  " + t)}</text>')

W, H = 2200, 1800
add(f'<svg viewBox="0 0 {W} {H}" role="img" xmlns="http://www.w3.org/2000/svg" '
    'aria-label="Recertification and discharge at the end of a sixty-day certification period, shown '
    'through a worked example. Skilled nursing, physical therapy and occupational therapy are all '
    'active. Each discipline decides for itself against its goals. Nursing discharges seven to eight '
    'days before the period ends with a non-OASIS discipline discharge, and owes no visit in the '
    'five-day recert window. PT and OT recertify: both visit inside the window, PT carries the OASIS '
    'recert, OT performs a non-OASIS recert eval. Their next-period frequency orders, PT two-weekly '
    'times three then one-weekly times three, OT one-weekly times four, feed the same plan-of-care '
    'pattern as flow one, pass two.">')
add('<defs><marker id="ar" viewBox="0 0 10 8" refX="9" refY="4" markerWidth="8" markerHeight="6.5" '
    f'orient="auto-start-reverse"><polygon points="0,0 10,4 0,8" fill="{INK}"/></marker></defs>')
add(f'<rect x="0" y="0" width="{W}" height="{H}" fill="#FBFBF8"/>')

# ---------------- masthead ----------------
lbl(50, 58, "COMPASSUS HOME HEALTH  ·  FLOW 5", cls="eyebrow")
lbl(50, 100, "Recertification & Discharge", cls="title")
lbl(50, 128, "Each discipline decides for itself — and the last one out does the OASIS", cls="deck")
lx = 1100
for name, col in [("Clinician (SN · PT · OT)", C["clin"]), ("DCS", C["dcs"]),
                  ("PCC / Scheduler", C["pcc"]), ("HCHB", C["hchb"]),
                  ("Insurance & Auth", C["auth"])]:
    add(f'<circle cx="{lx+13}" cy="72" r="13" fill="{col}"/>')
    lbl(lx+34, 78, name, cls="leg")
    lx += 34 + 8.4*len(name) + 36
add(f'<line x1="50" y1="150" x2="{W-50}" y2="150" stroke="{RULE}" stroke-width="1.4"/>')

BX, IX = 320, 350
BANDW = 1850

# ================= BAND 1 · the decision =================
AY, AH = 185, 262
add(f'<rect x="{BX}" y="{AY}" width="{BANDW}" height="{AH}" rx="10" fill="{BAND}"/>')
lbl(BX+22, AY+34, "THE DECISION  ·  EACH ACTIVE DISCIPLINE, SEPARATELY, AGAINST ITS OWN GOALS", cls="band")
c1 = AY + 62 + BH/2
block(IX, AY+62, BW, BH, C["clin"], ["Discipline reviews", "progress against", "its goals"])
diamond(IX+BW+GAP+90, c1, ["Goals met?"])
arrow(IX+BW, c1, IX+BW+GAP-6, c1)
oy1, oy2 = AY+44, AY+156
OBX = IX+BW+GAP+260
block(OBX, oy1, 300, 68, C["clin"], ["Discharge — discipline level", "(non-OASIS)"], small=True)
block(OBX, oy2, 300, 68, C["clin"], ["Recertify — visit inside", "the 5-day window"], small=True)
split = IX+BW+GAP+90+90+34
path(f"M {IX+BW+GAP+180} {c1} L {split} {c1} L {split} {oy1+34} L {OBX-6} {oy1+34}",
     label="Yes", lx=split+12, ly=oy1+58, anchor="start")
path(f"M {split} {c1} L {split} {oy2+34} L {OBX-6} {oy2+34}",
     label="No — more care indicated", lx=split+12, ly=oy2-14, anchor="start")
lbl(OBX+320, oy1+28, "leaves before the window —", "start", "note")
lbl(OBX+320, oy1+46, "no recert visit owed", "start", "note")
lbl(OBX+320, oy2+28, "the visit is already on the calendar —", "start", "note")
lbl(OBX+320, oy2+46, "plotted at the original plan of care", "start", "note")
lbl(IX+1300, AY+70, "DISCIPLINE-DEPENDENT", cls="colh")
sublist(IX+1294, AY+94, ["Some services discharge before recert",
                         "Others continue on goals not yet met",
                         "Slow progress mid-episode →",
                         "add-on order extends care (Flow 1)"])

# ================= BAND 2 · the worked example =================
EY, EH = AY + AH + 40, 560
add(f'<rect x="{BX}" y="{EY}" width="{BANDW}" height="{EH}" rx="10" fill="{BAND}"/>')
lbl(BX+22, EY+34, "THE WORKED EXAMPLE  ·  SN DISCHARGES — PT AND OT RECERTIFY", cls="band")
lbl(BX+BANDW-14, EY+34, "WINDOW EXPANDED — NOT TO SCALE", "end", "bandhi")

BARY, BARH = EY+80, 34
X0, XB = 430, 700                 # bar start, start of expanded days
DAYW = 76
def dx(d): return XB + (d-51)*DAYW
XEND = dx(61)                      # day-60/day-1 boundary = 1460
NX0, NX1 = XEND, 2130

# current-period bar
add(f'<rect x="{X0}" y="{BARY}" width="{XEND-X0}" height="{BARH}" rx="4" fill="#FFFFFF" '
    f'stroke="{MUT}" stroke-width="1.6"/>')
# window shading (days 56-60)
add(f'<rect x="{dx(56)}" y="{BARY}" width="{XEND-dx(56)}" height="{BARH}" fill="{C["dcs"]}" opacity=".16"/>')
# compression squiggle
add(f'<path d="M 640 {BARY-6} l 10 {BARH+12} m 12 -{BARH+12} l 10 {BARH+12}" stroke="{MUT}" '
    'stroke-width="2" fill="none"/>')
lbl((X0+640)/2, BARY+22, "days 1–50", "middle", "dt")
lbl(X0, BARY-14, "CURRENT 60-DAY CERTIFICATION PERIOD", "start", "trg")
for d in range(51, 61):
    add(f'<line x1="{dx(d)}" y1="{BARY+BARH}" x2="{dx(d)}" y2="{BARY+BARH+8}" stroke="{MUT}" stroke-width="1.4"/>')
    lbl(dx(d)+DAYW/2, BARY+BARH+24, str(d), "middle", "lb")
lbl((dx(56)+XEND)/2, BARY-14, "5-DAY RECERT WINDOW · DAYS 56–60", "middle", "pnl")
# boundary
add(f'<line x1="{XEND}" y1="{BARY-34}" x2="{XEND}" y2="{EY+EH-96}" stroke="{INK}" '
    'stroke-width="2.5" stroke-dasharray="12 7"/>')
lbl(XEND, BARY-44, "DAY 60 → DAY 1", "middle", "boundary")
# new-period bar
add(f'<rect x="{NX0}" y="{BARY}" width="{NX1-NX0}" height="{BARH}" rx="4" fill="#FFFFFF" '
    f'stroke="{MUT}" stroke-width="1.6"/>')
lbl((NX0+NX1)/2, BARY+22, "NEW 60-DAY CERTIFICATION PERIOD", "middle", "dt")

# lanes
LSN, LPT, LOT = EY+230, EY+340, EY+450
for ly_, name in [(LSN, "SN"), (LPT, "PT"), (LOT, "OT")]:
    chip(352, ly_-22, 56, 44, [name], C["clin"])
    add(f'<line x1="418" y1="{ly_}" x2="{X0+18}" y2="{ly_}" stroke="{RULE}" stroke-width="1.6"/>')

# SN — discipline discharge at day 52-53
snb_x, snb_w = dx(51)+30, 300
add(f'<line x1="{X0+18}" y1="{LSN}" x2="{snb_x-4}" y2="{LSN}" stroke="{RULE}" stroke-width="1.6"/>')
block(snb_x, LSN-32, snb_w, 64, C["clin"], ["SN final visit — discipline", "discharge (non-OASIS)"], small=True)
add(f'<circle cx="{snb_x+snb_w+26}" cy="{LSN}" r="7" fill="none" stroke="{INK}" stroke-width="2.2"/>')
lbl(snb_x, LSN+52, "days 52–53 — 7–8 days before the period ends. A discipline that is not", "start", "note")
lbl(snb_x, LSN+70, "recertifying owes no visit inside the window. SN is off the case.", "start", "note")
path(f"M {dx(52.5)} {LSN-38} L {dx(52.5)} {BARY+BARH+34}", dash=True)

# PT — OASIS recert visit day 57
ptb_x, ptb_w = dx(56)+8, 290
add(f'<line x1="{X0+18}" y1="{LPT}" x2="{ptb_x-4}" y2="{LPT}" stroke="{RULE}" stroke-width="1.6"/>')
block(ptb_x, LPT-32, ptb_w, 64, C["clin"], ["PT — OASIS recert visit"], small=True, badge="CARRIES THE OASIS")
arrow(ptb_x+ptb_w, LPT, NX0+54, LPT)
chip(NX0+60, LPT-32, 330, 64, ["PT · 2w3, then 1w3", "6 + 3 = 9 visits over 6 weeks"], C["clin"])

# OT — non-OASIS recert eval day 58
otb_x, otb_w = dx(57)+30, 300
add(f'<line x1="{X0+18}" y1="{LOT}" x2="{otb_x-4}" y2="{LOT}" stroke="{RULE}" stroke-width="1.6"/>')
block(otb_x, LOT-32, otb_w, 64, C["clin"], ["OT — recert eval", "(non-OASIS)"], small=True)
arrow(otb_x+otb_w, LOT, NX0+54, LOT)
chip(NX0+60, LOT-32, 330, 64, ["OT · 1w4", "4 visits over 4 weeks"], C["clin"])

lbl(IX+8, EY+EH-26, "one recertifying discipline carries the OASIS recert — here PT; OT's eval is "
    "non-OASIS · both visits were already plotted at the original plan of care", "start", "hi")

# ================= BAND 3 · the workflow =================
WY3, WH3 = EY + EH + 40, 336
add(f'<rect x="{BX}" y="{WY3}" width="{BANDW}" height="{WH3}" rx="10" fill="{BAND}"/>')
lbl(BX+22, WY3+34, "AFTER THE RECERT VISITS  ·  THE NEXT PERIOD IS BUILT", cls="band")
lbl(BX+BANDW-14, WY3+34, "THE SAME PATTERN AS FLOW 1, PASS 2", "end", "bandhi")
wb = WY3 + 66
wc = wb + BH/2
W5, G5 = 280, 30
w5x = [350, 660, 970, 1460, 1770]
DGX = 1355
block(w5x[0], wb, W5, BH, C["clin"], ["PT and OT establish next-", "period frequency orders"], badge="× 2 disciplines")
block(w5x[1], wb, W5, BH, C["dcs"], ["DCS reviews and approves", "each plan of care"],
      badge="× 2 disciplines")
block(w5x[2], wb, W5, BH, C["hchb"], ["HCHB generates visits", "and assignment tasks"])
diamond(DGX, wc, ["Auth on", "file?"], w=150, h=104)
block(w5x[3], wb, W5, BH, C["pcc"], ["Scheduler assigns all", "plotted visits — one pass"])
block(w5x[4], wb, W5, BH, C["clin"], ["New period's visits on", "PT and OT calendars"])
arrow(w5x[0]+W5, wc, w5x[1]-6, wc)
arrow(w5x[1]+W5, wc, w5x[2]-6, wc)
arrow(w5x[2]+W5, wc, DGX-75-6, wc)
path(f"M {DGX+75} {wc} L {w5x[3]-6} {wc}", label="Yes", lx=(DGX+75+w5x[3])/2, ly=wc-12)
arrow(w5x[3]+W5, wc, w5x[4]-6, wc)
block(DGX-190, wb+BH+42, 380, 54, C["auth"],
      ["No auth → the visit sits pending —", "not on the calendar, not counted"], small=True)
path(f"M {DGX} {wc+52} L {DGX} {wb+BH+36}", dash=True, label="No",
     lx=DGX+14, ly=wc+78, anchor="start")
lbl(w5x[0], wb+BH+26, "PT 2w3 → 1w3  ·  OT 1w4", "start", "sub")
lbl(w5x[0], wb+BH+46, "the scheduling workflow fires only now", "start", "sub")
lbl(IX, WY3+WH3-20, "a new certification period is a new auth question — traditional Medicare passes "
    "straight through; any other payer re-enters the auth cycle (Flow 3) before these visits can be "
    "assigned", "start", "hi")

# ================= if nobody recertifies =================
PY5, PH5 = WY3 + WH3 + 40, 148
add(f'<rect x="{IX}" y="{PY5}" width="{BANDW-60}" height="{PH5}" rx="10" fill="none" '
    f'stroke="{RULE}" stroke-width="1.8" stroke-dasharray="8 6"/>')
lbl(IX+26, PY5+36, "IF NO DISCIPLINE RECERTIFIES — THE AGENCY DISCHARGE", cls="pnl")
sublist(IX+38, PY5+66, ["Every discipline still discharges separately — the earlier ones non-OASIS, exactly like SN above",
                        "The last discipline active performs the agency discharge with the D/C OASIS — RN, PT or OT, whoever makes the final visit",
                        "The owner of the agency discharge is unknown until it happens — and the episode's capacity returns to the branch"])

# ================= boundaries =================
BDY = PY5 + PH5 + 40
lbl(50, BDY+30, "BOUNDARIES", cls="trg")
bnd = ["Recert visits are plotted at the original POC", "The window binds only recertifying disciplines",
       "Each discipline decides separately", "Scheduling fires only after frequency is set"]
bxx = IX
for t in bnd:
    w = 8.6*len(t) + 46
    chip(bxx, BDY+8, w, 42, [t], MUT)
    bxx += w + 20

add(f'<line x1="50" y1="{H-72}" x2="{W-50}" y2="{H-72}" stroke="{RULE}" stroke-width="1.4"/>')
lbl(50, H-40, "Current state · condensed on the primary map as phase 4", cls="foot")
lbl(W-50, H-40, "Flow 5 · recertification & discharge", "end", "foot")
add('</svg>')

import sys
OUT = sys.argv[1] if len(sys.argv) > 1 else "flow5.svg"
open(OUT, "w", encoding="utf-8").write("\n".join(out))
print("emitted", len(out), "| canvas", W, "x", H, "| ratio", round(W/H, 3),
      "| boundary x", XEND, "| last y", BDY+50)
