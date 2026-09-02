# -*- coding: utf-8 -*-
"""One referral, one episode.

Three sheets from one source so the comparison is exact:
  python gen_episode.py current   ->  current state
  python gen_episode.py target    ->  target state, eighteen months on
  python gen_episode.py both      ->  both side by side on one wide sheet

Canvas units = points on the output sheet.
"""
import sys

sys.path.insert(0, r"C:\Users\chigh\compassus-capacity-pm\.claude\skills\process-flow-map\assets")
from flowkit import *  # noqa

MODE = sys.argv[1] if len(sys.argv) > 1 else "current"
LOSS, SAVE = "#B03A2E", "#1E7A46"
BH_ = 290

# ════════════════════════════════════════════════════════════════ content
# band = (number, phase, claim, steps, terminals, outcome)
#   step     = (colour, [lines], [subs])
#   terminal = (slot index, label, [subs])  -> white outcome oval
CUR_BANDS = [
    ("1", "THE REFERRAL   ·   FRIDAY TO SUNDAY", "TWO ADMITTING SLOTS EXPIRE UNUSED",
     [(C["intake"], ["Referral accepted", "in Commure"],
       ["discharge expected Saturday", "RN holds a Saturday slot", "sales confirmed patient agreed"]),
      (C["pcc"], ["Saturday", "no contact made"],
       ["welcome call sits in a queue", "office staff work through it", "discharge has already slipped"]),
      (C["pcc"], ["Sunday, 11am", "welcome call"],
       ["discharged late Saturday", "daughter asks to start Monday", "nothing was wrong with the plan"]),
      (C["clin"], ["Two held slots", "expire"],
       ["Saturday and Sunday", "admitting time, unrecoverable", "the week starts a day behind"])],
     [], ("CAPACITY LOST", "Two admitting slots, unused.", "Monday now carries the admission.")),

    ("2", "ADMISSION AND THE PLAN OF CARE   ·   MONDAY", "THE VISIT BUDGET IS NOT IN THE ROOM",
     [(C["clin"], ["Start of care", "delivered Monday"],
       ["three days after referral", "the clock started Friday", "inside the required window"]),
      (C["clin"], ["Frequency written", "to clinical need"],
       ["payer allowance not visible", "visit floor not visible", "both were known days earlier"]),
      (C["dcs"], ["QA, plan lock,", "orders to the MD"],
       ["a moment, not four gates"]),
      (C["hchb"], ["Assignment tasks", "generate"],
       ["one per discipline", "again at approval", "for a decision already made"])],
     [], ("EXPOSURE CREATED", "Frequency set without the payer", "budget or the visit floor in view.")),

    ("3", "THE WEEKS THAT FOLLOW", "A GAP NOBODY CAN FILL IN TIME",
     [(C["pat"], ["Patient cancels", "Tuesday's visit"],
       ["called Monday evening", "rebooked on the call", "that part already works"]),
      (C["clin"], ["A two-hour gap", "opens in the day"],
       ["10am to 12pm Tuesday", "two other patients are nearby", "neither is visible to the branch"]),
      (C["pcc"], ["No replacement", "found in time"],
       ["no view of who else is due", "no view of who is approved", "no view of what could move"])],
     [(3, "The gap goes unused",
       ["paid per visit, so unpaid", "the clinician absorbs it", "the drive was already made"])],
     ("INCOME AND CAPACITY LOST", "The clinician carries the cost,", "not the branch.")),

    ("4", "THE PERIOD CLOSES", "TWO DEADLINES PASS UNSEEN",
     [(C["hchb"], ["Day 25: one visit", "below the floor"],
       ["nobody is shown this", "five days still remain", "one visit would have held it"]),
      (C["pcc"], ["Reassessment due"],
       ["one task among forty", "cleared in a bulk pass", "the window closes three days later"])],
     [(2, "Period reprices", ["paid at per-visit rates", "for the whole period"]),
      (3, "Therapy written off", ["delivered, and paid for", "but not billable"])],
     ("REVENUE FORFEITED", "A full period repriced, and", "delivered therapy unbillable.")),
]

