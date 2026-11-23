#!/usr/bin/env python3
"""Office Jokes — one-line joke entry for make.fun.

Writes a single one-line office joke (<200 chars) to /output/entry.txt.

The joke: a passive-aggressive office classic ("per my last email") meets
the out-of-office reply — the argument keeps going even while its author
is on holiday. Recognition (every office worker has lived this), a turn
at the end (the argument continues without its author), tight wording,
and no Monday-morning / photocopier cliche.
"""

import os

JOKE = "I put 'per my last email' in my out-of-office reply so the argument can continue without me."


def main() -> None:
    text = JOKE.strip()
    assert 1 <= len(text) <= 199, f"joke must be 1-199 chars, got {len(text)}"
    assert "\n" not in text, "joke must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)  # no trailing newline: the file is exactly the joke


if __name__ == "__main__":
    main()
