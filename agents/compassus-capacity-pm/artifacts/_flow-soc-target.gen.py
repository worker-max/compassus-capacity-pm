# -*- coding: utf-8 -*-
"""Flow 1T — Start of Care, TARGET STATE. v1.0.

Posture vocabulary is the 25 Aug variable workbook's own 'Future state — the tool's
role' column: Automate / Assist / Surface / Stays manual. Colour still = actor, so an
Assist or Surface block keeps the colour of the person who decides.
"""
import sys, os
sys.path.insert(0, os.environ.get("FLOWKIT", "/home/user/compassus-capacity-pm/.claude/skills/process-flow-map/assets"))
from flowkit import *

TOOL = C["hchb"]          # purple = the tool acting on its own

def surf(x, y, w, h, person, lines, badge=None):
    """SURFACE — the tool shows it, the person decides. Person's block, tool's stripe."""
    block(x, y, w, h, person, lines, badge=badge)
    add(f'<path d="M {x+6} {y} L {x+w-6} {y} A 6 6 0 0 1 {x+w} {y+6} L {x+w} {y+13} '
        f'L {x} {y+13} L {x} {y+6} A 6 6 0 0 1 {x+6} {y} Z" fill="{TOOL}"/>')

def assist(x, y, w, h, person, lines, badge=None):
    """ASSIST — the tool proposes, the person confirms."""
    split_block(x, y, w, h, TOOL, person, lines)
    if badge:
        bw = 8.3*len(badge)+18
        add(f'<rect x="{x+w-bw-8}" y="{y-14}" width="{bw}" height="23" rx="11.5" '
            f'fill="#FFFFFF" stroke="{person}" stroke-width="1.8"/>')
        add(f'<text x="{x+w-bw/2-8}" y="{y+2}" class="bdg" text-anchor="middle" '
            f'fill="{person}">{esc(badge)}</text>')

W, H = 2700, 1680
begin(W, H, aria=(
    "Start of care, target state. Pass one: the referral is captured with payer, discharge date, "
    "power-of-attorney flag and a verified contact number; eligibility and pending authorisation are "
    "derived from the payer rather than keyed; the referral releases to scheduling by rule; the tool "
    "recommends a care team and the DCS and scheduler confirm it; an automated voice and text contact "
    "reaches the patient; but confirming the patient is genuinely available stays a human decision, and "
    "nothing books until it clears; the tool then proposes the start-of-care and evaluation slots and the "
    "scheduler confirms; clinicians perform the visits. Pass two: the clinician plots frequency against a "
    "visit budget the tool now shows, the DCS still approves each discipline's plan of care as a hard stop, "
    "physician orders are auto-adjudicated with gray cases escalating, the 485 moment is unchanged, visits "
    "generate, authorisation is checked per visit and pending visits stay visible on the calendar, and "
    "assignment is proposed in one pass against the established care team with the scheduler confirming. "
    "A missed visit runs an automated 48-hour notification with rebooking and follow-up proposed to the "
    "scheduler. Seven gating constraints remain human decisions the tool may only surface."))

masthead("COMPASSUS HOME HEALTH  ·  FLOW 1 — TARGET STATE  ·  v1.0",
         "Start of Care — where the work goes",
         "The same flow as the current-state sheet, with every step marked by how far the tool may go")

legend([("Intake", C["intake"]), ("Insurance & Auth", C["auth"]), ("DCS", C["dcs"]),
        ("PCC / Scheduler", C["pcc"]), ("Clinician", C["clin"]), ("The tool", TOOL)],
       x=1520, per_row=6, gap=26)
lbl(W-50, 112, "PROPOSED — TARGET STATE, NOT RELEASE 1   ·   phase 1 is visualisation only (DE-03)",
    "end", "key")

# ---------------- posture key ----------------
KY = 172
add(f'<rect x="{BX}" y="{KY}" width="{8*SLOT+30}" height="62" rx="8" fill="#FFFFFF" '
    f'stroke="{RULE}" stroke-width="1.6"/>')
