# -*- coding: utf-8 -*-
"""_flow_vis — draw the future-state sheets from the Capacity & Scheduling Variable Workbook.

    python3 _flow_vis.py <flow> future|mvp|target <out.svg>

Four states. The two middle ones are BOTH future states — different evolutions of the same
future, not different subjects — and they are cumulative: MVP keeps everything the dashboard
gives you and adds the engine on top.

    future  FUTURE STATE — DASHBOARD VISUALIZATION. The process is unchanged; every step, actor
            and handoff stays where the current-state sheet put it. Reports scattered across
            HCHB, Workday, Commure, routing and telephony are pulled into one view, so the
            person already assigned to the step decides faster. A bold green outline marks a
            step that gains that view. Nothing is automated, and the scope is everything the
            workbook holds — showing is cheap, so show it all.

    mvp     FUTURE STATE — MVP. The dashboard, PLUS the automation and AI engine on the
            variables the workbook marks MVP = Yes. Those steps are redrawn at the posture
            their "Future state -- the tool's role" column gives them; every other step keeps
            the dashboard outline, because the visualisation does not go away when the engine
            arrives.

    target  TARGET STATE — optimal functionality. Every variable accounted for and acted on in
            the way the workbook says is most desirable.

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
    "soc": {"PCC creates scheduling grid entry": "DE-04 — the capacity tool replaces the "
            "scheduling grid; they are the same object, do not build both",
            "Pending-auth visits invisible - not on calendar, not counted": "pending visits "
            "become visible and counted, so the blind spot stops existing"},
    "dcs": {"Pending auth not on calendar, not counted": "pending visits become visible and "
            "counted, so the blind spot stops existing"},
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
__SEEN__ = {seen!r}
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
    # no label: several sheets already put a note directly under a block, and the dashed,
    # struck-through styling says it on its own. The footer carries the key.

def __skip__(lines):
    """A removed step is never drawn at all — painting the ghost over it leaves the original
    block's badge showing through the dashes."""
    return __MODE__ != "future" and __key__(lines) in __GONE__

def __outline__(x, y, w, h, badge, fill, bc):
    add(f'<rect x="{{x-4}}" y="{{y-4}}" width="{{w+8}}" height="{{h+8}}" rx="9" fill="none" '
        f'stroke="{{GRN}}" stroke-width="5"/>')
    if badge: __badge__(x, y, w, badge, bc or fill)

def __vis_mark__(x, y, w, h, lines, fill=None, small=False, badge=None, bc=None):
    k = __key__(lines)
    role = __SCOPE__.get(k)
    if __MODE__ == "future":
        # the dashboard: the process is untouched, the person just sees more
        if role: __outline__(x, y, w, h, badge, fill, bc)
        return
    if not role:
        # MVP keeps the dashboard everywhere the engine has not reached yet
        if k in __SEEN__: __outline__(x, y, w, h, badge, fill, bc)
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
        r = scope(ids, V, mvp_only=(mode == "mvp"))   # "both" uses full scope
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
    # every mapped block gains the dashboard view; MVP shows it wherever the engine has not
    # yet taken over, so the two future states read as one evolving into the other
    seen = {k for k, ids in vmap.items() if not k.startswith("_") and ids}
    src = PRELUDE.format(scope=sc, seen=seen, gone=REMOVED.get(flow, {}),
                         mode=mode) + "\n" + src

    # these land in a single-line footer with page text on the right — the 2200pt canvas
    # leaves room for roughly 180 characters, so keep them short
    if mode == "both":
        # some flows have no variable outside MVP, so the two sheets are byte-identical and
        # shipping both invites the reader to hunt for a difference that is not there
        title, key = ("FUTURE STATE · MVP  +  TARGET STATE",
                      "FUTURE STATE · MVP and TARGET STATE are identical here \u2014 every "
                      "variable behind every step is MVP = Yes \u00b7 solid = the tool does it; "
                      "colour bar = it proposes; top stripe = it shows")
    elif mode == "target":
        title, key = ("TARGET STATE",
                      "TARGET STATE — optimal functionality, every variable acted on · solid = "
                      "the tool does it; colour bar = it proposes; top stripe = it shows; "
                      "dashed = no longer a step")
    elif mode == "mvp":
        title, key = ("FUTURE STATE · MVP",
                      "FUTURE STATE · MVP — the dashboard plus the engine on MVP = Yes "
                      "variables · solid = the tool does it; colour bar = it proposes; top "
                      "stripe = it shows; outline = view only")
    else:
        title, key = ("FUTURE STATE · DASHBOARD VISUALIZATION",
                      "FUTURE STATE · DASHBOARD VISUALIZATION — the process is unchanged; a "
                      "green outline marks a step that gains one consolidated view · nothing "
                      "is automated")

    # the episode sheet has a "Current state — ..." line inside its READING THIS MAP panel;
    # the generic replace below would drop the whole footer key into that bullet.
    # Read this BEFORE mode is collapsed to the drawing vocabulary below.
    blurb = {"future": "The process is unchanged \u2014 the tool shows more",
             "mvp": "The dashboard, plus the engine on MVP variables",
             "target": "Every variable acted on in the desired way",
             "both": "Every variable acted on in the desired way"}[mode]

    if mode != "future":
        mode = "posture"              # mvp and target share the posture vocabulary
    src = src.replace("Current state \u2014 including what is wasteful or manual", blurb)
    src = src.replace("CURRENT STATE", title)
    src = re.sub(r'"Current state[^"]*"', lambda _: '"' + key + '"', src)
    src = src.replace("   \u00b7   current state, corrected 18 Aug 2026",
                      "   \u00b7   " + title)
    # the composite's footer is three concatenated fragments, so swap the whole lbl() call
    src = re.sub(r'lbl\(M, H-34, "Compassus.*?cls="foot"\)',
                 lambda _: 'lbl(M, H-34, "Compassus Home Health \u00b7 Capacity & Scheduling \u2014 '
                           + key.replace('"', "'") + '", cls="foot")', src, flags=re.S)

    # Not every generator says "current state" — the DCS sheet's eyebrow is just the company
    # name and its footer explains the sizing convention. Without a fallback those sheets ship
    # with no state on them at all, which is the one thing they must never do.
    if title not in src:
        src, n = re.subn(r'(cls="eyebrow"\))', r'\1', src, count=1)
        src = re.sub(r'(lbl\([^,]+,\s*[\d.]+,\s*")([^"]*)("\s*,\s*cls="eyebrow"\))',
                     lambda m: m.group(1) + m.group(2) + "   \u00b7   " + title + m.group(3),
                     src, count=1)
        src = re.sub(r'lbl\(\s*(?:50|M)\s*,\s*H-\d+\s*,\s*"(?:[^"\\]|\\.)*"'
                     r'(?:\s*"(?:[^"\\]|\\.)*")*\s*,\s*cls="foot"\)',
                     lambda _: 'lbl(50, H-40, "' + key.replace('"', "'") + '", cls="foot")',
                     src, count=1)

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
