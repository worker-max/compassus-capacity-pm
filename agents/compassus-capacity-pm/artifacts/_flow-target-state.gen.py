# -*- coding: utf-8 -*-
"""Target-state map — the FIRST non-current-state sheet in the set.
The footer convention is deliberately inverted. Canvas units = points on the sheet."""
import pathlib
import sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3]
                       / ".claude" / "skills" / "process-flow-map" / "assets"))
from flowkit import *  # noqa

W, H = 2300, 1840
RETX = 2150                       # the return path runs outside every band

begin(W, H, aria=(
 "The target-state home health capacity and scheduling map. A standing capacity envelope sits above "
 "the episode and is consulted at the referral decision; the episode then runs in four phases — "
 "referral to admission, plan of care, the clinician's week, and recertification or discharge — with "
 "discharge returning room to the envelope. Every step is marked with the release that delivers it "
 "and how far the system is permitted to go: read, assist, or control."))

masthead("COMPASSUS HOME HEALTH  ·  CAPACITY & SCHEDULING  ·  TARGET STATE",
         "The Envelope, and the Episode Run Against It",
         "Capacity measured first · scheduling and engagement performed against it · "
         "every step marked with its release and its posture", w=W)
legend([("Intake", C["intake"]), ("Insurance & Auth", C["auth"]), ("PCC / Scheduler", C["pcc"]),
        ("DCS", C["dcs"]), ("Clinician", C["clin"]), ("The platform", C["hchb"]),
        ("Per Diem / Float", C["float_"]), ("Branch Leadership", C["lead"])], 1600, per_row=4)

# ============ BAND 0 — THE ENVELOPE (the MVP) ============
EY, EH = 188, 232
E_R = band(EY, EH, "THE ENVELOPE  ·  CAPACITY MANAGEMENT",
           "VISUALISATION ONLY  ·  DE-03", slots=5)
eb = EY + 62
row(eb, [
 (C["lead"], ["Roster, availability", "territory"],
  ["Who we have, where they reach", "PTO flows in, never re-keyed"], "MVP · READ", 1),
 (C["lead"], ["The capacity math", "points, targets, ceilings"],
  ["Point value per visit type", "Target and ceiling per clinician"], "MVP · READ", 1),
 (C["lead"], ["Committed load", "vs. open room"],
  ["By day, week, discipline, zone", "The grid it replaces is retired"], "MVP · READ", 1),
 (C["lead"], ["Assessing capacity", "by discipline"],
  ["SOC-capable clinicians, apart", "The number that gates growth"], "MVP · READ", 1),
 (C["hchb"], ["Referral inflow", "discharge outflow"],
  ["What arrives, what leaves", "Measured against the envelope"], "MVP · READ", 1),
])
lbl(IX, EY+EH-12, "★  The MVP is this band and only this band — 19 of 79 variables.  "
    "Nothing here decides anything. It reports.", cls="hi")

# ============ PHASE 1 — REFERRAL TO ADMISSION ============
AY, AH = 450, 234
band(AY, AH, "PHASE 1  ·  REFERRAL TO ADMISSION", "THE CAPACITY READ BECOMES A REAL ANSWER", slots=6)
ab = AY + 62
row(ab, [
 (C["intake"], ["Intake receives", "the referral"],
  ["In Commure", "Payer and plan captured"], "V2 · ASSIST", 1),
 (C["auth"], ["Auth verifies and surfaces", "the payer rules"],
  ["The rules already exist in a note", "Now they travel with the referral"], "V2 · ASSIST", 1),
 (C["lead"], ["Capacity read", "can we accept?"],
  ["Reads the envelope above", "Right discipline, right zip", "A person still decides"], "MVP · READ", 1),
 (C["pcc"], ["Care team assigned", "at referral"],
  ["System recommends the team", "A human approves or edits", "DE-05"], "V2 · ASSIST", 1),
 (C["pcc"], ["Welcome call and", "availability capture"],
  ["Is the patient actually home?", "Asked before booking"], "V3 · ASSIST", 1),
 (C["pcc"], ["SOC and discipline", "evals booked"],
  ["SOC first", "Evals one to two days later"], "V2 · ASSIST", 1),
])
CAPX = IX + 2*SLOT + (SLOT-GAP)/2
path(f"M {CAPX} {EY+EH-2} L {CAPX} {ab-8}")
lbl(CAPX+16, (EY+EH+ab)/2 + 4, "consults the envelope", cls="trg")

# ============ PHASE 2 — PLAN OF CARE ============
PY, PH = 714, 234
band(PY, PH, "PHASE 2  ·  PLAN OF CARE", "THE VISIT BUDGET IS VISIBLE AS IT IS WRITTEN", slots=5)
pb = PY + 62
row(pb, [
 (C["clin"], ["Each discipline plots", "its own frequency"],
  ["Written to clinical need", "Payer budget now on screen", "Fewer abrupt discharges"], "V2 · READ", 1),
 (C["hchb"], ["The 485 moment"],
  ["QA, lock, submission, orders", "All alongside one another"], "V2 · READ", 1),
 (C["pcc"], ["Assignment", "in one pass"],
  ["One task per discipline", "Assigns every visit it generates"], "V2 · ASSIST", 1),
 (C["hchb"], ["Role match defaults to", "the paraprofessional"],
  ["Explicit opt-out, not opt-in", "DE-08 — frees starts capacity"], "V2 · ASSIST", 1),
 (C["auth"], ["Auth as a ceiling,", "made visible"],
  ["Pending visits become visible", "They count, and they plan"], "V2 · READ", 1),
])

