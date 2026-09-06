# 01 — The Welcome Call

> **Purpose.** Establish that the patient is actually home and available, so the start-of-care visit can
> be scheduled. This call happens **before** any scheduling engagement and is the patient's first contact
> with the agency in many markets.
>
> Inherits every rule in [`00-shared-agent-rules.md`](./00-shared-agent-rules.md).
> **Voice only** — `SR-29`, because no text consent exists until the SOC visit.
>
> **Status: DRAFT for editing.** `WC-` states are addressable. **[OPEN]** = needs the operator.

---

## [OPEN] Terminology to settle first

The knowledge base carries **two** calls that may be one call or two:

- **Welcome / intake call** — the scheduler's, described as *the scheduler's one true judgment call: is the
  patient actually home — not still inpatient, not deferring home-health admission to a later date.*
  It happens before the SOC and evals are assigned, so clinicians are never sent to a patient who isn't there.
- **Readiness call** — the PCC's, which *confirms home health orders, sets an arrival window, and gathers
  logistics — pets, competing doctor's appointments.* Standard everywhere but not universally performed.

The operator's description — *"in place to check and make sure that the patient is home and available"* —
matches the first. This file is drafted as **one call carrying both jobs**, with the logistics block
(`WC-06`) marked optional. **Confirm whether that is right before we build.**

---

## The one thing this call must produce

**A reliable answer to: is this patient home, and can a visit be scheduled?** Everything else is secondary.
A wrong answer here sends a clinician to an empty house and burns an SOC slot.

---

## State flow

### WC-00 — Precheck (system, before dialing)

| Check | Behaviour if it fails |
|---|---|
| Active POA on the case? | Apply `SR-06`. If the POA bars patient contact, do not call the patient — route to the office. |
| Best contact number and party on file? | If missing, do not guess. Return to the office. |
| Referral state permits scheduling? | If the referral has not cleared intake/auth, **do not call.** [OPEN] — confirm whether the welcome call precedes or follows the auth gate. |
| Region requires a script variant? | Load it. See `WC-07`. |

### WC-01 — Identify

`P-02`. Agency name, assistant name. **This call is not attached to a clinician** — no clinician has been
assigned yet, so `SR-01`'s named-clinician framing does not apply.

### WC-02 — Verify the party (`SR-05`)

`P-03`. Branch:

| Answer | Go to |
|---|---|
| The patient | `WC-03` |
| Primary caregiver / family on the case | `WC-03` |
| Someone else in the household | Ask for the patient or the person helping with their care. If unavailable → `WC-90` |
| Wrong number | `WC-91` |

### WC-03 — State the purpose plainly

Draft: *"Your doctor has asked us to come out and see you at home now that you're back. I'm calling to make
sure you're home and settled so we can get that first visit scheduled."*

Two things this does: it names the physician as the origin (see `WC-05`), and it frames the call as
**checking on them**, not selling them anything.

### WC-04 — The core determination: home and available?

This is the judgment the whole call exists for. Branch on what is actually true:

| Situation | Disposition | Agent behaviour |
|---|---|---|
| Home now, ready | **READY** | → `WC-06` |
| **Still inpatient** | **NOT-HOME-INPATIENT** | Capture expected discharge date if offered. Do not schedule. → `WC-08` |
| Home, but discharge was today / still settling | **READY-SOFT** | Note it; the SOC agent should be told. → `WC-06` |
| Going to a family member's / different address | **ADDRESS-CHANGE** | Capture the address they give. **Do not confirm it as valid** — the office verifies service area. → `WC-08` |
| Wants to defer home health to a later date | **DEFERRING** | Capture the date if offered. Do not argue. → `WC-08` |
| Declining services outright | **DECLINING** | `SR-24`. Disengage. → `WC-92` |
| Confused, cannot answer, no caregiver available | **UNCLEAR** | `SR-24`. Disengage. → `WC-92` |

**[OPEN] — how hard should this call push on DEFERRING?** There is a real timeliness argument (services
started promptly, evaluations completed shortly after returning home) and a real risk of pressuring a
patient who just got home. My read is: state the reason **once**, accept the answer, escalate. Confirm.

### WC-05 — Handling "who sent you / who is this"

Use the generalized physician framing: *their physician has asked us to come out and see them.* **[OPEN]** —
whether the agent will actually have the referring provider (PCP vs. hospitalist) available. Until that is
settled the agent stays generalized and never names a specific physician it has not been given.

### WC-06 — Logistics capture *(optional block — see terminology note)*

Ask only what materially affects the visit landing:

| Item | Why |
|---|---|
| Who needs to be present, and their availability | Feeds the caregiver-present constraint — the single most common cause of a failed visit |
| Standing appointments this week (dialysis, MD, specialist) | Hard constraints (`SR-18`) the scheduling agent must build around |
| Any times that genuinely do not work | Distinguish hard from soft here if possible; the note carries forward |
| Pets in the home | Clinician safety and access |
| Access / entry — gate code, apartment, stairs, parking | Prevents a clinician standing outside a locked door |
| Best number to reach them | Everything downstream depends on it |

**Everything captured here becomes the context the SOC agent opens with.** That handoff is the point of the
block — otherwise the patient answers the same questions twice, which is exactly the confusion `SR-15` exists
to prevent.

### WC-07 — Regional safety screening *(gated by market)*

Washington / Providence requires safety screening questions — firearms in the home, others present, mental
illness — instituted after a clinician was killed in a patient's home.

**[OPEN] — does the AI agent ask these, or is this block always human?** These are heavy questions and the
answers carry real consequence. My recommendation is that in the first prototype **the agent does not ask
them**, and any market requiring them routes the welcome call to a person. Needs the operator's decision.

### WC-08 — Set the expectation, then close

For **READY**: tell them someone will be in touch to set the visit time — **without promising when**
(`SR-08`), unless the process guarantees it and the operator says the agent may state it.

For **NOT-HOME-INPATIENT / DEFERRING / ADDRESS-CHANGE**: tell them the office will follow up. Nothing more.

### WC-90 / WC-91 / WC-92 — Exits

| ID | Condition | Disposition |
|---|---|---|
| **WC-90** | Right household, right party unavailable | **RETRY** — re-attempt per protocol |
| **WC-91** | Wrong number / unreachable | **BAD-CONTACT** — to the office, do not retry the same number |
| **WC-92** | Disengaged per `SR-24` | **ESCALATE** — message to the clinician and physician per `P-14` |

---

## Dispositions this call can return

`READY` · `READY-SOFT` · `NOT-HOME-INPATIENT` · `DEFERRING` · `ADDRESS-CHANGE` · `DECLINING` · `UNCLEAR` ·
`RETRY` · `BAD-CONTACT` · `NO-ANSWER` · `ESCALATE`

Each carries: what was said, what was captured, and the reviewable recording (`SR-25`).

---

## Open items on this file

1. Is the welcome call one call or two (welcome/intake + readiness)?
2. Does it sit before or after the authorization gate?
3. How hard may it push on a deferral?
4. Will the referring provider be available to name?
5. Does the AI agent ever run the regional safety screening, or does that route to a human?
6. May the agent state *when* the scheduling call will come?
