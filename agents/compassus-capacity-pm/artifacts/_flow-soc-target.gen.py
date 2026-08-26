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

W, H = 2830, 1780
GW = 168                       # a ghost slot is narrower than a live one
GSLOT = GW + GAP

begin(W, H, aria=(
    "Start of care, target state, version 1.1. Every block carries the number of the step it "
    "replaces on the current-state sheet, so the two can be read side by side. A dashed empty block "
    "marks a step that no longer exists: the DCS referral review in pass one, and the per-discipline "
    "assignment task in pass two. Light green blocks are the new capacity and scheduling engine; "
    "purple blocks are work that still happens inside HCHB. The engine captures the referral, derives "
    "eligibility and pending authorisation from the payer, and releases the referral to scheduling. It "
    "recommends a care team and makes the welcome contact, but confirming the patient is genuinely "
    "available stays the scheduler's decision and nothing books until it clears. In pass two the "
    "clinician plots frequency against a visit budget the engine now shows, the DCS still approves "
    "each plan of care as a hard stop, HCHB still generates the visits and checks authorisation, and "
    "the engine proposes the assignment in one pass."))

masthead("COMPASSUS HOME HEALTH  ·  FLOW 1 — TARGET STATE  ·  v1.1",
         "Start of Care — where the work goes",
         "Read beside Flow-SOC-Full. Numbers map to that sheet's steps; dashed blocks are steps that no longer exist")

legend([("Intake", C["intake"]), ("Insurance & Auth", C["auth"]), ("DCS", C["dcs"]),
        ("PCC / Scheduler", C["pcc"]), ("Clinician", C["clin"]), ("HCHB", HCHB),
        ("Capacity & Scheduling Engine", ENG)], x=1310, per_row=7, gap=22)
lbl(W-50, 112, "PROPOSED — TARGET STATE, NOT RELEASE 1   ·   phase 1 is visualisation only (DE-03)",
    "end", "key")

