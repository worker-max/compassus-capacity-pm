# -*- coding: utf-8 -*-
"""_flow_live — turn any flow-map generator into a hoverable sheet, without editing it.

    python3 _flow_live.py <generator.gen.py> <hotspot-map.json> <out.html> "<Title>"

How it works. The generator is executed with its block-drawing helpers instrumented, so
every block reports its own geometry and text. Nothing it draws changes — the SVG this
produces is byte-identical to the shipped sheet. The geometry is then used to lay a
transparent hit-layer over the finished drawing, and each hot spot carries the workbook
IDs for that block. Hover fires a panel; the sheet underneath is untouched, so the PDF
pipeline and the printed wall sheet are unaffected.

The block -> variable mapping lives in the hotspot JSON, keyed on the block's own text.
That is the only file to edit when the workbook moves.
"""
import json
import pathlib
import re
import sys

HELPERS = ["block", "eng", "assist", "surf", "man", "ghost", "chip"]
SKILL = pathlib.Path("/home/user/compassus-capacity-pm/.claude/skills/process-flow-map/assets")


def instrument(src):
    """Insert a recording call as the first statement of each block-drawing helper."""
    for h in HELPERS:
        pat = re.compile(rf"^(def {h}\(([^)]*)\):\n)", re.M)
        m = pat.search(src)
        if not m:
            continue
        args = m.group(2)
        # every helper's first four positional args are x, y, w, h
        rec = ("    __REC__.append((x, y, w, h, "
               "[a for a in (lines if isinstance(lines, list) else []) ], "
               f"{h!r}))\n")
        src = src[:m.end(1)] + rec + src[m.end(1):]
    return src


def run(gen_path):
    src = pathlib.Path(gen_path).read_text()
    src = instrument(src)
    # the generator writes to sys.argv[1]; give it a sink it will never be asked for
    ns = {"__REC__": [], "__name__": "__live__"}
    old_argv = sys.argv
    sys.argv = ["gen", "/dev/null"]
    try:
        exec(compile(src, gen_path, "exec"), ns)
    finally:
        sys.argv = old_argv
    svg = "\n".join(ns["out"])
    return svg, ns["__REC__"], ns["W"], ns["H"]


def key_of(lines):
    return " ".join(lines).replace("—", "-").replace("’", "'").strip()


def main():
    gen, mapfile, out_html, title = sys.argv[1:5]
    svg, rec, W, H = run(gen)
    vmap = json.loads(pathlib.Path(mapfile).read_text())
    variables = json.loads((pathlib.Path(gen).parent / "variables.json").read_text())

    # surf/man/assist call block() internally, so the same footprint reports twice —
    # the outer helper records first, and that is the one that knows the posture.
    seen, uniq = set(), []
    for r in rec:
        fp = r[:4]
        if fp in seen:
            continue
        seen.add(fp)
        uniq.append(r)
    rec = uniq

    hot, unmapped = [], []
    for x, y, w, h, lines, kind in rec:
        if not lines:
            continue
        k = key_of(lines)
        ids = vmap.get(k)
        if ids is None:
            unmapped.append(k)
            continue
        if not ids:                      # deliberately mapped to nothing
            continue
        hot.append({"x": x, "y": y, "w": w, "h": h, "v": ids, "t": k, "k": kind})

    for k in unmapped:
        print("  unmapped:", k)
    print(f"{len(hot)} hot spots · {len(unmapped)} unmapped · {len(rec)} blocks drawn")

    layer = ['<g id="hits">']
    for i, s in enumerate(hot):
        layer.append(f'<rect class="hit" data-i="{i}" x="{s["x"]}" y="{s["y"]}" '
                     f'width="{s["w"]}" height="{s["h"]}" rx="5"/>')
    layer.append("</g>")
    svg = svg.replace("</svg>", "\n".join(layer) + "\n</svg>")

    tpl = (SKILL / "wrapper.html").read_text()
    page = (tpl.replace("__SVG__", svg).replace("__TITLE__", title)
               .replace("__W", str(W)).replace("__H", str(H)))
    page += LIVE.replace("__HOT__", json.dumps(hot, ensure_ascii=False)) \
                .replace("__VARS__", json.dumps(variables, ensure_ascii=False))
    pathlib.Path(out_html).write_text(page)
    print("wrote", out_html)


