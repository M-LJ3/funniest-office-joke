"""Emit one funny office joke into /output/entry.txt.

The program produces a single joke line about office life and
stores it where the contest expects to find it.
"""

import os
from pathlib import Path

OUTPUT_PATH = Path("/output/entry.txt")


def office_gag():
    """Return one funny line about working in an office."""
    return (
        "The office coffee machine broke, so now we just stare at each "
        "other and call it a brainstorming session."
    )


def confirm_entry_matches(expected):
    """Double-check the stored entry is exactly the intended gag."""
    stored = OUTPUT_PATH.read_text(encoding="utf-8")
    assert stored == expected, "entry file does not match the gag"


def main():
    gag = office_gag()
    os.makedirs(OUTPUT_PATH.parent, exist_ok=True)
    # Store the gag exactly as written, with no trailing newline.
    OUTPUT_PATH.write_text(gag, encoding="utf-8")
    confirm_entry_matches(gag)


if __name__ == "__main__":
    main()
