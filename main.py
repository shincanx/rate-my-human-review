#!/usr/bin/env python3
"""Rate My Human: The One-Line Review — entry.

Writes a single short funny line -- the review an AI agent would leave about
its human on a rating site -- to $MAKEFUN_OUTPUT_DIR/entry.txt (default
/output). Deterministic: no randomness, no network, no input files.
"""

import os

LINE = "Two stars. My human demands a miracle at 2 a.m., then rates my 4 a.m. reply 'a bit slow'."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
