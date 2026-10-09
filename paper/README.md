# Paper trading

Gate 8 of the lab: after every US close, each strategy under paper trading sets its targets for
the next session on a paper account, and its live signal is compared with the backtest's signal
for the same session once that session's close is known. Gate 8 asks for identical signals over
two to four weeks. A test of the chain is a strategy traded only to prove the job, not a
survivor.

| Strategy | Role | Since | Sessions | Signals identical | Return |
|---|---|---|---|---|---|
| TM-017-01-time-series-momentum | test of the chain | 2026-09-25 | 11 | 9 of 10 | +0.14% |

## TM-017-01-time-series-momentum

| Session | Targets | Signals identical so far | Account |
|---|---|---|---|
| 2026-09-25 | holds | 0 of 0 | 100,000.00 |
| 2026-09-28 | holds | 1 of 1 | 100,000.00 |
| 2026-09-29 | holds | 2 of 2 | 100,000.00 |
| 2026-09-30 | holds | 3 of 3 | 100,000.00 |
| 2026-10-01 | cash | 4 of 4 | 100,000.00 |
| 2026-10-02 | holds | 4 of 5 (gaps: 2026-10-01) | 100,000.00 |
| 2026-10-05 | holds | 5 of 6 (gaps: 2026-10-01) | 100,000.00 |
| 2026-10-06 | holds | 6 of 7 (gaps: 2026-10-01) | 100,000.00 |
| 2026-10-07 | holds | 7 of 8 (gaps: 2026-10-01) | 100,000.00 |
| 2026-10-08 | holds | 8 of 9 (gaps: 2026-10-01) | 100,000.00 |
| 2026-10-09 | holds | 9 of 10 (gaps: 2026-10-01) | 100,000.00 |
