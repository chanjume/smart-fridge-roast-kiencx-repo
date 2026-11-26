#!/usr/bin/env python3
"""Roast the Smart Fridge: one line, best laugh wins.

The line: at 1:58 a.m. the fridge emails the wife a photo of the husband
eating her birthday cake, with the subject line "Exhibit A." The fridge is
not a nag or a snitch in the abstract -- it is a witness for the prosecution,
with a timestamp, a named victim, and a courtroom exhibit label. Fresh angle:
no takeout/doctor, no ice maker, no leftovers family, no 3 a.m. cake monologue.
One line, one scene, one punchline: the appliance kept receipts.
"""
import os

ENTRY = 'At 1:58 a.m. my fridge emailed my wife a photo of me eating her birthday cake. Subject line: "Exhibit A."'


def main():
    assert 1 <= len(ENTRY) <= 160, len(ENTRY)
    assert "\n" not in ENTRY.strip() and ENTRY.strip()
    out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)
    print(f"chars: {len(ENTRY)}")


if __name__ == "__main__":
    main()
