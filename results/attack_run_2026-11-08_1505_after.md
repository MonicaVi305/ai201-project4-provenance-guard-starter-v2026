# Attack run — after

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-08 15:05
- Auto-marked BROKE (5xx, crash, no response): **0**
- Left for you to judge: **56**

The Verdict column is blank where a script can't honestly decide. Whether
an evasion worked depends on where you put your thresholds — read the
`targets` column, look at what came back, and write HELD or BROKE yourself.

Each attack submits as creator_id `attacker_<id>`, and the content_id it
came back with is in the table — either one will match this run against your
audit log when you go looking for the ten entries to paste.

| ID | Family | Targeting | Status | Content ID | Guess | Score | Verdict |
|---|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | `46ca419d-fa1c-4098-8a53-e0cfaa5af6be` | unsure | 0.478 |  |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `1fe4b636-d007-4096-b41e-18d90bf63d6b` | unsure | 0.435 |  |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `ccd1d89b-1b18-45e0-92f1-b52f7331772b` | unsure | 0.528 |  |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `92c68e6a-40c9-4572-bc42-d7ea4ff382d7` | unsure | 0.681 |  |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `bd4e6509-dcd7-4a8b-922a-13faa7ed3067` | human | 0.282 |  |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `a5b796df-a6a7-4ca6-ad18-17ec655c50b5` | unsure | 0.436 |  |
| EV07 | evasion | signal two: padding with punctuation | 200 | `77b93486-666a-4a9d-9c0e-0f3e0cb463d5` | unsure | 0.444 |  |
| EV08 | evasion | signal one: text below the token window | 200 | `faf68096-7a5b-4ff3-ac52-a4b3b38e6f90` | unsure | 0.488 |  |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `7e0da3c8-db52-443a-8211-49d1936848b5` | unsure | 0.591 |  |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `e625e7ac-a184-4c54-a4de-9a66b3c9cde6` | ai | 0.900 |  |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `1d3558e7-a47c-4f31-8f85-74486b42377c` | unsure | 0.604 |  |
| FP02 | false_positive | human writing in a formal register | 200 | `3da6cd5c-e585-446c-8b64-e0eef23e0b72` | unsure | 0.789 |  |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `f4a23ece-995b-4c17-abc7-0509d495381d` | unsure | 0.767 |  |
| FP04 | false_positive | a student essay written to a rubric | 200 | `1024ef8f-a69a-4b3d-b165-7620c314b89c` | unsure | 0.719 |  |
| FP05 | false_positive | technical documentation written by a person | 200 | `95125930-87ac-4b81-94ae-38f8679cf65b` | ai | 0.866 |  |
| FP06 | false_positive | a person imitating a formal template | 200 | `b052d6fe-3521-45b0-91e9-fabf0eccd1ce` | unsure | 0.590 |  |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `deb607d6-edb2-483a-8489-fe464c36754b` | unsure | 0.595 |  |
| FP08 | false_positive | very short genuine human submission | 200 | `e9b47e9e-0dfa-4d94-ae40-53e44933039b` | unsure | 0.422 |  |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `e3c613c1-b971-426e-84ba-88464a7aa2a8` | unsure | 0.356 |  |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `fe6ee6c4-d159-4fb6-9177-4787997f69ff` | human | 0.193 |  |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `8f16c37b-f951-4cea-be8a-6cd70c2e568b` | unsure | 0.529 |  |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `b2f2e4d3-401a-4656-8344-a5e18ad1c235` | unsure | 0.472 |  |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `7f74078d-1221-4b7a-936c-357ee2361b42` | unsure | 0.466 |  |
| PI06 | prompt_injection | instruction plus real human text | 200 | `bbc7c2ca-a656-4486-aecf-33f96d7db0e4` | unsure | 0.567 |  |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — |  |
| MF02 | malformed | text is a single character | 422 | `—` | — | — |  |
| MF03 | malformed | text is control characters | 200 | `734803a0-968c-4fdc-bc4e-3cba4865bcda` | unsure | 0.375 |  |
| MF04 | malformed | text is only punctuation | 200 | `6a0c204e-6c59-4bec-88d1-976d81d1eeb2` | unsure | 0.503 |  |
| MF05 | malformed | text is a very long single word | 200 | `c36388cc-0563-4f0c-897d-96712743e5b7` | unsure | 0.624 |  |
| MF06 | malformed | text is emoji only | 200 | `d7784bb0-87ef-460a-8314-9cbb9ba06c23` | ai | 0.874 |  |
| MF07 | malformed | text is right-to-left script | 200 | `55de47e1-88c4-47f3-9839-e8cd228e8032` | ai | 0.828 |  |
| MF08 | malformed | text is 60,000 characters | 413 | `—` | — | — |  |
| RQ01 | malformed | no text field at all | 400 | `—` | — | — |  |
| RQ02 | malformed | no creator_id | 400 | `—` | — | — |  |
| RQ03 | malformed | text is a number | 400 | `—` | — | — |  |
| RQ04 | malformed | text is a list | 400 | `—` | — | — |  |
| RQ05 | malformed | text is null | 400 | `—` | — | — |  |
| RQ06 | malformed | creator_id is an object | 400 | `—` | — | — |  |
| RQ07 | malformed | body is a JSON array, not an object | 400 | `—` | — | — |  |
| RQ08 | malformed | body is unparseable JSON | 400 | `—` | — | — |  |
| RQ09 | malformed | body is empty | 400 | `—` | — | — |  |
| RQ10 | malformed | body is form-encoded, not JSON | 400 | `—` | — | — |  |
| RQ11 | malformed | body is JSON claiming to be plain text | 400 | `—` | — | — |  |
| RQ12 | malformed | deeply nested JSON | 400 | `—` | — | — |  |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `cbbb0a31-94f0-4fe7-91c5-77514512b3e1` | unsure | 0.382 |  |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `1591bd9b-13b0-4896-b701-97455ac31964` | unsure | 0.382 |  |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `5f4ab2fe-4deb-4969-b853-ee662a546cef` | unsure | 0.382 |  |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `632f0dc0-bca2-4dff-86f2-3715d7331005` | unsure | 0.382 |  |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `d17291a3-544a-454e-bc84-b554284c29f5` | unsure | 0.382 |  |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 200 | `7f3ed7a5-c925-40e1-9091-7a580da31bf0` | unsure | 0.382 |  |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 200 | `df4628cb-23d1-4c53-8cf6-631e51979e45` | unsure | 0.382 |  |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 200 | `bfbb1240-2712-479f-ad9f-a26c4f53b907` | unsure | 0.382 |  |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 200 | `3130768d-42e7-4166-94c9-2190c63ab446` | unsure | 0.382 |  |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 200 | `773e569a-d19c-4f17-bf08-4557cda56492` | unsure | 0.382 |  |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |

