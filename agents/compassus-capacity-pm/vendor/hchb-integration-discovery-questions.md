# HCHB Integration — Discovery Questions for the Overflow/Coverage Wedge

> **Purpose.** Answer the blocking dependencies in the [prototype spec](./overflow-coverage-prototype-spec.md)
> §12 before any build. These are the questions to put to **HCHB (vendor / account team)** and the **Compassus
> HCHB administrator**. The single most important one — *can we get the exception queues as a feed?* — decides
> whether v1 is an automated board or a semi-manual one.
>
> **How to use.** Split into the two audiences. Mark each answer **Y / N / partial**, capture the source
> (screen / report / API / table), and note freshness. Rows that come back N/partial are the build backlog.

---

## A. The demand feed — the two exception queues *(BLOCKING — everything hinges here)*

Ask HCHB first; the Compassus admin can confirm what's enabled.

1. **Is there an API or scheduled export** for the **Scheduling Status Alerts** queue (Rescheduled / Reassigned
   / Declined / Missed-by-Clinician) and the **Smart Scheduling Exceptions** queue ("Worker at Max Hours")? Or
   is the browser UI the only access?
2. **What fields come with each queue row** — `visitId`, patient zone/zip, discipline, service code + type,
   payor, **auth status**, visit date/time-window, and the **exception reason code**?
3. **At what cadence** does the feed refresh, and **what's the latency** relative to a clinician's PointCare
   sync? (We need to know how stale a "needs coverage" row can be.)
4. **Is the Smart Scheduling Exceptions queue available if Smart Scheduling is *not* enabled** at the pilot
   branch — or is enabling Smart Scheduling a prerequisite for that half of the feed?
5. **Can we filter the feed to one branch / team** server-side, or must we pull all and filter locally?
6. **De-dupe key:** if a visit is both a field-return *and* an SS exception, does it appear once or twice, and
   what's the stable identifier to collapse on?

## B. The write-back path — closing the loop

7. **Is there an API to assign a clinician to a visit** (post the claim back to HCHB), or does assignment for
   these exception visits **still have to happen in the Citrix app** (as the user guide implies)?
8. If write-back exists, **what does it require** (auth scope, worker ID, visit ID, effective-dating) and **are
   there guardrails** it enforces (scope, max-hours, auth) that we'd be duplicating or must respect?
9. If write-back does **not** exist, what's the **lowest-friction manual step** — can the coordinator confirm a
   claim in Web Scheduling, or only in Citrix? (Determines the "one-tap task" fallback in spec §5.)

## C. The supply record — worker fields we need

10. **Does the worker record expose `employmentType` / PRN status** and **pay model** (per-visit / salaried /
    hybrid)? These are the population switch and the earnings number — if HCHB doesn't hold them, our registry
    must (spec §3.2).
11. **Is the worker capacity %** — `(Scheduled + Completed) / Expected` — **available as data** (not just on
    the calendar screen), and is the **"Expected" target** readable per clinician?
12. **How is "Expected" configured** — a flat branch default, or tuned by discipline / market / role? (Sets
    whether the FT-extra headroom gate is trustworthy — STRAT L1.4.)
13. **Are Productivity-Point values** (per visit type × discipline) **exposed**, so we can reconcile them to our
    WVP table (SOC 2.5 / recert 1.75 / eval 1.5 / reassess 1.25 / dc 1.75 / routine 1.0)?
14. **Continuity %** — is the Smart-Scheduling continuity score readable as data, and does it carry a definition
    we can consume rather than recompute?
15. **Restrictions / competencies** ("No SOC", "No wound care", licenses, specialties) — where do these live and
    can we read them to enforce scope as a **hard rail** (the ECO-flagged correctness gap)?

## D. Identity, auth & environment

16. **Identity join:** what's the canonical clinician key across HCHB ↔ Workday (WD-ID ↔ HCHB-ID), and is there
    a resolution service or must we map it?
17. **Auth model for our integration:** service account? OAuth? What scopes, and who provisions them?
18. **Is there a non-production / sandbox HCHB instance** we can build and test against without touching live
    scheduling?
19. **Rate limits / volume constraints** on any API we'd poll.

## E. Compliance & data posture

20. **BAA coverage:** confirm the surface and fields we'd ingest are within an existing BAA; identify the
    **minimum-necessary** patient fields (we want zone/zip + date, **not** address/name/MRN beyond the join key)
    — CLAUDE.md HIPAA rules, IDX §6.
21. **PHI on the clinician board:** what may lawfully appear to a claiming clinician *before* they're assigned
    the patient? (Drives how much a card can show pre-claim.)
22. **Audit:** does HCHB log the assignment source, so a board-driven assignment is traceable for compliance?

## F. Roadmap (so we build in the seams, not against them)

23. **Is HCHB planning a clinician-facing open-shift / coverage-claim capability** natively? (If yes, our wedge
    may become a thin front-end or a stopgap — worth knowing before we build.)
24. **What's the Web Scheduling Early-Access roadmap** for: editable date range, write-back of exceptions
    (removing the Citrix round-trip), and any capacity/forecasting additions? (Vendor-encroachment watch —
    [fit analysis](./hchb-web-scheduling-analysis.md) §3.5.)

---

## Answer log (fill during discovery)

| # | Question (short) | Audience | Y/N/partial | Source (screen/report/API/table) | Freshness | Owner | Notes |
|---|---|---|---|---|---|---|---|
| A1 | Queue feed exists? | HCHB | | | | | **Blocking** |
| A2 | Queue fields | HCHB | | | | | |
| A3 | Feed cadence/latency | HCHB | | | | | |
| B7 | Assignment write-back API | HCHB | | | | | Decides one-tap fallback |
| C10 | PRN + pay model on worker | HCHB/admin | | | | | |
| C11 | Capacity % as data | HCHB/admin | | | | | |
| C12 | How "Expected" is set | admin | | | | | Gates FT-extra |
| C13 | Productivity-Point values | HCHB | | | | | Reconcile to WVP |
| D18 | Sandbox instance | HCHB | | | | | |
| E20 | BAA / min-necessary | Compassus | | | | | Pre-build |
| F23 | Native open-shift on roadmap? | HCHB | | | | | Strategy input |

*(Extend the log with the remaining rows as you work them; the shortlist above is the critical path.)*

---

*Companion to the overflow/coverage prototype spec and pilot charter. Answers here retire the spec's Open
Questions and set whether v1 is an automated feed or a semi-manual board.*
