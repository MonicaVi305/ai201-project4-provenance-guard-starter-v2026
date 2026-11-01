# Provenance Guard

> ### 👋 Start here
>
> **New to this repo? Read [RUNNING.md](RUNNING.md) first.**
>
> Once `python test.py` passes, in one terminal:
>
> ```bash
> python app.py
> ```
>
> and in another:
>
> ```bash
> curl -X POST http://127.0.0.1:5000/ping \
>   -H "Content-Type: application/json" \
>   -d '{"message": "hello"}'
> ```
>
> That's a web service. Something sent it text and it sent something back.
> Everything this unit is filling in the middle.
>
> **The rest of this file is your submission.** Fill it in as you go.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     Unit 7 asks for the first five sections. Unit 8 adds the five below.

     Everything is pasted as TEXT. A pasted curl response gets full credit;
     a picture of your terminal gets none.
     ───────────────────────────────────────────────────────────────────────── -->

<!-- ═══════════════════════ UNIT 7 — THE BUILD ═══════════════════════ -->

## What This Does

<!-- The path a submission takes, from arriving to the label a reader sees.
     Six or seven steps — this is the trace you wrote in Milestone 1. -->

1. A client sends `POST /submit` with JSON containing the text and a `creator_id`.
2. The route extracts and validates those fields (400 for missing or empty, 413 over 20,000 characters, 422 too short for the model).
3. `detector.model_signal(text)` runs local GPT-2, measures perplexity, and maps predictability to a 0–1 score; higher means more AI-like. It considers at most 400 tokens.
4. `stylometry.style_signal(text)` measures sentence-length variation, vocabulary repetition, and punctuation density, then returns a 0–1 score in the same direction (higher means more AI-like).
5. `scoring.combine_signals(model_score, style_score)` combines the scores. The rule is an equal-weight average, pulled back toward 0.5 when the two signals disagree by more than 0.35 (see The combining rule).
6. `scoring.score_to_label(combined_score)` maps scores to a guess and reader-facing label: `<= 0.35` human, `> 0.35` and `< 0.65` unsure, `>= 0.65` AI. The label text lives in `scoring.py` (see Label Variants).
7. The route creates a UUID `content_id`, appends the decision and its scores to the audit log, and returns the decision and identifiers as JSON. 

---

## Signals and Scoring

<!-- For each signal: what property it measures, why that might differ between
     human and AI writing, and WHAT IT CAN'T SEE.

     The blind spot is not optional. If you can't name it you don't understand
     the signal yet — and unit 8's attack set is built out of blind spots. -->

### Signal one — the model signal

**What it measures:** How predictable the text is to a local GPT-2 language model. It calculates perplexity and squashes it into a 0–1 score, with lower perplexity producing a higher AI-likelihood score.

**Why that might differ between human and AI writing:** A language model tends to select likely next words, so its own writing may be easy for a similar model to predict. Human writing can be less predictable because of unusual wording, abrupt shifts, or specific details.

**What it can't see:** It cannot establish authorship or understand why a phrase was chosen. Plain, conventional human writing can be predictable and score as AI-like; unusual or ornate AI writing can score as human-like. Topic, length, and the model used also affect the score.

### Signal two — the style signal

**What it measures:** Surface form rather than meaning: sentence-length spread, type-token ratio (unique words divided by total words), and punctuation density. Each measure is flipped so that higher means more AI-like, clipped to 0–1, then averaged with weights spread 0.5, vocabulary 0.25, punctuation 0.25. Punctuation counts expressive marks only (semicolons, colons, dashes, brackets, `!`, `?`, quotes), not commas or full stops. Type-token ratio is measured on the first 100 words so long and short texts compare fairly. The cut-offs that map each measure onto 0–1 are estimates from my hand-picked examples, not fitted values.

**Why that might differ between human and AI writing:** Generated prose can have more even sentence lengths, repeated vocabulary, and conventional punctuation. Human prose may vary more, though these are tendencies rather than reliable authorship rules.

