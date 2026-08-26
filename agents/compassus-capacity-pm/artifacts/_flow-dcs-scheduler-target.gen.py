# -*- coding: utf-8 -*-
"""DCS / Scheduler flow map. Canvas units = points on the output sheet,
so a 16-unit label prints at 16pt. Ratio ~1.5, matching the original sheet."""

C = dict(pcc="#C6A01F", hchb="#795CA7", dcs="#792E2E", clin="#2E599D",
         auth="#DF751D", intake="#1F6F78", lead="#1A1A1A")
INK, MUT, RULE, BAND = "#1B211E", "#5A6560", "#C9CCC5", "#E9E9E5"

out = []
def add(s): out.append(s)
def esc(t): return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

BW, BH, DW, DH, GAP = 250, 90, 180, 104, 28
EXW, EXH = 250, 76

def block(x, y, w, h, fill, lines, small=False, badge=None, tc="#fff", bc=None):
    add(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="5" fill="{fill}"/>')
    lh = 15.5 if small else 19
    cls = "bt s" if small else "bt"
    cy = y + h/2 - (len(lines)-1)*lh/2 + (5 if small else 6)
    for i, ln in enumerate(lines):
        add(f'<text x="{x+w/2}" y="{cy+i*lh}" class="{cls}" style="fill:{tc}" text-anchor="middle">{esc(ln)}</text>')
    if badge:
        bw = 8.3*len(badge)+18
        add(f'<rect x="{x+w-bw-8}" y="{y-14}" width="{bw}" height="23" rx="11.5" fill="#FFFFFF" '
            f'stroke="{bc or fill}" stroke-width="1.8"/>')
        add(f'<text x="{x+w-bw/2-8}" y="{y+2}" class="bdg" text-anchor="middle" fill="{bc or fill}">{esc(badge)}</text>')


# ================= TARGET-STATE POSTURE VOCABULARY =================
PAPER = "#FBFBF8"
ENG, ENGD = "#A6E22E", "#5F8A12"
HCHB_ = C["hchb"]     # the capacity & scheduling engine; dark green for its badges

def xref(x, y, n):
    w = 8.3*len(str(n))+16
    add(f'<rect x="{x+8}" y="{y-14}" width="{w}" height="22" rx="5" fill="#FFFFFF" '
        f'stroke="{MUT}" stroke-width="1.3"/>')
    add(f'<text x="{x+8+w/2}" y="{y+1}" class="bdg" text-anchor="middle" fill="{MUT}">{esc(str(n))}</text>')

def eng(x, y, w, h, lines, small=False, badge=None, n=None):
    """AUTOMATE — the engine does it."""
    block(x, y, w, h, ENG, lines, small=small, badge=badge, tc=INK, bc=ENGD)
    if n: xref(x, y, n)

def assist(x, y, w, h, person, lines, small=False, badge=None, n=None):
    """ASSIST — the engine proposes, the named person confirms."""
    BAR = 52
    add(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="5" fill="{ENG}"/>')
    add(f'<path d="M {x+w-BAR} {y} L {x+w-6} {y} A 6 6 0 0 1 {x+w} {y+6} L {x+w} {y+h-6} '
        f'A 6 6 0 0 1 {x+w-6} {y+h} L {x+w-BAR} {y+h} Z" fill="{person}"/>')
    lh = 15.5 if small else 19
    cls = "bt s" if small else "bt"
    cy = y + h/2 - (len(lines)-1)*lh/2 + (5 if small else 6)
    for i, ln in enumerate(lines):
        add(f'<text x="{x+(w-BAR)/2}" y="{cy+i*lh}" class="{cls}" style="fill:{INK}" '
            f'text-anchor="middle">{esc(ln)}</text>')
    if badge:
        bw = 8.3*len(badge)+18
        add(f'<rect x="{x+w-bw-8}" y="{y-14}" width="{bw}" height="23" rx="11.5" fill="#FFFFFF" '
            f'stroke="{person}" stroke-width="1.8"/>')
        add(f'<text x="{x+w-bw/2-8}" y="{y+2}" class="bdg" text-anchor="middle" fill="{person}">{esc(badge)}</text>')
    if n: xref(x, y, n)

def surf(x, y, w, h, person, lines, small=False, badge=None, n=None):
    """SURFACE — the engine shows it, the person decides."""
    block(x, y, w, h, person, lines, small=small)
    add(f'<path d="M {x+6} {y} L {x+w-6} {y} A 6 6 0 0 1 {x+w} {y+6} L {x+w} {y+13} '
        f'L {x} {y+13} L {x} {y+6} A 6 6 0 0 1 {x+6} {y} Z" fill="{ENG}"/>')
    if badge:
        bw = 8.3*len(badge)+18
        add(f'<rect x="{x+w-bw-8}" y="{y-14}" width="{bw}" height="23" rx="11.5" fill="#FFFFFF" '
            f'stroke="{person}" stroke-width="1.8"/>')
        add(f'<text x="{x+w-bw/2-8}" y="{y+2}" class="bdg" text-anchor="middle" fill="{person}">{esc(badge)}</text>')
    if n: xref(x, y, n)

def man(x, y, w, h, person, lines, small=False, badge=None, n=None):
    """Unchanged — a person, or still inside HCHB."""
    block(x, y, w, h, person, lines, small=small, badge=badge)
    if n: xref(x, y, n)

def ghost(x, y, w, h, lines, n=None, label="NO LONGER A STEP", above=False):
    """A step that no longer exists — it keeps its footprint, the flow runs past it."""
    add(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="5" fill="{PAPER}" '
        f'stroke="{MUT}" stroke-width="1.7" stroke-dasharray="7 5" opacity=".8"/>')
    cy = y + h/2 - (len(lines)-1)*16/2 + 5
    for i, ln in enumerate(lines):
        add(f'<text x="{x+w/2}" y="{cy+i*16}" class="bt s" style="fill:{MUT}" '
            f'text-anchor="middle" opacity=".85">{esc(ln)}</text>')
        wl = 7.0*len(ln)
        add(f'<line x1="{x+w/2-wl/2}" y1="{cy+i*16-5}" x2="{x+w/2+wl/2}" y2="{cy+i*16-5}" '
            f'stroke="{MUT}" stroke-width="1.2" opacity=".8"/>')
    if label: lbl(x+w/2, y+h+18 if not above else y-20, label, "middle", "trg")
    if n: xref(x, y, n)

def diamond(cx, cy, lines, w=DW, h=DH):
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

def conn(dd):
    add(f'<path d="{dd}" fill="none" class="ln"/>')

def path(dd, dash=False, label=None, lx=None, ly=None, anchor="middle"):
    d = ' stroke-dasharray="7 5" opacity=".68"' if dash else ''
    add(f'<path d="{dd}" fill="none" class="ln"{d} marker-end="url(#ar)"/>')
    if label:
        add(f'<text x="{lx}" y="{ly}" class="lb" text-anchor="{anchor}">{esc(label)}</text>')

def lbl(x, y, t, anchor="start", cls="lb"):
    add(f'<text x="{x}" y="{y}" class="{cls}" text-anchor="{anchor}">{esc(t)}</text>')

W, H = 2200, 1620
add(f'<svg viewBox="0 0 {W} {H}" role="img" xmlns="http://www.w3.org/2000/svg" '
    'aria-label="Start of care and resumption of care run a referral pass first: intake receives the '
    'referral in Commure, the auth team verifies eligibility and keys pending auth, intake gives '
    'final approval, DCS reviews the referral, the scheduler books the SOC or ROC visit and the discipline '
    'evaluations, clinicians perform them. Recertification and physician orders enter directly. All '
    'converge on the discipline plan-of-care pattern: clinician submits, DCS approves per '
    'discipline \u2014 without that approval nothing moves forward and the visits are held \u2014 '
    'auth gate, scheduler assigns per discipline. Missed visits run a separate '
    '48-hour compliance chain to a DCS breach workflow.">')
add('<defs><marker id="ar" viewBox="0 0 10 8" refX="9" refY="4" markerWidth="8" markerHeight="6.5" '
    f'orient="auto-start-reverse"><polygon points="0,0 10,4 0,8" fill="{INK}"/></marker></defs>')
add(f'<rect x="0" y="0" width="{W}" height="{H}" fill="#FBFBF8"/>')

# ---------------- masthead ----------------
lbl(50, 58, "COMPASSUS HOME HEALTH  ·  TARGET STATE  ·  v1.0", cls="eyebrow")
lbl(50, 100, "Plan of Care → Assignment", cls="title")
lbl(50, 128, "Read beside Flow-DCS-Scheduler — same blocks, same positions. A dashed, struck-through block is a step that no longer exists",
    cls="deck")

lx = 800
for name, col in [("Intake", C["intake"]), ("Insurance & Auth", C["auth"]), ("DCS", C["dcs"]),
                  ("PCC / Scheduler", C["pcc"]), ("Clinician", C["clin"]), ("HCHB", C["hchb"]),
                  ("Capacity & Scheduling Engine", ENG)]:
    add(f'<circle cx="{lx+13}" cy="72" r="13" fill="{col}"/>')
    lbl(lx+34, 78, name, cls="leg")
    lx += 34 + 8.4*len(name) + 40
lbl(W-50, 112, "SIZE = WEIGHT   ·   large = every time   ·   small = conditional   ·   pill = watch condition",
    "end", "key")
add(f'<line x1="50" y1="150" x2="{W-50}" y2="150" stroke="{RULE}" stroke-width="1.4"/>')

BX = 320                      # band left edge
IX = 350                      # first block inside a band
xs = [IX, IX+BW+GAP, IX+2*(BW+GAP), IX+2*(BW+GAP)+DW+GAP,
      IX+3*(BW+GAP)+DW+GAP, IX+3*(BW+GAP)+2*(DW+GAP), IX+4*(BW+GAP)+2*(DW+GAP)]
BANDW = xs[6] + BW + 30 - BX

# ---------------- PASS 1 ----------------
P1Y, PH = 185, 225
add(f'<rect x="{BX}" y="{P1Y}" width="{6*(BW+GAP)+30}" height="{PH}" rx="10" fill="{BAND}"/>')
lbl(BX+22, P1Y+34, "PASS 1  ·  START OF CARE / RESUMPTION OF CARE — from the referral", cls="band")
p1y = P1Y + 62
c1 = p1y + BH/2
p1x = [IX + i*(BW+GAP) for i in range(6)]
eng(p1x[0], p1y, BW, BH, ["Referral captured", "in Commure"], n="1")
eng(p1x[1], p1y, BW, BH, ["Eligibility verified,", "pending auth derived", "from the payer"], n="2")
eng(p1x[2], p1y, BW, BH, ["Released to", "scheduling"], n="3")
man(p1x[3], p1y, BW, BH, C["dcs"], ["DCS reviews", "referral"], n="4")
assist(p1x[4], p1y, BW, BH, C["pcc"], ["Scheduler books", "SOC / ROC visit", "+ discipline evals"],
       badge="ASSIST", n="5")
man(p1x[5], p1y, BW, BH, C["clin"], ["Clinicians perform", "SOC / ROC", "+ eval visits"], n="6")
for a in range(5):
    arrow(p1x[a]+BW, c1, p1x[a+1]-6, c1)
lbl(p1x[1]+BW/2, p1y+BH+30, "traditional Medicare passes straight through;", "middle", "note")
lbl(p1x[1]+BW/2, p1y+BH+50, "any other payer routes to the auth team", "middle", "note")
chip(50, c1-38, 250, 76, ["Referral arrives", "with initial orders"], INK)
arrow(300, c1, IX-6, c1)
lbl(50, c1-52, "TRIGGER", cls="trg")

# ---------------- PASS 2 ----------------
P2Y = 560
add(f'<rect x="{BX}" y="{P2Y}" width="{BANDW}" height="{PH}" rx="10" fill="{BAND}"/>')
lbl(BX+22, P2Y+34, "PASS 2  ·  DISCIPLINE PLAN OF CARE — the repeating pattern", cls="band")
p2y = P2Y + 62
c2 = p2y + BH/2
surf(xs[0], p2y, BW, BH, C["clin"], ["Clinician submits", "discipline plan", "of care"],
     badge="× N disciplines", n="1")
man(xs[1], p2y, BW, BH, C["dcs"], ["DCS reviews &", "approves"], badge="× N disciplines", n="2")
diamond(xs[2]+DW/2, c2, ["Approved?"])
man(xs[3], p2y, BW, BH, HCHB_, ["Visits generate", "in HCHB"], n="4")
diamond(xs[4]+DW/2, c2, ["Auth on", "file?"])
assist(xs[5], p2y, BW, BH, C["pcc"], ["Scheduler assigns", "to care team"], badge="ASSIST", n="6")
man(xs[6], p2y, BW, BH, C["clin"], ["Visits on", "clinician calendar"], n="7")
for a, b in [(xs[0]+BW, xs[1]), (xs[1]+BW, xs[2]), (xs[2]+DW, xs[3]),
             (xs[3]+BW, xs[4]), (xs[4]+DW, xs[5]), (xs[5]+BW, xs[6])]:
    arrow(a, c2, b-6, c2)
lbl(xs[3]-12, c2-12, "Yes", "end")
lbl(xs[5]-12, c2-12, "Yes", "end")

# entry bus
BUS = 316
conn(f"M {p1x[5]+BW/2} {p1y+BH} L {p1x[5]+BW/2} {P1Y+PH+72} L {BUS} {P1Y+PH+72} L {BUS} {c2}")
lbl((p1x[5]+BW/2 + BUS)/2, P1Y+PH+60,
    "after the eval visits, each discipline writes its own plan of care", "middle", "conn")
chip(50, c2-118, 250, 84, ["Recertification", "OASIS recert visit, or", "non-OASIS recert eval"], INK)
chip(50, c2+34, 250, 84, ["Physician order", "adds a discipline eval, or", "changes the visits ordered"], INK)
lbl(50, c2-134, "OTHER TRIGGERS", cls="trg")
conn(f"M 300 {c2-76} L {BUS} {c2-76} L {BUS} {c2}")
conn(f"M 300 {c2+76} L {BUS} {c2+76} L {BUS} {c2}")
arrow(BUS, c2, xs[0]-6, c2)
lbl(50, c2+140, "no OASIS · adds, reduces or redistributes", cls="note")
lbl(50, c2+158, "visits without changing the episode total", cls="note")

# ---------------- exceptions ----------------
exy = P2Y + PH + 54
man(xs[1]-42, exy, EXW, EXH, C["dcs"], ["QA backlog", "visits compress"], small=True)
man(xs[2]-35, exy, EXW, EXH, C["clin"], ["Returned to clinician", "for correction",
                                          "\u2014 visits are held"], small=True)
ghost(xs[4]-35, exy, EXW, EXH, ["Pending auth", "not on calendar, not counted"])
path(f"M {xs[1]+58} {p2y+BH} L {xs[1]+58} {exy-6}", dash=True)
path(f"M {xs[2]+DW/2} {c2+DH/2} L {xs[2]+DW/2} {exy-6}", dash=True,
     label="No \u2014 nothing moves forward", lx=xs[2]+DW/2+16, ly=exy-22, anchor="start")
path(f"M {xs[4]+DW/2} {c2+DH/2} L {xs[4]+DW/2} {exy-6}", dash=True, label="No",
     lx=xs[4]+DW/2+16, ly=exy-22, anchor="start")

# ---------------- episode budget ----------------
py, ph = exy + EXH + 54, 150
add(f'<rect x="{xs[1]}" y="{py}" width="{xs[6]+BW-xs[1]}" height="{ph}" rx="10" fill="none" '
    f'stroke="{RULE}" stroke-width="1.8" stroke-dasharray="8 6"/>')
lbl(xs[1]+26, py+36, "EPISODE VISIT BUDGET — set at plan-of-care approval, steered by DCS", cls="pnl")
chip(xs[1]+26, py+58, 330, 46, ["LUPA floor · too few visits"], C["dcs"])
chip(xs[1]+382, py+58, 400, 46, ["Utilisation ceiling · visits beyond need"], C["dcs"])
lbl(xs[1]+818, py+80, "Fixed 30-day PDGM payment: below the floor the period pays per visit;", cls="note")
lbl(xs[1]+818, py+100, "above the ceiling extra visits earn nothing and consume capacity.", cls="note")
path(f"M {xs[1]+186} {py-6} L {xs[1]+186} {p2y+BH+8}", dash=True)

# ---------------- missed visit ----------------
MVY = py + ph + 54
add(f'<rect x="{BX}" y="{MVY}" width="{xs[3]+BW+30-BX}" height="{PH}" rx="10" fill="{BAND}"/>')
lbl(BX+22, MVY+34, "MISSED VISIT — the compliance chain", cls="band")
m2y = MVY + 62
c3 = m2y + BH/2
man(xs[0], m2y, BW, BH, C["clin"], ["Clinician documents", "missed visit"], n="1")
eng(xs[1], m2y, BW, BH, ["MD notified inside", "48 hours"], n="2")
diamond(xs[2]+DW/2, c3, ["MD notified", "within 48h?"], w=200)
man(xs[3], m2y, BW, BH, HCHB_, ["Documented", "in HCHB"], n="4")
arrow(xs[0]+BW, c3, xs[1]-6, c3)
arrow(xs[1]+BW, c3, xs[2]+DW/2-100-6, c3)
arrow(xs[2]+DW/2+100, c3, xs[3]-6, c3)
lbl(xs[3]-12, c3-12, "Yes", "end")
chip(50, c3-38, 250, 76, ["Missed visit"], INK)
arrow(300, c3, xs[0]-6, c3)
lbl(50, c3-52, "TRIGGER", cls="trg")
man(xs[2]-35, MVY+PH+62, EXW, EXH, C["dcs"], ["DCS workflow", "48h breach"], small=True)
path(f"M {xs[2]+DW/2} {c3+DH/2} L {xs[2]+DW/2} {MVY+PH+44}", dash=True, label="No",
     lx=xs[2]+DW/2+16, ly=MVY+PH+30, anchor="start")

add(f'<line x1="50" y1="{H-72}" x2="{W-50}" y2="{H-72}" stroke="{RULE}" stroke-width="1.4"/>')
lbl(50, H-40, "TARGET STATE, PROPOSED · green = the capacity & scheduling engine (dark text); purple = still inside HCHB · phase 1 is visualisation only (DE-03)", cls="foot")
lbl(W-50, H-40, "Plan of care → assignment — target state", "end", "foot")
add('</svg>')

import sys
OUT = sys.argv[1] if len(sys.argv) > 1 else "dcs-target.svg"
open(OUT, "w", encoding="utf-8").write("\n".join(out))
print("emitted", len(out), "| canvas", W, "x", H, "| ratio", round(W/H, 3))
