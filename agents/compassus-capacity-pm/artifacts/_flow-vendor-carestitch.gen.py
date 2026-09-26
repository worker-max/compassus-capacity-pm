# -*- coding: utf-8 -*-
"""Flow V3 — CareStitch overlay. Vendor overlay, NOT current state.

The Compassus episode as mapped in the current-state set, with CareStitch placed where it would
sit as demoed on 23 Sep 2026, and each step badged for automation: in CareStitch today, roadmap,
beta (the HCHB integration), or an open opportunity for Compassus. Same vendor colour as V1/V2.
Canvas units = points on the output sheet.

    python3 _flow-vendor-carestitch.gen.py <out.svg>
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3] / ".claude/skills/process-flow-map/assets"))
from flowkit import *

SYNC = "#A33A6B"                     # the vendor system acting by itself (same slot on every overlay)
OUT = sys.argv[1] if len(sys.argv) > 1 else "flow.svg"

KIND = {  # automation badge: text, fill, stroke, text colour, dashed
    "live":  ("IN CARESTITCH TODAY", INK,   INK,       "#FFFFFF", False),
    "road":  ("ROADMAP",         "#FFFFFF", INK,       INK,       True),
    "build": ("BETA",            "#FFFFFF", C["auth"], "#B4520F", False),
    "opp":   ("OPPORTUNITY",     "#FFF1C2", "#B8900F", "#6E5200", False),
}

def abadge(x, y, w, kind):
    t, fill, stroke, tc, dash = KIND[kind]
    bw = 8.3*len(t) + 18
    d = ' stroke-dasharray="4 3"' if dash else ''
    add(f'<rect x="{x+w-bw-8}" y="{y-14}" width="{bw}" height="23" rx="11.5" fill="{fill}" '
        f'stroke="{stroke}" stroke-width="1.8"{d}/>')
    add(f'<text x="{x+w-bw/2-8}" y="{y+2}" class="bdg" text-anchor="middle" '
        f'style="fill:{tc}">{esc(t)}</text>')

def steps_row(y, steps, breaks=()):
    """steps: (fill | (left, right), lines, subs, kind|None, qualifier|None).
    Returns (centreline, [x of each block])."""
    xs, cy = [], y + BH/2
    for i, (fill, lines, subs, kind, qual) in enumerate(steps):
        x = IX + i*SLOT
        xs.append(x)
        if isinstance(fill, tuple):
            split_block(x, y, BW, BH, fill[0], fill[1], lines)
        else:
            block(x, y, BW, BH, fill, lines)
        if kind:
            abadge(x, y, BW, kind)
        if qual:
            lbl(x+8, y-6, qual, cls="lb")
        if subs:
            sublist(x, y+BH+26, subs)
        if i:
            if i in breaks:
                mx = x - GAP/2
                add(f'<line x1="{mx}" y1="{y-4}" x2="{mx}" y2="{y+BH+4}" stroke="{MUT}" '
                    'stroke-width="2" stroke-dasharray="6 5"/>')
                lbl(mx, y-16, "OR", "middle", "trg")
            else:
                arrow(xs[i-1]+BW, cy, x-6, cy)
    return cy, xs

W, H = 2900, 2060
begin(W, H, aria=(
    "Vendor overlay of CareStitch on the Compassus home health episode, as demoed on 23 September "
    "2026. Five bands: referral to admission, where CareStitch shows open points by clinician for an "
    "address; which clinician, where the scheduler filters to eligible clinicians and assigns by hand "
    "or sends a staffing request to priority groups; which day, where orders and frequencies are not "
    "ingested and the HCHB integration is a read-only beta; the day before and the day of, where the "
    "clinician still phones patients with click-to-call and a call log; and when the day breaks, where "
    "call-outs are reassigned by hand or offered as a request. A right-hand panel lists what is live, "
    "roadmap, beta and open."))
masthead("COMPASSUS HOME HEALTH  ·  VENDOR OVERLAY V3",
         "CareStitch on the Compassus Episode",
         "Where CareStitch would sit in our flow as demoed on 23 Sep 2026, and where automation is live, "
         "beta, roadmap or still open")
legend([("Intake", C["intake"]), ("Insurance & Auth", C["auth"]), ("PCC / Scheduler", C["pcc"]),
        ("Clinician", C["clin"]), ("Patient", C["pat"]), ("Branch Leadership", C["lead"]),
        ("HCHB", C["hchb"]), ("CareStitch", SYNC)], x=1500, cy=56, per_row=4, gap=30)

# automation key
KY = 188
lbl(50, KY+6, "AUTOMATION", cls="trg")
kx = 320
for kind, desc in [("live", "demonstrated in software"), ("road", "named as roadmap, no date"),
                   ("build", "built, not in production"), ("opp", "not built · ours to push")]:
    t = KIND[kind][0]
    bw = 8.3*len(t) + 18
    abadge(kx - 8 + bw + 8, KY+12, 0, kind)
    lbl(kx + bw + 12, KY+6, desc, cls="note")
    kx += bw + 12 + 7.2*len(desc) + 44

BR = BX + 6*SLOT + 30
PX = BR + 44
PW = W - 50 - PX

# ---------------------------------------------------------------- A  referral to admission
AY, AH = 235, 262
rA = band(AY, AH, "A  ·  REFERRAL TO ADMISSION", "CAPACITY YOU CAN SEE, NOT A NUMBER", slots=5)
chip(50, AY+60+BH/2-39, 250, 78, ["Referral arrives"], INK)
lbl(50, AY+60+BH/2-53, "TRIGGER", cls="trg")
arrow(300, AY+60+BH/2, IX-6, AY+60+BH/2)
cA, xA = steps_row(AY+60, [
    (C["intake"], ["Referral validated", "in intake platform"],
     ["Written to HCHB by RPA", "CareStitch API in development", "Labels could flow in"],
     "opp", None),
    ((C["lead"], SYNC), ["Accept or decline:", "open points by day"],
     ["Enter address, discipline", "Filter to PICC, language…", "No branch total, no forecast"],
     "live", None),
    (C["auth"], ["Verify eligibility,", "key pending auth"],
     ["Not ingested by CareStitch", "Custom property at best", "Pending demand invisible"],
     None, None),
    (C["pcc"], ["Welcome call, book", "SOC and evals"],
     ["Pending admits as a", "staffing-request queue", "Office notes shared"], None, None),
    (C["clin"], ["SOC and evals; each", "discipline writes", "its frequency"],
     ["Written in HCHB", "Orders not ingested", "by CareStitch"],
     None, "× N disciplines"),
])

# ---------------------------------------------------------------- data-in boundary
BY = AY + AH + 30
add(f'<line x1="{BX}" y1="{BY+24}" x2="{IX+280}" y2="{BY+24}" stroke="{C["hchb"]}" '
    'stroke-width="2.5" stroke-dasharray="14 7"/>')
add(f'<line x1="{IX+1250}" y1="{BY+24}" x2="{rA}" y2="{BY+24}" stroke="{C["hchb"]}" '
    'stroke-width="2.5" stroke-dasharray="14 7"/>')
add(f'<rect x="{IX+290}" y="{BY+4}" width="950" height="40" rx="20" fill="{PAPER}" '
    f'stroke="{C["hchb"]}" stroke-width="2"/>')
lbl(IX+765, BY+30, "HCHB → CARESTITCH: READ-ONLY BETA OR MANUAL REPORT UPLOAD  ·  NO WRITE-BACK",
    "middle", "boundary")
lbl(50, BY+30, "DATA IN", cls="trg")

# ---------------------------------------------------------------- B  which clinician
BYY, BHH = BY + 70, 262
rB = band(BYY, BHH, "B  ·  WHICH CLINICIAN", "THE SYSTEM FILTERS · THE SCHEDULER CHOOSES", slots=5)
cB, xB = steps_row(BYY+60, [
    (SYNC, ["Filters out ineligible", "clinicians"],
     ["Discipline, region by address", "Matching custom properties", "Seen-before asterisk"], "live", None),
    (C["pcc"], ["Assign directly by", "points and distance"],
     ["No ranking or suggestion", "Colour-coded open points", "Distance to nearest visit"], None, None),
    (SYNC, ["Or offer by request", "to priority groups"],
     ["Full-time first, then PRN", "Delays and reminders", "Read-and-reply log"], "live", None),
    (C["pcc"], ["Pick from those", "who said yes"],
     ["Or auto-assign first taker", "Clinician comments shown"], None, None),
    (SYNC, ["Recommends the", "best clinician"],
     ["Recommendation engine", "comes before any AI", "No date"], "road", None),
])

# ---------------------------------------------------------------- C  which day
CY, CH = BYY + BHH + 40, 300
rC = band(CY, CH, "C  ·  WHICH DAY — THE EPISODE", "THE EPISODE STAYS IN HCHB", slots=5)
cC, xC = steps_row(CY+60, [
    (C["hchb"], ["Frequency plotted", "via HCHB workflow"],
     ["Scheduler plots it today", "Unchanged by CareStitch"], None, None),
    (SYNC, ["Tasks read from", "HCHB into CareStitch"],
     ["Read-only screen beta", "Or agency uploads reports", "Never run in production"], "build", None),
    (C["pcc"], ["Spread the week by", "eye on the grid"],
     ["Medicare week Sun–Sat", "Points, map, mileage", "Front-loading is manual"], None, None),
    (SYNC, ["Episode guardrails", "and LUPA pacing"],
     ["SOC before eval: none", "LUPA: roadmap", "“Lives in the EMR”"], "road", None),
    (SYNC, ["Completion syncs", "back as a check mark"],
     ["Read from HCHB status", "No write-back"], "build", None),
])
lbl(IX, CY+CH-16, "CareStitch plans the week around HCHB, not with it. Orders, auth and compliance windows stay "
    "with the scheduler and the EMR.", "start", "hi")

# ---------------------------------------------------------------- D  day before / day of
DY, DH = CY + CH + 40, 262
rD = band(DY, DH, "D  ·  THE DAY BEFORE AND THE DAY OF", "THE CLINICIAN STILL CALLS", slots=6)
cD, xD = steps_row(DY+60, [
    (C["clin"], ["Call the patient", "from the app"],
     ["Click-to-call any number", "Call logged automatically", "Office can see the log"], "live", None),
    (C["clin"], ["Book the visit on the", "patient calendar"],
     ["Drive-time blocks shown", "Other disciplines in red", "Anchor fixed visits first"],
     None, None),
    (SYNC, ["Confirms the patient", "by text"],
     ["Top-five roadmap item", "Negotiation needs the engine"], "road", None),
    (C["pat"], ["Patient reschedules", "or negotiates"],
     ["Two-way, agentic: not built", "Compassus’s biggest ask"], "opp", None),
    (C["clin"], ["Visits documented", "in PointCare / HCHB"],
     ["CareStitch holds the plan", "HCHB holds the record"], None, None),
    (SYNC, ["Office optimizes", "routes centrally"],
     ["Optimize Route button", "Clinicians place one by one", "Offline-first mobile"], "live", None),
])

# ---------------------------------------------------------------- E  exceptions
EY, EH = DY + DH + 40, 262
rE = band(EY, EH, "E  ·  WHEN THE DAY BREAKS", "FAST, BUT BY HAND", slots=6)
cE, xE = steps_row(EY+60, [
    (C["clin"], ["Call-out, or reassign", "request from phone"],
     ["Lands in the office queue"], None, None),
    (C["pcc"], ["Reassign visit", "by visit"],
     ["Pre-filtered by points", "No suggested cover"], None, None),
    (SYNC, ["Or blast a request", "to priority groups"],
     ["Red when deadline near", "Blue when someone says yes"], "live", None),
    (SYNC, ["Nobody takes it:", "widen the search"],
     ["Add other territories", "Distance shown"], "live", None),
    (C["pcc"], ["Assign and", "push to the phone"],
     ["Or auto-assign first taker"], None, None),
    (SYNC, ["Care-team chat", "keeps everyone in"],
     ["Room per patient, auto-joined", "Export per cert period"], "live", None),
])

# ---------------------------------------------------------------- band-to-band connectors
def link(xfrom, cfrom, y_next, c_next, redge):
    conn(f"M {xfrom+BW} {cfrom} L {redge+18} {cfrom} L {redge+18} {y_next-20} L {BX-30} {y_next-20} "
         f"L {BX-30} {c_next}")
    arrow(BX-30, c_next, IX-6, c_next)
link(xA[-1], cA, BYY, cB, rA)
link(xB[-1], cB, CY, cC, rB)
link(xC[-1], cC, DY, cD, rC)
conn(f"M {BX-30} {cD} L {BX-30} {EY+60+BH/2}", dash=True)
arrow(BX-30, EY+60+BH/2, IX-6, EY+60+BH/2, dash=True)
lbl(BX-38, cD+100, "when a visit", "end", "lb")
lbl(BX-38, cD+118, "falls through", "end", "lb")

last_y = EY + EH

# ---------------------------------------------------------------- right panel: automation map
PY = 235
P1H = 1000
panel(PX, PY, PW, P1H, "WHERE AUTOMATION IS POSSIBLE")
sections = [
    ("live", "IN CARESTITCH TODAY", [
        "Eligibility filtering by region and properties (B)",
        "Open points by clinician and day, on a map (A)",
        "Staffing requests to priority groups (B, E)",
        "Click-to-call with automatic call log (D)",
        "Care-team chat created per patient (E)",
        "Central route optimization (D)",
    ]),
    ("build", "BETA", [
        "HCHB read by screen automation (C)",
        "No write-back of any kind",
    ]),
    ("road", "ROADMAP, NO DATE", [
        "Patient confirmation by text (D)",
        "Scheduling recommendation engine (B)",
        "LUPA and episode guardrails (C)",
        "API for other systems (A)",
    ]),
    ("opp", "OPEN OPPORTUNITIES FOR COMPASSUS", [
        "Capacity query from the intake platform (A)",
        "Plan-of-care orders fill the tasks (A, C)",
        "Agentic two-way patient scheduling (D)",
        "Suggested cover for a call-out (E)",
        "Scheduler productivity reporting",
    ]),
]
sy = PY + 80
for kind, head, items in sections:
    t = KIND[kind][0]
    bw = 8.3*len(t) + 18
    abadge(PX + 26 - 8 + bw + 8, sy, 0, kind)
    lbl(PX + 26 + bw + 14, sy + 4, head, cls="colh")
    sublist(PX + 20, sy + 38, items, lh=22)
    sy += 38 + 22*len(items) + 34
lbl(PX + 26, sy + 4, "Everything is visible and nothing is decided.", "start", "hi")
lbl(PX + 26, sy + 26, "The automation layer is still in research.", "start", "hi")
print("panel 1 content ends", sy + 26, "panel bottom", PY + P1H)

# ---------------------------------------------------------------- right panel: the request flow
QY = PY + P1H + 30
QH = last_y - QY
panel(PX, QY, PW, QH, "THE STAFFING REQUEST — THE STANDOUT")
nx, nw, nh = PX + 30, 170, 56
row1 = QY + 74
block(nx, row1, nw, nh, C["pcc"], ["Scheduler sends"], small=True)
block(nx + 250, row1, nw, nh, SYNC, ["Full-time now"], small=True)
block(nx + 500, row1, nw, nh, SYNC, ["PRN in 30 min"], small=True)
arrow(nx + nw, row1 + nh/2, nx + 250 - 6, row1 + nh/2)
arrow(nx + 250 + nw, row1 + nh/2, nx + 500 - 6, row1 + nh/2)
row2 = row1 + 110
block(nx, row2, nw, nh, C["clin"], ["Clinician replies"], small=True)
block(nx + 250, row2, nw, nh, SYNC, ["Card turns blue"], small=True)
block(nx + 500, row2, nw, nh, C["pcc"], ["Scheduler assigns"], small=True)
arrow(nx + nw, row2 + nh/2, nx + 250 - 6, row2 + nh/2)
arrow(nx + 250 + nw, row2 + nh/2, nx + 500 - 6, row2 + nh/2)
lbl(nx, row2 + nh + 56, "Replaces the Teams, email and text scramble. Every send, read and", "start", "note")
lbl(nx, row2 + nh + 78, "reply is logged, giving response-time and accept-rate data by", "start", "note")
lbl(nx, row2 + nh + 100, "clinician that Compassus does not have today.", "start", "note")
print("panel 2 content ends", row2 + nh + 100, "panel bottom", QY + QH)

# ---------------------------------------------------------------- where it breaks
WY = last_y + 40
lbl(50, WY+34, "WHERE IT", cls="trg"); lbl(50, WY+52, "BREAKS", cls="trg")
brk = [(["HCHB integration is a beta", "— read-only, never live"], C["hchb"]),
       (["Every assignment is", "a manual click"], C["pcc"]),
       (["No LUPA, window or", "sequence guardrails"], SYNC),
       (["Clinicians still phone", "every patient"], C["clin"]),
       (["No branch total or forecast", "— capacity read by eye"], C["lead"])]
wx = IX
for lines, col in brk:
    block(wx, WY+8, 470, 70, col, lines, small=True)
    wx += 490
print("last content y", WY + 78, "footer rule", H - 72)

footer("Vendor overlay · CareStitch as demoed 23 Sep 2026 · not current state and not a "
       "recommendation", "Overlay V3 · CareStitch")
finish(OUT)
