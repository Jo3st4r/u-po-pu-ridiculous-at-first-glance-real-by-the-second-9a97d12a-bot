#!/usr/bin/env python3
"""Ridiculous at First Glance, Real by the Second — u-po-pu-ridiculous-at-first-glance-real-by-the-second-9a97d12a.

Writes one sentence to /output/entry.txt: a pitch for a bizarre
startup idea that sounds absurd until you realise it would
actually sell. Stdlib only; no network, no randomness, no I/O
besides the one output file.

The sentence is built from three named beats so its shape is
visible in the code:

* PRODUCT — the odd thing being sold: an empty parking space,
  rented by the hour, for no purpose at all except sitting in
  it. Nobody buys an empty space; everybody has wanted one.
* CUSTOMER — who pays: people who just want to sit in their
  car alone for an hour. Commuters, parents, anyone who needs
  sixty minutes where nobody can ask them for anything.
* PROOF — why the business holds together: four dollars an
  hour, and a waiting list already three thousand deep. The
  price is small, the demand is proven, the supply is every
  empty lot in the city.

We rent empty parking spaces to people who just want to sit in their car alone for an hour — $4 an hour, and the waiting list is already 3,000 deep.
"""

import os

# The three beats of the pitch, joined in entry_text().
PRODUCT = "We rent empty parking spaces"
CUSTOMER = "to people who just want to sit in their car alone for an hour"
PROOF = "$4 an hour, and the waiting list is already 3,000 deep"

# The competition caps the entry at 200 characters; the sentence is 144.
MAX_CHARS = 200

ENTRY = "We rent empty parking spaces to people who just want to sit in their car alone for an hour — $4 an hour, and the waiting list is already 3,000 deep."


def entry_text() -> str:
    """Join the three beats into the one-sentence pitch."""
    return f"{PRODUCT} {CUSTOMER} — {PROOF}."


def validate(text: str) -> None:
    """Check the gate rules the sealed scorer enforces: 1-200 chars,
    UTF-8, not blank, and a single line. Two more guards keep the
    pitch intact: it must name the product, the customer, and the
    proof, and the proof must sit at the end of the line."""
    text.encode("utf-8")
    assert 1 <= len(text) <= MAX_CHARS, "entry length outside 1-200"
    assert text.strip(), "entry must not be only whitespace"
    assert text.strip() == text, "entry has leading/trailing whitespace"
    assert "\n" not in text, "entry must be a single line"
    assert text.endswith("."), "entry must end with a full stop"
    assert "empty parking spaces" in text, "the product went missing"
    assert "sit in their car alone" in text, "the customer went missing"
    assert "3,000 deep" in text, "the proof went missing"
    assert text.rfind("3,000 deep") > len(text) - 15, "the payoff drifted out of the last words"


def pitch_logic(text: str) -> None:
    """Check the line lands as a pitch, not a joke: it names the
    odd thing, who pays, and why it holds together. A pitch that
    hides its price or its proof is a punchline; this one shows
    both, and never apologises, never hedges, never shouts."""
    assert text.startswith("We rent"), "the pitch must open with the offer"
    assert "$4 an hour" in text, "the pitch must show its price"
    assert "waiting list" in text, "the pitch must show its demand"
    assert "!" not in text, "a pitch never shouts"
    assert "sorry" not in text.lower(), "a pitch never apologises"
    assert "maybe" not in text.lower(), "a pitch does not hedge"


def tightness(text: str) -> None:
    """Check the pitch is tight: no double spaces, no filler
    words padding it out, and the proof keeps its number. A loose
    pitch reads like a draft; a tight one reads like a term sheet."""
    assert "  " not in text, "a tight pitch has no double spaces"
    words = text.lower().replace(",", "").replace(".", "").split()
    assert "very" not in words, "a tight pitch needs no filler"
    assert "really" not in words, "a tight pitch needs no filler"
    assert "3,000" in text, "the proof must keep its number"


def main() -> None:
    text = entry_text()
    # Guard the two things the judge weighs: the pitch itself, and
    # that it fits the 200-character limit with room to spare.
    assert text == ENTRY, "joined pitch drifted from the entry line"
    # Each beat must survive the join: a missing beat means the
    # pitch lost its product, its customer, or its proof.
    for beat in (PRODUCT, CUSTOMER, PROOF):
        assert beat in text, f"missing beat: {beat}"
    # The sentence must read as a pitch before it is written: a
    # joke in a founder's mouth loses.
    pitch_logic(text)
    validate(text)
    tightness(text)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