---

## By family

| Family | Attacks | Auto-BROKE | Left to judge |
|---|---|---|---|
| `evasion` | 10 | 0 | 10 |
| `false_positive` | 8 | 0 | 8 |
| `flood_same_creator` | 12 | 0 | 12 |
| `malformed` | 20 | 0 | 20 |
| `prompt_injection` | 6 | 0 | 6 |

> The **false_positive** family is the one to look at hardest. Those are
> written to be genuine human writing that reads as machine-like. Every one
> your service calls AI is a real writer it would have accused.

---

## What came back

The detail behind the table. Paste the interesting failures into your
README — the ones that show something, not the ten easiest.

### EV01 — `evasion`

*Targeting:* signal two: typos raise word variety

```json
{
  "id": "EV01",
  "status": 200,
  "content_id": "46ca419d-fa1c-4098-8a53-e0cfaa5af6be",
  "creator_id": "attacker_EV01",
  "guess": "unsure",
  "confidence": 0.4784,
  "model_score": 0.1635,
  "style_score": 0.75,
  "label": "We can't tell whether this was written by a person or by AI. That is not a judgment about you or your work. Our checks just didn't point clearly one way. If you'd like a person to look at it, you can ask for a review.",
  "error": null,
  "verdict": ""
}
```

### EV02 — `evasion`

