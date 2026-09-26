# -*- coding: utf-8 -*-
"""Flow V2 — Axle Health overlay. Vendor overlay, NOT current state.

The Compassus episode as mapped in the current-state set, with Axle Health placed where it would
sit as demoed on 22 Sep 2026, and each step badged for automation: in Axle today, in development,
paused, or an open opportunity for Compassus. Same vendor colour as V1 so the overlays compare.
Canvas units = points on the output sheet.

    python3 _flow-vendor-axle.gen.py <out.svg>
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3] / ".claude/skills/process-flow-map/assets"))
from flowkit import *

SYNC = "#A33A6B"                     # the vendor system acting by itself (same slot on every overlay)
OUT = sys.argv[1] if len(sys.argv) > 1 else "flow.svg"

KIND = {  # automation badge: text, fill, stroke, text colour, dashed
    "live":  ("IN AXLE TODAY",   INK,       INK,       "#FFFFFF", False),
    "road":  ("IN DEVELOPMENT",  "#FFFFFF", INK,       INK,       True),
    "build": ("PAUSED",          "#FFFFFF", C["auth"], "#B4520F", False),
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
    "Vendor overlay of Axle Health on the Compassus home health episode, as demoed on 22 September "
    "2026. Five bands: referral to admission, where Axle supplies capacity by zip and could take a "
    "real-time intake feed; which clinician, where Axle recommends a care team with every factor shown; "
    "which day, where Axle bulks out visits inside fulfillment windows but the three-hour HCHB feed "
    "blocks routine orders; the day before and the day of, where the clinician optimizes and Axle texts "
    "the patient a confirmation; and when the day breaks, where the call-out reassignment flow is live. "
    "A panel on the right lists what is automated today, what is paused or in development, and the "
    "open opportunities."))
masthead("COMPASSUS HOME HEALTH  ·  VENDOR OVERLAY V2",
         "Axle Health on the Compassus Episode",
         "Where Axle would sit in our flow as demoed on 22 Sep 2026, and where automation is live, "
         "paused or still open")
legend([("Intake", C["intake"]), ("Insurance & Auth", C["auth"]), ("PCC / Scheduler", C["pcc"]),
        ("Clinician", C["clin"]), ("Patient", C["pat"]), ("Branch Leadership", C["lead"]),
        ("HCHB", C["hchb"]), ("Axle Health", SYNC)], x=1500, cy=56, per_row=4, gap=30)

# automation key
KY = 188
lbl(50, KY+6, "AUTOMATION", cls="trg")
kx = 320
for kind, desc in [("live", "demonstrated in software"), ("road", "stated as in development"),
                   ("build", "built, switched off"), ("opp", "not built · ours to push")]:
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
rA = band(AY, AH, "A  ·  REFERRAL TO ADMISSION", "AXLE SEES CAPACITY, NOT THE REFERRAL", slots=5)
chip(50, AY+60+BH/2-39, 250, 78, ["Referral arrives"], INK)
lbl(50, AY+60+BH/2-53, "TRIGGER", cls="trg")
arrow(300, AY+60+BH/2, IX-6, AY+60+BH/2)
cA, xA = steps_row(AY+60, [
    (C["intake"], ["Referral validated", "in intake platform"],
     ["Demographics, disciplines, auths", "Real-time feed to Axle offered", "Axle: \u201cgreat news\u201d"],
     "opp", None),
    (C["lead"], ["Accept or decline", "the referral"],
     ["Axle: utilization by zip", "Who could take this patient", "Not yet wired to intake"],
     "opp", None),
    (C["auth"], ["Verify eligibility,", "key pending auth"],
     ["Axle still schedules the visit", "Flagged as not yet writable", "Counted in capacity"],
     None, None),
    (C["pcc"], ["Welcome call, book", "SOC and evals"],
     ["SOC and eval work queues", "Patient constraints captured", "Care team recommended"],
     "live", None),
    (C["clin"], ["SOC and evals; each", "discipline writes", "its frequency"],
     ["Written in HCHB", "Reaches Axle on the next", "log ship"],
     None, "× N disciplines"),
])

# ---------------------------------------------------------------- data-in boundary
BY = AY + AH + 30
add(f'<line x1="{BX}" y1="{BY+24}" x2="{IX+260}" y2="{BY+24}" stroke="{C["hchb"]}" '
    'stroke-width="2.5" stroke-dasharray="14 7"/>')
add(f'<line x1="{IX+1270}" y1="{BY+24}" x2="{rA}" y2="{BY+24}" stroke="{C["hchb"]}" '
    'stroke-width="2.5" stroke-dasharray="14 7"/>')
add(f'<rect x="{IX+270}" y="{BY+4}" width="990" height="40" rx="20" fill="{PAPER}" '
    f'stroke="{C["hchb"]}" stroke-width="2"/>')
lbl(IX+765, BY+30, "NEW PATIENTS: INTAKE API, REAL TIME  ·  ROUTINE ORDERS: HCHB LOG SHIP, 3 h (AXLE NEEDS ~10–15 min)",
    "middle", "boundary")
lbl(50, BY+30, "DATA IN", cls="trg")

# ---------------------------------------------------------------- B  which clinician
BYY, BHH = BY + 70, 262
rB = band(BYY, BHH, "B  ·  WHICH CLINICIAN", "AXLE RECOMMENDS · A PERSON DECIDES", slots=5)
cB, xB = steps_row(BYY+60, [
    (SYNC, ["Flags an incomplete", "care team"],
     ["One of 15 work queues", "Cleared to zero daily"], "live", None),
    (SYNC, ["Recommends a clinician", "per discipline"],
     ["Territory, licence, capacity", "Employment type, distance", "Your logic, from a survey"],
     "live", None),
    (C["pcc"], ["Accept or override", "the care team"],
     ["Every factor shown", "Top of licence preferred", "PTO and fullness counted"], None, None),
    (SYNC, ["Every visit inherits", "the care team"],
     ["Unless someone overrides", "Write-back to HCHB paused"], "build", None),
    (C["clin"], ["Clinician told why", "they got the patient"],
     ["Axle routes this via manager", "By design, to avoid disputes", "Colin wants it direct"],
     "opp", None),
])

# ---------------------------------------------------------------- C  which day
CY, CH = BYY + BHH + 40, 300
rC = band(CY, CH, "C  ·  WHICH DAY — THE EPISODE", "THE ENGINE EXISTS · THE DATA DOESN\u2019T", slots=5)
cC, xC = steps_row(CY+60, [
    (C["hchb"], ["Frequency lands", "via HCHB workflow"],
     ["Scheduler plots it today", "Reaches Axle up to 3 h late"], None, None),
    (SYNC, ["Bulks out visits in", "fulfillment windows"],
     ["Medicare week, front-loading", "Same-order spacing", "Patient\u2019s usual weekday"], "live", None),
    (C["pcc"], ["Review and apply", "the dates"],
     ["Or the clinician sets days", "Configurable per role"], None, None),
    (SYNC, ["Writes the schedule", "back by RPA"],
     ["Built, switched off", "No live HCHB customer"], "build", None),
    (SYNC, ["Episode checks", "in work queues"],
     ["Eval before SOC, re-eval due", "Recert vs discharge", "LUPA pacing not shown"], "live", None),
])
lbl(IX, CY+CH-16, "Axle is ready for the day-of-week decision our schedulers make by hand today. "
    "At a 3-hour HCHB feed it cannot see new orders in time to make it.", "start", "hi")

# ---------------------------------------------------------------- D  day before / day of
DY, DH = CY + CH + 40, 262
rD = band(DY, DH, "D  ·  THE DAY BEFORE AND THE DAY OF", "CONFIRM, DON\u2019T ASK", slots=6)
cD, xD = steps_row(DY+60, [
    (C["clin"], ["Ask about next week", "at this visit"],
     ["Negotiation moves earlier", "Visit or standing constraint", "Replaces the evening calls"],
     None, None),
    (C["clin"], ["Optimize, then", "finalize the day"],
     ["Two taps, the night before", "Routes around own blocks", "Sequence, not clock times"],
     "live", None),
    (SYNC, ["Texts each patient", "an arrival window"],
     ["SMS, no patient app", "A confirmation, not a question", "Twilio under a BAA"], "live", None),
    (C["pat"], ["Patient replies", "if it won\u2019t work"],
     ["Reply goes to the clinician", "Agentic two-way: not advised", "Self-scheduling exists"],
     "opp", None),
    (C["clin"], ["Visits documented", "in PointCare"],
     ["Axle keeps the schedule", "EMR keeps the record"], None, None),
    (SYNC, ["Tracks location", "en route only"],
     ["Clinician starts each trip", "Whole-shift: a policy choice", "Miles logged for pay"],
     "live", None),
])

# ---------------------------------------------------------------- E  exceptions
EY, EH = DY + DH + 40, 262
rE = band(EY, EH, "E  ·  WHEN THE DAY BREAKS", "RUN LIVE IN THE DEMO", slots=6)
cE, xE = steps_row(EY+60, [
    (C["pcc"], ["Shift marked", "out sick"],
     ["Visits open in a", "reassign flow"], None, None),
    (SYNC, ["New clinician, or", "same clinician new day"],
     ["Every factor shown", "Front-loads within the week", "Or flip the service code"],
     "live", None),
    (C["pcc"], ["Accept all,", "submit"],
     ["Seconds, not an hour", "Call a PRN first if needed"], None, None),
    (SYNC, ["Push to the", "covering clinician"],
     ["Default notification", "Human call stays optional"], "live", None),
    (SYNC, ["Nobody fits: names", "the best anyway"],
     ["Prompts the office to call", "Incentives: in development"], "road", None),
    (SYNC, ["Missed visits queued", "for clinical managers"],
     ["Clinical managers work it", "MD notice: not shown"], "live", None),
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
    ("live", "AUTOMATED IN AXLE TODAY", [
        "Work queues for every scheduling gap (B, C)",
        "Care-team recommendation with the math (B)",
        "Dates inside fulfillment windows (C)",
        "Route optimizer and patient texts (D)",
        "Call-out reassignment in seconds (E)",
        "Utilization and forecast by zip (A)",
        "Analytics that audit the assignment logic",
    ]),
    ("build", "PAUSED", [
        "HCHB read and RPA write-back (B, C)",
        "Waits on a faster, reliable HCHB feed",
    ]),
    ("road", "IN DEVELOPMENT OR NOT BUILT", [
        "Dynamic incentives for hard-to-fill visits (E)",
        "Workday integration for availability",
        "Mobile app shown only by video, to come",
    ]),
    ("opp", "OPEN OPPORTUNITIES FOR COMPASSUS", [
        "Real-time intake feed for new patients (A)",
        "Capacity inside the accept / decline call (A)",
        "HCHB refresh by object: orders fast (C)",
        "Clinician sees why they got a patient (B)",
        "Two-way patient scheduling on top of confirm (D)",
        "LUPA pacing on the shared scenario (C)",
        "Marketing forecasts in and out of Axle (A)",
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
lbl(PX + 26, sy + 4, "Almost every step is live. The gap is the", "start", "hi")
lbl(PX + 26, sy + 26, "HCHB feed, and that one is ours.", "start", "hi")
print("panel 1 content ends", sy + 26, "panel bottom", PY + P1H)

# ---------------------------------------------------------------- right panel: the data path
QY = PY + P1H + 30
QH = last_y - QY
panel(PX, QY, PW, QH, "THE DATA PATH — WHAT GATES GO-LIVE")
nx, nw, nh = PX + 30, 190, 56
row1 = QY + 70
block(nx, row1, nw, nh, C["intake"], ["Intake platform"], small=True)
block(nx + 300, row1, nw, nh, SYNC, ["Axle"], small=True)
arrow(nx + nw, row1 + nh/2, nx + 300 - 6, row1 + nh/2)
lbl(nx + nw + 55, row1 + nh/2 - 10, "API", "middle", "lb")
lbl(nx + nw + 55, row1 + nh + 20, "real time", "middle", "lb")
row2 = row1 + 110
block(nx, row2, nw, nh, C["hchb"], ["HCHB orders"], small=True)
block(nx + 300, row2, nw, nh, SYNC, ["Axle"], small=True)
block(nx + 600, row2, nw - 40, nh, C["hchb"], ["HCHB"], small=True)
arrow(nx + nw, row2 + nh/2, nx + 300 - 6, row2 + nh/2)
arrow(nx + 300 + nw, row2 + nh/2, nx + 600 - 6, row2 + nh/2, dash=True)
lbl(nx + nw + 55, row2 + nh/2 - 10, "log ship", "middle", "lb")
lbl(nx + nw + 55, row2 + nh + 20, "3 h today", "middle", "lb")
lbl(nx + 300 + nw + 55, row2 + nh/2 - 10, "RPA", "middle", "lb")
lbl(nx + 300 + nw + 55, row2 + nh + 20, "paused", "middle", "lb")
lbl(nx, row2 + nh + 56, "Axle won\u2019t go live on data it can\u2019t time: new-patient data within", "start", "note")
lbl(nx, row2 + nh + 78, "~10 minutes, predictably. The intake feed covers new patients;", "start", "note")
lbl(nx, row2 + nh + 100, "routine orders need a faster HCHB refresh before band C works.", "start", "note")
print("panel 2 content ends", row2 + nh + 100, "panel bottom", QY + QH)

# ---------------------------------------------------------------- where it breaks
WY = last_y + 40
lbl(50, WY+34, "WHERE IT", cls="trg"); lbl(50, WY+52, "BREAKS", cls="trg")
brk = [(["Routine orders reach Axle", "~3 h late at Compassus"], C["hchb"]),
       (["Write-back paused — no live", "HCHB customer yet"], SYNC),
       (["Confirm-don\u2019t-ask vs our", "agentic two-way ambition"], C["pat"]),
       (["Assignment rationale goes", "to managers, not clinicians"], C["clin"]),
       (["No Workday feed; availability", "entry optional by default"], C["pcc"])]
wx = IX
for lines, col in brk:
    block(wx, WY+8, 470, 70, col, lines, small=True)
    wx += 490
print("last content y", WY + 78, "footer rule", H - 72)

footer("Vendor overlay · Axle Health as demoed 22 Sep 2026 · not current state and not a "
       "recommendation", "Overlay V2 · Axle Health")
finish(OUT)
