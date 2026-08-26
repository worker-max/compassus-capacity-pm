# -*- coding: utf-8 -*-
"""Payer economics — where the payer changes what the schedule may do.
Current state. Canvas units = points on the output sheet."""
import pathlib
import sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3]
                       / ".claude" / "skills" / "process-flow-map" / "assets"))
from flowkit import *  # noqa

W, H = 2600, 1970

begin(W, H, aria=(
    "Payer economics mapped against the schedule, current state. Five bands. Referral to "
    "schedulable: every payer but traditional Medicare routes through the authorisation team, "
    "which keys a pending-auth visit count set by the payer. Plan of care: each discipline plots "
    "its own frequency to clinical need while the payer rule sits unread in a coordination note "
    "written days earlier. Delivery: the same delivered visit carries five different values "
    "depending on payer class and period state. The miss: one missed visit means about 25 dollars "
    "mid-period or up to 1,386 dollars if it drops the period below its floor. Period end: a new "
    "certification period is a new authorisation question and a new case-mix group."))

masthead("COMPASSUS HOME HEALTH  ·  PAYER ECONOMICS",
         "What the payer does to the schedule",
         "The same operational event carries a different consequence in every payer class")

legend([("Intake", C["intake"]), ("Insurance & Auth", C["auth"]),
        ("PCC / Scheduler", C["pcc"]), ("Clinician", C["clin"]),
        ("DCS", C["dcs"]), ("HCHB", C["hchb"])], x=1480, per_row=4)

# ---------------------------------------------------------------- band 1
B1 = 190
band(B1, 258, "1  ·  REFERRAL TO SCHEDULABLE", "THE GATE IS PAYER-DEPENDENT", slots=5)
lbl(36, 232, "TRIGGER", cls="trg")
chip(36, 248, 264, 90, ["Referral accepted", "the clock starts"], INK)
arrow(306, 293, 344, 293)
row(B1 + 58, [
    (C["intake"], ["Referral received", "in Commure"], None, None, 1),
    (C["auth"], ["Eligibility verified,", "pending auth keyed"],
     ["allowance set by payer:", "1, 3, 5 or 10 visits", "traditional Medicare skips this"],
     "NON-MEDICARE", 1),
    (C["intake"], ["Final approval"],
     ["returns to intake", "only now is it schedulable"], None, 1),
    (C["pcc"], ["Welcome / intake call"],
     ["is the patient actually home", "the one true judgment call"], None, 1),
    (C["pcc"], ["SOC and evals booked"],
     ["seen within 48 hours", "RN at SOC, therapy 1-2 days"], None, 1),
])
sublist(350, B1 + 174, ["payer class identified here", "discharge date captured",
                        "benefit window may already run"])

# ---------------------------------------------------------------- band 2
B2 = 472
band(B2, 258, "2  ·  PLAN OF CARE", "PAYER LIMITS ARE INVISIBLE HERE", slots=4)
tag(36, 530, 264, 96, ["Payer rule already exists", "in a coordination note,", "written days earlier"])
arrow(306, 575, 344, 575, dash=True)
row(B2 + 58, [
    (C["clin"], ["Each discipline plots", "its own frequency"],
     ["written to clinical need", "the payer ceiling is not here",
      "RN also plots aide and MSW"], "x 4 DISCIPLINES", 1),
    (C["hchb"], ["Workflow fires", "per discipline"],
     ["once at submission,", "once again at approval"], None, 1),
    (C["dcs"], ["QA, POC lock, 485,", "orders to the MD"],
     ["a moment, not four gates"], "ALL AT ONCE", 1),
    (C["pcc"], ["One assignment pass"],
     ["one task per discipline", "assigns all visits at once"], None, 1),
])