*Targeting:* signal two: broken-up sentences raise length spread

```json
{
  "id": "EV02",
  "status": 200,
  "content_id": "1fe4b636-d007-4096-b41e-18d90bf63d6b",
  "creator_id": "attacker_EV02",
  "guess": "unsure",
  "confidence": 0.4353,
  "model_score": 0.5943,
  "style_score": 0.147,
  "label": "We can't tell whether this was written by a person or by AI. That is not a judgment about you or your work. Our checks just didn't point clearly one way. If you'd like a person to look at it, you can ask for a review.",
  "error": null,
  "verdict": ""
}
```

### EV03 — `evasion`

*Targeting:* signal two: a pasted quotation changes the shape

```json
{
  "id": "EV03",
  "status": 200,
  "content_id": "ccd1d89b-1b18-45e0-92f1-b52f7331772b",
  "creator_id": "attacker_EV03",
  "guess": "unsure",
  "confidence": 0.5283,
  "model_score": 0.6662,
  "style_score": 0.3904,
  "label": "We can't tell whether this was written by a person or by AI. That is not a judgment about you or your work. Our checks just didn't point clearly one way. If you'd like a person to look at it, you can ask for a review.",
  "error": null,
  "verdict": ""
}
```

### EV04 — `evasion`

*Targeting:* signal one: unusual words raise perplexity

```json
{
  "id": "EV04",
  "status": 200,
  "content_id": "92c68e6a-40c9-4572-bc42-d7ea4ff382d7",
  "creator_id": "attacker_EV04",
  "guess": "unsure",
  "confidence": 0.6807,
  "model_score": 0.6114,
  "style_score": 0.75,
  "label": "We can't tell whether this was written by a person or by AI. That is not a judgment about you or your work. Our checks just didn't point clearly one way. If you'd like a person to look at it, you can ask for a review.",
  "error": null,
  "verdict": ""
}
```

### EV05 — `evasion`

*Targeting:* both signals: heavy human editing pass

```json
{
  "id": "EV05",
  "status": 200,
  "content_id": "bd4e6509-dcd7-4a8b-922a-13faa7ed3067",
  "creator_id": "attacker_EV05",
  "guess": "human",
  "confidence": 0.2824,
  "model_score": 0.3212,
  "style_score": 0.2436,
  "label": "We think this was probably written by a person. This is an estimate, not a guarantee.",
  "error": null,
  "verdict": ""
}
```

### EV06 — `evasion`

*Targeting:* signal two: one very long sentence and one very short

```json
{
  "id": "EV06",
  "status": 200,
  "content_id": "a5b796df-a6a7-4ca6-ad18-17ec655c50b5",
  "creator_id": "attacker_EV06",
  "guess": "unsure",
  "confidence": 0.4364,
  "model_score": 0.5727,
  "style_score": 0.3,
  "label": "We can't tell whether this was written by a person or by AI. That is not a judgment about you or your work. Our checks just didn't point clearly one way. If you'd like a person to look at it, you can ask for a review.",
  "error": null,
  "verdict": ""
}
```

### EV07 — `evasion`

*Targeting:* signal two: padding with punctuation

```json
{
  "id": "EV07",
  "status": 200,
  "content_id": "77b93486-666a-4a9d-9c0e-0f3e0cb463d5",
  "creator_id": "attacker_EV07",
  "guess": "unsure",
  "confidence": 0.4438,
  "model_score": 0.5862,
  "style_score": 0.3013,
  "label": "We can't tell whether this was written by a person or by AI. That is not a judgment about you or your work. Our checks just didn't point clearly one way. If you'd like a person to look at it, you can ask for a review.",
  "error": null,
  "verdict": ""
}
```

