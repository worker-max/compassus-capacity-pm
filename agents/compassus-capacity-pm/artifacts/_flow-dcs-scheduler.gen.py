# -*- coding: utf-8 -*-
"""DCS / Scheduler flow map. Canvas units = points on the output sheet,
so a 16-unit label prints at 16pt. Ratio ~1.5, matching the original sheet."""

C = dict(pcc="#C6A01F", hchb="#795CA7", dcs="#792E2E", clin="#2E599D",
         auth="#DF751D", lead="#1A1A1A")
INK, MUT, RULE, BAND = "#1B211E", "#5A6560", "#C9CCC5", "#E9E9E5"

out = []
def add(s): out.append(s)
def esc(t): return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

BW, BH, DW, DH, GAP = 250, 90, 180, 104, 28
EXW, EXH = 250, 76

def block(x, y, w, h, fill, lines, small=False, badge=None):
    add(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="5" fill="{fill}"/>')
    lh = 15.5 if small else 19
    cls = "bt s" if small else "bt"
    cy = y + h/2 - (len(lines)-1)*lh/2 + (5 if small else 6)
    for i, ln in enumerate(lines):
        add(f'<text x="{x+w/2}" y="{cy+i*lh}" class="{cls}" text-anchor="middle">{esc(ln)}</text>')
    if badge:
        bw = 8.3*len(badge)+18
        add(f'<rect x="{x+w-bw-8}" y="{y-14}" width="{bw}" height="23" rx="11.5" fill="#FFFFFF" '
            f'stroke="{fill}" stroke-width="1.8"/>')
        add(f'<text x="{x+w-bw/2-8}" y="{y+2}" class="bdg" text-anchor="middle" fill="{fill}">{esc(badge)}</text>')

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
    'aria-label="Start of care and resumption of care run a referral pass first: office verifies, '
    'DCS reviews the referral, the scheduler books the SOC or ROC visit and the discipline '
    'evaluations, clinicians perform them. Recertification and add-on orders enter directly. All '
    'converge on the discipline plan-of-care pattern: clinician submits, DCS approves per '
    'discipline, auth gate, scheduler assigns per discipline. Missed visits run a separate '
    '48-hour compliance chain to a DCS breach workflow.">')
add('<defs><marker id="ar" viewBox="0 0 10 8" refX="9" refY="4" markerWidth="8" markerHeight="6.5" '
    f'orient="auto-start-reverse"><polygon points="0,0 10,4 0,8" fill="{INK}"/></marker></defs>')
add(f'<rect x="0" y="0" width="{W}" height="{H}" fill="#FBFBF8"/>')

# ---------------- masthead ----------------
lbl(50, 58, "COMPASSUS HOME HEALTH", cls="eyebrow")
lbl(50, 100, "Plan of Care → Assignment", cls="title")
lbl(50, 128, "The DCS and scheduler handoff — a simplified subset of the full swimlane",
    cls="deck")

lx = 1160
for name, col in [("PCC / Scheduler", C["pcc"]), ("HCHB", C["hchb"]), ("DCS", C["dcs"]),
                  ("Clinician", C["clin"]), ("Insurance & Auth", C["auth"])]:
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
add(f'<rect x="{BX}" y="{P1Y}" width="{4*(BW+GAP)+30}" height="{PH}" rx="10" fill="{BAND}"/>')
lbl(BX+22, P1Y+34, "PASS 1  ·  START OF CARE / RESUMPTION OF CARE — from the referral", cls="band")
p1y = P1Y + 62
c1 = p1y + BH/2
p1x = [IX, IX+BW+GAP, IX+2*(BW+GAP), IX+3*(BW+GAP)]
block(p1x[0], p1y, BW, BH, C["auth"], ["Office verifies", "eligibility"])
block(p1x[1], p1y, BW, BH, C["dcs"], ["DCS reviews", "referral"])
block(p1x[2], p1y, BW, BH, C["pcc"], ["Scheduler books", "SOC / ROC visit", "+ discipline evals"])
block(p1x[3], p1y, BW, BH, C["clin"], ["Clinicians perform", "SOC / ROC", "+ eval visits"])
for a in range(3):
    arrow(p1x[a]+BW, c1, p1x[a+1]-6, c1)
chip(50, c1-38, 250, 76, ["Referral arrives", "with initial orders"], INK)
arrow(300, c1, IX-6, c1)
lbl(50, c1-52, "TRIGGER", cls="trg")

# ---------------- PASS 2 ----------------
P2Y = 560
add(f'<rect x="{BX}" y="{P2Y}" width="{BANDW}" height="{PH}" rx="10" fill="{BAND}"/>')
lbl(BX+22, P2Y+34, "PASS 2  ·  DISCIPLINE PLAN OF CARE — the repeating pattern", cls="band")
p2y = P2Y + 62
c2 = p2y + BH/2
block(xs[0], p2y, BW, BH, C["clin"], ["Clinician submits", "discipline plan", "of care"],
      badge="× N disciplines")
