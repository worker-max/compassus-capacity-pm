# -*- coding: utf-8 -*-
"""Simplified DCS / Scheduler flow map — two passes plus the missed-visit chain."""

C = dict(pcc="#C6A01F", hchb="#795CA7", dcs="#792E2E", clin="#2E599D",
         pd="#795933", pat="#4E8A5B", auth="#DF751D", lead="#1A1A1A")
INK, MUT, RULE, BAND = "#1B211E", "#5A6560", "#C9CCC5", "#E9E9E5"

out = []
def add(s): out.append(s)
def esc(t): return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

def block(x, y, w, h, fill, lines, tier="spine", badge=None):
    add(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="4" fill="{fill}"/>')
    fs, lh = (13, 15) if tier == "spine" else (11, 13)
    cy = y + h/2 - (len(lines)-1)*lh/2 + 4
    for i, ln in enumerate(lines):
        cls = "bt" if tier == "spine" else "bt s"
        add(f'<text x="{x+w/2}" y="{cy+i*lh}" class="{cls}" text-anchor="middle">{esc(ln)}</text>')
    if badge:
        bw = 7.6*len(badge)+12
        add(f'<rect x="{x+w-bw-6}" y="{y-11}" width="{bw}" height="17" rx="8.5" fill="#FFFFFF" '
            f'stroke="{fill}" stroke-width="1.4"/>')
        add(f'<text x="{x+w-bw/2-6}" y="{y+1}" class="bdg" text-anchor="middle" fill="{fill}">{esc(badge)}</text>')

def diamond(cx, cy, w, h, lines):
    add(f'<polygon points="{cx},{cy-h/2} {cx+w/2},{cy} {cx},{cy+h/2} {cx-w/2},{cy}" '
        f'fill="#FFFFFF" stroke="{INK}" stroke-width="1.4"/>')
    y0 = cy - (len(lines)-1)*12/2 + 3.5
    for i, ln in enumerate(lines):
        add(f'<text x="{cx}" y="{y0+i*12}" class="dt" text-anchor="middle">{esc(ln)}</text>')

def chip(x, y, w, h, lines, stroke, fill="#FFFFFF"):
    add(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{min(h/2,22)}" fill="{fill}" '
        f'stroke="{stroke}" stroke-width="1.5"/>')
    y0 = y + h/2 - (len(lines)-1)*13/2 + 4
    for i, ln in enumerate(lines):
        add(f'<text x="{x+w/2}" y="{y0+i*13}" class="ct" text-anchor="middle" fill="{stroke}">{esc(ln)}</text>')

def arrow(x1, y1, x2, y2, dash=False):
    d = ' stroke-dasharray="5 4" opacity=".65"' if dash else ''
    add(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" class="ln"{d} marker-end="url(#ar)"/>')

def conn(dd):
    add(f'<path d="{dd}" fill="none" class="ln"/>')

def path(dd, dash=False, label=None, lx=None, ly=None, anchor="middle"):
    d = ' stroke-dasharray="5 4" opacity=".65"' if dash else ''
    add(f'<path d="{dd}" fill="none" class="ln"{d} marker-end="url(#ar)"/>')
    if label:
        add(f'<text x="{lx}" y="{ly}" class="lb" text-anchor="{anchor}">{esc(label)}</text>')

def lbl(x, y, t, anchor="start", cls="lb"):
    add(f'<text x="{x}" y="{y}" class="{cls}" text-anchor="{anchor}">{esc(t)}</text>')

W, H = 1600, 1250
add(f'<svg viewBox="0 0 {W} {H}" role="img" xmlns="http://www.w3.org/2000/svg" '
    'aria-label="Start of care and resumption of care run a referral pass first: office verifies, '
    'DCS reviews the referral, the scheduler books the SOC or ROC visit and the discipline '
    'evaluations. All triggers then converge on the discipline plan-of-care pattern: clinician '
    'submits, DCS approves per discipline, auth gate, scheduler assigns. Missed visits run a '
    'separate 48-hour compliance chain.">')
add('<defs><marker id="ar" viewBox="0 0 10 8" refX="9" refY="4" markerWidth="9" markerHeight="7" '
    f'orient="auto-start-reverse"><polygon points="0,0 10,4 0,8" fill="{INK}"/></marker></defs>')

# ---------------- legend ----------------
lx = 40
for name, col in [("PCC / Scheduler", C["pcc"]), ("Scheduling System (HCHB)", C["hchb"]),
                  ("DCS", C["dcs"]), ("Clinician", C["clin"]), ("Insurance & Auth", C["auth"])]:
    add(f'<circle cx="{lx+11}" cy="46" r="11" fill="{col}"/>')
    add(f'<text x="{lx+29}" y="50" class="leg">{esc(name)}</text>')
    lx += 29 + 7.2*len(name) + 34
lbl(W-40, 34, "SIZE = WEIGHT", "end", "key")
lbl(W-40, 52, "large = every time · small = conditional · pill = watch condition", "end", "keys")
add(f'<line x1="40" y1="76" x2="{W-40}" y2="76" stroke="{RULE}" stroke-width="1"/>')

xs = [286, 481, 676, 871, 1066, 1261, 1376]
bw, bh = 168, 66

# ---------------- PASS 1 ----------------
P1Y, PH = 100, 178
add(f'<rect x="270" y="{P1Y}" width="900" height="{PH}" rx="8" fill="{BAND}"/>')
lbl(288, P1Y+24, "PASS 1  ·  START OF CARE / RESUMPTION OF CARE — from the referral", cls="band")
p1y = P1Y + 52
c1 = p1y + bh/2
p1x, p1w = [286, 506, 726, 946], 190
block(p1x[0], p1y, p1w, bh, C["auth"], ["Office verifies", "eligibility"])
block(p1x[1], p1y, p1w, bh, C["dcs"], ["DCS reviews", "referral"])
block(p1x[2], p1y, p1w, bh, C["pcc"], ["Scheduler books", "SOC / ROC visit", "+ discipline evals"])
block(p1x[3], p1y, p1w, bh, C["clin"], ["Clinicians perform", "SOC / ROC", "+ eval visits"])
for a in range(3):
    arrow(p1x[a]+p1w, c1, p1x[a+1]-4, c1)
chip(40, c1-27, 210, 54, ["Referral arrives", "with initial orders"], INK)
arrow(250, c1, xs[0]-4, c1)
lbl(40, c1-42, "TRIGGER", cls="trg")

# ---------------- PASS 2 ----------------
P2Y = 392
add(f'<rect x="270" y="{P2Y}" width="{W-310}" height="{PH}" rx="8" fill="{BAND}"/>')
lbl(288, P2Y+24, "PASS 2  ·  DISCIPLINE PLAN OF CARE — the repeating pattern", cls="band")
p2y = P2Y + 52
c2 = p2y + bh/2
x2 = [286, 481, 676, 831, 1026, 1181, 1376]
block(x2[0], p2y, bw, bh, C["clin"], ["Clinician submits", "discipline POC / frequency"], badge="x N disciplines")
block(x2[1], p2y, bw, bh, C["dcs"], ["DCS reviews &", "approves"], badge="x N disciplines")
diamond(x2[2]+64, c2, 128, 76, ["Approved?"])
block(x2[3], p2y, bw, bh, C["hchb"], ["Visits generate", "in HCHB"])
diamond(x2[4]+64, c2, 128, 76, ["Auth on", "file?"])
block(x2[5], p2y, bw, bh, C["pcc"], ["Scheduler assigns", "to care team"], badge="x N disciplines")
block(x2[6], p2y, bw, bh, C["clin"], ["Visits on clinician", "calendar"])
for a, b in [(x2[0]+bw, x2[1]), (x2[1]+bw, x2[2]), (x2[2]+128, x2[3]),
             (x2[3]+bw, x2[4]), (x2[4]+128, x2[5]), (x2[5]+bw, x2[6])]:
    arrow(a, c2, b-4, c2)
lbl(x2[3]-8, c2-9, "Yes", "end")
lbl(x2[5]-8, c2-9, "Yes", "end")

# all three entry paths converge on one bus into Pass 2
BUS = 268
conn(f"M {p1x[3]+p1w/2} {p1y+bh} L {p1x[3]+p1w/2} {P1Y+PH+62} L {BUS} {P1Y+PH+62} L {BUS} {c2}")
lbl((p1x[3]+p1w/2 + BUS)/2, P1Y+PH+52,
    "after the eval visits, each discipline writes its own plan of care", "middle")
chip(30, c2-84, 226, 58, ["Recertification — OASIS recert", "visit, or non-OASIS recert eval"], INK)
chip(30, c2+26, 226, 58, ["Add-on order — status change:", "add, reduce or shift visits"], INK)
lbl(30, c2-100, "OTHER TRIGGERS", cls="trg")
conn(f"M 256 {c2-55} L {BUS} {c2-55} L {BUS} {c2}")
conn(f"M 256 {c2+55} L {BUS} {c2+55} L {BUS} {c2}")
arrow(BUS, c2, x2[0]-4, c2)
lbl(30, c2+100, "no OASIS · adds, reduces or redistributes visits", cls="note")
lbl(30, c2+114, "without changing the episode total", cls="note")

# ---------------- exceptions ----------------
exy, exh, exw = P2Y + PH + 46, 46, 168
block(x2[1], exy, exw, exh, C["dcs"], ["QA backlog", "visits compress"], tier="ex")
block(x2[2]-20, exy, exw, exh, C["clin"], ["Returned to clinician", "for correction"], tier="ex")
block(x2[4]-20, exy, exw, exh, C["auth"], ["Pending auth", "not on calendar, not counted"], tier="ex")
path(f"M {x2[1]+44} {p2y+bh} L {x2[1]+44} {exy-5}", dash=True)
path(f"M {x2[2]+64} {c2+38} L {x2[2]+64} {exy-5}", dash=True, label="No", lx=x2[2]+78, ly=exy-16)
path(f"M {x2[4]+64} {c2+38} L {x2[4]+64} {exy-5}", dash=True, label="No", lx=x2[4]+78, ly=exy-16)

# ---------------- episode budget ----------------
py, ph = exy + exh + 46, 118
add(f'<rect x="{x2[1]}" y="{py}" width="1082" height="{ph}" rx="8" fill="none" stroke="{RULE}" '
    'stroke-width="1.4" stroke-dasharray="6 5"/>')
lbl(x2[1]+18, py+26, "EPISODE VISIT BUDGET — set at plan-of-care approval, steered by DCS", cls="pnl")
chip(x2[1]+18, py+44, 252, 34, ["LUPA floor · too few visits"], C["dcs"])
chip(x2[1]+294, py+44, 268, 34, ["Utilisation ceiling · visits beyond need"], C["dcs"])
lbl(x2[1]+590, py+66, "Fixed 30-day PDGM payment: below the floor the period pays per visit;", cls="note")
lbl(x2[1]+590, py+81, "above the ceiling extra visits earn nothing and consume capacity.", cls="note")
path(f"M {x2[1]+134} {py-5} L {x2[1]+134} {p2y+bh+6}", dash=True)

# ---------------- missed visit ----------------
MVY = py + ph + 46
add(f'<rect x="270" y="{MVY}" width="775" height="{PH}" rx="8" fill="{BAND}"/>')
lbl(288, MVY+24, "MISSED VISIT — the compliance chain", cls="band")
m2y = MVY + 52
c3 = m2y + bh/2
block(x2[0], m2y, bw, bh, C["clin"], ["Clinician documents", "missed visit"])
block(x2[1], m2y, bw, bh, C["pcc"], ["Scheduler workflow", "notify MD"])
diamond(x2[2]+64, c3, 138, 78, ["MD notified", "within 48h?"])
block(x2[3], m2y, bw, bh, C["hchb"], ["Documented", "in HCHB"])
arrow(x2[0]+bw, c3, x2[1]-4, c3)
arrow(x2[1]+bw, c3, x2[2]-6, c3)
arrow(x2[2]+134, c3, x2[3]-4, c3)
lbl(x2[3]-8, c3-9, "Yes", "end")
chip(40, c3-22, 210, 44, ["Missed visit"], INK)
arrow(250, c3, x2[0]-4, c3)
lbl(40, c3-38, "TRIGGER", cls="trg")
block(x2[2]-20, MVY+PH+46, exw, exh, C["dcs"], ["DCS workflow", "48h breach"], tier="ex")
path(f"M {x2[2]+64} {c3+39} L {x2[2]+64} {MVY+PH+41}", dash=True, label="No", lx=x2[2]+78, ly=MVY+PH+30)

add(f'<line x1="40" y1="{H-58}" x2="{W-40}" y2="{H-58}" stroke="{RULE}" stroke-width="1"/>')
lbl(40, H-34, "Compassus Home Health · simplified view · a strict subset of the full swimlane", cls="foot")
lbl(W-40, H-34, "DCS and Scheduler only", "end", "foot")
add('</svg>')

open("/tmp/claude-0/-home-user/f0ef1ecc-a04c-5098-a365-4b559e397089/scratchpad/gen/flow.svg",
     "w", encoding="utf-8").write("\n".join(out))
print("emitted", len(out))