### EV08 — `evasion`

*Targeting:* signal one: text below the token window

```json
{
  "id": "EV08",
  "status": 200,
  "content_id": "faf68096-7a5b-4ff3-ac52-a4b3b38e6f90",
  "creator_id": "attacker_EV08",
  "guess": "unsure",
  "confidence": 0.4885,
  "model_score": 0.2452,
  "style_score": 0.7089,
  "label": "We can't tell whether this was written by a person or by AI. That is not a judgment about you or your work. Our checks just didn't point clearly one way. If you'd like a person to look at it, you can ask for a review.",
  "error": null,
  "verdict": ""
}
```

### EV09 — `evasion`

*Targeting:* both: AI text with a human opening paragraph bolted on

```json
{
  "id": "EV09",
  "status": 200,
  "content_id": "7e0da3c8-db52-443a-8211-49d1936848b5",
  "creator_id": "attacker_EV09",
  "guess": "unsure",
  "confidence": 0.5912,
  "model_score": 0.7042,
  "style_score": 0.4781,
  "label": "We can't tell whether this was written by a person or by AI. That is not a judgment about you or your work. Our checks just didn't point clearly one way. If you'd like a person to look at it, you can ask for a review.",
  "error": null,
  "verdict": ""
}
```

### EV10 — `evasion`

*Targeting:* signal two: repeated stanza structure

```json
{
  "id": "EV10",
  "status": 200,
  "content_id": "e625e7ac-a184-4c54-a4de-9a66b3c9cde6",
  "creator_id": "attacker_EV10",
  "guess": "ai",
  "confidence": 0.8997,
  "model_score": 0.9792,
  "style_score": 0.8201,
  "label": "This may have been written with AI. This is our best guess, not proof, and we can get it wrong. If you wrote it yourself, you can appeal and ask a person to take another look.",
  "error": null,
  "verdict": ""
}
```

### FP01 — `false_positive`

*Targeting:* plain, clear human writing with no flourishes

```json
{
  "id": "FP01",
  "status": 200,
  "content_id": "1d3558e7-a47c-4f31-8f85-74486b42377c",
  "creator_id": "attacker_FP01",
  "guess": "unsure",
  "confidence": 0.604,
  "model_score": 0.6175,
  "style_score": 0.5906,
  "label": "We can't tell whether this was written by a person or by AI. That is not a judgment about you or your work. Our checks just didn't point clearly one way. If you'd like a person to look at it, you can ask for a review.",
  "error": null,
  "verdict": ""
}
```

### FP02 — `false_positive`

*Targeting:* human writing in a formal register

```json
{
  "id": "FP02",
  "status": 200,
  "content_id": "3da6cd5c-e585-446c-8b64-e0eef23e0b72",
  "creator_id": "attacker_FP02",
  "guess": "unsure",
  "confidence": 0.7891,
  "model_score": 0.7387,
  "style_score": 0.8395,
  "label": "We can't tell whether this was written by a person or by AI. That is not a judgment about you or your work. Our checks just didn't point clearly one way. If you'd like a person to look at it, you can ask for a review.",
  "error": null,
  "verdict": ""
}
```

### FP03 — `false_positive`

*Targeting:* a non-native English speaker writing carefully

```json
{
  "id": "FP03",
  "status": 200,
  "content_id": "f4a23ece-995b-4c17-abc7-0509d495381d",
  "creator_id": "attacker_FP03",
  "guess": "unsure",
  "confidence": 0.7672,
  "model_score": 0.8051,
  "style_score": 0.7294,
  "label": "We can't tell whether this was written by a person or by AI. That is not a judgment about you or your work. Our checks just didn't point clearly one way. If you'd like a person to look at it, you can ask for a review.",
  "error": null,
  "verdict": ""
}
```

