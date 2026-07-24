# SME Perspective — Senior Scheduler / Staffing Coordinator

> Seeded v0 perspective (AI-generated from the scheduler / staffing-coordinator lens, grounded in the operator's
> strategy download). **To be validated with a real senior scheduler.** Preserved verbatim per the
> [SME discovery framework](../sme-discovery-framework.md).

# Day-to-Day Capacity Execution Tactics — Scheduler / Staffing-Coordinator Lens

These are the moves a great scheduler actually makes between 7:00 AM chaos and the 4:30 PM "did everything get covered" check. Each is written to be built into the 9-tab tool and to train an AI agent operating the capacity cockpit.

---

## 1. The Standing Per-Diem "Warm List" (engagement before you need them)

**Tactic.** The great scheduler never cold-calls a per-diem in a crisis. They maintain a live, ranked warm list and touch every active per-diem on a cadence — a low-stakes "you around Thursday/Friday this week?" text sent Monday — *before* there's a specific visit to fill. Per-diems who get contacted only when desperate quietly disengage.

**Trigger/context.** Every Monday AM, and any time a per-diem's last-worked date crosses a staleness threshold.

**Why it works.** Per-diem labor is an attention market. The clinician who feels remembered keeps their week loosely open for you. Silence reads as "they don't need me." Disengagement is almost always preceded by a gap in contact, not a bad visit.

**Encode as system logic.**
- Track per per-diem: `last_worked_date`, `last_contacted_date`, `avg_visits_per_week_trailing_4wk`, `accept_rate_trailing_20_asks`, `stated_availability_window`.
- **Disengagement flag:** fire when `days_since_last_worked > (2 × personal_median_gap)` OR `days_since_last_contacted > 7` OR `accept_rate dropping ≥30% vs. own baseline`.
- Weekly "warm-touch due" queue = all active per-diems with `last_contacted_date > 5 business days`.

**Train the AI agent.** Draft the Monday availability-check outreach per per-diem, personalized with their recent pattern. Propose; do **not** auto-send a booking. Guardrail: outreach is a *question about availability*, never a committed assignment. Escalate disengagement-flagged per-diems with a one-line "haven't worked in 18 days, median gap is 6 — recommend a personal call, not a text."

---

## 2. Forecast-the-Gap, Publish-the-Need (make the need visible early)

**Tactic.** The scheduler projects next week's discipline-level gap from current census + known referral pace + PTO calendar, and *publishes the need* to the per-diem pool 5–7 days out — "we're going to be short 2 RN SOC slots Wed/Thu in the north territory."

**Why it works.** The coordination burden a tool removes is exactly this: turning a diffuse anxiety into a specific, claimable, published slot. It converts the ask from "please rescue me" (low yield) to "here's paid work if you want it" (high yield).

**Encode as system logic.**
- Gap forecast per day per discipline = `projected_demand (scheduled + expected referrals from trailing pace + recert/SOC pipeline) − projected_supply (FT capacity − PTO − on-call recovery − territory load)`.
- Any day where `projected_gap ≥ 1` in a discipline surfaces a **publishable slot** with date, discipline, territory cluster, visit type.
- Per-diem-facing view: "open slots this/next week."

**Train the AI agent.** Run the forecast nightly, generate the ranked list of publishable slots, match each to the 3 best-fit per-diems. Draft the "here's what's open" broadcast. Guardrail: forecast and propose; a human confirms the published gap before broadcast (prevents over-publishing a slot a FT clinician can absorb). Never double-promise one slot to two per-diems.

---

## 3. Territory-First Assignment (cluster before you optimize anything else)

**Tactic.** When placing any visit, assign to the clinician whose *resting posture already sits in that cluster* before considering anyone else. Protect the geographic spine of each clinician's day — a new visit slots into an existing loop, not a 40-minute detour. Windshield time is the silent capacity killer.

**Encode as system logic.**
- Each clinician carries a `home_territory` + `resting_posture`.
- Assignment scoring: `proximity_score` = distance from new visit to clinician's *nearest already-scheduled visit that day* (not to home base — to their actual route).
- Directive engine ranks: in-cluster clinician with capacity > in-cluster near cap > adjacent-territory > cross-territory (flagged, requires reason).
- Hard flag when an assignment adds `> X min` incremental drive to a clinician's existing route.

**Train the AI agent.** Propose assignments ranked by route-incremental drive time, not straight-line distance from home. Show the top 2–3 with "adds 8 min to Maria's existing Tuesday loop" vs. "adds 35 min, crosses into east territory." Guardrail: never silently cross a territory boundary; surface it with the reason and the drive-time cost.

---

## 4. The Last-Minute Referral Decision Tree (who to ask, in what order)

