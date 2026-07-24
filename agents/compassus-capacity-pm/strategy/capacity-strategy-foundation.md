# Capacity Strategy Foundation — the Battle-Plan Logic

> **Purpose.** The strategic spine beneath the capacity tool: *what actually controls home-health branch
> capacity, in what order, and how each layer becomes tool logic and AI-agent behavior.* Grounded in the
> operator's SME download (Colin Highland, Jul 2026) and the Compassus discovery ([`../knowledge/`](../knowledge/)).
> This is v0 — the frame the SME discovery ([`../sme/sme-discovery-framework.md`](../sme/sme-discovery-framework.md))
> fills in and corrects.
>
> **Core principle.** Capacity is not one number to optimize; it is a *stack of controllable layers*, each of
> which caps the ones above it. You cannot day-to-day-schedule your way out of a broken staffing model, and you
> cannot staff your way out of a broken culture. Fix the stack bottom-up; manage it top-down.

## The capacity stack (the hierarchy of effectors)

```
                       ┌─ referrals must already exist ─┐   (precondition, not the capacity problem)
                       ▼                                 │
  ┌───────────────────────────────────────────────────┐ │  LAYER 1 · PRIMARY EFFECTOR
  │ STAFFING MODEL — balanced at every discipline,     │ │  "A branch cannot affect capacity if it is not
  │ unique to the market, SOC capacity as known slots  │ │   staffed appropriately at all discipline levels."
  └───────────────────────────────────────────────────┘ │
  ┌───────────────────────────────────────────────────┐ │  LAYER 2 · CONTROLLABLE PREPARATION
  │ TERRITORY — caseload distribution + resting posture │ │  Set clinicians so coverage + referral absorption
  │ so coverage & absorption are near-automatic         │ │  is nearly automatic.
  └───────────────────────────────────────────────────┘ │
  ┌───────────────────────────────────────────────────┐ │  LAYER 3 · DAILY MANAGEMENT
  │ DAY-TO-DAY — availability · patient willingness ·   │ │  Where the tool's cockpit + directive engine live.
  │ logistics · per-diem coordination                   │ │
  └───────────────────────────────────────────────────┘ │
  ┌───────────────────────────────────────────────────┐ │  MULTIPLIER (spans all layers)
  │ CULTURE & LEADERSHIP — protection → discretionary   │◀┘  Turns a good model into extra yeses; a bad one
  │ effort; reciprocity; respect + accountability       │    into quiet quitting and turnover.
  └───────────────────────────────────────────────────┘
```

Read it two ways: **each lower layer sets the ceiling for the layers above it** (staffing caps territory caps
day-to-day), and **culture multiplies whatever the stack produces** (a well-run day-to-day with a resentful
team leaks capacity; a lean model with a protected team punches above its weight).

---

## Layer 0 — Referrals (precondition)

Capacity is only a question once referral flow exists. Referral demand is *not* a capacity lever the branch
tunes to "make capacity"; it is the load the capacity stack must absorb. **Implication for the tool:** referral
inflow is an input to size and stress-test the model, never a substitute for fixing staffing. Accepting
referrals a branch cannot staff destroys quality, timeliness, and referral-source trust faster than declining
would.

## Layer 1 — Staffing model (the primary effector)

**The thesis:** the staffing model is what a branch can *change* to move capacity the most. It must (a) be
**balanced at every discipline level**, (b) be **unique to the market's potential**, and (c) treat **SOC
capacity as a managed, known-slot resource.**

### 1.1 Discipline balance — the offload structure
Assessing clinicians (RN, PT, OT, SLP) are the scarce, capacity-governing resource. Assistants (LPN, PTA, COTA)
exist to **absorb routine visits so assessing clinicians stay free for what only they can do.**

- Too few **LPNs** → RNs carry too many routine visits → RN assessment/SOC capacity collapses → admissions stall.
- Too few **PTAs** → PTs carry too much routine therapy → PT eval/SOC capacity collapses.
- The lever is the **RN:LPN and PT:PTA ratio**, derived from the branch's *case mix* (visit-type distribution),
  not a national default.

