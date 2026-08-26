# -*- coding: utf-8 -*-
"""The Episode, End to End — TARGET STATE. v1.0.

Same four phases as the current-state primary map, with every step marked by how far
the tool may go. Posture vocabulary is the 25 Aug variable workbook's own
'Future state — the tool's role' column: Automate / Assist / Surface / Stays manual.
"""
import sys, os
sys.path.insert(0, os.environ.get("FLOWKIT", "/home/user/compassus-capacity-pm/.claude/skills/process-flow-map/assets"))
from flowkit import *

TOOL = C["hchb"]

def surf(x, y, w, h, person, lines, badge=None):
    block(x, y, w, h, person, lines, badge=badge)
    add(f'<path d="M {x+6} {y} L {x+w-6} {y} A 6 6 0 0 1 {x+w} {y+6} L {x+w} {y+13} '
        f'L {x} {y+13} L {x} {y+6} A 6 6 0 0 1 {x+6} {y} Z" fill="{TOOL}"/>')

def assist(x, y, w, h, person, lines, badge=None):
    split_block(x, y, w, h, TOOL, person, lines)
    if badge:
        bw = 8.3*len(badge)+18
        add(f'<rect x="{x+w-bw-8}" y="{y-14}" width="{bw}" height="23" rx="11.5" '
            f'fill="#FFFFFF" stroke="{person}" stroke-width="1.8"/>')
        add(f'<text x="{x+w-bw/2-8}" y="{y+2}" class="bdg" text-anchor="middle" '
            f'fill="{person}">{esc(badge)}</text>')

def trow(y, steps, x0=IX, breaks=()):
    """steps: (kind, colour, lines, subs|None, badge|None, slots).
    kind: auto | assist | surf | man."""
    x, cy, prev = x0, y + BH/2, None
    for i, (kind, col, lines, subs, badge, slots) in enumerate(steps):
        w = slots*SLOT - GAP
        if kind == "auto":
            block(x, y, w, BH, TOOL, lines, badge=badge)
        elif kind == "assist":
            assist(x, y, w, BH, col, lines, badge=badge)
        elif kind == "surf":
            surf(x, y, w, BH, col, lines, badge=badge)
        else:
            block(x, y, w, BH, col, lines, badge=badge)
        if subs:
            sublist(x, y+BH+26, subs)
        if prev is not None:
            if i in breaks:
                mx = (prev + x)/2
                add(f'<line x1="{mx}" y1="{y-4}" x2="{mx}" y2="{y+BH+4}" stroke="{MUT}" '
                    'stroke-width="2" stroke-dasharray="6 5"/>')
                lbl(mx, y-16, "OR", "middle", "trg")
            else:
                arrow(prev, cy, x-6, cy)
        prev = x + w
        x += slots*SLOT
    return cy

W, H = 2450, 1690
begin(W, H, aria=(
    "The whole home health episode in target state, in four phases. Phase one, referral to admission: "
    "capture, eligibility and pending authorisation, and release to scheduling are automated; the care "
    "team and the welcome contact are proposed by the tool and confirmed by a person; confirming the "
    "patient is genuinely available stays a human decision and nothing books until it clears. Phase two, "
    "the plan of care: each discipline plots frequency against a visit budget the tool now shows, the DCS "
    "still approves each plan of care as a hard stop, the 485 moment is unchanged, visits generate, "
    "authorisation is checked with pending visits staying visible, and assignment is proposed in one pass. "
    "Phase three, steady state: the week is proposed against committed load, routing is automated, and the "
    "day-before confirmation becomes automated text and voice instead of the clinician's own evening calls "
    "— but clinical priority and the caregiver constraints stay human. Phase four: the recertification "
    "window is tracked by the tool, each discipline still decides for itself, and a new period is a new "
    "authorisation question."))

masthead("COMPASSUS HOME HEALTH  ·  CAPACITY & SCHEDULING  ·  TARGET STATE  ·  v1.0",
         "The Episode, End to End — where the work goes",
         "The same four phases as the current-state map, with every step marked by how far the tool may go")
legend([("Intake", C["intake"]), ("Insurance & Auth", C["auth"]), ("DCS", C["dcs"]),
        ("PCC / Scheduler", C["pcc"]), ("Clinician", C["clin"]), ("The tool", TOOL)],
       x=1290, per_row=6, gap=22)
lbl(W-50, 112, "PROPOSED — TARGET STATE, NOT RELEASE 1  ·  phase 1 is visualisation only (DE-03)",
    "end", "key")