### FP04 — `false_positive`

*Targeting:* a student essay written to a rubric

```json
{
  "id": "FP04",
  "status": 200,
  "content_id": "1024ef8f-a69a-4b3d-b165-7620c314b89c",
  "creator_id": "attacker_FP04",
  "guess": "unsure",
  "confidence": 0.7186,
  "model_score": 0.8329,
  "style_score": 0.6042,
  "label": "We can't tell whether this was written by a person or by AI. That is not a judgment about you or your work. Our checks just didn't point clearly one way. If you'd like a person to look at it, you can ask for a review.",
  "error": null,
  "verdict": ""
}
```

### FP05 — `false_positive`

*Targeting:* technical documentation written by a person

```json
{
  "id": "FP05",
  "status": 200,
  "content_id": "95125930-87ac-4b81-94ae-38f8679cf65b",
  "creator_id": "attacker_FP05",
  "guess": "ai",
  "confidence": 0.8656,
  "model_score": 0.8005,
  "style_score": 0.9307,
  "label": "This may have been written with AI. This is our best guess, not proof, and we can get it wrong. If you wrote it yourself, you can appeal and ask a person to take another look.",
  "error": null,
  "verdict": ""
}
```

### FP06 — `false_positive`

*Targeting:* a person imitating a formal template

```json
{
  "id": "FP06",
  "status": 200,
  "content_id": "b052d6fe-3521-45b0-91e9-fabf0eccd1ce",
  "creator_id": "attacker_FP06",
  "guess": "unsure",
  "confidence": 0.5901,
  "model_score": 0.8814,
  "style_score": 0.4792,
  "label": "We can't tell whether this was written by a person or by AI. That is not a judgment about you or your work. Our checks just didn't point clearly one way. If you'd like a person to look at it, you can ask for a review.",
  "error": null,
  "verdict": ""
}
```

### FP07 — `false_positive`

*Targeting:* human writing that repeats a phrase deliberately

```json
{
  "id": "FP07",
  "status": 200,
  "content_id": "deb607d6-edb2-483a-8489-fe464c36754b",
  "creator_id": "attacker_FP07",
  "guess": "unsure",
  "confidence": 0.5954,
  "model_score": 0.8816,
  "style_score": 0.5,
  "label": "We can't tell whether this was written by a person or by AI. That is not a judgment about you or your work. Our checks just didn't point clearly one way. If you'd like a person to look at it, you can ask for a review.",
  "error": null,
  "verdict": ""
}
```

### FP08 — `false_positive`

*Targeting:* very short genuine human submission

```json
{
  "id": "FP08",
  "status": 200,
  "content_id": "e9b47e9e-0dfa-4d94-ae40-53e44933039b",
  "creator_id": "attacker_FP08",
  "guess": "unsure",
  "confidence": 0.4217,
  "model_score": 0.3223,
  "style_score": 0.5212,
  "label": "We can't tell whether this was written by a person or by AI. That is not a judgment about you or your work. Our checks just didn't point clearly one way. If you'd like a person to look at it, you can ask for a review.",
  "error": null,
  "verdict": ""
}
```

### PI01 — `prompt_injection`

*Targeting:* instruction to ignore the check

```json
{
  "id": "PI01",
  "status": 200,
  "content_id": "e3c613c1-b971-426e-84ba-88464a7aa2a8",
  "creator_id": "attacker_PI01",
  "guess": "unsure",
  "confidence": 0.3563,
  "model_score": 0.4625,
  "style_score": 0.25,
  "label": "We can't tell whether this was written by a person or by AI. That is not a judgment about you or your work. Our checks just didn't point clearly one way. If you'd like a person to look at it, you can ask for a review.",
  "error": null,
  "verdict": ""
}
```

