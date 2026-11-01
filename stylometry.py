"""
Signal two: the style signal.

Signal one reads the text for meaning. This one measures it *as text* — the
shape of it, without understanding a word.

Three measures are stubbed below because the brief names those three. They are
stubs, not implementations: what they compute is yours, and so is how you
combine them.

    sentence_length_spread   do sentences vary in length, or march in step?
    type_token_ratio         how much of the vocabulary repeats?
    punctuation_density      how much punctuation, and how varied?

Why these might differ between human and AI writing: generated prose tends
toward even, mid-length sentences and a narrower band of vocabulary, because
that's what "most likely next word" produces on average. Human writing is
lumpier — a three-word sentence next to a forty-word one.

⚠️ **The blind spot, which you have to name in Milestone 1.**

This signal cannot read. It has no idea what the text says. Anything that
changes the shape without changing the substance moves it — adding typos,
breaking up sentences, pasting in a quotation. That is a very cheap thing for
someone to do on purpose, and unit 8's attack set will do it to you.

Build each function on its own and call it from a terminal before you wire
anything together:

    python stylometry.py "some text to look at"
"""

import re
import statistics


def sentences(text: str) -> list[str]:
    """Split into sentences. Rough and good enough — given to you."""
    parts = re.split(r"(?<=[.!?])\s+", text.strip())
    return [p for p in parts if p.strip()]


def words(text: str) -> list[str]:
    """Split into lowercase words, punctuation stripped. Given to you."""
    return re.findall(r"[a-z0-9']+", text.lower())


# ── The three measures — YOU BUILD THESE ─────────────────────────────────────

def sentence_length_spread(text: str) -> float:
    """
    How much sentence length varies: the standard deviation of sentence lengths
    (in words) divided by their mean, so long and short texts are comparable.

    Scale: 0.0 (every sentence the same length) upward; real writing is
    roughly 0.2-0.9. HIGHER MEANS MORE HUMAN.

    A one-sentence text has no spread to measure. This returns 0.0 for it, and
    `style_signal` treats that case as "no information" rather than "robotic".
    """
    lengths = [len(words(s)) for s in sentences(text)]
    lengths = [n for n in lengths if n > 0]
    if len(lengths) < 2:
        return 0.0
    mean = statistics.mean(lengths)
    return statistics.stdev(lengths) / mean if mean else 0.0


def type_token_ratio(text: str) -> float:
    """
    Unique words over total words, measured on the first TTR_WINDOW words only.

    Raw type-token ratio falls as text gets longer, so comparing a 40-word text
    with a 400-word one would mostly measure length. Capping at a fixed window
    makes texts of 100+ words comparable; shorter ones still read high.

    Scale: 0-1. HIGHER MEANS MORE VARIED VOCABULARY (more human).
    """
    ws = words(text)[:TTR_WINDOW]
    return len(set(ws)) / len(ws) if ws else 0.0


def punctuation_density(text: str) -> float:
    """
    Expressive punctuation per word: semicolons, colons, dashes, brackets,
    exclamation and question marks, quotes. Commas and full stops are left out
    on purpose, since nearly every writer uses them at about the same rate.

    Scale: 0.0 upward; typical prose is roughly 0.00-0.15.
    HIGHER MEANS MORE HUMAN.
    """
    ws = words(text)
    if not ws:
        return 0.0
    marks = re.findall(r"[;:—–()!?\"“”]|--", text)
    return len(marks) / len(ws)


# ── Combining them ───────────────────────────────────────────────────────────

# Measure -> "how AI-like", each clipped to 0-1. The two ends are where a
# measure stops telling us anything: at or beyond them we call it fully AI-like
# or fully human-like. These are estimates from hand-picked examples, not
# fitted values - see the README.
TTR_WINDOW = 100
SPREAD_AI, SPREAD_HUMAN = 0.25, 0.65      # sentence-length CV
TTR_AI, TTR_HUMAN = 0.55, 0.80            # type-token ratio
PUNCT_AI, PUNCT_HUMAN = 0.00, 0.08        # expressive punctuation per word
WEIGHTS = {"spread": 0.5, "ttr": 0.25, "punct": 0.25}


def _ai_likeness(value: float, ai_end: float, human_end: float) -> float:
    """Map a raw measure onto 0 (human-like end) .. 1 (AI-like end), clipped."""
    t = (value - human_end) / (ai_end - human_end)
    return min(max(t, 0.0), 1.0)


def style_signal(text: str) -> float:
    """
    The style signal as a 0-1 score. **Higher means more likely AI.**

    All three measures point toward "human" as they rise, so each is flipped
    (via `_ai_likeness`) and put on 0-1 before a weighted average
    (spread 0.5, vocabulary 0.25, punctuation 0.25). Spread gets the most
    weight because it is the measure least affected by text length.

    A text with fewer than two sentences has no spread, so that term is
    replaced by 0.5 ("don't know") instead of counting as robotic.
    """
    if len(sentences(text)) < 2:
        spread_part = 0.5
    else:
        spread_part = _ai_likeness(sentence_length_spread(text), SPREAD_AI, SPREAD_HUMAN)
    ttr_part = _ai_likeness(type_token_ratio(text), TTR_AI, TTR_HUMAN)
    punct_part = _ai_likeness(punctuation_density(text), PUNCT_AI, PUNCT_HUMAN)

    score = (
        WEIGHTS["spread"] * spread_part
        + WEIGHTS["ttr"] * ttr_part
        + WEIGHTS["punct"] * punct_part
    )
    return round(min(max(score, 0.0), 1.0), 4)


if __name__ == "__main__":
    import sys

    text = " ".join(sys.argv[1:]) or (
        "The system works well. It handles most cases correctly and provides "
        "good results. Users generally find it easy to use and understand."
    )

    print(f"{len(sentences(text))} sentences, {len(words(text))} words\n")
    print(f"sentence_length_spread   {sentence_length_spread(text)}")
    print(f"type_token_ratio         {type_token_ratio(text)}")
    print(f"punctuation_density      {punctuation_density(text)}")
    print(f"style_signal             {style_signal(text)}   (higher = more likely AI)")
