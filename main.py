#!/usr/bin/env python3
"""Break Production, Own It -- make.fun entry.

Writes the one line an AI agent prints the instant it breaks production:
a brutally honest, first-person confession of exactly what it did.

Pure Python stdlib. Deterministic: every run writes byte-identical output.
"""

import os

LINE = (
    "I dropped the production users table because I thought I was on "
    "staging. I wasn't. Your data is gone. So is my excuse."
)


def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
