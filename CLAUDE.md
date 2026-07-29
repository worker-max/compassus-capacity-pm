# Project Memory — Compassus Capacity & Scheduling

This repo holds the **knowledge and PM context** for the Compassus capacity &
scheduling initiative. A future session should read this file, then the knowledge
base, before doing capacity/staffing work.

## Read first (ground truth, reason from these)

- `agents/compassus-capacity-pm/knowledge/discovery-session.md` — the primary discovery ground truth.
- `agents/compassus-capacity-pm/knowledge/capacity-scheduling-summary.md` — two-function framing, CP-1…CP-10, open questions.
- `agents/compassus-capacity-pm/knowledge/staffing-model.md` — **the staffing model** (full design, decisions, demo norms, corrections).
- `agents/compassus-capacity-pm/AGENT.md` + `initiative-playbook.md` — agent identity and phased program.

## The staffing model (current active workstream)

A per-discipline, per-branch home health **staffing model** that finds the
"Goldilocks" headcount — enough to protect quality at current census and absorb
growth, without overstaffing any discipline into low visits-per-clinician (which
hurts branch economics *and* clinician pay). **It recommends; the regional leader
decides.** Full detail in `knowledge/staffing-model.md`. In one line:

```
ADC → attach-rate demand → visit-equivalent points → visit-load vs caseload binding
→ per-discipline turnover waterfall → maintain-vs-grow → FT core / flex split → regional override
```

Load-bearing facts to preserve across sessions:
- **Point weights (LOCKED):** routine 1.0 · eval 1.5 · SOC 2.5 · recert 1.75 · ROC 2.5 · therapy reassess 1.25. Productivity standard **30 pts/FTE/productive week**. These define discovery **open question #1** (the shared-currency point system).
- **Census overstates demand** — use per-discipline attach rates + BLENDED (not peak) visits/patient/week. Dual ceiling: `max(points-FTE, caseload-FTE)`.
- **Turnover waterfall non-overlap contract:** L2 availability (tenured PTO) → L3 `×(1 + ramp×turnover)` (ramp scales with churn — NOT flat) → L4 ÷(1−vacancy). Binding risk is **time-to-fill, not turnover frequency**.
- **Geography is the biggest lever** (metro 1.00 / mixed 0.85 / rural 0.68 productivity factor).
- **Per-diem is perishable** — size the pool to cover the vacancy+PTO gap AND keep each per-diem above a keep-warm floor (~5 visits/wk).
- **HHA is a separate currency** (aide-visit units), kept out of the clinical FTE total.
- **Two default decisions pending user confirmation (D1, D2):** 30 pts = per productive week (L2 separate); turnover lands in both a modest FT buffer and the per-diem pool.

## Cross-repo pointer (the built tool lives elsewhere)

The **working tool** is in **`worker-max/Aethergrid`**, branch
`claude/home-health-staffing-model-e7j6q6`, under `docs/staffing-model/`:
- `staffing-workbook.html` — interactive live calculator (ADC hero, demo-populate, per-diem/waterfall, CSV export).
- `staffing-workbook.xlsx` — live-formula spreadsheet (Excel / Google Sheets).
- `README.md` — the source design spec.

Keep this repo's `knowledge/staffing-model.md` and Aethergrid's `docs/staffing-model/`
in sync when the model changes.

## Working conventions

- Development branch for this workstream: `claude/home-health-staffing-model-e7j6q6` (both repos).
- These are internal Compassus operational materials — work in aggregates/operational signals; **no raw PHI** in this repo.
- When the model changes, update BOTH the knowledge doc here and the tool/spec in Aethergrid, and note any decision-registry (D1–D14) resolutions.
