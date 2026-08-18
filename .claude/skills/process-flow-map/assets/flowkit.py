# -*- coding: utf-8 -*-
"""flowkit — drawing primitives for Compassus process flow maps.

Canvas units are POINTS ON THE OUTPUT SHEET. A 16-unit label prints at 16pt.
Draw at sheet scale (2000–2900 wide), never at A4-and-shrink.

Usage:
    import sys; sys.path.insert(0, "<skill>/assets")
    from flowkit import *

    begin(2600, 1780, aria="...")
    masthead("COMPASSUS HOME HEALTH  ·  FLOW N", "Title", "deck line")
    legend([("PCC / Scheduler", C["pcc"]), ("Clinician", C["clin"])], x=1400)
    ...
    finish("out.svg")
"""

# ---------------------------------------------------------------- palette
# Colour = ACTOR. A workflow item in HCHB worked by a person carries the
# PERSON'S colour. Purple only where HCHB acts by itself.
C = dict(
    pcc="#C6A01F",      # PCC / Scheduler
    hchb="#795CA7",     # HCHB acting by itself
    dcs="#792E2E",      # ED / DCS
    clin="#2E599D",     # Clinician
    auth="#DF751D",     # Insurance & Auth
    intake="#1F6F78",   # Intake
    float_="#795933",   # Per Diem / Float
    pat="#4E8A5B",      # Patient
    lead="#1A1A1A",     # Branch Leadership (white text)
)
INK, MUT, RULE, BAND, TAG = "#1B211E", "#5A6560", "#C9CCC5", "#E9E9E5", "#E8EAED"
PAPER = "#FBFBF8"

# ---------------------------------------------------------------- geometry
BW, BH, GAP = 250, 90, 28       # standard block width / height / gap
SLOT = BW + GAP                 # one column slot on a banded sheet
BX, IX = 320, 350               # band left edge / first block inside a band

_out = []
_W = _H = 0


def add(s):
    _out.append(s)


def esc(t):
    return str(t).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def begin(w, h, aria=""):
    """Open the SVG. Always landscape; width follows content."""
    global _W, _H
    _W, _H = w, h
    _out.clear()
    add(f'<svg viewBox="0 0 {w} {h}" role="img" xmlns="http://www.w3.org/2000/svg" '
        f'aria-label="{esc(aria)}">')
    add('<defs><marker id="ar" viewBox="0 0 10 8" refX="9" refY="4" markerWidth="8" '
        f'markerHeight="6.5" orient="auto-start-reverse"><polygon points="0,0 10,4 0,8" '
        f'fill="{INK}"/></marker></defs>')
    add(f'<rect x="0" y="0" width="{w}" height="{h}" fill="{PAPER}"/>')


def finish(path):
    add('</svg>')
    open(path, "w", encoding="utf-8").write("\n".join(_out))
    print(f"emitted {len(_out)} | canvas {_W} x {_H} | ratio {round(_W/_H, 3)}")


# ---------------------------------------------------------------- text
def lbl(x, y, t, anchor="start", cls="lb"):
    add(f'<text x="{x}" y="{y}" class="{cls}" text-anchor="{anchor}">{esc(t)}</text>')


def sublist(x, y, items, lh=17):
    """Plain-language list under a block. 2–4 short items; never a paragraph."""
    for i, t in enumerate(items):
        add(f'<text x="{x+6}" y="{y+i*lh}" class="sub">{esc("·  " + t)}</text>')


