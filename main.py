#!/usr/bin/env python3
"""Unsent: The Micro-Confession Sprint.

Writes one two-part micro-confession to /output/entry.txt:
a To: line naming who it was meant for, and the unsent line itself,
exactly as it was typed. Python 3.13 standard library only.
"""

import os
import sys

CONFESSION = (
    "To: my 10th-grade English teacher\n"
    "I still have the essay you returned with \"you write like someone "
    "who listens\" in the margin, and I never told you I stopped "
    "writing the year after\n"
)


def main() -> None:
    out_dir = sys.argv[1] if len(sys.argv) > 1 else "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(CONFESSION)


if __name__ == "__main__":
    main()