TGT_BANDS = [
    ("1", "THE REFERRAL   ·   FRIDAY TO SUNDAY", "BOTH ADMITTING SLOTS GET USED",
     [(C["intake"], ["Referral accepted", "in Commure"],
       ["discharge risk flagged", "slot held, marked provisional", "sales confirmation recorded"]),
      (C["hchb"], ["Saturday, 7am", "readiness check"],
       ["discharge confirmed slipped", "slot released automatically", "no one had to notice"]),
      (C["pcc"], ["Saturday slot", "reassigned by 8am"],
       ["a second admission was waiting", "that patient is seen today", "the slot is not lost"]),
      (C["pcc"], ["Sunday call made", "early in the day"],
       ["patient still defers to Monday", "the system does not change that", "slot reassigned by 10am"])],
     [], ("CAPACITY USED", "Both admitting slots delivered", "an admission each.")),

    ("2", "ADMISSION AND THE PLAN OF CARE   ·   MONDAY", "THE BUDGET IS IN THE ROOM",
     [(C["clin"], ["Start of care", "delivered Monday"],
       ["the patient's own choice", "unchanged by any system", "the same Monday start"]),
      (C["clin"], ["Frequency written", "with the budget shown"],
       ["payer allowance on screen", "visit floor shown for the period", "shown, never enforced"]),
      (C["dcs"], ["QA and plan lock"],
       ["unchanged"]),
      (C["hchb"], ["Care team assigned", "once, at referral"],
       ["not once per discipline", "the task burst collapses", "one approval, not eight"])],
     [], ("EXPOSURE AVOIDED", "Frequency set against the real", "budget and the real floor.")),

    ("3", "THE WEEKS THAT FOLLOW", "THE GAP IS FILLED IN MINUTES",
     [(C["pat"], ["Patient cancels", "Tuesday's visit"],
       ["called Monday evening", "rebooked on the call", "unchanged from today"]),
      (C["hchb"], ["Gap detected", "immediately"],
       ["candidates ranked by drive time", "approval and discipline checked", "flexible visits identified"]),
      (C["clin"], ["Three options offered", "to the clinician"],
       ["accepted eight minutes later", "the clinician still chooses", "nothing is assigned to them"])],
     [(3, "Visit delivered in the gap",
       ["income protected", "another patient seen sooner", "the day holds together"])],
     ("INCOME AND CAPACITY KEPT", "The day holds together and", "the clinician is paid.")),

    ("4", "THE PERIOD CLOSES", "BOTH DEADLINES ARRIVE EARLY",
     [(C["hchb"], ["Day 18: tracking", "below the floor"],
       ["twelve days still available", "flagged to the branch", "while it can still be fixed"]),
      (C["clin"], ["A clinically needed", "visit is scheduled"],
       ["already in the plan of care", "no visit added for a number", "clinical judgment unchanged"]),
      (C["hchb"], ["Reassessment shown", "ten days out"],
       ["with its deadline attached", "not buried in a queue", "completed inside the window"])],
     [(3, "Period pays in full", ["the floor was cleared", "therapy stays billable"])],
     ("REVENUE PROTECTED", "Full period payment, and", "therapy stays billable.")),
]

SUMMARY = [
    ("1  ADMITTING TIME",
     ["two slots expired before", "the patient was ready"],
     ["released early, reassigned", "to waiting admissions"]),
    ("2  THE PLAN OF CARE",
     ["written blind to the payer", "budget and the visit floor"],
     ["written with both in view", "at the moment of decision"]),
    ("3  THE CANCELLED VISIT",
     ["a gap the branch could not", "fill inside the day"],
     ["refilled in minutes, income", "and capacity both kept"]),
    ("4  THE TWO DEADLINES",
     ["both passed unseen, both", "cost real money"],
     ["both surfaced while days", "still remained"]),
]

LEG = [("Intake", C["intake"]), ("Insurance & Auth", C["auth"]), ("PCC / Scheduler", C["pcc"]),
       ("Clinician", C["clin"]), ("DCS", C["dcs"]), ("HCHB", C["hchb"]), ("Patient", C["pat"])]


def draw_rows(bands, y0, x0, chipx, accent):
    for i, (_num, _phase, _claim, steps, terms, out) in enumerate(bands):
        b = y0 + i * (BH_ + 24)
        row(b + 58, [(col, lines, subs, None, 1) for col, lines, subs in steps], x0=x0)
        for slot, label, subs in terms:
            cx = x0 + slot * SLOT + BW / 2
            oval(cx, b + 103, BW / 2, 45, "#fff", [label], outline=INK)
            arrow(cx - BW / 2 - 28, b + 103, cx - BW / 2 - 6, b + 103)
            sublist(cx - BW / 2, b + 174, subs)
        head, l2, l3 = out
        chip(chipx, b + 58, 440, 96, ["", l2, l3], INK)
        add(f'<text x="{chipx + 220}" y="{b + 88}" class="ct" text-anchor="middle" '
            f'style="fill:{accent};font-weight:700">{esc(head)}</text>')


