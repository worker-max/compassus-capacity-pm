# -*- coding: utf-8 -*-
"""The primary current-state flow map. Canvas units = points on the output sheet."""

C = dict(pcc="#C6A01F", hchb="#795CA7", dcs="#792E2E", clin="#2E599D",
         auth="#DF751D", intake="#1F6F78", float_="#795933", lead="#1A1A1A")
INK, MUT, RULE, BAND = "#1B211E", "#5A6560", "#C9CCC5", "#E9E9E5"

out = []
def add(s): out.append(s)
def esc(t): return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

BW, BH, GAP = 250, 90, 28

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

def sublist(x, y, items):
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

def path(dd, dash=False):
    d = ' stroke-dasharray="7 5" opacity=".68"' if dash else ''
    add(f'<path d="{dd}" fill="none" class="ln"{d} marker-end="url(#ar)"/>')

def lbl(x, y, t, anchor="start", cls="lb"):
    add(f'<text x="{x}" y="{y}" class="{cls}" text-anchor="{anchor}">{esc(t)}</text>')

W, H = 2450, 1970
BX, IX = 320, 350
SLOT = BW + GAP
BANDW = 7*SLOT + 30

add(f'<svg viewBox="0 0 {W} {H}" role="img" xmlns="http://www.w3.org/2000/svg" '
    'aria-label="The current-state home health scheduling map in four phases. Referral to '
    'admission, plan of care established, steady state where the clinician runs their own week, '
    'and the end of the episode where the case either recertifies into a new period or discharges '
    'discipline by discipline. Colour marks the actor: intake, insurance and auth, the scheduler, '
    'the DCS, the clinician, HCHB itself, the float pool and branch leadership.">')
add('<defs><marker id="ar" viewBox="0 0 10 8" refX="9" refY="4" markerWidth="8" markerHeight="6.5" '
    f'orient="auto-start-reverse"><polygon points="0,0 10,4 0,8" fill="{INK}"/></marker></defs>')
add(f'<rect x="0" y="0" width="{W}" height="{H}" fill="#FBFBF8"/>')

# ---------------- masthead ----------------
lbl(50, 58, "COMPASSUS HOME HEALTH  ·  CAPACITY & SCHEDULING  ·  TARGET STATE  ·  v1.0", cls="eyebrow")
lbl(50, 100, "The Episode, End to End", cls="title")
lbl(50, 128, "Read beside Primary-Flow-Map — same blocks, same positions; only fill and wording change",
    cls="deck")
LEG0 = 1748
for r, grp in enumerate([[("Intake", C["intake"]), ("Insurance & Auth", C["auth"]),
                          ("PCC / Scheduler", C["pcc"]), ("DCS", C["dcs"])],
                         [("Clinician", C["clin"]), ("HCHB", C["hchb"]),
                          ("Per Diem / Float", C["float_"]), ("Branch Leadership", C["lead"])],
                         [("Capacity & Scheduling Engine", ENG)]]):
    lx, cy = LEG0, 58 + r*34
    for name, col in grp:
        add(f'<circle cx="{lx+13}" cy="{cy}" r="13" fill="{col}"/>')
        lbl(lx+34, cy+6, name, cls="leg")
        lx += 34 + 8.4*len(name) + 30
add(f'<line x1="50" y1="150" x2="{W-50}" y2="150" stroke="{RULE}" stroke-width="1.4"/>')

def band(y, h, title, right=None, slots=7, pad=0):
    w = slots*SLOT + 30 + pad
    add(f'<rect x="{BX}" y="{y}" width="{w}" height="{h}" rx="10" fill="{BAND}"/>')
    lbl(BX+22, y+34, title, cls="band")
    if right: lbl(BX+w-14, y+34, right, "end", "bandhi")

