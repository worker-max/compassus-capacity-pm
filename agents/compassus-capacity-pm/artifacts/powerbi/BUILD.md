# Power BI — the flow map as a hover-over report

Reproduces the hover layer natively in Power BI: hover a step on the map, see the workbook
variables behind it. No custom visuals, no embedded code, no domain allow-listing — and it drops
onto a SharePoint page through the first-party **Power BI web part**.

## What is in this folder

| File | What it is |
|---|---|
| `background-future-state-visualization-mvp.png` | Release-1 map, cropped to the exact drawing canvas (4400 x 3360) |
| `background-future-state-mvp.png` | Future-state MVP map, same canvas |
| `variables.csv` | Dimension. One row per workbook variable — 87 rows straight from the Master List, including **MVP** and **Future state -- the tool's role** |
| `blocks.csv` | Dimension. One row per step on the map, with its position as a percentage of the canvas |
| `block_variables.csv` | Bridge. Block ↔ variable, many-to-many |

The images are cropped to the SVG canvas exactly, so the percentages in `blocks.csv` land on the
artwork with no fudging.

## Model

    variables.csv  1 ──< block_variables.csv >── 1  blocks.csv
                   Id                    Flow + Block

Relate `block_variables[Id]` to `variables[Id]`, and `block_variables[Block]` to `blocks[Block]`.
Both single-direction, filtering from the dimension to the bridge.

## Build

1. **Page size.** Format page → Canvas settings → Custom, **1100 x 840**. This matches the image
   aspect exactly (2200:1680). Getting this wrong is the only thing that will misalign the hotspots.
2. **Background.** Format page → Canvas background → the PNG → Image fit **Fit**, transparency **0%**.
3. **The hotspot layer.** Add a **Scatter chart** and size it to the whole page.
   - X Axis → `blocks[X]`, Y Axis → `blocks[Y]`, Values/Details → `blocks[Block]`
   - Size → `blocks[BubbleSize]` (approximates each step's footprint)
   - X and Y axis: set range **Min 0, Max 100**, then turn both axes **off**
   - Turn off gridlines, title, and background; set the marker fill transparency high (85–100%)
   - `Y` is already flipped for you — the scatter plots upward, the canvas measures downward
4. **The tooltip.** New page → Page information → **Allow use as tooltip** on. Page size →
   Tooltip (320 x 480 or so). Put a table on it: `variables[Id]`, `Variable`, `Constraint`, `MVP`,
   `Posture`, `Gating`, `Confidence`, `Current`, `Sot`, `Notes`.
5. Back on the map page: select the scatter → Format → **Tooltip → Report page →** your tooltip page.

Hovering a step now shows only that step's variables, because the bridge carries the filter.

## Worth knowing

- **Hover works in the service and in the SharePoint web part.** On a touch screen it is a tap.
- **Circles, not rectangles.** Scatter markers are round, so the hit area approximates the block.
  `BubbleSize` scales them by real footprint; `LeftPct`/`TopPct`/`WidthPct`/`HeightPct` are in the
  file too if you would rather place transparent **buttons** by hand for exact rectangles — buttons
  give a precise hit area but only carry plain-text tooltips, not the variable table.
- **The `Posture` column** on `blocks.csv` holds `Automate` / `Assist` / `Surface` /
  `Out of MVP scope`. Put it on the scatter's legend and the hotspots colour themselves.
- **Licensing.** Viewers need Power BI Pro, or the workspace on Premium/Fabric capacity.

## The limit that is not Power BI's fault

`Current` = `Tacit` or `Manual` means nothing records that variable today, so no report can show it.
20 of the 47 MVP variables are in that state. Power BI will render those blocks dark no matter how
good the model is — they need capture built first. That is the same gap the dashed outlines mark on
the MVP sheet.

## Currently only routine visits

`blocks.csv` and `block_variables.csv` cover Flow 2. The other flows need their block-to-variable
map authored before they can be added; the schema does not change, the rows just extend.


---

## Driving it live from the workbook

The whole point: change an **MVP** cell in the workbook, refresh, and the map re-colours. No
redraw, no new export. This works, with one boundary worth stating plainly.

**What changes live:** the hotspot colours and everything in the tooltip — scope, posture, decider,
confidence, notes.

**What does not:** the background image. The artwork, the block positions and the wording are
fixed. So the map does not redraw itself; the layer over it does. For a live view that is what you
want anyway — and it means the background should be the **plain current-state map**, with Power BI
carrying all the state colour, rather than a pre-coloured one. `Flow-Routine-Visits.pdf`'s artwork
is the right background for that build.

**Wiring**

1. Put `CapacitySchedulingVariableWorkbook.xlsx` in SharePoint or OneDrive for Business.
2. Power BI Desktop → Get data → SharePoint folder / Web → the **Master List** sheet.
3. Keep `blocks.csv` and `block_variables.csv` as they are — geometry and the block-to-variable
   join do not change when someone edits the MVP column.
4. Publish, then set **Scheduled refresh** on the dataset. Pro allows 8 refreshes a day,
   Premium/Fabric 48. Excel on SharePoint does not support DirectQuery, so a cell edit shows up at
   the next refresh, not instantly.

**Computing the posture — do it in Power Query, not DAX.** The rule is: a block is in scope when a
majority of its variables are MVP = Yes, and its posture is the *most common* role among those,
ties broken toward the weaker posture. In Power Query that is a Group By on Block, a filter to
MVP = Yes, a count per Role, and a sort — a few steps, evaluated at refresh. The same logic in DAX
needs a TOPN over a summarised table with two sort keys and is markedly harder to read for no
benefit, since nothing here needs to respond to slicers.

Take ties toward the weaker posture deliberately. On the strongest-wins rule, 18 of 19 in-scope
blocks on routine visits came out `Automate` because one variable in each did — which is not what
the workbook says.

**The MVP column is not the only live column.** `Future state -- the tool's role` drives the
posture just as directly. If someone changes a variable from Assist to Automate, the map moves too.
That is correct, and worth saying out loud before the first demo so nobody is surprised.
