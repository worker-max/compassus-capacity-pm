# -*- coding: utf-8 -*-
"""The primary current-state flow map. Canvas units = points on the output sheet."""

C = dict(pcc="#C6A01F", hchb="#795CA7", dcs="#792E2E", clin="#2E599D",
         auth="#DF751D", intake="#1F6F78", float_="#795933", lead="#1A1A1A")
INK, MUT, RULE, BAND = "#1B211E", "#5A6560", "#C9CCC5", "#E9E9E5"

out = []
def add(s): out.append(s)
def esc(t): return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

BW, BH, GAP = 250, 90, 28

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
lbl(50, 58, "COMPASSUS HOME HEALTH  ·  CAPACITY & SCHEDULING  ·  CURRENT STATE", cls="eyebrow")
lbl(50, 100, "The Episode, End to End", cls="title")
lbl(50, 128, "Referral to admission · plan of care · the clinician's own week · recertify or discharge",
    cls="deck")
LEG0 = 1748
for r, grp in enumerate([[("Intake", C["intake"]), ("Insurance & Auth", C["auth"]),
                          ("PCC / Scheduler", C["pcc"]), ("DCS", C["dcs"])],
                         [("Clinician", C["clin"]), ("HCHB", C["hchb"]),
                          ("Per Diem / Float", C["float_"]), ("Branch Leadership", C["lead"])]]):
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

def row(y, steps, x0=None, breaks=()):
    """steps: (col, lines, subs, badge, slots). breaks: indices that get an OR divider, not an arrow."""
    x = IX if x0 is None else x0
    cy = y + BH/2
    prev = None
    for i, (col, lines, subs, badge, slots) in enumerate(steps):
        w = slots*SLOT - GAP
        block(x, y, w, BH, col, lines, badge=badge)
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
])
chip(50, ac-39, 250, 78, ["Referral arrives", "hospital · MD · facility"], INK)
arrow(300, ac, IX-6, ac)
lbl(50, ac-53, "TRIGGER", cls="trg")

# ================= PHASE 2 =================
QY, QH = AY + AH + 36, 240
band(QY, QH, "PHASE 2  ·  THE PLAN OF CARE IS ESTABLISHED", "ONE TASK PER DISCIPLINE, TWICE")
qb = QY + 62
qc = row(qb, [
 (C["clin"], ["Each discipline plots", "its own frequency"],
  ["Written to clinical need", "Payer limits not visible here", "RN also plots aide + MSW / ST"], "× N disciplines", 1),
 (C["dcs"], ["DCS reviews and", "approves the POC"],
  ["One task per discipline", "Utilisation management starts here"], "× N disciplines", 1),
 (C["dcs"], ["THE 485 MOMENT", "QA accepted  ·  POC locked", "485 submitted  ·  orders to MD"],
  ["Four things, not four gates", "Orders finalised and sent for signature"], "ALL AT ONCE", 2),
 (C["hchb"], ["HCHB generates visits", "and assignment tasks"],
  ["One task per discipline, again", "Eight tasks for a decision already made"], "× N disciplines", 1),
 (C["pcc"], ["Scheduler assigns", "the authorised visits"],
  ["Auth on file? asked per visit", "No auth → the visit sits pending"], None, 1),
 (C["hchb"], ["Visits land on the", "clinician's calendar"],
  ["Pending-auth visits never appear", "Citrix sync lags behind"], None, 1),
])

# ================= PHASE 3 =================
RY, RH = QY + QH + 36, 316
band(RY, RH, "PHASE 3  ·  STEADY STATE — the clinician runs their own week",
     "NO SCHEDULER WORKFLOW", slots=6)
