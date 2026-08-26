# -*- coding: utf-8 -*-
"""Flow 2 — Routine Visit Scheduling. Canvas units = points on the output sheet."""

C = dict(pcc="#C6A01F", hchb="#795CA7", dcs="#792E2E", clin="#2E599D",
         auth="#DF751D", intake="#1F6F78", lead="#1A1A1A")
INK, MUT, RULE, BAND = "#1B211E", "#5A6560", "#C9CCC5", "#E9E9E5"

out = []
def add(s): out.append(s)
def esc(t): return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

SHOW_VCHIPS = False          # off until the variable IDs are settled
BW, BH, GAP = 250, 90, 28
CHH = 27 if SHOW_VCHIPS else 0
EXW, EXH = 250, 78

def block(x, y, w, h, fill, lines, small=False, badge=None, tc="#fff", bc=None):
    add(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="5" fill="{fill}"/>')
    lh = 15.5 if small else 19
    cls = "bt s" if small else "bt"
    cy = y + h/2 - (len(lines)-1)*lh/2 + (5 if small else 6)
    for i, ln in enumerate(lines):
        add(f'<text x="{x+w/2}" y="{cy+i*lh}" class="{cls}" style="fill:{tc}" text-anchor="middle">{esc(ln)}</text>')
    if badge:
        bw = 8.3*len(badge)+18
        add(f'<rect x="{x+w-bw-8}" y="{y-14}" width="{bw}" height="23" rx="11.5" fill="#FFFFFF" '
            f'stroke="{bc or fill}" stroke-width="1.8"/>')
        add(f'<text x="{x+w-bw/2-8}" y="{y+2}" class="bdg" text-anchor="middle" fill="{bc or fill}">{esc(badge)}</text>')


# ================= TARGET-STATE POSTURE VOCABULARY =================
PAPER = "#FBFBF8"
ENG, ENGD = "#A6E22E", "#5F8A12"     # the capacity & scheduling engine; dark green for its badges

def xref(x, y, n):
    w = 8.3*len(str(n))+16
    add(f'<rect x="{x+8}" y="{y-14}" width="{w}" height="22" rx="5" fill="#FFFFFF" '
        f'stroke="{MUT}" stroke-width="1.3"/>')
    add(f'<text x="{x+8+w/2}" y="{y+1}" class="bdg" text-anchor="middle" fill="{MUT}">{esc(str(n))}</text>')

def eng(x, y, w, h, lines, small=False, badge=None, n=None):
    """AUTOMATE — the engine does it."""
    block(x, y, w, h, ENG, lines, small=small, badge=badge, tc=INK, bc=ENGD)
    if n: xref(x, y, n)

def assist(x, y, w, h, person, lines, small=False, badge=None, n=None):
    """ASSIST — the engine proposes, the named person confirms."""
    BAR = 52
    add(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="5" fill="{ENG}"/>')
    add(f'<path d="M {x+w-BAR} {y} L {x+w-6} {y} A 6 6 0 0 1 {x+w} {y+6} L {x+w} {y+h-6} '
        f'A 6 6 0 0 1 {x+w-6} {y+h} L {x+w-BAR} {y+h} Z" fill="{person}"/>')
    lh = 15.5 if small else 19
    cls = "bt s" if small else "bt"
    cy = y + h/2 - (len(lines)-1)*lh/2 + (5 if small else 6)
    for i, ln in enumerate(lines):
        add(f'<text x="{x+(w-BAR)/2}" y="{cy+i*lh}" class="{cls}" style="fill:{INK}" '
            f'text-anchor="middle">{esc(ln)}</text>')
    if badge:
        bw = 8.3*len(badge)+18
        add(f'<rect x="{x+w-bw-8}" y="{y-14}" width="{bw}" height="23" rx="11.5" fill="#FFFFFF" '
            f'stroke="{person}" stroke-width="1.8"/>')
        add(f'<text x="{x+w-bw/2-8}" y="{y+2}" class="bdg" text-anchor="middle" fill="{person}">{esc(badge)}</text>')
    if n: xref(x, y, n)

def surf(x, y, w, h, person, lines, small=False, badge=None, n=None):
    """SURFACE — the engine shows it, the person decides."""
    block(x, y, w, h, person, lines, small=small)
    add(f'<path d="M {x+6} {y} L {x+w-6} {y} A 6 6 0 0 1 {x+w} {y+6} L {x+w} {y+13} '
        f'L {x} {y+13} L {x} {y+6} A 6 6 0 0 1 {x+6} {y} Z" fill="{ENG}"/>')
    if badge:
        bw = 8.3*len(badge)+18
        add(f'<rect x="{x+w-bw-8}" y="{y-14}" width="{bw}" height="23" rx="11.5" fill="#FFFFFF" '
            f'stroke="{person}" stroke-width="1.8"/>')
        add(f'<text x="{x+w-bw/2-8}" y="{y+2}" class="bdg" text-anchor="middle" fill="{person}">{esc(badge)}</text>')
    if n: xref(x, y, n)

def man(x, y, w, h, person, lines, small=False, badge=None, n=None):
    """Unchanged — a person, or still inside HCHB."""
    block(x, y, w, h, person, lines, small=small, badge=badge)
    if n: xref(x, y, n)

def ghost(x, y, w, h, lines, n=None, label="NO LONGER A STEP", above=False):
    """A step that no longer exists — it keeps its footprint, the flow runs past it."""
    add(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="5" fill="{PAPER}" '
        f'stroke="{MUT}" stroke-width="1.7" stroke-dasharray="7 5" opacity=".8"/>')
    cy = y + h/2 - (len(lines)-1)*16/2 + 5
    for i, ln in enumerate(lines):
        add(f'<text x="{x+w/2}" y="{cy+i*16}" class="bt s" style="fill:{MUT}" '
            f'text-anchor="middle" opacity=".85">{esc(ln)}</text>')
        wl = 7.0*len(ln)
        add(f'<line x1="{x+w/2-wl/2}" y1="{cy+i*16-5}" x2="{x+w/2+wl/2}" y2="{cy+i*16-5}" '
            f'stroke="{MUT}" stroke-width="1.2" opacity=".8"/>')
    if label: lbl(x+w/2, y+h+18 if not above else y-20, label, "middle", "trg")
    if n: xref(x, y, n)

def vchip(x, y, w, ids):
    """light variable chip under a block"""
    if not SHOW_VCHIPS or not ids: return
    add(f'<rect x="{x}" y="{y}" width="{w}" height="{CHH}" rx="6" fill="#FFFFFF" '
        f'stroke="{RULE}" stroke-width="1.3"/>')
    add(f'<text x="{x+w/2}" y="{y+18.5}" class="vid" text-anchor="middle">{esc(" · ".join(ids))}</text>')

def sublist(x, y, w, items):
    for i, t in enumerate(items):
        add(f'<text x="{x+6}" y="{y+i*17}" class="sub">{esc("·  " + t)}</text>')

def chip(x, y, w, h, lines, stroke, fill="#FFFFFF"):
    add(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{min(h/2,26)}" fill="{fill}" '
        f'stroke="{stroke}" stroke-width="1.8"/>')
    y0 = y + h/2 - (len(lines)-1)*17/2 + 5
    for i, ln in enumerate(lines):
        add(f'<text x="{x+w/2}" y="{y0+i*17}" class="ct" text-anchor="middle" fill="{stroke}">{esc(ln)}</text>')

def arrow(x1, y1, x2, y2, dash=False):
    d = ' stroke-dasharray="7 5" opacity=".68"' if dash else ''
    add(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" class="ln"{d} marker-end="url(#ar)"/>')

def conn(dd):
    add(f'<path d="{dd}" fill="none" class="ln"/>')

def path(dd, dash=False):
    d = ' stroke-dasharray="7 5" opacity=".68"' if dash else ''
    add(f'<path d="{dd}" fill="none" class="ln"{d} marker-end="url(#ar)"/>')

def lbl(x, y, t, anchor="start", cls="lb"):
    add(f'<text x="{x}" y="{y}" class="{cls}" text-anchor="{anchor}">{esc(t)}</text>')

W, H = 2200, 1680
add(f'<svg viewBox="0 0 {W} {H}" role="img" xmlns="http://www.w3.org/2000/svg" '
    'aria-label="Routine visit scheduling in two phases. Phase one is a burst of scheduler work at '
    'admission: each discipline plots its own frequency, every submission generates its own '
    'assignment task, and the DCS approves each discipline plan of care — not approved, the visits '
    'are held. After the 485 the episode enters phase two, where the clinician manages their '
    'own week with no scheduler workflow at all. After the 485 every change arrives as a physician '
    'order — which may add a discipline evaluation, change frequency or reduce visits. The day before each visit the clinician confirms '
    'with the patient and then picks one of five dispositions in HCHB: accept, reschedule, '
    'reassign, miss or decline.">')
add('<defs><marker id="ar" viewBox="0 0 10 8" refX="9" refY="4" markerWidth="8" markerHeight="6.5" '
    f'orient="auto-start-reverse"><polygon points="0,0 10,4 0,8" fill="{INK}"/></marker></defs>')
add(f'<rect x="0" y="0" width="{W}" height="{H}" fill="#FBFBF8"/>')

# masthead
lbl(50, 58, "COMPASSUS HOME HEALTH  ·  FLOW 2 — TARGET STATE  ·  v1.0", cls="eyebrow")
lbl(50, 100, "Routine Visit Scheduling", cls="title")
lbl(50, 128, "Read beside Flow-Routine-Visits — same blocks, same positions. A dashed, struck-through block is a step that no longer exists",
    cls="deck")
lx = 1080
for name, col in [("DCS", C["dcs"]), ("PCC / Scheduler", C["pcc"]),
                  ("Clinician", C["clin"]), ("HCHB", C["hchb"]),
                  ("Capacity & Scheduling Engine", ENG)]:
    add(f'<circle cx="{lx+13}" cy="72" r="13" fill="{col}"/>')
    lbl(lx+34, 78, name, cls="leg")
    lx += 34 + 8.4*len(name) + 40
add(f'<line x1="50" y1="150" x2="{W-50}" y2="150" stroke="{RULE}" stroke-width="1.4"/>')

BX, IX = 320, 350
PH = 205
PH2 = 268

# ---------------- PHASE ONE ----------------
P1Y = 185
p1 = [IX + i*(BW+GAP) for i in range(5)]
add(f'<rect x="{BX}" y="{P1Y}" width="{5*(BW+GAP)+30}" height="{PH}" rx="10" fill="{BAND}"/>')
lbl(BX+22, P1Y+34, "PHASE 1  ·  FREQUENCY PLOTTING & INITIAL ASSIGNMENT — the burst", cls="band")
b1 = P1Y + 60
c1 = b1 + BH/2
surf(p1[0], b1, BW, BH, C["clin"], ["Evaluating clinician", "plots own discipline", "frequency"],
     badge="× N disciplines", n="1")
man(p1[1], b1, BW, BH, C["clin"], ["RN also plots aide", "frequency + MSW / ST", "initial eval"], n="2")
ghost(p1[2], b1, BW, BH, ["Each submission", "generates its own", "assignment task"], n="3", label="")
man(p1[3], b1, BW, BH, C["dcs"], ["DCS reviews &", "approves the POC"],
    badge="× N disciplines", n="4")
assist(p1[4], b1, BW, BH, C["pcc"], ["Scheduler assigns", "visits to care team"], badge="ASSIST", n="5")
vchip(p1[0], b1+BH+9, BW, ["S-01", "S-02", "S-03"])
vchip(p1[1], b1+BH+9, BW, ["SH-03", "S-37"])
vchip(p1[4], b1+BH+9, BW, ["S-15", "S-16", "S-22"])
arrow(p1[0]+BW, c1, p1[1]-6, c1)
arrow(p1[3]+BW, c1, p1[4]-6, c1)
# the care team is set at referral (DE-05), so the per-discipline task is gone — run past it
BYY = b1 + BH + 16
add(f'<path d="M {p1[1]+BW} {c1} L {p1[1]+BW+12} {c1} L {p1[1]+BW+12} {BYY} L {p1[3]-12} {BYY} '
    f'L {p1[3]-12} {c1}" fill="none" class="ln"/>')
arrow(p1[3]-12, c1, p1[3]-6, c1)
chip(50, c1-39, 250, 78, ["Admission", "SOC or eval visit"], INK)
arrow(300, c1, IX-6, c1)
lbl(50, c1-53, "TRIGGER", cls="trg")
lbl(p1[0], b1+BH+CHH+46, "RN at the SOC; PT and OT at their own evals, 1–2 days later",
    "start", "note")
lbl(p1[3]+BW/2, b1+BH+CHH+46, "one approval per discipline; not approved → visits held",
    "middle", "note")

# ---------------- 485 boundary ----------------
BY = P1Y + PH + 46
add(f'<line x1="{BX}" y1="{BY+26}" x2="{IX-14}" y2="{BY+26}" stroke="{INK}" '
    'stroke-width="2.5" stroke-dasharray="14 7"/>')
add(f'<line x1="{IX+494}" y1="{BY+26}" x2="{BX+6*(BW+GAP)+30}" y2="{BY+26}" stroke="{INK}" '
    'stroke-width="2.5" stroke-dasharray="14 7"/>')
add(f'<rect x="{IX}" y="{BY+6}" width="480" height="40" rx="20" fill="#FBFBF8" stroke="{INK}" stroke-width="2"/>')
lbl(IX+240, BY+32, "485 SUBMITTED — changes come by physician order", "middle", "boundary")
lbl(IX+240, BY+64, "a physician order may add a discipline evaluation, change the frequency, "
    "or reduce the visits", "middle", "note")
lbl(IX+240, BY+84, "every one routes through DCS approval and auth before reaching the scheduler",
    "middle", "note")

# ---------------- PHASE TWO ----------------
P2Y = BY + 110
p2 = [IX + i*(BW+GAP) for i in range(6)]
add(f'<rect x="{BX}" y="{P2Y}" width="{6*(BW+GAP)+30}" height="{PH2}" rx="10" fill="{BAND}"/>')
lbl(BX+22, P2Y+34, "PHASE 2  ·  STEADY STATE — the clinician runs their own week", cls="band")
lbl(BX+6*(BW+GAP)+8, P2Y+34, "NO SCHEDULER WORKFLOW", "end", "bandhi")
b2 = P2Y + 60
c2 = b2 + BH/2
steps = [
    (["Evaluate own", "capacity for", "the week"],
     ["Points already committed", "Days off · PTO · on-call", "Documentation still owed"]),
    (["Prioritise clinical", "need across", "the caseload"],
     ["Who is unstable", "Wound · IV · catheter due", "Labs due", "Who can safely wait"]),
    (["Group visits", "geographically"],
     ["Who sits near whom", "Drive time, not distance", "Bridges · rivers · crossings", "Where the day starts"]),
    (["Test against hard", "constraints"],
     ["Wound care timing", "Catheter and IV schedules", "Caregiver must be present", "Dialysis · MD appointments"]),
    (["Confirmation — clinician", "directs, engine calls"],
     ["\u201cCan you come later?\u201d", "\u201cNot Mondays\u201d", "Patient not home", "\u2192 see the panel below"]),
    (["Route — HCHB suggests,", "clinician adjusts"],
     ["The suggested route", "Patient time windows", "Traffic and time of day", "Where the day must end"]),
]
POSTURE = [("eng", None, None), ("surf", C["clin"], None), ("eng", None, None),
           ("surf", C["clin"], None), ("assist", C["clin"], "CLINICIAN-TRIGGERED"),
           ("eng", None, None)]
for i, (lines, items) in enumerate(steps):
    kind, who, bdg = POSTURE[i]
    if kind == "eng":
        eng(p2[i], b2, BW, BH, lines, badge=bdg, n=str(i+1))
    elif kind == "surf":
        surf(p2[i], b2, BW, BH, who, lines, badge=bdg, n=str(i+1))
    else:
        assist(p2[i], b2, BW, BH, who, lines, badge=bdg, n=str(i+1))
    sublist(p2[i], b2+BH+26, BW, items)
    if i: arrow(p2[i-1]+BW, c2, p2[i]-6, c2)
lbl(BX+22, P2Y+PH2-14, "what the clinician is working around at each step", "start", "note")

# ---------------- the day-before negotiation ----------------
NY, NH = P2Y + PH2 + 46, 152
add(f'<rect x="{IX}" y="{NY}" width="1450" height="{NH}" rx="10" fill="none" '
    f'stroke="{RULE}" stroke-width="1.8" stroke-dasharray="8 6"/>')
lbl(IX+26, NY+36, "THE DAY-BEFORE NEGOTIATION — what the clinician has to hold", cls="pnl")
lbl(IX+44, NY+72, "HARD  —  accept it and build the day around it", cls="colh")
sublist(IX+38, NY+96, 520, ["Dialysis days and times",
                            "MD and specialist appointments",
                            "Caregiver's working hours",
                            "Patient genuinely not home"])
add(f'<line x1="{IX+700}" y1="{NY+54}" x2="{IX+700}" y2="{NY+138}" stroke="{C["clin"]}" stroke-width="3"/>')
lbl(IX+718, NY+72, "SOFT  —  negotiable, and worth holding the line on", cls="colhb")
sublist(IX+712, NY+96, 620, ["\u201cCan you come after lunch?\u201d",
                             "\u201cNot first thing\u201d  ·  \u201cNot Mondays\u201d",
                             "A preferred time with no reason behind it"])
add(f'<line x1="{IX+26}" y1="{NY+54}" x2="{IX+26}" y2="{NY+138}" stroke="{INK}" stroke-width="3"/>')
lbl(IX, NY+NH+36, "The first visit at 8 or 9am is the single largest lever on an individual "
    "clinician's capacity.", "start", "hi")
lbl(IX, NY+NH+58, "Newer clinicians let the patient set the time, become over-accommodating, and push "
    "the cost onto the rest of the team.", "start", "note")

# ---------------- disposition ----------------
DY = NY + NH + 112
DISPH = 246
disp = [(C["clin"], ["Accept", "visit delivered as planned"]),
        (C["clin"], ["Reschedule", "within the week"]),
        (C["pcc"],  ["Reassign", "back to the scheduler", "WITH a plan"]),
        (C["dcs"],  ["Miss", "\u2192 compliance chain"]),
        (C["pcc"],  ["Decline", "back to the scheduler", "WITHOUT a plan"])]
dnote = [[("the most common disposition", "hi")],
         [("no scheduler workflow if rapid", "hi"), ("reschedule is turned on in HCHB", "hi")],
         [("the clinician recommends", "note"), ("who should take it", "note")],
         [("documentation and", "note"), ("compliance chain follow", "note")],
         [("nothing recommended \u2014", "note"), ("the branch manages placement", "note")]]
dx = [IX + i*(BW+GAP) for i in range(5)]
add(f'<rect x="{BX}" y="{DY}" width="{5*(BW+GAP)+30}" height="{DISPH}" rx="10" fill="{BAND}"/>')
lbl(BX+22, DY+34, "THE DAY BEFORE  \u00b7  THE CLINICIAN'S FIVE DISPOSITIONS", cls="band")
lbl(BX+5*(BW+GAP)+8, DY+34, "SELECTED IN HCHB", "end", "bandhi")
lbl(BX+22, DY+58, "chosen the day prior, straight after the confirmation call \u2014 not at the door "
    "on the day of the visit", "start", "note")
bd = DY + 76
for i, (col, lines) in enumerate(disp):
    block(dx[i], bd, BW, 76, col, lines, small=True)
    for j, (t, cls) in enumerate(dnote[i]):
        lbl(dx[i]+BW/2, bd+102+j*18, t, "middle", cls)
conn(f"M {p2[5]+BW} {c2} L {W-140} {c2} L {W-140} {DY-26} L {BX-30} {DY-26} L {BX-30} {bd+38}")
arrow(BX-30, bd+38, dx[0]-6, bd+38)
lbl(IX, DY+DISPH-16, "Reassign and Decline are both clinician selections in HCHB, and both return the "
    "visit to the scheduler \u2014 the difference is whether a recommendation comes with it.",
    "start", "hi")

# ---------------- boundaries ----------------
BDY = DY + DISPH + 46
lbl(50, BDY+30, "BOUNDARIES", cls="trg")
bnd = ["OASIS visits do not move", "Medicare week is Sunday–Saturday",
       "Inside the 60-day certification period", "Auth still gates assignment"]
bxx = IX
for t in bnd:
    w = 8.6*len(t) + 46
    chip(bxx, BDY+8, w, 42, [t], MUT)
    bxx += w + 20

# ---------------- where it breaks ----------------
WY = BDY + 82
lbl(50, WY+34, "WHERE IT", cls="trg"); lbl(50, WY+52, "BROKE", cls="trg")
brk = [(["RN cannot reassign to her own LPN", "an HCHB rule, not Medicare"], C["dcs"], False),
       (["Supervisor cannot see", "the supervisee's schedule"], C["dcs"], False),
       (["Day-before calls are", "unpaid evening work"], C["clin"], True),
       (["The weekly logic is", "undocumented and unassisted"], C["clin"], True)]
wx = IX
for lines, col, fixed in brk:
    if fixed:
        ghost(wx, WY+8, 420, 70, lines, label="FIXED BY THE ENGINE")
    else:
        block(wx, WY+8, 420, 70, col, lines, small=True)
    wx += 440

add(f'<line x1="50" y1="{H-72}" x2="{W-50}" y2="{H-72}" stroke="{RULE}" stroke-width="1.4"/>')
lbl(50, H-40, "TARGET STATE, PROPOSED · green = the capacity & scheduling engine (dark text); purple = still inside HCHB · phase 1 is visualisation only (DE-03)",
    cls="foot")
lbl(W-50, H-40, "Flow 2T · routine visits — target state", "end", "foot")
add('</svg>')

import sys
OUT = sys.argv[1] if len(sys.argv) > 1 else "flow2-target.svg"
open(OUT, "w", encoding="utf-8").write("\n".join(out))
print("emitted", len(out), "| canvas", W, "x", H, "| ratio", round(W/H, 3))
