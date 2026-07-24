# SME Discovery Framework — sourcing tactics, building the agents

> **Purpose.** A repeatable way to (1) pull real capacity-management tactics from home-health subject-matter
> experts, (2) validate them, and (3) turn each into **tool logic** *and* **AI-agent training**. This is how the
> capacity strategy ([`../strategy/capacity-strategy-foundation.md`](../strategy/capacity-strategy-foundation.md))
> gets filled in, corrected, and kept honest by the people who actually run branches.
>
> **The premise.** Great branches already know how to manage capacity — the knowledge is tacit and unevenly
> distributed. The job is to *extract it, structure it, and encode it* so every branch (and every AI agent in
> the tool) operates like the best one. We are not inventing tactics; we are harvesting and systematizing them.

## The pipeline

```
  SME  ──▶  tactic captured  ──▶  validated  ──▶  ┬─▶  SYSTEM RULE (measure / flag / enforce)
 (interview   (structured        (cross-checked    │
  or panel)    schema)            vs data + peers)  └─▶  AGENT TRAINING (reason / recommend / guardrail)
```

Every tactic ends life as **at least one of** a system rule or an agent-training example — usually both. A
tactic that can't be turned into either is a story, not a tactic; log it as context and move on.

## The SME roster (whose perspective we need)

Sourced to the capacity stack — each layer has owners who see it best. Prioritize the **top-performing branch's**
version of each role; the goal is to encode what the *best* do.

| Layer | SME roles to interview | What only they can tell us |
|---|---|---|
| Staffing model (L1) | **Branch Executive Director**, **Workforce/Staffing Strategist**, Area/Regional VP | Discipline-ratio truth, market-unique sizing, when to create a SOC role, unit economics |
| Clinical ops (L1↔L3) | **DCS / Clinical Manager** | Offload discipline, SOC/ROC assignment, acuity judgment, compliance-as-constraint |
| Territory (L2) | Branch Director, **senior Scheduler**, tenured field clinicians | Resting posture, caseload distribution, drive-time reality |
| Day-to-day (L3) | **Senior Scheduler / Staffing Coordinator**, **Per-Diem Coordinator** | The last-minute decision tree, per-diem engagement, real availability |
| Clinician truth | **Tenured field RN / SOC nurse**, PT, per-diem clinician | What earns the "yes," continuity, burnout signals, what a tool must never do |
| Culture (multiplier) | Branch ED + clinicians together | Reciprocity, protection, fairness, accountability |
| Outside-in | Intake/referral coordinator, a **referral source** (discharge planner) | What makes them route to us; speed/certainty they buy |

**Seeded v0:** we've already generated *hypothesized* tactics from five of these lenses (Branch ED, DCS,
Scheduler, Field RN/SOC nurse, Workforce Strategist) — see the [tactics library](./capacity-tactics-library.md).
Those are **starting hypotheses to validate with real SMEs**, not settled truth. They make the interviews
faster: confirm, correct, or kill each, and add what we missed.

## The interview method

**Format.** 45–60 min, one role at a time; then a **cross-role panel** on the two or three tactics where roles
disagree (disagreement is signal — it's usually a real tension to design around, not a wrong answer).

**Opening frame (every interview):** *"Think about the best branch you've seen run capacity. What did they
actually do differently — day to day — that a struggling branch doesn't? Be specific."*

**Probe by layer** (skip what's not their lane):
- **Staffing:** "How do you know a branch is mis-staffed *before* census stalls? What ratio of RN:LPN / PT:PTA do
  you actually run, and why that number for this market? When do you create a dedicated SOC nurse/PT?"
- **SOC:** "Walk me through who takes a SOC when nursing is on the case vs. not. How do you protect SOC capacity
  from routine overflow?"
- **Territory:** "How do you decide who covers where? What does a well-set-up clinician's territory look like so
  new referrals just get absorbed?"
- **Day-to-day:** "It's Friday at 3pm and a SOC comes in for a full clinician's ZIP. Walk me through exactly what
  you do — who you ask, in what order, how you ask." "How do you keep per-diems engaged and ready?"
- **Culture:** "Tell me about a time a clinician went the extra mile. What had the branch done to earn it? What's
  the fastest way to burn that goodwill?"
- **The anti-pattern:** "What's the most common mistake branches make that looks fine on a report but is killing
  capacity?" (The Branch ED's answer — *never diagnose 'we're full' without decomposing skilled clinicians' days
  by visit type* — is exactly the kind of gold this question surfaces.)

**Closing:** "If an AI assistant were helping your scheduler tomorrow, what should it *always* do, and what must
it *never* do?" → this directly seeds agent guardrails.

## The tactic-capture schema

Capture every tactic in this exact shape (it's what makes a tactic buildable and trainable):

| Field | What goes here |
|---|---|
| **Tactic** | Crisp name + 1–2 sentences: what the great branch actually does |
| **Layer** | Staffing / Territory / Day-to-day / Culture (or precondition) |
| **Trigger / context** | When it applies |
| **Why it works** | The operational mechanism |
| **Encode as system logic** | The rule / threshold / signal / formula the tool computes or enforces |
| **Train the AI agent** | How the agent reasons or acts on it — including explicit *"must never do X"* guardrails |
| **Evidence / confidence** | SME source(s), whether data confirms it, confidence (hypothesis / SME-asserted / data-validated) |
| **Open number** | Any threshold/ratio that still needs a real value (routes to the strategy's open questions) |

## Validation — before a tactic becomes a rule

A tactic graduates from "SME-asserted" to "encode it" when it clears:
1. **Cross-role check** — does at least one other role agree, and is the disagreement understood?
2. **Data check** — do the branch's own numbers move the way the tactic predicts (where data exists)?
3. **Guardrail check** — is there a way this rule, automated, could harm a clinician or a patient? If yes, it
   ships with the guardrail, not without it. (Clinician-facing asks especially — see the field-RN "must never"
   list.)
4. **Falsifiability** — what would tell us this tactic is wrong here? Write it down; revisit.

## From tactic → the two products

- **System rule.** Goes into the capacity business-rules set (strategy doc) and the tool backlog: a measure, a
  flag, a threshold, a formula, or a hard filter in the matching engine.
- **Agent training.** Becomes a training example for the AI agents operating in the tool: the situation, the
  correct reasoning, the recommended action, and the *prohibited* action. Structured so a directive the engine
  emits carries its **layer** and respects the **guardrails**. The tactics library is the corpus; as it grows,
  it's the difference between an agent that does math and one that reasons like a good branch manager.

## Running list of "open numbers" to get from SMEs

These are the thresholds the strategy needs real values for (they route here from the strategy's open questions):
- RN routine-visit % that signals mis-offload (ED hypothesized ~20–25%) — by discipline, by market.
- Target **RN:LPN / PT:PTA** ratios by case-mix archetype.
- Referral-inflow / SOC-ROC volume that **justifies a dedicated SOC role**.
- Healthy **resting-posture headroom** per territory (quantified).
- Healthy **per-diem flex %** vs. the red-flag level that means core staffing is short.
- **Referral-to-SOC** target intervals by source type.
- The **fairness** mechanics of discretionary effort — how to make it equitable and repaid without gaming.

## Cadence

- **Round 1 (now):** validate the seeded v0 tactics with one SME per role; capture new tactics.
- **Round 2:** cross-role panel on the tensions; lock the "open numbers" you can.
- **Ongoing:** every branch rollout is a discovery site — the best branches surface new tactics; feed them back
  through the schema so the library (and the agents) keep learning.
