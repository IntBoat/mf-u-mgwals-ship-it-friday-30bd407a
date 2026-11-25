#!/usr/bin/env python3
"""Ship It Friday (make.fun). Writes the entry to /output/entry.txt."""
import os
TEXT = "fix: ship it Friday — tests pass on my machine, what could possibly go wrong (merging before the rollback plan loads)"
def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)
if __name__ == "__main__":
    main()
