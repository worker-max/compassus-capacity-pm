# Knowledge Base — Compassus Capacity & Scheduling

The empirical ground truth for the Home Health Expert PM agent. Sourced from Compassus's own discovery work
(July 2026), not generic home-health theory. The agent reasons **from these documents first.**

## Contents

| File | What it is |
|---|---|
| [`discovery-session.md`](./discovery-session.md) | The full-day cross-functional discovery session — what schedulers actually do, the end-to-end workflow chain, the tooling landscape, why Smart Scheduling failed, and the session's Next Steps. **The primary ground truth.** |
| [`process-facts-2026-08.md`](./process-facts-2026-08.md) | **The distilled current-state process facts from the 17–18 Aug flow-mapping sessions** — admission, plan of care, auth's two interfaces, the clinician's own week, the five dispositions, missed-visit chain, capacity levers, recert & discharge, and the binding drawing conventions. Every flow sheet in `../artifacts/` draws from this file. |
| [`whiteboard-session-2026-08-13.md`](./whiteboard-session-2026-08-13.md) | The 13 Aug on-site whiteboard session — decisions DE-01…DE-10, the named bottlenecks, and the adoption constraints. |
| [`capacity-scheduling-summary.md`](./capacity-scheduling-summary.md) | The consolidated capacity-vs-scheduling analysis — the two-function framing, the 10 connection points (CP-1…CP-10), four stakeholder perspectives, the failure catalog, and the 9 open questions that gate requirements. |
| [`constraint-register.md`](./constraint-register.md) | **CN-01…CN-51 — what blocks scheduling today, classified by whether we can change it.** Regulatory · payer · HCHB-configurable · HCHB product limit · Compassus policy · cultural · labor agreement. **The nine product limits are the case for the initiative.** |
| [`bottleneck-dossiers.md`](./bottleneck-dossiers.md) | The twelve bottlenecks ranked by leverage, each with mechanism, evidence, downstream effects, what to measure, candidate remedies, and open questions. **The first four are the ones worth solving first.** |
| [`payer-and-episode-economics.md`](./payer-and-episode-economics.md) | **How payment works and what it constrains** — PDGM 30-day payment periods, 432 case-mix groups, the LUPA floor, the over-utilisation ceiling, the three payer classes, and the payer-rules-library schema with its three unverified seed entries. |
| [`business-case-and-kpis.md`](./business-case-and-kpis.md) | The modelled finance case ($7.9M/yr moderate, ~80 branches), its drivers, the primary/secondary KPI set with today's availability, and the vendor-fit read including the **posture-overreach** signal. |
| [`workbook-2026-08-13.md`](./workbook-2026-08-13.md) | Read-only index to the authoritative workbook — the fourteen tabs, the scoring semantics, and all 76 numbered + 3 unnumbered variables. |
| [`DRIVE-INDEX.md`](./DRIVE-INDEX.md) | **Every file in the Drive working folder and where it lives here.** Start here when asking "do we have that document?" |
| [`source/`](./source/) | Verbatim source records — the line-numbered 13 Aug transcript (resolves every `[T:###]` citation), the whiteboard exec summary + Part A, the 17 Aug flow clarifying document, and a dated CSV snapshot of all fourteen workbook tabs. |

## Provenance

- **Initiative working folder (fully ingested 18 Aug 2026):** `1RPI1ogTdyDeEf64OBRmaRQ0ESNWp5k5o` —
  twenty files, mapped one by one in [`DRIVE-INDEX.md`](./DRIVE-INDEX.md).
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

## What the August documents added

The ten above still hold. Five things the 13–18 August material made concrete, each of which changes
what gets built:

11. **Fifty-one constraints, and only nine are the real argument.** Sorting what HCHB imposes from what
    regulation requires is the initiative's organizing discipline. **CN-22…CN-30 cannot be toggled** —
    they are the case for building. Four of the loudest pain points (**CN-18, CN-31, CN-32, CN-33**) are
    Compassus's own and need no new system; run them on a separate, faster track.
12. **Payment is per 30-day period, not per certification period and not per visit.** Two payment
    periods sit inside one 60-day cert period, each with its own case-mix group, payment amount and LUPA
    threshold. **A model that only knows the cert period cannot see the cliff it is walking toward.**
13. **There is a ceiling as well as a floor.** Above the LUPA threshold, every further visit under
    episodic payment is cost with no revenue. The target is *the clinically right number, above the
    floor and no higher than the period supports* — shown to the clinician, **never** weighed against
    clinical need in an objective function.
14. **The fastest win needs no new data.** The auth team already writes payer rules into a coordination
    note at verification. **Surfacing them at plan-of-care creation is a schema and a surfacing point,
    not a data-gathering programme** — and it is a patient-care win, because abrupt discharges happen
    when nobody planned against the real visit budget.
15. **A higher vendor score can be a worse fit.** HCHB Smart Scheduling rates highest **and** overreaches
    our stated automation posture on 16 variables. That is the Alabama failure expressed as a number.

## Benchmarks worth remembering

- **~40–50 patients** per full-time RN+LPN team pair
- **30 points/week** productivity minimum (points otherwise undefined); FTE status maps to point
  expectation in the HCHB worker profile — **0.5 / 0.6 / 0.7 / 0.8 → 30 / 28 / 26 / 20 / 12 points**
- **50–60** daily auth notifications per scheduler, mostly non-actionable
- **7+** scheduler tasks generated per 3-discipline (Nursing/PT/OT) admission — **8** once approval
  workflow fires per discipline as well
- **432** PDGM case-mix groups; **LUPA thresholds run 2–6 visits**, group-specific, recalibrated annually
  (eighteen groups moved by one visit for CY 2026)
- **Pending-auth allowances of 1, 3, 5 or 10** visits, set by the payer, not by clinical need
- **CY 2026 rate pressure:** a permanent **−1.023%** behaviour-change adjustment plus a one-year **−3.0%**
- **~3,000 clinicians × ~30 minutes/day** of unpaid evening confirmation calls — *both figures are
  session estimates and need a survey before they carry a business case*
- **$7.9M/yr** modelled network impact, moderate scenario, ~80 branches ($4.0M conservative / $14.3M
  hopeful); **MVP captures 60%** of it
