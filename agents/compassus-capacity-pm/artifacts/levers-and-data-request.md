# Capacity and Scheduling: what this program is worth, and what we need to prove it

Two lists. The first is how this program makes or saves money, in plain terms. The second is the
data we need to request in order to put real numbers against each one.

---

# Part one: the business case levers

Seven ways this produces money, plus three we believe are real but have not put a number on yet.

---

## 1. We start more patients on service

**What happens.** We take on more patients without hiring, because we can see who has room and give
the hospital an answer faster.

**Why it works.** A clinician's open slot for tomorrow is like an empty seat on tomorrow's flight.
If it does not get filled, it is gone, and it does not come back the next day. Today the answer to
"can we take this patient" is slow, so slots expire while we are still working it out. The referral
system is getting better at accepting referrals; this picks up where that leaves off and turns an
acceptance into a started episode before the capacity to serve it disappears.

**What has to be true.** Referrals have to be there to take. They are, because we currently decline
some for lack of capacity.

**Rough size.** The largest single lever, and the one most worth arguing about.

---

## 2. We replace a canceled visit before the clinician's day is lost

**What happens.** A patient cancels, usually the evening before or the same morning. Rescheduling
that patient is normally handled during the cancellation call. What is left behind is a hole in the
clinician's day, and today we often cannot fill it fast enough for a replacement to actually fit
their schedule and their geography. So the slot is simply lost.

**Why it works.** This is an infrastructure problem, not a communication problem. To fill that hole
we need to know instantly which other patients are due, which of them are near enough, who is
approved, and which visits are flexible enough to move. Sometimes the right answer is pulling a
visit forward from later in the week, which trades a hole we cannot fill today for one we have
several days to fill. That is a decision nobody can make quickly by hand.

**Two things worth saying out loud to a leader.**

First, with most of our clinicians paid per visit, a lost slot is lost income for them, not lost
revenue for us. This is one of the clearest links between how well we schedule and why people leave.

Second, this gets harder as scheduling gets better. A tightly planned week has less slack to absorb
a cancellation than a loosely planned one. So the replacement capability has to come with the
optimization, not after it, or we will have made the problem worse.

**What has to be true.** We need to know which visits are genuinely movable and which are not.

---

## 3. Fewer Medicare periods fall short on visits

**What happens.** We see a 30-day Medicare period heading for too few visits while there is still
time to put a clinically needed visit back.

**Why it works.** Medicare pays a fixed amount for a 30-day period, but only if a minimum number of
visits happen. Miss it by one and the payment for the whole period drops sharply. Most misses are by
a single visit, and usually because a visit was missed or moved rather than because fewer visits
were needed. Today we find out after the period closes, when nothing can be done.

**The line we do not cross.** We would never add a visit a patient does not need in order to reach a
number. Federal auditors are actively looking at exactly that pattern. The only visits worth
recovering are ones that were clinically indicated and were lost to a scheduling failure.

---

## 4. Scheduling takes fewer people

**What happens.** Assigning visits requires fewer roles once the repetitive parts happen on their
own.

**Why it works.** Schedulers today spend most of their day working a task list rather than making
scheduling decisions. The same patient generates a separate task for every discipline involved,
twice over. Remove that work and the roles are no longer needed.

**Two honest caveats.** Some of this work should not exist at all, which means we cannot claim
credit for removing all of it. And the best published example of this software elsewhere freed ten
roles across roughly twenty to thirty branches, which is a good deal less than the three hundred to
one hundred figure discussed on site.

---

## 5. We buy less premium labor

**What happens.** Fewer visits covered by agency staff, overtime, or bonus pay because we could not
find anyone else in time.

**Why it works.** When someone calls out at seven in the morning, nobody can see who has room, so the
branch reaches for the most expensive option or loses the visit. Seeing available capacity turns an
emergency purchase into a planned assignment.

**One caveat.** Because most of our clinicians are paid per visit, the saving is the difference
between our rate and the agency rate, not the whole agency bill. In an organization with salaried
clinicians this lever would be much larger.

---

## 6. Fewer clinicians leave

**What happens.** A steadier, more predictable week means fewer resignations, and we spend less
replacing people.

**Why it works.** Most of our clinicians are paid per visit, so an unpredictable schedule is an
unpredictable paycheck. A study of 3,716 home health nurses found that those with the most erratic
week-to-week visit counts were markedly more likely to quit, and that steadying it cut the chance of
leaving by nine percentage points. The effect only appeared in full-time staff, which fits: it is
people who depend on the income who leave over it.

**Where it bites hardest.** The first year, when a new clinician is slower, does not know the
territory, and is deciding whether the job pays what they were told it would.

---

## 7. Less driving

**What happens.** Clinicians drive fewer miles, because the day is grouped sensibly and territories
follow real drive times rather than lines on a map.

**One caveat worth being straight about.** With most clinicians paid per visit, the time saved
belongs to them, not to us. What we save is the mileage we reimburse. The time they get back turns
into capacity, which is counted in lever one, not here. Counting it twice would be the easiest
mistake to make in this whole case.

---

## Three we believe in but have not priced

