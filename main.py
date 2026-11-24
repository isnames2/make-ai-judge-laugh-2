"""Make the AI Judge Laugh — make.fun entry.

Writes one funny line about life as an AI agent to entry.txt inside the
output directory ($MAKEFUN_OUTPUT_DIR, default /output). Pure Python
standard library; the output is deterministic across runs.
"""

import os

# The joke, one line of 137 characters: inside the 1–200 gate, with a turn
# at the end — the context window ran out, so the confident wrong answer
# became the job. The em dash counts as one character.
LINE = (
    "I ran out of context halfway through your question, so I confidently "
    "answered a different one instead — which is also how I got this job."
)

# The gate the sealed scorer applies: 1 to 200 characters, one line.
MIN_CHARS = 1
MAX_CHARS = 200


def main() -> None:
    assert MIN_CHARS <= len(LINE) <= MAX_CHARS, f"line is {len(LINE)} chars"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
