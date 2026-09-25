# SC-016-01 — Build plan

The card is locked (`card: SC-016-01-rosh-hashanah-to-yom-kippur`). The code follows it step by
step, in `strategy.py`, one function `positions(market, days)`.

1. **Rosh Hashanah's first day**, from the Hebrew calendar's rules alone, with integer arithmetic
   and no library: the days elapsed from the calendar's epoch to 1 Tishri of a Hebrew year, from the
   mean conjunction (the molad) of Tishri, 29 days, 12 hours and 793 parts (of 1,080 an hour) a
   month, with the postponements that keep the new year off Sunday, Wednesday and Friday and push it
   past a conjunction at or after noon; then the correction that keeps a year's length within the
   calendar's six lengths. The day is placed on the Gregorian calendar through Python's proleptic
   ordinals: the Hebrew epoch is day −1,373,427. Gregorian year `g`'s autumn holds Hebrew year
   `g + 3761`. Checked against the published dates of 2005 to 2025 (step 5).
2. **The calendar of scheduled sessions**, as SC-014-01 and SC-009-01 built it: weekdays less the
   New York Stock Exchange's holidays by rule, from 45 days before the market's first session to 62
   days after its last, read from no price.
3. **The window**: for each Gregorian year from the calendar's first to its last, the scheduled
   sessions after the last scheduled session before Rosh Hashanah's first day and up to the last
   scheduled session before the day `days` calendar days after it; a year whose sessions do not
   reach the window's end is left out, since the calendar runs two months past the market.
4. **The targets**: on each session of the market, whether the next scheduled session is in the
   window; the five funds in equal parts among those that trade when it is not, nothing when it is;
   a target only on the sessions on which the state changes, and on the first. The state of a
   session is read from the calendar alone, so the targets read no price.
5. **Checks before the run**, by `python -m lab.report --try`: gate 1's timing for the base and ten
   dates for each neighbour. The Rosh Hashanah dates are checked in the verdict's after-script
   against the published dates, which the reasoning lists by their windows.

The after-script that computes the clause and the reported measures is written after the run, in
the verdict's folder notes, reading the market's closes, the bill's rate and the snapshot's volumes;
it reuses this file's calendar functions so that the windows are the strategy's.