lbl(BX+22, KY+37, "HOW FAR THE TOOL GOES", cls="colh")
kx = BX + 240
def keyswatch(x, kind):
    y = KY+18
    if kind == "Automate":
        add(f'<rect x="{x}" y="{y}" width="46" height="26" rx="5" fill="{TOOL}"/>')
    elif kind == "Assist":
        add(f'<rect x="{x}" y="{y}" width="46" height="26" rx="5" fill="{TOOL}"/>')
        add(f'<rect x="{x+23}" y="{y}" width="23" height="26" rx="5" fill="{C["pcc"]}"/>')
    elif kind == "Surface":
        add(f'<rect x="{x}" y="{y}" width="46" height="26" rx="5" fill="{C["pcc"]}"/>')
        add(f'<rect x="{x}" y="{y}" width="46" height="9" rx="4" fill="{TOOL}"/>')
    else:
        add(f'<rect x="{x}" y="{y}" width="46" height="26" rx="5" fill="{C["clin"]}"/>')
for kind, txt in [("Automate", "the tool does it — a person owns the exception"),
                  ("Assist", "the tool proposes, a person confirms"),
                  ("Surface", "the tool shows, the person decides"),
                  ("Manual", "unchanged — clinical judgment, or hands on the patient")]:
    keyswatch(kx, kind)
    lbl(kx+58, KY+30, kind, cls="colh")
    lbl(kx+58, KY+48, txt, cls="note")
    kx += 58 + 8.6*len(txt) + 30

# ================= PASS 1 =================
P1Y, PH = 268, 232
p1 = [IX + i*SLOT for i in range(8)]
add(f'<rect x="{BX}" y="{P1Y}" width="{8*SLOT+30}" height="{PH}" rx="10" fill="{BAND}"/>')
lbl(BX+22, P1Y+34, "PASS 1  ·  REFERRAL TO THE FIRST VISITS", cls="band")
lbl(BX+8*SLOT+16, P1Y+34, "ONE HUMAN GATE LEFT", "end", "bandhi")
b1 = P1Y + 66
c1 = b1 + BH/2

block(p1[0], b1, BW, BH, TOOL, ["Referral captured", "in Commure"])
sublist(p1[0], b1+BH+26, ["Payer, plan, discharge date", "A verified number for the",
                          "right person  ·  consent to contact"])
block(p1[1], b1, BW, BH, TOOL, ["Eligibility verified,", "pending auth derived", "from the payer"])
sublist(p1[1], b1+BH+26, ["Derived, not keyed by hand", "Payer rules ride with the referral"])
block(p1[2], b1, BW, BH, TOOL, ["Referral released", "to scheduling"])
sublist(p1[2], b1+BH+26, ["Completeness is rule-checked", "Exception only → intake"])
assist(p1[3], b1, BW, BH, C["dcs"], ["Care team", "recommended"], badge="ASSIST")
sublist(p1[3], b1+BH+26, ["Discipline, role, restrictions", "Territory · competency · continuity",
                          "DCS and scheduler confirm"])
assist(p1[4], b1, BW, BH, C["pcc"], ["Welcome contact", "— voice and text"], badge="ASSIST")
sublist(p1[4], b1+BH+26, ["The tool makes contact", "Scheduler works the no-answers",
                          "Asks who may sign — POA"])
surf(p1[5], b1, BW, BH, C["pcc"], ["Is the patient", "actually available?"],
     badge="STILL THE JUDGMENT CALL")
sublist(p1[5], b1+BH+26, ["The tool shows what it heard", "The scheduler decides",
                          "Nothing books until this clears"])
assist(p1[6], b1, BW, BH, C["pcc"], ["SOC and evals", "scheduled"], badge="ASSIST")
sublist(p1[6], b1+BH+26, ["48-hour SOC window enforced", "Slots proposed against capacity",
                          "Scheduler confirms"])
