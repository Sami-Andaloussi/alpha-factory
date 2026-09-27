# CA-011-01 — Build plan

The card is locked (`card: CA-011-01-six-stage-sector-rotation`). One function,
`positions(market, average, holdings)`, in four steps, each commented in `strategy.py` by its number.

1. **The weeks**: the first session of each week, where the ISO year and week differ from the
   previous session's.
2. **The trends**: for IEF, SPY and DBC, the mean of the last `average` signal closes up to and
   including the session before, and whether the close of the session before stands above it, read
   from the signal prices whether the fund trades or not. No mean before `average` closes exist.
3. **The stage**: from the three signs, Pring's stage 1 to 6, or out of sequence, as the card lists
   them; no stage while any of the three means is missing.
4. **The targets**: on each week's first session with a stage, the funds the card names for that
   stage under `holdings` that trade share the portfolio equally; stage 6 under "assets" holds
   nothing; out of sequence, the sector funds that trade ("sectors") or all the funds that trade
   ("all", "assets"); if none of the funds named trades, zero on every fund. NaN on every other
   session, so that positions drift.

Why in this order: steps 2 and 3 are the card's stage, step 4 its holdings. Nothing is estimated;
nothing reads beyond the session before. The earliest read is the close `average` sessions before
the session before, 300 for the largest neighbour, within the card's memory of 301. Before the run,
`python -m lab.report --try` checks gate 1's timing for the three variants, ten dates for each
neighbour, and the memory. The clause and the reported measures are computed apart from the
battery, after the run, by the lab's engine at its costs, on the variant "sectors" against the
sector funds in equal parts.