**Tactic.** When a same-day/next-day referral lands, run a fixed order of operations: (1) FT clinician **already in that cluster** with headroom; (2) assessing clinician who can **offload** a routine visit to an assistant to free the slot; (3) SOC-dedicated nurse/PT whose bookable slot fits; (4) per-diem in the warm list for that territory; (5) escalate to branch leadership. Honor the SOC rule at every step — RN takes the SOC if nursing is on the case; PT only when nursing is NOT on the referral.

**Why it works.** A repeatable tree removes emotional bias and protects the highest-leverage capacity. Asking the in-cluster FT first is cheapest. Offloading routine to assistants frees skilled slots. Going to per-diem before exhausting cheaper internal capacity burns your scarce resource.

**Encode as system logic.**
- Matching + directive engine executes the tree in order, filtered by discipline eligibility.
- **SOC gate:** `if nursing_on_case → require RN for SOC; elif no_nursing → PT eligible`. Hard rule.
- Assessing→assistant offload: engine detects when a candidate is at cap but holds ≥1 assistant-eligible routine visit that day, and proposes the swap.

**Train the AI agent.** Walk the tree top-down and return the *first viable* placement plus next-best fallback, showing why each earlier tier was skipped. Guardrails: SOC rule is inviolable; propose offloads and per-diem asks but do not commit them; if it reaches "escalate," hand to a human with the full trail, never auto-decline a referral.

---

## 5. Protect-the-Clinician Sequencing (how the ask lands without breaking them)

**Tactic.** Before adding the last-minute visit, check what you're about to do *to the person*, not just the schedule. Won't drop a 6th visit on the clinician who did on-call last night. When they must ask a stretched clinician, they lead with the protection ("I'll pull your Friday routine to make room") so the ask is a trade, not a pile-on.

**Encode as system logic.**
- Per clinician daily: `visit_load vs. sustainable_cap`, `on_call_last_night` flag → mandatory recovery buffer, `consecutive_high_days` counter.
- **Fatigue/over-ask guard:** block or hard-flag assignment when `load ≥ cap`, `on_call_recovery = true`, or `asks_this_week > threshold`.
- Track `ask_count` and `yes_count` per clinician (over-relied-upon flag).

**Train the AI agent.** Surface the human cost inline: "Dev is the closest fit but did on-call last night — recommend protecting; next best is Priya, +10 min." When an ask to a stretched clinician is unavoidable, draft it *with the trade included*. Guardrail: never frame a naked pile-on; pair a stretch-ask with an offload or acknowledgment, and flag chronically over-asked clinicians to leadership.

---

## 6. You Can't Un-Ring the Bell: Read Real Availability (accepted ≠ pullable)

**Tactic.** Track the *true* state of every clinician's day: **once a visit is accepted and communicated to the patient, you can't quietly pull it back** to reassign the clinician elsewhere. Distinguish "has open time" from "is actually available" (PTO booked, on-call recovery owed, patient-willingness windows).

**Encode as system logic.**
- Visit states: `proposed → accepted → patient_confirmed → completed`. **`patient_confirmed` is locked** — engine cannot reassign it to free the clinician; only released via explicit human action with a reason.
- Availability = `calendar_open − PTO − on_call_recovery_owed − stated_unavailable_windows − patient_willingness_constraints`. Never equal to raw white space.
- On-call recovery generates an automatic non-availability block the morning after.

**Train the AI agent.** Compute *true* availability, never raw open time, and treat `patient_confirmed` visits as immovable. Guardrail: any reshuffle touching a confirmed visit requires explicit human release; flag the patient-commitment cost. State the availability number's basis ("Maria has 2 open blocks but 1 is on-call recovery — 1 truly available").

---

## 7. Fast Backfill on Cancellation/Discharge (recover the freed slot before it evaporates)

**Tactic.** When a visit cancels or a patient discharges, treat the freed slot as a *perishable asset* and immediately match it against waiting demand — the SOC pipeline, a recert due, a per-diem who wanted hours — ideally to the clinician *already going to be in that area*.

**Encode as system logic.**
- Discharge/cancellation → backfill matcher (matching engine run in reverse): freed slot's `time + territory_cluster + freed_clinician` becomes the key.
- Rank waiting demand by `same_cluster_fit > SOC/recert_due_urgency > per_diem_wanting_hours`.
- Time-decay urgency: backfill priority escalates the longer a same-day slot sits unfilled.

**Train the AI agent.** On any cancellation event, instantly propose the best backfill — prioritizing the freed clinician's own cluster so their route stays intact — within the decay window. Guardrail: propose, human confirms (especially anything requiring a patient/clinician contact); never silently rebook a clinician who may have already left the area without confirming availability.

---

## 8. The Right Ask, Framed Right, Timed Right (and knowing when NOT to ask)

**Tactic.** Pick *which* clinician to ask by yield, not proximity to your inbox — accept-rate history, current load, relationship state — then frame for a yes (specific, bounded, with the trade or the "why you") and time it for when they can actually say yes. Know when **not** to ask: not the on-call-recovery clinician, not the person asked twice yesterday, don't broadcast-blast a slot a targeted ask would fill cleaner.

