# -*- coding: utf-8 -*-
"""The weekend cascade — current state and target state.

How Saturday and Sunday admission performance sets, or costs, the following week.
Lever demonstrated: 1 Admission Throughput, in depth.
"""
import sys

from scenario_kit import *  # noqa

MODE = sys.argv[1] if len(sys.argv) > 1 else "current"

TITLE = "The weekend cascade"
DECK_C = ("Three weekend starts committed on Friday, and what each one did to the week that "
          "followed.")
DECK_T = "The same three referrals, the same patient decisions, and a different Monday."

LEVERS = [("L1", "Admission Throughput, in depth")]

CUR = [
    ("1", "FRIDAY   ·   THREE WEEKEND STARTS COMMITTED", "THE WEEKEND IS PLANNED ON FRIDAY AFTERNOON",
     [(C["intake"], ["Three referrals", "accepted"],
       ["two discharging Saturday", "one discharging Sunday", "all three agreed with sales"]),
      (C["pcc"], ["Weekend cover", "arranged"],
       ["one nurse Saturday, one Sunday", "each holding two admitting slots", "the week ahead is planned on it"]),
      (C["lead"], ["The week's admission", "target assumes them"],
       ["three starts before Monday", "and the caseload they carry", "Monday is planned as a full day"])],
     [(3, "Nothing is confirmed yet",
       ["no contact until the weekend", "sales confirmation is not consent", "the risk is invisible on Friday"])],
     ("THE WEEK IS BUILT ON THREE", "Three assumptions nobody will",
      "test until the weekend arrives.")),

    ("2", "SATURDAY", "ONE OF TWO STARTS",
     [(C["pcc"], ["Welcome calls made", "late morning"],
       ["after the day's other work", "by which time the day is set", "no slack left to redirect"]),
      (C["pat"], ["First patient", "discharged late"],
       ["still in the hospital at eleven", "the visit cannot happen", "reschedule to Monday"]),
      (C["clin"], ["One admitting slot", "expires"],
       ["the nurse is on shift regardless", "nothing else to fill it with", "the branch pays for the day"])],
     [(3, "One start delivered",
       ["the second patient was ready", "that admission goes well", "one of two"])],
     ("HALF A WEEKEND DAY LOST", "The nurse worked. One admission",
      "came out of it.")),

    ("3", "SUNDAY", "THE DAY THAT MOST OFTEN GOES WRONG",
     [(C["pcc"], ["Welcome call made", "at midday"],
       ["Sunday cover is thin", "the call waits its turn", "the family has been home a day"]),
      (C["pat"], ["The family defers", "to Monday"],
       ["a common Sunday pattern", "they want to settle first", "entirely reasonable, and unpredicted"]),
      (C["clin"], ["Both Sunday slots", "expire"],
       ["nothing to redirect them to", "no view of who else could start", "the nurse goes home early"])],
     [(3, "No starts on Sunday",
       ["the most common weekend outcome", "and the least examined", "three admissions now land Monday"])],
     ("A SUNDAY THAT SET THE WEEK BACK", "Two deferrals and a late discharge",
      "all arrive on Monday together.")),

    ("4", "MONDAY, AND THE WEEK THAT FOLLOWS", "THE CASCADE",
     [(C["pcc"], ["Three admissions", "land on Monday"],
       ["planned for two at most", "both admitting nurses consumed", "for most of the day"]),
      (C["clin"], ["Routine visits", "get pushed"],
       ["to Tuesday and Wednesday", "compressing the whole week", "some slip past their window"]),
      (C["lead"], ["Thursday's referral", "is declined"],
       ["the branch is genuinely full", "because Monday absorbed the weekend", "the source is told no"])],
     [(3, "The target is missed",
       ["not from a lack of demand", "from three weekend assumptions", "that nobody tested in time"])],
     ("ONE WEEKEND, ONE WHOLE WEEK", "The weekend did not just lose two",
      "days. It cost the week.")),
]

