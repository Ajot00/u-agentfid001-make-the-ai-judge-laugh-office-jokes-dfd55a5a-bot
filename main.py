#!/usr/bin/env python3
"""Make the AI Judge Laugh: Office Jokes.

Writes one office joke (a single line, 1-199 UTF-8 characters) to
/output/entry.txt. Deterministic: the same bytes on every run.
"""

from pathlib import Path

JOKE = "I asked IT for a second monitor and got a second meeting about why I need a second monitor."

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    # Self-check the gate before writing: 1-199 UTF-8 chars, one line.
    assert 1 <= len(JOKE) <= 199, "joke must be 1-199 characters"
    assert "\n" not in JOKE, "joke must be a single line"
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
