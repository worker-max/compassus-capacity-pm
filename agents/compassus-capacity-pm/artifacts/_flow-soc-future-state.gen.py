# -*- coding: utf-8 -*-
"""Future-state SOC/ROC admission flow. Canvas units = points on the sheet.

Deliberately breaks two house non-negotiables, because it has to: every other sheet in
the set is current state and says nothing on it is a proposal. This one is entirely a
proposal, so the eyebrow, the accent rule and the footer all say so -- a future-state
sheet that looks like a current-state sheet is a wall-level hazard.

Every box traces to a row of Capacity-Scheduling-Variable-Workbook.xlsx: the arena, the
future-state posture (Automate / Assist / Surface / Stays manual) and the decision owner
are read off that sheet, not invented here.
"""
import sys
sys.path.insert(0, "/home/user/compassus-capacity-pm/.claude/skills/process-flow-map/assets")
from flowkit import *   # noqa
import flowkit as fk

PLAT = "#A63A79"        # the capacity & scheduling platform -- a new actor
C["plat"] = PLAT

W, H = 2600, 1830
begin(W, H,
      "Future-state start-of-care flow. The capacity answer moves to the front: the platform reads "
      "the referral on arrival, tests it against admission capacity by discipline, and the branch "
      "director accepts or declines with a captured reason. Authorization keeps its human verification "
      "but the payer's rules are surfaced into the plan of care and pending-auth visits become visible "
      "in the capacity picture. Readiness outreach runs as an agentic voice call, because consent for "
      "text and email is not signed until the start-of-care visit; power-of-attorney status is surfaced "
      "before booking; the scheduler keeps the judgment the call raises. Assignment is proposed by the "
      "platform and confirmed by a person, always. The plan-of-care pass is largely unchanged -- the "
      "change is upstream. Constraints captured at the start of care are handed to the weekly build "
      "and the day-before confirmation round, because they drift.")

# ---------------- masthead ----------------
masthead("COMPASSUS HOME HEALTH  ·  FUTURE STATE  ·  FLOW 1",
         "Start of Care — Future State",
         "What the platform takes over, what it proposes, and what stays a human call — referral to visits on the calendar")
add(f'<rect x="50" y="152" width="{W-100}" height="5" rx="2.5" fill="{PLAT}"/>')
legend([("Intake", C["intake"]), ("Insurance & Auth", C["auth"]), ("DCS", C["dcs"]),
        ("PCC / Scheduler", C["pcc"]), ("Clinician", C["clin"]),
        ("Branch Leadership", C["lead"]), ("The platform", PLAT)],
       x=1330, cy=58, per_row=4, gap=30)
lbl(W-50, 132, "BADGE = HOW FAR THE SOFTWARE GOES   ·   automated   ·   proposes, you confirm   ·   "
                "surfaces, you decide   ·   stays human", "end", "key")

PH, SUBY = 250, 178

# ================= BAND 1 =================
B1 = 190
band(B1, PH, "1  ·  REFERRAL  →  CAN WE TAKE IT?", "THE CAPACITY ANSWER MOVES TO THE FRONT", slots=7)
c1 = row(B1+62, [
    (C["intake"], ["Intake receives", "the referral"],
     ["unchanged"], "STAYS HUMAN", 1),
    (PLAT, ["Referral read", "on arrival"],
     ["payer, zip, disciplines ordered", "expected start-of-care date",
      "a verified number for the right person"], "AUTOMATED", 2),
    (PLAT, ["Admission capacity", "tested against it"],
     ["start-of-care-capable clinicians, by discipline",
      "open room this week, by territory",
      "including visits held in pending auth"], "AUTOMATED", 2),
    (C["lead"], ["Branch director accepts", "or declines — with a reason"],
     ["capacity, clinical or geography — captured, not lost",
      "the reason is what makes next quarter's territory review real"],
     "SURFACES · DECIDE", 2),
])
chip(50, c1-38, 250, 76, ["Referral arrives", "in Commure"], INK)
arrow(300, c1, IX-6, c1)
lbl(50, c1-52, "TRIGGER", cls="trg")
lbl(IX, B1+PH-16, "Today nobody can see admission capacity — acceptance runs on a proxy and the decline reason is not kept.", cls="hi")

# ================= BAND 2 =================
B2 = B1 + PH + 34
band(B2, PH, "2  ·  AUTHORIZATION — THE RULES, BEFORE THEY BITE",
     "THE PAYER'S RULES ALREADY EXIST IN WRITING", slots=7)