# ---------------------------------------------------------------- shapes
def block(x, y, w, h, fill, lines, small=False, badge=None, tc="#fff"):
    """A step. Size = weight: large = every time, small = conditional."""
    add(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6" fill="{fill}"/>')
    lh = 16 if small else 19
    cls = "bt s" if small else "bt"
    cy = y + h/2 - (len(lines)-1)*lh/2 + (5 if small else 6)
    for i, ln in enumerate(lines):
        add(f'<text x="{x+w/2}" y="{cy+i*lh}" class="{cls}" style="fill:{tc}" '
            f'text-anchor="middle">{esc(ln)}</text>')
    if badge:
        bw = 8.3*len(badge)+18
        add(f'<rect x="{x+w-bw-8}" y="{y-14}" width="{bw}" height="23" rx="11.5" '
            f'fill="#FFFFFF" stroke="{fill}" stroke-width="1.8"/>')
        add(f'<text x="{x+w-bw/2-8}" y="{y+2}" class="bdg" text-anchor="middle" '
            f'fill="{fill}">{esc(badge)}</text>')


def split_block(x, y, w, h, left_fill, right_fill, lines):
    """One step owned jointly by two actors — half and half."""
    add(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6" fill="{left_fill}"/>')
    add(f'<rect x="{x+w/2}" y="{y}" width="{w/2}" height="{h}" rx="6" fill="{right_fill}"/>')
    cy = y + h/2 - (len(lines)-1)*19/2 + 6
    for i, ln in enumerate(lines):
        add(f'<text x="{x+w/2}" y="{cy+i*19}" class="bt" style="fill:#fff" '
            f'text-anchor="middle">{esc(ln)}</text>')


def chip(x, y, w, h, lines, stroke, fill="#FFFFFF"):
    """A watch condition, a trigger, or a state — not a step."""
    add(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{min(h/2,26)}" fill="{fill}" '
        f'stroke="{stroke}" stroke-width="1.8"/>')
    y0 = y + h/2 - (len(lines)-1)*17/2 + 5
    for i, ln in enumerate(lines):
        add(f'<text x="{x+w/2}" y="{y0+i*17}" class="ct" text-anchor="middle" '
            f'fill="{stroke}">{esc(ln)}</text>')


def diamond(cx, cy, lines, w=180, h=104):
    """A decision. Always white with ink outline, whoever owns it."""
    add(f'<polygon points="{cx},{cy-h/2} {cx+w/2},{cy} {cx},{cy+h/2} {cx-w/2},{cy}" '
        f'fill="#FFFFFF" stroke="{INK}" stroke-width="1.8"/>')
    y0 = cy - (len(lines)-1)*17/2 + 5
    for i, ln in enumerate(lines):
        add(f'<text x="{cx}" y="{y0+i*17}" class="dt" text-anchor="middle">{esc(ln)}</text>')


def oval(cx, cy, rx, ry, fill, lines, outline=None):
    """A terminus or an outcome. Outcomes are white + ink outline, not an actor colour."""
    if outline:
        add(f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="#FFFFFF" '
            f'stroke="{outline}" stroke-width="1.8"/>')
        tf = outline
    else:
        add(f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="{fill}"/>')
        tf = "#fff"
    y0 = cy - (len(lines)-1)*17/2 + 5
    for i, ln in enumerate(lines):
        add(f'<text x="{cx}" y="{y0+i*17}" class="bt s" style="fill:{tf}" '
            f'text-anchor="middle">{esc(ln)}</text>')


def tag(x, y, w, h, lines):
    """A grey input/reference feeder — data, not an action."""
    add(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="3" fill="{TAG}" '
        f'stroke="#C6CBD1" stroke-width="1"/>')
    cy = y + h/2 - (len(lines)-1)*17/2 + 5
    for i, ln in enumerate(lines):
        add(f'<text x="{x+w/2}" y="{cy+i*17}" class="tg" text-anchor="middle">{esc(ln)}</text>')


# ---------------------------------------------------------------- connectors
def arrow(x1, y1, x2, y2, dash=False):
    d = ' stroke-dasharray="7 5" opacity=".68"' if dash else ''
    add(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" class="ln"{d} '
        f'marker-end="url(#ar)"/>')


def path(dd, dash=False, label=None, lx=None, ly=None, anchor="middle"):
    """Orthogonal routed connector. Solid = the main path, dashed = exception/loop."""
    d = ' stroke-dasharray="7 5" opacity=".68"' if dash else ''
    add(f'<path d="{dd}" fill="none" class="ln"{d} marker-end="url(#ar)"/>')
    if label:
        add(f'<text x="{lx}" y="{ly}" class="lb" text-anchor="{anchor}">{esc(label)}</text>')


def conn(dd, dash=False):
    """Routed line with NO arrowhead — for buses and joins."""
    d = ' stroke-dasharray="7 5" opacity=".68"' if dash else ''
    add(f'<path d="{dd}" fill="none" class="ln"{d}/>')


# ---------------------------------------------------------------- layout
def masthead(eyebrow, title, deck, rule_y=150, w=None):
    w = w or _W
    lbl(50, 58, eyebrow, cls="eyebrow")
    lbl(50, 100, title, cls="title")
    lbl(50, 128, deck, cls="deck")
    add(f'<line x1="50" y1="{rule_y}" x2="{w-50}" y2="{rule_y}" stroke="{RULE}" '
        f'stroke-width="1.4"/>')


def legend(items, x, cy=72, per_row=None, gap=36):
    """items: [(name, colour)]. Pass per_row to wrap onto multiple rows."""
    rows = [items] if not per_row else [items[i:i+per_row] for i in range(0, len(items), per_row)]
    for r, grp in enumerate(rows):
        lx, y = x, cy + r*34
        for name, col in grp:
            add(f'<circle cx="{lx+13}" cy="{y}" r="13" fill="{col}"/>')
            lbl(lx+34, y+6, name, cls="leg")
            lx += 34 + 8.4*len(name) + gap


def band(y, h, title, right=None, slots=7, pad=0, x=BX):
    """A phase band. Width follows its own content — never a common right edge,
    or short bands read as half-empty. Returns the band's right edge."""
    w = slots*SLOT + 30 + pad
    add(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{BAND}"/>')
    lbl(x+22, y+34, title, cls="band")
    if right:
        lbl(x+w-14, y+34, right, "end", "bandhi")
    return x + w


def row(y, steps, x0=IX, breaks=()):
    """steps: (colour, lines, subs|None, badge|None, slots).
    breaks: indices that get an OR divider instead of an arrow.
    Returns the row centreline."""
    x, cy, prev = x0, y + BH/2, None
    for i, (col, lines, subs, badge, slots) in enumerate(steps):
        w = slots*SLOT - GAP
        block(x, y, w, BH, col, lines, badge=badge)
        if subs:
            sublist(x, y+BH+26, subs)
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


def spine(y, h, title, x=36, w=None):
    """The grey clean-path lane on a swimlane-style sheet. Returns its centreline."""
    w = w or (_W - 2*x)
    add(f'<rect x="{x-14}" y="{y}" width="{w+28}" height="{h}" fill="#DBDBD6" opacity=".55"/>')
    lbl(x+2, y+24, title, cls="spine")
    return y + h/2 + 12


def columns(titles, top, bottom, n=None, margin=36, gap=22, w=None):
    """Outlined functional columns. titles: [(name, colour)].
    Returns the list of column left edges and the column width."""
    w = w or _W
    n = n or len(titles)
    colw = (w - 2*margin - (n-1)*gap)/n
    cols = [margin + i*(colw+gap) for i in range(n)]
    for i, (t, col) in enumerate(titles):
        add(f'<rect x="{cols[i]}" y="{top}" width="{colw}" height="{bottom-top}" rx="4" '
            f'fill="none" stroke="{col}" stroke-width="1.6"/>')
        add(f'<text x="{cols[i]+16}" y="{top+30}" class="colt" fill="{col}">{esc(t)}</text>')
    return cols, colw


def panel(x, y, w, h, title, cls="pnl"):
    """A dashed reference panel — reading notes, constraints, payer rules."""
    add(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="none" '
        f'stroke="{RULE}" stroke-width="1.8" stroke-dasharray="8 6"/>')
    lbl(x+26, y+36, title, cls=cls)


def column_rule(x, y1, y2, colour=INK):
    """The thick vertical rule that heads a panel column."""
    add(f'<line x1="{x}" y1="{y1}" x2="{x}" y2="{y2}" stroke="{colour}" stroke-width="3"/>')


def footer(left, right, h=None, w=None):
    h = h or _H
    w = w or _W
    add(f'<line x1="50" y1="{h-72}" x2="{w-50}" y2="{h-72}" stroke="{RULE}" stroke-width="1.4"/>')
    lbl(50, h-40, left, cls="foot")
    lbl(w-50, h-40, right, "end", "foot")