# ════════════════════════════════════════════════════════════════ single sheets
if MODE in ("current", "target"):
    CUR = MODE == "current"
    bands = CUR_BANDS if CUR else TGT_BANDS
    accent = LOSS if CUR else SAVE
    W, H = 2600, 1880
    begin(W, H, aria=("One referral followed through a single episode, "
                      + ("current state, showing four points at which money leaves the business."
                         if CUR else
                         "target state eighteen months on, with the same patient decisions.")))
    masthead("COMPASSUS HOME HEALTH  ·  "
             + ("CURRENT STATE" if CUR else "TARGET STATE, EIGHTEEN MONTHS ON"),
             "One referral, one episode" + ("" if CUR else "  —  the same week, after"),
             ("Friday afternoon to the close of the first payment period. "
              "Four points where money leaves." if CUR else
              "The same patient, the same decisions they make, and what changes around them."))
    legend(LEG, x=1500, per_row=4)
    lbl(36, 224, "TRIGGER", cls="trg")
    chip(36, 248, 264, 90, ["Referral accepted", "Friday, 4pm"], INK)
    arrow(306, 293, 344, 293)

    for i, (num, phase, claim, *_rest) in enumerate(bands):
        band(190 + i * (BH_ + 24), BH_, f"{num}  ·  {phase}", claim, slots=6)
    draw_rows(bands, 190, IX, 1520, accent)

    P = 1455
    panel(320, P, 1698, 195,
          "WHAT THIS EPISODE COST, IN ORDER" if CUR else "WHAT CHANGED, IN ORDER")
    for j, (head, cur_items, tgt_items) in enumerate(SUMMARY):
        x = 350 + j * 420
        column_rule(x - 14, P + 54, P + 70, accent)
        lbl(x - 14, P + 92, head, cls="colh")
        sublist(x - 20, P + 122, cur_items if CUR else tgt_items)
    add(f'<rect x="2060" y="{P + 20}" width="470" height="112" rx="8" fill="none" '
        f'stroke="{RULE}" stroke-width="1.6" stroke-dasharray="7 5"/>')
    lbl(2080, P + 48, "LEVERS ON THIS SHEET", cls="colh")
    for k, (tag, nm) in enumerate([("L1", "Admission Throughput"),
                                   ("L3", "Same-Day Schedule Recovery"),
                                   ("L4", "Episode Payment Protection"),
                                   ("L5", "Reassessment Window Compliance")]):
        yy = P + 72 + k * 19
        add(f'<text x="2080" y="{yy}" class="sub" style="fill:{accent};font-weight:700">{tag}</text>')
        add(f'<text x="2118" y="{yy}" class="sub">{esc(nm)}</text>')
    footer(("Current state, August 2026.  A representative composite of documented branch patterns, "
            "not a single named case.  Nothing on this sheet is a proposal."
            if CUR else
            "TARGET STATE  ·  A PROPOSAL.  Eighteen months after implementation.  The patient makes "
            "the same decisions; what changes is what happens around them."),
           "Compassus Home Health  ·  One referral, one episode")

# ════════════════════════════════════════════════════════════════ combined
else:
    W, H = 4300, 1950
    begin(W, H, aria="One referral through one episode, current state and target state side by side.")
    masthead("COMPASSUS HOME HEALTH  ·  CURRENT STATE AND TARGET STATE",
             "One referral, one episode  —  today, and eighteen months on",
             "The same patient and the same decisions they make. Only what happens around them changes.")
    legend(LEG, x=3060, per_row=4)

    add(f'<rect x="320" y="172" width="1858" height="38" rx="6" fill="{LOSS}"/>')
    add('<text x="1249" y="198" class="band" text-anchor="middle" style="fill:#fff">'
        'TODAY</text>')
    add(f'<rect x="2240" y="172" width="1858" height="38" rx="6" fill="{SAVE}"/>')
    add('<text x="3169" y="198" class="band" text-anchor="middle" style="fill:#fff">'
        'EIGHTEEN MONTHS ON</text>')

    Y0 = 232
    for i in range(4):
        b = Y0 + i * (BH_ + 24)
        num, phase, claim = CUR_BANDS[i][0], CUR_BANDS[i][1], CUR_BANDS[i][2]
        band(b, BH_, f"{num}  ·  {phase}", claim, slots=6, x=320)
        band(b, BH_, "", TGT_BANDS[i][2], slots=6, x=2240)
    draw_rows(CUR_BANDS, Y0, 350, 1520, LOSS)
    draw_rows(TGT_BANDS, Y0, 2270, 3440, SAVE)

    P = Y0 + 4 * (BH_ + 24) + 16
    panel(320, P, 1858, 180, "WHAT IT COST")
    panel(2240, P, 1858, 180, "WHAT CHANGED")
    for j, (head, cur_items, tgt_items) in enumerate(SUMMARY):
        for base, items, acc in ((350, cur_items, LOSS), (2270, tgt_items, SAVE)):
            x = base + j * 452
            column_rule(x - 14, P + 50, P + 66, acc)
            lbl(x - 14, P + 88, head, cls="colh")
            sublist(x - 20, P + 116, items)
    add(f'<rect x="320" y="{P + 200}" width="1858" height="70" rx="8" fill="none" '
        f'stroke="{RULE}" stroke-width="1.6" stroke-dasharray="7 5"/>')
    lbl(340, P + 228, "LEVERS ON THIS SHEET", cls="colh")
    xx = 340
    for tag, nm in [("L1", "Admission Throughput"), ("L3", "Same-Day Schedule Recovery"),
                    ("L4", "Episode Payment Protection"), ("L5", "Reassessment Window Compliance")]:
        add(f'<text x="{xx}" y="{P + 252}" class="sub" style="fill:{INK};font-weight:700">{tag}</text>')
        add(f'<text x="{xx + 32}" y="{P + 252}" class="sub">{esc(nm)}</text>')
        xx += 42 + 7 * len(nm)
    footer("Left: current state, a representative composite of documented branch patterns.   "
           "Right: TARGET STATE, A PROPOSAL, eighteen months after implementation.",
           "Compassus Home Health  ·  One referral, one episode")

print("mode", MODE, "| canvas", W, "x", H, "| ratio", round(W / H, 2))
finish("flow.svg")