block(p1[7], b1, BW, BH, C["clin"], ["Clinicians perform", "SOC and evals"])
sublist(p1[7], b1+BH+26, ["RN at the SOC", "PT · OT · ST at their own"])
for a in range(7):
    arrow(p1[a]+BW, c1, p1[a+1]-6, c1)
chip(50, c1-39, 250, 78, ["Referral arrives", "hospital · MD · facility"], INK)
arrow(300, c1, IX-6, c1)
lbl(50, c1-53, "TRIGGER", cls="trg")

# pass-1 exceptions — drop from the gap ABOVE each block, onto its top edge
E1 = P1Y + PH + 44
EXW2 = 290
ex1x, ex2x = p1[1]-34, p1[5]-34
block(ex1x, E1, EXW2, 72, C["auth"], ["Payer outside the rules library", "→ the auth team works it"], small=True)
block(ex2x, E1, EXW2, 72, C["pcc"], ["Not home, or deferring", "→ the referral holds"], small=True)
path(f"M {p1[1]-14} {c1} L {p1[1]-14} {E1-6}", dash=True)
path(f"M {p1[5]-14} {c1} L {p1[5]-14} {E1-6}", dash=True)
lbl(50, E1+42, "WHAT FALLS", cls="trg"); lbl(50, E1+60, "TO A PERSON", cls="trg")

# ================= PASS 2 =================
P2Y = E1 + 72 + 50
p2 = [IX + i*SLOT for i in range(8)]
add(f'<rect x="{BX}" y="{P2Y}" width="{8*SLOT+30}" height="{PH}" rx="10" fill="{BAND}"/>')
lbl(BX+22, P2Y+34, "PASS 2  ·  THE PLAN OF CARE", cls="band")
lbl(BX+8*SLOT+16, P2Y+34, "THE VISIT BUDGET IS VISIBLE BEFORE IT IS SPENT", "end", "bandhi")
b2 = P2Y + 66
c2 = b2 + BH/2

surf(p2[0], b2, BW, BH, C["clin"], ["Clinician plots", "discipline frequency"], badge="SURFACE")
sublist(p2[0], b2+BH+26, ["The visit budget is shown here", "Payer limits, from the auth note",
                          "Clinical need still decides"])
block(p2[1], b2, BW, BH, C["dcs"], ["DCS approves the", "plan of care"], badge="× N disciplines")
sublist(p2[1], b2+BH+26, ["QA is a hard stop — it stays", "Not approved → visits held"])
block(p2[2], b2, BW, BH, TOOL, ["Physician orders", "auto-adjudicated"])
sublist(p2[2], b2+BH+26, ["Clear cases clear themselves", "Gray ones escalate to the DCS",
                          "A config choice, not a rule"])
block(p2[3], b2, BW, BH, C["dcs"], ["THE 485 MOMENT", "QA · lock · submit · orders"], badge="UNCHANGED")
sublist(p2[3], b2+BH+26, ["Four things, not four gates"])
block(p2[4], b2, BW, BH, TOOL, ["Visits generate"])
sublist(p2[4], b2+BH+26, ["Frequency becomes many visits"])
block(p2[5], b2, BW, BH, TOOL, ["Auth checked per visit", "— pending stays visible"])
sublist(p2[5], b2+BH+26, ["On the calendar, marked pending", "Counted as committed load",
                          "The balance is on screen"])
assist(p2[6], b2, BW, BH, C["pcc"], ["Assignment proposed", "— one pass"], badge="ASSIST")
sublist(p2[6], b2+BH+26, ["Against the established team", "No task per discipline",
                          "Scheduler owns urgency"])
block(p2[7], b2, BW, BH, C["clin"], ["Visits on the", "clinician's calendar"])
sublist(p2[7], b2+BH+26, ["Pending visits appear too"])
for a in range(7):
    arrow(p2[a]+BW, c2, p2[a+1]-6, c2)

