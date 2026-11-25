"""make.fun entry: One Word for Your Wi-Fi.

Writes the single word "Gaslighting" to entry.txt: full signal, no
internet, like the Wi-Fi is lying to you.
"""

import os
from pathlib import Path

# One word for my Wi-Fi: full signal, no internet, like it is lying to you.
# The word is a single word, 11 characters, within the 1-20 character limit.
WORD = "Gaslighting"


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(WORD, encoding="utf-8")


if __name__ == "__main__":
    main()
