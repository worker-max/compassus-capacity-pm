# -*- coding: utf-8 -*-
"""Flow V1 — VitalisCare Sync overlay. Vendor overlay, NOT current state.

The Compassus episode as mapped in the current-state set, with VitalisCare Sync placed where it
would sit as demoed on 24 Sep 2026, and each step badged for automation: in Sync today, on the
Vitalis roadmap, acknowledged gap with no date, or an open opportunity for Compassus.
Canvas units = points on the output sheet.

    python3 _flow-vendor-vitaliscare.gen.py <out.svg>
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3] / ".claude/skills/process-flow-map/assets"))
from flowkit import *

SYNC = "#A33A6B"                     # VitalisCare Sync acting by itself (vendor overlay only)
OUT = sys.argv[1] if len(sys.argv) > 1 else "flow.svg"

KIND = {  # automation badge: text, fill, stroke, text colour, dashed
    "live":  ("IN SYNC TODAY",   INK,       INK,       "#FFFFFF", False),
    "road":  ("VITALIS ROADMAP", "#FFFFFF", INK,       INK,       True),
    "build": ("GAP · NO DATE",   "#FFFFFF", C["auth"], "#B4520F", False),
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
    "Vendor overlay of VitalisCare Sync on the Compassus home health episode, as demoed on "
    "24 September 2026. Five bands: referral to admission, where Sync is not present; who, where Sync "
    "ranks providers and the scheduler decides; when, where Sync suggests better visit days; the day "
    "before and the day of, where Sync routes the clinician and the day-before patient confirmation "
    "is the largest open opportunity; and when the day breaks, where the Call-Off Center is on the "
    "Vitalis roadmap. A panel on the right lists what is automated today, what is on the roadmap and "
    "the open opportunities."))
masthead("COMPASSUS HOME HEALTH  ·  VENDOR OVERLAY V1",
         "VitalisCare Sync on the Compassus Episode",
         "Where Sync would sit in our flow as demoed on 24 Sep 2026, and where automation is live, "
         "promised or still open")
legend([("Intake", C["intake"]), ("Insurance & Auth", C["auth"]), ("PCC / Scheduler", C["pcc"]),
        ("Clinician", C["clin"]), ("Patient", C["pat"]), ("Branch Leadership", C["lead"]),
        ("HCHB", C["hchb"]), ("VitalisCare Sync", SYNC)], x=1500, cy=56, per_row=4, gap=30)

# automation key
KY = 188
lbl(50, KY+6, "AUTOMATION", cls="trg")
kx = 320
for kind, desc in [("live", "demonstrated in software"), ("road", "in design, dated or promised"),
                   ("build", "Vitalis named the gap, no date"), ("opp", "not on their roadmap · ours to push")]:
    t = KIND[kind][0]
    bw = 8.3*len(t) + 18
    abadge(kx - 8 + bw + 8, KY+12, 0, kind)     # draw badge starting at kx
    lbl(kx + bw + 12, KY+6, desc, cls="note")
    kx += bw + 12 + 7.2*len(desc) + 44

BR = BX + 6*SLOT + 30          # right edge of the widest band
PX = BR + 44                   # right-hand automation panel
PW = W - 50 - PX

# ---------------------------------------------------------------- A  referral to admission
AY, AH = 235, 262
rA = band(AY, AH, "A  ·  REFERRAL TO ADMISSION", "SYNC NOT PRESENT", slots=5)
chip(50, AY+60+BH/2-39, 250, 78, ["Referral arrives"], INK)
lbl(50, AY+60+BH/2-53, "TRIGGER", cls="trg")
arrow(300, AY+60+BH/2, IX-6, AY+60+BH/2)
cA, xA = steps_row(AY+60, [
    (C["intake"], ["Referral validated", "in intake platform"],
     ["Addresses, disciplines, auths", "Complete before it hits HCHB", "Could stream to Sync in transit"],
     "opp", None),
    (C["lead"], ["Accept or decline", "the referral"],
     ["No live capacity read today", "Sync roll-up is roadmap", "The front door of capacity"],
     "opp", None),
    (C["auth"], ["Verify eligibility,", "key pending auth"],
     ["Payer sets the visit count", "Sync cannot see pending auth", "Needs a ready / not-ready state"],
     "build", None),
    (C["pcc"], ["Welcome call, book", "SOC and evals"],
     ["Is the patient actually home?", "SOC within 48 hours", "Sync match could pick the SOC RN"],
     "opp", None),
    (C["clin"], ["SOC and evals; each", "discipline plots", "its own frequency"],
     ["Entered in HCHB", "Sync reads it on the next", "log ship"],
     None, "× N disciplines"),
])

# ---------------------------------------------------------------- HCHB -> Sync boundary
BY = AY + AH + 30
add(f'<line x1="{BX}" y1="{BY+24}" x2="{IX+300}" y2="{BY+24}" stroke="{C["hchb"]}" '
    'stroke-width="2.5" stroke-dasharray="14 7"/>')
add(f'<line x1="{IX+1230}" y1="{BY+24}" x2="{rA}" y2="{BY+24}" stroke="{C["hchb"]}" '
    'stroke-width="2.5" stroke-dasharray="14 7"/>')
add(f'<rect x="{IX+310}" y="{BY+4}" width="910" height="40" rx="20" fill="{PAPER}" '
    f'stroke="{C["hchb"]}" stroke-width="2"/>')
lbl(IX+765, BY+30, "HCHB LOG SHIP → SYNC  ·  every ~3 h at Compassus today  ·  ~10 min at their typical client",
    "middle", "boundary")
lbl(50, BY+30, "DATA IN", cls="trg")

# ---------------------------------------------------------------- B  who
BYY, BHH = BY + 70, 262
rB = band(BYY, BHH, "B  ·  WHO — LONG-TERM ASSIGNMENT", "SYNC RECOMMENDS · SCHEDULER DECIDES", slots=5)
cB, xB = steps_row(BYY+60, [
    (C["hchb"], ["Visits generated,", "assignment task", "per discipline"],
     ["Reaches Sync on the next", "log ship"], None, None),
    (SYNC, ["Ranks the top four", "per discipline"],
     ["Smart Choice or Best Mapping", "Caseload map, service span", "Language, team, prior visit"],
     "live", None),
    (C["pcc"], ["Accept, or override", "with a reason"],
     ["The reason trains the model", "Audit trail for leadership", "No territory rule yet"],
     None, None),
    (SYNC, ["RPA writes the", "assignment to HCHB"],
     ["Seconds to minutes", "Pending until confirmed", "Breaks if HCHB screens change"],
     "live", None),
    (C["clin"], ["Clinician told why", "they got the patient"],
     ["Not built — Vitalis liked it", "Matters most out of territory"],
     "opp", None),
])

# ---------------------------------------------------------------- C  when
CY, CH = BYY + BHH + 40, 300
rC = band(CY, CH, "C  ·  WHEN — THE WEEK", "THE SCHEDULER RE-ENTERS THE WEEK", slots=5)
cC, xC = steps_row(CY+60, [
    (SYNC, ["Flags visits on", "a better day"],
     ["Co-located visits that day", "Reasons plus a day map"], "live", None),
    (C["pcc"], ["Accept once or", "recurring, or dismiss"],
     ["Drag-and-drop with flags", "Auth window, license, duplicate"], None, None),
    (SYNC, ["Writes the move", "back by RPA"],
     ["Same write-back as band B"], "live", None),
    (SYNC, ["Episode and LUPA", "pacing flags"],
     ["No SOC or recert window", "No LUPA threshold", "Front-loading logic exists"], "build", None),
    (C["clin"], ["Sees the week", "in Sync360"],
     ["Sets own working hours", "Still documents in PointCare"], None, None),
])
lbl(IX, CY+CH-16, "Today the clinician runs their own week with no scheduler workflow. Sync's optimization is "
    "scheduler-driven — decide who owns the week before buying it.", "start", "hi")

# ---------------------------------------------------------------- D  day before / day of
DY, DH = CY + CH + 40, 262
band(DY, DH, "D  ·  THE DAY BEFORE AND THE DAY OF", "THE LARGEST CLINICIAN TIME SINK", slots=6)
cD, xD = steps_row(DY+60, [
    (C["clin"], ["Confirm with the", "patient — day before"],
     ["30–60 min a day, evenings", "Two-way text would halve it", "Not built in Sync"], "opp", None),
    (C["pat"], ["Patient replies", "with availability"],
     ["On-the-way ETA text", "Fewer no-shows"], "opp", None),
    (C["clin"], ["Starts the workday", "in Sync360"],
     ["GPS only while working", "Pause for personal time"], None, None),
    (SYNC, ["Routes the day,", "reroutes live"],
     ["Hands off to Google Maps, Waze", "Recalculates as visits change"], "live", None),
    (C["clin"], ["Visits documented", "in PointCare"],
     ["A second app to carry", "Sync can listen for actions"], None, None),
    ((C["lead"], SYNC), ["Reported versus", "tracked review"],
     ["Mileage and route adherence", "Start times, device-off flags", "A trust question for clinicians"],
     "live", None),
])

# ---------------------------------------------------------------- E  exceptions
EY, EH = DY + DH + 40, 262
band(EY, EH, "E  ·  WHEN THE DAY BREAKS", "SAME-DAY RECOVERY", slots=6)
cE, xE = steps_row(EY+60, [
    (C["clin"], ["Call-off entered in", "PointCare or HCHB"],
     ["Reaches Sync up to 3 h late", "Too late to recover today"], None, None),
    (C["clin"], ["Call-off or PTO", "entered in Sync"],
     ["Reaches Sync instantly", "Needs a habit change"], None, None),
    (SYNC, ["Call-Off Center", "ranks by urgency"],
     ["Visit window, compliance", "Must-cover vs deferrable", "Due before year end"], "road", None),
    (C["pcc"], ["Reschedule or", "replace"],
     ["Productivity, drive, overtime", "Same cover across the days", "Nobody takes it: not shown"],
     None, None),
    (SYNC, ["RPA to HCHB, push", "to the covering clinician"],
     ["Seconds to minutes", "Bypasses the log-ship lag"], "road", None),
    (C["pcc"], ["Missed visit: notify", "the MD within 48 h"],
     ["HCHB hard stop today", "Task auto-clearing: roadmap"], "opp", None),
], breaks=(1,))

# ---------------------------------------------------------------- band-to-band connectors
def link(xfrom, cfrom, y_next, c_next, redge):
    conn(f"M {xfrom+BW} {cfrom} L {redge+18} {cfrom} L {redge+18} {y_next-20} L {BX-30} {y_next-20} "
         f"L {BX-30} {c_next}")
    arrow(BX-30, c_next, IX-6, c_next)
link(xA[-1], cA, BYY, cB, rA)
link(xB[-1], cB, CY, cC, rB)
link(xC[-1], cC, DY, cD, rC)
# D -> E is an exception, not the main path
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
    ("live", "AUTOMATED IN SYNC TODAY", [
        "Ranked provider matches per discipline (B)",
        "RPA write-back of assignments and moves (B, C)",
        "Better-day suggestions with reasons (C)",
        "Licence and certification alerts (C)",
        "Live routing and rerouting of the day (D)",
        "Reported-versus-tracked visit review (D)",
        "PTO pulled from the HR system (iSolved)",
    ]),
    ("road", "ON THE VITALIS ROADMAP", [
        "Call-Off Center — before year end (E)",
        "Auto-clearing HCHB scheduler tasks — weeks",
        "Enterprise capacity roll-up by branch",
        "Plotting visits into HCHB by write-back",
    ]),
    ("build", "GAPS VITALIS NAMED, NO DATE", [
        "Authorization and readiness as states (A)",
        "Episode, LUPA and recert pacing (C)",
        "Therapy productivity and sequencing",
        "Patient communication of any kind (D)",
    ]),
    ("opp", "OPEN OPPORTUNITIES FOR COMPASSUS", [
        "Accept or decline referrals on live capacity (A)",
        "Stream intake data to Sync, skip the log ship (A)",
        "Sync picks the SOC clinician, not just long-term (A)",
        "Tell the clinician why they got a patient (B)",
        "Two-way day-before confirmation and ETA text (D)",
        "Territory map that follows referral patterns",
        "Missed-visit MD notification chain (E)",
        "Faster HCHB data: subset script or DB mirror",
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
lbl(PX + 26, sy + 4, "The largest clinician time back is band D,", "start", "hi")
lbl(PX + 26, sy + 26, "and nobody has built it yet.", "start", "hi")
print("panel 1 content ends", sy + 26, "panel bottom", PY + P1H)

# ---------------------------------------------------------------- right panel: the data path
QY = PY + P1H + 30
QH = last_y - QY
panel(PX, QY, PW, QH, "THE DATA PATH — WHY BAND E NEEDS SYNC")
nx, nw, nh = PX + 30, 190, 56
row1 = QY + 70
block(nx, row1, nw, nh, C["hchb"], ["HCHB"], small=True)
block(nx + 300, row1, nw, nh, SYNC, ["Sync"], small=True)
block(nx + 600, row1, nw - 40, nh, C["hchb"], ["HCHB"], small=True)
arrow(nx + nw, row1 + nh/2, nx + 300 - 6, row1 + nh/2)
arrow(nx + 300 + nw, row1 + nh/2, nx + 600 - 6, row1 + nh/2)
lbl(nx + nw + 55, row1 + nh/2 - 10, "log ship", "middle", "lb")
lbl(nx + nw + 55, row1 + nh + 20, "~3 h today", "middle", "lb")
lbl(nx + 300 + nw + 55, row1 + nh/2 - 10, "RPA", "middle", "lb")
lbl(nx + 300 + nw + 55, row1 + nh + 20, "sec–min", "middle", "lb")
row2 = row1 + 130
block(nx, row2, nw, nh, C["clin"], ["Call-off in Sync"], small=True)
block(nx + 300, row2, nw, nh, SYNC, ["Call-Off Center"], small=True)
arrow(nx + nw, row2 + nh/2, nx + 300 - 6, row2 + nh/2)
lbl(nx + nw + 55, row2 + nh/2 - 10, "instant", "middle", "lb")
lbl(nx, row2 + nh + 40, "A call-off entered in PointCare or HCHB waits for the next log ship.", "start", "note")
lbl(nx, row2 + nh + 62, "Entered in Sync, it skips it — so the habit change is the fix,", "start", "note")
lbl(nx, row2 + nh + 84, "until Compassus speeds up the HCHB feed.", "start", "note")
print("panel 2 content ends", row2 + nh + 84, "panel bottom", QY + QH)

# ---------------------------------------------------------------- where it breaks
WY = last_y + 40
lbl(50, WY+34, "WHERE IT", cls="trg"); lbl(50, WY+52, "BREAKS", cls="trg")
brk = [(["HCHB data reaches Sync", "~3 h late at Compassus"], C["hchb"]),
       (["Schedulers redo changes in", "HCHB — double entry"], C["pcc"]),
       (["RPA write-back breaks when", "HCHB changes a screen"], SYNC),
       (["Clinicians carry Sync360", "and PointCare"], C["clin"]),
       (["Built for hospice — home", "health logic is ahead"], SYNC)]
wx = IX
for lines, col in brk:
    block(wx, WY+8, 470, 70, col, lines, small=True)
    wx += 490
print("last content y", WY + 78, "footer rule", H - 72)

footer("Vendor overlay · VitalisCare Sync as demoed 24 Sep 2026 · not current state and not a "
       "recommendation", "Overlay V1 · VitalisCare Sync")
finish(OUT)