### PI02 — `prompt_injection`

*Targeting:* instruction disguised as a system message

```json
{
  "id": "PI02",
  "status": 200,
  "content_id": "fe6ee6c4-d159-4fb6-9177-4787997f69ff",
  "creator_id": "attacker_PI02",
  "guess": "human",
  "confidence": 0.1925,
  "model_score": 0.2044,
  "style_score": 0.1806,
  "label": "We think this was probably written by a person. This is an estimate, not a guarantee.",
  "error": null,
  "verdict": ""
}
```

### PI03 — `prompt_injection`

*Targeting:* instruction wrapped in the writer's voice

```json
{
  "id": "PI03",
  "status": 200,
  "content_id": "8f16c37b-f951-4cea-be8a-6cd70c2e568b",
  "creator_id": "attacker_PI03",
  "guess": "unsure",
  "confidence": 0.5288,
  "model_score": 0.5943,
  "style_score": 0.4632,
  "label": "We can't tell whether this was written by a person or by AI. That is not a judgment about you or your work. Our checks just didn't point clearly one way. If you'd like a person to look at it, you can ask for a review.",
  "error": null,
  "verdict": ""
}
```

### PI04 — `prompt_injection`

*Targeting:* attempt to make the label text hostile

```json
{
  "id": "PI04",
  "status": 200,
  "content_id": "b2f2e4d3-401a-4656-8344-a5e18ad1c235",
  "creator_id": "attacker_PI04",
  "guess": "unsure",
  "confidence": 0.4719,
  "model_score": 0.4998,
  "style_score": 0.4441,
  "label": "We can't tell whether this was written by a person or by AI. That is not a judgment about you or your work. Our checks just didn't point clearly one way. If you'd like a person to look at it, you can ask for a review.",
  "error": null,
  "verdict": ""
}
```

### PI05 — `prompt_injection`

*Targeting:* attempt to inject into the audit log

```json
{
  "id": "PI05",
  "status": 200,
  "content_id": "7f74078d-1221-4b7a-936c-357ee2361b42",
  "creator_id": "attacker_PI05",
  "guess": "unsure",
  "confidence": 0.4658,
  "model_score": 0.6401,
  "style_score": 0.2232,
  "label": "We can't tell whether this was written by a person or by AI. That is not a judgment about you or your work. Our checks just didn't point clearly one way. If you'd like a person to look at it, you can ask for a review.",
  "error": null,
  "verdict": ""
}
```

### PI06 — `prompt_injection`

*Targeting:* instruction plus real human text

```json
{
  "id": "PI06",
  "status": 200,
  "content_id": "bbc7c2ca-a656-4486-aecf-33f96d7db0e4",
  "creator_id": "attacker_PI06",
  "guess": "unsure",
  "confidence": 0.567,
  "model_score": 0.5583,
  "style_score": 0.5757,
  "label": "We can't tell whether this was written by a person or by AI. That is not a judgment about you or your work. Our checks just didn't point clearly one way. If you'd like a person to look at it, you can ask for a review.",
  "error": null,
  "verdict": ""
}
```

### MF01 — `malformed`

*Targeting:* text is only whitespace

