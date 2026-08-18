# -*- coding: utf-8 -*-
"""The detailed flow, in the original sheet's design: five functional columns,
the grey clean-path spine through the middle, feeders above, recovery below.
Canvas units = points on the output sheet."""

C = dict(pcc="#C6A01F", hchb="#795CA7", dcs="#792E2E", clin="#2E599D",
         auth="#DF751D", intake="#1F6F78", float_="#795933", lead="#1A1A1A",
         pat="#4E8A5B")
INK, MUT, RULE = "#1B211E", "#5A6560", "#C9CCC5"
TAG = "#E8EAED"

out = []
def add(s): out.append(s)
def esc(t): return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

def block(x, y, w, h, fill, lines, small=False, badge=None, tc="#fff"):
    add(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6" fill="{fill}"/>')
    lh = 16 if small else 18
    cls = "bt s" if small else "bt"
    cy = y + h/2 - (len(lines)-1)*lh/2 + (5 if small else 6)
    for i, ln in enumerate(lines):
        add(f'<text x="{x+w/2}" y="{cy+i*lh}" class="{cls}" fill="{tc}" text-anchor="middle">{esc(ln)}</text>')
    if badge:
        bw = 7.6*len(badge)+18
        add(f'<rect x="{x+w-bw-8}" y="{y-13}" width="{bw}" height="22" rx="11" fill="#FFFFFF" '
            f'stroke="{fill}" stroke-width="1.7"/>')
        add(f'<text x="{x+w-bw/2-8}" y="{y+2.5}" class="bdg" text-anchor="middle" fill="{fill}">{esc(badge)}</text>')

def tag(x, y, w, h, lines):
    add(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="3" fill="{TAG}" stroke="#C6CBD1" stroke-width="1"/>')
    lh = 17
    cy = y + h/2 - (len(lines)-1)*lh/2 + 5
    for i, ln in enumerate(lines):
        add(f'<text x="{x+w/2}" y="{cy+i*lh}" class="tg" text-anchor="middle">{esc(ln)}</text>')

def oval(cx, cy, rx, ry, fill, lines, outline=None):
    if outline:
        add(f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="#FFFFFF" '
            f'stroke="{outline}" stroke-width="1.8"/>')
        tfill = outline
    else:
        add(f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="{fill}"/>')
        tfill = "#fff"
    lh = 17
    y0 = cy - (len(lines)-1)*lh/2 + 5
    for i, ln in enumerate(lines):
        add(f'<text x="{cx}" y="{y0+i*lh}" class="bt s" style="fill:{tfill}" text-anchor="middle">{esc(ln)}</text>')

def diamond(cx, cy, lines, w=150, h=112):
    add(f'<polygon points="{cx},{cy-h/2} {cx+w/2},{cy} {cx},{cy+h/2} {cx-w/2},{cy}" '
        f'fill="#FFFFFF" stroke="{INK}" stroke-width="1.8"/>')
    y0 = cy - (len(lines)-1)*16/2 + 5
    for i, ln in enumerate(lines):
        add(f'<text x="{cx}" y="{y0+i*16}" class="dt" text-anchor="middle">{esc(ln)}</text>')

def arrow(x1, y1, x2, y2, dash=False):
    d = ' stroke-dasharray="6 5" opacity=".7"' if dash else ''
    add(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" class="ln"{d} marker-end="url(#ar)"/>')

def path(dd, dash=False, label=None, lx=None, ly=None, anchor="middle"):
    d = ' stroke-dasharray="6 5" opacity=".7"' if dash else ''
    add(f'<path d="{dd}" fill="none" class="ln"{d} marker-end="url(#ar)"/>')
    if label:
        add(f'<text x="{lx}" y="{ly}" class="lb" text-anchor="{anchor}">{esc(label)}</text>')

def lbl(x, y, t, anchor="start", cls="lb"):
    add(f'<text x="{x}" y="{y}" class="{cls}" text-anchor="{anchor}">{esc(t)}</text>')

W, H = 2600, 1780
add(f'<svg viewBox="0 0 {W} {H}" role="img" xmlns="http://www.w3.org/2000/svg" '
    'aria-label="Home health capacity and scheduling, detailed current-state flow in the original '
    'five-column design with corrections. Columns: clinician scheduling workflow, capacity read, '
    'scheduling and assignment, coordination, delivery and outcomes. A grey clean path runs through '
    'the middle from the admitted referral to the delivered visit. Corrections: scheduler steps are '
    'yellow because a person works them, visit confirmation coordination is run by the clinician the day before, patient '
    'preferences are a coordination note, the five dispositions are chosen the day before, the '
    'missed visit runs a 48-hour compliance chain, and pending-auth visits are invisible to the '
    'capacity read.">')
add('<defs><marker id="ar" viewBox="0 0 10 8" refX="9" refY="4" markerWidth="8" markerHeight="6.5" '
    f'orient="auto-start-reverse"><polygon points="0,0 10,4 0,8" fill="{INK}"/></marker></defs>')
add(f'<rect x="0" y="0" width="{W}" height="{H}" fill="#FBFBF8"/>')

# ---------------- masthead (centered, like the original) ----------------
lbl(W/2, 52, "Home Health Capacity & Scheduling — Detailed Flow", "middle", "title")
lbl(W/2, 82, "Continues the Home Health Intake Reset — from the PCC clinician scheduling workflow forward"
    "   ·   current state, corrected 18 Aug 2026", "middle", "deck")

legend = [("PCC (Scheduler)", C["pcc"]), ("HCHB", C["hchb"]), ("ED / DCS", C["dcs"]),
          ("Clinician", C["clin"]), ("Per Diem / Float", C["float_"]), ("Patient", C["pat"]),
          ("Insurance & Auth", C["auth"]), ("Branch Leadership", C["lead"])]
tw = sum(34 + 8.2*len(n) + 42 for n, _ in legend) - 42
lx = (W - tw)/2
for name, col in legend:
    add(f'<circle cx="{lx+13}" cy="122" r="13" fill="{col}"/>')
    lbl(lx+34, 128, name, cls="leg")
    lx += 34 + 8.2*len(name) + 42

# ---------------- columns ----------------
CT, CB = 170, 1660                    # column top and bottom
NC, CGAP, M = 5, 22, 36
colw = (W - 2*M - (NC-1)*CGAP)/NC     # 486.4
cols = [M + i*(colw+CGAP) for i in range(NC)]
titles = [("Clinician Scheduling Workflow", C["hchb"]),
          ("Capacity Read", "#2E86AB"),
          ("Scheduling & Assignment", C["pcc"]),
          ("Coordination", C["pat"]),
          ("Delivery & Outcomes", C["dcs"])]
for i, (t, col) in enumerate(titles):
    add(f'<rect x="{cols[i]}" y="{CT}" width="{colw}" height="{CB-CT}" rx="4" fill="none" '
        f'stroke="{col}" stroke-width="1.6"/>')
    add(f'<text x="{cols[i]+16}" y="{CT+30}" class="colt" fill="{col}">{esc(t)}</text>')

BW2, BH2 = colw-96, 58                # standard block inside a column
def cx(i): return cols[i] + (colw-BW2)/2

# ---------------- the clean-path spine ----------------
SY, SH2 = 830, 170
add(f'<rect x="{M-14}" y="{SY}" width="{W-2*(M-14)}" height="{SH2}" fill="#DBDBD6" opacity=".55"/>')
lbl(M+2, SY+24, "Admitted Episodic Referral — Ready to Schedule → Delivered Visit  (the clean path)",
    cls="spine")
sc = SY + SH2/2 + 12                  # spine centreline
SBW, SBH = 300, 74

s_pcc   = cols[0] + 96
s_read  = cols[1] + 30
d_cap   = cols[1] + 400
d_match = cols[2] + 66
s_asn   = cols[2] + 152
s_dbc   = cols[3] + 26
d_conf  = cols[3] + 400
s_del   = cols[4] + 40
d_stat  = cols[4] + 428

block(s_pcc, sc-SBH/2, SBW, SBH, C["pcc"], ["PCC completes clinician", "scheduling workflow"])
block(s_read, sc-SBH/2, SBW, SBH, C["pcc"], ["Read open capacity — day ·", "week · discipline · territory"])
diamond(d_cap, sc, ["Capacity", "available?"])
diamond(d_match, sc, ["Clean", "match?"])
block(s_asn, sc-SBH/2, SBW, SBH, C["pcc"], ["Assign visit — clinician,", "day, sequence — one pass"])
diamond(d_conf, sc, ["Confirmed?"])
block(s_del, sc-SBH/2, SBW, SBH, C["clin"], ["Visit delivered — docu-", "mented, OASIS locked"])
diamond(d_stat, sc, ["Visit", "status?"])

arrow(s_pcc+SBW, sc, s_read-6, sc)
arrow(s_read+SBW, sc, d_cap-75-6, sc)
path(f"M {d_cap+75} {sc} L {d_match-75-6} {sc}", label="Yes", lx=(d_cap+d_match)/2, ly=sc-12)
path(f"M {d_match+75} {sc} L {s_asn-6} {sc}", label="Yes", lx=(d_match+75+s_asn)/2, ly=sc-12)
arrow(s_asn+SBW, sc, d_conf-75-6, sc)
path(f"M {d_conf+75} {sc} L {s_del-6} {sc}", label="Yes", lx=(d_conf+75+s_del)/2, ly=sc-30)
add(f'<rect x="{d_conf+79}" y="{sc-18}" width="{s_del-d_conf-85}" height="36" rx="18" fill="#FFFFFF" '
    f'stroke="{C["clin"]}" stroke-width="1.8"/>')
add(f'<text x="{(d_conf+79+s_del-6)/2}" y="{sc+5}" class="ct" text-anchor="middle" '
    f'fill="{C["clin"]}">Accept</text>')
arrow(s_del+SBW, sc, d_stat-75-6, sc)

# ==================== COLUMN 1 — feeders ====================
y = CT + 56
tag(cx(0), y, BW2, 56, ["From Intake: signed orders /", "485 + F2F on file"])
arrow(cols[0]+colw/2, y+56, cols[0]+colw/2, y+96)
y += 102
tag(cx(0), y, BW2, 56, ["Ordered frequency & visit types", "(SOC / ROC / recert / add-on)"])
arrow(cols[0]+colw/2, y+56, cols[0]+colw/2, y+96)
y += 102
block(cx(0), y, BW2, BH2, C["pcc"], ["Welcome / readiness", "call by PCC"], badge="THE ONE JUDGMENT CALL")
lbl(cols[0]+colw/2, y+BH2+22, "is the patient actually home? not still", "middle", "note")
lbl(cols[0]+colw/2, y+BH2+40, "inpatient · not deferring admission", "middle", "note")
arrow(cols[0]+colw/2, y+BH2+50, cols[0]+colw/2, y+BH2+86)
y += BH2 + 92
block(cx(0), y, BW2, BH2, C["pcc"], ["PCC creates scheduling", "grid entry"])
arrow(cols[0]+colw/2, y+BH2, cols[0]+colw/2, sc-SBH/2-6)

# column 1 — below spine
y1 = SY + SH2 + 56
diamond(cols[0]+colw/2, y1+94, ["SOC / ROC", "urgent?"], w=190, h=120)
path(f"M {cols[0]+colw/2} {y1+154} L {cols[0]+colw/2} {y1+190}",
     label="Yes", lx=cols[0]+colw/2+14, ly=y1+180, anchor="start")
block(cx(0), y1+196, BW2, BH2, C["dcs"], ["Priority flag", "to scheduling"])
lbl(cols[0]+colw/2, y1+196+BH2+26, "every SOC / ROC is already time-sensitive —", "middle", "note")
lbl(cols[0]+colw/2, y1+196+BH2+44, "seen within 48 hours under Medicare. Urgent =", "middle", "note")
lbl(cols[0]+colw/2, y1+196+BH2+62, "clinical diagnosis or another factor deserving priority", "middle", "note")
pfy = y1+196+BH2/2
path(f"M {cx(0)+BW2} {pfy} L 533 {pfy} L 533 1620 L 1073 1620 L 1073 {SY+SH2+110+BH2/2} "
     f"L {cols[2]+(colw-BW2)/2-6} {SY+SH2+110+BH2/2}", dash=True,
     label="priority to scheduling", lx=810, ly=1610)
path(f"M {cols[0]+colw/2} {sc+SBH/2} L {cols[0]+colw/2} {y1+28}")

# ==================== COLUMN 2 ====================
y = CT + 56
tag(cx(1), y, BW2, 56, ["Roster — assessing (RN/PT/OT)", "vs assistant (LPN/PTA/HHA)"])
arrow(cols[1]+colw/2, y+56, cols[1]+colw/2, y+96)
y += 102
tag(cx(1), y, BW2, 56, ["FTE · per-diem · PTO ·", "availability"])
arrow(cols[1]+colw/2, y+56, cols[1]+colw/2, y+96)
y += 102
block(cx(1), y, BW2, BH2, C["hchb"], ["Compute committed", "load (points)"])
arrow(cols[1]+colw/2, y+BH2, cols[1]+colw/2, y+BH2+40)
y += BH2 + 46
block(cx(1), y, BW2, BH2, C["pcc"], ["Assessing capacity", "by discipline"])
arrow(cols[1]+colw/2, y+BH2, cols[1]+colw/2, sc-SBH/2-6)
# pending-auth distortion
block(cx(1), y+BH2+52, BW2, 54, C["auth"],
      ["Pending-auth visits invisible —", "not on calendar, not counted"], small=True)
path(f"M {cx(1)+BW2/2-90} {y+BH2+52} L {cx(1)+BW2/2-90} {y+BH2+8}", dash=True)
lbl(cols[1]+colw/2, y+BH2+52+54+20, "the read excludes what it cannot see", "middle", "note")

# column 2 — below spine
y2 = SY + SH2 + 56
block(cx(1), y2, BW2, BH2, C["lead"], ["Branch leadership review —", "reopen zip · adjust · defer"],
      badge="WHEN CAPACITY TIGHTENS")
path(f"M {d_cap} {sc+56} L {d_cap} {y2-40} L {cols[1]+colw/2} {y2-40} L {cols[1]+colw/2} {y2-6}",
     dash=True, label="No", lx=d_cap+14, ly=sc+80, anchor="start")
lbl(cols[1]+colw/2, y2+BH2+22, "territory alignment · referral acceptance", "middle", "note")
arrow(cols[1]+colw/2, y2+BH2+32, cols[1]+colw/2, y2+BH2+64)
y2b = y2 + BH2 + 70
block(cx(1), y2b, BW2, BH2, C["float_"], ["Engage per-diem / float —", "SOCs or coverage visits"])
lbl(cols[1]+colw/2, y2b+BH2+22, "no territory, on purpose — the", "middle", "note")
lbl(cols[1]+colw/2, y2b+BH2+40, "targeted capacity instrument", "middle", "note")
path(f"M {cols[1]+colw/2} {y2b+BH2+50} L {cols[1]+colw/2} {y2b+BH2+86}",
     label="none left", lx=cols[1]+colw/2+14, ly=y2b+BH2+74, anchor="start")
oval(cols[1]+colw/2, y2b+BH2+86+44, 170, 40, C["dcs"], ["Defer / waitlist /", "refer out"])


# ==================== COLUMN 3 ====================
y = CT + 56
tag(cx(2), y, BW2, 56, ["Routing / GPS — home base,", "mileage, sequence"])
lbl(cols[2]+colw/2, y+56+18, "straight-line today — not drive time", "middle", "note")
arrow(cols[2]+colw/2, y+56+26, cols[2]+colw/2, y+96)
y += 102
block(cx(2), y, BW2, BH2, C["hchb"], ["Discipline / role", "match (gate)"])
arrow(cols[2]+colw/2, y+BH2, cols[2]+colw/2, y+BH2+32)
y += BH2 + 38
block(cx(2), y, BW2, BH2, C["pcc"], ["Territory list — zip code", "reference"])
arrow(cols[2]+colw/2, y+BH2, cols[2]+colw/2, y+BH2+32)
y += BH2 + 38
block(cx(2), y, BW2, BH2, C["pcc"], ["Specialty competency", "match"])
arrow(cols[2]+colw/2, y+BH2, cols[2]+colw/2, y+BH2+32)
y += BH2 + 38
block(cx(2), y, BW2, BH2, C["pcc"], ["Continuity — prefer", "same clinician"])
arrow(cols[2]+colw/2, y+BH2, cols[2]+colw/2, y+BH2+32)
y += BH2 + 38
block(cx(2), y, BW2, BH2, C["pcc"], ["Reads patient preferences — coordination", "note: caregiver · window · day-of-week"],
      small=True, badge="WAS A PATIENT LANE")
arrow(cols[2]+colw/2, y+BH2, cols[2]+colw/2, sc-SBH/2-6)
lbl(cols[2]+colw/2, y+BH2+30, "the information is housed in HCHB — a person wrote", "middle", "note")
lbl(cols[2]+colw/2, y+BH2+48, "it, and the scheduler acts on it before selecting", "middle", "note")

# column 3 — below spine
y3 = SY + SH2 + 110
path(f"M {d_match} {sc+56} L {d_match} {y3-6}", dash=True, label="No",
     lx=d_match+14, ly=sc+80, anchor="start")
block(cx(2), y3, BW2, BH2, C["pcc"], ["Front-load early visits", "(protect LUPA floor)"])
arrow(cols[2]+colw/2, y3+BH2, cols[2]+colw/2, y3+BH2+40)
y3b = y3 + BH2 + 46
block(cx(2), y3b, BW2, BH2, C["pcc"], ["Resolve — reassign ·", "resequence · escalate"])
arrow(cols[2]+colw/2, y3b+BH2, cols[2]+colw/2, y3b+BH2+40)
y3c = y3b + BH2 + 46
block(cx(2), y3c, BW2, BH2, C["clin"], ["Clinician receives", "schedule"])
block(cx(2), y3c+BH2+52, BW2, 54, C["auth"],
      ["Auth gate — checked per visit;", "no auth → the visit sits pending"], small=True)
path(f"M {cx(2)} {y3c+BH2+52+27} L {cx(1)+BW2+24} {y3c+BH2+52+27} "
     f"L {cx(1)+BW2+24} 704", dash=True)

# ==================== COLUMN 4 ====================
y = CT + 300
block(cx(3), y, BW2, BH2, C["clin"], ["Visit confirmation coordination", "(SMS / voice) — day before"])
arrow(cols[3]+colw/2, y+BH2, cols[3]+colw/2, y+BH2+40)
y += BH2 + 46
block(cx(3), y, BW2, BH2, C["pat"], ["Patient confirms /", "negotiates"])
lbl(cols[3]+colw/2, y+BH2+22, "hard constraints get built around —", "middle", "note")
lbl(cols[3]+colw/2, y+BH2+40, "soft preferences are worth holding", "middle", "note")
path(f"M {cols[3]+colw/2} {y+BH2+50} L {cols[3]+colw/2} {sc-SBH/2-42} "
     f"L {d_conf} {sc-SBH/2-42} L {d_conf} {sc-56-6}")

# column 4 — below spine: dispositions then recovery
y4 = SY + SH2 + 46
lbl(cols[3]+16, y4+6, "NOT CONFIRMED — THE OTHER DISPOSITIONS", cls="pnl")
dch = [("Resched.", C["clin"]), ("Reassign", C["pcc"]),
       ("Miss", C["dcs"]), ("Decline", C["pcc"])]
dxx = cols[3]+16
for t, col in dch:
    wch = 7.6*len(t) + 26
    add(f'<rect x="{dxx}" y="{y4+16}" width="{wch}" height="36" rx="18" fill="#FFFFFF" '
        f'stroke="{col}" stroke-width="1.8"/>')
    add(f'<text x="{dxx+wch/2}" y="{y4+38}" class="ct" text-anchor="middle" fill="{col}">{esc(t)}</text>')
    dxx += wch + 8
lbl(cols[3]+16, y4+70, "selected in HCHB · reassign returns with a plan, decline without one", "start", "note")
lbl(cols[3]+16, y4+88, "decline is the least used — some clinicians are instructed never to use it", "start", "note")
path(f"M {d_conf} {sc+56} L {d_conf} {y4-34} L {cols[3]+8} {y4-34} L {cols[3]+8} {y4+34} "
     f"L {cols[3]+16-6} {y4+34}", dash=True, label="No",
     lx=d_conf-14, ly=sc+82, anchor="end")

y4b = y4 + 116
add(f'<rect x="{cx(3)}" y="{y4b}" width="{BW2}" height="{BH2}" rx="6" fill="{C["dcs"]}"/>')
add(f'<rect x="{cx(3)+BW2/2}" y="{y4b}" width="{BW2/2}" height="{BH2}" rx="6" fill="{C["pcc"]}"/>')
add(f'<text x="{cx(3)+BW2/2}" y="{y4b+25}" class="bt" fill="#fff" text-anchor="middle">Call-out coverage —</text>')
add(f'<text x="{cx(3)+BW2/2}" y="{y4b+43}" class="bt" fill="#fff" text-anchor="middle">DCS + scheduler together</text>')
arrow(cols[3]+colw/2, y4b+BH2, cols[3]+colw/2, y4b+BH2+38)
y4c = y4b + BH2 + 44
block(cx(3), y4c, BW2, 66, C["pcc"], ["Scheduler coordinates coverage —", "call · text · Teams — with FT", "or per-diem clinicians"], small=True)
arrow(cols[3]+colw/2, y4c+66, cols[3]+colw/2, y4c+66+38)
y4d = y4c + 66 + 44
block(cx(3), y4d, BW2, 66, C["pcc"], ["Scheduler reassigns to another", "clinician — or moves the visit", "to another day"], small=True)
gap45 = cols[3]+colw + CGAP/2
path(f"M {cx(3)+BW2} {y4d+33} L {gap45} {y4d+33} L {gap45} {sc+SBH/2+6}",
     dash=True, label="rebook", lx=gap45-8, ly=1200, anchor="end")

# ==================== COLUMN 5 ====================
y = CT + 420
block(cx(4), y, BW2, BH2, C["clin"], ["Visit in progress", "(EVV / clock-in)"])
lbl(cols[4]+colw/2, y+BH2+22, "Citrix sync lags — the status the office", "middle", "note")
lbl(cols[4]+colw/2, y+BH2+40, "sees can be hours behind", "middle", "note")
arrow(cols[4]+colw/2, y+BH2+50, cols[4]+colw/2, sc-SBH/2-6)

# column 5 — below spine
y5 = SY + SH2 + 56
block(cx(4), y5, BW2, BH2, C["clin"], ["Documentation", "pending"])
path(f"M {d_stat} {sc+56} L {d_stat} {y5-24} L {cols[4]+colw/2} {y5-24} L {cols[4]+colw/2} {y5-6}",
     dash=True, label="not documented", lx=d_stat-88, ly=sc+82, anchor="middle")
lbl(cols[4]+colw/2, y5+BH2+20, "scheduled → documentation pending → missed", "middle", "note")
arrow(cols[4]+colw/2, y5+BH2+30, cols[4]+colw/2, y5+BH2+60)
y5b = y5 + BH2 + 66
block(cx(4), y5b, BW2, BH2, C["clin"], ["Missed visit —", "clinician documents"])
arrow(cols[4]+colw/2, y5b+BH2, cols[4]+colw/2, y5b+BH2+36)
y5c = y5b + BH2 + 42
block(cx(4), y5c, BW2, BH2, C["pcc"], ["Scheduler workflow —", "notify MD within 48h"])
lbl(cols[4]+colw/2, y5c+BH2+20, "Medicare requirement and an HCHB hard stop;", "middle", "note")
lbl(cols[4]+colw/2, y5c+BH2+38, "late → workflow generates to the DCS", "middle", "note")
arrow(cols[4]+colw/2, y5c+BH2+48, cols[4]+colw/2, y5c+BH2+78)
y5d = y5c + BH2 + 84
block(cx(4), y5d, BW2, BH2, C["pcc"], ["Rebook within window ·", "recover / front-load"])
# completed branch — up to the revenue oval
oval(cols[4]+colw/2+10, CT+250, 180, 42, None,
     ["Period revenue realized", "(PDGM 30-day · timely NOA)"], outline=INK)
path(f"M {d_stat} {sc-56} L {d_stat} {CT+250+6}", dash=True,
     label="completed", lx=d_stat-14, ly=sc-96, anchor="end")
# KPI tag + feedback
tag(cx(4), y5d+BH2+42, BW2, 50, ["KPIs update → feedback to capacity"])
path(f"M {cols[4]+colw/2} {y5d+BH2+42+50} L {cols[4]+colw/2} 1640 L 566 1640 "
     f"L 566 984 L 640 984 L 640 {sc+SBH/2+6}",
     dash=True, label="KPIs feed the capacity re-read", lx=1300, ly=1630)

add(f'<line x1="{M}" y1="{H-64}" x2="{W-M}" y2="{H-64}" stroke="{RULE}" stroke-width="1.4"/>')
lbl(M, H-34, "Compassus Home Health · Capacity & Scheduling — current state; nothing on this sheet "
    "is a proposal. Colour = actor; a workflow item in HCHB worked by a person carries the person's "
    "colour.", cls="foot")
lbl(W-M, H-34, "Continues: Home Health Intake Reset · Page 2", "end", "foot")
add('</svg>')

open("/tmp/claude-0/-home-user/f0ef1ecc-a04c-5098-a365-4b559e397089/scratchpad/gen/detail.svg",
     "w", encoding="utf-8").write("\n".join(out))
print("emitted", len(out), "| canvas", W, "x", H, "| ratio", round(W/H, 3))
