# HCHB Web Scheduling — Executive Overview (One Page)

> **For:** steering committee / sponsors. **Re:** HCHB's browser-based Web Scheduling (Early Access).
> **From:** the capacity & scheduling initiative. **Full detail:** [operational spec sheet](./hchb-web-scheduling-operational-spec-sheet.md).

## The verdict
A **genuine, overdue upgrade to scheduling *execution*** — adopt it. But it lives almost entirely in the
**day-to-day scheduling** layer. It is the execution cockpit and the system of record; it is **not** a capacity-
planning, forecasting, economic, or engagement system. Treat it as the **spine we build around**, not the
strategy itself.

## What it is — and isn't
- **Is:** a browser app (SSO with Citrix) that lets schedulers work **by exception** — three live queues surface
  field returns, overall status, and Smart-Scheduling rejects — plus a **per-clinician weekly capacity %**
  (`(Scheduled + Completed) / Expected`, in Productivity Points).
- **Isn't:** forward-looking (fixed 8-day window, no forecast), SOC-aware, economic (no dollars/LUPA/agency
  cost), compliance-timed, or clinician-/patient-facing. It shows visits **after** they're schedulable — it
  can't see the intake→SOC readiness pipeline where the discovery says the real delays live.

## Fit-for-purpose (at a glance)
| Strong | Moderate | Absent |
|---|---|---|
| Schedule execution & exception triage | Capacity **measurement** (worker-week) | Capacity **planning / forecasting** |
| System of record / low integration burden | Workforce/flex **as a demand feed** | Readiness gauntlet (DCS/auth/POC/TIC) |
| Useful visit signals (continuity, hazardous-med, reminders) | Real-time visibility (gated by sync) | Economic layer · clinician & patient surfaces |

## Top benefits
1. Gets schedulers **out of Citrix** for triage — faster, browser-based, same login.
2. **Scheduling by exception** — surfaces only what needs a human; retires two static reports.
3. A **native capacity metric** — the first standardized, in-product answer to "is this clinician full?"
4. The **Smart-Scheduling exceptions queue** — a live, reason-coded overflow worklist (our best flex-coverage hook).

## Top risks to manage
1. **Capacity is shallow & unweighted** — present-tense, worker-week, ignores travel/doc/acuity; it **overstates
   headroom** and can burn out your best clinicians if used naively. The **"Expected" denominator is undocumented.**
2. **Manual-sync latency** — field truth (declines, misses, completions) lags reality; capacity can read stale.
3. **The exception fix still round-trips to Citrix** — the loop isn't closed in the browser.
4. **Roadmap encroachment** — Early Access is expanding toward the capacity space we're building; needs a standing watch.

## Recommendation
**Adopt it as the execution surface and data spine.** Do **not** mistake it for a capacity system — stand up the
planning, readiness, economic, compliance, and engagement layers **around** it. **Highest-value first use:**
harness its exception queues + worker capacity % as the demand-signal + headroom engine for an **opt-in,
earnings-led overflow/per-diem coverage** capability — the cleanest, lowest-risk wedge.

## The one decision this needs from you
Approve a short **HCHB integration discovery** (7 questions, led by: *how is "Expected" set?* and *are the
exception queues available as a data feed?*) — the answers determine whether we can automate on top of it or
only work beside it. *(Fund the discovery, not a build, at this gate.)*

---
*One-page summary; evidence and domain-by-domain detail in the [operational spec sheet](./hchb-web-scheduling-operational-spec-sheet.md).*
