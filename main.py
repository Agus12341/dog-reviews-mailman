#!/usr/bin/env python3
"""Write the dog's mailman review to entry.txt."""

import os

# The winning line: picked from three drafts judged pairwise on
# the kit's criteria (a funny one-line review a dog gives the
# mailman first, then the dog's own side of the visit as the
# joke, a dog's voice and priorities rather than a person in a
# fur suit, one tight line with a turn at the end, and a laugh
# that belongs to this dog and this mailman). The one-star
# grievance about smelling of other dogs is good but static;
# the two-star bribe list is funny but ends flat. The winner
# keeps score like a dog would: 412 visits, both ankles intact,
# and a rematch booked for tomorrow. The gate checks entry.txt
# as UTF-8 text of 1 to 200 characters: this line is 113 code
# points, 114 with its trailing newline (verified by a local
# run, byte for byte against the winning draft).
TEXT = "Five stars for the chase, zero for the catch: 412 visits, and the coward still has both ankles. Rematch tomorrow."


def write_entry(out_dir: str) -> None:
    """Write the line, with its trailing newline, into out_dir."""
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT + "\n")


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    write_entry(out_dir)


if __name__ == "__main__":
    main()
