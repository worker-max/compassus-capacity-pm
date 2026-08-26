# -*- coding: utf-8 -*-
"""Flow 3 — Authorization, at its two interfaces with scheduling.
Canvas units = points on the output sheet."""

C = dict(pcc="#C6A01F", hchb="#795CA7", dcs="#792E2E", clin="#2E599D",
         auth="#DF751D", intake="#1F6F78", lead="#1A1A1A")
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

W, H = 2200, 1600
add(f'<svg viewBox="0 0 {W} {H}" role="img" xmlns="http://www.w3.org/2000/svg" '
    'aria-label="Authorization mapped at its two interfaces with scheduling. At start of care auth '
    'is a gate: eligibility is verified, pending auth is keyed at a visit count set by the payer, '
    'and the referral returns to intake for final approval before a scheduler can touch it. Inside '
    'the episode auth is a ceiling: the plan of care is written to clinical need, every visit is '
    'checked for auth on file, authorised visits are consumed and a re-authorisation is requested '
    'as the cap approaches.">')
add('<defs><marker id="ar" viewBox="0 0 10 8" refX="9" refY="4" markerWidth="8" markerHeight="6.5" '
    f'orient="auto-start-reverse"><polygon points="0,0 10,4 0,8" fill="{INK}"/></marker></defs>')
add(f'<rect x="0" y="0" width="{W}" height="{H}" fill="#FBFBF8"/>')

# ---------------- masthead ----------------
lbl(50, 58, "COMPASSUS HOME HEALTH  ·  FLOW 3 — TARGET STATE  ·  v1.0", cls="eyebrow")
lbl(50, 100, "Authorization", cls="title")
lbl(50, 128, "Read beside Flow-Authorization — same blocks, same positions. A dashed, struck-through block is a step that no longer exists",
    cls="deck")
lx = 990
for name, col in [("Intake", C["intake"]), ("Insurance & Auth", C["auth"]), ("DCS", C["dcs"]),
                  ("Clinician", C["clin"]), ("PCC / Scheduler", C["pcc"]), ("HCHB", C["hchb"]),
                  ("Capacity & Scheduling Engine", ENG)]:
    add(f'<circle cx="{lx+13}" cy="72" r="13" fill="{col}"/>')
    lbl(lx+34, 78, name, cls="leg")
    lx += 34 + 8.4*len(name) + 34
add(f'<line x1="50" y1="150" x2="{W-50}" y2="150" stroke="{RULE}" stroke-width="1.4"/>')

BX, IX = 320, 350

# ---------------- INTERFACE 1 — the gate at SOC ----------------
AY, AH = 190, 300
p = [IX + i*(BW+GAP) for i in range(5)]
add(f'<rect x="{BX}" y="{AY}" width="{5*(BW+GAP)+30}" height="{AH}" rx="10" fill="{BAND}"/>')
lbl(BX+22, AY+34, "INTERFACE 1  ·  AT START OF CARE — auth is a GATE", cls="band")
lbl(BX+5*(BW+GAP)+8, AY+34, "THE GATE CLEARS ITSELF", "end", "bandhi")
ab = AY + 62
ac = ab + BH/2
a_steps = [
    (C["intake"], ["Intake receives", "in Commure"],
     ["From hospital, MD, facility", "Payer and plan captured"]),
    (C["auth"], ["Eligibility and", "benefits verified"],
     ["Automated today", "Coordination note written here", "← the payer's rules land here"]),
    (C["auth"], ["Pending auth derived", "from the payer"],
     ["1 · 3 · 5 or 10 visits", "Derived, not keyed by hand"]),
    (C["intake"], ["Released to", "scheduling"],
     ["Completeness is rule-checked", "Exception only → intake"]),
    (C["pcc"], ["Scheduler books", "SOC and evals"],
     ["The first visits land", "Auth is already spent on these"]),
]
A_POST = ["eng", "eng", "eng", "eng", "assist"]
for i, (col, lines, subs) in enumerate(a_steps):
    if A_POST[i] == "eng":
        eng(p[i], ab, BW, BH, lines, n=str(i+1))
    else:
        assist(p[i], ab, BW, BH, col, lines, badge="ASSIST", n=str(i+1))
    sublist(p[i], ab+BH+26, subs)
    if i: arrow(p[i-1]+BW, ac, p[i]-6, ac)