**What it can't see:** It cannot read meaning, verify who wrote the text, or distinguish genuine stylistic variation from edits. Typos, sentence splitting, quotations, or punctuation changes can move the measurements without changing authorship. Type-token ratio also depends on text length. In my calibration run it was also fooled in the other direction: AI text written with short and long sentences, brackets and a question mark scored `0.03` on style.

### The combining rule

<!-- Write the rule in words, then give the numbers. What happens when the two
     signals disagree? -->

**The rule:** Take the equal-weight average of the two signals. If the signals disagree by more than 0.35, pull that average halfway back toward 0.5, so two methods contradicting each other lands in "unsure" instead of letting one of them accuse or clear a writer alone. The 0.35 gap and the one-half pull are my estimates, not fitted values; they sit in `config.py` as `SPLIT_GAP` and `SPLIT_SHRINK`.

**The numbers:** `avg = 0.5 * model_score + 0.5 * style_score`. If `abs(model_score - style_score) > 0.35` then `combined_score = 0.5 + (avg - 0.5) * 0.5`, otherwise `combined_score = avg`. Weights `WEIGHT_MODEL_SIGNAL` and `WEIGHT_STYLE_SIGNAL` are both 0.5 in `config.py`.

**Where it lives:** `scoring.py::combine_signals`

<!-- ⚠️ The grader checks your code against that line. If your rule lives
     somewhere else, say where. -->

**A case where my two signals split, and what my rule does with it:** An AI-style paragraph written with short punchy sentences, a question mark and brackets ("Honestly? Nobody warns you about this part...") scored `0.614` on the model signal but `0.027` on the style signal, a gap of `0.59`. A plain average would give `0.32`, a confident "human" for AI text. The split rule pulls it to `0.410`, which is "unsure". The style signal is the one that is wrong here, because it only sees the shape of the text, and shape is easy to change.

**Calibration run** (both signals run on the same texts, then through the rule; texts were written for this test):

| Input | Model | Style | Combined | Guess |
|---|---|---|---|---|
| clearly AI | 0.788 | 0.750 | 0.769 | ai |
| clearly human (vivid, personal) | 0.323 | 0.114 | 0.218 | human |
| plain, conventional human | 0.744 | 0.665 | 0.705 | **ai** |
| formal human | 0.443 | 0.578 | 0.510 | unsure |
| lightly edited AI | 0.614 | 0.764 | 0.689 | ai |
| plain, varied-sentence human | 0.469 | 0.257 | 0.363 | unsure |
| AI with varied style (the split case) | 0.614 | 0.027 | 0.410 | unsure |
| ornate AI | 0.544 | 0.620 | 0.582 | unsure |

Clearly AI and clearly human land `0.55` apart (0.769 against 0.218). Lightly edited AI is still caught. The formal human text is "unsure", not accused. The row to worry about is the plain, conventional human text: **both signals read it as AI-like**, so the average agrees with them and the split rule never fires. That is a false positive this design cannot fix by re-weighting; it needs a better signal, or a wider unsure band, which I have not done.

### False-positive trace

A real writer uses plain, conventional language. In my calibration run, an ordinary paragraph about working from home (every sentence of similar length, no unusual punctuation) scored `0.744` on the model signal and `0.665` on the style signal, so the combined score was `0.705` and the guess was `ai`. Because both signals agree, the split rule does not rescue it. The writer would see the high-confidence AI label from Label Variants: “This may have been written with AI. This is our best guess, not proof, and we can get it wrong. If you wrote it yourself, you can appeal and ask a person to take another look.” The writer can submit `POST /appeal` with the returned `content_id` and an explanation; the service records an append-only appeal and marks the item `under_review`.

### Endpoint contracts

`POST /submit` accepts `Content-Type: application/json` with these fields:

| Field | Type | Meaning |
|---|---|---|
| `text` | string | Text to score; required, non-empty, and at most 20,000 characters. Fewer than three model tokens cannot be scored. |
| `creator_id` | string | Identifier used to associate the submission and any appeal with its creator. |

On success, return HTTP 200 with JSON:

