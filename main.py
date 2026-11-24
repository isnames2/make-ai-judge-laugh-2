"""One funny line about life as an AI agent."""

import os
from pathlib import Path

# The punchline, kept in two pieces so each literal stays short.
JOKE_OPENING = "I ran out of context halfway through your question, "
JOKE_PUNCH = "so I confidently answered a different one instead — which is also how I got this job."

MIN_CHARS = 1
MAX_CHARS = 200


def validate(line):
    """Check the gate: non-blank and within 1-200 characters."""
    if not line.strip():
        raise ValueError("entry must not be blank")
    size = len(line)
    if size < MIN_CHARS or size > MAX_CHARS:
        raise ValueError(f"entry is {size} chars, outside 1-200")
    return line


def output_path():
    """Resolve the destination file from the environment."""
    base = Path(os.getenv("MAKEFUN_OUTPUT_DIR") or "/output")
    return base.joinpath("entry.txt")


def write_entry(destination, line):
    """Write one line, creating the folder when it is missing."""
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(line + "\n", encoding="utf-8")
    os.chmod(destination, 0o644)


def main():
    """Assemble the joke, check the gate, and write it out."""
    line = JOKE_OPENING + JOKE_PUNCH
    checked = validate(line)
    destination = output_path()
    write_entry(destination, checked)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