chip(50, ac-39, 250, 78, ["Referral arrives", "hospital · MD · facility"], INK)
arrow(300, ac, IX-6, ac)
lbl(50, ac-53, "TRIGGER", cls="trg")

# traditional-Medicare bypass, drawn under the sublists
byp = AY + AH - 40
bx0, bx1 = p[0]+BW+14, p[3]+BW-24
path(f"M {bx0} {ac} L {bx0} {byp} L {bx1} {byp} L {bx1} {ab+BH+6}", dash=True)
lbl((bx0+bx1)/2, byp-11, "Traditional Medicare — no pending auth, straight through",
    "middle", "note")

lbl(IX, AY+AH+34, "The sentence this removes: “We know we have the referral, but it is just not in my "
    "workflow to schedule yet — it is stuck in auth.”", "start", "hi")

# ---------------- INTERFACE 2 — the ceiling inside the episode ----------------
QY, QH = AY + AH + 66, 240
q = [IX + i*(BW+GAP) for i in range(6)]
add(f'<rect x="{BX}" y="{QY}" width="{6*(BW+GAP)+30}" height="{QH}" rx="10" fill="{BAND}"/>')
lbl(BX+22, QY+34, "INTERFACE 2  ·  INSIDE THE PLAN OF CARE — auth is a CEILING", cls="band")
lbl(BX+6*(BW+GAP)+8, QY+34, "CHECKED PER VISIT, NOT PER EPISODE", "end", "bandhi")
qb = QY + 62
qc = qb + BH/2
q_steps = [
    (C["clin"], ["Clinician writes", "discipline frequency"],
     ["Written to clinical need", "The visit budget is shown here"], None),
    (C["dcs"], ["DCS reviews and", "approves the POC"],
     ["Utilisation management", "One task per discipline"], None),
    (C["hchb"], ["Auth on file for", "these visits?"],
     ["Asked of every visit", "Answered by HCHB, silently"], "GATE"),
    (C["pcc"], ["Scheduler assigns", "the authorised visits"],
     ["Proposed against the team", "Pending visits stay visible"], None),
    (C["hchb"], ["Visits consume", "the authorised count"],
     ["Counted down per visit", "The balance is on screen"], None),
    (C["auth"], ["Cap approached —", "re-auth requested"],
     ["Supporting documentation required", "The rule differs by payer, plan and state"], None),
]
Q_POST = [("surf", C["clin"]), ("man", C["dcs"]), ("man", C["hchb"]),
          ("assist", C["pcc"]), ("man", C["hchb"]), ("eng", None)]
for i, (col, lines, subs, badge) in enumerate(q_steps):
    kind, who = Q_POST[i]
    if kind == "eng":
        eng(q[i], qb, BW, BH, lines, badge=badge, n=str(i+1))
    elif kind == "surf":
        surf(q[i], qb, BW, BH, who, lines, badge=badge, n=str(i+1))
    elif kind == "assist":
        assist(q[i], qb, BW, BH, who, lines, badge=badge or "ASSIST", n=str(i+1))
    else:
        man(q[i], qb, BW, BH, who, lines, badge=badge, n=str(i+1))
    sublist(q[i], qb+BH+26, subs)
    if i: arrow(q[i-1]+BW, qc, q[i]-6, qc)

# no-auth exception
EY = QY + QH + 44
add(f'<rect x="{IX}" y="{EY}" width="{6*(BW+GAP)-28}" height="70" rx="8" fill="#FFFFFF" '
    f'stroke="{C["auth"]}" stroke-width="2"/>')
add(f'<rect x="{IX}" y="{EY}" width="7" height="70" rx="3.5" fill="{ENG}"/>')
lbl(IX+28, EY+29, "NO AUTH  —  the visit is pending, and visible", cls="pnlA")
lbl(IX+28, EY+52, "It sits on the clinician's calendar marked pending, it counts as committed load, and "
    "the remaining balance is on screen. Nothing lives on a sticky note.", "start", "note")
nx = q[2]+BW+14
path(f"M {nx} {qc} L {nx} {EY-6}", dash=True)
lbl(nx+12, EY-14, "No — no auth on file", "start", "conn")

# physician order / recert loop
LY = EY + 70 + 40
path(f"M {q[5]+BW} {qc} L {W-140} {qc} L {W-140} {LY} L {BX-30} {LY} L {BX-30} {qc}"
     f" L {q[0]-6} {qc}", dash=True)
lbl(IX+18, LY-12, "Every physician order, recertification and resumption of care re-enters this loop — "
    "and each one is a new auth question", "start", "hi")

