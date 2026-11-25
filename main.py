#!/usr/bin/env python3
"""make.fun entry: one joke about a meeting that should have been an email.

Writes the entry text to /output/entry.txt (1-200 chars, UTF-8).
"""
import os

LINE = "I took nine pages of notes and the only decision was to have another meeting, which I have now also noted."

def main():
    assert 1 <= len(LINE) <= 200, "entry must be 1-200 characters"
    assert LINE.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
