# -*- coding: utf-8 -*-
"""Flow 1T — Start of Care, TARGET STATE. v1.0.

Posture vocabulary is the 25 Aug variable workbook's own 'Future state — the tool's
role' column: Automate / Assist / Surface / Stays manual. Colour still = actor, so an
Assist or Surface block keeps the colour of the person who decides.
"""
import sys, os
sys.path.insert(0, os.environ.get("FLOWKIT", "/home/user/compassus-capacity-pm/.claude/skills/process-flow-map/assets"))
from flowkit import *

ENG = "#A6E22E"           # THE CAPACITY & SCHEDULING ENGINE — the only light block, dark text
HCHB = C["hchb"]          # unchanged: work that still happens inside HCHB

def _badge(x, y, w, txt, col):
    bw = 8.3*len(txt)+18
    add(f'<rect x="{x+w-bw-8}" y="{y-14}" width="{bw}" height="23" rx="11.5" '
        f'fill="#FFFFFF" stroke="{col}" stroke-width="1.8"/>')
    add(f'<text x="{x+w-bw/2-8}" y="{y+2}" class="bdg" text-anchor="middle" '
        f'fill="{col}">{esc(txt)}</text>')

def xref(x, y, n):
    """Cross-reference ordinal — which step on the current-state sheet this is."""
    w = 30 if len(str(n)) < 3 else 8.3*len(str(n))+16
    add(f'<rect x="{x+8}" y="{y-14}" width="{w}" height="23" rx="5" fill="#FFFFFF" '
        f'stroke="{MUT}" stroke-width="1.4"/>')
    add(f'<text x="{x+8+w/2}" y="{y+2}" class="bdg" text-anchor="middle" fill="{MUT}">{esc(n)}</text>')

def eng(x, y, w, h, lines, badge=None, n=None):
    """AUTOMATE — the engine does it."""
    block(x, y, w, h, ENG, lines, tc=INK)
    if badge: _badge(x, y, w, badge, "#5F8A12")
    if n: xref(x, y, n)

