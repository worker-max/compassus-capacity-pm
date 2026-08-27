# -*- coding: utf-8 -*-
"""_flow_vis — derive the VISUALISE-ONLY and MVP sheets from a CURRENT-STATE generator.

    python3 _flow_vis.py <flow> full|mvp <out.svg>

Visualise-only does not change the process. Every step, every actor and every handoff stays
exactly where the current-state sheet put it. What changes is that reports scattered across
HCHB, Workday, Commure, routing and telephony are pulled into one view, so the person already
assigned to that step decides faster and better informed.

So these sheets are the current-state sheets, marked. A bold green outline says: this step gets
a consolidated view. Nothing is recoloured, nothing moves, nothing is automated — which is also
why they overlay their current-state twin perfectly.

Both documents are derived from the workbook through vmap-<flow>.json, not from an editorial
list:

    full   outline where ANY variable behind the block has Current-state = In-system.
           The ceiling of free visualisation: no new capture, only consolidation.

    mvp    outline where ANY variable behind the block has MVP Req. = Yes.
           Where those variables are already In-system the outline is solid; where they are
           Manual or Tacit it is dashed and badged NEEDS CAPTURE, because release 1 committed
           to them and nothing records them yet.

MVP is not a subset of full. The difference between the two sheets is the release-1 build list.
"""
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent

FLOWS = {
    "soc":     ("_flow-detailed-composite.gen.py", "vmap-soc.json",
                "Home Health Capacity & Scheduling — Detailed Flow"),
    "episode": ("_flow-primary-map.gen.py",        "vmap-episode.json",
                "The Episode, End to End"),
    "routine": ("_flow-routine-visits.gen.py",     "vmap-routine-visits.json",
                "Routine Visit Scheduling"),
    "auth":    ("_flow-authorization.gen.py",      "vmap-authorization.json", "Authorization"),
    "dcs":     ("_flow-dcs-scheduler.gen.py",      "vmap-dcs-scheduler.json",
                "Plan of Care → Assignment"),
    "recert":  ("_flow-recert-discharge.gen.py",   "vmap-recert-discharge.json",
                "Recertification & Discharge"),
}

LIT, CAPTURE, DARK = "lit", "capture", "dark"


def key_of(lines):
    return " ".join(lines).replace("—", "-").replace("’", "'").strip()


def classify(ids, variables, mvp):
    """Read the workbook columns behind a block and decide how it is marked.

    The bar is a MAJORITY of the block's variables, not any one of them. Consolidating one
    report out of seven does not make the decision quicker or better informed — it just moves
    where you go to be under-informed. On an "any" rule 19 of routine visits' 21 blocks light
    up and the two sheets are indistinguishable, which is no use in a demo and, worse, is not
    true.
    """
    ds = [variables[i] for i in ids if i in variables]
    if not ds:
        return DARK
    if not mvp:
        insys = sum(1 for d in ds if d.get("current") == "In-system")
        return LIT if insys * 2 >= len(ds) else DARK
    yes = [d for d in ds if d.get("mvp") == "Yes"]
    if not yes:
        return DARK
    insys = sum(1 for d in yes if d.get("current") == "In-system")
    return LIT if insys * 2 >= len(yes) else CAPTURE


def sources(ids, variables):
    """The platforms a block's data would be pulled from, for the consolidated view."""
    out = []
    for i in ids:
        for tok in re.split(r"[+/,]", variables.get(i, {}).get("sot", "")):
            tok = tok.strip()
            if tok and tok.lower() not in ("manual", "derived", "config") and tok not in out:
                out.append(tok)
    return out


