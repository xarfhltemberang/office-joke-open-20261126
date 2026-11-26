#!/usr/bin/env python3
"""Write one original office joke to /output/entry.txt.

The competition gate requires UTF-8 text of 1 to 200 characters, not only
whitespace. The joke is written with no trailing newline, so the byte count
matches the character count exactly and the gate sees the joke alone.
"""

import os

JOKE = (
    "Our office printer only jams on documents that matter. "
    "It's the most loyal employee we have: "
    "never works, always present, impossible to fire."
)


def main() -> None:
    output_path = "/output/entry.txt"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
