# -*- coding: utf-8 -*-
"""One clinician's week — current state and target state.

Levers demonstrated: 2 Assessment Capacity Release, 3 Same-Day Schedule Recovery,
8 Clinician Retention, 9 Travel and Territory Efficiency.
"""
import sys

from scenario_kit import *  # noqa

MODE = sys.argv[1] if len(sys.argv) > 1 else "current"

TITLE = "One clinician's week"
DECK_C = ("A registered nurse who can admit, paid per visit. Monday to Friday, and what the week "
          "actually paid her.")
DECK_T = "The same nurse, the same caseload, and what changes around her."

LEVERS = [("L2", "Assessment Capacity Release"), ("L3", "Same-Day Schedule Recovery"),
          ("L8", "Clinician Retention"), ("L9", "Travel and Territory Efficiency")]

CUR = [
    ("1", "THE WEEK AS IT IS BUILT   ·   MONDAY", "ADMITTING TIME SPENT ON ROUTINE WORK",
     [(C["pcc"], ["Week assigned", "from the queue"],
       ["a points target for the week", "no view of who else could go", "assignment by availability"]),
      (C["clin"], ["She plots her own", "week around it"],
       ["no scheduler workflow at all", "grouped by distance on a map", "not by how long the drive takes"]),
      (C["clin"], ["Eleven routine visits", "stay on her list"],
       ["an assistant could take most", "nobody can see the assistant's week", "so they stay where they are"]),
      (C["clin"], ["Two admissions", "is all that fits"],
       ["she is one of two who can admit", "the branch turns one referral away", "on Wednesday"])],
     [], ("ADMITTING CAPACITY CONSUMED", "Routine work she did not need to",
          "carry crowds out two admissions.")),

    ("2", "A DAY INSIDE THAT WEEK   ·   TUESDAY", "THE DAY IS NEVER ANCHORED",
     [(C["clin"], ["First visit", "starts at 10am"],
       ["the patient preferred later", "nobody pushed back", "the whole day slides with it"]),
      (C["clin"], ["Crosses the territory", "twice"],
       ["visits grouped by distance", "not by drive time", "forty minutes she will not bill"]),
      (C["pat"], ["A patient is", "not ready"],
       ["fifteen minutes on the doorstep", "then a call to reschedule", "no replacement to offer"]),
      (C["clin"], ["Documentation", "after eight"],
       ["at home, unpaid", "plus tomorrow's confirmation calls", "about thirty minutes more"])],
     [], ("UNPAID TIME", "Roughly two hours she is not",
          "paid for, in a single day.")),

    ("3", "WHEN A VISIT FALLS THROUGH   ·   WEDNESDAY", "A GAP SHE CANNOT FILL HERSELF",
     [(C["pat"], ["Patient cancels", "the evening before"],
       ["rescheduled on the call", "that part already works", "the gap is the problem"]),
      (C["clin"], ["Two hours open", "in the middle"],
       ["two of her own patients are due", "neither is due today", "she has no view of anyone else's"]),
      (C["pcc"], ["The branch cannot", "fill it in time"],
       ["no view of who is approved", "no view of what could move", "by the time it is found, too late"])],
     [(3, "The gap goes unused",
       ["one visit fewer this week", "paid per visit, so unpaid", "the drive was already made"])],
     ("INCOME LOST, NOT COST SAVED", "She absorbs it. It never appears",
      "in a branch cost report.")),

    ("4", "WHAT THE WEEK PAID   ·   FRIDAY", "SHORT AGAIN, FOR THE FOURTH WEEK",
     [(C["hchb"], ["Points fall short", "of the target"],
       ["not through any fault of hers", "the work was not there to take", "or could not be reached"]),
      (C["clin"], ["Her pay lands below", "what she expected"],
       ["quoted a figure when hired", "has not reached it since", "no one has noticed"]),
      (C["lead"], ["Leadership sees", "a productivity number"],
       ["reported after the fact", "read as performance", "not as a signal she is struggling"])],
     [(3, "She starts looking",
       ["at six months in", "the branch finds out at exit", "replacement takes ninety days"])],
     ("A RESIGNATION IN PROGRESS", "Every signal existed. None of it",
      "reached anyone in time.")),
]