# ---------------- posture key ----------------
KY = 172
add(f'<rect x="{BX}" y="{KY}" width="{7*SLOT+30}" height="60" rx="8" fill="#FFFFFF" '
    f'stroke="{RULE}" stroke-width="1.6"/>')
lbl(BX+20, KY+36, "HOW FAR THE TOOL GOES", cls="colh")
kx = BX + 232
for kind, txt in [("Automate", "the tool does it — a person owns the exception"),
                  ("Assist", "the tool proposes, a person confirms"),
                  ("Surface", "the tool shows, the person decides"),
                  ("Manual", "unchanged — hands on the patient")]:
    y = KY+17
    if kind == "Automate":
        add(f'<rect x="{kx}" y="{y}" width="44" height="26" rx="5" fill="{TOOL}"/>')
    elif kind == "Assist":
        add(f'<rect x="{kx}" y="{y}" width="44" height="26" rx="5" fill="{TOOL}"/>')
        add(f'<rect x="{kx+22}" y="{y}" width="22" height="26" rx="5" fill="{C["pcc"]}"/>')
    elif kind == "Surface":
        add(f'<rect x="{kx}" y="{y}" width="44" height="26" rx="5" fill="{C["pcc"]}"/>')
        add(f'<rect x="{kx}" y="{y}" width="44" height="9" rx="4" fill="{TOOL}"/>')
    else:
        add(f'<rect x="{kx}" y="{y}" width="44" height="26" rx="5" fill="{C["clin"]}"/>')
    lbl(kx+54, KY+29, kind, cls="colh")
    lbl(kx+54, KY+47, txt, cls="note")
    kx += 54 + 8.6*len(txt) + 26

# ================= PHASE 1 =================
AY, AH = 262, 236
band(AY, AH, "PHASE 1  ·  REFERRAL TO ADMISSION", "ONE HUMAN GATE LEFT", slots=7)
ac = trow(AY+62, [
 ("auto", None, ["Referral captured", "in Commure"],
  ["Payer, plan, discharge date", "A verified number, and consent"], None, 1),
 ("auto", None, ["Eligibility and pending", "auth derived"],
  ["From the payer, not keyed", "Traditional Medicare passes through"], None, 1),
 ("auto", None, ["Released to", "scheduling"],
  ["Completeness is rule-checked", "Exception only → intake"], None, 1),
 ("assist", C["dcs"], ["Care team", "recommended"],
  ["Discipline, role, restrictions", "Territory · competency · continuity"], "ASSIST", 1),
 ("assist", C["pcc"], ["Welcome contact", "— voice and text"],
  ["The tool makes contact", "Scheduler works the no-answers"], "ASSIST", 1),
 ("surf", C["pcc"], ["Is the patient", "actually available?"],
  ["The tool shows what it heard", "The scheduler decides", "Nothing books until this clears"],
  "THE HUMAN GATE", 1),
 ("assist", C["pcc"], ["SOC and evals", "scheduled"],
  ["48-hour SOC window enforced", "Scheduler confirms"], "ASSIST", 1),
])
chip(50, ac-39, 250, 78, ["Referral arrives", "hospital · MD · facility"], INK)
arrow(300, ac, IX-6, ac)
lbl(50, ac-53, "TRIGGER", cls="trg")

# ================= PHASE 2 =================
QY, QH = AY + AH + 34, 236
band(QY, QH, "PHASE 2  ·  THE PLAN OF CARE", "THE BUDGET IS VISIBLE BEFORE IT IS SPENT", slots=7)
qc = trow(QY+62, [
 ("surf", C["clin"], ["Each discipline plots", "its own frequency"],
  ["The visit budget is shown here", "Payer limits, from the auth note",
   "Clinical need still decides"], "× N disciplines", 1),
 ("man", C["dcs"], ["DCS approves the", "plan of care"],
  ["QA is a hard stop — it stays", "Not approved → visits held"], "× N disciplines", 1),
 ("man", C["dcs"], ["THE 485 MOMENT", "QA accepted · POC locked", "485 submitted · orders to MD"],
  ["Four things, not four gates", "Clear orders auto-adjudicated; gray escalates"], "UNCHANGED", 2),
 ("auto", None, ["Visits generate"],
  ["Frequency becomes many visits"], None, 1),
 ("auto", None, ["Auth checked —", "pending stays visible"],
  ["On the calendar, marked pending", "Counted as committed load"], None, 1),
 ("assist", C["pcc"], ["Assignment proposed", "— one pass"],
  ["Against the established team", "No task per discipline"], "ASSIST", 1),
])
tag(50, qc-34, 250, 68, ["The payer's rules, written", "at verification days earlier"])
arrow(300, qc, IX-6, qc)
lbl(50, qc-48, "CARRIED FORWARD", cls="trg")