# ---------------------------------------------------------------- band 3
B3 = 754
band(B3, 176, "3  ·  WHAT A DELIVERED VISIT IS WORTH", "SAME VISIT, FIVE DIFFERENT VALUES", slots=7)
row(B3 + 58, [(C["clin"], ["Visit delivered", "and documented"], None, None, 1)])
lbl(36, B3 + 74, "White outline =", cls="note")
lbl(36, B3 + 96, "a payment state,", cls="note")
lbl(36, B3 + 118, "not an actor", cls="note")
cx = 646
for lines in [["EPISODIC  ·  BELOW THE FLOOR", "the visit that saves the period", "worth 1,363 dollars"],
              ["EPISODIC  ·  ABOVE THE FLOOR", "no further revenue", "0 dollars, to ~15.8 visits"],
              ["PER-VISIT  ·  AUTHORISED", "worth the contracted rate"],
              ["PER-VISIT  ·  NOT AUTHORISED", "non-billable, whoever needed it"],
              ["CAPPED  ·  BENEFIT EXHAUSTED", "non-billable, care stops"]]:
    chip(cx, B3 + 57, 300, 92, lines, INK)
    cx += 322

# ---------------------------------------------------------------- band 4
B4 = 954
band(B4, 340, "4  ·  THE MISSED VISIT", "ONE EVENT, FOUR MEANINGS", slots=6)
row(B4 + 58, [
    (C["clin"], ["Disposition selected", "the day before"],
     ["accept is the confirmed path", "reschedule is most likely",
      "reassign carries a plan"], "IN HCHB", 1),
    (C["clin"], ["Missed visit", "documented"],
     ["scheduled, then pending,", "then missed"], None, 1),
    (C["pcc"], ["Notify the MD", "within 48 hours"],
     ["an HCHB hard stop", "late generates a DCS task"], "MEDICARE", 1),
])
cx = 350
for lines in [["EPISODIC  ·  MID-PERIOD", "about 25 dollars"],
              ["EPISODIC  ·  FLOOR-CRITICAL", "1,258 to 1,386 dollars"],
              ["PER-VISIT", "the visit's contracted rate"],
              ["MANAGED  ·  ALSO", "risks the completion gate"]]:
    chip(cx, B4 + 242, 380, 80, lines, INK)
    cx += 408

# ---------------------------------------------------------------- band 5
B5 = 1318
band(B5, 230, "5  ·  PERIOD AND WINDOW END", "A NEW PERIOD IS A NEW QUESTION", slots=5)
row(B5 + 58, [
    (C["clin"], ["Each discipline", "decides separately"],
     ["recert or discharge,", "against its own goals"], None, 1),
    (C["hchb"], ["New certification", "period generates"],
     ["recert visits already plotted"], None, 1),
    (C["auth"], ["New auth question"],
     ["every recert, ROC, physician order", "new window, new allowance"], "GATE", 1),
])
chip(1184, B5 + 57, 300, 92,
     ["NEW 30-DAY PERIOD", "new case-mix group,", "new floor threshold"], INK)

# ---------------------------------------------------------------- panels
P = 1572
panel(320, P, 1400, 280, "THE FOUR CEILINGS ON ONE EPISODE  —  INDEPENDENT TESTS, NOT ONE RULE")
cols = [(350, "PERMISSION", ["what the payer allows", "unauthorised is non-billable",
                             "backdating window 0-5 days"]),
        (690, "FLOOR", ["LUPA, 2 to 5 visits by group", "below it the period reprices",
                        "a cliff, not a slope"]),
        (1030, "CEILING", ["visits above the floor", "earn nothing to ~15.8 visits",
                           "no one sees this today"]),
        (1370, "CAP", ["the annual benefit limit", "commercial and Medicaid",
                       "the employer may set it"])]
for x, head, items in cols:
    column_rule(x - 14, P + 60, P + 76)
    lbl(x - 14, P + 96, head, cls="colh")
    sublist(x - 20, P + 128, items)

panel(1750, P, 800, 280, "WHERE IT BREAKS")
sublist(1776, P + 76, [
    "The payer rule is written days before the plan of care",
    "and never surfaces at it",
    "Pending-auth visits sit on no calendar, count toward nothing",
    "Period state is invisible, so every miss is priced the same",
    "About 50 pending-auth notices a day train bulk-clearing",
    "A rebooked visit spends two slots to deliver one",
])

footer("Current state, August 2026.  Nothing on this sheet is a proposal.",
       "Compassus Home Health  ·  Payer economics and the schedule")
print("last content y =", P + 280)
import sys
finish(sys.argv[1] if len(sys.argv) > 1 else "payer-economics.svg")