# ============ PHASE 3 — THE CLINICIAN'S WEEK ============
WY, WH = 978, 234
band(WY, WH, "PHASE 3  ·  THE CLINICIAN'S WEEK",
     "THE TOOL RECOMMENDS  ·  THE HUMAN ACCEPTS  ·  DE-09", slots=5)
wb = WY + 62
row(wb, [
 (C["clin"], ["Clinician sees their", "own capacity and week"],
  ["Availability entered by them", "Their own results, visible"], "V2 · READ", 1),
 (C["hchb"], ["A recommended week", "is offered"],
  ["Clinical need, geography", "Drive time, not distance", "They adjust and accept"], "V2 · ASSIST", 1),
 (C["hchb"], ["Confirmation runs", "without the clinician"],
  ["Replaces the unpaid evening", "Arrival range, never a time", "Consent rules per region"], "V3 · CONTROL", 1),
 (C["clin"], ["The five dispositions", "the day before"],
  ["Accept is the confirmed path", "Reassign carries a plan"], "V2 · ASSIST", 1),
 (C["float_"], ["Coverage found and", "offered directly"],
  ["Triaged by clinical priority", "Reached, not begged", "Clinical sign-off retained"], "V3 · ASSIST", 1),
])

# ============ PHASE 4 — RECERTIFY OR DISCHARGE ============
RY, RH = 1242, 220
band(RY, RH, "PHASE 4  ·  RECERTIFY OR DISCHARGE", "A NEW PERIOD IS A NEW AUTHORISATION QUESTION", slots=5)
rb = RY + 62
rc = row(rb, [
 (C["clin"], ["Recert window", "surfaced early"],
  ["Not discovered at day 52", "Next-period frequency"], "V2 · READ", 1),
 (C["auth"], ["New period", "re-enters auth"],
  ["A new budget, not a carry-on", "Cap and benefit, not just auth"], "V2 · ASSIST", 1),
 (C["clin"], ["Discipline-by-discipline", "discharge"],
  ["Staggered, not simultaneous", "Each ends in the right type"], "V2 · READ", 1),
])
OVX = IX + 3*SLOT + 30
oval(OVX + 132, rc, 130, 44, "#FFFFFF", ["Room returns", "to the envelope"], outline=INK)
arrow(IX + 2*SLOT + (SLOT-GAP) + 6, rc, OVX - 4, rc)
conn(f"M {OVX+262} {rc} L {RETX} {rc} L {RETX} {EY+EH/2} L {E_R+10} {EY+EH/2}", dash=True)
lbl(RETX-16, (PY+PH+WY)/2 + 4, "a discharge is capacity, not an ending", "end", "trg")

# ============ KEY + OPEN QUESTIONS ============
KY, KH = 1520, 250
panel(BX, KY, 920, KH, "HOW TO READ THE MARKERS")
lbl(BX+22, KY+58, "RELEASE", cls="colhb")
for i, (t, d) in enumerate([("MVP", "the capacity envelope, visualisation only"),
                            ("V2", "scheduling — allocation against it"),
                            ("V3", "engagement — patients, coverage, outreach")]):
    chip(BX+22, KY+72+i*50, 86, 36, [t], INK)
    lbl(BX+124, KY+95+i*50, d, cls="sub")
lbl(BX+490, KY+58, "POSTURE  ·  how far the system may go", cls="colhb")
for i, (t, d) in enumerate([("READ", "it shows; a person decides"),
                            ("ASSIST", "it proposes; a person confirms"),
                            ("CONTROL", "it decides and acts")]):
    chip(BX+490, KY+72+i*50, 112, 36, [t], INK)
    lbl(BX+616, KY+95+i*50, d, cls="sub")
lbl(BX+22, KY+236, "15 of the 19 MVP variables are SCORED control. In phase 1 every one ships at "
    "READ — the score is a ceiling, not a commitment.", cls="hi")

QX, QW = BX + 950, 2018 - (BX + 950)
panel(QX, KY, QW, KH, "OPEN  ·  NOT DRAWN, TO BE CLOSED BY THE OPERATOR")
for i, q in enumerate([
  "Where does the capacity tool live relative to Commure?",
  "Do we accept the risk of turning off DCS order approval?",
  "Is the capacity read a hard gate, or advice a leader may overrule?",
  "Who owns the capacity number day to day — a new role, or the DCS?",
  "Does automated confirmation replace the day-before call, or add to it?",
  "Point values and targets — undecided, and they block the MVP.",
]):
    lbl(QX+22, KY+62+i*29, "·  " + q, cls="sub")
lbl(QX+22, KY+236, "Six boxes deliberately not drawn. A wrong box on a wall sheet "
    "outlives the meeting.", cls="hi")

footer("TARGET STATE  ·  this sheet IS a proposal — the only sheet in the set that is  ·  "
       "every other sheet is current state",
       "Compassus Home Health  ·  Capacity & Scheduling  ·  Target State  ·  22 Aug 2026", w=W)

finish("flow.svg")
