# -*- coding: utf-8 -*-
"""Generate the simplified DCS / Scheduler flow map as inline SVG."""

C = dict(pcc="#C6A01F", hchb="#795CA7", dcs="#792E2E", clin="#2E599D",
         pd="#795933", pat="#4E8A5B", auth="#DF751D", lead="#1A1A1A")
INK, MUT, RULE, BAND = "#1B211E", "#5A6560", "#C9CCC5", "#E9E9E5"

out = []
def add(s): out.append(s)

def esc(t):
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

def block(x, y, w, h, fill, lines, tier="spine", badge=None):
    """tier: spine (full) | ex (exception, smaller) """
    add(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="4" fill="{fill}"/>')
    fs = 13 if tier == "spine" else 11
    lh = 15 if tier == "spine" else 13
    cy = y + h/2 - (len(lines)-1)*lh/2 + 4
    for i, ln in enumerate(lines):
        add(f'<text x="{x+w/2}" y="{cy+i*lh}" class="bt{"" if tier=="spine" else " s"}" '
            f'text-anchor="middle">{esc(ln)}</text>')
    if badge:
        bw = 7.6*len(badge)+12
        add(f'<rect x="{x+w-bw-6}" y="{y-11}" width="{bw}" height="17" rx="8.5" '
            f'fill="#FFFFFF" stroke="{fill}" stroke-width="1.4"/>')
        add(f'<text x="{x+w-bw/2-6}" y="{y+1}" class="bdg" text-anchor="middle" '
            f'fill="{fill}">{esc(badge)}</text>')

def diamond(cx, cy, w, h, lines):
    add(f'<polygon points="{cx},{cy-h/2} {cx+w/2},{cy} {cx},{cy+h/2} {cx-w/2},{cy}" '
        f'fill="#FFFFFF" stroke="{INK}" stroke-width="1.4"/>')
    lh = 12
    y0 = cy - (len(lines)-1)*lh/2 + 3.5
    for i, ln in enumerate(lines):
        add(f'<text x="{cx}" y="{y0+i*lh}" class="dt" text-anchor="middle">{esc(ln)}</text>')

def chip(x, y, w, h, lines, stroke, fill="#FFFFFF"):
    add(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{h/2}" fill="{fill}" '
        f'stroke="{stroke}" stroke-width="1.5"/>')
    lh = 12
    y0 = y + h/2 - (len(lines)-1)*lh/2 + 3.5
    for i, ln in enumerate(lines):
        add(f'<text x="{x+w/2}" y="{y0+i*lh}" class="ct" text-anchor="middle" '
            f'fill="{stroke}">{esc(ln)}</text>')

def arrow(x1, y1, x2, y2, dash=False, label=None, lx=None, ly=None, anchor="middle"):
    d = ' stroke-dasharray="5 4" opacity=".65"' if dash else ''
    add(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" class="ln"{d} marker-end="url(#ar)"/>')
    if label:
        add(f'<text x="{lx}" y="{ly}" class="lb" text-anchor="{anchor}">{esc(label)}</text>')

def path(dd, dash=False, label=None, lx=None, ly=None):
    d = ' stroke-dasharray="5 4" opacity=".65"' if dash else ''
    add(f'<path d="{dd}" fill="none" class="ln"{d} marker-end="url(#ar)"/>')
    if label:
        add(f'<text x="{lx}" y="{ly}" class="lb" text-anchor="middle">{esc(label)}</text>')

W, H = 1600, 1010
add(f'<svg viewBox="0 0 {W} {H}" role="img" xmlns="http://www.w3.org/2000/svg" '
    f'aria-label="Simplified DCS and scheduler flow: five triggers feed one repeating '
    f'pattern of clinician submission, DCS approval per discipline, auth gate and scheduler '
    f'assignment; missed visits run a separate 48-hour compliance chain.">')
add('<defs><marker id="ar" viewBox="0 0 10 8" refX="9" refY="4" markerWidth="9" '
    'markerHeight="7" orient="auto-start-reverse">'
    f'<polygon points="0,0 10,4 0,8" fill="{INK}"/></marker></defs>')

# ---------- legend ----------
leg = [("PCC / Scheduler", C["pcc"]), ("Scheduling System (HCHB)", C["hchb"]),
       ("DCS", C["dcs"]), ("Clinician", C["clin"]), ("Insurance & Auth", C["auth"])]
lx = 40
for name, col in leg:
    add(f'<circle cx="{lx+11}" cy="46" r="11" fill="{col}"/>')
    add(f'<text x="{lx+29}" y="50" class="leg">{esc(name)}</text>')
    lx += 29 + 7.2*len(name) + 34
# size key
add(f'<text x="{W-40}" y="34" class="key" text-anchor="end">SIZE = WEIGHT</text>')
add(f'<text x="{W-40}" y="52" class="keys" text-anchor="end">'
    'large = every time &#183; small = conditional &#183; pill = watch condition</text>')
add(f'<line x1="40" y1="76" x2="{W-40}" y2="76" stroke="{RULE}" stroke-width="1"/>')

# ---------- band A ----------
BAY, BAH = 140, 170
add(f'<rect x="270" y="{BAY}" width="{W-310}" height="{BAH}" rx="8" fill="{BAND}"/>')
add(f'<text x="288" y="{BAY+24}" class="band">ORDER &#8594; APPROVAL &#8594; ASSIGNMENT '
    '&#8212; the repeating pattern</text>')

by, bh = BAY + 46, 66
xs = [286, 481, 676, 831, 1026, 1181, 1376]
bw = 168
block(xs[0], by, bw, bh, C["clin"], ["Clinician submits", "plan of care / order"])
block(xs[1], by, bw, bh, C["dcs"], ["DCS reviews &", "approves"], badge="x N disciplines")
diamond(xs[2]+64, by+bh/2, 128, 76, ["Approved?"])
block(xs[3], by, bw, bh, C["hchb"], ["Visits generate", "in HCHB"])
diamond(xs[4]+64, by+bh/2, 128, 76, ["Auth on", "file?"])
block(xs[5], by, bw, bh, C["pcc"], ["Scheduler assigns", "to care team"], badge="x N disciplines")
block(xs[6], by, bw, bh, C["clin"], ["Visits on clinician", "calendar"])

cy = by + bh/2
for a, b in [(xs[0]+bw, xs[1]), (xs[1]+bw, xs[2]), (xs[2]+128, xs[3]),
             (xs[3]+bw, xs[4]), (xs[4]+128, xs[5]), (xs[5]+bw, xs[6])]:
    arrow(a, cy, b-4, cy)
add(f'<text x="{xs[3]-8}" y="{cy-9}" class="lb" text-anchor="end">Yes</text>')
add(f'<text x="{xs[5]-8}" y="{cy-9}" class="lb" text-anchor="end">Yes</text>')

# ---------- triggers ----------
trg = ["Start of care", "Add-on order (in 60-day cert)", "Recertification",
       "Resumption of care"]
ty0, th, tg = cy - (4*44 + 3*12)/2, 44, 12
for i, t in enumerate(trg):
    y = ty0 + i*(th+tg)
    chip(40, y, 210, th, [t], INK)
    path(f"M 250 {y+th/2} L 268 {y+th/2} L 268 {cy} L {xs[0]-5} {cy}")
add(f'<text x="40" y="{ty0-16}" class="trg">TRIGGERS</text>')

# ---------- exceptions under A ----------
exy, exh, exw = BAY + BAH + 44, 46, 168
block(xs[1], exy, exw, exh, C["dcs"], ["QA backlog", "visits compress"], tier="ex")
block(xs[2]-20, exy, exw, exh, C["clin"], ["Returned to clinician", "for correction"], tier="ex")
block(xs[4]-20, exy, exw, exh, C["auth"], ["Pending auth", "not on calendar, not counted"], tier="ex")
path(f"M {xs[1]+44} {by+bh} L {xs[1]+44} {exy-5}", dash=True)
path(f"M {xs[2]+64} {by+bh/2+38} L {xs[2]+64} {exy-5}", dash=True, label="No",
     lx=xs[2]+78, ly=exy-16)
path(f"M {xs[4]+64} {by+bh/2+38} L {xs[4]+64} {exy-5}", dash=True, label="No",
     lx=xs[4]+78, ly=exy-16)

# ---------- episode budget panel ----------
py, ph = 452, 118
add(f'<rect x="{xs[1]}" y="{py}" width="{1082}" height="{ph}" rx="8" fill="none" '
    f'stroke="{RULE}" stroke-width="1.4" stroke-dasharray="6 5"/>')
add(f'<text x="{xs[1]+18}" y="{py+26}" class="pnl">EPISODE VISIT BUDGET '
    '&#8212; set at plan-of-care approval, steered by DCS</text>')
chip(xs[1]+18, py+44, 252, 34, ["LUPA floor · too few visits"], C["dcs"])
chip(xs[1]+294, py+44, 268, 34, ["Utilisation ceiling · visits beyond need"], C["dcs"])
add(f'<text x="{xs[1]+590}" y="{py+66}" class="note">Fixed 30-day PDGM payment: below the floor the '
    'period pays per visit;</text>')
add(f'<text x="{xs[1]+590}" y="{py+81}" class="note">above the ceiling extra visits earn nothing '
    'and consume capacity.</text>')
path(f"M {xs[1]+134} {py-5} L {xs[1]+134} {by+bh+6}", dash=True)

# ---------- band B ----------
BBY, BBH = 640, 170
add(f'<rect x="270" y="{BBY}" width="775" height="{BBH}" rx="8" fill="{BAND}"/>')
add(f'<text x="288" y="{BBY+24}" class="band">MISSED VISIT &#8212; the compliance chain</text>')
b2y = BBY + 46
c2 = b2y + bh/2
block(xs[0], b2y, bw, bh, C["clin"], ["Clinician documents", "missed visit"])
block(xs[1], b2y, bw, bh, C["pcc"], ["Scheduler workflow", "notify MD"])
diamond(xs[2]+64, c2, 138, 78, ["MD notified", "within 48h?"])
block(xs[3], b2y, bw, bh, C["hchb"], ["Documented", "in HCHB"])
arrow(xs[0]+bw, c2, xs[1]-4, c2)
arrow(xs[1]+bw, c2, xs[2]-6, c2)
arrow(xs[2]+134, c2, xs[3]-4, c2)
add(f'<text x="{xs[3]-8}" y="{c2-9}" class="lb" text-anchor="end">Yes</text>')
chip(40, c2-22, 210, 44, ["Missed visit"], INK)
path(f"M 250 {c2} L {xs[0]-5} {c2}")
add(f'<text x="40" y="{c2-38}" class="trg">TRIGGER</text>')
block(xs[2]-20, BBY+BBH+44, exw, exh, C["dcs"], ["DCS workflow", "48h breach"], tier="ex")
path(f"M {xs[2]+64} {c2+39} L {xs[2]+64} {BBY+BBH+39}", dash=True, label="No",
     lx=xs[2]+78, ly=BBY+BBH+28)

add(f'<line x1="40" y1="{H-58}" x2="{W-40}" y2="{H-58}" stroke="{RULE}" stroke-width="1"/>')
add(f'<text x="40" y="{H-34}" class="foot">Compassus Home Health &#183; simplified view &#183; '
    'a strict subset of the full swimlane</text>')
add(f'<text x="{W-40}" y="{H-34}" class="foot" text-anchor="end">DCS and Scheduler only</text>')
add('</svg>')

open("/tmp/claude-0/-home-user/f0ef1ecc-a04c-5098-a365-4b559e397089/scratchpad/gen/flow.svg",
     "w", encoding="utf-8").write("\n".join(out))
print("blocks emitted:", len(out))
