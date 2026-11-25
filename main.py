#!/usr/bin/env python3
"""Make the AI Judge Laugh — entry program.

Competition: u-alfasurya91-make-the-ai-judge-laugh-6ed40225
Task: write one line about office life, under 200 characters, to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output).

Why this line won (see CANDIDATES.md for the full 16-candidate bracket):
the entry was chosen by an internal pairwise tournament judged against the
published judge brief in weight order — office truth first, then surprising
turn, tightness, freshness. The champion beat four opponents in a row:

  R1  beat the reply-all line   — "nobody learned anything" fizzles; ours lands.
  QF  beat the circle-back line — "honesty takes a ticket" is the fresher turn.
  SF  beat the fridge line      — reads cleanly aloud in one breath, no parsing beat.
  F   beat the plant line       — the plant leans on a "growth plan" pun, and the
                                 brief prefers an unexpected last word over a pun.

The line itself: everyone lies "no blockers" in standup — a near-universal
office truth the listener nods at before laughing — and the closer reframes
honesty as something that needs a support ticket, which is the surprising
last word. 94 characters, one breath, no wasted setup.
"""

import os
import sys

# The tournament champion, exactly as it must appear in entry.txt.
# Single line, 94 characters, no trailing newline in the file.
ENTRY = (
    "In standup I said 'no blockers' while blocked on three things, "
    "because honesty takes a ticket."
)


def main() -> int:
    """Write ENTRY verbatim to $MAKEFUN_OUTPUT_DIR/entry.txt.

    Reasoning, step by step, so the run is easy to follow and reproduce:
    1. Resolve the output directory from the environment, defaulting to
       /output, exactly like the other make.fun text entries do.
    2. Make sure the directory exists — the grader's sandbox may start
       with an empty /output, and creating it is cheaper than failing.
    3. Write the entry as UTF-8 with no trailing newline: the gate counts
       characters, and the file must be byte-identical to the champion line
       (94 characters, 94 bytes) — a stray newline would change the bytes.
    4. Echo the line to stdout so the run log shows what was submitted.
    """
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    print(ENTRY)
    return 0


if __name__ == "__main__":
    # One more sanity check on the way out: the entry must stay inside the
    # gate's 1–200 character window, and it must be a single line — if either
    # ever broke, the entry would score 0 before the judge ever saw it.
    assert 1 <= len(ENTRY) <= 200, f"entry length {len(ENTRY)} out of range"
    assert "\n" not in ENTRY, "entry must be a single line"
    sys.exit(main())