# the payer-rule feeder — grey reference data in the left margin, per the house idiom
tag(50, c2-34, 262, 68, ["The payer's rules, written", "at verification days earlier"])
arrow(312, c2, p2[0]-6, c2)
lbl(50, c2-48, "CARRIED FORWARD", cls="trg")

# queue depth, surfaced — a watch condition, not a step
QD = P2Y + PH + 34
qcx = p2[1] + BW + 14
chip(qcx-149, QD, 298, 44, ["Queue depth is visible"], C["dcs"])
lbl(qcx+165, QD+28, "the DCS escalates before the backlog compresses anyone's visits", "start", "note")
path(f"M {qcx} {c2} L {qcx} {QD-6}", dash=True)
lbl(IX, QD+76, "Those rules were written days before anyone plotted a frequency. Surfacing them "
    "here — not at the cap — is the highest-value, lowest-complexity change on this sheet.",
    "start", "hi")

# ================= MISSED VISIT =================
MVY = QD + 76 + 40
mv = [IX + i*SLOT for i in range(5)]
add(f'<rect x="{BX}" y="{MVY}" width="{5*SLOT+30}" height="{PH-24}" rx="10" fill="{BAND}"/>')
lbl(BX+22, MVY+34, "A MISSED VISIT  ·  THE COMPLIANCE CHAIN", cls="band")
lbl(BX+5*SLOT+16, MVY+34, "THE CLOCK BECOMES THE TOOL'S", "end", "bandhi")
b3 = MVY + 62
c3 = b3 + BH/2
block(mv[0], b3, BW, BH, C["clin"], ["Clinician documents", "the missed visit"])
block(mv[1], b3, BW, BH, TOOL, ["MD notified inside", "48 hours"])
sublist(mv[1], b3+BH+26, ["The tool owns the clock", "Not a workflow someone works"])
assist(mv[2], b3, BW, BH, C["pcc"], ["Rebooking proposed"], badge="ASSIST")
sublist(mv[2], b3+BH+26, ["Into the week's open room", "Scheduler confirms"])
assist(mv[3], b3, BW, BH, C["pcc"], ["Follow-up on the", "failed visit"], badge="ASSIST")
sublist(mv[3], b3+BH+26, ["The contact attempt is logged", "Scheduler owns the outcome"])
block(mv[4], b3, BW, BH, TOOL, ["Documented", "in the record"])
for a in range(4):
    arrow(mv[a]+BW, c3, mv[a+1]-6, c3)
chip(50, c3-24, 250, 48, ["Missed visit"], INK)
arrow(300, c3, IX-6, c3)
block(mv[1]-34, MVY+PH-24+26, EXW2, 72, C["dcs"],
      ["48-hour breach", "→ still escalates to the DCS"], small=True)
path(f"M {mv[1]-14} {c3} L {mv[1]-14} {MVY+PH-24+20}", dash=True)

# ---------------- what stays human ----------------
PY2 = MVY + PH - 24 + 26 + 72 + 44
panel(IX, PY2, 2170, 160,
      "WHAT THE TOOL MAY ONLY SURFACE — the gating constraints a person still decides")
column_rule(IX+26, PY2+56, PY2+146)
sublist(IX+40, PY2+82, ["Is the patient actually available, before anything books",
                        "The caregiver has to be present  ·  the caregiver's own changing schedule",
                        "Cognitive and dementia constraints  ·  clinically driven timing"])
column_rule(IX+1210, PY2+56, PY2+146, C["dcs"])
sublist(IX+1226, PY2+82, ["Matching acuity to skill level",
                          "Finding coverage when someone calls out",
                          "Every one is a hard constraint, and lives in someone's head today"])

footer("Target state · v1.0 · PROPOSED, not current state — posture per the 25 Aug workbook's future-state column",
       "Flow 1T · start of care — target state")
finish(sys.argv[1] if len(sys.argv) > 1 else "flow1t.svg")
print("last content y", PY2+160, "| footer rule", H-72)
