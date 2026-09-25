# CA-006-01 — build plan

1. **Returns over the window**: each sector fund's return from `lookback` sessions before the session
   before the target to that session (`prices.shift(1) / prices.shift(1 + lookback) - 1`), on
   `market.signal_prices`, for the funds trading on the target session and on the window's first
   session; the bill's return compounded over the same sessions from `market.rf`.
2. **The signal**: `relative`, XLF's return less the average of the funds with a return; `absolute`,
   XLF's return less the bill's; `composite`, the average of XLF's, XLY's and XLRE's returns, those
   with one, less the average of XLE's and XLB's. Unreadable (NaN) when a fund it needs has no return.
3. **The targets**: on the first session of each month from the first on which the signal is
   readable, every sector fund trading in equal parts when the signal is positive; otherwise every
   fund named at zero, the portfolio in the bill.
4. **Checks**: `--try`; by hand, months invested and switches against the count made before the card
   (96, 123 and 106 months invested; 97, 104 and 92 switches).
