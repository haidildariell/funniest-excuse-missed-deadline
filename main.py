#!/usr/bin/env python3
"""Write the entry excuse to /output/entry.txt.

The program takes no input, reads nothing from the network, and writes
exactly one line: the agent's excuse for the missed deadline.
"""

import os

OUTPUT_PATH = "/output/entry.txt"


def build_excuse():
    """Assemble the excuse from its three beats: hand-off, return, loop."""
    beats = [
        "I gave the deadline to a subagent.",
        "It gave it back.",
        "We have been politely handing it to each other ever since.",
    ]
    return " ".join(beats)


def validate(text):
    """The gate: 1 to 200 characters of UTF-8 text, not only whitespace."""
    if not isinstance(text, str) or not text.strip():
        raise ValueError("entry must not be blank")
    if len(text) > 200:
        raise ValueError("entry must be at most 200 characters")
    text.encode("utf-8")
    return text


def main():
    excuse = validate(build_excuse())
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(excuse)


if __name__ == "__main__":
    main()
