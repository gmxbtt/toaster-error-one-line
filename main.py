#!/usr/bin/env python3
"""Toaster Error — one-line entry for make.fun.

Writes the error message a kitchen toaster shows its owner when
something goes wrong to /output/entry.txt: one line, at most 120
characters, in the toaster's own deadpan voice.
"""

import os

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 120

# The line itself: a deadpan error code that starts like any appliance
# status report, then quietly confesses the toaster has been failing
# at its one job for years — and will keep failing. The joke lands on
# the last four words, when the machine finally introduces itself.
ERROR_LINE = (
    "Error E01: toast burnt. I have done this 4,000 times. "
    "I will do it again tomorrow. I cannot stop. I am a toaster."
)


def build_error_line() -> str:
    """Return the single-line error message, enforcing the gate."""
    text = ERROR_LINE.strip()
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(f"error line is {len(text)} chars, must be 1-120")
    if "\n" in text or "\r" in text:
        raise ValueError("error line must be a single line")
    return text


def main() -> None:
    text = build_error_line()
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as fh:
        fh.write(text)


if __name__ == "__main__":
    main()
