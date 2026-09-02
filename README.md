# Home Health Tools

Operational tooling and expert agents for home health initiatives.

## Compassus Capacity & Scheduling — Expert Project Manager Agent

The first inhabitant of this repo is the **Home Health Expert Project Manager**: a senior
operational co-pilot designed to lead the Compassus capacity and scheduling initiative — from
planning, through a lighthouse pilot, to scaled rollout across the organization, to standing
governance.

It exists to make finite, geographically-distributed clinical capacity reliably meet variable,
time-sensitive demand — **without harming patients, clinicians, quality, or margin.**

### What's here

| Path | What it is |
|---|---|
| [`agents/compassus-capacity-pm/AGENT.md`](./agents/compassus-capacity-pm/AGENT.md) | The full agent definition — **Qualities & Identity**, **Functionality**, and **Perspective**. |
| [`agents/compassus-capacity-pm/initiative-playbook.md`](./agents/compassus-capacity-pm/initiative-playbook.md) | The phase-by-phase program the agent runs: Discover → Design → Pilot → Scale → Sustain. |
| [`agents/compassus-capacity-pm/knowledge/`](./agents/compassus-capacity-pm/knowledge/) | **The empirical ground truth** — Compassus's own July-2026 discovery work (discovery session + capacity/scheduling analysis). The agent reasons from this first. |
| [`agents/compassus-capacity-pm/artifacts/`](./agents/compassus-capacity-pm/artifacts/) | **The working artifacts** — the capacity / scheduling / engagement model, the variable inventory, the data index, and the source war-list. Start at its [README](./agents/compassus-capacity-pm/artifacts/README.md). |
| [`.claude/agents/compassus-capacity-pm.md`](./.claude/agents/compassus-capacity-pm.md) | A runnable Claude Code subagent — a tight standing prompt you can invoke directly for PM guidance. |
| [`agents/compassus-capacity-pm/vendor-evaluation/`](./agents/compassus-capacity-pm/vendor-evaluation/) | **The vendor scoring system** — the rubric, the one-page guide, the 16-vendor scorecard workbook, and the `/vendor-scorecard` skill that scores a returned questionnaire against the 41-element spec. |

### How to use it

- **As a thinking partner / co-pilot:** invoke the subagent (`.claude/agents/compassus-capacity-pm.md`)
  and put your capacity/scheduling questions, plans, and decisions to it. It reasons in the home
  health operating reality — PDGM, LUPA thresholds, OASIS/recert cycles, HHVBP, the clinical
  disciplines, HCHB/MatrixCare — and gives you a recommendation, its reasoning, and the caveats.
- **As a program backbone:** the initiative playbook gives you the phased structure, the
  phase-gate exit criteria, the KPI set, and the cadence rhythm to run the initiative for real.
- **As a definition to evolve:** `AGENT.md` is the canonical statement of the agent's identity,
  capabilities, and worldview. Refine it as the initiative teaches you what it needs to be.

### The current working model

Capacity, scheduling and engagement as three arenas — **capacity** is the envelope a branch can
deliver against, and **scheduling** and **engagement** are the two coordination activities performed
against it. Priorities come from the primary workbook (`Compassus Capacity & Scheduling Workbook
2026-08-11.xlsx`), not from judgment.

Three views at increasing depth, all in [`artifacts/`](./agents/compassus-capacity-pm/artifacts/):
the **one-pager** (a single landscape page, primary variables only — also rendered to PDF), the
**board** (the three boxes plus every variable per box), and the **diagram** (flow, sketch mapping,
and per-variable constraint / MVP / automation-posture detail).

### The three dimensions (how the agent was built out)

1. **Qualities & Identity** — who it is, the home-health expertise it commands, its traits,
   communication style, and non-negotiable guardrails (patient safety, clinician wellbeing,
   never gaming metrics, PHI/HIPAA discipline).
2. **Functionality** — the five-phase gated program, 15 core jobs-to-be-done, the artifacts it
   maintains, the capacity/scheduling/financial/quality/workforce KPI set, its cadences, and the
   lightweight tooling stack it orchestrates.
3. **Perspective** — the mental models it reasons with (capacity as productive visit-hours by
   discipline by zone; theory of constraints; the utilization–responsiveness curve; the LUPA
   cliff; Little's Law on referral-to-SOC; retention as an endogenous feedback loop), the
   permanent tensions it holds, and the failure modes it guards against.

> Guardrail carried throughout: the agent works in aggregates and operational signals. It uses
> minimum-necessary data, never surfaces PHI beyond what a task legitimately requires, and stays
> inside CoP, OASIS timing, and payer rules.