def row(y, steps, x0=None, breaks=(), post=None):
    """steps: (col, lines, subs, badge, slots). post: parallel [(kind, ordinal)] for target state."""
    x = IX if x0 is None else x0
    cy = y + BH/2
    prev = None
    for i, (col, lines, subs, badge, slots) in enumerate(steps):
        w = slots*SLOT - GAP
        kind, nn = (post[i] if post else ("man", None))
        if kind == "eng":
            eng(x, y, w, BH, lines, badge=badge, n=nn)
        elif kind == "surf":
            surf(x, y, w, BH, col, lines, badge=badge, n=nn)
        elif kind == "assist":
            assist(x, y, w, BH, col, lines, badge=badge or "ASSIST", n=nn)
        elif kind == "ghost":
            ghost(x, y, w, BH, lines, n=nn, label="")
        else:
            man(x, y, w, BH, col, lines, badge=badge, n=nn)
        if subs: sublist(x, y+BH+26, subs)
        if prev is not None:
            if i in breaks:
                mx = (prev + x)/2
                add(f'<line x1="{mx}" y1="{y-4}" x2="{mx}" y2="{y+BH+4}" stroke="{MUT}" '
                    'stroke-width="2" stroke-dasharray="6 5"/>')
                lbl(mx, y-16, "OR", "middle", "trg")
            else:
                arrow(prev, cy, x-6, cy)
        prev = x + w
        x += slots*SLOT
    return cy

# ================= PHASE 1 =================
AY, AH = 190, 240
band(AY, AH, "PHASE 1  ·  REFERRAL TO ADMISSION", "NOTHING SCHEDULES UNTIL AUTH AND INTAKE CLEAR")
ab = AY + 62
AC_POST = [("eng","1"),("eng","2"),("eng","3"),("man","4"),("surf","5"),("assist","6"),("man","7")]
ac = row(ab, [
 (C["intake"], ["Intake receives", "the referral"], ["In Commure", "Payer and plan captured"], None, 1),
 (C["auth"], ["Auth verifies eligibility", "keys pending auth"],
  ["Traditional Medicare passes through", "Visit count set by the payer", "→ detail in Flow 3"], None, 1),
 (C["intake"], ["Intake gives", "final approval"], ["The referral is now complete", "Only now does it move"], None, 1),
 (C["dcs"], ["DCS reviews", "the referral"], ["Orders read", "Disciplines confirmed"], None, 1),
 (C["pcc"], ["Scheduler makes the", "welcome / intake call"],
  ["Is the patient actually home?", "Not still inpatient", "Not deferring admission"], "THE ONE JUDGMENT CALL", 1),
 (C["pcc"], ["Scheduler assigns the", "SOC and discipline evals"], ["SOC first", "Evals one to two days later"], None, 1),
 (C["clin"], ["Clinicians perform", "SOC and evals"], ["RN at the SOC", "PT · OT · ST at their own"], None, 1),
], post=AC_POST)
chip(50, ac-39, 250, 78, ["Referral arrives", "hospital · MD · facility"], INK)
arrow(300, ac, IX-6, ac)
lbl(50, ac-53, "TRIGGER", cls="trg")

# ================= PHASE 2 =================
QY, QH = AY + AH + 36, 240
band(QY, QH, "PHASE 2  ·  THE PLAN OF CARE IS ESTABLISHED", "PLOTTED BY FREQUENCY · ASSIGNED IN ONE PASS")
qb = QY + 62
QC_POST = [("surf","1"),("man","2"),("man","3"),("man","4"),("assist","5"),("man","6")]
qc = row(qb, [
 (C["clin"], ["Each discipline plots", "its own frequency"],
  ["Written to clinical need", "Payer limits not visible here", "RN also plots aide + MSW / ST"], "× N disciplines", 1),
 (C["dcs"], ["DCS reviews and", "approves the POC"],
  ["One task per discipline", "Utilisation management starts here",
   "Not approved → nothing moves, visits held"], "× N disciplines", 1),
 (C["dcs"], ["THE 485 MOMENT", "QA accepted  ·  POC locked", "485 submitted  ·  orders to MD"],
  ["Four things, not four gates", "Orders finalised and sent for signature"], "ALL AT ONCE", 2),
 (C["hchb"], ["HCHB generates", "the visits"],
  ["The care team is already set", "Frequency becomes many visits"], None, 1),
 (C["pcc"], ["Scheduler assigns all", "plotted visits — one pass"],
  ["Many visits per frequency", "Auth on file? asked per visit", "No auth → the visit sits pending"], None, 1),
 (C["hchb"], ["Visits land on the", "clinician's calendar"],
  ["Pending visits appear, marked", "The sync lag is measured and shown"], None, 1),
], post=QC_POST)