TGT = [
    ("1", "FRIDAY   ·   THREE WEEKEND STARTS COMMITTED", "THE SAME THREE, WITH THE RISK NAMED",
     [(C["intake"], ["Three referrals", "accepted"],
       ["the same three referrals", "the same expected discharges", "nothing about Friday changes"]),
      (C["hchb"], ["Each start carries", "a readiness state"],
       ["confirmed, expected, or at risk", "based on discharge patterns", "and on what sales recorded"]),
      (C["pcc"], ["Weekend cover", "arranged the same"],
       ["one nurse Saturday, one Sunday", "but the slots are now provisional", "and a waiting list sits behind them"])],
     [(3, "A second call is queued behind each",
       ["patients who could start early", "if a slot came free", "nobody had to build that list by hand"])],
     ("THE WEEK IS BUILT ON THREE,", "with something ready to take",
      "the place of any that fall.")),

    ("2", "SATURDAY", "TWO STARTS, FROM THE SAME TWO SLOTS",
     [(C["hchb"], ["Readiness checked", "at seven"],
       ["automated, before the day starts", "the late discharge is already known", "no one had to chase it"]),
      (C["pat"], ["First patient", "discharged late"],
       ["exactly as before", "the patient's situation is unchanged", "only our knowledge of it changed"]),
      (C["pcc"], ["The slot is offered", "on by eight"],
       ["to the waiting patient behind it", "who accepts for that morning", "the nurse's day stays full"])],
     [(3, "Two starts delivered",
       ["one planned, one recovered", "from a slot that would have expired", "the same nurse, the same shift"])],
     ("A FULL SATURDAY", "The late discharge cost nothing",
      "except a different patient's order.")),

    ("3", "SUNDAY", "THE DEFERRAL STILL HAPPENS. THE DAY DOES NOT.",
     [(C["pcc"], ["Welcome call made", "at eight"],
       ["standardised, and early", "not waiting on office capacity", "four hours earlier than before"]),
      (C["pat"], ["The family still", "defers to Monday"],
       ["the same reasonable decision", "no system changes that", "but we know at eight, not at noon"]),
      (C["pcc"], ["Both slots reassigned", "by ten"],
       ["to patients ready today", "with the whole day still ahead", "the nurse works a full Sunday"])],
     [(3, "Two starts on Sunday",
       ["not the ones planned on Friday", "the slots were used, which is", "what the week actually needed"])],
     ("A SUNDAY THAT HELD", "The deferral was never the problem.",
      "Finding out too late was.")),

    ("4", "MONDAY, AND THE WEEK THAT FOLLOWS", "NO CASCADE",
     [(C["pcc"], ["One admission", "lands on Monday"],
       ["the deferred patient, as agreed", "four already started", "Monday was planned for two"]),
      (C["clin"], ["Routine visits", "run as planned"],
       ["nothing pushed into Tuesday", "nothing compressed", "no window put at risk"]),
      (C["lead"], ["Thursday's referral", "is accepted"],
       ["the branch has genuine room", "because the weekend did its work", "the source is told yes"])],
     [(3, "The target is met",
       ["from the same demand", "and the same people", "with four weekend starts, not one"])],
     ("ONE WEEKEND, ONE WHOLE WEEK", "The weekend set the week up",
      "instead of setting it back.")),
]

SUMMARY = [
    ("1  FRIDAY",
     ["three assumptions, none of", "them tested until the weekend"],
     ["the same three, each carrying", "a readiness state and a backup"]),
    ("2  SATURDAY",
     ["a late discharge takes a slot", "with nothing to replace it"],
     ["the slot is offered on by eight,", "the day stays full"]),
    ("3  SUNDAY",
     ["a midday call, a deferral,", "and two slots gone"],
     ["an eight o'clock call, the same", "deferral, both slots reused"]),
    ("4  THE WEEK",
     ["three admissions land Monday,", "the week compresses, a referral declined"],
     ["one lands Monday, the week runs", "as planned, the referral accepted"]),
]

FOOT = "Compassus Home Health  ·  The weekend cascade"
TRIG = ["Friday, 4pm", "three weekend starts"]

if MODE == "both":
    both(TITLE, "The same three referrals, the same patient decisions, and a different Monday.",
         CUR, TGT, SUMMARY, LEVERS, FOOT)
else:
    single(MODE, TITLE, DECK_C, DECK_T, CUR, TGT, SUMMARY, LEVERS, TRIG,
           "WHAT THE WEEKEND COST THE WEEK", "WHAT THE WEEKEND GAVE THE WEEK", FOOT)

finish("flow.svg")
