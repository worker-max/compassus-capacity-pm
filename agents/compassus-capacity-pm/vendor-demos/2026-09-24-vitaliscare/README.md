# VitalisCare Sync — vendor demo, 24 Sep 2026

Round-two demo against the [Vendor Demo Question Guide](https://drive.google.com/file/d/1-cvjVv3FA4BctCCAfgI2blnzo0367SLk/view). Teams recording, 2:00:32.
Scorecard going in: **67 · Consider · no open stop-checks.**

| File | What it is |
|---|---|
| `VitalisCare-Sync-Demo-Readout.pdf` | 19-page landscape PDF of the report for sharing (no author metadata) |
| `VitalisCare-Home-Health-Gaps-One-Pager.pdf` | One page: every change Sync needs for home health across capacity, scheduling and engagement, sized build / customize / roadmap / as-is, plus the risks of a hospice vendor learning home health. Source: `home-health-gap-one-pager.html` |
| `index.html` | Visual report: process flow with screens, question-by-question scoring, considerations, next steps |
| `transcript.md` | Full machine transcript, timestamped (no speaker labels) |
| `screens/HHMMSS.jpg` | 52 de-duplicated product and deck screens, named by time into the recording |

## Bottom line

**Hold at Consider. Don't advance on the product; advance on the partnership.** Sync is a real, live hospice scheduling engine with HCHB integration and a scheduler-decides philosophy that fits our Assist boundary. For home health, almost everything is still to be built: authorization and readiness, episode and LUPA, therapy disciplines, patient engagement and a territory view. Advance to the Oct 19 on-site only if the second call produces dates, scope and design-partner terms for that build, plus a plan for HCHB data cadence.

1. **Hospice product, and they said so.** "Our Sync tool has been developed primarily for hospice" (0:23:57). The demo used hospice disciplines, hospice F2F and RN-supervisory alerts, and hospice CMS benchmarks.
2. **Their own home health gap list is authorization and patient communication** (1:21:32). Compassus added LUPA and episode management, therapy productivity, territories and two-way patient scheduling. Vitalis's answer to each: "decision-tree logic," "weeks, not months."
3. **HCHB freshness is the binding constraint, and it's ours.** Their typical client ships HCHB logs about every 10 minutes; Compassus is at about 3 hours, which they called too stale for call-off recovery (0:47:27). Write-back is RPA, seconds to minutes.
4. **Advise, don't decide.** Every suggestion is accept or dismiss. Overrides need a reason, which feeds the model and gives an audit trail (0:59:04).
5. **Exceptions aren't shipped.** The Call-Off Center is "in design, slated for release before the end of the year" (1:04:48). Their capacity slide marks Exceptions "Live"; their roadmap slide says ranking and escalation are in development.
6. **The clinician app is a GPS tracking app.** Sync360 runs the workday, reroutes live and feeds route-adherence and mileage-discrepancy reviews (1:13:48, 1:44:36).

## Process flow as demoed

| # | Stage | Status | Essentials | Time |
|---|---|---|---|---|
| 0 | Configure | Live | Patient preferences (free text, web and app). Provider hours, PTO and long-term eligibility. Per-branch distance bands, daily visit quotas per discipline, RN/LPN substitution for SN orders, matching scope, new-worker ramp (default 2 weeks), FT/PT hours | 0:17:51 |
| 1 | Admit and authorize | Outside Sync | Sync starts after admission and auth. Intake plots visits in HCHB. Michael proposed feeding the Compassus intake platform into Sync and using capacity in accept/decline; Vitalis "can entertain" it | 0:27:55 |
| 2 | Who: Care Provider Matches | Live | Top 4 per discipline; Best Mapping (geography) or Smart Choice (geography plus capacity); caseload-fit map with service span; compatibility chips; AI rationale; override needs a reason; submit leads to pending, then RPA write-back | 0:32:52 |
| 3 | Write back / HCHB data | Live | Read: log ship, subset of fewer than 100 tables every ~10 min (large clients run the subset script themselves; one uses a DB mirror). Write: RPA. HCHB partnership talks for 2027 | 0:44:30 |
| 4 | When: schedule optimization | Live | Per-visit day-of-week suggestions with reasons and a map; accept once or recurring; drag-and-drop with flags (auth window, license, duplicates); cert alerts; original HCHB view; PTO; export; Notification Center (hospice F2F and RN gaps); Schedule Full monthly reshuffle. Vitalis prefers small incremental shifts | 0:54:36 |
| 5 | Exceptions: Call-Off Center | In design, EOY | Urgency-ranked queue from PTO, HCHB and PointCare declines; reschedule vs replace with trade-offs; continuity across multi-day outages; bypasses the log-ship lag if call-offs originate in Sync | 1:04:48 |
| 6 | Day of: clinician mobile (Sync360) | Live | Start, pause and end workday (GPS); routed list to Google Maps or Waze; live reroute; calendar; preferences; change notifications; own hours; PTO via HR integration (iSolved live, Workday to explore) | 1:13:48 |
| 7 | Oversee | Partly live | Live Map (day-of location, closest provider, tracking gaps); performance (visits/day, start time, device-off flags, reported vs tracked mileage, route adherence); SSVI Predictor (designed, hospice CMS benchmarks) | 1:36:30 |

## Question guide scoring

Answered 5 · partly 7 · not answered 3 · not asked 3.

| Q | Status | Evidence |
|---|---|---|
| C1 Referral decision | Not answered | No referral-vs-capacity check; branch roll-up is roadmap |
| C2 Episode, not visit | Not answered | No SOC, recert or LUPA logic; gap acknowledged when Compassus raised it (1:24:45) |
| C3 HCHB freshness | Answered | ~10 min typical; 3 h at Compassus is too stale; RPA seconds to minutes; no minimum committed |
| C4 Advise vs decide | Partly | Principle clear; no customer named who moved the line |
| C5 Clinician says no | Partly | App decline feeds a future Call-Off Center; override reasons learned; no clinician-facing rationale |
| C6 Tuesday goes wrong | Partly | Slides only; "nobody takes it" not addressed |
| C7 What you don't do | Partly | Volunteered auth and patient comms; no dates |
| C8 What breaks at our size | Partly | Largest 3,500 ADC; 3 orgs live (~6–7k patients) plus 1 beta; nothing on what broke |
| C9 One number | Not asked | |
| C10 Where you'll look worse | Not asked | Volunteered hospice-first anyway |
| V1 HH vs hospice | Answered | Primarily hospice; hospice demo data |
| V2 Therapy | Answered | Not modeled; productivity by HCHB points or visit count, prorated |
| V3 60-day episode | Not answered | Not attempted |
| V4 Patient comms | Answered | None; deprioritized in hospice (HIPAA, relationship); "within scope," no date or cost |
| V5 Not-ready visits | Answered | Only auth-window flags from HCHB data; readiness is not a state |
| V6 Points and roll-up dates | Partly | "Weeks, not months," no dates or funding |
| V7 Size and funding | Not asked | |
| V8 Product set | Partly | Sync (web), Sync360 (mobile + GPS), Account Portal, SSVI. Clinicians run Sync360 alongside PointCare |

## Considerations

- **High:** We would be the home health design partner. Most HH logic needs building; we specify it and our branches test it.
- **High:** HCHB cadence (3 h) is ours to fix: faster ship, a subset script on our side, a DB mirror, data modernization, or their 2027 HCHB partnership.
- **High:** The Call-Off Center makes lagged data survivable and is not shipped.
- **Medium:** RPA write-back fragility when HCHB screens change was not asked.
- **Medium:** GPS tracking and route adherence need change management and HR/legal review for salaried, tenured clinicians.
- **Medium:** HCHB stays in the loop: intake plots visits there, and scheduler workflow tasks pile up until auto-clear ships ("next few weeks").
- **Medium:** Scale and durability: 3 live orgs; company size and funding not covered; we would likely be their largest client by a multiple.
- **Medium:** Architecture & Continuity was on their agenda and skipped. Uptime, SOC 2 and HIPAA posture are open.
- **In their favour:** advise-not-decide, reasons on overrides, incremental change, a candid and fast team.

## Compassus asks raised in the room

- Keep new clinicians off SOC visits during ramp (Colin, 0:25:36). Not built; offered.
- Territory-aware matching and a branch-director territory map that follows referral patterns (Colin, 0:36:43, 1:36:30). Not built; "wouldn't be hard."
- Show clinicians the reasoning behind assignments outside their usual area (Colin, 0:41:27). Not built; liked.
- Day-before patient confirmation off the clinician's plate; two-way texting first (Colin and Compassus leadership, 1:17:30–1:32:00). Not built.
- Authorization as a scheduling constraint, not auth automation (1:23:33).
- LUPA and episode over- and under-utilization flags (1:24:45).
- No work inside HCHB; one screen for schedulers and clinicians (1:12:31).

## Next steps

Agreed:
- Vitalis sends the deck PDF (45 slides, about a quarter shown).
- Compassus shares the recording.
- Compassus sends deep-dive topics.
- Second virtual call, week of Oct 5 (Vitalis mostly out until then).
- Compassus explores faster HCHB log shipping.
- On-site summit week of Oct 19; attendees to be decided.

Recommended for the second call:
- A home health episode walk on the shared scenario.
- Written HH build scope, dates and funding.
- Minimum HCHB cadence per feature.
- The RPA break-and-repair story.
- A live Tuesday call-off including "nobody takes it."
- Architecture & Continuity.
- Company size and funding.
- One measured result.
- Clinician rationale and day-before confirmation plan.

## Attendees

- **Compassus:** Michael Thompson (VP Operational Excellence), Evan Kramer (Innovation & Operational Excellence), Colin Highland (initiative lead, PT), Paige Huffman (Sr PM).
- **VitalisCare:**
  - Dina Yankelewitz (CEO)
  - Bob Willix (VP Commercial Growth, RN)
  - Chavi Bornstein (Head of Product)
  - Shira Rubinstein (PO, Sync)
  - Faigy Stroh (Director of Customer Success)
  - R. Feldman (Lead Architect)
  - Malka Hess (data engineering)
  - Shayna Fishman (Sync360)
  - Rachel Greenhut (security)
  - Esther (dev and tech ops)

_Speaker attribution is inferred from context; the machine transcript has no speaker labels._
