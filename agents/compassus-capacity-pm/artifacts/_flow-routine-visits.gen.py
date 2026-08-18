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

def block(x, y, w, h, fill, lines, small=False, badge=None):
    add(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="5" fill="{fill}"/>')
    lh = 15.5 if small else 19
    cls = "bt s" if small else "bt"
    cy = y + h/2 - (len(lines)-1)*lh/2 + (5 if small else 6)
    for i, ln in enumerate(lines):
        add(f'<text x="{x+w/2}" y="{cy+i*lh}" class="{cls}" text-anchor="middle">{esc(ln)}</text>')
    if badge:
        bw = 8.3*len(badge)+18
        add(f'<rect x="{x+w-bw-8}" y="{y-14}" width="{bw}" height="23" rx="11.5" fill="#FFFFFF" '
            f'stroke="{fill}" stroke-width="1.8"/>')
        add(f'<text x="{x+w-bw/2-8}" y="{y+2}" class="bdg" text-anchor="middle" fill="{fill}">{esc(badge)}</text>')

def vchip(x, y, w, ids):
    """light variable chip under a block"""
    if not SHOW_VCHIPS or not ids: return
    add(f'<rect x="{x}" y="{y}" width="{w}" height="{CHH}" rx="6" fill="#FFFFFF" '
        f'stroke="{RULE}" stroke-width="1.3"/>')
    add(f'<text x="{x+w/2}" y="{y+18.5}" class="vid" text-anchor="middle">{esc(" · ".join(ids))}</text>')

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

W, H = 2200, 1290
add(f'<svg viewBox="0 0 {W} {H}" role="img" xmlns="http://www.w3.org/2000/svg" '
    'aria-label="Routine visit scheduling in two phases. Phase one is a burst of scheduler work at '
    'admission: each discipline plots its own frequency, every submission generates its own '
    'assignment task. After the 485 the episode enters phase two, where the clinician manages their '
    'own week with no scheduler workflow at all, and reassignment is the only thing that pulls the '
    'scheduler back in.">')
add('<defs><marker id="ar" viewBox="0 0 10 8" refX="9" refY="4" markerWidth="8" markerHeight="6.5" '
    f'orient="auto-start-reverse"><polygon points="0,0 10,4 0,8" fill="{INK}"/></marker></defs>')
add(f'<rect x="0" y="0" width="{W}" height="{H}" fill="#FBFBF8"/>')

# masthead
lbl(50, 58, "COMPASSUS HOME HEALTH  ·  FLOW 2", cls="eyebrow")
lbl(50, 100, "Routine Visit Scheduling", cls="title")
lbl(50, 128, "A burst of scheduler work at admission, then the clinician runs their own week",
    cls="deck")
lx = 1300
for name, col in [("DCS", C["dcs"]), ("PCC / Scheduler", C["pcc"]),
                  ("Clinician", C["clin"]), ("HCHB", C["hchb"])]:
    add(f'<circle cx="{lx+13}" cy="72" r="13" fill="{col}"/>')
    lbl(lx+34, 78, name, cls="leg")
    lx += 34 + 8.4*len(name) + 40
add(f'<line x1="50" y1="150" x2="{W-50}" y2="150" stroke="{RULE}" stroke-width="1.4"/>')

BX, IX = 320, 350
PH = 250 if SHOW_VCHIPS else 205

# ---------------- PHASE ONE ----------------
P1Y = 185
p1 = [IX + i*(BW+GAP) for i in range(4)]
add(f'<rect x="{BX}" y="{P1Y}" width="{4*(BW+GAP)+30}" height="{PH}" rx="10" fill="{BAND}"/>')
lbl(BX+22, P1Y+34, "PHASE 1  ·  FREQUENCY PLOTTING & INITIAL ASSIGNMENT — the burst", cls="band")
b1 = P1Y + 60
c1 = b1 + BH/2
block(p1[0], b1, BW, BH, C["clin"], ["Evaluating clinician", "plots own discipline", "frequency"],
      badge="× N disciplines")
block(p1[1], b1, BW, BH, C["clin"], ["RN also plots aide", "frequency + MSW / ST", "initial eval"])
block(p1[2], b1, BW, BH, C["hchb"], ["Each submission", "generates its own", "assignment task"],
      badge="× N disciplines")
block(p1[3], b1, BW, BH, C["pcc"], ["Scheduler assigns", "visits to care team"])
vchip(p1[0], b1+BH+9, BW, ["S-01", "S-02", "S-03"])
vchip(p1[1], b1+BH+9, BW, ["SH-03", "S-37"])
vchip(p1[3], b1+BH+9, BW, ["S-15", "S-16", "S-22"])
for a in range(3):
    arrow(p1[a]+BW, c1, p1[a+1]-6, c1)
chip(50, c1-39, 250, 78, ["Admission", "SOC or eval visit"], INK)
arrow(300, c1, IX-6, c1)
lbl(50, c1-53, "TRIGGER", cls="trg")
lbl(p1[0], b1+BH+CHH+26, "RN at the SOC; PT and OT at their own evals, 1–2 days later",
    "start", "note")

# ---------------- 485 boundary ----------------
BY = P1Y + PH + 46
add(f'<line x1="{BX}" y1="{BY+26}" x2="{IX-14}" y2="{BY+26}" stroke="{INK}" '
    'stroke-width="2.5" stroke-dasharray="14 7"/>')
add(f'<line x1="{IX+494}" y1="{BY+26}" x2="{BX+6*(BW+GAP)+30}" y2="{BY+26}" stroke="{INK}" '
    'stroke-width="2.5" stroke-dasharray="14 7"/>')
add(f'<rect x="{IX}" y="{BY+6}" width="480" height="40" rx="20" fill="#FBFBF8" stroke="{INK}" stroke-width="2"/>')
lbl(IX+240, BY+32, "485 SUBMITTED — after this, every order is an add-on", "middle", "boundary")
lbl(IX+240, BY+66, "add-on orders route through DCS approval and auth before reaching the scheduler",
    "middle", "note")

# ---------------- PHASE TWO ----------------
P2Y = BY + 92
p2 = [IX + i*(BW+GAP) for i in range(6)]
add(f'<rect x="{BX}" y="{P2Y}" width="{6*(BW+GAP)+30}" height="{PH}" rx="10" fill="{BAND}"/>')
lbl(BX+22, P2Y+34, "PHASE 2  ·  STEADY STATE — the clinician runs their own week", cls="band")
lbl(BX+6*(BW+GAP)+8, P2Y+34, "NO SCHEDULER WORKFLOW", "end", "bandhi")
b2 = P2Y + 60
c2 = b2 + BH/2
steps = [
    (["Evaluate own", "capacity for", "the week"],            ["S-04", "S-11", "C-06"]),
    (["Prioritise clinical", "need across", "the caseload"],  ["S-31", "S-33"]),
    (["Group visits", "geographically"],                      ["S-17", "S-19"]),
    (["Test against hard", "constraints"],                    ["S-21", "S-25", "S-28", "S-32"]),
    (["Confirm with the", "patient — day before"],            ["CO-01", "CO-06"]),
    (["Route — HCHB suggests,", "clinician adjusts"],         ["S-14", "S-18", "S-20"]),
]
for i, (lines, ids) in enumerate(steps):
    block(p2[i], b2, BW, BH, C["clin"], lines)
    vchip(p2[i], b2+BH+9, BW, ids)
    if i: arrow(p2[i-1]+BW, c2, p2[i]-6, c2)
lbl(p2[3]+BW/2, b2+BH+CHH+26, "wound timing · catheter · IV · patient preference · competing appointments",
    "middle", "note")

# ---------------- disposition ----------------
DY = P2Y + PH + 58
disp = [("Accept", C["clin"], ["Accept", "visit delivered"], []),
        ("Reschedule", C["clin"], ["Reschedule", "within the week"], ["S-26", "S-27"]),
        ("Reassign", C["pcc"], ["Reassign", "back to scheduler —", "usually RN to her own LPN"], ["S-15", "S-22"]),
        ("Miss", C["dcs"], ["Miss", "→ compliance chain"], ["S-38", "S-39"]),
        ("Decline", C["pcc"], ["Decline", "back to scheduler —", "must go to a different clinician"], ["S-12", "S-13"])]
dx = [IX + i*(BW+GAP) for i in range(5)]
add(f'<rect x="{BX}" y="{DY}" width="{5*(BW+GAP)+30}" height="{PH-40}" rx="10" fill="{BAND}"/>')
lbl(BX+22, DY+34, "AT THE VISIT  ·  THE CLINICIAN'S FIVE DISPOSITIONS", cls="band")
bd = DY + 60
for i, (_, col, lines, ids) in enumerate(disp):
    block(dx[i], bd, BW, 76, col, lines, small=True)
    vchip(dx[i], bd+76+9, BW, ids)
conn(f"M {p2[5]+BW/2} {b2+BH+6} L {p2[5]+BW/2} {DY-26} L {dx[2]+BW/2} {DY-26}")
arrow(dx[2]+BW/2, DY-26, dx[2]+BW/2, bd-6)
lbl(dx[2]+BW/2, bd+76+CHH+26, "the only recurring scheduler trigger", "middle", "hi")
lbl(dx[4]+BW/2, bd+76+CHH+26, "the scheduler sees it was declined", "middle", "hi")

# ---------------- boundaries ----------------
BDY = DY + PH + 26
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
lbl(50, WY+34, "WHERE IT", cls="trg"); lbl(50, WY+52, "BREAKS", cls="trg")
brk = [(["RN cannot reassign to her own LPN", "an HCHB rule, not Medicare"], C["dcs"]),
       (["Supervisor cannot see", "the supervisee's schedule"], C["dcs"]),
       (["Day-before calls are", "unpaid evening work"], C["clin"]),
       (["The weekly logic is", "undocumented and unassisted"], C["clin"])]
wx = IX
for lines, col in brk:
    block(wx, WY+8, 420, 70, col, lines, small=True)
    wx += 440

add(f'<line x1="50" y1="{H-72}" x2="{W-50}" y2="{H-72}" stroke="{RULE}" stroke-width="1.4"/>')
lbl(50, H-40, "Current state · variables are named in the variable reference, not on this sheet",
    cls="foot")
lbl(W-50, H-40, "Flow 2 of 4 · routine visits", "end", "foot")
add('</svg>')

open("/tmp/claude-0/-home-user/f0ef1ecc-a04c-5098-a365-4b559e397089/scratchpad/gen/flow2.svg",
     "w", encoding="utf-8").write("\n".join(out))
print("emitted", len(out), "| canvas", W, "x", H, "| ratio", round(W/H, 3))