> **Rule (tool + agent):** treat an assessing clinician whose schedule is >X% routine visits while assistant
> capacity sits open as a **mis-offload** signal — the first thing to fix before declaring a capacity shortage.
> The directive engine's assessing→assistant offload already gestures at this; the staffing view must show the
> *structural* imbalance, not just the daily one.

### 1.2 SOC capacity as known slots
Many strong branches run **SOC-dedicated nurses (and sometimes SOC-dedicated PTs)** who see *only* SOCs/ROCs.
This converts the branch's most growth-critical capacity from "whatever's left over" into **predictable, bookable
slots** — capacity you can plan and sell against.

- **SOC assignment rule (authoritative — corrects the tool's current approximation):**
  - **RN performs any SOC where nursing is tied to the case.**
  - **PT performs the SOC only when nursing is NOT on the referral.**
  - (ROC follows the same discipline logic on the recert cycle.)
- **Known-slot model:** a dedicated SOC role has a countable weekly SOC capacity; the tool should track SOC
  slots *as their own resource*, separate from routine-visit capacity, because they are the binding constraint
  on growth (discovery CP-3).

> **Rule (tool + agent):** SOC-eligibility is **not** "any RN/PT." It is: RN whenever nursing is on the case;
> PT only when nursing is absent. The matcher must encode this and must protect dedicated-SOC roles from routine
> overflow (routine assigned to a SOC nurse is capacity leakage).

### 1.3 Market-uniqueness
The same census requires a **different model in different markets** — geography/density, payer & case mix,
referral-source profile, rural vs. urban, seasonality. A model that works in dense urban Charleston fails on a
rural loop. **Implication:** the tool should hold a *per-market staffing model* (target ratios, SOC roles, flex
depth) rather than one global template, and flag branches drifting from their market-appropriate model.

## Layer 2 — Territory management (controllable preparation)

Territory is the **controllable variable that pre-positions capacity** so day-to-day management is easy. Tie
caseload distribution to data and logic, and set each clinician into a territory that gives the most effective
**"resting posture"** — so that **coverage of active clients and absorption of new referrals is nearly
automatic**, not a daily scramble.

- A good resting posture = a clinician's active caseload is geographically coherent, leaving natural headroom
  and short travel to absorb a nearby new referral without disruption.
- Territory is where you *bank* future ease: the better the resting posture, the fewer heroic day-to-day moves.

> **Rule (tool + agent):** measure territory *health* — caseload geographic coherence, overlap/coverage per
> zip, absorption headroom by discipline — as a **preparation-layer signal**, distinct from today's open points.
> The agent should treat a referral that lands in a well-posture'd territory as low-friction and one that lands
> in a fragmented territory as a flag to fix posture, not just to force an assignment.

## Layer 3 — Day-to-day management (where the tool operates)

Given a sound model and good territory, daily capacity management is **clinician availability, patient
willingness, and logistics** — plus **per-diem coordination**, which branches struggle with because it's
planning- and communication-heavy. This is exactly where the capacity cockpit + directive engine earn their
keep: **making the need visible** so per-diem and flex capacity can be deployed cleanly.

- Per-diem is a **flex layer**, not a substitute for core staffing; heavy reliance on it is a Layer-1 signal.
- A good tool improves per-diem management primarily by **visualization** — the team can see the need clearly,
  early, and match it to available flex.

> **Rule (tool + agent):** surface per-diem need *ahead of time* (forecasted gaps by discipline/zone/day),
> track engagement/disengagement, and make the coordination a one-click ask. But if per-diem is being used to
> paper over a structural gap, the agent should say so (escalate to Layer 1), not just keep booking flex.

## Multiplier — Culture & leadership

Culture decides whether the stack's theoretical capacity is *realized*. Clinicians go the extra mile — one more
PT eval on a Friday, one more SOC near full — **when the branch has earned it** by protecting them.

- **Reciprocity is the mechanism.** The nurse whose manager quietly offloaded her visits during a hard personal
  week is the nurse who says "yes" to the out-of-territory Friday visit later. Protection banked becomes
  discretionary effort withdrawn.
- **Respect + accountability** are the two rails: clear policies/processes that make the normal day better, and
  fair, consistent expectations across the team.
- Discretionary effort is **real capacity** — but it is *borrowed*, and it must be repaid or it disappears (and
  takes the clinician with it, on a turnover lag).

> **Rule (tool + agent):** the tool should make protection *legible and fair* — track who's been asked to stretch,
> whether the team is sharing the load equitably, and whether stretch is being repaid (lighter following week).
> **The agent must treat discretionary effort as a scarce, borrowed resource:** ask the clinician the branch has
> protected, frame it as a favor not an order, never ask the same person repeatedly, and never let an "ask"
> become the default coverage plan. Exploiting the yes destroys the culture that produced it.

---

## Capacity business rules (v0) — for the tool and the agents to enforce

Distilled from the above; each is a candidate for the matching engine + agent training. Mark ✔ where the tool
already does it, ✎ where it needs building.

| # | Rule | Status |
|---|---|---|
| SOC-1 | RN performs any SOC where **nursing is on the case**; PT performs the SOC **only when nursing is not on the referral**. ROC follows the same logic. | ✎ (tool currently treats any RN/PT as SOC-capable) |
| SOC-2 | Track **SOC/ROC slots as a distinct capacity resource**; protect dedicated-SOC roles from routine overflow. | ✎ |
| BAL-1 | Flag an assessing clinician running **>X% routine** while assistant capacity is open (a mis-offload / discipline-imbalance signal) before declaring a shortage. | ~partial (daily offload exists; structural view ✎) |
| BAL-2 | Hold a **per-market staffing model** (RN:LPN, PT:PTA, SOC roles, flex depth); flag drift from market-appropriate ratios. | ✎ |
| TERR-1 | Score **territory health** (caseload coherence, coverage per zip, absorption headroom) as a preparation-layer signal. | ✎ |
| DAY-1 | **Enforce restrictions/competencies** in matching ("No SOC", "No wound care", "No high-acuity", "Recerts only", "Weekends only") — hard filter, never just displayed. | ✎ (current correctness gap) |
| DAY-2 | Debit **travel + non-visit work** from capacity, not just visit points; use **drive-time**, not straight-line distance. | ✎ |
| PD-1 | Surface **per-diem need ahead of time**; track engagement; escalate to Layer 1 when flex is covering a structural gap. | ~partial (disengagement flag exists) |
| CUL-1 | Make discretionary effort **legible and fair**: track asks, load-sharing equity, and repayment (protect after stretch). | ✎ |
| CUL-2 | Agent **must not** exploit the yes: ask the protected clinician, frame as favor, never repeat-ask the same person, never make the ask the default plan. | ✎ (agent guardrail) |

## How this drives the tool and the AI agents

- **Tool:** the strategy stack maps to views. Layer 1 → a *staffing-model / discipline-balance* view (not just a
  roster). Layer 2 → a *territory-health* view (beyond the current capacity map). Layer 3 → the cockpit
  (exists). Culture → a *fairness/stretch-ledger* signal. Each layer needs its own leading indicators.
- **AI agents:** every directive the engine emits should carry its **layer** and respect the **business rules**
  above. A day-to-day directive that violates a Layer-1 truth (e.g. "just have the RN take more routine") is
  wrong even if it balances today. Agents are trained on the **tactics library** ([`../sme/`](../sme/)) —
  SME-sourced, validated patterns of what great branches actually do — so their recommendations reflect real
  operating wisdom, not just the math.

## Open strategic questions (for SME discovery)

- The **X% routine threshold** that signals RN/PT mis-offload — what is it, by discipline?
- Target **RN:LPN / PT:PTA ratios** by case-mix archetype — what are the real numbers?
- When is a **dedicated SOC role** justified (referral inflow / SOC-ROC volume threshold)?
- What defines a healthy **resting posture** quantitatively (coherence, headroom)?
- How much **per-diem flex** is healthy vs. a red flag?
- How is **discretionary effort** best made fair and repaid without turning it into a metric people game?