| Field | Type | Meaning |
|---|---|---|
| `content_id` | string | UUID for this submission; required to appeal. |
| `guess` | string | Machine-readable value: `human`, `unsure`, or `ai`. |
| `label` | string | Reader-facing explanation of the classification. |
| `reasoning` | string | Short explanation based on the combined and component scores; not a claim of proof. |
| `model_score` | number | Model signal from 0 to 1; higher means more AI-like. |
| `style_score` | number | Style signal from 0 to 1; higher means more AI-like. |
| `combined_score` | number | Score used for the thresholds, from 0 to 1. |
| `confidence` | number | Alias of `combined_score` for compatibility with the starter's draft response; it means AI-likelihood, not certainty of authorship. |

Invalid JSON, missing fields, or empty text should return HTTP 400 with `{"error": "invalid_request", "message": "..."}`. Text too short for the model should return HTTP 422 with `{"error": "text_too_short", "message": "..."}`. Text over 20,000 characters should return HTTP 413 with `{"error": "text_too_large", "message": "..."}`. The model still truncates accepted text at 400 tokens; the style signal sees the full accepted text.

`POST /appeal` accepts `Content-Type: application/json` with:

| Field | Type | Meaning |
|---|---|---|
| `content_id` | string | ID returned by `/submit`; must identify an existing decision. |
| `reasoning` | string | Writer's explanation of why the decision should be reviewed. |

On success, return HTTP 200 with `{"ok": true, "content_id": "...", "status": "under_review"}`. Append an appeal event to the audit log without replacing the original decision. Missing fields should return HTTP 400; an unknown `content_id` should return HTTP 404. The route must look up the original decision to obtain its `creator_id` for `audit.log_appeal`.

**Contract clarification:** The starter mentions `confidence` but does not define it, and its example response omits `combined_score`. This contract makes `confidence` an explicit alias and also returns the named score used by the label thresholds, so clients can interpret the result without reverse-engineering the log.



---

## Label Variants

<!-- The exact text of all three labels, as a reader would see them, and the
     score range each covers.

     Write them for someone who has never heard the word "threshold". -->

| Label | Score range | The exact text a reader sees |
|---|---|---|
| high-confidence human | 0.00 – 0.35 | We think this was probably written by a person. This is an estimate, not a guarantee. |
| unsure | 0.35 – 0.65 | We can't tell whether this was written by a person or by AI. That is not a judgment about you or your work. Our checks just didn't point clearly one way. If you'd like a person to look at it, you can ask for a review. |
| high-confidence AI | 0.65 – 1.00 | This may have been written with AI. This is our best guess, not proof, and we can get it wrong. If you wrote it yourself, you can appeal and ask a person to take another look. |

All three are reachable: in testing, a vivid human text scored `0.218` (human), a formal human text `0.510` (unsure), and a clearly AI text `0.769` (AI). The boundaries are inclusive (`<= 0.35` is human, `>= 0.65` is AI), matching `scoring.py`.

**Why I worded the "unsure" one this way:**
The person reading it may have written every word, so it opens with what we can't tell, then says outright that this is not a judgment about them or their work, and puts the doubt on our checks rather than on the writer. It ends with an offer of a human review so "unsure" is never a dead end. I avoided the words "score", "threshold" and "confidence".

---

## Sample Run

<!-- One submission and one appeal, pasted as text: the request, the response,
     and the log entries. -->

**A submission**

<!-- The response needs content_id, guess, confidence, label, AND both
     signal scores - model_score and style_score. Unit 8's tools read those
     two off the response, so leaving them out costs you next unit's
     diagnostics. -->

```bash
$ curl.exe -X POST http://127.0.0.1:5055/submit -H "Content-Type: application/json" -d '{"text": "In today'"'"'s fast-paced digital landscape, effective communication plays a crucial role in organizational success. Furthermore, leveraging innovative solutions can significantly enhance productivity and foster collaboration across diverse teams. ...", "creator_id": "m5-clearly_ai"}'
```