# ================= PHASE 3 =================
RY, RH = QY + QH + 34, 318
band(RY, RH, "PHASE 3  ·  STEADY STATE — the clinician's week",
     "THE EVENING CALLS STOP", slots=7)
rc = trow(RY+62, [
 ("auto", None, ["The week is", "proposed"],
  ["Against committed load and", "open room · days off · PTO"], None, 1),
 ("surf", C["clin"], ["Clinical priority", "across the caseload"],
  ["Who is unstable", "Wound · IV · catheter · labs"], None, 1),
 ("auto", None, ["Grouped and", "routed"],
  ["Drive time, not distance", "Bridges · rivers · crossings"], None, 1),
 ("surf", C["clin"], ["What the tool can", "only show"],
  ["Caregiver must be present", "Cognitive · dementia constraints",
   "The caregiver's own schedule"], None, 1),
 ("auto", None, ["Day-before confirmation", "— text and voice"],
  ["The tool confirms, not the clinician", "Clinician takes over when it fails"],
  "THE BIGGEST CHANGE", 1),
 ("assist", C["clin"], ["Order within", "the day"],
  ["The tool proposes the sequence", "The clinician adjusts"], "ASSIST", 1),
])
# dispositions strip inside the band
DY = RY + RH - 78
lbl(IX, DY-12, "THE DAY BEFORE  ·  THE FIVE DISPOSITIONS — chosen a day wide, not at the door", cls="trg")
dx = IX
for t, col in [("Accept", C["clin"]), ("Reschedule", C["clin"]), ("Reassign", C["pcc"]),
               ("Miss", C["dcs"]), ("Decline", C["pcc"])]:
    w = 8.6*len(t) + 64
    chip(dx, DY, w, 42, [t], col)
    dx += w + 16
lbl(dx + 14, DY+27, "rebooking and failed-visit follow-up are proposed to the scheduler; "
    "the reason a visit was declined is finally captured", "start", "note")

# ================= PHASE 4 =================
SY2, SH2 = RY + RH + 34, 236
band(SY2, SH2, "PHASE 4  ·  RECERTIFY OR DISCHARGE", "NEW PERIOD = NEW AUTH", slots=7)
sc = trow(SY2+62, [
 ("surf", C["clin"], ["Each discipline reviews", "its own goals"],
  ["Decided separately", "Some discharge before recert"], None, 1),
 ("auto", None, ["The recert window", "is tracked"],
  ["Days 56–60", "Binds only recertifying disciplines"], None, 1),
 ("man", C["clin"], ["Recert visits", "performed"],
  ["One carries the OASIS recert", "The others are non-OASIS"], None, 1),
 ("man", C["dcs"], ["DCS approves the", "next-period plan"],
  ["The same hard stop as phase 2"], "× N disciplines", 1),
 ("auto", None, ["Auth re-checked for", "the new period"],
  ["A new period is a new question"], None, 1),
 ("assist", C["pcc"], ["The next period", "is assigned"],
  ["Same one-pass proposal"], "ASSIST", 1),
 ("man", C["clin"], ["Or — the agency", "discharge"],
  ["The last discipline out does", "the D/C OASIS", "Capacity returns to the branch"], None, 1),
], breaks=(6,))

# ---------------- what stays human ----------------
PY2 = SY2 + SH2 + 36
panel(IX, PY2, 1976, 150,
      "WHAT THE TOOL MAY ONLY SURFACE — the gating constraints a person still decides")
column_rule(IX+26, PY2+52, PY2+136)
sublist(IX+40, PY2+78, ["Is the patient actually available, before anything books",
                        "The caregiver must be present  ·  the caregiver's own changing schedule",
                        "Cognitive and dementia constraints  ·  clinically driven timing"])
column_rule(IX+1090, PY2+52, PY2+136, C["dcs"])
sublist(IX+1106, PY2+78, ["Matching acuity to skill level",
                          "Finding coverage when someone calls out",
                          "Each is a hard constraint that lives in someone's head today"])

footer("Target state · v1.0 · PROPOSED, not current state — posture per the 25 Aug workbook's future-state column",
       "The episode, end to end — target state")
finish(sys.argv[1] if len(sys.argv) > 1 else "episode-target.svg")
print("last content y", PY2+150, "| footer rule", H-72)
