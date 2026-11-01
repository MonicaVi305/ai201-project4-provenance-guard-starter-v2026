# Acceptance criteria — Provenance Guard

Five criteria that say what "working" means for this service, written in unit 7
**before** you built it.

**All five are yours.** None are given.

An acceptance criterion names a number or something plainly observable. *"The
detector is accurate"* is an opinion — and perfect AI detection isn't possible
anyway, so it's an opinion about something nobody can deliver. *"Of 10 pieces I
wrote myself, at most 1 is labelled high-confidence AI"* is a criterion.

Under each, write a sentence or two on **why that target**. *"I allow at most 1
false positive in 10 because on a writing site a wrong accusation costs more
than a missed detection"* is a real answer.

> Missing your own targets next unit costs you nothing. Setting a target so
> easy you can't miss it does.
---

## Pick numbers you can defend

**Cover at least three of these five areas.** They're prompts, not a form.

| Area | A question it could answer |
|---|---|
| False positives | How often may a human's writing get called AI? |
| Score spread | How far apart should clearly-AI and clearly-human text score? |
| Label coverage | Is every one of your three labels actually reachable? |
| The appeal path | Does an appeal always change status and always get recorded? |
| Bad input | What happens when `text` is missing, empty, or enormous? |

Two things worth knowing before you pick numbers:

- **The expensive mistake is one-sided.** Missing some AI text costs the site a
  little. Accusing a real writer costs that person a lot. A criterion that
  treats both errors as equally bad is describing a system nobody would ship.
- **Unit 8 tests across three trials, and the target has to hold across all
  three.** Your first signal runs a model, so identical input can score
  differently twice. A target of "at most 1 in 10" against trials of 2, 1, 2 is
  a **miss**.

---
## 1.

<!-- Your criterion. It must name a number. -->
False positives: of 30 human-written texts, at most 1 (5%) is labeled high-confidence AI, and this holds in each of the three trials.

**Why this target:**

Calling a person’s real writing AI-made is the worst mistake this tool can make, because that person can get blamed for something they didn’t do. So this limit is the tightest. I didn’t pick 0% because with 30 test texts one odd case would fail the whole criterion. 5% allows about one mistake and no more.

---

## 2.

<!-- Your criterion. -->
Score spread: across 10 clearly human and 10 clearly AI texts, the average combined scores are at least 0.40 apart, and the highest-scoring human text scores below the lowest-scoring AI text (no overlap). Both must hold.


**Why this target:**
On a 0 to 1 scale, 0.40 is almost half the range. If clearly human texts average around 0.3 and clearly AI texts around 0.7, there’s room in the middle for an uncertain zone. If the gap is small, a tiny change in wording could flip a label. The no-overlap rule matters because averages can hide trouble: two groups can be far apart on average while some texts from each group still mix together.

---

## 3.

<!-- Your criterion. -->
Label coverage: on a test set of 30 texts (10 clearly human, 10 clearly AI, 10 borderline), all three labels appear at least once, and no single label takes more than 70% (21 of 30) of the results.


**Why this target:**
“At least once” checks that each label can actually be produced, because a label that never appears means the thresholds (0.35 and 0.65) leave a gap or sit in the wrong place. The 70% cap is an estimate, not a measured number. I will test on a set with a roughly even mix of clearly human, clearly AI and borderline text, so an even split would put each label near one third. One label taking 70% or more is more than double that share, which tells me the system is pushing nearly everything one way (for example, calling most text “unsure” because the style signal is stuck near 0.5) instead of telling the texts apart. If I miss this in testing, I will diagnose why and keep this number as written.

---

## 4.

<!-- Your criterion. -->
The appeal path: every appeal moves the status to under_review and saves a log entry (visible in the audit log via GET /log), in 10 out of 10 test appeals.


**Why this target:**

This one is about the code, not the model, so the target is 100%. A model’s guesses can be a little wrong, but an appeal that doesn’t get recorded is simply a bug, and someone loses their only way to challenge a result. I used 10 test appeals as enough runs to cover the usual cases (different labels, different reasons) without too much work.
---

## 5.

<!-- Your criterion. -->

Bad input: missing or empty text returns HTTP 400, text over 20,000 characters returns HTTP 413, and text too short for the model returns HTTP 422. Each response has an error message and no model_score or combined_score field, and the server keeps running afterward.

**Why this target:**
This is also a code rule, so the target is “every time.” Empty or missing text has nothing to judge, so any score would be made up. Text over 20,000 characters is rejected openly instead of cut off quietly, because judging only part of a text without saying so could give a wrong label nobody can explain. I chose 20,000 characters as a generous upper limit for one submission. The model only reads the first 400 tokens either way, so the limit mostly protects the service from huge requests.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     UNIT 8 — read this before you change anything above.

     If a criterion turns out to be BROKEN rather than merely unmet, you can
     revise it, and that earns credit. But never delete or edit the original
     line. Add the revision underneath, like this:

         ## 2. Uncertain cases land in the unsure band

         The system handles uncertain cases well.

         **Why this target:** ...

         > **Revised in unit 8:** Text I judged borderline scores between
         > 0.4 and 0.6 in at least 4 of 5 cases.
         >
         > **Why revised:** "well" gave me nothing to check. I couldn't
         > reach a verdict from it at all.

     That's a revision because the criterion couldn't be MEASURED.

     Lowering a target because you missed it is not a revision, and it costs
     you the point:

         ✗ "At most 1 of 10 of my own pieces flagged as AI" → "at most 3
            of 10", because 1 of 10 turned out to be hard.

     A number you missed stays where it is, gets diagnosed, and gets a fix
     attempted. That's where the points are.
     ───────────────────────────────────────────────────────────────────────── -->
