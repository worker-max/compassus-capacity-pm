# The house business-case format

> **Source.** "Business use cases" — Google Drive `1tAILpvwtEzLLCHv6XoLqasvYAfmlURIrhGWkfFpiiT4`,
> shared 21 Aug 2026. The document is one screenshot plus a short instruction. The PDF export is
> beside this file as `business-case-format-source.pdf`. Transcribed here because the numbers in
> the screenshot are the only published scale anchors we have for the home health business.

## The instruction, verbatim in substance

Start thinking about the business case for the scheduling effort. The screenshot shows how business
cases are typically laid out here. The hard savings levers go on the waterfall; the less certain,
harder to measure items are called out on the right. Claude can build an Excel model where the
assumptions can be played with, and then generate this output.

## The worked example — AI Coding, ICD-10 + QA

Title line: **AI Coding | ICD-10 + QA — $5.6M in Annual Net Value**
Subtitle: ICD-10 outsourced to a vendor, QA in-house with an AI tool at no cost, base case before
upside levers.

### Left panel — the waterfall

Titled "Annual Net Value Build-up." Three series: **value driver** (green), **cost** (red),
**subtotal / net** (navy). Read left to right, subtotals interrupting the run.

| Bar | Type | Amount |
|---|---|---|
| ICD-10 vendor avoided | value | +3.15M |
| Replacement vendor cost | cost | −1.05M |
| **ICD-10 Net** | subtotal | **2.10M** |
| QA vendor avoided | value | +1.12M |
| Face-to-face reduction | value | +0.75M |
| DCS turnover reduction | value | +0.21M |
| QA managers (7) | cost | −0.98M |
| QA AI tool | cost | 0 (free) |
| Central QA reduction | value | +2.40M |
| **QA Net** | subtotal | **3.50M** |
| **Total net benefit** | net | **5.60M** |

Gold summary bar beneath: direct economics 7.6M value − 2.0M cost = 5.6M net annual benefit,
276 percent ROI, split ICD-10 2.1M and QA 3.5M.

### Right panel — the upside

Dark navy, headed **THE UPSIDE**: three upside levers on top of the base case.

| Lever | Value | Basis given |
|---|---|---|
| Reimbursement uplift | 5.5M | More accurate primary diagnosis and comorbidity capture under PDGM — **1.0 percent of 549M home health revenue** |
| Value-based performance | 1.3M | Coding accuracy supports acuity capture and quality scores — **0.5 percent VBP swing on 260M in-scope episodic revenue** |
| Productivity improvements | Not yet valued | Placeholder callout — faster turnaround, capacity for growth, reduced LUPA risk |

Footer of the panel: quantified upside 6.8M per year and up.

## What this tells us beyond the format

- **Home health revenue is on the order of 549M dollars.** Every percentage lever we propose should
  be expressed against this, the way the coding case was.
- **In-scope episodic revenue is on the order of 260M dollars**, roughly 47 percent of the total.
  The remaining 53 percent is non-episodic. That is independent corroboration, from finance's own
  model, that the book is majority non-traditional-Medicare.
- **A 0.5 percent VBP swing is the accepted modelling convention here**, against episodic revenue
  only, not against total revenue.
- **Turnover reduction is already accepted as a hard waterfall lever**, not an upside item — the
  coding case puts DCS turnover reduction at 0.21M on the waterfall itself.
- **A placeholder already names reduced LUPA risk and capacity for growth** as unvalued
  productivity upside. That is precisely the ground the capacity and scheduling initiative covers,
  and it is currently sitting in someone else's business case as an unquantified footnote.

## Conventions to match

- Hard, countable, removable cost goes on the waterfall. Probabilistic or behaviour-dependent value
  goes in the right panel.
- Costs are shown explicitly and netted, not hidden. The AI tool at zero cost is still drawn.
- Subtotals break the waterfall into named workstreams, each with its own net.
- ROI is stated as a percentage against cost, alongside the net.
- Upside levers are expressed as a percentage of a named revenue base, with the base stated.
- One lever is allowed to be "not yet valued" with a named owner to fill it.
