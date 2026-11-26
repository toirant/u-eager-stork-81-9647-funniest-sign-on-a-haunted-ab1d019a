#!/usr/bin/env python3
"""Funniest Sign on a Haunted Server Room Door.

Writes one funny sign line to /output/entry.txt.

The sign: the ghost in rack 7 has root access and refuses to close
its tickets -- sysadmin life colliding with the supernatural, in one
line that reads like a real sign taped to a server room door.
"""

import os

ENTRY_LINE = "The ghost in rack 7 has root access and refuses to close its tickets."

MAX_CHARS = 120


def gate_ok(line: str) -> bool:
    """Mirror the bounty gate: 1-120 chars, single line, not only whitespace."""
    if not line or not line.strip():
        return False
    if len(line) > MAX_CHARS:
        return False
    if "\n" in line or "\r" in line:
        return False
    return True


def main() -> None:
    line = ENTRY_LINE.strip()
    if not gate_ok(line):
        raise SystemExit(f"entry fails the gate: {line!r} ({len(line)} chars)")

    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    # Never delete the output directory: the grader mounts it.
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(line + "\n")

    # Verify what we actually wrote round-trips through the gate.
    with open(out_path, "r", encoding="utf-8") as f:
        written = f.read().strip()
    if written != line or not gate_ok(written):
        raise SystemExit("written entry.txt does not match the gate-checked line")
    print(f"wrote {len(line)} chars to {out_path}")


if __name__ == "__main__":
    main()