# ================= PHASE 3 =================
RY, RH = QY + QH + 36, 316
band(RY, RH, "PHASE 3  ·  STEADY STATE — the clinician runs their own week",
     "NO SCHEDULER WORKFLOW", slots=6)
rb = RY + 62
RC_POST = [("eng","1"),("surf","2"),("eng","3"),("surf","4"),("assist","5"),("eng","6")]
rc = row(rb, [
 (C["clin"], ["Evaluate own capacity", "for the week"], ["Points already committed", "Days off · PTO · on-call"], None, 1),
 (C["clin"], ["Prioritise clinical need", "across the caseload"], ["Who is unstable", "Wound · IV · catheter · labs due"], None, 1),
 (C["clin"], ["Group visits", "geographically"], ["Drive time, not distance", "Bridges · rivers · crossings"], None, 1),
 (C["clin"], ["Test against hard", "constraints"],
  ["Wound · catheter · IV timing", "Caregiver must be present", "Preferences sit in a coordination note"], None, 1),
 (C["clin"], ["Confirmation — clinician", "directs, engine calls"], ["Hard versus soft pushback", "→ detail in Flow 2"], "CLINICIAN-TRIGGERED", 1),
 (None, ["Routed on drive time,", "not distance"], ["Time windows", "Where the day starts and ends"], None, 1),
], post=RC_POST)
# dispositions strip inside the band
DSY = rb + BH + 108
lbl(IX, DSY-10, "THE DISPOSITIONS  —  chosen the day before, selected in HCHB", cls="pnl")
dxx = IX
w = 8.9*6 + 60
chip(dxx, DSY+4, w, 40, ["Accept"], C["clin"])
dxx += w + 14
lbl(dxx, DSY+30, "confirmed → accepted", "start", "note")
dxx += 158
lbl(dxx, DSY+30, "NOT CONFIRMED →", "start", "trg")
dxx += 152
for t, col in [("Reschedule", C["clin"]), ("Reassign", C["pcc"]),
               ("Miss", C["dcs"]), ("Decline", C["pcc"])]:
    w = 8.9*len(t) + 60
    chip(dxx, DSY+4, w, 40, [t], col)
    dxx += w + 14
lbl(dxx + 8, DSY+30, "reassign returns with a plan, decline without one — decline is the least used",
    "start", "note")

# ================= PHASE 4 =================
SY, SH = RY + RH + 36, 230
band(SY, SH, "PHASE 4  ·  END OF EPISODE — recertify or discharge", "CONDENSED · DETAIL IN FLOW 5",
     slots=6, pad=76)
sb = SY + 62
sc = row(sb, [
 (C["hchb"], ["Recert window opens", "— last 5 days"],
  ["Recert visits are already booked", "Plotted at the original POC"], None, 1),
 (C["clin"], ["Recertifying disciplines", "set the next 60 days"],
  ["Discipline by discipline", "Goals met → discharge instead"], None, 1),
 (C["pcc"], ["The next period", "is assigned"],
  ["Only after frequency is set", "Same one-pass proposal"], None, 1),
 (C["clin"], ["Or discharge — each", "discipline separately"],
  ["Discipline discharges are non-OASIS", "Staggered, not simultaneous"], None, 1),
 (C["clin"], ["The last discipline out", "does the agency D/C OASIS"],
  ["RN, PT, OT — whoever visits last", "Owner is unknown until it happens"], None, 1),
], breaks=(3,), post=[("eng","1"), ("surf","2"), ("assist","3"), ("man","4"), ("man","5")])
chip(IX + 5*SLOT + 24, sc-39, 300, 78, ["Capacity returns", "to the branch"], INK)
arrow(IX + 4*SLOT + BW, sc, IX + 5*SLOT + 18, sc)

# recert loop back into phase 2
LOOP = SY + SH + 26
lpx = IX + 2*SLOT + 214
path(f"M {lpx} {sb+BH+6} L {lpx} {LOOP} L {BX-34} {LOOP} L {BX-34} {qc} L {IX-6} {qc}", dash=True)
lbl(lpx - 24, LOOP-12, "a new certification period re-enters the plan-of-care phase",
    "end", "hi")

