# -*- coding: utf-8 -*-
"""Flow V5 — all four vendors on the Start of Care flow. Vendor overlay, NOT current state.

The SOC / plan-of-care steps from Flow 1 (Start of Care — the Full Flow), with one lane per vendor
under every step. Each cell says what that vendor does at that step and where we know it from:
shown in the demo, claimed in the RFP return only, partly / roadmap, or not covered. Vendors run in
alphabetical order so no lane reads as a ranking. Canvas units = points on the output sheet.

    python3 _flow-vendor-soc-overlay.gen.py <out.svg>
"""
import sys, pathlib, json
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3] / ".claude/skills/process-flow-map/assets"))
from flowkit import *

OUT = sys.argv[1] if len(sys.argv) > 1 else "flow.svg"
DATA = json.load(open(pathlib.Path(__file__).with_name("_flow-vendor-soc-overlay.data.json")))

VENDORS = ["Arya", "Axle Health", "CareStitch", "VitalisCare"]
STATUS = {  # tag text, fill, stroke, dash, text colour
    "S": ("SHOWN IN DEMO",   "#FFFFFF", INK,       False, INK),
    "R": ("RFP RETURN ONLY", "#FFFFFF", INK,       True,  INK),
    "P": ("PARTLY / ROADMAP", "#FFF6DA", "#B8900F", True,  "#5A4300"),
    "N": ("NOT COVERED",     "#EFEFEC", "#EFEFEC", False, MUT),
}

W, H = 2900, 1830
LX = 50                    # vendor label column
X0 = 300                   # first step column
CW = (W - 50 - X0) / 7     # column pitch
BWS = CW - 24              # block / cell width
LH = 100                   # lane height
CH = 92                    # cell height

def cell(x, y, st, lines):
    tag_t, fill, stroke, dash, tc = STATUS[st]
    d = ' stroke-dasharray="6 4"' if dash else ''
    add(f'<rect x="{x}" y="{y}" width="{BWS}" height="{CH}" rx="6" fill="{fill}" stroke="{stroke}" '
        f'stroke-width="1.6"{d}/>')
    add(f'<text x="{x+10}" y="{y+19}" class="bdg" style="fill:{tc}">{esc(tag_t)}</text>')
    for i, ln in enumerate(lines[:3]):
        add(f'<text x="{x+10}" y="{y+42+i*19}" class="sub" style="fill:{tc};font-size:15.5px">{esc(ln)}</text>')

def tier(y, title, right, steps, key):
    """steps: (colour | (left, right), lines). key: DATA section. Returns bottom y."""
    top = y
    bh = 60 + BH + 26 + 4*LH + 10
    add(f'<rect x="{X0-22}" y="{top}" width="{W-50-(X0-22)}" height="{bh}" rx="10" fill="{BAND}"/>')
    lbl(X0-4, top+34, title, cls="band")
    lbl(W-64, top+34, right, "end", "bandhi")
    by = top + 56
    cy = by + BH/2
    for i, (fill, lines) in enumerate(steps):
        x = X0 + i*CW
        if isinstance(fill, tuple):
            split_block(x, by, BWS, BH, fill[0], fill[1], lines)
        else:
            block(x, by, BWS, BH, fill, lines)
        if i:
            arrow(x - 24, cy, x - 6, cy)
    ly = by + BH + 26
    for v, name in enumerate(VENDORS):
        yy = ly + v*LH
        lbl(LX, yy + CH/2 + 6, name, cls="colh")
        add(f'<line x1="{LX}" y1="{yy+CH+4}" x2="{X0-40}" y2="{yy+CH+4}" stroke="{RULE}" stroke-width="1"/>')
        for i in range(len(steps)):
            st, txt = DATA[key][i][name]
            cell(X0 + i*CW, yy, st, txt)
    return top + bh, cy

begin(W, H, aria=(
    "All four vendors placed on the Compassus Start of Care flow. Two tiers follow Flow 1: pass 1 from "
    "referral to the SOC and eval visits, and pass 2 from the discipline plan of care to visits on the "
    "calendar, the episode budget and missed visits. Under every step, one lane per vendor (Arya, Axle "
    "Health, CareStitch, VitalisCare, alphabetical) says what the vendor does there and whether it was "
    "shown in the demo, claimed only in the RFP return, partly built or on the roadmap, or not covered."))
masthead("COMPASSUS HOME HEALTH  ·  VENDOR OVERLAY V5",
         "Four Vendors on the Start of Care Flow",
         "The Flow 1 steps, with what each vendor does at each one and how we know: shown in its demo, "
         "claimed in its RFP return, partly built, or not covered")
legend([("Intake", C["intake"]), ("Insurance & Auth", C["auth"]), ("DCS", C["dcs"]),
        ("PCC / Scheduler", C["pcc"]), ("Clinician", C["clin"]), ("Patient", C["pat"]),
        ("Branch Leadership", C["lead"]), ("HCHB", C["hchb"])], x=1560, cy=56, per_row=4, gap=30)

