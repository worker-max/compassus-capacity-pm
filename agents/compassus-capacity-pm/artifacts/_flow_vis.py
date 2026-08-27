# -*- coding: utf-8 -*-
"""_flow_vis — derive the VISUALISE-ONLY sheets from a target-state generator.

    python3 _flow_vis.py <flow> full|mvp <out.svg>

Release 1 is visualisation only (DE-03): the tool SHOWS, it does not ACT. These sheets say that
in the drawing rather than in a footnote, and they are derived from the target generator with its
posture helpers rebound — so they stay positional clones of the current-state sheet for free.

Two documents, because they answer different questions:

  full — every report feeds the picture. What the visualisation looks like when all the data
         named on the current-state sheets is flowing into it.
  mvp  — the same sheet cut to what release 1 actually lights up. Everything else is drawn as
         NOT IN MVP so the gap between the two documents is the release-1 conversation.

Posture transform, applied to the target sheet:

  target SURFACE  -> VISUALISED   the engine already only showed it; that is release 1
  target ENGINE   -> VISUALISED   if the block is a read or a computation over data we hold,
                                  and the actor who owns it when the tool is silent is named
                                  in RELEASE below. Otherwise PHASE 2.
  target ASSIST   -> PHASE 2      a proposal is an action; release 1 does not propose
  target MANUAL   -> unchanged    hands on the patient, or still inside HCHB
  target GHOST    -> restored     where the step still exists in release 1 (see RESTORE)

Colour still means actor. A VISUALISED block keeps the person's colour and takes the engine
stripe; it never becomes solid green, because solid green means the engine did the work.
"""
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent

FLOWS = {
    "soc":     ("_flow-soc-target.gen.py",              "SOC / ROC"),
    "episode": ("_flow-episode-target.gen.py",          "The episode, end to end"),
    "routine": ("_flow-routine-visits-target.gen.py",   "Routine visit scheduling"),
    "auth":    ("_flow-authorization-target.gen.py",    "Authorization"),
    "dcs":     ("_flow-dcs-scheduler-target.gen.py",    "Plan of care to assignment"),
    "recert":  ("_flow-recert-discharge-target.gen.py", "Recertification & discharge"),
}

# Which engine blocks survive as visualisation, who owns them when the tool is silent, and
# whether the data is there on day one. "mvp" = lit in both documents. "full" = lit only in
# the full-scenario document. Anything not named here is PHASE 2 in both.
RELEASE = {
"soc": {
  "Open capacity read - day · week · discipline · territory": ("pcc",  "mvp"),
  "Committed load computed - points, live":                   ("pcc",  "mvp"),
  "Assessing capacity by discipline":                         ("pcc",  "mvp"),
  "Front-load early visits (protect LUPA floor)":             ("dcs",  "mvp"),
  "MD notified inside 48h - the engine owns the clock":        ("dcs",  "mvp"),
  "Territory applied - zip · drive time":                     ("pcc",  "full"),
  "Branch leadership review - reopen zip · adjust · defer":   ("lead", "full"),
  "Continuity - prefer same clinician":                       ("clin", "full"),
},
"episode": {
  "Auth verifies eligibility keys pending auth":              ("auth", "mvp"),
  "Evaluate own capacity for the week":                       ("clin", "mvp"),
  "Recert window opens - last 5 days":                        ("clin", "mvp"),
  "MD notified inside 48 hours":                              ("dcs",  "mvp"),
  "Intake receives the referral":                             ("intake", "full"),
  "Group visits geographically":                              ("clin", "full"),
  "Routed on drive time, not distance":                       ("clin", "full"),
},
"routine": {
  "Evaluate own capacity for the week":                       ("clin", "mvp"),
  "Group visits geographically":                              ("clin", "full"),
  "Route - HCHB suggests, clinician adjusts":                 ("clin", "full"),
},
"auth": {
  "Pending auth derived from the payer":                      ("auth", "mvp"),
  "Cap approached - re-auth requested":                       ("auth", "mvp"),
  "Intake receives in Commure":                               ("intake", "full"),
  "Eligibility and benefits verified":                        ("auth", "full"),
  "Released to scheduling":                                   ("auth", "full"),
},
"dcs": {
  "Eligibility verified, pending auth derived from the payer": ("auth", "mvp"),
  "MD notified inside 48 hours":                               ("dcs",  "mvp"),
  "Referral captured in Commure":                              ("intake", "full"),
  "Released to scheduling":                                    ("auth", "full"),
},
"recert": {},
}

# Ghosted steps that come BACK in release 1. The editorial line: visualisation cures
# invisibility, it does not cure workload. A ghost stays ghosted only where simply seeing
# the thing is the fix.
RESTORE = {
"soc": {},
"episode": {
  "Eight tasks for one decision the per-discipline explosion":  "hchb",
  "The weekly logic is undocumented and entirely unassisted":   "clin",
},
"routine": {
  "Each submission generates its own assignment task":          "hchb",
  "Day-before calls are unpaid evening work":                   "clin",
  "The weekly logic is undocumented and unassisted":            "clin",
},
"auth": {
  "~50 pending-auth workflows a day so schedulers bulk-clear without reading": "pcc",
},
"dcs": {},
"recert": {},
}

HELPERS = ["eng", "assist", "surf", "man", "ghost"]

