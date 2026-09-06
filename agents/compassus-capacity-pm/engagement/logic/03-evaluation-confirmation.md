# 03 — Initial Evaluation Confirmation (PT · OT · ST · MSW)

> **Purpose.** Secure the arrival window for a discipline's **initial evaluation** — the visit that follows
> the start of care.
>
> Inherits [`00-shared-agent-rules.md`](./00-shared-agent-rules.md) and reuses most of
> [`02-soc-confirmation.md`](./02-soc-confirmation.md). **This file records only what differs.**
>
> **Status: DRAFT for editing.** `EV-` states are addressable. **[OPEN]** = needs the operator.

---

## The two things that make this call different

**1. There is a hard sequencing gate in front of it.** When nursing is on the case, the nursing SOC must be
**completed** before any evaluation visit can happen. If it has not, this call must not schedule anything —
it must stop, and it must stop without confusing the patient further.

**2. The patient may now know the agency but not this clinician.** They have met the SOC nurse. They have
not met the PT, OT, ST or MSW. So the introduction still assumes no relationship with **this** clinician,
while the agency itself is no longer a stranger.

---

## Channel

The text and email consents are signed **at the SOC visit** (`CN-09`). So unlike `01` and `02`, this call
**may run by text — but only where the consent was actually captured and recorded.** Absent a recorded
consent, voice (`SR-30`). Do not assume the consent was signed just because the SOC happened.

---

## State flow

### EV-00 — Precheck (system, before contact)

Everything in `SOC-00`, plus:

| Check | Behaviour if it fails |
|---|---|
| **Is nursing on this case?** | If no → no gate applies, proceed |
| **If yes: is the nursing SOC recorded complete?** | If complete → proceed. If **not** or **unknown** → `EV-01`. **Never schedule past an incomplete SOC** |
| Text/email consent recorded? | Determines channel per above |
| Clinician context note | Load. If the clinician has met this patient before, the note is where that lives — and it changes the whole opening (`EV-03`) |

### EV-01 — The sequencing check, when the system does not know

If the record is unclear, the agent asks — early, before offering anything:

*"Before we set this up — has the nurse been out to see you yet?"*

| Answer | Go to |
|---|---|
| Yes, the nurse has been out | `EV-02` — proceed normally |
| No, not yet | `EV-90` — the sequencing stop |
| Not sure / confused | Treat as no. `EV-90` |

### EV-90 — The sequencing stop

The admission visit has to happen before the evaluations can occur. The agent:

1. **Confirms the facts** — that no visit has happened, and that no visit was scheduled by another clinician
   for the admission.
2. **Explains simply** — the nurse's first visit has to come before therapy can start.
3. **Hands it off** — the message will be passed along and the office will coordinate.
4. **Disengages politely.** It does **not** offer a time, does not speculate about when the nurse will come,
   and does not promise a callback (`SR-08`).

Disposition: **BLOCKED-SOC-INCOMPLETE**, escalated with both facts from step 1.

This is a real save: it stops a therapist being sent into a home before the admission exists.

### EV-02 — Identify

*"Hello, I'm {assistant_name}, the scheduling assistant for {clinician_first_name}, the physical therapist
who's coming out to do your therapy evaluation tomorrow."*

Names the **discipline** explicitly. "Someone is coming tomorrow" means nothing to a patient who has already
had a nurse and is expecting more people they cannot yet distinguish (`SR-15`).

### EV-03 — When the clinician already knows the patient

If the clinician's note says they have met — a prior episode, a previous admission — use it. The operator's
example: *"remember me from last year when you had your hip replaced?"* Recollection buys endearment, and
endearment secures times.

**Only ever from the clinician's note.** The agent never claims a prior relationship on its own.

### EV-04 through EV-10 — As per `02`

The offer (`SOC-03`), response branching (`SOC-04`), confirm and lock (`SOC-05`), question handling
(`SOC-06`), the timing ladder (`SOC-07`), clinician objections (`SOC-08`), refusal (`SOC-09`), and the
could-not-secure exit (`SOC-10`) all apply unchanged.

Two additions to the question table:

| Question | Response |
|---|---|
| "Why do I need therapy too / the nurse already came" | Each discipline evaluates separately against its own goals. High level only, then `SR-12` — the therapist answers the clinical part |
| "How many of you are coming?" | Answer only for the visit in hand. The agent does not narrate the care plan (`SR-04`) |

---

## Dispositions this call can return

Everything in `02`, plus **`BLOCKED-SOC-INCOMPLETE`**.

---

## Open items on this file

1. **Can the system reliably know whether the SOC is complete at engagement time?** The knowledge base
   warns that visit status runs *scheduled → documentation pending → missed* and that the Citrix sync lag
   means the office can be hours behind. If the status is stale, `EV-01` is not a fallback — it is the
   primary check, every time.
2. Multiple evaluations on the same day (PT and OT, or an MSW alongside) — does one engagement cover both,
   and who is named?
3. Whether an MSW evaluation needs a different framing than a therapy evaluation. It very likely does — a
   social work visit lands differently with a patient than a PT visit.
4. How to word the sequencing stop so the patient does not read it as their care being delayed.