def assist(x, y, w, h, person, lines, badge=None, n=None):
    """ASSIST — the engine proposes, a person confirms. The bar names who confirms."""
    BAR = 46
    add(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6" fill="{ENG}"/>')
    add(f'<path d="M {x+w-BAR} {y} L {x+w-6} {y} A 6 6 0 0 1 {x+w} {y+6} L {x+w} {y+h-6} '
        f'A 6 6 0 0 1 {x+w-6} {y+h} L {x+w-BAR} {y+h} Z" fill="{person}"/>')
    cy = y + h/2 - (len(lines)-1)*19/2 + 6
    for i, ln in enumerate(lines):
        add(f'<text x="{x+(w-BAR)/2}" y="{cy+i*19}" class="bt" style="fill:{INK}" '
            f'text-anchor="middle">{esc(ln)}</text>')
    if badge: _badge(x, y, w, badge, person)
    if n: xref(x, y, n)

def surf(x, y, w, h, person, lines, badge=None, n=None):
    """SURFACE — the engine shows it, the person decides."""
    block(x, y, w, h, person, lines, badge=badge)
    add(f'<path d="M {x+6} {y} L {x+w-6} {y} A 6 6 0 0 1 {x+w} {y+6} L {x+w} {y+14} '
        f'L {x} {y+14} L {x} {y+6} A 6 6 0 0 1 {x+6} {y} Z" fill="{ENG}"/>')
    if n: xref(x, y, n)

def man(x, y, w, h, person, lines, badge=None, n=None):
    """STAYS MANUAL, or still inside HCHB — unchanged."""
    block(x, y, w, h, person, lines, badge=badge)
    if n: xref(x, y, n)

def ghost(x, y, w, h, lines, n=None):
    """A step that no longer exists. Drops below the spine; the flow passes over it."""
    gy, gh = y + 24, h - 22
    add(f'<rect x="{x}" y="{gy}" width="{w}" height="{gh}" rx="6" fill="{PAPER}" '
        f'stroke="{MUT}" stroke-width="1.8" stroke-dasharray="7 5" opacity=".75"/>')
    cy = gy + gh/2 - (len(lines)-1)*16/2 + 5
    for i, ln in enumerate(lines):
        add(f'<text x="{x+w/2}" y="{cy+i*16}" class="bt s" style="fill:{MUT}" '
            f'text-anchor="middle" opacity=".85">{esc(ln)}</text>')
        wl = 7.0*len(ln)
        add(f'<line x1="{x+w/2-wl/2}" y1="{cy+i*16-5}" x2="{x+w/2+wl/2}" y2="{cy+i*16-5}" '
            f'stroke="{MUT}" stroke-width="1.3" opacity=".8"/>')
    lbl(x+w/2, gy+gh+18, "NO LONGER A STEP", "middle", "trg")
    if n: xref(x, gy, n)

# ---- geometry cloned from _flow-soc-full.gen.py so the two sheets overlay ----
DW, DH, W485 = 180, 104, 320
EXW, EXH = 250, 76
GW = 168
GSLOT = GW + GAP
xs = [IX, IX+BW+GAP, IX+2*(BW+GAP), IX+2*(BW+GAP)+DW+GAP,
      IX+2*(BW+GAP)+DW+GAP+W485+GAP, IX+3*(BW+GAP)+DW+GAP+W485+GAP,
      IX+3*(BW+GAP)+2*(DW+GAP)+W485+GAP, IX+4*(BW+GAP)+2*(DW+GAP)+W485+GAP]
BANDW = xs[7] + BW + 30 - BX
P1W = 8*SLOT + GSLOT + 30

W, H = 2830, 1820
begin(W, H, aria=(
    "Start of care, target state, version 1.2, drawn on the same skeleton as the current-state "
    "Flow 1 sheet so the two overlay: the same two passes, the same approved and auth-on-file "
    "decision diamonds, the same entry bus and other-trigger chips, the same exception row, episode "
    "visit budget panel and missed-visit compliance chain. Every block carries the number of the "
    "step it replaces. A dashed empty block marks a step that no longer exists. Light green is the "
    "new capacity and scheduling engine; purple is work that still happens inside HCHB."))

masthead("COMPASSUS HOME HEALTH  ·  FLOW 1 — TARGET STATE  ·  v1.2",
         "Start of Care — where the work goes",
         "Same skeleton as Flow-SOC-Full so the sheets overlay. Numbers map to that sheet's steps")
legend([("Intake", C["intake"]), ("Insurance & Auth", C["auth"]), ("DCS", C["dcs"]),
        ("PCC / Scheduler", C["pcc"]), ("Clinician", C["clin"]), ("HCHB", HCHB),
        ("Capacity & Scheduling Engine", ENG)], x=1310, per_row=7, gap=22)
lbl(W-50, 112, "PROPOSED — TARGET STATE, NOT RELEASE 1   ·   phase 1 is visualisation only (DE-03)",
    "end", "key")

# ---------------- key ----------------
KY = 168
add(f'<rect x="{BX}" y="{KY}" width="{P1W}" height="108" rx="8" fill="#FFFFFF" '
    f'stroke="{RULE}" stroke-width="1.6"/>')
lbl(BX+22, KY+34, "HOW FAR THE ENGINE GOES", cls="colh")
kx = BX + 250
for kind, txt in [("Engine", "the engine does it — a person owns the exception"),
                  ("Assist", "the engine proposes, the named person confirms"),
                  ("Surface", "the engine shows, the person decides"),
                  ("HCHB", "still done inside HCHB — unchanged"),
                  ("Manual", "unchanged — hands on the patient")]:
    y = KY+16
    if kind == "Engine":
        add(f'<rect x="{kx}" y="{y}" width="46" height="26" rx="5" fill="{ENG}"/>')
    elif kind == "Assist":
        add(f'<rect x="{kx}" y="{y}" width="46" height="26" rx="5" fill="{ENG}"/>')
        add(f'<rect x="{kx+32}" y="{y}" width="14" height="26" rx="5" fill="{C["pcc"]}"/>')
    elif kind == "Surface":
        add(f'<rect x="{kx}" y="{y}" width="46" height="26" rx="5" fill="{C["pcc"]}"/>')
        add(f'<rect x="{kx}" y="{y}" width="46" height="10" rx="4" fill="{ENG}"/>')
    elif kind == "HCHB":
        add(f'<rect x="{kx}" y="{y}" width="46" height="26" rx="5" fill="{HCHB}"/>')
    else:
        add(f'<rect x="{kx}" y="{y}" width="46" height="26" rx="5" fill="{C["clin"]}"/>')
    lbl(kx+58, KY+28, kind, cls="colh"); lbl(kx+58, KY+46, txt, cls="note")
    kx += 58 + 8.6*len(txt) + 26
add(f'<line x1="{BX+22}" y1="{KY+62}" x2="{BX+P1W-22}" y2="{KY+62}" stroke="{RULE}" stroke-width="1.2"/>')
lbl(BX+22, KY+92, "READING IT AGAINST THE ORIGINAL", cls="colh")
cx0 = BX + 330
add(f'<rect x="{cx0}" y="{KY+74}" width="30" height="23" rx="5" fill="#FFFFFF" stroke="{MUT}" stroke-width="1.4"/>')
add(f'<text x="{cx0+15}" y="{KY+90}" class="bdg" text-anchor="middle" fill="{MUT}">4</text>')
lbl(cx0+42, KY+90, "the step's position on Flow-SOC-Full  ·  5a / 5b = one step that splits", cls="note")
cx1 = cx0 + 42 + 8.6*68 + 26
add(f'<rect x="{cx1}" y="{KY+74}" width="46" height="23" rx="5" fill="#FFFFFF" stroke="{MUT}" stroke-width="1.4"/>')
add(f'<text x="{cx1+23}" y="{KY+90}" class="bdg" text-anchor="middle" fill="{MUT}">NEW</text>')
lbl(cx1+58, KY+90, "no equivalent there", cls="note")
cx2 = cx1 + 58 + 8.6*20 + 26
add(f'<rect x="{cx2}" y="{KY+74}" width="46" height="23" rx="5" fill="{PAPER}" stroke="{MUT}" '
    f'stroke-width="1.6" stroke-dasharray="5 4"/>')
lbl(cx2+58, KY+90, "a step that no longer exists — the flow passes over it", cls="note")

# ================= PASS 1 =================
P1Y, PH = 306, 242
add(f'<rect x="{BX}" y="{P1Y}" width="{P1W}" height="{PH}" rx="10" fill="{BAND}"/>')
lbl(BX+22, P1Y+34, "PASS 1  ·  START OF CARE / RESUMPTION OF CARE — from the referral", cls="band")
lbl(BX+P1W-14, P1Y+34, "ONE HUMAN GATE LEFT", "end", "bandhi")
p1y = P1Y + 66
c1 = p1y + BH/2
x = IX
eng(x, p1y, BW, BH, ["Referral captured", "in Commure"], n="1")
sublist(x, p1y+BH+26, ["Payer, plan, discharge date", "A verified number, and consent"]); pv=x+BW; x+=SLOT
eng(x, p1y, BW, BH, ["Eligibility verified,", "pending auth derived", "from the payer"], n="2")
arrow(pv, c1, x-6, c1)
lbl(x+BW/2, p1y+BH+30, "traditional Medicare still passes straight", "middle", "note")
lbl(x+BW/2, p1y+BH+50, "through; the rest is derived, not keyed", "middle", "note")
authx=x; pv=x+BW; x+=SLOT
eng(x, p1y, BW, BH, ["Referral released", "to scheduling"], n="3")
sublist(x, p1y+BH+26, ["Completeness is rule-checked", "Exception only → intake"])
arrow(pv, c1, x-6, c1); pv=x+BW; x+=SLOT
ghost(x, p1y, GW, BH, ["DCS reviews", "referral"], n="4"); gx=x; x+=GSLOT
assist(x, p1y, BW, BH, C["dcs"], ["Care team", "recommended"], badge="ASSIST", n="NEW")
sublist(x, p1y+BH+26, ["Discipline, role, restrictions", "DCS and scheduler confirm"])
arrow(pv, c1, x-6, c1); pv=x+BW; x+=SLOT
assist(x, p1y, BW, BH, C["pcc"], ["Welcome contact", "— voice and text"], badge="ASSIST", n="5a")
sublist(x, p1y+BH+26, ["The engine makes contact", "Scheduler works the no-answers"])
arrow(pv, c1, x-6, c1); pv=x+BW; x+=SLOT
surf(x, p1y, BW, BH, C["pcc"], ["Is the patient", "actually available?"], badge="THE JUDGMENT CALL", n="5b")
arrow(pv, c1, x-6, c1)
lbl(x+BW/2, p1y+BH+30, "is the patient actually home? not still", "middle", "note")
lbl(x+BW/2, p1y+BH+50, "inpatient, not deferring admission", "middle", "note")
gatex=x; pv=x+BW; x+=SLOT
assist(x, p1y, BW, BH, C["pcc"], ["Scheduler books", "SOC / ROC visit", "+ discipline evals"],
       badge="ASSIST", n="6")
arrow(pv, c1, x-6, c1); pv=x+BW; x+=SLOT
man(x, p1y, BW, BH, C["clin"], ["Clinicians perform", "SOC / ROC", "+ eval visits"], n="7")
arrow(pv, c1, x-6, c1)
lastp1 = x
path(f"M {gx+GW/2} {c1} L {gx+GW/2} {p1y+24-6}", dash=True)
chip(50, c1-38, 250, 76, ["Referral arrives", "with initial orders"], INK)
arrow(300, c1, IX-6, c1)
lbl(50, c1-52, "TRIGGER", cls="trg")

# ================= PASS 2 — identical xs geometry to the current-state sheet =================
P2Y = P1Y + PH + 150
add(f'<rect x="{BX}" y="{P2Y}" width="{BANDW}" height="{PH}" rx="10" fill="{BAND}"/>')
lbl(BX+22, P2Y+34, "PASS 2  ·  DISCIPLINE PLAN OF CARE — the repeating pattern", cls="band")
lbl(BX+BANDW-14, P2Y+34, "THE BUDGET IS VISIBLE BEFORE IT IS SPENT", "end", "bandhi")
p2y = P2Y + 66
c2 = p2y + BH/2
surf(xs[0], p2y, BW, BH, C["clin"], ["Clinician submits", "discipline plan", "of care"],
     badge="× N disciplines", n="1")
sublist(xs[0], p2y+BH+26, ["The visit budget is shown here", "Payer limits, from the auth note"])
man(xs[1], p2y, BW, BH, C["dcs"], ["DCS reviews &", "approves"], badge="× N disciplines", n="2")
sublist(xs[1], p2y+BH+26, ["QA is a hard stop — it stays"])
diamond(xs[2]+DW/2, c2, ["Approved?"])
man(xs[3], p2y, W485, BH, C["dcs"], ["THE 485 MOMENT", "QA accepted · POC locked",
                                     "485 submitted · orders to MD"], badge="ALL AT ONCE", n="4")
sublist(xs[3], p2y+BH+26, ["Four things, not four gates", "Clear orders auto-adjudicated; gray escalates"])
man(xs[4], p2y, BW, BH, HCHB, ["Visits generate", "in HCHB"], n="5")
diamond(xs[5]+DW/2, c2, ["Auth on", "file?"])
assist(xs[6], p2y, BW, BH, C["pcc"], ["Scheduler assigns all", "plotted visits", "— one pass"],
       badge="ASSIST", n="7")
sublist(xs[6], p2y+BH+26, ["Against the established team", "Scheduler owns urgency"])
man(xs[7], p2y, BW, BH, HCHB, ["Visits on", "clinician calendar"], n="8")
sublist(xs[7], p2y+BH+26, ["Pending visits appear too"])
for a, b in [(xs[0]+BW, xs[1]), (xs[1]+BW, xs[2]), (xs[2]+DW, xs[3]),
             (xs[3]+W485, xs[4]), (xs[4]+BW, xs[5]), (xs[5]+DW, xs[6]), (xs[6]+BW, xs[7])]:
    arrow(a, c2, b-6, c2)
lbl(xs[3]-12, c2-12, "Yes", "end")
lbl(xs[6]-12, c2-12, "Yes", "end")
add(f'<rect x="{xs[2]+8}" y="{c2-DH/2-14}" width="30" height="23" rx="5" fill="#FFFFFF" '
    f'stroke="{MUT}" stroke-width="1.4"/>')
add(f'<text x="{xs[2]+23}" y="{c2-DH/2+2}" class="bdg" text-anchor="middle" fill="{MUT}">3</text>')
add(f'<rect x="{xs[5]+8}" y="{c2-DH/2-14}" width="30" height="23" rx="5" fill="#FFFFFF" '
    f'stroke="{MUT}" stroke-width="1.4"/>')
add(f'<text x="{xs[5]+23}" y="{c2-DH/2+2}" class="bdg" text-anchor="middle" fill="{MUT}">6</text>')

# entry bus + other triggers — cloned
BUS = 316
conn(f"M {lastp1+BW/2} {p1y+BH} L {lastp1+BW/2} {P1Y+PH+72} L {BUS} {P1Y+PH+72} L {BUS} {c2}")
lbl((lastp1+BW/2 + BUS)/2, P1Y+PH+60,
    "after the eval visits, each discipline writes its own plan of care", "middle", "conn")
chip(50, c2-118, 250, 84, ["Recertification", "OASIS recert visit, or", "non-OASIS recert eval"], INK)
chip(50, c2+34, 250, 84, ["Add-on / physician order", "add-on = an added eval;", "other orders change visits"], INK)
lbl(50, c2-134, "OTHER TRIGGERS", cls="trg")
conn(f"M 300 {c2-76} L {BUS} {c2-76} L {BUS} {c2}")
conn(f"M 300 {c2+76} L {BUS} {c2+76} L {BUS} {c2}")
arrow(BUS, c2, xs[0]-6, c2)
tag(50, c2+140, 250, 58, ["The payer's rules, from", "verification days earlier"])
lbl(50, c2+216, "carried forward — surfaced at the plan of care, not at the cap", "start", "note")

# ---------------- exceptions — two survive, two are gone ----------------
exy = P2Y + PH + 54
man(xs[1]-42, exy, EXW, EXH, C["dcs"], ["QA backlog", "visits compress"])
add(f'<rect x="{xs[1]-42+8}" y="{exy-14}" width="30" height="23" rx="5" fill="#FFFFFF" '
    f'stroke="{MUT}" stroke-width="1.4"/>')
add(f'<text x="{xs[1]-42+23}" y="{exy+2}" class="bdg" text-anchor="middle" fill="{MUT}">e1</text>')
man(xs[2]-35, exy, EXW, EXH, C["clin"], ["Returned to clinician", "for correction"])
add(f'<rect x="{xs[2]-35+8}" y="{exy-14}" width="30" height="23" rx="5" fill="#FFFFFF" '
    f'stroke="{MUT}" stroke-width="1.4"/>')
add(f'<text x="{xs[2]-35+23}" y="{exy+2}" class="bdg" text-anchor="middle" fill="{MUT}">e2</text>')
ghost(xs[4]-35, exy-24, EXW, EXH+22, ["one assignment task", "per discipline"], n="e3")
ghost(xs[6]-35, exy-24, EXW+40, EXH+22, ["Pending auth — not on", "calendar, not counted"], n="e4")
path(f"M {xs[1]+58} {p2y+BH} L {xs[1]+58} {exy-6}", dash=True)
path(f"M {xs[2]+DW/2} {c2+DH/2} L {xs[2]+DW/2} {exy-6}", dash=True,
     label="No — nothing moves forward", lx=xs[2]+DW/2+16, ly=exy-22, anchor="start")
path(f"M {xs[5]+DW/2} {c2+DH/2} L {xs[5]+DW/2} {exy-6}", dash=True,
     label="No — but the visit stays visible now", lx=xs[5]+DW/2+16, ly=exy-22, anchor="start")
lbl(50, exy+64, "WHAT USED TO", cls="trg"); lbl(50, exy+82, "FALL OUT", cls="trg")

# ---------------- episode budget — cloned ----------------
py, ph = exy + EXH + 62, 150
panel(xs[1], py, xs[7]+BW-xs[1], ph, "EPISODE VISIT BUDGET — now visible at plan-of-care creation, not at the cap")
chip(xs[1]+26, py+58, 330, 46, ["LUPA floor · too few visits"], C["dcs"])
chip(xs[1]+382, py+58, 400, 46, ["Utilisation ceiling · visits beyond need"], C["dcs"])
lbl(xs[1]+818, py+80, "Fixed 30-day PDGM payment: below the floor the period pays per visit;", cls="note")
lbl(xs[1]+818, py+100, "above the ceiling extra visits earn nothing and consume capacity.", cls="note")
path(f"M {xs[1]+186} {py-6} L {xs[1]+186} {exy+EXH+6}", dash=True)

# ================= MISSED VISIT — cloned, plus two new steps =================
MVY = py + ph + 54
MVW = xs[5] + BW + 30 - BX
add(f'<rect x="{BX}" y="{MVY}" width="{MVW}" height="{PH}" rx="10" fill="{BAND}"/>')
lbl(BX+22, MVY+34, "MISSED VISIT — the compliance chain", cls="band")
lbl(BX+MVW-14, MVY+34, "THE CLOCK BECOMES THE ENGINE'S", "end", "bandhi")
m2y = MVY + 66
c3 = m2y + BH/2
man(xs[0], m2y, BW, BH, C["clin"], ["Clinician documents", "missed visit"], n="1")
eng(xs[1], m2y, BW, BH, ["MD notified inside", "48 hours"], n="2")
sublist(xs[1], m2y+BH+26, ["The engine owns the clock", "Not a workflow someone works"])
diamond(xs[2]+DW/2, c3, ["MD notified", "within 48h?"], w=200)
add(f'<rect x="{xs[2]+8}" y="{c3-DH/2-14}" width="30" height="23" rx="5" fill="#FFFFFF" '
    f'stroke="{MUT}" stroke-width="1.4"/>')
add(f'<text x="{xs[2]+23}" y="{c3-DH/2+2}" class="bdg" text-anchor="middle" fill="{MUT}">3</text>')
man(xs[3], m2y, BW, BH, HCHB, ["Documented", "in HCHB"], n="4")
assist(xs[4], m2y, BW, BH, C["pcc"], ["Rebooking proposed"], badge="ASSIST", n="NEW")
sublist(xs[4], m2y+BH+26, ["Into the week's open room", "Scheduler confirms"])
assist(xs[5], m2y, BW, BH, C["pcc"], ["Follow-up on the", "failed visit"], badge="ASSIST", n="NEW")
sublist(xs[5], m2y+BH+26, ["The contact attempt is logged", "Scheduler owns the outcome"])
arrow(xs[0]+BW, c3, xs[1]-6, c3)
arrow(xs[1]+BW, c3, xs[2]+DW/2-100-6, c3)
arrow(xs[2]+DW/2+100, c3, xs[3]-6, c3)
arrow(xs[3]+BW, c3, xs[4]-6, c3)
arrow(xs[4]+BW, c3, xs[5]-6, c3)
lbl(xs[3]-12, c3-12, "Yes", "end")
chip(50, c3-38, 250, 76, ["Missed visit"], INK)
arrow(300, c3, xs[0]-6, c3)
lbl(50, c3-52, "TRIGGER", cls="trg")
man(xs[2]-35, MVY+PH+62, EXW, EXH, C["dcs"], ["DCS workflow", "48h breach"])
path(f"M {xs[2]+DW/2} {c3+DH/2} L {xs[2]+DW/2} {MVY+PH+44}", dash=True, label="No",
     lx=xs[2]+DW/2+16, ly=MVY+PH+30, anchor="start")

footer("Target state · v1.2 · PROPOSED, not current state — same skeleton as Flow-SOC-Full, posture from the 25 Aug workbook",
       "Flow 1T · start of care — target state")
finish(sys.argv[1] if len(sys.argv) > 1 else "flow1t.svg")
print("last content y", MVY+PH+62+EXH, "| footer rule", H-72, "| pass1 right", BX+P1W)