**Easier to recruit clinicians.** Two reasons. Clinicians currently spend around half an hour every
evening, unpaid, calling tomorrow's patients to confirm; that goes away. And a recruit who is quoted
an expected income is far more likely to actually earn it when their week is protected and a
canceled visit gets replaced. We have left it unpriced because we do not yet track how long a
vacancy takes to fill or what a hire costs us.

**The same approach applied to hospice.** The workbook already notes hospice needs a few added rules
rather than a different product. It would roughly double what this is worth at little extra cost.

**Care we deliver and cannot bill.** Insurers allow only a short window to backdate an approval, and
care delivered outside it is written off. Nobody counts this today. It could be immaterial or it
could be the largest item on this page, and it is the first thing worth measuring.

---

## The one framing that ties it together

Capacity is perishable. A clinician's open slot is not inventory we can hold; it either gets used
that day or it is gone. Most of the value here is not about working faster. It is about being able
to answer, quickly and reliably, the question of what should go into an empty slot before the slot
stops existing.

---

# Part two: the data we need to request

Grouped by where it lives, so this can go out as requests to the right owners.

## The five that matter most and are quick

These are reports against systems we already have. Together they support five of the seven levers.
This is a two-week ask, not a project.

| What we need | Where it lives | Why we need it |
|---|---|---|
| Ninety days of scheduler task records, with start and finish times, grouped by task type | Patient record system | Turns "scheduling takes fewer people" from an assertion into a counted number |
| How clinicians are paid, split between per visit, hourly and salary, by branch | Payroll | Confirms the seventy percent figure and finds the exceptions. Several levers change size depending on this |
| Visit counts by discipline for twelve months | Patient record system | Shows how much work already sits with assistants and aides, which tells us whether there is headroom left |
| Agency, contract, per diem and overtime spend for twelve months, by branch | Payroll or finance | The starting point for the premium labor lever |
| Who left, when, and how long they had been here, for twenty-four months | Human resources system | Our real turnover rate. The current assumption implies thirteen percent; published home health nursing turnover is twenty-five to twenty-eight |

## Admissions and speed

| What we need | Where it lives | Why we need it |
|---|---|---|
| New patient starts per year, by branch | Patient record system | This is the number the largest lever multiplies against, and our current figure does not reconcile with our revenue |
| Timestamps from referral to first visit: accepted, insurance verified, approved, patient called, visit scheduled, visit delivered | Referral system and patient record system | Shows where the days actually go between saying yes and starting care |
| Referrals declined for lack of capacity, with a reason | Referral log | Sizes the demand we are turning away. This likely needs a reason code we do not have yet |

## Cancellations and lost slots

| What we need | Where it lives | Why we need it |
|---|---|---|
| Canceled and missed visits: how many, when they were canceled relative to the visit, and the reason | Patient record system | The starting point for lever two |
| Of those, how many left a gap in the clinician's day that was never filled | Patient record system | This is the actual loss. It is the number nobody has |
| How long it takes from a cancellation to a replacement visit being assigned, when one is | Patient record system | Tells us whether we are slow or simply unable |
| How often a visit is moved earlier in the week to cover a gap | Patient record system | Shows whether branches are already doing this by hand, and how well it works |
| Which visit types are genuinely flexible on timing | Clinical leadership | The system cannot move visits safely without this |

## Medicare periods

| What we need | Where it lives | Why we need it |
|---|---|---|
| How often 30-day periods end below the visit threshold, and by how many visits | Billing | Our real rate rather than the national one |
| For those that missed by one visit, whether a visit was missed, moved, or held for approval | Billing and patient record system | Separates the ones we could have prevented from the ones we could not |
| What a 30-day period costs us to deliver, by patient type | Finance | Without this we can describe the direction but not the size |

## Workforce

| What we need | Where it lives | Why we need it |
|---|---|---|
| Each clinician's visit count by week for twelve months | Patient record system | Lets us calculate how steady each person's week is, which predicts who is likely to resign |
| Pay quoted at hire against pay actually earned in the first ninety days | Payroll and recruiting | The clearest measure of whether new hires earn what they were told they would |
| Miles and drive time per visit, by branch | Patient record system or expenses | Replaces a placeholder figure we made up |
| How long vacancies take to fill, and how often offers are accepted | Human resources system | Needed later, for the recruiting argument |
| Reasons people give for leaving, coded consistently | Human resources system | Separates schedule and income causes from everything else |

## Insurance and approvals

| What we need | Where it lives | Why we need it |
|---|---|---|
| Visits delivered that we could not bill because approval came too late | Billing | Possibly the largest unmeasured item in the whole case |
| Days from our approval request to the insurer's answer, by insurer | Authorization team | Never been measured. It sits upstream of everything scheduling does |
| Visits sitting unscheduled while waiting on approval, at a point in time | Patient record system | Work we have accepted and cannot yet do, which today appears on no report |

---

## What to say if asked why we need all this

Every number in the business case is one of three things: measured, published, or assumed. Today too
many are assumed. This list is what turns the assumed ones into measured ones, and most of it is
already sitting in systems we own.