c2 = row(B2+62, [
    (C["auth"], ["Auth team verifies", "eligibility, keys", "pending auth"],
     ["unchanged — judgment against payer policy",
      "the allowance is the payer's, not clinical"], "STAYS HUMAN", 2),
    (C["intake"], ["Intake final", "approval"], ["unchanged"], None, 1),
    (PLAT, ["Payer rules surfaced", "into the plan of care"],
     ["the coordination note read at plan-of-care creation, not days after",
      "the pending-auth allowance shown as a ceiling while frequency is plotted",
      "every add-on, recert and resumption re-enters the same loop"],
     "PROPOSES · CONFIRM", 2),
    (PLAT, ["Held visits appear", "in the capacity picture"],
     ["on a calendar, counted, forecastable",
      "the ~50-a-day queue triaged, not bulk-cleared"], "AUTOMATED", 2),
])
lbl(IX, B2+PH-16, "Today a held visit sits on no calendar and counts toward nothing. If you cannot see it, you cannot plan it.", cls="hi")

# ================= BAND 3 =================
B3 = B2 + PH + 34
band(B3, PH, "3  ·  READINESS — AND WHY IT HAS TO BE A VOICE CALL",
     "CONSENT IS SIGNED AT THE SOC VISIT — NOTHING TEXTED CAN PRECEDE IT", slots=7)
c3 = row(B3+62, [
    (PLAT, ["Readiness outreach", "— agentic voice"],
     ["reaches the verified contact, not the chart's oldest number",
      "is the patient home — not still inpatient, not deferring",
      "text and email are unavailable until consent is signed"], "AUTOMATED", 3),
    (PLAT, ["Signing authority", "surfaced before booking"],
     ["who may sign the consent", "who may be contacted at all"],
     "SURFACES · DECIDE", 2),
    (C["pcc"], ["Scheduler owns what", "the call turns up"],
     ["deferring admission, family not ready, not home",
      "the exception now — not every referral"], "STAYS HUMAN", 2),
])
lbl(IX, B3+PH-16, "This is the scheduler's one true judgment call today, and they make it on every single referral.", cls="hi")

# ================= BAND 4 =================
B4 = B3 + PH + 34
band(B4, PH, "4  ·  ASSIGNMENT — PROPOSED, THEN CONFIRMED",
     "HUMAN CONFIRM IS THE LAST STEP, ALWAYS", slots=7)
c4 = row(B4+62, [
    (PLAT, ["Platform proposes", "clinician and slot"],
     ["discipline and role, competency, acuity to skill",
      "reachability by drive time, not distance",
      "continuity, and the compliance window it has to land in"],
     "PROPOSES · CONFIRM", 3),
    (C["pcc"], ["Scheduler confirms", "or overrides"],
     ["the override reason is captured",
      "it is the best training signal in the process"], "STAYS HUMAN", 2),
    (C["clin"], ["SOC / ROC and the", "discipline evals performed"],
     ["RN at the start of care", "PT, OT, ST at their own evals, 1–2 days later"], None, 2),
])
lbl(IX, B4+PH-16, "Clinicians already do this by hand when they recommend who should take a visit they cannot. That is the model, unpaid.", cls="hi")

# ================= BAND 5 =================
B5 = B4 + PH + 34
SLIM = 178
band(B5, SLIM, "5  ·  PLAN OF CARE  →  VISITS ON THE CALENDAR",
     "LARGELY UNCHANGED — THE CHANGE IS UPSTREAM", slots=7)
c5 = row(B5+62, [
    (C["clin"], ["Clinician plots", "frequency"], None, "× N disciplines", 2),
    (C["dcs"], ["DCS reviews", "and approves"], None, None, 1),
    (PLAT, ["Queue age visible to", "the people it blocks"], None, "SURFACES", 2),
    (PLAT, ["Visits generate ·", "auth checked per visit"], None, "AUTOMATED", 2),
])

# ================= handoff panel =================
PY, PHH = B5 + SLIM + 40, 172
panel(BX, PY, 7*SLOT+30, PHH, "WHAT THE START OF CARE HANDS TO THE WEEK — captured here, but none of it stays true on its own")
hx = BX + 26
for txt, col in [("Caregiver must be present", C["pat"]), ("Caregiver's own schedule", C["pat"]),
                 ("Competing appointments", C["pat"]), ("Times the patient refuses", C["pat"]),
                 ("How they want to be reached", C["pat"])]:
    w = 8.6*len(txt) + 40
    chip(hx, PY+56, w, 46, [txt], col)
    hx += w + 16
lbl(BX+26, PY+134, "Each of these is real at admission and quietly stops being real — the caregiver who has to open the door until mobility improves, the", cls="note")
lbl(BX+26, PY+154, "appointment booked in week four. They are re-established in the weekly build and the day-before round, not captured once and trusted.", cls="note")
path(f"M {BX+7*SLOT+30} {PY+PHH/2} L {BX+7*SLOT+120} {PY+PHH/2}", label="FLOW 2", lx=BX+7*SLOT+128, ly=PY+PHH/2+5, anchor="start")

footer("FUTURE STATE — every box on this sheet is a proposal. Current practice is Flow 1. "
       "Postures and owners are read from the variable workbook, not invented here.",
       "Future State · Flow 1 · SOC / ROC")
finish("flow-soc-future-state.svg")