```json
{
  "combined_score": 0.7692,
  "confidence": 0.7692,
  "content_id": "9d521991-f082-4bf5-9f0b-3de3df5c8807",
  "guess": "ai",
  "label": "This may have been written with AI. This is our best guess, not proof, and we can get it wrong. If you wrote it yourself, you can appeal and ask a person to take another look.",
  "model_score": 0.7885,
  "reasoning": "Model signal 0.7885, style signal 0.75, combined 0.7692 (higher means more AI-like).",
  "style_score": 0.75
}
```

(The text is shortened above; the real request sent the full paragraph from my calibration set. Bad input returns 400, 413 or 422 as in the endpoint contract.)

**An appeal**

```bash
$ curl.exe -X POST http://127.0.0.1:5055/appeal -H "Content-Type: application/json" -d '{"content_id": "9d521991-f082-4bf5-9f0b-3de3df5c8807", "reasoning": "I wrote this myself for a marketing class. I tend to write in a formal style."}'
```

```json
{"content_id": "9d521991-f082-4bf5-9f0b-3de3df5c8807", "ok": true, "status": "under_review"}
```

An unknown `content_id` returns `{"error": "not_found", ...}` with HTTP 404, and a missing `reasoning` returns HTTP 400.

**What the log shows afterwards**

```bash
$ curl.exe "http://127.0.0.1:5055/log?limit=2"
```

```json
{
  "count": 2,
  "entries": [
    {"timestamp": "2026-11-01T21:31:05+00:00", "content_id": "9d521991-f082-4bf5-9f0b-3de3df5c8807", "creator_id": "m5-clearly_ai", "guess": "ai", "model_score": 0.7885, "style_score": 0.75, "combined_score": 0.7692, "label": "This may have been written with AI. This is our best guess, not proof, and we can get it wrong. If you wrote it yourself, you can appeal and ask a person to take another look.", "status": "decided"},
    {"timestamp": "2026-11-01T21:31:10+00:00", "content_id": "9d521991-f082-4bf5-9f0b-3de3df5c8807", "creator_id": "m5-clearly_ai", "event": "appeal", "status": "under_review", "reasoning": "I wrote this myself for a marketing class. I tend to write in a formal style."}
  ]
}
```

The log is append-only: the original decision stays as `decided` and the appeal sits after it with status `under_review`.

---

## How I Used AI

**Moment 1**

- *What I asked for:* A review of my five acceptance criteria in `criteria.md` (Milestone 2): could someone who couldn't ask me what I meant check each one? I wrote the criteria myself and did not ask for them to be written.
- *What came back:* Criterion 4 (appeals) was checkable. Criteria 1, 2, 3 and 5 were not: no sample size or trial rule on the false-positive number, two different pass conditions in the score-spread one, no named test set for label coverage, and "a clear error message" instead of status codes. When I filled in my reasons, it also flagged two that were not mine: reason 3 cited results from "your trained model" that I never had, and reason 5 said the 10,000-word limit "is only an example", which contradicted my 20,000-character limit.
- *What I changed:* Criterion 1 now says 30 texts, at most 1 flagged, in each of three trials. Criterion 2 needs both a 0.40 gap and no overlap, across 10 texts per group. Criterion 3 names a 30-text set. Criterion 5 lists 400, 413 and 422 and the 20,000-character limit. I replaced the reason for 3 with an honest "70% is an estimate" and the reason for 5 with the real limit.

**Moment 2**

- *What I asked for:* The second signal and the combining rule for Milestone 4, run on clearly AI, clearly human, formal human and lightly edited AI text.
- *What came back:* Three style measures (sentence-length spread, vocabulary variety, expressive punctuation) and a rule that averages the signals and pulls the result halfway toward 0.5 when they disagree by more than 0.35, with a table of eight test texts. It also reported that a plain, ordinary human paragraph scored 0.71 and was labeled AI because both signals agreed, so no reweighting could fix it.
- *What I changed:* I read the table and the split case myself and kept the rule and the 0.35 and 0.65 thresholds as proposed. I chose not to widen the unsure band, so the plain-human false positive (0.71, labeled AI) is still there and is written up in the False-positive trace instead of being hidden by a looser threshold.

