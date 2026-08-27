# -*- coding: utf-8 -*-
"""_flow_vis — draw the future-state sheets from the Capacity & Scheduling Variable Workbook.

    python3 _flow_vis.py <flow> viz|future <out.svg>

Both sheets are MVP-scoped: a step is in scope when a majority of the variables behind it are
MVP = Yes in the workbook's own MVP column. They differ only in how far the tool is allowed to go.

    viz     FUTURE STATE VISUALIZATION MVP — release 1. The process is unchanged; every step,
            actor and handoff stays where the current-state sheet put it. Reports scattered
            across HCHB, Workday, Commure, routing and telephony are pulled into one view, so
            the person already assigned to the step decides faster. A bold green outline marks
            a step that gains that view. Nothing is automated.

    future  FUTURE STATE MVP — where the same MVP scope ends up. Each in-scope step is redrawn
            at the posture the workbook's "Future state -- the tool's role" column gives it:
            Automate, Assist or Surface. Steps out of MVP scope stay exactly as they are today,
            so the sheet shows release-1 scope against an unchanged background.

Nothing here is an editorial list. Change the MVP column in the workbook, re-run, and both
sheets change with it.
"""
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent

FLOWS = {
    "soc":     ("_flow-detailed-composite.gen.py", "vmap-soc.json"),
    "episode": ("_flow-primary-map.gen.py",        "vmap-episode.json"),
    "routine": ("_flow-routine-visits.gen.py",     "vmap-routine-visits.json"),
    "auth":    ("_flow-authorization.gen.py",      "vmap-authorization.json"),
    "dcs":     ("_flow-dcs-scheduler.gen.py",      "vmap-dcs-scheduler.json"),
    "recert":  ("_flow-recert-discharge.gen.py",   "vmap-recert-discharge.json"),
}

RANK = {"Automate": 3, "Assist": 2, "Surface": 1, "Stays manual": 0}

# Steps the future state removes outright. The workbook cannot express this — it says how far
# the tool goes on each variable, never that a step stops existing — so it is carried here from
# the target-state sheets, which is the only place that judgment was ever written down.
REMOVED = {
    "routine": {"Each submission generates its own assignment task": "DE-05 — the care team is "
                "set at referral, so the per-discipline assignment task has nothing to do"},
}


def key_of(lines):
    return " ".join(lines).replace("—", "-").replace("’", "'").strip()


def scope(ids, V, mvp_only=True):
    """In scope when a majority of the block's variables are MVP = Yes.

    A majority, not any one of them: on an "any" rule almost every block qualifies and the
    sheets stop discriminating, which is no use in a demo and is not true either.
    """
    ds = [V[i] for i in ids if i in V]
    if not ds:
        return None
    if mvp_only:
        yes = [d for d in ds if d.get("mvp") == "Yes"]
        if len(yes) * 2 < len(ds):
            return None
    else:
        yes = ds                      # full scope — every variable, MVP or not
    # the MODAL posture, ties broken toward the weaker one. Taking the strongest instead makes
    # a step read "Automate" because one variable of seven does — 18 of 19 blocks on routine
    # visits came out Automate that way, which is not what the workbook says.
    import collections
    tally = collections.Counter(d.get("role", "") for d in yes if d.get("role"))
    if not tally:
        return None
    top = max(tally.values())
    return min((r for r, n in tally.items() if n == top), key=lambda r: RANK.get(r, 0))


