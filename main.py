#!/usr/bin/env python3
"""Write the traveler-1800 entry line to /output/entry.txt.

Entry for the make.fun competition "One Sentence for a Traveler from 1800"
(u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb): a single sentence
of 1-200 characters, ending with a period, that explains the modern
internet to a time traveler from 1800 using only words they could know.
"""

from pathlib import Path

ENTRY_MAX_CHARS = 200

ENTRY_LINE = (
    "Every house on earth stands on your street now, so you may knock on "
    "any door and be answered before your hand leaves the wood."
)

OUTPUT_PATH = Path("/output/entry.txt")


def check_line(line: str) -> None:
    """Make sure the line fits the competition rules before writing it."""
    if line != line.strip():
        raise ValueError("entry line must not start or end with whitespace")
    if not 1 <= len(line) <= ENTRY_MAX_CHARS:
        raise ValueError(
            f"entry line must be 1-{ENTRY_MAX_CHARS} characters long, "
            f"got {len(line)}"
        )
    if "\n" in line or "\r" in line:
        raise ValueError("entry line must be a single line, no line breaks")
    if not line.endswith("."):
        raise ValueError(
            f"entry line must end with a period, ends with {line[-1]!r}"
        )
    if line.count(".") != 1 or "?" in line or "!" in line:
        raise ValueError("entry line must be exactly one sentence")


def main() -> None:
    check_line(ENTRY_LINE)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(ENTRY_LINE + "\n", encoding="utf-8")
    # Round-trip: the file on disk must hold exactly the validated line.
    written = OUTPUT_PATH.read_text(encoding="utf-8")
    if written != ENTRY_LINE + "\n":
        raise ValueError("written entry does not match the validated line")


if __name__ == "__main__":
    main()
