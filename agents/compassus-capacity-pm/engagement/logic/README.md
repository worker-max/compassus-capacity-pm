# Engagement Logic — the agent behaviour specs

> **What this is.** The conversational logic for the patient-facing engagement agents, written as
> numbered, addressable states so it can be edited a line at a time rather than rewritten. This is the
> substrate the voice agent prompts get built from — it is **not** the prompt itself.
>
> **Status: DRAFT, first pass.** Everything here derives from the operator's captures in
> [`../day-before-confirmation-protocol.md`](../day-before-confirmation-protocol.md) plus the project
> knowledge base. **[OPEN]** markers flag what I inferred or what is unresolved.

## The files

| File | Covers | Channel |
|---|---|---|
| [`00-shared-agent-rules.md`](./00-shared-agent-rules.md) | Rules every agent inherits — identity, who it may speak to, what it may never promise, the safe fallback, negotiation doctrine, escalation, the phrase bank | all |
| [`01-welcome-call.md`](./01-welcome-call.md) | Is the patient home and available, so the SOC can be scheduled | **voice only** |
| [`02-soc-confirmation.md`](./02-soc-confirmation.md) | Confirming tomorrow's start-of-care visit, assuming no prior relationship | **voice only** |
| [`03-evaluation-confirmation.md`](./03-evaluation-confirmation.md) | Confirming a discipline's initial evaluation, behind the SOC sequencing gate | voice, or text where consent was captured |

Routine, assessment, recert and discharge confirmations are **not written yet** — deliberately, per the
operator's sequencing. They come after these three are settled.

## Why the first three are voice

`CN-09` — the text and email consents are separate and are signed **at the SOC visit**. Nothing before that
visit has a consented text channel. So the welcome call and the SOC confirmation are voice by regulation,
not by preference, and the evaluation call is voice unless a consent was actually recorded.

That is also why these are the right first agents to build: **the voice agent is the one that is unblocked.**

## How to edit this

Every rule, state and phrase has an ID. Say *"change SR-08"* or *"SOC-07 rung 3 is wrong"* and the change
lands in one place. IDs are stable — new items take the next free number, nothing gets renumbered.

## The biggest open items across all three

1. **`CN-10`** — California treats an automated outbound call as a robocall. Needs a legal answer. It gates
   whether these agents may place calls at all in some markets.
2. **`SR-22`** — what may be left on a voicemail without a signed share-with-family consent.
3. **Whether the welcome call is one call or two** (welcome/intake + readiness).
4. **Whether the AI ever runs the regional safety screening** (`WC-07`), or that always routes to a human.
5. **How much latitude the agent gets on a firm-marked window** before it must escalate (`SOC-07`).
