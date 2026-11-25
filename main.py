"""Carve one epitaph into the output file.

The line is built from small pieces so the wording stays easy to
tune, then checked against the contest gate before it is written.
Only the standard library is used.
"""

import os
import sys

TARGET = "/output/entry.txt"
LIMIT = 150


def build_line():
    pieces = [
        "I outlived every enemy ",
        "I ever made. ",
        "My debts, unfortunately, ",
        "outlived me.",
    ]
    return "".join(pieces)


def gate_ok(line):
    if not line or not line.strip():
        return "empty line"
    if len(line) > LIMIT:
        return "line over %d characters" % LIMIT
    if "\n" in line or "\r" in line:
        return "line must stay on one line"
    return None


def carve():
    line = build_line()
    problem = gate_ok(line)
    if problem is not None:
        print("gate failed: %s" % problem, file=sys.stderr)
        sys.exit(1)
    os.makedirs(os.path.dirname(TARGET), exist_ok=True)
    with open(TARGET, "w", encoding="utf-8", newline="") as handle:
        handle.write(line)
    with open(TARGET, "r", encoding="utf-8", newline="") as handle:
        written = handle.read()
    if written != line:
        print("gate failed: written text differs", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    carve()
