# Posture-overreach findings — the calibration set

Sixteen findings from the 8.13 `Functional Scorecard` (its own counter at C18 reads 16), recorded
against HCHB Web Scheduling and HCHB Smart Scheduling. They exist nowhere else in the project.
Carried forward 27 Aug as the calibration set for the vendor scorecard.

Each is a worked example of a product **deciding** something we said a human must decide. That is
a different failure from a missing feature, it scores well on any coverage grid, and no vendor
will volunteer it. Questions D1 and D2 are where it surfaces in the returned questionnaires.

Test against the **current** `Future state -- the tool's role` column, not the 8.13 posture below.
Four rows drifted; the current value is the decided one. See the note at the end.

| Variable | Our posture (8.13) | Product | Finding |
|---|---|---|---|
| `SH-06` Territory / service area | Assist | Smart Scheduling | Branch/Team/Location match and Super Branch are hard constraints the engine auto-enforces (Worker Home Branch must equal Patient Branch), deciding service-area coverage rather than proposing it per our Assist posture. |
| `C-03` Clinician territory assignment (zip) | Assist | Smart Scheduling | Uses worker home/alternate-start geolocation to auto-route and auto-assign by proximity, effectively deciding zip-level coverage past our Assist posture. |
| `C-09` Per-diem / flex capacity | Assist | Smart Scheduling | Per-Visit/Contract workers are auto-included in the optimization pool and assigned by the engine, deciding flex-capacity use rather than proposing it per our Assist posture. |
| `C-10` Specialty competency supply | Assist | Smart Scheduling | Skills and Qualifiers are hard matching constraints auto-enforced, so specialty-competency supply is decided rather than proposed per our Assist posture. |
| `S-04` Preferred working days | Assist | Smart Scheduling | Recurring Worker Availability sets the default weekly working days the engine enforces automatically, exceeding our Assist posture. |
| `S-10` Preferred end time / hard stop | Assist | Smart Scheduling | Max Hours/Day and the fixed daily constraint act as an auto-enforced hard stop on the workday, exceeding our Assist posture on end time (indirect: a capacity cap, not a clock end-time). |
| `S-11` Max consecutive visits / daily volume | Assist | Smart Scheduling | Visits-per-Day and Hours-per-Day parameters auto-cap daily volume; engine stops at whichever fills first, exceeding our Assist posture. |
| `S-13` Overtime / extra-visit willingness | Read | Smart Scheduling | Engine auto-applies overtime penalties/1.5x rates and 30% caps to de-incentivize overtime, acting on it rather than only surfacing willingness per our Read posture. |
| `S-16` Specialty competency match | Assist | Smart Scheduling | Skills/Qualifiers competency match is an auto-enforced hard constraint, deciding rather than proposing per our Assist posture. |
| `S-22` Continuity of care | Assist | Smart Scheduling | Continuity is a core optimization: the engine auto-assigns to maximize a weighted continuity score and can override manual assignments, exceeding our Assist posture. |
| `S-38` Missed / unworked visit rescheduling | Assist | Smart Scheduling | Visit Dispatching auto-reassigns declined/reassigned visits to the next-best worker and stage-completes, exceeding our Assist posture. |
| `S-42` Day-by-day balancing | Assist | Smart Scheduling | Engine distributes visits across the 7-day window and Frequency-based Plotting assigns days by branch workload, balancing days automatically past our Assist posture. |
| `CO-06` Availability confirmation before booking | Read | Smart Scheduling | Engine auto-validates clinician and patient availability as a hard gate before booking, acting rather than only surfacing per our Read posture. |
| `CO-07` Reschedule coordination | Read | Smart Scheduling | Visit Dispatching and Rapid Reschedule auto-reschedule/reassign visits, exceeding our Read posture on reschedule coordination. |
| `CO-08` Failed-visit / no-show follow-up & rebooking | Assist | Smart Scheduling | Declined/reassigned visits are auto-rebooked to the next-best clinician by Visit Dispatching, exceeding our Assist posture on failed-visit follow-up. |
| `CO-09` Call-out coverage coordination | Read | Smart Scheduling | Visit Dispatching auto-reassigns call-out/declined visits to the next-best clinician (Find Shifts also surfaces unfilled shifts); the engine acts on coverage rather than only surfacing per our Read posture. |

## Posture drift since 8.13 — four rows

| Variable | 8.13 | Now | Read |
|---|---|---|---|
| `C-09` Per-diem and float pool | Assist | Surface | Stricter. A vendor auto-including per-diem in the optimisation pool is now overreach |
| `C-10` Specialty competency supply | Assist | Surface | Stricter, same shape |
| `C-13` Referral volume | Read | Stays manual | Held out of scope; no longer testable |
| `CO-01` Day-before confirmation | Assist | **Automate** | Looser, and deliberate. The one-pager sent to vendors asks for the day-before round to be automated, so a product confirming without a person is doing what we asked. Under the 8.13 baseline this would have been flagged |
