# -*- coding: utf-8 -*-
"""One branch's week — current state and target state.

Levers demonstrated: 1 Admission Throughput, 2 Assessment Capacity Release,
6 Scheduling Administration Cost, 7 Premium Labor Avoidance.
"""
import sys

from scenario_kit import *  # noqa

MODE = sys.argv[1] if len(sys.argv) > 1 else "current"

TITLE = "One branch's week"
DECK_C = ("A branch running at capacity. The queue, the call-out, the referral it had to turn "
          "down, and what the week added up to.")
DECK_T = "The same branch, the same week, and what it is able to do instead."

LEVERS = [("L1", "Admission Throughput"), ("L2", "Assessment Capacity Release"),
          ("L6", "Scheduling Administration Cost"), ("L7", "Premium Labor Avoidance")]

CUR = [
    ("1", "THE QUEUE   ·   MONDAY MORNING", "MOST OF THE DAY IS NOT A DECISION",
     [(C["hchb"], ["The queue rebuilds", "overnight"],
       ["a task for every discipline", "and again at approval", "plus one per patient awaiting approval"]),
      (C["pcc"], ["The scheduler opens", "them one at a time"],
       ["most need no action at all", "but each must be opened to know", "the day is spent finding out"]),
      (C["pcc"], ["Bulk clearing", "becomes the habit"],
       ["a rational response to the volume", "the one that mattered goes with it", "nobody can tell which"]),
      (C["pcc"], ["Real decisions get", "the time that is left"],
       ["the welcome call is one of them", "it slips to the afternoon", "or to tomorrow"])],
     [], ("ADMINISTRATION, NOT SCHEDULING", "The judgment work is squeezed",
          "into what the queue leaves over.")),

    ("2", "THE CALL-OUT   ·   WEDNESDAY, 7AM", "THE MOST EXPENSIVE OPTION IS THE FASTEST",
     [(C["clin"], ["A clinician calls", "out at seven"],
       ["six visits on her day", "two are time-sensitive", "four could move if someone knew"]),
      (C["pcc"], ["Nobody can see", "who has room"],
       ["capacity lives in a spreadsheet", "updated when someone remembers", "and not this morning"]),
      (C["pcc"], ["The branch calls", "around"],
       ["per diem first, then contract", "then incentive pay for extra work", "whoever answers first"])],
     [(3, "Covered, at a premium",
       ["two visits covered this way", "two moved, two simply missed", "the cost lands in the month"])],
     ("PREMIUM SPEND, BOUGHT IN A HURRY", "Not because coverage was scarce.",
      "Because it could not be seen.")),

    ("3", "A REFERRAL ARRIVES   ·   THURSDAY", "TURNED DOWN WITH CAPACITY IN THE BUILDING",
     [(C["intake"], ["Referral offered", "by the hospital"],
       ["a good fit for the branch", "the kind we want", "an answer needed today"]),
      (C["pcc"], ["Both admitting nurses", "look full"],
       ["their weeks are full of routine visits", "an assistant could take many", "no view of the assistant's week"]),
      (C["lead"], ["The branch declines"],
       ["a defensible call on what is visible", "the wrong call on what is true", "the source notices"])],
     [(3, "Capacity existed",
       ["it was in the wrong hands", "and nobody could see it", "the referral goes elsewhere"])],
     ("AN ADMISSION LOST", "Declined for want of capacity",
      "the branch actually had.")),

    ("4", "THE WEEK IN REVIEW   ·   FRIDAY", "NONE OF THIS APPEARS AS A NUMBER",
     [(C["lead"], ["The branch reviews", "the week"],
       ["visits delivered, points, census", "all of it accurate", "none of it showing what was lost"]),
      (C["hchb"], ["Premium spend", "posts to the month"],
       ["without the reason attached", "read as a staffing problem", "not a visibility problem"]),
      (C["lead"], ["The declined referral", "is not recorded"],
       ["no reason code exists for it", "so it never happened", "and cannot be counted"])],
     [(3, "The week looks fine",
       ["every number is defensible", "the losses are all invisible", "so nothing changes next week"])],
     ("INVISIBLE, THEREFORE PERMANENT", "What cannot be counted cannot",
      "be managed, or improved.")),
]

