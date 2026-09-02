# -*- coding: utf-8 -*-
"""Shared shell for the Compassus scenario sheets.

Every scenario family is: four bands, four steps a band, an outcome chip on the
right of each band, a summary panel, and a coverage strip naming which value
levers the sheet demonstrates. Current and target render from the same content
so the pair is structurally identical.
"""
import sys

sys.path.insert(0, r"C:\Users\chigh\compassus-capacity-pm\.claude\skills\process-flow-map\assets")
from flowkit import *  # noqa

LOSS, SAVE = "#B03A2E", "#1E7A46"
BH_ = 290
CHIPW = 440

LEG = [("Intake", C["intake"]), ("Insurance & Auth", C["auth"]), ("PCC / Scheduler", C["pcc"]),
       ("Clinician", C["clin"]), ("DCS", C["dcs"]), ("HCHB", C["hchb"]),
       ("Per Diem / Float", C["float_"]), ("Patient", C["pat"]), ("Branch leadership", C["lead"])]


def draw_rows(bands, y0, x0, chipx, accent):
    """bands = [(num, phase, claim, steps, terminals, outcome)]"""
    for i, (_n, _p, _c, steps, terms, out) in enumerate(bands):
        b = y0 + i * (BH_ + 24)
        row(b + 58, [(col, lines, subs, None, 1) for col, lines, subs in steps], x0=x0)
        for slot, label, subs in terms:
            cx = x0 + slot * SLOT + BW / 2
            oval(cx, b + 103, BW / 2, 45, "#fff", [label], outline=INK)
            arrow(cx - BW / 2 - 28, b + 103, cx - BW / 2 - 6, b + 103)
            sublist(cx - BW / 2, b + 174, subs)
        head, l2, l3 = out
        chip(chipx, b + 58, CHIPW, 96, ["", l2, l3], INK)
        add(f'<text x="{chipx + CHIPW/2}" y="{b + 88}" class="ct" text-anchor="middle" '
            f'style="fill:{accent};font-weight:700">{esc(head)}</text>')


def coverage(levers, x, y, accent, w=470):
    """The strip naming which levers this sheet demonstrates."""
    add(f'<rect x="{x}" y="{y}" width="{w}" height="112" rx="8" fill="none" '
        f'stroke="{RULE}" stroke-width="1.6" stroke-dasharray="7 5"/>')
    lbl(x + 20, y + 28, "LEVERS ON THIS SHEET", cls="colh")
    for i, (tag, name) in enumerate(levers):
        yy = y + 52 + i * 19
        add(f'<text x="{x + 20}" y="{yy}" class="sub" style="fill:{accent};font-weight:700">'
            f'{esc(tag)}</text>')
        add(f'<text x="{x + 58}" y="{yy}" class="sub">{esc(name)}</text>')


def single(mode, title, deck_cur, deck_tgt, bands_cur, bands_tgt, summary,
           levers, trigger, panel_title_cur, panel_title_tgt, foot_right,
           W=2600, H=1880):
    """Render one state on its own sheet."""
    cur = mode == "current"
    bands = bands_cur if cur else bands_tgt
    accent = LOSS if cur else SAVE
    begin(W, H, aria=f"{title}. " + (deck_cur if cur else deck_tgt))
    masthead("COMPASSUS HOME HEALTH  ·  "
             + ("CURRENT STATE" if cur else "TARGET STATE, EIGHTEEN MONTHS ON"),
             title + ("" if cur else "  —  the same week, after"),
             deck_cur if cur else deck_tgt)
    legend(LEG, x=1420, per_row=5)
    lbl(36, 224, "TRIGGER", cls="trg")
    chip(36, 248, 264, 90, trigger, INK)
    arrow(306, 293, 344, 293)
    for i, (num, phase, claim, *_r) in enumerate(bands):
        band(190 + i * (BH_ + 24), BH_, f"{num}  ·  {phase}", claim, slots=6)
    draw_rows(bands, 190, IX, 1520, accent)

    P = 1455
    panel(320, P, 1698, 195, panel_title_cur if cur else panel_title_tgt)
    for j, (head, cur_items, tgt_items) in enumerate(summary):
        x = 350 + j * 420
        column_rule(x - 14, P + 54, P + 70, accent)
        lbl(x - 14, P + 92, head, cls="colh")
        sublist(x - 20, P + 122, cur_items if cur else tgt_items)
    coverage(levers, 2060, P + 20, accent)
    footer(("Current state, August 2026.  A representative composite of documented branch patterns, "
            "not a single named case.  Nothing on this sheet is a proposal."
            if cur else
            "TARGET STATE  ·  A PROPOSAL.  Eighteen months after implementation.  Drawn against the "
            "same week and the same decisions people make."),
           foot_right)
    print("mode", mode, "| canvas", W, "x", H, "| ratio", round(W / H, 2))


def both(title, deck, bands_cur, bands_tgt, summary, levers, foot_right,
         W=4300, H=1950):
    """Render both states side by side."""
    begin(W, H, aria=f"{title}, current state and target state side by side. {deck}")
    masthead("COMPASSUS HOME HEALTH  ·  CURRENT STATE AND TARGET STATE",
             title + "  —  today, and eighteen months on", deck)
    legend(LEG, x=2860, per_row=5)

    add(f'<rect x="320" y="172" width="1858" height="38" rx="6" fill="{LOSS}"/>')
    add('<text x="1249" y="198" class="band" text-anchor="middle" style="fill:#fff">TODAY</text>')
    add(f'<rect x="2240" y="172" width="1858" height="38" rx="6" fill="{SAVE}"/>')
    add('<text x="3169" y="198" class="band" text-anchor="middle" style="fill:#fff">'
        'EIGHTEEN MONTHS ON</text>')

    Y0 = 232
    for i in range(len(bands_cur)):
        b = Y0 + i * (BH_ + 24)
        num, phase, claim = bands_cur[i][0], bands_cur[i][1], bands_cur[i][2]
        band(b, BH_, f"{num}  ·  {phase}", claim, slots=6, x=320)
        band(b, BH_, "", bands_tgt[i][2], slots=6, x=2240)
    draw_rows(bands_cur, Y0, 350, 1520, LOSS)
    draw_rows(bands_tgt, Y0, 2270, 3440, SAVE)

    P = Y0 + len(bands_cur) * (BH_ + 24) + 16
    panel(320, P, 1858, 180, "WHAT IT COST")
    panel(2240, P, 1858, 180, "WHAT CHANGED")
    for j, (head, cur_items, tgt_items) in enumerate(summary):
        for base, items, acc in ((350, cur_items, LOSS), (2270, tgt_items, SAVE)):
            x = base + j * 452
            column_rule(x - 14, P + 50, P + 66, acc)
            lbl(x - 14, P + 88, head, cls="colh")
            sublist(x - 20, P + 116, items)
    coverage(levers, 320, P + 200, INK, w=1858)
    footer("Left: current state, a representative composite of documented branch patterns.   "
           "Right: TARGET STATE, A PROPOSAL, eighteen months after implementation.", foot_right)
    print("mode both | canvas", W, "x", H, "| ratio", round(W / H, 2))
