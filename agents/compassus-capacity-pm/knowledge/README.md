# Knowledge Base — Compassus Capacity & Scheduling

The empirical ground truth for the Home Health Expert PM agent. Sourced from Compassus's own discovery work
(July 2026), not generic home-health theory. The agent reasons **from these documents first.**

## Contents

| File | What it is |
|---|---|
| [`discovery-session.md`](./discovery-session.md) | The full-day cross-functional discovery session — what schedulers actually do, the end-to-end workflow chain, the tooling landscape, why Smart Scheduling failed, and the session's Next Steps. **The primary ground truth.** |
| [`capacity-scheduling-summary.md`](./capacity-scheduling-summary.md) | The consolidated capacity-vs-scheduling analysis — the two-function framing, the 10 connection points (CP-1…CP-10), four stakeholder perspectives, the failure catalog, and the 9 open questions that gate requirements. |
| [`staffing-model.md`](./staffing-model.md) | **The per-discipline, per-branch staffing model** — visit-equivalent point system, census→demand translation, dual visit/caseload ceiling, per-discipline turnover waterfall, maintain-vs-grow, per-diem sizing, demo norms, and decisions. **Directly answers open question #1** (defines the point-system currency) and operationalizes CP-3 (SOC-as-binding-constraint) and CP-5. Working tool lives in `worker-max/Aethergrid` under `docs/staffing-model/`. |

## Provenance

- **Google Drive folder:** `1WEf_6FN7963y-MGwP3S3GaaPvqJ2RNF3`
- Source docs (owned by `worker@workforcewave.com`):
  - `HH Scheduling Discovery Session` — `1bQSDWjsymyI6hTQI0-MoYyi4PHZAOc-aDyJu_xe1a8Y`
  - `HH_Capacity_Scheduling_Summary` — `1GrasIJb4-eKrBDRCoCZWALB8vbiC8qKiOaSiK2ZLnAc`
  - `Foundational Knowledge for Home Health Capacity and Scheduling` — `1hncjJ_RIRE9TjveBAQMg5gwgT5UsAx3boISGhLTH0Wc` (earlier/lighter draft + the raw four-perspective chat log; superseded by the summary above)
- **Related, separate initiative:** `Compassus-Intake-Claude-Brief.pdf` — `1RGz-_uLLbkoDPDqSpjiArS6xDn0L5ZXo`. Options/compliance brief for AI-triaging inbound referral/intake email within HIPAA/BAA limits (redact-first → land in a BAA-covered surface). Relevant because intake is the upstream feed into capacity, but it is the referral-intake initiative, not this one.

> These are internal Compassus operational documents. Work in aggregates and operational signals; they contain
> no raw PHI and none should be introduced here.

## Distilled findings that shape the agent

The ten load-bearing facts the agent must reason from:

1. **The scheduling problem is not a scheduling problem.** Schedulers are administrators; their only true scheduling decision is the SOC intake call. Real inefficiency is upstream — clinical documentation, DCS workflow, auth holds, and (above all) capacity management. Scheduling gets blamed because it's the last visible touchpoint.
2. **Capacity must be solved before scheduling.** They are two distinct functions forced through one manual spreadsheet. Running scheduling optimization without a capacity foundation is exactly why the Alabama Smart Scheduling pilot failed.
3. **SOC-capable clinician availability is the binding constraint on growth** (CP-3), distinct from routine visit capacity. The overload cycle locks a branch at its volume indefinitely.
4. **The point system is the undefined shared currency** of both capacity and scheduling (CP-5). It must be defined before most requirements can be written — it's open question #1.
5. **The failure that repeats is the intake→scheduling handoff** (CP-8) — the most-cited communication breakdown.
6. **Change management, not technology, is the real risk.** Alabama's Smart Scheduling was never truly piloted because leadership let clinicians reject optimization. Clinician buy-in requires the "personal assistant, not control mechanism" framing — and, on pay-per-visit models, an earnings story.
7. **Cleanest pilot = a new-integration or brand-new branch**, ideally a pay-per-visit office (Providence, Ohio Health, BSMH) where existing habits won't fight the tool. Tenured clinicians are the hardest to change.
8. **The system landscape is fragmented and mostly not real-time:** HCHB (core, manual sync), Commure (new intake/referral), NestMed (real-time docs), Pulse (utilization), Workday (PTO — HCHB integration exists but is OFF), external coding vendor, Circadia (AI welcome calls).
9. **Hard operational constraints are real:** once a clinician accepts a visit, the back office cannot pull it (same-day changes are phone-only); Medicare compliance windows (48-hour MD notification on missed visits, 30-day reassessments, 14-day HHA supervisory, TIC clock from referral); the physical in-home calendar is a CoP requirement.
10. **Every stakeholder measures a different thing:** the ED measures growth/margin, the RN measures workload/burnout, the scheduler measures execution speed, the patient measures reliability and continuity. The agent must translate across all four — and the patient's line is the north star: *"schedule your clinicians around us, not just around branch metrics and tools."*

## Benchmarks worth remembering

- **~40–50 patients** per full-time RN+LPN team pair
- **30 points/week** productivity minimum (points otherwise undefined)
- **50–60** daily auth notifications per scheduler, mostly non-actionable
- **7+** scheduler tasks generated per 3-discipline (Nursing/PT/OT) admission
