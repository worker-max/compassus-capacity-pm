# -*- coding: utf-8 -*-
"""Flow V4 — Arya overlay. Vendor overlay, NOT current state.

The Compassus episode as mapped in the current-state set, with Arya placed where it would sit as
demoed on 28 Sep 2026, and each step badged for automation: in Arya today, Citrix screen automation
(the HCHB integration), promised but not shown, or an open opportunity for Compassus. Same vendor
colour as V1-V3.
Canvas units = points on the output sheet.

    python3 _flow-vendor-arya.gen.py <out.svg>
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3] / ".claude/skills/process-flow-map/assets"))
from flowkit import *

SYNC = "#A33A6B"                     # the vendor system acting by itself (same slot on every overlay)
OUT = sys.argv[1] if len(sys.argv) > 1 else "flow.svg"

KIND = {  # automation badge: text, fill, stroke, text colour, dashed
    "live":  ("IN ARYA TODAY",   INK,       INK,       "#FFFFFF", False),
    "road":  ("CLAIMED, NOT SHOWN", "#FFFFFF", INK,     INK,       True),
    "build": ("CITRIX RPA",      "#FFFFFF", C["auth"], "#B4520F", False),
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
    "Vendor overlay of Arya on the Compassus home health episode, as demoed on 28 September 2026. "
    "Five bands: referral to admission, where Arya texts the patient to confirm discharge and the "
    "capacity check was promised but not shown; which clinician, where guardrails filter, Arya ranks "
    "clinicians with a match score and a suggested time, the office approves and part-timers accept by "
    "text; which day, where each visit gets a capacity window and Arya writes back to HCHB by Citrix "
    "screen automation; the day before and the day of, where the clinician works by text and short "
    "links; and when the day breaks, where a call-out is one text and the agent moves or re-staffs the "
    "visits. A right-hand panel lists what is live, screen automation, promised and open."))
masthead("COMPASSUS HOME HEALTH  ·  VENDOR OVERLAY V4",
         "Arya on the Compassus Episode",
         "Where Arya would sit in our flow as demoed on 28 Sep 2026, and where automation is live, "
         "screen-automated, claimed or still open (demo plus RFP return)")
legend([("Intake", C["intake"]), ("Insurance & Auth", C["auth"]), ("PCC / Scheduler", C["pcc"]),
        ("Clinician", C["clin"]), ("Patient", C["pat"]), ("Branch Leadership", C["lead"]),
        ("HCHB", C["hchb"]), ("Arya", SYNC)], x=1500, cy=56, per_row=4, gap=30)

# automation key
KY = 188
lbl(50, KY+6, "AUTOMATION", cls="trg")
kx = 320
for kind, desc in [("live", "demonstrated in software"), ("build", "HCHB by screen automation"),
                   ("road", "in the RFP return or on the call, not demonstrated"), ("opp", "not built · ours to push")]:
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
rA = band(AY, AH, "A  ·  REFERRAL TO ADMISSION", "THE AGENT TEXTS THE PATIENT FIRST", slots=5)
chip(50, AY+60+BH/2-39, 250, 78, ["Referral arrives"], INK)
lbl(50, AY+60+BH/2-53, "TRIGGER", cls="trg")
arrow(300, AY+60+BH/2, IX-6, AY+60+BH/2)
cA, xA = steps_row(AY+60, [
    (C["intake"], ["Referral validated", "in intake platform"],
     ["Arya to read it here,", "not from HCHB", "Agreed on the call"],
     "opp", None),
    ((C["lead"], SYNC), ["Accept or decline:", "is there capacity?"],
     ["RFP: SOC-eligible staff with", "room, and episode impact", "Demo: “no good data”"],
     "road", None),
    (C["auth"], ["Verify eligibility,", "key pending auth"],
     ["RFP: blocked until auth clears,", "then moves to scheduling", "“Put in review” holds slot"],
     "live", None),
    (SYNC, ["Texts the patient:", "discharged yet?"],
     ["Reply sets the SOC window", "Preferences captured", "Spanish text and voice (claim)"],
     "live", None),
    (C["clin"], ["SOC and evals; each", "discipline writes", "its frequency"],
     ["Written in HCHB", "Read back by Arya", "Booked ahead in auth window"],
     None, "× N disciplines"),
])

# ---------------------------------------------------------------- data boundary
BY = AY + AH + 30
add(f'<line x1="{BX}" y1="{BY+24}" x2="{IX+230}" y2="{BY+24}" stroke="{C["hchb"]}" '
    'stroke-width="2.5" stroke-dasharray="14 7"/>')
add(f'<line x1="{IX+1300}" y1="{BY+24}" x2="{rA}" y2="{BY+24}" stroke="{C["hchb"]}" '
    'stroke-width="2.5" stroke-dasharray="14 7"/>')
add(f'<rect x="{IX+240}" y="{BY+4}" width="1050" height="40" rx="20" fill="{PAPER}" '
    f'stroke="{C["hchb"]}" stroke-width="2"/>')
lbl(IX+765, BY+30, "HCHB ⇄ ARYA: CITRIX SCREEN AUTOMATION  ·  READS 15–20 MIN  ·  WRITES ~15 MIN",
    "middle", "boundary")
lbl(50, BY+30, "DATA IN / OUT", cls="trg")

# ---------------------------------------------------------------- B  which clinician
BYY, BHH = BY + 70, 262
rB = band(BYY, BHH, "B  ·  WHICH CLINICIAN", "ARYA RANKS · THE OFFICE APPROVES", slots=5)
cB, xB = steps_row(BYY+60, [
    (SYNC, ["Guardrails filter", "who is eligible"],
     ["Licensure, on-call, PTO", "Max travel, point ceiling", "Set per branch"], "live", None),
    (SYNC, ["Ranks by match %", "with a suggested time"],
     ["Least drive time for the day", "Full-time first, continuity", "Reasons shown"], "live", None),
    (C["pcc"], ["Office approves", "(co-pilot mode)"],
     ["Accept, review or reject", "A typed reason becomes a rule", "Later: informed, not asked"], None, None),
    (C["clin"], ["Part-timer accepts", "by text link"],
     ["Full-time: assigned directly", "Nothing lands without a yes", "unless we set it to"], "live", None),
    (SYNC, ["Batched outreach,", "best fit first"],
     ["Texts or calls the eligible", "Next batch if no one", "Voice outbound not shown"], "live", None),
])

# ---------------------------------------------------------------- C  which day
CY, CH = BYY + BHH + 40, 300
rC = band(CY, CH, "C  ·  WHICH DAY — THE EPISODE", "CAPACITY WINDOWS, NOT EPISODE RULES", slots=5)
cC, xC = steps_row(CY+60, [
    (C["hchb"], ["Frequency held", "in HCHB"],
     ["Orders stay in HCHB", "Arya reads them"], None, None),
    (SYNC, ["Capacity window", "set for each visit"],
     ["SOC: 24 h from discharge", "Recurring: Medicare week", "RFP: guards fixed-day visits"], "live", None),
    (SYNC, ["Books visits ahead", "inside the auth"],
     ["RFP: reads auth, frequency", "and windows from HCHB", "Up to a month out (call)"], "road", None),
    (SYNC, ["LUPA, recert and", "front-loading logic"],
     ["Never came up", "Ours to specify"], "opp", None),
    (SYNC, ["Writes SOC and", "visits back to HCHB"],
     ["Shown on a mock HCHB", "RFP: <5 min · call: 15–20", "Live since mid-2025 (RFP)"], "build", None),
])
lbl(IX, CY+CH-16, "Arya fits each visit inside its window on the clinician’s calendar. Episode economics "
    "(LUPA, recert, front-loading) were never discussed.", "start", "hi")

# ---------------------------------------------------------------- D  day before / day of
DY, DH = CY + CH + 40, 262
rD = band(DY, DH, "D  ·  THE DAY BEFORE AND THE DAY OF", "THE CLINICIAN WORKS BY TEXT", slots=6)
cD, xD = steps_row(DY+60, [
    (SYNC, ["Preferences set", "at onboarding"],
     ["Days, times, regions", "Code by text, no password", "Re-checked every 2 weeks"], "live", None),
    (SYNC, ["Next-day route", "by short link"],
     ["Drive and patient time", "Start time adjustable", "Navigate and share"], "live", None),
    (SYNC, ["Tells the patient", "the arrival time"],
     ["From Arya or the", "clinician’s own phone", "Compassus number possible"], "live", None),
    (C["pat"], ["Patient replies", "or asks to move"],
     ["Two-way text live", "Preference noted", "Call-back cadence set"], "live", None),
    (C["clin"], ["Visits documented", "in PointCare / HCHB"],
     ["Arya holds the plan", "HCHB holds the record"], None, None),
    (SYNC, ["Voice line for", "clinicians"],
     ["Call in to change the day", "Completed after the call", "Offered as a follow-up"], "road", None),
])

# ---------------------------------------------------------------- E  exceptions
EY, EH = DY + DH + 40, 262
rE = band(EY, EH, "E  ·  WHEN THE DAY BREAKS", "ONE TEXT, THEN THE AGENT", slots=6)
cE, xE = steps_row(EY+60, [
    (C["clin"], ["Call-out", "by text"],
     ["“I can’t work Wednesday”"], None, None),
    (SYNC, ["Moves visits within", "the same week"],
     ["Inside each window", "Asks what to keep"], "live", None),
    (SYNC, ["Re-staffs what", "it can’t move"],
     ["Batched outreach", "Applicants ranked"], "live", None),
    (C["pcc"], ["Office gets only", "the critical items"],
     ["Teams, text or email", "“No one available”"], None, None),
    (SYNC, ["Offers an incentive", "for a hard visit"],
     ["Bonus or extra points", "“Negotiation scale”"], "road", None),
    (SYNC, ["Learns from", "every no"],
     ["Rejection breakdown", "Agent-health funnel"], "live", None),
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
    ("live", "IN ARYA TODAY", [
        "Discharge check by text to the patient (A)",
        "Ranked clinicians with a suggested time (B)",
        "Part-timer acceptance by text (B)",
        "Preferences and next-day route by link (D)",
        "Call-out handled by text (E)",
        "Rejection learning, insights, agent health (E)",
    ]),
    ("build", "CITRIX SCREEN AUTOMATION", [
        "Call: reads 15–20 min, writes ~15 min (C)",
        "RFP return: under 5 min; SSO logouts a risk",
    ]),
    ("road", "CLAIMED, NOT SHOWN", [
        "Referral-level capacity check (A · RFP)",
        "Clinician capacity rolled up by branch (RFP)",
        "Voice agents, in and out (D)",
        "Incentive negotiation (E)",
        "View of the learned rules (“the brain”)",
    ]),
    ("opp", "OPEN OPPORTUNITIES FOR COMPASSUS", [
        "Read from our intake platform (A)",
        "LUPA, recert and front-loading logic (C)",
        "Approval kept on, per action (B)",
        "Governance of learned rules",
        "Referral and discharge forecast (in neither)",
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
lbl(PX + 26, sy + 4, "The loop runs end to end.", "start", "hi")
lbl(PX + 26, sy + 26, "The rails are what to test.", "start", "hi")
print("panel 1 content ends", sy + 26, "panel bottom", PY + P1H)

# ---------------------------------------------------------------- right panel: the agent loop
QY = PY + P1H + 30
QH = last_y - QY
panel(PX, QY, PW, QH, "THE AGENT LOOP — THE STANDOUT")
nx, nw, nh = PX + 30, 170, 56
row1 = QY + 74
block(nx, row1, nw, nh, C["intake"], ["Referral in"], small=True)
block(nx + 250, row1, nw, nh, SYNC, ["Texts patient"], small=True)
block(nx + 500, row1, nw, nh, SYNC, ["Ranks + time"], small=True)
arrow(nx + nw, row1 + nh/2, nx + 250 - 6, row1 + nh/2)
arrow(nx + 250 + nw, row1 + nh/2, nx + 500 - 6, row1 + nh/2)
row2 = row1 + 110
block(nx, row2, nw, nh, C["pcc"], ["Office approves"], small=True)
block(nx + 250, row2, nw, nh, C["clin"], ["Clinician: yes"], small=True)
block(nx + 500, row2, nw, nh, C["hchb"], ["SOC in HCHB"], small=True)
conn(f"M {nx+500+nw/2} {row1+nh} L {nx+500+nw/2} {row1+nh+27} L {nx+nw/2} {row1+nh+27} L {nx+nw/2} {row2-6}")
arrow(nx + nw, row2 + nh/2, nx + 250 - 6, row2 + nh/2)
arrow(nx + 250 + nw, row2 + nh/2, nx + 500 - 6, row2 + nh/2)
lbl(nx, row2 + nh + 56, "The only vendor to run referral, patient, clinician and HCHB", "start", "note")
lbl(nx, row2 + nh + 78, "write-back as one live sequence. Every rejection reason feeds", "start", "note")
lbl(nx, row2 + nh + 100, "the rules the agent uses next time.", "start", "note")
print("panel 2 content ends", row2 + nh + 100, "panel bottom", QY + QH)

# ---------------------------------------------------------------- where it breaks
WY = last_y + 40
lbl(50, WY+34, "WHERE IT", cls="trg"); lbl(50, WY+52, "BREAKS", cls="trg")
brk = [(["HCHB by screen automation", "— 15–20 min, SSO logouts"], C["hchb"]),
       (["Capacity: in the RFP,", "not in the demo"], C["lead"]),
       (["Learned rules with no", "view or approval yet"], SYNC),
       (["Approval framed as a", "phase, not a setting"], C["pcc"]),
       (["No LUPA, recert or", "front-loading logic"], C["clin"])]
wx = IX
for lines, col in brk:
    block(wx, WY+8, 470, 70, col, lines, small=True)
    wx += 490
print("last content y", WY + 78, "footer rule", H - 72)

footer("Vendor overlay · Arya as demoed 28 Sep 2026 · not current state and not a "
       "recommendation", "Overlay V4 · Arya")
finish(OUT)
