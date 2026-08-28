# Power BI — the flow map as a hover-over report

Reproduces the hover layer natively in Power BI: **hover a step on the map, see the workbook
variables behind it.** No custom visuals, no embedded code, no domain allow-listing — and it drops
onto a SharePoint page through the first-party **Power BI web part**.

This exists because the interactive HTML version cannot be used: modern SharePoint pages strip
`<script>`, and the iframe route needs a tenant domain allow-list that is not going to be granted.
Power BI needs neither.

## Regenerating

    python3 _powerbi_export.py

Writes everything in this folder from `variables.json` and the `vmap-*.json` files. Re-run after
editing a vmap or re-importing the workbook.

## What is here

| File | What it is |
|---|---|
| `variables.csv` | Dimension. 87 rows, one per workbook variable, all columns including **MVP** and **Future role** |
| `blocks.csv` | Dimension. 119 rows — one per step across four flows, with geometry and its posture under **all three states** |
| `block_variables.csv` | Bridge. 273 rows, block ↔ variable, many-to-many |
| `background-<flow>-<state>.png` | 12 images, each cropped to the **exact drawing canvas** so the percentages in `blocks.csv` land on the artwork with no fudging |

Flows covered: SOC / ROC (30 blocks), Full Episode (40), DCS / Scheduler (24), Routine Visits (25).

## Model

    variables.csv  1 ──< block_variables.csv >── 1  blocks.csv
                   Id                      Flow + Block

Relate `block_variables[Id]` → `variables[Id]` and `block_variables[Block]` → `blocks[Block]`.
Both single-direction, filtering from the dimension into the bridge.

## Build

1. **Page size.** Format page → Canvas settings → Custom, matching the flow's aspect. SOC/ROC is
   2600×1780, so **1300 × 890**. `blocks.csv` carries `CanvasW` / `CanvasH` for each flow. Getting
   this wrong is the only thing that misaligns the hotspots.
2. **Background.** Format page → Canvas background → the PNG → Image fit **Fit**, transparency **0%**.
3. **The hotspot layer.** A **Scatter chart** sized to the whole page.
   - X → `blocks[X]`, Y → `blocks[Y]`, Details → `blocks[Block]`, Size → `blocks[BubbleSize]`
   - X and Y axis range **Min 0, Max 100**, then both axes **off**; gridlines, title and
     background off
   - `Y` is already flipped — the scatter plots upward, the canvas measures downward
   - Legend → `blocks[MVP]` (or `[Dashboard]` / `[Target]`) to colour the hotspots by state
4. **The tooltip.** New page → Page information → **Allow use as tooltip** on; page size Tooltip.
   Put a table on it: `variables[Id]`, `Variable`, `Future role`, `MVP`, `Gating`, `Confidence`,
   `Where it lives today`, `Why this posture`.
5. Back on the map page: select the scatter → Format → **Tooltip → Report page →** that page.

Hovering a step now shows only that step's variables, because the bridge carries the filter.

## Driving it live from the workbook

Change an **MVP** cell, refresh, the map re-colours. No redraw, no new export.

- **Changes live:** hotspot colours and everything in the tooltip.
- **Does not change:** the background image. Artwork, block positions and wording are fixed. For a
  live view that is what you want — and it means the background should be the **plain
  current-state map**, with Power BI carrying all the state colour.

Put the workbook in SharePoint / OneDrive, connect to the **Master List** sheet, publish, set
**Scheduled refresh** (Pro 8/day, Premium 48/day). Excel on SharePoint has no DirectQuery, so a
cell edit appears at the next refresh, not instantly.

**Compute the posture in Power Query, not DAX.** A block is in scope when a majority of its
variables are MVP = Yes; its posture is the *most common* role among those, ties broken toward the
weaker posture. In Power Query that is a Group By, a filter, a count and a sort. The same logic in
DAX needs a TOPN over a summarised table with two sort keys, for no benefit — nothing here responds
to slicers.

Take ties toward the **weaker** posture deliberately. On strongest-wins, 18 of 19 in-scope blocks on
routine visits came out `Automate` because one variable in each did.

**`Future role` is live too.** Changing a variable from Assist to Automate moves the map just as
much as changing its MVP flag. Say so before the first demo.

## Notes that will save someone an afternoon

- **Circles, not rectangles.** Scatter markers are round, so the hit area approximates the block.
  `BubbleSize` scales them by real footprint. `LeftPct` / `TopPct` / `WidthPct` / `HeightPct` are in
  the file if you would rather place transparent **buttons** for exact rectangles — but buttons
  carry only plain-text tooltips, not the filtered variable table. Start with the scatter.
- **`Removed`** in the state columns means the step stops existing in that state. It is carried by
  hand in `_flow_vis.py`'s `REMOVED` table because the workbook cannot express it — the workbook
  says how far the tool goes on a *variable*, never that a *step* disappears.
- **`View`** means the step is on the dashboard but the engine has not reached it in that state.
- **Licensing.** Viewers need Power BI Pro, or the workspace on Premium / Fabric capacity.

## The limit that is not Power BI's fault

`Where it lives today` = Tacit or Manual means nothing records that variable, so no report can show
it. Those steps render dark however good the model is — they need **capture** built first, which is
a separate workstream from the dashboard.