TGT = [
    ("1", "THE WEEK AS IT IS BUILT   ·   MONDAY", "ADMITTING TIME PROTECTED",
     [(C["pcc"], ["Week proposed", "with her caseload"],
       ["routine work offered to assistants", "only where they have room", "she reviews and adjusts"]),
      (C["clin"], ["She still plots", "her own week"],
       ["the tool recommends, she accepts", "nothing is assigned to her", "grouped by real drive time"]),
      (C["float_"], ["Seven routine visits", "move to an assistant"],
       ["who had the capacity", "and the right qualification", "visible for the first time"]),
      (C["clin"], ["Four admissions", "now fit"],
       ["two more than before", "the Wednesday referral is accepted", "no one was hired"])],
     [], ("ADMITTING CAPACITY RELEASED", "Two more admissions from the",
          "same nurse and the same week.")),

    ("2", "A DAY INSIDE THAT WEEK   ·   TUESDAY", "THE DAY IS ANCHORED AT NINE",
     [(C["hchb"], ["Confirmation handled", "the evening before"],
       ["not by her, and not unpaid", "a nine o'clock start negotiated", "the patient agreed to it"]),
      (C["clin"], ["First visit at nine", "anchors the day"],
       ["every visit after it holds", "no slide, no late finish", "the single largest lever she has"]),
      (C["clin"], ["Route follows", "drive time"],
       ["not distance on a map", "one crossing instead of two", "forty minutes back in the day"]),
      (C["clin"], ["Documentation", "inside the day"],
       ["the evening is her own", "no confirmation calls to make", "roughly two hours returned"])],
     [], ("TIME RETURNED", "About two hours a day, and the",
          "evening back.")),

    ("3", "WHEN A VISIT FALLS THROUGH   ·   WEDNESDAY", "THE GAP IS OFFERED BACK IN MINUTES",
     [(C["pat"], ["Patient cancels", "the evening before"],
       ["rescheduled on the call", "unchanged from today", "the gap is now visible"]),
      (C["hchb"], ["Options ranked", "immediately"],
       ["approval and discipline checked", "drive time from where she is", "flexible visits identified"]),
      (C["clin"], ["Three offers", "on her phone"],
       ["she chooses, or declines all", "accepted in eight minutes", "including one moved forward"])],
     [(3, "The gap is filled",
       ["the week stays whole", "the patient is seen sooner", "the later gap has days to fill"])],
     ("INCOME PROTECTED", "The week holds, and so does",
      "her paycheck.")),

    ("4", "WHAT THE WEEK PAID   ·   FRIDAY", "THE WEEK LANDS WHERE IT SHOULD",
     [(C["hchb"], ["Points land on", "target"],
       ["the work was there", "and it was reachable", "for the fourth week running"]),
      (C["clin"], ["Pay matches what", "she was quoted"],
       ["the number recruiting gave her", "is the number she earns", "at ninety days and at a year"]),
      (C["lead"], ["Leadership sees", "the trend, not the total"],
       ["a dip is visible in week one", "read as a signal, not a score", "a conversation, not a review"])],
     [(3, "She stays",
       ["the reason she leaves is removed", "not persuaded, just paid", "the caseload holds"])],
     ("A RESIGNATION AVOIDED", "The signals reached someone",
      "while it still mattered.")),
]

SUMMARY = [
    ("1  ADMITTING TIME",
     ["routine work she did not", "need to carry"],
     ["moved to assistants with room,", "two more admissions fit"]),
    ("2  THE SHAPE OF THE DAY",
     ["a ten o'clock start and", "two territory crossings"],
     ["anchored at nine, routed by", "drive time, evening returned"]),
    ("3  THE CANCELLED VISIT",
     ["a gap she could not fill,", "absorbed as lost income"],
     ["offered back in minutes,", "she still chooses"]),
    ("4  WHAT IT PAID",
     ["short again, and nobody", "saw it happening"],
     ["on target, and the trend is", "visible while it matters"]),
]

FOOT = "Compassus Home Health  ·  One clinician's week"
TRIG = ["Monday, 7am", "the week as assigned"]

if MODE == "both":
    both(TITLE, "The same nurse, the same caseload, and what changes around her.",
         CUR, TGT, SUMMARY, LEVERS, FOOT)
else:
    single(MODE, TITLE, DECK_C, DECK_T, CUR, TGT, SUMMARY, LEVERS, TRIG,
           "WHAT THE WEEK COST HER, AND US", "WHAT CHANGED", FOOT)

finish("flow.svg")