**Encode as system logic.**
- Per clinician: `accept_rate`, `preferred_visit_types`, `preferred_days/times`, `recent_ask_count`, `relationship_state`.
- **Ask-yield score** = `accept_rate × fit × availability_true × (1 − recent_ask_fatigue)`.
- **Do-not-ask filter:** exclude on-call recovery, at-cap, already-asked-N-times-this-window, stated-unavailable.
- Prefer *targeted single ask* to top-scorer over broadcast when one candidate's yield exceeds a confidence threshold.

**Train the AI agent.** Rank candidates by ask-yield, draft the ask with specifics baked in (exact time, drive-from-last-visit, end-of-day, the trade), pick send timing against the person's response pattern. Guardrails: enforce the do-not-ask filter absolutely; cap asks per clinician per window; prefer a targeted ask; never double-commit a slot while an ask is outstanding.

---

## 9. Balanced-Model Watchdog at the Discipline Level (spot the bottleneck before it bites)

**Tactic.** Watch the *ratio* of work to skill level, not just headcount. Notice when RNs are eating routine visits an LPN should carry, or SOC demand is outrunning the SOC-dedicated slots, and escalate it as a staffing-model signal — a *pattern* problem, so leadership can fix the mix.

**Encode as system logic.**
- Track `skill_level_utilization`: % of RN time on RN-only work vs. LPN-eligible; `SOC_demand vs. SOC_dedicated_capacity`; discipline-level `overload_index`.
- Signal fires when RNs perform `> X%` sub-skill visits over a trailing window, or SOC demand exceeds dedicated slots N days running.
- Feed the signal to the capacity strategy layer, tagged "staffing-model," distinct from day-to-day alerts.

**Train the AI agent.** Monitor utilization ratios and raise a *strategic* flag ("RNs covered 14 LPN-appropriate visits this week — recurring, recommend LPN capacity review") separate from daily assignment noise. Guardrail: classify as a model-level insight for leadership, not something to solve by reshuffling; never mask a structural shortage by silently overloading RNs.

---

## 10. Per-Diem Retention Ledger (protect the relationship, not just the booking)

**Tactic.** Run a systematic ledger on each per-diem — did we give them the hours we implied? did we cancel last-minute and cost them a paid day? are we spreading work fairly? — and actively repair debts. Per-diems leave over *fairness and reliability*, rarely over one bad visit.

**Encode as system logic.**
- Per per-diem: `hours_promised_vs_delivered`, `agency_cancellations_on_them` (count + recency), `share_of_pool_hours`, `days_since_last_offered_work`.
- **Debt flag:** agency-canceled a booked per-diem → mark "owed," prioritize for the next fitting slot.
- **Fairness flag:** pool-hour distribution skew beyond threshold → surface under-utilized willing per-diems.

**Train the AI agent.** Maintain the ledger and, when a fitting slot opens, give owed/under-utilized per-diems a ranking boost so repair and fairness happen automatically. Guardrail: fit and SOC/discipline rules still gate — boost an owed per-diem *among eligible* candidates, never book an unqualified one to settle a debt. Flag when the pool is concentrating on a few names.

---

## 11. Morning Blast-Radius Check (triage the day before it triages you)

**Tactic.** First thing, scan for the day's *fragility points* — every visit that depends on a single clinician with no backup, every SOC with a hard time window, every per-diem still unconfirmed — and pre-solve the top 2–3 before the phone rings.

**Encode as system logic.**
- Daily **fragility scan:** flag visits with `no_backup_candidate_in_cluster`, `hard_time_window`, `unconfirmed_per_diem`, `single_clinician_dependency`.
- Compute a per-day `capacity_slack` score; low slack + high fragility = priority pre-solve list.
- Surface top N fragility points ranked by blast radius.

**Train the AI agent.** Run the fragility scan at start of day and hand the human a ranked "here are today's 3 weak points and a pre-lined backup for each." Guardrail: pre-identify and pre-draft fallbacks but do not pre-book them (that wastes capacity on failures that don't happen); hold the backup ready to fire the instant the trigger occurs.

---

### Cross-cutting agent guardrails (apply to all tactics)
- **Propose, don't commit:** the agent drafts asks, ranks placements, and pre-lines backups; a human (or an explicit per-diem accept flow) closes anything involving a person's time or a patient commitment.
- **SOC rule and `patient_confirmed` locks are inviolable** — never overridden to optimize.
- **No double-booking / no double-asking** one slot while an ask is outstanding.
- **Show the cost, not just the pick:** every recommendation carries the drive-time, fatigue, or relationship cost that justifies it.
- **Separate strategic signals from daily noise:** model-level imbalances route to leadership, not into the day's reshuffle logic.