TGT = [
    ("1", "THE QUEUE   ·   MONDAY MORNING", "THE QUEUE ONLY CARRIES DECISIONS",
     [(C["hchb"], ["Notifications fire", "on change only"],
       ["not on the same state each day", "the volume falls away", "what remains needs an answer"]),
      (C["pcc"], ["The scheduler works", "exceptions"],
       ["urgency, coverage, local knowledge", "the work only a person can do", "fewer people, better used"]),
      (C["pcc"], ["Welcome calls go", "out first thing"],
       ["standardised, and early", "before the day fills", "readiness known while it is useful"]),
      (C["pcc"], ["Care team assigned", "once, at referral"],
       ["not once per discipline", "the task burst never forms", "approval is a single step"])],
     [], ("SCHEDULING, NOT ADMINISTRATION", "The queue holds decisions, and",
          "the day holds judgment work.")),

    ("2", "THE CALL-OUT   ·   WEDNESDAY, 7AM", "COVERAGE IS FOUND BEFORE IT IS BOUGHT",
     [(C["clin"], ["A clinician calls", "out at seven"],
       ["the same six visits", "the same two time-sensitive", "nothing about this changes"]),
      (C["hchb"], ["The branch can see", "who has room"],
       ["live, across the whole branch", "approval and discipline checked", "including flexible visits"]),
      (C["pcc"], ["Two covered from", "existing capacity"],
       ["clinicians already on the payroll", "who had room and were near", "offered, and they accepted"])],
     [(3, "Premium used once, not four times",
       ["for the visit that genuinely", "had no other option", "the rest cost nothing extra"])],
     ("PREMIUM SPEND, PLANNED", "Bought where it was needed,",
      "not where it was quickest.")),

    ("3", "A REFERRAL ARRIVES   ·   THURSDAY", "ACCEPTED, USING THE SAME PEOPLE",
     [(C["intake"], ["Referral offered", "by the hospital"],
       ["the same referral", "the same day", "the same people available"]),
      (C["hchb"], ["Admitting capacity", "shown honestly"],
       ["routine work that could move", "assistants with room to take it", "the true number, not the visible one"]),
      (C["pcc"], ["Routine visits", "shift to assistants"],
       ["only where they have capacity", "and the right qualification", "the nurse reviews and accepts"])],
     [(3, "The referral is accepted",
       ["an admission the branch would", "otherwise have declined", "no one was hired"])],
     ("AN ADMISSION GAINED", "The capacity was always there.",
      "Now it can be seen and used.")),

    ("4", "THE WEEK IN REVIEW   ·   FRIDAY", "THE LOSSES BECOME NUMBERS",
     [(C["lead"], ["The branch reviews", "the week"],
       ["the same accurate figures", "plus the ones that were missing", "capacity offered against filled"]),
      (C["hchb"], ["Premium spend shows", "its reason"],
       ["reactive or planned, per event", "a visibility problem is visible", "and therefore fixable"]),
      (C["lead"], ["Declines are recorded", "with a reason"],
       ["capacity, clinical, or geography", "counted, and trended", "the argument for hiring gets evidence"])],
     [(3, "The week can be improved",
       ["because it can be measured", "the same week, next week,", "is a decision, not a hope"])],
     ("MEASURED, THEREFORE MANAGEABLE", "The first week the branch could",
      "see what it lost.")),
]

SUMMARY = [
    ("1  THE QUEUE",
     ["a day spent opening items", "that needed no action"],
     ["a queue that only carries", "things needing a decision"]),
    ("2  THE CALL-OUT",
     ["premium bought four times", "because nothing was visible"],
     ["premium bought once, where", "it was genuinely needed"]),
    ("3  THE REFERRAL",
     ["declined for want of capacity", "the branch actually had"],
     ["accepted, by moving routine", "work to assistants with room"]),
    ("4  THE REVIEW",
     ["every loss invisible, so", "nothing changes next week"],
     ["losses counted, so the week", "can actually be improved"]),
]

FOOT = "Compassus Home Health  ·  One branch's week"
TRIG = ["Monday, 7am", "the queue as it stands"]

if MODE == "both":
    both(TITLE, "The same branch, the same week, and what it is able to do instead.",
         CUR, TGT, SUMMARY, LEVERS, FOOT)
else:
    single(MODE, TITLE, DECK_C, DECK_T, CUR, TGT, SUMMARY, LEVERS, TRIG,
           "WHAT THE WEEK COST THE BRANCH", "WHAT CHANGED", FOOT)

finish("flow.svg")