LIVE = r"""
<aside id="vp" hidden>
  <header><b id="vp-t"></b><button id="vp-x" aria-label="close">&times;</button></header>
  <div id="vp-b"></div>
  <footer id="vp-f"></footer>
</aside>
<p id="vp-hint">Hover any block to see the variables behind it &middot; click to pin
&middot; <b>Esc</b> to clear. Nothing here is on the printed sheet.</p>

<style>
#vp-hint{max-width:1900px;margin:14px auto 0;font-family:var(--mono);font-size:12.5px;
  color:#7C8781;letter-spacing:.03em}
#vp-hint b{color:#5A6560}
.hit{fill:transparent;cursor:pointer;pointer-events:all}
.hit:hover,.hit.pin{fill:#A6E22E;fill-opacity:.20;stroke:#A6E22E;stroke-width:3.5}
.hit.pin{stroke-dasharray:6 4}
#vp{position:fixed;right:clamp(10px,2vw,26px);top:clamp(10px,2vw,26px);width:min(380px,92vw);
  max-height:calc(100vh - 52px);overflow-y:auto;background:#FBFBF8;border:1px solid #C9CCC5;
  border-radius:12px;box-shadow:0 18px 48px -20px rgba(23,30,26,.5);z-index:9;
  font-family:var(--body);color:#1B211E}
#vp[hidden]{display:none}
#vp.left{right:auto;left:clamp(10px,2vw,26px)}
#vp header{display:flex;gap:10px;align-items:flex-start;padding:14px 14px 10px;
  border-bottom:1px solid #E9E9E5;position:sticky;top:0;background:#FBFBF8;border-radius:12px 12px 0 0}
#vp header b{flex:1;font-size:14.5px;line-height:1.35}
#vp-x{border:0;background:none;font-size:21px;line-height:1;color:#7C8781;cursor:pointer;padding:0 2px}
#vp-b{padding:4px 14px 10px}
.v{padding:12px 0;border-bottom:1px solid #EFEFEA}
.v:last-child{border-bottom:0}
.v .id{font-family:var(--mono);font-size:11.5px;letter-spacing:.07em;color:#5F8A12;font-weight:700}
.v .nm{font-size:14.5px;font-weight:600;margin:3px 0 7px;line-height:1.35}
.v .nt{font-size:13px;color:#5A6560;line-height:1.5;margin-top:7px}
.tags{display:flex;flex-wrap:wrap;gap:5px}
.tag{font-family:var(--mono);font-size:10.5px;letter-spacing:.05em;padding:2.5px 7px;
  border-radius:9px;border:1px solid #C9CCC5;color:#5A6560;white-space:nowrap}
.tag.hard{border-color:#792E2E;color:#792E2E}
.tag.gate{border-color:#DF751D;color:#DF751D}
.tag.mvp{border-color:#5F8A12;color:#4A6D0E;background:#F4FBE6}
.tag.lo{border-color:#792E2E;color:#792E2E}
#vp footer{padding:10px 14px 13px;border-top:1px solid #E9E9E5;font-family:var(--mono);
  font-size:11px;letter-spacing:.05em;color:#7C8781;line-height:1.6}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]) #vp{background:#161B18;
  border-color:#2C342E;color:#E8EBE7}
  :root:not([data-theme="light"]) #vp header{background:#161B18;border-color:#2C342E}
  :root:not([data-theme="light"]) .v{border-color:#232A25}
  :root:not([data-theme="light"]) #vp footer{border-color:#2C342E}
  :root:not([data-theme="light"]) .v .nt,:root:not([data-theme="light"]) .tag{color:#9AA69F}}
@media print{#vp,#vp-hint,#hits{display:none}}
</style>

<script>
const HOT = __HOT__, VARS = __VARS__;
const vp = document.getElementById('vp'), vpT = document.getElementById('vp-t'),
      vpB = document.getElementById('vp-b'), vpF = document.getElementById('vp-f'),
      hits = document.getElementById('hits');
let pinned = null;

const esc = s => String(s ?? '').replace(/[&<>]/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;'}[c]));

function tags(d){
  const t = [];
  if (d.constraint) t.push(`<span class="tag${/Hard/.test(d.constraint)?' hard':''}">${esc(d.constraint)}</span>`);
  if (d.mvp === 'Yes') t.push('<span class="tag mvp">MVP</span>');
  else if (d.mvp) t.push(`<span class="tag">MVP ${esc(d.mvp)}</span>`);
  if (d.posture) t.push(`<span class="tag">${esc(d.posture)}</span>`);
  if (d.gating === 'Y') t.push('<span class="tag gate">GATING</span>');
  if (d.confidence) t.push(`<span class="tag${d.confidence==='Low'?' lo':''}">conf ${esc(d.confidence)}</span>`);
  if (d.current) t.push(`<span class="tag">${esc(d.current)}</span>`);
  return `<div class="tags">${t.join('')}</div>`;
}

function show(i){
  const s = HOT[i];
  vpT.textContent = s.t;
  vpB.innerHTML = s.v.map(id => {
    const d = VARS[id];
    if (!d) return `<div class="v"><span class="id">${esc(id)}</span>
      <div class="nt">not in the 13 Aug inventory — check the backlog</div></div>`;
    return `<div class="v"><span class="id">${esc(id)} &middot; ${esc(d.layer)}</span>
      <div class="nm">${esc(d.variable)}</div>${tags(d)}
      ${d.notes ? `<div class="nt">${esc(d.notes)}</div>` : ''}
      ${d.sot ? `<div class="nt"><b>Source of truth:</b> ${esc(d.sot)}${
        d.sourced ? ` &middot; sourced by ${esc(d.sourced)}` : ''}</div>` : ''}</div>`;
  }).join('');
  const n = s.v.length;
  vpF.textContent = `${n} variable${n===1?'':'s'} · 13 Aug workbook inventory`;
  // keep the panel off the block being read
  const r = document.querySelector(`.hit[data-i="${i}"]`).getBoundingClientRect();
  vp.classList.toggle('left', r.left + r.width / 2 > window.innerWidth / 2);
  vp.hidden = false;
  hits.classList.add('on');
}

function clear(){
  if (pinned !== null) return;
  vp.hidden = true;
  hits.classList.remove('on');
}

document.querySelectorAll('.hit').forEach(el => {
  const i = +el.dataset.i;
  el.addEventListener('mouseenter', () => { if (pinned === null) show(i); });
  el.addEventListener('mouseleave', clear);
  el.addEventListener('click', e => {
    e.stopPropagation();
    document.querySelectorAll('.hit.pin').forEach(p => p.classList.remove('pin'));
    if (pinned === i) { pinned = null; clear(); return; }
    pinned = i; el.classList.add('pin'); show(i);
  });
});

function unpin(){
  pinned = null;
  document.querySelectorAll('.hit.pin').forEach(p => p.classList.remove('pin'));
  clear();
}
document.getElementById('vp-x').addEventListener('click', unpin);
document.addEventListener('keydown', e => { if (e.key === 'Escape') unpin(); });
document.addEventListener('click', e => { if (!vp.contains(e.target)) unpin(); });
</script>
"""

if __name__ == "__main__":
    main()
