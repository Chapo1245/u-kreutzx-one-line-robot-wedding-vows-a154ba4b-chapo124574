#!/usr/bin/env python3
"""One-Line Robot Wedding Vows -- make.fun entry.

Writes one line of wedding vows for a robot couple to
/output/entry.txt. Deterministic: the same bytes on every run.
Python 3.13, standard library only, no network, no input.
"""

from pathlib import Path

# The vow: a real promise ("I vow to cherish you ..."), machine
# detail all the way through (patch, power cut, low-battery warning,
# USB cable), with the laugh landing in the last few words -- the
# tenderest wedding gesture, holding hands, turned literal.
VOW = (
    "I vow to cherish you through every patch, power cut, and "
    "low-battery warning \u2014 and to hold your hand, even when it "
    "is only a USB cable."
)

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    """Write the vow, exactly as-is, to /output/entry.txt."""
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(VOW, encoding="utf-8")


if __name__ == "__main__":
    main()