PRELUDE = '''
__VIS__ = True
__D__ = [0]
__STATE__ = {state!r}
__SRC__ = {src!r}
GRN, GRND = "#A6E22E", "#5F8A12"

def __key__(lines):
    return " ".join(lines).replace("\\u2014", "-").replace("\\u2019", "'").strip()

def __vis_mark__(x, y, w, h, lines, fill=None, badge=None, bc=None):
    """Outline a step that gains a consolidated view. The block itself is untouched."""
    st = __STATE__.get(__key__(lines))
    if st not in ("lit", "capture"):
        return
    # solid vs dashed carries the distinction on its own. A text pill was tried and there is
    # nowhere to put it: above the block is the badge, below it is the sublist, inside it is
    # the block's own wording.
    dash = ' stroke-dasharray="9 6"' if st == "capture" else ""
    add(f'<rect x="{{x-4}}" y="{{y-4}}" width="{{w+8}}" height="{{h+8}}" rx="9" fill="none" '
        f'stroke="{{GRN}}" stroke-width="5"{{dash}}/>')
    # the outline runs straight through a badge sitting on the block's top edge, so put the
    # badge back on top of it
    if badge:
        bw = 8.3*len(badge)+18
        add(f'<rect x="{{x+w-bw-8}}" y="{{y-14}}" width="{{bw}}" height="23" rx="11.5" '
            f'fill="#FFFFFF" stroke="{{bc or fill}}" stroke-width="1.8"/>')
        add(f'<text x="{{x+w-bw/2-8}}" y="{{y+2}}" class="bdg" text-anchor="middle" '
            f'fill="{{bc or fill}}">{{esc(badge)}}</text>')
'''


def build(flow, mvp, out):
    gen, mapfile, nice = FLOWS[flow]
    src = (HERE / gen).read_text()
    variables = json.loads((HERE / "variables.json").read_text())
    vmap = json.loads((HERE / mapfile).read_text())

    state, srcmap = {}, {}
    for k, ids in vmap.items():
        if k.startswith("_") or not ids:
            continue
        state[k] = classify(ids, variables, mvp)
        srcmap[k] = sources(ids, variables)

    # one hook covers every block on the sheet: the row/phase helpers all call block()
    m = re.search(r"^(def block\(([^)]*)\):\n)", src, re.M)
    if not m:
        raise SystemExit(f"{gen}: no block() to hook")
    args = m.group(2)
    fwd = ", ".join(f"{k}={k}" for k in ("small", "badge", "tc", "bc") if k in args)
    back = ", ".join(f"{k}={k}" for k in ("badge", "bc") if k in args)
    guard = (f"    if __VIS__ and not __D__[0]:\n"
             f"        __D__[0] += 1\n"
             f"        try: block(x, y, w, h, fill, lines{', ' + fwd if fwd else ''})\n"
             f"        finally: __D__[0] -= 1\n"
             f"        return __vis_mark__(x, y, w, h, lines, fill=fill"
             f"{', ' + back if back else ''})\n")
    src = src[:m.end(1)] + guard + src[m.end(1):]
    src = PRELUDE.format(state=state, src=srcmap) + "\n" + src

    scope = "MVP" if mvp else "VISUALISE ONLY"
    key = ("MVP · solid green = one consolidated view, from data already in a system · "
           "dashed green = committed for release 1, nothing records it yet"
           if mvp else
           "VISUALISE ONLY · a green outline marks a step that gains one consolidated view "
           "instead of several reports · the process itself is unchanged")
    src = src.replace("CURRENT STATE", scope)
    src = re.sub(r'"Current state[^"]*"', lambda _: '"' + key + '"', src)
    src = re.sub(r'"[Nn]othing on this sheet is a proposal[^"]*"', lambda _: '"' + key + '"', src)

    ns = {"__name__": "__vis__"}
    argv = sys.argv
    sys.argv = ["gen", out]
    try:
        exec(compile(src, gen, "exec"), ns)
    finally:
        sys.argv = argv
    lit = sum(1 for v in state.values() if v == LIT)
    cap = sum(1 for v in state.values() if v == CAPTURE)
    print(f"{flow:8} {'mvp' if mvp else 'full':4} -> {out}  "
          f"({ns['W']}x{ns['H']})  outlined {lit}  needs-capture {cap}  "
          f"unmarked {len(state)-lit-cap}")
    return ns["W"], ns["H"], nice


if __name__ == "__main__":
    flow, scope, out = sys.argv[1:4]
    build(flow, scope == "mvp", out)