rb = RY + 62
rc = row(rb, [
 (C["clin"], ["Evaluate own capacity", "for the week"], ["Points already committed", "Days off · PTO · on-call"], None, 1),
 (C["clin"], ["Prioritise clinical need", "across the caseload"], ["Who is unstable", "Wound · IV · catheter · labs due"], None, 1),
 (C["clin"], ["Group visits", "geographically"], ["Drive time, not distance", "Bridges · rivers · crossings"], None, 1),
 (C["clin"], ["Test against hard", "constraints"],
  ["Wound · catheter · IV timing", "Caregiver must be present", "Preferences sit in a coordination note"], None, 1),
 (C["clin"], ["Confirm with the patient", "— the day before"], ["Hard versus soft pushback", "→ detail in Flow 2"], None, 1),
 (C["hchb"], ["Route — HCHB suggests,", "clinician adjusts"], ["Time windows", "Where the day starts and ends"], None, 1),
])
# dispositions strip inside the band
DSY = rb + BH + 108
lbl(IX, DSY-10, "THE FIVE DISPOSITIONS  —  chosen the day before, selected in HCHB", cls="pnl")
dpos = [("Accept", C["clin"]), ("Reschedule", C["clin"]), ("Reassign", C["pcc"]),
        ("Miss", C["dcs"]), ("Decline", C["pcc"])]
dxx = IX
for t, col in dpos:
    w = 8.9*len(t) + 60
    chip(dxx, DSY+4, w, 40, [t], col)
    dxx += w + 18
lbl(dxx + 16, DSY+30, "Accept is the common one.  Reassign and Decline both return the visit to the "
    "scheduler — with a recommendation, or without.", "start", "note")

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
 (C["hchb"], ["Scheduling workflow", "fires for the new period"],
  ["Only after frequency is set", "The recert visit needed none"], None, 1),
 (C["clin"], ["Or discharge — each", "discipline separately"],
  ["Discipline discharges are non-OASIS", "Staggered, not simultaneous"], None, 1),
 (C["clin"], ["The last discipline out", "does the agency D/C OASIS"],
  ["RN, PT, OT — whoever visits last", "Owner is unknown until it happens"], None, 1),
], breaks=(3,))
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
mc = row(EY, [
 (C["clin"], ["Clinician documents", "a missed visit"], None, None, 1),
 (C["pcc"], ["Scheduler notifies the", "MD within 48 hours"], None, None, 1),
 (C["dcs"], ["Not in time →", "workflow to the DCS"], None, None, 1),
])
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
sublist(IX+1022, PY+98, ["Current state — including what is wasteful or manual",
                         "Colour is the actor. Purple only where HCHB acts by itself",
                         "Flows 2, 3 and 5 hold the detail behind the condensed steps"])

# ================= where it breaks =================
WY = PY + PH + 48
lbl(50, WY+34, "WHERE IT", cls="trg"); lbl(50, WY+52, "BREAKS", cls="trg")
brk = [(["Eight tasks for one decision", "the per-discipline explosion"], C["hchb"]),
       (["Pending-auth visits are invisible", "not on a calendar, not counted"], C["auth"]),
       (["The weekly logic is undocumented", "and entirely unassisted"], C["clin"]),
       (["Capacity is read, never modelled", "so the levers are pulled late"], C["pcc"])]
wx = IX
for lines, col in brk:
    block(wx, WY+8, 480, 70, col, lines, small=True)
    wx += 500

add(f'<line x1="50" y1="{H-72}" x2="{W-50}" y2="{H-72}" stroke="{RULE}" stroke-width="1.4"/>')
lbl(50, H-40, "Current state · nothing on this sheet is a proposal", cls="foot")
lbl(W-50, H-40, "Primary map · four detail flows sit behind it", "end", "foot")
add('</svg>')

open("/tmp/claude-0/-home-user/f0ef1ecc-a04c-5098-a365-4b559e397089/scratchpad/gen/main.svg",
     "w", encoding="utf-8").write("\n".join(out))
print("emitted", len(out), "| canvas", W, "x", H, "| ratio", round(W/H, 3),
      "| band right", BX+BANDW, "| last content y", WY+78)
