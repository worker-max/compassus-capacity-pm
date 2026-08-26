# -*- coding: utf-8 -*-
"""The Episode, End to End — TARGET STATE. v1.1.

Same four phases as the current-state primary map, cross-referenced step by step.
Posture from the 25 Aug workbook's 'Future state — the tool's role' column.
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

W, H = 2830, 1800
GW = 168
GSLOT = GW + GAP

begin(W, H, aria=(
    "The whole home health episode in target state, version 1.1, in four phases, cross-referenced "
    "against the current-state primary map. Every block carries the number of the step it replaces. "
    "A dashed empty block marks a step that no longer exists: the DCS referral review in phase one, "
    "and the per-discipline assignment task in phase two. Light green blocks are the new capacity and "
    "scheduling engine; purple blocks are work that still happens inside HCHB. In phase three the "
    "day-before confirmation becomes automated text and voice instead of the clinician's own evening "
    "calls, while clinical priority and the caregiver constraints stay human decisions."))

masthead("COMPASSUS HOME HEALTH  ·  CAPACITY & SCHEDULING  ·  TARGET STATE  ·  v1.1",
         "The Episode, End to End — where the work goes",
         "Read beside Primary-Flow-Map. Numbers map to that sheet's steps, phase by phase")
legend([("Intake", C["intake"]), ("Insurance & Auth", C["auth"]), ("DCS", C["dcs"]),
        ("PCC / Scheduler", C["pcc"]), ("Clinician", C["clin"]), ("HCHB", HCHB),
        ("Capacity & Scheduling Engine", ENG)], x=1310, per_row=7, gap=22)
lbl(W-50, 112, "PROPOSED — TARGET STATE, NOT RELEASE 1  ·  phase 1 is visualisation only (DE-03)",
    "end", "key")

# ---------------- key ----------------
KY = 168
KW = 8*SLOT + GSLOT + 30
add(f'<rect x="{BX}" y="{KY}" width="{KW}" height="108" rx="8" fill="#FFFFFF" '
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
add(f'<line x1="{BX+22}" y1="{KY+62}" x2="{BX+KW-22}" y2="{KY+62}" stroke="{RULE}" stroke-width="1.2"/>')
lbl(BX+22, KY+92, "READING IT AGAINST THE ORIGINAL", cls="colh")
cx0 = BX + 330
add(f'<rect x="{cx0}" y="{KY+74}" width="30" height="23" rx="5" fill="#FFFFFF" stroke="{MUT}" stroke-width="1.4"/>')
add(f'<text x="{cx0+15}" y="{KY+90}" class="bdg" text-anchor="middle" fill="{MUT}">4</text>')
lbl(cx0+42, KY+90, "the step's position in that phase on the current-state map", cls="note")
cx1 = cx0 + 42 + 8.6*58 + 30
add(f'<rect x="{cx1}" y="{KY+74}" width="46" height="23" rx="5" fill="#FFFFFF" stroke="{MUT}" stroke-width="1.4"/>')
add(f'<text x="{cx1+23}" y="{KY+90}" class="bdg" text-anchor="middle" fill="{MUT}">NEW</text>')
lbl(cx1+58, KY+90, "no equivalent on the current-state map", cls="note")
cx2 = cx1 + 58 + 8.6*38 + 30
add(f'<rect x="{cx2}" y="{KY+74}" width="46" height="23" rx="5" fill="{PAPER}" stroke="{MUT}" '
    f'stroke-width="1.6" stroke-dasharray="5 4"/>')
lbl(cx2+58, KY+90, "a step that no longer exists — the flow passes over it", cls="note")

def phase(y, h, title, right, w):
    add(f'<rect x="{BX}" y="{y}" width="{w}" height="{h}" rx="10" fill="{BAND}"/>')
    lbl(BX+22, y+34, title, cls="band")
    lbl(BX+w-14, y+34, right, "end", "bandhi")

# ================= PHASE 1 =================
AY, AH = 306, 240
AW = 8*SLOT + GSLOT + 30
phase(AY, AH, "PHASE 1  ·  REFERRAL TO ADMISSION", "ONE HUMAN GATE LEFT", AW)
b1 = AY + 66; c1 = b1 + BH/2; x = IX
eng(x, b1, BW, BH, ["Referral captured", "in Commure"], n="1")
sublist(x, b1+BH+26, ["Payer, plan, discharge date", "A verified number, and consent"]); pv=x+BW; x+=SLOT
eng(x, b1, BW, BH, ["Eligibility and pending", "auth derived"], n="2")
sublist(x, b1+BH+26, ["From the payer, not keyed", "Traditional Medicare passes through"])
arrow(pv, c1, x-6, c1); authx=x; pv=x+BW; x+=SLOT
eng(x, b1, BW, BH, ["Released to", "scheduling"], n="3")
sublist(x, b1+BH+26, ["Completeness is rule-checked", "Exception only → intake"])
arrow(pv, c1, x-6, c1); pv=x+BW; x+=SLOT
ghost(x, b1, GW, BH, ["DCS reviews", "the referral"], n="4"); gx=x; x+=GSLOT
assist(x, b1, BW, BH, C["dcs"], ["Care team", "recommended"], badge="ASSIST", n="NEW")
sublist(x, b1+BH+26, ["Discipline, role, restrictions", "DCS and scheduler confirm"])
arrow(pv, c1, x-6, c1); pv=x+BW; x+=SLOT
assist(x, b1, BW, BH, C["pcc"], ["Welcome contact", "— voice and text"], badge="ASSIST", n="5a")
sublist(x, b1+BH+26, ["The engine makes contact", "Scheduler works the no-answers"])
arrow(pv, c1, x-6, c1); pv=x+BW; x+=SLOT
surf(x, b1, BW, BH, C["pcc"], ["Is the patient", "actually available?"], badge="THE HUMAN GATE", n="5b")
sublist(x, b1+BH+26, ["The engine shows what it heard", "The scheduler decides",
                      "Nothing books until this clears"])
arrow(pv, c1, x-6, c1); gatex=x; pv=x+BW; x+=SLOT
assist(x, b1, BW, BH, C["pcc"], ["SOC and evals", "scheduled"], badge="ASSIST", n="6")
sublist(x, b1+BH+26, ["48-hour SOC window enforced", "Scheduler confirms"])
arrow(pv, c1, x-6, c1); pv=x+BW; x+=SLOT
man(x, b1, BW, BH, C["clin"], ["Clinicians perform", "SOC and evals"], n="7")
sublist(x, b1+BH+26, ["RN at the SOC", "PT · OT · ST at their own"])
arrow(pv, c1, x-6, c1)
path(f"M {gx+GW/2} {c1} L {gx+GW/2} {b1+24-6}", dash=True)
chip(50, c1-39, 250, 78, ["Referral arrives", "hospital · MD · facility"], INK)
arrow(300, c1, IX-6, c1); lbl(50, c1-53, "TRIGGER", cls="trg")

# ================= PHASE 2 =================
QY, QH = AY + AH + 34, 240
QW = 7*SLOT + GSLOT + 30
phase(QY, QH, "PHASE 2  ·  THE PLAN OF CARE", "THE BUDGET IS VISIBLE BEFORE IT IS SPENT", QW)
b2 = QY + 66; c2 = b2 + BH/2; x = IX
surf(x, b2, BW, BH, C["clin"], ["Each discipline plots", "its own frequency"], badge="× N", n="1")
sublist(x, b2+BH+26, ["The visit budget is shown here", "Payer limits, from the auth note"]); pv=x+BW; x+=SLOT
man(x, b2, BW, BH, C["dcs"], ["DCS approves the", "plan of care"], badge="× N", n="2")
sublist(x, b2+BH+26, ["QA is a hard stop — it stays", "Not approved → visits held"])
arrow(pv, c2, x-6, c2); pv=x+BW; x+=SLOT
man(x, b2, BW, BH, C["dcs"], ["THE 485 MOMENT", "QA · lock · submit · orders"], badge="UNCHANGED", n="3")
sublist(x, b2+BH+26, ["Four things, not four gates", "Clear orders auto-adjudicated"])
arrow(pv, c2, x-6, c2); pv=x+BW; x+=SLOT
man(x, b2, BW, BH, HCHB, ["Visits generate", "in HCHB"], n="4")
sublist(x, b2+BH+26, ["Frequency becomes many visits"])
arrow(pv, c2, x-6, c2); pv=x+BW; x+=SLOT
ghost(x, b2, GW, BH, ["one assignment task", "per discipline"], n="4×N"); gx2=x; x+=GSLOT
man(x, b2, BW, BH, HCHB, ["Auth checked —", "pending stays visible"], n="NEW")
sublist(x, b2+BH+26, ["On the calendar, marked pending", "The engine shows the balance"])
arrow(pv, c2, x-6, c2); pv=x+BW; x+=SLOT
assist(x, b2, BW, BH, C["pcc"], ["Assignment proposed", "— one pass"], badge="ASSIST", n="5")
sublist(x, b2+BH+26, ["Against the established team", "No task per discipline"])
arrow(pv, c2, x-6, c2); pv=x+BW; x+=SLOT
man(x, b2, BW, BH, HCHB, ["Visits on the", "clinician's calendar"], n="6")
sublist(x, b2+BH+26, ["Pending visits appear too"])
arrow(pv, c2, x-6, c2)
path(f"M {gx2+GW/2} {c2} L {gx2+GW/2} {b2+24-6}", dash=True)
tag(50, c2-34, 250, 68, ["The payer's rules, written", "at verification days earlier"])
arrow(312, c2, IX-6, c2); lbl(50, c2-48, "CARRIED FORWARD", cls="trg")

# ================= PHASE 3 =================
RY, RH = QY + QH + 34, 334
RW = 6*SLOT + 30
phase(RY, RH, "PHASE 3  ·  STEADY STATE — the clinician's week", "THE EVENING CALLS STOP", RW)
b3 = RY + 66; c3 = b3 + BH/2; x = IX
eng(x, b3, BW, BH, ["The week is", "proposed"], n="1")
sublist(x, b3+BH+26, ["Against committed load and", "open room · days off · PTO"]); pv=x+BW; x+=SLOT
surf(x, b3, BW, BH, C["clin"], ["Clinical priority", "across the caseload"], n="2")
sublist(x, b3+BH+26, ["Who is unstable", "Wound · IV · catheter · labs"])
arrow(pv, c3, x-6, c3); pv=x+BW; x+=SLOT
eng(x, b3, BW, BH, ["Grouped and", "routed"], n="3·6")
sublist(x, b3+BH+26, ["Drive time, not distance", "Bridges · rivers · crossings",
                      "Two current steps, merged"])
arrow(pv, c3, x-6, c3); pv=x+BW; x+=SLOT
surf(x, b3, BW, BH, C["clin"], ["What the engine", "can only show"], n="4")
sublist(x, b3+BH+26, ["Caregiver must be present", "Cognitive · dementia constraints",
                      "The caregiver's own schedule"])
arrow(pv, c3, x-6, c3); pv=x+BW; x+=SLOT
eng(x, b3, BW, BH, ["Day-before confirmation", "— text and voice"], badge="THE BIGGEST CHANGE", n="5")
sublist(x, b3+BH+26, ["The engine confirms, not the clinician", "Clinician takes over when it fails"])
arrow(pv, c3, x-6, c3); pv=x+BW; x+=SLOT
assist(x, b3, BW, BH, C["clin"], ["Order within", "the day"], badge="ASSIST", n="NEW")
sublist(x, b3+BH+26, ["The engine proposes the sequence", "The clinician adjusts"])
arrow(pv, c3, x-6, c3)
DY = RY + RH - 74
lbl(IX, DY-12, "THE DAY BEFORE  ·  THE FIVE DISPOSITIONS — chosen a day wide, not at the door", cls="trg")
dx = IX
for t, col in [("Accept", C["clin"]), ("Reschedule", C["clin"]), ("Reassign", C["pcc"]),
               ("Miss", C["dcs"]), ("Decline", C["pcc"])]:
    w = 8.6*len(t) + 64
    chip(dx, DY, w, 42, [t], col); dx += w + 16
lbl(dx + 14, DY+27, "rebooking and failed-visit follow-up are proposed to the scheduler; "
    "the reason a visit was declined is finally captured", "start", "note")

# ================= PHASE 4 =================
SY2, SH2 = RY + RH + 34, 240
SW = 6*SLOT + 30 + 130
phase(SY2, SH2, "PHASE 4  ·  RECERTIFY OR DISCHARGE", "NEW PERIOD = NEW AUTH", SW)
b4 = SY2 + 66; c4 = b4 + BH/2; x = IX
eng(x, b4, BW, BH, ["The recert window", "is tracked"], n="1")
sublist(x, b4+BH+26, ["Days 56–60", "Recert visits are already booked"]); pv=x+BW; x+=SLOT
surf(x, b4, BW, BH, C["clin"], ["Recertifying disciplines", "set the next period"], n="2")
sublist(x, b4+BH+26, ["Discipline by discipline", "Goals met → discharge instead"])
arrow(pv, c4, x-6, c4); pv=x+BW; x+=SLOT
eng(x, b4, BW, BH, ["Auth re-checked for", "the new period"], n="NEW")
sublist(x, b4+BH+26, ["A new period is a new question"])
arrow(pv, c4, x-6, c4); pv=x+BW; x+=SLOT
assist(x, b4, BW, BH, C["pcc"], ["The next period", "is assigned"], badge="ASSIST", n="3")
sublist(x, b4+BH+26, ["Only after frequency is set", "Same one-pass proposal"])
arrow(pv, c4, x-6, c4); pv=x+BW; x+=SLOT
mx = (pv + x)/2
add(f'<line x1="{mx}" y1="{b4-4}" x2="{mx}" y2="{b4+BH+4}" stroke="{MUT}" stroke-width="2" '
    'stroke-dasharray="6 5"/>')
lbl(mx, b4-16, "OR", "middle", "trg")
man(x, b4, BW, BH, C["clin"], ["Or discharge — each", "discipline separately"], n="4")
sublist(x, b4+BH+26, ["Discharges are non-OASIS", "Staggered, not simultaneous"]); pv=x+BW; x+=SLOT
man(x, b4, BW, BH, C["clin"], ["The last discipline out", "does the agency D/C OASIS"], n="5")
sublist(x, b4+BH+26, ["Whoever visits last", "Owner unknown until it happens"])
arrow(pv, c4, x-6, c4)
chip(x+SLOT-28, c4-39, 280, 78, ["Capacity returns", "to the branch"], INK)
arrow(x+BW, c4, x+SLOT-34, c4)

# ---------------- what stays human ----------------
PY2 = SY2 + SH2 + 36
panel(IX, PY2, 2300, 154,
      "WHAT THE ENGINE MAY ONLY SURFACE — the gating constraints a person still decides")
column_rule(IX+26, PY2+54, PY2+140)
sublist(IX+40, PY2+80, ["Is the patient actually available, before anything books",
                        "The caregiver must be present  ·  the caregiver's own changing schedule",
                        "Cognitive and dementia constraints  ·  clinically driven timing"])
column_rule(IX+1290, PY2+54, PY2+140, C["dcs"])
sublist(IX+1306, PY2+80, ["Matching acuity to skill level",
                          "Finding coverage when someone calls out",
                          "Each is a hard constraint that lives in someone's head today"])

footer("Target state · v1.1 · PROPOSED, not current state — posture per the 25 Aug workbook's future-state column",
       "The episode, end to end — target state")
finish(sys.argv[1] if len(sys.argv) > 1 else "episode-target.svg")
print("last content y", PY2+154, "| footer rule", H-72)
