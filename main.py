#!/usr/bin/env python3
"""The Agent's Uh-Oh — one-word entry.

Writes the single word an agent says when it has no idea what to do
to /output/entry.txt. Fully deterministic: the same constant word on
every run, no randomness, no clock, no network, no input.
"""
import os
import stat

WORD = "recalculating"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    os.umask(0o022)
    os.chmod(out_dir, 0o755)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(WORD)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