PRELUDE = '''
__VIS__ = True
# The visualise-only helpers redraw THROUGH the generator's own surf()/block(), which are
# themselves guarded — so the guard has to stand down while we are inside one.
__D__ = [0]
__REL__ = {rel!r}
__RES__ = {res!r}
__MVP__ = {mvp!r}
P2_EDGE = "#5F8A12"

def __key__(lines):
    return " ".join(lines).replace("\\u2014", "-").replace("\\u2019", "'").strip()

def __vis_lit__(x, y, w, h, person, lines, small=False, badge=None, n=None):
    """VISUALISED — the tool shows this in release 1. Person's colour, engine stripe."""
    __D__[0] += 1
    try:
        surf(x, y, w, h, C[person] if isinstance(person, str) and person in C else person,
             lines, small=small, badge=badge, n=n)
    finally:
        __D__[0] -= 1

def __vis_p2__(x, y, w, h, person, lines, small=False, badge=None, n=None, label="PHASE 2"):
    """Not in release 1 — drawn in the actor's colour, with the horizon marked."""
    col = C[person] if isinstance(person, str) and person in C else person
    # the horizon beats whatever posture badge the target sheet carried: a block that still
    # says ASSIST here would read as release-1 scope, which is the one thing these sheets deny
    block(x, y, w, h, col, lines, small=small, badge=label, bc=P2_EDGE)
    add(f'<line x1="{{x+4}}" y1="{{y+h+3}}" x2="{{x+w-4}}" y2="{{y+h+3}}" stroke="{{P2_EDGE}}" '
        f'stroke-width="2.4" stroke-dasharray="6 4"/>')
    if n: xref(x, y, n)

def __vis_route__(kind, x, y, w, h, lines, person=None, small=False, badge=None, n=None):
    k = __key__(lines)
    if kind == "surf":
        # the engine only ever showed it — that IS release 1
        return __vis_lit__(x, y, w, h, person, lines, small, badge, n)

    hit = __REL__.get(k)
    if not hit:
        # an assist keeps the actor it already names; an unlisted engine block has none
        return __vis_p2__(x, y, w, h, person if kind == "assist" else MUT,
                          lines, small, badge, n)
    who, when = hit
    # an assist block already carries the colour of whoever decides; do not override it
    actor = person if kind == "assist" else who
    if __MVP__ and when == "full":
        return __vis_p2__(x, y, w, h, actor, lines, small, badge, n, label="NOT IN MVP")
    return __vis_lit__(x, y, w, h, actor, lines, small, badge, n)

def __vis_ghost__(x, y, w, h, lines, **kw):
    who = __RES__.get(__key__(lines))
    if who is None:
        __D__[0] += 1                     # leave it ghosted — seeing it IS the fix
        try:
            return ghost(x, y, w, h, lines, **kw)
        finally:
            __D__[0] -= 1
    n = kw.get("n")
    __vis_p2__(x, y, w, h, who, lines, small=True, n=n, label="STILL A STEP")
'''


def build(flow, mvp, out):
    gen, nice = FLOWS[flow]
    src = (HERE / gen).read_text()

    # route each posture helper through the visualise-only vocabulary
    for h in HELPERS:
        m = re.search(rf"^(def {h}\(([^)]*)\):\n)", src, re.M)
        if not m:
            continue
        args = m.group(2)
        if h == "ghost":
            # ghost() is not spelled the same in every generator — the SOC sheet's has no
            # label/above. Forward only the parameters this one actually declares.
            opt = ", ".join(f"{k}={k}" for k in ("n", "label", "above") if k in args)
            guard = (f"    if __VIS__ and not __D__[0]: return __vis_ghost__("
                     f"x, y, w, h, lines{', ' + opt if opt else ''})\n")
        elif h == "eng":
            guard = ("    if __VIS__ and not __D__[0]: return __vis_route__('eng', x, y, w, h, lines, "
                     "small=small, badge=badge, n=n)\n")
        elif h == "man":
            continue                      # manual work is unchanged in release 1
        else:
            guard = (f"    if __VIS__ and not __D__[0]: return __vis_route__({h!r}, x, y, w, h, lines, "
                     "person=person, small=small, badge=badge, n=n)\n")
        src = src[:m.end(1)] + guard + src[m.end(1):]

    src = PRELUDE.format(rel=RELEASE[flow], res=RESTORE[flow], mvp=mvp) + "\n" + src

    # re-label the sheet: it is no longer the target state
    scope = "MVP" if mvp else "FULL SCENARIO"
    src = src.replace("TARGET STATE", f"VISUALISE ONLY · {scope}")
    src = src.replace("target state", f"visualise only — {scope.lower()}")
    src = src.replace(
        "green = the capacity & scheduling engine (dark text); purple = still inside HCHB",
        "a green stripe = the tool shows it; a dashed green edge = a later phase; purple = HCHB")
    src = src.replace(
        "Green = the capacity & scheduling engine (dark text); purple = still inside HCHB.",
        "A green stripe = the tool shows it; a dashed green edge = a later phase; purple = HCHB.")
    src = src.replace("A dashed, struck-through block is a step that no longer exists",
                      "The tool shows; it does not act. A dashed green edge is a later phase")
    src = src.replace("same blocks, same positions; only fill and wording change",
                      "same blocks, same positions. The tool shows; it does not act")
    src = src.replace("Capacity & Scheduling Engine", "Shown by the tool")
    src = src.replace("PROPOSED \u00b7 a green stripe", "PROPOSED \u00b7 a green stripe")

    ns = {"__REC__": [], "__name__": "__vis__"}
    argv = sys.argv
    sys.argv = ["gen", out]
    try:
        exec(compile(src, gen, "exec"), ns)
    finally:
        sys.argv = argv
    return ns["W"], ns["H"], nice


if __name__ == "__main__":
    flow, scope, out = sys.argv[1:4]
    W, H, nice = build(flow, scope == "mvp", out)
    print(f"{flow:8} {scope:4} -> {out}  ({W}x{H})  {nice}")
