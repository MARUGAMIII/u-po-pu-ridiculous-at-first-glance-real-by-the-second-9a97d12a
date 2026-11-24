#!/usr/bin/env python3
"""Ridiculous at First Glance, Real by the Second.

Writes one sentence (max 200 chars) pitching a bizarre startup idea
that sounds absurd until the business logic lands.
Pure stdlib, deterministic, no network, no file reads outside this repo.
"""

import os

ENTRY = (
    "We rent out professional mourners to cry at strangers' funerals, "
    "because grieving families pay $40 a head so nobody dies looking "
    "unloved in public."
)


def main() -> None:
    # Gate: one ASCII sentence, 1-200 chars, exactly one sentence.
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars"
    ENTRY.encode("ascii")
    assert ENTRY.count(".") == 1 and ENTRY.endswith("."), "must be one sentence"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="ascii") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