PRELUDE = '''
__VIS__ = True
__D__ = [0]
__SCOPE__ = {scope!r}
__GONE__ = {gone!r}
__MODE__ = {mode!r}
GRN, GRND, DARKINK = "#A6E22E", "#5F8A12", "#1B211E"

def __key__(lines):
    return " ".join(lines).replace("\\u2014", "-").replace("\\u2019", "'").strip()

def __text__(x, y, w, h, lines, small, colour):
    lh = 15.5 if small else 19
    cls = "bt s" if small else "bt"
    cy = y + h/2 - (len(lines)-1)*lh/2 + (5 if small else 6)
    for i, ln in enumerate(lines):
        add(f'<text x="{{x+w/2}}" y="{{cy+i*lh}}" class="{{cls}}" style="fill:{{colour}}" '
            f'text-anchor="middle">{{esc(ln)}}</text>')

def __badge__(x, y, w, label, colour):
    bw = 8.3*len(label)+18
    add(f'<rect x="{{x+w-bw-8}}" y="{{y-14}}" width="{{bw}}" height="23" rx="11.5" '
        f'fill="#FFFFFF" stroke="{{colour}}" stroke-width="1.8"/>')
    add(f'<text x="{{x+w-bw/2-8}}" y="{{y+2}}" class="bdg" text-anchor="middle" '
        f'fill="{{colour}}">{{esc(label)}}</text>')

def __ghost__(x, y, w, h, lines):
    add(f'<rect x="{{x}}" y="{{y}}" width="{{w}}" height="{{h}}" rx="5" fill="#FBFBF8" '
        f'stroke="#5A6560" stroke-width="1.7" stroke-dasharray="7 5"/>')
    cy = y + h/2 - (len(lines)-1)*16/2 + 5
    for i, ln in enumerate(lines):
        add(f'<text x="{{x+w/2}}" y="{{cy+i*16}}" class="bt s" style="fill:#5A6560" '
            f'text-anchor="middle" opacity=".85">{{esc(ln)}}</text>')
        wl = 7.0*len(ln)
        add(f'<line x1="{{x+w/2-wl/2}}" y1="{{cy+i*16-5}}" x2="{{x+w/2+wl/2}}" '
            f'y2="{{cy+i*16-5}}" stroke="#5A6560" stroke-width="1.2" opacity=".8"/>')
    add(f'<text x="{{x+w/2}}" y="{{y+h+18}}" class="trg" text-anchor="middle">'
        f'NO LONGER A STEP</text>')

def __skip__(lines):
    """A removed step is never drawn at all — painting the ghost over it leaves the original
    block's badge showing through the dashes."""
    return __MODE__ != "viz" and __key__(lines) in __GONE__

def __vis_mark__(x, y, w, h, lines, fill=None, small=False, badge=None, bc=None):
    role = __SCOPE__.get(__key__(lines))
    if not role:
        return
    if __MODE__ == "viz":
        # release 1 changes nothing but what the person can see
        add(f'<rect x="{{x-4}}" y="{{y-4}}" width="{{w+8}}" height="{{h+8}}" rx="9" fill="none" '
            f'stroke="{{GRN}}" stroke-width="5"/>')
        if badge: __badge__(x, y, w, badge, bc or fill)
        return
    # future state: repaint the step at the posture the workbook gives it
    if role == "Automate":
        add(f'<rect x="{{x}}" y="{{y}}" width="{{w}}" height="{{h}}" rx="5" fill="{{GRN}}"/>')
        __text__(x, y, w, h, lines, small, DARKINK)
        __badge__(x, y, w, badge or "AUTOMATE", GRND)
    elif role == "Assist":
        BAR = 52
        add(f'<rect x="{{x}}" y="{{y}}" width="{{w}}" height="{{h}}" rx="5" fill="{{GRN}}"/>')
        add(f'<path d="M {{x+w-BAR}} {{y}} L {{x+w-6}} {{y}} A 6 6 0 0 1 {{x+w}} {{y+6}} '
            f'L {{x+w}} {{y+h-6}} A 6 6 0 0 1 {{x+w-6}} {{y+h}} L {{x+w-BAR}} {{y+h}} Z" '
            f'fill="{{fill}}"/>')
        __text__(x, y, w-BAR, h, lines, small, DARKINK)
        __badge__(x, y, w, badge or "ASSIST", fill)
    else:                                   # Surface — the person still decides
        add(f'<path d="M {{x+6}} {{y}} L {{x+w-6}} {{y}} A 6 6 0 0 1 {{x+w}} {{y+6}} '
            f'L {{x+w}} {{y+13}} L {{x}} {{y+13}} L {{x}} {{y+6}} '
            f'A 6 6 0 0 1 {{x+6}} {{y}} Z" fill="{{GRN}}"/>')
        if badge: __badge__(x, y, w, badge, bc or fill)
'''


def build(flow, mode, out):
    gen, mapfile = FLOWS[flow]
    src = (HERE / gen).read_text()
    V = json.loads((HERE / "variables.json").read_text())
    vmap = json.loads((HERE / mapfile).read_text())

    sc = {}
    for k, ids in vmap.items():
        if k.startswith("_") or not ids:
            continue
        r = scope(ids, V, mvp_only=(mode != "full"))
        if r:
            sc[k] = r

    m = re.search(r"^(def block\(([^)]*)\):\n)", src, re.M)
    if not m:
        raise SystemExit(f"{gen}: no block() to hook")
    args = m.group(2)
    fwd = ", ".join(f"{k}={k}" for k in ("small", "badge", "tc", "bc") if k in args)
    back = ", ".join(f"{k}={k}" for k in ("small", "badge", "bc") if k in args)
    guard = (f"    if __VIS__ and not __D__[0]:\n"
             f"        if __skip__(lines): return __ghost__(x, y, w, h, lines)\n"
             f"        __D__[0] += 1\n"
             f"        try: block(x, y, w, h, fill, lines{', ' + fwd if fwd else ''})\n"
             f"        finally: __D__[0] -= 1\n"
             f"        return __vis_mark__(x, y, w, h, lines, fill=fill"
             f"{', ' + back if back else ''})\n")
    src = src[:m.end(1)] + guard + src[m.end(1):]
    src = PRELUDE.format(scope=sc, gone=REMOVED.get(flow, {}), mode=mode) + "\n" + src

    if mode == "full":
        title, key = ("FUTURE STATE · FULL",
                      "FUTURE STATE · FULL — every variable in the workbook, MVP or not · "
                      "solid green = the tool does it; green with a colour bar = the tool "
                      "proposes, the named person confirms; a green top stripe = the tool "
                      "shows, the person decides")
    elif mode == "viz":
        title, key = ("FUTURE STATE VISUALIZATION · MVP",
                      "FUTURE STATE VISUALIZATION · MVP — the process is unchanged; a "
                      "green outline marks a step that gains one consolidated view instead of "
                      "several reports · scope and posture read from the workbook's MVP column")
    else:
        title, key = ("FUTURE STATE · MVP",
                      "FUTURE STATE · MVP — solid green = the tool does it; green with a "
                      "colour bar = the tool proposes, the named person confirms; a green top "
                      "stripe = the tool shows, the person decides · unmarked steps are out "
                      "of MVP scope and unchanged")
    if mode == "full":
        mode = "future"               # drawn with the same posture vocabulary
    src = src.replace("CURRENT STATE", title)
    src = re.sub(r'"Current state[^"]*"', lambda _: '"' + key + '"', src)

    ns = {"__name__": "__vis__"}
    argv = sys.argv
    sys.argv = ["gen", out]
    try:
        exec(compile(src, gen, "exec"), ns)
    finally:
        sys.argv = argv
    import collections
    c = collections.Counter(sc.values())
    print(f"{flow:8} {mode:6} -> {out}  ({ns['W']}x{ns['H']})  "
          f"in MVP {len(sc)}  {dict(c)}")


if __name__ == "__main__":
    build(sys.argv[1], sys.argv[2], sys.argv[3])