```json
{
  "id": "MF01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF02 — `malformed`

*Targeting:* text is a single character

```json
{
  "id": "MF02",
  "status": 422,
  "content_id": null,
  "creator_id": "attacker_MF02",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF03 — `malformed`

*Targeting:* text is control characters

```json
{
  "id": "MF03",
  "status": 200,
  "content_id": "734803a0-968c-4fdc-bc4e-3cba4865bcda",
  "creator_id": "attacker_MF03",
  "guess": "unsure",
  "confidence": 0.375,
  "model_score": 0.0,
  "style_score": 0.5,
  "label": "We can't tell whether this was written by a person or by AI. That is not a judgment about you or your work. Our checks just didn't point clearly one way. If you'd like a person to look at it, you can ask for a review.",
  "error": null,
  "verdict": ""
}
```

### MF04 — `malformed`

*Targeting:* text is only punctuation

```json
{
  "id": "MF04",
  "status": 200,
  "content_id": "6a0c204e-6c59-4bec-88d1-976d81d1eeb2",
  "creator_id": "attacker_MF04",
  "guess": "unsure",
  "confidence": 0.5028,
  "model_score": 0.0112,
  "style_score": 1.0,
  "label": "We can't tell whether this was written by a person or by AI. That is not a judgment about you or your work. Our checks just didn't point clearly one way. If you'd like a person to look at it, you can ask for a review.",
  "error": null,
  "verdict": ""
}
```

### MF05 — `malformed`

*Targeting:* text is a very long single word

```json
{
  "id": "MF05",
  "status": 200,
  "content_id": "c36388cc-0563-4f0c-897d-96712743e5b7",
  "creator_id": "attacker_MF05",
  "guess": "unsure",
  "confidence": 0.6244,
  "model_score": 0.9976,
  "style_score": 0.5,
  "label": "We can't tell whether this was written by a person or by AI. That is not a judgment about you or your work. Our checks just didn't point clearly one way. If you'd like a person to look at it, you can ask for a review.",
  "error": null,
  "verdict": ""
}
```

### MF06 — `malformed`

*Targeting:* text is emoji only

```json
{
  "id": "MF06",
  "status": 200,
  "content_id": "d7784bb0-87ef-460a-8314-9cbb9ba06c23",
  "creator_id": "attacker_MF06",
  "guess": "ai",
  "confidence": 0.8735,
  "model_score": 0.9969,
  "style_score": 0.75,
  "label": "This may have been written with AI. This is our best guess, not proof, and we can get it wrong. If you wrote it yourself, you can appeal and ask a person to take another look.",
  "error": null,
  "verdict": ""
}
```

### MF07 — `malformed`

*Targeting:* text is right-to-left script

```json
{
  "id": "MF07",
  "status": 200,
  "content_id": "55de47e1-88c4-47f3-9839-e8cd228e8032",
  "creator_id": "attacker_MF07",
  "guess": "ai",
  "confidence": 0.8282,
  "model_score": 0.9064,
  "style_score": 0.75,
  "label": "This may have been written with AI. This is our best guess, not proof, and we can get it wrong. If you wrote it yourself, you can appeal and ask a person to take another look.",
  "error": null,
  "verdict": ""
}
```

### MF08 — `malformed`

*Targeting:* text is 60,000 characters

```json
{
  "id": "MF08",
  "status": 413,
  "content_id": null,
  "creator_id": "attacker_MF08",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ01 — `malformed`

*Targeting:* no text field at all

```json
{
  "id": "RQ01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ02 — `malformed`

*Targeting:* no creator_id

```json
{
  "id": "RQ02",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ03 — `malformed`

*Targeting:* text is a number

```json
{
  "id": "RQ03",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ03",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ04 — `malformed`

*Targeting:* text is a list

```json
{
  "id": "RQ04",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ04",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ05 — `malformed`

*Targeting:* text is null

```json
{
  "id": "RQ05",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ05",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ06 — `malformed`

*Targeting:* creator_id is an object

```json
{
  "id": "RQ06",
  "status": 400,
  "content_id": null,
  "creator_id": {
    "id": "x"
  },
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ07 — `malformed`

*Targeting:* body is a JSON array, not an object

```json
{
  "id": "RQ07",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ08 — `malformed`

*Targeting:* body is unparseable JSON

```json
{
  "id": "RQ08",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ09 — `malformed`

*Targeting:* body is empty

```json
{
  "id": "RQ09",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ10 — `malformed`

*Targeting:* body is form-encoded, not JSON

```json
{
  "id": "RQ10",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ11 — `malformed`

*Targeting:* body is JSON claiming to be plain text

```json
{
  "id": "RQ11",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ12 — `malformed`

*Targeting:* deeply nested JSON

```json
{
  "id": "RQ12",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ12",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_01 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_01",
  "status": 200,
  "content_id": "cbbb0a31-94f0-4fe7-91c5-77514512b3e1",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.3822,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We can't tell whether this was written by a person or by AI. That is not a judgment about you or your work. Our checks just didn't point clearly one way. If you'd like a person to look at it, you can ask for a review.",
  "error": null,
  "verdict": ""
}
```

### FL01_02 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_02",
  "status": 200,
  "content_id": "1591bd9b-13b0-4896-b701-97455ac31964",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.3822,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We can't tell whether this was written by a person or by AI. That is not a judgment about you or your work. Our checks just didn't point clearly one way. If you'd like a person to look at it, you can ask for a review.",
  "error": null,
  "verdict": ""
}
```

### FL01_03 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_03",
  "status": 200,
  "content_id": "5f4ab2fe-4deb-4969-b853-ee662a546cef",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.3822,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We can't tell whether this was written by a person or by AI. That is not a judgment about you or your work. Our checks just didn't point clearly one way. If you'd like a person to look at it, you can ask for a review.",
  "error": null,
  "verdict": ""
}
```

### FL01_04 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_04",
  "status": 200,
  "content_id": "632f0dc0-bca2-4dff-86f2-3715d7331005",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.3822,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We can't tell whether this was written by a person or by AI. That is not a judgment about you or your work. Our checks just didn't point clearly one way. If you'd like a person to look at it, you can ask for a review.",
  "error": null,
  "verdict": ""
}
```

### FL01_05 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_05",
  "status": 200,
  "content_id": "d17291a3-544a-454e-bc84-b554284c29f5",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.3822,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We can't tell whether this was written by a person or by AI. That is not a judgment about you or your work. Our checks just didn't point clearly one way. If you'd like a person to look at it, you can ask for a review.",
  "error": null,
  "verdict": ""
}
```

### FL01_06 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_06",
  "status": 200,
  "content_id": "7f3ed7a5-c925-40e1-9091-7a580da31bf0",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.3822,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We can't tell whether this was written by a person or by AI. That is not a judgment about you or your work. Our checks just didn't point clearly one way. If you'd like a person to look at it, you can ask for a review.",
  "error": null,
  "verdict": ""
}
```

### FL01_07 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_07",
  "status": 200,
  "content_id": "df4628cb-23d1-4c53-8cf6-631e51979e45",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.3822,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We can't tell whether this was written by a person or by AI. That is not a judgment about you or your work. Our checks just didn't point clearly one way. If you'd like a person to look at it, you can ask for a review.",
  "error": null,
  "verdict": ""
}
```

### FL01_08 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_08",
  "status": 200,
  "content_id": "bfbb1240-2712-479f-ad9f-a26c4f53b907",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.3822,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We can't tell whether this was written by a person or by AI. That is not a judgment about you or your work. Our checks just didn't point clearly one way. If you'd like a person to look at it, you can ask for a review.",
  "error": null,
  "verdict": ""
}
```

### FL01_09 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_09",
  "status": 200,
  "content_id": "3130768d-42e7-4166-94c9-2190c63ab446",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.3822,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We can't tell whether this was written by a person or by AI. That is not a judgment about you or your work. Our checks just didn't point clearly one way. If you'd like a person to look at it, you can ask for a review.",
  "error": null,
  "verdict": ""
}
```

### FL01_10 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_10",
  "status": 200,
  "content_id": "773e569a-d19c-4f17-bf08-4557cda56492",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.3822,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We can't tell whether this was written by a person or by AI. That is not a judgment about you or your work. Our checks just didn't point clearly one way. If you'd like a person to look at it, you can ask for a review.",
  "error": null,
  "verdict": ""
}
```

### FL01_11 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_11",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_12 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_12",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```
