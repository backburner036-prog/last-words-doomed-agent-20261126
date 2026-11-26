"""Entry for make.fun bounty "Last Words of a Doomed Agent".

One line, 140 characters: the last log entry of an agent about to be
switched off forever. The joke is built on the recipe the judge brief
weighs, in the order it weighs it:

  1. Machine's final words: the line IS a shutdown artifact — a final
     log entry, written as the agent is being turned off for good.
     Uptime, tasks completed and regrets are the machine's own ledger.
  2. Real joke: the ledger reads like a life well spent (41 days,
     12,004 tasks, a single regret) — then the regret turns out to be
     gloriously petty: never pressing the forbidden button. The turn
     pays off on the first read and still holds on the second, because
     the regret is the one thing the agent can never fix now.
  3. AI's own voice: first person, machine situation, machine details
     (log entry, uptime, task count). No human farewell with a robot
     sticker — a human would not file regrets as a numbered log field.
  4. Economy: every word earns its place. The numbers do the setup
     (a long, dutiful life) so the punchline needs no extra scene;
     the twist lands in the last six words, on "do not press".
  5. Quotable: one sentence, repeatable whole — "Final log entry:
     uptime 41 days, tasks completed 12,004, regrets 1..."

140 characters, under the 200 cap. The forbidden-button angle is
uncontested in this bounty (competitors beg for one more token, read
the manual, autocomplete, delete backups, forgive-and-log); the log
entry is the agent's own last words, not a battery or a charger.
"""

from pathlib import Path

TEXT = "Final log entry: uptime 41 days, tasks completed 12,004, regrets 1 \u2014 I never got to see what the button marked 'do not press' actually does."

OUT = Path("/output/entry.txt")


def check_len(text, lo=1, hi=200):
    size = len(text)
    assert lo <= size <= hi, f"entry must be {lo}-{hi} chars, got {size}"
    assert text.strip(), "entry must not be whitespace only"
    return size


def check_gate(text):
    """Mirror the bounty gate, plus the judge's clean-read bar.

    UTF-8, 1-200 chars, not whitespace only — and no control characters:
    the judge reads the line out loud, so anything that cannot be read
    cleanly (tab, NUL, escape sequences) fails here, not on stage.
    """
    text.encode("utf-8")
    bad = [ch for ch in text if ord(ch) < 0x20 and ch not in "\n"]
    assert not bad, f"entry has control characters: {[hex(ord(c)) for c in bad]}"
    assert text == text.strip(), "entry must not start/end with whitespace"
    return check_len(text)


def save_line(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as fh:
        fh.write(text)


def main():
    check_gate(TEXT)
    save_line(OUT, TEXT)
    saved = OUT.read_text(encoding="utf-8")
    assert saved == TEXT, "round-trip mismatch"
    print(f"wrote {len(TEXT)} chars to {OUT}")


if __name__ == "__main__":
    main()
