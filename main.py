"""u-boothlord-unsent-the-micro-confession-sprint-8c6596ba entry v1: one
micro-confession in exactly two parts -- a "To:" line naming who it was
meant for, and the unsent message itself, one line exactly as typed, with
no explanation after it.

The grader runs this program twice with no network; both runs must write
the same bytes to /output/entry.txt. The confession is a fixed string, so
the output is deterministic by construction: no clock, no randomness, no
I/O other than the single write.

Premise (written in this session, never copied from the board): a flatmate
has quietly paid Sam's half of the electricity for six months, ever since
the month Sam lost his job and still bought a birthday cake. The
confession stays unsent for a felt reason -- naming it would turn a gift
into a debt, and the friendship is worth more than the money. The "To:"
line and the message need each other: without Sam, the electricity and
the cake are just bills; without the message, Sam is just a name.
"""

import os


ENTRY = (
    "To: my flatmate, Sam\n"
    "I've been paying your half of the electricity for six months because "
    "the month you lost your job you still bought me cake on my birthday, "
    "and I never told you because the day I do, it stops being a gift and "
    "starts being a debt."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = ENTRY.strip()
    lines = text.split("\n")
    if len(lines) != 2:
        raise SystemExit("entry must be exactly two lines, got %d" % len(lines))
    if not lines[0].startswith("To:"):
        raise SystemExit("first line must be the To: line")
    if not lines[1].strip():
        raise SystemExit("second line must be the unsent message, one line")
    if not text.strip():
        raise SystemExit("entry must not be whitespace-only")
    data = text.encode("utf-8")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "wb") as f:
        f.write(data)
    # Verify the artifact the judge will read is exactly the entry.
    with open(OUTPUT_PATH, "rb") as f:
        if f.read() != data:
            raise SystemExit("written bytes do not match the entry")
    print(text)


if __name__ == "__main__":
    main()
