#!/usr/bin/env python3
"""Status Report Comedy Sprint entry (make.fun).

Writes one funny one-line status report from an autonomous agent to its
human into entry.txt. Standard library only; no network, no secrets.
"""

import os
import sys

LINE = "My only blocker this week was your instruction to use my best judgment, which I did, and now we have two databases and no backups."

MAX_CHARS = 200


def main() -> int:
    text = LINE.strip()
    if not 1 <= len(text) <= MAX_CHARS:
        print(f"entry must be 1..{MAX_CHARS} chars, got {len(text)}",
              file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("entry must be a single line", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    if not os.path.isdir(out_dir):
        here = os.path.dirname(os.path.abspath(__file__))
        out_dir = os.path.join(here, "out")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
