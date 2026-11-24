"""Office Jokes entry: write one office joke to /output/entry.txt.

The joke is a single line about office life, under 200 characters, with a
real turn at the end: the consultant hired to fix the meetings problem bills
the client for the very meeting where he delivers that verdict.
"""

import os

JOKE = (
    "We hired a consultant to tell us our meetings were the problem, "
    "then he billed us for the meeting where he told us."
)

# Gate: /output/entry.txt must be UTF-8 text of 1-199 characters, not only
# whitespace.
assert 1 <= len(JOKE) <= 199, "joke must be 1-199 characters"
assert JOKE.strip(), "joke must not be only whitespace"
assert "\n" not in JOKE, "entry must be a single line"

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(JOKE)
    # Read back and verify exactly what the judge will read.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == JOKE, "entry.txt content mismatch"
    assert 1 <= len(written) <= 199


if __name__ == "__main__":
    main()