# ================= exceptions & levers =================
EY = LOOP + 54
lbl(50, EY+30, "MISSED VISIT", cls="trg"); lbl(50, EY+48, "AND LEVERS", cls="trg")
MC_POST = [("man",None),("eng",None),("man",None)]
mc = row(EY, [
 (C["clin"], ["Clinician documents", "a missed visit"], None, None, 1),
 (None, ["MD notified inside", "48 hours"], None, None, 1),
 (C["dcs"], ["Not in time →", "workflow to the DCS"], None, None, 1),
], post=MC_POST)
lbl(IX, EY+BH+26, "A compliance chain, not a dead end — Medicare requirement and an HCHB hard stop",
    "start", "note")
lvx = IX + 3*SLOT + 40
block(lvx, EY, 2*SLOT-GAP, BH, C["float_"], ["Per diem / float pool", "— no territory, on purpose"])
sublist(lvx, EY+BH+26, ["Takes the SOCs, absorbing the admission spike",
                        "Or covers visits to free a territory clinician"])
block(lvx + 2*SLOT, EY, 2*SLOT-GAP, BH, C["lead"], ["Branch leadership", "— the capacity decision"])
sublist(lvx + 2*SLOT, EY+BH+26, ["Territory alignment",
                                 "Referral acceptance when capacity tightens"])
lbl(lvx, EY-14, "PULLED ON PURPOSE WHEN CAPACITY TIGHTENS — not recovery, instrument", cls="trg")

# ================= panel =================
PY, PH = EY + BH + 80, 160
add(f'<rect x="{IX}" y="{PY}" width="{BANDW-60}" height="{PH}" rx="10" fill="none" '
    f'stroke="{RULE}" stroke-width="1.8" stroke-dasharray="8 6"/>')
lbl(IX+26, PY+36, "READING THIS MAP", cls="pnl")
add(f'<line x1="{IX+26}" y1="{PY+54}" x2="{IX+26}" y2="{PY+144}" stroke="{INK}" stroke-width="3"/>')
lbl(IX+44, PY+74, "THREE DIFFERENT CEILINGS ON ONE EPISODE", cls="colh")
sublist(IX+38, PY+98, ["Auth is permission — how many visits the payer will allow",
                       "LUPA is the floor — too few visits and the period pays per visit",
                       "Utilisation management is the ceiling — extra visits earn nothing"])
add(f'<line x1="{IX+1010}" y1="{PY+54}" x2="{IX+1010}" y2="{PY+144}" stroke="{C["pcc"]}" stroke-width="3"/>')
lbl(IX+1028, PY+74, "WHAT THIS MAP IS", cls="colhb")
sublist(IX+1022, PY+98, ["Target state — every block sits where the current-state map put it",
                         "Green is the engine. Purple is still HCHB. A colour bar means a person decides",
                         "Numbered chips read against the same numbers on Primary-Flow-Map"])

# ================= where it breaks =================
WY = PY + PH + 48
lbl(50, WY+34, "WHERE IT", cls="trg"); lbl(50, WY+52, "BROKE", cls="trg")
brk = [(["Eight tasks for one decision", "the per-discipline explosion"], C["hchb"]),
       (["Pending-auth visits are invisible", "not on a calendar, not counted"], C["auth"]),
       (["The weekly logic is undocumented", "and entirely unassisted"], C["clin"]),
       (["Capacity is read, never modelled", "so the levers are pulled late"], C["pcc"])]
wx = IX
for lines, col in brk:
    ghost(wx, WY+8, 480, 70, lines, label="ADDRESSED ABOVE")
    wx += 500

add(f'<line x1="50" y1="{H-72}" x2="{W-50}" y2="{H-72}" stroke="{RULE}" stroke-width="1.4"/>')
lbl(50, H-40, "TARGET STATE, PROPOSED · green = the capacity & scheduling engine (dark text); purple = still inside HCHB · phase 1 is visualisation only (DE-03)", cls="foot")
lbl(W-50, H-40, "The episode, end to end — target state", "end", "foot")
add('</svg>')

import sys
OUT = sys.argv[1] if len(sys.argv) > 1 else "episode-target.svg"
open(OUT, "w", encoding="utf-8").write("\n".join(out))
print("emitted", len(out), "| canvas", W, "x", H, "| ratio", round(W/H, 3),
      "| band right", BX+BANDW, "| last content y", WY+78)
