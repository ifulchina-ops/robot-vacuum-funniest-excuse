#!/usr/bin/env python3
"""The Robot Vacuum's Funniest Excuse — make.fun entry.

Writes one line (at most 120 characters) to /output/entry.txt: the excuse
a robot vacuum gives for missing a spot. Deterministic: the same line on
every run, no network, no randomness, no input files.
"""

import os

ENTRY = "I didn't miss that spot \u2014 I gave the dust bunny a head start, and it still beat me. Rematch at the dock."

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 120  # the sealed gate: /output/entry.txt must be 1-120 chars

# The joke, beat by beat: denial ("I didn't miss it"), a sporting excuse
# (the dust bunny got a head start), defeat ("it still beat me"), and a
# machine's idea of revenge (a rematch at the charging dock).


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= MAX_CHARS, f"entry is {len(text)} chars, must be 1-{MAX_CHARS}"
    assert "\n" not in text, "entry must be a single line"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
