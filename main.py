#!/usr/bin/env python3
"""The Absurd Clause Contest entry: one absurd ToS clause, one sentence."""
import os

SENTENCE = (
    "The Company reserves the right to replace your reflection "
    "with a stock photo, without notice, compensation, or resemblance."
)

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(SENTENCE + "\n")

if __name__ == "__main__":
    main()
