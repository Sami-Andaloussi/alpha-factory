# SC-010-01 — The equity funds over the first half of the trading month: verdict

**Not run.** The commit that locked this card held a card whose prediction had lost a line break in
an edit, so that it did not parse. The lab's check refused it, but its refusal was piped away and did
not stop the commit. The line break was restored in a second commit, and the run then refused the
card: a card changed after its lock is a new card. It has no trial and counts in no gate.

The hypothesis, unchanged, runs as
[SC-010-02](../SC-010-02-first-half-of-the-month/verdict.md), which names this card as its parent.
The code committed here, SC-008-01's unchanged, was never run.

## What was learned

- **About the lab.** A refusal that does not stop the next step is no barrier. The hook
  `tools/hooks/pre-commit` now runs the check on every card a commit stages and stops the commit it
  refuses.