# ---------------- what the payer already decided ----------------
PY, PH = LY + 46, 190
add(f'<rect x="{IX}" y="{PY}" width="1660" height="{PH}" rx="10" fill="none" '
    f'stroke="{RULE}" stroke-width="1.8" stroke-dasharray="8 6"/>')
lbl(IX+26, PY+36, "WHAT THE PAYER HAS ALREADY DECIDED — before anyone writes a plan of care", cls="pnl")
add(f'<line x1="{IX+26}" y1="{PY+54}" x2="{IX+26}" y2="{PY+172}" stroke="{INK}" stroke-width="3"/>')
lbl(IX+44, PY+74, "THE CAP IS SET UPSTREAM", cls="colh")
sublist(IX+38, PY+98, ["Every payer, plan and state sets its own — there is no single rule to learn",
                       "Indiana Medicaid — 8 visits shared across PT / OT / ST",
                       "Indiana Medicaid — 30 days from the discharge date, not the admit date",
                       "Ohio Medicaid — caps similarly; commercial and MA plans differ again"])
add(f'<line x1="{IX+880}" y1="{PY+54}" x2="{IX+880}" y2="{PY+172}" stroke="{C["auth"]}" stroke-width="3"/>')
lbl(IX+898, PY+74, "TWO CEILINGS, NOT ONE", cls="colhA")
sublist(IX+892, PY+98, ["Auth is permission — how many visits the payer will allow",
                        "PDGM is payment — the economic band for the period",
                        "LUPA is the floor; utilisation management is the ceiling",
                        "A visit can be authorised and still be uneconomic"])
lbl(IX, PY+PH+36, "The data already exists. The auth team writes the payer's rules into a coordination "
    "note at verification — days before anyone writes the plan of care.", "start", "hi")
lbl(IX, PY+PH+58, "Surfacing those rules at plan-of-care creation is the highest-value, "
    "lowest-complexity win in this flow — and a patient-care win, because abrupt discharges happen "
    "when nobody planned for the real visit budget.", "start", "note")

# ---------------- boundaries ----------------
BDY = PY + PH + 82
lbl(50, BDY+30, "BOUNDARIES", cls="trg")
bnd = ["Auth is drawn only where it meets scheduling",
       "Traditional Medicare has no pending auth",
       "Auth governs permission · PDGM governs payment"]
bxx = IX
for t in bnd:
    w = 8.6*len(t) + 46
    chip(bxx, BDY+8, w, 42, [t], MUT)
    bxx += w + 20

# ---------------- where it breaks ----------------
WY = BDY + 82
lbl(50, WY+34, "WHERE IT", cls="trg"); lbl(50, WY+52, "BROKE", cls="trg")
brk = [(["Pending-auth visits are invisible", "not on a calendar, not counted"], C["auth"]),
       (["~50 pending-auth workflows a day", "so schedulers bulk-clear without reading"], C["pcc"]),
       (["Plans of care ignore payer limits", "then the team is surprised"], C["clin"]),
       (["Abrupt discharge when the", "visit budget quietly runs out"], C["dcs"])]
wx = IX
for lines, col in brk:
    ghost(wx, WY+8, 420, 70, lines, label="ADDRESSED ABOVE")
    wx += 440
lbl(IX, WY+8+70+40, "Every failure this sheet used to end on is answered above: auth is derived rather than "
    "keyed, and the pending visit stays visible and counted.", "start", "hi")
lbl(IX, WY+8+70+60, "The payer's budget is shown at plan-of-care creation, and the balance is on screen "
    "long before it runs out.", "start", "note")

add(f'<line x1="50" y1="{H-72}" x2="{W-50}" y2="{H-72}" stroke="{RULE}" stroke-width="1.4"/>')
lbl(50, H-40, "TARGET STATE, PROPOSED · green = the capacity & scheduling engine (dark text); purple = still inside HCHB · phase 1 is visualisation only (DE-03)", cls="foot")
lbl(W-50, H-40, "Flow 3T · authorization — target state", "end", "foot")
add('</svg>')

import sys
OUT = sys.argv[1] if len(sys.argv) > 1 else "flow3-target.svg"
open(OUT, "w", encoding="utf-8").write("\n".join(out))
print("emitted", len(out), "| canvas", W, "x", H, "| ratio", round(W/H, 3),
      "| last content y", WY+8+70+60)