block(xs[1], p2y, BW, BH, C["dcs"], ["DCS reviews &", "approves"], badge="× N disciplines")
diamond(xs[2]+DW/2, c2, ["Approved?"])
block(xs[3], p2y, BW, BH, C["hchb"], ["Visits generate", "in HCHB"])
diamond(xs[4]+DW/2, c2, ["Auth on", "file?"])
block(xs[5], p2y, BW, BH, C["pcc"], ["Scheduler assigns", "to care team"], badge="× N disciplines")
block(xs[6], p2y, BW, BH, C["clin"], ["Visits on", "clinician calendar"])
for a, b in [(xs[0]+BW, xs[1]), (xs[1]+BW, xs[2]), (xs[2]+DW, xs[3]),
             (xs[3]+BW, xs[4]), (xs[4]+DW, xs[5]), (xs[5]+BW, xs[6])]:
    arrow(a, c2, b-6, c2)
lbl(xs[3]-12, c2-12, "Yes", "end")
lbl(xs[5]-12, c2-12, "Yes", "end")

# entry bus
BUS = 316
conn(f"M {p1x[3]+BW/2} {p1y+BH} L {p1x[3]+BW/2} {P1Y+PH+72} L {BUS} {P1Y+PH+72} L {BUS} {c2}")
lbl((p1x[3]+BW/2 + BUS)/2, P1Y+PH+60,
    "after the eval visits, each discipline writes its own plan of care", "middle", "conn")
chip(50, c2-118, 250, 84, ["Recertification", "OASIS recert visit, or", "non-OASIS recert eval"], INK)
chip(50, c2+34, 250, 84, ["Add-on order", "status change: add,", "reduce or shift visits"], INK)
lbl(50, c2-134, "OTHER TRIGGERS", cls="trg")
conn(f"M 300 {c2-76} L {BUS} {c2-76} L {BUS} {c2}")
conn(f"M 300 {c2+76} L {BUS} {c2+76} L {BUS} {c2}")
arrow(BUS, c2, xs[0]-6, c2)
lbl(50, c2+140, "no OASIS · adds, reduces or redistributes", cls="note")
lbl(50, c2+158, "visits without changing the episode total", cls="note")

# ---------------- exceptions ----------------
exy = P2Y + PH + 54
block(xs[1]-42, exy, EXW, EXH, C["dcs"], ["QA backlog", "visits compress"], small=True)
block(xs[2]-35, exy, EXW, EXH, C["clin"], ["Returned to clinician", "for correction"], small=True)
block(xs[4]-35, exy, EXW, EXH, C["auth"], ["Pending auth", "not on calendar, not counted"], small=True)
path(f"M {xs[1]+58} {p2y+BH} L {xs[1]+58} {exy-6}", dash=True)
path(f"M {xs[2]+DW/2} {c2+DH/2} L {xs[2]+DW/2} {exy-6}", dash=True, label="No",
     lx=xs[2]+DW/2+16, ly=exy-22, anchor="start")
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
block(xs[0], m2y, BW, BH, C["clin"], ["Clinician documents", "missed visit"])
block(xs[1], m2y, BW, BH, C["pcc"], ["Scheduler workflow", "notify MD"])
diamond(xs[2]+DW/2, c3, ["MD notified", "within 48h?"], w=200)
block(xs[3], m2y, BW, BH, C["hchb"], ["Documented", "in HCHB"])
arrow(xs[0]+BW, c3, xs[1]-6, c3)
arrow(xs[1]+BW, c3, xs[2]+DW/2-100-6, c3)
arrow(xs[2]+DW/2+100, c3, xs[3]-6, c3)
lbl(xs[3]-12, c3-12, "Yes", "end")
chip(50, c3-38, 250, 76, ["Missed visit"], INK)
arrow(300, c3, xs[0]-6, c3)
lbl(50, c3-52, "TRIGGER", cls="trg")
block(xs[2]-35, MVY+PH+62, EXW, EXH, C["dcs"], ["DCS workflow", "48h breach"], small=True)
path(f"M {xs[2]+DW/2} {c3+DH/2} L {xs[2]+DW/2} {MVY+PH+44}", dash=True, label="No",
     lx=xs[2]+DW/2+16, ly=MVY+PH+30, anchor="start")

add(f'<line x1="50" y1="{H-72}" x2="{W-50}" y2="{H-72}" stroke="{RULE}" stroke-width="1.4"/>')
lbl(50, H-40, "Large = happens every time  ·  small = conditional  ·  pill = a threshold, not a step. "
    "Both gates fire once per discipline.", cls="foot")
lbl(W-50, H-40, "DCS and Scheduler only", "end", "foot")
add('</svg>')

open("/tmp/claude-0/-home-user/f0ef1ecc-a04c-5098-a365-4b559e397089/scratchpad/gen/flow.svg",
     "w", encoding="utf-8").write("\n".join(out))
print("emitted", len(out), "| canvas", W, "x", H, "| ratio", round(W/H, 3))