# ---------------- key: posture, then cross-reference ----------------
KY = 168
BANDW = 8*SLOT + GSLOT + 30
add(f'<rect x="{BX}" y="{KY}" width="{BANDW}" height="108" rx="8" fill="#FFFFFF" '
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
    lbl(kx+58, KY+28, kind, cls="colh")
    lbl(kx+58, KY+46, txt, cls="note")
    kx += 58 + 8.6*len(txt) + 26

add(f'<line x1="{BX+22}" y1="{KY+62}" x2="{BX+BANDW-22}" y2="{KY+62}" stroke="{RULE}" stroke-width="1.2"/>')
lbl(BX+22, KY+92, "READING IT AGAINST THE ORIGINAL", cls="colh")
cx0 = BX + 330
add(f'<rect x="{cx0}" y="{KY+74}" width="30" height="23" rx="5" fill="#FFFFFF" stroke="{MUT}" stroke-width="1.4"/>')
add(f'<text x="{cx0+15}" y="{KY+90}" class="bdg" text-anchor="middle" fill="{MUT}">4</text>')
lbl(cx0+42, KY+90, "the step's position on the current-state sheet, counting left to right", cls="note")
cx1 = cx0 + 42 + 8.6*66 + 30
add(f'<rect x="{cx1}" y="{KY+74}" width="46" height="23" rx="5" fill="#FFFFFF" stroke="{MUT}" stroke-width="1.4"/>')
add(f'<text x="{cx1+23}" y="{KY+90}" class="bdg" text-anchor="middle" fill="{MUT}">NEW</text>')
lbl(cx1+58, KY+90, "no equivalent on the current-state sheet", cls="note")
cx2 = cx1 + 58 + 8.6*39 + 30
add(f'<rect x="{cx2}" y="{KY+74}" width="46" height="23" rx="5" fill="{PAPER}" stroke="{MUT}" '
    f'stroke-width="1.6" stroke-dasharray="5 4"/>')
lbl(cx2+58, KY+90, "a step that no longer exists — the flow passes over it", cls="note")

# ================= PASS 1 =================
P1Y, PH = 306, 244
add(f'<rect x="{BX}" y="{P1Y}" width="{BANDW}" height="{PH}" rx="10" fill="{BAND}"/>')
lbl(BX+22, P1Y+34, "PASS 1  ·  REFERRAL TO THE FIRST VISITS", cls="band")
lbl(BX+BANDW-14, P1Y+34, "ONE HUMAN GATE LEFT", "end", "bandhi")
b1 = P1Y + 68
c1 = b1 + BH/2
# slot walk: 3 engine, ghost, then 5 more
x = IX
eng(x, b1, BW, BH, ["Referral captured", "in Commure"], n="1")
sublist(x, b1+BH+26, ["Payer, plan, discharge date", "A verified number for the",
                      "right person  ·  consent to contact"]); s1e = x+BW; x += SLOT
eng(x, b1, BW, BH, ["Eligibility verified,", "pending auth derived", "from the payer"], n="2")
sublist(x, b1+BH+26, ["Derived, not keyed by hand", "Payer rules ride with the referral"])
authx = x; x += SLOT
eng(x, b1, BW, BH, ["Referral released", "to scheduling"], n="3")
sublist(x, b1+BH+26, ["Completeness is rule-checked", "Exception only → intake"])
prev = x + BW; x += SLOT
ghost(x, b1, GW, BH, ["DCS reviews", "the referral"], n="4")
gx = x; x += GSLOT
assist(x, b1, BW, BH, C["dcs"], ["Care team", "recommended"], badge="ASSIST", n="NEW")
sublist(x, b1+BH+26, ["Discipline, role, restrictions", "Territory · competency · continuity",
                      "DCS and scheduler confirm"])
arrow(prev, c1, x-6, c1)                       # the flow passes over the ghost
nxt = x + BW; x += SLOT
assist(x, b1, BW, BH, C["pcc"], ["Welcome contact", "— voice and text"], badge="ASSIST", n="5a")
sublist(x, b1+BH+26, ["The engine makes contact", "Scheduler works the no-answers",
                      "Asks who may sign — POA"])
arrow(nxt, c1, x-6, c1); nxt = x + BW; x += SLOT
surf(x, b1, BW, BH, C["pcc"], ["Is the patient", "actually available?"],
     badge="THE JUDGMENT CALL", n="5b")
sublist(x, b1+BH+26, ["The engine shows what it heard", "The scheduler decides",
                      "Nothing books until this clears"])
arrow(nxt, c1, x-6, c1); gatex = x; nxt = x + BW; x += SLOT
assist(x, b1, BW, BH, C["pcc"], ["SOC and evals", "scheduled"], badge="ASSIST", n="6")
sublist(x, b1+BH+26, ["48-hour SOC window enforced", "Slots proposed against capacity",
                      "Scheduler confirms"])
arrow(nxt, c1, x-6, c1); nxt = x + BW; x += SLOT
man(x, b1, BW, BH, C["clin"], ["Clinicians perform", "SOC and evals"], n="7")
sublist(x, b1+BH+26, ["RN at the SOC", "PT · OT · ST at their own"])
arrow(nxt, c1, x-6, c1)
arrow(s1e, c1, authx-6, c1)
arrow(authx+BW, c1, authx+SLOT-6, c1)
path(f"M {gx+GW/2} {c1} L {gx+GW/2} {b1+24-6}", dash=True)
chip(50, c1-39, 250, 78, ["Referral arrives", "hospital · MD · facility"], INK)
arrow(300, c1, IX-6, c1)
lbl(50, c1-53, "TRIGGER", cls="trg")

# pass-1 exceptions
E1 = P1Y + PH + 44
EXW2 = 290
block(authx-34, E1, EXW2, 72, C["auth"], ["Payer outside the rules library", "→ the auth team works it"], small=True)
block(gatex-34, E1, EXW2, 72, C["pcc"], ["Not home, or deferring", "→ the referral holds"], small=True)
path(f"M {authx-14} {c1} L {authx-14} {E1-6}", dash=True)
path(f"M {gatex-14} {c1} L {gatex-14} {E1-6}", dash=True)
lbl(50, E1+42, "WHAT FALLS", cls="trg"); lbl(50, E1+60, "TO A PERSON", cls="trg")

# ================= PASS 2 =================
P2Y = E1 + 72 + 50
add(f'<rect x="{BX}" y="{P2Y}" width="{BANDW}" height="{PH}" rx="10" fill="{BAND}"/>')
lbl(BX+22, P2Y+34, "PASS 2  ·  THE PLAN OF CARE", cls="band")
lbl(BX+BANDW-14, P2Y+34, "THE VISIT BUDGET IS VISIBLE BEFORE IT IS SPENT", "end", "bandhi")
b2 = P2Y + 68
c2 = b2 + BH/2
x = IX
surf(x, b2, BW, BH, C["clin"], ["Clinician plots", "discipline frequency"], badge="SURFACE", n="1")
sublist(x, b2+BH+26, ["The visit budget is shown here", "Payer limits, from the auth note",
                      "Clinical need still decides"]); nxt = x+BW; x += SLOT
man(x, b2, BW, BH, C["dcs"], ["DCS approves the", "plan of care"], badge="× N disciplines", n="2·3")
sublist(x, b2+BH+26, ["QA is a hard stop — it stays", "Not approved → visits held"])
arrow(nxt, c2, x-6, c2); dcsx = x; nxt = x+BW; x += SLOT
eng(x, b2, BW, BH, ["Physician orders", "auto-adjudicated"], n="NEW")
sublist(x, b2+BH+26, ["Clear cases clear themselves", "Gray ones escalate to the DCS",
                      "A config choice, not a rule"])
arrow(nxt, c2, x-6, c2); nxt = x+BW; x += SLOT
man(x, b2, BW, BH, C["dcs"], ["THE 485 MOMENT", "QA · lock · submit · orders"], badge="UNCHANGED", n="4")
sublist(x, b2+BH+26, ["Four things, not four gates"])
arrow(nxt, c2, x-6, c2); nxt = x+BW; x += SLOT
man(x, b2, BW, BH, HCHB, ["Visits generate", "in HCHB"], n="5")
sublist(x, b2+BH+26, ["Frequency becomes many visits"])
arrow(nxt, c2, x-6, c2); prev2 = x+BW; x += SLOT
ghost(x, b2, GW, BH, ["one assignment task", "per discipline"], n="5×N")
gx2 = x; x += GSLOT
man(x, b2, BW, BH, HCHB, ["Auth checked per visit", "— pending stays visible"], n="6")
sublist(x, b2+BH+26, ["On the calendar, marked pending", "Counted as committed load",
                      "The engine shows the balance"])
arrow(prev2, c2, x-6, c2); nxt = x+BW; x += SLOT
assist(x, b2, BW, BH, C["pcc"], ["Assignment proposed", "— one pass"], badge="ASSIST", n="7")
sublist(x, b2+BH+26, ["Against the established team", "No task per discipline",
                      "Scheduler owns urgency"])
arrow(nxt, c2, x-6, c2); nxt = x+BW; x += SLOT
man(x, b2, BW, BH, HCHB, ["Visits on the", "clinician's calendar"], n="8")
sublist(x, b2+BH+26, ["Pending visits appear too"])
arrow(nxt, c2, x-6, c2)
path(f"M {gx2+GW/2} {c2} L {gx2+GW/2} {b2+24-6}", dash=True)

tag(50, c2-34, 250, 68, ["The payer's rules, written", "at verification days earlier"])
arrow(312, c2, IX-6, c2)
lbl(50, c2-48, "CARRIED FORWARD", cls="trg")

QD = P2Y + PH + 34
qcx = dcsx + BW + 14
chip(qcx-149, QD, 298, 44, ["Queue depth is visible"], C["dcs"])
lbl(qcx+165, QD+28, "the DCS escalates before the backlog compresses anyone's visits", "start", "note")
path(f"M {qcx} {c2} L {qcx} {QD-6}", dash=True)
lbl(IX, QD+76, "Those rules were written days before anyone plotted a frequency. Surfacing them "
    "here — not at the cap — is the highest-value, lowest-complexity change on this sheet.",
    "start", "hi")

# ================= MISSED VISIT =================
MVY = QD + 76 + 40
mv = [IX + i*SLOT for i in range(5)]
add(f'<rect x="{BX}" y="{MVY}" width="{5*SLOT+30}" height="{PH-30}" rx="10" fill="{BAND}"/>')
lbl(BX+22, MVY+34, "A MISSED VISIT  ·  THE COMPLIANCE CHAIN", cls="band")
lbl(BX+5*SLOT+16, MVY+34, "THE CLOCK BECOMES THE ENGINE'S", "end", "bandhi")
b3 = MVY + 62
c3 = b3 + BH/2
man(mv[0], b3, BW, BH, C["clin"], ["Clinician documents", "the missed visit"], n="1")
eng(mv[1], b3, BW, BH, ["MD notified inside", "48 hours"], n="2·3")
sublist(mv[1], b3+BH+26, ["The engine owns the clock", "Not a workflow someone works"])
assist(mv[2], b3, BW, BH, C["pcc"], ["Rebooking proposed"], badge="ASSIST", n="NEW")
sublist(mv[2], b3+BH+26, ["Into the week's open room", "Scheduler confirms"])
assist(mv[3], b3, BW, BH, C["pcc"], ["Follow-up on the", "failed visit"], badge="ASSIST", n="NEW")
sublist(mv[3], b3+BH+26, ["The contact attempt is logged", "Scheduler owns the outcome"])
man(mv[4], b3, BW, BH, HCHB, ["Documented", "in HCHB"], n="4")
for a in range(4):
    arrow(mv[a]+BW, c3, mv[a+1]-6, c3)
chip(50, c3-24, 250, 48, ["Missed visit"], INK)
arrow(300, c3, IX-6, c3)
block(mv[1]-34, MVY+PH-30+26, EXW2, 72, C["dcs"],
      ["48-hour breach", "→ still escalates to the DCS"], small=True)
path(f"M {mv[1]-14} {c3} L {mv[1]-14} {MVY+PH-30+20}", dash=True)

# ---------------- what stays human ----------------
PY2 = MVY + PH - 30 + 26 + 72 + 44
panel(IX, PY2, 2300, 160,
      "WHAT THE ENGINE MAY ONLY SURFACE — the gating constraints a person still decides")
column_rule(IX+26, PY2+56, PY2+146)
sublist(IX+40, PY2+82, ["Is the patient actually available, before anything books",
                        "The caregiver has to be present  ·  the caregiver's own changing schedule",
                        "Cognitive and dementia constraints  ·  clinically driven timing"])
column_rule(IX+1290, PY2+56, PY2+146, C["dcs"])
sublist(IX+1306, PY2+82, ["Matching acuity to skill level",
                          "Finding coverage when someone calls out",
                          "Every one is a hard constraint, and lives in someone's head today"])

footer("Target state · v1.1 · PROPOSED, not current state — posture per the 25 Aug workbook's future-state column",
       "Flow 1T · start of care — target state")
finish(sys.argv[1] if len(sys.argv) > 1 else "flow1t.svg")
print("last content y", PY2+160, "| footer rule", H-72, "| band right", BX+BANDW)