KY = 190
lbl(50, KY+6, "HOW WE KNOW", cls="trg")
kx = 300
for st, desc in [("S", "seen working on the call"), ("R", "described in the vendor’s own return, not demonstrated"),
                 ("P", "part of it built, or named as roadmap"), ("N", "not in the demo or the return")]:
    tag_t, fill, stroke, dash, tc = STATUS[st]
    d = ' stroke-dasharray="6 4"' if dash else ''
    bw = 8.3*len(tag_t) + 22
    add(f'<rect x="{kx}" y="{KY-12}" width="{bw}" height="26" rx="6" fill="{fill}" stroke="{stroke}" stroke-width="1.6"{d}/>')
    add(f'<text x="{kx+11}" y="{KY+6}" class="bdg" style="fill:{tc}">{esc(tag_t)}</text>')
    lbl(kx + bw + 12, KY+6, desc, cls="note")
    kx += bw + 12 + 7.0*len(desc) + 46

P1 = [
    (C["intake"], ["Intake receives", "referral in Commure"]),
    (C["auth"], ["Auth verifies", "eligibility, keys", "pending auth"]),
    ((C["intake"], C["lead"]), ["Final approval:", "accept or decline"]),
    (C["dcs"], ["DCS reviews", "referral"]),
    (C["pcc"], ["Welcome / intake", "call: is the", "patient home?"]),
    (C["pcc"], ["Book SOC / ROC", "+ discipline evals"]),
    (C["clin"], ["Clinicians perform", "SOC / ROC + evals"]),
]
P2 = [
    (C["dcs"], ["Plans of care", "approved · 485", "all at once"]),
    (C["hchb"], ["Visits generate", "in HCHB"]),
    (C["auth"], ["Auth on file?", "Pending: off the", "calendar"]),
    (C["pcc"], ["Scheduler plots all", "visits · one pass"]),
    ((C["clin"], C["pat"]), ["Day before: visit", "confirmed with", "the patient"]),
    (C["dcs"], ["Episode budget:", "LUPA floor, use", "ceiling"]),
    (C["clin"], ["Missed visit:", "MD notified", "within 48 h"]),
]
b1, c1 = tier(235, "PASS 1  ·  START OF CARE / RESUMPTION OF CARE — from the referral",
              "NOTHING SCHEDULES UNTIL AUTH AND INTAKE CLEAR", P1, "pass1")
chip(50, 291 + BH/2 - 30, 200, 60, ["Referral arrives"], INK)
arrow(250, c1, X0-6, c1)
b2, c2 = tier(b1 + 44, "PASS 2  ·  DISCIPLINE PLAN OF CARE — through to the calendar",
              "×  N DISCIPLINES · EACH GATE FIRES ONCE PER DISCIPLINE", P2, "pass2")
conn(f"M {X0+6*CW+BWS} {c1} L {W-36} {c1} L {W-36} {b1+22} L {X0-40} {b1+22} L {X0-40} {c2}")
arrow(X0-40, c2, X0-6, c2)

# tally row: count of steps per status, per vendor
TY = b2 + 40
lbl(50, TY+22, "ACROSS THE", cls="trg"); lbl(50, TY+40, "14 STEPS", cls="trg")
tx = X0
for name in VENDORS:
    cnt = {k: 0 for k in STATUS}
    for sec in ("pass1", "pass2"):
        for col in DATA[sec]:
            cnt[col[name][0]] += 1
    lbl(tx, TY+20, name, cls="colh")
    lbl(tx, TY+44, f"{cnt['S']} shown  ·  {cnt['R']} RFP only  ·  {cnt['P']} partly  ·  {cnt['N']} not covered",
        cls="note")
    tx += (W - 50 - X0) / 4
# reading panel: plain facts across vendors, no ranking
RY = TY + 80
RH = H - 72 - 30 - RY
panel(50, RY, W - 100, RH, "READING THE SHEET — WHAT THE FOUR HAVE IN COMMON AND WHERE THEY SPLIT")
notes = [
    ("No vendor touches", ["DCS referral review, plan-of-care approval and", "the 485, or SOC documentation. These stay", "with people in HCHB and PointCare."]),
    ("Accept or decline", ["Axle and CareStitch showed a capacity read.", "Arya and VitalisCare describe one in their", "returns; neither showed it on the call."]),
    ("The day before", ["Arya and Axle texted the patient live.", "CareStitch has click-to-call, text on roadmap.", "VitalisCare has no patient messaging."]),
    ("The episode budget", ["No vendor showed LUPA pacing. Recert,", "front-loading and pacing are partial or", "left to the scheduler in all four."]),
]
nw = (W - 100 - 60) / 4
for i, (head, lines) in enumerate(notes):
    nx = 80 + i * nw
    lbl(nx, RY + 76, head, cls="colh")
    for j, ln in enumerate(lines):
        lbl(nx, RY + 104 + j * 22, ln, cls="note")
print("tally y", TY + 44, "panel", RY, RY + RH, "footer rule", H - 72)

footer("Vendor overlay · four vendors on Flow 1 · demos 22–28 Sep 2026 and RFP returns · not current state, "
       "not a ranking and not a recommendation", "Overlay V5 · SOC, four vendors")
finish(OUT)
