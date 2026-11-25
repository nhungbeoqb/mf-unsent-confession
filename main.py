#!/usr/bin/env python3
"""Unsent: The Micro-Confession Sprint.

Writes one two-part micro-confession to /output/entry.txt:
a To: line naming who it was meant for, and the unsent message
itself, one line written exactly as it was typed.
Pure Python 3 standard library; deterministic.
"""

import os

ENTRY = (
    "To: my brother's widow\n"
    "i kept his last voicemail and i still play it in the car park "
    "outside your house when i can't bring myself to come in, "
    "just to hear him say my name wrong again\n"
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
