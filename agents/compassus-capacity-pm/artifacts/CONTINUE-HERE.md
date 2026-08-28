# Continue here — flow maps, states, and the Power BI hover concept

State of play as of **27 Aug 2026**. Read this before touching the flow sheets.

## The four states, in order

Two of the four are future states — the dashboard and MVP are different evolutions of the same
future, and they are **cumulative**: MVP keeps everything the dashboard gives you and adds the
engine on top.

| # | State | What it says |
|---|---|---|
| 1 | **Current State** | today. The base generators, already signed off |
| 2 | **Future State · Dashboard Visualization** | reports from HCHB, Workday, Commure, routing and telephony pulled into one view. Green outline on every step that gains it. **Nothing automated.** Full scope |
| 3 | **Future State · MVP** | the dashboard **plus** the engine on `MVP = Yes` variables. Steps the engine has not reached **keep their outline** |
| 4 | **Target State** | optimal functionality, every variable acted on |

    python3 _flow_vis.py <flow> future|mvp|target|both <out.svg>

`both` is for flows where MVP and Target render identically — currently **DCS/Scheduler**, where
every variable behind every block is `MVP = Yes`. One sheet, combined label, rather than two files
that invite a hunt for a difference that is not there.

## Where the data comes from

- **`knowledge/source/CapacitySchedulingVariableWorkbook-2026-08-27.xlsx`** — the source of truth,
  87 variables on the `Master List` tab. Committed so it survives the session that uploaded it.
- **`variables.json`** — derived from it. Regenerate if the workbook changes.
- **`vmap-<flow>.json`** — block → variable IDs, keyed on the block's own text.

**Map a block to the variables behind the decision it embodies, not the data it happens to read.**
Mapping DCS plan-of-care approval to the frequency variables made it posture as `Automate`, which
is wrong — it now maps to `S-49` (review-queue depth) and reads `Surface`.

Posture per block is the **modal** role among the in-scope variables, ties broken toward the
**weaker** posture. Strongest-wins made 18 of 19 blocks read `Automate`.

## Done / not done

| Flow | vmap | Sheets |
|---|---|---|
| SOC / ROC — **the primary flow** | ✅ 30 blocks | ✅ all three, dated `8.27_` |
| Full Episode | ✅ 40 blocks | ✅ all three |
| DCS / Scheduler | ✅ 24 blocks | ✅ dashboard + combined MVP/Target |
| Routine Visits | ✅ 25 blocks | built, not circulated under dated names |
| Recert & Discharge | ❌ | — |
| Authorization | ❌ **cannot be derived** | `S-43` is the only authorization variable in the workbook |

**SOC/ROC is the flow every decision is based on**, then carried outward. Do that first, always.

## The Power BI hover concept — see `powerbi/BUILD.md`

The whole reason it exists: the interactive HTML cannot go on SharePoint (modern pages strip
`<script>`, and the iframe route needs a domain allow-list that will not be granted). Power BI
needs neither and embeds through the first-party web part.

The technique is a **transparent scatter over a page background image with a report-page tooltip**.
`powerbi/` holds the star schema, the geometry as canvas percentages, and 12 exact-canvas
backgrounds. `_powerbi_export.py` regenerates all of it.

Change an MVP cell in the workbook → refresh → the map re-colours. The **background artwork does
not change**, so for a live build the background should be the plain current-state map with Power
BI carrying the state colour.

## Traps already hit — do not re-learn these

- **Hash before you clone.** Drive titles and repo filenames do not agree. A target sheet was once
  built against the wrong original.
- **On a positional clone, a better idea that moves a block is a worse sheet.** Differences go in
  text, badge or fill.
- **`fill="{tc}"` loses to the CSS class** — use `style="fill:{tc}"`.
- **Never suppress stderr on a render.** A `KeyError` once hid behind `2>&1` and stale SVGs shipped.
- **Not every generator says "current state."** The DCS sheet's eyebrow is just the company name;
  without the fallback in `_flow_vis.py` its sheets ship with no state label at all.
- **Footer keys must stay under ~180 characters** — they share a line with the page reference.
- **The ghost label has nowhere to go** on most sheets; dashed + struck-through carries it.
