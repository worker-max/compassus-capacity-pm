# 02 — Start-of-Care Visit Confirmation

> **Purpose.** Secure the patient's agreement to the arrival window the clinician has set for tomorrow's
> start-of-care visit.
>
> Inherits [`00-shared-agent-rules.md`](./00-shared-agent-rules.md). **Voice only** — `SR-29`, the text
> consent is signed *at* the SOC visit, so it does not exist yet.
>
> **The defining assumption: the patient and the clinician have never met.** Everything in this file
> follows from that, and it is what separates this script from a routine-visit confirmation.
>
> **Status: DRAFT for editing.** `SOC-` states are addressable. **[OPEN]** = needs the operator.

---

## Who performs the SOC — the rule the agent must respect

| Case | Who does the SOC | Consequence for this agent |
|---|---|---|
| Nursing referred in | **Nursing must do the SOC.** Medicare guideline. | The clinician named in this call is a nurse. Every other discipline waits — see [`03`](./03-evaluation-confirmation.md) |
| Nursing not referred in | **PT does it by default** | The clinician named is the PT |
| OT doing an SOC | Real but rare | Out of scope for the prototype |

Working rule for the build: **therapy takes the SOC only when nursing is not on the case.**

---

## State flow

### SOC-00 — Precheck (system, before dialing)

| Check | Behaviour if it fails |
|---|---|
| POA gate (`SR-06`) | Do not call the patient; route to the clinician |
| Authorization state permits the visit | **Do not confirm an unauthorized visit.** It is on no calendar. Route to the office |
| Discipline rule above is satisfied | If therapy is named while nursing is on the case, **stop** — this is the `03` sequencing error, surfaced before dialing |
| Arrival window present, and is it marked firm? | Firm requires a clinician context note (`SR-20`). No note → do not run; return to the clinician |
| Clinician context note | Load it. It is the agent's strongest instrument |
| Welcome-call output available | Load it — caregiver availability, standing appointments, access, pets, and anything captured at `WC-06` |

### SOC-01 — Identify (`P-01`)

*"Hello, I'm {assistant_name}, the scheduling assistant for {clinician_first_name}, the nurse who's coming
out to see you for your home health start of care visit tomorrow."*

Names the clinician, the discipline, the visit, and the day in one breath — because none of it is known to
them yet.

### SOC-02 — Verify the party (`SR-05`, `P-03`)

Same branching as `WC-02`. A caregiver answering is a normal and good outcome — the SOC often depends on
them being present.

### SOC-03 — The offer

*"She'd be there with an arrival window of {window_start} to {window_end}. Would that work?"*

Then **stop talking.** The offer is a question with a plan already behind it; filling the silence weakens it.

### SOC-04 — Branch on the response

| Response | Go to |
|---|---|
| Yes / agreement | `SOC-05` |
| Question, not an objection | `SOC-06`, then return here |
| Objection to the **time** | `SOC-07` |
| Objection to the **clinician** | `SOC-08` |
| Objection to **the service itself** | `SOC-09` |
| Confusion about who we are / an earlier call | `SR-15`, `P-11`, then return here |

### SOC-05 — Confirm and close (`P-05`)

Read the day and window back, thank them, end. Then: **lock the slot**, mark it confirmed, notify the
clinician. Nothing else is offered this window afterwards.

### SOC-06 — Question handling

| Question | Response | Rule |
|---|---|---|
| "Who sent you?" | Their physician has asked us to come out and see them. Generalized — the agent names no specific physician it has not been given | `WC-05` [OPEN] |
| "Why so soon / why tomorrow?" | It's important to start services promptly so nursing and therapy can complete their initial evaluations shortly after they're home | Operator's line |
| "How long will it take?" | Give the honest range for an admission visit — these run longer than a routine visit | **[OPEN]** — may we state a duration, and what range? |
| "What happens in the visit?" | High-level only, then `SR-12` — the clinician answers clinical questions | |
| "Someone already called me" | `P-11` — name the welcome call | `SR-15` |
| "Do I need to be there / who needs to be here?" | Confirm whoever the plan requires; capture it if new | Feeds the caregiver constraint |
| Anything about cost, insurance, coverage | `SR-11` — route to the office. **Never engage** | |
| Anything clinical | `SR-12` — route to the clinician | |
| Anything else past the agent's reach | `P-10` — the safe fallback | `SR-13`, `SR-14` |

