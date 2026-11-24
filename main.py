"""Write the phone's last words at 1 percent battery to /output/entry.txt.

Stdlib only, no network, deterministic: the same line every run.
"""

import os

LINE = "Plot twist: I've been at 1 percent for three hours. I just liked watching you panic."

OUT_DIR = os.environ.get("ENTRY_OUTPUT_DIR", "/output")


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    path = os.path.join(OUT_DIR, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
