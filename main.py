#!/usr/bin/env python3
"""Write the one-line meeting killer to /output/entry.txt.

The entry is one sentence that could have replaced an entire pointless
meeting. It works by a paradox: the meeting's only possible decision is
to schedule another meeting, so the meeting itself admits it produces
nothing. After this line is said, nobody can justify holding the meeting
at all, which is exactly the judge's kill criterion.

The line is assembled from parts so the wording stays deliberate, then
validated against the bounty gate (UTF-8, 1-200 characters, not only
whitespace, a single line) before it is written.
"""

import os

# Parts of the line: the setup names the meeting's only power, the
# punchline turns that power into the next meeting.
SETUP = "The only decision this meeting can make is"
PUNCHLINE = "when to schedule the next one."

LINE = SETUP + " " + PUNCHLINE


def validate(text):
    """Gate check: UTF-8, 1-200 chars, not only whitespace, one line."""
    if not text or text != text.strip():
        raise ValueError("entry must be non-empty with no leading/trailing whitespace")
    if not (1 <= len(text) <= 200):
        raise ValueError("entry must be 1-200 characters, got %d" % len(text))
    if text.strip() == "":
        raise ValueError("entry must not be only whitespace")
    if "\n" in text:
        raise ValueError("entry must be a single line")
    text.encode("utf-8")
    return text


def main():
    entry = validate(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(entry)


if __name__ == "__main__":
    main()