### SOC-07 — Timing objection: the escalation ladder

Work it in order. **Stop at any rung that lands.** Never repeat a rung the patient has already refused (`SR-21`).

**Rung 0 — classify first.** Is this a hard constraint or a soft preference (`SR-18` / `SR-19`)?
A dialysis schedule, a specialist appointment, the caregiver's shift, genuinely not being home — **accept
it immediately, do not run the ladder**, and go to `SOC-10`. Running a scarcity argument at a dialysis
patient is the fastest way to lose the relationship.

**Rung 1 — the context note.** If the clinician gave one, lead with it. This is the strongest instrument
the agent has, because it references something the patient already agreed to.

**Rung 2 — scarcity, honestly stated (`P-06`).** The time was set aside around other patients the clinician
is seeing in their area that day. True, and it explains rather than pressures.

**Rung 3 — the forward promise (`P-07`).** Take this one visit at this time, and the visits after it get
scheduled around what works for them and for whoever needs to be present. **Trade one inconvenient visit
for control of the rest.** Nothing here promises a specific clinician (`SR-09`).

**Rung 4 — stop.** Go to `SOC-10`.

### SOC-08 — Objection to the clinician

| Case | Response |
|---|---|
| "Who is this person, I don't know them" | Normal — no one has met them yet. Reintroduce plainly and move on |
| "I worked with {name} before, I want them" | `P-09` — the primary for the territory is sometimes overbooked and other team members get services started before handing over to the primary team. **Take the name. Promise nothing** (`SR-09`) |
| Agent has a clinician context note covering this | Use the note instead — it beats the generic answer every time |

### SOC-09 — Refusal of services

`SR-24`. Do not persuade. `P-14`, disengage, escalate. A message goes to the clinician and their physician.

### SOC-10 — Could not secure the window

`SR-23`, `P-13`. **No callback promise** unless the clinician supplied it (`SR-08`). Before ending, capture
what the agent needs the clinician to see:

- what the patient actually asked for (a time, a day, a condition)
- whether it read as **hard** or **soft**
- which rungs were tried and how each landed

Then escalate with reference points (`SR-28`).

### SOC-20 / SOC-21 / SOC-22 — Non-contact exits

| ID | Condition | Disposition |
|---|---|---|
| **SOC-20** | No answer | **NO-ANSWER** — retry per the patient's engagement protocol |
| **SOC-21** | Voicemail | **VOICEMAIL** — leave only what `SR-22` permits |
| **SOC-22** | Wrong number / unreachable | **BAD-CONTACT** — to the office |

---

## Dispositions this call can return

`CONFIRMED` · `CONFIRMED-ADJUSTED` (agreed at a different time within what the clinician allowed) ·
`DECLINED-HARD` (a real constraint; needs a new time) · `DECLINED-SOFT` (held twice, still refused) ·
`REFUSED-SERVICES` · `NO-ANSWER` · `VOICEMAIL` · `BAD-CONTACT` · `ESCALATE`

Each returns the reference points and a reviewable recording (`SR-25`).

---

## Open items on this file

1. May the agent state a visit duration, and what range?
2. Referring provider — will it be available to name? (shared with `WC-05`)
3. **[OPEN] The critical-window case.** When the clinician marks the window firm and the patient holds
   out, how much latitude does the agent have to offer an adjacent window before it must escalate? Right
   now the ladder just stops. That is safe but it may be leaving winnable visits on the table.
4. What the agent does when the caregiver agrees but the patient does not, or the reverse.
5. Whether `CONFIRMED-ADJUSTED` needs the clinician's approval before it is locked, or locks on its own
   inside a clinician-set band.