<!-- ═══════════════════════ UNIT 8 — THE TEST ═══════════════════════ -->

---

## Rate Limiting

**My limits:** ___ per minute, ___ per day

**Why those numbers and not others:**
<!-- Think about two people: a real writer submitting their own work a few
     times an hour, and a script sending a thousand variations to map your
     thresholds. Your numbers have to be liveable for the first and hostile to
     the second. -->

**What a caller counts as:** <!-- per address, or per creator_id? They fail
differently — one script can look like a thousand callers, and one household
can look like one. -->

**The run of status codes when I pushed past it:**

<!-- python run_attacks.py --flood 15 -->

```

```

---

## Attack Run — Before

<!-- Every attack with its outcome and a held-or-broke mark.
     `run_attacks.py --label before` produces the table. -->



**Ten audit log entries from the run**

<!-- Choose entries that show the interesting failures, not the ten easiest. -->

```json

```

**The single worst outcome** — the one I'd least want to explain to a writer
whose work got caught by it:



---

## Run Log and Verdicts

<!-- Your five criteria across three trials. `run_eval.py --label before`. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1.  |  |  |  |  |  |
| 2.  |  |  |  |  |  |
| 3.  |  |  |  |  |  |
| 4.  |  |  |  |  |  |
| 5.  |  |  |  |  |  |

**Real output from one trial**, pasted as text, naming the file and function
that produced it:

```json

```

**Diagnoses**

<!-- For each miss AND each broken attack: the stage and the mechanism.

     Your service has five stages: the route, signal one, signal two, the
     combining rule, and the label mapping.

     Not a diagnosis:  "The evasion attacks got through."
     A diagnosis:      "Four evasion inputs got through. All four had typos
                        added to AI-generated text. My second signal measures
                        word variety, and typos raise word variety — so it read
                        them as more human. My combining rule weights that
                        signal at 0.6, so it dragged the whole score down."

     Look for a pattern. Five failures on one signal is one problem, not five. -->



---

## The Improvement

**What I changed:**

**Which diagnosis pointed at it:**

### Attack Run — After

<!-- Same format. `run_attacks.py --label after` -->



**Did it help, and how do I know:**

<!-- Widening the unsure band usually fixes one problem and creates another.
     Reporting that trade honestly is worth full credit. -->



---

## What's Still Broken

<!-- For each attack still getting through and each criterion still missed:
     what you'd do, and why you stopped. -->



**The trade I'd make if this ran for real:**

<!-- Two sentences. Fewer wrong accusations means more AI text getting through.
     Say which way you'd go and WHO PAYS FOR IT. -->



<!-- ═════════════════════════════════════════════════════════════════════

     SUBMISSION CHECKLIST — unit 7

       [ ] criteria.md has five numbered criteria, each naming a target
       [ ] Each has a reason underneath
       [ ] POST /submit returns content_id, guess, confidence, label,
           model_score and style_score
       [ ] Two signals that measure DIFFERENT things, each with a named blind spot
       [ ] Three label variants, all reachable, written out in full
       [ ] POST /appeal changes status and writes to the log
       [ ] Signals and Scoring names scoring.py::combine_signals
       [ ] Sample Run: a submission AND an appeal, as pasted text
       [ ] At least four new commits
       [ ] Repository URL submitted — WRITE IT DOWN

     SUBMISSION CHECKLIST — unit 8

       [ ] Rate limiting on /submit, with your numbers justified
       [ ] The pasted run of status codes showing 429
       [ ] Audit log with all nine fields, recording rejections too
       [ ] The attack set run IN FULL, every input with an outcome
       [ ] Ten audit log entries pasted as text
       [ ] Five criteria across three trials
       [ ] A diagnosis for every miss and every broken attack — stage AND mechanism
       [ ] One improvement, with Attack Run — After
       [ ] What's Still Broken, including the production trade
       [ ] At least four new commits
       [ ] The SAME repository URL as last unit

     Do not delete and recreate this repository.
     ═════════════════════════════════════════════════════════════════════ -->

---

📖 **How to run this project: [RUNNING.md](RUNNING.md)**
