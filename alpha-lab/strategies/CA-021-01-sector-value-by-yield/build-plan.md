# CA-021-01 — Build plan

One function, `positions(market, months, measure)`, in five steps, each commented in `strategy.py`
by its number, and a helper, `trailing_yield`, that reads one fund's yield on one target. The
construction is CA-024-01's on its sector group, the ranking on the yield, highest first.

1. **The targets' sessions**: the first session of each month, the market's first session left
   out, since a target reads the session before it.
2. **The trailing yield**, on each target's session t for each fund, from `signal_prices` and
   `signal_distributions` up to row t−1, never row t:
   - the window: the sessions after the same calendar date `months` months before t−1 (the month's
     last day where that date does not exist, as `pd.DateOffset` gives it) and up to t−1;
   - ranked or not: a fund whose reading starts after the window's first day is not ranked; a run
     of NaN that ends on t−1, a distribution not yet confirmed as the bars stood, counts as none;
     any other NaN in the window leaves the fund unranked;
   - each distribution given in the window, on its row c_j, a fraction f_j of the close before its
     ex-date: its cash over the close of t−1 is `f_j × A(c_j − 1) / A(t−1) / Π(1 − f_k)` over that
     distribution and every later one given up to t−1, the card's formula, summed over the window
     and annualised by 12/`months`; a close missing makes the yield NaN, the fund unranked.
3. **The score**: with `measure` "level" the yield; with "own" the yield over its mean on the sixty
   targets up to this one, all sixty read.
4. **The weights**: of the N funds trading, the n ranked hold n/N, split equally among the top third
   of their scores, rounded, one at least, ties broken by the funds' order (`method="first"`); a fund
   trading but not ranked holds 1/N.
5. **The targets**: from the first month in which a fund is ranked, on every first session of a
   month, every fund named, NaN elsewhere; the funds drift with prices between them. From then the
   portfolio is always fully invested, a month with no fund ranked holding each trading fund at
   1/N.

Why in this order: the dates, then what each fund paid, then the score, then the choice and the
weights, then the dates the targets hold, as CA-024-01. The yield is computed one fund and one
target at a time, in numpy, some 2,600 small sums a call, a fifth of a second. Before the run, the
counts of targets and decisions are compared with those made before the card, on the signal alone:
the base's 203 targets from 2006-02-01 and 33 clustered decisions, the variant's 144 from 2011-01-03
and 47, the neighbours' 35, 37, 40 and 24; the weights the pre-card count made are matched
exactly. `--try` checks the timing and the declared memory of 1,530 sessions.
